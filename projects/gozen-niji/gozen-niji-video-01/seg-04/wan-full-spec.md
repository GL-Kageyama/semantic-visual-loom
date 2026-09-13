# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第1話 S04「消えた記録」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「引き算」の所作——設定を開き、あの記録が消えて合計から1時間21分だけ抜けているのを見る（指の背骨の第4本・第1話で唯一の昼）。ニジは不在（記録すら消えて、画面にすら現れない）。登場人物は真白と美月（初登場）。画面文字なし（設定画面の合計から1時間21分だけ抜けている数字）。考えるより先に顔が笑う——全編で真白が声に出す唯一の台詞は嘘。**

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

> **One other character appears this segment — 美月 (MITSUKI), first appearance.** ニジ is absent (ledger 01–05 — the ghost exists only as text on the screen). 美月 is 真白's bright, casual best friend; established here for the first time, so slight variation in her appearance is allowed.

---

# 4. ENVIRONMENT

## Location

- ID: `BEDROOM → SCHOOL_ENTRANCE → 帰り道`
- Name: `真白の部屋（朝） → 学校の下駄箱 → 帰り道`
- Description: `The only daytime segment of episode 1. Morning in her bedroom (the curtain opened on a flat pale morning), then the school shoe lockers, then the road home. The waking world — full and fast`

## Environmental Behavior

- Wind: `none — a still, even day`
- Particles: `none — no dust motes, no floating lights, no VFX`
- Background Motion: `out-of-focus students cross the school background; pale daylight static and even; nothing supernatural moves`

---

# 5. OBJECTS

## PHONE

- Type: `smartphone`
- Appearance: `真白's ordinary modern smartphone, plain case, Japanese UI. The only surface on which the anomaly appears. At night the only light source; by day it stays in her bag, unlit, its weight carrying the sentence. Glass carries a soft bloom, never a hard specular glint`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
- Continuity Importance: `CRITICAL`

## SCREEN_TEXT

- Type: `UI text`
- Appearance: `No message text this segment — only ordinary UI: a screen-time settings panel whose day-total is short by exactly 1時間21分, the erased 2:00 A.M. record gone, every minute she actually spent still present. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI, now muted against the pale room`
- Narrative Importance: `HIGH`
- Visual Importance: `HIGH`
- Continuity Importance: `HIGH`

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

Morning subtracts the evidence: the record is gone, and the day's total is short by exactly 1 hour 21 minutes — while she goes through the day as always, smiling a smile she did not choose, and lying that she watched a video she never watched.

## Beginning

翌朝。The record is gone — the 2:00 A.M. entry erased as if it had never been. She gets up, opens the curtain. 昨日と同じ朝だった。

## Turn

Yet her finger opens the settings — screen time. The previous day's total is short by exactly that one hour twenty-one minutes. Every minute she actually spent remains. Only that record is missing, even from the total.

## Peak

School. She smiles the way she always does — slightly outside the middle of the circle. 美月 speaks: 「昨日さ、あれ、見た？」 真白's face arrives at a smile before she has decided to smile: 「見た見た。おもしろかった」. She did not watch it.

## Pull（引き — 切れ目）

帰り道。鞄の中のスマホが、重く感じられた。あの文が、中に入っているみたいに。Cut on her walking home, the phone's weight in her bag — the sentence stuck to her back.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The school beat holds 12s (40%) — the world moves faster than she does.

## Temporal Units

- BEAT — a held gaze over a single stretch of the day; the school beat is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:09]` — 「翌朝、記録は消えていた」.** Flat pale morning. She opens the curtain; the day is ordinary. Her finger in the settings: the record is gone, and the total is short by exactly 1時間21分. She stares at the number. _Density: SPARSE — two small moves, the subtraction held._
- **BEAT 2 `[0:09–0:21]` — 「学校、いつもの笑顔」 — longest share.** School. The shoe lockers. 美月 approaches, bright and casual. 「昨日さ、あれ、見た？」 — 真白's face reaches the smile before she has decided to smile. 「見た見た。おもしろかった」 美月 laughs 「だよねー」. It passes. Another ordinary day. _Density: DENSE, brisk — the waking world is full and fast._
- **BEAT 3 `[0:21–0:30]` — 「背中に張り付く」 — PULL.** 帰り道。She walks. The phone in her bag feels heavy, as if the sentence were inside it. Her face, still, forward. Cut on her walking. _Density: HELD — then cut precisely on the pull. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the total short by exactly 1時間21分 (≈0:06) ／ the smile arriving before the decision (≈0:14) ／ the lie (≈0:16) ／ the phone's weight (≈0:24)`

