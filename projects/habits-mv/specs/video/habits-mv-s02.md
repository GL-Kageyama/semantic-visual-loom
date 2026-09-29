# ═══ 演出要約 ════════════════════════════════════
# 『ハビッツ！！！』主題歌MV『誰の名』 pre-chorus-1「出席簿の転出欄」 / 反応 / motion —— 目で、読む。
#
#   まだ誰も読んでいない頁の上を、目が左から右へ渡り、行の終わりで着く。
#   9.015秒を、前半は目を入れずに使い、目は一度も止まらずに渡る——行末に着くのが、切れ目のコマである。
#   眉も口も動かず、目は字を追うだけで読まない——頁の下では、埃と光の縁が止まらない。
# ═════════════════════════════════════════════════

# Seedance 2.5 Full Specification — 『ハビッツ！！！』主題歌MV『誰の名』 habits-mv-s02「目が、一行を左から右へ渡る」 / 9.015s

⚠️ **この9.015秒は、この作品で2番目に顔を置く場所である** — `s01` が手を先に置いたので、
ここは順序の2番目である。**顔ではなく、目の側から。**
⚠️ **`l11` の「振り向く」（`s10`）まで、この作品は顔を置かない。** 置くのは**目**である。
⚠️ **`l01`「目で、読む。」** — 歌が「目で」と言う以上、**画面は目でなければならない。**
⚠️ **行の尺が揃っていない節である**（9.015 / 10.000 / 7.155）。**切れ目は行の頭だけである。**

---

⛔ **この仕様は 2026-09-28 に運動の層を作り直した（`0.1.0` → `0.2.0`）。**
**規則——「変化は、切れ目で終わる。」** この作品の切れ目は曲が置いたものであり、
実測で **26の切れ目のうち24が歌詞の行の頭と 20ms 以内で一致する**——
**この1本の切れ目は 17.074秒、`l02`「口は、動く。」の頭である。**
⛔ **前の版は、いちばん酷かった。** `held` 3.0 → `dense` 3.2 → `held` 2.815。
**目の横断は 14.259秒に終わり、切れ目は 17.074秒**——**2.815秒のあいだ、
画面は止まったまま、歌が「口は、動く。」と言っていた。**
⚠️ **「行末で止まる」という変化は正しい。間違っていたのは、止まる場所である。**
**いまは、目が行末に着くのが切れ目のコマである。**
⚠️ **そのため、まばたきをこの1本から外した**——**止まったあとが無くなり、切れ目がその位置を占める。**
⚠️ **土台は動いていない。** `shot-record.schema.json` の `motion` の註——
**「止まるのは主題であって、画面ではない。光と粉塵は動く。」**——を、前の版は
「動くのは目だけ」と読んでいた。**そこだけを直した。**
⚠️ **`§18` の `Negative Prompt` と `Style Motion` は1字も動かしていない**（`L10`）。

---

# 1. VIDEO

