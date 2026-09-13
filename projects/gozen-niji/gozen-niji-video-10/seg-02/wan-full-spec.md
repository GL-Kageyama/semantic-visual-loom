# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第10話 S42「あの子」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「止まる」——S41 で下から返してきた指が、最後に残った一つの名前「あの子」の上で長く止まる（指の背骨の第42本）。返すのが怖かった止まり。ニジは画面の中だけ・輪郭がほとんど消えかけ。中学の友人は顔を出さない（名前と文字のみ、思い出の中でも）。画面文字は「元気にしてますか。急にごめんね。」。**

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

> **ニジ appears this segment**（ledger 41–45 — outline almost gone）. 中学の友人は顔を出さない（名前と文字のみ）.

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
- Appearance: `One short message in the box, character-for-character: 元気にしてますか。急にごめんね。 Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
- Continuity Importance: `HIGH`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads short of 2:00 at the hinge of the night`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_10_疎遠になった、あの人のところへ.md`
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

The 宛先リスト open, reduced to one name — あの子, the middle-school friend. 真白's finger stops long over it. A short message, a year late, sits in the box: 元気にしてますか。急にごめんね。

## Beginning

From the beat before, the last remaining name. She opens the old thread — the middle-school friend's name, at the very bottom of the list, where it has stayed all along. The short message is already composed.

## Turn

The finger stops long over the name. 元気にしてますか。急にごめんね。 — a year late, two years since she spoke her true feelings to this person and was recoiled from. The name is the one she feared returning to most.

## Peak

The recollection. あの子 — the one she walked to the station with every morning, the one she sat side by side with on the rooftop at lunch, the first and last person she ever put her true feelings into words for.

## Pull（引き — 切れ目）

She stands before the send button, the finger still stopped over the name. Cut on the name and the stopped finger, the message unsent. 私が引かれた相手に、今さら、何を送るの — left hanging.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The stop over the name holds 11s (37%); the recollection holds 8s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「宛先を開く」 — ESTABLISH.** The list, one name at the bottom. She opens the old thread. In the box, the short message: 元気にしてますか。急にごめんね。 _Density: SPARSE — quiet UI movement, no event._
- **BEAT 2 `[0:07–0:18]` — 「名前の上で止まる」 — longest share.** Her finger stops long over the name — あの子, the middle-school friend. The name at the bottom, where it has stayed all along. The finger does not move. Hold longer than is comfortable. _Density: SPARSE, inverted — the event is the absence of motion._
- **BEAT 3 `[0:18–0:26]` — 「あの子」.** The recollection: walked to the station together in the morning, sat side by side on the rooftop at lunch, the first and last person she spoke her true feelings to. _Density: TRANSITION — memory, no motion but the eyes going distant._
- **BEAT 4 `[0:26–0:30]` — 「送信の前」.** The finger still stopped. The send button before her. Cut on the name and the stopped finger. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the short message (≈0:04) ／ the finger stopping over the name (≈0:08, then held) ／ the recollection (≈0:19)`

## Temporal Density

- Sparse regions: `0:00–0:07 (opening the thread), 0:07–0:18 (the held stop)`
- Dense regions: `0:18–0:26 (the recollection)`
- Long continuous action: `0:07–0:18 the stopped finger`
- Rapid transitions: `none — the slowest, most held segment of the episode`

---

# 9. ACTION

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MASHIRO`
- Action: `Opens the old thread from the list — the middle-school friend's name at the bottom`
- Intention: `To face the last remaining name`
- Intensity: `Low`
- Speed: `Steady, practiced — the same mechanical tap as always`

### Action Relationship

