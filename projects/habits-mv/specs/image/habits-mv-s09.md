# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第九のショット「四枚が、指の下で一度ずれる」（所作 / motion / 9.495s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、`verse-2` の1本目である**（動画の仕様 §19——`Segment ID: verse-2-1`。
`verse-2` は `s09` と `s10` の2本である）。
⚠️ **この1本は、2行を1本で受ける**——`l08`「**箱の側面に、四枚。**」＋
`l09`「**剥がさないまま、重なっている。**」（`bible.song.lines`）。
⚠️ **この1本の変化は、数えることである**——`aim` は
「**物を数えさせる1本。** 「四枚」を、画面の中で**数えられる形**にできるか。」と言い、
動画の仕様の前書きは「**数えるのは観客であって、手ではない。**」と添える。
`unit.after` は「四枚の端が、**指の下で一度ずれる。**」——**それだけである。**
⛔ **剥がさない。** 世界の規則「**運搬は一度も完了しない**」——**四枚が剥がれれば、運搬が一歩進む。**
⚠️ **顔は置かれない。** 動画の仕様 §3 は「⚠️ **この1本に顔は置かない** — 顔は `s10` で、
**呼ばれた後に**置かれる。」と書き、§16 `MUST NOT` は「**The face does not enter the frame** —
the face belongs to `s10`.」を持つ。
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——**四枚は、剥がされていない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s09.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into the side of a cardboard box and the slips gummed to it.**
    **The light, not the figure, is the subject** — and here it rakes across the stack so that
    **each slip has its own edge shadow and the count can be read without a line being read.**」
    ——**動画の側が先に、この様式を「箱の側面へ翻訳した」と書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s09.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/ChatGPT Image 2026年9月20日 03_29_35.png`
  と `.../ChatGPT Image 2026年9月20日 03_49_14.png`（**凍結した二枚**。`ledger.yaml` の `暮林蒼.identity` が
  指す先であり、動画の仕様 §6 も同じ先を指す）＋ 同じ作品の既存の生成物（`media/` の動画）
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s09` §6——「**この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が、ずれたあとの四枚を写すのは、そのためである**——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  **押さえる所作そのものは、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。**
- 記録: `shots/habits-mv-s09.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` に、カードが求める `[名前: …]` の註を書かない。** 理由は下の節に書く——
**この1本は手を置くが、人は置かれない。****註を書けば、置かれる。**

