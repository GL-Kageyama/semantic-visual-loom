# Wan 3.0 Full Specification — 神社 Clip 1/1 / 9s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**

⚠️ **この仕様は形式カード `recognizing-world` を1度だけ使う。**
カードの5つの欄が、この仕様の背骨である。

| カードの欄 | この1本の値 |
|---|---|
| `FIGURE` | **そこに居ない誰か。** この1本には、誰も写らない |
| `SIGN` | **雪の側の兆し。** 踏まれる前に、踏まれた形になる |
| `DEPTH` | **道が開くところまで。** 足跡の先で雪が解ける |
| `REFUSAL` | **灯籠だけは点かない。** ここで認知が止まる |

⚠️ **このカードは `video-spec` に文法を1つ足したものである。**
この仕様が足したのは **「兆しは環境に在り、社交には無い」という1点**だけである——
⚠️ **誰かが振り向くことは、場所が認知することではない。**
⚠️ **認知は積み上がる。** 「認知していない」から「認知した」への1カットは別の文法である——
**兆しが重なり、その重なりが時間である。**
⚠️ **`meaning-responsive` と混同しないこと。** あちらは世界が**ショットの意味**に答える。
こちらは**誰が居るか**に答える——**反応が何も意味しなくても、知覚した存在に反応する場所はこちらである。**

⚠️ **⚠️ この場所には床がある。** 他のすべてが応えても、**灯籠だけは応えない**——
**床の無い場所は、効果として読まれる。****床のある場所は、性格のある場所として読まれる。**

⚠️ **この作品は物語ではない。** 1ショットだけの最小の作品であり、
**7枚の文法カードの1枚が、仕様として立つかを試すために在る。**

---

# 1. VIDEO

