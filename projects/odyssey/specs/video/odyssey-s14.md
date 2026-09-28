# Seedance 2.5 Full Specification — 主題歌MV『永遠より遠い』 odyssey-s14「海を渡る——移動を、速さでなく距離で」 / 5.745s

# chorus-1 / motion / 運動 / video-spec
⚠️ **行: `l11` ／ 場所: `海` ／ 時刻: `夜` ／ 尺: 5.745秒。**
⚠️ **形式（`video-spec`）は §6 の `REF_FORMAT` に書く提案である。** ショット記録に `REF_FORMAT` の欄は無い——**形式は仕様の側にある。****ゆえにここに書いた形式は、まだ検査されていない。**
⚠️ **この作品で唯一、移動そのものを写す行である。** 出所: 曲の `l11`「海を渡る」。**この行も3回歌われる**（`l11`／`l20`／`l29`）。
⛔ **`props.舟` の `negative` が、この1本で効く**——「**no boat, no ship, no hull, no keel, no planking**」。⚠️ **詩は筏を詳しく書かない。この作品は書く**——**参照画像が無い以上、文が持たねばならない。** そして**「船」と書けば生成器は船を作る。****作り手のいない船は、この作品では嘘である**（`l14` が木を削っている）。
⚠️ **役は `運動`。** 固有基準は「重さ・慣性・加速・流れ・衝撃・**身体の可読性**・リズム」——**様式の物理で測る。**
⚠️ **この仕様のショット記録は `shots/odyssey-s14.yaml` である。**

---

# 1. VIDEO

