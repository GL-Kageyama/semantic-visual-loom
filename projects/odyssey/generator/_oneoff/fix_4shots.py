# ⛔ これは 2026-09-29 の一度きりの編集であり、**履歴であって道具ではない。**
#    **当てた結果は `../content/` に入っている。再実行してはならない**——
#    当てる相手（古い文字列）は、もう存在しない。
# -*- coding: utf-8 -*-
"""2026-09-29 の裁定①②を受けた s12-s15 の直し。全パターンを先に検査してから当てる。"""
import io, sys, pathlib

EDITS = []  # (path, old, new)


def add(path, old, new):
    EDITS.append((path, old, new))


S13 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s13.py")
S14 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s14.py")
S15 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s15.py")
S12 = str(pathlib.Path(__file__).resolve().parents[1] / "content" / "s12.py")

# ============================== s13 =========================================
add(S13, '"has_man": True,', '"has_man": False,')

add(S13, r'''              "⚠️ **それでも、この仕様は同一性の塊を §18 に置いた**（`has_man: True`）——**作品の錠として"
              "であり、枠の中身としてではない。** **§20 を見る。**"]},''',
    r'''              "⚠️ **この1本は、同一性の塊を §18 に置かない**（`has_man: False`）——**人物がこの枠に"
              "居ない以上、人物の錠を貼れば、居ない者を貼ることになる**（2026-09-29 の裁定①）。"
              "**§20 を見る。**"]},''')

add(S13, r'''   "identity": K.identity(
     extra_must="**この1本に人物は居ないが、同一性の塊は §18 の `Visual Prompt` と `Master Prompt` の"
                "両方にまるごと入る**——**それは作品の錠であり、この枠の中身ではない。**"
                "⚠️ **ゆえにこの1本も、`s05` が立てた顔から外れてはならない。**",
     may="水面の細かさ、島の画面の中の大きさ、反射の道の幅、水平線の画面の中の高さ、砂の明るさ。"),''',
    r'''   "identity": "⚠️ **この1本に人が一人も居ないので、人物の同一性は掛からない。** "
               "**掛かるのは島と海の同一性である**——**島が一つであること、低く平らであること、"
               "水際の白い線があること、そして水と水平線が一つであること。** "
               "⛔ **`男.identity` は参照集合に在るが（§6）、この1本は同一性の塊を §18 に貼らない**"
               "——**人物が枠に居ないためである**（2026-09-29 の裁定①。§20 を見る）。"
               "**ゆえに `s05` が立てた顔は、この1本には要らない。**",''')

add(S13, ' "must_not": K.must_not_common(has_man=True, goddess_extra=(',
    ' "must_not": K.must_not_common(has_man=False, goddess_extra=(')

add(S13, r'''⚠️ **そしてこの1本の枠に、筏の一部も入らない**（§16 の下の項を見る）。",
 ],''',
    r'''⚠️ **そしてこの1本の枠に、筏の一部も入らない**（§16 の下の項を見る）。",
   "⚠️ **この1本に男は居ないが、`男.negatives` は参照集合に在る**（§6）——**彼の禁制はこの1本でも"
   "掛かる**（逐語:「no muscular hero's body, no heroic pose, no heroic lighting」・"
   "「no youthful face, no beardless face, no clean or unlined skin」・「no armour, no helmet, "
   "no greaves, no shield」）。⚠️ **ここでは、それが「人を一人も置かないこと」として効く。**",
 ],''')

add(S13, r'''   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.** ⚠️ **この1本に彼は居ないが、塊は作品の錠である。**",''',
    r'''   "⚠️ **同一性の塊を §18 に貼らないこと** — **人物が枠に居ないので、この1本は人物の錠を運ばない**"
   "（`has_man: False`。2026-09-29 の裁定①）。**§20 を見る。**",''')

add(S13, '   "**The identity block pasted into §18 is preserved clause by clause.**",',
    '   "⚠️ **同一性の塊を §18 に置かないこと** — **人物が枠に居ないためである**（2026-09-29 の裁定①）。",')

add(S13, r'''one steers anything here.**\n\n"
   "**The identity lock of this work, carried here for continuity across all thirty-four shots: "
   "{IDENTITY}** **In this shot that lock is the work's, not the frame's: the frame holds the water, the "
   "horizon and, for as long as it lasts, the island — and nothing with a body in it.**\n\n"''',
    r'''one steers anything here.**\n\n"''')

add(S13, r'''   " ⚠️ **The identity block above belongs to this work's continuity and not to the contents of this "
   "frame: no person is in this frame at any moment.** ⚠️ **The island is low and level, with no peak and "''',
    r'''   " ⚠️ **No person is in this frame at any moment.** "
   "⚠️ **The island is low and level, with no peak and "''')

