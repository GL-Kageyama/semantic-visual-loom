# 画像仕様 — 一皿ができるまで 第1章 Clip 7/10（転換 / motion / 3s）

⚠️ **このショットは時刻を跨ぐ。** それでも `time` は単数（`明け方`）である——
**跨ぎは `unit` の対が持つ**（ショットは一時刻である。CLAUDE.md 固定方針）。
⚠️ **この1枚は「扉の前」である。** 窯の**外側**だけが写る——
`KAMADO.appearance` は添付され、**`KAMADO.interior` は `sealed` のまま**である。
**同じ物の、外と中を分けることは、この台帳の仕事である。**
⚠️ **文字は編集で載る**（`一晩`）。生成器に描かせない——`text_channel` の行き先は
`edit:timeline` である。
⚠️ **この仕様は §1–20 を持たない**——**種類の話であって、モードの話ではない**
（`L18` がこの形を見る）。**この1枚は色の勾配であり、動くのは光である。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine` の様式カード `luminous-anime`
- 焼く層: `timeline` の `text_events`（段3）
- 記録: `shots/hitosara-ch01-seg07.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: a closed iron oven door in a far wall, with a pair of hands stopped in front of it
- `ACTION`: waiting while the window behind goes from blue to gold
- `LOCATION`: a one-room bakery, before dawn
- `ACCENT`: the first gold of the coming morning across the stone floor

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of a closed iron oven door set into a far wall, with a
pair of working hands stopped in front of it, waiting while the window behind goes from blue
to gold, in a one-room bakery before dawn, with the first gold of the coming morning raking
across the stone floor as the strongest highlight. Hyper-detailed layered light: one
volumetric shaft from the window travelling across the room and reaching the oven wall,
anamorphic lens flare and bloom around the window, fine flour dust suspended in the beam.
The palette is the hinge of the shot — **deep blue still in the upper half, warm magenta and
gold already climbing the lower half**, the shift visible as a single gradient across the
stone floor. The stone floor and the iron door faintly reflective. Composition at the height
of the door, the door on the same side of frame as in every other shot, the light source
inside the frame at the window. The hands follow the character sheet — hands and coarse linen
apron only, **no face, no body, no ring, no watch**. Everything subordinate to the light,
clean anime lineart. Low visual density; the left of the frame is left quiet and uncrowded
for text to be placed over later.

## Negative（英語）

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no cross-section, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この1枚が、開示の境界のいちばん際どいところである

**扉は写ってよい。扉の隙間から漏れる光は、写ってはならない。**
この2つは同じ物の裏表であり、**言葉にしなければ同じ絵になる**——
だから §16 に相当する `MUST NOT` が、ここでは**この註である**：
`no glow through the door seam` は、この1枚でいちばん壊れやすい。
⚠️ **`no oven interior` と `no visible flame` は、この1枚では「まだ」である。**
08 で落ちる。**落ちる位置を台帳が宣言している**（`ledger.disclosure`）。

## 記録との対応

- `unit` … 「夜のまま、窯の扉は閉じている」→「明け方になり、扉の前の手が火を入れる」
- `motion`（**画像へは行かない**）… 「カメラは据えたまま、光だけが動く」。
  **`motion` は `mode` によらず必須である**（`L16`、決定 2026-09-13）
  ——ここでの運動は**光**であり、この1枚では**勾配**として現れる。
- `text_channel` … `0-3` overlay `一晩`
- `attached` … `KITCHEN.base`・`KITCHEN.states.明け方`・`KITCHEN.geography`・`KAMADO.appearance`
- `forbidden_set` … `PAN`・`KONA`
