# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第4話 S14「触ったら負け」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「触ったら負け」の確立——触らないと決めた手が、伏せたスマホへ伸びて机の上を探し、引き戻す、撤退の所作。ニジは不在（記録＝伏せたスマホとしてのみ）。登場人物は真白のみ。画面文字なし。画面を下に向けた黒いスマホの背中が机の上で妙に目立つ。この1本から第4話は逆方向へ折れる。**

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

> **ニジ is absent this segment**（ledger 14–15 — the ghost exists only as a record, the face-down phone）. No other character appears.

---

# 4. ENVIRONMENT

## Location

- ID: `BEDROOM`
- Name: `真白の部屋 (her bedroom)`
- Description: `Small, futon on the floor, curtained window, wall clock, desk, few objects. Pale muted daylight through the curtain — the room lit by the world, not the phone. The recurring stage — most night takes live here`

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
- Appearance: `No screen text this segment — the phone lies face-down, its screen hidden and dark. No UI, no glow, no text`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
- Continuity Importance: `HIGH`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Out of focus behind — close and unhurried, the "clock in her chest" made audible`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_04_現実を生きるほど、増える.md`
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

一週間、真白はスマホを置いた。机の上に、伏せて——画面が上を向かないように。触ったら負け、と決めて。The gesture the whole series has been building toward now turns against itself: the hand that has never stopped reaching now must be pulled back, empty.

## Beginning

The phone lies face-down on the desk. Screen turned to the wood. Its black back is conspicuously there — 妙に目立ってた. A week of this, and the rule she set against herself: 触ったら負け。

## Turn

Her hand — empty, unoccupied, of its own habit — reaches toward the face-down phone. Her fingers search the desk, find nothing to hold. 胸の中で時計が鳴ってた。 The body does not know the phone is gone from her hand.

## Peak

The face-down phone vibrates once. A thin red glow seeps from beneath its edge — a notification, an いいね stacking up, unseen. 真白は見なかった。見ない、と決めたから。

## Pull（引き — 切れ目）

