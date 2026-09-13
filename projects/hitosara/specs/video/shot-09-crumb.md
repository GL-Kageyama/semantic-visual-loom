# Wan 3.0 Full Specification — 一皿ができるまで 第1章「断面」Clip 9/10 / 2.5s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。** 投入の仕方は同じディレクトリの `README.md` を見よ。

⚠️ **開示の第2点である。ここでパンが割れる。** §18 `Negative Prompt` から
`no cut loaf`・`no visible crumb`・`no cross-section` の**3節が落ちる**。以後どのショットでも戻らない。
**禁止が消えることは、モデルがそれを描いてよいことである。** 台帳がこの位置に変化点を宣言している（`L10` が検算する）。
⚠️ **窯の3節（`no oven interior`・`no visible flame`・`no glow through the door seam`）は
08 で既に落ちている。** ここに無いのは**窯が写るからではない**——`forbidden_set` が `KAMADO` を
禁じており、**窯はそもそも画面に無い。** 無いのは**「禁じる必要が無くなったから」**である。
**この2つは別のことである**（`L14` の註と同じ理屈）。
⚠️ **止まるのは断面であって、画面ではない。** 動くのは**湯気**である。

---

# 1. VIDEO

- Duration: `2.5s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the inside of the loaf becomes visible, and it is what the light was for.

# 2. WORLD

## World Concept

Flour, water, salt, and time. This is the shot the whole film withholds until now: **the interior is the subject**, and everything before it was the outside of it.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame — **and in this shot there are no hands at all.**
- Light is the subject; here the light comes from inside the bread.
- The oven interior was opened in `08`. It is not in this shot — the oven is not in frame at all.
- **The crumb is not shown until the loaf is broken. This is the shot where it is broken.**
- The loaf is opened once. It is not cut into slices.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject. **Here the subject and the light are the same object.**
- Color Language: Magenta and gold against deep cyan shadow. The crust is a deep lacquered gold with the sheen of a real bake; the crumb is warmer still.
- Texture: Layered atmospheric depth. **Inside the torn bread, the glossy walls of the pockets catch and return the light, rendered one by one rather than as a texture.** Steam rising and thinning.
- Rendering: Hyper-detailed layered light — one volumetric shaft from the window, bloom and anamorphic flare around the source, the crumb's pockets each carrying a specular of their own.
- Visual Density: Low. The crumb, and the light inside it.
- Time: `朝`
- Atmosphere: The reveal, held small.

# 3. SUBJECTS

## The Loaf

- Reference: `PAN.appearance`
- Appearance: A baked loaf, torn open. The crust is deep gold; the crumb is a wall of air pockets, each catching the light from inside.
- Behavior: **The torn face does not move.** The loaf is not turned, not pressed, not moved on the bench after it opens.
- Continuity Requirements: The same loaf that was in the oven in `08` and the same one that reaches the table in `10`.

## The Steam

- Reference: —
- Appearance: Visible only as it leaves the torn face and thins against the dark.
- Behavior: It rises and thins. It does not billow, does not curl around the loaf, and does not persist.
- Continuity Requirements: —

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: A wooden bench, and the light of a window at the frame edge. Nothing else is in focus.
- Environmental Behavior: The dust falls. The light does not change.

# 5. OBJECTS

- `PAN` — the loaf, torn open. **The torn face fills the frame.**
- No other object is in frame: **no oven, no bread knife, no board, no plate, no hand.**

# 6. REFERENCES

- REF_CHARACTER: `hitosara-baker-character-sheet` (LOW — no hands in frame)
- REF_LOCATION: `hitosara-kitchen-board-morning` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (MEDIUM)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The loaf opens and the light is inside it.
- Beginning: A baked loaf on the bench, whole, its outside gold. It has not been broken.
- Turn: It tears open.
- Peak: The wall of air pockets taking the light from inside.
- Pull: Steam rises off the torn face and thins, and the crumb stays lit.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-1.5s` — density: `sparse` — One baked loaf on the bench. Gold outside. **Not yet broken.**
  - BEAT 2 `1.5-2.5s` — density: `held` — It tears open. The wall of pockets takes the light and brightens from inside. Steam rises.
