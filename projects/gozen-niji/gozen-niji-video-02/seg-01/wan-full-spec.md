# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第2話 S06「雰囲気変わった？」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「美月の開く指を、妙に細かく見る」——他人の指へ初めて視線が折れる（指の背骨の第6本）。ニジは不在（送信済みの文字としてのみ。S06には文字すら無い）。登場人物は真白と美月（美月はこの回の初出）。画面文字なし（美月の表情と問い）。最大の秒は「雰囲気変わった？」の問いと、遅れた笑いに。**

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold one turn (one dramatic beat) of a 57-part light-novel animation into a single 30-second take that ends on its pull`
- Register: `Restrained. The horror and the tenderness are both delivered by ordinary objects and withheld reaction, never by performance`
- Rule: `One turn = one generation. The arc is distributed across 57 takes; nothing is added after the pull`

---

# 2. WORLD

## World Concept

- Concept: `Contemporary Japan, unchanged in every visible way — except that a screen-time log records time as a receipt for time deposited with other people`
- Era: `Present day`
- Location: `A high-school student's small bedroom; her school; occasionally a corridor, a classroom, a festival yard`
- Time: `The story lives at 2:00 A.M. Daytime exists only as the shore on either side of it`
- Weather: `Clear and still. Nothing outside ever comments on the events`
- Atmosphere: `Absolute domestic ordinariness. The anomaly never disturbs a single physical object`

## World Rules

- The supernatural is **recorded, not staged**. Its evidence is text on a screen.
- The phone's light is the sole light source at night. It does not flicker, pulse, or behave unnaturally.
- Nothing in the physical world reacts to the anomaly — no wind, no moving shadows, no disturbed objects.
- Notifications are **silent**. They arrive as light only.
- ニジ never leaves the screen.

## Visual Language

- Art Direction: `Soft cel anime — flat color planes, clean closed thin lineart, soft-edged shadow terminators`
- Color Language: `Muted, low-saturation. Night = desaturated indigo lit by one cold blue-white screen. Day = pale, slightly overexposed, equally muted. The screen's blue-white is the only value allowed to be bright — and, from seg.10, ニジ's rainbow is the only hue allowed to be saturated`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces`
- Rendering: `Two-step cel shading with softened terminators; gentle bloom around the phone screen; light haze in the dark air`
- Visual Density: `Low. Simple uncluttered rooms, generous negative space, one focal point per beat`

---

# 3. SUBJECTS

## MASHIRO

- ID: `MASHIRO`
- Name: `真白 (Mashiro)`
- Type: `CHARACTER`
- Role: `Protagonist — the one who deposited the time`

### Appearance

- Japanese high-school girl, 16–17, second year. Deliberately unremarkable — the girl slightly outside the middle of the circle.
- Shoulder-length dark hair, a thin neck; small frame; quiet face that gives little away. 「真白」is blankness, not whiteness — an undecorated stillness, not white hair.
- Back curved from long hours over a phone; the memory of the screen's light on her face.
- At night: plain pajamas, in a futon on the floor. By day: standard Japanese school uniform, white collar.
- **Solid and real — she casts a shadow in the scene.** (The contrast anchor: ニジ, her copy, has none.)

### Behavior

- Personality: `Inward, observant, agreeable on the surface. Reads the room and matches it. Small voice`
- Typical Motion: `Almost nothing moves except her fingers. Her body stays still far more than it moves`
- Emotional Range: `Narrow and suppressed. She does not scream, gasp, or widen her eyes. Her reactions register as stillness — a finger stopping, a held breath`

### Continuity Requirements

- Must preserve: `face, shoulder-length hair and color, the thin neck, build, age; the curved posture; the same phone (same size, same case); the same futon, room layout, window and curtain; the restraint — her expression never resolves into a clear readable emotion`

> **美月 appears this segment**（best friend — bright, direct; sees through 真白's lie but does not press it）. ニジ is absent（ledger 06–09 — the ghost exists only as sent text）.

---

# 4. ENVIRONMENT

## Location

- ID: `CLASSROOM`
- Name: `教室 (the classroom)`
- Description: `Ordinary Japanese classroom, morning light making long thin shadows across desks`

## Environmental Behavior

- Wind: `none — the curtain does not move`
- Particles: `only the faintest haze catching the screen's bloom; no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; at most one distant car's headlights crossing the curtain, once`

---

# 5. OBJECTS

## PHONE

- Type: `smartphone`
- Appearance: `真白's ordinary modern smartphone, plain case, Japanese UI. The only light source at night; the only surface on which the anomaly appears. Glass carries a soft bloom, never a hard specular glint`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
- Continuity Importance: `CRITICAL`

