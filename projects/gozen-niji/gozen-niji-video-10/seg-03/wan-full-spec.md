# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第10話 S43「打っては消して」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「打っては消して」——S07 で回想された所作を、今度はあの子への一文で自分の指が実演する（指の背骨の第43本）。送信ボタンの前で入力中の文字が出ては消える。ニジは画面の隅で待つ（画面の中だけ・輪郭がほとんど消えかけ）。中学の友人は顔を出さない（名前と文字のみ）。画面文字なし。**

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
- Appearance: `No fixed text this segment — input text appearing and vanishing in the box, typed and erased. The exact strings are not canonical (diegetic, not reproduced); rendered only as ordinary Japanese UI, cold blue-white on dark UI`
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

Night. 真白 stands before the send button, the short message in the box. Her finger trembles. She begins to type, erases, begins again, erases — 打っては消して — the gesture she recalled in S07, now performed by her own hand, for あの子.

## Beginning

The composed message — 元気にしてますか。急にごめんね。 — sits in the box. Two years since she last spoke to this person, the one who recoiled when she put her true feelings into words.

## Turn

――私が引かれた相手に、今さら、何を送るの。 The finger trembles. It types, erases, types, erases — over and over, for one short message. 打っては消して。打っては消して。

## Peak

The repetition, and the shaking finger. In the corner of the screen, ニジ waits — almost faded, watching.

## Pull（引き — 切れ目）

