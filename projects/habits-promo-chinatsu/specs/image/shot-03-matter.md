# 画像仕様 — 『ハビッツ！！！』碓氷千夏 キャラクタープロモーション 第三ショット「名を出さずに、用件から切り出す」（対話 / motion / 4s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **共通の規則は、第一ショットの画像仕様のヘッダに書いてある**——読む。

---

⚠️ **この1枚が写すのは `after` の側である**——**口が動いていて、名がまだ来ていないところ。**
   `§7` の Peak がそれである——「**The position where the name belongs stays empty.**」＝
   `unit.after`（「**用件から話し始めている。名は、一度も来ない。**」）。
   **このショットでは、両者が同じ一点である**（第一ショットと同じ）。

⚠️ **口が動いている1枚である。** ⚠️ **静止画では、「動いている」は「語の途中である」としてしか
   現れない**——口が開ききっても閉じきってもいない、その途中の形である。
   ⚠️ **この1枚に、名は要らない。** 名が来る位置が空いていることが、この1枚の内容である。
   **空きは、Negative ではなく `Prompt` が書く**——禁制は空きを作らない。

⚠️ **視線は、聞き手の側へ行く。レンズへは来ない。**（`§16` MUST——「**It does not come to the lens.**」）
   ⚠️ **参照画像においても同じである。** ⚠️ **ここが、この作品で最も壊れやすい一点である**——
   話している顔は、いちばん簡単にカメラを見つける。**五分の一（五枚のうち一枚）ではなく、
   五枚のうち三枚が顔のショットである**——第三・第五、そして第一の後半である。
   **ゆえに第三の画像仕様は、視線の行き先を名指しで書く。**
   ⚠️ **第五ショットだけが、これを免れる**（著者の決定 2026-09-18）。**ここではない。**

⚠️ **聞き手は、枠の外にいる。** **画面の空いた側が、この1枚の第二の主題である。**
   ⚠️ **そちらを見せないこと**——肩も、後ろ姿も、机の上の手も、映り込みも。
   `no second person in frame` は §18 から写したものである。

⚠️ **このショットは、日本語で話す**（決定 2026-09-18、著者——`§14`）。
   ⚠️ **そのことは画像の側に現れない**——**音は1枚に写らないからである。**（**口が動くことは写る。**）
   ⚠️ **それでも音の節は、この1枚の `Negative` に在る**——**§18 の写しだからである**（下の一行）。
      **写らないものを禁じても、何も変わらない。** **が、消さない**——**二経路の禁止が一字も
      違わないことが、この作品の決定である**（`bible.yaml`「画像の経路」）。
   **発話の言語は、§14 と `Audio Prompt` が負う**（第一ショットのヘッダ）。

⚠️ **Negative は §18 `Negative Prompt` と同一である**（第一ショットのヘッダを読む）。
⚠️ **人名はローマ字にしない**（決定）。**Negative は字種を禁じない。**
⚠️ **下半身は枠に入らない。** この1枚は顔と、聞き手のいない側の空きである。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-promo-chinatsu-s03.yaml`
- 投入する文: **下の節の1段落目が `Prompt` であり、2段落目が `Negative` である**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない
- 記録: `shots/habits-promo-chinatsu-s03.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。

- `SCENE`: the mouth moving with no word arriving, and the place where a name belongs left empty
- `CHARACTERS`: 碓氷千夏 alone in frame, her gaze held past the frame's edge at someone who is not in it — **no one else is in this work**
- `SUBJECT`: 碓氷千夏's mouth, moving in the shape of a word, with no word issued and no name arriving
- `ACTION`: the mouth moving in the shape of speech, and nothing issued from it
- `LOCATION`: the left of the chest of a washable shirt in the staff room of a Japanese public elementary school, where the school-designated nameplate is worn
- `LIGHT`: a fluorescent key from the frame's upper edge, the lit side of the face warm and the shadow side deep cyan
- `ACCENT`: the lit edge of the cheek as the one small highlight, the shadow side left to carry the meaning

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of 碓氷千夏 speaking from the matter at hand with no name arriving, at the left of the chest of a washable shirt in the staff room of a Japanese public elementary school, under the fluorescent key that comes from the upper edge of the frame, with the lit edge of her cheek as the one small highlight and the shadowed side of her face left to carry the meaning. A scene board for the master staging of this one shot, in 16:9 — the blocking, the camera and the light fixed as the standard the take must match. She is a woman of thirty-three, her identity locked to the frozen reference pair, in a washable shirt with no outer garment; the nameplate is worn at the left of the chest, its printed face lost to the key. Her mouth is in the middle of a word and the sentence has already passed the place where a name belongs; her gaze is on the side the one she is speaking to is on, which is past the frame's edge, and it does not come to the lens. Clean anime lineart on the face, held deliberately below the light. Saturated where the light falls and deep cyan in the unlit half, the warm side reaching its high point here — skin lit, everything else cool. Hyper-detailed layered light: bloom around the fluorescent tube at the frame's upper edge, dust suspended between the lens and the face and individually rendered rather than a flat wash, the room behind present only as lit blur, low visual density with generous negative space on the side the listener is on. The frame is close, at her height, the face filling one part of it and the empty side of the room held as the frame's second subject, equal in weight to the face. No second person is anywhere in the frame: no caller, no listener, no colleague, no passer-by, and no hand but hers.

no second person in frame, no caller in frame, no listener in frame, no colleague in frame, no passer-by in frame, no legible text on any surface, no legible name text, no legible name on any in-world prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no glyph-like marks on any surface, no signature, no handwriting by the subject, no calling voice as a sound effect, no audible speech, no spoken name, no voice-over, no narration, no background music, no face before the name is called, no completed action, no finished movement, no resolved gesture, no smile, no tears, no fear, no pleading, no exaggerated expression, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket, no blazer, no outer garment, no identifying clothing, no identifying hairstyle, no identifying prop, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no watermark, no morphing or drifting facial identity, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## 記録との対応

- `unit` … 「口が、まだ動いていない」→「**用件から話し始めている。名は、一度も来ない。**」
- `beats` … 0-2s 口が動き出す／2-4s 話し続ける、名は最後まで来ない。
  **この1枚は BEAT 1 と BEAT 2 の境目である**——**名が来ないことは、最初から最後まで同じである。**
- `place` / `time` … `名札` / `2026年の勤務日の日中`
- `attached` … `碓氷千夏.identity`・`碓氷千夏.negatives`・`名札.base`・`名札.geography`
- ⚠️ **`rolemap` の `対話` が持つ固有基準のうち、「聞き手の反応」は空欄である**（ショット記録）。
  ⚠️ **「声との同期」は、ショットでは引ける**（決定 2026-09-18——彼女は喋る）。
  **が、この1枚には写らない**——**1枚は口の途中を写すだけで、音を持たない。**
  **引けない基準を、引けたことにしない。**