- Duration: `5.745s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take of one change — **移動が、距離として出る。** 最初のコマでは**海だけがあり、舟は画面に無い。** 最後のコマでは**舳先が波を割り、航跡が一度に伸びている**——⚠️ **泡が消えるのが、切れ目のコマである。** ⛔ **速くしない。****着かない。** ⚠️ **水平線は、この5.745秒のあいだ、一度も近くならない。**

# 2. WORLD

## World Concept

A bronze-age Mediterranean island shore at the end of the day, and the open sea beyond it. **No place in this work is named aloud.** The island holds a cave and a goddess who lives in it; a man has been on this shore for years and has not been able to leave it. ⚠️ **This is a theme-song music video:** one song of 299.920 seconds, thirty-four shots, no episode — **the work does not advance a story. It holds one man at the edge of one island and asks the same question with other light.** ⚠️ **The poem is older than classical Greece, and the picture is built that way**: rough stone, wood, coarse cloth and bronze; no marble, no columns, no temple. ⚠️ **この1本は、移動を速さでなく距離で写す。****速さは、この作品の主題ではない。** 「着いた」は `s18` の側であり、**この1本の仕事は「まだ着かないこと」である**（`aim` の逐語:「この作品に「冒険」の画は要らない——**要るのは、まだ着かないことである。**」）。⚠️ **ゆえにこの1本の画には、陸が一つも無い**——**`s13` で岸は枠の外へ出た。**

## World Rules

- **The people in the work do not know that they are inside a film.** ⚠️ **This is why he does not look at the lens** — the camera is not there for him.
- **The answer is never given.** The goddess offers and the man says nothing. **A shot in which he opens his mouth is a shot this work does not have.** ⚠️ **この1本に返事は無い。****島はもう画面に無い**（`unit` の逐語:「島はもう画面に無い。海だけがある。」）。**島が応えるのは `s20` である。**
- **The goddess is never a face.** She is a voice from off-frame, a warmth on surfaces, moving air, and a light on the water that comes from behind the camera. ⚠️ **この1本に彼女の姿は無い。****四つの姿のどれとしても現れない。** **この1本の光は星であり**（`ledger.locations.海.states.夜` の逐語）、**彼女の第四の姿（枠の外の背後から来る水面の光）ではない。** ⚠️ **この1本には歌がある**（`l11`）——**が、それはポストで載る。**
- **No proper name is ever seen or heard.** Not on screen, not in the song. ⚠️ **この1本には歌がある**——`l11` である。**名はどこにも無い。****行き先の名も、島の名も。**
- **The bow does not appear in this work.** The axe is inside the fifth book; the bow is outside it. ⚠️ **この1本に弓は無い。****あるのは斧に似ていない道具である**——**実際、この1本の枠に道具は一つも無い**（§7 を見る）。
- **This work does not arrive.** The raft is still offshore in the last frame of the last shot.
- **No text appears on any surface.** The work names things by voice; it does not write them.
- **The age of the poem is bronze-age Mediterranean, before classical Greece. It does not move.** ⚠️ **He is not dressed as a classical hero** — no armour, no helmet, no greaves, one coarse undyed wool tunic, bare feet.
- **Only so many places can stand at once.** この1本が置くのは一つ——`海`、**夜である。****陸は無い。** ⚠️ **`海.geography` の逐語:「from the raft the water surrounds the frame on all sides and no land is visible in any direction** including behind」——**この1本は、その側である。**
- **This work speaks Japanese.** It is the language of the song, and there is no other voice in it. ⚠️ **この1本には歌がある**——`l11`「海を渡る」である。**画面の中の声ではない。****歌はポストで載る。**
- ⛔ **この1本の筏は、船ではない。** ⚠️ **`props.舟.appearance` の逐語:「a raft and not a boat」**——**船体も、竜骨も、肋も、甲板張りも無い。** **この1本の画で、そこが読み取れねばならない。**
- ⛔ **この1本は、まだ着かない。****水平線の高さは、この5.745秒のあいだ変わらない。** ⚠️ **変われば、この1本は「どこかへ着いた」の画になり、`s18` の仕事を先に食う。**

## Visual Language

- Art Direction: Open sea at night, photographed from just above the water at the height of a raft's bow: long low swells with no white water moving steadily in one direction, the horizon level and unbroken. In the lower part of the frame, the raft itself — **the bow of a low platform, not a vessel**: twenty-odd unseasoned barked pine logs lashed with coarse hand-twisted cordage, hewn planks laid across them and not fastened flush, **no keel, no ribs, no planking, no gunwale, and no raised sail.** ⚠️ **Land is nowhere in this frame** — no island, no coast, no headland. ⚠️ **No marble, no columns, no architecture of any later age.**
- Color Language: A narrow, graded palette — black water, a sky one shade above it, wet pine reading pale and raw against both, and one white line: the reflected path on the surface, cut by the swell and by the logs. ⚠️ **Nothing is lit apart from the stars and their reflection** — **the shot has no second light.**
- Texture: Coarse water broken into fine facets; the swell faces smooth and black; **bark still on the logs, raw hewn faces, and the hand-twisted cordage's uneven surface**; the wake's foam decaying to a thin line. ⚠️ **No metal, no machined edge, no paint, and no varnished surface anywhere.** Film grain present and even.
- Rendering: Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, a gentle flare where the light is in frame. **Not a photograph's stillness: a film frame, with a real lens's fall-off at the edges.** No illustration, no CGI look, no cartoon color.
- Visual Density: Low and steady — water, horizon, bow, and the wake. ⚠️ **この1本は、遠近の層を一つしか持たない**——**陸が無いので、奥行きを測るものが水平線しかない。**
- Time: `夜` — the source is the stars and their reflection on the water; **the waves are black and the reflected path alone is white**（`ledger.locations.海.states.夜` の逐語）。**`s09`〜`s15` と同じ夜である。**⚠️ **この作品は話を進めない**——**ゆえにこの夜と、`s16` の夜明けとのあいだに、順序を読まない。**
- Atmosphere: The hour in which passage is measured by what is left behind and not by what arrives.

# 3. SUBJECTS

## 舟

- Reference: ⚠️ **参照は `ledger.props.舟` の `appearance`・`negative` である。****この1本の主題は、この筏の移動である。**
- Appearance: **筏である。****船ではない。** **二十数本の、皮の付いたままの未乾燥の松の丸太を、手で縒った粗い縄で縛り**、**その上に、削った板が、面を合わせずに渡してある。** **竜骨も、肋も、甲板張りも、欄も、帆柱の台も無い。** **短い支えのある帆柱がある**（`舟.appearance` の逐語:「a short stayed mast of trimmed pine」）——⚠️ **帆はまだ一本も張られていない**（`舟.negative` の逐語:「no sail already raised on the raft before the sail exists」）。**帆は `s17` で初めて張られる。** **低く沈み、縁では水に洗われている。****船尾に、縛られた操舵の櫂がある。**
- Behavior: **進行方向へ進み、うねりに乗って上下する。****水位線が縁を洗い、泡が縁を伝って後ろへ流れる。** ⚠️ **速くない**——**この1本の移動は、速さではなく、後ろへ伸びる航跡の長さで出る。**
- Continuity Requirements: **Must preserve** — 丸太と縄の手作りであること、低いこと、竜骨・肋・甲板張り・欄が無いこと、縁が水に洗われること、そして**帆が張られていないこと。** **May change** — 舳先の画面の中の高さ、水の被り方、丸太の濡れ方。
- ⛔ **この1本の掟は `props.舟.negative` である**——「**no boat, no ship, no hull, no keel, no planking**」。⚠️ **この1本を「舟」と訳して渡せば、生成器は船体を作る。****ゆえにこの仕様は、英語の側で筏を筏として書く**（§18 を見る）。
- ⚠️ **この1本に帆は無い。****帆は `s17`（`l15`）で布から帆になる**——**この1本で帆を張れば、作品は順序を飛ばす。**

## 海

- Reference: **この1本の場所である。** ⚠️ **参照は `ledger.locations.海` の `base`・`geography`・`states.夜` である。**
- Appearance: **長く低いうねりであり、白波を立てない。****水平線は一本で、途切れない。** **夜であり、波は黒く、水面に一本の道だけが白い**（`海.states.夜`）。⚠️ **陸は一つも無い****——どの方向にも。** **帆も、鳥も、他の舟も無い。**
- Behavior: **うねりが一方向へ進む。****そして筏の下で持ち上げ、縁で割れる。** **航跡だけが後ろへ伸び、消える**（`motion.quality` の逐語:「**航跡だけが後ろへ伸び、消える。**」）。⚠️ **水面のいちばん白いのは、星の反射の道である。**
- Continuity Requirements: **Must preserve** — うねりの方向と低さ、白波が無いこと、水平線が水平で途切れないこと、波が黒く反射の道だけが白いこと、そして**陸がどこにも無いこと。** **May change** — 水面の細かさ、反射の道の幅、航跡の泡の残り方。
- ⚠️ **`海.geography` の逐語:「the surface broken only by the raft's own wake and by weed passing」**——**この1本では、その二つが両方とも出る。****浮いている草が、水面を横切って流れて行く。**
- ⚠️ **水平線の高さが、この1本の時計である。****動かなければ「まだ着かない」が出る。**

## 人（舵を取る者）

- Reference: ⚠️ **参照集合は `男.identity` を挙げる。****この1本の筏は、彼が舵を取っている筏である。**
- Appearance: ⛔ **この1本の枠に入らない。****彼はカメラの後ろに居る。** ⚠️ **カメラは舳先の高さにあり、前へ進む**——**舵は船尾にあり、船尾はカメラの後ろにある。** **ゆえにこの1本は、彼を一度も写さずに、彼の居る筏を写す。**
- Behavior: **枠の外で舵を取っている。****ゆえに画面の側には、彼の動きが一つだけ残る**——**舵の効きで舳先の向きがごく僅かに変わる、その変化である。**
- Continuity Requirements: ⛔ **この1本の枠に、彼を出さないこと** — 手も、肩も、後ろ姿も、影も、映り込みも。 ⚠️ **それでも、この筏を「無人の筏」として置かないこと**（`s21` の註の逐語:「**この作品の筏は彼が作ったものであり、空の筏は嘘である。**」）。
- ⛔ **この判断の根拠を書く。** 記録の `unit`・ビート・`motion.subject` は、**彼を一度も名指さない。** そして **`s18` の記録の逐語:「この作品で初めて、男が水の上に居る。」**——**曲順で `s18`（`l16`）は、この1本（`l11`）の後である。** ⚠️ **ゆえにこの1本は、彼を水の上に見せない。****しかし筏を空にはできない。** **§20 に、この読みを書いた。**
- ⚠️ **この1本は、同一性の塊を §18 に置かない**（`has_man: False`）——**枠に居ない者の錠を貼れば、居ない者を貼ることになる**（2026-09-29 の裁定①）。**§20 を見る。**

# 4. ENVIRONMENT

- Location: `海` — **夜である。****陸は無い。** ⚠️ **カメラは舳先の高さで、水面のすぐ上にある。**
- Environment Elements: **長く低いうねり**（白波は無い）、**途切れない水平線**、**一本の反射の道**、**流れて行く浮いた草**、**航跡の細い泡の線。** ⚠️ **陸も、島も、岬も、水に立つ岩も無い。****月も無い。**
- Environmental Behavior: **うねりが一方向へ進む。****筏が持ち上げられ、落ち、縁で水を割る。** **航跡が後ろへ伸びては消える。** ⚠️ **水平線は動かない。** ⚠️ **海は彼に反応しない**（`s21` の註と同じ規則）——**応えるのは `s20` の島だけである。**

# 5. OBJECTS

- ⛔ **この1本の枠に、道具は一つも無い。****斧も、弓も、櫂以外の何も無い。** ⚠️ **操舵の櫂は船尾にあり、船尾はカメラの後ろである**（§3 を見る）。
- **筏の縁と、渡した板** — ⚠️ **この1本の下端に、舳先として入る。** **濡れて、生の木の色をしている。**
- **航跡** — ⚠️ **物ではない。****この1本の時計であり、距離そのものである。**
- **浮いた草** — **水面を横切って流れて行く。** ⚠️ **`海.base` の逐語:「the surface broken only by the raft's own wake **and by weed passing**」。**

# 6. REFERENCES

- REF_CHARACTER: `男` — ⚠️ **この1本に添付しない。****そしてこの1本の枠に、彼は居ない**（**舵を取りに船尾へ居る。****§20 を見る**）。`女神` — ⛔ **この1本に添付しない。****彼女は四つの姿のどれとしても現れない。**参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・`海.states.夜`・`舟`・`舟.appearance`・`舟.negative` の8鍵である。
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_STYLE: `cinematic-still` (HIGH)
- REF_SOURCE: `projects/odyssey/bible.yaml` and `projects/odyssey/ledger.yaml` (CRITICAL)
- ⚠️ **REF_BOARD は無い。** この経路は絵コンテを要求しない。**この経路の参照素材は `role` を持つ**——`reference_image`（最大30点）・`reference_video`・`reference_audio`・`first_frame`・`last_frame`。**この経路の入力の型は5つである**（テキストのみ／参照画像／先頭フレーム／動画編集／動画延長）。
- ⚠️ **この34本は「テキストのみ」の型である。** `first_frame` ではない——⚠️ **先頭フレームの型は `ratio: adaptive` を要求する**（`specmap.MODELS` の註）。この作品は `16:9` を固定する。
- ⚠️ **この経路は、実在の顔を含む参照画像・参照動画を受け取らない**（公式の警告）。**この作品の人物は実在しないので、この制限には当たらない。**——**当たらないことを、ここに書く。** ⚠️ **それでも、この作品は参照を渡さない**（裁定②）。**渡さない理由は制限ではなく、選択である。**
- ⚠️ **§1–17 は下敷きであり、生成器へ投入するのは §18 だけである。**
- ⚠️ **形式カード `video-spec` の文法は、この作品の下敷きそのものである**——**他の形式はどれも「`video-spec` に文法を1つ足したもの」である**（`impossible-camera` の逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、この1本はそれに何も足さない。**
- ⚠️ **形式カード `video-spec` の6つの変数**（⚠️ 定義はカードの逐語である）:
  - `SUBJECT`＝the arc — **「移動そのものを、距離で写す」ことである。****カメラは舳先の高さにあり、前へ進む**（`motion.quality` の逐語:「カメラは舟の舳先の高さで、前へ進む。」）。
  - `DURATION`＝clip length (**the model decides the duration**) — ⚠️ **この作品の尺は、曲から来る**（`bible.song.lines[].at` の差）。**この1本は `5.745s` である。**
  - `ASPECT`＝aspect ratio — **`16:9`**（裁定④。§1 の4定数が固定する）。
  - `BEATS`＝the beat list with second ranges — **3つであり、明示的に不等である**（`0-1.499s` transition ／ `1.499-3.499s` sparse ／ `3.499-5.745s` dense）。§8 を見る。
  - `CORE`＝the beat that gets the largest share — **最後のビートである**（`3.499-5.745s`、2.246秒）。⚠️ **舳先が波を割り、航跡が一度に伸びるのがそこである。**
  - `HOOK`＝the note the clip ends on — ⚠️ **泡が消えるコマである。****説明のビートをそのあとに足さない**（カードの逐語:「End on the note, not after it.」）——**この1本は、航跡の泡が消えたコマで終わる。**
- ⚠️ **カードの逐語:「A digest that gives every beat equal time is the video equivalent of cramming. **Uneven duration is the composition.**」**——この1本の配分は §8 に在る。**

# 7. NARRATIVE

- Core Event: **渡っている** — 着かないことが、この1本の出来事である。
- Beginning: **海だけがある。****舟の舳先が画面の下端に入る。**
- Turn: **舟が上下する。** 航跡が後ろへ伸びる。
- Peak: **舳先が波を割る。** 航跡が一度に伸びる。
- Pull: ⚠️ **泡が消えるのが、切れ目のコマである。** **水平線は、5.745秒のあいだ、一度も近くならない。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - MOVEMENT 1 `0-1.499s` — density: `transition` — 海だけがある。**舟の舳先が画面の下端に入る。**
  - MOVEMENT 2 `1.499-3.499s` — density: `sparse` — **舟が上下する。**航跡が後ろへ伸びる。
  - MOVEMENT 3 `3.499-5.745s` — density: `dense` — **舳先が波を割る。**航跡が一度に伸び、**泡が消えるのが、切れ目のコマである。**
- Temporal Density: **Uneven, and weighted to the last 2.246秒.** 最初の1.499秒は**海だけの画に舳先が入ること**に払われ、次の2.000秒は**舟がうねりに乗ること**に払われ、**最後の2.246秒がこの1本の出来事である**——**舳先が波を割り、航跡が一度に伸びて、泡が消える。** ⚠️ **`held` を1つも使わない。** ⛔ **速くしない。****一つずつ起きる**——**17秒で木が筏になる `s16` と、同じ呼吸である。**

# 9. ACTION

- `ACT_SEA` — Before: 海だけがある。**舟は画面に無い。** After: **舳先が画面の下端に入る**——**うねりが筏を持ち上げる。**
- `ACT_RISE` — Before: 舳先が下端にある。 After: **舟が上下し、航跡が後ろへ伸びる。**
- `ACT_BREAK` — Before: 航跡が伸びている。 After: **舳先が波を割る**——**航跡が一度に伸びる。**
- `ACT_FADE` — Before: 航跡が長い。 After: **泡が消えるのが、切れ目のコマである**——**水平線は動いていない。**

# 10. CAMERA

- Camera Language: Third person, **at the height of the bow, just above the water, moving forward with the raft.** ⚠️ **この高さは、この作品では `s21` の「在りえない高さ」ではない**——**`s21` の註の逐語:「`s14` は舳先の高さであり、この1本は在りえない高さである。」**
- Camera Events: One event only. `0-1.499s` — **the sea alone, and then the bow enters the lower edge of the frame as the swell lifts the raft**; then `1.499-3.499s` — **the raft rides the swells up and down and the wake begins to run back**; then `3.499-5.745s` — **the bow breaks the water, the wake lengthens at once, and the foam goes.** ⚠️ **カメラは、この1本のあいだ、一様に前へ進む。**⚠️ **動機は「移動すること」そのものである**——**追うものも、寄るものも無い。**
- Camera Behavior: **The style permits a dolly, a crane and a Steadicam, and this shot spends none of them** —— ⚠️ **この1本の移動は、水の高さを保ったままの前進である。****前進は一様であり、重さを持つ。** **No crane. No dolly. No Steadicam** — **ゆえにこの1本は、舳先の高さを一度も離れない。** **No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, and no unmotivated move.**

# 11. MOTION

## Subject Motion

**この1本の主題の運動は、前へ進む筏である。****舳先が水を割り、縁が水に洗われ、航跡が後ろへ伸びる。** ⚠️ **速さは出さない**——**出るのは距離である。**

## Object Motion

**動く物は、筏の一部と、水面の草だけである。** ⚠️ **この1本に道具は無い。**

## Environmental Motion

**うねりが一方向へ進み、白波を立てない。****水面の草が横切って流れて行く。** **水平線は動かない。** ⚠️ **この二つが同時であることが、この1本の「距離」である**——**近い面は速く流れ、遠い線は止まっている。**

## Physical Characteristics

- **Weight**: **筏の重さは、低さと、水の被りで出る。** **丸太は沈み、縁は洗われる。** ⚠️ **軽く跳ねる船ではない。**
- **Inertia**: **一度乗ったうねりは、次のうねりまで抜けない。****航跡は、舳先が去ったあとも残る。** ⚠️ **泡はすぐには消えない**——**消えるのは最後のコマである。**
- **Acceleration**: **加速しない。****うねりも、前進も、航跡の伸びも、一様である。** ⚠️ **この1本に、速くなる区間が一つも無い。**
- **Fluidity**: Continuous; no snap, no held cel, no stutter. ⚠️ **この5.745秒の全コマで、水面は動いている。**
- **Impact**: **静かなものだけである。****舳先が波を割るのは、衝撃ではなく、重さである。** ⚠️ **白波も、飛沫も、この1本には無い。**

# 12. EMOTION

- Emotional Arc: **渡っている。****それは、劇的でない時間である。** ⚠️ **この1本の感情は、「着かないこと」の側にある**——**`aim` の逐語:「この作品に「冒険」の画は要らない」。**
- Emotional Events: ⚠️ **この1本の出来事は、表情でも、まなざしでもない。****舳先が水を割ることである。** **誰も写さないのに、進んでいることだけが残る。**

# 13. LIGHTING

- Base Lighting: **夜である。****光源は星と、その水面の反射だけである。****波は黒く、反射の道だけが白い**（`ledger.locations.海.states.夜` の逐語）。⚠️ **月も、火も、灯も無い。** **生の木だけが、水面より一段明るい。**
- Lighting Events: **One, and it runs the whole shot.** **反射の道が、うねりと筏で細かく割れ続ける。** ⚠️ **光源は動かない。** ⚠️ **様式カードの逐語:「The grade holds for the whole shot — a colour temperature that swings is a different style.」**

# 14. AUDIO

- Dialogue: **None.** ⚠️ **彼は口を開かない**（`world.rules`）。**この作品に台詞は一つも無い。** ⚠️ **この作品は日本語を話す**；§18 がそれを名乗る。
- Sound Effects: **水が舳先と縁に当たる音。****縄と木が軋む音。****航跡が後ろで崩れる音。****弱い風。** ⚠️ **この1本に人の音は一つも無い**——**舵を取る者の音も、息も、掛け声も無い。**
- Music: **None, by specification.** ⚠️ **これは省略ではない** — §16 と §18 の両方が床の `no background music` を運び、⚠️ **この経路では `No BGM` が、実際に受け取られる数少ない否定の一つである。** 音床も、スコアも、切れ目のスティングも無い。 ⚠️ **主題歌はこの1本のあいだ鳴っている**（`l11`）——**が、この1本の中には無い。****編集で載る。**
- Environment: 夜の外海。**水、木、そして遠さ。** ⚠️ **鳥の声も、他の船の音も無い**（`海.base` の逐語:「No land, no sail, no bird, no other vessel.」）。

# 15. CONTINUITY

- Identity: ⚠️ **この1本に人が一人も居ないので、人物の同一性は掛からない。** **掛かるのは筏と海の同一性である**——**丸太と手縒りの縄、低さ、竜骨・肋・甲板張り・欄が無いこと、そして帆がまだ張られていないこと。** ⛔ **`男.identity` は参照集合に在るが（§6）、この1本は同一性の塊を §18 に貼らない**——**舵を取る者はカメラの後ろに居る**（2026-09-29 の裁定①。§20 を見る）。
- Spatial: **カメラは舳先の高さにあり、水の上である。** ⚠️ **水際の線と水平線は、この作品のどの岸の画と同じものである**（`海.geography` の逐語:「The same waterline and the same horizon appear in both, so that the two views are demonstrably one sea.」）——**ゆえにこの1本は、岸から見た海と同じ一つの海である。** ⚠️ **この1本は `video-spec` を名乗り、この形式は §15 から何も免除しない**——**免除を名乗るのは、`coexisting-realities` を名乗る4本だけである。****この1本の場所と時刻は、台帳の `海`／`夜` のままである。**
- Temporal: **夜である。****`s09`〜`s15` と同じ夜である。** ⚠️ **この作品は話を進めない**（§2 の逐語:「the work does not advance a story」）——**画の中に日付を与えるものは何も無い。**
- Visual: **The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **この1本の光は星とその反射だけである。**
- Motion: Full animation, not limited. **水面が流れ、筏が上下し、舳先が水を割り、航跡が伸びる。** ⚠️ **カメラは一様に前へ進み、止まらない。**
- Sound: **水、木、縄、風。****音楽なし。言葉なし。**
- ⚠️ **この34本は、すべて同じ経路である**（`SEEDANCE 2.5`）。**他の作品の三本（`MINIMAX H3`）とは別である。** ⚠️ **ずれてはならないのは、場所と、パレットと、光と、そして画面の文法である**——**プロンプトの字面ではない。**

# 16. CONSTRAINTS

## MUST NOT

- No woman in frame at any distance, in any focus; **no face for the goddess**, no portrait, no close-up of a woman, no white robes, no classical drapery, no veil, no halo, no divine light around a figure. ⚠️ ⚠️ **この1本の彼女は、四つの姿のどれとしても現れない。** **ここにあるのは、夜の海と筏だけである。** ⚠️ **海を女の形にしないこと**（`characters.女神.negatives` の逐語:「no visible body, no hands, no feet, no arms, no silhouette with a readable outline」）。
- No boat, no ship, no hull, no keel, no planking, no sail, no raft, and no other vessel.
- No blood, no wound, no corpse, no slaughter, no butchery, no carcass.
- No fire, no torch, no lamp, no flame used as a light source. ⚠️ **この作品の光は、日の光・月・星だけである。**
- No classical architecture, no columns, no marble, no temple, no built structure of any kind — no jetty, no wall, no stair, no path.
- No legible text on any surface; no letters, no numerals, no writing, no marks of a hand.
- No modern object, no machine, no synthetic material, no clothing of any later age.
- **No cut to a second setup.**
- No handheld wobble, no unmotivated camera move, no snap zoom, no unnatural rotation.
- No flat television lighting, no snapshot framing, no pure cartoon color, no CGI look, no illustration.
- **No person in frame at any moment** — **the frame holds the sea, the bow and the wake; whoever is steering is aft of the camera and is never seen** — no hands, no shoulders, no back, no silhouette, no figure at any distance, and no shadow or reflection of a person anywhere. ⚠️ **`s18` の記録の逐語:「この作品で初めて、男が水の上に居る。」**
- **No boat, no ship, no hull, and above all no keel, no ribs, no planking, no gunwale and no deck** ——⚠️ **`props.舟.negative` の逐語であり、この1本でいちばん効く禁制である。**
- **No sail, and no cloth of any kind on the raft**（`舟.negative` の逐語:「no sail already raised on the raft before the sail exists」——**帆は `s17` で初めて張られる**）。
- **No metal fastening, no nail, no rope that is not hand-twisted**（`舟.negative` の逐語）。
- **No land of any kind** — no island, no coast, no headland, no rock standing in the water, **and no land behind the camera either**（`海.geography` の逐語）。
- **No moon, no torch, no lamp, and no second light on the water** — **この夜の光は星と、その反射だけである**（`海.states.夜` の逐語）。
- **No white water, no breaking crest, no spray, and no foam except the raft's own wake**（`海.base` の逐語:「Long low swells with no white water」）。
- **No bird and no other vessel**（`海.base` の逐語）。
- **No oar, no pole and no tool in frame** — ⚠️ **操舵の櫂は船尾にあり、船尾はカメラの後ろである。**
- **No cut to a second setup.** ⚠️ **この1本は1つの画である。**
- ⚠️ **この1本の筏は、この禁制の対象ではない。****画の中の筏は、船ではない**（`props.舟.appearance` の逐語:「**a raft and not a boat**」）。**禁じられているのは船体・竜骨・甲板張り・欄であり、この1本の丸太と縄ではない。**
- ⚠️ **この1本に男は居ないが、`男.negatives` は参照集合に在る**（§6）——**彼の禁制はこの1本でも掛かる**（逐語:「no muscular hero's body, no heroic pose, no heroic lighting」・「no youthful face, no beardless face, no clean or unlined skin」・「no armour, no helmet, no greaves, no shield」）。⚠️ **ここでは、それが「手も、肩も、後ろ姿も入れないこと」として効く。**
- ⚠️ **形式 `video-spec` 自身の禁制**（カードの `## Negative`、逐語）: ``no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no background music, no watermark, no morphing or drifting facial identity``

