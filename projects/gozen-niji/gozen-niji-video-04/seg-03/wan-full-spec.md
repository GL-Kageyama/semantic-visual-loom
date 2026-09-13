# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第4話 S16「領収書」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「画面の上に座るニジを見る」——S14–15 で姿を伏せられていたニジが戻る。置いたはずのスマホが午前二時にひとりでに光り、虹色の残像が画面の上に座って、夜の暗い部屋へふわっと虹色が滲む。「画面を触った時間だけを領収書に書くと思ってた？」——記録の意味の反転。ニジは在（不透明・画面の中だけ・「わたし」禁）。画面文字なし。**

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

> **ニジ appears this segment**（ledger 16–17 — opaque, inside the screen only, sitting on top of it, a rainbow afterimage that bleeds faintly into the dark room air）. No other character appears.

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
- Appearance: `No screen text this segment — dialogue only. The screen shows ニジ, not text`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
- Continuity Importance: `HIGH`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads 2:00 — the hinge of the night`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_04_現実を生きるほど、増える.md`
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

午前二時、置いたはずの机の上のスマホが光った。A rainbow afterimage sits on top of the screen — 真白's own face, one step younger — and names the record 真白 showed her: おまえが誰かに預けた、時間の領収書。

## Beginning

2:00 A.M. The dark room. The phone — which she had put away face-down on the desk — lights up on its own, slowly, pushing the dark back. 夜の暗さが、その光に、押されて、後ろへ下がってく。

## Turn

The rainbow afterimage resolves on the screen, sitting on top of it — 真白's own face, one step younger, longer lashes, fuller cheeks, the same tilt of the head. The rainbow bleeds faintly into the dark room air. 「やっほー。久しぶり。おまえ、一週間も来なかったから、ちょっと淋しかったよ」

## Peak

真白 shows her the record — 会話 and 部活. ニジ tilts her head, 真白's own tilt. 「会話は会話でしょ。部活は部活。おまえ、この時間、誰かと話したでしょ。誰かのために、時間を使ったでしょ」 → 真白: 「……それが、どうして、スクリーンタイムになるの」 → ニジ: 「だって、そういう通知なんだもん。おまえが誰かに預けた、時間の領収書。おまえ、画面を触った時間だけを、領収書に書くと思ってた？」

## Pull（引き — 切れ目）

