# -*- coding: utf-8 -*-
"""odyssey-s12 — video-spec — 海 / 日没 / 9.734s. He leaves the frame in the first movement."""
import common as K


C = {
 "n": "s12",
 "title": "私は海を見ている——視線が交わらない",
 "duration": "9.734",
 "format": "video-spec",
 "has_man": True,
 "segment": "pre-chorus-4",

 "band": [
   "『永遠より遠い』 pre-chorus「海」 / 情景 / motion —— 私は海を見ている——視線が交わらない",
   "男が岸に立ち、海を見ている——海は彼の前にある。",
   "9.734秒、カメラは水面すれすれを左へ滑り、彼の視線の先へ行く——反射が一度に割れるのが、切れ目である。",
   "視線は交わらず、誰も彼を見返さない——写るのは、海と、その手前だけである。",
 ],
 "header": """⚠️ **`l08` と対である**——**視線が交わらない。**
`s11` は「**見られている**」であり、この1本は「**見ている**」である。
⛔ **この作品は、この2行を1本ずつに割った**——**同じ1本に入れれば、視線が交わることになる。**
⛔ **形式は `video-spec`。****不可視の視点（`s11`）が続いた直後に、いちばん素の画を置く。****文法を戻すことで、対が見える。**
⚠️ **この1本は `海` であるが、彼は岸に居る。****見えているものが海だからである**（`locations.海.geography` の註——「岸から見る海と、舟から見る海は、同じ場所である。**二つに割らない。**」）。
⛔ **彼は、この1本のあいだに枠の外へ出る。**——`unit` は前で「洞の黒の前に男が居る」と言い、後で「**男は岸に居て、海を見ている。**」と言い、**ビートの1つめは「彼はもう画面に居ない。」と書く。**⚠️ **ゆえに彼は冒頭に枠に居て、この1本のあいだに去る**——**去ることが、この1本の変化である**（2026-09-29 の裁定②）。⚠️ **1つめのビートが終わるまでに、彼は枠の外へ出る。**
⛔ **この1本は、彼の視線だけを写す1本である**——**彼は岸に居て、海を見ており、枠には戻らない。**⚠️ **彼は一度もレンズを見ない**——**ゆえに視線は交わらない。**
⚠️ **行: `l09` ／ 場所: `海` ／ 時刻: `日没` ／ 尺: 9.734秒。**
⚠️ **この仕様のショット記録は `shots/odyssey-s12.yaml` である。**""",

 "intent": "One continuous take of one change — **水平線が画面の中央へ来て、反射が一度に割れる。** 最初のコマでは海と手前の砂があり、**水面の反射は一枚である。** 最後のコマでは**水平線が画面の中央にあり、反射が一度に割れている**——⚠️ **カメラはそのあと動かない。** ⛔ **切らない。視点を変えない。** ⚠️ **この1本に居るのは彼一人である**——**彼は最初のビートで枠の外へ出る。****ゆえに出たあとのこの1本は、彼の視線の代わりをする画である。** ⚠️ **変化は切れ目のコマで終わる**——**反射が一度に割れたコマで、この1本は終わる。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、`l08`「私の顔を見ている」への返しである。**——`s11` が「**見られている**」なら、"
   "この1本は「**見ている**」である。⛔ **そして見ている者は、この1本のあいだに枠の外へ出る**——**最初のビートで岸へ出て、そこから海を見る。** "
   "**残るのは海だけである**——**この作品でいちばん大きいもの**（`ledger.locations` の註:"
   "「**この作品でいちばん大きいもの。**」）**が、人の代わりに画面を占める。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本に居るのは彼一人であり、彼は最初のビートで枠の外へ出る。** **ゆえに返事は、ここでも返されない**——"
               "**彼は海を見ており、海は答えない。**",
     "goddess": "⚠️ **この1本に彼女の姿は無い。****四つの姿のどれとしても現れない**——"
                "**この1本の水面の道は、日の光である**（`ledger.locations.海.states.日没` の逐語:"
                "「低い太陽が水面に一本の道を作っている。」）。⚠️ **彼女の第四の姿は「枠の外の背後から来る"
                "水面の光」であり、この道は前方から来る。** ⚠️ **声も、この1本の記録には無い**（§20 を見る）。",
     "name": "⚠️ **この1本には歌がある**——`l09` である。**名はどこにも無い。**",
     "bow": "⚠️ **この1本に持ち手が無い。****弓は無論のこと、斧すら無い。**",
     "places": "この1本が置くのは一つ——`海`、**この作品でいちばん大きいものである。** "
               "⚠️ **この1本は `岸` を引かない**——**見えているものが海だからである。**",
     "japanese": "⚠️ **この1本には歌がある**——`l09`「私は海を見ている」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **この作品は `l08` と `l09` を1本ずつに割った。** ⚠️ **同じ1本に入れれば、視線が交わる**"
     "——**この1本は、その分割の後半である。****ゆえに彼は、この1本のあいだに枠の外へ出る。**",
     "⚠️ **この1本の光は日の光だけである。****水面の道は、日のものである**"
     "（`bible.negative_base` が全ショットで火を禁じている）。",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "The open sea seen from an island's shore at the last of the day, photographed as a film: long low "
     "swells with no white water moving steadily in one direction, one unbroken horizon, a single path of "
     "warm light lying on the surface, and the near sand of the waterline dark and coarse at the frame's "
     "lower edge. ⚠️ **Beyond the waterline there is no land at all** — no island, no headland, no rock. "
     "⚠️ **No marble, no columns, no architecture of any later age.**",
   "Color Language":
     "A narrow, graded palette — cold slate blue in the water, warm ochre held in the single path on the "
     "surface, and the near sand dull and dark. ⚠️ **Nothing is lit apart from the water and the sand** "
     "— the same raking light falls on everything in the frame, and **the shot has no second light.**",
   "Texture":
     "The water's surface fine-grained and broken into small facets, the faces of the swell smooth and "
     "glassy; the near sand coarse and dark, cut across by the waterline; no foam, no spray, no white "
     "water. ⚠️ **The only skin and cloth in this frame are the man's, and only in the first movement, as he leaves it** — after that no person is in it at all. "
     "Film grain present and even.",
   "Visual Density": "Low. **The frame holds the water, the horizon and the near sand** — nothing else.",
   "Atmosphere": "The hour in which the gaze is in the frame and the one gazing goes out of it.",
   "Time": "`日没` — the last of the day, **the same evening as `s01`–`s08`**. ⚠️ **歌はこの1本を `夜`（`s11`）"
           "のあとに置く**——**この作品は話を進めないので、順序は逆行してよい**"
           "（§2 の逐語:「the work does not advance a story」）。**画の中に日付を与えるものは何も無い。**",
 }),

 "subjects": [
   dict(K.man_subject(
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
       "塊は作品の錠であると同時に、この枠の中身でもある。****§20 を見る。**"])),
   {"name": "海",
    "ref": "**この1本の主題である。** ⚠️ **参照は `ledger.locations.海` の `base`・`geography`・"
           "`states.日没` である。** ⚠️ **岸から見た海である**——**そして舟から見た海と同じ一つの海である**"
           "（台帳の註の逐語:「**岸から見る海と、舟から見る海は、同じ場所である。二つに割らない。**」）。",
    "appearance": "**長いうねりであり、白波を立てない。****水平線は一本で、途切れない。** "
                  "**そして水面に、低い日を受けた一本の道がある。** ⚠️ **陸は無い。****帆も、鳥も、"
                  "他の舟も無い**（`海.base`）。**手前には、水際に切られた砂がある。**",
    "behavior": "**うねりが一方向へ進む。****反射の道が細かく割れる。****そして波が返り、"
                "反射が一度に割れる**——⚠️ **それがこの1本の切れ目のコマである。** ⚠️ **水平線は動かない**"
                "——**動くのは、水平線の画面の中の高さである**（カメラが滑るからである）。",
    "continuity": "**Must preserve** — **水際の線、水平線の高さと途切れなさ、日の道の色温度、"
                  "白波が無いこと、そして陸・帆・鳥・他の舟が無いこと。** "
                  "**May change** — 反射の割れ方の細かさ、うねりの高さ、砂の明るさ、道の幅。",
    "notes": ["⚠️ **`海.base` の逐語:「Open sea, far from any land. Long low swells with no white water, "
              "moving steadily in one direction; the surface broken only by the raft's own wake and by "
              "weed passing.」**——⚠️ **この1本には筏の航跡が無い**（**筏はまだ枠の外である**）。"
              "**ゆえに水面を割るものは、うねりと反射だけである。**",
              "⚠️ **水際の線と水平線は、この作品のどの岸の画と同じものである**"
              "（`海.geography` の逐語:「The same waterline and the same horizon appear in both, so that "
              "the two views are demonstrably one sea.」）。"]},
 ],

 "environment": {
   "location": "`海` — **岸から見た海である。** ⚠️ **この1本の画面は海である**（`岸` は引かない——"
               "**見えているものが海だからである**）。**水際のすぐ沖に、水面すれすれでカメラがある。**",
   "elements": "**長いうねり**（白波は無い）、**途切れない水平線**、**水面の一本の道**、"
               "**手前の砂**、そして**水際の線**。 ⚠️ **水際の向こうに陸は無い。****帆も、鳥も、"
               "他の舟も無い。** ⚠️ **人工物を一つも置かない**——**桟橋も、網も、杭も無い。**",
   "behavior": "**うねりが一方向へ進む。****反射の道が細かく割れ、そして一度に割れる。** "
               "**手前の砂は動かない**——**動くのは、砂と水の境の線だけである。** "
               "⚠️ **場所は人に反応しない**——**彼が枠の外へ出ても、海は何もしない。**",
 },

 "objects": [
   "**無し。** ⚠️ **この1本に小道具は来ない。** **この作品の小道具は4つだけであり**（`ledger.props`）、"
   "**そのどれもこの枠に来ない**——**舟はまだ浜で作られており、帆はまだ縫われておらず、"
   "斧は仕事場に立ち、太陽の牛は記憶の中にしか居ない。**",
   "**水面の反射の道**, breaking into small facets and then breaking all at once — "
   "⚠️ **これは物ではない。****この1本の動くものであり、切れ目のコマを作る。**",
   "**水際の砂**, cut across by the waterline at the frame's lower edge — **この1本の手前の地面である。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****そしてこの1本で彼が枠に居るのは、"
                  "最初のビートだけである**（2026-09-29 の裁定②。§20 を見る）。"
                  "`女神` — ⛔ **この1本に添付しない。****彼女は四つの姿のどれとしても現れない。**"
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.日没` の5鍵である。"
                  "⚠️ **`男.identity` が引かれているのは、この1本に彼が居るからである**"
                  "——**そしてこの1本は、その塊を §18 の両方に貼る**（`has_man: True`）。",
 "ref_extra": [
   "- ⚠️ **形式カード `video-spec` の文法は、この作品の下敷きそのものである**"
   "——**他の形式はどれも「`video-spec` に文法を1つ足したもの」である**"
   "（例: `impossible-camera` の逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly "
   "as that card requires; what follows is only what this grammar adds to it.」）。"
   "**ゆえに §1–20 の骨格は `s01` と同じであり、この1本はそれに何も足さない。**",
   "- ⚠️ **形式カード `video-spec` の6つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `SUBJECT`＝the arc — **「私は海を見ている」を、海の画だけで返すことである。**"
   "**彼は最初のビートで枠の外へ出るので、残るのは海の画だけである**（`shot.aim` の逐語:「**「私は海を見ている」を、海の画だけで返せるか。**"
   "そして**`l08` の対であることを、観客に説明せずに立てられるか。**」）。",
   "  - `DURATION`＝clip length (**the model decides the duration**) — ⚠️ **この作品の尺は、"
   "曲から来る**（`bible.song.lines[].at` の差）。**この1本は `9.734s` である**"
   "——**「4秒より短いから伸ばす」をしない**（`docs/seedance-route.md` の明示の規則）。",
   "  - `ASPECT`＝aspect ratio — **`16:9`**（裁定④。§1 の4定数が固定する）。",
   "  - `BEATS`＝the beat list with second ranges — **3つであり、明示的に不等である**"
   "（`0-2.502s` transition ／ `2.502-5.996s` sparse ／ `5.996-9.734s` dense）。§8 を見る。",
   "  - `CORE`＝the beat that gets the largest share — **最後のビートである**（`5.996-9.734s`、3.738秒）。"
   "⚠️ **3つはほぼ等分に見えるが、等分ではない**——**この1本の山は最後にあり、"
   "最初のビートは、彼が枠の外へ出ることに払われる。**",
   "  - `HOOK`＝the note the clip ends on — ⚠️ **反射が一度に割れたコマである。**"
   "**説明のビートをそのあとに足さない**（カードの逐語:「End on the note, not after it.」）"
   "——**この1本は、割れたコマで終わる。**",
   "- ⚠️ **カードの逐語:「A digest that gives every beat equal time is the video equivalent of "
   "cramming. **Uneven duration is the composition.**」**——この1本の配分は §8 に在る。**",
 ],

 "narrative": {
   "core": "**海が、彼の見ているものをそのまま返す** — 見ている者は去り、海だけが「見ている」を立たせる。",
   "beginning": "**海と、手前の砂。** 波は低く、**反射はまだ一枚である。****彼はこのビートのあいだに、枠の外へ出る。**",
   "turn": "**カメラが水面すれすれを左へ滑る。** 反射が細かく割れる。",
   "peak": "**水平線が画面の中央に来る。** うねりが返る。",
   "pull": "⚠️ **反射が一度に割れるのが、切れ目のコマである。** **カメラはそのあと動かない。** "
           "**見ていることが、画面の側にだけ残る。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 3.738秒.** 最初の2.502秒は**海と砂のために払われる**"
            "——⛔ **彼が枠の外へ出ることが、そこで起きる。** 次の3.494秒で**カメラが滑り、反射が割れはじめ**、"
            "**最後の3.738秒がこの1本の出来事である。** ⚠️ **`held` を1つも使わない。** "
            "⚠️ **3つのビートは近い長さだが、等分ではない**——**最後が最も長い。**",

 "actions": [
   ("ACT_SEA", "波が低く、反射はまだ一枚である。",
    "**海と、手前の砂があり、彼が枠の外へ出て行く**——**このビートの終わりには、彼はもう居ない。**"),
   ("ACT_SLIDE", "反射はまだ一枚である。",
    "**カメラが水面すれすれを左へ滑る**——**動機は「彼の視線の先へ行くこと」である。**"),
   ("ACT_BREAK", "反射が割れはじめる。",
    "**反射が細かく割れる**——**うねりが返る。**"),
   ("ACT_CENTRE", "水平線はまだ画面の中央に無い。",
    "**水平線が画面の中央に来る**——**反射が一度に割れるのが、切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **at the surface of the water just off the shingle**, low enough that the "
               "horizon sits near the frame's centre and the near sand lies at the frame's lower edge. "
               "⚠️ **この1本のカメラは、彼の位置ではない**——**彼は最初のビートで枠の外へ出て、岸から海を見る。**",
   "events": "One event only. `0-2.502s` — **the frame holds the water and the near sand; the man goes out of the frame as this movement runs, and "
             "by its end there is nobody in the frame**; then `2.502-5.996s` — **a slow lateral travel left along the surface of the water**; "
             "then `5.996-9.734s` — **the travel ends when the horizon has come to the centre of the "
             "frame, and the reflection breaks all at once.** ⚠️ **動機は「彼の視線の先へ行くこと」である。** "
             "⚠️ **この1本は一度も岸へ向かない**——**振り返れば、この1本は彼の画になる。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** "
               "— a lateral travel at water height with the low frequency of a rig that has mass, and it "
               "does not wobble. No crane is used and no Steadicam: the travel stays at the water's own "
               "height and it does not rise. ⚠️ **止まったあと、カメラは動かない。** "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, and "
               "**no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、水面と、その上の反射である。** ⚠️ **うねりは低く、一方向へ進む。** "
              "**反射の道は細かく割れ、そして一度に割れる。****手前の砂は動かない。**",
   "object": "**動く物は無い。****この1本に物は一つも置かれていない**——**動くのは水と光と、最初のビートの彼だけである。**",
   "environment": "**うねりが一方向へ進み、水面が細かく割れる。** ⚠️ **風は弱く、白波を立てない**"
                  "（`海.base` の逐語:「Long low swells with no white water」）。"
                  "⚠️ **陸は水際の向こうに無く、帆も舟も鳥も無い。**",
   "weight": "**水の重さは、うねりの面に出る**——**低く、遅く、途切れない。** "
             "⚠️ **速い水はない。****この1本の水は、押すものであって、砕けるものではない。**",
   "inertia": "**割れた反射は、すぐには戻らない。** ⚠️ **うねりは、反射が割れたあとも進み続ける**"
              "——**止まるのは、この1本の最後のコマである。**",
   "acceleration": "**加速しない。** ⚠️ **うねりは速くならず、カメラも速くならない**"
                   "——**滑りは一様であり、終わりは水平線が決める。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この9.734秒に、止まったフレームは"
               "一つも無い**——**水は最後のコマまで動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**白波を立てないことが、この海の性質である**"
             "（`海.base` の逐語:「no white water」）。",
 },

 "emotion": {
   "arc": "**見ている者は、この1本のあいだに枠の外へ出る。****それでも、見ていることが立つ。** ⚠️ **この1本の感情は、海の側には無い**"
          "——**観客が、彼の代わりに海を見ることで生まれる。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****反射が一度に割れることである。** "
             "**彼は去り、視線だけが残る。**",
 },

 "lighting": {
   "base": "The sun's own light, low and raking across the water and making one path on the surface; no "
           "fill, no artificial source, **and no second light.** ⚠️ **この1本の光は日の光だけである**"
           "（`ledger.locations.海.states.日没` の逐語:「低い太陽が水面に一本の道を作っている。"
           "**この光は岸から見たものである。**」）。⚠️ **彼女の第四の姿（枠の外の背後から来る水面の光）は、"
           "この1本には無い**——**この道は前方から来る。**",
   "events": "**One, and it runs the whole shot.** 日の低さは変えず、**反射の道が細かく割れ、"
             "そして一度に割れる。** ⚠️ **光源は動かない**——**様式カードの逐語:「The grade holds for the "
             "whole shot — a colour temperature that swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**低いうねりが水面を進む音。****水際で、水が砂に当たる音。** "
          "⚠️ **この1本に人の音は一つも無い**——**彼は黙っており、足音もこの1本のミックスに載せない。** "
          "⚠️ **呼ぶ声は無い**——**この1本の記録は、彼女の声について何も言わない**（§20 を見る）。",
   "music": K.NO_MUSIC + " ⚠️ **主題歌はこの1本のあいだ鳴っている**（`l09`）——**が、"
            "この1本の中には無い。****編集で載る。** **生成された音床が来れば、同じ瞬間に"
            "二つの音楽が重なる。**",
   "environment": "日没の海。**うねり、水際の砂、そして弱い風。** "
                  "⚠️ **鳥の声も、帆の音も無い**——**この1本の海には、彼以外の何も居ない。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="**この1本の人物は、最初のビートだけ枠に居る**——**同一性の塊は §18 の `Visual Prompt` と"
                "`Master Prompt` の両方にまるごと入る**（`has_man: True`）。"
                "⚠️ **ゆえにこの1本も、`s05` が立てた顔から外れてはならない。**",
     may="水面の割れ方、反射の道の幅、うねりの高さ、水平線の画面の中の高さ、砂の明るさ。"),
   "spatial": "**水際のすぐ沖に、水面すれすれでカメラがある。****手前の砂は枠の下端にある。** "
              "⚠️ **水際の線と水平線は、この作品のどの岸の画と同じものである**"
              "（`海.geography` の逐語:「The same waterline and the same horizon appear in both, so that "
              "the two views are demonstrably one sea.」）——**ゆえにこの1本は、舟から見る海と"
              "同じ一つの海である。** ⚠️ **彼は岸に居て、最初のビートのあいだに枠の外へ出る。**",
   "temporal": "一日の終わり、**`s01`〜`s08` と同じ夕べである。** ⚠️ **歌はこの1本を `夜`（`s11`）の"
               "あとに置く**（`l08` の次が `l09`）——**この作品は話を進めないので、順序は逆行してよい。** "
               "**画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は日の光だけである。**"
             "⚠️ **この1本は `video-spec` を名乗り、この形式は §15 から何も免除しない**"
             "——**免除を名乗るのは、`coexisting-realities` を名乗る4本（`s07`・`s15`・`s22`・`s29`）だけである。**"
             "**この1本の場所と時刻は、台帳の `海`／`日没` のままである。**",
   "motion": "Full animation, not limited. **水面が動き、反射が割れ、カメラが1回だけ滑る。** "
             "⚠️ **カメラは止まったあと動かない。**",
   "sound": "**うねり、水際の砂、弱い風。****音楽なし。言葉なし。** ⚠️ **呼ぶ声は無い。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "⚠️ **この1本の彼女は、四つの姿のどれとしても現れない**——**水面の道は日の光であり、"
     "彼女の光ではない。****ゆえに彼女の禁制は、ここでも強く掛かる。****透ける姿も、輪郭も、"
     "声も置かない。**")) + [
   "⛔ **The only person in this frame is the one man, and only in the first movement** — **no second "
   "person at any time** — he goes out of the frame before that movement ends, and after he has gone "
   "there is no figure at any distance or in any focus, no silhouette, no one on the sand, and no shadow "
   "or reflection of a person anywhere. ⚠️ **ビートの1つめの逐語:「彼はもう画面に居ない。」**",
   "**No land beyond the waterline** — no island, no headland, no other shore, no rock in the water, "
   "**and the horizon unbroken**（`海.base` の逐語:「The horizon is level and unbroken.」）。",
   "**No bird, no sail, no other vessel, and no wreckage**（`海.base` の逐語:「No land, no sail, "
   "no bird, no other vessel.」）。",
   "**No white water, no breaking crest, no foam and no spray**（`海.base` の逐語:「Long low swells with "
   "no white water」）。⚠️ **この1本の波は低い。**",
   "**No second light, no fill, no umbrella setup, no flat television lighting** — "
   "**この1本の光は日の光だけである。**",
   "**No cut to a second setup.** ⚠️ **この1本は1つの画である。**",
 ],

 "must": [
   "**反射が一度に割れる** — そして**水平線が画面の中央に来ていることが、切れ目のコマである。**",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.** ⚠️ **この1本では、彼は最初のビートだけ枠に居て、やがて枠の外へ出る**"
   "——**塊は、その彼の同一性である。**",
   "⛔ **彼以外の誰も入れない** — どの距離にも、どのピントにも、**影にも、映り込みにも。** "
   "⚠️ **彼自身は、最初のビートのあいだに枠の外へ出る。**",
   "⚠️ **水際の線と水平線は、この作品の岸の画と同じものである** — **同じ一つの海であることが、"
   "二つの画のあいだで読めること。**",
   "⚠️ **水平線が画面の中央へ来ること** — **この1本の変化はそこへ向かう。**",
   "**日の光だけであること** — **専用の光源も、二つ目の光も無い。**",
   "⚠️ **変化は最後のコマで終わる** — **反射が一度に割れたコマで、この1本は終わる。**",
 ],

 "prefer": "The horizon held level and unbroken; the single path of light lying on the surface and "
           "breaking into fine facets; the near sand dark and coarse at the frame's lower edge; "
           "**the frame with no figure in it after the first movement, and nothing in it that reads as "
           "one.**",
 "allow": "A lens flare where the light crosses the frame; a moderate depth of field that lets the far "
          "water go soft; **a lateral travel at water height that ends when the horizon reaches the "
          "centre of the frame.**",

 "priorities": [
   "⛔ **彼以外の誰も入れないこと。** **ビートの1つめが名指しており、入ればこの1本は `l08` と対でなくなる。** "
   "⚠️ **彼自身は、そのビートのあいだに枠の外へ出る。**",
   "**反射が一度に割れること** — そして**それが切れ目のコマであること。**",
   "**水平線が画面の中央へ来ること。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "⚠️ **水際の線と水平線が、岸の画と同一であること** — **同じ一つの海であることを、"
   "二つの画のあいだで読ませる。**",
   "**日の光だけであること** — **専用の光源も、二つ目の光も無い。**",
   "⚠️ **白波を立てないこと** — **この海は砕けない。**",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `video-spec` を名乗る**——**この形式の禁制（`no uniform pacing`・"
   "`no equal-length beats`・`no static slideshow of stills` ほか）は §16 の床に在り、"
   "**カード自身の `Negative` も §16 の側から届く。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 9.734-second cinematic take (16:9) of the open sea seen from an island's shore at the last of the "
   "day, one clip, one continuous take, one change: **the horizon comes to the centre of the frame and "
   "the water's reflection breaks all at once.** **One person is in this frame, and only in the first "
   "movement: the man who watches this sea walks out of the frame before that movement ends, and he does "
   "not come back into it.**\n\n"
   "**The identity lock of this work, carried here for continuity: "
   "{IDENTITY}** **It is the man who leaves this frame: he is the only one in it, and only for the first "
   "movement, and he is not seen after it.**\n\n"
   "0-2.502s: **the water and the near sand — long low swells with no white water, one path of low sun "
   "lying on the surface — and the man goes out of the frame as the movement runs; by its end there is "
   "nobody in the frame.**\n"
   "2.502-5.996s: **the camera slides left along the surface of the water, and the reflection breaks into "
   "fine facets.**\n"
   "5.996-9.734s: **the horizon comes to the centre of the frame and the swell returns — and the "
   "reflection breaks all at once, and the take ends on that frame.**\n\n"
   "**The camera stays at the surface of the water just off the shingle and never turns back toward the "
   "land; the waterline and the horizon in this frame are the same waterline and the same horizon as in "
   "every shore shot of this work.** **Beyond the waterline there is no land, no sail, no bird and no "
   "other vessel, and the horizon stays level and unbroken.** **This is a bronze-age island before "
   "classical Greece: no made thing of any kind stands in this frame.** **This is a Japanese work.** "
   "No subtitles. No BGM.\n"
   "(One continuous take, one change: the reflection breaks all at once.)"),

 "visual_scene": (
   "The open sea seen from an island's shore at the last of the day, photographed as a film frame: long "
   "low swells with no white water moving steadily in one direction, the surface broken only into small "
   "fine facets; one unbroken horizon across the frame with no land anywhere beyond it; a single path of "
   "warm low light lying on the water; and, at the frame's lower edge, the near sand of the waterline, "
   "dark and coarse, cut across by the water's own line. **In the first movement the man is in the "
   "frame — on the near sand at the frame's lower edge, small and seen from behind, walking out of the "
   "picture — and he is gone before that movement ends; after that no other person is in the frame at any "
   "distance or in any focus, nothing stands on the sand, and no shadow or reflection of a person falls "
   "anywhere in it.** No sail, no bird, no other vessel, no rock in the water."),

 "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones",
   "coarse dark sand cut across by the waterline").replace(
   "warm ochre where the low sun falls",
   "warm ochre held in the single path on the water") + (
   " ⚠️ **The identity block above is this work's continuity lock, and this is the one frame in which "
   "it is also the frame's own contents: the man is in this frame for the first movement and walks out "
   "of it.** ⚠️ **The horizon is level, unbroken and holds its "
   "height for the whole shot**; the water carries no white water, and the light on it is the sun's own "
   "single path."),

 "motion_prompt": (
   "Full animation, not limited. **The long low swells move steadily in one direction and do not break; "
   "they carry no white water.** **The path of low light on the surface breaks into fine facets and then "
   "breaks all at once as the swell returns.** **The near sand does not move** — the only thing moving at "
   "the waterline is the line itself. **The camera slides left at the surface of the water and stops when "
   "the horizon reaches the centre of the frame, and does not move again.** No motion blur smears, no "
   "stutter, no floaty weightless motion, no static frames — **the water moves in every frame of the "
   "take.** **In the first movement the man walks out of the frame across the near sand; he is the only "
   "thing in the frame that is not water, light or sand, and after he has gone nothing else enters.**"),

 "camera_prompt": (
   "Third person, **at the surface of the water just off the shingle**, low enough that the horizon sits "
   "near the frame's centre and the near sand lies at the frame's lower edge. One event only: **a slow "
   "lateral travel left along the surface of the water, which ends when the horizon has come to the "
   "centre of the frame and the reflection breaks all at once.** ⚠️ **The move is motivated by going to "
   "where his gaze goes — and he himself has already left the frame, so the camera follows the gaze and "
   "not the man; the stop is motivated by the horizon's centre.** ⚠️ **The style permits a dolly, "
   "a crane and a Steadicam, and this shot spends the dolly** — a lateral travel at water height with the "
   "low frequency of a rig that has mass. No crane is used and no Steadicam: the travel does not rise and "
   "it does not follow anything. ⚠️ **Do not turn back toward the land and do not move again after the "
   "stop.** No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, no "
   "unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **low swells moving over the water, and water meeting sand at "
   "the waterline.** ⚠️ **There is no human sound in this shot at all** — **he makes no sound as he goes out of the "
   "frame: no voice, no breath, no footfall** — **and no voice of any kind is heard here.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ**"
                        "——⚠️ **この1本で彼が枠に居るのは最初のビートだけである**（`has_man: True`）"
                        "——**ゆえに塊は両方に入る**（§20 を見る）。",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ low swells ＋ water at the waterline ／ no music",
 "unresolved": [
   "✅ **裁定（2026-09-29）: この1本は彼が冒頭に枠に居て、この1本のあいだに去る**（裁定②）——"
   "**`unit.before`（「洞の黒の前に男が居る」）と `unit.after`（「**男は岸に居て、海を見ている。**」）が"
   "彼を枠の側に置き、ビートの1つめが「**彼はもう画面に居ない。**」と書くためである。** "
   "⚠️ **§8 のビート1の逐語は、そのビートの終わりの状態として読む**——**§18 は、裁定②に従って"
   "「彼がそのあいだに枠の外へ出る」と書いた。** "
   "⛔ **ゆえに `has_man: True` のまま、同一性の塊も §18 の両方に残る**——**そして塊は、"
   "去っていく彼の同一性である。** ⚠️ **この仕様は裁定の前、塊を「作品の錠であり枠の中身ではない」と"
   "打ち消していた**——**裁定②がその打ち消しを外した。**",
   "⚠️ **カメラの位置を記録は決めていない。****この仕様は「水際のすぐ沖、水面すれすれ」を採った**"
   "——**彼の位置（岸）から見た画として読むこともできる。** ⚠️ 動機は「彼の視線の先へ行くこと」である。",
   "⚠️ **彼女の声をこの1本に置くかどうかを、記録は何も言わない。****この仕様は置いていない**"
   "——**この1本は海の画であり、呼ぶ声が入れば、それは返事になる。** "
   "⚠️ **置くかどうかは著者が決める。**",
   "⚠️ **水面の道を、彼女の第四の姿（枠の外の背後から来る水面の光）と読む余地がある。**"
   "**この仕様は「日の光」を採った**（`海.states.日没` の逐語が「低い太陽が水面に一本の道を作っている」と"
   "言い、その道は前方から来るからである）。",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **彼以外の誰かが写る。** **遠景の点一つで、この1本は `l08` との対でなくなる。** "
   "禁制は §16 と `Master Prompt` の散文の両方に在る。",
   "**彼が枠に残る。** ⚠️ **最初のビートで出て行かなければ、ビートの1つめの逐語が偽になる**"
   "——**2.502秒より長く枠に居れば、この1本は彼の画になる。**",
   "**水平線が傾く、曲がる、途切れる。** ⚠️ **台帳の逐語:「The horizon is level and unbroken.」**"
   "——**水平線はこの1本の骨である。**",
   "**舟・帆・鳥・陸が入る。** ⚠️ **この海には、彼以外の何も無い。**",
   "**白波が立つ。** ⚠️ **波を低く保てないと、この1本は別の海になる。**",
   "**反射が徐々に割れる。** 一度に割れることが切れ目のコマの内容であり、**徐々に割れれば、"
   "この1本は歌に渡すものを渡していない。**",
   "**「綺麗な海」で終わる。** ⚠️ **美しいだけの海の画は、`l08` と対にならない**"
   "——**この1本は、見ている者が枠の外へ出たあとの海のために在る。**",
 ],
}

if __name__ == "__main__":
    print("s12 content OK — keys:", len(C))
