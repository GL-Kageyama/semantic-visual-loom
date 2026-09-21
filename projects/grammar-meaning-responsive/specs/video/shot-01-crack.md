# Wan 3.0 Full Specification — 台所 Clip 1/1 / 5s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**

⚠️ **この仕様は形式カード `meaning-responsive` を1度だけ使う。**
カードの4つの欄が、この仕様の背骨である。

| カードの欄 | この1本の値 |
|---|---|
| `BEARER` | **「大丈夫」という言葉。** 名指され、そして行為しない |
| `ANSWER` | **ひびが一本、走る。** 答えは世界の側に在る |
| `DELAY` | **一拍。** 即答せず、終端でもない |
| `LIMIT` | **一本で止まる。** 割れず、落ちず、二本目は来ない |

⚠️ **このカードは `video-spec` に文法を1つ足したものである。**
この仕様が足したのは **「枠の中の何も、この答えを起こさない」という1点**だけである——
**物は入ってこず、光源は変わらず、誰も動かない。****絵は、意味そのものに答えている。**
⚠️ **`impossible-camera` と混同しないこと。** あちらは視点がカメラの行けないところへ行く。
こちらは**視点が意味に応える**——**人物が感じたためにカメラが動くなら、それはあちらではなくこちらである。**
⚠️ **この1本のカメラは、動かない。** カメラの移動は意味についての*陳述*であり、
**この文法は、世界にそれを言わせたい。**

⚠️ **⚠️ この1本は声を持つ。** 担い手が言葉そのものである以上、
`bible.language` がここでは**実際に効く**——しかも §14 の声は**一曲だけ**である。

⚠️ **この作品は物語ではない。** 1ショットだけの最小の作品であり、
**7枚の文法カードの1枚が、仕様として立つかを試すために在る。**

---

# 1. VIDEO

