# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第6話 S24「一番上の名前」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「湊の名前の上で長く止まる」——流れていたリストが一番上で止まり、止まりへ反転する。最大の秒は「4時間52分」という数字の開示。憧れを「好き」と語らず、数字と「見てる」の二重性に押し込む。ニジは在・不透明・にやっとする（台帳 22–25）。湊は名前と数字だけ。**

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

## NIJI

- ID: `NIJI`
- Name: `ニジ (Niji)`
- Type: `CHARACTER (apparition, on-screen only)`
- Role: `The ghost of 2 A.M. — the crystallization of feelings 真白 never received`

### Appearance

- **真白's own face, one step younger** — longer lashes, slightly fuller cheeks. The same shoulder-length dark hair and thin neck; the same way of tilting her head.
- A blurred rainbow afterimage that resolves into that outline. Colors drift slowly: blue → green → blue.
- The outline is slightly blurred at the edges. **No shadow anywhere** — unlike 真白's solid, defined outline.
- Exists **inside the screen**. Never stands in the room at human scale.

### Behavior

- Personality: `Bright, teasing, unguarded — she smiles more honestly than 真白 can. She never cries. She calls 真白「おまえ」`
- Continuity: `her opacity is a strict function of the segment number (see the ledger); it never varies within a beat except in seg.55`

> **No other character appears this segment.** ニジ is present — fully opaque, inside the screen only, grinning and pointing (ledger 22–25: 在・不透明・リストを指す). 湊 stays a name and number only — no face, no figure (his body first appears in S26).

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
- Appearance: `A name and a number, rendered exactly character-for-character: 氷室湊……4時間52分. Cold blue-white on dark UI — the longest deposited time in the list`
- Narrative Importance: `HIGH`
- Visual Importance: `HIGH`
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

She looks at the top of the list. The name with the longest deposited time — 氷室湊. When ニジ places her finger on the screen, the number appears: 氷室湊……4時間52分. The longest in the list.

## Beginning

The flowing list stops at the top. 真白's eyes stop on that name. 氷室湊.

## Turn

「……湊先輩」. 「知ってるの？」. 「うん。……まあ、知ってる、っていうか。……見てる」. ニジ grins. 「おまえの、見てるは、――ずっと続いてる、見てるだったよ」. 湊——a senpai. An honors student. On the festival committee. The person 真白 had secretly watched.

## Peak

「どれだけ、預けてるの」. 「これだけ」. ニジ places her finger on the screen. The number appears:

氷室湊……4時間52分

――the longest in the list.

## Pull（引き — 切れ目）

「すごい、って、――なんか恥ずかしい」. 4時間52分 repeats itself in her head. Cut on the number, held on screen — the longest in the list.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The number reveal holds 10s (33%); the recognition holds 8s.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the bedroom; the number reveal is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「一番上の名前」.** The flowing list stops at the top. 真白's eyes stop on the name. 「……湊先輩」「知ってるの？」「……見てる」. _Density: TRANSITION — the flow stops; the name is recognized._
- **BEAT 2 `[0:07–0:15]` — 「ずっと続いてる、見てる」.** ニジ grins. 「おまえの、見てるは、――ずっと続いてる、見てるだったよ」. 湊——a senpai. An honors student. On the festival committee. The person she had secretly watched. _Density: DENSE — the tease; the name becomes a person._
- **BEAT 3 `[0:15–0:25]` — 「4時間52分」 — REVEAL, longest share.** 「どれだけ、預けてるの」「これだけ」. ニジ places her finger on the screen. The number appears: 氷室湊……4時間52分. ――the longest in the list. A slow dolly in until the number fills the frame. _Density: DENSE at the head (number → longest), then held._
- **BEAT 4 `[0:25–0:30]` — 「恥ずかしい」.** 真白 「すごい、って、――なんか恥ずかしい」. 4時間52分 repeats itself in her head. Cut on the number. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the list stopping on 湊's name (≈0:03) ／ the number appearing (≈0:17) ／ the number filling the frame (≈0:21)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the stop and recognition), 0:25–0:30 (the held pull)`
- Dense regions: `0:07–0:15 (the tease), 0:15–0:25 (the number reveal)`
- Long continuous action: `0:15–0:25 the number held on screen`
- Rapid transitions: `none — the stop and the number are the whole point`

---

# 9. ACTION

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `MASHIRO`
- Action: `The flowing list stops at the top; her finger holds long over the name 氷室湊`
- Intention: `None — the eye stops before the will does`
- Intensity: `Medium, internal`
- Speed: `A stop, then held`

