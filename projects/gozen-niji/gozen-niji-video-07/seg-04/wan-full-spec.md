# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第7話 S30「ひとつも無駄じゃなかったよ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**一番長く止まる名前（湊）と、ニジの初めての声——「おまえの時間は、ひとつも無駄じゃなかったよ」。その笑顔は、これまでで一番まぶしかった。ニジは画面の中に、不透明で在る（「わたし」はまだ言わない）。**

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

> **ニジ appears this segment**（ledger 29–30 — in, opaque; not yet わたし）. No other character appears — 美月・小春・湊 do not appear.

---

# 4. ENVIRONMENT

## Location

- ID: `CLASSROOM`
- Name: `教室 (the darkened classroom, night)`
- Description: `The classroom at night — 真白 alone, the phone screen the only light, ニジ inside the screen. The screen's light on her face in the dark`

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
- Appearance: `No message text this segment — the list stays open under the finger, ordinary diegetic UI. The dialogue is spoken, not text. No captions, no subtitles`
- Narrative Importance: `LOW`
- Visual Importance: `LOW`
- Continuity Importance: `LOW`

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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_07_文化祭前夜、スクリーンタイムを全部開く.md`
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

真白 calls out to ニジ and confirms her realization. ニジ answers — おまえの時間は、ひとつも無駄じゃなかったよ — and her smile is the brightest 真白 has ever seen.

## Beginning

The finger that was stroking the names stops longest on one name — 湊. 真白 looks up. 「……ねえ、ニジ」

## Turn

「うん？」「私の時間、――全部、宛先付いてるね」「うん。付いてる」「……ひとつも、逃げてないね」

## Peak

「うん。――おまえの時間は、――ひとつも無駄じゃ、なかったよ」

## Pull（引き — 切れ目）

On the far side of the screen, ニジ smiles — her usual unguarded smile, but to 真白 brighter than any smile she has ever seen. In the dark classroom, the screen's light falls on 真白's face. Cut on ニジ's smile.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** ニジ's answer holds 9s (30%); the longest-stop name is held 6s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「一番長く止まる名前」 — the stop, made visible.** The stroking finger stops and holds longest on one name — 湊. 真白 looks up. _Density: SPARSE — one deliberate stop, and its half-beat of address._
- **BEAT 2 `[0:06–0:16]` — 「ねえ、ニジ」 — the exchange.** 「……ねえ、ニジ」――「うん？」「私の時間、全部、宛先付いてるね」――「うん。付いてる」「……ひとつも、逃げてないね」。 _Density: DENSE — a quick back-and-forth, the confirmation._
- **BEAT 3 `[0:16–0:25]` — 「ひとつも無駄じゃなかった」 — ニジ's answer, longest share.** 「うん。――おまえの時間は、――ひとつも無駄じゃ、なかったよ」。 _Density: DENSE at the head, then the line, held._
- **BEAT 4 `[0:25–0:30]` — 「ニジの笑顔」 — held, then cut.** ニジ smiles — her usual unguarded smile, brighter than any before it; the screen's light on 真白's face. Cut on the smile. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the finger stopping longest on one name (≈0:04) ／ the exchange (0:06–0:16) ／ ニジ's ひとつも無駄じゃなかったよ (≈0:18) ／ the dazzling smile (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the stop), 0:25–0:30 (the smile)`
- Dense regions: `0:06–0:16 (the exchange), 0:16–0:25 (the answer)`
- Long continuous action: `0:25–0:30 the smile, held`
- Rapid transitions: `none — a slow, held night`

---

# 9. ACTION

## Action — ACT_STOP_NAME

- ID: `ACT_STOP_NAME`
- Subject: `MASHIRO`
- Action: `The stroking finger stops, and holds longest on one name — 湊`
- Intention: `Not reading — arriving. The name she stops on longest`
- Intensity: `Medium`
- Speed: `Slow, then still`

### Action Relationship

- Before: `— (continues from S29's stroking finger)`
- After: `ACT_ASK`

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MASHIRO`
- Action: `Looks up and speaks — 「……ねえ、ニジ」「私の時間、全部、宛先付いてるね」「……ひとつも、逃げてないね」`
- Intention: `To confirm what the list showed her`
- Intensity: `Low, quiet`
- Speed: `Slow, small voice`

### Action Relationship

- Before: `ACT_STOP_NAME`
- After: `ACT_ANSWER`

## Action — ACT_ANSWER

- ID: `ACT_ANSWER`
- Subject: `NIJI`
- Action: `Answers — 「うん。付いてる」、then 「うん。――おまえの時間は、――ひとつも無駄じゃ、なかったよ」`
- Intention: `To reassure — plainly, without drama`
- Intensity: `Medium`
- Speed: `Bright, even — 句点で切る`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_SMILE`

