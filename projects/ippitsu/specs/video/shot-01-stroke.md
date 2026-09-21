# Wan 3.0 Full Specification — 一筆 Clip 1/1 / 6s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。** 投入の仕方は同じディレクトリの `README.md` を見よ。

⚠️ **この作品は物語ではない。** 1ショットだけの最小の作品であり、
**Style 4.3「動く絵画」が成立するかを試すために在る**（決定 2026-09-21、著者。D-14）。

⚠️ **この1本の変化は1つだけである。**「白い紙が、墨を持つ。」
**それ以外のことは何も起こらない**——人物も、物語も、開示も無い。

⚠️ **この仕様は、このリポジトリで最初に「生成の前に書かれた」仕様である。**
参照画像は1枚もまだ無い（`ledger.yaml` の `紙.base`）。**四つの手の①（生成する）は著者のものである。**

⚠️ **この作品の様式カードは、このリポジトリの中に在る**（`references/styles/sumi-e.md`）。
**走らせるときは `SVL_STYLES_DIR=references/styles` を張ること**——張らなければ `L20` が違反として鳴る。
⚠️ **これは作品の欠陥ではなく、置き場の性質である。**

⚠️ **§18 `Audio Prompt` は作品の言語（`Japanese`）を名乗る**（`L27`）。
発話は1つも置かないが、**空欄は中立ではない**——生成器は、指定されなければ自分の既定で喋る。

---

# 1. VIDEO

