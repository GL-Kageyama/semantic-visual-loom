# 画像仕様 — 『未現像』第10章「現像」 第一のショット「沈める。そして、小さな手が浮かぶ」（運動（作画） / motion / 14s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
⛔ **このショットは `mode: motion` である。そして画像は要る。**

⛔ **この1本は、この摘要版の山である**（`PLAN.md` §1「山の作り方」の第3段）。
⛔ **そして、最初に焼く2枚のうちの1枚である**——**著者の指定**（`PLAN.md` §4-c 問い10、
裁定 c）「**最初に焼く2枚は、著者の指定である——11（山）と 13（白）。**」
⚠️ **理由は「この2枚で、この作品の画面が決まるから」である。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch10-seg01.yaml` ＋
  **既存の出力**——場所は `distill-essence-engine/examples/migenzo/migenzo-art-board/prompt.md`、
  絹は同 `migenzo-kinu-character-sheet/prompt.md`、**娘は同 `migenzo-musume-character-sheet/prompt.md`**
  （⛔ **この1本は、娘の設定画を使う唯一の画像である**——下の註）、
  同じ暗室の既存ボードは同 `migenzo-scene-board/prompt.md`
  （⚠️ **`_backup_20260905/` は参照しない**——依頼の指定である）
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch10-seg01.yaml`（`key_image`）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）。
  ⚠️ **第一世代が在った**——`10_01_ChatGPT Image 2026年9月23日 02_10_50.png`
  （2026-09-23、著者が投入。**参照画像は添付していない**——下の節のとおりである）。
  ⚠️ **そして、いま作業ディレクトリに無い**（**実測**、2026-09-24）。**その削除は `git status` に出ない**（追跡されていなかった）。
  ⚠️ **予備が在る**——`10_01_ChatGPT Image 2026年9月23日 03_40_41.png`（2026-09-23、著者が投入）。
  ⛔ **著者裁定（2026-09-24）——この1枚を採用する。** **選んだのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `documentary-photo` —— 5つの穴（`SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`）

⚠️ **`SCENE`・`ACTION`・`LIGHT` は両方のカードに同名で在る**——**同じ値が両方の穴に入る。**
5＋5＝10 ではなく、**和は7**である。

- `SCENE`: the sinking — one strip of film let down into the developer, and what the liquid hands back in its place
- `CHARACTERS`: `[絹: the back of a woman, late fifties, thin, black blouse, seen from behind, running away]` and `[娘: a small child's hand only — the palm and fingers spread flat over the round black mouth of a lens]` — ⛔ **両方とも、像のなかに居る。** **この部屋には、誰も居ない**（沈め終われば、絹の手は枠から出ている）
- `SUBJECT`: a wet silver-gelatin print lying in the amber developer with an image floating up in it — a back turned away and running, and a small hand covering the round black mouth of a lens
- `ACTION`: the image coming up out of the white, its outline settling — the shoulder line, then the arm, then the open hand, then at the near edge the small hand over the lens, stopping one finger's width short of it
- `LOCATION`: the darkroom of the art board — one windowless room, the developing tray at its center, everything past the red light's reach sunk in near-black
- `LIGHT`: the room's constant state — one dim red safelight and the warm amber glow of the developer tray; no time of day and no directional light. ⛔ **像のなかのいちばん明るい線は、レンズと指のすきまから漏れる赤いひとすじである**
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は `unit.after` である**——**この1本の答えそのものだからである。**
⚠️ **理由**: `KEEP` は**フィルムの幅と、手の大きさ**である（`shots/migenzo-ch10-seg01.yaml`）。
⛔ **幅は、画面のなかの大きさでしかない。** **ゆえに錨は、着地点を焼かねばならない**——
**動画はフィルムから始まり、この1枚の幅と、この1枚の手の大きさへ、着地しなければならない。**
⚠️ **`FROM` を焼けば、この1本は「その幅から始まって、どこかへ行く」1本になる。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the sinking of the film in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. In the darkroom of the art board — the one windowless room whose only light is a dim red safelight and the warm amber glow of the developer tray, everything outside that island sunk into near-black — one wet silver-gelatin print lies in the amber liquid, its full flat even width held in the frame, and inside the liquid an image has come up in it. In the image: a woman's back, turned away and running, with one arm and an open hand; and nearer than the back, at the near edge of the image, a small child's hand laid flat over the round black mouth of a lens, the palm and the fingers spread, the hand stopped one finger's width short of the lens, and through that one gap a single strand of red light comes in and is the brightest line in the picture. The place where the child's face would be is plain white, and that white has no edge: it dissolves into the rest of the image with no line drawn between them, and there is no eye, no nose and no mouth in it. The image is still wet and floating, the outlines not yet hardened, the white still moving under the surface. The width of the print is even from edge to edge and the small hand is small against the lens: those two sizes are the two things that must be the same at the beginning and at the end. `[絹: woman, late fifties, thin, black blouse, seen from behind, no face]` — inside the image, her back only. `[娘: a small child's hand only, the palm and fingers spread flat over the round black mouth of a lens]` — inside the image, the hand only; the rest of her is not in the picture and her face is not in the picture. No person stands in the room. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board, the tray filling the space the art board left open. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no glossy photo paper, no digital image on the paper, no glowing or emitting paper, no visible fingerprint ridges, no forensic texture, no legible handprint, no eyes in the white, no face in the white, no line drawn around the white, no second face, no adult hand on the lens, no gripping or clutching hand, no tense clawed fingers, no fingers closed over the lens, no lens covered completely, no wound, no blood, no body, no child in the room, no figure in the room, no hand at the tray, no tongs, no clean dry print, no dry paper, no bubbles, no number of bubbles, no second image, no reflection of the room in the liquid, no bright evenly lit room, no portrait lighting, no soft studio falloff, no smiling, no reading of the image as a photograph of a photograph, no visible camera body, no brand of camera

