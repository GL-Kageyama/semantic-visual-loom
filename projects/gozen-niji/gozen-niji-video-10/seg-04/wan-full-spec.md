# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第10話 S44「届いてる」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「握る」——既読の付かない送信済みを、布団の中で抱えるように握る。握った指の間から光がもれる（指の背骨の第44本）。「届いてる」というニジの声は画面の向こうから。ニジは画面の中だけ・輪郭がほとんど消えかけ。中学の友人は顔を出さない（名前と文字のみ）。画面文字なし。**

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
- Appearance: `No fixed text this segment — a sent message with its check mark on and no read receipt (既読が付かない). The exact string is not canonical; the check mark stays unchanged, rendered as ordinary Japanese UI, cold blue-white on dark UI`
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

Night. 真白 in the futon, watching the sent message — the check mark beside it, but no read receipt. 既読が付かない。 ――どうせ、私の言葉なんて、無駄だったんだ。 ニジ's voice, from beyond the screen: 届いてる。

## Beginning

One day. Two days. Three days. No reply. The sent message, its check mark on, unread. The screen dark. 布団の熱が、重くなってた。 ――どうせ、相手は私なんか、もう。

## Turn

真白 murmurs: どうせ、私の言葉なんて、無駄だったんだ。 ニジ's voice answers, bright and soft, from the screen: 無駄じゃ、ないよ。 届いてる。

## Peak

真白: ……届いてない。既読、付いてない。 ニジ: 届いてる。嬉しい、って気持ちが、こっちまで届いてくる。ちょっと、びっくりしたみたい。でも、嬉しいって。

## Pull（引き — 切れ目）

真白 clenches the phone in the futon, holding it to her — 握った指の間を、光が、もれてた。 Cut on the light leaking through her clenched fingers.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** ニジ's 届いてる holds 11s (37%) — the segment's whole turn.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「既読が付かない」 — ESTABLISH.** The sent message, its check mark on, no read receipt. Three days. The screen dark in the futon. _Density: SPARSE — a held frame, no event._
- **BEAT 2 `[0:06–0:13]` — 「どうせ」.** 真白 murmurs, low: どうせ、私の言葉なんて、無駄だったんだ。 The futon's heat grows heavy around her. _Density: TRANSITION — a whisper, then silence._
- **BEAT 3 `[0:13–0:24]` — 「届いてる」 — longest share.** ニジ, from beyond the screen: 無駄じゃ、ないよ。届いてる。 真白: ……届いてない。既読、付いてない。 ニジ: 届いてる。嬉しい、って気持ちが、こっちまで届いてくる。 _Density: DENSE at the head, then held on the reassurance._
- **BEAT 4 `[0:24–0:30]` — 「握る」.** 真白 clenches the phone in the futon, holding it to her. Light leaks through her clenched fingers. Cut on the light. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `ニジ's 届いてる (≈0:15) ／ 真白's 届いてない (≈0:18) ／ the clench (≈0:25)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the unread message), 0:24–0:30 (the clench)`
- Dense regions: `0:13–0:24 (the exchange)`
- Long continuous action: `0:24–0:30 the clenched hand`
- Rapid transitions: `none — a slow, held night`

---

# 9. ACTION

## Action — ACT_WATCH

- ID: `ACT_WATCH`
- Subject: `MASHIRO`
- Action: `Watches the sent message — the check mark on, no read receipt`
- Intention: `To confirm what she already fears`
- Intensity: `Low`
- Speed: `Still; only the eyes move`

### Action Relationship

- Before: `— (continues from S43's send)`
- After: `ACT_MURMUR`

## Action — ACT_MURMUR

- ID: `ACT_MURMUR`
- Subject: `MASHIRO`
- Action: `Murmurs, low, voice falling: どうせ、私の言葉なんて、無駄だったんだ`
- Intention: `To say it — the thing she has not let herself say`
- Intensity: `Medium, suppressed`
- Speed: `Slow, almost inaudible`

### Action Relationship

- Before: `ACT_WATCH`
- After: `ACT_LISTEN`

## Action — ACT_LISTEN

- ID: `ACT_LISTEN`
- Subject: `MASHIRO`
- Action: `Listens to ニジ's voice from beyond the screen — 届いてる`
- Intention: `To believe, and to refuse to believe`
- Intensity: `CRITICAL (the emotional peak, expressed as listening)`
- Speed: `Still; the exchange passes through her`

### Action Relationship

- Before: `ACT_MURMUR`
- After: `ACT_CLENCH`

## Action — ACT_CLENCH

