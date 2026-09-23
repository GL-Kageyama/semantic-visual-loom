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
- 生成物の置き場: このディレクトリ。
  ⚠️ **第一世代が在る**——`01_01_ChatGPT Image 2026年9月23日 03_02_10.png`（2026-09-23、著者が投入）。
  ⛔ **これは候補であって、採用ではない**（`CLAUDE.md`「**生成はサンプルである。**」）。**選ぶのは著者である。**
  ⛔ **そして、この1枚は焼き直しと裁定された**（2026-09-24、著者）——**下の実測の節を読む。**
  ⚠️ **第二世代が在った**——`01_01_ChatGPT Image 2026年9月24日 01_16_51.png`（2026-09-24、著者が投入）。
  ⛔ **これも焼き直しと裁定された**（2026-09-24、著者）。⚠️ **そして、いま作業ディレクトリに無い**
  （**実測**、2026-09-24——このディレクトリに `01_01_*` は1枚も無い）。
  ⚠️ **その削除は `git status` に出ない**——**第二世代は追跡されていなかったからである。**
  ⛔ **そして、いま第三世代を焼いている**（2026-09-24、著者）。**ゆえに、この1本は、まだ採用されていない。**
  ⚠️ **脂痕の設計の岐路は、著者裁定で閉じた**（2026-09-24）——**「細かい論点なので、追わない」**。
  **ゆえに、この1本の脂痕は、面の読めない鈍いよごれのままでよい**（下の実測の節の (6)）。
  ⚠️ **第一世代は、もう作業ディレクトリに無い**（**実測**、2026-09-24——`git status` が `D` を出す）。
  ⛔ **この削除は、この稿では触っていない**（ステージしていない）。

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
- `LIGHT`: the room's constant state — the dim red light of a safelight that stands outside the frame and comes as far as the tray, and the warm amber glow of the developer; ⛔ **枠が持つのは光そのものであって、灯ではない**; no time of day and no directional light
- `ASPECT`: 16:9, landscape

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the first development of the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. In the darkroom of the art board — one windowless room, sunk into near-black except where the light reaches, whose only light is the red light of a safelight standing outside the frame and coming as far as the tray, and the warm amber glow of the developer — a wet silver-gelatin print is held up out of the amber liquid by a hand that enters the frame at its near edge, the fingers pinching the corner — a woman's hand, late fifties, thin, a narrow wrist, long fingers, the nails pared short, the fingertips faintly stained from the developer, the tendons of the back of the hand lying quiet — the sheet lifted clear of the surface and dripping, the liquid in the tray below it still and unbroken, and in the print a face has come up: the outline first, then the eyes open and looking away to one side, then a mouth that closed on something it had started to say. Below the eye, on the image itself, one thumb's mark of grease is left and has not been wiped — the same thumb that holds the corner put it there — a dull matte smudge the width of a thumb's pad lying darker than the silver around it, its surface unreadable, holding no light of its own and catching none, and it is the only mark on the image. The hand's owner stands at the tray with her face outside the frame, and she does not look at the eyes that have come up — the picture looks at them and she does not, and that difference is the whole surface of this board. The white of the paper is silver-white and not the white of paper: it stays silver-white and is not stained red or amber, and the image stands in it without an edge of its own — the silver washing out into the white where the image stops, no even margin and no frame around it, a sheet still coming up and not a finished photograph. The blocking, the camera and the light fixed as the standard every cut of this scene must match: the tray and the print as the subject, the one hand at its edge, the safelight as the only light, the room otherwise still. One scene, one staging. `[絹: woman, late fifties, thin, short black hair faintly streaked with grey gathered loosely at the back, a calm sunken-eyed face, a black apron over a black blouse, hands faintly stained from developing chemicals]` — the figure, whose identity is locked to the frozen setting sheet. The one face that has come up in the print is the face of a woman who would not be photographed, caught in the instant of that refusal — and what the print holds is that instant and not a portrait: the neck turned away and the line of the shoulder standing out strong where it turned, a little of the room's red light pooled in the hollow between the neck and the shoulder, a single loose strand of hair hanging behind the ear and taking the light and going a little white, the eyes open and not on us, gone aside as if escaping something, and the mouth shut on what it had started to say, the lips just parted before they closed and the gap between them gone dark; the only light on the face is the room's red light, crossing it the way it crosses the tray, and the same heavy grain lies over the skin as over everything else in the print, so that the face is no cleaner than the paper around it. It is not the daughter. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, blown highlights on the white paper, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board, the hand filling the space the art board left open. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no glossy photo paper, no digital image on the paper, no glowing or emitting paper, no visible fingerprint ridges, no forensic texture, no legible handprint, no small hand pressing the lens, no youthful face for 絹, no clean unstained hands, no smiling expression, no second figure, no face in the room, no face other than the one in the image on the paper, no open drawer, no second print, no hand touching the eyes in the image, no wiping of the mark, no light source visible in frame, no safelight lamp in frame, no portrait lighting, no beauty light on the face, no soft flattering light on the face, no retouched or smoothed skin, no bokeh, no blurred background inside the image, no soft-focus shoulder, no finished photograph, no frame around the image, no border around the image, no even margin around the image, no broad heavy hand, no sinewy or veined hand, no masculine hand, no sheet lying under the liquid, no liquid over the image, no glossy print surface, no bright evenly lit room

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

