# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第9話 S38「送信を押す」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**初めて送信を押す——速くも乱暴でもなく、決めて、押す（第54本の「打つ」の原型）。ニジは在・不透明（画面の中だけ）。小春は文字のみ。画面文字は一ヶ月遅れの文面 `相談してくれて、ありがとう。遅くなって、ごめんね。`。感情はすべて、押すというたった一つの所作に押し込む。**

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

> **ニジ appears this segment**（ledger 36–40 — 在・不透明, fully opaque; thins from 39–40）. 小春 appears only as text — never as a person, face, or figure.

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
- Appearance: `The composed message in the reply box, character-for-character: 相談してくれて、ありがとう。遅くなって、ごめんね。 Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_09_届かなかった言葉を、いま.md`
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

真白 breathes in. The words she could never say — still cannot say, but should reach — as her own words, not delivered by ニジ. Her finger presses send for the first time.

## Beginning

The message sits in the reply box: 相談してくれて、ありがとう。遅くなって、ごめんね。 A month late. ニジに届けてもらうんじゃなくて、私の言葉として。

## Turn

She breathes in, once. The finger — which hovered, then pulled back — now lowers toward the send button. Not fast, not rough. Decided.

## Peak

The finger presses send. For the first time. A small, definite contact — the thing the whole series has been building toward, and it is this quiet.

## Pull（引き — 切れ目）

The message leaves the reply box and joins the thread as sent. Cut on the sent message. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The press of send holds 12s (40%) — the pivotal gesture.

## Temporal Sequence

