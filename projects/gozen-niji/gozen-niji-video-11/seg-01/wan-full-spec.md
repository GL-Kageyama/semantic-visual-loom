# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第11話 S46「屋台の灯り」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「指を休ませる」——手は空（指の背骨の第46本）。画面も握るものもない。屋台の灯りの下の湊の背中と「今日で最後だ」という気づきだけに配る。ニジは不在（第11話に幽霊はいない）。登場人物は真白と湊のみ。画面文字なし。S47 の「声をかける」が効くのは、この1本で手を空にして湊の横に立つから。**

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

> **湊 appears this segment**（third-year 氷室湊 — festival committee, composed, carries document bundles）. ニジ is absent（ledger 46–51 — the ghost does not appear in this chapter）.

---

# 4. ENVIRONMENT

## Location

- ID: `FESTIVAL_YARD`
- Name: `文化祭の裏庭 (the festival back yard)`
- Description: `Back yard at night, paper lanterns, food-stall smoke and light — warm pools of lantern light floating in deep indigo night`

## Environmental Behavior

- Wind: `none — the curtain does not move`
- Particles: `only the faintest haze catching the screen's bloom; no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; at most one distant car's headlights crossing the curtain, once`

---

# 5. OBJECTS

## PHONE

- Type: `smartphone (湊's)`
- Appearance: `Dim and ordinary in 湊's hand, plain case, Japanese UI, its content unreadable. 真白 carries no phone this segment — her hands are empty and still`
- Narrative Importance: `LOW`
- Visual Importance: `LOW`
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

The last night of the culture festival. In the festival yard, 真白 finds 湊 alone under the paper lanterns, committee work done, looking at his phone. 今日で最後だ、と、真白は思う。 This is her last chance — and she steps toward him.

## Beginning

Night. The festival yard: paper lanterns warm in the dark, food-stall smoke drifting and vanishing, laughter from the stalls. 湊 alone, his work finished, phone in hand; the lantern light falls soft on his face.

## Turn

真白 sees him, and stops. 今日で最後だ、と、真白は思った。この文化祭が終わったら、明日からは、またいつも通りの学校。 The realization lands without a word.

## Peak

Her decision. She steps out of the dark toward 湊's back — her hand empty, no phone, nothing to hold. This is the thing she has not been able to do for a year.

## Pull（引き — 切れ目）

真白 stands beside him. Hand empty, the festival sound around them, the lantern light on both their faces. Cut before she opens her mouth — the word is left for S47.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The realization (今日で最後だ) holds 10s (33%); the approach is held 7s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「屋台の灯り」 — ESTABLISH.** Night festival yard. Paper lanterns warm in the dark air. Food-stall smoke drifts and vanishes; laughter from the stalls. 湊 alone, his back to camera, phone in hand, lantern light soft on his face. _Density: SPARSE — one quiet figure in a living crowd._
- **BEAT 2 `[0:07–0:17]` — 「今日で最後だ」 — TURN, longest share.** 真白, in the dark at the edge of the light, sees him and stops. 今日で最後だ、と、真白は思う。この文化祭が終わったら、明日からは、またいつも通りの学校。Her face does not resolve into anything; her hand is empty. _Density: SPARSE, internal — the event is a thought._
- **BEAT 3 `[0:17–0:24]` — 「近づく」 — PEAK.** She steps out of the dark toward 湊's back. Slowly, deliberately. The lantern light reaches her as she comes into it. _Density: TRANSITION — one sustained movement._
- **BEAT 4 `[0:24–0:30]` — 「横に立つ」.** 真白 stands beside him. Both faces in the lantern light. The festival sound around them. She has not spoken. Cut before the word. _Density: HELD — then a clean cut. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `真白 finding 湊 and stopping (≈0:08) ／ the thought 今日で最後だ (≈0:10) ／ her stepping toward him (≈0:18)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the yard), 0:07–0:17 (the held realization)`
- Dense regions: `0:17–0:24 (the approach)`
- Long continuous action: `0:17–0:24 the step out of the dark`
- Rapid transitions: `none — a slow, warm night`

---

# 9. ACTION

## Action — ACT_SEE

- ID: `ACT_SEE`
- Subject: `MASHIRO`
- Action: `Stops at the edge of the lantern light and sees 湊, alone, phone in hand`
- Intention: `Not to spy — to find him. She has come looking, whether she knows it or not`
- Intensity: `Low`
- Speed: `Nothing. A held gaze`

### Action Relationship

- Before: `—`
- After: `ACT_REALIZE`

## Action — ACT_REALIZE

- ID: `ACT_REALIZE`
- Subject: `MASHIRO`
- Action: `Takes in that this is the last night. 今日で最後だ。Her hand stays empty at her side`
- Intention: `To let the fact settle before she moves`
- Intensity: `Medium, internal`
- Speed: `Still`

### Action Relationship

- Before: `ACT_SEE`
- After: `ACT_APPROACH`

## Action — ACT_APPROACH