- No music of any kind in this shot. ⚠️ **この経路では `No BGM` が、実際に受け取られる数少ない否定の一つである。**
- No on-screen subtitles, no captions, no burned-in subtitles in any language. ⚠️ **この経路には、字幕を作るための公式の記法がある**（`【】`）——**ゆえにこの節は、他の二つの経路よりここで必要である。**
- No watermark.
- No uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion.

## MUST

- **移動が距離として出る** — **航跡が後ろへ伸び、泡が消えるのが、切れ目のコマである。**
- **It is a raft and not a boat** — ⚠️ **丸太、手縒りの縄、低さ、縁が水に洗われること。**
- ⚠️ **同一性の塊を §18 に貼らないこと** — **枠に居ない者の錠を貼らないためである**（`has_man: False`。2026-09-29 の裁定①）。**§20 を見る。**
- ⛔ **人を一人も枠に入れない** — **舵を取る者はカメラの後ろである**（§20 を見る）。
- ⚠️ **水平線が一度も近くならないこと** — **着かないことが、この1本の仕事である。**
- ⚠️ **帆がまだ張られていないこと。****帆は `s17` の仕事である。**
- **星の光だけであること** — **月も、二つ目の光も無い。**
- ⚠️ **変化は最後のコマで終わる** — **泡が消えたコマで、この1本は終わる。**

