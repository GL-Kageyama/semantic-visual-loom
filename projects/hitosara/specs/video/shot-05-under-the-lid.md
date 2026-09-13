# Wan 3.0 Full Specification — 一皿ができるまで 第1章「蓋の下」Clip 5/10 / 4s

⚠️ **この作品で唯一の `still` である。** このショットの内容は**「何も起きない」**ことである。
⚠️ **だが、止まるのは主題であって、画面ではない。** 決定（2026-09-13、著者）——
**動くのは光と粉塵だけ**である。様式 `luminous-anime` の `Motion character` は
「held frame を禁ずる」と言うが、**これは衝突ではない**——
禁じているのは**止まった絵**であって、**止まった主題**ではない。
⚠️ **だから §11 は空にできない。** 空にすれば、**止まっているのか書き忘れたのかが分からない。**
⚠️ **この1本は最も失敗しやすい。** モデルは空白を埋めたがる——**余白は、指示しなければ空白にならない。**

---

# 1. VIDEO

- Duration: `4s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. **No change in the subject.** The change is in the viewer: what was unseen becomes something that is being watched, and stays unseen.

# 2. WORLD

## World Concept

Flour, water, salt, and time. This is the shot where time is passing and nothing shows it — the dough is under the cloth and the film refuses to look under it.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame.
- Light is the subject; here the light crosses a lid and the lid does not answer.
- The oven interior is not shown until it is opened. It is not shown here.
- The crumb is not shown until the loaf is broken. It is not broken here.
- **The dough is not shown before it is shown.** Not under the cloth, not through it, not as a silhouette on it.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject. This shot is the film's emptiest frame and it is lit like every other.
- Color Language: Magenta and gold against deep cyan shadow, with generous negative space. The linen reads almost white where the light crosses it.
- Texture: Layered atmospheric depth. Fine flour dust suspended in the beam and individually rendered; the linen's weave legible where the light rakes across it.
- Rendering: Hyper-detailed layered light — one volumetric shaft from a window at the frame edge, bloom and anamorphic flare around the source.
- Visual Density: The lowest in the film. **The emptiness is the subject.**
- Time: `朝`
- Atmosphere: Waiting, and nothing is coming.

# 3. SUBJECTS

## The Bowl and its Lid

- Reference: `KITCHEN.base`, `KONA.appearance`
- Appearance: A wide ceramic bowl under a coarse linen cloth, flour settled on the cloth from earlier handling.
- Behavior: The cloth does not lift, twitch, breathe or settle. **The cloth is not the subject of a motion; it is the subject of a non-motion.**
- Continuity Requirements: The same bowl and the same cloth that appear in `04` and `06`. Here the cloth is at rest.

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: A wooden bench, the covered bowl on it, the light of a window at the frame edge, the room falling away out of focus.
- Environmental Behavior: The light travels slowly across the linen from one edge to the other over the full four seconds. That travel is the only large motion in the frame.

# 5. OBJECTS

- `KONA` — flour settled on the linen, and the dust in the air.
- No other object is in frame: **no hand, no tool, no cloth beside it, no second object, no crumb, no steam, no water.**

# 6. REFERENCES

- REF_CHARACTER: `hitosara-baker-character-sheet` (LOW — no hands in frame)
- REF_LOCATION: `hitosara-kitchen-board-morning` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (MEDIUM)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: **None.** That is the event.
- Beginning: A covered bowl, and light arriving from the window.
- Turn: None. The shot refuses the turn.
- Peak: The moment the light finishes crossing the linen and nothing has happened.
- Pull: The bowl is exactly as it was. The shot ends on an unchanged frame.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2.5s` — density: `held` — Only the covered bowl is in frame. The light comes from the window and moves; the cloth does not.
  - BEAT 2 `2.5-4s` — density: `held` — Still nothing. Dust crosses the beam. That is all that moves.
- Temporal Density: Both beats are `held`, and they are held at the same pressure — **the shot has no accent, on purpose.** An accent would be an event.

# 9. ACTION

