# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第二十三のショット「二つの手が止まり、紙の上の字は、読めないままである」（モンタージュ / motion / 6.703s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、`final-chorus` の5本目である**（動画の仕様 §19——`Segment ID: final-chorus-5`）。
⚠️ **この1本の変化は「読めないままである」ことである**——`unit.after` は
「二つの手が止まり、**紙の上の字は、読めないままである。**」。`motion.quality` は
「速い所作を二度。**そのあと、長く止まる。**」と言い、`motion.law` は
「**止まったあと、紙は一度もしなない**——**この作品の最後のサビの、最後の静止である。**」と定める。
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——**二つの手は止まり、
その下の字は、依然として語になっていない。**
⛔ **「長く止まる」の長さは、この1枚には写らない。** 秒は時間の側にある（下の `## 記録との対応`）。
⚠️ **カメラは二つの場所を跨がない。** 動画の仕様 §16 `MUST NOT`——
「**No cut and no camera crossing between the two places.**」⚠️ **ゆえに `place` は単数である**
（`名札`）——**二人は別の場所にいるが、画面は一つである**（`ledger.locations` の註）。
⚠️ **この現場は、サビの14本が共有する現場である**（`ledger.locations.名札`——
`s05`〜`s08`・`s12`〜`s16`・`s19`〜`s23`）。
⛔ **この1本は、この作品で最後の「顔でない」ショットである。** 動画の仕様 §15 `Spatial`——
「**This is the last shot of the final chorus that is not a face** — `s24` and `s25` put faces on four
people.」⚠️ **ゆえにこの1枚は、顔が来る前の最後の一枚である。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s23.md` は
    この1本でも同じ組を立てている。**動画の側が先に、この様式を「二本の手」へ訳している。**
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s23.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/` の**凍結した宮下遥の一枚**と
  **凍結した橋本悠斗の一枚**（`ledger.yaml` の `宮下遥.identity` と `橋本悠斗.identity` が指す先である）
  ＋ 同じ作品の既存の生成物（`media/` の動画）
  ⚠️ **この1本の `reference_set` は6点である**——`宮下遥.identity`・`宮下遥.negatives`・
  `橋本悠斗.identity`・`橋本悠斗.negatives`・`名札`・`名札.appearance`。
  ⚠️ **`negatives` が `reference_set` に入っているのは、この作品ではこの2本だけである**
  （`s22` と `s23`）——**それが何を意味するかは下の「床」の節に書く。**
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
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** **この作品は `Not photorealistic, …` を2段落目に置く。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この1枚が「止まったあとの二枚の紙」を写すのは、そのためである**——**渡すのは世界の側である。**
  **押さえる所作も、長い静止も、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** **この作品の前提は「名は、どこにも読めない」である**
  ——**文字列に日本語の字を置けば、置かれる側へ回る。** ⚠️ **この1本では、その一行がとくに重い**（下の節）。
