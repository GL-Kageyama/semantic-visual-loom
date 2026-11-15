# Wan 3.0 Full Specification — 受け火 第3章「呑む」Clip 2/3「喉が動かない」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・魂火・該当なし）のみ日本語。
> この1本の個性：**第3章の第2幕＝喉が火を呑み、初めて動かなくなる**。八器官の初の停止。台帳の一番下に「該当なし」の印が境文字で浮かぶ。喉の炎は描かない。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the ritual-and-stop third of Chapter 3 (呑む) into one 30-second take — the throat swallows the nameless fire and, for the first time, will not move; the 該当なし mark surfaces in the ledger`
- Register: `Restrained and spare. Emotion is never named — it surfaces through a throat that stops mid-motion, and a mark that surfaces in the ledger. The horror and the tenderness both live in ordinary objects and withheld action`
- Rule: `One organ = one turn; one chapter = three takes (arrival / ritual-and-question / stop-and-pull); nothing is added after the pull. The throat's stop is stillness, never light`

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
- **The throat shows nothing** — no glow, no flame, no inner light. It moves, then stops; that is all.
- No mark on his forehead (the seal appears only from S08).

### Behavior

- Personality: `Does not name; quiet. Does not name emotion. Has nothing that could be called an answer`
- Typical Motion: `Only the eight-organ ritual moves; everything else is near-still`
- Emotional Range: `Suppressed. No readable emotion on the face. Response appears as stillness — a hand that stops, a throat that will not move`

### Continuity Requirements

- Must preserve: `face, hair, build, age, the dark-indigo coat, and the namelessness (nothing about him draws the eye)`

## 魂火 (TAMABI) — 名なしの胎児

- ID: `UNNAMED`
- Name: `（名なし）`
- Type: `SUBJECT (a soul of the dead)`
- Role: `The nameless soul being swallowed — cast out before it was named`

### Appearance

- A pale blue-white fire, **not human-shaped**, the smallest of all fires. It sinks into the throat and stays there.

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

- `魂火（名なしの胎児）` — 喉の奥へ沈んでいく。青白い火、唯一の光源。`CRITICAL`
- `台帳` — 名を綴じる本。一番下の欄に、印がひとつ浮かぶ——**該当なし。画面に映る文字は境文字（細く角張った架空の字形・実在の文字ではない）**

---

# 6. REFERENCES

- `REF_CHARACTER` — `ukebi-okuribi-character-sheet/ChatGPT Image 2026年8月26日 21_38_35.png` · `HIGH`。Defines 送り火's face, hair, build, coat, and the namelessness. Does **not** define events or emotional tone
- `REF_STYLE` — `references/styles/soft-cel-anime.md` · `HIGH`。Defines rendering, palette discipline, lineart weight, shading steps, motion idiom
- `REF_FORMAT` — `references/formats/video-spec.md` · `HIGH`。Defines the §1–20 skeleton, uneven density, the identity lock, the six §18 slots
- `REF_SOURCE` — `soul-voice-teller/examples/ukebi/草稿/draft_03_呑む` · `CRITICAL`。Defines every event, the exact on-screen text, and what is and is not revealed
- `REF_BIBLE` — `soul-voice-teller/examples/ukebi/台帳/series-bible.md` · `CRITICAL`。Defines the staged disclosure, the voice rules, and the organ ledger

---

# 7. NARRATIVE

## Core Event

送り火は喉を動かす。八つの器官の三つ目。魂を呑む。転生先へ送るのではなく、いったん喉の奥へしまう。喉が上下する。火が喉の奥へ沈んでいく。それで終わりのはずだった。喉が、動かない。魂は喉に残る。完璧だったはずの八器官が、初めて止まった。台帳の一番下の欄に、印がひとつ浮かぶ——該当なし。

## Beginning

送り火は喉を動かす。火が喉の奥へ沈んでいく。喉が上下する。名もない火を、名もないまま流れへ戻す。それが境の営みだった。

## Turn

喉が、動かない。呑み込んだはずの火が、喉の奥に残る。どの器官もそれを引き受けられない。どの動詞もそれを動かせない。八器官が、初めて止まった。

## Peak

喉の奥で、火が静かに燃え続けている——**だが、その炎は画面に出さない**。喉はただ止まっている。名のない火が、名のないまま喉を塞いでいる。台帳の一番下の欄に、印がひとつ浮かぶ。

## Pull（引き — 切れ目）

