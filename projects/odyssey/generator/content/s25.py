# -*- coding: utf-8 -*-
"""odyssey-s25 — transformation — 沈んだ場所 / 夜 / 8.377s. Lines l25+l26 welded into one shot.

Disclosure change point ④ (`男.名: absent`) — the work's last disclosure.
A transformation shot in which nothing transforms: only the name changed.
"""
import common as K


C = {
 "n": "s25",
 "title": "誰でもない——変身の形式で、何も変えない",
 "duration": "8.377",
 "format": "transformation",
 "has_man": True,
 "place": "沈んだ場所",
 "time": "夜",
 "segment": "bridge-3",

 "band": [
   "『永遠より遠い』 bridge「沈んだ場所」 / 開示 / motion —— 誰でもない——変身の形式で、何も変えない",
   "水面に浮く一人から光が少しずつ抜け、輪郭が水と区別できなくなる。",
   "8.377秒、カメラは離れず、寄りもしない——顔が同じ顔であるのが、切れ目である。",
   "見た目は変わらず、誰も名を呼ばない——変わったのは、名だけである。",
 ],
 "header": """⛔ **開示の変化点④である**（`ledger.disclosure`）——`男.名: absent`。
出所は曲の `l25`「**誰でもないと名乗った**」。
⚠️ **値が `present` でなく `absent` である**——**観客が知るのは「名乗られた名が、名でない」ことである。**
⛔ **これがこの作品の最後の開示である**——**ここから先、観客は何も新しく知らない。**
⚠️ **2行を束ねた理由は長さである。** 実測: `l25` は 3.590秒、`l26` は 4.787秒。
⚠️ **`l25` は下限4秒に満たない**（`s07` の註を見る）。
⛔ **形式は `transformation`。****この作品で3本目である。**
⛔ **この1本が、この形式の使い方の頂点である**——**変身の形式を使い、変身を一度も見せない。**
**変わったのは名だけである。** ⚠️ **「誰でもない」とは、そういうことである。**
⚠️ **`world.rules` の三番が、ここで初めて意味を持つ**——「**固有名は、画面にも歌にも一度も現れない。**」
⛔ **この作品は、名が無いことを名乗る1本を持っている。**
⚠️ **`mode: motion`。****記録の `motion.quality` の逐語:「光が彼の顔から少しずつ抜けていく。それだけである。」**
⚠️ **この仕様のショット記録は `shots/odyssey-s25.yaml` である。**""",

 "intent": "One continuous take of one change — **変わったのは名だけである。**"
           "最初のコマでは**水面に浮かぶ顔に、星の反射の光が当たっている。**"
           "最後のコマでは**影が濃くなり、輪郭が水と区別できなくなり、そして顔は同じ顔である**"
           "——**変わらないことが、切れ目のコマである。**"
           "⛔ **変身の形式を使いながら、この1本は変身を一度も見せない。****カットも、ディゾルブも、"
           "過程の段も無い。** ⚠️ **観客が知るのは「名乗られた名が、名でない」ことだけであり、"
           "そしてそれは画面に一度も現れない。**"
           "⛔ **彼は名乗らない**——**彼の口は動かない。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本の場所も、同じ記憶である。** 曲の `l25` と `l26` が名指す水は、"
   "**`s23` と `s24` と同じ水である**——⛔ **同じ夜、同じ場所、そして同じ一人の記憶である。**"
   "⛔ **そしてこの1本で、開示が終わる。****ここから先、観客は何も新しく知らない。**"
   "⚠️ **この1本の主題は「名」である**——**にもかかわらず、名は画面にも歌にも一度も現れない**"
   "（`world.rules` の三番の逐語:「**固有名は、画面にも歌にも一度も現れない。**」）。"
   "⚠️ **画面が写せるのは光だけである**——**記録の逐語:「光が彼の顔から少しずつ抜けていく。それだけである。」**"
   "**変わったのは名である。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本は、返事を待たない1本である。****返事は `s24` で既に来ている。**"
               "**ここで来るのは知であって、応答ではない。**",
     "goddess": "⚠️ **この1本は彼女の場所ではない。****彼女は四つの姿のどれとしても現れない**——"
                "**この1本の光は星だけであり、それは彼女の仕業として書かれない。**"
                "⛔ **「誰でもない」という一行を、彼女の仕業にしない。**",
     "name": "⛔ **ここがこの1本の中心である。** ⚠️ **`world.rules` の三番の逐語:「固有名は、"
             "画面にも歌にも一度も現れない。」** ⛔ **この1本は、名が無いことを名乗る1本である**"
             "——**ゆえにこの1本は、名を一度も出さない。****画面にも、字にも、音にも。**"
             "⚠️ **彼の口は動かない。****名乗るのは歌であって、彼ではない。**",
     "bow": "⚠️ **この1本に持ち手が無い。****弓も、斧も、道具も一つも出ない**——"
            "**彼は浮かんだままで、手は水の中にある。**",
     "places": "この1本が置くのは一つ——`沈んだ場所`。⚠️ **`s23`・`s24` と同じ水であり、"
               "**違うのは「舟がそこに居ないこと」だけである。**",
     "japanese": "⚠️ **この1本には歌がある**——`l25` と `l26` の2行が、この8.377秒の上を歌っている"
                 "（`l25` は 3.590秒、`l26` は 4.787秒）。**そして歌は日本語である。**",
   },
   extra=[
     "⛔ **この1本が、この作品の最後の開示の変化点である**——`男.名: absent`。"
     "⚠️ **ここから先、観客は何も新しく知らない。**"
     "**ゆえにこの1本のあとの `final-chorus` は、知を増やさない**——**反復と運動の区間である。**",
     "⛔ **形式 `transformation` の3本目である。**⚠️ **記録の `motion.law` の逐語:「この作品は、"
     "この形式を『物が変わる』ために2度使い、『人が変わる』ために1度使う。そして3度目は、何も変わらない。」**",
     "⚠️ **この場所の光は星だけである**（`ledger.locations.沈んだ場所.states.夜` の註:「光源は星だけである。"
     "岸も舟も無いので、明るいものは何も無い——水面だけが、星を受けて黒く光る」）。"
     "⚠️ **ゆえにこの1本に、夜明けの光も、月も、火も無い。****抜けていく光は、この一つの光源のうちの、"
     "彼の顔に当たっていた分である。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, photographed from **directly above** as a film frame: **the surface is the whole of "
     "the frame** — no shore, no land, no landmark, no raft, no wreckage, nothing floating in it. "
     "**One man lies at the surface, face up, alone.** ⚠️ **No made thing is in this frame except the one "
     "garment he is wearing** — no vessel, no rope, no tool, no fire. **No marble, no columns, no "
     "architecture of any later age.**",
   "Color Language":
     "A narrow, graded palette — black water with one broken path of reflected starlight across it, and "
     "**the man's skin, his salt-stiffened hair and the one undyed wool tunic the only warm thing in the "
     "frame.** ⚠️ **The light does not come from anywhere in the frame** — it is the stars and their "
     "reflection. ⚠️ **The shot has no second light and no warm source**, and **the picture's colour is the "
     "same in the first frame and the last: what falls is the amount of light on his face, not the grade.**",
   "Texture":
     "Still black water, fine-grained and broken, carrying one path of reflected starlight; the wool of the "
     "tunic coarse and dark with water, worn through at the shoulder seam; his hair matted with salt and "
     "spread on the surface; skin roughened and marked, and **the shadows deepening on it as the light "
     "leaves.** ⚠️ **No shore, no shingle, no sand and no land are in this frame.** Film grain present and "
     "even.",
   "Rendering":
     "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, a gentle flare where "
     "the light is in frame. **Not a photograph's stillness: a film frame, with a real lens's fall-off at "
     "the edges.** No illustration, no CGI look, no cartoon color.",
   "Visual Density": "Low, **and it falls** — the frame empties toward the water as his outline goes. "
                     "⚠️ **ビートの `dense` は、物が多いことではない。****この1本でいちばん多くが起きている"
                     "ということであり、それは「変わらないことが確定する」ことである。**",
   "Time": "`夜` — the night of the bridge, on the same water as `海`. ⚠️ **This place has no before and no "
           "after**（`沈んだ場所.states.夜` の逐語:「この場所には、前後が無い。」）. ⚠️ **それでもこの1本は"
           "「過ぎていく」1本である**——**光が抜けるのに、8.377秒かかる。****この作品で、時間が最も長く"
           "感じられる1本である。**",
   "Atmosphere": "The moment the name goes out of him — **and the picture shows it by taking the light away, "
                 "because the picture may not show anything else.**",
 }),

 "subjects": [
   {"name": "男",
    "ref": "**この1本の主題であり、この1本に居る唯一の人である。** ⚠️ **参照集合が `男.identity` を持つ**"
           "——**裁定②により参照画像は1枚も無いので、その英文だけが彼の顔を守る。**"
           "⚠️ **そしてこの1本では、その顔が `KEEP` である**（§8）——**変わらないことが、この1本の内容である。**",
    "appearance": "**§18 に逐語で貼られた塊のとおりである。****最初のコマでは、星の反射の光が彼の顔に当たっている。**"
                  "**濡れた髪が水に広がり、髭が水面に出て、着ている一枚の粗い白い羊毛が水を吸って重い。**"
                  "⚠️ **裸足で、脚と腕は裸である**——**海中なので、それらは水面の下にある。**",
    "behavior": "**彼は浮いているだけである。** ⚠️ **彼は話さない。****名乗らない。****口が動かない。**"
                "⛔ **「誰でもないと名乗った」のは歌であって、彼ではない**——"
                "**この1本は、名乗りを一度も写さない。**"
                "⚠️ **水面が彼をわずかに運ぶので、彼は画の中で少しずつ動く**——**動かしているのは水面である。**",
    "continuity": "**Must preserve** — §18 に逐語で貼られた同一性の塊の、一句一句。体格・肌・髪・髭・顔・傷・"
                  "**着ている一枚と、着ていないすべて**。⛔ **この1本の `KEEP` は顔である**"
                  "——**影が濃くなっても、顔の形は変わらない。**"
                  "⚠️ **カードの `avoid` の逐語:「Morphing that abandons the subject's identity instead of "
                  "carrying it」**——**この1本は、同一性を運ぶ側である。**"
                  "**May change** — 影の深さ、輪郭の見え方、光の量、髪の水への広がり方、"
                  "そして画の中の彼の位置（**水面が運ぶ分だけ**）。",
    "notes": ["⚠️ **`transformation` の5つの変数は、この1本ではこう当てはめられる**"
              "（§8 の `Temporal Density` を見る）——`FROM`＝**光の当たっている顔である**／ "
              "`TO`＝**光の抜けた顔である**（**影が濃くなり、輪郭が水と区別できなくなる**）／ "
              "`TRIGGER`＝**歌の行の頭である**（2.002秒。**画面の中に引き金が無いことを、ここで名乗る**）／ "
              "`KEEP`＝**顔である**／ `DURATION`＝`8.377s`。",
              "⛔ **この1本は、名を失うことを写す。****しかし名は写せない。****ゆえに写すのは光である。**"
              "**これが、この1本の設計の全部である。**"]},
   {"name": "nobody",
    "ref": "**この1本に、彼のほかに人は一人も居ない。** ⚠️ **参照集合にも、もう一人を置く鍵が無い。**"
           "⛔ **ここが最後の開示の変化点である**——**しかし、居ない者を画の中に置かない。**"
           "**「誰でもない」は、誰かを足す理由にならない。**",
    "appearance": "**無い。** ⚠️ **水の下にも、水面にも、遠景にも、誰も居ない。**",
    "behavior": "**無い。** ⚠️ **動くのは水面と、彼の髪と、衣の端だけである。**",
    "continuity": "⚠️ **二体目を足さないこと。****この1本は `s24` と同じ水である**"
                  "——**`s24` の危険が、この1本にもそのまま掛かる。**",
    "notes": ["⚠️ **`Negative Prompt` はこの経路では床にならない**（§18 の前書き）。**ゆえにこれは肯定形で負う。**",
              "⚠️ **「誰でもない」を、生成器は「誰か別人」と読むかもしれない。**"
              "**この1本の人称は、一人称のままである。**"]},
 ],

 "environment": {
   "location": "`沈んだ場所` — **記憶の中の海であり、`s23`・`s24` と同じ水である。**"
               "⛔ **違うのは一つだけである**（逐語:「Its only difference is that the raft is not in it.」）"
               "——**舟が居ない。** ⚠️ **岸も、目印も無い**（逐語:「There is no landmark and no shore; the "
               "camera cannot orient by anything.」）。",
   "elements": "夜の水面と、**星を受けた一本の反射の道**、そして**水の上に浮いている一人**。"
               "⚠️ **破片を一つも置かない**（`沈んだ場所.base` の逐語:「No wreckage, no bodies, no oars, no "
               "mast, no floating wood, no blood, no cloth.」）。",
   "behavior": "**水面は同じ向きへ、同じ速さで動きつづける。**"
               "⚠️ **この1本では、その動きが彼をわずかに運ぶ**——**8.377秒のあいだに、彼は画の中で少し動く。**"
               "⚠️ **そして反射の道が、彼の顔から少しずつ滑り落ちていく**（2.002秒から。§13）。"
               "⚠️ **環境は彼に反応しない**——**水面は彼を避けず、彼も水面を変えない。**",
 },

 "objects": [
   "**水面と、星の反射の一本の道** — **この1本で変わるのは、この道の当たる場所である。**"
   "⚠️ **光源は動かない。****動くのは水面であり、それに乗って道が滑る。**",
   "**彼が着ている一枚の粗い羊毛の衣** — 衣装であって小道具ではない"
   "（逐語:「one coarse undyed wool tunic, worn through at the shoulder seam, belted with a plain leather cord」）。"
   "⚠️ **水を吸って重く、最後のコマではほとんど見えない**——**影が濃くなるからである。**",
   "⚠️ **この作品の小道具は4つだけであり**（`ledger.props`）、**この1本に来るものは無い**"
   "——舟・帆・斧・太陽の牛は、**この記憶のこの瞬間に無い。**",
 ],

 "ref_character": "**この1本は `男` の1本である。****そして、この1本に人は彼一人である。**"
                  "⚠️ **彼以外の人を、どの距離にも、どのピントにも置かない**"
                  "（`forbidden_set` の逐語:「no other human being in frame — no companion, no crowd, no "
                  "second person」）。⛔ **女神は現れない**——四つの姿のどれとしても。"
                  "⛔ **そしてこの1本は、名を一度も出さない。**"
                  "⚠️ **参照は `男.identity` と `男.negatives`、そして場所の3鍵である。****添付は0点である**（裁定②）。",

 "ref_extra": [
   "⚠️ **形式カード `transformation` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; what "
   "follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §6 のこの一行と、§9 と §11 に足された一つの規則である。**",
   "⛔ **カードの逐語:「The change is the time, and it is not compressed.」**"
   "⚠️ **ゆえにこの1本は、両端の状態にではなく、抜けていく時間そのものに秒を使う**（§8・§9）。",
   "⚠️ **カードは「引き金を与えるか、無いと名乗れ」と言う**（逐語:「Give the change a trigger, or state "
   "that it has none — do not leave the moment it starts to chance」）。"
   "⛔ **この1本の引き金は歌の行の頭である**（2.002秒）——**画面の中に引き金が無いことを、ここで名乗る**（§8）。",
 ],

 "narrative": {
   "core": "**名だけが変わる** — 変身の形式を使い、変身を一度も見せない。",
   "beginning": "水面に浮かぶ男の顔。**星の反射の光が当たっている。**",
   "turn": "**光が抜けはじめる。****影が濃くなる。****顔の形は変わらない。**",
   "peak": "**輪郭が水と区別できなくなる。**",
   "pull": "⚠️ **しかし顔は同じ顔である**——**変わらないことが、切れ目のコマである。**"
           "**この作品は、名が無いことを、この1本で名乗り終える。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, in three parts, and the change takes all of them.** 最初の2.002秒は**光の当たっている顔**に払われ、"
            "次の2.999秒は**抜けはじめる光**に払われ、**最後の3.376秒がこの1本の頂点である**"
            "——**輪郭が水と区別できなくなり、そして顔は同じ顔である。**"
            "⚠️ **この1本は2行を束ねている**（`l25` は 3.590秒、`l26` は 4.787秒——記録の実測）"
            "——⛔ **ゆえに1本の中で、意味の区切りが 3.590秒のあたりにある。**"
            "**この仕様はその区切りにビートを置かない**——**置けば、二つ目の変化になる**"
            "（カードの逐語:「One change, one subject.」）。"
            "⚠️ **`mode: motion`** ——**この1本は動く1本である。****動くのは光と水面とカメラである。**"
            "**ゆえに末尾のビートは `dense` である。** ⚠️ **`held` を1つも使わない。** "
            "⚠️ **`transformation` の5つの変数（形式カードの逐語）**: `FROM`＝**光の当たっている顔である**／ "
            "`TO`＝**光の抜けた顔である**（**影が濃くなり、輪郭が水と区別できなくなる**）／ "
            "`TRIGGER`＝**歌の行の頭である**（2.002秒。**画面の中に引き金が無いことを、ここで名乗る**）／ "
            "`KEEP`＝**顔である**（**同じ顔のままであること。****変わらないことが、切れ目のコマである**）／ "
            "`DURATION`＝`8.377s`。",

 "actions": [
   ("ACT_LIT", "切り出しは水面である。",
    "**水面に浮かぶ男の顔。****星の反射の光が当たっている。**"),
   ("ACT_DRAIN", "光は彼の顔の上にある。",
    "**光が抜けはじめる**——**反射の道が、彼の顔から少しずつ滑り落ちていく。****影が濃くなる。**"),
   ("ACT_FADE", "影はまだ顔の形を残している。",
    "**輪郭が水と区別できなくなる**——**彼は水の一部のように見えはじめる。**"),
   ("ACT_SAME", "それでも彼は浮かんでいる。",
    "⚠️ **しかし顔は同じ顔である**——**変わらないことが、この1本の切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **directly above him** — the lens looking straight down at the water, so that "
               "he lies in the frame's centre and the empty sea fills everything around him. "
               "⚠️ **記録の逐語:「カメラは彼から離れず、しかし寄りもしない。」**"
               "⚠️ **`s24` と同じ真上である**——**この記憶の水は、この高さで写される。**",
   "events": "One event only. `0-8.377s` — **a slow continuous travel that keeps him in the frame at the "
             "same distance and at one fixed height, at a rate that does not change, still travelling on "
             "the last frame of the take.** ⚠️ **動機は「真上に留まること」である**——"
             "**水面が彼をわずかに運ぶので、カメラは同じ速さで流れて、同じ距離を保つ。**"
             "**ゆえに離れず、寄りもしない。** ⚠️ **そしてこの移動は、変わったことを語らない**"
             "——**変わるのは光である。****カメラは、この1本でいちばん何も言わないものである。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the Steadicam** "
               "— a slow travel that holds its distance, with the low frequency of a rig that has mass, and "
               "it does not wobble. **The height does not change.** ⚠️ **降りない。****寄らない。****離れない。**"
               "**回らない。****傾けない**——**答えも、変化も、カメラの側では作られない。**"
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, and "
               "**no unmotivated move.**",
 },

 "motion": {
   "subject": "**男の顔、そして彼の周りの水面。** ⚠️ **記録の `motion.subject` の逐語である。**",
   "object": "**動く物は彼の髪と衣の端、そして水面の反射の道である。****そしてこの1本では、"
             "その道が彼の顔から滑り落ちていく**（2.002秒から）——**これが `FROM` から `TO` への移動である。**"
             "⚠️ **彼は何も持っていないので、動かされる物は無い。**",
   "environment": "**水面は同じ向きへ、同じ速さで動きつづける。****星の反射の道が細かく割れては戻る。**"
                  "⚠️ **風はこの1本の画にも音にも無い**——**道を動かすのは水面であって、風ではない。**"
                  "⚠️ **環境は彼に反応しない**——**彼が水と区別できなくなっても、水面は同じ速さで動く。**",
   "weight": "**水は重い。****水を吸った羊毛は重い。****そして影が濃くなるほど、彼の顔は水の側へ寄る**"
             "——**この1本の重さは、沈んでいないのに沈んで見えることの重さである。**",
   "inertia": "**水面は行き過ぎてから戻る。****彼の体は、その動きに少しだけ遅れて従う。**"
              "⚠️ **しかし抜けた光は戻らない**——**カードの逐語:「The return is a decision.」**"
              "**そしてこの1本は、戻らないという決定である。** ⚠️ **最初のコマの光は、最後のコマに無い。**",
   "acceleration": "**加速しない。****抜ける速さも一定である**——**後半に急に暗くならない。**"
                   "⚠️ **この1本に見せ場の加速は一つも無い。****変化は、均した速さで最後まで続く。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この8.377秒に、止まったフレームは一つも無い**"
               "——**光が抜けているあいだも、水面と髪とカメラが動いている。**",
   "impact": "**無い。** ⚠️ **この1本には衝撃も、変わる音も無い**——**変わるのは光の量だけである。**",
 },

 "emotion": {
   "arc": "**一人が浮かんでいて、その顔から光が抜けていく。** そして**それが「名を失った」に見えること**が、"
          "この1本の感情である。⛔ **説明は一つも無い**——**名も、字幕も、声も、字も無い。**"
          "⚠️ **この作品は、いちばん言いたいことを、いちばん何も言わない1本に負わせている。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****輪郭が水と区別できなくなることである。**"
             "**そして顔は同じ顔である。** ⛔ **この作品は、それに名前を与えない**"
             "——**名を与えないことが、この1本の内容である。**",
 },

 "lighting": {
   "base": "The stars and their reflection on the water — **and nothing else.** ⚠️ **この1本の光源は一つであり、"
           "それは星である**（`沈んだ場所.states.夜` の註:「光源は星だけである」）。"
           "⚠️ **そして最初のコマでは、星を受けた反射の道が彼の顔に当たっている**——**それが `FROM` である。**"
           "⚠️ **火を出さない。****日の光も、夜明けの光も、月も出さない。**"
           "⚠️ **彼を別に照らさない**——**彼の顔の光は、水面の反射の道そのものである。**",
   "events": "**One, and it takes the whole shot.** **星を受けた水面の反射の道が、彼の顔から少しずつ"
             "滑り落ちていく**（2.002秒から 8.377秒まで）。⚠️ **光源は動かない**"
             "——**様式カードの逐語:「The grade holds for the whole shot — a colour temperature that swings "
             "is a different style.」** ⚠️ **これは色温度の揺れではない**——**変わるのは、彼の顔に当たる"
             "光の量だけである。****画全体の色は、最初のコマと最後のコマで同じである。**"
             "⚠️ **この機構（光源は動かず、水面が道を運ぶ）は、この仕様の側の判断である**"
             "——§20 の未処理を見る。",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE + " ⛔ **彼は名乗らない**——**名乗るのは歌である**（`l25`）。"
             "**この1本には、名乗りの音が一つも無い。**",
   "sfx": "**水の音だけである。****低い波が同じ間隔で寄せて返る音。**"
          "⚠️ **この1本に人の音は一つも無い**——**彼は何も言わず、口が動かず、泳がない。**"
          "⚠️ **衣の擦れる音も無い**——**彼は浮いているだけである。**",
   "music": K.NO_MUSIC + " ⚠️ **この1本の上では `l25` と `l26` が歌われている**"
            "——**ゆえに生成された音床は、同じ8.377秒に二つの音楽を置くことになる。**",
   "environment": "夜の海。**水、そして水だけである。** ⚠️ **岸の音も、鳥の音も、舟の音も無い**"
                  "——**この場所には、水以外の何も無い**（`沈んだ場所.base` の逐語:「Nothing is visible in "
                  "the water and nothing is visible on it.」）。",
 },

 "continuity": {
   "identity": "**Must preserve** — §18 に逐語で貼られた同一性の塊の、一句一句。体格・肌・髪・髭・顔・傷・"
               "**着ている一枚と、着ていないすべて**。⛔ **この1本の `KEEP` は顔である**"
               "——**影が濃くなっても、輪郭が水に溶けても、顔の形は変わらない。**"
               "⚠️ **カードの `avoid` の逐語:「Morphing that abandons the subject's identity instead of "
               "carrying it」**——**この1本は、同一性を運ぶ側である。****ゆえに同一性の塊が §18 に在る。**"
               "**May change** — 影の深さ、輪郭の見え方、光の量、髪の水への広がり方、そして水が運ぶ分の位置。",
   "spatial": "**面は水だけである。****岸も、陸も、目印も無い**——**カメラは何によっても向きを定められない**"
              "（`沈んだ場所.geography` の逐語）。**彼は画のほぼ中央に、上を向いて浮いている。**"
              "**カメラは真上にあり、彼との距離と高さを変えない。** ⚠️ **ゆえに画の中の彼の位置は、"
              "水面が運ぶ分だけ動く。****それはカメラの移動ではない。**",
   "temporal": "夜である。⚠️ **この3本（`s23`・`s24`・`s25`）は同じ記憶の三つの瞬間である**"
               "——**`s24` から `s25` へ、時は経たない。****変わるのは知だけである**（開示の変化点④）。"
               "⛔ **そしてこの1本が、この作品の最後の開示である**——**ここから先、観客は何も新しく知らない。**"
               "⚠️ **画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** ⚠️ **光は星とその反射だけである。**"
             "⚠️ **この1本は `transformation` を名乗るが、その形式は §15 と衝突しない**"
             "——**カードが §15 に求めるのは「カットもディゾルブも過程の段も無いこと」であって、"
             "場所でも時刻でも同一性でもない。****ゆえに §15 は一句も免除されない。**"
             "⚠️ **そしてカードは「誰が変わるか」を一つに限る**（逐語:「One change, one subject.」）"
             "——**この1本で変わるのは、彼の顔に当たる光だけである。**",
   "motion": "Full animation, not limited. **光と、水面と、髪と、衣と、カメラが動く。** "
             "⚠️ **彼は浮かんだままである。****カメラは1回だけ動き、切れ目のコマでもまだ動いている。**",
   "sound": "**水。****音楽なし。言葉なし。** ⚠️ **名乗りの音も無い。**"
            "⚠️ **この1本の上では主題歌が歌っているが、この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**彼女はこの1本に、四つの姿のどれとしても現れない。** **声も、温かさも、動く空気も、"
     "水面の光も、ここには無い**——**この1本の光は星だけであり、それは彼女の仕業として書かれない。**"
     "⛔ **「誰でもない」という一行を、彼女の仕業にしない。**")) + [
   "⛔ **No intermediate stage is shown** — **光は連続して抜けるだけである。****二段階の状態を並べない。**"
   "（逐語, the card's own `Negative`: `no intermediate stage held`）。",
   "⛔ **No name is ever visible or audible** — no letters, no numerals, no writing on any surface, no "
   "spoken name, no subtitle, and **no caption saying that he has no name** (逐語, `forbidden_set`: "
   "`no legible text on any surface`). ⚠️ **`world.rules` の三番が、この1本でいちばん強く掛かる。**",
   "⛔ **His mouth does not move, and he does not name himself** — **名乗るのは歌である**（`l25`）。",
   "⛔ **No second simultaneous transformation** — **変わっているのは、この一人だけである**"
   "（逐語, the card's own `Negative`）。**水面も、光も、同時に別のものへ変わらない。**",
   "⛔ **No second person in this frame at any distance and in any focus** — no companion, no one "
   "swimming, no silhouette, **and no second body at the surface or under it**"
   "（逐語, `forbidden_set`: `no other human being in frame — no companion, no crowd, no second person`）。",
   "⛔ **No morphing that abandons his identity** — **顔は同じ顔である。**"
   "**変わるのは、その上に当たる光の量だけである**（逐語, the card's `avoid`）。",
   "⚠️ **No return to the opening state** — **カードの逐語:「The return is a decision.」**"
   "**この1本は戻らない。****抜けた光は、最後のコマまで戻らない。**",
   "⚠️ **No blanket colour grade** — **画全体の色は、最初のコマと最後のコマで同じである。**"
   "**暗くなるのは、彼の顔に当たる光の量だけである。**",
   "⚠️ **No sunlight, no dawn light, no moonlight, no firelight** — **この場所の光は星だけである**"
   "（`沈んだ場所.states.夜` の註）。**彼を別に照らす光も無い。**",
   "⚠️ **No boat, no ship, no hull, and no vessel in this frame** — **この水には舟が居ない**"
   "（`沈んだ場所.geography` の逐語:「Its only difference is that the raft is not in it.」）。",
   "⚠️ **No white water** — **この場所の波は黒く、白いのは反射の道だけである**"
   "（`沈んだ場所.states.夜` の註の逐語:「波は黒く、反射の道だけが白い。」）。",
 ],
 "must": [
   "⛔ **名を失うことを、姿を変えずに写す** — **この1本の狙いである**（記録の `aim` の逐語）。",
   "**光が彼の顔から少しずつ抜けていく** — **そしてそれだけである**"
   "（記録の `motion.quality` の逐語:「光が彼の顔から少しずつ抜けていく。それだけである。」）。",
   "⛔ **変わらないこと** — **顔は最後のコマまで同じ顔である**（§8 の `KEEP`）。",
   "**影が濃くなり、輪郭が水と区別できなくなる** — そして**それがこの1本の頂点である。**",
   "⛔ **変身の形式を使いながら、変身を一度も見せない** — **カットも、ディゾルブも、過程の段も無い。**",
   "⛔ **名を一度も出さない** — **画面にも、字にも、音にも。****彼は名乗らない。**",
   "**光は星とその水面の反射だけである** — 火も、月も、日の光も、夜明けの光も無い。",
   "⚠️ **カメラは彼から離れず、寄りもしない** — **記録の逐語であり、高さも変えない。**",
   "⚠️ **`transformation` の5つを満たすこと** — `FROM`・`TO`・`TRIGGER`・`KEEP`・`DURATION`。"
   "**そして引き金は歌の行の頭である**——**画面の中には無い。**",
 ],
 "prefer": "The frame read as water first and a man second — **the reflection's path lying across his face "
           "at the first frame and slipping off it by the last**; the shadows deepening on the skin; his "
           "hair spread on the surface; **the black carried without detail** — the one value the grade does "
           "not touch.",
 "allow": "A lens flare where the reflected path crosses the frame; a moderate depth of field that lets the "
          "deeper water go soft; **a slow travel that keeps its distance and its height and never stops.**",

 "priorities": [
   "⛔ **名を失うことを、姿を変えずに写すこと** — **この1本の狙いである**（記録の `aim` の逐語）。",
   "⛔ **顔が変わらないこと** — **この形式の最大の罠はモーフィングである**（カードの `avoid` が名指しする）。"
   "**この1本は、同一性を運ぶ側である。**",
   "⛔ **名を一度も出さないこと** — **`world.rules` の三番。****画面にも、字にも、音にも。**",
   "⛔ **変身を一度も見せないこと** — **カットも、ディゾルブも、過程の段も無い。**",
   "⛔ **彼の口が動かないこと** — **名乗るのは歌である。**",
   "⚠️ **カメラが離れも寄りもしないこと** — **記録の逐語であり、高さも距離も保つ。**",
   "**光は星とその反射だけであること** — 火も、月も、夜明けの光も無い。",
   "⚠️ **`transformation` の5つを満たすこと** — `FROM`・`TO`・`TRIGGER`・`KEEP`・`DURATION`。",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `transformation` を名乗るが、その禁制（`no cut`・`no dissolve`・`no wipe`・"
   "`no stated process`・`no intermediate stage held` ほか）は §16 に在って、ここには無い。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "An 8.377-second cinematic take (16:9) of open sea at night, seen from directly above, one clip, one "
   "continuous take, one change: **the light leaves his face, and his face does not change.** At the first "
   "frame one man floats at the surface with the path of reflected starlight lying across his face; at the "
   "last the light has gone off it, the shadows have deepened, **the outline of his head is barely "
   "distinguishable from the water — and it is the same face.**\n\n"
   "0-2.002s: **the man's face at the surface, lit** — the broken path of reflected starlight lying across "
   "it. **He does not move.**\n"
   "2.002-5.001s: **the light begins to leave** — **the reflected path slides off his face as the water "
   "carries it away**, and the shadows on his skin deepen. **The shape of his face does not change.**\n"
   "5.001-8.377s: **the outline becomes barely distinguishable from the water** — **and the face is the "
   "same face, and it is the same face on the last frame of the take.**\n\n"
   "{IDENTITY}\n\n"
   "**He is the only person in this frame at any distance and in any focus: no second body, no one "
   "swimming, no other person at the surface or under it, and no second thing changing with him.** **The "
   "light is the stars and their one broken path on the water, and there is no other source and no second "
   "light: no fire, no torch, no lamp, no dawn and no moon.** **No blood, no wound and no corpse.** "
   "**No boat, no ship, no sail and no other vessel is in this frame, and nothing is floating in it.** "
   "**He does not speak and he does not name himself, and no letters appear on any surface.** **This is a "
   "bronze-age sea before classical Greece.** **This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the light has left his face, and his face has not changed.)"),

 "visual_scene": (
   "Open sea at night, photographed from directly above as a film frame: black water, fine-grained and "
   "broken, carrying one path of reflected starlight; no land, no landmark and no shore anywhere in the "
   "frame. **At the centre one man lies at the surface, face up, alone, still — dark hair matted with salt "
   "and spread on the water, a full beard above the surface, weathered skin, and one coarse undyed wool "
   "tunic, dark and heavy with water, worn through at the shoulder seam — and the path of reflected "
   "starlight lies across his face, deepening the shadows on it and sliding off it as the surface carries "
   "it away, so that the outline of his head goes toward the water's own black. He is the only person in "
   "the frame and nothing else is in the frame with him.**"),

 "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones", "still black water broken by one path of reflected starlight"
 ),

 "motion_prompt": (
   "Full animation, not limited, one continuous change with no cut and no dissolve. **The water moves and "
   "he does not.** The surface runs in one direction at a rate that does not change, and the broken path "
   "of starlight on it splits and comes back; **from 2.002s the reflected path slides off his face and the "
   "shadows on his skin deepen, and from 5.001s the outline of his head becomes barely distinguishable "
   "from the water.** **He floats face up and holds that: not one stroke, not one raised hand, no turning "
   "of the head, no sinking — and his face is the same face all the way to the last frame.** **The camera "
   "travels slowly at one fixed height, keeping the same distance from him, and does not stop.** No "
   "morphing or drifting facial identity, no motion blur smears, no stutter, no static frames — **the "
   "light moves in every frame of the take, and his face has not changed on the last one.**"),

 "camera_prompt": (
   "Third person, **directly above him** — the lens looking straight down at the water, so that he lies in "
   "the frame's centre and the empty sea fills everything around him. One event only: **a slow continuous "
   "travel that keeps him at the same distance and at one fixed height, at a rate that does not change, "
   "still travelling on the last frame of the take.** ⚠️ **The move is motivated by staying above him** — "
   "the surface carries him slowly, so the camera travels at the same rate to hold the same distance. "
   "⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot spends the Steadicam** — a "
   "slow travel with the low frequency of a rig that has mass. **It neither approaches him nor leaves "
   "him.** No descent, no approach, no withdrawal, no tilt, no rotation, no handheld, no whip, no shake, "
   "no snap zoom, no rack focus, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water, and only water — long low swell arriving and going back "
   "at one interval.** ⚠️ **There is no human sound in this shot at all** — he does not speak, does not "
   "name himself, does not call and does not swim, and there is no second person and no vessel to make a "
   "sound. ⚠️ **Nothing else is heard** — no shore, no bird, no oar, and no sound of anything being done, "
   "**no sound marking the change.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (transformation) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②）。"
                        "⚠️ **この1本は人物を持つので、同一性の塊が §18 の `Master Prompt` と `Visual Prompt` の"
                        "両方に逐語で貼られている**——**要約しない。**"
                        "⚠️ **参照集合は `男.identity` と `男.negatives`、そして場所の3鍵である**"
                        "——**`s24` と同じ5鍵であり、`s23` とは違う。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water only ／ no music",
 "unresolved": [
   "⚠️ **光が抜ける機構を、記録は名指していない。** この仕様は「**星を受けた水面の反射の道が、"
   "彼の顔から滑り落ちていく**」とした——**光源は動かず、動くのは水面である。**"
   "⛔ **機構を書かねば、生成器は「画が暗くなる」と読む**——**それは様式の法（`The grade holds for the "
   "whole shot`）に触れる。****この機構で正しいかは、絵を見て著者が決める。**",
   "⚠️ **`TRIGGER` を「歌の行の頭（2.002秒）」とした。** 記録のビートは曲の事象で切られており、"
   "**画面の中に引き金が無い。** カードは「引き金を与えるか、無いと名乗れ」と言うので、"
   "**無いと名乗った**（逐語:「Give the change a trigger, or state that it has none — do not leave the "
   "moment it starts to chance」）。**この読みが正しいかは著者が決める。**",
   "⚠️ **この1本は2行を束ねている**（`l25` 3.590秒 ＋ `l26` 4.787秒）。⚠️ **この仕様は2行を1本として扱い、"
   "`FROM` も `TO` も一つずつである**——カードの逐語:「**One change, one subject.**」"
   "⛔ **2行目の内容を、この1本に足していない**（足せば「二つ目の変化」になり、この形式が壊れる）。"
   "**ゆえにこの1本は、歌が2行あるのに、画の変化は1つである。****それが正しいかは著者が決める。**",
   "⚠️ **名が無いことを、機械は測れない。** **測れるのは「名が画面にも音にも一度も現れないこと」までである。**"
   "**その先は、絵と歌を突き合わせて著者が見る。**",
   "⚠️ **「輪郭が水と区別できなくなる」を、生成器が「彼が水になる」と読むか。**"
   "⛔ **この1本は変身の形式を名乗るので、その読みへ引かれやすい**——"
   "**それでも彼は人であり、顔は同じ顔である**（カードの `avoid` の逐語:「Morphing that abandons the "
   "subject's identity」）。**どこまで溶かしてよいかは、絵を見て著者が決める。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **顔が変わる（モーフィング）。** **この1本のいちばん高い危険である**"
   "——**カードの `avoid` が名指しし、そしてこの1本は変身の形式を名乗っている。**",
   "⛔ **名が出る。** ⚠️ **字幕・字・声・呼び名**——**`world.rules` の三番に反する。**",
   "⛔ **彼が口を動かす／名乗る。** ⚠️ **名乗るのは歌である。**",
   "**過程の段が見える。** ⚠️ **ディゾルブ・二段階・カット**——**この形式が存在する理由がそれである。**",
   "**画全体が暗くなる。** ⚠️ **様式の法（`The grade holds for the whole shot`）に触れる**"
   "——**抜けるのは彼の顔の光だけである。**",
   "**戻る。** ⚠️ **カードの逐語:「The return is a decision.」****この1本は戻らない。**",
   "**二つ目が同時に変わる。** ⚠️ **水面・光・舟**——**カードの逐語:「no second simultaneous "
   "transformation」。**",
   "**カメラが寄る／離れる。** ⚠️ **記録の逐語に反する**（「カメラは彼から離れず、しかし寄りもしない。」）。",
   "**二体目が浮く。** ⚠️ **`s24` と同じ危険であり、この水は同じ水である。**",
   "**白い波が立つ。** ⚠️ **この場所の波は黒い**（`states.夜` の逐語:「波は黒く、反射の道だけが白い。」）。",
   "**光が増える。** ⚠️ **月・火・夜明けの光が入れば、この1本は別の時刻の1本になる。**",
 ],
}

if __name__ == "__main__":
    print("s25 content OK — keys:", len(C))