## ⛔ 実測（2026-09-23、n=1）と、焼き直しの3点（著者裁定 2026-09-24）

- ⚠️ **焼かれた1枚**——`01_01_*`。**見えたままを書く。**
- ⛔ **芯は在る**——**白から顔が浮かび、眼が横へ逸れ、親指の脂痕が残っている。**
- ⛔ **だが、3つ外れている。**
- ⛔ **（1）灯が、枠に写っている**——**右上に、傘と、明るい口の開いた器具が読める。**
  ⚠️ **そして部屋の奥が近黒でない**（棚が読める）。**`LOCATION` は `near-black` と言っている。**
  ⛔ **原因は肯定の側である**——`LIGHT` と `Prompt` が、器具を名指す既定の1文
  （`the one windowless room whose only light is a dim red safelight`）を持っていた。
  ⚠️ **その1文は `migenzo-art-board` のものである**（**実測**——あのボードの `Merged` に同じ1文が在る）。
  ⛔ **そして否定形では止まらない**——02 は `no lamp` / `no bulb` / `no bare light source` を持ち、
  それでも器具が描かれた（**実測**）。
  ⚠️ **ゆえに肯定の側を書き換えた**——**器具は枠の外に立ち、枠が持つのは光そのものである。**
  ⛔ **`Negative` には2節を足した**（`no light source visible in frame` / `no safelight lamp in frame`）。
  ⚠️ **この2節は、この1枚には初めから1つも無かった**（**実測**: 画像仕様13本でこの綴りを持つのは
  02・05・06-1・06-2・07・08・09・11。**01・03・04・10・12 は持たない**）。
- ⛔ **（2）像の女が、現代のポートレートとして出た**——**効く句が、一般の句に負けた。**
  ⚠️ **口は閉じず、肌は滑らかで、粒は肌の上に乗っていない。**
  ⛔ **原因は語順である**——`an ordinary face at the moment of refusing something` は、
  **「どこにでもいる顔」を先に立て、「拒み」を後ろへ落とす。**
  ⚠️ **ゆえに肯定の側を「拒みの瞬間」に置き換えた**——**頭は半ば巡り、眼は既に横へ行き、
  口は言いかけた語の上で閉じ、肌の上には画面と同じ粒が乗る。**
  ⛔ **否定形は足していない**——**否定形は空欄になり、生成器が衣装で埋める。**
  ⚠️ **次も現代的に読めるなら、次の梃は `Negative` の側である**（**この1枚では、まだ使っていない**）。
- ⛔ **（3）脂痕が、赤く光る指紋として出た**——**隆線が読める。**
  ⛔ **これは、この1枚の `Negative` が既に禁じていた**（`no visible fingerprint ridges` /
  `no forensic texture` / `no legible handprint` / `no glowing or emitting paper`。
  **動画側も `no fingerprint ridges in the mark` を持つ**——**実測**）。
  ⛔ **原因は肯定の側である**——`and it catches the red light` が、光ることを求めていた。
  ⚠️ **ゆえに書き換えた**——**鈍い無光沢のよごれ。まわりの銀より暗い。面は読めない。自らは光を持たない。**
