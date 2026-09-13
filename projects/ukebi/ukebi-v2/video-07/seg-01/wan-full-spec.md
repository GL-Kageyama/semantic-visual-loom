# Wan 3.0 Full Specification — 受け火 第7章「悼む」Clip 1/3「早瀬甚吾の来臨（独り）」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・少女・早瀬甚吾）のみ日本語。
> この1本の個性：**第7章の第1幕＝客の来臨。独り死んで、誰にも悼まれなかった兵・早瀬甚吾の魂火が届く。誰にも読まれなかった手紙と、誰にも聞かれなかった最期の声が、火のなかにうっすら見える。** 送り火の額には該当なしの印が既に残る（06-3 より）。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the guest-arrival first third of Chapter 7 (悼む) into one 30-second take — the soul-fire of 早瀬甚吾, a soldier who died alone and was mourned by no one, arrives with the weight of an unseen corpse; inside the fire, letters no one read and a last voice no one heard appear as a half-transparent vision; 送り火 sees it`
- Register: `Restrained and spare. The sorrow is a voice that reached no one. Emotion is never named — it surfaces through an unheard last word and a letter no hand ever received`

---

# 2. WORLD

## World Concept

- Concept: `A boundary at a railroad crossing that leads nowhere, where a nameless man sends the dead to the other world with eight organs of his own body — each organ a verb: hands that send, fingers that bind, a throat that swallows, arms that hold, ears that measure, eyes that price, a voice that mourns, a back that discards`
- Era: `Timeless — the dead of every era mingle at the same crossing`
- Location: `A railroad crossing whose rails reach no station, no town; a barrier raised that never lowers`
- Time: `Time does not flow. There is no morning; only the hour work begins`
- Weather: `No rain falls, yet the air is damp; every sound is far away`
- Atmosphere: `Sparse, still, low-saturation deep indigo and rust red; the pale-blue soul-fire is the one true light`

## World Rules

- **根本律**：送ることは、受け取られることに先立たれる。（All sending is preceded by being received. 送り火は送るばかりで、送られたことが一度もない。）
- 八器官＝八動詞。ひとつの魂を、ひとつの器官で、ひとつの動詞で処理する。どの器官にも淀みがなく、どの動きにも迷いがない。
- 超常は**演じない、記録する**。その証拠は台帳・秤・判という世界の物と、青白い魂火だけ。
- 魂火が唯一の光源。物理世界は何も反応しない——風も、動く影も、乱れる物もない。音はみな遠い。
- 火は**人のかたちをしない**。火の中に浮かぶ幻は半透明の記憶であって、魂が人の姿を取ることではない。
- 現世の断片（盆・夏）は匂わせるだけで描き込まない。

## Visual Language

- Art Direction: `Soft cel anime — flat color planes, clean closed thin lineart, soft-edged shadow terminators`
- Color Language: `Muted, low-saturation. The world is deep indigo and rust red. The soul-fire is a pale blue-white; its inner vision reads earth-toned and dissolving`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces. Things read damp though dry`
- Rendering: `Two-step cel shading with softened terminators; faint haze in the damp air; no bloom, no lens flare`
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
- Open scooping hands — hands made to scoop, that have never been scooped.
- **A mark on his forehead — 該当なし, a square mark in the boundary script, thin and angular, dark ink** (pressed in 06-3).

### Behavior

- Personality: `Does not name; quiet. Does not name emotion. Has nothing that could be called an answer`
- Typical Motion: `Almost still; his voice will move, but not yet`
- Emotional Range: `Suppressed. No readable emotion on the face`

### Continuity Requirements

- Must preserve: `face, hair, build, age, the dark-indigo coat, the namelessness, and the forehead mark 該当なし`

## 少女 (the girl) — 花・未開示

- ID: `GIRL`
- Name: `少女 (her name is not spoken and never appears on screen — 篠宮花 is revealed only in Chapter 8)`
- Type: `CHARACTER`
- Role: `The girl, present since 第3章 — a soul with no value, who has never left his side`

### Appearance

