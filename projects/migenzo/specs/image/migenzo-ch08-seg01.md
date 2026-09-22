# 画像仕様 — 『未現像』第8章「対峙」 第一のショット「背で受けて、息をひとつ、置く」（対話 / still / 8s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⛔ **この1本の仕事は、語られていることに、時間を与えることである。**
⚠️ **台詞は無い**（§0-f）。⛔ **ゆえに、この1本の「対話」は、沈黙の形をしている。**
⛔ **そして、語っている者は、顔を持たない**——**顔が無いので、口は動かない。**
⚠️ **ゆえに、この1本に、うなずきも、まばたきの演技も置かない。**

⛔ **この1本の変化は、ひとつだけである**——**二十年、浅く保たれてきた息が、ひとつ、置かれる。**
**肩が、わずかに下がる。** ⛔ **背は、曲がらない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch08-seg01.yaml` ＋
  **既存の出力**——`migenzo-art-board/prompt.md`・同じ暗室の `migenzo-scene-board/prompt.md`・
  **絹は `migenzo-kinu-character-sheet/prompt.md`**、**盗人は `migenzo-nusubito-character-sheet/prompt.md`**
  （⚠️ **`_backup_20260905/` は参照しない**）
  ⛔ **盗人の設定画は「眼だけが実である」と宣言する**——**05 と同じ申し送りを、この1本も負う。**
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch08-seg01.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。⚠️ **まだ1枚も無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: the one who has spent twenty years not being answered to, standing with her back to us, while the answer is spoken to her back
- `CHARACTERS`: `[絹: woman, late fifties, thin, short black hair faintly streaked with grey gathered loosely at the back, a black apron over a black blouse — seen only from behind, her back to the camera]` in the near frame, filling it, and `[盗人: a grown figure standing in the dark at the threshold, whose face the darkness does not describe — the only thing that reads is the eyes, a child's eyes, catching the red light]` — ⚠️ **盗人は閾を越えない**
- `SUBJECT`: a woman's back filling the near part of the frame, the red safelight catching the right-hand edge of it and leaving the rest in the dark, and past her, in the open doorway, darkness with two points of returned red light in it
- `ACTION`: nothing — the back holds still and the shoulders are held a very little raised, the way a breath is held when it has been kept shallow for twenty years
- `LOCATION`: the doorway of the darkroom of the art board — the door standing open, and the outside giving no light at all
- `LIGHT`: the room's constant state — the dim red light of a safelight that stands outside the frame, whose right-hand edge catches the edge of her back and does not reach her front, and the warm amber glow of the developer tray further off; ⛔ **枠が持つのは光そのものであって、灯ではない**; the doorway is not lit
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は `unit.before` である**——**肩が、まだ、上がったままになっているところである。**
⚠️ **理由は2つある。**
- ⛔ **（1）「わずかに下がった肩」は、1枚では「肩」としか読めない。** **差は、動く前後でしか無い。**
  **ゆえに、この錨が `after` を焼いても、この1本は何も得ない**——**同じ背中の画になる。**
- ⛔ **（2）この1本は「緩む」1本である。そして、緩みは、保たれているものが先に在って初めて読める。**
  **保たれているものを画面から外せば、8秒はただの背中になる。**
⚠️ **ゆえに錨は、`draft_01-1` の「その数えかたが、二十年、変わらない」の側を焼く。**
⛔ **そして、動画はこの保持から始まり、8秒目で一度だけ、それを緩める。**
**錨が緩みを先に焼けば、動画は「肩を上げる」ところから始めねばならない**——
**それは、この作品が主題にしている習慣を、生成器に発明させることである。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the silence that is addressed to someone in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. One single photograph, one single view: this whole frame is one moment in this room, and there is no second picture in it, no panel, no grid and no strip of separate exposures. The doorway of the darkroom of the art board: one windowless room lit by a safelight that stands outside the frame — what is in the frame is the red light it makes, and not the fixture that makes it — the door standing open, and outside the door nothing at all — no corridor, no street, no light. Filling the near part of the frame, close to the camera, is the back of a woman in her late fifties — thin, short black hair faintly streaked with grey gathered loosely at the back, a black apron over a black blouse — standing with her back to us, so that what the frame is of is the back of a plain black blouse and a black apron and the fall of her hair, and nothing of her front. The red safelight catches the right-hand edge of her back and no more, leaving the rest of her in the dark. Her back is straight and she is not moving, and her shoulders are held a very little raised, the way a person holds a breath that has been kept shallow for twenty years and has not yet let it down. Past her, out in the open doorway, there is darkness, and in that darkness there are two points where the red light comes back off something, and they are the only thing that reads as being there at all: two points, a child's eyes, and the darkness does not describe the rest of the figure — no face, no clothing, no body. Nothing is being said aloud in this room, no one speaks, and there is no mouth to read anywhere in this frame; what is happening is that something is being said to this back, and the back is receiving it. `[絹: woman, late fifties, thin, short black hair faintly streaked with grey gathered loosely at the back, a black apron over a black blouse — the figure whose identity is locked to the frozen setting sheet, photographed from behind only]`. `[盗人: a grown figure standing in the dark at the threshold, undescribed by the darkness; only the eyes read, and they are a child's eyes]`. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no turned head, no looking back, no face in profile, no three-quarter view, no face in frame, no face visible, no face in a mirror, no reflection of a face, no over-the-shoulder framing, no portrait framing, no close-up on the back, no light reaching her front, no fill light on her front, no body lit from the front, no readable face on the figure at the threshold, no facial features on the figure, no eyes other than the two points, no glowing eyes, no luminous or emitting eyes, no light of their own, no sunglasses, no goggles, no mask, no hood over the face in view, no child's body, no child in frame, no small stature, no second figure at the threshold, no third person, no fourth person, no group at the threshold, no crowd, no open door with daylight behind it, no corridor, no street, no room beyond the door, no lamp beyond the door, no doorway light spill, no light from outside, no window light, no torch, no pocket in frame, no hand in a pocket, no crossed arms, no folded arms, no hands raised, no gesturing, no pointing, no nodding, no head lowered, no shrugged shoulders, no hunched back, no bent back, no slumped posture, no visible breath, no mist, no dramatic tension lighting, no low angle, no confrontation staging, no standoff composition, no mirrored symmetry, no dramatic shadow on the wall, no weapon, no bag, no coat collar turned up, no hat, no smile, no angry expression, no expression staged for the camera, no contact sheet, no sheet of frames, no grid of panels, no multiple panels, no split frame, no diptych, no triptych, no collage, no filmstrip layout, no border between images, no white border around the picture, no second view, no several images in one frame, no light source visible in frame, no safelight lamp in frame, no lamp, no bulb, no bare light source

---

## ⛔ 背中を撮る——この基盤に、背中だけを引く経路が無い

- ⚠️ **設定画は顔を持つ。背中を撮るための欄は、この基盤に無い**
  （`shots/migenzo-ch08-seg01.yaml` の申し送り）。
- ⛔ **ゆえに、この1枚は、肯定の側で方向を名指す**——
  「**standing with her back to us, so that what the frame is of is the back of a plain black blouse
  and a black apron and the fall of her hair, and nothing of her front**」。
- ⚠️ **そして、この1枚は `no turned head` / `no looking back` / `no face in frame` を持つ。**
  ⛔ **振り返りの構図は、この種の画で最も出やすいものであり、そして
  もっとも高くつくものである**——**一度でも顔が出れば、この作品の禁制が破れる。**
- ⚠️ **そして `no body lit from the front` の理由**——**照らせば、顔が描かれる**
  （`PLAN.md` §2「**見せるには体を照らす必要があり、照らせば顔が描かれる**——**05 と 09 が、
  まさにそれを避けている**」）。⛔ **この1本は、その2本のうちの1本である。**

## ⛔ ポケットの手は、この摘要版に無い

- ⚠️ **原文は書いている**——`draft_08-1`「**握っている手のかたちが、ポケットの布のうえに、
  すこし浮き上がっている。……指の節が、四つ、浮いている**」。
- ⛔ **この摘要版は、それを採らない**（`PLAN.md` §2——「**この摘要版に無い**」）。
  **理由は、上の「照らせば顔が描かれる」と同じ1点である。**
  ⚠️ **これは損失である**（`PLAN.md` §2 がそう書いている）。**損失を、この1枚で埋めない。**
- ⛔ **ゆえに `no pocket in frame` / `no hand in a pocket` が、この1枚に在る。**
  **ポケットは、この作品の画面に無い。**

## ⛔ 語っている者を、演じさせない

- ⛔ **この1本には台詞が無く、語っている者は顔を持たない。**
  ⚠️ **ゆえに、この1本が置けるのは、時間だけである。**
- ⚠️ **この1枚の側の解き方**: **暗さが、その者を記述しないこと**——
  「**the darkness does not describe the rest of the figure — no face, no clothing, no body**」。
  ⛔ **読めないことは、この作品では内容である**（05 と同じ形——**空白の面も、顔である**）。
- ⛔ **そして `no light of their own` が在る**——**二点は、赤い光が返っているところである。**
  **眼が光っているのではない。** **発光させれば、この者は「超常の存在」になる。**

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である。**

## ⛔ 実測（2026-09-23、n=1）と、焼き直しの2点（著者裁定）

- ⚠️ **焼かれた1枚**——`08_01_*`。**見えたままを書く。**
- ⛔ **この1枚は、キー画像として使えない**——**4分割のコンタクトシートである。**
  ⚠️ **芯は上段に在る**（**背中・赤い縁・戸口の二点**）。**だが、1枚ではない。**
- ⛔ **原因は、肯定の側に「1枚であること」が1節も無かったことである。**
  ⚠️ **この仕様は `A scene board for ...` で始まる**——
  **`scene-board` は「板」であり、生成器はそれを「複数のコマを並べた板」と読んだ。**
  ⛔ **他の12枚ではそう読まれなかったが、それは偶然である。**
- ⛔ **直したのは2点である。**
  **（1）「1枚の写真である」ことを、プロンプトの冒頭と末尾の両方で肯定形で書いた**
  （**no panel ではなく、one single view fills the frame である**）。
  ⚠️ **`Negative` にも `no contact sheet` / `no grid of panels` / `no split frame` /
  `no white border around the picture` ほかを足した**——**肯定の裏である。**
  **（2）灯を枠の外へ出した**（**02・06-1・06-2・07 と同じ欠陥である**）。
- ⚠️ **この4分割は、4つのコマが互いに少しずつ違う。** **ゆえに、切り出しても使わない**——
  **どれが「この1本の枠」かを、② は決められない。**

## 記録との対応

- `unit` … `before`「手前いっぱいに、絹の背がある……**背は、まっすぐである。**
  **肩が、わずかに、上がったままになっている**」→ `after`「**同じ枠。同じ背。**
  ⚠️ **変わったのは、肩である**……**二十年、浅く保たれてきた息が、ひとつ、置かれる。**
  ⛔ **背は、曲がらない。**」
- `beats` … 0-3s 背と赤い光の縁、向こうの暗さと二点（**言葉は既に始まっている**）／
  3-6s **動かない（この3秒が本体である）**／6-8s **肩が、ひとつ、下がる。**
  ⚠️ **この1枚が切るのは 0-3s である**——**保持の側である。**
- ⛔ **動きは、この1本にひとつも無い。** ⚠️ **動くのは、赤い安全光のゆらぎと、
  二点が返す光のわずかな移ろいだけである。**
  ⛔ **そして、この1枚は、その移ろいを焼かない**——**焼けば、二点が「表情」になる。**
- ⚠️ **この部屋の地理の法**（`ledger.暗室.geography`）——**外は、この画の外に無い。**
  **戸口の向こうは、暗さであって、外ではない。**
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`・`絹.identity`・`盗人.identity`
  ⚠️ **`attached` の確定は ③ である。**
  ⛔ **そして 05 と同じ申し送りを、③ はもう一度負う**——**`盗人.identity` を引くなら、
  「眼だけが錨である」ことを ③ が負う**（`bible.negative_base` の核2節は**娘の顔**を
  禁じているだけであり、**この者を禁じていない**）。
