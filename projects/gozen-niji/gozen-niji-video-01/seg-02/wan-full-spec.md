# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第1話 S02「午前2時の通知」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「見る」の所作——目を覚まして、時計からスマホへ目を移す（指の背骨の第2本）。ニジは不在（画面の文字としてのみ）。登場人物は真白のみ。画面文字は「午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ」——身に覚えのない一時間二十一分。S03 の「止まり」が効くのは、この1本まで指が動いているから。**

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

> **No other character appears this segment.** ニジ is absent (ledger 01–05 — the ghost exists only as text on the screen). 美月 does not appear until S04.

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
- Appearance: `午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ — the screen-time record, rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
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

At 2:00 A.M. the phone lights silently with a screen-time record of 1 hour 21 minutes she did not spend — during which the phone moved.

## Beginning

She wakes in the dark. まぶたの裏に、まだタイムラインの光が残ってた。She rubs her eyes, letting them adjust to the dark ceiling, trying to go back to sleep.

## Turn

Beside the pillow, the phone lights up. No sound. A notification — screen time. She is awake; the record should not be possible.

## Peak

The record: 午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ. An hour and twenty-one minutes — the time she was asleep. During it, the phone was moving.

## Pull（引き — 切れ目）

誰かの指が、真白のスマホで、何かを、打っていた。Cut on the record on screen and her still face — the first instance of the trunk question.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The record reveal holds 12s (40%).

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the dark bedroom; the record reveal is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「目が覚める」.** Her eyes open in the dark. The ceiling, then the wall clock: 2:00. She rubs her eyes; the afterimage of the timeline still behind her lids. _Density: SPARSE — three small moves, heavy and slow._
- **BEAT 2 `[0:06–0:11]` — 「通知」.** Beside the pillow, the phone lights up. No sound. Its bloom expands into the dark before the phone is framed. _Density: TRANSITION — the turn, quick and quiet._
- **BEAT 3 `[0:11–0:23]` — 「身に覚えのない記録」 — REVEAL, longest share.** The screen-time record fills the frame: 午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ. An hour twenty-one minutes she was asleep for. _Density: DENSE at the head (the numbers), then the record alone, held._
- **BEAT 4 `[0:23–0:30]` — 「誰かの指」 — PULL.** Her face, lit from below, still. The record remains on screen. The dread that has not yet formed a question. Cut on the record and her face. _Density: HELD — then cut precisely on the pull. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the phone lighting silently (≈0:07) ／ the record filling the frame (≈0:12) ／ the hour twenty-one minutes registering (≈0:19)`

## Temporal Density

- Sparse regions: `0:00–0:06 (waking), 0:23–0:30 (the held dread)`
- Dense regions: `0:06–0:23 (notification → record → numbers)`
- Long continuous action: `0:23–0:30 the held stillness`
- Rapid transitions: `0:06–0:11 (the phone lighting)`

---

# 9. ACTION

## Action — ACT_WAKE

- ID: `ACT_WAKE`
- Subject: `MASHIRO`
- Action: `Eyes open in the dark; head turns toward the clock, then the phone`
- Intention: `Involuntary waking`
- Intensity: `Low`
- Speed: `Slow, heavy`

### Action Relationship

