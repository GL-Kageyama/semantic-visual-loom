# Wan 3.0 Full Specification — 受け火 第4章「預かる」Clip 2/3「預かる＋問い」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・コダマ・少女）のみ日本語。
> この1本の個性：**第4章の第2幕＝所作・問い**。腕を動かし、コダマの火を抱える（預かる）。火が震え、初めて抱かれる。火が問う「あなたは、誰かに預けられたことがあるか」。送り火は答えない。腕が止まる。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the ritual-and-question third of Chapter 4 (預かる) into one 30-second take — the arms hold the orphan's fire, the fire asks whether he was ever held, he does not answer, and the arms stop`
- Register: `Restrained and spare. Emotion is never named — it surfaces through a fire that trembles at being held for the first time, and through arms that stop at a question. The horror and the tenderness both live in ordinary objects and withheld action`
- Rule: `One organ = one turn; one chapter = three takes (arrival / ritual-and-question / stop-and-pull); nothing is added after the pull`

---

# 2. WORLD

## World Concept

- Concept: `A boundary at a railroad crossing that leads nowhere, where a nameless man sends the dead to the other world with eight organs of his own body — each organ a verb: hands that send, fingers that bind, a throat that swallows, arms that hold, ears that measure, eyes that price, a voice that mourns, a back that discards`
- Era: `Timeless — the dead of every era mingle at the same crossing`
- Location: `A railroad crossing whose rails reach no station, no town; a barrier raised that never lowers`
- Time: `Time does not flow. There is no morning; only the hour work begins`
- Weather: `No rain falls, yet the air is damp; every sound is far away`
- Atmosphere: `Sparse, still, low-saturation deep indigo and rust red, lit only by the pale blue-white soul-fires`

## World Rules

- **根本律**：送ることは、受け取られることに先立たれる。（All sending is preceded by being received. 送り火は送るばかりで、送られたことが一度もない。）
- 八器官＝八動詞。ひとつの魂を、ひとつの器官で、ひとつの動詞で処理する。どの器官にも淀みがなく、どの動きにも迷いがない。
- 超常は**演じない、記録する**。その証拠は台帳・秤・判という世界の物と、青白い魂火だけ。
- 魂火が唯一の光源。物理世界は何も反応しない——風も、動く影も、乱れる物もない。音はみな遠い（台帳の紙の「かさり」だけが聞こえる）。
- 現世の断片（盆・夏）は匂わせるだけで描き込まない。

## Visual Language

