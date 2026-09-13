# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第6話 S23「名前が流れる」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「流しながら眺める」——流れる名前が、画面の文字から記憶へ変わる。浮かんでは沈む記憶（小学生の隣の席／一年の同じ部活／文化祭の準備）に、名前を押し込む。頂点は「全部、預けてたんだ」の一言。ニジは在・不透明（台帳 22–25）。画面文字なし。**

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
- A blurred rainbow afterimage that resolves into that outline. Colors drift slowly: blue → green → blue.
- The outline is slightly blurred at the edges. **No shadow anywhere** — unlike 真白's solid, defined outline.
- Exists **inside the screen**. Never stands in the room at human scale.

### Behavior

- Personality: `Bright, teasing, unguarded — she smiles more honestly than 真白 can. She never cries. She calls 真白「おまえ」`
- Continuity: `her opacity is a strict function of the segment number (see the ledger); it never varies within a beat except in seg.55`

> **No other character appears this segment.** ニジ is present — fully opaque, inside the screen only (ledger 22–25: 在・不透明・リストを指す). The names are text only.

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
- Appearance: `No fixed on-screen text this segment — a flowing column of names, no single string to reproduce. Rendered as an ordinary phone scrolls a list: cold blue-white on dark UI`
- Narrative Importance: `MEDIUM`
- Visual Importance: `LOW`
- Continuity Importance: `MEDIUM`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads 2:00 at the hinge of the night`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_06_宛先リスト、三十二人.md`
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

The list flows. 真白 watches the names as if reading them aloud — names she knows. Names she had forgotten. Names she never answered. Names that never answered her. To each, a brief memory surfaces and sinks.

## Beginning

The flowing list. Her finger scrolls the names slowly. The names she knows pass from bottom to top.

## Turn

Names forgotten. Names never answered. Names that never answered her. A memory surfaces and sinks for each — the elementary-school seatmate, the first-year clubmate, the festival-prep classmate.

## Peak

「全部、預けてたんだ」— 真白 murmurs it. ニジ answers. 「うん。――おまえは、思うより、ずっとたくさんの人に、時間を渡してる」.

## Pull（引き — 切れ目）

――全部、宛先. The flowing list will not stop. Cut on the flowing list, one name slipping past the edge — all of them, addressees.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The flow of names holds 9s (30%); the exchange holds 9s.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the bedroom; the flow is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:09]` — 「流れる名前」 — longest continuous action.** The list flows. Her finger scrolls the names slowly. The names she knows pass from bottom to top — a column of names. _Density: SPARSE — one long continuous scroll, almost no event._
- **BEAT 2 `[0:09–0:17]` — 「浮かんでは沈む」.** Names forgotten, names never answered, names that never answered her. The elementary-school seatmate. The first-year clubmate. The festival-prep classmate. To each, a brief memory surfaces and sinks. _Density: DENSE — the names become memory._
- **BEAT 3 `[0:17–0:26]` — 「全部、預けてたんだ」 — PEAK.** 真白 murmurs it. 「全部、預けてたんだ」. ニジ answers. 「うん。――おまえは、思うより、ずっとたくさんの人に、時間を渡してる」. _Density: SPARSE, internal — a quiet realization spoken aloud._
- **BEAT 4 `[0:26–0:30]` — 「全部、宛先」.** ――全部、宛先. The flowing list will not stop. Cut on the flowing list. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the flowing column of names (0:00–0:09) ／ the memories surfacing (≈0:12) ／ the exchange (≈0:19)`

## Temporal Density

- Sparse regions: `0:00–0:09 (the flowing names), 0:26–0:30 (the held pull)`
- Dense regions: `0:09–0:17 (the memories)`
- Long continuous action: `0:00–0:09 the list flowing under the finger`
- Rapid transitions: `none — a single, quiet realization`

---

# 9. ACTION

## Action — ACT_FLOW

- ID: `ACT_FLOW`
- Subject: `MASHIRO`
- Action: `Finger scrolls the list slowly, steadily — リストを流しながら眺める`
- Intention: `To read the names as they pass`
- Intensity: `Low`
- Speed: `Slow, even, continuous`

### Action Relationship

- Before: `— (continues from S22's first touch)`
- After: `ACT_RECALL`

## Action — ACT_RECALL

- ID: `ACT_RECALL`
- Subject: `MASHIRO`
- Action: `Eyes move over the passing names; each one surfaces a brief memory that sinks again`
- Intention: `None — the names do this on their own`
- Intensity: `Medium, internal`
- Speed: `Slow, drifting`

