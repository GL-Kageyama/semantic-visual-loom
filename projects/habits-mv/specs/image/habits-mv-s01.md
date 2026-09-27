# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第一のショット「閉じた出席簿が、開かれる」（所作 / motion / 8.059s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⛔ **この紙は、この作品で最初の画像仕様である。** `projects/habits-mv/specs/image/` は
**これまで空だった。** 実測（2026-09-28）——**27本のどれも `key_image` を持たず、
`specs/image/` には1枚も無い。** ゆえに `L18` の「`key_image` が読めない」は
**27本ぶん在り、この1本で1つ減る。**
⚠️ **記録が無いのであって、食い違っているのではない**（`ledger.yaml` の `註 L18`）——
**だから違反ではない。****だが、この27本の画像の側は一度も検査されていない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s01.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a desk in a school staff room at the end of the day**」
    ——**動画の側が先に、この様式を「机へ翻訳した」と書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s01.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/prompt.md`
  （凍結した設定画の読み）と、同じ作品の既存の生成物（`media/` の3本の動画）
- 添付する参照: **無い。** ⛔ **`specs/image/生成時参照イラスト/` に `s01` のフォルダは無い**
  ——**この1本の `reference_set` は `碓氷千夏.negatives` だけを挙げ、`identity` を挙げないからである。**
  ⚠️ **不在は、置き忘れではない。** 動画の側も同じである（`specs/video/生成時参照イラスト/` にも `s01` は無い）。
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
  ⚠️ **この組では、`L22` は鳴らない**（実測 2026-09-28）——`scene-board` の5穴と
  `luminous-anime` の4穴の**和が、そのまま下の7欄である**（`specmap.MODELS` の註と同じ7欄。
  `check.py --self-test` の `L22_FIVE`／`L22_FOUR` がこの2枚を例に持っている）。
  ⚠️ **隣の作品（`migenzo`）は2件鳴る**——あちらは `documentary-photo` を選び、
  **様式の側の穴が違う**（`SUBJECT`/`ACTION`/`SCENE`/`LIGHT`/`ASPECT`）。**赤の有無は、作品の違いである。**
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** 様式カードの雛形は
  `Not photorealistic, …` で終わるが、**この作品はそれを2段落目に置く**——**この作品は実写ではない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s01` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が「開いた頁」を写すのは、そのためである**——
  **渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。** 隣の作品が題を書いているのは、あちらの前提が違うからである。
- 記録: `shots/habits-mv-s01.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` に、カードが求める `[名前: …]` の註を書かない。** 理由は下の節に書く——
**この1本に人は置かれない。****註を書けば、置かれる。**

