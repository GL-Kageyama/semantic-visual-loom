# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第11話 S49「湊も預けてる」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「湊も預けてる」——湊のスマホだけが、ほんの少し明るい（指の背骨の第49本）。真白の手は空のまま、物語の核心であるスマホが湊の手の中にあり、ほんの少し明るくなる。二人分の「預けた時間」が、ここで初めて揃う。最大の秒は「私も、誰かに時間を預けてるから」という湊の告白と、その余波に配る。ニジは不在（第11話に幽霊はいない）。登場人物は真白と湊のみ。画面文字なし（湊のスマホの宛先リストは真白には見えず、文字は映さない）。**

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
- Appearance: `Dim and ordinary in 湊's hand, plain case, Japanese UI — its screen just slightly brighter, an ordinary wake, its content unreadable (the list 真白 cannot see). 真白 carries no phone this segment — her hands are empty and still`
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

湊 reveals, in his quiet way, that he too deposits time: 「でも、なんか分かる気がする。私も、誰かに時間を預けてるから」. 真白's heart nearly stops. He is sending his to someone who will soon be gone — and he speaks the series' own title back at her: 「午前二時のあれ」.

## Beginning

「……はい」 — 真白 answers 湊's smile from the beat before. Between them, the warmth has not yet settled into words.

## Turn

「でも、――なんか分かる気がする。私も、――誰かに時間を預けてるから」. 真白は、その言葉に、心臓が止まるか、と思った。湊も、預けてる。

## Peak

「……湊先輩も、ですか」 — 「うん。会えなくなる人に。この文化祭が終わったら、県外に行っちゃう人に」. 湊 looks at his phone; its screen is, just slightly, brighter. 湊のスマホにも、真白には見えない宛先リストがあるんだろうな、と、真白は思う。同じ数字が並んでるんだろうな、と。

## Pull（引き — 切れ目）

「……返せますかね、そういうの」 — 「さあ。でも、返さないと、ずっと残るんだろ。午前二時のあれが」。 Cut on the series title, spoken aloud by a person for the first time.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** 湊's revelation holds 10s (33%); the phone's faint brightness is held 6s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「……はい」 — ESTABLISH.** 真白 answers the smile from before. The warmth between them, not yet words. _Density: SPARSE — a held, warm beat._
- **BEAT 2 `[0:06–0:16]` — 「私も預けてる」 — TURN, longest share.** 「でも、――なんか分かる気がする。私も、――誰かに時間を預けてるから」. 真白は、心臓が止まるか、と思った。湊も、預けてる。_Density: DENSE at the head, then held on her face._
- **BEAT 3 `[0:16–0:24]` — 「会えなくなる人」 — PEAK.** 「……湊先輩も、ですか」. 「うん。会えなくなる人に。この文化祭が終わったら、県外に行っちゃう人に」. 湊 looks at his phone; its screen, just slightly, brighter. 真白 thinks of the list she cannot see — the same numbers, in a row. _Density: TRANSITION — the mirror of her own secret._
- **BEAT 4 `[0:24–0:30]` — 「午前二時のあれが」 — PULL.** 「……返せますかね、そういうの」. 「さあ。でも、返さないと、ずっと残るんだろ。午前二時のあれが」. Cut on the title, spoken aloud. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `湊's 「私も、誰かに時間を預けてるから」 (≈0:08) ／ the phone brightening slightly (≈0:19) ／ 「午前二時のあれが」 (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the held warmth), 0:24–0:30 (the title)`
- Dense regions: `0:06–0:16 (the revelation)`
- Long continuous action: `0:16–0:24 湊 looking at his phone`
- Rapid transitions: `none — a slow, warm exchange`

---

# 9. ACTION

## Action — ACT_ANSWER

- ID: `ACT_ANSWER`
- Subject: `MASHIRO`
- Action: `Answers 「……はい」, the smile from before still between them`
- Intention: `To stay in the warmth a moment longer`
- Intensity: `Low`
- Speed: `Still`

