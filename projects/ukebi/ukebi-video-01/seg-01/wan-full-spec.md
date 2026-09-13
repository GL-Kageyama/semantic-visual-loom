# Wan 3.0 Full Specification — 受け火 第1章 S03「手が止まる」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../ukebi-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・幸恵）・定型句のみ日本語。
> この1本の個性：**手＝送る（淀みない→止まる）＋幸恵の土色の魂火と戻る問い＋花の不在＋三人称制限＋定型句（指示先は幸恵）**。

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
- No mark on his forehead (the seal appears only from S08).

### Behavior

- Personality: `Does not name; quiet. Does not name emotion. Has nothing that could be called an answer`
- Typical Motion: `Only the eight-organ ritual moves; everything else is near-still`
- Emotional Range: `Suppressed. No readable emotion on the face. Response appears as stillness — a hand that stops, a throat that will not move`

### Continuity Requirements

- Must preserve: `face, hair, build, age, the dark-indigo coat, and the namelessness (nothing about him draws the eye)`

## 幸恵 (SACHI)

- ID: `SACHI`
- Name: `幸恵`
- Type: `SUBJECT (a soul of the dead)`
- Role: `The guest soul to be sent — a woman who walked until she fell by the roadside`

### Appearance

- A pale blue-white fire, **not human-shaped**, earth-colored — the color of a long road walked.
- Inside the fire: feet that kept walking, a dry throat, a place never reached.
- Pale blue-white yet red at once, wavering between blue and red. Weightless; warmth stays on the palm that scoops it.

### Behavior

- Slides in along the rail "like a fire that has lost its way" — it arrives to be sent, not to be seen.
- After it is gone, its voice returns: 「あなたは、誰に送られるの」 — the first question 送り火 has ever been asked.

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

## 魂火 (TAMABI) — 幸恵's fire

- Type: `light / soul`
- Appearance: `a pale blue-white fire, earth-colored, not human-shaped, wavering between blue and red`
- Function: `the sole light source; inside it is a whole life — feet that kept walking, a dry throat, a place never reached`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
- Continuity Importance: `CRITICAL`

## 台帳 (the ledger)

- Type: `book`
- Appearance: `dry white paper, ink characters; one line bears the name 幸恵`
- Material: `paper`
- Function: `binds the names; the name 幸恵 is written with the one close sound`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
- Continuity Importance: `HIGH`

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
- Source: `soul-voice-teller/examples/ukebi/草稿/draft_01_送る.md`
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

A man whose whole day is one of waiting and sending — his hand opens to wait, scoops the soul-fire, raises it, and sends it down the flow. Then a voice comes back, and the hand that only ever sent stops at the back of the throat.

## Beginning

The crossing has no morning, only the hour work begins. 送り火 stands on the rails, hand open, waiting. A woman's soul-fire arrives — 幸恵, earth-colored; a soul that walked until it fell by the roadside, now a pale blue-white fire sliding along the rail, like a fire that has lost its way.

## Turn

Inside the fire: feet that kept walking, a dry throat, a place never reached. 送り火 sees them, and then sends. He moves his hand — the first of the eight organs. The hand takes the fire, raises it, sends it down the flow. The fire brightens a little; it has no weight, yet warmth stays on the palm. The name 幸恵 is written in a single line of the ledger; the fire flows down the rail, and beyond the rails brightens a little.

## Peak

「あなたは、誰に送られるの」— the woman's fire raises a voice. The fire is already gone from the palm, yet the voice comes back, laying a question on his hand. He does not answer. He has never been asked. He has a hand that scoops, and no hand that has ever been scooped.

## Pull（引き — 切れ目）

The hand, without thought, touches the back of the throat. The hand stops. Cut on the stopped hand. The 定型句: この魂は、まだ誰にも名付けられていない。

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The stopping holds 11s (37%) to fix the halted hand.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:08]` — 「待つ」 — ESTABLISH.** 送り火 stands on the rails, hand open, waiting. 幸恵's earth-colored soul-fire slides in along the rail and stops before him. _Density: SPARSE — a long held waiting, almost no event._
- **BEAT 2 `[0:08–0:15]` — 「送る」.** The hand takes the fire, raises it, sends it down the flow. The fire brightens a little; warmth stays on the palm. The name 幸恵 is written in one line of the ledger; the fire flows away, beyond brightens. _Density: TRANSITION — the ritual, unhesitating._
- **BEAT 3 `[0:15–0:19]` — 「問い」.** 「あなたは、誰に送られるの」 — the fire's voice returns, laying a question on his palm. He does not answer. He has never been asked. _Density: DENSE — the voice comes back against the flow._
- **BEAT 4 `[0:19–0:30]` — 「止まる」 — CORE, longest share.** The hand, without thought, touches the back of the throat. The hand stops. Only the fire's warmth remains on the palm. The 定型句. _Density: HELD — the stop, then the whisper, then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the hand stopping (0:19–0:30) ／ the returned question (≈0:17) ／ the name 幸恵 recorded (≈0:13)`

## Temporal Density