- `SCENE`: the first opening — a closed attendance register on a desk is opened by one hand and the page carrying the transfer column comes up; the column is on screen and is not read
- `CHARACTERS`: **one right hand, and no one in place** — a right hand, the back of it, the knuckles, the nails cut short, a small thickening on the first joint of the right middle finger where a pen rests, the plain cuff of a white shirt at the wrist; **no head, no shoulder, no standing figure behind the desk** — **no name is given to the model, because a name brings a person**
- `SUBJECT`: the opened attendance register standing up on its own page, and the one right hand that opened it
- `ACTION`: opening the register — the cover lifted and the leaves fanned and fallen one after another with the fore-edge still rocking; the pads of the fingers coming down on the cover near its outer edge **and pressing**, the page standing on its own edge under them and not yet settled; **not reading it**
- `LOCATION`: a desk in a school staff room at the end of a working day, 2026 — the desk's worn wooden face, a drawer closed, the back of a chair; **nothing else on the desk**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling across the cover and the page, bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the cream of the page edge and the one hand — the only warm things the tube finds in a narrow, cold room

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the first opening of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of an opened attendance register standing up on its own page on a desk, and the one right hand that opened it, in a desk in a school staff room at the end of a working day, with the cream of the page edge and the one hand as the only warm things the light finds. The register lies square to the desk's edge, cloth over board, the thickness of a register's left sleeve, a bound spine, its fore-edge layered cream and not smooth; the cover is lifted and the leaves have fanned and fallen one after another with the fore-edge still rocking, and the page stands up on its own edge and does not turn, not yet settled — and on the page the transfer column is on screen: characters written in ink by more than one hand, present and not readable, the marks of cut print and of ballpoint and of pencil drawn as the three different marks they are and none of them legible. The hand is a right hand and a hand only — the back of it, the knuckles, the nails cut short, a small thickening on the first joint of the right middle finger where a pen rests, the plain cuff of a white shirt at the wrist — the pads of the fingers come down on the cover near its outer edge and press it, holding the page up. No head enters the frame, no shoulder, no standing figure behind the desk, and there is nothing else on the desk: no mug, no pen cup, no terminal, no stack of paper. The desk is wood with the polish of forearms on it, and its worn edge is in the near foreground. The writing is not read: no eye is in the frame, no head bends over the page, and no finger tracks a line down it. The room's light is a fluorescent tube above and behind the camera, falling flat across the cover and the page and blooming on the pale surfaces; the paper is the brightest thing in the frame, the tube is the only light, and everything the desk edge shadows has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette is narrow and cold — fluorescent white, the grey-green of the cover with its cloth weave, the cream of the page edge — and the warm side is reduced to one hand and to the paper itself. Layered atmospheric depth from near to far; dust suspended and individually rendered in the air above the desk where the tube catches it, and it is the only thing in the frame that is still moving. Low visual density: one focal point, the cover and the standing page and the hand that arrived on it, with generous negative space and most of the frame given to the desk. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at desk height, looking slightly down, the register square in the frame with its closed edge toward the camera, and the standing page as the frame's only diagonal. One scene, one staging; the same desk, the same tube and the same hand wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no head, no shoulder, no standing figure, no person behind the desk, no second figure, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no second turn of the page, no reading, no eye in the frame, no head bent over the page, no finger tracking a line, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」。
  そして `Visual breakdown` は**「wide and sky-heavy, a low horizon … the figure small against the world」**
  と言い、まとめは「**the light, not the character, is the subject**」である。
- ⛔ **この部屋に、空は無い。** **この作品の光は、天井の蛍光灯1本である**
  （`s01` §13——「Fluorescent over a working desk at the end of the working day」。
  「**outside there is nothing left to see**」）。
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
- ⚠️ **この作品は、既にその翻訳を自分で書いている。** `s01` §2 `Visual Language`——
  「**Luminous realist anime, translated into a desk in a school staff room at the end of the day.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**机の上の1本が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。** ⚠️ **隣の作品が同じ手を使っている**
  （`migenzo` の `no window, no time of day, no directional light`——同じ理由である）。

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- ⛔ **隣の作品（`migenzo`）と、答えが逆である。** あちらは
  「**`Not photorealistic` を、ここに写してはならない**」という節を持ち、
  **様式カードの否定を落として `no smooth CGI` だけを残した**（裁定 2026-09-23、著者）
  ——**あちらの作品は実写である。**