add(S13, r'''                        "——**この1本に人物は居ないが、塊は両方に入る**（`has_man: True`。§20 を見る）。",''',
    r'''                        "——⛔ **この1本に人物は居ないので、同一性の塊は §18 に入らない**（`has_man: False`）"
                        "——**`Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は書かれていない。**"
                        "⚠️ **`男.negatives` は参照集合に在る**——**ゆえに §16 は彼の禁制も運ぶ**（§20 を見る）。",''')

add(S13, r'''   "⛔ **この1本の画面に人物が居ないこと。** 記録の `unit`・`motion.subject`・ビートは彼を一度も名指さず、"
   "**`s18` の記録は「この作品で初めて、男が水の上に居る」と書く**——**曲順で `s18`（`l16`）は"
   "この1本（`l10`）より後である。** ⚠️ **しかし参照集合は `男.identity` と `男.negatives` を挙げ、"
   "他の2本（`s14`・`s15`）と同じ8鍵である。** ⚠️ **この仕様は、塊を作品の錠として §18 に置き、"
   "枠の中身としては置かなかった。****`has_man: False` にすれば、塊は §18 から消える**"
   "——**どちらが正かは著者が決める。**",''',
    r'''   "✅ **裁定（2026-09-29）: この1本は人物を枠に置かず、同一性の塊も §18 に貼らない**（`has_man: False`）"
   "——**記録の `unit`・`motion.subject`・ビートが彼を一度も名指さないためである。** "
   "⚠️ **この仕様は裁定の前、塊を作品の錠として §18 に置いていた**——**裁定①がそれを落とした。** "
   "⛔ **ゆえに `Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は無い。** "
   "⚠️ **`男.negatives` は参照集合に在るので、§16 は彼の禁制を運び続ける。**",''')

add(S13, r'''**曲順で `s18`（`l16`）はこの1本（`l10`）より後である。**
⚠️ **この仕様のショット記録は `shots/odyssey-s13.yaml` である。**''',
    r'''**曲順で `s18`（`l16`）はこの1本（`l10`）より後である。**
⛔ **2026-09-29 の裁定①: この1本は同一性の塊を §18 に貼らない**（`has_man: False`。§20 を見る）。
⚠️ **この仕様のショット記録は `shots/odyssey-s13.yaml` である。**''')

# ============================== s14 =========================================
add(S14, '"has_man": True,', '"has_man": False,')

add(S14, r'''              "⚠️ **それでも、この仕様は同一性の塊を §18 に置いた**（`has_man: True`）"
              "——**作品の錠としてであり、枠の中身としてではない。**"]},''',
    r'''              "⚠️ **この1本は、同一性の塊を §18 に置かない**（`has_man: False`）——**枠に居ない者の錠を"
              "貼れば、居ない者を貼ることになる**（2026-09-29 の裁定①）。**§20 を見る。**"]},''')

add(S14, r'''   "identity": K.identity(
     extra_must="**この1本の枠に彼は居ないが、同一性の塊は §18 の `Visual Prompt` と `Master Prompt` の"
                "両方にまるごと入る**——**それは作品の錠であり、この枠の中身ではない。**"
                "⚠️ **ゆえにこの1本も、`s05` が立てた顔から外れてはならない。**",
     may="舳先の画面の中の高さ、水の被り方、丸太の濡れ方、航跡の長さ、反射の道の割れ方。"),''',
    r'''   "identity": "⚠️ **この1本に人が一人も居ないので、人物の同一性は掛からない。** "
               "**掛かるのは筏と海の同一性である**——**丸太と手縒りの縄、低さ、竜骨・肋・甲板張り・"
               "欄が無いこと、そして帆がまだ張られていないこと。** "
               "⛔ **`男.identity` は参照集合に在るが（§6）、この1本は同一性の塊を §18 に貼らない**"
               "——**舵を取る者はカメラの後ろに居る**（2026-09-29 の裁定①。§20 を見る）。",''')

add(S14, ' "must_not": K.must_not_common(has_man=True, goddess_extra=(',
    ' "must_not": K.must_not_common(has_man=False, goddess_extra=(')

add(S14, r'''**禁じられているのは船体・竜骨・甲板張り・欄であり、この1本の丸太と縄ではない。**",
 ],''',
    r'''**禁じられているのは船体・竜骨・甲板張り・欄であり、この1本の丸太と縄ではない。**",
   "⚠️ **この1本に男は居ないが、`男.negatives` は参照集合に在る**（§6）——**彼の禁制はこの1本でも"
   "掛かる**（逐語:「no muscular hero's body, no heroic pose, no heroic lighting」・"
   "「no youthful face, no beardless face, no clean or unlined skin」・「no armour, no helmet, "
   "no greaves, no shield」）。⚠️ **ここでは、それが「手も、肩も、後ろ姿も入れないこと」として効く。**",
 ],''')