### Action Relationship

- Before: `ACT_FLOW`
- After: `ACT_SPEAK`

## Action — ACT_SPEAK

- ID: `ACT_SPEAK`
- Subject: `MASHIRO`
- Action: `Murmurs 「全部、預けてたんだ」 — the finger does not stop`
- Intention: `To say aloud what the list has made plain`
- Intensity: `Medium, suppressed`
- Speed: `A murmur, then stillness under the flow`

### Action Relationship

- Before: `ACT_RECALL`
- After: `ACT_NIJI`

## Action — ACT_NIJI

- ID: `ACT_NIJI`
- Subject: `NIJI`
- Action: `Answers 「うん。――おまえは、思うより、ずっとたくさんの人に、時間を渡してる」 — bright, unguarded, inside the screen`
- Intention: `To confirm, lightly — she never says わたし`
- Intensity: `Low`
- Speed: `Ordinary, gentle`

### Action Relationship

- Before: `ACT_SPEAK`
- After: `— (cut on the flowing list)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Only the screen or the finger are ever sharp`
- Depth of Field: `Very shallow — the room is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:09]`** — Locked close on the screen as the list flows — the column of names passing upward under the glass. Almost no camera movement.
- **`[0:09–0:17]`** — A slow, barely perceptible drift along the flowing names. The names are slightly out of focus at the edges; the finger steers below.
- **`[0:17–0:22]`** — Cut to her face, lit from below, the finger in the foreground still scrolling. She murmurs the line.
- **`[0:22–0:26]`** — Brief return to the screen — ニジ inside it, opaque, bright, answering.
- **`[0:26–0:30]`** — Locked on the flowing list; one name slips past the edge. Cut on the list.

---

# 11. MOTION

## Subject Motion

- Her finger carries the movement — a slow, even scroll; the rest of her body holds
- The murmur moves her lips only faintly; the finger does not stop
- ニジ, inside the screen, answers in place — fully opaque; her colors drift slowly blue → green → blue

## Object Motion

- The phone does not move on its own. Ever
- The list flows by ordinary UI scrolling only — names passing upward, no glitch, no flicker
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion in the room
- ニジ's rainbow, inside the screen, is the only saturated hue

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her finger`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet recognition (the names as they pass)
- ↓ Memory surfacing and sinking (each name carries a short life)
- ↓ The realization, spoken (全部、預けてたんだ)
- ↓ The weight, held (全部、宛先 — and the list will not stop)

## Emotional Events

- Event: `The flowing names` — Emotion: `Quiet recognition — these are her people` — Intensity: `LOW` — Timing: `0:00–0:09`
- Event: `The memories surfacing and sinking` — Emotion: `A faint ache — the forgotten and the unreturned` — Intensity: `MEDIUM, internal` — Timing: `≈0:12`
- Event: `「全部、預けてたんだ」` — Emotion: `The realization, spoken — and ニジ's gentle confirmation` — Intensity: `HIGH, but quiet` — Timing: `≈0:19`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo; ニジ's rainbow is the only saturated hue, and it lives inside the screen`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on the ceiling as a soft blue rectangle.
- **`[0:00–0:09]`** — The list flows; the light is steady, cold.
- **`[0:17–0:22]`** — Cut to her face, lit from below, nearly silhouetted; the knuckles bright.
- **`[0:22–0:26]`** — ニジ, inside the screen, is the only color not drowned in indigo.
- **`[0:26–0:30]`** — The list fills the frame, cold blue-white. Cut on the list.

---

# 14. AUDIO

## Dialogue

- 真白: 「全部、預けてたんだ」 — a quiet murmur, almost to herself
- ニジ: 「うん。――おまえは、思うより、ずっとたくさんの人に、時間を渡してる」 — soft, bright, unguarded

> The names are **not read aloud.** No voice recites the list. No narration, no voice-over.

## Sound Effects

- The soft friction of a finger on glass, close and continuous — the flow's pulse
- The wall clock's dry discrete ticking, faint throughout
- Soft futon fabric as she shifts, once

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the flow. It may thin toward the exchange, leaving only room tone, the finger, and the clock`

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

- Show the list flowing — a column of names, no fixed on-screen string to reproduce (the names pass by)
- Speak only the two lines: 真白 「全部、預けてたんだ」 ／ ニジ 「うん。――おまえは、思うより、ずっとたくさんの人に、時間を渡してる」
- ニジ present, fully opaque, inside the screen only — 真白's own face one step younger, a rainbow afterimage
- The finger keeps scrolling through the murmur; it never stops
- End on the flowing list, cut on the pull ――全部、宛先

