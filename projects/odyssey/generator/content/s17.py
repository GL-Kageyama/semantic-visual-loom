# -*- coding: utf-8 -*-
"""odyssey-s17 — transformation — 舟の置き場 / 夜明け / 6.543s. The man is here."""
import common as K


C = {
 "n": "s17",
 "title": "布が、帆になる",
 "duration": "6.543",
 "format": "transformation",
 "has_man": True,
 "segment": "verse-2-2",

 "header": """⛔ **この1本で、この作品で唯一の「与えられた物」が作られる。** 出所は曲の `l15`「帆を縫って風を待つ」——**この一行が、布の行き先を帆に決めている。**
⚠️ **`world.rules` の二番が、この1本に出る**——「**女神は差し出したあとも、道具を与える。**斧・錐・帆の布・星の道——**断られた側が、出発の術を教える。**」
⛔ **ゆえにこの帆は、この作品で唯一の「与えられた物」である。** ⚠️ **誰から来たのかを、この作品は一度も言わない。** **言わないことが、この規則の実装である。**
⚠️ **`props.帆.negative` の1行が効く**——「**no sail worn as a garment by any person**」。⚠️ **詩では、この布は彼の身にも掛かる。この作品では掛からない**——**曲の `l15` が、布の行き先を帆に決めている。**
⚠️ **形式は `transformation`。** **`s16` と同じである**——**`s16` は木が筏になり、この1本は布が帆になる。****この作品は2本を対にして置いた。**
⚠️ **切れ間は `l15` の歌い終わりである**（155.266–161.809。**行の長さが、そのままこの1本の長さである**）。
⚠️ **この仕様のショット記録は `shots/odyssey-s17.yaml` である。**""",

 "intent": "One continuous take of one change — **布が帆になる。** 最初のコマでは布は浜に平らに広がり、四隅を石で押さえられていて、**まだ布でしかない。** 最後のコマでは縫い目が浮き、風を孕んで張りきっている——**張りきるのが、切れ目のコマである。** ⚠️ **切らない。溶かさない。過程を名指さない。** 形式カードの逐語:「**the change is the shot, and the viewer watches two states be the same subject at different moments.**」 ⚠️ **変わるのは布であって、縫っている男ではない**——**二つ目の主題を同時に変えない。** ⚠️ **変化は切れ目のコマで終わる**——張りきった瞬間に、この1本は終わる。",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、この作品の労働の場所で、二番目の夜明けである**——`s16` と同じ朝、同じ浜である。"
   "⛔ **そしてこの1本で作られるものは、この作品で唯一「与えられた」ものである**——"
   "**斧も、錐も、星の道も、同じ側から来た。****この作品は、その出所を一度も言わない。**"
   "⚠️ **言わないことが実装である**（`world.rules` の二番）——**名指せば、この作品は説明になる。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本には彼が居る。****それでも返事は無い**——**縫う手は動き、口は開かない。**"
               "**黙っていることは、この作品では何もしないことではない。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "**それでもこの1本の主題は、彼女の側から来た布である**——"
                "**この作品は、与えた者を写さずに、与えられた物だけを写す。**",
     "name": "⚠️ **この1本に名は無い。** 布にも、帆にも、彼にも、**どこにも書かれないし、呼ばれない。**",
     "bow": "⚠️ **この1本に弓は無い。** 彼が持つのは**青銅の針と、手で撚った糸**だけである。"
            "⚠️ **斧はこの1本では使われない**——**薪の上に立てて置かれたままである。**",
     "places": "この1本が置くのは一つ——`舟の置き場`、**この作品の6つの場所のうち、労働の場所はここだけである**"
               "（`ledger.locations.舟の置き場.base` は「A working place on the shingle just above the waterline」で始まる）。"
               "⚠️ **`s16` と同じ場所であり、この1本は場所を立て直していない。**",
     "japanese": "⚠️ **この1本には歌がある**——`l15`「帆を縫って風を待つ」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **この作品で唯一の「与えられた物」が、この1本で作られる。****誰から来たのかは、一度も言わない。**"
     "**言わないことが、この規則の実装である**——**出所を名指せば、この作品は説明になる。**",
     "⚠️ **この布は、この1本では彼の身に掛からない**（`props.帆.negative` の逐語:「**no sail worn as a "
     "garment by any person**」）。**詩では掛かる。この作品では掛からない**——**布の行き先は帆である。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "A working place on an island's shingle at dawn, photographed as a film. Unseasoned pine logs and "
     "hewn planks on trestles of driftwood, drifts of pale wood shavings and cut cordage spreading "
     "outward and never swept, a bronze double-axe left standing in a log. Undyed wool, hand-twisted "
     "cordage, and a square of heavy undyed cloth. ⚠️ **No building, no shelter, no fire, no tool other "
     "than what the hand holds.** ⚠️ **No marble, no columns, no architecture of any later age.**",
   "Color Language":
     "A narrow, graded palette — the sea still dark, the sky going from blue to grey-white, and the "
     "shavings' white the first thing to brighten. ⚠️ **There are no cast shadows yet** — the light is "
     "not oblique, so everything stands by outline and not by shadow. ⚠️ **Nothing is lit apart from the "
     "place** — the same flat dawn light falls on the cloth, on his hands and on the shingle, and **the "
     "shot has no second light.**",
   "Texture":
     "Pale unseasoned wood shavings and cut cordage over damp shingle; pine logs still barked and "
     "uneven; a cloth of coarse open weave, stiff and slightly yellowed, its seams raised lines and its "
     "lower edge raw; the cloth's own folds held from lying; and skin and coarse wool where the man is. "
     "⚠️ **No machine stitching and no cut edge that is not raw.** Film grain present and even.",
   "Rendering":
     "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, a gentle flare "
     "where the sky is in frame. **Not a photograph's stillness: a film frame, with a real lens's "
     "fall-off at the edges.** No illustration, no CGI look, no cartoon color.",
   "Visual Density": "Low to moderate. **The cloth is the single focal point and nothing in the frame "
                     "competes with it** — the man is bent over it, and the work around them is ground.",
   "Time": "`夜明け` — the thirty minutes when the sky goes from blue to grey-white and the light is "
           "still flat. **The same dawn as `s16`, and the second and last dawn of this work's working "
           "place; the work does not fix a date.**",
   "Atmosphere": "The half hour when work can be seen before the light has decided anything.",
 }),

 "subjects": [
   K.man_subject(
     behavior="**彼は布のそばに膝をつき、縫う。**速度は一定で、急がない。針は右手にあり、**糸は左手で引かれる。**"
              "⚠️ **彼はこの1本の主題ではない**——**主題は布である。**彼は**変える者であって、変わる者ではない。**"
              "⚠️ **彼は口を開かず、レンズを見ない。**",
     may="膝の位置、針の速さ、上体の角度、袖の落ち方、そして影がまだ無いこと。",
     extra_notes=[
       "⚠️ **この1本の主題ではない。** **変わるのは布である**——形式カードの逐語:「**One change, one "
       "subject.** The subject of the change stays the subject all the way through … **A second subject "
       "transforming at the same time turns the shot into a montage.**」",
       "⚠️ **`s05` が立てた顔の基準から外れない。** ⚠️ **この1本は顔の大写しを持たない**——**それでも"
       "英文の塊は §18 にまるごと入る。**",
     ]),
   {"name": "帆",
    "ref": "**この1本の主題である。** ⚠️ **参照は `props.帆` の `appearance` と `negative` である**——"
           "**この作品に参照画像は無い**（裁定②）ので、**この英文が布の同一性を運ぶ。**",
    "appearance": "**重い無染色の布である。**手で縫われ、縫い目が長く不揃いで、**浮いた線として見える。**"
                  "布は硬く、少し黄ばみ、織りは粗く開いている。**下の縁は生のままで、縁かがりが無い。**"
                  "⚠️ **模様も、染めも、刺繍も、印も無い**（`props.帆.negative`）。"
                  "⚠️ **平らに広げられているあいだは、畳まれていた折り目を保っている。**",
    "behavior": "**針が出入りするたびに、形が決まっていく。**縫い目が浮き、布が張り、**最後に風が入って膨らむ。**"
                "⚠️ **布は自分では動かない**——**動かすのは針と、そして風である。**",
    "continuity": "**Must preserve** — 布の材質、粗い織り、硬さと黄ばみ、**下の縁が生であること**、"
                  "縫い目が浮いた線であること、**そして模様も染めも印も無いこと**。"
                  "**May change** — 折り目の形、布の張り、縫い目の位置、風の入る場所、そして縁の浮き方。",
    "notes": ["⛔ **形式カード `transformation` の5つの変数は、この1本ではこの布に当てはめられる**"
              "（§6 の「形式の文法」と §17 を見る）。",
              "⚠️ **この布は、この1本の変わる主題である。** **彼は変える者である**——"
              "**二つ目が同時に変われば、この1本はモンタージュになる。**",
              "⚠️ **`s16` の木と対である。** **`s16` は木が筏になり、この1本は布が帆になる。**"]},
 ],

 "environment": {
   "location": "`舟の置き場` — **この作品の6つの場所のうち、労働の場所はここだけである**"
               "（`ledger.locations.舟の置き場.base`）。"
               "⚠️ **岸の右手の端であり、洞口からは見えない。**"
               "**水際は仕事場から二歩である。** ⚠️ **この場所は夜明けしか持たない**——"
               "`ledger.locations.舟の置き場.states` の鍵は `夜明け` だけであり、**この場所を使うのは `s16` とこの1本の2本だけである。**",
   "elements": "建造中の筏、樹皮のついたままの未乾燥の松の丸太、流木の架け台に載った粗削りの板、"
               "**外へ広がったまま一度も掃かれない白い削り屑と、切れ端の縄**、薪に立てて置かれた青銅の両刃の斧、"
               "そして**四隅を石で押さえられて平らに広げられた、重い無染色の布**。"
               "⚠️ **建物も、小屋も、火も無い。**",
   "behavior": "**空だけが明るくなっていく。**海はまだ暗く、**光がまだ斜めでないので、物は影ではなく輪郭で立っている。**"
               "⚠️ **削り屑の白だけが、いちばん先に明るくなる。** 風は削り屑の縁と、ほどけた縄を動かす"
               "——**そして布に入る。** 水は同じ間隔で寄せて返す。⚠️ **場所は彼に反応しない**——"
               "**彼が手を止めても、波は止まらない。**",
 },

 "objects": [
   "**帆** — **この1本の主題である。**四隅を石で押さえられて平らに広がり、縫われ、そして風を孕む。"
   "⚠️ **模様も染めも印も無い。** ⚠️ **誰の身にも掛からない。**",
   "**針** — 青銅である。**手で撚った糸を通し、布を出入りする。** ⚠️ **この1本で唯一、彼が持つ道具である。**",
   "**糸** — 手で撚られている。**太さが不揃いである。** ⚠️ **機械の縫い目は無い**（`props.帆.negative`）。",
   "**石**, four stones weighting the corners of the cloth — **風が布に入ると、最後には用を失う。**",
   "**削り屑と切れ端の縄**, spreading outward from the raft and never swept — **この1本では動かない。**"
   "**動くのは、その縁を払う風だけである。**",
   "**斧**, the bronze double-axe left standing in a log — ⚠️ **この1本では使われない。**"
   "**薪から抜かれず、彼の手にも渡らない。**",
   "⚠️ **この作品の小道具は4つだけであり**（`ledger.props`）、**そのうちこの1本に来るのは帆ひとつである**"
   "——舟・斧・太陽の牛は、**まだ作られていないか、まだ記憶にすら無い。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — **この1本には添付しない。彼女はこの1本に、四つの姿のどれとしても現れない**"
                  "——**それでもこの1本の主題は、彼女の側から来た布である。** "
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`舟の置き場`・`舟の置き場.geography`・"
                  "`舟の置き場.states.夜明け`・`帆`・`帆.appearance`・`帆.negative` の8鍵である。"
                  "⚠️ **集合が挙げているのは `帆` であって、`舟` ではない**——**この1本で形を変えるのは布であり、"
                  "筏はこの1本では作られない。**",
 "ref_extra": [
   "- ⚠️ **`transformation` は `video-spec` に一つの文法を足したものである**"
   "（形式カードの逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card "
   "requires; what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と"
   "同じであり、違うのは §8 に書いた5つの変数と、§16 に運んだ形式カード自身の禁制である。**",
 ],

 "narrative": {
   "core": "**布が帆になる** — この作品で唯一の「与えられた物」が、この1本で作られる。",
   "beginning": "**布は浜に平らに広がり、四隅を石で押さえられている。****まだ布でしかない。**"
                "縫い目は一本も無い。",
   "turn": "**針が出入りする。****縫い目が、浮いた線として立っていく**——布が、平らでない形を持ちはじめる。",
   "peak": "**風が布に入る。****布が膨らみ、張る。**",
   "pull": "⚠️ **張りきるのが、切れ目のコマである。****縫い目が立ち、織りが開き、布が帆になっている。**"
           "**その瞬間に、`l15` の歌が終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.545秒.** 最初の1.498秒は**まだ布でしかないこと**のために払われ、"
            "次の2.5秒は**縫うことに**払われ、**最後の2.545秒がこの1本の出来事である。** "
            "⚠️ **カードの逐語:「Spend the shot's seconds on the passage, not on the two states.」**"
            "——**この1本は、両端ではなく、変わっているあいだに秒を使う。** "
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**風が入ったあとも、波と削り屑は動いている。**\n"
            "- ⚠️ **`transformation` の5つの変数**（⚠️ 定義はカードの逐語である）:\n"
            "  - `FROM`＝the substance, figure or place as the shot opens — **布である。**浜に平らに広げられ、"
            "四隅を石で押さえられ、**まだ帆ではない。**\n"
            "  - `TO`＝what it becomes — **帆である。**縫い目が浮いた線として立ち、風を孕んで張りきり、"
            "**ステイを引く。**\n"
            "  - `TRIGGER`＝the event the change starts from — ⚠️ **針が布に入ることである。**"
            "**その時点が、この1本の変化の始まりである**——**始まりを偶然に任せない**"
            "（カードの逐語:「Give the change a trigger, or state that it has none — do not leave the "
            "moment it starts to chance」）。**風は最後に来るが、変化を始めるのは針である。**\n"
            "  - `KEEP`＝what must stay recognisable across the change — ⛔ **布そのものである。**粗い織り、"
            "硬さ、黄ばみ、**下の縁が生であること**、そして**模様も染めも印も無いこと。**"
            "**同じ布が別の時点にあるのであって、別の布に置き換わるのではない。**\n"
            "  - `DURATION`＝clip length — **`6.543s`。**",

 "actions": [
   ("ACT_SPREAD", "布は畳まれたまま、石は置かれていない。",
    "**布は浜に平らに広がり、四隅を石で押さえられている**——**そして、まだ布でしかない。**"),
   ("ACT_SEW", "布は平らであり、縫い目が一本も無い。",
    "**針が出入りし、縫い目が浮いた線として立っている**——**布が、平らでない形を持ちはじめる。**"),
   ("ACT_FILL", "布は折り目を保ったまま、風を受けていない。",
    "**風が布に入る**——布が膨らみ、ステイが張る。"),
   ("ACT_TAUT", "布は膨らんでいるが、まだ張りきっていない。",
    "**布が張りきる**——縫い目が立ち、織りが開く。**その張りきるコマが、この1本の切れ目である。**"),
 ],

 "camera": {
   "language": "Third person, **low, near the cloth's own plane** — the lens a hand's width above the "
               "shingle, so that the cloth is a surface the frame slides along and the raft, the work and "
               "the brightening sky stand above it. ⚠️ **この高さは `s16` の仕事場の高さである。**",
   "events": "One event only. `0-3.998s` — **a slow lateral travel along the cloth's surface, keeping "
             "the line of the seam, at the needle's own pace and never leading it**; then `3.998-6.543s` "
             "— **the same travel continues and rises only as much as the cloth rises**, and it is still "
             "moving when the cloth pulls taut. ⚠️ **動機は縫い目である。** ⚠️ **布の向こうの縁を越えない。**"
             "⚠️ **この1本は一度も布から離れない**——**離れれば、縫い目を追う動機が消える。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** "
               "— a low weighted lateral travel with the low frequency of a rig that has mass, and it does "
               "not wobble. ⚠️ **crane も Steadicam も、この1本では使わない**——**この画は布の面に沿って"
               "低く滑るだけであり、持ち上がる必要が無い。** ⚠️ **風が入ったあと、カメラは布の面から"
               "離れない。** No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural "
               "rotation, and **no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、布である。**平らな布が、縫い目によって形を持ち、"
              "**風によって膨らみ、張る。** ⚠️ **彼の手も動くが、彼は主題ではない**——"
              "**変わるのは布であって、縫う者ではない。**",
   "object": "**針が布を出入りし、糸が引かれる。****縫い目が浮いた線として立つ。**"
             "**石が最後には用を失う**——風が布を持ち上げるからである。"
             "⚠️ **削り屑と切れ端の縄は動かない**——**動くのは、その縁を払う風だけである。**"
             "⚠️ **斧は動かない。**",
   "environment": "**風が布に入る** — 一斉に、しかし突風としては入らない。"
                  "**空の色が青から灰白へ移り、削り屑の白が最初に明るくなる。**"
                  "水は同じ間隔で寄せて返す。⚠️ **環境は彼に反応しない。**",
   "weight": "**布は帆になった瞬間に重くなる。**風を受けてステイを引き、**張りきった布は、"
             "もう浜に置かれていたものではない。** ⚠️ **この1本の重さは、布が風を抱えることで現れる。**",
   "inertia": "**布は遅れて落ち着く。**風が緩んでも、すぐには戻らない。"
              "**縫い目は、針が止まったあとも少しのあいだ動く。** ⚠️ **何も瞬間には止まらない。**",
   "acceleration": "**加速しない。** 針の速さは一定であり、**風も突風として入らない。** "
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この6.543秒に、止まったフレームは"
               "一つも無い**——**布は最後のコマまで動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**張りきることは、打撃ではない。**"
             "**音を立てない変化である。**",
 },

 "emotion": {
   "arc": "**この作品で唯一の「与えられた物」が、作られる。** そして**その出所が、この1本では"
          "一度も言われないこと**が、この1本の感情である。"
          "⚠️ **感謝の画ではない**——**彼は黙って縫っている。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****布が張りきることである。** "
             "**誰から来た布なのかは、画面のどこにも無い**——**無いことが、この作品の規則の実装である。**",
 },

 "lighting": {
   "base": "The sun is not up yet: the light is the sky's own, **flat and without direction** — no fill, "
           "no artificial source, and **no cast shadow anywhere in the frame.** ⚠️ **この1本の光源は"
           "一つであり、それは空である。** ⚠️ **布を別に照らさない**——**布は浜と同じ光の中にある。**",
   "events": "**One, and it runs the whole shot.** 空が青から灰白へ移り、**物が輪郭で立っていく。**"
             "**削り屑の白が最初に明るくなり、次に布の縫い目が浮き、最後に青銅の針が縁を持つ。**"
             "⚠️ **光源は動かない。** ⚠️ **様式カードの逐語:「The grade holds for the whole shot — a colour "
             "temperature that swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**針が粗い織りを通る音、糸が引かれる音、そして布に風が入る音。**"
          "⚠️ **彼は何も言わないが、無音ではない**——**縫う音が、この1本の音の側の主題である。** "
          "⚠️ **斧の音は鳴らない**——**斧はこの1本では使われない。** "
          "⚠️ **機械の縫い目の音は無い**——**糸は手で撚られ、針は手で動く。**",
   "music": K.NO_MUSIC + " ⚠️ **そしてこの1本には、歌が在る**——`l15`「帆を縫って風を待つ」であり、"
            "**行の長さが、そのままこの1本の長さである**（155.266–161.809）。"
            "**生成された音床が来れば、同じ瞬間に二つの音楽が重なる。**",
   "environment": "夜明けの島の仕事場。**水、風、木、布、そして一人の人間の手仕事。** "
                  "⚠️ **呼ぶ声は無い**——**彼は呼ばれていないし、呼んでもいない。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="**体格・肌・髪・髭・顔・傷・着ている一枚と、着ていないすべて・裸足であること。** "
                "⚠️ **この1本は顔の大写しを持たないが、塊は §18 にまるごと入る**——**ゆえにこの1本も、"
                "`s05` が立てた顔から外れてはならない。**",
     may="膝の位置、針の速さ、上体の角度、袖の落ち方、影がまだ無いこと。"),
   "spatial": "**仕事場は岸の右手の端にあり、洞口からは見えない。****水際は仕事場から二歩である。**"
              "筏は手前の地面に立ち、水はその向こうにある。"
              "⚠️ **カメラは布の側から離れない**——**布の向こうの縁を越えれば、水の画になる。**"
              "⚠️ **`s16` と同じ配置である**——**この1本は場所を立て直していない。**",
   "temporal": "一日の始まり、**`s16` と同じ夜明けである。** ⚠️ **この1本は、空が明るくなりきる前の"
               "30分の中にある**——**その中で、彼は働く。** 画の中に日付を与えるものは何も無い。",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は空の光だけである。**"
             "⚠️ **この1本は `transformation` を名乗るが、この形式は §15 から何も免除しない**"
             "——**`coexisting-realities` と違い、免除を名乗る欄が無い形式である。**"
             "**免除するのは、`KEEP` が保つものだけであり、それは布の同一性である。**",
   "motion": "Full animation, not limited. **針が動き、布が動き、風が布を動かす。** "
             "⚠️ **カメラは1回だけ動き、そして布の面から離れない。**",
   "sound": "布、糸、針、水、風。**音楽なし。言葉なし。** ⚠️ **主題歌はこの1本のあいだ鳴っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**この1本には彼が居る**——**ゆえに女神の禁制は、他人の形で来る。**"
     "**与えた者を、人のかたちで置かない。****布の出所を、誰かの姿で説明しない。**")) + [
   "**No second person in frame at all** — no companion, no crowd, no figure at any distance, "
   "**no one on the shingle behind him and no one on the water.**",
   "**No cut, no dissolve, no wipe between the cloth and the sail.** ⚠️ **この1本の変化は、"
   "切れ目のコマまで一続きである。**",
   "**No stated process** — no caption, no voice-over, no date stamp, **no text of any kind naming what "
   "is happening.** ⚠️ **カードの逐語:「No process beat.」**",
   "**No held intermediate stage that explains the change** — **途中の段を、観客のために止めない。**",
   "**No second simultaneous transformation** — ⚠️ **変わるのは布だけである。****縫っている男は変わらない。**",
   "**No sail worn as a garment by any person** (逐語, `props.帆.negative`). ⚠️ **この布は彼の身に掛からない。**",
   "**No pattern, no dye, no embroidery, no emblem, no mark on the sail** (逐語, `props.帆.negative`).",
   "**No modern canvas, no synthetic fabric, no machine stitching** (逐語, `props.帆.negative`). "
   "⚠️ **糸は手で撚られている。**",
   "**No sail already raised on the raft before the sail exists** (逐語, "
   "`ledger.props.舟.negative`). ⚠️ **この1本の布は、まだ浜の上にある。**",
   "⚠️ **No tool in his hand except the needle** — **斧は薪から抜かれず、彼の手に渡らない。**",
   "⚠️ **No boat, no ship, no hull, no keel, no planking** (逐語, `ledger.props.舟.negative`)"
   "**、そして何も張られていないこと。** ⚠️ **この1本の筏は、まだ建造中である。**",
 ],

 "must": [
   "**布が帆になる** — そして**風を孕んで張りきるのが、切れ目のコマである。**",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.**",
   "⛔ **切らない。溶かさない。過程を名指さない。****変化は一続きであり、途中の段を止めない。**",
   "⚠️ **変わるのは布だけである** — **縫っている男は、この1本では変わらない。**",
   "⚠️ **誰から来た布なのかを、一度も言わない** — **画面にも、音にも、字にも無い。**",
   "⚠️ **布は誰の身にも掛からない** — **この1本の布は帆であり、帆でしかない。**",
   "**No second person appears, at any distance, in any focus.**",
   "⚠️ **彼はレンズを見ず、口を開かない。**",
   "⚠️ **変化は最後のコマで終わる** — 張りきった瞬間に、この1本は終わる。",
   "⚠️ **この1本は、この作品で唯一の「与えられた物」が作られる1本である** — **それでも、"
   "与えた者は写らない。**",
 ],

 "prefer": "The cloth held as the single focal point; the shavings' white brightening first; the seams "
           "standing as raised lines; his hands in the mid-tones; **the flat, shadowless dawn held for "
           "the whole take.**",
 "allow": "The wind entering the cloth all at once and not as a gust; the stones losing their hold on the "
          "corners; the thread's thickness varying; a gentle flare where the brightening sky is in frame; "
          "**a slow low travel along the cloth that never crosses its far edge.**",

 "priorities": [
   "⛔ **変化は一続きであること。** **切れば、この1本は二つの画になり、`transformation` が成立しない。**",
   "⛔ **布が帆になること** — そして**張りきるのが切れ目のコマであること。**",
   "⚠️ **変わるのは布だけであること** — **縫っている男を、二つ目の変わる主題にしない。**",
   "⚠️ **誰から来た布なのかを言わないこと** — **`world.rules` の二番の実装がこれである。**",
   "⚠️ **布を誰の身にも掛けないこと** — **`props.帆.negative` の逐語がこれである。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "⚠️ **`transformation` の5つを満たすこと** — `FROM` は布、`TO` は帆、`TRIGGER` は針、"
   "`KEEP` は布そのもの、`DURATION` は 6.543秒。",
   "**No second person, at any distance, in any focus.**",
   "**光は空の光だけであること** — 専用の光源も、火も無い。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `transformation` を名乗るが、その禁制（`no cut`・`no dissolve`・`no stated process`・"
   "`no second simultaneous transformation` ほか）は §16 に在って、ここには無い。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 6.543-second cinematic take (16:9) of a working place on a bronze-age island's shingle at dawn, one "
   "clip, one continuous take, one change: **the cloth becomes a sail.** **The change is the whole of the "
   "shot; the man who sews it is not the thing that changes.**\n\n"
   "**{IDENTITY}** He is on his knees beside the cloth with a bronze needle in his right hand and the "
   "hand-twisted thread in his left. **He does not speak and he does not look at the lens.**\n\n"
   "0-1.498s: **the cloth lies flat on the shingle, weighted at its four corners with stones, and it is "
   "still only cloth** — there is not one seam in it.\n"
   "1.498-3.998s: **the needle goes in and out and the thread is pulled through**, and **the seams rise "
   "as lines** — the cloth begins to hold a shape that is not flat.\n"
   "3.998-6.543s: **the wind enters it.** The cloth bellies and the stays pull, **and on the last frame "
   "it is taut and the seams stand up — and the take ends on that frame.**\n\n"
   "**The camera slides low along the cloth's own plane, keeps the line of the seam, and never crosses "
   "the cloth's far edge.** **Nothing in this frame says where the cloth came from, and nothing says it "
   "in the sound either.** **The cloth is never worn as a garment by anyone: it is a sail, and only a "
   "sail.** **No second person is in this frame at any distance or in any focus, and no woman is in it "
   "at all.** **This is a bronze-age shore before classical Greece: hand-twisted cordage, a bronze "
   "needle, undyed cloth, and no machine stitching — no made thing of any later age.** **This is a "
   "Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the cloth becomes a sail.)"),

 "visual_scene": (
   "A working place on a bronze-age island's shingle at dawn, photographed as a film frame: unseasoned "
   "pine logs still barked, hewn planks on trestles of driftwood, drifts of pale wood shavings and cut "
   "cordage spreading outward and never swept, a bronze double-axe left standing in a log at the edge of "
   "the frame. **In the near ground, a square of heavy undyed cloth laid out flat on the damp shingle, "
   "its four corners weighted with stones, its lower edge raw and unhemmed; long uneven hand-sewn seams "
   "rising from it as raised lines; the cloth stiff and slightly yellowed, its weave coarse and open, "
   "holding the folds it was carried in.** The waterline lies two paces beyond the work; the sky above "
   "is going from blue to grey-white and the sea is still dark. No building, no shelter, no fire."),

 "visual_meta": (
   "Anamorphic lens with subtle oval bokeh and a gentle flare where the light is in frame; a moderate "
   "depth of field; a graded palette of dark water and a sky going from blue to grey-white, in which "
   "the shavings' white is the brightest thing in the frame. Pale unseasoned wood shavings and cut "
   "cordage over damp shingle; barked pine logs on driftwood trestles; a coarse open-weave cloth, stiff "
   "and slightly yellowed, its seams raised lines and its lower edge raw; skin and coarse wool where "
   "the man is; even film grain over everything. No painterly stroke, no airbrush, no plastic surface, "
   "no CGI look, no illustration. ⚠️ **The light is flat and casts no shadow at all** — everything in "
   "this frame stands by outline, and the shavings' white is the first thing to brighten."),

 "motion_prompt": (
   "Full animation, not limited. **The cloth is the mover.** The needle goes in and out of the coarse "
   "weave at a steady pace and the thread is drawn through after it, **and the seams rise as lines**; "
   "**the cloth takes the shape the stitches decide and stops being flat.** **Then the wind enters it "
   "all at once, the cloth bellies, the stays pull, and on the last frame it is taut** — and it is still "
   "holding the wind when the take ends. **His hands move with the needle and his upper body is still; "
   "he does not change.** **The camera slides low along the cloth's plane at the seam's own pace and "
   "does not cross its far edge.** The shavings and the cut cordage do not move except where the wind "
   "lifts their edges; the sea arrives and goes back at the same interval throughout. No motion blur "
   "smears, no stutter, no floaty weightless motion, no static frames — **the cloth moves in every frame "
   "of the take.**"),

 "camera_prompt": (
   "Third person, **low, near the cloth's own plane** — the lens a hand's width above the shingle, so "
   "that the cloth is a surface the frame slides along and the work and the brightening sky stand above "
   "it. One event only: **a slow lateral travel along the cloth's surface that keeps the line of the "
   "seam at the needle's own pace and never leads it, continuing and rising only as much as the cloth "
   "rises, and still moving when the cloth pulls taut.** ⚠️ **The move is motivated by the seam; it "
   "never leaves the cloth.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot "
   "spends the dolly** — a low weighted lateral travel with the low frequency of a rig that has mass. "
   "⚠️ **No crane is used, and no Steadicam** — this frame only slides, and has no reason to lift. "
   "⚠️ **Do not cross the cloth's far edge and do not lift away from it.** No handheld, no whip, no "
   "shake, no snap zoom, no rack focus, no unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **a bronze needle passing through coarse cloth, the thread "
   "drawn through after it, the cloth taking the wind, and the water arriving and going back two paces "
   "off.** ⚠️ **He says nothing, but this shot is not silent — the sound of the sewing is the subject of "
   "this shot's sound.** ⚠️ **No axe sounds in this shot; the axe is never lifted from the log.** "
   "⚠️ **No machine stitching is heard: the thread is hand-twisted and the needle is driven by hand.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (transformation) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ。**"
                        "⚠️ **参照集合の8鍵のうち、この1本の主題は `帆` である**（`舟` ではない）。",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ needle ＋ thread ＋ cloth in the wind ＋ water ／ no music",
 "unresolved": [
   "⚠️ **`transformation` の5つの変数のうち、`TRIGGER` の読みが著者に委ねられている。**"
   "**この仕様は「針が布に入ること」を変化の始まりとした**——**風を `TRIGGER` に読むこともできる**"
   "（風が入らなければ帆にならない）。⚠️ **どちらが正しいかは、絵を見て決めることである。**"
   "**この仕様は、始まりを偶然に任せないというカードの指示の側を採った。**",
   "⚠️ **斧を画面に置いたままにした。** `props.斧.negative` の逐語に「no other tool」が在るので、"
   "**針と斧が同じ画に居ることが誤りになりうる。** ⚠️ **この仕様は、斧を「薪に立てて置かれたまま、"
   "この1本では使われない」ものとして書いた**——**抜くかどうかは、著者が見て決める。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **カットが入り、二本の画になる。** この1本の最大の危険である——**`transformation` の主張は"
   "「切らない」であり、切れば二つの状態を並べただけになる。** 禁制は §16 と `Master Prompt` の散文の両方に在る。",
   "⛔ **過程が名指される。** ⚠️ **この経路には字幕を作るための公式の記法がある**（`【】`）——"
   "**「縫う」「帆になる」と画面に書かれれば、この1本は説明になる。**",
   "**二人目が入る。** ⚠️ 人が居る画に人を足すのは生成器にとって自然であり、**この作品では「一人」が主題である。**",
   "⚠️ **布が彼の身に掛かる。** ⚠️ **詩では掛かるので、生成器がそう読みやすい**——"
   "**`props.帆.negative` の1行が、この1本ではいちばん効くべき禁制である。**",
   "**縫い目が機械になる。** ⚠️ **この経路は布を縫う画を、既製の縫い目で埋めやすい**"
   "——**糸は手で撚られ、縫い目は不揃いでなければならない。**",
   "**風が入らず、布が平らなまま終わる。** 張りきることが切れ目のコマの内容であり、"
   "**張らなければ、この1本は帆を作っていない。**",
   "**顔が動く（drift）。** ⚠️ **この1本は顔の大写しを持たないが、顔は画の上端に入りうる**"
   "——**参照画像が1枚も無いので、守る道具は英文だけである。**",
 ],
}

if __name__ == "__main__":
    print("s17 content OK — keys:", len(C))