## PREFER

The logs kept raw and barked and the cordage visibly hand-twisted; the raft sitting low, awash at the edges; the wake growing longer rather than the water moving faster; **weed crossing the frame as the second thing that breaks the surface.**

## ALLOW

A lens flare where the light crosses the frame; a moderate depth of field that lets the far water go soft; **the bow entering and leaving the lower edge of the frame as the swell carries it.**

# 17. GENERATION PRIORITIES

1. **移動が距離として出ること** — **泡が消えるコマで終わること。** **この1本の切れ目はそれである。**
2. ⛔ **筏であって船でないこと** — **竜骨も、肋も、甲板張りも、欄も無い。** **帆も無い。**
3. ⛔ **水平線が近くならないこと** — **着けば、この1本は `s18` の仕事を先に食う。**
4. ⛔ **人を一人も枠に入れないこと** — **舵を取る者はカメラの後ろである。**
5. ⚠️ **同一性の塊を §18 に置かないこと** — **枠に居ないためである**（2026-09-29 の裁定①）。
6. ⚠️ **水際の線と水平線が、岸の画と同一であること。**
7. **星の光だけであること** — **月も、火も、二つ目の光も無い。**
8. Everything else.

---

# 18. SEEDANCE 2.5 PROMPT MAPPING

⚠️ **この経路の §18 は、他の二つの経路と書き方が違う。** **時区分をプロンプトの中に書ける**（`0-3s:`）——**ゆえに `Master Prompt` が、それ自体で一本の時間割を持つ。**
⚠️ **そして `Negative Prompt` を、この経路は床として受け取らない**（`specmap.MODEL_UNRECEIVED_SLOTS`）。公式に否定として扱われるのは**字幕と音声だけ**である（`"No subtitles."` / `"No BGM"`）。**残りは、ただの散文として読まれる。**
⚠️ **ゆえに禁制は二箇所に置く**——**ここの `Negative Prompt`**（**この作品が何を禁じるかの記録**。⚠️ **この経路はこれを受け取らない**）と、**`Master Prompt` の散文**（**この経路が実際に読む側**）。**同じことを二度書いているのではない。片方は床で、片方は助言である。**
⚠️ **`L30` がこれを鳴らす。** **それが正しい**——鳴らなければ、この経路の否定が床であるかのように読まれる。**この作品は、それを承知で使うと宣言している**（`bible.route_limits_accepted` の `SEEDANCE 2.5: Negative Prompt`）。**除外は作品の宣言であって、基盤の判断ではない。**
⚠️ **この節の `Negative Prompt` と `Style Motion` は、34本で同一である。** 理由は `L10` にある——`ledger.disclosure` の4つの変化点が `negative: covered`（**§18 の `Negative Prompt` は変わらない**）を宣言しており、**「覆った」は「同じである」を要求する。** ゆえに**ショット固有の禁制はこの節に書かない**——それは `shot.forbidden_set`（引き渡しの層）と §16 が持つ。⚠️ **形式カード自身の `Negative` は §16 の側から届く**——この作品は形式をショットごとに名乗るので、**カードの `Negative` をここに混ぜれば、`Negative Prompt` がショットごとに動き、`L10` の4つの `covered` が偽になる。**
⚠️ **この1本は `video-spec` を名乗る**——**この形式の禁制（`no uniform pacing`・`no equal-length beats`・`no static slideshow of stills` ほか）は §16 の床に在り、**カード自身の `Negative` も §16 の側から届く。** **ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**

