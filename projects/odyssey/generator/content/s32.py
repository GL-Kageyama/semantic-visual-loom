# -*- coding: utf-8 -*-
"""odyssey-s32 — time-fold — 海 / 夜 / 6.702s. l33「まだ着かない」（2度目）。"""
import common as K


C = {
 "n": "s32",
 "title": "近づかない時間そのもの",
 "duration": "6.702",
 "format": "time-fold",
 "has_man": False,
 "segment": "final-chorus-6",

 "band": [
   "『永遠より遠い』 final-chorus「海」 / 余白 / still —— まだ着かない——2度目。近づかない時間そのもの",
   "明るさは同じ位置にあり、波が同じ形で何度も寄せる。",
   "6.702秒、カメラは三脚の上で波の一周期を丸ごと写す——もう一度同じ周期が始まるのが、切れ目である。",
   "時間は過ぎるが、距離には変わらない——一歩も近づかない。",
 ],
 "header": """⚠️ **`l33`「まだ着かない」の2度目である。****同じ行が2度歌われる**（記録の逐語）。
⛔ **この作品は、同じ行に同じ役（`余白`）と同じ `mode`（`still`）を与え、形式だけを変えた**——
**`s31` は `meaning-responsive`、この1本は `time-fold` である**（記録の逐語）。
⛔ **2つの形式が、2つの違うことを言う**——**`s31` は「意味に反応して、近づかない」であり、**
**この1本は「時間そのものが、距離にならない」である**（記録の逐語）。
⚠️ **`L36` が「同じ行を2回覆う」を註にする**（`s22` の註を見る）。
⚠️ **この1本の直後に、この作品の最後の行が来る**（`l34`「耐えよ わが心よ」）。
⛔ **この1本の画には、人が一人も入らない。****記録の `unit` と `beats` のどこにも、人物が現れない**——
**ゆえにこの1本は、人を一人も置かない。**（§3 と §15 を見る）。
⚠️ **この仕様のショット記録は `shots/odyssey-s32.yaml` である。**""",

 "intent": "**同じ一行の2度目に、別の何かを返せるか。** ⚠️ **`s31` が「近づかない」であり、"
           "この1本は「その時間そのもの」である**（`aim` の逐語）。"
           "⛔ **この1本の時間は、過ぎない。****そして止まりもしない。**"
           "**時間が、距離に変わらない**（`motion.law` の逐語）。"
           "⚠️ **同じ画を2度置くことが、この1本の設計である**——"
           "**2度目であることが、この1本の内容である。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本の場所は `海`、時刻は `夜` である。****陸は、どこにも無い。**"
   "⛔ **この作品は、帰り着かない**（`world.rules` の五番）。"
   "⚠️ **この1本が置くのは、時間そのものである**——"
   "**波が一つの周期を描き、そして同じ周期がもう一度始まる。**"
   "**そのあいだ、あの一点は同じ位置にある。**"
   "⛔ **ゆえにこの6.702秒は、過ぎた時間ではなく、"
   "測られた時間である**——**測っても、距離にならない。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本の画には、人が一人も入らない。****ゆえにこの規則は、"
               "この1本では「人に返事が来ない」としてではなく、"
               "** 「世界が、人に向かわずに在る」として効く。****それでも返事は返らない。**"
               "**周期が何度巡っても、あの一点は、何も返さない**"
               "——**巡ることそのものが、この1本の時間である。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "⛔ **この1本でも、あの明るさを彼女の形にしない**——"
                "**人のかたちも、手のかたちも、光の柱も作らない。**",
     "name": "⚠️ **この1本に名は無い。** ⛔ **そしてこの1本も、"
             "あの明るさに名前を与えない**——**島とも、岸とも、家とも呼ばない。**",
     "bow": "⚠️ **この1本に弓は無い。****舟も、斧も、帆も、この1本の画には無い。**",
     "places": "この1本が置くのは一つ——`海`、**この作品でいちばん多く写る場所である**"
               "（`ledger.locations.海` の実測註——19本）。"
               "⛔ **そしてこの1本では、その場所が「時間の器」になる**"
               "——**`time-fold` の逐語:「**the frame is the container, not the traveller**」。**",
     "japanese": "⚠️ **この1本には歌がある**——`l33`「まだ着かない」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **形式 `time-fold` の文法は「`video-spec` に一つの文法を足したもの」である**"
     "（カードの逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card "
     "requires; what follows is only what this grammar adds to it.」）。"
     "⚠️ **この1本の文法は §8 に書かれる**（カードの `Sources` の逐語:「Its grammar is written into "
     "the `video-spec` skeleton — **§8 TEMPORAL STRUCTURE** — which already asks for deliberately "
     "unequal second ranges; this card is that instruction taken to its end.」）。"
     "**ゆえにこの1本の本体は、ビートの配分そのものである。**",
     "⚠️ **カードの逐語:「**Distinguish from `coexisting-realities`.** Here the times *succeed one "
     "another* — one place at many moments. There they coexist and none is earlier.」"
     "⛔ **ゆえにこの1本では、波の周期が順に来る**——**寄せて、返して、"
     "もう一度寄せる。****`s29` の二つの距離は、これとは逆である**"
     "（あちらは順に来ない）。",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, far from any land, photographed as a film frame. **The frame holds the water, "
     "the horizon and the sky above it, and nothing else**: long low swells with no white water, "
     "**coming in and returning in one visible cycle and then beginning that same cycle again**, and "
     "one broken path of reflected starlight on the near water. **On the horizon's line, at one point, "
     "the darkness is slightly thinner than it is anywhere else on the line** — the same point, the "
     "same size, at the same distance, the whole clip. ⚠️ **No land, no island, no shore, no sail, no "
     "bird, no vessel of any kind — and no part of the raft in the frame.**",
   "Color Language":
     "A narrow, graded palette, and it has one source: **the night is lit by the stars and by their "
     "reflection on the water, so the waves are black and the reflected path alone is white**"
     "（`ledger.locations.海.states.夜` の逐語:「光源は星と、その水面の反射だけである。波は黒く、"
     "反射の道だけが白い。」）. ⚠️ **The one bright point on the horizon is not a second colour** — "
     "**it is the same black, lifted a little.****Nothing warm enters the frame, and nothing glows.**",
   "Texture":
     "The water's surface fine-grained and broken, long low swells with no crest and no white water; "
     "the reflected path broken into short strokes on the moving face of the water; **the swell's face "
     "carrying the same grain at the same scale through every pass of its cycle**; **the sky's grain "
     "slightly coarser where the darkness thins at that one point on the horizon**; even film grain, "
     "visible in the black. ⚠️ **There is no shingle, no stone, no wool, no skin and no cloth in this "
     "frame.**",
   "Rendering":
     "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, **a gentle flare "
     "on the one reflected path**. **Not a photograph's stillness: a film frame, with a real lens's "
     "fall-off at the edges.** No illustration, no CGI look, no cartoon color.",
   "Visual Density": "**Low, and it does not change over the entire 6.702秒.**"
                     "⚠️ **この1本は `mode: still` であり、密度も止まっている**"
                     "——**波の周期は密度を変えない。****同じ量の水が、"
                     "同じ量の光を受けて、同じところまで来て、同じところまで返る。**",
   "Time": "`夜` — the source is the stars and their reflection on the water; the waves black and the "
           "reflected path alone white. ⚠️ **この作品は一日のうちの三つの時刻しか使わない**"
           "（`日没`・`夜`・`夜明け`）。**画の中に日付を与えるものは何も無い。**"
           "⛔ **そしてこの1本では、時刻が進まない**——**周期が巡っても、"
           "夜は夜のままである。**",
   "Atmosphere": "The night measured by a wave's own cycle — and the measure changes nothing.",
 }),

 "subjects": [
   {"name": "あの一点",
    "ref": "⛔ **この1本の `SURVIVOR` である。****周期が何度巡っても、"
           "これだけが変わらない**（カードの逐語:「**One survivor.** Something in the frame does not "
           "change across the whole span — that is what makes the passage legible as time rather than "
           "as several unrelated states.」）。"
           "⚠️ **参照は `ledger.locations.海.geography` の逐語と、`海.base` の "
           "「At night the surface carries one broken path of reflected light」である。**"
           "⚠️ **参照画像は無い**（裁定②）。",
    "appearance": "**水平線の上の、一点である。****そこだけ、暗さがわずかに薄い。**"
                  "**縁も、輪郭も、にじみも無い。**"
                  "⚠️ **形を持たない。****島にも、帆にも、灯にも読めない。**",
    "behavior": "⛔ **動かない。****この6.702秒のあいだ、同じ位置に、同じ大きさで在る**"
                "——**波が一つの周期を描いても、"
                "そして同じ周期がもう一度始まっても、この一点は同じ位置にある**"
                "（`beats` の3番目の逐語）。"
                "⚠️ **この1本で「時が経った」と言えるのは、"
                "この一点が動かないことによってだけである。**",
    "continuity": "**Must preserve** — 位置、大きさ、形を持たないこと、"
                  "そして**周期が巡っても変わらないこと**。"
                  "**May change** — 暗さの薄さの度合い（ごくわずかに揺れてよい）。",
    "notes": ["⛔ **この一点を、この1本は動かさない。****動けば、"
              "この1本の時間を測るものが消える**——**「過ぎた」と「変わった」の区別が、"
              "そこで失われる。**",
              "⛔ **この1本の画には、人が一人も入らない。****記録の `unit`（前・後）と `beats` のどこにも、人物が現れない**"
              "——**ゆえにこの1本は、人を一人も置かない。**"
              "**参照集合は「固定するもの」を挙げており、「画に居る者」を挙げているのではない。**（§15 の `identity` を見る）"]},
   {"name": "波の周期",
    "ref": "⛔ **この1本の `PASSES` である。****時間がこの場所に対してすることを、"
           "これが担う。** ⚠️ **参照は `ledger.locations.海.base` の逐語"
           "（「Long low swells with no white water, moving steadily in one direction」）。**",
    "appearance": "**長く低いうねりである。****白波を立てない。****一つの方向へ動き、"
                  "寄せて、返す。**"
                  "⚠️ **一つの周期が、この1本の時間の単位である**"
                  "——**波そのものが、この1本の時計である。**",
    "behavior": "**寄せて、返す。****そして、同じ周期がもう一度始まる**"
                "（`beats` の3番目の逐語:「**もう一度、同じ周期が始まる。**」）。"
                "⛔ **周期は、同じ形で来る**"
                "（`motion.quality` の逐語:「**波が、同じ形で何度も寄せる。**」）"
                "——**違う波ではない。****同じ形が、もう一度である。**",
    "continuity": "**Must preserve** — うねりの低さ、白波が無いこと、"
                  "**そして周期が同じ形で来ること**。"
                  "**May change** — 位相、反射の線の位置、うねりの高さのごくわずかな差。",
    "notes": ["⚠️ **この1本の時間の単位は、秒ではなく周期である。**"
              "**秒は、周期を数えるためにある**——**この1本は、"
              "一つの周期と、その次の周期の始まりを写す。**",
              "⛔ **周期の数を、この仕様は数え直していない。****記録のビートは"
              "「一つの周期」（1.997–4.504秒）と「もう一度、"
              "同じ周期が始まる」（4.504–6.702秒）を挙げている。**"
              "**ゆえにこの1本は、周期を「一つ、そして次の一つの始まり」として書く。**"]},
 ],

 "environment": {
   "location": "`海` — **夜である。****四方を水に囲まれ、どの方向にも陸が見えない**"
               "（`海.geography` の逐語）。⚠️ **カメラは固定されている。****記録は"
               "「三脚の上」と書く**（`motion.quality` の逐語:「**カメラは三脚の上で、"
               "波の一つの周期を丸ごと写す。**」）——⛔ **三脚そのものは画に入らない。**"
               "⛔ **舟も、人も、この1本の画には入らない。**",
   "elements": "**長く低いうねり**、**寄せて返す一つの周期**、**同じ形で来る2度目の周期**、"
               "**星の反射の道**、**平らで途切れない水平線**、**その一点だけ薄い暗さ**、"
               "そして**その上の空**。"
               "⛔ **陸も、島も、帆も、鳥も、他の船も無い。**"
               "⛔ **そしてこの1本の画には、人が一人も入らない。**",
   "behavior": "⛔ **この1本の出来事は、周期が巡ることである。****波が寄せて返り、"
               "そして同じ周期がもう一度始まる**——**あの一点は、"
               "そのあいだ、同じ位置にある。**"
               "⚠️ **時間は、この場所を変えない。****変わるのは、"
               "水の位置だけである。**",
 },

 "objects": [
   "**無い。** ⚠️ **この1本の画には、物が一つも無い**——**水と、水平線と、その一点と、"
   "その上の空だけである。**",
   "⚠️ **`ledger.props` の4つ（舟・帆・斧・太陽の牛）は、この1本には来ない。**"
   "**参照集合が `舟` を挙げているのは、この作品の場所と、彼が乗っているものを固定するためである**"
   "——**舟はこの1本の画角の外にある。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本の画には入らない。****この1本のどこにも、人物が現れない**（§3 と §15）。"
                  "`女神` — **この1本には添付しない。** "
                  "⚠️ **`男.identity` と `男.negatives` が集合に在っても、それは外見を固定するためであり**",
 "ref_extra": [
   "- ⚠️ **形式カード `time-fold` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; "
   "what follows is only what this grammar adds to it.」）。"
   "**ゆえに §1–20 の骨格は `s01` と同じであり、違うのは §8 の組み方である。**",
   "- ⚠️ **カードの逐語:「**The camera is the anchor.** The place is held. The camera may not cut away "
   "and re-enter, because coming back to the place is a second shot and this grammar's whole claim is "
   "that it was never left. **A fixed frame is the native case.**」"
   "⛔ **ゆえにこの1本のカメラは動かない**——**動かないことが、この形式の本来の形である。**",
   "- ⚠️ **カードの逐語:「**Uneven duration.** The seconds are not spread evenly over the span; choose "
   "the part of the passage the shot lingers on.」****この1本が長く留まるのは、"
   "2番目のビート（1.997–4.504秒、2.507秒）である**——**周期そのものである。**"
   "**3番目のビート（4.504–6.702秒、2.198秒）は、"
   "同じ周期の始まりであり、周期はそこで切れる。**",
   "- ⚠️ **形式カード `time-fold` の5つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `PLACE`＝the place that holds still — **`海` である。****この作品でいちばん多く写る場所である**"
   "（`ledger.locations.海` の実測註——19本）。",
   "  - `PASSES`＝what time does to it — **波の周期である。****寄せて、返して、"
   "同じ形でもう一度始まる。****この1本の時計は、波そのものである。**",
   "  - `SURVIVOR`＝what does not change across the span — **あの一点である。**"
   "**周期が何度巡っても、同じ位置に、同じ大きさで在る。**"
   "⚠️ **これが無ければ、この1本は「いくつかの無関係な状態」に見える**"
   "（カードの逐語）。**カメラも、この1本では同じ役をする**（固定されている）。",
   "  - `RANGE`＝the span of time the shot crosses — ⛔ **この1本では、"
   "尺度を持った時間ではない。****波の一つの周期と、その次の周期の始まりである。**"
   "**6.702秒という長さは、その巡りを数えるうちに尽きる**"
   "——**時間は距離に変わらない**（`motion.law` の逐語）。",
   "  - `DURATION`＝clip length — **`6.702s`。**",
   "⚠️ **カードの `Negative` の逐語:「no cut, no time-skip, … no return to the place after leaving "
   "it」**——**この1本は場所を離れない。****ゆえにこの禁制のうち、"
   "この1本が最も強く受けるのは「切らないこと」である。**",
 ],

 "narrative": {
   "core": "**同じ一行の2度目に、別の何かを返せるか** — **この1本は「近づかない時間そのもの」である。**",
   "beginning": "**一点と、その周りの海。****距離がある。**"
                "⚠️ **この1.997秒で、この1本の場所と、"
                "そこにある距離が立てられる。**",
   "turn": "**波が一つの周期を描く。****寄せて、返す。****一点は動かない。**"
           "⚠️ **この1本の時間は、ここで初めて数えられる**"
           "——**波が、この1本の時計になる。**",
   "peak": "**もう一度、同じ周期が始まる。****一点は同じ位置にある。**"
           "⚠️ **時が経った証拠は、これだけである**——**同じ形が、"
           "もう一度来たこと。**",
   "pull": "⚠️ **周期が始まることが、切れ目のコマである。**"
           "**そしてこの1本の直後に、この作品の最後の行が来る**（`l34`）"
           "——**この作品は、着かないまま最後の行へ渡る。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and the unevenness is the content.** ⚠️ **この1本の配分は、"
            "`s31` とほぼ同じでありながら、意味が違う**"
            "——**`s31` は3つのビートを持ち、この1本は2つの周期を持つ。** "
            "**2.507秒（周期そのもの）と、2.198秒（同じ周期の始まり）である。**"
            "⛔ **この1本が長く留まるのは、周期の側である**"
            "（カードの逐語:「**choose the part of the passage the shot lingers on**」）。"
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**波はこの1本でも動き続ける。**",

 "actions": [
   ("ACT_SHOW", "一点と、その周りの海がある。**距離がある。**",
    "**場所と、そこにある一点と、その間の距離が立てられる**"
    "——**まだ、時は数えられていない。**"),
   ("ACT_CYCLE", "波が、寄せ始めている。",
    "**波が一つの周期を描く**——**寄せて、返す。****そのあいだ、"
    "一点は動かない。****時が、波の形で数えられる。**"),
   ("ACT_RESTART", "周期は、返し終えている。",
    "**同じ形の周期が、もう一度始まる**——**そして一点は、"
    "同じ位置にある。****周期が始まることが、この1本の切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **low over the water, the horizon running high across the frame, the one "
               "point small on that line** — **and this framing is the whole clip.** "
               "⚠️ **この1本の画角は、波の周期を丸ごと入れるために在る**"
               "——**寄せて返すまでが、一つの画に入る。**",
   "events": "**None. The camera does not move at all.** ⚠️ **記録は、"
             "この1本のカメラを「三脚の上」と書く**"
             "（`motion.quality` の逐語:「**カメラは三脚の上で、"
             "波の一つの周期を丸ごと写す。**」）。"
             "⛔ **この1本の形式では、固定が本来の形である**"
             "（カードの逐語:「**A fixed frame is the native case.**」）。"
             "⚠️ **ゆえにこの1本の §10 には、時刻を持つ出来事が一つも無い。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends none of "
               "them** — ⚠️ **この1本にはカメラ移動の動機が一つも無い**——"
               "**様式の法は「動機の無い移動を禁じる」であり、"
               "この1本は時間を写すのであって、場所を移るのではない**"
               "（カードの逐語:「**the frame is the container, not the traveller**」）。 "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and **no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、波の周期である。**"
              "**寄せて、返して、同じ形でもう一度始まる。****あの一点は動かない**"
              "（`motion.quality` の逐語:「**波が、同じ形で何度も寄せる。****あの明るさは動かない。**」）。",
   "object": "⚠️ **この1本には、動く物が無い。****動くのは水だけである。**"
             "⛔ **そして、あの一点は物ではない。**",
   "environment": "**星の光が、静的な光源として画面の外に在る。****その反射が、"
                  "動く面の上で短い線に砕ける。**"
                  "⚠️ **周期が巡っても、光は変わらない**——"
                  "**変わるのは、水の位置だけである。**",
   "weight": "**うねりは低く、質量は水のものである。****速さは周期ごとに同じである。**"
             "⚠️ **この1本の重さは、周期の一定さに現れる**"
             "——**同じ形で来ることが、この1本の時間の重さである。**",
   "inertia": "**返し切るまで、波は止まらない。****そして返し切ったところで、"
              "次の周期が始まる。**"
              "⚠️ **この1本に、間（ま）は無い**——**周期と周期は、"
              "続いている。**",
   "acceleration": "**加速しない。****周期の速さは、"
                   "最初から最後まで同じである。**"
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この6.702秒に、"
               "止まったフレームは一つも無い**——**`mode: still` は、"
               "画面が止まることを意味しない。**",
   "impact": "**無い。** ⛔ **この1本に衝撃は一つも無い**——"
             "**周期が巡ることは、出来事ではない。**"
             "**同じことが、もう一度である。**",
 },

 "emotion": {
   "arc": "**同じことの2度目を、飽きずに持てるか。** ⚠️ **この1本は、"
          "`s31` と同じ主題を、別の形式で置く**"
          "——**`s31` は「近づかない」であり、この1本は「その時間そのもの」である。**"
          "⛔ **2度目を、繰り返しにしない。****繰り返しを、"
          "時間の測り方に変える**——**それがこの1本の感情である。**",
   "events": "⚠️ **この1本の出来事は、同じ周期がもう一度始まることである。**"
             "⚠️ **人が居ないので、この1本には感情の担い手が一人も居ない。**",
 },

 "lighting": {
   "base": "**夜である。****光源は星と、その水面の反射だけである。****波は黒く、"
           "反射の道だけが白い**（`ledger.locations.海.states.夜` の逐語）。"
           "⚠️ **この1本の光源は一つであり、それは星である。**"
           "⚠️ **月も、火も、灯も無い。**",
   "events": "**None.** ⛔ **この1本では、光の出来事が一つも起きない**"
             "——**周期が巡っても、明るさは変わらない。**"
             "**あの一点も、`s30`・`s31` と同じ大きさのままである。**"
             "⚠️ **この1本の時間の変化は、"
             "波の形だけが運ぶ**——**光は、この1本の時計ではない。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水の音だけである。****長く低いうねりが動く音、砕けない面が擦れる音。**"
          "⚠️ **打ち上げる音は無い**——**この海は白波を立てない。**"
          "⚠️ **木の音も、縄の音も、櫂の音も無い**——**舟はこの1本の画にも音にも入らない。** "
          "⚠️ **周期が巡っても、音は同じである**——**寄せと返しで音の量は変わらない。**",
   "music": K.NO_MUSIC + " ⚠️ **そしてこの1本には、歌が在る**——`l33`「まだ着かない」であり、"
            "**行の長さが、そのままこの1本の長さである**（274.787–281.489。**6.702秒**"
            "——`bible.song` の `final-chorus` の実測である）。"
            "**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜の外海。**水と、その上の空気だけである。**"
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
              "direction, including behind.」）。⚠️ **カメラは低く、水面のすぐ上にあり、"
              "固定されている。****この6.702秒のあいだ、"
              "画角は一度も変わらない。**"
              "⚠️ **この1本で、この海が `s31` の海と同一であることが保たれる**"
              "（`海.geography` の逐語:「**the same waterline and the same horizon appear in both**」）。",
   "temporal": "**夜である。****この作品の三つの時刻のうちの一つである**"
               "（`日没`・`夜`・`夜明け`）。⚠️ **この作品は曲に従って時刻を選んでおり、"
               "時計には従っていない**（`bible.time_source: song`）。"
               "**画の中に日付を与えるものは何も無い。**"
               "⛔ **そしてこの1本は、日付や時間を画面に書かない**"
               "（カードの `Negative` の逐語:「**no date stamp, no caption, no title card carrying "
               "elapsed time**」）——**経過は、波の形だけが運ぶ。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は星の光だけである。**"
             "⚠️ **そしてこの1本の一点は、`s31` の一点と同一でなければならない**"
             "——**位置も、大きさも、暗さの薄さの度合いも、"
             "`s31` の最後のコマのままである。**"
             "⛔ **この3本（`s30`・`s31`・`s32`）は、"
             "一つの明るさを引き継いでいる。**",
   "motion": "Full animation, not limited. **波が、同じ形で寄せて返す。** "
             "⚠️ **カメラは一度も動かない。****あの一点は、"
             "この6.702秒のあいだ、一度も動かない。**",
   "sound": "水だけ。**音楽なし。言葉なし。** ⚠️ **主題歌はこの1本のあいだ鳴っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "⚠️ **この1本の画には、人が一人も入らない**——**ゆえに女神の禁制は、"
     "「彼女を人のかたちで置かない」だけでなく、「**人の形を一つも置かない**」として効く。**")) + [
   "**No person in this frame at all** — ⚠️ **この1本には、人が一人も入らない。**",
   "**No second person in frame at any distance, in any focus.**",
   "**No cut, no time-skip, and no return to the place after leaving it** "
   "（逐語, カードの `Negative`）——⛔ **この1本は場所を離れない。**",
   "**No camera move of any kind** — **カメラは固定されている。**",
   "**No date stamp, no caption, and no title card carrying elapsed time** "
   "（逐語, カードの `Negative`）——**経過は、波の形だけが運ぶ。**",
   "**No aging makeup, no prosthetic, and no stated \"years later\"** （同、逐語）。"
   "**この1本の時間は、人の側に何も残さない。**",
   "**Nothing in the frame changes except the water** — ⛔ **あの一点を動かさない。**"
   "**動けば、この1本の時間を測るものが消える。**",
   "**No island, no land, no shore in this frame** — ⛔ **この作品は、"
   "帰り着かない**（`world.rules` の五番）。",
   "**No boat, no ship, no hull, no other vessel in frame** "
   "（`ledger.locations.海.base` の逐語:「No land, no sail, no bird, no other vessel.」）。",
   "**No beam, no ray, no shaft of light, and no lens flare.**",
   "**No white water, no breaking crest, no spray** — **この海は白波を立てない。**",
   "**No caption naming the meaning, and no voice-over naming it.**",
 ],

 "must": [
   "⛔ **周期が同じ形で来ること** — **違う波を、2度目にしない。**",
   "⛔ **あの一点が動かないこと** — **`SURVIVOR` が無ければ、"
   "この1本は「いくつかの無関係な状態」に見える。**",
   "⛔ **カメラが動かないこと** — **この形式では、固定が本来の形である。**",
   "⛔ **人が一人も入らないこと。**",
   "⚠️ **あの一点が `s31` の最後のコマと同一であること。**",
   "⚠️ **時間が距離に変わらないこと** — **周期が巡っても、"
   "距離は一歩も変わらない。**",
   "⚠️ **配分が均等でないこと** — **長く留まるのは周期の側である。**",
   "⛔ **人が一人も入らないこと** — **この枠は、海だけで在る。****参照集合が人の外見を挙げていても、それは画に人を置く指示ではない。**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **変化は最後のコマで終わる** — **周期が始まることが、切れ目のコマである。**",
 ],

 "prefer": "The night held black and the reflected path the only white; the swell kept long, low and "
           "crestless; **the cycle kept identical in shape on its second pass**; **the one point on the "
           "horizon kept at exactly the same position and size from the first frame to the last**; "
           "**the camera held absolutely still.**",
 "allow": "The reflected path breaking into short strokes and re-forming; the swell's height varying "
          "slightly through the cycle; **the second pass beginning before the first has fully "
          "settled**; **a gentle flare on the one reflected path.**",

 "priorities": [
   "⛔ **あの一点が動かないこと** — **`SURVIVOR` であり、"
   "破れれば時間が測れなくなる。**",
   "⛔ **周期が同じ形で来ること** — **この1本の時計である。**",
   "⛔ **カメラが動かないこと。**",
   "⛔ **人が一人も入らないこと。**",
   "⚠️ **距離が変わらないこと** — **着かないことが、この作品の主題である。**",
   "⛔ **人が一人も入らないこと** — **この枠は、海だけで在る。****参照集合が人の外見を挙げていても、それは画に人を置く指示ではない。**",
   "**No second person, at any distance, in any focus.**",
   "**光は星の光だけであること。**",
   "⚠️ **この1本が 6.702秒であること**（曲の `l33` の実測である）。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `time-fold` を名乗るが、その禁制（`no cut`・`no time-skip`・`no date stamp`・"
   "`no cross-dissolve`・`no return to the place after leaving it` ほか）は §16 に在って、"
   "ここには無い。** **ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。** "
   "⚠️ **この形式の文法は §8 に書いた**——**この節に持ち込めば、34本の同一性が崩れる。**"),

 "master": (
   "A 6.702-second cinematic take (16:9) of open sea at night far from any land, one clip, one "
   "continuous take, one change: **the same cycle begins again, and the distance has not changed.**\n\n"
   "⚠️ **No person is in this frame and no part of the raft is in it either — the water is alone, at every distance and in every focus.**\n\n"
   "0-1.997s: **the one point and the water around it, with distance in them.**\n"
   "1.997-4.504s: **the swell draws one whole cycle** — in, and back — **and the point does not "
   "move.**\n"
   "4.504-6.702s: **the same cycle begins again, in the same shape** — **and the point is in the same "
   "place** — and the take ends there.\n\n"
   "**The camera is fixed and never cuts: this frame is the container, not the traveller.** **One "
   "light only — the stars and their reflection, unchanged through every pass of the cycle.** **The "
   "one point on the horizon stays at the same size, the same brightness and the same place as in the "
   "shot before this one, and it does not move.** **No island, no land, no shore, no sail, no bird, no "
   "other vessel, and nothing warm in the frame.** **No person is in this frame at any distance or in "
   "any focus, and no woman is in it at all.** **This is a bronze-age sea before classical Greece: no "
   "made thing of any later age.** **This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the same cycle begins again, and the distance has not changed.)"),

 "visual_scene": (
   "Open sea at night, far from any land, photographed as a film frame, low over the water: **long low "
   "swells with no white water, drawing one visible cycle — in, and back — and then beginning the same "
   "cycle again in the same shape**, the surface fine-grained and broken, and one broken path of "
   "reflected starlight lying across the near water as short strokes. The horizon runs level and "
   "unbroken across the frame, darker than the sky and darker than the water, and **at one point on "
   "that line the darkness is slightly thinner than it is anywhere else on the line — the same point "
   "as in the previous shot of this work, at the same size and the same distance, with no shape and no "
   "edge and no colour of its own.** The sky above is black with stars, and the stars do not change. "
   "**Nothing else is in the frame: no shore, no island, no sail, no bird, no vessel, no person, no "
   "moon.**"),

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
   "Full animation, not limited. **The swell is the only mover: it draws one whole cycle — in, and "
   "back — and then begins that same cycle again in the same shape and at the same speed.** The "
   "reflected path of the stars breaks into short strokes on its face and re-forms as it passes. "
   "**The one point on the horizon does not move at all: it is in the same place, at the same size and "
   "at the same brightness in the first second and in the last.** **The camera does not move in this "
   "take: not laterally, not forward, not up, and it does not turn.** No motion blur smears, no "
   "stutter, no floaty weightless motion, no static frames — **the water moves in every frame of the "
   "take.**"),

 "camera_prompt": (
   "Third person, **low just above the water, the horizon running high across the frame, the one "
   "point small on that line.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot "
   "spends none of them** — the style's law forbids a move without a motive, and **this shot's frame "
   "is the container of a span of time, not a traveller through it: a fixed frame is this form's "
   "native case.** **There is no camera event in this shot, and it never cuts.** ⚠️ **Do not drift, do "
   "not creep, and do not let the frame breathe.** No handheld, no whip, no shake, no snap zoom, no "
   "rack focus, no unnatural rotation, and **no unmotivated move.**"),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **long low water moving, and the fine sound of an unbroken "
   "surface sliding against itself, through one whole cycle and then the same cycle again.** "
   "⚠️ **No crest breaks and nothing slaps or slaps back.** ⚠️ **No wood, no cordage and no oar are "
   "heard: the raft is not in this frame and not in this shot's sound.** ⚠️ **No bell, no bird and no "
   "shore reaches this shot.** ⚠️ **Nothing here is silent — the water is the subject of this shot's "
   "sound.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (time-fold) ／ "
                        "REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**"
                        "（裁定②。そしてこの経路は既定で何も添付しない）。"
                        "⚠️ **参照集合が `男.identity` を挙げていても、この1本は同一性の塊を §18 に貼らない**——**記録の `unit` と `beats` のどこにも、人物が現れないからである**（§3 と §15 を見る）。"
                        "⚠️ **この1本の場所は `海`、生存者はあの一点である。**",
 "camera_events_count": "no camera event — the camera does not move in this shot (§10)",
 "audio_events": "no dialogue ／ water only ／ no music",
 "unresolved": [
   "⚠️ **この1本と `s31` は、同じ主題を2度置く**（`l32`・`l33`「まだ着かない」）。"
   "⚠️ **記録は「同じ行に同じ役と同じ `mode` を与え、形式だけを変えた」と書く**"
   "——**ゆえに観客には、近い画が2度続いて見える。**"
   "⛔ **この仕様は、2本の差を「波の数え方」に置いた**（`s31` は近づかないこと、"
   "この1本は周期そのもの）。**その差が絵で読めるかは、絵を見て決めることである。**",
   "⚠️ **この1本の `RANGE`（跨ぐ時間の幅）を、この仕様は「波の一つの周期」とした。**"
   "⚠️ **カードは「years, a lifetime, a season」を例に挙げている**"
   "——**この1本は、それらを一つも持たない。**"
   "**記録の逐語は「時間が、距離に変わらない」であり、"
   "この仕様はそれを、波の周期という、いちばん短い尺度で読んだ。**"
   "⛔ **別の尺度（この海の、陸の無い時間そのもの）を採ることもできる。"
   "****決めるのは著者である。**",
   "⚠️ **カードの `Negative` の逐語は「no cut, no time-skip, … no return to the place after leaving "
   "it」であり、この1本はどれも犯していない。**"
   "⚠️ **ただし「場所を離れない」ことは、この1本では"
   "「カメラが動かない」ことと別ではない**——**この2つを、"
   "この仕様は§10と§15の両方に書いた。**",
 ],
 "risks": [
   "⛔ **あの一点が動く。** この1本の `SURVIVOR` である——"
   "**動けば、時間が測れなくなり、この1本は「いくつかの無関係な状態」になる。**",
   "⛔ **周期が、2つの違う波になる。** ⚠️ **2度目は「同じ形」でなければならない**"
   "（`motion.quality` の逐語）——**違う波を2つ写せば、"
   "この1本は「時間が過ぎた」ショットになる。**",
   "⛔ **カメラが動く。** ⚠️ **この形式では、固定が本来の形である。**",
   "⛔ **人が入る。** ⚠️ **この1本の画には、人が一人も入ってはならない**——**この経路は、夜の海の画に人物を足したがる。**",
   "⛔ **経過を示すものが画面に入る。** ⚠️ **日付、字幕、タイトルカードのどれか一つで、"
   "この1本は「何年かが過ぎた」ショットになる。**",
   "⚠️ **画が退屈になる。** ⚠️ **この1本は2度同じことをする**——"
   "**2度目の周期が、"
   "1度目と絵で区別できなければ、それは繰り返しではなく反復になる。**",
   "⚠️ **`s31` の一点と、この1本の一点が食い違う。**",
 ],
}
