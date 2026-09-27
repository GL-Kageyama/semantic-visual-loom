# Seedance 2.5 Full Specification — 『ハビッツ！！！』主題歌MV『誰の名』 habits-mv-s01「閉じた出席簿が、開かれる」 / 8.059s

⚠️ **この8.059秒は、この作品の1本目である。** 歌が1行も無い区間であり、
`ledger.song_coverage` は**この節だけを節ごとに受ける**（`L36` の②）。
⚠️ **この作品の最初の一変化は「手」である。** 世界の規則「**手が先にあり、顔が後に来る**」は、
**1本の内側の規則であると同時に、作品全体の規則でもある**——ゆえにこの1本は、**顔を持てない。**
⚠️ **参照集合に `碓氷千夏.identity` を入れない。** **この1本は手しか写さない。**
人のかたちの一枚を渡せば、生成器は顔を置く。**ゆえに渡すのは禁制の側だけである。**
⚠️ **世界の規則は「運搬は一度も完了しない」である。** この1本の変化は**「開く」であって「読む」ではない。**
*転出欄は開かれるが、まだ誰も読んでいない*——**運搬の最初の一歩が、ここで止まる。**

---

⛔ **この仕様は 2026-09-28 に運動の層を作り直した（`0.1.0` → `0.2.0`）。**
**規則——「変化は、切れ目で終わる。」** この作品の切れ目は曲が置いたものであり、
実測で **26の切れ目のうち24が歌詞の行の頭と 20ms 以内で一致する。**
⛔ **前の版は、そのアクセントに静止で入っていた。** この1本では**変化が切れ目の 1.5秒前に終わっていた**
（テイクを 0.25秒窓で測ると、6.00秒で山を打ち、以後 1.5秒を山の 1.3〜4.0% で過ごしている）。
**いまは、頁が沈みきる瞬間に切れ目が来る。**
⚠️ **土台は動いていない。** `shot-record.schema.json` の `motion` の註——
**「止まるのは主題であって、画面ではない。光と粉塵は動く。」**——を、前の版は
「主題が止まるなら画面も止まる」と読んでいた。**そこだけを直した。**
⚠️ **`§18` の `Negative Prompt` と `Style Motion` は1字も動かしていない**（`L10`）。

---

# 1. VIDEO

