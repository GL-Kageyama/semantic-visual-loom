# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第3話 S10「画面の中の何か」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**ニジ初登場——通知でも着信でもなく、ただゆっくり明るくなる画面。滲んだ虹色の残像が肩まで伸びた髪・細い首・真白と同じ顔（一歩幼い・完全に不透明）へ輪郭を得る。恐怖は顔に出さず、布団を掴んで関節が白くなる指だけに落とす。名前はまだ付けない（S12まで）。**

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

> **ニジ appears this segment**（ledger 10 — her first appearance: a blurred rainbow afterimage resolving into 真白's own face, one step younger, fully opaque, inside the screen only）. No other character appears this segment.

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

- Type: `none`
- Appearance: `No message text this segment — no UI, no bubbles, no notification. The screen carries only the blurred rainbow afterimage resolving into ニジ's face, its cold blue-white glow on a dark empty screen`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_03_午前二時の幽霊の名前.md`
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

午前2時、the phone lights by itself — no notification, no call, only the screen slowly brightening, and the night's darkness pushed back. 真白 lifts it in both hands. Inside the screen: something. A blurred rainbow afterimage that, as she narrows her eyes, slowly takes an outline — shoulder-length hair, a thin neck — **her own face, one step younger**. It speaks: 「やっほー」.

## Beginning

2:00 A.M. The room is dark. The phone by the pillow brightens on its own — no notification, no ring. Just light, slowly, quietly, pushing the dark back. 真白 watches it, still, from the futon.

## Turn

She picks it up in both hands. Inside the screen — something is there. A blurred rainbow afterimage, smudged. As she narrows her eyes, it slowly gains an outline: shoulder-length hair, a thin neck. It is **her own outline** — her own face, but one step younger. Longer lashes. Slightly fuller cheeks. One step short of the face she sees in the mirror every day.

## Peak

「やっほー」 — the thing in the screen, wearing her own face, speaks. 真白's throat closes; the words roll and will not come out. Her fingers grip the futon, and the knuckles go white.

## Pull（引き — 切れ目）

「……だれ」 — her voice hoarse, the first sound she manages. Cut on the question, held, against the glowing screen and the younger face inside it. 誰、何、なぜ — left hanging.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The outline-resolving reveal holds 12s (40%); the whitening grip is held 7s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「光る」.** 2:00 A.M. The phone by the pillow brightens on its own — no notification, no ring. The screen's light pushes the dark back. Her eyes go to it, and stay. _Density: SPARSE — one slow brightening._
- **BEAT 2 `[0:07–0:19]` — 「輪郭」 — REVEAL, longest share.** Her hands lift the phone. Inside: a blurred rainbow afterimage. As she narrows her eyes, it slowly gains an outline — shoulder-length hair, a thin neck. Her own face, one step younger. Fully opaque. _Density: DENSE at the head (blur → outline), then the face, held._
- **BEAT 3 `[0:19–0:26]` — 「やっほー」 — PEAK, held.** The thing in the screen speaks. 真白's throat closes. Her fingers grip the futon; the knuckles go white. Nothing else moves. _Density: SPARSE, inverted — the event is the grip, not the face._
- **BEAT 4 `[0:26–0:30]` — 「だれ」.** 「……だれ」 — hoarse, barely voiced. Her eyes on the younger face. Cut to black on the question, the screen still glowing. _Density: HELD — then cut precisely on the pull. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the screen brightening on its own (≈0:02) ／ the outline resolving into her own face (≈0:12) ／ the knuckles going white (≈0:20, then held)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the brightening), 0:19–0:26 (the held grip)`
- Dense regions: `0:07–0:19 (blur → outline, the reveal)`
- Long continuous action: `0:19–0:26 the whitening grip, held`
- Rapid transitions: `none — the slowest, most held reveal of the series so far`

---

# 9. ACTION

## Action — ACT_WATCH

