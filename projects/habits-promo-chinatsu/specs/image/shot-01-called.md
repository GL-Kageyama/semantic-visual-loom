# 画像仕様 — 『ハビッツ！！！』碓氷千夏 キャラクタープロモーション 第一ショット「名が呼ばれ、返事が一拍遅れる」（反応 / motion / 5s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
`§18` も `Negative Prompt` も `Style Motion` も無い——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` でも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

---

✅ **決定（2026-09-18、著者）——この作品は、画像 → 動画の二経路を持つ。**
   これは**基盤の決定（2026-09-13、著者）そのもの**である。**この一段は、それに戻った。**
   ⚠️ **戻る前に、この作品は経路を一つしか持っていなかった**——理由は `bible.yaml`「画像の経路」に
   **反転として残してある。消していない。**
   ✅ **理由は安定である。** 画像→動画では、**外れた一枚は一枚の値段で棄却できる。**
   文→動画では、外れはテイクを払った後にしか分からない
   （固定方針——**Generation is a sample. Adoption is selection, and the author is the editor.**）

⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——**最初のコマではない。**
   最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
   **この二十八秒の主題は、五つとも「変化」である。**

⚠️ **この作品の画像の `Negative` は、五枚で同一であり、しかも §18 `Negative Prompt` とも同一である。**
   理由は三つある——
     ① **この作品の禁止は、一度も変わらない**（`ledger.yaml` の開示の註。`L14` が一度も鳴らない）。
     ② **画像は動画へ添付される。** 経路ごとに禁止が違えば、**画像が許したものを動画が受け取る。**
        同一であることは、**参照とテイクが同じことを禁じていること**である。
     ③ `L21` は「覆っているか」を見る（**覆うであって、等しいではない**）。
        **この作品は、覆うより強く出る——等しくする。**
   ⚠️ **ゆえにこの Negative は §18 からの写しである。写しは食い違う**——
      鳴らす者は `L21` だけであり、**`L21` は動画の §18 を読まない**（あちらは `L10`・`L14` が負う）。
      **この一致を読む検査は、いま無い。穴のまま記録する**（`semantic.check_image_negative` の註）。

⚠️ **人名はローマ字にしない**（決定）。プロンプトの中の「碓氷千夏」は**日本語の字のまま置く。**
   ゆえに Negative は「**読める文字**」を禁じるのであって、**字種を禁じない**——
   `no Japanese kanji or kana` は**使わない。使えば、名そのものが消える。**

⚠️ **この1枚が写すのは `after` の側である**——**変化が済んだところ。** 規則はそれであって、
   `§7` の Peak ではない。**このショットでは、両者が同じ一点である**（Peak——
   「She has finished turning, and her mouth has still not opened.」＝ `unit.after`）。
   ⚠️ **第二ショットでは、両者は離れる。** Peak は「指がなぞっている」であり、
   `after` は「指が止まっている」である。**あちらは `after` を採った**——
   §17 が「**The stop is the content**」と書くのだから、止まった手がその側である。
   ⚠️ **この規則が効くのは、この1枚が参照画像だからである**——参照画像は
   **テイクが到達すべき姿**を固定する。**途中を渡せば、途中が標準になる。**
   ⚠️ **`§7` の Beginning（背中と横顔の半分）は、この1枚ではない**
   ——その瞬間は**動画の BEAT 1 が担う。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-promo-chinatsu-s01.yaml`
- 投入する文: **下の節の1段落目が `Prompt` であり、エンジンの出力であって、`chatgpt-image-2.5` へ
  投入する正典である**（決定B）。**2段落目が `Negative` である**（決定A）
