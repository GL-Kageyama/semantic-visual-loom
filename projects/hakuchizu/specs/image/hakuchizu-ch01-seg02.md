# 画像仕様 — 『白地図』第1章「暖簾」 S02（運動 / motion / 8s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⚠️ **この1本の変化は「歩くこと」ではない。** 変化は**影の寿命**である——
**この1枚は「影がひとつだけ在る」状態を切る。** ⚠️ **影が2つ写れば、この1枚は別の話の1枚になる。**

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg02.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg02.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: footsteps crossing an unmarked white street, the shadow born under the foot and gone before the next step lands
- `CHARACTERS`: 灯 seen from behind, mid-step, face not drawn — one figure only, no second person anywhere
- `SUBJECT`: 灯's back and the single shadow under the stepping foot
- `ACTION`: walking at the pace of twenty years, the shadow placed under the foot and taken back again
- `LOCATION`: the same stone-paved street as the art board, seen level and low to the ground
- `LIGHT`: morning light lying flat on the white, even and without direction
- `ACCENT`: the one shadow — dark, edged, and the only dark thing in the frame
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of 灯's back mid-step and the single shadow under the stepping foot, walking at the pace of twenty years as the shadow is placed under the foot and taken back again, at the same stone-paved street as the art board seen level and low to the ground, with the one shadow — dark and edged — the only dark thing in the frame. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. Thin visible pencil line art beneath the washes. The story's four colours — vermilion, ultramarine, ochre and a faint glimmer of gold gilt — reach this frame only as the shadow's dark: the street is white, the figure is white, and the town's colour is not here to be seen. The white ground kept pure white, not cream or ivory. Flat and paper-based, no directional light, no spatial illusion. 灯 is drawn from behind — back, outline, and one hand — and the face is not drawn at all. The shadow is laid down like a stroke of pigment and keeps a hard edge; it is not blurred and it is not a photographic shadow. Only one shadow exists in the frame; there is no second person and no second footfall.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no second person, no second shadow, no more than one shadow in frame, no visible face on the figure, no blurred shadow, no soft photographic shadow, no numerals, no numbers, no noren in frame, no shop front in frame, no directional light, no sunbeam, no fully-painted flat vermilion cloth

## ⚠️ この Negative の末尾1節は、開示の系列である

`no fully-painted flat vermilion cloth` は S01–S07 が持ち、**S08 で落ちる**（`ledger.disclosure`）。
⚠️ **画像の系列を読む検査は無い**（`L10` の相手は §18 である）——人が読める形でここに置く。

## 記録との対応

- `unit` … 「まだ誰の足音も無い」→「影はもう消えている」。**この1枚が切るのは後者である**——
  ⚠️ **影が在る1枚でなければ、このショットの画にならない**（消えたあとの白は S05 の画である）。
- `beats` … **切る瞬間は 2-5s（`held`）**——**影の寿命を観客の身体に入れる側**である。
- `forbidden_set` に `灯の顔` が在る … `no visible face on the figure` がその節である。
- `attached` … `灯.identity`・`灯.states.支払いの前`・`灯.negatives`・`通り.base`・`通り.geography`
  ⚠️ **`灯.states` は `支払いの前` である**——**この1枚の指先は、まだ色を持っている**（S11 で白くなる）。
