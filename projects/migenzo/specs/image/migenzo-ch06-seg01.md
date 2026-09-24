# 画像仕様 — 『未現像』第6章「二人目・三人目」 第一のショット「吊り線のうえで、一枚ではなくなる」（総覧 / motion / 8s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⛔ **この1本は、この作品で唯一 `総覧` の役を持つ1本である**（`PLAN.md` §1 の註）。
⚠️ **ゆえに、この1本に出来事を置かない。** **量そのものが出来事である。**
⛔ **そして、この1枚に手を入れない**——**吊るす行為は、この1本の前に終わっている。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch06-seg01.yaml` ＋
  **既存の出力**——`migenzo-art-board/prompt.md` と、同じ暗室の `migenzo-scene-board/prompt.md`
  （⚠️ **`_backup_20260905/` は参照しない**）
  ⛔ **人物の設定画は要らない**——**この1本に人物は入らない。**
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch06-seg01.yaml`（`key_image`）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）。
  ⚠️ **第二世代が在る**——`06_01_ChatGPT Image 2026年9月24日 00_56_44.png`（2026-09-24、焼き直し）。
  ⚠️ **第一世代は、このディレクトリに無い**（**実測**、2026-09-24——このディレクトリの `06_01_*` は、この1枚だけである）。
  ⚠️ **`git status` は、この位置について何も言わない**——**第一世代が在った場所を、この稿は見ていない**（追跡されていた形跡も無い）。
  ⛔ **著者裁定（2026-09-24）——この1枚を採用する。** **選んだのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。

  ⛔ **同じディレクトリの `06_02_*` は、この仕様のものではない**——**あちらは `migenzo-ch06-seg02.md`
  （第二のショット「差し出す。」）の1枚である**（⚠️ **ファイル名は章番号と枝番である**）。

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: a line of drying prints where the quantity itself is the event — one sheet is not what is hanging there
- `CHARACTERS`: no figure in frame — ⚠️ **この1本に人物は入らない。** **吊るした者は、もうこの枠に居ない**
- `SUBJECT`: a line strung across the darkroom with many silver-white prints hanging from it by small clips, seen from behind, dry and opaque, standing one behind another further than the frame goes
- `ACTION`: the light no longer passing through the paper — it now lies on the surface — while the sheets sway a little, less and less as they dry
- `LOCATION`: the darkroom of the art board — one windowless room, the line crossing it, the developer tray and its amber liquid standing back in the same island of light, behind the paper and out of focus
- `LIGHT`: the room's constant state — the dim red light of a safelight that stands outside the frame, and the warm amber glow of the developer tray; ⛔ **枠が持つのは光そのものであって、灯ではない**; ⛔ **この1本の光は、紙を抜けない。紙の表面に在る**（乾いたからである）
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は `unit.after` である**——「**乾いた。光はもう通らない。白い紙が、何枚も、
互いのうしろに並んでいる。**」
⚠️ **理由**: この1本の答えは「**一人ではない**」が、**数えられないこと**で届くことである。
⛔ **`before` を焼けば、この1枚は「濡れた紙が光っている」画になる**——
**それは美しいが、量を持たない。** ⚠️ **この1本の役は `総覧` である。**
⚠️ **そして、この1枚は紙の裏を見ている**——**ゆえに、紙のうえの像は、この画に無い。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the line of drying prints in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The darkroom of the art board: one windowless room lit by a safelight that stands outside the frame — what is in the frame is the red light it makes, and not the fixture that makes it — with the developer tray and its amber liquid standing back in the same small island of light, behind the paper and out of focus so that its surface is not a face in this frame. A line is strung across the room, and a great many silver-white photographic prints hang from it, each one held by a small clip at its top edge, and we are looking at their backs: the paper side, not the picture side, so that nothing on them is legible as a photograph. They are dry now — the light no longer passes through them, and instead of glowing from inside they are simply pale opaque sheets, one standing behind another, further back than the frame goes, so that at the front the sheets can still be picked out and past the first several they cannot be counted at all, and the row continues out of the frame on both sides. A few of them are still moving a very little, and the movement is getting smaller as they dry. Nothing is being hung up and nothing is being taken down; no one is in this frame. `[no figure in frame]` — the line and the paper, and the light lying on the surface of the paper. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no person, no figure, no body, no hand, no fingers, no arm, no face, no readable photograph on the paper, no face on the paper, no portrait on the paper, no image visible on the facing side, no picture side of the paper turned toward us, no developed image, no image on the film, no glowing paper, no paper lit from inside, no self-luminous paper, no light passing through the paper, no translucent sheet, no digital image on the paper, no glossy photo paper, no inkjet print, no ink, no bubble jet texture, no digital noise on the paper, no torn sheet, no creased sheet, no fallen sheet on the floor, no peg or clothespin in a hand, no printing line or rope of laundry, no clothing on the line, no towel, no bedsheet, no counting of the sheets made easy, no neat row of evenly spaced identical sheets, no symmetrical grid, no evenly measured spacing, no small number of sheets, no single sheet, no two sheets, no visible end of the line, no reel or spool, no tongs, no tray with paper in it, no bottles or jars, no enlarger, no light source visible in frame, no safelight lamp in frame, no lamp, no bulb, no bare light source, no bright evenly lit room, no studio backdrop, no product photograph of hanging prints, no gallery wall, no frames, no pegs on a wall