- Art Direction: `Soft cel anime — flat color planes, clean closed thin lineart, soft-edged shadow terminators`
- Color Language: `Muted, low-saturation. The world is deep indigo and rust red. The soul-fire's pale blue-white is the only bright value — and the only light source. The fire is pale blue-white yet reads red, wavering between blue and red`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces. Things read damp though dry`
- Rendering: `Two-step cel shading with softened terminators; faint haze in the damp air; the soul-fire glows without bloom or lens flare`
- Visual Density: `Low. One focal point per beat. Generous negative space. Nothing is crowded`

---

# 3. SUBJECTS

## 送り火 (OKURIBI)

- ID: `OKURIBI`
- Name: `送り火 (nameless)`
- Type: `CHARACTER`
- Role: `Protagonist — lord of the boundary; an apparatus that sends souls to the next world through eight organs`
- Reference: `ukebi-okuribi-character-sheet/ChatGPT Image 2026年8月26日 21_38_35.png (attached — the identity lock)`

### Appearance

- A plain, unremarkable adult man, neither young nor old — nothing about him draws the eye. Namelessness itself is his appearance.
- Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat.
- Open scooping hands — hands made to scoop, that have never been scooped. Arms made to hold — that have never been held.
- No mark on his forehead (the seal appears only from S08).

### Behavior

- Personality: `Does not name; quiet. Does not name emotion. Has nothing that could be called an answer`
- Typical Motion: `Only the eight-organ ritual moves; everything else is near-still`
- Emotional Range: `Suppressed. No readable emotion on the face. Response appears as stillness — arms that stop`

### Continuity Requirements

- Must preserve: `face, hair, build, age, the dark-indigo coat, and the namelessness (nothing about him draws the eye)`

## 少女 (the girl) — 花・未開示

- ID: `GIRL`
- Name: `少女 (her name is not spoken and never appears on screen — 篠宮花 is revealed only much later)`
- Type: `CHARACTER`
- Role: `The girl who stands beside 送り火 — the first soul he ever discarded`

### Appearance

- A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet, though no rain falls on her.
- A dark-indigo neckerchief at the collar — the same damp-dark indigo as the uniform. **The neckerchief is always this deep indigo; it never changes color.**
- Long dark indigo hair; a quiet, steady gaze.
- She does **not** resemble 送り火. **No mark on her forehead.** A **solid, real figure** — not translucent, not dissolving, not a fire. She does not glow.

### Behavior

- Personality: `Says nothing yet (her first words come in Clip 3). Quiet and steady; she stands beside him and watches`
- Typical Motion: `Almost still; she stands and watches`
- Emotional Range: `Not named. Her standing beside him is the whole of it`

### Continuity Requirements

- Must preserve: `the dark-indigo sailor uniform that reads damp-dark though dry, the deep-indigo neckerchief, the long dark indigo hair, the quiet steady gaze, and the absence of any resemblance to 送り火`

## 魂火 (TAMABI) — コダマ

- ID: `KODAMA`
- Name: `コダマ`
- Type: `SUBJECT (a soul of the dead)`
- Role: `The soul being held — an orphan child with no one to take them in, who wants to be held (預けられたい)`

### Appearance

- A pale blue-white fire, **not human-shaped**, now gathered in 送り火's arms.
- The fire trembles a little — a fire that had never been held, held for the first time.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter
- `台帳` (the ledger) — dry paper; each turned page rasps かさり, the only sound at the boundary; the last row is always blank

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `all distant except the dry rustle of the ledger's page`

---

# 5. OBJECTS

- `魂火（コダマ）` — 青白い火、送り火の腕の中に収まる。抱かれたことのない火が、初めて抱かれて小さく震える。唯一の光源。`CRITICAL`
- `台帳` — 名を綴じる本。このクリップでは開かれない（画面文字なし）

---

# 6. REFERENCES

- `REF_CHARACTER` — `ukebi-okuribi-character-sheet/ChatGPT Image 2026年8月26日 21_38_35.png` · `HIGH`。Defines 送り火's face, hair, build, coat, and the namelessness. Does **not** define events or emotional tone
- `REF_HANA` — `ukebi-hana-character-sheet/ChatGPT Image 2026年8月26日 21_36_52.png` · `HIGH`。Defines the girl's uniform, hair, gaze, and the deep-indigo neckerchief. Does **not** define events or emotional tone
- `REF_STYLE` — `references/styles/soft-cel-anime.md` · `HIGH`。Defines rendering, palette discipline, lineart weight, shading steps, motion idiom
- `REF_FORMAT` — `references/formats/video-spec.md` · `HIGH`。Defines the §1–20 skeleton, uneven density, the identity lock, the six §18 slots
- `REF_SOURCE` — `soul-voice-teller/examples/ukebi/草稿/draft_04_預かる` · `CRITICAL`。Defines every event, the exact on-screen text, and what is and is not revealed
- `REF_BIBLE` — `soul-voice-teller/examples/ukebi/台帳/series-bible.md` · `CRITICAL`。Defines the staged disclosure, the voice rules, and the organ ledger

---

# 7. NARRATIVE

## Core Event