## SCREEN_TEXT

- Type: `UI text`
- Appearance: `No message text this segment — the disclosure is 美月's face and question, not text. 美月's chat app opens, but no message is shown (the sent words belong to S07)`
- Narrative Importance: `LOW`
- Visual Importance: `LOW`
- Continuity Importance: `LOW`

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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_02_おまえが言えなかった、たった一言.md`
- Priority: `CRITICAL`
- Defines: `every event, the exact on-screen text, the ending line, and what is and is not revealed`

## REF_BIBLE

- Type: `BIBLE`
- Source: `soul-voice-teller/examples/gozen-niji/台帳/series-bible.md`
- Priority: `CRITICAL`
- Defines: `the staged disclosure, the voice rules, and the addressee ledger`

## REF_CHARACTER

- Type: `CHARACTER`
- Source: `gozen-niji-mashiro-character-sheet/prompt.md ／ gozen-niji-niji-character-sheet/prompt.md`
- Priority: `HIGH`
- Defines: `the locked character design — 真白 (solid, real, casts a shadow) and ニジ (her copy, one step younger, no shadow, a rainbow afterimage blue → green → blue)`

---

# 7. NARRATIVE

## Core Event

Morning classroom. 美月, at the next seat, suddenly says 「なんか、雰囲気変わった？」 — and 真白's heart nearly stops. She answers with her usual smile, a beat too late.

## Beginning

Window light lays long thin shadows across the desks. The sound of prints handed along, a pen rolling off a desk. 真白 at her seat, notebook open, still turning last night over.

## Turn

「なんか、雰囲気変わった？」 — sudden, close. 真白's heart stops. ――ばれた？ 「変わってないよ」 — she smiles as always, but the smile comes half a second late. 美月's head tilts; something in it is not the same as yesterday.

## Peak

美月 opens her chat — that way of opening, the thumb stroking the screen. 真白's eyes stay on that finger, minutely, as if it were her own hand moving.

## Pull（引き — 切れ目）

Cut on the finger — 美月's thumb beginning to stroke the screen, and 真白's gaze fixed on it, too long. The question 「雰囲気変わった？」 is left hanging; the chat she is opening holds something 真白 has not seen yet.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The question and the delayed smile hold 10s (33%); the watched finger is held 6s.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the morning classroom; the question and its delayed smile are their own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「朝の教室」 — ESTABLISH.** Morning light, long thin shadows across the desks. Prints handed along; a pen rolls off a desk. 真白 at her seat, notebook open, thinking about last night. _Density: SPARSE — quiet daylight, no event._
- **BEAT 2 `[0:06–0:16]` — 「雰囲気変わった？」 — longest share.** 美月, at the next seat, suddenly: 「なんか、雰囲気変わった？」 真白's heart stops. ――ばれた？ 「変わってないよ」 — the smile arrives half a second late. 美月's head tilts; something in it is not the same as yesterday. _Density: DENSE at the head, then held on the face._
- **BEAT 3 `[0:16–0:24]` — 「開く指」.** 美月 opens her chat — the thumb stroking the screen. 真白's eyes stay on that finger, minutely, as if it were her own. _Density: TRANSITION — one insert, the finger, quiet._
- **BEAT 4 `[0:24–0:30]` — 「見る」 — held, then cut.** 真白's gaze, fixed on the finger, too long. The thumb begins to stroke the screen. Cut on the finger. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the question 「雰囲気変わった？」 (≈0:08) ／ the delayed smile (≈0:12) ／ 美月's thumb beginning to stroke the screen (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the classroom), 0:24–0:30 (the held gaze)`
- Dense regions: `0:06–0:16 (the question and the late smile)`
- Long continuous action: `0:24–0:30 真白 watching the finger, held`
- Rapid transitions: `none — a slow, held morning`