- Before: `—` (continues from S01's closing screen)
- After: `ACT_NOTICE`

## Action — ACT_NOTICE

- ID: `ACT_NOTICE`
- Subject: `MASHIRO`
- Action: `Sees the phone light up; her head turns to it`
- Intention: `Startled — she is awake, and the notification disproves itself`
- Intensity: `Low, quiet`
- Speed: `Slow, then still`

### Action Relationship

- Before: `ACT_WAKE`
- After: `ACT_READ`

## Action — ACT_READ

- ID: `ACT_READ`
- Subject: `MASHIRO`
- Action: `Picks up the phone and reads the record, once, then again`
- Intention: `To disprove it`
- Intensity: `Medium, internal`
- Speed: `Quick at first, slowing as it fails to make sense`

### Action Relationship

- Before: `ACT_NOTICE`
- After: `ACT_STILL`
- Causes: `ACT_STILL`

## Action — ACT_STILL

- ID: `ACT_STILL`
- Subject: `MASHIRO`
- Action: `Her face goes still; the phone stays in her hand; nothing moves`
- Intention: `None — the body arriving before the understanding`
- Intensity: `HIGH, entirely internal`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_READ`
- After: `— (cut on the pull)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Very shallow — often only the screen or her face is sharp`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Cut to her face on the pillow as her eyes open. Static, close. Rack focus past her to the wall clock: 2:00.
- **`[0:06–0:09]`** — Slow tilt down to the phone beside the pillow as it lights. The bloom grows into frame before the phone itself does.
- **`[0:09–0:11]`** — Slow push in on the phone as her hand reaches for it.
- **`[0:11–0:18]`** — One slow continuous dolly in on the screen until the record fills the frame. The piece's single sustained move, and it belongs to the reveal.
- **`[0:18–0:23]`** — Absolutely locked on the record. Static. The numbers held.
- **`[0:23–0:30]`** — Pull focus off the screen onto her still face in the dim light. Hold. Cut on the record and her face.

---

# 11. MOTION

## Subject Motion

- Her body moves slowly and heavily — waking, rubbing her eyes, turning her head
- Her fingers carry the small precise movements — reaching for the phone, picking it up
- The stillness at the end is absolute: not a pause, but a stop

## Object Motion

- The phone lights up without being touched — but this must read as ordinary, not supernatural. It is lit, not animated
- Screen content changes by ordinary UI transitions only. Nothing glitches, flickers, distorts, or behaves supernaturally
- The wall clock's second hand advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body (slow to wake), near-zero for her fingers once they move`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None`

---

# 12. EMOTION

## Emotional Arc

- Disorientation (awake at 2:00)
- ↓ Quiet surprise (the phone disagrees with her being awake)
- ↓ Cold recognition (the record of time she did not spend)
- ↓ Unformed dread (the phone moved while she slept)

## Emotional Events

- Event: `The phone lights silently` — Emotion: `Being contradicted by an object` — Intensity: `LOW` — Timing: `≈0:07`
- Event: `The record fills the frame` — Emotion: `Cold recognition` — Intensity: `HIGH` — Timing: `≈0:15`
- Event: `Her face goes still` — Emotion: `Dread that has not yet formed a question` — Intensity: `HIGH, entirely internal` — Timing: `0:23–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo`

## Lighting Events

- **`[0:00–0:06]`** — Dark, near-black. The faintest ambient indigo; her face barely legible.
- **`[0:06–0:09]`** — The phone wakes: bloom expands into the dark before the phone is framed. The single most important lighting event — light arriving without sound.
- **`[0:11–0:23]`** — As the camera closes on the screen, its light dominates the frame; her face falls almost to silhouette. The evidence outshines the person.
- **`[0:23–0:30]`** — Her face returns, dim, lit only from below. The record still glowing.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. No narration, no voice-over.

## Sound Effects

- The wall clock's second hand, dry discrete ticks, present throughout
- Soft futon fabric as she shifts and rubs her eyes
- The soft sound of a hand reaching for and picking up the phone
- **The notification is silent.** No chime, no buzz, no vibration. It arrives as light only — this must be preserved

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness, then **withdraw**. Music thins as the camera closes on the record, and is entirely gone by the moment her face goes still, leaving only room tone and the clock`

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

- Render the on-screen Japanese exactly: `午前2時00分〜午前3時21分` ／ `使用時間　1時間21分` ／ `アプリ　メッセージ`
- Keep the notification silent — light only
- Keep the phone screen the sole night light source
- End on the record on screen and her still face, cut on the pull

## MUST NOT（この1本の禁止・開示台帳 01–05 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person, no eyes, no hand but her own
- **No rainbow, no iridescence, no colored afterimage**
- No second character
- No on-screen subtitles or captions burned in (the record is diegetic, not a subtitle)

## PREFER

- Framing the record large, straight-on and held rather than skimmed
- Silence over score at the peak
- Holds over movement

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in may be omitted
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

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:06] she wakes in the dark, the wall clock reads 2:00, and she rubs her eyes; [0:06–0:11] the phone lights up beside her pillow without any sound, its bloom expanding into the dark; [0:11–0:23] THE REVEAL — the camera closes slowly on a screen-time record reading exactly 午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ, an hour and twenty-one minutes she was asleep for; [0:23–0:30] her face goes still in the dim light, the record still on screen, and the shot cuts on the record and her face. The reveal holds the largest share of the duration. Ends on the pull, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. A plain unremarkable Japanese high-school girl, 16–17, shoulder-length dark hair, a thin neck, small frame, back curved over her phone, in plain pajamas in a futon on the floor. A small bedroom: futon, curtained window, wall clock, few objects. Night is deep indigo lit solely by one cold blue-white phone screen from below her face, her face nearly silhouetted, shadows soft and deep, no fill. The phone screen shows an ordinary Japanese UI in cold blue-white, a screen-time record reading exactly 午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her body moves slowly and heavily — waking, rubbing her eyes, turning her head; her fingers carry the small precise movements, reaching for and picking up the phone. The stillness at the end is absolute — not a pause but a stop. Ordinary weight and inertia: the phone has heft, the futon compresses, her body is slow to wake. Gentle acceleration everywhere. The phone lights up without being touched, but it reads as ordinary — lit, not animated; it never moves by itself and never glitches, flickers or distorts, its screen changing only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or her face is sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] cut to her face as her eyes open, static, then rack focus past her to the wall clock reading 2:00. [0:06–0:09] slow tilt down to the phone as its bloom expands into frame ahead of it. [0:09–0:11] slow push in as her hand reaches for it. [0:11–0:18] one slow continuous dolly in until the record fills the frame. [0:18–0:23] absolutely locked on the record, static. [0:23–0:30] pull focus off the screen onto her still face; hold; cut on the record and her face.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, present throughout. Soft futon fabric as she shifts and rubs her eyes. The soft sound of a hand reaching for and picking up the phone. The notification makes NO sound — no chime, no buzz, no vibration; it arrives as light only. No spoken words at all. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as the camera closes on the record and entirely gone by the moment her face goes still, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep01-seg02-30s-01`
- Segment ID: `S02`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_01, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 5s / 12s / 7s. Reveal = BEAT 3 at 12s (40%)`
- Camera Events: `6 events as listed in §10. One sustained dolly (0:11–0:18)`
- Action Events: `ACT_WAKE → ACT_NOTICE → ACT_READ → ACT_STILL`
- Audio Events: `no dialogue ／ silent notification ／ clock ticking throughout ／ music gone by the stillness`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the pull`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- *(none yet — to be filled after the first generation)*

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The record's three lines carry the evidence. If they render as noise the segment fails. Check first; if unusable, generate the screen as a plate and composite the text in post.
- **The phone lighting may look supernatural.** It must read as an ordinary phone lighting up, not a glow effect. If it reads as a flash, tone the bloom down.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.
- **The model may add a ghost.** The negative prompt front-loads this; verify frame by frame.

## Changes

- *(none yet)*

## Next Generation

- If the text renders cleanly, consider holding the final stillness 1–2 seconds longer, taking the time from beat 1.
