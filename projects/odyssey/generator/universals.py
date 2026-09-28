# -*- coding: utf-8 -*-
"""Find every claim in the written specs whose scope is the whole work.

⚠️ Copied verbatim from verify.py's lesson: a scan keyed on the PHRASE I expect misses the
variant. s09's denial used a different verb; the batch-E instruction keyed on "every sea shot"
and therefore never saw s03's "every shot of this work". So this keys on the CLASS — a
quantifier whose scope is the work — and prints every hit for a human to read.
"""
import re, pathlib, collections

SPECS = sorted((pathlib.Path(__file__).resolve().parent.parent / "specs" / "video").glob("odyssey-s*.md"))

# A quantifier over shots/this work. Deliberately loose: false negatives are the failure mode
# that already bit twice, false positives cost only reading time.
Q = re.compile(
    r"\b(every|all|each|any|no|never|always|none)\b[^.!?\n]{0,90}?"
    r"\b(shot|shots|take|takes|frame|frames|specification|specifications|"
    r"this work|the work|this video|the sea|the shore|the island)\b", re.I)

seen = collections.defaultdict(list)
for p in SPECS:
    for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        # Only prose claims: skip the headings and the template-owned invariant strings we
        # already know are cross-spec identical (the L10/L26 constants and the block).
        for m in re.finditer(r"[^.!?\n]{0,160}\b(?:every|all|each|any|no|never|always|none)\b[^.!?\n]{0,160}", line):
            s = m.group(0).strip()
            if not Q.search(s):
                continue
            seen[s].append("%s:%d" % (p.stem.replace("odyssey-", ""), i))

print("全称の候補: %d 種 / 出現 %d 箇所\n" % (len(seen), sum(len(v) for v in seen.values())))
for s, where in sorted(seen.items(), key=lambda kv: -len(kv[1])):
    mark = "★%d本" % len(where) if len(where) > 1 else " 1本"
    print("%s  %s" % (mark, " ".join(sorted(set(where)))))
    print("      %s" % (s[:200] + ("…" if len(s) > 200 else "")))
