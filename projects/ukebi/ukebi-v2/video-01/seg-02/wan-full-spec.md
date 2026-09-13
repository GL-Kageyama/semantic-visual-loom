# Wan 3.0 Full Specification — 受け火 第1章「送る」Clip 2/3「送る・問い」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・幸恵・魂火）のみ日本語。
> この1本の個性：**第1章の第2幕＝手が送る、そして問いが戻る**。送った後の空の手のひらに問いが置かれる。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the ritual-and-question third of Chapter 1 (送る) into one 30-second take that ends on its pull — the hand sends 幸恵, and a voice comes back to the empty palm`
- Register: `Restrained and spare. Emotion is never named — it surfaces through the body (a hand that scoops, an open palm that receives a question). The horror and the tenderness both live in ordinary objects and withheld action`
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

## 魂火 (TAMABI) — 幸恵

- ID: `SACHI`
- Name: `幸恵`
- Type: `SUBJECT (a soul of the dead)`
- Role: `The soul to be sent — a woman who walked until she fell by the roadside`

### Appearance

- A pale blue-white fire, **not human-shaped**, earth-colored (土の色).
- The fire brightens a little as the hand takes it; it has no weight, yet warmth lingers on the palm.
- No apparition here — the inner life was shown in Clip 1; here the fire is only a fire being sent.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter as the fire departs
- `台帳` (the ledger) — dry paper; each turned page rasps かさり, the only sound at the boundary; the name 幸恵 is written in one line

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `all distant except the dry rustle of the ledger's page`

---

# 5. OBJECTS

- `魂火（幸恵）` — 青白い火、土の色。唯一の光源。手に取られると少し明るくなる。`CRITICAL`（すくう手にぬくもりが残る）
- `台帳` — 名を綴じる本。乾いた白い紙、暗い墨の**境文字**（架空の字形・実在の文字ではない）。**このクリップで開かれ、魂の名が境文字で一行記される**。世界に実在する文字が現れる唯一の面——その文字は生者には読めない

---

# 6. REFERENCES

- `REF_CHARACTER` — `ukebi-okuribi-character-sheet/ChatGPT Image 2026年8月26日 21_38_35.png` · `HIGH`。Defines 送り火's face, hair, build, coat, and the namelessness. Does **not** define events or emotional tone
- `REF_STYLE` — `references/styles/soft-cel-anime.md` · `HIGH`。Defines rendering, palette discipline, lineart weight, shading steps, motion idiom
- `REF_FORMAT` — `references/formats/video-spec.md` · `HIGH`。Defines the §1–20 skeleton, uneven density, the identity lock, the six §18 slots
- `REF_SOURCE` — `soul-voice-teller/examples/ukebi/草稿/draft_01` · `CRITICAL`。Defines every event, the exact on-screen text, and what is and is not revealed
- `REF_BIBLE` — `soul-voice-teller/examples/ukebi/台帳/series-bible.md` · `CRITICAL`。Defines the staged disclosure, the voice rules, and the organ ledger

---

# 7. NARRATIVE

## Core Event

送り火 moves his hand — the first of the eight organs. The hand takes the fire, raises it, sends it down the flow. The name is written in one line of the ledger — in the boundary script, unreadable glyphs; the narration speaks it, 幸恵. The fire flows away, and beyond the rails brightens a little. Then a voice comes back — 「あなたは、誰に送られるの」 — laid on the empty palm. He does not answer; he has no answer.

## Beginning

The fire rests before his hand. The hand scoops it, raises it, sends it. The ritual — unhesitating, practiced, chosen without thought. The fire brightens a little; warmth lingers on the palm.

## Turn

The fire is already gone from the palm — yet the voice comes back. It lays a question on his hand. He does not answer; he has never been asked. He has a hand that scoops, and no hand that has ever been scooped.

## Peak

The open palm, empty now, with the question laid on it. 「あなたは、誰に送られるの」 — the voice, near and far, arriving after the fire is gone.

## Pull（引き — 切れ目）

