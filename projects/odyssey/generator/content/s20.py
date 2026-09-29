# -*- coding: utf-8 -*-
"""odyssey-s20 — recognizing-world — 海 / 夜 / 6.942s. The island answers by going."""
import common as K


C = {
 "n": "s20",
 "title": "2度目の出発には、島の側が応える",
 "duration": "6.942",
 "format": "recognizing-world",
 "has_man": True,
 "segment": "chorus-2-1",

 "band": [
   "『永遠より遠い』 chorus-2「海」 / 離脱 / motion —— 2度目の出発には、島の側が応える",
   "遠い島の輪郭が波に合わせて一度だけ揺れ、それから消える。",
   "6.942秒、カメラは舟の上で島へ向かって回る——輪郭が消えるのが、切れ目である。",
   "島は在ることをやめ、彼は戻らない——航跡だけが後ろへ伸びる。",
 ],
 "header": """⚠️ **`l19`「死なない島を出て」の2度目である。** ⚠️ **言葉は `chorus-1` と一語も違わない。**
⛔ **この作品は役も同じにした**（`s13` の註を見る）——**差分は §6 の形式が持つ。**
⛔ **形式は `recognizing-world`**——**場所が、そこにいる者に反応し、反応が積み重なる。**
⚠️ **この形式をこの作品で使うのは、この1本だけである。****ゆえに「2度目」であることが、形式の側から保証される。**
⚠️ **1度目（`s13`）は島が黙って遠ざかり、この1本は島が応える。**
⚠️ **この1本の `time` は `夜` である。** 直前の `verse-2` は `夜明け` であった——⛔ **曲が `l14` から `l18` で暁を歌い、`l19` のサビで夜へ戻る。****この作品は曲に従った**（`bible.time_source: song`）。**時計には従っていない。**
⚠️ **切れ間は `l19` の歌い終わりである**（181.037–187.979。**行の長さが、そのままこの1本の長さである**）。
⚠️ **この仕様のショット記録は `shots/odyssey-s20.yaml` である。**""",

 "intent": "**同じ行の2度目に、別の何かを返せるか。** ⚠️ **`s13` が「意図」であり、この1本は「行為」である**"
           "——その差を、**形式の差だけで立てられるか。** "
           "⛔ **反応するのは場所であって、人ではない。****彼は振り向かない。**"
           "**これは「場所が認識する」という形式であり、「認識についての場面」ではない**"
           "（カードの逐語）。⛔ **切らない。1本は1つの画である。** "
           "⚠️ **変化は切れ目のコマで終わる**——**島が在ることをやめる。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、この作品で唯一 `recognizing-world` を名乗る**"
   "（⚠️ **`roster.json` の実測: 34本でこの形式を名乗るのは、この1本だけである**）。"
   "**場所が、そこにいる者に反応し、反応が積み重なる形式である。**"
   "⛔ **この作品では、それをするのは島である。****応えるのは島であり、"
   "応えることができないのは海である**——**`s15`・`s21`・`s22` の海は、彼に何も返さない。**"
   "⚠️ **ゆえにこの1本が、この作品の「もう一つの側」を一度だけ見せる。**"
   "⛔ **それでもこの1本の答えは、言葉ではない。****島は在ることをやめる。**"),

 "world_rules": K.world_rules(
   drop=(), tails={
     "answer": "⛔ **この1本では、返事が来る。****ただしそれは、彼にではなく、場所からである。**"
               "**島は在ることをやめる。****それ以外の何もしない**——**カードの `REFUSAL` がこれである。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "⚠️ **この1本で応えるのは女神ではない**——**島である。****この作品は、"
                "島と女神を別々に置いた。**",
     "name": "⚠️ **この1本に名は無い。**⚠️ **島は `死なない島` と歌われるが、この1本はその名を"
             "画面に出さない**——**在ることをやめるものが、名を持たない。**",
     "bow": "⚠️ **この1本に弓は無い。** **画面にあるのは、舟と、彼の背と、船尾に縛られた"
            "舵の櫂だけである。**",
     "places": "この1本が持つのは `海` である。⚠️ **島は場所ではない**——**この作品の `place` は6つであり、"
               "島はそのどれでもない**（`ledger.locations`）。**島は、この1本では輪郭としてだけ在り、"
               "そして輪郭でなくなる。**",
     "japanese": "⚠️ **この1本には歌がある**——`l19`「死なない島を出て」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **カードの逐語:「The sign is environmental, not social.** Other characters may not turn, "
     "greet, or react — that is a scene about recognition, not a setting that recognises.」"
     "**ゆえにこの1本では、彼は振り向かない。****振り向くのはカメラであって、人ではない。**",
     "⛔ **カードの逐語:「**The setting has a limit.** `REFUSAL` states what the place will not do "
     "even for this figure — the point past which the recognition stops. **A setting that does "
     "everything reads as an effect; a setting with a floor reads as a place with a character.**」"
     "**ゆえにこの1本には床が在る。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, photographed as a film frame, seen from the raft itself. **In the near "
     "ground, the raft's stern and the man's back, low in the frame; beyond it the water to the "
     "horizon; and at the horizon's far limit, the last edge of an island.** ⚠️ **No vessel of any "
     "kind other than the raft, no sail, no bird.** ⚠️ **The island is a line at the limit of seeing "
     "and nothing more — it has no detail, no shore, no interior, and it is not a place in the frame.**",
   "Color Language":
     "A narrow, graded palette: **the source is the stars and their reflection, so the waves are black "
     "and the reflected path alone is white.** ⚠️ **The island's outline is darker than the sky and "
     "darker than the water — it is a subtraction, not a shape with a colour of its own.** "
     "⚠️ **Nothing is lit apart from the place** — **one light only, and it is the starlight's; the "
     "shot has no second light.**",
   "Texture":
     "The raft under the frame — pine logs, coarse hand-twisted cordage, hewn planks; the water as "
     "**long low swells with no white water**, moving steadily in one direction, broken only by the "
     "raft's own wake; **and his coarse wool and skin in the near ground.** ⚠️ **The island's outline "
     "carries no texture at all: it is the one thing in this frame with no surface.** Film grain "
     "present and even.",
   "Rendering":
     "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, a gentle flare on "
     "the one reflected path. **Not a photograph's stillness: a film frame.** No illustration, no CGI "
     "look, no cartoon color.",
   "Visual Density": "Low, and it **decreases** over the shot: the frame begins with two things — the "
                     "raft and the island's outline — and ends with one. "
                     "⚠️ **この1本の密度は、経過とともに下がる。**",
   "Time": "`夜` — the source is the stars and their reflection on the water. ⚠️ **この4本（`s20`〜`s22`）は"
           "夜である**——**曲のサビが夜へ戻るからである**（`bible.time_source: song`）。"
           "**画の中に日付を与えるものは何も無い。**",
   "Atmosphere": "The hour in which the only light answers, and the land does not.",
 }),

 "subjects": [
   K.man_subject(
     behavior="⛔ **この1本で、彼は振り向かない。****彼は舟尾に立ち、左手を縛られた舵の櫂に置いている。**"
              "**背中が画の手前側の低いところにあり、それだけである。**"
              "⚠️ **島が消えても、彼は何もしない。****見も、聞きも、答えたともしない**"
              "——**カードの逐語:「**Other characters may not turn, greet, or react.**」**"
              "⚠️ **彼は口を開かず、レンズを見ない。**",
     may="背中の角度、左手の指の力の入り方、袖の落ち方、丸太の下の水の動き。",
     extra_notes=[
       "⛔ **この1本の主題は、彼ではなく、島が在ることをやめることである。**"
       "**彼が反応すれば、この1本は「認識についての場面」になり、"
       "「場所が認識する」という形式が壊れる。**",
       "⚠️ **彼はこの1本で一度も島のほうを見ない。****最初から最後まで、前を向いている**"
       "——**振り向くのはカメラだけである。**",
       "⚠️ **`s05` が立てた顔の基準から外れない。** ⚠️ **この1本は顔を写さない（背中と肩だけである）**"
       "——**それでも塊は §18 にまるごと入る。**",
     ]),
   {"name": "遠い島の輪郭",
    "ref": "**この1本の `SIGN` である。** ⚠️ **この作品に `島` という場所は無く、参照画像も無い**"
           "（裁定②）——**輪郭は、この1本では絵ではなく、減っていく線である。**",
    "appearance": "**見える限界にある、細い一本の線である。**⚠️ **岸も、木も、家も、内側も無い。**"
                  "**空より暗く、水より暗い**——**色を持たず、あるのは不在だけである。**"
                  "⚠️ **遠近の手がかりを一つも持たない。**",
    "behavior": "⛔ **輪郭は、この1本のあいだ一度だけ揺れる。****波の動きに合わせて、一度だけである。**"
                "**そして消える。****消えるときに、崩れもしないし、沈みもしない**"
                "——**在ることをやめるだけである。**",
    "continuity": "**Must preserve** — **見える限界にあること**、細いこと、"
                  "**岸も木も家も持たないこと**、**色を持たないこと**、"
                  "**そして「消える」であって「遠ざかる」でも「沈む」でもないこと**。"
                  "**May change** — 揺れの幅、消える速さ、そして消える前の最後の明るさ。",
    "notes": ["⛔ **カードの逐語:「**The recognition may be wrong.**」**——**この1本の認識は"
              "正しい。****島は彼を知っており、それが彼に対してすることは、在ることをやめることである。**",
              "⛔ **この1本の `SIGN` は、島ではなく、輪郭である。****島を描けば（岸、木、家）、"
              "この1本は場所の画になり、減っていく線の画にならない。**"]},
 ],

 "environment": {
   "location": "`海` — **この作品でいちばん多く写る場所である。** **カメラは舟の上にある。**"
               "**この1本の画には、水と、舟と、そして見える限界の一本の線がある。**"
               "⚠️ **`海.base` の逐語:「No land, no sail, no bird, no other vessel.」**"
               "——**この1本は、その逐語へ向かって進む。****最後のコマで、画はそれに一致する。**",
   "elements": "**長く低いうねり**（白波の無いもの）、**一つの方向へ絶えず動く水面**、"
               "**舟の航跡**、流れてくる海藻、**舟の船尾と、その上の彼の背**、"
               "**そして遠い島の輪郭**——**見える限界にある、色を持たない一本の線である。**"
               "⚠️ **他の船も、帆も、鳥も無い。**",
   "behavior": "⛔ **この1本の反応は、この層にある。****遠い島の輪郭が、波の動きに合わせて一度だけ揺れる。**"
               "**それから消える。** ⚠️ **海は彼に反応しない**——"
               "**反応するのは島の側であり、海の側ではない。**"
               "**航跡は後ろへ伸び続け、うねりは同じ速さで動き続ける。**"
               "⚠️ **島が消えても、水は変わらない。**",
 },

 "objects": [
   "**舟** — **この1本の地面である。**丸太、手で撚った縄、粗削りの板、"
   "**船尾に縛られた舵の櫂**、**何も張られていない短いマスト。** ⚠️ **この1本のあいだ、"
   "舟は前へ進み続ける。**",
   "**遠い島の輪郭** — **この1本の `SIGN` である。**⚠️ **揺れ、そして消える。**"
   "**この1本の出来事は、これである。**",
   "**航跡** — 舟の後ろへ伸びる。⚠️ **島が消えても、航跡は残る**"
   "——**この1本で、動いているものが動き続けるのは、これだけである。**",
   "**舵の櫂と、彼の左手** — **彼はこの1本では動かさない。**"
   "⚠️ **この1本の彼は、舵を取っているのでも、漕いでいるのでもない。**",
   "⚠️ **この作品の小道具4つのうち、この1本に来るのは舟だけである**（`ledger.props`）——"
   "**帆も、斧も、太陽の牛も、この1本の画には無い。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — **この1本には添付しない。彼女はこの1本に、四つの姿のどれとしても現れない。** "
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.夜`・`舟`・`舟.appearance`・`舟.negative` の8鍵である。"
                  "⚠️ **集合に `島` は無い**——**島はこの作品の場所ではない。**",
 "ref_extra": [
   "- ⚠️ **形式カード `recognizing-world` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; "
   "what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §8 に書いた5つの変数と、§16 に運んだカード自身の禁制である。**",
   "- ⚠️ **カードの逐語:「Its grammar is written into the `video-spec` skeleton — §4's environmental "
   "behaviour and §13 LIGHTING EVENTS.」**——**ゆえにこの1本では、§4 の `behavior` と §13 の `events` が"
   "文法の置き場である。****認識は、その2箇所に書かれる。**",
 ],

 "narrative": {
   "core": "**2度目の出発に、島の側が応える** — そして**応えることが、在ることをやめることである。**",
   "beginning": "**海と、遠い島の輪郭がある。****輪郭はまだ動かない。**"
                "⚠️ **この1.999秒は、輪郭が在るところである。**",
   "turn": "**輪郭が揺れる。****波の動きに合わせて、一度だけ。**"
           "⚠️ **場所が、ここで初めて応える。**",
   "peak": "**輪郭が消える。**",
   "pull": "⚠️ **島が在ることをやめるのが、切れ目のコマである。****海だけが残る**"
           "——**その瞬間に、`l19` の歌が終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.444秒.** 頭の1.999秒は**輪郭が在るところ**のために払われ、"
            "次の2.499秒は**揺れることに**払われ、**最後の2.444秒がこの1本の出来事である。** "
            "⚠️ **この作品は均平に配らない**（`L37` が敷き詰めを、§8 が不均等を検算する）。"
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**輪郭が消えるあいだも、うねりは動き続けている。**\n"
            "- ⚠️ **`recognizing-world` の5つの変数**（⚠️ 定義はカードの逐語である）:\n"
            "  - `FIGURE`＝who the setting recognises — **`男` である。**"
            "**この1本は「2度目の出発」であり、場所はその2度目に応える。**\n"
            "  - `SIGN`＝how the setting shows it has noticed — ⛔ **遠い島の輪郭が、"
            "波の動きに合わせて一度だけ揺れることである。**"
            "⚠️ **人の側の合図ではない**（カードの逐語:「**The sign is environmental, not social.**」）"
            "——**彼は振り向かない。****合図は、場所そのものの側にある。**\n"
            "  - `DEPTH`＝how far the recognition goes — **島が在ることをやめるまでである。**"
            "⚠️ **遠ざかるのでも、沈むのでもない**——**「在ることをやめる」が、この認識の深さである。**\n"
            "  - `REFUSAL`＝what the setting will not do — ⛔ **島は、起きない。話さない。彼を引き止めない。"
            "そして、自分を作っている水以外のもので答えない。**"
            "⚠️ **カードの逐語:「**A setting that does everything reads as an effect; a setting with a "
            "floor reads as a place with a character.**」**——**この床が、この1本を効果ではなく場所に"
            "している。** ⚠️ **別れの場面にも、赦しにも、声にもならない。**\n"
            "  - `DURATION`＝clip length — **`6.942s`。**",

 "actions": [
   ("ACT_SHOW", "海と、遠い島の輪郭がある。",
    "**同じであり、輪郭はまだ動かない。** ⚠️ **この1本の出発点が、ここで立てられる。**"),
   ("ACT_STIR", "輪郭は静止している。",
    "**輪郭が一度だけ揺れる**——**波の動きに合わせて、一度だけである。**"),
   ("ACT_CEASE", "輪郭がある。",
    "**輪郭が無い**——**海だけが残る。** ⚠️ **在ることをやめるのが、切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **on the raft, low, behind him** — the frame holds his back and shoulder "
               "in the near ground, the water beyond, and **the horizon at the far limit of seeing.** "
               "⚠️ **この1本のカメラは、人ではなく、島へ向く。**",
   "events": "One event only. `0-1.999s` — **the frame looks out at the horizon and holds, with the "
             "outline at its far limit**; then `1.999-6.942s` — **a slow turn toward the island's "
             "outline, at the swell's own pace, and it does not stop when the outline goes**"
             "——**動機は「島が応えるのを見ること」であり、それだけである。**"
             "⚠️ **彼は振り向かない。****振り向くのはカメラである**"
             "（カードの逐語:「**Other characters may not turn, greet, or react.**」）。",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends none of "
               "them** — ⚠️ **この1本のカメラは舟の上で向きを変えるだけであり、"
               "持ち上がる理由も、横へ流れる理由も、手の内側へ入る理由も無い。**"
               "⚠️ **手ぶれをしない。** ⚠️ **一度も止まらない**——"
               "**輪郭が消えたあとも、回り続けている。** "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and **no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、島である。**⚠️ **彼はこの1本で動かない。**"
              "**うねりが舟を動かし、舟が彼を動かす**——**彼自身は、舵を動かさない。**",
   "object": "⛔ **遠い島の輪郭が、一度だけ揺れ、そして消える。**"
             "**舟がうねりに合わせて上下する。****航跡が後ろへ伸び続ける。**"
             "⚠️ **舵の櫂は動かない。****彼の左手も動かない。**",
   "environment": "**うねりが同じ方向へ、同じ速さで動き続ける。**"
                  "**水面の反射の道が、星の下で揺れる。**"
                  "⚠️ **島が消えても、海の側は何も変えない**"
                  "——**反応は一度だけで、それは島の側で起きる。**"
                  "⚠️ **海は彼に反応しない。**",
   "weight": "**舟は重く、うねりは低い。****島の側には重さが無い**"
             "——**輪郭は、消えるときに何も残さない。** ⚠️ **この軽さが、この1本の答えである。**",
   "inertia": "⛔ **島の輪郭は、遅れて消える。****揺れてから消えるまでに間がある。**"
              "⚠️ **その間が、この1本の真ん中である。** ⚠️ **何も瞬間には止まらない。**",
   "acceleration": "**加速しない。****カメラの回り方も、うねりの速さも一定である。**"
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この6.942秒に、止まったフレームは"
               "一つも無い**——**輪郭が静止して見えるあいだも、水は動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**消えることは、打撃ではない。**"
             "**音を立てない変化である。**",
 },

 "emotion": {
   "arc": "**同じ一行の2度目に、返事が来ること。**⚠️ **ただし返事は、彼に対してではない。**"
          "**場所が在ることをやめることであり、それは別れではなく、"
          "場所が場所であることをやめることである。** "
          "⛔ **感傷にしない。****彼は振り向かない。****ゆえにこの1本には、別れの顔が無い。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****輪郭が揺れ、そして消えることである。**"
             "⚠️ **`s13`（1度目）は島が黙って遠ざかる。****この1本は、島が応える。**"
             "**その差が、この1本の感情である。**",
 },

 "lighting": {
   "base": "**夜である。****光源は星と、その水面の反射だけである。****波は黒く、反射の道だけが白い**"
           "（`ledger.locations.海.states.夜` の逐語）。"
           "⚠️ **この1本の光源は一つであり、それは星である。**"
           "⚠️ **月も、火も、灯も無い。**",
   "events": "⛔ **この1本の `events` は、カードの文法の置き場である**"
             "（カードの逐語:「Its grammar is written into … §13 LIGHTING EVENTS」）。"
             "**One, and it runs the second half of the shot.** "
             "**島の輪郭は、空より暗く、水より暗い**——**ゆえにその消失は、"
             "光が増えることではなく、光が減ることである。**"
             "⚠️ **光源そのものは動かない。**"
             "⚠️ **様式カードの逐語:「The grade holds for the whole shot — a colour temperature that "
             "swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水が舟の丸太に当たる音、縄の鳴る音。****そして、島が消えるときに何も鳴らないこと。**"
          "⚠️ **消える音を作らない**——**島には音の側が無い。**"
          "⚠️ **彼は何も言わないが、無音ではない**——**水の音が、この1本の音の側の主題である。**",
   "music": K.NO_MUSIC + " ⚠️ **そしてこの1本には、歌が在る**——`l19`「死なない島を出て」であり、"
            "**行の長さが、そのままこの1本の長さである**（181.037–187.979）。"
            "**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜の外海。**水、木、縄、風。** ⚠️ **鳥の声は無い。****呼ぶ声も、"
                  "別れの言葉も無い**——**この1本には、人の側の音が一つも無い。** "
                  "⚠️ **島の側にも音が無い。****この1本で応えるものは、静かである。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="**体格・肌・髪・髭・顔・傷・着ている一枚と、着ていないすべて・裸足であること。** "
                "⚠️ **この1本は彼の背中だけを写す**——**それでも塊は §18 にまるごと入る。**",
     may="背中の角度、左手の指の力の入り方、袖の落ち方、丸太の下の水の動き。"),
   "spatial": "**舟の上である。****彼は舟尾に立ち、カメラはそのすぐ後ろにある。**"
              "**島は見える限界にあり、どの方向にも陸は無い**——"
              "**この1本の画は、その逐語へ向かって進む。**"
              "⚠️ **この1本で、この海が `s03` の海と同一であることが保たれる**"
              "（`海.geography` の逐語:「**the same waterline and the same horizon appear in both**」）。",
   "temporal": "**夜である。**⚠️ **曲がサビで夜へ戻ったからである**（`bible.time_source: song`）"
               "——**`verse-2` の夜明けから、時計は逆戻りする。****この作品は曲に従っており、"
               "時計には従っていない。** 画の中に日付を与えるものは何も無い。",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は星の光だけである。**"
             "⚠️ **この1本は `recognizing-world` を名乗るが、その文法は §15 から何も免除しない**"
             "——**この1本は、場所も時刻も一つであり、連続性は全部そのままである。**"
             "**`§15` に例外を求めるのは `coexisting-realities`（`s22`）だけである。**",
   "motion": "Full animation, not limited. **輪郭が揺れ、消え、うねりが動き、カメラが回る。** "
             "⚠️ **彼は動かない。** **この対比が、この1本の全体である。**",
   "sound": "水、木、縄。**音楽なし。言葉なし。** ⚠️ **主題歌はこの1本のあいだ鳴っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**この1本には彼が居る**——**ゆえに女神の禁制は、他人の形で来る。**"
     "**島を、彼女の姿で説明しない。**")) + [
   "**No second person in frame at all** — no companion, no crowd, no figure at any distance, "
   "**no one on the island and no one on the water.**",
   "⛔ **No character reacting in place of the setting** (逐語, `recognizing-world` の `## Negative`). "
   "⚠️ **彼は振り向かない。****見もしない。****何も言わない。**",
   "**No cut between the unrecognised and the recognised state** (逐語, `recognizing-world` の "
   "`## Negative`). ⚠️ **揺れから消失まで、一続きである。**",
   "**No on-screen caption and no voice-over announcing recognition** (逐語, `recognizing-world` の "
   "`## Negative`). ⚠️ **島の名も、島へ向けた言葉も、画面にも音にも出ない。**",
   "**No blanket mood change** (逐語, `recognizing-world` の `## Negative`). "
   "⚠️ **海は何も変えない**——**変わるのは輪郭だけである。**",
   "**No setting without a floor** (逐語, `recognizing-world` の `## Negative`). "
   "⛔ **島は、起きない。話さない。引き止めない。水以外のもので答えない。**",
   "**No boat, no ship, no hull, no other vessel** (逐語, `ledger.props.舟.negative` の "
   "`no boat, no ship, no hull`、そして `ledger.locations.海.base` の `no other vessel`)。"
   "⚠️ **この1本の海には、彼の筏しか無い。**",
   "⚠️ **この1本の舟は筏である**——`ledger.props.舟.negative` の逐語は「**no boat, no ship, no hull, "
   "no keel, no planking**」であり、**この禁制は、筏を舟として描くことを禁じている。**"
   "**画の近景にあるのは、その筏である**（`ledger.props.舟.appearance` の逐語:「A raft, not a "
   "boat.」）。",
   "**No sail is set on the raft in this frame, and no bird appears** (逐語, `ledger.locations.海.base` "
   "の `no sail`, `no bird`).",
   "**No wheel, no helm, no rudder, no tiller** — ⚠️ **舵は船尾に縛られた一本の櫂である。**",
   "**No shore, no beach, no trees, no houses, no interior on the island** — ⛔ **島は、"
   "見える限界の一本の線であり、場所ではない。**",
   "**No island that rises, approaches, grows, glows, or speaks.** ⛔ **消えるだけである。**",
   "**No white water, no breaking crest, no spray** — **この海は白波を立てない。**",
 ],

 "must": [
   "**2度目の出発に、島の側が応えること** — そして**応えることが、在ることをやめることである。**",
   "⛔ **彼が振り向かないこと。****反応するのは場所であって、人ではない。**",
   "⛔ **この1本に床が在ること** — **島は起きない。話さない。引き止めない。水以外のもので答えない。**",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.**",
   "⛔ **切らない。** **1本は1つの画である。****カメラは1回だけ動く。**",
   "⚠️ **輪郭の消え方は「在ることをやめる」であること** — **遠ざかるのでも、"
   "沈むのでも、崩れるのでもない。**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **彼はレンズを見ず、口を開かない。**",
   "⚠️ **変化は最後のコマで終わる** — **海だけが残るところで、この1本は終わる。**",
   "⚠️ **`recognizing-world` の5つを満たすこと** — `FIGURE` は男、`SIGN` は輪郭の一度の揺れ、"
   "`DEPTH` は在ることをやめるまで、`REFUSAL` は島がしないこと、`DURATION` は 6.942秒。",
 ],

 "prefer": "The night held dark, the waves black and only the reflected path white; the raft kept small "
           "and low in the near frame; the outline kept thin and without texture; **the removal kept "
           "quiet, with no sound and no glow.**",
 "allow": "The outline wavering once with the swell and no more; the outline going darker as it goes; "
          "the wake lengthening throughout; a gentle flare on the reflected path; **a slow turn that "
          "keeps going after the outline is gone.**",

 "priorities": [
   "⛔ **彼が振り向かないこと。** **反応させれば、この1本は「認識についての場面」になり、"
   "形式が壊れる。**",
   "⛔ **この1本に床が在ること。** **島が何もしないことが、この1本を場所にしている。**",
   "⛔ **消え方が「在ることをやめる」であること** — **遠ざかるのでも、沈むのでもない。**",
   "⚠️ **島を描き込まないこと** — **岸も、木も、家も、内側も無い。****見える限界の一本の線である。**",
   "⚠️ **海を変えないこと** — **変わるのは輪郭だけである。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "**No second person, at any distance, in any focus.**",
   "**光は星の光だけであること** — 月も、火も、灯も無い。",
   "⚠️ **`s13` との差が、形式の差だけで立っていること** — **言葉も役も同じである。**",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `recognizing-world` を名乗るが、その禁制（`no character reacting in place of the "
   "setting`・`no cut between unrecognised and recognised states`・`no setting without a floor` ほか）は "
   "§16 に在って、ここには無い。** **ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 6.942-second cinematic take (16:9) of open sea at night, one clip, one continuous take, shot from "
   "the raft itself, one change: **the setting answers — and its answer is to stop being there.**\n\n"
   "**{IDENTITY}** **His back and shoulder are low in the near ground and he is facing away; he does "
   "not turn, he does not look toward the island, he does not speak, and he does not look at the "
   "lens.**\n\n"
   "0-1.999s: **the sea and, at the far limit of seeing, the last edge of a distant island — a thin "
   "line, darker than the sky and darker than the water, with no shore, no trees, no houses and no "
   "interior.** The outline does not move yet.\n"
   "1.999-4.498s: **the outline wavers — once, with the swell — and settles.**\n"
   "4.498-6.942s: **the outline goes.** It does not recede and it does not sink: **it stops being "
   "there.** **Only the sea is left** — and the take ends on that.\n\n"
   "**What answers is the setting, not a character: the man never turns and never reacts.** **The island "
   "will not rise, will not speak, will not keep him, and will not answer with anything but the water "
   "it is made of — the setting has a floor.** **The camera turns toward the island and keeps turning "
   "after the outline is gone.** **No other vessel, no sail on the raft, no bird, no white water.** "
   "**No second person is in this frame at any distance or in any focus, and no woman is in it at "
   "all.** **This is a bronze-age sea before classical Greece: no made thing of any later age.** "
   "**This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the island answers by ceasing to be there.)"),

 "visual_scene": (
   "Open sea at night seen from the raft itself, photographed as a film frame: **the raft's stern and "
   "the man's back low in the near ground** — unseasoned pine logs still barked and uneven, lashed with "
   "coarse hand-twisted cordage, a steering oar tied at the stern and lashed, not fitted, **and a short "
   "mast of a trimmed pine trunk stayed with rope with nothing set on it.** **Beyond the raft the water "
   "is black, broken only by the raft's own wake and by one broken path of reflected starlight; at the "
   "far limit of seeing, at the horizon, a thin dark line — the last edge of a distant island, with no "
   "shore and no interior.** No land in any other direction, no other vessel, no sail, no bird, no "
   "moon."),

 "visual_meta": (
   "Anamorphic lens with subtle oval bokeh and a gentle flare on the reflected path; a moderate depth "
   "of field with the horizon held just inside it, so that the island's outline stays a line and never "
   "resolves; a graded palette of black water and a sky one shade above it, with one white reflected "
   "path and one darker line at the horizon. Barked pine logs and coarse hand-twisted cordage at the "
   "raft's edge; undyed wool with visible fibre and a worn shoulder seam; skin roughened and marked; "
   "even film grain over everything. No painterly stroke, no airbrush, no plastic surface, no CGI "
   "look, no illustration. ⚠️ **The frame loses one of its two things over the shot** — it begins with "
   "the raft and the island's outline, and ends with the raft alone."),

 "motion_prompt": (
   "Full animation, not limited. **The island's outline is the mover, and it moves once.** "
   "**It wavers with the swell — a single waver, small — and then it goes; and going, it does not "
   "recede, does not sink and does not break up: it stops being there.** The sea does not change when "
   "it goes: **the swell keeps running at the same rate and the wake keeps lengthening behind the "
   "raft**, and the reflected path keeps moving on the water. **The man does not move: his back stays "
   "as it is, his left hand stays on the lashed oar, and he never turns.** **The camera turns slowly "
   "toward the outline at the swell's own pace and keeps turning after the outline is gone, and it "
   "never stops.** No motion blur smears, no stutter, no floaty weightless motion, no static frames — "
   "**the water moves in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **on the raft, low, behind him** — the frame holds his back and shoulder in the near "
   "ground, the water beyond, and the horizon at the far limit of seeing. One event only: **a slow turn "
   "toward the island's outline, at the swell's own pace, that does not stop when the outline goes.** "
   "⚠️ **The move is motivated by looking toward what is answering; the frame turns and he does not.** "
   "⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot spends none of them** — the "
   "camera turns where it stands, on the raft, and never rises, never travels laterally and never "
   "closes in. No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, no "
   "unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water working against the raft's logs and the low creak of "
   "hand-twisted cordage.** ⚠️ **Nothing sounds when the island goes — there is no sound side to the "
   "outline, and inventing one would make the shot an effect rather than a place.** "
   "⚠️ **He says nothing, but this shot is not silent: the water is the subject of this shot's sound.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (recognizing-world) ／ "
                        "REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②）。"
                        "⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ。**"
                        "⚠️ **参照集合の8鍵のうち、この1本の場所は `海`、乗っているものは `舟` である。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water ＋ cordage ／ no music",
 "unresolved": [
   "⛔ **`ledger.locations.海.base` は逐語で「No land … visible in any direction, including "
   "behind」と言い、この1本のビートは「遠い島の輪郭」から始まる。**"
   "⚠️ **この仕様は、記録のビートを採った**（**記録が正である**）——"
   "**ただし輪郭を「見える限界の、色を持たない一本の線」に限り、"
   "そしてこの1本の出来事をその消失に置くことで、最後のコマで画は `base` の逐語に一致する。**"
   "⚠️ **それでも、最初の1.999秒は `base` の逐語と食い違っている。****この食い違いを、"
   "この仕様は消していない。**",
   "⚠️ **島の輪郭を描き込まないと読んだこと。** ⚠️ **ビートは「遠い島の輪郭」としか言わず、"
   "岸も木も家も挙げていない。****この仕様は、それを「見える限界の一本の線」と読んだ**"
   "——**描き込めば、この1本は場所の画になり、カードの `SIGN`（環境の側の合図）が、"
   "風景の説明になる。** ⚠️ **どこまで描くかは、絵を見て決めることである。**",
   "⚠️ **認識が正しいと読んだこと。** カードは逐語で「**The recognition may be wrong.**」と言う"
   "——**この1本の認識は当たっている、とこの仕様は読んだ**"
   "（**島は彼を知っており、そのうえで在ることをやめる**）。"
   "⚠️ **誤認として読むこともできる**（**消えたのは島ではない、という読みである**）。"
   "**どちらかは記録からは読めない。****この仕様は、`unit.after` の逐語"
   "（「**島は、もう在ることをやめている。**」）の側を採った。**",
 ],
 "risks": [
   "⛔ **彼が振り向く。** ⚠️ **この経路は、島が消える画に、人を振り向かせる**"
   "——**カードの禁制がそれを禁じている。****この1本の形式はそこに懸かっている。**",
   "⛔ **島が描き込まれる。** ⚠️ **岸、木、家、灯が入れば、この1本は別の作品になる。**",
   "⛔ **島が遠ざかる、または沈む。** ⚠️ **この経路は「消える」を「遠ざかる」に写す。**"
   "**在ることをやめることだけが、この1本の出来事である。**",
   "⚠️ **別れの感情が入る。** ⚠️ **彼が振り向かず、音が鳴らなければ、感情は場所の側にだけ残る。**"
   "**感傷になれば、カードの床が消える。**",
   "**他の船が入る。** ⚠️ **夜の海の画は、この経路では灯を足したくなる**"
   "——**`海.base` が禁じている。**",
   "**「認識」が字幕になる。** ⚠️ **島の名や、彼の心情が字になれば、この1本は説明である。**",
   "**背中が顔になる。** ⚠️ **彼が横を向けば、この1本は彼の画になる**"
   "——**参照画像が1枚も無いので、守る道具は英文だけである。**",
 ],
}

if __name__ == "__main__":
    print("s20 content OK — keys:", len(C))