- Duration: `5s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. **The world answers a meaning, once, with a delay — and the camera does not answer at all.**

# 2. WORLD

## World Concept

A kitchen in the afternoon. One word is placed in it — 「大丈夫」, once. One beat later, **a single crack runs across the window glass and stops.** Nobody moves.

## World Rules

- **Nothing in the frame causes the answer.** No object enters, no light source changes, no one acts. **The picture answers the meaning itself.**
- **The bearer is named, and it does not act.** The bearer is the word 「大丈夫」 — **the picture answers the bearer; the bearer does not make the picture answer.**
- **The answer is in the world, not in the camera.** A surface gives way. **A camera move would be a statement *about* the meaning, and this grammar wants the world to make it.**
- **The delay is composed.** ⚠️ **Answering instantly reads as a cut; answering at the end of the clip reads as a reveal.** One beat sits between the two.
- **The limit is stated.** The answer reaches one crack and stops — **an answer that reached everything would read as a colour grade, not as a response.**
- **Nobody moves.** The subject is stopped; **what moves is the light, and the crack.**
- **No musical cue carries the meaning.** The world carries it.
- **No caption and no voice-over names what the picture is answering.**
- **No legible text** appears anywhere.

## Visual Language

- Art Direction: An oil painting. Thick impasto brushstrokes, raised pigment, canvas weave, chiaroscuro, fine craquelure, translucent glaze layers, dry hardened strokes. **Strong light and dark carry the composition.**
- Color Language: Oil deepened through glazes. ⚠️ **The palette stays deepened for the whole shot** — a colour that flattens or turns bright is a different style.
- Texture: Impasto, canvas weave, craquelure, the hardness of strokes left to dry.
- Rendering: True oil on canvas. Not digital, no flat colour, no airbrush smoothness.
- Visual Density: Low. **A figure at a window, the light across the paint, and one crack.**
- Time: 昼下がり
- Atmosphere: Held and ordinary. **The room is not tense; it simply answers.**

# 3. SUBJECTS

## The Figure at the Window

- Reference: `窓辺の人物.identity` (MEDIUM)
- Appearance: One person seated at the kitchen window, **facing out through the glass.** Seen from the side, in the room's own light.
- Behavior: **Nothing.** ⚠️ **The figure does not move for the whole shot** — the posture, the direction of the face, and the hands stay exactly as they were. **The word is placed, and the figure does not follow it with anything.**
- Continuity Requirements: Must Preserve: **posture, direction of gaze, and position.** May Change: nothing.

## The Window Glass

- Reference: (none — the glass is not a registered entity; it is the surface the answer arrives on)
- Appearance: A pane of glass in the kitchen window, catching the afternoon light across its surface.
- Behavior: **It gives way once.** A single crack runs across it — **and stops.** ⚠️ **Nothing strikes it, and nothing is thrown at it.** It does not shatter, it does not fall out, and it does not crack a second time.
- Continuity Requirements: Must Preserve: **the pane's place in the frame and its legibility as one pane.** May Change: exactly one crack, once.

# 4. ENVIRONMENT

- Location: `台所`
- Environment Elements: A lived-in kitchen in the afternoon — the window and its light, the surface the figure sits at, the room behind them.
- Environmental Behavior: **Almost nothing.** The afternoon light travels across the raised paint as the shot holds — **that is the only environmental motion before the crack, and it is the same light throughout.** ⚠️ **No weather, no draught, no object falling, and nothing crossing the frame.**

# 5. OBJECTS

- The window, the surface, and whatever the room holds quietly. **Nothing in the frame is an instrument of the answer.**
- ⚠️ **No thrown object, no stone, no bird, no branch, no door, and no second pane.** Nothing touches the glass at any point.

# 6. REFERENCES

- REF_LOCATION: `台所.base` — **未作成。** この作品の画像の経路はまだ1度も走っていない
  （`ledger.yaml` を見よ）(MEDIUM)
  ⚠️ **在ることと、渡したことは違う。** **この1本は、いま何も添付していない**
  （ショット記録の `attached: []` を見よ）。
- REF_STYLE: `oil-painting` (HIGH)
- REF_FORMAT: `meaning-responsive` — this defines the one grammar this shot is
- REF_SOURCE: `projects/grammar-meaning-responsive/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The world answers one word, one beat later, with one crack.
- Beginning: An afternoon kitchen, a figure at the window, **and one word placed.**
- Turn: **One beat passes and nothing happens** — the delay, held open.
- Peak: **The crack runs and stops.**
- Pull: Nothing follows. **Nobody moves, no second crack comes, and the crack's meaning is never named** — the audience is left to make it.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — The word 「大丈夫」 is placed, once. The figure faces out. Nothing enters, the light does not change, nobody moves.
  - BEAT 2 `2-3s` — density: `held` — **The delay.** Nothing happens. **This one second is the lag itself.**
  - BEAT 3 `3-4s` — density: `dense` — **The crack runs** across the pane and stops. Nobody moves, and nothing has touched the glass.
  - BEAT 4 `4-5s` — density: `held` — The crack stays stopped. **It does not shatter, it does not fall, and no second crack comes.**
- Temporal Density: ⚠️ **The delay is composed, and it is not at either end** — an instant answer would read as a cut and a last-frame answer would read as a reveal.

# 9. ACTION

- `ACT_PLACE` — Before: the room is as it was. After: **one word has been placed in it, and nothing else has changed.**
- `ACT_WAIT` — Before: the word has been placed. After: **one beat has passed with nothing happening.**
- `ACT_ANSWER` — Before: the pane is whole. After: **one crack has run across it and stopped.**
- Causes: **⚠️ none.** There is no visible cause — **nothing in the frame makes the glass give way, and there is no process beat.** ⚠️ **The cause is absent by construction; staging one would be a different grammar.**

# 10. CAMERA

- Camera Language: **An oil painting's frame, placed with the weight of something set down.** The composition is decided once, the figure at the window sits inside it, and the frame is left where it was put. ⚠️ **The style's physical law, in the card's own words** (`oil-painting`) — **The camera has weight.** It holds, or moves with the slowness of a heavy dolly. Chiaroscuro is spent by a camera that hurries.
- Camera Events: `0-5s` none — **the frame is set down once and holds.** ⚠️ **A hold is an event, written with its range like any other**: timing `0-5s`; movement none; target the window and the figure inside it; speed none. **What the hold is spent on is the surface** — the light travels across the impasto and the paint stays, **and the frame does not have to travel for that to be visible.**
- Camera Behavior: **Held, and the hold stays a statement about the world rather than about the meaning.** ⚠️ **The reason, which travels on into §18: a camera move here would be the shot telling the audience what the crack means** — and **naming the meaning is the one thing this grammar refuses.** One continuous take; no cut.

