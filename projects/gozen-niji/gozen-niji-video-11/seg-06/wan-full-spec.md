# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第11話 S51「残る記録は、ひとつ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「残る記録は、ひとつ」——午前二時、残る記録を開く（指の背骨の第51本）。屋台の灯りから自分の部屋へ帰り、身に覚えのない記録が最後に残った記録として、もう一度同じ数字で現れる。指は迷いなく、それを開く。最大の秒は「残る記録は、ひとつだけ」という開示と、その数字に配る。ニジは不在（第11話に幽霊はいない）。登場人物は真白のみ（湊は屋台に残る）。画面文字は「午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ」。**

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

> **No other character appears this segment.** 湊 stays at the festival; 真白 is alone in her room. ニジ is absent（ledger 46–51 — the ghost does not appear in this chapter）.

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

- Type: `smartphone (真白's)`
- Appearance: `真白's ordinary modern smartphone, plain case, Japanese UI. The only light source at night; the only surface on which the anomaly appears. Glass carries a soft bloom, never a hard specular glint`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
- Continuity Importance: `CRITICAL`

## SCREEN_TEXT

- Type: `UI text`
- Appearance: `One remaining record, rendered exactly as an ordinary phone renders it: cold blue-white on dark UI — 午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
- Continuity Importance: `HIGH`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads just past 2:00 A.M.`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_11_最後の宛先、湊.md`
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

Night, 2:00 A.M. Back in her room, 真白 opens her phone — screen time, the addressee list — and finds that only one record remains. It is the first one: the message addressed to herself.

## Beginning

The festival is over. 真白, in her futon, in the dark, opens her phone at 2:00 A.M. The screen's light is the only light.

## Turn

Screen time. The addressee list. The rows that were once filled are gone, returned one by one. 残る記録は、ひとつだけ。

## Peak

The record — the first one — fills the frame: 午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ. 最初の記録。自分自身へ、宛てた言葉。

## Pull（引き — 切れ目）

Cut on the record, held on screen, with nothing after it — the last night-time record, waiting for the finale.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The single remaining record holds 11s (37%).

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「開く」 — ESTABLISH.** Night, 2:00 A.M. Her room, dark, the futon warm. She opens the phone; its light is the only light. _Density: SPARSE — the familiar ritual, quiet._
- **BEAT 2 `[0:06–0:17]` — 「残る記録」 — TURN, longest share.** Screen time. The addressee list. The rows returned, one by one. 残る記録は、ひとつだけ。_Density: DENSE at the head (the empty list), then held._
- **BEAT 3 `[0:17–0:25]` — 「最初の記録」 — PEAK.** The one record fills the frame: 午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ. 最初の記録。自分自身へ、宛てた言葉。_Density: SPARSE, inverted — the event is the numbers, held._
- **BEAT 4 `[0:25–0:30]` — 「自分自身へ」.** The record on screen, still. Her face, lit from below, still. Cut on the record. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the single remaining record (≈0:08) ／ the numbers filling the frame (≈0:18) ／ 自分自身へ (≈0:24)`

## Temporal Density

- Sparse regions: `0:00–0:06 (opening), 0:17–0:25 (the held record)`
- Dense regions: `0:06–0:17 (the list emptied to one)`
- Long continuous action: `0:25–0:30 the held record on screen`
- Rapid transitions: `none — the slowest, most held segment of the episode`

---

# 9. ACTION

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MASHIRO`
- Action: `Opens the phone at 2:00 A.M., in the dark, in her futon`
- Intention: `To see what remains`
- Intensity: `Low`
- Speed: `Slow, practiced — the same ritual as always`

### Action Relationship

- Before: `—` (returns from the festival night)
- After: `ACT_READ_LIST`

## Action — ACT_READ_LIST

- ID: `ACT_READ_LIST`
- Subject: `MASHIRO`
- Action: `Opens screen time, then the addressee list, and finds only one record left`
- Intention: `To take in the emptying — all the rows returned`
- Intensity: `Medium, internal`
- Speed: `Slow; the eyes move down the empty list`

### Action Relationship

- Before: `ACT_OPEN`
- After: `ACT_READ_RECORD`

## Action — ACT_READ_RECORD

- ID: `ACT_READ_RECORD`
- Subject: `MASHIRO`
- Action: `Reads the one record — 午前2時00分〜午前3時21分 — the first record, the message to herself`
- Intention: `To recognize it. Not dread, now — return`
- Intensity: `HIGH, entirely internal`
- Speed: `Very slow; the eyes hold on the numbers`

### Action Relationship

- Before: `ACT_READ_LIST`
- After: `ACT_STILL`

## Action — ACT_STILL

- ID: `ACT_STILL`
- Subject: `MASHIRO`
- Action: `Her face goes still, lit from below; the record stays on screen. Nothing moves`
- Intention: `None — the recognition, settling`
- Intensity: `Medium, restrained`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_READ_RECORD`
- After: `— (cut on the record)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Very shallow — often only the screen or her face is sharp`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Static, close on her hand and the phone, the screen waking in the dark. Her face, lit from below, in the background.
- **`[0:06–0:13]`** — A slow tilt down to the screen as the addressee list opens — the rows empty, returned. Only one remains.
- **`[0:13–0:17]`** — One slow continuous dolly in on the list until the single remaining record fills the frame.
- **`[0:17–0:25]`** — Absolutely locked on the record. Static. The numbers held.
- **`[0:25–0:30]`** — Pull focus off the screen onto her still face, lit from below. Hold. Cut on the record and her face.

---

# 11. MOTION

## Subject Motion

- Her body moves slowly and heavily — the familiar ritual, unhurried
- Her fingers carry the small precise movements — opening screen time, the list
- The stillness at the end is absolute: not a pause, but a stop

