# Seedance 2.5 Full Specification — 『ハビッツ！！！』主題歌MV『誰の名』 habits-mv-s03「口が、字の形をなぞって動く」 / 10.000s

⚠️ **この10.000秒は、この作品で最も長い「顔の一部」である。**
⚠️ **顔の一部を置くのは3本だけである**——`s02`（目・9.015秒）・`s03`・`s04`（口・7.155秒）。
**顔そのものを置くのは `s10`・`s24`・`s25` の3本である**（うち5人）。**混ぜて数えない。**
⚠️ **`l02`「口は、動く。」——音は出ない。** `bible.constants.音` が
「**呼び声ではなく、紙と手の音**」と定める以上、**口は動いても、声帯は動かない。**
⚠️ **この行の直後に、2.527秒の歌の無い間が在る**（27.074–29.601）。**その間は `s03` ではなく `s04` が吸う。**
**行が終わったところで、ショットも終わる。**（`ledger.song_coverage` の `l02` の註）

---

⛔ **この仕様は 2026-09-28 に運動の層を作り直した（`0.1.0` → `0.2.0`）。**
**規則——「変化は、切れ目で終わる。」** ⚠️ **この1本の切れ目（27.074）は、行の頭ではない**——
**実測で、26の切れ目のうち行の頭でないのは2つだけであり、これがその一つである。**
これは `l02` が**終わる**点であり、**そのあと 2.527秒、歌が無い。**
⛔ **それでも切れ目は曲の事象である**——*息が切れる点*であり、**置いたのはこの作品ではない。**
⛔ **前の版は、そこへ 3.9秒の静止で入っていた。**
`held` 3.4 → `dense` 2.7 → `held` 3.9。**唇の動きは 23.174秒に終わり、切れ目は 27.074秒。**
**27本のうち、末尾の `held` がこれより長いのは `s27`（7.309秒）だけである。**
⚠️ **いまは、最後の字の形が切れ目のコマで閉じきる。**
⚠️ **土台は動いていない。** `shot-record.schema.json` の `motion` の註——
**「止まるのは主題であって、画面ではない。光と粉塵は動く。」**——を、前の版は
「音が出ないことは、画面が止まること」と読んでいた。**そこだけを直した。**
⚠️ **`§18` の `Negative Prompt` と `Style Motion` は1字も動かしていない**（`L10`）。

---

# 1. VIDEO