# 11. MOTION

## Subject Motion

**None.** The figure at the window does not move at all — posture, gaze and hands hold for the whole five seconds. ⚠️ **This is why the shot's mode is `still`: the subject is stopped, and the picture is not frozen.**

## Object Motion

**None.** Nothing in the frame is moved, thrown, or set down.

## Environmental Motion

**The light, and then the crack.** Through the first three beats the afternoon light travels across the raised impasto — ridges catch and release, and the same stroke reads differently a moment later. **The paint stays; the reading of it changes.** At `3-4s` the pane gives way: one crack runs across it **and stops.** ⚠️ **After that the light keeps doing exactly what it was doing** — the answer does not change the room's behaviour, and it does not spread.

## Physical Characteristics

- Weight: The room has it. **The camera has it too — a heavy frame, held.**
- Inertia: **The figure has it completely** — stillness here is not an absence of motion but a mass that is not moving.
- Acceleration: None. ⚠️ **The crack does not accelerate and does not slow; it runs and it stops.**
- Fluidity: None. **Oil does not flow, it settles** — and this shot's one event is a solid giving way, not a liquid moving.
- Impact: **None is shown.** ⚠️ **Nothing strikes the glass.** The crack is not an impact; it is an answer.

# 12. EMOTION

- Emotional Arc: The ordinary steadiness of a room in the afternoon, and the small wrongness of a world that has just answered.
- Emotional Events: The beat in which nothing happens — **the audience waits through it, and the waiting is what the crack lands in.**

# 13. LIGHTING

- Base Lighting: Afternoon light through the window, **chiaroscuro-strong** — the light side and the dark side clearly divided, deepened through glazes.
- Lighting Events: `0-5s` — **none that the shot stages.** ⚠️ **The light travels across the raised paint as the frame holds, and that is the only light behaviour in the shot.** ⚠️ **The crack does not change the light**: no flare, no flash, no brightening, no answering glow.

# 14. AUDIO

- Dialogue: **One word, once — 「大丈夫」, in Japanese, placed in the first two seconds and not repeated.**
- Sound Effects: Almost none — **the room's own small quiet**, and the small dry sound of the pane giving way.
- Music: None.
- Environment: An ordinary interior in the afternoon, close and low.

# 15. CONTINUITY

- Identity: The same figure for the whole shot — **same posture, same direction of gaze, same place.** The same pane throughout.
- Spatial: **The composition does not change at all.** The figure's position and the pane's place in the frame hold, and the crack does not move them.
- Temporal: One held moment with one answer in it. **Nothing is skipped, and the delay is not compressed.**
- Visual: Chiaroscuro holds, the impasto keeps its ridges, and **the palette stays deepened through glazes** for the whole shot.
- Motion: **The subject is stopped and the light is moving.** ⚠️ **There is no frozen frame anywhere in it** — stillness here is the subject's, not the picture's.
- Sound: The room's quiet is unbroken.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止）

- No visible cause, and **no on-screen actor causing the change.**
- No camera move answering the meaning, **no rack focus carrying the meaning**, and no cut.
- No blanket colour grade — **the answer must not read as a filter.**
- No second crack, no shattering, no falling glass.
- No musical cue carrying the meaning.
- No caption and no voice-over naming the meaning.
- No flat colour, no airbrush smoothness, not digital.
- No readable text of any kind, and no on-screen subtitles.

## MUST

- **Nobody moves** — the figure holds its posture for the whole shot.
- **The delay is one beat**, and it is neither instant nor at the end.
- **The answer is one crack, in the world**, and it stops.
- **Nothing strikes the glass**, and nothing enters the frame.
- **The camera does not move**, and it does not answer.
- The light does not change when the crack runs.

## PREFER

- The figure and the pane both in frame, with the crack visible enough to be unmistakable and small enough not to be a spectacle.

## ALLOW

- The light travelling across the raised paint as the frame holds.

# 17. GENERATION PRIORITIES

