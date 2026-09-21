# Wan 3.0 Full Specification — 角砂糖 Clip 1/1 / 8s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**

⚠️ **この仕様は形式カード `transformation` を1度だけ使う。**
カードの4つの欄が、この仕様の背骨である。

| カードの欄 | この1本の値 |
|---|---|
| `FROM` | 熱い紅茶の中の、角の立った白い立方体 |
| `TO` | 花の形 |
| `TRIGGER` | **熱。** 茶は既に熱く、**枠の中に新しい原因は現れない** |
| `KEEP` | **白さ。** 花は砂糖であり、砂糖は白い |

⚠️ **このカードは `video-spec` に文法を1つ足したものである。**
§1–20 は `video-spec` が要求するとおりに埋めてあり、この仕様が足したのは
**「変化は時間であり、圧縮されない」という1点**だけである。

⚠️ **この作品は物語ではない。** 1ショットだけの最小の作品であり、
**7枚の文法カードの1枚が、仕様として立つかを試すために在る。**
⚠️ **ゆえに、この仕様を物語として読まないこと。** ここには人物も、話数も、場所の移動も無い。

---

# 1. VIDEO

- Duration: `8s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change — the cube becomes a flower
  — **and the shot spends its seconds on the passage itself, not on the two states.**

# 2. WORLD

## World Concept

Hot tea, and one sugar cube inside it. **There is no clock** — not because time is withheld,
but because there is nothing else for time to pass through. Before the corners go and after
the flower is there: that is all of it.

## World Rules

- **One thing changes, and only one.** The cube becomes a flower. Nothing else in the frame changes at all.
- **The change is never cut.** No cut, no dissolve, no wipe — a cut is the one thing this grammar exists to remove.
- **No intermediate stage is held.** The form between cube and flower is never stopped and shown.
- **Whiteness is kept across the change.** The flower is sugar, and sugar is white.
- **It does not return.** The flower is not undone inside this clip.
- **No person, no hand, no spoon, no cup rim** is in the frame at any point.
- **No legible text** appears anywhere.

## Visual Language

- Art Direction: Extreme macro photography. One white sugar cube at the scale where it fills the frame — granular faces, tiny facets catching light, the tea's amber behind it dissolving into smooth rounded defocus.
- Color Language: Near-monochrome. **The white of the sugar against the tea's single amber; no third hue anywhere in the frame.**
- Texture: Enlarged granularity, the cube's porous faces, the wet sheen where tea has reached it.
- Rendering: True macro photography. **A razor-thin plane of focus**; whatever leaves it goes to smooth rounded bokeh. Not an illustration, not a render.
- Visual Density: Very low. The cube, the tea immediately around it, and defocus.
- Time: 時刻を持たない
- Atmosphere: Still and hot. **The only thing alive in the frame is the cube's outline.**

# 3. SUBJECTS

## The Sugar Cube

- Reference: (none — the cube is not a registered entity; it is the subject of the shot)
- Appearance: A white sugar cube, its corners sharp and its faces slightly porous, wet where the tea has already reached it. **White is the whole of its colour.**
- Behavior: The corners go first. **The mass keeps its place and loses its edges** — the outline rounds, then resolves, once, into a flower. **It is not stirred, not pushed, and not touched.**
- Continuity Requirements: Must Preserve: the white, the granular surface, the place in the frame. May Change: the silhouette — **the corners are what the change spends.**

# 4. ENVIRONMENT

- Location: `紅茶`
- Environment Elements: Hot tea at the scale of the cube. Its surface is not in frame; what is in frame is the tea immediately around the cube, and the light coming through it.
- Environmental Behavior: The tea is still — **it is not stirred.** Only the slow local current the cube itself makes as it goes. **No steam, no bubble, no foam, and nothing else drifts across the frame.**

# 5. OBJECTS

- The cube is both the object and the subject. **There is no second object.**
- No spoon, no cup wall, no rim, no saucer, no tea leaf, no grain of sugar loose in the frame. **Nothing else is in the frame.**

# 6. REFERENCES

- REF_LOCATION: `紅茶.base` — **未作成。** この作品の画像の経路はまだ1度も走っていない
  （`ledger.yaml` を見よ）(MEDIUM)
  ⚠️ **在ることと、渡したことは違う。** **この1本は、いま何も添付していない**
  （ショット記録の `attached: []` を見よ）。
  ⚠️ **`紅茶.geography` も同じである**——位置関係は§4の文が持ち、ボードはまだ無い。
- REF_STYLE: `macro-photo` (HIGH)
- REF_FORMAT: `transformation` — this defines the one grammar this shot is
- REF_SOURCE: `projects/grammar-transformation/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The cube becomes a flower.
- Beginning: An intact cube, its corners standing, its faces still granular.
- Turn: The corners go — **the outline begins to give, and this is the passage, not a stage.**
- Peak: The mass resolves, once, into the form of a flower. **It is not tied twice.**
- Pull: The flower is still white and still sugar, and **the clip ends on it — unfinished, and not undone.**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — The cube is whole. Six faces, eight corners, the grain of them unbroken.
  - BEAT 2 `2-5s` — density: `held` — **The passage.** The corners round and the mass loosens outward. **This is the change being spent, not an intermediate stage being shown.**
  - BEAT 3 `5-7s` — density: `dense` — The form resolves into a flower, once.
  - BEAT 4 `7-8s` — density: `held` — The flower holds. It is not undone.
