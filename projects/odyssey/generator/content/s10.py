# -*- coding: utf-8 -*-
"""odyssey-s10 — time-fold — 森の洞口 / 夜 / 10.452s. has_man."""
import common as K


C = {
 "n": "s10",
 "title": "老いない 死なない——時間が通らない10秒",
 "duration": "10.452",
 "format": "time-fold",
 "has_man": True,
 "segment": "pre-chorus-2",

 "header": """⚠️ **行: `l07`「老いない 死なない」。** 場所は `森の洞口`、時刻は `夜`、尺は 10.452秒。
⚠️ **この行は 10.000秒であり、直後に 0.452秒の歌の無い間がある**（96.649–97.101）。
**この1本が吸うので、尺は 10.452秒になる。** ⚠️ **歌の無い間を、専用の行にしない**——
**それは容器である。**
⚠️ **この曲の「ちょうど 10.000秒」の行は5本ある。****字幕キューの上限を疑わせる**——
**「10秒歌われた」と読まない。**
⛔ **形式は `time-fold` である。****この作品で4本あるうちの2本目である。**
⛔ **`s03` は時間を通し、この1本は時間を通さない。**
**同じ形式の逆の使い方であり、ゆえにこの1本は `s03` を参照して読まれる。**
⚠️ **役は `開示` である。** 固有基準は「見せ方の順序・情報量・**何を隠したか**」——
⛔ **この1本が隠すのは、時間である。**
⛔ **開示の変化点は `s09` に在り、ここには無い**——`l07` は同じ開示の続きである。""",

 "intent": "One continuous take of one change — **time does not go through this shot.** The frame opens on the cave's black with the man standing at the edge of it; **the light moves the whole time** — the moon's angle changes, the underside of one leaf's temperature changes, his hair is moved by the air — **and yet at no point can it be said that anything has advanced**: the camera comes in on **one single strand of his hair, and that strand is in the same place at the end as it was at the start**, and the take ends on that frame — **through the 0.452 seconds after the singing stops, in which only the light moves and nothing changes.** ⚠️ **He does not age, does not move and does not speak; nothing is done to him and nothing is done to the place.**",

 "world_concept": K.world_concept(
   "⛔ **この1本は、この作品の「死なない島」を写す1本である。** "
   "**それは不死の像ではなく、時間の外にある10秒である。** "
   "⚠️ **人を止めて写すのではない**——**光と空気だけを動かし、"
   "そこにいる者を動かさないことで作る。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本で彼は何も言わない。****そしてこの1本は、"
               "何も求められていない10秒である**——**`l06` の差し出しに対する返事は、"
               "`s09` の沈黙であって、この1本ではない。**",
     "goddess": "⚠️ **彼女はこの1本に、四つの姿のどれとしても現れない**"
                "——**この1本は彼女の1本ではない。****この1本の主題は、"
                "そこにいる者が時間の外にあることである。** "
                "⚠️ **ゆえにこの1本には、理由の説明できない空気の動きも使わない**"
                "（`s09` がそれを使った）。**動くのは月の光と、彼の髪だけである。**",
     "name": "⚠️ **`l07` は「老いない 死なない」と歌う。****それは状態であって、名ではない。**",
     "bow": "⚠️ **この1本で彼は何も持たない。****手は空である。**",
     "places": "この1本が置くのは一つ——`森の洞口`、**`s02` が立て、`s09` が声の側から写した、"
               "同じ洞口である。**⚠️ **内陸である**——**海はこの画に入らない。**",
     "japanese": "⚠️ **この1本には歌がある**——`l07` がこの10.452秒のうちの10.000秒の上を"
                 "歌っている。**そして歌は日本語である。**⚠️ **末尾の0.452秒には、"
                 "歌が無い。****それでも、この1本は日本語の作品である。**",
   },
   extra=[
     "⛔ **「死なない」を、否定形で書かない。** **この作品は、"
     "老いないことを老いの否定として写さない**——**老いが来ないのではなく、"
     "時間が通らないのである。****ゆえに §16 の禁制はすべて「起きない」の形であって、"
     "「打ち消す」の形ではない。**",
     "⚠️ **`time-fold` は §15 と衝突しない**——**場所は動かず、時刻も動かない。"
     "****この1本が畳むのは時間そのものであり、場所でも同一性でもない。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "The mouth of a cave in a wooded slope at night, always seen from outside, photographed as a film. "
     "Rough grey rock split into a wide low opening; **the interior is wholly unlit — a black shape, not "
     "a room.** Dense low scrub and thin trees crowd the entrance and grow right up to the rock, with no "
     "path and no stair. ⚠️ **The man is of this place and not above it** — one coarse worn tunic, bare "
     "feet. ⚠️ **No marble, no columns, no architecture of any later age.**",
   "Color Language":
     "A narrow palette at night — cold blue-grey in the rock that faces the sky, and a black that holds "
     "no detail in the opening. ⚠️ **そして色は、この10.452秒のあいだに一度も移らない**"
     "——**移れば、それは時間が通ったということである。****光の角度は変わるが、色は変わらない。**",
   "Texture":
     "Rough grey rock with grain and fracture lines; dense scrub with leaves that catch what light there "
     "is; the black of the opening flat and detail-free, with no surface inside it; **his hair and the "
     "hem of his tunic, seen close.** ⚠️ **畳まれるのは時間であって、面ではない**"
     "——**肌も布も石も、この1本のあいだ、同じ粗さである。** Film grain present and even.",
   "Visual Density":
     "**Low and even, and it does not fall.** ⚠️ **この1本は密度を上げない**"
     "——**寄るのはカメラであって、物が増えるのではない。** "
     "**背景は `s09` と同じ洞口のままであり、新しい物は一つも入らない。**",
   "Atmosphere": "The ten seconds in which someone is not subject to the thing everyone else is subject to.",
   "Time": "`夜` — the light is the moon and the stars only. "
           "⛔ **そしてこの1本では、時刻が進まない**——**月の光は角度を変えるが、"
           "夜はまだ同じ夜である。****この作品は日付を固定しない。**",
 }),

 "subjects": [
   K.man_subject(
     behavior="**彼は洞の黒の手前に立っている。****この10.452秒のあいだ、彼は動かない。** "
              "**髪が空気で動く**——**それがこの1本で、彼に起きる唯一のことである。** "
              "⚠️ **彼は老いない。****肌も、髪の色も、姿勢も、この1本のあいだ変わらない。** "
              "⚠️ **カメラは彼の髪の一筋へ寄り、その一筋は最後まで同じ場所にある。**",
     may="髪の一筋が空気で動く量、光が当たる面、画の中で彼が占める大きさ、そして黒の縁の位置。",
     extra_notes=[
       "⚠️ **この1本は彼を止めて写すのではない。** **光と空気が動き続けるので、"
       "画面は止まっていない**——**それでも、彼の側では何も進まない。** "
       "**その差が、この1本の主題である。**",
       "⚠️ **彼は何も持たない。****手は空である。**",
       "⚠️ **彼はこの1本で一度も振り向かない。****そして口を開かない。**",
       "⚠️ **彼に歳を取らせない。****皺を増やさず、髪を白くせず、姿勢を変えない**"
       "——**それは化粧の問題ではなく、この1本が時間を通さないという問題である。**",
     ]),
   {"name": "nobody",
    "ref": "**この1本に、二番目の人物は居ない。** ⚠️ **この1本には、"
           "理由の説明できない空気の動きも無い**——**動くのは月の光と、彼の髪だけである。**",
    "appearance": "**無い。** ⚠️ **この1本の主題は、黒と、光と、動かない一人である。**",
    "behavior": "**無い。** ⚠️ **動くのは光と髪と空気だけである。**",
    "continuity": "⚠️ **二番目を入れないこと。** **この作品は「一人」の作品である。**",
    "notes": ["⚠️ **`Negative Prompt` はこの経路では床にならない**（§18 の前書き）。**ゆえにこれは"
              "肯定形で負う** — §16 `MUST NOT` と、`Master Prompt` 自身の一文が負う。",
              "⚠️ **弱い守りである。記録として書く。****洞の黒の中に人型を作るのは、"
              "生成器にとって自然である。**"]},
 ],

 "environment": {
   "location": "`森の洞口` — **`s02` が立て、`s09` が声の側から写した、同じ洞口である。** "
               "⚠️ **この1本は場所を作り直さない**——**岩の割れ目の走りも、潅木のbankも、"
               "`s09` のままである。**",
   "elements": "荒い灰色の岩、広く低い開口部、**内側はまったく灯りの無い黒**、"
               "入口に密集する低い潅木と細い木、そして月と星の光。"
               "⚠️ **道も、階段も、建てられた物も無い。****海はこの画に入らない。**",
   "behavior": "**月の光が、岩の面をゆっくり角度を変えて滑る。****葉の裏の明るさが、"
               "それにつれて変わる。** ⚠️ **潅木は、この1本では洞の側だけ揺れることをしない**"
               "——**それは `s09` の事象である。****この1本で空気が動かすのは、彼の髪だけである。** "
               "⚠️ **そして、光がどれだけ動いても、この場所は何も進まない。**",
 },

 "objects": [
   "**彼が持つもの: 無し。** ⚠️ **手は空である。**",
   "**岩**, grey and split into a wide low opening — **`s09` と同じ形である。**",
   "**潅木**, dense and low, crowding the entrance — ⚠️ **この1本では洞の側だけ揺れることをしない。**",
   "⚠️ **この作品の小道具は4つだけであり**（`ledger.props`）、**そのどれもこの1本には来ない。** "
   "**斧も、錐も、帆の布も、まだ彼の手に無い。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — **この1本には添付しない。彼女はこの1本に、四つの姿のどれとしても現れない。** "
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`女神.negatives` の6鍵である。",

 "narrative": {
   "core": "**時間が、この10秒を通らない** — 老いないとは、そういうことである。",
   "beginning": "**洞の黒。****葉が一枚、裏返る。**",
   "turn": "**光が角度を変える。****髪が揺れる。****しかし何も進まない。**",
   "peak": "**カメラが髪の一筋へ寄る。****同じ一筋が、まだ同じ場所にある。**",
   "pull": "⚠️ **歌の無い 0.452秒が、この1本の末尾に在る。****光だけが動き、"
           "何も変わらないまま切れ目が来る。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last four and a half seconds.** 最初の2.498秒は**黒と、"
            "裏返る葉一枚**のために払われ、次の3.501秒は**光が角度を変え、髪が揺れる**ことに払われ、"
            "**最後の4.453秒がこの1本の出来事である**——**カメラが髪の一筋へ寄り、"
            "そして歌の無い 0.452秒が末尾に来る。** "
            "⚠️ **`held` を1つも使わない。****止まるのは主題であって、画面ではない**"
            "——**光と、空気と、カメラは動く**（`shot-record.schema.json` の `motion`）。**ゆえに末尾は `dense` のまま切れる。** "
            "⚠️ **`time-fold` の5つの変数（形式カードの逐語。⚠️ 定義はカードの逐語である）**: "
            "`PLACE`＝the place that holds still — **`森の洞口`、`s02` が立てた洞口である。**"
            "**カメラはこの場所を離れない。**／ "
            "`PASSES`＝what time does to it — **光が岩の面を滑り、月の角度が変わり、葉の裏の明るさが変わり、"
            "彼の髪が空気で動く。** ⛔ **しかし、この1本では何も蓄積しない**"
            "——**角度が変わることは、時間が経つことではない。****それゆえこの1本は、"
            "`s03` の逆である。**／ "
            "`SURVIVOR`＝what does not change across the span — ⚠️ **ひとつだけ名指す。"
            "カメラが寄っていく、髪の一筋である。****10.452秒のあいだ、"
            "その一筋は動くが、最後まで同じ場所にある。****そして彼は老いない。** "
            "⚠️ **「光」を生存者にしてはならない**——**光が動くことが、この1本の材料である。**／ "
            "`RANGE`＝the span of time the shot crosses — ⛔ **跨ぐ幅は無い。**"
            "**この1本は一夜の幅を持ちながら、その幅を進まない。**"
            "**`s03` が畳んだのは一日の終わりだが、この1本は一日すら畳まない**"
            "——**畳めば、そこに時間が通る。**／ `DURATION`＝clip length — **`10.452s`**"
            "（**`l07` の 10.000秒と、直後の歌の無い 0.452秒を吸ったものである**）。",

 "actions": [
   ("ACT_BLACK", "洞の黒が画面を占め、彼が立っている。",
    "**葉が一枚、裏返る。****光は動いている。****他には何も起きない。**"),
   ("ACT_LIGHT", "月の光が岩の面にある。",
    "**光が角度を変える**——**髪が空気で揺れる。****しかし何も進まない。**"),
   ("ACT_STRAND", "カメラはまだ遠い。",
    "**カメラが髪の一筋へ寄る****——そしてその一筋は、まだ同じ場所にある。**"),
   ("ACT_END", "歌が止まる。",
    "**光だけが動き、何も変わらないまま切れ目が来る****——それが、この1本の切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **behind him, at the height of his head** — the lens at his back, so that "
               "his hair is the near subject and the black is beyond it. "
               "⚠️ **`s09` は彼の背後から洞口へ寄った。****この1本は彼の背後から、"
               "彼の髪の一筋へ寄る**——**洞ではなく、彼へ寄る1本である。**",
   "events": "One event only. `0-10.452s` — **one very slow continuous push toward a single strand of "
             "his hair, at a rate that does not change, still travelling on the last frame of the "
             "take.** ⚠️ **動機は光である**——**カメラは、光が当たっているものへ寄る。** "
             "⚠️ **この移動は「進む」ではない。****寄るだけで、何も明かされない。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** "
               "— a very slow weighted forward travel with the low frequency of a rig that has mass, "
               "**on a steady support, not handheld, and it does not wobble.** "
               "⚠️ **面が動かないので、寄りの効果は「近づく」ではなく「同じものを見続ける」である。** "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and **no unmotivated move.**",
 },

 "motion": {
   "subject": "**洞の黒、潅木の葉、男の髪と裾。** ⚠️ **時間そのものが主題である。** "
              "**彼は動かず、光と空気だけが動く。**",
   "object": "**葉の裏が、光の角度に合わせて明るさを変える。****そして元へ戻る。** "
             "⚠️ **動く物は無い**——**彼は何も持っていない。**",
   "environment": "**月の光が岩の面を滑り、角度を変える。****空気が彼の髪と裾を動かす。** "
                  "⚠️ **この1本では潅木が洞の側だけ揺れることをしない**"
                  "——**それは `s09` の事象である。**",
   "weight": "**黒は重い。****岩は重い。****彼も重い**——**この1本の動きはすべて、"
             "重さを持ったまま、ゆっくりである。**",
   "inertia": "**光は行き過ぎてから、わずかに遅れて面を離れる。****髪は押されたあと、"
              "少しだけ遅れて戻る。** ⚠️ **何も瞬間には戻らない。**",
   "acceleration": "**加速しない。** ⚠️ **カメラの寄りも、光の角度の変わり方も、"
                   "この10.452秒のあいだ一定である**——**加速すれば、そこに時間が通る。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この10.452秒に、"
               "止まったフレームは一つも無い**——**光と、空気と、カメラが動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**この1本の変化は、"
             "変化が無いことである。**",
 },

 "emotion": {
   "arc": "**10秒が過ぎる。** ⚠️ **そして、何も過ぎていない。** "
          "**この1本の感情は、その矛盾が平気でいることである。**",
   "events": "⛔ **この1本の出来事は、表情でも、まなざしでもない。****光が動いて、"
             "しかし何も蓄積しないことである。** **彼はそれを見ておらず、"
             "そして何も言わない。**",
 },

 "lighting": {
   "base": "Moonlight and starlight only, falling from behind the camera and from the sky above the "
           "slope; no fill, no artificial source and no fire. **The opening is a black shape against a "
           "lighter sky, and nothing inside it is ever lit.** ⚠️ **演出的な照明が、"
           "ここで時間を作る**（`motion.law` の註）——**光が角度を変えることが、"
           "この1本の「動いているが進まない」の材料である。**",
   "events": "**One, and it is continuous.** 月の光が岩の面をゆっくり滑り、**葉の裏の明るさが"
             "それにつれて変わる。** ⚠️ **光源は動かない**——**動くのは角度である。**"
             "⚠️ **そして、この光は一度も「別の光」にならない**"
             "——**色温度が移れば、それは時間が通ったということである。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**空気が彼の髪と裾を動かす音、葉が触れ合う音。** ⚠️ **足音は無い**"
          "——**彼は動かない。** ⚠️ **洞の中からは何も聞こえない。**",
   "music": K.NO_MUSIC + " ⚠️ **この1本の上では `l07`「老いない 死なない」が、"
            "10.000秒のあいだ歌われている**——**そして末尾の 0.452秒には、歌が無い。**"
            "**その無い区間が、この1本の末尾に在る。**",
   "environment": "夜の森の洞口、内陸。**空気と葉だけである。** "
                  "⚠️ **呼ぶ声は無い。****この1本では、誰も喋っていない。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="体格・肌・髪・髭・顔・傷・**着ている一枚と、着ていないすべて**。**裸足であること。** "
                "⛔ **そしてこの1本では、それらが10.452秒のあいだ変わらないこと**"
                "——**肌の粗さ、髪の白の混じり方、皺の深さ、姿勢、そのすべてが、"
                "最初のコマと最後のコマで同じである。** "
                "⚠️ **この1本は彼の髪へ寄るので、顔のすぐ近くまで来る**"
                "——**同一性の塊が、この1本では最も強く試される。**",
     may="髪の一筋が空気で動く量、光が当たる面、画の中で彼が占める大きさ、そして黒の縁の位置。"),
   "spatial": "斜面は画面の手前から奥へ上がり、**洞口は画面の上部にある。** "
              "**彼はその手前に背を向けて立っている。** ⚠️ **内陸である**"
              "——**海はこの1本の画に入らない。** ⚠️ **`s09` と同じ配置である**"
              "——**この1本は、`s09` が終わった画の続きから始まる**"
              "（**`s09` の末尾で黒が画面の大半を占めていた**）。",
   "temporal": "夜、**`s09` のすぐ続きである**——`l07` は `l06` の 6.016秒後である。"
               "⛔ **そしてこの1本では、時刻が進まない。****10.452秒のあいだ、"
               "夜は同じ夜である。****画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** ⚠️ **光は月と星だけである。** "
             "⚠️ **この1本は `time-fold` を名乗るが、`coexisting-realities` や `remembered-world` と"
             "違って §15 と衝突しない**——**場所は動かず、時刻も動かず、同一性も一つである。**"
             "**畳まれるのは時間そのものであり、ゆえに §15 は一句も免除されない。**",
   "motion": "Full animation, not limited. **光と、髪と、空気と、カメラが動く。** "
             "⚠️ **カメラは1回だけ動き、切れ目のコマでもまだ動いている。** ⚠️ **彼は1コマも動かない。**",
   "sound": "**空気、葉。****音楽なし。言葉なし。** ⚠️ **この1本で主題歌が歌っているが、"
            "この1本の中には無い**——**編集で載る。****そして末尾の 0.452秒には、歌も無い。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**この1本に彼女は現れない**——**ゆえに女神の禁制は、他人の形で来る。** "
     "**この10秒を、女の姿で説明しない。**")) + [
   "⛔ **Nothing may advance in this shot** — **no object grows, no plant withers, no shadow moves on "
   "and stays moved, no light becomes another light.** ⚠️ **この1本の変化は、"
   "変化が無いことである。**",
   "**No aging and no de-aging on the man** — **皺を増やさず、髪を白くせず、肌を乾かさず、"
   "姿勢を崩さない。****この1本は彼の髪へ寄るので、この危険が最も高い。**",
   "**No clock, no sundial, no hourglass and no marked time of any kind in the frame**"
   "——**時間を数える物を置けば、この1本は時間の話ではなく、時間を測る話になる。**",
   "**No colour temperature change across the take** — **色が移れば、それは時間が通ったということである。**",
   "**No second person in frame at all** — no companion, no crowd, **no figure inside the black, "
   "and no one at any distance.**",
 ],

 "must": [
   "**The light moves and nothing advances** — **この10.452秒のあいだ、"
   "何も蓄積しない。**",
   "**One strand of his hair is the survivor** — **それは動き、そして最後まで同じ場所にある。**",
   "**He does not age and the place does not change** — **肌も、髪も、岩も、潅木も、"
   "最初のコマと同じである。**",
   "**The camera travels in and is still travelling on the last frame.**",
   "**The 0.452 seconds after the singing stops is part of this shot** — **光だけが動き、"
   "何も変わらずに切れる。**",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot**, **and that none of it changes in 10.452 seconds.**",
   "⚠️ **He does not turn, does not look at the lens and does not open his mouth.**",
 ],

 "prefer": "The black of the opening beyond him; moonlight changing its angle on the rock; the underside "
           "of one leaf brightening and going back; his hair moved by the air and settling again; the "
           "camera ending on one strand.",

 "allow": "A moderate depth of field that lets the slope behind go soft; the moon's light laying a hard "
          "edge on the rock that faces the sky; grain running faintly through the black.",

 "priorities": [
   "⛔ **Nothing advances.** ⚠️ **この1本の主題は、動いているのに進まないことである。**"
   "**何かが進めば、この1本は `s03` の劣化した写しになる。**",
   "⛔ **The man does not age.** ⚠️ **この1本は彼の髪へ寄るので、肌と髪と皺が最も強く試される。**"
   "**参照画像は1枚も無い**（裁定②）——**§18 の英文だけがそれを守る。**",
   "**The camera is still travelling on the last frame** — **止まるのは `s09` の側である。**",
   "**The 0.452 un-sung seconds are absorbed at the tail** — ⚠️ **専用の行にしない。"
   "****そして「10秒歌われた」と読まない。**",
   "**One light, one grade, and no colour temperature change.**",
   "**`s10` begins where `s09` ended** — **同じ洞口、同じ夜、同じ彼である。**",
   "**Japanese is what this work speaks** — named in §18, and the line sung over this shot is Japanese.",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `time-fold` を名乗るが、その禁制（`no cut`・`no time-skip`・`no date stamp`・"
   "`no aging makeup`・`no cross-dissolve` ほか）は §16 に在って、ここには無い。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 10.452-second cinematic take (16:9) of the mouth of a cave in a wooded slope at night, one clip, "
   "one continuous take, one change: **time does not go through this shot.** "
   "**The light moves for the whole take and nothing advances: the man does not age, the place does not "
   "change, and one strand of his hair is in the same place at the end as it was at the start.**\n\n"
   "{IDENTITY}\n\n"
   "0-2.498s: **the cave's black holds the frame and the man stands at the edge of it**; one leaf turns "
   "over. The moonlight is already moving.\n"
   "2.498-5.999s: **the light changes its angle on the rock and his hair is moved by the air** — "
   "**and nothing has advanced.** Not a colour, not a shadow that stays moved.\n"
   "5.999-8.497s: **the camera comes in on one single strand of his hair, and that strand is still in "
   "the same place.**\n"
   "8.497-10.452s: **only the light moves, and nothing changes, and the take ends on that frame** — "
   "**this last 0.452 seconds is the part of the shot in which nothing is sung over it, and it is "
   "still the same shot.**\n\n"
   "**Nothing in this shot advances**: no object grows, no plant withers, no shadow moves on and stays "
   "moved, and the colour temperature does not change from the first frame to the last. "
   "**The man does not age in it** — the same skin, the same hair with the same grey in it, the same "
   "lines and the same posture at the end as at the start — **and he does not move**: no step, no turn "
   "and no gesture, and his mouth stays closed. "
   "**The camera travels very slowly in toward a single strand of his hair and is still travelling on "
   "the last frame.** "
   "**The light is the moon and the stars only, from behind the camera and from the sky above the "
   "slope; only its angle changes, the colour stays, and nothing inside the opening is ever lit.** "
   "**No second person is in this frame at any distance or in any focus** — no one at the cave mouth, "
   "no figure inside the black, no companion, no crowd. "
   "**This is a bronze-age shore before classical Greece: one coarse wool tunic, bare feet, no armour, "
   "no helmet, no weapon, no ornament, and no heroic pose and no heroic lighting.** "
   "**This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the light moves and nothing advances.)"),

 "visual_scene": (
   "The mouth of a cave in a wooded slope at night, always seen from outside, photographed as a film "
   "frame: rough grey rock split into a wide low opening, with the fracture lines running across it; "
   "dense low scrub and thin trees crowding the entrance and growing right up to the rock; no path and "
   "no stair; moonlight and starlight laying a hard edge on the rock that faces the sky. **The interior "
   "of the opening is wholly unlit — a flat black shape with no surface inside it.** **A man stands "
   "before the opening with his back to the lens, still, small against the rock, with one strand of his "
   "hair lifted by the air; the moonlight is at an angle on the rock, and nothing in the frame is "
   "different from one moment to the next except the light.**"),

 "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones",
   "rough grey rock with fracture lines and a black opening with no surface inside it") + (
   " ⚠️ **One light and one grade for the whole take** — the moonlight's angle changes and the colour "
   "does not."),

 "motion_prompt": (
   "Full animation, not limited. **The man does not move at all**: no step, no turn, no gesture and no "
   "tilt of the head in the whole take, and **only one strand of his hair and the hem of his tunic move "
   "in the air, and they settle again.** What moves is the light and the camera. "
   "**The moonlight slides across the rock and changes its angle, and the underside of one leaf "
   "brightens with it and goes back.** ⚠️ **Nothing accumulates**: no shadow moves on and stays moved, "
   "no colour shifts, the man does not age and nothing in the frame is different at the end from what "
   "it was at the start **except the light's angle.** "
   "**The camera travels very slowly in toward one strand of his hair and does not stop.** "
   "No motion blur smears, no stutter, no floaty weightless motion, no static frames — **the light, the "
   "air and the camera move in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **behind him, at the height of his head** — the lens at his back, so that his hair is "
   "the near subject and the black is beyond it. One event only: **one very slow continuous push toward "
   "a single strand of his hair, at a rate that does not change, still running on the last frame of the "
   "take.** ⚠️ **The move is motivated by the light — the camera goes toward what the light is on.** "
   "⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** — a very "
   "slow weighted forward travel with the low frequency of a rig that has mass, **on a steady support, "
   "not handheld.** ⚠️ **Because the surface does not change, this travel reads as staying with the "
   "same thing rather than as getting closer to anything.** "
   "⚠️ **Do not reveal anything by moving: this shot uncovers no new part of the frame.** "
   "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, no unmotivated "
   "move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **air moving his hair and the hem of his tunic, and leaves "
   "touching each other.** ⚠️ **He says nothing and he does not move, so there is no footfall in this "
   "shot, and no sound comes out of the opening** — **this shot's sound is air and leaves, and it does "
   "not change from the first frame to the last.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (time-fold) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⚠️ **同一性は `Visual Prompt` の英文が運ぶ**——"
                        "**`s05` が立てた基準を、この1本は夜の側で、そして最も近くで繰り返す。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ air ＋ leaves ／ no music",
 "unresolved": [
   "⛔ **「動いているが進まない」を、機械は測れない。** **測れるのは、§16 と `Master Prompt` が"
   "「何も蓄積しない」と書いていることまでである。** "
   "⚠️ **この1本の失敗の形は「何かが進む」であって、それは `s03` の劣化した写しになる。**",
   "⛔ **10.452秒のうち、歌が乗っているのは 10.000秒である。** **末尾の 0.452秒には歌が無い。**"
   "**この0.452秒が、この作品では「容器」としてこの1本に吸われている**"
   "——**専用の行にしない、という記録の判断である。****それが正しいかは、私が決めたことではない。**",
   "⚠️ **`s03` と同じ形式である。****この1本が `s03` の逆として読めるかどうかは、"
   "「何も進まない」が実際に保たれるかに掛かっている。****ゆえにこの1本は、"
   "この作品で最も静かな失敗（少しだけ進む）をしやすい。**",
   "⚠️ **この1本は彼の髪へ寄るので、顔のすぐ近くまで来る。** **参照画像が1枚も無い状態で"
   "10秒間それを保つのは、この作品で最も高い注文の一つである**（裁定②）。",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **何かが進む。** ⚠️ **この1本のいちばん高い危険である。****進めば、"
   "この1本は `s03` の劣化した写しになる。**",
   "⛔ **彼が老いる。** ⚠️ **10秒のあいだに皺が増え、髪が白くなる**"
   "——**生成器が「時間の経過」をそう解釈するのは自然である。**",
   "**色温度が移る。** ⚠️ **移れば、それは時間が通ったということである。**",
   "**光が「別の光」になる。** ⚠️ **光源は月と星だけであり、それは変わらない。**",
   "**カメラが何かを明かす。** ⚠️ **寄るだけで、新しい部分を写さない。**",
   "**洞の黒の中に人型ができる。** ⚠️ **禁制集合は「いかなる距離でも、"
   "いかなる焦点でも、女を枠に入れない」と言っている。**",
   "**顔が動く（drift）。** ⚠️ **この1本は最も近くへ寄るので、この危険が最も高い。**"
   "**参照画像が1枚も無いので、守る道具は英文だけである**（裁定②）。",
 ],
}

if __name__ == "__main__":
    print("s10 content OK — keys:", len(C))