- 記録: `shots/habits-mv-s23.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の `[名前: …]` の註は、この1枚では「名前と、どの一枚を取るか」だけを持つ**——
理由は下の節に書く。**外見は、凍結した二枚が持つ。**

- `SCENE`: the fifth of the final chorus — two hands in two places stop on two sheets inside one frame, the second taking the same posture as the first, and the writing under both stays unresolved
- `CHARACTERS`: `[宮下遥: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` `[橋本悠斗: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **two right hands, in two places, and no one in either place**; **no face, no chin, no hair, no shoulder above either cuff, and no standing figure at either sleeve**, and neither hand is reading anything
- `SUBJECT`: two right hands at rest on two sheets of paper at two left sleeves, the second in the same posture as the first, in one composition
- `ACTION`: having pressed and stopped — one hand came down flat, stopped, and the second has taken the same posture and stays in it; **the paper does not flex again after the stop, nothing is turned or lifted, and the writing under the two hands stays exactly as unresolved as it was before they moved**
- `LOCATION`: two left sleeves carrying the school nameplate, at two desks in the middle of a working day, 2026, held in one frame — **the same composition twice**, the plate and the paper under each hand the only things in it; **no window, no clock, and nothing that would tell the two places apart**
- `LIGHT`: the room's constant state, and **the same light in both places** — **the light lies at a reading angle across both halves and does not change**, flat and even, bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the sleeves shadow gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the cream of the paper under each hand — **the same cream twice**, and the only warm thing in the frame besides skin

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the fifth of the final chorus of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of two right hands at rest on two sheets of paper at two left sleeves carrying the school's nameplate, in the middle of a working day, with the cream of the paper under each hand as the only warm thing in the frame besides skin and the light, not the figure, as the subject. One composition holds both places and it does not cut: the same frame geometry carries both, and the second hand has taken the posture the first one took and is staying in it. Each hand has come down flat on its own sheet and has stopped, and the sheet did not flex when it landed and does not flex again; the characters on the two sheets are present on screen and not readable — drawn as the three different marks of cut print and of ballpoint and of pencil, each of them still an unfinished mark, none of them a word. Each hand is the only figure in its own place — the pads, the back of the hand, the knuckles, no further, the arm not in the frame beyond the plain cuff. No head enters the frame at either sleeve, no shoulder, no face, and there is no third hand and no third place; nobody is reading either sheet, and nothing in the frame is being called. Nothing in the frame tells the two places apart: the same desk-height, the same cloth, the same plastic, the same paper — there is no window, no clock, no difference of weather, and no prop that belongs to one place and not the other, so that **the only difference between the two halves is how much deep cyan the shadows hold**. The light is one fluorescent tube above and behind the camera, lying at a reading angle across both places and not changing — bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the sleeves shadow gone to deep cyan — and the dust over the two sheets and the light crossing the paper are the only things still moving. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette is the same palette twice: paper cream, skin, cloth, and the dark of a pressed shadow. Layered atmospheric depth from near to far, dust suspended and individually rendered where the tube catches it, and very low visual density — one focal point, the resting hand, twice. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens close at the desk and unmoving, the paper at the frame's centre in both halves, and the writing on it no more in focus than the hand that rests on it. One scene, one staging; the same desk, the same tube and the same press wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no legible text on any surface, no legible name text, no characters resolving into words, no resolvable glyph, no readable kanji, no readable kana, no readable script of any kind, no sharper focus on the writing than on the hand, no magnified detail of the characters, no insert of the writing, no focus pull onto the writing, no rack focus, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no reading, no eye in the frame, no head bent over the paper, no finger tracking the writing, no face in the frame, no head, no shoulder, no head at either sleeve, no face at either sleeve, no standing figure, no second figure, no third hand, no third place, no caller in the frame, no crowd, no group of people, no cut, no dissolve, no wipe, no transition between the two places, no second camera angle, no reframe between the two places, no pan, no tilt, no push-in, no pull-back, no camera crossing between the two places, no camera movement during the stop, no difference of light between the two places, no window, no clock, no difference of weather, no prop that belongs to one place and not the other, no distinguishing detail between the two halves, no third desk, no lifted paper, no turned sheet, no peel, no sheet taken, no sheet handed to anyone, no flex of the paper after the stop, no ripple, no spring back, no lifted corner of the paper, no curl, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies」「Volumetric god rays」
  「Anamorphic lens flare」「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**二つの袖と、その下の紙しか映さない**——
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、既に翻訳を書いている。** `s23` §2 `Visual Language`——
  「**Luminous realist anime, translated into two hands at rest.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**止まった二本の手が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その光が「読む角度」で二つの半分に同じだけ横たわる**——
  **光は、二つを一つに見せる道具であると同時に、「読めてしまう」ことへの圧である。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ この1本の床は、この作品でいちばん厚い——`no legible text on any surface` が「床だから」ではなく「この行のため」に効いている

- ⚠️ **この1本の二人は、床の行数が違う。** `ledger.yaml` の実測（2026-09-28）——
  **`characters.*.negatives` は、この作品の六人のうち五人が3行である**——
  `no face before the name is called`・`no identifying clothing, hairstyle, or prop`・`no legible name text`。
  ⛔ **`橋本悠斗` だけが4行である**——**その3行に `no legible text on any surface` が足されている。**
- ⚠️ **理由は、話の側にある。** `shots/habits-mv-s23.yaml` の前書き——
  「**第二巻第8話は、名が読まれる話である**——ゆえにこの一人の手が持つ紙は、
  **この作品で唯一、読める字を持ちうる。**」
  ⚠️ **ゆえに `reference_set` に `negatives` が入っているのは、この作品では `s22` と `s23` の2本だけである。**
  **床の行そのものが、この1本では参照物として添付される。**
- ⛔ **それでもこの作品は読ませない。** 同じ前書き——
  「⚠️ **それでもこの作品は読ませない。** ——**この1本が持つ行は「まだ、呼ばれていない。」である。**
  **読める字を置けば、呼ばれていないことの方が偽になる。**」
  ⚠️ **そして「`no legible text on any surface` は27本すべてに在る**（`props.*.negative`）。
  **この1本だけは、その一行が「床だから」ではなく「この行のため」に効いている。**」
- ⛔ **ゆえにこの1枚の `Negative` は、字を「読ませない」ために、いちばん多くの節を使う。**
  実測（2026-09-28、2段落目を `, ` で切り、`character`・`glyph`・`text`・`script`・`kanji`・`kana`・
  `romaji`・`alphabet`・`cursive`・`handwriting`・`signature`・`read` の語を含む節を数えた。
  ⚠️ **`no character added beyond the shot`（「このショット以外の人物を足さない」）は数から外した**
  ——**この作品で `character` は「字」と「人物」の両方を意味する**）——
  **字に触れる節は、`s22` が14、この1本が17である。** 段落の総節も **`s22` が105、この1本が116**。
  ⚠️ **この1本だけが持つ節は5つ**——`no characters resolving into words`・`no resolvable glyph`・
  `no readable kanji`・`no readable kana`・`no readable script of any kind`。
  ⚠️ **焦点の側では、`s22` が2節・この1本が5節である**（実測——
  `s22` は `no insert of the writing`・`no magnified detail of the characters`、
  この1本はそれに `no sharper focus on the writing than on the hand`・`no focus pull onto the writing`・
  `no rack focus` を足す）。**数えたのは、実際に並べてからである。**
- ⚠️ **そして `Prompt` の側でも、字は「語になっていない」と書かれる**——
  「each of them still an unfinished mark, none of them a word」。
  ⛔ **これは演出ではなく、この1本の危険への対処である**——**下の節を参照。**

## ⚠️ 止まったあと、紙は一度もしなない——この1枚が写すのは「最後の静止」である

- ⚠️ **この1本の法は、運動の側に在る。** `motion.law`——
  「**止まったあと、紙は一度もしなない**——**この作品の最後のサビの、最後の静止である。**」
- ⚠️ **残りの二拍は、二つの「以上」である。** `beats` の実測——`0-1.5s` は `dense`
  （「宮下遥の手。**紙を押さえる。**」）、`1.5-3.4s` は `held`（「止まる。」）、
  `3.4-6.703s` は `held`（「橋本悠斗の手が、**同じ姿勢を取る。**」）。
  ⚠️ **`6.703s` のうち、`5.203s` が `held` である**（`1.5` から `6.703` まで。`beats` の三行から引いた）。
  ⛔ **「この作品で最も長い静止」とは書けない。** 実測（`shots/` の `beats` から `held` の合計を引いた）——
  **27本のうち、この1本は6番目である**（`s27` 10.809秒 ＞ `s17` 9.032秒 ＞ `s26` 6.006秒 ＞
  `s10` 5.514秒 ＞ `s09` 5.295秒 ＞ **この1本 5.203秒**）。⚠️ **この1本が持つのは「長さ」ではなく
  「最後であること」である**——`motion.law` の言葉は「**この作品の最後のサビの、最後の静止**」であって、
  **最長の静止ではない。**
- ⛔ **1枚は時間を持たない。** ゆえにこの1枚は、**止まっている最中の一枚**を写す——
  **二本の手が同じ姿勢で止まり、その下の紙が、しなったままの形で固まっていない。**
  ⚠️ **ゆえに `Negative` に `no flex of the paper after the stop, no ripple, no spring back,
  no lifted corner of the paper, no curl` を置く。** **紙が動けば、最後の静止が静止でなくなる。**
- ⚠️ **この1枚が「読めないまま」を写すのは、この静止のあとの状態である。**
  **字は、止まる前から読めなかった。****止まったことが、読めないことにしたのではない。**
  ⛔ **この区別が、この1本と `s24`・`s25`（顔が来る2本）を分けている。**

## ⚠️ 二つの場所を、光で区別してはならない

- ⚠️ **この1本は二つの場所を1枚に置く。** 動画の仕様 §16 `MUST NOT` は
  「**No cut and no camera crossing between the two places.**」と定め、
  §13 `Lighting Events` は「**None, in either place.**」と書く——
  **`s23` は「the light lies at a reading angle in both halves and does not change」である。**
- ⛔ **ゆえにこの1枚は、二度目の側にだけ窓を置かない。****窓も、時計も無い**（動画の仕様 §4）。
  **光も、埃の量も、同じである。**
  ⚠️ **この作品は、名札を机の上に置かない**（`ledger.locations.名札` の `geography`）——
  **ゆえに「机の上の名札」は、この1枚でも起きない。**
- ⚠️ **差は、位置だけである**——動画の仕様 §15 `Spatial`——
  「⚠️ **The two places occupy the same frame geometry** — **the second posture lands where the first one
  did.**」**この1枚が写す「同じ姿勢」は、その差の側である。**
- ⚠️ **この1本は、この作品で三度目の「二つの場所を1枚に置く」である**——`s08`（`chorus-1` の4本目）、
  `s22`（`final-chorus` の4本目）、そしてこの1本。⚠️ **この1枚は、`s08` の画像仕様の写しではない。**
  ⛔ **ゆえに `SUBJECT` は「the second in the same posture as the first」と言い、
  `ACTION` は「the writing … stays exactly as unresolved as it was before they moved」と言う**——
  **同じ構図の上で、写す状態が違う。**

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** §16 `MUST NOT` は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持ち、
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚が写すのは、人の手であり、二度写される。** ゆえに `no photographic faces` だけでなく、
  **`no grain`・`no painterly brush strokes`・`no soft airbrush` もこの1枚で効く。**
  ⚠️ **そして二度写すということは、同じ手が二つの描き方で現れうるということである**——
  **`no second shadow tone within a single material` が、この1枚では二つの半分の間にも掛かる。**
- ⚠️ **この1本では、写実が「読める字」の側からも来る。** 実写に寄れば寄るほど、
  紙の上の線は**語として解像する**——**ゆえに `no sharper focus on the writing than on the hand` が、
  この1枚では「様式の防波堤」と「この行の防波堤」を兼ねる。**

## ⚠️ `[名前: …]` の註を、この1枚では**二本に二つ**書く——`s08` との差

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⛔ **この1本のどちらの場所にも、置かれる人は居ない。** 動画の仕様 §16 `MUST NOT`——
  「**No face is placed.** ⚠️ **This shot carries the work's thickest floor for exactly this reason.**」
  「**No voice is heard.**」⚠️ **この作品の順序は「手が先にあり、顔が後に来る」である**
  （`bible.world.rules`）——**この1本は、その順序の最後の一歩である。****次に来るのは、顔である。**
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
    **出典についての日本語の散文**であり、読む相手は人である（実測——`specs/video/habits-mv-s06.md` は
    「**路線バス運転士・52歳**」と引く）。⚠️ **同じ語をこの1枚の `CHARACTERS` に英語で置けば、
    行き先は `chatgpt-image-2.5` の入力である。** **中身が同じでも、行き先が違えば意味が違う。**
    ⚠️ **ゆえにこの穴には、名前と指し先しか置かない。**
- ⛔ **この作品の先例は、二本の手を1枚に置くとき註を書かなかった。** `s08` の画像仕様の
  `CHARACTERS` は「**two right hands, in two places, and no one in either place** — **each hand its own
  frozen setting sheet's**」であり、**名前を1つも書いていない。**
  **この1枚は、それと逆を選ぶ**——**二つの名前を、それぞれの註として書く。**
  ⚠️ **理由は、この1本の二人が「誰でもよい二本」ではないからである**——
  `reference_set` は `宮下遥.identity` と `橋本悠斗.identity` を**別々に**持ち、
  ⚠️ **とくに `橋本悠斗` の側は、`negatives` が参照物としてこの1本に効いている**（上の「床」の節）。
  ⛔ **どちらの流儀が正しいかを決める検査は無い**——**ゆえに差を、ここに書く。**
  **黙って `s08` に合わせず、黙って `s08` から離れもしない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  この1本の失敗——**字が語になること**と**切れ目**と**顔**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が「解像」にある。** 動画の仕様 §20 の1番目——
  「**The characters may resolve into words.** ⚠️ **The first risk of this shot**」——
  **この作品で最も厚い床を持つ1本の、最初の危険がこれである。**
  §16 `MUST NOT`——「**No characters resolve into words.** ⚠️ **This shot carries the work's thickest
  floor for exactly this reason.**」
  **ゆえに `Negative` に、字に触れる14行（上の「床」の節に列挙したもの）を置く。**
  ⚠️ **この1本の失敗は静かである**——**一枚の紙が読めた瞬間、この行が持っていた意味が反転する。**
  他の失敗（顔・切れ目・声）は目に見えるが、**この失敗は「よく描けている」側から来る。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——**床は3節**であり、**この作品は `no calling voice as a sound effect` と
  `no face before the name is called` を足して5行にする**）。**ゆえにこの段落は、動画の §18 の写しではない**
  ——**同じ床を、効く場所へ置いたものである。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s23.yaml` の **`key_image`**（この稿で足した）
- `role`: **`モンタージュ`**（記録の `role`）。`place`: **`名札`**。`time`: **`勤務日の日中`**。
  `mode`: **`motion`**。`duration`: **`6.703s`**。
- `unit.after`（この1枚が写す状態）: 「二つの手が止まり、**紙の上の字は、読めないままである。**」
- `reference_set` は**この1本では6点**である——`宮下遥.identity`・`宮下遥.negatives`・
  `橋本悠斗.identity`・`橋本悠斗.negatives`・`名札`・`名札.appearance`。
  ⚠️ **`negatives` を2点とも含むのは、この作品では `s22` と `s23` だけである。**
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
- ⚠️ **この1枚と `s22` の画像仕様は、ほとんど同じ形である。** 実測——
  **`s22` と `s23` の `unit.before` は一言も違わない**（どちらも
  「二つの手が、**それぞれ別の紙の上にある。**」）。**`role`・`place`・`time`・`mode` も同じである。**
  差は四つ——**`unit.after`**（`s22` は「呼ばれないままでいる」／`s23` は「字は、読めないままである」）、
  **`duration`**（5.345s／6.703s）、**`beats` の切り方**（`0-1.4/1.4-3.0/3.0-5.345s`／
  `0-1.5/1.5-3.4/3.4-6.703s`——⚠️ **どちらも `held` が二拍で、この1本のほうが `1.358s` 長い**）、
  そして**床**（`s23` だけが `橋本悠斗` の4行目を参照物として持つ）。
  ⚠️ **この同型は、記録の側の事実である**——**ゆえに二枚は、`ACTION` の側で書き分けられている**
  （`s22` は「止まって、呼ばれない」／`s23` は「止まって、字が語にならない」）。
  **食い違いを均さず、ここに書く。**
- ⚠️ **この1枚は、この作品で最後の「顔でない」ショットの一枚である**（動画の仕様 §15 `Spatial`——
  「**`s24` and `s25` put faces on four people.**」）。**次に来る1枚は、顔を持つ。**
