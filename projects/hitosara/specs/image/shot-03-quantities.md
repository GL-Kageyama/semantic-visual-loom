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
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg03.yaml`
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
- 焼く層: `timeline` の `text_events`（段3）。**文字はここではなく、そこで載る**
- 記録: `shots/hitosara-ch01-seg03.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the quantities and the order laid out to be written over
- `CHARACTERS`: no figure in frame, no hands
- `SUBJECT`: flour, water and salt measured out on a flour-dusted bench
- `ACTION`: lying still and separated, each in its own place
- `LOCATION`: a wooden kneading bench, straight down from above, morning
- `LIGHT`: flat even light from directly above, the bench evenly lit, nothing favoured
- `ACCENT`: the single fingertip of salt, catching the strongest highlight

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of flour, water and salt measured out on a flour-dusted bench, lying still and separated, each in its own place, at a wooden kneading bench seen straight down from above in the morning, with the single fingertip of salt catching the strongest highlight. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Flat even light from directly above, the bench evenly lit, nothing favoured. Hyper-detailed layered light: a soft shaft through the air above the bench, bloom held to the salt and the wet rim, flour dust suspended and individually rendered rather than a flat wash. A saturated palette of magenta and gold in the lit half against deep cyan beneath the bench edge, the damp bench faintly reflective and doubling the light. Composition symmetrical and top-down, the three substances on the lower two thirds with the upper corners left open — the even light itself is the subject. Clean anime lineart, held below the light. No figure in frame, no hands. One focal point, generous negative space. Nothing in this image is written.

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
