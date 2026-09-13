# 画像仕様 — 一皿ができるまで 第1章 Clip 5/10（余白 / still / 4s）

⚠️ **この1枚の内容は「何も起きない」ことである。** 手は入らず、蓋は動かず、
麺棒も布も無い。**動いているのは光と粉塵だけ**——そして静止画では、
その2つも1枚に凍る。
⚠️ **だからこの1枚は、いちばん失敗しやすい。** モデルは空白を埋めたがる——
**余白は、指示しなければ空白にならない。**
⚠️ **この仕様は §1–20 を持たない**——**種類の話であって、モードの話ではない**
（`L18` がこの形を見る）。⚠️ **`mode: still` は「静止画で終わる」ではない。**
止まるのは**主題**であって、画面ではない——この1枚は**動画の最初のコマ**である。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg05.yaml`
    ——gozen-niji の `series-constants.md`（シリーズ定数＋開示台帳）と同じ型である
- 投入する文: **下の `Prompt` はエンジンの出力であり、`chatgpt-image-2.5` へ投入する正典である**（決定B）
- ⚠️ **下の欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`scene-board` が要求する穴は、下の4つでは足りない**（`SCENE`／`CHARACTERS`／`LIGHT` が要る。
  2層の和で7欄になる——`ACTION`・`LOCATION` は両層に同名で在り、**同じ値が両方の穴に入る**）
- ⚠️ **⑦Negative の出力はここではなく下の `Negative` 節へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は節として保つ**——`L21` と開示の系列が節の集合として読む
- 記録: `shots/hitosara-ch01-seg05.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: a wide ceramic bowl under a coarse linen lid, flour settled on the cloth
- `ACTION`: sitting utterly still while the window light crosses it
- `LOCATION`: a wooden bench in a one-room bakery, morning
- `ACCENT`: the warm gold light sliding across the linen

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of a wide ceramic bowl under a coarse linen lid with
flour settled on the cloth, sitting utterly still while the window light crosses it, on a
wooden bench in a one-room bakery in the morning, with the warm gold of the morning light
sliding across the linen as the strongest highlight. Hyper-detailed layered light:
volumetric shafts travelling through the air from a window at the frame edge, anamorphic
lens flare and bloom around the light source, fine flour dust suspended in the beam and
individually rendered. A saturated palette of magenta and gold against deep cyan shadow, the
damp bench and the stone floor faintly reflective where the light reaches them. Composition
low and close to the bowl, the bowl slightly off center with the light source at the frame
edge, everything subordinate to the light, clean anime lineart. The scene is emphatically
empty — **only the bowl, the lid, the bench and the light are present. No hand, no tool, no
cloth, no second object, no crumb, no steam.** Low visual density; generous negative space is
the subject. No readable lettering anywhere.

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
