# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第二十二のショット「二つの手が止まり、呼ばれないままでいる」（モンタージュ / motion / 5.345s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、`final-chorus` の4本目である**（動画の仕様 §19——`Segment ID: final-chorus-4`）。
⚠️ **この1本の変化は「答えられない停止」である**——`unit.after` は
「二つの手が止まり、**呼ばれないままでいる。**」。`motion.quality` は
「速い所作を二度。**間に、短い停止を一つ。**」と言う。
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——**二つの手は止まり、どちらも呼ばれていない。**
⛔ **「間」は、この1枚には写らない。** 動画の仕様 §8——「**One dense movement, then two held ones** —
and **the middle held movement is empty.**」**空の間は時間の側にあり、1枚には残らない。**
⚠️ **それでもこの1本の主題は、その間である**（§12 `Emotional Events`——「**The event is the interval.**」）。
**ゆえにこの1枚は、間が空けたあとの形を写す。****間そのものは、動画の側が持つ。**
⛔ **顔は置かれない。** 動画の仕様 §16 `MUST NOT`——「**No face is placed.** ⚠️ **The shot's question is
whether it can be held without one, and a face here answers a call that never came.**」
§17 の優先順位1——「**No face** — ⚠️ **this is the shot's whole question.**」
⚠️ **カメラは二つの場所を跨がない。** §16 `MUST NOT`——「**No cut and no camera crossing between the
two places.**」⚠️ **ゆえに `place` は単数である**（`名札`）——**二人は別の場所にいるが、画面は一つである**
（`ledger.locations` の註）。
⚠️ **この現場は、サビの14本が共有する現場である**（`ledger.locations.名札`——
`s05`〜`s08`・`s12`〜`s16`・`s19`〜`s23`）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/seedance-2.5/habits-mv-s22.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into two hands at rest on two sheets.**」そして
    「here it is the same light in both places, **which is the only thing that says they belong to one
    work.**」——**動画の側が先に、この様式を「二枚の紙の上の二本の手へ翻訳した」と書いている。**
    画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s22.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/14_三宅隆/ChatGPT Image 2026年9月21日 01_00_44.png`
  と `distill-essence-engine/examples/habits/character/サブ/21_池田絵里/ChatGPT Image 2026年9月21日 01_13_25.png`
  （**凍結した人のかたちの一枚ずつ**。`ledger.yaml` の `三宅隆.identity` と `池田絵里.identity` が
  指す先であり、動画の仕様 §6 も同じ二つの先を指す）＋ 同じ作品の既存の生成物（`media/` の動画）
- 添付する参照: **`specs/image/生成時参照イラスト/s22/` の2枚**——`池田絵里_設定画.png`・`三宅隆_設定画.png`。
  ⚠️ **この2枚は、この作品の動画の側の同じ2枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s22/`。実測 2026-09-28、ハッシュが一致した）。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s22` §6——「**この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が「二本の手が止まったあとの二枚の紙」を写すのは、
  そのためである**——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  **押さえる所作も、空の間も、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。**
- 記録: `shots/habits-mv-s22.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の `[名前: …]` の註は、この1枚では「名前と、どの一枚を取るか」だけを持つ**——
理由は下の節に書く。**外見は、凍結した二枚が持つ。**