---

## ⛔ 紙は「裏側」を撮る——この1本の設計である

- ⚠️ **原文は、濡れているあいだ紙が光を通すことを書く**——
  「**赤い安全光が紙の裏を抜けて、白が内側からうっそりと光っている**」。
  ⛔ **裏から抜けるということは、この1本は紙の裏を見ている、ということである。**
- ⛔ **そして、この設計は、この作品の最も重い禁制と両立する**——
  **紙の表に像を描かなければ、そこに顔は生まれない。**
  ⚠️ **`娘.identity` の三義（顔の無限）に触れずに「量」を撮る道は、この1本ではこれである。**
- ⚠️ **`shots/migenzo-ch06-seg01.yaml` の申し送り**——**`印画紙.negative` の
  `no digital image on the paper` / `no glossy photo paper` は、この設計と両立する。**
  ⛔ **だが `未露光のフィルム.negative` の `no developed image` を、この1本へ引いてはならない**
  ——**この1本の紙は、現像された紙である。**
  ⚠️ **ゆえに `no developed image` は、この1枚の `Negative` に無い。**

## ⛔ 量は、枠の外へはみ出したまま置かれる

- ⛔ **カメラはパンしない**（`shots/migenzo-ch06-seg01.yaml` の `law`）——
  「**線の端まで振れば、「量」を見せるための運動になる**——**それは never to make a point に反する。**」
- ⚠️ **ゆえに、この1枚は、線の端を焼かない。**
  ⛔ **`no visible end of the line` がそれである**——**はみ出していることが、量である。**
- ⛔ **そして `no neat row of evenly spaced identical sheets` / `no symmetrical grid` を落とす理由**——
  **等間隔の整列は、「数えられる」という読みを生む。**
  ⚠️ **この1本は、数えられないことを撮っている。**

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である。**

## ⚠️ 実測（2026-09-23、n=1——候補であって採用ではない）

- ⚠️ **焼かれた1枚**——`06_01_*`。**見えたままを書く。これは欠陥の指摘ではない。**
- ✅ **設計は保たれた**——**紙は裏側で、表の像は無い。** **白は銀塩の白で、発光していない。**
  **紙は乾いており、不透明で、互いのうしろに並んでいる。** **量は多く、線の端は見えない。**
