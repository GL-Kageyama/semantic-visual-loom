# 画像仕様 — 『白地図』第1章「暖簾」 S09（反応 / motion / 7s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⚠️ **この1本の変化は「音が戻ること」である。** ゆえにこの1枚が切るのは
**布が鳴っている側**——**鳴る前を切れば、この1枚は S06 と見分けがつかない。**
⚠️ **くぐる者は来ない。** 草稿 L17「揺れる朱の下を、**誰かがくぐるはずだった**」——
**「はずだった」を画にする方法は、揺れの下を空のまま置くことである。**
⚠️ **この1本の縁は、草稿 L17 の一行が決めている**——
「湯気の匂いも、店の奥の暖かさも、**まだ白のままだった**」。**湯気を出さない。**

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg09.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg09.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: the cloth sounding once in the wind, and the paving beneath the swing left empty
- `CHARACTERS`: 灯 standing still at the edge of the frame, seen from behind, face not drawn — not moving
- `SUBJECT`: the vermilion noren lifting once, and the empty paving under it
- `ACTION`: the cloth swinging once, its lower edge drawn inward, the street under it staying empty
- `LOCATION`: the front of the noren shop, the cloth and the ground below it in one frame
- `LIGHT`: morning light lying flat on the white, even and without direction
- `ACCENT`: the empty paving under the lifted hem — the place where someone would have passed
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of the vermilion noren lifting once in the wind, its lower edge drawn inward, with the paving under it left empty — 灯 standing still at the edge of the frame, seen from behind, not moving — at the front of the noren shop with the cloth and the ground below it in one frame, under morning light lying flat on the white, with the empty paving under the lifted hem holding the frame. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. The cloth is the faded vermilion of a cloth through a second winter, paler on the hems that faced the sun and deeper on the hems that stayed in shade, its lower hems indigo, and the pigment still wet enough to sit on the paper with body and an uneven surface. The wind is shown by the cloth alone, and the cloth has moved once: its hems are still where the one movement left them. 灯 is drawn from behind — back, outline, and one hand — and the face is not drawn at all. Flat and paper-based, no directional light, no spatial illusion. Nobody passes under the cloth and nothing crosses it; no kettle and no stove are in the frame; the shop's interior is not in the frame.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no flat vermilion without pigment body, no dry even vermilion paint, no person passing under the noren, no passer-by, no second person, no visible person among the white shapes, no kettle, no teakettle, no visible stove or fire, no steam, no smoke, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light

## ⚠️ この Negative は、S08 で動いたあとの側である

`no flat vermilion without pigment body` と `no dry even vermilion paint` が入り、
`no fully-painted flat vermilion cloth` が落ちている（`ledger.disclosure` の `negative: changed`）。
⚠️ **この1枚は暖簾が朱である**——ゆえに**乾いて均した朱を禁じる側に居る。**
⚠️ **画像の系列を読む検査は無い**（`L10` の相手は §18 である）——人が読める形でここに置く。

## 記録との対応

- `unit` … 「鳴っていない」→「ぱさりと鳴った」。**この1枚が切るのは後者である。**
- `beats` … **切る瞬間は 2-3s（`dense`）**——**この作品でいちばん短い出来事**である1秒を切る。
  ⚠️ **3-5s（揺れの下が空である側）を切るのも同じ1本の画である**——
  **どちらを採るにせよ、「くぐる者が居ない」ことが画の縁である。**
- `forbidden_set` に `くぐる者`・`薬缶`・`湯気` が在る … `no person passing under the noren`・
  `no kettle`・`no steam` がその節である。⚠️ **薬缶は音と、覚えられている形だけである**（台帳）。
- `attached` … `灯.identity`・`灯.states.支払いの前`・`灯.negatives`・`暖簾の店の前.base`・
  `暖簾の店の前.geography`・`暖簾の店の前.states.朱が戻った`・`暖簾.appearance`・`暖簾.negative`・
  `薬缶.appearance`・`薬缶.negative`
  ⚠️ **`薬缶.appearance` は「音である」**——**この1枚に物として写さない**（`no kettle`）。
