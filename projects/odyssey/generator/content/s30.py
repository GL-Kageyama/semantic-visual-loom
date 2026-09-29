# -*- coding: utf-8 -*-
"""odyssey-s30 — meaning-responsive — 海 / 夜 / 6.542s. l31「なんでもない島へ」。"""
import common as K


C = {
 "n": "s30",
 "title": "水平線の一点だけが、少し明るい",
 "duration": "6.542",
 "format": "meaning-responsive",
 "has_man": False,
 "segment": "final-chorus-4",

 "band": [
   "『永遠より遠い』 final-chorus「海」 / 情景 / motion —— なんでもない島へ——水平線の一点だけが、少し明るい",
   "水平線の一点だけがわずかに明るい——そこに何かがある。",
   "6.542秒、カメラはその一点へごくゆっくり寄る——明るさが同じ大きさのままであるのが、切れ目である。",
   "陸は現れず、明るさは大きくならない——それは、陸の証明ではない。",
 ],
 "header": """⚠️ **`l31`「なんでもない島へ」である。**
⛔ **この1本の狙いは「何でもない」を、6.5秒で肯定的に写すことである**——
**明るさだけで、そこに何かがあると言えるか**（`aim` の逐語）。
⛔ **島を写せば、この行は「島へ着く」になる。**
⚠️ **形式は `meaning-responsive`。****`s24` と同じである**——
**`s24` は「失われた」に反応し、この1本は「何でもない」に反応する**（記録の逐語）。
⚠️ **この作品で `情景` を使うのは4本である**（`s01`・`s04`・`s12`・`s30`）——
⛔ **`intro` の両端と、`pre-chorus` の終わりと、ここである。**
**すべて「世界が、人の居ないところで在る」ショットである**（記録の逐語）。
⚠️ **ここだけ 6.542秒である**——**`chorus-1` では 3.910秒であり、束ねる相手（`l12`）が要った。**
**ここでは1行で下限4秒を超えるので束ねない**——**曲が伸ばしたからであり、この作品が割ったのではない**
（記録の逐語）。**この差分が、`final-chorus` と `chorus-1` の2点のうちの1点目である。**
⛔ **この1本の画には、人が一人も入らない。****記録の `unit` と `beats` のどこにも、人物が現れない**——
**ゆえにこの1本は、人を一人も置かない。**（§3 と §15 を見る）。
⚠️ **この仕様のショット記録は `shots/odyssey-s30.yaml` である。**""",

 "intent": "⛔ **「何でもない」を、6.5秒で肯定的に写せるか。** ⚠️ **島を写せば、この行は"
           "「島へ着く」になる。** ⛔ **明るさだけで、そこに何かがあると言えるか**（`aim` の逐語）。"
           "⚠️ **この1本は `mode: motion` である**——**止まるのは、あの明るさだけである。**"
           "**波は動き、カメラは寄る。****動かないのは、一点の明るさの大きさである。**"
           "⛔ **切らない。****1本は1つの画である。** "
           "⚠️ **変化は切れ目のコマで終わる**——**大きくならないことが、そのコマである。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本の場所は `海`、時刻は `夜` である。****陸は、どこにも無い。**"
   "⛔ **そしてこの1本でも、陸は現れない**（`world.rules` の五番）。"
   "⚠️ **この1本が置くのは「遠さ」ではなく「一点」である**——"
   "**水平線の一点だけが、わずかに明るい。****何も見えないが、そこに何かがある。**"
   "⛔ **その何かを、この作品は名指さない。****名指せば、"
   "「何でもない」が「何かである」に変わってしまう。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本の画には、人が一人も入らない****——ゆえにこの規則の "
               "`answer` は、この1本では「人に返事が来ない」としてではなく、"
               "** 「世界が、人に向かわずに在る」として効く。****それでも返事は返らない。**"
               "**あの少しの明るさは、誰かに向けたものではない**——"
               "**この1本には、受け取る者が一人も居ない。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "⛔ **この1本の明るさを、彼女の形にしない**——"
                "**人のかたちも、手のかたちも、光の柱も作らない。**"
                "**与えられているものも、この1本には無い**——"
                "**あるのは、わずかに明るい一点だけである。**",
     "name": "⚠️ **この1本に名は無い。** ⛔ **そしてこの1本は、"
             "あの明るさに名前を与えない**——**島とも、岸とも、家とも呼ばない。**"
             "**呼べば、この1本は「そこへ着く」ショットになる。**",
     "bow": "⚠️ **この1本に弓は無い。****舟も、斧も、帆も、この1本の画には無い。**",
     "places": "この1本が置くのは一つ——`海`。⚠️ **この1本にも、"
               "`world.rules` の五番が効く**——**この作品は、帰り着かない。**"
               "**ゆえにこの1本は、島を写さない。****明るさは、陸の証明ではない**"
               "（`motion.law` の逐語:「**この作品に陸は現れない**…**明るさは、"
               "陸の証明ではない。**」）。",
     "japanese": "⚠️ **この1本には歌がある**——`l31`「なんでもない島へ」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **形式 `meaning-responsive` の文法は「`video-spec` に一つの文法を足したもの」である**"
     "（カードの逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card "
     "requires; what follows is only what this grammar adds to it.」）。"
     "**この1本では、意味を運ぶもの（`BEARER`）は水平線である**——**それは、何もしない。**"
     "**この1本の答え（`ANSWER`）は世界の側に在る****——"
     "水平線の一点だけが、わずかに明るい。****カメラはそれを起こさない。**",
     "⚠️ **カードの逐語:「The answer is in the world, not in the camera.」**"
     "**ゆえにこの1本の文法は、§10 の `target` と §12 の光の出来事に書かれる**"
     "（カードの `Sources` の逐語:「Its grammar is written into the `video-spec` skeleton — "
     "**§10 CAMERA's target and §12 LIGHTING** — and it is the card that most needs §12's lighting "
     "events, because the world's answer is staged there.」）。"
     "⚠️ **この1本のカメラは寄るが、寄ることは答えではない**——"
     "**答えは、寄っても大きくならない明るさの側にある。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, far from any land, photographed as a film frame. **The frame holds the water, "
     "the horizon and the sky above it, and nothing else**: long low swells with no white water, moving "
     "steadily in one direction, and one broken path of reflected starlight on the near water. **On the "
     "horizon's line, at one point, the darkness is a little thinner than it is anywhere else on the "
     "line** — a slight lift, no bigger than the eye would lose if it looked away. ⚠️ **No land, no "
     "island, no shore, no sail, no bird, no vessel of any kind — and no part of the raft in the "
     "frame.**",
   "Color Language":
     "A narrow, graded palette, and it has one source: **the night is lit by the stars and by their "
     "reflection on the water, so the waves are black and the reflected path alone is white**"
     "（`ledger.locations.海.states.夜` の逐語:「光源は星と、その水面の反射だけである。波は黒く、"
     "反射の道だけが白い。」）. ⚠️ **The one bright point on the horizon is not a second colour** — "
     "**it is the same black, lifted a little.****Nothing warm enters the frame, and nothing glows.**",
   "Texture":
     "The water's surface fine-grained and broken, long low swells with no crest and no white water; "
     "the reflected path broken into short strokes on the moving face of the water; **the sky's grain "
     "slightly coarser where the darkness thins at that one point on the horizon**; even film grain, "
     "visible in the black. ⚠️ **There is no shingle, no stone, no wool, no skin and no cloth in this "
     "frame** — **the surface of this shot is water and the air above it.**",
   "Rendering":
     "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, **a gentle flare "
     "on the one reflected path**. **Not a photograph's stillness: a film frame, with a real lens's "
     "fall-off at the edges.** No illustration, no CGI look, no cartoon color.",
   "Visual Density": "Low, and slightly lower than `s29` at the end — **この1本は、"
                     "明るい一点だけを余計に持つ。** ⚠️ **それ以外は何も入らない**"
                     "——**この1本の密度は、最後の2.041秒でわずかに上がる**"
                     "（寄るぶんだけ、一点が大きくなるからである）。",
   "Time": "`夜` — the source is the stars and their reflection on the water; the waves black and the "
           "reflected path alone white. ⚠️ **この作品は一日のうちの三つの時刻しか使わない**"
           "（`日没`・`夜`・`夜明け`）。**画の中に日付を与えるものは何も無い。**"
           "⛔ **そしてこの1本の明るさは、夜明けではない**——**夜明けは `s18` のものである。**",
   "Atmosphere": "The night in which one point of the horizon is not quite as dark as the rest of it.",
 }),

 "subjects": [
   {"name": "水平線の一点",
    "ref": "⛔ **この1本の主題である。****参照は `ledger.locations.海.geography` の逐語"
           "（「the horizon is level and unbroken」）と、`海.base` の「At night the surface carries one "
           "broken path of reflected light」である。** ⚠️ **参照画像は無い**（裁定②）。",
    "appearance": "**水平線の上の、一点である。****そこだけ、暗さがわずかに薄い。**"
                  "**縁も、輪郭も、にじみも無い**——**線の上に、少しだけ明るい区間があるだけである。**"
                  "⚠️ **形を持たない。****島にも、帆にも、灯にも読めない。**"
                  "⛔ **それがこの1本の全部である**——**他には何も足さない。**",
    "behavior": "⛔ **動かない。****この6.542秒のあいだ、同じ位置に、同じ大きさで在る。**"
                "⚠️ **`mode: motion` であるこの1本で、止まっているのはこれだけである**"
                "（`motion.subject` の逐語:「**波は動き、その明るさは動かない。**」）。"
                "⛔ **大きくならない。****カメラが寄っても、大きくならない**"
                "——**大きくならないことが、この1本の切れ目のコマである**"
                "（`beats` の3番目の逐語）。",
    "continuity": "**Must preserve** — 位置（水平線の同じ一点）、大きさ、形を持たないこと、"
                  "暖かい色を持たないこと、そして**動かないこと**。"
                  "**May change** — 暗さの薄さの度合い（ごくわずかに揺れてよい）、"
                  "そして画面上でのわずかな位置のずれ（カメラが寄るぶんだけ）。",
    "notes": ["⛔ **この一点に、原因を置かない**——**カードの `Negative` の逐語:"
              "「**no visible cause**」**。**灯も、火も、舟も、星の増加も、"
              "この明るさの原因として画面に入らない。**",
              "⛔ **この一点を、島にしない。****陸にしない。****近づいた先に何かを見せない**"
              "——**この作品は帰り着かない**（`world.rules` の五番）。",
              "⛔ **この1本の画には、人が一人も入らない。****記録の `unit`（前・後）と `beats` のどこにも、人物が現れない**"
              "——**ゆえにこの1本は、人を一人も置かない。**"
              "**参照集合は「固定するもの」を挙げており、「画に居る者」を挙げているのではない**"
              "（§15 の `identity` を見る）。"]},
   {"name": "近い水面",
    "ref": "**この1本の動く側である。** ⚠️ **参照は `ledger.locations.海` の `base` と `states.夜`。**",
    "appearance": "**長く低いうねりであり、白波を立てない。****一つの方向へ、絶えず同じ速さで動く。**"
                  "**星の反射が短い線になって、その面を走る。**",
    "behavior": "**流れる。****この6.542秒のあいだ、一度も止まらない。**"
                "⚠️ **この1本の動きは、この層のものである**——**暗さの薄い一点は、"
                "この動きの中にありながら、動かない。**",
    "continuity": "**Must preserve** — うねりの低さ、白波が無いこと、反射が短い線であること、"
                  "一つの方向へ動くこと。**May change** — 反射の線の位置、うねりの高さ、位相。",
    "notes": ["⚠️ **この1本の密度の変化は、この層には無い**——**変わるのは、"
              "暗さの薄い一点の見え方だけである**（カメラが寄るぶん）。"]},
 ],

 "environment": {
   "location": "`海` — **夜である。****四方を水に囲まれ、どの方向にも陸が見えない**"
               "（`海.geography` の逐語）。⚠️ **この1本のカメラは低く、水面のすぐ近くにある**"
               "——**舟も、人も、この1本の画には入らない**。",
   "elements": "**長く低いうねり**、**一つの方向へ絶えず動く水面**、**星の反射の道**、"
               "**平らで途切れない水平線**、**その一点だけ薄い暗さ**、そして**その上の空**。"
               "⛔ **陸も、島も、帆も、鳥も、他の船も無い。**"
               "⛔ **そしてこの1本の画には、人が一人も入らない。**",
   "behavior": "**波が動き続ける。****一点の明るさは、動かない。**"
               "⚠️ **この二つが同時に在ることが、この1本の全部である**"
               "——**世界が、人の居ないところで在る**（`s30` の記録の逐語）。"
               "⛔ **この一点に、誰も気づかない。****気づく者が、この1本には一人も居ない。**",
 },

 "objects": [
   "**無い。** ⚠️ **この1本の画には、物が一つも無い**——**水と、水平線と、その一点と、"
   "その上の空だけである。**",
   "⚠️ **`ledger.props` の4つ（舟・帆・斧・太陽の牛）は、この1本には来ない。**"
   "**参照集合が `舟` を挙げているのは、この作品の場所と、彼が乗っているものを固定するためである**"
   "——**舟はこの1本の画角の外にある。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本の画には入らない。****この1本のどこにも、人物が現れない**（§3 と §15）。"
                  "`女神` — **この1本には添付しない。****彼女はこの1本に、"
                  "四つの姿のどれとしても現れない。** "
                  "⚠️ **`男.identity` と `男.negatives` が集合に在っても、それは外見を固定するためであり**"
                  "——**ゆえにこの集合は、この1本に人が居ることも、彼女が居ることも主張しない。**",
 "ref_extra": [
   "- ⚠️ **形式カード `meaning-responsive` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; "
   "what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じである。**",
   "- ⚠️ **カードの逐語:「**This is a single point: nothing in the frame causes the answer.** No object "
   "moves into the frame, no light source changes, no one acts.」****この1本では、"
   "明るさの原因が画面の中に無い**——**光の源は変わらず、星だけである。****変わるのは、"
   "暗さの薄さだけである。**",
   "- ⚠️ **カードの逐語:「**The bearer is named, and it does not act.** … The carrier is what the "
   "picture is answering; the carrier is not what makes the picture answer.」"
   "**この1本の `BEARER` は水平線である**——**この行の「何でもない」は、"
   "何も無い一本の線に載っている。****その線は、何もしない。**"
   "⛔ **人が居ないので、`BEARER` を人にすることはできない**"
   "——**人の代わりに立てるのは、この線だけである。**",
   "- ⚠️ **カードの逐語:「**The delay is composed.** The gap between the meaning and the answer is the "
   "shot's time. Answering instantly reads as a cut; answering at the end of the clip reads as a "
   "reveal.」****この1本の遅れは、2.002秒後に始まり、6.542秒まで続く**——"
   "**答えは途中で来て、最後まで確定しない。****ゆえにこの1本は、"
   "カットにも、露見にも読めない。**",
   "- ⚠️ **形式カード `meaning-responsive` の5つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `BEARER`＝what carries the meaning — **水平線である。****この行の「何でもない」を運び、"
   "何もしない。** ⛔ **人を立てない**（この1本の画には、人が一人も入らない）。",
   "  - `ANSWER`＝how the picture answers it — **水平線の一点だけが、"
   "わずかに明るい。****そして、大きくならない。**"
   "⚠️ **答えは世界の側に在って、カメラの側には無い**"
   "（カードの逐語:「The answer is in the world, not in the camera.」）。",
   "  - `DELAY`＝how far the answer lags the meaning — **2.002秒である。**"
   "**最初の2.002秒は一様であり、そのあとで一点が薄くなる。**"
   "**そして残りの4.540秒は、その答えが確定しない時間である。**",
   "  - `LIMIT`＝what the answer may not reach — ⛔ **明るさは大きくならない。**"
   "**形を持たない。****近づいても、距離は縮まらない。****水には触れない。**"
   "**そして陸にはならない。**⚠️ **この限界が、この1本を「何でもない」のまま保つ**"
   "（カードの逐語:「What the answer may not touch keeps it legible.」）。",
   "  - `DURATION`＝clip length — **`6.542s`。**",
   "⛔ **カードの `avoid` のうち、この1本で最も危ないのは「A camera move, a cut, or a rack focus "
   "standing in for the answer」である。****この1本はカメラが寄る**（`motion.quality` の逐語）"
   "——**ゆえにこの1本では、答えがカメラより先に来ていなければならない。**"
   "⚠️ **`beats` の順序が、それを保証している****——答えは2.002秒で来て、カメラは4.501秒から動く。**"
   "**動くときには、答えはもう出ている。****ゆえに寄ることは、答えの原因にならない。**",
 ],

 "narrative": {
   "core": "**明るさだけで、そこに何かがあると言えるか** — **島を写せば、この行は「島へ着く」になる。**",
   "beginning": "**海と水平線。****一様である。****島はまだ無い。**"
                "⚠️ **この2.002秒は、答えがまだ来ていない時間である。**",
   "turn": "**一点が、わずかに明るい。****波は動き、明るさは動かない。**"
           "⚠️ **この1本の答えは、ここで出る。****遅れは2.002秒である。**",
   "peak": "**カメラが一点へ寄る。****明るさは、同じ大きさのままである。**",
   "pull": "⚠️ **大きくならないのが、切れ目のコマである。****何も見えないが、"
           "そこに何かがある**——**その状態のまま、`l31` の歌が終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.041秒.** 頭の2.002秒は**答えが来る前**のために"
            "払われ、次の2.499秒は**答えが出て、しかし確定しないこと**に払われ、"
            "**最後の2.041秒がこの1本の出来事である**——**寄っても大きくならないこと。** "
            "⚠️ **この1本だけ 6.542秒である**——**`chorus-1` では 3.910秒であり、"
            "束ねる相手（`l12`）が要った**（記録の逐語）。**この2.632秒の差が、"
            "`final-chorus` と `chorus-1` の2点のうちの1点目である。** "
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**波は動き続け、カメラも寄る。**",

 "actions": [
   ("ACT_UNIFORM", "海と水平線がある。**一様である。**",
    "**同じ画が2.002秒のあいだ保たれる**——**水平線のどこも、"
    "他より明るくも暗くもない。**"),
   ("ACT_LIFT", "水平線は、どこも同じ暗さである。",
    "**一点だけ、暗さが薄くなる**——**形を持たず、大きさを持たず、"
    "動かない一点が、水平線の上に在る。**"),
   ("ACT_APPROACH", "一点が、わずかに明るい。**波は動いている。**",
    "**カメラがその一点へ寄る**——**そして明るさは、同じ大きさのままである。**"
    "**大きくならないことが、この1本の切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **low over the water, the horizon running high across the frame** — "
               "**the one bright point sits on that line, small in the frame.** "
               "⚠️ **この1本の画角は、水平線と、その上の一点を、"
               "同じ一つの面の中に置く。**",
   "events": "**One, in the last beat: from 4.501s to the end of the clip, a very slow approach "
             "toward the one bright point on the horizon, at a constant speed, ending while the point "
             "is still small.** ⚠️ **この1本のカメラの出来事は一つだけである**"
             "——**動機は「そこに何かがあるのか」であり、"
             "様式の法が許す「動機のある移動」の側にある**"
             "（`motion.law` の逐語:「**この様式は、"
             "動機のあるカメラ移動だけを許す**」）。"
             "⛔ **そしてこの1本の答えは、この出来事より先に来ている**"
             "——**答えは2.002秒、カメラは4.501秒。****ゆえに寄ることは、"
             "答えの原因でも、答えそのものでもない。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the "
               "dolly** — ⚠️ **この1本の移動は外向きではなく内向きであり、"
               "近づく向きだけである**——**横へも、上へも動かない。****速さは一定で、"
               "ごく遅い。** ⚠️ **そして寄る先は、"
               "「何かがある」と確定しない一点である**——"
               "**この1本は、寄りながら、"
               "そこに何も見えないまま終わる。** "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and **no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、波である。****そして止まっているのは、"
              "あの明るさである**（`motion.subject` の逐語:「**波は動き、"
              "その明るさは動かない。**」）。"
              "⚠️ **この二つが同じ画にあることが、この1本の全部である。**",
   "object": "⚠️ **この1本には、動く物が無い。****動くのは水だけである。**"
             "⛔ **そして、あの一点は物ではない**——**動かないことが、"
             "その正体の全部である**（形も、縁も、大きさの変化も持たない）。",
   "environment": "**星の光が、静的な光源として画面の外に在る。****その反射が、"
                  "動く面の上で短い線に砕ける。**"
                  "⛔ **この1本では、光源が変わらない**"
                  "（カードの逐語:「**no light source changes**」）"
                  "——**明るくなるのは、暗さの薄さだけである。**",
   "weight": "**うねりは低く、質量は水のものである。****速さは一度も変わらない。**"
             "⚠️ **この1本のカメラの移動も、質量を持つ**——**ごく遅く、"
             "一定で、重い。****急に寄ることは、この1本では許されない。**",
   "inertia": "**反射の線は、遅れて消える。****カメラの移動も、"
              "止まるときにわずかに残る**——**しかしこの1本は、"
              "寄り切る前に終わる。**",
   "acceleration": "**波は加速しない。****カメラも加速しない**"
                   "——**この1本の最後の2.041秒は、"
                   "一定の速さで近づくだけである。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この6.542秒に、"
               "止まったフレームは一つも無い**——**あの一点が動かないことと、"
               "画面が止まることは違う。**",
   "impact": "**無い。** ⛔ **この1本に衝撃は一つも無い**——"
             "**「何でもない」に、打撃を与えない。**"
             "**大きくならないことは、音を立てない出来事である。**",
 },

 "emotion": {
   "arc": "**何でもない、という肯定。** ⚠️ **この作品は、"
          "「何かがある」と言わずに「何かがある」と言う**——"
          "**その最小の形が、この1本である。**"
          "⛔ **不安を感情にしない**——**脅かす画ではない。****期待にもしない**"
          "——**期待させれば、着かないことが裏切りになる。**"
          "**わずかな明るさが、わずかな明るさのまま残る。**",
   "events": "⚠️ **この1本の出来事は、暗さが一段薄くなることである。**"
             "⚠️ **人が居ないので、この1本には感情の担い手が一人も居ない**"
             "——**残るのは、波と、一点と、一つの光だけである。**",
 },

 "lighting": {
   "base": "**夜である。****光源は星と、その水面の反射だけである。****波は黒く、"
           "反射の道だけが白い**（`ledger.locations.海.states.夜` の逐語）。"
           "⚠️ **この1本の光源は一つであり、それは星である。**"
           "⚠️ **月も、火も、灯も無い。**",
   "events": "**One, and it is the shot's answer: at 2.002s the darkness thins at a single point on "
             "the horizon, and it stays at the same size and the same brightness for the remaining "
             "4.540s.** ⛔ **これは光の増加ではない。****より明るい光が入るのではなく、"
             "そこの暗さが薄いだけである。**"
             "⚠️ **カードは「光源が変わらないこと」を求めている**"
             "（`Negative` の逐語:「**no light source changes**」）"
             "——**星の数も、星の明るさも、この1本では変わらない。**"
             "⛔ **そしてこの出来事の原因を、画面の中に置かない**"
             "（`Negative` の逐語:「**no visible cause**」）。",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水の音だけである。****長く低いうねりが動く音、砕けない面が擦れる音。**"
          "⚠️ **打ち上げる音は無い**——**この海は白波を立てない。**"
          "⚠️ **木の音も、縄の音も、櫂の音も無い**——**舟はこの1本の画にも音にも入らない。** "
          "⚠️ **そして遠くの音も無い**——**鐘も、鳥も、岸の音も届かない。**",
   "music": K.NO_MUSIC + " ⚠️ **そしてこの1本には、歌が在る**——`l31`「なんでもない島へ」であり、"
            "**行の長さが、そのままこの1本の長さである**（261.144–267.686。**6.542秒**"
            "——`bible.song` の `final-chorus` の実測である）。"
            "**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜の外海。**水と、その上の空気だけである。**"
                  "⚠️ **呼ぶ声も、歌う声も、鳥の声も無い。**"
                  "⚠️ **この1本には、人の側の音が一つも無い**——**人が一人も居ないからである。**",
 },

 "continuity": {
   "identity": "**Must preserve** — この1本が写すものの、一句一句（海の面、光、時刻、そしてこの1本で動かないと決めたもの）。"
              "⛔ **この1本の画には、人が一人も入らない**——**ゆえにこの1本に、守るべき顔も、体も、衣も無い。**"
              "**同一性の基準は、この1本では人物ではなく、この枠そのものである**——**記録の `unit`（前・後）と `beats` のどこにも、人物が現れないからである**"
              "（§3 と §18 を見る）。"
              " **May change** — 無い。**この1本に、変わりうる人物が一人も居ない。**",
   "spatial": "**四方を水に囲まれ、どの方向にも陸が見えない**（`海.geography` の逐語:"
              "「From the raft, the water surrounds the frame on all sides and no land is visible in any "
              "direction, including behind.」）。⚠️ **カメラは低く、水面のすぐ上にある。**"
              "⛔ **そしてこの1本のカメラは、最後の2.041秒だけ、"
              "水平線の一点へごくゆっくり近づく**——"
              "**近づく距離は、水平線までの距離に対してごく小さい。**"
              "⚠️ **この1本で、この海が `s29` の海と同一であることが保たれる**"
              "（`海.geography` の逐語:「**the same waterline and the same horizon appear in both**」）。",
   "temporal": "**夜である。****この作品の三つの時刻のうちの一つである**"
               "（`日没`・`夜`・`夜明け`）。⚠️ **この作品は曲に従って時刻を選んでおり、"
               "時計には従っていない**（`bible.time_source: song`）。"
               "**画の中に日付を与えるものは何も無い。**"
               "⛔ **そしてこの1本の明るさを、夜明けの前触れにしない**——"
               "**明るさは同じ大きさのままで、増えない。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は星の光だけである。**"
             "⚠️ **そしてこの1本の一点は、グレードではなく、暗さの薄さである**"
             "——**カードの `Negative` の逐語:「**no blanket colour grade**」**"
             "**（一面に広がる答えは、この形式では答えではない）。**",
   "motion": "Full animation, not limited. **波が動き続ける。** "
             "⚠️ **カメラは最後の2.041秒だけ、一定の速さで寄る。**"
             "**あの一点は、この6.542秒のあいだ、一度も動かないし、大きくならない。**",
   "sound": "水だけ。**音楽なし。言葉なし。** ⚠️ **主題歌はこの1本のあいだ鳴っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "⚠️ **この1本の画には、人が一人も入らない**——**ゆえに女神の禁制は、"
     "「彼女を人のかたちで置かない」だけでなく、「**人の形を一つも置かない**」として効く。**")) + [
   "**No person in this frame at all** — ⚠️ **この1本には、人が一人も入らない**"
   "（記録の逐語:「すべて「世界が、人の居ないところで在る」ショットである」）。",
   "**No second person in frame at any distance, in any focus.**",
   "**No visible cause for the brightness** — ⛔ **この1本の答えには、原因が無い**"
   "（カードの `Negative` の逐語:「**no visible cause**」）。"
   "**灯も、火も、舟も、星の増加も、原因として置かない。**",
   "**No light source changes** （カードの `Negative` の逐語）。"
   "**星の数も、星の明るさも、この1本では変わらない。**",
   "**No blanket colour grade** — ⛔ **一面に広がる答えにしない**"
   "（カードの `Negative` の逐語:「no blanket colour grade」）。"
   "**変わるのは、水平線の一点だけである。**",
   "**No camera move standing in for the answer** (逐語, カードの `Negative`: "
   "「no camera move answering the meaning」) — ⚠️ **この1本は寄るが、"
   "寄ることは答えではない。****答えは2.002秒に来て、カメラは4.501秒から動く。**",
   "**No rack focus carrying the meaning, and no cut** (同、逐語:「no rack focus carrying the meaning, "
   "no cut」)。",
   "**No island, no land, no shore in this frame** — ⛔ **この1本は、"
   "あの一点を陸と呼ばない**（`world.rules` の五番）。",
   "**No boat, no ship, no hull, no other vessel in frame** "
   "（`ledger.locations.海.base` の逐語:「No land, no sail, no bird, no other vessel.」）。",
   "**No beam, no ray, no shaft of light, and no lens flare standing in for the answer.**",
   "**No white water, no breaking crest, no spray** — **この海は白波を立てない。**",
   "**No caption naming the meaning, and no voice-over naming it** "
   "（カードの `Negative` の逐語:「no caption naming the meaning, no voice-over naming the meaning」）。",
 ],

 "must": [
   "⛔ **「何でもない」を肯定的に写すこと** — **島を写せば、この行は「島へ着く」になる。**",
   "⛔ **明るさが大きくならないこと** — **寄っても、同じ大きさのままであること。**",
   "⛔ **切らない。****1本は1つの画である。**",
   "⛔ **人が一人も入らないこと** — **近景にも、遠景にも、人に読める形を置かない。**",
   "⚠️ **答えが世界の側に在ること** — **カメラの移動が答えの原因にならないこと**"
   "（答えは2.002秒、カメラは4.501秒から）。",
   "⚠️ **波が動き続けること** — **止まるのは、あの一点だけである。**",
   "⛔ **人が一人も入らないこと** — **この枠は、海だけで在る。****参照集合が人の外見を挙げていても、それは画に人を置く指示ではない。**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **変化は最後のコマで終わる** — **大きくならないことが、切れ目のコマである。**",
   "⚠️ **この1本が `l31`「なんでもない島へ」であることを、画面の側で保つこと**"
   "——**「何でもない」を、何かに変えない。**",
 ],

 "prefer": "The night held black and the reflected path the only white; the swell kept long, low and "
           "crestless; **the one point on the horizon kept small, shapeless and unflickering**; the "
           "horizon kept level and unbroken; **the camera's approach kept constant and very slow, and "
           "ended before the point resolved**; **the brightness's size kept exactly what it was at "
           "2.002s.**",
 "allow": "The reflected path breaking into short strokes and re-forming; the swell's height varying "
          "slightly as it runs; **the darkness at that one point thinning by a barely measurable "
          "degree and settling**; **the point's position drifting with the swell as the camera "
          "approaches**; **a gentle flare on the one reflected path.**",

 "priorities": [
   "⛔ **明るさが大きくならないこと** — **大きくすれば、この1本は「そこへ着く」ショットになる。**",
   "⛔ **陸を写さないこと** — **この作品は、帰り着かない。**",
   "⛔ **人が一人も入らないこと** — **この1本は「世界が、人の居ないところで在る」ショットである。**",
   "⚠️ **答えがカメラの移動に由来しないこと** — **カードの `avoid` の一番目である。**",
   "⛔ **切らないこと。**",
   "⛔ **人が一人も入らないこと** — **この枠は、海だけで在る。****参照集合が人の外見を挙げていても、それは画に人を置く指示ではない。**",
   "**No second person, at any distance, in any focus.**",
   "**光は星の光だけであること** — 月も、火も、灯も無い。",
   "⚠️ **この1本が 6.542秒であること** — **`chorus-1` の 3.910秒ではない**"
   "（曲が伸ばしたからである）。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `meaning-responsive` を名乗るが、その禁制（`no visible cause`・"
   "`no camera move answering the meaning`・`no cut`・`no rack focus carrying the meaning` ほか）は "
   "§16 に在って、ここには無い。** **ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。** "
   "⚠️ **この形式の文法は §10 の `target` と §12 の光の出来事に書いた**"
   "——**この節に持ち込めば、34本の同一性が崩れる。**"),

 "master": (
   "A 6.542-second cinematic take (16:9) of open sea at night far from any land, one clip, one "
   "continuous take, one change: **one point of the horizon answers, and it does not grow.**\n\n"
   "⚠️ **No person is in this frame and no part of the raft is in it either — the water is alone, at every distance and in every focus.**\n\n"
   "0-2.002s: **the sea and the horizon, uniform** — the water moving, no point on the line brighter "
   "than any other.\n"
   "2.002-4.501s: **the darkness thins at one point on the horizon** — a slight lift, no shape, no "
   "edge — **and the waves keep moving while that brightness does not move.**\n"
   "4.501-6.542s: **the camera approaches that one point very slowly and at a constant speed**, and "
   "**the brightness stays exactly the size it was** — the take ends before the point resolves.\n\n"
   "**The answer is in the world, not in the camera: the brightness arrives at 2.002s, before any "
   "camera movement begins, and the approach never changes it. No light source changes; the stars are "
   "the only light and they stay as they are. No visible cause for the brightness appears in the "
   "frame.** **No island, no land, no shore, no sail, no bird, no other vessel, and nothing warm in "
   "the frame.** **No person is in this frame at any distance or in any focus, and no woman is in it "
   "at all.** **This is a bronze-age sea before classical Greece: no made thing of any later age.** "
   "**This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: one point of the horizon answers, and it does not grow.)"),

 "visual_scene": (
   "Open sea at night, far from any land, photographed as a film frame, low over the water: **long low "
   "swells with no white water, moving steadily in one direction, the surface fine-grained and broken, "
   "and one broken path of reflected starlight lying across the near water as short strokes.** The "
   "horizon runs level and unbroken across the frame, darker than the sky and darker than the water, "
   "and **at one point on that line the darkness is very slightly thinner than it is anywhere else on "
   "the line — a slight lift with no shape, no edge and no colour of its own.** The sky above is black "
   "with stars, and the stars do not brighten. **Nothing else is in the frame: no shore, no island, no "
   "sail, no bird, no vessel, no person, no moon.**"),

 "visual_meta": K.VISUAL_META.replace(
   "a gentle flare where the light is in frame",
   "a gentle flare on the one reflected path").replace(
   "a graded palette of cold slate blue in the water and the wet stone, warm ochre where the low sun "
   "falls",
   "a graded palette of black water with one broken white path of reflected starlight, and no warm "
   "tone anywhere in the frame").replace(
   "Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked; wet shingle "
   "with individual stones",
   "The water's surface fine-grained and broken; no wool, no cloth, no skin and no stone anywhere in "
   "this frame") + (
   " ⚠️ **No person is in this frame at all, at any distance and in any focus: this shot is the sea "
   "alone, with no figure in it and no part of the raft in it.**"),

 "motion_prompt": (
   "Full animation, not limited. **The waves are the movers; the one brightness on the horizon does "
   "not move and does not grow.** The swell runs in one direction at a steady rate with no crest and "
   "no white water, and the reflected path of the stars breaks into short strokes on its face and "
   "re-forms. **From 4.501s to the end the camera approaches that one point very slowly and at a "
   "constant speed, and the point stays small in the frame as it comes** — **its apparent size in the "
   "frame changes only as much as the camera's approach changes it, and its brightness is the same "
   "size in the last frame as in the frame where it first appeared.** **Nothing else moves: nothing "
   "enters the water and nothing crosses the line.** No motion blur smears, no stutter, no floaty "
   "weightless motion, no static frames — **the water moves in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **low just above the water, the horizon running high across the frame, the one "
   "bright point small on that line.** **The camera event: from 4.501s to the end of the clip, one "
   "very slow dolly-in toward that point, at a constant speed, inward only** — no lateral drift, no "
   "rise, no fall — **ending while the point is still small and unresolved.** ⚠️ **The style permits "
   "a dolly, a crane and a Steadicam, and this shot spends the dolly.** **This move has a motive that "
   "the style allows — the question of whether anything is there — and it is not the shot's answer: "
   "the answer arrived in the world at 2.002s, before the move began.** No crane is used, and no "
   "Steadicam. No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
   "and **no unmotivated move.**"),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **long low water moving, and the fine sound of an unbroken "
   "surface sliding against itself.** ⚠️ **No crest breaks and nothing slaps or slaps back.** "
   "⚠️ **No wood, no cordage and no oar are heard: the raft is not in this frame and not in this "
   "shot's sound.** ⚠️ **No bell, no bird and no shore reaches this shot** — the brightness on the "
   "horizon has no sound of its own. ⚠️ **Nothing here is silent — the water is the subject of this "
   "shot's sound.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (meaning-responsive) ／ "
                        "REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**"
                        "（裁定②。そしてこの経路は既定で何も添付しない）。"
                        "⚠️ **参照集合が `男.identity` を挙げていても、この1本は同一性の塊を §18 に貼らない**——**記録の `unit` と `beats` のどこにも、人物が現れないからである**（§3 と §15 を見る）。"
                        "⚠️ **この1本の主題は `海` と `海.geography` である**"
                        "（`舟` は画の外にある）。",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water only ／ no music",
 "unresolved": [
   "⚠️ **カードの `avoid` の一番目（「A camera move … standing in for the answer」）と、"
   "記録の「カメラはその一点へ、ごくゆっくり寄る」が、字面では食い違う。**"
   "⚠️ **記録が正である**——**ゆえにこの仕様は寄ることを書いた。**"
   "⚠️ **そして食い違いを、時間の順序で解いた****——答えは2.002秒に来て、"
   "カメラは4.501秒から動く。****ゆえに寄ることは、答えの原因でも、答えそのものでもない。**"
   "⛔ **この解き方が通るかどうかは、絵を見て決めることである。**"
   "**通らなければ、寄ることを落とし、答えだけを残すのが、"
   "この形式の側の正しい形である。**",
   "⚠️ **この1本の初出が、`s04`（`pre-chorus` の終わり）と字面上は近い。**"
   "⚠️ **`s04` が何を写すかを、この仕様は確かめていない**（この1本の担当の外である）"
   "——**両方が「明るい一点」であれば、同じ画が2度来ることになる。**"
   "**確かめるのは著者である。**",
 ],
 "risks": [
   "⛔ **明るさが大きくなる。** この1本の最大の危険である——**大きくすれば、"
   "この行は「島へ着く」になる。** 禁制は §16 と `Master Prompt` の散文の両方に在る。",
   "⛔ **陸が入る。** ⚠️ **明るい一点を、この経路は島の輪郭として描きたがる**"
   "——**そしてこの作品は帰り着かない。**",
   "⛔ **人が入る。** ⚠️ **この1本の画には、人が一人も入ってはならない**——**この経路は、夜の海の画に人物を足したがる。**",
   "⛔ **光の柱、光芒、レンズフレアが、答えの代わりに入る。** ⚠️ **この1本の答えは、"
   "暗さが薄いことであって、光が射すことではない。**",
   "⛔ **舟が入る。** ⚠️ **夜の海の画は、この経路では手前の構造物を足したくなる。**",
   "⚠️ **カメラの寄りが速すぎる。** ⚠️ **この1本の移動は、"
   "「ごくゆっくり」でなければならない**——**速ければ、それは答えを主張する移動になる。**",
   "⚠️ **波が止まる。** ⚠️ **この1本で止まってよいのは、あの一点だけである。**"
   "**波が止まれば、`mode: motion` が成立しない。**",
 ],
}
