# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第3話 S12「ニジ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**名前の瞬間——名前は意味でなく「虹色してるから」と、色から生まれる。指は画面に触れず、声だけで誰かに「名前」を与える初めての所作。ニジは「ニジ、ね。……いい名前」と繰り返し、真白よりずっと正直な、泣きそうに笑う。**

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
- Appearance: `No message text this segment — no UI, no bubbles, no notification. The screen carries only ニジ's face and the rainbow afterimage drifting in its corner, on a dark empty screen`
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

真白 gives the ghost a name. She looks at the rainbow drifting in the corner of the screen — 青から、緑から、また青へ — and says 「……ニジ。虹色してるから。」 ニジ repeats it, delighted, and smiles 泣きそうに笑う — a smile on the verge of tears.

## Beginning

The dialogue has settled. 真白 asks 「名前、ないの？」 ニジ answers 「ないよ。おまえが、つけて。」 The younger face in the screen tilts its head — the same way 真白 does in the mirror.

## Turn

真白 hesitates: 「……勝手に、つけていいの。」 ニジ: 「いいよ。だって、おまえのものだもん。」 真白 looks at the screen — the rainbow afterimage in the corner, its colors drifting slowly. 青から、緑から、また青へ。

## Peak

「……ニジ。」 The ghost tilts her head: 「ニジ？」 真白: 「虹色してるから。……ニジ。」 The thing in the screen — now ニジ — repeats the name, once, as if tasting it.

## Pull（引き — 切れ目）

「ニジ、ね。……いい名前。」 ニジ smiles — more honestly than 真白 ever can — and it is a smile on the verge of tears. Cut on that smile.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The naming holds 8s (27%); the rainbow-watching holds 9s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:09]` — 「名前、ないの？」 — the request.** 真白: 名前、ないの？ ニジ: ないよ。おまえが、つけて。 真白: ……勝手に、つけていいの。 ニジ: いいよ。だって、おまえのものだもん。 _Density: DENSE — the exchange that grants the naming._
- **BEAT 2 `[0:09–0:18]` — 「虹色」.** 真白 looks at the screen — the rainbow afterimage in the corner, its colors drifting slowly. 青から、緑から、また青へ。 _Density: SPARSE, held — the name is born from the color._
- **BEAT 3 `[0:18–0:26]` — 「ニジ」 — PEAK, the naming.** ……ニジ。 ニジ？ 虹色してるから。……ニジ。 The ghost repeats the name, once, as if tasting it. _Density: DENSE at the head (the naming), then held._
- **BEAT 4 `[0:26–0:30]` — 「いい名前」.** ニジ、ね。……いい名前。 ニジ smiles — more honestly than 真白 can — a smile on the verge of tears. Cut on the smile. _Density: HELD — then cut precisely on the pull. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the granting おまえが、つけて (≈0:03) ／ the rainbow drifting 青→緑→青 (≈0:12) ／ the naming ……ニジ (≈0:19) ／ the smile (≈0:27)`

## Temporal Density

- Sparse regions: `0:09–0:18 (the rainbow-watching)`
- Dense regions: `0:00–0:09 (the request), 0:18–0:26 (the naming)`
- Long continuous action: `0:09–0:18 the slow drifting of the rainbow, watched`
- Rapid transitions: `none — a gentle, held segment`

---

# 9. ACTION

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MASHIRO`
- Action: `Asks 「名前、ないの？」, the phone in both hands, her fingers resting, not touching the screen`
- Intention: `To give the thing in the screen a name — the first thing she chooses to do`
- Intensity: `Medium`
- Speed: `Slow, careful`

### Action Relationship

- Before: `—` (continues from S11's unlanded meaning)
- After: `ACT_LOOK`

## Action — ACT_LOOK

- ID: `ACT_LOOK`
- Subject: `MASHIRO`
- Action: `Looks at the rainbow afterimage in the corner of the screen, its colors drifting slowly — 青から、緑から、また青へ`
- Intention: `To find the name in what she sees`
- Intensity: `Low, sustained`
- Speed: `Still. Only her eyes move`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_NAME`

## Action — ACT_NAME

- ID: `ACT_NAME`
- Subject: `MASHIRO`
- Action: `Names her — 「……ニジ。虹色してるから。……ニジ」 — the fingers never touching the screen`
- Intention: `To give the ghost a name, and with it a hold on her`
- Intensity: `CRITICAL (the naming — an act done by voice, not by touch)`
- Speed: `Slow, and quiet`

### Action Relationship

- Before: `ACT_LOOK`
- After: `ACT_GAZE`

## Action — ACT_GAZE

