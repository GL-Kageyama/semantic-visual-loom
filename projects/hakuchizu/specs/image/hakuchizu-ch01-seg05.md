# 画像仕様 — 『白地図』第1章「暖簾」 S05（総覧 / still / 6s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⚠️ **`総覧` は「広い画」ではない。** **列ぜんたいが一度に主題になる**ことがこの種別である——
**この1枚に寄りの画を1枚も挟まない。**
⚠️ **この1本に人は立たない。** ゆえにこの1枚にも立たない（`shots/hakuchizu-ch01-seg05.yaml`）。
⚠️ **この1枚が切るのは「暗さの差がまだ在る」側である**——**差が消えたあとの白は、
このショットの結論であって、このショットの画ではない。**

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg05.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg05.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: morning light crossing a row of white shutters until the white is the same white everywhere and the row can no longer be counted
- `CHARACTERS`: no figure in frame
- `SUBJECT`: the row of white shutters, all of them equally white by the end
- `ACTION`: the light crossing from the near end of the row to the far end, the difference in darkness closing behind it
- `LOCATION`: the same street, seen along the row of closed shutters rather than at any one of them
- `LIGHT`: the morning light crossing the row — flat and even, shown as a change in brightness and gaining no direction
- `ACCENT`: the vanishing difference between the near end and the far end of the row — the last place a unit could still be seen
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of a row of white shutters under morning light crossing from the near end to the far end, the difference in darkness closing behind it until the white is the same white everywhere and the row can no longer be counted — at the same street, seen along the row of closed shutters rather than at any one of them, with the vanishing difference between the near end and the far end the last place a unit could still be seen. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. Thin visible pencil line art beneath the washes. This is a total view and not a close view: the whole row is the subject at once, and there is no single shutter, no single house and no single detail picked out. The light is shown as brightness travelling along the row and never by a shadow growing — this style has no directional light, and the white does not shine, because the white is the paper itself. The story's four colours are not in this frame; the white ground is kept pure white, not cream or ivory. Flat and paper-based, no spatial illusion. No figure in frame, no numbering and nothing to count by: no house number, no plate, no mark on any shutter.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no visible person among the white shapes, no cat in frame, no numerals, no numbers, no house numbers, no door numbers, no lettering on the shutters, no directional light, no sunbeam, no lengthening shadows, no cast shadow on the shutters, no close view, no fully-painted flat vermilion cloth

## ⚠️ この Negative の末尾1節は、開示の系列である

`no fully-painted flat vermilion cloth` は S01–S07 が持ち、**S08 で落ちる**（`ledger.disclosure`）。
⚠️ **画像の系列を読む検査は無い**（`L10` の相手は §18 である）——人が読める形でここに置く。

## 記録との対応

- `unit` … 「暗さの差が、列にひとつずつという数え方を与えている」→「暗さの差が消えた」。
  **この1枚が切るのは前者である。**
- `beats` … **切る瞬間は 2-4s（`held`＝この1本の核）**——**差が縮んでいる最中**である。
  ⚠️ **差が無い側を切れば、この1枚は「白い壁」の1枚になり、法（草稿 L7）が画から落ちる。**
- `mode: still` に対して … **止まるのは主題（列）であって、画面ではない。動くのは光である。**
  この1枚に光の**方向**は無い——**明るさの差としてだけ在る**（記録の `motion.quality`）。
- `forbidden_set` に `数字` が在る … `no numerals`・`no numbers`・`no numbering` がその節である。
  ⚠️ **草稿 L7「数字は町を戻さない」——数を画に置けない。**
- `attached` … `通り.base`・`通り.geography`・`白い形.appearance`・`白い形.negative`
