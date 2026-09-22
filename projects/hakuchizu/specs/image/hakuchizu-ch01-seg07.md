# 画像仕様 — 『白地図』第1章「暖簾」 S07（モンタージュ / motion / 9s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⚠️ **この1本の変化は「薄い鉛筆の格子が白に浮かぶこと」である。色はまだ来ない。**
——**ゆえにこの1枚は、格子が置かれたあとの布を切る。** **色が1つでも入れば、この1枚は S08 の1枚になる。**
⚠️ **切らない。** `モンタージュ` と名乗るが**カットを1つも使わない**——
**格子は、同じ一枚の布の上に一本ずつ置かれる**（記録の註）。
⛔ **布に載るのは格子だけである**（2026-09-22 の著者の裁定・第二）——
⚠️ **手も、頭も、品も、載らない。** **格子は図ではない**（下の「布に載るもの」を見よ）。

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg07.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg07.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: a faint pencil grid lying on the white cloth, with no colour yet and nothing drawn inside the cells
- `CHARACTERS`: nobody is in the frame and nobody is drawn on the cloth — the grid is a structure, not a picture
- `SUBJECT`: the white cloth with a faint pencil grid on it — thin ruled lines crossing at even intervals, the cells left empty
- `ACTION`: the grid having been laid one line at a time and stopped, leaving the cloth still white
- `LOCATION`: the front of the noren shop, the cloth seen straight on
- `LIGHT`: morning light lying flat on the white, even and without direction
- `ACCENT`: the thinness of the ruling — pencil and not pigment: no bloom, no weight, no colour
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of a white noren carrying a faint pencil grid — thin ruled lines crossing one another at even intervals, laid over the whole cloth like the graticule of a map, with every cell left empty — the grid having been laid one line at a time and stopped, leaving the cloth still white, at the front of the noren shop with the cloth seen straight on, under morning light lying flat on the white, with the thinness of the ruling itself carrying the frame. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. Here the pencil ruling is the whole picture and the washes have not arrived: the lines are dry, thin, uneven in pressure, even in spacing and grey, they do not bloom, they do not thicken and they carry no colour — the cloth under them is paper, kept pure white and not cream or ivory. Nothing is drawn inside the cells: they are empty paper, and no picture, no object, no figure and no letter appears anywhere on the cloth. The story's four colours are not in this frame at all. Flat and paper-based, no directional light, no spatial illusion. The ruling is one group laid on one whole undivided cloth. No figure is drawn anywhere: no hand, no head, no face, and nobody is named and nothing is written — the grid is structure, not a scene.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no colour on the noren, no wash on the cloth, no shading, no checkered pattern, no plaid, no printed textile pattern, no checkerboard, no wind in the cloth, no swinging cloth, no lifted cloth, no drawn face, no face on the cloth, no panel divisions, no split frame, no comic panels, no legible text on the noren, no shop name on the noren, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no numerals, no numbers, no directional light, no fully-painted flat vermilion cloth

## ⚠️ この Negative の末尾1節は、開示の系列である

`no fully-painted flat vermilion cloth` は S01–S07 が持ち、**S08 で落ちる**（`ledger.disclosure`）。
⛔ **この1枚の Negative は、2026-09-22 の裁定（第二・格子）で動いた。**
⚠️ **旧い文はこう書いていた**——「S07 は `negative: covered` を宣言している。**この1枚の節の集合は
S06 と同じである。**」 **2つとも偽である。**
- **台帳の側**——`seg07` は `negative: changed` になった（下の4節を足したため。`ledger.disclosure`）。
- **このカードの側**——**この1枚の節の集合は、初めから S06 と同じではなかった。**
  ⚠️ **2026-09-22 の裁定の直前に数えた**（`no watermark` の行を `,` で割った数）——
  **S06 は41節、S07 は37節である。** S06 だけが `no wind in the cloth` や `no door opening`・
  `no smoke` を持つ。⛔ **「集合を同じくする」は、私が書いた註であって、データではなかった。**
  ⚠️ **この裁定のあと、S07 は44節である**（+4の柄・+3の静止）。

⚠️ **足した4節**——`no checkered pattern` ／ `no plaid` ／ `no printed textile pattern` ／
`no checkerboard`。**動画の側（§18）と同語である。**
⚠️ **理由は動画と同一である**——**「布＋等間隔の格子」は、モデルにとってチェック柄
（ギンガム・タータン）の語彙に最も近い。** ⛔ **そして、この危険は画像の側でより大きい**——
**この1枚が先に作られ、動画はこの1枚を animate する。** ここでギンガムが出れば、
**動画の Negative はもうそれを消せない。**

