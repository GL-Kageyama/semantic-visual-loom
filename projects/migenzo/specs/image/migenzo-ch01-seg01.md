# 画像仕様 — 『未現像』第1章「現像」 第一のショット「白い紙から像が浮かび、その代償が像の縁に脂として残る」（質感 / motion / 10s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⛔ **この紙は、この作品で最初の画像仕様である。** `projects/migenzo/specs/image/` は
**これまで空だった。** ゆえに `L18` の「`key_image` が読めない」は**13本ぶん在り、この1本で1つ減る。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch01-seg01.yaml` ＋
  **既存の出力**——場所は `distill-essence-engine/examples/migenzo/migenzo-art-board/prompt.md`、
  絹は同 `migenzo-kinu-character-sheet/prompt.md`、同じ章の既存ボードは同 `migenzo-scene-board/prompt.md`
  （⚠️ **`_backup_20260905/` は参照しない**——依頼の指定である）
- 投入する文: **下の節の1段落目が `Prompt` であり、エンジンの出力であって、`chatgpt-image-2.5` へ
  投入する正典である。****2段落目が `Negative` である**
- ⚠️ **下の7欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`REF_FORMAT` と `REF_STYLE` が「どのカードの穴か」を名乗る。** `L22` がそれを読み、
  **名乗ったカードが実際にその穴を宣言しているか**を確かめる——**名乗りは宣言であって、一致ではない。**
  ⚠️ **この組では、`L22` は2件鳴る**（実測、`PLAN.md` §0-d・§4-d-2 の F2）——
  **`missing: ACCENT`／`extra: ASPECT・LIGHT・SCENE`。** ⛔ **この赤は承知のうえである**——
  **`L22` はカードとエンジンの表を突き合わせており、この仕様の欄を1つも読んでいない。**
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
- 記録: `shots/migenzo-ch01-seg01.yaml`
- 生成物の置き場: このディレクトリ。⚠️ **まだ1枚も無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `documentary-photo` —— 5つの穴（`SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`）

⚠️ **`SCENE`・`ACTION`・`LIGHT` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋5＝10 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the first development — a line stands up in the white, the eyes come up, the mouth closes, and the cost of it stays on the image as a mark of grease
- `CHARACTERS`: `[絹: woman, late fifties, thin, short black hair faintly streaked with grey gathered loosely at the back, a calm sunken-eyed face, a black apron over a black blouse, hands faintly stained from developing chemicals]` — **only her right hand and forearm enter the frame**, the fingertips holding the near edge of the print; her face is not in this frame
- `SUBJECT`: the wet silver-gelatin print lying in the amber developer with a face coming up in it, and the thumb's grease mark left on the image below the eye
- `ACTION`: standing at the tray holding the print by its edge, having just lifted it clear of the liquid, **not looking at the eyes that have come up**
- `LOCATION`: the darkroom of the art board — one windowless room, the developer tray at its center, everything past the red light's reach left near-black
- `LIGHT`: the room's constant state — one dim red safelight and the warm amber glow of the developer tray; no time of day and no directional light
- `ASPECT`: 16:9, landscape

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the first development of the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. In the darkroom of the art board — the one windowless room whose only light is a dim red safelight and the warm amber glow of the developer tray, the rest of the room sunk into near-black — a wet silver-gelatin print is held just clear of the amber liquid by a hand that enters the frame at its near edge, the fingers pinching the corner, and in the print a face has come up: the outline first, then the eyes open and looking away to one side, then a mouth that closed on something it had started to say. Below the eye, on the image itself, one thumb's mark of grease is left and has not been wiped, and it catches the red light. The hand's owner stands at the tray with her face outside the frame, and she does not look at the eyes that have come up — the picture looks at them and she does not, and that difference is the whole surface of this board. The white of the paper is silver-white and not the white of paper: it stays silver-white and is not stained red or amber. The blocking, the camera and the light fixed as the standard every cut of this scene must match: the tray and the print as the subject, the one hand at its edge, the safelight as the only light, the room otherwise still. One scene, one staging. `[絹: woman, late fifties, thin, short black hair faintly streaked with grey gathered loosely at the back, a calm sunken-eyed face, a black apron over a black blouse, hands faintly stained from developing chemicals]` — the figure, whose identity is locked to the frozen setting sheet. The one face that has come up in the print is a woman's face turned away, an ordinary face at the moment of refusing something, and it is not the daughter. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, blown highlights on the white paper, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board, the hand filling the space the art board left open. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no glossy photo paper, no digital image on the paper, no glowing or emitting paper, no visible fingerprint ridges, no forensic texture, no legible handprint, no small hand pressing the lens, no youthful face for 絹, no clean unstained hands, no smiling expression, no second figure, no face in the frame, no open drawer, no second print, no hand touching the eyes in the image, no wiping of the mark, no portrait lighting, no glossy print surface, no bright evenly lit room

---

## ⚠️ `Not photorealistic` を、ここに写してはならない

- ⚠️ **既存のボード（`migenzo-art-board`／`migenzo-scene-board`）の `Merged` は、
  末尾の否定列に `Not photorealistic` を持つ。** ⛔ **この1枚は持たない**——
  **裁定（2026-09-23、著者）「入れない（推奨）」。**
- ⚠️ **根拠は実測である**（`bible.negative_base` の註）——**様式カードの Negative は
  `not photorealistic` を持たず**、**人物設定画は `Photorealistic rendering` を肯定の先頭に置く。**
  そして**あの句は、同じ1本のプロンプトの `documentary photograph` と自己矛盾する**
  （`bible.light` の註が同じ衝突を扱っている）。
- ⚠️ **採った読み**: あの句の隣は `no studio lighting`・`no perfect focus`・`no smooth CGI`・
  `no digital polish` である——**ゆえに意図は「CG の滑らかさ」であり、実写ではない。**
  **この1枚は、CG の滑らかさだけを禁じる**（`no smooth CGI`・`no 3D render`・`no digital polish`）。
- ⛔ **食い違いの在り処は distill 側のボードであり、この作品は触れない**（読み取りのみ。
  申し送りは `PLAN.md` §4-b）。

## ⚠️ 様式カードの `available natural light` を、ここに写してはならない

- `documentary-photo` の忠実の錨は `Available natural light, no artificial setup` と言い、
  **`Motion character` は「人工の光源が到着することは別の様式である」と註する。**
- ⛔ **この部屋の赤い安全光は、到着しない。** **時刻を持たない、その場所の恒常の状態である**
  （`bible.world.visual_language.light`——出典は `migenzo-art-board` の
  「no time of day and no directional light — the **"state" this board fixes is the light itself**」）。
- ⚠️ **ゆえに、この1枚の `LIGHT` は「自然光」ではなく「状態」である。** **写せば、部屋が昼になる。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`WAN 3.0`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**空白の面**と**偽の字**——を禁じているのは、**この段落である。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の27節**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。**

## 記録との対応

- `unit` … 「液面に沈んだ、何も浮かんでいない白い印画紙」→
  「線が立ち、眼が浮かび、口元が閉じ、**眼のすこし下に親指の脂痕が一つ残っている**」
- `beats` … 0-3s 待ち時間／3-5s **輪郭**／5-7s **眼**／7-10s **口元・引き上げ・脂痕。**
  ⚠️ **この1枚が切るのは 7-10s の瞬間である**——**`unit.after` そのものであり、このショットの見せ場である。**
  ⛔ **眼は、まだ横へ逸れている**（`draft_01-2`）。
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`・`印画紙`・`脂痕`・`絹.identity`・`絹.negatives`
  ⚠️ **`attached` の確定は ③ である。** ここに在るのは②の見込みである。
- ⚠️ **`no small hand pressing the lens` が、この1枚にも掛かる**——**01〜10 の10本が負う床である**
  （幹の逆転を明かさない。`PLAN.md` §2）。⛔ **11 で落ちる。**
- ⚠️ **この1枚の像の顔は、娘ではない。** `PLAN.md` §0-b——**01 で浮かぶのは「拒んだ女」の像である**
  （`話割り.md` 1-2）。⛔ **ゆえに `no fully rendered face of the daughter` は、
  この1枚では「像の顔を空白にせよ」という指示ではない**——**否定形は空欄になり、生成器が衣装で埋める。**
  ⚠️ **肯定の側が「横へ逸れた女の顔」を名指している**（上の `Prompt`）。