## Action — ACT_SMILE

- ID: `ACT_SMILE`
- Subject: `NIJI`
- Action: `Smiles — her usual unguarded smile, but this time brighter than any 真白 has seen — まぶしい`
- Intention: `None — the smile is simply there, and it is dazzling`
- Intensity: `Medium, warm`
- Speed: `Still, and held`

### Action Relationship

- Before: `ACT_ANSWER`
- After: `— (cut on the smile)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Into the screen with her`
- Lens Character: `Long-ish, shallow. Only the screen or her face are ever sharp`
- Depth of Field: `Very shallow — the classroom falls away into near-black`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:04]`** — Locked close on the list, the finger stroking the names, then stopping and holding longest on one — 湊.
- **`[0:04–0:06]`** — Rack focus up to 真白's face, lit from below, as she looks up.
- **`[0:06–0:14]`** — A gentle two-shot — 真白's face and, in the screen, ニジ — through the exchange, the screen's light between them.
- **`[0:14–0:16]`** — Close on ニジ, inside the screen — her face, 真白's face one step younger, opaque.
- **`[0:16–0:24]`** — Hold on ニジ as she says おまえの時間は、ひとつも無駄じゃなかったよ。 No camera movement.
- **`[0:24–0:30]`** — Close on ニジ's smile — the rainbow afterimage soft behind her — and, once, the screen's light on 真白's face. Cut on the smile.

---

# 11. MOTION

## Subject Motion

- The finger strokes, then stops and holds on one name — a single, deliberate stillness
- 真白's face is still, lit from below; only her lips move, small
- ニジ inside the screen is still, then smiles — the only real motion, held

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a list under the finger. Nothing glitches, flickers, or distorts
- ニジ's rainbow colors drift slowly — blue → green → blue — the only continuous motion

## Environmental Motion

- The classroom is still and dark; nothing moves in it
- No wind, no moving shadows, no particles

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand`
- Inertia: `High for the bodies, near-zero for the finger`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Arrival (the finger stopping longest on one name)
- ↓ Confirmation (the exchange — 全部、宛先付いてるね)
- ↓ Reassurance (おまえの時間は、ひとつも無駄じゃなかったよ)
- ↓ Dazzlement (the smile brighter than any before it)

## Emotional Events

- Event: `The finger stops longest on 湊's name` — Emotion: `Arrival — the stroking resolving into a stop` — Intensity: `MEDIUM` — Timing: `≈0:04`
- Event: `ニジ's おまえの時間は、ひとつも無駄じゃなかったよ` — Emotion: `Reassurance — plain, warm, without drama` — Intensity: `HIGH` — Timing: `≈0:18`
- Event: `ニジ's smile` — Emotion: `Dazzlement — まぶしい, brighter than any smile before` — Intensity: `HIGH, held — no facial performance, the light carries it` — Timing: `0:25–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft darkness fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `Near-black. The classroom is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against near-black; ニジ's rainbow the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on her face from below.
- **`[0:04–0:14]`** — The screen's light carries the exchange, between her face and ニジ's.
- **`[0:16–0:24]`** — Close on ニジ inside the screen — her rainbow the frame's only saturated color, cold blue-white on 真白's face outside.
- **`[0:24–0:30]`** — The smile; the screen's light soft on 真白's face. Cut on the smile.

---

# 14. AUDIO

## Dialogue

- 真白: 「……ねえ、ニジ」→「私の時間、――全部、宛先付いてるね」→「……ひとつも、逃げてないね」 — quiet, small voice
- ニジ: 「うん？」→「うん。付いてる」→「うん。――おまえの時間は、――ひとつも無駄じゃ、なかったよ」 — bright, even, 句点で切る

> No other speech. ニジ does not yet use the subject わたし. No narration, no voice-over.

## Sound Effects

- The soft friction of a thumb on glass, once, as the finger strokes and stops
- The near-silence of an emptied school at night

## Environment

- Deep quiet, almost nothing

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, warm. Never sinister, never sentimental — no horror strings, no swelling`
- Emotional Function: `Hold the room's stillness under the exchange, then thin to nothing at the smile, leaving only room tone`

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

- Render ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same head-tilt — a blurred rainbow afterimage, **fully opaque**, inside the screen only, never at human scale in the room
- The finger stops and holds longest on one name (湊) before she speaks
- ニジ's line is exactly: おまえの時間は、ひとつも無駄じゃなかったよ — spoken plainly, 句点で切る
- End on ニジ's smile, brighter than any before — cut on the smile

## MUST NOT（この1本の禁止・開示台帳 29–30 レンジより）