### Action Relationship

- Before: `— (continues from S23's flow)`
- After: `ACT_RECOGNIZE`

## Action — ACT_RECOGNIZE

- ID: `ACT_RECOGNIZE`
- Subject: `MASHIRO`
- Action: `Speaks 「……湊先輩」, then 「……見てる」 — naming what she has been doing`
- Intention: `To name the person, and to half-admit the watching`
- Intensity: `Medium, suppressed`
- Speed: `Small, halting`

### Action Relationship

- Before: `ACT_STOP`
- After: `ACT_NIJI_TEASE`

## Action — ACT_NIJI_TEASE

- ID: `ACT_NIJI_TEASE`
- Subject: `NIJI`
- Action: `Grinning, teases 「おまえの、見てるは、――ずっと続いてる、見てるだったよ」 — inside the screen, fully opaque`
- Intention: `To see through 真白 — lightly, never cruelly`
- Intensity: `Low`
- Speed: `Playful, unguarded`

### Action Relationship

- Before: `ACT_RECOGNIZE`
- After: `ACT_REVEAL`

## Action — ACT_REVEAL

- ID: `ACT_REVEAL`
- Subject: `NIJI`
- Action: `Places her finger on the screen — 「これだけ」 — and the number appears: 氷室湊……4時間52分`
- Intention: `To show the amount`
- Intensity: `CRITICAL (the reveal, in a number)`
- Speed: `One touch, then the number`

### Action Relationship

- Before: `ACT_NIJI_TEASE`
- After: `ACT_EMBARRASSED`

## Action — ACT_EMBARRASSED

- ID: `ACT_EMBARRASSED`
- Subject: `MASHIRO`
- Action: `Speaks 「すごい、って、――なんか恥ずかしい」, eyes on the number, unable to move`
- Intention: `To deflect the magnitude`
- Intensity: `Medium, suppressed`
- Speed: `A murmur, then still`

### Action Relationship

- Before: `ACT_REVEAL`
- After: `— (cut on the number)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Only the screen or the finger are ever sharp`
- Depth of Field: `Very shallow — the room is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. One sustained dolly, and it belongs to the number`

## Camera Events

- **`[0:00–0:07]`** — Locked close on the screen as the list stops at the top. The name 氷室湊 sits at the head of the column. 真白's finger stills above it.
- **`[0:07–0:15]`** — Slight slow drift toward ニジ inside the screen, grinning, teasing. Then back to the name.
- **`[0:15–0:22]`** — One slow continuous dolly in on the name as ニジ's finger touches the screen — the number appears beneath it: 氷室湊……4時間52分. The segment's single sustained move.
- **`[0:22–0:25]`** — Absolutely locked on the number, filling the frame. Static.
- **`[0:25–0:30]`** — A slow pull back just enough to bring 真白's still face and the number into frame together. Cut on the number.

---

# 11. MOTION

## Subject Motion

- Her finger stops over 湊's name, then holds — the flow's reversal, and the emotional core
- 真白's body holds; her lips move faintly, halting, through the exchange
- ニジ, inside the screen, grins and points — fully opaque; her colors drift slowly blue → green → blue
- The reveal is ニジ's single touch; after it, only her colors move

## Object Motion

- The phone does not move on its own. Ever
- The list stops and the number appears by ordinary UI only — no glitch, no flicker, no supernatural transition
- The number, once on screen, does not move

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion in the room
- ニジ's rainbow, inside the screen, is the only saturated hue

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her finger — until the stop, which is held`
- Acceleration: `Gentle everywhere except the stop`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes. The only impact is a list ceasing to move`

---

# 12. EMOTION

## Emotional Arc

- Recognition (the name — 湊 — at the top)
- ↓ Exposure (the tease: her watching, seen through)
- ↓ The number (4時間52分 — the magnitude, landing)
- ↓ Embarrassment (すごい、って、なんか恥ずかしい — held)

## Emotional Events

- Event: `The list stops on 氷室湊` — Emotion: `Recognition — the person she has been searching for, unconsciously` — Intensity: `HIGH` — Timing: `≈0:03`
- Event: `ニジ's tease — ずっと続いてる、見てる` — Emotion: `Exposure, light and warm` — Intensity: `MEDIUM` — Timing: `≈0:10`
- Event: `The number appears — 氷室湊……4時間52分` — Emotion: `The magnitude, landing as a number, not a feeling` — Intensity: `CRITICAL — expressed only as a still finger` — Timing: `≈0:17, held to 0:25`
- Event: `すごい、って、なんか恥ずかしい` — Emotion: `Embarrassment, suppressed` — Intensity: `MEDIUM` — Timing: `≈0:27`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo; ニジ's rainbow is the only saturated hue, and it lives inside the screen`