- Sparse regions: `0:00–0:08 (waiting), 0:19–0:30 (the stop)`
- Dense regions: `0:15–0:19 (the returned question)`
- Long continuous action: `0:19–0:30 the hand, touching the throat, then still`
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
- After: `ACT_SEND`

## Action — ACT_SEND

- ID: `ACT_SEND`
- Subject: `OKURIBI (送り火)`
- Action: `The hand scoops the fire, raises it, sends it down the flow; the name 幸恵 is written in the ledger`
- Intention: `The ritual — unhesitating, practiced, chosen without thought`
- Intensity: `Low, unvarying`
- Speed: `Steady, practiced, each gesture distinct`

### Action Relationship

- Before: `ACT_WAIT`
- After: `ACT_QUESTION`

## Action — ACT_QUESTION

- ID: `ACT_QUESTION`
- Subject: `SACHI (幸恵's soul-fire)`
- Action: `「あなたは、誰に送られるの」 — the already-departed fire lays a question on his palm`
- Intention: `Not to accuse — to ask. The first question he has ever been asked`
- Intensity: `Medium, quiet`
- Speed: `A voice, near and far, arriving after the fire is gone`

### Action Relationship

- Before: `ACT_SEND`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `OKURIBI (送り火)`
- Action: `The hand, without thought, touches the back of the throat — and stops`
- Intention: `None. The stop is not chosen; the hand that only sent now knows being grasped`
- Intensity: `Low, a held stillness`
- Speed: `Slow rise, then a complete halt`

### Action Relationship

- Before: `ACT_QUESTION`
- After: `— (cut on the stopped hand)`

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

- **`[0:00–0:08]`** — Wide to medium: 送り火 standing on the rails, hand open, the earth-colored fire gliding in along the rail toward him.
- **`[0:08–0:15]`** — Close on the hand: scoop, raise, send. A brief tilt to the ledger as the name 幸恵 is written in one line. The fire flows away.
- **`[0:15–0:19]`** — Close on the open palm, empty now. The voice returns to it — the camera holds on the hand, not the face.
- **`[0:19–0:30]`** — The hand rises slowly to the back of the throat and stops there. Hold on the stopped hand. Cut.

---

# 11. MOTION

## Subject Motion

- The hand carries essentially all the movement; the rest of the body holds.
- Scoop, raise, send — practiced, unhurried, without hesitation.
- The stop is a slow rise, then a complete halt; the fingers do not close, they only stop.
- 幸恵's fire slides in weightlessly and is sent down the flow without resistance.

## Object Motion

- The ledger page turns with a single dry rustle as the name 幸恵 is written.
- The fire brightens a little as it is taken, then flows away down the rail.
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

- Stillness (waiting, as always)
- ↓ Routine (scoop, raise, send — the unhesitating ritual)
- ↓ Unasked (a question laid on the palm, with no answer in him)
- ↓ The stop (a hand that only sent, now touching the throat)

## Emotional Events

- Event: `The name 幸恵 recorded` — Emotion: `Routine without ceremony — one more name in the ledger` — Intensity: `LOW` — Timing: `≈0:13`
- Event: `「あなたは、誰に送られるの」` — Emotion: `Unasked — he has no answer; he has never been asked` — Intensity: `MEDIUM, entirely internal, in the open palm` — Timing: `≈0:17`
- Event: `The hand stops at the throat` — Emotion: `The stop — the hand that only sent now knows being grasped (the 定型句's reference here leans toward 幸恵's soul)` — Intensity: `LOW, a held stillness` — Timing: `≈0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `幸恵's soul-fire — pale blue-white, the only light and the only bright value`
- Fill Light: `Almost none. Deep indigo shadow fills everything the fire does not reach`
- Rim Light: `A very faint cool edge on the hand and coat from the fire's spill`
- Ambient Light: `Near-black indigo and rust red; the rails glow faintly as the fire departs`
- Color Temperature: `Cold blue-white against deep indigo and rust red, with the earth-color in the fire`

## Lighting Events

- **`[0:00]`** — 送り火 under the damp dark, the earth-colored fire the only light, coming in along the rail.
- **`[0:08–0:15]`** — The fire brightens a little as the hand takes it; the ledger's page catches the light for the name 幸恵.
- **`[0:15–0:19]`** — The palm is empty and dim; only the warmth's faint glow remains.
- **`[0:19–0:30]`** — The hand rises into shadow at the throat. Hold. Cut.

---

# 14. AUDIO

## Dialogue

> **The fire's voice** (幸恵's soul-fire): `あなたは、誰に送られるの` — Japanese, character-for-character, near and far, a voice that comes back after the fire is gone. **The 定型句** (境の地の声, near-and-far whisper): `この魂は、まだ誰にも名付けられていない。` as the pull. 送り火 does not speak — he has no answer.

## Sound Effects

- A single dry rustle of the ledger page (かさり) as the name 幸恵 is written — the one close sound.
- All else is far: no footsteps, no breath, no rail, no wind.

## Environment

- The damp near-silence of a place where time does not flow — a silence in which the page's rustle and the returned voice are the only events.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender without sentiment. Never sinister`
- Emotional Function: `Hold the stillness under the ritual; it may thin toward the close, leaving only the whisper and the rustle`

