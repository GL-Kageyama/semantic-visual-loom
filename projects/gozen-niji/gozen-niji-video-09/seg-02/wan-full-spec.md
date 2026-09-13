# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第9話 S37「……無理だよ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**指が引く——押せない、と身体が先に答える「無理」。カーテンの外が白む夜明けと、急かさず泣きもせずただ待つニジの沈黙（ニジは無言・在・不透明）。小春は文字のみ。画面文字なし。S38 の「押す」が重くなるのは、この1本で一度「押せない」を刻むから。**

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
- Appearance: `No message text this segment — only the empty reply box with its blinking cursor. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
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

The finger cannot move. Outside the curtain the sky is lightening. 真白 murmurs — 「……無理」「私、こんなの、――無理だよ」 — and ニジ, in the corner of the screen, says nothing and only waits.

## Beginning

The reply box still empty, the cursor still blinking. The finger that hovered over the send button now will not move — cannot move. The night has thinned to the first gray before dawn.

## Turn

The finger pulls back. The curtain is whitening; morning sounds begin far away. 私、こんなの、――無理だよ。

## Peak

真白 murmurs 「……無理」 and then 「私、こんなの、――無理だよ」, into the empty dark. ニジ does not hurry her. She does not cry. She only waits.

## Pull（引き — 切れ目）

――待ってる。 Cut on ニジ, silent and still in the corner of the screen, and on 真白's refusal, hanging in the air. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The refusal holds 10s (33%); the finger's pulling back is held 9s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「動かない」.** The reply box still empty, the cursor blinking. The finger that hovered over the send button will not move. _Density: SPARSE — the event is the absence of motion._
- **BEAT 2 `[0:06–0:15]` — 「引く」.** The finger pulls back from the send button. Beyond the curtain the sky whitens; morning sounds begin, far away. _Density: TRANSITION — the dawn, and the finger's surrender._
- **BEAT 3 `[0:15–0:25]` — 「無理」 — PEAK, longest share.** 真白 murmurs 「……無理」 — then 「私、こんなの、――無理だよ」. Almost nothing moves. The words are small, and they hang. _Density: DENSE at the head, then held._
- **BEAT 4 `[0:25–0:30]` — 「待つ」.** ニジ, in the corner of the screen, says nothing. She does not hurry, does not cry. She only waits. Cut on her silence. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the finger pulling back (≈0:08) ／ the curtain whitening (≈0:10) ／ 「……無理」 (≈0:16) ／ 「無理だよ」 (≈0:20)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the finger that will not move), 0:25–0:30 (ニジ's silence)`
- Dense regions: `0:15–0:25 (the refusal)`
- Long continuous action: `0:06–0:15 the finger pulling back, the sky whitening`
- Rapid transitions: `none — a held, quiet segment`

---

# 9. ACTION

## Action — ACT_FROZEN

- ID: `ACT_FROZEN`
- Subject: `MASHIRO`
- Action: `The finger, which hovered over the send button, will not move`
- Intention: `None — the body refuses before she does`
- Intensity: `Medium`
- Speed: `Zero`

### Action Relationship

