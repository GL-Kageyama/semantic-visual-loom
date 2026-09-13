# Wan 3.0 Full Specification — 一皿ができるまで 第1章「夜明け」Clip 7/10 / 3s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。** 投入の仕方は同じディレクトリの `README.md` を見よ。

⚠️ **このショットは時刻を跨ぐ。** それでも `time` は単数（`明け方`）である——
**跨ぎは `unit` の対が持つ**（ショットは一時刻である。CLAUDE.md 固定方針）。
⚠️ **カメラは据えたまま、光だけが動く。** 主題は**光**であり、
**フレームは動かない**——転換は光が行う。
⚠️ **ここが開示の境界のいちばん際どいところである。** **扉は写ってよい。
扉の隙間から漏れる光は、写ってはならない。** この2つは同じ物の裏表であり、
**言葉にしなければ同じ絵になる。**

---

# 1. VIDEO

- Duration: `3s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the light in the room goes from blue to gold, and a hand puts fire into a closed oven.

# 2. WORLD

## World Concept

Flour, water, salt, and time. The night ends on the oven's side of the room — the film never says how long the proof took, and this shot is where that time is compressed into a colour.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame.
- Light is the subject; here it is the only thing that changes.
- The oven interior is not shown until it is opened. **It is not opened here** — the door stays shut and no light comes through it.
- The crumb is not shown until the loaf is broken. It is not broken here.
- The fire is put in, and that is all that happens to the oven in this shot.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject. **The palette shift is the shot.**
- Color Language: The hinge of the film. Deep blue in the upper half, warm magenta and gold already climbing the lower half, the shift visible as a single gradient across the stone floor.
- Texture: Layered atmospheric depth. Fine flour dust suspended in the beam; the stone floor and the iron door faintly reflective.
- Rendering: Hyper-detailed layered light — one volumetric shaft from the window travelling across the room and reaching the oven wall, bloom and anamorphic flare around the window.
- Visual Density: Low. The left of the frame is left quiet.
- Time: `明け方`
- Atmosphere: The moment the room becomes the morning.

# 3. SUBJECTS

## The Hands

- Reference: `hitosara-baker-character-sheet`
- Appearance: Hands and a coarse linen apron. Lit from the window, rimmed in blue at the start and in gold at the end.
- Behavior: The hands rest in front of the door, then move to put the fire in. They do not open the door.
- Continuity Requirements: Same hands, same apron, no drift.

## The Oven Door

- Reference: `KAMADO.appearance`
- Appearance: A closed iron door set into a far wall, on iron hinges.
- Behavior: **It does not move.** It is shut at the start of the shot and shut at the end of it.
- Continuity Requirements: The same oven, in the same wall, on the same side of frame as in every other shot.

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: The wood-fired oven in the far wall with its iron door; the stone floor in front of it, dusted with flour; a window behind, blue and going gold.
- Environmental Behavior: **The window light changes from blue to gold across the shot.** That is the environmental event and the only one.

# 5. OBJECTS

- `KAMADO` — the closed iron door, its hinges, and whatever is behind it. **The interior is not visible and no light escapes the seam.**
- No other object is in frame: no bowl, no bread, no flour sack.

# 6. REFERENCES

- REF_CHARACTER: `hitosara-baker-character-sheet` (HIGH)
- REF_LOCATION: `hitosara-kitchen-board-before-dawn` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (MEDIUM)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The room changes colour and the fire is lit behind a closed door.
- Beginning: A blue room, a shut oven, and a pair of hands stopped in front of it.
- Turn: The window goes from blue to gold.
- Peak: The gold reaching the stone floor.
- Pull: The hands put the fire in and come away; the door is still shut.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-1.5s` — density: `transition` — The window is blue. The oven door is shut. The hands are stopped in front of it.
  - BEAT 2 `1.5-3s` — density: `transition` — The window is gold. The hands move and put the fire in. **The door is still shut.**
- Temporal Density: Both beats are `transition` and they carry equal weight — the shot is one continuous shift with no held beat at all.

# 9. ACTION

- `ACT_LIGHT` — Before: the window is blue. After: the window is gold.
- `ACT_KNEAD` — Before: the hands are stopped. After: the hands have put the fire in and come away. **The door is not touched.**

# 10. CAMERA

- Camera Language: Third-person, at the height of the door, the door on the same side of frame as in every other shot, the window inside the frame.
- Camera Events: None. **The camera is set down and left.** The transition is performed by the light, not by the frame.
- Camera Behavior: Locked off for the full three seconds. No handheld, no whip, no push, no pull, no rack focus. One continuous take; no cut.

# 11. MOTION

## Subject Motion

**The subject is the light, and the light changes.** The window's colour moves from blue to gold as a single continuous gradient, and the boundary between the cool upper half and the warming lower half travels down the room.

## Object Motion

The iron door does not move — not on its hinges, not in the frame. The hands move once, at `1.5s`, and then are still.

## Environmental Motion

The light travels across the room, down the wall and onto the stone floor. Fine flour dust falls through the beam continuously and is individually rendered. **Both keep moving through every beat.**

## Physical Characteristics

- Weight: The light has no weight; the door has all of it.
- Inertia: The colour shift does not overshoot and does not reverse. It goes one way.
- Acceleration: Constant. There is no instant in this shot where the change is sudden.
- Fluidity: The light moves as a volume of air travelling across a room, not as a gradient pasted on the frame.
- Impact: None.

# 12. EMOTION

- Emotional Arc: Overnight becomes morning without anyone deciding it.
- Emotional Events: The instant the stone floor takes the gold.

# 13. LIGHTING

