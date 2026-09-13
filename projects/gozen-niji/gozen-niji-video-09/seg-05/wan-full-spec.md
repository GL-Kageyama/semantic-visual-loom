# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第9話 S40「返すと、薄くなる」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**欄が空いた。指は休む。記録を返したあとの静けさから、薄くなっていくニジの輪郭へ焦点が移る——第52本へ続く最初の薄まり。ニジは在・薄い（この薄まりが核心・画面の中だけ・「わたし」と名乗る・泣かない）。小春は文字のみ。画面文字なし（小春の欄が空いたスクリーンタイム）。感情はすべて、薄くなる輪郭と、言いかけて飲み込む「やめて」に押し込む。**

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

> **ニジ appears this segment**（ledger 36–40 — 在・薄い; the outline thins clearly from 39–40）. 小春 appears only as text — never as a person, face, or figure.

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
- Appearance: `No message text this segment — the screen-time log, with 小春's entry slightly emptied. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
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

That night 真白 opens the screen-time log and sees 小春's entry slightly emptied. 返せた. ニジ, in the screen, is growing thin — her rainbow fading — and she says it, calmly: 返すと、わたし、薄くなるんだよ。

## Beginning

Night. The screen-time log; 小春's entry is now slightly emptied. 真白, her voice trembling quietly: 「……返せた」「ニジ、返せたよ。ほら、空いた」

## Turn

ニジ: 「うん。届いたよ」 Then 真白 notices it — ニジ's body slightly transparent, the rainbow in the screen thinning. 「へへ。ちょっと、薄くなった」, with a smile that holds no lie.

## Peak

ニジ, calmly, as a fact: 「返すと、わたし、薄くなるんだよ。だって、わたしは、おまえが返さなかった、時間の塊だから。返した分だけ、還っていくの」

## Pull（引き — 切れ目）

真白 starts 「やめて」 and swallows it. Cut on the thinned ニジ. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The thinning holds 11s (37%) — the decisive reveal.

## Temporal Sequence

- **BEAT 1 `[0:00–0:05]` — 「空いた」.** Night. The screen-time log; 小春's entry now slightly emptied. _Density: SPARSE — quiet UI, the emptied entry, no event._
- **BEAT 2 `[0:05–0:13]` — 「返せた」.** 真白, her voice trembling quietly: 「……返せた」「ニジ、返せたよ。ほら、空いた」 ニジ: 「うん。届いたよ」 _Density: DENSE at the head (the exchange), then held._
- **BEAT 3 `[0:13–0:24]` — 「薄くなる」 — PEAK, longest share.** 真白 notices — ニジ's body slightly transparent, the rainbow thinning. ニジ: 「へへ。ちょっと、薄くなった」 ニジ: 「返すと、わたし、薄くなるんだよ。だって、わたしは、おまえが返さなかった、時間の塊だから。返した分だけ、還っていくの」 The outline thins, clearly, as the record is returned. _Density: DENSE at the head, then the thinned figure, held._
- **BEAT 4 `[0:24–0:30]` — 「やめて」.** 真白 starts 「やめて」 — and swallows it. Cut on the thinned ニジ. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `小春's emptied entry (≈0:03) ／ 返せた (≈0:08) ／ the thinning noticed (≈0:15) ／ the explanation (≈0:19) ／ the swallowed やめて (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:05 (the emptied entry), 0:24–0:30 (the swallowed word)`
- Dense regions: `0:05–0:13 (the exchange), 0:13–0:24 (the thinning)`
- Long continuous action: `0:13–0:24 the rainbow thinning, held`
- Rapid transitions: `none — a held, quiet segment`

---

# 9. ACTION

## Action — ACT_OPENLOG

- ID: `ACT_OPENLOG`
- Subject: `MASHIRO`
- Action: `Opens the screen-time log; 小春's entry is slightly emptied`
- Intention: `To confirm it — 返せた`
- Intensity: `Low, then rising`
- Speed: `Steady, then still`

### Action Relationship

