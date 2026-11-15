# Wan 3.0 Full Specification — 受け火 第2章「綴じる」Clip 2/3「綴じる・読んで」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・結城文・魂火）のみ日本語。
> この1本の個性：**第2章の第2幕＝指が台帳に名を綴じ、白い頁に触れ、「読んで」と問われる**。台帳の文字は境文字、名は声が運ぶ。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the ritual-and-question third of Chapter 2 (綴じる) into one 30-second take — the fingers bind 結城文's name into the ledger, the page is closed, a blank first page is touched, and the fire asks 読んで`
- Register: `Restrained and spare. Emotion is never named — it surfaces through a finger that binds, a blank page that trembles, and a question the man cannot answer. The horror and the tenderness both live in ordinary objects and withheld action`
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
- Open scooping hands — hands made to scoop, that have never been scooped.
- No mark on his forehead (the seal appears only from S08).

### Behavior

- Personality: `Does not name; quiet. Does not name emotion. Has nothing that could be called an answer`
- Typical Motion: `Only the eight-organ ritual moves; everything else is near-still`
- Emotional Range: `Suppressed. No readable emotion on the face. Response appears as stillness — a hand that stops, a throat that will not move`

### Continuity Requirements

- Must preserve: `face, hair, build, age, the dark-indigo coat, and the namelessness (nothing about him draws the eye)`

## 魂火 (TAMABI) — 結城文

- ID: `YUKI`
- Name: `結城文`
- Type: `SUBJECT (a soul of the dead)`
- Role: `The soul being bound — a writer who was never read even once; his fire asks 読んで`

### Appearance

- A pale blue-white fire, **not human-shaped**. Wavering like it wants to turn a page.
- No apparition inside the fire in this clip — the seeing happened in Clip 1; here the fire only asks.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter
- `台帳` (the ledger) — dry paper; each turned page rasps かさり, the only sound at the boundary; souls' names are entered line by line; the last row is always blank

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `all distant except the dry rustle of the ledger's page`

---

# 5. OBJECTS

- `台帳` — 名を綴じる本。乾いた白い紙。**画面に映る文字は境文字（細く角張った架空の字形・実在の文字ではない）**。一番下の欄だけはいつも白い。`CRITICAL`
- `魂火（結城文）` — 青白い火、頁をめくりたがるように揺れる。唯一の光源。

---

# 6. REFERENCES

- `REF_CHARACTER` — `ukebi-okuribi-character-sheet/ChatGPT Image 2026年8月26日 21_38_35.png` · `HIGH`。Defines 送り火's face, hair, build, coat, and the namelessness. Does **not** define events or emotional tone
- `REF_STYLE` — `references/styles/soft-cel-anime.md` · `HIGH`。Defines rendering, palette discipline, lineart weight, shading steps, motion idiom
- `REF_FORMAT` — `references/formats/video-spec.md` · `HIGH`。Defines the §1–20 skeleton, uneven density, the identity lock, the six §18 slots
- `REF_SOURCE` — `soul-voice-teller/examples/ukebi/草稿/draft_02_綴じる` · `CRITICAL`。Defines every event, the exact on-screen text, and what is and is not revealed
- `REF_BIBLE` — `soul-voice-teller/examples/ukebi/台帳/series-bible.md` · `CRITICAL`。Defines the staged disclosure, the voice rules, and the organ ledger

---

# 7. NARRATIVE

## Core Event

送り火は指を動かす。八つの器官の二つ目。台帳を開き、魂を一頁に綴じる。ペンが名を記す——結城文という名は、頁の上に一行、境文字で記される。紙は乾いている。墨は紙に吸われていく。頁は閉じられる。指が、台帳の最初の頁に触れる。頁は白紙だった。白いのは一番下の欄だけではなかった。「読んで」結城文の魂火が言う。

## Beginning

送り火は台帳を開く。指が頁を押さえる。ペンが名を記す。結城文という名が、頁の上に一行、境文字で記される。

## Turn

台帳の一番下の欄だけは、いつも白い。開くたび白い。指はそこを一度も綴じたことがない。綴じられた頁は閉じられる。指が、台帳の最初の頁に触れる。頁は白紙だった。

## Peak

「読んで」。結城文の魂火が言う。白い頁は白いまま、彼の指の下でじっとしている。紙のかさり、という音が、震えているように聞こえる。

## Pull（引き — 切れ目）

白い頁が一枚、指の下で震えている。Cut on the blank page. （読めない、は Clip 3。）

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The binding and the blank page hold the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:08]` — 「綴じる」 — ESTABLISH.** The fingers open the ledger, hold the page, and the pen writes the name 結城文 in one line of the boundary script — thin, angular, unreadable glyphs, not Japanese — while the narration speaks 結城文、という. _Density: SPARSE — the precise, unhesitating binding._
- **BEAT 2 `[0:08–0:20]` — 「白い頁」 — CORE, longest share.** The page is closed. The finger touches the first page — it is blank. Blank is not only the last row. _Density: HELD — the blank page, held under the finger._
- **BEAT 3 `[0:20–0:30]` — 「読んで」.** 結城文's fire says 読んで. The blank page trembles. Cut on the blank page. _Density: HELD — the question laid on the page._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the blank page under the finger (0:08–0:20) ／ the name written in boundary script (≈0:05) ／ 読んで (≈0:24)`

