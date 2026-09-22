# 画像仕様 — 『白地図』第1章「暖簾」 S11（離脱 / motion / 9s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⚠️ **この1本の変化は「そこに居なくなること」である。** ゆえにこの1枚が切るのは
**灯がもう歩きだしている側**——**触れる前を切れば、この1枚は S09 の1枚になる。**
⚠️ **この1本は、この作品で唯一「人が画から出ていく」1本である**（S02 は人が画に入ってくる1本である）。
⚠️ **最後の画は、朱と、白と、影である。**

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg11.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg11.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: the vermilion left behind on the cloth, and 灯's shadow the last thing in the frame that still has colour
- `CHARACTERS`: 灯 seen from behind, walking away, face not drawn — the only figure, with the fingertips gone slightly white
- `SUBJECT`: 灯 from behind, the hand just off the cloth, and the long thin shadow laid on the white
- `ACTION`: letting go of a cloth that does not follow, and walking off at the pace of twenty years
- `LOCATION`: the front of the noren shop on the street, the vermilion cloth behind and the white ahead
- `LIGHT`: morning light lying flat on the white, even and without direction
- `ACCENT`: the shadow — still holding colour while the fingertips have gone white
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of 灯 seen from behind walking away, the hand just off the vermilion noren, and the long thin shadow laid on the white — letting go of a cloth that does not follow and walking off at the pace of twenty years, at the front of the noren shop on the street with the vermilion cloth behind and the white ahead, with the shadow — still holding colour — the last thing in the frame. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. The cloth behind stays where it is and does not follow the hand: it is not pulled, not stretched and not lifted, and its colour does not move again — the faded vermilion of a cloth through a second winter, paler on the hems that faced the sun, deeper on the hems that stayed in shade, its lower hems indigo, the pigment still sitting on the paper with body. The fingertips have gone a little white, and they whiten from the edge as paper taking the hand back, not as a pale gradient along the fingers. The shadow keeps its colour and holds a hard edge, laid down like a stroke of pigment. 灯 is drawn from behind — back, outline, and the hand — and the face is not drawn at all. Flat and paper-based, no directional light, no spatial illusion. Nobody is named, nothing is written, and no name is called anywhere.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no flat vermilion without pigment body, no dry even vermilion paint, no cloth following the hand, no stretched or pulled cloth, no movement in the vermilion cloth, no second person, no visible person among the white shapes, no visible face on the figure, no pale gradient on the hand, no blurred shadow, no soft photographic shadow, no called or written name, no lettering of a name, no numerals, no numbers, no cat in frame, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no directional light

## ⚠️ この Negative は、S08 で動いたあとの側である

`no flat vermilion without pigment body` と `no dry even vermilion paint` が入り、
`no fully-painted flat vermilion cloth` が落ちている（`ledger.disclosure`）。
⚠️ **S08 の12秒が保った濡れを、この1枚の指が確かめる**——ゆえにこの1枚も、
**乾いて均した朱を禁じる側に居る**（草稿 L23「朱は**まだ乾いていない**」）。

## 記録との対応

- `unit` … 「手はまだ朱に触れていない」→「灯はもうそこにいない」。
  **この1枚が切るのは後者である**——⚠️ **この1本の変化は「居なくなること」である。**
- `beats` … **切る瞬間は 7-9s（`sparse`）**。⚠️ **この2秒に、声を1つも置かない。名前を呼ばない。**
- ⛔ **この開示点を画は負っていない。** `灯.渡した声: 名を失った` を負っているのは
  **この映画の側の保留**である——**この作品は台詞もナレーションも持たず**（`PLAN.md` §0-e）、
  **渡した声の名を、どこでも一度も呼ばない。** ⚠️ **これは判断であって、確かめられたことではない。**
  **画が負っていない開示点が1つある、と記録しておく**（穴のまま置く）。
- `forbidden_set` に `呼ばれる名`・`立ち止まる灯` が在る … `no called or written name`・
  **振り返らない**がその節である（草稿 L21「灯はそれが、**いやではなかった。**」）。
- `attached` … `灯.identity`・`灯.states.支払いのあと`・`灯.negatives`・`暖簾の店の前.base`・
  `暖簾の店の前.geography`・`暖簾の店の前.states.朱が戻った`・`暖簾.appearance`・`暖簾.negative`・
  `白い形.appearance`・`白い形.negative`