- Temporal Density: The held beat is the shortest and carries the shot — and in it, **the crumb does not move; the steam does.**

# 9. ACTION

- `ACT_BREAK` — Before: the crust is unbroken. After: the crumb is in frame.
- `ACT_RISE` — Before: there is no steam. After: steam is rising off the torn face and thinning.

# 10. CAMERA

- Camera Language: Third-person, close and low, the torn face of the loaf filling the frame and the crust a dark rim around it, the light source inside the frame at the edge.
- Camera Events: `0-1.5s` close on the whole loaf. `1.5-2.5s` hold as it opens — **the camera does not push in on the reveal.**
- Camera Behavior: Almost still. No handheld, no whip, no rack focus, no push on the break. One continuous take; no cut.

# 11. MOTION

## Subject Motion

**The torn face does not move.** The wall of air pockets holds its position from the instant it opens to the end of the shot. **The subject holds; what moves is the steam and the light on it.**

## Object Motion

The loaf is not turned, lifted, pressed or moved on the bench after it opens.

## Environmental Motion

**Steam is the primary mover.** It leaves the torn face, rises, and thins against the dark — it does not billow and does not curl. Fine flour dust falls through the beam at its own pace. Both keep moving through every beat after the break.

## Physical Characteristics

- Weight: The loaf has the weight of bread and it sits.
- Inertia: The torn face stops as soon as it opens — there is no recoil and no settling.
- Acceleration: One — the tear, at `1.5s`. Everything after it is slow.
- Fluidity: The steam moves as vapour losing heat, not as smoke.
- Impact: None. The bread gives without resistance.

# 12. EMOTION

- Emotional Arc: The outside of a thing turns out to have been the outside of something.
- Emotional Events: The instant the light is visibly inside the loaf.

# 13. LIGHTING

- Base Lighting: Morning, from a window at the frame edge. One raking shaft, warm gold.
- Lighting Events: At `1.5s` the crumb begins returning the light from inside, so the brightest part of the frame moves from the crust to the interior. **No new light source appears** — the same shaft is now lit from within.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: The crust giving, once, close. Silence otherwise.
- Music: One sustained tone entering on the break and held under the rest of the shot.
- Environment: A room with no clock in it.

# 15. CONTINUITY

- Identity: The loaf is the same loaf that was in the oven in `08`. No hands appear; the character sheet is not exercised in this shot.
- Visual: **From this shot onward the crumb is a permitted element.** The palette is unchanged.
- Motion: Full animation, not limited — the atmosphere is the primary mover, and after the break the atmosphere is the steam.
- Sound: Close, dry, small.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 皿 レンジより）

- No human face. No full body of the baker. No second person. **No hands at all.**
- No wall clock, no calendar, no digital timer.
- No readable text of any kind.
- No brand label, no packaging text.
- No kitchen appliance with a display.
- No oven in frame. The oven is not in this shot, and its absence is not the same thing as its prohibition.
- **The crumb is no longer forbidden.** It is the subject of this shot. No `no cut loaf`, no `no visible crumb`, no `no cross-section`.
- **No sliced bread.** The loaf is torn open once, not cut into slices — slicing is a different act with a different meaning.
- No knife, no board, no plate.

## MUST

- Full animation. The steam rises and the dust falls for the whole shot after the break.
- **The torn face holds** — it does not move once it is open.
- The crust is unbroken for the first 1.5 seconds.

## PREFER

- The torn face filling the frame, the crust a dark rim around it.

## ALLOW

- One pocket of the crumb catching a specular that no other pocket catches.

# 17. GENERATION PRIORITIES

