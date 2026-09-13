# Wan 3.0 Full Specification — 受け火 第8章 S11「目が初めて花を見る」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../ukebi-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・篠宮花）・定型句のみ日本語。
> この1本の個性：**目＝見る（背→目・振り返る→見る）＋値付ける目が値付けではないことをする（ただ見る）＋花の在（額に判）＋三人称制限＋定型句が震える（「この魂は、まだ、誰にも、名付けられていない。」）**。

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

## 花 (HANA) — 篠宮花

- ID: `HANA`
- Name: `篠宮花 (revealed in S10; still not spoken by 送り火)`
- Type: `CHARACTER`
- Role: `The first self 送り火 discarded — his half-self, whose eyes had been watching him from the beginning`

### Appearance

- A high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet, though no rain falls on her.
- Long dark indigo hair; a quiet, steady gaze. At the crossing, no one had ever looked at 送り火 — only she looks at him.
- She does **not** resemble 送り火 — the discarded half-self is not a facial resemblance. No copy, no reflection, no suggestion they are the same person.

### Behavior

- Says nothing; barely moves. Her eyes have been watching him from the beginning, all along — and now, at last, they are met.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter

> The 台帳 (registry), the 秤 (scale), and the 判 (seal) are all absent as objects this chapter. There is no guest soul — the chapter's light is the boundary's dim indigo and the faint light of the flow at the rails' far end. The seal is already on 送り火's forehead (S08+).

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `total stillness — 境 has no sound at all; no wind, no rain, no breathing`

---

# 5. OBJECTS

