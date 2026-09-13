# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第5話 S18「小春のお辞儀」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**指が初めて休む1本——主役は小春の「お辞儀」（胸に抱えた教科書と、ほんの少し浅い角度）。ニジは不在（学校・小春）。登場人物は真白と小春のみ。画面文字なし（スマホも出さない）。既読無視した後悔は一言も語らず、浅いお辞儀と待っていた笑顔に押し込む。**

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

> **小春 appears this segment**（first-year 柴崎小春 — holds a textbook to her chest; her bow is slightly too shallow）. ニジ is absent（ledger 18 — school）.

---

# 4. ENVIRONMENT

## Location

- ID: `CORRIDOR`
- Name: `学校の廊下 (a school corridor)`
- Description: `Ordinary Japanese high-school corridor in the morning, window light drawing white rectangles across the floor. Pale, slightly overexposed, equally muted — daytime as the shore on either side of 2:00 A.M.`

## Environmental Behavior

- Wind: `none — nothing stirs`
- Particles: `none; no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; the morning light is still and the white rectangles on the floor do not shift`

---

# 5. OBJECTS

## TEXTBOOK

- Type: `textbook`
- Appearance: `小春's textbook, held pressed to her chest the whole segment — it moves only with her bow. The one object this school scene turns on`
- Narrative Importance: `MEDIUM`
- Visual Importance: `HIGH`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_05_届いた、届いていない、の狭間で.md`
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

Morning corridor. 小春 — the first-year whose consultation 真白 has left on read for a month — stops in front of her, a textbook held to her chest, and bows. The bow is slightly too shallow.

## Beginning

Window light draws white rectangles across the corridor floor. 小春 approaches with a textbook pressed to her chest, stops in front of 真白. 真白's fingers are still — the gesture that matters belongs to someone else.

## Turn

「あ、おはようございます」 — and the bow. Slightly too shallow, a first-year's not-yet-practiced bow. 真白 left her on read for a month; the bow holds no reproach. It is warm and unburdened.

## Peak

真白 returns it: 「……おはよう」 — her own voice small. 小春's smile is the face that was waiting for 真白's reply.

## Pull（引き — 切れ目）

Cut on 小春's smiling face, held. どうして、あの子、笑ってるの。既読無視したのに。 The question is left hanging, unanswered.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The bow holds 9s (30%); the small reply is held 8s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「朝の廊下」 — ESTABLISH.** Morning corridor. Window light draws white rectangles on the floor. 小春 approaches with a textbook pressed to her chest, and stops. 真白's fingers are still — for once, the hands are not the subject. _Density: SPARSE — quiet daylight, no event._
- **BEAT 2 `[0:07–0:16]` — 「お辞儀」 — longest share.** 「あ、おはようございます」 — and the bow, slightly too shallow. A first-year's not-yet-practiced bow, the textbook held to her chest. The angle is off by a little — that off-ness is the whole thing. _Density: DENSE at the head, then held on the bow._
- **BEAT 3 `[0:16–0:24]` — 「返す」.** 真白 returns it: 「……おはよう」 — her own voice small. 小春's face lifts into a smile — the face that was waiting for this. _Density: TRANSITION — one small reply, one waiting face._
- **BEAT 4 `[0:24–0:30]` — 「笑顔」 — held, then cut.** 小春's smile, held. 真白 looks at it, and does not understand it. どうして、あの子、笑ってるの。既読無視したのに。 Cut on the smile. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the bow, slightly too shallow (≈0:10) ／ the small reply 「……おはよう」 (≈0:19) ／ 小春's waiting smile (≈0:25)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the corridor), 0:24–0:30 (the held smile)`
- Dense regions: `0:07–0:16 (the bow)`
- Long continuous action: `0:07–0:16 the bow, held a beat too long`
- Rapid transitions: `none — a slow, held morning`

---

# 9. ACTION

## Action — ACT_APPROACH

- ID: `ACT_APPROACH`
- Subject: `KOHARU`
- Action: `Walks up with a textbook pressed to her chest, stops in front of 真白`
- Intention: `To greet her — openly, without reproach`
- Intensity: `Low`
- Speed: `Ordinary, a little shy`

### Action Relationship

- Before: `—`
- After: `ACT_BOW`

## Action — ACT_BOW

- ID: `ACT_BOW`
- Subject: `KOHARU`
- Action: `Bows — 「あ、おはようございます」 — the angle slightly too shallow`
- Intention: `A first-year's practiced-but-not-yet bow. No message behind it but greeting`
- Intensity: `MEDIUM — the off-ness is the subject`
- Speed: `Slow, then held a beat too long`

### Action Relationship

- Before: `ACT_APPROACH`
- After: `ACT_RETURN`

## Action — ACT_RETURN

