# Wan 3.0 Full Specification — 受け火 第4章 S06「膝の上」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../ukebi-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火）・定型句のみ日本語。
> この1本の個性：**腕＝預かる（止まる→預かられる・受動のはじまり）＋コダマの伸ばした両手の火と問い＋花の台詞「代わりに、あんたを預からせて」＋花の在（判なし）＋三人称制限＋定型句（指示先はコダマの魂）**。

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

## コダマ (KODAMA)

- ID: `KODAMA`
- Name: `コダマ`
- Type: `SUBJECT (a soul of the dead)`
- Role: `The guest soul to be sent — an orphan no one came to claim`

### Appearance

- A pale blue-white fire, **not human-shaped**, with two hands reaching upward — palms turned upward, waiting to be lifted.
- Inside the fire: nights it was never held, a name it was never called, two hands left reaching.
- Pale blue-white yet red at once, wavering between blue and red. It stops, still, before his chest.

### Behavior

- It waits — its whole death it has waited for arms to come.
- Held for the first time, it speaks a question: あなたは、誰かに預けられたことがあるか。

## 花 (HANA)

- ID: `HANA`
- Name: `少女 (the girl — nameless; she has no name yet)`
- Type: `CHARACTER`
- Role: `The soul seated at 「該当なし」 — present, standing beside 送り火`

### Appearance

