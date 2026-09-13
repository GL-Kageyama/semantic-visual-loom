# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第9話 S36「指が、止まった」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**送信ボタンの上で指が浮き、震える——押すでも引くでもない、決めかねて震える所作（第9話の導入）。ニジは在・不透明（画面の中だけ・完全に不透明）。小春は文字のみ。画面文字なし（空の返信ボックスと点滅カーソル、既読無視した一ヶ月前の相談）。S38 の「押す」が重くなるのは、この震えを刻むから。**

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

> **ニジ appears this segment**（ledger 36–40 — 在・不透明, fully opaque; thins from 39–40）. 小春 appears only as text — never as a person, face, or figure.

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
- Appearance: `No message text this segment — only the empty reply box with its blinking cursor, and the month-old consultation from 小春, read and left unanswered, in the history. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
- Continuity Importance: `HIGH`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads short of 2:00 at the hinge of the night`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_09_届かなかった言葉を、いま.md`
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

真白 opens 小春's thread — the consultation message from a month ago, read and never answered — and her finger, over the send button, hovers and trembles. 指が、止まった。

## Beginning

The thread is open, 小春's name at the top. The month-old consultation sits in the history, read and left. The reply box is empty; the cursor blinks.

## Turn

Her finger floats over the send button — not pressing, not pulling back. The pad of the finger trembles, small. 既読無視した相手に、今さら届けるの？

## Peak

The trembling, held. The finger hovers, unable to press, unable to leave. The empty reply box, the blinking cursor, the month-old words she left behind.

## Pull（引き — 切れ目）

指が、止まった。 Cut on the hovering, trembling finger and the blinking cursor. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The trembling finger holds 12s (40%) to engrave the hesitation.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「開く」.** 小春's thread, open. The month-old consultation in the history, read and left unanswered. The reply box is empty; the cursor blinks. _Density: SPARSE — quiet UI, no event. The finger has not moved yet._
- **BEAT 2 `[0:06–0:18]` — 「震える」 — ESTABLISH, longest share.** Her finger floats over the send button — not pressing, not pulling back. The pad of the finger trembles, small and involuntary. _Density: SPARSE — the event is the tremor, held past comfort._
- **BEAT 3 `[0:18–0:26]` — 「既読無視」.** Her face, lit from below by the screen. 既読無視した相手に、今さら届けるの？ The cursor keeps blinking. The finger keeps trembling. _Density: DENSE at the head, then held._
- **BEAT 4 `[0:26–0:30]` — 「止まった」.** The finger holds — still trembling, unable to press, unable to leave. The empty reply box, the blinking cursor. Cut on the finger and the cursor. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the finger hovering over the send button (≈0:08) ／ the tremor held (≈0:10) ／ the blinking cursor (≈0:20) ／ the stopped finger (≈0:28)`

## Temporal Density

- Sparse regions: `0:00–0:06 (opening the thread), 0:06–0:18 (the tremor)`
- Dense regions: `0:18–0:26 (the thought, the blinking cursor)`
- Long continuous action: `0:06–0:18 the hovering, trembling finger`
- Rapid transitions: `none — a held, suspended segment`

---

# 9. ACTION

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MASHIRO`
- Action: `Opens 小春's thread — the month-old consultation, read and left unanswered`
- Intention: `To answer, and not being able to`
- Intensity: `Low`
- Speed: `Steady, then slowing`

### Action Relationship