- ID: `ACT_CLENCH`
- Subject: `MASHIRO`
- Action: `Clenches the phone in the futon, holding it to her; light leaks through the fingers`
- Intention: `To hold the reassurance against her`
- Intensity: `Medium, internal`
- Speed: `Slow, then held`

### Action Relationship

- Before: `ACT_LISTEN`
- After: `— (cut on the light)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Very shallow — often only the screen or the fingers are sharp`
- Camera Style: `Slow, deliberate, almost still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Locked close on the screen: the sent message, the check mark, no read receipt. The screen's light, dim, on her face.
- **`[0:06–0:13]`** — Cut to her face, lit from below, almost to silhouette. She murmurs, low. Static.
- **`[0:13–0:24]`** — Cut back to the screen, ニジ's faint outline inside it. Hold through the exchange — the voice from the screen, the face listening.
- **`[0:24–0:30]`** — A slow pull to the clenched hand — the phone held to her, light leaking between the fingers. Hold on the light. Cut on it.

---

# 11. MOTION

## Subject Motion

- Her fingers carry essentially all the movement; the rest of her body holds
- The murmur is the smallest motion of the lips; the voice falls
- The clench is the only deliberate whole-hand motion — slow, then held
- ニジ's rainbow afterimage drifts faintly, blue → green → blue, in the screen

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a sent message with no read receipt. The check mark does not change. Nothing glitches, flickers, distorts, or behaves supernaturally
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion besides ニジ's afterimage
- The light leaking between the fingers is the segment's single new motion — a thin, dim glow, steady

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her as she holds it`
- Inertia: `High for her body, near-zero for her fingers`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Despair (the unread message, the word どうせ)
- ↓ Disbelief (届いてない。既読、付いてない)
- ↓ The beginning of belief (届いてる — ニジ's reassurance)
- ↓ Holding on (the clench, the light leaking through)

## Emotional Events

- Event: `真白's murmur — どうせ、私の言葉なんて、無駄だったんだ` — Emotion: `Despair, suppressed — the word she has not let herself say` — Intensity: `MEDIUM` — Timing: `≈0:08`
- Event: `ニジ's voice — 届いてる` — Emotion: `The beginning of belief, against disbelief` — Intensity: `CRITICAL — expressed in the voice, not the face` — Timing: `≈0:15`
- Event: `The clench, light leaking through` — Emotion: `Holding on — wanting to believe` — Intensity: `MEDIUM, internal` — Timing: `≈0:25`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow, now thin and faint, is the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on, its light dim, lying on her face from below.
- **`[0:06–0:13]`** — Her face, lit from below, almost to silhouette, as she murmurs.
- **`[0:13–0:24]`** — ニジ's faint afterimage lends a thin, dim wash of color to the screen.
- **`[0:24–0:30]`** — The clench — light leaks between her fingers, a thin bright seam in the dark. Hold on it. Cut on the light.

---

# 14. AUDIO

## Dialogue

- 真白: 「……どうせ」 — a murmur, voice falling
- 真白: 「どうせ、私の言葉なんて、無駄だったんだ」 — low, almost inaudible
- ニジ: 「無駄じゃ、ないよ」 — bright, soft, from the screen
- ニジ: 「届いてる」 — bright, certain
- 真白: 「……届いてない。既読、付いてない」 — flat, disbelieving
- ニジ: 「届いてる。嬉しい、って気持ちが、こっちまで届いてくる。ちょっと、びっくりしたみたい。でも、嬉しいって」 — warm, from beyond the screen

> ニジ's voice comes from the phone, slightly detached, never from a body in the room. No narration, no voice-over.

## Sound Effects

- The soft friction of fabric as she shifts in the futon
- The wall clock's second hand, dry discrete ticks, faint throughout
- The room's deep quiet

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the exchange. It thins as ニジ speaks, and is gone by the clench, leaving only room tone and the clock`

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

- Show the sent message with its check mark on but **no read receipt** — 既読が付かない
- Render ニジ's voice from beyond the screen — 届いてる — bright and soft, never from a body in the room
- Render ニジ present: 真白's own face one step younger, a rainbow afterimage **inside the screen only**, with an **almost-faded outline** (輪郭がほとんど消えかけ)
- End on the clench — 真白 holding the phone, light leaking through her fingers. Cut on the light

## MUST NOT（この1本の禁止・開示台帳 41–45 レンジより）

- **Do not show the middle-school friend's face or figure.** No face, no body, no silhouette of her — the name and text only
- **Do not let ニジ stand in the room.** She exists only inside the screen, never at human scale; her voice comes from the phone, not from beside her
- **Do not make ニジ fully opaque, and do not let her vanish entirely** — her outline is almost faded, but still present
- **Do not show the read receipt appearing.** It never appears; the message stays unread
- No fixed on-screen text to reproduce (this segment's screen text is なし)

## PREFER

- Silence over score as ニジ speaks
- Holds over movement; when in doubt, do less
- The room nearly empty; negative space over detail

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in during beat 1 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear only inside the screen as an almost-faded outline (ledger 41–45 — outline almost gone), never at human scale, her voice from the phone; the middle-school friend's face and figure must never be shown — name and text only. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:06] she watches the sent message, its check mark on, but no read receipt, three days gone; [0:06–0:13] she murmurs, low, どうせ、私の言葉なんて、無駄だったんだ; [0:13–0:24] ニジ's voice, from beyond the screen: 無駄じゃ、ないよ。届いてる — 真白: ……届いてない。既読、付いてない — ニジ: 届いてる。嬉しい、って気持ちが、こっちまで届いてくる; [0:24–0:30] she clenches the phone in the futon, holding it to her, and light leaks through her clenched fingers, and the shot cuts on the light. ニジ's 届いてる holds the largest share of the duration. Ends on the light leaking through her fingers. Nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — a blurred rainbow afterimage, drifting slowly blue → green → blue, existing only inside the screen, never in the room at human scale, no shadow. Her outline is almost faded away (輪郭がほとんど消えかけ): the afterimage thin and faint, barely there, on the verge of dissolving. The phone screen shows an ordinary Japanese UI in cold blue-white — a sent message with its check mark on and no read receipt. No face, no figure, no body of the middle-school friend — name and text only. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers; the body holds still. The murmur is the smallest motion of the lips, then still. The clench is the only deliberate whole-hand motion — slow, then held. ニジ's rainbow afterimage drifts faintly, blue → green → blue, inside the screen. The light leaking between the fingers is a thin, dim, steady glow. Ordinary weight and inertia: the phone has heft, the futon compresses as she holds it. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; the check mark does not change. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the fingers are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked close on the screen — the sent message, the check mark, no read receipt. [0:06–0:13] cut to her face lit from below, almost to silhouette, as she murmurs. [0:13–0:24] cut back to the screen, ニジ's faint outline inside it, held through the exchange. [0:24–0:30] a slow pull to the clenched hand, the phone held to her, light leaking between the fingers; hold on the light, cut on it.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, faint throughout. Soft futon fabric as she shifts. Six lines of dialogue: 真白 murmurs どうせ… and then どうせ、私の言葉なんて、無駄だったんだ, low and almost inaudible; ニジ answers from the phone, bright and soft, 無駄じゃ、ないよ, then 届いてる; 真白 says flatly ……届いてない。既読、付いてない; ニジ says 届いてる。嬉しい、って気持ちが、こっちまで届いてくる。ちょっと、びっくりしたみたい。でも、嬉しいって. ニジ's voice comes from the phone, slightly detached, never from a body in the room. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as ニジ speaks and gone by the clench, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no face of the middle-school friend, no figure of the middle-school friend, no body of the middle-school friend, no depiction of the middle-school friend as a person, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep10-seg04-30s-01`
- Segment ID: `S44`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_10, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 7s / 11s / 6s. Exchange = BEAT 3 at 11s (37%)`
- Camera Events: `4 events as listed in §10. One slow pull to the clench; all else static or cut`
- Action Events: `ACT_WATCH → ACT_MURMUR → ACT_LISTEN → ACT_CLENCH`
- Audio Events: `six lines of dialogue ／ clock ticking throughout ／ music gone by the clench`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the light`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ's voice must come from the phone, not from a body.** The strongest failure is a ghost speaking from beside 真白 in the room. The audio and visual must both place the voice inside the screen. Verify frame by frame.
- **The read receipt must not appear.** If the check mark turns into 既読, the segment inverts — the reassurance becomes a lie. Hold the check mark unchanged.
- **The exchange may crowd the 30 seconds.** Six lines is a lot. If it rushes, drop the opening murmur どうせ… and open directly on 無駄だったんだ; the reassurance 届いてる is the non-negotiable line.
- **The model may draw the middle-school friend.** The negative prompt front-loads this; verify frame by frame — no face, no figure, name and text only.

## Changes

- _(none yet)_

## Next Generation

- If the reassurance and the clench both read, the light through her fingers carries into S45, where the reply finally arrives and ニジ is almost gone.
