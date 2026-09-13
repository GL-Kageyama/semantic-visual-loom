# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第6話 S25「最後に返すといいよ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**対話、指は休む——止まった指のままニジの言葉を聞く。「最後に返すといいよ」、36話にわたる返信の旅の出発点。理由の三段（いちばんたくさん預けてる／いちばん返すのが難しい／いちばん返したら何かが変わる）に重大さを押し込む。ニジは在・不透明・笑う（台帳 22–25）。**

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

> **No other character appears this segment.** ニジ is present — fully opaque, inside the screen only, smiling (ledger 22–25: 在・不透明・リストを指す). 湊 stays a name only — no face, no figure (his body first appears in S26).

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
- Appearance: `No new on-screen text this segment — the name 氷室湊 rests at the top of the list, unchanged from S24; dialogue only`
- Narrative Importance: `MEDIUM`
- Visual Importance: `LOW`
- Continuity Importance: `MEDIUM`

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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_06_宛先リスト、三十二人.md`
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

ニジ says it. 「……この人、最後に返すと、いいよ」. 真白 stares at 湊's name, unable to move.

## Beginning

The name 湊 still rests on the screen. 真白 stares at it, unable to move. 4時間52分 lingers at the edge of her mind.

## Turn

「……なぜ」. 「だって、おまえ、いちばんたくさん預けてるから。――いちばん返すのが難しくて。――いちばん返したら、――何かが変わるから」. ニジ smiles.

## Peak

真白 cannot move. A longing she cannot put into words. She had deposited time with someone she had only ever watched through a screen.

## Pull（引き — 切れ目）

――湊先輩に返す。――何を。――どうやって。Cut on the unanswered question, held in the dark.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The reason holds 9s (30%); the line holds 9s.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the bedroom; the stillness is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「動けない」.** 真白 stares at 湊's name, unable to move. The finger rests. 4時間52分 lingers at the edge of her mind. _Density: SPARSE — stillness, the finger at rest._
- **BEAT 2 `[0:06–0:15]` — 「最後に返すといいよ」 — the line.** ニジ says it. 「……この人、最後に返すと、いいよ」. 真白 「……なぜ」. _Density: TRANSITION — one line, one question._
- **BEAT 3 `[0:15–0:24]` — 「理由」 — longest share.** ニジ answers. 「だって、おまえ、いちばんたくさん預けてるから。――いちばん返すのが難しくて。――いちばん返したら、――何かが変わるから」. ニジ smiles. _Density: DENSE — the three-part reason, delivered lightly._
- **BEAT 4 `[0:24–0:30]` — 「何を。どうやって。」** 真白 cannot move. A longing without words. ――湊先輩に返す。――何を。――どうやって。Cut on the unanswered question. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `ニジ's line (≈0:08) ／ the three-part reason (≈0:16) ／ the unanswered question (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the frozen stillness), 0:24–0:30 (the held pull)`
- Dense regions: `0:15–0:24 (the reason)`
- Long continuous action: `0:00–0:06 the motionless 真白`
- Rapid transitions: `none — a quiet exchange in the dark`

---

# 9. ACTION

## Action — ACT_FROZEN

- ID: `ACT_FROZEN`
- Subject: `MASHIRO`
- Action: `Stares at 湊's name, unable to move. The finger rests, entirely still`
- Intention: `None — the body is held by what the name means`
- Intensity: `Medium, internal`
- Speed: `Zero, and held`

### Action Relationship

- Before: `— (continues from S24's held number)`
- After: `ACT_NIJI_LINE`

## Action — ACT_NIJI_LINE

- ID: `ACT_NIJI_LINE`
- Subject: `NIJI`
- Action: `Speaks 「……この人、最後に返すと、いいよ」 — bright, inside the screen, fully opaque`
- Intention: `To give 真白 an order she does not yet understand`
- Intensity: `Low`
- Speed: `Light, unguarded`

### Action Relationship

- Before: `ACT_FROZEN`
- After: `ACT_WHY`

## Action — ACT_WHY

- ID: `ACT_WHY`
- Subject: `MASHIRO`
- Action: `Speaks 「……なぜ」 — small, without moving`
- Intention: `To understand`
- Intensity: `Medium, suppressed`
- Speed: `A murmur`

### Action Relationship

- Before: `ACT_NIJI_LINE`
- After: `ACT_REASON`

## Action — ACT_REASON

- ID: `ACT_REASON`
- Subject: `NIJI`
- Action: `Answers 「だって、おまえ、いちばんたくさん預けてるから。――いちばん返すのが難しくて。――いちばん返したら、――何かが変わるから」 — and smiles`
- Intention: `To give the reason, lightly, without pressing`
- Intensity: `Low`
- Speed: `Even, gentle, teasing under the surface`