- `SCENE`: the first of the second verse — four slips stacked on the side of a box are pressed one by one from the top down, and the stack shifts once by a millimetre; nothing is peeled and nothing is taken
- `CHARACTERS`: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**; **no head, no shoulder, no face** — **no name is given to the model, because a name brings a person**
- `SUBJECT`: four address slips stacked and gummed to the side of a cardboard box, and one right hand at rest on them
- `ACTION`: having pressed the four one by one from the top down — each press short and finished, the next beginning without a pause — and then stopped; the stack has shifted once, by a millimetre, and is still; **the fingers do not close on anything, and nothing is peeled, lifted or taken**
- `LOCATION`: the side of a cardboard box of address slips on a desk, in the middle of a working day, 2026 — the box's side square to the frame with a crushed corner, and the four edges at the frame's centre; **the inside of the box is never shown**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera, raking across the stack so that **each slip casts its own edge shadow**, bloom on the lifted edges, the paper the brightest thing in the frame, and everything the box shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the four slightly different creams of the slips — four edges, four tones, and the only thing that makes the count readable without a word being read

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the first of the second verse of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of four address slips stacked and gummed to the side of a cardboard box on a desk, in the middle of a working day, with the four slightly different creams of the slips as the only thing that makes the count readable without a word being read. The box's side is square to the frame and stays square, its corner crushed, and the stack sits at the frame's centre; the edges are lifted and dust has settled into the lift, so that each slip casts its own edge shadow and the four are countable at the same time. One right hand has come to rest on them: the four were pressed one by one from the top down, each press short, flat and finished with the next beginning without a pause, and the hand has stopped; the fingers are not closed on anything and the wrist has not turned. The characters on the slips are present on screen and not readable — the marks of cut print and of ballpoint and of pencil drawn as the three different marks they are, none of them legible — and nothing has been peeled, lifted or taken: the stack has shifted once, by a millimetre, and it moved together rather than coming apart. No head enters the frame, no shoulder, no face, and no second figure; the only other thing in the frame is the board of the box, and its inside is never shown. Nothing else is on the desk. The light is one fluorescent tube above and behind the camera, raking across the stack so that each slip throws its own edge shadow — bloom on the lifted edges, the paper the brightest thing in the frame, everything the box shadows gone to deep cyan — and the dust along the four edges still moves after the hand has stopped. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one material and no gradient inside a single material. The palette is paper and board: four slightly different creams and the tan of the box. Layered atmospheric depth from near to far, dust suspended and individually rendered along the four edges, and low visual density — one focal point, the stack's four edges, with the box's side filling the rest of the frame. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at the height of the stack, square to the box's side, holding the whole stack so that the count stays in the frame. One scene, one staging; the same box, the same tube and the same stack wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no legible text on any surface, no legible name text, no readable characters on any prop, no legible characters on the slips, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no peel, no peeling, no slip lifted, no slip taken, no slip handed to anyone, no stack of three, no stack of five, no count other than four, no fifth slip, no second hand, no face in the frame, no head, no shoulder, no standing figure, no reading, no eye in the frame, no finger tracking the writing, no insert of the writing, no magnified detail of the characters, no rack focus onto a slip, no tilt down the stack, no push-in on the fourth slip, no open box, no box lid, no inside of the box, no second object on the desk, no mug, no pen cup, no terminal, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered rather than a flat gradient」「Volumetric god rays — visible shafts of light
  travelling through air」「Anamorphic lens flare and bloom around the light source」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon, the light source inside the frame or
  just outside its edge; the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**箱の側面と、その上の四枚しか映さない**——
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s09` §2 `Visual Language`——
  「**Luminous realist anime, translated into the side of a cardboard box and the slips gummed to it.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**四枚の札が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その「光」が四枚の端を数えさせている**（`s09` §2——「**here it rakes across
  the stack so that each slip has its own edge shadow**」）。**光は、数を読ませる道具である。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ 四枚は、四枚のまま写す——数が変われば、この1枚は意味を失う

- ⚠️ **この1本の主題は数である。** `aim` の「**「四枚」を、画面の中で数えられる形にできるか**」が
  それであり、動画の仕様 §16 `MUST` は
  「**All four are countable in the frame at the same time.**」と定める。
- ⛔ **この1枚では、数が明かす側である。** 動画の仕様 §7 `Pull`——
  「**Nothing has been taken, and the audience has counted to four.**」
  ⚠️ **隣の `s10` が「いちばん古い一枚が、いちばん下にある。」を明かすのに対し、
  この1本は枚数だけを明かす**（`ledger.disclosure`——`s10` が変化点であり、この1本は変化点ではない）。
- ⚠️ **ゆえに `Negative` に `no stack of three, no stack of five, no count other than four, no fifth slip`
  を置く。** 動画の仕様 §20 の1番目——
  「**The slips may come out as three or five.** ⚠️ **The first risk of this shot**: the count is the
  shot's subject and a generator will happily make a stack of any size. **A count that is wrong makes
  the shot meaningless.**」**この段落は、その事故を塞ぐ唯一の段である。**
- ⚠️ **そして、四枚は並列である。** 端が浮き、埃が入り、**それぞれが自分の影を持つ**——
  **「四枚がある」ではなく「四枚が数えられる」が、この1枚の側の仕事である。**
  ⚠️ **中は映さない**（動画の仕様 §4——「⚠️ **箱の中は映さない。** **中身が映れば、
  この1本は「数える」ではなく「確かめる」になる。**」）。

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s09` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render**」と、同じ一覧の末尾の「**no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚が写すのは、人の手と、古い紙である。** ゆえに `no photographic faces` だけでなく、
  **`no grain`・`no painterly brush strokes`・`no glossy plastic page`・`no plastic-looking paper`
  もこの1枚で効く**——**四枚の札は古い紙であり、艶のある面ではない。**
  ⚠️ **動画の仕様 §11 は「**Four old slips are lighter than one new page**」と言い、
  「**this is the lightest paper in it**」と添える**——**軽さは、実写の質感では出ない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、四枚の札が実写になる。**

