# 画像仕様 — 一皿ができるまで 第1章 Clip 1/10（情景 / motion / 3s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg01.yaml`
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
- 記録: `shots/hitosara-ch01-seg01.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the morning light picking out one shelf among the rows
- `CHARACTERS`: no figure in frame — a hand enters only at the very end
- `SUBJECT`: rows of unmarked paper flour sacks on a scarred wooden shelf
- `ACTION`: standing undisturbed while the morning light picks out a single shelf
- `LOCATION`: a small stone mill, one room, first light
- `LIGHT`: one low shaft from the window taking a single shelf, the rest of the rack left dim
- `ACCENT`: the warm gold of flour dust hanging in the shaft of light

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of rows of unmarked paper flour sacks standing undisturbed while the morning light picks out a single shelf, at a small stone mill, one room, at first light, with the warm gold of flour dust hanging in the shaft of light as the strongest highlight. A scene board for the master staging of this one scene, in 16:9 — the blocking, the camera and the light fixed as the standard every cut of the scene must match. One low shaft from the window takes a single shelf; the rest of the rack stays dim. Hyper-detailed layered light: the shaft travelling through the air from a window at the frame edge, anamorphic flare and bloom around the source, flour dust suspended and individually rendered rather than a flat wash. A saturated palette of magenta and gold in the lit half against deep cyan in the dim racks, the stone floor and the shelf edge faintly reflective and doubling the light. Composition wide and slightly low, the lit shelf across the upper third with the dark rows receding behind it; the shelf small and subordinate to the light. Clean anime lineart on the sacks, kept deliberately below the light. No figure in frame — a hand enters only at the very end of the shot. Low visual density: one focal point, generous negative space. No readable lettering anywhere, on the sacks or on the shelf.

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この Negative は、開示の系列の一部である

この作品の画像プロンプトの Negative は、**§18 と同じ系列を持つ**——`no oven interior`・
`no visible flame`・`no glow through the door seam` の3節は、**08 で開くまで全部に在り、
08 で落ちる。** 09 ではさらに `no cut loaf`・`no visible crumb`・`no cross-section` が落ちる
（割った断面が主題になる）。
⚠️ **いまこの系列を読む検査は無い**——`L10`・`L14` の相手は §18 であり、
画像プロンプトではない。**相手は引き渡しの層である**（段2）。だからここに
**人が読める形で系列を書いておく**——書かなければ、画像の側の開示は
誰にも検収されない。

## 記録との対応

- `unit` … 「粉屋の棚は、まだ誰にも選ばれていない」→「朝の光が、棚の一段だけを選び出す」
- `beats` … 0-2s 棚の全景／2-3s 光が一段だけを選ぶ。**光が動くことが、この1枚の内容である。**
  静止画であっても、`beats` は「どの瞬間を切るか」を決めるためにある。
- `place` / `time` … `MILL` / `朝`（`MILL.states.朝` が `reference_set` に在る）
- `attached` … `MILL.base`・`MILL.states.朝`・`MILL.geography`・`KONA.appearance`
