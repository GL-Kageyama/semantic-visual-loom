# 画像仕様 — 一皿ができるまで 第1章 Clip 1/10（情景 / motion / 3s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像は動画の最初のコマである。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine` の様式カード `luminous-anime`
- 記録: `shots/hitosara-ch01-seg01.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: rows of unmarked paper flour sacks on a scarred wooden shelf
- `ACTION`: standing undisturbed while the morning light picks out a single shelf
- `LOCATION`: a small stone mill, one room, first light
- `ACCENT`: the warm gold of flour dust hanging in the shaft of light

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of rows of unmarked paper flour sacks on a scarred
wooden shelf, standing undisturbed while the morning light picks out a single shelf, in a
small stone mill at first light, with the warm gold of flour dust hanging in the shaft of
light catching the strongest highlight. Hyper-detailed layered light: volumetric shafts
travelling through the air from a window at the frame edge, anamorphic lens flare and bloom
around the source, fine flour dust suspended and individually rendered rather than a flat
wash. A saturated palette of magenta and gold against deep cyan shadow, the stone floor
worn and faintly reflective where the light reaches it. Low and close composition, the shelf
across the upper third, the light source inside the frame, everything small and subordinate
to the light, clean anime lineart kept deliberately below the light. A pale, dust-muted
morning; the palette is saturated, not muted. Low visual density: one focal point and
generous negative space. No readable lettering anywhere on the sacks or the walls.

## Negative（英語）

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