- ⚠️ **`no small hand pressing the lens` は、この焼き直しでも掛かる**——
  **01〜10 の10本が負う床である**（**11 で落ちる**）。
- ⚠️ **この1枚の動画仕様は、灯の節を1つも持たない**（**実測**——動画仕様13本で、
  この綴りが0なのは 01 だけである）。**動画側へ足すかは、著者の裁定に預ける**——
  ⛔ **画像の仕様を直したことは、動画の仕様を直したことではない。**

## ⛔ 実測（2026-09-24、第二世代 n=1）——灯は消え、肖像は残った

- ⚠️ **焼かれた1枚**——`01_01_ChatGPT Image 2026年9月24日 01_16_51.png`。**見えたままを書く。**
- ⛔ **（1）灯は、消えた。** **器具は枠のどこにも無い**（左上・上辺・右奥を拡大して確認）。
  ⚠️ **そして部屋の奥が、今度は近黒である**——第一世代は棚が読めた。**`LOCATION` の `near-black` が守られた。**
  ⛔ **赤は「光そのもの」として出ている**（トレイの縁に落ちる赤、液の左下にたまる赤）。
  ⚠️ **実測**: 肯定の側を書き換えた焼き直しは、これで **7本とも器具を写していない**（6本＋この1枚）。
- ⛔ **（2）像の女は、まだ肖像である。** ただし第一世代とは**外れかたが違う**——
  ⚠️ **粒と口は、今回は仕様の側に在る**（**訂正**）。増感し脱色して拡大すると、
  **肌の上に、像の他の面と同じ粗い粒が乗っている**（第一世代の「粒が乗っていない」は、今回は当たらない）。
  そして**口は閉じている**（「弛んだ口」という読みは、赤い光と艶が作っていた）。
  ⛔ **残るのは、光の宛がいと、面の解像である**——
  **頬に整った光の勾配が乗っており**（`no portrait lighting` が在るのに、である）、
  **像の面では顔だけが解像し、他はぼけている**。**ソースは逆を書いている**——
  `draft_01-2_拒んだ女.md`「避けた先に、**肩の線が強く出ている**」。
  ⚠️ **ゆえに肯定の側へ、ソースの語をそのまま戻した**——**首は避け、肩の線が強く立ち、
  首と肩のあいだのくぼみに赤い光がたまり、耳のうしろの後れ毛が光をうけて、すこし白い。**
- ⛔ **（3）紙が、仕上がった写真として出た**——**均一な白い縁が、像のまわりに在る**（実測、第二世代）。
  ⚠️ **これは 10 の予備の「白い縁」と同じ族である**（11 は禁じ、10 は禁じていない）。
  ⛔ **ゆえに、この1枚にも節を足した**（`no border around the image` / `no even margin around the image` /
  `no frame around the image`）——⚠️ **11 の禁止族と同じ語である。****保留中の裁定に、実例が1つ増えた。**
  そして**肯定の側も書き換えた**——**像は白へ溶け、自分の縁を持たない。**
- ⛔ **（4）手が、絹の手でない。** **腱と血管が立ち、爪は短く四角く、幅がある**——
  **男の手として読める**（実測、第二世代）。仕様は「thin、late fifties、現像液で薄く染まった手」。
  ⚠️ **肯定の側に、絹の手の形を書いた**（細い手首・長い指・短い爪・指先の染み・**静かな甲の腱**）。
- ⛔ **（5）紙が、まだ液から上がっていない**（実測、第二世代）——
  **液面が紙の左側を横切っている。** 仕様の `ACTION` は「**just lifted it clear of the liquid**」。
  ⚠️ **肯定の側を「液の上へ持ち上げられ、雫を垂らしており、下の液面は静かで破れていない」へ直した。**