- ID: `ACT_RETURN`
- Subject: `MASHIRO`
- Action: `Returns the greeting — 「……おはよう」 — her own voice small`
- Intention: `To match the room, as always. The reply comes out smaller than she meant`
- Intensity: `Low, internal`
- Speed: `Slow, quiet`

### Action Relationship

- Before: `ACT_BOW`
- After: `ACT_LOOK`

## Action — ACT_LOOK

- ID: `ACT_LOOK`
- Subject: `MASHIRO`
- Action: `Looks at 小春's smiling face, and does not understand it`
- Intention: `To read why — どうして笑ってるの。既読無視したのに`
- Intensity: `Medium, suppressed`
- Speed: `Still; only the eyes move, searching`

### Action Relationship

- Before: `ACT_RETURN`
- After: `— (cut on the smile)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, standing height. Two-shot, then closer`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Shallow — 小春 sharp, the corridor soft behind`
- Camera Style: `Slow, deliberate, almost still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Static wide two-shot at standing height: 小春 approaching along the corridor, the window light drawing white rectangles on the floor.
- **`[0:07–0:12]`** — Cut to 小春, static, medium. She bows — 「あ、おはようございます」. Hold a beat too long, the slightly-too-shallow angle legible.
- **`[0:12–0:16]`** — Slow push-in, imperceptible, on the bow's angle — the small off-ness that is the whole event.
- **`[0:16–0:20]`** — Cut to 真白, static, close. 「……おはよう」 — the small voice.
- **`[0:20–0:26]`** — Cut to 小春's face lifting into a smile, static, close.
- **`[0:26–0:30]`** — Hold on the smile. Cut on the smile. Nothing after it.

---

# 11. MOTION

## Subject Motion

- 小春 carries the textbook to her chest the whole time; it does not slip or drop
- The bow is the segment's only full gesture — slow, slightly too shallow, held a beat too long
- 真白's body holds nearly still; only her lips move, small, for the reply
- In the last beats only her eyes move, searching 小春's face

## Object Motion

- The textbook stays pressed to 小春's chest; it moves only with her bow
- Nothing else moves in the corridor

## Environmental Motion

- Morning light is still; the white rectangles on the floor do not shift
- No wind, no moving shadows, no particles

## Physical Characteristics

- Weight: `Ordinary. The textbook has heft; 小春 leans into the bow`
- Inertia: `High for both bodies`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet morning (the corridor, unbothered)
- ↓ Unburdened greeting (the too-shallow bow, no reproach in it)
- ↓ Concealment (the small reply — smaller than she meant)
- ↓ Unanswered question (どうして笑ってるの。既読無視したのに)

## Emotional Events

- Event: `The bow, slightly too shallow` — Emotion: `小春's unburdened warmth — no reproach for a month of silence` — Intensity: `MEDIUM` — Timing: `≈0:10`
- Event: `真白 returns 「……おはよう」 small` — Emotion: `Concealment — the voice smaller than intended` — Intensity: `LOW, internal` — Timing: `≈0:19`
- Event: `小春's waiting smile` — Emotion: `The unanswered question — どうして笑ってるの。既読無視したのに` — Intensity: `MEDIUM, suppressed` — Timing: `0:24–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Pale flat daylight from the corridor windows — soft, slightly overexposed`
- Fill Light: `Even, flat. The corridor is bright and unbothered`
- Rim Light: `A faint cool edge along both girls' hair from the window`
- Ambient Light: `Day. Muted, low-saturation, nothing dramatic`
- Color Temperature: `≈5600K pale daylight, slightly overexposed, muted like the whole series`

## Lighting Events

- **`[0:00]`** — Morning light already full; white rectangles lie on the floor.
- **`[0:07–0:16]`** — The light on 小春's face is flat and even; the bow is the only change.
- **`[0:16–0:24]`** — Light unchanged on 真白's face — her small reply is the only change.
- **`[0:24–0:30]`** — Light unchanged. Cut on the smile.

---

# 14. AUDIO

## Dialogue

- 小春: 「あ、おはようございます」 — bright, a little shy
- 真白: 「……おはよう」 — small, quiet

> No other speech. 真白's inner line どうして笑ってるの。既読無視したのに is **not voiced** — no narration, no voice-over.

## Sound Effects

- Morning corridor: soft footsteps, distant students, the faint rustle of a uniform
- The textbook against 小春's chest, a soft papery press
- The room is full and ordinary — the world is loud and unbothered

## Environment

- Day. Full and ordinary corridor ambience — unbothered, unmenacing

## Music

- Style: `Sparse — a few sustained tones, or nothing`
- Tempo: `Slow`
- Mood: `Ordinary, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the morning's ordinary surface under the concealment. It thins toward the smile, leaving only room tone`

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

