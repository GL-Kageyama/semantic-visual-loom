# Wan 3.0 Full Specification — 一皿ができるまで 第1章「窯」Clip 8/10 / 5s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。** 投入の仕方は同じディレクトリの `README.md` を見よ。

⚠️ **開示の第1点である。** ここで窯が開く——§18 `Negative Prompt` から
`no oven interior`・`no visible flame`・`no glow through the door seam` の
**3節が落ちる**。以後どのショットでも戻らない。**禁止が消えることは、
モデルがそれを描いてよいことである。** 台帳がこの位置に変化点を宣言している（`L10` が検算する）。
⚠️ **この落ちる3節は、04・06 の §18 には在る。** 比較の相手は直前の動きのショットであり、
間に静的なショットが挟まっていても跨いで比べる（`L14`）。

---

# 1. VIDEO

- Duration: `5s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: what was behind the iron door is now in front of it.

# 2. WORLD

## World Concept

Flour, water, salt, and time. The oven is where the time closes. Until this shot, the oven has been a closed iron door and nothing else.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame.
- Light is the subject — and here, the fire is the light source itself.
- The oven interior is not shown until it is opened. **This is the shot where it opens.**
- The crumb is not shown until the loaf is broken. It is not broken here.
- The fire does not spread and does not go out.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject. Here the light is a fire and there is almost nothing else.
- Color Language: The palette narrows. Gold and black; the magenta of the earlier shots is gone. The cyan exists only in the unlit half of the room.
- Texture: Layered atmospheric depth. Flour dust suspended, and burning as it crosses the flame. No grain, no paper texture, no painterly stroke.
- Rendering: Hyper-detailed layered light — bloom and anamorphic flare around the fire, which is the only permitted source. Particles suspended and visible against the dark.
- Visual Density: Low, and darker than any other shot in the film.
- Time: `明け方`
- Atmosphere: Warm, narrow, and the brightest dark in the film.

# 3. SUBJECTS

## The Hands

- Reference: `hitosara-baker-character-sheet`
- Appearance: The same hands and the same coarse linen apron. Here they are lit from below by the fire, and the apron's shadow moves on the wall.
- Behavior: The hands open the door and then leave the frame. They do not reach into the oven.
- Continuity Requirements: Same hands, same apron, no drift.

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: The wood-fired oven in the far wall; its iron door on iron hinges. The stone floor in front of it, dusted with flour. The window behind, blue and going gold. Hanging flour dust.
- Environmental Behavior: The window light changes from blue to gold during the shot. The fire does not change size. The dust falls through the fire's light.

# 5. OBJECTS

- `KAMADO` — the iron door, its hinges, the fire behind it. **The door is the subject of the first beat.**
- No other object is in frame: the bench, the bowl and the tools are out of frame by now.

# 6. REFERENCES

- REF_CHARACTER: `hitosara-baker-character-sheet` (HIGH)
- REF_LOCATION: `hitosara-kitchen-board-before-dawn` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (MEDIUM)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The door opens and the fire is simply there.
- Beginning: An iron door, closed, with one line of light at the seam.
- Turn: The door turns on its hinges.
- Peak: The fire. It does not change; it simply is visible.
- Pull: Dust crosses the flame and burns, and that is the only thing that happens.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-1.5s` — density: `transition` — The iron turns. The inside is still not visible. One line of light lengthens from the seam.
  - BEAT 2 `1.5-4s` — density: `held` — The fire. It does not move; it wavers.
  - BEAT 3 `4-5s` — density: `sparse` — Dust crosses in front of the flame and burns. Nothing else happens.
- Temporal Density: The held beat holds the largest share — and it is the one where nothing moves.

# 9. ACTION

- `ACT_OPEN` — Before: the door is shut. After: the door is open.
- `ACT_HOLD` — Before: the fire is hidden. After: the fire is seen.
- `ACT_CROSS` — Before: dust is falling. After: dust is falling and one mote of it has burned.

# 10. CAMERA

- Camera Language: Third-person, at the height of the door. The fire is the subject and the frame is built around it; the room falls away.
- Camera Events: `0-1.5s` medium, the closed door and the seam of light. `1.5-4s` hold as the door opens, the fire taking the center. `4-5s` hold on the fire with the dust crossing it.
- Camera Behavior: Almost still. A very slow, weighted settle; no handheld, no whip. One continuous take; no cut.

# 11. MOTION

## Subject Motion

The fire does not travel. It wavers — short tongues, quickly, in place.

## Object Motion

The iron door turns on its hinges and stops. Nothing else moves.

## Environmental Motion

Flour dust falls continuously and crosses in front of the flame, burning as it does. The window light changes from blue to gold. Both keep moving through every beat.

## Physical Characteristics

- Weight: The door has weight; the fire has none.
- Inertia: The door stops when it is stopped. The fire never stops.
- Acceleration: The door accelerates once at the start of its swing.
- Fluidity: The flame moves as a body of gas, not as a shape pasted on.
- Impact: None.

# 12. EMOTION

