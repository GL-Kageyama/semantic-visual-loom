# Wan 3.0 Full Specification — 受け火 第7章 S09「悼まれることを払いのけない」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../ukebi-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・早瀬甚吾）・定型句のみ日本語。
> この1本の個性：**声＝悼む（悼む声が止まる→悼みは声ではない）＋早瀬甚吾の独り死んだ兵の火＋少女の一句「あなたを悼む声がない」＋花の在（額に判・S08以降）＋三人称制限＋定型句（指示先が悼む者自身へ傾きはじめる）**。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold one chapter (one organ, one reversal) of an 11-chapter short-story cycle into a single 30-second take that ends on its pull`
- Register: `Restrained and spare. Emotion is never named — it surfaces through the body (a hand stopping, a throat that will not swallow, a scale that will not tilt). The horror and the tenderness both live in ordinary objects and withheld action`
- Rule: `One organ = one turn. The arc is distributed across 12 takes; nothing is added after the pull`

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

- **The fundamental law** — all sending is preceded by being received. 送り火 only sends, and has never himself been received.
- **Eight organs = eight verbs.** One soul is processed by one organ with one verb. No organ hesitates; no motion doubts.
- **The supernatural is never performed, only recorded.** Its evidence is the world's own objects — the ledger, the scale, the seal — and the pale blue-white soul-fire. Nothing else.
- **The soul-fire is the sole light source.** The physical world does not react — no wind, no moving shadows, nothing stirred. All sound is distant except the dry rustle of the ledger's page.
- **Fragments of the living world (the Bon festival, summer) are only hinted at, never drawn in.**

## Visual Language

- Art Direction: `Soft cel anime — flat color planes, clean closed thin lineart, soft-edged shadow terminators`
- Color Language: `Muted, low-saturation. The world is deep indigo and rust red. The soul-fire's pale blue-white is the only bright value — and the only light source. The fire is pale blue-white yet reads red, wavering between blue and red`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces. Things read damp though dry — the rust's red, the air`
- Rendering: `Two-step cel shading with softened terminators; faint haze in the damp air; the soul-fire glows without bloom or lens flare`
- Visual Density: `Low. One focal point per beat. Generous negative space. Nothing is crowded`

---

# 3. SUBJECTS

## 送り火 (OKURIBI)

- ID: `OKURIBI`
- Name: `送り火 (nameless)`
- Type: `CHARACTER`
- Role: `Protagonist — lord of the boundary; an apparatus that sends souls to the next world through eight organs`

### Appearance

- A plain, unremarkable man, neither young nor old — nothing about him draws the eye. Namelessness itself is his appearance.
- Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat.
- Open scooping hands — hands made to scoop, that have never been scooped.
- A faint pale square seal on his forehead reading 該当なし (S08 onward).

### Behavior

- Personality: `Does not name; quiet. Does not name emotion. Has nothing that could be called an answer`
- Typical Motion: `Only the eight-organ ritual moves; everything else is near-still`
- Emotional Range: `Suppressed. No readable emotion on the face. Response appears as stillness — a hand that stops, a throat that will not move`

### Continuity Requirements

- Must preserve: `face, hair, build, age, the dark-indigo coat, the namelessness, and the faint pale square seal on the forehead`

## 早瀬甚吾 (JINGO)

- ID: `JINGO`
- Name: `早瀬甚吾`
- Type: `SUBJECT (a soul of the dead)`
- Role: `The guest soul to be sent — a soldier who died alone`

### Appearance

- A pale blue-white fire, **not human-shaped**, steady, without flicker or drift — it carries the weight of a corpse nobody saw off.
- Inside the fire: letters no one read, a final voice no one heard, the night he died alone.
- Pale blue-white yet red at once; it settles before him, heavy, though it has no mass.

### Behavior

- It settles before him, heavy, and does not move. It has no face, no shape, no voice — only the weight of an unwitnessed death.

## 花 (HANA)

- ID: `HANA`
- Name: `少女 (the girl — nameless; she has no name yet)`
- Type: `CHARACTER`
- Role: `The soul without a price — present, watching from the dark indigo`

### Appearance

- A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet, though no rain falls on her.
- Long dark indigo hair; a quiet, steady gaze. At the crossing, no one had ever looked at 送り火 — only she looks at him.
- She does **not** resemble 送り火 — no copy, no reflection, no suggestion they are the same person.

### Behavior

- Watches from the deep indigo behind him, still. Then she speaks, quiet and level: あなたを悼む声がない。

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter

> The 台帳 (registry) is absent in this chapter — no page turns, no mark. The 秤 (scale) is absent too. The 判 (seal) is not an object here — it is already on 送り火's forehead (S08+).

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `total stillness — 境 has no sound at all; no wind, no rain, no breathing`

---

# 5. OBJECTS

## 魂火 (TAMABI) — 早瀬甚吾's fire

- Type: `light / soul`
- Appearance: `a pale blue-white fire, not human-shaped, steady; it carries the weight of a corpse nobody saw off, though it has no mass`
- Function: `the sole light source; inside it is a life — letters no one read, a final voice no one heard, the night he died alone`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
- Continuity Importance: `CRITICAL`

> The 台帳 (registry) is absent in this chapter. The 判 (seal) is already on 送り火's forehead (S08+).

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
- Source: `soul-voice-teller/examples/ukebi/草稿/draft_07_悼む.md`
- Priority: `CRITICAL`
- Defines: `every event, the exact on-screen text, the ending line, and what is and is not revealed`

## REF_BIBLE

- Type: `BIBLE`
- Source: `soul-voice-teller/examples/ukebi/台帳/series-bible.md`
- Priority: `CRITICAL`
- Defines: `the staged disclosure, the voice rules, and the organ ledger`

---

# 7. NARRATIVE

## Core Event

A soldier's soul-fire — the weight of a corpse nobody saw off — arrives. 送り火 moves the seventh organ, his voice, and mourns: a low voice carries the name 早瀬甚吾. The girl speaks: あなたを悼む声がない. The voice stops. For the first time he does not brush away being mourned.

## Beginning

The fire arrives and settles before him, heavy. He sees into it: letters no one read, a final voice no one heard, the night he died alone. The name 早瀬甚吾 sits in the fire.

## Turn

He mourns — the low voice, the seventh organ, carries the name. It has always ended there. Then the girl, watching, says: あなたを悼む声がない。

## Peak

The voice stops. Mourning was not a voice — it was something heavy, placed somewhere in the chest. He was mourned. And, for the first time, he did not brush it away.

## Pull（引き — 切れ目）

The boundary's own voice, near and far, in a whisper: この魂は、まだ誰にも名付けられていない。 Cut. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The stopping of the voice holds 14s (47%) — the organ's stop takes the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「魂火が届く」 — ESTABLISH.** The soldier's fire settles before 送り火 — pale blue-white, but it carries the weight of a corpse nobody saw off. Inside it: letters no one read, a final voice no one heard, the night he died alone. _Density: SPARSE — one heavy fire, almost no event._
- **BEAT 2 `[0:07–0:13]` — 「悼む」.** 送り火 moves his voice. A low voice carries the name: 早瀬甚吾. The dead man's name rides on the voice. Mourning is carrying a name on the voice. It has always ended here. _Density: TRANSITION — the ritual, before the stop._
- **BEAT 3 `[0:13–0:27]` — 「声が、止まる」 — REVEAL, longest share.** The girl speaks: あなたを悼む声がない。 The voice stops. Silence. Mourning was not a voice — it is something heavy, placed somewhere in the chest. He was mourned. For the first time, he does not brush it away. His scooping hands stay open and still. _Density: SPARSE, held — the whole turn is a stillness._
- **BEAT 4 `[0:27–0:30]` — 「払いのけない」.** The boundary's voice, near and far, in a whisper: この魂は、まだ誰にも名付けられていない。 Cut on the whisper. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the low voice carrying the name (≈0:09) ／ the girl's line (≈0:13) ／ the voice stopping (≈0:14–0:27)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the fire), 0:13–0:27 (the voice stopped)`
- Dense regions: `0:07–0:13 (the mourning)`
- Long continuous action: `0:13–0:27 the stopped voice — the longest held stillness`
- Rapid transitions: `none — the slowest, most held segment of the chapter`