該当なし。境文字の印が、白い欄に浮かぶ。声がそれを言う。Cut。（少女は Clip 3。）

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The throat's stop holds the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:08]` — 「呑む」 — ESTABLISH.** The throat moves; the nameless fire sinks into it. The throat rises and falls. _Density: SPARSE — the practiced swallowing._
- **BEAT 2 `[0:08–0:20]` — 「喉が動かない」 — CORE, longest share.** The throat stops. It will not move. The fire stays lodged; the eight organs stop for the first time. The throat shows nothing — no glow, no flame. _Density: HELD — the stop, then a clean stillness._
- **BEAT 3 `[0:20–0:30]` — 「該当なし」.** In the ledger's last row, a mark surfaces — 該当なし, in the boundary script, spoken by the voice. Cut on the mark. _Density: HELD — the mark, then the cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the throat stopping (0:08–0:20) ／ the 該当なし mark surfacing (≈0:24)`

## Temporal Density

- Sparse regions: `0:00–0:08 (the swallowing)`
- Dense regions: `0:08–0:20 (the stop) ／ 0:20–0:30 (the mark)`
- Long continuous action: `0:08–0:20 the throat, stopping`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_SWALLOW

- ID: `ACT_SWALLOW`
- Subject: `OKURIBI (送り火)`
- Action: `The throat moves; the nameless fire sinks into it`
- Intention: `To swallow one soul — the third organ, without hesitation`
- Intensity: `Low, exact`
- Speed: `A slow, practiced swallow`

### Action Relationship

- Before: `—`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `OKURIBI (送り火)`
- Action: `The throat stops. It will not move. The fire stays lodged; the eight organs stop for the first time`
- Intention: `None — the stop is not chosen; no organ can take the fire, no verb can move it`
- Intensity: `Low, a held stillness`
- Speed: `A complete halt; the throat is still`

### Action Relationship

- Before: `ACT_SWALLOW`
- After: `— (cut on the 該当なし mark)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not inside his first person`
- Lens Character: `Throat-level and intimate; the throat and the ledger are the subject, the face secondary`
- Depth of Field: `Shallow — the throat and the mark are sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with the throat; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:08]`** — Close on the throat, moving as the fire sinks in; a brief tilt to the ledger, the last row blank.
- **`[0:08–0:20]`** — The throat stops; hold on the still throat, showing nothing.
- **`[0:20–0:30]`** — The ledger's last row: the 該当なし mark surfaces in boundary script. Hold on the mark. Cut.

---

# 11. MOTION

## Subject Motion

- The throat carries the motion — a swallow, then a complete halt.
- The fire sinks into the throat and stays.

## Object Motion

- The ledger is still, then the mark surfaces in the last row — a slow appearing, not a movement.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.

## Physical Characteristics

- Weight: `The throat's swallow has ordinary heft; the stop has the weight of stillness`
- Inertia: `High for the body; the stop is the only abrupt thing, and it is stillness, not a snap`
- Acceleration: `Gentle everywhere; the stop is absolute`
- Fluidity: `Limited-animation — holds punctuated by small precise gestures`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Stillness (the swallowing, as always)
- ↓ The stop (the throat will not move)
- ↓ The mark (該当なし surfacing)
- ↓ The unspoken (the first failure of the perfect apparatus)

## Emotional Events

- Event: `The throat stops` — Emotion: `The first stop of the eight organs — the perfect apparatus fails, and it is only stillness` — Intensity: `LOW, entirely internal` — Timing: `≈0:13`
- Event: `The 該当なし mark surfaces` — Emotion: `The world records what no organ can process — a mark that means no name fits` — Intensity: `LOW, a held stillness` — Timing: `≈0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The nameless soul-fire — pale blue-white, the only light and the only bright value, now lodged in the throat`
- Fill Light: `Almost none. Deep indigo shadow fills everything`
- Rim Light: `A very faint cool edge on the throat and coat from the fire's spill`
- Ambient Light: `Near-black indigo and rust red`
- Color Temperature: `Cold blue-white against deep indigo and rust red`

## Lighting Events

- **`[0:00]`** — The fire's light plays on the throat as it swallows.
- **`[0:08–0:20]`** — The throat in the fire's faint spill, still. It shows no inner light. Hold.
- **`[0:20–0:30]`** — The ledger's last row, the mark surfacing in the dim. Hold. Cut.

---

# 14. AUDIO

## Dialogue

> **The boundary's voice** (境の地の声): `該当なし。` — the narration speaks the mark, since the ledger's script is unreadable. 送り火 does not speak. The 定型句 does not appear here (it comes at Clip 3).

## Sound Effects

- Almost none — the damp near-silence. A dry rustle as the ledger's mark surfaces.

## Environment