- Before: `—` (continues from S39's reply, that same night)
- After: `ACT_EXCLAIM`

## Action — ACT_EXCLAIM

- ID: `ACT_EXCLAIM`
- Subject: `MASHIRO`
- Action: `「……返せた」「ニジ、返せたよ。ほら、空いた」 — her voice trembling, quietly happy`
- Intention: `To show her — the time was returned`
- Intensity: `Medium, a quiet joy`
- Speed: `Slow, trembling`

### Action Relationship

- Before: `ACT_OPENLOG`
- After: `ACT_ANSWER`

## Action — ACT_ANSWER

- ID: `ACT_ANSWER`
- Subject: `NIJI`
- Action: `「うん。届いたよ」 — then, as 真白 notices the thinning, 「へへ。ちょっと、薄くなった」 with a smile holding no lie`
- Intention: `To reassure her, and to state the fact lightly`
- Intensity: `Medium, bright`
- Speed: `Easy, unhurried`

### Action Relationship

- Before: `ACT_EXCLAIM`
- After: `ACT_EXPLAIN`

## Action — ACT_EXPLAIN

- ID: `ACT_EXPLAIN`
- Subject: `NIJI`
- Action: `「返すと、わたし、薄くなるんだよ。だって、わたしは、おまえが返さなかった、時間の塊だから。返した分だけ、還っていくの」 — calmly, as a fact`
- Intention: `To tell her the truth without asking for anything`
- Intensity: `CRITICAL, delivered without weight`
- Speed: `Even, gentle`

### Action Relationship

- Before: `ACT_ANSWER`
- After: `ACT_SWALLOW`

## Action — ACT_SWALLOW

- ID: `ACT_SWALLOW`
- Subject: `MASHIRO`
- Action: `Starts 「やめて」 and swallows it`
- Intention: `To stop what is happening, and not being able to`
- Intensity: `CRITICAL, suppressed to a breath`
- Speed: `A word, caught and held`

### Action Relationship

- Before: `ACT_EXPLAIN`
- After: `— (cut on the thinned ニジ)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, very shallow. Only the screen or her face is ever sharp`
- Depth of Field: `Very shallow — the room is a soft indigo blur`
- Camera Style: `Slow, deliberate, nearly still. One slow push to the screen as ニジ thins, and it belongs to the thinning`

## Camera Events

- **`[0:00–0:05]`** — Locked close on the screen — the screen-time log, 小春's entry slightly emptied. ニジ small in the corner, already thin.
- **`[0:05–0:13]`** — Cut to her face, lit from below, the voice trembling quietly on 返せた. Then back to the screen, ニジ answering.
- **`[0:13–0:24]`** — A slow continuous push in on ニジ inside the screen as her outline thins — the rainbow fading, blue → green → blue, weaker. The piece's single sustained move, and it belongs to the thinning.
- **`[0:24–0:30]`** — Hold on the thinned ニジ. Her lips move on やめて — and she swallows it. Cut on ニジ.

---

# 11. MOTION

## Subject Motion

- 真白's finger is at rest; almost all her movement is in the voice and the eyes
- ニジ barely moves — only her rainbow afterimage, drifting blue → green → blue, and now thinning, the colors weaker
- The thinning is the segment's only real "movement" — a slow, visible fading of the outline
- The swallowed やめて is a catch in the breath, not a gesture

## Object Motion

- The phone does not move on its own. Ever
- The screen-time log is still; only 小春's entry reads slightly emptied
- The wall clock's second hand advances in discrete ticks, faint behind

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only other motion
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; her hand rests on it`
- Inertia: `High for her body; near-total stillness`
- Acceleration: `None. The thinning is a slow, even fade, not a flicker`
- Fluidity: `Limited-animation — holds, and one slow fading of the outline`
- Impact: `None. The only event is a figure growing thin`

---

# 12. EMOTION

## Emotional Arc

- Quiet joy (返せた — the entry emptied)
- ↓ Lightness (ニジ's smile — ちょっと、薄くなった)
- ↓ The truth, calmly given (返すと、わたし、薄くなるんだよ)
- ↓ A refusal, swallowed (やめて — caught and held)

## Emotional Events

- Event: `「ニジ、返せたよ。ほら、空いた」` — Emotion: `Quiet joy, trembling` — Intensity: `MEDIUM` — Timing: `≈0:08`
- Event: `ニジ's outline thins` — Emotion: `The truth, arriving without drama` — Intensity: `CRITICAL, delivered lightly` — Timing: `≈0:15, held to 0:24`
- Event: `The swallowed やめて` — Emotion: `A refusal she cannot complete` — Intensity: `CRITICAL, suppressed` — Timing: `≈0:26`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo; ニジ's rainbow is the only saturated hue, and it is thinning`

## Lighting Events

- **`[0:00]`** — Screen on, its light on the ceiling as a soft blue rectangle.
- **`[0:13–0:24]`** — ニジ's rainbow — the only saturated color in the frame — thins and weakens as the camera closes, blue → green → blue, dimmer.
- **`[0:24–0:30]`** — The rainbow at its faintest, still present. Cut on the thinned ニジ.

---

# 14. AUDIO

## Dialogue

- 真白: 「……返せた」 — quiet, the voice trembling
- 真白: 「ニジ、返せたよ。ほら、空いた」 — a quiet, happy tremor
- ニジ: 「うん。届いたよ」 — bright, easy
- ニジ: 「へへ。ちょっと、薄くなった」 — a small laugh, a smile holding no lie
- ニジ: 「返すと、わたし、薄くなるんだよ。だって、わたしは、おまえが返さなかった、時間の塊だから。返した分だけ、還っていくの」 — calm, matter-of-fact
- 真白: 「やめて」 — started, and swallowed; a caught breath

## Sound Effects

- The wall clock's dry discrete ticking, faint throughout
- A soft fabric rustle as she shifts once at the start
- The thinning of ニジ makes no sound

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Tender, and quietly sorrowful underneath. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the explanation, then thin — like the rainbow — leaving only room tone and the clock`

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

- ニジ present, **clearly thin** — her outline distinctly thinner, semi-transparent, the rainbow fading blue → green → blue, weaker
- Let the outline thin **as the record is returned** — this is the segment's core
- Render ニジ's explanation: 「返すと、わたし、薄くなるんだよ。だって、わたしは、おまえが返さなかった、時間の塊だから。返した分だけ、還っていくの」
- ニジ smiles lightly — へへ、ちょっと、薄くなった — a smile holding no lie; she never cries
- 真白 starts 「やめて」 and swallows it
- End by cutting on the thinned ニジ, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 36–40 レンジより）

- **No full disappearance.** ニジ thins, but never vanishes, dissolves, or fades out — she must remain present, however thin
- ニジ stays inside the screen; she never stands in the room at human scale
- 小春 appears only as text — never as a person, face, or figure
- No other person, crowd, or silhouette
- ニジ must not cry

## PREFER

- The thinning slow and even — a fade, not a flicker
- The explanation delivered lightly, as a fact, not a tragedy
- Silence over score at the explanation

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The push to the screen may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ is present and clearly thin — the outline thins as the record is returned, but never fully disappears (ledger 36–40); 小春 appears only as text. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at night. ニジ is present inside the screen, now clearly thin, and thinning. Beats, deliberately uneven: [0:00–0:05] the screen-time log is open, 小春's entry slightly emptied; [0:05–0:13] 真白, her voice trembling quietly, says ……返せた and ニジ、返せたよ。ほら、空いた and ニジ answers うん。届いたよ; [0:13–0:24] THE THINNING — 真白 notices ニジ's body slightly transparent, the rainbow fading, and ニジ says, calmly, へへ。ちょっと、薄くなった then 返すと、わたし、薄くなるんだよ。だって、わたしは、おまえが返さなかった、時間の塊だから。返した分だけ、還っていくの as her outline thins, clearly, as the record is returned; [0:24–0:30] 真白 starts やめて and swallows it, and the shot cuts on the thinned ニジ. The thinning holds the largest share of the duration. Ends on the thinned ニジ, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ, inside the screen only, is 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same tilt of the head — a blurred rainbow afterimage resolved into that outline, colors drifting slowly blue → green → blue, no shadow anywhere, now clearly thin, her outline distinctly thinner and semi-transparent, the rainbow fading as the record is returned. The screen shows an ordinary Japanese UI in cold blue-white — the screen-time log, one entry slightly emptied. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. 真白's finger is at rest; almost all her movement is in the voice and the eyes. ニジ barely moves — only her rainbow afterimage, drifting slowly blue → green → blue, and now thinning, the colors weaker, the outline fading slowly and evenly as the record is returned. The thinning is the segment's only real movement — a slow, visible fade, not a flicker. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or her face is sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:05] locked close on the screen — the screen-time log, 小春's entry slightly emptied, ニジ small in the corner, already thin. [0:05–0:13] cut to her face lit from below on 返せた, then back to the screen, ニジ answering. [0:13–0:24] a slow continuous push in on ニジ inside the screen as her outline thins, the rainbow fading blue → green → blue, weaker. [0:24–0:30] hold on the thinned ニジ, her lips moving on やめて and swallowing it; cut on ニジ.

## Audio Prompt

Almost silent. Deep quiet night room tone and a wall clock ticking, dry and discrete, faint throughout. A soft fabric rustle once at the start. Dialogue, quiet and unhurried: 真白 says ……返せた, then ニジ、返せたよ。ほら、空いた, her voice trembling with a quiet joy; ニジ answers うん。届いたよ, bright and easy, then へへ。ちょっと、薄くなった, a small laugh with no lie, then 返すと、わたし、薄くなるんだよ。だって、わたしは、おまえが返さなかった、時間の塊だから。返した分だけ、還っていくの, calm and matter-of-fact; 真白 starts やめて and swallows it, a caught breath. The thinning makes no sound. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning like the rainbow toward the close and leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no full disappearance, no complete vanishing, no dissolving into nothing, no fading out to invisibility, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep09-seg05-30s-01`
- Segment ID: `S40`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_09, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 5s / 8s / 11s / 6s. Thinning = BEAT 3 at 11s (37%)`
- Camera Events: `4 events as listed in §10. One sustained push (0:13–0:24)`
- Action Events: `ACT_OPENLOG → ACT_EXCLAIM → ACT_ANSWER → ACT_EXPLAIN → ACT_SWALLOW`
- Audio Events: `five lines of dialogue ／ the swallowed やめて ／ clock throughout ／ the thinning silent`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the thinned ニジ`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ may vanish entirely.** This is the highest-risk frame of the range. She must thin — clearly — but never disappear. If she vanishes, regenerate and hold her at a faint-but-present semi-transparent outline.
- **The thinning may read as a flicker.** It must be a slow, even fade tied to the returned record, not a glitch or a dissolve-to-nothing.
- **The model may add tears.** ニジ never cries. She smiles lightly. If tears appear, it breaks the character rule.
- **The explanation may be over-weighted.** 「返すと、わたし、薄くなるんだよ」 must be delivered lightly, as a fact — not a tragedy.

## Changes

- _(none yet)_

## Next Generation

- If the thinning reads clearly and ニジ stays present, S41 (下から返していく) begins 真白 returning the remaining time, one addressee at a time.
