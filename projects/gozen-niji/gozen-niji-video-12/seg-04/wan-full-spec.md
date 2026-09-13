# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第12話 S55「返せた」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「返せた」——ニジの笑顔を見る。白い光が、第3話で真白が名付けた色（虹色）へゆっくり戻る。真白の「うん」だけが声を震わせ、彼女はそれを止めない。完全消失を出さない。三状態の弧の第2歩目——ここで初めて虹色が戻る。**

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold one turn (one dramatic beat) of a 57-part light-novel animation into a single 30-second take that ends on its pull`
- Register: `Restrained. The horror and the tenderness are both delivered by ordinary objects and withheld reaction, never by performance`
- Rule: `One turn = one generation. The arc is distributed across 57 takes; nothing is added after the pull`

---

# 2. WORLD

## World Concept

- Concept: `Contemporary Japan, unchanged in every visible way — except that a screen-time log records time as a receipt for time deposited with other people`
- Era: `Present day`
- Location: `A high-school student's small bedroom; her school; occasionally a corridor, a classroom, a festival yard`
- Time: `The story lives at 2:00 A.M. Daytime exists only as the shore on either side of it`
- Weather: `Clear and still. Nothing outside ever comments on the events`
- Atmosphere: `Absolute domestic ordinariness. The anomaly never disturbs a single physical object`

## World Rules

- The supernatural is **recorded, not staged**. Its evidence is text on a screen.
- The phone's light is the sole light source at night. It does not flicker, pulse, or behave unnaturally.
- Nothing in the physical world reacts to the anomaly — no wind, no moving shadows, no disturbed objects.
- Notifications are **silent**. They arrive as light only.
- ニジ never leaves the screen.

## Visual Language

- Art Direction: `Soft cel anime — flat color planes, clean closed thin lineart, soft-edged shadow terminators`
- Color Language: `Muted, low-saturation. Night = desaturated indigo lit by one cold blue-white screen. Day = pale, slightly overexposed, equally muted. The screen's blue-white is the only value allowed to be bright — and, from seg.10, ニジ's rainbow is the only hue allowed to be saturated`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces`
- Rendering: `Two-step cel shading with softened terminators; gentle bloom around the phone screen; light haze in the dark air`
- Visual Density: `Low. Simple uncluttered rooms, generous negative space, one focal point per beat`

---

# 3. SUBJECTS

## MASHIRO

- ID: `MASHIRO`
- Name: `真白 (Mashiro)`
- Type: `CHARACTER`
- Role: `Protagonist — the one who deposited the time`

### Appearance

- Japanese high-school girl, 16–17, second year. Deliberately unremarkable — the girl slightly outside the middle of the circle.
- Shoulder-length dark hair, a thin neck; small frame; quiet face that gives little away. 「真白」is blankness, not whiteness — an undecorated stillness, not white hair.
- Back curved from long hours over a phone; the memory of the screen's light on her face.
- At night: plain pajamas, in a futon on the floor. By day: standard Japanese school uniform, white collar.
- **Solid and real — she casts a shadow in the scene.** (The contrast anchor: ニジ, her copy, has none.)

### Behavior

- Personality: `Inward, observant, agreeable on the surface. Reads the room and matches it. Small voice`
- Typical Motion: `Almost nothing moves except her fingers. Her body stays still far more than it moves`
- Emotional Range: `Narrow and suppressed. She does not scream, gasp, or widen her eyes. Her reactions register as stillness — a finger stopping, a held breath`

### Continuity Requirements

- Must preserve: `face, shoulder-length hair and color, the thin neck, build, age; the curved posture; the same phone (same size, same case); the same futon, room layout, window and curtain; the restraint — her expression never resolves into a clear readable emotion`

## NIJI

- ID: `NIJI`
- Name: `ニジ (Niji)`
- Type: `CHARACTER (apparition, on-screen only)`
- Role: `The ghost of 2 A.M. — the crystallization of feelings 真白 never received`

### Appearance

- **真白's own face, one step younger** — longer lashes, slightly fuller cheeks. The same shoulder-length dark hair and thin neck; the same way of tilting her head.
- A blurred rainbow afterimage — 虹色, the colour 真白 named in episode 3 — slowly returning as the white light regains it. Colors drift slowly: blue → green → blue. A blur and afterimage, not rays, not particles.
- The outline is slightly blurred at the edges. **No shadow anywhere** — unlike 真白's solid, defined outline.
- Exists **inside the screen**. Never stands in the room at human scale.

### Behavior

- Personality: `Bright, teasing, unguarded — she smiles more honestly than 真白 can. She never cries. She calls 真白「おまえ」`
- Continuity: `her opacity is a strict function of the segment number (see the ledger); it never varies within a beat except in seg.55`

> **ニジ appears this segment**（ledger 54–55 — white light regaining the rainbow）.

---

# 4. ENVIRONMENT

## Location

- ID: `BEDROOM`
- Name: `真白の部屋 (her bedroom)`
- Description: `Small, futon on the floor, curtained window, wall clock, desk, few objects. Dark except for the phone. The recurring stage — most night takes live here`

## Environmental Behavior

- Wind: `none — the curtain does not move`
- Particles: `only the faintest haze catching the screen's bloom; no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; at most one distant car's headlights crossing the curtain, once`

---

# 5. OBJECTS

## PHONE

- Type: `smartphone`
- Appearance: `真白's ordinary modern smartphone, plain case, Japanese UI. The only light source at night; the only surface on which the anomaly appears. Glass carries a soft bloom, never a hard specular glint`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
- Continuity Importance: `CRITICAL`

