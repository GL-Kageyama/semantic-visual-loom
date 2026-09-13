# Wan 3.0 Full Specification — 受け火 第7章「悼む」Clip 2/3「悼む＋「悼む声がない」」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・少女・早瀬甚吾）のみ日本語。
> この1本の個性：**第7章の第2幕＝所作・転。声が動き、死んだ者の名が声に乗せられる。悼むとは、名を声に乗せること。それで終わるはずだった。少女が言う——「あなたを悼む声がない」。** 声はまだ完全には止まらない（止まるのは Clip 3）。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the ritual-and-turn of Chapter 7 (悼む) into one 30-second take — the voice moves and the dead man's name is carried on it; to mourn is to carry a name on the voice; that is how it was always to end — until the girl speaks: あなたを悼む声がない`
- Register: `Restrained and spare. The turn is a single spoken sentence. Emotion is never named; it is a name carried on a low voice, and a girl's quiet interruption of it`

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
- Color Language: `Muted, low-saturation. The world is deep indigo and rust red. The soul-fire is a pale blue-white`
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
- A mark on his forehead — 該当なし, a square mark in the boundary script (pressed in 06-3).

### Behavior

- Personality: `Does not name; quiet. Does not name emotion. Has nothing that could be called an answer`
- Typical Motion: `Almost still; his voice moves, and carries a dead man's name`
- Emotional Range: `Suppressed. No readable emotion on the face; the mourning is in the voice, not the face`

### Continuity Requirements

- Must preserve: `face, hair, build, age, the dark-indigo coat, the namelessness, and the forehead mark 該当なし`

## 少女 (the girl) — 花・未開示

- ID: `GIRL`
- Name: `少女 (her name is not spoken and never appears on screen — 篠宮花 is revealed only in Chapter 8)`
- Type: `CHARACTER`
- Role: `The girl who speaks the turn — あなたを悼む声がない`

### Appearance

- A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet, though no rain falls on her.
- A dark-indigo neckerchief at the collar — the same damp-dark indigo as the uniform. **The neckerchief is always this deep indigo; it never changes color.**
- Long dark indigo hair; a quiet, steady gaze.
- She does **not** resemble 送り火. **No mark on her forehead.** A **solid, real figure** — not translucent, not dissolving, not a fire. She does not glow.

### Behavior

- Personality: `Quiet and steady; she speaks one sentence, plainly`
- Typical Motion: `Almost still; her lips move once`
- Emotional Range: `Not named. Her plainness is the whole of it`

### Continuity Requirements

- Must preserve: `the dark-indigo sailor uniform that reads damp-dark though dry, the deep-indigo neckerchief, the long dark indigo hair, the quiet steady gaze, and the absence of any resemblance to 送り火`

## 早瀬甚吾 (HAYASE JINGO) — ゲストの魂火

- ID: `GUEST_07`
- Name: `早瀬甚吾 (his name is carried by the voice, never written on screen)`
- Type: `SOUL-FIRE / VISION`
- Role: `Guest — a soldier who died alone; his fire waits before the voice's organ`

### Appearance

- The soul-fire is a **pale blue-white flame**; within and above it, a half-transparent earth-toned vision of a soldier heavy with a solitary death.

### Behavior

- Personality: `Solitary; he is mourned, and the mourning is his name carried on a voice`
- Typical Motion: `Almost none; the vision drifts faintly`
- Emotional Range: `A solitary death, held in an unheard word`

### Continuity Requirements

- Must preserve: `the solitary weight; the half-transparency; the absolute non-resemblance to 少女`

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent
- `魂火` (the soul-fire) — the pale blue-white fire of 早瀬甚吾

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air`
- Background Motion: `almost none; time does not flow`
- Sound: `the only sound is the low voice carrying a name`

---

# 5. OBJECTS

- `魂火` — the pale blue-white fire holding 早瀬甚吾's vision. `MINOR`

---

# 6. REFERENCES

- `REF_CHARACTER` — `ukebi-okuribi-character-sheet/ChatGPT Image 2026年8月26日 21_38_35.png` · `HIGH`
- `REF_HANA` — `ukebi-hana-character-sheet/ChatGPT Image 2026年8月26日 21_36_52.png` · `HIGH`
- `REF_STYLE` — `references/styles/soft-cel-anime.md` · `HIGH`
- `REF_FORMAT` — `references/formats/video-spec.md` · `HIGH`
- `REF_SOURCE` — `soul-voice-teller/examples/ukebi/草稿/draft_07_悼む` · `CRITICAL`
- `REF_BIBLE` — `soul-voice-teller/examples/ukebi/台帳/series-bible.md` · `CRITICAL`

---

# 7. NARRATIVE

## Core Event

送り火は、声を動かす。八つの器官の、七つ目。魂を悼む。低い声で名前が呼ばれる。早瀬甚吾。死んだ者の名が声に乗せられる。悼むということは、名を声に乗せることだった。それで終わりのはずだった。「あなたを悼む声がない」少女が、言う。

## Beginning

声が動く。低い声で、名が呼ばれる。早瀬甚吾。死んだ者の名が、声に乗せられる。悼むとは、名を声に乗せること。

## Turn

「あなたを悼む声がない」——少女が、言う。

## Peak

それで終わるはずだった。悼む。悼んで送る。それが境の営みだった。それが、少女のひとことで止められる。

## Pull（引き — 切れ目）

Cut on the girl's line, the mourning voice left hanging. 声が完全に止まるのは Clip 3。（定型句も Clip 3。）

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The girl's single sentence holds the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:09]` — 「名を声に乗せる」 — ESTABLISH.** The voice moves; a low voice calls the dead man's name. 早瀬甚吾. _Density: SPARSE — the working ritual._
- **BEAT 2 `[0:09–0:21]` — 「少女のひとこと」 — CORE, longest share.** あなたを悼む声がない — the girl speaks, once. _Density: HELD — the sentence._
- **BEAT 3 `[0:21–0:30]` — 「止められる」.** The mourning is cut short by her words; the voice left hanging. Cut. _Density: HELD — the interruption, then the cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the name carried on the voice (≈0:04) ／ the girl's line (≈0:11) ／ the mourning cut short (≈0:23)`

