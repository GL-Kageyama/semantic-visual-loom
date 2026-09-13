# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第6話 S26「すれ違い」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**すれ違い、指は休む——夜の部屋から昼の学校へ一転。湊とすれ違うだけで、真白は何もせず。最大の秒は「見なかった湊」と「背中を見る真白」に配る。ニジは不在（台帳 26）。湊は真白を見ない——書類の束を抱えて早足で。**

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

> **湊 appears this segment** — third-year 氷室湊, composed, carries document bundles; glimpsed only, does not look at 真白. ニジ is absent (ledger 26 — the ghost does not exist in this scene).

---

# 4. ENVIRONMENT

## Location

- ID: `CORRIDOR`
- Name: `学校の廊下 (the school corridor)`
- Description: `School hallway at lunch break, windows throwing long white rectangles of light onto the floor, pale flat daylight, distant class voices. 真白 stands in the mid-ground`

## Environmental Behavior

- Wind: `none — still daylight, nothing moves`
- Particles: `at most a faint drift of dust or haze in the daylight`
- Background Motion: `almost none — distant blurred students, motionless`

---

# 5. OBJECTS

## DOCUMENT_BUNDLE

- Type: `papers`
- Appearance: `A bundle of festival-committee documents carried against 湊's side — white sheets, the corners swaying slightly with his stride`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
- Continuity Importance: `HIGH`

## SCREEN_TEXT

- Type: `UI text`
- Appearance: `No screen text this segment — the passing is wordless, and no screen appears`
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

The next day, lunch break, the corridor. 真白 passes 湊. 湊 does not look at her — carrying a bundle of festival-committee documents, he walks quickly past. 真白 watches his back.

## Beginning

The corridor at lunch break. Distant class voices echo. Window light falls white onto the floor.

## Turn

湊. Carrying a bundle of festival-committee documents, walking quickly. He does not look at 真白. The white document corners sway. In the instant of passing, 湊's profile enters 真白's eyes, then is gone.

## Peak

真白 watches his back. In 湊's back she sees the outline of the time she deposited. The receding back turns the corridor corner and disappears.

## Pull（引き — 切れ目）

――自分からは届かない。――届けたら壊れる。――だから、真白は、ずっと、見てるだけだった。Cut on the empty corridor.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The passing holds 9s (30%); the watching back holds 9s.

## Temporal Units

- BEAT — a held view over a single stretch of the corridor; the passing is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「昼休みの廊下」.** Day. Distant class voices echo. Window light falls white onto the floor. 真白 stands in the corridor. _Density: SPARSE — daylight, still, untroubled._
- **BEAT 2 `[0:06–0:15]` — 「すれ違い」 — longest share.** 湊. Carrying a bundle of festival-committee documents, walking quickly. He does not look at 真白. The white document corners sway. In the instant of passing, a profile enters and is gone. _Density: DENSE — the whole exchange is a non-exchange._
- **BEAT 3 `[0:15–0:24]` — 「背中」.** 真白 watches his back. In 湊's back she sees the outline of the time she deposited. The receding back turns the corridor corner. _Density: SPARSE — the camera holds on her watching._
- **BEAT 4 `[0:24–0:30]` — 「見えなくなる」.** The back turns the corner and is gone. The empty corridor. ――自分からは届かない。届けたら壊れる。Cut on the empty corridor. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `湊 passing without looking (≈0:08) ／ the profile glimpsed (≈0:11) ／ the back turning the corner (≈0:20)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the corridor), 0:15–0:24 (the watching)`
- Dense regions: `0:06–0:15 (the passing)`
- Long continuous action: `0:15–0:24 the receding back`
- Rapid transitions: `none — the whole segment is one held passing`

---

# 9. ACTION

## Action — ACT_WAIT

- ID: `ACT_WAIT`
- Subject: `MASHIRO`
- Action: `Stands in the corridor as the class voices echo; then her eyes catch 湊 approaching`
- Intention: `None — an ordinary moment, about to be interrupted`
- Intensity: `Low`
- Speed: `Still, ordinary`

### Action Relationship

- Before: `— (continues from S25's dark, cut to day)`
- After: `ACT_PASS`

## Action — ACT_PASS

- ID: `ACT_PASS`
- Subject: `MINATO`
- Action: `Passes 真白 quickly, carrying a bundle of festival-committee documents, without looking at her`
- Intention: `None toward her — he is on an errand and does not see her`
- Intensity: `Low`
- Speed: `Quick, composed, unhurried in his own direction`

### Action Relationship

- Before: `ACT_WAIT`
- After: `ACT_GLIMPSE`

## Action — ACT_GLIMPSE

- ID: `ACT_GLIMPSE`
- Subject: `MASHIRO`
- Action: `In the moment of passing, her eyes catch 湊's profile — a white document corner swaying — and it is gone`
- Intention: `Involuntary — the eye finds what it has always searched for`
- Intensity: `Medium, internal`
- Speed: `One instant, then gone`