## SCREEN_TEXT

- Type: `UI text`
- Appearance: `No message text this segment — the screen holds only ニジ, her white light slowly regaining the rainbow. No UI text, no exchange`
- Narrative Importance: `LOW`
- Visual Importance: `LOW`
- Continuity Importance: `LOW`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads 2:00 A.M.`
- Narrative Importance: `MEDIUM`
- Visual Importance: `MEDIUM`
- Continuity Importance: `MEDIUM`

---

# 6. REFERENCES

## REF_STYLE

- Type: `STYLE`
- Source: `references/styles/soft-cel-anime.md`
- Priority: `HIGH`
- Defines: `rendering, palette discipline, lineart weight, shading steps, motion idiom (holds, twos and threes)`
- Does not define: `events, identity, or emotional tone`

## REF_FORMAT

- Type: `FORMAT`
- Source: `references/formats/video-spec.md`
- Priority: `HIGH`
- Defines: `the §1–20 skeleton, uneven density, the identity lock, the six §18 slots`

## REF_SOURCE

- Type: `SOURCE`
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_12_また明日.md`
- Priority: `CRITICAL`
- Defines: `every event, the exact on-screen text, the ending line, and what is and is not revealed`

## REF_BIBLE

- Type: `BIBLE`
- Source: `soul-voice-teller/examples/gozen-niji/台帳/series-bible.md`
- Priority: `CRITICAL`
- Defines: `the staged disclosure, the voice rules, and the addressee ledger`

## REF_CHARACTER

- Type: `CHARACTER`
- Source: `gozen-niji-mashiro-character-sheet/prompt.md ／ gozen-niji-niji-character-sheet/prompt.md`
- Priority: `HIGH`
- Defines: `the locked character design — 真白 (solid, real, casts a shadow) and ニジ (her copy, one step younger, no shadow, a rainbow afterimage blue → green → blue)`

---

# 7. NARRATIVE

## Core Event

ニジ asks 「……返せた？」 and 真白 answers 「うん。――返せた」. ニジ smiles — a smile 真白 does not know, but has seen somewhere. The white light slowly regains the rainbow: 虹色, the colour 真白 named in episode 3.

## Beginning

ニジ, from the screen: 「……返せた？」. 真白: 「うん。――返せた」.

## Turn

ニジ smiles — a smile 真白 does not know, but has seen somewhere; the smile 真白 wished she could show herself. ニジ: 「返してくれて、ありがとう」／ 「おまえがくれた時間、ちゃんと生きてきたよ」.

## Peak

真白: 「……うん」 — her voice shakes, and she does not stop it. The white light slowly regains the rainbow, drifting blue → green → blue — the colour 真白 named.

## Pull（引き — 切れ目）

The rainbow, returned — ニジ's smile, the colour 真白 named. Cut on the regained rainbow, with nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The return of the rainbow holds 12s (40%).

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「返せた」.** ニジ — 「……返せた？」. 真白 — 「うん。――返せた」. _Density: SPARSE — two quiet lines, no event._
- **BEAT 2 `[0:07–0:18]` — 「笑顔と、ありがとう」.** ニジ smiles — the smile 真白 wished she could show herself. ニジ: 「返してくれて、ありがとう」「おまえがくれた時間、ちゃんと生きてきたよ」. _Density: DENSE — the smile and the thanks._
- **BEAT 3 `[0:18–0:28]` — 「虹色を取り戻す」 — REVEAL, longest share.** 真白: 「……うん」 — her voice shakes; she does not stop it. The white light slowly regains the rainbow, drifting blue → green → blue — the colour 真白 named in episode 3. _Density: SPARSE, held — the colour returns without ceremony._
- **BEAT 4 `[0:28–0:30]` — 「虹色」.** Hold on the regained rainbow. Cut precisely on the pull. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `ニジ's smile (≈0:09) ／ the colour returning (≈0:20) ／ the rainbow holding (≈0:28)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the two quiet lines), 0:18–0:30 (the held return and the rainbow)`
- Dense regions: `0:07–0:18 (the smile and the thanks)`
- Long continuous action: `0:18–0:28 the slow return of colour`
- Rapid transitions: `none — a quiet, held segment`

