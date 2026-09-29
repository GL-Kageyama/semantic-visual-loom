# -*- coding: utf-8 -*-
"""odyssey-s24 — meaning-responsive — 沈んだ場所 / 夜 / 4.708s. The man floats, face up.

Disclosure change point ③ (`沈んだ者たち: present`). This is the shot that carries `男.identity`.
"""
import common as K


C = {
 "n": "s24",
 "title": "私だけが浮いていた——いちばん短い1本が、いちばん重い一行を負う",
 "duration": "4.708",
 "format": "meaning-responsive",
 "has_man": True,
 "place": "沈んだ場所",
 "time": "夜",
 "segment": "bridge-2",

 "band": [
   "『永遠より遠い』 bridge「沈んだ場所」 / 余白 / still —— 私だけが浮いていた——最も短い1本が、最も重い一行を負う",
   "空の海に、一人が水面に浮いている——他には何も無い。",
   "4.708秒、カメラは真上から彼と、彼の周りの海を写す——水面が一度だけ大きく上下するのが、切れ目である。",
   "彼は浮いているだけで、動かず、何も言わない——それだけである。",
 ],
 "header": """⛔ **開示の変化点③である**（`ledger.disclosure`）——`沈んだ者たち: present`。
出所は曲の `l24`「**私だけが浮いていた**」。
⚠️ **この作品で最も短いショットである**（記録の逐語）。⚠️ **下限の4秒は上回っている**——**ゆえに伸ばさない。**
⛔ **「短いから伸ばす」をしない**（`docs/seedance-route.md` の明示の規則）。
⚠️ **`s23` を変化点にしなかった理由**（`ledger.disclosure` の註の逐語）——
「**あの一行は、仲間が居たことを告げるが、彼らがどうなったかを告げない。**『**居た**』と『**もう居ない**』は別の知である。」
⛔ **ゆえに知が動くのは、この1本である。**
⛔ **形式は `meaning-responsive`。****起きたことではなく、意味に反応して画面が変わる。**
⚠️ **この1本では、何も起きていない。** **水面だけが動いている。** **それでも画面が、失われたことを知っている。**
⚠️ **`mode: still`。** **止まるのは主題である**——**浮かんでいる者は、何もしていない。**
⚠️ **この1本は顔を持つ。** 参照集合が `男.identity` を含み、`ledger.locations.沈んだ場所.geography` の逐語が
「**A body in this location floats at the surface, alone, face up, with nothing else in frame.**」と言う
——**ゆえに §18 の `Master Prompt` と `Visual Prompt` の両方に、同一性の塊が逐語で貼られている**（`s23` には無い）。
⚠️ **`attached` を書かない。** 書けば「意図にあるのに添付が無い」ではなく「**記録が無い**」と鳴る（`L6`）。**この作品は、まだ1本も生成していない。**
⚠️ **この仕様のショット記録は `shots/odyssey-s24.yaml` である。**""",

 "intent": "One continuous take of one change — **意味に、画面が答える。** 最初のコマでは海は空であり、何も無い。"
           "最後のコマでは**一人が水面に浮かび、水面が一度だけ大きく上下し、そして彼はまだ浮かんでいる**"
           "——**応答のあとも浮かんだままであることが、切れ目のコマである。**"
           "⚠️ **何も起きていない。****そして答えに、原因が一つも無い。**"
           "⚠️ **彼は動かない**——**泳がず、手を上げず、振り向かない。**"
           "⚠️ **この1本はこの作品で最も短い**（記録の逐語）——**4.708秒で、一人だけが残ったことを写す。**"
           "⛔ **短いから伸ばさない。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本の場所も、記憶である。** 曲の `l24` が名指す水は、**`s23` と同じ水である**——"
   "⛔ **同じ夜、同じ場所、そして同じ一人の記憶である。**"
   "⚠️ **違うのは、知だけである**——`s23` では仲間が**居た**ことが告げられ、この1本では**もう居ない**ことが告げられる。"
   "⛔ **この場所の `base` は、物ではなく水を書く**（`ledger.locations.沈んだ場所` の註の逐語:"
   "「**死を写せば、この作品は悲惨な話になり、`theme-song.md` の抑制と衝突する。**」）。"
   "⚠️ **ゆえにこの1本は、失われたものを一度も名指さない。****名指すのは、水面の動きだけである。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本は、この作品で初めて「返事」を持つ1本である**——**しかし返すのは人ではない。**"
               "**水面である。** ⚠️ **何が失われたかを、画面は一度も言わない。****それでも画面は、知っている。**",
     "goddess": "⚠️ **この1本は彼女の場所ではない。****彼女は四つの姿のどれとしても現れない**——"
                "**この1本の光は星だけであり、それは彼女の仕業として書かれない。**",
     "name": "⚠️ **この行は、名を呼ばない。**「**私だけが**」——**この一行は名乗るが、名を与えない。**"
             "**画面にも、音にも、字にも、名は無い。**",
     "bow": "⚠️ **この1本に持ち手が無い。****弓も、斧も、道具も一つも出ない**——"
            "**彼の手は水の中にあり、何も握っていない。**",
     "places": "この1本が置くのは一つ——`沈んだ場所`。⚠️ **`s23` と同じ水であり、"
               "**違うのは「舟がそこに居ないこと」だけである。**",
     "japanese": "⚠️ **この1本には歌がある**——`l24`「私だけが浮いていた」が、この4.708秒の上を歌っている。"
                 "**そして歌は日本語である。**",
   },
   extra=[
     "⛔ **この1本が開示の変化点である**——`沈んだ者たち: present`。⚠️ **しかし、それを言うのは画面ではない。**"
     "**この1本は水だけを写す。** 台帳の註の逐語:「**ゆえにこの場所の `base` は、物ではなく水を書く。**」",
     "⚠️ **`s23` と `s24` は、同じ記憶の、別の知である。****時は経たない。**"
     "**ゆえにこの1本は、`s23` の続きではない**——**同じ夜の、もう一つの瞬間である。**",
     "⚠️ **この場所の光は星だけである**（`ledger.locations.沈んだ場所.states.夜` の註:「光源は星だけである。"
     "岸も舟も無いので、明るいものは何も無い——水面だけが、星を受けて黒く光る」）。"
     "⛔ **この場所の `base` には、もと「at the hour before dawn」と書いてあった**——"
     "**台帳の註がそれを直している**（**この3本は夜である**。**夜明けは `s16`〜`s19` であって、この記憶ではない**）。"
     "⚠️ **ゆえにこの1本に、夜明けの光は無い。**",
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
     "reflection, and it is the same from the first frame to the last. ⚠️ **The shot has no second light "
     "and no warm source.**",
   "Texture":
     "Still black water, fine-grained and broken, carrying one path of reflected starlight; the wool of the "
     "tunic coarse and dark with water, worn through at the shoulder seam; his hair matted with salt and "
     "spread on the surface; skin roughened and marked. ⚠️ **No shore, no shingle, no sand and no land are "
     "in this frame** — the frame holds water, night air and one man. Film grain present and even.",
   "Rendering":
     "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, a gentle flare where "
     "the light is in frame. **Not a photograph's stillness: a film frame, with a real lens's fall-off at "
     "the edges.** No illustration, no CGI look, no cartoon color.",
   "Visual Density": "Low — **the frame is empty water and one man, and it stays that way.** ⚠️ **This is "
                     "the shortest shot of the work**（記録の逐語）, so the density is earned with the frame's "
                     "emptiness rather than with the amount of time: **there is nothing in it to look at "
                     "except him and the surface.**",
   "Time": "`夜` — the night of the bridge, on the same water as `海`. ⚠️ **This place has no before and no "
           "after**（`沈んだ場所.states.夜` の逐語:「この場所には、前後が無い。」）. **The work does not fix a "
           "date**, and this is a memory rather than a record. ⚠️ **画の中で時は進まない** —"
           "**進むのは水面だけである。**",
   "Atmosphere": "The moment the loss becomes knowledge — **and the picture says it with water, because it "
                 "may not say it with anything else.**",
 }),

 "subjects": [
   {"name": "男",
    "ref": "**この1本の主題であり、この1本に居る唯一の人である。** ⚠️ **参照集合が `男.identity` を持つ**"
           "——**裁定②により参照画像は1枚も無いので、その英文だけが彼の顔を守る。**"
           "⚠️ **彼は水の上に、顔を上にして浮いている**（`ledger.locations.沈んだ場所.geography` の逐語:"
           "「A body in this location floats at the surface, alone, face up, with nothing else in frame.」）"
           "——**ゆえにこの1本は、この記憶で初めて顔を持つ1本である**（`s23` の参照集合には `男.identity` が無い）。",
    "appearance": "**§18 に逐語で貼られた塊のとおりである。** **濡れた髪が水に広がり、髭が水面に出て、"
                  "着ている一枚の粗い白い羊毛が水を吸って重い**（逐語:「one coarse undyed wool tunic, worn "
                  "through at the shoulder seam, belted with a plain leather cord」）。"
                  "⚠️ **裸足で、脚と腕は裸である**——**海中なので、それらは水面の下にある。**",
    "behavior": "**彼は浮いているだけである。****呼吸のたびに、水面がわずかに上下する。****それだけである。**"
                "⚠️ **彼は泳がず、手を動かさず、振り向かず、沈まない。**"
                "⚠️ **止まっていることが、この1本の意味を運ぶ**（形式カードの逐語:「**The bearer is named, "
                "and it does not act.**」）。",
    "continuity": "**Must preserve** — §18 に逐語で貼られた同一性の塊の、一句一句。"
                  "体格・肌・髪・髭・顔・傷・**着ている一枚と、着ていないすべて**。"
                  "⚠️ **この1本は、この記憶で初めて顔を写す1本である**——ゆえに**顔の一致は `s05` の岸から離れない。**"
                  "**May change** — 髪の水への広がり方、衣の水の含み方、水面の形、画の中の位置、"
                  "そして水面の高さ。",
    "notes": ["⚠️ **`meaning-responsive` の5つの変数は、この1本ではこう当てはめられる**"
              "（§8 の `Temporal Density` を見る）——`BEARER`＝**浮いている彼である**（**意味を運び、動かない**）／ "
              "`ANSWER`＝**水面が一度だけ大きく上下することである**（**世界の側で起きる**）／ "
              "`DELAY`＝**約1秒である**（1.502秒 → 2.5秒。**差は0.998秒**）／ "
              "`LIMIT`＝**答えは彼に届かない**（**浮かんだままである**）／ `DURATION`＝`4.708s`。",
              "⚠️ **彼が生きているかどうかを、この仕様は決めない。****記録が与えるのは「浮いている」と"
              "「呼吸のたびに水面が上下する」の二つだけである。** **この1本は、その二つだけを写す。**"]},
   {"name": "nobody",
    "ref": "**この1本に、彼のほかに人は一人も居ない。** ⚠️ **参照集合にも、もう一人を置く鍵が無い。**"
           "⛔ **ここが開示の変化点である**——**しかし、居ない者を画の中に置かない。**"
           "**置けば、この1本は別の1本になり、抑制と衝突する。**"
           "⚠️ **「もう居ない」ことを負うのは、画面ではなく、曲と台帳である。**",
    "appearance": "**無い。** ⚠️ **水の下にも、水面にも、遠景にも、誰も居ない。**",
    "behavior": "**無い。** ⚠️ **動くのは水面と、彼の髪と、衣の端だけである。**",
    "continuity": "⚠️ **二体目を足さないこと。****この1本がいちばん危ういのはここである**"
                  "——**開示が「仲間はもう居ない」へ動く1本なので、生成器は「もう一人」を足す方向へ引かれる。**"
                  "**足せば、この作品の抑制がそこで終わる。**",
    "notes": ["⚠️ **`Negative Prompt` はこの経路では床にならない**（§18 の前書き）。**ゆえにこれは肯定形で負う** "
              "— §16 `MUST NOT` と、`Master Prompt` 自身の散文が負う。",
              "⚠️ **弱い守りである。記録として書く。** ⚠️ **そしてこの1本では、"
              "「水に浮かぶ体」がこの作品でいちばん足されやすいものである。**"]},
 ],

 "environment": {
   "location": "`沈んだ場所` — **記憶の中の海であり、`s23` と同じ水である。**"
               "⛔ **違うのは一つだけである**（逐語:「Its only difference is that the raft is not in it.」）"
               "——**舟が居ない。** ⚠️ **岸も、目印も無い**（逐語:「There is no landmark and no shore; the "
               "camera cannot orient by anything.」）。",
   "elements": "夜の水面と、**星を受けた一本の反射の道**、そして**水の上に浮いている一人**。"
               "⚠️ **破片を一つも置かない**（`沈んだ場所.base` の逐語:「No wreckage, no bodies, no oars, no "
               "mast, no floating wood, no blood, no cloth.」）——**この場所の `base` は、物ではなく水を書く。**",
   "behavior": "**水面は同じ向きへ、同じ速さで動きつづける。****星の反射の道が、その上で細かく割れては戻る。**"
               "⚠️ **そして 2.5秒に一度だけ、水面が大きく上下する**——**それがこの1本の答えである。**"
               "⚠️ **環境は彼に反応しない**——**彼は浮かんだままであり、水面は彼を動かさない。**",
 },

 "objects": [
   "**水面と、星の反射の一本の道** — **この1本で動くのはこれだけである。**",
   "**彼が着ている一枚の粗い羊毛の衣** — 衣装であって小道具ではない"
   "（逐語:「one coarse undyed wool tunic, worn through at the shoulder seam, belted with a plain leather cord」）。"
   "⚠️ **水を吸って重く、肩の縫い目が擦り切れている。** 腰の革の紐のほかに、身につけた物が無い。",
   "⚠️ **この作品の小道具は4つだけであり**（`ledger.props`）、**この1本に来るものは無い**"
   "——舟・帆・斧・太陽の牛は、**この記憶のこの瞬間に無い。****舟は、この水に居ないことになっている。**",
 ],

 "ref_character": "**この1本は `男` の1本である。****そして、この1本に人は彼一人である。**"
                  "⚠️ **彼以外の人を、どの距離にも、どのピントにも置かない**"
                  "（`forbidden_set` の逐語:「no other human being in frame — no companion, no crowd, no "
                  "second person」）。⛔ **女神は現れない**——四つの姿のどれとしても。"
                  "**彼女の顔も、彼女の声も、彼女の温かさも、この1本には無い。**"
                  "⚠️ **参照は `男.identity` と `男.negatives`、そして場所の3鍵である。**"
                  "⛔ **添付は0点である**（裁定②）。",

 "ref_extra": [
   "⚠️ **形式カード `meaning-responsive` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; what "
   "follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §6 のこの一行と、§10・§12・§13 に足された一つの規則である。**",
   "⛔ **カードの逐語:「The camera may not tilt, push, or cut to express it — a camera move is a "
   "*statement about* the meaning, and this grammar wants the world to make it.」**"
   "⚠️ **ゆえにこの1本のカメラは、答えを作らない。****答えるのは水面である**（§10・§13）。",
   "⚠️ **カードは「何が意味を運ぶか」を名指せと言う**（逐語:「The bearer is named, and it does not act.」）。"
   "**この1本の `BEARER` は、浮いている彼である**——**そして彼は動かない**（§8）。",
 ],

 "narrative": {
   "core": "**一人だけが残ったことを、画面は水で受け取る** — 起きたことではなく、意味に反応する。",
   "beginning": "**真上から見た、空の海。****何も無い。** 面は水だけである。",
   "turn": "**一人が浮いている。****呼吸のたびに、水面がわずかに上下する。**",
   "peak": "**水面が一度だけ大きく上下する**（2.5秒から）。",
   "pull": "**それだけである**——**それだけであることが、切れ目のコマである。**"
           "**応答のあとも、彼は同じところに浮かんでいる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, in three parts, and the answer is the longest of them.** 最初の1.502秒は**空の海**に払われ、"
            "次の0.998秒は**彼と、呼吸に合わせた水面**に払われ、**最後の2.208秒がこの1本の答えである**"
            "——**水面が一度だけ大きく上下し、そして彼は浮かんだままである。**"
            "⚠️ **この1本はこの作品で最も短い**（記録の逐語）ので、**密度は時間の量ではなく、"
            "配分の形で稼ぐ**——**空・人・応答の三段であり、応答がいちばん長い。**"
            "⚠️ **`mode: still`** ——**止まるのは主題であって、画面ではない**"
            "（`shot-record.schema.json` の `motion`）。**水面と光とカメラは最後のコマまで動いている。**"
            "⚠️ **`held` を1つも使わない。** **ゆえに末尾のビートは `dense` である。** "
            "⚠️ **`meaning-responsive` の5つの変数（形式カードの逐語）**: `BEARER`＝**浮いている彼である**"
            "（**意味を運び、そして動かない**）／ `ANSWER`＝**水面が一度だけ大きく上下することである**"
            "（**世界の側で起きる。****カメラでも、彼の体でも、光でもない**）／ `DELAY`＝**約1秒である**"
            "（**1.502秒 → 2.5秒。差は0.998秒。**即答すればカットに見え、末尾で答えれば露見になる）／ "
            "`LIMIT`＝**答えは彼に届かない**（**浮かんだままである。****沈まず、動かず、起こされない**）"
            "——**届けば、答えは blanket colour grade として読まれる**／ `DURATION`＝`4.708s`。",

 "actions": [
   ("ACT_EMPTY", "切り出しは海である。",
    "**真上から見た、空の海。****何も無い。****明るいものは一つも無い。**"),
   ("ACT_FLOAT", "面は水だけで、その上に何も無い。",
    "**一人が浮いている**——**顔を上にして、動かない。****呼吸のたびに、水面がわずかに上下する。**"),
   ("ACT_ANSWER", "水面は細かく動いている。",
    "**水面が一度だけ大きく上下する**——**そして戻り、彼は同じところに浮かんだままである。**"
    "**そのコマが、この1本の切れ目である。**"),
 ],

 "camera": {
   "language": "Third person, **directly above him** — the lens looking straight down at the water, so that "
               "he lies in the frame's centre and the empty sea fills everything around him. "
               "⚠️ **記録の逐語:「カメラは真上から、彼と、彼の周りの空の海を写す。」**"
               "⚠️ **岸の高さでも、水面の高さでもない**——**真上である。**",
   "events": "One event only, **and it is not the answer.** `0-4.708s` — **a slow continuous travel across "
             "the water from directly above, at a rate that does not change, still travelling on the last "
             "frame of the take**; **he enters the frame at 1.502秒** because **カメラが彼のいるところへ着くのであって、"
             "彼が動くのではない。** ⚠️ **高さを変えない**——**真上の一つの高さを、最初のコマから最後のコマまで保つ。**"
             "⛔ **そしてこの移動は答えではない。****形式カードの逐語:「The camera may not tilt, push, or cut "
             "to express it — a camera move is a *statement about* the meaning, and this grammar wants the "
             "world to make it.」****答えるのは 2.5秒の水面である。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the crane** "
               "— held overhead at one fixed height, travelling at a rate that does not change, with the "
               "low frequency of a rig that has mass, and it does not wobble. ⚠️ **降りない。****寄らない。**"
               "**回らない。****傾けない**——**答えは、カメラの側では一つも作られない。**"
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, and "
               "**no unmotivated move.**",
 },

 "motion": {
   "subject": "**水面と、浮いている男の背中。****主題は止まる**——**彼は浮いているだけである。**"
              "⚠️ **記録の `motion.subject` の逐語である。**",
   "object": "**動くのは彼の髪と、衣の端だけである。****そして水面が一度だけ大きく上下する**（2.5秒から）"
             "——**それがこの1本の答えである。** ⚠️ **彼は何も持っていないので、動く物は無い。**"
             "**彼の体は、水面の上下に少しだけ遅れて従う。**",
   "environment": "**水面は同じ向きへ、同じ速さで動きつづける。****星の反射の道が細かく割れては戻る。**"
                  "⚠️ **風はこの1本の画にも音にも無い**——**水面を動かすものが、画面の中に一つも無い**（§13）。"
                  "⚠️ **環境は彼に反応しない**——**彼が浮かんでいても、水面は彼を避けない。**",
   "weight": "**水は重い。****そして水を吸った羊毛は重い**——**彼の体は水面の下にあり、"
             "この1本の重さは、浮いていることの重さである。**",
   "inertia": "**水面は行き過ぎてから戻る。****大きく上下した水面は、ゆっくり戻る。**"
              "**彼の体は、その上下に少しだけ遅れて従う。** ⚠️ **何も瞬間には戻らない。**",
   "acceleration": "**加速しない。** ⚠️ **カメラの流れも、水面の間隔も、一定である**"
                   "——**この1本に見せ場の加速は一つも無い。****大きく上下することも、急ではない。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この4.708秒に、止まったフレームは一つも無い**"
               "——**彼が止まっているあいだも、水面と髪とカメラが動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**一度だけ大きく上下することは、衝撃ではなく、応答である。**",
 },

 "emotion": {
   "arc": "**止まっている一人が、水面に浮いている。** そして**それが「一人だけが残った」に見えること**が、"
          "この1本の感情である。⚠️ **何も起きていないのに、画面が失われたことを知っている。**"
          "⛔ **説明は一つも無い**——**群れも、舟も、他の誰も、この画に居ない。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****水面が一度だけ大きく上下することである。**"
             "**彼はそれを見ない**——**見ていないものを、画面だけが知っている。**"
             "⛔ **この作品は、それに名前を与えない**——**字幕も、声も、字も無い。**",
 },

 "lighting": {
   "base": "The stars and their reflection on the water — **and nothing else.** ⚠️ **この1本の光源は一つであり、"
           "それは星である**（`沈んだ場所.states.夜` の註:「光源は星だけである」）。"
           "⚠️ **火を出さない。****日の光も、夜明けの光も、月も出さない**——**この記憶は夜の中にある。**"
           "⚠️ **彼を別に照らさない**——**彼は同じ星の光の中にあり、専用の光を持たない。**",
   "events": "**One, and it is not light.** ⚠️ **この1本の答えは、光の側では起きない。**"
             "2.5秒から水面が一度だけ大きく上下するので、**星の反射の道がそこで一度だけ大きく割れる**"
             "——**それが光の側で起きることの全部である。****光源は動かない。**"
             "⚠️ **様式カードの逐語:「The grade holds for the whole shot — a colour temperature that swings "
             "is a different style.」****色はどこでも同じである。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水の音だけである。****低い波が同じ間隔で寄せて返る音、そして 2.5秒に一度だけ、水が大きく動く音。**"
          "⚠️ **この1本に人の音は一つも無い**——**彼は何も言わず、泳がず、呼ばない。**"
          "⚠️ **足音も、衣の擦れる音も無い**——**彼は浮いているだけである。**",
   "music": K.NO_MUSIC + " ⚠️ **この1本の上では `l24`「私だけが浮いていた」が歌われている**"
            "——**ゆえに生成された音床は、同じ4.708秒に二つの音楽を置くことになる。**"
            "**この1本は短いので、それはいっそう避けねばならない。**",
   "environment": "夜の海。**水、そして水だけである。** ⚠️ **岸の音も、鳥の音も、舟の音も無い**"
                  "——**この場所には、水以外の何も無い**（`沈んだ場所.base` の逐語:「Nothing is visible in "
                  "the water and nothing is visible on it.」）。",
 },

 "continuity": {
   "identity": "**Must preserve** — §18 に逐語で貼られた同一性の塊の、一句一句。体格・肌・髪・髭・顔・傷・"
               "**着ている一枚と、着ていないすべて**。⚠️ **この1本は、この記憶で初めて顔を写す1本である**"
               "（`s23` の参照集合には `男.identity` が無く、この1本には在る）——**ゆえに顔の一致は `s05` の岸から"
               "離れてはならない。** ⚠️ **基盤は、参照画像が無い状態でそれを守る規則を一つだけ持っている**"
               "——`video-spec` 形式カードの逐語:「**Identity lock.** … the continuity block … is **pasted "
               "whole into every instance** — not summarized, not referenced.」**ゆえにこの仕様は、あの塊を "
               "§18 の `Visual Prompt` と `Master Prompt` の両方に、まるごと貼っている。** ⚠️ **要約しない。** "
               "**May change** — 髪の水への広がり方、衣の水の含み方、水面の形、画の中の位置、そして水面の高さ。",
   "spatial": "**面は水だけである。****岸も、陸も、目印も無い**——**カメラは何によっても向きを定められない**"
              "（`沈んだ場所.geography` の逐語:「There is no landmark and no shore; the camera cannot orient "
              "by anything.」）。**彼は画のほぼ中央に、上を向いて浮いている。****カメラは真上にあり、"
              "一つの高さを保つ。** ⚠️ **この場所には前後が無い**——**ゆえに「中央」とは、この1本では"
              "画の中央のことである。**",
   "temporal": "夜である。⚠️ **この3本（`s23`・`s24`・`s25`）は同じ記憶の三つの瞬間である**"
               "——**`s23` から `s24` へ、時は経たない。****変わるのは知だけである**（開示の変化点③）。"
               "⚠️ **画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** ⚠️ **光は星とその反射だけである。**"
             "⚠️ **この1本は `meaning-responsive` を名乗るが、その形式は §15 と衝突しない**"
             "——**`remembered-world` や `coexisting-realities` と違い、この形式が免除を求めるのは"
             "「答えの原因が画面に無いこと」であって、場所でも時刻でも同一性でもない。**"
             "**ゆえに §15 は一句も免除されない。**",
   "motion": "Full animation, not limited. **水面と、髪と、衣と、カメラが動く。** "
             "⚠️ **彼は最後のコマまで同じところに浮かんでいる。**"
             "⚠️ **カメラは1回だけ動き、切れ目のコマでもまだ動いている。**",
   "sound": "**水。****音楽なし。言葉なし。** ⚠️ **この1本の上では主題歌が歌っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "**彼女はこの1本に、四つの姿のどれとしても現れない。** **声も、温かさも、動く空気も、水面の光も、"
     "ここには無い**——**この1本の光は星だけであり、それは彼女の仕業として書かれない。**")) + [
   "⛔ **No second person in this frame at any distance and in any focus** — no companion, no one "
   "swimming, no one standing, no silhouette, no boat's crew, and **no second body at the surface or "
   "under it** (逐語, `forbidden_set`: `no other human being in frame — no companion, no crowd, no "
   "second person`). ⚠️ **開示が動く1本であり、ここがこの1本のいちばん高い危険である。**",
   "⛔ **No corpse, no drowned face, no limb at the surface, no hand reaching up, no hair that is not "
   "his** — **この1本は水を写す。****人を二人にしない。**",
   "⚠️ **No wreckage, no oars, no mast, no floating wood, no cloth, no blood** in the water (逐語, "
   "`沈んだ場所.base`). ⚠️ **面は水と、浮いている一人だけである。**",
   "⚠️ **No visible cause for the water's single rise** — no wind shown, no rain, no breaking swell, no "
   "wake from his body, no current made visible, and nothing entering the frame (逐語, the card's own "
   "`Negative`: `no visible cause`).",
   "⚠️ **No camera move, no cut, and no rack focus carrying the meaning** (逐語, the card's own `Negative`). "
   "**カメラは答えを作らない**——**答えるのは水面である。**",
   "⚠️ **No blanket colour grade** — **答えは水面の形で起き、色では起きない**（逐語, the card's own "
   "`Negative`: `no blanket colour grade`）。",
   "⚠️ **No caption and no voice-over naming the meaning** (逐語, the card's own `Negative`) "
   "——**「一人だけが残った」と、画面は一度も言わない。**",
   "⚠️ **No sunlight, no dawn light, no moonlight, no firelight** — **この場所の光は星だけである**"
   "（`沈んだ場所.states.夜` の註）。**彼を別に照らす光も無い。**",
   "⚠️ **No boat, no ship, no hull, and no vessel in this frame** — **この水には舟が居ない**"
   "（`沈んだ場所.geography` の逐語:「Its only difference is that the raft is not in it.」）。",
   "⛔ **No drift that changes him** — **顔は最後のコマまで同じ顔である。**"
   "**滑ってよいのは水面だけである。**",
 ],
 "must": [
   "**一人だけが残ったことを、4.708秒で写す** — **この1本の狙いである**（記録の `aim` の逐語）。",
   "**一人が水面に浮いている** — **顔を上にして。****そして浮かんだままであることが、切れ目のコマである。**",
   "⚠️ **答えは世界の側で起きる** — **水面が一度だけ大きく上下する。****カメラでも、彼の体でも、光でもない。**",
   "⚠️ **答えに原因が無い** — **風も、雨も、彼の動きも、画面に入る物も無い。**",
   "⛔ **この1本に、彼のほかに人は一人も居ない** — **水の中にも、水面にも、遠景にも。**",
   "⚠️ **答えは彼に届かない** — **沈まず、動かず、起こされない。****浮かんだままである**"
   "（§8 の `LIMIT`）。",
   "⚠️ **`mode: still`** — **止まるのは主題である。****彼は浮いているだけである。**"
   "**カメラと水面は止まらない。**",
   "**光は星とその水面の反射だけである** — 火も、月も、日の光も無い。",
   "⚠️ **4.708秒を伸ばさない** — **この作品で最も短いショットである**（記録の逐語）。"
   "**下限の4秒は上回っている。****ゆえに伸ばす理由が無い。**",
   "⚠️ **`meaning-responsive` の5つを満たすこと** — 意味を運ぶのは彼、答えるのは世界、"
   "**遅れは約1秒、答えは彼に届かない、そして尺は 4.708秒である。**",
 ],
 "prefer": "The frame read as water first and a man second — **the surface fine-grained and broken, his "
           "hair spread on it, the wool dark and heavy with water**; the reflection's path low and broken "
           "around him; **the black carried without detail** — the one value the grade does not touch.",
 "allow": "A lens flare where the reflected path crosses the frame; a moderate depth of field that lets "
          "the deeper water go soft; **a slow overhead travel that never changes its height and never stops.**",

 "priorities": [
   "⛔ **一人だけが残ったことを、4.708秒で写すこと** — **この1本の狙いである**（記録の `aim` の逐語）。",
   "⛔ **答えに原因を置かないこと** — **画面の中の何かが水面を動かせば、この形式はそこで壊れる。**",
   "⛔ **二体目を水に置かないこと** — **開示の変化点であり、ここが最も足されやすい。**",
   "⚠️ **答えが彼に届かないこと** — **彼は浮かんだままであり、沈まない**（§8 の `LIMIT`）。",
   "⚠️ **短さを保つこと** — **4.708秒。****伸ばさない。**",
   "**顔の一致** — **この記憶で初めて写る顔であり、参照画像が1枚も無い**（裁定②）。",
   "**光は星とその反射だけであること** — 火も、月も、日の光も無い。",
   "⚠️ **`meaning-responsive` の5つを満たすこと** — 意味を運ぶのは彼、答えるのは水面、"
   "**遅れは約1秒、限度は彼、尺は 4.708秒。**",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `meaning-responsive` を名乗るが、その禁制（`no visible cause`・"
   "`no camera move answering the meaning`・`no blanket colour grade` ほか）は §16 に在って、ここには無い。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 4.708-second cinematic take (16:9) of open sea at night, seen from directly above, one clip, one "
   "continuous take, one change: **the water answers.** At the first frame the sea is empty; at the last "
   "one man floats at the surface and the water has risen once and come back, **and he is still floating.** "
   "**Nothing in the frame causes it — no wind, no rain, no wake from his body, and nothing entering the "
   "frame.**\n\n"
   "0-1.502s: **the sea from directly above and there is nothing in it.** The surface is the whole of the "
   "frame and nothing in it is lit.\n"
   "1.502-2.5s: **one man is floating, face up, and he does not move.** His breath makes the surface rise "
   "and fall very slightly. **He does not swim, he does not raise a hand, and he does not sink.**\n"
   "2.5-4.708s: **the surface rises once, largely, and comes back** — the path of reflected starlight "
   "splits wide where it rises — **and the take ends on the man still floating at the surface.**\n\n"
   "{IDENTITY}\n\n"
   "**He is the only person in this frame at any distance and in any focus: no second body, no one "
   "swimming, no other person at the surface or under it, no wreckage, no oars, no mast, no floating wood "
   "and no cloth in the water.** **The light is the stars and their one broken path on the water, and "
   "there is no other source and no second light: no fire, no torch, no lamp, no dawn and no moon.** "
   "**No boat, no ship, no sail and no other vessel is in this frame.** **This is a bronze-age sea before "
   "classical Greece: no made thing of any later age and no legible text on any surface.** **This is a "
   "Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the water answers.)"),

 "visual_scene": (
   "Open sea at night, photographed from directly above as a film frame: black water, fine-grained and "
   "broken, carrying one path of reflected starlight that runs low across the surface; no land, no "
   "landmark and no shore anywhere in the frame. **At the centre of the frame one man lies at the surface, "
   "face up, alone, still: dark hair matted with salt and spread on the water, a full beard above the "
   "surface, weathered skin, and one coarse undyed wool tunic, dark and heavy with water, worn through at "
   "the shoulder seam. He is the only person in the frame and nothing else is in the frame with him** — no "
   "raft, no wreckage, no floating wood and nothing else at the surface or under it."),

 "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones", "still black water broken by one path of reflected starlight"
 ),

 "motion_prompt": (
   "Full animation, not limited. **The water moves and the man does not.** The surface runs in one "
   "direction at a rate that does not change, and the broken path of starlight on it splits and comes "
   "back; **from 2.5s the surface rises once, largely, and returns**, and **he follows that rise and fall "
   "only slightly, a little late, the way a body at the surface does.** **He floats face up and holds "
   "that: not one stroke, not one raised hand, no turning of the head, no sinking.** **The camera travels "
   "slowly across the water from directly above at one fixed height and does not stop.** No motion blur "
   "smears, no stutter, no floaty weightless motion, no static frames — **the water moves in every frame "
   "of the take, and he is still floating on the last one.**"),

 "camera_prompt": (
   "Third person, **directly above him** — the lens looking straight down at the water, so that he lies in "
   "the frame's centre and the empty sea fills everything around him. One event only: **a slow continuous "
   "travel across the water from directly above, at a rate that does not change, still travelling on the "
   "last frame of the take**; **he comes into the frame at 1.502s because the camera arrives where he is "
   "floating, not because he moves.** ⚠️ **The move is not the answer** — the answer is the water at 2.5s. "
   "⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot spends the crane** — held "
   "overhead at one fixed height, with the low frequency of a rig that has mass. **The height does not "
   "change.** No descent, no approach, no tilt, no rotation, no handheld, no whip, no shake, no snap zoom, "
   "no rack focus, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water, and only water — long low swell arriving and going back "
   "at one interval, and one large movement of water once, at 2.5s.** ⚠️ **There is no human sound in this "
   "shot at all** — he does not speak, does not call, does not swim, and there is no second person and no "
   "vessel to make a sound. ⚠️ **Nothing else is heard** — no shore, no bird, no oar, and no sound of "
   "anything being done."),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (meaning-responsive) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⚠️ **この1本は人物を持つので、同一性の塊が §18 の `Master Prompt` と "
                        "`Visual Prompt` の両方に逐語で貼られている**——**要約しない。**"
                        "⚠️ **参照集合は `男.identity` と `男.negatives`、そして場所の3鍵である**"
                        "——**`s23` と違い、この1本には `男.identity` が在る。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water only, and one large movement of water once ／ no music",
 "unresolved": [
   "⚠️ **彼の目が開いているか閉じているかを、記録は決めていない。** この仕様はどちらも書かない"
   "——**決まっていないことを、仕様が決めれば、それは記録が測定でなくなる**（`L6` の註と同じ理由）。",
   "⚠️ **呼吸が音として聞こえるかどうかを、記録は決めていない。** この仕様は §14 に呼吸の音を置いていない。"
   "**置くかどうかは、絵と音を聞いて著者が決める。**",
   "⚠️ **「水面が一度だけ大きく上下する」が、この形式の言う「世界の答え」として十分かどうか。**"
   "カードは**「即答すればカットに見え、末尾で答えれば露見になる」**と言う（逐語）ので、"
   "**この仕様は答えを中ほど（2.5秒）に置いた**——**それで正しいかは、著者が見て決める。**",
   "⚠️ **カメラの移動が「意味を語る」と読まれないか。** カードは"
   "「a camera move is a *statement about* the meaning」と警告する。**この仕様は移動を「彼のいるところへ着くこと」"
   "に動機づけたが、それでも答えの直前にあるので、並置として読まれうる。**",
   "⚠️ **「水面が大きく上下する」を、生成器が「波が立つ」と読むか。** この場所の波は黒い"
   "（`states.夜` の逐語:「波は黒く、反射の道だけが白い。」）——**白い波が立てば、この1本は静けさを失う。**"
   "**許容の内側に収まっているかは、絵を見て著者が決める。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **二体目が水面に浮く。** **この1本のいちばん高い危険である**——**開示が「仲間はもう居ない」へ動く1本なので、"
   "生成器は「もう一人」を足す方向へ引かれる。**",
   "⛔ **血・傷・死体が出る。** ⚠️ **この場所の `base` が「物ではなく水を書く」のは、まさにこれを避けるためである。**",
   "**彼が泳ぐ・動く。** ⚠️ **`mode: still` が崩れ、この1本は「浮いている」の1本ではなくなる。**",
   "**水面の上下に原因が出る。** ⚠️ **風・雨・彼の動き・画面に入る物**——**どれか一つでも見えれば、"
   "この形式はそこで壊れる。**",
   "**答えが彼を動かす。** ⚠️ **沈む、顔が水に入る、位置が変わる**——**`LIMIT` の違反である。**",
   "**カメラが答えを作る。** ⚠️ **降りる、寄る、傾く、回る**——**カードが名指しで禁じている。**",
   "**光が増える。** ⚠️ **月・火・日の光が入れば、この1本は別の時刻の1本になる。**",
   "**短さが伸びる。** ⚠️ **4.708秒のあとにビートが足されれば、この作品で最も短いショットでなくなる**"
   "——**そして記録の `duration` と食い違う。**",
   "**顔が変わる。** ⚠️ **参照画像が1枚も無いので、守る道具は §18 の英文だけである**（裁定②）。",
   "**舟が浮かぶ。** ⚠️ **この作品は全ショットで舟と船を禁じており、この水には舟が居ないことになっている。**",
 ],
}

if __name__ == "__main__":
    print("s24 content OK — keys:", len(C))