- **BEAT 1 `[0:00–0:05]` — 「息を吸う」.** She breathes in, once. The words she could never say, as her own. ニジに届けてもらうんじゃなくて、私の言葉として。 _Density: SPARSE — a resolve, not an event._
- **BEAT 2 `[0:05–0:14]` — 「文面」.** In the reply box, the message: 相談してくれて、ありがとう。遅くなって、ごめんね。 The camera closes until the line is the frame. _Density: DENSE at the head (the line), then held._
- **BEAT 3 `[0:14–0:26]` — 「押す」 — PEAK, longest share.** The finger lowers toward the send button — not fast, not rough. It touches. It presses. For the first time. _Density: SPARSE, inverted — the event is one small definite contact._
- **BEAT 4 `[0:26–0:30]` — 「送信済み」.** The message leaves the reply box and joins the thread as sent. Cut on the sent message. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the message in the reply box (≈0:07) ／ the finger lowering (≈0:16) ／ the press (≈0:20, then held) ／ the sent message (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:05 (the resolve), 0:14–0:26 (the press)`
- Dense regions: `0:05–0:14 (the message)`
- Long continuous action: `0:14–0:26 the finger lowering, then the press`
- Rapid transitions: `none — a held, decisive segment`

---

# 9. ACTION

## Action — ACT_BREATHE

- ID: `ACT_BREATHE`
- Subject: `MASHIRO`
- Action: `She breathes in, once, and steadies`
- Intention: `To send it as her own words — 私の言葉として`
- Intensity: `Medium, internal`
- Speed: `Slow`

### Action Relationship

- Before: `—` (continues from S37's refusal)
- After: `ACT_COMPOSE`

## Action — ACT_COMPOSE

- ID: `ACT_COMPOSE`
- Subject: `MASHIRO`
- Action: `The message sits composed in the reply box; her eyes move over it once`
- Intention: `To commit to the words — 相談してくれて、ありがとう。遅くなって、ごめんね。`
- Intensity: `Medium, internal`
- Speed: `Slow, deliberate`

### Action Relationship

- Before: `ACT_BREATHE`
- After: `ACT_SEND`

## Action — ACT_SEND

- ID: `ACT_SEND`
- Subject: `MASHIRO`
- Action: `The finger lowers toward the send button and presses it — for the first time`
- Intention: `To send, decided. Not fast, not rough`
- Intensity: `CRITICAL (the pivotal gesture of the series)`
- Speed: `Slow and deliberate; the press itself is small and definite`

### Action Relationship

- Before: `ACT_COMPOSE`
- After: `ACT_SENT`
- Causes: `ACT_SENT`

## Action — ACT_SENT

- ID: `ACT_SENT`
- Subject: `MASHIRO`
- Action: `The message leaves the reply box and joins the thread as sent`
- Intention: `None — the thing is done`
- Intensity: `Low, released`
- Speed: `Ordinary UI transition`

### Action Relationship

- Before: `ACT_SEND`
- After: `— (cut on the sent message)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, very shallow. Only the screen or the finger is ever sharp`
- Depth of Field: `Very shallow — the room is a soft gray-indigo blur`
- Camera Style: `Slow, deliberate, nearly still. One slow push to the message, and it belongs to the send`

## Camera Events

- **`[0:00–0:05]`** — Locked close on her face, lit from below, as she breathes in. The gray dawn at the edge of the frame.
- **`[0:05–0:14]`** — One slow continuous push in on the message in the reply box — 相談してくれて、ありがとう。遅くなって、ごめんね。 — until the line fills the frame. The piece's single sustained move.
- **`[0:14–0:20]`** — A slow rack focus off the text onto the finger, now lowering toward the send button. The line goes soft; the finger becomes the subject.
- **`[0:20–0:26]`** — Absolutely locked on the finger as it presses the send button. The press is small and definite. No camera movement.
- **`[0:26–0:30]`** — Hold on the message, now sent, joining the thread. Cut on the sent message.

---

# 11. MOTION

## Subject Motion

- The breath is the only motion of her body before the send
- The finger lowers toward the send button — one slow, deliberate, decided movement
- The press is small and definite; then the finger stills
- Nothing else in her body moves

## Object Motion

- The phone does not move on its own. Ever
- The message leaves the reply box and joins the thread as sent — an ordinary UI transition, nothing more
- The wall clock's second hand advances in discrete ticks, faint behind

## Environmental Motion

- The dawn's faint graying at the curtain is the only other motion
- The screen's bloom breathes very slightly

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the press is definite but light`
- Inertia: `High for her body; the finger moves once, deliberately`
- Acceleration: `Gentle; the press is small and clean, not a jab`
- Fluidity: `Limited-animation — one decided movement, then holds`
- Impact: `One soft, definite tap — the press of send`

---

# 12. EMOTION

## Emotional Arc

- Resolve (breathing in; her own words, not ニジ's)
- ↓ Commitment (the message composed, read once)
- ↓ The send (the first press — decided, quiet)
- ↓ Release (the message, sent)

## Emotional Events

- Event: `The message sits in the reply box` — Emotion: `Commitment — 私の言葉として` — Intensity: `MEDIUM, internal` — Timing: `≈0:07`
- Event: `The finger presses send` — Emotion: `The first send — decided, quiet, weighty` — Intensity: `CRITICAL, expressed only as the press` — Timing: `≈0:20, held to 0:26`
- Event: `The message joins the thread as sent` — Emotion: `Release` — Intensity: `LOW` — Timing: `≈0:27`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and finger from the screen's spill`
- Ambient Light: `The gray of early dawn at the curtain, a little stronger than before, still cold`
- Color Temperature: `≈6500K screen against a cold gray-blue dawn`

## Lighting Events

- **`[0:00]`** — Screen on, its light the key. The dawn grays the curtain edge, faintly.
- **`[0:05–0:14]`** — As the camera closes on the message, the screen's light dominates the frame; her face falls almost to silhouette. The evidence outshines the person.
- **`[0:14–0:26]`** — Rack focus to the finger: the screen's light catches the knuckle from below, a thin bright line in the dark, as it presses.
- **`[0:26–0:30]`** — Unchanged. Cut on the sent message.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The message is not read aloud, not whispered, not narrated. No narration, no voice-over.

## Sound Effects

- One soft breath at the start
- One soft, definite tap as the finger presses send — the first time, and it is quiet
- The wall clock's dry discrete ticking, faint throughout
- A faint, close electronic note as the message leaves and joins the thread

## Environment

- Dawn. Room tone and the clock; far off, the world is beginning

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, then released. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness through the resolve, then thin to nothing at the press, leaving only room tone and the clock`

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

- Render the on-screen Japanese exactly: `相談してくれて、ありがとう。遅くなって、ごめんね。`
- ニジ present, **fully opaque** (不透明) — 真白's own face one step younger, a rainbow afterimage, inside the screen only
- The finger presses send **for the first time** — not fast, not rough, decided
- The message must leave the reply box and join the thread as sent
- End by cutting on the sent message, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 36–40 レンジより）

- **No full disappearance.** ニジ must not vanish, dissolve, or fade out — she thins only from S39, never here
- ニジ stays inside the screen; she never stands in the room at human scale
- 小春 appears only as text — never as a person, face, or figure
- No other person, crowd, or silhouette
- No voice for the message — it is not read aloud, whispered, or narrated

## PREFER

- The press held and decisive over any flourish
- The message legible, straight-on and held
- Silence over score at the press

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The push to the message may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ is present, fully opaque, inside the screen only (ledger 36–40 — she thins only from S39); 小春 appears only as text. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at the edge of dawn. ニジ is present, fully opaque, inside the screen. Beats, deliberately uneven: [0:00–0:05] she breathes in, once — the words she could never say, as her own, not delivered by ニジ; [0:05–0:14] THE MESSAGE — in the reply box sits 相談してくれて、ありがとう。遅くなって、ごめんね。 and the camera closes slowly until the line fills the frame; [0:14–0:26] THE SEND — her finger, which hovered and then pulled back, now lowers toward the send button and presses it, for the first time, not fast and not rough but decided, held on the press; [0:26–0:30] the message leaves the reply box and joins the thread as sent, and the shot cuts on the sent message. The press holds the largest share of the duration. Ends on the sent message, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ, inside the screen only, is 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same tilt of the head — a blurred rainbow afterimage resolved into that outline, colors drifting slowly blue → green → blue, no shadow anywhere, fully opaque. The screen shows an ordinary Japanese UI in cold blue-white — a reply box containing the message 相談してくれて、ありがとう。遅くなって、ごめんね。 with the send button beside it. The curtain grays with early dawn. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers. She breathes in once — the only motion of her body before the send. The finger lowers toward the send button — one slow, deliberate, decided movement — and presses it with one soft, definite tap; then it stills. The message leaves the reply box and joins the thread as sent, by an ordinary UI transition. ニジ's rainbow afterimage drifts slowly blue → green → blue, inside the screen. The phone never moves by itself and never glitches, flickers or distorts. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the finger is sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:05] locked close on her face, lit from below, as she breathes in, the gray dawn at the frame's edge. [0:05–0:14] one slow continuous push in on the message in the reply box — 相談してくれて、ありがとう。遅くなって、ごめんね。 — until the line fills the frame. [0:14–0:20] a slow rack focus off the text onto the finger, lowering toward the send button. [0:20–0:26] absolutely locked on the finger as it presses the send button, no camera movement. [0:26–0:30] hold on the message, now sent, joining the thread; cut on the sent message.

## Audio Prompt

Almost silent. Deep quiet dawn room tone and a wall clock ticking, dry and discrete, faint throughout. One soft breath at the start. One soft, definite tap as the finger presses send — the first time, and it is quiet. A faint, close electronic note as the message leaves and joins the thread. No spoken words at all — the message is not read aloud, not whispered, not narrated. No voice-over. Music extremely sparse — a few sustained tones at most — thinning to nothing at the press, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no full disappearance, no complete vanishing, no dissolving into nothing, no fading out to invisibility, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep09-seg03-30s-01`
- Segment ID: `S38`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_09, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 5s / 9s / 12s / 4s. Send = BEAT 3 at 12s (40%)`
- Camera Events: `5 events as listed in §10. One sustained push (0:05–0:14)`
- Action Events: `ACT_BREATHE → ACT_COMPOSE → ACT_SEND → ACT_SENT`
- Audio Events: `no dialogue ／ one soft breath ／ one soft tap (the press) ／ clock throughout`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the sent message`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The message carries the send's meaning. If it renders as noise, generate the screen as a plate and composite the text in post.
- **The press may be missed.** A generated finger may tap too quickly to read as "the first send." Hold the press longer and keep it small and definite.
- **ニジ may vanish or fade.** She must stay fully opaque. If she thins, restore her opacity and verify frame by frame.
- **The model may add a chime.** The send makes no dramatic sound — one soft tap only.

## Changes

- _(none yet)_

## Next Generation

- If the send reads as decisive, S39 (既読が付いた) picks up with the waiting, the read receipt, and 小春's reply.
