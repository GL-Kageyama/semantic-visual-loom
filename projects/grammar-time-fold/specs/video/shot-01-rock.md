# Wan 3.0 Full Specification — 一枚岩 Clip 1/1 / 10s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**

⚠️ **この仕様は形式カード `time-fold` を1度だけ使う。**
カードの4つの欄が、この仕様の背骨である。

| カードの欄 | この1本の値 |
|---|---|
| `PLACE` | 海に突き出た一枚岩。**カメラはここを離れない** |
| `PASSES` | 100年分の波。**時は、この枠を通り抜ける** |
| `SURVIVOR` | **岩そのもの。** 周りのすべてが変わるあいだ、これだけが変わらない |
| `RANGE` | **100年** |

⚠️ **このカードは `video-spec` に文法を1つ足したものである。**
この仕様が足したのは **「時は並べられず、積まれる」という1点**だけである——
**枠は容器であって、旅人ではない。**
⚠️ **`coexisting-realities` と混同しないこと。** あちらは複数の時が**同時に**在り、
こちらは**順に過ぎる。** どちらも先に来ない枠は、あちらである。

⚠️ **この作品は物語ではない。** 1ショットだけの最小の作品であり、
**7枚の文法カードの1枚が、仕様として立つかを試すために在る。**

---

# 1. VIDEO