## Master Prompt

A 5.745-second cinematic take (16:9) of the open sea at night, shot from just above the water at the height of a raft's bow, moving forward with it, one clip, one continuous take, one change: **the raft is under way and has not arrived — the wake lengthens, the foam goes, and the horizon has not come one step closer.** **No land is in this frame at any moment: no island, no coast, no headland, and no land behind the camera either.**

**The raft is not an empty one: the man who built it steers it from the stern, which is behind the camera, and he is not seen at any moment.**

0-1.499s: **the sea alone, and then the bow comes into the lower edge of the frame as the swell lifts the raft.**
1.499-3.499s: **the raft rides up and down; the wake begins to run back.**
3.499-5.745s: **the bow breaks the water and the wake lengthens at once — and the take ends as the foam goes.**

**The raft is a raft and not a boat**: twenty-odd unseasoned barked pine logs lashed with coarse hand-twisted cordage, hewn planks laid across them and not fastened flush, **no keel, no ribs, no planking, no gunwale, no metal fastening, no nail, and no sail** — only a short stayed mast of trimmed pine with nothing bent to it. **It sits low and the water washes over its edges.** **The night's only light is the stars and their single reflected path on the water: the waves are black and the reflected path alone is white.** **Long low swells with no white water, weed passing across the frame, and the only foam is the raft's own wake.** **No other vessel, no bird, no moon, the horizon level and unbroken.** **This is a bronze-age world: no made thing of any later age stands in this frame, and this raft is hand-built from unseasoned timber.** **This is a Japanese work.** No subtitles. No BGM.
(One continuous take, one change: the crossing is shown as distance and not as speed.)

