# Wan 3.0 Full Specification — 一皿ができるまで 第1章「粉と水」Clip 2/10 / 2s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。** 投入の仕方は同じディレクトリの `README.md` を見よ。

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
- Appearance: Water already pooled on the flour as a film — its edge sharp at the start, gone by the end.
- Behavior: It spreads into the flour. **It does not arrive.** It is already lying there when the shot begins, and it never pours, wells up, or comes up out of the flour.
- Continuity Requirements: The same vessel, the same water, in every shot.

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: A wooden bench, flour heaped on it, and the light of a window at the frame edge. Nothing else is in focus.
- Environmental Behavior: The dust falls; the light does not move within the shot's short span.

# 5. OBJECTS

- `KONA` — the flour, heaped, its grains separate and countable at the start.
- `MIZU` — the water, as a film over the flour and then as a boundary inside it. **It is in frame from the first frame; nothing delivers it.**
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
- Beginning: The apex of a heap of flour seen at a very shallow angle, **a film of water already lying on it and its edge still sharp**. The dry grains are separate and countable.
- Turn: **That edge gives way.**
- Peak: The film spreads and the edges of the grains go out one after another.
- Pull: What is left is one damp mass where there were two things.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-1s` — density: `sparse` — The apex of the heap at a very shallow angle, **the water already pooled on it and its edge still sharp**. The dry grains are separate and countable.
  - BEAT 2 `1-2s` — density: `dense` — **The sharp edge gives way.** The film spreads and the grain boundaries go out one after another. Density rises only for this second.
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

The subject is the boundary and the boundary is what moves — the water's edge advances into the flour and the sharp line becomes a gradient. **⚠️ The water itself does not arrive and does not rise: the edge advances where the water already lies.**

## Object Motion

The heap of flour does not move. It is not stirred, not pressed, and not displaced.

## Environmental Motion

Flour dust falls through the beam continuously and is individually rendered. It keeps moving through both beats.

## Physical Characteristics

- Weight: The water has weight and it sits — **it is already sitting when the shot opens**; the flour takes it without collapsing.
- Inertia: The film stops advancing where the flour stops taking it. There is no overshoot, no run-off, **and no liquid that comes up out of the flour.**
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
- Sound Effects: A very small sound of water **soaking into** powder. The room is otherwise silent.
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
- **No liquid welling up, erupting, or rising out of the flour.**
- **No pouring, no stream, no jet, no jug, no vessel, no tap — nothing delivers the water. It is already in frame when the shot begins.**

## MUST

- Full animation. The boundary advances and the dust falls for the whole shot.
- The heap of flour does not move.
- **The water is already lying on the flour in the first frame.** Nothing delivers it during the shot.

## PREFER

- The boundary across the centre of the frame, the wet side and the dry side both readable.

## ALLOW

- One visible specular on a single wet grain face.

# 17. GENERATION PRIORITIES

1. **The water is already there** — a film on the flour from the first frame. **Water that arrives, wells up, or erupts out of the flour is a different shot, and it is this shot's most likely failure.**
2. **The flour does not move** — a stirred or pressed heap is a different shot.
3. **The water does not splash** — it wets. A splash turns a macro into an action shot.
4. **No legible lettering** — on anything that appears in frame.
5. **Only two substances** — no salt, no bowl, no tool enters the macro.
6. **Grains, not texture** — the film's rule is that particles are individually rendered, and this shot is where that rule is most visible.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 2-second continuous cinematic macro take (16:9), luminous realist anime, on a wooden bench in a one-room bakery in the morning, at the boundary between flour and water. Beats, deliberately uneven: [0-1s] the apex of a heap of flour seen at a very shallow angle with a film of water already lying on it, its edge still sharp, the dry grains separate and countable; [1-2s] that edge gives way, the film spreads, and the grain boundaries go out one after another until there is no boundary left. The water is already lying there and nothing pours it or lets it rise out of the flour. The heap does not move; the water does not splash. The palette is magenta and gold against deep cyan shadow, at its densest. (No face, no clock, no salt in frame, no legible lettering anywhere.)

## Visual Prompt

Luminous realist anime macro. Magenta and gold against deep cyan shadow, the densest in the film. Hyper-detailed layered light — one volumetric shaft from a window at the frame edge, a shallow depth of field so only the boundary is in focus, flour dust suspended in the beam and individually rendered, every grain separately drawn and every wet grain face carrying one specular. A wooden bench surface, flour heaped on it. Two-step cel on the fingertips at the frame edge; the light rendered continuously. The water is cooler in tone than the flour and that difference is the picture. No human face, no full body, no second person. No salt, no bowl, no tool, no water splash, no drops flying in the air, no running tap, no liquid welling up out of the flour, no water erupting from the flour, no pouring, no stream, no jug, no vessel, no water source in frame. No readable text, no brand label, no packaging text, no oven interior, no visible flame, no cut loaf, no visible crumb, no torn-open loaf, no cross-section, no wall clock, no calendar, no digital timer, no kitchen appliance with a display, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited. The boundary is the primary mover: the water is already lying on the flour when the shot opens, and its edge advances into the flour, fast at first and then slowing as it soaks, until the sharp line becomes a gradient. The water does not arrive, does not pour, does not well up and does not rise out of the flour — nothing delivers it and the only thing that moves is its edge. The heap of flour does not move — it is not stirred, not pressed, not displaced. Flour dust falls through the beam continuously. No splash, no drip, no run-off, no overshoot, no impact, no liquid erupting from the flour, no water rising up, no pouring, no stream, no water source, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, macro, at the height of the bench surface, shallow depth of field so that only the boundary is in focus. Nearly still — no handheld, no whip, no shake, no rack focus. [0-1s] hold on the apex. [1-2s] a push of a few millimetres as the water lands. One continuous take; no cut.

## Audio Prompt

No dialogue. A very small sound of water soaking into powder, once. Silence otherwise. Music: none — the score is absent for this shot. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, no salt, no salt shaker, no water splash, no drops flying in the air, no running tap, no liquid welling up out of the flour, no water erupting from the flour, no water rising up out of the flour, no pouring, no stream of water, no jet of water, no jug, no vessel, no faucet, no water source in frame, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover, and here the moving atmosphere is the water's edge itself: it advances continuously and never holds. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg02-2s-02`
- Segment ID: `01-2`
- Specification Version: `0.1.1`
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

