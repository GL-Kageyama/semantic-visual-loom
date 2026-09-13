# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第12話 S56「行ってらっしゃい」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「行ってらっしゃい」——別れでなく送り出し（朝、家を出る人に掛ける日常の言葉）。虹色の残像がスマホの画面の中にだけゆっくり光へ溶け、他へはどこにも行かない。溶けたあとにニジが残らない。三状態の弧の最終歩。**

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
- A blurred rainbow afterimage, dissolving slowly into light — inside the screen, going nowhere else. Colors drift slowly: blue → green → blue, thinning as she dissolves.
- The outline is slightly blurred at the edges. **No shadow anywhere** — unlike 真白's solid, defined outline.
- Exists **inside the screen**. Never stands in the room at human scale.

### Behavior

- Personality: `Bright, teasing, unguarded — she smiles more honestly than 真白 can. She never cries. She calls 真白「おまえ」`
- Continuity: `her opacity is a strict function of the segment number (see the ledger); it never varies within a beat except in seg.55`

> **ニジ appears this segment**（ledger 56 — the rainbow dissolving into light）.

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
- Appearance: `No message text this segment — the screen holds only ニジ, the iridescent afterimage dissolving into light. No UI text, no exchange`
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

ニジ smiles once more and says 「――行ってらっしゃい」. The iridescent afterimage dissolves, slowly, into light — inside 真白's phone screen, going nowhere else.

## Beginning

ニジ — the rainbow, 真白's own face one step younger — smiles once more. A small, bright, honest smile.

## Turn

ニジ: 「――行ってらっしゃい」. Not a goodbye — the everyday send-off, said to someone leaving the house. The iridescent afterimage begins to dissolve into light.

## Peak

The rainbow dissolves into light — slowly — inside the phone screen, going nowhere else. No exit, no scattering, no room: the light thins and stays within the screen.

## Pull（引き — 切れ目）

The screen, holding only the faint light where ニジ was — nothing remaining. Cut on the dissolved light, with nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The dissolve holds 16s (53%).

## Temporal Sequence

- **BEAT 1 `[0:00–0:10]` — 「行ってらっしゃい」.** ニジ smiles once more — a small, bright, honest smile. ニジ: 「――行ってらっしゃい」. Not a goodbye. _Density: SPARSE — a spoken line and a smile._
- **BEAT 2 `[0:10–0:26]` — 「光に溶ける」 — REVEAL, longest share.** The iridescent afterimage dissolves into light — slowly — inside the phone screen, going nowhere else. No exit, no scattering, no room. The light thins and stays within the screen. _Density: DENSE at the head, then the thinning light, held._
- **BEAT 3 `[0:26–0:30]` — 「残らない」.** The screen holds only the faint light where ニジ was — nothing remaining. Cut precisely on the dissolved light. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `ニジ's smile (≈0:05) ／ the dissolve beginning (≈0:12) ／ the light thinning to nothing (≈0:24)`

## Temporal Density

- Sparse regions: `0:00–0:10 (the spoken line and the smile)`
- Dense regions: `0:10–0:26 (the dissolve)`
- Long continuous action: `0:10–0:26 the slow dissolve into light`
- Rapid transitions: `none — a single held dissolve`

---

# 9. ACTION

## Action — ACT_SMILE

- ID: `ACT_SMILE`
- Subject: `NIJI`
- Action: `Smiles once more — a small, bright, honest smile`
- Intention: `To send her off`
- Intensity: `Low`
- Speed: `Slow, unforced`

### Action Relationship

