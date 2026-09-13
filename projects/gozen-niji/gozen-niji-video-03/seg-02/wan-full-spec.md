# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第3話 S11「預けた時間」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「預けた時間」の説明——いいね・既読・返事が、そのまま「時間」の名前に変わる。概念は一度も語らず、画面の光を浴びた指が「急に重くなる」ことだけで観客に落とす。指は画面に触れずに休み、その休んだ指にこの話の重量が乗る。名前はまだ付けない（S12まで）。**

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

> **ニジ appears this segment**（ledger 11–13 — present, fully opaque, inside the screen only）. No other character appears this segment.

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
- Appearance: `No message text this segment — no UI, no bubbles, no notification. The screen carries only ニジ's face, her rainbow colors drifting slowly on a dark empty screen`
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

ニジ explains what she is: 「おまえが誰かに預けた時間。それが、集まると、こういうのができるんだよ。」 真白 cannot keep up — いいね？ 既読？ 返事？ — and the finger bathed in the screen's light suddenly feels heavy.

## Beginning

Continuing from the question she could not finish. 真白 holds the phone in both hands, eyes on the younger face in the screen, still. The room is dark; the screen is the only light.

## Turn

ニジ: 「おまえが誰かに預けた時間。それが、集まると、こういうのができるんだよ。」 真白: 「預けるって、何。」 ニジ: 「時間を渡すってこと。おまえは、毎日、誰かに時間を渡してる。いいね、とか、既読、とか、返事、とか。そういうの、ぜんぶ時間だよ。」

## Peak

真白's understanding cannot keep up. いいねが時間？ 既読が？ 返事が？ The finger in the screen's light — the finger that does these things every night — **suddenly feels heavy**.

## Pull（引き — 切れ目）

She looks down at her own finger, as if the weight were really there. The meaning does not land. Cut on the heavy finger and the unanswered idea: 時間が、預けられている。

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** ニジ's explanation holds 14s (47%); the heavy finger is held 7s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:08]` — 「預けた時間」 — the nature, stated.** ニジ speaks: おまえが誰かに預けた時間。それが、集まると、こういうのができるんだよ。 Her face, one step younger, in the screen. 真白 listens, still. _Density: DENSE — the reveal in words._
- **BEAT 2 `[0:08–0:15]` — 「預けるって何」 — the question, then the answer.** 真白: 預けるって、何。 ニジ: 時間を渡すってこと。おまえは、毎日、誰かに時間を渡してる。いいね、とか、既読、とか、返事、とか。そういうの、ぜんぶ時間だよ。 _Density: DENSE — dialogue, the turn._
- **BEAT 3 `[0:15–0:22]` — 「重い」 — PEAK, held.** 真白's understanding cannot keep up. いいねが時間？ 既読が？ 返事が？ The finger in the screen's light suddenly feels heavy. Nothing moves. _Density: SPARSE, inverted — the event is a weight._
- **BEAT 4 `[0:22–0:30]` — 「意味」.** She looks down at her own finger, as if the weight were really there. The meaning does not land. The screen holds the younger face, waiting. Cut to black on the heavy finger. _Density: HELD — then cut. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `ニジ's explanation of 預けた時間 (≈0:02) ／ the listing いいね、既読、返事 (≈0:11) ／ the finger suddenly heavy (≈0:16, then held)`

## Temporal Density

- Sparse regions: `0:15–0:22 (the heavy finger), 0:22–0:30 (the unlanding meaning)`
- Dense regions: `0:00–0:15 (the explanation, the dialogue)`
- Long continuous action: `0:15–0:30 the still hand and the weight`
- Rapid transitions: `none — this is a held, dialogue-driven segment`

---

# 9. ACTION

## Action — ACT_LISTEN

- ID: `ACT_LISTEN`
- Subject: `MASHIRO`
- Action: `Holds the phone in both hands, eyes on the younger face in the screen, still. The fingers rest, not touching the screen`
- Intention: `To hear what she is`
- Intensity: `Low`
- Speed: `Still. Only her eyes move`

### Action Relationship

