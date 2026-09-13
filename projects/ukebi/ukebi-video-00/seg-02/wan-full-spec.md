# Wan 3.0 Full Specification — 受け火 序章 S02「喉の奥の留まり」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../ukebi-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火）・定型句のみ日本語。
> この1本の個性：**喉の奥の燃焼（火でも魂でもない）＋花の不在＋定型句の初出＋二人称「あなた」＋魂火は去った後**。

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

## 喉の留まり (the lodged thing)

- ID: `LODGED`
- Type: `SUBJECT (unnamed — neither fire nor soul)`
- Role: `The one thing none of the eight organs can process`

### Appearance

- A small burning in the hollow of the throat — **neither flame nor face**. Not an object, not a jewel, only a burning.
- Pale blue-white yet red at once, wavering faintly between blue and red. Weightless; the only bright value in the frame.

### Behavior

- Does not act. It simply is, and has always been — kept burning all along.
- 送り火 does not notice it. Only the witness (you) sees it.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. In this segment the crossing falls away into deep indigo and rust red behind the throat. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; here only a dark receding edge behind the close-up, almost unreadable in the dark

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `near-silence — no page rustle, no footsteps, no breath, no wind`

---

# 5. OBJECTS

## 喉の留まり (the lodged thing)

- Type: `light / burning (not a soul-fire)`
- Appearance: `a small burning in the throat's hollow, neither flame nor face, wavering faintly between pale blue-white and red`
- Function: `the sole light source of this segment — the only bright value`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
- Continuity Importance: `CRITICAL`

> The 台帳 (ledger) is untouched in this segment — no page turns, no rustle.

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
- Source: `soul-voice-teller/examples/ukebi/草稿/draft_00_迎え火.md`
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

Something — neither fire nor soul — burns quietly in the back of the throat, where none of the eight organs can reach it. 送り火 does not notice. Only the witness sees it.

## Beginning

The throat's hollow, in the moment after 送り火 has passed. Something is lodged there — you saw it, and cannot unsee it. The eight organs are finished; none of them reached it.

## Turn

It belongs to none of the eight organs, none of the eight verbs. As if it had been there from the beginning. As if it had been kept burning all along.

## Peak

It is not fire. Not soul. Yet it burns. 送り火 does not notice it. Only you see it.

## Pull（引き — 切れ目）

The 定型句, first appearance — the boundary's own voice, near and far: この魂は、まだ誰にも名付けられていない。Cut on the burning.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The burning holds 11s (37%) to fix the lodged thing in the eye.

## Temporal Units

- BEAT — a held witness's gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「喉の奥」 — ESTABLISH.** 送り火's throat, in the moment after he has passed. Something is lodged in the hollow — you saw it, and cannot unsee it. _Density: SPARSE — a held re-grounding on the throat._
- **BEAT 2 `[0:07–0:18]` — 「燃えている」 — CORE, longest share.** The lodged thing burns, quietly. It fits none of the eight organs, none of the eight verbs. As if it had always been there. Not fire, not soul — yet burning. _Density: SPARSE, held — one continuous burning, almost no event._
- **BEAT 3 `[0:18–0:25]` — 「気づかない」.** 送り火 does not notice. His face in profile, eyes not turning toward it. Only you see it. _Density: HELD — the gap between seeing and being seen._
- **BEAT 4 `[0:25–0:30]` — 「定型句」 — PULL.** The boundary's own voice: この魂は、まだ誰にも名付けられていない。 Cut on the burning. _Density: HELD — then a clean cut. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the burning in the throat (0:07–0:18) ／ 送り火 not noticing (≈0:20) ／ the 定型句 (≈0:25)`

## Temporal Density

- Sparse regions: `0:00–0:18 (the throat, the burning)`
- Dense regions: `none — the slowest, most held segment of the prologue`
- Long continuous action: `0:07–0:18 the lodged thing burning`
- Rapid transitions: `none — the whole segment is one held gaze`

---

# 9. ACTION

## Action — ACT_THROAT_LODGED

- ID: `ACT_THROAT_LODGED`
- Subject: `the lodged thing (unnamed)`
- Action: `Burns quietly in the hollow of the throat, without moving, without flaring`
- Intention: `None — it does not act; it simply is, and has always been`
- Intensity: `Low, unvarying`
- Speed: `Still; a slow, faint waver only`

### Action Relationship

- Before: `—`
- After: `ACT_UNAWARE`

## Action — ACT_UNAWARE

- ID: `ACT_UNAWARE`
- Subject: `OKURIBI (送り火)`
- Action: `Passes without pausing; the face in profile, the eyes never turning toward the lodged thing`
- Intention: `None — he does not know it is there`
- Intensity: `Low`
- Speed: `Slow, steady, already leaving`

### Action Relationship

- Before: `ACT_THROAT_LODGED`
- After: `ACT_SEEN`

## Action — ACT_SEEN

- ID: `ACT_SEEN`
- Subject: `the witness (you)`
- Action: `Holds the lodged thing in view; the seeing itself is the only remaining act`
- Intention: `To have seen — there is nothing to do with it`
- Intensity: `Low, a held breath`
- Speed: `Still`

