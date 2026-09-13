# 画像仕様 — 一皿ができるまで 第1章 Clip 9/10（様式美 / motion / 2.5s）

⚠️ **開示の第2点である。ここでパンが割れる。** この1枚から
`no cut loaf`・`no visible crumb`・`no cross-section` の**3節が落ちる**——
**割った断面が、初めて画面に出る。**
⚠️ **この落ちる3節は、画像の経路と動画の経路の両方で落ちる。** 動画の §18 は
`L10` が台帳と突き合わせて検算する（台帳が `negative: changed` を宣言している）。
**この画像プロンプトの側を読む検査は、まだ無い**——相手は引き渡しの層である（段2）。
⚠️ **この仕様は §1–20 を持たない**——**種類の話であって、モードの話ではない**
（`L18` がこの形を見る）。**`mode: motion` でも画像の仕様は節を持たない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg09.yaml`
    ——gozen-niji の `series-constants.md`（シリーズ定数＋開示台帳）と同じ型である
- 投入する文: **下の `Prompt` はエンジンの出力であり、`chatgpt-image-2.5` へ投入する正典である**（決定B）
- ⚠️ **下の欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`scene-board` が要求する穴は、下の4つでは足りない**（`SCENE`／`CHARACTERS`／`LIGHT` が要る。
  2層の和で7欄になる——`ACTION`・`LOCATION` は両層に同名で在り、**同じ値が両方の穴に入る**）
- ⚠️ **⑦Negative の出力はここではなく下の `Negative` 節へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は節として保つ**——`L21` と開示の系列が節の集合として読む
- 記録: `shots/hitosara-ch01-seg09.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: a baked loaf torn open, its crumb exposed
- `ACTION`: the wall of air pockets taking the light from inside
- `LOCATION`: a wooden bench in a one-room bakery, morning
- `ACCENT`: the warm gold light inside the crumb

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of a baked loaf torn open with its crumb exposed, the
wall of air pockets taking the light from inside, on a wooden bench in a one-room bakery in
the morning, with the warm gold light inside the crumb as the strongest highlight. **This is
the shot the whole film withholds until now: the interior is the subject.** Hyper-detailed
layered light: one volumetric shaft from the window, anamorphic lens flare and bloom around
the source, flour dust suspended — and, inside the torn bread, the glossy walls of the
pockets catching and returning that light, rendered one by one rather than as texture. A
saturated palette of magenta and gold against deep cyan shadow, the crust a deep lacquered
gold with the sheen of a real bake. Composition close and low, the torn face of the loaf
filling the frame and the crust a dark rim around it, the light source inside the frame at
the edge, clean anime lineart kept subordinate to the light. No hands in frame. No oven in
frame. Low visual density: the crumb, and the light inside it. No readable lettering anywhere.

## Negative（英語）

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no hands, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この Negative は、前の6本と**同じ系列の続き**である

- `no oven interior`・`no visible flame`・`no glow through the door seam` … **08 で落ちた。** ここにも無い。
- `no cut loaf`・`no visible crumb`・`no cross-section` … **この1本で落ちる。**
⚠️ **落ちることは、増えることより重い。** 以後どのショットでも戻らない——
**禁止が消えることは、モデルがそれを描いてよいことである**（`L14` の註と同じ理屈）。
⚠️ **`no oven interior` の3節がここに無いのは、窯が写るからではない。**
`forbidden_set` が `KAMADO` を禁じており、**窯はそもそも画面に無い。**
無いのは**「禁じる必要が無くなったから」**である——**この2つは別のことである。**

## 記録との対応

- `unit` … 「パンの外は金である」→「内の気泡が光を受ける」
- `beats` … 0-1.5s 外は金、まだ割れていない／1.5-2.5s 割れる。
  **この1枚が切るのは 1.5-2.5s の側である。**
- `disclosure_state` … `KAMADO.interior: opened` / `PAN.interior: opened`
- `forbidden_set` … `KAMADO`・`KONA`
- `attached` … `KITCHEN.base`・`KITCHEN.geography`・`PAN.appearance`