- ID: `ACT_WATCH`
- Subject: `MASHIRO`
- Action: `Eyes go to the phone and stay as it brightens by itself in the dark`
- Intention: `To understand what woke the screen`
- Intensity: `Low`
- Speed: `Still. Only her eyes move`

### Action Relationship

- Before: `—`
- After: `ACT_LIFT`

## Action — ACT_LIFT

- ID: `ACT_LIFT`
- Subject: `MASHIRO`
- Action: `Lifts the phone in both hands and brings it close, narrowing her eyes at the blurred rainbow afterimage inside`
- Intention: `To see what is in the screen`
- Intensity: `Medium, internal`
- Speed: `Slow, careful`

### Action Relationship

- Before: `ACT_WATCH`
- After: `ACT_GRIP`

## Action — ACT_GRIP

- ID: `ACT_GRIP`
- Subject: `MASHIRO`
- Action: `As the outline resolves into her own face, her fingers grip the futon; the knuckles go white. Her throat works, but no sound comes`
- Intention: `None — the body arrives before the understanding. The fear goes into the grip, not the face`
- Intensity: `CRITICAL (the first appearance, expressed as a whitening grip)`
- Speed: `Instant, then held`

### Action Relationship

- Before: `ACT_LIFT`
- Simultaneous With: `NIJI's first word 「やっほー」`
- After: `ACT_ASK`

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MASHIRO`
- Action: `Forces out the first sound — 「……だれ」, hoarse, eyes still on the younger face in the screen`
- Intention: `To name the unnameable thing in front of her`
- Intensity: `Medium, barely voiced`
- Speed: `Slow, then still`

### Action Relationship

- Before: `ACT_GRIP`
- After: `— (cut to black)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Only the screen or her hands are ever sharp`
- Depth of Field: `Very shallow — the room falls away into deep indigo`
- Camera Style: `Slow, deliberate, nearly still. One slow push to the screen, and it belongs to the reveal`

## Camera Events

- **`[0:00–0:07]`** — Low static close on the phone by the pillow. The screen brightens on its own, silently, its light pushing the dark back. Optional: an imperceptibly slow push-in.
- **`[0:07–0:12]`** — Her hands enter frame and lift the phone toward her. The blurred rainbow afterimage is visible, out of focus, beginning to sharpen.
- **`[0:12–0:19]`** — One slow continuous dolly in on the screen as the afterimage gains its outline — shoulder-length hair, a thin neck, a face. The piece's single sustained move, and it belongs to the reveal. Locked, held.
- **`[0:19–0:26]`** — Cut to her face, lit from below, nearly to silhouette. Then rack focus to her hand gripping the futon in the foreground — the knuckles white, the only sharp thing in the frame.
- **`[0:26–0:30]`** — Slow pull back just enough to bring the younger face in the screen and her whitening grip into one frame. Cut to black on the question.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially all the movement — until the grip, when they carry the meaning
- The lift is slow and careful; the narrowing of her eyes is the only visible reaction on her face
- The grip is the peak: fingers close around the futon, knuckles going white, held — not a shake, a clamp
- At the end only her lips move, forming the question with effort

## Object Motion

- The phone does not move on its own; it does not vibrate, jump, or glitch. Its screen only brightens, slowly, as if the backlight were waking
- Screen content does not scroll, type, or distort. The only thing on it is the blurred rainbow afterimage gaining an outline
- The wall clock's second hand advances in discrete ticks, faint, out of focus

## Environmental Motion

- The night's darkness seems to recede as the screen brightens — but nothing in the room actually moves
- The screen's bloom breathes very slightly — the only continuous motion

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in both hands; the futon compresses under her grip`
- Inertia: `High for her body, near-zero for her fingers — until the grip, which is instant and locked`
- Acceleration: `Gentle everywhere except the grip`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes. The only impact is a hand closing white`

---

# 12. EMOTION

## Emotional Arc

- Quiet alert (the screen waking on its own)
- ↓ Cold recognition — not fear, recognition (the outline is her own face)
- ↓ The body arriving before the mind (the whitening grip)
- ↓ A question that does not land (……だれ, into the glowing screen)

## Emotional Events

- Event: `The screen brightens by itself` — Emotion: `Quiet alert — something is beginning` — Intensity: `LOW` — Timing: `≈0:02`
- Event: `The outline resolves into her own face, one step younger` — Emotion: `Cold recognition` — Intensity: `HIGH` — Timing: `≈0:12`
- Event: `The knuckles go white` — Emotion: `The body arriving before the understanding` — Intensity: `CRITICAL — expressed only as a whitening grip. No facial performance` — Timing: `≈0:20, held to 0:26`
- Event: `「……だれ」` — Emotion: `The question that does not land` — Intensity: `MEDIUM, suppressed` — Timing: `0:26–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. The rainbow afterimage inside the screen is the only saturated hue in the frame`

## Lighting Events

- **`[0:00]`** — The screen wakes, slowly — no flash, no dim. Its light grows and the dark around it seems to step back.
- **`[0:07–0:19]`** — As the camera closes on the screen, its light dominates the frame; her face falls almost to silhouette. The evidence outshines the person.
- **`[0:19–0:26]`** — Rack focus to the hand: the screen's light catches the knuckles from below, white against the dark futon.
- **`[0:30]`** — Cut to black on the question. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

- ニジ: 「やっほー」 — bright, unguarded, from inside the screen. Her first spoken word in the series
- 真白: 「……だれ」 — hoarse, barely voiced, the first sound she manages

> ニジ's speech carries **no 「わたし」** — no first-person self-reference, not here, not yet. She calls 真白「おまえ」. No narration, no voice-over.

## Sound Effects

- The near-silence of the screen waking — no chime, no buzz, no vibration. It arrives as light only
- The soft fabric of the futon as her fingers close on it and the knuckles go white — a faint, tense crease
- A wall clock ticking, dry and discrete, present and growing louder in the held beats

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental — no horror strings, no sting`
- Emotional Function: `Hold the room's stillness under the brightening, then **withdraw** as the outline resolves — the reveal needs silence. Music is gone by the whitening grip, leaving only room tone and the clock`

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