- ⚠️ **この作品は、実写ではない。** `s01` §2 は「**Clean anime lineart**」と言い、
  §16 の `MUST NOT` は「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  そして `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **ゆえに、この1枚は様式カードの否定をそのまま負う。**
  ⛔ **隣の作品の節を、この作品へ写してはならない**——**写せば、机の上の1枚が実写になる。**

## ⚠️ 様式カードの `[名前: 性別、髪、体格、衣服]` の註を、この1枚では書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う——
  **隣の作品はそれを書き、その註を `Prompt` の中にも置いている。**
- ⛔ **この1本に、置かれる人は居ない。** `s01` §1——「**no face is in this shot at all**」。
  §16 `MUST NOT`——「**The face does not come into this shot. No head, no shoulder, no
  standing figure behind the desk.**」
  ⚠️ **この作品の順序は「手が先にあり、顔が後に来る」である**（`bible.world.rules`）——
  **この1本は、その順序の1歩目である。**
- ⚠️ **註は「置かれるべき人」を教えるための道具である。** **置いてはならない1本で書けば、
  それは置くための指示になる。** ゆえに `CHARACTERS` は**手の記述だけを持つ**——
  **名前を1つも書かない。**
- ⚠️ **これは `scene-board` の `do` からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**
- ⛔ **訂正（2026-09-28）——この `CHARACTERS` は「`a girl's hand`」と書いてあった。**
  **「`a girl's`」を落とし、「`a right hand`」にした。** 気づいたのは `s26` の画像仕様である
  ——あちらが `s01` と自分の欄を並べて数え、**「`s01` は `a girl's hand` と書くが、この1枚は
  `a right hand` とだけ書く」**と記録していた。⚠️ **私が見落としていた。**
  **理由は `s02` と同じである**——⛔ **出典はこの人を `女33` と言う**
  （`distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/prompt.md` の「出典の語」）。
  **`girl` は10代を意味し、出典に無い。**
  ⛔ **そして、この一語は外へ出ていた。** `specs/video/habits-mv-s01.md` の `Observed Problems` と
  `takes/habits-mv-s01-video-1.yaml` が、戻ってきた手を
  **「10代の女子の手として読めない」と欠陥に数えていた**——**その前提は、この一語から来ている。**
  **前提が誤りなら、成人の手であることは欠陥ではない**（両文書とも、そう書き直した）。
  ⚠️ **残した記述は出典を持つ**——`爪の短い手`・`右手中指の第一関節の小さな膨らみ` は
  同じ `prompt.md` の「**ルック＝**」の行にある。**落としたのは、出典に無い一語だけである。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s01` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**空白の面**と**偽の字**——を禁じているのは、**この段落である。**
  ⛔ **そして実測（2026-09-28、動画3本）が、その差を出した**——
  **机の上の手書きが、日本語の字ではなく、ラテン文字の草書として戻った。**
  動画の §18 は `no real-world alphabet` を既に持っていた。**散文として読まれた。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。** 実測（2026-09-28）——**5節すべてを覆っている。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s01.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `碓氷千夏.negatives` を含む5点**であり、
  **`碓氷千夏.identity` を意図的に持たない**——**人のかたちの一枚を渡せば、生成器は顔を置く**
  （`s01` の前書きと §6）。⚠️ **この判断は画像の側でも同じである。**
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この稿の文字列は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
  ⚠️ **`specs/image/01_…png` は在るが、それはこの稿の文字列から出たものではない**（下の最後の項）。
  **「ファイルが在る」と「この稿が送られた」は別である**——**`take.file` の側が、まだ1つも無い。**
- ⛔ **この稿で、`ACTION` と `Prompt` の物理を直した。** 直す前は
  「`without pressing`」「`not pressing`」「`does not turn`」——**`0.1.0` の物理であった。**
  ⚠️ **`0.2.0` の動画の仕様は、それを名指しで反転させている**（`s01` §10 の `Inertia`——
  「**The paper overshoots and settles.**」——「**これは前の版の `No overshoot and no settle` を
  反転させる**」と、その節自身が書いている）。
  そして `shots/habits-mv-s01.yaml` の末尾のビートは
  「**転出欄の頁が持ち上がり、指に押さえられて沈む——沈みきるのが、切れ目のコマである。**」と言う。
- ⚠️ **この1枚が写すのは「終わったあとの状態」である**（上の `## 渡す先`）。
  **指が押していない絵は、この1本の終わりの状態ではない。** ゆえに直した。
  ⛔ **仕様は直したが、標本は直っていない。** `specs/image/01_…png` は
  **直す前の文の側から出た1枚である**——**それがこの1枚の元であるかは、著者が見て決めることである。**