add(S14, r'''   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.** ⚠️ **この1本に彼は居ないが、塊は作品の錠である。**",''',
    r'''   "⚠️ **同一性の塊を §18 に貼らないこと** — **枠に居ない者の錠を貼らないためである**"
   "（`has_man: False`。2026-09-29 の裁定①）。**§20 を見る。**",''')

add(S14, '   "**The identity block pasted into §18 is preserved clause by clause.**",',
    '   "⚠️ **同一性の塊を §18 に置かないこと** — **枠に居ないためである**（2026-09-29 の裁定①）。",')

add(S14, r'''   "**The identity lock of this work, carried here for continuity across all thirty-four shots: "
   "{IDENTITY}** **In this shot that lock is the work's, not the frame's: the man steers from the stern, "
   "which is behind the camera, and he is not seen at any moment. This raft is not an empty one.**\n\n"''',
    r'''   "**The raft is not an empty one: the man who built it steers it from the stern, which is behind "
   "the camera, and he is not seen at any moment.**\n\n"''')

add(S14, r'''   " ⚠️ **The identity block above belongs to this work's continuity and not to the contents of this "
   "frame: no person is in this frame at any moment — whoever steers is aft of the camera.** "''',
    r'''   " ⚠️ **No person is in this frame at any moment — whoever steers is aft of the camera.** "''')

add(S14, r'''                        "——**この1本に人物は居ないが、塊は両方に入る**（`has_man: True`。§20 を見る）。",''',
    r'''                        "——⛔ **この1本に人物は居ないので、同一性の塊は §18 に入らない**（`has_man: False`）"
                        "——**`Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は書かれていない。**"
                        "⚠️ **`男.negatives` は参照集合に在る**——**ゆえに §16 は彼の禁制も運ぶ**（§20 を見る）。",''')

add(S14, r'''   "⛔ **舵を取る者の扱い。** 記録の `unit`・ビート・`motion.subject` は、**彼を一度も名指さない。**"
   "そして **`s18` の記録は「この作品で初めて、男が水の上に居る」と書く**——**曲順で `s18`（`l16`）は"
   "この1本（`l11`）より後である。** ⚠️ **しかし参照集合は `男.identity` と `男.negatives` を挙げ、"
   "他の2本（`s13`・`s15`）と同じ8鍵である。** ⚠️ **この仕様は、彼を船尾（カメラの後ろ）に置き、"
   "枠には入れなかった**——**無人にはできないからである**（`s21` の註の逐語:「**この作品の筏は"
   "彼が作ったものであり、空の筏は嘘である。**」）。**他の読み（彼を枠に入れる／筏を無人のまま置く）も"
   "成り立つ。****どちらが正かは著者が決める。**",''',
    r'''   "✅ **裁定（2026-09-29）: この1本は人物を枠に置かず、同一性の塊も §18 に貼らない**（`has_man: False`）"
   "——**記録の `unit`・ビート・`motion.subject` が彼を一度も名指さないためである。** "
   "⚠️ **この仕様は裁定の前、彼を船尾（カメラの後ろ）に置き、塊を作品の錠として §18 に置いていた**"
   "——**裁定①が塊を落とした。****ゆえに `{IDENTITY}` は §18 に無い。** "
   "⚠️ **それでも筏は無人ではない**（`s21` の註の逐語:「**この作品の筏は彼が作ったものであり、"
   "空の筏は嘘である。**」）——**この読みは裁定のあとも変わっていない。**",''')

# ============================== s15 =========================================
add(S15, '_MN = K.must_not_common(has_man=True, goddess_extra=(',
    '_MN = K.must_not_common(has_man=False, goddess_extra=(')

add(S15, '"has_man": True,', '"has_man": False,')

add(S15, r'''              "⚠️ **それでも、この仕様は同一性の塊を §18 に置いた**（`has_man: True`）"
              "——**作品の錠としてであり、枠の中身としてではない。**"]},''',
    r'''              "⚠️ **この1本は、同一性の塊を §18 に置かない**（`has_man: False`）——**人物がこの枠に"
              "居ない以上、人物の錠を貼れば、居ない者を貼ることになる**（2026-09-29 の裁定①）。"
              "**§20 を見る。**"]},''')