- Before: `—` (continues from S36's hovering, trembling finger)
- After: `ACT_PULLBACK`

## Action — ACT_PULLBACK

- ID: `ACT_PULLBACK`
- Subject: `MASHIRO`
- Action: `The finger draws back from the send button, slowly, giving up`
- Intention: `To stop — 無理`
- Intensity: `CRITICAL (the surrender, expressed as withdrawal)`
- Speed: `Slow, heavy, reluctant`

### Action Relationship

- Before: `ACT_FROZEN`
- After: `ACT_MURMUR`

## Action — ACT_MURMUR

- ID: `ACT_MURMUR`
- Subject: `MASHIRO`
- Action: `She murmurs 「……無理」 and 「私、こんなの、――無理だよ」, barely moving her lips`
- Intention: `To say the thing she could not say to 小春`
- Intensity: `CRITICAL, almost inaudible`
- Speed: `Very slow, small`

### Action Relationship

- Before: `ACT_PULLBACK`
- After: `ACT_WAIT`

## Action — ACT_WAIT

- ID: `ACT_WAIT`
- Subject: `NIJI`
- Action: `In the corner of the screen, ニジ says nothing, does not hurry, does not cry — only waits`
- Intention: `To wait for 真白, without pushing`
- Intensity: `Low, sustained`
- Speed: `Still. Only her rainbow afterimage drifts`

### Action Relationship

- Before: `ACT_MURMUR`
- After: `— (cut on her silence)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, very shallow. Only the screen or the finger is ever sharp`
- Depth of Field: `Very shallow — the room is a soft indigo blur, graying at the edges`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Locked close on the screen and hand. The reply box still empty, the cursor blinking. The finger motionless over the send button.
- **`[0:06–0:15]`** — A slow drift up and out just enough to take in the curtain, now whitening, as the finger pulls back from the send button.
- **`[0:15–0:25]`** — Cut to her face, lit from below by the screen, the gray dawn at the edge of the frame. Her lips barely move on the refusal. Static.
- **`[0:25–0:30]`** — Back to the screen — ニジ in the corner, silent, waiting. Cut on her.

---

# 11. MOTION

## Subject Motion

- The finger pulls back from the send button — one slow, heavy, reluctant withdrawal; then nothing
- Her lips barely move on the murmured refusal — the only other motion in her body
- ニジ in the screen does not move except for her rainbow afterimage, drifting blue → green → blue

## Object Motion

- The phone does not move on its own. Ever
- Screen content is almost still — the cursor blinks; nothing else changes
- The wall clock's second hand advances in discrete ticks, faint behind

## Environmental Motion

- The dawn does not visibly move anything — only a slow, faint graying at the curtain
- The screen's bloom breathes very slightly on the ceiling

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; her hand is heavy on it`
- Inertia: `High everywhere; the pullback is slow and heavy, not a flinch`
- Acceleration: `Gentle, then nothing`
- Fluidity: `Limited-animation — one slow withdrawal, then holds`
- Impact: `None. The only event is a finger giving up`

---

# 12. EMOTION

## Emotional Arc

- Refusal (the finger that will not move)
- ↓ Surrender (pulling back; the dawn comes regardless)
- ↓ The small confession (……無理だよ — barely voiced)
- ↓ Being waited for (ニジ's silence, which does not push)

## Emotional Events

- Event: `The finger pulls back` — Emotion: `Surrender — 無理` — Intensity: `CRITICAL, expressed as withdrawal` — Timing: `≈0:08`
- Event: `「私、こんなの、――無理だよ」` — Emotion: `The small confession, almost inaudible` — Intensity: `HIGH, suppressed` — Timing: `≈0:20`
- Event: `ニジ waits without pushing` — Emotion: `Being waited for — a tenderness that does not insist` — Intensity: `LOW, sustained` — Timing: `0:25–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `The first gray of dawn at the curtain — a cold, faint lightening, not yet daylight`
- Color Temperature: `≈6500K screen against the first gray-blue of dawn. A subtle, cold shift`

## Lighting Events

- **`[0:00]`** — Screen on, its light the only real light. The room still deep indigo.
- **`[0:06–0:15]`** — The curtain begins to whiten — a faint gray edge grows at the window, the first sign that the night is ending.
- **`[0:15–0:25]`** — Her face lit from below by the screen; the gray dawn just touches the far edge of the frame, colder than the screen.
- **`[0:25–0:30]`** — Unchanged. Cut on ニジ's rainbow in the dark screen.

---

# 14. AUDIO

## Dialogue

- 真白: 「……無理」 — a murmur, barely voiced
- 真白: 「私、こんなの、――無理だよ」 — small, into the empty dark

> ニジ has **no line** in this segment. She says nothing. No narration, no voice-over.

## Sound Effects

- The blinking cursor's faint electronic tick, under everything
- The wall clock's dry discrete ticking
- The first morning sounds, far away — a distant train, the thin sound of a street waking. They are distant, not inside the room

## Environment

- Night thinning into dawn. Room tone and the clock, and far off, the world beginning

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Resigned, suspended. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the refusal. It may thin toward the close, leaving only room tone, the cursor, and the distant morning`

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
- Let the finger pull back from the send button — one slow, heavy withdrawal
- 真白's refusal, small and barely voiced: 「……無理」「私、こんなの、――無理だよ」
- ニジ says nothing and does not cry — she only waits
- End by cutting on ニジ's silence in the corner of the screen, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 36–40 レンジより）

- **No full disappearance.** ニジ must not vanish, dissolve, or fade out — she thins only from S39, never here
- ニジ stays inside the screen; she never stands in the room at human scale
- No line for ニジ in this segment — she is silent
- 小春 appears only as text — never as a person, face, or figure
- No other person, crowd, or silhouette

## PREFER

- The refusal held and small, over any performed emotion
- Silence over score
- Negative space over detail; the room may be nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The pullback may be read as a single slow movement (not a flinch)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ is present, fully opaque, inside the screen only (ledger 36–40 — she thins only from S39); ニジ is silent, and 小春 appears only as text. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at the edge of dawn. ニジ is present, fully opaque, inside the screen. Beats, deliberately uneven: [0:00–0:06] the reply box still empty, the cursor blinking, the finger that hovered over the send button now motionless; [0:06–0:15] THE SURRENDER — the finger pulls back from the send button, one slow heavy withdrawal, and beyond the curtain the sky whitens, morning sounds beginning far away; [0:15–0:25] THE PEAK — 真白 murmurs ……無理 and then 私、こんなの、――無理だよ, small and barely voiced, the words hanging in the air; [0:25–0:30] ニジ, in the corner of the screen, says nothing, does not hurry, does not cry — only waits — and the shot cuts on her silence. The refusal holds the largest share of the duration. Ends on ニジ's silence, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ, inside the screen only, is 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same tilt of the head — a blurred rainbow afterimage resolved into that outline, colors drifting slowly blue → green → blue, no shadow anywhere, fully opaque. The screen shows an open chat thread with an empty reply box and a blinking cursor, in ordinary Japanese UI in cold blue-white; ニジ sits small in its corner. The curtain is whitening with the first gray of dawn. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers and the lips. The finger pulls back from the send button — one slow, heavy, reluctant withdrawal — then holds still. Her lips barely move on the murmured refusal. ニジ does not move except for her rainbow afterimage, drifting slowly blue → green → blue, inside the screen. The curtain lightens with a slow, faint graying; nothing else in the room moves. Ordinary weight and inertia: the phone has heft, her hand is heavy. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the finger is sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked close on the screen and hand, the reply box empty, the cursor blinking, the finger motionless. [0:06–0:15] a slow drift up and out just enough to take in the curtain, now whitening, as the finger pulls back. [0:15–0:25] cut to her face lit from below, the gray dawn at the edge of the frame, her lips barely moving on the refusal, static. [0:25–0:30] back to the screen — ニジ in the corner, silent, waiting; cut on her.

## Audio Prompt

Almost silent, thinning into the first morning. Deep quiet night room tone, a wall clock ticking dry and discrete, and the faint electronic tick of the blinking cursor. Far away, the first morning sounds — a distant train, a street waking — thin and outside the room. Two murmured lines, barely voiced: 真白 says ……無理, then 私、こんなの、――無理だよ. ニジ has no line — she is silent. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only room tone, the cursor, and the distant morning. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no full disappearance, no complete vanishing, no dissolving into nothing, no fading out to invisibility, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep09-seg02-30s-01`
- Segment ID: `S37`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_09, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 9s / 10s / 5s. Refusal = BEAT 3 at 10s (33%)`
- Camera Events: `4 events as listed in §10. One slow drift (0:06–0:15)`
- Action Events: `ACT_FROZEN → ACT_PULLBACK → ACT_MURMUR → ACT_WAIT`
- Audio Events: `two murmured lines ／ ニジ silent ／ clock and cursor throughout ／ distant morning sounds`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on ニジ's silence`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ may speak.** The temptation to give her a reassuring line is strong. She must be silent here. If a line appears, regenerate on the Audio slot.
- **ニジ may vanish or fade.** She must stay fully opaque. If she thins, restore her opacity and verify frame by frame.
- **The dawn may read as a cut to morning.** It is only a faint graying at the curtain — the room stays dark, the screen stays the key light.
- **The refusal may be over-performed.** 「無理だよ」 must stay small and barely voiced. If it reads as a sob, pull it back.

## Changes

- _(none yet)_

## Next Generation

- If the refusal holds and ニジ stays silent, S38 (送信を押す) turns on the first press of the send button.