## Visual Prompt

Open sea at night, photographed from just above the water at the height of a raft's bow: long low swells with no white water moving steadily in one direction, the water black and broken into fine facets, and one reflected path of starlight lying on it in white; the horizon level and unbroken beyond, and no land anywhere. **In the lower part of the frame, the bow of a raft** — twenty-odd unseasoned barked pine logs lashed with coarse hand-twisted cordage, hewn planks laid across them and not fastened flush, **no keel, no ribs, no planking, no gunwale and no sail**, only a short stayed mast of trimmed pine with nothing bent to it; the logs sit low and the water washes over them, and **a thin line of wake trails back out of the frame**. **No figure is in the frame at any distance or in any focus — the man steers from the stern, behind the camera — and no shadow or reflection of a person falls anywhere in it.** No other vessel, no bird, no moon. Anamorphic lens with subtle oval bokeh and a gentle flare where the light is in frame; a moderate depth of field; a graded palette of cold slate blue in the water and the wet stone, cold white held in the one reflected path on the black water. **no skin and no cloth anywhere in this frame**: barked raw pine logs and hand-twisted cordage, awash at the edges; even film grain over everything. No painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration. ⚠️ **No person is in this frame at any moment — whoever steers is aft of the camera.** ⚠️ **This is a raft and not a boat**: no hull, no keel, no planking, **and no sail has been bent to the mast yet**; the only foam is the raft's own wake.

