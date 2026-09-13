# 画像仕様 — 一皿ができるまで 第1章 Clip 3/10（図解 / composite / 5s）

⚠️ **このショットは `composite` である。** 画像1枚＋文字であり、
**文字は生成器が描かない**——`timeline` の `text_events` が編集で焼く。
だからこの1枚は**文字の入らない下地**である。
⚠️ **`text_channel` はこの仕様には現れない。** 行き先は `edit:timeline` であって
プロンプトではない（`FIELD_DESTINATION`）。**生成に渡してはならない**——
渡せば、モデルが数字を描き、綴りを間違え、二重になる。
⚠️ **この仕様は §1–20 を持たない**——**種類の話であって、モードの話ではない**
（`L18` がこの形を見る）。§18 は**動画の仕様**のものであり、`composite` でも無い。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine` の様式カード `luminous-anime`
- 焼く層: `timeline` の `text_events`（段3）。**文字はここではなく、そこで載る**
- 記録: `shots/hitosara-ch01-seg03.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: flour, water and salt measured out on a flour-dusted bench
- `ACTION`: lying still and separated, each in its own place
- `LOCATION`: a wooden kneading bench, straight down from above, morning
- `ACCENT`: the single fingertip of salt, catching the strongest highlight

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of flour, water and salt measured out on a
flour-dusted bench, lying still and separated each in its own place, on a wooden kneading
bench seen straight down from above in the morning, with the single fingertip of salt
catching the strongest highlight. Hyper-detailed layered light: one volumetric shaft
crossing the bench diagonally, anamorphic lens flare and bloom around the light source,
flour dust suspended and individually rendered. A saturated palette of magenta and gold
against deep cyan shadow, the damp bench faintly reflective. Overhead composition,
deliberately uncrowded: the three substances hold the lower two thirds, and **the upper
third and the lower right corner are left as clean empty bench** — a quiet surface with
nothing on it, for text to be placed over later. Nothing rests on those areas: no tool, no
cloth, no crumb, no shadow that would break the flatness. Everything subordinate to the
light, clean anime lineart, no hands and no figure in frame at all. Low visual density.
Absolutely no lettering, no numerals, no labels, no marks of any kind anywhere in the image.

## Negative（英語）

no readable text, no numerals, no digits, no measurement marks, no labels, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no hands, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ 文字を禁じる語を、この1本だけ厚くしてある

ほかの6本にも `no readable text` は在る。ここは**それに加えて**
`no numerals`・`no digits`・`no measurement marks`・`no labels` を置いている。
**理由は「図解だから」ではない**——この1枚は**文字が載る下地**であり、
モデルが数字を描けば、その上に本物の数字が載って**二重になる。**
⚠️ **禁じる語を足すことは、欠陥を消すことではない。** 消えるかどうかは
生成を見なければ分からない。**足したのは、失敗の形を先に名指しするためである。**

## ⚠️ この Negative は、開示の系列の一部である

`no oven interior`・`no visible flame`・`no glow through the door seam` の3節は、
**08 で開くまで全部の画像プロンプトに在り、08 で落ちる。**

## 記録との対応

- `unit` … 「分量は、どこにも書かれていない」→「分量と順序が、画面の上に一度だけ置かれる」
- `text_channel`（**画像へは行かない**）
  - `0.5-3.5` overlay `粉 250g　水 175g　塩 5g　酵母 1g`
  - `3.5-5.0` overlay `混ぜる　捏ねる　休ませる　焼く`
- `motion`（**画像へは行かない**）… 「主題（図）は止まり、光と粉塵だけが動く」。
  **`motion` は `mode` によらず必須である**（`L16`、決定 2026-09-13）
  ——ここでの運動は**編集の運動**でもある。
- `attached` … `KITCHEN.base`・`KITCHEN.geography`・`KONA.appearance`・`MIZU.appearance`・`SHIO.appearance`