### Action Relationship

- Before: `ACT_WHY`
- After: `ACT_HELD`

## Action — ACT_HELD

- ID: `ACT_HELD`
- Subject: `MASHIRO`
- Action: `Does not move. The longing stays wordless. ――何を。――どうやって。`
- Intention: `None — the question has no answer yet`
- Intensity: `HIGH, internal, entirely still`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_REASON`
- After: `— (cut on the unanswered question)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Only the screen or her face are ever sharp`
- Depth of Field: `Very shallow — the room is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Locked on 真白's still face, lit from below, the name on the screen a soft bright edge in the foreground. She does not move.
- **`[0:06–0:15]`** — Slight slow drift toward ニジ inside the screen, speaking, smiling. Back to 真白 for 「……なぜ」.
- **`[0:15–0:24]`** — Two-shot of the screen and 真白's face, held — ニジ delivering the reason, 真白 listening without moving. No camera movement.
- **`[0:24–0:30]`** — A slow, almost imperceptible push-in on 真白's face, still and lit from below. Cut on the unanswered question.

---

# 11. MOTION

## Subject Motion

- 真白 does not move — the finger rests, the body holds. The reaction is a stillness
- Her lips part once, faintly, for 「……なぜ」 — and then nothing
- ニジ, inside the screen, smiles and speaks — fully opaque; her colors drift slowly blue → green → blue

## Object Motion

- The phone does not move on its own. Ever
- The name on the screen stays as it is — no glitch, no flicker, no supernatural transition
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion in the room
- ニジ's rainbow, inside the screen, is the only saturated hue

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand; the futon compresses under her`
- Inertia: `High — almost nothing moves`
- Acceleration: `None. The segment is held`
- Fluidity: `Limited-animation — holds punctuated by the smallest movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Stillness (held on the name, unable to move)
- ↓ An order, lightly given (最後に返すといいよ)
- ↓ The reason, in three parts (何かが変わるから)
- ↓ The unanswered question (何を。どうやって。)

## Emotional Events

- Event: `ニジ's line — 最後に返すといいよ` — Emotion: `A quiet pull — something is being set in motion` — Intensity: `MEDIUM` — Timing: `≈0:08`
- Event: `The reason — いちばん返したら、何かが変わるから` — Emotion: `The weight of it, delivered lightly` — Intensity: `HIGH, but quiet` — Timing: `≈0:18`
- Event: `The unanswered question — 何を。どうやって。` — Emotion: `Longing without words, held` — Intensity: `CRITICAL — expressed only as stillness` — Timing: `0:24–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo; ニジ's rainbow is the only saturated hue, and it lives inside the screen`

## Lighting Events

- **`[0:00]`** — Screen already on; the name is a soft bright edge in the foreground.
- **`[0:00–0:24]`** — Steady, cold. ニジ's rainbow, inside the screen, is the only color not drowned in indigo.
- **`[0:24–0:30]`** — A slow push-in on 真白's face, still and lit from below. Cut on the dark.

---

# 14. AUDIO

## Dialogue

- ニジ: 「……この人、最後に返すと、いいよ」 — bright, unguarded
- 真白: 「……なぜ」 — small, without moving
- ニジ: 「だって、おまえ、いちばんたくさん預けてるから。――いちばん返すのが難しくて。――いちばん返したら、――何かが変わるから」 — gentle, teasing under the surface

> ニジ never says 「わたし」. No narration, no voice-over.

## Sound Effects