---

# 9. ACTION

## Action — ACT_RECEIVE

- ID: `ACT_RECEIVE`
- Subject: `OKURIBI (送り火)`
- Action: `Receives the soldier's fire as it settles before him; sees into it`
- Intention: `To read the death inside the fire — letters, the final voice, the night`
- Intensity: `Low`
- Speed: `Still, held`

### Action Relationship

- Before: `—`
- After: `ACT_MOURN`

## Action — ACT_MOURN

- ID: `ACT_MOURN`
- Subject: `OKURIBI (送り火)`
- Action: `Moves the voice — the seventh organ — and speaks the name in a low voice: 早瀬甚吾`
- Intention: `To mourn — to carry a name on the voice`
- Intensity: `Low, ritual`
- Speed: `Slow, low, practiced`

### Action Relationship

- Before: `ACT_RECEIVE`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `OKURIBI (送り火)`
- Action: `The voice stops. His lips close and still; the name falls silent`
- Intention: `Not chosen — the voice will not go on after the girl's line`
- Intensity: `Medium, entirely still`
- Speed: `A halt — the sound is simply gone`

### Action Relationship

- Before: `ACT_MOURN`
- After: `ACT_NOT_BRUSH`
- Causes: `the girl's line あなたを悼む声がない`

## Action — ACT_NOT_BRUSH

