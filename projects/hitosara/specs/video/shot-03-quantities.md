# Wan 3.0 Full Specification — 一皿ができるまで 第1章「分量」Clip 3/10 / 5s

⚠️ **この作品で唯一の `composite` である。** 画は**層の合成**であり、
**文字は生成器が描かない**——焼くのは `timeline` の `text_events` である。
⚠️ **だからこのショットには、2種類の「動き」がある。**
生成の中の動き（光と粉塵）と、**編集の中の動き（文字の出現と保持）**である。
⚠️ **§11 は生成の側の運動だけを書く。** 文字は §11 に現れない——
**生成器は文字を知らない。** これを書かないと、モデルが数字を描く。

---

# 1. VIDEO

- Duration: `5s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: quantities that were nowhere are stated once, over a plate of ingredients that does not move.

# 2. WORLD

## World Concept

Flour, water, salt, and time. The film states its proportions once and never again — the numbers are not spoken by anyone and are not written by anyone in the room.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame.
- Light is the subject; the ingredients are what the light falls on.
- The oven interior is not shown until it is opened. It is not shown here.
- The crumb is not shown until the loaf is broken. It is not broken here.
- **No lettering is generated.** Any text in the finished clip is composited afterwards.
- The frame is neither pushed nor pulled. The subject holds.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject. This is the film's one diagrammatic shot and it is still lit like the rest.
- Color Language: Magenta and gold against deep cyan shadow. Three ingredients, three separate notes of the same palette.
- Texture: Layered atmospheric depth. Flour dust suspended above the heap; salt read as individual grains; the water film faintly reflective.
- Rendering: Hyper-detailed layered light — one volumetric shaft from a window at the frame edge, bloom and anamorphic flare around the source.
- Visual Density: Low, and deliberately so — **the right of the frame is left quiet and uncrowded**, because text is placed over it later.
- Time: `朝`
- Atmosphere: Exact, calm, and the only shot in the film that states a number.

# 3. SUBJECTS

## The Ingredients

- Reference: `KONA.appearance`, `MIZU.appearance`, `SHIO.appearance`
- Appearance: A heap of flour, a film of water, and a pinch of salt, arranged separately on a wooden bench so that all three are legible at once.
- Behavior: They do not move. Nothing is stirred, poured or combined in this shot.
- Continuity Requirements: Same bench, same morning light, same palette as every other shot in the kitchen.

## The Hands

- Reference: `hitosara-baker-character-sheet`
- Appearance: Not in frame. This shot has no hands in it.
- Behavior: —
- Continuity Requirements: Same hands and apron whenever they appear elsewhere; here they do not.

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: A wooden bench, the three ingredients on it, the light of a window at the frame edge, and the room falling away out of focus behind.
- Environmental Behavior: Nothing changes. The light holds its angle for the full five seconds.

# 5. OBJECTS

- `KONA` — a heap of flour, its grains separate where the light rakes across it.
- `MIZU` — water, as a still film in a shallow hollow of the flour.
- `SHIO` — salt, only as much as sits on a fingertip, and no fingertip in frame.
- No other object is in frame: no bowl, no tool, no scale, no oven.

# 6. REFERENCES

- REF_CHARACTER: `hitosara-baker-character-sheet` (LOW — no hands in frame)
- REF_LOCATION: `hitosara-kitchen-board-morning` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (MEDIUM)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The proportions are stated once, over a bench that does not move.
- Beginning: Three ingredients on a bench, in the morning light, with nothing said about them.
- Turn: Nothing turns. The shot holds.
- Peak: The held frame, with the dust moving through the beam and the ingredients exactly where they were.
- Pull: The ingredients are still there, still separate, and the shot ends.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-3s` — density: `held` — Flour, water and salt on the kneading bench. The frame does not move. Dust falls through the light.
  - BEAT 2 `3-5s` — density: `sparse` — The same frame, unchanged. The dust keeps falling. The light holds.
- Temporal Density: The held beat holds the largest share, and **nothing in it moves but the light and the dust.**

# 9. ACTION

- `ACT_HOLD` — Before: three ingredients lie separate. After: three ingredients lie separate. **The change is not in the picture.**
- `ACT_FALL` — Before: dust is falling. After: dust is falling. The only continuous action in the shot.

# 10. CAMERA

- Camera Language: Third-person, at the height of the bench, close enough that all three ingredients are legible. Static.
- Camera Events: None. The camera does not move for the full five seconds.
- Camera Behavior: Locked off. No handheld, no whip, no push, no pull, no rack focus. One continuous take; no cut.

# 11. MOTION

## Subject Motion

**The subject does not move.** The flour, the water and the salt hold exactly the position they are given for the entire five seconds. **The subject of this shot is a diagram, and a diagram that moves is not a diagram.**

## Object Motion

None. No object is displaced, lifted, poured or combined.

## Environmental Motion

**Light and dust are the only movers.** Flour dust falls through the beam continuously and is individually rendered, drifting very slowly across the quiet right side of the frame. The window light holds its angle but its bloom breathes slightly, so the frame is never a frozen still.

## Physical Characteristics

- Weight: Nothing is in motion, so nothing carries weight.
- Inertia: Absolute. Nothing that is still is disturbed.
- Acceleration: None.
- Fluidity: The dust behaves as individual grains in air, not as a haze.
- Impact: None.

# 12. EMOTION

- Emotional Arc: The calm of an exact thing.
- Emotional Events: None. This shot is the film's rest.

# 13. LIGHTING

