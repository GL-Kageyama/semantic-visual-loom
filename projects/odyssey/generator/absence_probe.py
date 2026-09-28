# -*- coding: utf-8 -*-
"""Measure: which specs put the identity block AND a person-absence claim in the same slot?"""
import re, pathlib, lit

ROOT = pathlib.Path(__file__).resolve().parents[3]

# ⛔ **`ROOT` がリポジトリの根を指しているかを、読む前に確かめる。**
#    ⚠️ **2026-09-29**: `parents[3]` を `parents[2]` と誤ると `ROOT` は `<repo>/projects` を指し、
#    この道具は**別の木を読んで、それらしい数を出す**——`verify.py` は「31 specs」と言った。
#    ⚠️ **黙って別の木を読むより、落ちるほうがよい。**
assert (ROOT / "CLAUDE.md").is_file() and (ROOT / "projects" / "odyssey").is_dir(), (
    "ROOT がリポジトリの根を指していない: %s" % ROOT)
SPECS = sorted((ROOT / "projects/odyssey/specs/video").glob("odyssey-s*.md"))

def slot(text, name):
    m = re.search(r"^## %s\s*\n(.*?)(?=\n## |\n---\s*\n# |\Z)" % re.escape(name), text, re.S | re.M)
    return m.group(1).strip("\n") if m else ""

# a deliberately broad net — every sentence in the slot that talks about nobody being there
NET = re.compile(r"[^.!?]*\b(no (?:figure|person|human|man|one|body)|nobody|not a (?:living )?(?:figure|person|soul)|empty of (?:people|figures)|without (?:a )?(?:person|figure|human))\b[^.!?]*[.!?]", re.I)

for p in SPECS:
    t = p.read_text(encoding="utf-8")
    b18 = t.split("# 18. SEEDANCE 2.5 PROMPT MAPPING", 1)[1].split("\n---\n", 1)[0]
    for s in ("Master Prompt", "Visual Prompt"):
        body = slot(b18, s)
        has_id = lit.IDENTITY in body
        hits = NET.findall(body)
        sents = [m.group(0).strip() for m in NET.finditer(body)]
        if has_id and sents:
            print("=== %s / %s   (identity: YES)" % (p.stem, s))
            for x in sents:
                print("      %s" % x[:170])
