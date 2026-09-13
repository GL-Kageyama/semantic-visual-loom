# Wan 3.0 Full Specification — 受け火 第5章 S07「手首をつかまれる」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../ukebi-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火）・定型句のみ日本語。
> この1本の個性：**耳＝測る（測る→測られる・受動態の傾斜の二歩目）＋秤の針が振れない（該当なし）＋少女が秤を降り、手首をかるくつかむ＋花の台詞「あなたの重さは」＋花の在（判なし）＋三人称制限＋定型句**。

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

## 花 (HANA)

- ID: `HANA`
- Name: `少女 (the girl — nameless; she has no name yet)`
- Type: `CHARACTER`
- Role: `The soul weighed at the scale — a soul without a price, sent nowhere. She is herself a soul (該当なし); her own pale blue-white fire is the chapter's light`

### Appearance

- A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet, though no rain falls on her.
- Long dark indigo hair; a quiet, steady gaze. At the crossing, no one had ever looked at 送り火 — only she looks at him.
- She does **not** resemble 送り火 — no copy, no reflection, no suggestion they are the same person.
- No seal appears yet (the seal on 送り火's forehead is S08 onward).

### Behavior

- Stands on the pan of the scale; her weight does not move the needle — 該当なし, neither heavy nor light.
- Steps off the scale, reaches out, and her fingers take his wrist, lightly — a weightless one asks after weight.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter
- `秤` (the scale) — a pan and a needle, dry and still; it weighs souls to decide where each is sent; the needle points straight up

> The 台帳 (registry) is absent in this chapter — no page turns, no mark.

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `soundless — no page rustle; the scale is soundless too (the needle does not tilt, so there is no tilt to hear). Only the one voice and the near-absence around the scale`

---

# 5. OBJECTS

## 秤 (Hakari — the scale)

- Type: `measuring instrument / object`
- Appearance: `a pan and a needle, dry and still; the needle points straight up; the face reads 該当なし`
- Material: `dry metal and wood — the air is damp but the scale is dry`
- Function: `weighs souls to decide where each is sent — heavy souls go far, light souls go near; a soul without a price stands on the pan and the needle does not move`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
- Continuity Importance: `HIGH`

> The girl's own soul-fire (pale blue-white) is the chapter's light — there is no guest soul this chapter. The 台帳 (registry) is absent.

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
- Source: `soul-voice-teller/examples/ukebi/草稿/draft_05_測る.md`
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

There is a scale at the crossing for weighing souls — the next life is decided by how heavy the soul is. The man listens with his ears, the fifth organ, for the tilt of the needle. The girl's weight does not move the needle at all: 該当なし. She steps off the scale, reaches out, and her fingers take his wrist, lightly. Measured by hand, he learns his own weight for the first time. His ears stop.

## Beginning

There is a scale at the crossing, for weighing souls — to decide where each is sent. Heavy souls go far, light souls go near. The man moves his ears, the fifth organ: he listens for the tilt of the needle. He does not look; he measures by ear. Weight arrives as sound.

## Turn

The girl's weight does not move the needle. 該当なし. The needle does not tilt; the pan does not sink. She will be sent nowhere — neither heavy nor light. A soul without a price stands on the pan. The needle points straight up. It does not move. There is no sound. The ears meant for measuring hear nothing to measure.

## Peak

The girl steps off the scale. She reaches out, touches his arm — not the scale. She measures by hand. Her fingers take his wrist, lightly. A weightless one asks after weight. His wrist taken, the man learns his own weight for the first time — the hardness of the bone in his wrist. The ears meant for measuring are now, themselves, measured. By hand. His ears stop.

## Pull（引き — 切れ目）

At the crossing, no one had ever measured him; only the girl tries to. Her fingers on his wrist. Her voice: あなたの重さは。 Cut on the grip and the whisper: この魂は、まだ誰にも名付けられていない。

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The taking of the wrist holds 9s (30%) — the reversal (being measured by hand) carries the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「秤と、耳」 — ESTABLISH.** A scale at the crossing. The man listens with his ears, the fifth organ, for the tilt of the needle. Heavy souls far, light souls near. _Density: SPARSE — the scale, the listening, almost nothing else._
- **BEAT 2 `[0:07–0:14]` — 「針が振れない」.** The girl on the scale. The needle does not tilt; the pan does not sink. 該当なし. The needle points straight up, still, soundless. _Density: HELD — the motionless needle, the silence of the scale._
- **BEAT 3 `[0:14–0:23]` — 「手首をつかまれる」 — TURN, longest share.** The girl steps off the scale, reaches out, her fingers take his wrist, lightly. Measured by hand, he learns his own weight, the bone's hardness. _Density: SPARSE then HELD — one small gesture, a whole reversal._
- **BEAT 4 `[0:23–0:30]` — 「耳が止まる／あなたの重さは」.** His ears stop. Her voice: あなたの重さは。 Cut on the grip and the whisper of the 定型句. Nothing after it. _Density: HELD — the question, the whisper, the cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the taking of the wrist (0:14–0:23) ／ the motionless needle and 該当なし (≈0:10) ／ her question あなたの重さは (≈0:25)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the listening), 0:14–0:23 (the wrist)`
- Dense regions: `0:07–0:14 (the needle that will not move — a few facts stacked in the silence)`
- Long continuous action: `0:14–0:23 the reaching out and taking of the wrist`
- Rapid transitions: `none — a held, deliberate segment`

---

# 9. ACTION

## Action — ACT_LISTEN

- ID: `ACT_LISTEN`
- Subject: `OKURIBI (送り火)`
- Action: `He listens with his ears for the tilt of the needle, not looking`
- Intention: `The fifth organ — to know the weight by the sound of the needle`
- Intensity: `Low`
- Speed: `Still; the listening is the only motion`

### Action Relationship

- Before: `—`
- After: `ACT_WEIGH`

## Action — ACT_WEIGH

- ID: `ACT_WEIGH`
- Subject: `SCALE（秤）`
- Action: `The girl stands on the pan; the needle does not tilt, points straight up`
- Intention: `To measure her — and fail. 該当なし. Neither heavy nor light`
- Intensity: `Low, then still`
- Speed: `Nothing moves. The needle is straight up, soundless`

### Action Relationship

- Before: `ACT_LISTEN`
- After: `ACT_DESCEND`

## Action — ACT_DESCEND

- ID: `ACT_DESCEND`
- Subject: `HANA（少女）`
- Action: `She steps off the scale and reaches toward his arm`
- Intention: `Not the scale — she will measure by hand`
- Intensity: `Low, sure`
- Speed: `Slow, deliberate`

### Action Relationship

- Before: `ACT_WEIGH`
- After: `ACT_GRASP`

## Action — ACT_GRASP

- ID: `ACT_GRASP`
- Subject: `HANA (花)`
- Action: `Her fingers take his wrist, lightly`
- Intention: `A weightless one asks after weight — to measure him with her hand`
- Intensity: `Low, exact`
- Speed: `A light, sure grip; the fingers close without force`

### Action Relationship

- Before: `ACT_DESCEND`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `OKURIBI (送り火)`
- Action: `His wrist taken, he learns his own weight — his ears stop`
- Intention: `None. The organ that measured is now measured, by hand`
- Intensity: `Medium, internal`
- Speed: `A full stop — only the grip holds, still`

### Action Relationship

- Before: `ACT_GRASP`
- After: `— (cut on the grip)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, at the height of the scale and then of the wrist. Watchful, not intimate`
- Lens Character: `Medium. The crossing reads as one sparse plane behind the scale`
- Depth of Field: `Shallow — the needle and then the wrist are sharp; the background falls away`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Behavior

`Static with slow drift and a slow follow. No whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:07]`** — Medium close on the scale and the man listening beside it. Static, watchful. The needle visible, vertical.
- **`[0:07–0:14]`** — Close on the pan with the girl standing on it, the needle straight up, motionless. 該当なし reading at the scale's face. Nearly static.
- **`[0:14–0:23]`** — The camera follows her as she steps off, slow, then holds close on her fingers closing around his wrist. The grip, light and sure.
- **`[0:23–0:30]`** — Hold on the grip — her fingers on his wrist, the two of them still. Cut.

---

# 11. MOTION

## Subject Motion

- The man is nearly motionless throughout — only the listening, and then nothing. His ears stop.
- The girl's motion is small and exact: she steps down, reaches out, and her fingers close around his wrist.
- The needle is the central stillness — straight up, never moving, never even trembling.

## Object Motion

- The scale does not move on its own; the pan does not sink; the needle does not tilt.
- Nothing else in the crossing moves. The barrier stays raised; the rails do not stir.

## Environmental Motion

- None. The air is damp but still; no wind, no particles beyond the faintest haze.

## Physical Characteristics

- Weight: `The pivotal physics. The girl is weightless — the pan does not sink, the needle does not move. The man, by contrast, has weight, and it is only through her grip that he feels it — the bone in his wrist, hard and real`
- Inertia: `High for the man — he is rooted until the grip closes; the girl moves with quiet certainty`
- Acceleration: `Gentle everywhere; the grasp is a closing, not a clutch`
- Fluidity: `Limited-animation — holds punctuated by small precise movements (the listening, the step, the closing fingers)`
- Impact: `None, but the one weighted contact — her fingers on his wrist — must read as the first time he feels his own weight`

---

# 12. EMOTION

## Emotional Arc

- Listening (the fifth organ, the needle's tilt as sound)
- ↓ The motionless needle (該当なし — a weight that will not read)
- ↓ Measured by hand (her fingers on his wrist — the bone's hardness)
- ↓ The question (あなたの重さは — his ears stop)

## Emotional Events

- Event: `The needle will not move` — Emotion: `A silence that refuses to resolve — neither heavy nor light` — Intensity: `LOW` — Timing: `≈0:10`
- Event: `Her fingers close around his wrist` — Emotion: `Being measured — not named, but felt; the first knowledge of his own weight` — Intensity: `MEDIUM — carried in the bone's hardness, not the face` — Timing: `≈0:18`
- Event: `Her question` — Emotion: `A question he has no answer for — the ears stop` — Intensity: `LOW, held` — Timing: `≈0:25`
- Event: `The whisper of the 定型句` — Emotion: `A namelessness named, from far away` — Intensity: `LOW — a close, distant whisper` — Timing: `≈0:28`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The soul-fire — pale blue-white, the only light. It lights the scale, the girl, and the wrist`
- Fill Light: `Almost none. Deep indigo fills everything the fire does not reach`
- Rim Light: `A faint cool edge on the needle and on the girl's dark hair`
- Ambient Light: `Deep indigo and rust red; the air is damp and dark`
- Color Temperature: `Cold blue-white fire against deep indigo, rust red at the edges`