- The damp near-silence; every sound far away; no footsteps, no breath, no rail, no wind.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender without sentiment. Never sinister`
- Emotional Function: `Hold the stillness under the stop; it may thin toward the close`

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

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the throat.

## Sound Continuity

- **The sound law** — no sound except the dry rustle of the ledger's page.

---

# 16. CONSTRAINTS

## MUST

- Show the throat stopping — a complete halt, no glow, no flame, no inner light. The fire lodged in the throat must **not** be shown as a light.
- Render the 該当なし mark as the **boundary script** — thin, angular, fictional, unreadable glyphs, not Japanese. The word 該当なし is spoken by the narration, never written in readable text.
- End on the 該当なし mark; cut on the mark.
- Keep 送り火's face, hair, build, coat and namelessness exactly as the attached character sheet.

## MUST NOT（この1本の禁止・開示台帳 03 レンジより）

- **No 花** — no schoolgirl, no sailor uniform, no long dark indigo hair, no quiet steady gaze of a girl, no second figure, no female figure, no silhouette of another person. (She appears in Clip 3, not here.)
- **No glowing object in the throat, no flame inside the throat, no inner light in the throat, no light leaking from the throat, no light inside the body.** The swallowed fire is not made visible as a light.
- No readable text — no Japanese kanji or kana, no real-world alphabet. The boundary script only.

## PREFER

- Silence over score.
- The throat and the mark as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the exact shape of the boundary script glyphs, the depth of the shadow.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 花 is absent: no schoolgirl, no sailor uniform, no second figure. She appears only in Clip 3. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take; it follows the attached character sheet.
3. **The throat restraint** — no glow, no flame, no inner light in the throat. The stop is stillness, not light.
4. **The boundary script, not readable text** — 該当なし is spoken, never written legibly.
5. **The uneven density** — the stop must hold the largest share.
6. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
7. **The style** — flat cel planes, soft light, limited animation.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl anywhere. Beats, deliberately uneven: [0:00–0:08] the throat moves, and the nameless fire sinks into it, the throat rising and falling; [0:08–0:20] the throat stops — it will not move, the fire staying lodged, the eight organs stopping for the first time, the throat showing nothing, no glow, no light; [0:20–0:30] in the ledger's last row, a mark surfaces — 該当なし, in the boundary script, spoken by the voice. Cut on the mark. The stop holds the largest share. (The pull — この魂は、まだ誰にも名付けられていない。 — does not appear in this clip.)

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl, no sailor uniform, no long dark indigo hair, no second figure. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The soul-fire is pale blue-white, not human-shaped, the only light and the only bright value, the smallest of all fires, now lodged in the throat. The throat shows nothing: no glow, no flame, no inner light. A dry ledger whose last row bears one mark in the boundary script — thin, angular, fictional, unreadable glyphs, not Japanese, not any real alphabet. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the throat; the body holds still. The throat swallows once, then stops completely — a held halt, not a snap; the fire stays lodged. The ledger's mark surfaces slowly in the last row. No wind, no dust, no particles, the faintest haze in the damp air. The barrier stays raised and still. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Throat-level and intimate; the throat and the ledger are the subject, the face secondary. Shallow depth of field; the throat and the mark are sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:08] close on the throat, moving; a brief tilt to the blank last row. [0:08–0:20] the throat stops; hold on the still throat. [0:20–0:30] the ledger's last row, the mark surfacing; hold on the mark. Cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. A dry rustle as the ledger's mark surfaces, the one close sound. The boundary's voice speaks the mark — 該当なし。 No other dialogue. Music extremely sparse — a few sustained tones at most — thinning toward the close. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no schoolgirl, no sailor uniform, no long dark indigo hair, no second person, no female figure, no silhouette of another person, no reflection of a girl, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no light leaking from the throat, no light inside the body, no readable text, no Japanese kanji or kana, no real-world alphabet, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch03-seg02-30s-01`
- Segment ID: `03-2`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_03_呑む, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 8s / 12s / 10s. The stop = BEAT 2 at 12s (40%)`
- Camera Events: `3 events as listed in §10. All third-person-limited holds`
- Action Events: `ACT_SWALLOW → ACT_STOP`
- Audio Events: `boundary's voice (該当なし) ／ dry rustle`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the 該当なし mark`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The throat may glow.** This is where the restraint is tested hardest. The throat must show nothing; verify frame by frame that no light, flame, or glow appears.
- **The 該当なし mark may render as real Japanese.** It must be thin, angular, fictional, unreadable glyphs. Verify it is not legible.
- **A schoolgirl may be added.** The negative front-loads `no schoolgirl`; verify frame by frame — 花 appears only in Clip 3.
- **The stop may read as a flinch.** It must be a complete, unhurried halt.

## Changes

- _(none yet)_

## Next Generation

- If the stop reads and the mark surfaces, 03-3 introduces 花 — a girl in a dark-indigo sailor uniform at the seat of 該当なし, watching him.
