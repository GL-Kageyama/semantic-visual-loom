# -*- coding: utf-8 -*-
"""odyssey-s11 — impossible-camera — 森の洞口 / 夜 / 6.782s. The man is here; she is never shown."""
import common as K


C = {
 "n": "s11",
 "title": "私の顔を見ている——見る主体を写さない",
 "duration": "6.782",
 "format": "impossible-camera",
 "has_man": True,
 "segment": "pre-chorus-3",

 "band": [
   "『永遠より遠い』 pre-chorus「森の洞口」 / 反応 / still —— 私の顔を見ている——見る主体を写さない",
   "黒い洞の前に男の横顔があり、誰かが見ていることが画面の側に残る。",
   "6.782秒、カメラだけが彼の目と同じ高さへゆっくり上がる——彼が一度も視線を動かさないのが、切れ目である。",
   "見ている者は写されず、光源も動かない——彼は、見返さない。",
 ],
 "header": """⛔ **この一行が、女神に顔を与えない設計の出所である。** 出所は曲の `l08`「私の顔を見ている」——⛔ **写るのは、見られている男の顔である。****彼女の顔ではない。**
⚠️ **この読み替えが、裁定②（参照なし）と `world.rules` の二番を同時に満たす。** **彼女を写さずに、彼女が居ることを写す1本である。**
⛔ **形式は `impossible-camera`**——**物理的に存在しえない視点**である。**彼女の位置は、この作品で唯一カメラが立てる場所である。**
⚠️ **この形式をこの作品で使うのは4本である**（`s11`・`s21`・`s28`・`s33`）。
⚠️ **`mode: still`。****止まるのは主題である**——**見られている者は動かない。**
⚠️ **行: `l08` ／ 場所: `森の洞口` ／ 時刻: `夜` ／ 尺: 6.782秒。**
⚠️ **参照集合に `女神.negatives` を持つ**——**この作品でその3本目である**（`s09`・`s10`・`s11`）。
⚠️ **この仕様のショット記録は `shots/odyssey-s11.yaml` である。**""",

 "intent": "One continuous take of one change — **ごく弱い光が彼の頬に着き、そして留まる。** 最初のコマでは彼の横顔は暗く、**光は一つも当たっていない。** 最後のコマでは頬に光があり、**彼は一度も視線を動かしていない**——⚠️ **動かさないことが、切れ目のコマである。** ⛔ **この視点は、この作品でカメラが立てる唯一の場所である**——**彼女の位置であり、彼女は写らない。** ⚠️ **切らない。視点を変えない。** 形式カードの逐語:「**the shot is the journey of a viewpoint, and the journey is the time**」——**この1本の時間は、この視点が在ることそのものである。** ⚠️ **変化は切れ目のコマで終わる**——**彼が動かないまま、この1本は終わる。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、この作品で唯一「見る側」を写さない1本である。**——`s09` と `s10` は洞口で彼女の声と"
   "気配を立て、**この1本は同じ夜の同じ場所で、彼女が見ている側だけを写す。** "
   "⛔ **ゆえに彼女の顔は、この作品のどこにも無い**——**顔を与えれば、この作品は神話の映像化になる。**"
   "**この1本が写すのは、見られている男の顔である。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本は、返事がいちばん近いところにある1本である**——**見られている者は、"
               "見返すことができる。****ゆえに彼は一度も視線を動かさない。**"
               "**動かないことが、この作品の返事の代わりである。**",
     "goddess": "⛔ **この1本の視点は、彼女の位置である。****それでも彼女は四つの姿のうち二つとしてしか"
                "現れない**——**面の上の温かさと、洞から出てくる空気である。** "
                "⚠️ **顔も、体も、輪郭も無い。****第一の姿（枠の外の低い女声）は、この1本では使わない**"
                "（§20 を見る）。",
     "name": "⚠️ **この1本に名は無い。** 曲の `l08` は「私」と「あなた」しか言わない——"
             "**名指せば、この作品は説明になる。**",
     "bow": "⚠️ **この1本に持ち手が無い。****弓は無論のこと、斧すら無い**——"
            "**彼は何も持たずに、暗い中に立っている。**",
     "places": "この1本が置くのは一つ——`森の洞口`、**この作品で唯一、女神が実在する場所である。**"
               "⚠️ **この1本はその場所を立て直さない**——`s02`・`s09`・`s10` と同じ洞口である。",
     "japanese": "⚠️ **この1本には歌がある**——`l08`「私の顔を見ている」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **見返さないことは、この作品では返事をしないことである。** ⚠️ **この1本は、その規則がいちばん"
     "危うい1本である**——**見られている者は、見返すことができるからである。**",
     "⚠️ **この1本の光は、火でも灯火でもない**（`bible.negative_base` が全ショットで火を禁じている）。"
     "**頬に当たる温かさは、この作品では彼女の第二の姿である。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "A wooded slope at night on a bronze-age island, photographed as a film: rough grey rock split into a "
     "wide low opening whose interior is wholly unlit, dense low scrub and thin trees crowding right up to "
     "the stone. ⚠️ **Only the rock, the scrub and one man's head and shoulder are in this frame** — no "
     "ground under him, no horizon behind him, no made thing at the opening. ⚠️ **No marble, no columns, "
     "no architecture of any later age.**",
   "Color Language":
     "Almost no colour at all: a cold slate grey in the moonlit rock, a warmer near-black in the opening's "
     "shadow, and **the skin carried as the one warm value in the frame** — the cheek where the glow "
     "falls. ⚠️ **That warmth is the shot's only warm note and it appears at 2.001秒** — before it, the "
     "frame is grey and black only.",
   "Texture":
     "Rough grey rock with cracks and old water-marks; dry scrub leaves at the edges of the frame; skin "
     "roughened and marked, the beard's individual hairs legible; the unlit opening a flat, grainless "
     "black. ⚠️ **No water is in this frame and nothing on it is wet.** ⚠️ **No cloth is in this frame** "
     "— the shoulder is bare and the tunic is out of the frame's reach. Film grain present and even.",
   "Visual Density": "Very low. **The frame holds one thing — a face in profile — and the dark around it.**",
   "Atmosphere": "The moment when being looked at is the whole of the frame, and no one is there to be seen.",
   "Time": "`夜` — the same night as `s09` and `s10`, on the slope at the cave mouth. **The work does not "
           "fix a date.** ⚠️ **The light in this frame does not change with the hour** — there is no sun "
           "in it; what changes is the glow on his cheek.",
 }),

 "subjects": [
   K.man_subject(
     behavior="**彼は立ったまま、動かない。**横顔が枠の左側にあり、**視線は枠の外の一点にある。**"
              "⚠️ **彼はその点から目を離さない**——**この6.782秒のあいだ、まばたきのほかは何も動かない。**"
              "⚠️ **彼はレンズを見ない。**",
     may="頬の上の光の位置、暗さの縁、カメラの高さ、そして**まばたきの間隔**。",
     extra_notes=[
       "⚠️ **この1本の主題は「見られている」ことである**——**彼は変わる者ではなく、変えられる者である。** "
       "カードの逐語:「**Compose the viewpoint's existence, not the movement of a camera placed at a "
       "point**」——**この1本では、存在するのが視点であり、動かないのが彼である。**",
       "⚠️ **彼は何も持たない。****弓も、斧も、道具も無い**——**手は体の側にあり、枠の中でも動かない。**",
       "⚠️ **`s05` が立てた顔の基準から外れない。****この1本は顔の側から写す**——"
       "**参照画像が1枚も無いので、守る道具は英文の塊だけである。**",
     ]),
   {"name": "光",
    "ref": "⛔ **この1本の第二の主題である。** ⚠️ **光源は枠の外にあり、この作品は最後までそれを名指さない。**"
           "**ゆえに固定するのは「何であるか」ではなく、どこに当たり、どう動くかである。**"
           "⚠️ **この1本は彼女の第二の姿だけを、光として写す1本である。**",
    "appearance": "**ごく弱い、拡散した光である。**輪郭を持たず、点にもならない。"
                  "**当たる面だけが少し明るくなる**——頬、顎の線、髭の一本ずつ。"
                  "⚠️ **光源は一度も枠に入らない**——**入れば、それは灯火である。**"
                  "⚠️ **光は月でも星でもない**（それらは岩と空の側にあり、彼の頬には届かない）。",
    "behavior": "**2.001秒に、光が彼の頬に着く。****そして留まる**——動かない。"
                "⚠️ **広がりもしない**——**当たる場所が少しずつ面になり、そこで止まる。**"
                "⚠️️ **この1本で動くのは、光と空気だけである。**",
    "continuity": "**Must preserve** — 光の弱さ、方向（枠の外から）、色温度（肌の側の温かさ）、"
                  "そして**枠の中に光源が現れないこと**。**May change** — 当たる面の広さ、明るさの段、"
                  "髭と肌のどこが先に明るくなるか。",
    "notes": ["⚠️ **`cinematic-still` の規則がこの1本でいちばん厳しく効く**——**「光は演出的である」であり、"
              "「専用の光源を持たない」。****この1本の光は、枠の外から来る一度きりのものである。**",
              "⛔ **光を強くしない。****強くなれば、この1本は照らされている画になり、見られている画でなくなる。**"]},
   {"name": "森の洞口",
    "ref": "**この1本の場所である。** ⚠️ **参照は `ledger.locations.森の洞口` の `geography` と `states.夜` である。**"
           "⚠️ **`s02` が場所の基準を立てた**——**この1本はそこから外れてはならない。**",
    "appearance": "**粗い灰色の岩、広く低い開口部、そして絶対的な黒。****内側は一度も見えない。**"
                  "開口部の縁に、潅木と細い木が迫っている。",
    "behavior": "**洞から出てくる空気が、枠の縁の潅木を動かす。** ⚠️ **黒は動かない**——"
                "**黒は黒のままである。**",
    "continuity": "**Must preserve** — 開口部の位置と形、岩の割れ目の走り、潅木のbank、そして"
                  "**「内側が見えない」こと**。**May change** — 潅木の葉の向き、黒の縁、空気の強さ。",
    "notes": ["⚠️ **この1本は場所を立て直さない**——**`s02`・`s09`・`s10` と同じ洞口である。**",
              "⛔ **内側は、この1本でも一度も見えない。**"]},
 ],

 "environment": {
   "location": "`森の洞口` — **この作品で唯一、女神が実在する場所である。** ⚠️ **岸から内陸へ上がった斜面の、"
               "いちばん奥である。****この1本はその場に、彼女の側から立つ。**",
   "elements": "夜の粗い灰色の岩、広く低い開口部、**内側の見えない黒**、開口部に迫る潅木と細い木、"
               "**そして洞から出てくる空気。** ⚠️ **地面は枠の下に見えない。** ⚠️ **人工物を一つも置かない**"
               "——**敷居も、段も、刻みも、灯火も無い。**",
   "behavior": "**空気が洞から出て、枠の縁の潅木を動かす。****月と星は岩を照らすが、彼の頬には届かない。**"
               "⚠️ **黒は動かない**——**動くのは、黒と肌の境である。** ⚠️ **場所は彼に反応しない**"
               "——**彼が動かないのと、場所が動かないのは、別のことである。**",
 },

 "objects": [
   "**無し。** ⚠️ **この1本に小道具は来ない。** **この作品の小道具は4つだけであり**（`ledger.props`）、"
   "**そのどれもこの夜の洞口には来ない**——**舟も、帆も、斧も、太陽の牛も、まだ彼の手に無いか、"
   "まだ記憶にすら無い。**",
   "**洞から出てくる空気**, moving the scrub at the edge of the frame — **この1本で動く二つのうちの一つである。**",
   "**頬に当たる光**, arriving from outside the frame at 2.001秒 — ⚠️ **これは物ではない。**"
   "**この1本の記録は、これを主題として扱う**（§3 の「光」を見る）。",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — ⛔ **この1本に添付しない。****彼女は四つの姿のうち二つとしてだけ現れ、"
                  "顔も体も持たない**——**ゆえに §6 に貼るのは `女神.negatives` の側である**（台帳の註）。"
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`女神.negatives`・`森の洞口`・"
                  "`森の洞口.geography`・`森の洞口.states.夜` の6鍵である。"
                  "⛔ **`女神.identity` は引かない**——**引けば、この1本は彼女を写す1本になる。**",
 "ref_extra": [
   "- ⚠️ **形式カード `impossible-camera` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; "
   "what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §6 のこの一行と、§16 に運んだカード自身の禁制である。**",
   "- ⚠️ **形式カード `impossible-camera` の5つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `EYE`＝the viewpoint that cannot exist — ⛔ **彼女の位置である。****この作品で彼女は体を持たない**"
   "——**ゆえに、そこにカメラは立てない。****この1本は、立てない場所に立つ。**",
   "  - `ENTRY`＝how the shot arrives at it — ⛔ **光である。****最初の2.001秒、枠は暗い。**"
   "**そして枠の外からごく弱い光が彼の頬に着く。****その光が立っている側が、この視点である**"
   "——**カメラは彼女の位置へ歩いて行かない。****光とともに、そこに在る。**"
   "⚠️ **入口を言わない視点は、前のショットの継続エラーとして読まれる**"
   "（カードの逐語:「An unstated entry reads as a continuity error in the previous shot rather than as "
   "this grammar」）。",
   "  - `PATH`＝what the viewpoint travels through — **暗さそのものである。**"
   "**この1本の道には目盛りが無い**——**近さも遠さも測るものが無く、したがって速さも無い。**"
   "**あるのは、頬の高さから目の高さまでの、手のひら一つぶんの上昇だけである。**"
   "⚠️ **カードの逐語:「Give the path its own law of scale and physics, and keep it consistent inside "
   "the shot」**——**この道の法は「光が動くぶんしか動かない」であり、この1本のあいだ変わらない。**",
   "  - `ARRIVAL`＝where the shot leaves the viewer — ⛔ **彼の顔である。****光はまだ頬にあり、"
   "彼は一度も視線を動かしていない。****観客は、彼女が立っている場所に置き去りにされる**"
   "——**見られていることが、返事をされないまま終わる。**"
   "⚠️ **カードの逐語:「The shot arrives somewhere. … Leaving the viewer inside with no arrival spends "
   "the journey and keeps nothing.」**",
   "  - `DURATION`＝clip length — **`6.782s`。**",
   "- ⚠️ **この形式をこの作品で使う4本**（`s11`・`s21`・`s28`・`s33`）**は、互いに別の視点である**"
   "——**この1本は「見る者の位置」であり、他は運動と対話である。**",
 ],

 "narrative": {
   "core": "**光が、彼の頬に着く** — 見る主体を一度も写さずに、「見られている」が立つ。",
   "beginning": "**暗い中に横顔がある。****光は当たっていない。** 目と、鼻の線と、髭だけが暗さから出ている。",
   "turn": "**ごく弱い光が、枠の外から頬に着く。****光源は枠に入らない。** 彼は動かない。",
   "peak": "**光が頬に留まり、面になる。** 顎の線と、髭の一本ずつが明るくなる。",
   "pull": "⚠️ **彼が一度も視線を動かさないことが、切れ目のコマである。**"
           "**光は最後のコマまで当たり続け、彼は最後のコマまで動かない。**"
           "**見られていることは、返事をされない。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.279秒.** 最初の2.001秒は**暗さのために払われる**"
            "——**まだ何も起きていないことが、この1本の前提である。** 次の2.502秒で**光が着き、"
            "最後の2.279秒がこの1本の出来事である。** ⚠️ **`held` を1つも使わない。** "
            "止まるのは主題であって、画面ではない——**光と空気は最後のコマまで動いている。**",

 "actions": [
   ("ACT_DARK", "洞口の黒と、その前の横顔。",
    "**横顔が暗さから出ている**——**光は一つも当たっていない。**"),
   ("ACT_ARRIVE", "頬に光が無い。",
    "**枠の外から、ごく弱い光が頬に着く**——**光源は枠に入らない。**"),
   ("ACT_SPREAD", "光は一点である。",
    "**光が面になる**——頬、顎の線、髭の一本ずつが明るくなる。"),
   ("ACT_HOLD", "彼は動かない。",
    "**光が当たり続け、彼は一度も視線を動かさない**——**そのコマが、この1本の切れ目である。**"),
 ],

 "camera": {
   "language": "Third person — ⛔ **and the third person is her place.** The viewpoint stands inside the "
               "darkness at the cave mouth, at the height of the man's cheek, and rises only to the height "
               "of his eyes. ⚠️ **この1本のカメラは、物理的に存在しえない一つの場所である**"
               "（形式カードの逐語:「the premise \"the camera is at a place\" is dropped」）。",
   "events": "One event only. `0-2.001s` — **the viewpoint holds where it is, at the height of his cheek, "
             "and there is no light**; then `2.001-4.503s` — **the light arrives from outside the frame, "
             "and the viewpoint is where the light is standing**; then `4.503-6.782s` — **the viewpoint "
             "rises to the height of his eyes at the light's own pace and stops, and it does not move "
             "again.** ⚠️ **動機は光である。** ⚠️ **この1本は一度も彼へ寄らない**——"
             "**寄れば、この1本は顔の大写しになり、視点であることをやめる。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the crane** "
               "— a rise of less than a hand's width with the low frequency of a rig that has mass, and it "
               "does not wobble. No dolly is used and no Steadicam: the viewpoint does not travel sideways "
               "and it does not follow anything. ⚠️ **止まったあと、視点は動かない。** "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, and "
               "**no unmotivated move.** ⚠️ **fisheye で「不可能な視点」を代用しない**"
               "（カードの逐語:「no fisheye distortion standing in for an impossible viewpoint」）。",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、顔の上の光である。** ⚠️ **男は動かない**——"
              "**見られている者は動かない**（`mode: still`）。**頬に光が着き、面になり、留まる。**"
              "⚠️ **光そのものは動かない**——**動くのは、当たる場所の広さである。**",
   "object": "**動く物は無い。****彼は何も持たず、何も置かれていない。** ⚠️ **この1本に物的な運動は"
             "一つも無い**——**あるのは、光の着くことと、空気だけである。**",
   "environment": "**洞から出てくる空気が、枠の縁の潅木を動かす。** ⚠️ **波はこの1本に無い**"
                  "——**内陸である**（`s02` と同じ）。**月と星は岩の側にあり、空は枠の上端にある。**"
                  "⚠️ **海は遠く下にある**——**音の側にだけ、その気配がある**（§14）。",
   "weight": "**この1本に重さを持つ物は無い。** ⚠️ **彼は立っているが、体重は画の外である**"
             "——**枠の下に地面が見えない。****重さが現れるのは、まばたきの側である。**",
   "inertia": "**慣性を持つものが無い。****光は着いた場所に留まり、空気は潅木の葉を少しだけ行き過ぎさせる。**"
              "⚠️ **彼には慣性が無い**——**動かないものは、遅れて止まることもない。**",
   "acceleration": "**加速しない。****光は一様に着き、空気は突風として来ない。** "
                   "⚠️ **この1本に速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この6.782秒に、止まったフレームは"
               "一つも無い**——**光と空気は最後のコマまで動いている。**"
               "⚠️ **`mode: still` は「静止画」ではない**（`s06` の註の逐語:「止まるのは主題であって、"
               "画面ではない。**光と埃とカメラは動く**」）。",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**光が着くことは、打撃ではない。**"
             "**音を立てない変化である。**",
 },

 "emotion": {
   "arc": "**見られている。****そして、見返さない。** ⚠️ **この1本の感情は、彼の側には無い**"
          "——**観客が、彼女の位置に置かれることで生まれる。**"
          "**誰かがそこに居るのに、誰も写っていない。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしの動きでもない。****光が着いて留まることである。** "
             "**彼は何も答えない**——**答えないことが、この1本の全部である。**",
 },

 "lighting": {
   "base": "The moon and the stars, falling on the rock and on the scrub and **not reaching his cheek**; no "
           "fill, no artificial source, and **no light source anywhere inside the frame.** ⚠️ **この1本の"
           "光源は二つである**——**ひとつは空の光であり、もうひとつは枠の外から来る温かさである。** "
           "⚠️ **火は一つも無い。**",
   "events": "**One, and it is the whole shot.** `2.001秒` に温かさが頬に着き、**面へ広がり、そして留まる。** "
             "⚠️ **光源は動かない**——**様式カードの逐語:「The grade holds for the whole shot — a colour "
             "temperature that swings is a different style.」** ⚠️ **この1本の明るさは、彼の頬の上でだけ"
             "上がる**——**画全体の色温度は動かない。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**洞から出てくる空気が、乾いた潅木の葉をこする音。****そして遠く下の海。** "
          "⚠️ **この1本に人の音は一つも無い**——**彼は動かず、息だけがある。** "
          "⚠️ **洞の中から何も喋らない**——**この1本で彼女は見ており、見ることは返事ではない。**",
   "music": K.NO_MUSIC + " ⚠️ **そしてこの1本には、歌が在る**——`l08`「私の顔を見ている」である。"
            "**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜の洞口。**空気、乾いた葉、そして遠くの海があることの気配。** "
                  "⚠️ **呼ぶ声は無い**——**この1本は、黙って見ている側の1本である。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="**体格・肌・髪・髭・顔・傷・着ている一枚と、着ていないすべて・裸足であること。** "
                "⚠️ **この1本は横顔である**——**横顔は、この作品でいちばん顔の形が読まれる角度である。**"
                "**ゆえにこの1本も、`s05` が立てた顔から外れてはならない。**",
     may="頬の上の光の位置、暗さの縁、カメラの高さ、まばたきの間隔、髭のどの一本が先に明るくなるか。"),
   "spatial": "**洞口は斜面の奥にあり、開口部は海側を向いている**——`s02` が立てた地理である。"
              "⚠️ **この1本は地面を写さない**——**枠の下に岸は無く、海も無い。**"
              "**あるのは岩と、潅木と、横顔だけである。** ⚠️ **視点は彼女の側にあり、彼は視点の側を"
              "見ない**——**視線は枠の外の一点にあり、その点はこの作品のどこにも写らない。**",
   "temporal": "**`s09` と `s10` と同じ夜である。** ⚠️ **この1本は、彼女が喋ったあとの夜の中にある**"
               "——**弧として、この1本は `l08` の1行だけを負う。** 画の中に日付を与えるものは何も無い。",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は月と星、そして枠の外から来る温かさだけである。**"
             "⚠️ **この1本は `impossible-camera` を名乗るが、この形式は §15 から何も免除しない**"
             "——**免除を名乗るのは、`coexisting-realities` を名乗る4本（`s07`・`s15`・`s22`・`s29`）だけである。**"
             "**この1本の場所と時刻は、台帳の `森の洞口`／`夜` のままである。**",
   "motion": "Full animation, not limited. **光が動き、空気が動き、視点が少しだけ上がる。** ⚠️ **彼は動かない。**"
             "⚠️ **カメラは1回だけ動き、そして止まる。**",
   "sound": "**空気、乾いた葉、遠くの海。****音楽なし。言葉なし。** ⚠️ **洞からは何も喋らない。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "⛔ **この1本の視点は彼女の位置である**——**ゆえに女神の禁制は、ここでいちばん強く掛かる。** "
     "**彼女の姿を、この枠に一切入れない。****顔も、体も、手も、輪郭も無い**"
     "（台帳 `女神.negatives` の逐語:「no visible body, no hands, no feet, no arms, no silhouette with a "
     "readable outline」）。**開口部に人の形を置かない**——**この1本は、それを必要としない。**")) + [
   "**No turn toward the lens, no answer, no open mouth.** ⚠️ **見返すことは、この作品では返事である。** "
   "**この1本は、返事をしないことで立っている。**",
   "**No light source inside the frame at any moment** — no lamp, no torch, no candle, **no moonbeam "
   "standing in for the glow on his cheek.** ⚠️ **光源は枠の外にある。**",
   "**No second person in frame at all** — no companion, no crowd, no figure at any distance, "
   "**no one on the slope behind him and no one at the opening.**",
   "**No cut, and no second setup.** ⚠️ **この1本は1つの視点である**——**視点を変えれば、この1本は"
   "別の1本になる。**",
   "**No conventional camera position, no unstated entry, no fisheye distortion standing in for an "
   "impossible viewpoint, no path that changes its own physics, no shot without an arrival.** "
   "⚠️ **この5つは形式カード `impossible-camera` の `Negative` の逐語であり、§16 の床の側に在る。**",
   "**No close-up that fills the frame with the face.** ⚠️ **寄れば、視点であることが消える**"
   "——**この1本は彼の顔を、暗さの中の一つの面として持つ。**",
 ],

 "must": [
   "**光が彼の頬に着き、そして留まる** — そして**彼が一度も視線を動かさないことが、切れ目のコマである。**",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.**",
   "⛔ **女神の姿を、この枠に一切入れない** — **顔も、体も、輪郭も無い。****この1本の彼女は、"
   "面の上の温かさと、洞から出てくる空気だけである。**",
   "⚠️ **入口（`ENTRY`）を言う** — **光とともに入る**。**言わなければ、この1本は前のショットの"
   "継続エラーとして読まれる。**",
   "⚠️ **この視点は、この作品でカメラが立てる唯一の場所である** — **彼女の位置であり、"
   "彼女は写らない。**",
   "⚠️ **彼は見返さず、口を開かない** — **見ることは、この1本の彼女の側にある。**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **光を強くしない** — **強くなれば、この1本は照らされている画になる。**",
   "⚠️ **変化は最後のコマで終わる** — **彼が動かないまま、この1本は終わる。**",
   "⚠️ **この1本は `mode: still` である** — **止まるのは主題であり、画面ではない。**"
   "**光と空気と視点は動いている。**",
 ],

 "prefer": "The profile held against the opening's black with no ground beneath it; the glow arriving on "
           "the cheek and spreading no further than the jaw; the beard's individual hairs catching first; "
           "**the frame's one warm value given to the skin and to nothing else.**",
 "allow": "A rise of less than a hand's width that stops when it arrives; the air moving the scrub's "
          "leaves at the frame's edge; a moderate depth of field that lets the far edge of the scrub go "
          "soft; **a black that stays opaque for the whole take.**",

 "priorities": [
   "⛔ **見返さないこと。** **返事をすれば、この作品の規則が破れる**——**この1本は、その規則がいちばん"
   "近いところにある。**",
   "⛔ **女神の姿を一度も出さないこと。** **この1本の視点は彼女の位置であり、そこに彼女を置けば、"
   "この1本は別の1本になる。**",
   "**光が頬に着いて留まること** — そして**彼が動かないことが切れ目のコマであること。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "⚠️ **`impossible-camera` の5つを満たすこと** — `EYE` は彼女の位置、`ENTRY` は光、`PATH` は暗さ、"
   "`ARRIVAL` は彼の顔、`DURATION` は 6.782秒。",
   "**光源を枠の中に置かないこと** — 灯火も、月の光条も、内側からの光も無い。",
   "**No second person, at any distance, in any focus.**",
   "⚠️ **`mode: still` のまま、画面が止まらないこと** — 光と空気は動いている。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `impossible-camera` を名乗るが、その禁制（`no conventional camera position`・"
   "`no unstated entry`・`no cut`・`no fisheye distortion standing in for an impossible viewpoint`・"
   "`no path that changes its own physics`・`no shot without an arrival`）は §16 に在って、ここには無い。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 6.782-second cinematic take (16:9) at night at the mouth of a cave on a bronze-age island, one clip, "
   "one continuous take, one change: **a very weak light arrives on a man's cheek from outside the frame "
   "and stays there, and he does not move at all.** **The viewpoint of this shot is not a place a camera "
   "can stand — it is where the goddess is, and she is never shown.**\n\n"
   "**{IDENTITY}** He is seen in profile from the frame's left against the black of the opening, at the "
   "height of his eyes. **His mouth is closed, his eyes are fixed on one point outside the frame, and he "
   "never turns toward the lens and never answers.**\n\n"
   "0-2.001s: **almost nothing is lit: the line of a forehead, a cheek and a beard against the opening's "
   "black, and no light falls on him at all.** The frame is the dark.\n"
   "2.001-4.503s: **a very weak light arrives on his cheek from outside the frame** — it is not a lamp, "
   "not a fire and not the moon, its source never enters the frame, and it does not move; **and he does "
   "not move either.**\n"
   "4.503-6.782s: **the light stays on his cheek and he never moves his gaze once — and the take ends on "
   "that frame, with the light still on him.**\n\n"
   "**The viewpoint is entered through that light: the shot opens in the dark, there is no approach and "
   "no cut, and the light that finds his cheek is where the viewpoint stands — it rises only as far as the "
   "height of his eyes and stops there.** **No source of light is inside this frame at any moment.** "
   "**No woman is in this frame at any distance and in any focus: she is not shown as a person at any "
   "moment, not as a face, not as a body, not as a silhouette at the opening — her presence is the warmth "
   "on his cheek and the air coming out of the cave, and nothing else.** **No second person is in this "
   "frame at any distance or in any focus.** **This is a bronze-age island before classical Greece: rough "
   "grey rock, dry scrub, no made thing at the opening, no fire and no torch anywhere.** **This is a "
   "Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the light arrives on his cheek and he does not move.)"),

 "visual_scene": (
   "The mouth of a cave in a wooded slope at night, photographed as a film frame: rough grey rock split "
   "into a wide low opening whose interior is wholly unlit — a black shape and not a room, with no inside "
   "visible in it at any moment; dense low scrub and thin trees crowding the entrance and growing right up "
   "to the stone. **In the left part of the frame, a man's head and shoulder in profile against that "
   "black: the line of a heavy brow, the cheek and the jaw, the beard, and the hair falling past the ear. "
   "His eyes are fixed on one point outside the frame and he does not move.** There is no ground in the "
   "frame beneath him and no horizon behind him; above the opening there is the night sky, and nothing "
   "else is in the frame."),

 "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones",
   "rough grey rock with cracks and old water-marks").replace(
   "warm ochre where the low sun falls",
   "no warm light anywhere except the skin the glow reaches") + (
   " ⚠️ **There is no sun in this frame and no fire in it: the only light on him is a very weak glow that "
   "comes from behind the camera and never enters the frame.** ⚠️ **The black of the opening is absolute "
   "and carries no detail** — it is the one value in the frame the grade does not touch, and nothing in it "
   "is ever legible."),

 "motion_prompt": (
   "Full animation, not limited. **The man does not move at all — not his gaze, not his head, not his "
   "shoulder.** **What moves is the light: a very weak glow arrives on his cheek from outside the frame "
   "at 2.001 seconds, spreads across the skin as far as the jaw, and stays there unmoving for the rest of "
   "the take.** **The viewpoint rises slowly from the height of his cheek to the height of his eyes at the "
   "light's own pace, and stops and does not move again.** The air coming out of the cave moves the dry "
   "scrub leaves at the edge of the frame and nothing else; the black of the opening does not move at all. "
   "No motion blur smears, no stutter, no floaty weightless motion, no static frames — **the light and the "
   "air move in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **standing inside the darkness at the mouth of the cave at the height of his face** — a "
   "position no camera can occupy: **she is never a body in this work, and this is the one place the "
   "frame is allowed to stand.** One event only: **a rise of less than a hand's width, from the height of "
   "his cheek to the height of his eyes, at the light's own pace, which stops when it arrives and does not "
   "move again.** ⚠️ **The move is motivated by the light, and the stop is the arrival.** ⚠️ **The style "
   "permits a dolly, a crane and a Steadicam, and this shot spends the crane** — a rise with the low "
   "frequency of a rig that has mass, and it does not wobble. No dolly is used and no Steadicam: the "
   "viewpoint does not travel sideways and it does not follow anything. ⚠️ **Do not approach him and do "
   "not let the frame find a light source inside it.** No handheld, no whip, no shake, no snap zoom, no "
   "rack focus, no unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **the air coming out of the cave moving dry scrub leaves at the "
   "edge of the frame, and the sea far below the slope.** ⚠️ **He says nothing, and nothing speaks from "
   "inside the cave** — **she is looking, and looking is not an answer; this shot is not silent, and it "
   "carries no voice at all.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (impossible-camera) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ。**"
                        "⚠️ **参照集合の6鍵のうち、`女神` から引いているのは `女神.negatives` である**"
                        "（`女神.identity` は引かない——台帳の註:「§6 に貼るのは negatives の側である」）。",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ air from the cave ＋ dry scrub ＋ the sea far below ／ no music",
 "unresolved": [
   "⚠️ **この1本に女神の声を置くかどうかを、記録は何も言わない。****この仕様は置いていない**"
   "——**この1本は見られている側であり、返事が無いことが内容である。**"
   "⚠️ **彼女の第一の姿（枠の外の低い女声）をこの1本に置くかどうかは、著者が決める。**",
   "⚠️ **頬の光を「光」と呼ぶか「気配」と呼ぶかが、`s02` とこの1本で違う。****`s02` は「内側の温かさは、"
   "光ではなく気配である」と書き、この1本の記録は「ごく弱い光が当たりはじめる」と書く**"
   "（`森の洞口.states.夜` は「光源は月と星だけである」と言う）。⚠️ **どちらに揃えるかは著者が決める**"
   "——**この仕様は、記録の語（光）を採った。**",
   "⚠️ **`s06` の註は `still` を5本と言い、`s06`・`s08`・`s11`・`s31`・`s32` を名指す。**"
   "**記録の `mode:` を全部数えると6本である**（`s24` が `still` である）——"
   "**この2つは食い違っている。****どちらが正かは著者が決める。**",
   "⚠️ **`ENTRY`（入口）の読みが著者に委ねられている。****この仕様は「光とともに入る」を採った**"
   "——**「ショットは最初から彼女の位置に在る」という読みもできる。**"
   "⚠️ **カードは入口を言えと要求するので、この仕様は言う側を採った。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **彼がレンズを見る。** この1本のいちばん高い危険である——**見返せば、この1本は「見られている」"
   "ではなく「見ている」になり、`s12` と対でなくなる。** 禁制は §16 と `Master Prompt` の散文の両方に在る。",
   "⛔ **女神の姿が現れる。** ⚠️ **「彼女の位置」という指定は、生成器には「彼女を出せ」と読まれうる**"
   "——**開口部のシルエット一つで、この1本は別の1本になる。**",
   "**光が灯火になる。** ⚠️ **頬を明るくしようとすると、生成器は枠の中に光源を置く**"
   "——**この作品は全ショットで火を禁じている。**",
   "**顔が動く（drift）。** ⚠️ **参照画像が1枚も無いので、守る道具は英文の塊だけである**"
   "——**この1本は横顔であり、横顔はいちばん形が読まれる。**",
   "**寄りすぎる。** ⚠️ **顔の大写しになれば、視点の存在は画面から消える**"
   "——**この1本は視点の1本である。**",
   "**光が強くなりすぎる。** 弱いことが内容であり、**強ければ、この1本は照らされている画になる。**",
   "**空気が止まり、潅木が動かない。** ⚠️ **`mode: still` でも画面は止まらない**"
   "——**止まれば、この1本は静止画の並びになる。**",
 ],
}

if __name__ == "__main__":
    print("s11 content OK — keys:", len(C))
