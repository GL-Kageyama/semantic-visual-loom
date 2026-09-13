# Wan 3.0 Full Specification — 受け火 第1章「送る」Clip 3/3「手が止まる」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative は series-constants から、§7–20 はこの1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・魂火）のみ日本語。
> この1本の個性：**第1章の第3幕＝手が喉の奥に触れて止まる**。転は静止で語る——喉の奥に**何も見せない**ことが忠実。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold the stop-and-pull third of Chapter 1 (送る) into one 30-second take that ends on its pull — the hand that only sent touches the throat and stops`
- Register: `Restrained and spare. Emotion is never named — it surfaces through the body (a hand that stops at the throat). The horror and the tenderness both live in ordinary objects and withheld action`
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
- Color Language: `Muted, low-saturation. The world is deep indigo and rust red. The soul-fire's pale blue-white is the only bright value — and the only light source`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces. Things read damp though dry`
- Rendering: `Two-step cel shading with softened terminators; faint haze in the damp air`
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

## 魂火 (TAMABI)

- ID: `TAMABI`
- Type: `SUBJECT (a soul of the dead)`
- Role: `Already sent — gone down the flow. Only its warmth remains on the palm`

### Appearance

- Absent. The fire has flowed away down the rail. Only the warmth lingers on the open palm.
- **The throat shows nothing** — no glow, no flame, no inner light. The stop is the whole event.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side is faintly lighter now
- `台帳` (the ledger) — dry paper; closed now, the name 幸恵 already written

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `all distant`

---

# 5. OBJECTS

- `魂火` — もう無い。手のひらにぬくもりだけが残る。`CRITICAL`（火は流れへ行った——残るのは温もり）
- `台帳` — 閉じられている。名 `幸恵` は既に記された

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

The fire is gone. The question is left open on the palm. Then the hand, without thought, rises and touches the back of the throat — and stops. The hand that only sent now knows being grasped. The throat shows nothing; the stop is everything.

## Beginning

The open palm, empty. The fire has flowed away. Only the warmth remains on the palm.

## Turn

The hand, without thought, rises toward the back of the throat. It is not a chosen gesture; it simply happens — the hand that sent, now reaching for something it cannot send.

## Peak

The hand touches the back of the throat — and stops. Completely. The fingers do not close; they only stop. A hand made to scoop, now knowing what it is to be grasped. The throat is not shown to glow; the stop alone carries it.

## Pull（引き — 切れ目）

Only the fire's warmth remains on the palm. The 定型句 — この魂は、まだ誰にも名付けられていない。 — as the boundary's own whisper. Cut on the stopped hand.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The stopping holds the largest share.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「空の手」 — ESTABLISH.** The open palm, empty; only the fire's warmth remains. The question from Clip 2 is still there, unanswered. _Density: SPARSE — a held empty palm._
- **BEAT 2 `[0:07–0:19]` — 「止まる」 — CORE, longest share.** The hand, without thought, rises to the back of the throat and stops. Completely. The hand that only sent now knows being grasped. The throat shows nothing. _Density: HELD — the stop, then a clean stillness._
- **BEAT 3 `[0:19–0:30]` — 「ぬくもり・定型句」.** Only the warmth remains on the palm. The 定型句 — この魂は、まだ誰にも名付けられていない。 — as the boundary's whisper. Cut. _Density: HELD — the whisper, then the clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the hand stopping at the throat (0:07–0:19) ／ the 定型句 (≈0:24)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the empty palm)`
- Dense regions: `0:19–0:30 (the 定型句)`
- Long continuous action: `0:07–0:19 the hand, touching the throat, then still`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `OKURIBI (送り火)`
- Action: `The open palm, empty, the question still on it; only the fire's warmth remains`
- Intention: `None — the question is left open`
- Intensity: `Low, a held stillness`
- Speed: `Still`

### Action Relationship

- Before: `—`
- After: `ACT_RISE`

## Action — ACT_RISE

- ID: `ACT_RISE`
- Subject: `OKURIBI (送り火)`
- Action: `The hand, without thought, rises toward the back of the throat`
- Intention: `Not chosen — the hand reaches for something it cannot send`
- Intensity: `Low`
- Speed: `A slow rise`