- A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet, though no rain falls on her.
- Long dark indigo hair; a quiet, steady gaze.
- She does **not** resemble 送り火 — no copy, no reflection, no suggestion they are the same person.
- No seal appears yet (the seal on 送り火's forehead is S08 onward).

### Behavior

- Stands beside him, watching. Then she speaks, low and sure: 代わりに、あんたを預からせて。
- She lowers the fire from his arms, then lowers the man down onto her lap — a quiet core of strength.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter

> The 台帳 (registry) is absent in this chapter — no page turns, no mark.

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `soundless — no page rustle; the only near sounds are the two voices and the crease of cloth`

---

# 5. OBJECTS

## 魂火 (TAMABI) — コダマ's fire

- Type: `light / soul`
- Appearance: `a pale blue-white fire, not human-shaped, with two hands reaching upward, wavering between blue and red`
- Function: `the sole light source; inside it is a life — nights never held, a name never called, two hands left reaching`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
- Continuity Importance: `CRITICAL`

> The 台帳 (registry) is absent in this chapter.

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
- Source: `soul-voice-teller/examples/ukebi/草稿/draft_04_預かる.md`
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

The girl stands beside him. The soul-fire of an orphan no one came to claim arrives — palms turned upward, waiting to be lifted — and stops, still, before his chest. He takes it into his arms, the fourth organ. Then the fire asks him a question he cannot answer, his arms stop, and the girl lowers him, for the first time, onto her lap — his body taking on weight it has never had.

## Beginning

The girl stands beside the man. The fire of a child no one came for arrives: palms upturned, as if waiting to be held up. Inside the fire are nights it was never held, a name it was never called, and two hands left reaching. It stops, still, before his chest.

## Turn

He moves his arms — the fourth organ. To hold the soul. To keep it in his arms until its next life is decided. The fire that had been still before his chest settles into his arms. It trembles, small — a fire never held, held for the first time. It should have ended there: he has held many souls in these arms. Hold, and send. That was the work of the crossing. Then the fire speaks: あなたは、誰かに預けられたことがあるか。 He does not answer. He has never been held — only ever the one who holds. His arms stop.

## Peak

The girl speaks: 代わりに、あんたを預からせて。 She lowers the orphan's fire gently from his arms. Then she lowers the standing man down onto her lap. The arms that were meant to hold have lost what they held — and are, themselves, held. On her lap, his body takes on weight for the first time.

## Pull（引き — 切れ目）

At the crossing, no one had ever held him; only the girl holds him. The arms that were meant to hold are now the ones being held. Cut on the weight of his body in her lap, and the whisper: この魂は、まだ誰にも名付けられていない。

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The lowering onto her lap holds 11s (37%) — the reversal (being held) carries the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「隣に立つ少女と、コダマの火」 — ESTABLISH.** The girl stands beside the man. The orphan's fire arrives, palms turned upward, and stops before his chest, still. Inside the fire: nights it was never held, a name never called. _Density: SPARSE — one still fire, the girl at his side._
- **BEAT 2 `[0:06–0:12]` — 「腕で預かる」.** His arms move — the fourth organ. The fire settles into his arms and trembles, small: a fire never held, held for the first time. _Density: TRANSITION — the holding, gentle, practiced._
- **BEAT 3 `[0:12–0:19]` — 「預けられたことがあるか」 — TURN.** The fire speaks: あなたは、誰かに預けられたことがあるか。 He does not answer. He has never been held. His arms stop. _Density: HELD — the question, and the arms that freeze._
- **BEAT 4 `[0:19–0:30]` — 「少女の膝の上へ」 — REVERSAL, longest share.** The girl speaks: 代わりに、あんたを預からせて。 She lowers the fire from his arms, then lowers him down onto her lap. His body takes on weight for the first time. Cut on the weight; the whisper of the 定型句. _Density: HELD then a clean cut. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the lowering onto her lap (0:19–0:30) ／ the question あなたは、誰かに預けられたことがあるか (≈0:12) ／ the arms stopping (≈0:16)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the fire and the girl beside him)`
- Dense regions: `0:19–0:30 (the lowering — several small acts in a few seconds: lowering the fire, lowering the man, the weight settling)`
- Long continuous action: `0:19–0:30 the slow lowering of the man onto her lap`
- Rapid transitions: `none — a held, deliberate segment`

---

# 9. ACTION

## Action — ACT_ARRIVE

- ID: `ACT_ARRIVE`
- Subject: `KODAMA (コダマの魂火)`
- Action: `The fire arrives with palms turned upward and stops before his chest`
- Intention: `To be lifted — it has waited its whole death for arms to come`
- Intensity: `Low`
- Speed: `Still. The fire only trembles, small, waiting`

### Action Relationship

- Before: `—`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `OKURIBI (送り火)`
- Action: `His arms move and take the fire into them; the fire settles and trembles`
- Intention: `The fourth organ — to keep the soul until its next life is decided`
- Intensity: `Low, practiced`
- Speed: `Gentle, ritual, unhurried`

### Action Relationship

- Before: `ACT_ARRIVE`
- After: `ACT_ASK`

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `KODAMA (コダマ)`
- Action: `The fire speaks: あなたは、誰かに預けられたことがあるか`
- Intention: `A question the man cannot answer — to ask, not to accuse`
- Intensity: `Low, quiet`
- Speed: `Slow; the words are the fire's only motion`

### Action Relationship