- ID: `ACT_APPROACH`
- Subject: `MASHIRO`
- Action: `Steps out of the dark toward 湊's back, slowly, deliberately`
- Intention: `To stand beside him. This is the thing she could not do for a year`
- Intensity: `Medium, internal`
- Speed: `Slow, steady — the only movement in the segment`

### Action Relationship

- Before: `ACT_REALIZE`
- After: `ACT_STAND`

## Action — ACT_STAND

- ID: `ACT_STAND`
- Subject: `MASHIRO`
- Action: `Stands beside 湊, hand empty, and does not speak`
- Intention: `To be there. The word is still ahead of her`
- Intensity: `Low`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_APPROACH`
- After: `— (cut before the word)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Level, at standing height, held back at first — then closing to a two-shot`
- Lens Character: `Long-ish, shallow. The crowd and stalls fall away soft behind`
- Depth of Field: `Shallow — 湊 sharp, the festival soft and glowing behind`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Wide-ish, static, at standing height: 湊's back under the lantern light, the stalls and smoke soft behind, the night alive around him.
- **`[0:07–0:13]`** — Cut to 真白 at the edge of the light, static, medium. Her face unreadable; the lanterns glow behind her in the dark.
- **`[0:13–0:17]`** — Hold on her, then a slow rack focus from her face out to 湊's back in the light beyond — the distance between them.
- **`[0:17–0:24]`** — One slow lateral drift as she steps into the light, following her toward 湊's back. The piece's single sustained move.
- **`[0:24–0:30]`** — Settle into a two-shot from the side: 湊 and 真白 side by side, lantern light on both. Static. Cut before the word.

---

# 11. MOTION

## Subject Motion

- 真白's body holds almost completely still until the approach — one slow, deliberate step out of the dark
- Her hands are empty and still at her sides; there is no phone to reach for
- 湊 barely moves — a slight shift of his weight, the faint motion of his thumb over the phone, then still

## Object Motion

- The phone in 湊's hand is dim and ordinary; it moves only as his thumb rests on it
- Paper lanterns sway very slightly; the smoke drifts and thins — no wind, only the breath of the crowd
- Nothing glitches, flickers, distorts, or behaves supernaturally

## Environmental Motion

- The festival is alive in soft, out-of-focus movement — distant figures, drifting smoke, lantern glow
- No wind, no moving shadows, no particles

## Physical Characteristics

- Weight: `Ordinary. The two of them stand with ordinary weight on the ground`
- Inertia: `High for both bodies; near-zero movement throughout`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by one slow, deliberate movement`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Ordinary festival night (the yard, warm and unbothered)
- ↓ Recognition (she has found him, and this is the last night)
- ↓ Decision (the step she could not take for a year)
- ↓ Stillness (standing beside him, before the word)

## Emotional Events

- Event: `真白 finds 湊 alone and stops` — Emotion: `Recognition, not surprise` — Intensity: `MEDIUM, internal` — Timing: `≈0:08`
- Event: `今日で最後だ` — Emotion: `The last chance settling in — quiet, not dramatic` — Intensity: `MEDIUM, entirely internal` — Timing: `≈0:12`
- Event: `She steps out of the dark toward him` — Emotion: `Decision — the body moving before the courage has finished arriving` — Intensity: `MEDIUM` — Timing: `0:17–0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Warm paper-lantern glow — amber, soft, low-saturation. The festival is the one warm place in the series`
- Fill Light: `Soft, even. The lanterns and stall lights fill the yard; the night air beyond is deep indigo`
- Rim Light: `A faint warm edge on 湊's hair and shoulder from the nearest lantern`
- Ambient Light: `Deep indigo night, with warm pools of lantern light floating in it`
- Color Temperature: `≈2900K lantern light against deep indigo night — warm, but kept muted, never saturated`

## Lighting Events

- **`[0:00]`** — The yard already lit — warm lanterns, drifting smoke catching the glow.
- **`[0:07–0:17]`** — 真白 stands at the edge of the light: her face half in dark, half in the faint amber spill. The light does not reach her eyes.
- **`[0:17–0:24]`** — As she steps forward, the lantern light crosses her face and lands fully on it — the moment she enters the warm.
- **`[0:24–0:30]`** — Both faces lit softly by the lanterns, warm and even. Cut.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. 真白's thought (今日で最後だ) is not voiced. No narration, no voice-over.

## Sound Effects

- A night festival, soft and continuous — distant laughter, stall voices, the sizzle of food, paper lanterns creaking faintly
- The warm murmur of a crowd, far enough to be a texture, not a scene

## Environment

- Open night air, full and ordinary. The world is warm, alive, and unbothered

## Music

- Style: `Sparse — a few sustained tones, or nothing`
- Tempo: `Slow`
- Mood: `Warm, gentle, suspended. Never sinister, never sentimental`
- Emotional Function: `Hold the warmth of the night under her decision. It thins as she steps toward 湊, leaving only the crowd murmur and the lanterns`

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