- Before: `—` (continues from S55's rainbow)
- After: `ACT_SEND`

## Action — ACT_SEND

- ID: `ACT_SEND`
- Subject: `NIJI`
- Action: `Says 「――行ってらっしゃい」 — the everyday send-off, not a goodbye`
- Intention: `To send 真白 forward`
- Intensity: `Medium, tender`
- Speed: `Slow, even`

### Action Relationship

- Before: `ACT_SMILE`
- After: `ACT_DISSOLVE`

## Action — ACT_DISSOLVE

- ID: `ACT_DISSOLVE`
- Subject: `NIJI`
- Action: `The iridescent afterimage dissolves into light — slowly — inside the phone screen, going nowhere else`
- Intention: `None — the dissolution itself`
- Intensity: `CRITICAL (the peak, expressed as the dissolve)`
- Speed: `Slow, and slowing`

### Action Relationship

- Before: `ACT_SEND`
- After: `— (cut on the dissolved light)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, very shallow. Only the screen or the fingers are ever sharp`
- Depth of Field: `Very shallow — the background is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:10]`** — Locked close on ニジ — the rainbow, 真白's own face one step younger — smiling. Static.
- **`[0:10–0:26]`** — Hold on ニジ as the iridescent afterimage dissolves into light, inside the screen, going nowhere else. No camera movement at all — the light does the moving. The frame stays within the screen.
- **`[0:26–0:30]`** — Hold on the faint light where ニジ was — nothing remaining. Cut precisely on the dissolved light. Nothing after it.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially no movement; her body holds
- Only her eyes move, watching ニジ dissolve
- ニジ's smile is still; her lips form 「――行ってらっしゃい」, the faintest motion

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only. Nothing glitches, flickers, or distorts
- The wall clock's second hand advances in discrete ticks

## Environmental Motion

- The iridescent afterimage dissolves into light, slowly, inside the screen — no scattering, no drift into the room
- The light thins and stays within the screen
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

- A bright, honest smile (the send-off)
- ↓ The everyday word, not a goodbye (行ってらっしゃい)
- ↓ The dissolve into light (inside the screen, going nowhere else)
- ↓ Nothing remaining (the faint light, then cut)

## Emotional Events

- Event: `ニジ's smile` — Emotion: `Brightness without ceremony` — Intensity: `MEDIUM` — Timing: `≈0:05`
- Event: `「――行ってらっしゃい」` — Emotion: `The send-off — not a farewell, not a goodbye` — Intensity: `MEDIUM, tender` — Timing: `≈0:09`
- Event: `The dissolve into light` — Emotion: `A loss that is also a release — without performance, without tears` — Intensity: `CRITICAL — expressed only as the slow dissolve. No facial performance, no tears` — Timing: `≈0:12`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow is the only saturated hue — thinning as she dissolves`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on the ceiling as a soft blue rectangle.
- **`[0:10–0:26]`** — ニジ's rainbow thins as the afterimage dissolves into light, inside the screen. The saturated hue fades into the screen's own cold white.
- **`[0:26–0:30]`** — Only the faint light where ニジ was. Cut to black. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

> ニジ, soft and bright: 「――行ってらっしゃい」. Nothing else. No narration, no voice-over. No tears. It is not a goodbye — the tone is the everyday send-off, light and unhurried.

## Sound Effects

- The wall clock's second hand, dry discrete ticks, present throughout
- Soft futon fabric as she settles, once, at the very start
- A near-silence as the afterimage dissolves

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender. Never sinister, never sentimental — no horror strings, no swelling`
- Emotional Function: `Hold the room's stillness. It may thin as the light dissolves, leaving only room tone and the clock`

---

# 15. CONTINUITY

> 57本は57回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

- **Identity**: 真白 — plain Japanese high-school girl 16–17, shoulder-length dark hair, thin neck, small frame, curved posture over a phone. Same face in every take.
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen.
- **The room**: futon on the floor, curtained window, wall clock, sparse.
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light.
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue.
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers.
- **(seg.10+) ニジ**: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same neck tilt and shoulder-length hair — a rainbow afterimage inside the screen, casting no shadow, dissolving into light by the segment's end.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。

## MUST

- ニジ is present — 真白's own face one step younger — inside the screen only
- Render the iridescent afterimage dissolving into light — **inside the phone screen, going nowhere else**
- ニジ says 「――行ってらっしゃい」 as a send-off, not a goodbye
- End by cutting on the dissolved light, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 56 レンジより）

- **No figure remaining after the dissolve.** After the afterimage dissolves into light, ニジ must not remain — no residual outline, no lingering rainbow
- The light must not scatter into the room — it stays inside the screen
- No tears, no crying, no tear streaks — a loss that is also a release
- No second character — ニジ is inside the screen, never standing in the room

## PREFER

- The dissolve uninterrupted — the whole segment is one held gaze
- Silence over score at the peak
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The dissolve's speed may vary very slightly — it must read as slow
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: the rainbow must dissolve into light, and nothing of ニジ may remain after (ledger 56). This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:10] ニジ — the rainbow, 真白's own face one step younger — smiles once more and says 「――行ってらっしゃい」, the everyday send-off, not a goodbye; [0:10–0:26] THE REVEAL — the iridescent afterimage dissolves into light, slowly, INSIDE the phone screen, going nowhere else, no exit, no scattering, no room, the light thinning and staying within the screen; [0:26–0:30] the screen holds only the faint light where ニジ was — nothing remaining — and the shot cuts on the dissolved light. The dissolve holds the largest share of the duration. Ends on the dissolved light, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. On screen, ニジ — 真白's own face, one step younger, longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, no shadow, smiling — inside the phone screen only; her iridescent afterimage dissolves into light, slowly, INSIDE the screen, going nowhere else, the saturated hue fading into the screen's own cold white. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost nothing moves except the eyes; the body and the finger hold still. ニジ's iridescent afterimage dissolves into light, slowly, inside the screen — no scattering, no drift into the room, the light thinning and staying within the screen. Her lips form 「――行ってらっしゃい」, the faintest motion. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the fingers are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:10] locked close on ニジ — the rainbow, 真白's own face one step younger — smiling, static. [0:10–0:26] hold on ニジ as the iridescent afterimage dissolves into light, inside the screen, going nowhere else, no camera movement, the frame staying within the screen. [0:26–0:30] hold on the faint light where ニジ was; cut precisely on the dissolved light.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, present throughout. Soft futon fabric once at the start. ニジ, soft and bright: 「――行ってらっしゃい」 — the everyday send-off, not a goodbye. No narration, no voice-over, no other speech. Music extremely sparse — a few sustained tones at most — thinning as the light dissolves, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion, no tears.

## Negative Prompt

no figure remaining after the dissolve, no residual afterimage, no lingering rainbow, no tears, no tear streaks, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep12-seg05-30s-01`
- Segment ID: `S56`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_12, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `3 beats, NON_UNIFORM — 10s / 16s / 4s. Dissolve = BEAT 2 at 16s (53%)`
- Camera Events: `3 events as listed in §10. No sustained dolly; all locked holds`
- Action Events: `ACT_SMILE → ACT_SEND → ACT_DISSOLVE`
- Audio Events: `ニジ one line ／ clock ticking throughout ／ music thins as the light dissolves`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the dissolved light`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The dissolve may read as a scattering.** The light must thin inside the screen and go nowhere else. If it drifts into the room, re-prompt for the containment.
- **The model may leave a residual figure.** After the dissolve, ニジ must not remain. The negative prompt front-loads "no figure remaining"; verify the last frames.
- **The word may read as a farewell.** 「行ってらっしゃい」 is a send-off, not a goodbye. Keep the tone light and unhurried.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the dissolve reads well, consider holding it 1–2 seconds longer, taking the time from beat 1.