## Motion Prompt

Full animation, not limited. **The long low swells move steadily in one direction and do not break.** **The raft rides them up and down, sits low, and the water washes over its edges.** **The bow breaks the water and the wake runs back and lengthens — and the foam of it decays, slowly, until it goes.** **Weed crosses the frame and passes out of it.** **The reflected path of starlight wavers on the running water and runs unbroken.** **The horizon does not move at all** — **it is exactly as far away in the last frame as in the first.** No motion blur smears, no stutter, no floaty weightless motion, no static frames — **the water moves in every frame of the take.**

## Camera Prompt

Third person, **at the height of the bow, just above the water**, moving forward with the raft at an even rate. One event only: **the bow enters the lower edge of the frame, rides the swells, and breaks the water as the wake lengthens; the camera never leaves the bow's height.** ⚠️ **The move is motivated by the crossing itself — there is nothing to chase, nothing to approach and nothing to leave behind.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot spends none of them** — the move is a forward travel at water level, and it carries a real rig's even rate. No crane. No dolly. No Steadicam. **Do not rise, do not descend, and do not slow.** No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, no unmotivated move.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the song, and the song is the only voice this work will ever have. **No line is spoken in this shot: there is no dialogue anywhere in this work, and there is no voice-over and no narration.** **The Japanese is not spoken here; it is what this work is** — and **nothing is written on screen**: no subtitles, no captions, in any language. Sound effects, nothing mixed forward: **water breaking at the bow and washing along the edges, cordage and timber creaking under load, the wake collapsing behind, and a little wind** — **and nothing else, because there is no one in this frame to make a sound.** **No voice of any kind** — no one here calls and no one is called. **Music: none — this shot carries no music of any kind.** No bed, no score, no sting, no drum.

## Negative Prompt