- Duration: `8.059s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take of one change — **a closed register on a desk is opened by a hand, and the transfer column comes up.** ⚠️ **The first movement this work ever shows is a hand**, and **no face is in this shot at all**: the order the work is built on is not yet two steps old. ⚠️ **The change completes on the last frame of the take** — the page is still settling when the cut arrives, and **the frame is never still in the meantime**: dust crosses, the tube's light breathes, and the camera is descending from the first frame to the last.

# 2. WORLD

## World Concept

2026, Japan. Kawaguchi in Saitama, Adachi in Tokyo, Totsuka in Yokohama — and in this shot, a staff room at the end of a working day, at a desk with last year's attendance register on it. There is no magic, no institution and no secret organization: there is only a daily life in which the etiquette of the written name is thoroughly in place. **The name is the subject of this work, and the name this work is about is the one that is read the wrong way** — which is why every name on every in-world prop is printed or written and nowhere legible. ⚠️ **This is a theme-song music video:** one song of 179.320 seconds, twenty-seven shots, no episode — **the work does not advance a story. It holds one question and asks it again with other hands.**

## World Rules

- **The people in the work do not know that they are inside a film.**
- **The hand comes first and the face comes after. The order is not swapped. A face is placed only after it has been called.**
- **The name lives on the side of being called, not on the side of being written.** A name is made of the number of times it has been called.
- **The sound is not a calling voice; it is the sound of paper and hands.** A calling voice is heard only on the side of the one called.
- **The carrying in this work never completes.** It is not received, or it is treated as not received, or it is received and not read where it arrives. **Not completing is the only way a movement is kept from becoming an event** — an event is a carrying that completes.
- **No text is burned into this work.** In-world text is a different thing from a subtitle, and this work draws the first and forbids the second.
- **The writing seen in this work is print, ballpoint and pencil — and none of it is legible.**
- **Only so many places can stand at once.** This shot places one.
- **This work speaks Japanese.** It is the language of the room and of the people in it.

## Visual Language

- Art Direction: Luminous realist anime, translated into a desk in a school staff room at the end of the day. A Japanese record-keeping site, 2026: three resolutions of the written name — print, ballpoint pen, pencil — the thickness of a register's left sleeve, a fluorescent tube, a desk whose edge has taken years of forearms. **The light, not the figure, is the subject** — and here the light is a fluorescent tube, falling flat across a closed cover.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The palette is narrow — fluorescent white, the grey-green of the cover, the cream of the page edge, the warm side reduced to one hand and to the paper itself.
- Texture: Layered atmospheric depth from near to far; dust suspended and individually rendered where the tube catches it above the desk. The cover's cloth has a weave and the page edge is layered, not smooth. No grain overlay, no paper texture, no painterly stroke.
- Rendering: Clean anime lineart on the figure, drawn at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — **no second tone inside one piece of cloth, no gradient inside a single material, no soft airbrush.** ⚠️ **The written name is drawn as the resolution it is** — cut, printed, ballpoint and pencil are four different marks, not one texture applied four times.
- Visual Density: Low. One focal point — the cover and the hand that arrives on it — with generous negative space, most of the frame given to the desk.
- Time: `勤務日の夕方` — the end of a working day, indoors. **The same working day as the twenty-six shots that follow it; the work does not fix a date.**
- Atmosphere: A desk that is being cleared at the end of a day, and is not being watched.

# 3. SUBJECTS

## 碓氷千夏の右手

- Reference: the frozen setting sheet — `distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/ChatGPT Image 2026年9月18日 20_29_36.png` （キャラクター設定画）＋ `.../ChatGPT Image 2026年9月17日 21_56_32.png` （表情シート）. ⚠️ **この1本には添付しない** — **この1本は手しか写さない。**
- Appearance: **外見の記述は出典に一行も無い**（方針 §5a）。**凍結した二枚が外見である。** この1本が置くのは**右手だけ**である — 甲の幅、指の関節、爪の形、袖口から先。⚠️ **顔・髪・名札・衣服の識別は置かない。** 手は**誰の手でもない手**として写り、**「読む手は、誰の手。」という問いの側に立つ。**
- Behavior: **手は画面の下から入り、表紙に触れ、頁を一度だけ起こす。** ⚠️ **急がない。** 指の腹が表紙を押さえ、角が少し浮く — **この作品で最初の運動はこれだけである。**
- Continuity Requirements: **Must preserve** — 手の造形は凍結した二枚に従う（<b>この1本では添付しないが、他の4本と同じ手でなければならない</b>）。**May change** — 何も変えない。⚠️ **爪の形と関節の節は、`s02`〜`s04` の同じ手と一致すること。**

## nobody

- **この1本に、二番目の人物は居ない。** 顔も、立ち姿も、肩も、写らない。
- ⚠️ **`Negative Prompt` はこの経路では床にならない**（§18 の前書き）。**ゆえにこれは肯定形で負う** — §16 `MUST NOT` と、`Master Prompt` 自身の一文が負う。
- ⚠️ **弱い守りである。記録として書く。**

# 4. ENVIRONMENT

- Location: `出席簿の転出欄` — **the site of this work's first line, not a room.** ⚠️ **基盤画像は無い** — 本編の側にもまだ無い。**この作品は、それを作らない。**
- Environment Elements: 区立小学校の職員室。机の上。**出席簿は閉じた状態から開かれる。** 机の面、蛍光灯の管、閉じたままの引き出し、机の脇の椅子の背。⚠️ **範囲を広げない** — 歌が「目で、読む」「口は、動く」「音は、出ない」と言っている以上、以後の3本は顔の側へ寄る。**部屋は要らない。**
- Environmental Behavior: 埃が、管の下で浮いて動く。**机は動かない。** ⚠️ **手が止まったあとも、埃と光は動き続ける** — それがこの1本を静止画にしない。風の出来事は無い。

# 5. OBJECTS

- **前年度の出席簿**, closed on the desk. 左袖ほどの厚みの表紙、**閉じたままの小口**、背の綴じ。**開かれる。** ⚠️ **欄は記入済みだが、読めない。**
- **転出欄**, on the opened page. **この作品の一行が残っている欄である** — ⚠️ **開いた頁の上に出るが、まだ読まれない。**
- **机の面** — 木目と、前腕が作った艶。ほかに何も置かない。
- No other object is in frame.

# 6. REFERENCES

- REF_CHARACTER: 碓氷千夏 — **この1本には添付しない。** 参照集合が挙げているのは `碓氷千夏.negatives` だけである——**ゆえに渡るのは禁制の側だけである。** ⚠️ **この1本は手しか写さない**——**ゆえに渡るのは禁制の側（`碓氷千夏.negatives`）だけである。**
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_STYLE: `luminous-anime` (HIGH)
- REF_SOURCE: `projects/habits-mv/bible.yaml` and `projects/habits-mv/ledger.yaml` (CRITICAL)
- ⚠️ **REF_BOARD は無い。** この経路は絵コンテを要求しない。**この経路の参照素材は `role` を持つ**——
  `reference_image`（最大30点）・`reference_video`・`reference_audio`・**`first_frame`**・**`last_frame`**。
  **この経路の入力の型は5つである**（テキストのみ／参照画像／先頭フレーム／動画編集／動画延長）。
  ⚠️ **この27本は「参照画像」の型である。** 人のかたちの一枚と、小道具の語を、`reference_image` として並べる
  ——**`first_frame` ではない**（先頭フレームの型は `ratio: adaptive` を要求する。`specmap.MODELS` の註）。
- ⚠️ **この経路は、実在の顔を含む参照画像・参照動画を受け取らない**（公式の警告）。
  **この作品の人物は実在しないので、この制限には当たらない。**——**当たらないことを、ここに書く。**
- ⚠️ **§1–17 は下敷きであり、生成器へ投入するのは §18 だけである。**

# 7. NARRATIVE

- Core Event: **A closed register is opened by a hand, and the transfer column comes up.**
- Beginning: **The register is shut and the desk is empty of hands** — the tube's light is on the cover and already changing, dust is already crossing the desk, and the camera is already descending.
- Turn: **The hand arrives from below the frame.** It is the first movement of the work, and it is not a face.
- Peak: **The cover rises, the leaves fan and fall, and the page comes up under the hand** — and it is still being pressed flat when the take ends.
- Pull: ⚠️ **The column is up and nobody has read it.** The shot ends there — **the first step of the carrying, stopped.**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - MOVEMENT 1 `0-1.6s` — density: `transition` — the closed register and the light on the cover: **the tube's light breathes once, dust crosses the desk, and the camera is already descending.** Nothing of the register has changed yet, and **the frame is not still** — this movement establishes the motion the whole take runs on.
  - MOVEMENT 2 `1.6-3.8s` — density: `sparse` — **the hand enters from the bottom of the frame** and the pads of the fingers find the cover's edge. One arrival, no hesitation; **the register has not opened yet.**
  - MOVEMENT 3 `3.8-8.059s` — density: `dense` — **the register opens.** The cover swings up, the leaves fan and fall one after another, the fore-edge rocks and settles, and **the page carrying the transfer column rises under the hand and is pressed flat — and is still settling on the last frame of the take.** ⚠️ **The cut arrives on that frame.** The page is not turned past the column.
- Temporal Density: **The weight of the take is at its end, in one long movement that does not stop before the cut.** ⚠️ **Eight seconds without a song, and the picture runs the whole way** — because the song's first line lands on the cut at 8.059s, and **a picture that has already stopped cannot receive it.** ⚠️ **There is no `held` movement in this shot.** Stillness here would be stillness of the *frame*, and this work's floor does not have one: **the subject holds or moves, and the light and the dust move either way.**

# 9. ACTION

- `ACT_ARRIVE` — Before: no hand is in frame. After: **the pads of the fingers are on the cover.** ⚠️ **The hand comes from below the frame; the arm is never shown to its source.**
- `ACT_OPEN` — Before: the register is closed. After: **the transfer column is up on the opened page.** ⚠️ **The register is opened, not read. Nothing is transported in this shot.**

# 10. CAMERA

- Camera Language: Third person, **close**, placed at the desk — **this work puts the camera at one of three sites** (run-10【ルックとカメラ】: 「カメラは、机上の手、左袖の名札、めくられる名簿の三箇所に置かれる」). This is the first of the three, and it is the work's first frame: the lens sits at desk height, looking slightly down at the cover.
- Camera Events: One event only. `0-8.059s` — **a slow, continuous descent**: the lens comes down toward the desk and slightly to the right, at a rate that does not change, and **it is still descending when the take ends.** ⚠️ **This is the descent the whole reading section runs on** — it begins here and no cut stops it, so `s02` and `s03` pick it up already in progress.
- Camera Behavior: No handheld, no whip, no shake. **No push-in on the page and no cut to the column.** ⚠️ **The camera does not stop before the cut** — the frame arrives at the register at the same moment the song arrives at its first line. No sudden zoom, no unnatural rotation. ⚠️ **The composition is allowed to change: the desk enters and the register grows in the frame as the lens comes down.** It never becomes a close-up of the column.

# 11. MOTION

## Subject Motion

**A right hand entering the frame from below, pressing the cover, and opening the register.** ⚠️ **It is the change this shot carries, and it is one change.** The wrist does not rotate; the movement is in the fingers and in the paper under them.

## Object Motion

**The cover, once** — it swings up. **The leaves, in sequence** — they fan and fall one after another, and the block rocks at the fore-edge until it settles. **The page, once** — it rises under the hand and is pressed flat, and **it is still settling on the last frame.** ⚠️ **Nothing is carried anywhere.**

## Environmental Motion

Dust moves in the air under the tube and catches the light. ⚠️ **Nothing about it stops when the hand does** — the dust goes on crossing, and the fore-edge of the page goes on breathing, through to the cut. ⚠️ **This is the layer the shot runs on**, not a decoration on a still.

## Physical Characteristics

- **Weight**: **Paper has little, and this work's paper is light** — the cover rises without resistance. ⚠️ **But light is not weightless: the pages have mass enough to fall and to rock the block, and the settle at the end of the take is that mass coming to rest.**
- **Inertia**: **The paper overshoots and settles.** ⚠️ **This reverses the previous version of this shot, which said `No overshoot and no settle`.** The leaves fall past their resting angle, the fore-edge rocks, and the hand presses the page back down — **and the take ends before that settles.**
- **Acceleration**: **The hand arrives at the rate it travelled at**; the paper does not — it falls faster than it is released and slows as it lands. ⚠️ **Two rates, one change.**
- **Fluidity**: Continuous; no snap, no held cel, no stutter. ⚠️ **There is no held frame anywhere in this take** — the opening 1.6 seconds are a movement of light and dust, not a still.
- **Impact**: **Two, and both soft**: the pads meeting the cover, and the block meeting the desk as the register opens. **Nothing else touches anything.**

# 12. EMOTION

- Emotional Arc: **The interval before the first movement** — the frame runs on dust and light until the hand arrives, and then does not stop for it.
- Emotional Events: ⚠️ **The event of this shot is not an expression.** It is the arrival itself — **the first time this work shows a hand** — and the shot does not celebrate it. **The emotion is in the flatness of the treatment: a first movement, given no more room than any other.**

# 13. LIGHTING

- Base Lighting: Fluorescent over a working desk at the end of the working day, with the style's bloom on the pale surfaces. The tube is above and behind the camera and the room's own light has not been switched off yet; outside there is nothing left to see. The paper is the brightest thing in the frame and the rest of the staff room has gone to deep cyan.
- Lighting Events: **None** — no lamp is switched, no shade moves, and the tube does not strike or fail. ⚠️ **But the light in the frame changes continuously**, and it changes because the subject moves: the cover carries a shadow off the desk as it rises, the fanned leaves pass the tube's light through themselves and throw moving edges across the page, and the hand's shadow arrives before the hand does. ⚠️ **This is not a lighting event; it is the consequence of the shot's one change**, and the previous version of this section called it "the light does not change once" — which was true only of a shot in which nothing moved.

# 14. AUDIO

- Dialogue: **None.** No line is spoken in this shot, and **no one is in it to speak one.** ⚠️ **This is not a silent shot** — see Sound Effects. ⚠️ **The work still speaks Japanese**; §18 names it.
- Sound Effects: **Paper, cloth and one soft contact.** The cover's board taking the pads of the fingers; the small dry sound of a page standing up on its edge; ⚠️ **and the absence of a voice** — nothing in this shot is called, and the absence is placed rather than left out. **Nothing is mixed forward.**
- Music: **None, by specification.** ⚠️ **This is not an omission** — §16 and §18 both carry the floor's `no background music`, and ⚠️ **on this route `No BGM` is one of the few negations that is actually received.** ⚠️ **And it matters more here than anywhere: the work's only music is the song 『誰の名』, placed in post over this shot** — a generated bed would put two songs on the same eight seconds. There is no bed, no score, no sting, and nothing rises at the cut.
- Environment: An empty staff room at the end of a working day. The tube's hum, a corridor, and the building's own quiet are permitted; a musical sting is not. **No calling voice as a sound effect** — and here there is no voice at all.

# 15. CONTINUITY

- Identity: **Must preserve** — the hand belongs to 碓氷千夏, whose setting sheet is frozen in `distill-essence-engine`; **this shot carries the hand and does not attach the sheet.** ⚠️ **The hand of this shot and the eyes and mouth of the next three are one person's.**
- Spatial: The register lies square to the desk's edge throughout; **the hand comes from below the frame and the frame does not open to show where from.** ⚠️ **Nothing is moved for the camera.**
- Temporal: The end of a working day, and **the same day as the twenty-six shots that follow.** **Nothing in frame supplies a date.**
- Visual: The fluorescent key, the palette and the dust are the same in all twenty-seven shots. **The light is the staff room's tube** — the work's four evening shots share it.
- Motion: Full animation, not limited. **The atmosphere is the primary mover**; the hand is the subject.
- Sound: Paper, cloth, one soft contact, and no music. **No calling voice as a sound effect.** ⚠️ **The song is not in this shot** — it goes on in post, and the shot is written silent so that the song has somewhere to land.
- ⚠️ **この27本は、すべて同じ経路である**（`SEEDANCE 2.5`）。**本編の三本（`MINIMAX H3`）とは別である。**⚠️ **ずれてはならないのは、人物と、パレットと、光である**——**プロンプトの字面ではない。**

# 16. CONSTRAINTS

## MUST NOT

- No legible text on any surface — not on the register, not on the address slip, not on the claim tag, not on the nameplate, not on the bundle. ⚠️ **These characters are on screen and none of them can be read.**
- No romaji in place of the Japanese name; no real-world alphabet in frame.
- **No blank surface where the writing should be, and no nonsense glyphs** — a surface with nothing on it and a surface with invented marks both fail, in opposite directions.
- No face before the name is called.
- No calling voice as a sound effect; no spoken line; no voice-over; no narration. ⚠️ **This shot has no dialogue** — see §14.
- No music of any kind in this shot. ⚠️ **On this route `No BGM` is one of the few negations that is actually received** — a bed arriving is a violation of this section, not a matter of taste.
- No on-screen subtitles, no captions, no burned-in subtitles in any language. ⚠️ **This route has an official notation for producing subtitles** (`【】`), which makes this clause more necessary here than on either of the other two routes.
- No watermark.
- No wall clock, no calendar, no digital timer, no date stamp.
- No uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion.
- No character added beyond the shot; no person the shot does not hold.
- No identifying clothing, hairstyle, or prop — **the people of this work are not told apart by what they wear.**
- No smile, no tears, no fear, no exaggerated expression.
- Not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces.
- **The face does not come into this shot.** No head, no shoulder, no standing figure behind the desk.
- **The register is not read.** No eye enters the frame, no head bends over the page, no finger tracks a line.
- **The page is not turned past the transfer column.** One opening, one page standing — **a second turn would make this a different shot.**
- No second object on the desk; no mug, no pen cup, no terminal, no stack.

## MUST

- **A closed register is opened by a hand, and the transfer column comes up.**
- **The hand arrives from below the frame and the arm is never followed to its source.**
- **The cover, the leaves and the page each move exactly once.**
- **The column is on screen and cannot be read.**
- ⚠️ **The change is still in progress on the last frame** — the page is settling when the take ends.
- ⚠️ **There is no still frame in this take.** Light and dust move in every one of its 193 frames; a frame in which the picture is frozen is a failure of this section.

## PREFER

- Desk height for the lens, with the register square in the frame and its closed edge toward the camera; the page standing as the frame's only diagonal.

## ALLOW

- The tube at the upper edge of the frame, blooming; dust in the air above the desk; the desk's worn edge in the near foreground.

# 17. GENERATION PRIORITIES

1. **A hand, before any face** — this shot is where the work's order is established. ⚠️ **If a face appears here, the order is broken for the whole work.**
2. **The register is openable and its writing is not readable** — both halves at once.
3. **The change is still happening on the last frame** — the page is still settling when the cut arrives. ⚠️ **A take that has finished moving before its cut hands the song a stopped picture.**
4. **One page, one lift, one hand** — nothing else happens. ⚠️ **One change is not one movement**: the dust, the light through the leaves, the rocking fore-edge and the descending camera are all moving underneath it, and they are what keeps this from being a still.
5. **Japanese is what this work speaks** — named in §18, even though this shot holds no words.
6. Everything else.

---

# 18. SEEDANCE 2.5 PROMPT MAPPING

⚠️ **この経路の §18 は、他の二つの経路と書き方が違う。** **時区分をプロンプトの中に書ける**（`0-3s:`）——
**ゆえに `Master Prompt` が、それ自体で一本の時間割を持つ。**
⚠️ **そして `Negative Prompt` を、この経路は床として受け取らない**（`specmap.MODEL_UNRECEIVED_SLOTS`）。
公式に否定として扱われるのは**字幕と音声だけ**である（`"No subtitles."` / `"No BGM"`）。
**残りは、ただの散文として読まれる。**
⚠️ **ゆえに禁制は二箇所に置く**——**ここの `Negative Prompt`**（**この作品が何を禁じるかの記録**。
⚠️ **この経路はこれを受け取らない**）と、**`Master Prompt` の散文**（**この経路が実際に読む側**）。
**同じことを二度書いているのではない。片方は床で、片方は助言である。**
⚠️ **`L30` がこれを鳴らす。** **それが正しい**——鳴らなければ、この経路の否定が床であるかのように読まれる。
**この作品は、それを承知で使うと宣言している**（`bible.route_limits_accepted` の
`SEEDANCE 2.5: Negative Prompt`）。**除外は作品の宣言であって、基盤の判断ではない。**
⚠️ **この節は27本で同一である。** 理由は `L10` にある——`disclosure` の3つの変化点が
`negative: covered`（**§18 は変わらない**）を宣言しており、**「覆った」は「同じである」を要求する。**
ゆえに**ショット固有の禁制はこの節に書かない**——それは `shot.forbidden_set`（引き渡しの層）が持つ。

## Master Prompt

An 8-second cinematic piece (16:9), luminous realist anime, at a desk in a school staff room at the end of a working day, 2026. One continuous take, one change: **a closed attendance register lying on the desk is opened by a hand, and the page carrying the transfer column comes up.** **No face is in this shot — the frame holds a desk, a closed book, and one hand.**

0-1.6s: the desk and the closed register. The cover is cloth over board, the thickness of a register's left sleeve; the page edge is layered cream at the fore-edge. **The register is not moving yet, and the frame is not still** — the fluorescent tube above breathes once, dust crosses the desk from left to right, and **the camera is already descending toward the desk.**
1.6-3.8s: **a right hand enters from the bottom of the frame** and the pads of the fingers find the cover's outer edge. The hand does not hurry and does not feel for the corner; it has done this before. **The register is still closed.** Dust lifts behind the wrist.
3.8-8.059s: **the register opens.** The cover swings up, the leaves fan and fall one after another, the fore-edge rocks and settles, and **the page carrying the transfer column rises under the hand** — **characters written in ink by more than one hand, present on screen and not readable.** The hand presses the page flat, **and the page is still settling on the last frame of the take.** The page is not turned further.
**The hand is a hand only: no head enters the frame, no shoulder, no standing figure, no second object on the desk.** **The writing on the page is present and cannot be made out — the characters are Japanese characters, set in the Japanese script, and they are not legible.** **This is a Japanese work.** No subtitles. No BGM.
(One continuous take, one change: the register is opened and the transfer column comes up.)

## Visual Prompt

Luminous realist anime, translated into a desk in a staff room at the end of the day: the light, not the figure, is the subject, and here it falls flat from a fluorescent tube across a closed cover. One hand only — the back of the hand, the knuckles, the nails, the cuff and no further; **no face, no head, no shoulder, no standing figure.** The register: cloth over board, the thickness of a register's left sleeve, a layered cream fore-edge, a bound spine. Its opened page carries the transfer column — **characters in ink, written by more than one hand, present and not readable.** The desk: a worn wooden surface with the polish of forearms on it, and nothing else on it. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp. Saturated where the light falls, deep cyan in everything the desk edge shadows; the palette narrow — fluorescent white, the grey-green of the cover, the cream of the page, and the warm side reduced to one hand. Bloom on the pale surfaces, dust suspended and individually rendered above the desk, generous negative space and low visual density.

## Motion Prompt

Full animation, not limited — the atmosphere does not idle. **A hand entering the frame from below and opening the register; the cover swinging up; the leaves fanning and falling one after another; the fore-edge rocking; the page rising under the hand and being pressed flat — and still settling at the end of the take.** ⚠️ **The pages have mass: they fall past their resting angle and rock to a stop, and the take ends before the stop is complete.** The hand's own rate does not change; the paper's does. Dust crosses the desk throughout and **the fore-edge of the page goes on breathing through to the last frame.** ⚠️ **No held frames, and no frame anywhere in the take in which the picture is still** — the opening seconds are a movement of light and dust, not a still. No motion blur smears, no stutter, no floaty weightless motion.

## Camera Prompt

Third person, close, placed at the desk — **at desk height, looking slightly down, so that the register is seen the way a person sitting at the desk would see it.** One camera event only: **a slow, continuous descent toward the desk and slightly to the right, at a rate that does not change, still running on the last frame of the take.** ⚠️ **The composition is allowed to change** — the desk enters the frame and the register grows in it. ⚠️ **Do not stop the move before the cut.** No push-in onto the column, no cut to an insert of it, no rack focus. No handheld, no whip, no shake, no sudden zoom, no unnatural rotation.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of everything this work holds. **No line is spoken in this shot: no one is in it to speak one, and there is no voice-over and no narration.** **The Japanese is not spoken here; it is what this work is** — and **nothing is written on screen**: no subtitles, no captions, in any language. Sound effects, nothing mixed forward: the cover's board taking the pads of the fingers, a page standing up on its edge, the hum of a fluorescent tube, a corridor. ⚠️ **And one absence, placed rather than left out: nothing in this shot is called** — no voice of any kind, and no sound that could be taken for one. **Music: none — this shot carries no music of any kind.** No bed, no score, no sting, no drum; ⚠️ **the song goes on in post, over this shot, and nothing else may be in the same place.** No calling voice as a sound effect.

## Negative Prompt

no watermark, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no swelling music, no drum, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no crowd, no face before the name is called, no legible name text, no legible text on any surface, no readable characters on any prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no identifying clothing, hairstyle, or prop, no character added beyond the shot, no additional person beyond the shot, no wall clock, no calendar, no digital timer, no date stamp, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no smile, no tears, no fear, no exaggerated expression, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-mv-s01-8.059s-01`
- Segment ID: `intro-1`
- Specification Version: `0.2.0`
- Generation Date: `2026-09-28`
- ⚠️ **版が `0.1.0` から動いた**（2026-09-28、運動の層の作り直し）。⛔ **`media/` に在る `01_…mp4` は `0.1.0` から出ている**
  （`takes/habits-mv-s01-video-1.yaml` の `params.source_version`）——**ゆえに `L25` の版の照合が、
  この1本と `s02`・`s03` で「投入 `0.1.0` → 現在 `0.2.0`」を言う。** **それが正しい。**
  **この3本は、いまの仕様の生成物ではない。**