- Base Lighting: Before dawn, changing to morning. The window is blue at the start and gold at the end.
- Lighting Events: One — the shift. **No other light appears**: the fire put in at `1.5s` is behind a closed door and gives the room nothing.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: The room at night, then the room at morning. The fire, once, behind the door — muffled. Nothing else.
- Music: One sustained tone that does not resolve.
- Environment: A room with no clock in it.

# 15. CONTINUITY

- Identity: The hands and apron follow the character sheet. The oven is the same oven, in the same wall, on the same side of frame as in every other shot.
- Visual: The palette is the film's hinge — this is the only shot where the two halves of the palette are both present.
- Motion: Full animation, not limited — **the atmosphere is the primary mover and here it is the entire cast.**
- Sound: Dry, low, and the fire is muffled by iron.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 窯 レンジより）

- No human face. No full body of the baker. No second person.
- No wall clock, no calendar, no digital timer. **The passage of the night must not be measured by anything in the frame.**
- **No glow through the door seam.** The door is permitted; light escaping it is not. This is the most fragile constraint in the shot.
- No oven interior. No visible flame. **The fire is behind a closed door in this shot.**
- No cut loaf, no visible crumb, no cross-section — the loaf is not broken yet.
- No readable text of any kind.
- No brand label, no packaging text.
- No kitchen appliance with a display.
- No hand reaching into the oven, and no hand opening the door.

## MUST

- Full animation. The colour shift and the dust continue for the whole three seconds.
- **The camera does not move.**
- The oven door does not move.

## PREFER

- The door in the same position in frame as in every other shot, with the window inside the frame.

## ALLOW

- One faint reflection of the gold on the stone floor.

# 17. GENERATION PRIORITIES

1. **No light at the door seam** — this outranks beauty. A closed door with a warm line under it is the single most likely failure and it reveals the shot's withheld thing one shot too early.
2. **No flame, no interior** — there is fire, and it is behind iron. It is not visible.
3. **The camera does not move** — the transition is the light's, not the frame's.
4. **The door does not move** — it stays shut. It is opened in the next shot, not this one.
5. **One continuous gradient** — not two colour grades cut together.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 3-second continuous cinematic take (16:9), luminous realist anime, in a one-room bakery with no clock in it, at the wood-fired oven in the far wall before dawn. Beats, deliberately uneven: [0-1.5s] the window is blue, the iron oven door is shut, and a pair of hands is stopped in front of it; [1.5-3s] the window goes gold, the hands move and put the fire in behind the closed door and come away. **The camera does not move; the light is what changes**, as one continuous gradient down the room. The palette is the film's hinge: deep blue in the upper half, warm magenta and gold climbing the lower half. (No face, no clock — and **no light escapes the door seam**; the oven interior is not visible in this clip.)

## Visual Prompt

Luminous realist anime. **The palette is the hinge of the shot** — deep blue still in the upper half, warm magenta and gold already climbing the lower half, the shift visible as a single gradient across the stone floor. Hyper-detailed layered light — one volumetric shaft from the window travelling across the room and reaching the oven wall, bloom and anamorphic flare around the window, fine flour dust suspended in the beam and individually rendered. A closed iron oven door set into a far wall, on iron hinges, with **no light at the seam**. A stone floor dusted with flour and faintly reflective where the light reaches it. Two-step cel on the hands; the light rendered continuously. Low visual density; the left of the frame is quiet. No human face, no full body, no second person. No glow through the door seam, no visible flame, no oven interior. No readable text, no brand label, no packaging text, no cut loaf, no visible crumb, no torn-open loaf, no cross-section, no wall clock, no calendar, no digital timer, no kitchen appliance with a display, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited. The light is the primary mover: the window's colour travels from blue to gold as one continuous gradient, and the boundary between the cool upper half and the warming lower half moves down the room and onto the stone floor. Fine flour dust falls through the beam continuously. **The camera does not move. The iron door does not move** — not on its hinges, not in the frame. The hands move once and are still. No impact, no collision, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, at the height of the door, the door on the same side of frame as in every other shot, the window inside the frame. **Locked off for the full three seconds** — no handheld, no whip, no shake, no push, no pull, no rack focus, no drift. **The transition is performed by the light, not by the frame.** One continuous take; no cut.

## Audio Prompt

No dialogue. The room at night, then the room at morning. The fire, once, behind the door — muffled by iron. Nothing else. Music: one sustained tone that does not resolve. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no light under the door, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover, and here the atmosphere is the light itself: it shifts continuously from blue to gold and never holds. Camera moves with weight and commitment — which in this shot means it holds its frame absolutely. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg07-3s-01`
- Segment ID: `01-7`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `3s`
- References: `REF_CHARACTER (hitosara-baker-character-sheet, HIGH) ／ REF_LOCATION (hitosara-kitchen-board-before-dawn, HIGH) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `2 beats, NON_UNIFORM — 1.5s / 1.5s, both transition. No held beat`
- Camera Events: `none. Locked off for the full duration`
- Action Events: `ACT_LIGHT → ACT_KNEAD`
- Audio Events: `no dialogue ／ one muffled fire ／ sustained tone`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`
- Compositing: `one text_event is burned over this clip by the timeline layer — 0-3s. It is not generated.`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Light may appear at the door seam.** This is the failure to watch for above all others: it is the natural way to render "there is fire inside", and it reveals the withheld interior one shot before the film opens it.
- **The door may open.** It stays shut. It is opened in `08`, and only there.
- **The shift may be cut rather than continuous.** Two colour grades must not read as two shots; the gradient has to travel.
- **The camera may drift.** On a three-second static shot a slow push is the model's default and it would steal the transition from the light.
