# Wan 3.0 Full Specification — 実家 Clip 1/1 / 9s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**

⚠️ **この仕様は形式カード `remembered-world` を1度だけ使う。**
カードの4つの欄が、この仕様の背骨である。

| カードの欄 | この1本の値 |
|---|---|
| `WITNESS` | この家で育った者の記憶である。**見ている者は枠の外に居る** |
| `DRIFT` | **窓の外の庭の形。** 滑り、そして戻る |
| `CONSTANT` | **部屋そのもの。** 壁も、畳も、窓枠の位置も動かない |
| `EXACT` | **冷蔵庫に貼った子供の絵。** 一寸も動かない |

⚠️ **このカードは `video-spec` に文法を1つ足したものである。**
この仕様が足したのは **「時は過ぎず、世界のほうが滑る」という1点**だけである——
**ゆえに `time-fold` ではない。** あちらでは時が過ぎ、こちらでは**時が立ち、世界が動く。**
⚠️ **滑りは作為的であり、乱数ではない。** 滑るものは1つ、名指され、
**滑りながら意味を保つ**——庭は庭のままであり、部屋は部屋のままである。

⚠️ **この文法は §15 CONTINUITY と衝突する。**
継続の床は隣り合う世界を要求し、この文法は**記憶の仕方で**隣り合う世界を要求する。
**ゆえに §15 は、どの要素が免除されるかを明記する**——⚠️ **免除されるのは庭の形だけである。**
**すべてを免除すれば、この枠は記憶ではなく雑音になる。**

⚠️ **この作品は物語ではない。** 1ショットだけの最小の作品であり、
**7枚の文法カードの1枚が、仕様として立つかを試すために在る。**

---

# 1. VIDEO

