# -*- coding: utf-8 -*-
"""odyssey-s21 — impossible-camera — 海 / 夜 / 6.143s. The whole sea, and the raft as a point."""
import common as K


C = {
 "n": "s21",
 "title": "海を渡る——海の全体と、その上の舟とを、同じ画に",
 "duration": "6.143",
 "format": "impossible-camera",
 "has_man": True,
 "segment": "chorus-2-2",

 "band": [
   "『永遠より遠い』 chorus-2「海」 / 運動 / motion —— 海を渡る——海の全体と、その上の舟とを、同じ画に",
   "舟が水の上にあり、カメラが上がるにつれて海の全体と一つの点になる。",
   "6.143秒、カメラは高さを上げ続ける——舟が点になるのが、切れ目である。",
   "他の船は一隻も無く、鳥も帆も無い——動くのは、波とこの一点だけである。",
 ],
 "header": """⚠️ **`l20`「海を渡る」の2度目である。** ⚠️ **役は `運動` で、`s14` と同じである。**
⛔ **差分は形式が持つ**——`s14` は舳先の高さであり、**この1本は在りえない高さである。**
⛔ **形式は `impossible-camera`。** ⚠️ **この作品で4本あるうちの2本目である**（`s11` の註を見る）。
⚠️ **`s28`（`l29`「海を渡る」の3度目）は、この1本と対になる**——**`s21` は上から、`s28` は下から。****同じ海を、二つの在りえない視点で挟む。**
⛔ **この作品の `海` は、この1本で最も広く出る。****34本の中で、この1本だけが海の全体を持つ。**
⚠️ **この1本の `time` は `夜` である。****光源は星だけであり、海は黒い**——**ゆえに「海の全体」は、広さではなく、暗さとして立つ。**
⚠️ **切れ間は `l20` の歌い終わりである**（187.979–194.122。**行の長さが、そのままこの1本の長さである**）。
⚠️ **この仕様のショット記録は `shots/odyssey-s21.yaml` である。**""",

 "intent": "**海の大きさを、一度だけ正面から見せられるか。** ⚠️ **壮大さは、広さではなく、着かなさから来る。** "
           "⛔ **この1本はカメラ移動ではない。****「カメラはどこかに居る」という前提が外れている**"
           "（カードの逐語）。**この1本が組むのは、視点の運動ではなく、視点の存在である。**"
           "⛔ **切らない。****この上昇は一続きである。** "
           "⚠️ **変化は切れ目のコマで終わる**——**舟が点になる。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、この作品の「海」を、初めて全体として置く。**"
   "⚠️ **実測: この作品で `place` が `海` であるのは19本である**（`roster.json`）——"
   "**その19本のうち、海の全体を持つのはこの1本だけである**"
   "（記録の逐語:「**34本の中で、この1本だけが海の全体を持つ。**」）。"
   "**この1本だけが、水を一枚の面として持つ。**"
   "⛔ **そしてそれは、彼を小さくするためではない。**"
   "**この1本が着くのは、距離である**——**この作品で初めて、距離が見える。**"
   "⚠️ **`s28` が下から同じことをする**——**この作品は、同じ海を二つの在りえない視点で挟む。**"),

 "world_rules": K.world_rules(
   drop=(), tails={
     "answer": "⚠️ **この1本には彼が居る**（**舟の上に、点として**）。****それでも返事は無い**"
               "——**海は大きいが、それは答えではない。****広さは、彼に何も返さない。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "⚠️ **この高さは、与えられたものではない**——**誰の視点でもない。**"
                "**この作品は、その持ち主を名指さない。**",
     "name": "⚠️ **この1本に名は無い。**⚠️ **海も、舟も、彼も、どこにも書かれないし、呼ばれない。**",
     "bow": "⚠️ **この1本に弓は無い。**⚠️ **この高さからは、彼が何を持っているかも見えない**"
            "——**見えるのは、舟の上の小さな点だけである。**",
     "places": "この1本が持つのは `海` である。⚠️ **この1本は、この場所を離れない**"
               "——**高さは変わるが、場所は変わらない。**"
               "**視点は上がるが、海の上にとどまる。**",
     "japanese": "⚠️ **この1本には歌がある**——`l20`「海を渡る」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **この作品に他の船は一隻も無い**（`bible.negative_base` の逐語:「**no boat, no ship, no "
     "hull, no other vessel**」）。**海は空である。**"
     "⚠️ **この1本は、その空をいちばん広く写す1本である**——**ゆえにこの1本で、"
     "その禁制がいちばん効く。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, photographed as a film frame, **from a height at which the whole sea is one "
     "surface.** **The surface runs from the near edge to the horizon and is broken by one thing: the "
     "raft's wake, a single long line, with the raft itself at the head of it as a point.** "
     "⚠️ **No land, no sail, no bird, no other vessel, and nowhere in the frame any support for the "
     "viewpoint** (逐語, `ledger.locations.海.base`).",
   "Color Language":
     "A narrow, graded palette and almost no values in it: **the water is black, the sky is a shade "
     "above it, and the reflected starlight is the one white thing** — a path that becomes a line and "
     "then a scratch as the frame rises. ⚠️ **At the end the frame is two darks and one mark.** "
     "⚠️ **Nothing is lit apart from the place** — **one light only, and it is the starlight's.**",
   "Texture":
     "From this height the swell stops reading as swell: **long low ridges with no white water, running "
     "steadily in one direction, so evenly that the surface reads as one material.** "
     "⚠️ **The raft's logs and cordage cease to be readable within the first seconds** — **by the end "
     "there is no texture in the frame except the water's own movement and the wake.** Film grain "
     "present and even.",
   "Rendering":
     "Photographic — anamorphic optics, a deep focus at the end so that the surface and the horizon are "
     "both sharp, subtle oval bokeh, the faintest flare on the reflected path. "
     "⚠️ **No fisheye distortion and no wide-angle warp standing in for the height** "
     "(逐語, `impossible-camera` の `## Negative`). **A real lens, at a height nobody can hold.**",
   "Visual Density": "Low, and it **decreases** over the shot: the frame begins with a raft, its wake "
                     "and the water near it, and ends with **one surface, one horizon and one mark.** "
                     "⚠️ **この1本の密度は、上がるほど下がる。**",
   "Time": "`夜` — the source is the stars and their reflection on the water. **The waves are black and "
           "the reflected path alone is white** (逐語, `ledger.locations.海.states.夜`). "
           "**画の中に日付を与えるものは何も無い。**",
   "Atmosphere": "The hour in which the sea can only be seen by losing the raft.",
 }),

 "subjects": [
   K.man_subject(
     behavior="⚠️ **この1本で彼は点である。****最初の1.499秒には、舟尾に立って左手を舵の櫂に置いている**"
              "——**そこから先は、舟と一緒に小さくなっていく。**"
              "⚠️ **この1本のあいだ、彼は動かない。****動くのは海と、視点だけである。**"
              "⚠️ **彼は口を開かず、レンズを見ない。**",
     may="背中の角度、左手の位置、そして舟と一緒に小さくなること。",
     extra_notes=[
       "⛔ **参照集合が `男.identity` を挙げているので、舟は無人にしない。**"
       "**この作品の筏は彼が作ったものであり、空の筏は嘘である。**"
       "⚠️ **それでもこの1本は、彼を一度も近くで写さない**——"
       "**最初から、舟の一部として写す。**",
       "⚠️ **彼を大きくしないこと。** ⚠️ **この1本の主題は距離であり、"
       "距離は彼が小さくなることで立つ。**",
       "⚠️ **`s05` が立てた顔の基準から外れない。** ⚠️ **この1本は彼を近くで写さないが、"
       "塊は §18 にまるごと入る。**",
     ]),
   {"name": "海の全体",
    "ref": "**この1本の `EYE` が立つ面である。** ⚠️ **参照は `海` の `base`・`geography`・"
           "`states.夜` である**——**この作品に参照画像は無い**（裁定②）。",
    "appearance": "**一つの面である。****長く低い稜が、白波を立てずに、一つの方向へ等しく走っている**"
                  "——**その等しさで、水は一つの材質として読める。**"
                  "**その面を破るものが一つだけある**——**舟の航跡であり、"
                  "その先頭に舟が点としてある。**"
                  "⚠️ **陸も、帆も、鳥も、他の船も無い。**",
    "behavior": "**面は同じ方向へ、同じ速さで動き続ける。**"
                "⚠️ **高さが上がっても、面は読み取れるままである**"
                "（`impossible-camera` の逐語:「**its scale and physics are its own**」）"
                "——**平たくなっていくが、別のものにはならない。**"
                "**航跡は長い一本の線であり、舟はその先頭である。**",
    "continuity": "**Must preserve** — **一つの方向への等しい流れ**、**白波の無いこと**、"
                  "**面を破るものが航跡だけであること**、**水平線が水平であること**、"
                  "**そして舟が航跡の先頭にあること**。"
                  "**May change** — 面の見え方（高さによって平たくなる）、舟の大きさ、"
                  "航跡の長さ、そして反射の道の細さ。",
    "notes": ["⛔ **他の船を一隻も入れないこと。** ⚠️ **高い視点の海の画は、"
              "この経路がいちばん自然に船を足すところである**"
              "——**`bible.negative_base` の逐語と §16 の禁制の両方に在る。**",
              "⚠️ **魚眼にしないこと。****この1本の高さは、歪みではなく、"
              "支えの無さで立つ。**"]},
 ],

 "environment": {
   "location": "`海` — **この作品でいちばん多く写る場所である。**"
               "⚠️ **この1本はその全体を持つ唯一の1本である。****「海の全体が入る」は、"
               "この1本の到着そのものである。**"
               "**陸はどの方向にも見えない**（`海.geography` の逐語）"
               "——**この1本の画には、地平線の向こうにも何も無い。**",
   "elements": "**長く低い稜**（白波の無いもの）、**一つの方向へ等しく走る面**、"
               "**舟の航跡**——**長い一本の線である**、**その先頭の舟**、"
               "**空と、星と、その水面の反射の道。**"
               "⚠️ **他の船も、帆も、鳥も、陸も、そして視点を支えるものも無い。**",
   "behavior": "**面は同じ方向へ、同じ速さで動き続ける。**"
               "**航跡は後ろへ伸び続け、舟はその先頭にある。**"
               "⚠️ **海は彼に反応しない**——**この1本の海は、彼を認識もしないし、"
               "まして応えもしない**（**応えるのは `s20` の島だけである**）。"
               "⚠️ **視点が上がっても、水は何も変えない。****変わるのは、"
               "水の見え方だけである。**",
 },

 "objects": [
   "**舟** — **この1本では、最初は近く、最後は点である。**"
   "⚠️ **丸太も、縄も、舵の櫂も、この1本では最初の1.499秒でしか読めない。**"
   "**それでも、この1本の航跡の先頭にあるのは、彼の舟である。**",
   "**航跡** — ⛔ **この面を破るものは、航跡と、流れてくる海藻だけである**"
   "（`ledger.locations.海.base` の逐語:「the surface broken only by the raft's own wake and by weed passing」）。"
   "****長い一本の線であり、"
   "高さが上がるほど、面の中でいちばん長く残る。**"
   "⚠️ **この1本の航跡は、この1本の時間そのものである**——**6.143秒で、舟はこれだけ進んだ。**",
   "**短いマスト** — 刈り込んだ松の幹であり、縄で支えてある。⚠️ **この1本には何も張られていない**"
   "——**そして最初の1.499秒を過ぎれば、これも点の中に消える。**",
   "**星と、その反射の道** — 空と、水面の一本の道。⚠️ **この1本の唯一の明るいものである。**",
   "⚠️ **この作品の小道具4つのうち、この1本に来るのは舟だけである**（`ledger.props`）——"
   "**帆も、斧も、太陽の牛も、この1本の画には無い。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — **この1本には添付しない。彼女はこの1本に、四つの姿のどれとしても現れない。** "
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.夜`・`舟`・`舟.appearance`・`舟.negative` の8鍵である。"
                  "⚠️ **集合が `男.identity` を挙げているので、この1本の舟は無人ではない**"
                  "——**それでも彼は、この1本では点である。**",
 "ref_extra": [
   "- ⚠️ **形式カード `impossible-camera` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; "
   "what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §8 に書いた5つの変数と、§16 に運んだカード自身の禁制である。**",
   "- ⚠️ **カードの逐語:「Its grammar is written into the `video-spec` skeleton — §10 CAMERA — which "
   "asks for timing, movement, target and speed; this card asks what the viewpoint *is*, which that "
   "section has no field for.」**——**ゆえにこの1本では、§10 の `language` と `events` が"
   "文法の置き場である。****視点が何であるかは、そこに書かれる。**",
   "- ⚠️ **この作品で `impossible-camera` を使うのは4本であり、この1本はその2本目である。**"
   "**`s11` が1本目であり、`s28` がこの1本と対になる**——**`s21` は上から、`s28` は下から。**",
 ],

 "narrative": {
   "core": "**海の全体と、その上の舟とが、同じ一つの画に入る** — そして**舟は点である。**",
   "beginning": "**舟と、その周りの海。****まだ近い。**"
                "⚠️ **この1.499秒は、舟が舟として読めるところである。**",
   "turn": "**視点が上がる。****舟が小さくなる。****航跡だけが長い。**"
           "⚠️ **ここで、水が面になりはじめる。**",
   "peak": "**海の全体が入る。**",
   "pull": "⚠️ **舟が点になるのが、切れ目のコマである。****面と、水平線と、"
           "一つの印だけが残る**——**その瞬間に、`l20` の歌が終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.144秒.** 頭の1.499秒は**舟が近いこと**のために払われ、"
            "次の2.500秒は**上がることに**払われ、**最後の2.144秒がこの1本の到着である。** "
            "⚠️ **この作品は均平に配らない**（`L37` が敷き詰めを、§8 が不均等を検算する）。"
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**舟が点になるあいだも、面は動き続けている。**\n"
            "- ⚠️ **`impossible-camera` の5つの変数**（⚠️ 定義はカードの逐語である）:\n"
            "  - `EYE`＝the viewpoint that cannot exist — ⛔ **「海の全体が一つの面であり、"
            "舟がその上の点である」高さである。****そしてこの高さには、支えが一つも無い**"
            "——**マストも、崖も、鳥も、岩も、機械も無い。****これがこの視点の在りえなさである。**\n"
            "  - `ENTRY`＝how the shot arrives at it — ⛔ **カードの逐語:「**The entry is stated.** … "
            "An unstated entry reads as a continuity error in the previous shot rather than as this "
            "grammar.」**——**ゆえにこの1本は、舟の甲板の高さから始まる。****人が立てる高さである。**"
            "**そこから、カットなしに上がる。****入口は、"
            "前のショットの続きとして読める高さに置かれている。**\n"
            "  - `PATH`＝what the viewpoint travels through — **舟の上の空気、次に航跡、"
            "そして面の全体である。****面は平たくなっていくが、読み取れるままである**"
            "（カードの逐語:「**Give the path its own law of scale and physics, and keep it consistent "
            "inside the shot.**」）。\n"
            "  - `ARRIVAL`＝where the shot leaves the viewer — ⛔ **距離である。**"
            "**この作品で初めて、距離が見える。****海の全体と、その上の点とが、一つの画にある。**"
            "⚠️ **カードの逐語:「**The shot arrives somewhere.** … Leaving the viewer inside with no "
            "arrival spends the journey and keeps nothing.」**\n"
            "  - `DURATION`＝clip length — **`6.143s`。**",

 "actions": [
   ("ACT_NEAR", "舟が水の上にあり、海は一様である。",
    "**同じであり、舟はまだ近い。** ⚠️ **この1本の入口が、ここに置かれる。**"),
   ("ACT_RISE", "視点は舟の甲板の高さにある。",
    "**視点が上がっている**——**舟が小さくなり、航跡だけが長い。**"),
   ("ACT_ARRIVE", "舟がまだ舟として読める。",
    "**海の全体が入っている**——**舟は点である。**"
    "⚠️ **点になるのが、切れ目のコマである。**"),
 ],

 "camera": {
   "language": "⛔ **この1本の `EYE` は「視点」であって「カメラの位置」ではない**"
               "（カードの逐語:「**A viewpoint that is merely an unusual camera position**」は "
               "`avoid` に在る）。**この1本は、支えの無い高さから海を見る。**"
               "**それでも入口は、舟の甲板の高さ——人が立てる高さである。**"
               "⚠️ **この1本は、この作品で唯一、海の全体を画に入れる。**",
   "events": "⛔ **この1本の時間は、視点の旅そのものである。**"
             "`0-1.499s` — **舟の甲板の高さ。舟と、その周りの海。**"
             "`1.499-3.999s` — **上昇が続く。****舟が小さくなり、航跡だけが長い。**"
             "`3.999-6.143s` — **海の全体が入り、舟は点になる**"
             "——**そしてこの1本は、そこで止まらずに終わる。**"
             "⚠️ **上昇は一続きであり、途中で止まらない。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the crane** "
               "— ⚠️ **ただし、この1本では昇降機が主題ではない。****昇降機は入口の形であり、"
               "この1本が組んでいるのは視点の存在である。**"
               "**支えが無いから、この高さは在りえない。**"
               "⚠️ **Neither a dolly nor a Steadicam is used, and neither is needed**"
               "——**この1本は上がるだけであり、横へも、寄りも、しない。**"
               "**A fixed frame is not this card's case; but neither is a move with a target and a "
               "speed** (カードの逐語:「**Treating it as a camera move with a target and a speed**」は "
               "`avoid` に在る)。 No handheld, no whip, no shake, no snap zoom, no rack focus, no "
               "unnatural rotation, and **no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、面である。****面は同じ方向へ、同じ速さで動き続ける。**"
              "**航跡は長い一本の線として後ろへ伸びる。**"
              "⚠️ **この1本の彼は動かない。****海が動き、視点が動く。**",
   "object": "**舟は小さくなっていく。****航跡は伸び続ける。**"
             "⚠️ **丸太も、縄も、舵の櫂も、この1本では最初の1.499秒でしか読めない**"
             "——**そして消えるのは、形ではなく、大きさである。**",
   "environment": "**面が一つの方向へ等しく走り続ける。****反射の道が、面の上で細くなる。**"
                  "⚠️ **高さが上がっても、水の速さは変わらない。**"
                  "⚠️ **海は彼に反応しない。****また、視点にも反応しない。**",
   "weight": "**この1本の重さは、水そのものである。****面は低く、重く、等しく動く。**"
             "⚠️ **舟は、その重さの上に置かれた軽いものである**"
             "——**点になることで、それが見える。**",
   "inertia": "**水は止まらないし、急に変わらない。**⚠️ **この1本の面には、"
              "始まりも終わりもない**——**最初のコマから最後のコマまで、同じ速さである。**"
              "⚠️ **下降もしない。****視点は、上がったまま終わる。**",
   "acceleration": "**加速しない。****上昇も、水も、一定である。**"
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この6.143秒に、止まったフレームは"
               "一つも無い**——**面は最後のコマまで動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**遠くなることは、打撃ではない。**"
             "**音を立てない変化である。**",
 },

 "emotion": {
   "arc": "**着かなさ。** ⚠️ **この1本の壮大さは、広さから来ない**"
          "——**着かないことから来る**（`shots/odyssey-s21.yaml` の `aim` の逐語）。"
          "**面はどこまでも続き、舟は点であり、この1本はそこに着かない。** "
          "⛔ **勝利にしない。****この1本は、彼を小さくすることを目的にしていない**"
          "——**距離を置くだけである。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****舟が点になることである。**"
             "⚠️ **`s14`（1度目）は舳先の高さである。****この1本は在りえない高さであり、"
             "その差がこの1本の感情である。**",
 },

 "lighting": {
   "base": "**夜である。****光源は星と、その水面の反射だけである。****波は黒く、"
           "反射の道だけが白い**（`ledger.locations.海.states.夜` の逐語）。"
           "⚠️ **この1本の光源は一つであり、それは星である。**"
           "⚠️ **月も、火も、灯も無い。****高さが上がっても、光源は増えない。**",
   "events": "**One, and it is the whole shot.** **反射の道が、面の上で細くなり、"
             "一本の線になり、かすり傷のようになる**——**この1本の高さは、"
             "光の量ではなく、光の細さで見える。**"
             "⚠️ **光源そのものは動かない。**"
             "⚠️ **様式カードの逐語:「The grade holds for the whole shot — a colour temperature that "
             "swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水の音、風の音、そして徐々に薄くなっていくこと。**"
          "⚠️ **この1本の音は、高さとともに痩せる**——**水音が遠くなり、"
          "最後には風だけになる。** ⚠️ **この薄れ方は演出である**"
          "——**高さが上がれば、水の音は届かない。**"
          "⚠️ **船の音は無い**——**この海に他の船は一隻も無い。**",
   "music": K.NO_MUSIC + " ⚠️ **そしてこの1本には、歌が在る**——`l20`「海を渡る」であり、"
            "**行の長さが、そのままこの1本の長さである**（187.979–194.122）。"
            "**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜の外海の、支えの無い高さ。**水、風、そして何も無いこと。** "
                  "⚠️ **鳥の声は無い**（`海.base` の逐語）——**この高さに、鳥は居ない。**"
                  "**ゆえにこの視点を、鳥が持っていると読ませる余地も無い。**"
                  "⚠️ **呼ぶ声も、歌う声も無い。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="**体格・肌・髪・髭・顔・傷・着ている一枚と、着ていないすべて・裸足であること。** "
                "⚠️ **この1本は彼を近くで写さない**——**それでも塊は §18 にまるごと入る。**"
                "⚠️ **舟が無人になれば、この1本は別の作品になる。**",
     may="背中の角度、左手の位置、そして舟と一緒に小さくなること。"),
   "spatial": "**この1本の視点は `海` の上にある。****高さは変わるが、場所は変わらない。**"
              "**陸はどの方向にも見えない**（`海.geography` の逐語）。"
              "⚠️ **入口が舟の甲板の高さにあるので、この1本は `s20` の続きとして読める**"
              "（カードの逐語:「**An unstated entry reads as a continuity error in the previous shot**」"
              "——**ゆえに入口は、明示され、かつ手前の画から続く高さに置かれる**）。",
   "temporal": "**夜である。****`s20` と同じ夜であり、`s22` も同じ夜である。**"
               "⚠️ **この3本は続いている**——**曲のサビが、3本続けて夜である。**"
               "画の中に日付を与えるものは何も無い。",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は星の光だけである。**"
             "⚠️ **この1本は `impossible-camera` を名乗るが、その文法は §15 から何も免除しない**"
             "——**この1本は、場所も時刻も一つである。****変わるのは高さだけであり、"
             "高さは §15 の欄ではない。**",
   "motion": "Full animation, not limited. **面が動き、航跡が伸び、視点が上がる。** "
             "⚠️ **彼は動かない。****この対比が、この1本の全体である。**",
   "sound": "水、風、そしてその薄れ方。**音楽なし。言葉なし。** ⚠️ **主題歌はこの1本のあいだ"
            "鳴っているが、この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**この1本には彼が居る（点として）**——**ゆえに女神の禁制は、他人の形で来る。**"
     "**この高さの持ち主を、人のかたちで置かない。**")) + [
   "**No second person in frame at all** — no companion, no crowd, no figure at any distance, "
   "**no one on the water anywhere.**",
   "**No boat, no ship, no hull, no other vessel** (逐語, `ledger.props.舟.negative` の "
   "`no boat, no ship, no hull`、そして `ledger.locations.海.base` の `no other vessel`)。"
   "⛔ **この1本はいちばん広く海を写すので、この禁制がいちばん効く。****海は空である。**"
   "⚠️ **この1本の舟は筏である**——`ledger.props.舟.negative` の逐語は「**no boat, no ship, no hull, "
   "no keel, no planking**」であり、**この禁制は、筏を舟として描くことを禁じている。**"
   "**高い位置から点として見えるのは、その筏である。**",
   "**No conventional camera position** (逐語, `impossible-camera` の `## Negative`). "
   "⚠️ **この高さに、支えを置かない。**",
   "**No unstated entry** (逐語, `impossible-camera` の `## Negative`). "
   "⚠️ **この1本は、人が立てる高さから始まる。****入口を画面の外に置かない。**",
   "**No cut** (逐語, `impossible-camera` の `## Negative`). **上昇は一続きである。**",
   "**No fisheye distortion standing in for the impossible viewpoint** "
   "(逐語, `impossible-camera` の `## Negative`). **歪みではなく、支えの無さで立つ。**",
   "**No path that changes its own physics** (逐語, `impossible-camera` の `## Negative`). "
   "⚠️ **面は平たくなっていくが、読み取れるままである。****途中で別のものにならない。**",
   "**No shot without an arrival** (逐語, `impossible-camera` の `## Negative`). "
   "⚠️ **この1本は距離に着く。**",
   "⛔ **No support for the viewpoint anywhere in the frame** — no drone, no aircraft, no bird, no "
   "mast, no cliff, no rock, no tower, no balloon, **no shape the height could be standing on.**",
   "**No sail set on the raft in this frame, and no bird appears** (逐語, `ledger.locations.海.base` の "
   "`no sail`, `no bird`).",
   "**No wheel, no helm, no rudder, no tiller** — ⚠️ **舵は船尾に縛られた一本の櫂である。**",
   "**No white water, no breaking crest, no spray** — **この海は白波を立てない。****この1本の面は、"
   "そのことで一枚の材質として読める。**",
   "**No land, no shore, no island, no coastline, and no light on the water other than the stars.**",
 ],

 "must": [
   "**海の全体と、その上の舟とが、同じ一つの画に入ること** — そして**舟が点になること。**",
   "⛔ **入口が明示されること** — **この1本は、人が立てる高さから始まる。**",
   "⛔ **切らないこと。****上昇は一続きである。**",
   "⛔ **この1本が視点の存在を組むこと** — **カメラの位置と速さの話にしない。**",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.**",
   "⚠️ **この1本の面が、平たくなっても読み取れるままであること** — **別のものにならない。**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **彼はレンズを見ず、口を開かない。**",
   "⚠️ **変化は最後のコマで終わる** — **舟が点になったところで、この1本は終わる。**"
   "**そのあと、視点は下りない。**",
   "⚠️ **`impossible-camera` の5つを満たすこと** — `EYE` は支えの無い高さ、`ENTRY` は舟の甲板の高さ、"
   "`PATH` は面の全体、`ARRIVAL` は距離、`DURATION` は 6.143秒。",
 ],

 "prefer": "The water kept black and even; the wake the single line that breaks it; the frame's density "
           "falling as the viewpoint rises; the reflected path thinning to a scratch; "
           "**the man read as part of the raft and then as part of the point.**",
 "allow": "The near water passing faster than the far; the surface flattening as the frame rises; the "
          "raft crossing from readable to a point over the last seconds; **a rise that ends without "
          "descending and without settling.**",

 "priorities": [
   "⛔ **舟が点になること。** **この1本の切れ目は、それである。**",
   "⛔ **切らないこと。****上昇は一続きである。**",
   "⛔ **入口が明示されること。****手前の画から続く高さから始める。**",
   "⛔ **他の船を一隻も入れないこと** — **この1本はいちばん広く海を写す。**",
   "⚠️ **支えを置かないこと** — **マストも、崖も、鳥も、機械も無い。**"
   "**在りえなさは、支えの無さである。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "**No second person, at any distance, in any focus.**",
   "**光は星の光だけであること** — 月も、火も、灯も無い。",
   "⚠️ **`impossible-camera` の5つを満たすこと** — とくに `ENTRY` と `ARRIVAL`。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `impossible-camera` を名乗るが、その禁制（`no conventional camera position`・"
   "`no unstated entry`・`no fisheye distortion`・`no shot without an arrival` ほか）は §16 に在って、"
   "ここには無い。** **ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 6.143-second cinematic take (16:9) of open sea at night, one clip, one continuous take, from a "
   "viewpoint that cannot exist, one change: **the whole sea comes into frame and the raft becomes a "
   "point on it.**\n\n"
   "**{IDENTITY}** **He is on the raft, standing at the stern with his left hand on the lashed steering "
   "oar; he does not move, does not speak, and does not look at the lens, and he becomes smaller with "
   "the raft.**\n\n"
   "**The entry is stated: the shot begins at the raft's own deck height — a height a person could "
   "stand at — and rises from there, and it never cuts.**\n\n"
   "0-1.499s: **the raft and the water around it, still near.** The raft is readable: logs, cordage, the "
   "lashed oar.\n"
   "1.499-3.999s: **the viewpoint rises. The raft gets smaller and only the wake is long.**\n"
   "3.999-6.143s: **the whole sea is in frame and the raft is a point** — and the take ends on that, "
   "still rising.\n\n"
   "**There is nothing in this frame for the viewpoint to stand on: no drone, no aircraft, no bird, no "
   "mast, no cliff, no rock, no balloon — the height is unsupported, and that is what makes it "
   "impossible.** **The water never changes what it is: long low ridges with no white water, running "
   "steadily in one direction, and only the raft's wake breaks them.** **There is no other vessel "
   "anywhere — the sea is empty — and no land, no sail, no bird, no moon.** **No fisheye and no "
   "wide-angle warp: a real lens at a height nobody can hold.** **No second person is in this frame at "
   "any distance or in any focus, and no woman is in it at all.** **This is a bronze-age sea before "
   "classical Greece: no made thing of any later age.** **This is a Japanese work.** No subtitles. No "
   "BGM.\n"
   "(One continuous take, one change: the sea becomes a surface with a point on it.)"),

 "visual_scene": (
   "Open sea at night, photographed as a film frame from a height at which the whole sea is one "
   "surface: **long low ridges of black water with no white water, running steadily in one direction, "
   "the surface broken by one thing only — the raft's wake, a single long line, with the raft at its "
   "head as a small point.** In the first seconds the raft is still readable — unseasoned pine logs "
   "lashed with coarse hand-twisted cordage, a steering oar tied at the stern and lashed, not fitted, "
   "a short mast with nothing set on it — **and then it is a point.** Above it the sky is a shade above "
   "the water and carries one broken path of reflected starlight. **Nowhere in the frame is there any "
   "support for this viewpoint. No other vessel, no land, no sail, no bird, no moon.**"),

 "visual_meta": (
   "Anamorphic lens with subtle oval bokeh and a gentle flare on the reflected path; **the focus "
   "deepening as the frame rises, so that the surface and the horizon are both sharp by the end**; a "
   "graded palette of black water and a sky one shade above it, with one white reflected path that "
   "becomes a line and then a scratch. Long low ridges with no white water and the raft's one long "
   "wake; barked pine logs and coarse hand-twisted cordage in the first seconds only; even film grain "
   "over everything. No painterly stroke, no airbrush, no plastic surface, no CGI look, no "
   "illustration. ⚠️ **The frame loses its texture as it rises** — by the end there is nothing in it "
   "but the water's own movement, the horizon, and one mark."),

 "motion_prompt": (
   "Full animation, not limited. **The surface is the mover: long low ridges running steadily in one "
   "direction at the same rate from the first frame to the last, broken by nothing but the raft's "
   "wake.** **The wake lengthens behind the raft throughout, a single long line, and the raft stays at "
   "its head.** **The viewpoint rises continuously and does not stop, and the raft crosses from "
   "readable to a point over the last seconds; the water does not change speed as the frame rises, and "
   "the surface stays readable as it flattens — it never becomes another material.** **The man stays "
   "where he is and does not turn.** No motion blur smears, no stutter, no floaty weightless motion, no "
   "static frames — **the water moves in every frame of the take.**"),

 "camera_prompt": (
   "⛔ **This is not a camera move with a target and a speed — it is a viewpoint whose existence is the "
   "shot.** **The entry is stated: the shot begins at the raft's own deck height, a height a person "
   "could stand at, and rises from there without a cut.** ⚠️ **The style permits a dolly, a crane and a "
   "Steadicam, and this shot spends the crane** — **but the crane is the shape of the entry, not the "
   "subject of the shot: what rises is a viewpoint with nothing to stand on.** ⚠️ **Neither a dolly nor "
   "a Steadicam is used, and neither is needed** — this frame rises and does not travel sideways and "
   "does not close in. **No fisheye and no wide-angle warp.** ⚠️ **Nowhere in the frame is there a "
   "support for this viewpoint.** No handheld, no whip, no shake, no snap zoom, no rack focus, no "
   "unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water working against the raft's logs, and wind.** "
   "⚠️ **The sound thins with the height — the water falls away behind the viewpoint and the wind is "
   "what is left.** ⚠️ **No other vessel is heard: there is none in this sea.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (impossible-camera) ／ "
                        "REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②）。"
                        "⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ。**"
                        "⚠️ **参照集合の8鍵のうち、この1本の主題は `海` であり、その上に `舟` がある。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water ＋ wind ／ no music",
 "unresolved": [
   "⚠️ **この1本の `EYE` が「在りえない高さ」であるためには、支えが無いことが画で読める必要がある。**"
   "⚠️ **カードの逐語は「**A viewpoint that is merely an unusual camera position**」を `avoid` に置く"
   "——**ゆえにこの仕様は、支えの不在を §16 と英文の両方に明示し、"
   "入口を「人が立てる高さ」に置いた。** ⚠️ **それでも、この高さが「カメラの位置」と"
   "読まれる余地は残る。****高さそのものは §15 の欄ではないので、"
   "この1本は §15 から何も免除を求めていない。**",
   "⚠️ **この1本に彼を残したこと。** ⚠️ **ショット記録の `motion.subject` は"
   "「波面の全体、舟、そしてその航跡」であり、彼に触れていない。**"
   "**しかし参照集合は `男.identity` を挙げており、この作品の筏は彼が作ったものである**"
   "——**ゆえにこの仕様は、舟を無人にせず、彼を最初の1.499秒だけ読める位置に置いた。**"
   "⚠️ **点になったあと、点が彼であるかどうかを、この1本は言わない。**",
   "⚠️ **音の薄れ方を、この仕様が決めたこと。** ⚠️ **記録の `motion` にも `aim` にも、"
   "音の指示は無い。****この仕様は「高さが上がれば水音は届かない」という物理から、"
   "薄れ方を書いた。** ⚠️ **`bible` にも台帳にも、この判断の根拠は無い。**",
 ],
 "risks": [
   "⛔ **他の船が入る。** ⚠️ **広い海の画は、この経路がいちばん自然に船を足すところである**"
   "——**`bible.negative_base` の逐語と §16 の禁制の両方に在る。**",
   "⛔ **支えが入る。** ⚠️ **高い視点を、この経路はマスト・崖・鳥・機体で説明したがる**"
   "——**説明が入れば、この1本は「在りえない視点」ではなく「ドローン映像」になる。**",
   "⛔ **高さが歪みで作られる。** ⚠️ **魚眼・超広角は、この経路で高さを出すいちばん安い方法である**"
   "——**カードの禁制がそれを禁じている。**",
   "⚠️ **海が別のものになる。** ⚠️ **高さが上がるにつれ、この経路は水を雲や布に写しやすい**"
   "——**面は読み取れるままでなければならない。**",
   "**入口が無い。** ⚠️ **最初から高い位置に居れば、この1本は前のショットの継続エラーとして読まれる。**",
   "**壮大になる。** ⚠️ **この1本の感情は着かなさであり、勝利ではない。**",
   "**彼が消える。** ⚠️ **舟が無人に描かれれば、この作品の筏ではなくなる**"
   "——**参照画像が1枚も無いので、守る道具は英文だけである。**",
 ],
}

if __name__ == "__main__":
    print("s21 content OK — keys:", len(C))
