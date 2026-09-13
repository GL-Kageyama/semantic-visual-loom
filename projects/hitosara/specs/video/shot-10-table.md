# Wan 3.0 Full Specification — 一皿ができるまで 第1章「一皿」Clip 10/10 / 4s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。** 投入の仕方は同じディレクトリの `README.md` を見よ。

⚠️ **この作品の最後のショットである。** ここで映像は**切れ目で動く**——
⚠️ **様式 `luminous-anime` の `Motion character` は「何かが常に動いている」と言う。**
モンタージュは**1ショットの中で連続して動かない**——**切れ目で動く。**
**これは衝突ではない。** `law` が明示しているとおり、
**「常に何かが動いている」は断片のそれぞれの中で満たされる。**
⚠️ **文字（`一皿`）は生成器が描かない。** 焼くのは `timeline` の `text_events` である
——だから §18 は文字を**要求しない**し、Negative は文字を**禁じる**。
⚠️ **§18 の節列は、系列の続きである。** 落ちたのは 08 の窯の3節と 09 の断面の3節だけで、
**それ以外の節は 09 と同じ位置に在る**——`no hands`・`no knife`・`no board`・`no plate` を
外したのは、**この1本には手が入り、皿が主題だからである**（`forbidden_set` でもない）。
⚠️ **`no flour sack`・`no lettering on the plate`・`no salt` を §16 に書き、
§18 の節列には足していない。** 節列は**明かしの系列**であって、**この1本の思いつきを
足す場所ではない**——足せば、その1本だけが持つ禁止が**非可逆の増分として読まれる**（`L14`）。
⚠️ **`no lettering on the plate` は `no readable text` に含まれる。** 書き分けても
**集合としては新しい節**であり、**同じ禁止の言い換えを機械は見分けられない**（`L14` の註）。

---

# 1. VIDEO

- Duration: `4s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take built of short fragments that join at cuts. A single change: an empty plate becomes a plate with a meal on it.

# 2. WORLD

## World Concept

Flour, water, salt, and time. The time is paid off here, in four seconds, and the film ends on the plate it promised in its title.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame.
- Light is the subject; here it is what the fragments are cut on.
- The oven interior was opened in `08` and is not in this shot.
- The crumb was opened in `09` and **is** in this shot — it is permitted now.
- **No lettering is generated.** Any text in the finished clip is composited afterwards.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject. The fragments are cut so that the light is continuous across them even when the space is not.
- Color Language: Magenta and gold against deep cyan shadow. The palette is at its warmest here and it does not go cold again.
- Texture: Layered atmospheric depth. Steam and flour dust suspended together; the table surface faintly reflective.
- Rendering: Hyper-detailed layered light — one volumetric shaft from the window, bloom and anamorphic flare around the source.
- Visual Density: Low, with **the right of the frame left quiet and uncrowded**, because text is placed over it at the end.
- Time: `朝`
- Atmosphere: Arrived.

# 3. SUBJECTS

## The Plate

- Reference: `TABLE.base`, `PAN.appearance`
- Appearance: One plate on a bare table, the torn loaf on it, steam standing up from it.
- Behavior: The plate is set down once and does not move after that. **In the last fragment it is the only thing in frame and it holds.**
- Continuity Requirements: The same loaf that was broken in `09`.

## The Hands

- Reference: `hitosara-baker-character-sheet`
- Appearance: Hands and a coarse linen apron, entering at the frame edge only.
- Behavior: They set the plate down and leave. **They do not appear in the last fragment.**
- Continuity Requirements: Same hands, same apron, no drift.

# 4. ENVIRONMENT

- Location: `TABLE`
- Environment Elements: A plain table by a window, a chair, a window, the room falling away out of focus.
- Environmental Behavior: The light does not change across the shot. **The fragments are cut on motion, not on light.**

# 5. OBJECTS

- `TABLE` — the table, and the plate on it.
- `PAN` — the torn loaf, its crumb permitted and visible.
- No other object is in frame: **no oven, no flour sack, no salt.**

# 6. REFERENCES

- REF_CHARACTER: `hitosara-baker-character-sheet` (MEDIUM)
- REF_LOCATION: `hitosara-table-board` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (LOW — the room is only suggested)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The plate is put down, and the film stops on it.
- Beginning: An empty plate.
- Turn: Fragments. The plate is set; the loaf is set on it; the table and the chair and the window.
- Peak: The plate with the meal on it, the steam standing.
- Pull: The camera comes to rest in front of it, the steam the only thing still moving, and holds.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-1.5s` — density: `dense` — The plate is set down. Steam rises. The loaf is broken and the crumb takes the gold.
  - BEAT 2 `1.5-2.5s` — density: `dense` — The table. The chair. The window. Three fragments, joined short.
  - BEAT 3 `2.5-4s` — density: `held` — It stops in front of the plate. Only the steam moves. Held long.
