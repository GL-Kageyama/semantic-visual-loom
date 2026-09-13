# Wan 3.0 Full Specification — 受け火 第1章「送る」Clip 1/3「幸恵が来る」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・幸恵・魂火）のみ日本語。
> この1本の個性：**第1章の第1幕＝客（幸恵）の来臨と、火の中の死に方（半透明の旅人）**。送る前の「見る」を描く。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the arrival-and-inner-life third of Chapter 1 (送る) into one 30-second take that ends on its pull — the guest 幸恵 is seen before she is sent`
- Register: `Restrained and spare. Emotion is never named — it surfaces through the body and through what a man sees inside a fire. The horror and the tenderness both live in ordinary objects and withheld action`
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

- A pale blue-white fire, **not human-shaped**. The fire is the body; the guest's death is not the fire taking a human form, but a memory the fire shows.
- Earth-colored (土の色) — a soul that walked until it fell by the wayside. The earth-color rides the pale blue-white, wavering between blue and red.
- Within the fire, faintly, the death surfaces as a **translucent apparition, not a solid figure** — a weary traveler: feet that kept walking, a dry throat, a place never reached. Half-dissolved, the edges wavering, earth-toned, melting back into the flame.
- Weightless; warmth lingers in the hand that scoops it.

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

- `魂火（幸恵）` — 青白い火、土の色。唯一の光源。人のかたちをしていない。`CRITICAL`（火の中の死に方＝歩き続けた足・乾いた喉・届かなかった場所を、半透明の旅人の幻として映す）
- `台帳` — 名を綴じる本。乾いた白い紙、墨の字。**世界に実在する文字が現れる唯一の面**。このクリップではまだ開かれない（綴じるのは Clip 2）

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

The crossing has no morning, only the hour work begins. 送り火 stands on the rails, hand open, waiting. A woman's soul-fire arrives — 幸恵, earth-colored. Inside the fire, faintly, her death surfaces: a weary traveler, feet that kept walking, a dry throat, a place never reached. He sees — only sees.

## Beginning

The hand opens to wait. That is his morning. 幸恵's earth-colored soul-fire slides in along the rail and stops before him, like a fire that has lost its way.

## Turn

Within the fire, the death surfaces as a translucent apparition — a weary traveler, earth-toned, half-dissolved: feet that kept walking, a dry throat, a place never reached. 送り火 sees them. He does not act; this is the part before the organ moves — the seeing that precedes the sending.

## Peak

The fire holds still before his open hand. The traveler's edges waver between blue and red, then melt back into the flame — and the fire is only a fire again, waiting. He looks, and what he has seen does not leave his face. It has nowhere to go.

## Pull（引き — 切れ目）

Cut on the earth-colored fire, still, before his open hand. He will send it next — but not yet. (The 定型句 does not appear here — it comes at Clip 3.)

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The seeing of the inner life holds the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「待つ」 — ESTABLISH.** 送り火 stands on the rails, hand open, waiting. 幸恵's earth-colored soul-fire slides in along the rail and stops before him. _Density: SPARSE — a long held waiting, almost no event._
- **BEAT 2 `[0:07–0:19]` — 「火の中の一生」 — CORE, longest share.** Within the fire, a translucent weary traveler surfaces — feet that kept walking, a dry throat, a place never reached; earth-toned, half-dissolved, the edges wavering between blue and red. 送り火 sees — only sees. _Density: HELD — the death made faintly visible, then it dissolves._
- **BEAT 3 `[0:19–0:30]` — 「止まる」.** The fire holds still before his open hand; the traveler melts back into the flame; the fire is only a fire again, waiting. Cut on the earth-colored fire. _Density: HELD — the stillness after the seeing._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the seeing of the inner life (0:07–0:19) ／ the fire coming to rest before him (≈0:06) ／ the traveler dissolving (≈0:20)`

## Temporal Density

- Sparse regions: `0:00–0:07 (waiting)`
- Dense regions: `0:07–0:19 (the death surfacing inside the fire)`
- Long continuous action: `0:19–0:30 the fire holding still, the traveler melting away`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_WAIT

- ID: `ACT_WAIT`
- Subject: `OKURIBI (送り火)`
- Action: `Stands on the rails, hand open, waiting; 幸恵's earth-colored fire slides in and stops`
- Intention: `Waiting and sending — the whole of his day`
- Intensity: `Low`
- Speed: `Still, then a slow arrival`

### Action Relationship

- Before: `—`
- After: `ACT_SEE`

## Action — ACT_SEE

