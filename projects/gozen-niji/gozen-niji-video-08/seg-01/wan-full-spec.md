# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第8話 S32「集まった姿」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「輪郭の明瞭さ」への気づき——音のない反芻だけが動く休止点（指の背骨の第32本・指は休む）。ニジは在る（画面の中だけ・完全に不透明・輪郭がこれまでで最も明瞭）。登場人物は真白とニジのみ。画面文字なし。S33 で初めてニジの指が透けるのは、この1本で「明瞭」を刻むから。**

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

> **ニジ appears this segment**（ledger S32 — 在・輪郭がこれまでで最も明瞭）. 真白とニジのみが人物。美月・小春・湊は登場しない。

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
- Appearance: `No message text this segment — only ordinary UI: the dark, otherwise empty screen holding ニジ inside it, no message, no chat thread, no text. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_08_わたしは、おまえが預けた時間.md`
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

真白 repeats the sentence in her head — 預けた時間が、集まった姿 — and looks again at ニジ in the screen, who tonight is clearer than she has ever been.

## Beginning

The line from S31 still hangs in the air. 真白 mouths it silently, once, without voice. The dark room; the phone light is the only light. ニジ sits in the screen, knees drawn up.

## Turn

「……どういう意味」 「そのままの意味だよ」 — and in the pause, 真白 notices: today the outline is clear. 真白's face, 真白's voice, but someone who is not 真白. ニジ, inside the screen, looks up at her.

## Peak

The clearest she has ever been. The rainbow afterimage has settled into an outline — longer lashes, slightly fuller cheeks, the same way of tilting her head. ニジ looks up, and 真白 cannot look away from her own face, one step younger.

## Pull（引き — 切れ目）

「そのままの意味だよ」 explains nothing. Cut on ニジ's face, looking up at her, clearer than ever. どういう意味 — left hanging.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The outline reveal holds 9s (30%); the rumination holds 7s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「反芻」 — ESTABLISH.** Dark bedroom, 2:00 A.M. 真白 mouths the sentence silently, once — 預けた時間が、集まった姿. Her lips move without sound. The phone light is the only light; her face nearly silhouetted. _Density: SPARSE — a held silence, no event._
- **BEAT 2 `[0:07–0:15]` — 「どういう意味」.** 真白 asks 「……どういう意味」, quiet, almost to herself. ニジ answers 「そのままの意味だよ」 — the same words, no more. In the pause, 真白's eyes move over ニジ and stop. _Density: TRANSITION — two lines of speech, then a stillness._
- **BEAT 3 `[0:15–0:24]` — 「輪郭」 — REVEAL, longest share.** Inside the screen, ニジ is the clearest she has ever been. The rainbow afterimage has settled into a crisp outline: 真白's own face, one step younger. Knees drawn up, looking up at her. 真白's eyes hold on that face. She does not blink. _Density: DENSE at the head, then the face alone, held._
- **BEAT 4 `[0:24–0:30]` — 「そのまま」.** ニジ's face, looking up, clearer than ever. The answer explains nothing. 真白's eyes stay on it. Cut on the face. Nothing after it. _Density: HELD — then a clean cut on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the rumination of the sentence (≈0:03) ／ 「……どういう意味」 (≈0:08) ／ the clearest outline, looking up (≈0:16, then held)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the rumination), 0:24–0:30 (the held gaze)`
- Dense regions: `0:15–0:24 (the outline reveal)`
- Long continuous action: `0:15–0:24 the two faces held together through the glass`
- Rapid transitions: `none — a slow, still night`

---

# 9. ACTION

## Action — ACT_MOUTH

- ID: `ACT_MOUTH`
- Subject: `MASHIRO`
- Action: `Mouths the sentence silently — 預けた時間が、集まった姿 — once, lips moving without sound`
- Intention: `To make the sentence mean something by repeating it`
- Intensity: `Low`
- Speed: `Very slow, barely moving`

### Action Relationship

- Before: `—` (continues from S31's naming)
- After: `ACT_ASK`

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MASHIRO`
- Action: `Asks 「……どういう意味」, quiet, her eyes on the screen`
- Intention: `To get an answer she can hold`
- Intensity: `Medium, internal`
- Speed: `Slow`

### Action Relationship

- Before: `ACT_MOUTH`
- After: `ACT_NOTICE`

## Action — ACT_NOTICE

