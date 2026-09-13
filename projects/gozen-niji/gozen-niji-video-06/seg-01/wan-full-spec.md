# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第6話 S22「三十二人」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「触れて流す」の初演——アプリの使用時間から宛先ごとの預けた時間へ、画面が切り替わる。指を置くとリストが流れ始める。最大の秒は「三十二人」という数の開示。三つの名前（美月 3時間14分／お母さん 1時間02分／小春 0時間47分）の数字の傾きに感情を押し込む。ニジは在・不透明・リストを指す（台帳 22–25）。**

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

> **No other character appears this segment.** ニジ is present — fully opaque, inside the screen only, pointing at the list (ledger 22–25: 在・不透明・リストを指す). The three names are text only.

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
- Appearance: `The addressee list — per-addressee deposited time, not per-app usage — thirty-two names, lower names shorter, higher names longer. At the top, three names and their times, rendered exactly character-for-character: 美月…………3時間14分 ／ お母さん……1時間02分 ／ 小春…………0時間47分. Cold blue-white on dark UI`
- Narrative Importance: `HIGH`
- Visual Importance: `HIGH`
- Continuity Importance: `HIGH`

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

2:00 A.M. 真白 opens the hidden screen beyond the screen-time log ニジ showed her — not per-app usage, but per-addressee deposited time. Thirty-two names line up. The addressee list was thirty-two people.

## Beginning

2:00 A.M. The screen's light falls cold into the room. 真白's finger opens the hidden screen deep in the screen-time settings.

## Turn

The list. Thirty-two people. When her finger rests on it, the list begins to flow slowly — lower names shorter, higher names longer. Three names sit at the top:

美月…………3時間14分
お母さん……1時間02分
小春…………0時間47分

## Peak

Thirty-two people. The people 真白 deposited time with this year. Each name carries a number. The list keeps flowing.

## Pull（引き — 切れ目）

The camera closes on the three names. The flowing list continues, and the thirty-two are still not fully seen. Cut on the flowing list and the three names, the count of thirty-two hanging over them.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The reveal of the list holds 10s (33%); the finger's first touch holds 9s.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the bedroom; the reveal is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「隠れた画面」.** Night, 2:00 A.M. 真白's finger opens the hidden screen deep in the screen-time settings — not per-app usage, but the column of addressees. _Density: SPARSE — quiet UI movement, no event. The finger is still moving._
- **BEAT 2 `[0:06–0:16]` — 「三十二人」 — REVEAL, longest share.** The list appears. Thirty-two names. Lower names shorter, higher names longer. At the top, three names: 美月 3時間14分 / お母さん 1時間02分 / 小春 0時間47分. _Density: DENSE at the head (list → names and numbers), then the list held._
- **BEAT 3 `[0:16–0:25]` — 「触れて流す」.** Her finger touches the list, and it begins to flow slowly. Names pass from bottom to top. The slope of the numbers reads. _Density: TRANSITION — one quiet motion, the flow begins._
- **BEAT 4 `[0:25–0:30]` — 「三つの名前」.** The camera holds the three names large and still. The list keeps flowing, and the thirty-two are still not fully seen. Cut on the list. _Density: HELD — then cut precisely on the pull. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the list revealing 32 addressees (≈0:08) ／ the finger's first touch starting the flow (≈0:17) ／ the three names held (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:06 (opening the hidden screen), 0:25–0:30 (the three names held)`
- Dense regions: `0:06–0:16 (the list reveal)`
- Long continuous action: `0:16–0:25 the list flowing under the finger`
- Rapid transitions: `none — a single, quiet reveal`

---