---

# 15. CONTINUITY

> 12本は12回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

## Identity（must remain consistent）

- 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. No mark on his forehead.
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

> 共通不変部の MUST/MUST NOT は series-constants §16 相当。ここには**この1本に固有**の制約のみ。

## MUST

- Establish the hand's ritual — scoop, raise, send — practiced and unhesitating, before the stop.
- Render the on-screen Japanese exactly: the ledger's one line `幸恵` (character-for-character).
- Keep the soul-fire the sole light source.
- End on the hand stopping at the throat, cut on the stopped hand.

## MUST NOT（この1本の禁止・開示台帳 01–04 レンジより）

- **No 花 — no girl, no schoolgirl, no sailor uniform, no long dark hair, no second person, no female figure, no silhouette of another person, no reflection of a girl.**
- No human form in the fire — 幸恵 is earth-colored fire, not a woman's figure.
- No on-screen text other than the ledger line `幸恵`.

## PREFER

- Silence over score.
- The hand as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the ledger's binding, the exact hue of the earth-color, the fire's waver.
- The faint rustle of the page may be near-inaudible.

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: 花 is absent — no girl, no silhouette, no reflection, no second figure. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take.
3. **The exact Japanese** — the on-screen ledger line `幸恵` and the dialogue are evidence; unreadable or altered, the work fails.
4. **The uneven density** — the hand's stop (the take's spine) must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a nameless man whose hand sends the dead down the flow. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No girl anywhere. Beats, deliberately uneven: [0:00–0:08] 送り火 stands on the rails, hand open, waiting, as an earth-colored soul-fire — 幸恵 — slides in along the rail and stops before him; [0:08–0:15] the hand takes the fire, raises it, sends it down the flow, and the name 幸恵 is written in one line of the ledger; [0:15–0:19] the fire is already gone, yet a voice returns to the empty palm — あなたは、誰に送られるの — and he does not answer; [0:19–0:30] the hand, without thought, touches the back of the throat and stops, and the pull whispers この魂は、まだ誰にも名付けられていない。 Cut on the stopped hand. The stop holds the largest share of the duration. Ends on the 定型句.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No girl, no schoolgirl, no sailor uniform, no long dark hair, no second figure, no female figure, no silhouette of another person, no reflection of a girl. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The soul-fire is earth-colored, pale blue-white, not human-shaped, the only light and the only bright value; everything else is deep indigo and rust red. A dry ledger whose page bears one line of Japanese in ink: 幸恵. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the hand and the fire; the body holds still. The hand scoops, raises, and sends the fire down the flow in one practiced, unhurried gesture, without hesitation; the fire brightens a little and flows away without resistance. Then the hand rises slowly to the back of the throat and stops completely — the only abrupt thing is stillness, not a snap. The ledger page turns with a single dry rustle as 幸恵 is written. No wind, no dust, no particles, the faintest haze in the damp air; the barrier stays raised and still. The fire has no weight, only warmth on the palm. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Hand-level and intimate; the hand is the subject, the face secondary. Shallow depth of field; the hand, the fire, and the ledger line are sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:08] wide to medium, 送り火 standing on the rails, hand open, the earth-colored fire gliding in. [0:08–0:15] close on the hand — scoop, raise, send; a brief tilt to the ledger as 幸恵 is written. [0:15–0:19] close on the empty palm; the voice returns to it, the camera holding on the hand, not the face. [0:19–0:30] the hand rises slowly to the throat and stops; hold on the stopped hand; cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. A single dry rustle of the ledger page as 幸恵 is written, the one close sound; all else far away, no footsteps, no breath, no wind. A voice — 幸恵's soul-fire, near and far, returning after the fire is gone: あなたは、誰に送られるの。 送り火 does not speak. Then the pull, the 定型句 in the boundary's own whisper: この魂は、まだ誰にも名付けられていない。 Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only the whisper and the rustle. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no girl, no schoolgirl, no sailor uniform, no long dark hair, no second person, no female figure, no silhouette of another person, no reflection of a girl, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-ch01-seg01-30s-01`
- Segment ID: `S03`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_01, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 8s / 7s / 4s / 11s. The stop = BEAT 4 at 11s (37%)`
- Camera Events: `4 events as listed in §10. All third-person-limited holds and a tilt`
- Action Events: `ACT_WAIT → ACT_SEND → ACT_QUESTION → ACT_STOP`
- Audio Events: `幸恵's voice ／ ledger rustle ／ 定型句 (境の地の声) ／ near-silence`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the stopped hand`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The stop may read as a flinch.** It must be a complete, unhurried halt — a slow rise, then stillness. If it reads as a twitch, slow the rise.
- **The ledger line 幸恵 may render as noise.** It is evidence — character-for-character. If unusable, tighten the shot on the page; the name must read.
- **Identity drift.** 送り火's face may shift across the take. §15 is the defense.
- **The model may add a figure.** The negative prompt front-loads `no girl, no second person`; verify frame by frame.

## Changes

- _(none yet)_

## Next Generation

- If the stop reads, S04 continues with the fingers — the binding that comes to know "reading".