## Lighting Events

- **`[0:00]`** — Screen already on; the list is steady and cold.
- **`[0:07–0:15]`** — ニジ's rainbow, inside the screen, is the only color not drowned in indigo.
- **`[0:15–0:22]`** — As the camera closes on the number, its light dominates the frame; her face falls almost to silhouette. The evidence outshines the person.
- **`[0:25–0:30]`** — The number fills the frame, cold blue-white. Cut on the number.

---

# 14. AUDIO

## Dialogue

- 真白: 「……湊先輩」 — small, halting
- ニジ: 「知ってるの？」 — light, curious
- 真白: 「うん。……まあ、知ってる、っていうか。……見てる」
- ニジ: 「見てる、ねえ」 — a grin in the voice
- ニジ: 「おまえの、見てるは、――ずっと続いてる、見てるだったよ」
- 真白: 「……続いてる、って、分かるの」
- ニジ: 「うん。――あの人の欄が、――毎日増えるんだもん」
- 真白: 「どれだけ、預けてるの」
- ニジ: 「これだけ」
- 真白: 「――ちょっと」
- ニジ: 「へへ。――おまえ、すごいね」
- 真白: 「すごい、って、――なんか恥ずかしい」

> The number is **not spoken.** It appears as text only. ニジ never says 「わたし」. No narration, no voice-over.

## Sound Effects

- The soft friction of a finger on glass, until the stop — then its **conspicuous absence**
- The wall clock's dry discrete ticking, faint throughout, growing louder in the held beats
- Soft futon fabric as she shifts, once

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, warm under the tease, then resolving into stillness. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness, then thin as the number appears — by the number there is only room tone, the finger's absence, and the clock`

---

# 15. CONTINUITY

> 57本は57回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

- **Identity**: 真白 — plain Japanese high-school girl 16–17, shoulder-length dark hair, thin neck, small frame, curved posture over a phone. Same face in every take.
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen.
- **The room**: futon on the floor, curtained window, wall clock, sparse.
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light.
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue.
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers.
- **(seg.10+) ニジ**: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same neck tilt and shoulder-length hair — a rainbow afterimage inside the screen, casting no shadow, at the opacity this segment requires.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。

## MUST

- Render the on-screen Japanese exactly, character-for-character: `氷室湊……4時間52分`
- Show the number as the reveal — the longest deposited time in the list, appearing under ニジ's touch
- Let the list stop on 湊's name, and hold the stopped finger long
- ニジ present, fully opaque, inside the screen only, grinning and pointing — 真白's own face one step younger, a rainbow afterimage
- 湊 stays a name and a number — no face, no figure, no cutaway to him
- End on the number held on screen, with 真白's embarrassment and nothing after it

## MUST NOT（この1本の禁止・開示台帳 22–25 レンジより）