---

# 9. ACTION

## Action — ACT_ANSWER

- ID: `ACT_ANSWER`
- Subject: `MASHIRO`
- Action: `Answers — 「うん。――返せた」`
- Intention: `To confirm what she has done`
- Intensity: `Low`
- Speed: `Slow, even`

### Action Relationship

- Before: `—` (continues from S54's typed line)
- After: `ACT_WATCH`

## Action — ACT_WATCH

- ID: `ACT_WATCH`
- Subject: `MASHIRO`
- Action: `Eyes settle on ニジ's smile — the smile she wished she could show herself — and hold`
- Intention: `To see it, and to recognize it`
- Intensity: `Medium, internal`
- Speed: `Still, and holding`

### Action Relationship

- Before: `ACT_ANSWER`
- After: `ACT_UTTER`

## Action — ACT_UTTER

- ID: `ACT_UTTER`
- Subject: `MASHIRO`
- Action: `Says 「……うん」 — her voice shakes, and she does not stop it. The finger stays at rest`
- Intention: `To let the feeling through, without performing it`
- Intensity: `CRITICAL (the peak, expressed as a shaking voice)`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_WATCH`
- After: `— (cut on the rainbow)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, very shallow. Only the screen or the fingers are ever sharp`
- Depth of Field: `Very shallow — the background is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Locked close on her face and the screen, the white light soft in frame. No camera movement.
- **`[0:07–0:18]`** — Cut to ニジ — the smile, 真白's own face one step younger. Static, close. The white light begins to gather colour at the edges.
- **`[0:18–0:28]`** — Hold on ニジ as the rainbow returns, drifting blue → green → blue. No camera movement at all — the colour does the moving.
- **`[0:28–0:30]`** — Hold on the regained rainbow. Cut precisely on the pull. Nothing after it.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially no movement; her body holds
- Only her eyes move, settling on ニジ's smile and holding
- Her lips form 「……うん」 — the faintest motion, then still

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only. Nothing glitches, flickers, or distorts
- The wall clock's second hand advances in discrete ticks

## Environmental Motion

- ニジ's white light slowly regains the rainbow — a blur, drifting blue → green → blue, not rays, not particles
- The rainbow is a blur and afterimage, slow and unhurried
- Only the screen's bloom breathes faintly on the ceiling

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet confirmation (返せた)
- ↓ Recognition (the smile she wished she could show herself)
- ↓ A feeling allowed to surface (the shaking 「……うん」)
- ↓ The colour returning (the rainbow, then cut)

## Emotional Events

- Event: `ニジ's smile` — Emotion: `Recognition — a smile she knows from somewhere, wished she could show herself` — Intensity: `HIGH` — Timing: `≈0:09`
- Event: `The shaking 「……うん」` — Emotion: `A feeling let through, not performed. Her voice shakes; she does not stop it` — Intensity: `CRITICAL — expressed only as a shaking voice. No tears, no facial performance` — Timing: `≈0:20`
- Event: `The rainbow returning` — Emotion: `The colour 真白 named, come back` — Intensity: `HIGH` — Timing: `≈0:22`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow is the only saturated hue in the frame`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on the ceiling as a soft blue rectangle.
- **`[0:07–0:18]`** — ニジ's white light begins to gather colour at the edges — the first faint blue.
- **`[0:18–0:28]`** — The rainbow returns fully, drifting blue → green → blue, the only saturated colour in the frame. Her face remains nearly silhouetted.
- **`[0:30]`** — Cut to black on the rainbow. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

> ニジ, soft: 「……返せた？」. 真白: 「うん。――返せた」. ニジ: 「返してくれて、ありがとう」／ 「おまえがくれた時間、ちゃんと生きてきたよ」. 真白: 「……うん」 — her voice shakes, and she does not stop it. No narration, no voice-over. No tears, no sobbing.

## Sound Effects

- The wall clock's second hand, dry discrete ticks, present throughout
- Soft futon fabric as she settles, once, at the very start
- A near-silence around the shaking 「……うん」

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender. Never sinister, never sentimental — no horror strings, no swelling`
- Emotional Function: `Hold the room's stillness. It may warm very slightly as the rainbow returns, then thin, leaving only room tone and the clock`

---

# 15. CONTINUITY

> 57本は57回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

- **Identity**: 真白 — plain Japanese high-school girl 16–17, shoulder-length dark hair, thin neck, small frame, curved posture over a phone. Same face in every take.
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen.
- **The room**: futon on the floor, curtained window, wall clock, sparse.
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light.
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue.
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers.
- **(seg.10+) ニジ**: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same neck tilt and shoulder-length hair — a rainbow afterimage inside the screen, casting no shadow, at the opacity this segment requires.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。

## MUST

- ニジ is present — 真白's own face one step younger — inside the screen only
- Render the white light **slowly regaining the rainbow**, 虹色 — the colour 真白 named in episode 3 — drifting blue → green → blue, a blur/afterimage, not rays or particles
- ニジ smiles — 真白's own face, one step younger, smiling more honestly than 真白 can
- 真白's voice shakes on 「……うん」 — and she does not stop it
- End by cutting on the regained rainbow, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 54–55 レンジより）

- **No complete disappearance.** ニジ must not vanish — the colour returns to her
- No tears, no crying, no tear streaks — the feeling surfaces only as a shaking voice
- No second character — ニジ is inside the screen, never standing in the room

## PREFER

- The return of colour uninterrupted — the whole segment is one held gaze
- Silence over score at the peak
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The rainbow's drift speed may vary very slightly — it must read as slow
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: the white light must regain the rainbow — but ニジ must not vanish (ledger 54–55). This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:07] ニジ, a white light in the screen, asks 「……返せた？」 and 真白 answers 「うん。――返せた」; [0:07–0:18] ニジ smiles — the smile 真白 wished she could show herself — and says 「返してくれて、ありがとう」「おまえがくれた時間、ちゃんと生きてきたよ」; [0:18–0:28] THE REVEAL — 真白 says 「……うん」, her voice shaking and not stopping it, as the white light slowly regains the RAINBOW, 虹色, drifting blue → green → blue, the colour 真白 named in episode 3; [0:28–0:30] hold on the regained rainbow, and the shot cuts on the rainbow. The return of colour holds the largest share of the duration. Ends on the rainbow, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. On screen, ニジ — 真白's own face, one step younger, longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, no shadow, smiling — inside the phone screen only; her WHITE light slowly regains the RAINBOW, 虹色, drifting slowly blue → green → blue, a blur and afterimage, not rays, not particles. The rainbow is the only saturated hue in the frame. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost nothing moves except the eyes; the body and the finger hold still. ニジ's white light slowly regains the rainbow, drifting blue → green → blue, slow and unhurried, a blur and afterimage, not rays, not particles. Her lips form 「……うん」 — the faintest motion, then still. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the fingers are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] locked close on her face and the screen, the white light soft in frame, no movement. [0:07–0:18] cut to ニジ — the smile, 真白's own face one step younger — static, close, the white light gathering colour at the edges. [0:18–0:28] hold on ニジ as the rainbow returns, drifting blue → green → blue, no camera movement. [0:28–0:30] hold on the regained rainbow; cut precisely on the pull.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, present throughout. Soft futon fabric once at the start. ニジ, soft: 「……返せた？」. 真白: 「うん。――返せた」. ニジ: 「返してくれて、ありがとう」「おまえがくれた時間、ちゃんと生きてきたよ」. 真白: 「……うん」 — her voice shakes, and she does not stop it. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — warming very slightly as the rainbow returns, then thinning, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion, no tears, no sobbing.

## Negative Prompt

no complete disappearance, no fully faded figure, no vanishing apparition, no tears, no tear streaks, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep12-seg04-30s-01`
- Segment ID: `S55`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_12, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 11s / 10s / 2s. Rainbow return = BEAT 3 at 10s (33%)`
- Camera Events: `4 events as listed in §10. No sustained dolly; all static holds`
- Action Events: `ACT_ANSWER → ACT_WATCH → ACT_UTTER`
- Audio Events: `ニジ three lines ／ 真白 two lines (the second shaking) ／ clock ticking throughout`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the rainbow`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The rainbow may render as rays or particles.** It must be a blur and afterimage, drifting blue → green → blue. If it reads as an aura, re-prompt for the blur.
- **The shaking voice may read as crying.** The voice shakes; there are no tears. The negative prompt front-loads this; watch for any wetness on either face.
- **The model may keep the colour drained.** The rainbow must return here — if ニジ stays white, the arc is broken.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the rainbow reads well, consider holding the return 1–2 seconds longer, taking the time from beat 1.