### Action Relationship

- Before: `ACT_UNAWARE`
- After: `— (cut on the burning)`

---

# 10. CAMERA

## Camera Language

- Perspective: `The witness's POV — the eye that alone sees it. Not 送り火's first person, not a third person riding on him`
- Lens Character: `Long, intimate. The world narrows to the throat and the burning`
- Depth of Field: `Very shallow — only the throat's hollow is sharp; the crossing falls away`
- Camera Style: `Almost still. It does not follow 送り火 away; it stays with the burning`

## Camera Behavior

`Almost still — one held, intimate close-up on the throat; a very slow drift; no whip, no shake, no cut until the final.`

## Camera Events

- **`[0:00–0:07]`** — Close on 送り火's throat as he passes, the hollow in shadow. A slow settle onto the lodged thing.
- **`[0:07–0:18]`** — Held, close, on the burning. No movement but its faint waver. The light lives only in the throat's hollow.
- **`[0:18–0:25]`** — A very slow drift to 送り火's face in profile, eyes not turning. The burning stays in the frame's edge, still seen, still unseen.
- **`[0:25–0:30]`** — Drift back to the burning and hold. Cut on it.

---

# 11. MOTION

## Subject Motion

- The lodged thing is the only living motion — a slow, faint waver, and otherwise still.
- 送り火's passage is slow, steady, already receding; his eyes do not turn.
- The witness does not move; the seeing is a held stillness.

## Object Motion

- Nothing else moves. No page turns in this segment; the ledger is not touched.
- The barrier stays raised and still.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.
- Time does not flow; the only change is the burning.

## Physical Characteristics

- Weight: `The lodged thing has no weight; it is a burning, not an object`
- Inertia: `Total — everything holds; nothing starts or stops`
- Acceleration: `None; the waver is a slow, even pulse`
- Fluidity: `Limited-animation — long holds, one faint waver`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- A held breath (seeing what cannot be unseen)
- ↓ Unease without words (it belongs to none of the eight organs)
- ↓ Isolation (he does not notice; only you see)
- ↓ The unnamed (this soul is not yet named by anyone)

## Emotional Events

- Event: `The lodged thing burning` — Emotion: `Unease — it fits none of the eight organs, yet it burns` — Intensity: `LOW, a slow pressure` — Timing: `≈0:07–0:18`
- Event: `送り火 does not notice` — Emotion: `Isolation — the gap between the one who sees and the one who is seen` — Intensity: `LOW-MEDIUM, entirely in the witness's stillness` — Timing: `≈0:20`
- Event: `The 定型句` — Emotion: `The unnamed — this soul is not yet named by anyone (its reference here leans toward the lodged thing itself)` — Intensity: `LOW` — Timing: `≈0:25`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The lodged thing's own faint burn — the only bright value in the frame now`
- Fill Light: `Almost none. Deep indigo shadow fills the throat and the crossing`
- Rim Light: `A very faint cool edge on 送り火's jaw from the burning`
- Ambient Light: `Near-black indigo and rust red, far off and dim`
- Color Temperature: `Cold blue-white tinged with the fire's red, against deep indigo`

## Lighting Events

- **`[0:00]`** — The throat's hollow in shadow as 送り火 passes; the lodged thing begins to read as a small glow.
- **`[0:07–0:18]`** — The burning is the only light — steady, faint, blue-white wavers red.
- **`[0:18–0:25]`** — The light falls away toward his receding profile; the burning stays as the one bright point at the frame's edge.
- **`[0:25–0:30]`** — Hold on the burning. Cut.

---

# 14. AUDIO

## Dialogue

> **The boundary's own voice** (境の地の声), addressing "you" in second person — near and far, a whisper, sparse. Japanese, character-for-character: `火でもない。魂でもない。なのに、燃えている。` (opening) … `送り火は、それに気づいていない。` … and the 定型句 as the pull: `この魂は、まだ誰にも名付けられていない。` No other speech. 送り火 does not speak.

## Sound Effects

- No page rustle in this segment — the ledger is untouched.
- All else is far: no footsteps, no breath, no wind. The world is silent to near-inaudibility.

## Environment

