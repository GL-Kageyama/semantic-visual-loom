# 画像仕様 — 一皿ができるまで 第1章 Clip 10/10（モンタージュ / motion / 4s）

⚠️ **これは1枚ではない。** `モンタージュ` は**短い断片が切れ目で繋がる**——
この仕様は**断片の下地**であり、繋ぎは編集が行う。
⚠️ **文字は編集で載る**（`一皿`）。`text_channel` の行き先は `edit:timeline` である。
⚠️ **ここで `motion.law` が様式と正面から噛み合う。** 様式 `luminous-anime` の
Motion character は「何かが常に動いている」と言う。モンタージュは
**1ショットの中で連続して動かない**——切れ目で動く。`law` はその衝突を明示している:
**断片のそれぞれの中で満たされる。**
⚠️ **この噛み合わせを機械が読むことは、いま無い**——`motion.law` と様式カードの
`Motion character` を突き合わせる照合は未実装である。**ここに記録として残す。**
⚠️ **この仕様は §1–20 を持たない**——**種類の話であって、モードの話ではない**
（`L18` がこの形を見る）。⚠️ **`composite` だったのは以前の話である**——
決定（2026-09-13、著者）で `mode` は `motion` になった。**断片は動く。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg10.yaml`
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
- 記録: `shots/hitosara-ch01-seg10.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the plate set down, the loaf broken on it, the steam standing
- `CHARACTERS`: no figure in frame; hands may enter at the frame edge only if the fragment needs them
- `SUBJECT`: one plate on a bare table, the torn loaf on it, steam standing up from it
- `ACTION`: holding still while only the steam moves
- `LOCATION`: a plain table by a window in a one-room bakery, morning
- `LIGHT`: the window light falling across the plate, the steam catching it
- `ACCENT`: the warm gold light falling across the plate

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of one plate on a bare table with the torn loaf on it and steam standing up from it, holding still while only the steam moves, at a plain table by a window in a one-room bakery in the morning, with the warm gold light falling across the plate as the strongest highlight. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. The window light falls across the plate and the steam catches it. Hyper-detailed layered light: the shaft travelling through the air from the window at the frame edge, anamorphic flare and bloom around the source, steam and dust suspended and individually rendered rather than a flat wash. A saturated palette of magenta and gold on the plate and the steam against deep cyan in the room behind, the bare table faintly reflective and doubling the light. Composition level and close, the plate on the lower two thirds with the table edge and the window behind it and the air above the plate left open; the plate small and subordinate to the light. Clean anime lineart, held below the light. No figure in frame — hands may enter at the frame edge only if the fragment needs them. One focal point, generous negative space.

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この Negative は、系列の終点である

- `no oven interior`・`no visible flame`・`no glow through the door seam` … **08 で落ちた。**
- `no cut loaf`・`no visible crumb`・`no cross-section` … **09 で落ちた。**
**この作品の画像プロンプトの Negative は、ここで最小になる。**
⚠️ **最小であることは、緩いということではない**——残っているのは
**作品の恒常的な禁止**（顔・時計・読める文字・ブランド）と、**様式の禁止**である。
⚠️ **この系列を読む検査は、いま無い。** 相手は引き渡しの層である（段2）。

## 記録との対応

- `unit` … 「皿は空である」→「皿の上に、一皿がある」
- `beats` … 0-1.5s 皿が置かれる／1.5-2.5s 断片が三つ、短く繋がる／2.5-4s 止まる、湯気だけが動く。
  **この1枚が切るのは 2.5-4s の側である**——`density: held` の側。
- `text_channel` … `3.4-4.0` overlay `一皿`
- `place` … `TABLE`（`TABLE.base` が `reference_set` に在る）
- `forbidden_set` … `KAMADO`・`KONA`・`SHIO`
