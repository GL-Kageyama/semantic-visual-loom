# 画像仕様 — 『ハビッツ！！！』第二巻『重なった名』 第7話「表札と宛名票」 第二のショット「宛名票の名が、目で、表札へ運ばれ、重ならないところで、止まる」（所作 / motion / 12s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この紙は、この作品で最初の画像仕様である。** `projects/habits/specs/image/` は
**これまで空だった**（第一話の三枚は `MINIMAX H3` で、参照するのは絵コンテであって
`key_image` ではない）。ゆえに `L18` の註「5 本が `key_image` を持たない」は**4 本になる**。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは回さない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-ch02-seg07.yaml` ＋
  `distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md`（設定画 改訂稿5）
- 投入する文: **下の節の1段落目が `Prompt` であり、エンジンの出力であって、`chatgpt-image-2.5` へ
  投入する正典である**（決定B）。**2段落目が `Negative` である**（決定A）
- ⚠️ **下の7欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`REF_FORMAT` と `REF_STYLE` が「どのカードの穴か」を名乗る。** `L22` がそれを読み、
  **名乗ったカードが実際にその穴を宣言しているか**を確かめる——**名乗りは宣言であって、一致ではない。**
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**——
  **見出しが本文の間にあると、選択がそれを巻き込む。** 空行1つが、そのまま `Negative` を
  繋ぐ空行である。**繋がった文字列の写しは置かない**（写しは食い違う）。
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **そして `first_frame` は、このショットでは二重に選べない**——この経路の先頭フレームの型は
  **`ratio: adaptive` を要求する**ので、`16:9` を名乗れなくなる（`specmap.MODELS` の註）。
- 記録: `shots/habits-ch02-seg07.yaml`
- 生成物の置き場: このディレクトリ。⚠️ **実測（2026-09-21）——出力は
  `ChatGPT Image 2026年9月21日 13_57_54.png` として在る**（2,169,206 B、
  `sha256 5557edd3…`）。**この行が名乗っていた `habits-ch02-seg07.png` ではない。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the midday sun dividing the nameplate on the post into a lit half and a shadowed half
- `CHARACTERS`: `[暮林蒼: man, twenty-six, black hair cut short, tall, a work jacket and cap]` — the only figure, standing still, the box held in the crook of his arm
- `SUBJECT`: the wooden nameplate on the gatepost and the printed address slip glued to the side of the box
- `ACTION`: standing still with his eyes up at the plate, having stopped where the two sets of characters do not overlap
- `LOCATION`: the front of a private house on a narrow street in Adachi, Tokyo, at midday
- `LIGHT`: the sun taking the right half of the plate, the left half in the post's shadow
- `ACCENT`: the sunlit right half of the plate as the brightest thing in the frame, the carved hollow beside it catching no light

⚠️ **人名はローマ字にしない**（決定）。**ゆえに括弧の中の名だけが日本語の字で、記述は英語である**
——**家の規約は「生成に渡す文字列は英語」であり、人名の字種はその外にある。**
**この二つは矛盾しない。** ⚠️ **綴りを直さないこと。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of the wooden nameplate on the gatepost and the printed address slip glued to the side of the box, standing still with his eyes up at the plate where the two sets of characters do not overlap, at the front of a private house on a narrow street in Adachi, Tokyo, at midday, with the sunlit right half of the plate as the brightest thing in the frame and the carved hollow beside it catching no light. A scene board for the master staging of this one scene, in 16:9 — the blocking, the camera and the light fixed as the standard every cut of the scene must match. One scene, one staging. `[暮林蒼: man, twenty-six, black hair cut short, tall, a work jacket and cap]` is the only figure and he is in place: a last-mile delivery courier, the tallest of the figures this work draws, his identity locked to the frozen setting sheet — the forehead broad with the cap worn shallow so the breadth still reads, cheekbones spreading wide and setting the width of the face, a short jaw whose corner stands with a square chin, a long nose with the tip falling, large ears standing out sideways, the spacing of the eyes left to the style; a handheld terminal clipped at one hip so the belt dips on that side alone; the age carried not by the face but by the forearms, the skin below the sleeve darker than the face and the skin the sleeve covers paler than either. The box is held in the crook of his arm, its corner pressed white into the palm, and the box is not set down. **No expression is placed on the face.** The nameplate: wood, square, screwed to the post, **two characters cut into the grain with the hollow filled with black, the upper half of the plate faded lighter than the lower, four rounded corners, two screw heads with cross slots** — **carved, not painted, and not readable.** The address slip, turned to the camera, glued to the side of the box: paper, ruled into four fields, **the topmost field carrying two characters printed flat and even-edged in black ink, laid on the surface rather than cut into it** — **printed, not carved, and not readable.** **The two sets of characters are drawn as different marks — one cut into wood and filled black, the other printed flat in ink — and neither set can be made out: they are present in the picture and unreadable.** This is a Japanese work and these are Japanese characters, set in the Japanese script. A worn stone at the foot of the post with one chipped corner, a closed sliding door with glass, and nothing readable behind the glass. Hyper-detailed layered light: bloom where the sun crosses the post, a faint anamorphic flare crossing the lens, dust suspended in the air in front of the post and individually rendered rather than a flat wash. A saturated palette with the warm side held to the lit half of the plate and to skin, deep cyan in the post's shadow, the grey of the stone, the pale of cardboard, the white of the slip, the warm brown of the post. Clean anime lineart at one thin even weight with no thickening at the contour, kept deliberately below the light; cel shading held to a single shadow tone per material with the boundary left crisp. Composition medium and slightly low — the lens sits below his eye line, and the plate and the slip are both in the picture because he is looking at them, the frame never turning to read either. Generous negative space and low visual density.

no legible name text, no legible name on any in-world prop, no legible text on the address slip, no legible text on the nameplate, no legible text on any surface, no readable house number, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank nameplate, no empty plate, no painted letters on the nameplate, no flat characters where the carving should be, no printed characters where the carving should be, no carving where the printing should be, no signature, no handwriting by the courier, no calling voice as a sound effect, no face before the name is called, no character added beyond the shot, no unnecessary character, no resident at the door, no opened door, no receiving hand, no passer-by added, no bystander added, no second person with the courier's face, no second person wearing his cap or his jacket, no completed delivery, no setting the box down, no handing over, no knock, no doorbell, no smile, no tears, no fear, no exaggerated expression, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no watermark, no cut to a legible insert, no close-up on the writing, no wide sky-heavy composition, no low horizon, no dusk palette, no magenta and gold dusk sky, no sky as the subject, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces, no morphing or drifting facial identity, no rounded jaw, no short nose, no small ears, no face younger than the age stated, no wall clock, no calendar, no digital timer, no date stamp

---

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **ゆえに、この作品の禁制が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**空白の面**と**偽の字**——を禁じているのは、**この段落である。**
  動画の §18 にも同じ句が在るが、**あちらでは助言に落ちる。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**5節**——
  基盤の3節（`no watermark`／`no on-screen subtitles`／`no background music`）と、
  この作品の2節（`no calling voice as a sound effect`／`no face before the name is called`）。
  **画像の `Negative` にも同じ床が掛かる**（`semantic._negative_of` の `image` の枝）。
- ⚠️ **ゆえにこの段落は、動画の §18 の写しではない。** **同じ床を、効く場所へ置いたものである。**

## ⚠️ `no Japanese kanji or kana` を、ここに写してはならない

- 姉妹作品 `hitosara` の画像仕様の `Negative` は、この句を持つ。**この作品は持たない。**
- 根拠は**この作品の映画の層自身が書いている**——`specs/video/habits-ch02-seg01.md:36-38`:

  > ⚠️ **人名はローマ字にしない**（決定）。…**日本語の字のまま置く。**
  > ゆえに Negative は「**読める名**」を禁じるのであって、**字種を禁じない**——
  > `no Japanese kanji or kana` は**使わない。使えば、名そのものが消える。**

- ⚠️ **禁じているのは可読性であって、字種ではない。** この段落の先頭の十句がそれを負う
  ——`no legible name text` から `no nonsense glyphs` までである。
- ⚠️ **そして、この区別は「本物の字形を要求する」側でもある。** 禁じるのは**読めること**と
  **偽物であること**の二つであり、**本物の彫りと本物の印刷は、要求されている。**

## ⚠️ 構図は、様式カードの Visual breakdown から離れる（ずれの宣言）

- `luminous-anime` の Visual breakdown は「**wide and sky-heavy, a low horizon, the light source
  inside the frame or just outside its edge; the figure small against the world**」と言う。
- **この1枚はそうしない。** 置き場は**家の前の、狭い道**であり、**中距離・やや low**である
  ——**空は主題ではない。**
- ⚠️ **根拠は好みではない。** このショットの §10 が**カメラを決めている**——
  「**the lens sits below his eye line throughout: the plate and the slip are seen because he is
  looking at them, and the frame never turns to read either. Keep this framing medium.**」
  **これが `LOCATION` と画角を決める。**
- ⚠️ **そして、この形の欠陥は実測で出ている**（`L22` の註——画像仕様が様式カードだけを名乗り、
  10本の `Prompt` の構図が**どのカードからも来ていなかった**）。
  **ゆえに `scene-board` を名乗り、ずれをここに書く**——**ずれは黙って起きるのではなく、
  宣言して起きる。**
- ⚠️ **`Negative` は、カードの構図を名指しで禁じている**——`no wide sky-heavy composition`／
  `no low horizon`／`no sky as the subject`。**様式の色も同じ**——`no dusk palette`／
  `no magenta and gold dusk sky`。**この場面の光は、正午の太陽である。**

## ⚠️ 設定画の PNG を、この1枚と一緒に添付しないこと

- ⚠️ **実測（2026-09-21、私が開いて見た）**——`distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/`
  に在る2枚の PNG（設定画 改訂稿5・表情シート 改訂稿7）は、**どちらも読める日本語の字を持つ**
  ——「暮林蒼」「改訂稿5」「改訂稿7」「様」「たろう」、および6つの軸の註。
- ⚠️ **このショットの前提は「読めない名」である。** そして**添付は、テキストの指定に勝つ**
  ——この作品が既に踏んでいる（「添付画像の服がテキスト指定に勝つ」）。
- **ゆえに、この1枚を動画へ添付するとき、設定画の PNG を並べない。**
  ⚠️ **§6 の `REF_CHARACTER` が指すのは `prompt.md`（改訂稿5）であって、その PNG ではない。**
- ⚠️ **これは推測ではなく、二つの実測の重なりである**——**字が在ること**と、
  **添付が勝つこと**。**どちらも、この作品の中で既に確かめられている。**

## 記録との対応

- `unit` … 「宛名票の名が、紙の上にあり、まだ表札へ運ばれていない」→
  「運ばれた名が表札のところで無く、目が、**重ならないところで止まっている**」
- `beats` … 0-3s 柱と表札／3-6s 宛名票／6-9s 往復／9-12s **止まる。**
  ⚠️ **この1枚が切るのは 9-12s の瞬間である**——**`unit.after` そのものであり、
  このショットの見せ場である。** ただし**目はまだ上にあり、顔は置かれ、表情は置かれない。**
- `place` / `time` … `表札と宛名票` / `昼（届け先の玄関の前）`
- `attached` … `暮林蒼.identity`・`暮林蒼.negatives`・`表札と宛名票.base`
- ⚠️ **`text_channel` の2本は、この1枚にも掛かる。** 表札の字と宛名票の字は、
  **どちらも生成器が描く**（`lettering`）——**ゆえにこの1枚が、その描き方を決める。**
  **ここで偽の字が出れば、動画の側でも出る。**
