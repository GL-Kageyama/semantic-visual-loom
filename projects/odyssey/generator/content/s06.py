# -*- coding: utf-8 -*-
"""odyssey-s06 — meaning-responsive — 岸 / 日没 / 6.143s. has_man."""
import common as K


C = {
 "n": "s06",
 "title": "見る——この作品で最初の行為",
 "duration": "6.143",
 "format": "meaning-responsive",
 "has_man": True,
 "segment": "verse-1-2",

 "band": [
   "『永遠より遠い』 verse-1「岸」 / 反応 / still —— 見る——この作品で最初の行為",
   "水際に立った男が海を見て、一歩も動かない——海が、彼の視線の先でだけ広がる。",
   "6.143秒、カメラは彼の背中から海へ寄っていく——彼の髪が一度強く押されるのが、切れ目である。",
   "止まるのは主題であって画面ではない——彼は歩かず、振り向かず、一言も言わない。",
 ],
 "header": """⚠️ **行: `l02`「海の方を見ていた」。** 場所は `岸`、時刻は `日没`、尺は 6.143秒——
**`l02` の実測の長さそのものである**（60.479→66.622）。
⚠️ **`mode: still` である。** この作品で `still` を使うのは5本だけである
（`s06`・`s08`・`s11`・`s31`・`s32`）。⛔ **5本に共通する性質がある——ここは、この作品が何かを言わない場所である。**
**見る（`s06`）・言わない（`s08`）・見られる（`s11`）・着かない（`s31`・`s32`）。****沈黙が、静止として現れる。**
⚠️ **役は `反応` である。** 固有基準は「抑制・微細な身体・表情の段階」——
**この1本では、その3つが全部「動かないこと」の中にある。**
⚠️ **形式は `meaning-responsive`**（起きたことではなく意味に反応して画面が変わる）。
⛔ **この1本では、彼が海を見るという「意味」に、海の側が反応する。**
**何も起きていないのに、画面が彼の行為を知っている。**
⚠️ **この仕様のショット記録は `shots/odyssey-s06.yaml` である。**""",

 "intent": "One continuous take of one change — **the sea opens at the line his gaze falls on.** At the first frame he is a back at the waterline with the sea still far and flat; by the last frame the water at that one line has widened and gone on widening while the water on either side of it has not, **and the wind pushes his hair hard once** — and the take ends on that frame. ⚠️ **He does not move at all.** **He does not speak, does not lift a hand, and does not look at the lens.** ⚠️ **The change completes on the last frame of the take** — his hair is still being pushed when the cut arrives — **and the frame is never still in the meantime**: the swell keeps arriving, his hair and the hem of his tunic keep moving, and the camera keeps travelling.",

 "world_concept": K.world_concept(
   "⚠️ **この1本で、この作品に人間の行為が初めて入る。** 曲の2行目が「海の方を見ていた」と言っており、"
   "**この1本の実体がそれである。** ⚠️ **そして `s05` が彼を岸に立たせ、この1本が彼に何かをさせる**"
   "——**それが「見る」である。** **この作品の最初の行為は、何もしないことにいちばん近い行為である。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **彼はこの1本で、この作品で最初の行為をする**——**見る。** "
               "⚠️ **そして彼は口を開かない。****彼がするのは見ることだけであり、それは返事ではない。** "
               "**見ることと、答えることは、この作品では別である。**",
     "goddess": "⚠️ **彼女はこの1本に、四つの姿のどれとしても現れない**——**この1本の光は日の光そのものである。** "
                "**この1本の変化は海の側で起きるが、それは彼女の仕業として書かれない。**",
     "name": "⚠️ **曲の2行目は、彼を何とも名指さない**——「海の方を見ていた」は彼がしたことを言い、"
             "**誰であるかを言わない。**",
     "bow": "⚠️ **この1本で彼は何も持たない。****手は空である。**",
     "places": "この1本が置くのは一つ——`岸`、**`s05` が彼を立たせたのと同じ岸である。**",
     "japanese": "⚠️ **この1本には歌がある**——`l02` がこの6.143秒の上を歌っている。**そして歌は日本語である。**",
   },
   extra=[
     "⛔ **「意味に画面が反応する」は、この作品では `L30` の側の危険である。** "
     "**§18 の `Negative Prompt` はこの経路では床にならない**——ゆえに**形式カード自身の禁制"
     "（`no visible cause`・`no camera move answering the meaning` ほか）は §16 が運び、"
     "`Master Prompt` の散文がそれを実際に負う。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "A bronze-age Mediterranean island shore at the end of the day, photographed as a film. Rough wet "
     "stone, coarse sand, low dense scrub, sea-worn driftwood; undyed wool and stiff salt cloth. "
     "⚠️ **The man is of this place and not above it** — one coarse worn tunic, bare feet. "
     "⚠️ **No marble, no columns, no architecture of any later age.**",
   "Color Language":
     "A narrow, graded palette — cold slate blue in the water and the wet stone, warm ochre where the "
     "low sun falls, and the man carried mostly in the ochre and the mid-tones rather than in the blue. "
     "⚠️ **The answer is not a grade** — **水面の色は、彼の視線の先でも、他のどこでも、同じである。**"
     "⚠️ **He is not lit apart from the shore, and the shot has no second light.**",
   "Texture":
     "Wet shingle with grain and individual stones; coarse wool with visible fibre and a worn shoulder "
     "seam; skin roughened and marked; the water's surface fine-grained and broken, never glassy. "
     "Film grain present and even.",
   "Visual Density":
     "Low to moderate at the first frame and **falling** — he is the near subject at the start, and by "
     "the last frame the water holds most of the picture and he is small in it. **Nothing in the frame "
     "competes with the two of them: the man, and the water he is looking at.**",
   "Atmosphere": "The minute in which a man finds out that the sea will answer a look and not a word.",
   "Time": "`日没` — the last of the day, on the island's shore. **The same evening and the same shore as "
           "`s01`, `s04`, `s05`, `s08`; the work does not fix a date.**",
 }),

 "subjects": [
   K.man_subject(
     behavior="**彼は水際に立って、海を見ている。****この作品で最初の行為がこれである。** "
              "**彼は一歩も動かず、手を上げず、口を開かない。** 髪と裾だけが風に押される。"
              "⚠️ **彼が見るということが、この1本の「意味」であり、そしてこの1本の唯一の事件である。**",
     may="髪の押され方、裾の鳴り方、風の当たる面、そして彼が画の中で占める大きさ。",
     extra_notes=[
       "⚠️ **彼はこの1本で何も持たない。****手は空である。**",
       "⚠️ **彼は水面の、自分の視線が落ちた一本の線から目を離さない**——**彼が見ているのは海全体ではない。**"
       "**ゆえに答えも、その一本の線にだけ来る。**",
     ]),
   {"name": "nobody",
    "ref": "**この1本に、二番目の人物は居ない。** 顔も、立ち姿も、肩も、遠景の点も、写らない。",
    "appearance": "**無い。** ⚠️ **この1本の主題は、彼と、彼の前の海である。**",
    "behavior": "**無い。** ⚠️ **動くのは彼と波と風だけである。**",
    "continuity": "⚠️ **二番目を入れないこと。** **この作品は「一人」の作品である。**",
    "notes": ["⚠️ **`Negative Prompt` はこの経路では床にならない**（§18 の前書き）。**ゆえにこれは肯定形で負う** "
              "— §16 `MUST NOT` と、`Master Prompt` 自身の一文が負う。",
              "⚠️ **弱い守りである。記録として書く。** ⚠️ **岸に人を置くのは生成器にとって自然である。**"]},
 ],

 "environment": {
   "location": "`岸` — **`s05` が彼を立たせた岸である。** ⚠️ **この1本は場所を作り直さない**"
               "——**立っている場所も、水際の線も、`s05` のままである。**",
   "elements": "水際の線、粗い暗い砂、濡れた小石、流木の一本、乾いた海藻、背後へ上がる低く密な潅木のbank、"
               "そして彼の前の海と、水平線。⚠️ **範囲を広げない** — **歌の2行目が「海の方を見ていた」と"
               "言っている以上、この1本は岸と海で閉じる。**",
   "behavior": "**波は `s05` と同じ間隔で寄せて返す**——**彼が動かなくても、速さを変えない。** "
               "**潅木は風で動き、彼の髪と裾を押す。** ⚠️ **環境は彼に反応しない**"
               "——**海の側が応えるのは、彼の視線の先の一本の線だけである。**",
 },

 "objects": [
   "**彼が持つもの: 無し。** ⚠️ **手は空である。**",
   "**水際の線**, the line where the water meets the shingle — **`s05` と同じ位置にある。**",
   "**乾いた海藻**, lying on the shingle above the waterline — ⚠️ **この1本では動かない。**",
   "**流木**, one bare limb, sea-worn, at the edge of the frame.",
   "⚠️ **この作品の小道具は4つだけであり**（`ledger.props`）、**そのどれもこの1本には来ない** "
   "— 舟・帆・斧・太陽の牛は、まだ作られていないか、まだ記憶にすら無い。",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — **この1本には添付しない。彼女はこの1本に、四つの姿のどれとしても現れない。** "
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`岸` の5鍵である。",

 "narrative": {
   "core": "**海が、彼の視線の先でだけ広がる** — 見るという行為に、海の側が応える。",
   "beginning": "**彼の背中。****海はまだ遠い。**",
   "turn": "**カメラが海へ寄る。****彼が小さくなり、波が大きくなる。**",
   "peak": "**海が画面の大半を占める。****波が返る。**",
   "pull": "⚠️ **彼の髪が一度だけ強く押されるのが、切れ目のコマである。****彼はその瞬間も、"
           "一歩も動いていない。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 1.6 seconds.** 最初の2秒は**彼の背中**のために払われ、"
            "次の2.5秒は**カメラが海へ寄る**ことに払われ、**最後の1.64秒がこの1本の出来事である**"
            "——**海が画面の大半を占め、彼の髪が押される。** "
            "⚠️ **`held` を1つも使わない。****`mode: still` であって、止まるのは主題であり、画面ではない**"
            "——**光と埃とカメラは動く**（`shot-record.schema.json` の `motion`）。**ゆえに末尾のビートは `dense` である。** "
            "⚠️ **`meaning-responsive` の5つの変数（形式カードの逐語）**: "
            "`BEARER`＝**彼の「見る」という行為である**（彼は画面の中で意味を運び、そして彼は動かない）／ "
            "`ANSWER`＝**海が、彼の視線の落ちた一本の線でだけ広がる**——**他のどこでも広がらない**／ "
            "`DELAY`＝**答えは後半に来る**（4.503秒から。**即答すればカットに見え、末尾で答えれば露見になる**）／ "
            "`LIMIT`＝**答えは彼にも岸にも光にも届かない**——**彼の体は変わらず、水面の色はどこでも同じである。**"
            "**届けば blanket colour grade として読まれる**／ `DURATION`＝`6.143s`。",

 "actions": [
   ("ACT_STAND", "彼は水際に立っている。海は彼の前にある。",
    "**彼は一歩も動かない。****海はまだ遠く、平らである。**"),
   ("ACT_LOOK", "彼の視線はまだ定まっていない。",
    "**彼の視線が、水面の一本の線に落ちる**——**この作品で最初の行為である。**"),
   ("ACT_OPEN", "水面はどこも同じ高さである。",
    "**その一本の線のところだけ、海が広がる**——**他のどこも広がらない。**"),
   ("ACT_PUSH", "彼の髪は静かである。",
    "**風が彼の髪を一度だけ強く押す****——そしてそれが、この1本の切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **behind him and at the shore's own height** — the lens at a standing "
               "person's chest, so that he is a back in the near frame and the sea is beyond him. "
               "⚠️ **`s01` が立てた岸の高さである。**",
   "events": "One event only. `0-6.143s` — **a slow continuous push from behind him out toward the "
             "sea, at a rate that does not change, still travelling on the last frame of the take.** "
             "⚠️ **動機は彼の視線である**——**カメラは彼が見ているものへ寄っていく。** "
             "⚠️ **⛔ そしてこの移動は答えではない。****形式カードの逐語:「The camera may not tilt, push, or "
             "cut to express it — a camera move is a *statement about* the meaning, and this grammar "
             "wants the world to make it.」****カメラが寄るから海が大きく見えるのではない**"
             "——**その手前で、海の側が既に広がっている。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** "
               "— a slow weighted forward travel with the low frequency of a rig that has mass, and it "
               "does not wobble. ⚠️ **彼を追い越さない。****彼はカメラより先に居ない**"
               "——**カメラは彼の背中から離れて、海へ行く。** "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and **no unmotivated move.** ⚠️ **寄るのは彼ではなく海である**——**顔の大写しを作らない。**",
 },

 "motion": {
   "subject": "**男の顔、肩、そして彼の前の海。** ⚠️ **主題は止まる。** "
              "**彼は一歩も動かず、手を上げず、口を開かない。** 動くのは波と、彼の髪と裾と、埃である。"
              "⚠️ **止まっていることが、この1本の意味を運ぶ。**",
   "object": "**波が寄せて返る** — 同じ間隔で、一度も速さを変えずに。**泡の位置が変わる。** "
             "⚠️ **彼は何も持っていないので、動く物は無い**——**動くのは彼の髪と裾だけである。**",
   "environment": "**風が潅木を動かし、彼の髪と裾を押す。** **波は同じ間隔で寄せて返す。** "
                  "⚠️ **環境は彼に反応しない**——**彼が止まっても、波は止まらない。** "
                  "⚠️ **音の側の環境は水と風だけである**（§14）。",
   "weight": "**水は重く、その上の光は重さを持たない。****そして彼の体は重い**"
             "——**彼が動かないので、この1本の重さは水の側にある。**",
   "inertia": "**波は行き過ぎてから戻る。****彼の髪は押されたあと、少しだけ遅れて戻る。** "
              "⚠️ **何も瞬間には戻らない。**",
   "acceleration": "**加速しない。** ⚠️ **カメラの寄りも、波の間隔も、一定である**"
                   "——**この1本に見せ場の加速は一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この6.143秒に、止まったフレームは一つも無い**"
               "——**彼が止まっているあいだも、波と髪とカメラが動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**答えは静かであり、音を立てない。**",
 },

 "emotion": {
   "arc": "**止まっている一人の男が、海を見る。** そして**それが「何かが起きた」に見えること**が、"
          "この1本の感情である。⚠️ **何も起きていないのに、画面が彼の行為を知っている。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしの動きでもない。****海が、彼の視線の先でだけ広がることである。** "
             "**彼はそれを見て、何も言わない**——**この作品は、それに名前を与えない。**",
 },

 "lighting": {
   "base": "The sun's own light, low and raking, falling on him and on the shingle at the same angle; "
           "no fill, no artificial source, and a flare permitted where the light is in frame. "
           "⚠️ **この1本は彼を別に照らさない**——**最初の人間に、専用の光を当てない。**",
   "events": "**One, and it is small.** カメラが水面へ出るにつれて、**日の道が画面の中を横切る位置を変える**"
             "（2.003秒から）。⚠️ **光源は動かない。** ⚠️ **そしてこの1本の答えは、光の側では起きない**"
             "——**様式カードの逐語:「The grade holds for the whole shot — a colour temperature that "
             "swings is a different style.」****色はどこでも同じであり、変わるのは水面の形だけである。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**波が寄せて返る音、そして風が髪と裾を押す音。** ⚠️ **彼は何も言わない**"
          "——**この1本の音の側の主題は、返事が無いことである。** ⚠️ **足音は無い**——**彼は動かない。**",
   "music": K.NO_MUSIC + " ⚠️ **この1本の上では `l02`「海の方を見ていた」が歌われている**"
            "——**ゆえに生成された音床は、同じ6秒に二つの音楽を置くことになる。**",
   "environment": "日没の岸、島の水際。**水、風、そして一人の人間の呼吸。** ⚠️ **呼ぶ声は無い**"
                  "——**彼は呼ばれておらず、呼んでもいない。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="体格・肌・髪・髭・顔・傷・**着ている一枚と、着ていないすべて**。**裸足であること。** "
                "⚠️ **この1本は `s05` の顔から外れてはならない**——**そして `s06` は、"
                "この作品で最初に「動かない顔」を写す1本である。**",
     may="髪の押され方、裾の鳴り方、画の中の大きさ、そして日の道の当たる面。"),
   "spatial": "岸は画面の手前を左から右へ走り、海はその向こうにある。**彼は水際に立ち、カメラは"
              "彼の背中の後ろから海へ出ていく。** ⚠️ **`s05` と同じ配置である**"
              "——**この1本は場所を立て直していない。**",
   "temporal": "一日の終わり、**`s05` のすぐ続きである**——`l02` は `l01` の7.580秒後である。"
               "⚠️ **画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** ⚠️ **光は日の光だけである。**"
             "⚠️ **この1本は `meaning-responsive` を名乗るが、その形式は §15 と衝突しない**"
             "——**`remembered-world` や `coexisting-realities` と違い、この形式が免除を求めるのは"
             "「答えの原因が画面に無いこと」であって、場所でも時刻でも同一性でもない。**"
             "**ゆえに §15 は一句も免除されない。**",
   "motion": "Full animation, not limited. **波と、髪と、裾と、カメラが動く。** "
             "⚠️ **カメラは1回だけ動き、切れ目のコマでもまだ動いている。**",
   "sound": "**水、風。****音楽なし。言葉なし。** ⚠️ **この1本で主題歌が歌っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**この1本は人が居る1本である**——**ゆえに女神の禁制は、他人の形で来る。** "
     "**海の側が応えることを、女の姿で見せない。**")) + [
   "**No visible cause for the answer** — **nothing in the frame makes the sea widen.** He does not "
   "gesture, does not point, does not speak; nothing is thrown and nothing enters the water. "
   "⚠️ **形式カードの逐語:「This is a single point: nothing in the frame causes the answer.」**",
   "**The answer may not reach the man, the shore or the light** — no rim on him, no glow, no second "
   "light, **no blanket colour grade**; the water's colour is the same at the line and away from it.",
   "⚠️ **No camera move standing in for the answer** — **カメラが寄るから大きく見えるのではない。**",
   "**No second person in frame at all** — no companion, no crowd, no figure at any distance, **no one "
   "on the shore behind him and no one in the water.**",
 ],

 "must": [
   "**The sea opens at the line his gaze falls on** — and **does not open anywhere else.**",
   "**He does not move at all** — not a step, not a hand, not his mouth. ⚠️ **この1本の意味は、"
   "動かないことの中にある。**",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.**",
   "⚠️ **He does not look at the lens**, and **he does not open his mouth.**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **The change is still in progress on the last frame** — his hair is still being pushed.",
   "⚠️ **The answer arrives late and is in the world, not in the camera.**",
 ],

 "prefer": "His back and shoulder in the near frame at the start and the sea beyond him; the swell "
           "carried with mass; his hair and the hem of his tunic moving in the wind; the water holding "
           "most of the picture by the end.",

 "allow": "A lens flare where the light is in frame; a moderate depth of field that lets the far water "
          "go soft; the wind arriving as one long push rather than a gust.",

 "priorities": [
   "⚠️ ⛔ **The face.** **This shot shows the first person of the work for the second time, and there "
   "are 28 shots behind it.** ⚠️ **No image is attached and none can be** (裁定②) — **the English block "
   "in §18's `Visual Prompt` is the whole of the lock, and it is not summarized.**",
   "**He does not move.** ⚠️ **動けば、この1本は「見る」の1本ではなくなる。**",
   "**The answer is in the water and not in the camera.** ⚠️ **形式カードの第一の禁制である。**",
   "**The answer does not reach the man, the shore or the light** — **届けば blanket colour grade になる。**",
   "**He does not look at the lens and does not open his mouth.**",
   "**No second person, and no vessel on the water.**",
   "**The shot is `s05`'s shore and `s05`'s man** — this shot does not build a second place.",
   "**Japanese is what this work speaks** — named in §18, and the line sung over this shot is Japanese.",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `meaning-responsive` を名乗るが、その禁制（`no visible cause`・"
   "`no camera move answering the meaning` ほか）は §16 に在って、ここには無い。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 6.143-second cinematic take (16:9) of a bronze-age island shore at the end of the day, one clip, "
   "one continuous take, one change: **the sea opens at the line his gaze falls on.** "
   "**This is the second shot of the work and the first act in it: a man stands still at the waterline "
   "and looks — he does not move, does not lift a hand and does not speak.**\n\n"
   "{IDENTITY}\n\n"
   "0-2.003s: **his back at the waterline, and the sea still far and flat.** The swell is already "
   "arriving at the rate it will keep.\n"
   "2.003-4.503s: **the camera travels out past him and the water grows in the frame.** He gets "
   "smaller; the swell gets larger; **he has still not moved.**\n"
   "4.503-6.143s: **the water holds most of the picture and the sea opens at one line — the line his "
   "gaze is on — and it does not open anywhere else on the surface.** The wind pushes his hair hard "
   "once, **and the take ends on that frame, with his hair still being pushed and his mouth still "
   "closed.**\n\n"
   "**The camera travels slowly out from behind him toward the water and is still travelling on the "
   "last frame; it does not pass him and it does not go close on his face.** "
   "**Nothing in this frame causes the water to open: he does not move, nothing is thrown, no light "
   "source changes, and the camera's travel is not the answer.** "
   "**The light is the sun's own, falling on him and on the shingle at the same angle — he is not lit "
   "apart from the shore, and the water's colour is the same at that line and away from it.** "
   "**No second person is in this frame at any distance or in any focus — no one on the shore behind "
   "him and no one in the water, and no boat, no ship, no sail, no other vessel anywhere.** "
   "**This is a bronze-age shore before classical Greece: one coarse wool tunic, bare feet, no armour, "
   "no helmet, no weapon, no ornament, and no heroic pose and no heroic lighting.** "
   "**This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the sea opens at the line he is looking at.)"),

 "visual_scene": (
   "A bronze-age Mediterranean island shore at the end of the day, photographed as a film frame: coarse "
   "dark sand and wet shingle with sea-worn driftwood, dry weed and small flat stones; low wet rocks at "
   "the waterline; a rising bank of dense low scrub behind, with no trees and no path; the sea filling "
   "the upper part of the frame beyond him, the horizon level and unbroken. **A man stands at the "
   "waterline with his back to the lens, facing the water, one arm's width from the near edge of the "
   "frame, still.** The water's surface is fine-grained and broken, and **at one line across it the "
   "swell is wider and further out than anywhere else on the surface.**"),

 "visual_meta": K.VISUAL_META + (
   " ⚠️ **He is carried in the ochre and the mid-tones, not in the blue** — the same raking light falls "
   "on him as on the shingle."),

 "motion_prompt": (
   "Full animation, not limited. **The man does not move at all** — he is standing at the waterline with "
   "his back to the lens and he holds that; **there is no step, no gesture and no turn in the whole "
   "take.** What moves is the water, the wind and the camera. **The sea arrives and goes back on an "
   "interval that does not change, and at the line his gaze is on the swell is wider and reaches "
   "further out than anywhere else on the surface — and that is the only thing in the frame that is "
   "not the same as it was.** **The wind pushes his hair hard once, late, and the hem of his tunic with "
   "it, and his hair is still moving when the take ends.** **The camera travels slowly out from behind "
   "him toward the water and does not stop.** No motion blur smears, no stutter, no floaty weightless "
   "motion, no static frames — **the water, his hair and the camera move in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **behind him and at the shore's own height** — the lens at a standing person's chest, "
   "so that he is a back in the near frame and the sea is beyond him. One event only: **a slow "
   "continuous push out from behind him toward the sea, at a rate that does not change, still running "
   "on the last frame of the take.** ⚠️ **The move is motivated by his gaze — the camera goes toward "
   "what he is looking at.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot "
   "spends the dolly** — a slow weighted forward travel with the low frequency of a rig that has mass. "
   "⚠️ **This travel is not the answer** — the sea is already wider at that line before the camera "
   "reaches it, and a camera move standing in for the meaning is what this shot must not do. "
   "⚠️ **Do not pass him and do not go close on his face.** No handheld, no whip, no shake, no snap "
   "zoom, no rack focus, no unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **the swell arriving and going back, and wind pushing through "
   "his hair and the hem of his tunic.** ⚠️ **He says nothing and he does not move, so there is no "
   "footfall in this shot** — **the absence of an answer is the subject of this shot's sound.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (meaning-responsive) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⚠️ **同一性は `Visual Prompt` の英文が運ぶ**——"
                        "**`s05` が立てた基準を、この1本は繰り返す。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water ＋ wind through hair ／ no music",
 "unresolved": [
   "⚠️ **「海が、彼の視線の先でだけ広がる」を、機械は測れない。** **測れるのは、§16 が"
   "「他では広がらない」と書いていることと、`Master Prompt` が同じことを散文で負っていることまでである。** "
   "⚠️ **そこから先は、見た者が言う。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
   "⚠️ **この1本は彼の背中を写す。** **同一性の塊は §18 に在るが、この1本の画が顔を近くで写さない**"
   "——**ゆえにこの1本が良くても、顔が保たれたことの測定にはならない。**"
   "（`s08` が顔を初めて近くに出す。**その1本のほうが測定として重い。**）",
 ],
 "risks": [
   "⛔ **彼が動く。** ⚠️ **この1本の意味は「見る」ことであり、動けば別の1本になる。**"
   "禁制は §16 と `Master Prompt` の散文の両方に在る。",
   "⛔ **答えがカメラの側で起きる。** ⚠️ **形式カード自身の第一の禁制である**——"
   "**寄りの画は、それ自体が答えに見える。**",
   "**答えが画面全体に届く。** ⚠️ **水面全体が持ち上がれば、それは答えではなく blanket colour grade である。**",
   "**二人目が入る。** ⚠️ **岸に人を置くのは生成器にとって自然であり、この作品では「一人」が主題である。**",
   "**彼がレンズを見る。** ⚠️ **立ち止まっている人物の画で、生成器が最も自然にやることである。**",
   "**背後の海に舟が浮かぶ。** この作品は全ショットで禁じている。",
   "**顔が動く（drift）。** ⚠️ **参照画像が1枚も無いので、守る道具は英文だけである**（裁定②）。",
 ],
}

if __name__ == "__main__":
    print("s06 content OK — keys:", len(C))
