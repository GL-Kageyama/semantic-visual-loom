# 画像仕様 — 『ハビッツ！！！』碓氷千夏 キャラクタープロモーション 第四ショット「名の書かれた位置から、半歩下がる」（所作 / motion / 7s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **共通の規則は、第一ショットの画像仕様のヘッダに書いてある**——読む。

---

✅ **決定（2026-09-18、著者）——下半身は、スカートである。**

   ⚠️ **この決定は、テキストではなく画像から来た。** 経緯を残す——
      凍結した同一性の側、`ChatGPT Image 2026年9月18日 20_29_36.png`（**設定画・改訂稿4**）は
      **スカートを着ている。** 一方、追跡されている `ChatGPT Image 2026年9月17日 21_54_53.png`
      （**設定画・改訂稿3**）は**ズボンを穿いている**——⚠️ **この一枚を、記録はどれも名乗っていない。**
      ⚠️ **そして、どちらのテキストも下半身を書いていない**——
      `prompt.md` にも `expression.md` にも、その git 履歴にも、スカート／ズボン／パンツ／
      skirt／trouser は**一度も現れない**（実測）。
      **ゆえにこの一段は、著者に訊いた。著者が「スカートでいこう」と答えた。**

   ⚠️ **これは「出典に無い」のではなく「出典が言っていない」である。**
      出典の衣装は`洗えるシャツ、学校指定の名札`である（run-10）。**下半身は、そこに一行も無い。**
      **凍結した一枚が持つことは、出典が書いたことではない**——ゆえに `ledger.yaml` の
      `states` ではなく `identity` の註に在る（台帳の註）。**この決定も、そこに足す。**

   ⚠️ **この1枚だけが、全身を写す。**（`§3`——「**This is the only shot where she is in frame
      from something other than close range**」）。
      **ゆえにスカートは、五枚のうち、この一枚にしか現れない。**
      ⚠️ **他の四枚に書いてはならない**——枠に入らないものを `Prompt` に書けば、
      **モデルは枠の外の出来事を発明する。**

   ⚠️ **`no trousers` は、書かない。** 理由は二つである——
      ① **この作品の五枚の Negative は同一である**（第一ショットのヘッダ）。一行足せば、
         **五枚とも直すことになる**——そして §18 の Negative には、その一行は無い。
      ② **著者の規則は「否定形は空欄になり、モデルが衣装で埋める」である**（決定 2026-09-17）。
         **肯定形で書く。** 肯定形——`a plain skirt`——が、この決定の書き方である。

⚠️ **この1枚が写すのは `after` の側である**——**半歩下がって、まだ下がりきっていないところ。**
   `§7` の Peak がそれである——「**The half step, taken — and not completed.**」＝
   `unit.after`（「**半歩下がり、まだ下がりきっていない。重心は、後ろ足に移っている。**」）。
   **このショットでは、両者が同じ一点である。**
   ⚠️ **下がりきった姿を渡せば、テイクは下がりきる**——**そしてこの作品は、そこで終わる。**

⚠️ **紙は映って、読めない。**（`§5`——「**The line is written, the column is filled, and none of
   it can be read**」）。⚠️ **参照画像において、判読できないことは最も壊れやすい**——
   生成器は罫線の欄を、**もっともらしい字で埋める。**
   ⚠️ **「見せない」ではなく「見せて、読めない」である。** ゆえにこの1枚は、
   **紙を主題の一つとして置き、その上で字を解像させない。**

⚠️ **机の上のものは、何も動いていない。** 頁はめくられず、ペンは無く、他の紙も無い（`§5`）。
⚠️ **Negative は §18 `Negative Prompt` と同一である**（第一ショットのヘッダを読む）。
   ⚠️ **`no legible text on any surface` は第一ショットから在る**——開示の宣言は `covered` である。
⚠️ **人名はローマ字にしない**（決定）。**Negative は字種を禁じない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-promo-chinatsu-s04.yaml`
- 投入する文: **下の節の1段落目が `Prompt` であり、2段落目が `Negative` である**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない
- ⚠️ **出席簿のボードは参照しない**——**まだ無い**（`ledger.yaml` が `habits-tenshutsu-ran-board`
  として記録し、**未製作**と書く）。**曰く付きの参照を、在ることにしない**（`§6`）。
- 記録: `shots/habits-promo-chinatsu-s04.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。

