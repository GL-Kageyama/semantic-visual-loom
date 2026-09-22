# 画像仕様 — 『白地図』第1章「暖簾」 S04（所作 / motion / 5s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⚠️ **この1本の変化は「避けること」ではなく「線」である。** ゆえにこの1枚が切るのは
**線がそれている側**である——**まっすぐな線を切れば、この1枚は S02 と同じ画になる。**
⚠️ **この1本は、自転車を一度も「自転車」として見せない。**
**白は形であって、輪郭線ではない**——**物が白に置き換わっているのであって、物の絵が白いのではない。**

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg04.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg04.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: the walking line bending once around a white bicycle shape and coming back to straight
- `CHARACTERS`: 灯 seen from behind, in the middle of the bend, face not drawn — one figure only
- `SUBJECT`: the thin pencil line of the walk, bent outward once around the white shape
- `ACTION`: the line stepping aside around the white shape and returning, without slowing
- `LOCATION`: the same street, in front of the closed shutters where the white bicycle shape leans
- `LIGHT`: morning light lying flat on the white, even and without direction
- `ACCENT`: the white bicycle shape — white on white, with no outline, no shadow and no light of its own
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of the thin pencil line of a walk bending outward once around a white bicycle shape, with 灯 seen from behind in the middle of the bend — the line stepping aside and returning without slowing — at the same street in front of the closed shutters where the white bicycle shape leans against the wall, under morning light lying flat on the white. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. Thin visible pencil line art beneath the washes — and here the line of the walk stays visible after it bends, because a stroke that covers what it crosses keeps its revision. The white bicycle shape is a shape of white paper replacing a thing that was there, not a bicycle drawn in line and not a bicycle painted white: it has no outline of its own, no shading, no shadow and no highlight. The story's four colours are not in this frame; the street is white and the white ground is kept pure white, not cream or ivory. Flat and paper-based, no directional light, no spatial illusion. 灯 is drawn from behind — back, outline, and one hand — and the face is not drawn at all. The bend is narrow: the least that still reads as a step aside.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no visible person among the white shapes, no cat in frame, no outline drawing of a bicycle, no mechanical detail drawn in line, no spokes drawn, no shading on the white shape, no shadow cast by the white shape, no highlight on the white shape, no second person, no visible face on the figure, no numerals, no numbers, no directional light, no fully-painted flat vermilion cloth

## ⚠️ この Negative の末尾1節は、開示の系列である

`no fully-painted flat vermilion cloth` は S01–S07 が持ち、**S08 で落ちる**（`ledger.disclosure`）。
⚠️ **画像の系列を読む検査は無い**（`L10` の相手は §18 である）——人が読める形でここに置く。

## 記録との対応

- `unit` … 「線は、まっすぐである」→「線がひとつ曲がった」。**この1枚が切るのは後者である**——
  ⚠️ **曲がった線は消えない**（様式の法「the revision stays visible」）。
  **ゆえにこの1枚には、曲がったあとの線が写っている必要がある。**
- `beats` … **切る瞬間は 2-3s（`held`）**——**この1本の核である1秒**を切る。
- `forbidden_set` に `猫` が在る … 草稿 L5「猫はもういない」。`no cat in frame` がその節である。
- `attached` … `灯.identity`・`灯.states.支払いの前`・`灯.negatives`・`通り.base`・
  `通り.geography`・`白い形.appearance`・`白い形.negative`
  ⚠️ **`灯の足元に影を置かない。** 影は S02 の主題である（記録の `motion.law`）。
  ゆえにこの1枚の Negative に `no more than one shadow` を**置かない**——
  **置けば、S02 の節をこの1枚へ写すことになる。影そのものを禁じるのは、この1枚の仕事ではない。**
