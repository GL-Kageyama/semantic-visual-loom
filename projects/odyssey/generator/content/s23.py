# -*- coding: utf-8 -*-
"""odyssey-s23 — remembered-world — 沈んだ場所 / 夜 / 11.649s. No person.

⚠️ This is the one shot of the thirty-four whose `reference_set` does not carry `男.identity`.
   The record says why: 彼はこの記憶の中に居ない. So `has_man` is False and no `{IDENTITY}`
   is written anywhere in this file — the generator appends nothing and pastes nothing.
"""
import common as K


C = {
 "n": "s23",
 "title": "太陽の牛——歌は屠ったと歌い、画面は屠る前を写す",
 "duration": "11.649",
 "format": "remembered-world",
 "has_man": False,
 "place": "沈んだ場所",
 "time": "夜",
 "segment": "bridge-1",

 "header": """⛔ **この作品でいちばん危うい1本である。** 出所は曲の `l23`「あの者たちは太陽の牛を屠った」——
⚠️ **この行は 10.000秒であり、直後に 1.649秒の歌の無い間がある**（215.053–216.702）。
⛔ **歌は「屠った」と歌う。では屠る場面を映すか。****映さない。** 理由は二つ（`props.太陽の牛` の註に書いてある）——
① **歌は既に過去形で歌っている。****いま起きていることではない。**
② **この作品の抑制**（`theme-song.md` の裁定5、および全編の語り口）。
⚠️ **ゆえに画面は、屠られる前の牛を写す。** ⛔ **耳が出来事を聞き、目が失われたものを見る**——**この食い違いは事故ではなく、この作品の設計である。**
⛔ **参照集合に `男.identity` を入れない。****彼はこの記憶の中に居ない**——**`l24`「私だけが浮いていた」が、彼の位置を決めている。**
⚠️ **この1本に人は一人も居ない。** そして**それでも `男.negatives` は参照集合に在る**（§6）。
⚠️ **`太陽の牛.negative` の3行目**——「**no cattle in any other scene of this work**」。**この牛は、この1本にしか現れない。**
⚠️ **形式は `remembered-world`**（記録でなく記憶。保たれた瞬間の中で中身が滑る）——**この作品で3本あるうちの3本目である**（`s02` の註を見る）。
⚠️ **この仕様のショット記録は `shots/odyssey-s23.yaml` である。**""",

 "intent": "One continuous take of one change — **牛の群れが、水際に立っている。** 最初のコマでは海は空であり、何も無い。最後のコマでは**七、八頭の牛が水際に立ち、低い光がその脚の間を抜けており、歌は既に終わっている**——**牛が立ったままであることが、切れ目のコマである。** ⚠️ **屠る場面は、この1本に一度も来ない。****歌が歌ったことは、画面では起きない。** ⚠️ **この1本に人は一人も居ない**——どの距離にも、どのピントにも。⚠️ **変化は切れ目のコマで終わる**——最後の1.649秒は歌の無い間であり、**その間も牛は立っている。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本の場所は、記憶である。** 曲の `l23` と `l24` が名指す水は、"
   "**`海` と同じ水である**——⚠️ **違うのは一つだけである**（`ledger.locations.沈んだ場所.geography` の逐語:"
   "「Its only difference is that the raft is not in it.」）。"
   "⛔ **この作品は、ここで島の外へ出る。** 岸も、洞口も、舟の置き場も無い——**面は水だけである。**"
   "⚠️ **そしてこの1本は、この作品で唯一「歌が歌ったこと」を写さない1本である**——"
   "**抑制が、いちばん強く試される。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本に人は一人も居ない。****ゆえに返事は、ここでも返されない**——"
               "**牛の群れは差し出しではない。** **この場所は、誰かが答える場所ではない。**",
     "goddess": "⚠️ **この1本は彼女の場所ではない。** **彼女は四つの姿のどれとしても現れない**——"
                "**声も、温かさも、動く空気も、水面の光も、ここには無い。**"
                "**この1本の光は星だけであり、それは彼女の仕業として書かれない。**",
     "name": "⚠️ **この行は、誰の名も呼ばない。** 曲は「**あの者たち**」と言う——"
             "**人数も、名も、誰であるかも言わない。****画面にも、音にも、字にも、名は無い。**",
     "bow": "⚠️ **この1本に持ち手が居ない。** **弓は無論のこと、牛を屠る道具も、一本も出ない**"
            "（`太陽の牛.negative` の逐語:「**no person with the herd, no herder, no weapon near them**」）。",
     "places": "この1本が置くのは一つ——`沈んだ場所`。⚠️ **`海` と同じ水であり、"
               "**違うのは「舟がそこに居ないこと」だけである。**",
     "japanese": "⚠️ **この1本には歌がある**——`l23`「あの者たちは太陽の牛を屠った」が、この11.649秒の上を歌っている。"
                 "**そして歌は日本語である。**",
   },
   extra=[
     "⛔ **歌は屠ったと歌い、画面は屠る前を写す。** **この食い違いは、この作品の設計である**"
     "——`props.太陽の牛` の註が二つの理由を書いている（**歌は既に過去形であること／この作品の抑制**）。"
     "⚠️ **画面は、屠られる前の牛を写す。****それがこの1本の内容である。**",
     "⛔ **この1本の記憶の持ち主は `男` である。****そして彼は、この記憶の中に居ない**"
     "——**それが参照集合から `男.identity` が外れている理由である**（記録のヘッダ）。"
     "⚠️ **証人が画の中に居ないことは、この形式の違反ではない**（`s02` の同じ読みを見る）。",
     "⚠️ **この牛は、この作品のどのショットにも現れない。****この1本にだけ現れる**"
     "（`太陽の牛.negative` の逐語:「**no cattle in any other scene of this work — the herd appears here and nowhere else**」）。",
     "⚠️ **この場所の光は星だけである**（`ledger.locations.沈んだ場所.states.夜` の註:"
     "「光源は星だけである。岸も舟も無いので、明るいものは何も無い」）。**ゆえにこの1本に、日の光も、"
     "夜明けの光も、火も無い。****牛の白と淡い金が、この画で唯一明るいものである。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, photographed as a film: **the surface is the whole of the frame** — no shore, no "
     "land, no landmark, no raft, no wreckage, nothing floating. Low long swell with no white water. "
     "⚠️ **The herd stands at the water's edge of the frame's own water** — seven or eight head, white and "
     "pale gold, heavy-horned, small against the sea. ⚠️ **No made thing is in this frame** — no vessel, "
     "no rope, no tool, no fire. **No marble, no columns, no architecture of any later age.**",
   "Color Language":
     "A narrow, graded palette — black water with one broken path of reflected starlight across it, and "
     "**the herd's white and pale gold the only lit thing in the frame.** ⚠️ **The light does not come "
     "from anywhere in the frame** — it is the stars and their reflection, and it is the same from the "
     "first frame to the last. ⚠️ **The shot has no second light and no warm source.**",
   "Texture":
     "Still black water, fine-grained and broken, carrying one path of reflected starlight; the herd's "
     "coat pale and dry, ribs showing under it; heavy horns with a dull sheen; night air with no haze and "
     "no spray. ⚠️ **No skin and no cloth are in this frame, and nothing in it is wet shore.** Film grain "
     "present and even.",
   "Rendering":
     "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, a gentle flare where "
     "the light is in frame. **Not a photograph's stillness: a film frame, with a real lens's fall-off at "
     "the edges.** No illustration, no CGI look, no cartoon color.",
   "Visual Density": "Low, and **rising once** — the frame is empty for the first three seconds and the "
                     "herd is the only thing that ever enters it. **Nothing in the frame competes with the "
                     "herd:** the water is ground and the light is the only other event.",
   "Time": "`夜` — the night of the bridge, on the same water as `海`. ⚠️ **This place has no before and "
           "no after**（`沈んだ場所.states.夜` の逐語:「この場所には、前後が無い。」）. **The work does not "
           "fix a date**, and this is a memory rather than a record.",
   "Atmosphere": "The moment a memory holds on to — **the thing itself still standing, before anything "
                 "happened to it.**",
 }),

 "subjects": [
   {"name": "nobody",
    "ref": "**この1本に、人物は一人も居ない。** 顔も、立ち姿も、肩も、遠景の点も、写らない。"
           "⛔ **牛のそばに人は置かない**（`太陽の牛.negative` の逐語:「**no person with the herd, no herder, "
           "no weapon near them**」）。⚠️ **そしてこの1本の記憶の持ち主も、この記憶の中に居ない**"
           "——**参照集合が `男.identity` を引かない理由が、それである。**",
    "appearance": "**無い。** ⚠️ **この1本の主題は牛の群れであり、人はその前にも後ろにも居ない。**",
    "behavior": "**無い。** ⚠️ **動くのは水面と光だけである。**",
    "continuity": "⚠️ **人を一人も入れないこと。****一人が入れば、この1本は「あの者たち」の画になる**"
                  "——**歌が名指した者たちを、この1本は写さない。****写さないことが、この1本の内容である。**",
    "notes": ["⚠️ **`Negative Prompt` はこの経路では床にならない**（§18 の前書き）。**ゆえにこれは肯定形で負う** "
              "— §16 `MUST NOT` と、`Master Prompt` 自身の散文が負う。",
              "⚠️ **弱い守りである。記録として書く。** ⚠️ **そしてこの1本では、牛のそばに人を置くことが、"
              "この作品でいちばん起きやすい事故である**——**家畜の画には、生成器が牧者を足す。**"]},
   {"name": "太陽の牛",
    "ref": "**この1本の主題である。** ⚠️ **参照は `ledger.props.太陽の牛` の `appearance` と `negative` である**"
           "——**この作品に参照画像は無い**（裁定②）ので、**この英文が牛の同一性を運ぶ。**"
           "⛔ **この牛は、この1本にしか現れない。**",
    "appearance": "**水際に立つ牛である。** 七、八頭——**白と淡い金、重い角、動かない、水の方を向いている。**"
                  "**肋骨が見える。****草を食べず、遠ざかりもしない。** 群れは距離を置いて立ち、"
                  "**一つの枠に群れ全体が入り、海を背に小さく見える。**⚠️ **そのそばに人は見えない**"
                  "（逐語:「**and no person is visible with them**」）。",
    "behavior": "**牛は動かない。****動くのは水面と、その上の光だけである。** "
                "⚠️ **この1本の中で、牛は一歩も歩かず、草を食べず、こちらを見ない。**"
                "**立っていることが、この1本の出来事である。**",
    "continuity": "**Must preserve** — **頭数と、白と淡い金の色、重い角、肋骨の見え方、そして「動かないこと」。**"
                  "⚠️ **滑らないものは牛である**（§8 の `CONSTANT`）。"
                  "**May change** — 光の当たる面、脚の間を抜ける光の幅、群れの前の水の形、"
                  "そしてカメラが流れるあいだの、画の中の位置。",
    "notes": ["⚠️ **`remembered-world` の5つは、この1本ではこう当てはめられる**（§8 の `Temporal Density` を見る）"
              "——`WITNESS`＝`男`（**彼の記憶であり、彼はこの記憶の中に居ない**）／`DRIFT`＝**低い光**／"
              "`CONSTANT`＝**牛**／`EXACT`＝**頭数と形**／`DURATION`＝`11.649s`。",
              "⛔ **屠る場面は、この1本に一度も来ない。****牛は立ったままである。**"
              "**歌が歌ったことは、耳が受け取り、目は受け取らない**——**それがこの1本の設計である**"
              "（`props.太陽の牛` の註）。",
              "⚠️ **牛はこの作品のどのショットにも現れない**（`props.太陽の牛.negative` の3行目）。"
              "**ゆえにこの1本は、捨てることを前提にした1本である**——**同じ牛を、別のショットで作り直さない。**"]},
 ],

 "environment": {
   "location": "`沈んだ場所` — **記憶の中の海であり、`海` と同じ水である。** ⚠️ **この作品は、ここで島の外へ出る**"
               "——**岸も、洞口も、舟の置き場も、この1本には無い。**"
               "⛔ **違うのは一つだけである**（逐語:「Its only difference is that the raft is not in it.」）"
               "——**舟が居ない。**",
   "elements": "夜の水面と、**星を受けた一本の反射の道**、そして**水際に立つ牛の群れ**——"
               "**七、八頭、白と淡い金、重い角、肋骨が見える、動かない。**"
               "⚠️ **破片を一つも置かない** — 漂流物も、櫂も、帆も、布も、血も、無い。"
               "**面は水だけである。**",
   "behavior": "**水面は同じ向きへ、同じ速さで動きつづける。****星の反射の道が、その上で細かく割れては戻る。**"
               "⚠️ **牛は動かない** ——**この1本の環境は、牛に一度も反応しない。**"
               "⚠️ **場所は人に反応しない** ——**この1本に人は居ない。**",
 },

 "objects": [
   "**牛の群れ** — **この1本の唯一の主題である。** 水際に立ち、動かない。"
   "⚠️ **この作品の小道具4つのうち、この1本に来るのはこれ一つである。**",
   "**星の反射の道**, one broken path of starlight on the black water — "
   "**この1本で動くのはこれと水面だけである。**",
   "**低い光** — **牛の脚の間を抜ける。** ⚠️ **光源は星であり、火でも朝でもない**"
   "（`沈んだ場所.states.夜` の註:「光源は星だけである」）。",
   "⚠️ **この作品の小道具は4つだけであり**（`ledger.props`）、**この1本に来るのは `太陽の牛` ひとつである**"
   "——舟・帆・斧は、**この記憶の中に無い。****舟は、この水に居ないことになっている。**",
 ],

 "ref_character": "**この1本に人物は一人も居ない**——**ゆえに人物に添付しない。** `男` も `女神` も、"
                  "**この1本には四つの姿のどれとしても現れない。** ⚠️ **参照集合が挙げているのは "
                  "`男.negatives`・`沈んだ場所`・`沈んだ場所.geography`・`沈んだ場所.states.夜`・`太陽の牛`・"
                  "`太陽の牛.appearance`・`太陽の牛.negative` の7鍵である。** "
                  "⛔ **`男.identity` は、この7鍵の中に無い**——**彼はこの記憶の中に居ない**（記録のヘッダ）。"
                  "⚠️ **それでも `男.negatives` は在る**——**彼の禁制は、この1本でも掛かる。**",

 "ref_extra": [
   "⚠️ **形式カード `remembered-world` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; what "
   "follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §6 のこの一行と、§16 に運んだカード自身の禁制である。**",
   "⚠️ **カードは「何を免除するかを名乗れ」と要求する**（逐語:「The specification must say which elements "
   "are exempt — and must not exempt everything, because a frame where nothing is exact is not a memory, "
   "it is noise.」）。**この1本の免除は §8 と §15 が名乗る**——**免除するのは光だけであって、"
   "牛でも、頭数でも、場所でも、時刻でもない。**",
 ],

 "narrative": {
   "core": "**牛の群れが、水際に立っている** — 歌は屠ったと歌い、画面は屠る前を写す。",
   "beginning": "**空の海。****何も無い。** 面は水だけで、明るいものは一つも無い。",
   "turn": "**牛の群れが現れる。**水際に、白と淡い金。**動かない。**",
   "peak": "**光が脚の間を抜ける。**牛は立ったままである。",
   "pull": "⚠️ **牛が立ったままであることが、切れ目のコマである。****ここから 1.649秒、歌は無い**"
           "——**歌が終わったあとも、牛は同じところに立っている。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last four and a half seconds.** 最初の3秒は**空の海**に払われ、"
            "次の4秒は**牛が現れること**に払われ、**最後の4.648秒がこの1本の出来事である**——"
            "**光が脚の間を抜け、牛が立ったままである。** ⚠️ **この最後の4.648秒のうち 1.649秒は、"
            "歌の無い間である**（215.053–216.702）——**その間、画面が全部を負う。**"
            "⚠️ **`held` を1つも使わない。****止まるのは牛であって、画面ではない**"
            "（`shot-record.schema.json` の `motion`）——**水面と光は最後のコマまで動いている。**"
            "**ゆえに末尾のビートは `dense` である。** "
            "⚠️ **`remembered-world` の5つの変数（形式カードの逐語）**: `WITNESS`＝**`男` である**"
            "（**この記憶は彼のものであり、彼はこの記憶の中に居ない**——§6）／ `DRIFT`＝**低い光である**"
            "（**牛の脚の間を抜け、そして戻る。****滑るのは光だけである**）／ `CONSTANT`＝**牛である**"
            "（**一歩も動かず、頭数も形も変わらない**）／ `EXACT`＝**頭数と形である**"
            "（七、八頭、白と淡い金、重い角、肋骨が見える——**この1本が確かなのはここである**）／ "
            "`DURATION`＝`11.649s`。",

 "actions": [
   ("ACT_EMPTY", "切り出しは空の海である。", "**海は空であり、何も無い。****明るいものは一つも無い。**"),
   ("ACT_APPEAR", "面は水だけで、水際に立つものは無い。",
    "**牛の群れが現れる**——**水際に、白と淡い金、七、八頭。****動かない。**"),
   ("ACT_CROSS", "光は水面の道の上にある。",
    "**光が牛の脚の間を抜ける**——**水面の反射が低く、牛の下を通る。**"),
   ("ACT_STAY", "歌はまだ鳴っている。",
    "**牛が立ったままである****——歌が終わり、1.649秒が過ぎても、牛は同じところに立っている。**"
    "**その立ったままのコマが、この1本の切れ目である。**"),
 ],

 "camera": {
   "language": "Third person, **low, at the water's own surface** — the lens close to the waterline so that "
               "the herd stands above the frame's centre and the sea fills everything behind it. "
               "⚠️ **岸の高さでも、舟の高さでもない**——**この1本の地面は、水面そのものである。**",
   "events": "One event only. `0-7.001s` — **a slow lateral travel to the left along the front of the herd, "
             "at a rate that does not change**; then `7.001-11.649s` — **the same travel continues without "
             "stopping, and it is still moving on the last frame of the take.** ⚠️ **動機は「数えること」である**"
             "——**カメラは群れの前を左へ流れ、牛の数を数えていく。** ⚠️ **止まらないし、切らない。**"
             "⚠️ **牛の後ろへ回らない**——**この1本は群れの前から動かない。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** "
               "— a low weighted lateral travel with the low frequency of a rig that has mass, and it does "
               "not wobble. ⚠️ **動機の無い移動をしない。** ⚠️ **水面すれすれの高さを保つ**"
               "——**持ち上がらない。****持ち上がれば、この1本は牛を見下ろす画になる。**"
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, and "
               "**no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、牛である——そして牛は動かない。** "
              "**立っていることが主題の運動である。** ⚠️ **動くのは水面と光だけである。**",
   "object": "**光が脚の間を抜ける** — 低い反射の道が、牛の下を通って、そして戻る"
             "（**滑って、戻るのがこの1本の `DRIFT` である**）。"
             "⚠️ **牛は一歩も動かない。****草を食べず、遠ざからず、こちらを見ない。**",
   "environment": "**水面は同じ向きへ、同じ速さで動きつづける。****星の反射の道が細かく割れては戻る。**"
                  "⚠️ **風はこの1本の音にも画にも無い**——**面は水だけである**（§14）。",
   "weight": "**水は重く、光は重さを持たない。****そして牛は重い**——"
             "**牛が動かないので、この1本の重さは、立っていることの重さである。**",
   "inertia": "**水面は行き過ぎてから戻る。****反射の道は、割れたあと少しだけ遅れて戻る。**"
              "⚠️ **牛は慣性を持たない**——**動かないからである。**"
              "**何も瞬間には戻らない。**",
   "acceleration": "**加速しない。** ⚠️ **カメラの流れも、水面の周期も、一定である**"
                   "——**この1本に見せ場の加速は一つも無い。** ⚠️ **牛は急に現れない**"
                   "——**現れたあとは、最後のコマまで同じところに立っている。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この11.649秒に、止まったフレームは一つも無い**"
               "——**牛が動かないあいだも、水面と反射とカメラが動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**牛が現れることは、衝撃ではない。**"
             "⛔ **屠ることも、刃も、血も、この1本には一度も来ない。**",
 },

 "emotion": {
   "arc": "**何も無い海に、立っているものが現れる。** そして**それが「まだ何も起きていない」に見えること**が、"
          "この1本の感情である。⚠️ **屠る場面を写さないのに、屠られたことが伝わる**"
          "——**伝えるのは画面ではなく、耳である。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****牛が水際に立っていることである。**"
             "**そしてこの1本は、その牛に名前を与えないし、数え上げた数を言わない。**"
             "⛔ **歌が歌ったことは、この1本では起きない**——**起きないことが、この1本の返事である。**",
 },

 "lighting": {
   "base": "The stars and their reflection on the water — **and nothing else.** ⚠️ **この1本の光源は一つであり、"
           "それは星である**（`沈んだ場所.states.夜` の註:「光源は星だけである。岸も舟も無いので、"
           "明るいものは何も無い——水面だけが、星を受けて黒く光る」）。"
           "⚠️ **火を出さない。****日の光も、夜明けの光も出さない**——**この記憶は夜の中にある。**"
           "⚠️ **牛を別に照らさない**——**牛の白と淡い金は、同じ星の光の中にある。**",
   "events": "**One, and it is low.** 7.001秒から、**星を受けた反射の道が低く伸びて、牛の脚の間を抜けていく。**"
             "⚠️ **光源は動かない**——**様式カードの逐語:「The grade holds for the whole shot — a colour "
             "temperature that swings is a different style.」** ⚠️ **この1本の色は、最初のコマと最後のコマで"
             "同じである**——**変わるのは、光の位置ではなく、牛の下を通る光の幅である。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水の音だけである。****低い波が同じ間隔で寄せて返る音。** ⚠️ **この1本に人の音は一つも無い。**"
          "⚠️ **牛は音を立てない**——**蹄の音も、息も、鳴き声も無い。**"
          "⚠️ **屠る音は無い**——**この1本に屠る場面が無いからである。**",
   "music": K.NO_MUSIC + " ⚠️ **この1本の上では `l23`「あの者たちは太陽の牛を屠った」が歌われている**"
            "——**ゆえに生成された音床は、同じ11.649秒に二つの音楽を置くことになる。**",
   "environment": "夜の海。**水、そして水だけである。** ⚠️ **岸の音も、鳥の音も、舟の音も無い**"
                  "——**この場所には、水以外の何も無い**（`沈んだ場所.base` の逐語:「Nothing is visible in "
                  "the water and nothing is visible on it.」）。",
 },

 "continuity": {
   "identity": "⚠️ **この1本に人物が居ないので、人物の同一性は掛からない。** "
               "**掛かるのは牛と場所の同一性である**——**頭数、白と淡い金、重い角、肋骨の見え方、"
               "そして「動かないこと」**、そして**水だけであること**。"
               "⛔ **`男.identity` はこの1本の参照集合に無い**——**彼はこの記憶の中に居ない**"
               "（記録のヘッダ）。**ゆえに §18 の `Visual Prompt` と `Master Prompt` に、"
               "同一性の塊は貼られていない。**",
   "spatial": "**面は水だけである。****岸も、陸も、舟も、目印も無い**——"
              "**カメラは何によっても向きを定められない**（`沈んだ場所.geography` の逐語）。"
              "**牛は水際に立ち、カメラはその前を左へ流れる。** ⚠️ **この場所には前後が無い**"
              "——**ゆえに「水際」とは、この1本では画面の下端のことである。**",
   "temporal": "夜である。⚠️ **この3本（`s23`・`s24`・`s25`）は同じ記憶の三つの瞬間である**"
               "——**`s23` と `s24` のあいだに、時は経たない。**"
               "⚠️ **画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** ⚠️ **光は星とその反射だけである。**"
             "⚠️ **この1本は `remembered-world` を名乗るので、§15 が免除するものを §8 と §15 が名乗る**"
             "——**免除するのは「光が滑ること」だけであって、牛でも、頭数でも、場所でも、時刻でもない。**"
             "**カードの逐語:「must not exempt everything, because a frame where nothing is exact is not a "
             "memory, it is noise.」****この1本で正確なのは、牛の頭数と形である。**",
   "motion": "Full animation, not limited. **水面が動き、光が滑り、カメラが流れる。** "
             "⚠️ **牛は最後のコマまで同じところに立っている。**"
             "⚠️ **カメラは1回だけ動き、切れ目のコマでもまだ動いている。**",
   "sound": "**水。****音楽なし。言葉なし。** ⚠️ **牛の音は無い。**"
            "⚠️ **この1本の上では主題歌が歌っているが、この1本の中には無い**——**編集で載る。**",
 },

 "must_not": K.must_not_common(has_man=False, goddess_extra=(
     "⛔ **この1本に人は一人も居ない**——**ゆえに女神の禁制もここでは「誰も出さない」として効く。** "
     "**彼女はこの1本に、四つの姿のどれとしても現れない**——**この場所は記憶であり、彼女の場所ではない。** "
     "**声も、温かさも、動く空気も、水面の光も置かない。**")) + [
   "⛔ **No person in this frame at any distance or in any focus** — no herder, no one standing with the "
   "herd, no one at the water's edge, no one in the water, no silhouette on the horizon (逐語, "
   "`太陽の牛.negative`: `no person with the herd, no herder, no weapon near them`).",
   "⛔ **No slaughter, no butchery, no blood, no carcass, no hide, no meat, no fire, no spits** (逐語, "
   "`太陽の牛.negative`). ⚠️ **歌は屠ったと歌う。この1本はそれを写さない。**",
   "**No weapon near the herd** — no knife, no blade, no axe, nothing laid on the ground beside them, and "
   "no hand holding anything (逐語, `太陽の牛.negative`).",
   "⚠️ **No boat, no ship, no hull, no sail, no raft, and no other vessel** — **この水には舟が居ない**"
   "（`沈んだ場所.geography` の逐語:「Its only difference is that the raft is not in it.」）。",
   "⚠️ **No wreckage, no oars, no mast, no floating wood, no cloth, no body in the water** (逐語, "
   "`沈んだ場所.base`). ⚠️ **面は水だけである。**",
   "⚠️ **No sunlight, no dawn light, no moonlight, no firelight** — **この場所の光は星だけである**"
   "（`沈んだ場所.states.夜` の註）。**牛を別に照らす光も無い。**",
   "⚠️ **No drift that destroys the herd's identity** — **牛は滑らない。** **滑るのは光だけである**"
   "（§8 の `DRIFT`）。**頭数も、色も、角の形も、肋骨の見え方も、最後のコマまで同じである。**",
   "⚠️ **この1本に男は居ないが、`男.negatives` は参照集合に在る**（§6）——**彼の禁制はこの1本でも掛かる**"
   "（逐語:「no muscular hero's body, no heroic pose, no heroic lighting」・"
   "「no youthful face, no beardless face, no clean or unlined skin」・"
   "「no armour, no helmet, no greaves, no shield」）。⚠️ **ここでは、それが「牛の群れと一緒に人を置かないこと」"
   "として効く。**",
 ],
 "must": [
   "**牛の群れが、水際に立っている** — そして**立ったままであることが、切れ目のコマである。**",
   "⛔ **屠る場面を一度も写さない** — **牛は立っている。****血も、刃も、死体も無い。**",
   "**この1本に人は一人も居ない** — どの距離にも、どのピントにも。**牛のそばにも、水の中にも。**",
   "⚠️ **牛のそばに牧者を置かない** — 逐語:「**no person with the herd, no herder, no weapon near them**」。",
   "⚠️ **この牛は、この1本にしか現れない** — **同じ群れを、他のどのショットにも置かない。**",
   "**光が脚の間を抜ける** — そして**その光は星の反射である。****火でも、朝でも、月でもない。**",
   "⚠️ **変化は最後のコマで終わる** — **歌が終わったあと 1.649秒、牛は立ったままである。**",
   "⚠️ **水位の音は水だけである** — **牛は鳴かない。****人は何も言わない。**",
 ],
 "prefer": "The herd held small against the sea with the whole group in one frame; the water's surface "
           "fine-grained and broken; **the ribs showing under the pale coat**; the reflection's path low "
           "and passing between the legs; **the black carried without detail** — the one value the grade "
           "does not touch.",
 "allow": "A lens flare where the reflected path crosses the frame; a moderate depth of field that lets "
          "the far water go soft; **a low lateral travel that never turns around the herd and never stops.**",

 "priorities": [
   "⛔ **屠る場面を写さないこと。** **この1本の内容は「まだ起きていない」ことであり、写せば別の1本になる。**",
   "⛔ **牛のそばに人を置かないこと** — **家畜の画に牧者を足すのは、生成器にとって最も自然なことである。**",
   "**牛が水際に立っていること** — そして**立ったままであることが切れ目のコマであること。**",
   "⚠️ **牛の頭数と形が、最後のコマまで滑らないこと** — **滑るのは光だけである。**",
   "**光が星とその反射だけであること** — 日の光も、火も、専用の光源も無い。",
   "⚠️ **`男.identity` を入れないこと** — **彼はこの記憶の中に居ない**（記録のヘッダ）。"
   "**同一性の塊は、この1本の §18 には無い。**",
   "**舟を出さないこと** — **この水に舟は居ない。**",
   "⚠️ **`remembered-world` の5つを満たすこと** — 証人は `男`、滑るのは光、滑らないのは牛、"
   "正確なのは頭数と形、そして**滑った光は戻る。**",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `remembered-world` を名乗るが、その禁制（`no drift that destroys identity`・"
   "`no caption explaining that this is a memory` ほか）は §16 に在って、ここには無い。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "An 11.649-second cinematic take (16:9) of open sea at night, one clip, one continuous take, one change: "
   "**the herd of cattle is standing at the water's edge.** **The song over this shot says the cattle of "
   "the sun were killed; this shot does not show it — it shows them before anything happened to them.** "
   "**There is no person in this frame at any distance and in any focus.**\n\n"
   "0-3.005s: **the sea is empty and there is nothing in it.** The surface is the whole of the frame and "
   "nothing in it is lit.\n"
   "3.005-7.001s: **the herd appears at the water's edge** — seven or eight head, white and pale gold, "
   "heavy-horned, small against the sea, **standing still and facing the water.** Their ribs show. **They "
   "do not graze and they do not move away.**\n"
   "7.001-11.649s: **the low reflected light crosses between their legs**, the herd still standing, **and "
   "the take ends on that frame — the herd has not moved, and the song has already stopped.**\n\n"
   "**The light is the stars and their one broken path on the water, and there is no other source and no "
   "second light: no fire, no torch, no lamp, no dawn and no moon.** **No blood, no wound, no corpse, no "
   "slaughter, no butchery, no carcass, no hide, no meat, and no blade and no weapon near the herd.** "
   "**No person is with the herd and no one is in the water; no boat, no ship, no sail, no raft and no "
   "other vessel is in this frame, and nothing is floating in it.** **This is a bronze-age sea before "
   "classical Greece: no made thing of any later age and no legible text on any surface.** **This is a "
   "Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the herd is standing at the water's edge.)"),

 "visual_scene": (
   "Open sea at night, photographed as a film frame: black water, fine-grained and broken, carrying one "
   "path of reflected starlight that runs low across the surface; the horizon level and unbroken and no "
   "land anywhere in the frame. **At the frame's own waterline, a herd of cattle stands facing the water — "
   "seven or eight head, white and pale gold, heavy-horned, their ribs showing under the pale coat, "
   "standing still and not grazing, the whole group small and together against the sea, and no person "
   "visible with them.** No shore, no landmark, no raft, no wreckage and nothing floating anywhere in the "
   "water."),

 "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones", "still black water broken by one path of reflected starlight"
 ).replace(
   "Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked; ", ""
 ) + (
   " ⚠️ **Nothing in this frame is cloth, skin or shore** — the frame holds water, night air and the herd, "
   "and the herd's pale coat is the only lit surface in it."),

 "motion_prompt": (
   "Full animation, not limited. **The water moves and the herd does not.** The surface runs in one "
   "direction at a rate that does not change, and the broken path of starlight on it splits and comes "
   "back; **from 7.001s the reflected light lies low and crosses between the herd's legs.** **The herd "
   "stands at the water's edge and holds that: not one step, not one turn of the head, no grazing, and "
   "they do not look toward the lens.** **The camera travels slowly to the left along the front of the "
   "herd and does not stop.** No motion blur smears, no stutter, no floaty weightless motion, no static "
   "frames — **the water and the light move in every frame of the take, and the herd is still standing on "
   "the last one.**"),

 "camera_prompt": (
   "Third person, **low, at the water's own surface** — the lens close to the waterline, so that the herd "
   "stands above the frame's centre and the sea fills everything behind it. One event only: **a slow "
   "lateral travel to the left along the front of the herd, at a rate that does not change, still running "
   "on the last frame of the take.** ⚠️ **The move is motivated by counting them** — the camera passes in "
   "front of the herd and counts it. ⚠️ **The style permits a dolly, a crane and a Steadicam, and this "
   "shot spends the dolly** — a low weighted lateral travel with the low frequency of a rig that has mass. "
   "⚠️ **It does not stop and it does not cut, and it does not rise** — lifting would turn this into a "
   "shot that looks down on the herd. No handheld, no whip, no shake, no snap zoom, no rack focus, no "
   "unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water, and only water — long low swell arriving and going "
   "back at one interval.** ⚠️ **There is no human sound in this shot at all, and the herd makes no "
   "sound**: no hooves, no breath, no lowing, no bell. ⚠️ **Nothing else is heard** — no shore, no bird, "
   "no vessel, no oar, and no sound of anything being done."),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (remembered-world) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⛔ **この1本に人物は居ないので、同一性の塊は §18 に入らない**"
                        "——**入るのは牛と場所の記述である。****参照集合の7鍵に `男.identity` は無く"
                        "（記録の測定）、`Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は書かれていない。**"
                        "⚠️ **`男.negatives` だけは集合に在る**——**ゆえに §16 は彼の禁制も運ぶ。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water only, and no sound from the herd ／ no music",
 "unresolved": [
   "⚠️ **光の出所が、記録の中で一つに定まっていない。** `props.太陽の牛.appearance` の逐語は"
   "「Cattle standing at the edge of the sea **in the last of the light**」と言い、"
   "`locations.沈んだ場所.states.夜` の註は「**光源は星だけである**」と言う。"
   "⚠️ **この仕様は、場所と時刻の側（夜・星だけ）を採り、光を「星を受けた水面の低い反射」とした**"
   "——**ゆえに日の光も夜明けの光も、この1本には無い。**"
   "⛔ **どちらが正しいかは、絵を見て著者が決める。**",
   "⚠️ **`WITNESS` の読みが著者に委ねられている。** この形式は「誰の記憶か」を要求する。"
   "**この仕様は `男` とした**（**この場所の記憶を持つのは彼だけであり、`l24` が彼の位置を決めている**）。"
   "⚠️ **彼はこの記憶の中に居ないので、形式カードの「証人は画の中に居ない」という読みを採っている**"
   "（`s02` と同じ読み）。**この読みが正しいかは、著者が見て決める。**",
   "⚠️ **`Visual Meta` から「肌」と「布」と「岸」の句を外した。** この1本には人物も布も岸も無いので、"
   "**その三句をそのまま §18 に置けば、生成器へ「肌と布と濡れた小石を出せ」と言うことになる。**"
   "⚠️ **外した判断は、この仕様の側の判断である**——**残すべきだったかどうかは、著者が見て決める。**",
   "⚠️ **「屠る場面を写していない」ことを、機械は測れない。** **測れるのは、§16 と `Master Prompt` が"
   "血と刃と死体を一度も描写していないことまでである。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **人が入る。** この1本のいちばん高い危険である——**家畜の画には、生成器が牧者を足す。**"
   "禁制は §16 と `Master Prompt` の散文の両方に在る。",
   "⛔ **屠る場面が出る。** ⚠️ **歌がその一行を歌っているので、生成器はその方向へ引かれる。**"
   "**血も、刃も、死体も、この1本には無い。**",
   "**牛が動く。** ⚠️ **歩き、草を食べ、こちらを見れば、この1本は「立っている」の1本ではなくなる。**",
   "**牛が水に入る。** ⚠️ **水際に立つことが指定であり、入れば別の画になる。**",
   "**舟が浮かぶ。** ⚠️ **この作品は全ショットで舟と船を禁じている**——そしてこの水には"
   "**そもそも舟が居ないことになっている。**",
   "**光が太陽になる。** ⚠️ **この場所の時刻は夜である**——**日の光が入れば、この1本は別の時刻の1本になる。**",
   "**牛の形が滑る（drift）。** ⚠️ **参照画像が1枚も無いので、守る道具は英文だけである**（裁定②）。"
   "**滑ってよいのは光だけである。**",
   "**牛がもう一度、別のショットに現れる。** ⚠️ **この群れは、この1本にしか現れない**"
   "（`太陽の牛.negative` の3行目）。",
 ],
}

if __name__ == "__main__":
    print("s23 content OK — keys:", len(C))