## Lighting Events

- **`[0:00]`** — The fire's pale light lies on the scale and the man listening.
- **`[0:07–0:14]`** — The light is still on the girl on the pan, the needle vertical and faintly bright, 該当なし legible at the scale's face.
- **`[0:14–0:23]`** — The light follows her down and to his wrist as her fingers close.
- **`[0:23–0:30]`** — Hold: the fire's light on the joined wrist and the girl's hand. Cut.

---

# 14. AUDIO

## Dialogue

> **One spoken line, then silence.**
> HANA（少女）: `あなたの重さは` — low, level, a question that is not a demand.
> 送り火 does not answer. The 定型句 is the boundary's whisper at the pull, not on screen: `この魂は、まだ誰にも名付けられていない。`

## Sound Effects

- The scale is soundless in this chapter — the needle does not tilt, so there is no tilt to hear. This absence is the point.
- The dry rustle of the registry's page — absent here; the chapter has no registry.
- The faintest soft sound of cloth as the girl steps down and reaches — small, close.

## Environment

- A damp, soundless crossing. Every sound is far away except the one voice and the near-absence around the scale.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, held. Never sinister, never sentimental`
- Emotional Function: `Hold the silence of the motionless needle, then thin to nothing as her fingers close. The music must not insist on the moment — the grip and the question carry it`

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

- **The sound law** — no sound except the one spoken voice and the near-absence around the scale; no registry page in this chapter.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は series-constants（Negative・受け火開示台帳）相当。ここには**この1本に固有**の制約のみ。

## MUST

- Establish the ears' stop and the reversal into being measured — the fifth organ freezing as her fingers close on his wrist.
- Render the on-screen Japanese exactly: `該当なし`（秤の印。character-for-character）。
- Render the spoken line exactly: `あなたの重さは`（character-for-character）。
- Make the needle's stillness the central fact — straight up, never moving, no tilt, no sound.
- Keep the soul-fire the sole light source — pale blue-white against deep indigo and rust red.
- End on the grip and the 定型句 whisper, cut with nothing after it.

## MUST NOT（この1本の禁止・開示台帳 S07 レンジより）

- **No name, no identity for the girl.** Do not say 篠宮, do not say 花. She has no name yet.
- **No seal on 送り火's forehead** — the seal is S08 onward. His forehead is bare.
- **Do not make the girl resemble 送り火** — no copy, no reflection, no suggestion they are the same person, no matching face, no mirrored pose.
- **The needle must not tilt** — it points straight up and never moves. No twitch, no drift.
- No on-screen subtitles or captions burned in (the scale's 該当なし is diegetic, not a subtitle; the spoken line is never written).

## PREFER

- The taking of the wrist held as long as possible — the whole turn is one small, weighted gesture.
- Silence over score; the one voice and the near-absence are the only sounds.
- Negative space over detail; the crossing may be nearly empty.

## ALLOW

- Slight variation in the scale's design (pan, needle, face) and the girl's sleeve length.
- The imperceptible settle of the camera may be omitted (a fully locked frame is equally correct).
- Music may be absent altogether.

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: 花 appears but only as 少女 — no name, no identity, no seal. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take; 花 must never resemble 送り火.
3. **The exact Japanese** — 秤の印 `該当なし` and the spoken line `あなたの重さは` are evidence; unreadable or altered, the work fails.
4. **The uneven density** — the taking of the wrist (the take's spine) must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Beats, deliberately uneven: [0:00–0:07] a scale at the crossing, and a plain unremarkable man listening with his ears, the fifth organ, for the tilt of the needle; [0:07–0:14] a girl stands on the pan, the needle does not tilt, points straight up, 該当なし reading at the scale's face, soundless; [0:14–0:23] the girl steps off, reaches out, and her fingers take his wrist lightly — measured by hand, he learns his own weight, the bone's hardness; [0:23–0:30] his ears stop, and she asks, あなたの重さは. The taking of the wrist holds the largest share. Ends on the grip and a whisper: この魂は、まだ誰にも名付けられていない。

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A railroad crossing: rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls. A scale for weighing souls — a pan and a needle, dry and still, its face reading 該当なし. A plain unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands, bare forehead. A girl, a high-school student in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though no rain falls on her, long dark indigo hair, a quiet steady gaze; she does not resemble the man. The soul-fire is the only light and the only bright value, pale blue-white. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the girl: her step off the pan, her reach, her fingers closing around his wrist. The needle is the central stillness — straight up, never moving, never even trembling; the pan does not sink. The man is nearly motionless throughout, only listening, and then nothing — his ears stop. Gentle acceleration everywhere; the grasp is a closing, not a clutch. No wind, no moving shadows, no particles beyond the faintest haze. No impacts beyond the one weighted grip. No motion blur smears, no squash and stretch.

## Camera Prompt

Close, at the height of the scale and then of the wrist, watchful and nearly still; the camera drifts and never whips or shakes. [0:00–0:07] medium close on the scale and the man listening beside it, static. [0:07–0:14] close on the pan with the girl standing on it, the needle straight up, 該当なし legible at the scale's face, nearly static. [0:14–0:23] follow her as she steps off, slow, then hold close on her fingers closing around his wrist. [0:23–0:30] hold on the grip, her fingers on his wrist, the two still; cut.

## Audio Prompt

Almost silent. A damp, soundless crossing; every sound is far away. The scale is soundless — the needle does not tilt, so there is no tilt to hear; this absence is the point. One spoken line: the girl, low and level, あなたの重さは. The man does not answer. The faintest soft sound of cloth as she steps down and reaches, close. Music extremely sparse — a few sustained tones at most, thinning to nothing. At the pull, a close and distant whisper, the voice of the boundary, neither on-screen nor loud: この魂は、まだ誰にも名付けられていない。 No horror strings, no sting, no swelling emotion.

## Negative Prompt

no resemblance between the girl and the man, no copy of the man, no reflection of the girl, no seal on the forehead, no name written for the girl, no tilting of the needle, no movement of the pan, no on-screen subtitles, no captions, no English text, no narration text, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no morphing or drifting facial identity, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges, no watermark

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-ch05-seg01-30s-01`
- Segment ID: `S07`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_05_測る, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 7s / 9s / 7s. The wrist = BEAT 3 at 9s (30%)`
- Camera Events: `4 events as listed in §10. No sustained dolly; all static, drift, or follow`
- Action Events: `ACT_LISTEN → ACT_WEIGH → ACT_DESCEND → ACT_GRASP → ACT_STOP`
- Audio Events: `one spoken line ／ the soundless scale ／ cloth as she reaches ／ 定型句 whisper at the pull`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the grip`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The needle may be animated to move.** The whole point is its stillness — straight up, never tilting. If it twitches or drifts, hold the frame tighter and cut the needle's motion.
- **The 該当なし may render as noise.** It is the chapter's on-screen evidence; if unusable, prefer it sharp and legible — it must read character-for-character.
- **The grasp may read as weightless or as a clutch.** Her fingers must close lightly and surely, and the man must feel his own weight through it — the bone's hardness, not a romantic clasp.
- **The girl may resemble the man.** She must never be a copy or reflection of 送り火. The negative prompt front-loads this; verify frame by frame.

## Changes

- _(none yet)_

## Next Generation

- If the grip and the still needle read, confirm the girl's non-resemblance and the bare forehead carry forward — the seal must not appear until S08.