- A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet, though no rain falls on her.
- A dark-indigo neckerchief at the collar — the same damp-dark indigo as the uniform. **The neckerchief is always this deep indigo; it never changes color.**
- Long dark indigo hair; a quiet, steady gaze.
- She does **not** resemble 送り火. **No mark on her forehead.** A **solid, real figure** — not translucent, not dissolving, not a fire. She does not glow.

### Behavior

- Personality: `Quiet and steady; she stands aside and watches the arriving fire`
- Typical Motion: `Almost still; a steady gaze`
- Emotional Range: `Not named`

### Continuity Requirements

- Must preserve: `the dark-indigo sailor uniform that reads damp-dark though dry, the deep-indigo neckerchief, the long dark indigo hair, the quiet steady gaze, and the absence of any resemblance to 送り火`

## 早瀬甚吾 (HAYASE JINGO) — ゲストの魂火

- ID: `GUEST_07`
- Name: `早瀬甚吾 (his name is carried by the narration's voice, never written on screen)`
- Type: `SOUL-FIRE / VISION`
- Role: `Guest — a soldier who died alone and was mourned by no one; the fire holds letters no one read and a last voice no one heard`

### Appearance

- The soul-fire is a **pale blue-white flame**, the only true light — it does **not** take a human form.
- Within and above the fire floats a **half-transparent vision**, dissolving into the earth color: a soldier with the weight of an unseen corpse. His outline wavers; he is a memory the fire reflects, not a body.
- He does **not** resemble 少女 — not a schoolgirl, no sailor uniform, no indigo hair.

### Behavior

- Personality: `Solitary. He does not speak; the unheard last voice is the whole of him`
- Typical Motion: `Almost none; the vision drifts faintly within the fire`
- Emotional Range: `A solitary death, held in an unheard word`

### Continuity Requirements

- Must preserve: `the solitary weight; the half-transparency; the earth-tone dissolving; the absolute non-resemblance to 少女`

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter
- `魂火` (the soul-fire) — the pale blue-white fire of 早瀬甚吾, floating before 送り火, the only true light

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `all distant; the fire makes no sound`

---

# 5. OBJECTS

- `魂火` — the pale blue-white fire holding 早瀬甚吾's vision; the light of the whole take. `CRITICAL`

---

# 6. REFERENCES

- `REF_CHARACTER` — `ukebi-okuribi-character-sheet/ChatGPT Image 2026年8月26日 21_38_35.png` · `HIGH`。Defines 送り火's face, hair, build, coat, and the namelessness. Does **not** define events or emotional tone
- `REF_HANA` — `ukebi-hana-character-sheet/ChatGPT Image 2026年8月26日 21_36_52.png` · `HIGH`。Defines the girl's uniform, hair, gaze, and the deep-indigo neckerchief. Does **not** define events or emotional tone
- `REF_STYLE` — `references/styles/soft-cel-anime.md` · `HIGH`。Defines rendering, palette discipline, lineart weight, shading steps, motion idiom
- `REF_FORMAT` — `references/formats/video-spec.md` · `HIGH`。Defines the §1–20 skeleton, uneven density, the identity lock, the six §18 slots
- `REF_SOURCE` — `soul-voice-teller/examples/ukebi/草稿/draft_07_悼む` · `CRITICAL`。Defines every event, the exact on-screen text, and what is and is not revealed
- `REF_BIBLE` — `soul-voice-teller/examples/ukebi/台帳/series-bible.md` · `CRITICAL`。Defines the staged disclosure, the voice rules, and the organ ledger

---

# 7. NARRATIVE

## Core Event

独り死んで、誰にも悼まれなかった兵の魂火が、届く。早瀬甚吾、という。誰にも見送られなかった死体の重さをしている。青白い火が、声の器官の前に静かに置かれる。火のなかには、誰にも読まれなかった手紙と、誰にも聞かれなかった最期の声と、独りで死んだ夜が入っている。送り火には、それが見える。

## Beginning

早瀬甚吾の魂火が、届く。青白い火。火の内側に、独りの重さをした兵の幻影が、地の色に溶けて揺らぐ。少女が、傍らでそれを見ている。

## Turn