## Object Motion

- The phone moves only as her hand moves it — ordinary UI transitions, nothing supernatural
- Screen content changes by ordinary UI only; nothing glitches, flickers, or distorts
- The wall clock's second hand advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers once they move`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Return (the festival over, the room unchanged)
- ↓ Recognition (the list emptied to one)
- ↓ Arrival (the first record — the message to herself)
- ↓ Stillness (the recognition, settling)

## Emotional Events

- Event: `The list, returned to one` — Emotion: `Recognition — the emptying is complete, not frightening` — Intensity: `MEDIUM, internal` — Timing: `≈0:08`
- Event: `The one record — 午前2時00分〜午前3時21分` — Emotion: `Arrival — the first record, understood at last` — Intensity: `HIGH, entirely internal` — Timing: `≈0:18`
- Event: `Her face goes still` — Emotion: `Stillness — 自分自身へ、宛てた言葉` — Intensity: `MEDIUM, restrained` — Timing: `0:25–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo`

## Lighting Events

- **`[0:00]`** — Dark, near-black. The faintest ambient indigo; her face barely legible.
- **`[0:00–0:06]`** — The screen wakes: its bloom expands into the dark. The only light.
- **`[0:06–0:17]`** — As the camera closes on the screen, its light dominates the frame; her face falls almost to silhouette. The record outshines the person.
- **`[0:25–0:30]`** — Her face returns, dim, lit only from below. The record still glowing.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The record is read, not spoken. No narration, no voice-over.

## Sound Effects

- The wall clock's second hand, dry discrete ticks, present throughout
- Soft futon fabric as she shifts and opens the phone
- The soft sound of a finger on glass, once, as the list opens

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, resolved. Never sinister, never sentimental — no horror strings, no swelling`
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

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。Negative の土台は series-constants のもの＋先頭にこの本の禁止。

## MUST

- Render the on-screen Japanese exactly: `午前2時00分〜午前3時21分` ／ `使用時間　1時間21分` ／ `アプリ　メッセージ`
- Show the list emptied to a single remaining record — 残る記録は、ひとつだけ
- Keep the phone screen the sole night light source
- End on the record on screen and her still face, cut on the pull

## MUST NOT（この1本の禁止・開示台帳 46–51 レンジより）

- **ニジは登場しない。** No ghost, no figure, no silhouette, no reflection, no second person, no eyes, no hand but her own. This episode has no ニジ at all
- **No rainbow, no iridescence, no colored afterimage**
- **No second character** — 湊 stays at the festival; this is 真白 alone in her room
- No on-screen subtitles or captions burned in (the record is diegetic, not a subtitle)
- Do not give this record the dread of S02 — it is return, not fear

## PREFER

- Framing the record large, straight-on and held rather than skimmed
- Silence over score at the peak
- Holds over movement; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in may be omitted
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not appear (ledger 46–51 — the ghost does not appear in this chapter); 真白 alone, no second character. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:06] she opens her phone in the dark, the screen the only light; [0:06–0:17] THE TURN — she opens screen time, then the addressee list, and finds the rows all returned, 残る記録は、ひとつだけ, only one record left; [0:17–0:25] the one record fills the frame, reading exactly 午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ — the first record, the message to herself; [0:25–0:30] her face goes still in the dim light, the record still on screen, and the shot cuts on the record and her face. The single remaining record holds the largest share of the duration. Ends on the record, held, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. She is alone, in plain pajamas in a futon on the floor. The phone screen shows an ordinary Japanese UI in cold blue-white, an addressee list emptied to a single remaining record reading exactly 午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her body moves slowly and heavily; her fingers carry the small precise movements, opening screen time and the list. The stillness at the end is absolute — not a pause but a stop. Ordinary weight and inertia: the phone has heft, the futon compresses. The phone moves only as her hand moves it; it never moves by itself and never glitches, flickers or distorts, its screen changing only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No wind, no moving shadows, no particles. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or her face is sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] static, close on her hand and the phone, the screen waking in the dark. [0:06–0:13] a slow tilt down to the screen as the addressee list opens, the rows empty. [0:13–0:17] one slow continuous dolly in until the single remaining record fills the frame. [0:17–0:25] absolutely locked on the record, static, the numbers held. [0:25–0:30] pull focus off the screen onto her still face, lit from below; hold; cut on the record and her face.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, present throughout. Soft futon fabric as she shifts and opens the phone. The soft sound of a finger on glass, once, as the list opens. No spoken words at all — the record is read, not spoken. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as the camera closes on the record and entirely gone by the moment her face goes still, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep11-seg06-30s-01`
- Segment ID: `S51`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_11, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 11s / 8s / 5s. Remaining record = BEAT 2 at 11s (37%)`
- Camera Events: `5 events as listed in §10. One sustained dolly (0:13–0:17)`
- Action Events: `ACT_OPEN → ACT_READ_LIST → ACT_READ_RECORD → ACT_STILL`
- Audio Events: `no dialogue ／ clock ticking throughout ／ music gone by the stillness`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the record`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The record's three lines carry the evidence. If they render as noise the segment fails. Check first; if unusable, generate the screen as a plate and composite the text in post.
- **The record may read as dread, not return.** This is S02's record, but its meaning is now the opposite. If the tone tips cold or frightened, strip any sting and hold the stillness warmer.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.
- **The model may add a ghost.** "2 A.M." + "one remaining record" is a strong prior. The negative prompt front-loads this; verify frame by frame — no figure, no eyes, no rainbow.

## Changes

- _(none yet)_

## Next Generation

- If the record renders cleanly and lands as return, this is the last night-time record — S52 (the finale's first light) begins from it.
