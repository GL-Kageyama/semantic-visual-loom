# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第10話 S41「下から返していく」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「返す」の実践——宛先リストの下から、短い挨拶を打っては送り、返した欄がひとつずつ空いていく連なり（指の背骨の第41本）。返すたびにニジの輪郭が薄くなる。ニジは画面の中だけ・輪郭がほとんど消えかけ。中学の友人は顔を出さない（名前と文字のみ）。画面文字なし。**

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
- Appearance: `No fixed text this segment — a succession of short greetings typed and sent, each returned slot emptying. The exact strings are not canonical; rendered only as ordinary Japanese UI, cold blue-white on dark UI, exactly as a phone renders it`
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

Night. 真白, who has learned to return, works her way up the 宛先リスト from the bottom — short greetings, one after another — and each returned slot empties, each name leaves the screen, and ニジ's outline thins a little more with every return.

## Beginning

2:00 A.M. The 宛先リスト is open, the phone the only light in the dark room. Her thumb scrolls down to the bottom of the list, where the oldest names live.

## Turn

The succession. A short greeting — ありがとう。あのとき、助かった。 ごめんね、返事、遅くなって。 — typed, sent. The slot empties. A name leaves the list. Then the next. Each one the same, and with each one, ニジ's outline thins a little more.

## Peak

The cumulative effect: the names on screen growing fewer, the list almost empty, ニジ's outline almost gone — the rainbow afterimage thin and faint in the corner.

## Pull（引き — 切れ目）

下の方から、上がっていって、残ったのは、あの子だった。 Cut on the list, now reduced to a single remaining name at the bottom — あの子, the middle-school friend. Her face never appears; only the name.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The succession holds 12s (40%) to engrave the return.

## Temporal Sequence

- **BEAT 1 `[0:00–0:08]` — 「リストの下」 — ESTABLISH.** Dark bedroom, 2:00 A.M. The 宛先リスト open, the phone the only light. Her thumb scrolls down to the bottom of the list. _Density: SPARSE — quiet UI movement, no event._
- **BEAT 2 `[0:08–0:20]` — 「返していく」 — longest share.** A short greeting typed and sent. The slot empties. A name leaves. Then the next, then the next — the same motion, the same release. With each return, ニジ's outline thins a little more. _Density: DENSE, rhythmic — the succession is the whole event._
- **BEAT 3 `[0:20–0:26]` — 「薄くなる」.** The list is almost empty. ニジ's outline is almost gone, the rainbow afterimage thin and faint in the corner of the screen. _Density: TRANSITION — the screen empties out._
- **BEAT 4 `[0:26–0:30]` — 「残った名前」.** One name remains at the bottom. Her thumb slows, then stops short of it. Cut on the single remaining name — あの子. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the succession of returns (0:08–0:20) ／ the last name remaining (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:08 (scrolling to the bottom), 0:26–0:30 (the held pause)`
- Dense regions: `0:08–0:20 (the succession)`
- Long continuous action: `0:08–0:20 the repeated typing-and-sending`
- Rapid transitions: `none — a steady, quiet procession`

---

# 9. ACTION

## Action — ACT_SCROLL

- ID: `ACT_SCROLL`
- Subject: `MASHIRO`
- Action: `Opens the 宛先リスト and scrolls down to the bottom`
- Intention: `To begin returning from the oldest names first`
- Intensity: `Low`
- Speed: `Steady, practiced`

### Action Relationship

- Before: `—`
- After: `ACT_RETURN`

## Action — ACT_RETURN

- ID: `ACT_RETURN`
- Subject: `MASHIRO`
- Action: `Types a short greeting and sends it, again and again — the return, in succession`
- Intention: `To return the deposited time, one name at a time`
- Intensity: `Low, rhythmic`
- Speed: `Steady, practiced, the same arc each time`

### Action Relationship

- Before: `ACT_SCROLL`
- After: `ACT_THIN`

## Action — ACT_THIN

- ID: `ACT_THIN`
- Subject: `NIJI`
- Action: `The outline thins with each return — the rainbow afterimage fading, blue → green → blue, slower and fainter`
- Intention: `Not her own doing — the consequence of time being returned`
- Intensity: `Low, continuous`
- Speed: `Slow, gradual`

### Action Relationship

- Before: `ACT_RETURN`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `MASHIRO`
- Action: `The thumb slows and stops short of the last remaining name`
- Intention: `Not yet — the one name left is the one she cannot return yet`
- Intensity: `Medium, internal`
- Speed: `A near-stop, held`

### Action Relationship

- Before: `ACT_THIN`
- After: `— (cut on the name)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Shallow — the screen or the fingers sharp, the room a soft indigo blur`
- Camera Style: `Slow, deliberate, almost still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:08]`** — Locked close on the screen and her hand. The list scrolls down under the thumb. Optional: an imperceptibly slow push-in.
- **`[0:08–0:20]`** — Stayed close, following the succession — the typing hand, the send, the slot emptying, the name leaving. No cuts, one continuous held frame, the corner of the screen holding ニジ's faint afterimage.
- **`[0:20–0:26]`** — A very slow pull-back just enough to hold both the emptying list and ニジ's thinning outline in the corner together.
- **`[0:26–0:30]`** — Settle on the list — one name remaining at the bottom. Her thumb slows above it. Cut on the name.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially all the movement; the rest of her body holds
- The return is a steady, practiced repetition — type, send, next — the same arc, the same rhythm
- ニジ's outline thins gradually: the rainbow afterimage drifts blue → green → blue, slower and fainter with each return
- The final near-stop is the only break in the succession — the thumb slowing short of the last name

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a greeting sent, a slot emptying, a name leaving. Nothing glitches, flickers, distorts, or behaves supernaturally
- The wall clock's second hand advances in discrete ticks, out of focus behind

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion besides ニジ's afterimage
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers (instant, practiced)`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Practiced calm (the return, now a routine she has learned)
- ↓ Quiet release (each name leaving, each slot emptying)
- ↓ Thinning (the names gone, ニジ fading with them)
- ↓ A stop short of dread (the one name left — あの子)

