# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第7話 S27「文化祭前夜」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**指が休む一日——文化祭前夜、真白は一日中動いていて、スマホを開いたのは数えるほどしかなかった。夜になれば一秒も止まらないあの親指が、昼のあいだは手を離れて、じっとしている。ニジは不在（日中・教室）。S28 の「全部開く」が効くのは、この1本で「開けなかった一日」を刻むから。**

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

> **ニジ is absent this segment**（ledger 27–28 — daytime / classroom）. No other character appears — 美月・小春・湊 do not appear.

---

# 4. ENVIRONMENT

## Location

- ID: `CLASSROOM` (and the school — gym, corridor)
- Name: `教室と学校 (her classroom, and the school)`
- Description: `The day before the culture festival. Morning classroom decoration, a long banner across the corridor, the gym stage check, a whiteboard schedule. Pale flat daylight, slightly overexposed, muted. 真白 among the others, hands busy`

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
- Appearance: `No message text this segment — the phone stays mostly unopened all day; no on-screen text, no UI worth rendering, no captions, no subtitles`
- Narrative Importance: `LOW`
- Visual Importance: `LOW`
- Continuity Importance: `LOW`

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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_07_文化祭前夜、スクリーンタイムを全部開く.md`
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

The culture festival eve. 真白 is in motion all day — morning classroom decoration, afternoon gym stage check — and in that whole day, the number of times she opened her phone could be counted on one hand.

## Beginning

Morning. Classroom decoration. 真白 cuts and pastes origami too. Across the corridor, someone is hanging a long banner.

## Turn

Afternoon. The gym stage check. On the whiteboard, tomorrow's schedule is written, erased, and written again. 真白's body is in motion all day. The phone is barely opened.

## Peak

The time 真白 spent with her phone open that day could be counted on one hand. The thumb that at night never stops for a second rests all through the day.

## Pull（引き — 切れ目）

放課後. Only 真白 remains in the classroom. Everyone else has already gone home. The window slants, the sun sets. One classroom light goes out. Cut on the darkened classroom — the eve.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The day's movement holds 12s (40%) to engrave the busyness.

## Temporal Sequence

- **BEAT 1 `[0:00–0:08]` — 「飾り付け」 — ESTABLISH.** Morning classroom decoration — origami cut and pasted; across the corridor, someone hangs a long banner; 真白's hands are full of paper and glue, not the phone. _Density: SPARSE — quiet daylight, busy hands._
- **BEAT 2 `[0:08–0:20]` — 「ステージ確認」 — longest share.** Afternoon gym stage check — on the whiteboard, tomorrow's schedule written, erased, written again; her body in motion all day, the screen never opened. _Density: DENSE at the head, then the day's rhythm, held._
- **BEAT 3 `[0:20–0:26]` — 「数えるほど」 — the resting finger.** The time 真白 opened her phone that day could be counted on one hand — the thumb that at night never stops for a second rests all through the day. _Density: SPARSE, internal — the only event is an absence._
- **BEAT 4 `[0:26–0:30]` — 「明かりが消えた」 — held, then cut.** 放課後 — only 真白 remains, everyone gone; the window slants, the sun sets, one classroom light goes out. Cut on the darkened classroom. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the morning decoration (0:00–0:08) ／ the stage check and the rewritten schedule (≈0:12) ／ the light going out (≈0:28)`

## Temporal Density

- Sparse regions: `0:00–0:08 (decoration), 0:20–0:26 (the resting finger)`
- Dense regions: `0:08–0:20 (the day's movement)`
- Long continuous action: `0:08–0:20 the day passing in preparation`
- Rapid transitions: `none — the day is a slow, held stretch`

---

# 9. ACTION

## Action — ACT_DECORATE

- ID: `ACT_DECORATE`
- Subject: `MASHIRO`
- Action: `Cuts and pastes origami pieces for the classroom decoration, hands busy with paper and glue`
- Intention: `To prepare the festival — the same thing everyone is doing`
- Intensity: `Low`
- Speed: `Steady, ordinary, unhurried`

### Action Relationship

- Before: `—`
- After: `ACT_CHECK`

## Action — ACT_CHECK

- ID: `ACT_CHECK`
- Subject: `MASHIRO`
- Action: `Afternoon — at the gym stage check; the whiteboard schedule is written, erased, and written again`
- Intention: `To confirm tomorrow's festival — the day's rhythm`
- Intensity: `Low`
- Speed: `Steady; the day flows past her`

### Action Relationship

- Before: `ACT_DECORATE`
- After: `ACT_COUNT`

## Action — ACT_COUNT

