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
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg07.yaml`
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
- 焼く層: `timeline` の `text_events`（段3）
- 記録: `shots/hitosara-ch01-seg07.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the window going from blue to gold and the hand moving to light the fire
- `CHARACTERS`: a pair of hands stopped in front of the door — no face, no body
- `SUBJECT`: a closed iron oven door in a far wall, with a pair of hands stopped in front of it
- `ACTION`: waiting while the window behind goes from blue to gold
- `LOCATION`: a one-room bakery, before dawn
- `LIGHT`: the window turning gold, the room filling with the first warm light
- `ACCENT`: the first gold of the coming morning across the stone floor

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of a closed iron oven door in a far wall with a pair of hands stopped in front of it, waiting while the window behind goes from blue to gold, at a one-room bakery at first light, with the first gold of the coming morning across the stone floor as the strongest highlight. A scene board for the master staging of this one scene, in 16:9 — the blocking, the camera and the light fixed as the standard every cut of the scene must match. The window turns gold and the room fills with the first warm light; the door stays closed and the iron stays dark. Hyper-detailed layered light: the shaft travelling across the floor from the window, anamorphic flare and bloom around the window at the frame edge, dust suspended and individually rendered rather than a flat wash. A saturated palette of magenta and gold on the floor and the near wall against deep cyan still holding in the corners of the room, the stone floor faintly reflective and doubling the light. Composition fixed and wide, the door off-centre on the far wall with the hands low in the frame and the window light entering from behind them; the hands small and subordinate to the light. Clean anime lineart on the hands and the iron, held below the light. Hands and coarse linen apron only, no face, no body, no ring, no watch. One focal point, generous negative space.

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