⚠️ **`no wind in the cloth`・`no swinging cloth`・`no lifted cloth` を戻した。**
**S06 が持ち、S07 が落としていた3節である**（旧い註はこれを「集合を同じくする」の裏づけに
使っていたが、**落ちていたので裏づけになっていなかった**）。
⛔ **S07 の布は動かない。** 出典は2つある——
`specs/video/hakuchizu-ch01-seg07.md` **§18 `Motion Prompt`**「**The cloth itself never moves:
it does not swing, does not lift, does not flutter and does not answer anything,
and there is no wind in this shot.**」（**生成器へ渡る文である**）、
および **§15 CONTINUITY**「動くのは格子だけである。**布は動かず、カメラも動かない。**」。
**ゆえにこの3節は、この1枚では正しい。**
⚠️ **S08 の画像では、この3節は使えない**——**あちらでは色の着いたところが動く**（裁定・第三）。

⛔ **2026-09-22 の著者の指示で、S08 の文字列から格子が外れた**
（`specs/video/hakuchizu-ch01-seg08.md` §20・`PLAN.md` §4-g）。
⚠️ **この1枚（S07）は、いまも格子を切っている**——**こちらからは書き換えていない。**
⛔ **この1枚の格子が S08 へ渡るかは、著者の裁定を仰いでいる**（同 §20 の申し送り1）。
⚠️ **裁定を仰ぐ根拠**——**著者自身の S08 の1枚（`08_ChatGPT Image …16_14_20.png`）に、
線は1本も無い。** **§18 が、その1枚に無いものを名指していた。**

## ⛔ 布に載るもの——**格子だけである。図は描かない**（2026-09-22 の著者の裁定・第二）

⛔ **布に載るのは、薄い鉛筆の格子だけである。**
⚠️ **格子は図ではない**——**地図の経緯線である**（`props.暖簾.appearance`）。
**桝目の中は空である。** **手も、頭も、品も、字も、描かない。**

⚠️ **この裁定に至った道（第一の裁定——品を落とす）。** 1段落目の名詞句が、はじめ
**魚そのものを指す語順**になっていた——**色を通す S08 の初回生成で、布の上に魚の絵が描かれた。**
句を「結ばれた包み」に直すと、**今度は包みが透けて、中の魚が見える画**になった。
**2度とも品が出たので、品の名を英語から全部落とした。**

⚠️ **そして第二の裁定で、品を落としたあとに残っていた「形」も落ちた。**
**手と頭の線は、布の上に載らない**——⛔ **載るのは格子である。**
**理由は同じ機序である**——**名詞を肯定文が名指せば、モデルはそれを描く。**
⚠️ **「差し出す手」は、この作品では品と同じ強さの名詞である。**
**ゆえに、この1枚が名指すのは「格子」だけである**（`PLAN.md` §4-e）。

## 記録との対応

- `unit` … 「布の上には何も無い」→「薄い鉛筆の格子が置かれている」。**この1枚が切るのは後者である。**
- `beats` … **切る瞬間は 7-9s（`held`）**——**格子が止まり、色が来ない側**である。
  ⚠️ **この2秒が山への溜めである**（`transformation` の `TRIGGER` がここで画面に置かれる）。
- ⛔ **この1枚は発明である。** 草稿は色の話しか書かない。**線と色を2本に分けたのは、
  この作品の様式が既に持っている工程（薄い鉛筆の線画の上に薄塗りのウォッシュ）を2本に分けたことである。**
  ⚠️ **`hakuchizu-imageboard/01-1` の共通様式は「線画だけの領域を作らない」と言う**——
  **この1枚は、線画だけの1枚である。** **裁定を仰ぐべき一行である**（`PLAN.md` §1・記録の ⛔）。
  ⛔ **第二の裁定（格子）は、この一行への回答ではない。** **格子もまた鉛筆である**——
  **この1枚は、依然として線画だけの1枚である。** **申し送りは生きている。**
- `forbidden_set` に `布の上の顔` が在る … `no face on the cloth`・`no drawn face` がその節である。
- `attached` … `灯.identity`・`灯.negatives`・`暖簾の店の前.base`・`暖簾の店の前.geography`・
  `暖簾の店の前.states.白`・`暖簾.appearance`・`暖簾.negative`
