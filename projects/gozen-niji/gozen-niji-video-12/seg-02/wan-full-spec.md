# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第12話 S53「宛先は、自分」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「宛先は、自分」——名簿の最後の一行が自分自身の名前であることに気づく。指は休み、これは所作ではなく気づき。初めて宛先に名前を付ける。ニジは白い光のまま（虹色を出さない）。この命名が S54「返すよ」の動機になる。**

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
- A faint white light where the rainbow afterimage once was — still colourless. Pale and faint, a blur, not a glow, not rays. No colour, no rainbow.
- The outline is slightly blurred at the edges. **No shadow anywhere** — unlike 真白's solid, defined outline.
- Exists **inside the screen**. Never stands in the room at human scale.

### Behavior

- Personality: `Bright, teasing, unguarded — she smiles more honestly than 真白 can. She never cries. She calls 真白「おまえ」`
- Continuity: `her opacity is a strict function of the segment number (see the ledger); it never varies within a beat except in seg.55`

> **ニジ appears this segment**（ledger 53 — white light, still colourless）.

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
- Appearance: `No message text this segment — the naming is spoken, not typed. The screen holds ニジ as white light, and an addressee list whose last line is her own name`
- Narrative Importance: `LOW`
- Visual Importance: `LOW`
- Continuity Importance: `LOW`

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

真白 understands what the last record is: the time she deposited with herself — 「どうせ、誰も、私を、見てない」 — and names its addressee for the first time. 宛先は、自分。

## Beginning

ニジ (white light) is there, in the screen. 真白 speaks, low: 「……最後の宛先、分かったよ」.

## Turn

The first record — 「おまえが私にくれた時間、私が生きてるよ」 — was a message to herself. The time she spent thinking no one saw her, the time she left unreturned: 「どうせ、誰も、私を、見てない」.

## Peak

She names the addressee for the first time — 宛先は、自分. The last line of the list is her own name.

## Pull（引き — 切れ目）

宛先は、自分. Cut on the realization, the white light of ニジ still holding in the screen.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The naming reveal holds 10s (33%).

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「最後の宛先」.** 真白 speaks, low — 「……最後の宛先、分かったよ」. ニジ (white light) listens from the screen. _Density: SPARSE — a spoken line, no event._
- **BEAT 2 `[0:06–0:16]` — 「どうせ、誰も見てない」 — recollection.** She recalls the words she aimed at herself: どうせ、誰も、私を、見てない。 The time she left unreturned. The addressee field, her own name, at the bottom. _Density: DENSE — the recollection lands, then stills._
- **BEAT 3 `[0:16–0:26]` — 「宛先は、自分」 — REVEAL, longest share.** She names the addressee for the first time. 宛先は、自分. The realization held — no motion, only the white light of ニジ. _Density: SPARSE, inverted — the event is the naming, not the motion._
- **BEAT 4 `[0:26–0:30]` — 「白い光」.** Hold on the white light of ニジ in the screen. Cut precisely on the pull. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the recollection 「どうせ、誰も、私を、見てない」(≈0:08) ／ the naming 宛先は、自分 (≈0:18)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the spoken line), 0:16–0:30 (the held naming and the white light)`
- Dense regions: `0:06–0:16 (the recollection)`
- Long continuous action: `0:16–0:26 the held realization`
- Rapid transitions: `none — a quiet, internal segment`

---

# 9. ACTION

## Action — ACT_SPEAK

- ID: `ACT_SPEAK`
- Subject: `MASHIRO`
- Action: `Speaks, low, to ニジ — 「……最後の宛先、分かったよ」`
- Intention: `To voice the answer she has reached`
- Intensity: `Low`
- Speed: `Slow, unforced`

### Action Relationship

- Before: `—` (continues from S52's white light)
- After: `ACT_RECALL`

## Action — ACT_RECALL

- ID: `ACT_RECALL`
- Subject: `MASHIRO`
- Action: `Eyes go inward, over the words she aimed at herself: どうせ、誰も、私を、見てない`
- Intention: `To trace the time she left unreturned`
- Intensity: `Medium, internal`
- Speed: `Slow, and slowing`

### Action Relationship

- Before: `ACT_SPEAK`
- After: `ACT_NAME`

## Action — ACT_NAME

- ID: `ACT_NAME`
- Subject: `MASHIRO`
- Action: `Names the addressee for the first time — 宛先は、自分. The finger stays at rest`
- Intention: `To attach a name to what the record is`
- Intensity: `CRITICAL (the peak, expressed as a naming)`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_RECALL`
- After: `— (cut on the white light)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, very shallow. Only the screen or the fingers are ever sharp`
- Depth of Field: `Very shallow — the background is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Locked close on her face and the screen, the white light of ニジ soft in frame. She speaks. No camera movement.
- **`[0:06–0:14]`** — A slow drift toward the screen — the addressee list, the last line her own name. The piece's single sustained move.
- **`[0:14–0:16]`** — Absolutely locked on the last line of the list. Static.
- **`[0:16–0:26]`** — Cut back to her face, the realization settling. No camera movement at all.
- **`[0:26–0:30]`** — Hold on the white light of ニジ in the screen. Cut precisely on the pull.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially no movement; her body holds
- Only her eyes move — inward over the recollection, then settling
- The stillness is absolute after the naming

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a list visible. Nothing glitches, flickers, or distorts
- The wall clock's second hand advances in discrete ticks

## Environmental Motion

- ニジ (white light) holds in the screen — a faint, pale light, no drift of colour
- Only the screen's bloom breathes faintly on the ceiling

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet certainty (the answer found: 最後の宛先)
- ↓ Recollection (the words she aimed at herself)
- ↓ The naming (宛先は、自分 — the first time the addressee has a name)
- ↓ Stillness (the white light, then cut)

## Emotional Events

- Event: `The recollection 「どうせ、誰も、私を、見てない」` — Emotion: `Recognition, not self-pity` — Intensity: `MEDIUM, internal` — Timing: `≈0:08`
- Event: `The naming 宛先は、自分` — Emotion: `The realization made real — a naming, not a cry` — Intensity: `CRITICAL — expressed only as stillness. No facial performance, no tears` — Timing: `≈0:18`
- Event: `The white light holding` — Emotion: `The presence that does not leave` — Intensity: `MEDIUM, suppressed` — Timing: `0:26–0:30`

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
- **`[0:06–0:16]`** — As the camera drifts to the list, the screen's cold white dominates the frame; her face falls almost to silhouette.
- **`[0:16–0:26]`** — Her face lit from below, almost to silhouette, as the realization settles.
- **`[0:30]`** — Cut to black on the white light. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

> 真白, low and even: 「……最後の宛先、分かったよ」／ 「私、自分に時間を、預けてた。『どうせ、誰も、私を、見てない』って」. ニジ, from the screen, a single soft 「うん」. No narration, no voice-over. No tears.

## Sound Effects

- The wall clock's second hand, dry discrete ticks, present throughout
- Soft futon fabric as she shifts, once, at the very start
- The near-absence of sound around the naming

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental — no horror strings, no swelling`
- Emotional Function: `Hold the room's stillness, then withdraw as the naming lands, leaving only room tone and the clock`

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

