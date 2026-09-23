# 画像仕様 — 『未現像』第9章「最後の暗室」 第一のショット「宙づり。触れない」（余白 / still / 10s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⛔ **この1本の仕事は、耐えることである**（`rolemap.ROLES` の `余白` の固有基準——
**「耐えるか・張力の保持」**）。⛔ **ゆえに、この1本に出来事を置かない。**
**何も起こらないことが、起こることである。**
⚠️ **`PLAN.md` §1「山の作り方」の第2段**——「**09・10（8s＋10s）** — **言葉と、宙づり。**」
⛔ **09 が言葉の側であり、この1本が宙づりの側である。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch09-seg01.yaml` ＋
  **既存の出力**——`migenzo-art-board/prompt.md`・同じ暗室の `migenzo-scene-board/prompt.md`・
  手の年代と薬品の染みは `migenzo-kinu-character-sheet/prompt.md`
  （⚠️ **`_backup_20260905/` は参照しない**）
  ⛔ **この1枚は「手だけ」を撮る。** **手だけを引く欄は、この基盤に無い**（下の註）。
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch09-seg01.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。
  ⚠️ **第二世代が在る**——`09_01_ChatGPT Image 2026年9月24日 01_04_05.png`（2026-09-24、焼き直し）。
  ⚠️ **第一世代は、このディレクトリに無い**（**実測**、2026-09-24——このディレクトリの `09_01_*` は、この1枚だけである）。
  ⚠️ **`git status` は、この位置について何も言わない**——**第一世代が在った場所を、この稿は見ていない**（追跡されていた形跡も無い）。
  ⛔ **著者裁定（2026-09-24）——この1枚を採用する。** **選んだのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: a hand holding one strip of film above a liquid that is still moving for the first time in twenty years, and not lowering it
- `CHARACTERS`: `[絹: only her hand and forearm enter the frame — woman, late fifties, thin, hands faintly stained from developing chemicals]` — ⛔ **彼女の体も、顔も、この枠に入らない**
- `SUBJECT`: a small island of light in a dark room — the developing tray with its amber liquid standing as one taut skin across it, one blank white silver-gelatin sheet lying flat in that liquid with nothing floating up in it, one thread-thin ripple running from the near rim to the far rim, the empty drawer standing open in the wall beside it, and just above the surface a hand holding one small strip of unexposed film whose width can be seen
- `ACTION`: nothing — the hand stays at exactly the same height and does not lower; the surface is still moving and the one ripple is about to go out
- `LOCATION`: the last darkroom — inside the island of light there are only the tray with its blank white sheet lying under the liquid, its whole shape lying in the lower left of the tray where the amber is shallow and its near edge catching the light, and the open empty drawer, and everything past the reach of the light is not wall but darkness
  ⛔ **この白は、2026-09-23 の著者裁定で、ここに決まった**（動画の §5・§20 の食い違い(4)——
  **初稿は「枠に紙が無い」と読んでいた**）。⚠️ **根拠は、アートボードと、台帳の `暗室.base` と、
  第10章の源である**（`draft_10-1`「二十年のあいだ、なにも浮かばなかったその白のなかに」）。
- `LIGHT`: the room's constant state — the dim red light of a safelight that stands outside the frame and comes as far as the tray and the drawer and no further, and the warm amber glow of the developer itself; ⛔ **枠が持つのは光そのものであって、灯ではない**; ⛔ **液面は光を吸うので、フィルムの影は液面に落ちない**
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は 4-7s のなかである**——**二度目の波が、ふちからふちへ走っているところである。**
⚠️ **理由**: ⛔ **この1本には、`before` と `after` の区別が無い**——**手は、1センチも動かない**
（記録——「**手は、同じ高さにある**」「**1センチも下がっていない**」）。
**ゆえに、どちらの端を焼いても、同じ画になる。**
⛔ **だが、同じでないものが、1つだけ在る**——**液面である。**
⚠️ **静止した液面を焼けば、この部屋の戸が開いたことが、この1枚から消える**——
**二十年動かなかった液が、今夜、まだ動いている**（記録の `before`「**二十年動かなかった液が、
今夜、戸が開いたことで、まだ、動いている**」）。
⛔ **ゆえに、波が走っているあいだで切る。**
⚠️ **そして、赤い光のなかを、ほこりが落ちている**——**これも、二十年動かなかった空気の、
はじめての運動である。** **この2つが、この1本の「まだ動いている」である。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the surface that is waiting for the hand in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The last darkroom: a small island of light in a room that is otherwise dark — and inside that island there are only two things, the developing tray with its amber liquid — and lying flat under that liquid one sheet of blank white silver-gelatin paper, its whole shape lying in the lower left of the tray where the amber is shallow, its near edge catching the light and its white readable through the amber, with nothing floating up in it — and, in the wall beside it, a drawer standing open and empty, and everything past the reach of the light is not a wall and not a corner of a room but simply darkness. The liquid in the tray stands as one taut skin across the whole tray, and lying flat under it is that one sheet of blank white silver-gelatin paper, its shape readable through the amber and its edge catching the light, with nothing floating up in it and no image on it, and over the liquid there is a very thin film, and one thread-thin ripple is running straight from the near rim to the far rim and is about to go out. Just above the surface, held at exactly the same height and not lowering, is a woman's hand and forearm coming in from outside the frame — a hand in her late fifties, thin, the fingers and the skin around the nails faintly stained from years of developing chemicals — and between the fingers it holds one small strip of unexposed film held flat so that its width can be seen: a dry flat strip with nothing on it at all, no image and no frame and no exposure. It has not touched the liquid and it is not going to touch it. The liquid takes the light rather than reflecting the room, so the strip casts no shadow on the surface. In the red light, fine dust is hanging and going slowly down — the first movement this air has had in twenty years. Her body and her face are not in this frame and there is nobody else in the room. `[絹: only her hand and forearm — woman, late fifties, thin, hands faintly stained from developing chemicals]`. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board, with everything that is not the tray, its blank sheet and the drawer gone into the dark. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no person, no figure, no body, no face, no second hand, no left hand, no face in the frame, no reflection of a face in the liquid, no image on the film strip, no developed image, no frames on the strip, no sprocket holes reading as a picture, no negative with a face, no photograph in the tray, no print in the tray, no contents in the drawer, no object in the drawer, no film canister, no canister, no reel or spool, no bottles or jars, no enlarger, no tongs, no second strip, no hand descending, no hand tilted down, no fingers opening, no fingers releasing, no fingertips at the liquid, no contact with the surface, no motion blur on the hand, no motion blur on the film strip, no blur on the fingers, no bubbles, no foam, no concentric ripples, no circular wave pattern, no drop hitting the surface, no splash, no drop of liquid in the air, no third ripple, no jagged line on the surface, no zigzag ripple, no lightning-shaped ripple, no regular pattern of ripples, no mirror-flat surface reflecting the room, no light source visible in frame, no safelight lamp in frame, no lamp, no bulb, no bare light source, no painted or drawn liquid, no glowing dust, no sparkle or star effect, no lens flare, no god rays, no lit wall, no lit back wall, no corner of the room, no second room, no doorway, no open door, no shelf, no furniture other than the tray and the drawer, no table, no chair, no stool, no watch on the wrist, no ring, no bracelet, no nail polish, no long fingernails, no youthful hand, no clean unstained hand, no manicured hand, no glove, no sleeve with a cuff, no apron in frame, no bright evenly lit room, no dry tray, no empty tray

---

## ⛔ 光の島——この部屋の見えかたは、源が決めている

- ⚠️ **この1本は、`最後の暗室` を引く最初の1本である。** **鍵は 2026-09-23 に増えた**
  （`PLAN.md` §0-e の改訂、著者裁定）。
- ⛔ **そして、この部屋の見えかたは源が決めている**——
  **赤い光が届くのは、トレイと引き出しと、そのまわりだけである**（`draft_09-1`）。
- ⛔ **ゆえに ③ は、`base` に「同じアートボード」を引き、そのうえで
  「光の島の外は闇」を、否定形でなく肯定形の側で持つ必要がある**
  （`shots/migenzo-ch09-seg01.yaml` の申し送り(1)）。
  ⛔ **否定形は空欄になり、生成器が壁で埋める。**
- ⚠️ **この1枚も、同じ形で書いてある**——
  「**everything past the reach of the light is not a wall and not a corner of a room
  but simply darkness**」。
  ⛔ **ゆえに `no lit wall` / `no lit back wall` / `no corner of the room` は、その肯定の裏である。**

## ⛔ 沈めない——この1本は、沈める前である

- ⛔ **この1本の `after` は、まだ、触れていない**（記録——「**フィルムの端は、まだ、液に触れていない**」）。
  ⚠️ **像が浮かべば、この摘要版は、ここで終わる。**
- ⛔ **ゆえに `no image on the film strip` / `no developed image` / `no negative with a face` が在る**
  （申し送り(2)——**`未露光のフィルム` の否定集合が、この1本では特効である**）。
- ⚠️ **そして、この物は S10 と S11 の2本に連続して現れる**——
  **S11 の `KEEP` が「フィルムの幅」である**（`ledger.props.未露光のフィルム`）。
  ⛔ **③ は、この2本で同じ幅を保つ必要がある**（**幅は台帳が持つ唯一の寸法である**）。
  ⚠️ **ゆえに、この1枚は、フィルムを「幅の見える一枚」として焼く**——
  **丸めない。面で見せない。** **つまんだ指のあいだから、幅が読めるように置く。**
- ⛔ **そして `no bubbles` が在る**——**この作品の画面に在ってよいものは、液面と、
  沈むものと、浮かぶものである。** **泡を数えれば、02 の反復になる。**

## ⛔ 娘.identity を、この1本では引かない

- ⛔ **娘は、まだ、何も持たない。** **浮かぶのは 11 である**（申し送り(3)）。
- ⚠️ **ゆえに、この1枚の `CHARACTERS` に、娘の欄が無い。**

## ⛔ 「手だけ」を引く経路が、この基盤には無い

- ⚠️ **設定画は顔・体格・エプロンを持つ。手だけを引く欄は無い**
  （07・08 と同じ申し送りである）。
- ⛔ **ゆえに、この1枚の `CHARACTERS` は、手を言葉で書く**——
  **肯定の側が「a woman's hand, in her late fifties, thin, faintly stained」と定める。**
- ⛔ **そして `no glove` / `no sleeve with a cuff` / `no apron in frame` が在る**——
  **この枠に在るのは、手と、前腕と、フィルムだけである。**

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である。**
  ⚠️ **そして `documentary-photo` の `available natural light` は、ここでは特に害になる**——
  **この部屋の光は、状態である。**

## ⛔ 実測（2026-09-23、n=1）と、焼き直しの3点（著者裁定）

- ⚠️ **焼かれた1枚**——`09_01_*`。**見えたままを書く。**
- ⛔ **芯は在る**——**手は同じ高さに保たれ、波が1本走り、引き出しは開いたまま空である。**
- ⛔ **だが、2つ外れている。**
  **（1）トレイの液に沈んでいる白い紙が、見えない**——**この1本の `LOCATION` はそれを書いている。**
  ⚠️ **そして 06-2 と同じ欠陥である**（**同じ 2026-09-23 の裁定で、同じ位置に決まった白である**）。
  **（2）波が、稲妻の形をしている**——**仕様は「糸のように細い1本」であり、形は書いていなかった。**
- ⛔ **直したのは3点である。**
  **（a）紙の位置を名指した**（液面の下・トレイの左下手前・琥珀の浅いところ・形が透けて読める・
  近い縁が光を受ける・浮かない）。
  ⚠️ **（b）波に形を与えた**——**`straight`（まっすぐ）を足し、`Negative` に
  `no jagged line on the surface` / `no zigzag ripple` / `no lightning-shaped ripple` を足した。**
  **（c）灯を枠の外へ出した**（**02・06-1・06-2・07・08 と同じ欠陥である**）。
- ⛔ **`no third ripple` は、この焼き直しでも残る**——**3度目は、もはや波でなく、周期である。**
- ⚠️ **そして `no print in the tray` / `no photograph in the tray` も残る**——
  **トレイに在るのは、白いままの紙である。**

## 記録との対応

- `unit` … `before`「**闇のなかの、小さな赤い島である。** 島のなかにあるのは3つだけ——
  **現像トレイと、その琥珀の液面と、隣の壁の引き出し**……**そして、液面のすぐ上に、絹の手がある。**
  ⛔ **触れていない。**」→ `after`「**同じ枠。手は、同じ高さにある。**
  ⛔ **1センチも下がっていない。** ⚠️ **変わったのは、液面である**……
  ⛔ **フィルムの端は、まだ、液に触れていない。**」
- `beats` … 0-4s 光の島と、止まっている手（**波が一度走って、消える**）／
  4-7s **波が、もう一度、走る。ほこりが、ひとつ、落ちていく**／
  7-10s **液面が止まり、膜はまだ張り、ほこりはまだ落ちている。**
  ⚠️ **この1枚が切るのは 4-7s である。**
- ⛔ **この1本は、2度目の波のあと、3度目を走らせない**——**3度目は、もはや波でなく、周期である。**
  ⚠️ **ゆえに、この1枚の波も、1本だけである。**
  ⛔ **`no third ripple` / `no regular pattern of ripples` / `no concentric ripples` がそれである**
  ——**同心円は「何かが落ちた」であり、この1本には、落ちたものが無い。**
- ⛔ **この10秒で、出来事はゼロである。** ⚠️ **この1枚も、出来事を焼かない。**
- ⚠️ **この部屋の地理の法**（`ledger.locations.最後の暗室.geography`）——
  **光の届かない面は、沈んだまま暗い。** **この枠の外縁は、闇であって、壁ではない。**
- `place` / `time` … `最後の暗室` / 時刻を持たない
- `attached`（見込み）… `最後の暗室.base`・`最後の暗室.geography`・`未露光のフィルム`・
  `印画紙`（トレイの液面）・`絹.identity`（**手と前腕だけである**）
  ⛔ **`娘.identity` を置かない。** ⚠️ **`attached` の確定は ③ である。**
