# Wan 3.0 Full Specification — 一皿ができるまで 第1章「捏ねる」Clip 4/10 / 6s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。** 投入の仕方は同じディレクトリの `README.md` を見よ。

⚠️ **この仕様書は動画の仕様である。** §1–20 を持ち、§18 がモデル名（`WAN 3.0`）を名乗る。
⚠️ **§1–20 を持たないのは画像の仕様である**（`specs/image/`）——**種類の話であって、
モードの話ではない。** 全ショットが2つの経路を持つ。
⚠️ **渡す文字列は英語である。** 註と見出しの日本語は人へ、本文の英語はモデルへ。

---

# 1. VIDEO

- Duration: `6s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: separate flour and water become one mass under the hands.

# 2. WORLD

## World Concept

Flour, water, salt, and time. There is no clock anywhere — time advances on the dough's side. The hands make the time, the proof carries it, the oven closes it.

## World Rules

- Time advances on the dough's side. No clock appears in frame, ever.
- Only the hands are seen. The baker's face is never in frame — the people of this work are hands, an apron, and their shadow.
- Light is the subject. Flour dust floats in it.
- The oven interior is not shown until it is opened.
- The crumb is not shown until the loaf is broken.
- Only six objects exist: flour, water, salt, yeast, a bowl, an oven.

## Visual Language

- Art Direction: Luminous realist anime — the light, not the figure, is the subject. Clean anime lineart on the hands, deliberately subordinate to the light.
- Color Language: A saturated palette of magenta and gold against deep cyan shadow. The accent is the warm gold of the crust.
- Texture: Layered atmospheric depth. Flour dust suspended and catching the light. Wet work surfaces doubling the light source. No grain, no paper texture, no painterly stroke.
- Rendering: Hyper-detailed layered light — volumetric shafts travelling through the air, anamorphic flare and bloom around the source, particles suspended. Two-step cel on the hands; the light is rendered continuously.
- Visual Density: Low. One focal point per beat, generous negative space.
- Time: `朝`
- Atmosphere: Warm, saturated, dust-lit. The air moves even when nothing else does.

# 3. SUBJECTS

## The Hands

- Reference: `hitosara-baker-character-sheet`
- Appearance: A pair of working hands, neither young nor old, flour worked into the knuckle lines. A coarse linen apron, tied once, the ties hanging loose. No rings, no watch, no bracelet.
- Behavior: The hands do not hesitate and do not perform. Each motion completes before the next begins.
- Continuity Requirements: The apron is the same apron in every shot. The hands are the same hands — no drift across takes.

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: A wooden kneading bench scarred by years of scraping. A stone floor. One window. A wood-fired oven set into the far wall, its iron door closed. Hanging flour dust.
- Environmental Behavior: Dust is always falling and never settles. The window light moves across the bench. Nothing else in the room moves.

# 5. OBJECTS

- `KONA` — flour, heaped in a shallow well on the bench. Particles fine enough to stay airborne.
- `MIZU` — water, poured into the well, forming a skin before it takes the flour.
- `SHIO` — salt, only ever the amount that fits on a fingertip.

# 6. REFERENCES

- REF_CHARACTER: `hitosara-baker-character-sheet` (HIGH)
- REF_LOCATION: `hitosara-kitchen-board` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (MEDIUM)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The hands bring separate things into one thing.
- Beginning: Flour and water sit apart in the same hollow.
- Turn: The palm pushes through and the two stop being two.
- Peak: The mass turns glossy and its surface tightens.
- Pull: The hands stop — and the dust is still falling.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-1.5s` — density: `dense` — The heel of the palm drives the dough out. Flour jumps and scatters into the light.
  - BEAT 2 `1.5-4s` — density: `held` — Fold, turn, press. The rhythm is not even: there are strikes and there are rests.
  - BEAT 3 `4-6s` — density: `held` — The dough takes on a sheen and its surface tightens. The hands stop. The dust has not stopped falling.
- Temporal Density: The middle beat holds the largest share, and it is the least eventful.

# 9. ACTION

- `ACT_GATHER` — Before: flour and water are separate. After: a shaggy mass forms.
- `ACT_KNEAD` — Before: a shaggy mass. After: a smooth, elastic mass.
- `ACT_REST` — Before: the hands are working. After: the hands are still and open on the bench.

# 10. CAMERA

- Camera Language: Third-person, low and close to the bench — the height of the dough, not of a person. The hands and the mass are the subject; nothing above the apron enters frame.
- Camera Events: `0-1.5s` medium, the hollow and the two substances. `1.5-4s` close on the mass, the hands entering and leaving the frame edge. `4-6s` hold on the glossy surface, dust falling through the light.
- Camera Behavior: A slow, weighted drift. No handheld, no whip. One continuous take; no cut.

# 11. MOTION

## Subject Motion

The hands push, fold, and turn. Each strike is fast; each rest is long. The mass does not move on its own yet.

## Object Motion

The dough deforms under the palm and springs back slowly. Its surface goes from matte to glossy.

## Environmental Motion

Flour dust falls continuously and never settles. It is the only thing in the room that never stops.

## Physical Characteristics