- `ACT_WAIT` — Before: the bowl is covered and nothing is happening. After: the bowl is covered and nothing has happened. **`before` and `after` look the same, and they are not the same.**

# 10. CAMERA

- Camera Language: Third-person, low and close to the bowl, the bowl slightly off centre with the light source at the frame edge.
- Camera Events: None. The camera does not move for the full four seconds.
- Camera Behavior: Locked off. **A camera that drifts here would supply the event the shot is refusing.** No handheld, no whip, no push, no pull, no rack focus. One continuous take; no cut.

# 11. MOTION

## Subject Motion

**The subject does not move.** The cloth lies exactly as it lies for all four seconds: it does not lift, twitch, breathe, settle or fall. **This shot's subject is that nothing happens, and a cloth that moves would make something happen.**

## Object Motion

None. No object is displaced or disturbed. The bowl is not nudged, the cloth is not adjusted.

## Environmental Motion

**Light and dust are the only movers.** The window light travels slowly across the linen from one edge to the other, so that the brightest part of the cloth is in a different place at the end than at the start. Fine flour dust falls through the beam continuously and is individually rendered, crossing the frame at its own pace. **Both keep moving through every beat** — the frame is never frozen, even though nothing in it happens.

## Physical Characteristics

- Weight: The cloth has the weight of cloth resting on a rim; it is not taut and it is not floating.
- Inertia: Absolute. Nothing that is still is disturbed.
- Acceleration: None in the subject. The light's travel is constant.
- Fluidity: The dust behaves as individual grains in air, not as a haze.
- Impact: None.

# 12. EMOTION

- Emotional Arc: The patience of a thing that is not being watched and is being watched anyway.
- Emotional Events: None. **The absence of an event is the emotional event**, and it must not be supplied by the model.

# 13. LIGHTING

- Base Lighting: Morning, from a window at the frame edge. One raking shaft, warm gold on linen, deep cyan in the room behind.
- Lighting Events: None discrete — the shaft's bloom breathes and the pool of light travels, and that is all.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: Room tone, and nothing else. No cloth, no ceramic, no handling.
- Music: One sustained tone held under the entire shot, with no swell and no resolution.
- Environment: A room with no clock in it.

# 15. CONTINUITY

- Identity: Same bowl, same cloth, same bench as `04` and `06`. Same hands and apron whenever they appear; here they do not.
- Visual: The palette is the film's palette at its emptiest. The composition carries the most negative space of any shot in the film.
- Motion: Full animation, not limited — **the atmosphere is the primary mover, and here the atmosphere carries the entire shot.**
- Sound: Quiet, held, unresolved.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 発酵 レンジより）

- No human face. No full body of the baker. No second person. **No hands at all.**
- No wall clock, no calendar, no digital timer. **Time must not be made visible in this shot by any means.**
- No oven interior, no visible flame, no glow through the door seam — the oven is not in this shot.
- No cut loaf, no visible crumb, no cross-section — the loaf is not broken yet.
- No readable text of any kind.
- No brand label, no packaging text.
- No kitchen appliance with a display.
- **No steam** — steam is the explanation that something is happening under the cloth, and this shot is about not being shown that.
- **No water** — water in frame turns "nothing has happened yet" into "something is already happening".
- No hand, no tool, no second object, no crumb.

## MUST

- Full animation. The light travels across the linen and the dust falls, for the entire four seconds.
- **The cloth does not move.** Not a lift, not a twitch, not a breath, not a settle.

## PREFER

- The bowl in the lower half, generous space above it.

## ALLOW

- One grain of flour sliding off the crown of the cloth as the light reaches it — **a grain, not the cloth.**

# 17. GENERATION PRIORITIES

