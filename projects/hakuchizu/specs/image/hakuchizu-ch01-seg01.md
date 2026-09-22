# 画像仕様 — 『白地図』第1章「暖簾」 S01（情景 / motion / 6s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である——
**種類の話であって、モードの話ではない**（`L18` がこの形を見る）。
⚠️ **この1枚は動画の最初のコマではない。** 「このショットの見せ場の1枚」であり、
**添付（参照画像）として**動画へ渡る（決定 2026-09-13）——最初のコマにすれば、
**`unit` の変化が画面の上で起きなくなる。**
⚠️ **この1本に人は立たない**（`shots/hakuchizu-ch01-seg01.yaml`）——この1枚にも立たない。

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg01.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**（決定A・決定B）
  ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**——
  見出しが本文の間にあると、選択がそれを巻き込む。**繋がった写しは置かない**（写しは食い違う）。
- 記録: `shots/hakuchizu-ch01-seg01.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**同じ値が両方の穴に入る。**
5＋5＝10 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`gouache-abstract` の5つ目の穴 `ASPECT` は、`scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: the last of the night's colour going out of an emptied street at first light
- `CHARACTERS`: no figure in frame — the street is empty
- `SUBJECT`: a downtown street returned almost entirely to paper white, the last thin colour still lying on a roof and on a door
- `ACTION`: the vermilion on the roof going out first, then the ultramarine on the door, until the white is the same white everywhere
- `LOCATION`: a downtown street of stone paving and closed shutters, seen wide, before the sun is up
- `LIGHT`: the first thin light of dawn lying flat on the white, even and without direction
- `ACCENT`: the two places where colour is still remembered — the roof and the door
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of a downtown street returned almost entirely to paper white, the last thin colour still lying on a roof and on a door, with the vermilion on the roof going out first and then the ultramarine on the door, until the white is the same white everywhere — at a street of stone paving and closed shutters seen wide before the sun is up, with the two places where colour is still remembered catching the least colour left in the frame. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. Thin visible pencil line art beneath the washes. The story's four colours — vermilion, ultramarine, ochre and a faint glimmer of gold gilt — present only where the town still remembers: the vermilion on the roof already gone pale, the ultramarine on the door not yet paled, ochre and gold only as small accents, none of them saturated. The white ground kept pure white, not cream or ivory. Flat and paper-based, no directional light, no spatial illusion — the first light of dawn lies on the white as an even film and does not make it shine. No figure in frame: the street is empty, no one walks, no one stands. Wide, quiet, almost without incident.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no figure in the street, no person in frame, no cat in frame, no numerals, no numbers, no house numbers, no noren in frame, no shop front in frame, no directional light, no sunbeam, no light shaft, no lens flare, no fully-painted flat vermilion cloth

## ⚠️ この Negative の末尾1節は、開示の系列である

`no fully-painted flat vermilion cloth` は、**S01 から S07 までの7枚が持ち、S08 で落ちる**——
`ledger.disclosure` の `negative: changed` がその記録である。
⚠️ **この1枚に暖簾は写らない。** それでも節を落とさないのは、
**系列が「ショットの都合」ではなく「観客の知識の順序」だからである。**
⚠️ **画像の系列を読む検査は無い**（`L10` の相手は §18 である）——
**相手は引き渡しの層である**（段2）。だからここに人が読める形で書いておく。

## 記録との対応

- `unit` … 「戻りかけの色がまだ残っている」→「色はどこにも無い」。**この1枚が切るのは前者である。**
- `beats` … **切る瞬間は 0-2s（`held`）**——**色がまだ数えられる側**である。
  ⚠️ **消えたあとを切れば、この1枚はただの白い通りになる。**
  **このショットの画の同一性は「色がまだ在る白」であって、「白」ではない。**
- `forbidden_set` に `灯`・`猫`・`数字`・`写真的な四角` が在る … **この1枚に人は立たず、数を置かない。**
  ⚠️ **`no numerals` は「数は町を戻さない」（草稿 L7）の画の側である。**
- `attached` … `通り.base`・`通り.geography`（**人物の鍵が1つも無い。これは省き忘れではない**）