---

## ⛔ この1枚だけが、娘の設定画を使う

- ⚠️ **`ledger.characters.娘.identity` の錨は「小さな手」だけである**（`PLAN.md` §0-g、2026-09-23 裁定）。
  **ゆえに、この1枚が設定画から取るのは、手の形だけである。**
- ⛔ **そして、あの設定画は日本語の註記を3つ持ち、
  `no heavy film grain` / `no shallow depth of field` / `no yellow cast` を宣言する**——
  **暗室の逆である。** ⚠️ **この作品の暗室の画は、その3つを全部持つ。**
  **⛔ 動画側の指定が勝つ**（`shots/migenzo-ch10-seg01.yaml` の申し送り(3)）。
  ⚠️ **ゆえに、この1枚の `Negative` に、その3節を写さない。**
  **写せば、この1枚はこの作品の様式を自分で禁じる。**
- ⚠️ **そして、`no small hand pressing the lens` を、この1枚の `Negative` に置かない。**
  ⛔ **この1本で、その禁制が落ちる**（`ledger.disclosure`、`negative: changed`）——
  **置けば、この1枚は自分の主題を禁じる。** **動きかたは「削除」である**（入れ替えではない）。
- ⛔ **落としたぶんの危険は、逆側に立つ**——**手が主題になれば、こんどは手が描かれすぎる。**
  ⚠️ **ゆえに肯定形の側が手を定める**——**開いた手のひら、指を広げたまま、レンズの直前で止まる。**
  **禁制の側は「握る」「つかむ」「爪を立てる」「完全にふさぐ」を落とす。**
- ⚠️ **`no image on the unexposed film` は、この1枚では不活性である**——**枠にフィルムが無い。**
  ⛔ **だが床からは外さない**（`L21` が両経路で要求する）。
  ⚠️ **記録の申し送り(4)は動画の禁制集合についてのものであり、③ が扱う。**

## ⚠️ 像のなかの白は、否定的でなく**内容**である

- ⛔ **`draft_10-2` が、顔の場所を白として書いている**——
  「**娘の顔は、どこにも浮かばない。娘は映っていない。顔があるはずの場所が、白い。
  その白のなかに、眼も、鼻も、口も、浮かばない。**」
- ⚠️ **ゆえに、この1枚の肯定文は、その白を明示する**——**消すのではなく、書く。**
  ⛔ **`no fully rendered face of the daughter` は、それでも13本すべてに残る**（`bible.negative_base`）。
  ⚠️ **禁制と内容が食い違わないのは、肯定文が「線のない白」を名指しているからである。**
- ⚠️ **`no fully rendered face of the daughter` を、この1枚の唯一の顔の指示にしない**——
  **否定形は空欄になり、生成器が衣装で埋める。** **肯定の側が「逃げる背中」を名指している。**

## ⚠️ `Not photorealistic` を、ここに写してはならない

- ⛔ **既存ボードの `Merged` の末尾の否定列にあるあの句を、この1枚は持たない**——
  **裁定（2026-09-23、著者）「入れない（推奨）」。** ⚠️ **根拠は `migenzo-ch01-seg01.md` の同じ節である**
  （あの句は同じプロンプトの `documentary photograph` と自己矛盾し、隣は `no smooth CGI` である）。
- ⛔ **様式カードの `available natural light` も写さない**——**この部屋の赤い安全光は到着しない。
  時刻を持たない、その場所の恒常の状態である。**

## 記録との対応

- `FROM` / `TO` / `KEEP` / `TRIGGER` … `shots/migenzo-ch10-seg01.yaml` の4語。
  ⚠️ **この1枚が焼くのは `TO` である。** ⛔ **`TRIGGER`（沈めること）は、この枠に残っていない。**
- `unit` … `before`「液面の上にかざされた、幅の見えているフィルム」→
  `after`「液のなかに、像がある。濡れた印画紙のうえに、逃げる背中と、レンズを押さえる小さな手。
  娘の顔の場所は、白い。」
- `beats` … 0-3s 宙づり／3-5s **沈める（`TRIGGER`、一度だけ）**／5-12s **`CORE`（7秒・50%）**／
  12-14s 像はまだ濡れている。⚠️ **この1枚が切るのは 5-12s の終わりである。**
  ⛔ **浮かぶ順序に眼を置かない**（`draft_10-2`「**眼が浮かぶ。像のなかに、眼はない。**」）。
- ⚠️ **泡を、この1枚にも置かない**——**この作品の画面に在ってよいものは、
  液面と、沈むものと、浮かぶものである**（`shots/migenzo-ch10-seg01.yaml` の註）。
  ⛔ **ゆえに `Negative` が `no bubbles` を落とす。** **数えれば、02 の反復になる。**
- ⚠️ **この1枚に、絹の顔も、絹の手も無い**——**この摘要版の山は、彼女の中ではなく、液面の上にある。**
- `place` / `time` … `最後の暗室` / 時刻を持たない
- `attached`（見込み）… `最後の暗室.base`・`最後の暗室.geography`・`未露光のフィルム`・`印画紙`・
  `絹.identity`・**`娘.identity`（この1本で初めて立つ）**
  ⚠️ **`attached` の確定は ③ である。** ここに在るのは②の見込みである。