送り火は、腕を動かす。八つの器官の、四つ目。魂を預かる。転生先が決まるまで、腕の中にしまっておく。火を抱える。胸の前でじっと止まっていた火が、送り火の腕に収まる。火は小さく震えた。抱かれたことのない火が、初めて抱かれた。コダマの魂火が、言う。「あなたは、誰かに預けられたことがあるか」。送り火は、答えない。預けられたことなどなかった。抱える腕を持っていて、抱かれる腕を持ったことがない。腕が、止まる。

## Beginning

送り火は、腕を動かす。四つ目の器官。魂を預かる。火を抱える。胸の前の火が、腕に収まる。

## Turn

火が、小さく震えた。抱かれたことのない火が、初めて抱かれた。コダマの魂火が、言う——「あなたは、誰かに預けられたことがあるか」。

## Peak

送り火は、答えない。預けられたことなどなかった。抱える腕を持っていて、抱かれる腕を持ったことがない。伸ばされた両手を受け取ることはできても、自分の両手を誰かに伸ばしたことはなかった。

## Pull（引き — 切れ目）

腕が、止まる。Cut。（少女の介入と定型句は Clip 3。）

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The question and the arms stopping hold the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「預かる」 — ESTABLISH.** The arms move; the fire is gathered into them. The fire trembles — held for the first time. _Density: SPARSE — the holding._
- **BEAT 2 `[0:07–0:19]` — 「あなたは、誰かに預けられたことがあるか」 — CORE, longest share.** コダマ's fire asks. 送り火 does not answer. He has always held, never been held; he could receive two outstretched hands, but never stretched out his own. _Density: HELD — the question, and the silence that answers it._
- **BEAT 3 `[0:19–0:30]` — 「腕が止まる」.** The arms stop. Hold. Cut. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the question (≈0:09) ／ the arms stopping (≈0:22)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the holding)`
- Dense regions: `0:07–0:19 (the question) ／ 0:19–0:30 (the arms stopping)`
- Long continuous action: `0:07–0:19 the silence that answers the question`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `OKURIBI (送り火)`
- Action: `Moves his arms — the fourth organ — and gathers the fire into them; the fire trembles, held for the first time`
- Intention: `To hold the soul in trust until a destination is decided (預かる)`
- Intensity: `Low, exact`
- Speed: `A slow, practiced gathering`

### Action Relationship

- Before: `—`
- After: `ACT_ASK`

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `KODAMA (the orphan soul-fire)`
- Action: `Asks — あなたは、誰かに預けられたことがあるか`
- Intention: `To ask the one thing it knows how to ask — whether he, too, was ever held`
- Intensity: `Low, direct`
- Speed: `Still; the question is spoken, not moved`

### Action Relationship

- Before: `ACT_HOLD`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `OKURIBI (送り火)`
- Action: `Does not answer; the arms stop. He has always held, never been held`
- Intention: `None — the stop is not chosen; the answer he does not have stops the arms`
- Intensity: `Low, a held stillness`
- Speed: `A complete halt; the arms are still`

### Action Relationship

- Before: `ACT_ASK`
- After: `— (cut on the arms stopping)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not inside his first person`
- Lens Character: `Arm-level and intimate; the arms and the fire in them are the subject, the face secondary`
- Depth of Field: `Shallow — the fire in the arms is sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with the arms; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:07]`** — Close on the arms moving, gathering the fire; a tremble.
- **`[0:07–0:19]`** — Hold on the fire in the arms; the question, and 送り火's silence.
- **`[0:19–0:30]`** — The arms stop; hold on the still arms. Cut.

---

# 11. MOTION

## Subject Motion

- The arms carry the motion — a gathering, then a complete halt.
- The fire trembles once and holds.

## Object Motion

- Nothing moves.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.

## Physical Characteristics

- Weight: `The fire has no weight; the holding has the weight of an answer he does not have`
- Inertia: `High for the body; the stop is the only abrupt thing, and it is stillness, not a snap`
- Acceleration: `Gentle everywhere; the stop is absolute`
- Fluidity: `Limited-animation — holds punctuated by small precise gestures`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Stillness (the holding, as always)
- ↓ The question (were you ever held?)
- ↓ The silence (he was not)
- ↓ The stop (the arms stop)

## Emotional Events

- Event: `The fire asks` — Emotion: `A question no one had ever asked him — were you ever held?` — Intensity: `LOW, entirely internal` — Timing: `≈0:09`
- Event: `The arms stop` — Emotion: `He has always held, never been held — the stop is the answer he does not have` — Intensity: `LOW, a held stillness` — Timing: `≈0:22`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The orphan soul-fire in the arms — pale blue-white, the only light and the only bright value, close against his chest`
- Fill Light: `Almost none. Deep indigo shadow fills everything the fire does not reach`
- Rim Light: `A very faint cool edge on the arms and the girl's hair from the fire's spill`
- Ambient Light: `Near-black indigo and rust red`
- Color Temperature: `Cold blue-white against deep indigo and rust red`