- ニジ's **first appearance** — a blurred rainbow afterimage that resolves into 真白's own face, one step younger, **fully opaque**
- Render ニジ as 真白's own face, one step younger: longer lashes, slightly fuller cheeks, the same way of tilting her head. Never a different person's design
- Keep her **inside the phone screen**. She never stands in the room at human scale
- The phone wakes **silently** — light only, no chime, no buzz, no vibration
- Show the fear through the whitening grip on the futon, not through her face
- End on 「……だれ」, cut to black on the question, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 10 レンジより）

- **No transparency.** ニジ is fully opaque. She is a blurred *afterimage*, not a transparent ghost — blurred, never see-through
- **No 「わたし」 from ニジ.** No first-person self-reference in her speech
- **Do not name her.** No「ニジ」on screen, in speech, or in any text before S12
- **No ghost in the room.** No apparition at human scale beside her, no second body outside the screen, no glowing eyes
- No supernatural VFX — no glitch, no particles, no light rays, no aura. The rainbow is a smudged afterimage, not a light effect
- Do not have 真白 scream, gasp, or widen her eyes

## PREFER

- The outline resolving slowly, so the recognition lands before the face is fully sharp
- Silence over score at the reveal
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in during beat 1 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ appears for the first time (ledger 10 — a blurred rainbow afterimage resolving into 真白's own face, one step younger, fully opaque, inside the screen only). No transparency, no 「わたし」 in her speech, no name before S12. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:07] the phone by the pillow brightens on its own — no notification, no ring, just slow light pushing the dark back; [0:07–0:19] THE REVEAL — she lifts it in both hands, and a blurred rainbow afterimage inside the screen slowly gains an outline, the same shoulder-length dark hair and thin neck, resolving into her own face one step younger, fully opaque, with no shadow anywhere; [0:19–0:26] THE PEAK — the thing in the screen speaks 「やっほー」, her throat closes, and her fingers grip the futon until the knuckles go white; [0:26–0:30] she forces out 「……だれ」, hoarse, and the shot cuts to black on the question against the glowing screen. The reveal holds the largest share of the duration. Ends on the question, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ is 真白's own face one step younger (longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head), a rainbow afterimage INSIDE the phone screen, never standing in the room at human scale, with no shadow anywhere, fully opaque. Her colors drift slowly, blue to green to blue. Night is deep indigo lit solely by one cold blue-white phone screen; the rainbow inside the screen is the only saturated hue. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her hands lift the phone slowly and carefully; she narrows her eyes at the screen. The blurred rainbow afterimage gains its outline gradually, smudged and opaque — blurred, never transparent — resolving into a crisp, fully opaque face. Her fingers close around the futon and the knuckles go white, held, not a shake but a clamp. At the end only her lips move, forming the question with effort. The phone never moves by itself and never glitches, flickers or distorts; its screen only brightens slowly, like a waking backlight. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or her hands are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] low static close on the phone as the screen brightens on its own, optionally an imperceptibly slow push-in. [0:07–0:12] her hands lift the phone; the blurred rainbow afterimage begins to sharpen. [0:12–0:19] one slow continuous dolly in on the screen as the afterimage gains its outline — the piece's single sustained move. [0:19–0:26] cut to her face lit from below, then rack focus to her hand gripping the futon, the white knuckles the only sharp thing in the frame. [0:26–0:30] a slow pull back to bring the younger face in the screen and her whitening grip into one frame; cut to black on the question.