add(S15, r'''   "identity": K.identity(
     extra_must="**この1本の枠に人は一人も居ないが、同一性の塊は §18 の `Visual Prompt` と "
                "`Master Prompt` の両方にまるごと入る**（`has_man: True`）——"
                "**それは作品の錠であり、この枠の中身ではない。** ⚠️ **ゆえにこの1本も、"
                "`s05` が立てた顔から外れてはならない。** ⚠️ **しかしこの1本の画には、"
                "その顔を置く場所が無い。**",
     may="水面の細かさ、反射の道の位置、水平線の画面の中の高さ、そして引ききったあとの画角。"),''',
    r'''   "identity": "⚠️ **この1本に人が一人も居ないので、人物の同一性は掛からない。** "
               "**掛かるのは水と、光と、空の同一性である**——**同じ一つの水であること、"
               "同じ一つのグレードであること、二つのあいだに分割線を引かないこと。** "
               "⛔ **`男.identity` は参照集合に在るが（§6）、この1本は同一性の塊を §18 に貼らない**"
               "——**貼れば、この枠に居ない者を貼ることになる**（2026-09-29 の裁定①）。"
               "⚠️ **この形式の `BEARER` は光であり、人ではない**（§3 と §6 を見る）。",''')

add(S15, r'''   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.** ⚠️ **この1本に人は居ないが、塊は作品の錠である。**",''',
    r'''   "⚠️ **同一性の塊を §18 に貼らないこと** — **人物が枠に居ないので、この1本は人物の錠を運ばない**"
   "（`has_man: False`。2026-09-29 の裁定①）。**§20 を見る。**",''')

add(S15, '   "**The identity block pasted into §18 is preserved clause by clause.**",',
    '   "⚠️ **同一性の塊を §18 に置かないこと** — **人物が枠に居ないためである**（2026-09-29 の裁定①）。",')

add(S15, r'''   "**The identity lock of this work, carried here for continuity across all thirty-four shots: "
   "{IDENTITY}** **In this shot that lock is the work's, not the frame's: no person is in this frame at "
   "any moment, and the frame is not anyone's position — the one thing that stands in both of the two "
   "distances is a single reflected path of light.**\n\n"''',
    r'''   "**No person is in this frame at any moment, and the frame is not anyone's position — the one "
   "thing that stands in both of the two distances is a single reflected path of light.**\n\n"''')

add(S15, r'''   "⚠️ **The identity block above is this work's continuity lock and is not the contents of this frame: "
   "no person is in this frame at any moment — no bearer with a body, no one on the water, no figure at "
   "any distance, in any focus.** " + K.VISUAL_META.replace(''',
    r'''   "⚠️ **No person is in this frame at any moment — no bearer with a body, no one on the water, no "
   "figure at any distance, in any focus.** "
   + K.VISUAL_META.replace(''')

add(S15, r'''                        "⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ**"
                        "——**この1本に人は居ないが、塊は両方に入る**（`has_man: True`。§20 を見る）。"''',
    r'''                        "⛔ **この1本に人は居ないので、同一性の塊は §18 に入らない**（`has_man: False`）"
                        "——**`Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は書かれていない。**"
                        "⚠️ **`男.negatives` は参照集合に在る**——**ゆえに §16 は彼の禁制も運ぶ**（§20 を見る）。"''')

add(S15, r'''   "**No cut to a second setup.** ⚠️ **この1本は1つの画である。**",
 ],''',
    r'''   "**No cut to a second setup.** ⚠️ **この1本は1つの画である。**",
   "⚠️ **この1本に男は居ないが、`男.negatives` は参照集合に在る**（§6）——**彼の禁制はこの1本でも"
   "掛かる**（逐語:「no muscular hero's body, no heroic pose, no heroic lighting」・"
   "「no youthful face, no beardless face, no clean or unlined skin」・「no armour, no helmet, "
   "no greaves, no shield」）。⚠️ **ここでは、それが「人を一人も置かないこと」として効く。**",
 ],''')

add(S15, r'''   "⛔ **この1本の画面に人が居ないこと。** 記録の `unit` は「**海と、水平線だけがある。**」であり、"
   "`motion.subject` は「水面、水平線、そしてその上の空。」である——**どちらも人も舟も名指さない。** "
   "⚠️ **そして参照集合は `男.identity`・`舟` を挙げる。** ⚠️ **この仕様は、"
   "「名指されていない者は居ない」と読んだ**（この作品の `unit` は小石の一つまで名指す）"
   "——**ゆえに bearer を人ではなく光にした。** ⚠️ **もう一方の読み（`s22` のように筏と人を置く）も"
   "成り立つ。****どちらが正かは著者が決める。**",''',
    r'''   "✅ **裁定（2026-09-29）: この1本は人物を枠に置かず、同一性の塊も §18 に貼らない**（`has_man: False`）"
   "——**記録の `unit`（「海と、水平線だけがある。」）も `motion.subject` も、人も舟も名指さない。** "
   "⚠️ **この仕様は裁定の前、塊を作品の錠として §18 に置き、その直後の一文で打ち消していた**"
   "——**裁定①が塊を落とした。****ゆえに `{IDENTITY}` は §18 に無い。** "
   "⚠️ **bearer を人ではなく一本の反射の道にした読みは、裁定のあとも変わっていない。** "
   "⚠️ **`男.negatives` は参照集合に在るので、§16 は彼の禁制を運び続ける。**",''')