## MUST NOT（この1本の禁止・開示台帳 22–25 レンジより）

- **ニジ must not be transparent or translucent.** In S22–25 she is fully opaque (不透明)
- **ニジ must not say わたし.** She calls 真白 「おまえ」 and never refers to herself in first person
- ニジ never leaves the screen — she never stands in the room at human scale
- No rainbow or iridescence anywhere except ニジ herself, inside the screen
- No second character in the room — the names are text only
- Do not voice the list — the names are not read aloud, whispered, or narrated

## PREFER

- The flow uninterrupted for as long as possible — the whole segment is one held scroll
- Silence over score at the exchange
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The names may be generic and slightly out of focus at the edges — only the flow must read
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear fully opaque, inside the screen only (ledger 22–25 — 在・不透明・リストを指す), must not be transparent or translucent, and must not say わたし. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:09] her finger scrolls a list of names, a column flowing upward under the glass, the screen the only light; [0:09–0:17] the passing names surface brief memories — an elementary-school seatmate, a first-year clubmate, a festival-prep classmate — each one surfacing and sinking; [0:17–0:26] 真白 murmurs 全部、預けてたんだ, and ニジ, inside the screen, answers うん。――おまえは、思うより、ずっとたくさんの人に、時間を渡してる; [0:26–0:30] the list keeps flowing, one name slipping past the edge, and the shot cuts on the flowing list. The flow holds the largest share of the duration. Ends on the list, flowing, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. Night is deep indigo lit solely by the phone screen from below her face, her face nearly silhouetted, shadows soft and deep, no fill. The phone screen shows an ordinary Japanese UI in cold blue-white — a flowing column of names, no fixed text required. ニジ (Niji), inside the phone screen only, never in the room: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same head-tilt — a rainbow afterimage, fully opaque, no shadow, colors drifting slowly blue → green → blue; her rainbow is the only saturated hue. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers. Her finger scrolls the list in a slow, even, continuous motion; the names pass upward in ordinary UI scrolling, no glitch, no flicker. The murmur moves her lips only faintly; the finger does not stop. ニジ, inside the screen, answers in place, fully opaque; her rainbow afterimage drifts slowly blue → green → blue. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere. The phone never moves by itself; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; only the screen or the finger are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:09] locked close on the screen as the list flows, almost no movement. [0:09–0:17] a slow, barely perceptible drift along the flowing names. [0:17–0:22] cut to her face lit from below, the finger still scrolling in the foreground, as she murmurs. [0:22–0:26] brief return to the screen, ニジ inside it answering. [0:26–0:30] locked on the flowing list, one name slipping past the edge; cut on the list.

## Audio Prompt

Deep quiet night room tone. The soft friction of a finger on glass, close and continuous — the flow's pulse. The wall clock's dry discrete ticking, faint throughout. Soft futon fabric as she shifts once. Two lines of dialogue only: 真白 murmurs 全部、預けてたんだ, quiet and almost to herself; ニジ answers うん。――おまえは、思うより、ずっとたくさんの人に、時間を渡してる, soft, bright, unguarded. The names are not read aloud — no voice recites the list. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the exchange and leaving only room tone, the finger, and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparent figure, no translucent apparition, no see-through ghost, no ghost standing in the room at human scale, no figure outside the phone screen, no わたし spoken by ニジ, no rainbow or iridescence apart from ニジ herself, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep06-seg02-30s-01`
- Segment ID: `S23`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_06, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 9s / 8s / 9s / 4s. Flow = BEAT 1 at 9s (30%)`
- Camera Events: `5 events as listed in §10. No sustained dolly; all drift or static`
- Action Events: `ACT_FLOW → ACT_RECALL → ACT_SPEAK → ACT_NIJI`
- Audio Events: `two lines of dialogue ／ finger on glass throughout ／ names never voiced`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the flowing list`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ transparency.** The model may render ニジ as a see-through ghost, or standing in the room. She must be fully opaque and inside the screen only. Verify frame by frame.
- **ニジ saying わたし.** Her line must call 真白 「おまえ」 and never slip into first person. Check the audio closely.
- **The flow may not read.** A generated scroll may look floaty or random. The even, continuous motion is the point — if it reads as noise, hold the framing tighter on the finger.
- **The list read aloud.** The model may want to voice the names. The negative prompt forbids narration; confirm no name is spoken.

## Changes

- _(none yet)_

## Next Generation

- If the flow reads well, S24 depends on the same list stopping at the top name — carry the screen plate forward.
