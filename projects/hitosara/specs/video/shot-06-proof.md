# Wan 3.0 Full Specification — 一皿ができるまで 第1章「発酵」Clip 6/10 / 8s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。** 投入の仕方は同じディレクトリの `README.md` を見よ。

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
- Generation Intent: One continuous take. A single change: the dough stops being smaller than its container
  — **and it never becomes smaller again.**

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
- Appearance: A pale, slightly damp mass under a linen lid. Its surface is matte at the start and becomes taut, **and it stays taut — it does not go slack and never sags back.**
- Behavior: It does not seek, and **it never occupies less room than it did.** It does not sink, collapse, deflate, or fall back.
- Continuity Requirements: The mass must be continuous with the mass kneaded in the previous shot. No change of color, no change of scale.

# 4. ENVIRONMENT

- Location: `KITCHEN`
- Environment Elements: A wooden bench. A wide ceramic bowl under a linen lid. One window. A wood-fired oven set into the far wall, its iron door closed. Hanging flour dust.
- Environmental Behavior: Dust is always falling. The window light crosses the bowl during the shot. The lid moves once, and only because the dough moves it. **The lid rests on the dough from the first frame to the last; no gap ever opens between them.**

# 5. OBJECTS

- `KONA` — the fine dust that has settled on the lid, sliding off when the lid lifts.
- The bowl and its linen lid. **The lid stays on the dough for the whole shot.** No other vessel is in frame.

# 6. REFERENCES

- REF_LOCATION: `hitosara-kitchen-board-midday` (HIGH)
- REF_GEOGRAPHY: `hitosara-kitchen-geography` (MEDIUM)
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hitosara/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The dough takes up more room than it was given.
- Beginning: The bowl is larger than its contents.
- Turn: The surface rises without anything touching it, **and it does not come back down.**
- Peak: The dough touches the underside of the lid.
- Pull: The lid has lifted a fraction **and stays there**; flour slides off its rim.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — The bowl under its lid. Nothing is happening outside it.
  - BEAT 2 `2-5s` — density: `held` — The surface lifts by an amount you can see. The shadows of bubbles move inside.
  - BEAT 3 `5-7s` — density: `held` — **The dough presses the lid up and holds it up. The lid stays in contact with the dough.**
  - BEAT 4 `7-8s` — density: `dense` — The lid has lifted a fraction and stays there; flour slides off the rim. **The dough is still rising when the shot ends.**
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

The dough rises. There is no visible cause — that is the point of the shot. **It rises for the whole shot and never sinks: it does not collapse, does not deflate, and does not fall back. The rise is one-way.**

## Object Motion

The lid moves only when the dough reaches it, **and it stays on the dough** — it never stands free above it. The flour on the lid slides when the lid moves.

## Environmental Motion

Flour dust falls continuously. The window light crosses the bowl. Both keep moving through every beat, including the held ones.

## Physical Characteristics

- Weight: The mass gains presence without gaining visible size. **It only ever gains height; it never loses it.**
- Inertia: It does not stop when the light stops moving. **Nothing here falls.**
- Acceleration: Almost none. This is the slowest motion in the film.
- Fluidity: The surface moves as a skin **over a mass that is still rising** — it is not a membrane that inflates and then deflates.
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
- **No deflation, no collapse, no sinking, no falling back of the dough.**
- **No gap between the lid and the dough. The lid never stands free above the dough.**
- **No over-proofed, slumped or exhausted dough.**

## MUST

- Full animation. The dust falls and the light moves for the entire shot.
- The rising must have no visible cause.
- **The dough only ever rises. It is higher at the end than at the start, and it never sinks.**
- **The lid stays in contact with the dough for the whole shot.**

## PREFER

- The bowl slightly off-center, with the light source at the frame edge.

## ALLOW

- A single dry tick on the lid.

# 17. GENERATION PRIORITIES

1. **The rise is one-way** — the dough is higher at the end than at the start, and it never sinks, collapses or deflates. ⚠️ **This is the failure this shot actually produced.** It outranks beauty.
2. **The withheld oven** — no oven interior, no flame, no seam glow.
3. **No cause** — no hand, no draft, no tool may appear to explain the rise.
4. **The lid stays on the dough** — no gap ever opens between them.
5. **The light as subject** — flare and bloom belong to the source.
6. **The slow beat** — the held middle must hold the largest share.
7. **The atmosphere always moving** — dust falling even while the dough seems still.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

An 8-second continuous cinematic take (16:9), luminous realist anime, at a wooden bench in a one-room bakery with no clock in it. A wide ceramic bowl under a linen lid, flour dust hanging in the light. Beats, deliberately uneven: [0-2s] the bowl under its lid, nothing happening outside it; [2-5s] the dough's surface lifts by an amount you can see, the shadows of bubbles moving inside it; [5-7s] the dough presses the lid up and holds it up, the lid staying in contact with the dough; [7-8s] the lid has lifted a fraction and stays there, and flour slides off its rim. No hands and no tool enter the frame; the rise must have no visible cause. **The rise is one-way: the dough is higher at the end than at the start, and it never sinks, never collapses and never falls back.** The light is the subject. (No face, no clock, no oven interior — the oven door stays closed in this clip.)

## Visual Prompt