- Before: `—` (continues from S35's finger stopping on the thread)
- After: `ACT_HOVER`

## Action — ACT_HOVER

- ID: `ACT_HOVER`
- Subject: `MASHIRO`
- Action: `The finger floats over the send button, not pressing, not pulling back`
- Intention: `None — suspended between sending and not sending`
- Intensity: `CRITICAL (the hesitation, expressed as suspension)`
- Speed: `Zero, but trembling`

### Action Relationship

- Before: `ACT_OPEN`
- After: `ACT_TREMBLE`

## Action — ACT_TREMBLE

- ID: `ACT_TREMBLE`
- Subject: `MASHIRO`
- Action: `The pad of the finger trembles, small and involuntary`
- Intention: `None — the body caught between two refusals`
- Intensity: `CRITICAL, entirely internal`
- Speed: `Small, fast tremor inside the stillness`

### Action Relationship

- Before: `ACT_HOVER`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `MASHIRO`
- Action: `The finger holds over the send button, still trembling, unable to press or leave`
- Intention: `To do nothing — the impossibility of the choice`
- Intensity: `CRITICAL, sustained`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_TREMBLE`
- After: `— (cut on the finger and the cursor)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, very shallow. Only the screen or the finger is ever sharp`
- Depth of Field: `Very shallow — the room is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Locked close on the screen and her hand. The thread is open; the empty reply box, the blinking cursor.
- **`[0:06–0:12]`** — A slow drift down and in until the send button and the hovering finger are the frame. Nothing else moves.
- **`[0:12–0:18]`** — Absolutely locked on the finger over the send button — the tremor is the only motion. Hold past comfort.
- **`[0:18–0:26]`** — Cut to her face, lit from below by the screen, the cursor blinking in the foreground. Static, close.
- **`[0:26–0:30]`** — Back to the finger and the empty reply box together. Cut on the trembling finger and the blinking cursor.

---

# 11. MOTION

## Subject Motion

- The finger carries essentially all the movement — and it is a tremor, not a gesture
- She opens the thread with one steady movement; from then on only the finger trembles
- The rest of her body holds absolutely still
- The tremor is small, involuntary, and continuous

## Object Motion

- The phone does not move on its own. Ever
- Screen content is almost still — only the cursor blinks, in a steady rhythm
- The wall clock's second hand advances in discrete ticks, faint behind

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only other motion

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand`
- Inertia: `High for her body, near-zero for the finger — but the finger is held in suspension`
- Acceleration: `None. Nothing begins or ends; the tremor is a vibration, not a movement`
- Fluidity: `Limited-animation — one held gesture, a vibration inside it`
- Impact: `None. The only event is a finger that cannot move`

---

# 12. EMOTION

## Emotional Arc

- Quiet return (opening the thread she abandoned)
- ↓ Suspension (the finger hovering — neither press nor withdraw)
- ↓ The month-old guilt (既読無視した相手に、今さら)
- ↓ Paralysis (the held tremor, the choice that will not come)

## Emotional Events

- Event: `The finger floats over the send button` — Emotion: `Suspension — the choice not made` — Intensity: `CRITICAL, expressed only as the hovering finger` — Timing: `≈0:08, held to 0:18`
- Event: `既読無視した相手に、今さら` — Emotion: `The month-old guilt, surfacing as stillness` — Intensity: `MEDIUM, internal` — Timing: `≈0:20`
- Event: `The cursor blinks, and nothing else moves` — Emotion: `Paralysis` — Intensity: `HIGH, but motionless` — Timing: `0:26–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and finger from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. No change through the segment`

## Lighting Events

- **`[0:00]`** — Screen already on. Its light lies on the ceiling as a soft blue rectangle.
- **`[0:06–0:18]`** — The camera closes on the finger; the screen's light catches the knuckle as a thin bright line in the dark.
- **`[0:18–0:26]`** — Her face lit from below, almost to silhouette; the cursor a small bright point in the foreground.
- **`[0:26–0:30]`** — Unchanged. Cut on the finger and the cursor.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The thought 既読無視した相手に、今さら is internal, not spoken. No narration, no voice-over.

## Sound Effects

- The blinking cursor — a very faint, close, electronic tick, steady through the held beats
- The wall clock's second hand, dry discrete ticks, faint under the cursor
- A very soft breath, once, as the finger begins to tremble

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a cursor gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the tremor. It may thin toward the close, leaving only room tone, the cursor, and the clock`

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

- ニジ present, **fully opaque** (不透明) — 真白's own face one step younger, a rainbow afterimage, inside the screen only
- Let the finger hover over the send button and tremble — not pressing, not pulling back
- Show the reply box empty with a blinking cursor
- End by cutting on the trembling finger and the blinking cursor, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 36–40 レンジより）

- **No full disappearance.** ニジ must not vanish, dissolve, or fade out — she thins only from S39, never here
- ニジ stays inside the screen; she never stands in the room at human scale
- 小春 appears only as text — never as a person, face, or figure
- No other person, crowd, or silhouette
- No on-screen subtitles or captions burned in (the phone UI is diegetic, not a subtitle)

## PREFER

- The tremor held longer than is comfortable — the whole segment is one suspended gesture
- Silence over score
- Negative space over detail; the room may be nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The drift toward the finger may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ is present, fully opaque, inside the screen only (ledger 36–40 — she thins only from S39); 小春 appears only as text. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at night. ニジ is present, fully opaque, inside the screen. Beats, deliberately uneven: [0:00–0:06] 小春's chat thread is open, the month-old consultation in the history read and left unanswered, the reply box empty, the cursor blinking; [0:06–0:18] THE HESITATION — her finger floats over the send button, not pressing and not pulling back, the pad of the finger trembling small and involuntary, held past comfort; [0:18–0:26] her face lit from below, the thought 既読無視した相手に、今さら届けるの？ unspoken, the cursor still blinking, the finger still trembling; [0:26–0:30] the finger holds, unable to press or leave, and the shot cuts on the trembling finger and the blinking cursor. The hesitation holds the largest share of the duration. Ends on the stopped finger, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ, inside the screen only, is 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same tilt of the head — a blurred rainbow afterimage resolved into that outline, colors drifting slowly blue → green → blue, no shadow anywhere, fully opaque. The screen shows an open chat thread with an empty reply box and a blinking cursor, in ordinary Japanese UI in cold blue-white. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers; the body holds absolutely still. The finger floats over the send button and trembles — a small, involuntary, continuous vibration inside the stillness, not a press and not a withdrawal. She opens the thread with one steady movement, then nothing moves but the trembling finger and the blinking cursor. ニジ's rainbow afterimage drifts slowly blue → green → blue, inside the screen. Ordinary weight and inertia: the phone has heft, the futon compresses. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the finger is sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked close on the screen and hand, the thread open, the empty reply box, the blinking cursor. [0:06–0:12] a slow drift down and in until the send button and the hovering finger are the frame. [0:12–0:18] absolutely locked on the finger over the send button, the tremor the only motion, held past comfort. [0:18–0:26] cut to her face lit from below, the cursor blinking in the foreground, static. [0:26–0:30] back to the finger and the empty reply box together; cut on the trembling finger and the blinking cursor.

## Audio Prompt

Almost silent. Deep quiet night room tone. A very faint, close electronic tick of the blinking cursor, steady through the held beats. The wall clock's dry discrete ticking, faint under the cursor. One soft breath as the finger begins to tremble. No spoken words at all — the thought is internal, not voiced. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only room tone, the cursor, and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no full disappearance, no complete vanishing, no dissolving into nothing, no fading out to invisibility, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep09-seg01-30s-01`
- Segment ID: `S36`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_09, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 12s / 8s / 4s. Tremor = BEAT 2 at 12s (40%)`
- Camera Events: `5 events as listed in §10. One slow drift (0:06–0:12)`
- Action Events: `ACT_OPEN → ACT_HOVER → ACT_TREMBLE → ACT_HOLD`
- Audio Events: `no dialogue ／ cursor tick throughout ／ clock faint under the cursor`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the trembling finger`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The tremor may read as a tap.** A generated finger may press the button instead of hovering over it. The hover is the point — if it presses, tighten the frame on the hovering finger and lengthen the hold.
- **ニジ may vanish or fade.** This range forbids full disappearance; she must stay fully opaque here. If she thins, restore her opacity and verify frame by frame.
- **The model may add 小春 as a person.** 小春 is text-only. If a face or figure appears, it is a failure of the ledger.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the tremor reads as suspension, S37 (……無理だよ) picks up with the finger pulling back and the refusal.
