# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第七のショット「手が一枚をつまみ上げ、面をこちらへ向ける」（所作 / motion / 2.473s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、`chorus-1` の3本目である**（動画の仕様 §19——`Segment ID: chorus-1-3`。
`chorus-1` は `s05`・`s06` と、この1本である）。
この1本の行は `l06`「**読む手は、誰の手。**」であり、`aim` は
「**この曲で最も字義どおりの1行を、最も字義どおりに撮る。** 「読む手は、誰の手。」——**手しか映さない。**」と言う。
⛔ **ゆえにこの1枚は、手と紙しか映さない。** 動画の仕様 §3 はこの1本を
「**この作品で最も厳密に「誰も居ない」1本である。** **手と紙以外は、何も置かない。**」と書き、
§6 は「**この1本は `identity` を添付する** — 手の造形がこの人物のものであるためである。
⚠️ **顔は置かない。**」——**渡す一枚と、画面に置くものは、別である。**
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——`unit.after` は
「手が札を一枚つまみ上げ、**面をこちらへ向けている。**」。**面はこちらを向くが、字は読めない。**
⚠️ **この現場は、サビの14本が共有する現場である**（`ledger.yaml` の `名札` の註——
「**サビの14本は、すべてこの現場である。** ——**「読む手は、誰の手。」の現場である。**」）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s07.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a piece of paper held up between two fingers.**」
    ——**動画の側が先に、この様式を「指の間の一枚へ翻訳した」と書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s07.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/03_高橋由美/ChatGPT Image 2026年9月20日 19_50_54.png`
  （**凍結した人のかたちの一枚**。`ledger.yaml` の `高橋由美.identity` が指す先であり、動画の仕様 §6 も同じ先を指す）
  ＋ 同じ作品の既存の生成物（`media/` の3本の動画）
- 添付する参照: **`specs/image/生成時参照イラスト/s07/` の1枚**——`高橋由美_設定画.png`。
  ⚠️ **この1枚は、この作品の動画の側の同じ1枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s07/`。実測 2026-09-28、ハッシュが一致した）。
  ⚠️ **置き場を2つに分けたのは、経路が2つだからである**——**この作品は「画像 → 動画」の順に走り、
  参照を渡す先が、それぞれ別である。** ⛔ **片方を差し替えたら、もう片方も差し替える。**
  ⛔ **これは用意であって、添付ではない。** `attached` を書くのは、送った日である。
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative` である。**
  `chatgpt-image-2.5` へ投入する正典は、**この2段落そのものである。**
  ⛔ **但し、この2段落は `distill-essence-engine` の出力ではない**——**この稿で、2枚のカードの穴と
  動画の仕様から、私（Claude）が組成したものである**（実測 2026-09-28）。⚠️ **エンジンは一度も回っていない。**
  ⛔ **「エンジンの出力である」と書いてはならない**——**出所の名乗りは、そのまま出典として読まれる。**
  ⚠️ **回して出た `Merged` と差し替えるか、この2段落をそのまま使うかは、著者の裁定である**——
  決定C は「`Prompt` は `distill-essence-engine` が作る」と言っている。
- ⚠️ **下の7欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`REF_FORMAT` と `REF_STYLE` が「どのカードの穴か」を名乗る。** `L22` がそれを読み、
  **名乗ったカードが実際にその穴を宣言しているか**を確かめる——**名乗りは宣言であって、一致ではない。**
  ⚠️ **この組では、2枚のカードの穴の和が、そのまま下の7欄である**（実測 2026-09-28——
  `distill-essence-engine` の `references/formats/scene-board.md` の
  `## Environment variables` は `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT` を、
  `references/styles/luminous-anime.md` の同じ節は `SUBJECT`／`ACTION`／`LOCATION`／`ACCENT` を宣言している）。
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** 様式カードの雛形は
  `Not photorealistic, …` で終わるが、**この作品はそれを2段落目に置く**——**この作品は実写ではない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s07` §6——「**この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が「面をこちらへ向けた一枚」を写すのは、そのためである**——
  **渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。**
- 記録: `shots/habits-mv-s07.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` に、カードが求める `[名前: …]` の註を書かない。** 理由は下の節に書く——
**この1本に人は置かれない。****註を書けば、置かれる。**

- `SCENE`: the third of the chorus — a hand pinches one slip of paper and lifts it clear, and turns its face toward the camera; the face of the paper is given to the audience and what is on it is not read
- `CHARACTERS`: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**, at this work's one thin even weight; **no head, no shoulder, no face, and no standing figure at the sleeve** — **no name is given to the model, because a name brings a person**
- `SUBJECT`: one sheet of paper held up between the thumb and the first finger of one right hand, and the hand at its upper edge
- `ACTION`: pinching one sheet between the thumb and the first finger and turning its face toward the camera — the sheet hanging from the pinch and bending under its own weight, one swing and then still, its lower edge still moving after the hand has stopped; **not read**
- `LOCATION`: a left sleeve and the school nameplate fixed to it, in the middle of a working day, 2026 — the sleeve hangs behind the sheet at the left and the plate on it is background only; **nothing else is in this frame**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling across the sheet and the cloth, bloom on the pale surfaces, the sheet the brightest thing in the frame because the light is behind it, and everything the sleeve shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the warm white of one sheet of paper held against the tube — translucent at its middle and dark at its edges, and the only thing in the frame the light passes through

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the third of the chorus of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of one sheet of paper held up between the thumb and the first finger of one right hand, and the hand that lifted it, at a left sleeve carrying a school nameplate, in the middle of a working day, with the warm white of the backlit sheet as the only thing in the frame the light passes through. One sheet is held at one pinch and hangs from it, bending under its own weight — one swing and then still, its lower edge still moving for a moment after the hand has stopped. Its face is toward the camera and what is written on it cannot be made out: the characters are present on screen and not readable, the marks of cut print and of ballpoint and of pencil drawn as the three different marks they are and none of them legible, and the paper's fibre showing where the light comes through it. The hand is a right hand and it is the only figure in the frame — one hand at the sheet's upper edge, thumb and first finger, the knuckles, no further, and the arm not in frame beyond the cuff. No head enters the frame, no shoulder, no face, and no standing figure behind the sleeve; the plate on the sleeve is the school's designated nameplate, plastic, its characters present and not readable. The sleeve hangs behind the sheet at the left and nothing else is in this frame: no second sheet, no bundle, no desk, no mug, no pen cup. The light is a fluorescent tube above and behind the camera, falling flat across the sheet and the cloth and blooming on the pale surfaces; the sheet is the brightest thing in the frame because the light is behind it, so it goes translucent at its middle and dark at its edges, and everything the sleeve shadows has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette is narrow and cold — the warm white of paper held against a tube, the grey of its shadowed edge, the cyan of the room — and skin is the only warm thing in it besides the sheet. Layered atmospheric depth from near to far; dust suspended and individually rendered in the air around the sheet where the tube catches it, and the sheet's lower edge is the only thing in the frame that is still moving. Very low visual density: one focal point, the hanging sheet and the hand that holds it, with the sleeve and the room's cyan filling the rest. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at the height of the sheet and not approaching it, the sheet hanging at the frame's centre with the sleeve behind it at the left. One scene, one staging; the same sleeve, the same tube and the same sheet wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no legible text on any surface, no legible name text, no readable characters on any prop, no legible characters on the nameplate, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no face in the frame, no head, no shoulder, no standing figure at the sleeve, no second figure, no second sheet, no bundle, no reading, no eye in the frame, no finger tracking the writing, no insert of the writing, no magnified detail of the characters, no rack focus onto the sheet, no push-in, no zoom, no sheet laid down, no sheet handed to anyone, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered rather than a flat gradient」「Volumetric god rays — visible shafts of light
  travelling through air」「Anamorphic lens flare and bloom around the light source」
  「**A saturated dusk palette: magenta and gold against deep cyan shadow**」。
  そして `Visual breakdown` は**「wide and sky-heavy, a low horizon, the light source inside the frame or
  just outside its edge; the figure small against the world」**
  と言い、まとめは「**the light, not the character, is the subject**」である。
- ⛔ **この画面に、空は無い。** この1本は**手と紙しか映さない**（動画の仕様 §3）——
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s07` §2 `Visual Language`——
  「**Luminous realist anime, translated into a piece of paper held up between two fingers.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**つまんだ一枚が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その「光」が紙の裏側に在る**（`s07` §2——「**and here the light is behind
  the paper, so the sheet goes translucent at its middle and dark at its edges**」）。
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s07` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render**」と、同じ一覧の末尾の「**no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚が写すのは、人の手である。** ゆえに `no photographic faces` だけでなく、
  **`no grain`・`no painterly brush strokes`・`no soft airbrush` もこの1枚で効く**——
  **凍結した一枚はアニメの絵であり、実写ではない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、つまんだ一枚が実写になる。**

## ⚠️ 様式カードの `[名前: 性別、髪、体格、衣服]` の註を、この1枚では書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う——
  **隣の作品はそれを書き、その註を `Prompt` の中にも置いている。**
- ⛔ **この1本に、置かれる人は居ない。** 動画の仕様 §3 の `nobody` は
  「**この1本は、この作品で最も厳密に「誰も居ない」1本である。** **手と紙以外は、何も置かない。**」
  と言い、§6 は「**顔は置かない。**」と言い、§16 `MUST NOT` は
  「**The face does not enter the frame.**」と言う。
  ⚠️ **この作品の順序は「手が先にあり、顔が後に来る」である**（`bible.constants.顔`）——
  **この1本は、その順序の1歩目である。**
- ⚠️ **註は「置かれるべき人」を教えるための道具である。** **置いてはならない1本で書けば、
  それは置くための指示になる。** ゆえに `CHARACTERS` は**手の記述だけを持つ**——
  **名前を1つも書かない。**
  ⚠️ **手の外見も書き起こさない。** この1本の人物の外見の記述は出典に一行も無く
  （方針 §5a——`ledger.yaml` の `characters` の註）、**凍結した一枚が外見である**。
  ゆえに `CHARACTERS` は**その一枚を指す**——**名指しも、書き起こしもしない。**
- ⚠️ **これは `scene-board` の `do` からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s07` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**空白の面**と**偽の字**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が表の側に在る。** `s07` §20 の1番目——
  「**The sheet may be rendered legible.** ⚠️ **The first risk of this shot and the worst one**:
  the paper is turned toward the camera on purpose, and a generator asked for a sheet facing the
  camera will write on it.」「**A readable sheet here ends the work's premise at its most literal
  moment.**」そして2番目——「**The camera may move in.** ⚠️ **The turn toward the camera is an
  invitation a generator will accept** — **and the shot's meaning is that the invitation is
  refused.**」**ゆえに `Negative` に `no insert of the writing, no magnified detail of the
  characters, no rack focus onto the sheet, no push-in, no zoom` を置く。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この作品は、基盤の床をそのまま負う。**（`specmap.BASE_NEGATIVES`）
  **床は3節**」であり、**`L21` が、その床を動画の §18 と画像の `Negative` の両方に要求する**）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s07.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「手が札を一枚つまみ上げ、**面をこちらへ向けている。**」
- `reference_set` は**この1本では4点**である——`高橋由美.identity`・`高橋由美.negatives`・
  `名札`・`名札.appearance`。⚠️ **`s01` と違い、この1本は `identity` を含む**——
  動画の仕様 §6——「**この1本は `identity` を添付する** — 手の造形がこの人物のものであるためである。」
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した人のかたちの一枚を渡す）。
  ⛔ **それでも `CHARACTERS` に名前を書かない**——**置かれる人が居ないからである**（上の節）。
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
