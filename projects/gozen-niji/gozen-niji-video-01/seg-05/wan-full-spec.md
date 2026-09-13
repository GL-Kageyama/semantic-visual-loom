# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第1話 S05「待つ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「握る」の所作——画面の縁を握る（指の背骨の第5本・第1話の締め）。ニジは不在（画面の文字としてのみ）。登場人物は真白のみ。画面文字は「おまえ、いま、起きてるんだろ。」——その後に何も足さない、第1話のフックの鎖の起点。**

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

> **No other character appears this segment.** ニジ is absent (ledger 01–05 — the ghost exists only as text on the screen). 美月, who appeared in S04, does not return this segment.

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
- Appearance: `おまえ、いま、起きてるんだろ。 — the received message, rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
- Continuity Importance: `HIGH`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks — unnaturally loud. Reaches 2:00 at the hinge of the night`
- Narrative Importance: `HIGH`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_01_午前二時、あなたのスマホは他人のもの.md`
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

She does not sleep. She lies with the screen open, waiting for 2:00 A.M. — and at 2:00 A.M. the phone lights: 「おまえ、いま、起きてるんだろ。」 Her breath stops.

## Beginning

Night. 真白 is not asleep. In the futon, she holds the phone open, wanting to see whether it will light.

## Turn

Why wait. 待つということは、また何かが来るかもしれないと思っている、ということだ。The wall clock's second hand is unnaturally loud. The futon's heat clings to her skin.

## Peak

Her finger grips the edge of the screen, hard. The clock reaches 2:00. The phone lights.

## Pull（引き — 切れ目）

＞ おまえ、いま、起きてるんだろ。 真白は、画面の前で、息を、止めた。Cut to black on the line. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The wait holds 12s (40%) — the dread that has agreed to itself.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the dark bedroom; the wait is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「眠れない」.** Night. She is awake, holding the open screen, not stroking it. The screen's glow on her face. She is waiting. _Density: SPARSE — one held position, almost no event._
- **BEAT 2 `[0:07–0:19]` — 「待つ」 — longest share.** The wall clock's second hand, unnaturally loud. The futon's heat clings to her skin. Her finger grips the edge of the screen, harder. The clock, the clock, the clock. _Density: SPARSE, held — the whole beat is one continuous wait._
- **BEAT 3 `[0:19–0:24]` — 「午前2時」.** The second hand reaches 2:00. Beside her, the phone lights. No sound. Its bloom expands into the dark. _Density: TRANSITION — the turn, quick and silent._
- **BEAT 4 `[0:24–0:30]` — 「起きてるんだろ」 — HOOK.** On the screen, the line appears: おまえ、いま、起きてるんだろ。 Her breath stops. Cut to black on the line. _Density: HELD — then cut precisely on the hook. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the finger gripping the edge (0:07–0:19) ／ the phone lighting at 2:00 (≈0:20) ／ the line appearing (≈0:25) ／ the cut (0:30)`

## Temporal Density

- Sparse regions: `0:00–0:19 (the wait — the whole first two-thirds)`
- Dense regions: `0:19–0:30 (2:00 → the line → the cut)`
- Long continuous action: `0:07–0:19 the held wait, the gripping finger`
- Rapid transitions: `0:19–0:24 (the phone lighting)`

---

# 9. ACTION

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `MASHIRO`
- Action: `Lies holding the open screen, thumb resting on the glass, not stroking`
- Intention: `Waiting for 2:00 A.M. — which means she believes something will come`
- Intensity: `Medium, suppressed`
- Speed: `Motionless`

### Action Relationship