### Action Relationship

- Before: `ACT_PASS`
- After: `ACT_WATCH_BACK`

## Action — ACT_WATCH_BACK

- ID: `ACT_WATCH_BACK`
- Subject: `MASHIRO`
- Action: `Watches his back recede; in it she sees the outline of the time she deposited`
- Intention: `None — the watching is all she does`
- Intensity: `HIGH, internal, entirely still`
- Speed: `Held, until the back turns the corner`

### Action Relationship

- Before: `ACT_GLIMPSE`
- After: `ACT_GONE`

## Action — ACT_GONE

- ID: `ACT_GONE`
- Subject: `MASHIRO`
- Action: `The back turns the corner and is gone; the corridor is empty. She does not follow`
- Intention: `To stay where she has always stayed — watching only`
- Intensity: `Medium, suppressed`
- Speed: `Still, then cut`

### Action Relationship

- Before: `ACT_WATCH_BACK`
- After: `— (cut on the empty corridor)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Level, at standing height, in the corridor. 真白's point of view for the passing`
- Lens Character: `Long-ish, shallow. 湊 is a figure moving through soft daylight`
- Depth of Field: `Shallow — the corridor falls away to pale blurred students and windows`
- Camera Style: `Slow, deliberate, nearly still. One held view, and it belongs to the passing`

## Camera Events

- **`[0:00–0:06]`** — Static wide on the corridor — window light throwing white rectangles onto the floor, distant class voices. 真白 in the mid-ground.
- **`[0:06–0:11]`** — Cut to 真白's point of view: 湊 approaching with a bundle of documents, his face not toward her.
- **`[0:11–0:15]`** — The passing, in close — the white document corners swaying, his profile entering and leaving the frame in a single instant.
- **`[0:15–0:24]`** — Cut back to 真白, watching; over her shoulder, the receding back down the corridor. The camera does not move.
- **`[0:24–0:30]`** — The back turns the corner and is gone. Hold on the empty corridor. Cut.

---

# 11. MOTION

## Subject Motion

- 湊 moves with an unhurried, composed stride, the document bundle held to his side
- 真白 is nearly still; only her head turns a few degrees to keep the back in view
- No one else is in focus; the blurred students are distant and motionless

## Object Motion

- The white document corners sway slightly with 湊's stride — the only small, quick motion
- Nothing supernatural moves; the corridor is ordinary

## Environmental Motion

- The window light is still; long rectangles of light lie unmoving on the floor
- A faint drift of dust or haze in the daylight, at most

## Physical Characteristics

- Weight: `Ordinary. Bodies and paper have heft`
- Inertia: `High — the passing is steady and composed`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Ordinariness (the corridor, the voices, the light)
- ↓ A non-exchange (he passes, and does not see her)
- ↓ The outline of the deposited time (in his receding back)
- ↓ The distance, named (自分からは届かない — and the corridor empty)

## Emotional Events

- Event: `湊 passes without looking` — Emotion: `The distance made physical` — Intensity: `HIGH, but quiet` — Timing: `≈0:08`
- Event: `The profile, glimpsed and gone` — Emotion: `A flash of the person she has watched` — Intensity: `MEDIUM, internal` — Timing: `≈0:11`
- Event: `The back turning the corner` — Emotion: `The outline of the deposited time, receding out of reach` — Intensity: `CRITICAL — expressed only as a held gaze` — Timing: `0:20–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Pale flat daylight from the corridor windows — soft, slightly overexposed, muted`
- Fill Light: `Even, flat. The corridor is bright and unbothered`
- Rim Light: `A faint cool edge along 湊's hair and the document bundle`
- Ambient Light: `Day. Muted, low-saturation`
- Color Temperature: `≈5600K pale daylight. No screen light — the night is over`

## Lighting Events

- **`[0:00]`** — Daylight already full; white rectangles of window light on the floor.
- **`[0:06–0:15]`** — As 湊 passes, the light catches the white document corners — a bright, swaying edge against the pale corridor.
- **`[0:15–0:24]`** — 真白 watches from the mid-ground; the receding back moves toward the bright window light.
- **`[0:24–0:30]`** — The back turns the corner out of the light. The corridor empties. Cut.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The passing is not spoken. No narration, no voice-over.

## Sound Effects

- Distant class voices, echoing down the corridor, unbroken
- 湊's composed, receding footsteps — the segment's pulse
- The faint rustle of the document bundle as he passes
- The corridor's quiet, after he is gone

## Environment

- Day. Full and ordinary school ambience — voices, soft foot traffic, the hollow of a hallway

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the day's surface, then thin as he passes — by the empty corridor there is only the receding footsteps, and then the quiet`

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

