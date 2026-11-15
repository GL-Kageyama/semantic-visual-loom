# Wan 3.0 Full Specification — 受け火 第2章「綴じる」Clip 3/3「指が止まる（白い頁）」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・結城文・魂火）のみ日本語。
> この1本の個性：**第2章の第3幕＝綴じる指が「読む」を知り、白い頁の上で止まる**。転は静止で語る。頁は白いまま。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the stop-and-pull third of Chapter 2 (綴じる) into one 30-second take that ends on its pull — the finger that can bind but not read stops over the blank page`
- Register: `Restrained and spare. Emotion is never named — it surfaces through a finger that stops over a blank page, and a page that trembles wanting to be read. The horror and the tenderness both live in ordinary objects and withheld action`
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
- Role: `The soul that asked 読んで — his fire holds beside the blank page`

### Appearance

- A pale blue-white fire, **not human-shaped**, wavering like it wants to turn a page.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter
- `台帳` (the ledger) — dry paper; open to the blank first page; the last row always blank

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `all distant except the dry rustle of the ledger's page`

---

# 5. OBJECTS

- `台帳` — 開かれた白い頁。文字はない。頁が震えて「読んでほしい」と待っている。`CRITICAL`
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

送り火は頁を読もうとする。読めない。綴じる指は持っていても、読む指は持っていなかった。誰かの頁を読んだことがなかった。誰かに読まれたことも。白い頁は白いまま、彼の指の下でじっとしている。文字はない。それなのに、頁は読んでほしいと震えている。綴じる指が、初めて「読む」ということを知りたがる。指が、止まる。

## Beginning

指が、白い頁の上にある。読もうとする。頁は白いまま、動かない。

## Turn

読めない。綴じる指は持っていても、読む指は持っていなかった。誰かの頁を読んだことがない。誰かに読まれたこともない。

## Peak

白い頁は白いまま震えている。紙のかさり、という音が、震えているように聞こえる。綴じる指が、初めて「読む」ということを知りたがる。

## Pull（引き — 切れ目）

指が、止まる。白い頁が一枚、彼の指の下で、まだ震えている。The 定型句 — この魂は、まだ誰にも名付けられていない。 Cut。

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The stopping holds the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「読もうとする」 — ESTABLISH.** The finger is on the blank page, trying to read. The page is white, still. _Density: SPARSE — a held blank page._
- **BEAT 2 `[0:07–0:19]` — 「止まる」 — CORE, longest share.** He cannot read. He has a finger to bind, no finger to read. The page trembles, wanting to be read; the binding finger learns, for the first time, what it is to want to read. The finger stops. _Density: HELD — the stop, then a clean stillness._
- **BEAT 3 `[0:19–0:30]` — 「震える頁・定型句」.** The blank page trembles under his stopped finger. The 定型句 — この魂は、まだ誰にも名付けられていない。 — as the boundary's whisper. Cut. _Density: HELD — the whisper, then the clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the finger stopping (0:07–0:19) ／ the 定型句 (≈0:24)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the blank page)`
- Dense regions: `0:19–0:30 (the 定型句)`
- Long continuous action: `0:07–0:19 the finger, stopping over the page`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_TRY

- ID: `ACT_TRY`
- Subject: `OKURIBI (送り火)`
- Action: `Tries to read the blank page under his finger`
- Intention: `To read — a verb the binding finger does not hold`
- Intensity: `Low, held`
- Speed: `Still; the trying is a held gaze, not a motion`

### Action Relationship

- Before: `—`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `OKURIBI (送り火)`
- Action: `The finger stops over the blank page. He cannot read; the page trembles, wanting it`
- Intention: `None — the finger that binds has no finger to read; the stop is not chosen`
- Intensity: `Low, a held stillness`
- Speed: `A complete halt; the page trembles lightly`

### Action Relationship

- Before: `ACT_TRY`
- After: `— (cut on the stopped finger)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not inside his first person`
- Lens Character: `Hand-level and intimate; the finger and the page are the subject, the face secondary`
- Depth of Field: `Shallow — the finger and the page are sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with the finger; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:07]`** — Close on the finger over the blank page; the page is white, still.
- **`[0:07–0:19]`** — The finger stops; the page trembles under it. Hold on the stopped finger; the page trembles.
- **`[0:19–0:30]`** — Hold on the stopped finger; the page trembles; the 定型句 whispers. Cut.

---

# 11. MOTION

## Subject Motion

- The finger carries essentially all the movement; the rest of the body holds.
- The stop is a complete halt; the page trembles lightly, a held motion.

## Object Motion

- The blank page trembles; the ledger is otherwise still; the fire wavers.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.

## Physical Characteristics

- Weight: `The finger's touch has ordinary heft; the stop has the weight of stillness`
- Inertia: `High for the body; the stop is the only abrupt thing, and it is stillness, not a snap`
- Acceleration: `Gentle everywhere; the stop is absolute`
- Fluidity: `Limited-animation — holds punctuated by small precise gestures`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Stillness (the blank page, the trying)
- ↓ The inability (a finger to bind, no finger to read)
- ↓ The stop (the binding finger learns what it is to want to read)
- ↓ The trembling (the page waits, the whisper names the unnamed)

## Emotional Events

