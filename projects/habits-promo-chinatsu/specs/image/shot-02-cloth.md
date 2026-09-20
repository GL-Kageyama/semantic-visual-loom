# 画像仕様 — 『ハビッツ！！！』碓氷千夏 キャラクタープロモーション 第二ショット「布の上で、指が止まる」（所作 / motion / 7s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
⚠️ **共通の規則は、第一ショットの画像仕様のヘッダに書いてある**——読む。
   （2経路・`after` の側・Negative は五枚同一・人名はローマ字にしない・見出しに番号を振らない）

---

⚠️ **この1枚が写すのは `after` の側である**——**指が止まって、留め具がまだ閉じていないところ。**
   ⚠️ **`§7` の Peak は、ここではない。** Peak は「**The finger is tracing, and the characters
   stay under the cloth.**」——**なぞっている最中**である。
   ⚠️ **この1枚は `after` を採った**（`unit.after`——「**布の上で、指が止まっている。**
   三文字が、布の下にある。**留め具は、まだ閉じない。**」）。
   **理由は §17 が第一位に置く一行である**——「**The stop is the content** — the finger stops
   and the hand stays.」**このショットの内容は、止まった手である。**
   ⚠️ **参照画像は、テイクが到達すべき姿を固定する。** なぞっている最中を渡せば、
   **「まだ止まっていない」が標準になる。**

⚠️ **この1枚に、字は写らない。** 三文字は**布の下**にあり、留め具は**開いたまま**である。
   ⚠️ **見せてしまう経路は三つある**——布を持ち上げる、布が透ける、留め具が閉じる。
   **Negative が三つとも禁じている**（`no legible text on any surface`・
   `no completed action` は §18 から写したものである）。
   ⚠️ **この1枚は参照画像である。ゆえに「字が読める」を渡せば、テイクは字を読ませにいく。**

⚠️ **顔は下を向いており、主題を持たない。**（`§3`——「**her face holds no subject in this shot.**」）
   ⚠️ **参照画像においても、顔は主題ではない。** 手が主題である。

⚠️ **Negative は §18 `Negative Prompt` と同一である**（第一ショットのヘッダを読む）。
   ⚠️ **このショットで消える禁止は無い**——`no completed action` は第一ショットから在る。
   **留め具が閉じないことは、禁止の話ではない。保持の話である。**

⚠️ **人名はローマ字にしない**（決定）。**Negative は字種を禁じない。**
⚠️ **下半身は枠に入らない。** この1枚は左胸と手の最も近い枠である——**衣装はシャツで足りる。**

⚠️ **この1枚は、一度、生成器に棄却された**（2026-09-18——「プロンプトの内容が
   コンテンツポリシーに違反している可能性があります」）。**理由は告知されない。**
   ⚠️ **この一段は、棄却の原因を断定しない。** 分かっていることだけを書く——
     **この1枚は、この作品で最も近い枠であり、体の部位を最も多く名指ししていた。**
   ✅ **打った手は二つである。**
     ① **`breast` を `the left of the chest` に戻した**——**出典は `胸の左` である**
        （run-10「第3話 三文字をなぞる」——「**名札は胸の左に着ける。**」）。
        **`breast` は、この一段の訳語であった。原文より狭く、原文より強い。**
        ⚠️ **言い換えではない。原文へ寄せたのである。**
     ② **狭い枠の中で体の部位を二度名指ししていた三箇所を減らした**——重複した位置句、
        「**on the left of the chest and the hand**」→「**on the hand and the cloth**」、
        「**across the chest**」→「**across the shirt**」。
   ⚠️ **題材は一字も変えていない。** 手が布の上で止まること、留め具が閉じないこと、
      **三文字が布の下にあること**——**この1枚の中身は、そのままである。**
   ⚠️ **再投入で通らなければ、次の被疑は「学校という場」と「`no outer garment`」である。**
      **そのときも、題材ではなく語を動かす。**
   ⚠️ **置換は五ショット両経路に一度に効かせた**（`bible.yaml`「画像の経路」に対応表）。
      **片側だけ直せば、作品が同じ場所を二つの名で呼ぶ。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-promo-chinatsu-s02.yaml`
- 投入する文: **下の節の1段落目が `Prompt` であり、2段落目が `Negative` である**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**——
  **見出しが本文の間にあると、選択がそれを巻き込む。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない
- 記録: `shots/habits-promo-chinatsu-s02.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。