- 小春 holds the textbook to her chest the whole segment
- The bow is **slightly too shallow** — a first-year's not-yet-practiced bow. The off-angle must read
- 真白's reply is small-voiced
- End on 小春's smile — the face that was waiting for 真白's reply

## MUST NOT（この1本の禁止・開示台帳 18 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person, no eyes, no hand but the two girls' own. ニジ does not appear in this segment — she is absent
- **No rainbow, no iridescence, no colored afterimage.** Her color is introduced later
- **No screen text in this segment, and no phone.** This is a school scene; nothing is read, nothing is sent
- Do not make 小春 sinister, doubtful, or knowing — she is bright and unguarded
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The too-shallow bow over any exaggerated gesture — the off-angle is the whole point
- Silence over score as the smile is held
- Negative space over detail; the corridor may be nearly empty

## ALLOW

- Slight variation in corridor background students and window arrangement
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not be shown (ledger 18 — school; the ghost is absent); no second character beyond 小春, who is bright and unguarded. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school corridor in the morning. Beats, deliberately uneven: [0:00–0:07] window light draws white rectangles across the corridor floor, 小春 approaches with a textbook pressed to her chest and stops in front of 真白; [0:07–0:16] 小春 bows — あ、おはようございます — the angle slightly too shallow, a first-year's not-yet-practiced bow, held a beat too long; [0:16–0:24] 真白 returns it — ……おはよう — her own voice small, and 小春's face lifts into a smile that was waiting for this; [0:24–0:30] 小春's smile is held, and 真白 looks at it without understanding it — どうして笑ってるの、既読無視したのに — and the shot cuts on the smile. The bow holds the largest share of the duration. Ends on the smile, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. By day she wears a standard Japanese school uniform. Scene: a Japanese high-school corridor in the morning, pale flat daylight from the windows laying white rectangles on the floor, slightly overexposed and equally muted. Facing her, 小春 (Koharu) — a first-year girl, smaller and rounder, shoulder-length hair, in the same uniform, bright and unguarded, holding a textbook to her chest, her bow slightly too shallow. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. 小春 carries the textbook to her chest the whole time; it does not slip or drop. The bow is the segment's only full gesture — slow, slightly too shallow, held a beat too long. 真白's body holds nearly still; only her lips move, small, for the reply. In the last beats only her eyes move, searching 小春's face. The textbook moves only with the bow. Nothing else moves. Gentle acceleration everywhere. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, standing height. Longish lens, shallow depth of field; 小春 sharp, the corridor soft behind. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] static wide two-shot at standing height, 小春 approaching along the corridor, window light drawing white rectangles on the floor. [0:07–0:12] cut to 小春, static, medium; she bows, held a beat too long, the slightly-too-shallow angle legible. [0:12–0:16] slow, imperceptible push-in on the bow's angle. [0:16–0:20] cut to 真白, static, close; ……おはよう, the small voice. [0:20–0:26] cut to 小春's face lifting into a smile, static, close. [0:26–0:30] hold on the smile; cut on the smile.

## Audio Prompt

Day. Full and ordinary corridor ambience — soft footsteps, distant students, the faint rustle of a uniform. Two lines of dialogue only: 小春 says あ、おはようございます, bright and a little shy; 真白 answers ……おはよう, small and quiet. The soft papery press of a textbook against 小春's chest. No narration, no voice-over — 真白's inner question is not voiced. Music extremely sparse — a few sustained tones at most — thinning toward the smile, leaving only room tone. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep05-seg01-30s-01`
- Segment ID: `S18`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_05, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 9s / 8s / 6s. Bow = BEAT 2 at 9s (30%)`
- Camera Events: `6 events as listed in §10. One imperceptible push-in (0:12–0:16)`
- Action Events: `ACT_APPROACH → ACT_BOW → ACT_RETURN → ACT_LOOK`
- Audio Events: `two lines of dialogue ／ inner question unvoiced ／ sparse music thinning`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the smile`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- *(none yet — to be filled after the first generation)*

## Anticipated risks (to check in the first generation)

- **The too-shallow bow may not read.** The off-angle is the whole event. If the bow looks perfectly practiced, the segment loses its subject — hold the bow a beat longer and angle it off a little more.
- **小春 reads as sinister.** If her smile or bow is ambiguous, the episode inverts into horror and loses its subject. She must be bright and unguarded.
- **The model may add a ghost.** "A month on read" is a guilt prior. The negative prompt front-loads the no-ghost clause; verify frame by frame — no figure, no eyes, no rainbow.
- **The model may add a phone.** This is a school scene — no phone, no screen text. If one appears, regenerate on the Visual slot.

## Changes

- *(none yet)*

## Next Generation

- If the too-shallow bow and the waiting smile both read, this segment closes cleanly; S19 begins the night the reply is revealed.