- ⚠️ **日付の出所**: `media/` に置かれたファイルの mtime（2026-09-28 05:10）である——
  **投入した時刻そのものではない。** ⛔ **世代の記録は `takes/habits-mv-s01-video-1.yaml` に在る**——
  **この仕様は世代を写さない**（写した分は古びる）。

## Resolved Values

- Duration: `8.059s`
- References: `REF_CHARACTER (碓氷千夏 — **この1本には添付しない**) ／ REF_FORMAT (video-spec) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`
- Temporal Structure: `3 movements, NON_UNIFORM — 0-1.6s / 1.6-3.8s / 3.8-8.059s`. The held movement = `none`
- Camera Events: `1 event as listed in §10`
- Action Events: `ACT_ARRIVE → ACT_OPEN`
- Audio Events: `no dialogue ／ paper ＋ cloth ＋ one soft contact ＋ one placed absence ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.2.0` — **運動の層を作り直した**（2026-09-28）。**生成はまだ `0.1.0` の1本だけである。**
**採用は、まだ選ばれていない**——**選ぶのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。
⛔ **この節は仕様の側であって、世代の記録ではない**——**記録は `takes/habits-mv-s01-video-1.yaml` に在る。**

### `0.1.0` → `0.2.0`（2026-09-28）——運動の層