## Lighting Events

- **`[0:00]`** — The fire's light plays on the arms as it is gathered.
- **`[0:07–0:19]`** — The fire in the arms, its light on his face; the girl standing in the dim.
- **`[0:19–0:30]`** — The arms in the fire's faint spill, still. Hold. Cut.

---

# 14. AUDIO

## Dialogue

> **コダマの魂火** (the orphan soul-fire): `あなたは、誰かに預けられたことがあるか。` — spoken once, direct and quiet. 送り火 does not answer. The girl does not speak yet. The 定型句 does not appear (it comes at Clip 3).

## Sound Effects

- Almost none — the damp near-silence. A dry rustle, distant.

## Environment

- The damp near-silence; every sound far away; no footsteps, no breath, no rail, no wind.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender without sentiment. Never sinister`
- Emotional Function: `Hold the stillness under the question; it may thin toward the close`

---

# 15. CONTINUITY

> 30本は30回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

## Identity（must remain consistent）

- 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. No mark on his forehead. (Follows `ukebi-okuribi-character-sheet/…21_38_35.png`.)
- 少女 — a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet, though no rain falls on her; a dark-indigo neckerchief at the collar; long dark indigo hair; a quiet, steady gaze. She does not resemble 送り火. No mark on her forehead. (Follows `ukebi-hana-character-sheet/…21_36_52.png`.)
- The stage — a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls.

## Visual Continuity

- **The light law** — the soul-fire's pale blue-white is the only light and the only bright value; everything else is deep indigo and rust red.
- **The palette law** — muted, low-saturation everywhere; the pale blue-white soul-fire is the only bright value.
- **The scarf law** — the girl's neckerchief is always the deep damp-dark indigo; it never changes color.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the arms.

## Sound Continuity

- **The sound law** — no sound except the dry rustle of the ledger's page (which does not turn in this clip) and, once, the fire's question.

---

# 16. CONSTRAINTS

## MUST

- Show the arms holding the fire, and the fire trembling — held for the first time.
- Render コダマ's question as spoken dialogue, not on-screen text: あなたは、誰かに預けられたことがあるか。
- Show the arms stopping — a complete halt, stillness.
- Show the girl standing beside 送り火 — a solid, real figure, silent.
- Fix her neckerchief as the deep damp-dark indigo; it never changes color.
- Keep 送り火's face, hair, build, coat and namelessness exactly as the attached character sheet.

## MUST NOT（この1本の禁止・開示台帳 04 レンジより）

- **No name** — the girl's name 篠宮花 is not spoken and never appears on screen. She is only 少女.
- **No mark on her forehead.** **No resemblance to 送り火.**
- **No translucent/dissolving girl** — she is a real, solid body.
- **No glow on her** — she does not emit light.
- No red scarf, no white scarf, no bright neckerchief, no changing scarf color, no drifting neckwear color.
- No readable text — no Japanese kanji or kana, no real-world alphabet.
- No on-screen text (the ledger is not opened in this clip).

## PREFER

- Silence over score.
- The arms and the fire as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the exact hue of the fire's waver.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 少女 is unnamed, unmarked, unlike 送り火, and a solid figure. This outranks everything, including beauty.
2. **Identity stability** — both faces must not drift across the take; they follow the attached character sheets.
3. **The question** — あなたは、誰かに預けられたことがあるか。 is spoken, not written.
4. **The scarf fix** — the neckerchief is deep damp-dark indigo, never changing.
5. **The uneven density** — the question and the stop must hold the largest share.
6. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
7. **The style** — flat cel planes, soft light, limited animation.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands; and a high-school girl standing beside him in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though no rain falls, a dark-indigo neckerchief at the collar, long dark indigo hair, a quiet steady gaze — she does not resemble the man. Beats, deliberately uneven: [0:00–0:07] the arms move — the fourth organ — and gather the orphan's fire into them, the fire trembling, held for the first time; [0:07–0:19] the fire asks — あなたは、誰かに預けられたことがあるか — and 送り火 does not answer, for he has always held, never been held; [0:19–0:30] the arms stop. Hold. Cut. The question and the stop hold the largest share. (The pull — この魂は、まだ誰にも名付けられていない。 — does not appear in this clip.)

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands, arms that hold. A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though no rain falls on her; a dark-indigo neckerchief at the collar, the same damp-dark indigo as the uniform; long dark indigo hair; a quiet steady gaze. She is a real, solid figure — not translucent, not dissolving, not a fire. She does not resemble the man. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The soul-fire is pale blue-white, not human-shaped, the only light and the only bright value, gathered in his arms, trembling faintly. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the arms and the fire; the bodies hold still. The arms move once, gathering the fire; the fire trembles once; then the arms stop completely — a held halt, not a snap. The girl stands still. No wind, no dust, no particles, the faintest haze in the damp air; the barrier stays raised and still. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Arm-level and intimate; the arms and the fire are the subject, the faces secondary. Shallow depth of field; the fire in the arms is sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:07] close on the arms gathering the fire, the tremble. [0:07–0:19] hold on the fire in the arms, the question and his silence. [0:19–0:30] the arms stop; hold, then cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. The fire speaks once, quiet and direct: あなたは、誰かに預けられたことがあるか。 送り火 does not answer; the girl does not speak yet. No 定型句 here. All sound far away, no footsteps, no breath, no rail, no wind. Music extremely sparse — a few sustained tones at most — thinning toward the close. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no name text, no nameplate, no subtitle naming the girl, no red scarf, no white scarf, no bright neckerchief, no changing scarf color, no drifting neckwear color, no translucent girl, no dissolving figure, no ghostly girl, no glowing girl, no bloom on her, no mark on her forehead, no reflection of a girl, no feminine mirror of the man's face, no copy of the man, no double, no solid human body inside the fire, no standing child inside the fire, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch04-seg02-30s-01`
- Segment ID: `04-2`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_HANA (hana character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_04_預かる, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 7s / 12s / 11s. The question = BEAT 2 at 12s (40%)`
- Camera Events: `3 events as listed in §10. All third-person-limited holds`
- Action Events: `ACT_HOLD → ACT_ASK → ACT_STOP`
- Audio Events: `fire's question (あなたは、誰かに預けられたことがあるか) ／ near-silence`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the arms stopping`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The question may render as on-screen text.** It must be spoken only; verify no subtitle or readable text appears.
- **The arms may read as a flinch.** The stop must be a complete, unhurried halt.
- **The girl may be translucent or ghost-like.** She must be a real, solid body.
- **The neckerchief may drift in color.** It must stay deep damp-dark indigo.

## Changes

- _(none yet)_

## Next Generation

- If the stop reads, 04-3 continues with the girl — she lowers the fire from his arms, then lowers 送り火 onto her lap: 代わりに、あんたを預からせて. The 定型句 ends the chapter.
