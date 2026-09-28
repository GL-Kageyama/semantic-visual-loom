# -*- coding: utf-8 -*-
"""Verify the invariants the checks read, across every spec written so far.

The checker knows about §18 as a whole; this knows about the two strings L10 compares, the four
constants L26 reads, the seven slots L17 requires, and the identity block that 裁定② leaves as
the only lock. Run it after every batch.
"""
import re
import sys
import pathlib

import lit

ROOT = pathlib.Path(__file__).resolve().parents[3]

# ⛔ **`ROOT` がリポジトリの根を指しているかを、読む前に確かめる。**
#    ⚠️ **2026-09-29**: `parents[3]` を `parents[2]` と誤ると `ROOT` は `<repo>/projects` を指し、
#    この道具は**別の木を読んで、それらしい数を出す**——`verify.py` は「31 specs」と言った。
#    ⚠️ **黙って別の木を読むより、落ちるほうがよい。**
assert (ROOT / "CLAUDE.md").is_file() and (ROOT / "projects" / "odyssey").is_dir(), (
    "ROOT がリポジトリの根を指していない: %s" % ROOT)
SPECS = sorted((ROOT / "projects/odyssey/specs/video").glob("odyssey-s*.md"))
CJK = re.compile(r"[぀-ヿ一-鿿]")
bad = []


def slot(text, name):
    m = re.search(r"^## %s\s*\n(.*?)(?=\n## |\n---\s*\n# |\Z)" % re.escape(name), text, re.S | re.M)
    return m.group(1).strip("\n") if m else None


print("%-12s %-18s %6s %5s %5s %5s %5s" % ("shot", "format", "lines", "neg", "sty", "cst", "idblk"))
for p in SPECS:
    t = p.read_text(encoding="utf-8")
    name = p.stem
    fmt = re.search(r"^- REF_FORMAT: `([^`]+)`", t, re.M)
    fmt = fmt.group(1) if fmt else "?"
    neg = slot(t, "Negative Prompt")
    sty = re.sub(r"\n\(Source:.*$", "", slot(t, "Style Motion") or "", flags=re.S).strip("\n")
    m18 = re.search(r"^# 18\. SEEDANCE 2\.5 PROMPT MAPPING", t, re.M)
    body18 = t.split("# 18. SEEDANCE 2.5 PROMPT MAPPING", 1)[1].split("\n---\n", 1)[0] if m18 else ""
    slots = {s: slot(body18, s) for s in
             ("Master Prompt", "Visual Prompt", "Motion Prompt", "Camera Prompt",
              "Audio Prompt", "Negative Prompt", "Style Motion")}
    missing = [s for s, v in slots.items() if v is None]
    if missing:
        bad.append("%s: missing slots %s" % (name, missing))
    if neg != lit.NEGATIVE:
        bad.append("%s: §18 Negative Prompt differs from the work's single line" % name)
    if sty != lit.STYLE_MOTION:
        bad.append("%s: §18 Style Motion differs from the work's" % name)
    if lit.CONST not in t:
        bad.append("%s: the four work constants are not verbatim (L26)" % name)
    d = re.search(r"^- Duration: `([0-9.]+)s`$", t, re.M)
    if not d:
        bad.append("%s: no §1 Duration line (L23)" % name)
    for s, v in slots.items():
        if v and CJK.search(v):
            bad.append("%s: CJK inside slot %s (the strings handed over are English)" % (name, s))
    idblk = sum(1 for s in ("Master Prompt", "Visual Prompt")
                if lit.IDENTITY in (slots.get(s) or ""))
    print("%-12s %-18s %6d %5s %5s %5s %5s" % (
        name, fmt, t.count("\n"),
        "ok" if neg == lit.NEGATIVE else "DIFF",
        "ok" if sty == lit.STYLE_MOTION else "DIFF",
        "ok" if lit.CONST in t else "DIFF",
        "%d/2" % idblk if idblk else "-"))