- Event: `The finger stops over the blank page` — Emotion: `The stop — a finger that can bind but not read, now wanting to` — Intensity: `LOW, a held stillness` — Timing: `≈0:13`
- Event: `The 定型句` — Emotion: `The boundary's own whisper — この魂は、まだ誰にも名付けられていない。` — Intensity: `LOW, near and far` — Timing: `≈0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `結城文's soul-fire — pale blue-white, the only light and the only bright value`
- Fill Light: `Almost none. Deep indigo shadow fills everything`
- Rim Light: `A very faint cool edge on the finger and page from the fire's spill`
- Ambient Light: `Near-black indigo and rust red`
- Color Temperature: `Cold blue-white against deep indigo and rust red`

## Lighting Events

- **`[0:00]`** — The blank page in the fire's cool light, bright and empty.
- **`[0:07–0:19]`** — The finger stops; the fire's waver plays over the page.
- **`[0:19–0:30]`** — The stopped finger in the fire's light; the page trembles. Hold. Cut.

---

# 14. AUDIO

## Dialogue

> **The 定型句** (境の地の声, near-and-far whisper): `この魂は、まだ誰にも名付けられていない。` as the pull. 送り火 does not speak. 結城文's fire does not speak again.

## Sound Effects

- The dry rustle of the ledger's page — now trembling, like the paper wants to be read. Almost no other sound.

## Environment

- The damp near-silence of a place where time does not flow — a silence in which the whisper is the only event.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender without sentiment. Never sinister`
- Emotional Function: `Hold the stillness; it may thin toward the close, leaving only the whisper`

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

- **The sound law** — no sound except the dry rustle of the ledger's page, and at the pull, the boundary's own whisper.

---

# 16. CONSTRAINTS

## MUST

- End on the finger stopping over the blank page, cut on the stopped finger.
- Keep the page blank — no text appears on it, readable or otherwise.
- The 定型句 `この魂は、まだ誰にも名付けられていない。` as the boundary's whisper (near and far), not on-screen text.
- Keep 送り火's face, hair, build, coat and namelessness exactly as the attached character sheet.

## MUST NOT（この1本の禁止・開示台帳 02 レンジより）

- **No 花** — no schoolgirl, no sailor uniform, no long dark indigo hair, no quiet steady gaze of a girl, no second figure, no female figure, no silhouette of another person.
- **No glowing object in the throat, no flame inside the throat, no inner light in the throat.** The 留まり is not made visible here.
- No readable text — no Japanese kanji or kana, no real-world alphabet. The page is blank.
- No apparition inside the fire.

## PREFER

- Silence over score.
- The finger and the page as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the depth of the page's whiteness, the tremble of the page.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 花 is absent: no schoolgirl, no sailor uniform, no second figure. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take; it follows the attached character sheet.
3. **The blank page** — the page stays blank; the name was already spoken, never written here.
4. **The uneven density** — the stop must hold the largest share.
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl anywhere. Beats, deliberately uneven: [0:00–0:07] the finger rests on the blank page, trying to read; [0:07–0:19] he cannot read — a finger to bind, no finger to read — the page trembles, wanting it, and the finger stops completely; [0:19–0:30] the blank page trembles under the stopped finger, and the pull whispers この魂は、まだ誰にも名付けられていない。 Cut on the stopped finger. The stop holds the largest share.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl, no sailor uniform, no long dark indigo hair, no second figure. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The soul-fire is pale blue-white, not human-shaped, the only light and the only bright value. A blank page under the finger — clean, white, no text. No glowing object in the throat, no flame inside the throat, no inner light in the throat. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the finger; the body holds still. The finger stops over the blank page completely — a held halt, not a snap; the page trembles lightly under it. The fire wavers. No wind, no dust, no particles, the faintest haze in the damp air. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Hand-level and intimate; the finger and the page are the subject, the face secondary. Shallow depth of field; the finger and the page are sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:07] close on the finger over the blank page. [0:07–0:19] the finger stops; the page trembles; hold on the stopped finger. [0:19–0:30] hold on the stopped finger; the 定型句 whispers. Cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. The dry rustle of the ledger's page, now trembling like the paper wants to be read. Then the pull, the 定型句 in the boundary's own whisper, near and far: この魂は、まだ誰にも名付けられていない。 Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only the whisper. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no schoolgirl, no sailor uniform, no long dark indigo hair, no second person, no female figure, no silhouette of another person, no reflection of a girl, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no apparition inside the fire, no human shape in the fire, no readable text, no Japanese kanji or kana, no real-world alphabet, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch02-seg03-30s-01`
- Segment ID: `02-3`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_02_綴じる, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 7s / 12s / 11s. The stop = BEAT 2 at 12s (40%)`
- Camera Events: `3 events as listed in §10. All third-person-limited holds`
- Action Events: `ACT_TRY → ACT_STOP`
- Audio Events: `定型句 (境の地の声) ／ dry rustle of the page`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the stopped finger`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The blank page may gain text.** It must stay clean and blank; verify no characters appear on it.
- **The stop may read as a flinch.** It must be a complete, unhurried halt. If it reads as a twitch, slow it.
- **A schoolgirl may be added.** The negative front-loads `no schoolgirl`; verify frame by frame.
- **The throat may glow.** Must be absent — no light, no flame in the throat.

## Changes

- _(none yet)_

## Next Generation

- If the finger stops and the page stays blank, Chapter 3 (呑む / 胎児 / 喉) continues — the smallest fire, and the girl who appears at the seat of 該当なし.