- **Do not make ニジ transparent.** No translucent apparition, no see-through figure, no fading ghost — she is opaque
- **Do not give ニジ the subject わたし.** She calls 真白 「おまえ」 and does not yet say わたし (her first わたし belongs to S31)
- **ニジ must not cry.** Her smile may be dazzling, but no tears — she does not know how to cry
- No 美月, no 小春, no 湊 as live figures — only 真白 and ニジ
- No on-screen subtitles or captions burned in (the dialogue is spoken, not text)
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- ニジ's smile over any performed emotion — the light carries the dazzlement
- The stopped finger over any explicit statement of feeling
- Silence over score at the smile

## ALLOW

- Slight variation in the list's layout and the classroom furnishing
- The two-shot of 真白 and ニジ may be a single shot or a cut between them
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must be shown fully opaque inside the screen (ledger 29–30 — in, opaque); she does not yet say わたし; no other character. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school girl alone in her darkened classroom at night, ニジ inside the phone screen. Beats, deliberately uneven: [0:00–0:06] the stroking finger stops and holds longest on one name — 湊 — and 真白 looks up; [0:06–0:16] the exchange — 真白: 私の時間、全部、宛先付いてるね…ひとつも、逃げてないね; ニジ: うん。付いてる; [0:16–0:25] ニジ's answer: うん。――おまえの時間は、――ひとつも無駄じゃ、なかったよ; [0:25–0:30] ニジ smiles — her usual unguarded smile, but brighter than any 真白 has seen, まぶしい — and the shot cuts on the smile. ニジ is fully opaque, no shadow, inside the screen only, 真白's own face one step younger with the same shoulder-length dark hair and thin neck, a rainbow afterimage. The answer holds the largest share. Ends on the smile, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. By day she wears a standard Japanese school uniform; here, after school, she is alone in the classroom in that uniform. A darkened classroom: the phone screen the only light, cold blue-white from below, her face nearly silhouetted, shadows deep and soft, no fill. ニジ: inside the screen only, never at human scale in the room — 真白's own face one step younger (longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same head-tilt), a blurred rainbow afterimage that resolves into that outline, fully opaque, no shadow, colors drifting slowly blue → green → blue, smiling. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. The finger strokes, then stops and holds on one name — a single deliberate stillness. 真白's face is still, lit from below; only her lips move, small. ニジ inside the screen is still, then smiles — the only real motion, held. Her rainbow colors drift slowly, blue → green → blue. Ordinary weight and inertia: the phone has heft in her hand. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. Only the screen's bloom breathes faintly in the dark. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder — into the screen with her. Longish lens, very shallow depth of field; only the screen or her face are ever sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:04] locked close on the list, the finger stroking the names, then stopping and holding longest on one — 湊. [0:04–0:06] rack focus up to 真白's face, lit from below. [0:06–0:14] a gentle two-shot of 真白's face and, in the screen, ニジ, through the exchange. [0:14–0:16] close on ニジ inside the screen, opaque. [0:16–0:24] hold on ニジ as she says おまえの時間は、ひとつも無駄じゃなかったよ, no camera movement. [0:24–0:30] close on ニジ's smile, the rainbow afterimage soft behind her; cut on the smile.

## Audio Prompt

Deep quiet night room tone — the near-silence of an emptied school. The soft friction of a thumb on glass, once, as the finger strokes and stops. Dialogue only, small and warm: 真白 — ……ねえ、ニジ; 私の時間、全部、宛先付いてるね; ……ひとつも、逃げてないね. ニジ — うん？; うん。付いてる; うん。――おまえの時間は、――ひとつも無駄じゃ、なかったよ, bright and even, 句点で切る. ニジ does not use the subject わたし. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning to nothing at the smile, leaving only room tone. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparency, no translucent apparition, no see-through figure, no fading ghost, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep07-seg04-30s-01`
- Segment ID: `S30`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_07, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 10s / 9s / 5s. ニジ's answer = BEAT 3 at 9s (30%)`
- Camera Events: `6 events as listed in §10. One rack focus (0:04–0:06)`
- Action Events: `ACT_STOP_NAME → ACT_ASK → ACT_ANSWER → ACT_SMILE`
- Audio Events: `dialogue (真白 + ニジ) ／ thumb-on-glass once ／ music thinning to nothing at the smile`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the smile`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ reads as a translucent ghost.** She must be fully opaque. If the model renders her see-through, strengthen the "no transparency" front-load.
- **The smile may read as sentimental.** まぶしい is a brightness, not a tearful smile. If tears or a performed sweetness appear, regenerate — ニジ does not know how to cry.
- **The finger may not stop on a single name.** The whole beat rests on the stroke resolving into one held stop. If it keeps stroking, hold the close on the finger longer.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the stop, the answer, and the smile all read, this segment is done; S31 is the key beat — ニジ looks into 真白's eyes for the first time and says わたし for the first time.
