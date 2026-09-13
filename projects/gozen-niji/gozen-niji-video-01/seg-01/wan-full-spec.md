# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第1話 S01「撫でる指」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「撫でる」の確立——一秒も止まらない親指（指の背骨の第1本）。ニジは不在（画面の文字としてのみ）。登場人物は真白のみ。画面文字なし（UIの「いいね 23」と既読のままの3トークのみ）。S03 の「止まり」が効くのは、この1本で「止まらない」を刻むから。**

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
- Appearance: `No message text this segment — only ordinary UI: いいね 23 and three chats read and left unanswered, pinned at the top. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
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

Night. In the futon, her thumb strokes the timeline the way it does every night — unhurried, mechanical, not chosen. The gesture that the rest of the series will make stop.

## Beginning

11 P.M. The futon still holds the day's warmth. The phone is propped by the pillow; its light paints a soft blue rectangle on the dark ceiling. One car passes, far away.

## Turn

いいね二十三. Three chats, read and left unanswered, pinned at the top of the screen. 返すと、続く。続くと、何を言えばいいか分からなくなる。だから返さない——既読を付けて、画面を閉じる。それが一番、関係を壊さない。

## Peak

The thumb keeps stroking, the same arc, the same rhythm. She has to talk herself out of it: 言い聞かせないと、指が返事を打ち始めるから。The finger is faster than her.

## Pull（引き — 切れ目）

She closes the screen. The blue rectangle leaves the ceiling; the room goes dark. Cut on the darkened room and the wall clock, still short of 2:00 — the quiet before the wake.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The stroke holds 12s (40%) to engrave the gesture.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the bedroom; the stroke is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:12]` — 「撫でる」 — ESTABLISH, longest share.** Dark bedroom, 11 P.M. The phone propped by the pillow, the only light. Her thumb strokes the screen, over and over, unhurried and mechanical. The screen paints a soft blue rectangle on the dark ceiling. Far beyond the curtain, one car's headlights cross and are gone. _Density: SPARSE — long continuous action, almost no event._
- **BEAT 2 `[0:12–0:18]` — 「いいね二十三」.** On screen, small: いいね 23. Three chats sit read and unanswered, pinned at the top. Her thumb strokes on beneath them. _Density: TRANSITION — quiet UI detail, no break in the motion._
- **BEAT 3 `[0:18–0:26]` — 「言い聞かせる」.** Her face, lit from below. The thumb still moving, the same arc. She is talking herself out of replying. The finger wants to begin. _Density: SPARSE, internal — the only "event" is a restraint._
- **BEAT 4 `[0:26–0:30]` — 「閉じる」.** She closes the screen. The blue rectangle leaves the ceiling. The room goes dark. The wall clock, still short of 2:00. Cut to black on the dark room. _Density: HELD — then a clean cut. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the stroke in motion (0:00–0:12) ／ the three unanswered chats (≈0:14) ／ the screen closing (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:12 (the repeated stroke), 0:18–0:26 (the restraint)`
- Dense regions: `0:12–0:18 (the three chats)`
- Long continuous action: `0:00–0:12 the thumb stroking`
- Rapid transitions: `none — the slowest, most held segment of the episode`

---

# 9. ACTION

## Action — ACT_STROKE

- ID: `ACT_STROKE`
- Subject: `MASHIRO`
- Action: `Thumb strokes the screen, repeatedly, without variation`
- Intention: `Not enjoyment — habit. She is not choosing to do this`
- Intensity: `Low`
- Speed: `Steady, practiced, slightly too fast`

### Action Relationship

- Before: `—`
- After: `ACT_GLANCE`

## Action — ACT_GLANCE

- ID: `ACT_GLANCE`
- Subject: `MASHIRO`
- Action: `Eyes move over the three read-but-unanswered chats, then away`
- Intention: `To keep them from becoming a reply`
- Intensity: `Low`
- Speed: `Quick, then back to the stroke`

### Action Relationship

- Before: `ACT_STROKE`
- After: `ACT_RESTRAIN`

## Action — ACT_RESTRAIN

- ID: `ACT_RESTRAIN`
- Subject: `MASHIRO`
- Action: `The thumb hesitates over the reply box, then does not type`
- Intention: `言い聞かせる — to talk the finger out of it`
- Intensity: `Medium, internal`
- Speed: `A near-stop, caught and released back into the stroke`

### Action Relationship

- Before: `ACT_GLANCE`
- After: `ACT_CLOSE`

## Action — ACT_CLOSE

- ID: `ACT_CLOSE`
- Subject: `MASHIRO`
- Action: `Closes the screen and sets the phone down, turning over to sleep`
- Intention: `To end the ritual`
- Intensity: `Low`
- Speed: `Slow, ordinary`

### Action Relationship

- Before: `ACT_RESTRAIN`
- After: `— (cut to black)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Very shallow — often only the screen or the fingers are sharp`
- Camera Style: `Slow, deliberate, almost still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:12]`** — Locked close on the hand and the propped phone, the ceiling's blue rectangle soft in the background. No movement at all except the thumb. Optional: an imperceptibly slow push-in.
- **`[0:12–0:18]`** — A slight, slow tilt down to bring the three chats into frame at the top of the screen. Still close, still nearly still.
- **`[0:18–0:26]`** — Cut to her face, lit from below by the screen, the thumb in the foreground still moving. Static, close.
- **`[0:26–0:30]`** — The thumb reaches the side button; the screen goes off. The blue rectangle leaves the ceiling. Hold on the darkened room, the wall clock faintly legible. Cut to black.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially all the movement; the rest of her body holds.
- The stroke is repetitive and mechanical — the same arc, the same rhythm, no variation.
- The restraint is a near-stop, caught and released back into the stroke.
- Closing the screen is the only deliberate whole-hand motion, and it is slow and ordinary.

## Object Motion

- The phone does not move on its own. Ever.
- Screen content changes by ordinary UI transitions only — a timeline scrolling, a screen going dark. Nothing glitches, flickers, distorts, or behaves supernaturally.
- The wall clock's second hand advances in discrete ticks.

## Environmental Motion

- One car's headlights sweep across the curtain, early, and do not return.
- The screen's bloom breathes very slightly on the ceiling — the only continuous motion.

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers (instant, practiced)`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Numb habit (the stroke that isn't chosen)
- ↓ Quiet avoidance (the three chats she will not answer)
- ↓ Restraint (the finger that wants to begin a reply)
- ↓ Release (closing the screen; the ritual ends)

## Emotional Events

- Event: `The three read-but-unanswered chats` — Emotion: `Avoidance, not guilt` — Intensity: `LOW` — Timing: `≈0:14`
- Event: `The thumb hesitates over the reply box` — Emotion: `Restraint — 言い聞かせる` — Intensity: `MEDIUM, entirely internal` — Timing: `≈0:20`
- Event: `The screen closes` — Emotion: `Release into the dark` — Intensity: `LOW` — Timing: `≈0:27`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo, warm from the futon's remembered day-heat at the edge`
- Color Temperature: `≈6500K screen against deep indigo, with a faint warmth where the futon still holds the day`

## Lighting Events

- **`[0:00]`** — Screen already on. Its light lies on the ceiling as a soft blue rectangle.
- **`[0:12–0:18]`** — The light shifts slightly as she scrolls — the rectangle bends, barely.
- **`[0:18–0:26]`** — Her face is lit from below, almost to silhouette, the knuckles bright.
- **`[0:26–0:30]`** — The screen goes off. The blue rectangle leaves the ceiling. The room falls to near-black — only the faintest ambient indigo. Cut.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The three chats are read, not spoken. No narration, no voice-over.

## Sound Effects

- The soft friction of a thumb on glass, close and continuous, through the whole segment — its rhythm the segment's pulse.
- A single distant car passing, early.
- Soft futon fabric as she turns over at the end.
- The wall clock's second hand, dry discrete ticks, faint under the stroke.

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the stroke. It may thin toward the close, leaving only room tone, fabric, and the clock`

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

- Establish the stroke — the same arc, the same rhythm, unhurried and mechanical.
- Render the on-screen Japanese exactly: `いいね 23` (the number may be shown as 23 likes; the three chats are UI, no text need render).
- Keep the phone screen the sole night light source.
- End on the screen going dark and the room falling to near-black, cut on the dark.

## MUST NOT（この1本の禁止・開示台帳 01–05 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person, no eyes, no hand but her own.
- **No rainbow, no iridescence, no colored afterimage.**
- No second character — 美月 does not appear until S04.
- No on-screen subtitles or captions burned in (the phone UI is diegetic, not a subtitle).

## PREFER

- The stroke uninterrupted for as long as possible — the whole segment is one held gesture.
- Silence over score.
- Negative space over detail; the room may be nearly empty.

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing.
- The imperceptible push-in during beat 1 may be omitted (a fully locked frame is equally correct).
- Music may be absent altogether.

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

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 11 P.M. Beats, deliberately uneven: [0:00–0:12] her thumb strokes her phone screen in the futon, over and over, the screen the only light, painting a soft blue rectangle on the dark ceiling; [0:12–0:18] on screen, いいね 23 and three chats read and left unanswered, pinned at the top; [0:18–0:26] her face lit from below, the thumb still moving, she is talking herself out of replying — the finger wants to begin; [0:26–0:30] she closes the screen, the blue rectangle leaves the ceiling, the room goes dark, and the shot cuts on the dark room. The stroke holds the largest share of the duration. Ends on the dark.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. A plain unremarkable Japanese high-school girl, 16–17, shoulder-length dark hair, a thin neck, small frame, back curved over her phone, in plain pajamas in a futon on the floor. A small bedroom: futon, curtained window, wall clock, few objects. Night is deep indigo lit solely by one cold blue-white phone screen from below her face, her face nearly silhouetted, shadows soft and deep, no fill, with a faint warmth at the edge where the futon still holds the day. The phone screen shows an ordinary Japanese UI in cold blue-white. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers; the body holds still. The thumb strokes the screen in a repetitive mechanical arc, the same rhythm without variation. One near-stop as the thumb hesitates over the reply box, then back into the stroke. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. One car's headlights sweep across the curtain early and do not return. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the fingers are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:12] locked close on the hand and propped phone, optionally an imperceptibly slow push-in. [0:12–0:18] a slight slow tilt down to bring the three chats into frame. [0:18–0:26] cut to her face lit from below, static, the thumb moving in the foreground. [0:26–0:30] the thumb reaches the side button, the screen goes off, the blue rectangle leaves the ceiling; hold on the darkened room, cut to black.

## Audio Prompt

Almost silent. Deep quiet night room tone. The close continuous friction of a thumb on glass, its rhythm the segment's pulse. A single distant car passing early. Soft futon fabric as she turns over at the end. The wall clock's dry discrete ticking, faint under the stroke. No spoken words at all — the three chats are read, not spoken. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only room tone, fabric, and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep01-seg01-30s-01`
- Segment ID: `S01`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_01, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 12s / 6s / 8s / 4s. Stroke = BEAT 1 at 12s (40%)`
- Camera Events: `4 events as listed in §10. No sustained dolly; all static, drift, or tilt`
- Action Events: `ACT_STROKE → ACT_GLANCE → ACT_RESTRAIN → ACT_CLOSE`
- Audio Events: `no dialogue ／ thumb-on-glass throughout ／ clock faint under the stroke`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the dark`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The stroke may look floaty.** A generated thumb may stroke with no weight or variation. The mechanical repetition is the point — if it looks random, hold the framing tighter on the hand.
- **Identity drift.** Her face may shift across the take. §15 is the defense.
- **The model may add a ghost.** The negative prompt front-loads this; verify frame by frame.
- **The いいね count and the three chats may render as noise.** They are secondary to the stroke; if unusable, prefer them out of focus — the stroke must read first.

## Changes

- _(none yet)_

## Next Generation

- If the stroke reads well, consider a vertical 9:16 variant — the viewer is in the same posture as the protagonist.
