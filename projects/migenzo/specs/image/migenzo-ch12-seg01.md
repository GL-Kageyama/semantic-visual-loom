# 画像仕様 — 『未現像』第12章「白」 第一のショット「なにも浮かばない印画紙」（離脱 / still / 9s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⛔ **この1本は、この摘要版の最後の1本である。**
⛔ **そして、最初に焼く2枚のうちのもう1枚である**——**著者の指定**（`PLAN.md` §4-c 問い10、
裁定 c）「**最初に焼く2枚は、著者の指定である——11（山）と 13（白）。**」
⚠️ **この2枚で、この作品の画面が決まる。** ⛔ **そして、この2枚は、この作品の両端である。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch12-seg01.yaml` ＋
  **既存の出力**——場所は `distill-essence-engine/examples/migenzo/migenzo-art-board/prompt.md`、
  同じ暗室の既存ボードは同 `migenzo-scene-board/prompt.md`
  （⚠️ **`_backup_20260905/` は参照しない**——依頼の指定である）
  ⛔ **人物の設定画は、この1枚には要らない**——**この枠に人物が居ないからである。**
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch12-seg01.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。⚠️ **まだ1枚も無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `documentary-photo` —— 5つの穴（`SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`）

⚠️ **`SCENE`・`ACTION`・`LIGHT` は両方のカードに同名で在る**——**同じ値が両方の穴に入る。**
5＋5＝10 ではなく、**和は7**である。

- `SCENE`: the white — a sheet pulled out of the liquid with nothing on it, and the room's red light crossing it
- `CHARACTERS`: no figure in frame — ⛔ **この作品で唯一、人物の居ない1枚である**（13本のうち12本に人物が居る）
- `SUBJECT`: one wet silver-gelatin sheet hanging in the air above the tray, silver-white and blank, a pair of tongs pinching its corner, and a band of red light lying across it
- `ACTION`: the sheet held still in the air, its last water already fallen, the light crossing the white and the white taking a little of it and staying white
- `LOCATION`: the darkroom of the art board — the light island: the tray with its amber liquid at the center, its surface still at last, and everything outside the red light's reach sunk in the darkness that has been along those walls for twenty years
- `LIGHT`: the room's constant state — one dim red safelight and the warm amber glow of the developer tray, the paper catching both and staying silver-white; no time of day and no directional light. ⛔ **光の島の縁は、この枠に入る**——**赤から闇への変わり目が、この1本の境界である**
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は `unit.after` である**——**白が、決まらないまま、決まったところである。**
⚠️ **理由が3つある。**
**（1）この1本の主題は、白である**（`shots/migenzo-ch12-seg01.yaml`）——
**`unit.after`「なにも浮かばない。白いままだった。」が、この1本の答えそのものである。**
**（2）⛔ 「像が消えかけている」状態を錨にすれば、錨が消えかけの像を固定する**——
**この1本が消しているものを、参照画像が保ってしまう。**
**（3）この1本の変化は、可逆でない**——**液から出て乾けば、白はもう変わらない。**
⚠️ **ゆえに錨は、変わらないほうを焼く。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the last white of the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. In the darkroom of the art board, the light island: a developing tray with amber liquid at its center, the surface now still, and beyond the reach of the red safelight the room's unlit faces sunk in the darkness that has been settled along those walls for twenty years — and the edge where the red gives way to that darkness is held inside this frame. Above the tray, one wet silver-gelatin sheet hangs in the air, held at its corner by a pair of tongs that come in from outside the frame, and no hand is on them in this frame. The sheet is blank: nothing has come up on it, no outline, no trace, no mark at all — just the white of silver gelatin, and that white is not flat, because the sheet is still wet and the wet surface holds a faint sheen that catches the light. A band of red light lies across the white, and the white takes a little of it and stays white, exactly where it is. The paper the white is on is the heaviest thing in the room. `[no figure in frame]` — this is the one frame of the work in which nobody stands: no hand at the tray, no person holding the tongs. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board, the tray filling the space the art board left open. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no glossy photo paper, no digital image on the paper, no glowing or emitting paper, no visible fingerprint ridges, no forensic texture, no legible handprint, no person, no figure, no hand, no fingers, no arm, no face, no silhouette, no child's hand, no image on the print, no faint trace of an image, no residue of an image, no ghost of a face, no outline on the paper, no mark on the paper, no stain on the paper, no yellowed or aged paper, no torn or creased sheet, no flat featureless rectangle of pure white, no blown-out white with no texture, no water drops falling, no splash, no ripple on the surface, no tongs held by a visible hand, no second sheet, no second tray, no open drawer, no bottles or jars, no enlarger, no print hanging on a line, no bright evenly lit room, no portrait lighting, no smiling, no sad expression anywhere

---

## ⛔ この1枚では、床と内容が一致する——この作品で唯一

- ⚠️ **`no image on the unexposed film` / `no readable text` / `no lettering in frame` は、
  13本すべてに掛かる**（`bible.negative_base`）。⛔ **そして、この1本では、
  それらが初めて「撮りたいもの」と一致する**（`shots/migenzo-ch12-seg01.yaml` の申し送り(3)）。
  **禁制と内容が一致する1本は、この摘要版でこれだけである。**
- ⛔ **だが `negative` は名詞を消せない**（hakuchizu の実測）——
  **ゆえに、肯定文の側が「白」「銀塩の白」「なにも浮かんでいない」を名指す。**
  ⚠️ **上の `Prompt` がそれを名指している**——**「no outline, no trace, no mark at all」は
  禁制でなく内容の記述であり、その直後に「just the white of silver gelatin」と肯定している。**
- ⚠️ **`no flat featureless rectangle of pure white` を落とす理由**——
  ⛔ **「何も無い白」は、白い矩形ではない。** **湿った面の艶が在り、赤い光の帯が在る。**
  **それを禁じれば、この1枚は空の紙になる。** ⚠️ **`ledger.props.印画紙` の註**——
  「**何も浮かばない白も、この物の姿である（S13）。それは失敗した現像ではない。
  何も浮かばない印画紙は、この世界で最も重い像である。**」
- ⚠️ **`no small hand pressing the lens` は、この1枚に掛からない**——
  **あれは 01〜10 の10本が負う禁制であり、11 で落ちている**（`ledger.disclosure`、
  `negative: changed`。**動きかたは「削除」である**——入れ替えではない）。
  ⛔ **ゆえに、この1枚の `Negative` 段落に、その句は無い。**
  ⚠️ **`bible.yaml` の註が「S11 より前の10本にだけ掛かる」と書いているのは、これである。**
  ⛔ **そして、この1本では「手が無い」ことが内容である**——
  **ゆえに、この1枚の `Negative` の「手」の節は、禁制ではなく記述として置いてある**
  （`no person, no figure, no hand` — **無人であることが、この1本の内容である**）。
  ⚠️ **隣の `no child's hand` は、この1枚自身の記述であって、落ちた句ではない。**