- ID: `ACT_SEE`
- Subject: `OKURIBI (送り火)`
- Action: `Sees the death inside the fire — the weary traveler, the feet that walked, the dry throat, the place never reached`
- Intention: `Not to act — to see. The part of the ritual that precedes the organ`
- Intensity: `Low, held`
- Speed: `Still; the seeing is a gaze, not a motion`

### Action Relationship

- Before: `ACT_WAIT`
- After: `ACT_REST`

## Action — ACT_REST

- ID: `ACT_REST`
- Subject: `SACHI (幸恵's soul-fire)`
- Action: `Holds still before his open hand; the traveler dissolves back into the flame; the fire is only a fire again`
- Intention: `Waiting to be sent — no resistance, no fear`
- Intensity: `Low, a held stillness`
- Speed: `Still; the dissolving is slow, the edges wavering`

### Action Relationship

- Before: `ACT_SEE`
- After: `— (cut on the fire's stillness)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not inside his first person`
- Lens Character: `Fire-level and intimate; the fire and its inner vision are the subject, the face secondary`
- Depth of Field: `Shallow — the fire and the traveler within it are sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with the fire; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:07]`** — Wide to medium: 送り火 on the rails, hand open, the earth-colored fire gliding in along the rail toward him.
- **`[0:07–0:19]`** — Close on the fire: within it the translucent traveler surfaces — feet, dry throat, the place never reached — the camera holding on the vision, not the face.
- **`[0:19–0:30]`** — The fire holds still before his hand; the traveler melts back into the flame. Hold on the earth-colored fire. Cut.

---

# 11. MOTION

## Subject Motion

- 送り火 holds almost still; only his open hand waits.
- 幸恵's fire slides in weightlessly along the rail and comes to rest before him.
- The traveler's apparition surfaces and dissolves — a slow waver, not a movement; the edges flicker between blue and red.

## Object Motion

- The barrier stays raised and still; nothing is stirred.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.

## Physical Characteristics

- Weight: `The fire has no weight; the apparition has none either — it is a seen thing, not a body`
- Inertia: `High for the body and the world; near-zero for the fire (instant, gliding)`
- Acceleration: `Gentle everywhere; the dissolving is slow, not a snap`
- Fluidity: `Limited-animation — holds punctuated by small precise gestures`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Stillness (waiting, as always)
- ↓ The seeing (a death surfacing inside the fire)
- ↓ The dissolving (the fire is only a fire again)
- ↓ The unspoken (what he saw has nowhere to go)

## Emotional Events

- Event: `The traveler surfaces inside the fire` — Emotion: `The death made faintly visible — not sorrow, but a held seeing` — Intensity: `LOW, entirely internal` — Timing: `≈0:10`
- Event: `The traveler dissolves back into the flame` — Emotion: `The fire is only a fire again — the seeing has passed, nothing is concluded` — Intensity: `LOW, a held stillness` — Timing: `≈0:22`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `幸恵's soul-fire — pale blue-white, the only light and the only bright value, riding an earth-color`
- Fill Light: `Almost none. Deep indigo shadow fills everything the fire does not reach`
- Rim Light: `A very faint cool edge on the hand and coat from the fire's spill`
- Ambient Light: `Near-black indigo and rust red`
- Color Temperature: `Cold blue-white against deep indigo and rust red, with the earth-color in the fire`

## Lighting Events

- **`[0:00]`** — 送り火 under the damp dark, the earth-colored fire the only light, coming in along the rail.
- **`[0:07–0:19]`** — The fire brightens a little as the traveler surfaces within it; the earth-color and the blue-red waver.
- **`[0:19–0:30]`** — The traveler melts away; the fire settles to a steady earth-tinted glow before his hand. Hold. Cut.

---

# 14. AUDIO

## Dialogue

> **The boundary's voice** (境の地の声): `旅路で斃れた女——幸恵、という` — the narration speaks the name and the death, since the fire's script is unreadable. The 定型句 does not appear (it comes at Clip 3). 送り火 does not speak.

## Sound Effects

- Almost none — the damp near-silence of a place where time does not flow.

## Environment

