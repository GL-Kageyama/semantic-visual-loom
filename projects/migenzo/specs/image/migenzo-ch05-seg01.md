# 画像仕様 — 『未現像』第5章「追う者」 第一のショット「見られる側に立つ」（反応 / motion / 9s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⛔ **この1本の主題は、絹の反応であって、来る者ではない。**
⚠️ **そして、この1本に演劇を置かない**（依頼——**「単純な演出」**）。
⛔ **ゆえに、この1枚にあるのは「首が回ったこと」と「眼が止まったこと」だけである。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch05-seg01.yaml` ＋
  **既存の出力**——`migenzo-art-board/prompt.md`・同じ暗室の `migenzo-scene-board/prompt.md`・
  **絹は `migenzo-kinu-character-sheet/prompt.md`**、**盗人は `migenzo-nusubito-character-sheet/prompt.md`**
  （⚠️ **`_backup_20260905/` は参照しない**）
  ⛔ **盗人の設定画は「眼だけが実である」と宣言する**——**この1本が、その宣言を使う最初の1本である。**
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch05-seg01.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。⚠️ **まだ1枚も無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: a woman who has spent twenty years not being looked at, being looked at — and her eyes coming back from the side they always went to
- `CHARACTERS`: `[絹: woman, late fifties, thin, short black hair faintly streaked with grey gathered loosely at the back, a calm sunken-eyed face, a black apron over a black blouse]` in the near frame, and `[盗人: a grown figure standing in the dark at the threshold, whose face the darkness does not describe — the only thing that reads is the eyes, a child's eyes, catching the red light]` — ⚠️ **盗人は閾を越えない**
- `SUBJECT`: 絹's face in the near foreground with her eyes come back and resting forward, and beyond her, in the open doorway, a figure stopped at the threshold with two points of red light where its eyes are
- `ACTION`: her eyes no longer going aside — they stop, and that is all that happens
- `LOCATION`: the doorway of the darkroom of the art board — the door standing open, and the outside giving no light at all
- `LIGHT`: the room's constant state — one dim red safelight that reaches only the inside, and the warm amber glow of the developer tray; the two points beyond the threshold are the safelight coming back off the eyes, not a light of their own
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は `unit.after` である**——**絹の眼が、戻っているところである。**
⚠️ **理由**: この1本の到達は 6-9s にあり、**この1本の向きが変わったことを読ませるのは、
その1点だけである**（`PLAN.md` §2「**絹が壊してきた人生が、絹のほうへ歩いてくる**」）。
⛔ **`before` を焼けば、この1枚は「二十年、横を向いている女」になる**——
**それは 01〜04 が既に持っている画であり、この1本の画ではない。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the moment the looking changes direction in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The doorway of the darkroom of the art board: one windowless room whose only light is a dim red safelight, the door standing open, and outside the door nothing at all — no corridor, no street, no light. In the near part of the frame, close to the camera, the face of a woman in her late fifties: thin, short black hair faintly streaked with grey gathered loosely at the back, a calm sunken-eyed face, a black apron over a black blouse. Her head has turned and her eyes have come back from the side they always went to; they are resting now, forward, on the doorway, and she is not moving. Beyond her, out in the open doorway, a grown figure has walked up and stopped exactly at the threshold and does not cross it: the darkness does not describe it, there is no face to read, no clothing to read, no body to read — the only thing that comes out of that darkness is the eyes, two points where the red safelight returns off them, and they are a child's eyes. Nothing else in the frame moves; this is two people holding still, one looking and one being looked at. `[絹: woman, late fifties, thin, short black hair faintly streaked with grey gathered loosely at the back, a calm sunken-eyed face, a black apron over a black blouse]` — the figure whose identity is locked to the frozen setting sheet. `[盗人: a grown figure at the threshold, undescribed by the darkness; only the eyes read, and they are a child's eyes]`. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no readable face on the figure at the threshold, no facial features on the figure, no eyes other than the two points, no glowing eyes, no luminous or emitting eyes, no light of their own, no sunglasses, no goggles, no mask, no hood over the face in view, no child's body, no child in frame, no small stature, no youthful build, no second face, no third person, no silhouette of a third person, no open door with daylight behind it, no corridor, no street, no room beyond the door, no lamp beyond the door, no doorway light spill, no light from outside, no window light, no torch, no bright evenly lit room, no dramatic tension lighting, no low angle, no confrontation staging, no standoff composition, no mirrored symmetry, no dramatic shadow on the wall, no raised hand, no reaching hand, no weapon, no bag, no coat collar turned up, no hat, no smile, no angry expression, no expression staged for the camera

---

## ⛔ 盗人の顔は「描かない」——`bible.negative_base` は、この者を禁じていない

- ⛔ **基盤の核2節は、娘の顔を禁じているだけである**（`bible.negative_base`）。
  ⚠️ **この者の禁止は、この1枚が自分で持つ**（`shots/migenzo-ch05-seg01.yaml` の申し送り——
  「**この作品の否定集合に「顔を描くな」が要る**」）。
- ⚠️ **そして、この1枚は否定形だけで書かない。** **肯定の側が、暗さを名指している**——
  「**the darkness does not describe it, there is no face to read**」。
  **読めないことは、この作品では内容である**（`no featureless blank face` を hakuchizu が
  使ったのと同じ形——**空白の面も、顔である**）。
- ⛔ **ゆえに `no glowing eyes` が在る。** **二点は、赤い光が返っているところである**——
  **眼が光っているのではない。** **発光させれば、この者は「超常の存在」になる。**
- ⛔ **そして `no light from outside` が在る**——**外は、この作品に無い**（`PLAN.md` §0-e）。
  **戸口の向こうは、暗さであって、外ではない。**

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である。**

## 記録との対応

- `unit` … `before`「閾のところに、まだ、だれも居ない。……**彼女の眼は、横へ逸れている**」
  → `after`「暗さのなかに**ひとつの体**が立ち、**閾で止まっている。**
  ⛔ **顔は描かれない。赤い光を返しているのは、眼の二点だけである。**
  **そして絹の眼が、戻っている。逸れずに、その二点のほうを向いている。**」
- `beats` … 0-3s 開いた戸口と暗さ、**眼は横へ逸れている**／3-6s **体の輪郭が立ち、閾で止まる**／
  6-9s **絹の眼が戻り、止まる。** ⚠️ **この1枚が切るのは 6-9s である。**
- ⛔ **この1本で起きることは、首が回ることと、眼が止まることだけである。**
  ⚠️ **「受け止める」を、大きな動作にしない**——**大きければ、それは決意の演技になる。**
- ⚠️ **この部屋の地理の法**——**外は入らない。来る者は閾を越えない。**
  ⚠️ **ゆえに、この1枚の立っている位置は、この1本の意味そのものである。**
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`・`絹.identity`・`盗人.identity`
  ⚠️ **`attached` の確定は ③ である。**