- Temporal Density: The passage takes the largest share — **the grammar spends its seconds on the change, not on the two states at either end.**

# 9. ACTION

- `ACT_GIVE` — Before: the corners hold their edges. After: the edges have begun to round.
- `ACT_RESOLVE` — Before: the mass is a cube with softened corners. After: the mass holds the form of a flower.
- `ACT_HOLD` — Before: the form is arriving. After: the form has arrived and stays.
- Causes: **heat.** ⚠️ **The cause is not new in the frame** — the tea is already hot when the shot opens, nothing enters, and nothing is added. **There is no process beat.**

# 10. CAMERA

- Camera Language: **A macro frame placed at the cube's own scale, its plane of focus razor-thin and set across the cube's middle.** ⚠️ **This is a placement and not a viewpoint that watches**: the frame is the place the change happens, and it is composed once at `0s` and left there. ⚠️ **The style's physical law, in the card's own words** (`macro-photo`) — **The camera is the mover, and it moves less than in any other style.** A focus rack, or a few millimetres of drift, is a full gesture.
- Camera Events: `0-8s` none — **the frame is placed once and holds for the whole take.** ⚠️ **A hold is an event, written with its range like any other**: timing `0-8s`; movement none; target the cube's near face, inside the thin plane; speed none. **What the hold is spent on is the passage** — the outline travels, the frame does not.
- Camera Behavior: **Still, and the stillness is the decision.** ⚠️ **The reason, which travels on into §18: the change is the event** — a camera move would be a second event at the same moment, **and it would also throw the subject out of the razor-thin plane** (a millimetre of travel is enough). One continuous take; no cut.

# 11. MOTION

## Subject Motion

The cube's corners round, and the mass resolves into a flower. **The motion is one-way and it happens once.** The cube keeps its place in the frame — **what travels is the outline, not the position.** Nothing is tied twice, and the form does not come undone.

## Object Motion

None. The cube is the only object and it is the subject.

## Environmental Motion

The tea immediately around the cube moves — **a slow, warm local current, made by the cube and not by anything else.** It is the only other thing in the frame that moves, and it never crosses the frame.

## Physical Characteristics

- Weight: Sugar has almost none, and water gives it just enough. **It settles; it does not fall.**
- Inertia: Once the outline has begun to give, it keeps giving — **the change does not stop halfway and wait.**
- Acceleration: Slow, then suddenly fast at the resolve. **The passage is not even.**
- Fluidity: Dissolution, not melting — **a solid losing its edges into a liquid that is already touching it.**
- Impact: None.

# 12. EMOTION

- Emotional Arc: The patience of a small thing that is being taken apart and is arranging itself at the same time.
- Emotional Events: The moment the outline stops being a cube and is not yet a flower.

# 13. LIGHTING

- Base Lighting: Soft daylight through the tea. **One small specular highlight on the cube's wet face**, and the rest falling away.
- Lighting Events: None. The light does not change, does not travel, and does not cross the frame.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: Almost none — **the single small tick of a sugar cube meeting liquid**, in the first second.
- Music: None.
- Environment: The low, close room tone of a kitchen, unbroken.

# 15. CONTINUITY

- Identity: The same cube for the whole shot — **same material, same white, same place in the frame.**
- Spatial: The cube does not move within the frame; the composition is fixed from the first frame to the last.
- Temporal: One continuous passage. **Nothing is skipped between beats.**
- Visual: The plane of focus stays razor-thin, the bokeh stays smooth, and the palette stays white-on-amber for the whole shot.
- Motion: The outline moves for the whole shot. **There is no held frame anywhere in it.**
- Sound: The room tone is unbroken.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止）

