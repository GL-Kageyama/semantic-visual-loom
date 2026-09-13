# 画像仕様 — 一皿ができるまで 第1章 Clip 6/10（運動（自然現象） / motion / 8s）

⚠️ **これはこのショットの見せ場の1枚である。** **動画へ添付（参照画像）として渡る**——
だから**§7 Beginning「The bowl sits under its cloth, small and low」の瞬間ではない。**
**この1枚は、生地が自分の布を持ち上げたところを切る。**
⚠️ **前の版は `before` の側を切っていた**——著者が前提を選び直したので直した（04 と同じ）。
⚠️ **この作品の主題が、この1枚に掛かっている。** 「発酵が時を運ぶ」——時計は無く、
時間は**生地の側で進む**。**だからこの1枚には、時間の目盛りを描くものが1つも無い。**
⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である
——**種類の話であって、モードの話ではない**（`L18` がこの形を見る）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg06.yaml`
    ——gozen-niji の `series-constants.md`（シリーズ定数＋開示台帳）と同じ型である
- 投入する文: **下の節の1段落目が `Prompt` であり、エンジンの出力であって、`chatgpt-image-2.5` へ
  投入する正典である**（決定B）。**2段落目が `Negative` である**（決定A）
- ⚠️ **下の7欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`REF_FORMAT` と `REF_STYLE` が「どのカードの穴か」を名乗る。** `L22` がそれを読み、
  **名乗ったカードが実際にその穴を宣言しているか**を確かめる——**名乗りは宣言であって、一致ではない。**
- ⚠️ **⑦Negative の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` と開示の系列が
  **段落の集合**として読む。
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**——
  **見出しが本文の間にあると、選択がそれを巻き込む。** 空行1つが、そのまま `Negative` を
  繋ぐ空行である。**繋がった文字列の写しは置かない**（写しは食い違う）。
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）
- 記録: `shots/hitosara-ch01-seg06.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the dough rising until it lifts its own cloth
- `CHARACTERS`: no figure in frame, no hands
- `SUBJECT`: a wide ceramic bowl under a coarse linen cloth, the cloth lifted from below by the dough
- `ACTION`: lifting the cloth — rising without anything pushing it
- `LOCATION`: a wooden bench in a one-room bakery, midday
- `LIGHT`: flat midday light lying across the lifted linen
- `ACCENT`: the warm gold light of midday lying flat across the linen

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of a wide ceramic bowl under a coarse linen cloth, the cloth lifted from below by the dough, rising with nothing pushing it, at a wooden bench in a one-room bakery at midday, with the warm gold light of midday lying flat across the linen as the strongest highlight. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Flat midday light lies across the lifted linen. Hyper-detailed layered light: the shaft falling through the air above the bowl, bloom around the window at the frame edge, flour dust suspended and individually rendered rather than a flat wash. A saturated palette of magenta and gold on the lit cloth against deep cyan in the room behind, with flour slipping from the rim of the cloth and caught in the light. Composition level and close, the bowl across the lower two thirds with the lifted cloth as the single raised point and the air above it left open; the cloth small and subordinate to the light. Clean anime lineart on the linen, held below the light. No figure in frame, no hands — the dough itself is what moves. One focal point, generous negative space.

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
  **この1枚が写すのは `after` の側である**——**このショットの変化が済んだところ。**
  ⚠️ **§7 Beginning（"The bowl sits under its cloth, small and low"）は、この1枚ではない。**
  **その瞬間は動画の BEAT 1〜2 が担う。**
- `motion`（**画像へは行かない**）… 「生地そのもの／外から見れば、ほとんど止まっている」
  ——**1枚は動かない。** だからこの欄は画像には現れず、
  **「どの瞬間を切るか」を決めるためだけに在る。**
- `time: 昼` … **画面の色であって、尺度ではない。** `KITCHEN.states.昼` が添付に在る。
- `forbidden_set` に `KAMADO`・`PAN` … **窯もパンも、まだ画面に出ない。**
- `attached` … `KITCHEN.base`・`KITCHEN.states.昼`・`KITCHEN.geography`・`KONA.appearance`