送り火は、その独りの重さを見る。誰にも読まれなかった手紙と、誰にも聞かれなかった最期の声が、火のなかにうっすら浮かぶ。

## Peak

それでも彼は、死ぬ前に声を出した。手紙を書いた。届かないとわかっていても。独りで死ぬということが、どういうことなのかを、誰かに知らせたかった。けれど、誰もいなかった。送り火には、その、届かなかった声が見える。

## Pull（引き — 切れ目）

Cut on the unheard last voice, held within the fire. （定型句は Clip 3。）

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The unheard last voice holds the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:09]` — 「火が届く」 — ESTABLISH.** The pale-blue fire arrives; within it, a soldier's half-transparent vision, heavy with a solitary death, dissolving into earth color. _Density: SPARSE — the arrival._
- **BEAT 2 `[0:09–0:21]` — 「届かなかった声」 — CORE, longest share.** The letters no one read, the last voice no one heard, faintly surfacing in the fire. _Density: HELD — the unheard word._
- **BEAT 3 `[0:21–0:30]` — 「誰もいなかった」.** He spoke, he wrote, though it would not reach anyone — and no one was there. 送り火 sees it. Cut. _Density: HELD — the sight, then the cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the fire arriving (≈0:02) ／ the unheard last voice surfacing (≈0:11) ／ 送り火 seeing (≈0:23)`

## Temporal Density

- Sparse regions: `0:00–0:09 (the arrival)`
- Dense regions: `0:09–0:21 (the unheard voice) ／ 0:21–0:30 (the seeing)`
- Long continuous action: `0:09–0:21 the vision held within the fire`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_ARRIVE

- ID: `ACT_ARRIVE`
- Subject: `GUEST_07 (早瀬甚吾's fire)`
- Action: `The pale-blue soul-fire arrives, floating before 送り火; within it, a soldier's half-transparent vision, heavy with a solitary death`
- Intention: `To be mourned — a soul that came to be spoken of one last time`
- Intensity: `Low, a slow drifting in`
- Speed: `Slow; the fire settles before him`

### Action Relationship

- Before: `—`
- After: `ACT_SEE`

## Action — ACT_SEE

- ID: `ACT_SEE`
- Subject: `OKURIBI (送り火)`
- Action: `He sees the letters no one read and the last voice no one heard`
- Intention: `None — the seeing is involuntary; the eye attends and receives`
- Intensity: `Low, entirely internal`
- Speed: `Still; the gaze holds`

### Action Relationship

- Before: `ACT_ARRIVE`
- After: `— (cut on the unheard voice)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not inside his first person`
- Lens Character: `Fire-level and intimate; the unheard last voice within the fire is the subject, the faces secondary`
- Depth of Field: `Shallow — the vision in the fire is sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with the fire; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:09]`** — The pale-blue fire arriving; within it, the half-transparent vision.
- **`[0:09–0:21]`** — The letters no one read, the last voice no one heard. Hold on the vision.
- **`[0:21–0:30]`** — 送り火 seeing; then back to the vision. Cut.

---

# 11. MOTION

## Subject Motion

- 送り火 is almost still; his eyes attend. 少女 stands still, watching. The guest's vision drifts faintly within the fire.

## Object Motion

- The fire hovers, steady, unreacting.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.

## Physical Characteristics

- Weight: `The vision carries the weight of an unseen corpse; it is a memory, not a body`
- Inertia: `Near-total stillness; only the fire's faint drift`
- Acceleration: `None`
- Fluidity: `Limited-animation — a held gaze, the vision drifting slightly`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Arrival (a pale fire, a solitary weight)
- ↓ The unheard voice (letters no one read, a last word no one heard)
- ↓ The night he died alone (no one was there)
- ↓ The unspoken (a man who reached no one)

## Emotional Events