# 9. ACTION

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MASHIRO`
- Action: `Finger taps into the hidden screen deep in the screen-time settings — per-addressee deposited time, not per-app usage`
- Intention: `To see what ニジ showed her`
- Intensity: `Low`
- Speed: `Steady, practiced`

### Action Relationship

- Before: `— (continues from the preceding episode's hidden screen)`
- After: `ACT_TOUCH`

## Action — ACT_TOUCH

- ID: `ACT_TOUCH`
- Subject: `MASHIRO`
- Action: `Her finger rests on the list — 触れて流す — and the list begins to flow under it`
- Intention: `To read it. The touch is what starts the flow`
- Intensity: `Low`
- Speed: `A single light touch, then the flow`

### Action Relationship

- Before: `ACT_OPEN`
- After: `ACT_READ`

## Action — ACT_READ

- ID: `ACT_READ`
- Subject: `MASHIRO`
- Action: `Eyes move over the three names — 美月, お母さん, 小春 — and register the number: thirty-two`
- Intention: `To understand the scale`
- Intensity: `Medium, internal`
- Speed: `Slow, and slowing`

### Action Relationship

- Before: `ACT_TOUCH`
- After: `— (cut on the list)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Only the screen or the finger are ever sharp`
- Depth of Field: `Very shallow — the room is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Locked close on the screen and her hand as the hidden screen opens. Optional: an imperceptibly slow push-in.
- **`[0:06–0:16]`** — One slow continuous dolly in on the list — the column of names, then the three names at the top with their numbers. The reveal's single sustained move.
- **`[0:16–0:22]`** — Slight tilt as the finger touches and the list begins to flow. The names pass upward under the glass.
- **`[0:22–0:30]`** — Locked on the three names, filling the frame — 美月 3時間14分, お母さん 1時間02分, 小春 0時間47分. The list still flows faintly behind. Cut on the list.

---

# 11. MOTION

## Subject Motion

- Her finger carries essentially all the movement; the rest of her body holds
- The touch is a single light contact — then the list flows, and the finger only steers it
- ニジ, inside the screen, points toward the list, fully opaque; her colors drift slowly blue → green → blue

## Object Motion

- The phone does not move on its own. Ever
- The list flows by ordinary UI scrolling only — names passing upward, no glitch, no flicker
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion in the room
- ニジ's rainbow, inside the screen, is the only saturated hue

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet intent (opening the hidden screen)
- ↓ Recognition of scale (thirty-two people — not fear, a slow awe)
- ↓ The flow begins (the finger touches; the names become her history)
- ↓ The weight, held (three names, and thirty-two still unseen)

## Emotional Events

- Event: `The list reveals thirty-two addressees` — Emotion: `Recognition of scale` — Intensity: `HIGH` — Timing: `≈0:08`
- Event: `The finger touches and the list flows` — Emotion: `The names beginning to become hers` — Intensity: `MEDIUM, internal` — Timing: `≈0:17`
- Event: `The three names held on screen` — Emotion: `The weight of thirty-two, only just visible` — Intensity: `MEDIUM, suppressed` — Timing: `0:25–0:30`

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
- **`[0:06–0:16]`** — As the camera closes on the list, its light dominates the frame; her face falls almost to silhouette.
- **`[0:16–0:25]`** — The list flows; ニジ's rainbow, inside the screen, is the only color not drowned in indigo.
- **`[0:25–0:30]`** — The three names fill the frame, cold blue-white. Cut on the list.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. ニジ is present but silent. The names are read, not spoken. No narration, no voice-over.

## Sound Effects

- The soft friction of a finger on glass, close and continuous
- The wall clock's dry discrete ticking, faint throughout
- Soft futon fabric as she shifts, once, at the start

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the flow. It may thin toward the close, leaving only room tone, fabric, and the clock`

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

- Render the on-screen Japanese exactly, character-for-character: `美月…………3時間14分` ／ `お母さん……1時間02分` ／ `小春…………0時間47分`
- Show the list as thirty-two addressees — per-addressee deposited time, not per-app usage
- The finger touches the list and it begins to flow; lower = shorter, higher = longer
- ニジ present, fully opaque, inside the screen only, pointing at the list — 真白's own face one step younger, a rainbow afterimage
- End on the three names held, cut on the flowing list

## MUST NOT（この1本の禁止・開示台帳 22–25 レンジより）

- **ニジ must not be transparent or translucent.** In S22–25 she is fully opaque (不透明)
- **ニジ must not say わたし.** She calls 真白 「おまえ」 and never refers to herself in first person
- ニジ never leaves the screen — she never stands in the room at human scale
- No rainbow or iridescence anywhere except ニジ herself, inside the screen
- No second character in the room — no 美月, no 湊; the names are text only

## PREFER

- Framing the three names large, straight-on and held — legibility is the whole point
- Silence over score
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in during beat 1 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear fully opaque, inside the screen only (ledger 22–25 — 在・不透明・リストを指す), must not be transparent or translucent, and must not say わたし; the three names must render exactly. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:06] her finger opens the hidden screen deep in the screen-time settings — not per-app usage, but per-addressee deposited time; [0:06–0:16] THE REVEAL — a list of thirty-two names, lower names shorter, higher names longer, and at the top three names read 美月…………3時間14分, お母さん……1時間02分, 小春…………0時間47分, and the camera closes slowly until the list fills the frame; [0:16–0:25] her finger touches the list and it begins to flow under the glass, names passing upward; [0:25–0:30] the camera locks on the three names held, the list still flowing faintly behind, and the shot cuts on the list. The reveal holds the largest share of the duration. Ends on the list, held, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. Night is deep indigo lit solely by the phone screen from below her face, her face nearly silhouetted, shadows soft and deep, no fill. The phone screen shows an ordinary Japanese UI in cold blue-white — a list of thirty-two addressees with times, the top three reading exactly 美月…………3時間14分, お母さん……1時間02分, 小春…………0時間47分. ニジ (Niji), inside the phone screen only, never in the room: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same head-tilt — a rainbow afterimage, fully opaque, no shadow, colors drifting slowly blue → green → blue, pointing at the list; her rainbow is the only saturated hue. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers. Her finger opens the hidden screen, then rests on the list in a single light touch, and the list flows under it in ordinary UI scrolling — names passing upward, no glitch, no flicker. ニジ, inside the screen, points at the list and stays fully opaque; her rainbow afterimage drifts slowly blue → green → blue. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere. The phone never moves by itself; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; only the screen or the finger are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked close on the screen and hand as the hidden screen opens, optionally an imperceptibly slow push-in. [0:06–0:16] one slow continuous dolly in on the list — the column of names, then the three names with their numbers. [0:16–0:22] a slight tilt as the finger touches and the list begins to flow. [0:22–0:30] locked on the three names filling the frame, the list still flowing faintly behind; cut on the list.