- ID: `ACT_COUNT`
- Subject: `MASHIRO`
- Action: `Opens her phone once, briefly — the count of the day is only a few times — and puts it away`
- Intention: `None — she is too busy; the phone is not where her hand goes`
- Intensity: `Medium, internal`
- Speed: `Quick, and then away — the finger rests`

### Action Relationship

- Before: `ACT_CHECK`
- After: `ACT_EVE`

## Action — ACT_EVE

- ID: `ACT_EVE`
- Subject: `MASHIRO`
- Action: `放課後 — alone in the classroom as the others leave; the sun sets; one classroom light goes out`
- Intention: `None — the day ending`
- Intensity: `Low`
- Speed: `Slow, still`

### Action Relationship

- Before: `ACT_COUNT`
- After: `— (cut on the dark)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Wide and level, at classroom and corridor height. Day, then dusk`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Shallow — 真白 sharp, the busy school soft behind`
- Camera Style: `Slow, deliberate, almost still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:08]`** — Static wide of the classroom, morning light, decoration in progress; 真白 among the others, cutting and pasting. A long banner crosses the corridor in the far background.
- **`[0:08–0:14]`** — Cut to the gym, static, wide — the stage check, the whiteboard schedule in frame.
- **`[0:14–0:20]`** — Close on the whiteboard: the schedule written, erased, written again. A slow tilt, unhurried.
- **`[0:20–0:26]`** — Cut to 真白, close — a brief glance at the phone in her hand, then away. Her hands return to the work.
- **`[0:26–0:30]`** — Slow, low two-shot of the classroom emptying. The sun slants and sets. One light goes out. Hold on the dark. Cut.

---

# 11. MOTION

## Subject Motion

- 真白's hands carry the day — cutting, pasting, checking; her body is busy and ordinary
- The single phone-glance is quick, and then the finger rests — the day's whole point
- Her body is in more motion here than in any night segment; the night's stillness is inverted

## Object Motion

- The phone is opened once, briefly, then set down — it does not move on its own, ever
- The whiteboard schedule is written, erased, written again — the day's rhythm
- Nothing glitches, flickers, or behaves unnaturally

## Environmental Motion

- The busy school is alive in soft, out-of-focus movement — distant students, a long banner hanging
- The sun slants and sets through the windows; one light goes out at the end
- No wind, no moving shadows, no particles

## Physical Characteristics

- Weight: `Ordinary. Paper, glue, the phone's heft`
- Inertia: `High for the bodies, low for the hands`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Busy ordinariness (the festival preparation, hands full)
- ↓ The day flowing past (the schedule, the stage check)
- ↓ A quiet distance (the phone barely opened — the finger resting)
- ↓ The eve settling (the empty classroom, the light out)

## Emotional Events

- Event: `The whiteboard schedule written, erased, written again` — Emotion: `The day's rhythm — busy and unbroken` — Intensity: `LOW` — Timing: `≈0:14`
- Event: `The phone opened only a countable few times` — Emotion: `A quiet distance — the finger that never rests at night, resting all day` — Intensity: `MEDIUM, internal` — Timing: `≈0:22`
- Event: `One classroom light goes out` — Emotion: `The eve settling — 文化祭前夜` — Intensity: `LOW` — Timing: `≈0:28`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Pale flat daylight from the windows — soft, slightly overexposed, muted`
- Fill Light: `Even, flat. The school is bright and unbothered`
- Rim Light: `A faint cool edge along 真白's hair from the window`
- Ambient Light: `Day. Muted, low-saturation, nothing dramatic`
- Color Temperature: `≈5600K pale daylight, warming toward dusk at the end`

## Lighting Events

- **`[0:00]`** — Morning light full; long thin shadows across the classroom.
- **`[0:08–0:20]`** — Flat, even daylight through the gym and corridor.
- **`[0:20–0:26]`** — Unchanged — 真白's face flat and quiet.
- **`[0:26–0:30]`** — The sun slants low and golden, then fails. One light goes out; the room falls to near-dark. Cut.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. No narration, no voice-over.

## Sound Effects

- Morning classroom: paper being cut and pasted, low voices, chairs
- A marker on the whiteboard — the schedule being written, erased, written again
- The day's full, ordinary ambience — the world is loud and busy
- At the end, the room empties: receding footsteps, a door, and then one switch — a light going out

## Environment

- Day. Full and ordinary school ambience — busy, unmenacing

## Music

- Style: `Sparse — a few sustained tones, or nothing`
- Tempo: `Slow`
- Mood: `Ordinary, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the day's ordinary surface. It thins toward the close, leaving only the emptying room and the click of the light`

---

# 15. CONTINUITY

> 57本は57回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

