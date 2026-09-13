# Wan 3.0 Full Specification — 一皿ができるまで 第1章「粉と水」Clip 2/10 / 2s

⚠️ **この作品でいちばん短いショットである。** 2秒——**触れた瞬間だけが速く、あとは滲む。**
⚠️ **主題は界面そのものである。** 粉の山は動かない。**動くのは水の側である。**
⚠️ **`02` の画像仕様は拡大であり、`04` の画像仕様は中景である。** 同じ「粉と水」でも
**尺度が違う**——この動画仕様は**02 の側**（界面の拡大）である。

---

# 1. VIDEO

- Duration: `2s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: two substances stop being two.

# 2. WORLD

## World Concept

Flour, water, salt, and time. Here the film states its first fact: flour and water do not mix by being put together — they mix when the water reaches every grain.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame.
- Light is the subject; here it is what makes the boundary legible at all.
- The oven interior is not shown until it is opened. It is not shown here.
- The crumb is not shown until the loaf is broken. It is not broken here.
- Salt is not in this shot. Salt comes later.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject. This is the film's only true macro shot, and the light is what gives the grains their edges.
- Color Language: Magenta and gold against deep cyan shadow. The water carries a cooler note than the flour, and that difference is the whole picture.
- Texture: Layered atmospheric depth. Every grain separately rendered; the film is at its densest here and nowhere else.
- Rendering: Hyper-detailed layered light — one volumetric shaft from a window at the frame edge, a shallow depth of field so that only the boundary is in focus, the wet grains catching a specular on each face.
- Visual Density: The highest in the film — and it is held for less than a second.
- Time: `朝`
- Atmosphere: Close, quiet, and the only shot where the room is not visible.

# 3. SUBJECTS

## The Hands

- Reference: `hitosara-baker-character-sheet`
- Appearance: Hands and a coarse linen apron. Only the fingertips are in frame, at the edge, and they are still.
- Behavior: The fingertips rest and do not stir. This shot is not about the hand.
- Continuity Requirements: Same hands, same apron, no drift.

## The Water

- Reference: `MIZU.appearance`
- Appearance: Water pooling on the flour — a film first, then a boundary.
- Behavior: It spreads into the flour. It does not splash, does not drip from a height, and does not run.
- Continuity Requirements: The same vessel, the same water, in every shot.

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: A wooden bench, flour heaped on it, and the light of a window at the frame edge. Nothing else is in focus.
- Environmental Behavior: The dust falls; the light does not move within the shot's short span.

# 5. OBJECTS

- `KONA` — the flour, heaped, its grains separate and countable at the start.
- `MIZU` — the water, as a film over the flour and then as a boundary inside it.
- No other object is in frame: no salt, no bowl, no tool.

# 6. REFERENCES

- REF_CHARACTER: `hitosara-baker-character-sheet` (MEDIUM)
- REF_LOCATION: `hitosara-kitchen-board-morning` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (LOW — the room is not visible)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The water reaches the flour and the boundary between them stops existing.
- Beginning: The apex of a heap of flour seen at a very shallow angle, grains separate.
- Turn: The water touches.
- Peak: The film spreads and the edges of the grains go out one after another.
- Pull: What is left is one damp mass where there were two things.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-1s` — density: `sparse` — The apex of the heap at a very shallow angle. The grains are separate and countable.
  - BEAT 2 `1-2s` — density: `dense` — The water touches. The film spreads and the grain boundaries go out. Density rises only for this second.
- Temporal Density: The dense beat is short on purpose. The shot exists to make one instant slow enough to see.

# 9. ACTION

- `ACT_SETTLE` — Before: the water lies on the surface. After: the water is inside the flour.
- `ACT_DISSOLVE` — Before: the boundary is sharp. After: there is no boundary.

# 10. CAMERA

- Camera Language: Third-person, macro, at the height of the bench surface. The depth of field is shallow so that only the boundary is in focus.
- Camera Events: `0-1s` hold on the apex. `1-2s` an almost imperceptible push of a few millimetres as the water lands.
- Camera Behavior: Nearly still. No handheld, no whip, no rack focus. One continuous take; no cut.

# 11. MOTION

## Subject Motion

The subject is the boundary and the boundary is what moves — the water's edge advances into the flour and the sharp line becomes a gradient.

## Object Motion

The heap of flour does not move. It is not stirred, not pressed, and not displaced.

## Environmental Motion

Flour dust falls through the beam continuously and is individually rendered. It keeps moving through both beats.

## Physical Characteristics

- Weight: The water has weight and it sits; the flour takes it without collapsing.
- Inertia: The film stops advancing where the flour stops taking it. There is no overshoot and no run-off.
- Acceleration: Fast at the instant of contact, then slowing as it soaks — the only acceleration in the shot.
- Fluidity: The water moves as a film wetting a surface, not as a body of liquid.
- Impact: None visible. The contact is quiet.

# 12. EMOTION

- Emotional Arc: The first fact of the film, stated small.
- Emotional Events: The moment the sharp boundary is gone.

# 13. LIGHTING