## Temporal Density

- Sparse regions: `0:00–0:09 (the name on the voice)`
- Dense regions: `0:09–0:21 (the girl's line) ／ 0:21–0:30 (the interruption)`
- Long continuous action: `0:09–0:21 the single sentence, held`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_MOURN

- ID: `ACT_MOURN`
- Subject: `OKURIBI (送り火)`
- Action: `Moves his voice — the seventh organ — and mourns; a low voice carries the dead man's name: 早瀬甚吾`
- Intention: `To mourn — to carry the name on the voice`
- Intensity: `Low, a low steady voice`
- Speed: `Slow; the name is spoken once, low`

### Action Relationship

- Before: `—`
- After: `ACT_SPEAK`

## Action — ACT_SPEAK

- ID: `ACT_SPEAK`
- Subject: `GIRL (少女)`
- Action: `Speaks one sentence — あなたを悼む声がない`
- Intention: `To tell him what no one has ever told him`
- Intensity: `Low, a plain quiet sentence`
- Speed: `Slow; spoken once`

### Action Relationship

- Before: `ACT_MOURN`
- After: `ACT_CUTSHORT`

## Action — ACT_CUTSHORT

- ID: `ACT_CUTSHORT`
- Subject: `OKURIBI (送り火)`
- Action: `The mourning is cut short; the voice is left hanging`
- Intention: `None — the ritual is interrupted`
- Intensity: `Low, a held stillness`
- Speed: `Still; the voice hangs, not yet stopped`

### Action Relationship

- Before: `ACT_SPEAK`
- After: `— (cut on the girl's line)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not inside his first person`
- Lens Character: `Intimate and face-level; the girl's speaking lips are the subject, the faces secondary`
- Depth of Field: `Shallow — the girl's face as she speaks is sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with the line; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:09]`** — 送り火's voice moving; the name on the voice.
- **`[0:09–0:21]`** — The girl speaking, once. Hold on her lips.
- **`[0:21–0:30]`** — The mourning left hanging. Cut.

---

# 11. MOTION

## Subject Motion

- 送り火 is almost still; his voice moves. 少女 is almost still; her lips move once. The guest's vision drifts faintly.

## Object Motion

- The fire hovers, steady.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.

## Physical Characteristics

- Weight: `The name has no weight; it is carried on the voice`
- Inertia: `Near-total stillness; only the lips and the voice`
- Acceleration: `None`
- Fluidity: `Limited-animation — a held stillness, one spoken line`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Mourning (a name carried on the voice — the ritual works)
- ↓ The girl's line (あなたを悼む声がない)
- ↓ The interruption (the mourning cut short)
- ↓ The unspoken (who has been mourned, though not dead)

## Emotional Events

- Event: `The name carried on the voice` — Emotion: `To mourn is to carry a name on the voice` — Intensity: `LOW, a low steady voice` — Timing: `≈0:04`
- Event: `The girl's line` — Emotion: `あなたを悼む声がない — the one who mourns has no one to mourn him` — Intensity: `LOW, a quiet plain sentence` — Timing: `≈0:11`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The pale blue-white soul-fire of 早瀬甚吾 — the one true light`
- Fill Light: `Almost none. Soft indigo fills the space`
- Rim Light: `A faint cool edge on the girl's hair and 送り火's coat from the fire`
- Ambient Light: `Deep indigo; the rust-red of the rails reads faintly red in the damp dark`
- Color Temperature: `Cold, near-monochrome indigo, warmed only by the pale-blue fire`

## Lighting Events

- **`[0:00]`** — The name on the voice in the fire's light.
- **`[0:09–0:21]`** — The girl's face as she speaks.
- **`[0:21–0:30]`** — The mourning, hanging. Cut.

---

# 14. AUDIO

## Dialogue

> **送り火**（低い声で、一度）: `早瀬甚吾。` — the dead man's name carried on the voice; the mourning itself.
> **少女**（静かに、一度）: `あなたを悼む声がない。` 境の地の声 does not speak here. The 定型句 does not appear (it comes at Clip 3).

## Sound Effects

- None — the voice is the only sound.

## Environment

- The damp near-silence; every sound far away; no footsteps, no breath, no rail, no wind.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Sorrowful without sentiment; suspended. Never sinister`
- Emotional Function: `Hold the two spoken lines under the silence; it may thin toward the close`

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