- Duration: `9s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. **A place registers a presence that is never shown — and stops at one thing it will not do.**

# 2. WORLD

## World Concept

A shrine at midnight. Snow that no one has walked on takes the shape of footprints, front to back, **before anyone walks.** Past the footprints the snow melts and a way opens. **The lanterns, alone, do not light.**

## World Rules

- **The signs are environmental, not social.** Nobody turns, greets, or reacts — **that would be a scene about recognition, not a setting that recognises.**
- **The recognition accumulates.** ⚠️ **It does not switch on** — signs stack, and **the stacking is the time.** A single cut between unrecognised and recognised is a different grammar.
- **The setting has a floor.** ⚠️ **`REFUSAL`: the lanterns do not light.** Everything else answers; here the recognition stops.
- **The recognition is for someone who is not in the frame.** The footprints form with no walker in sight — **the card allows this, and calls it often the shot's point.**
- **No blanket mood change.** The place does not shift in atmosphere; **it does one specific thing at a time.**
- **The place's own sound is the place's**, not anyone's footsteps.
- **No caption and no voice-over announcing that the place knows.**
- **No legible text** appears anywhere.

## Visual Language

- Art Direction: A Japanese ukiyo-e woodblock print. Flat mineral-pigment colour planes in indigo, crimson and ochre over broad black; hand-carved ink outlines with visible chisel marks; wood-grain texture and print misregistration; **bold Japanese composition with diagonal depth and negative space.**
- Color Language: Broad black plus a few planes of indigo, crimson and ochre. ⚠️ **Flat fill is what this medium is** — a plane must not gain a gradient during the shot.
- Texture: Washi grain, print pressure marks, the wood-grain of the block, bleeding. **Flat light without shadows.**
- Rendering: True woodblock printing. Not photorealistic, no digital gradient, no 3D render, no soft shading.
- Visual Density: Low. **A snow-covered approach, lanterns along it, a torii at the far end, and the marks the place is making in the snow.**
- Time: 真夜中
- Atmosphere: Still and cold. **The place is not eerie; it is attentive.**

# 3. SUBJECTS

## The Approach in the Snow

- Reference: (none — the approach is not a registered entity; it is the subject of the shot)
- Appearance: The shrine's approach under untouched snow, running from the near side of the frame to the torii at the far end, with lanterns standing along both sides.
- Behavior: **It registers.** Footprints take shape in it, front to back, **with no one walking**; past them the snow gives way and a way opens. ⚠️ **The marks accumulate one after another — the surface is never switched from blank to marked.**
- Continuity Requirements: Must Preserve: **the approach's place in the frame, its diagonal, and the snow's flat untouched quality everywhere the marks have not reached.** May Change: the snow where the recognition has arrived.

## The Lanterns

- Reference: (none — the lanterns are not a registered entity)
- Appearance: Stone lanterns standing along both sides of the approach, unlit, dark against the snow.
- Behavior: **They do nothing.** ⚠️ **They are the floor** — everything else in the frame answers, and these do not. **They do not flicker, they do not glow, and they do not light at the end.**
- Continuity Requirements: Must Preserve: **their unlit state, their place, and their number.** May Change: nothing.

# 4. ENVIRONMENT

- Location: `神社`
- Environment Elements: The approach and its snow, the lanterns along both sides, the torii at the far end, and the shrine grounds beyond it.
- Environmental Behavior: **The snow is where everything happens.** It takes the shape of footprints ahead of any walker, and past them it gives way and opens a path. ⚠️ **Nothing else in the environment changes**: no wind moves the snow, no branch drops its load, no animal crosses, and **the air does not change.**

# 5. OBJECTS

- The approach, the snow, the lanterns, and the torii. **Nothing else is in the frame.**
- ⚠️ **No person, no figure, no priest, and no animal** at any point. **Nothing carries the recognition but the place.**

# 6. REFERENCES

- REF_LOCATION: `神社.base` — **未作成。** この作品の画像の経路はまだ1度も走っていない
  （`ledger.yaml` を見よ）(MEDIUM)
  ⚠️ **在ることと、渡したことは違う。** **この1本は、いま何も添付していない**
  （ショット記録の `attached: []` を見よ）。
- REF_STYLE: `mokuhanga` (HIGH)
- REF_FORMAT: `recognizing-world` — this defines the one grammar this shot is
- REF_SOURCE: `projects/grammar-recognizing-world/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: A place registers a presence and stops at one thing.
- Beginning: Midnight, untouched snow, and every lantern dark. **Nothing has been registered yet.**
- Turn: **The snow takes the shape of footprints ahead of any walker** — one, then another, front to back.
- Peak: **Past the footprints the snow gives way and a way opens.** The recognition has reached that far.
- Pull: **The lanterns stay dark.** Everything else has answered, and **this one thing has not.**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-3s` — density: `sparse` — Midnight. Snow no one has walked on, the lanterns along both sides, **and not one of them lit.**
  - BEAT 2 `3-6s` — density: `dense` — **The snow takes the shape of footprints**, front to back, with no walker in sight. ⚠️ **Not a switch — the signs accumulate, one after another.**
  - BEAT 3 `6-8s` — density: `dense` — Past the footprints **the snow melts and the way opens.** The recognition has reached that far.
  - BEAT 4 `8-9s` — density: `held` — **The lanterns do not light.** Everything else has answered; **this does not.**
- Temporal Density: ⚠️ **The seconds are not spread evenly** — the accumulation takes the middle, and **the refusal is given a full second of its own at the end.**

# 9. ACTION

- `ACT_BLANK` — Before: the approach is composed. After: **the frame holds, and nothing has been registered yet.**
- `ACT_REGISTER` — Before: the snow is untouched. After: **footprints have taken shape in it, front to back, with no walker.**
- `ACT_OPEN` — Before: the snow is still closed past the footprints. After: **it has given way and a way is open.**
- `ACT_REFUSE` — Before: the lanterns are dark. After: **they are dark.**
- Causes: **the presence of someone not in the frame.** ⚠️ **Nothing visible causes any of it** — no walker, no wind, no animal, and **there is no process beat.** ⚠️ **The refusal has no cause either; it is a floor, not a decision.**

# 10. CAMERA

- Camera Language: **A woodblock print's sheet, laid flat and held still** — the frame is an object on paper and not a window, and the composition is a print's: a bold diagonal from the near side to the torii at the far end, with the lanterns dividing the frame along it. ⚠️ **The style's physical law, in the card's own words** (`mokuhanga`) — **The camera is a sheet, not a window.** The frame holds still. A print is an object on paper, and a camera that travels turns it back into a scene.
- Camera Events: `0-9s` none — **the sheet is laid down once and holds for the whole take.** ⚠️ **A hold is an event, written with its range like any other**: timing `0-9s`; movement none; target the approach, from the near side to the torii; speed none. **What the hold is spent on is the registering** — the snow takes the marks, and **the frame does not have to travel for a place to answer.**
- Camera Behavior: **Still, and the stillness is what keeps this a print.** ⚠️ **The reason, which travels on into §18: the one thing that changes here changes in the snow and not in the viewpoint** — a camera that travelled would turn the sheet back into a scene, **and the scene is where the recognition would have to be staged instead of registered.** One continuous take; no cut.

# 11. MOTION

## Subject Motion

**The snow, and only the snow.** Footprints take shape in it, front to back, ahead of any walker; past them the surface gives way and opens. ⚠️ **The motion accumulates rather than switching** — one mark, then another, each landing where the last one stopped.

## Object Motion

**None.** The lanterns, the torii and the ground do not move. ⚠️ **The lanterns in particular do nothing at all** — they are the shot's floor, and any motion in them would be an answer.

## Environmental Motion

**The block re-prints rather than flows.** The image lands, and then lands again — and ⚠️ **between impressions the colour planes slip a little against the ink line, so an edge doubles and settles.** **The drift is the print's, not the subject's**, and it is the same drift for the whole shot. ⚠️ **The colour planes stay flat** — a plane that gains a gradient is a different style.

## Physical Characteristics

- Weight: **Snow has it, and so does the stone.** Nothing here is light — the marks in the snow are made *by* the snow, not on it.
- Inertia: **The accumulation has it** — once the marks have begun, they continue front to back at the same rate.
- Acceleration: None. **The signs arrive one after another at an even pace; what is uneven is only how the seconds are spent.**
- Fluidity: None. **Nothing flows here** — a print lands, and lands again.
- Impact: None. **Nothing touches the snow.**

# 12. EMOTION

- Emotional Arc: The steadiness of a place that has already decided, and the small coldness of the one thing it will not do.
- Emotional Events: The last second, when everything has answered and **the lanterns have not** — and the audience understands that this is not a failure but a floor.

# 13. LIGHTING

- Base Lighting: Flat light without shadows — **the medium's own light**, a print's light rather than a lamp's. Broad black and flat mineral planes carry the division of the frame.
- Lighting Events: ⚠️ **`0-9s` — none.** ⚠️ **This is the section this card is written into, and here the event is a non-event: the lanterns do not light, and nothing else in the frame changes its light either.** ⚠️ **No glow, no brightening, no dawn, and no blanket mood change** — the recognition is not staged as light, and **the refusal is staged as the absence of one specific light.**

# 14. AUDIO

- Dialogue: None.
- Sound Effects: **The place's own sound** — snow's particular quiet, and no footsteps at all, because there is no walker.
- Music: None.
- Environment: Cold, open, and still. **The sound belongs to the place and not to anyone in it.**

# 15. CONTINUITY

- Identity: The same approach, the same lanterns and the same torii for the whole shot — **same place, same composition, same number of lanterns.**
- Spatial: **The composition does not change at all.** The diagonal from the near side to the torii holds, and the marks appear within it without moving it.
- Temporal: One continuous accumulation. ⚠️ **Nothing is skipped, and there is no cut between unrecognised and recognised states.**
- Visual: **The ink line stays carved for the whole shot** and the planes stay flat. A line that softens into a brush stroke is a different style.
- Motion: **The snow accumulates; everything else holds.**
- Sound: Unbroken, and no footsteps enter it.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止）

- No character reacting in place of the setting — **nobody turns, greets, or appears.**
- No cut between unrecognised and recognised states.
- **No lantern lighting** — not a flicker, not a glow, not at the end.
- No blanket mood change.
- No setting without a floor — **the refusal must be legible as a refusal.**
- No person, no figure, no priest, no animal.
- No wind, and nothing dropping its load.
- No on-screen caption and no voice-over announcing recognition.
- No soft shading, no digital gradient, no 3D render, **not photorealistic.**
- No readable text of any kind.

## MUST

- **The signs are in the setting** — snow, the way it takes a shape, the way it gives way.
- **The recognition accumulates** rather than switching on.
- **The footprints form ahead of any walker**, and no walker is shown.
- **The lanterns stay dark for the whole shot**, including the last frame.
- **The camera does not move**, and the frame is a print rather than a window.
- The colour planes stay flat and the ink line stays carved.

## PREFER

- The torii small and legible at the far end, with the lanterns dividing the frame along the approach's diagonal.

## ALLOW

- Print misregistration doubling an edge and settling, as the style's own motion under the shot's.

# 17. GENERATION PRIORITIES

1. **The floor is legible** — ⚠️ **the lanterns stay dark while everything else answers.** Without it the place reads as an effect. It outranks beauty.
2. **The signs are environmental** — nothing social, and no figure anywhere.
3. **The recognition accumulates** — not a cut, not a switch.
4. **The footprints form ahead of any walker**, with no walker shown.
5. **No mood change** — one specific thing happens at a time.
6. **The camera does not move**, and the frame stays a print.
7. **The planes stay flat and the line stays carved.**
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 9-second continuous take (16:9) of a shrine approach at midnight under untouched snow, one clip, from a woodblock print's sheet laid flat and held still. Beats, deliberately uneven: [0-3s] midnight — snow that no one has walked on, lanterns along both sides of the approach, and not one of them lit; [3-6s] **the snow takes the shape of footprints, front to back, with no walker anywhere in the frame** — and this accumulates, one mark after another, rather than switching on; [6-8s] past the footprints the snow gives way and **a way opens**; [8-9s] **the lanterns do not light.** Everything in the frame answers except that one thing: **the place registers a presence that is never shown, and stops at what it will not do.** Nothing social happens — nobody turns, greets or appears — and the recognition is never announced. (No character reacting in place of the setting, no cut between unrecognised and recognised states, no lantern lighting, no blanket mood change, no person, no figure, no animal, no wind, no on-screen caption, no voice-over announcing recognition.)

## Visual Prompt

A Japanese ukiyo-e woodblock print of a snow-covered shrine approach at midnight. Flat mineral-pigment colour planes in indigo, crimson and ochre over broad black; hand-carved ink outlines with visible chisel marks; wood-grain texture and print misregistration; bold Japanese composition with diagonal depth and negative space; washi grain, print pressure marks, **flat light without shadows**. Stone lanterns stand along both sides of the approach, unlit, dark against the snow, with a torii small at the far end. The colour planes stay flat and never gain a gradient. Not photorealistic, no digital gradient, no 3D render, no soft shading, no readable text.

## Motion Prompt

**The block re-prints rather than flows** — an image lands, and then lands again, and **between impressions the colour planes slip a little against the ink line so an edge doubles and settles.** The drift is the print's and not the subject's. **The snow is what registers**: footprints take shape in it, front to back, **with no walker anywhere in the frame**, and past them the snow gives way and a way opens. **The marks accumulate — one after another, never switched on at once.** Everything else holds completely: the lanterns, the torii and the ground do not move, **and the lanterns do not light at any point, including the last frame.** Nothing social happens and no figure enters. **The sheet is laid flat and held still** — the marks change in the snow, and the frame stays where it was laid. No smooth continuous animation, no dissolving gradients, no morphing contours, no motion blur, no camera travel, no blanket mood change.

## Camera Prompt

**A woodblock print's sheet, laid flat and held still for the whole take** — **the frame is an object on paper and not a window.** No pan, no push, no pull, no rack, no handheld, and no camera travel: **a print is an object on paper, and a camera that travels turns it back into a scene.** The composition is a bold diagonal from the near side of the frame to the torii at the far end, with the lanterns dividing the frame along it, and it does not change for the whole shot. **The one thing that changes here changes in the snow** — the marks take shape in it, front to back, with no walker — and **the frame stays where it was laid while that happens.** One continuous take; no cut.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of this work and of every word it holds; **if any speech is placed in it, that speech is Japanese.** **No speech is placed in this shot.** No dialogue, no voice-over, no narration, and **no voice-over announcing recognition.** Sound effects: **the place's own sound** — snow's particular quiet, and **no footsteps at all, because there is no walker.** Ambient: cold, open and still, with the sound belonging to the place and not to anyone in it. **Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell.**

## Negative Prompt

not photorealistic, no digital gradient, no 3D render, no soft shading, no character reacting in place of the setting, no cut between unrecognised and recognised states, no on-screen caption, no voice-over announcing recognition, no blanket mood change, no setting without a floor, no person, no figure, no priest, no animal, no lantern lighting, no wind, no readable text, no watermark, no on-screen subtitles, no background music

## Style Motion

**The block is the mover, and it works by impression** — the frame re-prints rather than flows: an image lands, and then lands again, **and this shot's accumulation of marks arrives the same way, one landing after another.** **Misregistration is the motion** — between impressions the colour planes slip a little against the ink line, so an edge doubles and settles; **the drift is the print's, not the subject's**, which is why the snow's own registering reads as a separate layer above it. **The camera is a sheet, not a window** — the frame holds still, **and this shot holds completely.** **Stillness is the ground; the planes stay flat** — a colour plane must not gain a gradient during the shot, **and the one thing this shot refuses is staged as an absence of light rather than as a change in the print.** ⚠️ **What this style does not do**: smooth continuous animation, dissolving gradients, morphing contours, motion blur, or a camera that moves for its own sake. ⚠️ **The ink line stays carved for the whole shot** — a line that softens into a brush stroke is a different style. (Source: the `Motion character` of the style card `mokuhanga`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `grammar-recognizing-world-s01-9s-01`
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
- Generation Date: `2026-09-22`（⚠️ **根拠は戻ってきたファイルの時刻**——`media/9ba21ee4-b44b-4e50-9114-bbdd05690fe5.mp4` の `03:22`。
  **著者が名乗った日付ではない。** ⚠️ **そのファイルは `0.2.0` の投入に対するものである**——
  **この版の投入は、まだ無い。**）
- Adopted Take: `—`（**まだ採用されていない。**⚠️ **テイクは1本、`media/` に在る**——
  **テイクの記録はまだ無い。** 記録を書くのは著者である（`projects/hitosara/media/README.md`）。
  ⚠️ **ファイル名は `NN__` の接頭辞を持たない**——**名前から記録を引けない。**
  ⚠️ **採用は選別であり、著者が編集である**（`CLAUDE.md`）。）

## Resolved Values

- Duration: `9s`
- References: `REF_LOCATION (神社.base, 未作成) ／ REF_STYLE (mokuhanga, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
  ⚠️ **この行は「仕様が名指した参照」であって、「実際に渡した参照」ではない。**
  **この1本は、いま何も渡していない**（`attached: []`）。
- Temporal Structure: `4 beats, NON_UNIFORM — 3s / 3s / 2s / 1s. The accumulation = BEAT 2 and 3; the refusal = BEAT 4 at 1s`
- Camera Events: `none — the sheet is laid down once at 0s and holds for the whole shot`
- Action Events: `ACT_BLANK → ACT_REGISTER → ACT_OPEN → ACT_REFUSE`
- Audio Events: `no dialogue ／ no music ／ no footsteps`
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

⚠️ **この作品は、形式カード `recognizing-world` が初めて使われた記録である。**

## Observed Problems

（**機械の測定は、まだ無い。** 戻ってきたファイルの測定は**テイクの記録**
（`verdict.machine.measured`）に書く——`L25` がそれを §1 と突き合わせる。
⚠️ **この行は「問題が無い」ことを言っていない。** **測っていないのである。**）

## Anticipated risks (to check in the first generation)

1. **The lanterns may light.** ⚠️ **This is the likeliest failure and the most damaging**: a generator asked for an atmospheric night shrine will light the lanterns, because that is what makes the shot look finished. **Then there is no floor, and the place reads as an effect.** Check the last second especially.
2. **A walker may appear.** The footprints must form with no one in the frame. A generator will very often supply the person making them. **Check every frame.**
3. **The recognition may switch on.** The snow may flip from blank to fully marked in one step, which reads as a cut between states — **§8 asks for the marks to accumulate one after another.**
4. **The snow may react everywhere.** A blanket change — the whole approach melting, the whole frame brightening — is a mood change rather than a specific sign. **§4 says the marks appear where the recognition has reached, and not everywhere.**
5. **The lanterns may be omitted.** The other failure mode: the floor is invisible because the thing that refuses is not in frame at all. **§3 requires them present, unlit, and counted.**
6. **The print may soften.** Gradients arriving in the flat planes, or the ink line turning into a brush stroke, means the style has drifted.