- Before: `— (continues from S41's last name)`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `MASHIRO`
- Action: `The finger stops long over the name — あの子 — and does not move`
- Intention: `None — the body arrives before the decision. This is the stop she feared`
- Intensity: `CRITICAL (the emotional peak, expressed as stillness)`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_OPEN`
- After: `ACT_REMEMBER`
- Causes: `ACT_REMEMBER`

## Action — ACT_REMEMBER

- ID: `ACT_REMEMBER`
- Subject: `MASHIRO`
- Action: `The eyes go distant; the recollection surfaces — the walk to the station, the rooftop, the true feelings`
- Intention: `To weigh what this name was to her`
- Intensity: `Medium, suppressed`
- Speed: `Still; only the eyes move, and barely`

### Action Relationship

- Before: `ACT_STOP`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `MASHIRO`
- Action: `The finger remains stopped over the name; the send button before her, un-pressed`
- Intention: `To stand before the send — not yet to send`
- Intensity: `Medium, internal`
- Speed: `Held, then cut`

### Action Relationship

- Before: `ACT_REMEMBER`
- After: `— (cut on the name)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Very shallow — often only the screen or the fingers are sharp`
- Camera Style: `Slow, deliberate, almost still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Locked close on the screen and hand. The thread opens; the short message sits in the box. Optional: an imperceptibly slow push-in.
- **`[0:07–0:18]`** — Absolutely locked on the name and the stopped finger above it. No camera movement at all. Hold longer than is comfortable.
- **`[0:18–0:22]`** — Cut to her face, lit from below, the eyes distant — the recollection. Static, close.
- **`[0:22–0:26]`** — A very slow drift back to the screen, the name and the stopped finger.
- **`[0:26–0:30]`** — Hold on the name and the finger; the send button visible above. Cut on the name. Nothing after it.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially all the movement; the rest of her body holds
- The stop is absolute: not a slowing, not a hesitation — the finger stops over the name and stays
- During the recollection, only her eyes move, and barely; her expression never resolves
- The final hold is the same stopped finger, unchanged

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a thread opening. Nothing glitches, flickers, distorts, or behaves supernaturally
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion
- ニジ's rainbow afterimage drifts faintly, blue → green → blue, in the corner of the screen
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers — until the stop, which is instantaneous`
- Acceleration: `Gentle everywhere except the stop`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes. The segment's only impact is a hand ceasing to move`

---

# 12. EMOTION

## Emotional Arc