- Duration: `6s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the white paper comes to hold ink
  — **and the ink only ever spreads.**

# 2. WORLD

## World Concept

Paper and ink. Nothing else is in the frame. There is no clock — **not because time is withheld,
but because there is nothing for time to pass through.** Before the stroke and after it: that is all of it.

## World Rules

- The stroke happens once. It is not corrected, not retraced, not repeated.
- The ink moves in one direction only: outward. **It never narrows, never retreats, never dries back to white.**
- The brush leaves. **What moves after it is the paper's, not the hand's.**
- The void stays empty. No dust, no haze, no light shaft drifts in to fill it.
- The ink stays monochrome. No colour and no colour-temperature shift.
- No legible text, no seal, no signature appears anywhere.
- No person, no figure, no hand is in the frame at any point.

## Visual Language

- Art Direction: Graded black ink on washi — the five inks, dry-brush strokes, bleeding, boldly reserved negative space, single-stroke economy.
- Color Language: Monochrome. Gradations of black ink on warm off-white paper. **No second hue in the frame at any time.**
- Texture: Washi grain, bleeding edges, dry-brush breaks, dark ink dots.
- Rendering: Hand-drawn ink wash. **Not a photographic surface, and not a render.**
- Visual Density: Very low. Paper, one stroke, and the void. Nothing else.
- Time: 時刻を持たない
- Atmosphere: Still and dry. **The only thing alive in the frame is the ink.**

# 3. SUBJECTS

## The Ink

- Reference: (none — the ink is not a registered entity; it is the subject of the shot)
- Appearance: A single dark stroke laid on washi, its edge wet where it travelled, the wet edge **only ever moving outward from the line.**
- Behavior: It spreads into the fibre. **It does not narrow, does not retreat, and does not dry back to white.** It does not pulse, breathe, or bloom-and-shrink.
- Continuity Requirements: One mark, one pressure, no seam. The stroke is continuous with itself.

# 4. ENVIRONMENT

- Location: `紙`
- Environment Elements: One sheet of washi filling the frame, its fibre visible. Nothing else is in the frame but the paper, the ink, and — for one beat — the brush.
- Environmental Behavior: The paper does not move, does not flutter, does not breathe. **Only the ink moves within it. The void stays empty for the whole shot.**

# 5. OBJECTS

- The brush. It enters from the frame's edge before the stroke, lays the mark once, **and leaves before the shot ends. It is never seen again.**
- No ink stone, no water dish, no seal, no weight, no table edge. **Nothing else is in the frame.**

# 6. REFERENCES

- REF_LOCATION: `紙.base` — **作成済み、しかしこの動画へは渡さない。**（**著者の裁定、2026-09-22**）
  （`media/01_ChatGPT Image 2026年9月22日 00_10_37.png`。
  `ledger.yaml` と `takes/ippitsu-s01-image-1.yaml` を見よ）(MEDIUM)
  ⚠️ **在ることは、渡したことではない。** そして**この作品では、渡さないことが決まった。**
  **著者の言葉**: 「**参照イメージがない方が自然だったよ。参照があると、筆跡が画面上に、
  すでに乗ってしまう**」——
  ⚠️ **この1枚は `after` の側である**（墨は既に紙の上にあり、広がっている）。
  **このショットの主題は「墨が紙へ移る」という出来事そのもの**である——
  **ゆえに出来事の後の姿を参照として渡すことは、§7 の `before` と食い違う。**
  ⚠️ **渡したかどうかは、テイクが持つ**——**1本目は渡し（`params.references` に1件）、
  2本目は渡していない（`references: []`）。** **著者が採ったのは2本目である。**
  ⚠️ **ゆえに §6 の `REF_LOCATION` は、この動画にとって「画像の経路」ではなくなった。**
  **紙の見た目は、§4 と §5 の文が固定する。** ⚠️ **`紙.base` は台帳から消えない**——
  **画像の側の基準であり続ける**（`ledger.yaml` を見よ）。
  ⚠️ **これは一筆だけの裁定である。**（**著者、2026-09-22**）
  **基盤の規則は変わらない**——`schemas/shot-record.schema.json` と
  `engine/ledger/specmap.py` は、**いまも「キー画像は動画へ添付して渡る」と言っており、
  それは他の作品では正しい。**
  ⚠️ **ゆえに基盤は動かしていない。****この例外は、この作品の記録の中にだけ在る。**
  ⚠️ **スキーマを読むだけの人には、この例外は見えない。****穴として記録する**（`HISTORY.md` の `0.33.8`）。
- REF_STYLE: `sumi-e` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/ippitsu/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: The white paper comes to hold ink.
- Beginning: The paper is blank and the brush has not touched it.
- Turn: The stroke is laid — **once, and it is not revised.**
- Peak: The ink enters the fibre and does not stop.
- Pull: The brush is gone and the ink is still spreading.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — Blank paper. The brush enters the frame and has not touched it yet. **The void is already the composition.**
  - BEAT 2 `2-3s` — density: `dense` — One stroke is laid. **Once. Not corrected, not retraced, not repeated.** The brush leaves the paper.
  - BEAT 3 `3-6s` — density: `held` — The brush is gone. The ink enters the fibre and keeps spreading. **It never narrows and never returns.**
- Temporal Density: Half the shot is the third beat — **the part with no hand in it.**

# 9. ACTION

- `ACT_ENTER` — Before: the brush is outside the frame. After: the brush is over the paper.
- `ACT_LAY` — Before: the paper is blank. After: one stroke is on it.
- `ACT_WICK` — Before: the mark sits on the surface. After: the ink is in the fibre and travelling.

# 10. CAMERA

- Camera Language: The frame is a scroll, not a window. One flat frontal view of the sheet, held at the paper's own scale, the void given as much of the frame as the subject.
- Camera Events: `0-2s` the whole sheet. `2-3s` hold, unmoved, while the stroke lands. `3-6s` hold — **the camera does not move at all while the ink spreads.**
- Camera Behavior: **Still.** No push, no drift, no pan, no handheld, no whip. One continuous take; no cut. **Any camera movement spends the negative space, which is what the shot is about.**

# 11. MOTION

## Subject Motion

The ink spreads outward from the stroke into the paper. **One way only: the ink is at its largest at the end. It never narrows, never retreats, and never dries back to white.** It does not pulse, and it does not breathe.

## Object Motion

The brush moves once — in, one stroke, out — and is gone before the third beat. **After it leaves, nothing in the frame moves but the ink.**

## Environmental Motion

None. The paper does not move, the void does not fill, and nothing drifts across the frame.

## Physical Characteristics

- Weight: The ink has the weight of water in fibre. **It has no bounce.**
- Inertia: Once it is in the paper it keeps going without the hand, **and it never comes back.**
- Acceleration: Almost none, and it does not slow to a stop within the shot.
- Fluidity: A wet edge travelling through fibre — **not a membrane that inflates and then deflates.**
- Impact: None.

# 12. EMOTION

- Emotional Arc: The patience of a mark that is still arriving after the hand has gone.
- Emotional Events: The moment the brush leaves the paper and the ink keeps moving.

# 13. LIGHTING

- Base Lighting: Flat, even, frontal light on the sheet. **No directional key, and no shadow cast across the paper.**
- Lighting Events: None. The light does not change, and no shaft crosses the frame.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: Almost none — the dry contact of the brush for a fraction of a second as the stroke lands.
- Music: None.
- Environment: The room tone of a dry room, unbroken.

# 15. CONTINUITY

- Identity: The same sheet for the whole shot — same grain, same tone, same edges.
- Visual: Monochrome, flat light, bold negative space, washi grain in every frame.
- Motion: The ink moves for the whole shot, including the beats where nothing else does. **Limited animation is not acceptable — the ink is never a held frame.**
- Sound: The room tone is unbroken across the cut.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止・この作品は開示台帳を持たない）

- No second stroke. No retracing, no correction, no doubling of the line.
- No brush after the stroke lands. **The brush is gone before the shot ends.**
- **No ink narrowing, no ink retreating, no drying back to white. The ink is at its largest at the end.**
- No filled negative space. No dust, no haze, no particle, no light shaft entering the void.
- No colour. No colour-temperature shift. No red seal, no stamp, no signature, no seal box.
- No readable text of any kind.
- No person, no figure, no hand.

## MUST

- The stroke happens exactly once.
- **The ink spreads outward through the whole third beat and never comes back.**
- The void stays empty for the whole shot.
- The camera does not move.
- Monochrome throughout.

## PREFER

- The stroke placed off-centre, with the larger part of the sheet left empty.

## ALLOW

- A single dry tick as the brush meets the paper.

# 17. GENERATION PRIORITIES

1. **The ink is one-way** — it is at its largest at the end, and it never narrows, never retreats and never dries back to white. ⚠️ **This is the failure a soft mass produced for the neighbouring work — a mark that blooms and then shrinks reads as breathing, not as ink.** It outranks beauty.
2. **The stroke happens once** — no second stroke, no retracing, no correction.
3. **The void stays empty** — the reserved white survives the whole shot; nothing drifts in to fill it.
4. **The brush is gone** — after the stroke lands, nothing moves but the ink.
5. **The camera holds still** — a scroll, not a window; no movement for its own sake.
6. **Monochrome throughout** — no colour and no colour-temperature shift.
7. **The paper's texture** — washi grain, dry brush, bleeding.
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 6-second continuous cinematic take (16:9), sumi-e ink wash, on a single sheet of washi that fills the frame. Beats, deliberately uneven: [0-2s] blank paper, the brush entering the frame and not yet touching it; [2-3s] one stroke is laid — once, not corrected, not retraced — and the brush leaves the paper; [3-6s] the brush is gone and the ink enters the fibre and keeps spreading. **The ink moves one way only: it is at its largest at the end, and it never narrows, never retreats and never dries back to white.** The void stays empty for the whole shot, and the camera does not move. Monochrome throughout. (No person, no hand, no brush after the stroke, no second stroke, no seal, no readable text.)

## Visual Prompt

Sumi-e ink wash on washi paper. Graded black ink — the five inks — dry-brush strokes, bleeding edges, boldly reserved negative space, single-stroke economy, washi grain, dark ink dots. Monochrome: gradations of black on warm off-white paper, with no second hue anywhere in the frame. One sheet of paper fills the frame, flat and frontal, carrying one dark stroke whose wet edge has travelled outward into the fibre. Very low visual density: the paper, one stroke, and the void; nothing else. No second stroke, no retracing of the stroke, no brush after the stroke lands, no person, no figure, no hand, no color, no red seal, no stamp, no signature, no readable text, no filled negative space, no ambient particles, no haze, no light shafts crossing the frame, no hard outline, not photorealistic, no 3D render, no photographic surface.

## Motion Prompt

Hand-drawn ink wash. **The stroke is the event and it happens once** — a single decisive gesture that lands and is not revised, not retraced and not repeated; the brush enters, lays the mark, and leaves before the shot ends. **After the brush has stopped, the ink keeps moving**: the wet edge travels outward through the washi fibre for the whole of the last three seconds. **The movement is one-way — the ink is at its largest at the end; it never narrows, never retreats, never pulses, never breathes, and never dries back to white.** Nothing else in the frame moves: the paper does not flutter, the void does not fill, and no particle, haze or light shaft drifts in. **The camera does not move.** No second stroke, no morphing contours, no motion blur, no continuous ambient motion, no full animation.

## Camera Prompt

The frame is a scroll, not a window: one flat frontal view of the sheet, held at the paper's own scale, with the void given as much of the frame as the subject. **The camera does not move at all** — no push, no drift, no pan, no handheld, no whip. One continuous take; no cut.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of this work and of every word it holds; **if any speech is placed in it, that speech is Japanese.** **No speech is placed in this shot.** No dialogue, no voice-over, no narration. Sound effects: almost none — only the dry contact of the brush for a fraction of a second as the stroke lands. Ambient: the room tone of a dry room, unbroken. **Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell.**

## Negative Prompt

no color, no photorealistic, no hard outline, no second stroke, no retracing of the stroke, no ink retreating, no ink narrowing, no drying back to white, no brush after the stroke lands, no filled negative space, no ambient particles, no haze, no light shafts crossing the frame, no morphing contours, no motion blur, no camera move for its own sake, no seal, no signature, no stamp, no readable text, no watermark, no on-screen subtitles, no background music

## Style Motion

**The stroke is the event, and it happens once.** Motion is a single decisive gesture that lands and is not revised — not a continuous flow; between strokes, nothing moves. **The ink keeps moving after the brush has stopped** — bleeding and wicking continue into the washi, so what changes in the frame after the gesture is the paper's, not the hand's. **The camera is a scroll, not a window** — the frame holds still; the bold negative space is what the shot is about, and a moving camera spends it. **Stillness is the ground; the void stays empty** — nothing drifts in to fill it: no ambient particles, no haze, no light shafts crossing the frame. ⚠️ **What this style does not do**: full animation, continuous ambient motion, morphing contours, motion blur, or a camera that moves for its own sake. **The ink stays monochrome for the whole shot** — a colour or colour-temperature shift is a different style, not a beat of this one. (Source: the `Motion character` of the style card `sumi-e`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ippitsu-s01-6s-01`
- Segment ID: `01-1`
- Specification Version: `0.1.2`
  ⚠️ **この行は、この仕様の*現在*の版である**——`L25` がここを読み、各テイクの
  `source_version`（**投入した時点の版**）と突き合わせて、**ずれを註に書く。**
  ⚠️ **註を同じ行に足してはならない。** **足すと、この行は読まれなくなる**
  （`specmap.SPEC_VERSION_LINE` は行末までを版とする）——**私はこれを一度踏んだ**（2026-09-22）。
  **検査が黙ったことは、検査が通ったことではない。**
  ⚠️ **2本のテイクが投入されたのは `0.1.0` である**（`takes/ippitsu-s01-video-1.yaml` ／
  `…-video-2.yaml` の `source_version`）。**§18 は `0.1.0`・`0.1.1`・`0.1.2` で同一である**
  から、**投入文字列は版を跨いで変わっていない。**
