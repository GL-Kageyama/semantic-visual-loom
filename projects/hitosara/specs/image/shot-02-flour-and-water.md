# 画像仕様 — 一皿ができるまで 第1章 Clip 2/10（質感 / motion / 2s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である
——**種類の話であって、モードの話ではない**（`L18` がこの形を見る）。
⚠️ **この1枚は「拡大」である。** ショットの単位は変化であって、枚数の単位ではない——
同じ台の上で、**見る尺度だけが変わる。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg02.yaml`
    ——gozen-niji の `series-constants.md`（シリーズ定数＋開示台帳）と同じ型である
- 投入する文: **下の節の1段落目が `Prompt` であり、エンジンの出力であって、`chatgpt-image-2.5` へ
  投入する正典である**（決定B）。**2段落目が `Negative` である**（決定A）
- ⚠️ **下の7欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`REF_FORMAT` と `REF_STYLE` が「どのカードの穴か」を名乗る。** `L22` がそれを読み、
  **名乗ったカードが実際にその穴を宣言しているか**を確かめる——**名乗りは宣言であって、一致ではない。**
- ⚠️ **⑦Negative の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` と開示の系列が
  **段落の集合**として読む。
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**——
  **見出しが本文の間にあると、選択がそれを巻き込む。** 空行1つが、そのまま `Negative` を
  繋ぐ空行である。**繋がった文字列の写しは置かない**（写しは食い違う）。
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）
- 記録: `shots/hitosara-ch01-seg02.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the water spreading into a film until the boundary between flour and water is gone
- `CHARACTERS`: no figure in frame, no hands
- `SUBJECT`: a shallow well of flour with water just touching it
- `ACTION`: the water spreading as a film across the grains until the boundary between them disappears
- `LOCATION`: a wooden kneading bench, extreme close view, morning
- `LIGHT`: morning light raking across the wet crest, the film catching it
- `ACCENT`: the wet line where the water meets the flour, catching the strongest highlight

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of a shallow well of flour with water just touching it, the water spreading as a film across the grains until the boundary between them disappears, at a wooden kneading bench seen extremely close in the morning, with the wet line where the water meets the flour catching the strongest highlight. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Morning light rakes across the wet crest and the film catches it. Hyper-detailed layered light: the shaft travelling low through the air above the bench, bloom around the source at the frame edge, flour dust suspended and individually rendered where the light catches it rather than a flat wash. A saturated palette of magenta and gold in the lit grain against deep cyan in the shadowed hollow, the wet bench faintly reflective and doubling the light. Composition low and close, the crest of the flour across the lower third and the shallow hollow filling the frame; the grains small and subordinate to the light. Clean anime lineart, held below the light. No figure in frame, no hands. Low visual density: one focal point, generous negative space.

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この Negative は、開示の系列の一部である

`no oven interior`・`no visible flame`・`no glow through the door seam` の3節は、
**08 で開くまで全部の画像プロンプトに在り、08 で落ちる。**
⚠️ **いまこの系列を読む検査は無い**——`L10`・`L14` の相手は §18 である。
**相手は引き渡しの層である**（段2）。だからここに人が読める形で書いておく。

## 記録との対応

- `unit` … 「粉は粉であり、水は水である」→「粉の一粒ごとに水の膜がかかり、境が消える」
- `beats` … 0-1s 頂点を浅い角度から／1-2s 水が触れ、膜が広がる。
  **この1枚が切る瞬間は 1-2s の側である**——`density: dense` の側を切る。
- `forbidden_set` に `SHIO` が在る … **塩はまだ画面に出ない。** 出るのは 03 である。
- `attached` … `KITCHEN.base`・`KITCHEN.geography`・`KONA.appearance`・`MIZU.appearance`・`BAKER.sheet`
