# 画像仕様 — 一皿ができるまで 第1章 Clip 5/10（余白 / still / 4s）

⚠️ **この1枚の内容は「何も起きない」ことである。** 手は入らず、蓋は動かず、
麺棒も布も無い。**動いているのは光と粉塵だけ**——そして静止画では、
その2つも1枚に凍る。
⚠️ **だからこの1枚は、いちばん失敗しやすい。** モデルは空白を埋めたがる——
**余白は、指示しなければ空白にならない。**
⚠️ **この仕様は §1–20 を持たない**——**種類の話であって、モードの話ではない**
（`L18` がこの形を見る）。⚠️ **`mode: still` は「静止画で終わる」ではない。**
止まるのは**主題**であって、画面ではない——この1枚は**このショットの見せ場の1枚**である。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg05.yaml`
    ——gozen-niji の `series-constants.md`（シリーズ定数＋開示台帳）と同じ型である
- 投入する文: **下の `Prompt` はエンジンの出力であり、`chatgpt-image-2.5` へ投入する正典である**（決定B）
- ⚠️ **下の7欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`REF_FORMAT` と `REF_STYLE` が「どのカードの穴か」を名乗る。** `L22` がそれを読み、
  **名乗ったカードが実際にその穴を宣言しているか**を確かめる——**名乗りは宣言であって、一致ではない。**
- ⚠️ **⑦Negative の出力はここではなく下の `Negative` 節へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は節として保つ**——`L21` と開示の系列が節の集合として読む
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）
- 記録: `shots/hitosara-ch01-seg05.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: nothing happens under the lid
- `CHARACTERS`: no figure in frame, no hands
- `SUBJECT`: a wide ceramic bowl under a coarse linen lid, flour settled on the cloth
- `ACTION`: sitting utterly still while the window light crosses it
- `LOCATION`: a wooden bench in a one-room bakery, morning
- `LIGHT`: the window light crossing the linen, the bench otherwise quiet
- `ACCENT`: the warm gold light sliding across the linen

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of a wide ceramic bowl under a coarse linen lid with flour
settled on the cloth, sitting utterly still while the window light crosses it, at a wooden bench in
a one-room bakery in the morning, with the warm gold light sliding across the linen as the strongest
highlight. A scene board for the master staging of this one scene, in 16:9 — the camera and the
light fixed as the standard every cut of the scene must match. The window light crosses the linen;
the bench is otherwise quiet. Hyper-detailed layered light: the shaft travelling through the air
above the bowl, bloom around the window at the frame edge, flour dust suspended and individually
rendered as it falls rather than a flat wash. A saturated palette of magenta and gold on the lit
linen against deep cyan in the room behind, the bench faintly reflective and doubling the light.
Composition still and level, the bowl centred on the lower two thirds with the empty air above it
left open; the bowl small and subordinate to the light. Clean anime lineart on the cloth, held below
the light. No figure in frame, no hands. The lid has not moved and does not move — everything that
moves in this shot is the light and the dust. One focal point, generous negative space.

## Negative（英語）

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no hands, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no cross-section, no steam, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ `no steam` を、この1本だけに足してある

蒸気は「発酵している」という**説明**である。このショットは
**見えないものを、見えないまま見る**——説明を足せば、余白が埋まる。
⚠️ **`MUST NOT` の側に在るのは、足すことより消すことのほうが難しいからである。**
（記録の `forbidden_set` に `MIZU` が在るのも同じ理由である——水を見せれば、
「まだ何も起きていない」が「もう何かが起きている」に変わる。）

## ⚠️ この Negative は、開示の系列の一部である

`no oven interior`・`no visible flame`・`no glow through the door seam` の3節は、
**08 で開くまで全部の画像プロンプトに在り、08 で落ちる。**

## 記録との対応

- `unit` … 「ボウルに蓋がされている」→「蓋は一度も動かない。動かないことが、このショットの内容である」。
  **`before` と `after` が同じに見えることを、`L1` は鳴らさない**——
  **同じに見えることと、同じであることは別である。**
- `beats` … 0-2.5s 蓋は動かない／2.5-4s まだ動かない。**どちらも `density: held`。**
- `forbidden_set` に `KAMADO`・`PAN`・`MIZU` … **窯も、パンも、水も、まだ出ない。**
- `attached` … `KITCHEN.base`・`KITCHEN.geography`・`KONA.appearance`