1. **No visible cause.** ⚠️ **The moment anything in the frame explains the crack, the grammar is gone.** It outranks beauty.
2. **Nobody moves.** The stillness is the shot's ground, and the answer lands in it.
3. **The delay is one beat** — not instant, not at the end.
4. **The crack stops at one.** It does not spread, and no second one comes.
5. **The camera does not move and does not answer.**
6. **The meaning is never named** — no caption, no voice-over, no musical cue.
7. **The light does not change when the crack runs.**
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 5-second continuous take (16:9) of an afternoon kitchen, one clip, from a frame set down once and held. Beats: [0-2s] one word is placed in the room once — 「大丈夫」 — while a figure seated at the window faces out through the glass, and nothing else happens: nothing enters, the light does not change, nobody moves; [2-3s] **the delay** — nothing happens at all, and this one second is the lag itself; [3-4s] **one crack runs across the window glass and stops** — nobody moves, and nothing has touched the glass; [4-5s] the crack stays stopped and nothing follows it. **Nothing in the frame causes the crack: no object enters, no light source changes, and no one acts — the picture answers the meaning itself, and it is never named.** **The camera is set down once and holds — a camera move here would be the shot telling the audience what the crack means.** (No visible cause, no on-screen actor causing the change, no camera move answering the meaning, no rack focus carrying the meaning, no second crack, no shattering, no falling glass, no caption naming the meaning, no voice-over naming the meaning.)

## Visual Prompt

An oil painting of an afternoon kitchen with a figure seated at the window. Thick impasto brushstrokes, raised pigment, canvas weave, chiaroscuro, fine craquelure, translucent glaze layers, dry hardened strokes. **Strong light and dark carry the composition**, and the palette is deepened through glazes and stays deepened for the whole shot. The afternoon light catches the ridges of the paint. The pane is whole at first, then carries one crack. Low visual density: a figure, a window, the light across the paint. No flat colour, no airbrush smoothness, not digital, no readable text, no on-screen subtitles, no watermark.

## Motion Prompt

**The subject does not move at all.** The figure seated at the window holds posture, gaze and hands for the whole shot — **the stillness is the ground the answer lands in.** What moves is the light: it travels across the raised impasto so ridges catch and release, **and the paint stays while the reading of it changes.** At the third beat **one crack runs across the window glass and stops** — it does not shatter, it does not fall, and no second crack comes. **Nothing strikes the glass and nothing in the frame causes it.** After the crack the light keeps doing exactly what it was doing: the answer does not spread and does not change the room. **The camera is set down once and holds, and no move of any kind answers the crack** — the crack is the event, and the camera is not a second one. No flowing liquid motion, no contour morphing, no motion blur, no camera move, no rack focus carrying the meaning.

## Camera Prompt

**An oil painting's frame, set down once and left where it was put** — the composition is decided before the shot, the figure at the window sits inside it, and **the frame does not travel.** **The style permits a camera that moves with the slowness of a heavy dolly; this shot spends none of it** — **the light already travels across the impasto, and a still frame is what lets the reading of the paint change without the camera announcing it.** No move of any kind answers the crack: **the crack is the event, and the camera is not a second one.** One continuous take; no cut, and no rack focus carrying the meaning.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of this work and of every word it holds, **and the one word this shot places is spoken in Japanese: 「大丈夫」 is spoken once, in the first two seconds, and is not repeated.** No narration, no voice-over, **and no voice-over naming what the picture is answering.** No caption and no on-screen subtitles. Sound effects: almost none — the room's own small quiet, and the small dry sound of the pane giving way. Ambient: an ordinary interior in the afternoon, close and low. **Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell, and no musical cue carrying the meaning.**

## Negative Prompt

not digital, no flat color, no airbrush smoothness, no visible cause, no camera move answering the meaning, no cut, no rack focus carrying the meaning, no on-screen actor causing the change, no blanket colour grade, no caption naming the meaning, no voice-over naming the meaning, no second crack, no shattering, no falling glass, no musical cue, no readable text, no watermark, no on-screen subtitles, no background music

## Style Motion