- `SCENE`: the fourth of the final chorus — two hands in two places stop on two sheets inside one frame, and neither hand is called, and the frame does not cut
- `CHARACTERS`: `[三宅隆: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` `[池田絵里: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **two right hands, in two places, and no one in either place**; **no face, no chin, no hair, no shoulder above either cuff, and no standing figure at either sleeve**, neither hand reads anything, and no arm is in the frame
- `SUBJECT`: two right hands at rest on two sheets of paper at two left sleeves, in the same posture, in one composition
- `ACTION`: having pressed — one fast flat press in the first place, and then the same press arriving in the second — and both hands now at rest in the same shape and staying there; **nothing is turned, lifted or carried, and neither hand is answering anything**
- `LOCATION`: two left sleeves carrying the school nameplate, at two desks in the middle of a working day, 2026, held in one frame — **the same composition twice**, the plate and the paper under each hand the only things in it; **no window, no clock, and nothing that would tell the two places apart**
- `LIGHT`: the room's constant state, and **the same light in both places** — the flat light of a fluorescent tube above and behind the camera falling across the paper and the cloth, bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the sleeves shadow gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the cream of the paper under each hand — **the same cream twice**, and the only warm thing in the frame besides skin

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the fourth of the final chorus of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of two right hands at rest on two sheets of paper at two left sleeves carrying the school's nameplate, in the middle of a working day, with the cream of the paper under each hand as the only warm thing in the frame besides skin and the light, not the figure, as the subject. One composition holds both places and it does not cut: the same frame geometry carries both, the second posture lands where the first one landed, and the same palette is used twice in the same values. Each hand has come down flat on its own sheet and has stopped: the sheet took the press and did not move, its grain shows where the pads rest, and neither hand is closed on anything. The characters on the two sheets are present on screen and not readable, drawn as the three different marks of cut print and of ballpoint and of pencil, and none of them legible. Each hand is the only figure in its own place — the pads, the back of the hand, the knuckles, no further, the arm not in the frame beyond the plain cuff. No head enters the frame at either sleeve, no shoulder, no face, and there is no third hand and no third place; nobody is watching either hand, and nobody in the frame is being answered. Nothing in the frame tells the two places apart: the same desk-height, the same cloth, the same plastic, the same paper — there is no window, no clock, no difference of weather, and no prop that belongs to one place and not the other, so that **the only difference between the two halves is how much deep cyan the shadows hold**. The light is one fluorescent tube above and behind the camera, falling flat and even across both places — bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the sleeves shadow gone to deep cyan — and the dust over the two sheets and the light crossing the paper are the only things still moving. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette is the same palette twice: paper cream, skin, cloth, and the dark of a pressed shadow. Layered atmospheric depth from near to far, dust suspended and individually rendered where the tube catches it, and very low visual density — one focal point, the resting hand, twice. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens close at the desk and unmoving, the paper at the frame's centre in both halves, the same placement for both hands. One scene, one staging; the same desk, the same tube and the same press wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no legible text on any surface, no legible name text, no readable characters on any prop, no legible characters on the nameplate, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no reading, no eye in the frame, no head bent over the paper, no finger tracking the writing, no insert of the writing, no magnified detail of the characters, no face in the frame, no head, no shoulder, no head at either sleeve, no face at either sleeve, no standing figure, no second figure, no third hand, no third place, no caller in the frame, no crowd, no group of people, no cut, no dissolve, no wipe, no transition between the two places, no second camera angle, no reframe between the two places, no pan, no tilt, no push-in, no pull-back, no camera crossing between the two places, no camera movement during the interval, no difference of light between the two places, no window, no clock, no difference of weather, no prop that belongs to one place and not the other, no distinguishing detail between the two halves, no third desk, no lifted paper, no turned sheet, no peel, no sheet taken, no sheet handed to anyone, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies」「Volumetric god rays」
  「Anamorphic lens flare」「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**二つの袖と、その下の紙しか映さない**——
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s22` §2 `Visual Language`——
  「**Luminous realist anime, translated into two hands at rest on two sheets.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**止まった二本の手が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その「光」が二つの場所を一つの作品に見せている唯一のものである**
  （`s22` §2——「**here it is the same light in both places, which is the only thing that says they
  belong to one work.**」）。**光は、二つを一つにする道具である。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ 二つの場所を、光で区別してはならない

- ⚠️ **この1本は二つの場所を1枚に置く。** 動画の仕様 §16 `MUST NOT` は
  「**No cut and no camera crossing between the two places.**」と定め、
  §13 `Lighting Events` は「**None, in either place.** ⚠️ **A change of light would fill the interval**,
  and **the interval is what the shot has instead of a call.**」と書く。
- ⛔ **ゆえにこの1枚は、二度目の側にだけ窓を置かない。****窓も、時計も無い**（動画の仕様 §4——
  「⚠️ **二つの場所を区別する物を置かない。**」）。**光も、埃の量も、同じである。**
  ⚠️ **この作品は、名札を机の上に置かない**（`ledger.locations.名札` の `geography`）——
  **ゆえに「机の上の名札」は、この1枚でも起きない。**
- ⚠️ **差は、位置だけである**——動画の仕様 §15 `Spatial`——「⚠️ **The two places occupy the same
  frame geometry** — the second posture lands where the first one did.」
  **この一枚が写す「同じ姿勢」は、その差の側である。**
- ⚠️ **この1本は、この作品で二度目の「二つの場所を1枚に置く」である**——`s08`（`chorus-1` の4本目）が
  一度目であり、**この1本は `final-chorus` の4本目である。**
  ⚠️ **差は、間に空の停止を挟むかどうかである**（`s22` の前書き——「**`s08` は二つの手が同じ姿勢へ収まり、
  `s16` は同時に止まった。** **この1本は、間に停止を持つ。**」）。
  ⛔ **ゆえにこの1枚は、`s08` の画像仕様の写しではない。**