- 湊 must not look at 真白 — he passes quickly, carrying a bundle of festival-committee documents, without seeing her
- 湊's face appears only in profile, and only for the single instant of passing — no frontal face, no held gaze
- 真白 in her standard school uniform, in the corridor at lunch break
- 真白 watches his back, and does not follow — the distance is the point
- End on the empty corridor after the back turns the corner, cut on the pull

## MUST NOT（この1本の禁止・開示台帳 26 レンジより）

- **Do not show ニジ.** No figure, no silhouette, no reflection, no eyes, no rainbow, no iridescence, no colored afterimage. She does not exist in this scene
- **湊 must not look at 真白.** The single look — even a glance — would break the reveal withheld until S47
- Do not have 真白 call out, wave, or follow — she stays and watches only
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The passing held long, unhurried — the whole segment is one held gaze
- Silence over score at the empty corridor
- 真白's point of view for the passing, and her watching for the pull

## ALLOW

- Slight variation in corridor background students and window arrangement
- The document bundle may be partly out of focus — only the passing and the back must read
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not be shown (ledger 26 — the ghost does not exist in this scene); 湊 must not look at 真白. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school corridor at lunch break, pale flat daylight. Beats, deliberately uneven: [0:00–0:06] the corridor, distant class voices, white rectangles of window light on the floor; [0:06–0:15] 湊 — a composed third-year boy on the festival committee — passes 真白 quickly, carrying a bundle of documents, without looking at her; the white document corners sway, and his profile enters and leaves the frame in a single instant; [0:15–0:24] 真白 watches his back recede down the corridor, seeing in it the outline of the time she deposited; [0:24–0:30] the back turns the corner and is gone, the corridor empties, and the shot cuts on the empty corridor. The passing holds the largest share of the duration. Ends on the empty corridor, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. By day she wears a standard Japanese school uniform. Scene: a Japanese high-school corridor at lunch break, pale flat daylight, slightly overexposed and muted, white rectangles of window light on the floor. 湊 (Minato) — a third-year boy, festival committee, composed, short neat dark hair, a little taller than 真白, in the boys' school uniform, carrying a bundle of white documents; he passes without looking at 真白, his face shown only in profile for a single instant. No ghost, no rainbow, no afterimage anywhere. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. 湊 moves with an unhurried, composed stride, the document bundle held to his side, the white corners swaying slightly. 真白 is nearly still; only her head turns a few degrees to keep the back in view. No one else is in focus. The window light is still; long rectangles of light lie unmoving on the floor. Ordinary weight and inertia; gentle acceleration everywhere. No impacts, no collisions, no motion blur smears, no squash and stretch. Nothing supernatural moves — the corridor is ordinary.

## Camera Prompt

Level, at standing height, in the corridor. Longish lens, shallow depth of field; 湊 is a figure moving through soft daylight. Slow and deliberate, nearly still. [0:00–0:06] static wide on the corridor, window light on the floor, 真白 in the mid-ground. [0:06–0:11] cut to 真白's point of view, 湊 approaching with the documents, his face not toward her. [0:11–0:15] the passing in close, the white document corners swaying, his profile entering and leaving the frame in a single instant. [0:15–0:24] cut back to 真白 watching, the receding back over her shoulder; the camera does not move. [0:24–0:30] the back turns the corner and is gone; hold on the empty corridor; cut.

## Audio Prompt

Day. Full ordinary school ambience — distant class voices echoing down the corridor, soft foot traffic, the hollow of a hallway. No speech at all. 湊's composed, receding footsteps are the segment's pulse, with the faint rustle of the document bundle as he passes. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as he passes and leaving only the receding footsteps, then the quiet of the empty corridor. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep06-seg05-30s-01`
- Segment ID: `S26`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_06, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 9s / 9s / 6s. Passing = BEAT 2 at 9s (30%)`
- Camera Events: `5 events as listed in §10. No sustained dolly; all static or cut`
- Action Events: `ACT_WAIT → ACT_PASS → ACT_GLIMPSE → ACT_WATCH_BACK → ACT_GONE`
- Audio Events: `no dialogue ／ receding footsteps ／ no music after the passing`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the empty corridor`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **湊 looking at 真白.** The single most damaging failure — even a glance breaks the reveal withheld until S47. Verify frame by frame that his eyes never meet hers.
- **The model may add ニジ.** The series has trained the model to expect her. The negative prompt front-loads "no ghost, no rainbow"; verify no afterimage, no silhouette, no color leaks into the daylight.
- **湊's face reading as a full portrait.** He must appear only in profile, for a single instant. If the model holds his face, the passing loses its distance.
- **真白 following or calling out.** She must stay and watch only. The restraint is the emotion.

## Changes

- _(none yet)_

## Next Generation

- This closes episode 6. S27 (文化祭前夜) returns to the day, and ニジ remains absent through S28 — do not carry her back in.