- ⛔ **（6）脂痕が、読めない。** 眼の下・像の上を、**拡大と増感の両方**で見た——
  **鈍いよごれは、見つからない。**
  ⚠️ **ただし、これは仕様どおりとも読める**——この痕は（2026-09-24 の裁定で）
  「**鈍い無光沢のよごれ、面は読めない、自らは光を持たない**」と書かれており、**空欄に近い**。
  ⛔ **そしてソースは逆を書いている**——`draft_01-3_脂痕.md`「**近づけば、模様の一本一本が
  数えられるほどはっきりしている**」。⚠️ **この1点は、著者の裁定に預ける**——
  **機構の欠陥ではなく、設計の分岐である**（痕を読ませるか、消すか）。
  ⚠️ **この稿で足したのは、位置と大きさだけである**（**親指の腹ひとつ分、像の上に一つだけ、同じ親指が置いた**）。
- ⚠️ **`no small hand pressing the lens` は、この焼き直しでも掛かる**（**実測**: レンズを押す手は、この1枚にも無い）。

## 記録との対応

- `unit` … 「液面に沈んだ、何も浮かんでいない白い印画紙」→
  「線が立ち、眼が浮かび、口元が閉じ、**眼のすこし下に親指の脂痕が一つ残っている**」
- `beats` … 0-3s 待ち時間／3-5s **輪郭**／5-7s **眼**／7-10s **口元・引き上げ・脂痕。**
  ⚠️ **この1枚が切るのは 7-10s の瞬間である**——**`unit.after` そのものであり、このショットの見せ場である。**
  ⛔ **眼は、まだ横へ逸れている**（`draft_01-2`）。
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`・`印画紙`・`脂痕`
  ⚠️ **`attached` の確定は ③ である。** ここに在るのは②の見込みである。
  ⛔ **訂正（2026-09-23、著者裁定）——`絹.identity`・`絹.negatives` を、この見込みから外した。**
  ⚠️ **根拠は `shots/migenzo-ch01-seg01.yaml` の申し送りである**——「⛔ **`絹` を入れない。**
  この1本に絹の手は入るが、**主題は紙である**」。⛔ **そして裁定は「参照画像を付けるのは
  13（アートボード）と 05（設定画）の2本だけ」である**（`PLAN.md` §4-c 問い11・問い14）。
  **ゆえに、絹が自分の設定画を持つのは 05 の1本である。**
  ⚠️ **禁制の側は失われない**——`絹.negatives` の3節は、**この1枚の `Negative` にも既に在る**（実測）。
- ⚠️ **`no small hand pressing the lens` が、この1枚にも掛かる**——**01〜10 の10本が負う床である**
  （幹の逆転を明かさない。`PLAN.md` §2）。⛔ **11 で落ちる。**
- ⚠️ **この1枚の像の顔は、娘ではない。** `PLAN.md` §0-b——**01 で浮かぶのは「拒んだ女」の像である**
  （`話割り.md` 1-2）。⛔ **ゆえに `no fully rendered face of the daughter` は、
  この1枚では「像の顔を空白にせよ」という指示ではない**——**否定形は空欄になり、生成器が衣装で埋める。**
  ⚠️ **肯定の側が「横へ逸れた女の顔」を名指している**（上の `Prompt`）。

## ⛔ 訂正（2026-09-23、著者裁定）——`no face in the frame` を外した

- ⛔ **この1枚は、自分の `Prompt` と衝突していた。** `Prompt` は
  「**and in the print a face has come up**: the outline first, then the eyes open and looking away
  to one side…」と「The one face that has come up in the print is a woman's face turned away…」を
  要求し、**`Negative` が `no face in the frame` と言っていた**——
  **ゆえに、この1枚は自分の主題を禁じうる1節を持っていた。**
- ⚠️ **外したうえで、動画の §16 と同じ文面を置いた**——
  **`no face in the room`**（部屋の側に顔を置くな）＋
  **`no face other than the one in the image on the paper`**（浮かぶ顔は、この1本の内容である）。
  ⛔ **肯定形が既に書いている**——「**The hand's owner stands at the tray with her face outside the
  frame**」——**ゆえに、部屋の側の顔は、禁制でなく内容として落ちる**（否定形は空欄になり、
  生成器が衣装で埋める）。
- ⚠️ **同じ綴りは13枚のうち4枚に在る**（01・06-02・07・09。**実測**）——
  ⛔ **だが食い違っているのは 01 だけである。** 06-02・07・09 の `Prompt` は
  「Her body and her face are not in this frame and there is nobody else in the room.」と
  **はっきり書いており、そこではこの節が正しい。** **ゆえに、この3枚は触っていない。**