- Generation Date: `2026-09-22`（⚠️ **根拠は戻ってきたファイルの時刻**——1本目 `00:18:11`、
  2本目 `00:36:03`。**著者が名乗った日付ではない。**）
- Adopted Take: `2`（**参照なし**。⚠️ **著者の裁定、2026-09-22**——`takes/ippitsu-s01-video-2.yaml`）
  ⚠️ **この欄は前は無かった。** **テイクが1本のときは要らなかった**——
  **採用はテイクの欄（`adopted`）に在り、ここはその写しである。**

## Resolved Values

- Duration: `6s`
- References: `REF_LOCATION (紙.base, 作成済み) ／ REF_STYLE (sumi-e, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
  ⚠️ **この行は「仕様が名指した参照」であって、「実際に渡した参照」ではない。**
  渡したものはテイクが持つ（`takes/ippitsu-s01-video-1.yaml` の `params.references`）。
- Temporal Structure: `3 beats, NON_UNIFORM — 2s / 1s / 3s. The ink = BEAT 3 at 3s (50%)`
- Camera Events: `none — the camera does not move. One continuous take`
- Action Events: `ACT_ENTER → ACT_LAY → ACT_WICK`
- Audio Events: `no dialogue ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.2` — **①（生成する）と ②（測る）が済み、著者が採否を決めた。** ③（型の同定）と ④（直す）は開いていない。
   ⚠️ **② は、いまテイク2本について済んでいる**——**1本目（参照あり）と2本目（参照なし）。**
   ⚠️ **採否も済んだ**（**著者の裁定、2026-09-22**）——**採用は2本目、不採用は1本目。**
   **著者の言葉**: 「**参照イメージがない方が自然だったよ。参照があると、筆跡が画面上に、
   すでに乗ってしまう**」
   ⚠️ **これは §6 の裁定である。** **`REF_LOCATION` は在るが、この動画へは渡さない。**
   ⚠️ **そして、これは測りと食い違う。** §13 の光も §14 の音も1本目が満たし2本目が満たしていない。
   **それでも著者は2本目を採った。**
   ⇒ **採否は測りが決めるものではない**——**採用は選別であり、作者は編集である**（`CLAUDE.md`）。

⚠️ **版ごとに動いた節。****`0.1.0` から `0.1.2` まで、動いたのは同じ3節だけである。**

| 版 | 動いた節 | `§18` |
|---|---|---|
| `0.1.0` → `0.1.1` | §6（`REF_LOCATION` 未作成→作成済み）・§19・§20 | **同一** |
| `0.1.1` → `0.1.2` | §6（裁定——渡さない）・§19（採用テイク）・§20（ここ） | **同一** |

⚠️ **`§1–18` は動いていない、ではない**——**§6 は2度動いた。**
   **動いていないのは `§18` であり、それは投入される唯一の節である。**
   ゆえに **`§18` の投入文字列は `0.1.0` のときと同一である**
   （「生成器へ投入するのは §18 だけである」——この仕様の冒頭）。
   ⚠️ **だが版は上げる。** 版はファイルの状態を指すものであり、
   **中身が動いたのに版が動かなければ、版は状態を指さなくなる**
   ——`params.source_version` が凍結しているのは、まさにその状態である。
   ⚠️ **`L25` はこれを見て「仕様が生成のあとに直っている」と註に書く。**
   **その註の後半（「もう一度そのままでは再生成できない」）は、この場合は当たっていない**——
   **投入される §18 は動いていないからである。****これは検査の側の穴である**（穴のまま記録する）。

⚠️ **画像仕様も同時に動いた**（`specs/image/shot-01-stroke.md`）——**あちらが渡す先を名指していた。**
   **節番号を持つのは動画の仕様だけである**（画像仕様は §1–20 を持たない）。
   ⚠️ **画像仕様は版を持たない。** **だから「`0.1.1` になった」とは書かない**——
   **このリポジトリは、あのファイルの版を名乗る欄を知らない**（`takes/ippitsu-s01-image-1.yaml` にも
   `source_version` は無い）。**無い版を書けば、書いた数が実測として読まれる。**
   ⚠️ **この2行は、私が一度踏んだ穴である**（2026-09-22。`HISTORY.md` の `0.33.7` を見よ）。

## Observed Problems

⚠️ **測った値はここに写さない。** 写しは食い違う——**第2の正典を作らず、第1の正典を指す。**
   **`takes/ippitsu-s01-video-1.yaml` と `takes/ippitsu-s01-video-2.yaml` を見よ。**
   ここには**判定だけ**を書く。

⚠️ **この節は、いまテイクを2本持つ。** 2本目は**著者が参照画像を外して生成したものである**
   （`01(参照イメージ無し)_…`）。**ゆえに、下の判定は「どちらのテイクの話か」を言わなければならない。**
   ⚠️ **1本目だけを読んだ判定が、いつまでも正しいとは限らない**——**実際、2本目で2つ変わった**（下の2項目）。

- ⚠️ **想定していなかったものが1つ在った——手である。****§20 の下の7項目に「手」は無かった。**
  実測で **14 フレーム（0.87–2.27s）**、枠の **1.45%** まで。**筆を握る指であり、左下から入る。**
  ⚠️ **そして §20 の3番目の risk が、これを塞ぐどころか許していた**——
  「**a hand that lingers**」と書いてある。**居座らない手は許される、と読める。**
  **§2 と §16 は手を禁じている。仕様の内部で食い違っている。**⚠️ **どちらを直すかは著者が決める。**
- ⚠️ **余白は使われた。だが §20 の4番目が名指した原因（靄・埃・光の筋）ではない。**
  **紙は暗くならない**（四隅は全時刻で 231–236）——**墨そのものが余白を使ったのである。**
  ⚠️ **これは §4（`The void stays empty for the whole shot`）と §8（墨は3秒広がる）が
  両立しないことから来ている**——18% から始まる染みが3秒広がれば、比は必ず逆転する。
- **フレームレートが食い違った**——§1 は `24fps`、戻りは `30fps`（`L25`）。
  ⚠️ **これはこの作品の決定ではない**——経路の性質であり、`hitosara/takes/README.md` に既に記録がある。
- **`params.references` が空であった。****「渡していない」ではなく「記録が無い」であった。**
  キー画像はこの動画より 7分24秒 早く在った——**ゆえに渡せた。**⚠️ **渡せたことは、渡したことではない。**
  ⚠️ **これは1本目についての記述である。****この欄は著者が埋めた**（`takes/ippitsu-s01-video-1.yaml` を見よ）。
  2本目は `references: []` である——**著者が名付けたからである。**
  ⇒ ⚠️ **そして著者が裁定した。****参照は渡さない。採用は2本目である。**（下の `### 裁定` を見よ）

