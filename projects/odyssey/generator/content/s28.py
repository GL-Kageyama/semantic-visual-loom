# -*- coding: utf-8 -*-
"""odyssey-s28 — impossible-camera — 海 / 夜 / 5.744s. l29「海を渡る」の3度目、下から。

The 3rd of the work's 4 impossible-camera shots, and the pair of s21:
the same sea held between two viewpoints that cannot exist — above and below.
"""
import common as K


C = {
 "n": "s28",
 "title": "海を渡る——水の中から、舟の影が通る",
 "duration": "5.744",
 "format": "impossible-camera",
 "has_man": False,
 "place": "海",
 "time": "夜",
 "segment": "final-chorus-2",

 "header": """⚠️ **`l29`「海を渡る」の3度目である。** ⚠️ **役は `運動` で、`s14`・`s21` と同じである。**
出所は曲の `l29`（248.378–254.122、**5.744秒**であり、**この1本の尺そのものである**）。
⛔ **3本は形式で分かれる**——`s14` は舳先の高さ、`s21` は上から、**この1本は下から。**
⚠️ **`s21` とこの1本が対である**——**同じ海を、二つの在りえない視点で挟む**（記録の註の逐語）。
⛔ **形式は `impossible-camera`。****この作品で4本あるうちの3本目である**（`s11` の註）。
⚠️ **記録の註は、この形式の名がまだ検査されていないことを明記している**"
"（逐語:「**ショット記録に `REF_FORMAT` の欄は無い**——形式は仕様（§6）の側にある。"
"ゆえにここに書いた形式は、まだ検査されていない。」）。
⚠️ **この1本は `final-chorus` の2行目である。**
⛔ **裁定 2026-09-29**: **記録が人物を名指さない1本は、同一性の塊を落とす。**
**この1本の `unit`（前・後）と `beats` のどこにも人物が現れないので、この1本がそれに当たる**
——**`has_man: False` であり、塊は §18 に貼られない。**
⚠️ **この仕様のショット記録は `shots/odyssey-s28.yaml` である。**""",

 "intent": "**水を渡ることを、水の中から写せるか。**"
           "⚠️ **壮大さを、3度目に別の角度から**（記録の `aim` の逐語）。"
           "**最初のコマでは、すでに水面の下に視点がある。****そこに舟は無く、光と、水面の裏側だけがある。**"
           "**最後のコマでは、影が通り過ぎ、そして影が消えている**"
           "——⛔ **影が消えることが、この1本の切れ目のコマである。**"
           "⚠️ **切らない。1本は1つの画である。** **この視点は、どこにも置けない。**",

 "world_concept": K.world_concept(
   "⛔ **この1本は、この作品で4本ある `impossible-camera` の3本目である**"
   "（`s11` の註がそのことを定める）。"
   "⚠️ **この作品の海は19本に現れるが、水の内側から見たのはこの1本だけである。**"
   "⛔ **この1本が写すのは、渡ることそのものではなく、"
   "渡ったことが水の中に残すもの（＝ほとんど何も残らないこと）である。**"
   "⚠️ **`world.rules` の逐語:「この作品は、帰り着かない。」**——**ゆえにこの1本は、"
   "対岸を写さない。****着く場所は、この1本の画には無い。**"
   "⚠️ **`unit.before` の逐語:「舟は水の上を進んでいる。」**"
   "**`unit.after` の逐語:「水面の下から見て、舟の影が通っていく。」**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⛔ **この1本に答えは無い。****影が通り過ぎ、そして消える。****水は何も残さない**"
               "——**渡ったことは、水の中には残らない。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "**この1本の光は星と、その水面での屈折だけである。****水中に光源は無い**"
                "（**発光するものも、光る生き物も置かない**）。"
                "⚠️ **この1本は彼女の側の1本ではない**——**彼も、この画には居ない。**",
     "name": "⚠️ **この1本に名は無い。** ⛔ **言葉はこの画に一つも入らない。****水中には文字も、"
             "名も、掲示も無い**（逐語, `forbidden_set`: `no legible text on any surface`）。"
             "**「海を渡る」は歌の言葉であり、画面の言葉ではない。**",
     "bow": "⚠️ **この1本に弓は無い。** ⚠️ **この1本に道具は一つも無い**——**画にあるのは水と、"
            "光と、影だけである。****斧も、針も、櫂も、この画には入らない。**",
     "places": "この1本が置くのは `海` であり、**その水の内側である。** ⛔ **`沈んだ場所` ではない**"
               "——**この1本の水は深い場所ではなく、水面のすぐ下である。****沈んだ者たちも、"
               "沈んだものも、この画には無い。**",
     "japanese": "⚠️ **この1本には歌がある**——`l29`「海を渡る」であり、**5.744秒である**"
                 "（248.378–254.122）。**歌はポストで載る。****この画の中の音は水だけである。**",
   },
   extra=[
     "⛔ **記録の `motion.law` の逐語:「この様式は実写である（裁定①）。水中の画も、実写の物理に従う"
     "——光は水面で屈折し、影は水の動きで歪む。」**"
     "⚠️ **ゆえにこの1本の水は、実在の水の物理で描かれる**——**屈折は実際の屈折であり、"
     "歪みは実際の波の屈折率の変化による。** **そしてこの物理は、5.744秒のあいだ変わらない。**",
     "⚠️ **この1本の役は `運動` である。** 固有基準は「重さ・慣性・加速・流れ・衝撃・身体の可読性・"
     "リズム。**様式の物理で測る**」（`rolemap.ROLES`）——⛔ **ゆえにこの1本は水の物理で測られる。**"
     " **カメラの美しさでは測られない。**",
     "⚠️ **`s21` とこの1本が対である**（記録の註の逐語）——**`s21` は上から、この1本は下から。**"
     "**同じ海を、二つの在りえない視点で挟む。**"
     "⚠️ **ゆえにこの1本は、`s21` と同じ海・同じ夜である**——"
     "**そして `s21` が空の側から見たものを、この1本は水の側から見る。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, **photographed from inside the water, just below the surface, looking up**: the "
     "underside of the surface is the ceiling of the frame and it is never still; **everything above it "
     "reaches the frame only as light and, when the raft crosses, as a shadow.** ⚠️ **The water the "
     "viewpoint is in is dark and almost formless** — **no sand, no rock, no bottom, no wreck and no "
     "living thing is in this frame.**",
   "Color Language":
     "One value, and it is very dark: black water, and above it the surface's underside shot through with "
     "the sky's own light, **which is compressed into one region where the sky is visible and is a mirror "
     "everywhere else.** ⚠️ **The shadow that crosses is not a colour but the absence of that light**"
     "——**ゆえにこの1本の画には、暖かい色が一つも無い。** ⚠️ **The grade is the same in the first frame "
     "and the last; the light sways, but the exposure does not open.**",
   "Texture":
     "Water with no surface of its own to grab — **a body of fine suspended matter that catches the light "
     "and no more**; the underside of the surface as a moving skin, its light breaking into cells and "
     "reforming; **the shadow's edge soft and continuously redrawn, never a clean line**"
     "（**光は水面で屈折し、影は水の動きで歪む**）。⚠️ **Film grain present and even, and the grain is a "
     "large part of what this frame is made of.**",
   "Rendering":
     "**Photographic, and physically consistent** — **a real lens and a real body of water: light bends at "
     "the surface, and what is above the surface is compressed into the cone through which it can be "
     "seen.** ⚠️ **This is not a fisheye and not a distortion effect**"
     "——**この1本の「在りえなさ」は視点の側にあり、レンズの側には無い。** "
     "No painterly stroke, no CGI look, no illustration.",
   "Visual Density": "Very low, **and almost nothing in it is an object** — 光、水面の裏側、そして影。"
                     "⚠️ **ビートの `dense` は、物が多いことではない。****この1本でいちばん多くが"
                     "起きているということであり、それは「影が通り過ぎたこと」である。**",
   "Time": "`夜` — **`final-chorus` の2行目である**（`l29`、248.378–254.122）。"
           "⚠️ **この1本の空は `s21` と同じ空である**——**ただし、水の屈折を通して見た空である。**",
   "Atmosphere": "The hour in which the sea is not a surface to cross but a place that keeps nothing"
                 "——**渡ったあとに、水の中に何も残らないこと。**",
 }),

 "subjects": [
   {"name": "水中の光",
    "ref": "⛔ **記録の `motion.subject` の逐語である**（「水中の光、水面の裏側、そして舟の影。」）。"
           "⚠️ **この1本の第一の主題は光であり、そしてその光は上の空から来る。**",
    "appearance": "**水面を通って入り、水中で揺れる光である。**"
                  "**水面の上の空が、水の屈折によって一つの領域に集められて見える**"
                  "（逐語, `motion.law`: 「光は水面で屈折し」）。"
                  "⚠️ **その領域の外側では、水面の裏側は鏡であり、暗い水を映し返す。**"
                  "**水中に光源は一つも無く、光はすべて上から来る。**",
    "behavior": "**揺れる。****そして波の周期で細かく割れ、戻る**（記録の `motion.quality` の逐語:"
                "「光が水中を揺らす。」）。⚠️ **速くならない。****この揺れはこの1本のあいだ、"
                "同じ振幅で続く**——**うねりが変わらないからである。**",
    "continuity": "**Must preserve** — 光源は上だけであること、屈折は実際の屈折であること、"
                  "揺れの振幅と周期、そして水中に光源が無いこと。"
                  "**May change** — 水面の割れ方、光の網の細かさ、そして影が入るあいだだけ光が欠けること。",
    "notes": ["⛔ **光る生き物を置かない。****この経路は、暗い水中の画に発光を足しやすい**"
              "——**そしてそれを足せば、この1本の光は上から来なくなり、"
              "`世界の規則` の答えが変わる。**",
              "⚠️ **この1本の光は、`s21` の空の光と同じ一つの光である**——"
              "**`s21` は上の側でそれを見て、この1本は下の側でそれを受ける。**"]},
   {"name": "水面の裏側",
    "ref": "⛔ **記録の `motion.subject` の逐語である。** ⚠️ **この1本の「天井」であり、"
           "そしてこの1本のいちばん動くものである。**",
    "appearance": "**上の面であり、そしてこの1本では、それは膜である。****星の光がその膜を通り、"
                  "空は水の屈折で一つの領域に圧される。**"
                  "⚠️ **その領域の外では、裏側は鏡である**——**水が水を映し、暗さが暗さを返す。**"
                  "**膜は絶えず形を変える。****白波は無く、割れ目は無い。**",
    "behavior": "**波立つ**（記録の `motion.quality` の逐語:「水面が上で波立ち」）。"
                "**うねりが下から見えるので、膜はゆっくり上下し、そして細かく皺を寄せる。**"
                "**影が上を通るとき、その皺は影の輪郭を書き換える**"
                "——**影は止まっているのに、影の形が動く。**",
    "continuity": "**Must preserve** — 膜が絶えず動いていること、屈折の領域と鏡の領域の境界、"
                  "白波が無いこと、そして影の輪郭が水の動きで歪むこと（逐語, `motion.law`）。"
                  "**May change** — 皺の細かさ、膜の上下、影が入る位置。",
    "notes": ["⛔ **この1本の水面は破れない。****`海.base` の逐語:「no white water」**"
              "——**下から見ても、この海は砕けない。**",
              "⚠️ **この1本の水は `s27` と同じ水である**——**`s27` の櫂が破ったのも、"
              "この膜である。**"]},
   {"name": "舟の影",
    "ref": "⛔ **記録の `motion.subject` と `unit.after` の逐語である**"
           "（「そして舟の影。」／「水面の下から見て、舟の影が通っていく。」）。"
           "⚠️ **この1本に現れる唯一の「彼の側のもの」であり、そしてそれは影である。**",
    "appearance": "**光の欠けた領域である。****丸太も、縄も、板も、櫂も、そこには見えない**"
                  "——**この1本の影は、形を持たない。****輪郭は水の動きで歪み、"
                  "そして細部はどこにも無い**（逐語, `motion.law`: 「影は水の動きで歪む」）。"
                  "⚠️ **影は `上` から来る**——**ゆえに影が通るとき、この1本の光が欠ける。**",
    "behavior": "**ゆっくり横切る**（記録の `motion.quality` の逐語:「その影がゆっくり横切る。」）。"
                "⚠️ **速くならない。****`s27` の漕ぎと同じ速さである**——"
                "**この作品の舟は、一度も加速しない。**"
                "**そしてこの1本の最後で、影は通り過ぎ、消える**"
                "（記録の第3のビートの逐語:「影が消えるのが、切れ目のコマである。」）。",
    "continuity": "**Must preserve** — 影が形を持たないこと、輪郭が水の動きで歪むこと、"
                  "ゆっくり進むこと、そして最後に消えること。"
                  "**May change** — 影の濃さ、歪みの細かさ、横切る角度と、消える位置。",
    "notes": ["⛔ **影を舟として描かない。****丸太の縁も、縄も、板も、この画では読めない**"
              "——**それは夜の水であり、影はただ光の欠けたところである。**"
              "⚠️ **そして彼は影の中にも居ない**——**平台は不透明であり、"
              "水の膜は下から見れば光しか通さない。**",
              "⚠️ **この1本の影が、この作品で唯一「渡ることが誰にも見えない」ことを示すものである。**"]},
 ],

 "environment": {
   "location": "`海` — **その水の内側であり、水面のすぐ下である。** ⚠️ **深い場所ではない**"
               "（**`沈んだ場所` は別の場所である**）。⚠️ **底は見えないし、底を写さない。**"
               "⛔ **この1本の画には、水平線が無い**——**視点が水の中にあるからである。**",
   "elements": "**水**、**水面の膜（裏側）**、**星の光（水面の屈折を通したもの）**、そして**舟の影**。 "
               "⚠️ **砂も、岩も、底も、藻の見せ場も、生き物も、沈んだものも置かない。**"
               "⚠️ **帆も、鳥も、他の舟も置かない**（`海.base` の逐語）。",
   "behavior": "**うねりが上を通り、膜がゆっくり上下する。****水そのものは重く、ゆっくりと動く**"
               "——**この1本の視点は、その水に運ばれる。**"
               "**光は揺れ、影が入ると欠け、影が過ぎると戻る。**",
 },

 "objects": [
   "**この1本に物は無い。** ⛔ **画にあるのは水、光、膜、そして影である**"
   "——**舟も、櫂も、彼の体も、この画には形として入らない。**"
   "⚠️ **ゆえにこの1本には、小道具の検算すべき対象が一つも無い**"
   "（⚠️ **この作品の小道具は4つであり**——`ledger.props` の 舟・帆・斧・太陽の牛"
   "——**この1本に来るのは舟だけであり、そしてそれは影としてだけ来る**）。",
   "⚠️ **影は物ではない。****この1本の影は、光の欠けた領域である**"
   "——**ゆえにこの1本では、影の側からも、物の検算をしない。**",
   "⚠️ **この1本に文字は一つも無い。****板も、樽も、帆も、この画には無いので、"
   "文字が乗りうる面がそもそも無い**（逐語, `forbidden_set`: `no legible text on any surface`）。",
 ],

 "ref_character": "⚠️ **この1本に人は一人も居ない。****そして参照集合は `男.identity` を名乗る**"
                  "——**それでも、この1本はその塊を §18 に貼らない**"
                  "（`has_man: False`、**裁定 2026-09-29**）。"
                  "⚠️ **根拠は記録の側にある**：**`unit`（前・後）と `beats` のどこにも人物が現れない。**"
                  "⛔ **この1本の画は、光と膜と影だけである。**"
                  "⚠️ **`forbidden_set` の逐語:「no other human being in frame — no companion, no crowd, "
                  "no second person」**——**この1本では、"
                  "その禁制は彼自身にも掛かる**（**水の膜は下から見れば光しか通さない**）。"
                  "⚠️ **参照集合は `男.identity`・`男.negatives`・`海`・`海.geography`・`海.states.夜`・"
                  "`舟`・`舟.appearance`・`舟.negative` の8鍵である**——**`s26`・`s27` と同じ8鍵である。**"
                  "**添付は0点である**（裁定②）。",

 "ref_extra": [
   "- ⚠️ **形式カード `impossible-camera` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; what "
   "follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §8 に書いた5つの変数と、§16 に運んだカード自身の禁制である。**",
   "- ⚠️ **カードの逐語:「Its grammar is written into the `video-spec` skeleton — §10 CAMERA — which "
   "asks for timing, movement, target and speed; this card asks what the viewpoint *is*, which that "
   "section has no field for.」**——**ゆえにこの1本では、§10 の `language` と `events` が文法の置き場"
   "である。****視点が何であるかは、そこに書かれる。**",
   "- ⚠️ **カードの逐語:「This is unfolding: the shot is the journey of a viewpoint, and the journey is "
   "the time.」**——**ゆえにこの1本の5.744秒は、視点の旅そのものである。**",
   "- ⚠️ **この作品で `impossible-camera` を使うのは4本であり、この1本はその3本目である。**"
   "**`s21` とこの1本が対である**——**`s21` は上から、この1本は下から。**"
   "**同じ海を、二つの在りえない視点で挟む。**",
   "- ⚠️ **この経路（`SEEDANCE 2.5`）では、`Negative Prompt` は床として受け取られない**（`L30`）。"
   "**ゆえにこの1本の禁制は、肯定形で §18 の散文にも書かれている**"
   "——**入口が述べられ、径の物理が一貫し、そして到着があることは、"
   "すべて散文の側で肯定形で言われる。**",
 ],

 "narrative": {
   "core": "**影が通り過ぎる** — 水を渡ることが、水の中から見られる。"
           "**そして渡ったあと、水の中には何も残らない。**",
   "beginning": "**水中。****上に水面がある。**（記録の第1のビートの逐語）"
                "**舟はまだ画に入っていない。**",
   "turn": "**影が横切る。****ゆっくりである。****光が揺れる。**（記録の第2のビートの逐語）",
   "peak": "**影が通り過ぎる。****水面が歪み、そして影が消える**（記録の第3のビートの逐語）"
           "——⛔ **それが、この1本の切れ目のコマである。**",
   "pull": "⚠️ **この1本は、彼を写さず、舟も写さず、そして対岸も写さない。**"
           "**残るのは、動きつづける膜と、光だけである**——"
           "**`s30` は、この1本のあとに来る。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.246秒.** 最初の1.499秒は**水中の表白と、"
            "上にある膜のために払われる**——**この1本でいちばん静かな区間である。** "
            "次の1.999秒は**影が入ってくるところである**——**ゆっくり横切り、光が揺れる。**"
            "**最後の2.246秒がこの1本の到着である**——**影が通り過ぎ、膜が歪み、そして影が消える。**"
            "⚠️ **形式カードの逐語:「One beat — the core reveal — takes the largest single share (a "
            "useful anchor: ~30% of `DURATION`).」**——**この1本の中心は第3のビートであり、"
            "その2.246秒は 5.744秒のうちの約39%である。**"
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**影が消えたあとも、膜は動きつづけている。**\n"
            "- ⚠️ **`impossible-camera` の5つの変数**（⚠️ 定義はカードの逐語である）:\n"
            "  - `EYE`＝the viewpoint that cannot exist — ⛔ **水面のすぐ下から上を見る視点である。**"
            "**そしてこの視点には、支えが一つも無い**——**水の中にカメラは置けない。**"
            "**これがこの視点の在りえなさである。**"
            "⚠️ **在りえなさは視点の側にあり、レンズの側には無い**"
            "（カードの `avoid` の逐語:「**A viewpoint that is merely an unusual camera position**」）。\n"
            "  - `ENTRY`＝how the shot arrives at it — ⛔ **カードの逐語:「**The entry is stated.** … "
            "An unstated entry reads as a continuity error in the previous shot rather than as this "
            "grammar.」**——**ゆえにこの1本は、舟の航跡の割れ目を通って入る**"
            "（`海.base` の逐語:「the surface broken only by the raft's own wake」）。"
            "**前の1本（`s27`）は、同じ水の上を舟が進んでいく1本である**"
            "——**最初のコマは、すでに水面の下である。**\n"
            "  - `PATH`＝what the viewpoint travels through — **水面のすぐ下の水であり、"
            "その中を視点は水に運ばれて流れる。****この水の法則はこの1本のものである**"
            "（カードの逐語:「**Give the path its own law of scale and physics, and keep it "
            "consistent inside the shot.**」）——**光は水面で屈折し、影は水の動きで歪み、"
            "そしてこの物理は5.744秒のあいだ変わらない。**\n"
            "  - `ARRIVAL`＝where the shot leaves the viewer — ⛔ **影が消えたあとの水の中である。**"
            "**残るのは、動きつづける膜と光だけである。**"
            "⚠️ **この作品は着かないので、この視点も着かない**"
            "——**そして着かなかったことが、この1本の到着である**"
            "（カードの逐語:「**The shot arrives somewhere.** … Leaving the viewer inside with no "
            "arrival spends the journey and keeps nothing.」）。\n"
            "  - `DURATION`＝clip length — **`5.744s`。**",

 "actions": [
   ("ACT_SURFACE", "視点は水面のすぐ下にあり、膜が上にある。",
    "**水中。****上に水面がある。****光は膜を通って水中に散っている。**"),
   ("ACT_SHADOW_ENTER", "光が揺れており、影はまだ無い。",
    "**影が入ってくる**——**光の欠けた領域が、ゆっくり横切り始める。**"),
   ("ACT_SHADOW_CROSS", "影は画の中ほどにある。",
    "**影が横切る。****ゆっくりである。****光が揺れる。**"
    "**影の輪郭は、膜の動きによって絶えず書き換えられる。**"),
   ("ACT_SHADOW_GONE", "影はもう画の中に無い。",
    "⛔ **影が通り過ぎる。****水面が歪み、そして影が消える**"
    "——**影が消えることが、この1本の切れ目のコマである。**"),
 ],

 "camera": {
   "language": "⛔ **この1本の `EYE` は視点であって、カメラの位置ではない**"
               "（カードの `avoid` の逐語:「**A viewpoint that is merely an unusual camera position**」）。"
               "**この1本は、水面のすぐ下から上を見る。**"
               "⛔ **この視点は在りえない**——**水の中にカメラは置けない**"
               "（**水はレンズを満たし、そして夜の水は光を通さない**）。"
               "⚠️ **入口は述べられる**（カードの `do` の逐語:「**State the entry — say how the "
               "viewpoint got where no camera can be**」）——"
               "⛔ **この1本は、舟の航跡の割れ目を通って入る**"
               "（`海.base` の逐語:「the surface broken only by the raft's own wake」）。"
               "**前の1本（`s27`）は、同じ水の上を舟が進んでいく1本である**"
               "——**その航跡が、この1本の入口である。****最初のコマは、すでに水面の下である。**",
   "events": "⛔ **この1本の時間は、視点の旅そのものである。**"
             "`0-1.499s` — **水中。****上に水面がある。**"
             "`1.499-3.498s` — **影が横切る。****ゆっくりである。****光が揺れる。**"
             "`3.498-5.744s` — **影が通り過ぎる。****水面が歪み、影が消えるのが、切れ目のコマである。**"
             "⚠️ **この旅は一続きであり、途中で止まらない。****そして `5.744s` で、"
             "この視点はまだ水の中に居る**——**それが出発点から動いた距離の全部である。**",
   "behavior": "⛔ **この1本は、ドリーも、クレーンも、ステディカムも使わない**"
               "——**この視点を運ぶのは水そのものである。**"
               "**ゆえに動きの動機は、機械ではなく、うねりである**"
               "（カードの `avoid` の逐語:「**Treating it as a camera move with a target and a speed**」）。"
               "⚠️ **この1本が組むのは、視点の存在であって、カメラの移動ではない**"
               "（カードの `do` の逐語:「**Compose the viewpoint's existence, not the movement of a "
               "camera placed at a point**」）。"
               "**ゆえに視点は、水に浮かされ、うねりに合わせて上下し、そして水平にゆっくり流れる。**"
               "⚠️ **そしてこの流れは、影と同じ向きであり、同じ速さである**"
               "——**水も、舟も、この1本では一度も加速しない。**"
               "**A fixed frame is not this card's case; but neither is a move with a target and a "
               "speed.** No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural "
               "rotation, and **no unmotivated move.**",
 },

 "motion": {
   "subject": "⛔ **記録の `motion.subject` の逐語:「水中の光、水面の裏側、そして舟の影。」**"
              "**この3つが、この1本の主題の全部である。****ゆえにこの1本に、身体も、"
              "道具も、生き物も無い。**",
   "object": "**この1本に物は無い。** ⚠️ **動くのは膜と、光と、影だけである。**"
             "**舟は、この1本では影としてだけ動く**——**そしてそれは物ではない。**",
   "environment": "**うねりが上を通り、膜が絶えず形を変える。****光は水面の屈折で集まり、"
                  "そして揺れる。****影が入ると光が欠け、影が過ぎると戻る。**"
                  "⚠️ **この3つは、この1本のあいだ同じ物理で動きつづける**"
                  "（カードの `avoid` の逐語:「**A path whose physics changes halfway for convenience**」）。"
                  "⚠️ **白波を立てない**（`海.base` の逐語:「no white water」）。",
   "weight": "⛔ **水は重い。****この1本の動きはすべて遅い**——"
             "**光の揺れも、膜の上下も、影の横切りも、水の質量の側から来る。**"
             "⚠️ **ゆえにこの1本の速さを、カメラで作らない。**"
             "**時間を伸ばせば、この水は水でなくなる**（**この1本の遅さは、"
             "水の慣性そのものである**）。",
   "inertia": "**うねりは止まらない。****膜は、前の動きを次の動きへ持ち越す。**"
              "**影が消えたあとも、水は影が通ったあとの動きを続ける**"
              "——**この1本の最後のコマで、膜はまだ動いている。**",
   "acceleration": "**加速しない。****この1本のあいだ、うねりの速さも、影の速さも、"
                   "視点の流れも一定である。**"
                   "⛔ **ゆえに影は急に現れず、急に消えない**——**それは入ってきて、通り過ぎる。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この5.744秒に、"
               "止まったフレームは一つも無い**——**膜は全フレームで動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い。****影が通ることは、衝突ではない。**",
 },

 "emotion": {
   "arc": "**壮大さを、3度目に別の角度から**（記録の `aim` の逐語）——"
          "⚠️ **ただしこの1本の壮大さは、広さではなく、"
          "「渡ったものが水の中に何も残さないこと」の側にある。**"
          "⛔ **感動的にしない。****この1本は、水と光と影だけの1本である。**",
   "events": "⚠️ **この1本の出来事は、人物の側には一つも無い。****影が入ってきて、"
   "ゆっくり横切り、そして消えることである。**"
   "⚠️ **この作品は、それに名を与えない**——**喪失という語も、意味づけも、この画には無い。**",
 },

 "lighting": {
   "base": "**上から来る光だけである。****星と、その水面での屈折である。**"
           "⚠️ **水中に光源は一つも無い**——**発光する生き物も、光る鉱物も、沈んだ灯も無い。**"
           "⚠️ **月も、火も、灯も出さない**（逐語, `forbidden_set`: `no fire, no torch, no lamp, no "
           "flame used as a light source`）。"
           "⚠️ **この1本の入口にあるのは同じ一つの光である**"
           "——**`s21` が空の側から見た光を、この1本は水の側から受ける。**"
           "⚠️ **彼女の第四の姿（枠の外の背後から来る水面の光）を、この1本に置かない**"
           "——**この1本の光は上からであり、そしてそのことは彼女の仕業として書かれない。**",
   "events": "**One, and it runs the whole shot.** **水面を通って入った光が、水の中で揺れつづける**"
             "（0秒から 5.744秒まで）。**そして `1.499s` から `5.744s` のあいだ、"
             "影が通るあいだだけ、その光が欠ける。**"
             "⚠️ **光源は動かない**——**様式カードの逐語:「The grade holds for the whole shot — a "
             "colour temperature that swings is a different style.」**"
             "⛔ **そしてこの1本では、光が増えない。****影が消えても、露出が開かない。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE + " ⛔ **この1本に人は一人も居ないので、"
             "声の入る余地がそもそも無い**——**語るのは歌だけである**（`l29`）。",
   "sfx": "⛔ **この1本の音は、水の音である。**"
          "**上を通るうねりの、低くこもった音。****膜が動く音。****そして `s27` から続く、"
          "櫂が水をかく音が、遠く、遅れて、鈍く届く。**"
          "⚠️ **水中の音は、こもり、そして遅れる**——**実写の物理である**"
          "（記録の `motion.law` の逐語:「水中の画も、実写の物理に従う」）。"
          "⚠️ **この1本に声は一つも無い。****息も、歌も、叫びも無い。**"
          "⚠️ **その他の船の音も、鳥の声も、帆の音も無い。**",
   "music": K.NO_MUSIC + " ⚠️ **この1本のあいだ、主題歌は `final-chorus` の2行目である**（`l29`）"
            "——**が、この1本の中には無い。****編集で載る。**"
            "**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜の、水面のすぐ下。**水、膜、そして遠くの木と縄。**"
                  "⚠️ **この1本の環境音は、この1本の画と同じくらい少ない**"
                  "——**水中には、彼の労働の音しか届かない。**",
 },

 "continuity": {
   "identity": "⛔ **この1本には、守るべき人物が枠に一人も居ない。**"
               "**ゆえに同一性の塊は §18 に貼られない**（`has_man: False`、裁定 2026-09-29）"
               "——**参照集合が `男.identity` を名乗っていても、記録の `unit` と `beats` が"
               "人物を名指さないからである。** "
               "⚠️ **この1本で守るのは、画の中の人物ではなく、"
               "この作品の人物が全編で同一であることである**——"
               "**その錠は、彼の居る31本が負う。** "
               "**May change** — **この1本では何も変わらない**——**人が画に居ないからである。**",
   "spatial": "**水面のすぐ下に視点があり、上に膜がある。****水平線はこの画に無い**"
              "——**視点が水の中にあるからである。**"
              "⚠️ **底は見えないし、写さない。****この1本の水は、"
              "深さの無い面として扱われない**——**水は体積であり、"
              "その中に視点が浮かんでいる。**",
   "temporal": "夜である。⛔ **この1本は `final-chorus` の2行目である**"
               "——**`s27`（1行目）のあとに来る。**"
               "⚠️ **この1本は `s27` と同じ水であり、同じ夜である**"
               "——**`s27` の櫂が破った膜を、この1本は下から見る。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **この1本の光は上から来る一つの光である。**"
             "⚠️ **この1本は `impossible-camera` を名乗る。****そして `impossible-camera` は "
             "§15 から何も免除しない**——**免除を名乗るのは `coexisting-realities` を名乗る4本だけである。**",
   "motion": "Full animation, not limited. **膜が動き、光が揺れ、影が通り過ぎる。**"
             "⚠️ **この1本の視点は、水に運ばれて動く。****ゆえにこの1本では、"
             "画面の側の移動が一つも無い**"
             "——**在りえないのは視点であり、動きではない。**",
   "sound": "水、膜、そして遠くの木と縄。**音楽なし。言葉なし。**"
            "⚠️ **声も、息も、そして歌も無い。**",
 },

 "must_not": K.must_not_common(has_man=False, goddess_extra=(
     "**この1本には彼も、誰も居ない**——**ゆえに女神の禁制は、"
     "「誰も現れないこと」として来る。**"
     "⛔ **この1本の光を、水中から来させない。****発光するものを置かない。**")) + [
   "⛔ **No person in this frame at any distance and in any focus, and no part of any person** — "
   "**no body, no limb, no hand, no hair, and no silhouette or reflection of one in the water above**"
   "（逐語, `forbidden_set`: `no other human being in frame — no companion, no crowd, no second "
   "person`）。**水の膜は下から見れば光しか通さない。**",
   "⛔ **The raft is never rendered as a form** — **no log, no bark, no cordage, no plank and no oar is "
   "legible in this frame: what crosses is the shadow it casts, and nothing more**"
   "（記録の `motion.subject` の逐語:「そして舟の影。」）。",
   "⛔ **No sunken thing and no drowned person** — no wreck, no timber, no hull below, no body in the "
   "water, **and no bottom: this water is just below the surface and it is not the sunken place.**",
   "⛔ **No living thing in the water** — no fish, no shoal, no creature and no weed as spectacle; "
   "**この画に生物を置けば、この1本は別の1本になる。**",
   "⛔ **No light under the water and no bioluminescence** — **the light comes from above and from "
   "nowhere else**; no glow, no spark, no luminous matter, **no fire, no torch, no lamp and no flame "
   "used as a light source**（逐語, `forbidden_set`）。",
   "⛔ **No fisheye and no distortion effect standing in for the impossible viewpoint** — "
   "**affirmatively: this is a real lens in real water, and the light bends at the surface because "
   "water bends light.** **在りえなさは視点の側にあり、レンズの側には無い**"
   "（カードの `Negative` の逐語:「no fisheye distortion standing in for an impossible viewpoint」を、"
   "**§16 の側から受け取ったうえで、ここでは肯定形で言う**）。",
   "**No time ramp and no slow motion** — **この1本の遅さは水の質量から来るのであり、"
   "時間を伸ばして作る遅さではない。**",
   "**No land, no island, no shore, no coast, no sail, no bird and no other vessel** "
   "(逐語, `海.base` と `海.geography`)——**この1本の画には水平線すら無い。**",
   "**No white water, no breaking crest, no spray and no foam** — **上から見ても、下から見ても、"
   "この海は砕けない**（逐語, `海.base` の `no white water`）。",
   "**No moon** — **この1本の光は星だけである**（`海.states.夜` の註の逐語:「光源は星と、"
   "その水面の反射だけである。」）。",
   "**No marbling, no caustic pattern, no shimmering decoration** — **光は水面の屈折によって"
   "欠け、揺れ、戻るのであり、模様として貼られない。**",
   "⚠️ **No glamour rendering of the crossing** — no grandeur, no swell of music in the image, "
   "**and nothing that congratulates the frame: 壮大さは、広さではなく、残らなさの側にある。**",
 ],
 "must": [
   "⛔ **入口が述べられること** — **この1本は舟の航跡の割れ目を通って入る**"
   "（カードの `do` の逐語:「State the entry — say how the viewpoint got where no camera can be」）。"
   "**最初のコマは、すでに水面の下である。**",
   "⛔ **この1本の視点は、水面のすぐ下から上を見ること** — **記録の `motion.quality` の逐語:「カメラは"
   "水の中にあり、上へ向いている。」** ⚠️ **視点であって、カメラの位置ではない。**",
   "**水中の光、水面の裏側、そして舟の影** — **この3つが枠にあること**"
   "（記録の `motion.subject` の逐語）。",
   "⛔ **影がゆっくり横切ること**（記録の `motion.quality` の逐語:「その影がゆっくり横切る。」）。"
   "**影は入ってきて、通り過ぎる**——**一度も加速しない。**",
   "⛔ **影が消えること** — **それが切れ目のコマである**（記録の第3のビートの逐語）。"
   "⚠️ **そのあとに説明のビートを足さない**（カードの逐語:「End on the note, not after it.」）。",
   "⛔ **径の物理が一貫していること** — **光は水面で屈折し、影は水の動きで歪み、"
   "そして水中の音はこもる**（記録の `motion.law` の逐語）。"
   "**この物理は5.744秒のあいだ変わらない。**",
   "**水面の裏側が絶えず動いていること** — **記録の `motion.quality` の逐語:「水面が上で波立ち」"
   "——`held` を一つも使わない。**",
   "⛔ **到着があること** — **この視点は、影が消えたあとの水の中で終わる。**"
   "**残るのは膜と光だけである**（カードの `do` の逐語:「End on an arrival that carries the shot's "
   "meaning」）。",
   "**This frame holds no person at all** — no body, no limb, no hand and no hair, **and the identity "
   "block is not pasted into §18**（`has_man: False`、裁定 2026-09-29"
   "——**記録の `unit` と `beats` が人物を名指さないからである**）。",
   "⛔ **切らない。** **1本は1つの画である。**",
   "⚠️ **`impossible-camera` の5つを満たすこと** — `EYE`・`ENTRY`・`PATH`・`ARRIVAL`・`DURATION`"
   "（§8）。",
 ],
 "prefer": "The shadow read as an absence of light rather than as an object; **its edge soft and "
           "continuously redrawn by the surface**; the light swaying in the water at the swell's own "
           "period; **the surface's underside carrying both the compressed sky and the mirror, with the "
           "boundary between them moving**; the water dark, with the suspended matter catching just "
           "enough light to hold the frame.",
 "allow": "Weed passing near the surface as a dark thread and nothing more; the swell lifting the whole "
          "frame; the viewpoint drifting with the water in the shadow's own direction; the light going "
          "out of the frame as the shadow crosses; **an arrival that leaves the frame in water and "
          "still moving.**",

 "priorities": [
   "⛔ **在りえなさが視点の側にあること** — **レンズの歪みで作った在りえなさは、この1本を壊す。**",
   "⛔ **入口が述べられていること** — **述べなければ、この1本は前の1本のミスとして読まれる。**",
   "⛔ **径の物理が一貫していること** — **屈折と歪みは、5.744秒のあいだ同じ法則である。**",
   "⛔ **影が消えるところで終わること** — **到着の無い1本は、旅を使って何も残さない。**",
   "⛔ **人を一人も写さないこと** — **水の膜は下から見れば光しか通さない。**",
   "⛔ **舟を形として写さないこと** — **渡るものは影としてだけ来る。**",
   "⚠️ **速くしないこと** — **時間を伸ばせば、この水は水でなくなる。**",
   "⚠️ **光を一つに保つこと** — 水中の光源も、月も、灯も無い。",
   "**The frame holds no person, and the identity block is not pasted into §18**"
   "（`has_man: False`、裁定 2026-09-29）。",
   "⚠️ **`impossible-camera` の5つを満たすこと** — `EYE`・`ENTRY`・`PATH`・`ARRIVAL`・`DURATION`。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `impossible-camera` を名乗る。****カード自身の禁制（`no conventional camera "
   "position`・`no unstated entry`・`no cut`・`no fisheye distortion standing in for an impossible "
   "viewpoint`・`no path that changes its own physics`・`no shot without an arrival`）は §16 の側から"
   "届く**——**ここには書かない。** **ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"
   "⛔ **そしてこの経路では、その `Negative Prompt` は床として受け取られない**（`L30`）"
   "——**ゆえにこの1本では、入口・径の物理・到着が、"
   "すべて肯定形で §18 の散文にも書かれている。**"),

 "master": (
   "A 5.744-second impossible-camera take (16:9) inside the water of the open sea at night, just below "
   "the surface, looking up, one clip, no cut, one viewpoint: **the journey of a viewpoint that cannot "
   "exist — it is in the water, and the raft's shadow crosses above it and passes.**\n\n"
   "**This shot arrives here through the water the raft has broken** — the entry is stated: **the "
   "viewpoint comes in through the raft's own wake, the one break on the surface, and the first frame "
   "is already under it.** Above, the underside of the surface is the ceiling of the frame and it is "
   "never still.\n\n"
   "0-1.499s: **underwater, with the surface above.** **The raft has not entered the frame.**\n"
   "1.499-3.498s: **a shadow crosses, slowly** — a region where the light from above is missing, its "
   "edge redrawn by the moving surface; **the light sways in the water.**\n"
   "3.498-5.744s: **the shadow passes over and is gone** — the surface distorts, the light comes back, "
   "**and the take ends on the shadow disappearing.**\n\n"
   "**No person is in this frame at any distance and in any focus, and no part of any person is in it, "
   "including any reflection or silhouette above the surface.** **The raft is never shown as a form: no "
   "log, no bark, no cordage, no plank and no oar is legible — only the shadow it casts crosses the "
   "frame.** **The light comes from above and from nowhere else: no light source is in the water, no "
   "glow, no spark and no luminous matter, and no fire, torch or lamp.** **This is real water and a "
   "real lens — the light bends at the surface, and what is above is compressed into the cone through "
   "which it can be seen; it is not a fisheye and not a distortion effect.** **No time ramp and no slow "
   "motion is used: the slowness is the water's own mass.** **There is no bottom, no wreck and no "
   "drowned thing; no fish, no creature and no weed as spectacle.** **No land, no island, no sail, no "
   "bird and no other vessel appears; there is no white water, no spray and no breaking crest, and no "
   "moon.** **No blood, no wound and no corpse.** **This is a bronze-age sea before classical Greece.** "
   "**This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one viewpoint: the shadow crosses above and is gone.)"),

 "visual_scene": (
   "Inside the water of the open sea at night, just below the surface, looking up: **the underside of "
   "the surface is the ceiling of the frame and it is never still** — a moving skin, shot through with "
   "the sky's light, which is **compressed into one region where the sky is visible and is a mirror "
   "everywhere else, reflecting the dark water below it**; the swell passes through it so that it lifts "
   "and falls and gathers fine wrinkles. The water the viewpoint floats in is dark and almost "
   "formless, **with fine suspended matter catching just enough light to hold the frame** and no rock, "
   "no sand, no bottom, no wreck and no living thing in it. **Through this, a shadow crosses above the "
   "viewpoint from one side of the frame to the other, slowly — a region where the light from above is "
   "missing, with no shape of its own and no detail in it, its edge soft and continuously redrawn by "
   "the moving surface** — and then the surface distorts, the light comes back, and the shadow is gone. "
   "**No log, no bark, no cordage, no plank and no oar is legible anywhere in this frame.** "
   "**No person is in the frame at any distance or in any focus, no part of any person is in it, and "
   "nothing above the surface is legible except its light and the shadow that blocks it.**"),

 "visual_meta": (
   "Wide underwater optics with a real lens's fall-off and a moderate depth of field; **the framing is "
   "not a fisheye and does not bend the frame's edges** — the light bends at the surface because water "
   "bends light. **A graded palette of one dark value: black water, a surface underside a shade above "
   "it, the sky's light compressed into one region, and the shadow that is the absence of that light.** "
   "Fine suspended matter throughout, catching the light and no more; the surface's underside as a "
   "moving skin, its light breaking into cells and reforming; the shadow's edge soft and never a clean "
   "line; **even film grain over everything, and the grain is a large part of what this frame is made "
   "of.** No painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration. "
   "⚠️ **The frame is dark and almost empty by design** — the only bright thing in it is the light that "
   "comes down through the surface, and the only event in it is that light going away and coming back."),

 "motion_prompt": (
   "Full animation, not limited, one continuous take with no cut. **The surface's underside is the "
   "ceiling of the frame and it moves in every frame of the take** — it lifts and falls with the swell "
   "and gathers fine wrinkles, and **the light that comes down through it sways in the water at the "
   "swell's own period, fine cells of light breaking apart and reforming.** **From one side of the "
   "frame a shadow crosses above the viewpoint, slowly, and it has no shape of its own: it is a region "
   "where the light from above is missing, its edge soft and continuously redrawn by the moving "
   "surface, so that its outline changes even while it travels at a constant rate.** **The shadow "
   "passes over, and as it goes the surface distorts and the light comes back, and the take ends on the "
   "shadow disappearing.** **The whole shot is slow because water has mass: nothing accelerates, "
   "nothing snaps, and no time ramp is used.** **There is no person and no part of a person in this "
   "frame at any point, and no log, no bark, no cordage, no plank and no oar is ever legible in it.** "
   "No motion blur smears, no stutter, no floaty weightless motion, no static frames — **the water "
   "moves in every frame of the take.**"),

 "camera_prompt": (
   "**A viewpoint that cannot exist: inside the water, just below the surface, looking up.** "
   "**The entry is stated** — **the viewpoint comes in through the raft's own wake, the one break on "
   "the surface, and the first frame is already under it, so the shot reads as continuing from the "
   "previous one rather than as an error in it.** **The path has its own law and keeps it: in this "
   "water the light bends at the surface, what is above is compressed into the cone through which it "
   "can be seen, and the surface's underside is a mirror everywhere outside that — and none of this "
   "changes at any point in the shot.** **The style permits a dolly, a crane and a Steadicam; this shot "
   "spends neither** — **what carries the viewpoint is the water itself: it floats with the swell, "
   "rises and falls with it, and drifts slowly in the same direction and at the same rate as the "
   "shadow, so no rig is used and none is needed.** "
   "**This composes the existence of a viewpoint, not the movement of a camera "
   "placed at a point.** **And the shot arrives: at the end the shadow has passed and is gone, the "
   "surface is still moving, and the viewpoint is left in the water — that is where this shot's meaning "
   "is.** No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, and no "
   "unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water heard from inside it — the low, muffled passage of "
   "the swell overhead, the surface moving as a skin, and, distant and late and dull, the sound of the "
   "oar working the water from the previous shot.** ⚠️ **Sound in this shot is muffled and delayed by "
   "the water, which is the physical law of the shot and does not change.** ⚠️ **There is no human "
   "sound of any kind** — no voice, no breath, no song and no shout. ⚠️ **There is no other vessel, no "
   "bird and no sail to be heard, and no white water and no spray: this sea does not break.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (impossible-camera) ／ "
                        "`REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②）。"
                        "⛔ **この1本は画に人が一人も居ないので、同一性の塊は §18 の `Master Prompt` にも "
                        "`Visual Prompt` にも貼られていない**（`has_man: False`、裁定 2026-09-29）"
                        "——**参照集合が `男.identity` を名乗っていても、記録が人物を名指さないからである。**"
                        "⚠️ **参照集合は `男.identity`・`男.negatives`・`海`・`海.geography`・`海.states.夜`・"
                        "`舟`・`舟.appearance`・`舟.negative` の8鍵である**——"
                        "**`s26`・`s27` と同じ8鍵である。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water heard from inside ／ no music",
 "unresolved": [
   "⚠️ **この1本に彼の姿を入れるかどうかを、記録は書いていない。**"
   "⚠️ **記録の `motion.subject` は3つを名乗り、そのどれも人ではない**"
   "（逐語:「水中の光、水面の裏側、そして舟の影。」）。"
   "**この仕様は「入れない」と読んだ**——**根拠は3つある。**"
   "① **平台は不透明であり、上に居る体は下から見えない。**"
   "② **夜の水面は下から見れば鏡であり、上にあるものは光としてしか来ない**"
   "（記録の `motion.law` の逐語:「光は水面で屈折し」）。"
   "③ **`unit.after` の逐語も「舟の影」であって「彼」ではない。**"
   "⛔ **ゆえにこの1本の画には、人も、人の一部も、その反映も入らない。**"
   "✅ **裁定 2026-09-29 が、この読みを認めた**——**記録が人物を名指さない1本は、"
   "同一性の塊を落とす。****この1本は `has_man: False` である。**"
   "**上の3つの根拠は、そのまま残す**（**裁定は「塊を落とす」であって、"
   "「読みを消す」ではない**）。",
   "⚠️ **「舟の影」を、舟そのものとして描かないと読んだ。**"
   "⚠️ **記録は `影` と書き、`舟` とは書かない。**"
   "**ゆえにこの1本の画には、丸太も、縄も、板も、櫂も読めない**"
   "——**夜の水の下から見えるのは、光の欠けた領域だけである。**"
   "**舟を形として見せたければ、この読みは変わる。**",
   "⚠️ **入口をどこに置くかを、記録は細かくは決めていない。****この仕様は"
   "「舟の航跡の割れ目」を採った**——**`海.base` の逐語が航跡を"
   "「この面の唯一の割れ目」と書いているからである。**"
   "⚠️ **`s27` の櫂が破った水を入口にする読みも在りうる**"
   "（**`s27` は同じ夜の、すぐ前の1本である**）。**どちらが正かは著者が決める。**",
   "⛔ **記録自身が、この形式の名はまだ検査されていないと書いている**"
   "（逐語:「ショット記録に `REF_FORMAT` の欄は無い——形式は仕様（§6）の側にある。"
   "ゆえにここに書いた形式は、まだ検査されていない。」）。"
   "**この仕様は、その提案どおり `impossible-camera` を §6 に書いた**"
   "——**ショット記録に欄が無いので、この形式名を記録と突き合わせる検査は無い。**",
   "⛔ **「壮大さ」を、機械は測れない。****測れるのは「影が入り、横切り、そして消えること」"
   "と「膜が全フレームで動いていること」までである。**"
   "**その先（それが水を渡ることとして読めるか）は、絵を見て著者が決める。**",
   "⚠️ **水中の音の扱いを、記録は決めていない。****この仕様は「こもり、遅れる」を採った**"
   "——**記録の `motion.law` が「水中の画も、実写の物理に従う」と書くからである。**"
   "**水中の音を消す（あるいは水中の音を付けない）読みも在りうる。**",
   "⚠️ **`video-spec` の `DURATION` の括弧書き。** カードは逐語で「the model decides the duration」と"
   "言うが、**この作品では曲が長さを決める**（`bible.time_source: song`）。"
   "**この仕様は曲の側を採った**——**§1 の `Duration` は記録の逐語である**（`L23`）。"
   "⚠️ **この1本は `s27` の直後であり、`29` 秒台の後半に在る。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**"
   "⚠️ **そしてこの1本では、黒帯が入れば、水の中の暗さと黒帯が"
   "見分けにくくなる**——**この1本だけの問題である。**",
 ],
 "risks": [
   "⛔ **レンズの歪みで「在りえなさ」を作る。** ⚠️ **この1本のいちばん高い危険である**"
   "——**この経路は、水中の画を魚眼で作る。****この1本の在りえなさは視点の側にあり、"
   "そして在りえなさは、レンズでは作れない。**",
   "⛔ **人が写る（あるいは人の反映が膜に写る）。** ⚠️ **この経路は、水中の画に人影を足しやすい**"
   "——**この1本の画は、光と膜と影だけである。**"
   "⚠️ **裁定 2026-09-29 で同一性の塊は §18 から落ちたが、"
   "この危険は消えていない**——**§16 と §18 の散文の側で禁じられている。**",
   "⛔ **舟が形として写る（丸太・縄・板）。** ⚠️ **渡るものは影としてだけ来る。**",
   "⛔ **入口が述べられない。** ⚠️ **述べなければ、この1本は前の1本のミスとして読まれる**"
   "（カードの `avoid` の逐語）。",
   "⛔ **到着が無い。** ⚠️ **影が消えるところで終わらなければ、この1本は旅を使って何も残さない。**",
   "**水中の光源が入る（発光・光る生き物・沈んだ灯）。**"
   "⚠️ **それを足せば、この1本の光は上から来なくなる。**",
   "**沈んだもの・沈んだ者が写る。** ⚠️ **この作品に `沈んだ場所` が在るので、"
   "この経路は水の中の画にそれを置きやすい**——**この1本は水面のすぐ下である。**",
   "**月が写る。** ⚠️ **この1本の光源は星だけである**（`海.states.夜` の註の逐語）。",
   "**時間を伸ばして遅さを作る。** ⚠️ **この1本の遅さは水の質量から来る。**",
   "**白波が立つ、砕ける。** ⚠️ **この海は白波を立てない**（逐語:「no white water」）。",
   "**光が模様として貼られる（コースティクス・装飾的な網目）。**"
   "⚠️ **この1本の光は、屈折によって欠け、揺れ、戻るのである。**",
   "**`s21` と同じ画になる。** ⚠️ **対ではあるが、同じではない**"
   "——**`s21` は上から、この1本は下からである。**",
 ],
}

if __name__ == "__main__":
    print("s28 content OK — keys:", len(C))