no watermark, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no swelling music, no drum, no legible text on any surface, no readable characters on any surface, no letters, no numerals, no writing of any kind, no bow, no arrow, no quiver, no archery, no classical architecture, no columns, no marble, no temple, no built structure, no armour, no helmet, no shield, no sword, no weapon of any kind, no face for the goddess, no portrait of a woman, no woman in frame, no body for the goddess, no white robes, no classical drapery, no veil, no halo, no aura, no divine light around a figure, no second person in frame, no companion, no crowd, no blood, no wound, no corpse, no slaughter, no butchery, no carcass, no fire, no torch, no lamp, no flame used as a light source, no modern object, no machine, no synthetic material, no clothing of any later age, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no flat TV lighting, no snapshot look, no pure cartoon color, no CGI, no illustration

## Style Motion

- **The frame is one frame of a take, and the take does not cut.** Time enters as continuation, not as a second setup — a cut would make it two stills.
- **What moves was already in the frame.** The camera's slow travel, a flare crossing the lens, a held gesture completing: nothing is introduced that the still did not imply.
- **Shallow depth is the mover's constraint.** What leaves the plane of focus loses itself, and coming back into it is the beat — the shot's changes happen at the focus plane.
- **The camera moves with a real rig's weight** — dolly, crane, Steadicam — or holds. But a hold here is a decision a camera makes, not a photograph's stillness.
- ⚠️ **What this style does not do**: cuts to a second setup, flat television lighting, snapshot framing, handheld wobble, unmotivated camera moves. ⚠️ **The grade holds for the whole shot** — a colour temperature that swings is a different style.
(Source: the `Motion character` of the style card `cinematic-still`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `odyssey-s14-5.745s-01`
- Segment ID: `chorus-1-2`
- Specification Version: `0.1.0`
- Generation Date: ⚠️ **未記入。** **この作品は、まだ1本も生成していない。**
- ⚠️ **日付は、生成した者が生成した日に書く。****私ではない**——**何が実際に起きたかを、私は見ていない。** ⛔ **世代の記録は `takes/` に置く**（この作品にはまだ無い）。**この仕様は世代を写さない。**

## Resolved Values

- Duration: `5.745s`
- References: `REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は既定で何も添付しない）。⛔ **この1本の §18 は人物の同一性を運ばない**——**人物がこの枠に居ないためである**（`has_man: False`）——**`Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は書かれていない。**⚠️ **`男.negatives` は参照集合に在る**——**ゆえに §16 は彼の禁制も運ぶ**（§20 を見る）。
- Temporal Structure: `3 movements, NON_UNIFORM — 0-1.499s / 1.499-3.499s / 3.499-5.745s`. The held movement = `none`
- Camera Events: `1 event as listed in §10`
- Action Events: `ACT_SEA → ACT_RISE → ACT_BREAK → ACT_FADE`
- Audio Events: `no dialogue ／ water ＋ timber ＋ cordage ＋ wind ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **初版である。** ⛔ **この節は仕様の側であって、世代の記録ではない**——**記録は `takes/` に在る。** **採用は、まだ選ばれていない**——**選ぶのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。

### 未処理（この版では決めていない）

- ✅ **裁定（2026-09-29）: この1本は人物を枠に置かず、同一性の塊も §18 に貼らない**（`has_man: False`）——**記録の `unit`・ビート・`motion.subject` が彼を一度も名指さないためである。** ⚠️ **この仕様は裁定の前、彼を船尾（カメラの後ろ）に置き、塊を作品の錠として §18 に置いていた**——**裁定①が塊を落とした。****ゆえに `{IDENTITY}` は §18 に無い。** ⚠️ **それでも筏は無人ではない**（`s21` の註の逐語:「**この作品の筏は彼が作ったものであり、空の筏は嘘である。**」）——**この読みは裁定のあとも変わっていない。**
- ⚠️ **カメラの足場を、記録は書かない。** 参照集合が `舟` を挙げ、`motion.quality` が「カメラは舟の舳先の高さで、前へ進む」と書くので、**この仕様はカメラを筏の側に置いた**——**それが筏の上なのか、舳先の外なのかは、記録からは読めない。**⚠️ **どちらでも、この1本の画は同じである**（下端に舳先、上に水平線）。
- ⚠️ **この1本に帆柱があるかどうかを、記録は明示しない。** 参照は `舟.appearance`（帆柱を含む）と `舟.negative`（帆を張るな）の両方を引く。**この仕様は、帆柱を立てたまま、帆だけを張らない、と読んだ。**
- ⚠️ **`l11` は3回歌われる**（`l11`／`l20`／`l29`）。**この作品は3本とも役を同じにし、差分を §6 の形式が持つ**——**この1本は `video-spec` であり、`s21`・`s30` の形式はこの仕様からは読めない。**
- ⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**

## Observed Problems

- ⚠️ **まだ1本も生成していないので、観察は無い。** **空である。** ⛔ **絵を見る検査は、この基盤に無い**——**見たことを書けるのは、見た者だけである。**

## Anticipated risks (to check in the first generation)

- ⛔ **船として出る。** ⚠️ **竜骨、肋、甲板張り、欄、金属の留め具**——**一つでも出れば、この1本はこの作品の嘘になる。**
- ⛔ **帆が張られる。** ⚠️ **`s17` の仕事を先に食う。**
- ⛔ **水平線が近くなる、あるいは陸が入る。** ⚠️ **着けば、この1本は `s18` の画になる。**
- **速さが出る。** ⚠️ **舳先に白波が立ち、飛沫が上がれば、この1本は「冒険」の画になる**——**要るのは距離である。**
- **舵を取る者が写る。** ⚠️ **手一つでも入れば、`s18` の「初めて」が壊れる。**
- **航跡が伸びない。** ⚠️ **距離の手がかりが消えれば、この1本はただの海の画になる。**
- **月が光源として入る。** ⚠️ **この夜の光は星である。**
- **様式美に寄りすぎる。** ⚠️ **`様式美` は `s15` の役である**——**この1本は `運動` であり、重さと慣性で測られる。**
