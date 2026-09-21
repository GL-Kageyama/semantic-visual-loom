# Wan 3.0 Full Specification — 一筆 Clip 1/1 / 6s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。** 投入の仕方は同じディレクトリの `README.md` を見よ。

⚠️ **この作品は物語ではない。** 1ショットだけの最小の作品であり、
**Style 4.3「動く絵画」が成立するかを試すために在る**（決定 2026-09-21、著者。D-14）。

⚠️ **この1本の変化は1つだけである。**「白い紙が、墨を持つ。」
**それ以外のことは何も起こらない**——人物も、物語も、開示も無い。

⚠️ **この仕様は、このリポジトリで最初に「生成の前に書かれた」仕様である。**
参照画像は1枚もまだ無い（`ledger.yaml` の `紙.base`）。**四つの手の①（生成する）は著者のものである。**

⚠️ **この作品の様式カードは、このリポジトリの中に在る**（`references/styles/sumi-e.md`）。
**走らせるときは `SVL_STYLES_DIR=references/styles` を張ること**——張らなければ `L20` が違反として鳴る。
⚠️ **これは作品の欠陥ではなく、置き場の性質である。**

⚠️ **§18 `Audio Prompt` は作品の言語（`Japanese`）を名乗る**（`L27`）。
発話は1つも置かないが、**空欄は中立ではない**——生成器は、指定されなければ自分の既定で喋る。

---

# 1. VIDEO

