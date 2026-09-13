# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第12話 S54「返すよ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「返すよ」——第3本と同じ一文を、今度は真白自身の指で一文字ずつ打つ。第1話の冒頭と同じフレーミング。ニジは白い光のまま（色は S55 で戻る）。完全消失を出さない。第1本の「撫でる」が始めた指の弧が、ここで「打つ」に着地する。**

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
- Still white light — colourless, holding. The rainbow has not yet returned; the colour comes back only in the next segment. Pale and faint, a blur, not a glow, not rays. No colour, no rainbow.
- The outline is slightly blurred at the edges. **No shadow anywhere** — unlike 真白's solid, defined outline.
- Exists **inside the screen**. Never stands in the room at human scale.

### Behavior

- Personality: `Bright, teasing, unguarded — she smiles more honestly than 真白 can. She never cries. She calls 真白「おまえ」`
- Continuity: `her opacity is a strict function of the segment number (see the ledger); it never varies within a beat except in seg.55`

> **ニジ appears this segment**（ledger 54–55 — white light, before the rainbow returns）.

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
- Appearance: `The sentence おまえが私にくれた時間、私が生きてるよ。 typed by 真白's own finger, one character at a time. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
- Continuity Importance: `CRITICAL`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads 2:00 A.M.`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_12_また明日.md`
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

真白 says 「……返すよ」, and types — with her own finger, character by character — the same sentence as S03: 「おまえが私にくれた時間、私が生きてるよ。」 In the same framing as episode 1's opening.

## Beginning

ニジ (white light) holds in the screen. 真白 has understood — ニジ carries her feelings too, the words she aimed at herself. ニジ, soft: 「うん。おまえが自分に向けた言葉も、ちゃんと集まってたよ」.

## Turn

真白: 「……返すよ」. She types, character by character, the sentence from episode 3. This time it is her own finger — slow, deliberate, one character at a time.

## Peak

The sentence completes under her finger: おまえが私にくれた時間、私が生きてるよ。 Her own hand, having written it.

## Pull（引き — 切れ目）

The completed line, held on screen, typed by her own finger. Cut on the line, with nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The typing holds 17s (57%) — one sentence, one character at a time.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「返すよ」.** 真白 speaks — 「……返すよ」. ニジ (white light) waits in the screen. _Density: SPARSE — a spoken line, no event._
- **BEAT 2 `[0:07–0:24]` — 「打つ」 — REVEAL, longest share.** Her own finger types the sentence, character by character, slow and deliberate. おまえが私にくれた時間、私が生きてるよ。 Each character appears under her finger. The camera holds close, in the same framing as episode 1's opening — the hand and the screen. _Density: DENSE, continuous — but unhurried. One sentence, one character at a time._
- **BEAT 3 `[0:24–0:30]` — 「完成」.** The completed line, held on screen. Her hand, having written it, still. Cut precisely on the line. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the first character appearing (≈0:08) ／ the sentence completing (≈0:24) ／ the held line (≈0:28)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the spoken line)`
- Dense regions: `0:07–0:24 (the typing, one character at a time)`
- Long continuous action: `0:07–0:24 the deliberate typing`
- Rapid transitions: `none — a single held gesture`

---

# 9. ACTION

## Action — ACT_RESOLVE

- ID: `ACT_RESOLVE`
- Subject: `MASHIRO`
- Action: `Speaks — 「……返すよ」`
- Intention: `To declare what she is about to do`
- Intensity: `Low`
- Speed: `Slow, even`

### Action Relationship

