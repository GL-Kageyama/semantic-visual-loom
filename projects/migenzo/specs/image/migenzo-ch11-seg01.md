# 画像仕様 — 『未現像』第11章「受け取る」 第一のショット「白は、判決を下さない」（反応 / still / 8s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⛔ **この1本の仕事は、抑制である**（`rolemap.ROLES` の `反応` の固有基準——
**「抑制・微細な身体・表情の段階」**）。⛔ **ゆえに、この1本に表情を置かない。**
⚠️ **抑制の担い手は、動かない4本の指である。**
⛔ **そして、この1本の変化は、彼女ではなく、白のほうで起きる。**

⛔ **そして、この1本の終わりで、何も決まらない**——
`draft_11-2`「**白は判決を下さない。愛だ、とも、留置だ、とも、白は言わない。**」

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch11-seg01.yaml` ＋
  **既存の出力**——`migenzo-art-board/prompt.md`・同じ暗室の `migenzo-scene-board/prompt.md`・
  絹は `migenzo-kinu-character-sheet/prompt.md`（**指だけである**）
  ⛔ **娘の設定画は、この1枚の入力に置かない**（下の註）——`migenzo-ch10-seg01.md` が、
  娘の設定画を使う唯一の画像である。 ⚠️ **`_backup_20260905/` は参照しない。**
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch11-seg01.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。
  ⚠️ **第一世代が在った**——`11_01_ChatGPT Image 2026年9月23日 03_28_57.png`（2026-09-23、著者が投入）。
  ⛔ **これは焼き直しと裁定された**（2026-09-23、著者）——**仕様の側は直した**（縁の3節。下の節）。
  ⛔ **そして、この1枚は、もう作業ディレクトリに無い**（**実測**、2026-09-24——`git status` が `D` を出す）。
  ⛔ **この削除は、この稿では触っていない**（ステージしていない）。
  ⚠️ **第二世代が在る**——`11_01_ChatGPT Image 2026年9月24日 02_30_36.png`（2026-09-24、著者が投入）。
  ⛔ **著者裁定（2026-09-24）——この1枚を採用する。** **選んだのは著者である**
  （`CLAUDE.md`「**生成はサンプルである。**」）。**ゆえに、この1本は採用済みである**
  （`PLAN.md` §4-f の第二巡）。⚠️ **残る外れは、下の第二世代の実測に置く**——**直さない**（裁定）。

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: an image that came up in the liquid and a verdict that does not come — the light crosses the white place and leaves nothing in it
- `CHARACTERS`: `[絹: only four fingers of her hand enter the frame, at the near corner of the paper — woman, late fifties, thin, fingers faintly stained from developing chemicals]` and `[娘: inside the picture on the paper only — a small child's hand held flat over the round black mouth of a lens]` — ⛔ **絹の体も顔もこの枠に入らない。** **娘は像のなかに居て、この部屋には居ない**
- `SUBJECT`: a wet print lying flat in the amber developer, its full width in the frame, with an image in it — a back in a black blouse and a black apron turned away and running, a small hand laid flat over the lens, and a white place where a face should be with no line between the white and the image — and a band of red light crossing that white
- `ACTION`: the red light crossing the white and showing nothing in it, and going out the far side and leaving nothing; the four fingers at the corner do not move at all
- `LOCATION`: the last darkroom — the tray inside the small island of light, and the four fingers of a hand resting on the near corner of the paper, the outermost little finger lifted a very little and floating
- `LIGHT`: the room's constant state — the dim red light of a safelight that stands outside the frame and comes as far as the tray, and the warm amber glow of the developer; ⛔ **枠が持つのは光そのものであって、灯ではない**; the band crossing the print is that red light itself, and it is passing
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は 3-7s のなかである**——**赤い光が、白のなかを横切っているところである。**
⚠️ **理由**: ⛔ **`before`（光が白に入る前）と `after`（光が出たあと）は、
白に関して、同じ画である**——**どちらも「白のなかに何も無い」である**
（記録の `after`「**光のあとに、何も残っていない。** ⚠️ **境目も、無いままである**」）。
⛔ **ゆえに、両端のどちらを焼いても、この1本は何も持たない。**
**この1本が持っている枠は、横断のあいだだけである。**
⛔ **ただし、その横断を「顔が現れる瞬間」として焼いてはならない**——**下の註のとおりである。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the white that nothing comes out of in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The last darkroom: a small island of light in a room that is otherwise dark, and in the developing tray, under the amber liquid, one photographic print lying flat and even, still wet, its full width held in the frame, and everything that is not the tray and this paper gone into the dark. On the print there is an image: a woman's back in a black blouse and a black apron, turned away and running, with one arm and an open hand; and nearer than the back, a small child's hand laid flat over the round black mouth of a lens, held flat on the glass, with a single strand of red light coming in through the one gap at its edge. And just above and behind that small hand there is the place where the face of the child whose hand it is should be, and that place is white: not a blur and not a glow, but one white area with no line drawn between it and the image, the boundary melted in the liquid, so that the white and the picture meet without an edge, and there is nothing inside the white at all. A band of red light is crossing that white at this moment, and inside the band the white is exactly the same white as outside it — the light passes over it and shows nothing in it, and it will go out the far side and leave nothing behind. At the near corner of the print, resting on the paper, are four fingers of a woman's hand — late fifties, thin, the fingers faintly stained from years of developing chemicals — and the outermost little finger is lifted a very little above the corner of the paper and is floating, with the red light passing under it. The four fingers in this room are a grown woman's hand and they do not move; the small hand is small, and it is inside the picture on the paper — the two are not the same size and not the same hand, and the small one is a child's. `[絹: only four fingers of her hand, at the near corner of the paper — woman, late fifties, thin, fingers faintly stained from developing chemicals]` — no body, no face, no wrist, no palm in the frame. `[娘: inside the picture on the paper only — a small child's hand held flat over the round black mouth of a lens]` — the hand is in the image and is not in the room, and her face is not drawn. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board, with everything that is not the tray and the paper gone into the dark. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no person, no figure, no body, no face, no adult figure in the room, no hand in the room other than the four fingers at the corner, no second hand in the room, no arm in frame, no wrist, no palm, no thumb, no face in the white, no eyes in the white, no faint face in the white, no suggestion of a face in the white, no partial face, no blurred face, no ghost face, no line drawn around the white, no edge to the white, no outline of a head in the white, no shading inside the white, no modelling inside the white, no face-like pattern in the white, no second face, no face in the image on the paper, no eyes in the image on the paper, no adult hand on the lens, no large hand on the lens, no gripping or clutching hand, no tense clawed fingers, no fingers closed over the lens, no lens covered completely, no wound, no blood, no tongs, no bubbles, no foam, no film canister, no roll of film, no reel or spool, no bottles or jars, no enlarger, no second print, no dry print, no dry paper, no print lifted out of the tray, no liquid running off the paper, no drip from the paper, no smear on the paper, no fingerprints on the paper, no motion blur on the fingers, no reflection of the room in the liquid, no glowing paper, no luminous white, no god rays, no lens flare, no light source visible in frame, no safelight lamp in frame, no bright evenly lit room, no portrait lighting, no visible camera body, no brand of camera, no border around the print, no white border, no deckled edge, no readable text on the paper, no writing on the paper, no date stamp in the image

---

## ⛔ 白は、内容である——「見えかけて、無い」を、1枚に焼かない

- ⛔ **この1本のなかで、いちばん危ないのは、`draft_11-3` の一行を、そのまま描かせることである**——
  「**消えるまでのあいだ、白のなかに、顔のかたちがあるように見えて、やはり、ない。**」
- ⚠️ **「見えかけて、無い」は、時間のなかにしか無い。**
  ⛔ **1枚に焼けば、「見えかけている顔」が焼かれる**——**そしてそれは、この作品の核の禁制である。**
- ⛔ **ゆえに、この1枚は逆を焼く**——**光が白のなかに在るのに、白が白のままであること。**
  ⚠️ **肯定の側がそう書いている**——
  「**inside the band the white is exactly the same white as outside it — the light passes over it
  and shows nothing in it**」。
  ⛔ **何も現れないことが、この1本の内容である。**
- ⛔ **`no fully rendered face of the daughter` は、この13本すべてに残る**（`bible.negative_base`）。
  ⚠️ **そしてここでは、それが主題である**（申し送り(3)——「**ここでは「出ない」ことが主題である**」）。
  ⛔ **だが、それをこの1枚の唯一の顔の指示にしない**——
  **否定形は空欄になり、生成器が衣装で埋める。** **肯定の側が「線のない、ひとつの白」を名指している。**
  ⚠️ **そして `no faint face in the white` / `no blurred face` / `no ghost face` /
  `no face-like pattern in the white` が、その白を守る。**

## ⛔ 2つの手を、別々のものとして書く——そして、禁制は落ちている

- ⛔ **`no small hand pressing the lens` は、この1本には掛からない**——
  ⚠️ **11 で落ちた**（`negative: changed`）。**動きかたは「削除」である**（入れ替えではない）。
  ⛔ **ゆえに、この1枚の `Negative` に、その節は無い。**
  **置けば、この1枚は自分の主題の一部を禁じる。**
- ⛔ **そして危険は、逆側に立つ**——**11 と同じである**——
  「**手が描かれすぎる**」。⚠️ **この1本では、さらに、紙の角の4本の指と、
  像のなかの小さな手が、同じ枠に同居する**（申し送り(2)）。
- ⚠️ **ゆえに肯定形が、大きさの関係を名指す**——
  「**the four fingers in this room are a grown woman's hand……the small hand is small, and it is
  inside the picture on the paper — the two are not the same size and not the same hand,
  and the small one is a child's**」。
  ⛔ **大きさは、画面のなかでしか測れない**——**そしてこの1枚には、測る相手が同居している**
  （`migenzo-ch10-seg01.md` と同じ理屈である——**幅は、画面のなかの大きさでしかない**）。
- ⛔ **そして `no second hand in the room` が在る**——**部屋の手は、4本の指だけである。**
  ⚠️ **ゆえに `no wrist` / `no palm` / `no thumb` / `no arm in frame` も在る**——
  **この枠に在るのは、紙の角にかかった指だけである。**
- ⛔ **この1枚の入力に、娘の設定画を置かない**——**像のなかの小さな手は、言葉で書く。**
  ⚠️ **それは `attached` の話ではない**——**動画の側で `娘.identity` を引くかは ③ が決める**
  （申し送り(1)——**「どちらでも成立する。② は決めない」**）。
- ⛔ **そして「手だけ」を引く経路が、この基盤には無い**（07・08・09・10 と同じ申し送りである）——
  **絹の4本の指も、言葉で書く。**

## ⛔ 表情を、この1枚に置かない

- ⛔ **彼女の顔は、この枠に無い。** **ゆえに、この1枚に表情は、置きようが無い。**
  ⚠️ **これは偶然ではない**——**`反応` の抑制の担い手は、動かない4本の指である。**
- ⚠️ **そして、この1本の変化は、彼女ではなく、白のほうで起きる。**
  ⛔ **ゆえに `no motion blur on the fingers` が在る**——
  **この4本の指は、8秒のあいだ、1本も動かない。**
- ⛔ **息ひとつ、置かない**——**息を置けば、それは `所作` になる**（**08 の役である**）。

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である。**
  ⚠️ **そして `documentary-photo` の `available natural light` は、ここでは特に害になる**——
  **この部屋の光は、状態である。**

## ⛔ 実測（2026-09-23、n=1）と、焼き直しの2点（著者裁定）

- ⚠️ **焼かれた1枚**——`11_01_*`。**見えたままを書く。**
- ⛔ **芯は在る**——**レンズを覆う小さな手、紙の角の4本の指（小指が浮いている）、
  白、赤い帯、そして白のなかに何も現れないこと。**
- ⛔ **だが、1つ外れている**——**像のなかの女の服が、白い。**
  ⚠️ **この女は 10 の像と同じ女である。** **そして `migenzo-ch10-seg01.md` は、
  彼女を肯定の側で `a black blouse` と定めている**——
  ⛔ **この画像仕様は、服を1字も書いていなかった。**
  ⚠️ **10 と 11 は、この摘要版で隣り合う2本である。**
  **同じ1枚の印画紙を映しながら服の色が変わるなら、それは編集で繋げない。**
- ⛔ **原因は、10 の仕様から1節が落ちていることである**——
  **`CHARACTERS` と `SUBJECT` の両方に、`a black blouse and a black apron` を足した。**
- ⚠️ **そして、白の場所を名指した**——**「顔があるはずの場所」は、
  生成器には位置を持たない。** **ゆえに「小さな手の、すぐ上と後ろ」と書いた**
  （**手が belongs to している者の顔である**）。
- ⚠️ **灯を枠の外へ出した**（**02・06-1・06-2・07・08・09 と同じ欠陥である**）。
  ⛔ **この1枚は、それを最初から `Negative` に持っていた**（**02 と同じ型である**）。
- ⛔ **`no fully rendered face of the daughter` は、この焼き直しでも残る**——
  **そしてここでは、それが主題である。**

## ⛔ 実測（2026-09-24、第二世代 n=1。**採用**）——白のなかに、何も現れない

- ⚠️ **焼かれた1枚**——`11_01_ChatGPT Image 2026年9月24日 02_30_36.png`。**見えたままを書く。**
- ⛔ **主題は満たされた**——**赤い帯が像を横切り、白の面の上を通っている。**
  ⛔ **そして、白のなかに、顔も眼も、かたちも現れていない**——`no face in the white` /
  `no faint face in the white` / `no face-like pattern in the white` の族が守られている。
  ⚠️ **この1本の内容は「何も現れないこと」であり、それが画になっている。**
- ⛔ **娘の小さな手** ✓——**丸い黒いレンズの口の上に、平らに置かれている。**
  **手は小さく**、`no adult hand on the lens` / `no large hand on the lens` /
  `no gripping or clutching hand` を満たす。
- ⛔ **背を向けて走る女** ✓——**膨らんだ袖の黒い上着と黒いエプロン**、背を向け、
  片腕を伸ばして手を開いている。⚠️ **第一世代の外れ（服が白い）は、これで閉じた。**
  ⛔ **ただし「10 の像と同じ服であるか」は、この稿では測っていない。**
- ⛔ **紙** ✓——**液に平らに横たわり、幅いっぱい**。濡れている。**雫は無い。**
- ⛔ **縁** ✓——**紙の縁は、まっすぐな裁ち切りである。白い縁も、ギザギザの耳も無い**
  （第一世代の2点のうち、これが閉じた）。
- ⛔ **灯** ✓——**トレイの外は近黒である**（右上の画素は (1,1,1)、**実測**）。器具はどこにも無い。
- ⛔ **絹の4本の指**——**左下から、長い爪の4本が入り、先が紙の手前の角へ届いている** ✓。
  ⚠️ **いちばん外の指は、他から離れて、先に暗い隙間がある**——「**わずかに浮いている**」と読める。
  ⛔ **ただし、それが「紙の角の上」であるかは、確かめられない**（**実測の限界**）。
- ⛔ **残る外れ**——**4本の指だけでなく、手の甲も枠に入っている。**
  仕様は「**手の四本の指だけが枠に入る**」と言い、`Negative` は `no palm` / `no wrist` /
  `no arm in frame` / `no thumb` を持つ。⚠️ **実測——親指 ✓無し、前腕 ✓無し、手首 ✓無し。
  だが甲は、左下の枠の角へ抜けていく。**
- ⛔ **著者裁定（2026-09-24）——この1枚を採用する。** ⚠️ **上の残りは、記録であって、
  次の焼き直しの指示ではない**（**選んだのは著者である**）。

## 記録との対応

- `unit` … `before`「トレイの液のなかに、まだ濡れている印画紙がある——像のなかに、
  逃げる絹の背中と、レンズを押さえる小さな手がある。⚠️ **そして、顔があるはずの場所がある。
  その場所だけが、白い。** ⚠️ **境目が、とけている**……**紙の手前の角に、絹の4本の指がある。
  いちばん外の小指が、紙の角の、すこしうえで、浮いている。**」→
  `after`「**同じ枠。指は、1本も動いていない。** ⚠️ **変わったのは、白である**——
  **赤い光が、白のなかを横切って、行ってしまった。** ⛔ **そして、光のあとに、何も残っていない。**
  ⚠️ **白のなかに、顔のかたちは、無い。**」
- `beats` … 0-3s 濡れた印画紙と、浮いた小指（**観客は、像を読む時間を持つ**）／
  3-7s **赤い光が、白のなかへ入り、横切る**／7-8s **光のあとに、何も残っていない。**
  ⚠️ **この1枚が切るのは 3-7s である。**
- ⛔ **光の横断は、8秒のうち4秒かける**——**速く通せば、それは「ちらつき」である。**
  ⚠️ **「見えかけて、無い」が読めるためには、光が遅くなければならない**（記録の `quality`）。
- ⛔ **この1本の明るさは、白そのものではなく、白が在る場所である**——
  **白は、闇のなかの光の島の、いちばん明るいところにある。**
  ⚠️ **ゆえに `no luminous white` / `no glowing paper` が在る**——
  **白は、光っているのではない。** **光を受けているのである。**
- ⚠️ **この部屋の地理の法**（`ledger.locations.最後の暗室.geography`）——
  **光の届かない面は、沈んだまま暗い。**
- `place` / `time` … `最後の暗室` / 時刻を持たない
- `attached`（見込み）… `最後の暗室.base`・`最後の暗室.geography`・`印画紙`・
  `絹.identity`（**指だけである**）
  ⚠️ **`娘.identity` を引くかは ③ が決める**（申し送り(1)）——**② は決めない。**
  ⚠️ **`attached` の確定は ③ である。**