- Duration: `6s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the white paper comes to hold ink
  — **and the ink only ever spreads.**

# 2. WORLD

## World Concept

Paper and ink. Nothing else is in the frame. There is no clock — **not because time is withheld,
but because there is nothing for time to pass through.** Before the stroke and after it: that is all of it.

## World Rules

- The stroke happens once. It is not corrected, not retraced, not repeated.
- The ink moves in one direction only: outward. **It never narrows, never retreats, never dries back to white.**
- The brush leaves. **What moves after it is the paper's, not the hand's.**
- The void stays empty. No dust, no haze, no light shaft drifts in to fill it.
- The ink stays monochrome. No colour and no colour-temperature shift.
- No legible text, no seal, no signature appears anywhere.
- No person, no figure, no hand is in the frame at any point.

## Visual Language

- Art Direction: Graded black ink on washi — the five inks, dry-brush strokes, bleeding, boldly reserved negative space, single-stroke economy.
- Color Language: Monochrome. Gradations of black ink on warm off-white paper. **No second hue in the frame at any time.**
- Texture: Washi grain, bleeding edges, dry-brush breaks, dark ink dots.
- Rendering: Hand-drawn ink wash. **Not a photographic surface, and not a render.**
- Visual Density: Very low. Paper, one stroke, and the void. Nothing else.
- Time: 時刻を持たない
- Atmosphere: Still and dry. **The only thing alive in the frame is the ink.**

# 3. SUBJECTS

## The Ink

- Reference: (none — the ink is not a registered entity; it is the subject of the shot)
- Appearance: A single dark stroke laid on washi, its edge wet where it travelled, the wet edge **only ever moving outward from the line.**
- Behavior: It spreads into the fibre. **It does not narrow, does not retreat, and does not dry back to white.** It does not pulse, breathe, or bloom-and-shrink.
- Continuity Requirements: One mark, one pressure, no seam. The stroke is continuous with itself.

# 4. ENVIRONMENT

- Location: `紙`
- Environment Elements: One sheet of washi filling the frame, its fibre visible. Nothing else is in the frame but the paper, the ink, and — for one beat — the brush.
- Environmental Behavior: The paper does not move, does not flutter, does not breathe. **Only the ink moves within it. The void stays empty for the whole shot.**

# 5. OBJECTS

- The brush. It enters from the frame's edge before the stroke, lays the mark once, **and leaves before the shot ends. It is never seen again.**
- No ink stone, no water dish, no seal, no weight, no table edge. **Nothing else is in the frame.**

# 6. REFERENCES

- REF_LOCATION: `紙.base` — **未作成**（`ledger.yaml` を見よ）(MEDIUM)
- REF_STYLE: `sumi-e` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/ippitsu/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The white paper comes to hold ink.
- Beginning: The paper is blank and the brush has not touched it.
- Turn: The stroke is laid — **once, and it is not revised.**
- Peak: The ink enters the fibre and does not stop.
- Pull: The brush is gone and the ink is still spreading.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — Blank paper. The brush enters the frame and has not touched it yet. **The void is already the composition.**
  - BEAT 2 `2-3s` — density: `dense` — One stroke is laid. **Once. Not corrected, not retraced, not repeated.** The brush leaves the paper.
  - BEAT 3 `3-6s` — density: `held` — The brush is gone. The ink enters the fibre and keeps spreading. **It never narrows and never returns.**
- Temporal Density: Half the shot is the third beat — **the part with no hand in it.**

# 9. ACTION

- `ACT_ENTER` — Before: the brush is outside the frame. After: the brush is over the paper.
- `ACT_LAY` — Before: the paper is blank. After: one stroke is on it.
- `ACT_WICK` — Before: the mark sits on the surface. After: the ink is in the fibre and travelling.

# 10. CAMERA

- Camera Language: The frame is a scroll, not a window. One flat frontal view of the sheet, held at the paper's own scale, the void given as much of the frame as the subject.
- Camera Events: `0-2s` the whole sheet. `2-3s` hold, unmoved, while the stroke lands. `3-6s` hold — **the camera does not move at all while the ink spreads.**
- Camera Behavior: **Still.** No push, no drift, no pan, no handheld, no whip. One continuous take; no cut. **Any camera movement spends the negative space, which is what the shot is about.**

# 11. MOTION

## Subject Motion

The ink spreads outward from the stroke into the paper. **One way only: the ink is at its largest at the end. It never narrows, never retreats, and never dries back to white.** It does not pulse, and it does not breathe.

## Object Motion

The brush moves once — in, one stroke, out — and is gone before the third beat. **After it leaves, nothing in the frame moves but the ink.**

## Environmental Motion

None. The paper does not move, the void does not fill, and nothing drifts across the frame.

## Physical Characteristics

- Weight: The ink has the weight of water in fibre. **It has no bounce.**
- Inertia: Once it is in the paper it keeps going without the hand, **and it never comes back.**
- Acceleration: Almost none, and it does not slow to a stop within the shot.
- Fluidity: A wet edge travelling through fibre — **not a membrane that inflates and then deflates.**
- Impact: None.

# 12. EMOTION

- Emotional Arc: The patience of a mark that is still arriving after the hand has gone.
- Emotional Events: The moment the brush leaves the paper and the ink keeps moving.

# 13. LIGHTING

- Base Lighting: Flat, even, frontal light on the sheet. **No directional key, and no shadow cast across the paper.**
- Lighting Events: None. The light does not change, and no shaft crosses the frame.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: Almost none — the dry contact of the brush for a fraction of a second as the stroke lands.
- Music: None.
- Environment: The room tone of a dry room, unbroken.

# 15. CONTINUITY

- Identity: The same sheet for the whole shot — same grain, same tone, same edges.
- Visual: Monochrome, flat light, bold negative space, washi grain in every frame.
- Motion: The ink moves for the whole shot, including the beats where nothing else does. **Limited animation is not acceptable — the ink is never a held frame.**
- Sound: The room tone is unbroken across the cut.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・この作品は開示台帳を持たない）

- No second stroke. No retracing, no correction, no doubling of the line.
- No brush after the stroke lands. **The brush is gone before the shot ends.**
- **No ink narrowing, no ink retreating, no drying back to white. The ink is at its largest at the end.**
- No filled negative space. No dust, no haze, no particle, no light shaft entering the void.
- No colour. No colour-temperature shift. No red seal, no stamp, no signature, no seal box.
- No readable text of any kind.
- No person, no figure, no hand.

## MUST

- The stroke happens exactly once.
- **The ink spreads outward through the whole third beat and never comes back.**
- The void stays empty for the whole shot.
- The camera does not move.
- Monochrome throughout.

## PREFER

- The stroke placed off-centre, with the larger part of the sheet left empty.

## ALLOW

- A single dry tick as the brush meets the paper.

# 17. GENERATION PRIORITIES

1. **The ink is one-way** — it is at its largest at the end, and it never narrows, never retreats and never dries back to white. ⚠️ **This is the failure a soft mass produced for the neighbouring work — a mark that blooms and then shrinks reads as breathing, not as ink.** It outranks beauty.
2. **The stroke happens once** — no second stroke, no retracing, no correction.
3. **The void stays empty** — the reserved white survives the whole shot; nothing drifts in to fill it.
4. **The brush is gone** — after the stroke lands, nothing moves but the ink.
5. **The camera holds still** — a scroll, not a window; no movement for its own sake.
6. **Monochrome throughout** — no colour and no colour-temperature shift.
7. **The paper's texture** — washi grain, dry brush, bleeding.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 6-second continuous cinematic take (16:9), sumi-e ink wash, on a single sheet of washi that fills the frame. Beats, deliberately uneven: [0-2s] blank paper, the brush entering the frame and not yet touching it; [2-3s] one stroke is laid — once, not corrected, not retraced — and the brush leaves the paper; [3-6s] the brush is gone and the ink enters the fibre and keeps spreading. **The ink moves one way only: it is at its largest at the end, and it never narrows, never retreats and never dries back to white.** The void stays empty for the whole shot, and the camera does not move. Monochrome throughout. (No person, no hand, no brush after the stroke, no second stroke, no seal, no readable text.)

## Visual Prompt

Sumi-e ink wash on washi paper. Graded black ink — the five inks — dry-brush strokes, bleeding edges, boldly reserved negative space, single-stroke economy, washi grain, dark ink dots. Monochrome: gradations of black on warm off-white paper, with no second hue anywhere in the frame. One sheet of paper fills the frame, flat and frontal, carrying one dark stroke whose wet edge has travelled outward into the fibre. Very low visual density: the paper, one stroke, and the void; nothing else. No second stroke, no retracing of the stroke, no brush after the stroke lands, no person, no figure, no hand, no color, no red seal, no stamp, no signature, no readable text, no filled negative space, no ambient particles, no haze, no light shafts crossing the frame, no hard outline, not photorealistic, no 3D render, no photographic surface.

## Motion Prompt

Hand-drawn ink wash. **The stroke is the event and it happens once** — a single decisive gesture that lands and is not revised, not retraced and not repeated; the brush enters, lays the mark, and leaves before the shot ends. **After the brush has stopped, the ink keeps moving**: the wet edge travels outward through the washi fibre for the whole of the last three seconds. **The movement is one-way — the ink is at its largest at the end; it never narrows, never retreats, never pulses, never breathes, and never dries back to white.** Nothing else in the frame moves: the paper does not flutter, the void does not fill, and no particle, haze or light shaft drifts in. **The camera does not move.** No second stroke, no morphing contours, no motion blur, no continuous ambient motion, no full animation.

## Camera Prompt

The frame is a scroll, not a window: one flat frontal view of the sheet, held at the paper's own scale, with the void given as much of the frame as the subject. **The camera does not move at all** — no push, no drift, no pan, no handheld, no whip. One continuous take; no cut.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of this work and of every word it holds; **if any speech is placed in it, that speech is Japanese.** **No speech is placed in this shot.** No dialogue, no voice-over, no narration. Sound effects: almost none — only the dry contact of the brush for a fraction of a second as the stroke lands. Ambient: the room tone of a dry room, unbroken. **Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell.**

## Negative Prompt

no color, no photorealistic, no hard outline, no second stroke, no retracing of the stroke, no ink retreating, no ink narrowing, no drying back to white, no brush after the stroke lands, no filled negative space, no ambient particles, no haze, no light shafts crossing the frame, no morphing contours, no motion blur, no camera move for its own sake, no seal, no signature, no stamp, no readable text, no watermark, no on-screen subtitles, no background music

## Style Motion

**The stroke is the event, and it happens once.** Motion is a single decisive gesture that lands and is not revised — not a continuous flow; between strokes, nothing moves. **The ink keeps moving after the brush has stopped** — bleeding and wicking continue into the washi, so what changes in the frame after the gesture is the paper's, not the hand's. **The camera is a scroll, not a window** — the frame holds still; the bold negative space is what the shot is about, and a moving camera spends it. **Stillness is the ground; the void stays empty** — nothing drifts in to fill it: no ambient particles, no haze, no light shafts crossing the frame. ⚠️ **What this style does not do**: full animation, continuous ambient motion, morphing contours, motion blur, or a camera that moves for its own sake. **The ink stays monochrome for the whole shot** — a colour or colour-temperature shift is a different style, not a beat of this one. (Source: the `Motion character` of the style card `sumi-e`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ippitsu-s01-6s-01`
- Segment ID: `01-1`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `6s`
- References: `REF_LOCATION (紙.base, 未作成) ／ REF_STYLE (sumi-e, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 2s / 1s / 3s. The ink = BEAT 3 at 3s (50%)`
- Camera Events: `none — the camera does not move. One continuous take`
- Action Events: `ACT_ENTER → ACT_LAY → ACT_WICK`
- Audio Events: `no dialogue ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **まだ生成していない。** 四つの手の①は著者のものである。

## Observed Problems

_(none yet)_

## Anticipated risks (to check in the first generation)

- **The ink may come back.** A soft wet edge that blooms and then shrinks reads as **breathing, not as ink** — and a diffusion model asked for "bleeding" will animate it both ways unless it is told not to. The one-way rule is front-loaded in §1, §2, §3, §8, §11, §16, §17 and §18; **verify frame by frame. This is the most likely failure of this shot.**
- **A second stroke may be added.** Models asked for a sumi-e stroke tend to complete the gesture — a second, balancing mark, or a retrace of the first.
- **The brush may stay in frame.** It must be gone before the third beat; a hand that lingers turns this into a shot about a hand.
- **The void may be filled.** Haze, dust motes, or a light shaft across the paper would spend the negative space, which is the composition.
- **A seal may appear.** Ink-wash styles very often add a red seal; it is the most likely source of colour in the frame.
- **The camera may drift.** A slow push is the default behaviour of the model and it is not wanted here.
- **The shot may come back as a time-lapse** — the ink spreading in compressed time rather than in six continuous seconds.
