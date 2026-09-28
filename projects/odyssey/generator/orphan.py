# -*- coding: utf-8 -*-
"""Which specs contain prose that POINTS AT the identity block (and so is orphaned when it goes)?"""
import re, pathlib, lit

ROOT = pathlib.Path(__file__).resolve().parents[3]

# ⛔ **`ROOT` がリポジトリの根を指しているかを、読む前に確かめる。**
#    ⚠️ **2026-09-29**: `parents[3]` を `parents[2]` と誤ると `ROOT` は `<repo>/projects` を指し、
#    この道具は**別の木を読んで、それらしい数を出す**——`verify.py` は「31 specs」と言った。
#    ⚠️ **黙って別の木を読むより、落ちるほうがよい。**
assert (ROOT / "CLAUDE.md").is_file() and (ROOT / "projects" / "odyssey").is_dir(), (
    "ROOT がリポジトリの根を指していない: %s" % ROOT)
SPECS = sorted((ROOT / "projects/odyssey/specs/video").glob("odyssey-s*.md"))

POINTER = re.compile(
    r"[^.!?\n]*(?:identity block (?:above|carried|the)|block above|carried (?:here|above) as|"
    r"the lock above|continuity lock (?:above|carried)|lock carried (?:here|above))[^.!?\n]*[.!?]",
    re.I)

TEN = ["odyssey-s%d" % n for n in (12,13,14,15,26,28,29,30,31,32)]
print("%-12s %5s %5s  %s" % ("shot", "idblk", "ptr", "pointing sentences"))
for p in SPECS:
    t = p.read_text(encoding="utf-8")
    b18 = t.split("# 18. SEEDANCE 2.5 PROMPT MAPPING", 1)[1].split("\n---\n", 1)[0]
    def slot(name):
        m = re.search(r"^## %s\s*\n(.*?)(?=\n## |\n---\s*\n# |\Z)" % re.escape(name), b18, re.S | re.M)
        return m.group(1) if m else ""
    idblk = sum(1 for s in ("Master Prompt","Visual Prompt") if lit.IDENTITY in slot(s))
    ptr = []
    for s in ("Master Prompt","Visual Prompt"):
        ptr += [m.group(0).strip() for m in POINTER.finditer(slot(s))]
    mark = "◀ 10のうち" if p.stem in TEN else ""
    if idblk or ptr:
        print("%-12s %5s %5d  %s" % (p.stem, "%d/2"%idblk if idblk else "-", len(ptr), mark))
        for x in ptr:
            print("        · %s" % x[:150])