Cut on the empty palm. (The 定型句 does not appear here — it comes at Clip 3.)

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The returned question and the empty palm hold the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「送る」 — ESTABLISH.** The hand scoops the fire, raises it, sends it down the flow. The fire brightens a little; the name 幸恵 is written in one line of the ledger. _Density: TRANSITION — the ritual, unhesitating._
- **BEAT 2 `[0:07–0:12]` — 「流れる」.** The fire flows away down the rail; beyond the rails brightens a little. The palm is left open and empty. _Density: SPARSE — a held departure._
- **BEAT 3 `[0:12–0:20]` — 「問い」.** 「あなたは、誰に送られるの」 — the fire's voice returns, laying a question on his palm. He does not answer; he has never been asked. _Density: DENSE — the voice comes back against the flow._
- **BEAT 4 `[0:20–0:30]` — 「空の手」 — CORE, longest share.** The open palm, empty, the question laid on it. Hold. Cut. _Density: HELD — the question, then the clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the returned question (0:12–0:20) ／ the empty palm (0:20–0:30) ／ the name 幸恵 recorded (≈0:05)`

## Temporal Density

- Sparse regions: `0:07–0:12 (the departure)`
- Dense regions: `0:12–0:20 (the returned question)`
- Long continuous action: `0:20–0:30 the empty palm, held`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_SEND

- ID: `ACT_SEND`
- Subject: `OKURIBI (送り火)`
- Action: `The hand scoops the fire, raises it, sends it down the flow; the name 幸恵 is written in the ledger`
- Intention: `The ritual — unhesitating, practiced, chosen without thought`
- Intensity: `Low, unvarying`
- Speed: `Steady, practiced, each gesture distinct`

### Action Relationship

- Before: `—`
- After: `ACT_FLOW`

## Action — ACT_FLOW

- ID: `ACT_FLOW`
- Subject: `SACHI (幸恵's soul-fire)`
- Action: `Flows away down the rail; beyond the rails brightens a little; the palm is left open`
- Intention: `To be sent — no resistance, no fear`
- Intensity: `Low`
- Speed: `A slow gliding departure`

### Action Relationship

- Before: `ACT_SEND`
- After: `ACT_QUESTION`

## Action — ACT_QUESTION

- ID: `ACT_QUESTION`
- Subject: `SACHI (幸恵's soul-fire)`
- Action: `「あなたは、誰に送られるの」 — the already-departed fire lays a question on his palm`
- Intention: `Not to accuse — to ask. The first question he has ever been asked`
- Intensity: `Medium, quiet`
- Speed: `A voice, near and far, arriving after the fire is gone`

### Action Relationship

- Before: `ACT_FLOW`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `OKURIBI (送り火)`
- Action: `The open palm, empty, the question laid on it — he does not answer`
- Intention: `None. He has no answer; he has never been asked`
- Intensity: `Low, a held stillness`
- Speed: `Still; the palm stays open`

### Action Relationship

- Before: `ACT_QUESTION`
- After: `— (cut on the empty palm)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not inside his first person`
- Lens Character: `Hand-level and intimate; the hand is the subject, the face secondary`
- Depth of Field: `Shallow — the hand, the fire, and the ledger line are sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with the hand; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:07]`** — Close on the hand: scoop, raise, send. A brief tilt to the ledger as the name 幸恵 is written in one line.
- **`[0:07–0:12]`** — The fire flows away down the rail; beyond brightens a little; the palm is left open.
- **`[0:12–0:20]`** — Close on the open palm, empty now. The voice returns to it — the camera holds on the hand, not the face.
- **`[0:20–0:30]`** — Hold on the empty palm. Cut.

---

# 11. MOTION

## Subject Motion

- The hand carries essentially all the movement; the rest of the body holds.
- Scoop, raise, send — practiced, unhurried, without hesitation.
- 幸恵's fire brightens a little, then flows away down the rail without resistance.

## Object Motion

- The ledger page turns with a single dry rustle as the name 幸恵 is written.
- The barrier stays raised and still.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.
- Beyond the rails brightens a little as the fire departs; nothing else moves.

## Physical Characteristics

- Weight: `The fire has no weight; warmth alone stays on the palm. 送り火's hand has ordinary heft`
- Inertia: `High for the body, near-zero for the fire (instant, gliding)`
- Acceleration: `Gentle everywhere; the stop is the only abrupt thing, and it is stillness, not a snap`
- Fluidity: `Limited-animation — holds punctuated by small precise gestures`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Routine (scoop, raise, send — the unhesitating ritual)
- ↓ Unasked (a question laid on the palm, with no answer in him)
- ↓ The empty palm (the first question, left open)

## Emotional Events

- Event: `The name 幸恵 recorded` — Emotion: `Routine without ceremony — one more name in the ledger` — Intensity: `LOW` — Timing: `≈0:05`
- Event: `「あなたは、誰に送られるの」` — Emotion: `Unasked — he has no answer; he has never been asked` — Intensity: `MEDIUM, entirely internal, in the open palm` — Timing: `≈0:16`
- Event: `The empty palm held` — Emotion: `The question left open — nothing is concluded` — Intensity: `LOW, a held stillness` — Timing: `≈0:26`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `幸恵's soul-fire — pale blue-white, the only light and the only bright value`
- Fill Light: `Almost none. Deep indigo shadow fills everything the fire does not reach`
- Rim Light: `A very faint cool edge on the hand and coat from the fire's spill`
- Ambient Light: `Near-black indigo and rust red; the rails glow faintly as the fire departs`
- Color Temperature: `Cold blue-white against deep indigo and rust red, with the earth-color in the fire`

## Lighting Events

- **`[0:00]`** — The fire rests before his hand, the only light.
- **`[0:00–0:07]`** — The fire brightens a little as the hand takes it; the ledger's page catches the light for the name 幸恵.
- **`[0:07–0:12]`** — The fire departs; beyond the rails brightens a little; the palm dims.
- **`[0:12–0:30]`** — The palm is empty and dim; only the warmth's faint glow remains. Hold. Cut.

---

# 14. AUDIO

## Dialogue

> **The boundary's voice** (境の地の声): `幸恵、という` — the narration speaks the name, since the ledger's script is unreadable. **The fire's voice** (幸恵's soul-fire): `あなたは、誰に送られるの` — Japanese, character-for-character, near and far, a voice that comes back after the fire is gone. 送り火 does not speak — he has no answer. The 定型句 does not appear here.