- `SCENE`: half a step back taken from the place where the name is written, and not finished
- `CHARACTERS`: 碓氷千夏 alone in frame, standing whole at the open register — **no one else is in this work**
- `SUBJECT`: 碓氷千夏 whole in frame, her weight on the back foot, the half step unfinished
- `ACTION`: standing half a step back with the step not completed, weight on the back foot
- `LOCATION`: at the open attendance register on a desk in the staff room of a Japanese public elementary school, at its transfer column
- `LIGHT`: a fluorescent key from above the frame's edge, the page's surface carrying the glare at an angle so the ink does not resolve
- `ACCENT`: the paper white of the page as the brightest surface in the frame

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of 碓氷千夏 standing half a step back from the open attendance register with the step not finished, at the open attendance register on a desk in the staff room of a Japanese public elementary school, at its transfer column, under the fluorescent key that comes from above the frame's edge, with the paper white of the page as the brightest surface in the frame. A scene board for the master staging of this one shot, in 16:9 — the blocking, the camera and the light fixed as the standard the take must match. She is a woman of thirty-three, her identity locked to the frozen reference pair, in a washable shirt and a plain skirt with no outer garment; the nameplate is worn at the left of the chest, its printed face lost to the key. She stands whole in the frame, her weight on the back foot, the half step stopped before it finishes, her upper body upright and her face not performing. Clean anime lineart on the figure, the desk and the page, held deliberately below the light. Saturated where the light falls and deep cyan in the unlit half; paper white is the brightest surface in the frame and the warm side is reduced to skin. Hyper-detailed layered light: bloom around the fluorescent tube above, the page's surface carrying the glare at an angle to the key so the ink does not resolve, dust suspended above the desk and individually rendered rather than a flat wash, the room behind present only as lit blur, low visual density — one page, one figure, and the distance between them. The frame is at the height of the desk and slightly to the side, so that the register and the distance between it and her are held together, the desk's near edge soft in the foreground at the bottom. The register is a previous year's attendance book, open at the transfer column, one line standing in it that no one erased; the ruled columns and the writing are present and unreadable. Nothing on the desk has been touched: no pen, no other paper, and the page has not turned. No second person is anywhere in the frame: no caller, no listener, no colleague, no passer-by, and no hand but hers.

no second person in frame, no caller in frame, no listener in frame, no colleague in frame, no passer-by in frame, no legible text on any surface, no legible name text, no legible name on any in-world prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no glyph-like marks on any surface, no signature, no handwriting by the subject, no calling voice as a sound effect, no audible speech, no spoken name, no voice-over, no narration, no background music, no face before the name is called, no completed action, no finished movement, no resolved gesture, no smile, no tears, no fear, no pleading, no exaggerated expression, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket, no blazer, no outer garment, no identifying clothing, no identifying hairstyle, no identifying prop, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no watermark, no morphing or drifting facial identity, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## 記録との対応

- `unit` … 「名の書かれた紙の前に、まっすぐ立っている」→「**半歩下がり、まだ下がりきっていない。
  重心は、後ろ足に移っている。**」
- `beats` … 0-4s 紙と、その前に立つ彼女／4-7s 半歩下がる、そして下がりきらない。
  **この1枚は BEAT 2 の側である。**
- `place` / `time` … `出席簿の転出欄` / `2026年の勤務日の日中`
- `attached` … `碓氷千夏.identity`・`碓氷千夏.negatives`・`出席簿の転出欄.base`・`出席簿の転出欄.geography`
- ⚠️ **この1枚に、名札と紙が同じ枠に入る。** **身につけている名と、書かれた名**——
  **この作品で、その二つが一つの画面に並ぶのは、ここだけである。**
- ⚠️ **この1枚は全身を写す唯一の一枚である**——**ゆえに、身長と体格が固定されるのも、ここである。**
  `identity` の註（設定画・改訂稿4）が、その姿を負う。