- Duration: `9.015s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take of one change — **an eye crosses a single line of writing from left to right and comes to rest on the last character of it.** ⚠️ **The eye is the only thing that changes**: the brow, the mouth and the head are held, so that the work's second step is still not a face but a part of one. ⚠️ **The crossing ends on the last frame of the take** — the stop and the cut are the same instant — and **the frame under the eye is never still**: the page is still settling from the shot before, dust crosses it, the lit edge of the ruling slides, and the camera is descending from the first frame to the last.

# 2. WORLD

## World Concept

2026, Japan. Kawaguchi in Saitama, Adachi in Tokyo, Totsuka in Yokohama — and in this shot, the same desk and the same opened register, minutes later. There is no magic, no institution and no secret organization: there is only a daily life in which the etiquette of the written name is thoroughly in place. **The name is the subject of this work, and the name this work is about is the one that is read the wrong way** — which is why every name on every in-world prop is printed or written and nowhere legible. ⚠️ **This is a theme-song music video:** one song of 179.320 seconds, twenty-seven shots, no episode — **the work does not advance a story. It holds one question and asks it again with other hands.**

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

- Art Direction: Luminous realist anime, translated into the opened page of a register at the end of a working day. **The light, not the figure, is the subject** — and here the light lies along the ruled lines of a page, and the only thing crossing it is an eye.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The palette narrows to the page — cream, ruling grey, ink black, and the pale of an eye. **Almost the whole frame is paper.**
- Texture: Layered atmospheric depth from near to far; dust suspended where the tube catches it. The page's fibre and the ink's absorption are both visible at this distance. No grain overlay, no painterly stroke.
- Rendering: Clean anime lineart on the figure, drawn at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — **no second tone inside one piece of cloth, no gradient inside a single material, no soft airbrush.** ⚠️ **The written name is drawn as the resolution it is** — cut, printed, ballpoint and pencil are four different marks, not one texture applied four times.
- Visual Density: **Very low.** One focal point — the line of writing and the eye above it — with the rest of the frame given to blank paper.
- Time: `勤務日の夕方` — the end of a working day, indoors, at the same desk as the shot before and the shots after.
- Atmosphere: A page that is being read and not being understood, and nobody watching it.

# 3. SUBJECTS

## 碓氷千夏の目

- Reference: the frozen setting sheet — `distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/ChatGPT Image 2026年9月18日 20_29_36.png` ＋ `.../ChatGPT Image 2026年9月17日 21_56_32.png` （表情シート）＋ `.../碓氷千夏_キービジュアル.png`（註の無い一枚）。⚠️ **この三枚目は、凍結した二枚を組み直したものではない**（2026-09-28 著者作成）——**註の字を持たない一枚である。この作品の画面は字が読めてはならない。** **All three are the source of this work's 碓氷千夏; the face is theirs and is not re-derived here.**
- Appearance: **外見の記述は出典に一行も無い**（方針 §5a）。**凍結した二枚が外見である。** ⚠️ **この1本が置くのは目の側だけである** — 眉、まぶた、睫毛、眼球の動き、そして行の上の光。**顔の残りは、この1本では主題ではない。**
- Behavior: **視線が字を追い、行末で止まる。** ⚠️ **眉も口も動かさない** — **動くのは目だけである。** まばたきが一度だけ、行末のあとに来る。
- Continuity Requirements: **Must preserve** — 凍結した二枚の顔。**May change** — 何も変えない。⚠️ **`s03` の口と `s04` の停止は、この同じ顔の続きである。**

## nobody

- **この1本に、二番目の人物は居ない。** ⚠️ **話し相手も、呼ぶ者も出ない。**

# 4. ENVIRONMENT

- Location: `出席簿の転出欄` — the same site as the shot before — **the register's opened page**, and nothing of the room beyond it.
- Environment Elements: 机の上。**開かれた頁。** 罫線、欄、書かれた字、頁の小口。⚠️ **この1本は頁と目の外へ出ない。** 部屋は背景の深いシアンとしてだけ在る。
- Environmental Behavior: 埃が頁の上を渡る。**頁は動かない。** ⚠️ **目が止まったあとも、埃と、頁の上の光の縁は動き続ける。**

# 5. OBJECTS

- **開かれた頁と、その一行** — 欄に沿って書かれた字。**複数の筆跡が混じっている。** ⚠️ **読めない。**
- **罫線** — 印刷された細い線。**欄の幅は均一でない**（手で書かれた字が、欄からはみ出している箇所がある）。
- **机の面** — 頁の外側にわずかに見える。
- No other object is in frame.

# 6. REFERENCES

- REF_CHARACTER: 碓氷千夏 — `distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/ChatGPT Image 2026年9月18日 20_29_36.png` ＋ `distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/ChatGPT Image 2026年9月17日 21_56_32.png` ＋ `distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/碓氷千夏_キービジュアル.png` (CRITICAL). **この1本は `identity` を添付する** — 目を置く1本である。⚠️ ただし**顔の全部ではない**：凍結した二枚のうち、**目の側がこの1本の主題である。** ⚠️ **三枚目を加えた**（2026-09-28）——**凍結した二枚は改訂の箱と引き出し線の註を持ち、この作品の画面は字が読めてはならない**（`no legible text on any surface`）。**註の字を持たない一枚を、参照の側に置く。**
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

- Core Event: **An eye crosses one line of writing and stops at the end of it.**
- Beginning: The page is open, the light is on it, and **the eye is not yet in the frame.**
- Turn: **The eye enters and takes the line** — left to right, once, without slowing.
- Peak: **It reaches the end of the line and comes to rest on the last character** — and what it has read is still not readable.
- Pull: ⚠️ **It stops, and nothing is done about what it stopped on.** **The take ends on that instant** — the stop is not a movement that finishes early and waits; **it is the last thing that happens.**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - MOVEMENT 1 `0-2.2s` — density: `sparse` — the opened page, still settling from the shot before. **The eye is not in the frame yet.** ⚠️ **This movement belongs to the paper, and the paper is moving**: the fore-edge is still breathing off the block, dust crosses left to right and against it, and the lit edge of the ruling slides as the camera comes down. Nothing of the eye has changed.
  - MOVEMENT 2 `2.2-9.015s` — density: `dense` — **the eye enters and crosses the line** from left to right. One pass, uninterrupted, at a rate that does not change — **and it arrives on the last character of the line on the last frame of the take.** ⚠️ **The stop is not a movement inside this shot; it is where the shot ends.** The page goes on settling throughout, the dust crosses against the eye's direction, the lit edge slides right, and **the camera never finishes its descent.**
- Temporal Density: **The take is one long movement that does not slow before the cut.** ⚠️ **The previous version of this section put the work's weight in two held movements around a short one** — the page before the eye arrived, and the eye after it stopped. ⛔ **The second of those was the defect**: the eye stopped at 14.259s and the cut was at 17.074s, so **2.815 seconds of stopped picture received the song's next line.** ⚠️ **There is no `held` movement in this shot** — stillness of the *frame* is not this work's stillness, and the subject's own stillness is now placed where the song puts its accent.

# 9. ACTION

- `ACT_READ` — Before: the line has not been crossed. After: **an eye has crossed it, once, from left to right.** ⚠️ **Nothing is understood. The reading is the movement, not the meaning.**
- `ACT_STOP` — Before: the eye is travelling. After: **the eye is still, at the end of the line.**

# 10. CAMERA

- Camera Language: Third person, **close**, at the page — the same placement as the shot before, at desk height, looking slightly down. **The camera is at the desk; the eye is above the page.**
- Camera Events: One event only. `0-9.015s` — **the descent begun in `s01` continues**: the lens keeps coming down toward the page and slightly right, at a rate that does not change, and **it is still descending on the last frame of this take.** ⚠️ **No cut stops it.**
- Camera Behavior: ⚠️ **No rack focus onto the writing, and no cut to a legible insert.** The camera does not do with the lens what the eye is doing. **No push-in on the line.** ⚠️ **But the camera is not parked**: the page grows slowly in the frame as the lens comes down, and the ruled columns cross the frame edge at the end as they did not at the start. **It never becomes a close-up of a single character.** ⚠️ **The camera does not stop before the cut** — it arrives with the eye.

# 11. MOTION

## Subject Motion

**An eye crossing a line and coming to rest on its last character — with the arrival placed on the last frame of the take.** ⚠️ **It is the change this shot carries, and it is one change** — the brow does not move, the mouth does not move, the head does not tilt, and the shoulders are not in the frame. ⛔ **The blink the previous version placed after the stop is gone**: there is no longer an after-the-stop for it to sit in.

## Object Motion

**The page is still settling from the shot before** — its fore-edge lifts and falls a few times and comes to rest early in movement 1. The writing does not change, and the ruled columns do not move in themselves; **what moves across them is light.** ⚠️ **This is a small motion and it is not nothing** — it is the difference between a page lying on a desk and a photograph of one.

## Environmental Motion

Dust moves over the page and catches the tube, **crossing against the direction the eye is travelling**, so that the frame has two movements in it at once and only one of them is the eye. ⚠️ **None of it stops when the eye does** — the dust is still crossing on the last frame.

## Physical Characteristics

- **Weight**: **The eye has none; the page has a little.** The page lies flat and is settling; the light crossing it has none. ⚠️ **This shot carries less weight than the shot before it** — the register's mass belongs to `s01`, and what is left here is a page coming to rest.
- **Inertia**: The eye arrives at the end of the line and **stops without overshoot and without ease** — it is not decelerating, it simply is not going on. ⚠️ **Because the arrival is the last frame, there is no settle to see**: the take ends on the instant of the stop.
- **Acceleration**: **The eye's rate does not change from the start of the line to the end of it** — the crossing is one speed and then zero. ⚠️ **The page's rate does change**: the fore-edge rocks down and slows as it comes to rest.
- **Fluidity**: Continuous; the saccade is not a snap and not a stutter. ⚠️ **There are no small jumps** — the eye crosses the line as one movement.
- **Impact**: **None.** Nothing in this shot touches anything.

# 12. EMOTION

- Emotional Arc: **The interval between reading a name and knowing it** — crossed once, and then cut off at the instant of arrival.
- Emotional Events: **The stop.** ⚠️ **The shot's event is that nothing follows the reading** — no recognition, no reaction, no turn. ⚠️ **And now nothing can follow it inside this shot**: the stop is the last frame, and whatever the face would have done is left to the shot after it. **The emotion is in the restraint, and the restraint is the cut.**

# 13. LIGHTING

- Base Lighting: Fluorescent over a working desk at the end of the working day, with the style's bloom on the pale surfaces. The tube is above and behind the camera and the room's own light has not been switched off yet; outside there is nothing left to see. The paper is the brightest thing in the frame and the rest of the staff room has gone to deep cyan.
- Lighting Events: **None** — no lamp is switched and the tube does not strike or fail. ⚠️ **A change of light as an event would be read as a change of understanding**, and this shot has none. ⚠️ **But the light in the frame moves the whole time**, and it moves because the page and the camera move: the lit edge of the ruling slides right as the lens comes down, dust crosses the beam and takes its own shadows with it, and the eye's own socket shadows the page beneath it as it travels.

# 14. AUDIO

- Dialogue: **None.** No line is spoken, and **no one is in this shot to speak one.** ⚠️ **The work still speaks Japanese**; §18 names it.
- Sound Effects: **Paper and breath, and nothing else placed.** The small dry sound of a page under a hand that is not moving it; a breath taken through the nose and let out; ⚠️ **and the absence of any sound from the reading** — **the eye crosses the line and makes no sound at all**, and that absence is placed rather than left out.
- Music: **None, by specification.** ⚠️ **On this route `No BGM` is one of the few negations that is actually received** (§18), and ⚠️ **the work's only music is the song, placed in post over this shot.** Nothing rises when the eye stops.
- Environment: A staff room at the end of a working day. The tube, a corridor, the building's quiet. **No calling voice as a sound effect.**

# 15. CONTINUITY

- Identity: **Must preserve** — the face and the eye of the frozen setting sheet, and **the same person as the hand in `s01`.** **May change** — nothing. ⚠️ **No expression is placed on the face** other than what the eye is doing.
- Spatial: The page is square to the frame and stays square; **the eye is above it throughout.** ⚠️ **Nothing is moved for the camera.**
- Temporal: The same working day, minutes after `s01`. **Nothing in frame supplies a date.**
- Visual: The fluorescent key, the palette and the dust are the same as `s01` and as all twenty-seven shots. **This is the second of the four evening shots.**
- Motion: Full animation, not limited. **The atmosphere is the primary mover**; the eye is the change. ⚠️ **The atmosphere does not stop when the eye does** — the page settles, the dust crosses, and the camera descends through to the cut.
- Sound: Paper, one breath, and no music. **No calling voice as a sound effect.**
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
- **The head does not turn and does not bend closer.** No tilt, no nod, no movement of the shoulders.
- **The mouth does not move in this shot** — the mouth belongs to `s03`.
- **The writing does not become readable**, and no insert of it is cut in.
- **No finger tracks the line.** The reading is done by the eye alone; **a finger would make it a different gesture.**

## MUST

- **An eye crosses one line from left to right and comes to rest on the last character.**
- **It is the only thing in the frame that changes.**
- **The line it has crossed cannot be read.**
- ⚠️ **The arrival is on the last frame of the take** — the cut and the stop are the same instant.
- ⚠️ **There is no still frame in this take.** The page, the dust, the lit edge of the ruling and the camera move in every one of its 216 frames.

## PREFER

- The line occupying the lower third of the frame and the eye above it, so that the distance between them is the shot's whole composition.

## ALLOW

- Dust over the page; the page's fibre; the uneven width of the ruled columns.

# 17. GENERATION PRIORITIES

1. **The eye is the only thing that changes** — a brow, a mouth or a head moving turns this into a face, and the work is not there yet. ⚠️ **It is not the only thing that moves**: the page, the dust, the lit edge and the camera run underneath it, and they are what keeps the frame from being a still.
2. **The line is crossed once and the speed does not change.**
3. **The writing stays unreadable** — the shot's whole subject is that the eye has been over it.
4. **Nothing follows the stop** — no recognition, no reaction, no turn.
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

A 9-second cinematic piece (16:9), luminous realist anime, over the opened page of an attendance register at the end of a working day, 2026. One continuous take, one change: **an eye crosses a single line of writing from left to right and stops at the end of it.**

0-2.2s: the opened page and the light lying along its ruled columns. **The eye is not in the frame yet.** The columns are printed thin lines of uneven width, and the characters inside them were written in ink by more than one hand — **present and not readable.** **The page is still settling from the shot before** — its fore-edge lifts and falls and comes to rest — dust crosses the columns from left to right, the lit edge of the ruling slides as the camera comes down, and **the descent does not stop.**
2.2-9.015s: **an eye enters and crosses one line from left to right.** One pass, uninterrupted; **the rate does not change from the start of the line to the end of it.** The brow and the mouth are held and do not move. Dust keeps crossing, against the eye's direction; the page is at rest now and the light on it is not. **The eye reaches the last character of the line on the final frame of the take** — the stop and the cut are the same instant. **Nothing follows the stop** — no recognition, no reaction, no blink.
**Only the eye changes: the head does not tilt, the mouth does not move, and no finger tracks the line.** **The writing on the page is present and cannot be made out — the characters are Japanese characters, set in the Japanese script, and they are not legible.** **This is a Japanese work.** No subtitles. No BGM.
(One continuous take, one change: an eye crosses the line and stops at the end of it.)

## Visual Prompt

Luminous realist anime, translated into the opened page of a register at the end of the day: the light, not the figure, is the subject, and here it lies along ruled columns and stops where the fore-edge shadows. Almost the whole frame is paper. Above the line, one eye and the side of the brow — **the rest of the face is not the subject of this shot and is not detailed.** The page: printed thin ruling of uneven width, characters written inside it in ink by more than one hand, **present and not readable.** The desk's worn edge in the near foreground. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp. Saturated where the light falls, deep cyan in the fore-edge shadow; cream, ruling grey, ink black, and the pale of one eye. Bloom on the pale surface, dust suspended and individually rendered over the page, generous negative space and very low visual density.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. **One eye crossing a line from left to right, once, at a rate that does not change, reaching the last character on the final frame.** The brow is held, the mouth is held, the head does not tilt, and there is no hand in the frame. **The stop has no overshoot, no ease and no settle** — the eye is not decelerating, it simply is not going on, and **the take ends on that frame.** ⚠️ **The page, the dust, the lit edge of the ruling and the camera move throughout the shot**, and none of them stops when the eye does — the fore-edge of the page rocks down and comes to rest early, dust crosses against the eye's direction, **and the camera is still descending on the last frame.** ⚠️ **No held frames and no still frames anywhere in this take.** No impact, no motion blur smears, no stutter.

## Camera Prompt

Third person, close, at desk height looking slightly down — the same placement as the shot before. One camera event only: **the slow descent begun in the previous shot continues toward the page and slightly to the right, at a rate that does not change, and it is still running on the last frame of the take.** ⚠️ **Do not stop the move before the cut**, and **do not rack focus onto the writing and do not cut to an insert of it** — the camera does not do with the lens what the eye is doing. ⚠️ **The page may grow in the frame as the lens comes down, but it never becomes a close-up of a single character.** No handheld, no whip, no shake, no push-in on the line, no sudden zoom, no unnatural rotation.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of everything this work holds. **No line is spoken in this shot: no one is in it to speak one, and there is no voice-over and no narration.** **The Japanese is not spoken here; it is what this work is** — and **nothing is written on screen**: no subtitles, no captions, in any language. Sound effects, nothing mixed forward: a page under a hand that is not moving it, one breath taken through the nose, the hum of the tube, a corridor. ⚠️ **And one absence, placed rather than left out: the reading makes no sound at all** — the eye crosses the line and nothing is heard. **Music: none — this shot carries no music of any kind.** No bed, no score, no sting, no drum; ⚠️ **the song goes on in post, over this shot.** Nothing rises when the eye stops. No calling voice as a sound effect.

## Negative Prompt

no watermark, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no swelling music, no drum, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no crowd, no face before the name is called, no legible name text, no legible text on any surface, no readable characters on any prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no identifying clothing, hairstyle, or prop, no character added beyond the shot, no additional person beyond the shot, no wall clock, no calendar, no digital timer, no date stamp, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no smile, no tears, no fear, no exaggerated expression, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-mv-s02-9.015s-01`
- Segment ID: `pre-chorus-1-1`
- Specification Version: `0.3.0`
- ⚠️ **`0.2.0` → `0.3.0` は、参照の側の変更である**（2026-09-28）——**運動の層は動いていない。** **三枚目（`碓氷千夏_キービジュアル.png`）を、この1本が渡す参照に加えた。** ⛔ **ゆえに次の投入は、テイク1と2つの点で違う**——**運動の層の差だけを見るなら、参照を持たない `s01` が対照である。**
- Generation Date: `2026-09-28`
- ⚠️ **版が `0.1.0` から動いた**（2026-09-28、運動の層の作り直し）。⛔ **`media/` に在る `02_…mp4` は `0.1.0` から出ている**
  （`takes/habits-mv-s02-video-1.yaml` の `params.source_version`）——**ゆえに `L25` の版の照合が
  「投入 `0.1.0` → 現在 `0.3.0`」を言う。** **それが正しい。この1本は、いまの仕様の生成物ではない。**