- Emotional Arc: The moment a closed thing becomes an open one.
- Emotional Events: The instant the fire is no longer hidden.

# 13. LIGHTING

- Base Lighting: Night giving way to dawn. The window is blue at the start and gold at the end.
- Lighting Events: The fire becomes the dominant source the instant the door passes the seam. From that point the room is lit from below.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: The iron hinge, once. The low breath of the fire, continuous. Nothing else.
- Music: One sustained tone, held under the whole shot.
- Environment: A room with no clock in it.

# 15. CONTINUITY

- Identity: The hands and apron follow the character sheet. The oven is the same oven, in the same wall, on the same side of frame as in every previous shot.
- Visual: From this shot onward the oven interior is a permitted element. The palette narrows to gold and black.
- Motion: Full animation, not limited — and here the fire replaces the dust as the primary mover.
- Sound: The hinge is dry; the fire is low.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 窯 レンジより）

- No human face. No full body of the baker. No second person.
- No wall clock, no calendar, no digital timer.
- **The oven interior is no longer forbidden.** It is the subject of this shot.
- No cut loaf, no visible crumb, no cross-section — the loaf is not broken here.
- No readable text of any kind.
- No hand reaching into the oven.

## MUST

- Full animation. The fire wavers and the dust falls for the entire shot.
- The fire must be the only light source from the moment the door opens.

## PREFER

- The fire in the lower half of the frame, with the dark above it.

## ALLOW

- A single mote of flour burning as it crosses the flame.

# 17. GENERATION PRIORITIES

1. **The withheld crumb** — no cut loaf, no crumb, no cross-section. This outranks beauty.
2. **The fire is the only source** — no window light on the fire itself, no second light in the room.
3. **The fire does not travel** — it wavers in place. A fire that moves is a different shot.
4. **The hands leave** — nothing reaches into the oven.
5. **One mote burns** — a single mote, not a shower of sparks.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 5-second continuous cinematic take (16:9), luminous realist anime, in a one-room bakery with no clock in it, at the wood-fired oven in the far wall. Beats, deliberately uneven: [0-1.5s] the iron door is shut and one line of light lengthens along the seam; [1.5-4s] the door turns on its hinges and the fire is simply there, taking the center of the frame, wavering in place; [4-5s] a mote of flour dust crosses in front of the flame and burns, and nothing else happens. The fire is the only light source from the moment the door opens; the room is lit from below. The palette narrows to gold and black. (No face, no clock — and the oven interior is permitted in this clip; it is the subject.)

## Visual Prompt

Luminous realist anime. The palette narrows: gold and black, with the magenta of earlier shots gone and deep cyan only in the unlit half of the room. Hyper-detailed layered light — bloom and anamorphic flare around the fire, which is the only permitted source; flour dust suspended and visible against the dark. A wood-fired oven set into a far wall, its iron door on iron hinges. A stone floor dusted with flour. A window behind, blue going gold. Two-step cel on the hands; the light rendered continuously. Low visual density, and darker than any other shot in the film. No human face, no full body, no second person. No hand reaching into the oven. No cut loaf, no visible crumb, no torn-open loaf, no cross-section. No wall clock, no calendar, no readable text, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited — the fire replaces the dust as the primary mover. The flame wavers in place with short tongues; it does not travel, does not spread, and does not go out. The iron door turns on its hinges, accelerates once, and stops. Flour dust falls continuously and crosses in front of the flame, and one mote burns. The window light changes from blue to gold. No impact, no collision, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, at the height of the door. The fire is the subject and the frame is built around it; the room falls away. Almost still — a very slow, weighted settle; no handheld, no whip, no shake. [0-1.5s] medium, the closed door and the seam of light. [1.5-4s] hold as the door opens and the fire takes the center. [4-5s] hold on the fire with the dust crossing it. One continuous take; no cut.

## Audio Prompt

No dialogue. The iron hinge, once, dry. The low breath of the fire, continuous. Music: one sustained tone held under the whole shot. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover, and here the fire is the atmosphere: it wavers continuously and never holds. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg08-5s-01`
- Segment ID: `01-8`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `5s`
- References: `REF_CHARACTER (hitosara-baker-character-sheet, HIGH) ／ REF_LOCATION (hitosara-kitchen-board-before-dawn, HIGH) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 1.5s / 2.5s / 1s. The fire = BEAT 2 at 2.5s (50%)`
- Camera Events: `3 events as listed in §10. One continuous take`
- Action Events: `ACT_OPEN → ACT_HOLD → ACT_CROSS`
- Audio Events: `no dialogue ／ one hinge ／ sustained tone`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The fire may travel.** It must waver in place; a fire that crosses the frame is a different shot with a different meaning.
- **A second light may be invented** — a lamp, a glow on the wall, a rim light on the hands from the window. From the instant the door opens the fire is the only source.
- **The crumb may appear.** The loaf is not broken in this shot; a cut loaf in frame is the failure to watch for here.
- **The oven interior may be rendered as a room.** It is a fire in a dark mouth, not a chamber with walls.
