# 画像仕様 — 『白地図』第1章「暖簾」 S10（開示 / still / 6s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⚠️ **この1枚が切るのは、減る前である。** 草稿 L19「ただ、うしろのほうで、
**いちばん白に近かったものがひとつ減った。**」——
**空いた場所を切れば、この1枚は「減ったあと」をモデルへ渡すことになり、
6秒のうちの1秒（`dense`）が最初から起きている画になる。**
⚠️ **減ることは、動くことではない。** 消えるものは、どこかへ行かない——
**その形の上に紙が戻るだけである**（S01 と同じ法）。**「減る」を運動として撮れば、
この1本は「何かが飛び去る」1本になる。**

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg10.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg10.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: the payment finishing — the one white shape nearest to white is the one that will go
- `CHARACTERS`: 灯 standing below at the edge of the frame, seen from behind, face not drawn — not counting
- `SUBJECT`: the row of white laundry shapes hanging on the second-floor veranda of the neighbouring house, one of them a shade whiter than the rest
- `ACTION`: the shapes hanging without moving, or the one nearest to white having gone and left its place on the line empty
- `LOCATION`: the front of the noren shop, the neighbouring veranda above inside the same frame, the vermilion noren at the frame's edge
- `LIGHT`: morning light lying flat on the white, even and without direction
- `ACCENT`: the single shape that is a shade whiter than the others — the difference is small
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of the row of white laundry shapes hanging on the second-floor veranda of the neighbouring house, one of them a shade whiter than the rest, the shapes hanging without moving — 灯 standing below at the edge of the frame, seen from behind, not counting — at the front of the noren shop with the neighbouring veranda above inside the same frame and the vermilion noren at the frame's edge, under morning light lying flat on the white, with that one shade of white difference holding the frame. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. The laundry shapes are shapes of white paper where things were: they carry no outline of their own, no shading and no shadow, they do not swing in the wind, and they are all white — the one nearest to white is only a shade whiter, and it is nearest to white rather than white. Where a shape has gone, the line is left empty and nothing else marks the place: what is left is a rope and a gap, because nothing goes anywhere and there are no marks of departure. 灯 is drawn from behind — back, outline, and one hand — and the face is not drawn at all. The cloth at the frame's edge is the faded vermilion of a cloth through a second winter, and its lower hems are indigo. Flat and paper-based, no directional light, no spatial illusion. No figure is among the white shapes and nobody stands on the veranda, and the frame holds no number of any kind.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no flat vermilion without pigment body, no dry even vermilion paint, no visible person among the white shapes, no figure on the veranda, no cat in frame, no numerals, no numbers, no counting marks, no tally marks, no lifted or swinging laundry, no wind in the laundry, no outline around the white shapes, no shadow under the white shapes, no marks of departure, no kettle, no visible stove or fire, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no directional light

## ⚠️ この Negative は、S08 で動いたあとの側である

`no flat vermilion without pigment body` と `no dry even vermilion paint` が入り、
`no fully-painted flat vermilion cloth` が落ちている（`ledger.disclosure`）。
⚠️ **`no marks of departure` は、この1枚の法である**——**減ることは、その形の上に紙が戻ることである。**
**飛沫も、跡も、行き先も置かない。**

## 記録との対応

- `unit` … 「いちばん白に近いものがひとつある」→「ひとつ減った」。**この1枚が切るのは前者である。**
- `beats` … **切る瞬間は 0-2s（`held`）**——**減る前**である。
  ⚠️ **差は小さくする**（`beats` の註）——**「いちばん白に近い」は、いちばん白いことではない。**
- ⛔ **減るものを「隣家の二階のベランダ」に置いたのは発明である**（要承認）。
  草稿は「うしろのほうで」と書き、**どこの白が減ったかを書かない**（`ledger.disclosure` の註）。
- `forbidden_set` に `減る白の正体` が在る … **何が減ったのかを描かない。**
  **名指せないことが、この1本の内容である。**
- `attached` … `灯.identity`・`灯.states.支払いのあと`・`灯.negatives`・`暖簾の店の前.base`・
  `暖簾の店の前.geography`・`暖簾の店の前.states.朱が戻った`・`暖簾.appearance`・`暖簾.negative`・
  `白い形.appearance`・`白い形.negative`
