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
- ⛔ **添付する参照画像（著者裁定、2026-09-23）**:
  `distill-essence-engine/examples/migenzo/migenzo-kinu-character-sheet/ChatGPT Image 2026年9月5日 07_16_48.png`
  ——⛔ **この13本で、絹の設定画が付くのは、この1枚だけである**（`PLAN.md` §4-c 問い14）。
  ⚠️ **根拠**——**13本のうち、顔が枠に入るのはこの1本だけである**（実測。`PLAN.md` §4-c 問い11 の
  理由 (c)）。**ゆえに、同一性が要るのも、この1本だけである。**
  ⛔ **そして他の12本には付けない。**
  ⚠️ **裁定の文面との関係を申告する**——問い11 は「**人物の設定画は、付ける先ではない**」と書いた。
  ⛔ **著者は 2026-09-23 の問い14 で、05 を例外として承認した**（**13＝アートボード／05＝設定画**）。
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch05-seg01.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。
  ⚠️ **第一世代が在った**——`05_01_ChatGPT Image 2026年9月23日 02_28_36.png`
  （2026-09-23、著者が投入。⛔ **設定画を添付して焼かれた**——
  `生成時参照イラスト/05_01/` の1枚が 02:24 に置かれ、この焼きは 02:28 である）。
  ⛔ **これは焼き直しと裁定された**（2026-09-24、著者）。⚠️ **そして、もう作業ディレクトリに無い**
  （**実測**、2026-09-24——`git status` が `D` を出す）。⛔ **この削除は、この稿では触っていない。**
  ⚠️ **第二世代が在る**——`05_01_ChatGPT Image 2026年9月24日 01_23_50.png`（2026-09-24、焼き直し）。
  ⛔ **著者裁定（2026-09-24）——この1枚を採用する。** **選んだのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。

## ⚠️ 設定画を付けて焼いた1枚について（**実測 n=1**。2026-09-23）

- ⛔ **様式は保たれた。** 重い粒子、浅い深度、赤い安全光の外はほぼ黒、瓶とトレイ、右に開いた戸口。
  ⛔ **設定画が宣言する3つの逆（`no heavy film grain` / `no shallow depth of field` /
  `no yellow cast`）は、写らなかった。** **註釈の文字も、入らなかった**
  （`L21` が禁じる唯一の段はここである——**この経路には、否定のための専用のパラメータが在る**）。
  ⚠️ **ゆえに問い11 の理由 (a)（あの紙はこの作品の逆を宣言している）と (b)（文字を持つ）は、
  この1枚では現実にならなかった。** **n=1 である。**
- ⚠️ **だが、この1枚では `SUBJECT` が読めない。** 絹は横顔で、**眼は影の側にあり、
  「眼が戻って、前に休んでいる」は読み取れない。** ⛔ **この1本の主題は、その2つだけである**
  （上の註——「首が回ったこと」と「眼が止まったこと」）。
  ⚠️ **採用するか、焼き直すかは、著者が決める**（**この記録は欠陥の指摘ではなく、見えたままである**）。

## ⛔ 実測（2026-09-24）と、焼き直し（著者裁定）

- ⛔ **灯が、枠に写っている**——**左上に器具の頭（傘と、赤く光る口）。**
  ⚠️ **光源が枠に入れば、この部屋は「照明のある部屋」になり、光は状態でなくなる**
  （`bible.world.visual_language.light`——**光は、方向ではなく状態である**）。
- ⛔ **原因は肯定の側である**——`LIGHT` と `Prompt` が、器具を名指す既定の1文
  （`one windowless room whose only light is a dim red safelight`）を持っていた。
  ⚠️ **その1文は `migenzo-art-board` のものである**（**実測**——あのボードの `Merged` に同じ1文が在る）。
- ⛔ **ゆえに、この1枚は焼き直しと裁定された**（2026-09-24、著者）。
  ⚠️ **肯定の側を書き換えた**——**器具は枠の外に立ち、枠が持つのは光そのものである。**
  ⛔ **`Negative` に2節を足した**（`no light source visible in frame` / `no safelight lamp in frame`）。
  ⚠️ **この2節は、この1枚には初めから1つも無かった**（**実測**: 0）。
- ⚠️ **実測（2026-09-24）**: 仕様を直した6本（02・06-1・06-2・07・08・09）の焼き直しは、
  **6本とも器具を写さなかった。** 逆に、この節を持たない仕様で焼かれた 01・05・12 は、
  **3本とも写した。** ⛔ **否定形だけでは止まらない**——02 は `no lamp` / `no bulb` /
  `no bare light source` を持ち、それでも描かれた。
- ⚠️ **`SUBJECT` が読めないことは、焼き直しでも見る**——
  **絹は横顔で、眼は影の側にある**（2026-09-23 の節）。⛔ **この1本の主題は、
  首が回ったことと、眼が止まったことだけである。**
- ⛔ **設定画を添付する1本であることに変わりはない**（著者裁定、2026-09-23）——
  **この13本で、絹の設定画が付くのは、この1枚だけである。**

## ⛔ 実測（2026-09-24、第二世代 n=1）——灯は消え、主題が読める

- ⚠️ **焼かれた1枚**——`05_01_ChatGPT Image 2026年9月24日 01_23_50.png`。**見えたままを書く。**
- ⛔ **（1）灯は、消えた。** **器具は枠のどこにも無い**（左上・上辺を拡大して確認）。
  ⚠️ **これで8本目である**——**肯定の側を書き換えた仕様から焼かれた8本は、8本とも器具を写していない。**
