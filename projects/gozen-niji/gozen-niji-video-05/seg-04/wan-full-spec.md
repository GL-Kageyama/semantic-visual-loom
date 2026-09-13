# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第5話 S21「次は、おまえが届けなよ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**対話——指は完全に休み、声だけが動く。ニジは在（不透明・画面の中だけ）で、泣き方を知らない。画面文字なし。諦めも沈黙も演じず、落ちていく声と、泣かないニジの静けさに押し込む。**

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

> **No other character appears this segment.** ニジ is present（ledger 19–21 — in, fully opaque, on-screen only）. No screen text; dialogue only.

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
- Appearance: `真白's ordinary modern smartphone, plain case, Japanese UI. The only light source at night; the only surface on which the anomaly appears. Glass carries a soft bloom, never a hard specular glint. This segment the screen shows no text — an empty ordinary UI`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
- Continuity Importance: `CRITICAL`

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

Night. ニジ says it quietly: 「次は、おまえが届けなよ」. 真白's voice drops: 「――私には、無理」. Beyond the screen, ニジ does not know how to cry — the same way 真白 does not.

## Beginning

「次は」 — ニジ's voice, in the still of the night. A beat. Then the rest of it.

## Turn

「次は、おまえが届けなよ」 — not a demand, a handing-over. The words 真白 has never said, delivered now to her own hand.

## Peak

真白: 「――私には、無理」 — then, lower: 「私には無理だよ。届けるなんて、私にできる、わけない」. Her voice falls and does not rise again.

## Pull（引き — 切れ目）

Beyond the screen, ニジ does not know how to cry — the same way 真白 does not. The tears do not come, because she does not know how to let them. Cut on ニジ's face, held, not crying, with the something unexpressed.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The demand holds 9s (30%); the refusal is held 9s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「次は」.** Night. ニジ's voice, in the still: 「次は」. A beat of silence before the rest. _Density: SPARSE — one word, then a held quiet._
- **BEAT 2 `[0:07–0:16]` — 「次は、おまえが届けなよ」 — longest share.** 「次は、おまえが届けなよ」 — not a demand, a handing-over. The words 真白 has never said, delivered now to her own hand. _Density: DENSE at the head, then the words, held._
- **BEAT 3 `[0:16–0:25]` — 「私には無理」.** 真白: 「――私には、無理」 — then lower: 「私には無理だよ。届けるなんて、私にできる、わけない」. Her voice falls and does not rise again. _Density: SPARSE, internal — the refusal is a descending line._
- **BEAT 4 `[0:25–0:30]` — 「泣き方を知らない」 — held, then cut.** Beyond the screen, ニジ does not know how to cry — the same way 真白 does not. Cut on ニジ's face, held, not crying, with the something unexpressed. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `「次は」 (≈0:04) ／ 「次は、おまえが届けなよ」 (≈0:09) ／ 「――私には、無理」 (≈0:18)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the opening word), 0:16–0:25 (the refusal)`
- Dense regions: `0:07–0:16 (the demand)`
- Long continuous action: `0:25–0:30 ニジ's held face, not crying`
- Rapid transitions: `none — the slowest stretch of the episode`

---

# 9. ACTION

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `NIJI`
- Action: `Says 「次は」 — one word, then a beat`
- Intention: `To begin — to hand something over`
- Intensity: `Low, gentle`
- Speed: `Slow, quiet`

### Action Relationship

