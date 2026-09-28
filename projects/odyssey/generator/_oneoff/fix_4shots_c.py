# ⛔ これは 2026-09-29 の一度きりの編集であり、**履歴であって道具ではない。**
#    **当てた結果は `../content/` に入っている。再実行してはならない**——
#    当てる相手（古い文字列）は、もう存在しない。
# -*- coding: utf-8 -*-
"""人物の居ない s13/s14/s15 の Visual Prompt から、布と肌の材質を落とす（s23 と同じ手当て）。

`K.VISUAL_META` の材質の列は、この作品では人物の布と肌を名指す——
人物の居ない枠にそれを貼れば、塊と同じ形の残り方になる（s23 は既に外している。
s26・s28 は自前の visual_meta を書いて「no skin and no cloth」と明記している）。
"""
import io, sys, pathlib

EDITS = []


def add(path, old, new):
    EDITS.append((path, old, new))


S13 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s13.py")
S14 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s14.py")
S15 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s15.py")

add(S13, r''' "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones",
   "a dark island outline over coarse dark sand and wet shingle, read as outline only").replace(
   "warm ochre where the low sun falls",
   "cold white held in the one reflected path on the black water") + (''',
    r''' "visual_meta": K.VISUAL_META.replace(
   "Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked; ",
   "**no skin and no cloth anywhere in this frame**: ").replace(
   "wet shingle with individual stones",
   "a dark island outline over coarse dark sand and wet shingle, read as outline only").replace(
   "warm ochre where the low sun falls",
   "cold white held in the one reflected path on the black water") + (''')

add(S14, r''' "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones",
   "barked raw pine logs and hand-twisted cordage, awash at the edges").replace(
   "warm ochre where the low sun falls",
   "cold white held in the one reflected path on the black water") + (''',
    r''' "visual_meta": K.VISUAL_META.replace(
   "Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked; ",
   "**no skin and no cloth anywhere in this frame**: ").replace(
   "wet shingle with individual stones",
   "barked raw pine logs and hand-twisted cordage, awash at the edges").replace(
   "warm ochre where the low sun falls",
   "cold white held in the one reflected path on the black water") + (''')

add(S15, r'''   + K.VISUAL_META.replace(
     "wet shingle with individual stones",
     "the water's surface broken into fine facets, running").replace(
     "warm ochre where the low sun falls",
     "cold white held in the one unbroken reflected path of the stars") + (''',
    r'''   + K.VISUAL_META.replace(
     "Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked; ",
     "**no skin and no cloth anywhere in this frame**: ").replace(
     "wet shingle with individual stones",
     "the water's surface broken into fine facets, running").replace(
     "warm ochre where the low sun falls",
     "cold white held in the one unbroken reflected path of the stars") + (''')

srcs = {}
for path in (S13, S14, S15):
    srcs[path] = io.open(path, encoding="utf-8").read()

bad = []
for i, (path, old, new) in enumerate(EDITS):
    n = srcs[path].count(old)
    if n != 1:
        bad.append((i, path, n, old.splitlines()[0][:80]))
if bad:
    for i, path, n, head in bad:
        print("%3d %s count=%d %s" % (i, path.split("/")[-1], n, head))
    sys.exit(1)

for path, old, new in EDITS:
    srcs[path] = srcs[path].replace(old, new, 1)

for path, text in srcs.items():
    io.open(path, "w", encoding="utf-8").write(text)

print("applied %d edits" % len(EDITS))