- Before: `—` (continues from S04's walk home, into the night)
- After: `ACT_GRIP`

## Action — ACT_GRIP

- ID: `ACT_GRIP`
- Subject: `MASHIRO`
- Action: `Her finger grips the edge of the screen, the grip tightening, slowly`
- Intention: `Holding on — to the phone, to the wait`
- Intensity: `Medium, internal`
- Speed: `Very slow, continuous`

### Action Relationship

- Before: `ACT_HOLD`
- After: `ACT_LIGHT`

## Action — ACT_LIGHT

- ID: `ACT_LIGHT`
- Subject: `MASHIRO`
- Action: `The phone lights at 2:00; she does not move, only her eyes go to it`
- Intention: `None — this is what she was waiting for`
- Intensity: `HIGH, entirely internal`
- Speed: `The light arrives; she stays still`

### Action Relationship

- Before: `ACT_GRIP`
- After: `ACT_BREATH_STOP`

## Action — ACT_BREATH_STOP

- ID: `ACT_BREATH_STOP`
- Subject: `MASHIRO`
- Action: `Her breath stops as the new line appears`
- Intention: `None — involuntary`
- Intensity: `CRITICAL, entirely internal`
- Speed: `Instant, then held to the cut`

### Action Relationship

- Before: `ACT_LIGHT`
- After: `— (cut to black)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Very shallow — often only the screen, the fingers, or her face is sharp`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Static, wide-ish and low: her form in the futon, the screen's glow on her face. Nothing moves.
- **`[0:07–0:19]`** — A slow, imperceptible push toward the hand gripping the edge of the screen. The grip tightens almost imperceptibly. No other movement. Optionally cut to the wall clock, its second hand sweeping.
- **`[0:19–0:24]`** — Cut to the phone as its bloom expands into frame, ahead of the phone itself. No cut inside this — a single silent approach.
- **`[0:24–0:30]`** — Slow push to the screen as the line appears. Locked on the line. Cut to black on it.

---

# 11. MOTION

## Subject Motion

- Her body holds absolutely still — only the grip on the edge of the screen tightens, slowly
- Her breathing is the only other motion, shallow and quiet, until it stops
- At the light, she does not move; only her eyes go to the screen

## Object Motion

- The phone does not move on its own. Ever. It lights, but does not animate
- Screen content changes by ordinary UI transitions only — a message arriving. Nothing glitches, flickers, distorts, or behaves supernaturally
- The wall clock's second hand advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her grip; the futon compresses under her`
- Inertia: `Very high — she is nearly frozen in the wait`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation — holds punctuated by tiny movements`
- Impact: `None. The only impact is a breath stopping`

---

# 12. EMOTION

## Emotional Arc

- Sleepless intent (wanting to see whether it will light)
- ↓ Consent (waiting — worse than fear, because it is agreement)
- ↓ Anticipation (the clock reaches 2:00)
- ↓ Being addressed (the line — and her breath stops)

## Emotional Events

- Event: `The grip tightens on the edge of the screen` — Emotion: `Holding on` — Intensity: `MEDIUM, internal` — Timing: `0:07–0:19`
- Event: `The phone lights at 2:00` — Emotion: `Anticipation confirmed` — Intensity: `HIGH, entirely internal` — Timing: `≈0:20`
- Event: `おまえ、いま、起きてるんだろ。` — Emotion: `Being addressed` — Intensity: `CRITICAL` — Timing: `≈0:25`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo`

## Lighting Events

- **`[0:00–0:19]`** — Screen already on, its glow lying on her face and the ceiling. The room is otherwise near-black.
- **`[0:19–0:24]`** — The screen brightens fractionally as the new message lands — but this is the phone waking from dim, not a flash, not a pulse.
- **`[0:24–0:30]`** — The screen's light dominates the frame; her face falls almost to silhouette. Then black.

---

# 14. AUDIO

## Dialogue

> **No speech.** The line 「おまえ、いま、起きてるんだろ。」 is not voiced — it is text on the screen. No narration, no voice-over.

## Sound Effects

- The wall clock's second hand — discrete, dry ticks, present throughout, and **unnaturally loud** in this segment
- Soft futon fabric as she lies, barely shifting
- The shallow sound of her breathing — present, quiet — and then it stops
- **The phone's light is silent.** No chime, no buzz, no vibration. It arrives as light only

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness, then **withdraw**. Music thins through the wait and is entirely gone by the moment the line appears, leaving only room tone, the clock, and her stopped breath`

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

- Render the on-screen Japanese exactly: `おまえ、いま、起きてるんだろ。`
- Keep the phone's light silent — light only
- Keep the phone screen the sole night light source
- End on the line and cut immediately. Nothing may follow it

## MUST NOT（この1本の禁止・開示台帳 01–05 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person, no eyes, no hand but her own
- **No rainbow, no iridescence, no colored afterimage**
- No second character
- No on-screen subtitles or captions burned in (the line is diegetic, not a subtitle)
- No voice for the line — it is not read aloud, whispered, or narrated

## PREFER

- The wait held as long as possible; the whole first two-thirds is one continuous stillness
- Silence over score at the line
- Holds over movement

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not be shown (ledger 01–05 — the ghost exists only as text on the screen); no second character. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at night. Beats, deliberately uneven: [0:00–0:07] she lies awake holding the open screen without stroking it, the screen's glow on her face, waiting; [0:07–0:19] the wall clock's second hand ticks unnaturally loud, her finger grips the edge of the screen, harder, the futon's heat clinging to her skin — a long continuous wait; [0:19–0:24] the second hand reaches 2:00 and the phone lights beside her without any sound, its bloom expanding into the dark; [0:24–0:30] on the screen a line appears — おまえ、いま、起きてるんだろ。 — and her breath stops, and the shot cuts to black on the line. The wait holds the largest share of the duration. Ends on the line and cuts immediately, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. A plain unremarkable Japanese high-school girl, 16–17, shoulder-length dark hair, a thin neck, small frame, back curved over her phone, in plain pajamas in a futon on the floor. A small bedroom: futon, curtained window, wall clock, few objects. Night is deep indigo lit solely by one cold blue-white phone screen from below her face, her face nearly silhouetted, shadows soft and deep, no fill. The phone screen shows an ordinary Japanese UI in cold blue-white, and at the end one received message reading exactly おまえ、いま、起きてるんだろ。 No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her body holds absolutely still — only the grip on the edge of the screen tightens, slowly. Her breathing is the only other motion, shallow and quiet, until it stops. At the light she does not move; only her eyes go to the screen. Ordinary weight and inertia: the phone has heft in her grip, the futon compresses, she is nearly frozen in the wait. Gentle acceleration everywhere. The phone lights but does not move by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen, the fingers, or her face is sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] static, wide-ish and low, her form in the futon, the screen's glow on her face. [0:07–0:19] a slow imperceptible push toward the hand gripping the edge of the screen, the grip tightening; optionally cut to the wall clock, its second hand sweeping. [0:19–0:24] cut to the phone as its bloom expands into frame. [0:24–0:30] slow push to the screen as the line appears, locked on the line; cut to black on it.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's second hand, dry discrete ticks, present throughout and unnaturally loud. Soft futon fabric as she lies, barely shifting. The shallow sound of her breathing, quiet — and then it stops. The phone's light is silent — no chime, no buzz, no vibration. No spoken words at all — the line is not voiced, not whispered, not narrated. No voice-over. Music extremely sparse — a few sustained tones at most — thinning through the wait and entirely gone by the moment the line appears, leaving only room tone, the clock, and her stopped breath. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep01-seg05-30s-01`
- Segment ID: `S05`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_01, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 12s / 5s / 6s. Wait = BEAT 2 at 12s (40%)`
- Camera Events: `4 events as listed in §10. No sustained dolly; all static or slow push`
- Action Events: `ACT_HOLD → ACT_GRIP → ACT_LIGHT → ACT_BREATH_STOP`
- Audio Events: `no dialogue ／ silent light ／ clock unnaturally loud ／ breath stops ／ music gone by the line`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut to black on the line`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- *(none yet — to be filled after the first generation)*

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The final line is the hook of the whole episode. If it renders as noise the segment fails. Check first; if unusable, composite the text in post.
- **The wait may read as empty rather than held.** If the first two-thirds feels dead rather than tense, tighten the grip's visibility and let the clock get louder sooner.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.
- **The model may add a ghost.** "2 A.M." + a message is a strong horror prior. The negative prompt front-loads this; verify frame by frame.

## Changes

- *(none yet)*

## Next Generation

- This is the episode's hook. If the line lands cleanly, the cut to black is the whole point — hold it exactly, and consider a vertical 9:16 variant.