- **ニジ must not be transparent or translucent.** In S22–25 she is fully opaque (不透明)
- **ニジ must not say わたし.** She calls 真白 「おまえ」 and never refers to herself in first person
- ニジ never leaves the screen — she never stands in the room at human scale
- No rainbow or iridescence anywhere except ニジ herself, inside the screen
- **Do not show 湊.** He is text only here — no face, no figure, no silhouette, no cutaway (his body first appears in S26)
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- Framing the number large, straight-on and held — legibility is the whole point
- The stopped finger over the face, for the reaction
- Silence over score at the number

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The list above the name may be slightly out of focus — only the number must read
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear fully opaque, inside the screen only (ledger 22–25 — 在・不透明・リストを指す), must not say わたし; 湊 must stay a name and number only (no face, no figure). This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:07] the flowing list stops at the top on a name — 氷室湊 — and 真白 speaks 湊先輩, 知ってるの？, ……見てる; [0:07–0:15] ニジ, inside the screen, grins and teases おまえの、見てるは、――ずっと続いてる、見てるだったよ, and 真白 answers 続いてる、って、分かるの, and ニジ あの人の欄が、――毎日増えるんだもん; [0:15–0:25] THE REVEAL — 真白 asks どれだけ、預けてるの, ニジ says これだけ and places her finger on the screen, and a number appears reading 氷室湊……4時間52分, and the camera closes slowly until the number fills the frame; [0:25–0:30] 真白 says すごい、って、――なんか恥ずかしい, and the shot cuts on the number. The reveal holds the largest share of the duration. Ends on the number, held, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. Night is deep indigo lit solely by the phone screen from below her face, her face nearly silhouetted, shadows soft and deep, no fill. The phone screen shows an ordinary Japanese UI in cold blue-white — a list with a name at the top and, beneath it, a number reading exactly 氷室湊……4時間52分. ニジ (Niji), inside the phone screen only, never in the room: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same head-tilt — a rainbow afterimage, fully opaque, no shadow, colors drifting slowly blue → green → blue, grinning and pointing at the name; her rainbow is the only saturated hue. 湊 does not appear as a person — only his name and number. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers. The flowing list stops at the top; her finger holds still over the name 氷室湊. ニジ, inside the screen, grins and points, fully opaque; her rainbow afterimage drifts slowly blue → green → blue. The reveal is ニジ's single touch, after which the number appears by ordinary UI only — no glitch, no flicker, no supernatural transition — and the number, once on screen, does not move. 真白's lips move faintly and haltingly through the exchange. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere except the stop. The phone never moves by itself. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; only the screen or the finger are sharp. Slow and deliberate, nearly still. [0:00–0:07] locked close on the screen as the list stops at the top, 真白's finger stilling above the name. [0:07–0:15] slight slow drift toward ニジ inside the screen, grinning, teasing; then back to the name. [0:15–0:22] one slow continuous dolly in on the name as ニジ's finger touches the screen and the number appears beneath it — the segment's single sustained move. [0:22–0:25] absolutely locked on the number, filling the frame, static. [0:25–0:30] a slow pull back to bring 真白's still face and the number into frame together; cut on the number.

## Audio Prompt

Deep quiet night room tone. The soft friction of a finger on glass — until the stop, then its conspicuous absence. The wall clock's dry discrete ticking, faint throughout, growing louder in the held beats. Soft futon fabric as she shifts once. Dialogue only, quick and halting: 真白 湊先輩, ニジ 知ってるの？, 真白 うん。……まあ、知ってる、っていうか。……見てる, ニジ 見てる、ねえ, ニジ おまえの、見てるは、――ずっと続いてる、見てるだったよ, 真白 続いてる、って、分かるの, ニジ あの人の欄が、――毎日増えるんだもん, 真白 どれだけ、預けてるの, ニジ これだけ, 真白 ――ちょっと, ニジ へへ。――おまえ、すごいね, 真白 すごい、って、――なんか恥ずかしい. The number is not spoken. ニジ never says わたし. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as the number appears, leaving only room tone, the finger's absence, and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparent figure, no translucent apparition, no see-through ghost, no ghost standing in the room at human scale, no figure outside the phone screen, no わたし spoken by ニジ, no rainbow or iridescence apart from ニジ herself, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep06-seg03-30s-01`
- Segment ID: `S24`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_06, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 8s / 10s / 5s. Reveal = BEAT 3 at 10s (33%)`
- Camera Events: `5 events as listed in §10. One sustained dolly (0:15–0:22)`
- Action Events: `ACT_STOP → ACT_RECOGNIZE → ACT_NIJI_TEASE → ACT_REVEAL → ACT_EMBARRASSED`
- Audio Events: `twelve lines of dialogue ／ the number never voiced ／ music gone by the number`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the number`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The single line `氷室湊……4時間52分` carries the reveal. If it renders as noise the segment fails. Check first; if unusable, generate the screen as a plate and composite the text in post.
- **ニジ transparency.** The model may render ニジ as a see-through ghost, or standing in the room. She must be fully opaque and inside the screen only. Verify frame by frame.
- **ニジ saying わたし.** Her lines must call 真白 「おまえ」 and never slip into first person. Check the audio closely.
- **湊 may appear as a person.** The strongest non-ニジ risk: the model may draw 湊's face in the list or a cutaway. He is text only here. The negative prompt front-loads this indirectly; verify no face appears.
- **Dialogue density.** Twelve lines in 30 seconds is the densest exchange of the episode. If it crowds the number, thin the middle lines — the reveal must hold the largest share.

## Changes

- _(none yet)_

## Next Generation

- If the number renders cleanly, S25 opens on this same held number — carry the screen plate forward.