- ID: `ACT_NOTICE`
- Subject: `MASHIRO`
- Action: `Eyes move over ニジ and stop — she registers the clear outline as a stillness, not a reaction`
- Intention: `None — the noticing happens by itself`
- Intensity: `HIGH (the reveal, expressed as held eyes)`
- Speed: `Zero — the eyes simply stop moving`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_LOOKUP`

## Action — ACT_LOOKUP

- ID: `ACT_LOOKUP`
- Subject: `NIJI`
- Action: `Sits with knees drawn up and looks up at 真白 through the glass, held`
- Intention: `Not to persuade — to wait. She has said all she will say`
- Intensity: `Medium, unguarded`
- Speed: `Still — only the slow drift of the rainbow`

### Action Relationship

- Before: `ACT_NOTICE`
- After: `— (cut on the face)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level, looking slightly down into the screen from 真白's side`
- Lens Character: `Long-ish, shallow. The room falls away into soft indigo`
- Depth of Field: `Shallow — ニジ's face sharp through the glass, the room soft behind`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Locked close on 真白's face, lit from below, lips barely moving. Optional: an imperceptibly slow push-in as she mouths the sentence.
- **`[0:07–0:12]`** — A slow tilt down into the screen — ニジ inside, knees drawn up. The two faces at the edge of the glass.
- **`[0:12–0:15]`** — Cut to 真白's eyes, still, held on the screen.
- **`[0:15–0:24]`** — Cut to ニジ inside the screen — clearest she has ever been — and hold. No push, no rack, no reframe. The face is the frame.
- **`[0:24–0:30]`** — Hold on ニジ's face, looking up. Cut on the face.

---

# 11. MOTION

## Subject Motion

- 真白's body holds; only her lips move, and only to mouth the sentence once, soundlessly
- 真白's eyes move once — over ニジ — and then stop
- ニジ's only movement is looking up, held, and the slow drift of her rainbow
- The rest is stillness. This is a held breath of a segment

## Object Motion

- The phone does not move on its own. Ever
- Screen content is static except the slow drift of ニジ's rainbow — blue to green to blue
- The wall clock's second hand advances in discrete ticks, out of focus behind

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand; the futon compresses under her`
- Inertia: `High — almost nothing moves at all`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by the smallest precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Incomprehension (the sentence repeated, still not landing)
- ↓ A question asked into the dark (「……どういう意味」)
- ↓ Recognition, unacknowledged (the outline is clear — and it is her own face)
- ↓ Held attention (the answer that explains nothing)

## Emotional Events

- Event: `The sentence mouthed once, silently` — Emotion: `Incomprehension — turning the words over, not yet feeling them` — Intensity: `LOW` — Timing: `≈0:03`
- Event: `「……どういう意味」` — Emotion: `A question asked, quietly, almost to herself` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:08`
- Event: `The clearest outline, looking up at her` — Emotion: `Recognition — 真白's own face, one step younger, and it will not look away` — Intensity: `HIGH, entirely in the eyes` — Timing: `≈0:16, held`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow is the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on the ceiling as a soft blue rectangle.
- **`[0:07–0:15]`** — As the camera tilts into the screen, ニジ's rainbow light dominates — the clearest and steadiest it has been in the whole series.
- **`[0:15–0:24]`** — ニジ's outline holds the frame; the room's dark is pushed furthest back.
- **`[0:30]`** — Cut on the face. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

- 真白: 「……どういう意味」 — quiet, almost to herself
- ニジ: 「そのままの意味だよ」 — calm, no more than the words

> The rumination of 預けた時間が、集まった姿 is **mouthed, not spoken, not narrated**. No voice-over.

## Sound Effects

- Deep quiet night room tone, almost nothing
- The wall clock's second hand, dry discrete ticks, faint throughout
- The soft friction of fabric, once, as 真白 shifts

## Environment

- Deep quiet night room tone. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the exchange. It thins as the camera finds ニジ's face, leaving only room tone and the clock`

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

- ニジ is **present** — inside the screen only, fully opaque, her outline the clearest it has been in the series
- ニジ is 真白's own face, one step younger — longer lashes, slightly fuller cheeks, the same head-tilt
- ニジ sits with knees drawn up, **looking up** at 真白 — the first time the power sits on 真白's side
- The rumination of 預けた時間が、集まった姿 is mouthed, not spoken and not shown as on-screen text
- End by cutting on ニジ's face, looking up, clearer than ever, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 S32 レンジより）

- **No full-body transparency.** ニジ is opaque here — no translucent body, no see-through torso or face, no fading, no dissolving, no disappearing. The transparency curve begins later, and only at the fingers
- **No figure in the room.** ニジ never stands in the room at human scale; she is inside the screen only
- **No other faces.** 真白 and ニジ are the only figures in the segment
- **No generic ghost.** ニジ is not a horror ghost — no ghostly glow, no spectral aura, no glowing eyes
- Do not have 真白 cry, gasp, or widen her eyes; the recognition registers as held eyes