### ⚠️ 2本目で変わったこと（2026-09-22、参照画像なしの1本）

- ⚠️ **手は参照から来ていなかった。****§20 の3番目の risk の原因についての私の見当は外れた。**
  **参照を外しても手は出た**——**むしろ増えた**（14 フレーム → **78**、1.40秒 → **2.57秒**）。
  ⚠️ **ゆえに手の原因は、この仕様の側に在る**——§4/§5 の主体の無い筆と、§2/§16 の禁止の衝突である。
  **2本目は、この穴が参照と無関係であることを示した。**⚠️ **n=1 対 n=1 である**（テイクを見よ）。
- ⚠️ **§13 LIGHTING を、2本目は満たしていない。****1本目は満たしている。**
  §13 は「Flat, even, frontal light… **No directional key**」と求める——
  **2本目には勾配が在る**（最小二乗で **25.3 レベル**、最も明るい角は左上。1本目は 2.8 レベル）。
- ⚠️ **§14 AUDIO を、2本目は満たしていない。****1本目は満たしている。**
  §14 は「Almost none — …**for a fraction of a second**」と求める——
  **2本目には 1.7秒・床から 35 dB の山が在る。**
  ⚠️ **そして山の頂点は「stroke lands」の時刻ではない。**
- ⚠️ **余白については、2本目のほうが残る**——**が、どちらも §16 の「larger part」は満たしていない。**
- ⚠️ **そして、この4項目は「この2つのファイル」の性質である**——
  **「参照なしの経路は §13 を満たさない」とは言えない。****n=1 対 n=1 を超えない。**