- ⚠️ **日付の出所**: `media/` に置かれたファイルの mtime（2026-09-28 05:13）である——
  **投入した時刻そのものではない。** ⛔ **世代の記録は `takes/habits-mv-s02-video-1.yaml` に在る**——
  **この仕様は世代を写さない**（写した分は古びる）。

## Resolved Values

- Duration: `9.015s`
- References: `REF_CHARACTER (碓氷千夏 — 設定画＋表情シート＋キービジュアル, CRITICAL) ／ REF_FORMAT (video-spec) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`
- Temporal Structure: `2 movements, NON_UNIFORM — 0-2.2s / 2.2-9.015s`. The held movement = `none`
- Camera Events: `1 event as listed in §10`
- Action Events: `ACT_READ → ACT_STOP`
- Audio Events: `no dialogue ／ paper ＋ one breath ＋ one placed absence ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.3.0` — **運動の層を作り直した**（2026-09-28）。⚠️ **`0.2.0` → `0.3.0` で、渡す参照が二枚から三枚になった**（運動の層は動いていない）。**生成はまだ `0.1.0` の1本だけである。**
**採用は、まだ選ばれていない**——**選ぶのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。
⛔ **この節は仕様の側であって、世代の記録ではない**——**記録は `takes/habits-mv-s02-video-1.yaml` に在る。**