- Establish 湊 alone under the lantern light — his back, his calm, the committee work just finished
- Show 真白's hands empty and still; there is no phone in this segment for her
- Keep the festival light warm but muted, never saturated — the palette law holds even here
- End on the two of them side by side, cut before she opens her mouth

## MUST NOT（この1本の禁止・開示台帳 46–51 レンジより）

- **ニジは登場しない。** No ghost, no figure, no silhouette, no reflection, no second person, no eyes, no hand but the two living people's own. This episode has no ニジ at all
- **No rainbow, no iridescence, no colored afterimage**
- **No on-screen text.** There is no phone screen to read; the night is the surface
- Do not make 湊 sinister, menacing, or knowing — he is composed and ordinary
- Do not give this night horror grammar — no dread, no cold, no sense of being watched
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- 湊's back over his face in the opening — the distance 真白 has watched from
- Silence over score at the approach
- Negative space over detail; the crowd may be soft shapes in the dark

## ALLOW

- Slight variation in lantern pattern, stall arrangement, crowd shapes
- The lateral drift of beat 3 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not appear (ledger 46–51 — the ghost does not appear in this chapter); only 真白 and 湊. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a night culture festival in a school back yard. Beats, deliberately uneven: [0:00–0:07] 湊 (Minato), a composed third-year boy, stands alone under warm paper lanterns, committee work done, phone dim in his hand, food-stall smoke drifting and vanishing, distant laughter; [0:07–0:17] 真白, at the edge of the light, sees him and stops, thinking 今日で最後だ、この文化祭が終わったら明日からはまたいつも通りの学校, her hands empty and still; [0:17–0:24] she steps out of the dark toward his back, slowly, the lantern light crossing her face; [0:24–0:30] she stands beside him, the two of them side by side in the warm light, and the shot cuts before she opens her mouth. The realization holds the largest share of the duration. Ends on the stillness before the word, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. She wears her standard Japanese school uniform; her hands are empty. Scene: a school festival back yard at night — paper lanterns glowing warm and soft, food-stall smoke drifting, the dark night air indigo around it all. Beside the light, 湊 (Minato) — a third-year boy, festival committee, composed and quiet, short neat dark hair, in the boys' school uniform, a little taller, with a calm face. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Bodies hold almost completely still; almost nothing moves except 真白's one slow, deliberate step out of the dark toward 湊. Her hands are empty and still at her sides. 湊 barely moves — a slight shift of weight, his thumb resting on a dim phone. Paper lanterns sway very slightly; the smoke drifts and thins. The festival crowd is alive only in soft, out-of-focus movement. The phone in 湊's hand is dim and ordinary, never glitching, flickering or distorting. Gentle acceleration everywhere. No wind, no moving shadows, no particles, no impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Level, at standing height, held back at first, then closing to a two-shot. Longish lens, shallow depth of field; 湊 sharp, the festival soft and glowing behind. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] wide-ish and static on 湊's back under the lantern light. [0:07–0:13] cut to 真白 at the edge of the light, static, medium; her face unreadable. [0:13–0:17] a slow rack focus from her face out to 湊's back in the light beyond. [0:17–0:24] one slow lateral drift following her into the light. [0:24–0:30] settle into a two-shot from the side, both in the lantern light; cut before the word.

## Audio Prompt

No speech at all — this segment is wordless; the thought is not voiced. Open night air, warm and full: a soft continuous festival — distant laughter, stall voices, the sizzle of food, paper lanterns creaking faintly, the murmur of a crowd far enough to be a texture. No narration, no voice-over. Music extremely sparse — a few sustained tones at most, warm and gentle — thinning as she steps toward 湊, leaving only the crowd murmur and the lanterns. No horror strings, no sting, no swelling emotion, no coldness.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep11-seg01-30s-01`
- Segment ID: `S46`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_11, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 10s / 7s / 6s. Realization = BEAT 2 at 10s (33%)`
- Camera Events: `5 events as listed in §10. One lateral drift (0:17–0:24)`
- Action Events: `ACT_SEE → ACT_REALIZE → ACT_APPROACH → ACT_STAND`
- Audio Events: `no dialogue ／ warm festival ambience ／ sparse music thinning`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut before the word`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The festival may read as warm-and-saturated instead of muted.** The palette law is strict — the lanterns are amber but low-saturation. If it goes full carnival orange, pull the saturation down.
- **湊 may read as sinister.** A lone boy under lanterns + a girl watching from the dark is a horror trope. He must be calm and ordinary; the night must be warm, not threatening.
- **The model may add a ghost.** The negative prompt front-loads this; verify frame by frame — no figure, no eyes, no rainbow.
- **Her empty hands may read as missing something.** The absence of the phone is the point (45 segments of phone, now nothing). If the model puts a phone in her hand, re-issue — it is the one thing this segment forbids.

## Changes

- _(none yet)_

## Next Generation

- If the stillness reads, S47 (the word 声をかける) depends on this segment establishing that 真白 has stood beside him with empty hands.