## Audio Prompt

Almost silent. Deep quiet night room tone. The soft friction of a finger on glass, close and continuous. The wall clock's dry discrete ticking, faint throughout. Soft futon fabric as she shifts once at the start. No spoken words at all — the names are read, not spoken; ニジ is present but silent. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only room tone, fabric, and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparent figure, no translucent apparition, no see-through ghost, no ghost standing in the room at human scale, no figure outside the phone screen, no わたし spoken by ニジ, no rainbow or iridescence apart from ニジ herself, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep06-seg01-30s-01`
- Segment ID: `S22`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_06, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 10s / 9s / 5s. Reveal = BEAT 2 at 10s (33%)`
- Camera Events: `4 events as listed in §10. One sustained dolly (0:06–0:16)`
- Action Events: `ACT_OPEN → ACT_TOUCH → ACT_READ`
- Audio Events: `no dialogue ／ finger on glass ／ clock faint ／ ニジ silent`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the list`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The three names carry the reveal. If they render as noise the segment fails. Check first; if unusable, generate the screen as a plate and composite the text in post.
- **ニジ transparency.** The strongest risk: the model may render ニジ as a see-through ghost, or standing in the room. She must be fully opaque and inside the screen only. The negative prompt front-loads this; verify frame by frame.
- **ニジ saying わたし.** She must never speak of herself in first person. This segment is wordless, so it is mostly safe — but confirm she stays silent and does not mouth a name for herself.
- **The list may not read as thirty-two.** If the count is illegible, the three names at the top are the evidence — hold them longer.

## Changes

- _(none yet)_

## Next Generation

- If the names render cleanly, S23 depends on the same list flowing — carry the screen plate forward.
