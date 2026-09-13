# Wan 3.0 Full Specification — 一皿ができるまで 第1章「粉屋の棚」Clip 1/10 / 3s

⚠️ **この作品の最初のショットである。** ここで決まることは2つ——**顔を映さないこと**と、
**棚の袋に文字が無いこと**である。以後、この2つは戻らない。
⚠️ **`mode: motion` である。** 主題は**光**であり、光は動く。
⚠️ **止まっているのは棚のほうである。** 決定（2026-09-13、著者）——
**止まるのは主題であって、画面ではない。** ここでは**光と粉塵が動き、棚が動かない。**

---

# 1. VIDEO

- Duration: `3s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the morning light stops being general and picks out one shelf.

# 2. WORLD

## World Concept

Flour, water, salt, and time. The film opens in the mill — the place the flour comes from — and the light is what chooses.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame.
- Light is the subject; the room is what the light falls on.
- The oven interior is not shown until it is opened. It is not shown here.
- The crumb is not shown until the loaf is broken. It is not broken here.
- No lettering is legible anywhere — not on the sacks, not anywhere.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject. The shelf exists in order to be selected by the light.
- Color Language: Magenta and gold against deep cyan shadow, the same palette the whole film carries. Here it is at its most diffuse — the light is not yet aimed.
- Texture: Layered atmospheric depth. Flour dust suspended in the beam and individually rendered; no grain, no paper texture, no painterly stroke.
- Rendering: Hyper-detailed layered light — volumetric shaft from the window, bloom and anamorphic flare around the source. Two-step cel on the hands; the light drawn continuously.
- Visual Density: Low. Sacks, a beam of light, dust.
- Time: `朝`
- Atmosphere: Early, quiet, and not yet directed at anything.

# 3. SUBJECTS

## The Hands

- Reference: `hitosara-baker-character-sheet`
- Appearance: Hands and a coarse linen apron. Weathered, flour on them, no ring, no watch.
- Behavior: At the end of the shot a hand enters the frame and takes one sack. It does not take two.
- Continuity Requirements: Same hands, same apron, no drift.

# 4. ENVIRONMENT

- Location: `MILL`
- Environment Elements: Wooden shelving, one shelf per row, sacks of flour standing on them. A window at the frame edge. A hanging balance and the way out, at the edges of the room.
- Environmental Behavior: The light moves slowly across the shelves and settles on one. Dust falls through it the whole time.

# 5. OBJECTS

- `KONA` — the sacks of flour. Fine particles; where the light catches a seam, dust lifts off it.
- No other object is in frame. No oven, no bread, no bowl.

# 6. REFERENCES

- REF_CHARACTER: `hitosara-baker-character-sheet` (HIGH)
- REF_LOCATION: `hitosara-mill-board-dawn` (HIGH)
- REF_GEOGRAPHY: `hitosara-mill-geography` (MEDIUM)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The light picks out one shelf, and a hand takes from that shelf.
- Beginning: The whole shelf rack, evenly lit, nothing chosen.
- Turn: The beam moves and one row becomes brighter than the others.
- Peak: The chosen shelf, with dust rising in the beam.
- Pull: A hand enters and closes on a sack. The shot ends before it lifts.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — The full rack. Sacks in rows, none of them readable. The light falls but has not chosen.
  - BEAT 2 `2-3s` — density: `held` — The beam edges sideways and one row brightens. Dust rises into it. A hand enters.
- Temporal Density: The held beat carries the meaning and is the shortest — the shot is decided in its last second.

# 9. ACTION

- `ACT_TRAVEL` — Before: the light lies across all the shelves. After: it lies across one.
- `ACT_TAKE` — Before: nothing has been taken. After: a hand is closed on a sack.

# 10. CAMERA

- Camera Language: Third-person, at the height of the shelves, the rack filling the frame. Almost no depth of field; the light does the separating.
- Camera Events: `0-2s` wide on the rack. `2-3s` a very slow drift with the beam, ending with the hand entering frame.
- Camera Behavior: Nearly still. A slow weighted settle, no handheld, no whip. One continuous take; no cut.

# 11. MOTION

## Subject Motion

The light is the subject and the light moves — a slow crawl across the rack, then a lateral settle onto one row. It does not flicker and it does not swing.

## Object Motion

The shelves and the sacks do not move. Nothing on the rack is displaced except by the hand at the end.

## Environmental Motion

Flour dust falls through the beam continuously and is individually rendered. The dust keeps moving through both beats, including the beat where nothing else happens.

## Physical Characteristics

- Weight: The light has no weight; the sacks have all of it.
- Inertia: The light comes to rest without overshoot. The shelf never moves at all.
- Acceleration: Constant, very slow, with a single gentle deceleration as it settles.
- Fluidity: The beam behaves as a volume of air, not as a shape pasted over the frame.
- Impact: None.

# 12. EMOTION

- Emotional Arc: The moment an undifferentiated room becomes a room with a direction.
- Emotional Events: The instant one shelf is brighter than its neighbours.

# 13. LIGHTING

- Base Lighting: Morning, from a window at the frame edge. Cool in the shadow, gold in the beam.
- Lighting Events: The beam narrows onto one shelf at `2s` and stays there. No second light appears and no light is switched on.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: A room that is empty of people. A hand on cloth at the very end. Nothing else.
- Music: One sustained tone, entering under BEAT 2.
- Environment: A mill with no clock in it.

# 15. CONTINUITY

- Identity: The hands and apron follow the character sheet. No face, no body, no ring, no watch.
- Visual: The palette is the film's palette at its most diffuse; this is the only shot in the mill.
- Motion: Full animation, not limited — the atmosphere is the primary mover and here the light is the atmosphere.
- Sound: Dry, close, small.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 粉 レンジより）

- No human face. No full body of the baker. No second person.
- No wall clock, no calendar, no digital timer.
- No oven interior, no visible flame, no glow through the door seam — the oven is not in this shot.
- No cut loaf, no visible crumb, no cross-section — the loaf is not broken yet.
- **No readable text of any kind** — and in particular no readable text on the sacks.
- No brand label, no packaging text.
- No kitchen appliance with a display.

## MUST

- Full animation. The light crawls and the dust falls for the whole shot.
- The face stays out of frame even as the hand enters.

## PREFER

- The chosen shelf in the lower third, with the rack above it still in shadow.

## ALLOW

- A single sack taken, and only one.

# 17. GENERATION PRIORITIES

1. **No legible lettering** — on the sacks or anywhere. This outranks beauty.
2. **The light is the only thing that moves** — the shelf does not shift, sway or breathe.
3. **The face stays out** — the hand enters at the frame edge and the arm is never followed up.
4. **One sack** — a hand taking two sacks is a different shot with a different meaning.
5. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 3-second continuous cinematic take (16:9), luminous realist anime, in a flour mill in the morning, at a wooden rack of flour sacks. Beats, deliberately uneven: [0-2s] the whole rack is evenly lit and nothing has been chosen, the sacks in rows and none of them readable; [2-3s] the light edges sideways and one row brightens, dust rising into the beam, and a hand enters the frame and closes on one sack. The light is the subject; the shelf does not move. The palette is magenta and gold against deep cyan shadow, at its most diffuse. (No face, no clock, no legible lettering anywhere.)

## Visual Prompt

Luminous realist anime. Magenta and gold against deep cyan shadow, diffuse and not yet aimed. Hyper-detailed layered light — a volumetric shaft from a window at the frame edge, bloom and anamorphic flare around the source, flour dust suspended in the beam and individually rendered rather than a flat wash. A wooden rack of flour sacks in rows, one shelf per row, the sacks coarse and unmarked. A hanging balance and the way out at the edges of the room, out of focus. Two-step cel on the hands; the light rendered continuously. Low visual density. No human face, no full body, no second person. No readable text, no lettering on the sacks, no brand label, no packaging text, no oven interior, no visible flame, no cut loaf, no visible crumb, no torn-open loaf, no cross-section, no wall clock, no calendar, no digital timer, no kitchen appliance with a display, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited. The light is the primary mover: it crawls slowly across the rack and settles laterally onto one row, with one gentle deceleration and no overshoot. Flour dust falls through the beam continuously and is individually rendered. The shelf and the sacks do not move at all. A hand enters at the frame edge and closes on one sack. No impact, no collision, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, at the height of the shelves, the rack filling the frame. Nearly still — a slow weighted settle with the beam, no handheld, no whip, no shake. [0-2s] wide on the rack. [2-3s] a very slow drift ending with the hand entering frame. One continuous take; no cut.

## Audio Prompt

No dialogue. A room empty of people. A hand on cloth, once, at the very end. Music: one sustained tone entering under the second beat. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover and here the atmosphere is the light itself: it crawls continuously and never holds. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg01-3s-01`
- Segment ID: `01-1`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `3s`
- References: `REF_CHARACTER (hitosara-baker-character-sheet, HIGH) ／ REF_LOCATION (hitosara-mill-board-dawn, HIGH) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `2 beats, NON_UNIFORM — 2s / 1s. The choosing = BEAT 2 at 1s (33%)`
- Camera Events: `2 events as listed in §10. One continuous take`
- Action Events: `ACT_TRAVEL → ACT_TAKE`
- Audio Events: `no dialogue ／ one hand on cloth ／ sustained tone`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Lettering may appear on the sacks.** It is the most likely failure in this shot and the one that matters most — a readable word here breaks the film's rule in its first second.
- **The shelf may move.** It must not. A rack that shifts or breathes turns a light-as-subject shot into a camera-as-subject shot.
- **The light may flicker.** It crawls; it does not flicker and does not swing.
- **Two hands may enter.** One sack, one hand.