- Duration: `10.000s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take of one change — **a mouth moves through the shapes of characters and closes without making a sound.** ⚠️ **The shot is about a mouth that is forming a name and not reaching a voice**, and the sound of the shot is the sound of the room, not of the mouth. ⚠️ **The last shape closes on the last frame of the take** — the mouth is still moving when the cut arrives — and **the frame is never still under it**: the page is finishing its settle, dust crosses the lit page, and the camera is descending from the first frame to the last.

# 2. WORLD

## World Concept

2026, Japan. Kawaguchi in Saitama, Adachi in Tokyo, Totsuka in Yokohama — and in this shot, the same desk, the same page, the same person's mouth. There is no magic, no institution and no secret organization: there is only a daily life in which the etiquette of the written name is thoroughly in place. **The name is the subject of this work, and the name this work is about is the one that is read the wrong way** — which is why every name on every in-world prop is printed or written and nowhere legible. ⚠️ **This is a theme-song music video:** one song of 179.320 seconds, twenty-seven shots, no episode — **the work does not advance a story. It holds one question and asks it again with other hands.**

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

- Art Direction: Luminous realist anime, translated into the lower half of a face above a page. **The light, not the figure, is the subject** — and here it comes from above, so the mouth's own shadow is under the lower lip and the page below is brighter than the face.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The palette narrows to skin, page and ink; **the mouth is the only place in the frame where the palette has any red in it at all.**
- Texture: Layered atmospheric depth from near to far; dust suspended where the tube catches it. Skin is drawn smooth and matte, without pores or specular noise. No grain overlay, no painterly stroke.
- Rendering: Clean anime lineart on the figure, drawn at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — **no second tone inside one piece of cloth, no gradient inside a single material, no soft airbrush.** ⚠️ **The written name is drawn as the resolution it is** — cut, printed, ballpoint and pencil are four different marks, not one texture applied four times.
- Visual Density: Low. One focal point — the mouth and the line of writing below it — with the rest of the frame given to page and to the shadow under the lip.
- Time: `勤務日の夕方` — the end of a working day, indoors, at the same desk as the shot before and the shot after.
- Atmosphere: A mouth shaping a name it is not going to say, over a page nobody is watching.

# 3. SUBJECTS

## 碓氷千夏の口

- Reference: the frozen setting sheet — `distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/ChatGPT Image 2026年9月18日 20_29_36.png` ＋ `.../ChatGPT Image 2026年9月17日 21_56_32.png` （表情シート）.
- Appearance: **凍結した二枚が外見である。** ⚠️ **この1本が置くのは口の側だけである** — 上唇と下唇、口角、顎の下の影、そして唇の内側の暗さ。**息は出るが、声帯は動かない。**
- Behavior: **字の形が、唇に一度ずつ現れては消える。** ⚠️ **途中で止まり、また始まる** — 全部を続けてなぞらない。**一度も音にならない。**
- Continuity Requirements: **Must preserve** — 凍結した二枚の顔、`s02` の目と同じ人物であること。**May change** — 何も変えない。⚠️ **この口は `s04` で止まる。その止まり方が `s04` の主題である。**

## nobody

- **この1本に、二番目の人物は居ない。** **呼ばれる者も、呼ぶ者も出ない。**

# 4. ENVIRONMENT

- Location: `出席簿の転出欄` — the same site — **the page, seen from the side of the face.** ⚠️ **この1本は頁と口の外へ出ない。**
- Environment Elements: 机の上、開かれた頁、そして口の下の影。**この1本は、頁の明るさと、唇の下の暗さの二つでできている。** ⚠️ **部屋は要らない。**
- Environmental Behavior: 埃が頁の上を渡る。**頁は動かない。** ⚠️ **口が閉じたあとも、埃と頁の光は動き続ける。**

# 5. OBJECTS

- **開かれた頁と、その一行** — `s02` と同じ頁である。**読めない。**
- **唇** — 動くが、音を出さない。
- **机の面** — 頁の外側にわずかに見える。
- No other object is in frame. ⚠️ **この1本には手が入らない** — 手は `s01` で置かれ、`s11` で戻る。

# 6. REFERENCES

- REF_CHARACTER: 碓氷千夏 — `distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/ChatGPT Image 2026年9月18日 20_29_36.png` ＋ `distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/ChatGPT Image 2026年9月17日 21_56_32.png` (CRITICAL). **この1本は `identity` を添付する** — 口を置く1本である。⚠️ **表情シートを添付する意味が、この1本で最も大きい**：口は表情の側にある。
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

- Core Event: **A mouth moves through the shapes of characters and closes without making a sound.**
- Beginning: The mouth is shut and the page below it is lit — and the page is still moving: it is finishing the settle it began in `s01`, dust is crossing it, and the camera is still coming down.
- Turn: **The shapes begin** — one character at a time appearing on the lips and going.
- Peak: **It stops part-way and starts again** — the mouth does not carry the whole name through, **and it does not finish early either: the last shape is still being closed when the take ends.**
- Pull: ⚠️ **The lips close and nothing has been said.** The shot ends on the absence of a voice.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - MOVEMENT 1 `0-1.8s` — density: `sparse` — the closed mouth and the light on the page below it. **The mouth is shut** — this movement belongs to the paper, **and the paper is moving**: the page is finishing its settle, dust crosses the lit surface, and the camera's descent continues. Nothing of the mouth has changed.
  - MOVEMENT 2 `1.8-10.000s` — density: `dense` — **the shapes of characters appear on the lips, one after another, without a gap**, and go. **The breath is audible as air, not as a voice.** The sequence stops part-way and starts again, **and it is still running when the take ends: the last shape closes on the final frame.** ⚠️ **The lips do not stop before the cut** — the page settles beneath them, the dust goes on crossing, and the camera never finishes its descent.
- Temporal Density: **The take is one long movement of the lips that does not stop before the cut.** ⚠️ **The previous version of this section put the movement in the middle and the silence on both sides of it** — `held` 3.4s, `dense` 2.7s, `held` 3.9s. ⛔ **The second silence was the defect**: the lips finished at 23.174s and the cut was at 27.074s, so **3.9 seconds of stopped picture held under a song that had stopped singing.** ⚠️ **Silence in the mouth is not stillness in the frame.** There is no `held` movement in this shot.

# 9. ACTION

- `ACT_SHAPE` — Before: the mouth is closed. After: **the shapes of characters have crossed the lips, one at a time, and gone.** ⚠️ **No voice is produced. The breath is air only.**
- `ACT_SILENCE` — Before: the shapes are still coming. After: **the lips are closed and nothing has been said.** ⚠️ **This is the change of the shot** — the silence is not the absence of an action, it is the action's result.

# 10. CAMERA

- Camera Language: Third person, **close**, at the lower half of the face — **the same desk placement as the two shots before it, held a little higher so that the mouth and the page are in one frame.**
- Camera Events: One event only. `0-10.000s` — **the descent begun in `s01` continues**: the lens keeps coming down and slightly right, at a rate that does not change, and **it is still descending on the last frame of this take.**
- Camera Behavior: No handheld, no whip, no shake. **No cut to the mouth and no push-in on it** — the mouth is read from the same frame the page is read from. ⚠️ **But the camera is not parked**: the page and the mouth both grow slowly as the lens comes down, and **the camera arrives with the last shape.** ⚠️ **The camera does not stop before the cut.** It never becomes a close-up of the mouth alone.

# 11. MOTION

## Subject Motion

**A mouth moving through the shapes of characters without a gap, stopping part-way, starting again, and closing on the last frame of the take.** ⚠️ **It is the change this shot carries, and it is one change.** The jaw moves very little; the work is done by the lips. The eyes are not the subject of this shot and do not lead it. **The last movement is the lips closing — and it is not finished before the take is.**

## Object Motion

**The page finishes settling** — the fore-edge lifts once and comes down and stays, early in movement 1. The writing does not change. ⚠️ **What moves across the page for the rest of the take is light**, and it moves as the lens comes down.

## Environmental Motion

Dust moves over the page and catches the tube, crossing the lit surface throughout. ⚠️ **None of it stops when the lips close** — the dust is still crossing on the last frame. ⚠️ **And the breath is visible**: air leaving the lips moves the dust immediately in front of the mouth, faintly and continuously, for the whole of movement 2.

## Physical Characteristics

- **Weight**: **None in the mouth.** ⚠️ **The shot's physical law is that the breath carries nothing** — air passes the lips and no voice is made of it. ⚠️ **What weight there is belongs to the page**, which is coming to rest under its own.
- **Inertia**: The shapes start and stop **without ease** — the lips are not winding up to a word and not recovering from one. ⚠️ **The one exception is the last shape**, which is closing when the take ends and therefore has no settle to show.
- **Acceleration**: **Each shape takes the same time as the one before it** — the rhythm is even **and the rhythm is not a beat**: the shapes do not line up with anything. ⚠️ **The page's rate does change**: the fore-edge rocks down and slows as it comes to rest.
- **Fluidity**: Continuous; the shapes are drawn, not posed. ⚠️ **No shape is held for the camera** — each appears and goes. ⚠️ **And there is no gap between them**: the mouth is in motion for the whole of movement 2.
- **Impact**: **None.** Nothing in this shot touches anything.

# 12. EMOTION

- Emotional Arc: **The whole distance between forming a name and saying it** — kept in motion for ten seconds and cut off on the near side.
- Emotional Events: **The restart.** ⚠️ **The shot's event is that the mouth begins again after stopping** — **not that it succeeds.** The emotion is in the repetition, and the shot does not comment on it. ⚠️ **The take ends on the closing shape rather than after it**, so the shot does not show the mouth at rest either.

# 13. LIGHTING

- Base Lighting: Fluorescent over a working desk at the end of the working day, with the style's bloom on the pale surfaces. The tube is above and behind the camera and the room's own light has not been switched off yet; outside there is nothing left to see. The paper is the brightest thing in the frame and the rest of the staff room has gone to deep cyan.
- Lighting Events: **None** — no lamp is switched and the tube does not strike or fail. ⚠️ **A change of light as an event would be read as a change of resolve.** ⚠️ **But the light in the frame moves throughout**: the mouth's own shadow shifts on the page beneath it as the lips form each shape, dust crosses the beam, and the lit edge of the ruling slides right as the lens comes down.

# 14. AUDIO

- Dialogue: **None, and this shot is where that is decided.** ⚠️ **The mouth moves and no line is spoken** — `bible.constants.音` puts the work's sound in paper and hands, and a voice here would make every later silence in the work a different silence. **The work still speaks Japanese**; §18 names it.
- Sound Effects: **Air, paper, and nothing else placed.** The breath passing the lips, audible as air and not as a voice; the small sound of a page under a still room; ⚠️ **and the absence of the voice the mouth is shaping** — **the shot's loudest element is the thing it does not make.**
- Music: **None, by specification.** ⚠️ **On this route `No BGM` is one of the few negations that is actually received** (§18), and ⚠️ **the song is placed in post over this shot.** ⚠️ **A bed here would give the mouth a voice it does not have.**
- Environment: A staff room at the end of a working day. The tube, a corridor, the building. **No calling voice as a sound effect** — and here there is no voice at all.

# 15. CONTINUITY

- Identity: **Must preserve** — the same face and the same person as `s01` and `s02`; the setting sheet and the expression sheet are both attached. **May change** — nothing.
- Spatial: The page stays square to the frame and the mouth stays above it. ⚠️ **Nothing is moved for the camera.**
- Temporal: The same working day, after `s02`. **Nothing in frame supplies a date.**
- Visual: The same fluorescent key, the same palette, the same dust as all twenty-seven shots.
- Motion: Full animation, not limited. **The atmosphere is the primary mover**; the mouth is the change. ⚠️ **The atmosphere does not stop when the lips do** — the page settles, the dust crosses, and the camera descends through to the cut.
- Sound: Air, paper, no voice, no music. **No calling voice as a sound effect.** ⚠️ **No sound is not no motion** — the breath is visible in the dust in front of the mouth, and the mouth never stops moving inside this take.
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
- **No voice, no whisper, no breath that becomes a word.** ⚠️ **The lips move and the vocal folds do not** — this is the shot.
- **The mouth does not smile and does not tighten.** No expression is placed on it.
- **The eyes are not the subject of this shot** — they do not lead, and they do not move to the line.
- **No hand enters this shot.** The hand belongs to `s01` and returns in `s11`.

## MUST

- **The shapes of characters cross the lips without a gap, stop, and start again.**
- **No sound is produced by the mouth** — the breath is air and nothing more.
- **The last shape closes on the last frame of the take** — the mouth is still moving when the cut arrives.
- ⚠️ **There is no still frame in this take.** The page, the dust, the light on the ruling and the camera move in every one of its 240 frames.

## PREFER

- The mouth in the upper third and the page below it, so that the shapes are made **above** the writing they belong to and never touch it.

## ALLOW

- Dust over the page; the shadow under the lower lip; the uneven ruled columns of the page.

# 17. GENERATION PRIORITIES

1. **The mouth moves and there is no voice** — either half failing loses the shot. ⚠️ **This is the shot the work's whole sound design rests on.**
2. **The shapes stop part-way and begin again** — a mouth that carries the whole name through in one pass is a different shot.
3. **The lips close on the last frame**, and the closing is the change. ⚠️ **A mouth that has finished and is waiting hands the cut a stopped picture** — which is what the previous version of this shot did for 3.9 seconds.
4. **No expression** — a smile or a tightened mouth makes this a reaction.
5. ⚠️ **No sound is not no motion** — the page settles, the dust crosses, the light on the ruling slides and the camera descends for all ten seconds.
6. **Japanese is what this work speaks** — named in §18, even though this shot holds no words.
7. Everything else.

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

A 10-second cinematic piece (16:9), luminous realist anime, on the lower half of a face above an opened register page at the end of a working day, 2026. One continuous take, one change: **a mouth moves through the shapes of characters, stops part-way, begins again, and closes without making a sound.**

0-1.8s: the closed mouth and the light lying on the page below it. **The lips are shut, and the page below is not** — it is finishing a settle of its own, its fore-edge lifting once and coming down; dust crosses the lit surface from left to right, and **the camera is already descending toward it.**
1.8-10.000s: **the shapes of characters appear on the lips, one after another without a gap, and go.** The breath passes as air and **no voice is made of it** — and it is visible: it moves the dust immediately in front of the mouth. The jaw moves very little and the work is done by the lips. The sequence **stops part-way and begins again**, and **the last shape closes on the final frame of the take** — the mouth is still moving when the shot ends. The page below is unchanged, **and the characters on it still cannot be made out.**
**The mouth moves and no sound comes out of it: no voice, no whisper, no breath that becomes a word, and no line is spoken in this shot.** **No expression is placed on the mouth and no hand enters the frame.** **The writing on the page is present and cannot be made out — the characters are Japanese characters, set in the Japanese script, and they are not legible.** **This is a Japanese work.** No subtitles. No BGM.
(One continuous take, one change: the mouth closes and nothing has been said.)

## Visual Prompt

Luminous realist anime, translated into the lower half of a face above a page at the end of the day: the light, not the figure, is the subject, and here it comes from above so that the mouth's own shadow sits under the lower lip and the page below is brighter than the face. Lips, mouth corner, chin, and the shadow they cast; **the eyes are not the subject of this shot and are not detailed.** The page below carries characters written in ink by more than one hand — **present and not readable.** Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp. Saturated where the light falls, deep cyan in the unlit half; the palette narrows to skin, page and ink, and **the mouth is the only place in the frame with any red in it.** Bloom on the pale page, dust suspended and individually rendered, low visual density.

## Motion Prompt

Full animation, not limited — the atmosphere does not idle. **A mouth forming the shapes of characters without a gap, stopping part-way, beginning again, and closing on the final frame of the take.** The jaw moves very little and the lips do the work; **no sound is produced and the breath is air only** — and the breath is visible, moving the dust in front of the mouth. The shapes are drawn and not posed — **no shape is held for the camera**, and there is no gap between them: **the mouth is in motion for the whole of the shot.** The eyes do not lead and the head does not tilt. ⚠️ **The page, the light on the ruling, the dust and the camera move throughout**, and none of them stops when the lips do: the fore-edge of the page rocks down and comes to rest early, dust crosses the lit surface, **and the camera is still descending on the last frame.** ⚠️ **No held frames and no still frames anywhere in this take.** No impact, no motion blur smears, no stutter.

## Camera Prompt

Third person, close, at desk height looking slightly down — the same placement as the two shots before, held so that the mouth and the page are in one frame. One camera event only: **the slow descent begun two shots earlier continues toward the page and slightly to the right, at a rate that does not change, and it is still running on the last frame of the take.** ⚠️ **Do not stop the move before the cut**, and **do not push in on the mouth and do not cut to it** — the mouth is read from the same frame the page is read from. ⚠️ **The page and the mouth may grow in the frame as the lens comes down, but it never becomes a close-up of the mouth alone.** No handheld, no whip, no shake, no sudden zoom, no unnatural rotation.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of everything this work holds. ⚠️ **This shot is the one that decides what this work sounds like: the mouth moves and no line is spoken** — no voice, no whisper, no breath that becomes a word, and no voice-over and no narration. **The Japanese is not spoken here; it is what this work is** — and **nothing is written on screen**: no subtitles, no captions, in any language. Sound effects, nothing mixed forward: the breath passing the lips as air, a page under a still room, the hum of the tube, a corridor. ⚠️ **And one absence, placed rather than left out: the voice the mouth is shaping does not come** — and the shot's loudest element is the thing it does not make. **Music: none — this shot carries no music of any kind.** No bed, no score, no sting, no drum; ⚠️ **a bed would give the mouth a voice it does not have, and the song goes on in post over this shot instead.** No calling voice as a sound effect.

## Negative Prompt

no watermark, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no swelling music, no drum, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no crowd, no face before the name is called, no legible name text, no legible text on any surface, no readable characters on any prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no identifying clothing, hairstyle, or prop, no character added beyond the shot, no additional person beyond the shot, no wall clock, no calendar, no digital timer, no date stamp, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no smile, no tears, no fear, no exaggerated expression, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-mv-s03-10.000s-01`
- Segment ID: `pre-chorus-1-2`
- Specification Version: `0.2.0`
- Generation Date: `2026-09-28`
- ⚠️ **版が `0.1.0` から動いた**（2026-09-28、運動の層の作り直し）。⛔ **`media/` に在る `03_…mp4` は `0.1.0` から出ている**
  （`takes/habits-mv-s03-video-1.yaml` の `params.source_version`）——**ゆえに `L25` の版の照合が
  「投入 `0.1.0` → 現在 `0.2.0`」を言う。** **それが正しい。この1本は、いまの仕様の生成物ではない。**