**Oil is the slowest mover here — it does not flow, it settles.** What changes in the frame is not the shape but the surface: pigment deepening, a glaze sinking, **and this shot's held frame is exactly what that needs.** **The light does the moving** — it travels across the raised impasto, so ridges catch and release and the same stroke reads differently a moment later; **the paint stays and the reading of it changes.** **The camera has weight** — it holds, or moves with the slowness of a heavy dolly, **and this shot holds entirely, because a camera that answered the crack would be the shot telling the audience what the crack means.** **Stillness is the ground** — a held frame is native to this style, **and the one event here is a solid giving way rather than anything flowing.** **What this style does not do**: flowing liquid motion, contour morphing, fast cuts, digital smoothness, motion blur, or a camera that moves for its own sake. **The palette stays deepened through glazes** — a colour that flattens or turns bright is a different style. (Source: the `Motion character` of the style card `oil-painting`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `grammar-meaning-responsive-s01-5s-01`
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
- Generation Date: `2026-09-22`（⚠️ **根拠は戻ってきたファイルの時刻**——`media/f04ee826-ba52-4bd7-99e0-601b219f29ea.mp4` の `03:20`。
  **著者が名乗った日付ではない。** ⚠️ **そのファイルは `0.2.0` の投入に対するものである**——
  **この版の投入は、まだ無い。**）
- Adopted Take: `—`（**まだ採用されていない。**⚠️ **テイクは1本、`media/` に在る**——
  **テイクの記録はまだ無い。** 記録を書くのは著者である（`projects/hitosara/media/README.md`）。
  ⚠️ **ファイル名は `NN__` の接頭辞を持たない**——**名前から記録を引けない。**
  ⚠️ **採用は選別であり、著者が編集である**（`CLAUDE.md`）。）

## Resolved Values

- Duration: `5s`
- References: `REF_LOCATION (台所.base, 未作成) ／ REF_STYLE (oil-painting, HIGH) ／ REF_CHARACTER (窓辺の人物.identity, MEDIUM) ／ REF_SOURCE (bible.yaml, CRITICAL)`
  ⚠️ **この行は「仕様が名指した参照」であって、「実際に渡した参照」ではない。**
  **この1本は、いま何も渡していない**（`attached: []`）。
- Temporal Structure: `4 beats, NON_UNIFORM — 2s / 1s / 1s / 1s. The delay = BEAT 2 at 1s; the answer = BEAT 3 at 1s`
- Camera Events: `none — the frame is set down once at 0s and holds; it does not answer`
- Action Events: `ACT_PLACE → ACT_WAIT → ACT_ANSWER`
- Audio Events: `one word, once ／ no music ／ no narration`
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

⚠️ **この作品は、形式カード `meaning-responsive` が初めて使われた記録である。**
⚠️ **この作品は、7本のうちで唯一、発話を持つ。** ゆえに **`bible.language` の宣言が
実際に効く唯一の1本**である——**他の6本では、この宣言は空振りしている。**

## Observed Problems

（**機械の測定は、まだ無い。** 戻ってきたファイルの測定は**テイクの記録**
（`verdict.machine.measured`）に書く——`L25` がそれを §1 と突き合わせる。
⚠️ **この行は「問題が無い」ことを言っていない。** **測っていないのである。**）

## Anticipated risks (to check in the first generation)

1. **A visible cause may be staged.** A generator asked for a cracking window will very often put something in the frame to break it — a bird, a stone, a branch, a gust. ⚠️ **Any of those ends the grammar.** Check the frames before the crack.
2. **The delay may be collapsed.** The crack may arrive on the same beat as the word, which reads as a cut. **§8 puts a full second of nothing between them.**
3. **The camera may answer.** A push-in or a rack focus on the crack is the standard way a drama marks a revelation — **and it is exactly what this card forbids.**
4. **It may not stop at one.** The crack may spread, the pane may shatter, or a second crack may come. **§8's last beat says it stays stopped.**
5. **The meaning may be named.** A caption, a subtitle, a voice-over, or a musical sting on the crack. ⚠️ **With speech in this shot, check the subtitles especially** — a burned-in rendering of 「大丈夫」 is the measured failure mode.
6. **The answer may read as a grade.** If the whole frame darkens, brightens or shifts when the crack runs, the answer has reached everything and stopped being a response.
