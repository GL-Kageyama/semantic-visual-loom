# 画像仕様 — 『白地図』第1章「暖簾」 S06（反応 / still / 8s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⚠️ **この1本の変化は「触れないこと」である。** 草稿 L9「灯は房に触れそうになって、**やめる。**」
——⚠️ **ゆえにこの1枚は、指が止まっている側を切る。** **触れたあとの1枚は、別の話である。**
⚠️ **この1本の風は、S09 で戻ってくる。** 同じ風であり、ここでは**布が答えない**。

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg06.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg06.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: fingertips stopping short of a hem — the white cloth does not answer the wind
- `CHARACTERS`: 灯 — only one hand and part of the arm at the edge of the frame, from the side; the figure's face is never in the frame
- `SUBJECT`: a white undyed noren hanging from its rod, and 灯's fingertips stopped short of one hem
- `ACTION`: the wind passing through as dust sliding on the paving, the fingers stopping short, the cloth not moving at all
- `LOCATION`: the front of the noren shop on the same street
- `LIGHT`: morning light lying flat on the white, even and without direction
- `ACCENT`: the small distance between fingertip and hem — the whole shot is in that gap
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of a white undyed noren hanging from its rod and 灯's fingertips stopped short of one hem, the wind passing through as dust sliding on the paving while the cloth does not move at all — at the front of the noren shop on the same street, under morning light lying flat on the white, with the small distance between fingertip and hem holding the whole frame. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. Thin visible pencil line art beneath the washes. The noren is one cloth of white paper hanging from a bar, its several hems hanging straight down, and it is blank: no drawing, no pattern, no mon, no shop name, no text — its white is the white of the paper itself, kept pure white and not cream or ivory. The cloth does not swing, does not lift and does not answer: only the dust moves, and the dust slides as placed grains of pigment and not as blurred smoke. 灯 is present only as one hand and part of an arm at the frame edge, seen from the side; the face is not drawn at all, and the fingertips still hold their colour. Flat and paper-based, no directional light, no spatial illusion. The camera never crosses the noren and the shop's interior is not in the frame.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no swinging cloth, no fluttering noren, no wind in the cloth, no lifted cloth, no legible text on the noren, no shop name on the noren, no drawing or pattern on the noren, no crest or mon on the noren, no colour on the noren, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no door opening, no steam, no smoke, no numerals, no numbers, no directional light, no blurred dust, no smoke-like haze, no fully-painted flat vermilion cloth

## ⚠️ この Negative の末尾1節は、開示の系列である

`no fully-painted flat vermilion cloth` は S01–S07 が持ち、**S08 で落ちる**（`ledger.disclosure`）。
⚠️ **この1枚に朱は1つも無い**（このショットの暖簾は白である）。それでも節を落とさないのは、
**系列が「ショットの都合」ではなく「観客の知識の順序」だからである。**

## 記録との対応

- `unit` … 「指先は房の手前にある」→「指は戻っている」。**この1枚が切るのは前者である。**
- `beats` … **切る瞬間は 5-6s（`held`＝この1本の変化）**。⚠️ **この1秒が、山の前の息止めである。**
  ⚠️ **風（3-5s）を切ってもよいが、その場合も布は動かない**——
  **風が来たことは埃でしか判らない**（記録の `motion.law`）。
- `mode: still` の判断 … **この1枚は手が1つ写っている。** これは事故ではなく判断である
  （記録の註——**主題は暖簾であり、動いたものが止まる**）。
- `forbidden_set` に `店の内側` が在る … `no shop interior`・`no door opening` がその節である
  （`PLAN.md` §0-f——**カメラは店の奥へ入らない**）。
- `attached` … `灯.identity`・`灯.states.支払いの前`・`灯.negatives`・`暖簾の店の前.base`・
  `暖簾の店の前.geography`・`暖簾の店の前.states.白`・`暖簾.appearance`・`暖簾.negative`