- ID: `ACT_NOT_BRUSH`
- Subject: `OKURIBI (送り火)`
- Action: `Does not brush it away. Something heavy settles on the chest; his scooping hands stay open and still at his sides`
- Intention: `For the first time, to let being mourned stay`
- Intensity: `Low, withheld`
- Speed: `Motionless`

### Action Relationship

- Before: `ACT_STOP`
- After: `— (the whisper, then cut)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, at the level of the fire and the two figures. Inside the stillness with him`
- Lens Character: `Long-ish, shallow. Only the fire or the face is sharp`
- Depth of Field: `Very shallow — the fire glows, the background falls away into indigo`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Behavior

`Static with a slow push-in. No whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:07]`** — Close on the soldier's fire — pale blue-white, heavy, the only bright value. Slowly the frame finds 送り火's face behind it, in the dark, the faint pale square seal on his forehead.
- **`[0:07–0:13]`** — A slight push-in toward his mouth and throat — the low voice carries the name. The girl waits in the deep indigo behind him, still, watching.
- **`[0:13–0:27]`** — On the girl's line the frame holds. The voice stops. His lips close and still. Hold on his face and the stillness of his body, the fire's light steady. No movement at all.
- **`[0:27–0:30]`** — Hold on the stillness. The whisper comes over it. Cut on the dark.

---

# 11. MOTION

## Subject Motion

- Almost all movement belongs to the voice — the faint parting of his lips, the low name.
- When the voice stops, the whole body is still; nothing else moves at all.
- His scooping hands stay open and still at his sides — the only other "motion" is their not moving.
- The girl is still throughout; she only watches.

## Object Motion

- The fire does not move, flicker, or drift. It is a steady pale blue-white, the only bright value.
- Nothing else in the frame moves on its own.

## Environmental Motion

- None. No wind, no moving shadows, no particles — only the faintest haze in the damp air.

## Physical Characteristics

- Weight: `The fire reads heavy — the weight of a corpse nobody saw off — though it has no mass`
- Inertia: `High. The body is still; the voice stops without recoil`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by one small movement (the name), then stillness`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Weight (the fire that carries an un-witnessed death)
- ↓ Ritual (the low voice carrying the name — as it has always done)
- ↓ The stop (the voice gone; mourning is not a voice)
- ↓ Being mourned and not brushing it away (the heaviness stays)

## Emotional Events

- Event: `The low voice carrying the name 早瀬甚吾` — Emotion: `Ritual, practiced — mourning as it has always been` — Intensity: `LOW` — Timing: `≈0:09`
- Event: `The girl's line あなたを悼む声がない` — Emotion: `The question turns toward him — who has been mourned while still alive` — Intensity: `MEDIUM, entirely still` — Timing: `≈0:13`
- Event: `The voice stopping` — Emotion: `Mourning is not a voice — something heavy placed on the chest` — Intensity: `MEDIUM, withheld into stillness` — Timing: `≈0:14–0:27`
- Event: `Not brushing it away` — Emotion: `For the first time, being mourned is allowed to stay` — Intensity: `LOW` — Timing: `≈0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The soldier's soul-fire — pale blue-white, the only light and the only bright value`
- Fill Light: `Almost none. Deep soft indigo fills everything the fire does not reach`
- Rim Light: `A very faint cool edge on 送り火's hair and shoulders from the fire's spill`
- Ambient Light: `Near-black indigo, with the faint rust-red of the rails at the far edge`
- Color Temperature: `Cold blue-white fire against deep indigo and rust red`

