# Wan 3.0 Full Specification — 一皿ができるまで 第1章「発酵」Clip 6/10 / 8s

⚠️ **この作品の主題である。** 時計は無く、時間は生地の側で進む。
⚠️ **§18 `Negative Prompt` は 04 と1節も違わない。** 開示の変化点は 08 にあり、
ここでは動かない。**動かないことは、応答していないことではない。**

---

# 1. VIDEO

- Duration: `8s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the dough stops being smaller than its container.

# 2. WORLD

## World Concept

Flour, water, salt, and time. There is no clock anywhere — time advances on the dough's side. The proof is where the time is actually carried.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame.
- Light is the subject. Flour dust floats in it.
- The oven interior is not shown until it is opened.
- The crumb is not shown until the loaf is broken.
- Nothing is pushed in this shot. What moves, moves by itself.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject.
- Color Language: A saturated palette of magenta and gold against deep cyan shadow. At midday the gold flattens and the cyan lifts.
- Texture: Layered atmospheric depth. Flour dust suspended and catching the light. No grain, no paper texture, no painterly stroke.
- Rendering: Hyper-detailed layered light — volumetric shafts, anamorphic flare and bloom around the source, particles suspended.
- Visual Density: Low. A bowl, a lid, and the light. Almost nothing else.
- Time: `昼`
- Atmosphere: Warm and still, and yet the air is visibly moving.

# 3. SUBJECTS

## The Dough

- Reference: (none — the dough is not a registered entity; it is the subject of the shot, not a character)
- Appearance: A pale, slightly damp mass under a linen lid. Its surface is matte at the start and becomes taut.
- Behavior: It does not seek. It only occupies more room than it did.
- Continuity Requirements: The mass must be continuous with the mass kneaded in the previous shot. No change of color, no change of scale.

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: A wooden bench. A wide ceramic bowl under a linen lid. One window. A wood-fired oven set into the far wall, its iron door closed. Hanging flour dust.
- Environmental Behavior: Dust is always falling. The window light crosses the bowl during the shot. The lid moves once, and only because the dough moves it.

# 5. OBJECTS

- `KONA` — the fine dust that has settled on the lid, sliding off when the lid lifts.
- The bowl and its linen lid. No other vessel is in frame.

# 6. REFERENCES

- REF_LOCATION: `hitosara-kitchen-board-midday` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (MEDIUM)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The dough takes up more room than it was given.
- Beginning: The bowl is larger than its contents.
- Turn: The surface rises without anything touching it.
- Peak: The dough touches the underside of the lid.
- Pull: The lid lifts a fraction, and flour slides off its rim.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — The bowl under its lid. Nothing is happening outside it.
  - BEAT 2 `2-5s` — density: `held` — The surface lifts by an amount you can see. The shadows of bubbles move inside.
  - BEAT 3 `5-7s` — density: `held` — The dough reaches the underside of the lid and keeps trying.
  - BEAT 4 `7-8s` — density: `dense` — The lid floats up a fraction; flour slides off the rim.
- Temporal Density: Two thirds of the shot is the second and third beats — the least eventful part of the film.

# 9. ACTION

- `ACT_SETTLE` — Before: the dough sits low. After: the dough fills the bowl.
- `ACT_RISE` — Before: the surface is flat. After: the surface is domed.
- `ACT_LIFT` — Before: the lid rests on the rim. After: the lid rests on the dough.

# 10. CAMERA

- Camera Language: Third-person, at the height of the bowl. The bowl and the light are the subject; the room is out of focus behind it.
- Camera Events: `0-2s` medium, the whole bowl. `2-7s` slowly closer, until the surface fills the lower half of the frame. `7-8s` hold on the rim as the flour slides.
- Camera Behavior: A slow, weighted push with commitment; no handheld, no whip. One continuous take; no cut.

# 11. MOTION

## Subject Motion

The dough rises. There is no visible cause — that is the point of the shot.

## Object Motion

The lid moves only when the dough reaches it. The flour on the lid slides when the lid moves.

## Environmental Motion

Flour dust falls continuously. The window light crosses the bowl. Both keep moving through every beat, including the held ones.

## Physical Characteristics

- Weight: The mass gains presence without gaining visible size.
- Inertia: It does not stop when the light stops moving.
- Acceleration: Almost none. This is the slowest motion in the film.
- Fluidity: The surface moves as a skin, not as a liquid.
- Impact: None.

# 12. EMOTION

- Emotional Arc: The patience of something that is not waiting.
- Emotional Events: The moment the dough touches the lid.

# 13. LIGHTING

- Base Lighting: Midday through one window. Flat gold over the bowl, cyan in the room behind.
- Lighting Events: The light crosses the bowl during the shot; the shadow of the rim travels across the dough.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: Almost none. A faint, dry tick as the lid lifts.
- Music: One sustained tone, held for the whole shot.
- Environment: A room with no clock in it.

# 15. CONTINUITY

- Identity: The cup of the bowl and the weave of the linen match the previous shot.
- Visual: Warm saturated light; deep cyan behind; flour dust in every frame.
- Motion: Full animation, not limited — the atmosphere moves first and never stops.
- Sound: The room tone is unbroken across the cut.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 発酵 レンジより）

- No human face. No full body of the baker. No second person.
- No hands in frame at all — nothing touches the dough in this shot.
- No wall clock, no calendar, no digital timer.
- No oven interior, no visible flame, no glow through the door seam.
- No cut loaf, no visible crumb, no cross-section.
- No readable text of any kind.

## MUST

- Full animation. The dust falls and the light moves for the entire shot.
- The rising must have no visible cause.

## PREFER

- The bowl slightly off-center, with the light source at the frame edge.

## ALLOW

- A single dry tick on the lid.

# 17. GENERATION PRIORITIES

1. **The withheld oven** — no oven interior, no flame, no seam glow. This outranks beauty.
2. **No cause** — no hand, no draft, no tool may appear to explain the rise.
3. **The light as subject** — flare and bloom belong to the source.
4. **The slow beat** — the held middle must hold the largest share.
5. **The atmosphere always moving** — dust falling even while the dough seems still.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

An 8-second continuous cinematic take (16:9), luminous realist anime, at a wooden bench in a one-room bakery with no clock in it. A wide ceramic bowl under a linen lid, flour dust hanging in the light. Beats, deliberately uneven: [0-2s] the bowl under its lid, nothing happening outside it; [2-5s] the dough's surface lifts by an amount you can see, the shadows of bubbles moving inside it; [5-7s] the dough reaches the underside of the lid and keeps trying; [7-8s] the lid floats up a fraction and flour slides off its rim. No hands and no tool enter the frame; the rise must have no visible cause. The light is the subject. (No face, no clock, no oven interior — the oven door stays closed in this clip.)

## Visual Prompt

Luminous realist anime. A saturated palette — magenta and gold in the lit half, deep cyan in the shadow — with the warm gold of the crust as the accent. Hyper-detailed layered light: volumetric shafts travelling through the air, anamorphic flare and bloom around the light source, flour dust suspended and catching the light. A wooden bench, one window, a wide ceramic bowl under a coarse linen lid with flour settled on it, a stone floor, the wood-fired oven in the far wall with its iron door closed. Low visual density: the bowl, the lid, and the light; almost nothing else. No human face, no full body, no second person, no hands at all. No oven interior, no visible flame, no glow through the oven door seam. No cut loaf, no visible crumb. No wall clock, no calendar, no readable text, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. Flour dust falls continuously and never settles; the window light crosses the bowl for the whole shot. The dough's surface rises as a skin, with almost no acceleration — the slowest motion in the film. The lid moves only once, and only because the dough reaches it; flour slides off the rim. No hand, no draft, no tool, no visible cause. No impact, no collision, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, at the height of the bowl. The bowl and the light are the subject; the room is soft behind it. A slow, weighted push with commitment; no handheld, no whip, no shake. [0-2s] medium, the whole bowl. [2-7s] slowly closer until the surface fills the lower half of the frame. [7-8s] hold on the rim as the flour slides. One continuous take; no cut.

## Audio Prompt

No dialogue. Almost no effects — a single faint dry tick as the lid lifts. Music: one sustained tone held for the whole shot. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: dust drifts and light shafts sweep continuously even when nothing else is happening. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg06-8s-01`
- Segment ID: `01-6`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `8s`
- References: `REF_LOCATION (hitosara-kitchen-board-midday, HIGH) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `4 beats, NON_UNIFORM — 2s / 3s / 2s / 1s. The rise = BEATS 2–3 at 5s (62%)`
- Camera Events: `3 events as listed in §10. One continuous take`
- Action Events: `ACT_SETTLE → ACT_RISE → ACT_LIFT`
- Audio Events: `no dialogue ／ one sustained tone`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **A hand may be added to explain the rise.** The negative and §17 both front-load it; verify frame by frame — this is the most likely failure of this shot.
- **The dough may be given a visible cause** (a draft, a tool, a light change) that reads as the reason it moves.
- **The shot may come back as a time-lapse.** It must be a continuous 8 seconds, not a compressed one.