- Before: `—` (continues from S53's naming)
- After: `ACT_TYPE`

## Action — ACT_TYPE

- ID: `ACT_TYPE`
- Subject: `MASHIRO`
- Action: `Her own finger types the sentence, character by character, slow and deliberate`
- Intention: `To return, with her own hand, the words ニジ once wrote for her`
- Intensity: `CRITICAL (the peak, expressed as the act of typing)`
- Speed: `Slow — one character at a time, no rush`

### Action Relationship

- Before: `ACT_RESOLVE`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `MASHIRO`
- Action: `The hand goes still over the completed line`
- Intention: `None — the act is done`
- Intensity: `Medium`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_TYPE`
- After: `— (cut on the line)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. The same framing as episode 1's opening — the hand and the screen`
- Lens Character: `Long-ish, very shallow. Only the screen or the fingers are ever sharp`
- Depth of Field: `Very shallow — the background is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Locked close on her face and the screen, the white light of ニジ soft in frame. She speaks. No camera movement.
- **`[0:07–0:24]`** — Cut to the hand and the screen — the same framing as episode 1's opening. The camera holds, locked, while her finger types the sentence, character by character. No movement at all.
- **`[0:24–0:30]`** — Hold on the completed line. Static. Cut precisely on the line. Nothing after it.

---

# 11. MOTION

## Subject Motion

- Her finger carries all the movement — the deliberate typing, one character at a time
- The rest of her body holds; only her eyes follow the characters as they appear
- The typing is slow and even — not fast, not hesitant

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — characters appearing under the finger. Nothing glitches, flickers, or distorts
- The wall clock's second hand advances in discrete ticks

## Environmental Motion

- ニジ (white light) holds in the screen, faint and pale — no drift of colour
- Only the screen's bloom breathes faintly on the ceiling

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her finger — practiced, but unhurried`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet resolve (「……返すよ」)
- ↓ The deliberate act (typing, one character at a time)
- ↓ A completion without ceremony (the line, held)

## Emotional Events

- Event: `「……返すよ」` — Emotion: `Resolve, not triumph` — Intensity: `LOW` — Timing: `≈0:03`
- Event: `The first character appears under her finger` — Emotion: `The act beginning — the same words, now her own` — Intensity: `MEDIUM` — Timing: `≈0:08`
- Event: `The sentence completes` — Emotion: `A quiet completion — no exclamation, no tears` — Intensity: `HIGH — expressed only as the stillness of a hand that has written it` — Timing: `≈0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's white light is the same cold white — drained of colour`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on the ceiling as a soft blue rectangle.
- **`[0:07–0:24]`** — As the camera holds on the hand and screen, the cold white dominates the frame; the screen's glow brightens faintly with each character — never flickering.
- **`[0:24–0:30]`** — The completed line glowing softly. Cut to black on the line. No flash, just the cut.

---

# 14. AUDIO

## Dialogue

> 真白, low and even: 「……返すよ」. ニジ, from the screen, soft: 「うん。おまえが自分に向けた言葉も、ちゃんと集まってたよ」. No narration, no voice-over. The sentence is typed, not read aloud. No tears.

## Sound Effects

- The soft, close taps of a finger on glass — one per character, even and unhurried
- The wall clock's second hand, dry discrete ticks, under the typing
- Soft futon fabric as she settles, once, at the very start

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, gentle. Never sinister, never sentimental — no horror strings, no swelling`
- Emotional Function: `Hold the room's stillness under the typing. It may thin toward the close, leaving only room tone, the taps, and the clock`

---

# 15. CONTINUITY

> 57本は57回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

- **Identity**: 真白 — plain Japanese high-school girl 16–17, shoulder-length dark hair, thin neck, small frame, curved posture over a phone. Same face in every take.
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen.
- **The room**: futon on the floor, curtained window, wall clock, sparse.
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light.
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue.
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers.
- **(seg.10+) ニジ**: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same neck tilt and shoulder-length hair — white light inside the screen, casting no shadow, at the colourless state this segment requires.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。

## MUST

- Render the on-screen Japanese exactly, character by character, typed by 真白's own finger: `おまえが私にくれた時間、私が生きてるよ。`
- Frame it in the same framing as episode 1's opening — close, hand-level, over-the-shoulder, the hand and the screen
- ニジ is present — 真白's own face one step younger — inside the screen only, as **white light** (still colourless)
- End by cutting on the completed line, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 54–55 レンジより）

- **No complete disappearance.** ニジ must not vanish — she is white light, still present, waiting
- No rainbow, no iridescence, no colored afterimage — the colour returns only in S55
- No tears, no crying — a quiet completion, not a grief
- No second character — ニジ is inside the screen, never standing in the room

## PREFER

- The typing uninterrupted — the whole segment is one held gesture
- Silence over score at the peak
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The tapping rhythm may vary very slightly — but it must read as deliberate, not fast
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must remain white light — no rainbow yet, and no complete disappearance (ledger 54–55). This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:07] she speaks low — 「……返すよ」 — where ニジ, a white light, waits in the screen; [0:07–0:24] THE REVEAL — in the same framing as episode 1's opening, close on the hand and the screen, her own finger types the sentence character by character, slow and deliberate: おまえが私にくれた時間、私が生きてるよ。 ; [0:24–0:30] the completed line is held, and the shot cuts on the line. The typing holds the largest share of the duration. Ends on the completed line, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. The phone screen shows an ordinary Japanese UI in cold blue-white — the compose field, where 真白's own finger types, character by character, the sentence おまえが私にくれた時間、私が生きてるよ。 In the screen, ニジ — 真白's own face, one step younger, longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, no shadow — is WHITE light, still colourless. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the finger; the body holds still. Her finger types the sentence character by character, slow and even — not fast, not hesitant — each character appearing under the finger. ニジ's white light holds in the screen, faint and pale — no drift of colour. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the fingers are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] locked close on her face and the screen, the white light soft in frame, no movement. [0:07–0:24] cut to the hand and the screen — the same framing as episode 1's opening — and hold, locked, while her finger types the sentence character by character. [0:24–0:30] hold on the completed line, static; cut precisely on the line.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, under the typing. The soft close taps of a finger on glass — one per character, even and unhurried. Soft futon fabric once at the start. 真白, low and even: 「……返すよ」. ニジ, from the screen, soft: 「うん。おまえが自分に向けた言葉も、ちゃんと集まってたよ」. The sentence is typed, not read aloud. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the close, leaving only room tone, the taps, and the clock. No horror strings, no sting, no swelling emotion, no tears.

## Negative Prompt

no complete disappearance, no fully faded figure, no vanishing apparition, no rainbow, no iridescence, no colored afterimage, no tears, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep12-seg03-30s-01`
- Segment ID: `S54`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_12, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `3 beats, NON_UNIFORM — 7s / 17s / 6s. Typing = BEAT 2 at 17s (57%)`
- Camera Events: `3 events as listed in §10. No sustained dolly; all locked holds`
- Action Events: `ACT_RESOLVE → ACT_TYPE → ACT_HOLD`
- Audio Events: `真白 one line ／ ニジ one line ／ finger taps one per character ／ clock under the typing`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the completed line`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The sentence carries the entire return. If it renders as noise the segment fails. Check first; if unusable, generate the screen as a plate and composite the text in post.
- **The typing may read as too fast or too slow.** It must be one character at a time, unhurried. If it reads as autocomplete, slow it down; if it drags, tighten.
- **The model may restore the rainbow.** ニジ is white light here; colour returns only in S55. The negative prompt front-loads this; verify frame by frame.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the typing reads well, consider a vertical 9:16 variant — the viewer is in the same posture as the protagonist.
