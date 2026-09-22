# 画像仕様 — 『未現像』第6章「二人目・三人目」 第二のショット「差し出す。そして、代償だけが像に残る」（所作 / motion / 10s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⚠️ **07 と 08 は同じ役（`所作`）であり、それは意図である**（`PLAN.md` §1 の註）——
⛔ **「手が動く1本と、手が止まる1本」。** **この1本が、動くほうである。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch06-seg02.yaml` ＋
  **既存の出力**——`migenzo-art-board/prompt.md`・同じ暗室の `migenzo-scene-board/prompt.md`・
  絹は `migenzo-kinu-character-sheet/prompt.md`（⚠️ **`_backup_20260905/` は参照しない**）
  ⚠️ **そして `脂痕` は、S01 と同じ物である**——**S01 の画像仕様が、この物の1度目を焼いている。**
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch06-seg02.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。⚠️ **まだ1枚も無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: a hand letting one small strip of film down into the developer — the one act this shot has
- `CHARACTERS`: `[絹: only her hand and forearm enter the frame — woman, late fifties, thin, hands faintly stained from developing chemicals]` — ⛔ **彼女の体も、顔も、この枠に入らない**
- `SUBJECT`: her hand holding a small strip of unexposed film just above the amber liquid, the end of it touching, the surface of the liquid just broken
- `ACTION`: letting the film down — slowly, without hurry — and the liquid's surface breaking once where the end goes in
- `LOCATION`: the darkroom of the art board — the developing tray filling the lower part of the frame, one blank white silver-gelatin sheet lying flat in that liquid with nothing floating up in it and no image on it, everything past the red light's reach sunk in near-black
- `LIGHT`: the room's constant state — one dim red safelight and the warm amber glow of the developer tray; the liquid takes the light rather than reflecting the room, so the film casts no shadow on the surface
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は 2-5s の終わりである**——**端が液に触れ、液面が割れるところである。**
⚠️ **理由**: この1本の主題は**絹の手**である（`shots/migenzo-ch06-seg02.yaml` の `motion.subject`）。
⛔ **ゆえに錨は、手を持たねばならない**——
**手を持たない錨を渡せば、生成器は手を発明する。そしてこの作品では、手の大きさと年齢が内容である。**
⚠️ **そして、この1本の唯一の動作が、この瞬間である**（「この3秒が、この1本の唯一の動作である」）。
⛔ **`unit.after`（脂痕が滲んだ状態）を焼けば、この1枚は「手の無い1本」になる**——
**滲みは 8-10s に遅れて来るものであり、§11 と §12 の散文が運ぶ。**
⚠️ **そして `脂痕` という物の錨は、S01 の画像が既に持っている。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the hand that gives something away in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The darkroom of the art board: one windowless room whose only light is a dim red safelight, the developing tray with its amber liquid filling the lower part of the frame, one blank white silver-gelatin sheet lying flat in that liquid with nothing floating up in it and no image on it and staying blank, and everything past the light's reach sunk in near-black. Into the frame from outside comes one hand and its forearm — a woman's hand, in her late fifties, thin, the fingers and the skin around the nails faintly stained from years of developing chemicals — and between the fingers it holds one small strip of unexposed film, a dry flat strip with nothing on it at all, no image and no frame and no exposure. She is letting it down into the liquid, without hurry, and at this instant the end of the strip has just met the surface: the film floats for a moment and stays, held up by the film of the liquid, and where the end has gone in the surface has broken once and is closing. The liquid takes the light rather than reflecting the room, so the strip casts no shadow on the surface. Her body and her face are not in this frame and there is nobody else in the room. `[絹: only her hand and forearm — woman, late fifties, thin, hands faintly stained from developing chemicals]`. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no person, no figure, no body, no face, no second hand, no left hand, no face in the frame, no reflection of a face in the liquid, no image on the film strip, no developed image, no frames on the strip, no sprocket holes reading as a picture, no negative with a face, no photograph in the tray, no print in the tray, no grease mark, no thumb mark, no stain, no smear, no fingerprint, no bubbles, no foam, no ripples beyond the one break, no splash, no drop of liquid in the air, no tongs, no second strip, no film canister, no reel or spool, no bottles or jars, no enlarger, no watch on the wrist, no ring, no bracelet, no nail polish, no long fingernails, no youthful hand, no clean unstained hand, no manicured hand, no glove, no sleeve with a cuff, no apron in frame, no dramatic hand modelling, no product photography of a hand, no bright evenly lit room, no dry tray, no empty tray

---

## ⛔ この1枚に、像の中身を焼かない

- ⛔ **原文が浮かばせるのは、三人の「撮るな」という顔である**（`draft_06-4`）。
  ⚠️ **その顔に鍵は無い**（`PLAN.md` §0-g）。**そして `bible.negative_base` が禁じているのは、
  娘の顔だけである**（`shots/migenzo-ch06-seg02.yaml` の申し送り(1)）。
- ⚠️ **この画像仕様の側の解き方**: **この1枚は、沈める瞬間で切る。**
  **ゆえに、浮かぶ像は、この枠にまだ無い。**
  ⛔ **`no image on the film strip` / `no developed image` / `no negative with a face` がそれである。**
  ⚠️ **動画の側の解き方は §18 の仕事である**（記録の申し送り(1)——**③ が決める**）。
- ⛔ **そして `no grease mark, no thumb mark` を落とす理由**——
  **滲みは 8-10s の出来事である。** **この1枚に置けば、この1本は最初から代償を払っている。**
  ⚠️ **代償が滲むのは、置いたあとである。**

## ⛔ トレイの紙——この白は、2026-09-23 の著者裁定で、ここに決まった

- ⛔ **初稿は「トレイに紙は無い」と読んでいた**（**動画の仕様の §5 と同じ型である**）。
- ⚠️ **根拠は3つ**——`ledger.locations.暗室.base`「**中央の現像トレイに、何も浮かんでいない
  銀塩印画紙が一枚。**」／`migenzo-art-board/prompt.md`（**同じ状態を固定している**——
  「the developer tray in the center holding a sheet of blank white silver-gelatin paper」）／
  **台帳の `props.印画紙` の一覧が、この位置（S07）を含んでいる。**
- ⛔ **ゆえに、この1枚は紙を肯定形で持つ**——**液のなかに伏せて在り、白のまま、動かない。**
  ⚠️ **そして `no paper in the tray` は、落とした。**
- ⛔ **禁じるのは「紙が在ること」ではなく、「白が主題になること」である**——
  **ゆえに `no luminous white` / `no glowing or emitting paper` は残し、
  `no print in the tray` / `no photograph in the tray` も残す**
  （**浮かぶのは、この1本ではフィルムの像である**）。

## ⛔ 「手だけ」を引く経路が、この基盤には無い

- ⚠️ **設定画は顔・体格・エプロンを持つ。** **手だけを引く欄は無い**
  （`shots/migenzo-ch06-seg02.yaml` の申し送り(2)）。
- ⛔ **ゆえに、この1枚の `CHARACTERS` は、手を言葉で書く**——
  **肯定の側が「a woman's hand, in her late fifties, thin, faintly stained」と定める。**
  ⚠️ **そして `Negative` が、若い手・手入れされた手・きれいな手を落とす**——
  **この作品の手は、二十年、薬品のなかにある手である。**
- ⛔ **`no watch on the wrist` / `no ring` も同じ理由である**——
  **この手に、身につけたものが無い**ことは、この作品では内容である。

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である。**
  ⚠️ **そして `documentary-photo` の `available natural light` は、ここでは特に害になる**——
  **この部屋の光は、状態である。**

## 記録との対応

- `unit` … `before`「**その上に、絹の手が、小さなフィルムをかざしている。**……フィルムは、
  まだ液に触れていない。乾いている。」→ `after`「**沈み終えたフィルムの上で、液面がとまっている。**
  ⚠️ そして、**像の縁に、脂痕が滲んでいる**」
- `beats` … 0-2s かざされた手とフィルム／2-5s **沈める（唯一の動作）**／
  5-8s 液面がとまり、像が浮きはじめる（**枠が持つのは像の縁である**）／8-10s **脂痕が滲む**。
  ⚠️ **この1枚が切るのは 2-5s の終わりである。**
- ⛔ **速くしない。** **急げば、それは「作業」になる**——
  **この動作は差し出しであり、作業ではない。**
- ⚠️ **`meaning-responsive` の `DELAY`（遅れ）が、この1本では 5-10s の静止である**——
  ⛔ **即答は、カットに見える**（カード）。
- ⚠️ **§12 `LIGHTING` が、この1本ではじめて「出来事」を持つ**——**だが、光源は変わらない。
  変わるのは、光の返りかたである**（滲んだ脂が、赤い光を返しはじめる）。
  ⚠️ **ゆえに、この1枚の光は、この部屋の恒常の状態のままである。**
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`・`脂痕`・`絹.identity`（**手だけである**）
  ⚠️ **`attached` の確定は ③ である。**