- Temporal Density: Two dense beats and a held one. **The held beat is the longest and it is where the film ends.**

# 9. ACTION

- `ACT_PLACE` — Before: the plate is empty. After: the plate has the loaf on it.
- `ACT_CUT` — Before: the room is one place. After: it has been three.
- `ACT_REST` — Before: the frame is moving through fragments. After: it has stopped, and the steam has not.

# 10. CAMERA

- Camera Language: Third-person, low and level with the table, the plate slightly off centre, a chair and a window suggested soft and out of focus behind, the light source inside the frame at the window.
- Camera Events: `0-1.5s` close on the plate being set. `1.5-2.5s` three short fragments joined at cuts. `2.5-4s` settle and hold, the plate in frame.
- Camera Behavior: **Short, deliberate moves that end at cuts, then one long rest.** No handheld, no whip, no shake. One continuous take built of fragments; the joins are cuts.

# 11. MOTION

## Subject Motion

In the first two beats the subject is the plating: the plate is set down, the loaf is broken and set on it, and the fragments carry the room past. **In the last beat the subject stops** — the plate and the loaf on it hold exactly where they are, and only the steam keeps moving.

## Object Motion

The plate is set down once and is not touched again. The loaf is placed and does not shift. **Nothing is displaced after the second beat.**

## Environmental Motion

Steam rises off the torn loaf continuously and thins, and is the primary mover of the last beat. Flour dust is suspended in the shaft. Both keep moving after the frame has come to rest.

## Physical Characteristics

- Weight: The plate has the weight of ceramic and it lands with it.
- Inertia: The plate stops when it is set down; there is no slide and no settling.
- Acceleration: The fragments accelerate and stop at each cut. The last beat has no acceleration at all.
- Fluidity: The steam moves as vapour losing heat, not as smoke.
- Impact: The plate meeting the table, once, quiet.

# 12. EMOTION

- Emotional Arc: The film arrives at the thing it has been making.
- Emotional Events: The moment the frame stops and the steam does not.

# 13. LIGHTING

- Base Lighting: Morning, from a window inside the frame. One shaft, warm gold across the plate. The table surface faintly reflective.
- Lighting Events: None. **The light is the continuity across the cuts** — it does not change between fragments, and that is what makes them fragments of one room.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: Ceramic on wood, once. A chair, briefly. The room otherwise quiet.
- Music: One sustained tone that enters with the last beat and holds, unresolved past the last frame.
- Environment: A room with no clock in it.

# 15. CONTINUITY

- Identity: The hands and apron follow the character sheet; they appear only in the first two beats. The loaf is the one broken in `09`.
- Visual: **The crumb is permitted and visible.** The palette is at its warmest. The composition reserves the right of the frame for text that will be composited later.
- Motion: Full animation, not limited — **and here the fragments are what carry it**: each fragment moves continuously, and the joins between them are cuts.
- Sound: Close, warm, small.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 皿 レンジより）

- No human face. No full body of the baker. No second person.
- No wall clock, no calendar, no digital timer.
- No readable text of any kind — **and in particular no lettering on the plate or on the loaf.**
- No brand label, no packaging text.
- No kitchen appliance with a display.
- No oven in frame. No flour sack in frame. No salt in frame.
- No hand in the last fragment.
- No camera shake, no whip, no handheld.

## MUST

- Full animation. Each fragment moves continuously; the steam keeps moving after the frame comes to rest.
- **The joins between fragments are cuts** — the fragments are not blended and there is no dissolve.
- The right of the frame stays quiet and uncrowded.
- The plate comes to rest and holds for the final 1.5 seconds.

## PREFER

- The light continuous across the cuts, so the fragments read as one room.

## ALLOW

- One brief glimpse of the chair, out of focus.

# 17. GENERATION PRIORITIES

