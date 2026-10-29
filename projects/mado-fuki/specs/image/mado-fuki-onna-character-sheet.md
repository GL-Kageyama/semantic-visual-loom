# 画像仕様 — キャラクターシート（参照・人物 / still）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
`§18` も `Negative Prompt` も `Style Motion` も無い——それらは**動画の仕様**の持ち物である。
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚はショットではない。** `shots/*.yaml` の `key_image:` から引かれない——
ゆえに **`L22` はこの文を読まない。** 読む層が無いことを、隠さずに書いておく。
**規律は人の側に置く。**

⚠️ **この1枚は「参照」であって「画」ではない。** 動画の4本に添付して、
**同じ女であること**を運ぶために在る。**この1枚自体は、作品のどのフレームでもない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`
  - `format`: `character-sheet` ／ `style`: `cinematic-still`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml`（`world.visual_language`・`constants.窓`）＋
    `ledger.yaml`（`characters.女`）＋ `specs/video/mado-fuki-s01.md` §3 ＋
    `specs/video/mado-fuki-s02.md` §3
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: **この1枚には記録（`shots/*.yaml`）が無い。** 出来た画像の置き場と、
  `identity` へ書く語だけが下の「できたあとに」に在る。

## 主題（英語・2枚のカードの穴・8欄）

- `REF_FORMAT`: `character-sheet` —— 4つの穴（`SUBJECT`／`N`／`EXPRESSIONS`／`DETAILS`）
- `REF_STYLE`: `cinematic-still` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`GRADE`）

⚠️ **`SUBJECT` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
4＋5＝9 ではなく、**和は8**である。

- `SUBJECT`: a woman seen only from behind — dark sweater with the sleeves pushed up to the forearm, a grey cloth in her right hand, short dark hair cut to the nape, slim build, ordinary height
- `N`: four views in one row — straight back, back three-quarter left, back three-quarter right, and a closer back from the waist up
- `EXPRESSIONS`: no expression heads — this work never shows her face; the row beneath the figures holds the right hand and the cloth instead
- `DETAILS`: the cloth's wrung edge and the way the right hand takes it, the sleeve rolled to the forearm, the sweater's shoulder seam, the hem where it falls over the trousers
- `ACTION`: standing still, arms relaxed and clear of the silhouette, the cloth held down at her right side
- `LOCATION`: a plain white ground, no scene
- `LIGHT`: flat even light, no cast shadow
- `GRADE`: neutral — **no colour grade**（この作品の色はショットごとに動く。シートは色を運ばない）

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A character model sheet of a woman seen only from behind — dark sweater with the sleeves pushed up to the forearm, a grey cloth in her right hand, short dark hair cut to the nape — on a plain white ground, four views in one row: straight back, back three-quarter left, back three-quarter right, and a closer back from the waist up, all at the same character height and the same eye line on a shared horizontal guide, standing with her arms relaxed and clear of the silhouette, the cloth held down at her right side. Below the row, no expression heads: the right hand taking the cloth's edge, and the same hand pressing the cloth flat against an unseen pane and stopping. Beside the figures, enlarged detail insets of the cloth's wrung edge, the sleeve rolled to the forearm, the sweater's shoulder seam, and the hem over the trousers. Flat even light, no cast shadow, no background scene. A production reference readable as a specification, not a finished illustration. Her build is slim and her height ordinary; the sweater is dark, plain knit, with a soft shoulder and no pattern; the trousers are dark and straight; the shoes are flat and worn. The clothing is contemporary and nothing in it dates her, and she wears no jewellery. A real person photographed under flat studio light — no anamorphic bokeh, no shallow-focus fall-off and no colour grade, because this sheet is a reference and not a frame of the film.

no human face, no head turned toward the camera, no front view, no profile view, no expression heads, no second person, no cast shadow, no background scene, no window, no sea, no room, no dramatic lighting, no dramatic pose, no anamorphic bokeh, no colour grade, no teal-and-orange grade, no props beyond the cloth, no mirror, no reflection of a face, no lettering of any kind, no callout lines, no annotations, no watermark, no on-screen subtitles, no CGI, no illustration, no painterly brush strokes

## ⚠️ なぜ正面と横顔が無いのか

**この作品は、彼女の顔を一度も映さない。** `bible.yaml` の規則がそう決め
（「彼女の顔は主役にならない。手と背中が主役である」）、`negative_base` が
`no second person` を持ち、4本の §16 がすべて `No close-up of the face` を書き、
`s02` は手と前腕しか枠に持たない。**ゆえに正面のカウンター（顔）は、この作品では一度も使われない。**

⚠️ **そして、顔を参照に入れることは中立ではない。** `character-sheet` のカード自身が言う——
**顔を指定しなければ、様式の平均の顔が入る。** それは「指定しない」ではなく、
**「その顔を選ぶ」である。** 参照に顔が在れば、生成器にとって**それを写す誘因**になる。

だからこのシートは、**カードの標準的な回転図（front／three-quarter／side／back）から、
意図して外れる**——**back と、back の three-quarter と、back の close だけ**。
`drama-pilot` の `drama-pilot-akari-character-sheet` と同じ判断である。

⚠️ **代わりに何が仕様を担うか。** **同じ高さ・同じアイラインの水平ガイド**と、
**手・布・袖・肩の縫い目・裾の insets** である。**カードは「情報が mood に勝つ」と言う**——
その情報を、顔ではなく**手と衣装**が負う。⚠️ **文字は持たない**（`bible` の
「読み取れる文字は無い」）。**callout は書かず、insets が仕様になる。**

## ⚠️ カード2枚が食い違う1点と、どちらを採るか

`cinematic-still` の `## Negative` は **`no flat TV lighting`** を持ち、`## Fidelity anchors` は
**アナモルフィック・浅い被写界深度・色のグレーディング**を名指す。`character-sheet` の側は
**平らな光・影なし・白い地**を要求する。**そのまま重ねれば、2枚のカードが互いを打ち消す。**

**採るのは `character-sheet` の側である。** そのカードが自分で
*The sheet is read as a specification, so information beats mood everywhere they conflict* と
書いている——**この1枚は作品のフレームではない**からである。
ゆえに上の文は、`no flat TV lighting` を**落とし**、`no anamorphic bokeh` と
`no colour grade` を**足している**。⚠️ **これは書き漏れではない——選んだことである。**
⚠️ **色をシートに載せない理由。** この作品の色は `s01` の冷たい青緑から `s04` の金まで動く。
**動くものを参照に固定すれば、4本ともその色に引かれる。**

## ⚠️ できたあとに、何が変わるか

**この1枚が出来るまで、`characters.女.identity` は「未作成」のままである。**
**無いファイルを指す語は、嘘である。**

1. 画像を `projects/mado-fuki/media/` に置く（**このディレクトリはまだ無い**）。
2. `ledger.yaml` の `characters.女.identity` を、そのファイルと名前へ書き換える。
3. 動画の4本の §6 に `REF_CHARACTER:` の一行を足す（§19 の `References:` も同じ語を持つ）。
   ⚠️ **`s02` にも添付する**——あの1本の枠に在るのは彼女の手と前腕であり、
   **手が彼女のものであることを運ぶのはこの1枚だけである。**
   ⚠️ **`s02` は `body_parts: {hand: 1}` を宣言している**——ゆえに §6 の行は
   `REF_CHARACTER` だけでなく、**手が1本であることの出所**でもある。