1. **The cloth does not move** — this outranks everything. A cloth that lifts is a different shot.
2. **No steam, no water, no hand** — each of them supplies an event the shot is refusing.
3. **The frame is not frozen** — the light and the dust must keep moving; a still image is a failure of a different kind.
4. **The camera is locked off** — a slow push is the model's default on a static scene and it would invent the accent this shot does not have.
5. **Emptiness** — the model will want to fill the frame. Left unfilled, this is the film's only rest that is a rest in the subject too.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 4-second continuous cinematic take (16:9), luminous realist anime, on a wooden bench in a one-room bakery in the morning, on a wide ceramic bowl under a coarse linen cloth. **Nothing happens.** Beats, deliberately even: [0-2.5s] only the covered bowl is in frame, the light coming from the window and moving across the linen, the cloth not moving; [2.5-4s] still nothing, dust crossing the beam, the cloth still not moving. **The subject holds; only the light and the flour dust move.** The palette is magenta and gold against deep cyan shadow, with the most negative space in the film. (No face, no clock, no hands, no steam, no water.)

## Visual Prompt

Luminous realist anime. Magenta and gold against deep cyan shadow, with generous negative space and the linen reading almost white where the light crosses it. Hyper-detailed layered light — one volumetric shaft from a window at the frame edge, bloom and anamorphic flare around the source, fine flour dust suspended in the beam and individually rendered, the linen's weave legible where the light rakes across it. A wide ceramic bowl under a coarse linen cloth with flour settled on the cloth, on a wooden bench, the room falling away out of focus behind. The scene is emphatically empty. Low visual density; the emptiness is the subject. No human face, no full body, no second person, no hands, no steam, no water, no tool, no second object, no crumb, no readable text, no brand label, no packaging text, no oven interior, no visible flame, no cut loaf, no visible crumb, no torn-open loaf, no cross-section, no wall clock, no calendar, no digital timer, no kitchen appliance with a display, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited — **and the subject does not move.** The cloth lies exactly as it lies for all four seconds: it does not lift, twitch, breathe, settle or fall. **Light and flour dust are the only movers**: the window light travels slowly across the linen so that the brightest part of the cloth is in a different place at the end than at the start, and fine dust falls through the beam continuously, crossing the frame at its own pace. **The camera does not push, pull, pan or rack focus.** No hand enters. No impact, no collision, no motion blur smears, no stutter, **and no frozen held frame** — the frame is alive with light and dust while nothing happens.

## Camera Prompt

Third-person, low and close to the bowl, the bowl slightly off centre with the light source at the frame edge. **Locked off for the entire four seconds** — no handheld, no whip, no shake, no push, no pull, no rack focus, no drift. **A drifting camera would supply the event this shot is refusing.** One continuous take; no cut.

## Audio Prompt

No dialogue. Room tone and nothing else — no cloth, no ceramic, no handling, no footsteps. Music: one sustained tone held under the entire shot, with no swell, no sting, no resolution, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no hands, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, no steam, no water, no tool, no crumb, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover, and here the atmosphere carries the whole shot: the light travels and the dust falls continuously and never hold. Camera moves with weight and commitment — which in this shot means it holds its frame absolutely. No stutter, no shooting on threes, and **no held frame in the sense of a frozen image** — the frame must stay alive with light and dust while the subject does nothing. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg05-4s-01`
- Segment ID: `01-5`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `4s`
- References: `REF_LOCATION (hitosara-kitchen-board-morning, HIGH) ／ REF_GEOGRAPHY (hitosara-kitchen-geography, MEDIUM) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `2 beats, NON_UNIFORM — 2.5s / 1.5s, both held at equal pressure. No accent`
- Camera Events: `none. Locked off for the full duration`
- Action Events: `ACT_WAIT` (single)
- Audio Events: `no dialogue ／ room tone ／ one sustained tone`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The cloth will move.** It is the single most likely failure: a video model asked to animate a covered bowl will make the cloth breathe, lift or settle. Any of those turns this shot into the event it refuses.
- **The frame will be frozen instead.** The opposite failure — a model that reads "nothing happens" as "still image". The shot needs light and dust in constant motion.
- **The camera will drift.** Slow push is the default. It must be locked off.
- **Steam will be invented.** It is the obvious way to show that something is under the cloth, and it is exactly what the film is withholding.
