# -*- coding: utf-8 -*-
"""odyssey-s31 — meaning-responsive — 海 / 夜 / 7.101s. l32「まだ着かない」（1度目）。"""
import common as K


C = {
 "n": "s31",
 "title": "まだ着かない、近づかない",
 "duration": "7.101",
 "format": "meaning-responsive",
 "has_man": False,
 "segment": "final-chorus-5",

 "band": [
   "『永遠より遠い』 final-chorus「海」 / 余白 / still —— まだ着かない——近づかないことを、7秒",
   "明るい一点が、同じ位置にあり続ける。",
   "7.101秒、波だけが動き続け、カメラも動かない——同じ距離のままであるのが、切れ目である。",
   "あの明るさは動かず、何も近づかない——この1本では、一歩も進まない。",
 ],
 "header": """⛔ **`l32`「まだ着かない」である。****この行は、この曲にしか無い**——
**`chorus-1`・`chorus-2` には無い**（記録の逐語）。
⛔ **着かないことが、この作品の主題である。**
**`world.rules` の五番**: 「**この作品は、帰り着かない。**」
⚠️ **この1本と `s32` は、その主題を2度置く**（記録の逐語）。
⚠️ **`mode: still`。****止まるのは主題である**——**近づくという主題が止まっている**（`aim` の逐語）。
⛔ **この1本は、`s30` の答えを持ち越している。**
**`s30` で水平線の一点が少し明るくなり、この1本はその続きである**——
**明るさは同じ位置にあり、7.101秒のあいだ、近づかない**（`unit` の逐語）。
⚠️ **形式は `meaning-responsive`。****`s30` と同じ形式である**——
**`s30` は「何でもない」に反応し、この1本は「まだ着かない」に反応する。**
⛔ **この1本の画には、人が一人も入らない。****記録の `unit` と `beats` のどこにも、人物が現れない**——
**ゆえにこの1本は、人を一人も置かない。**（§3 と §15 を見る）。
⚠️ **この仕様のショット記録は `shots/odyssey-s31.yaml` である。**""",

 "intent": "⛔ **近づかないことを、7秒で写せるか。** ⚠️ **`mode: still`——"
           "止まるのは主題である。****近づくという主題が、止まっている**（`aim` の逐語）。"
           "⛔ **この1本は、何も起きないことを7.101秒かけて確かめる。**"
           "**確かめることが、この1本の出来事である。** "
           "⚠️ **着かないことが主題である以上、この1本の画は、"
           "着かないことを肯定的に持たなければならない**——"
           "**暗い画でも、空しい画でもない。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本の場所は `海`、時刻は `夜` である。****陸は、どこにも無い。**"
   "⛔ **この作品は、帰り着かない**（`world.rules` の五番）。"
   "⚠️ **この1本が写すのは、その主題のいちばん静かな形である**——"
   "**あの少しの明るさが、同じ位置に、同じ大きさで在り続ける。**"
   "⛔ **この1本の中でも、一歩も近づかない。**"
   "**この1本は、間（ま）である**（役は `余白`）——"
   "**主題が止まっているあいだの、7.101秒である。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本の画には、人が一人も入らない。****ゆえにこの規則は、"
               "この1本では「人に返事が来ない」としてではなく、"
               "** 「世界が、人に向かわずに在る」として効く。****それでも返事は返らない。**"
               "**あの明るさは、7.101秒のあいだ、少しも近づかない**"
               "——**近づかないことが、この1本の答えである。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "⛔ **そしてこの1本でも、あの明るさを彼女の形にしない**——"
                "**人のかたちも、手のかたちも、光の柱も作らない。**"
                "**この1本には、与える者も、与えられた物も無い。**",
     "name": "⚠️ **この1本に名は無い。** ⛔ **そしてこの1本は、"
             "あの明るさに名前を与えない**——**島とも、岸とも、家とも呼ばない。**"
             "**呼べば、この1本は「そこへ着く」ショットになる。**",
     "bow": "⚠️ **この1本に弓は無い。****舟も、斧も、帆も、この1本の画には無い。**",
     "places": "この1本が置くのは一つ——`海`。⚠️ **そしてこの1本は、"
               "`world.rules` の五番を、いちばん正面から写す**——"
               "**「この作品は、帰り着かない」という一行が、"
               "この1本の設計そのものである。****ゆえにこの1本は、"
               "距離が縮まないことを、7.101秒かけて確かめる。**",
     "japanese": "⚠️ **この1本には歌がある**——`l32`「まだ着かない」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **形式 `meaning-responsive` の文法は「`video-spec` に一つの文法を足したもの」である**"
     "（カードの逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card "
     "requires; what follows is only what this grammar adds to it.」）。"
     "**この1本では、意味を運ぶもの（`BEARER`）は「あの一点までの距離」である**"
     "——**それは、何もしない。**"
     "**この1本の答え（`ANSWER`）は、世界の側に在る****——"
     "波が返り、同じ距離がそのまま残る。**",
     "⚠️ **カードの `do` の逐語:「Keep the answer's cause absent from the frame」**"
     "——**この1本では、距離が縮まないことに原因が無い。****舟の速度も、"
     "漕ぐ力も、帆も、この1本の画には無い。****ゆえにこの1本の「縮まない」は、"
     "** 効果ではなく事実として在る。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, far from any land, photographed as a film frame. **The frame holds the water, "
     "the horizon and the sky above it, and nothing else**: long low swells with no white water, moving "
     "steadily in one direction, and one broken path of reflected starlight on the near water. **On the "
     "horizon's line, at one point, the darkness is a little thinner than it is anywhere else on the "
     "line** — the same point, the same size, at the same distance, for the whole clip. ⚠️ **No land, "
     "no island, no shore, no sail, no bird, no vessel of any kind — and no part of the raft in the "
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
   "Visual Density": "**Low, and it does not change over the entire 7.101秒.**"
                     "⚠️ **この1本は `mode: still` であり、密度も止まっている**"
                     "——**動くのは波だけであり、密度を動かすものは一つも無い。**",
   "Time": "`夜` — the source is the stars and their reflection on the water; the waves black and the "
           "reflected path alone white. ⚠️ **この作品は一日のうちの三つの時刻しか使わない**"
           "（`日没`・`夜`・`夜明け`）。**画の中に日付を与えるものは何も無い。**"
           "⛔ **そしてこの1本では、時間が経っても何も変わらない**——"
           "**変わるのは波の位相だけである。**",
   "Atmosphere": "The hour in which nothing closes — the same distance at the last frame as at the "
                 "first.",
 }),

 "subjects": [
   {"name": "あの一点までの距離",
    "ref": "⛔ **この1本の `BEARER` である。****この行の「まだ着かない」を運び、何もしない。**"
           "⚠️ **参照は `ledger.locations.海.geography` の逐語と、`海.base` の "
           "「At night the surface carries one broken path of reflected light」である。**"
           "⚠️ **参照画像は無い**（裁定②）。",
    "appearance": "**水平線の一点と、この画とのあいだの距離である。****それ自体は見えない。**"
                  "**見えるのは、その一点が水平線の上で小さいことだけである**"
                  "——**小ささが、この距離の唯一の証拠である。**"
                  "⛔ **この距離には、目盛りが無い。****測る者も、この1本には居ない。**",
    "behavior": "⛔ **何もしない。****縮まない。****広がらない。**"
                "**この7.101秒のあいだ、最初のコマの距離が、最後のコマの距離である。**"
                "⚠️ **波は動くが、波はこの距離に届かない**"
                "——**波は寄せて返るだけで、舟を運ばない**（`motion.subject` の逐語:「**主題は止まる。**」）。",
    "continuity": "**Must preserve** — あの一点の位置、大きさ、形を持たないこと、"
                  "そして**距離が変わらないこと**。"
                  "**May change** — 波の位相、うねりの高さ、反射の線の位置、"
                  "そして一点の見え方のごくわずかな揺れ。",
    "notes": ["⛔ **この距離を、この1本は縮めない。****縮めれば、"
              "「まだ着かない」が「着く」になる**——**この作品の主題が、そこで終わる。**",
              "⛔ **この1本の画には、人が一人も入らない。****記録の `unit`（前・後）と `beats` のどこにも、人物が現れない**"
              "——**ゆえにこの1本は、人を一人も置かない。**"
              "**参照集合は「固定するもの」を挙げており、「画に居る者」を挙げているのではない。**（§15 の `identity` を見る）",
              "⚠️ **この1本の `BEARER` を人にすることはできない**——**画に人が居ないからである。**"
              "**人の代わりに立てるのは、この距離だけである。**"]},
   {"name": "近い水面",
    "ref": "**この1本の動く側である。** ⚠️ **参照は `ledger.locations.海` の `base` と `states.夜`。**",
    "appearance": "**長く低いうねりであり、白波を立てない。****一つの方向へ、"
                  "絶えず同じ速さで動く。****星の反射が短い線になって、その面を走る。**",
    "behavior": "**流れる。****この7.101秒のあいだ、一度も止まらない。**"
                "⚠️ **そして波は返る**——**返ることが、この1本の最後の出来事である**"
                "（`beats` の3番目の逐語:「**波が返る**」）。"
                "**返っても、何も近づかない。**",
    "continuity": "**Must preserve** — うねりの低さ、白波が無いこと、反射が短い線であること。"
                  "**May change** — 反射の線の位置、うねりの高さ、位相。",
    "notes": ["⚠️ **この1本で動いてよいのは、この層だけである。****波が止まれば、"
              "この1本は止まった画になる。**"]},
 ],

 "environment": {
   "location": "`海` — **夜である。****四方を水に囲まれ、どの方向にも陸が見えない**"
               "（`海.geography` の逐語）。⚠️ **カメラは低く、水面のすぐ近くにある**"
               "——**この7.101秒のあいだ、一度も動かない。**"
               "⛔ **舟も、人も、この1本の画には入らない。**",
   "elements": "**長く低いうねり**、**一つの方向へ絶えず動く水面**、**星の反射の道**、"
               "**平らで途切れない水平線**、**その一点だけ薄い暗さ**、そして**その上の空**。"
               "⛔ **陸も、島も、帆も、鳥も、他の船も無い。**"
               "⛔ **そしてこの1本の画には、人が一人も入らない。**",
   "behavior": "⛔ **この1本の出来事は、何も起きないことである。****波が動き、"
               "一点は動かず、カメラも動かない**——**ゆえに、何も近づいていない**"
               "（`motion.quality` の逐語）。"
               "⚠️ **「何も起きない」は、この1本では欠落ではない。****7.101秒かけて"
               "確かめられた事実である。**",
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
                  "⚠️ **`男.identity` と `男.negatives` が集合に在っても、それは外見を固定するためであり**"
                  "——**ゆえにこの集合は、この1本に人が居ることも、彼女が居ることも主張しない。**",
 "ref_extra": [
   "- ⚠️ **形式カード `meaning-responsive` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; "
   "what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じである。**",
   "- ⚠️ **カードの逐語:「**The delay is composed.** The gap between the meaning and the answer is the "
   "shot's time.」****この1本では、意味と答えの間隔が、この1本の全体である**"
   "——**「まだ着かない」は最初のコマから最後のコマまで同じであり、"
   "答え（同じ距離がまだ在ること）は最終コマでしか確定しない。**"
   "⛔ **ゆえにこの1本は、遅れそのものを7.101秒である。**",
   "- ⚠️ **カードの逐語:「**The limit is stated.** What the answer may not touch keeps it legible. "
   "An answer that reaches everything reads as a filter or a grade, not as a response.」"
   "**この1本の限界は「距離が縮まないこと」である**——**そして限界が破られれば、"
   "この1本の答えは「着く」という別の答えになる。**",
   "- ⚠️ **形式カード `meaning-responsive` の5つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `BEARER`＝what carries the meaning — **あの一点までの距離である。**"
   "**「まだ着かない」を運び、何もしない。** ⛔ **人を立てない**（この1本の画には、人が一人も入らない）。",
   "  - `ANSWER`＝how the picture answers it — **波が返り、同じ距離がそのまま残る。**"
   "**この1本の答えは「縮まない」という事実であり、変化ではない。**"
   "⚠️ **カードの逐語:「The answer is in the world, not in the camera.」**",
   "  - `DELAY`＝how far the answer lags the meaning — **この1本の全体である。**"
   "**意味は最初のコマから在り、答えが確定するのは最後のコマである。**"
   "**中間の5.099秒は、遅れの構成である。**",
   "  - `LIMIT`＝what the answer may not reach — ⛔ **距離は縮まらない。**"
   "**明るさは大きくならない。****形は現れない。****音は届かない。**"
   "**そして陸にはならない。**",
   "  - `DURATION`＝clip length — **`7.101s`。**",
   "⚠️ **カードの `Negative` の逐語:「no camera move answering the meaning」**"
   "——⛔ **この1本のカメラは、答えに動かされない。****動かないことが、"
   "この1本では `mode: still` と一致する。**",
 ],

 "narrative": {
   "core": "**近づかないことを、7秒で写せるか** — **止まるのは主題である。**"
           "**近づくという主題が、止まっている。**",
   "beginning": "**一点と、その周りの海。****距離がある。**"
                "⚠️ **この2.002秒で、この距離はもう、この1本の距離である。**",
   "turn": "**波が動く。****一点は動かない。****カメラも動かない。**"
           "⚠️ **この1本には、転換が無い。****変わらないことが、"
           "この1本の内容である。**",
   "peak": "**同じ距離のままである。****7.101秒が過ぎる。**",
   "pull": "⚠️ **波が返る——近づかないことが、切れ目のコマである。**"
           "**波は戻り、距離は戻らない、のではなく、"
           "距離ははじめから動いていない。****それで `l32` の歌が終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven only in what it withholds.** ⚠️ **この1本は `mode: still` である**"
            "——**密度も配分も、動かない。****3つのビートの配分は `s30` とほぼ同じであるのに、"
            "この1本には「寄る」ビートが無い。**"
            "⚠️ **ゆえに最後の2.599秒は、`s30` の最後の2.041秒と違って、"
            "何も足さない**——**「波が返る」だけである。** "
            "⛔ **この差が、この1本と `s30` の差である。****ビートを均等にしないのは、"
            "切れ目が曲の事象だからである**（`L37`）。"
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**波はこの1本でも動き続ける。**",

 "actions": [
   ("ACT_SHOW", "一点と、その周りの海がある。**距離がある。**",
    "**同じ画が2.002秒のあいだ保たれる**——**距離が、"
    "この1本の主題として立てられる。**"),
   ("ACT_HOLD", "一点は、まだ同じ距離にある。",
    "**波が動き、一点は動かない**——**カメラも動かない。****ゆえに、"
    "何も近づいていない。**"),
   ("ACT_RETURN", "波は、寄せたところまできている。",
    "**波が返る**——**そして同じ距離が、そのまま残っている。**"
    "**近づかないことが、この1本の切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **low over the water, the horizon running high across the frame, the one "
               "point small on that line** — **and this framing is the whole clip.** "
               "⚠️ **この1本の画角は、距離を測るために在る**——"
               "**一点が小さいことが、距離の唯一の証拠である。**",
   "events": "**None. The camera does not move at all.** ⚠️ **この1本には動機が無い**"
             "——**近づく主題が、止まっている。****動く理由が、"
             "この1本には一つも無い**（`motion.quality` の逐語:「**カメラも動かない。**」"
             "「**ゆえに、何も近づいていない。**」）。"
             "⚠️ **ゆえにこの1本の §10 には、時刻を持つ出来事が一つも無い。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends none of "
               "them** — ⚠️ **この1本にはカメラ移動の動機が一つも無い**——"
               "**様式の法は「動機の無い移動を禁じる」であり、ゆえにこの1本のカメラは動かない**"
               "（`motion.law` の逐語:「常に何かを追っているか、何かへ寄っているか、"
               "何かから離れている」——**この1本は、そのどれでもない**）。 "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and **no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題は、止まっている。****波だけが動き続ける。**"
              "**あの明るさは動かない。****カメラも動かない**"
              "（`motion.subject` の逐語）。"
              "⚠️ **ゆえに、何も近づいていない。**",
   "object": "⚠️ **この1本には、動く物が無い。****動くのは水だけである。**"
             "⛔ **そして、あの一点は物ではない**——**動かないことが、"
             "その正体の全部である。**",
   "environment": "**星の光が、静的な光源として画面の外に在る。****その反射が、"
                  "動く面の上で短い線に砕ける。**"
                  "⚠️ **この1本では、光も動かない**——"
                  "**`s30` の一点の明るさは、この1本ではもう在り、"
                  "そのまま在り続ける。**",
   "weight": "**うねりは低く、質量は水のものである。****速さは一度も変わらない。**"
             "⚠️ **この1本の主題の重さは、"
             "動かないことの重さである**——**距離は、"
             "動かないことによって、いちばん重くなる。**",
   "inertia": "**反射の線は、遅れて消える。****波は、寄せたぶんだけ返る。**"
              "⚠️ **この1本の時間は、この往復だけでできている**"
              "——**往復しても、距離は一歩も動かない。**",
   "acceleration": "**加速しない。****波の速さは一定であり、"
                   "距離も一定である。**"
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この7.101秒に、"
               "止まったフレームは一つも無い**——**`mode: still` は、"
               "画面が止まることを意味しない。**"
               "**止まるのは、主題である。**",
   "impact": "**無い。** ⛔ **この1本に衝撃は一つも無い**——"
             "**波が返ることは、打撃ではない。**"
             "**音を立てない出来事である。**",
 },

 "emotion": {
   "arc": "**着かないことを、感情にしない。** ⚠️ **この1本は、"
          "待つ画でも、諦めの画でもない**"
          "——**待てば、着かないことが焦りになる。****諦めれば、"
          "着かないことが敗北になる。**"
          "**この1本が置くのは、ただの事実である****——"
          "「まだ着かない」は、状態であって、感情ではない。**",
   "events": "⚠️ **この1本の出来事は、何も起きないことである。**"
             "⚠️ **人が居ないので、この1本には感情の担い手が一人も居ない**"
             "——**残るのは、波と、一点と、一つの光と、"
             "変わらない距離だけである。**",
 },

 "lighting": {
   "base": "**夜である。****光源は星と、その水面の反射だけである。****波は黒く、"
           "反射の道だけが白い**（`ledger.locations.海.states.夜` の逐語）。"
           "⚠️ **この1本の光源は一つであり、それは星である。**"
           "⚠️ **月も、火も、灯も無い。**",
   "events": "**None.** ⛔ **この1本では、光の出来事が一つも起きない**"
             "——**`s30` で始まった明るさは、この1本ではもう在り、"
             "変わらない。****大きさも、位置も、色も同じである。**"
             "⚠️ **ゆえにこの1本の §12 には、時刻を持つ出来事が無い**"
             "——**`s30` の答えを、この1本は繰り返さない。****持ち越すだけである。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水の音だけである。****長く低いうねりが動く音、砕けない面が擦れる音。**"
          "⚠️ **打ち上げる音は無い**——**この海は白波を立てない。**"
          "⚠️ **木の音も、縄の音も、櫂の音も無い**——**舟はこの1本の画にも音にも入らない。** "
          "⚠️ **そして遠くの音も無い**——**鐘も、鳥も、岸の音も届かない。**"
          "**あの一点は、音を持たない。**",
   "music": K.NO_MUSIC + " ⚠️ **そしてこの1本には、歌が在る**——`l32`「まだ着かない」であり、"
            "**行の長さが、そのままこの1本の長さである**（267.686–274.787。**7.101秒**"
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
              "direction, including behind.」）。⚠️ **カメラは低く、水面のすぐ上にある。**"
              "⛔ **この1本のカメラは、一度も動かない**——**`s30` の最後のビートで始まった接近は、"
              "この1本では起きない。**"
              "⚠️ **この1本で、この海が `s30` の海と同一であることが保たれる**"
              "（`海.geography` の逐語:「**the same waterline and the same horizon appear in both**」）。",
   "temporal": "**夜である。****この作品の三つの時刻のうちの一つである**"
               "（`日没`・`夜`・`夜明け`）。⚠️ **この作品は曲に従って時刻を選んでおり、"
               "時計には従っていない**（`bible.time_source: song`）。"
               "**画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は星の光だけである。**"
             "⚠️ **そしてこの1本の一点は、`s30` の一点と同一でなければならない**"
             "——**位置も、大きさも、暗さの薄さの度合いも、"
             "`s30` の最後のコマのままである。**"
             "⛔ **変えれば、この2本は続いていない画になる。**",
   "motion": "Full animation, not limited. **波が動き続ける。** "
             "⚠️ **カメラは一度も動かない。****あの一点は、"
             "この7.101秒のあいだ、一度も動かないし、大きくならない。**",
   "sound": "水だけ。**音楽なし。言葉なし。** ⚠️ **主題歌はこの1本のあいだ鳴っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "⚠️ **この1本の画には、人が一人も入らない**——**ゆえに女神の禁制は、"
     "「彼女を人のかたちで置かない」だけでなく、「**人の形を一つも置かない**」として効く。**")) + [
   "**No person in this frame at all** — ⚠️ **この1本には、人が一人も入らない。**",
   "**No second person in frame at any distance, in any focus.**",
   "**No camera move of any kind** — ⛔ **この1本のカメラは動かない**"
   "（`motion.quality` の逐語:「カメラも動かない」）。**寄ることも、引くことも、"
   "横へ流れることも無い。**",
   "**No camera move standing in for the answer** (逐語, カードの `Negative`: "
   "「no camera move answering the meaning」)。",
   "**No cut, and no rack focus carrying the meaning** （同、逐語）。",
   "**Nothing comes closer and nothing grows** — ⛔ **距離が縮まないこと**"
   "——**縮めば「着く」になり、この行が終わる。****明るさも大きくしない。**",
   "**No visible cause for what does not change** — ⚠️ **距離が縮まないことに、"
   "原因を画面に置かない**（カードの `do` の逐語:「Keep the answer's cause absent from the frame」）。"
   "**漕ぐ力も、帆も、流れも、この1本には無い。**",
   "**No island, no land, no shore in this frame** — ⛔ **この1本は、"
   "あの一点を陸と呼ばない**（`world.rules` の五番）。",
   "**No boat, no ship, no hull, no other vessel in frame** "
   "（`ledger.locations.海.base` の逐語:「No land, no sail, no bird, no other vessel.」）。",
   "**No beam, no ray, no shaft of light, and no lens flare standing in for the answer.**",
   "**No white water, no breaking crest, no spray** — **この海は白波を立てない。**",
   "**No caption naming the meaning, and no voice-over naming it** "
   "（カードの `Negative` の逐語）。",
 ],

 "must": [
   "⛔ **近づかないこと** — **距離が、この7.101秒のあいだ、一歩も変わらないこと。**",
   "⛔ **カメラが動かないこと** — **`mode: still` は、画面が止まることではなく、"
   "主題が止まっていることである。****波は動き続ける。**",
   "⛔ **人が一人も入らないこと。**",
   "⚠️ **あの一点が、`s30` の最後のコマと同一であること** — 位置も、大きさも、"
   "暗さの薄さの度合いも。",
   "⚠️ **答えが世界の側に在ること** — **「縮まない」は、"
   "変化ではなく事実として写ること。**",
   "⚠️ **波が返ること** — **この1本の最後の出来事はこれだけである。**",
   "⛔ **人が一人も入らないこと** — **この枠は、海だけで在る。****参照集合が人の外見を挙げていても、それは画に人を置く指示ではない。**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **変化は最後のコマで終わる** — **近づかないことが、切れ目のコマである。**",
   "⛔ **切らないこと。****1本は1つの画である。**",
 ],

 "prefer": "The night held black and the reflected path the only white; the swell kept long, low and "
           "crestless; **the one point on the horizon kept at exactly the same distance, size and "
           "brightness from the first frame to the last**; **the camera held absolutely still**; "
           "**the wave's return kept as the only event in the clip.**",
 "allow": "The reflected path breaking into short strokes and re-forming; the swell's height varying "
          "slightly as it runs; **the darkness at that one point thinning by a barely measurable "
          "degree and settling**; **a gentle flare on the one reflected path.**",

 "priorities": [
   "⛔ **距離が縮まないこと** — **この1本の主題であり、破れれば別のショットになる。**",
   "⛔ **カメラが動かないこと** — **この1本には動機が無い。**",
   "⛔ **人が一人も入らないこと。**",
   "⚠️ **一点が `s30` と同一であること** — **この2本は続いている。**",
   "⚠️ **答えがカメラの移動に由来しないこと** — **カードの `avoid` の一番目である。**",
   "⛔ **人が一人も入らないこと** — **この枠は、海だけで在る。****参照集合が人の外見を挙げていても、それは画に人を置く指示ではない。**",
   "**No second person, at any distance, in any focus.**",
   "**光は星の光だけであること** — 月も、火も、灯も無い。",
   "⚠️ **この1本が 7.101秒であること**（曲の `l32` の実測である）。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `meaning-responsive` を名乗るが、その禁制（`no visible cause`・"
   "`no camera move answering the meaning`・`no cut`・`no rack focus carrying the meaning` ほか）は "
   "§16 に在って、ここには無い。** **ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。** "
   "⚠️ **この形式の文法は §10 の `target` と §12 の光の出来事に書いた**——"
   "**この節に持ち込めば、34本の同一性が崩れる。**"),

 "master": (
   "A 7.101-second cinematic take (16:9) of open sea at night far from any land, one clip, one "
   "continuous take, one change: **the distance does not close.**\n\n"
   "⚠️ **No person is in this frame and no part of the raft is in it either — the water is alone, at every distance and in every focus.**\n\n"
   "0-2.002s: **the one point and the water around it, with distance in them** — the point small on "
   "the horizon, the water moving.\n"
   "2.002-4.502s: **the waves move; the point does not; the camera does not** — **and therefore "
   "nothing comes any closer.**\n"
   "4.502-7.101s: **the same distance, still** — **the wave returns, and the distance is what it was** "
   "— and the take ends there.\n\n"
   "**The camera does not move at all in this take, and it never cuts.** **The answer is in the world, "
   "not in the camera: the waves keep moving and the distance keeps its exact value, and nothing in "
   "the frame causes that.** **The one point on the horizon stays at the same size, the same "
   "brightness and the same place as in the shot before this one, and it does not grow.** **One light "
   "only — the stars and their reflection.** **No island, no land, no shore, no sail, no bird, no "
   "other vessel, and nothing warm in the frame.** **No person is in this frame at any distance or in "
   "any focus, and no woman is in it at all.** **This is a bronze-age sea before classical Greece: no "
   "made thing of any later age.** **This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the distance does not close.)"),

 "visual_scene": (
   "Open sea at night, far from any land, photographed as a film frame, low over the water: **long low "
   "swells with no white water, moving steadily in one direction, the surface fine-grained and broken, "
   "and one broken path of reflected starlight lying across the near water as short strokes.** The "
   "horizon runs level and unbroken across the frame, darker than the sky and darker than the water, "
   "and **at one point on that line the darkness is slightly thinner than it is anywhere else on the "
   "line — the same point as in the previous shot of this work, at the same size and the same "
   "distance, with no shape and no edge and no colour of its own.** The sky above is black with stars, "
   "and the stars do not brighten. **Nothing else is in the frame: no shore, no island, no sail, no "
   "bird, no vessel, no person, no moon.**"),

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
   "Full animation, not limited. **The waves move and nothing else does.** The swell runs in one "
   "direction at a steady rate with no crest and no white water, comes in and returns in its own "
   "cycle, and the reflected path of the stars breaks into short strokes on its face and re-forms. "
   "**The one point on the horizon does not move, does not grow and does not change its brightness: "
   "its distance from the frame is the same in the last second as in the first.** **The camera does "
   "not move in this take: not laterally, not forward, not up, and it does not turn.** No motion blur "
   "smears, no stutter, no floaty weightless motion, no static frames — **the water moves in every "
   "frame of the take.**"),

 "camera_prompt": (
   "Third person, **low just above the water, the horizon running high across the frame, the one "
   "point small on that line.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot "
   "spends none of them** — the style's law forbids a move without a motive, and **this shot has no "
   "motive to follow, to approach or to leave: its subject is a thing that does not come closer.** "
   "**There is no camera event in this shot, and it never cuts to a second setup.** ⚠️ **Do not "
   "drift, do not creep, and do not let the frame breathe.** No handheld, no whip, no shake, no snap "
   "zoom, no rack focus, no unnatural rotation, and **no unmotivated move.**"),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **long low water moving, and the fine sound of an unbroken "
   "surface sliding against itself, coming in and returning.** ⚠️ **No crest breaks and nothing slaps "
   "or slaps back.** ⚠️ **No wood, no cordage and no oar are heard: the raft is not in this frame and "
   "not in this shot's sound.** ⚠️ **No bell, no bird and no shore reaches this shot** — the point on "
   "the horizon has no sound of its own. ⚠️ **Nothing here is silent — the water is the subject of "
   "this shot's sound.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (meaning-responsive) ／ "
                        "REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**"
                        "（裁定②。そしてこの経路は既定で何も添付しない）。"
                        "⚠️ **参照集合が `男.identity` を挙げていても、この1本は同一性の塊を §18 に貼らない**——**記録の `unit` と `beats` のどこにも、人物が現れないからである**（§3 と §15 を見る）。"
                        "⚠️ **この1本の主題は `海` と `海.geography` である**"
                        "（`舟` は画の外にある）。",
 "camera_events_count": "no camera event — the camera does not move in this shot (§10)",
 "audio_events": "no dialogue ／ water only ／ no music",
 "unresolved": [
   "⚠️ **記録は `mode: still` を「この作品の5本のうちの1本」と書く**（`motion.law` の逐語）。"
   "⚠️ **この仕様は still の本数を数え直していない**——**数えれば、"
   "別の数になる可能性がある**（`s06`・`s08`・`s11`・`s24`・`s31`・`s32`）。"
   "⛔ **ゆえにこの仕様は、本数を書かない。****数を決めるのは著者である。**",
   "⚠️ **この1本と `s32` は、同じ行（`l32`・`l33`「まだ着かない」）を2度覆う。**"
   "⚠️ **`L36` がそれを註にする**（`s22` の註を見る）。"
   "**この1本は `meaning-responsive`、`s32` は `time-fold` であり、"
   "2つの形式が2つの違うことを言う**——**が、画そのものが2本とも「変わらない海」であるため、"
   "観客には同じ画が2度続いて見える危険がある。**"
   "⛔ **差をどこに置くかは、絵を見て決めることである。**",
   "⚠️ **この1本の `mode: still` と、`L37` の「末尾のビートは `dense`」が、"
   "字面上は噛み合わない。** ⚠️ **記録のビートは 0-2.002（transition）／2.002-4.502（sparse）／"
   "4.502-7.101（dense）であり、`dense` は維持されている**"
   "——**この1本の `dense` は、"
   "「濃い」ではなく「切れ目のコマ」を意味する**（`beats` の逐語:「**近づかないことが、"
   "切れ目のコマである**」）。**この読みで書いた。**",
 ],
 "risks": [
   "⛔ **カメラが動く。** この1本の最大の危険である——**動機の無い移動は様式の法が禁じているが、"
   "7.101秒の静止は、この経路では「動き出したい」画である。**"
   "**少しでも寄れば、「近づかない」という主題が壊れる。**",
   "⛔ **距離が縮まる。** ⚠️ **一点が大きくなる、または位置がずれるだけで、"
   "この1本は「着く」ショットになる。**",
   "⛔ **何かが入る。** ⚠️ **島、帆、鳥、舟、光の柱のどれか一つで、"
   "この1本の「まだ」が消える。**",
   "⛔ **人が入る。** ⚠️ **この1本の画には、人が一人も入ってはならない**——**この経路は、夜の海の画に人物を足したがる。**",
   "⚠️ **画が退屈になる。** ⚠️ **この1本は `mode: still` であり、"
   "密度が動かない**——**退屈は欠陥ではないが、"
   "「何も無い画」と「何も起きない画」は違う。**"
   "**波の往復が、この1本の唯一の生命である。**",
   "⚠️ **`s30` の一点と、この1本の一点が食い違う。**"
   "**位置、大きさ、暗さの薄さの度合いが変われば、この2本は続いていない画になる。**",
 ],
}