### `0.2.0` → `0.3.0`（2026-09-28）——三枚目の参照

**渡す参照を二枚から三枚にした。** 変わったのは §3 の `Reference`・§6 の `REF_CHARACTER`・§19 である。
- **`碓氷千夏_キービジュアル.png` を加えた**（著者作成）——**`ledger.yaml` の `碓氷千夏.identity` が名乗る三枚目である。**
- ⛔ **動機は衝突である。** **凍結した設定画は `転 出` の見出しと行数字を持つ**（設定画 ⑨ を実測、2026-09-28）
  ——**`s03` のテイクでは、その印刷が読める日本語として戻った。参照集合が、この作品の禁制集合
  （`no legible text on any surface`）とぶつかっている。**
  **註の字を持たない一枚を参照の側に置くことは、この衝突を薄める**——⚠️ **これは私の判断であって、実測ではない。**
- ⚠️ **凍結した二枚は動かしていない。** 三枚目は、その二枚と併せて渡す一枚である。
- ⚠️ **`s01` はこの変更を受けていない**——**参照を1枚も持たない1本であり、次の投入で運動の層だけを見るための対照である。**

### `0.1.0` → `0.2.0`（2026-09-28）——運動の層

**規則「変化は、切れ目で終わる」を入れた。** 変わったのは §1・§7・§8・§10・§11・§12・§13・§15・§16・§17・§18 の三つのプロンプト・§19。
⛔ **変わった中身**:
- **末尾の `held`（`6.2-9.015s`）を消し、横断を切れ目のコマで終わらせた。**
  **止まることと切れることが、同じ瞬間になった。**