---

# 9. ACTION

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MITSUKI`
- Action: `Leans in from the next seat, head tilted, and asks 「なんか、雰囲気変わった？」`
- Intention: `Not suspicion — noticing. She means it lightly`
- Intensity: `Low`
- Speed: `Ordinary, bright`

### Action Relationship

- Before: `—`
- After: `ACT_DEFLECT`

## Action — ACT_DEFLECT

- ID: `ACT_DEFLECT`
- Subject: `MASHIRO`
- Action: `Answers 「変わってないよ」 with her usual smile — which arrives half a second late`
- Intention: `To match the room, as always. The delay is the whole event`
- Intensity: `Medium, internal`
- Speed: `Nothing, then the smile, whole and late`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_OPEN`

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MITSUKI`
- Action: `Opens her chat app — the thumb strokes the screen smoothly`
- Intention: `To check something she half-remembers`
- Intensity: `Low`
- Speed: `Practiced, smooth — the same arc 真白 knows in her own hand`

### Action Relationship

- Before: `ACT_DEFLECT`
- After: `ACT_WATCH`

## Action — ACT_WATCH

- ID: `ACT_WATCH`
- Subject: `MASHIRO`
- Action: `Eyes stay on 美月's finger, minutely, too long — as if it were her own hand`
- Intention: `Not to spy — to recognize. The gesture is hers`
- Intensity: `Medium, suppressed`
- Speed: `Still; only the eyes move`

### Action Relationship

- Before: `ACT_OPEN`
- After: `— (cut on the finger)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, at desk height. Two-shot, then closer`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Shallow — 美月 sharp, the classroom soft behind`
- Camera Style: `Slow, deliberate, almost still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Static two-shot at desk level: 美月 in the next seat, 真白 behind, the window light laying long shadows across the desks.
- **`[0:06–0:12]`** — Cut to 真白, static, close. Hold through the question and the half-second gap before the smile arrives.
- **`[0:12–0:16]`** — Cut to 美月, static, close. Her head tilts — something in it is not the same as yesterday.
- **`[0:16–0:20]`** — Insert: 美月's thumb on glass, macro-close, only the fingertip sharp.
- **`[0:20–0:26]`** — Rack focus from the finger up to 真白's eyes, still watching it.
- **`[0:26–0:30]`** — Hold on 真白's gaze fixed on the finger, then the finger itself beginning to stroke. Cut on the finger.

---

# 11. MOTION

## Subject Motion

- 真白's body holds; her face is still until the late smile, which arrives whole, a beat behind
- The late smile is a two-stage hold — nothing, then the expression, complete
- 美月's head tilts once, then her thumb strokes the screen open in a smooth practiced arc
- Only the eyes move in the last beats; everything else is held

## Object Motion

- The phone moves only as 美月's thumb strokes it open — ordinary UI motion, no glitch, no flicker
- The pen rolls off a desk once, early, and stops
- The classroom is alive in soft, out-of-focus movement — papers, distant students

## Environmental Motion