1. **The crust stays whole until 1.5s** — the shot's meaning is the interval before the break, and it must exist.
2. **The torn face does not move after the break** — the crumb is the still subject, the steam is the mover.
3. **No knife, no slices** — a sliced loaf is a different film's shot.
4. **No hands** — this shot has none, and a hand turns the light inside the bread into an act of showing.
5. **Pockets, not texture** — the film's rule is that particles are individually rendered, and here that rule is the whole image.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 2.5-second continuous cinematic take (16:9), luminous realist anime, on a wooden bench in a one-room bakery in the morning, on a single baked loaf. Beats, deliberately uneven: [0-1.5s] the loaf on the bench, whole, its outside a deep lacquered gold, not yet broken; [1.5-2.5s] it tears open, the wall of air pockets taking the light from inside and brightening, and steam rising off the torn face and thinning. **The torn face does not move after it opens; the steam does.** The palette is magenta and gold against deep cyan shadow. (No face, no hands, no clock — and **the crumb is permitted in this clip; it is the subject.**)

## Visual Prompt

Luminous realist anime. Magenta and gold against deep cyan shadow; the crust a deep lacquered gold with the sheen of a real bake, and the crumb warmer still. Hyper-detailed layered light — one volumetric shaft from a window at the frame edge, bloom and anamorphic flare around the source, flour dust suspended and individually rendered, **and inside the torn bread the glossy walls of the pockets catching and returning that light, rendered one by one rather than as a texture.** The torn face of the loaf filling the frame, the crust a dark rim around it, the light source inside the frame at the edge. Two-step cel on the crust; the light rendered continuously. Low visual density: the crumb, and the light inside it. No human face, no full body, no second person, no hands. No knife, no board, no plate, no oven in frame, no sliced bread, no readable text, no brand label, no packaging text, no wall clock, no calendar, no digital timer, no kitchen appliance with a display, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited. The crust is unbroken for the first 1.5 seconds, then it tears open once with no recoil and no settling. **After the break the torn face does not move at all** — it holds its position to the end of the shot. Steam is the primary mover: it leaves the torn face, rises, and thins against the dark; it does not billow and does not curl. Flour dust falls through the beam continuously. No turn, no lift, no press, no impact, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, close and low, the torn face of the loaf filling the frame, the crust a dark rim around it, the light source inside the frame at the edge. Almost still — no handheld, no whip, no shake, no rack focus. [0-1.5s] close on the whole loaf. [1.5-2.5s] hold as it opens — **the camera does not push in on the reveal.** One continuous take; no cut.

## Audio Prompt

No dialogue. The crust giving, once, close. Silence otherwise. Music: one sustained tone entering on the break and held to the end. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no hands, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no knife, no board, no plate, no oven, no sliced bread, no bread slices, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover, and after the break the atmosphere is the steam: it rises and thins continuously and never holds. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg09-2.5s-01`
- Segment ID: `01-9`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `2.5s`
- References: `REF_LOCATION (hitosara-kitchen-board-morning, HIGH) ／ REF_GEOGRAPHY (hitosara-kitchen-geography, MEDIUM) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `2 beats, NON_UNIFORM — 1.5s / 1s. The break = BEAT 2 at 1s (40%)`
- Camera Events: `2 events as listed in §10. One continuous take`
- Action Events: `ACT_BREAK → ACT_RISE`
- Audio Events: `no dialogue ／ one break ／ sustained tone`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The break may happen too early.** The first 1.5 seconds are the shot: the crust must be whole for them.
- **The crumb may move after opening.** It must hold. A crumb that shifts or settles turns a still subject into a moving one and loses the contrast with the steam.
- **A knife or a hand may appear.** Both are natural defaults for bread and both are wrong here — the loaf is torn, and no one is in frame.
- **The pockets may render as texture.** The film's rule is one by one; a flat crumb loses the light that this shot exists to show.
