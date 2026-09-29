# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第八のショット「二つの手が、同じ姿勢で止まる」（モンタージュ / motion / 8.218s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、`chorus-1` の4本目である**（動画の仕様 §19——`Segment ID: chorus-1-4`。
`chorus-1` は `s05`・`s06`・`s07` と、この1本である）。
⚠️ **この1本の変化は「同じ姿勢が二度」である**——`unit.after` は
「二つの手が、**同じ姿勢で止まっている。**」。⚠️ **そして二つの場所は、繋がらない**——
`motion.law` は「**二つの場所は、繋がらない**——カメラは跨がず、**同じ位置で二度目を迎える**」と定める。
⛔ **ゆえにこの1枚の主題は、静止の側にある。** 動画の仕様 §16 は
「**No cut, no dissolve, no wipe between the two places.** ⚠️ **The second press arrives inside the
same shot** — **this is the shot's entire design.**」と書く。
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——**二つの手が、同じ形で止まっている。**
⛔ **顔は置かれない。** 動画の仕様 §3 は片山大翔の右手について「**顔は置かない。**」と書き、
§16 `MUST NOT` は「**No third hand and no third place.**」を持つ。
⚠️ **この現場は、サビの14本が共有する現場である**（`ledger.yaml` の `名札` の註——
「**サビの14本は、すべてこの現場である。** ——**「読む手は、誰の手。」の現場である。**」）。
⚠️ **二人は別の場所にいる。それでも画面は一つである**（`ledger` の `locations` の註——
27本は6つを巡る）。**ゆえに `place` は単数である**（`名札`）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/seedance-2.5/habits-mv-s08.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a hand pressed on paper — twice, in one frame, in the
    same composition.** **The light, not the figure, is the subject** — and here the light is the same
    light in both places, which is the only thing that says they belong to one work.」——**動画の側が先に、この様式を「紙の上の手へ翻訳した」と
    書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s08.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/04_片山大翔/ChatGPT Image 2026年9月18日 05_08_30.png`
  と `distill-essence-engine/examples/habits/character/サブ/23_石川久美子/ChatGPT Image 2026年9月18日 05_11_14.png`
  （**凍結した人のかたちの一枚ずつ**。`ledger.yaml` の `片山大翔.identity` と `石川久美子.identity` が
  指す先であり、動画の仕様 §6 も同じ先を指す）＋ 同じ作品の既存の生成物（`media/` の動画）
- 添付する参照: **`specs/image/生成時参照イラスト/s08/` の2枚**——`片山大翔_設定画.png`・`石川久美子_設定画.png`。
  ⚠️ **この2枚は、この作品の動画の側の同じ2枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s08/`。実測 2026-09-28、ハッシュが一致した）。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s08` §6——「**この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が「同じ姿勢で止まった二つの手」を写すのは、そのためである**
  ——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  **二度目の押さえが来ることは、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。**
- 記録: `shots/habits-mv-s08.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` に、カードが求める `[名前: …]` の註を書かない。** 理由は下の節に書く——
**この1本は二本の手を置くが、そのどちらの場所にも人は置かれない。****註を書けば、置かれる。**

- `SCENE`: the fourth of the chorus — two hands in two places come to rest in the same posture inside one frame, and the frame does not cut
- `CHARACTERS`: **two right hands, in two places, and no one in either place** — **each hand its own frozen setting sheet's**, at this work's one thin even weight; **no head, no shoulder, no face, and no standing figure at either sleeve** — **no name is given to the model, because a name brings a person**
- `SUBJECT`: two right hands pressing paper down at two left sleeves, in the same posture, in one composition
- `ACTION`: pressing paper down — one fast flat press, then a finger slipping on the sheet without leaving it so the press does not become a stroke, then the same press again in another place, and then both hands at rest in the same shape; **nothing is turned, lifted or carried**
- `LOCATION`: two left sleeves carrying the school nameplate, in the middle of a working day, 2026, held in one frame — **the same composition twice**, the plate and the paper under each hand the only things in it; **no desk, no window, no clock, and nothing that would tell the two places apart**
- `LIGHT`: the room's constant state, and the same light in both places — the flat light of a fluorescent tube above and behind the camera falling across the paper and the cloth, bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the sleeves shadow gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the cream of the paper under each hand — the same cream twice, and the only warm thing in the frame besides skin

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the fourth of the chorus of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of two right hands pressing paper down at two left sleeves carrying the school's nameplate, in the middle of a working day, with the cream of the paper under each hand as the only warm thing in the frame besides skin. One composition holds both places and it does not cut: the second press lands where the first one landed, in the same shape, and the same frame geometry carries both. The first hand presses the paper flat in one fast even movement, and the first finger slips on the sheet without leaving it, so that the press does not become a stroke; then a second hand, in another place, makes the same press, and both stop in the same posture and stay. Under each hand a sheet of paper takes the press and does not move; its grain shows where the pads rest, and the characters on it are present on screen and not readable, drawn as the three different marks of cut print and of ballpoint and of pencil, none of them legible. Each hand is the only figure in its own place: two hands at two plates on two cloth sleeves, the pads meeting the paper and nothing else touching anything. No head enters the frame at either sleeve, no shoulder, no face, and there is no third hand and no third place; the plates on the sleeves are the school's designated nameplate, plastic, a dark border, their characters present and not readable, and they are background only. Nothing in the frame tells the two places apart: there is no desk, no window, no clock, no difference of weather, and no prop that belongs to one room and not the other, so that the only difference between the two halves is how much deep cyan the shadows hold. The light is one fluorescent tube above and behind the camera, falling flat and even across both places — bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the sleeves shadow gone to deep cyan — and in the long second half only the dust over the two sleeves and the light crossing the paper are still moving. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette is the same palette twice: paper cream, skin, cloth, and the dark of a pressed shadow. Layered atmospheric depth from near to far, dust suspended and individually rendered where the tube catches it, and very low visual density — one focal point, the pressed hand, twice. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens close at the sleeve and unmoving, the sleeve and the plate at the frame's centre in both halves, the same placement for both presses. One scene, one staging; the same sleeve, the same tube and the same press wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no cut, no dissolve, no wipe, no transition between the two places, no second camera angle, no reframe between the two presses, no pan, no tilt, no push-in, no pull-back, no legible text on any surface, no legible name text, no readable characters on any prop, no legible characters on the nameplate, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no face in the frame, no head, no shoulder, no standing figure at either sleeve, no third hand, no third place, no second figure, no desk, no window, no clock, no distinguishing prop between the two places, no lifting of the paper, no turning of the sheet, no peeling, no reading, no eye in the frame, no sheet handed to anyone, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered rather than a flat gradient」「Volumetric god rays — visible shafts of light
  travelling through air」「Anamorphic lens flare and bloom around the light source」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon, the light source inside the frame or
  just outside its edge; the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**二つの袖と、その下の紙しか映さない**——
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s08` §2 `Visual Language`——
  「**Luminous realist anime, translated into a hand pressed on paper.**」**この1枚は、その訳文の側に立つ。**
  訳す前の側（空）を写せば、**押さえた手が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ 二つの場所を、光で区別してはならない

