# -*- coding: utf-8 -*-
"""odyssey-s02 — remembered-world — 森の洞口 / 日没 / 13.000s. No person."""
import common as K


C = {
 "n": "s02",
 "title": "女神が居る場所を、彼女を写さずに立てる",
 "duration": "13.000",
 "format": "remembered-world",
 "has_man": False,
 "segment": "intro-2",

 "header": """⛔ **この作品で最初の内陸である。** 出所は `intro`——**歌がまだ1行も無い区間の2本目である。**
⚠️ **10.500–23.500。曲が置いた境界が無い区間である。** 切れ目は実測の山（10.500秒の +14.6 dB）の直後に在る。
⛔ **この1本で島の内陸を見せる。男はまだ入らない。**
**入らないことが、`world.rules` の一番である**——「**返事は、この作品の中で一度も返されない。**」**彼女の場所へ入れば、返事をすることになる。**
⚠️ **形式は `remembered-world`**（記録でなく記憶。保たれた瞬間の中で中身が滑る）。
⚠️ **この作品で洞窟を使うのは3本だけである**（`s02`・`s09`・`s10`）。**この1本が最初であり、そして最も外側である。**
⛔ **洞の内側は、この1本では一度も見えない。****見えないことが、この1本の内容である。**
⚠️ **この仕様のショット記録は `shots/odyssey-s02.yaml` である。**""",

 "intent": "One continuous take of one change — **洞口が黒くなる。** 最初のコマでは洞口はまだ灰色の岩であり、日没の光がその面を斜めに滑っている。最後のコマでは**洞口は完全な黒であり、何も見せない**——岩の割れ目に残った細い光の線が消えるのが、切れ目のコマである。⚠️ **内側は一度も見えない。****この1本が渡すのは「内側がある」という確信だけであって、内側そのものではない。** ⚠️ **変化は切れ目のコマで終わる**——線が消える瞬間に、この1本は終わる。",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、この作品で最初の内陸である。**——`s01` と `s03` と `s04` は海と岸だけであり、"
   "**島の中へ入るのはここが最初である。** ⚠️ **そしてここは、女神の場所である。** "
   "**彼女はこの1本に現れないが、この1本は彼女の場所を写している**——"
   "**この作品が彼女に与える唯一の実在は、場所である。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本に人は一人も居ない。****ゆえに返事は、ここでも返されない**——"
               "**彼女の場所を写すことと、彼女に会うことは、この作品では別である。**",
     "goddess": "⚠️ **この1本は彼女の場所である。** それでも**彼女は四つの姿のどれとしても現れない**——"
                "**内側が見えないのだから、声も、温かさも、動く空気も、水面の光も、ここには無い。**"
                "**この作品は、彼女を「場所そのもの」として置く。**",
     "name": "⚠️ **この1本は、歌のまだ始まらない区間である**（`intro`）。**名はどこにも無い。**",
     "bow": "⚠️ **この1本に持ち手が居ない。** **弓は無論のこと、斧すら無い。**",
     "places": "この1本が置くのは一つ——`森の洞口`、**この作品で最初の内陸である。**",
     "japanese": "⚠️ **この1本には歌が無い**——`intro` であり、**声は 52.899秒からである。**",
   },
   extra=[
     "⛔ **返事は、この作品の中で一度も返されない。** ⚠️ **この1本は、その規則がいちばん危うい1本である**"
     "——**彼女の場所を写しながら、彼女に会わない。** ゆえに**洞の内側を一度も見せない。**",
     "⚠️ **この作品は光を一つしか持たない。****洞の内側が温かく見えても、それは火ではない**"
     "（`bible.negative_base` が全ショットで火を禁じている）。**内側の温かさは、光ではなく気配である。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "A bronze-age Mediterranean island, inland: a scrub-covered slope of rough grey stone rising to a "
     "cave mouth, photographed as a film. Dry leaves, coarse rock with cracks and old water-marks, "
     "sea-worn stone underfoot. ⚠️ **The mouth is a hole in the rock and nothing more is shown of it** "
     "— no structure, no threshold, no carving, no made thing. **No marble, no columns, no architecture "
     "of any later age.**",
   "Color Language":
     "A narrow, graded palette — warm orange where the low sun still reaches the slope, cold grey in "
     "the rock's shaded faces, and **the mouth carried as an absolute black that takes no colour at "
     "all.** ⚠️ **The black is where the palette stops** — it is the one value in this work that the "
     "grade does not touch.",
   "Texture":
     "Rough grey rock with cracks, old water-marks and a granular weathered surface; dry leaves with "
     "visible veins turning edge-on in the wind; sea-worn stone underfoot. ⚠️ **No water is in this "
     "frame and nothing on it is wet.** ⚠️ **No skin and no cloth are in this frame.** Film grain "
     "present and even.",
   "Visual Density": "Low. **The frame holds one thing — the mouth — and the slope is what leads to it.**",
   "Atmosphere": "The hour when a place stops being a place and becomes somewhere **inside**.",
   "Time": "`日没` — the last of the day, on the island's inland slope. **The same evening as `s01` and "
           "`s03`; the work does not fix a date.** ⚠️ **This shot runs from the light to the black** — "
           "by its last frame the sun is no longer in the frame at all.",
 }),

 "subjects": [
   {"name": "nobody",
    "ref": "**この1本に、人物は一人も居ない。** 顔も、立ち姿も、肩も、遠景の点も、写らない。"
           "⚠️ **島の内陸に入るのがこの1本であるのに、そこに住む者を写さない**——**それが `remembered-world` の形式を選んだ理由である。**",
    "appearance": "**無い。** ⚠️ **この1本の「主題」は場所であって、人物ではない。**",
    "behavior": "**無い。** ⚠️ **動くのは岩と葉と光であり、誰かではない。**",
    "continuity": "⚠️ **人を一人も入れないこと。** **二人目が入れば、この作品の「一人」が壊れるのではなく、"
                  "この1本が女神の場所でなくなる**——**彼女の場所は、人の居ない場所である。**",
    "notes": ["⚠️ **`Negative Prompt` はこの経路では床にならない**（§18 の前書き）。**ゆえにこれは肯定形で負う** "
              "— §16 `MUST NOT` と、`Master Prompt` 自身の散文が負う。",
              "⚠️ **弱い守りである。記録として書く。** ⚠️ **そしてこの1本では、弱さが最も高くつく**"
              "——**人が一人入れば、女神の場所は人の場所になる。**"]},
   {"name": "森の洞口",
    "ref": "**この1本の主題である。** ⚠️ **参照は `ledger.locations.森の洞口` の `geography` と `states.夜` である**"
           "——**この1本は、その場所を立てる。**",
    "appearance": "**岩の面、割れ目、潅木、そして黒。** ⚠️ **黒は形を持たない**——"
                  "**この1本に与えられる黒は「何も見えないこと」であって、暗い内側の描写ではない。**"
                  "**亀裂が一本、岩の面を斜めに走り、日の最後の光を受けて細い線になる。**",
    "behavior": "**光が岩の面をゆっくり斜めへ滑る。****葉が風で裏返る。****そして洞口が黒くなる。** "
                "⚠️ **黒は動かない**——**動くのは黒の縁である。** **縁が内側へ寄り、黒が広がり、最後に線が消える。**",
    "continuity": "**Must preserve** — **洞口の位置と形、岩の割れ目の走り、潅木のbank、そして"
                  "「内側が見えない」こと。** **May change** — 黒の縁の位置、光の当たる面、葉の向き、"
                  "そして最後の線の細さ。",
    "notes": ["⚠️ **`remembered-world` の5つは、この場所に当てはめられる**（§8 の `Temporal Density` を見る）"
              "——**証人は `男` である**（この場所を何年も見てきた男。**この1本には居ないが、この1本は彼の記憶である**）。",
              "⛔ **内側は、この1本では一度も見えない。** **この1本が見せるのは、黒のふちまでである。**"]},
 ],

 "environment": {
   "location": "`森の洞口` — **この作品で最初の内陸であり、女神の場所である。** ⚠️ **`s01` の岸から内陸へ上がった場所**"
               "——**この作品は、岸を先に立ててから島へ入る。** **この1本はその最初の一歩であり、そして最も外側である。**",
   "elements": "斜面の粗い灰色の岩、岩の面を走る亀裂、乾いた潅木の葉、足もとの海蝕の石、"
               "そして**洞口そのもの**——**黒い穴であり、内側は見えない。** ⚠️ **人工物を一つも置かない**"
               "——**敷居も、段も、刻みも、灯火も無い。**",
   "behavior": "光は岩の面をゆっくり斜めへ滑り、**日の高さが下がるにつれて届く面が減っていく。** "
               "潅木は風で裏返る。⚠️ **洞口は動かない**——**動くのは縁である。** "
               "⚠️ **場所は人に反応しない**——**この1本に人は居ない。**",
 },

 "objects": [
   "**無し。** ⚠️ **この1本に小道具は来ない。** **この作品の小道具は4つだけであり**（`ledger.props`）、"
   "**そのどれもまだ作られていないか、まだ記憶にすら無い。**",
   "**岩の割れ目**, one crack running diagonally across the rock face — **この1本の最後の光を受ける。**",
   "**乾いた潅木の葉**, turning over in the wind — **この1本では動き、そして戻る**（`remembered-world` の `DRIFT`）。",
 ],

 "ref_character": "**この1本に人物は一人も居ない**——**ゆえに添付しない。** `男` も `女神` も、"
                  "**この1本には四つの姿のどれとしても現れない。** 参照集合が挙げているのは "
                  "`森の洞口`・`森の洞口.geography`・`森の洞口.states.夜` の3鍵である。",

 "narrative": {
   "core": "**洞口が黒くなる** — 女神の場所が、彼女を写さずに立つ。",
   "beginning": "**潅木の間から、洞の入り口が現れる。****まだ遠い。** そして**光がまだ岩の面に当たっている。**",
   "turn": "**光が斜めになり、届く面が減る。****洞口が灰から黒へ移りはじめる。**",
   "peak": "**洞口が完全に黒くなる。****内側は何も見せない。**",
   "pull": "⚠️ **岩の割れ目に残った細い光の線が消えるのが、切れ目のコマである。**"
           "**内側が、完全に内側になる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last four seconds.** 最初の3秒は**遠い洞口**のために払われ、"
            "次の6秒は**岩の面と葉**に払われ、**最後の4秒がこの1本の出来事である。** "
            "⚠️ **`held` を1つも使わない。** ⚠️ **`remembered-world` は「時が経たない」形式であるのに、"
            "ビートに長さがあるのは矛盾ではない**——**滑るのは時間ではなく、画面の中身の確かさである。**",

 "actions": [
   ("ACT_EMERGE", "潅木のbankが画面の手前にあり、洞口は見えない。",
    "**潅木の間から洞口が現れる**——**まだ遠く、灰色である。**"),
   ("ACT_SLIDE", "光は岩の面の高いところに当たっている。",
    "**光が斜めへ滑り、届く面が減っている****——葉が裏返る。**"),
   ("ACT_DARKEN", "洞口は灰であり、内側の暗さはまだ薄い。",
    "**洞口が黒くなる**——**縁が内側へ寄り、黒が広がる。**"),
   ("ACT_LINE", "岩の割れ目は日を受けている。",
    "**割れ目の光が細い線になる****——そして消える。****その消えるコマが、この1本の切れ目である。**"),
 ],

 "camera": {
   "language": "Third person, **at a walker's height on the slope** — the lens low enough that the "
               "cave mouth sits above the frame's centre and the slope's rise is legible. "
               "⚠️ **この1本のカメラは、この場所を訪ねる者の高さである。**",
   "events": "One event only. `0-8.996s` — **a slow approach through the scrub toward the mouth, "
             "closing the distance without arriving**; then `8.996-13s` — **the camera stops and holds "
             "while the mouth goes black.** ⚠️ **動機は洞口である。** ⚠️ **この1本は一度も内側へ入らない**"
             "——**寄ることは、入ることではない。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** "
               "— a slow forward travel with the low frequency of a rig that has mass, and it does not "
               "wobble. ⚠️ **動機の無い移動をしない。** ⚠️ **止まったあと、カメラは動かない。** "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and **no unmotivated move.** ⚠️ **カメラが内側へ入れば、この1本は別の1本になる**"
               "——**洞口の手前で止まることが、この1本の内容である。**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、黒の縁である。** 潅木の葉が風で裏返り、岩の面の光がゆっくり斜めへ滑り、"
              "**そして洞口の黒が広がる。** ⚠️ **黒そのものは動かない**——**動くのは、黒と光の境である。**",
   "object": "**葉が裏返る** — そして**戻る**（`remembered-world` の `DRIFT`）。"
             "**割れ目の光の線が細くなる** — そして**消える。** ⚠️ **岩は動かない。** "
             "⚠️ **この1本に動く物は無い**——**動くのは光と葉だけである。**",
   "environment": "**日の高さが下がり、届く面が減る。** 潅木は風で動く。"
                  "⚠️ **波はこの1本に無い**——**内陸である。** ⚠️ **音の側の環境は風と葉だけである**（§14）。",
   "weight": "**この1本に重さを持つ物は無い。** ⚠️ **岩は動かず、葉は軽い。** "
             "**重さが現れるのは光の側である**——**光が面を滑る速さは、日の動く速さである。**",
   "inertia": "**葉は裏返ったあと、少しだけ行き過ぎてから戻る。** ⚠️ **黒の縁は慣性を持たない**"
              "——**縁は光に従い、光は止まらない。**",
   "acceleration": "**加速しない。** ⚠️ **この1本の変化は一定の割合で進む**——"
                   "**日の沈みが加速しないのと同じである。** ⚠️ **急に黒くならない。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この13秒に、止まったフレームは一つも無い**"
               "——**光と葉は、最後のコマまで動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**変化は静かであり、音を立てない。**",
 },

 "emotion": {
   "arc": "**人が居ない場所に、気配だけがある。** そして**それが「誰かが居る」に見えること**が、この1本の感情である。"
          "⚠️ **誰も写さないのに、居るように見える**——**それを作るのは、内側を見せないことである。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****洞口が黒くなることである。** "
             "**暗くなることは、何かが中に在ることの証明ではない**——**この作品は、証明しない。**",
 },

 "lighting": {
   "base": "The sun's own light, low and raking, crossing the rock face at a shallow angle; no fill, no "
           "artificial source. ⚠️ **この1本の光源は一つであり、それは日である。** "
           "⚠️ **洞の内側から光を出さない**——**内側が温かく見えるのは、光ではなく気配である。**",
   "events": "**One, and it runs the whole shot.** 光の当たる面が高いところから低いところへ移り、"
             "**届く面が減り、そして割れ目の一本の線だけが残る。** ⚠️ **その線が消えるのが、切れ目のコマである。** "
             "⚠️ **光源は動かない**——**様式カードの逐語:「The grade holds for the whole shot — a colour "
             "temperature that swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**風と、潅木の葉のこすれる音。** ⚠️ **この1本に人の音は一つも無い。** "
          "⚠️ **洞から音を出さない**——**内側から何かが聞こえれば、それは返事である。**",
   "music": K.NO_MUSIC + " ⚠️ **この1本は `intro` の真ん中であり、歌はまだ始まっていない**"
            "——**ゆえにこの1本には、重ねる音床が存在しない。**",
   "environment": "島の内陸の日没。**風、乾いた葉、そして遠くの海があることの気配。** "
                  "⚠️ **呼ぶ声は無い**——**この1本には、呼ぶ者も、呼ばれる者も居ない。**",
 },

 "continuity": {
   "identity": "⚠️ **この1本に人物が居ないので、人物の同一性は掛からない。** "
               "**掛かるのは場所の同一性である**——**洞口の形、割れ目の走り、潅木のbank、"
               "そして「内側が見えない」こと。** ⚠️ **`s09` と `s10` は同じ洞口を写す**"
               "——**この1本が場所の基準を立てる。**",
   "spatial": "斜面は画面の手前から奥へ上がり、**洞口は画面の上部にある。** 潅木のbankは手前側であり、"
              "**カメラはその間を抜ける。** ⚠️ **内陸である**——**海はこの1本の画に入らない**"
              "（**入れば、この1本は岸の1本になる**）。",
   "temporal": "一日の終わり、**`s01`・`s03`・`s04` と同じ夕べである。** ⚠️ **この1本は日の光から黒へ抜ける**"
               "——**画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** ⚠️ **光は日の光だけである。**"
             "⚠️ **この1本は `remembered-world` を名乗るので、§15 が免除するものを §8 と §15 が名乗る**"
             "——**免除するのは「中身の確かさ」であって、場所でも時刻でも光でもない。**",
   "motion": "Full animation, not limited. **光が滑り、葉が裏返り、黒の縁が広がる。** "
             "⚠️ **カメラは1回だけ動き、そして止まる。**",
   "sound": "**風、乾いた葉。****音楽なし。言葉なし。** ⚠️ **洞からの音は無い。**",
 },

 "must_not": K.must_not_common(has_man=False, goddess_extra=(
     "**この1本は彼女の場所である**——**ゆえに女神の禁制は、ここでいちばん強く掛かる。** "
     "**内側を人で埋めない。****女の像を置かない。****誰かの気配を、顔の形で作らない。**")),
 "must": [
   "**洞口が黒くなる**——**そして岩の割れ目の細い線が消えるのが、切れ目のコマである。**",
   "⛔ **洞の内側を一度も見せない。****黒は黒のままである。**",
   "**この1本に人は一人も居ない** — どの距離にも、どのピントにも。",
   "⚠️ **女神を四つの姿のどれとしても出さない** — 声も、温かさも、動く空気も、水面の光も無い。"
   "⚠️ **ゆえにこの1本の女神は、場所そのものである。**",
   "**人の作ったものを一つも置かない** — 敷居も、段も、刻みも、灯火も無い。",
   "**火を一つも出さない。** **内側の温かさは、光ではなく気配である。**",
   "⚠️ **変化は最後のコマで終わる** — 線が消える瞬間に、この1本は終わる。",
 ],
 "prefer": "The mouth held in the upper part of the frame; the slope's rise legible underfoot; "
           "the leaves turning and returning; **the black given no colour at all** — the one value the "
           "grade does not touch.",
 "allow": "A lens flare where the light crosses the frame; a moderate depth of field that lets the "
          "scrub's far edge go soft; **a slow forward travel that does not arrive.**",

 "priorities": [
   "⛔ **内側を見せないこと。** **この1本の内容は「見えない」ことであり、見せれば別の1本になる。**",
   "**洞口が黒くなること** — そして**割れ目の線が消えるのが切れ目のコマであること。**",
   "⚠️ **女神を四つの姿のどれとしても出さないこと。** **この1本で彼女は場所である。**",
   "**人を一人も入れないこと** — どの距離にも、どのピントにも。",
   "**火を出さないこと。** **内側の温かさは光ではない。**",
   "⚠️ **`remembered-world` の5つを満たすこと** — 証人は `男`、滑るのは黒の縁、滑らないのは黒そのもの、"
   "正確なのは洞口の形、そして**滑ったものは戻る。**",
   "**日の光だけであること** — 専用の光源も、内側からの光も無い。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `remembered-world` を名乗るが、その禁制（`no drift that destroys identity`・"
   "`no caption explaining that this is a memory` ほか）は §16 に在って、ここには無い。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 13-second cinematic take (16:9) of a bronze-age island's inland slope at the end of the day, one clip, "
   "one continuous take, one change: **the cave mouth goes black.** **This is the first inland place this "
   "work shows, and it is the goddess's place — and she is not in it.**\n\n"
   "0-3.003s: **the cave mouth appears between the scrub, still far off, still grey.** The light is still on "
   "the rock.\n"
   "3.003-8.996s: **the light slides down the rock face and the leaves turn over.** The mouth is still grey.\n"
   "8.996-13s: **the mouth goes black and shows nothing.** One thin line of last light is left in a crack in "
   "the rock — **and the line goes out, and the take ends on that frame.**\n\n"
   "**The camera travels slowly toward the mouth and stops short of it; it never enters, and it does not move "
   "again after it stops.** **The inside is never seen — the black is black for the whole shot and no light "
   "comes out of it.** **No person is in this frame at any distance or in any focus; there is no figure on "
   "the slope and none in the mouth.** **No fire is in this frame; the warmth at the mouth is not light.** "
   "**The light is the sun's own and there is no other source.**\n"
   "**This is a bronze-age island before classical Greece: rough grey stone, dry scrub, sea-worn stone "
   "underfoot, and no made thing of any kind.** **This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the mouth goes black.)"),

 "visual_scene": (
   "A bronze-age island's inland slope at the end of the day, photographed as a film frame: rough grey stone "
   "rising against the sky, dry low scrub with leaves turned edge-on by the wind, sea-worn stone underfoot, "
   "dark cracks running across the rock face. **In the upper part of the frame, a cave mouth: a hole in the "
   "rock with no threshold, no stair and no made thing at it, and no inside visible in it — the black takes "
   "no colour at all and stays opaque for the whole shot.** One crack runs diagonally across the face beside "
   "the mouth and holds the last of the light as a thin line."),

 "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones", "rough grey rock with cracks and old water-marks") + (
   " ⚠️ **The black of the mouth is absolute and carries no detail** — it is the one value in the frame the "
   "grade does not touch, and nothing in it is ever legible."),

 "motion_prompt": (
   "Full animation, not limited. **The light slides slowly down the rock face** as the sun drops; **the "
   "leaves of the scrub turn over in the wind and turn back** — that turning and returning is the shot's "
   "drift. **The cave mouth's black widens: the rim of the black moves inward, and the black itself does "
   "not move at all.** **The crack's line of light narrows and goes out on the last frame.** "
   "**The camera travels forward slowly and stops short of the mouth, and does not move again.** "
   "No motion blur smears, no stutter, no floaty weightless motion, no static frames — **the light and the "
   "leaves move in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **at a walker's height on the slope**, low enough that the cave mouth sits above the "
   "frame's centre and the rise of the ground is legible. One event only: **a slow forward travel through "
   "the scrub toward the mouth that closes the distance without arriving, until it stops and holds while "
   "the mouth goes black.** ⚠️ **The move is motivated by the mouth; the stop is motivated by the mouth "
   "too.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** — a "
   "slow weighted forward travel, with the low frequency of a rig that has mass. ⚠️ **Do not enter the "
   "mouth and do not move again after the stop** — entering would make this a different shot. "
   "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **wind, and the dry leaves of the scrub scraping against each "
   "other.** ⚠️ **There is no human sound in this shot at all, and no sound comes out of the cave** — "
   "**anything heard from inside would be an answer, and this work never answers.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (remembered-world) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⚠️ **この1本に人物は居ないので、同一性の塊は §18 に入らない**"
                        "——**入るのは場所の記述である。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ wind ＋ dry leaves, and no sound from the cave ／ no music",
 "unresolved": [
   "⚠️ **`remembered-world` の5つ（`WITNESS`・`DRIFT`・`CONSTANT`・`EXACT`・`DURATION`）のうち、"
   "証人だけが画の中に居ない。****証人は `男` である**——**この1本は彼の記憶であり、彼はここに何年も居る。**"
   "⚠️ **この読みが正しいかは、著者が見て決める。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
   "⚠️ **「内側がある」と観客が信じるかどうかは、機械には測れない。** **測れるのは、"
   "§16 と `Master Prompt` が内側を一度も描写していないことまでである。**",
 ],
 "risks": [
   "⛔ **内側が見える。** この1本のいちばん高い危険である——**暗い内側に、形や、床や、光が現れれば、"
   "この1本は別の1本になる。** 禁制は §16 と `Master Prompt` の散文の両方に在る。",
   "**人が入る。** ⚠️ 洞の画に人を置くのは生成器にとって自然であり、**この作品では「一人」が主題である。**",
   "**火が出る。** ⚠️ 洞の内側を温かく見せようとすると、生成器は灯火を置く。"
   "**この作品は全ショットで火を禁じている。**",
   "**女神が現れる。** ⚠️ 「彼女の場所」という指定は、生成器には「彼女を出せ」と読まれうる。"
   "**四つの姿のどれも出さない。**",
   "**カメラが中へ入る。** ⚠️ **洞口へ寄る画は、そのまま入る画になりやすい**——"
   "**止まることが、この1本の内容である。**",
   "**割れ目の線が消えない。** 線が消えることが切れ目のコマの内容であり、**消えなければ、"
   "この1本は歌に渡すものを渡していない。**",
   "**洞口が完全な黒にならない。** 灰のまま終われば、**「内側がある」という確信が立たない。**",
 ],
}

if __name__ == "__main__":
    print("s02 content OK — keys:", len(C))