- No cut, no dissolve, no wipe. **The change is never interrupted.**
- No intermediate stage held for the viewer. **No stage of the change is stopped and shown.**
- No second subject changing. **Nothing else in the frame transforms.**
- No caption naming the change, and no voice-over naming it.
- No colour beyond the white of the sugar and the amber of the tea.
- No spoon, no hand, no cup rim, no person, no figure.
- No steam, no bubble, no foam.
- No readable text of any kind.
- No camera move for its own sake.

## MUST

- The change happens exactly once and **finishes as a flower inside the clip.**
- **Whiteness is kept across the whole change.**
- The cube stays in the same place in the frame throughout.
- The camera does not move.
- No stated process — the shot explains nothing.

## PREFER

- The cube placed off-centre, with the larger part of the frame given to defocused tea.

## ALLOW

- One small specular highlight travelling across the wet face as the outline gives.

# 17. GENERATION PRIORITIES

1. **The change is not compressed** — the shot spends its seconds on the passage, not on the cube and not on the flower. ⚠️ **This is the failure the grammar exists to prevent: a shot that lingers on the two states and skips the middle is not this card.** It outranks beauty.
2. **No process beat** — the change needs no explanation, and the frame gives none.
3. **One subject** — the cube stays the subject all the way through, and nothing else transforms with it.
4. **Whiteness is kept** — the flower is sugar, and sugar is white.
5. **The change is not cut** — no dissolve, no wipe, no camera event standing in for it.
6. **The plane of focus stays thin** — a frame that resolves front to back is a different style.
7. **Stillness of the camera** — the frame is composed once and left alone.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

An 8-second continuous macro take (16:9) of a single white sugar cube in hot tea, one clip. Beats, deliberately uneven: [0-2s] the cube is whole — six faces, eight corners, unbroken; [2-5s] the passage — the corners round and the mass loosens outward, and the shot spends itself here; [5-7s] the form resolves, once, into a flower; [7-8s] the flower holds and is not undone. **The change is not compressed and it is never cut — there is no intermediate stage held for the viewer, and no caption names what is happening.** Whiteness is kept across the whole change: the flower is sugar, and sugar is white. **The camera is a macro frame placed at the cube's own scale and held there — the change is the event, and the frame does not travel away from it.** (No second subject changing, no spoon, no hand, no cup rim, no readable text.)

## Visual Prompt

Extreme macro photography of a single white sugar cube in hot tea. Granular faces with tiny facets catching light, the wet sheen where the tea has reached it, the tea's amber behind it dissolving into smooth rounded defocus. Near-monochrome: white against a single amber, no third hue anywhere in the frame. **A razor-thin plane of focus — whatever leaves it goes to smooth rounded bokeh.** Very low visual density: the cube, the tea immediately around it, and defocus; nothing else. Soft daylight through the tea with one small specular highlight on the wet face. No wide shot, no flat even lighting, no hard outline, no illustration, no painted texture, no CGI, not a render, no 3D gloss.

## Motion Prompt

Macro. **The change is the time, and it is spent on the passage — not on the two states at either end.** The corners go first, then the mass loosens outward and resolves, once, into a flower. **The motion is one-way and it happens once**: the outline is never tied twice, never corrected, and the form is never undone inside the clip. **The cube keeps its place in the frame throughout — what travels is the outline, not the position.** Whiteness is carried across the whole change; only the silhouette moves. The tea immediately around the cube makes a slow, warm local current and nothing else in the frame moves. **The camera is placed once at the cube's own scale and holds** — the outline travels, and the frame does not. No second simultaneous transformation, no stated process, no intermediate stage held, no morphing contours, no motion blur, no full animation.

## Camera Prompt

**A macro frame placed at the cube's own scale, composed once at the start and held there for the whole take.** The cube sits inside a razor-thin plane of focus and stays inside it while its outline loosens — **the frame is the place the change happens, and it does not travel away from it.** **The style permits a focus rack, or a few millimetres of drift; this shot spends neither** — **the change is already the largest event in the frame, and a millimetre of travel would throw the subject out of the plane that holds it.** Nothing pushes in and nothing pulls back: **the passage is the event, and the camera is not a second one.** Focus stays razor-thin from the first frame to the last. One continuous take; no cut, no dissolve, no wipe.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of this work and of every word it holds; **if any speech is placed in it, that speech is Japanese.** **No speech is placed in this shot.** No dialogue, no voice-over, no narration, no caption naming the change. Sound effects: almost none — only the single small tick of a sugar cube meeting liquid, in the first second. Ambient: the low, close room tone of a kitchen, unbroken. **Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell.**