- ⚠️ **日付の出所**: `media/` に置かれたファイルの mtime（2026-09-28 05:20）である——
  **投入した時刻そのものではない。** ⛔ **世代の記録は `takes/habits-mv-s03-video-1.yaml` に在る**——
  **この仕様は世代を写さない**（写した分は古びる）。

## Resolved Values

- Duration: `10.000s`
- References: `REF_CHARACTER (碓氷千夏 — 設定画＋表情シート, CRITICAL) ／ REF_FORMAT (video-spec) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`
- Temporal Structure: `2 movements, NON_UNIFORM — 0-1.8s / 1.8-10.000s`. The held movement = `none`
- Camera Events: `1 event as listed in §10`
- Action Events: `ACT_SHAPE → ACT_SILENCE`
- Audio Events: `no dialogue ／ air ＋ paper ＋ one placed absence ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.2.0` — **運動の層を作り直した**（2026-09-28）。**生成はまだ `0.1.0` の1本だけである。**
**採用は、まだ選ばれていない**——**選ぶのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。
⛔ **この節は仕様の側であって、世代の記録ではない**——**記録は `takes/habits-mv-s03-video-1.yaml` に在る。**

### `0.1.0` → `0.2.0`（2026-09-28）——運動の層

**規則「変化は、切れ目で終わる」を入れた。** 変わったのは §1・§7・§8・§10・§11・§12・§13・§15・§16・§17・§18 の三つのプロンプト・§19。
⛔ **変わった中身**:
- **末尾の `held`（`6.1-10.000s`）を消した。** 最後の字の形が、切れ目のコマで閉じきる。
- **頭の `held`（`0-3.4s`）を `sparse` に置き換えた。** 頁はまだ沈んでいる。
- **「形は一つずつ」を「隙間なく」に直した。** 前の版は形と形のあいだに間が在り、
  **その間が静止として読まれる**——**音が無いことは、唇が止まることではない。**