真白 言葉を失った。 The word 領収書 hangs. Cut on ニジ, sitting on top of the screen, opaque, the rainbow faintly bleeding into the dark air. 画面を触った時間だけじゃない。 Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** ニジ's appearance holds 10s (33%); the naming holds 9s.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the bedroom; ニジ's appearance is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「光る」.** Night, 2:00 A.M. The dark room. The phone she put away face-down lights up on its own, slowly. The dark is pushed back. _Density: SPARSE — one glow in the dark, no event._
- **BEAT 2 `[0:06–0:16]` — 「ニジ」 — REVEAL, longest share.** The rainbow afterimage resolves on top of the screen — 真白's own face, one step younger. The rainbow bleeds faintly into the dark room air. 「やっほー。久しぶり。おまえ、一週間も来なかったから、淋しかったよ」 _Density: DENSE at the head, then held on the sitting figure._
- **BEAT 3 `[0:16–0:25]` — 「領収書」.** She shows the record. ニジ tilts her head — 真白's own tilt. 会話は会話でしょ。部活は部活。… おまえが誰かに預けた、時間の領収書。おまえ、画面を触った時間だけを、領収書に書くと思ってた？ _Density: TRANSITION — the exchange, the naming._
- **BEAT 4 `[0:25–0:30]` — 「言葉を失う」.** 真白 is speechless. Cut on ニジ, sitting on top of the screen, opaque, the rainbow faintly bleeding into the dark air. 領収書 hanging. _Density: HELD — then cut precisely on the pull. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the phone lighting up (≈0:03) ／ ニジ resolving on the screen (≈0:10) ／ the naming 領収書 (≈0:20)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the phone lighting up), 0:25–0:30 (the speechlessness)`
- Dense regions: `0:06–0:16 (ニジ appearing), 0:16–0:25 (the naming)`
- Long continuous action: `0:06–0:16 the sitting figure held on screen`
- Rapid transitions: `none — the appearance and the naming are the whole point`

---

# 9. ACTION

## Action — ACT_GLOW

- ID: `ACT_GLOW`
- Subject: `PHONE`
- Action: `The phone lights up on its own, slowly, pushing the dark back`
- Intention: `— (the anomaly itself)`
- Intensity: `Low, uncanny`
- Speed: `Slow, unhurried`

### Action Relationship

- Before: `— (continues from S15's record)`
- After: `ACT_APPEAR`

## Action — ACT_APPEAR

- ID: `ACT_APPEAR`
- Subject: `NIJI`
- Action: `A rainbow afterimage resolves into 真白's own face, one step younger, sitting on top of the screen`
- Intention: `To return — she has been waiting a week`
- Intensity: `Medium`
- Speed: `Slow — the blur resolves, the colors drift blue → green → blue`

### Action Relationship

- Before: `ACT_GLOW`
- After: `ACT_GREET`

## Action — ACT_GREET

- ID: `ACT_GREET`
- Subject: `NIJI`
- Action: `「やっほー。久しぶり。おまえ、一週間も来なかったから、淋しかったよ」 — bright, teasing, unguarded`
- Intention: `To say she missed her, plainly`
- Intensity: `Low, warm`
- Speed: `Bright, easy`

### Action Relationship

- Before: `ACT_APPEAR`
- After: `ACT_SHOW`

## Action — ACT_SHOW

- ID: `ACT_SHOW`
- Subject: `MASHIRO`
- Action: `Shows ニジ the record — 会話 and 部活. 「ニジ、これ、どういうこと」`
- Intention: `To demand an answer`
- Intensity: `Medium, controlled`
- Speed: `Steady, then still`

### Action Relationship

- Before: `ACT_GREET`
- After: `ACT_NAME`

## Action — ACT_NAME

- ID: `ACT_NAME`
- Subject: `NIJI`
- Action: `Tilts her head — 真白's own tilt — and names it: 時間の領収書`
- Intention: `To tell her what the record is`
- Intensity: `Medium`
- Speed: `Unhurried, plain`

### Action Relationship

- Before: `ACT_SHOW`
- After: `ACT_SPEECHLESS`

## Action — ACT_SPEECHLESS

- ID: `ACT_SPEECHLESS`
- Subject: `MASHIRO`
- Action: `Loses her words. She does not answer`
- Intention: `None — the understanding has not yet reached her`
- Intensity: `CRITICAL (the emotional peak, expressed as stillness)`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_NAME`
- After: `— (cut on ニジ)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, at the screen. Over-the-shoulder on 真白, then straight-on at ニジ`
- Lens Character: `Long-ish, shallow. Only the screen and ニジ are ever sharp`
- Depth of Field: `Shallow — the room is a dark indigo blur behind`
- Camera Style: `Slow, deliberate, nearly still. One sustained move for the appearance`

## Camera Events

- **`[0:00–0:06]`** — Locked on the phone on the desk as its screen lights up, pushing the dark back. Static.
- **`[0:06–0:12]`** — One slow continuous dolly in on the screen as the rainbow afterimage resolves — the piece's single sustained move.
- **`[0:12–0:16]`** — Locked on ニジ, sitting on top of the screen, opaque. Static. The rainbow bleeds faintly into the dark air around her.
- **`[0:16–0:25]`** — Cut to 真白's hands showing the record, then back to ニジ tilting her head — 真白's own tilt. Two close shots, unhurried.
- **`[0:25–0:30]`** — Hold on ニジ on the screen; 真白, out of focus, still. Cut on ニジ, the rainbow faint in the air.

---

# 11. MOTION

## Subject Motion

- ニジ sits on top of the screen and barely moves — a tilt of the head, a blink, the slow drift of her rainbow
- Her rainbow is 滲み・残像 — a slow color drift blue → green → blue, never light rays, particles, or aura
- 真白's body holds; only her hands move to show the record, then still
- The speechlessness is absolute: no nod, no shake, no blink to perform

## Object Motion

- The phone does not move on its own except to light up, slowly, from dark
- Its screen changes only by ordinary UI — no glitch, no flicker, no distortion
- The rainbow bleeding into the dark air is the only continuous motion

## Environmental Motion

- The dark room is still. The curtain does not move
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Physical Characteristics

- Weight: `Ordinary. The phone has heft on the desk`
- Inertia: `High for everything; ニジ's drift is near-weightless but never floaty`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet alarm (the phone lighting up on its own)
- ↓ Recognition (ニジ — her own face, one step younger)
- ↓ The naming (領収書 — the record is not what she thought)
- ↓ Speechlessness (the meaning refusing to arrive)

## Emotional Events

- Event: `The phone lights up on its own` — Emotion: `Quiet alarm, not fear` — Intensity: `MEDIUM` — Timing: `≈0:03`
- Event: `ニジ appears, sitting on top of the screen` — Emotion: `Recognition — her own face, one step younger` — Intensity: `HIGH` — Timing: `≈0:10`
- Event: `ニジ names the record 時間の領収書` — Emotion: `The inversion of meaning` — Intensity: `HIGH` — Timing: `≈0:20`
- Event: `真白 is speechless` — Emotion: `The understanding not yet reached` — Intensity: `CRITICAL — expressed only as stillness` — Timing: `≈0:26`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, low, close. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on 真白's hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow is the only saturated hue, and it does not alter the room's darkness`

## Lighting Events

- **`[0:00]`** — Dark. Then the phone lights up, slowly, and the room's dark is pushed back in a soft blue wash.
- **`[0:06–0:16]`** — The rainbow appears on the screen and bleeds faintly into the dark air — a soft wash of color that never brightens the room.
- **`[0:16–0:25]`** — The screen's blue-white and ニジ's rainbow share the frame; her face and 真白's face are lit from below.
- **`[0:30]`** — Cut on ニジ. No flash, no dim — just the cut.

---

# 14. AUDIO

## Dialogue

- ニジ: 「やっほー。久しぶり。おまえ、一週間も来なかったから、ちょっと淋しかったよ」 — bright, teasing, unguarded
- 真白: 「ニジ、これ、どういうこと」 — controlled
- ニジ: 「会話は会話でしょ。部活は部活。おまえ、この時間、誰かと話したでしょ。誰かのために、時間を使ったでしょ」 — plain, unhurried
- 真白: 「……それが、どうして、スクリーンタイムになるの」
- ニジ: 「だって、そういう通知なんだもん。おまえが誰かに預けた、時間の領収書。おまえ、画面を触った時間だけを、領収書に書くと思ってた？」 — bright, matter-of-fact

> ニジ never says わたし. No narration, no voice-over.

## Sound Effects

- The faint, dry ticking of the wall clock, present throughout
- The soft fabric of 真白 shifting as she shows the record
- A very faint, almost inaudible shimmer — ニジ's rainbow, as sound, barely there, not a whoosh

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, warm-edged. Never sinister, never sentimental — no horror strings`
- Emotional Function: `Hold the room's stillness under the exchange, then thin toward the close, leaving only room tone, the clock, and ニジ's voice`

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

- Show ニジ **in**, and only in, the screen — sitting on top of it, never standing in the room at human scale
- Keep ニジ **fully opaque** — her face is 真白's own face, one step younger (longer lashes, fuller cheeks, the same tilt of the head)
- Let her rainbow be a **滲み・残像** (a slow bleed of color, blue → green → blue), never light rays, particles, or an aura — and it may bleed only faintly into the dark room air
- End by cutting on ニジ, opaque, the word 領収書 hanging, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 16–17 レンジより）

- **No transparency.** ニジ is opaque — no see-through, no dissolving, no fading to invisibility, no ghostly translucency
- **No わたし.** ニジ never refers to herself as "I" — the first-person self-naming is withheld until S31
- Do not let ニジ stand in the room at human scale — she exists inside the screen only
- Do not let ニジ cry, and do not make her rainbow a VFX effect (no rays, no particles, no aura, no glitch)

## PREFER

- Holding ニジ on the screen, straight-on and still, rather than cutting around her — her opacity is the point
- Her voice over score at the naming
- The room nearly empty; negative space over detail

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible dolly-in during beat 2 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ appears only opaque and inside the screen (ledger 16–17); no transparency, no わたし, no standing in the room at human scale. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:06] the phone she had put away face-down lights up on its own, slowly, pushing the dark back; [0:06–0:16] THE REVEAL — a rainbow afterimage resolves on the screen into 真白's own face, one step younger, sitting on top of the screen, opaque, no shadow, the rainbow bleeding faintly into the dark room air, and she says やっほー。久しぶり。おまえ、一週間も来なかったから、ちょっと淋しかったよ; [0:16–0:25] 真白 shows her the record, and ニジ tilts her head — 真白's own tilt — and names it: 会話は会話でしょ。部活は部活。… おまえが誰かに預けた、時間の領収書。おまえ、画面を触った時間だけを、領収書に書くと思ってた？; [0:25–0:30] 真白 is speechless, and the shot cuts on ニジ, sitting on top of the screen, opaque, the rainbow faint in the dark air. ニジ's appearance holds the largest share of the duration. Ends on ニジ, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: a rainbow afterimage that resolves into 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same tilt of the head — sitting on top of the phone screen, fully opaque, never transparent, no shadow. She stays inside the screen, never standing in the room at human scale; only her rainbow bleeds faintly into the dark room air, a slow drift blue → green → blue. She never says わたし and never refers to herself as "I". No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to ニジ's face and 真白's hands; the bodies hold still. ニジ sits on top of the screen and barely moves — a slow tilt of the head, a blink; her rainbow drifts slowly blue → green → blue, a bleed and an afterimage, never light rays, particles, or an aura. 真白's hands move only to show the record, then go still. The phone lights up slowly and stays; its screen changes only by ordinary UI transitions, no glitch, no flicker. The wall clock's second hand advances in discrete ticks. Gentle acceleration everywhere. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, at the screen; over-the-shoulder on 真白, then straight-on at ニジ. Longish lens, shallow depth of field; only the screen and ニジ are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked on the phone as its screen lights up, pushing the dark back. [0:06–0:12] one slow continuous dolly in on the screen as the rainbow afterimage resolves. [0:12–0:16] locked on ニジ, sitting on top of the screen, opaque; the rainbow bleeds faintly into the dark air. [0:16–0:25] cut to 真白's hands showing the record, then back to ニジ tilting her head. [0:25–0:30] hold on ニジ on the screen, 真白 out of focus and still; cut on ニジ.