## Sound Effects

- A single dry rustle of the ledger page (かさり) as the name 幸恵 is written — the one close sound.
- All else is far: no footsteps, no breath, no rail, no wind.

## Environment

- The damp near-silence of a place where time does not flow — a silence in which the page's rustle and the returned voice are the only events.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender without sentiment. Never sinister`
- Emotional Function: `Hold the stillness under the ritual; it may thin toward the close`

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

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the organ's gesture.

## Sound Continuity

- **The sound law** — no sound except the dry rustle of the registry's page.

---

# 16. CONSTRAINTS

## MUST

- Establish the hand's ritual — scoop, raise, send — practiced and unhesitating.
- Render the on-screen text as the **boundary script** — thin, angular, fictional, unreadable glyphs, not Japanese. The name `幸恵` is spoken by the narration, never written in readable text.
- Keep the soul-fire the sole light source.
- End on the empty palm, cut on the hand.

## MUST NOT（この1本の禁止・開示台帳 01 レンジより）

- **No 花** — no schoolgirl, no sailor uniform, no long dark indigo hair, no second person, no female figure, no silhouette of another person, no reflection of a girl.
- **No glowing object in the throat, no flame inside the throat, no inner light in the throat.** The 留まり is not shown here.
- No apparition inside the fire — the inner life was shown in Clip 1; here the fire is only a fire being sent.
- No on-screen text other than the ledger line `幸恵`.

## PREFER

