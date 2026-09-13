# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第11話 S48「時間を預けてました」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「時間を預けてました」——手は空のまま、面と向かって言葉で渡す（指の背骨の第48本）。画面の文字でしか「届ける」を知らなかった主人公が、初めて声で告白する。最大の秒は「……私、あなたに、時間を預けてました」という告白と、その説明、湊の返答に配る。ニジは不在（第11話に幽霊はいない）。登場人物は真白と湊のみ。画面文字なし（対話のみ）。**

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

> **湊 appears this segment**（third-year 氷室湊 — festival committee, composed, carries document bundles）. ニジ is absent（ledger 46–51 — the ghost does not appear in this chapter）.

---

# 4. ENVIRONMENT

## Location

- ID: `FESTIVAL_YARD`
- Name: `文化祭の裏庭 (the festival back yard)`
- Description: `Back yard at night, paper lanterns, food-stall smoke and light — warm pools of lantern light floating in deep indigo night`

## Environmental Behavior

- Wind: `none — the curtain does not move`
- Particles: `only the faintest haze catching the screen's bloom; no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; at most one distant car's headlights crossing the curtain, once`

---

# 5. OBJECTS

## PHONE

- Type: `smartphone (湊's)`
- Appearance: `Dim and ordinary in 湊's hand, plain case, Japanese UI, its content unreadable. 真白 carries no phone this segment — her hands are empty and still`
- Narrative Importance: `LOW`
- Visual Importance: `LOW`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_11_最後の宛先、湊.md`
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

真白 confesses to 湊, in the festival yard: 「……私、あなたに、時間を預けてました」. He does not understand — 「……時間？」 — and she explains: she watched his back for a year, and she can now say her time was not wasted. He looks at her a long while, and then smiles a smile she has never seen.

## Beginning

The unfinished 「あの、――」 from the beat before. 言う前に、どうせ、と思った。どうせ、私は湊先輩のこと、何も知らない。どうせ、湊先輩は私のこと、知らない。でも、真白は言う。

## Turn

「……私、あなたに、時間を預けてました」 — the confession, out loud, to a person, for the first time in the series. 「……時間？」

## Peak

Her explanation: 変な話だとは思うんです。でも、私は、あなたの背中をずっと見てました。あなたが頑張ってるところを。私の時間は、無駄じゃなかったって、今なら言えます。 The lantern light sways in the wind; 湊's shadow sways and returns.

## Pull（引き — 切れ目）

湊 looks at her for a long while — その間、真白は、提灯の灯りを見てた — and then smiles, 真白の知らない笑い方、目じりが下がる笑い方。「……変な人だな」。 Cut on the smile.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The confession holds 10s (33%); the smile is held 6s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「どうせ」 — ESTABLISH.** The unfinished あの、 from before. 言う前に、どうせ、と思う。どうせ、私は湊先輩のこと、何も知らない。どうせ、湊先輩は私のこと、知らない。でも、真白は言う。_Density: SPARSE, internal — a doubt she talks herself past._
- **BEAT 2 `[0:06–0:16]` — 「預けてました」 — TURN, longest share.** 「……私、あなたに、時間を預けてました」. 「……時間？」. The series' private word, spoken to a person for the first time. _Density: DENSE at the head, then held on the word between them._
- **BEAT 3 `[0:16–0:24]` — 「背中」 — PEAK.** 変な話だとは思うんです。でも、私は、あなたの背中をずっと見てました。あなたが頑張ってるところを。私の時間は、無駄じゃなかったって、今なら言えます。The lantern light sways; 湊's shadow sways and returns. _Density: TRANSITION — the explanation, and the world's faint answer._
- **BEAT 4 `[0:24–0:30]` — 「変な人だな」 — PULL.** 湊 looks at her a long while, then smiles — 真白の知らない笑い方、目じりが下がる笑い方。「……変な人だな」. Cut on the smile. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the confession 「……私、あなたに、時間を預けてました」 (≈0:08) ／ the explanation (≈0:18) ／ 湊's unfamiliar smile and 「……変な人だな」 (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the doubt), 0:24–0:30 (the held smile)`
- Dense regions: `0:06–0:16 (the confession)`
- Long continuous action: `0:24–0:30 湊 looking at her, then the smile`
- Rapid transitions: `none — a slow, warm exchange`