## ⚠️ この1枚は「間」を写せない——写すのは、間が空けたあとの形である

- ⚠️ **この1本の中核は、時間の側に在る。** 動画の仕様 §8 `Temporal Density`——
  「**One dense movement, then two held ones — and the middle held movement is empty.**」
  §12 `Emotional Events`——「⚠️ **The event is the interval.**」
- ⛔ **1枚は時間を持たない。****この1枚は、空の間そのものを写すことができない。**
  ゆえにこの1枚が写すのは、**間のあとに残った形である**——**二本の手が、同じ姿勢で止まっている。**
- ⚠️ **それでも、この1枚は間を「指す」ことはできる。** 動画の仕様 §10——
  「⚠️ **The interval is empty and the camera does not fill it.**」
  **この1枚が空であること**——**二本の手のほかに何も無く、誰も呼んでいないこと**——が、
  **間が空だったことの、1枚の側の証拠である。**
  ⚠️ **ゆえに `Prompt` に「nobody is watching either hand, and nobody in the frame is being answered」
  を置き、`Negative` に `no caller in the frame, no crowd, no group of people` を置く。**
- ⚠️ **間の長さも、この1枚には無い。** 動画の仕様 §15 `Temporal`——この1本は
  「**the work's 5.345秒 contain one action and a stop**」である。
  ⛔ **1枚は秒を持たないので、`duration` をこの1枚の側に書かない**（`## 記録との対応` にのみ書く）。

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s22` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚が写すのは、人の手であり、二度写される。** ゆえに `no photographic faces` だけでなく、
  **`no grain`・`no painterly brush strokes`・`no soft airbrush` もこの1枚で効く**——
  **凍結した二枚はアニメの絵であり、実写ではない。** ⚠️ **そして二度写すということは、
  同じ手が二つの描き方で現れうるということである**——**`no second shadow tone within a single
  material` が、この1枚では二つの半分の間にも掛かる。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、止まった二本の手が実写になる。**

## ⚠️ `[名前: …]` の註を、この1枚では**二本に二つ**書く——`s08` との差

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う——
  **隣の作品はそれを書き、その註を `Prompt` の中にも置いている。**
- ⛔ **この1本のどちらの場所にも、置かれる人は居ない。** 動画の仕様 §3 `nobody`——
  「**この1本に、二番目の人物は居ない。** **二本の手は、別々の場所の二人である。**」
  「⚠️ **呼んだ者は、画面に居ない。** **呼び声も置かない。**」
  §16 `MUST NOT`——「**No face is placed.**」「**No voice is heard.**」
  ⚠️ **この作品の順序は「手が先にあり、顔が後に来る」である**（`bible.world.rules`）——
  **この1本は、その順序の1歩目である。**
- ⚠️ **註は「置かれるべき人」を教えるための道具である。** **置いてはならない1本で書けば、
  それは置くための指示になる。** ⚠️ **それでもこの1枚は、註を二つ書く**——
  **二人の手が二つの凍結した一枚を指すからである。**
  - ⛔ **註が持つのは、名前と「どの一枚を取るか」だけである。****年齢も、性別も、職も、外見も持たない。**
    理由は `ledger.yaml` の `characters` の註にある——「**外見の記述は、出典に一行も無い**（方針 §5a）。
    … **凍結した一枚が、外見である。**」
    ⚠️ **名前は、どの一枚を添付するかを選ぶ鍵である**——**記述を書く許可ではない。**
    ⛔ **この作品の正典が持たないことを註が持てば、註そのものが新しい事実になる。**
  - ⛔ **そして理由は、もう一つ在る。** **`CHARACTERS` の穴は註ではなく、生成器へ渡る文字列である**
    ——**そこに書かれたものは、描かれる。** 動画の仕様が年齢や職を書くのは、
    **出典についての日本語の散文**であり、読む相手は人である（実測——`specs/video/seedance-2.5/habits-mv-s06.md` は
    「**路線バス運転士・52歳**」と引く）。⚠️ **同じ語をこの1枚の `CHARACTERS` に英語で置けば、
    行き先は `chatgpt-image-2.5` の入力である。** **中身が同じでも、行き先が違えば意味が違う。**
    ⚠️ **ゆえにこの穴には、名前と指し先しか置かない。**
- ⛔ **この作品の先例は、二本の手を1枚に置くとき註を書かなかった。** `s08` の画像仕様の
  `CHARACTERS` は「**two right hands, in two places, and no one in either place** — **each hand its own
  frozen setting sheet's**」であり、**名前を1つも書いていない。**
  **この1枚は、それと逆を選ぶ**——**二つの名前を、それぞれの註として書く。**
  ⚠️ **理由は、この1本の二人が「誰でもよい二本」ではないからである**——
  `reference_set` は `三宅隆.identity` と `池田絵里.identity` を**別々に**持ち、
  動画の仕様 §6 も**二人ぶん別々に** `REF_CHARACTER` を立てている。
  ⛔ **どちらの流儀が正しいかを決める検査は無い**——**ゆえに差を、ここに書く。**
  **黙って `s08` に合わせず、黙って `s08` から離れもしない。**
- ⚠️ **これは `scene-board` の `do` からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s22` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  この1本の失敗——**切れ目**と**二つの場所の区別**と**顔**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が「切れ目」にある。** `s22` §20 の1番目——
  「**A face may be placed.** ⚠️ **The first risk of this shot**: a hand stopping over paper reads, to a
  generator, as somebody about to look up, and **a face here answers a call the shot is about not
  receiving.**」 そして2番目——「**A voice may be added** — a distant call, a murmur — which supplies
  the call the interval is made of the absence of.」、3番目——「**The interval may be shortened or
  filled** by the generator with an extra motion.」、4番目——「**A cut may be inserted** between the two
  places.」、6番目——「**The two places may be distinguished** by light or prop.」
  **ゆえに `Negative` に `no face in the frame, no head, no shoulder, no head at either sleeve,
  no face at either sleeve` と、`no caller in the frame, no crowd, no group of people` と、
  `no cut, no dissolve, no wipe, no transition between the two places, no second camera angle,
  no reframe between the two places, no pan, no tilt, no push-in, no pull-back, no camera crossing
  between the two places` と、`no window, no clock, no difference of weather, no prop that belongs to
  one place and not the other` を置く。**
  ⚠️ **切れ目が入れば、この1本は二つの普通のショットになり、最も長いサビの行が無駄になる。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——**床は3節**であり、**この作品は `no calling voice as a sound effect` と
  `no face before the name is called` を足して5行にする**）。**ゆえにこの段落は、動画の §18 の写しではない**
  ——**同じ床を、効く場所へ置いたものである。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s22.yaml` の **`key_image`**（この稿で足した）
- `role`: **`モンタージュ`**（記録の `role`）。`place`: **`名札`**。`time`: **`勤務日の日中`**。
  `mode`: **`motion`**。`duration`: **`5.345s`**。
- `unit.after`（この1枚が写す状態）: 「二つの手が止まり、**呼ばれないままでいる。**」
- `reference_set` は**この1本では6点**である——`三宅隆.identity`・`三宅隆.negatives`・
  `池田絵里.identity`・`池田絵里.negatives`・`名札`・`名札.appearance`。
  ⚠️ **この1本は `identity` を2点とも含む**——動画の仕様 §6 が二人ぶん別々に `REF_CHARACTER` を立て、
  §15 `Identity` は「**Must preserve** — both hands from their frozen sheets」と書く。
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した一枚ずつを渡す）——
  ⛔ **それでも `CHARACTERS` の註が持つのは名前と指し先だけである**（上の節）。
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
- ⚠️ **この1枚と `s23` の画像仕様は、ほとんど同じ形である。** 実測——
  **`s22` と `s23` の `unit.before` は一言も違わない**（どちらも
  「二つの手が、**それぞれ別の紙の上にある。**」）。**`role`・`place`・`time`・`mode` も同じである。**
  差は三つ——**`unit.after`**（`s22` は「呼ばれないままでいる」／`s23` は「字は、読めないままである」）、
  **`duration`**（5.345s／6.703s）、**動画の仕様 §8 の拍**（`0-1.4/1.4-3.0/3.0-5.345s`／
  `0-1.5/1.5-3.4/3.4-6.703s`）。⚠️ **この同型は、記録の側の事実である**——
  **ゆえに二枚は、`SUBJECT` の側で書き分けられている**（`s22` は「止まって、呼ばれない」／
  `s23` は「止まって、字が読めないままである」）。**食い違いを均さず、ここに書く。**