- The damp near-silence; every sound far away; no footsteps, no breath, no rail, no wind.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender without sentiment. Never sinister`
- Emotional Function: `Hold the stillness under the seeing; it may thin toward the close`

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

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the fire and the seeing.

## Sound Continuity

- **The sound law** — no sound except the dry rustle of the registry's page (which does not turn in this clip).

---

# 16. CONSTRAINTS

## MUST

- Show the fire's inner life — the translucent weary traveler — as a **seen thing, not a solid figure**: half-transparent, earth-toned, the edges wavering, melting into the flame.
- Keep the soul-fire the sole light source.
- End on the fire holding still before his open hand; cut on the fire.
- Keep 送り火's face, hair, build, coat and namelessness exactly as the attached character sheet.

## MUST NOT（この1本の禁止・開示台帳 01 レンジより）

- **No 花** — no schoolgirl, no sailor uniform, no long dark indigo hair, no quiet steady gaze of a girl, no second figure that resembles 花. (幸恵's apparition is a weary traveler, earth-toned, translucent — never a schoolgirl, never resembling 花.)
- **No glowing object in the throat, no flame inside the throat, no inner light in the throat.** The 留まり is not shown here.
- No solid human body inside the fire — the traveler is a half-dissolved apparition, not a standing person; the fire is not a person.
- No on-screen text (the ledger is not opened in this clip).

## PREFER

- Silence over score.
- The fire as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the exact hue of the earth-color, the fire's waver, the traveler's degree of transparency.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 花 is absent: no schoolgirl, no sailor uniform, no long dark indigo hair, no second figure resembling her. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take; it follows the attached character sheet.
3. **The guest's translucency** — the traveler is a half-dissolved seen thing, never a solid body; the fire remains a fire.
4. **The throat restraint** — no glow, no flame, no inner light in the throat.
5. **The uneven density** — the seeing of the inner life must hold the largest share.
6. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
7. **The style** — flat cel planes, soft light, limited animation.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl anywhere. Beats, deliberately uneven: [0:00–0:07] 送り火 stands on the rails, hand open, waiting, as an earth-colored soul-fire — 幸恵 — slides in along the rail and stops before him; [0:07–0:19] within the fire, faintly, a translucent weary traveler surfaces — feet that kept walking, a dry throat, a place never reached — earth-toned, half-dissolved, the edges wavering between blue and red, and 送り火 sees, only sees; [0:19–0:30] the fire holds still before his open hand, the traveler melts back into the flame, and the fire is only a fire again, waiting. Cut on the earth-colored fire. The seeing holds the largest share. (The pull — この魂は、まだ誰にも名付けられていない。 — does not appear in this clip.)

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl, no sailor uniform, no long dark indigo hair, no second figure resembling a girl. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The soul-fire is earth-colored, pale blue-white, not human-shaped, the only light and the only bright value. Within the fire, faintly, the guest's death is a translucent apparition — a weary traveler, earth-toned, half-dissolved, the edges wavering, melting into the flame: feet that kept walking, a dry throat, a place never reached. Not a solid figure, not a standing person. No glowing object in the throat, no flame inside the throat, no inner light in the throat. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the fire and the seeing; the body holds still. The fire slides in weightlessly and comes to rest. The traveler surfaces and dissolves — a slow waver, not a movement; the edges flicker between blue and red. No wind, no dust, no particles, the faintest haze in the damp air; the barrier stays raised and still. The fire has no weight. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Fire-level and intimate; the fire and its inner vision are the subject, the face secondary. Shallow depth of field; the fire and the traveler within it are sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:07] wide to medium, 送り火 on the rails, hand open, the earth-colored fire gliding in. [0:07–0:19] close on the fire, the translucent traveler surfacing within it, the camera holding on the vision. [0:19–0:30] the traveler melts away, the fire settles before his hand; hold, then cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. The boundary's voice speaks the name once, near and far: 旅路で斃れた女——幸恵、という. No other dialogue, no 定型句 here. All sound far away, no footsteps, no breath, no rail, no wind. Music extremely sparse — a few sustained tones at most — thinning toward the close. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no schoolgirl, no sailor uniform, no long dark indigo hair, no second figure resembling a girl, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no solid human body inside the fire, no standing person inside the fire, no readable text, no Japanese kanji or kana, no real-world alphabet, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch01-seg01-30s-01`
- Segment ID: `01-1`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_01, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 7s / 12s / 11s. The seeing = BEAT 2 at 12s (40%)`
- Camera Events: `3 events as listed in §10. All third-person-limited holds`
- Action Events: `ACT_WAIT → ACT_SEE → ACT_REST`
- Audio Events: `near-silence ／ no dialogue`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the fire's stillness`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The traveler may render as a solid ghost.** It must be a half-dissolved seen thing, not a body. If it reads as a standing person, raise transparency and dissolve it further into the fire.
- **The fire may read as a person-shaped flame.** The fire is the body; the apparition is inside it. Verify the fire is not human-shaped.
- **A schoolgirl may be added.** The negative front-loads `no schoolgirl`; verify frame by frame.
- **The throat may glow.** Must be absent — no light, no flame in the throat.

## Changes

- _(none yet)_

## Next Generation

- If the seeing reads, 01-2 continues with the hand — the sending, and the question that comes back.