## PREFER

- Holds over movement; when in doubt, do less
- The rumination silent over voiced
- Negative space over detail; the room may be nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in during beat 1 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear inside the screen only, fully opaque, her outline the clearest it has been in the series (ledger S32 — 在・輪郭がこれまでで最も明瞭); no full-body transparency, no figure in the room, no other faces. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M., with a figure inside her phone screen. Beats, deliberately uneven: [0:00–0:07] 真白 mouths the sentence silently, once — 預けた時間が、集まった姿 — her lips moving without sound, the screen the only light; [0:07–0:15] she asks ……どういう意味 and the figure answers そのままの意味だよ, and in the pause her eyes move over it and stop; [0:15–0:24] THE REVEAL — inside the screen the figure is the clearest it has ever been, 真白's own face one step younger with knees drawn up, looking UP at her, the rainbow afterimage settled into a crisp outline, and she cannot look away; [0:24–0:30] そのままの意味だよ explains nothing, and the shot cuts on the figure's face looking up at her. The outline reveal holds the largest share of the duration. Ends on the face, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: inside the phone screen only — 真白's own face one step younger, longer lashes and slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — a rainbow afterimage resolved into a clear, fully opaque outline, no shadow anywhere, blue drifting slowly to green and back, the clearest she has ever been; never standing in the room at human scale. Night is deep indigo lit solely by the cold blue-white screen. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost nothing moves. 真白's body holds; her lips move only to mouth the sentence once, soundlessly. Her eyes move once, over the figure, and then stop. ニジ's only movement is looking up, held, and the slow drift of her rainbow — blue to green to blue, never shimmering or pulsing. Ordinary weight and inertia; the phone has heft, the futon compresses. The phone never moves by itself and never glitches, flickers or distorts; its screen is static except the rainbow's drift. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level, looking slightly down into the screen from 真白's side. Longish lens, shallow depth of field; ニジ's face sharp through the glass, the room soft behind. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] locked close on 真白's face lit from below, lips barely moving, optionally an imperceptibly slow push-in. [0:07–0:12] a slow tilt down into the screen to ニジ, knees drawn up, the two faces at the edge of the glass. [0:12–0:15] cut to 真白's eyes, still, held on the screen. [0:15–0:24] cut to ニジ inside the screen — clearest she has ever been — and hold, no push, no rack, no reframe. [0:24–0:30] hold on ニジ's face looking up; cut on the face.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, faint throughout. The soft friction of fabric, once, as 真白 shifts. Two lines of dialogue only: 真白 asks ……どういう意味 quiet, almost to herself; ニジ answers そのままの意味だよ calm, no more than the words. The sentence 預けた時間が、集まった姿 is mouthed, not spoken and not narrated — no voice-over. Music extremely sparse — a few sustained tones at most — thinning as the camera finds ニジ's face and leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no fully transparent figure, no translucent body, no see-through torso, no see-through face, no fading figure, no dissolving, no disappearing, no vanishing, no full-body transparency, no second person in the room, no full-body figure in the room, no figure stepping out of the phone, no ghostly glow, no spectral aura, no generic anime ghost girl, no spirit girl, no other faces, no extra person, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep08-seg01-30s-01`
- Segment ID: `S32`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_08, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 8s / 9s / 6s. Outline = BEAT 3 at 9s (30%)`
- Camera Events: `5 events as listed in §10. No sustained dolly; all static, drift, or tilt`
- Action Events: `ACT_MOUTH → ACT_ASK → ACT_NOTICE → ACT_LOOKUP`
- Audio Events: `two lines of dialogue ／ clock ticking faint ／ no voice-over`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the face`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The outline may not read as "clearest ever".** This is a continuity fact, not a beauty fact — if ニジ just looks ordinary, the "one step younger" contrast must be pushed (longer lashes, fuller cheeks, same head-tilt).
- **The model may make her transparent.** "Ghost in a phone" is a strong prior toward see-through figures. The negative prompt front-loads the full-body-transparency ban; verify frame by frame.
- **The model may put her in the room.** ニジ never leaves the screen. This is the single most damaging failure for the whole series.
- **The rumination may be voiced.** 真白 must mouth the sentence, not speak it. If the model voices it, strip the audio.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the outline reads clearly and she stays in the screen, this segment is done; the clarity it establishes is what S33's transparent fingers will cost against.