> **No objects this chapter.** There is no soul-fire (no guest soul — the light is the boundary's dim indigo and the faint light of the flow), no registry, no scale. The 判 (seal) is already on 送り火's forehead (S08+), part of his identity rather than an object here.

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
- Source: `soul-voice-teller/examples/ukebi/草稿/draft_08_捨てる.md`
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

He turns around. The eye made for pricing does what is not pricing — it sees 花. At the boundary, no one had ever seen him; only the girl had been watching. Now, for the first time, he sees her. The eye moves to her on its own — the first movement of an organ from him to her. Instead of turning a discarding back, he turns a seeing eye.

## Beginning

The back is still turned, still stopped. He knows through his back that she does not turn away — she is looking at him, always.

## Turn

He turns around. The eye that prices, toward the girl who has no price.

## Peak

The eye sees 花. Not pricing — just seeing. The eye moves to her on its own. 花 says nothing, but her eyes had been watching him from the beginning, all along.

## Pull（引き — 切れ目）

The boundary's voice, near and far, now trembling — the refrain, with its added punctuation: この魂は、まだ、誰にも、名付けられていない。 Cut. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The seeing — the eye's first movement toward her — holds 14s (47%).

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「背は向けられたまま」 — ESTABLISH.** The back is still turned, still stopped. He knows through his back that she does not turn away — she is looking at him, always. _Density: SPARSE — the held stillness of S10, carried over._
- **BEAT 2 `[0:06–0:12]` — 「振り返る」.** He turns around. The back gives way to the face; the eye that prices turns toward the girl who has no price. _Density: TRANSITION — the turn, before the seeing._
- **BEAT 3 `[0:12–0:26]` — 「目が、花を見る」 — REVEAL, longest share.** The eye sees 花 — not pricing, just seeing. The eye moves to her on its own. 花 says nothing, but her eyes had been watching him from the beginning, all along. The first movement of an organ from him to her. _Density: SPARSE, held — the whole turn is this one gaze._
- **BEAT 4 `[0:26–0:30]` — 「震える定型句」.** The boundary's voice, near and far, trembling: この魂は、まだ、誰にも、名付けられていない。 Cut on the trembling whisper. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the turning around (≈0:09) ／ the eye seeing 花 (≈0:12) ／ the trembling refrain (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the still back), 0:12–0:26 (the gaze)`
- Dense regions: `0:06–0:12 (the turning)`
- Long continuous action: `0:12–0:26 the seeing`
- Rapid transitions: `none — the gaze is the slowest, most held moment of the chapter`

---

# 9. ACTION

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `OKURIBI (送り火)`
- Action: `Holds the stopped back, knowing through it that she does not turn away`
- Intention: `Not to turn — not yet`
- Intensity: `Low, still`
- Speed: `Motionless`

### Action Relationship

- Before: `— (continues from S10's stopped back)`
- After: `ACT_TURN_AROUND`

## Action — ACT_TURN_AROUND

- ID: `ACT_TURN_AROUND`
- Subject: `OKURIBI (送り火)`
- Action: `Turns around — the back gives way to the face`
- Intention: `To face her, instead of discarding her`
- Intensity: `Medium`
- Speed: `Slow, deliberate`

### Action Relationship

- Before: `ACT_HOLD`
- After: `ACT_SEE`

## Action — ACT_SEE

- ID: `ACT_SEE`
- Subject: `OKURIBI (送り火)`
- Action: `The eye sees 花 — not pricing, just seeing. The eye moves to her on its own`
- Intention: `Not to value her — to see her, for the first time`
- Intensity: `Medium, entirely still`
- Speed: `A held gaze — the first movement of an organ from him to her`

### Action Relationship

- Before: `ACT_TURN_AROUND`
- After: `— (the trembling refrain, then cut)`

---

# 10. CAMERA

## Camera Language

- Perspective: `From behind the back, then around to his face, then to her — the frame does the turning with him`
- Lens Character: `Long-ish, shallow. The eyes — his, then hers — are what the frame finds`
- Depth of Field: `Shallow — one pair of eyes sharp at a time`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Behavior

`Static behind the back, then around with the turn to the two faces. No whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:06]`** — Hold behind the stopped back, as in S10. Beyond it, 花, still looking at him.
- **`[0:06–0:12]`** — The camera comes around as he turns — the back gives way to his face, the faint seal on his forehead, then his eyes.
- **`[0:12–0:26]`** — On his eyes — the eye that prices, now only looking. Then a slow drift to her: 花's face, her quiet steady gaze, watching him from the beginning. Hold on her eyes.
- **`[0:26–0:30]`** — Hold on her eyes (or his — the gaze), the whisper trembling over it. Cut on the whisper.

---

# 11. MOTION

## Subject Motion

- The turning around is the only whole-body motion — slow, deliberate, from the stopped back to the face.
- Then only the eyes move — his gaze settling on her, hers already on him.
- 花 says nothing and barely moves; only her eyes, holding him.

## Object Motion

- Nothing moves on its own. The raised barrier is still; the rails do not move; the flow beyond is a faint, distant light.
- No flicker, no drift, no disturbance.

## Environmental Motion

- None. No wind, no rain (though the air reads wet), no moving shadows, no particles — only the faintest haze in the damp air.

## Physical Characteristics

- Weight: `The turn carries the weight of leaving off the ritual — a turn toward, not away`
- Inertia: `High. The body stills into the gaze without recoil`
- Acceleration: `Gentle; the turn slows into the held look`
- Fluidity: `Limited-animation — one slow turn, then a held frame`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- The still back (knowing she is watching)
- ↓ The turning (to face her, not discard her)
- ↓ The seeing (the eye that prices, only looking)
- ↓ The trembling refrain (who has never been named)

## Emotional Events

- Event: `The eye seeing 花, not pricing` — Emotion: `The first movement of an organ from him to her — not ritual, but something beginning` — Intensity: `MEDIUM, withheld into the gaze` — Timing: `≈0:12`
- Event: `花's eyes, watching from the beginning` — Emotion: `She had been seeing him all along — now met` — Intensity: `MEDIUM, entirely still` — Timing: `≈0:18`
- Event: `The trembling refrain` — Emotion: `The refrain breaks — the added commas are the voice's hesitation. この魂は、まだ、誰にも、名付けられていない。 now leans toward 送り火 himself and 花` — Intensity: `MEDIUM` — Timing: `≈0:26`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `No soul-fire here. The dim light of the boundary — deep indigo, with the faint light of the flow at the far edge of the rails`
- Fill Light: `Almost none. Soft indigo fills the space`
- Rim Light: `A very faint cool edge on 送り火's face and 花's hair from the distant flow`
- Ambient Light: `Deep indigo; the rust-red of the rails reads faintly red in the damp dark`
- Color Temperature: `Cold, near-monochrome indigo, with the rust red of the rails`

## Lighting Events

- **`[0:00]`** — The boundary dim, the flow a faint light at the rails' far end.
- **`[0:06–0:12]`** — As he turns, his face comes into the faint light — the seal on his forehead, his eyes.
- **`[0:12–0:26]`** — The light settles on her face as the gaze is met. No change — the seeing is a stillness of light.
- **`[0:26–0:30]`** — Hold. Cut on the whisper.

---

# 14. AUDIO

## Dialogue

> No speech. 花 says nothing. 送り火 says nothing — he does not yet speak her name (that is S12). The only voice is the boundary's own, near and far.

## Narration

> The boundary's own voice, near and far, at the pull — now trembling, the refrain with its added punctuation: `この魂は、まだ、誰にも、名付けられていない。` The added commas are audible hesitations. The 指示先 has shifted: it now leans toward 送り火 himself and 花, not the guest.

## Sound Effects

- None. No wind, no rain, no footsteps, no breathing — 境 is silent.

## Environment

- Total stillness. The kind of silence in which a tremble in the voice is the only sound.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, grave, tender. Never sinister, never sentimental`
- Emotional Function: `Hold the stillness under the gaze, then fall away entirely as the refrain trembles — leaving only the trembling voice`

---

# 15. CONTINUITY

> 12本は12回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

## Identity（must remain consistent）

- 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. A faint pale square seal on his forehead reading 該当なし (S08+).
- 花 (S10 = 篠宮花, revealed) — a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though the rain never falls on her. Long dark indigo hair, a quiet steady gaze that watches. She must never resemble 送り火 — the discarded half-self is not a facial resemblance.
- The stage — a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls.

## Visual Continuity

- **The light law** — no soul-fire this chapter; the boundary's deep indigo and the faint light of the flow at the rails' far end are the only light. (The soul-fire's absence is this chapter's own.)
- **The palette law** — muted, low-saturation everywhere; deep indigo and rust red, near-monochrome.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the organ's gesture.

## Sound Continuity

- **The sound law** — total stillness; 境 has no sound at all. Only the boundary's trembling voice (the refrain) is heard.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は series-constants（Negative・受け火開示台帳）相当。ここには**この1本に固有**の制約のみ。

## MUST

- Show the eye doing what is not pricing — it sees 花, it does not value her.
- The turn: from the stopped back, around to the face, then to the gaze.
- 花 says nothing; her eyes have been watching him from the beginning.
- Keep 送り火's faint pale square seal `該当なし` on his forehead.
- End on the trembling refrain この魂は、まだ、誰にも、名付けられていない。 with nothing after it.

## MUST NOT（この1本の禁止・開示台帳 S11 レンジより）

- **送り火 does not speak 花's name aloud** — the naming (「花」 from his mouth) is S12.
- **花 must never resemble 送り火** — no mirror, no reflection, no doubling, no same-person suggestion.
- No on-screen text (S11 の画面文字は「なし」).
- No environmental sound — 境 has no sound (no wind, no rain).

## PREFER

- The gaze held as long as possible — the whole turn is one held look.
- Silence over score at the seeing.
- Negative space over detail; the frame nearly empty but for the two faces.

## ALLOW

- Slight variation in the exact framing of the two faces (his eyes then hers).
- Music may be absent altogether.

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: 花's name/identity are already revealed (S10); 送り火 does not yet speak her name (S12). 花 must never resemble 送り火. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take (with the seal); 花 must never resemble 送り火.
3. **The exact Japanese** — the trembling refrain この魂は、まだ、誰にも、名付けられていない。 (with its added commas) is evidence; altered or unreadable, the work fails.
4. **The uneven density** — the seeing (the take's spine) must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, at a railroad crossing that leads nowhere. A plain unremarkable man — 送り火 — turns around and, for the first time, sees the girl with his eyes instead of discarding her with his back. Beats, deliberately uneven: [0:00–0:06] the back is still turned, still stopped, and he knows through it that she does not turn away — she is looking at him, always; [0:06–0:12] he turns around, the back giving way to the face; [0:12–0:26] THE REVEAL — the eye made for pricing does what is not pricing: it sees 花, it moves to her on its own, and her eyes, which had been watching him from the beginning, meet his; [0:26–0:30] the boundary's voice, near and far, trembling, speaks the refrain この魂は、まだ、誰にも、名付けられていない。, and the shot cuts on the trembling whisper. The seeing holds the largest share of the duration. Ends on the refrain.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, light haze in the damp air, muted low-saturation palette, simple uncluttered stage, generous negative space, one focal point per shot. 送り火: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands, and a faint pale square seal on his forehead reading 該当なし. 花: a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though the rain never falls on her, long dark indigo hair, a quiet steady gaze that watches — she must never resemble 送り火. The stage: a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls. No soul-fire here; the deep indigo of the boundary, the faint light of the flow at the rails' far end, the rust-red rails. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. The turning around is the only whole-body motion — slow, deliberate, from the stopped back to the face. Then only the eyes move: his gaze settling on her, hers already on him. 花 says nothing and barely moves; only her eyes hold him. Nothing moves on its own — the raised barrier is still, the rails do not move, the flow beyond is a faint distant light. No wind, no rain, no moving shadows, no particles, only the faintest haze in the damp air. Gentle acceleration; the turn slows into the held look. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

From behind the back, then around to his face, then to her — the frame does the turning with him. Longish lens, shallow depth of field; one pair of eyes sharp at a time. Slow, deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] hold behind the stopped back; beyond it, 花, still looking at him. [0:06–0:12] the camera comes around as he turns — the back gives way to his face, the faint seal, then his eyes. [0:12–0:26] on his eyes, then a slow drift to her: 花's face, her quiet steady gaze watching him; hold on her eyes. [0:26–0:30] hold on the gaze; cut on the whisper.

## Audio Prompt

Almost silent — 境 has no sound. No speech; 花 says nothing, 送り火 says nothing — he does not yet speak her name. At the pull, the boundary's own voice, near and far, trembling, speaks the refrain with its added punctuation: この魂は、まだ、誰にも、名付けられていない。. No wind, no rain, no footsteps, no breathing, no ambient bed. Music extremely sparse — a few sustained tones at most — falling away entirely as the refrain trembles, leaving only the trembling voice. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no mirror, no reflection, no doubling of the two faces, no resemblance between the man and the girl, no same person, no split self as a clone, no on-screen text, no subtitles, no captions, no wind, no rain, no environmental sound, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no watermark, no morphing or drifting facial identity, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no narration text, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no moving shadows, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-ch08-seg02-30s-01`
- Segment ID: `S11`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_08_捨てる, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 6s / 14s / 4s. Seeing = BEAT 3 at 14s (47%)`
- Camera Events: `4 events as listed in §10. Behind the back → around to his face → to her eyes`
- Action Events: `ACT_HOLD → ACT_TURN_AROUND → ACT_SEE`
- Audio Events: `no dialogue ／ the trembling refrain (定型句・震え) ／ total silence otherwise`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the whisper`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The model may make 花 resemble 送り火.** The gaze is intimate; the model may render her as his reflection. The negative prompt front-loads this.
- **The model may have 送り火 speak her name.** The naming 「花」 is S12. Verify no dialogue.
- **The gaze may read as pricing.** The eye must look, not measure — no ledger, no scale, no appraisal in the frame.
- **The tremor may render as extra text.** The refrain is a trembling voice, never a subtitle. Verify no caption.

## Changes

- _(none yet)_

## Next Generation

- If the gaze reads well, carry its stillness into S12, where the eyes close the device down and the mouth opens to name her.