# ============================== s12 =========================================
add(S12, 'odyssey-s12 — video-spec — 海 / 日没 / 9.734s. He is not in this frame at any moment.',
    'odyssey-s12 — video-spec — 海 / 日没 / 9.734s. He leaves the frame in the first movement.')

add(S12, r'''⛔ **この1本には、彼が一人も画面に居ない。**——**`unit` の逐語:「彼はもう画面に居ない。」**
⚠️ **ビートの1つめが、それを名指す。** ⛔ **この1本は、彼の視線だけを写す1本である。**''',
    r'''⛔ **彼は、この1本のあいだに枠の外へ出る。**——`unit` は前で「洞の黒の前に男が居る」と言い、後で「**男は岸に居て、海を見ている。**」と言い、**ビートの1つめは「彼はもう画面に居ない。」と書く。**⚠️ **ゆえに彼は冒頭に枠に居て、この1本のあいだに去る**——**去ることが、この1本の変化である**（2026-09-29 の裁定②）。⚠️ **1つめのビートが終わるまでに、彼は枠の外へ出る。**
⛔ **この1本は、彼の視線だけを写す1本である**——**彼は岸に居て、海を見ており、枠には戻らない。**⚠️ **彼は一度もレンズを見ない**——**ゆえに視線は交わらない。**''')

add(S12, r'''⚠️ **この1本に人は一人も居ない**——**彼は岸に居て、枠に入らない。****ゆえにこの1本は、彼の視線の代わりをする画である。**''',
    r'''⚠️ **この1本に居るのは彼一人である**——**彼は最初のビートで枠の外へ出る。****ゆえに出たあとのこの1本は、彼の視線の代わりをする画である。**''')

add(S12, r'''この1本は「**見ている**」である。⛔ **そして見ている者は、この枠に居ない。** ''',
    r'''この1本は「**見ている**」である。⛔ **そして見ている者は、この1本のあいだに枠の外へ出る**——**最初のビートで岸へ出て、そこから海を見る。** ''')

add(S12, r'''     "answer": "⚠️ **この1本に人は一人も居ない。** **ゆえに返事は、ここでも返されない**——''',
    r'''     "answer": "⚠️ **この1本に居るのは彼一人であり、彼は最初のビートで枠の外へ出る。** **ゆえに返事は、ここでも返されない**——''')

add(S12, r'''"——**この1本は、その分割の後半である。****ゆえに彼は、この枠に入らない。**",''',
    r'''"——**この1本は、その分割の後半である。****ゆえに彼は、この1本のあいだに枠の外へ出る。**",''')

add(S12, r'''water. ⚠️ **No skin and no cloth are in this frame** — no person is in it at any moment. ''',
    r'''water. ⚠️ **The only skin and cloth in this frame are the man's, and only in the first movement, as he leaves it** — after that no person is in it at all. ''')

add(S12, r'''   {"name": "nobody",
    "ref": "⛔ **この1本に、人物は一人も居ない。** 顔も、立ち姿も、肩も、遠景の点も、写らない。"
           "⚠️ **参照集合は、それでも `男.identity` を引く**——**この1本に彼は居ないのに、である。**",
    "appearance": "**無い。** ⚠️ **この1本の主題は海であって、人物ではない。**",
    "behavior": "**無い。** ⚠️ **動くのは水面と反射とカメラであり、誰かではない。**",
    "continuity": "⚠️ **人を一人も入れないこと** — どの距離にも、どのピントにも。"
                  "**入れば、この1本は `l08` と対でなくなる**——**視線が交わる。**"
                  "⚠️ **影も、水面への映り込みも入れない。**",
    "notes": ["⚠️ **この仕様は、同一性の塊を作品の錠として §18 に置いた**——**参照集合が `男.identity` を"
              "引いているからである。****そして `Visual Prompt` の側では、生成器が自動で付ける"
              "「**In the frame.**」の一行を、直後の一文が打ち消している**（§20 を見る）。",
              "⚠️ **この1本の守りは弱い。記録として書く。** **人が一人入れば、この1本は人の画になる**"
              "——**ゆえに禁制は §16 と `Master Prompt` の散文の両方に在る。**"]},''',
    r'''   dict(K.man_subject(
     behavior="**最初のビートのあいだ、岸の手前の砂の上に居る。****そして枠の外へ歩き出し、"
              "この1本のあいだに去る**——**去ったあとは、水際のすぐ後ろから海を見ている**"
              "（`unit.after` の逐語:「**男は岸に居て、海を見ている。**」）。"
              "⚠️ **彼は一度もレンズを見ないし、一度も振り返らない。**",
     may="彼の画面の中の大きさ、歩き出す速さ、砂の上に見える量、そして彼が枠を出る時刻"
         "（ビートの1つめの終わりまで）。",
     extra_notes=[
       "⛔ **この判断の根拠を書く。** `unit.before` は「洞の黒の前に男が居る」と言い、`unit.after` は"
       "「**男は岸に居て、海を見ている。**」と言う——**ゆえに彼はこの1本のあいだに枠に居て、去る**"
       "（2026-09-29 の裁定②）。⚠️ **ビートの1つめ（0-2.502s）の逐語:「彼はもう画面に居ない。」**"
       "——**ゆえに彼は、そのビートが終わるまでに枠の外へ出る。**",
       "⚠️ **この1本は同一性の塊を §18 の両方に置く**（`has_man: True`）——**彼が枠に居るので、"
       "塊は作品の錠であると同時に、この枠の中身でもある。****§20 を見る。**"])),''')

