# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第7話 S28「全部開く」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**設定→スクリーンタイム→宛先リストを、全部開く指。S27 が「開けなかった一日」を刻み、この1本で指はその反転を演じる——一画面も飛ばさず、次へ次へと全部を開いていく。ニジは不在（日中・教室）。画面の文字はなし（普通の UI のみ）。**

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

- ID: `CLASSROOM`
- Name: `教室 (the darkened classroom, after school)`
- Description: `放課後. The classroom after the festival eve — 真白 alone at her seat, origami scraps on the desk. Near-black; the phone screen is now the room's only light`

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
- Appearance: `No message text this segment — only ordinary settings UI (設定, スクリーンタイム, アプリごとの使用時間, 宛先リスト, 預けた時間の一覧) opened in sequence. Rendered as ordinary phone UI, not as evidence; no captions, no subtitles`
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

放課後. 真白 stays at her seat, opens her phone, and opens 設定 → スクリーンタイム → 宛先リスト — every single one, without skipping any.

## Beginning

The classroom is dark (at the end of S27 one light went out). Only 真白 remains at her seat. On the desk, origami scraps. She opens her phone.

## Turn

設定. スクリーンタイム. アプリごとの使用時間. 宛先リスト. 預けた時間の一覧. ——それらを、ひとつ残らず、全部。 The finger skips no screen, opening the next, and the next.

## Peak

The finger does not stop. 宛先リスト. 預けた時間の一覧. 真白 closes nothing — she opened everything. The finger that rested all day now opens everything at once.

## Pull（引き — 切れ目）