- ⛔ **だが、赤い安全光の灯そのものが、枠の左上に入っている。**
  ⛔ **13枚の画像仕様のうち、枠の内の光源そのものを名指して禁じる節を持つのは2枚だけである**
  （実測、2026-09-23——**基準は「光源そのものを名指して禁じる節の有無」である**。② が明記した）——
  **`ch02-seg01` は `no lamp` / `no bulb` / `no bare light source` を持ち、`ch11-seg01` は
  `no light source visible in frame` / `no safelight lamp in frame` を持つ**
  （⚠️ **ファイル名の番号である。ショット番号では 03 と 12**）。
  ⚠️ **この基準に数えない節が、ほかの11枚に在る**——
  `no bright evenly lit room`（**13枚すべて**——**明るさの状態であり、光源を名指していない**）／
  `no lamp beyond the door`（`ch05`・`ch08`——**扉の外の光であり、枠の内の光源ではない**）／
  `no dramatic spotlight into the drawer`（`ch04`）と `no spotlight`（`ch07`）——**当てかたの節である**／
  `no lit wall`・`no lit back wall`（`ch09`）——**照らされた面の節である**／
  `no paper lit from inside`（**この1枚**）と `no body lit from the front`（`ch08`）——**向きの節である**。
  ⛔ **ゆえに「残る9枚は、光源について何も言わない」は成り立たない**——**初稿の書きぶりである。**
  ⛔ **この1本の画像仕様は、それを持っていなかった**（下の `Negative` を見よ）。
  ⚠️ **動画の仕様（`specs/video/migenzo-ch06-seg01.md` §16・§18）は、それを足した**——
  **「光は、方向ではなく状態である」**（`bible.constants.光`）**からの帰結として。**
  ⛔ **ゆえに、この1枚を参照画像として添付するなら、§16 と参照画像が食い違う。**
- ⛔ **裁定（2026-09-23、著者——「推奨で進めよ」）: 焼き直す。** **直したのは3点である。**
  ⚠️ **（1）灯**——**肯定の側を直した。** **灯は枠の外に立ち、枠が持つのはそれが作る赤い光である。**
  ⛔ **そして `Negative` に、動画の仕様と同じ5節を足した**
  （`no light source visible in frame` / `no safelight lamp in frame` / `no lamp` / `no bulb` /
  `no bare light source`）。
  ⚠️ **02 と違い、この1本は否定の側を最初から持っていなかった**——
  **02 は「禁じていたのに描かれた」、この1本は「禁じていなかった」。** **同型の欠陥である。**
  ⛔ **（2）トレイ**——**著者へ渡した表では触れていない1点である**（**約束より1つ多い**）。
  **`LOCATION` とプロンプトに「奥に立ち、面にしない」を足した**——
  ⚠️ **動画の仕様 §4・§16 はそれを要求しており、この画像仕様は書いていなかった。**
  ⚠️ **（3）等間隔**——**これは仕様ではなく生成の側の外れである。**
  **`no neat row of evenly spaced identical sheets` は既に在る。****ゆえに1節も足していない。**
- ⚠️ **この1本に、他の食い違いは見えていない。**

## 記録との対応

- `unit` … `before`「**まだ濡れている印画紙**が並んでいる。……**赤い安全光が紙の裏を抜けて、
  白が内側からうっすらと光っている。**」→ `after`「**乾いた。光はもう通らない。
  白い紙が、何枚も、互いのうしろに並んでいる。**」
- `beats` … 0-3s 濡れた紙と、留めているものが見える／3-5s **乾き——光の抜けかたが、
  白の内側から表面へ移る**／5-8s **乾いた紙が、重なりながら並んでいる。**
  ⚠️ **この1枚が切るのは 5-8s である。**
- ⛔ **発光させない。** **乾きであって、光ではない**——
  ⚠️ **`bible.negative_base` の白の節**「**the white stays silver-white**」が、ここで効く。
- ⚠️ **この1本の最後に残るのは、量だけである。** ⛔ **ここでカメラを引かない。**
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`・`印画紙`
  ⛔ **人物の鍵を置かない。** ⚠️ **`attached` の確定は ③ である。**