- `SCENE`: a surname read through cloth in three slow passes of one finger, and the finger stopping — **the cloth stays plain above it**
- `CHARACTERS`: 碓氷千夏 alone in frame, her face down and holding no subject — **no one else is in this work**
- `SUBJECT`: 碓氷千夏's right hand, stopped on the cloth over the nameplate
- `ACTION`: stopped on the cloth over the nameplate, the pin still unfastened
- `LOCATION`: the left of the chest of a washable shirt in the staff room of a Japanese public elementary school, at the cloth over the school-designated nameplate
- `LIGHT`: a fluorescent key from above and at the frame's upper edge, the hand lit along its upper edge
- `ACCENT`: the lit upper edge of the hand as the one small highlight in the frame

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of 碓氷千夏's right hand stopped on the cloth over the school-designated nameplate, at the left of the chest of a washable shirt in the staff room of a Japanese public elementary school, under the fluorescent key that comes from above and at the frame's upper edge, with the lit upper edge of the hand as the one small highlight. A scene board for the master staging of this one shot, in 16:9 — the blocking, the camera and the light fixed as the standard the take must match. She is a woman of thirty-three, her identity locked to the frozen reference pair, in a washable shirt with no outer garment; the nameplate is worn at the left of the chest, its printed face lost to the key. One finger has finished three slow passes over the cloth and has stopped there, and the hand has not been withdrawn; the cloth stays between the finger and the name it reads, a shallow fold still standing in the weave, and the pin is present and unfastened. Her face is down and holds no subject. Clean anime lineart on the hand and the cloth, held deliberately below the light. Saturated where the light falls and deep cyan in the unlit side of the shirt, the palette narrowed to cloth, skin and plastic. Hyper-detailed layered light: bloom around the fluorescent tube above the frame's upper edge, the hand lit along its upper edge with its shadow falling across the shirt and lying on the cloth, dust suspended and individually rendered behind the hand rather than a flat wash, the room behind present only as lit blur, the lowest visual density in the work and one focal point. The frame is the closest in the work, on the hand and the cloth, the edge of the plastic only at the frame's edge and the hand filling much of it, the finger pressing the cloth rather than hovering over it. No second person is anywhere in the frame: no caller, no listener, no colleague, no passer-by, and no hand but hers.

no second person in frame, no caller in frame, no listener in frame, no colleague in frame, no passer-by in frame, no legible text on any surface, no legible name text, no legible name on any in-world prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no glyph-like marks on any surface, no signature, no handwriting by the subject, no calling voice as a sound effect, no audible speech, no spoken name, no voice-over, no narration, no background music, no face before the name is called, no completed action, no finished movement, no resolved gesture, no smile, no tears, no fear, no pleading, no exaggerated expression, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket, no blazer, no outer garment, no identifying clothing, no identifying hairstyle, no identifying prop, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no watermark, no morphing or drifting facial identity, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## 記録との対応

- `unit` … 「名札が、胸の左にある。手は、まだ上がっていない」→「**布の上で、指が止まっている。**
  三文字が、布の下にある。**留め具は、まだ閉じない。**」
- `beats` … 0-4s 手が入り、上がる／4-7s 三文字をなぞる、そして止まる。
  **この1枚は BEAT 2 の側である**——**保持の側であり、この作品で唯一「保持が主題である」ショット。**
- `place` / `time` … `名札` / `2026年の勤務日の日中`
- `attached` … `碓氷千夏.identity`・`碓氷千夏.negatives`・`名札.base`・`名札.geography`
- ⚠️ **この1枚が写す「止まった」は、静止画では「手が引かれていないこと」としてしか現れない。**
  **動きの不在が、この1枚では形である**（第一ショットと同じ構造である）。
- ⚠️ **このショットがこの作品の中心である**（`§17`——「This is the work's centre」）。
  **ゆえにこの1枚が外れたときの値段が、五枚で最も高い。**
  **それでも、経路を切る理由にはならない**——**外れた一枚は、一枚の値段で棄却できる。**