- ⚠️ **この1本は二つの場所を1枚に置く。** 動画の仕様 §16 `MUST NOT` は
  「**The two places are not distinguished by light, weather, prop or time of day.**」と定め、
  §13 `Lighting Events` は「**None, in either place.** ⚠️ **The two places share the light exactly** —
  a difference of light would make them two shots and lose the shot.」と書く。
- ⛔ **ゆえにこの1枚は、二度目の側にだけ窓を置かない。** **机も、窓も、時計も無い**（動画の仕様 §5——
  「⚠️ **二つの場所を区別する物を置かない** — **机も、窓も、時計も無い。** **区別する物を置けば、
  そこは二つの場所ではなくなる。**」）。**光も、埃の量も、同じである。**
  ⚠️ **この作品は、名札を机の上に置かない**（`ledger.yaml` の `名札` の `geography`）——
  **ゆえに「机の上の名札」は、この1枚でも起きない。**
- ⚠️ **差は、位置だけである**——`motion.law` の言葉では「**同じ位置で二度目を迎える**」。
  **この一枚が写す「同じ姿勢」は、その差の側である。**

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s08` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render**」と、同じ一覧の末尾の「**no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚が写すのは、人の手である。** ゆえに `no photographic faces` だけでなく、
  **`no grain`・`no painterly brush strokes`・`no soft airbrush` もこの1枚で効く**——
  **凍結した一枚はアニメの絵であり、実写ではない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、押さえた手が実写になる。**

## ⚠️ 様式カードの `[名前: 性別、髪、体格、衣服]` の註を、この1枚では書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う——
  **隣の作品はそれを書き、その註を `Prompt` の中にも置いている。**
- ⛔ **この1本のどちらの場所にも、置かれる人は居ない。** 動画の仕様 §3 の `nobody` は
  「**この1本に、二番目の人物は居ない。** ⚠️ **二本の手は、二人である**——**それでも、
  それぞれの場所に一人しか居ない。**」と言い、片山大翔の右手の節は「**顔は置かない。**」と言い、
  §16 `MUST NOT` は「**No third hand and no third place.**」を持つ。
  ⚠️ **この作品の順序は「手が先にあり、顔が後に来る」である**（`bible.constants.顔`）——
  **この1本は、その順序の1歩目である。**
- ⚠️ **註は「置かれるべき人」を教えるための道具である。** **置いてはならない1本で書けば、
  それは置くための指示になる。** ゆえに `CHARACTERS` は**二本の手の記述だけを持つ**——
  **名前を1つも書かない。**
  ⚠️ **手の外見も書き起こさない。** この1本の二人の外見の記述は出典に一行も無く
  （方針 §5a——`ledger.yaml` の `characters` の註）、**凍結した各一枚が外見である**。
  ゆえに `CHARACTERS` は**その二枚を指す**——**名指しも、書き起こしもしない。**
  ⚠️ **この仕様自身の §3 `Continuity Requirements` も同じことを言う**——
  「⚠️ **二人の手は、この作品の他の手と同じ様式で描かれる。**」
  **この1枚の外れは、1枚で終わらない。**
- ⚠️ **これは `scene-board` の `do` からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s08` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**切れ目**と**二つの場所の区別**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が編集の側に在る。** `s08` §20 の1番目——
  「**A cut may be inserted.** ⚠️ **The first risk of this shot and the one that costs the most**:
  a generator given two hands in two places will separate them, because that is what montage means
  everywhere else. **A cut here makes this two ordinary shots and wastes the longest chorus line.**」
  そして2番目——「**The two places may be distinguished** by different light, a window, a clock, or a
  change of weather — which is the same failure by another route.」**ゆえに `Negative` に
  `no cut, no dissolve, no wipe, no transition between the two places, no second camera angle,
  no reframe between the two presses` と、`no desk, no window, no clock, no distinguishing prop
  between the two places` を置く。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——**床は3節**であり、**この作品は `no calling voice as a sound effect` と
  `no face before the name is called` を足して5行にする**）。**ゆえにこの段落は、動画の §18 の写しではない**
  ——**同じ床を、効く場所へ置いたものである。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s08.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「二つの手が、**同じ姿勢で止まっている。**」
- `reference_set` は**この1本では6点**である——`片山大翔.identity`・`片山大翔.negatives`・
  `石川久美子.identity`・`石川久美子.negatives`・`名札`・`名札.appearance`。
  ⚠️ **`s01` と違い、この1本は `identity` を2点とも含む**——動画の仕様 §6——
  「**この1本は `identity` を添付する。**」⚠️ **画像の側の `content` も同じ側に立つ**
  （凍結した一枚ずつを渡す）。⚠️ **それでも註は書かない**——
  **人が置かれるからではなく、手の造形がその二人のものであるためである。**
  ⛔ **それでも `CHARACTERS` に名前を書かない**——**置かれる人が居ないからである**（上の節）。
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