- Quiet intent (opening the last thread)
- ↓ The stop she feared (the finger over あの子's name)
- ↓ The weight of memory (the walk, the rooftop, the true feelings)
- ↓ Unresolved dread (standing before the send button)

## Emotional Events

- Event: `The finger stops over the name` — Emotion: `The stop she feared — not surprise, but the name she dreaded returning to` — Intensity: `CRITICAL — expressed only as stillness. No facial performance` — Timing: `≈0:08, held to 0:18`
- Event: `The recollection of あの子` — Emotion: `The weight of what this name was — the first and last person she told her true feelings` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:19`
- Event: `The send button, un-pressed` — Emotion: `Unresolved dread — 何を送るの, left hanging` — Intensity: `MEDIUM` — Timing: `≈0:27`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow, now thin and faint, is the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on the ceiling as a soft blue rectangle.
- **`[0:07–0:18]`** — The light holds steady on the name and the stopped finger; ニジ's faint afterimage adds a thin, dim wash of color at the corner.
- **`[0:18–0:22]`** — Cut to her face, lit from below, almost to silhouette — the eyes in shadow.
- **`[0:26–0:30]`** — Light unchanged. Cut on the name.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The message and the memory are not spoken, not whispered, not read aloud. No narration, no voice-over.

## Sound Effects

- The soft friction of a thumb on glass through beat 1 — then its **conspicuous absence** at 0:08, an audible hole in the mix, the moment the finger stops
- The wall clock's second hand, dry discrete ticks, present throughout, growing louder in the held beats
- Soft futon fabric as she shifts, once, at the very start

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved, faintly weighted. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness, then **withdraw**. Music thins as the finger stops, and is entirely gone by the recollection, leaving only room tone and the clock`

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

- Render the on-screen Japanese exactly: `元気にしてますか。急にごめんね。` — the short message in the box
- Let the finger stop long over the name, and hold on it longer than is comfortable. This is the emotional peak, and it is stillness
- Render ニジ present: 真白's own face one step younger, a rainbow afterimage **inside the screen only**, with an **almost-faded outline** (輪郭がほとんど消えかけ)
- End by cutting on the name and the stopped finger, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 41–45 レンジより）

- **Do not show the middle-school friend's face or figure.** No face, no body, no silhouette of her — the name and text only, even in the recollection
- **Do not let ニジ stand in the room.** She exists only inside the screen, never at human scale
- **Do not make ニジ fully opaque, and do not let her vanish entirely** — her outline is almost faded, but still present
- No voice for the message or the memory — it is not read aloud, whispered, or narrated
- No additional on-screen text beyond the message and the ordinary UI (no captions, no subtitles burned in)

## PREFER

- Framing the name large, straight-on and held rather than skimmed — the stop is the whole point here
- Silence over score at the peak
- Holds over movement; when in doubt, do less
- The room nearly empty; negative space over detail

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in during beat 1 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear only inside the screen as an almost-faded outline (ledger 41–45 — outline almost gone), never at human scale; the middle-school friend's face and figure must never be shown — name and text only, even in the recollection. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:07] the 宛先リスト is reduced to one name at the bottom, she opens the old thread, and a short message sits in the box reading 元気にしてますか。急にごめんね。; [0:07–0:18] THE PEAK — her finger STOPS long over the name, あの子, the middle-school friend, and is held motionless, longer than is comfortable; [0:18–0:26] the recollection — she walked to the station with her every morning, sat side by side on the rooftop at lunch, and she is the first and last person she spoke her true feelings to; [0:26–0:30] the finger still stopped, the send button before her, and the shot cuts on the name. The stop holds the largest share of the duration. Ends on the name and the stopped finger, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — a blurred rainbow afterimage, drifting slowly blue → green → blue, existing only inside the screen, never in the room at human scale, no shadow. Her outline is almost faded away (輪郭がほとんど消えかけ): the afterimage thin and faint, barely there, on the verge of dissolving. The phone screen shows an ordinary Japanese UI in cold blue-white — a thread with a single name at the bottom, and in the box one short message reading exactly 元気にしてますか。急にごめんね。 No face, no figure, no body of the middle-school friend — name and text only, even in the recollection. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers; the body holds still. The thumb taps once to open the thread, then STOPS instantaneously and completely over the name and is held motionless — moving, then not moving, no slowing and no hesitation. During the recollection only her eyes move, and barely. ニジ's rainbow afterimage drifts faintly, blue → green → blue, in the corner of the screen. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere except that one instantaneous stop. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the fingers are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] locked close on the screen and hand as the thread opens, the short message in the box, optionally an imperceptibly slow push-in. [0:07–0:18] absolutely locked on the name and the stopped finger, no camera movement, held longer than is comfortable. [0:18–0:22] cut to her face lit from below, the eyes distant, static. [0:22–0:26] a very slow drift back to the screen, the name and the stopped finger. [0:26–0:30] hold on the name and the finger, the send button visible above; cut on the name.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, present throughout and growing louder in the held beats. The soft friction of a thumb on glass through the opening — and its conspicuous absence, an audible hole in the mix, the moment the finger stops. Soft futon fabric movement once at the start. No spoken words at all — the message and the memory are not read aloud, not whispered, not narrated. No voice-over. Music extremely sparse — a few sustained tones at most — thinning as the finger stops and entirely gone by the recollection, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no face of the middle-school friend, no figure of the middle-school friend, no body of the middle-school friend, no depiction of the middle-school friend as a person, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep10-seg02-30s-01`
- Segment ID: `S42`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_10, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 11s / 8s / 4s. Stop = BEAT 2 at 11s (37%)`
- Camera Events: `5 events as listed in §10. One cut, one slow drift; all else static or held`
- Action Events: `ACT_OPEN → ACT_STOP → ACT_REMEMBER → ACT_HOLD`
- Audio Events: `no dialogue ／ clock ticking throughout ／ music gone by the recollection`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the name`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The stop may not read.** A generated finger may keep moving or drift. The instantaneous stop plus the long hold is the peak; if it does not read, lengthen the hold first.
- **The model may draw the middle-school friend's face in the recollection.** "The person I told my feelings to" is a strong prior for a flashback portrait. The negative prompt front-loads this; verify frame by frame — no face, no figure, name and text only.
- **Japanese text rendering.** The message `元気にしてますか。急にごめんね。` carries the segment. If it renders as noise, the segment fails; if unusable, generate the screen as a plate and composite the text in post.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the stop and the message both read, this segment hands the unresolved dread straight into S43, where the finger begins the typing-and-erasing that this stop foreshadows.
