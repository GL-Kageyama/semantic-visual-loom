# 画像仕様 — 一皿ができるまで 第1章 Clip 8/10（運動（微細運動） / motion / 5s）

⚠️ **開示の第1点である。ここで窯が開く。** この1枚から
`no oven interior`・`no visible flame`・`no glow through the door seam` の**3節が落ちる**。
⚠️ **だが、この1枚が写すのは「開いた後」ではない。** 動画の §7 Beginning は
"An iron door, closed, with one line of light at the seam." と言う——
**だからこの1枚は、閉じた扉と、隙間の光である。**
⚠️ **落ちた3節のうち、この1枚で目に見えるのは `no glow through the door seam` だけである。**
残る2節（`no oven interior`・`no visible flame`）は**まだ画面に何も変えない**——
**それでも落ちる。** 落ちるのは**この1本の許し**であって、**この1枚の絵**ではない。
⚠️ **この仕様は §1–20 を持たない**——**種類の話であって、モードの話ではない**（`L18` がこの形を見る）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg08.yaml`
    ——gozen-niji の `series-constants.md`（シリーズ定数＋開示台帳）と同じ型である
- 投入する文: **下の `Prompt` はエンジンの出力であり、`chatgpt-image-2.5` へ投入する正典である**（決定B）
- ⚠️ **下の欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`scene-board` が要求する穴は、下の4つでは足りない**（`SCENE`／`CHARACTERS`／`LIGHT` が要る。
  2層の和で7欄になる——`ACTION`・`LOCATION` は両層に同名で在り、**同じ値が両方の穴に入る**）
- ⚠️ **⑦Negative の出力はここではなく下の `Negative` 節へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は節として保つ**——`L21` と開示の系列が節の集合として読む
- 記録: `shots/hitosara-ch01-seg08.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: a closed iron oven door in a far wall, and one line of light lengthening along its seam
- `ACTION`: about to turn on its hinges — the instant before the door gives
- `LOCATION`: a one-room bakery at the wood-fired oven, before dawn
- `ACCENT`: the single line of firelight at the seam, brighter than anything else in the frame

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of a closed iron oven door in a far wall with one line
of light lengthening along its seam, about to turn on its hinges in the instant before the
door gives, at the wood-fired oven in a one-room bakery before dawn, with the single line of
firelight at the seam brighter than anything else in the frame as the strongest highlight.
Hyper-detailed layered light: bloom and anamorphic flare gathering around the seam, fine flour
dust suspended in the air and visible against the dark, the stone floor dusted with flour and
faintly reflective. The palette has narrowed — gold and black, with the magenta of the earlier
shots gone and deep cyan only in the unlit half of the room. Composition at the height of the
door, the door on the same side of frame as in every other shot, the seam running vertically
through the frame, everything subordinate to that one line of light, clean anime lineart. **The
door is shut. Nothing is visible through it except the line at the seam.** The hands follow the
character sheet — hands and coarse linen apron only, **no face, no body, no ring, no watch** —
and they are on the door, not reaching past it. Low visual density, and darker than any other
plate in the film. No readable lettering anywhere.

## Negative（英語）

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no cut loaf, no visible crumb, no cross-section, no hand reaching into the oven, no second light source, no lamp, no shelf inside the oven, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この3節が落ちることは、この1枚では**まだ何も変えない**

`no oven interior` と `no visible flame` は、**この1枚の絵を1画素も変えない**——
扉は閉じており、中は写らないからである。**それでも2節は落ちる。**
⚠️ **落ちるのは「禁じる必要が無くなったから」である**——`disclosure_state` が
`KAMADO.interior: opened` になり、`ledger.disclosure` が `negative: changed` を宣言している。
⚠️ **「写らないから要らない」と「開いたから要らない」は、別のことである。**
前者なら**この1枚だけ**落とせばよい。**落ちるのはこの1枚から先の全部である。**
**同じ理由で、`no glow through the door seam` は、この1枚でいちばん重い**——
07 では**禁じられていた光**が、この1枚では**主題そのもの**である。

## ⚠️ この Negative は、開示の系列の2つ目の折れ目である

- `no oven interior`・`no visible flame`・`no glow through the door seam` … **この1本で落ちる。**
- `no cut loaf`・`no visible crumb`・`no cross-section` … **09 で落ちる。** ここにはまだ在る。
⚠️ **この作品の画像プロンプトの Negative は、ここで半分になる。**
⚠️ **この系列を読む検査は、いま無い。** `L10` は動画の §18 を相手にする。
**画像の側の相手は引き渡しの層である**（段2）。

## 記録との対応

- `unit` … 「窯の扉は閉じている」→「扉が開き、中の火だけが動いている」。
  **この1枚が写すのは `before` の側である**——ただし `before` の**最後の瞬間**。
- 動画仕様の §7 Beginning … "An iron door, closed, with one line of light at the seam."
  **この1枚は、その一文の絵である。**
- 動画仕様の BEAT 1 `0-1.5s` … 鉄が回り、中はまだ見えない。**この1枚はその手前である。**
- `disclosure_state` … `KAMADO.interior: opened` / `PAN.interior: sealed`
- `forbidden_set` … `PAN`・`KONA`
- `attached` … `BAKER.sheet`・`KITCHEN.base`・`KITCHEN.states.明け方`・`KITCHEN.geography`・`KAMADO.appearance`