- Event: `The unheard last voice surfaces within the fire` — Emotion: `A solitary death, held in an unheard word` — Intensity: `LOW, a held sorrow` — Timing: `≈0:11`
- Event: `送り火 sees it` — Emotion: `He spoke and wrote though it would reach no one, and no one was there` — Intensity: `LOW, entirely internal` — Timing: `≈0:23`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The pale blue-white soul-fire — the one true light in the boundary`
- Fill Light: `Almost none. Soft indigo fills the space`
- Rim Light: `A faint cool edge on 送り火's coat and the girl's hair from the fire`
- Ambient Light: `Deep indigo; the rust-red of the rails reads faintly red in the damp dark`
- Color Temperature: `Cold, near-monochrome indigo, warmed only by the pale-blue fire`

## Lighting Events

- **`[0:00]`** — The fire arriving, its pale-blue light touching the crossing.
- **`[0:09–0:21]`** — The vision surfacing in the fire's light.
- **`[0:21–0:30]`** — The unheard voice, lit by the fire. Cut.

---

# 14. AUDIO

## Dialogue

> **境の地の声**（語り）: `早瀬甚吾、という。` — the narration carries his name, since the boundary's script is unreadable. 送り火 does not speak. 少女 does not speak. 早瀬甚吾 does not speak. The 定型句 does not appear (it comes at Clip 3).

## Sound Effects

- None — the fire makes no sound.

## Environment

- The damp near-silence; every sound far away; no footsteps, no breath, no rail, no wind.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Sorrowful without sentiment; suspended. Never sinister`
- Emotional Function: `Hold the unheard voice under the silence; it may thin toward the close`

---

# 15. CONTINUITY

> 30本は30回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

## Identity（must remain consistent）

- 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. A mark on his forehead — 該当なし, a square mark in the boundary script, thin and angular, dark ink. (Follows `ukebi-okuribi-character-sheet/…21_38_35.png`.)
- 少女 — a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet, though no rain falls on her; a dark-indigo neckerchief at the collar; long dark indigo hair; a quiet, steady gaze. She does not resemble 送り火. No mark on her forehead. (Follows `ukebi-hana-character-sheet/…21_36_52.png`.)
- 早瀬甚吾's fire — a pale blue-white flame; a half-transparent earth-toned vision of a soldier heavy with a solitary death, unlike 少女.
- The stage — a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls.

## Visual Continuity

- **The light law** — the soul-fire is the one true light; the dim indigo carries the rest.
- **The palette law** — muted, low-saturation everywhere; the fire alone is bright.
- **The scarf law** — the girl's neckerchief is always the deep damp-dark indigo; it never changes color.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; almost all movement is the fire's faint drift.

## Sound Continuity

- **The sound law** — near-silence; the narration speaks once.

---

# 16. CONSTRAINTS

## MUST

- Show the fire as a **pale blue-white flame**, not a human shape.
- Show the guest's vision as a **half-transparent, earth-toned, dissolving apparition** — a soldier with the weight of an unseen corpse, not a solid body.
- Keep the vision **unlike 少女** — no schoolgirl, no sailor uniform, no indigo hair.
- Show the girl as a **solid, real figure** — not translucent, not dissolving, not a fire.
- Show the mark 該当なし on 送り火's forehead (pressed in 06-3), never on the girl's.
- Fix her neckerchief as the deep damp-dark indigo; it never changes color.
- Keep 送り火's face, hair, build, coat and namelessness exactly as the attached character sheet.

## MUST NOT（この1本の禁止・開示台帳 07 レンジより）

- **No name for the girl** — 篠宮花 is not spoken and never appears on screen. She is only 少女.
- **No mark on the girl's forehead.** **No resemblance of the girl to 送り火.**
- **No translucent/dissolving girl** — she is a real, solid body.
- **No glow on the girl** — she does not emit light.
- **No solid guest body** — the guest stays a half-transparent vision, unlike 少女.
- No red scarf, no white scarf, no bright neckerchief, no changing scarf color, no drifting neckwear color.
- No readable text — no Japanese kanji or kana, no real-world alphabet. The boundary script only.

## PREFER

