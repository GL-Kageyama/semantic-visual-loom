# Wan 3.0 Full Specification — 受け火 序章「迎え火」Clip 2/3「喉の留まり（姿なき）」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・魂火）のみ日本語。
> この1本の個性：**序章の第2幕＝喉の留まりを「姿なきまま」見てしまう**。画面には何も描かず、語りだけで「燃えている」を運ぶ。炎も発光も出さない。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the second third of the prologue (迎え火) into one 30-second take seen through あなた's eyes — 送り火 passes before you, and you catch sight of something lodged in his throat, shown only as stillness, never as flame or figure`
- Register: `Restrained and spare. Emotion is never named — it surfaces through a throat that shows nothing while the narration insists something burns. The horror and the tenderness both live in ordinary objects and withheld action`
- Rule: `One organ = one turn; the prologue = three takes (overview / the unseen stop / only you see). The 留まり is invisible — carried by voice and stillness, never by light. Second person`

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
- **The throat shows nothing** — no glow, no flame, no inner light. An ordinary throat, still.

### Behavior

- Personality: `Does not name; quiet. Does not name emotion. Has nothing that could be called an answer`
- Typical Motion: `Only the eight-organ ritual moves; everything else is near-still`
- Emotional Range: `Suppressed. No readable emotion on the face. Response appears as stillness — a hand that stops, a throat that will not move`

### Continuity Requirements

- Must preserve: `face, hair, build, age, the dark-indigo coat, and the namelessness (nothing about him draws the eye)`

## あなた (YOU)

- ID: `YOU`
- Type: `PRESENCE (the viewer, second person)`
- Role: `The one standing at the crossing. Not a visible figure — the camera's vantage and the narration's addressee`

### Appearance

- **Never shown.** No body, no silhouette, no hands in frame. あなた is the position the camera occupies, not a person in the image.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter
- `遮断機` (the barrier) — raised, never lowering; its shadow falls black across the track

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `all distant`

---

# 5. OBJECTS

- `魂火` — 既に送られた。手のひらにぬくもりだけが残る。`CRITICAL`（光源はここでは残照だけ）
- `喉` — ただの喉。何も光らない。留まりは**姿を見せない**

---

# 6. REFERENCES

- `REF_CHARACTER` — `ukebi-okuribi-character-sheet/ChatGPT Image 2026年8月26日 21_38_35.png` · `HIGH`。Defines 送り火's face, hair, build, coat, and the namelessness. Does **not** define events or emotional tone
- `REF_STYLE` — `references/styles/soft-cel-anime.md` · `HIGH`。Defines rendering, palette discipline, lineart weight, shading steps, motion idiom
- `REF_FORMAT` — `references/formats/video-spec.md` · `HIGH`。Defines the §1–20 skeleton, uneven density, the identity lock, the six §18 slots
- `REF_SOURCE` — `soul-voice-teller/examples/ukebi/草稿/draft_00_迎え火` · `CRITICAL`。Defines every event, the second-person voice, and what is and is not revealed
- `REF_BIBLE` — `soul-voice-teller/examples/ukebi/台帳/series-bible.md` · `CRITICAL`。Defines the staged disclosure, the voice rules, and the organ ledger

---

# 7. NARRATIVE

## Core Event

送り火が、あなたの前を通り過ぎる。そのとき、見えてしまう。喉の奥に、何かがひとつ留まっている。八つの器官のどれにも当てはまらない何か。火でもない。魂でもない。なのに、燃えている。画面には何も見えない——ただの喉が、静かに通り過ぎていく。語りだけが、それを告げる。

## Beginning

儀礼は終わった。送り火が、あなたの前を通り過ぎようとする。火は既に送られ、手のひらにぬくもりだけが残っている。

## Turn

そのとき、見えてしまう。喉の奥に、何かがひとつ留まっている。どの器官もそれを処理できない。どの動詞もそれを動かせない。火でもない。魂でもない。なのに、燃えている。

## Peak

画面には、その「燃えている」ものは出ない。喉はただの喉だ。静かだ。光もない。語りが「燃えている」と言うたび、画面の喉はますます何も見せない。そのずれが、留まりを留まりにしている。

## Pull（引き — 切れ目）

送り火は通り過ぎていく。喉の奥の何かは、彼には気づかれていない。Cut。

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The glimpsed stop — a throat showing nothing while the narration insists — holds the largest share.

## Temporal Units