add(S12, r'''               "⚠️ **場所は人に反応しない**——**この1本に人は居ない。**",''',
    r'''               "⚠️ **場所は人に反応しない**——**彼が枠の外へ出ても、海は何もしない。**",''')

add(S12, r''' "ref_character": "`男` — ⚠️ **この1本に添付しない。****そしてこの1本の画面に、彼は居ない。**"
                  "`女神` — ⛔ **この1本に添付しない。****彼女は四つの姿のどれとしても現れない。**"
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.日没` の5鍵である。"
                  "⚠️ **`男.identity` が引かれているのは、この1本に彼が居るからではない**"
                  "（**`unit` の逐語:「彼はもう画面に居ない。」**）——**作品の連続性の錠だからである**（§20 を見る）。",''',
    r''' "ref_character": "`男` — ⚠️ **この1本に添付しない。****そしてこの1本で彼が枠に居るのは、"
                  "最初のビートだけである**（2026-09-29 の裁定②。§20 を見る）。"
                  "`女神` — ⛔ **この1本に添付しない。****彼女は四つの姿のどれとしても現れない。**"
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.日没` の5鍵である。"
                  "⚠️ **`男.identity` が引かれているのは、この1本に彼が居るからである**"
                  "——**そしてこの1本は、その塊を §18 の両方に貼る**（`has_man: True`）。",''')

add(S12, r'''   "beginning": "**海と、手前の砂。** 波は低く、**反射はまだ一枚である。****彼はもう画面に居ない。**",''',
    r'''   "beginning": "**海と、手前の砂。** 波は低く、**反射はまだ一枚である。****彼はこのビートのあいだに、枠の外へ出る。**",''')

add(S12, r'''——⛔ **彼がもう居ないことの確認である。** 次の3.494秒で''',
    r'''——⛔ **彼が枠の外へ出ることが、そこで起きる。** 次の3.494秒で''')

add(S12, r'''    "**海と、手前の砂だけがある**——**彼はもう画面に居ない。**"),''',
    r'''    "**海と、手前の砂があり、彼が枠の外へ出て行く**——**このビートの終わりには、彼はもう居ない。**"),''')

add(S12, r'''"⚠️ **この1本のカメラは、彼の位置ではない**——**彼は岸に居て、枠に入らない。**",''',
    r'''"⚠️ **この1本のカメラは、彼の位置ではない**——**彼は最初のビートで枠の外へ出て、岸から海を見る。**",''')

add(S12, r'''`0-2.502s` — **the frame holds the water and the near sand and does not ''',
    r'''`0-2.502s` — **the frame holds the water and the near sand; the man goes out of the frame as this movement runs, and ''')
add(S12, r'''             "move**; then `2.502-5.996s`''',
    r'''             "by its end there is nobody in the frame**; then `2.502-5.996s`''')

add(S12, r'''   "object": "**動く物は無い。****この1本に物は一つも置かれていない**——**動くのは水と光だけである。**",''',
    r'''   "object": "**動く物は無い。****この1本に物は一つも置かれていない**——**動くのは水と光と、最初のビートの彼だけである。**",''')

add(S12, r'''   "arc": "**見ている者が画面に居ないのに、見ていることが立つ。** ⚠️ **この1本の感情は、海の側には無い**''',
    r'''   "arc": "**見ている者は、この1本のあいだに枠の外へ出る。****それでも、見ていることが立つ。** ⚠️ **この1本の感情は、海の側には無い**''')

add(S12, r'''             "**誰も写さないのに、視線だけがある。**",''',
    r'''             "**彼は去り、視線だけが残る。**",''')