- ID: `ACT_GAZE`
- Subject: `MASHIRO`
- Action: `Watches as ニジ repeats the name and smiles — 泣きそうに笑う, a smile on the verge of tears`
- Intention: `To see what she has just given her`
- Intensity: `Medium, suppressed`
- Speed: `Very slow`

### Action Relationship

- Before: `ACT_NAME`
- After: `— (cut on the smile)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. The screen or her face are sharp; the room falls away`
- Depth of Field: `Very shallow — the room is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. The one move belongs to the name`

## Camera Events

- **`[0:00–0:09]`** — Locked close on the screen and the younger face inside it. The exchange plays out in a quiet two-shot rhythm between the screen and her face, lit from below.
- **`[0:09–0:18]`** — A slow push toward the corner of the screen where the rainbow afterimage drifts — 青から、緑から、また青へ. The color fills the frame softly.
- **`[0:18–0:26]`** — Cut to her face, lit from below, as she names her — then back to the screen, where ニジ repeats the name.
- **`[0:26–0:30]`** — Locked on ニジ's face as she smiles, on the verge of tears. Cut to black on the smile.

---

# 11. MOTION

## Subject Motion

- Her fingers rest on the phone, never touching the screen — the whole segment turns on this stillness
- Only her eyes move: to the screen, to the drifting rainbow, back to the face
- Her lips form the name with effort, quietly; nothing else moves
- ニジ's head tilts — the same way 真白 tilts her own in the mirror

## Object Motion

- The phone does not move on its own. Ever
- Screen content does not scroll, type, or distort. Only the rainbow afterimage drifts, its colors changing slowly — blue to green to blue
- The wall clock's second hand advances in discrete ticks, faint, out of focus

## Environmental Motion

- The screen's bloom breathes very slightly — the only continuous motion
- Nothing in the room moves. The curtain does not stir

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes. The only impact is a name, given by voice`

---

# 12. EMOTION

## Emotional Arc

- A quiet decision (asking for the name)
- ↓ Finding it in the color (the drifting rainbow)
- ↓ The naming (……ニジ — a hold on her)
- ↓ A smile on the verge of tears (what the name gave her)

## Emotional Events

- Event: `おまえが、つけて` — Emotion: `Permission — the name is hers to give` — Intensity: `MEDIUM` — Timing: `≈0:03`
- Event: `The rainbow drifting 青→緑→青` — Emotion: `The name found in the color, not the meaning` — Intensity: `MEDIUM, quiet` — Timing: `≈0:12`
- Event: `……ニジ` — Emotion: `The naming — the first hold on the ghost` — Intensity: `CRITICAL` — Timing: `≈0:19`
- Event: `ニジ's smile — 泣きそうに笑う` — Emotion: `Joy that carries the edge of tears. The ghost does not cry — she smiles on the verge of it` — Intensity: `HIGH, withheld` — Timing: `≈0:27`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow is the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on, ニジ's rainbow drifting softly inside the glass.
- **`[0:09–0:18]`** — As the camera closes on the rainbow, its color fills the frame — the only saturated light in the dark, and it is gentle, not luminous.
- **`[0:18–0:26]`** — Her face lit from below as she names her; the screen's light the whole of the frame.
- **`[0:30]`** — Cut to black on the smile. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

- 真白: 「名前、ないの？」
- ニジ: 「ないよ。おまえが、つけて」
- 真白: 「……勝手に、つけていいの」
- ニジ: 「いいよ。だって、おまえのものだもん」
- 真白: 「……ニジ」 ／ ニジ: 「ニジ？」 ／ 真白: 「虹色してるから。……ニジ」
- ニジ: 「ニジ、ね。……いい名前」

> ニジ's speech carries **no 「わたし」** — no first-person self-reference. She calls 真白「おまえ」, ending with a period. No narration, no voice-over.

## Sound Effects

- The wall clock's dry discrete ticking, present throughout
- The faint, soft sound of her breath as she forms the name
- Almost nothing else — the naming is carried by the voices alone

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender. Never sinister, never sentimental — no swelling, no sting`
- Emotional Function: `Hold the room's stillness, then thin to nothing at the smile, leaving only room tone and the clock`

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
- ニジ's dialogue — exactly: `ないよ。おまえが、つけて` ／ `いいよ。だって、おまえのものだもん` ／ `ニジ、ね。……いい名前`
- 真白's naming — exactly: `……ニジ` ／ `虹色してるから。……ニジ`
- The fingers never touch the screen — the naming is an act of voice, not touch
- Show ニジ's smile as 泣きそうに笑う — a smile on the verge of tears. She does **not** cry
- End on the smile, cut to black, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 11–13 レンジより）

