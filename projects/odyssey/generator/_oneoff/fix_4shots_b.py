# ⛔ これは 2026-09-29 の一度きりの編集であり、**履歴であって道具ではない。**
#    **当てた結果は `../content/` に入っている。再実行してはならない**——
#    当てる相手（古い文字列）は、もう存在しない。
# -*- coding: utf-8 -*-
"""s12 の §15/§6/§7/§4 に残った「彼は枠に居ない」の残りと、s13/s14 の §19 の一行。"""
import io, sys, pathlib

EDITS = []


def add(path, old, new):
    EDITS.append((path, old, new))


S12 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s12.py")
S13 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s13.py")
S14 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s14.py")

add(S12, r'''     extra_must="**この1本に人物は居ないが、同一性の塊は §18 の `Visual Prompt` と `Master Prompt` の"
                "両方にまるごと入る**——**それは作品の錠であり、この枠の中身ではない。**"
                "⚠️ **ゆえにこの1本も、`s05` が立てた顔から外れてはならない。**",''',
    r'''     extra_must="**この1本の人物は、最初のビートだけ枠に居る**——**同一性の塊は §18 の `Visual Prompt` と"
                "`Master Prompt` の両方にまるごと入る**（`has_man: True`）。"
                "⚠️ **ゆえにこの1本も、`s05` が立てた顔から外れてはならない。**",''')

add(S12, r'''"同じ一つの海である。** ⚠️ **彼は岸に居て、枠に入らない。**",''',
    r'''"同じ一つの海である。** ⚠️ **彼は岸に居て、最初のビートのあいだに枠の外へ出る。**",''')

add(S12, r'''"**人は一人も枠に居ない**（`shot.aim` の逐語:''',
    r'''"**彼は最初のビートで枠の外へ出るので、残るのは海の画だけである**（`shot.aim` の逐語:''')

add(S12, r'''"最初のビートは「彼がもう居ない」ことの確認に払われる。**"''',
    r'''"最初のビートは、彼が枠の外へ出ることに払われる。**"''')

add(S12, r'''   "core": "**海が、彼の見ているものをそのまま返す** — 見ている者を一度も写さずに、「見ている」が立つ。",''',
    r'''   "core": "**海が、彼の見ているものをそのまま返す** — 見ている者は去り、海だけが「見ている」を立たせる。",''')

add(S12, r'''   "Atmosphere": "The hour in which the gaze is in the frame and the one gazing is not.",''',
    r'''   "Atmosphere": "The hour in which the gaze is in the frame and the one gazing goes out of it.",''')

for p in (S13, S14):
    add(p, r'''                        "既定で何も添付しない）。⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ**"
                        "——⛔ **この1本に人物は居ないので、同一性の塊は §18 に入らない**（`has_man: False`）"''',
        r'''                        "既定で何も添付しない）。⛔ **この1本の §18 は人物の同一性を運ばない**"
                        "——**人物がこの枠に居ないためである**（`has_man: False`）"''')

srcs = {}
for path in (S12, S13, S14):
    srcs[path] = io.open(path, encoding="utf-8").read()

bad = []
for i, (path, old, new) in enumerate(EDITS):
    n = srcs[path].count(old)
    if n != 1:
        bad.append((i, path, n, old.splitlines()[0][:90]))
if bad:
    print("=== 当たらないパターン ===")
    for i, path, n, head in bad:
        print("%3d %s count=%d  %s" % (i, path.split("/")[-1], n, head))
    sys.exit(1)

for path, old, new in EDITS:
    srcs[path] = srcs[path].replace(old, new, 1)

for path, text in srcs.items():
    io.open(path, "w", encoding="utf-8").write(text)

print("applied %d edits" % len(EDITS))