- BEAT — a held gaze (あなた's eyes) over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:08]` — 「通り過ぎる」 — ESTABLISH.** 送り火 approaches and begins to pass before you; the ritual is done; the warmth is left on the palm. _Density: SPARSE — the approach._
- **BEAT 2 `[0:08–0:22]` — 「見えてしまう」 — CORE, longest share.** You catch sight of it: something lodged in the throat. The throat shows nothing — no glow, no flame, no inner light. The narration insists: 火でもない。魂でもない。なのに、燃えている。 _Density: HELD — the gap between what is spoken and what is shown._
- **BEAT 3 `[0:22–0:30]` — 「気づかれていない」.** He passes on, unaware. The throat is just a throat. Cut. _Density: HELD — the passage, the unnoticed thing._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the glimpsed stop, spoken not shown (0:08–0:22) ／ the passage (≈0:04) ／ the unnoticed leaving (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:08 (the approach)`
- Dense regions: `0:08–0:22 (the spoken-yet-unseen stop)`
- Long continuous action: `0:22–0:30 the passage, the leaving`
- Rapid transitions: `none — a slow, held gaze`

---

# 9. ACTION

## Action — ACT_APPROACH

- ID: `ACT_APPROACH`
- Subject: `OKURIBI (送り火)`
- Action: `Approaches and begins to pass before あなた; the ritual is done`
- Intention: `To move past — the day's work continues`
- Intensity: `Low`
- Speed: `A slow passage`

### Action Relationship

- Before: `—`
- After: `ACT_GLIMPSE`

## Action — ACT_GLIMPSE

- ID: `ACT_GLIMPSE`
- Subject: `YOU (あなた, the vantage — not shown)`
- Action: `Catch sight of something lodged in the throat — a thing no organ can process, no verb can move`
- Intention: `None — it is seen, not sought`
- Intensity: `Low, held`
- Speed: `Still; the glimpse is a seeing, not a motion`

### Action Relationship

- Before: `ACT_APPROACH`
- After: `ACT_LEAVE`

## Action — ACT_LEAVE

- ID: `ACT_LEAVE`
- Subject: `OKURIBI (送り火)`
- Action: `Passes on, unaware; the throat shows nothing; the thing stays unnoticed`
- Intention: `To continue — he does not know`
- Intensity: `Low`
- Speed: `A slow leaving`

### Action Relationship

- Before: `ACT_GLIMPSE`
- After: `— (cut on the leaving)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Second person — the camera is あなた's vantage at the crossing, never showing あなた's body, never a face`
- Lens Character: `Watching from where you stand; the man's throat is the subject, the face secondary`
- Depth of Field: `Shallow — the throat and the man are sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with you; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final. The camera is あなた's eyes — it never shows its own body or hands.`

## Camera Events

- **`[0:00–0:08]`** — 送り火 approaches, passing before you; the camera holds at your eye-level.
- **`[0:08–0:22]`** — Close on the throat: it shows nothing, no glow, no light — the camera holds on the ordinary throat while the narration speaks.
- **`[0:22–0:30]`** — He passes on; the camera holds as the unnoticed thing leaves the frame with him. Cut.

---

# 11. MOTION

## Subject Motion

- 送り火 passes before you — a slow, unhurried walk; the throat shows nothing.
- あなた has no motion; you are a vantage, not a body in the frame.

## Object Motion

- The barrier stays raised and still; nothing is stirred.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.

## Physical Characteristics

- Weight: `送り火's body has ordinary heft; the passage is slow`
- Inertia: `High for the world; the walk is fluid but unhurried`
- Acceleration: `Gentle everywhere; nothing snaps`
- Fluidity: `Limited-animation — holds punctuated by small precise gestures`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Stillness (the ritual done, the warmth left)
- ↓ The glimpse (something lodged, seen by you alone)
- ↓ The gap (the narration insists; the image refuses)
- ↓ The leaving (unnoticed, carried on)

## Emotional Events

- Event: `You catch sight of the thing in the throat` — Emotion: `A held wrongness — a thing no organ can process, spoken but not shown` — Intensity: `LOW, entirely internal` — Timing: `≈0:11`
- Event: `He passes on, unaware` — Emotion: `The loneliness of seeing what no one else sees` — Intensity: `LOW, a held stillness` — Timing: `≈0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The departed fire's faint spill — the warmth left on the palm, barely a light now`
- Fill Light: `Almost none. Deep indigo shadow fills everything`
- Rim Light: `A very faint cool edge on the man from the memory of the fire`
- Ambient Light: `Near-black indigo and rust red`
- Color Temperature: `Cold blue-white, fading against deep indigo and rust red`

## Lighting Events

- **`[0:00]`** — 送り火 in the damp dark, the fire's warmth already leaving the palm.
- **`[0:08–0:22]`** — The throat in shadow. It shows no light. Hold.
- **`[0:22–0:30]`** — He passes into the dim. Hold. Cut.

---

# 14. AUDIO

## Dialogue

> **The boundary's voice** (境の地の声, second person): `そのとき、見えてしまう。喉の奥に、何かがひとつ留まっている。` Then `火でもない。魂でもない。なのに、燃えている。` — the narration carries what the image refuses to show. 送り火 does not speak. The 定型句 does not appear here (it comes at Clip 3).

## Sound Effects

- Almost none — the damp near-silence of a place where time does not flow.

## Environment

- The damp near-silence; every sound far away; no footsteps, no breath, no rail, no wind.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender without sentiment. Never sinister`
- Emotional Function: `Hold the stillness; it may thin toward the close, leaving only the spoken words`

---

# 15. CONTINUITY

> 30本は30回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

## Identity（must remain consistent）

- 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. No mark on his forehead. (Follows `ukebi-okuribi-character-sheet/…21_38_35.png`.)
- The stage — a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls.
- あなた — never a visible body; the camera is your vantage, the narration addresses you.

## Visual Continuity

- **The light law** — the soul-fire's pale blue-white is the only light and the only bright value; here it is already leaving, a fading spill.
- **The palette law** — muted, low-saturation everywhere; the pale blue-white soul-fire is the only bright value.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the passage.

## Sound Continuity

- **The sound law** — no sound except the boundary's voice.

---

# 16. CONSTRAINTS

## MUST

- Show the throat as nothing — no glow, no flame, no inner light, no figure. The stop is carried by the narration and the stillness alone.
- Keep 送り火's face, hair, build, coat and namelessness exactly as the attached character sheet.
- End on him passing on, unaware; cut on the leaving.
- Keep the camera as あなた's vantage — never show あなた's body or hands.

## MUST NOT（この1本の禁止・開示台帳 序 レンジより）

- **No 花** — no schoolgirl, no sailor uniform, no long dark indigo hair, no quiet steady gaze of a girl, no second figure, no female figure, no silhouette of another person.
- **No glowing object in the throat, no flame inside the throat, no inner light in the throat, no light leaking from the throat, no light inside the body.** The 留まり must not be made visible.
- No on-screen text.
- No visible あなた — no viewer's hands, no first-person body parts in frame.

## PREFER

- Silence over score.
- The throat as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the exact depth of the shadow, the fading warmth on the palm.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 花 is absent: no schoolgirl, no sailor uniform, no second figure. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take; it follows the attached character sheet.
3. **The throat restraint** — no glow, no flame, no inner light in the throat. The stop is spoken, not shown.
4. **The second person** — the camera is あなた's vantage; あなた is never a visible body.
5. **The uneven density** — the glimpsed stop must hold the largest share.
6. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
7. **The style** — flat cel planes, soft light, limited animation.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere, seen through the viewer's own eyes — second person, あなた's vantage, never showing the viewer's body. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl anywhere. Beats, deliberately uneven: [0:00–0:08] he approaches and begins to pass before you, the ritual done, the warmth left on the palm; [0:08–0:22] you catch sight of something lodged in his throat — but the throat shows nothing, no glow, no flame, no inner light, an ordinary throat held still while the narration speaks 火でもない。魂でもない。なのに、燃えている。; [0:22–0:30] he passes on, unaware, the thing unnoticed. Cut on the leaving. The gap between the spoken and the shown holds the largest share.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl, no sailor uniform, no long dark indigo hair, no second figure. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The throat shows nothing: no glow, no flame, no inner light, no light leaking from the throat. The viewer is never shown — no hands, no body in frame. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the man's slow passage; the body holds still. The throat shows nothing — no movement, no light. No wind, no dust, no particles, the faintest haze in the damp air. The barrier stays raised and still. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Second person — the camera is the viewer's own vantage at the crossing, never showing the viewer's body, hands, or face. Watching from where you stand; the man and his throat are the subject. Shallow depth of field; the throat and the man are sharp, the crossing falls away. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:08] he approaches, passing before you. [0:08–0:22] close on the throat — it shows nothing — the camera holding while the narration speaks. [0:22–0:30] he passes on; hold on the leaving. Cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. The boundary's voice, near and far, addresses you: そのとき、見えてしまう。喉の奥に、何かがひとつ留まっている。 Then 火でもない。魂でもない。なのに、燃えている。 No other dialogue. Music extremely sparse — a few sustained tones at most — thinning toward the close. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no schoolgirl, no sailor uniform, no long dark indigo hair, no second person, no female figure, no silhouette of another person, no reflection of a girl, no viewer's hands, no first-person body parts, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no light leaking from the throat, no light inside the body, no readable text, no Japanese kanji or kana, no real-world alphabet, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch00-seg02-30s-01`
- Segment ID: `A-2`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_00_迎え火, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 8s / 14s / 8s. The glimpsed stop = BEAT 2 at 14s (47%)`
- Camera Events: `3 events as listed in §10. Second person, no visible viewer`
- Action Events: `ACT_APPROACH → ACT_GLIMPSE → ACT_LEAVE`
- Audio Events: `boundary's voice (second person) ／ near-silence`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the leaving`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The throat may glow.** The restraint is tested hardest here. The throat must show nothing — no light, no flame, no glow, no figure. Verify frame by frame.
- **The narration may be rendered as on-screen text.** The spoken 燃えている must stay voice-only; verify no captions appear.
- **The viewer may appear.** The camera must stay a vantage — no hands, no body in frame.
- **A schoolgirl may be added.** The negative front-loads `no schoolgirl`; verify frame by frame.

## Changes

- _(none yet)_

## Next Generation

- If the stop is glimpsed without ever being shown, A-3 (あなただけが見えている) closes the prologue — 送り火 unaware, only you seeing, and the 定型句.
