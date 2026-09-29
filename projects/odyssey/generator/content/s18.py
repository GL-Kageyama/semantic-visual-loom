# -*- coding: utf-8 -*-
"""odyssey-s18 — video-spec — 海 / 夜明け / 7.101s. The man is on the water for the first time."""
import common as K


C = {
 "n": "s18",
 "title": "星を数えて舵を取る——この作品で初めて、彼は水の上に居る",
 "duration": "7.101",
 "format": "video-spec",
 "has_man": True,
 "segment": "verse-2-3",

 "band": [
   "『永遠より遠い』 verse-2「海」 / 所作 / motion —— 星を数えて舵を取る——この作品で初めて、彼は水の上に居る",
   "暗い海の上で、男が星を見て舵を動かし、舟が向きを変える。",
   "7.101秒、カメラは彼の肩越しに空へ上がっていく——星が動かないのが、切れ目である。",
   "舵輪は無く、縛られた一本の櫂だけが舵である——それ以外の機構は、この作品に一つも無い。",
 ],
 "header": """⛔ **この作品で初めて、男が水の上に居る。** 出所は曲の `l16`「星を数えて舵を取る」。
⚠️ **`verse-2` は夜明けである。** ただし——**夜明けでも、星はまだ出ている。****この1本の空は、まだ夜の空である。**
⛔ **この読みが、`s19` の設計を決めている**（あちらの註を見る）——**夜明けに星が残っているから、「沈まない」が言える。**
⚠️ **形式は `video-spec`。** ⚠️ **`s16`・`s17` と連続して `transformation` を使わなかった**——**`s16`（17.234秒）と `s17`（6.543秒）の変身のあとに、素の画を置く。****文法を戻すことで、変身が終わったことが分かる。**
⚠️ **この1本は、この作品で2本しかない `夜明け` の海である**（`ledger.locations.海.states.夜明け`——**この場所の状態のうち、これが最後のものである**）。
⚠️ **切れ間は `l16` の歌い終わりである**（161.809–168.910。**行の長さが、そのままこの1本の長さである**）。
⚠️ **この仕様のショット記録は `shots/odyssey-s18.yaml` である。**""",

 "intent": "**「数える」を、数を言わずに写せるか。** そして**夜明けの海を、暗い画として立てられるか。** "
           "⚠️ **この1本は、彼が初めて水の上に居る1本である**——**それでも、壮大な画にしない。**"
           "**見えているのは、暗い海と、残っている星と、彼の手である。** "
           "⛔ **切らない。1本は1つの画である。** ⚠️ **変化は切れ目のコマで終わる**——"
           "**舟が向きを変え、そして星が動かない。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本が置くのは `海` である**——**この作品の6つの場所のうち、いちばん多く写る場所である**"
   "（`roster.json` の実測——**34本のうち19本**。⚠️ **`海` が最初に出るのは `s03` である**）。"
   "`s01` から `s15` まで、海は彼から見えていた。**この1本で、彼はその上に居る。**"
   "⛔ **実測: その19本のうち、彼がその上に居る最初の1本が、この1本である**"
   "（記録の逐語:「**この作品で初めて、男が水の上に居る。**」）。"
   "⚠️ **変身のあとの、素の画である**（`s16` と `s17` が2本続けて形を変えた）。**文法を戻すことで、変身が終わったことが分かる。**"),

 "world_rules": K.world_rules(
   drop=(), tails={
     "answer": "⚠️ **この1本には彼が居る。****それでも返事は無い**——**星は数を返さないし、海は答えない。**"
               "**彼が動かすのは舵だけであり、動くのは舟だけである。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "**この1本の空に星はあるが、星の道はまだ与えられていない**——"
                "**この1本で彼がしているのは、与えられた道を辿ることではなく、数えることである。**",
     "name": "⚠️ **この1本に名は無い。** 星にも、舟にも、彼にも、**どこにも書かれないし、呼ばれない。**"
             "⚠️ **この1本は数えるが、数を言わない**——**数えることは、名指すことではない。**",
     "bow": "⚠️ **この1本に弓は無い。** 彼の手にあるのは**縛られた舵の櫂**だけである。"
            "⚠️ **斧は浜に残っている**——**この1本に道具は無い。**",
     "places": "この1本が置くのは `海` である——**この作品の6つの場所のうち、いちばん多く写る場所である**"
               "（`roster.json` の実測——**34本のうち19本**）。"
               "⚠️ **この1本で初めて、彼は水の上に居る。**"
               "**島は見えない**（`ledger.locations.海.base` の逐語:「**No land**」）。",
     "japanese": "⚠️ **この1本には歌がある**——`l16`「星を数えて舵を取る」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⚠️ **この場所の逐語が、この1本の禁制である**（`ledger.locations.海.base`）——"
     "「**No land, no sail, no bird, no other vessel.**」"
     "**ゆえにこの1本にも、他の船も、帆も、鳥も、陸も無い。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at dawn, photographed as a film frame, seen from the raft itself. **Forty-odd unseasoned "
     "pine logs lashed side by side with coarse hand-twisted cordage, still barked and uneven; a low "
     "platform of hewn planks laid across them and not fastened flush; a steering oar tied at the stern, "
     "lashed, not fitted; a short mast of a trimmed pine trunk, stayed with rope, with nothing set on "
     "it.** ⚠️ **No land, no sail, no bird, no other vessel** (逐語, `ledger.locations.海.base`).",
   "Color Language":
     "A narrow, graded palette — **the sea is still dark and the sky has only begun to go from blue to "
     "grey-white**, so the frame is almost one value with the stars standing in it. "
     "⚠️ **The reflected starlight is the only bright thing on the water**, and the water is black "
     "around it. ⚠️ **Nothing is lit apart from the place** — **one light only, and it is the sky's; the "
     "shot has no second light.**",
   "Texture":
     "The raft under the frame: pine grain and bark, coarse hand-twisted cordage with its uneven twist, "
     "hewn plank ends, wet wood along the edges where the water comes over. **The water is long low "
     "swells with no white water**, moving steadily in one direction, the surface broken only by the "
     "raft's own wake. ⚠️ **No spray, no breaking crest anywhere in this frame.** Skin and coarse wool "
     "where the man is. Film grain present and even.",
   "Rendering":
     "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, a gentle flare on "
     "the one reflected path of light. **Not a photograph's stillness: a film frame.** No illustration, "
     "no CGI look, no cartoon color.",
   "Visual Density": "Low. **The frame is dark and almost empty by design** — the raft at the bottom, "
                     "the man low in the frame, the stars above, and **nothing else at any depth.** "
                     "⚠️ **空が空くのは、この1本の内容ではなく、この1本の条件である。**",
   "Time": "`夜明け` — the thirty minutes when the sky goes from blue to grey-white. **The sea is still "
           "dark and the stars are still out**; they go out one by one. **The work does not fix a date.**",
   "Atmosphere": "The half hour when a person can still steer by what is left in the sky.",
 }),

 "subjects": [
   K.man_subject(
     behavior="**彼は舟尾に立ち、左手を縛られた舵の櫂に置いている。**⚠️ **舵輪ではない**——"
              "**縛られた一本の櫂である**（`props.舟.appearance` の逐語:「**a steering oar tied at the "
              "stern, lashed, not fitted**」）。**彼は空を見上げ、それから櫂を動かす。**"
              "⚠️ **動きは小さい。****急がない。** ⚠️ **彼は口を開かず、レンズを見ない。**",
     may="左手の位置、見上げる角度、上体の傾き、袖の落ち方、そして足の下の丸太が動くこと。",
     extra_notes=[
       "⛔ **この作品で初めて、男が水の上に居る。** ⚠️ **それでも、この1本は彼の画ではない**——"
       "**彼は低く、小さく、そしてカメラは彼の肩越しに空へ上がっていく。**",
       "⚠️ **この1本は数を言わない。****彼は数えているが、数を口にしない**——"
       "**数を言えば、この1本は説明になる。**",
       "⚠️ **`s05` が立てた顔の基準から外れない。** ⚠️ **この1本は顔の大写しを持たない**——"
       "**それでも英文の塊は §18 にまるごと入る。**",
     ]),
   {"name": "舟",
    "ref": "**この1本の場所であり、彼が乗っているものである。** ⚠️ **参照は `props.舟` の `appearance` と "
           "`negative` である**——**この作品に参照画像は無い**（裁定②）。",
    "appearance": "**筏であって、船ではない。**二十数本の未乾燥の松の丸太を、粗く手で撚った縄で"
                  "横に並べて縛ってある。**丸太は樹皮がついたままで、不揃いである。**"
                  "粗削りの板を載せた低い平台があり、**板は突き付けられていない。**"
                  "**竜骨も、肋も、張り板も、マスト座も、舵も無い**——**船尾に縛られた一本の舵の櫂がある。**"
                  "**刈り込んだ松の幹の短いマストが、縄で支えてある**——**そこには何も張られていない。**"
                  "**だいたい人の1.5倍の長さで、低く、縁は水をかぶっている。**"
                  "**すべてが間に合わせで、どこも対称でない。**",
    "behavior": "**舟はうねりに合わせて上下する。**⚠️ **自分の意思では動かない**——"
                "**動かすのは、海と、彼の左手とである。** ⚠️ **そしてこの1本の終わりに、向きを変える。**",
    "continuity": "**Must preserve** — 丸太の数と不揃いさ、手で撚った縄、樹皮、低い平台、"
                  "**突き付けられていない板**、**船尾に縛られた舵の櫂**、"
                  "**そして竜骨も肋も張り板も舵輪も無いこと**。"
                  "**May change** — うねりに対する角度、平台の上の彼の位置、航跡の長さ、"
                  "そして**この1本の最後に、向き。**",
    "notes": ["⛔ **`props.舟.negative` の1行目が、この1本でも効く**——"
              "「**no boat, no ship, no hull, no keel, no planking**」。**筏を船にしない。**",
              "⚠️ **舵輪を描かない。** 「舵を取る」という語が、この経路を舵輪へ引き寄せる——"
              "**機構の可読性が、この様式の物理である**（`motion.law` の逐語）。",
              "⚠️ **帆を張らない。** 参照集合が挙げているのは `舟` であり、`帆` ではない——"
              "**この1本の空には、まだ何も張られていない。**"]},
 ],

 "environment": {
   "location": "`海` — **この作品の6つの場所のうち、いちばん多く写る場所である**"
               "（`roster.json` の実測——**34本のうち19本**）。"
               "**陸はどの方向にも見えない**（`ledger.locations.海.geography` の逐語:「**no land is "
               "visible in any direction, including behind**」）。"
               "⚠️ **カメラは舟の上にあり、舟は水の上にある。**",
   "elements": "**長く低いうねり**（白波の無いもの）、**一つの方向へ絶えず動いている水面**、"
               "**舟の航跡だけがその面を破っている**、流れてくる海藻、"
               "**そして舟そのもの**——丸太、縄、板、舵の櫂、**何も張られていない短いマスト**。"
               "⚠️ **他の船も、帆も、鳥も、陸も無い。**",
   "behavior": "**うねりは同じ方向へ、同じ速さで動き続ける。**舟はそれに合わせて上下し、"
               "**航跡だけが後ろへ伸びる。** ⚠️ **星は動かない**——"
               "**空が明るくなっても、星の位置は変わらない。**"
               "⚠️ **海は彼に反応しない**——**彼が舵を動かしても、うねりの向きは変わらない。**",
 },

 "objects": [
   "**舟** — **この1本の地面である。**丸太、手で撚った縄、粗削りの板、そして**船尾に縛られた舵の櫂**。"
   "⚠️ **竜骨も、肋も、張り板も、舵輪も無い。**",
   "**舵の櫂** — **この1本で彼が触る唯一の物である。****船尾に縛られ、据え付けられていない。**"
   "⚠️ **この1本の終わりに、彼の左手がこれを動かし、舟が向きを変える。**",
   "**短いマスト** — 刈り込んだ松の幹であり、縄で支えてある。⚠️ **この1本には、何も張られていない。**",
   "**星** — 空にまだ出ている。⚠️ **この1本はどれも名指さず、形として読まない**"
   "——**名指すのは `s19` の仕事である。**",
   "**航跡** — 舟の後ろへ伸びる。⚠️ **この面を破るものは、航跡と、流れてくる海藻だけである**"
   "（`ledger.locations.海.base` の逐語:「the surface broken only by the raft's own wake and by weed passing」）。",
   "⚠️ **この作品の小道具4つのうち、この1本に来るのは舟だけである**（`ledger.props`）——"
   "**帆は浜で縫われたままである。** 斧は浜に残り、太陽の牛はまだ記憶にすら無い。",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — **この1本には添付しない。彼女はこの1本に、四つの姿のどれとしても現れない。** "
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.夜明け`・`舟`・`舟.appearance`・`舟.negative` の8鍵である。"
                  "⚠️ **集合が挙げているのは `舟` であって、`帆` ではない**——**この1本の空には何も張られていない。**",
 "ref_extra": [
   "- ⚠️ **`video-spec` は、この作品の基本の形式である**（逐語:「**This card is `video-spec` plus one "
   "grammar.**」——**他の形式は、この形式に文法を1つ足したものである**）。"
   "**ゆえにこの1本には、§8 の5つ以外に足す文法が無い**——"
   "**§8 に書いた6つの変数が、この形式の環境変数の全部である。**",
   "- ⚠️ **この1本の形式が変わっているのは、意図である**——`s16`・`s17` が `transformation` を名乗り、"
   "**この1本は素の `video-spec` に戻る。****戻ること自体が、変身が終わったことの合図である。**",
 ],

 "narrative": {
   "core": "**男が初めて水の上に立ち、星を見て舵を取り、舟が向きを変える** — そして**星は動かない。**",
   "beginning": "**暗い海と、明るくなりはじめた空。****星が、まだ全部出ている。**"
                "舟はうねりに合わせて上下しているが、**まだ向きを変えていない。**",
   "turn": "**彼が星を見て、舵を動かす。****動きは小さい。**"
           "⚠️ **この2秒半は、彼の手と、動かない星とのあいだにある。**",
   "peak": "**舟が向きを変える。****そして星は動かない。**",
   "pull": "⚠️ **星が動かないことが、切れ目のコマである。****舟は向きを変え、空は明るくなり、"
           "星は同じところにある**——**その瞬間に、`l16` の歌が終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.599秒.** 頭の2.002秒は**暗い海と、まだ出ている星**のために払われ、"
            "次の2.500秒は**彼が星を見て、舵を動かすことに**払われ、**最後の2.599秒がこの1本の出来事である。** "
            "⚠️ **形式カードの逐語:「One beat — the core reveal — takes the largest single share (a useful "
            "anchor: ~30% of `DURATION`).」**——**この1本の中心は第3のビートであり、その2.599秒は "
            "7.101秒のうちの約37%である。** ⚠️ **この作品は均平に配らない**（`L37` が敷き詰めを、"
            "§8 が不均等を検算する）。⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**舟が向きを変えるあいだも、うねりは動き続けている。**\n"
            "- ⚠️ **`video-spec` の6つの変数**（⚠️ 定義はカードの逐語である）:\n"
            "  - `SUBJECT`＝the arc — **星を数えて舵を取ることである。**"
            "**暗い海から始まり、星を見て舵を動かし、舟が向きを変えるところで終わる。**\n"
            "  - `DURATION`＝clip length (**the model decides the duration**) — ⛔ **この作品では、"
            "曲が長さを決める**（`bible.time_source: song`）。**`l16` の行の長さがそのままこの1本であり、"
            "それは `7.101s` である**——**ゆえに §1 の `Duration` は記録の逐語であり、モデルは決めない。**"
            "⚠️ **カードの括弧書きは、この作品では成り立たない。****その事実をここに書く。**\n"
            "  - `ASPECT`＝aspect ratio — **`16:9` である**（裁定④。**この作品はアスペクトを一つに固定する**）。\n"
            "  - `BEATS`＝the beat list with second ranges — **上に書いた3つである**"
            "（0–2.002／2.002–4.502／4.502–7.101）。\n"
            "  - `CORE`＝the beat that gets the largest share — ⚠️ **第3のビートである**"
            "（`4.502-7.101s`、**2.599秒**）。**舟が向きを変え、星が動かない。**\n"
            "  - `HOOK`＝the note the clip ends on — ⚠️ **星が動かないことである。**"
            "**舟は回り、空は明るくなり、星は同じ高さにある**——**切れ目はそのコマで来る。**",

 "actions": [
   ("ACT_DRIFT", "舟はうねりの上にあり、向きは変わっていない。",
    "**暗い海と、明るくなりはじめた空**——そして**星が、まだ全部出ている。**"),
   ("ACT_READ", "彼の手は舵の櫂に触れているが、まだ動かしていない。",
    "**彼が星を見て、舵を動かす**——**動きは小さい。**"),
   ("ACT_TURN", "舟は元の向きのまま、航跡は真っ直ぐである。",
    "**舟が向きを変える**——**航跡が曲がり、そして星は動かない。**"),
 ],

 "camera": {
   "language": "Third person, **on the raft itself, low and close behind him** — the frame holds the "
               "back of his head and shoulder, the stern and the lashed oar in the near ground, **and "
               "the sky opening above him.** ⚠️ **この高さは、彼が立っている高さである。**"
               "⚠️ **この1本は水の画ではない**——**水は下のほうにあり、上は空である。**",
   "events": "One event only. `0-2.002s` — **the frame holds at his shoulder, low, still**; then "
             "`2.002-7.101s` — **a slow rise over his shoulder toward the sky, at the pace of his own "
             "look upward and never leading it**, and **it is still rising when the raft turns.** "
             "⚠️ **動機は、彼が見上げることである。** ⚠️ **カットしない。この上昇は途中で止まらない。**"
             "⚠️ **彼の顔を越えない**——**この1本は顔の画ではない。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the crane** "
               "— a rise from his shoulder toward the open sky, with a real rig's weight and a slow "
               "start. ⚠️ **Neither a dolly nor a Steadicam is used, and neither is needed**"
               "——**この1本は持ち上がるだけであり、横へも、手の内側へも動かない。**"
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and **no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、彼の左手と、舟と、そして星である。**"
              "**彼は星を見て、舵を動かす。****動きは小さく、確かである。**"
              "⚠️ **舟は上下し、星は動かない**（`motion.quality` の逐語）。",
   "object": "**舵の櫂が動く**——**縛られたまま、船尾で角度を変える。****舟がうねりに合わせて上下する。**"
             "**航跡が後ろへ伸び、そして曲がる。** ⚠️ **丸太と縄は動かない**——"
             "**この1本には、緩む縄も、ずれる板も無い。**",
   "environment": "**長く低いうねりが、一つの方向へ絶えず動く。****航跡だけがその面を破る。**"
                  "⚠️ **空の色が青から灰白へ移り、星が一つずつ消えていく**"
                  "——**それでも、この1本のあいだは、まだ全部が出ている。**"
                  "⚠️ **海は彼に反応しない。**",
   "weight": "**舟は重いが、小さく見える。****彼の左手には、水の重さが返ってくる。**"
             "⚠️ **この1本の重さは、梃子ではなく、水そのものである。**",
   "inertia": "**向きは、急には変わらない。****舵を動かしてから、舟が応えるまでに間がある。**"
              "⚠️ **この間が、この1本の真ん中である。** ⚠️ **何も瞬間には止まらない。**",
   "acceleration": "**加速しない。** 彼の手は一定の速さで動き、**カメラの上昇も一定である。**"
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この7.101秒に、止まったフレームは"
               "一つも無い**——**うねりは最後のコマまで動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**向きが変わることは、打撃ではない。**"
             "**音を立てない変化である。**",
 },

 "emotion": {
   "arc": "**数えること。****数を言わずに、数えていること。** ⚠️ **この1本の感情は、"
          "「初めて水の上に居る」ことの高ぶりではない**——**静かな手仕事である。**"
          "⛔ **壮大にしない。****暗い画のまま、最後まで行く。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしの大写しでもない。****舟が向きを変え、"
             "星が動かないことである。** ⚠️ **彼は数えているが、数はどこにも出ない**"
             "——**数が出れば、この1本は説明になる。**",
 },

 "lighting": {
   "base": "**太陽はまだ出ていない。**光源は空と、**水面に映った星の一筋だけである。**"
           "**海はまだ暗く、空だけが灰白へ向かっている。** ⚠️ **この1本の光源は一つであり、それは空である。**"
           "⚠️ **舟を別に照らさない**——**彼の顔にも、特別な光を当てない。**",
   "events": "**One, and it runs the whole shot.** **空の低いところが灰白へ移りはじめ、星が一つずつ"
             "消えていく**——**それでも北斗が名指されるのは `s19` であり、この1本はまだ全部の星を"
             "同じ扱いで写す。** ⚠️ **光源は動かない。** ⚠️ **様式カードの逐語:「The grade holds for the "
             "whole shot — a colour temperature that swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水が舟の丸太に当たる音、縄の鳴る音、そして舵の櫂が水を噛む音。**"
          "⚠️ **彼は何も言わないが、無音ではない**——**水の音が、この1本の音の側の主題である。** "
          "⚠️ **白波の音は無い**——**この海は白波を立てない**（`海.base` の逐語:「**no white water**」）。",
   "music": K.NO_MUSIC + " ⚠️ **そしてこの1本には、歌が在る**——`l16`「星を数えて舵を取る」であり、"
            "**行の長さが、そのままこの1本の長さである**（161.809–168.910）。"
            "**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜明け前の外海。**水、木、縄、そして風。** ⚠️ **鳥の声は無い**——"
                  "**この海に鳥は居ない**（`海.base` の逐語:「**no bird**」）。"
                  "⚠️ **呼ぶ声も、歌う声も無い。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="**体格・肌・髪・髭・顔・傷・着ている一枚と、着ていないすべて・裸足であること。** "
                "⚠️ **この1本は顔の大写しを持たないが、塊は §18 にまるごと入る**——**ゆえにこの1本も、"
                "`s05` が立てた顔から外れてはならない。**",
     may="左手の位置、見上げる角度、上体の傾き、袖の落ち方、丸太の下の水の動き。"),
   "spatial": "**舟の上である。****彼は舟尾に立ち、カメラはそのすぐ後ろにある。**"
              "**陸はどの方向にも見えない**（`海.geography` の逐語）。"
              "⚠️ **この1本で、この作品の2つの視点が同じ海であることが証明される**"
              "（`海.geography` の逐語:「**the same waterline and the same horizon appear in both**」）"
              "——**岸から見た海と、舟から見た海は、同じ一つの海である。**",
   "temporal": "一日の始まり、**`s17` と同じ夜明けである。** ⚠️ **この作品の `夜明け` は"
               "「空が青から灰白へ移る30分」であり、**星がまだ出ている。** 画の中に日付を与えるものは"
               "何も無い。",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は空の光だけである。**"
             "⚠️ **この1本は `video-spec` を名乗るので、§15 に例外を求めない**"
             "——**この1本は、場所も時刻も一つである。**",
   "motion": "Full animation, not limited. **彼の手が動き、舵が動き、舟が動き、うねりが動く。** "
             "⚠️ **カメラは1回だけ動き、そして止まらない。**",
   "sound": "水、木、縄、舵の櫂。**音楽なし。言葉なし。** ⚠️ **主題歌はこの1本のあいだ鳴っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**この1本には彼が居る**——**ゆえに女神の禁制は、他人の形で来る。**"
     "**星の道を与えた者を、人のかたちで置かない。**")) + [
   "**No second person in frame at all** — no companion, no crowd, no figure at any distance, "
   "**no one on the water and no one on the raft with him.**",
   "**No boat, no ship, no hull, no other vessel** (逐語, `ledger.props.舟.negative` の "
   "`no boat, no ship, no hull`、そして `ledger.locations.海.base` の `no other vessel`)。"
   "⚠️ **この1本の海には、彼の筏しか無い。**",
   "⚠️ **この1本の舟は筏である**——`ledger.props.舟.negative` の逐語は「**no boat, no ship, no hull, "
   "no keel, no planking**」であり、**この禁制は、筏を舟として描くことを禁じている。**"
   "**画の中の筏は、この禁制の対象ではない**（`ledger.props.舟.appearance` の逐語:「A raft, not a "
   "boat.」）。",
   "**No sail is set on the raft in this frame** (逐語, `ledger.locations.海.base` の `no sail`). "
   "⚠️ **マストは立っているが、そこには何も張られていない。**",
   "**No bird anywhere in this frame** (逐語, `ledger.locations.海.base`).",
   "**No land, no shore, no island, no coastline visible in any direction, including behind** "
   "(逐語, `ledger.locations.海.base`). ⚠️ **この1本では、島はもう見えない。**",
   "**No wheel, no helm, no rudder, no tiller** — ⚠️ **舵は船尾に縛られた一本の櫂である。**",
   "**No keel, no ribs, no planking, no metal fastenings, no nails** (逐語, `props.舟.negative`). "
   "**No rope that is not hand-twisted.**",
   "**No white water, no breaking crest, no spray** — **この海は白波を立てない。**",
   "**No constellation singled out, read as a shape, or named** — ⚠️ **星はこの1本では全部が同じ扱いである。**"
   "**北斗が名指されるのは `s19` である。**",
   "⚠️ **No legible number, no tally, no mark on any surface, no counting written down.** "
   "**彼は数えているが、数は画面に出ない。**",
   "⚠️ **No backwash of a wake that folds over itself, and no speedboat wake** — "
   "**航跡は、ゆっくり引かれた一本の線である。**",
 ],

 "must": [
   "**彼が初めて水の上に居ること** — そして**それでも壮大にしないこと。**",
   "**星を見て、舵を動かし、舟が向きを変えること** — そして**星は動かないこと。**",
   "⚠️ **舵は舵輪ではなく、船尾に縛られた一本の櫂であること。**",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.**",
   "⛔ **切らない。** **1本は1つの画である。****カメラは1回だけ動く。**",
   "⚠️ **彼は数を言わない。****数を言えば、この1本は説明になる。**",
   "⚠️ **陸も、帆も、鳥も、他の船も無い** — **`海.base` の逐語が、この1本の禁制である。**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **彼はレンズを見ず、口を開かない。**",
   "⚠️ **変化は最後のコマで終わる** — 星が動かないまま、この1本は終わる。",
   "⚠️ **この1本は、彼が海の上に居る最初の1本である** — **この場所の逐語を、この1本で曲げない。**",
 ],

 "prefer": "The raft held as the ground of the frame; the dark sea kept dark; the reflected stars the "
           "only bright thing; his hand on the lashed oar read clearly as a lever and not a helm; "
           "**the rise over his shoulder kept slow, and the sky opening as it rises.**",
 "allow": "The raft moving under him more than he moves; the wake lengthening and bending; the stars "
          "over the whole frame; a gentle flare on the one reflected path; **a slow rise that never "
          "reaches his face and never leaves the raft.**",

 "priorities": [
   "⛔ **星が動かないこと。** **この1本の切れ目は、それである**——"
   "**舟が回っても星が同じところにあれば、この1本は成立する。**",
   "⛔ **舵を舵輪にしないこと。** 「舵を取る」という語が、この経路を舵輪へ引き寄せる。",
   "⚠️ **陸・帆・鳥・他の船を入れないこと** — **`海.base` の逐語がこれである。**",
   "⚠️ **数を画面に出さないこと** — **彼は数えているが、数は言わない。**",
   "⚠️ **壮大にしないこと** — **暗い画のまま、最後まで行く。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "**No second person, at any distance, in any focus.**",
   "⚠️ **`video-spec` の6つを満たすこと** — `SUBJECT` は星を数えて舵を取ること、`CORE` は第3のビート、"
   "`HOOK` は星が動かないこと、`DURATION` は曲が決めた 7.101秒。",
   "**光は空の光だけであること** — 専用の光源も、火も無い。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `video-spec` を名乗る。****この形式は他の形式の土台であり、"
   "§16 に運ぶカード自身の禁制を持たない**——**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 7.101-second cinematic take (16:9) of open sea at dawn, one clip, one continuous take, shot from "
   "the raft itself, one change: **the raft stops drifting and takes its heading.**\n\n"
   "**{IDENTITY}** He stands at the stern with his left hand on the steering oar, **which is tied at the "
   "stern and lashed, not fitted — it is not a wheel and it is not a helm.** **He looks up at the "
   "stars, and then he moves the oar. He does not speak and he does not look at the lens.**\n\n"
   "0-2.002s: **the sea is dark and the sky has only begun to lighten, and the stars are still all "
   "out.** The raft rides the swell and has not turned.\n"
   "2.002-4.502s: **he looks at the stars and moves the oar.** **The movement is small.** The frame "
   "rises slowly over his shoulder toward the sky.\n"
   "4.502-7.101s: **the raft turns** — the wake bends — **and the stars do not move**, and the take "
   "ends on that.\n\n"
   "**There is no land in any direction, including behind; no other vessel; no sail set on the raft; no "
   "bird; and no white water anywhere.** **The raft is a raft: logs lashed with hand-twisted cordage, no "
   "keel, no planking, no rudder, no wheel.** **He counts but no number appears anywhere in the frame "
   "and he says none.** **No second person is in this frame at any distance or in any focus, and no "
   "woman is in it at all.** **This is a bronze-age sea before classical Greece: no made thing of any "
   "later age.** **This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the raft takes its heading, and the stars do not move.)"),

 "visual_scene": (
   "Open sea at dawn seen from the raft itself, photographed as a film frame: **the raft fills the "
   "lower part of the frame** — forty-odd unseasoned pine logs still barked and uneven, lashed side by "
   "side with coarse hand-twisted cordage, a low platform of hewn planks laid across them and not "
   "fastened flush, **a steering oar tied at the stern and lashed, not fitted**, and a short mast of a "
   "trimmed pine trunk stayed with rope with **nothing set on it.** **The man stands at the stern, his "
   "back to the frame, his left hand on the oar; the frame holds the back of his head and his shoulder "
   "and does not show his face.** **Beyond the raft the sea is dark and long-swelled with no white "
   "water, the wake the only break on it; above it the sky is going from blue to grey-white and the "
   "stars are still out. There is no land in any direction, no sail, no bird, no other vessel.**"),

 "visual_meta": (
   "Anamorphic lens with subtle oval bokeh and a gentle flare on the reflected path; a moderate depth "
   "of field; a graded palette that is almost all dark — black water, a sky going from the blue of "
   "night to grey-white, and one white path of reflected starlight as the only bright thing in the "
   "frame. Barked pine logs and coarse hand-twisted cordage at the raft's edge; undyed wool with "
   "visible fibre and a worn shoulder seam; skin roughened and marked; even film grain over "
   "everything. No painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration. "
   "⚠️ **The frame is dark and almost empty by design** — the sea is still black, the stars stand in "
   "the sky above it, and the only bright thing on the water is the one broken reflected path."),

 "motion_prompt": (
   "Full animation, not limited. **His left hand moves the lashed steering oar and the raft answers it "
   "late, so that the turn is spread over the last seconds and never snaps.** **The movement of his "
   "hand is small and sure**; his upper body turns only as far as the oar does. **The raft rides the "
   "long low swell the whole time, and the wake lengthens behind it and then bends.** **The stars do "
   "not move at all — they keep their positions from the first frame to the last.** **The camera rises "
   "slowly over his shoulder toward the sky, at the pace of his own look upward, and it is still rising "
   "when the take ends.** The water in the near ground breaks only at the raft's edge and along the "
   "wake; there is no spray and no breaking crest anywhere in the frame. No motion blur smears, no "
   "stutter, no floaty weightless motion, no static frames — **the swell moves in every frame of the "
   "take.**"),

 "camera_prompt": (
   "Third person, **on the raft, low and close behind him** — the frame holds the back of his head and "
   "his shoulder, the stern and the lashed oar in the near ground, and the sky opening above. One event "
   "only: **a slow rise over his shoulder toward the open sky, at the pace of his own look upward and "
   "never leading it.** ⚠️ **The move is motivated by his looking up; it never reaches his face and "
   "never leaves the raft.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot "
   "spends the crane** — a rise with a real rig's weight and a slow start. ⚠️ **Neither a dolly nor a "
   "Steadicam is used, and neither is needed** — this frame only rises, and has no reason to travel "
   "sideways. No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, no "
   "unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water working against the raft's logs, the low creak of "
   "hand-twisted cordage taking the load, and the steering oar biting the water as it turns.** "
   "⚠️ **He says nothing, but this shot is not silent — the water is the subject of this shot's sound.** "
   "⚠️ **No white water and no spray are heard; this sea does not break.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②）。"
                        "⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ。**"
                        "⚠️ **参照集合の8鍵のうち、この1本の場所は `海`、乗っているものは `舟` である。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water ＋ cordage ＋ steering oar ／ no music",
 "unresolved": [
   "⚠️ **この1本の空に帆が無いこと。** ⚠️ **この作品は `s17` で帆を縫い上げているので、"
   "時系列では帆は存在する。** ⚠️ **しかしこの1本の参照集合は `帆` を挙げておらず、"
   "`海.base` は逐語で `no sail` と言う。** **この仕様は「この1本では張られていない」と読んだ**"
   "——**いつ張るのかは、記録からは読めない。****`s23`〜`s34` のどこかである。**",
   "⚠️ **`video-spec` の `DURATION` の括弧書き。** カードは逐語で「**the model decides the "
   "duration**」と言うが、**この作品では曲が長さを決める**（`bible.time_source: song`）。"
   "**この仕様は曲の側を採った**——**§1 の `Duration` は記録の逐語である**（`L23`）。"
   "**ゆえにこの1本では、カードの括弧書きが成り立たない。****その食い違いは §8 に書いた。**",
   "⚠️ **星を名指さなかったこと。** ⚠️ **`ledger.locations.海.states.夜明け` は"
   "「北の七つは高さを変えない」と書く。****この1本でも、その七つは空にある。**"
   "**しかしこの仕様は、この1本ではどれも名指さず、形としても読まない**——"
   "**名指すのは `s19` の仕事であり、先に名指せば、あちらの1本が何も言わなくなる。**"
   "⚠️ **これは裁定ではなく、この仕様の判断である。**",
 ],
 "risks": [
   "⛔ **舵が舵輪になる。** ⚠️ **この経路は「舵を取る」という語を、いちばん自然に舵輪へ写す。**"
   "**`props.舟.appearance` の逐語と §16 の禁制の両方に在る。**",
   "⛔ **他の船が入る。** ⚠️ **海の画に船を足すのは、この経路がいちばん自然にやってしまうことである**"
   "——**`海.base` の逐語と §16 の禁制の両方に在る。**",
   "⛔ **島が入る。** ⚠️ **`s13`〜`s15` の海は島を写してきたので、この経路は島を残しやすい。**"
   "**この1本は「陸はどの方向にも見えない」である。**",
   "⚠️ **帆が張られる。** ⚠️ **この作品は `s17` で帆を持っているので、"
   "この経路が「帆船」を描く余地がある。****この1本は張られていない。**",
   "**北斗が先に名指される。** ⚠️ **`s19` の1本が、この1本で消費されうる。**",
   "**壮大になる。** ⚠️ **空が開いた画は、この経路では英雄的に作られやすい**"
   "——**この1本は暗いままである。**",
   "**顔が動く（drift）。** ⚠️ **この1本は顔を写さないが、見上げる角度で横顔が出る**"
   "——**参照画像が1枚も無いので、守る道具は英文だけである。**",
 ],
}

if __name__ == "__main__":
    print("s18 content OK — keys:", len(C))