1. **No legible lettering** — on anything, anywhere. The title card is composited, not generated.
2. **The joins are cuts** — a dissolve or a blend turns a montage into a single drifting shot and loses the film's ending.
3. **The last fragment holds** — the plate must not drift, breathe or be pushed in on.
4. **No hand in the last fragment** — the film ends on the plate, not on the person.
5. **The light does not change across the cuts** — it is the only continuity the fragments have.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 4-second continuous cinematic take built of short fragments that join at cuts (16:9), luminous realist anime, at a plain table by a window in a one-room bakery in the morning. Beats, deliberately uneven: [0-1.5s] a plate is set down and the torn loaf is set on it, steam rising and the crumb taking the gold; [1.5-2.5s] the table, the chair, the window — three fragments joined short; [2.5-4s] it stops in front of the plate and holds, with only the steam moving. **The light does not change across the cuts** — it is what makes the fragments one room. (No face, no clock, no hand in the last fragment, no legible lettering anywhere — the title is composited afterwards.)

## Visual Prompt

Luminous realist anime. Magenta and gold against deep cyan shadow, at its warmest. Hyper-detailed layered light — one volumetric shaft from a window inside the frame, bloom and anamorphic flare around the source, steam and flour dust suspended together and individually rendered, the table surface faintly reflective. One plate on a bare table, the torn loaf on it, its crumb visible and warm, steam standing up from it. A chair and a window suggested soft and out of focus behind. Two-step cel on the hands; the light rendered continuously. Low visual density, with **the right of the frame left quiet and uncrowded.** No human face, no full body, no second person, no hand in the last fragment. No readable text, no lettering on the plate or the loaf, no brand label, no packaging text, no oven in frame, no flour sack, no salt, no wall clock, no calendar, no digital timer, no kitchen appliance with a display, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited — **and it is carried by the fragments.** In the first two beats the subject moves: the plate is set down and stops without sliding, the loaf is broken and placed and does not shift, and three short fragments carry the table, the chair and the window past, **joined at cuts** — not blended, not dissolved, not a whip. **In the last beat the subject stops**: the plate and the loaf hold exactly where they are, and only the steam keeps rising and thinning. Steam is the primary mover of the last beat. No camera shake, no handheld, no drift, no push in the last beat, no impacts beyond the plate meeting the table, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, low and level with the table, the plate slightly off centre, a chair and a window soft and out of focus behind, the light source inside the frame at the window. Short, deliberate moves that end at cuts, then one long rest. [0-1.5s] close on the plate being set. [1.5-2.5s] three short fragments at cuts. [2.5-4s] settle and hold on the plate. No handheld, no whip, no shake, no push in the final beat. One continuous take built of fragments; the joins are cuts.

## Audio Prompt

No dialogue. Ceramic on wood, once. A chair, briefly. The room otherwise quiet. Music: one sustained tone entering with the last beat and holding, unresolved past the last frame. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven, no salt, no sliced bread, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: the steam rises continuously and never holds, and in the final beat it is the only thing moving. **Where the shot is a montage, "something is always moving" is satisfied inside each fragment** — each fragment moves continuously and the joins between them are cuts, not holds. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg10-4s-01`
- Segment ID: `01-10`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `4s`
- References: `REF_CHARACTER (hitosara-baker-character-sheet, MEDIUM) ／ REF_LOCATION (hitosara-table-board, HIGH) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 1.5s / 1s / 1.5s. The rest = BEAT 3 at 1.5s (38%)`
- Camera Events: `3 events as listed in §10, joined at cuts`
- Action Events: `ACT_PLACE → ACT_CUT → ACT_REST`
- Audio Events: `no dialogue ／ one ceramic ／ sustained tone`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`
- Compositing: `one text_event is burned over this clip by the timeline layer — 3.4-4.0s. It is not generated.`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The fragments may blend.** A model asked for a montage will often produce one continuous drifting move instead of cuts. The joins must be cuts.
- **The last beat may drift.** A slow push or a breathing frame in the final 1.5 seconds destroys the ending; the frame must come to rest.
- **Lettering may appear on the plate.** The film's title is composited; a generated word on the ceramic doubles it.
- **A hand may stay in the last fragment.** The film ends on the plate, not on the person.
- **The light may change between fragments.** It must not — the light is the only thing that makes them one room.