- ニジ is present — 真白's own face one step younger — inside the screen only, as **white light** (still colourless)
- No screen text (§0.5: なし — the naming is spoken and internal, not an on-screen exchange)
- Let the naming 宛先は、自分 be the peak, and hold on it
- End by cutting on the white light of ニジ, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 53 レンジより）

- **No rainbow, no iridescence, no colored afterimage.** ニジ remains white light — the colour returns only in S55
- No tears, no crying — a naming, not a grief
- No second character — ニジ is inside the screen, never standing in the room

## PREFER

- The stillness uninterrupted — the whole segment is one held realization
- Silence over score at the peak
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The slow drift toward the list may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must remain white light, still colourless — no rainbow (ledger 53). This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:06] she speaks low to the screen — 「……最後の宛先、分かったよ」 — where ニジ, a white light, listens; [0:06–0:16] she recalls the words she aimed at herself, どうせ、誰も、私を、見てない, the time she left unreturned, the addressee list with her own name at the bottom; [0:16–0:26] THE REVEAL — she names the addressee for the first time, 宛先は、自分, and the realization is held; [0:26–0:30] hold on the white light of ニジ, and the shot cuts on the white light. The naming holds the largest share of the duration. Ends on the white light, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. On screen, ニジ — 真白's own face, one step younger, longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, no shadow — inside the phone screen only, as WHITE light, still colourless. The screen also shows an addressee list whose last line is her own name. No rainbow, no iridescence, no colored afterimage. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost nothing moves except the eyes; the body and the finger hold still. ニジ's white light holds in the screen, faint and pale — no drift of colour. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the fingers are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked close on her face and the screen, the white light soft in frame, no movement. [0:06–0:14] a slow drift toward the screen — the addressee list, the last line her own name — the piece's single sustained move. [0:14–0:16] locked on the last line, static. [0:16–0:26] cut back to her face, the realization settling, no movement. [0:26–0:30] hold on the white light of ニジ; cut precisely on the pull.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, present throughout. Soft futon fabric once at the start. 真白, low and even: 「……最後の宛先、分かったよ」 then 「私、自分に時間を、預けてた。『どうせ、誰も、私を、見てない』って」. ニジ, from the screen, a single soft 「うん」. No narration, no voice-over, no other speech. Music extremely sparse — a few sustained tones at most — withdrawing as the naming lands, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion, no tears.

## Negative Prompt

no rainbow, no iridescence, no colored afterimage, no tears, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep12-seg02-30s-01`
- Segment ID: `S53`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_12, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 10s / 10s / 4s. Naming = BEAT 3 at 10s (33%)`
- Camera Events: `5 events as listed in §10. One sustained drift (0:06–0:14)`
- Action Events: `ACT_SPEAK → ACT_RECALL → ACT_NAME`
- Audio Events: `真白 two lines ／ ニジ one 「うん」 ／ clock ticking throughout`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the white light`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The model may restore the rainbow.** ニジ must stay white light here. If colour leaks in, it spoils S55. The negative prompt front-loads "no rainbow"; verify frame by frame.
- **The naming may read as a spoken line too loud.** It is quiet and even. If it reads as a performance, drop the volume, not the line.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.
- **The model may add a tear.** A naming, not a grief. The base negative carries "no crying"; watch for any wetness.

## Changes

- _(none yet)_

## Next Generation

- If the naming reads cleanly, consider holding it 1–2 seconds longer, taking the time from beat 1.