## Audio Prompt

Almost silent. Deep quiet night room tone and a wall clock ticking, dry and discrete, growing louder in the held beats. The screen wakes with no sound — no chime, no buzz, no vibration. The soft fabric of the futon as her fingers close on it, a faint tense crease. Two spoken lines: ニジ says 「やっほー」, bright and unguarded, from inside the screen — no 「わたし」 in her speech, she calls 真白 「おまえ」; 真白 says 「……だれ」, hoarse and barely voiced. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as the outline resolves and gone by the whitening grip, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparency, no translucency, no see-through body, no わたし in ニジ's speech, no first-person self-reference, no name spoken before this moment, no standing in the room at human scale, no figure outside the phone screen, no full-height apparition, no glowing eyes, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep03-seg01-30s-01`
- Segment ID: `S10`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_03, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 12s / 7s / 4s. Reveal = BEAT 2 at 12s (40%)`
- Camera Events: `5 events as listed in §10. One sustained dolly (0:12–0:19)`
- Action Events: `ACT_WATCH → ACT_LIFT → ACT_GRIP → ACT_ASK`
- Audio Events: `two spoken lines (ニジ 「やっほー」 ／ 真白 「……だれ」) ／ screen silent (light only) ／ clock ticking throughout`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut to black on the question`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The model makes ニジ transparent.** The single most damaging failure here. She must be a blurred *afterimage*, opaque — blurred is not the same as see-through. Verify frame by frame that her body is never translucent.
- **The model renders her as a different person.** Her face must be 真白's own, one step younger. If she looks like a separate character, the whole staged disclosure collapses. §15 (in series-constants) is the defense.
- **The model names her or lets her say 「わたし」.** Both are forbidden before S12/S31. Check the audio and any rendered text.
- **The model adds a full-body ghost in the room.** She lives inside the screen only. If a figure appears at human scale beside 真白, regenerate.

## Changes

- _(none yet)_

## Next Generation

- If the outline reads as 真白's own face, fully opaque and inside the screen, this segment lands the series' first apparition; S11 continues with her explanation of 「預けた時間」.