add(S12, r'''          "⚠️ **この1本に人の音は一つも無い**——**彼は岸に居るが、この枠に居ない。** ''',
    r'''          "⚠️ **この1本に人の音は一つも無い**——**彼は黙っており、足音もこの1本のミックスに載せない。** ''')

add(S12, r'''   "**No person in frame at any moment** — no figure at any distance, in any focus, **no silhouette, "
   "no head above the water, no one on the sand, and no shadow and no reflection of a person.** "
   "⚠️ **ビートの1つめの逐語:「彼はもう画面に居ない。」**",''',
    r'''   "⛔ **The only person in this frame is the one man, and only in the first movement** — **no second "
   "person at any time** — he goes out of the frame before that movement ends, and after he has gone "
   "there is no figure at any distance or in any focus, no silhouette, no one on the sand, and no shadow "
   "or reflection of a person anywhere. ⚠️ **ビートの1つめの逐語:「彼はもう画面に居ない。」**",''')

add(S12, r'''   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.** ⚠️ **この1本に彼は居ないが、塊は作品の錠である。**",''',
    r'''   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.** ⚠️ **この1本では、彼は最初のビートだけ枠に居て、やがて枠の外へ出る**"
   "——**塊は、その彼の同一性である。**",''')

add(S12, r'''   "⛔ **人を一人も入れない** — どの距離にも、どのピントにも、**影にも、映り込みにも。**",''',
    r'''   "⛔ **彼以外の誰も入れない** — どの距離にも、どのピントにも、**影にも、映り込みにも。** "
   "⚠️ **彼自身は、最初のビートのあいだに枠の外へ出る。**",''')

add(S12, r'''           "**the frame with no figure in it and nothing in it that reads as one.**",''',
    r'''           "**the frame with no figure in it after the first movement, and nothing in it that reads as "
           "one.**",''')

add(S12, r'''   "⛔ **人を一人も入れないこと。** **ビートの1つめが名指しており、入ればこの1本は `l08` と対でなくなる。**",''',
    r'''   "⛔ **彼以外の誰も入れないこと。** **ビートの1つめが名指しており、入ればこの1本は `l08` と対でなくなる。** "
   "⚠️ **彼自身は、そのビートのあいだに枠の外へ出る。**",''')

add(S12, r'''   "the water's reflection breaks all at once.** **No person is in this frame at any moment — the man "
   "who is watching this sea is on the shingle behind the camera, outside the frame, and he never enters "
   "it.**\n\n"''',
    r'''   "the water's reflection breaks all at once.** **One person is in this frame, and only in the first "
   "movement: the man who watches this sea walks out of the frame before that movement ends, and he does "
   "not come back into it.**\n\n"''')

add(S12, r'''   "**The identity lock of this work, carried here for continuity across all thirty-four shots: "
   "{IDENTITY}** **In this shot that lock is the work's, not the frame's: the frame holds the water, the "
   "near sand and the horizon, and nothing with a body in it.**\n\n"''',
    r'''   "**The identity lock of this work, carried here for continuity across all thirty-four shots: "
   "{IDENTITY}** **It is the man who leaves this frame: he is the only one in it, and only for the first "
   "movement, and he is not seen after it.**\n\n"''')

add(S12, r'''   "0-2.502s: **the water and the near sand — long low swells with no white water, one path of low sun "
   "lying on the surface, and nobody in the frame.**\n"''',
    r'''   "0-2.502s: **the water and the near sand — long low swells with no white water, one path of low sun "
   "lying on the surface — and the man goes out of the frame as the movement runs; by its end there is "
   "nobody in the frame.**\n"''')

add(S12, r'''   "dark and coarse, cut across by the water's own line. **No figure is in the frame at any distance or "
   "in any focus, nothing stands on the sand, and no shadow or reflection of a person falls anywhere in "
   "it.** No sail, no bird, no other vessel, no rock in the water."),''',
    r'''   "dark and coarse, cut across by the water's own line. **In the first movement the man is in the "
   "frame — on the near sand at the frame's lower edge, small and seen from behind, walking out of the "
   "picture — and he is gone before that movement ends; after that no other person is in the frame at any "
   "distance or in any focus, nothing stands on the sand, and no shadow or reflection of a person falls "
   "anywhere in it.** No sail, no bird, no other vessel, no rock in the water."),''')

add(S12, r'''   " ⚠️ **The identity block above belongs to this work's continuity and not to the contents of this "
   "frame: no person is in this frame at any moment.** ⚠️ **The horizon is level, unbroken and holds its "''',
    r'''   " ⚠️ **The identity block above is this work's continuity lock, and this is the one frame in which "
   "it is also the frame's own contents: the man is in this frame for the first movement and walks out "
   "of it.** ⚠️ **The horizon is level, unbroken and holds its "''')

