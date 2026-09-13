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
  - `format`: `scene-board` ／ `style`: `luminous-anime`
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg10.yaml`
    ——gozen-niji の `series-constants.md`（シリーズ定数＋開示台帳）と同じ型である
- 投入する文: **下の `Prompt` はエンジンの出力であり、`chatgpt-image-2.5` へ投入する正典である**（決定B）
- ⚠️ **下の欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`scene-board` が要求する穴は、下の4つでは足りない**（`SCENE`／`CHARACTERS`／`LIGHT` が要る。
  2層の和で7欄になる——`ACTION`・`LOCATION` は両層に同名で在り、**同じ値が両方の穴に入る**）
- ⚠️ **⑦Negative の出力はここではなく下の `Negative` 節へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は節として保つ**——`L21` と開示の系列が節の集合として読む
- 焼く層: `timeline` の `text_events`（段3）
- 記録: `shots/hitosara-ch01-seg10.yaml`

## 主題（英語・`distill-essence-engine` の4欄）

- `SUBJECT`: one plate on a bare table, the torn loaf on it, steam standing up from it
- `ACTION`: holding still while only the steam moves
- `LOCATION`: a plain table by a window in a one-room bakery, morning
- `ACCENT`: the warm gold light falling across the plate

## Prompt（英語・そのまま投入する）

A luminous realist anime illustration of one plate on a bare table with the torn loaf on it
and steam standing up from it, holding still while only the steam moves, on a plain table by
a window in a one-room bakery in the morning, with the warm gold light falling across the
plate as the strongest highlight. Hyper-detailed layered light: one volumetric shaft from
the window, anamorphic lens flare and bloom around the source, flour dust and the steam
suspended together and individually rendered. A saturated palette of magenta and gold
against deep cyan shadow, the table surface faintly reflective. Composition low and level
with the table, the plate slightly off center, a chair and a window suggested soft and out
of focus behind, the light source inside the frame at the window, everything subordinate to
the light, clean anime lineart. **Hands may enter at the frame edge only if the fragment
needs them — no face, no body, no ring, no watch.** Low visual density: the plate, the
steam, and the light. The right of the frame is left quiet and uncrowded for text to be
placed over later. No readable lettering anywhere.

## Negative（英語）

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