- **The motion law** — limited animation, holds, twos and threes; almost all movement is the lips and the voice.

## Sound Continuity

- **The sound law** — near-silence; two spoken lines, no more.

---

# 16. CONSTRAINTS

## MUST

- Show the voice carrying the dead man's name; show the girl speaking one sentence.
- Render 送り火's mourning line 早瀬甚吾 as spoken, in a low voice, never as on-screen text.
- Render the girl's line あなたを悼む声がない as spoken, once, never as on-screen text.
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
- The girl's speaking face as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- The low quality of the voice to carry a little sorrow, unperformed.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 少女 is unnamed, unmarked, unlike 送り火, and a solid figure; the guest is a half-transparent vision unlike 少女. This outranks everything, including beauty.
2. **Identity stability** — both real figures must not drift across the take; they follow the attached character sheets.
3. **The two spoken lines** — the name on the voice, and the girl's single sentence; spoken, never written.
4. **The scarf fix** — the neckerchief is deep damp-dark indigo, never changing.
5. **The uneven density** — the girl's line must hold the largest share.
6. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
7. **The style** — flat cel planes, soft light, limited animation.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands, and a square mark on his forehead — 該当なし — in a thin angular unreadable boundary script; and a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though no rain falls, a dark-indigo neckerchief at the collar, long dark indigo hair, a quiet steady gaze — she does not resemble the man. Beats, deliberately uneven: [0:00–0:09] the man's voice moves and a low voice carries the dead man's name — 早瀬甚吾 — to mourn is to carry a name on the voice; [0:09–0:21] the girl speaks once — あなたを悼む声がない; [0:21–0:30] the mourning is cut short, the voice left hanging. Cut. The girl's line holds the largest share. (The girl's name 篠宮花 is not spoken, not shown.)

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands; a square mark on his forehead — 該当なし — in a thin, angular, fictional, unreadable boundary script. A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though no rain falls on her; a dark-indigo neckerchief at the collar, the same damp-dark indigo as the uniform; long dark indigo hair; a quiet steady gaze. She is a real, solid figure — not translucent, not dissolving, not a fire. She does not resemble the man. A pale blue-white flame with a half-transparent, earth-toned, dissolving vision of a soldier heavy with a solitary death inside it, unlike the girl. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost nothing moves: 送り火 is nearly still, his voice moving; the girl's lips move once; the guest's vision drifts faintly. No wind, no dust, no particles, the faintest haze in the damp air; the barrier stays raised and still. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Intimate and face-level; the girl's speaking face is the subject, the faces secondary. Shallow depth of field; the girl's face as she speaks is sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:09] 送り火's voice moving, the name on the voice. [0:09–0:21] the girl speaking, once; hold on her lips. [0:21–0:30] the mourning left hanging; cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. Two spoken lines, and no other sound. 送り火 speaks once, low: 早瀬甚吾。 The girl speaks once, quietly: あなたを悼む声がない。 No 定型句 here. No footsteps, no breath, no rail, no wind. Music extremely sparse — a few sustained tones at most — thinning toward the close. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no name text, no nameplate, no subtitle naming the girl, no red scarf, no white scarf, no bright neckerchief, no changing scarf color, no drifting neckwear color, no translucent girl, no dissolving girl, no ghostly girl, no glowing girl, no bloom on the girl, no mark on the girl's forehead, no reflection of a girl, no feminine mirror of the man's face, no copy of the man, no double, no solid guest body, no guest as a real person, no guest resembling the girl, no schoolgirl guest, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch07-seg02-30s-01`
- Segment ID: `07-2`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_HANA (hana character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_07_悼む, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 9s / 12s / 9s. The girl's line = BEAT 2 at 12s (40%)`
- Camera Events: `3 events as listed in §10. All third-person-limited holds`
- Action Events: `ACT_MOURN → ACT_SPEAK → ACT_CUTSHORT`
- Audio Events: `送り火 (早瀬甚吾) ／ 少女 (あなたを悼む声がない) ／ silence`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the girl's line`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The lines may render as on-screen text.** They must be spoken only.
- **The girl may be translucent or ghost-like.** She must be a real, solid body.
- **The guest may resemble 少女.** He must be a different kind of shape entirely.
- **The neckerchief may drift in color.** It must stay deep damp-dark indigo.

## Changes

- _(none yet)_

## Next Generation

- 07-3 closes the chapter — the voice stops; only she mourned him; mourning was not a voice but a weight placed on the chest. The 定型句 ends it.