- Silence over score.
- The hand as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the ledger's binding, the exact hue of the earth-color, the fire's waver.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 花 is absent: no schoolgirl, no sailor uniform, no second figure. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take; it follows the attached character sheet.
3. **The boundary script, not readable text** — the on-screen ledger line is the fictional boundary script (unreadable glyphs), never Japanese; the name `幸恵` and the dialogue are carried by the voice.
4. **The throat restraint** — no glow, no flame, no inner light in the throat.
5. **The uneven density** — the returned question and the empty palm must hold the largest share.
6. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
7. **The style** — flat cel planes, soft light, limited animation.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl anywhere. Beats, deliberately uneven: [0:00–0:07] the hand scoops the earth-colored soul-fire — 幸恵 — raises it, sends it down the flow, and the name is written in one line of the ledger in the boundary script — thin, angular, unreadable glyphs, not Japanese — while the narration speaks 幸恵; [0:07–0:12] the fire flows away down the rail and beyond brightens a little, the palm left open; [0:12–0:20] the fire is already gone, yet a voice returns to the empty palm — あなたは、誰に送られるの — and he does not answer; [0:20–0:30] the open palm, empty, the question laid on it. Cut on the empty palm. The question and the empty palm hold the largest share. (The pull — この魂は、まだ誰にも名付けられていない。 — does not appear in this clip.)

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl, no sailor uniform, no long dark indigo hair, no second figure. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The soul-fire is earth-colored, pale blue-white, not human-shaped, the only light and the only bright value. A dry ledger whose page bears one line in the boundary script — thin, angular, fictional, unreadable glyphs, not Japanese, not any real alphabet. No apparition inside the fire. No glowing object in the throat, no flame inside the throat, no inner light in the throat. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the hand and the fire; the body holds still. The hand scoops, raises, and sends the fire down the flow in one practiced, unhurried gesture, without hesitation; the fire brightens a little and flows away without resistance. The ledger page turns with a single dry rustle as 幸恵 is written. No wind, no dust, no particles, the faintest haze in the damp air; the barrier stays raised and still. The fire has no weight, only warmth on the palm. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Hand-level and intimate; the hand is the subject, the face secondary. Shallow depth of field; the hand, the fire, and the ledger line are sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:07] close on the hand — scoop, raise, send; a brief tilt to the ledger as 幸恵 is written. [0:07–0:12] the fire flows away, beyond brightens a little, the palm left open. [0:12–0:20] close on the empty palm; the voice returns to it, the camera holding on the hand, not the face. [0:20–0:30] hold on the empty palm. Cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. A single dry rustle of the ledger page as the name is written, the one close sound; all else far away, no footsteps, no breath, no wind. The boundary's voice speaks the name — 幸恵、という. Then a voice — 幸恵's soul-fire, near and far, returning after the fire is gone: あなたは、誰に送られるの。 送り火 does not speak. Music extremely sparse — a few sustained tones at most — thinning toward the close. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no schoolgirl, no sailor uniform, no long dark indigo hair, no second person, no female figure, no silhouette of another person, no reflection of a girl, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no apparition inside the fire, no human shape in the fire, no readable text, no Japanese kanji or kana, no real-world alphabet, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch01-seg02-30s-01`
- Segment ID: `01-2`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_01, CRITICAL)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 5s / 8s / 10s. The empty palm = BEAT 4 at 10s (33%)`
- Camera Events: `4 events as listed in §10. All third-person-limited holds and a tilt`
- Action Events: `ACT_SEND → ACT_FLOW → ACT_QUESTION → ACT_HOLD`
- Audio Events: `幸恵's voice ／ ledger rustle ／ near-silence`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the empty palm`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The ledger line 幸恵 may render as noise.** It is evidence — character-for-character. If unusable, tighten the shot on the page; the name must read.
- **The question may read as a whisper too faint.** It must be a clear, near-and-far voice returning to the palm.
- **A schoolgirl may be added.** The negative front-loads `no schoolgirl`; verify frame by frame.
- **The throat may glow.** Must be absent — no light, no flame in the throat.

## Changes

- _(none yet)_

## Next Generation

- If the question lands, 01-3 continues with the hand touching the throat — and stopping.