### Action Relationship

- Before: `ACT_HOLD`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `OKURIBI (送り火)`
- Action: `The hand touches the back of the throat — and stops. The fingers do not close; they only stop`
- Intention: `None. The stop is not chosen; the hand that only sent now knows being grasped`
- Intensity: `Low, a held stillness`
- Speed: `Slow rise, then a complete halt`

### Action Relationship

- Before: `ACT_RISE`
- After: `— (cut on the stopped hand)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not inside his first person`
- Lens Character: `Hand-level and intimate; the hand is the subject, the face secondary`
- Depth of Field: `Shallow — the hand and the throat are sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits with the hand; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:07]`** — Close on the open palm, empty; only the warmth's faint glow remains.
- **`[0:07–0:19]`** — The hand rises slowly to the back of the throat and stops. Hold on the stopped hand; the throat is not shown to glow.
- **`[0:19–0:30]`** — Hold on the stopped hand. Cut.

---

# 11. MOTION

## Subject Motion

- The hand carries essentially all the movement; the rest of the body holds.
- The rise is a slow, unthought gesture; the stop is a complete halt — the fingers do not close, they only stop.

## Object Motion

- Nothing moves; the ledger is closed; the fire is gone.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.

## Physical Characteristics

- Weight: `送り火's hand has ordinary heft; the stop has the weight of stillness`
- Inertia: `High for the body; the stop is the only abrupt thing, and it is stillness, not a snap`
- Acceleration: `Gentle everywhere; the rise is slow, the stop is absolute`
- Fluidity: `Limited-animation — holds punctuated by small precise gestures`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Stillness (the empty palm, the open question)
- ↓ The rise (a hand reaching for what it cannot send)
- ↓ The stop (a hand that only sent, now knowing being grasped)
- ↓ The warmth (only the fire's warmth remains)

## Emotional Events

- Event: `The hand stops at the throat` — Emotion: `The stop — the hand that only sent now knows being grasped (the 定型句's reference here leans toward 幸恵's soul)` — Intensity: `LOW, a held stillness` — Timing: `≈0:13`
- Event: `The 定型句` — Emotion: `The boundary's own whisper — この魂は、まだ誰にも名付けられていない。` — Intensity: `LOW, near and far` — Timing: `≈0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `None — the fire has gone. Only the faintest cool spill of the departed fire's warmth`
- Fill Light: `Almost none. Deep indigo shadow fills everything`
- Rim Light: `A very faint cool edge on the hand from the memory of the fire's spill`
- Ambient Light: `Near-black indigo and rust red; the far rails glow faintly`
- Color Temperature: `Cold blue-white, fading against deep indigo and rust red`

## Lighting Events

- **`[0:00]`** — The palm is empty and dim; only the warmth's faint glow remains.
- **`[0:07–0:19]`** — The hand rises into shadow at the throat. The throat shows no light. Hold.
- **`[0:19–0:30]`** — The stopped hand in shadow; the faint warmth on the palm. Cut.

---

# 14. AUDIO

## Dialogue

> **The 定型句** (境の地の声, near-and-far whisper): `この魂は、まだ誰にも名付けられていない。` as the pull. 送り火 does not speak. The fire's voice does not return here.

## Sound Effects

- Almost none — the damp near-silence. No footsteps, no breath, no rail, no wind, no page rustle.

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

- **The light law** — the soul-fire's pale blue-white is the only light and the only bright value; here it is gone, leaving only the faintest spill.
- **The palette law** — muted, low-saturation everywhere; the pale blue-white is the only bright value.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the hand.

## Sound Continuity

- **The sound law** — no sound except, at the pull, the boundary's own whisper.

---

# 16. CONSTRAINTS

## MUST

- End on the hand stopping at the throat, cut on the stopped hand.
- **The throat shows nothing** — no glow, no flame, no inner light. The stop is the whole event.
- Keep the soul-fire absent — only the warmth remains on the palm.
- The 定型句 `この魂は、まだ誰にも名付けられていない。` as the boundary's whisper (near and far), not on-screen text.

## MUST NOT（この1本の禁止・開示台帳 01 レンジより）

- **No 花** — no schoolgirl, no sailor uniform, no long dark indigo hair, no second person, no female figure, no silhouette of another person, no reflection of a girl.
- **No glowing object in the throat, no flame inside the throat, no inner light in the throat, no light leaking from the throat.** The 留まり is not made visible here.
- No on-screen text.

## PREFER

- Silence over score.
- The hand as the sole subject of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the exact hue of the warmth's faint glow, the depth of the shadow.

---

# 17. GENERATION PRIORITIES

1. **The staged disclosure** — 花 is absent: no schoolgirl, no sailor uniform, no second figure. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take; it follows the attached character sheet.
3. **The throat restraint** — no glow, no flame, no inner light in the throat. The stop carries it, not a light.
4. **The uneven density** — the stop must hold the largest share.
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing whose rails lead nowhere. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl anywhere. Beats, deliberately uneven: [0:00–0:07] the open palm, empty, only the fire's warmth remaining on it, the unanswered question still there; [0:07–0:19] the hand, without thought, rises to the back of the throat and stops — completely, the fingers not closing, the hand that only sent now knowing being grasped; the throat shows nothing, no glow, no light; [0:19–0:30] only the warmth remains on the palm, and the pull whispers この魂は、まだ誰にも名付けられていない。 Cut on the stopped hand. The stop holds the largest share.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, light haze in the damp air, muted low-saturation palette, deep indigo and rust red, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No schoolgirl, no sailor uniform, no long dark indigo hair, no second figure. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The soul-fire is gone — only the faintest cool spill of warmth on the open palm. The throat shows nothing: no glow, no flame, no inner light. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the hand; the body holds still. The hand rises slowly, without thought, to the back of the throat and stops completely — the fingers do not close, they only stop. The stop is absolute stillness, not a snap. No wind, no dust, no particles, the faintest haze in the damp air. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Hand-level and intimate; the hand is the subject, the face secondary. Shallow depth of field; the hand and the throat are sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:07] close on the open palm, empty, the faint warmth. [0:07–0:19] the hand rises slowly to the throat and stops; hold on the stopped hand, the throat showing nothing. [0:19–0:30] hold on the stopped hand. Cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. No footsteps, no breath, no rail, no wind, no page rustle. Then the pull, the 定型句 in the boundary's own whisper, near and far: この魂は、まだ誰にも名付けられていない。 Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only the whisper. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no schoolgirl, no sailor uniform, no long dark indigo hair, no second person, no female figure, no silhouette of another person, no reflection of a girl, no glowing object in the throat, no flame inside the throat, no inner light in the throat, no light leaking from the throat, no light inside the body, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no readable text, no Japanese kanji or kana, no real-world alphabet, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-v2-ch01-seg03-30s-01`
- Segment ID: `01-3`
- Specification Version: `2.0.0`
- Generation Date: `2026-08-30`

## Resolved Values

- Duration: `30s`
- References: `REF_CHARACTER (okuribi character sheet, HIGH) ／ REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_01, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 7s / 12s / 11s. The stop = BEAT 2 at 12s (40%)`
- Camera Events: `3 events as listed in §10. All third-person-limited holds`
- Action Events: `ACT_HOLD → ACT_RISE → ACT_STOP`
- Audio Events: `定型句 (境の地の声) ／ near-silence`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the stopped hand`

---

# 20. ITERATION

## Version

`2.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The stop may read as a flinch.** It must be a complete, unhurried halt — a slow rise, then stillness. If it reads as a twitch, slow the rise.
- **The throat may glow.** This is the clip where the restraint is tested hardest. The throat must show nothing; verify frame by frame that no light, flame, or glow appears.
- **A schoolgirl may be added.** The negative front-loads `no schoolgirl`; verify frame by frame.
- **Identity drift.** 送り火's face may shift across the take. §15 is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the stop reads and the throat stays dark, Chapter 2 (結城文/指) continues with the fingers — the binding that comes to know "reading".
