# -*- coding: utf-8 -*-
"""odyssey-s27 — video-spec — 海 / 夜 / 7.500s. l28「死なない島を出て」の3度目。

The first shot of the final chorus, and the first time the work places labour.
Role 所作 — the third of three roles used for the same line.
"""
import common as K


C = {
 "n": "s27",
 "title": "死なない島を出て——3度目は、手である",
 "duration": "7.500",
 "format": "video-spec",
 "has_man": True,
 "place": "海",
 "time": "夜",
 "segment": "final-chorus-1",

 "band": [
   "『永遠より遠い』 final-chorus「海」 / 所作 / motion —— 3度目は、行為である——彼は漕いでいる",
   "柄が水に入り、引き、抜ける——舟が前に進む。",
   "7.500秒、カメラは舟の後ろから彼の背中を写す——舟が進むのが、切れ目である。",
   "漕ぐことの繰り返しだけであり、着く先は見えない——機構は、この手だけである。",
 ],
 "header": """⚠️ **`l28`「死なない島を出て」の3度目である。** ⛔ **`final-chorus` の1行目である。**
出所は曲の `l28`（240.878–248.378、**7.500秒**であり、**この1本の尺そのものである**）。
⛔ **`s13`（`離脱`）・`s20`（`recognizing-world`）と役を変えた**——
**3度目は、行為である。****彼はもう出発していて、いま漕いでいる。**
⚠️ **3本の役が違うことが、3度の違いの実装である**（**形式の差だけに頼っていない**）。
⚠️ **この1本は `final-chorus` の最初であり、ここから6行が続く。**
⚠️ **`final-chorus` は `chorus-1`・`chorus-2` と言葉が2点だけ違う**
（`なんでもない島へ` が伸び、`まだ着かない` が2行に増える）。**その2点は `s30`・`s31`・`s32` が負う。**
**この1本は、その2点を先取りしない。**
⚠️ **形式は `video-spec`。****この作品のいちばん素の文法で、労働を置く。**
⚠️ **この仕様のショット記録は `shots/odyssey-s27.yaml` である。**""",

 "intent": "**3度目のサビの1行目に、初めて「労働」を置けるか。**"
           "⚠️ **`s13` は意図であり、`s20` は島の応答であり、そしてこの1本は手である。**"
           "**最初のコマでは舟の後ろ姿があり、彼はまだ漕いでいない。**"
           "**最後のコマでは、柄が水に入り、引き、抜け、そして舟が進んでいる**"
           "——⛔ **進むことが、この1本の切れ目のコマである。**"
           "⚠️ **壮絶にしない。****この労働は、力ではなく、繰り返しである。**"
           "**切らない。1本は1つの画である。**",

 "world_concept": K.world_concept(
   "⛔ **この1本から `final-chorus` が始まる**（この区間は 240.878–281.489 であり、"
   "**6行がこの1本のあとに続く**）。"
   "⚠️ **この1本は `海` の19本のうちの1本であり、そしてこの作品で初めて、"
   "「漕ぐこと」が主題になる1本である。**"
   "⛔ **この作品の労働はすべて手である**（記録の `motion.law` の逐語）"
   "——**`s16` の斧、`s17` の針、そしてこの1本の櫂であり、機構は一つも無い。**"
   "⚠️ **`world.rules` の逐語:「この作品は、帰り着かない。」**——**ゆえにこの1本でも、"
   "漕ぐことは進むことであって、着くことではない。**"
   "⚠️ **`unit.before` の逐語:「舟は水の上にあり、島は無い。」**"
   "——⛔ **島はこの1本の枠に無い。****彼はすでに出ていて、いま漕いでいる。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⛔ **この1本に答えは無い。****漕ぐことは、海に何かを求めることではない**"
               "——**柄が水に入り、引き、抜ける。****海は何も返さない。****舟だけが進む。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "**この1本の光は星とその水面の反射だけであり、それは彼女の仕業として書かれない。**"
                "⛔ **この労働を、彼女の助けにしない**——**漕いでいるのは彼であり、手は彼のものである。**",
     "name": "⚠️ **この1本に名は無い。** ⛔ **出て行く島の名も、行き先の名も、歌は言わない**"
             "（逐語:「固有名は、画面にも歌にも一度も現れない。」）。"
             "**「死なない島」は名ではなく、説明である。**",
     "bow": "⚠️ **この1本に弓は無い。** ⚠️ **そして道具は櫂一本だけである**"
            "——**斧は浜にあり、針は布のところにあり、この1本の枠には櫂しか無い。**"
            "**「no steel blade, no iron」**（`斧.negative` の逐語）。",
     "places": "この1本が置くのは `海` である。⚠️ **島は枠に無い**（`unit.before` の逐語:「島は無い。」）。"
               "**陸はどの方向にも見えない**——**`海.geography` の逐語:「no land is visible in any "
               "direction, **including behind**」**。",
     "japanese": "⚠️ **この1本には歌がある**——`l28`「死なない島を出て」であり、**7.500秒である**"
                 "（240.878–248.378）。**歌はポストで載る。****画面の中の声ではない。**",
   },
   extra=[
     "⛔ **記録の `motion.law` の逐語:「この作品の労働はすべて手である」**——`s16` の斧、`s17` の針、"
     "そしてこの1本の櫂。**機構は一つも無い。**"
     "⚠️ **ゆえにこの1本に、滑車も、梃子も、櫂受けも、機械も無い**"
     "（**櫂は船尾に縛られたまま、手で使われる**——`舟.appearance` の逐語:「a steering oar tied at the "
     "stern, lashed, not fitted」）。",
     "⚠️ **この1本の役は `所作` である。** 固有基準は「所作の明瞭さ・変化の一点性・引きの強さ」"
     "（`rolemap.ROLES`）——⛔ **ゆえにこの1本の所作は、一つの動作の反復として読めなければならない。**"
     "**漕ぐという行為が、画面の側から読めることが、この1本の検収である。**",
     "⚠️ **`final-chorus` の2点の言葉の違い（`なんでもない島へ` が伸び、`まだ着かない` が2行に増える）は、"
     "`s30`・`s31`・`s32` が負う**（記録の註の逐語）。**この1本は、その2点を先取りしない。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, photographed as a film frame **from behind the raft**: the stern lies in the near "
     "ground — twenty-odd unseasoned pine logs still barked and uneven, lashed side by side with coarse "
     "hand-twisted cordage, a low platform of hewn planks not fastened flush, **and one oar tied at the "
     "stern with rope, lashed, not fitted, its handle nearest the frame** — and beyond it **one man's "
     "back and arms, and past him black water to a level horizon.** ⚠️ **No land, no sail, no bird, no "
     "other vessel** (逐語, `ledger.locations.海.base`). ⚠️ **No made thing is in this frame except the "
     "raft, the rope, the oar and the one garment he wears.** **No marble, no columns, no architecture of "
     "any later age.**",
   "Color Language":
     "A narrow, graded palette — **the waves are black and the only white in the frame is one broken path "
     "of reflected starlight on the surface and the pale line the oar's blade tears in it.** His wet skin "
     "and the coarse undyed wool are the only things in the frame that are neither water nor light. "
     "⚠️ **The shot has no second light and no warm source**（`海.states.夜` の註の逐語:「光源は星と、"
     "その水面の反射だけである。波は黒く、反射の道だけが白い。」）。⚠️ **The grade is the same in the "
     "first frame and the last.**",
   "Texture":
     "Pine grain and bark under the hand, coarse hand-twisted cordage carrying its uneven twist, hewn "
     "plank ends, and the wet edge where the water comes over; **the wool tunic dark and heavy with water "
     "across his shoulders, wrung and slick where the oar's loom has worked against it**; skin roughened, "
     "marked, salt-stiffened, with the cords of the forearm standing. **The water is long low swells with "
     "no white water**, and **the raft's own wake is the only break on it.** Film grain present and even.",
   "Rendering":
     "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, a gentle flare on the "
     "one reflected path. **Not a photograph's stillness: a film frame, with a real lens's fall-off at the "
     "edges.** No illustration, no CGI look, no cartoon color.",
   "Visual Density": "Low, **and the density is repetition, not objects** — この1本の画は、"
                     "丸太と、縄と、柄と、背中と、腕だけである。⚠️ **ビートの `dense` は、物が多いことでは"
                     "ない。****この1本でいちばん多くが起きているということであり、それは"
                     "「舟が進んだこと」である。**",
   "Time": "`夜` — the night the final chorus begins. ⚠️ **この1本の最初のコマは、`final-chorus` の"
           "最初のコマである**（240.878）——**それより前は、`bridge` の最後の1本（`s26`）が負っている。**",
   "Atmosphere": "The hour in which leaving stops being an intention and becomes something a body does "
                 "— **and it is done slowly, and it is done again.**",
 }),

 "subjects": [
   K.man_subject(
     behavior="⛔ **漕ぐ。****柄が水に入り、引き、抜ける**——**記録の `motion.quality` の逐語であり、"
              "そしてその繰り返しだけがこの1本である。**"
              "⚠️ **動きは小さい。****上体は前へ傾き、そして戻る。****腕が引き、手が柄を握ったままである。**"
              "⚠️ **彼は口を開かず、レンズを見ない。****この1本は彼の背中を写し、顔を写さない。**",
     may="上体の傾き、腕の角度、手の位置、袖の落ち方と濡れ方、そしてうねりに対する体の高さ。",
     extra_notes=[
       "⚠️ **この1本の主題は「漕ぐこと」であって、彼の感情ではない。**"
       "⛔ **壮絶にしない。****力まず、急がず、そして一度も速くならない。**",
       "⚠️ **`s05` が立てた顔の基準から外れない。** ⚠️ **この1本は顔を写さないが、"
       "塊は §18 にまるごと入る**——**ゆえにこの1本も、その顔から外れてはならない。**",
     ]),
   {"name": "海",
    "ref": "**この1本の場所である。** ⚠️ **参照は `ledger.locations.海` の `base`・`geography`・"
           "`states.夜` である。****この1本の海は、`s18` から続く同じ一つの海である。**",
    "appearance": "**長く低いうねりであり、白波を立てない。****水平線は一本で、途切れず、傾かない。** "
                  "**水面に一本の反射の道があり、そして舟の航跡が、この面の唯一の割れ目である**"
                  "（`海.base` の逐語:「the surface broken only by the raft's own wake」）。"
                  "⚠️ **陸は無い。****帆も、鳥も、他の舟も無い。**",
    "behavior": "**うねりが一方向へ進みつづける。****水平線は動かない。****航跡が後ろへ伸びる。** "
                "⚠️ **この1本では、航跡が伸びることが「進んだ」ことの証拠である**"
                "——**海は何も言わない。**",
    "continuity": "**Must preserve** — 水平線の途切れなさと傾きの無さ、白波が無いこと、"
                  "航跡がこの面の唯一の割れ目であること、そして陸・帆・鳥・他の舟が無いこと。"
                  "**May change** — うねりの高さ、航跡の長さと曲がり、反射の道の割れ方。",
    "notes": ["⛔ **この1本の海に島は無い。****記録は「島は無い」と逐語で書く**（`unit.before`）。"
              "⚠️ **参照集合も `岸` を挙げていない**——**ゆえにこの1本の画に、陸は一つも無い。**",
              "⚠️ **`海.base` の逐語:「Long low swells with no white water, moving steadily in one "
              "direction」**——**漕いでも、この海は白波を立てない。****櫂が破るのは、水面だけである。**"]},
 ],

 "environment": {
   "location": "`海` — **舟の後ろから、船尾と彼の背中を見ている。** ⚠️ **陸はどの方向にも見えない**"
               "（`海.geography` の逐語:「no land is visible in any direction, **including behind**」）。"
               "⛔ **ゆえにこの1本の画は、四方が水である。****島はもう見えない。**",
   "elements": "**夜の水面**（長く低いうねり、白波は無い）、**一本の途切れない水平線**、**星**、"
               "**水面の反射の道**、そして**舟の航跡**。 "
               "⚠️ **陸を一つも置かない。****帆も、鳥も、他の舟も置かない**（`海.base` の逐語）。",
   "behavior": "**うねりは同じ向きへ、同じ速さで進みつづける。****舟はうねりに合わせて上下する。** "
               "**航跡が後ろへ伸び、そして少しずつ曲がる**——**彼の漕ぎが、舟の向きをわずかに変えるからである。**"
               "⚠️ **風は弱く、帆は無いので、動くのは水と舟と彼だけである。**",
 },

 "objects": [
   "**漕ぎ手の柄** — ⚠️ **記録の `motion.subject` の逐語:「男の背中、腕、そして漕ぎ手の柄。」**"
   "**この1本のいちばん手前にあるものである。** 柄は木であり、**手で握られ、水を吸って暗い。** "
   "⛔ **櫂は船尾に縛られており、嵌められてはいない**（`舟.appearance` の逐語:「a steering oar tied at "
   "the stern, lashed, not fitted」）。**ゆえにこの1本に、櫂受けも、留め金も、金属も無い。**",
   "**二十数本の、皮の付いた節のある松の丸太**と、**手で縛った粗い縄**、**削った板**"
   "——**この1本の手前の地面である**（`舟.appearance` の逐語）。"
   "⚠️ **この1本では、丸太の縁で水がかぶり、そして彼の体重でわずかに沈む。**",
   "**水面の反射の道と、櫂が破る白い一線** — **この1本で動く光である。**"
   "⚠️ **光源は動かない。****動くのは水面と、櫂の刃である。**",
   "⚠️ **この作品の小道具は4つだけであり**（`ledger.props`——舟・帆・斧・太陽の牛）、"
   "**この1本に来るのは舟だけである。** **帆は張られておらず、斧は浜にあり、"
   "太陽の牛は `s23` の記憶の中にしか居ない。**",
 ],

 "ref_character": "**この1本は `男` の1本である。****そして、この1本に人は彼一人である。**"
                  "⚠️ **彼以外の人を、どの距離にも、どのピントにも置かない**"
                  "（`forbidden_set` の逐語:「no other human being in frame — no companion, no crowd, no "
                  "second person」）。⛔ **女神は現れない**——四つの姿のどれとしても。"
                  "⚠️ **参照集合は `男.identity` と `男.negatives`、そして `海` の3鍵と `舟` の3鍵である**"
                  "——**`s26`・`s28` と同じ8鍵である。****添付は0点である**（裁定②）。",

 "ref_extra": [
   "- ⚠️ **形式カード `video-spec` はこの作品の土台である**——**他の形式はどれも"
   "「`video-spec` に文法を1つ足したもの」である。****ゆえにこの1本は、骨格に何も足さない。**",
   "- ⚠️ **`video-spec` の6つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `SUBJECT`＝the arc — **漕ぐことである。****舟の後ろ姿から始まり、柄が水に入り、引き、抜け、"
   "そして舟が進むところで終わる。**",
   "  - `DURATION`＝clip length (**the model decides the duration**) — ⚠️ **この作品では曲が長さを"
   "決める**（`bible.time_source: song`）。**この1本は `7.500s` であり、`l28` の行の長さそのものである**"
   "——**「4秒より短いから伸ばす」をしない**（`docs/seedance-route.md` の明示の規則）。"
   "⚠️ **カードの括弧書きは、この作品では成り立たない**（§20 の未処理を見る）。",
   "  - `ASPECT`＝aspect ratio — **`16:9` である**（裁定④。**この作品はアスペクトを一つに固定する**）。",
   "  - `BEATS`＝the beat list with second ranges — **上に書いた3つであり、明示的に不等である**"
   "（0–2.002／2.002–5.003／5.003–7.5）。§8 を見る。",
   "  - `CORE`＝the beat that gets the largest share — ⚠️ **第3のビートである**（`5.003-7.5s`、"
   "**2.497秒**）。**もう一度柄が水に入り、そして舟が進む。**"
   "⚠️ **3つは近い長さだが、等分ではない**——**この1本の山は最後の漕ぎであり、"
   "最初の2.002秒は「まだ漕いでいない」ことに払われる。**",
   "  - `HOOK`＝the note the clip ends on — ⛔ **舟が進むことである。****漕ぎの最後の一撃で舟が進み、"
   "そしてそこで切れる**——**説明のビートをそのあとに足さない**（カードの逐語:「End on the note, not "
   "after it.」）。",
   "- ⚠️ **カードの逐語:「Fix physics — weight, inertia, fluidity — so motion has mass」**"
   "——**この1本の物理は §11 に在る。****水の重さが、この1本の手応えである。**",
   "- ⚠️ **この経路（`SEEDANCE 2.5`）では、`Negative Prompt` は床として受け取られない**（`L30`）。"
   "**ゆえにこの1本の禁制は、肯定形で §18 の散文にも書かれている。**",
 ],

 "narrative": {
   "core": "**漕ぐ** — 3度目のサビの1行目に、初めて労働が置かれる。"
           "**そしてそれは、力ではなく、繰り返しである。**",
   "beginning": "**舟の後ろ姿。****まだ漕いでいない。**（記録のビートの逐語）"
                "**柄は手の中にあり、刃は水の上にある。**",
   "turn": "**柄が水に入る。****引き、抜ける。****繰り返す。**",
   "peak": "**もう一度、柄が水に入る。** ⛔ **そして舟が進む。**",
   "pull": "⚠️ **進むことが、切れ目のコマである。****この作品は着かないので、"
           "この1本は進んだところで終わる**——**`final-chorus` の2行目は、この1本のあとに来る。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.497秒.** 最初の2.002秒は**舟の後ろ姿と、まだ漕いでいない"
            "手に払われる**——**この1本でいちばん静かな区間である。** 次の3.001秒で**柄が水に入り、引き、"
            "抜ける**——**繰り返しの区間である。****最後の2.497秒がこの1本の出来事である**"
            "——**もう一度漕ぎ、そして舟が進む。**"
            "⚠️ **形式カードの逐語:「One beat — the core reveal — takes the largest single share (a useful "
            "anchor: ~30% of `DURATION`).」**——**この1本の中心は第3のビートであり、その2.497秒は "
            "7.500秒のうちの約33%である。**"
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**彼が漕いでいないあいだも、海と舟は動いている。**",

 "actions": [
   ("ACT_REST", "舟はうねりの上にあり、彼の手は柄にある。",
    "**舟の後ろ姿。****まだ漕いでいない。****柄は手の中にあり、刃は水の上にある。**"),
   ("ACT_ENTER", "上体がまだ前へ傾いていない。",
    "**柄が水に入る**——**上体が前へ傾き、腕が伸びる。**"),
   ("ACT_PULL", "刃は水の中にある。",
    "**引き、抜ける**——**水の重さが、腕に返る。****舟がわずかに進む。**"),
   ("ACT_AGAIN", "柄は水の外にあり、舟はまだ進みつづけている。",
    "⛔ **もう一度、柄が水に入る。****そして舟が進む**——**進むことが、この1本の切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **behind the raft, low, at the stern** — the frame holds the lashed logs and "
               "the tied oar's handle in the near ground, **his back and arms beyond them**, and the black "
               "water and the level horizon past him. ⚠️ **この1本は彼の背中を写し、顔を写さない**"
               "（記録の `motion.quality` の逐語:「カメラは舟の後ろから、彼の背中を写す。」）。",
   "events": "One event only. `0-7.500s` — **a slow continuous forward travel that keeps pace with the "
             "raft at a rate that does not change, holding the same distance from the stern, still "
             "travelling on the last frame of the take.** ⚠️ **動機は「漕がれている舟について行くこと」で"
             "ある**——**進むことでも、着くことでもない。** ⚠️ **ゆえに船尾は画の中で同じ大きさのままであり、"
             "そして漕ぎのたびに舟がわずかに前へ出る**——**その前へ出ることが、この1本で画面に見える"
             "唯一の「進んだ」の証拠である。** ⚠️ **カメラは一度も彼の前に回らない。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** "
               "— a forward travel at the raft's own height with a real rig's weight, and it does not "
               "wobble. ⚠️ **クレーンもステディカムも使わない**——**この1本は浮きも、回りも、"
               "寄りもしない。****前へだけ、同じ速さで動く。**"
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, and "
               "**no unmotivated move.**",
 },

 "motion": {
   "subject": "⛔ **記録の `motion.subject` の逐語:「男の背中、腕、そして漕ぎ手の柄。」**"
              "**漕ぐ。****柄が水に入り、引き、抜ける。****その繰り返しだけがこの1本である。**"
              "（記録の `motion.quality` の逐語）。",
   "object": "**柄が動く**——**水に入り、引き、抜ける。****櫂は船尾に縛られたまま、手で動かされる**"
             "——**嵌められていないので、支えるのは彼の手と腕である。**"
             "**丸太と縄と板は動かない**（**動くのは、うねりに合わせた舟全体の上下だけである**）。",
   "environment": "**長く低いうねりが、一つの方向へ絶えず動く。****航跡が後ろへ伸び、そして少しずつ曲がる。**"
                  "**星は同じところに留まる。****水平線は動かない。**"
                  "⚠️ **白波を立てない**（`海.base` の逐語:「no white water」）。"
                  "⚠️ **海は彼に反応しない**——**漕いでも、海は何も返さない。**",
   "weight": "⛔ **水は重い。****刃が水に入るとき、柄に重さが返る。****引きは、その重さを押しのける仕事である。**"
             "⚠️ **この1本の重さは、速さに出ない**——**遅さに出る。****速く漕げば、重さが消える。**",
   "inertia": "**舟は、漕いだあとに進みつづける。****次の漕ぎまで、その進みは残る。**"
              "⚠️ **止まるのは、彼が漕ぐのをやめたときだけである**——**そしてこの1本では、"
              "彼は一度もやめない。** ⚠️ **水は、柄を離れたあとも波を返す。**",
   "acceleration": "**加速しない。****漕ぎの速さも、舟の進みも、この7.500秒のあいだ一定である。**"
                   "⛔ **ゆえに水平線は近くならない**——**速く漕げば、この1本は「着く」と言うことになる。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この7.500秒に、止まったフレームは"
               "一つも無い**——**漕いでいないあいだも、海と舟とカメラが動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**刃が水に入ることは、打撃ではない。**"
             "**そしてこの1本の音は、その一度ごとに同じである。**",
 },

 "emotion": {
   "arc": "**労働。****それは力ではなく、繰り返しである。**"
          "⚠️ **この1本の感情は、彼の内面ではない**——**手と、柄と、水のあいだにある。**"
          "⛔ **壮絶にしない。****英雄的にしない。****この作品は、漕ぐことを、漕ぐこととして置く。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****柄が水に入り、引き、抜け、"
   "そして舟が進むことである。** ⚠️ **この作品は、それに名を与えない**"
   "——**労働という語も、意味づけも、画面には無い。**",
 },

 "lighting": {
   "base": "The stars and their reflection on the water — **and nothing else.** ⚠️ **この1本の光源は一つであり、"
           "それは星である**（`海.states.夜` の註の逐語）。⚠️ **月も、火も、灯も出さない。**"
           "⚠️ **彼を別に照らさない**——**彼の背中の光は、水面の反射の道そのものである。**"
           "⚠️ **彼女の第四の姿（枠の外の背後から来る水面の光）を、この1本に置かない**"
           "——**この1本の光は星であり、そしてそのことは彼女の仕業として書かれない。**",
   "events": "**One, and it runs the whole shot.** **星を受けた一本の道が、動く水面の上で細かく割れては戻り、"
             "そして櫂がその中を破る**（0秒から 7.500秒まで）。"
             "⚠️ **光源は動かない**——**様式カードの逐語:「The grade holds for the whole shot — a colour "
             "temperature that swings is a different style.」** ⛔ **そしてこの1本では、光が増えない。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE + " ⛔ **この1本は `所作` の1本であり、語るのは歌である**（`l28`）。"
             "**画面の中に声は一つも無い。**",
   "sfx": "⛔ **この1本の音は、漕ぐ音である。****刃が水に入る音、引きのあいだ水が柄を伝う音、"
          "そして抜けるときの一滴の音。****縄が荷を受けて低く鳴る。**"
          "⚠️ **この1本に人の声は一つも無い**——**息遣いも、掛け声も、唸りも無い**"
          "（**それは英雄の音であり、この作品には無い**）。"
          "⚠️ **白波の音は無い**——**この海は白波を立てない**（`海.base` の逐語:「no white water」）。",
   "music": K.NO_MUSIC + " ⚠️ **この1本のあいだ、主題歌は `final-chorus` に入っている**（`l28`）"
            "——**が、この1本の中には無い。****編集で載る。**"
            "**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜の外海。**水、木、縄、そして弱い風。** ⚠️ **鳥の声も、帆の音も、他の船の音も無い**"
                  "——**この海には、彼の筏しか無い。** ⚠️ **呼ぶ声も、歌う声も無い。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="**この1本は彼の背中と腕を写す**——**ゆえに塊のうち、体格・髪・着ている一枚・"
                "裸足であることが、この1本で読める。**"
                "⛔ **顔は写さないが、塊は §18 にまるごと入る。****ゆえにこの1本も、"
                "`s05` が立てた顔から外れてはならない。**",
     may="上体の傾き、腕の角度、手の位置、袖の落ち方と濡れ方、髪の乱れ、"
         "そしてうねりに対する体の高さ。"),
   "spatial": "**舟の後ろ、船尾のすぐ後ろに、低くカメラがある。****手前の地面は、縛られた丸太と縄である。** "
              "**彼はその向こうに、前を向いて座している。**"
              "⚠️ **陸はどの方向にも見えない。****後ろにも見えない**（`海.geography` の逐語）"
              "——⛔ **ゆえにこの1本の画は、四方が水である。**",
   "temporal": "夜である。⛔ **この1本は `final-chorus` の最初のコマである**"
               "——**`bridge` の最後の1本（`s26`）のあとに来る。**"
               "⚠️ **`s13`（`chorus-1`）・`s20`（`chorus-2`）と同じ行である**"
               "——**時は三度目であるが、画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は星とその反射だけである。**"
             "⚠️ **この1本は `video-spec` を名乗り、この形式は §15 から何も免除しない**"
             "——**免除を名乗るのは `coexisting-realities` を名乗る4本だけである。**",
   "motion": "Full animation, not limited. **彼の上体と腕が動き、柄が動き、舟が動き、うねりが動く。** "
             "⚠️ **カメラは1回だけ動き、切れ目のコマでもまだ動いている。**",
   "sound": "水、木、縄、そして櫂の刃。**音楽なし。言葉なし。** ⚠️ **掛け声も、息遣いも無い。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**この1本には彼が居る**——**ゆえに女神の禁制は、他人の形で来る。**"
     "⛔ **この労働を彼女の助けにしない。****水面の光を、この1本の後ろから来させない。**")) + [
   "⛔ **No island, no land, no shore, no coast, no headland, and no wake line that leads back to one** "
   "— **この1本は、島を出たあとの1本である**（逐語, `unit.before`: `舟は水の上にあり、島は無い。`）。"
   "⚠️ **水際の線も、砂も、岸の光も入れない。**",
   "⛔ **No second person in frame at any distance and in any focus** — no companion, no crowd, no figure "
   "on the water, **and no one on the raft with him**"
   "（逐語, `forbidden_set`: `no other human being in frame — no companion, no crowd, no second person`）。",
   "⛔ **No mechanism for the oar** — **no oarlock, no rowlock, no thole pin, no crutch, no pivot, no "
   "lever, no pulley, no fitting of any kind; no metal fastenings and no nails; no rope that is not "
   "hand-twisted**（逐語, `ledger.props.舟.negative`）。"
   "**櫂は船尾に縛られ、手と腕が支える。****この作品の労働はすべて手である。**",
   "**No second oar and no pair of oars** — **この1本に櫂は一本だけである**"
   "（逐語, `舟.appearance`: `a steering oar tied at the stern`）。",
   "**The raft stays a raft** — no boat, no ship, no hull, **no keel, no ribs, no planking, no rudder, "
   "no wheel, no helm, and nothing fitted flush**（逐語, `舟.negative`）。",
   "**No sail set on the raft in this frame and no mast step in use** — **この1本の参照集合は `帆` を"
   "挙げていない**（逐語, `海.base` の `no sail`）。",
   "**No land, no bird and no other vessel visible in any direction, including behind** "
   "(逐語, `海.base` と `海.geography`)。",
   "**No white water, no breaking crest, no spray and no foam** — **漕いでも、この海は砕けない**"
   "（逐語, `海.base` の `no white water`）。",
   "⚠️ **No heroic treatment of the work** — **no straining, no grimace, no thrown-back head, no "
   "shout, no sweat-spray caught in light, no muscular display, and no heroic lighting on the arms.**"
   "**この1本の労働は、力ではなく、繰り返しである。**",
   "⚠️ **No sound of exertion** — no breath, no grunt and no shout: **掛け声は英雄の音である。**",
   "⚠️ **No glamour shot of the sea** — no golden light, no spectacle, no swelling grandeur: "
   "**壮大にすれば、この1本は労働でなくなる。**",
   "⛔ **His face does not turn to the frame** — **この1本は彼の背中を写す**"
   "（記録の逐語:「カメラは舟の後ろから、彼の背中を写す。」）。"
   "⚠️ **振り向けば、この1本は別の1本になり、そして同一性の守りが弱くなる。**",
 ],
 "must": [
   "⛔ **漕ぐこと** — **柄が水に入り、引き、抜ける。****そして繰り返す**"
   "（記録の `motion.quality` の逐語）。",
   "⛔ **舟が進むこと** — **この1本の切れ目のコマである**（記録のビートの逐語）。"
   "**進むことの証拠は、航跡と、画の中の舟の前への出である。**",
   "**彼の背中と、腕と、漕ぎ手の柄が枠にあること** — **記録の `motion.subject` の逐語である。**",
   "⛔ **労働を、力ではなく繰り返しとして置くこと** — **この1本の狙いである**"
   "（記録の `aim` の逐語:「3度目のサビの1行目に、初めて『労働』を置けるか。」）。",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.**",
   "⛔ **切らない。** **1本は1つの画である。****カメラは1回だけ動く。**",
   "⛔ **島を写さないこと** — **彼はもう出ている**（逐語, `unit.before`）。",
   "⛔ **機構を一つも入れないこと** — **櫂は縛られており、嵌められていない。**"
   "**支えるのは手と腕である。**",
   "**カメラは舟について行くこと** — **同じ距離を保ち、漕ぎのたびに前へ出る分だけが画に見える。**",
   "**光は星と、その水面の反射だけであること** — 月も、火も、夜明けの光も無い。",
   "⚠️ **`video-spec` の6つを満たすこと** — `SUBJECT`・`DURATION`・`ASPECT`・`BEATS`・`CORE`・`HOOK`"
   "（§8）。**`HOOK` は「舟が進むこと」である。**",
 ],
 "prefer": "The stroke read clearly as one action repeated — enter, pull, come out, and the raft's own "
           "surge on each one; **the handle in the near ground and his back beyond it**; the wet wool "
           "across the shoulders and the slick the loom has worked into it; the black carried without "
           "detail; **the wake the only break on the surface, lengthening and bending very slightly.**",
 "allow": "The raft moving under him more than he moves; the swell lifting the whole frame; a gentle flare "
          "on the one reflected path; the pale line the blade tears in the water; **a forward travel that "
          "holds its distance and never stops.**",

 "priorities": [
   "⛔ **漕ぐことが読めること** — **この1本の役（`所作`）の固有基準である**"
   "（逐語, `rolemap.ROLES`: 「所作の明瞭さ・変化の一点性・引きの強さ」）。"
   "**漕ぎが読めなければ、この1本は何も言っていない。**",
   "⛔ **機構を入れないこと** — **櫂受け一つで、この作品の労働は手でなくなる。**",
   "⛔ **壮絶にしないこと** — **力、唸り、英雄的な光は、この1本を別の作品にする。**",
   "⛔ **島を写さないこと** — **彼はもう出ている。**",
   "⛔ **顔を枠に向けないこと** — **背中を写す1本である。**",
   "⚠️ **舟が前へ出ることを、画の中で見えるようにすること** — **進んだことの唯一の証拠である。**",
   "⚠️ **速くしないこと** — **速く漕げば、この1本は「着く」と言うことになる。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "**光は星とその反射だけであること** — 月も、火も、夜明けの光も無い。",
   "⚠️ **`video-spec` の6つを満たすこと** — `SUBJECT`・`DURATION`・`ASPECT`・`BEATS`・`CORE`・`HOOK`。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `video-spec` を名乗る。****カード自身の禁制（`no uniform pacing`・"
   "`no equal-length beats`・`no static slideshow of stills`・`no floaty weightless motion`・"
   "`no scene cuts to unrelated locations` ほか）は §16 の側から届く**"
   "——**ここには書かない。** **ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"
   "⛔ **そしてこの経路では、その `Negative Prompt` は床として受け取られない**（`L30`）"
   "——**ゆえにこの1本の禁制は、肯定形で §18 の散文にも書かれている。**"),

 "master": (
   "A 7.500-second cinematic take (16:9) of open sea at night, seen from behind the raft, one clip, one "
   "continuous take, one change: **the oar goes into the water, is pulled, and comes out, again, and the "
   "raft moves forward.** At the first frame the raft has not yet begun to be rowed; at the last the "
   "raft is moving forward on the stroke and the take ends there.\n\n"
   "0-2.002s: **the raft's stern from behind, and his back** — the tied oar's handle in his hands and its "
   "blade above the water. **He has not begun to row.**\n"
   "2.002-5.003s: **the oar goes into the water, is pulled, and comes out** — his upper body leans "
   "forward and comes back, and the raft gains a little each time. **The stroke repeats.**\n"
   "5.003-7.500s: **the oar goes into the water again, is pulled, and comes out** — and **the raft moves "
   "forward, and the take ends on that.**\n\n"
   "{IDENTITY}\n\n"
   "**He is the only person in this frame at any distance and in any focus** — no second person, no one "
   "on the raft with him and no one on the water. **No land, no island, no shore, no coastline, no sail, "
   "no bird and no other vessel is visible in any direction, including behind.** **He rows with one oar "
   "only, and that oar is tied at the stern with hand-twisted rope, lashed and not fitted: there is no "
   "oarlock, no rowlock, no pivot, no lever, no metal fastening and no nail.** **The raft is a raft: logs "
   "lashed side by side with hand-twisted cordage, no keel, no planking, no rudder, and no sail set on "
   "it.** **The light is the stars and their one broken path on the water, and there is no other source: "
   "no moon, no fire, no lamp and no dawn.** **His face is not turned to the frame and he does not "
   "speak.** **No blood, no wound and no corpse.** **This is a bronze-age sea before classical Greece.** "
   "**This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the stroke is repeated, and the raft moves forward.)"),

 "visual_scene": (
   "Open sea at night, photographed as a film frame from behind the raft: **the stern lies in the near "
   "ground** — twenty-odd unseasoned pine logs still barked and uneven, lashed side by side with coarse "
   "hand-twisted cordage, a low platform of hewn planks laid across them and not fastened flush, the "
   "water coming over the logs' edge — **and one oar tied at the stern with hand-twisted rope, lashed, "
   "not fitted, its wooden handle nearest the frame and its blade above the water.** Beyond the stern, "
   "**one man sits facing away with his back and both arms to the frame, his face not visible**: a broad "
   "back in a coarse undyed wool tunic, dark and heavy with water and worn through at the shoulder seam, "
   "wet dark hair hanging below the ears, bare forearms and bare feet braced against the logs. Past him "
   "the water is black and long-swelled with no white water, the raft's own wake the only break on it, "
   "and the horizon is level and unbroken with the stars above it. **There is no land in any direction, "
   "including behind; no sail, no bird, no other vessel, and no second person anywhere in the frame.**"),

 "visual_meta": (
   "Anamorphic lens with subtle oval bokeh and a gentle flare on the one reflected path; a moderate "
   "depth of field; **a graded palette that is almost one value — black water, a sky a shade above it, "
   "and one white broken path of reflected starlight, with the pale line the blade tears in the water.** "
   "Barked pine logs and coarse hand-twisted cordage in the near ground, wet along the edge; coarse "
   "undyed wool with visible fibre, dark and heavy with water across the shoulders, worn through at the "
   "shoulder seam; skin roughened and marked, salt-stiffened, with the cords of the forearm standing; "
   "even film grain over everything. No painterly stroke, no airbrush, no plastic surface, no CGI look, "
   "no illustration. ⚠️ **The frame is dark and almost empty by design** — the sea is black, the stars "
   "stand above it, and the only bright things in it are the one broken reflected path and the thin "
   "pale line the oar's blade tears."),

 "motion_prompt": (
   "Full animation, not limited, one continuous take with no cut. **The stroke, repeated — enter, pull, "
   "come out — and the raft gaining a little on each one.** **The blade enters the water with weight, "
   "the pull has the water's resistance in it, and the blade comes out trailing; his upper body leans "
   "forward and comes back and his shoulders carry the load, so the work reads as weight and not as "
   "gesture.** **The oar is tied at the stern and not fitted, so his hands and arms are what hold it, "
   "and the loom works against the wet wool across his shoulders.** **He never strains, never speeds up "
   "and never shouts; the rate is the same in the first stroke and the last.** **The raft rides the long "
   "low swell the whole time; the wake lengthens behind it and bends very slightly, and it is the only "
   "break on the surface — there is no spray and no breaking crest anywhere in the frame.** **The camera "
   "travels forward at the raft's own rate the whole time and holds its distance.** **His face is not "
   "turned to the frame at any point, and he never looks back.** No motion blur smears, no stutter, no "
   "floaty weightless motion, no static frames — **the water and the oar move in every frame of the "
   "take.**"),

 "camera_prompt": (
   "Third person, **behind the raft, low, at the stern** — the frame holds the lashed logs and the tied "
   "oar's handle in the near ground, his back and arms beyond them, and the black water and the level "
   "horizon past him. One event only: **a slow continuous forward travel that keeps pace with the raft "
   "at a rate that does not change, holding the same distance from the stern, still travelling on the "
   "last frame of the take.** ⚠️ **The move is motivated by following the raft being rowed — not by "
   "approaching him and not by arriving anywhere.** ⚠️ **The style permits a dolly, a crane and a "
   "Steadicam, and this shot spends the dolly** — a forward travel at the raft's own height, with the "
   "low frequency of a rig that has mass. ⚠️ **No crane is used and no Steadicam is needed** — this "
   "frame travels forward only, and it never rises, never turns and never comes round in front of him. "
   "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, no unmotivated "
   "move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **the blade going into the water, water running along the loom "
   "through the pull, the blade coming out, and the low creak of hand-twisted cordage taking the load "
   "each time.** ⚠️ **There is no human sound in this shot at all** — no breath, no grunt, no shout and "
   "no voice, **because the work is repetition and not exertion.** ⚠️ **The sound is the same on every "
   "stroke**, and **no sound marks the raft's advance** — the water does not change its note. "
   "⚠️ **No white water and no spray are heard; this sea does not break.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②）。"
                        "⚠️ **この1本は人物を持つので、同一性の塊が §18 の `Master Prompt` と "
                        "`Visual Prompt` の両方に逐語で貼られている**——**要約しない。**"
                        "⚠️ **参照集合は `男.identity`・`男.negatives`・`海`・`海.geography`・`海.states.夜`・"
                        "`舟`・`舟.appearance`・`舟.negative` の8鍵である**——**`s26`・`s28` と同じ8鍵である。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ the stroke and the water ／ no music",
 "unresolved": [
   "⚠️ **この1本の櫂が、台帳のどの櫂であるかを、記録は書いていない。**"
   "⚠️ **`舟.appearance` は櫂を一本だけ挙げる**（逐語:「a steering oar tied at the stern, lashed, not "
   "fitted」）——**舵として縛られた櫂である。****この仕様は、その一本を漕ぎに使うと読んだ**"
   "（記録の `motion.subject` の逐語:「そして漕ぎ手の柄」）。"
   "⛔ **ゆえにこの1本に、二本目の櫂も、櫂受けも無い。**"
   "**この読みが正しいかは著者が決める**——**別の櫂を足せば、`舟.negative` の"
   "「no metal fastenings, no nails」と、そして「労働はすべて手である」という一行に触れる。**",
   "⚠️ **カメラの位置と、彼の体の向きを、記録は細かくは決めていない。****この仕様は"
   "「船尾の後ろから、前を向いた背中」を採った**——**記録の逐語:「カメラは舟の後ろから、"
   "彼の背中を写す。」** ⚠️ **彼が立っているか、座しているかを、記録は言わない。**"
   "**この仕様は「座している」とした**——**筏は低く、立って漕ぐには狭いからである。**"
   "**どちらが正かは、絵を見て著者が決める。**",
   "⛔ **`s13` の註は「この作品は3本とも役を同じにした——差分は §6 の形式が持つ」と書き、"
   "この1本の記録は「`s13`・`s20` と役を変えた」と書く。****記録のうち、この2つは食い違っている。**"
   "⚠️ **この仕様は、この1本の側の記録（役を変えた）に従った**——"
   "**役は `所作` であり、`s13`・`s20` の `離脱` とは違う。**"
   "**どちらが正かは著者が決める**（**この食い違いは、この仕様の外にある。**）",
   "⛔ **「労働」を、機械は測れない。****測れるのは「漕ぎが反復されていること」と"
   "「舟が前へ出ていること」までである。**"
   "**その先（それが労働として読めるか）は、絵を見て著者が決める。**",
   "⚠️ **この1本で帆を張るかどうかを、記録は書いていない。**"
   "**この仕様は「張られていない」と読んだ**——**彼が漕ぐ1本だからである**"
   "（**帆が張られていれば、この1本の労働は別の意味になる**）。"
   "⚠️ **この1本の参照集合は `帆` を挙げていない。**",
   "⚠️ **`video-spec` の `DURATION` の括弧書き。** カードは逐語で「the model decides the duration」と"
   "言うが、**この作品では曲が長さを決める**（`bible.time_source: song`）。"
   "**この仕様は曲の側を採った**——**§1 の `Duration` は記録の逐語である**（`L23`）。",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **機構が入る（櫂受け・留め金・梃子）。** ⚠️ **この1本のいちばん高い危険である**"
   "——**この経路は「漕ぐ」を櫂受けと櫂の機構として描く。****この作品の労働はすべて手である。**",
   "⛔ **壮絶になる。** ⚠️ **唸り、力を込めた腕、投げ出された光**——**英雄の労働である。**"
   "**この1本は、繰り返しの労働である。**",
   "⛔ **島が写る。** ⚠️ **`s13` の海は島を写してきたので、この経路は島を残しやすい**"
   "——**この1本は島を出たあとの1本である。**",
   "⛔ **舟が舟になる（竜骨・板張り・舵輪）。** ⚠️ **台帳の逐語:「A raft, not a boat.」**",
   "**顔が枠に向く。** ⚠️ **振り向けば、この1本は別の1本になり、そして同一性の守りが弱くなる**"
   "——**参照画像が1枚も無いので、守る道具は英文だけである。**",
   "**漕ぎが読めない。** ⚠️ **所作の明瞭さが失われれば、この1本は何も言っていない。**",
   "**速くなる。** ⚠️ **速く漕げば、この1本は「着く」と言うことになる。**",
   "**白波が立つ、砕ける。** ⚠️ **この海は白波を立てない**（逐語:「no white water」）。",
   "**二本目の櫂が入る。** ⚠️ **台帳が挙げる櫂は一本だけである。**",
   "**帆が張られる。** ⚠️ **この1本は漕ぐ1本であり、帆の1本ではない。**",
   "**掛け声・息遣いが入る。** ⚠️ **それは英雄の音であり、この作品には無い。**",
 ],
}

if __name__ == "__main__":
    print("s27 content OK — keys:", len(C))