## Temporal Density

- Sparse regions: `0:00–0:08 (the binding)`
- Dense regions: `0:08–0:20 (the blank page) ／ 0:20–0:30 (the question)`
- Long continuous action: `0:08–0:20 the finger resting on the blank page`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_BIND

- ID: `ACT_BIND`
- Subject: `OKURIBI (送り火)`
- Action: `Opens the ledger, holds the page, and the pen writes the name 結城文 in one line of boundary script`
- Intention: `To bind one soul to one page — the second organ, without hesitation`
- Intensity: `Low, exact`
- Speed: `A slow, practiced gesture`

### Action Relationship

- Before: `—`
- After: `ACT_CLOSE`

## Action — ACT_CLOSE

- ID: `ACT_CLOSE`
- Subject: `OKURIBI (送り火)`
- Action: `Closes the page; the finger touches the first page — it is blank`
- Intention: `Closing is binding; the bound page is never opened — but the first page is blank, not only the last row`
- Intensity: `Low, held`
- Speed: `A slow touch, then rest`

### Action Relationship

- Before: `ACT_BIND`
- After: `ACT_ASK`

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `YUKI (結城文's soul-fire)`
- Action: `Speaks 読んで; the blank page trembles under the finger`
- Intention: `To be read — the one thing the binding finger cannot do`
- Intensity: `Low, near and far`
- Speed: `A held stillness; the page trembles`

### Action Relationship

- Before: `ACT_CLOSE`
- After: `— (cut on the blank page)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not inside his first person`
- Lens Character: `Hand-level and intimate; the finger and the page are the subject, the face secondary`
- Depth of Field: `Shallow — the finger, the page, and the fire are sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with the finger; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:08]`** — Close on the hand: the ledger opens, the pen writes the name in the boundary script; a brief tilt to the blank last row.
- **`[0:08–0:20]`** — The page closes; the finger touches the first page — blank. Hold on the blank page.
- **`[0:20–0:30]`** — The fire asks 読んで; the page trembles. Hold on the blank page. Cut.

---

# 11. MOTION

## Subject Motion

- The fingers carry almost all the movement — opening, holding, writing, closing, touching.
- The pen writes the name in one line of boundary script, the ink drawn into the dry paper.
- The blank page trembles under the finger.

## Object Motion

- The barrier stays raised and still; nothing is stirred.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.

## Physical Characteristics

- Weight: `The finger's touch has ordinary heft; the page trembles lightly`
- Inertia: `High for the body and the world; the page's trembling is a small, held motion`
- Acceleration: `Gentle everywhere; nothing snaps`
- Fluidity: `Limited-animation — holds punctuated by small precise gestures`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Stillness (the binding, as always)
- ↓ The blank page (not only the last row is white)
- ↓ The question (読んで)
- ↓ The trembling (the page waits to be read)

## Emotional Events

- Event: `The finger touches the blank first page` — Emotion: `A held wrongness — the binding finger has never bound the last row, and the first page is blank too` — Intensity: `LOW, entirely internal` — Timing: `≈0:13`
- Event: `The fire asks 読んで` — Emotion: `The question laid on the page — the one verb the finger does not know` — Intensity: `LOW, near and far` — Timing: `≈0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `結城文's soul-fire — pale blue-white, the only light and the only bright value`
- Fill Light: `Almost none. Deep indigo shadow fills everything the fire does not reach`
- Rim Light: `A very faint cool edge on the hand and page from the fire's spill`
- Ambient Light: `Near-black indigo and rust red`
- Color Temperature: `Cold blue-white against deep indigo and rust red`

## Lighting Events

- **`[0:00]`** — The hand and ledger under the fire's cool light; the dry paper catches the spill.
- **`[0:08–0:20]`** — The blank page in the fire's light, bright and empty.
- **`[0:20–0:30]`** — The fire's waver plays over the trembling page. Hold. Cut.

---

# 14. AUDIO

## Dialogue

> **The boundary's voice** (境の地の声): `結城文、という` — the narration speaks the name as the boundary script writes it. Then **結城文's soul-fire**: `読んで` — near and far, returning to the page. 送り火 does not speak. The 定型句 does not appear (it comes at Clip 3).

## Sound Effects

- A single dry rustle of the ledger's page — the one close sound, as the page is closed. All else far away.

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
- The stage — a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls.

## Visual Continuity

- **The light law** — the soul-fire's pale blue-white is the only light and the only bright value; everything else is deep indigo and rust red.
- **The palette law** — muted, low-saturation everywhere; the pale blue-white soul-fire is the only bright value.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the finger.