- Before: `ACT_HOLD`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `OKURIBI (送り火)`
- Action: `His arms stop. He does not answer. He has never been held`
- Intention: `None. The organ freezes — he has only ever held, never been held`
- Intensity: `Medium, internal`
- Speed: `A full stop of the arms`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_RECEIVE`

## Action — ACT_RECEIVE

- ID: `ACT_RECEIVE`
- Subject: `HANA (少女)`
- Action: `She lowers the fire from his arms, then lowers him onto her lap`
- Intention: `代わりに、あんたを預からせて — to hold him, since he was never held`
- Intensity: `Low, sure — a quiet core of strength`
- Speed: `Slow, careful; the lowering of the man is deliberate and gentle`

### Action Relationship

- Before: `ACT_STOP`
- After: `— (cut on the weight in her lap)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, at the height of his chest, then lowering with him to her lap. Watchful, not intimate`
- Lens Character: `Medium. The crossing reads as one sparse plane behind the two figures`
- Depth of Field: `Shallow — the fire and the hands are sharp; the girl and the rail fall softly`
- Camera Style: `Slow, deliberate, nearly still. It drifts and lowers; it never whips or shakes`

## Camera Behavior

`Static with slow drift and a slow lowering. No whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:06]`** — Medium close: the girl standing beside the man, the fire arriving before his chest, palms up. Static, watchful.
- **`[0:06–0:12]`** — Close on his arms as they take the fire in; the fire's pale light on his hands. The girl, soft in the background, watching.
- **`[0:12–0:19]`** — Close on the fire as it speaks, then on his arms freezing. The girl still in frame, just behind.
- **`[0:19–0:30]`** — The camera lowers with the man as the girl lowers him — the frame dropping from his height to her lap. Hold on his body settled in her lap, the weight reading in the fold of the skirt, the slack of his arms. Cut.

---

# 11. MOTION

## Subject Motion

- The fire's only motion is a small tremble — first when it settles into his arms, again when she lowers it.
- The man's arms move once, then freeze; afterward his body is lowered, limp, into her lap — the slack arms fall open.
- The girl moves with slow certainty: she lowers the fire, then the man. Every motion is deliberate and sure.

## Object Motion

- Nothing else in the crossing moves. The barrier stays raised; the rails do not stir.
- The registry is not present in this chapter — no page turns, no mark.

## Environmental Motion

- None. The air is damp but still; no wind, no particles beyond the faintest haze.

## Physical Characteristics

- Weight: `The pivotal physics. The fire is weightless; the man, for the first time, has weight. His body sinks into the girl's lap, the skirt creases under him, the slack arms hang with real heaviness`
- Inertia: `High for the man — once his arms freeze, the whole body follows into stillness; the lowering is one slow, heavy descent`
- Acceleration: `Gentle everywhere; the lowering is a slow settle, not a drop`
- Fluidity: `Limited-animation — holds punctuated by small precise movements (the tremble, the freeze, the slow descent)`
- Impact: `None, but the one weighted contact — his body settling onto her lap — must read as the first time his body has had mass`

---

# 12. EMOTION

## Emotional Arc

- Waiting (a fire with palms upturned, a girl standing beside him)
- ↓ The practiced holding (the fourth organ, gentle)
- ↓ The unanswerable question (the arms that freeze)
- ↓ Being held (lowered onto her lap — his body takes on weight)

## Emotional Events

- Event: `The fire speaks its question` — Emotion: `A held breath — a question with no answer in him` — Intensity: `LOW, quiet` — Timing: `≈0:12`
- Event: `His arms stop` — Emotion: `The halt — he has only ever held, never been held` — Intensity: `MEDIUM, internal` — Timing: `≈0:16`
- Event: `She lowers him onto her lap` — Emotion: `The first weight — being held, neither spoken nor shown on the face` — Intensity: `MEDIUM — carried in the slack arms and the crease of the skirt` — Timing: `≈0:24`
- Event: `The whisper of the 定型句` — Emotion: `A namelessness named, from far away` — Intensity: `LOW — a close, distant whisper` — Timing: `≈0:28`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The soul-fire — pale blue-white, the only light. It lights his chest and hands, then the girl as she lowers him`
- Fill Light: `Almost none. Deep indigo fills everything the fire does not reach`
- Rim Light: `A faint cool edge on the girl's dark hair and on his slack hands`
- Ambient Light: `Deep indigo and rust red; the air is damp and dark`
- Color Temperature: `Cold blue-white fire against deep indigo, rust red at the edges`

## Lighting Events

- **`[0:00]`** — The fire, pale blue-white, is the world's light, held before his chest.
- **`[0:06–0:12]`** — The light climbs his hands as he takes the fire in.
- **`[0:12–0:19]`** — The light is still on his frozen arms and on the fire's small tremble.
- **`[0:19–0:30]`** — As the girl lowers the fire and then the man, the light moves down with them — from his chest to her lap — and settles, faint, on the weight of his body. Cut.