`0.1.1` — **1回生成し、1回失敗した。**「水が触れる」という書き方をやめた。

## Observed Problems

- **⚠️ 粉から液体が突然溢れてきた（第1回生成、`0.1.0`）。映像は綺麗だった。**
  **原因は仕様である。** `0.1.0` は §7 Turn・§8 BEAT 2・§18 Master の3箇所で
  **「the water touches（水が触れる）」**と書いていた——**「水が在る」ではなく「水が来る」である。**
  そして**どこから来るかを、どこにも書いていなかった。** モデルはその空欄を埋めた——
  **画面に器が無いのだから、粉の中から湧かせるのが唯一の手である。**
  ⚠️ **これは生成器の失敗ではない。我々の失敗である。**
  ⚠️ **仕様は元から割れていた。** §3「Water pooling on the flour — **a film first**, then a boundary」と
  §5「as a film over the flour **and then** as a boundary inside it」は**最初から膜である**と言い、
  §7・§8・§18 は**1秒目に水が来る**と言っていた。**機械は後者を選び、足りない原因を補った。**
- **直し方**: 「触れる」を消し、**「最初のコマから既に在る」**にした（`0.1.1`）。
  §3・§5・§7・§8・§11・§14・§16・§17・§18 の9箇所。**変化は1つのままである**——
  「2つが2つでなくなる」であって、「水が来る」ではない（§1 Generation Intent）。

## Anticipated risks (to check in the first generation)

- **The water may arrive.** ⚠️ **実測で出た（第1回）。** It is already lying on the flour in the first frame; nothing pours it and nothing lets it rise out of the flour. **A film that comes up out of the flour is the failure this shot actually produced**, and it changes the shot's meaning more than a splash does.
- **The water may splash.** It wets; it does not splash and does not fall from a height.
- **The heap may be stirred.** Nothing presses or displaces the flour in this shot; that is `04`'s job, not this one.
- **Salt may appear.** It is the natural thing for a model to add to a bowl of flour and water. It is not in this shot.
- **Grains may become texture.** At macro scale the film's rule about individually rendered particles is what separates this shot from a stock photograph of flour.