- The wall clock's dry discrete ticking, faint throughout, growing louder in the held beats
- Soft futon fabric as she shifts, once, at the start
- The near-absence of sound — the finger no longer moves on the glass

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, warm under the reason, then resolving into stillness. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness, then thin after the reason — by the unanswered question there is only room tone, the clock, and a held breath`

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

- Speak only the three lines: ニジ 「……この人、最後に返すと、いいよ」 ／ 真白 「……なぜ」 ／ ニジ 「だって、おまえ、いちばんたくさん預けてるから。――いちばん返すのが難しくて。――いちばん返したら、――何かが変わるから」
- ニジ present, fully opaque, inside the screen only, smiling — 真白's own face one step younger, a rainbow afterimage
- 真白 stays frozen on 湊's name — the finger rests, nothing moves
- End on the unanswered question ――何を。――どうやって, cut on the dark

## MUST NOT（この1本の禁止・開示台帳 22–25 レンジより）

- **ニジ must not be transparent or translucent.** In S22–25 she is fully opaque (不透明)
- **ニジ must not say わたし.** She calls 真白 「おまえ」 and never refers to herself in first person
- ニジ never leaves the screen — she never stands in the room at human scale
- No rainbow or iridescence anywhere except ニジ herself, inside the screen
- **Do not show 湊.** He remains a name only — no face, no figure, no cutaway (his body first appears in S26)
- Do not have 真白 cry, gasp, or widen her eyes — the reaction is stillness

## PREFER

- Stillness over movement — the whole segment is a held breath
- Silence over score after the reason
- 真白's face over the screen, for the reaction

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The name on the screen may be slightly out of focus — the focus is 真白's stillness
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear fully opaque, inside the screen only (ledger 22–25 — 在・不透明・リストを指す), must not say わたし; 湊 must stay a name only (no face, no figure). This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:06] 真白 stares at a name on the screen — 氷室湊 — unable to move, the finger at rest; [0:06–0:15] ニジ, inside the screen, says ……この人、最後に返すと、いいよ, and 真白 answers ……なぜ; [0:15–0:24] ニジ answers だって、おまえ、いちばんたくさん預けてるから。――いちばん返すのが難しくて。――いちばん返したら、――何かが変わるから, and smiles; [0:24–0:30] 真白 does not move, the longing wordless — ――何を。――どうやって — and the shot cuts on the dark. The reason holds the largest share of the duration. Ends on the unanswered question, held, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. Night is deep indigo lit solely by the phone screen from below her face, her face nearly silhouetted, shadows soft and deep, no fill. The phone screen shows an ordinary Japanese UI in cold blue-white — a name, 氷室湊, resting at the top of the list. ニジ (Niji), inside the phone screen only, never in the room: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same head-tilt — a rainbow afterimage, fully opaque, no shadow, colors drifting slowly blue → green → blue, smiling; her rainbow is the only saturated hue. 湊 does not appear as a person — only his name. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost nothing moves. 真白 is frozen on the name, the finger at rest; her lips part once, faintly, for ……なぜ, and then nothing. ニジ, inside the screen, smiles and speaks, fully opaque; her rainbow afterimage drifts slowly blue → green → blue. Ordinary weight and inertia. The phone never moves by itself; its screen changes only by ordinary UI transitions, and the name stays as it is. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; only the screen or her face are sharp. Slow and deliberate, nearly still. [0:00–0:06] locked on 真白's still face lit from below, the name a soft bright edge in the foreground. [0:06–0:15] slight slow drift toward ニジ inside the screen, speaking and smiling, then back to 真白 for ……なぜ. [0:15–0:24] held two-shot of the screen and 真白's face, no camera movement. [0:24–0:30] a slow, almost imperceptible push-in on 真白's face, still and lit from below; cut on the dark.

## Audio Prompt

Deep quiet night room tone. The wall clock's dry discrete ticking, faint throughout, growing louder in the held beats. Soft futon fabric as she shifts once at the start. The near-absence of sound — the finger no longer moves on the glass. Three lines of dialogue only: ニジ ……この人、最後に返すと、いいよ, bright and unguarded; 真白 ……なぜ, small and still; ニジ だって、おまえ、いちばんたくさん預けてるから。――いちばん返すのが難しくて。――いちばん返したら、――何かが変わるから, gentle and teasing under the surface. ニジ never says わたし. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning after the reason, leaving only room tone, the clock, and a held breath. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparent figure, no translucent apparition, no see-through ghost, no ghost standing in the room at human scale, no figure outside the phone screen, no わたし spoken by ニジ, no rainbow or iridescence apart from ニジ herself, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep06-seg04-30s-01`
- Segment ID: `S25`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_06, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 9s / 9s / 6s. Reason = BEAT 3 at 9s (30%)`
- Camera Events: `4 events as listed in §10. No sustained dolly; all drift, hold, or push-in`
- Action Events: `ACT_FROZEN → ACT_NIJI_LINE → ACT_WHY → ACT_REASON → ACT_HELD`
- Audio Events: `three lines of dialogue ／ no screen text ／ music gone after the reason`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the dark`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ transparency.** The model may render ニジ as a see-through ghost, or standing in the room. She must be fully opaque and inside the screen only. Verify frame by frame.
- **ニジ saying わたし.** Her lines must call 真白 「おまえ」 and never slip into first person. Check the audio closely.
- **The stillness may read as emptiness.** The frozen 真白 is the emotion. If the model adds a gesture or a facial performance, the restraint is broken — keep the body and face still.
- **湊 may appear as a person.** He remains a name only here. Verify no face, no figure, no cutaway.

## Changes

- _(none yet)_

## Next Generation

- S26 is a scene change — day, school, and ニジ is absent. Do not carry the night bedroom or ニジ forward.