- **息を、見えるようにした。** 唇の前の埃が動く。`bible.constants.音` の「紙と手の音」を、ここで視覚の側から負う。
- **§11 の「Object Motion: None」を撤回した。** 頁は沈み、光は滑る。
- **§10 のカメラを、`s01` から続く止まらない降下にした。**
- ⚠️ **§18 の `Negative Prompt` と `Style Motion` は1字も動かしていない**（`L10`）。

## Observed Problems

- ⛔ **この1本の §20 の1番目が、そのまま起きた** — 「**The writing may be rendered legible.** ⚠️ **The first risk of this shot, and on this route the one the `Negative Prompt` cannot stop.**」 **実測が、それを裏づけた。**
- ⛔ **左の頁の手書きが、ラテン文字の草書として戻った** — 日本語の字ではない。§18 は `no real-world alphabet` を**既に持っていた**——**この経路では散文として読まれた**（`L30`）。
- ⛔ **右の頁の印刷が、読める日本語で戻った** — `転` `出` の見出しと、`1`〜`10` の行数字。§18 は `no legible text on any surface` / `no legible name text` を持っていた。⚠️ **そして、この作品の凍結した設定画にも、同じ印刷の見出しと行数字が在る**（設定画 ⑨ を実測、2026-09-28）——**参照集合と禁制集合が、ここで衝突している。** ⛔ **どちらを正とするかは著者の裁定である**（私の判断で直していない）。
- ⛔ **解像度が食い違った** — §1 は `1920x1080`、戻ってきたのは `1280x720` である（**`L25` が鳴る。鳴るのが正しい**）。
- ✅ **衣装は凍結した設定画と一致した** — 白いシャツ、襟のV、紺の紐が二本。⚠️ **私は一度これを「紺のセーラー襟」と読み違え、2倍に切って読み直した。**
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