## Negative Prompt

no wide shot, no flat even lighting, no CGI, no illustration, no painted texture, no cut, no dissolve, no wipe, no stated process, no intermediate stage held, no caption naming the change, no voice-over naming the change, no second simultaneous transformation, no second subject changing, no spoon, no hand, no cup rim, no readable text, no steam, no bubble, no foam, no camera move for its own sake, no morphing contours, no motion blur, no colour beyond white and amber, no watermark, no on-screen subtitles, no background music

## Style Motion

**The plane of focus is razor-thin, so motion is measured by what stays inside it.** A millimetre of travel throws the subject out of the plane entirely, and **this shot spends none of that travel** — the cube does not go anywhere, and its outline is what moves. **Everything is magnified, including time** — a surface giving way, a wet edge advancing; at this scale the smallest movement is the largest event, **and this shot's whole change is of that size.** **The camera is the mover, and it moves less than in any other style** — a focus rack or a few millimetres of drift is a full gesture here, so a shot that holds completely is the native case, not an absence. **Stillness is the ground** — the subject is held in focus and the shot is about what is visible while nothing travels. **What this style does not do**: wide movement, travelling shots, articulated full-body motion, deep-focus staging, cuts, or a camera that covers distance. **Focus stays thin for the whole shot** — a frame that resolves front to back is a different style, not a beat of this one. (Source: the `Motion character` of the style card `macro-photo`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `grammar-transformation-s01-8s-01`
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
- Generation Date: `2026-09-22`（⚠️ **根拠は戻ってきたファイルの時刻**——`media/4466d551-1479-49c0-936a-d543d85785d5.mp4` の `02:53`。
  **著者が名乗った日付ではない。** ⚠️ **そのファイルは `0.2.0` の投入に対するものである**——
  **この版の投入は、まだ無い。**）
- Adopted Take: `—`（**まだ採用されていない。**⚠️ **テイクは1本、`media/` に在る**——
  **テイクの記録はまだ無い。** 記録を書くのは著者である（`projects/hitosara/media/README.md`）。
  ⚠️ **ファイル名は `NN__` の接頭辞を持たない**——**名前から記録を引けない。**
  ⚠️ **採用は選別であり、著者が編集である**（`CLAUDE.md`）。）

## Resolved Values

- Duration: `8s`
- References: `REF_LOCATION (紅茶.base, 未作成) ／ REF_STYLE (macro-photo, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
  ⚠️ **この行は「仕様が名指した参照」であって、「実際に渡した参照」ではない。**
  **この1本は、いま何も渡していない**（`attached: []`）。
- Temporal Structure: `4 beats, NON_UNIFORM — 2s / 3s / 2s / 1s. The passage = BEAT 2 at 3s (38%)`
- Camera Events: `none — the frame is placed once at 0s and holds for the whole shot`
- Action Events: `ACT_GIVE → ACT_RESOLVE → ACT_HOLD`
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

⚠️ **この作品は、形式カード `transformation` が初めて使われた記録である。**

## Observed Problems

（**機械の測定は、まだ無い。** 戻ってきたファイルの測定は**テイクの記録**
（`verdict.machine.measured`）に書く——`L25` がそれを §1 と突き合わせる。
⚠️ **この行は「問題が無い」ことを言っていない。** **測っていないのである。**）

## Anticipated risks (to check in the first generation)

1. **The passage may be compressed.** A generator that reads `[0-2s] cube / [5-7s] flower` may skip the middle and cut between them. **The grammar's whole claim is that the middle is the shot.**
2. **An intermediate stage may be held.** The passage may arrive as a stopped, legible "half-cube" — which is exactly the process beat the card forbids.
3. **The change may not finish.** The shot may end before the flower is there, which reads as an interrupted dissolve rather than as an unfinished change. ⚠️ **§8 says the change finishes inside the clip; the clip ends after it.**
4. **The white may drift.** A tear, a seam, or a tone shift between the cube and the flower would make this a substitution rather than a continuity.
5. **The second subject.** Steam or a bubble entering to fill the frame would be a second thing changing at the same time. **Check for it.**