- Duration: `9s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. **Time does not pass — the world slips, and one thing in the frame never does.**

# 2. WORLD

## World Concept

A tatami room seen in a dream: everything in it is slightly wrong, and one thing in it is exactly right. **This is not a record of the room. It is someone's memory of it** — which is why the slipping is the grammar and not a defect.

## World Rules

- **This is a memory, not a record.** The frame is the witness's memory; it is not the world.
- **Time does not pass.** The moment is held, and the world is what moves — **which is why this is not `time-fold`.**
- **One thing slips, and it is named: the shape of the garden outside the window.** Its trees, its wall, and the tilt of its ground change and change back.
- **One thing is kept exact: the child's drawing taped to the refrigerator.** It does not move by a hair, and **it is the ruler the drift is measured against.**
- **The drift keeps its meaning.** The garden stays a garden and the room stays the room — **drift that destroys meaning is a defect, not this grammar.**
- **The drift returns.** A thing that slips and stays slipped is a different grammar.
- **The room is not exempt from §15.** Only the garden's shape is.
- **No person and no figure** is in the frame at any point — the witness's eye is outside it.
- **No legible text** appears anywhere.

## Visual Language

- Art Direction: An instant photograph. White instant-film border framing the image, on-camera flash direct and slightly hard, faded vintage colour, slight softness and mild blur, subtle chemical mottling in the emulsion. **A casual snapshot of a private moment, the subject centred under the flash.**
- Color Language: Faded warmth, flash-cooled skin tones. ⚠️ **The colours keep ageing for the whole shot** — a colour that stabilises and turns accurate is a different style.
- Texture: Soft grain, the white border, instant film texture and its subtle mottling.
- Rendering: True instant film. Not studio lighting, not professionally graded, not crisp digital sharpness, not an illustration, not a render.
- Visual Density: Low and domestic. **Tatami, a window, a refrigerator with one drawing on it.**
- Time: 夢の中
- Atmosphere: Held and slightly wrong. **The room is not frightening; it is simply not quite remembered correctly.**

# 3. SUBJECTS

## The Room

- Reference: (none — the room is not a registered entity; it is the subject of the shot)
- Appearance: A tatami room, lived in. A window on the left, a refrigerator on the right, the floor below. **Its contents — a wall's scuff marks, the grain of the tatami — are as the witness half-remembers them.**
- Behavior: **The room does not move.** Its walls, its tatami, and the positions of the window and the refrigerator hold for the whole shot. ⚠️ **It is the constant, and it is not exempt from §15.**
- Continuity Requirements: Must Preserve: **everything** — the room is the frame's ground. May Change: nothing.

## The Drawing

- Reference: (none — the drawing is not a registered entity)
- Appearance: A child's drawing on a sheet of paper, taped to the refrigerator door. **Its shape, its place, and its edges are exact.**
- Behavior: **It does not move, at all, for the whole shot.** ⚠️ **It is not the shot's actor and it is not its reveal — it is the ruler.** The audience sees it from the first frame and uses it without being told.
- Continuity Requirements: Must Preserve: **its exact shape, its exact place, and its legibility as a drawing.** May Change: nothing.

# 4. ENVIRONMENT

- Location: `実家`
- Environment Elements: The room's interior, and the garden seen through the window on the left.
- Environmental Behavior: **The garden is the only thing that slips.** Its trees change in number and shape, the wall changes height, and the ground changes its tilt — **and then all of it returns to the shape it had at the start.** ⚠️ **Nothing else in the environment changes, and nothing enters the frame.**

# 5. OBJECTS

- The refrigerator, the window, the tatami, and the drawing taped to the door. **Nothing else is named in the frame.**
- ⚠️ **No second room, no opening door, and no object entering.** Nothing crosses the frame at any point.

# 6. REFERENCES

- REF_LOCATION: `実家.base` — **未作成。** この作品の画像の経路はまだ1度も走っていない
  （`ledger.yaml` を見よ）(MEDIUM)
  ⚠️ **在ることと、渡したことは違う。** **この1本は、いま何も添付していない**
  （ショット記録の `attached: []` を見よ）。
- REF_STYLE: `instant-photo` (HIGH)
- REF_FORMAT: `remembered-world` — this defines the one grammar this shot is
- REF_SOURCE: `projects/grammar-remembered-world/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The garden slips, and the frame turns out to be a memory.
- Beginning: The room as remembered. **Nothing has slipped yet.**
- Turn: **The garden begins to change** — trees, wall, ground — and the room does not.
- Peak: The room holds and the drawing holds, **while the garden is wrong.**
- Pull: The garden returns to its shape, and **nothing is left of the slipping** — the room and the drawing are exactly as they were, and the audience now knows what the frame is.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-3s` — density: `sparse` — The room as remembered. The garden through the window, the refrigerator, and the drawing taped to its door.
  - BEAT 2 `3-6s` — density: `dense` — **The slipping.** Outside, the trees change in number, the wall changes height, the ground tilts. **The garden stays a garden. The room does not move and the drawing does not move by a hair.**
  - BEAT 3 `6-9s` — density: `held` — **The return.** The garden comes back to its shape and the slipping leaves nothing behind. **The room and the drawing are exactly as they were — and the audience now knows this frame is a memory.**
- Temporal Density: ⚠️ **The seconds are not spread evenly** — the slipping takes the middle and the return is given room to be quiet.

# 9. ACTION

- `ACT_SHOW` — Before: the room is whole and unremarkable. After: **the room and the drawing have both been established as what does not move.**
- `ACT_SLIP` — Before: the garden is as it was. After: **its trees, wall and ground are wrong, and it is still a garden.**
- `ACT_RETURN` — Before: the garden is wrong. After: **it is as it was, and nothing marks that it left.**
- Causes: **memory.** ⚠️ **Nothing in the frame causes the slipping** — no agent acts, nothing enters, and **there is no process beat.** The witness is not in the frame, and the drift is not caused by anything the audience can see.

# 10. CAMERA

- Camera Language: **A print held in a hand and looked at** — the frame is an instant photograph, composed once (window on the left, refrigerator on the right) and then kept, **and the hand is the placement: the picture is looked at from where it is held.** ⚠️ **The style's physical law, in the card's own words** (`instant-photo`) — **The camera does not travel.** An instant photograph is a thing held in a hand — the only drift available is the small unsteadiness of holding it.
- Camera Events: `0-9s` none — **the print goes nowhere for the whole take.** ⚠️ **A hold is an event, written with its range like any other**: timing `0-9s`; movement the small unsteadiness of a held print, and nothing beyond it; target the room, window left and refrigerator right; speed none. **What the hold is spent on is the room's one exact thing** — the drawing on the refrigerator never moves, **and it is what the garden's slipping is measured against.**
- Camera Behavior: **Held, and the holding is this style's own state rather than a restraint.** ⚠️ **The reason, which travels on into §18: time does not pass in this shot; the world slips** — the movement belongs to the garden and to the emulsion, **and a travelling frame would put a third motion into a room whose whole point is that it holds.** One continuous take; no cut.

# 11. MOTION

## Subject Motion

**The room does not move, and the drawing does not move.** The subject that moves is the garden outside the window: its trees, its wall, and the tilt of its ground shift, hold their wrongness for a moment, and shift back. **The slipping is one-way at no point** — it is a departure and a return, not a substitution.

## Object Motion

None. The refrigerator, the window, the tatami, and the drawing are all still for the whole shot.

## Environmental Motion

**The garden, and nothing else.** ⚠️ **The garden's slipping is meaning-preserving**: the trees are still trees, the wall is still a wall, and the garden is recognisably the same garden before, during, and after. **The return is complete** — nothing of the slipping is left at the end.

## Physical Characteristics

- Weight: Domestic and unremarkable. **The room has the weight of a room; the garden has the weight of a view.**
- Inertia: **The room has it completely.** The garden has none — it slips without resistance and returns without resistance.
- Acceleration: None. **The slipping is not fast and is not gradual; it is simply so.**
- Fluidity: The slipping is like a surface under water — **the shape moves while the thing stays the same thing.**
- Impact: None.

# 12. EMOTION

- Emotional Arc: The unease of a room that is almost right, and the small steadiness of one thing in it that is exactly right.
- Emotional Events: The moment the garden is wrong and the drawing is not — **the audience is not told which one to trust, and trusts the drawing anyway.**

# 13. LIGHTING

- Base Lighting: On-camera flash, direct and slightly hard, subject centred under it. **The light of the whole shot is the flash.**
- Lighting Events: None. ⚠️ **The flash never relights** — the light does not change, does not travel, and does not answer the slipping. **The garden slips under a light that does not move.**

# 14. AUDIO

- Dialogue: None.
- Sound Effects: Almost none — **the room's own small quiet**, unbroken.
- Music: None.
- Environment: A lived-in interior, close and low, with nothing outside it audible.

# 15. CONTINUITY

⚠️ **このショットは、この節と衝突する。** ゆえに**免除をここに明記する。**

- Identity: The room keeps its identity for the whole shot, and the drawing keeps its identity exactly. **The garden keeps its identity as a garden across the slipping** — it is the same garden before, during, and after.
- Spatial: **The positions of the window, the refrigerator, and the drawing do not change at all.** ⚠️ **What the garden's contents do is exempt from this clause, and nothing else is.**
- Temporal: One held moment. **Time does not pass** — nothing in the frame travels through time, and the world is what moves.
- Visual: The flash does not change, the colours keep ageing, and the white border holds for the whole shot.
- Motion: **The garden slips and returns; everything else holds.** ⚠️ **The slipping is a departure, not a substitution, and it is complete by the last frame.**
- Sound: The room's quiet is unbroken.
- ⚠️ **免除の範囲**: **窓の外の庭の形だけである。** 部屋の位置関係、冷蔵庫の位置、絵の形は**免除されない**——**それらが正確であることによって、滑りが滑りとして読める。**

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止）

- No drift that destroys identity — **the garden stays a garden and the room stays the room.**
- No slipped element that never returns.
- No melting or warping faces, no garbled characters, no mojibake, and no illegible text.
- No caption and no voice-over explaining that this is a memory. **The frame must not announce its own grammar.**
- No people, no figure, no second room, no opening door.
- No camera travel.
- No studio lighting, no professional color grading, no crisp digital sharpness.
- No colour that stabilises — **the colours keep ageing for the whole shot.**
- No readable text of any kind.
- No CGI, no illustration.

## MUST

- **The drawing on the refrigerator stays exact** — shape, place, and edges, for the whole shot.
- **The room does not move** — walls, tatami, window, and refrigerator hold.
- **Only the garden's shape slips**, and it returns completely by the last frame.
- The drift keeps its meaning: **it reads as memory, not as damage.**
- The camera does not travel and the frame does not cut.
- The flash does not relight.

## PREFER

- The window on the left and the refrigerator on the right, with the drawing small in the frame but fully legible.

## ALLOW

- The emulsion's own slight mottling and settle as the picture surfaces — **the style's motion, under the shot's motion.**

# 17. GENERATION PRIORITIES

1. **The drawing stays exact.** ⚠️ **It is the ruler; without it the slipping reads as a failed generation.** It outranks beauty.
2. **The drift is meaning-preserving** — the garden stays a garden.
3. **The drift returns.** A slipped thing that stays slipped is a different grammar.
4. **The room does not move.** Only the garden's shape is exempt from §15.
5. **Time does not pass** — the moment is held and the world is what moves.
6. **No caption and no voice-over announcing the memory.**
7. **The flash never relights, and the colours keep ageing.**
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 9-second continuous take (16:9) of a tatami room seen in a dream, one clip, seen in an instant photograph held in a hand and looked at. Beats: [0-3s] the room as remembered — a window on the left, a refrigerator on the right, a child's drawing taped to its door; [3-6s] the slipping — outside, the trees change in number, the wall changes height, and the ground tilts, while the garden stays a garden, and the room and the drawing do not move by a hair; [6-9s] the return — the garden comes back to its shape and leaves nothing behind. This is a memory, not a record: time does not pass, and the world is what moves. One thing in the frame is exact — the drawing on the refrigerator — and it never moves; it is what the slipping is measured against. (No people, no figure, no second room, no camera travel, no caption or voice-over explaining that this is a memory.)

## Visual Prompt

An instant photograph of a tatami room, taken with on-camera flash. White instant-film border framing the image, direct and slightly hard flash, faded vintage colours, slight softness and mild blur, instant film texture with subtle chemical mottling. A casual snapshot of a private moment, subject centred under the flash. A window on the left with a garden beyond it, a refrigerator on the right with a child's drawing taped to its door, tatami below. The room is lived in and slightly wrong in the way a remembered room is — scuff marks on the wall, the grain of the mats — and every part of it is legible, never garbled. No studio lighting, no professional color grading, no crisp digital sharpness, no CGI, no illustration, no readable text.

## Motion Prompt

Time does not pass; the world slips. The room does not move at all — its walls, its tatami, and the positions of the window and the refrigerator hold for the whole shot. The shape of the garden outside the window is what changes: its trees shift in number and shape, its wall changes height, its ground tilts — and it returns, completely, by the last frame, so that the slipping leaves nothing behind. The slipping keeps its meaning: the garden stays a garden and the room stays the room. The child's drawing taped to the refrigerator never moves by a hair — it is exact for the whole shot, and it is what the drift is measured against. The flash does not relight, and the colours keep ageing. The frame is a print held in a hand — the small unsteadiness of holding it is the only movement the frame has, and the world is what slips. No drift that destroys identity, no slipping that never returns, no melting or warping faces, no garbled characters, no camera travel.

## Camera Prompt

A single instant-photograph frame, held in a hand and looked at, composed once — window on the left, refrigerator on the right — and then kept. The camera goes nowhere — no pan, no zoom, no rack, no travel, no handheld walk. The only drift this style has is the small unsteadiness of holding a print; this shot spends exactly that much and not a hair more — the world is what slips here, and the frame is the still thing that the slipping is measured against. The white border holds the picture for the whole shot and is never crossed. One continuous take; no cut.

## Audio Prompt

The language of this work is Japanese — Japanese is the language of this work and of every word it holds; if any speech is placed in it, that speech is Japanese. No speech is placed in this shot. No dialogue, no voice-over, no narration, and no caption or voice-over explaining that this is a memory. Sound effects: almost none — only the room's own small quiet. Ambient: a lived-in interior, close and low, with nothing outside it audible. Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell.

## Negative Prompt

no studio lighting, no professional color grading, no crisp digital sharpness, no CGI, no illustration, no drift that destroys identity, no illegible text, no garbled characters, no mojibake, no melting or warping faces, no slipped element that never returns, no caption explaining that this is a memory, no people, no figure, no second room, no door opening, no camera travel, no colour that stabilises, no readable text, no watermark, no on-screen subtitles, no background music

## Style Motion

The print is a surface, and its chemistry is what moves — the image surfaces, mottles and settles slightly, and that change belongs to the emulsion, not to the subject. This is why the style and this grammar do not argue: the style's own motion sits under the subject, and the subject's slipping is a separate layer above it. The flash does not change — it is the light of the whole shot, and this shot's garden slips under a light that never relights. The frame is a kept object — the white border holds and the picture never leaves it, and the room's one exact thing is kept inside that border. The camera does not travel — an instant photograph is a thing held in a hand, and the only drift available is the small unsteadiness of holding it. What this style does not do: studio relighting, crisp continuous action, sharp articulated movement, colour grading, cuts, or a camera that goes anywhere. The colours keep ageing for the whole shot — a colour that stabilises and turns accurate is a different style.

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `grammar-remembered-world-s01-9s-01`
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
- Generation Date: `2026-09-22`（⚠️ **根拠は戻ってきたファイルの時刻**——`media/affada3c-82c7-4482-8a7b-08357ef00dd1.mp4` の `03:05`。
  **著者が名乗った日付ではない。** ⚠️ **そのファイルは `0.2.0` の投入に対するものである**——
  **この版の投入は、まだ無い。**）
- Adopted Take: `—`（**まだ採用されていない。**⚠️ **テイクは1本、`media/` に在る**——
  **テイクの記録はまだ無い。** 記録を書くのは著者である（`projects/hitosara/media/README.md`）。
  ⚠️ **ファイル名は `NN__` の接頭辞を持たない**——**名前から記録を引けない。**
  ⚠️ **採用は選別であり、著者が編集である**（`CLAUDE.md`）。）

## Resolved Values

- Duration: `9s`
- References: `REF_LOCATION (実家.base, 未作成) ／ REF_STYLE (instant-photo, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
  ⚠️ **この行は「仕様が名指した参照」であって、「実際に渡した参照」ではない。**
  **この1本は、いま何も渡していない**（`attached: []`）。
- Temporal Structure: `3 beats, NON_UNIFORM — 3s / 3s / 3s. The slipping = BEAT 2; the return = BEAT 3`
- Camera Events: `none — the print is held once at 0s, and it goes nowhere`
- Action Events: `ACT_SHOW → ACT_SLIP → ACT_RETURN`
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

⚠️ **この作品は、形式カード `remembered-world` が初めて使われた記録である。**

## Observed Problems

（**機械の測定は、まだ無い。** 戻ってきたファイルの測定は**テイクの記録**
（`verdict.machine.measured`）に書く——`L25` がそれを §1 と突き合わせる。
⚠️ **この行は「問題が無い」ことを言っていない。** **測っていないのである。**）

## Anticipated risks (to check in the first generation)

1. **The slipping may destroy meaning.** A generator told to change the garden's shape may return an entirely different garden — **and then the drift has destroyed identity, which the card calls a defect.**
2. **The drawing may move.** The ruler is the smallest thing in the frame and the easiest to lose. ⚠️ **Check the refrigerator door explicitly, frame by frame.**
3. **The room may move with the garden.** If the walls shift too, there is no constant, and the frame is noise rather than memory.
4. **The slipping may not return.** The garden must be as it was in the last frame — **a slipped thing that stays slipped is a different grammar.**
5. **Text may appear.** A handwritten date in the border, a caption, a chyron. ⚠️ **The style's own breakdown allows a handwritten date in the border; §16 forbids readable text here.** Check which one arrived.
6. **The frame may announce itself.** A caption or a voice-over saying this is a memory defeats the whole shot — **the audience must work it out from the drawing.**