Her hand hangs over the phone, then withdraws to her side. 触ったら負け holds. Cut on the face-down phone, its black back conspicuous on the desk, the red glow still faint beneath the edge. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The searching hand holds 12s (40%) to engrave the withdrawal.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the bedroom; the searching hand is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「伏せる」 — ESTABLISH.** Pale daylight in the small room. The phone lies face-down on the desk, its black back conspicuous. A week of this. 触ったら負け. _Density: SPARSE — a still room, one rule forming._
- **BEAT 2 `[0:07–0:19]` — 「探す」 — the gesture, longest share.** Her empty hand reaches toward the face-down phone, then her fingers search the desk, finding nothing to hold. The body remembers the phone. _Density: SPARSE, continuous — the withdrawal-in-motion, held._
- **BEAT 3 `[0:19–0:26]` — 「震える」.** The face-down phone vibrates once; a thin red glow seeps from beneath its edge — a notification she will not look at. Her face does not turn. _Density: TRANSITION — one small event, ignored._
- **BEAT 4 `[0:26–0:30]` — 「負けない」.** Her hand withdraws to her side. 触ったら負け holds. Cut on the face-down phone. The red glow still faint beneath the edge. _Density: HELD — then a clean cut. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the hand reaching and searching (0:07–0:19) ／ the vibration and the red glow (≈0:20) ／ the hand withdrawing (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the face-down phone), 0:07–0:19 (the searching hand)`
- Dense regions: `0:19–0:26 (the vibration and the red glow)`
- Long continuous action: `0:07–0:19 the hand searching the desk`
- Rapid transitions: `none — a held, still segment of withdrawal`

---

# 9. ACTION

## Action — ACT_RESOLVE

- ID: `ACT_RESOLVE`
- Subject: `MASHIRO`
- Action: `Sits at the desk before the face-down phone; the rule forms — 触ったら負け`
- Intention: `To not touch it. To make the record go away by never opening the phone`
- Intensity: `Low`
- Speed: `Still`

### Action Relationship

- Before: `— (continues from S13's night)`
- After: `ACT_REACH`

## Action — ACT_REACH

- ID: `ACT_REACH`
- Subject: `MASHIRO`
- Action: `Her empty hand reaches toward the face-down phone, then her fingers search the desk, finding nothing`
- Intention: `Not choice — habit. The body reaching for what it has removed`
- Intensity: `Medium, internal`
- Speed: `Slow, then searching, uncertain`

### Action Relationship

- Before: `ACT_RESOLVE`
- After: `ACT_REFUSE`

## Action — ACT_REFUSE

- ID: `ACT_REFUSE`
- Subject: `MASHIRO`
- Action: `The phone vibrates once; she does not look. Her face does not turn`
- Intention: `見ない、と決めたから — to keep the rule`
- Intensity: `Medium, suppressed`
- Speed: `A near-still refusal, held`

### Action Relationship

- Before: `ACT_REACH`
- After: `ACT_WITHDRAW`

## Action — ACT_WITHDRAW

- ID: `ACT_WITHDRAW`
- Subject: `MASHIRO`
- Action: `Her hand hangs over the phone, then withdraws to her side`
- Intention: `触ったら負け — to win by not touching`
- Intensity: `Low`
- Speed: `Slow, ordinary`

### Action Relationship

- Before: `ACT_REFUSE`
- After: `— (cut on the face-down phone)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, at desk height. Across the desk at the face-down phone`
- Lens Character: `Long-ish, shallow. Only the phone's black back or her hand are ever sharp`
- Depth of Field: `Shallow — the room falls away to pale daylight`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Locked on the face-down phone on the desk, its black back filling the frame. The room's pale daylight lies still around it. Optional: an imperceptibly slow push-in.
- **`[0:07–0:13]`** — Her hand enters frame from the side, reaching toward the phone. The camera stays on the hand and the phone together.
- **`[0:13–0:19]`** — The hand searches the desk surface — fingers patting the wood, finding nothing. Macro-close on the fingertips, the empty space.
- **`[0:19–0:26]`** — Hold on the face-down phone as it vibrates once; a thin red glow seeps from beneath its edge onto the wood. Her face stays out of frame, or averted at the edge.
- **`[0:26–0:30]`** — The hand withdraws, leaving the phone alone. Cut on the face-down phone, the red glow still faint beneath the edge.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially all the movement; the rest of her body holds
- The reach and the search are unsteady, hesitant — not the practiced mechanical stroke of S01, but a hand that no longer knows its job
- The refusal is a held stillness: the phone vibrates, and she does not move
- The withdrawal is slow, ordinary — the hand leaving the desk empty

## Object Motion

- The phone does not move on its own except to vibrate once, in place, against the desk
- Its screen stays dark and hidden — face-down. Only the red glow from beneath the edge shows that anything arrived
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Environmental Motion

- Pale daylight is still. The curtain does not move
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the desk bears its weight`
- Inertia: `High for her body, hesitant for her hand — no longer the practiced instant of S01`
- Acceleration: `Gentle everywhere; the vibration is the only sudden thing`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes. The segment's only event is a hand that does not land`

---

# 12. EMOTION

## Emotional Arc

- Quiet resolve (the rule: 触ったら負け)
- ↓ The body's habit fighting back (the reaching, searching hand)
- ↓ The test, refused (the vibration, not looking)
- ↓ Restraint that holds (the withdrawal; the rule survives one more day)

## Emotional Events

- Event: `The face-down phone, conspicuous on the desk` — Emotion: `Quiet resolve — a rule, not a feeling` — Intensity: `LOW` — Timing: `≈0:04`
- Event: `The hand reaches and searches, finding nothing` — Emotion: `Withdrawal — the body reaching for what it has removed` — Intensity: `MEDIUM, entirely internal` — Timing: `0:07–0:19`
- Event: `The phone vibrates; she does not look` — Emotion: `Refusal, held` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:20`
- Event: `The hand withdraws` — Emotion: `Restraint that holds` — Intensity: `LOW` — Timing: `≈0:27`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Pale muted daylight through the curtain — the room is lit, for once, by the world and not the phone`
- Fill Light: `Soft and even. The room is dim but legible in the day's flat light`
- Rim Light: `A faint cool edge on the phone's black back where the daylight grazes it`
- Ambient Light: `Day. Muted, low-saturation, slightly overexposed`
- Color Temperature: `≈5600K pale daylight. The phone's screen is off — for the first beat in the series, there is no blue-white glow`

## Lighting Events

- **`[0:00]`** — Day already full. The phone's black back catches a thin highlight where the daylight grazes it.
- **`[0:19–0:26]`** — The phone vibrates; a thin red glow seeps from beneath its edge and lies as a narrow red line on the desk wood. The only color in the room, and she does not look at it.
- **`[0:26–0:30]`** — The red glow remains, faint, as the hand withdraws. Cut on the face-down phone. No flash, no dim — just the cut.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The rule 触ったら負け is internal — it is not spoken, not whispered, not narrated.

## Sound Effects

- The dry discrete ticking of the wall clock, close and unhurried — the "clock in her chest" made audible
- The soft hush of fingertips searching the desk wood, brief and uncertain
- One short vibration of the phone against the desk — a single buzz, then nothing
- The room's quiet daylight hush

## Environment

- Quiet day room tone, almost nothing. The kind of silence in which a phone vibrating once is very loud

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, muted. Never sinister, never sentimental`
- Emotional Function: `Hold the room's daytime stillness under the searching hand. It may thin toward the close, leaving only room tone and the clock`

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

- Render the phone face-down, its screen hidden and dark — no screen content, no UI, no text
- Let the hand reach toward the face-down phone and search the desk, finding nothing, and hold it longer than is comfortable
- Show the single vibration and the thin red glow seeping from beneath the phone's edge — the only notification, and she does not look
- End by cutting on the face-down phone, its black back conspicuous, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 14–15 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person, no eyes, no hand but her own. ニジ does not appear in this beat — only the record (the face-down phone)
- **No rainbow, no iridescence, no colored afterimage**
- No on-screen text, no UI, no screen glow — the phone is face-down and dark
- Do not have 真白 touch the phone, turn it over, or look at the notification

## PREFER

- The empty-handed searching held as long as possible — the whole segment is one withheld gesture
- Silence over score
- Negative space over detail; the desk may be nearly empty

## ALLOW

- Slight variation in the wall-clock design, desk surface, room furnishing
- The imperceptible push-in during beat 1 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not be shown (ledger 14–15 — the ghost exists only as a record, the face-down phone); no second character. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school girl alone in her small bedroom in pale daylight. Beats, deliberately uneven: [0:00–0:07] the phone lies face-down on the desk, screen hidden, its black back conspicuous, and she has resolved 触ったら負け; [0:07–0:19] her empty hand reaches toward the face-down phone and her fingers search the desk, finding nothing to hold — the body remembering the phone it has removed; [0:19–0:26] the face-down phone vibrates once and a thin red glow seeps from beneath its edge, and she does not look; [0:26–0:30] her hand withdraws to her side, and the shot cuts on the face-down phone, the red glow still faint beneath the edge. The searching hand holds the largest share of the duration. Ends on the face-down phone, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. In this beat it is day — pale muted daylight through the curtain, slightly overexposed — and the phone lies face-down on the desk, its screen hidden and dark, no glow, no text. Only a thin red notification glow may seep from beneath the phone's edge. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to one hand; the body holds still. Her empty hand reaches toward the face-down phone, then her fingers search the desk, hesitant and unsteady, finding nothing — no longer the practiced mechanical stroke, but a hand that no longer knows its job. The phone vibrates once, in place, against the desk; its screen stays dark and hidden, only a thin red glow seeping from beneath the edge. She does not move; her face does not turn. Her hand withdraws slowly to her side. The wall clock's second hand advances in discrete ticks. Gentle acceleration everywhere; the vibration is the only sudden thing. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, at desk height — across the desk at the face-down phone. Longish lens, shallow depth of field; only the phone's black back or her hand are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] locked on the face-down phone, its black back filling the frame, optionally an imperceptibly slow push-in. [0:07–0:13] her hand enters frame from the side, reaching toward the phone. [0:13–0:19] macro-close on the fingertips searching the desk wood, finding nothing. [0:19–0:26] hold on the face-down phone as it vibrates once, a thin red glow seeping from beneath its edge; her face stays averted. [0:26–0:30] the hand withdraws, leaving the phone alone; cut on the face-down phone.

## Audio Prompt

Almost silent. Quiet day room tone. The dry discrete ticking of a wall clock, close and unhurried — the "clock in her chest" made audible. The soft hush of fingertips searching the desk wood, brief and uncertain. One short vibration of the phone against the desk — a single buzz, then nothing. No spoken words at all — the rule 触ったら負け is internal, not spoken, not narrated. No voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep04-seg01-30s-01`
- Segment ID: `S14`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_04, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 12s / 7s / 4s. Search = BEAT 2 at 12s (40%)`
- Camera Events: `5 events as listed in §10. No sustained dolly; all static or drift`
- Action Events: `ACT_RESOLVE → ACT_REACH → ACT_REFUSE → ACT_WITHDRAW`
- Audio Events: `no dialogue ／ wall clock throughout ／ one vibration against the desk`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the face-down phone`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The daylight may read as a lighting error.** The series is a night piece; this beat is deliberately day. If the pale daylight reads as "wrong," keep the phone's black back as the anchor — it must still be the focal point.
- **The searching hand may look random.** A generated hand may pat the desk without intent. The point is withdrawal — if it reads random, tighten the framing on the fingertips and the empty space.
- **The model may add a ghost.** "A phone she won't touch" is a light horror prior. The negative prompt front-loads this; verify frame by frame.
- **The red glow may be missed or exaggerated.** It is one thin line, not a flare. If it reads as VFX, cut it — the vibration alone is enough.

## Changes

- _(none yet)_

## Next Generation

- If the withdrawal reads cleanly, the hand's hesitation here becomes the seed of S16, where the phone lights up on its own.
