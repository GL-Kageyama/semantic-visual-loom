# 画像仕様 — 一皿ができるまで 第1章 Clip 4/10（運動（躍動） / motion / 6s）

⚠️ **これは動画の最初のコマである。** 決定（2026-09-13、著者）で、全ショットは
画像 → 動画の順に回る。**だからこの1枚は、04 の動画の t=0 でなければならない**——
§7 Beginning「Flour and water sit apart in the same hollow」の瞬間である。
⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である
——**種類の話であって、モードの話ではない**（`L18` がこの形を見る）。
⚠️ **02 と紛らわしい。別の1枚である。** 02 は**界面の拡大**（粉と水の境目だけ）であり、
04 は**中景の穴**（粉の窪みと、そこへ入る手）である。**尺度と、手の有無が違う。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg04.yaml`
    ——gozen-niji の `series-constants.md`（シリーズ定数＋開示台帳）と同じ型である
- 投入する文: **下の `Prompt` はエンジンの出力であり、`chatgpt-image-2.5` へ投入する正典である**（決定B）
- ⚠️ **下の欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`scene-board` が要求する穴は、下の4つでは足りない**（`SCENE`／`CHARACTERS`／`LIGHT` が要る。
  2層の和で7欄になる——`ACTION`・`LOCATION` は両層に同名で在り、**同じ値が両方の穴に入る**）
- ⚠️ **⑦Negative の出力はここではなく下の `Negative` 節へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は節として保つ**——`L21` と開示の系列が節の集合として読む
- 記録: `shots/hitosara-ch01-seg04.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: a shallow well of flour with water pooled in it, and one open hand entering at the frame edge
- `ACTION`: hanging over the hollow — the instant before the palm closes on it
- `LOCATION`: a wooden kneading bench scarred by scraping, one-room bakery, morning
- `ACCENT`: the warm gold light lying across the wet rim of the hollow

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of a shallow well of flour with water pooled in it and
one open hand entering at the frame edge, hanging over the hollow in the instant before the
palm closes on it, at a wooden kneading bench scarred by scraping in a one-room bakery in the
morning, with the warm gold light lying across the wet rim of the hollow as the strongest
highlight. Hyper-detailed layered light: volumetric shafts travelling through the air from a
window at the frame edge, anamorphic lens flare and bloom around the source, flour dust
suspended and individually rendered rather than a flat wash. A saturated palette of magenta
and gold against deep cyan shadow, the damp bench and the wet rim faintly reflective and
doubling the light. Composition low and close at the height of the bench, the hollow across
the lower third and the hand coming in from the edge, everything subordinate to the light,
clean anime lineart on the hand kept deliberately below the light. **The two substances are
still two** — no fold has happened, no mass has formed. The hand follows the character sheet:
hands and coarse linen apron only, no face, no body, no ring, no watch. Low visual density:
one focal point, generous negative space. No readable lettering anywhere.

## Negative（英語）

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no cross-section, no second hand, no formed dough, no smooth elastic mass, no dough hook, no bench scraper, no flour cloud, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この1本だけに足した語がある——**失敗の形を先に名指しする**

この1枚は**動きの直前**である。モデルは「捏ねている途中」を描きたがる——
だから `no formed dough`・`no smooth elastic mass`・`no flour cloud` を置く。
**02 と同じ理由である**（`no numerals` を厚くしたのと同じ作法）——
⚠️ **禁じる語を足すことは、欠陥を消すことではない。** 消えるかどうかは生成を見なければ
分からない。**足したのは、失敗の形を先に名指しするためである。**
`no second hand` も同じである——**手は1つだけ**、しかも**枠の縁から**入る。

## ⚠️ この Negative は、開示の系列の一部である

`no oven interior`・`no visible flame`・`no glow through the door seam` の3節は、
**08 で開くまで全部の画像プロンプトに在り、08 で落ちる。**
`no cut loaf`・`no visible crumb`・`no cross-section` の3節は、**09 で割るまで在り、09 で落ちる。**
⚠️ **この系列は、動画の §18 と同じ系列である。** 同じ禁制が、2つの経路の両方に要る
——**最初のコマで破られうるからである。**
⚠️ **この系列を読む検査は、いま無い。** `L10`・`L14` の相手は §18 である。
**相手は引き渡しの層である**（段2）。

## 記録との対応

- `unit` … 「粉と水は、まだ別々にそこにある」→「手の下で、ひとつの塊になる」。
  **この1枚が写すのは `before` の側である。**
- 動画仕様の §7 Beginning … "Flour and water sit apart in the same hollow."
  **この1枚は、その一文の絵である。**
- 動画仕様の BEAT 1 は `0-1.5s` で既に掌が押している——**この1枚はその手前である。**
- `motion`（**画像へは行かない**）… 「押し、畳み、回す」。**この1枚には現れない**
  ——1枚は動かない。動くのは動画の側である。
- `forbidden_set` に `KAMADO`・`PAN` … **窯もパンも、まだ画面に出ない。**
- `attached` … `BAKER.sheet`・`KITCHEN.base`・`KITCHEN.geography`・`KONA.appearance`・`MIZU.appearance`