- **頭の `held`（`0-3.0s`）を `sparse` に置き換えた。** 頁は前の1本からまだ沈んでいる。
- **まばたきを外した。** 止まったあとが無くなったので、置き場所が消えた。
- **§11 の「Everything the eye is looking at is still」を撤回した。** 頁は沈み、埃は渡り、光の縁は滑る。
- **§10 のカメラを、`s01` から続く止まらない降下にした。** 前の版は「数センチの重い沈み」で、
  **「何も明かさず」「構図を最後まで保つ」**と言っていた。
- ⚠️ **§18 の `Negative Prompt` と `Style Motion` は1字も動かしていない**（`L10`）。

## Observed Problems

- ⛔ **解像度が食い違った** — §1 は `1920x1080`、戻ってきたのは `1280x720` である（**`L25` が鳴る。鳴るのが正しい**）。**フレームレート 24fps と尺は一致した。**
- ⛔ **頁の字が、日本語として読めない** — **ラテン文字でも、キリル文字でも、片仮名でもない記号**が混ざって並んでいる。§18 は `no real-world alphabet` / `no nonsense glyphs` / `no pseudo-kanji` を持っていたが、**この経路では散文として読まれた**（`L30`）。**画像の経路にだけ、否定のための欄が在る**——**「画像→動画」へ移る理由が、ここで実測になった。**
- ⛔ **両目が入り、髪と額も入っている** — §1 は「**still not a face but a part of one**」と言い、`SUBJECT` は `the one eye` と言う。**戻ってきたのは両目である。**
- ⚠️ **頁を斜めに横切る強い影が在る** — §13 は「平坦な蛍光灯」を言う。**この影は方向を持つ**（腕の影である可能性は残る。**判定していない**）。
- ⚠️ **この1本の変化を、3コマからは仕様どおりに読めていない** — 仕様は「目が一行を左から右へ渡り、行末で止まる」と言う。**見えたのは「頁から目が立ち上がる」動きである。** ⛔ **コマとコマの間は見ていない——読めていないことを、読めたことにしない。**
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
  ⚠️ **この1本は `identity` を添付する側である**（§6）——**その一枚が実際に渡ったかを、私は見ていない。**
  ⛔ **`attached` は書いていない**——**推測で書けば、記録が測定になる。**