## Temporal Density

- Sparse regions: `0:00–0:09 (the subtraction), 0:21–0:30 (the walk)`
- Dense regions: `0:09–0:21 (school — the only full, brisk passage in episode 1)`
- Long continuous action: `0:21–0:30 the walk home`
- Rapid transitions: `0:09–0:21 (morning to school, the social beat)`

---

# 9. ACTION

## Action — ACT_CHECK

- ID: `ACT_CHECK`
- Subject: `MASHIRO`
- Action: `Opens the settings; reads the total that is short by exactly 1時間21分`
- Intention: `To find the record — and finds its absence`
- Intensity: `Medium, internal`
- Speed: `Steady, then still`

### Action Relationship

- Before: `—` (continues from S03's re-read)
- After: `ACT_WEAR_SMILE`

## Action — ACT_WEAR_SMILE

- ID: `ACT_WEAR_SMILE`
- Subject: `MASHIRO`
- Action: `Her face arrives at a smile at school, before any decision to smile`
- Intention: `To keep the surface intact — the muscles do it by themselves`
- Intensity: `Low, and false`
- Speed: `Instant — faster than thought, which is the point`

### Action Relationship

- Before: `ACT_CHECK`
- After: `ACT_LIE`

## Action — ACT_LIE

- ID: `ACT_LIE`
- Subject: `MASHIRO`
- Action: `Says 「見た見た。おもしろかった」 about a video she never watched, and laughs lightly`
- Intention: `To end the conversation cleanly`
- Intensity: `Low`
- Speed: `Immediate, easy`

### Action Relationship

- Before: `ACT_WEAR_SMILE`
- After: `ACT_WALK`

## Action — ACT_WALK

- ID: `ACT_WALK`
- Subject: `MASHIRO`
- Action: `Walks home; the phone in her bag feels heavier than it should`
- Intention: `None — just the walk`
- Intensity: `Medium, suppressed`
- Speed: `Ordinary`

### Action Relationship

- Before: `ACT_LIE`
- After: `— (cut on the pull)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Daytime: a little further back than the night takes — we observe her across the room, across the hall, not inside her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Slightly deeper than the night beats; the waking world is in focus around her`
- Camera Style: `Slightly more movement than the night — a slow push, a mild drift. Still never whips or shakes`

## Camera Events

- **`[0:00–0:05]`** — Static wide of the curtain opening on a flat pale morning. Then a slow push to the settings screen and the shortened total.
- **`[0:05–0:09]`** — Locked on the number — the total short by exactly 1時間21分. Static. The only sharp thing in the room is the number.
- **`[0:09–0:13]`** — Cut to the shoe lockers. Slight handheld drift (the only handheld in episode 1 — the waking world is less steady than the night).
- **`[0:13–0:18]`** — Close on 真白's smile arriving before the rest of her face.
- **`[0:18–0:21]`** — Two-shot of 真白 and 美月, bright and casual. The lie passes.
- **`[0:21–0:30]`** — Cut to 帰り道. Static, medium, from behind her — her back, her bag, the phone inside it. Hold as she walks. Cut.

---

# 11. MOTION

## Subject Motion

- In the morning, her fingers move precisely and then still on the number
- At school her body moves normally but her face moves first — the smile precedes her
- On the walk home she moves at an ordinary pace; only the bag sways slightly

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a settings panel opening. Nothing glitches, flickers, distorts, or behaves supernaturally
- At school, the phone stays in her bag; it does not light

## Environmental Motion

- Out-of-focus students cross the background at school
- Pale daylight, static and even; no wind
- Nothing supernatural moves anywhere

## Physical Characteristics

- Weight: `Ordinary — with one exception: the phone in her bag reads slightly too heavy. This is internal, not visual — the bag does not visibly sag`
- Inertia: `Normal for a person going through a day`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation, slightly fuller in the school beat`
- Impact: `None`

---

# 12. EMOTION

## Emotional Arc

- Cold absence (the record is gone)
- ↓ Suppression (the smile that arrives by itself)
- ↓ Practiced ease (the lie, delivered cleanly)
- ↓ Weight (the sentence stuck to her back)

## Emotional Events

- Event: `The total is short by exactly 1時間21分` — Emotion: `Cold absence — the evidence removing itself` — Intensity: `HIGH, internal` — Timing: `≈0:06`
- Event: `The smile arrives before the decision` — Emotion: `Practiced absence` — Intensity: `LOW, deliberately hollow` — Timing: `≈0:14`
- Event: `The lie 「見た見た」` — Emotion: `The cost of the surface` — Intensity: `LOW` — Timing: `≈0:16`
- Event: `The phone's weight in her bag` — Emotion: `The sentence stuck to her back` — Intensity: `MEDIUM, suppressed` — Timing: `0:21–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Flat pale daylight — even, slightly overexposed, not warm or hopeful, merely neutral`
- Fill Light: `Broad and soft; the morning has no deep shadow`
- Rim Light: `None — the day is even`
- Ambient Light: `Pale, flat. The world is legible everywhere`
- Color Temperature: `≈5200K flat daylight, slightly cool. Nothing golden, nothing warm`

## Lighting Events

- **`[0:00]`** — Hard cut from S03's dark to flat pale morning — the harshest lighting change in episode 1. Daylight is not relief; it is merely even.
- **`[0:05–0:09]`** — The settings screen glows faintly in the daylight — the phone's blue-white now muted against the pale room.
- **`[0:09–0:21]`** — School: neutral, unremarkable daylight. No dramatic shafts.
- **`[0:21–0:30]`** — Late-afternoon light on the way home, slightly lower, still muted. Her back is in shadow — the bag, and what is inside it, is not.

---

# 14. AUDIO

## Dialogue

### Dialogue Event

- Speaker: `MITSUKI (美月 — 真白's friend, first appearance)`
- Content: `「昨日さ、あれ、見た？」`
- Timing: `≈0:13`
- Delivery: `Casual, bright, entirely unremarkable — the sound of an ordinary school morning`

### Dialogue Event

- Speaker: `MITSUKI`
- Content: `「だよねー」`
- Timing: `≈0:18`
- Delivery: `Light, easy`

### Dialogue Event

- Speaker: `MASHIRO`
- Content: `「見た見た。おもしろかった」`
- Timing: `≈0:16`
- Delivery: `Light, easy, immediate. Nothing in the voice indicates it is a lie. It is the only thing 真白 says aloud in the entire episode — and it is untrue`

## Sound Effects

- Morning: faint birds, distant traffic, a house waking
- School: shoe lockers, distant chatter, ordinary corridor noise — briefly and suddenly full, then gone
- 帰り道: her footsteps, the soft swing of her bag, distant city sound

## Environment

- Morning and day: fuller than the night — the waking world is loud, but not warm
- 帰り道: thinning again toward the quiet of the night to come

## Music

- Style: `Sparse — a few soft sustained tones, or nothing`
- Tempo: `Slow`
- Mood: `Suspended, unresolved. Never sentimental`
- Emotional Function: `The day passes under the same suspended tension as the night — the music does not resolve it. It may thin entirely on the walk home`

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

- Show the total short by exactly 1時間21分 — the subtraction is the evidence
- Let the smile arrive before the decision to smile
- Render the two spoken lines exactly as given: 美月「昨日さ、あれ、見た？」 ／ 真白「見た見た。おもしろかった」
- End on the walk home, the phone heavy in her bag, cut on the pull

## MUST NOT（この1本の禁止・開示台帳 01–05 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person in the night scenes, no eyes, no hand but her own
- **No rainbow, no iridescence, no colored afterimage**
- No second character other than 美月
- No on-screen subtitles or captions burned in
- The record must not reappear — it is gone. Do not show any supernatural trace in the day

## PREFER

- The school beat brisk and full, then the walk home quiet — the contrast is the point
- 真白 slightly outside the middle of the circle — not alone, not included
- The phone's weight conveyed by her posture, never by a visible effect

## ALLOW

- Slight variation in 美月's appearance (she is first established here)
- Slight variation in the shoe lockers, school hallway, and the road home
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not be shown (ledger 01–05 — the ghost exists only as text on the screen); the only other character is 美月, in her first appearance. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school girl the morning after a strange night. Beats, deliberately uneven: [0:00–0:09] flat pale morning, she opens the curtain, then her finger opens the settings and reads a screen-time total that is short by exactly 1時間21分 — the record gone, every minute she actually spent still there; [0:09–0:21] school, the shoe lockers, a bright casual girl asks 昨日さ、あれ、見た？ and 真白's face reaches a smile before she has decided to smile, answering 見た見た。おもしろかった about a video she never watched, the friend laughing だよねー; [0:21–0:30] 帰り道, she walks home, the phone in her bag feeling heavy, as if the sentence were inside it, and the shot cuts on her walking. The school beat holds the largest share of the duration. Ends on the pull, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, simple uncluttered rooms, generous negative space, one focal point per shot. A plain unremarkable Japanese high-school girl, 16–17, shoulder-length dark hair, a thin neck, small frame, back slightly curved, now in a standard Japanese school uniform; her friend 美月, a bright casual girl with slightly shorter, livelier hair and an open upright posture, in the same uniform. Morning and school are flat pale even daylight, slightly overexposed, not warm or hopeful, merely neutral; late-afternoon light on the way home is slightly lower but still muted, her back in shadow. The phone screen, where it appears, shows an ordinary Japanese UI in cold blue-white, now muted against the pale room. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. In the morning her fingers move precisely and then still on the number. At school her body moves normally but her face moves first — the smile precedes her, faster than thought. On the walk home she moves at an ordinary pace, the bag swaying slightly. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. Out-of-focus students cross the background at school. Pale daylight is static and even, no wind. The phone in her bag reads slightly too heavy, but this is internal — the bag does not visibly sag. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Daytime: a little further back than the night takes — we observe her across the room, across the hall, not inside her. Longish lens, shallow depth of field slightly deeper than the night beats. Slightly more movement than the night — a slow push, a mild drift — but never whipping or shaking. [0:00–0:05] static wide of the curtain opening, then a slow push to the settings screen and the shortened total. [0:05–0:09] locked on the number, static. [0:09–0:13] cut to the shoe lockers, slight handheld drift. [0:13–0:18] close on 真白's smile arriving before the rest of her face. [0:18–0:21] two-shot of 真白 and 美月. [0:21–0:30] cut to 帰り道, static, medium, from behind her; hold as she walks; cut.

## Audio Prompt

Morning: faint birds, distant traffic, a house waking. School: shoe lockers, corridor chatter, ordinary daylight noise — briefly and suddenly full, then gone. 帰り道: her footsteps, the soft swing of her bag, distant city sound. Only three spoken lines: a bright casual girl's voice asking 昨日さ、あれ、見た？, the protagonist answering lightly and immediately 見た見た。おもしろかった (it is a lie — she never watched it), and the friend laughing だよねー. No narration, no voice-over. Music sparse — a few soft sustained tones at most — thinning on the walk home. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person in the night scenes, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep01-seg04-30s-01`
- Segment ID: `S04`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_01, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `3 beats, NON_UNIFORM — 9s / 12s / 9s. School = BEAT 2 at 12s (40%)`
- Camera Events: `6 events as listed in §10. Mild handheld in the school beat only`
- Action Events: `ACT_CHECK → ACT_WEAR_SMILE → ACT_LIE → ACT_WALK`
- Audio Events: `3 dialogue lines (all in the school beat) ／ morning and school ambience ／ music thins on the walk`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the walk home`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- *(none yet — to be filled after the first generation)*

## Anticipated risks (to check in the first generation)

- **The subtraction must read.** The total short by exactly 1時間21分 is the only "event" of the morning. If the number is unreadable, the beat loses its meaning. Check the number; if unusable, composite it in post.
- **The smile must be hollow, not happy.** A generated smile will tend toward warmth. The point is that it arrives before the decision, faster than thought — if it reads as genuine joy, tone it down.
- **Identity drift across the night-to-day cut.** Her face may shift between the night and day registers. §15 (in series-constants) is the defense; if drift appears, generate the school beat separately.
- **The model may add a ghost or a rainbow in the daylight.** The negative prompt front-loads this; verify frame by frame.

## Changes

- *(none yet)*

## Next Generation

- If the school beat reads well, consider holding the walk home 1–2 seconds longer — the phone's weight is the segment's true end.