**規則「変化は、切れ目で終わる」を入れた。** 変わったのは §1・§7・§8・§10・§11・§12・§13・§17・§18 の五つのプロンプト・§19。
⛔ **変わった中身**:
- **末尾の `held`（`5.0-8.059s`）を `dense` に置き換えた。** 変化は切れ目のコマで終わる——
  **頁は、沈みきる瞬間に切れる。**
- **頭の `held`（`0-2.5s`）を `transition` に置き換えた。** 動かない2.5秒を、光と埃の1.6秒にした。
- **§10 のカメラを、止まらない降下にした。** 前の版は「数センチの重い沈み」で、
  **「何も明かさず、手を追わない」「構図を最後まで保つ」**と言っていた。
- **§11 の物理を直した。** 前の版は `No overshoot and no settle` / `Acceleration: None` だった——
  **紙が軽いことは、紙が止まることではない。**
- **§13 の「この1本で光は一度も変わらない」を撤回した。** 主題が動けば光は変わる。
- ⚠️ **§18 の `Negative Prompt` と `Style Motion` は1字も動かしていない**（`L10`）。

## Observed Problems

- ⛔ **解像度が食い違った** — §1 は `1920x1080`、戻ってきたのは `1280x720` である（**`L25` が鳴る。鳴るのが正しい**）。**フレームレート 24fps と尺は一致した**——外れたのはこの欄だけである。
- ⚠️ **手に、骨と腱が立ち、成人の手に見える。** ⛔ **この行は、初め「10代の女子の手として読めない」と書いてあった——その前提が誤りである。** `distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/prompt.md` の「出典の語」は `女33・会計年度任用職員（事務）` と言う。**成人の手であることは、それ自体では外れではない。** ⚠️ **外れかどうかを決めるのは「凍結した二枚の手と同じ手か」であり、それはこの層には読めない**——`migenzo` の実測に見えた外れ（「手が男性に読める」）は、**別の作品の、別の人物の話である。**
- ⚠️ **最後のコマで、頁が画面に対してほぼ垂直に立てられる** — §10 の「1つのカメラ事象」にこれを数えるかは、**未処理である。**
- ⚠️ **蛍光灯が枠の上辺で強く、青い** — **空は写っていない**が、この明るさは §13 の平坦な光より演出されている。**様式カードの空へ寄る力が、ここで最も強い。**
- ⛔ **上の「見たこと」は3コマから書いた**（2026-09-28）——**全コマを見ていない。** **絵を見る検査は、この基盤に無い。**
- ⚠️ **`L30` がこの仕様の上で鳴る** — §18 `Negative Prompt` に中身が在り、**この経路はその欄を床として受け取らない。**
  **§1–17 を直しても消えない。** この作品は**承知で使うと宣言している**
  （`bible.route_limits_accepted` の `SEEDANCE 2.5: Negative Prompt`）——**ゆえに `L30` は違反ではなく、名指された註になる。**
  ⚠️ **除外は作品の宣言であって、基盤の判断ではない。** **そして、宣言が言えるのはそこまでである**
  ——**その否定が実際に効いたかは、生成の外では見えない。**
