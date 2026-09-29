# -*- coding: utf-8 -*-
"""odyssey-s14 — video-spec — 海 / 夜 / 5.745s. The one line that films the crossing itself."""
import common as K


C = {
 "n": "s14",
 "title": "海を渡る——移動を、速さでなく距離で",
 "duration": "5.745",
 "format": "video-spec",
 "has_man": False,
 "segment": "chorus-1-2",

 "band": [
   "『永遠より遠い』 chorus-1「海」 / 運動 / motion —— 海を渡る——移動を、速さでなく距離で",
   "島の無い海の上を、舟が舳先で波を割って進む——航跡だけが後ろへ伸びて消える。",
   "5.745秒、カメラは舳先の高さで前へ進む——泡が消えるのが、切れ目である。",
   "速さは見せず、着く先も見せない——動くのは舟と海だけである。",
 ],
 "header": """# chorus-1 / motion / 運動 / video-spec
⚠️ **行: `l11` ／ 場所: `海` ／ 時刻: `夜` ／ 尺: 5.745秒。**
⚠️ **形式（`video-spec`）は §6 の `REF_FORMAT` に書く提案である。** ショット記録に `REF_FORMAT` の欄は無い——**形式は仕様の側にある。****ゆえにここに書いた形式は、まだ検査されていない。**
⚠️ **この作品で唯一、移動そのものを写す行である。** 出所: 曲の `l11`「海を渡る」。**この行も3回歌われる**（`l11`／`l20`／`l29`）。
⛔ **`props.舟` の `negative` が、この1本で効く**——「**no boat, no ship, no hull, no keel, no planking**」。⚠️ **詩は筏を詳しく書かない。この作品は書く**——**参照画像が無い以上、文が持たねばならない。** そして**「船」と書けば生成器は船を作る。****作り手のいない船は、この作品では嘘である**（`l14` が木を削っている）。
⚠️ **役は `運動`。** 固有基準は「重さ・慣性・加速・流れ・衝撃・**身体の可読性**・リズム」——**様式の物理で測る。**
⚠️ **この仕様のショット記録は `shots/odyssey-s14.yaml` である。**""",

 "intent": "One continuous take of one change — **移動が、距離として出る。** 最初のコマでは**海だけがあり、舟は画面に無い。** 最後のコマでは**舳先が波を割り、航跡が一度に伸びている**——⚠️ **泡が消えるのが、切れ目のコマである。** ⛔ **速くしない。****着かない。** ⚠️ **水平線は、この5.745秒のあいだ、一度も近くならない。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、移動を速さでなく距離で写す。****速さは、この作品の主題ではない。** "
   "「着いた」は `s18` の側であり、**この1本の仕事は「まだ着かないこと」である**"
   "（`aim` の逐語:「この作品に「冒険」の画は要らない——**要るのは、まだ着かないことである。**」）。"
   "⚠️ **ゆえにこの1本の画には、陸が一つも無い**——**`s13` で岸は枠の外へ出た。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本に返事は無い。****島はもう画面に無い**（`unit` の逐語:「島はもう画面に無い。"
               "海だけがある。」）。**島が応えるのは `s20` である。**",
     "goddess": "⚠️ **この1本に彼女の姿は無い。****四つの姿のどれとしても現れない。** "
                "**この1本の光は星であり**（`ledger.locations.海.states.夜` の逐語）、"
                "**彼女の第四の姿（枠の外の背後から来る水面の光）ではない。** "
                "⚠️ **この1本には歌がある**（`l11`）——**が、それはポストで載る。**",
     "name": "⚠️ **この1本には歌がある**——`l11` である。**名はどこにも無い。****行き先の名も、島の名も。**",
     "bow": "⚠️ **この1本に弓は無い。****あるのは斧に似ていない道具である**——"
            "**実際、この1本の枠に道具は一つも無い**（§7 を見る）。",
     "places": "この1本が置くのは一つ——`海`、**夜である。****陸は無い。** "
               "⚠️ **`海.geography` の逐語:「from the raft the water surrounds the frame on all sides and "
               "no land is visible in any direction** including behind」——**この1本は、その側である。**",
     "japanese": "⚠️ **この1本には歌がある**——`l11`「海を渡る」である。**画面の中の声ではない。**"
                 "**歌はポストで載る。**",
   },
   extra=[
     "⛔ **この1本の筏は、船ではない。** ⚠️ **`props.舟.appearance` の逐語:「a raft and not a boat」**"
     "——**船体も、竜骨も、肋も、甲板張りも無い。** **この1本の画で、そこが読み取れねばならない。**",
     "⛔ **この1本は、まだ着かない。****水平線の高さは、この5.745秒のあいだ変わらない。** "
     "⚠️ **変われば、この1本は「どこかへ着いた」の画になり、`s18` の仕事を先に食う。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, photographed from just above the water at the height of a raft's bow: long low "
     "swells with no white water moving steadily in one direction, the horizon level and unbroken. In the "
     "lower part of the frame, the raft itself — **the bow of a low platform, not a vessel**: twenty-odd "
     "unseasoned barked pine logs lashed with coarse hand-twisted cordage, hewn planks laid across them "
     "and not fastened flush, **no keel, no ribs, no planking, no gunwale, and no raised sail.** "
     "⚠️ **Land is nowhere in this frame** — no island, no coast, no headland. ⚠️ **No marble, no "
     "columns, no architecture of any later age.**",
   "Color Language":
     "A narrow, graded palette — black water, a sky one shade above it, wet pine reading pale and raw "
     "against both, and one white line: the reflected path on the surface, cut by the swell and by the "
     "logs. ⚠️ **Nothing is lit apart from the stars and their reflection** — **the shot has no second "
     "light.**",
   "Texture":
     "Coarse water broken into fine facets; the swell faces smooth and black; **bark still on the logs, "
     "raw hewn faces, and the hand-twisted cordage's uneven surface**; the wake's foam decaying to a thin "
     "line. ⚠️ **No metal, no machined edge, no paint, and no varnished surface anywhere.** "
     "Film grain present and even.",
   "Visual Density":
     "Low and steady — water, horizon, bow, and the wake. ⚠️ **この1本は、遠近の層を一つしか持たない**"
     "——**陸が無いので、奥行きを測るものが水平線しかない。**",
   "Atmosphere": "The hour in which passage is measured by what is left behind and not by what arrives.",
   "Time": "`夜` — the source is the stars and their reflection on the water; **the waves are black and "
           "the reflected path alone is white**（`ledger.locations.海.states.夜` の逐語）。"
           "**`s09`〜`s15` と同じ夜である。**⚠️ **この作品は話を進めない**——"
           "**ゆえにこの夜と、`s16` の夜明けとのあいだに、順序を読まない。**",
 }),

 "subjects": [
   {"name": "舟",
    "ref": "⚠️ **参照は `ledger.props.舟` の `appearance`・`negative` である。****この1本の主題は、"
           "この筏の移動である。**",
    "appearance": "**筏である。****船ではない。** **二十数本の、皮の付いたままの未乾燥の松の丸太を、"
                  "手で縒った粗い縄で縛り**、**その上に、削った板が、面を合わせずに渡してある。** "
                  "**竜骨も、肋も、甲板張りも、欄も、帆柱の台も無い。** **短い支えのある帆柱がある**"
                  "（`舟.appearance` の逐語:「a short stayed mast of trimmed pine」）——"
                  "⚠️ **帆はまだ一本も張られていない**（`舟.negative` の逐語:「no sail already raised on "
                  "the raft before the sail exists」）。**帆は `s17` で初めて張られる。** "
                  "**低く沈み、縁では水に洗われている。****船尾に、縛られた操舵の櫂がある。**",
    "behavior": "**進行方向へ進み、うねりに乗って上下する。****水位線が縁を洗い、泡が縁を伝って後ろへ流れる。** "
                "⚠️ **速くない**——**この1本の移動は、速さではなく、後ろへ伸びる航跡の長さで出る。**",
    "continuity": "**Must preserve** — 丸太と縄の手作りであること、低いこと、竜骨・肋・甲板張り・欄が無いこと、"
                  "縁が水に洗われること、そして**帆が張られていないこと。** "
                  "**May change** — 舳先の画面の中の高さ、水の被り方、丸太の濡れ方。",
    "notes": ["⛔ **この1本の掟は `props.舟.negative` である**——「**no boat, no ship, no hull, no keel, "
              "no planking**」。⚠️ **この1本を「舟」と訳して渡せば、生成器は船体を作る。**"
              "**ゆえにこの仕様は、英語の側で筏を筏として書く**（§18 を見る）。",
              "⚠️ **この1本に帆は無い。****帆は `s17`（`l15`）で布から帆になる**"
              "——**この1本で帆を張れば、作品は順序を飛ばす。**"]},
   {"name": "海",
    "ref": "**この1本の場所である。** ⚠️ **参照は `ledger.locations.海` の `base`・`geography`・"
           "`states.夜` である。**",
    "appearance": "**長く低いうねりであり、白波を立てない。****水平線は一本で、途切れない。** "
                  "**夜であり、波は黒く、水面に一本の道だけが白い**（`海.states.夜`）。"
                  "⚠️ **陸は一つも無い****——どの方向にも。** **帆も、鳥も、他の舟も無い。**",
    "behavior": "**うねりが一方向へ進む。****そして筏の下で持ち上げ、縁で割れる。** "
                "**航跡だけが後ろへ伸び、消える**（`motion.quality` の逐語:「**航跡だけが後ろへ伸び、"
                "消える。**」）。⚠️ **水面のいちばん白いのは、星の反射の道である。**",
    "continuity": "**Must preserve** — うねりの方向と低さ、白波が無いこと、水平線が水平で途切れないこと、"
                  "波が黒く反射の道だけが白いこと、そして**陸がどこにも無いこと。** "
                  "**May change** — 水面の細かさ、反射の道の幅、航跡の泡の残り方。",
    "notes": ["⚠️ **`海.geography` の逐語:「the surface broken only by the raft's own wake and by weed "
              "passing」**——**この1本では、その二つが両方とも出る。**"
              "**浮いている草が、水面を横切って流れて行く。**",
              "⚠️ **水平線の高さが、この1本の時計である。****動かなければ「まだ着かない」が出る。**"]},
   {"name": "人（舵を取る者）",
    "ref": "⚠️ **参照集合は `男.identity` を挙げる。****この1本の筏は、彼が舵を取っている筏である。**",
    "appearance": "⛔ **この1本の枠に入らない。****彼はカメラの後ろに居る。** ⚠️ **カメラは舳先の高さにあり、"
                  "前へ進む**——**舵は船尾にあり、船尾はカメラの後ろにある。** "
                  "**ゆえにこの1本は、彼を一度も写さずに、彼の居る筏を写す。**",
    "behavior": "**枠の外で舵を取っている。****ゆえに画面の側には、彼の動きが一つだけ残る**"
                "——**舵の効きで舳先の向きがごく僅かに変わる、その変化である。**",
    "continuity": "⛔ **この1本の枠に、彼を出さないこと** — 手も、肩も、後ろ姿も、影も、映り込みも。 "
                  "⚠️ **それでも、この筏を「無人の筏」として置かないこと**（`s21` の註の逐語:"
                  "「**この作品の筏は彼が作ったものであり、空の筏は嘘である。**」）。",
    "notes": ["⛔ **この判断の根拠を書く。** 記録の `unit`・ビート・`motion.subject` は、"
              "**彼を一度も名指さない。** そして **`s18` の記録の逐語:「この作品で初めて、"
              "男が水の上に居る。」**——**曲順で `s18`（`l16`）は、この1本（`l11`）の後である。** "
              "⚠️ **ゆえにこの1本は、彼を水の上に見せない。****しかし筏を空にはできない。** "
              "**§20 に、この読みを書いた。**",
              "⚠️ **この1本は、同一性の塊を §18 に置かない**（`has_man: False`）——**枠に居ない者の錠を"
              "貼れば、居ない者を貼ることになる**（2026-09-29 の裁定①）。**§20 を見る。**"]},
 ],

 "environment": {
   "location": "`海` — **夜である。****陸は無い。** ⚠️ **カメラは舳先の高さで、水面のすぐ上にある。**",
   "elements": "**長く低いうねり**（白波は無い）、**途切れない水平線**、**一本の反射の道**、"
               "**流れて行く浮いた草**、**航跡の細い泡の線。** "
               "⚠️ **陸も、島も、岬も、水に立つ岩も無い。****月も無い。**",
   "behavior": "**うねりが一方向へ進む。****筏が持ち上げられ、落ち、縁で水を割る。** "
               "**航跡が後ろへ伸びては消える。** ⚠️ **水平線は動かない。** "
               "⚠️ **海は彼に反応しない**（`s21` の註と同じ規則）——**応えるのは `s20` の島だけである。**",
 },

 "objects": [
   "⛔ **この1本の枠に、道具は一つも無い。****斧も、弓も、櫂以外の何も無い。** "
   "⚠️ **操舵の櫂は船尾にあり、船尾はカメラの後ろである**（§3 を見る）。",
   "**筏の縁と、渡した板** — ⚠️ **この1本の下端に、舳先として入る。** "
   "**濡れて、生の木の色をしている。**",
   "**航跡** — ⚠️ **物ではない。****この1本の時計であり、距離そのものである。**",
   "**浮いた草** — **水面を横切って流れて行く。** ⚠️ **`海.base` の逐語:「the surface broken only by "
   "the raft's own wake **and by weed passing**」。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****そしてこの1本の枠に、彼は居ない**"
                  "（**舵を取りに船尾へ居る。****§20 を見る**）。"
                  "`女神` — ⛔ **この1本に添付しない。****彼女は四つの姿のどれとしても現れない。**"
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.夜`・`舟`・`舟.appearance`・`舟.negative` の8鍵である。",
 "ref_extra": [
   "- ⚠️ **形式カード `video-spec` の文法は、この作品の下敷きそのものである**"
   "——**他の形式はどれも「`video-spec` に文法を1つ足したもの」である**"
   "（`impossible-camera` の逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as "
   "that card requires; what follows is only what this grammar adds to it.」）。"
   "**ゆえに §1–20 の骨格は `s01` と同じであり、この1本はそれに何も足さない。**",
   "- ⚠️ **形式カード `video-spec` の6つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `SUBJECT`＝the arc — **「移動そのものを、距離で写す」ことである。**"
   "**カメラは舳先の高さにあり、前へ進む**（`motion.quality` の逐語:「カメラは舟の舳先の高さで、"
   "前へ進む。」）。",
   "  - `DURATION`＝clip length (**the model decides the duration**) — ⚠️ **この作品の尺は、曲から来る**"
   "（`bible.song.lines[].at` の差）。**この1本は `5.745s` である。**",
   "  - `ASPECT`＝aspect ratio — **`16:9`**（裁定④。§1 の4定数が固定する）。",
   "  - `BEATS`＝the beat list with second ranges — **3つであり、明示的に不等である**"
   "（`0-1.499s` transition ／ `1.499-3.499s` sparse ／ `3.499-5.745s` dense）。§8 を見る。",
   "  - `CORE`＝the beat that gets the largest share — **最後のビートである**（`3.499-5.745s`、2.246秒）。"
   "⚠️ **舳先が波を割り、航跡が一度に伸びるのがそこである。**",
   "  - `HOOK`＝the note the clip ends on — ⚠️ **泡が消えるコマである。**"
   "**説明のビートをそのあとに足さない**（カードの逐語:「End on the note, not after it.」）"
   "——**この1本は、航跡の泡が消えたコマで終わる。**",
   "- ⚠️ **カードの逐語:「A digest that gives every beat equal time is the video equivalent of "
   "cramming. **Uneven duration is the composition.**」**——この1本の配分は §8 に在る。**",
 ],

 "narrative": {
   "core": "**渡っている** — 着かないことが、この1本の出来事である。",
   "beginning": "**海だけがある。****舟の舳先が画面の下端に入る。**",
   "turn": "**舟が上下する。** 航跡が後ろへ伸びる。",
   "peak": "**舳先が波を割る。** 航跡が一度に伸びる。",
   "pull": "⚠️ **泡が消えるのが、切れ目のコマである。** **水平線は、5.745秒のあいだ、一度も近くならない。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.246秒.** 最初の1.499秒は**海だけの画に舳先が入ること**に"
            "払われ、次の2.000秒は**舟がうねりに乗ること**に払われ、**最後の2.246秒がこの1本の出来事である**"
            "——**舳先が波を割り、航跡が一度に伸びて、泡が消える。** ⚠️ **`held` を1つも使わない。** "
            "⛔ **速くしない。****一つずつ起きる**——**17秒で木が筏になる `s16` と、同じ呼吸である。**",

 "actions": [
   ("ACT_SEA", "海だけがある。**舟は画面に無い。**",
    "**舳先が画面の下端に入る**——**うねりが筏を持ち上げる。**"),
   ("ACT_RISE", "舳先が下端にある。",
    "**舟が上下し、航跡が後ろへ伸びる。**"),
   ("ACT_BREAK", "航跡が伸びている。",
    "**舳先が波を割る**——**航跡が一度に伸びる。**"),
   ("ACT_FADE", "航跡が長い。",
    "**泡が消えるのが、切れ目のコマである**——**水平線は動いていない。**"),
 ],

 "camera": {
   "language": "Third person, **at the height of the bow, just above the water, moving forward with the "
               "raft.** ⚠️ **この高さは、この作品では `s21` の「在りえない高さ」ではない**"
               "——**`s21` の註の逐語:「`s14` は舳先の高さであり、この1本は在りえない高さである。」**",
   "events": "One event only. `0-1.499s` — **the sea alone, and then the bow enters the lower edge of "
             "the frame as the swell lifts the raft**; then `1.499-3.499s` — **the raft rides the swells "
             "up and down and the wake begins to run back**; then `3.499-5.745s` — **the bow breaks the "
             "water, the wake lengthens at once, and the foam goes.** "
             "⚠️ **カメラは、この1本のあいだ、一様に前へ進む。**"
             "⚠️ **動機は「移動すること」そのものである**——**追うものも、寄るものも無い。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends none of them** "
               "—— ⚠️ **この1本の移動は、水の高さを保ったままの前進である。**"
               "**前進は一様であり、重さを持つ。** **No crane. No dolly. No Steadicam** — "
               "**ゆえにこの1本は、舳先の高さを一度も離れない。** **No handheld, no whip, no shake, "
               "no snap zoom, no rack focus, no unnatural rotation, and no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、前へ進む筏である。****舳先が水を割り、縁が水に洗われ、"
              "航跡が後ろへ伸びる。** ⚠️ **速さは出さない**——**出るのは距離である。**",
   "object": "**動く物は、筏の一部と、水面の草だけである。** ⚠️ **この1本に道具は無い。**",
   "environment": "**うねりが一方向へ進み、白波を立てない。****水面の草が横切って流れて行く。** "
                  "**水平線は動かない。** ⚠️ **この二つが同時であることが、この1本の「距離」である**"
                  "——**近い面は速く流れ、遠い線は止まっている。**",
   "weight": "**筏の重さは、低さと、水の被りで出る。** **丸太は沈み、縁は洗われる。** "
             "⚠️ **軽く跳ねる船ではない。**",
   "inertia": "**一度乗ったうねりは、次のうねりまで抜けない。****航跡は、舳先が去ったあとも残る。** "
              "⚠️ **泡はすぐには消えない**——**消えるのは最後のコマである。**",
   "acceleration": "**加速しない。****うねりも、前進も、航跡の伸びも、一様である。** "
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この5.745秒の全コマで、"
               "水面は動いている。**",
   "impact": "**静かなものだけである。****舳先が波を割るのは、衝撃ではなく、重さである。** "
             "⚠️ **白波も、飛沫も、この1本には無い。**",
 },

 "emotion": {
   "arc": "**渡っている。****それは、劇的でない時間である。** ⚠️ **この1本の感情は、"
          "「着かないこと」の側にある**——**`aim` の逐語:「この作品に「冒険」の画は要らない」。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****舳先が水を割ることである。** "
             "**誰も写さないのに、進んでいることだけが残る。**",
 },

 "lighting": {
   "base": "**夜である。****光源は星と、その水面の反射だけである。****波は黒く、反射の道だけが白い**"
           "（`ledger.locations.海.states.夜` の逐語）。⚠️ **月も、火も、灯も無い。** "
           "**生の木だけが、水面より一段明るい。**",
   "events": "**One, and it runs the whole shot.** **反射の道が、うねりと筏で細かく割れ続ける。** "
             "⚠️ **光源は動かない。** ⚠️ **様式カードの逐語:「The grade holds for the whole shot — "
             "a colour temperature that swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水が舳先と縁に当たる音。****縄と木が軋む音。****航跡が後ろで崩れる音。****弱い風。** "
          "⚠️ **この1本に人の音は一つも無い**——**舵を取る者の音も、息も、掛け声も無い。**",
   "music": K.NO_MUSIC + " ⚠️ **主題歌はこの1本のあいだ鳴っている**（`l11`）——**が、"
            "この1本の中には無い。****編集で載る。**",
   "environment": "夜の外海。**水、木、そして遠さ。** ⚠️ **鳥の声も、他の船の音も無い**"
                  "（`海.base` の逐語:「No land, no sail, no bird, no other vessel.」）。",
 },

 "continuity": {
   "identity": "⚠️ **この1本に人が一人も居ないので、人物の同一性は掛からない。** "
               "**掛かるのは筏と海の同一性である**——**丸太と手縒りの縄、低さ、竜骨・肋・甲板張り・"
               "欄が無いこと、そして帆がまだ張られていないこと。** "
               "⛔ **`男.identity` は参照集合に在るが（§6）、この1本は同一性の塊を §18 に貼らない**"
               "——**舵を取る者はカメラの後ろに居る**（2026-09-29 の裁定①。§20 を見る）。",
   "spatial": "**カメラは舳先の高さにあり、水の上である。** ⚠️ **水際の線と水平線は、この作品の"
              "どの岸の画と同じものである**（`海.geography` の逐語:「The same waterline and the same "
              "horizon appear in both, so that the two views are demonstrably one sea.」）"
              "——**ゆえにこの1本は、岸から見た海と同じ一つの海である。** "
              "⚠️ **この1本は `video-spec` を名乗り、この形式は §15 から何も免除しない**"
              "——**免除を名乗るのは、`coexisting-realities` を名乗る4本だけである。**"
              "**この1本の場所と時刻は、台帳の `海`／`夜` のままである。**",
   "temporal": "**夜である。****`s09`〜`s15` と同じ夜である。** ⚠️ **この作品は話を進めない**"
               "（§2 の逐語:「the work does not advance a story」）——**画の中に日付を与えるものは"
               "何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **この1本の光は星とその反射だけである。**",
   "motion": "Full animation, not limited. **水面が流れ、筏が上下し、舳先が水を割り、航跡が伸びる。** "
             "⚠️ **カメラは一様に前へ進み、止まらない。**",
   "sound": "**水、木、縄、風。****音楽なし。言葉なし。**",
 },

 "must_not": K.must_not_common(has_man=False, goddess_extra=(
     "⚠️ **この1本の彼女は、四つの姿のどれとしても現れない。** **ここにあるのは、夜の海と筏だけである。** "
     "⚠️ **海を女の形にしないこと**（`characters.女神.negatives` の逐語:「no visible body, no hands, "
     "no feet, no arms, no silhouette with a readable outline」）。")) + [
   "**No person in frame at any moment** — **the frame holds the sea, the bow and the wake; whoever is "
   "steering is aft of the camera and is never seen** — no hands, no shoulders, no back, no silhouette, "
   "no figure at any distance, and no shadow or reflection of a person anywhere. "
   "⚠️ **`s18` の記録の逐語:「この作品で初めて、男が水の上に居る。」**",
   "**No boat, no ship, no hull, and above all no keel, no ribs, no planking, no gunwale and no deck** "
   "——⚠️ **`props.舟.negative` の逐語であり、この1本でいちばん効く禁制である。**",
   "**No sail, and no cloth of any kind on the raft**（`舟.negative` の逐語:「no sail already raised on "
   "the raft before the sail exists」——**帆は `s17` で初めて張られる**）。",
   "**No metal fastening, no nail, no rope that is not hand-twisted**（`舟.negative` の逐語）。",
   "**No land of any kind** — no island, no coast, no headland, no rock standing in the water, "
   "**and no land behind the camera either**（`海.geography` の逐語）。",
   "**No moon, no torch, no lamp, and no second light on the water** — **この夜の光は星と、その反射だけである**"
   "（`海.states.夜` の逐語）。",
   "**No white water, no breaking crest, no spray, and no foam except the raft's own wake**"
   "（`海.base` の逐語:「Long low swells with no white water」）。",
   "**No bird and no other vessel**（`海.base` の逐語）。",
   "**No oar, no pole and no tool in frame** — ⚠️ **操舵の櫂は船尾にあり、船尾はカメラの後ろである。**",
   "**No cut to a second setup.** ⚠️ **この1本は1つの画である。**",
   "⚠️ **この1本の筏は、この禁制の対象ではない。****画の中の筏は、船ではない**（`props.舟.appearance` の逐語:「**a raft and not a boat**」）。**禁じられているのは船体・竜骨・甲板張り・欄であり、この1本の丸太と縄ではない。**",
   "⚠️ **この1本に男は居ないが、`男.negatives` は参照集合に在る**（§6）——**彼の禁制はこの1本でも"
   "掛かる**（逐語:「no muscular hero's body, no heroic pose, no heroic lighting」・"
   "「no youthful face, no beardless face, no clean or unlined skin」・「no armour, no helmet, "
   "no greaves, no shield」）。⚠️ **ここでは、それが「手も、肩も、後ろ姿も入れないこと」として効く。**",
 ],

 "must": [
   "**移動が距離として出る** — **航跡が後ろへ伸び、泡が消えるのが、切れ目のコマである。**",
   "**It is a raft and not a boat** — ⚠️ **丸太、手縒りの縄、低さ、縁が水に洗われること。**",
   "⚠️ **同一性の塊を §18 に貼らないこと** — **枠に居ない者の錠を貼らないためである**"
   "（`has_man: False`。2026-09-29 の裁定①）。**§20 を見る。**",
   "⛔ **人を一人も枠に入れない** — **舵を取る者はカメラの後ろである**（§20 を見る）。",
   "⚠️ **水平線が一度も近くならないこと** — **着かないことが、この1本の仕事である。**",
   "⚠️ **帆がまだ張られていないこと。****帆は `s17` の仕事である。**",
   "**星の光だけであること** — **月も、二つ目の光も無い。**",
   "⚠️ **変化は最後のコマで終わる** — **泡が消えたコマで、この1本は終わる。**",
 ],

 "prefer": "The logs kept raw and barked and the cordage visibly hand-twisted; the raft sitting low, "
           "awash at the edges; the wake growing longer rather than the water moving faster; "
           "**weed crossing the frame as the second thing that breaks the surface.**",
 "allow": "A lens flare where the light crosses the frame; a moderate depth of field that lets the far "
          "water go soft; **the bow entering and leaving the lower edge of the frame as the swell "
          "carries it.**",

 "priorities": [
   "**移動が距離として出ること** — **泡が消えるコマで終わること。** **この1本の切れ目はそれである。**",
   "⛔ **筏であって船でないこと** — **竜骨も、肋も、甲板張りも、欄も無い。** **帆も無い。**",
   "⛔ **水平線が近くならないこと** — **着けば、この1本は `s18` の仕事を先に食う。**",
   "⛔ **人を一人も枠に入れないこと** — **舵を取る者はカメラの後ろである。**",
   "⚠️ **同一性の塊を §18 に置かないこと** — **枠に居ないためである**（2026-09-29 の裁定①）。",
   "⚠️ **水際の線と水平線が、岸の画と同一であること。**",
   "**星の光だけであること** — **月も、火も、二つ目の光も無い。**",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `video-spec` を名乗る**——**この形式の禁制（`no uniform pacing`・"
   "`no equal-length beats`・`no static slideshow of stills` ほか）は §16 の床に在り、"
   "**カード自身の `Negative` も §16 の側から届く。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 5.745-second cinematic take (16:9) of the open sea at night, shot from just above the water at the "
   "height of a raft's bow, moving forward with it, one clip, one continuous take, one change: "
   "**the raft is under way and has not arrived — the wake lengthens, the foam goes, and the horizon has "
   "not come one step closer.** **No land is in this frame at any moment: no island, no coast, no "
   "headland, and no land behind the camera either.**\n\n"
   "**The raft is not an empty one: the man who built it steers it from the stern, which is behind "
   "the camera, and he is not seen at any moment.**\n\n"
   "0-1.499s: **the sea alone, and then the bow comes into the lower edge of the frame as the swell lifts "
   "the raft.**\n"
   "1.499-3.499s: **the raft rides up and down; the wake begins to run back.**\n"
   "3.499-5.745s: **the bow breaks the water and the wake lengthens at once — and the take ends as the "
   "foam goes.**\n\n"
   "**The raft is a raft and not a boat**: twenty-odd unseasoned barked pine logs lashed with coarse "
   "hand-twisted cordage, hewn planks laid across them and not fastened flush, **no keel, no ribs, no "
   "planking, no gunwale, no metal fastening, no nail, and no sail** — only a short stayed mast of "
   "trimmed pine with nothing bent to it. **It sits low and the water washes over its edges.** "
   "**The night's only light is the stars and their single reflected path on the water: the waves are "
   "black and the reflected path alone is white.** **Long low swells with no white water, weed passing "
   "across the frame, and the only foam is the raft's own wake.** **No other vessel, no bird, no moon, "
   "the horizon level and unbroken.** **This is a bronze-age world: no made thing of any later age "
   "stands in this frame, and this raft is hand-built from unseasoned timber.** **This is a Japanese "
   "work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the crossing is shown as distance and not as speed.)"),

 "visual_scene": (
   "Open sea at night, photographed from just above the water at the height of a raft's bow: long low "
   "swells with no white water moving steadily in one direction, the water black and broken into fine "
   "facets, and one reflected path of starlight lying on it in white; the horizon level and unbroken "
   "beyond, and no land anywhere. **In the lower part of the frame, the bow of a raft** — twenty-odd "
   "unseasoned barked pine logs lashed with coarse hand-twisted cordage, hewn planks laid across them "
   "and not fastened flush, **no keel, no ribs, no planking, no gunwale and no sail**, only a short "
   "stayed mast of trimmed pine with nothing bent to it; the logs sit low and the water washes over "
   "them, and **a thin line of wake trails back out of the frame**. **No figure is in the frame at any "
   "distance or in any focus — the man steers from the stern, behind the camera — and no shadow or "
   "reflection of a person falls anywhere in it.** No other vessel, no bird, no moon."),

 "visual_meta": K.VISUAL_META.replace(
   "Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked; ",
   "**no skin and no cloth anywhere in this frame**: ").replace(
   "wet shingle with individual stones",
   "barked raw pine logs and hand-twisted cordage, awash at the edges").replace(
   "warm ochre where the low sun falls",
   "cold white held in the one reflected path on the black water") + (
   " ⚠️ **No person is in this frame at any moment — whoever steers is aft of the camera.** "
   "⚠️ **This is a raft and not a boat**: no hull, no keel, no planking, **and no sail has been bent to "
   "the mast yet**; the only foam is the raft's own wake."),

 "motion_prompt": (
   "Full animation, not limited. **The long low swells move steadily in one direction and do not break.** "
   "**The raft rides them up and down, sits low, and the water washes over its edges.** "
   "**The bow breaks the water and the wake runs back and lengthens — and the foam of it decays, slowly, "
   "until it goes.** **Weed crosses the frame and passes out of it.** **The reflected path of starlight "
   "wavers on the running water and runs unbroken.** **The horizon does not move at all** — "
   "**it is exactly as far away in the last frame as in the first.** No motion blur smears, no stutter, "
   "no floaty weightless motion, no static frames — **the water moves in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **at the height of the bow, just above the water**, moving forward with the raft at an "
   "even rate. One event only: **the bow enters the lower edge of the frame, rides the swells, and "
   "breaks the water as the wake lengthens; the camera never leaves the bow's height.** "
   "⚠️ **The move is motivated by the crossing itself — there is nothing to chase, nothing to approach "
   "and nothing to leave behind.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot "
   "spends none of them** — the move is a forward travel at water level, and it carries a real rig's "
   "even rate. No crane. No dolly. No Steadicam. **Do not rise, do not descend, and do not slow.** "
   "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
   "no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water breaking at the bow and washing along the edges, "
   "cordage and timber creaking under load, the wake collapsing behind, and a little wind** — "
   "**and nothing else, because there is no one in this frame to make a sound.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⛔ **この1本の §18 は人物の同一性を運ばない**"
                        "——**人物がこの枠に居ないためである**（`has_man: False`）"
                        "——**`Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は書かれていない。**"
                        "⚠️ **`男.negatives` は参照集合に在る**——**ゆえに §16 は彼の禁制も運ぶ**（§20 を見る）。",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water ＋ timber ＋ cordage ＋ wind ／ no music",
 "unresolved": [
   "✅ **裁定（2026-09-29）: この1本は人物を枠に置かず、同一性の塊も §18 に貼らない**（`has_man: False`）"
   "——**記録の `unit`・ビート・`motion.subject` が彼を一度も名指さないためである。** "
   "⚠️ **この仕様は裁定の前、彼を船尾（カメラの後ろ）に置き、塊を作品の錠として §18 に置いていた**"
   "——**裁定①が塊を落とした。****ゆえに `{IDENTITY}` は §18 に無い。** "
   "⚠️ **それでも筏は無人ではない**（`s21` の註の逐語:「**この作品の筏は彼が作ったものであり、"
   "空の筏は嘘である。**」）——**この読みは裁定のあとも変わっていない。**",
   "⚠️ **カメラの足場を、記録は書かない。** 参照集合が `舟` を挙げ、`motion.quality` が"
   "「カメラは舟の舳先の高さで、前へ進む」と書くので、**この仕様はカメラを筏の側に置いた**"
   "——**それが筏の上なのか、舳先の外なのかは、記録からは読めない。**"
   "⚠️ **どちらでも、この1本の画は同じである**（下端に舳先、上に水平線）。",
   "⚠️ **この1本に帆柱があるかどうかを、記録は明示しない。** 参照は `舟.appearance`"
   "（帆柱を含む）と `舟.negative`（帆を張るな）の両方を引く。**この仕様は、帆柱を立てたまま、"
   "帆だけを張らない、と読んだ。**",
   "⚠️ **`l11` は3回歌われる**（`l11`／`l20`／`l29`）。**この作品は3本とも役を同じにし、"
   "差分を §6 の形式が持つ**——**この1本は `video-spec` であり、`s21`・`s30` の形式は"
   "この仕様からは読めない。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **船として出る。** ⚠️ **竜骨、肋、甲板張り、欄、金属の留め具**——**一つでも出れば、"
   "この1本はこの作品の嘘になる。**",
   "⛔ **帆が張られる。** ⚠️ **`s17` の仕事を先に食う。**",
   "⛔ **水平線が近くなる、あるいは陸が入る。** ⚠️ **着けば、この1本は `s18` の画になる。**",
   "**速さが出る。** ⚠️ **舳先に白波が立ち、飛沫が上がれば、この1本は「冒険」の画になる**"
   "——**要るのは距離である。**",
   "**舵を取る者が写る。** ⚠️ **手一つでも入れば、`s18` の「初めて」が壊れる。**",
   "**航跡が伸びない。** ⚠️ **距離の手がかりが消えれば、この1本はただの海の画になる。**",
   "**月が光源として入る。** ⚠️ **この夜の光は星である。**",
   "**様式美に寄りすぎる。** ⚠️ **`様式美` は `s15` の役である**"
   "——**この1本は `運動` であり、重さと慣性で測られる。**",
 ],
}

if __name__ == "__main__":
    print("s14 content OK — keys:", len(C))