add(S12, r'''   "stutter, no floaty weightless motion, no static frames — **the water moves in every frame of the "
   "take.**"),''',
    r'''   "stutter, no floaty weightless motion, no static frames — **the water moves in every frame of the "
   "take.** **In the first movement the man walks out of the frame across the near sand; he is the only "
   "thing in the frame that is not water, light or sand, and after he has gone nothing else enters.**"),''')

add(S12, r'''⚠️ **The move is motivated by going to "
   "where his gaze goes; the stop is motivated by the horizon's centre.**''',
    r'''⚠️ **The move is motivated by going to "
   "where his gaze goes — and he himself has already left the frame, so the camera follows the gaze and "
   "not the man; the stop is motivated by the horizon's centre.**''')

add(S12, r'''⚠️ **There is no human sound in this shot at all** — **the man is on the shingle "
   "and never enters the frame** — **and no voice of any kind is heard here.**"''',
    r'''⚠️ **There is no human sound in this shot at all** — **he makes no sound as he goes out of the "
   "frame: no voice, no breath, no footfall** — **and no voice of any kind is heard here.**"''')

add(S12, r'''                        "——**この1本に彼は居ないが、塊は両方に入る**（`has_man: True`。§20 を見る）。",''',
    r'''                        "——⚠️ **この1本で彼が枠に居るのは最初のビートだけである**（`has_man: True`）"
                        "——**ゆえに塊は両方に入る**（§20 を見る）。",''')

add(S12, r'''   "⛔ **この1本の参照集合は `男.identity` を引く**——**そして `unit` は「彼はもう画面に居ない」と言う。**"
   "⚠️ **この仕様は、塊を作品の錠として §18 に置いた**（`has_man: True`）——**`has_man: False` にすれば、"
   "塊は `Master Prompt` と `Visual Prompt` の両方から消える。****どちらが正かは著者が決める。** "
   "⚠️ **`has_man: True` のまま置いた以上、生成器が `Visual Prompt` に付ける「**In the frame.**」の一行は"
   "残る**——**この仕様は、その直後の一文で打ち消している。**",''',
    r'''   "✅ **裁定（2026-09-29）: この1本は彼が冒頭に枠に居て、この1本のあいだに去る**（裁定②）——"
   "**`unit.before`（「洞の黒の前に男が居る」）と `unit.after`（「**男は岸に居て、海を見ている。**」）が"
   "彼を枠の側に置き、ビートの1つめが「**彼はもう画面に居ない。**」と書くためである。** "
   "⚠️ **§8 のビート1の逐語は、そのビートの終わりの状態として読む**——**§18 は、裁定②に従って"
   "「彼がそのあいだに枠の外へ出る」と書いた。** "
   "⛔ **ゆえに `has_man: True` のまま、同一性の塊も §18 の両方に残る**——**そして塊は、"
   "去っていく彼の同一性である。** ⚠️ **この仕様は裁定の前、塊を「作品の錠であり枠の中身ではない」と"
   "打ち消していた**——**裁定②がその打ち消しを外した。**",''')

add(S12, r'''   "⛔ **誰かが写る。** この1本のいちばん高い危険である——**遠景の点一つで、この1本は人の画になる。** "
   "禁制は §16 と `Master Prompt` の散文の両方に在る。",''',
    r'''   "⛔ **彼以外の誰かが写る。** **遠景の点一つで、この1本は `l08` との対でなくなる。** "
   "禁制は §16 と `Master Prompt` の散文の両方に在る。",''')

add(S12, r'''   "**人の影か映り込みが入る。** ⚠️ **彼は岸に居るので、影は自然に落ちうる**——"
   "**砂の上の影一つで、ビートの1つめが偽になる。**",''',
    r'''   "**彼が枠に残る。** ⚠️ **最初のビートで出て行かなければ、ビートの1つめの逐語が偽になる**"
   "——**2.502秒より長く枠に居れば、この1本は彼の画になる。**",''')

add(S12, r'''   "**「綺麗な海」で終わる。** ⚠️ **美しいだけの海の画は、`l08` と対にならない**"
   "——**この1本は、見ている者が居ないことのために在る。**",''',
    r'''   "**「綺麗な海」で終わる。** ⚠️ **美しいだけの海の画は、`l08` と対にならない**"
   "——**この1本は、見ている者が枠の外へ出たあとの海のために在る。**",''')

# ============================== 実行 ========================================
srcs = {}
for path in (S12, S13, S14, S15):
    with io.open(path, encoding="utf-8") as f:
        srcs[path] = f.read()

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
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(text)

print("applied %d edits to %d files" % (len(EDITS), len(srcs)))