- ⚠️ **この作品の27本のうち、3本（`s01`〜`s03`）が 2026-09-28 に生成器へ送られた**——
  **`takes/` に3本のテイクが在る。** ⚠️ **残る24本は、まだ1本も送られていない。**
  **`L6` が27本ぶん鳴りつづけるのは、それが理由である**——欄が無い場合は `no_record` として鳴る
  （`L6` は「**記録が無い**」と「**食い違い**」を混同しない）。
  ⛔ **`attached` は書いていない。** `attached` は「**実際に何が付いたか**」の欄であり、
  **著者が何を添付したかを、私は見ていない**——**推測で書けば、記録が測定になる。**

## Anticipated risks (to check in the first generation)

- **A face may be placed.** ⚠️ **The first risk of this shot, and the one this route is worst at.** The setting sheet is deliberately not attached, but a generator asked for a hand at a desk may supply a person. **A head in this frame breaks the work's order at its first step.** — the guard is the Master Prompt's own sentence, and it is weaker than it looks.
- **The register may come back with legible text.** The clause `no legible name text` sits in the slot this route reads as prose. **If the transfer column can be read, the work's premise is over.**
- **The page may not read as paper** — a plastic-looking page loses the work's physical law, which is that paper is light.
- **The hand may read as a stranger's** — a hand drawn without the sheet's joints and nails will not match the same person's eyes and mouth in `s02`–`s04`.
- **A second object may be added to the desk.** A mug, a pen cup or a terminal makes this shot about a workplace instead of about a register.
- **The opening 1.6 seconds may come back as a still.** ⚠️ **This is the failure the restructure was written against.** The beat is now `transition`, not `held`: the tube's light has to breathe, the dust has to be crossing, and **the camera has to be visibly descending.** ⛔ **A frozen opening is the same defect as a frozen ending** — it hands the cut a picture that is not moving.
- **The take may finish moving before its cut.** ⚠️ **The page has to still be settling at 8.059s.** If the register has come to rest and the hand has stopped, the song's first line lands on a stopped frame, and the shot is the shot it was before this version.