- Before: `—` (continues from S10's 「……だれ」)
- After: `ACT_ASK`

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MASHIRO`
- Action: `Asks 「預けるって、何」, the question small and unsteady`
- Intention: `To make the abstract become concrete`
- Intensity: `Medium, suppressed`
- Speed: `Slow`

### Action Relationship

- Before: `ACT_LISTEN`
- After: `ACT_HEAVY`

## Action — ACT_HEAVY

- ID: `ACT_HEAVY`
- Subject: `MASHIRO`
- Action: `As ニジ lists いいね・既読・返事, her understanding fails; the finger bathed in the screen's light suddenly feels heavy. She holds it as if the weight were real`
- Intention: `None — the idea lands in the body, not the mind`
- Intensity: `CRITICAL (the concept, expressed as a physical weight)`
- Speed: `Instant, then held`

### Action Relationship

- Before: `ACT_ASK`
- Simultaneous With: `ニジ's line そういうの、ぜんぶ時間だよ`
- After: `ACT_GAZE`

## Action — ACT_GAZE

- ID: `ACT_GAZE`
- Subject: `MASHIRO`
- Action: `Looks down at her own finger, then back to the screen, the meaning not landing`
- Intention: `To make the weight mean something`
- Intensity: `Medium, suppressed`
- Speed: `Very slow`

### Action Relationship

- Before: `ACT_HEAVY`
- After: `— (cut to black)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. The screen, or her hands, or her eyes are sharp; the rest falls away`
- Depth of Field: `Very shallow — the room is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. The one move belongs to the finger`

## Camera Events

- **`[0:00–0:08]`** — Locked close on the screen and the younger face inside it. ニジ speaks. Static, or an imperceptibly slow push-in.
- **`[0:08–0:15]`** — A slight, slow cut to her face, lit from below, listening. Then back to the screen — the exchange, in a quiet two-shot rhythm.
- **`[0:15–0:22]`** — A slow tilt down to her hand and the phone — the finger in the screen's light, suddenly heavy. Rack focus onto the finger.
- **`[0:22–0:30]`** — Hold on the finger. Then a slow pull back just enough to bring the finger and the younger face into one frame. Cut to black on the finger.

---

# 11. MOTION

## Subject Motion

- Her body holds almost still; the fingers rest on the phone without touching the screen
- Only her eyes move — screen to her own hand, and back — until the finger goes heavy
- The heaviness is a stillness that becomes weight: the hand does not move, but it seems to carry more
- Her lips part on the question and close again; nothing else

## Object Motion

- The phone does not move on its own. Ever
- Screen content does not scroll, type, or distort. The only thing on it is ニジ's face, whose rainbow colors drift slowly — blue to green to blue
- The wall clock's second hand advances in discrete ticks, faint, out of focus

## Environmental Motion

- The screen's bloom breathes very slightly — the only continuous motion
- Nothing in the room moves. The curtain does not stir

## Physical Characteristics

- Weight: `Ordinary — then, in a beat, the finger feels heavy, as if the light itself had weight`
- Inertia: `High for her body, near-zero for her fingers`
- Acceleration: `Gentle everywhere. The heaviness arrives as a still, sudden pressure`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes. The only impact is a finger growing heavy`

---

# 12. EMOTION

## Emotional Arc

- Listening (hearing what she is)
- ↓ Unsteadiness (預けるって、何 — the question that wants ground)
- ↓ The idea landing in the body (the finger suddenly heavy)
- ↓ A meaning that does not resolve (cut on the weight)

## Emotional Events

- Event: `ニジ explains 預けた時間` — Emotion: `The world tilting — everyday gestures renamed as time` — Intensity: `MEDIUM` — Timing: `≈0:02`
- Event: `いいね、既読、返事 — ぜんぶ時間だよ` — Emotion: `Cold recognition, not yet understood` — Intensity: `HIGH` — Timing: `≈0:11`
- Event: `The finger suddenly heavy` — Emotion: `The body arriving before the mind` — Intensity: `CRITICAL — expressed only as a physical weight. No facial performance` — Timing: `≈0:16, held to 0:22`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow is the only saturated hue in the frame`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on her face from below. ニジ's rainbow drifts slowly inside the glass, the only color in the dark.
- **`[0:08–0:15]`** — Her face nearly to silhouette as the camera holds on the screen; the screen's light the whole frame.
- **`[0:15–0:22]`** — The tilt down to the finger: the screen's light catches it from below, the knuckle a thin bright line, the finger seeming to sink under the light.
- **`[0:30]`** — Cut to black on the finger. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

- ニジ: 「おまえが誰かに預けた時間。それが、集まると、こういうのができるんだよ。」
- 真白: 「預けるって、何」
- ニジ: 「時間を渡すってこと。おまえは、毎日、誰かに時間を渡してる。いいね、とか、既読、とか、返事、とか。そういうの、ぜんぶ時間だよ。」

> ニジ's speech carries **no 「わたし」** — no first-person self-reference. She calls 真白「おまえ」, ending with a period. No narration, no voice-over.

## Sound Effects

- The wall clock's dry discrete ticking, present throughout, growing louder in the held beats
- The soft friction of her palms against the phone's case as she shifts her grip, once, when the finger grows heavy
- Almost nothing else

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental — no horror strings, no swelling`
- Emotional Function: `Hold the room's stillness under the dialogue, then **thin** as the finger grows heavy, leaving only room tone and the clock at the cut`

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

- Render ニジ as 真白's own face, one step younger, **fully opaque**, a rainbow afterimage **inside the phone screen**
- ニジ's dialogue — exactly: `おまえが誰かに預けた時間。それが、集まると、こういうのができるんだよ。` ／ `時間を渡すってこと。おまえは、毎日、誰かに時間を渡してる。いいね、とか、既読、とか、返事、とか。そういうの、ぜんぶ時間だよ。`
- Keep the fingers at rest — no scrolling, no typing; the segment's gesture is stillness
- Show the heaviness of the finger as the concept lands — not in the face, in the hand
- End on the heavy finger, cut to black, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 11–13 レンジより）

- **No transparency.** ニジ is fully opaque. Blurred is not transparent
- **No 「わたし」 from ニジ.** No first-person self-reference in her speech
- **Do not name her.** No「ニジ」in speech or text before S12
- **No ghost in the room.** No apparition at human scale, no second body outside the screen
- No supernatural VFX — no glitch, no particles, no light rays. The rainbow is a smudged afterimage
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The dialogue carried in stillness — long holds, few cuts
- The finger's heaviness over any explicit statement of the idea
- Silence over score at the peak

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The push-in during beat 1 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ is present, fully opaque, inside the screen only (ledger 11–13). No transparency, no 「わたし」 in her speech, no name before S12. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at night, holding her phone in both hands. Beats, deliberately uneven: [0:00–0:08] the younger face inside the screen speaks — おまえが誰かに預けた時間。それが、集まると、こういうのができるんだよ。 — and she listens, still; [0:08–0:15] she asks 預けるって、何, and ニジ answers 時間を渡すってこと。おまえは、毎日、誰かに時間を渡してる。いいね、とか、既読、とか、返事、とか。そういうの、ぜんぶ時間だよ。; [0:15–0:22] THE PEAK — her understanding cannot keep up, いいねが時間？ 既読が？ 返事が？, and the finger bathed in the screen's light suddenly feels heavy; [0:22–0:30] she looks down at her own finger as if the weight were real, the meaning not landing, and the shot cuts to black on the heavy finger. The explanation holds the largest share of the duration. Ends on the heavy finger, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ is 真白's own face one step younger (longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head), a rainbow afterimage INSIDE the phone screen, never standing in the room at human scale, with no shadow anywhere, fully opaque. Her colors drift slowly, blue to green to blue. Night is deep indigo lit solely by one cold blue-white phone screen. No on-screen text, no message bubbles — the screen carries only her face. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her body holds almost still; the fingers rest on the phone without touching the screen. Only her eyes move, screen to her own hand and back. Then the finger goes heavy — the hand does not move, but it seems to carry more, a stillness that becomes weight. Her lips part on the question and close again. The phone never moves by itself and never glitches, flickers or distorts; its screen content does not scroll or type, only ニジ's rainbow colors drifting slowly blue to green to blue. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; the screen, her hands, or her eyes are sharp, the rest falls away. Slow and deliberate, nearly still. [0:00–0:08] locked close on the screen and the younger face inside it, optionally an imperceptibly slow push-in. [0:08–0:15] a slight, slow cut to her face lit from below, then back to the screen — a quiet two-shot rhythm. [0:15–0:22] a slow tilt down to her hand and the phone, rack focus onto the finger in the screen's light. [0:22–0:30] hold on the finger, then a slow pull back to bring the finger and the younger face into one frame; cut to black on the finger.

## Audio Prompt

Almost silent. Deep quiet night room tone and a wall clock ticking, dry and discrete, growing louder in the held beats. The soft friction of her palms against the phone's case as she shifts her grip once, when the finger grows heavy. Three spoken lines, quiet and close: ニジ says おまえが誰かに預けた時間。それが、集まると、こういうのができるんだよ。 — 真白 asks 預けるって、何 — ニジ answers 時間を渡すってこと。おまえは、毎日、誰かに時間を渡してる。いいね、とか、既読、とか、返事、とか。そういうの、ぜんぶ時間だよ。 ニジ's speech has no 「わたし」, no first-person self-reference, and she calls 真白 「おまえ」. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as the finger grows heavy, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparency, no translucency, no see-through body, no わたし in ニジ's speech, no first-person self-reference, no name spoken before S12, no standing in the room at human scale, no figure outside the phone screen, no full-height apparition, no glowing eyes, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep03-seg02-30s-01`
- Segment ID: `S11`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_03, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 8s / 7s / 7s / 8s. Explanation = BEAT 1–2 at 15s (50%)`
- Camera Events: `4 events as listed in §10. One slow tilt (0:15–0:22)`
- Action Events: `ACT_LISTEN → ACT_ASK → ACT_HEAVY → ACT_GAZE`
- Audio Events: `three spoken lines ／ no 「わたし」 from ニジ ／ clock ticking throughout`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut to black on the heavy finger`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The model lets ニジ say 「わたし」.** The single most damaging failure for S11–S13. Her speech must never self-reference in the first person. Check the audio line by line.
- **The model makes ニジ transparent.** She is fully opaque, inside the screen. Verify no translucency.
- **The model invents on-screen text.** This segment has no screen text — the screen carries only her face. If message bubbles or captions appear, regenerate.
- **The heaviness reads as nothing.** The finger growing heavy is the emotional peak and it is stillness. If it does not read, lengthen the hold and tighten the frame on the hand.

## Changes

- _(none yet)_

## Next Generation

- If the heaviness reads, this segment carries the world's rule — いいね、既読、返事 are all time — and S12 turns to the naming.