### Action Relationship

- Before: `—` (continues from S48's smile)
- After: `ACT_REVEAL`

## Action — ACT_REVEAL

- ID: `ACT_REVEAL`
- Subject: `MINATO`
- Action: `Says 「でも、なんか分かる気がする。私も、誰かに時間を預けてるから」`
- Intention: `Not to confess — to recognize. He means it lightly, and it lands heavy`
- Intensity: `Medium`
- Speed: `Slow, low, ordinary`

### Action Relationship

- Before: `ACT_ANSWER`
- After: `ACT_STOP_HEART`

## Action — ACT_STOP_HEART

- ID: `ACT_STOP_HEART`
- Subject: `MASHIRO`
- Action: `Her heart nearly stops — 湊も預けてる — and she asks 「……湊先輩も、ですか」`
- Intention: `To be sure she heard him right`
- Intensity: `HIGH, entirely internal`
- Speed: `Still; the voice is small and careful`

### Action Relationship

- Before: `ACT_REVEAL`
- After: `ACT_LOOK_AT_PHONE`

## Action — ACT_LOOK_AT_PHONE

- ID: `ACT_LOOK_AT_PHONE`
- Subject: `MINATO`
- Action: `Answers 「うん。会えなくなる人に。…県外に行っちゃう人に」, then looks at his phone, its screen just slightly brighter`
- Intention: `To show her, without saying it, that the same list is in his hand`
- Intensity: `Medium`
- Speed: `Slow; the eyes lower to the screen`

### Action Relationship

- Before: `ACT_STOP_HEART`
- After: `ACT_TITLE`

## Action — ACT_TITLE

- ID: `ACT_TITLE`
- Subject: `MASHIRO → MINATO`
- Action: `真白 asks 「返せますかね、そういうの」; 湊 answers 「さあ。でも、返さないと、ずっと残るんだろ。午前二時のあれが」`
- Intention: `To name the thing they now both carry`
- Intensity: `Medium`
- Speed: `Slow, low, quiet — the title spoken like an ordinary thing`

### Action Relationship

- Before: `ACT_LOOK_AT_PHONE`
- After: `— (cut on the title)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, face-to-face. Two-shot, then alternating close-ups, then the phone`
- Lens Character: `Long-ish, shallow. The festival falls away soft behind`
- Depth of Field: `Shallow — 湊 sharp, then 真白, then the faintly bright screen`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Static two-shot: the two of them in the lantern light, the smile still settling between them.
- **`[0:06–0:13]`** — Cut to 湊, static, close. The revelation leaves his mouth low and ordinary.
- **`[0:13–0:16]`** — Cut to 真白, static, close. 心臓が止まるか、と思う. Her face does not resolve.
- **`[0:16–0:22]`** — Two-shot again as she asks 「……湊先輩も、ですか」 and he answers 「会えなくなる人に…」.
- **`[0:22–0:26]`** — Insert: 湊's hand, the phone, its screen just slightly brighter — the list 真白 cannot see. Nothing legible.
- **`[0:26–0:30]`** — Cut back to 湊, close. 「返さないと、ずっと残るんだろ。午前二時のあれが」 Cut on the title.

---

# 11. MOTION

## Subject Motion

- 真白's body is nearly still; her hands stay empty at her sides; only her mouth moves, small and careful
- 湊 is still; his single motion is lowering his eyes to the phone in his hand
- The revelation does not move the air; the two of them barely shift

## Object Motion

- 湊's phone screen brightens, just slightly — an ordinary wake, not a glow. It does not move on its own
- No text is legible on the screen; it is only a faint brightness
- Nothing glitches, flickers, distorts, or behaves supernaturally

## Environmental Motion

- The festival is alive only in soft, out-of-focus movement — distant figures, drifting smoke
- No wind, no moving shadows, no particles

## Physical Characteristics

- Weight: `Ordinary. The two of them stand with ordinary weight; the phone has heft in 湊's hand`
- Inertia: `High for both bodies; near-zero movement throughout`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Warmth (the smile, still between them)
- ↓ Shock, quiet (湊 also deposits — her heart nearly stopping)
- ↓ Recognition (the same list, the same numbers, in his hand)
- ↓ Shared weight (the title spoken aloud, and received)

## Emotional Events

- Event: `「私も、誰かに時間を預けてるから」` — Emotion: `Quiet shock — the mirror of her own secret` — Intensity: `HIGH, entirely internal` — Timing: `≈0:08`
- Event: `湊's phone, just slightly brighter` — Emotion: `Recognition — the same list is in his hand` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:19`
- Event: `「午前二時のあれが」` — Emotion: `Shared weight — the thing they now both carry, named` — Intensity: `MEDIUM` — Timing: `≈0:27`

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
- **`[0:06–0:16]`** — The light holds steady on 湊 as he speaks, then on 真白.
- **`[0:22–0:26]`** — A faint cool blue-white rises on 湊's face as his phone brightens — the screen's light, small against the warm.
- **`[0:26–0:30]`** — The warm returns as the phone lowers. Cut on the title.

---

# 14. AUDIO

## Dialogue

- 真白: 「……はい」
- 湊: 「でも、――なんか分かる気がする。私も、――誰かに時間を預けてるから」
- 真白: 「……湊先輩も、ですか」
- 湊: 「うん。――会えなくなる人に。――この文化祭が終わったら、――県外に行っちゃう人に」
- 真白: 「……返せますかね、そういうの」
- 湊: 「さあ。――でも、返さないと、ずっと残るんだろ。――午前二時のあれが」

> No other speech. No narration, no voice-over.

## Sound Effects

- The soft night festival continuing — distant laughter, stall voices, the sizzle of food
- The faint, ordinary sound of a phone waking — soft, not a chime, not a buzz

## Environment

- Open night air, warm and full, unbothered

## Music

- Style: `Sparse — a few sustained tones, or nothing`
- Tempo: `Slow`
- Mood: `Warm, held, quietly moved. Never sinister, never sentimental`
- Emotional Function: `Hold the space under the revelation. It thins as 湊 looks at his phone, leaving only the crowd murmur and the two voices`

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

- Render the spoken lines exactly, including 「午前二時のあれが」 — the series title spoken by a person
- Show 湊's phone screen brighten just slightly — an ordinary wake, not a glow, and **no legible text on it**
- Keep 真白's hands empty and still throughout
- Keep 湊's revelation quiet and ordinary — recognition, not drama
- End by cutting on 「午前二時のあれが」, nothing after it

## MUST NOT（この1本の禁止・開示台帳 46–51 レンジより）

- **ニジは登場しない。** No ghost, no figure, no silhouette, no reflection, no second person, no eyes but the two living people's own. This episode has no ニジ at all
- **No rainbow, no iridescence, no colored afterimage**
- **No on-screen text.** 湊's phone is faintly bright, but the list 真白 cannot see must stay unreadable — do not invent characters on the screen
- Do not make 湊 sinister, menacing, or knowing
- Do not give this night horror grammar
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The faint brightness of 湊's phone as the only "screen" moment — a mirror of the series' whole visual language
- Silence over score at the title
- Negative space over detail

## ALLOW

- Slight variation in lantern pattern and crowd shapes
- The insert of the phone may be omitted (a fully locked two-shot is equally correct)
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

A 30-second continuous cinematic take (16:9), soft cel anime, of a night culture festival in a school back yard. Beats, deliberately uneven: [0:00–0:06] 真白 answers ……はい, the smile from before still settling between them; [0:06–0:16] THE REVELATION — 湊 says でも、なんか分かる気がする、私も、誰かに時間を預けてるから, and 真白's heart nearly stops, 湊も預けてる; [0:16–0:24] she asks ……湊先輩も、ですか and he answers うん、会えなくなる人に、この文化祭が終わったら、県外に行っちゃう人に, and 湊 looks at his phone, its screen just slightly brighter, the list 真白 cannot see; [0:24–0:30] she asks ……返せますかね、そういうの and he answers さあ、でも、返さないと、ずっと残るんだろ、午前二時のあれが, and the shot cuts on the title. The revelation holds the largest share of the duration. Ends on the title, spoken aloud, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. She wears her standard Japanese school uniform; her hands are empty. Scene: a school festival back yard at night — warm soft paper lanterns, drifting smoke, indigo night air. Facing her, 湊 (Minato) — a third-year boy, festival committee, composed and quiet, short neat dark hair, in the boys' school uniform, a little taller, with a calm face; he holds a phone whose screen is just slightly bright, its content unreadable. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Bodies hold almost completely still. 真白's only movement is her mouth, small and careful; her hands stay empty and still at her sides. 湊 is still; his single motion is lowering his eyes to the phone in his hand. The phone's screen brightens just slightly — an ordinary wake, not a glow; it never moves by itself and never glitches, flickers or distorts. No text is legible on the screen. The festival crowd is alive only in soft, out-of-focus movement. No wind, no moving shadows, no particles. Gentle acceleration everywhere. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, face-to-face. Longish lens, shallow depth of field; 湊 sharp, then 真白, then the faintly bright screen. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] static two-shot, the two of them in the lantern light. [0:06–0:13] cut to 湊, static, close, as the revelation leaves his mouth low and ordinary. [0:13–0:16] cut to 真白, static, close; 心臓が止まるか、と思う. [0:16–0:22] two-shot again; ……湊先輩も、ですか; 会えなくなる人に…. [0:22–0:26] insert on 湊's hand and phone, its screen just slightly brighter, nothing legible. [0:26–0:30] cut back to 湊, close; 返さないと、ずっと残るんだろ、午前二時のあれが; cut on the title.

## Audio Prompt

Six lines of dialogue only: 真白 says ……はい; 湊 says でも、なんか分かる気がする、私も、誰かに時間を預けてるから, low and ordinary; 真白 asks ……湊先輩も、ですか, small and careful; 湊 answers うん、会えなくなる人に、この文化祭が終わったら、県外に行っちゃう人に; 真白 asks ……返せますかね、そういうの; 湊 answers さあ、でも、返さないと、ずっと残るんだろ、午前二時のあれが. The soft night festival continues under them — distant laughter, stall voices, the sizzle of food — and the faint ordinary sound of a phone waking. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as 湊 looks at his phone, leaving only the crowd murmur and the two voices. No horror strings, no sting, no swelling emotion, no coldness.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep11-seg04-30s-01`
- Segment ID: `S49`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_11, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 10s / 8s / 6s. Revelation = BEAT 2 at 10s (33%)`
- Camera Events: `6 events as listed in §10. One insert (0:22–0:26)`
- Action Events: `ACT_ANSWER → ACT_REVEAL → ACT_STOP_HEART → ACT_LOOK_AT_PHONE → ACT_TITLE`
- Audio Events: `six lines of dialogue ／ warm festival ambience ／ a phone waking faintly ／ sparse music thinning`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the title`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The phone's brightness may read as supernatural.** It is an ordinary wake — small, blue-white against the warm. If it glows or pulses, tone it down until it is almost nothing.
- **The screen may show text.** 湊's list is invisible to 真白 and must stay unreadable. If characters appear, blur or remove them — the screen is only a faint brightness.
- **「午前二時のあれが」 may land as a reveal, not a shared recognition.** It must be spoken low and ordinary, like something both of them already carry. If it lands as a dramatic beat, the series' restraint is broken.
- **The model may add a ghost.** The negative prompt front-loads this; verify frame by frame.

## Changes

- _(none yet)_

## Next Generation

- If the title lands ordinary and the phone stays faint, S50 (湊 calling her name) depends on this segment having made their shared secret real.