## Lighting Events

- **`[0:00]`** — The fire already burning, steady. Its light lies on 送り火's face, the seal on his forehead faint but present.
- **`[0:07–0:13]`** — The fire's light holds steady while the voice speaks.
- **`[0:13–0:27]`** — No change in the light — the fire does not dim or pulse. The stillness is a stillness of light, not of darkness.
- **`[0:27–0:30]`** — Hold. Cut on the deep indigo.

---

# 14. AUDIO

## Dialogue

> 送り火, in a low voice, the seventh organ: `早瀬甚吾`. Then the girl, quiet and level: `あなたを悼む声がない`. These are the organ's voice and the girl's voice — not sound in the air. 境 has no sound.

## Narration

> The boundary's own voice, near and far, a whisper at the pull: `この魂は、まだ誰にも名付けられていない。` The 指示先 hovers — it seems to name the soldier (named, yet unmourned), but after he is mourned it begins to lean, faintly, toward the mourner himself. Still steady — not yet the tremor of S11.

## Sound Effects

- None. No wind, no rain, no footsteps, no breathing — 境 is silent.

## Environment

- Total stillness. The kind of silence in which a voice, when it stops, leaves a weight behind.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, grave, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the stillness under the low voice, then fall away entirely when the voice stops — leaving only the whisper`

---

# 15. CONTINUITY

> 12本は12回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

## Identity（must remain consistent）

- 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. A faint pale square seal on his forehead reading 該当なし (S08+).
- 花 (S05+) — a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though the rain never falls on her. Long dark indigo hair, a quiet steady gaze that watches. She must never resemble 送り火.
- The stage — a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls.

## Visual Continuity

- **The light law** — the soul-fire's pale blue-white is the only light and the only bright value; everything else is deep indigo and rust red.
- **The palette law** — muted, low-saturation everywhere; the pale blue-white soul-fire is the only bright value.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the organ's gesture.

## Sound Continuity

- **The sound law** — total stillness; 境 has no sound at all. Only the two voices and the whisper are heard.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は series-constants（Negative・受け火開示台帳）相当。ここには**この1本に固有**の制約のみ。

## MUST

- Show the soldier's fire as heavy — the weight of a corpse nobody saw off — though it has no mass.
- The voice must read as the seventh organ: the low voice carrying the name 早瀬甚吾.
- Render the girl's line exactly: `あなたを悼む声がない`（spoken, not on screen）。
- Keep 送り火's faint pale square seal `該当なし` on his forehead.
- End on the whisper この魂は、まだ誰にも名付けられていない。 with nothing after it.

## MUST NOT（この1本の禁止・開示台帳 S09 レンジより）

- **Do not reveal 篠宮花's name or identity.** She is 少女 — no name, no "篠宮", no "花".
- **The girl must never resemble 送り火** — no mirror, no reflection, no doubling, no same-person suggestion.
- No on-screen text (S09 の画面文字は「なし」).
- No environmental sound — 境 has no sound (no wind, no rain, no breathing).

## PREFER

- The stopped voice held as long as possible — the whole turn is one held stillness.
- Silence over score at the stop.
- Negative space over detail.

## ALLOW

- Slight variation in the fire's exact shape and the depth of the indigo.
- Music may be absent altogether.

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: 花 remains nameless, no identity (S10 reveals her name and identity). This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take (with the seal); 花 must never resemble 送り火.
3. **The exact Japanese** — the name 早瀬甚吾 and the girl's line あなたを悼む声がない are evidence; unreadable or altered, the work fails.
4. **The uneven density** — the stopped voice (the take's spine) must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing that leads nowhere. A plain unremarkable man — 送り火 — mourns a soul with the seventh organ of his body, his voice. Beats, deliberately uneven: [0:00–0:07] a soldier's soul-fire settles before him, pale blue-white, heavy with the weight of a corpse nobody saw off; [0:07–0:13] his low voice carries the name 早瀬甚吾 — mourning is carrying a name on the voice; [0:13–0:27] THE REVEAL — a girl watching in the dark indigo speaks: あなたを悼む声がない, and the voice stops; mourning is not a voice, it is something heavy placed on the chest, and for the first time he does not brush it away; [0:27–0:30] the boundary's voice, near and far, whispers この魂は、まだ誰にも名付けられていない。, and the shot cuts on the dark. The stopped voice holds the largest share of the duration. Ends on the whisper.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, simple uncluttered stage, generous negative space, one focal point per shot. 送り火: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands, and a faint pale square seal on his forehead reading 該当なし. The girl (少女): a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though the rain never falls on her, long dark indigo hair, a quiet steady gaze that watches — she must never resemble 送り火. The stage: a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls. The light law: the soul-fire's pale blue-white is the only light and the only bright value; everything else is deep indigo and rust red. The fire is a pale blue-white soul-fire, steady, without a human shape. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the voice: the faint parting of his lips as the low name is spoken, then the stop — his lips close and still, and the whole body is motionless. His scooping hands stay open and still at his sides. The girl is still throughout; she only watches. The soul-fire does not move, flicker, or drift. No wind, no moving shadows, no particles, only the faintest haze in the damp air. Gentle acceleration everywhere; nothing snaps or jerks. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, at the level of the fire and the two figures — inside the stillness with him. Longish lens, very shallow depth of field; often only the fire or the face is sharp. Slow, deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] close on the soldier's fire, then slowly find 送り火's face behind it, the seal faint on his forehead. [0:07–0:13] a slight push-in toward his mouth and throat as the low voice carries the name; the girl waits in the deep indigo behind him. [0:13–0:27] on the girl's line, the frame holds; the voice stops, his lips close and still; hold on his face and the stillness of his body, the fire's light steady. [0:27–0:30] hold on the stillness; cut on the dark.

## Audio Prompt

Almost silent — 境 has no sound. 送り火, in a low voice: 早瀬甚吾. Then the girl, quiet and level: あなたを悼む声がない. Then the voice is simply gone. At the pull, the boundary's own voice, near and far, in a whisper: この魂は、まだ誰にも名付けられていない。. No wind, no rain, no footsteps, no breathing, no ambient bed. Music extremely sparse — a few sustained tones at most — falling away entirely when the voice stops, leaving only the whisper. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no girl revealing a name, no "篠宮", no "花" name, no reflection of the girl in the man, no mirror image, no doubling of the two faces, no resemblance between the man and the girl, no on-screen text, no subtitles, no captions, no wind, no rain, no breathing, no environmental sound, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no watermark, no morphing or drifting facial identity, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no narration text, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no moving shadows, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-ch07-seg01-30s-01`
- Segment ID: `S09`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_07_悼む, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 6s / 14s / 3s. Stopped voice = BEAT 3 at 14s (47%)`
- Camera Events: `4 events as listed in §10. No dolly; all static or a slow push-in`
- Action Events: `ACT_RECEIVE → ACT_MOURN → ACT_STOP → ACT_NOT_BRUSH`
- Audio Events: `送り火's low name 早瀬甚吾 ／ the girl's line ／ the whisper (定型句) ／ total silence between`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the dark`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The model may add a face to the soul-fire.** The fire is a fire — no human shape. The negative prompt front-loads this; verify frame by frame.
- **The model may reveal the girl's name or resemblance.** 篠宮花's name and identity are S10. She must not resemble 送り火. This is the most damaging failure.
- **The whisper may render as on-screen text.** The 定型句 is a voice, never subtitled. Verify no caption appears.
- **The stop may read as a cut.** The voice must simply stop — not a loud cut, not a fade. Hold the stillness.

## Changes

- _(none yet)_

## Next Generation

- If the stopped voice reads well, keep the whisper near and far — the tremor (added punctuation) is reserved for S11.