Luminous realist anime. A saturated palette — magenta and gold in the lit half, deep cyan in the shadow — with the warm gold of the crust as the accent. Hyper-detailed layered light: volumetric shafts travelling through the air, anamorphic flare and bloom around the light source, flour dust suspended and catching the light. A wooden bench, one window, a wide ceramic bowl under a coarse linen lid with flour settled on it, the lid resting on the dough with no gap beneath it, a stone floor, the wood-fired oven in the far wall with its iron door closed. Low visual density: the bowl, the lid, and the light; almost nothing else. No human face, no full body, no second person, no hands at all. No oven interior, no visible flame, no glow through the oven door seam. No cut loaf, no visible crumb. No wall clock, no calendar, no readable text, no grain, no paper texture, no painterly stroke, no deflating dough, no collapsing dough, no sinking dough, no dough falling back, no slump, no over-proofed dough, no gap between the lid and the dough, no lid standing free above the dough.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. Flour dust falls continuously and never settles; the window light crosses the bowl for the whole shot. The dough's surface rises as a skin over a mass that keeps rising, with almost no acceleration — the slowest motion in the film. **The rise is one-way: the dough is higher at the end than at the start, and it never sinks, never collapses, never deflates and never falls back — there is no drop, no slump and no deflation at any point.** The lid moves only once and stays resting on the dough; it never stands free above it and no gap ever opens between them. Flour slides off the rim. No hand, no draft, no tool, no visible cause. No impact, no collision, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third-person, at the height of the bowl. The bowl and the light are the subject; the room is soft behind it. A slow, weighted push with commitment; no handheld, no whip, no shake. [0-2s] medium, the whole bowl. [2-7s] slowly closer until the surface fills the lower half of the frame. [7-8s] hold on the rim as the flour slides. One continuous take; no cut.

## Audio Prompt

No dialogue. Almost no effects — a single faint dry tick as the lid lifts. Music: one sustained tone held for the whole shot. No swell, no sting, no melody.

## Negative Prompt

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no torn-open loaf, no sliced bread, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces, no deflating dough, no collapsing dough, no sinking dough, no falling back, no slump, no over-proofed dough, no gap between the lid and the dough

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: dust drifts and light shafts sweep continuously even when nothing else is happening. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames with only one element moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hitosara-ch01-seg06-8s-02`
- Segment ID: `01-6`
- Specification Version: `0.1.1`
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

`0.1.1` — **1回生成し、1回失敗した。**「keeps trying（〜し続けようとする）」という書き方をやめた。

## Observed Problems

- **⚠️ 生地が上がったあと、突然、萎んで、どさっと落ちた（第1回生成、`0.1.0`）。**
  **原因は仕様である。** `0.1.0` は §8 BEAT 3 と §18 Master の2箇所で
  **「the dough reaches the underside of the lid and `keeps trying`」**と書いていた。
  ⚠️ **「keeps trying」は、この10本の仕様で、このショットにしか無い語である**
  （他の9本には一度も出てこない——`grep` 実測）。
  **「試み続ける」は、失敗できる動作である。** モデルはその通りに描いた——
  **押して、支えきれずに沈んで、また押す。**
- ⚠️ **そして、どこにも「戻らない」と書いていなかった。** §16 `MUST NOT` は6項目あり、
  **そのどれも生地の動きの向きについて言っていない。** §11 Fluidity の
  **「the surface moves as a `skin`」**は、上限の無い膜として読める——
  **膨らむ膜は、膨らむのをやめれば萎む。**
  ⚠️ **`shot-07` には同じ考え方が既に書いてある**——
  「`The colour shift does not overshoot and does not reverse. It goes one way.`」
  **shot-06 にだけ、それが無かった。**

### 実測（`ffprobe` と画素）

| 測ったもの | 値 |
|---|---|
| 尺 | **8.000s / 240フレーム**（仕様の `8s` と一致） |
| フレームレート | **30fps**（仕様は `24fps`——他の動画と同じ食い違い） |
| 解像度 | 1920×1080 |
| 布の下の暗い領域（中央・画像下半分） | **5.6s まで 10〜18%。6.0s に 46.8% へ跳ね、以後 40% 前後で戻らない** |

⚠️ **落ちたのは 5.6s → 6.0s の0.4秒である**——**仕様の BEAT 3 は `5-7s`。**
**書いてある位置で、書いてある通りに落ちている。**

### 直し方

**「keeps trying」を消し、「一方向である」を明示した**（`0.1.1`）。
§1・§3・§4・§5・§7・§8・§11・§16・§17・§18 の**18箇所**。
⚠️ **変化は1つのままである**——「生地が器より大きくなる」であって、**「戻る」ではない。**

## Anticipated risks (to check in the first generation)

- **The dough may collapse or deflate.** ⚠️ **実測で出た（第1回）。** The rise is one-way: it is higher at the end than at the start and never sinks. **A soft mass that lifts will fall unless it is told not to** — and `0.1.0` never told it.
- **A gap may open between the lid and the dough.** The lid must stay resting on the dough; if it stands free, the dough below it reads as having collapsed.
- **A hand may be added to explain the rise.** The negative and §17 both front-load it; verify frame by frame — this is the most likely failure of this shot.
- **The dough may be given a visible cause** (a draft, a tool, a light change) that reads as the reason it moves.
- **The shot may come back as a time-lapse.** It must be a continuous 8 seconds, not a compressed one.