The last screen — the list of deposited time — opens. The finger still rests on the screen. Cut on the full list, just opened, before she reads what is in it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The opening sequence holds 11s (37%) to engrave the finger's journey.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「放課後」 — ESTABLISH.** The darkened classroom; only 真白 remains at her seat; origami scraps on the desk; she opens the phone — the screen's light becoming the room's only light. _Density: SPARSE — one deliberate act, and its half-beat of alone-ness._
- **BEAT 2 `[0:06–0:17]` — 「全部開く」 — longest share.** 設定. スクリーンタイム. アプリごとの使用時間. 宛先リスト. 預けた時間の一覧. The finger skips no screen, opening the next, and the next. _Density: DENSE — a chain of openings, each one unhurried._
- **BEAT 3 `[0:17–0:25]` — 「止まらない」 — the finger, unstopping.** The finger does not stop; 真白 closes nothing, having opened everything; the finger that rested all day now opens everything at once. _Density: SPARSE, inverted — the event is the absence of stopping._
- **BEAT 4 `[0:25–0:30]` — 「一覧」 — held, then cut.** The last screen — the list of deposited time — opens; the finger still rests on the glass. Cut on the list. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the screen becoming the only light (≈0:05) ／ the chain of openings (0:06–0:17) ／ the list appearing (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:06 (放課後), 0:17–0:25 (the unstopping finger)`
- Dense regions: `0:06–0:17 (the chain of openings)`
- Long continuous action: `0:06–0:17 the finger opening screen after screen`
- Rapid transitions: `none — a slow, deliberate evening`

---

# 9. ACTION

## Action — ACT_ALONE

- ID: `ACT_ALONE`
- Subject: `MASHIRO`
- Action: `Alone in the darkened classroom, at her seat, opens the phone — the screen's light becoming the only light`
- Intention: `To look — after a day of not looking`
- Intensity: `Low`
- Speed: `Slow, ordinary`

### Action Relationship

- Before: `— (continues from S27's darkened classroom)`
- After: `ACT_OPEN`

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MASHIRO`
- Action: `Opens 設定, then スクリーンタイム, then アプリごとの使用時間, then 宛先リスト, then 預けた時間の一覧 — one after another, skipping nothing`
- Intention: `To open everything — ひとつ残らず、全部`
- Intensity: `Medium, deliberate`
- Speed: `Steady, unhurried — a chain, not a rush`

### Action Relationship

- Before: `ACT_ALONE`
- After: `ACT_ALL`

## Action — ACT_ALL

- ID: `ACT_ALL`
- Subject: `MASHIRO`
- Action: `Keeps going — 宛先リスト, 預けた時間の一覧 — until everything is open, nothing closed`
- Intention: `Not to skip — every single one`
- Intensity: `Medium`
- Speed: `Steady; the finger does not stop`

### Action Relationship

- Before: `ACT_OPEN`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `MASHIRO`
- Action: `The last screen — the list of deposited time — is open; the finger rests on the glass, not yet reading`
- Intention: `None — the opening is done, the looking has not begun`
- Intensity: `Low`
- Speed: `Still`

### Action Relationship

- Before: `ACT_ALL`
- After: `— (cut on the list)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, at desk height. Inside the dark classroom with her`
- Lens Character: `Long-ish, shallow. Only the screen or her hand are ever sharp`
- Depth of Field: `Very shallow — the classroom falls away into near-black`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:05]`** — Low static wide of the darkened classroom, 真白 at her seat. The phone lights; its cold blue-white fills the frame.
- **`[0:05–0:12]`** — Close on the screen and her thumb — 設定, then スクリーンタイム, the finger tapping through, unhurried.
- **`[0:12–0:17]`** — A slow push-in as the finger reaches 宛先リスト, then 預けた時間の一覧 — the chain of openings, one sustained move.
- **`[0:17–0:25]`** — Cut to her face, lit from below by the screen, the finger still moving in the foreground. She does not look away.
- **`[0:25–0:30]`** — Cut to the screen: the list of deposited time, open and held. Cut on the list.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially all the movement; the rest of her body holds
- The opening is a chain — steady, unhurried, skipping nothing; the finger never stops
- Her face is still, lit from below; only her eyes move, following the screens

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — menus opening, one after another. Nothing glitches, flickers, or distorts
- The screen's light is now the room's only light; its bloom breathes very slightly

## Environmental Motion

- The classroom is still and dark; nothing moves in it
- No wind, no moving shadows, no particles

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand`
- Inertia: `High for her body, near-zero for the finger`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Alone-ness (the darkened classroom, the day done)
- ↓ Deliberation (the chain of openings, nothing skipped)
- ↓ Unstoppability (the finger that will not stop, opening everything)
- ↓ Anticipation (the list, open and held — not yet read)

## Emotional Events

- Event: `The phone becomes the room's only light` — Emotion: `Alone-ness — the day done, the eve settling` — Intensity: `LOW` — Timing: `≈0:05`
- Event: `The finger opens screen after screen without stopping` — Emotion: `Deliberation — ひとつ残らず、全部` — Intensity: `MEDIUM` — Timing: `0:06–0:17`
- Event: `The list of deposited time opens` — Emotion: `Anticipation — the looking has not yet begun` — Intensity: `MEDIUM, held` — Timing: `≈0:27`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft darkness fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `Near-black. The classroom is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against near-black. No change through the segment`

## Lighting Events

- **`[0:00]`** — The classroom is near-dark; the phone lights and its bloom expands into the dark frame before the phone itself is sharp.
- **`[0:05–0:17]`** — As the camera closes on the screen, its light dominates the frame; her face falls almost to silhouette.
- **`[0:17–0:25]`** — Her face is lit from below, almost to silhouette, the knuckles bright.
- **`[0:30]`** — Cut on the list. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. No narration, no voice-over.

## Sound Effects

- The soft friction of a thumb on glass, close and continuous — its rhythm the segment's pulse
- The quiet of an emptied school: a distant door, a hallway voice far off, then nothing
- The screen's soft taps as each menu opens — 設定, スクリーンタイム, 宛先リスト

## Environment

- Evening. Near-silence — the kind of quiet an emptied classroom holds after the festival eve

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, deliberate. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the finger's chain of openings. It may thin toward the close, leaving only the thumb on glass`

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

- Show the finger opening 設定 → スクリーンタイム → アプリごとの使用時間 → 宛先リスト → 預けた時間の一覧, one after another, skipping nothing
- Make the phone screen the room's only light source — the day is done, the classroom is dark
- Keep the opening steady and unhurried — a chain, not a rush
- End on the list of deposited time, open and held — cut on the list, before she reads it

## MUST NOT（この1本の禁止・開示台帳 27–28 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person, no eyes, no hand but her own. ニジ is absent
- **No rainbow, no iridescence, no colored afterimage**
- No 美月, no 小春, no 湊 — no named character but 真白
- No story-critical on-screen text — the menus are ordinary UI, not evidence; no captions, no subtitles
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The chain of openings over any single screen — the finger's journey is the content
- Silence over score
- Negative space over detail; the classroom may be nearly empty

## ALLOW

- Slight variation in the settings-UI layout and the classroom furnishing
- The push-in may be omitted (a fully locked frame is equally correct)
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

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school girl alone in her darkened classroom after school. Beats, deliberately uneven: [0:00–0:06] she sits alone at her seat, origami scraps on the desk, and opens her phone — its light becoming the room's only light; [0:06–0:17] her finger opens 設定, then スクリーンタイム, then アプリごとの使用時間, then 宛先リスト, then 預けた時間の一覧, one after another, skipping nothing — ひとつ残らず、全部; [0:17–0:25] the finger does not stop, she closes nothing, having opened everything at once; [0:25–0:30] the last screen — the list of deposited time — is open and held, and the shot cuts on the list, before she reads what is in it. The chain of openings holds the largest share. Ends on the list, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. By day she wears a standard Japanese school uniform; here, after school, she is alone in the classroom in that uniform. A darkened classroom: the phone screen is now the only light, cold blue-white from below her face, her face nearly silhouetted, shadows deep and soft, no fill. The screen shows an ordinary Japanese settings UI in cold blue-white. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the finger; the body holds still. The finger opens screen after screen — 設定, スクリーンタイム, 宛先リスト — in a steady, unhurried chain, skipping nothing, never stopping. Ordinary weight and inertia: the phone has heft in her hand. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. Only the screen's bloom breathes faintly in the dark. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, at desk height — inside the dark classroom with her. Longish lens, very shallow depth of field; only the screen or her hand are ever sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:05] low static wide of the darkened classroom, 真白 at her seat, the phone lighting. [0:05–0:12] close on the screen and her thumb, the finger tapping through 設定 then スクリーンタイム, unhurried. [0:12–0:17] a slow push-in as the finger reaches 宛先リスト then 預けた時間の一覧. [0:17–0:25] cut to her face lit from below, the finger still moving in the foreground. [0:25–0:30] cut to the screen, the list of deposited time open and held; cut on the list.