- **No transparency.** ニジ is fully opaque
- **No 「わたし」 from ニジ.** No first-person self-reference in her speech
- **No actual crying.** The smile may carry the edge of tears, but no tears fall, no sobbing
- **No ghost in the room.** No apparition at human scale, no second body outside the screen
- No supernatural VFX — no glitch, no particles, no light rays. The rainbow is a smudged afterimage
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The name carried in stillness — long holds, few cuts
- The rainbow's slow color-drift over any explicit explanation of the name
- Silence over score at the smile

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The push toward the rainbow may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ is present, fully opaque, inside the screen only (ledger 11–13); her name is given here, by 真白, born from the rainbow's color. No transparency, no 「わたし」 in her speech, no crying. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at night, holding her phone in both hands. Beats, deliberately uneven: [0:00–0:09] she asks 名前、ないの？, and the younger face in the screen answers ないよ。おまえが、つけて — and grants いいよ。だって、おまえのものだもん; [0:09–0:18] she looks at the rainbow afterimage drifting in the corner of the screen, its colors changing slowly — 青から、緑から、また青へ; [0:18–0:26] THE PEAK — she names her ……ニジ。虹色してるから。……ニジ, and the ghost repeats the name as if tasting it; [0:26–0:30] ニジ smiles — ニジ、ね。……いい名前 — a smile on the verge of tears, and the shot cuts to black on that smile. The naming holds the largest share of the duration. Ends on the smile, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ is 真白's own face one step younger (longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head), a rainbow afterimage INSIDE the phone screen, never standing in the room at human scale, with no shadow anywhere, fully opaque. Her colors drift slowly, blue to green to blue. Her smile is more honest than 真白's — and at the end it is a smile on the verge of tears, but she does not cry. Night is deep indigo lit solely by one cold blue-white phone screen. No on-screen text, no message bubbles. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her fingers rest on the phone and never touch the screen; the whole segment turns on this stillness. Only her eyes move — to the screen, to the drifting rainbow, back to the face. Her lips form the name quietly. ニジ's head tilts — the same way 真白 tilts her own in the mirror — and her rainbow colors drift slowly, blue to green to blue. At the end her smile arrives, gentle and honest, on the verge of tears but not crying. The phone never moves by itself and never glitches, flickers or distorts; its screen content does not scroll or type. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; the screen or her face are sharp, the room falls away. Slow and deliberate, nearly still. [0:00–0:09] locked close on the screen and the younger face inside it, a quiet two-shot rhythm between the screen and her face lit from below. [0:09–0:18] a slow push toward the corner of the screen where the rainbow afterimage drifts — 青から、緑から、また青へ. [0:18–0:26] cut to her face lit from below as she names her, then back to the screen where ニジ repeats the name. [0:26–0:30] locked on ニジ's face as she smiles on the verge of tears; cut to black on the smile.

## Audio Prompt

Almost silent. Deep quiet night room tone and a wall clock ticking, dry and discrete, present throughout. The faint soft sound of her breath as she forms the name. The dialogue, quiet and close: 真白 — 名前、ないの？ ／ ……勝手に、つけていいの ／ ……ニジ ／ 虹色してるから。……ニジ. ニジ — ないよ。おまえが、つけて ／ いいよ。だって、おまえのものだもん ／ ニジ？ ／ ニジ、ね。……いい名前. ニジ's speech has no 「わたし」, no first-person self-reference, and she calls 真白 「おまえ」. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning to nothing at the smile, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparency, no translucency, no see-through body, no わたし in ニジ's speech, no first-person self-reference, no standing in the room at human scale, no figure outside the phone screen, no full-height apparition, no glowing eyes, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep03-seg03-30s-01`
- Segment ID: `S12`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_03, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 9s / 9s / 8s / 4s. Naming = BEAT 3 at 8s (27%)`
- Camera Events: `4 events as listed in §10. One slow push (0:09–0:18)`
- Action Events: `ACT_ASK → ACT_LOOK → ACT_NAME → ACT_GAZE`
- Audio Events: `the naming dialogue ／ no 「わたし」 from ニジ ／ clock ticking throughout`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut to black on the smile`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The model renders ニジ as a different person.** Her face must be 真白's own, one step younger. If she drifts into a separate character, the naming loses its meaning.
- **The model lets her cry.** She may smile on the verge of tears, but no tears fall. Verify the final smile does not resolve into weeping.
- **The model lets her say 「わたし」 or makes her transparent.** Both forbidden. Check audio and frames.
- **The rainbow reads as a light effect.** It must be a smudged, drifting afterimage — blue to green to blue — not rays, particles, or an aura.

## Changes

- _(none yet)_

## Next Generation

- If the smile reads as 泣きそうに笑う — honest joy carrying the edge of tears — this segment lands the naming; S13 turns to how she might go home.
