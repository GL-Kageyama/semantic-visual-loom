# 画像仕様 — 一皿ができるまで 第1章 Clip 2/10（質感 / motion / 2s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である
——**種類の話であって、モードの話ではない**（`L18` がこの形を見る）。
⚠️ **この1枚は「拡大」である。** ショットの単位は変化であって、枚数の単位ではない——
同じ台の上で、**見る尺度だけが変わる。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine` の様式カード `luminous-anime`
- 記録: `shots/hitosara-ch01-seg02.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: a shallow well of flour with water just touching it
- `ACTION`: the water spreading as a film across the grains until the boundary between them disappears
- `LOCATION`: a wooden kneading bench, extreme close view, morning
- `ACCENT`: the wet line where the water meets the flour, catching the strongest highlight

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of a shallow well of flour with water just touching
it, the water spreading as a film across the grains until the boundary between them
disappears, on a wooden kneading bench in extreme close view in the morning, with the wet
line where water meets flour catching the strongest highlight. Hyper-detailed layered light:
volumetric shafts travelling through the air, anamorphic lens flare and bloom around the
light source, individual grains of flour rendered one by one and individually lit — not a
flat white mass. A saturated palette of magenta and gold against deep cyan shadow, the wet
stone and the damp bench faintly reflective and doubling the light. Extreme close, shallow
focus, the light source inside the frame at its edge, everything subordinate to the light,
clean anime lineart. The hands of the baker enter only at the frame edge as a pouring hand —
no face, no body, no ring, no watch. Low visual density: one focal point. No readable
lettering anywhere.

## Negative（英語）

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