### ⚠️ 裁定（2026-09-22、著者）

- **採用は2本目（参照なし）。不採用は1本目（参照あり）。**
  **著者の言葉**: 「**参照イメージがない方が自然だったよ。参照があると、筆跡が画面上に、
  すでに乗ってしまう**」——`adopted: true` が `takes/ippitsu-s01-video-2.yaml` に、
  `adopted: false` が `takes/ippitsu-s01-video-1.yaml` に在る。
- ⚠️ **採否は、測りが決めたものではない。** **それがこの裁定の内容である。**
  上の4項目は**2本目に不利に並んでいる**（光・音・手の量・§20 の緩い条件）。
  **著者はそれでも2本目を採った。** ⇒ **採用は選別であり、作者は編集である**（`CLAUDE.md`）。
  ⚠️ **この裁定を「測りが間違っていた」と読まないこと。** **測りは正しく、それでも足りない。**
  **測りは「参照が何を画面へ持ち込むか」を測っていなかった**——
  **§7 の `before`（紙は白い）が、参照の中では既に終わっている**という一点を。
- ⚠️ **§6 への帰結**: **`REF_LOCATION` は在るが、この動画へは渡さない。**
  **紙の見た目は §4 と §5 の文が固定する。**
- ⚠️ **未解決のまま残ること**: §20 の3番目の risk（「a hand that lingers」）と §2/§16 の衝突、
  §4 と §8 の両立しないこと、§1 の `24fps`。
  **著者の裁定は、この3つに触れていない。****採否は、仕様の欠陥を消さない。**