- Base Lighting: Morning, from a window at the frame edge. A single raking shaft that makes each of the three ingredients read differently.
- Lighting Events: None. The angle is fixed; only the bloom breathes.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: The room, quiet. No handling, no pouring, no tools.
- Music: None. The score stays out, as it does in every still beat of the film.
- Environment: A room with no clock in it.

# 15. CONTINUITY

- Identity: Same bench, same light, same palette as every other kitchen shot.
- Visual: The palette is the film's palette; the composition reserves the right of the frame for text that will be composited later.
- Motion: Full animation, not limited — **the atmosphere is the primary mover, and here the atmosphere is the only mover.**
- Sound: Quiet, room tone only.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 仕込み レンジより）

- No human face. No full body of the baker. No second person. **No hands at all.**
- No wall clock, no calendar, no digital timer.
- No oven interior, no visible flame, no glow through the door seam — the oven is not in this shot.
- No cut loaf, no visible crumb, no cross-section — the loaf is not broken yet.
- **No readable text of any kind — and in particular no numerals, no units, no letters, no labels.** The text in the finished clip is composited afterwards and is not generated.
- No brand label, no packaging text.
- No kitchen appliance with a display, no scale, no measuring cup with markings.
- No salt shaker with a label, no pouring from height.

## MUST

- Full animation. The dust falls and the light breathes for the whole five seconds.
- **The ingredients hold their position exactly.** A hand, a stir, or a settled heap all break this shot.
- The right of the frame stays quiet and uncrowded.

## PREFER

- The three ingredients in the lower half, the light above them.

## ALLOW

- One faint specular on the water film.

# 17. GENERATION PRIORITIES

1. **No numerals, no units, no letters** — the single most likely failure, and the one that matters most. The quantities are composited, not generated.
2. **Nothing in the frame moves** except the light and the dust.
3. **No hands** — a hand entering here turns a diagram into an action.
4. **Three ingredients, separately legible** — a combined mass is a different shot.
5. **A quiet right side** — the text has to land somewhere.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 5-second continuous cinematic take (16:9), luminous realist anime, on a wooden kneading bench in a one-room bakery in the morning, with three ingredients laid out separately. Beats, deliberately uneven: [0-3s] flour, water and salt on the bench, the frame locked off, dust falling through the light; [3-5s] the same frame, unchanged, the dust still falling and the light holding. **Nothing in the frame moves but the light and the flour dust.** The subject holds. The palette is magenta and gold against deep cyan shadow. (No face, no clock, no hands, no numerals or lettering of any kind — the quantities are composited afterwards.)

## Visual Prompt

Luminous realist anime. Magenta and gold against deep cyan shadow. Hyper-detailed layered light — one volumetric shaft from a window at the frame edge, bloom and anamorphic flare around the source, flour dust suspended above the heap and individually rendered. A wooden kneading bench; a heap of flour with its grains separate where the light rakes across it; a still film of water in a shallow hollow of the flour; a pinch of salt read as individual grains. The right of the frame is left quiet and uncrowded. Low visual density. No human face, no full body, no second person, no hands. No numerals, no units, no letters, no readable text, no labels, no brand label, no packaging text, no scale, no measuring cup with markings, no salt shaker with a label, no oven interior, no visible flame, no cut loaf, no visible crumb, no torn-open loaf, no cross-section, no wall clock, no calendar, no digital timer, no kitchen appliance with a display, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited — and yet **the subject does not move.** The flour, the water and the salt hold exactly the position they are given for the entire shot; nothing is displaced, lifted, poured or combined. Light and flour dust are the only movers: the dust falls and drifts slowly across the quiet right side of the frame, and the bloom around the light source breathes. **The camera does not push, pull, pan or rack focus.** No hand enters. No impact, no collision, no motion blur smears, no stutter, **and no held frames in the sense of a frozen image** — the frame is alive with dust even when nothing else happens.

## Camera Prompt

Third-person, at the height of the bench, close enough that all three ingredients are legible. **Locked off, for the entire five seconds** — no handheld, no whip, no shake, no push, no pull, no rack focus, no drift. The composition places the three ingredients in the lower half and leaves the right of the frame quiet. One continuous take; no cut.

## Audio Prompt

No dialogue. Room tone only — no handling, no pouring, no tools, no footsteps. Music: none. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no numerals, no digits, no units of measure, no labels, no human face, no full body of the baker, no second person, no hands, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no scale, no measuring cup, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, no salt shaker, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover, and here the atmosphere is the dust and the breathing bloom: they move continuously and never hold. Camera moves with weight and commitment — which in this shot means it does not move at all, and holds its frame. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg03-5s-01`
- Segment ID: `01-3`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `5s`
- References: `REF_LOCATION (hitosara-kitchen-board-morning, HIGH) ／ REF_GEOGRAPHY (hitosara-kitchen-geography, MEDIUM) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `2 beats, NON_UNIFORM — 3s / 2s. The hold = BEAT 1 at 3s (60%)`
- Camera Events: `none. Locked off for the full duration`
- Action Events: `ACT_HOLD → ACT_FALL`
- Audio Events: `no dialogue ／ room tone ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`
- Compositing: `two text_events are burned over this clip by the timeline layer — 0.5-3.5s and 3.5-5.0s. They are not generated.`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Numerals may be drawn.** It is by far the most likely failure in this shot: the prompt describes quantities, and a model will want to write them. Any generated digit makes the composite double up.
- **A hand may enter and stir.** The shot is a diagram; a hand turns it into an action and destroys the only rest the film has.
- **The camera may drift.** A slow push is the default behaviour of a video model on a static scene. The frame is locked off here.
- **The heap may settle or the water may spread.** Both would be motion in the subject, and the subject is the one thing that must hold.