- Weight: The mass gains weight as it comes together.
- Inertia: It resists the fold and then gives.
- Acceleration: Fast at the strike, slow at the release.
- Fluidity: It moves as one body, not as crumbs.
- Impact: No impact. This is pressure, not collision.

# 12. EMOTION

- Emotional Arc: Work without urgency.
- Emotional Events: The moment the two substances stop being two.

# 13. LIGHTING

- Base Lighting: One window, low sun. The light is the brightest thing in frame and the light source is inside the frame.
- Lighting Events: The sun drops during the shot; the shaft across the bench lengthens.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: The wet slap of the palm, the scrape of the bench, the small hiss of flour moving.
- Music: Extremely sparse — one sustained tone, no more.
- Environment: A room with no clock in it.

# 15. CONTINUITY

- Identity: The hands and apron follow the character sheet exactly. No drift.
- Visual: Warm saturated light; deep cyan in the shadow; flour dust in every frame.
- Motion: Full animation, not limited — something is always moving, and the atmosphere moves first.
- Sound: The bench is the same bench; its scrape is the same scrape.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・開示台帳 仕込み レンジより）

- No human face. No full body of the baker. No second person.
- No wall clock, no calendar, no digital timer.
- No oven interior, no visible flame, no glow through the door seam.
- No cut loaf, no visible crumb, no cross-section.
- No readable text of any kind.

## MUST

- Full animation. The dust falls for the entire shot.
- The light source is inside or at the edge of the frame.

## PREFER

- The hands entering and leaving the frame rather than being centered.
- An uneven rhythm over an even one.

## ALLOW

- The apron ties swinging into frame.

# 17. GENERATION PRIORITIES

1. **The withheld oven** — no oven interior, no flame, no seam glow. This outranks beauty.
2. **The hands** — identity must not drift; they follow the character sheet.
3. **The light as subject** — the flare and bloom belong to the source, not to the dough.
4. **The uneven rhythm** — fast strikes, long rests.
5. **The atmosphere always moving** — dust never settles, even in the held beats.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 6-second continuous cinematic take (16:9), luminous realist anime, at a wooden kneading bench in a one-room bakery with no clock in it. Identity: a pair of working hands, neither young nor old, flour worked into the knuckle lines, a coarse linen apron with the ties hanging loose, no rings and no watch. Beats, deliberately uneven: [0-1.5s] the heel of the palm drives the dough out, flour jumping into the light; [1.5-4s] fold, turn, press — fast strikes and long rests, the mass turning from matte to glossy; [4-6s] the hands stop and lie open on the bench, the dust still falling through the light. The light is the subject; the light source is inside the frame. (No face, no clock, no oven interior — the oven door stays closed in this clip.)

## Visual Prompt

Luminous realist anime. Clean anime lineart on the hands, kept subordinate to the light. A saturated palette — magenta and gold in the lit half, deep cyan in the shadow — with the warm gold of the crust as the accent. Hyper-detailed layered light: volumetric shafts travelling through the air, anamorphic flare and bloom around the light source, flour dust suspended and catching the light. Wet work surfaces doubling the light source. A wooden kneading bench scarred by scraping, a stone floor, one window, the flour heaped in a shallow well with water poured into it. Low visual density: one focal point, generous negative space. No human face, no full body, no second person. No oven interior, no visible flame, no glow through the oven door seam. No cut loaf, no visible crumb. No wall clock, no calendar, no readable text, no grain, no paper texture, no painterly stroke.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. Flour dust falls continuously and never settles, even when the hands are still. The hands push, fold, and turn with an uneven rhythm: fast at the strike, slow at the release. The dough deforms under the palm and springs back slowly, its surface going from matte to glossy. No impact, no collision, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, at the height of the dough — low and close to the bench. The hands and the mass are the subject; nothing above the apron enters frame. A slow, weighted drift with commitment; no handheld, no whip, no shake. [0-1.5s] medium, the hollow and the two substances. [1.5-4s] close on the mass, the hands entering and leaving the frame edge. [4-6s] hold on the glossy surface as the dust falls. One continuous take; no cut.

## Audio Prompt

No dialogue. The wet slap of the palm, the scrape of the bench, the small hiss of flour moving, all close. Music extremely sparse — one sustained tone at most. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: dust drifts and light shafts sweep continuously even when the hands are still. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg04-6s-01`
- Segment ID: `01-4`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `6s`
- References: `REF_CHARACTER (hitosara-baker-character-sheet, HIGH) ／ REF_LOCATION (hitosara-kitchen-board, HIGH) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `3 beats, NON_UNIFORM — 1.5s / 2.5s / 2s. The kneading = BEAT 2 at 2.5s (42%)`
- Camera Events: `3 events as listed in §10. One continuous take`
- Action Events: `ACT_GATHER → ACT_KNEAD → ACT_REST`
- Audio Events: `no dialogue ／ sparse tone`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The hands may render with a face attached.** The negative front-loads `no human face`; verify frame by frame.
- **The lamp may be invented.** A clock or lamp with a display is the most likely intrusion into a room that must have neither.
- **The animation may come back limited.** The style is full animation; held frames are a failure of this style, not a stylistic choice.
