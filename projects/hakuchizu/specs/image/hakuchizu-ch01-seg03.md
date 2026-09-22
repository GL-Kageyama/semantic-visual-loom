# 画像仕様 — 『白地図』第1章「暖簾」 S03（質感 / motion / 7s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⚠️ **この1本に人は立たない**（草稿 L5「通りに人影はない」）——**撒いた者は、この1枚にも居ない。**
⚠️ **この1本は「白のなかで唯一動くもの」を撮る。** ゆえにこの1枚が切るのは、
**水がまだ在る側**である——**乾いた境だけを切れば、動くものが画から消える。**

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg03.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg03.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: water sprinkled before dawn drying on the paving until only its boundary is left, faintly darker
- `CHARACTERS`: no figure in frame — whoever sprinkled the water is never shown
- `SUBJECT`: the water's trace drying on the stone paving and the dry boundary it leaves
- `ACTION`: the boundary moving outward as the water goes, the dry side widening
- `LOCATION`: the stone paving of the same street, seen from above and close
- `LIGHT`: morning light lying flat on the white, even and without direction
- `ACCENT`: the boundary line — only faintly darker than the white around it
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of the water's trace drying on the stone paving and the dry boundary it leaves, with the boundary moving outward as the water goes and the dry side widening, at the stone paving of the same street seen from above and close, under morning light that lies flat on the white — the boundary line only faintly darker than the white around it. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. Thin visible pencil line art beneath the washes. The wet paving and the dry paving are told apart by how dense the wash is and not by shine: the water lies as a thin transparent wash over the stone, and gouache is opaque, so the stone is covered where the water is, never glowing and never reflective. The story's four colours reach this frame only as the faint density of that wash; the street is otherwise white, and the white ground is kept pure white, not cream or ivory. Flat and paper-based, no directional light, no spatial illusion. No figure in frame: no one sprinkles, no one walks, no one stands. The dry boundary is the only thing moving, and it is almost nothing — the least mark that still reads.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no figure sprinkling water, no person in frame, no cat in frame, no rain, no falling water, no splash, no droplets in the air, no wet reflection, no mirror-like paving, no puddle, no numerals, no numbers, no directional light, no sunbeam, no fully-painted flat vermilion cloth

## ⚠️ この Negative の末尾1節は、開示の系列である

`no fully-painted flat vermilion cloth` は S01–S07 が持ち、**S08 で落ちる**（`ledger.disclosure`）。
⚠️ **画像の系列を読む検査は無い**（`L10` の相手は §18 である）——人が読める形でここに置く。

## 記録との対応

- `unit` … 「乾いたところと乾いていないところの差が、まだ読める」→「乾いた境だけが濃い」。
  **この1枚が切るのは前者である**——⚠️ **差が読めなければ、この1枚は乾きを見せられない。**
- `beats` … **切る瞬間は 0-2s（`sparse`）**。⚠️ **5-7s（乾ききった側）を切れば、
  「白のなかで唯一動くもの」が画から消える**（註）。
- `forbidden_set` に `水を撒く者` が在る … `no figure sprinkling water` がその節である。
- `attached` … `通り.base`・`通り.geography`・`水の跡.appearance`・`水の跡.negative`
  ⚠️ **`no wet reflection` と `no glossy` は、様式の `avoid`（`gloss`）と `水の跡.negative` の
  両方に由来する**——**濡れは、色の濃さで示す。光らせない。**