- **Identity**: 真白 — plain Japanese high-school girl 16–17, shoulder-length dark hair, thin neck, small frame, curved posture over a phone. Same face in every take.
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen.
- **The room**: futon on the floor, curtained window, wall clock, sparse.
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light.
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue.
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。

## MUST

- Show the day's movement — decoration, stage check, the whiteboard schedule written, erased, written again
- Keep the phone barely opened — the finger rests all day; the count is only a few times
- Keep the daylight pale, flat, slightly overexposed, and muted
- End on the classroom emptying, the sun setting, one light going out — cut on the dark

## MUST NOT（この1本の禁止・開示台帳 27–28 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person, no eyes, no hand but her own. ニジ is absent in the daytime
- **No rainbow, no iridescence, no colored afterimage**
- No 美月, no 小春, no 湊 — no named character but 真白
- No on-screen text — she barely opens the phone; no UI, no captions, no subtitles
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The day's busyness over any single event — the movement is the content
- Background students soft, distant, and out of focus
- Silence over score at the light going out

## ALLOW

- Slight variation in classroom layout, decoration, and background students
- The single phone-glance may be omitted (the phone may stay out of hand the whole day)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not be shown (ledger 27–28 — daytime / classroom); no second character. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school girl at her school on the day before the culture festival. Beats, deliberately uneven: [0:00–0:08] morning, classroom decoration, her hands busy cutting and pasting origami, a long banner hung across the corridor behind; [0:08–0:20] afternoon, the gym stage check, a whiteboard schedule written, erased and written again, the whole day passing in movement, her phone never opened; [0:20–0:26] she opens her phone once, briefly — the day's count is only a few times — and puts it away, the finger that never stops at night resting all day; [0:26–0:30] 放課後, the classroom empties, the sun sets, one classroom light goes out, and the shot cuts on the darkened classroom. The day's movement holds the largest share. Ends on the eve, in the dark.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. By day she wears a standard Japanese school uniform. Scene: her high school the day before the culture festival — classroom decoration, a long banner across the corridor, a gym stage check, a whiteboard schedule. Pale flat daylight, slightly overexposed, equally muted. Background students soft and out of focus. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her hands are busy and ordinary — cutting, pasting, checking. The single phone-glance is quick, then the finger rests. The whiteboard schedule is written, erased, written again — the day's rhythm. The busy school is alive in soft out-of-focus movement — distant students, a long banner hanging. The sun slants and sets; one light goes out at the end. The phone never moves by itself and never glitches, flickers or distorts. Gentle acceleration everywhere. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Wide and level, at classroom and corridor height. Longish lens, shallow depth of field; 真白 sharp, the busy school soft behind. Slow and deliberate, almost still; the camera drifts and never whips or shakes. [0:00–0:08] static wide of the classroom, morning light, decoration in progress, a long banner across the corridor behind. [0:08–0:14] cut to the gym, static, wide, the stage check and the whiteboard schedule in frame. [0:14–0:20] close on the whiteboard, the schedule written, erased, written again; a slow tilt. [0:20–0:26] cut to 真白, close, a brief glance at the phone in her hand, then away. [0:26–0:30] slow low two-shot of the classroom emptying, the sun setting, one light going out; hold on the dark, cut.

## Audio Prompt

Day. Full and ordinary school ambience — paper being cut and pasted, low voices, chairs, a marker on the whiteboard as the schedule is written, erased, written again. No spoken words at all — no dialogue, no narration, no voice-over. At the end the room empties: receding footsteps, a door, and one switch — a light going out. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only the emptying room and the click of the light. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep07-seg01-30s-01`
- Segment ID: `S27`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_07, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 8s / 12s / 6s / 4s. Day's movement = BEAT 2 at 12s (40%)`
- Camera Events: `5 events as listed in §10. No sustained dolly; all static, drift, or tilt`
- Action Events: `ACT_DECORATE → ACT_CHECK → ACT_COUNT → ACT_EVE`
- Audio Events: `no dialogue ／ school ambience throughout ／ music thinning to the light going out`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the dark`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The day may read as empty rather than busy.** The whole point is a full day of movement against the night's stillness. If the preparation looks thin, add more background activity — the banner, the voices, the schedule.
- **The model may add a ghost.** Daytime + "festival eve" is a weaker prior than 2 A.M., but verify anyway — no figure, no rainbow, no eyes.
- **The phone-glance may read as the subject.** It must be a glancing, countable thing, not a focus. If it dominates, cut it to a single beat or omit it.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the day's movement reads as full and the light-out lands as the eve, the segment is done; S28 picks up in that same darkened classroom as she opens the phone.