## ⚠️ 様式カードの `[名前: 性別、髪、体格、衣服]` の註を、この1枚では書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う——
  **隣の作品はそれを書き、その註を `Prompt` の中にも置いている。**
- ⛔ **この1本に、置かれる人は居ない。** 動画の仕様 §3 は
  「⚠️ **この1本に顔は置かない** — 顔は `s10` で、**呼ばれた後に**置かれる。」と言い、
  §16 `MUST NOT` は「**The face does not enter the frame** — the face belongs to `s10`.」を持つ。
  ⚠️ **この作品の順序は「手が先にあり、顔が後に来る」である**（`bible.constants.顔`）——
  **この1本は、その順序の1歩目であり、顔は次の1本である。**
- ⚠️ **註は「置かれるべき人」を教えるための道具である。** **置いてはならない1本で書けば、
  それは置くための指示になる。** ゆえに `CHARACTERS` は**手の記述だけを持つ**——
  **名前を1つも書かない。**
  ⚠️ **手の外見も書き起こさない。** この1本の人物の外見の記述は出典に一行も無く
  （方針 §5a——`ledger.yaml` の `characters` の註）、**凍結した二枚が外見である**。
  ゆえに `CHARACTERS` は**その二枚を指す**——**名指しも、書き起こしもしない。**
  ⚠️ **この手は `s10` で同じ人物の顔と対になる**（動画の仕様 §3 `Continuity Requirements`——
  「⚠️ **この手は `s10` で同じ人物の顔と対になる。**」）——**この1枚の外れは、1枚で終わらない。**
- ⚠️ **これは `scene-board` の `do` からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s09` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**数**と**剥がすこと**と**読ませること**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が「数」にある。** `s09` §20 の2番目と3番目——
  「**A slip may be peeled** — the hands of a generator reach for labels in order to move them.」
  「**The writing may be rendered legible**, turning the count into a reading.」
  **ゆえに `Negative` に `no peel, no peeling, no slip lifted, no slip taken, no slip handed to anyone`
  と、`no reading, no insert of the writing, no magnified detail of the characters, no rack focus onto
  a slip` を置く。** ⚠️ **剥がれれば運搬が完了する**——**この1本は、それを止める段でもある。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——**床は3節**であり、**この作品は `no calling voice as a sound effect` と
  `no face before the name is called` を足して5行にする**）。**ゆえにこの段落は、動画の §18 の写しではない**
  ——**同じ床を、効く場所へ置いたものである。**

- ⛔ **そして、この段落は共有の尾から1節を落としている**——`no stack of paper` である。
  ⛔ **この1本の主題は、紙が重なった山そのものである。**
  **尾は27本で共有されているが、その1節だけは、重なりを主題に持つ1本では主題を禁じてしまう。**
  ⚠️ **尾の目的は「机の上に二つ目の物を置かない」であって、「紙を描かない」ではない**——
  **この1本では、前者は `no second object on the desk, no mug, no pen cup, no terminal` が負う。**
  **ゆえに落としたのは1節であり、他の36節は一字も動かしていない。**
  ⚠️ **同じ衝突は、この作品に5本ある**——`s10`・`s11`・`s21`・`s24`・`s25`。

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s09.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「四枚の端が、**指の下で一度ずれる。**」
- `reference_set` は**この1本では6点**である——`暮林蒼.identity`・`暮林蒼.negatives`・`宛名票`・
  `宛名票.negative`・`宛名票の一行`・`宛名票の一行.geography`。
  ⚠️ **`s07` と違い、この1本は `identity` を含む**——動画の仕様 §6——
  「**この1本は `identity` を添付する** — 手の造形がこの人物のものであるためである。⚠️ **顔は置かない。**」
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した二枚を渡す）。
  ⛔ **それでも `CHARACTERS` に名前を書かない**——**置かれる人が居ないからである**（上の節）。
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
