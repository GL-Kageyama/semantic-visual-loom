# 画像仕様 — キャラクターシート（参照・人物 / still）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
`§18` も `Negative Prompt` も `Style Motion` も無い——それらは**動画の仕様**の持ち物である。
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚はショットではない。** `shots/*.yaml` の `key_image:` から引かれない——
ゆえに **`L22` はこの文を読まない。** 読む層が無いことを、隠さずに書いておく。
**規律は人の側に置く。**

⚠️ **この1枚は「参照」であって「画」ではない。** 動画の5本に添付して、
**同じ人物であること**を運ぶために在る。**この1枚自体は、作品のどのフレームでもない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`
  - `format`: `character-sheet` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml`（`world.visual_language`・`constants.人物`）＋
    `ledger.yaml`（`characters.あかり`）＋ `specs/video/drama-pilot-s01.md` §3 ＋
    `specs/video/drama-pilot-s04.md` §3
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**（決定B／決定A）
- 記録: **この1枚には記録（`shots/*.yaml`）が無い。** 出来た画像の置き場と、
  `identity` へ書く語だけが下の「できたあとに」に在る。

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `character-sheet` —— 4つの穴（`SUBJECT`／`N`／`EXPRESSIONS`／`DETAILS`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`SUBJECT` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
4＋4＝8 ではなく、**和は7**である。

- `SUBJECT`: a girl seen only from behind — white shirt, dark trousers, a small paper lantern in her right hand
- `N`: four views in one row — straight back, back three-quarter left, back three-quarter right, and a closer back from the waist up
- `EXPRESSIONS`: no expression heads — this work never shows her face; the row beneath the figures holds the hands and the lantern instead
- `DETAILS`: the shirt's collar seam and rolled cuff, the lantern's paper body and wire handle where the hand takes it, the trouser hem over a worn shoe
- `ACTION`: standing still, arms relaxed and clear of the silhouette, the lantern held down at her right side
- `LOCATION`: a plain white ground, no scene
- `ACCENT`: the lantern's pale paper, the one warm note against the white

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A character model sheet of a girl seen only from behind — white shirt, dark trousers, a small paper lantern in her right hand — on a plain white ground, four views in one row: straight back, back three-quarter left, back three-quarter right, and a closer back from the waist up, all at the same character height and the same eye line on a shared horizontal guide, standing with her arms relaxed and clear of the silhouette, the lantern held down at her right side. Below the row, no expression heads: a single hand taking the lantern's wire handle, and the same hand lifting it to eye level and stopping. Beside the figures, enlarged detail insets of the shirt's collar seam and rolled cuff, the lantern's paper body and wire handle, and the trouser hem over a worn shoe. Flat even light, no cast shadow, no background scene. A production reference readable as a specification, not a finished illustration. Her hair is short and dark, cut to the nape; the shirt is plain white cotton with a soft collar and a rolled cuff; the trousers are dark, straight and untapered; the shoes are worn and dark. Her build is slim, her height ordinary for her age. The clothing is contemporary and nothing in it dates her. Clean anime lineart with flat cel shading and no rendered skin texture; the ground is pure white and the figures are fully lit with no shadow thrown. The lantern's paper is pale and translucent, the one warm note against the white.

no human face, no head turned toward the camera, no front view, no profile view, no expression heads, no second person, no cast shadow, no background scene, no scenery, no dramatic lighting, no dramatic pose, no lettering of any kind, no callout lines, no annotations, no watermark, no on-screen subtitles, no photographic faces, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no lit lantern, no flame, no ember

## ⚠️ なぜ正面と横顔が無いのか

**この作品は、彼女の顔を一度も映さない。** `bible.yaml` の `constants.人物` がそう決め、
`negative_base` が `no close-up of a face` を持ち、`s01` の §3 が
「her face is never shown close」と書き、`s04` の §3 が「the face is not in this shot」と書く。
**ゆえに正面のカウンター（顔）は、この作品では一度も使われない。**

⚠️ **そして、顔を参照に入れることは中立ではない。** `character-sheet` のカード自身が言う——
**顔を指定しなければ、様式の平均の顔が入る。** それは「指定しない」ではなく、
**「その顔を選ぶ」である。** 参照に顔が在れば、生成器にとって**それを写す誘因**になる。

だからこのシートは、**カードの標準的な回転図（front／three-quarter／side／back）から、
意図して外れる**——**back と、back の three-quarter と、back の close だけ**。
`hitosara` の `hitosara-baker-character-sheet`（「手と前掛け。顔は映さない」）と同じ判断である。

⚠️ **代わりに何が仕様を担うか。** **同じ高さ・同じアイラインの水平ガイド**と、
**手・提灯・袖口・裾の insets** である。**カードは「情報が mood に勝つ」と言う**——
その情報を、顔ではなく**衣装と手**が負う。⚠️ **文字は持たない**（`bible` の
「読み取れる文字は無い」）。**callout は書かず、insets が仕様になる。**

## ⚠️ できたあとに、何が変わるか

**この1枚が出来るまで、`characters.あかり.identity` は「未作成」のままである。**
**無いファイルを指す語は、嘘である。**

1. 画像を `projects/drama-pilot/media/` に置く（**このディレクトリはまだ無い**）。
2. `ledger.yaml` の `characters.あかり.identity` を、そのファイルと名前へ書き換える。
3. 動画の5本の §6 に `REF_CHARACTER:` の一行を足す（`§19` の `References:` も同じ語を持つ）。
   ⚠️ **`s03` は彼女が枠に居ない**（カメラが谷へ降りる）——**そこに添付する理由は無い。**
   ⚠️ **`s05` は5秒で切れ、彼女はもう居ない**——**添付するなら、彼女が居る5秒のためである。**
4. ⚠️ **`s04` の §6 を変えるなら、`ab/old-drama-pilot-s04.md` にも同じ変更を入れる**——
   さもなければ [`ab/README.md`](../../ab/README.md) の
   「`## DIRECTION` 以外1バイトも違わない」が嘘になる。