## ⚠️ 錨が「白」であることの危険を、申告する

- ⛔ **この1枚を錨にすると、動画の 0-6s が消すもの（像の最後の輪郭）が、錨に無い。**
  ⚠️ **ゆえにこの1本の「うすくなって、消えていく」は、§11 MOTION の散文だけが持つ。**
- ⚠️ **採った読み**: **この作品の最後の状態は、白である。**
  **消えかけを錨にすれば、錨のほうが強い**——**参照画像は、そこに在るものを保つ。**
  ⛔ **そして、この1本の `unit.before` は「像の最後がまだ残っている」であるから、
  錨に before を焼けば、この1本は「消えかけから、消えかけへ」になる。**
- ⚠️ **これは分岐であり、隠さない**——**もし著者が、焼いた動画で輪郭が消えずに残ると見たら、
  この1枚だけ、`unit.before` の「いちばんうすく残った小さな手」で焼き直す道がある。**
  ⛔ **その場合も、白の側は変わらない**——**変わるのは、錨が「消える前」を持つかどうかだけである。**
  ⚠️ **判断は著者である**（画像は著者が焼き、動画も著者が回す）。

## ⚠️ `Not photorealistic` を、ここに写してはならない

- ⛔ **既存ボードの `Merged` の末尾の否定列にあるあの句を、この1枚も持たない**——
  **裁定（2026-09-23、著者）「入れない（推奨）」。** ⚠️ **根拠は `migenzo-ch01-seg01.md` の同じ節である。**
- ⛔ **様式カードの `available natural light` も写さない**——**赤い安全光は到着しない。
  時刻を持たない、その場所の恒常の状態である。**

## 記録との対応

- `unit` … `before`「像は、消えかけている。最後に小さな手がうすくなって、消えていった。
  その小さな手が、まだ、いちばんうすく残っている。水が、紙の下の角へ集まって、ひとつ、落ちる。」
  → `after`「**なにも浮かばない。白いままだった。** 水は、もう、落ちていない。
  赤い光が、白のうえを流れている。**白は、その光をすこし吸って、それでも白いまま、そこにある。**」
- `beats` … 0-3s 宙にある、濡れた1枚／3-6s **像が白へ戻りきり、水が二度落ちる**／
  6-9s **白。赤い光が、そのうえを流れる。** ⚠️ **この1枚が切るのは 6-9s である。**
  ⛔ **水滴を、この1枚に置かない**（`draft_12-1`「**ぽた、ぽた、と二度、音がして、それきり**」）——
  **「それきり」が、この1本の終わりである。**
- `role: 離脱` … ⚠️ **この1本の境界は、光の島の縁である。**
  ⛔ **ゆえに、この1枚は島の縁を枠に入れる**——**縁が写らなければ、「紙が液の外に在る」ことが消える。**
  ⚠️ **「出た先」は、この摘要版では撮らない**（`PLAN.md` §0-e——**外は、この画の外に無い**）。
- ⚠️ **この1枚に、絹の顔も、絹の手も、トングを握る手も無い。**
  **残るのは、紙と、トングと、島と、赤い光である**——**道具だけが入る。**
  ⛔ **トングは台帳に鍵を作らない**（`ledger.props` の註）。**この道具は状態を持たない。**
- `place` / `time` … `最後の暗室` / 時刻を持たない
- `attached`（見込み）… `最後の暗室.base`・`最後の暗室.geography`・`印画紙`
  ⛔ **人物の鍵をひとつも引かない**——**この作品で唯一の1本である。**
  ⚠️ **`attached` の確定は ③ である。** ここに在るのは②の見込みである。
- ⛔ **この1枚の `Negative` は、動画の §18 の写しではない。** 同じ床を、
  **効く場所（画像の経路の否定パラメータ）へ置いたものである**——
  ⚠️ **動画の経路（`WAN 3.0`）は、字幕と音声だけを否定として扱い、残りを散文として読む**（`L30`）。