- ⛔ **（2）主題が、読める。** **眼は開き、前で休んでいる。**
  ⛔ **第一世代の欠陥（横顔で、眼が影の側にあり、「眼が戻って、前に休んでいる」が読み取れない）は、
  この1枚で直った。** ⚠️ **この1本の主題は、その1点だけである。**
- ⚠️ **（3）そして、残る弱さが1つ在る**——**「その二点のほうを向いている」が弱い。**
  **顔はほぼ正面、眼は前——二点のほうへはごく僅かである**（眼を4倍に拡大して確認）。
  ⚠️ **ただし、絹の眼と、閾の二点は、同じ高さに在る**——**構図の結びは残っている。**
- ⚠️ **（4）部屋が、読める。** 瓶（ラベル付き）・吊した紙・トレイ・棚・扉の取っ手まで読める。
  ⛔ **これは欠陥と呼ばない**——**アートボードの `Merged` 自身が「the tray, the bottles, the fan,
  the shelf all resolving at a glance」と宣言している**（**12 で同じ判断をした**）。
  ⚠️ **ただし、第一世代の実測は「赤い安全光の外はほぼ黒」であった**——**この世代は、そこが動いている。**
- ⚠️ **（5）エプロンが、読めない。** **黒の上着の上に黒である**——胴の右に、滑らかな面と
  縫い目らしき線が一本見えるが、**エプロンと呼べるかは、この解像では決められない**（10・11 の同じ問いへの材料）。
- ⚠️ **（6）二点は、光っていない。** **閾の暗さのなかに、赤い光を返す点が2つ**——
  **顔の他の造作は読めず、`no facial features on the figure` は満たされている。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: a woman who has spent twenty years not being looked at, being looked at — and her eyes coming back from the side they always went to
- `CHARACTERS`: `[絹: woman, late fifties, thin, short black hair faintly streaked with grey gathered loosely at the back, a calm sunken-eyed face, a black apron over a black blouse]` in the near frame, and `[盗人: a grown figure standing in the dark at the threshold, whose face the darkness does not describe — the only thing that reads is the eyes, a child's eyes, catching the red light]` — ⚠️ **盗人は閾を越えない**
- `SUBJECT`: 絹's face in the near foreground with her eyes come back and resting forward, and beyond her, in the open doorway, a figure stopped at the threshold with two points of red light where its eyes are
- `ACTION`: her eyes no longer going aside — they stop, and that is all that happens
- `LOCATION`: the doorway of the darkroom of the art board — the door standing open, and the outside giving no light at all
- `LIGHT`: the room's constant state — the dim red light of a safelight that stands outside the frame and reaches only the inside, and the warm amber glow of the developer; ⛔ **枠が持つのは光そのものであって、灯ではない**; the two points beyond the threshold are that red light coming back off the eyes, not a light of their own
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は `unit.after` である**——**絹の眼が、戻っているところである。**
⚠️ **理由**: この1本の到達は 6-9s にあり、**この1本の向きが変わったことを読ませるのは、
その1点だけである**（`PLAN.md` §2「**絹が壊してきた人生が、絹のほうへ歩いてくる**」）。
⛔ **`before` を焼けば、この1枚は「二十年、横を向いている女」になる**——
**それは 01〜04 が既に持っている画であり、この1本の画ではない。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the moment the looking changes direction in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The doorway of the darkroom of the art board: one windowless room whose only light is the red light of a safelight standing outside the frame and reaching as far as the doorway, the door standing open, and outside the door nothing at all — no corridor, no street, no light. In the near part of the frame, close to the camera, the face of a woman in her late fifties: thin, short black hair faintly streaked with grey gathered loosely at the back, a calm sunken-eyed face, a black apron over a black blouse. Her head has turned and her eyes have come back from the side they always went to; they are resting now, forward, on the doorway, and she is not moving. Beyond her, out in the open doorway, a grown figure has walked up and stopped exactly at the threshold and does not cross it: the darkness does not describe it, there is no face to read, no clothing to read, no body to read — the only thing that comes out of that darkness is the eyes, two points where the red safelight returns off them, and they are a child's eyes. Nothing else in the frame moves; this is two people holding still, one looking and one being looked at. `[絹: woman, late fifties, thin, short black hair faintly streaked with grey gathered loosely at the back, a calm sunken-eyed face, a black apron over a black blouse]` — the figure whose identity is locked to the frozen setting sheet. `[盗人: a grown figure at the threshold, undescribed by the darkness; only the eyes read, and they are a child's eyes]`. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no readable face on the figure at the threshold, no facial features on the figure, no eyes other than the two points, no glowing eyes, no luminous or emitting eyes, no light of their own, no sunglasses, no goggles, no mask, no hood over the face in view, no child's body, no child in frame, no small stature, no youthful build, no second face, no third person, no silhouette of a third person, no open door with daylight behind it, no corridor, no street, no room beyond the door, no lamp beyond the door, no doorway light spill, no light from outside, no window light, no torch, no light source visible in frame, no safelight lamp in frame, no bright evenly lit room, no dramatic tension lighting, no low angle, no confrontation staging, no standoff composition, no mirrored symmetry, no dramatic shadow on the wall, no raised hand, no reaching hand, no weapon, no bag, no coat collar turned up, no hat, no smile, no angry expression, no expression staged for the camera

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