## Audio Prompt

Evening. Near-silence — the quiet of an emptied classroom after the festival eve. The close continuous friction of a thumb on glass, its rhythm the segment's pulse. The soft taps of each menu opening. A distant door, a hallway voice far off, then nothing. No spoken words at all — no dialogue, no narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only the thumb on glass. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep07-seg02-30s-01`
- Segment ID: `S28`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_07, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 11s / 8s / 5s. Opening chain = BEAT 2 at 11s (37%)`
- Camera Events: `5 events as listed in §10. One slow push-in (0:12–0:17)`
- Action Events: `ACT_ALONE → ACT_OPEN → ACT_ALL → ACT_HOLD`
- Audio Events: `no dialogue ／ thumb-on-glass throughout ／ music thinning to the taps`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the list`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The chain of openings may read as a montage, not a gesture.** The point is one finger moving through screens. If it reads as jump-cuts, hold the close on the thumb and let the screens pass under it.
- **The model may add a ghost.** The dark classroom + a girl alone at night is a strong prior. The negative prompt front-loads the no-ghost clause; verify frame by frame — no figure, no eyes, no rainbow.
- **The UI may render as readable story text.** The menus are not evidence — they must stay ordinary, out-of-focus UI. If they render as bold readable labels, they draw focus from the finger.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the finger's journey reads as one deliberate gesture and the list lands as the hook, the segment is done; S29 opens that same list and reads it for the first time.
