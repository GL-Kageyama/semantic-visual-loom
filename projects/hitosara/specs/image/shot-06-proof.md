# 画像仕様 — 一皿ができるまで 第1章 Clip 6/10（運動（自然現象） / motion / 8s）

⚠️ **これは動画の最初のコマである。** **だからこの1枚は、06 の動画の t=0 でなければならない**
——§7 Beginning「The bowl sits under its cloth, small and low」の瞬間である。
⚠️ **この作品の主題が、この1枚に掛かっている。** 「発酵が時を運ぶ」——時計は無く、
時間は**生地の側で進む**。**だからこの1枚には、時間の目盛りを描くものが1つも無い。**
⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である
——**種類の話であって、モードの話ではない**（`L18` がこの形を見る）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine` の様式カード `luminous-anime`
- 記録: `shots/hitosara-ch01-seg06.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: a wide ceramic bowl under a coarse linen cloth, the dough just touching the cloth from below
- `ACTION`: rising — slowly, from the inside, without anything pushing it
- `LOCATION`: a wooden bench in a one-room bakery, midday
- `ACCENT`: the warm gold light of midday lying flat across the linen

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of a wide ceramic bowl under a coarse linen cloth with
the dough just touching the cloth from below, rising slowly from the inside without anything
pushing it, on a wooden bench in a one-room bakery at midday, with the warm gold light of
midday lying flat across the linen as the strongest highlight. Hyper-detailed layered light:
volumetric shafts travelling through the air from a window at the frame edge, anamorphic lens
flare and bloom around the source, fine flour dust suspended and individually rendered. A
saturated palette of magenta and gold against deep cyan shadow, the bench faintly reflective
where the light reaches it. Composition at the height of the bowl, level with the cloth so
that the lift of the cloth is legible as a *difference from flat*, everything subordinate to
the light, clean anime lineart. **The cloth is already being pushed from below** — one convex
lift at the centre, the weave drawn tight over it, the flour that settled on the cloth
beginning to slide toward the rim. **Nothing else in the frame moves or is about to move.**
No hand, no tool, no second object, no oven, no bread. Low visual density: the bowl, the
cloth, the lift, and the light. No readable lettering anywhere — **and in particular nothing
that could be read as a clock, a dial, a timer or a number.**

## Negative（英語）

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no hands, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no cross-section, no steam, no bubble, no foam, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この1枚の失敗の形は「気泡を描くこと」である

`no bubble`・`no foam` を、この1本だけに足してある。気泡は**発酵の説明**である——
**説明を描けば、時間が目盛りになる。** この作品で時間を運ぶのは**生地の側**であって、
気泡の絵ではない。**見えないものを、見えないまま見せる。**
⚠️ **05 の `no steam` と、同じ判断である**（蒸気も「発酵している」という説明である）。
⚠️ **禁じる語を足すことは、欠陥を消すことではない。** 足したのは**失敗の形を先に名指しするため**
である。**消えるかどうかは生成を見なければ分からない。**

## ⚠️ `no wall clock`・`no calendar`・`no digital timer` が、この1枚では主題に属する

他のショットでは**世界の恒常的な禁止**（作品の決めごと）である。**ここでは違う**——
**この作品は時計を持たないことで時間を語る。** だからこの3節は、
**このショットの内容そのものに属する禁止**である。⚠️ **同じ語が、ショットによって違う理由で在る。**
**この区別は人間にしか読めない**——機械は3節が在ることしか見ない。

## ⚠️ この Negative は、開示の系列の一部である

`no oven interior`・`no visible flame`・`no glow through the door seam` の3節は、
**08 で開くまで全部の画像プロンプトに在り、08 で落ちる。**
`no cut loaf`・`no visible crumb`・`no cross-section` の3節は、**09 で割るまで在り、09 で落ちる。**
⚠️ **この系列を読む検査は、いま無い。** 相手は引き渡しの層である（段2）。

## 記録との対応

- `unit` … 「生地は、置かれたまま小さい」→「生地は、蓋を持ち上げる」。
  **この1枚が写すのは `before` の側である**——しかも**持ち上がり始めた側**。
  動画の BEAT 2（`2-5s`）が、この1枚の続きである。
- 動画仕様の §7 Beginning … "The bowl sits under its cloth, small and low."
  **この1枚は、その一文の絵である。**
- `motion`（**画像へは行かない**）… 「生地そのもの／外から見れば、ほとんど止まっている」
  ——**1枚は、まさにその「ほとんど止まっている」の側である。**
- `time: 昼` … **画面の色であって、尺度ではない。** `KITCHEN.states.昼` が添付に在る。
- `forbidden_set` に `KAMADO`・`PAN` … **窯もパンも、まだ画面に出ない。**
- `attached` … `KITCHEN.base`・`KITCHEN.states.昼`・`KITCHEN.geography`・`KONA.appearance`