- Morning light is still; long thin shadows lie unmoving across the desks
- No wind, no moving shadows, no particles

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in 美月's hand`
- Inertia: `High for the bodies, near-zero for the thumb`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Ordinary morning (the classroom, unbothered)
- ↓ Concealment (the heart that nearly stops, answered with a late smile)
- ↓ Unease (美月's head tilts with something different in it)
- ↓ Fixation (the eyes that will not leave 美月's finger)

## Emotional Events

- Event: `「なんか、雰囲気変わった？」`
  Emotion: `Concealment — the heart stopping, the smile a beat late`
  Intensity: `MEDIUM, entirely internal`
  Timing: `≈0:08`

- Event: `美月's head tilts with something different in it`
  Emotion: `Unease — she has noticed`
  Intensity: `MEDIUM`
  Timing: `≈0:14`

- Event: `真白 watches 美月's finger, minutely`
  Emotion: `Fixation — recognizing her own gesture on another hand`
  Intensity: `MEDIUM, suppressed`
  Timing: `0:20–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Pale flat classroom daylight from the left windows — soft, slightly overexposed`
- Fill Light: `Even, flat. The classroom is bright and unbothered`
- Rim Light: `A faint cool edge along 真白's hair from the window`
- Ambient Light: `Day. Muted, low-saturation, nothing dramatic`
- Color Temperature: `≈5600K pale daylight, slightly overexposed, muted like the whole series`

## Lighting Events

- **`[0:00]`** — Morning light already full; long thin shadows lie across the desks.
- **`[0:06–0:16]`** — The light on 真白's face is flat and even — her expression is the only thing that changes.
- **`[0:16–0:24]`** — A faint screen-glow rises on 美月's face as the chat opens.
- **`[0:24–0:30]`** — Light unchanged. Cut on the finger.

---

# 14. AUDIO

## Dialogue

- 美月: 「なんか、雰囲気変わった？」 — bright, close, sudden
- 真白: 「変わってないよ」 — light, and half a second late

> No other speech. No narration, no voice-over.

## Sound Effects

- Morning classroom: prints handed along, a pen rolling off a desk, chairs, distant corridor voices
- The soft friction of a thumb on glass, once, as 美月 opens the chat
- The room is full and ordinary — the world is loud and unbothered

## Environment

- Day. Full and ordinary classroom ambience — unbothered, unmenacing

## Music

- Style: `Sparse — a few sustained tones, or nothing`
- Tempo: `Slow`
- Mood: `Ordinary, gentle. Never sinister, never sentimental`
- Emotional Function: `Hold the morning's ordinary surface under the concealment. It thins as 美月 opens the chat, leaving only room tone and the thumb's friction`

---

# 15. CONTINUITY

> 57本は57回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

- **Identity**: 真白 — plain Japanese high-school girl 16–17, shoulder-length dark hair, thin neck, small frame, curved posture over a phone. Same face in every take.
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen.
- **The room**: futon on the floor, curtained window, wall clock, sparse.
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light.
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue.
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。

## MUST

- The smile at 「変わってないよ」 arrives **visibly late** — roughly half a second of nothing before the mouth moves
- 美月's head-tilt carries "something different from yesterday" — a noticing, never a suspicion
- Establish that 真白 watches 美月's finger minutely — the gesture that mirrors her own
- Keep the morning light pale, flat, slightly overexposed, and muted
- End on 美月's finger beginning to stroke the screen, cut on the finger

## MUST NOT（この1本の禁止・開示台帳 06–09 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person, no eyes, no hand but the two girls' own. ニジ does not appear in this episode
- **No rainbow, no iridescence, no colored afterimage.** Her color is introduced later; showing it here destroys her arrival
- **No on-screen text in this segment.** 美月's chat app opens, but no message is shown — the sent words belong to S07
- **No voice for the ghost.** There is no text yet, and nothing is read aloud
- Do not make 美月 sinister, doubtful, or knowing — she is bright and unguarded
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The late smile over the heart-stopping reaction — the face stays still until the smile
- Silence over score as the chat opens
- Negative space over detail; the classroom may be nearly empty

## ALLOW

- Slight variation in classroom background students and desk arrangement
- The pen-rolling detail may be omitted if it distracts
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not be shown (ledger 06–09 — the ghost exists only as sent text); no rainbow, no eyes, no voice for the ghost; 美月 alone appears beside 真白. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school classroom in the morning. Beats, deliberately uneven: [0:00–0:06] pale flat daylight lays long thin shadows across the desks, prints handed along, a pen rolling off a desk, 真白 at her seat with her notebook open; [0:06–0:16] 美月 at the next seat suddenly asks なんか、雰囲気変わった？ and 真白's heart nearly stops, and she answers 変わってないよ with a smile that arrives half a second late, and 美月 tilts her head with something different in it; [0:16–0:24] 美月 opens her chat, her thumb stroking the screen, and 真白's eyes stay on that finger minutely; [0:24–0:30] 真白's gaze holds on the finger as it begins to stroke the screen, and the shot cuts on the finger. The question and the late smile hold the largest share. Ends on the finger, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. By day she wears a standard Japanese school uniform. Scene: a Japanese high-school classroom in the morning, pale flat daylight from the left windows laying long thin shadows across the desks, slightly overexposed and equally muted. Beside her, 美月 (Mitsuki) — her best friend, bright and direct, with slightly shorter, livelier hair and an open upright posture, in the same uniform. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Bodies hold; only small movements. 真白's late smile is a two-stage hold — nothing, then the expression arrives whole, a half second behind. 美月's head tilts once, then her thumb strokes the screen open in a smooth practiced arc. In the last beats only the eyes move. A pen rolls off a desk once, early, and stops. The classroom is alive in soft out-of-focus movement. The phone moves only as 美月's thumb strokes it open — ordinary UI motion, no glitch, no flicker. Gentle acceleration everywhere. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, at desk height. Longish lens, shallow depth of field; 美月 sharp, the classroom soft behind. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] static two-shot at desk level, 美月 in the next seat, 真白 behind, window light laying long shadows. [0:06–0:12] cut to 真白, static, close; hold through the half-second gap before the smile. [0:12–0:16] cut to 美月, static, close; her head tilts with something different in it. [0:16–0:20] insert, macro-close on 美月's thumb on glass, only the fingertip sharp. [0:20–0:26] rack focus from the finger up to 真白's eyes, still watching. [0:26–0:30] hold on 真白's gaze, then the finger beginning to stroke; cut on the finger.

## Audio Prompt

Day. Full and ordinary classroom ambience — prints handed along, a pen rolling off a desk, chairs, distant corridor voices. Two lines of dialogue only: 美月 asks なんか、雰囲気変わった？ bright and sudden; 真白 answers 変わってないよ, light and half a second late. The soft friction of a thumb on glass, once, as 美月 opens the chat. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as the chat opens, leaving only room tone and the thumb's friction. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep02-seg01-30s-01`
- Segment ID: `S06`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_02, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 10s / 8s / 6s. Question + late smile = BEAT 2 at 10s (33%)`
- Camera Events: `6 events as listed in §10. One insert, one rack focus; all else static or held`
- Action Events: `ACT_ASK → ACT_DEFLECT → ACT_OPEN → ACT_WATCH`
- Audio Events: `two lines of dialogue ／ thumb-on-glass once ／ sparse music thinning`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the finger`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- *(none yet — to be filled after the first generation)*

## Anticipated risks (to check in the first generation)

- **The late smile lands on time.** If the half-second gap is not visible, the opening beat has no content. Check first; if it reads as on-time, lengthen the hold before the smile.
- **美月 reads as sinister.** If her head-tilt or smile is ambiguous, the episode inverts into horror and loses its subject. She must be bright and unguarded.
- **The model may add a ghost.** "2 A.M." is a strong prior. The negative prompt front-loads the no-ghost clause; verify frame by frame — no figure, no eyes, no rainbow.
- **The watched finger may not read as the subject.** The whole point is 真白's gaze on 美月's gesture. If it reads as a casual glance, hold the rack focus on 真白's eyes longer.

## Changes

- *(none yet)*

## Next Generation

- If the late smile and the watched finger both read, this segment is done; the reveal of S07 depends on this finger being established as a motif.