- Before: `—` (continues from S20's message)
- After: `ACT_DEMAND`

## Action — ACT_DEMAND

- ID: `ACT_DEMAND`
- Subject: `NIJI`
- Action: `「次は、おまえが届けなよ」 — a handing-over, not a demand`
- Intention: `To give the task to 真白's own hand`
- Intensity: `MEDIUM — the turn of the episode`
- Speed: `Quiet, steady`

### Action Relationship

- Before: `ACT_OPEN`
- After: `ACT_REFUSE`

## Action — ACT_REFUSE

- ID: `ACT_REFUSE`
- Subject: `MASHIRO`
- Action: `「――私には、無理」「私には無理だよ。届けるなんて、私にできる、わけない」 — her voice falling`
- Intention: `To refuse — and to mean it`
- Intensity: `MEDIUM, sinking`
- Speed: `Slow, and slowing; the voice drops and does not rise`

### Action Relationship

- Before: `ACT_DEMAND`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `NIJI`
- Action: `Holds, in the screen — does not know how to cry, and so does not. The same way 真白 does not`
- Intention: `None — the absence of a thing she was never taught`
- Intensity: `CRITICAL (the pull, expressed as a face that will not cry)`
- Speed: `Still`

### Action Relationship

- Before: `ACT_REFUSE`
- After: `— (cut on ニジ's face)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Low and close, at futon height. Into the dark with her`
- Lens Character: `Long-ish, shallow. Only the screen, her face, or ニジ's outline are ever sharp`
- Depth of Field: `Shallow — the room falls away into deep indigo`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Low static two-shot of her face and the screen, ニジ's opaque rainbow outline inside the glass. 「次は」 — then quiet.
- **`[0:07–0:16]`** — Hold on ニジ inside the screen. 「次は、おまえが届けなよ」. The demand is the frame.
- **`[0:16–0:21]`** — Cut to 真白, static, close, lit from below. 「――私には、無理」.
- **`[0:21–0:25]`** — Hold on 真白. 「私には無理だよ。届けるなんて、私にできる、わけない」. The voice falls; the frame does not move.
- **`[0:25–0:30]`** — Cut back to ニジ's face, inside the glass, held — not crying, with the something unexpressed. Cut on it.

---

# 11. MOTION

## Subject Motion

- 真白's body holds nearly still; her lips move once, small, for the refusal
- ニジ moves little — a tilt of the head, the same way 真白 tilts hers; she is inside the glass
- In the last beats, nothing moves but the faint drift of ニジ's rainbow afterimage
- The face does not cry; it holds — the tears that do not come because she was never taught how

## Object Motion

- The phone does not move on its own. Ever
- Nothing on the screen changes — no text, no notification, no glitch
- ニジ's rainbow drifts slowly — blue → green → blue — inside the screen, never leaving it

## Environmental Motion

- Nothing moves in the room. The curtain does not stir
- The screen's bloom breathes very slightly — the only continuous motion

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for both; the only motion is the faint rainbow drift`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes. The segment's only impact is a voice falling`

---

# 12. EMOTION

## Emotional Arc

- Quiet beginning (次は — one word in the dark)
- ↓ The handing-over (次は、おまえが届けなよ — not a demand)
- ↓ Sinking refusal (――私には、無理 — the voice falls and does not rise)
- ↓ The unlearned tears (泣き方を知らない — the same way 真白 does not)

## Emotional Events

- Event: `「次は、おまえが届けなよ」` — Emotion: `The handing-over — a task given to 真白's own hand` — Intensity: `MEDIUM` — Timing: `≈0:09`
- Event: `「――私には、無理」` — Emotion: `Sinking refusal — the voice falls and does not rise` — Intensity: `MEDIUM, descending` — Timing: `≈0:18`
- Event: `ニジ does not know how to cry` — Emotion: `The unlearned tears — the same absence as 真白's` — Intensity: `CRITICAL, expressed as a face that will not cry` — Timing: `0:25–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft indigo fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo; ニジ's rainbow is the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on; its light lies on her face from below.
- **`[0:07–0:16]`** — ニジ's rainbow is the only saturated color in the frame — a slow, contained drift inside the glass.
- **`[0:16–0:25]`** — The screen's light catches 真白's face from below as the voice falls.
- **`[0:25–0:30]`** — The light settles on ニジ's face, inside the glass, held. Cut on it.

---

# 14. AUDIO

## Dialogue

- ニジ: 「次は」「次は、おまえが届けなよ」 — quiet, steady. Calls 真白 「おまえ」; **never says 「わたし」**
- 真白: 「――私には、無理」「私には無理だよ。届けるなんて、私にできる、わけない」 — her voice falling, and not rising again

> No other speech. No narration, no voice-over.

## Sound Effects

- A wall clock ticking, dry and discrete, growing louder in the held beats
- ニジ's voice has a faint, close, glassy resonance — it lives inside the screen
- The deep quiet of the room, in which a clock gets louder

## Environment

- Night. Room tone and the clock only — deep quiet, almost nothing

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, resigned. Never sinister, never sentimental — no horror strings`
- Emotional Function: `Hold the night's stillness, then withdraw as 真白 refuses, leaving only room tone, the clock, and ニジ's quiet`

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

- ニジ fully opaque, inside the screen only — never standing in the room
- ニジ is 真白's own face one step younger, a rainbow afterimage drifting blue → green → blue
- 真白's voice falls on 「――私には、無理」 and does not rise again
- End on ニジ's face, held, not crying, with the something unexpressed — cut on it

## MUST NOT（この1本の禁止・開示台帳 19–21 レンジより）

- **No transparency.** ニジ is fully opaque; no see-through figure, no fading body
- **ニジ does not say 「わたし」.** No first-person self-reference. She calls 真白 「おまえ」
- **ニジ does not cry.** No tears, no weeping, no crying on ニジ's face — she does not know how
- **ニジ never leaves the screen.** No standing figure in the room, no full-scale body
- **No screen text in this segment.** It is dialogue only; nothing is read, nothing is sent
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The falling voice over any performed anguish — the drop is the whole event
- Silence over score at the pull
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- A hint of sadness may enter ニジ's smile, but never tears
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ may be shown but only fully opaque, inside the screen, not crying, never saying 「わたし」 (ledger 19–21); no screen text. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at night, with ニジ — a rainbow afterimage of her own face, one step younger, fully opaque, no shadow, inside the phone screen only. Beats, deliberately uneven: [0:00–0:07] ニジ says 次は — one word, then a beat of quiet; [0:07–0:16] 次は、おまえが届けなよ — not a demand, a handing-over, the words 真白 has never said delivered now to her own hand; [0:16–0:25] 真白 answers ――私には、無理 and then, lower, 私には無理だよ。届けるなんて、私にできる、わけない, her voice falling and not rising again; [0:25–0:30] beyond the screen, ニジ does not know how to cry — the same way 真白 does not — and the shot cuts on ニジ's face, held, not crying, with the something unexpressed. The demand holds the largest share of the duration. Ends on ニジ's face, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. At night she wears plain, fully-covered pajamas — a buttoned top and long trousers — in the futon. ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — fully opaque, a blurred rainbow afterimage inside the phone screen only, no shadow anywhere, colors drifting slowly blue → green → blue, never standing in the room at human scale, never transparent. The screen shows no text — an empty, ordinary Japanese UI in cold blue-white. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. 真白's body holds nearly still; her lips move once, small, for the refusal. ニジ moves little — a tilt of the head, the same way 真白 tilts hers — inside the glass. In the last beats nothing moves but the faint drift of ニジ's rainbow afterimage. The face does not cry; it holds — the tears that do not come because she was never taught how. Nothing on the screen changes — no text, no notification, no glitch. The phone never moves by itself and never glitches, flickers or distorts. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Low and close, at futon height — into the dark with her. Longish lens, shallow depth of field; only the screen, her face, or ニジ's outline are ever sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] low static two-shot of her face and the screen, ニジ's opaque rainbow outline inside the glass; 次は, then quiet. [0:07–0:16] hold on ニジ inside the screen; 次は、おまえが届けなよ. [0:16–0:21] cut to 真白, static, close, lit from below; ――私には、無理. [0:21–0:25] hold on 真白; 私には無理だよ、届けるなんて、私にできる、わけない, the voice falling, the frame still. [0:25–0:30] cut back to ニジ's face inside the glass, held — not crying, with the something unexpressed; cut on it.

## Audio Prompt

Almost silent. Deep quiet night room tone and a wall clock ticking, dry and discrete, growing louder in the held beats. ニジ's voice has a faint, close, glassy resonance — it lives inside the screen. Dialogue only: ニジ — 次は; 次は、おまえが届けなよ, quiet and steady, calling 真白 おまえ, never saying わたし. 真白 — ――私には、無理; 私には無理だよ。届けるなんて、私にできる、わけない, her voice falling and not rising again. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — withdrawing as 真白 refuses, leaving only room tone, the clock, and ニジ's quiet. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparent or translucent ghost, no see-through figure, no fading body, no half-visible ニジ, ニジ does not say わたし, no first-person self-reference, no tears, no crying, no weeping, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep05-seg04-30s-01`
- Segment ID: `S21`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_05, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 9s / 9s / 5s. Demand = BEAT 2 at 9s (30%)`
- Camera Events: `5 events as listed in §10. All static or held; no sustained dolly`
- Action Events: `ACT_OPEN → ACT_DEMAND → ACT_REFUSE → ACT_HOLD`
- Audio Events: `dialogue (ニジ × 真白) ／ no screen text ／ music withdrawn at the refusal`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on ニジ's face`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- *(none yet — to be filled after the first generation)*

## Anticipated risks (to check in the first generation)

- **ニジ cries.** The single most damaging failure. She does not know how to cry — no tears, no weeping. If tears appear, regenerate on the Visual slot.
- **ニジ leaves the screen or turns transparent.** She is fully opaque and inside the glass only. Verify frame by frame.
- **The refusal reads as anger rather than a sinking.** 真白's voice falls; it does not rise, snap, or shake. If it reads as a fight, re-record the Audio slot.
- **The model adds screen text.** This segment is dialogue only — no message, no notification. If text appears, regenerate on the Visual slot.

## Changes

- *(none yet)*

## Next Generation

- If the falling voice and ニジ's unlearned tears both read, episode 5 closes cleanly; episode 6 (S22) begins the addressee list of thirty-two.
