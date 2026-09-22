# 画像仕様 — 『未現像』第7章「留置」 第一のショット「動けるのに、動かない」（所作 / motion / 9s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⚠️ **07 と 08 は同じ役（`所作`）であり、それは意図である**（`PLAN.md` §1 の註）——
⛔ **「手が動く1本と、手が止まる1本」。** **この1本が、止まるほうである。**

⛔ **この1本の意味は、指が止まったことではない**——
**止まった距離が、二十年と同じだったことである。**
⚠️ **ゆえに、この1枚は、その距離を、他の距離と同格に置く。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch07-seg01.yaml` ＋
  **既存の出力**——`migenzo-art-board/prompt.md`・同じ暗室の `migenzo-scene-board/prompt.md`・
  絹は `migenzo-kinu-character-sheet/prompt.md`（⚠️ **`_backup_20260905/` は参照しない**）
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch07-seg01.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。⚠️ **まだ1枚も無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: a hand that can move, arriving, measuring the weight of something without taking it, and going back
- `CHARACTERS`: `[絹: only her hand and forearm enter the frame — woman, late fifties, thin, hands faintly stained from developing chemicals]` — ⛔ **彼女の体も、顔も、この枠に入らない**
- `SUBJECT`: the inside of an open wooden drawer with a small film canister lying on its side, its length running across the drawer's bottom and its round lid turned to the left, and a hand come in from outside the frame, stopped short of the canister, the palm opened a little and the fingers loosely together and not spread
- `ACTION`: the hand having extended and stopped, the fingertips not closing, held at the same distance it has been held at for twenty years
- `LOCATION`: the darkroom of the art board — the inside of the open drawer taking the whole frame, the red light reaching only its near edge
- `LIGHT`: the room's constant state — the dim red light of a safelight that stands outside the frame and reaches no further than the near edge of the drawer, and the warm amber glow of the developer tray further off; ⛔ **枠が持つのは光そのものであって、灯ではない**; no time of day and no directional light
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は 3-6s のなかである**——**手が止まり、掌がすこし開いているところである。**
⚠️ **理由**: ⛔ **この1本の `before` と `after` は、同じ枠である**——
**「**この1本の最初と最後に、画面は同じである**」**（`shots/migenzo-ch07-seg01.yaml`）。
**ゆえに、`after` を焼けば、この1枚は「手の無い引き出しの内側」になる**——
**それは `before` と同じであり、この1本の何も持っていない。**
⚠️ **この1本を持っている枠は、真ん中だけである。**
⛔ **そして `no small hand pressing the lens` の側からも、この1枚は安全である**——
**筒は開かない。手は、筒をつかまない。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the hand that stops short in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The inside of an open wooden drawer fills the frame: the wooden bottom of it, dry and pale, and lying on that bottom one small film canister laid on its side — a plain closed cylinder lying flat along the wood, its round lid turned to the left, its length running across the drawer's bottom, and it has been in exactly this place for twenty years. The red light of the darkroom, which comes from a safelight standing outside the frame, reaches no further than the near edge of the drawer, so the back of the inside stays dark and the canister sits half in it. Into the frame from outside comes one hand and its forearm — a woman's hand, in her late fifties, thin, the fingers and the skin around the nails faintly stained from years of developing chemicals — and it has extended toward the canister and stopped a little short of it. The palm has opened a little and lifted, the way a hand does when it is weighing something, and the fingers are neither closed nor spread: they stay loosely together, held open at that same small distance from the canister, the distance they have been held at for twenty years. The canister has not moved and is not going to move. Her body and her face are not in this frame and there is nobody else in the room. `[絹: only her hand and forearm — woman, late fifties, thin, hands faintly stained from developing chemicals]`. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no person, no figure, no body, no face, no second hand, no face in the frame, no image on the canister, no canister opened, no lid off, no open canister, no film taken out, no developed image, no image on the film, no frames on the film, no negative, no photograph, no paper, no print, no tongs, no grease mark, no thumb mark, no dust, no cobweb, no mouse, no second canister, no reel or spool, no bottles or jars, no enlarger, no second drawer, no chest of drawers, no watch on the wrist, no ring, no bracelet, no nail polish, no long fingernails, no youthful hand, no clean unstained hand, no manicured hand, no glove, no dramatic lighting into the drawer, no spotlight, no glow from inside the drawer, no shallow depth of field used to isolate the fingertips, no extreme close-up of two fingertips, no splayed fingers, no fingers spread wide, no hand spread flat, no product photography of a hand, no light source visible in frame, no safelight lamp in frame, no lamp, no bulb, no bare light source, no bright evenly lit room, no polished wood, no varnish shine, no open drawer with anything else in it

---

## ⛔ 強調しない——この1枚でいちばん大事なところである

- ⛔ **寄れば「止まった指」を強調する画になる**——**それは `never to make a point` に反する**
  （`shots/migenzo-ch07-seg01.yaml` の `law`）。
- ⚠️ **ゆえに `no extreme close-up of two fingertips` / `no shallow depth of field used to isolate
  the fingertips` / `no dramatic lighting into the drawer` が、この1枚に在る。**
  ⛔ **この3節は、`documentary-photo` の様式の側からも、この文法の側からも要る。**
- ⚠️ **そして、肯定の側が距離を名指している**——
  「**held open at that same small distance from the canister, the distance they have been held
  at for twenty years**」。
  ⛔ **同格に置かれた距離だけが、「二十年、同じだった」と読める。**
- ⛔ **震えは、この1枚に置かない**（`draft_07-2`「**量った手の指先が、すこし震えて、とまる**」）——
  **震えは、3-6s の最後に一度だけ置かれる運動であり、画像は「とまったあと」を焼く。**
  ⚠️ **ゆえに、この1枚の手は、静止している。**

## ⛔ 筒を開けない——世界の法である

- ⚠️ **`構想/world.md`**——「**一度も重ね合わせでなかったものは、現像できない**」。
  ⛔ **ゆえに `no canister opened, no lid off, no film taken out, no developed image` が在る。**
  ⚠️ **これは禁制であると同時に、この1本の内容である**——
  **観客は、この1本の終わりで「触れれば、開けてしまう」と知る。**
- ⚠️ **`未露光のフィルム` の否定集合が、この1本では特に効く**
  （`shots/migenzo-ch07-seg01.yaml` の申し送り）。
- ⚠️ **そして ③ への申し送り**——**この物は S04 で失われている。**
  **S04 と この1本のあいだに、返却の画は無い。**
  ⛔ **矛盾として扱わない**——**台帳が状態を持ち、画面が持たないだけである。**

## ⛔ 「手だけ」を引く経路が、この基盤には無い

- ⚠️ **07 と同じ申し送りである。** **この1枚の `CHARACTERS` は、手を言葉で書く。**
  ⛔ **肯定の側が「a woman's hand, in her late fifties, thin, faintly stained」と定め、
  `Negative` が若い手・手入れされた手を落とす。**

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である。**

## ⛔ 実測（2026-09-23、n=1）と、焼き直しの3点（著者裁定）

- ⚠️ **焼かれた1枚**——`07_01_*`。**見えたままを書く。**
- ⛔ **芯は在る**——**開いた引き出しの内側に筒が在り、手が入り、止まっている。**
- ⛔ **だが、2つ外れている。**
  **（1）筒が、直立している**——**この1本は「横たわっている」筒である。**
  **（2）指が、広く開いている**——**仕様は「掌がすこし開く」であって、「指を広げる」ではない。**
- ⛔ **（1）の原因は、英語の曖昧さである**——**初稿の `SUBJECT` は `lying on its bottom` と書いていた。**
  ⚠️ **これは「底面で立っている」と読める。** **日本語の註は「横たわっている」と言っている**
  （下の `unit` の `before`）。**ゆえに、英語の側が意味を1つに定めていなかった。**
  ⛔ **直した: `lying on its side`——長さは引き出しの底を横切り、丸い蓋は左を向く。**
- ⛔ **（2）は、肯定の側の語が足りなかった。** **`the palm opened a little` だけでは、
  生成器は指まで開く。** ⚠️ **ゆえに「loosely together, neither closed nor spread」を足し、
  `Negative` に `no splayed fingers` / `no fingers spread wide` / `no hand spread flat` を足した。**
- ⚠️ **そして灯を枠の外へ出した**（**02・06-1・06-2 と同じ欠陥である**——
  **動画の §16・§18 は禁じている**）。**この1枚は筒の内側なので、灯は元から入りにくい。**
- ⛔ **距離の設計（`held at that same small distance`）は、1字も変えていない。**

## 記録との対応

- `unit` … `before`「暗い木のなかに、フィルムの筒が横たわっている——二十年、そこに在るものである。
  ⚠️ **筒の上に、まだ、手は無い。**」→ `after`「**同じ枠。手は、もう、無い。**
  ⚠️ **筒は、1ミリも動いていない**」
- `beats` … 0-3s 木の底と筒（画面は動かない）／3-6s **手が入り、伸び、止まる。掌がすこし開く**／
  6-9s **手が、同じ速さでひっこむ。** ⚠️ **この1枚が切るのは 3-6s である。**
- ⛔ **速く引けば、それは「拒んだ」になる。** **これは拒否ではない。**
  ⚠️ **残るのは、同じ位置に在る筒と、同じ距離だけである。**
- ⚠️ **この1本の最初と最後に、画面は同じである**——
  ⛔ **ゆえに、この1枚は、その「同じ」のあいだにある、ただ1つの枠である。**
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`・`引き出し`・`未露光のフィルム`
  ⛔ **人物の鍵を置かない**（**設定画は顔を持つ**）。⚠️ **`attached` の確定は ③ である。**