- **A voice may be produced.** ⚠️ **The first risk of this shot, and the one that would cost the work most.** A generator asked for a moving mouth will often supply audible speech or a whisper. **`no calling voice as a sound effect` is in the slot this route reads as prose** — the guard is the Master Prompt's own sentence.
- **The writing may become legible**, and then the shot becomes a shot about reading aloud.
- **The mouth may smile or tighten** — an expression turns the shot into a reaction, and the work does not react here.
- **The shapes may run straight through** without stopping, which loses the restart — and the restart is the shot's event.
- ⛔ **The mouth may finish early and wait.** ⚠️ **This is the failure the restructure was written against.** The take is 10.000s and the last shape has to be closing at 10.000s — **a mouth that closes at 6s and holds hands the cut a stopped picture**, which is what the previous version of this shot did for 3.9 seconds.
- **The page may come back as a still.** Movement 1 is `sparse`, not `held`: the fore-edge has to still be settling, dust has to be crossing, and the camera has to be visibly descending. ⛔ **A frozen opening is the same defect as a frozen ending.**
- **The camera may be parked.** ⚠️ The descent has to still be running at 10.000s.
- **The eyes may take over.** ⚠️ **This shot is the mouth's**; an eye leading the frame makes it a duplicate of `s02`.
- **A hand may enter the frame** and make this a gesture instead of a silence.
- **Music may be placed anyway**, which would give the mouth a voice by the back door.