- Base Lighting: Morning, from a window at the frame edge. A single shaft, shallow and raking, so that each wet grain face carries a specular.
- Lighting Events: None. The light holds still for the full two seconds.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: A very small sound of water meeting powder. The room is otherwise silent.
- Music: None. This shot is the one place the score is absent.
- Environment: A room with no clock in it.

# 15. CONTINUITY

- Identity: The fingertips follow the character sheet — no face, no body, no ring, no watch.
- Visual: The palette is the film's palette at its densest. This is the only macro shot in the film.
- Motion: Full animation, not limited — the primary mover is the boundary itself, and here the subject is the mover.
- Sound: Close, dry, small.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 仕込み レンジより）

- No human face. No full body of the baker. No second person.
- No wall clock, no calendar, no digital timer.
- No oven interior, no visible flame, no glow through the door seam — the oven is not in this shot.
- No cut loaf, no visible crumb, no cross-section — the loaf is not broken yet.
- No readable text of any kind.
- No brand label, no packaging text.
- No kitchen appliance with a display.
- **No salt** — salt is not in this shot.
- No water splash, no drops flying in the air, no running tap.

## MUST

- Full animation. The boundary advances and the dust falls for the whole shot.
- The heap of flour does not move.

## PREFER

- The boundary across the centre of the frame, the wet side and the dry side both readable.

## ALLOW

- One visible specular on a single wet grain face.

# 17. GENERATION PRIORITIES

1. **The flour does not move** — a stirred or pressed heap is a different shot.
2. **The water does not splash** — it wets. A splash turns a macro into an action shot.
3. **No legible lettering** — on anything that appears in frame.
4. **Only two substances** — no salt, no bowl, no tool enters the macro.
5. **Grains, not texture** — the film's rule is that particles are individually rendered, and this shot is where that rule is most visible.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 2-second continuous cinematic macro take (16:9), luminous realist anime, on a wooden bench in a one-room bakery in the morning, at the boundary between flour and water. Beats, deliberately uneven: [0-1s] the apex of a heap of flour seen at a very shallow angle, the grains separate and countable; [1-2s] the water touches, the film spreads, and the grain boundaries go out one after another until there is no boundary left. The heap does not move; the water does not splash. The palette is magenta and gold against deep cyan shadow, at its densest. (No face, no clock, no salt in frame, no legible lettering anywhere.)

## Visual Prompt

Luminous realist anime macro. Magenta and gold against deep cyan shadow, the densest in the film. Hyper-detailed layered light — one volumetric shaft from a window at the frame edge, a shallow depth of field so only the boundary is in focus, flour dust suspended in the beam and individually rendered, every grain separately drawn and every wet grain face carrying one specular. A wooden bench surface, flour heaped on it. Two-step cel on the fingertips at the frame edge; the light rendered continuously. The water is cooler in tone than the flour and that difference is the picture. No human face, no full body, no second person. No salt, no bowl, no tool, no water splash, no drops flying in the air, no running tap. No readable text, no brand label, no packaging text, no oven interior, no visible flame, no cut loaf, no visible crumb, no torn-open loaf, no cross-section, no wall clock, no calendar, no digital timer, no kitchen appliance with a display, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited. The boundary is the primary mover: the water's edge advances into the flour, fast at the instant of contact and then slowing as it soaks, until the sharp line becomes a gradient. The heap of flour does not move — it is not stirred, not pressed, not displaced. Flour dust falls through the beam continuously. No splash, no drip, no run-off, no overshoot, no impact, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, macro, at the height of the bench surface, shallow depth of field so that only the boundary is in focus. Nearly still — no handheld, no whip, no shake, no rack focus. [0-1s] hold on the apex. [1-2s] a push of a few millimetres as the water lands. One continuous take; no cut.

## Audio Prompt

No dialogue. A very small sound of water meeting powder, once. Silence otherwise. Music: none — the score is absent for this shot. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, no salt, no salt shaker, no water splash, no drops flying in the air, no running tap, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover, and here the moving atmosphere is the water's edge itself: it advances continuously and never holds. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg02-2s-01`
- Segment ID: `01-2`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `2s`
- References: `REF_CHARACTER (hitosara-baker-character-sheet, MEDIUM) ／ REF_LOCATION (hitosara-kitchen-board-morning, HIGH) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `2 beats, NON_UNIFORM — 1s / 1s. The contact = BEAT 2 at 1s (50%)`
- Camera Events: `2 events as listed in §10. One continuous take`
- Action Events: `ACT_SETTLE → ACT_DISSOLVE`
- Audio Events: `no dialogue ／ one contact ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The water may splash.** It wets; it does not splash and does not fall from a height. A splash is the most likely failure and it changes the shot's meaning.
- **The heap may be stirred.** Nothing presses or displaces the flour in this shot; that is `04`'s job, not this one.
- **Salt may appear.** It is the natural thing for a model to add to a bowl of flour and water. It is not in this shot.
- **Grains may become texture.** At macro scale the film's rule about individually rendered particles is what separates this shot from a stock photograph of flour.