――でも、真白は送った。 The finger stops trembling. The last erase is done; the short message is there. Cut on the finger, resolved — the send itself belongs to the next beat.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The typing-and-erasing holds 12s (40%) to engrave the gesture.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「送信の前」 — ESTABLISH.** The message in the box: 元気にしてますか。急にごめんね。 Two years since she spoke to this person; the one who recoiled. _Density: SPARSE — a held frame, no event yet._
- **BEAT 2 `[0:06–0:18]` — 「打っては消して」 — longest share.** The finger types, erases, types, erases — over and over. The input text appears and vanishes, appears and vanishes. The same gesture she knew with 美月, now for あの子. _Density: DENSE, rhythmic — the repetition is the whole event._
- **BEAT 3 `[0:18–0:25]` — 「震える指」.** The finger trembles. ニジ waits in the corner of the screen, her outline almost faded. _Density: TRANSITION — the tremor builds, then steadies._
- **BEAT 4 `[0:25–0:30]` — 「でも、送った」.** The last erase is done. The finger stops trembling. ――でも、真白は送った。 Cut on the finger, resolved. _Density: HELD — then a clean cut. The send itself is not shown._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the typing-and-erasing (0:06–0:18) ／ the trembling finger (≈0:20) ／ the resolution (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:06 (before the send), 0:25–0:30 (the resolution)`
- Dense regions: `0:06–0:18 (the typing-and-erasing)`
- Long continuous action: `0:06–0:18 the repeated typing and erasing`
- Rapid transitions: `the input text appearing and vanishing — the only fast element`

---

# 9. ACTION

## Action — ACT_STAND

- ID: `ACT_STAND`
- Subject: `MASHIRO`
- Action: `Stands before the send button, the short message in the box`
- Intention: `To send it — and not to send it`
- Intensity: `Medium, internal`
- Speed: `Still; the finger hovers`

### Action Relationship

- Before: `— (continues from S42's stopped finger)`
- After: `ACT_TYPE_ERASE`

## Action — ACT_TYPE_ERASE

- ID: `ACT_TYPE_ERASE`
- Subject: `MASHIRO`
- Action: `Types, erases, types, erases — over and over, one short message`
- Intention: `Not to write — to get through the sending. The gesture is older than the words`
- Intensity: `CRITICAL (the emotional peak, expressed as repetition)`
- Speed: `Small, quick, shaky — the same arc, over and over`

### Action Relationship

- Before: `ACT_STAND`
- After: `ACT_TREMBLE`
- Causes: `ACT_TREMBLE`

## Action — ACT_TREMBLE

- ID: `ACT_TREMBLE`
- Subject: `MASHIRO`
- Action: `The finger trembles over the keyboard; ニジ waits in the corner`
- Intention: `None — the body shaking before the decision`
- Intensity: `Medium`
- Speed: `A fine tremor, then steadying`

### Action Relationship

- Before: `ACT_TYPE_ERASE`
- After: `ACT_RESOLVE`

## Action — ACT_RESOLVE

- ID: `ACT_RESOLVE`
- Subject: `MASHIRO`
- Action: `The last erase is done; the finger stops trembling and settles over the send`
- Intention: `でも、真白は送った — the decision to send`
- Intensity: `Medium, internal`
- Speed: `A settle, then a cut — the send itself is not shown`

### Action Relationship

- Before: `ACT_TREMBLE`
- After: `— (cut on the finger)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Very shallow — often only the screen or the fingers are sharp`
- Camera Style: `Slow, deliberate, almost still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Locked close on the screen and hand. The message in the box. Optional: an imperceptibly slow push-in.
- **`[0:06–0:18]`** — Held close on the input box and the finger. The text appears and vanishes, appears and vanishes, under the same shaky arc.
- **`[0:18–0:25]`** — A slight, slow tilt to bring ニジ into frame at the corner of the screen, waiting, her outline almost faded.
- **`[0:25–0:30]`** — Return to the finger. The last erase, the tremor settling. Cut on the finger. The send itself is not shown.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially all the movement; the rest of her body holds
- The typing-and-erasing is small, quick, shaky — the same arc, over and over
- The tremor is fine and ceaseless, then settles once at the end
- ニジ's rainbow afterimage drifts faintly, blue → green → blue, waiting

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — text appearing in the input box and being deleted. Nothing glitches, flickers, distorts, or behaves supernaturally
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion besides ニジ's afterimage
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers — the typing-and-erasing is quick and nervous`
- Acceleration: `Gentle in the body, small and sharp in the fingers`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Dread (standing before the send button)
- ↓ The old gesture (typing and erasing, over and over)
- ↓ Trembling (the body shaking before the decision)
- ↓ Resolution (でも、真白は送った)

## Emotional Events

- Event: `The typing-and-erasing` — Emotion: `The old gesture — 打っては消して, the same one she knew with 美月` — Intensity: `CRITICAL — expressed as repetition, not as a face` — Timing: `0:06–0:18`
- Event: `The trembling finger` — Emotion: `The body shaking before the decision` — Intensity: `MEDIUM` — Timing: `≈0:20`
- Event: `The resolution` — Emotion: `でも、真白は送った — a decision made, not a release` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:26`

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
- **`[0:06–0:18]`** — The light flickers slightly, imperceptibly, as text appears and vanishes — the room's blue-white surface shifting with the erasing.
- **`[0:18–0:25]`** — ニジ's faint afterimage contributes a thin, dim wash of color at the corner.
- **`[0:25–0:30]`** — Light unchanged. Cut on the finger.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The hesitation is internal. No narration, no voice-over.

## Sound Effects

- The soft tap-tap of a thumb on glass, close, repeating — type, erase, type, erase, its rhythm the segment's pulse
- The faint electronic chime of text deleted, repeated with the tapping
- The wall clock's second hand, dry discrete ticks, faint under the taps

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tense in a quiet way. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the repetition. It thins as the finger settles, and is gone by the cut, leaving only room tone and the clock`

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

- Establish the typing-and-erasing — the finger types, erases, types, erases, over and over, the input text appearing and vanishing
- Render ニジ present: 真白's own face one step younger, a rainbow afterimage **inside the screen only**, waiting in the corner, with an **almost-faded outline** (輪郭がほとんど消えかけ)
- Let the finger tremble, then settle once
- End by cutting on the finger, resolved — **do not show the send itself**

## MUST NOT（この1本の禁止・開示台帳 41–45 レンジより）

- **Do not show the middle-school friend's face or figure.** No face, no body, no silhouette of her — the name and text only
- **Do not let ニジ stand in the room.** She exists only inside the screen, never at human scale
- **Do not make ニジ fully opaque, and do not let her vanish entirely** — her outline is almost faded, but still present
- No fixed on-screen text to reproduce (this segment's screen text is なし); the typed text is diegetic, appearing and vanishing, not a canonical string
- No second living person in the room

## PREFER

- The repetition uninterrupted for as long as possible — the whole segment is one held gesture
- Silence over score
- Negative space over detail; the room may be nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in during beat 1 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear only inside the screen as an almost-faded outline (ledger 41–45 — outline almost gone), never at human scale; the middle-school friend's face and figure must never be shown — name and text only. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:06] the short message 元気にしてますか。急にごめんね。 sits in the box, and she stands before the send button; [0:06–0:18] the finger types, erases, types, erases — over and over, the input text appearing and vanishing, the same gesture she knew with 美月, now for あの子; [0:18–0:25] the finger trembles, and ニジ waits in the corner of the screen, her outline almost faded; [0:25–0:30] the last erase is done, the finger stops trembling and settles, ――でも、真白は送った, and the shot cuts on the finger. The typing-and-erasing holds the largest share of the duration. Ends on the finger, resolved — the send itself is not shown. Nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — a blurred rainbow afterimage, drifting slowly blue → green → blue, existing only inside the screen, waiting in the corner, never in the room at human scale, no shadow. Her outline is almost faded away (輪郭がほとんど消えかけ): the afterimage thin and faint, barely there, on the verge of dissolving. The phone screen shows an ordinary Japanese UI in cold blue-white — a message box with 元気にしてますか。急にごめんね。 and the input text appearing and vanishing. No face, no figure, no body of the middle-school friend — name and text only. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers; the body holds still. The typing-and-erasing is small, quick and shaky — type, erase, type, erase — the same arc, over and over. The finger trembles finely, then settles once at the end. ニジ's rainbow afterimage drifts faintly, blue → green → blue, waiting in the corner. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration in the body, small and sharp in the fingers. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions — text appearing in the input box and being deleted. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the fingers are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked close on the screen and hand, the message in the box, optionally an imperceptibly slow push-in. [0:06–0:18] held close on the input box and the finger — the text appearing and vanishing under the same shaky arc. [0:18–0:25] a slight, slow tilt to bring ニジ into frame at the corner, waiting, her outline almost faded. [0:25–0:30] return to the finger, the last erase, the tremor settling; cut on the finger.

## Audio Prompt

Almost silent. Deep quiet night room tone. The soft tap-tap of a thumb on glass, close and repeating — type, erase, type, erase — its rhythm the segment's pulse. A faint electronic chime as text is deleted, repeated with the tapping. The wall clock's dry discrete ticking, faint under the taps. No spoken words at all — the hesitation is internal. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as the finger settles and gone by the cut, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no face of the middle-school friend, no figure of the middle-school friend, no body of the middle-school friend, no depiction of the middle-school friend as a person, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep10-seg03-30s-01`
- Segment ID: `S43`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_10, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 12s / 7s / 5s. Typing-and-erasing = BEAT 2 at 12s (40%)`
- Camera Events: `4 events as listed in §10. One slight tilt; all else static or held`
- Action Events: `ACT_STAND → ACT_TYPE_ERASE → ACT_TREMBLE → ACT_RESOLVE`
- Audio Events: `no dialogue ／ tap-tap of typing throughout ／ clock faint under the taps`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the finger`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The repetition may read as a loop, not as hesitation.** Each erase must land as a nervous act, not a glitch. If the text flickers or the motion looks random, hold the frame tighter on the finger and slow the erase slightly.
- **The tremor may look like a mistake.** The trembling finger is the emotional peak. If it reads as noise, reduce the tremor to a fine, barely-visible shake rather than cutting it.
- **The model may draw the middle-school friend.** "Sending to someone after two years" is a strong prior for a face. The negative prompt front-loads this; verify frame by frame — no face, no figure, name and text only.
- **The send must not be shown.** The cut must land on the finger resolved, not on the message leaving. If the send appears, the segment bleeds into S44.

## Changes

- _(none yet)_

## Next Generation

- If the typing-and-erasing reads as the S07 gesture returned, the cut hands the unresolved send straight into S44, where the message is sent and no read receipt comes.