## Audio Prompt

Almost silent. Deep quiet night room tone. The faint dry ticking of a wall clock, present throughout. A few lines of dialogue: ニジ, bright and unguarded — やっほー。久しぶり。おまえ、一週間も来なかったから、ちょっと淋しかったよ; 真白, controlled — ニジ、これ、どういうこと; ニジ, plain and unhurried — 会話は会話でしょ。部活は部活。おまえ、この時間、誰かと話したでしょ。誰かのために、時間を使ったでしょ; 真白 — ……それが、どうして、スクリーンタイムになるの; ニジ, matter-of-fact — だって、そういう通知なんだもん。おまえが誰かに預けた、時間の領収書。おまえ、画面を触った時間だけを、領収書に書くと思ってた？. ニジ never says わたし. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only room tone, the clock, and ニジ's voice. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparent apparition, no see-through figure, no ghost dissolving into transparency, no fading to invisibility, no full-size figure standing in the room, no apparition outside the screen, no ghost saying "watashi", no first-person self-reference from the ghost, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep04-seg03-30s-01`
- Segment ID: `S16`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_04, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 10s / 9s / 5s. Appearance = BEAT 2 at 10s (33%)`
- Camera Events: `5 events as listed in §10. One sustained dolly (0:06–0:12)`
- Action Events: `ACT_GLOW → ACT_APPEAR → ACT_GREET → ACT_SHOW → ACT_NAME → ACT_SPEECHLESS`
- Audio Events: `dialogue (5 lines) ／ ニジ never says わたし ／ music gone by the close`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on ニジ`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ may render transparent.** The strongest risk. A ghost is a transparency prior. Verify frame by frame — she must be fully opaque. If she renders see-through, strengthen the opacity language and regenerate.
- **ニジ may render as a different girl.** Her face must be 真白's own, one step younger. If she becomes a stranger, regenerate with the face-lock emphasized.
- **The rainbow may become VFX.** Rays, particles, or an aura are wrong. It is a slow bleed, a colored afterimage. If it glitters, dial it down.
- **ニジ may say わたし.** The first-person self-naming is withheld until S31. If it appears, regenerate the dialogue.
- **The model may stand ニジ in the room.** She sits on the screen only. If a full-size figure appears beside the desk, regenerate.

## Changes

- _(none yet)_

## Next Generation

- If ニジ renders opaque and in-screen, this hands off to S17 — where she names the word 真白 was about to whisper.