- The damp near-silence of a place where time does not flow — a silence with nothing in it but the whisper.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, held. Never sinister, never sentimental`
- Emotional Function: `Hold the stillness under the whisper. It thins toward the close, leaving only the whisper and the faintest tone`

---

# 15. CONTINUITY

> 12本は12回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

## Identity（must remain consistent）

- 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. No mark on his forehead.
- The stage — a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls.

## Visual Continuity

- **The light law** — the lodged thing's faint burn is the only light and the only bright value; everything else is deep indigo and rust red.
- **The palette law** — muted, low-saturation everywhere; the lodged thing's pale blue-white burn is the only bright value.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; the only movement is the burning's faint waver.

## Sound Continuity

- **The sound law** — no sound at all in this segment; near-silence, no page rustle.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は series-constants §16 相当。ここには**この1本に固有**の制約のみ。

## MUST

- Hold the lodged thing as a burning, not an object — a slow faint waver in the throat's shadow.
- Keep the camera at the witness's POV (second-person "you").
- End on the 定型句 (the boundary's own voice) and cut on the burning.

## MUST NOT（この1本の禁止・開示台帳 01–04 レンジより）

- **No 花 — no girl, no schoolgirl, no sailor uniform, no long dark hair, no second person, no female figure, no silhouette of another person, no reflection of a girl.**
- No human form in the lodged thing — it is not a face, not a figure, not a jewel, only a burning.
- No on-screen text (this segment shows no diegetic writing; the 定型句 is voice, not text).
- No soul-fire in this segment (the soul has been sent; only the lodged thing burns).

## PREFER

- Silence over score.
- The burning as one held, uninterrupted close-up.
- Negative space over detail.

## ALLOW

- Slight variation in the burning's exact waver and color between blue and red.
- The crossing behind may be nearly unreadable in the dark.

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: 花 is absent — no girl, no silhouette, no reflection, no second figure. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take.
3. **The exact Japanese narration** — the narration lines and the 定型句 are evidence; unreadable or altered, the work fails.
4. **The uneven density** — the burning in the throat (the take's spine) must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of something burning in the hollow of a nameless man's throat. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No girl anywhere. Beats, deliberately uneven: [0:00–0:07] 送り火's throat in the moment after he has passed, something lodged in the hollow, seen and cannot be unseen; [0:07–0:18] the lodged thing burns quietly — it fits none of the eight organs, none of the eight verbs, as if it had always been there, not fire, not soul, yet burning; [0:18–0:25] 送り火 does not notice, his face in profile, eyes not turning toward it, only the viewer sees it; [0:25–0:30] the boundary's own voice, near and far, a whisper: この魂は、まだ誰にも名付けられていない。 Cut on the burning. The burning holds the largest share of the duration. Ends on the 定型句.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the burning, light haze in the damp air, muted low-saturation palette, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No girl, no schoolgirl, no sailor uniform, no long dark hair, no second figure, no female figure, no silhouette of another person, no reflection of a girl. His throat in close view; in its hollow, a small burning that is neither flame nor face, wavering faintly between pale blue-white and red. The railroad crossing behind falls away into deep indigo and rust red, air damp though no rain falls, a raised barrier that never lowers. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — long holds punctuated by one faint waver, never continuous interpolation. The burning is the only living motion: a slow, even pulse, otherwise still. 送り火's passage is slow and steady, already receding, his eyes not turning. Nothing else moves — no wind, no dust, no particles, the faintest haze in the damp air; the barrier stays raised and still; time does not flow. The lodged thing has no weight; nothing collides, falls, or strikes. No motion blur smears, no squash and stretch.

## Camera Prompt

The witness's POV throughout — the eye that alone sees it; not 送り火's first person, not a third person riding on him. Long, intimate lens, very shallow depth of field; only the throat's hollow is sharp. Almost still; the camera does not follow 送り火 away, it stays with the burning. [0:00–0:07] close on 送り火's throat as he passes, a slow settle onto the lodged thing. [0:07–0:18] held close on the burning, no movement but its faint waver. [0:18–0:25] a very slow drift to his face in profile, eyes not turning, the burning still at the frame's edge. [0:25–0:30] drift back to the burning and hold; cut.

## Audio Prompt

Almost silent — the damp near-silence of a place where time does not flow. No page rustle, no footsteps, no breath, no wind. A voice — the boundary's own voice, near and far, a whisper — addresses the viewer in second person, sparse: 火でもない。魂でもない。なのに、燃えている。 … 送り火は、それに気づいていない。 … and the pull, the 定型句: この魂は、まだ誰にも名付けられていない。 No other speech. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only the whisper. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no girl, no schoolgirl, no sailor uniform, no long dark hair, no second person, no female figure, no silhouette of another person, no reflection of a girl, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-ch00-seg02-30s-01`
- Segment ID: `S02`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_00, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 11s / 7s / 5s. The burning = BEAT 2 at 11s (37%)`
- Camera Events: `4 events as listed in §10. All witness-POV holds and drifts`
- Action Events: `ACT_THROAT_LODGED → ACT_UNAWARE → ACT_SEEN`
- Audio Events: `narration (境の地の声, 3 lines incl. 定型句) ／ near-silence (no page rustle)`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the burning`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The burning may render as a jewel or an object.** It must read as a burning inside the throat's shadow — neither a flame nor a face. If it hardens into a gem, dim it toward ember and loosen the edge.
- **Identity drift.** 送り火's face may shift across the take. §15 is the defense.
- **The model may add a figure.** The negative prompt front-loads `no girl, no second person`; verify frame by frame.
- **The 定型句 may be mis-timed.** It must land on the pull, not earlier, and read as the boundary's own voice, not a character's.

## Changes

- _(none yet)_

## Next Generation

- If the burning reads as nameless and unnamed, the series continues in S03 — the hand that stops, where the guest's soul first raises a voice.
