# 画像仕様 — 一筆 第一ショット「白い紙が、墨を持つ」（様式美 / motion / 6s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。

⚠️ **この作品は物語ではない。** 1ショットだけの最小の作品であり、
**Style 4.3「動く絵画」が成立するかを試すために在る**（決定 2026-09-21、著者。D-14）。

---

⚠️ **この1枚が写すのは `after` の側である**——**墨が紙の中にあり、広がり続けているところ。**
   `§7` の Pull がそれである——「**The brush is gone and the ink is still spreading.**」＝
   `unit.after`（「**墨は紙の中にあり、広がり続けている。狭まらない。戻らない。**」）。

⚠️ **この1枚に、筆は無い。** 筆は第二の拍で紙を離れ、第三の拍には枠の外にいる。
   ⚠️ **「筆が無いこと」は、この1枚の内容である**——**空きは `Prompt` が書く**（`Negative` ではない）。

⚠️ **一方向である。** この1枚は**動きの一瞬**を止めたものであり、**その一瞬は「広がっている途中」**である。
   ⚠️ **対称な染みを描かせないこと**——**対称な染みは、広がりではなく結果である。**

⚠️ **Negative は §18 `Negative Prompt` と同一である。**
   ⚠️ **写らないものを禁じても、何も変わらない**（1枚は音を持たない）。
   **が、消さない**——**二経路の禁止が一字も違わないことが、この作品の規約である**（`bible.yaml`）。

⚠️ **この1枚は、この作品で最初に作られる画像である**（`ledger.yaml` の `紙.base` は「まだ無い」と言う）。

---

## 渡す先

- 生成器: （著者が選ぶ）（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `sumi-e`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/ippitsu-s01.yaml`
- 投入する文: **下の節の1段落目が `Prompt` であり、2段落目が `Negative` である**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない
  - ⚠️ **渡るのは、生成のあとである。** いまは1枚も無い（`shots/ippitsu-s01.yaml` の註を見よ）
- 記録: `shots/ippitsu-s01.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `sumi-e` —— **5つの穴**（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋5＝10 ではなく、**重なりを除いて8**である。

⚠️ **それでも、この節は7欄である。**（`L22` の註を見よ）
   **基盤は、様式の寄与を4つに固定している**——`specmap.SPEC_KINDS['image']['vars_from']['style']`
   が `SUBJECT`／`ACTION`／`LOCATION`／`ACCENT` の4名を**直に並べている**からである。
   ゆえに**5つ目の穴 `ASPECT` は、ここへ書いても書かなくても `L22` が1件鳴る**——
   検査が見ているのは**名乗ったカードの宣言と、この4名の一致**であって、
   **この節の中身ではない。**
   ⚠️ **`ASPECT` をここに足さない。** 足せば節の見出し（7欄）と `SPEC_KINDS` の両方と食い違う。
       **直すべきはどちらか——それは著者が決める**（この作品は鳴らしただけである）。
   ⚠️ **実測（2026-09-21）**: 様式カード55枚のうち、この4名と**一致するのは8枚**である
      （`luminous-anime` はその1枚であり、**既存の17本の画像仕様はすべてそれを名乗っている**）。
      **`sumi-e` はその8枚に入らない。**

- `SCENE`: the moment after a single stroke has been laid, with the ink already travelling into the paper
- `CHARACTERS`: no person and no figure — the brush was the only agent and it has already left the frame
- `SUBJECT`: one dark ink stroke on washi, its wet edge spreading outward into the fibre
- `ACTION`: the ink spreading outward from the stroke into the paper
- `LOCATION`: a single sheet of washi paper filling the frame
- `LIGHT`: flat, even, frontal light on the sheet, with no directional key and no shadow cast across the paper
- `ACCENT`: the wet edge of the stroke — the one place in the frame where the ink is still moving

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A sumi-e ink wash on a single sheet of washi paper that fills the frame, under flat and even frontal light with no cast shadow, with the wet edge of the stroke as the one place where the ink is still travelling. A scene board for the master staging of this one shot, in 16:9 — the composition, the camera and the light fixed as the standard the take must match. One dark stroke has been laid on the paper, once, and is not corrected and not retraced; the ink has entered the fibre and its wet edge is spreading outward, at its largest yet and still going. The brush is not in the frame — nothing is in the frame but the paper, the one stroke, and the void. Graded black ink, the five inks, dry-brush strokes, bleeding edges, single-stroke economy, washi grain, dark ink dots. Monochrome: gradations of black on warm off-white paper, with no second hue anywhere in the frame. Very low visual density: the stroke sits off-centre and the larger part of the sheet is left empty, the reserved white given as much of the frame as the mark. The frame is flat and frontal, at the paper's own scale, holding still.

no color, no photorealistic, no hard outline, no second stroke, no retracing of the stroke, no ink retreating, no ink narrowing, no drying back to white, no brush after the stroke lands, no filled negative space, no ambient particles, no haze, no light shafts crossing the frame, no morphing contours, no motion blur, no camera move for its own sake, no seal, no signature, no stamp, no readable text, no watermark, no on-screen subtitles, no background music

## 記録との対応

- `unit` … 「紙は白い。墨はまだ紙の外にあり、紙の中に無い。」→「**墨は紙の中にあり、広がり続けている。狭まらない。戻らない。**」
- `beats` … 0-2s 白い紙、筆がまだ触れていない／2-3s 一筆が置かれる、1回だけ／3-6s 筆は去り、墨が広がり続ける。
  **この1枚は BEAT 3 の途中である**——**広がりの終わりではなく、途中を写す。**
- `place` / `time` … `紙` / `時刻を持たない`
- `attached` … 無い。**この作品はまだ生成されていない**（ショット記録の註を見よ）
- ⚠️ **`rolemap` の `様式美` が持つ固有基準は「構図・余白・静止の強度」である。**
  **この1枚は、その3つを1枚で引く**——構図はオフセンターの一筆、余白は空いたまま、
  静止は「動いている途中の一瞬を止めた」ことである。
  ⚠️ **引けない基準を、引けたことにしない。** この作品に引けない基準は無い——
  **人物も、聞き手も、声も無い作品だからである。**