- ⚠️ **下の7欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`REF_FORMAT` と `REF_STYLE` が「どのカードの穴か」を名乗る。** `L22` がそれを読み、
  **名乗ったカードが実際にその穴を宣言しているか**を確かめる——**名乗りは宣言であって、一致ではない。**
  ⚠️ **`scene-board` は、五欄すべてを宣言する唯一のカードである**（実測——
  `art-board` は `HOUR`／`LIGHT_SOURCE`、`concept-board` は `WORLD`／`WEATHER`、
  `progress-board` は `WORK`／`SCALE` を宣言する）。**選べるカードは一つしかない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**——
  **見出しが本文の間にあると、選択がそれを巻き込む。** 空行1つが、そのまま `Negative` を
  繋ぐ空行である。**繋がった文字列の写しは置かない**（写しは食い違う）。
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない
- 記録: `shots/habits-promo-chinatsu-s01.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: a name reaching her in a staff room with no voice in it, and the reply arriving one beat late
- `CHARACTERS`: 碓氷千夏 alone in frame, turned, her mouth still closed — **no one else is in this work**
- `SUBJECT`: 碓氷千夏, turned toward the frame, having finished turning and not answering
- `ACTION`: having finished turning, and not answering
- `LOCATION`: the left of the chest of a washable shirt in the staff room of a Japanese public elementary school, where the school-designated nameplate is worn
- `LIGHT`: a fluorescent key from the upper edge of the frame, the plastic of the nameplate catching it
- `ACCENT`: the plastic of the nameplate as the one small highlight in the frame

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of 碓氷千夏 having finished turning toward the frame with her mouth still closed, at the left of the chest of a washable shirt in the staff room of a Japanese public elementary school, under the fluorescent key that comes from the upper edge of the frame, with the plastic of the school-designated nameplate catching that light as the one small highlight. A scene board for the master staging of this one shot, in 16:9 — the blocking, the camera and the light fixed as the standard the take must match. She is a woman of thirty-three, her identity locked to the frozen reference pair, in a washable shirt with no outer garment; the nameplate is worn at the left of the chest, its printed face lost to the key. Her head has weight and has come to rest without overshooting; the turn is finished and the mouth has not opened. Clean anime lineart on the figure, held deliberately below the light. Saturated where the light falls and deep cyan in the unlit half, a narrow palette of fluorescent white, paper white and one plastic highlight, with the warm side reduced to skin. Hyper-detailed layered light: bloom around the fluorescent tube at the frame's upper edge, anamorphic flare only where the tube sits at the edge, dust suspended and individually rendered rather than a flat wash, a lit wall behind her present only as lit blur, low visual density and generous negative space. The frame is close, at her shoulder, the figure filling much of it, and the light — not the figure — is the subject. No second person is anywhere in the frame: no caller, no listener, no colleague, no passer-by, and no hand but hers.

no second person in frame, no caller in frame, no listener in frame, no colleague in frame, no passer-by in frame, no legible text on any surface, no legible name text, no legible name on any in-world prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no glyph-like marks on any surface, no signature, no handwriting by the subject, no calling voice as a sound effect, no audible speech, no spoken name, no voice-over, no narration, no background music, no face before the name is called, no completed action, no finished movement, no resolved gesture, no smile, no tears, no fear, no pleading, no exaggerated expression, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket, no blazer, no outer garment, no identifying clothing, no identifying hairstyle, no identifying prop, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no watermark, no morphing or drifting facial identity, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## 記録との対応

- `unit` … 「名が呼ばれ、彼女の頭がまだ動き出していない」→「**振り向ききって、口がまだ開かない。**」
  **この1枚が写すのは `after` の側である**——**このショットの変化が済んだところ。**
- `beats` … 0-3s 背中と横顔の半分／3-5s 振り向ききって口が開かない。**この1枚は BEAT 2 の側である。**
  ⚠️ **静止画であっても `beats` は「どの瞬間を切るか」を決めるためにある**（`hitosara` の註）。
- `place` / `time` … `名札` / `2026年の勤務日の日中`
- `attached` … `碓氷千夏.identity`・`碓氷千夏.negatives`・`名札.base`・`名札.geography`
- ⚠️ **この1枚が写す「遅れ」は、静止画では「口が開いていないこと」としてしか現れない。**
  **動きの不在が、この1枚では形である。**