## Emotional Events

- Event: `The succession of returns` — Emotion: `Practiced release — not joy, not grief, a returning` — Intensity: `LOW` — Timing: `0:08–0:20`
- Event: `ニジ's outline thinning with each return` — Emotion: `Quiet loss, unacknowledged — the afterimage fading` — Intensity: `MEDIUM, entirely internal` — Timing: `≈0:20`
- Event: `The thumb stops short of the last name` — Emotion: `The approach of dread — あの子 remains` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:27`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo, warm from the futon's remembered day-heat at the edge`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow — now thin and faint — is the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on the ceiling as a soft blue rectangle.
- **`[0:08–0:20]`** — The screen's light holds steady through the succession; only the UI changes. ニジ's afterimage contributes a faint, thin wash of color.
- **`[0:20–0:26]`** — As the list empties, ニジ's color grows fainter — the saturated hue almost gone, leaving the screen's blue-white to dominate.
- **`[0:26–0:30]`** — Light unchanged. Cut on the name.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The greetings are typed, not spoken. No narration, no voice-over.

## Sound Effects

- The soft friction of a thumb on glass, close and continuous, through the succession — each tap and send its own small rhythm
- The faint electronic tap of a message sending, repeated
- The wall clock's second hand, dry discrete ticks, faint under the taps

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, gentle, slightly diminishing. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the succession. It thins with each return, and is nearly gone by the last name, leaving only room tone and the clock`

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

- Establish the succession — a short greeting typed and sent, the slot emptying, a name leaving, repeated
- Render ニジ present: 真白's own face one step younger, a rainbow afterimage **inside the screen only**, with an **almost-faded outline** (輪郭がほとんど消えかけ)
- Let her outline thin visibly with each return — the afterimage growing fainter, never disappearing entirely
- End on the list reduced to a single remaining name at the bottom, cut on that name

## MUST NOT（この1本の禁止・開示台帳 41–45 レンジより）

- **Do not show the middle-school friend's face or figure.** No face, no body, no silhouette of her — the name and text only
- **Do not let ニジ stand in the room.** She exists only inside the screen, never at human scale
- **Do not make ニジ fully opaque, and do not let her vanish entirely** — her outline is almost faded, but still present
- No fixed on-screen text to reproduce (this segment's screen text is なし); do not invent a single canonical greeting string
- No second living person in the room

## PREFER

- The succession uninterrupted for as long as possible — the whole segment is one held procession
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

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:08] the 宛先リスト is open, the phone the only light, and her thumb scrolls down to the bottom of the list; [0:08–0:20] the succession — a short greeting typed and sent, the slot emptying, a name leaving the list, again and again, and with each return ニジ's outline thins a little more; [0:20–0:26] the list is almost empty, ニジ's rainbow afterimage thin and faint in the corner; [0:26–0:30] one name remains at the bottom, her thumb slows and stops short of it, and the shot cuts on the name. The succession holds the largest share of the duration. Ends on the last remaining name — あの子, whose face never appears. Nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — a blurred rainbow afterimage, drifting slowly blue → green → blue, existing only inside the screen, never in the room at human scale, no shadow. Her outline is almost faded away (輪郭がほとんど消えかけ): the afterimage thin and faint, barely there, on the verge of dissolving. The phone screen shows the 宛先リスト in ordinary Japanese UI, cold blue-white, the list thinning to a single remaining name at the bottom. No face, no figure, no body of the middle-school friend — name and text only. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers; the body holds still. The return is a steady practiced repetition — type, send, next — the same arc, the same rhythm. ニジ's outline thins gradually: the rainbow afterimage drifts blue → green → blue, slower and fainter with each return, but never disappears entirely. The thumb slows and stops short of the last remaining name. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, shallow depth of field; the screen or the fingers are sharp, the room a soft indigo blur. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:08] locked close on the screen and hand, the list scrolling down, optionally an imperceptibly slow push-in. [0:08–0:20] stayed close, following the succession in one continuous held frame, the corner of the screen holding ニジ's faint afterimage. [0:20–0:26] a very slow pull-back to hold both the emptying list and ニジ's thinning outline together. [0:26–0:30] settle on the list — one name remaining at the bottom — her thumb slowing above it; cut on the name.

## Audio Prompt

Almost silent. Deep quiet night room tone. The soft friction of a thumb on glass through the succession, close and continuous, each tap and send its own small rhythm. A faint electronic tap as each message sends. The wall clock's dry discrete ticking, faint under the taps. No spoken words at all — the greetings are typed, not spoken. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning with each return and nearly gone by the last name, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no face of the middle-school friend, no figure of the middle-school friend, no body of the middle-school friend, no depiction of the middle-school friend as a person, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep10-seg01-30s-01`
- Segment ID: `S41`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_10, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 8s / 12s / 6s / 4s. Succession = BEAT 2 at 12s (40%)`
- Camera Events: `4 events as listed in §10. No sustained dolly; all static, drift, or pull-back`
- Action Events: `ACT_SCROLL → ACT_RETURN → ACT_THIN → ACT_HOLD`
- Audio Events: `no dialogue ／ thumb-on-glass throughout ／ clock faint under the taps`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the last remaining name`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The succession may read as a loop, not a progression.** Each return must visibly remove one name. If the list does not shrink, the segment has no arc — hold the frame tighter on the list and let each empty slot read clearly.
- **ニジ's thinning may not register.** The opacity shift is the segment's quiet spine. If the afterimage looks static, slow the change and widen slightly on the later beats so the fade is visible against the list.
- **The model may draw the middle-school friend.** The last remaining name is the strongest prior for "show the person." The negative prompt front-loads this; verify frame by frame — no face, no figure, name only.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the succession and the thinning both read, the last name carries straight into S42, where the finger must stop over it — the pause here is the setup for that stop.