- ⚠️ **規則の側の裁定**（**著者、2026-09-22**）: **上の §6 の裁定は、一筆だけのものである。**
  **基盤の規則——「キー画像は動画へ添付して渡る」——は変わらない。**
  ⇒ **`schemas/shot-record.schema.json` と `engine/ledger/specmap.py` は動かしていない。**
  ⚠️ **`reference_set` も動かしていない。****当時の意図として残る**（ショット記録を見よ）。

## Anticipated risks (to check in the first generation)

- **The ink may come back.** A soft wet edge that blooms and then shrinks reads as **breathing, not as ink** — and a diffusion model asked for "bleeding" will animate it both ways unless it is told not to. The one-way rule is front-loaded in §1, §2, §3, §8, §11, §16, §17 and §18; **verify frame by frame. This is the most likely failure of this shot.**
  **→ ⚠️ 起きなかった**（2026-09-22 実測。**テイクを見よ**——89 の段のうち減ったのは2つだけである）。
- **A second stroke may be added.** Models asked for a sumi-e stroke tend to complete the gesture — a second, balancing mark, or a retrace of the first.
  **→ 起きなかった。** 繋がった墨は1つである（テイクを見よ）。
- **The brush may stay in frame.** It must be gone before the third beat; a hand that lingers turns this into a shot about a hand.
  **→ ⚠️ §20 の条件は1本目で満たされた**（筆は 2.27s に消え、第三拍より前）。**だが、この1文が手を許した**
  ——**「居座る手」だけが悪いと読める。**⚠️ **そして、この項目の下に手が隠れていた。**
  ⚠️ **2本目はこの条件さえ満たしていない**——**手は 3.53s まで在り、第三拍に入って 0.53秒 残る。**
  **`Observed Problems` を見よ。**
- **The void may be filled.** Haze, dust motes, or a light shaft across the paper would spend the negative space, which is the composition.
  **→ 靄も埃も光の筋も無い。****だが余白は使われた**——**墨そのものによってである。**
  **`Observed Problems` を見よ。**
- **A seal may appear.** Ink-wash styles very often add a red seal; it is the most likely source of colour in the frame.
  **→ 印は起きなかった**（署名も読み取れる文字も無い。**焼かれた字幕も無い**）。
  ⚠️ **だが色は来た——手から来た。**
  **「色の源になりそうなもの」の予想が外れていた**——§20 は落款を名指したが、
  実際に彩度を持つ画素は**肌だけ**である（テイクを見よ）。
- **The camera may drift.** A slow push is the default behaviour of the model and it is not wanted here.
  **→ 起きなかった。****2つの方法が一致して (0,0) である**（位相相関／墨の無い紙片を追う方法）。
- **The shot may come back as a time-lapse** — the ink spreading in compressed time rather than in six continuous seconds.
  **→ 起きなかった。** 180 フレーム / 30fps の連続である。
- ⚠️ **この目録は、この1本では足りなかった。** 上の `Observed Problems` を見よ——
  **ここに無いものが1つ起きた。**