## Sound Continuity

- **The sound law** — no sound except the dry rustle of the ledger's page.

---

# 16. CONSTRAINTS

## MUST

- Render the on-screen name as the **boundary script** — thin, angular, fictional, unreadable glyphs, not Japanese. The name 結城文 is spoken by the narration, never written in readable text.
- Show the last row of the ledger blank, and the first page blank.
- End on the blank page under the finger, the fire asking 読んで; cut on the blank page.
- Keep 送り火's face, hair, build, coat and namelessness exactly as the attached character sheet.

## MUST NOT（この1本の禁止・開示台帳 02 レンジより）

- **No 花** — no schoolgirl, no sailor uniform, no long dark indigo hair, no quiet steady gaze of a girl, no second figure, no female figure, no silhouette of another person.
- **No glowing object in the throat, no flame inside the throat, no inner light in the throat.** The 留まり is not shown here.
- No readable text — no Japanese kanji or kana, no real-world alphabet, no English text. The boundary script only.
- No apparition inside the fire (the seeing is over).

## PREFER

- Silence over score.
- The finger and the page as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the exact shape of the boundary script glyphs (they stay thin and angular), the depth of the blank page's whiteness.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 花 is absent: no schoolgirl, no sailor uniform, no second figure. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take; it follows the attached character sheet.
3. **The boundary script, not readable text** — the name is spoken, never written in a readable script.
4. **The blank page** — the first page is blank, not only the last row.
5. **The uneven density** — the blank page must hold the largest share.
6. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
7. **The style** — flat cel planes, soft light, limited animation.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl anywhere. Beats, deliberately uneven: [0:00–0:08] the fingers open the ledger, hold the page, and the pen writes the name 結城文 in one line of the boundary script — thin, angular, unreadable glyphs, not Japanese — while the narration speaks 結城文、という; [0:08–0:20] the page is closed, and the finger touches the first page — it is blank, not only the last row; [0:20–0:30] the fire asks 読んで, and the blank page trembles under the finger. Cut on the blank page. The blank page and the question hold the largest share. (The pull — この魂は、まだ誰にも名付けられていない。 — does not appear in this clip.)

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl, no sailor uniform, no long dark indigo hair, no second figure. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The soul-fire is pale blue-white, not human-shaped, the only light and the only bright value, wavering like it wants to turn a page. A dry ledger whose page bears one line in the boundary script — thin, angular, fictional, unreadable glyphs, not Japanese, not any real alphabet — and whose last row is blank. Then the first page, blank. No apparition inside the fire. No glowing object in the throat, no flame inside the throat, no inner light in the throat. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the fingers and the page; the body holds still. The fingers open, hold, write, close, and touch in one practiced, unhurried sequence; the pen draws one line of boundary script into the dry paper. The page turns with a single dry rustle as it closes; the blank page trembles lightly under the finger. No wind, no dust, no particles, the faintest haze in the damp air; the barrier stays raised and still. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Hand-level and intimate; the finger, the page, and the fire are the subject, the face secondary. Shallow depth of field; the finger, the page, and the fire are sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:08] close on the hand — open, hold, write the boundary script; a brief tilt to the blank last row. [0:08–0:20] the page closes; the finger touches the blank first page; hold. [0:20–0:30] the fire asks 読んで; the page trembles; hold on the blank page. Cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. A single dry rustle of the ledger page as it closes, the one close sound; all else far away. The boundary's voice speaks the name — 結城文、という. Then 結城文's soul-fire, near and far: 読んで。 送り火 does not speak. Music extremely sparse — a few sustained tones at most — thinning toward the close. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no schoolgirl, no sailor uniform, no long dark indigo hair, no second person, no female figure, no silhouette of another person, no reflection of a girl, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no apparition inside the fire, no human shape in the fire, no readable text, no Japanese kanji or kana, no real-world alphabet, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch02-seg02-30s-01`
- Segment ID: `02-2`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_02_綴じる, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 8s / 12s / 10s. The blank page = BEAT 2 at 12s (40%)`
- Camera Events: `3 events as listed in §10. All third-person-limited holds`
- Action Events: `ACT_BIND → ACT_CLOSE → ACT_ASK`
- Audio Events: `boundary's voice (結城文、という) ／ 結城文's 読んで ／ single dry rustle`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the blank page`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The boundary script may render as real Japanese.** It must be thin, angular, fictional, unreadable glyphs. Verify the name is not legible.
- **The first page may not read as blank.** It must be a clean blank page, not a filled one. Verify no text appears on it.
- **A schoolgirl may be added.** The negative front-loads `no schoolgirl`; verify frame by frame.
- **The throat may glow.** Must be absent — no light, no flame in the throat.

## Changes

- _(none yet)_

## Next Generation

- If the blank page reads and the question lands, 02-3 closes the chapter — the finger that can bind but cannot read, stopping over the blank page, and the 定型句.