---

# 14. AUDIO

## Dialogue

> **Two spoken lines, then silence.**
> KODAMA（コダマの魂火）: `あなたは、誰かに預けられたことがあるか` — quiet, without accusation, the fire's voice small and clear.
> HANA（少女）: `代わりに、あんたを預からせて` — low, sure, a quiet core of strength.
> 送り火 does not answer. The 定型句 is the boundary's whisper at the pull, not on screen: `この魂は、まだ誰にも名付けられていない。`

## Sound Effects

- The dry rustle of the registry's page — absent here; the chapter has no registry. The crossing is otherwise soundless.
- The faintest soft sound of the fire's tremble as it settles and as it is lowered.
- The soft crease of the girl's skirt as the man's weight settles into her lap — small, close, the one bodily sound.

## Environment

- A damp, soundless crossing. Every sound is far away except the two voices and the small crease of cloth.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the weight of the lowering, then thin to silence as the whisper arrives. The music must not insist on the tenderness — the slack arms carry it`

---

# 15. CONTINUITY

> 12本は12回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

## Identity（must remain consistent）

- 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. No mark on his forehead.
- 花 (S05+) — a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though the rain never falls on her. Long dark indigo hair, a quiet steady gaze that watches. She must never resemble 送り火.
- The stage — a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls.

## Visual Continuity

- **The light law** — the soul-fire's pale blue-white is the only light and the only bright value; everything else is deep indigo and rust red.
- **The palette law** — muted, low-saturation everywhere; the pale blue-white soul-fire is the only bright value.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the organ's gesture.

## Sound Continuity

- **The sound law** — no sound except the two spoken voices and the soft crease of cloth; no registry page in this chapter.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は series-constants（Negative・受け火開示台帳）相当。ここには**この1本に固有**の制約のみ。

## MUST

- Establish the arms' stop and the reversal into being held — the fourth organ freezing, then the man lowered onto the girl's lap.
- Render the two spoken lines exactly: `あなたは、誰かに預けられたことがあるか` ／ `代わりに、あんたを預からせて`（character-for-character）。
- Make the man's body take on weight for the first time — the skirt creases, the slack arms hang with real heaviness.
- Keep the soul-fire the sole light source — pale blue-white against deep indigo and rust red.
- End on the weight of his body in her lap and the 定型句 whisper, cut with nothing after it.

## MUST NOT（この1本の禁止・開示台帳 S06 レンジより）

- **No name, no identity for the girl.** Do not say 篠宮, do not say 花. She has no name yet.
- **No seal on 送り火's forehead** — the seal is S08 onward. His forehead is bare.
- **Do not make the girl resemble 送り火** — no copy, no reflection, no suggestion they are the same person, no matching face, no mirrored pose.
- No on-screen text — this chapter has no registry, no mark, no written word on screen.
- No on-screen subtitles or captions burned in (the two lines are spoken, never written).

## PREFER

- The lowering held as long as possible — the whole turn is one slow, weighted descent.
- Silence over score; the two voices and the crease of cloth are the only sounds.
- Negative space over detail; the crossing may be nearly empty.

## ALLOW

- Slight variation in the girl's skirt length and the fire's exact size.
- The imperceptible settle of the camera may be omitted (a fully locked frame is equally correct).
- Music may be absent altogether.

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: 花 appears but only as 少女 — no name, no identity, no seal. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take; 花 must never resemble 送り火.
3. **The exact Japanese** — the two spoken lines are evidence; unreadable or altered, the work fails.
4. **The uneven density** — the lowering onto her lap (the take's spine) must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Beats, deliberately uneven: [0:00–0:06] a girl stands beside a plain unremarkable man as an orphan's soul-fire arrives, palms upturned, and stops before his chest; [0:06–0:12] his arms move — the fourth organ — and take the fire in; it trembles, small; [0:12–0:19] the fire speaks, あなたは、誰かに預けられたことがあるか, and his arms stop — he has never been held, only ever the one who holds; [0:19–0:30] the girl speaks, 代わりに、あんたを預からせて, lowers the fire from his arms, then lowers the man down onto her lap, and his body takes on weight for the first time. The lowering holds the largest share. Ends on the weight in her lap and a whisper: この魂は、まだ誰にも名付けられていない。

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A railroad crossing: rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls. A plain unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands, bare forehead. A girl, a high-school student in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though no rain falls on her, long dark indigo hair, a quiet steady gaze; she does not resemble the man. The soul-fire is the only light and the only bright value, pale blue-white, its two hands reaching upward. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fire's small tremble, the man's single holding gesture, and the girl's slow lowering. The man's arms move once, then freeze. The girl lowers the fire, then lowers the man — one slow, heavy descent; the skirt creases under him, the slack arms hang with real heaviness, his body settling with weight for the first time. Gentle acceleration everywhere; the lowering is a settle, not a drop. No wind, no moving shadows, no particles beyond the faintest haze. No impacts beyond the one weighted settle. No motion blur smears, no squash and stretch.

## Camera Prompt

Close, at the height of his chest, watchful and nearly still; the camera drifts and lowers and never whips or shakes. [0:00–0:06] medium close, the girl beside him and the fire arriving, static. [0:06–0:12] close on his arms taking the fire in, the girl soft in the background. [0:12–0:19] close on the fire as it speaks, then on his arms freezing. [0:19–0:30] the camera lowers with the man as the girl lowers him, the frame dropping from his height to her lap; hold on his body settled in her lap, the slack arms and the creased skirt; cut.

## Audio Prompt

Almost silent. A damp, soundless crossing; every sound is far away. Two spoken lines: the fire, quiet and clear, あなたは、誰かに預けられたことがあるか; the girl, low and sure, 代わりに、あんたを預からせて. The man does not answer. The faint soft crease of the girl's skirt as his weight settles, close. Music extremely sparse — a few sustained tones at most, thinning to silence. At the pull, a close and distant whisper, the voice of the boundary, neither on-screen nor loud: この魂は、まだ誰にも名付けられていない。 No horror strings, no sting, no swelling emotion.

## Negative Prompt

no resemblance between the girl and the man, no copy of the man, no reflection of the girl, no seal on the forehead, no name written for the girl, no on-screen text, no on-screen subtitles, no captions, no English text, no narration text, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no morphing or drifting facial identity, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges, no watermark

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-ch04-seg01-30s-01`
- Segment ID: `S06`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_04_預かる, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 6s / 7s / 11s. The lowering = BEAT 4 at 11s (37%)`
- Camera Events: `4 events as listed in §10. No sustained dolly; all static, drift, or lowering`
- Action Events: `ACT_ARRIVE → ACT_HOLD → ACT_ASK → ACT_STOP → ACT_RECEIVE`
- Audio Events: `two spoken lines ／ fire's tremble ／ the crease of the skirt ／ 定型句 whisper at the pull`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the weight in her lap`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The lowering may read as weightless.** A generated body may drift down without mass. The point is the first weight — if it looks floaty, tighten the crease of the skirt and the hang of the slack arms.
- **The girl may resemble the man.** She must never be a copy or reflection of 送り火. The negative prompt front-loads this; verify frame by frame.
- **The two spoken lines may render as subtitles.** They are spoken, never written. The negative prompt excludes on-screen text; verify.
- **The fire may lose its two reaching hands.** The palms-upturned shape is the fire's identity — if it renders as a shapeless glow, hold the framing tighter on its two hands.

## Changes

- _(none yet)_

## Next Generation

- If the weight of the lowering reads, confirm the girl's non-resemblance and the bare forehead carry forward — the seal must not appear until S08.
