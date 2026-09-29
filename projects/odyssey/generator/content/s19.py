# -*- coding: utf-8 -*-
"""odyssey-s19 — time-fold — 沈まない星 / 夜明け / 12.127s. One star outside time."""
import common as K


C = {
 "n": "s19",
 "title": "北斗は沈まない——一つだけが時間の外にある",
 "duration": "12.127",
 "format": "time-fold",
 "has_man": True,
 "segment": "verse-2-4",

 "band": [
   "『永遠より遠い』 verse-2「沈まない星」 / 様式美 / motion —— 北斗は沈まない——一つだけが時間の外にある",
   "明るくなっていく空で星が一つずつ消えるが、北斗だけが同じ高さに残る。",
   "12.127秒、カメラは三脚の上で北斗へゆっくり寄る——他の星が全部消えるのが、切れ目である。",
   "北斗は一度も動かない——他の全部が動いているから、それが見える。",
 ],
 "header": """⛔ **`verse-2` を夜明けにした読みが、この1本で効く。****沈まない、とは——夜明けにも、まだ沈まない、ということである。**
**日の出とともに全部が消えるとき、一つだけが残る。****「沈まない星」の意味が、夜ではなく夜明けにある。**
⚠️ **この読みは、詩の第五巻に忠実である**——彼は舵を取りながら、**一度も沈まない星座を左手に保つ**（5.273）。
⛔ **この1本の場所だけが、この作品で唯一「上が開いている」**（`locations.沈まない星`）——**他の5つは、すべて水平である。**
⚠️ **2行を束ねた理由は長さである。** 実測: `l17` は 3.510秒——**この曲で最も短い行である**（`l04` と同位）。`l18` は 8.617秒。**2行で 12.127秒。**
⚠️ **形式は `time-fold`。****この作品で4本目である**（`s03` の註を見る）。
⚠️ **切れ間は `l18` の歌い終わりである**（168.910–181.037）。**`l17` の頭から `l18` の終わりまでであり、`l18` は 8.617秒で、`verse-2` では `l14` に次いで長い。****行の長さが、そのままこの1本の長さである**。
⚠️ **この仕様のショット記録は `shots/odyssey-s19.yaml` である。**""",

 "intent": "**一つの星が沈まないことを、12秒で写せるか。** ⚠️ **時間が経っていることが見えなければ、"
           "沈まないことは見えない。** "
           "⛔ **切らない。戻らない。****この1本は空を離れない。** "
           "⚠️ **他の全部が動いているから、一つが動かないことが見える**（`motion.law` の逐語）"
           "——**ゆえにこの1本の12秒は、空が青から灰白へ移るために払われる。** "
           "⛔ **変化は切れ目のコマで終わる**——**他の星が全部消え、北斗だけが同じ高さにある。**",

 "world_concept": K.world_concept(
   "⚠️ **この場所は、この作品で唯一「上が開いている」**——**他の5つは、すべて水平である。**"
   "⛔ **この1本だけが、彼の頭上を正面から写す。**"
   "（⚠️ **`place` が `沈まない星` であるのは、34本でこの1本だけである**——`roster.json` の実測。"
   "**ゆえにこの画角を持つのは、この1本だけである。**）"
   "⚠️ **それでもこの場所は、彼から切り離されていない**——**北斗は彼の左手の側にあり、"
   "柄は彼の舟首を指している**（`沈まない星.geography` の逐語）。"
   "**空は、彼の上にあるのではなく、彼の手の側にある。**"
   "⚠️ **この作品の `夜明け` は「空が青から灰白へ移る30分」である。****この1本は、その30分を畳む。**"),

 "world_rules": K.world_rules(
   drop=(), tails={
     "answer": "⚠️ **この1本には彼が居る**（画面の下端に、左手だけが）。**それでも返事は無い**"
               "——**星は消えるが、それは返事ではない。****空は彼のために明るくなるのではない。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "⚠️ **この1本の北斗は、与えられた道ではない**——**彼が数えているだけである。**"
                "**与えた者を、この1本も写さない。**",
     "name": "⚠️ **この1本に名は無い。**⚠️ **北斗は名指されるが、名ではなく、形と高さで示される**"
             "——**この作品に、星座の名を書く欄は無い。**",
     "bow": "⚠️ **この1本に弓は無い。** **画面の下端にあるのは、船尾に縛られた舵の櫂と、"
            "そこに置かれた左手だけである。**",
     "places": "この1本が持つのは `沈まない星` である——**この作品で唯一、上が開いている場所であり、"
               "この場所を使うのはこの1本だけである**（`ledger.locations.沈まない星` の実測）。"
               "⚠️ **同じ海の上でありながら、この1本の画は水ではなく空である。**",
     "japanese": "⚠️ **この1本には歌がある**——`l17`「北斗は沈まない」と `l18`「沈まない星を見ている」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **この1本の意味が、この1本の置かれた時刻にある。**"
     "**夜に置けば、「沈まない」は何も言わない**——**全部が沈まないからである**"
     "（`ledger.locations.沈まない星` の註の逐語）。**夜明けに置くから、一つだけが残ることが見える。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "The night sky above open water, seen from below, photographed as a film frame. **Seven bright "
     "stars in the shape of a long-handled ladle — four of the bowl and three of the handle — holding "
     "their position low and clear above the horizon.** ⚠️ **At the very bottom of the frame: the stern "
     "of the raft, the lashed steering oar, and his left hand on it.** **No clouds, no moon, no other "
     "constellation read as a shape** (逐語, `ledger.locations.沈まない星.base`).",
   "Color Language":
     "A narrow, graded palette that moves in one direction only — **the sky goes from the blue of night "
     "to grey-white, and the stars are subtracted from it one at a time.** "
     "⚠️ **The seven keep the same value throughout** — they do not brighten and they do not dim, "
     "**because they are not part of the passage.** ⚠️ **Nothing is lit apart from the place** — "
     "**one light only, and it is the sky's own; the shot has no second light.**",
   "Texture":
     "Air, and the last of the night in it: **no cloud texture, no haze bank, no moon, nothing in the "
     "sky but the stars and the lightening.** At the bottom edge, the raft: **wet pine logs, coarse "
     "hand-twisted cordage, and his hand**. ⚠️ **The horizon line is level and unbroken and carries no "
     "land.** Film grain present and even.",
   "Rendering":
     "Photographic — anamorphic optics, a shallow depth of field set at the stars, subtle oval bokeh, "
     "**the faintest flare on the brightest of the seven.** **Not a photograph's stillness: a film "
     "frame.** No illustration, no CGI look, no cartoon color.",
   "Visual Density": "Very low. **The frame is almost all sky, and emptiness is the content** — "
                     "**the stars are subtracted from it until seven are left.** "
                     "⚠️ **空が空いていること自体が、この1本の主題である。**",
   "Time": "`夜明け` — the thirty minutes when the sky goes from blue to grey-white. ⚠️ **この場所の状態は"
           "これひとつである**（`ledger.locations.沈まない星.states.夜明け`）。**夜明けの空も、"
           "まだ夜の空である**（`base` の註）——**ゆえに星はまだ出ている。** 画の中に日付を与えるものは"
           "何も無い。",
   "Atmosphere": "The half hour in which everything in the sky leaves except one thing.",
 }),

 "subjects": [
   K.man_subject(
     behavior="⛔ **この1本に彼は居るが、画の下端に左手だけがある。**"
              "**彼は船尾に立ち、左手を縛られた舵の櫂に置いている**——**この1本のあいだ、"
              "その手はほとんど動かない。** ⚠️ **顔は写らない。****見上げる角度も写らない。**"
              "⚠️ **彼は口を開かず、レンズを見ない。**",
     may="左手の指の力の入り方、袖の落ち方、画面の下端に出入りする丸太の位置。",
     extra_notes=[
       "⛔ **この1本の主題は、彼ではなく、空である。****彼はこの1本の物差しの一端である**——"
       "**北斗が彼の左手の側にあることが、この1本の定位である**"
       "（`沈まない星.geography` の逐語:「**the ladle is on the raft's left hand — the same side in "
       "every frame that holds it**」）。",
       "⚠️ **この1本は彼を見ない。****ゆえに見上げる角度も、目の動きも無い**——"
       "**もし目が入れば、この1本は彼の画になる。**",
       "⚠️ **`s05` が立てた顔の基準から外れない。** ⚠️ **この1本は顔を写さないが、"
       "塊は §18 にまるごと入る。**",
     ]),
   {"name": "空と、七つの星",
    "ref": "**この1本の主題である。** ⚠️ **参照は `沈まない星` の `base` と `geography`、"
           "そして `states.夜明け` である**——**この作品に参照画像は無い**（裁定②）。",
    "appearance": "**長柄の柄杓の形をした七つの明るい星である。****椀が四つ、柄が三つ。**"
                  "**地平線の低いところに、はっきりと、高さを保って居る。**"
                  "⚠️ **雲も、月も、形として読める他の星座も無い。**"
                  "⚠️ **地平線は画の低いところを横切る。** 七つは地平線の上にあり、動かない。",
    "behavior": "⛔ **七つは、この1本のあいだ、同じ高さに留まる。**"
                "**他の星は一つずつ消えていく。****空は青から灰白へ移る。**"
                "**七つだけが、その両方に動かされない。** ⚠️ **七つは地平線へ近づかない**"
                "（`geography` の逐語:「**they never approach it**」）。",
    "continuity": "**Must preserve** — 七つの数（**椀が四つ、柄が三つ**）、形、明るさ、"
                  "**地平線からの高さ**、**彼の左手の側にあること**、**柄が舟首を指していること**。"
                  "**May change** — 空の色だけである。⚠️ **星の位置は変わらない。**",
    "notes": ["⛔ **七つの位置を、この1本のあいだ一度も動かさないこと。****それ以外の星は全部消える。**"
              "**この対比が、この1本の全体である。**",
              "⚠️ **七つを、いっそう明るくしないこと。** **それは「特別な星」の画になり、"
              "「動かない星」の画にならない**——**動かないことが主題である。**"]},
 ],

 "environment": {
   "location": "`沈まない星` — **この作品で唯一、上が開いている場所である。**"
               "**舟の真上である**（`geography` の逐語:「**Directly above the raft**」）。"
               "**地平線は画の低いところを横切る。** ⚠️ **陸は無い。**"
               "⚠️ **カメラはこの場所を離れない**（`time-fold` の逐語:「**The camera is the anchor. "
               "The place is held.**」）。",
   "elements": "**七つの明るい星**（椀が四つ、柄が三つ）、**消えていく他の星**、"
               "**青から灰白へ移る空**、**画の低いところを横切る水平線**、"
               "**そして画の下端に、舟の船尾と、縛られた舵の櫂と、そこに置かれた左手。**"
               "⚠️ **雲も、月も、鳥も、陸も、他の船も無い。**",
   "behavior": "**星が一つずつ消えていく。**⚠️ **消える順も、速さも、一様ではない。**"
               "**空の色が青から灰白へ移り、低いところから明るくなる。**"
               "**七つは高さを変えない。** ⚠️ **地平線は水平のままである。**"
               "⚠️ **空は彼に反応しない**——**彼が居ても居なくても、同じ速さで明るくなる。**",
 },

 "objects": [
   "**七つの星** — **この1本の生存者である。**⚠️ **この1本のあいだ、一度も動かない。**"
   "**それ以外の星は、全部消える。**",
   "**他の星** — 一つずつ消えていく。⚠️ **一斉にではない。****ばらばらに、"
   "しかし確実に、数が減っていく。**",
   "**空** — 青から灰白へ移る。⚠️ **この1本の経過そのものである。**",
   "**舵の櫂と、彼の左手** — 画の下端にある。⚠️ **この1本のあいだ、ほとんど動かない**"
   "——**この1本の静止は、この手にある。**",
   "**舟の船尾** — 画の下端。**丸太と、手で撚った縄。** ⚠️ **水はこの1本の画には入らない**"
   "（入るのは水平線までである）。",
   "⚠️ **この作品の小道具4つのうち、この1本に来るのは舟だけである**（`ledger.props`）——"
   "**帆も、斧も、太陽の牛も、この1本の画には無い。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — **この1本には添付しない。彼女はこの1本に、四つの姿のどれとしても現れない。** "
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`沈まない星`・"
                  "`沈まない星.geography`・`沈まない星.states.夜明け`・`海`・`海.geography`・"
                  "`海.states.夜明け` の8鍵である。"
                  "⚠️ **集合が `海` を3鍵挙げているのは、この空が海の上にあるからである**"
                  "——**画に入るのは水平線までであり、水そのものではない。**",
 "ref_extra": [
   "- ⚠️ **形式カード `time-fold` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; "
   "what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §8 に書いた5つの変数と、§16 に運んだカード自身の禁制である。**",
   "- ⚠️ **この形式は、この作品で4本目である。****`s03` が `time-fold` の1本目であり、"
   "`s03` の註が `SURVIVOR` の読み方を定めている**——**「『境』を生存者にしてはならない」"
   "（`s03` の逐語。**消えるものが、生存者ではありえない**）。"
   "⛔ **この1本は、消えないものを生存者にした。****他の全部が消えるから、七つが測れる。**",
 ],

 "narrative": {
   "core": "**空が青から灰白へ移り、星が一つずつ消えていくあいだ、七つだけが同じ高さに留まる** "
           "— そして**他の星が全部消えても、七つはまだそこにある。**",
   "beginning": "**空に星がある。****まだ全部出ている。**地平線は低く、七つはその上にある。",
   "turn": "**星が消えはじめる。****空が青くなる。**⚠️ **七つは高いままである**"
           "——**この2秒半から4.5秒のあいだに、数が減りはじめる。**",
   "peak": "**他の星が全部消える。****空は灰白である。**",
   "pull": "⚠️ **北斗だけが同じ高さにあるのが、切れ目のコマである。****空はもう明るく、"
           "他の星は一つも無く、七つだけがまだそこにある**——**その瞬間に、`l18` の歌が終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 4.633秒.** 頭の2.995秒は**まだ全部出ている空**のために払われ、"
            "次の4.499秒は**消えていく星と、青くなっていく空**に払われ、"
            "**最後の4.633秒がこの1本の出来事である。** "
            "⚠️ **形式カードの逐語:「**Uneven duration.** The seconds are not spread evenly over the "
            "span; choose the part of the passage the shot lingers on.」**——**この1本が長く居るのは、"
            "「他の星が全部消えて、七つだけが残る」ところである。** "
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**七つが止まっているあいだも、"
            "他の星は動き続けている。**\n"
            "- ⚠️ **`time-fold` の5つの変数**（⚠️ 定義はカードの逐語である）:\n"
            "  - `PLACE`＝the place that holds still — **`沈まない星`、舟の真上の空である。**"
            "**カメラはこの場所を離れない**（カードの逐語:「**The camera is the anchor. The place is "
            "held.**」）。**カットして戻ることは無い**——**戻れば、それは2本目の画であり、"
            "「一度も離れていない」というこの形式の主張が消える。**\n"
            "  - `PASSES`＝what time does to it — **星が一つずつ消え、空の色が青から灰白へ移る。**"
            "**この作品の `夜明け` は「空が青から灰白へ移る30分」であり、この1本はその30分である。**\n"
            "  - `SURVIVOR`＝what does not change across the span — ⛔ **ひとつだけ名指す。"
            "長柄の柄杓の形をした七つの星である**（**椀が四つ、柄が三つ**）。"
            "**12.127秒のあいだ、七つは高さを一度も変えない**——**ゆえに他の全部の移動が測れる。**"
            "⚠️ **「空の色」を生存者にしてはならない**——**色が移ることが、この1本の変化である。**"
            "⚠️ **カメラの位置も生存者ではない**——**カメラはわずかに寄るからである。**\n"
            "  - `RANGE`＝the span of time the shot crosses — **夜明けの30分である。**"
            "**空に星が全部出ているところから、他の星が一つも無くなるところまで。**"
            "⚠️ **年でも一生でも季節でもない**——**この作品が畳むのは、一日の始まりである。**"
            "⚠️ **画面の中には、経過した時間を名指すものが何も無い**（日付も、字幕も、"
            "「何年後」も無い——それらはカードの禁制である）。\n"
            "  - `DURATION`＝clip length — **`12.127s`。**",

 "actions": [
   ("ACT_HOLD", "プレースは固定され、七つは地平線の上にある。",
    "**同じであり、そしてこれは変わらない。** ⚠️ **「何もしない」ではない**——"
    "**この1本の物差しが、ここで立てられる。**"),
   ("ACT_ERASE", "空に星が全部出ている。",
    "**星が一つずつ消えている**——**消える順も速さも、一様ではない。**"),
   ("ACT_WHITEN", "空は青い。",
    "**空が青から灰白へ移っている**——**低いところから明るくなる。**"),
   ("ACT_REMAIN", "空に星があり、七つはその中にある。",
    "**他の星が一つも無く、七つだけが同じ高さにある**——"
    "**残ることが、切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **directly below, looking up** — the frame is the sky above the raft, "
               "with the horizon low in it and **the stern of the raft, the lashed oar and his left "
               "hand at the very bottom edge.** ⚠️ **この1本だけが、この作品で空を正面から写す。**"
               "⚠️ **他の5つの場所は、すべて水平である。**",
   "events": "One event only. `0-12.127s` — **a slow push toward the seven stars, short, at a "
             "constant rate, motivated by nothing but the looking itself.** "
             "⚠️ **この押しは、七つに着かない**——**12秒で近づくが、近づききらない。**"
             "⚠️ **カメラは場所を離れない。****切り返しも、戻りも無い**"
             "（`time-fold` の逐語:「**The camera may not cut away and re-enter, because coming back to "
             "the place is a second shot.**」）。",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** "
               "— a slow push with a real rig's weight, at a constant rate, **the only move in the "
               "shot.** ⚠️ **Neither a crane nor a Steadicam is used, and neither is needed**"
               "——**この1本は上にも横にも動かない。****動くのは、七つへ向かう一方向だけである。**"
               "**A fixed frame would be the native case of this card, and this shot declines it by one "
               "short move and no more.** No handheld, no whip, no shake, no snap zoom, no rack focus, "
               "no unnatural rotation, and **no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、空である。**⚠️ **七つは動かない。****それ以外の星が消え、"
              "空の色が移る。** ⚠️ **動いているのは、七つ以外の全部である。**",
   "object": "**七つの星は、この1本のあいだ一度も動かない。**"
             "**他の星が、一つずつ、順に、不可逆に消える。**"
             "⚠️ **画面の下端では、彼の左手と舵の櫂がほとんど動かない**——"
             "**この1本の静止は、そこにもある。**",
   "environment": "**空の色が、青から灰白へ、一方向に移る。****低いところから明るくなる。**"
                  "⚠️ **地平線は水平のままである。** ⚠️ **雲は動かない**——**雲が無いからである。**"
                  "⚠️ **環境は彼に反応しない。**",
   "weight": "⚠️ **この1本に重さは無い**——**主題が空だからである。**"
             "**重さの代わりにあるのは、不可逆性である**——**消えた星は戻らない。**",
   "inertia": "**消えることは、遅い。**⚠️ **星は一瞬で消えない**——"
              "**薄くなってから、消える。****そして戻らない。**",
   "acceleration": "**加速しない。****空の色の移り方も、星の消え方も、一様ではないが、"
                   "加速はしない。** ⚠️ **押しも一定の速さである。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この12.127秒に、止まったフレームは"
               "一つも無い**——**七つが止まっているように見えるのは、周りが動いているからである。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**星が消えることは、打撃ではない。**"
             "**音を立てない変化である。**",
 },

 "emotion": {
   "arc": "**時間が経っていることが見えること。****そして、一つだけがそれに動かされないこと。** "
          "⚠️ **この1本の感情は、壮大さではない**——**引き算である。**"
          "**空から、順に、全部が引かれていく。****最後に一つだけ残る。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****他の星が全部消えて、"
             "七つだけが同じ高さにあることである。** ⚠️ **この1本は彼を見ない**"
             "——**見上げる角度も、目の動きも写さない。**",
 },

 "lighting": {
   "base": "**太陽はまだ出ていない。**光源は空そのものである。"
           "**星は空の光の側にあり、照らされているのではない。**"
           "⚠️ **この1本の光源は一つであり、それは空である。**"
           "⚠️ **七つの星を別に照らさない**——**他の星と同じ扱いのまま、同じ高さに残る。**",
   "events": "**One, and it runs the whole shot.** **空の低いところが灰白へ移りはじめ、"
             "星が一つずつ消えていく**——**この移りが、この1本の経過そのものである。**"
             "⚠️ **光源は動かない。** ⚠️ **様式カードの逐語:「The grade holds for the whole shot — "
             "a colour temperature that swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水が舟の丸太に当たる音、そして縄の鳴る音**——**画の下端にあるものの音である。**"
          "⚠️ **この1本には、空の音が無い**——**星は音を立てないし、空の色も音を立てない。** "
          "⚠️ **この1本の音は、画の下端からだけ来る**——**それでも無音ではない。**",
   "music": K.NO_MUSIC + " ⚠️ **そしてこの1本には、歌が在る**——`l17`「北斗は沈まない」と "
            "`l18`「沈まない星を見ている」であり、**2行の長さが、そのままこの1本の長さである**"
            "（168.910–181.037）。**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜明け前の、外海の上の空。**水と、木と、縄と、そして何も無い空。** "
                  "⚠️ **鳥の声は無い**——**この空に鳥は居ない。** ⚠️ **呼ぶ声も、歌う声も無い。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="**体格・肌・髪・髭・顔・傷・着ている一枚と、着ていないすべて・裸足であること。** "
                "⚠️ **この1本が写すのは左手だけである**——**それでも塊は §18 にまるごと入る。**"
                "⚠️ **手は、その塊の一部である**（肌、節、傷）。",
     may="左手の指の力の入り方、袖の落ち方、画面の下端に出入りする丸太の位置。"),
   "spatial": "**舟の真上から見上げている。****地平線は画の低いところを横切る。**"
              "**北斗は彼の左手の側にあり、柄は舟首を指している**（`geography` の逐語）"
              "——**この定位は、この1本のあいだ変わらない。**"
              "⚠️ **陸は無い。** ⚠️ **`s18` と `s20` とで、この海は同じ一つの海である**"
              "（`海.geography` の逐語:「**the same waterline and the same horizon appear in both**」）。",
   "temporal": "一日の始まり、**`s17`・`s18` と同じ夜明けである。** ⚠️ **この1本は `verse-2` の最後である**"
               "——**夜明けが、ここで使い切られる。** 画の中に日付を与えるものは何も無い。",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は空の光だけである。**"
             "⚠️ **この1本は `time-fold` を名乗るが、その文法は §15 から何も免除しない**"
             "——**この1本は、場所も時刻も一つであり、"
             "生存者が一つである。**（免除を名乗るのは `coexisting-realities` であり、"
             "`s22` の仕事である。）",
   "motion": "Full animation, not limited. **星が消え、空の色が移り、カメラがわずかに寄る。** "
             "⚠️ **七つだけが動かない。****この対比が、この1本の全体である。**",
   "sound": "水、木、縄。**音楽なし。言葉なし。** ⚠️ **主題歌はこの1本のあいだ鳴っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**この1本には彼が居る（左手だけが）**——**ゆえに女神の禁制は、他人の形で来る。**"
     "**星の道を与えた者を、人のかたちで置かない。**")) + [
   "**No second person in frame at all** — no companion, no crowd, no figure at any distance, "
   "**no one on the water.**",
   "**No cut, no time-skip, no cross-dissolve, and no return to this place after leaving it** "
   "(逐語, `time-fold` の `## Negative`). ⚠️ **この1本は空を離れない。**",
   "**No date stamp, no caption, no title card carrying elapsed time, no aging makeup, no prosthetic** "
   "(逐語, `time-fold` の `## Negative`). ⚠️ **経過した時間を名指すものが、画面に一つも無い。**",
   "**No clouds, no moon in this frame, and no other constellation read as a shape** "
   "(逐語, `ledger.locations.沈まない星.base`).",
   "**No land, no shore, no island, no coastline** — **この1本の水平線は、空と海の境だけである。**"
   "**No bird, and no other vessel either** (逐語, `ledger.locations.海.base`)。"
   "⚠️ **この1本の舟は筏である**——`ledger.props.舟.negative` の逐語は「**no boat, no ship, no hull, "
   "no keel, no planking**」であり、**この禁制は、筏を舟として描くことを禁じている。**"
   "**画の下端にあるのは、その筏である**（`ledger.props.舟.appearance` の逐語:「A raft, not a "
   "boat.」）。",
   "**No star other than the seven keeps its position** — **他の星は全部消える。**",
   "**The seven never approach the horizon and never move.** ⚠️ **高さが変われば、この1本は何も"
   "言わなくなる。**",
   "**No glow, no halo, no added brightness on the seven** — **動かないことが主題であり、"
   "特別であることは主題ではない。**",
   "**No star chart, no diagram, no line drawn between the seven, and no legible name.** "
   "**形は形として写るのであって、図として描かれない。**",
   "**No wheel, no helm, no rudder, no tiller** — ⚠️ **画面の下端にあるのは、船尾に縛られた"
   "一本の櫂である。**",
   "⚠️ **No second light** — **空のほかに光源を置かない。****火も、灯も、月も無い。**",
 ],

 "must": [
   "**七つが、この1本のあいだ一度も動かないこと** — そして**他の星は全部消えること。**",
   "⛔ **カメラがこの場所を離れないこと。****切り返さない。戻らない。**",
   "⛔ **時間が経っていることが見えること** — **星が減り、空の色が移る。**"
   "**見えなければ、「沈まない」は何も言わない。**",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.**",
   "⚠️ **北斗と、彼の左手が同じ側にあること** — **この定位が、この1本の定位である。**",
   "⚠️ **経過した時間を名指すものを画面に置かないこと** — **日付も、字幕も、"
   "「何年後」も無い。**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **彼はレンズを見ず、口を開かない。****この1本は彼を見ない。**",
   "⚠️ **変化は最後のコマで終わる** — **他の星が一つも無く、七つだけが同じ高さにある。**",
   "⚠️ **`time-fold` の5つを満たすこと** — `PLACE` は舟の真上の空、`PASSES` は星が消え空が移ること、"
   "`SURVIVOR` は七つ、`RANGE` は夜明けの30分、`DURATION` は 12.127秒。",
 ],

 "prefer": "The sky held as almost the whole frame; the subtraction of the stars kept uneven and "
           "irreversible; the seven held at exactly the same value throughout; the horizon low and "
           "level; **the raft's stern and his hand kept at the very bottom edge, small and still.**",
 "allow": "The low part of the sky whitening before the high part; the stars vanishing at uneven "
          "rates; the faintest flare on the brightest of the seven; **a short slow push that never "
          "reaches them and never leaves the place.**",

 "priorities": [
   "⛔ **七つが動かないこと。** **この1本の全体は、それである**——"
   "**動けば、「沈まない星」は成立しない。**",
   "⛔ **時間が経っていることが見えること。****星が減り、空の色が移る**"
   "——**見えなければ、この1本は静止画である。**",
   "⛔ **カメラが場所を離れないこと。****切り返しも、戻りも無い。**",
   "⚠️ **経過した時間を名指さないこと** — **日付も、字幕も、タイトルカードも無い。**",
   "⚠️ **彼を見ないこと** — **画面の下端の左手だけであり、顔も、見上げる角度も写さない。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "**No second person, at any distance, in any focus.**",
   "**光は空の光だけであること** — 月も、火も、灯も無い。",
   "⚠️ **`time-fold` の5つを満たすこと** — とくに `SURVIVOR` が七つであること、"
   "`RANGE` が夜明けの30分であること。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `time-fold` を名乗るが、その禁制（`no cut`・`no time-skip`・`no date stamp`・"
   "`no cross-dissolve`・`no return to the place after leaving it` ほか）は §16 に在って、"
   "ここには無い。** **ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 12.127-second cinematic take (16:9) of the night sky above open water, seen from below, one clip, "
   "one continuous take, one change: **the sky goes from night to grey-white and every star is erased "
   "from it except seven.**\n\n"
   "**{IDENTITY}** **His left hand is on the lashed steering oar at the very bottom edge of the frame; "
   "his face is not in this frame and he does not look at the lens and does not speak.**\n\n"
   "0-2.995s: **the stars are all still out**, and the seven sit low and clear above the horizon.\n"
   "2.995-7.494s: **the stars begin to go out one at a time, unevenly**, the sky goes blue, and **the "
   "seven keep their height.**\n"
   "7.494-12.127s: **every other star is gone and the sky is grey-white, and the seven are still at the "
   "same height** — and the take ends on that.\n\n"
   "**The seven stars are a long-handled ladle: four of the bowl and three of the handle. They never "
   "move, never brighten, and never approach the horizon.** **The camera is the anchor: it does not cut "
   "away, does not cut back, and never leaves this sky.** **No clouds, no moon, no land, no bird, no "
   "other vessel, and no other constellation read as a shape.** **Nothing in this frame names the "
   "elapsed time: no date, no caption, no title card.** **No second person is in this frame at any "
   "distance or in any focus, and no woman is in it at all.** **This is a bronze-age sea before "
   "classical Greece: no made thing of any later age.** **This is a Japanese work.** No subtitles. No "
   "BGM.\n"
   "(One continuous take, one change: everything in the sky leaves except seven stars that do not "
   "move.)"),

 "visual_scene": (
   "The night sky above open water, seen from below, photographed as a film frame: **almost the whole "
   "frame is sky**, going from the blue of night to grey-white, with **seven bright stars in the shape "
   "of a long-handled ladle — four of the bowl and three of the handle — holding their position low and "
   "clear above the horizon**; the horizon line runs across the lower part of the frame and the seven "
   "sit above it, unmoved. **At the very bottom edge of the frame: the stern of the raft, a steering "
   "oar tied there and lashed, not fitted, and his left hand on it.** No clouds, no moon in this frame, "
   "no other constellation read as a shape, no land, no bird, no other vessel."),

 "visual_meta": (
   "Anamorphic lens with subtle oval bokeh and a gentle flare on the stars; a moderate depth of field; "
   "a graded palette of deep blue going to grey-white, with the seven stars the only hard points in it "
   "and the raft's stern at the bottom edge the only dark mass. Barked pine logs and coarse "
   "hand-twisted cordage at the very bottom edge; undyed wool with visible fibre; skin roughened and "
   "marked; even film grain over the whole sky. No painterly stroke, no airbrush, no plastic surface, "
   "no CGI look, no illustration. ⚠️ **The frame is almost all sky, and emptiness is the content** — "
   "the stars are subtracted from it one at a time until seven are left, and nothing in the frame "
   "measures how long that took."),

 "motion_prompt": (
   "Full animation, not limited. **The sky is the mover and the seven stars are the one thing that does "
   "not move.** **The stars go out one at a time, unevenly and irreversibly — each thins and then is "
   "gone, and none of them comes back** — while **the seven keep exactly their height, their spacing "
   "and their brightness from the first frame to the last.** The sky's colour travels in one direction "
   "only, from blue to grey-white, the low part whitening before the high part. **His left hand and the "
   "lashed oar at the bottom edge stay almost still.** **The camera pushes slowly toward the seven at a "
   "constant rate and never reaches them, and it never leaves the sky.** No motion blur smears, no "
   "stutter, no floaty weightless motion, no static frames — **the sky changes in every frame of the "
   "take.**"),

 "camera_prompt": (
   "Third person, **directly below, looking up** — the frame is the sky above the raft, with the "
   "horizon low in it and the raft's stern and his left hand at the very bottom edge. One event only: "
   "**a slow push toward the seven stars, short, at a constant rate, that never reaches them.** "
   "⚠️ **The camera is the anchor: it does not cut away, does not cut back, and never leaves this "
   "sky.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** — "
   "a slow push with a real rig's weight. ⚠️ **Neither a crane nor a Steadicam is used, and neither is "
   "needed** — this frame moves in one direction only, toward the seven. No handheld, no whip, no "
   "shake, no snap zoom, no rack focus, no unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water working against the raft's logs, and the low creak of "
   "hand-twisted cordage — the sounds of the only things in frame that are not sky.** "
   "⚠️ **There is no sky sound: the stars make none and the lightening makes none. This is the "
   "quietest frame of the work, and it is still not silent.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (time-fold) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②）。"
                        "⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ。**"
                        "⚠️ **参照集合の8鍵のうち、この1本の主題は `沈まない星` である。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water ＋ cordage ／ no music",
 "unresolved": [
   "⚠️ **この1本の `PLACE` が `沈まない星` であり、`海` ではないこと。**"
   "⚠️ **参照集合は `海` の3鍵も挙げている**（`海`・`海.geography`・`海.states.夜明け`）"
   "——**この空が海の上にあるからである。** "
   "⛔ **この仕様は、画に入るものを「水平線まで」と読んだ**——**水そのものは画に入らない。**"
   "⚠️ **この読みが正しければ、この1本の `place` は `沈まない星` である**"
   "（**この場所は、この作品でこの1本だけが使う**）。**記録からは、ここまでしか読めない。**",
   "⚠️ **`time-fold` の「固定の枠が本来の場合」と、`motion.quality` の「北斗へゆっくり寄る」の関係。** "
   "⚠️ **カードは逐語で「A fixed frame is the native case.」と言い、"
   "ショット記録は「カメラは三脚の上で、北斗へゆっくり寄る」と言う。**"
   "**この仕様は、押しを1回だけ許し、それ以外の動きを全部禁じる形にした**"
   "——**カードの「離れない」を破らない範囲である。** ⚠️ **押しを0にすべきかは、"
   "絵を見て決めることである。**",
   "⚠️ **彼の左手を画に入れたこと。****参照集合は `男.identity` を挙げているが、"
   "ショット記録の `motion.subject` は「空、星、そして明るくなっていく東の空」であり、"
   "彼に触れていない。**⚠️ **この仕様は、`沈まない星.geography` の逐語"
   "（「**the ladle is on the raft's left hand — the same side in every frame that holds it**」）と、"
   "`verse-2` の第五巻の註（舵を取りながら、一度も沈まない星座を左手に保つ）から、"
   "左手を下端に置いた。** ⚠️ **顔を入れないことが、この判断の条件である。**",
   "⚠️ **`l17` の長さについて。** 記録は「**この曲で最も短い行である**（`l04` と同位）」と書く。"
   "⚠️ **私が `bible.song.lines[].at` の差から出した数は、`l17` が 3.510秒、`l03` と `l04` が 3.511秒である**"
   "——**記録の「同位」は、この 0.001秒を丸めた言い方である。****この仕様は記録の側を採った**（記録が正である）。",
 ],
 "risks": [
   "⛔ **七つが動く、または明るさが変わる。** ⚠️ **この経路は「特別な星」を作りたがる**"
   "——**動かないことだけが主題である。**",
   "⛔ **時間が経っていることが見えない。** ⚠️ **星が減らなければ、この1本はただの星空である。**"
   "**12秒で、他の星が全部消えること。**",
   "⛔ **カットが入る。** ⚠️ **12秒の空は、この経路では途中で切り返したくなる**"
   "——**`time-fold` の主張は「一度も離れていない」である。**",
   "⚠️ **北斗が柄杓の形に描かれない。** ⚠️ **椀が四つ、柄が三つ、という数が要る**"
   "——**数が違えば、この1本は星座ではなく、点の集まりになる。**",
   "⚠️ **月が入る。** ⚠️ **夜明けの空を描けば、この経路は月を置く**"
   "——**`base` の逐語が禁じている。**",
   "**経過時間が名指される。** ⚠️ **字幕や日付はこの作品の床で禁じられているが、"
   "「夜明け」という語が画に入れば同じことである。**",
   "**左手が顔の大きさになる。** ⚠️ **画の下端の小さなものでなければ、この1本は彼の画になる。**",
 ],
}

if __name__ == "__main__":
    print("s19 content OK — keys:", len(C))
