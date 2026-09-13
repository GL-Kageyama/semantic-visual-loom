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
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg09.yaml`
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
- 記録: `shots/hitosara-ch01-seg09.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the loaf torn open and the crumb taking the light
- `CHARACTERS`: no figure in frame, no hands
- `SUBJECT`: a baked loaf torn open, its crumb exposed
- `ACTION`: the wall of air pockets taking the light from inside
- `LOCATION`: a wooden bench in a one-room bakery, morning
- `LIGHT`: morning light falling into the cut face, the air pockets lighting from inside
- `ACCENT`: the warm gold light inside the crumb

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of a baked loaf torn open with its crumb exposed, the wall of air pockets taking the light from inside, at a wooden bench in a one-room bakery in the morning, with the warm gold light inside the crumb as the strongest highlight. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Morning light falls into the cut face and the air pockets light from inside. Hyper-detailed layered light: the shaft travelling through the air above the bench, bloom around the window at the frame edge, flour dust and steam suspended and individually rendered rather than a flat wash. A saturated palette of magenta and gold where the crumb takes the light against deep cyan in the crust's shadow, the torn face faintly reflective and doubling the light. Composition close and level, the torn face across the centre with the dark crust around it and the air above left open; the loaf small and subordinate to the light. Clean anime lineart on the crust, held below the light. No figure in frame, no hands. One focal point, generous negative space.

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