- Silence over score.
- The unheard last voice within the fire as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the exact shape of the fire's inner vision.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 少女 is unnamed, unmarked, unlike 送り火, and a solid figure; the guest is a half-transparent vision unlike 少女. This outranks everything, including beauty.
2. **Identity stability** — both real figures must not drift across the take; they follow the attached character sheets.
3. **The unheard last voice** — letters no one read, a last word no one heard.
4. **The fire is not a human shape** — the vision is a memory the fire reflects.
5. **The scarf fix** — the neckerchief is deep damp-dark indigo, never changing.
6. **The uneven density** — the unheard voice must hold the largest share.
7. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
8. **The style** — flat cel planes, soft light, limited animation.
9. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands, and a square mark on his forehead — 該当なし — in a thin angular unreadable boundary script; and a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though no rain falls, a dark-indigo neckerchief at the collar, long dark indigo hair, a quiet steady gaze — she does not resemble the man. A pale blue-white soul-fire floats before the man, and within and above it a half-transparent, earth-toned, dissolving vision of a soldier heavy with a solitary death — the fire does not take a human form, the vision is a memory the fire reflects, and it does not resemble the girl. Beats, deliberately uneven: [0:00–0:09] the fire arrives, the vision within it; [0:09–0:21] the letters no one read, the last voice no one heard, surfacing faintly; [0:21–0:30] he spoke and wrote though it would reach no one, and no one was there, and the man sees it. Cut on the unheard last voice. The unheard voice holds the largest share. (The girl's name 篠宮花 is not spoken, not shown.)

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands; a square mark on his forehead — 該当なし — in a thin, angular, fictional, unreadable boundary script, not Japanese, not any real alphabet. A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though no rain falls on her; a dark-indigo neckerchief at the collar, the same damp-dark indigo as the uniform; long dark indigo hair; a quiet steady gaze. She is a real, solid figure — not translucent, not dissolving, not a fire. She does not resemble the man. A pale blue-white flame, the only true light — not a human shape — and within and above it a half-transparent, earth-toned, dissolving vision of a soldier with the weight of an unseen corpse, his outline wavering; he is a memory, not a body, and he does not resemble the girl. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost nothing moves: the fire hovers steady, its inner vision drifting faintly; 送り火 and the girl are nearly still, his eyes attending. No wind, no dust, no particles, the faintest haze in the damp air; the barrier stays raised and still. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Fire-level and intimate; the unheard last voice within the fire is the subject, the faces secondary. Shallow depth of field; the vision in the fire is sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:09] the fire arriving, the vision within it. [0:09–0:21] the letters no one read, the last voice no one heard; hold on the vision. [0:21–0:30] 送り火 seeing, then back to the vision; cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. The boundary's voice speaks once, near and far: 早瀬甚吾、という。 送り火 does not speak; the girl does not speak; the guest does not speak. The fire makes no sound. No 定型句 here. No footsteps, no breath, no rail, no wind. Music extremely sparse — a few sustained tones at most — thinning toward the close. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no name text, no nameplate, no subtitle naming the girl, no red scarf, no white scarf, no bright neckerchief, no changing scarf color, no drifting neckwear color, no translucent girl, no dissolving girl, no ghostly girl, no glowing girl, no bloom on the girl, no mark on the girl's forehead, no reflection of a girl, no feminine mirror of the man's face, no copy of the man, no double, no solid guest body, no guest as a real person, no guest resembling the girl, no schoolgirl guest, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch07-seg01-30s-01`
- Segment ID: `07-1`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_HANA (hana character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_07_悼む, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 9s / 12s / 9s. The unheard voice = BEAT 2 at 12s (40%)`
- Camera Events: `3 events as listed in §10. All third-person-limited holds`
- Action Events: `ACT_ARRIVE → ACT_SEE`
- Audio Events: `boundary's voice (早瀬甚吾、という) ／ silence`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the unheard voice`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The guest may render as a solid person.** He must be a half-transparent, dissolving vision.
- **The guest may resemble 少女.** He must be a different kind of shape entirely.
- **The girl may be translucent or ghost-like.** She must be a real, solid body.
- **The neckerchief may drift in color.** It must stay deep damp-dark indigo.

## Changes

- _(none yet)_

## Next Generation

- 07-2 continues — 送り火 mourns 早瀬甚吾 (the voice calls his name), then 少女 speaks: あなたを悼む声がない。 The voice stops.