## Anticipated risks (to check in the first generation)

- **The writing may be rendered legible.** ⚠️ **The first risk of this shot, and on this route the one the `Negative Prompt` cannot stop.** If the line can be read, the eye's crossing becomes information instead of procedure.
- **The eye may be given an expression.** A lifted brow or a narrowed lid turns this into a face reacting, and the work is not there yet.
- **The head may bend closer.** The distance between the eye and the page is the shot's composition; closing it changes the shot's meaning.
- **A finger may enter and track the line** — a reading gesture the work has not asked for.
- **An insert of the writing may be cut in.** ⚠️ **That shows the audience what the eye saw**, and the shot exists because they are not shown it.
- ⛔ **The eye may stop before the last frame.** ⚠️ **This is the failure the restructure was written against.** The take is 9.015s and the eye has to be arriving at 9.015s — **an eye that reaches the end of the line at 6s and waits hands the song a stopped picture**, which is what the previous version of this shot did for 2.815 seconds.
- **The page may come back as a still.** Movement 1 is `sparse`, not `held`: the fore-edge has to still be settling from `s01`, dust has to be crossing, and the camera has to be visibly descending to the page. ⛔ **A frozen opening is the same defect as a frozen ending.**
- **The camera may be parked.** ⚠️ The descent has to still be running at 9.015s. A lens that settles in the first two seconds makes this shot a photograph of a page with an eye moving over it.
- **Music may be placed anyway.** ⚠️ **On this route `No BGM` is one of the few negations actually received**, so a bed arriving is a violation of §16, not a matter of taste.