---

# 9. ACTION

## Action — ACT_STEEL

- ID: `ACT_STEEL`
- Subject: `MASHIRO`
- Action: `Talks herself past the doubt — どうせ、と思う。でも、言う`
- Intention: `To speak anyway, knowing it may mean nothing`
- Intensity: `Medium, internal`
- Speed: `Still; the breath gathers`

### Action Relationship

- Before: `—` (continues from S47's unfinished word)
- After: `ACT_CONFESS`

## Action — ACT_CONFESS

- ID: `ACT_CONFESS`
- Subject: `MASHIRO`
- Action: `Says 「……私、あなたに、時間を預けてました」 out loud, to him`
- Intention: `To hand over the truth of the past year`
- Intensity: `CRITICAL (the emotional peak, spoken plain)`
- Speed: `Slow, quiet, deliberate — a small voice that does not break`

### Action Relationship

- Before: `ACT_STEEL`
- After: `ACT_EXPLAIN`

## Action — ACT_EXPLAIN

- ID: `ACT_EXPLAIN`
- Subject: `MASHIRO`
- Action: `Explains — あなたの背中をずっと見てました、私の時間は無駄じゃなかった`
- Intention: `To make him understand the confession is not strange, but true`
- Intensity: `Medium, internal`
- Speed: `Slow, halting, then firm on the last line`

### Action Relationship

- Before: `ACT_CONFESS`
- After: `ACT_SMILE`

## Action — ACT_SMILE

- ID: `ACT_SMILE`
- Subject: `MINATO`
- Action: `Looks at her a long while, then smiles — 目じりが下がる笑い方 — and says 「……変な人だな」`
- Intention: `Not mockery — warmth. He has understood something`
- Intensity: `Medium`
- Speed: `Slow; the smile arrives whole`

### Action Relationship

- Before: `ACT_EXPLAIN`
- After: `— (cut on the smile)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, face-to-face. Two-shot, then alternating close-ups`
- Lens Character: `Long-ish, shallow. The festival falls away soft behind`
- Depth of Field: `Shallow — 真白 sharp while she speaks, then 湊 sharp as he smiles`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Static close on 真白, her face unreadable, the doubt gathering. The lanterns glow soft behind her.
- **`[0:06–0:13]`** — Hold on 真白 as the confession leaves her mouth — the words plain and quiet, the camera not moving.
- **`[0:13–0:16]`** — Cut to 湊, static, close. 「……時間？」 — not mocking, simply not understanding.
- **`[0:16–0:22]`** — Cut back to 真白 as she explains, the lantern light swaying across her face with the faint wind.
- **`[0:22–0:26]`** — A slow rack focus off 真白 onto 湊 across from her, his shadow swaying on the ground and returning.
- **`[0:26–0:30]`** — Hold on 湊's face as the smile forms — 目じりが下がる笑い方. 「……変な人だな」 Cut on the smile.

---

# 11. MOTION

## Subject Motion

- 真白's body is nearly still; only her mouth moves as she confesses and explains, slow and quiet
- Her hands stay empty and still at her sides throughout
- 湊 is still, watching her; his single motion is the smile, which forms slowly, the corners of his eyes dropping
- The look between them carries the whole segment

## Object Motion

- The lantern light sways once in a faint wind; 湊's shadow sways on the ground and returns
- Nothing glitches, flickers, distorts, or behaves supernaturally

## Environmental Motion

- The festival is alive only in soft, out-of-focus movement — distant figures, drifting smoke
- No wind beyond the one faint sway; no moving shadows beyond the sway of the lantern

## Physical Characteristics

- Weight: `Ordinary. The two of them stand with ordinary weight`
- Inertia: `High for both bodies; near-zero movement throughout`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Doubt (どうせ、私は何も知らない)
- ↓ Courage (the confession, spoken anyway)
- ↓ Vulnerability (the explanation — a year, laid open)
- ↓ Warmth received (his smile, a kind she has never seen)

## Emotional Events

- Event: `「……私、あなたに、時間を預けてました」` — Emotion: `Courage over doubt — the truth finally spoken` — Intensity: `CRITICAL, expressed as plain speech, never performance` — Timing: `≈0:08`
- Event: `Her explanation` — Emotion: `Vulnerability — あなたの背中をずっと見てました` — Intensity: `HIGH, internal` — Timing: `≈0:18`
- Event: `湊's smile — 真白の知らない笑い方` — Emotion: `Warmth received, not yet understood` — Intensity: `MEDIUM` — Timing: `≈0:26`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Warm paper-lantern glow — amber, soft, low-saturation, from around and above`
- Fill Light: `Soft, even. The lanterns and stall lights fill the yard`
- Rim Light: `A faint warm edge on both their hair and shoulders`
- Ambient Light: `Deep indigo night with warm pools of lantern light`
- Color Temperature: `≈2900K lantern light against deep indigo night — warm, muted`

## Lighting Events

- **`[0:00]`** — Both faces in the lantern light, warm and even.
- **`[0:06–0:16]`** — The light holds steady on 真白's face as she confesses.
- **`[0:16–0:22]`** — The lantern light sways once across her face — a soft, warm movement, nothing more.
- **`[0:22–0:26]`** — The light swings gently onto 湊, his shadow swaying and returning.
- **`[0:26–0:30]`** — Warm and even on his face as the smile forms. Cut.

---

# 14. AUDIO

## Dialogue

- 真白: 「……私、あなたに、時間を預けてました」 — small, quiet, deliberate
- 湊: 「……時間？」 — low, not mocking
- 真白: 「変な話だとは思うんです。――でも、私は、あなたの背中をずっと見てました。あなたが頑張ってるところを。――私の時間は、無駄じゃなかったって、――今なら言えます」
- 湊: 「……変な人だな」 — low, warm

> No other speech. No narration, no voice-over.

## Sound Effects

- The soft night festival continuing — distant laughter, stall voices, the sizzle of food
- The faint creak of a paper lantern swaying once in the wind

## Environment

- Open night air, warm and full, unbothered

## Music

- Style: `Sparse — a few sustained tones, or nothing`
- Tempo: `Slow`
- Mood: `Warm, held, tender. Never sinister, never sentimental`
- Emotional Function: `Hold the space under the confession. It thins as 湊 smiles, leaving only the crowd murmur and the two voices`

---

# 15. CONTINUITY

> 57本は57回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

- **Identity**: 真白 — plain Japanese high-school girl 16–17, shoulder-length dark hair, thin neck, small frame, curved posture over a phone. Same face in every take.
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen.
- **The room**: futon on the floor, curtained window, wall clock, sparse.
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light.
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue.
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。Negative の土台は series-constants のもの＋先頭にこの本の禁止。

## MUST

- Render the spoken lines exactly: 「……私、あなたに、時間を預けてました」／「……時間？」／ the explanation ／「……変な人だな」
- Keep the confession plain and spoken — no SF tone, no drama; it is a girl's awkward truth
- Show 湊's smile as 真白の知らない笑い方 — the corners of his eyes dropping, warm, not mocking
- Keep 真白's hands empty and still throughout
- End by cutting on the smile, nothing after it

## MUST NOT（この1本の禁止・開示台帳 46–51 レンジより）

- **ニジは登場しない。** No ghost, no figure, no silhouette, no reflection, no second person, no eyes but the two living people's own. This episode has no ニジ at all
- **No rainbow, no iridescence, no colored afterimage**
- **No on-screen text.** The confession is spoken, not typed; no phone screen shows it
- Do not make 湊 mocking, cruel, or sinister — 「変な人だな」 is warmth, not a put-down
- Do not give this night horror grammar
- Do not have 真白 cry or break down; the confession is delivered whole and steady

## PREFER

- The sway of the lantern as the only physical response to the confession — the world answering softly
- Silence over score at the smile
- Negative space over detail

## ALLOW

- Slight variation in lantern pattern and crowd shapes
- The rack focus may be omitted (a fully locked two-shot is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not appear (ledger 46–51 — the ghost does not appear in this chapter); only 真白 and 湊. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a night culture festival in a school back yard. Beats, deliberately uneven: [0:00–0:06] 真白 gathers herself past the doubt — どうせ、私は湊先輩のこと、何も知らない、どうせ、湊先輩は私のこと、知らない、でも真白は言う; [0:06–0:16] THE CONFESSION — she says ……私、あなたに、時間を預けてました, and 湊 answers ……時間？, the series' private word spoken to a person for the first time; [0:16–0:24] she explains — 変な話だとは思うんです、でも私はあなたの背中をずっと見てました、私の時間は無駄じゃなかったって今なら言えます — and the lantern light sways once, 湊's shadow swaying and returning; [0:24–0:30] 湊 looks at her a long while and then smiles a smile she has never seen, 目じりが下がる笑い方, and says ……変な人だな, and the shot cuts on the smile. The confession holds the largest share of the duration. Ends on the smile, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. She wears her standard Japanese school uniform; her hands are empty. Scene: a school festival back yard at night — warm soft paper lanterns, drifting smoke, indigo night air. Facing her, 湊 (Minato) — a third-year boy, festival committee, composed and quiet, short neat dark hair, in the boys' school uniform, a little taller, with a calm face whose smile lowers the corners of his eyes. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Bodies hold almost completely still. 真白's only movement is her mouth, confessing and explaining slow and quiet; her hands stay empty and still at her sides. 湊 is still, watching her; his single motion is the smile, forming slowly, the corners of his eyes dropping. The lantern light sways once in a faint wind; 湊's shadow sways on the ground and returns. The festival crowd is alive only in soft, out-of-focus movement. Nothing glitches, flickers or distorts. Gentle acceleration everywhere. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, face-to-face. Longish lens, shallow depth of field; 真白 sharp while she speaks, then 湊 sharp as he smiles. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] static close on 真白, the doubt gathering. [0:06–0:13] hold on 真白 as the confession leaves her mouth, the camera not moving. [0:13–0:16] cut to 湊, static, close; ……時間？. [0:16–0:22] cut back to 真白 as she explains, the lantern light swaying across her face. [0:22–0:26] a slow rack focus onto 湊, his shadow swaying and returning. [0:26–0:30] hold on 湊's face as the smile forms; ……変な人だな; cut on the smile.

## Audio Prompt

Four lines of dialogue only: 真白 says ……私、あなたに、時間を預けてました small and deliberate; 湊 answers ……時間？ low, not mocking; 真白 explains 変な話だとは思うんです、でも私はあなたの背中をずっと見てました、私の時間は無駄じゃなかったって今なら言えます, slow and then firm; 湊 says ……変な人だな low and warm. The soft night festival continues under them — distant laughter, stall voices, the sizzle of food — and the faint creak of a lantern swaying once. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as 湊 smiles, leaving only the crowd murmur and the two voices. No horror strings, no sting, no swelling emotion, no coldness.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep11-seg03-30s-01`
- Segment ID: `S48`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_11, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 10s / 8s / 6s. Confession = BEAT 2 at 10s (33%)`
- Camera Events: `6 events as listed in §10. One rack focus (0:22–0:26)`
- Action Events: `ACT_STEEL → ACT_CONFESS → ACT_EXPLAIN → ACT_SMILE`
- Audio Events: `four lines of dialogue ／ warm festival ambience ／ sparse music thinning`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the smile`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The confession may land as a genre line.** 「時間を預けてました」 must read as a girl's awkward truth, not a sci-fi reveal. If it sounds staged, strip any tonal distance and keep it plain.
- **「変な人だな」 may read as mockery.** The smile must carry the warmth — 目じりが下がる. If it reads as a put-down, the segment inverts.
- **The model may add a ghost.** The negative prompt front-loads this; verify frame by frame.
- **The confession may lose its weight across a cut.** If the alternating close-ups break the held feeling, prefer the locked two-shot throughout.

## Changes

- _(none yet)_

## Next Generation

- If the confession and the smile both read, S49 (湊's own revelation) depends on this segment having made his warmth real.