# ---------------------------------------------------------------------------
# The class of defect that 裁定⑤/⑥ ruled on (2026-09-29), checked here against the
# WRITTEN specs — independently of tpl.py's assertion, so that two different readers
# agree. Both directions are checked, because either one alone is a way to be wrong:
#   · the block in a slot that also denies anyone is there  → the prompt contradicts itself
#   · prose that points AT the block while the block is gone → a sentence pointing at nothing
#
# ⚠️ The distinction that makes this checkable: `no SECOND person` (or `he is the only
# person`) is a legitimate sentence from a shot he stands in. `no person` is a denial that
# the frame holds anyone. Only the second contradicts the block.
# ---------------------------------------------------------------------------
SECOND = r"(?:second|other|another|one other|any second)"
# ⛔ The qualifier sits AFTER the `no`, not before it — "no second person", never "second no person".
# The first version of this pattern had the two the wrong way round, so it never once fired and
# every "no second person" read as a denial of the man himself. Captured rather than looked behind
# because a look-behind must be fixed-width and "one other" makes this one variable-width.
# group(1) is None ⟺ the `no` denies anyone at all.
DENIES_ANYONE = re.compile(
    r"\bno\s+(?:(%s)\s+)?(?:person|figure|human|body)\b" % SECOND, re.I)
ONLY_HIM = re.compile(r"\b(?:he is|he's) the only (?:person|figure|human)\b", re.I)
POINTS_AT_BLOCK = re.compile(
    r"[^.!?\n]*(?:identity block (?:above|carried|the)|block above|"
    r"carried (?:here|above) as|continuity lock (?:above|carried))[^.!?\n]*", re.I)

contradictions, orphans = [], []
for p in SPECS:
    t = p.read_text(encoding="utf-8")
    b18 = t.split("# 18. SEEDANCE 2.5 PROMPT MAPPING", 1)[1].split("\n---\n", 1)[0]
    for s in ("Master Prompt", "Visual Prompt"):
        body = slot(b18, s) or ""
        has_block = lit.IDENTITY in body
        # Strip the "only him" sentences before asking whether anyone is denied.
        stripped = ONLY_HIM.sub("", body)
        # ⚠️ A denial inside a "nothing arrives / nothing changes" enumeration is a claim about
        # CHANGE, not about presence: s08's "no object, no figure, no light change" means nothing
        # alters, and he stands there throughout. Sentence-scope it so that reading survives.
        changed = re.sub(
            r"[^.!?\n]*\bnothing\b[^.!?\n]*\b(?:arrives|changes|moves|alters)\b[^.!?\n]*[.!?]",
            "", stripped, flags=re.I)
        # ⚠️ A qualifier carries down a list. s10's "No SECOND person is in this frame — no one at
        # the cave mouth, no figure inside the black, no companion, no crowd" denies a second person
        # four times, once per noun. Reading "no figure" there as a denial of the man himself would
        # be reading it out of its own sentence, so: inside one sentence, a qualified denial
        # qualifies every later denial in it.
        # ⚠️ Collapse whitespace BEFORE splitting: the specs are hard-wrapped, so splitting on a
        # newline cuts s10's sentence in two and strands its qualifier on the first line.
        denies = []
        for sent in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", changed)):
            qualified = None
            for m in DENIES_ANYONE.finditer(sent):
                if m.group(1) is not None:
                    qualified = m.start()
                elif qualified is None:
                    denies.append(m.group(0))
        if has_block and denies:
            contradictions.append("%s / %s: block + %r" % (p.stem, s, denies[0][:70]))
        pts = [m.group(0).strip() for m in POINTS_AT_BLOCK.finditer(body)]
        if pts and not has_block:
            orphans.append("%s / %s: %r" % (p.stem, s, pts[0][:70]))

print()
print("⚠️ 以下は候補である。**どちらが誤りかは、この道具には決められない**——")
print("   記録（`shots/*.yaml` の `unit`・`beats`）が彼を枠に置いているかを読むこと。")
print("   塊が誤り（彼が居ない）／文が誤り（彼は居る）の二種類が、同じ形で出る。")
print()
print("自己矛盾（塊 ＋ 誰も居ないと言う）: %d" % len(contradictions))
for x in contradictions:
    print("  " + x)
print("指す先の無い文（塊を指すが塊が無い）: %d" % len(orphans))
for x in orphans:
    print("  " + x)

if contradictions or orphans:
    bad += contradictions + orphans

print()
if bad:
    print("FAILURES (%d):" % len(bad))
    for b in bad:
        print("  " + b)
    sys.exit(1)
print("all invariants hold across %d specs" % len(SPECS))