- Duration: `10s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take from a camera that never leaves the place.
  **A hundred years pass through one frame — and the shot spends its seconds unevenly across them.**

# 2. WORLD

## World Concept

A rock standing out of the sea, and a hundred years going past it. **The frame does not travel** —
it holds, and time moves through it. Everything around the rock is worn down; the rock is not.
At the last second a bird lands on it.

## World Rules

- **The camera never leaves.** No cut, no return — **leaving and coming back would be a second shot.**
- **One survivor.** The rock itself does not change across the whole span, and **that is what makes the passage read as time rather than as several unrelated states.**
- **The times are stacked, not laid end to end.** A hundred years pass through one frame, in order, and none of them arrives alongside another.
- **The seconds are not spread evenly.** The shot chooses where in the span it lingers.
- **No date stamp, no caption, no title card carrying elapsed time.**
- **No aging makeup, no prosthetic, and no stated "years later."**
- **No human figure** in the frame at any point.
- **No legible text** appears anywhere.

## Visual Language

- Art Direction: Large-format landscape photography. f/64 deep focus — the rock, the sea at its foot, and the horizon all sharp at once. Full tonal range from deep shadow to bright highlight, fine detail at every scale. **The land and the sky are the subject, and nothing intrudes on them.**
- Color Language: Natural film color with a subtle cool cast. **The palette shifts with the weather and the light, and never with the year** — nothing in the frame dates it.
- Texture: Fine grain, crisp edges, the rock's wet face and the sea's surface at the same resolution.
- Rendering: True large-format photography. Deep focus held for the whole shot. Not an illustration, not a render, no HDR oversaturation.
- Visual Density: Low. **Rock, sea, horizon, sky — and at the end, one bird.**
- Time: 100年
- Atmosphere: Quiet majesty. **The frame is not dramatic; the span is.**

# 3. SUBJECTS

## The Rock

- Reference: (none — the rock is not a registered entity; it is the subject of the shot)
- Appearance: A single mass of stone standing out of the sea, its face dark and wet at the waterline and dry above it. **Its edges stay as they are for the whole shot.**
- Behavior: **It does not move, and it does not wear.** Everything around it is taken down by the span; the rock is the one thing the hundred years does not touch. **It is not the shot's actor — it is the shot's measure.**
- Continuity Requirements: Must Preserve: its place in the frame, its silhouette, its edges. May Change: **nothing.**

## The Bird

- Reference: (none — the bird is not a registered entity)
- Appearance: One bird, seen at the scale the deep focus gives it — small, and sharp.
- Behavior: **It lands once, at the end, and stays.** It does not arrive before the last second, and it does not leave. **It is the one thing in the frame that appears rather than passes.**
- Continuity Requirements: Must Preserve: its stillness after landing. May Change: nothing.

# 4. ENVIRONMENT

- Location: `一枚岩`
- Environment Elements: The sea around the rock at its foot, and the sky above the horizon. A far shoreline sits low on the horizon behind the rock.
- Environmental Behavior: **The sea does everything.** Waves come and return, the sea's level falls across the span, the light crosses the frame, the clouds replace one another. **The far shoreline is worn down and grows lower.** ⚠️ **No storm, no boat, no building, and nothing crosses the frame.**

# 5. OBJECTS

- The rock is both the object and the subject.
- The bird is the only other thing that exists in the frame, and it arrives in the last second.
- **No boat, no buoy, no building, no mast, no fence, no litter, no driftwood** in the frame.

# 6. REFERENCES

- REF_LOCATION: `一枚岩.base` — **未作成。** この作品の画像の経路はまだ1度も走っていない
  （`ledger.yaml` を見よ）(MEDIUM)
  ⚠️ **在ることと、渡したことは違う。** **この1本は、いま何も添付していない**
  （ショット記録の `attached: []` を見よ）。
  ⚠️ **`一枚岩.geography` も同じである**——構図は§4と§10の文が持ち、ボードはまだ無い。
- REF_STYLE: `landscape-photo` (HIGH)
- REF_FORMAT: `time-fold` — this defines the one grammar this shot is
- REF_SOURCE: `projects/grammar-time-fold/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: A hundred years pass through one frame.
- Beginning: Rock, sea, sky. **Nothing has happened yet.**
- Turn: **Time begins to move through the frame** — the sea changes colour, the light moves, the clouds replace one another, and the rock stays.
- Peak: Everything around the rock is worn down. **The rock's own face is not.**
- Pull: A bird lands, and **the whole span arrives after the fact, in that one small still shape.**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-3s` — density: `sparse` — Rock, sea, sky. A wave returns at the rock's foot. Nothing has begun.
  - BEAT 2 `3-7s` — density: `held` — **The passage.** Waves come and return, the sea's colour turns, the light crosses, the clouds replace one another. **Only the rock holds.**
  - BEAT 3 `7-9s` — density: `dense` — The wearing down. The sea thins, the far shoreline drops, the waves strike differently. **The rock's face is not touched.**
  - BEAT 4 `9-10s` — density: `held` — A bird lands and stays.
- Temporal Density: **The passage takes the largest share.** ⚠️ **The seconds are deliberately unequal** — the span is not spread evenly across the clip, and the shot lingers where the hundred years are most legible.

# 9. ACTION

- `ACT_HOLD` — Before: the frame is composed and settled. After: **it is still composed and settled, and time has begun to move through it.**
- `ACT_WEAR` — Before: the sea and the far shoreline are as the shot opened. After: they are lower and thinner.
- `ACT_LAND` — Before: the rock's top is bare. After: **one bird is on it, and it does not move.**
- Causes: **time.** ⚠️ **Nothing in the frame causes anything** — no agent acts, nothing enters to make something happen, and **there is no process beat.** The span is the cause, and the span is not a thing in the frame.

# 10. CAMERA

- Camera Language: **A large-format frame on a tripod, set up before the shot begins** — composed once (rock low and slightly off-centre, horizon on the upper third) with deep focus from the near water to the far horizon, and then **left alone completely. The tripod is the placement: the camera stands in the place and follows nothing through it.** ⚠️ **The style's physical law, in the card's own words** (`landscape-photo`) — **The camera is set up, not followed.** A large-format frame stands on a tripod; the shot is composed and then left alone.
- Camera Events: `0-10s` none — **the frame stands for the whole hundred years.** ⚠️ **A hold is an event, written with its range like any other**: timing `0-10s`; movement none; target the rock, with the horizon on the upper third; speed none. **What the hold is spent on is the span** — the time passes through the frame, **and everything except the rock is what moves.**
- Camera Behavior: **Fixed, and the fixing is the grammar's own requirement rather than a stylistic preference.** ⚠️ **The reason, which travels on into §18: coming back to the place after leaving it is a second shot, and this grammar's whole claim is that the place was never left** — the camera cannot leave, **or the hundred years become a cut.** One continuous take; no cut.

# 11. MOTION

## Subject Motion

**The rock does not move at all.** It holds its place, its silhouette, and its edges for the whole ten seconds. **What moves is everything around it** — and the rock is what lets that motion be read as a span rather than as a series of states.

## Object Motion

The bird is still once it has landed. **Its only motion is the landing itself**, in the last second, and after that it does not move.

## Environmental Motion

This is where the shot lives. Waves come and return at the rock's foot; the sea's level and colour change across the span; the light crosses the frame; the clouds replace one another overhead; the far shoreline is worn lower. **The motion is continuous and never stops** — the frame is never still even though the camera is.

## Physical Characteristics

- Weight: The sea has it and the rock carries it. **The rock's mass is the reason the frame can hold.**
- Inertia: Nothing here starts or stops. **The span does not accelerate and does not rest.**
- Acceleration: None. **The passage is even in reality and uneven only in how the seconds are spent.**
- Fluidity: The sea, entirely. **Water is the medium the span is written in.**
- Impact: Waves against the rock, unbroken, for the whole shot.

# 12. EMOTION

- Emotional Arc: The quiet of a thing that is not being asked to do anything, while a hundred years go past it.
- Emotional Events: The last second, when the bird lands and **the size of what has already happened becomes visible.**

# 13. LIGHTING

- Base Lighting: Direct sun with a full tonal range, deep shadow on the rock's far side and bright highlight on the water. **The light is not fixed** — it crosses the frame and changes as the span passes.
- Lighting Events: `3-9s` — **the light travels and the sky's weather turns over.** ⚠️ **This is the only light change, and it is what makes the passage visible in a frame where nothing else moves.**

# 14. AUDIO

- Dialogue: None.
- Sound Effects: The sea at the rock's foot, unbroken, for the whole shot. **No impact is singled out.**
- Music: None.
- Environment: Open air, a distant waterline, wind that rises and falls across the span.

# 15. CONTINUITY

- Identity: The same rock for the whole shot — **same mass, same edges, same place in the frame.** The same bird from the moment it lands.
- Spatial: **The composition does not change at all.** The rock does not move within the frame and the horizon does not move.
- Temporal: One continuous passage. ⚠️ **A hundred years pass with no cut and no time-skip** — the span is crossed by the frame holding, not by the shot jumping.
- Visual: Deep focus held for the whole shot, the grain stays fine, and the tonal range stays full.
- Motion: **Continuous. There is no held frame anywhere in it.**
- Sound: The sea is unbroken.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止）

- No cut, no cross-dissolve, and no time-skip. **The place is never left.**
- No return to the place after leaving it.
- No date stamp, no caption, and no title card carrying elapsed time.
- No aging makeup, no prosthetic, and no stated "years later."
- **The camera must not move** — no pan, no zoom, no drift, no rack.
- No people, no figure, no boat, no building.
- No storm, and no second bird — **the bird is one, and it lands once.**
- No shallow depth of field, no HDR oversaturation, no lens flare.
- No readable text of any kind.

## MUST

- **One survivor: the rock does not change across the whole span.**
- Everything else in the frame is worn down or replaced by the span.
- The camera stays fixed and the composition stays the same for the whole shot.
- The span is 100 years, and **no element of the frame dates it.**
- The seconds are spent unevenly across the span.
- The bird arrives only in the last second.

## PREFER

- The rock placed low and slightly off-centre, with the horizon on the upper third and the larger part of the frame given to sea and sky.

## ALLOW

- The sea's colour shifting across the span as the light and the weather turn.

# 17. GENERATION PRIORITIES

1. **One survivor** — the rock does not change. ⚠️ **Without it the span reads as several unrelated states, and the card has failed.** It outranks beauty.
2. **The camera never moves and never cuts** — leaving the place is a second shot.
3. **The times are stacked, not laid end to end** — a hundred years pass through one frame, in order.
4. **Uneven duration** — the shot lingers on the passage, not on the beginning or the end.
5. **No date stamp, no caption, no title card** — nothing in the frame carries the elapsed time.
6. **Everything else changes** — if only one thing moved, the span would not be legible.
7. **The bird is one, and it lands once, at the end.**
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 10-second continuous take (16:9) of a rock standing out of the sea, one clip, from a large-format frame on a tripod, standing in the place for the whole shot. Beats, deliberately uneven: [0-3s] rock, sea, sky, and a wave returning at the rock's foot — nothing has begun; [3-7s] time moves through the frame — waves come and return, the sea's colour turns, the light crosses, the clouds replace one another, and only the rock holds; [7-9s] everything around the rock is worn down — the sea thins and the far shoreline drops — and the rock's own face is not touched; [9-10s] a bird lands on the rock and stays. **A hundred years pass inside this one frame: the times are stacked, not laid end to end, and the shot never cuts and never skips time.** Nothing in the frame dates it. **The rock is the one survivor** — the whole span is legible because that one thing does not change. (No camera move, no pan, no zoom, no date stamp, no caption, no title card carrying elapsed time, no people, no boat, no building.)

## Visual Prompt

Large-format landscape photography of a rock standing out of the sea, the sea and sky carrying the frame alone. **f/64 deep focus: the rock, the water at its foot, and the far horizon all sharp at once.** Full tonal range from deep shadow to bright highlight, fine detail at every scale, unbroken depth from near water to far horizon, crisp edges, fine grain. Natural film color with a subtle cool cast. The rock sits low and slightly off-centre, the horizon on the upper third. No people, no figure, no boat, no building, no shallow depth of field, no HDR oversaturation, no illustration, no CGI, no lens flare, no readable text.

## Motion Prompt

**The rock does not move at all — it is the one thing the hundred years do not touch.** Everything around it moves: waves come and return at its foot, the sea's level and colour turn across the span, the light crosses the frame, the clouds replace one another, and the far shoreline is worn lower and lower. **The motion is continuous; the frame is never still even though the camera is.** At the last second **one bird lands and stays**, and after that it does not move. **The camera is set up on its tripod and stays there** — this is one place, held, with time passing through it; **a camera that left would make the return a second shot.** No cut, no cross-dissolve, no time-skip, no return to the place after leaving it, no aging makeup, no stated "years later."

## Camera Prompt

**A large-format frame on a tripod, set up before the shot and standing in the place for the whole take** — composed once, rock low and slightly off-centre with the horizon on the upper third, and then **left alone completely.** **A camera that left the place would make the return a second shot, and the place is never left.** No pan, no zoom, no drift, no rack, no handheld, no whip. Deep focus is held from the first frame to the last: the near water and the far horizon stay sharp at once. **What moves is the world** — waves, light, cloud, the far shoreline — **and the frame is the one thing the hundred years do not touch.** One continuous take; no cut, no cross-dissolve, no time-skip.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of this work and of every word it holds; **if any speech is placed in it, that speech is Japanese.** **No speech is placed in this shot.** No dialogue, no voice-over, no narration, no caption carrying elapsed time. Sound effects: the sea at the rock's foot, unbroken, with no single impact singled out. Ambient: open air, a distant waterline, and wind that rises and falls across the span. **Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell.**

## Negative Prompt

no shallow depth of field, no HDR oversaturation, no people, no CGI, no illustration, no cut, no time-skip, no date stamp, no caption, no title card carrying elapsed time, no aging makeup, no prosthetic, no cross-dissolve, no return to the place after leaving it, no camera move, no zoom, no pan, no drift, no rack, no bird flock, no second bird, no storm, no boat, no building, no readable text, no lens flare, no watermark, no on-screen subtitles, no background music

## Style Motion

**Everything is in focus, so nothing can hide in depth** — motion anywhere in the frame is equally visible at every scale, near and far, **and this shot's whole event is of that kind.** **What moves is the land's own time** — water, light, cloud shadow, the far shoreline giving way; **human-scale motion is out of scale here, and the one bird is the only exception the shot allows.** **The camera is set up, not followed** — a large-format frame stands on a tripod, and this shot is composed once and then left alone. **Stillness is close to the ground state** — the land may hold for the whole shot and the light is the event, **which is why the rock can carry the frame while the span passes.** **What this style does not do**: shallow focus pulls, handheld drift, fast motion, a figure entering the frame, cuts, animated skies. **Focus stays deep for the whole shot** — a plane of focus that narrows is a different style. (Source: the `Motion character` of the style card `landscape-photo`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `grammar-time-fold-s01-10s-01`
- Segment ID: `01-1`
- Specification Version: `0.3.0`
  ⚠️ **この行は、この仕様の*現在*の版である**——`L25` がここを読み、各テイクの
  `source_version`（**投入した時点の版**）と突き合わせて、**ずれを註に書く。**
  ⚠️ **註を同じ行に足してはならない。** **足すと、この行は読まれなくなる**
  （`specmap.SPEC_VERSION_LINE` は行末までを版とする）。
  **検査が黙ったことは、検査が通ったことではない。**
  ⚠️ **`0.2.0` から変わったのは §10 と §18 の `Camera Prompt`、そして §19 と §20 である**
  ——**演出の段（`skills/staging/`）がカメラを書き直した。** ⚠️ **ゆえに投入文字列が変わった**——
  **`media/` に在る1本は `0.2.0` の投入に対するものであり、この版はまだ生成されていない。**
- Generation Date: `2026-09-22`（⚠️ **根拠は戻ってきたファイルの時刻**——`media/16d3bd84-1f31-4a40-8ddc-4d01c8727ad6.mp4` の `02:59`。
  **著者が名乗った日付ではない。** ⚠️ **そのファイルは `0.2.0` の投入に対するものである**——
  **この版の投入は、まだ無い。**）
- Adopted Take: `—`（**まだ採用されていない。**⚠️ **テイクは1本、`media/` に在る**——
  **テイクの記録はまだ無い。** 記録を書くのは著者である（`projects/hitosara/media/README.md`）。
  ⚠️ **ファイル名は `NN__` の接頭辞を持たない**——**名前から記録を引けない。**
  ⚠️ **採用は選別であり、著者が編集である**（`CLAUDE.md`）。）

## Resolved Values

- Duration: `10s`
- References: `REF_LOCATION (一枚岩.base, 未作成) ／ REF_STYLE (landscape-photo, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
  ⚠️ **この行は「仕様が名指した参照」であって、「実際に渡した参照」ではない。**
  **この1本は、いま何も渡していない**（`attached: []`）。
- Temporal Structure: `4 beats, NON_UNIFORM — 3s / 4s / 2s / 1s. The passage = BEAT 2 at 4s (40%)`
- Camera Events: `none — the frame is set up once, before 0s, and stands for the whole shot`
- Action Events: `ACT_HOLD → ACT_WEAR → ACT_LAND`
- Audio Events: `no dialogue ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.3.0` — **演出の段（`skills/staging/`）で §10 と §18 の `Camera Prompt` を書き直した。**
⚠️ **変わったのはこの2つと §19・§20 だけである**——**§1–9 と §11–17 は同一。**
⚠️ **この版はまだ生成されていない**——`media/` に在る1本は `0.2.0` の投入に対するものである。
①（生成する）は著者のものであり、**②（測る）は開いていない**——
**測定はテイクの記録を要する**（`L25` はテイクが1本も無ければ走らない）。**テイクの記録はまだ無い。**
③（型の同定）と ④（直す）も開いていない。

⚠️ **この仕様で確かめたのは、文法が仕様として書けるかどうかである。**
**文法が効いたかどうかではない**——⚠️ **生成はこの基盤の外で起きる。**
⚠️ **生成は1度走った**（`0.2.0` の投入に対して）。 だが **`## Examples` はまだ `- —` である**——
**文法が効いたという記録は、まだどこにも無い。**

⚠️ **この作品は、形式カード `time-fold` が初めて使われた記録である。**

## Observed Problems

（**機械の測定は、まだ無い。** 戻ってきたファイルの測定は**テイクの記録**
（`verdict.machine.measured`）に書く——`L25` がそれを §1 と突き合わせる。
⚠️ **この行は「問題が無い」ことを言っていない。** **測っていないのである。**）

## Anticipated risks (to check in the first generation)

1. **The span may not read as a span.** If the shot changes only one thing, it reads as a single slow change rather than as a hundred years. **The survivor is what makes the difference — check that everything else really does turn over.**
2. **The rock may be eroded.** The most probable failure: the generator wears the rock down too, because that is what waves do to stone. ⚠️ **Then there is no survivor, and the grammar has failed** — the card requires one thing that does not change.
3. **The camera may drift.** A slow push or a slight zoom is the standard way a generator fills ten seconds. **The card forbids it** — leaving the place is a second shot.
4. **A date may appear.** A caption, a title card, a chyron, or a year rendered into the frame. **Check for it explicitly.**
5. **The sea may carry a boat or a building may enter.** Both are a second subject, and both date the frame.
6. **The bird may arrive early or in a flock.** §8 puts it in the last second, and §16 says one bird, once.
