# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第二十のショット「指が名札の角をつまみ、少し持ち上げる」（所作 / motion / 2.393s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、`final-chorus` の2本目である**（動画の仕様 §19——`Segment ID: final-chorus-2`）。
⚠️ **この1本の変化は「角が浮くこと」である**——`unit.after` は
「指が名札の角をつまみ、**少し持ち上げている。**」。`motion.quality` は
「速い。**つまむ動きが一つ。**ほとんど持ち上がらない。」と言う。
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——**角は浮き、指は止まり、名札は袖に着いたままである。**
⛔ **この1本に、紙は無い。** 動画の仕様 §4——「⚠️ **この1本に紙は無い。** **物は名札だけである。**」
§5——「**この1本で動く物は、これだけである。**」⚠️ **ゆえにこの1枚は、この作品で唯一、
紙を持たない画像仕様である。**
⚠️ **持ち上がるのは角だけである。** 動画の仕様 §1——「**the plate never leaves the sleeve.**」
§16 `MUST`——「**The plate does not leave the sleeve.**」
⚠️ **顔は置かれない。** 動画の仕様 §3 の山田健太の指の節は「置くのは**指だけ**である。
⚠️ **顔は置かない。**」と書き、§16 `MUST NOT` は「**The face does not enter the frame.**」を持つ。
⚠️ **この1本は、この現場の最も近い1本である**（動画の仕様 §4）——**袖と名札しか入らない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s20.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a corner of plastic lifted off cloth.**」そして
    「here the lifted corner takes the tube and throws a shadow onto the sleeve, so **the whole change is
    legible in a few millimetres of shadow.**」——**動画の側が先に、この様式を
    「布から浮いたプラスチックの角へ翻訳した」と書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s20.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/12_山田健太/ChatGPT Image 2026年9月21日 00_52_45.png`
  （**凍結した人のかたちの一枚**。`ledger.yaml` の `山田健太.identity` が指す先であり、
  動画の仕様 §6 も同じ先を指す）＋ 同じ作品の既存の生成物（`media/` の動画）
- 添付する参照: **`specs/image/生成時参照イラスト/s20/` の1枚**——`山田健太_設定画.png`。
  ⚠️ **この1枚は、この作品の動画の側の同じ1枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s20/`。実測 2026-09-28、ハッシュが一致した）。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s20` §6——「**この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が「角が浮いて止まった名札」を写すのは、そのためである**
  ——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  **つまむ所作そのものは、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。**
- 記録: `shots/habits-mv-s20.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の `[名前: …]` の註は、この1枚では「名前と、どの一枚を取るか」だけを持つ**——
理由は下の節に書く。**外見は、凍結した一枚が持つ。**

- `SCENE`: the second of the final chorus — two fingers pinch one corner of the nameplate the person is wearing and lift that corner a little, and the plate stays on the sleeve
- `CHARACTERS`: `[山田健太: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **the fingers and the plate are the whole figure in the frame**; **no face, no chin, no hair, no shoulder above the cuff**, the fingers do not close on the plate, and no arm is in the frame
- `SUBJECT`: the plastic nameplate worn on the left sleeve, one corner of it pinched between two fingertips and off the cloth
- `ACTION`: pinching and lifting — two fingers arrive at one corner, take it, and bring it up by a few millimetres, and then stop; **the corner pivots and the rest of the plate stays flat, there is no spring back, and the plate is not being taken off**
- `LOCATION`: a left sleeve carrying the school's nameplate at a desk in the middle of a working day, 2026 — **the sleeve filling the frame and the desk only at the corner of frame**; **no paper, and nothing on any desk**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera, and **the lifted corner takes the tube and throws a shadow onto the cloth, so that the whole change is legible in a few millimetres of shadow**; bloom on the plastic's highlight and no bloom on the cloth, deep cyan in everything the sleeve shadows; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the plastic's highlight and the thin shadow under the lifted corner — **the brightest thing in the frame is the plate, not the paper**, because there is no paper

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the second of the final chorus of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration, very close on a left sleeve at a desk in the middle of a working day, of the school's designated plastic nameplate worn on the cloth with one corner pinched between two fingertips and lifted a few millimetres off it, and the light, not the figure, as the subject. The sleeve fills the frame and the desk appears only at the corner of frame: no paper is anywhere, and nothing else is on any surface. The lifted corner takes the tube and throws a shadow onto the cloth, so that the whole change is legible in a few millimetres of shadow; the plastic keeps a hard highlight and the cloth does not, and the plastic's highlight is the brightest thing in the frame. The weave of the sleeve is drawn at this distance and so is the plate's grain; the corner pivots and the rest of the plate stays flat against the arm, and it has stopped where the fingers stopped. The fingers do not close on the plate and nothing is being unfastened — the plate is not coming off, and the sound of a fastening would be a different shot. The plate's characters are present on screen and not readable, drawn as the marks they are and never resolving. No face enters the frame, no head, no shoulder, no standing figure; the fingers, the cuff and the plate are the whole figure, and no arm is in the frame beyond the cuff. Nothing is read: no finger points at the plate's face, the plate's face is not turned toward the camera, and no eye is in the frame. The light is one fluorescent tube above and behind the camera, falling flat and even, with bloom on the plastic's highlight and on the pale surfaces, and everything the sleeve shadows gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside the cloth and no gradient inside the plastic. The palette is cloth, plastic and skin, near to a neutral cloth grey and the pale plastic of a school's designated nameplate. Layered atmospheric depth from near to far; dust suspended and individually rendered where the tube catches it, and after the fingers stop the dust goes into the shadow under the lifted corner and keeps moving there — it is the only thing in the frame that is still moving. Very low visual density: one focal point, the lifted corner, with the sleeve filling the rest of the frame. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens very close on the left sleeve and unmoving, the plate and its pinched corner at the frame's centre, and the desk's edge only at the corner of frame. One scene, one staging; the same sleeve, the same tube and the same plate wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no legible text on any surface, no legible name text, no readable characters on any prop, no legible characters on the nameplate, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no paper, no sheet, no page, no bundle, no desk surface in frame, no desk beyond its edge, no face in the frame, no head, no head above the cuff, no shoulder, no standing figure, no second figure, no second hand, no arm in the frame, no fingers closing on the plate, no grip, no plate taken off the sleeve, no plate removed, no pin undone, no fastening opened, no click, no pin, no velcro, no plate on the desk, no plate lying flat on anything, no second nameplate, no spare nameplate, no corner lifted beyond a few millimetres, no bend of the plate, no spring back, no flex, no plate turned toward the camera, no plate's face shown, no finger pointing at the plate, no reading, no eye in the frame, no insert of the plate, no magnified detail of the characters, no rack focus onto the plate, no push-in on the corner, no cut, no zoom, no reframe, no second camera angle, no extra motion added to fill the time, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies」「Volumetric god rays」
  「Anamorphic lens flare」「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**袖と、その上の名札しか映さない**——
  **この現場が、この作品でいちばん近くまで寄られる1本であり**（動画の仕様 §10——
  「**the work's `名札` site at its closest**」——⚠️ **近さが名指しされているのは「現場」であって
  「作品」ではない**）、**空が入る余地は構図の側に1つも無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s20` §2 `Visual Language`——
  「**Luminous realist anime, translated into a corner of plastic lifted off cloth.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**名札の角が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その「光」がプラスチックの面を画面で最も明るいものにしている**
  （`s20` §2——「**the plastic's highlight is the brightest thing in the frame**」）。
  ⚠️ **この一文は、この作品にとって異常である**——**この作品の他の26本は、紙を最も明るいものとする。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ 短い所作が三本続く——この1本と `s19`・`s21` を、同じ絵にしてはならない

- ⚠️ **`s19`・`s20`・`s21` は、同じ現場（`名札`）・同じ時刻（`勤務日の日中`）・同じ `role`（所作）で、
  三本続けて2.6秒未満である。**
  実測（`shots/` の `duration`）——**`s20` 2.393秒 ＜ `s19` 2.474秒 ＜ `s21` 2.554秒。**
  ⛔ **「この曲で最も速い畳みかけ」とは書けない。** 実測——**2.6秒未満が三本続く区間は、この曲に三つある**
  （`s05`〜`s07` が7.420秒／`s12`〜`s14` が7.420秒／`s19`〜`s21` が7.421秒。**差は1ミリ秒である**）。
  ⚠️ **区間の速さでは、三つを区別できない。** ⚠️ **区別できるのは、三本の長さの揃い方である**——
  前の二つは三本が互いに1ミリ秒以内であるのに対し、**この三本は互いに違い、
  そのうちのこの1本が、2.6秒未満の9本のうちで最も短い**（⚠️ **27本のうち2.6秒未満は9本で、
  そのすべてが `所作`・`名札` である**——`shots/` の実測）。
  ⚠️ **三本のうち最も短いのが、この1本である。** 動画の仕様 §1——「**The shot has the least motion in
  the work**」、`motion.law`——「**この1本の動きの量は、この作品で最小である**」。
- ⛔ **この1本は、三本のうちで唯一、紙を持たない。** 動画の仕様 §4——
  「⚠️ **この1本に紙は無い。** **物は名札だけである。**」
  ⚠️ **ゆえに「三本は同じ現場で同じ長さの所作である」は成り立つが、「三本は同じ絵である」は成り立たない。**
  - **`s19` で変わるのは「紙」である**（机の上で一枚が返る）。
  - **この1本（`s20`）で変わるのは「名札の角」である**——**布から数ミリ、それだけである。**
  - **`s21` で変わるのは「束から出る一枚」である**（束は動かず、一枚が指の間へ出る）。
- ⚠️ **最も近いこと自体が、この1本の設計である。** 動画の仕様 §10——「**very close**, on the left
  sleeve — **the work's `名札` site at its closest.**」「⚠️ **Nothing but cloth, plate and fingers is in
  the frame.**」**ゆえに机は端だけであり**（§16 `PREFER`——「**the desk's edge only at the corner of
  frame**」）、**この1本は「机の上の1本」ではない**（§5）。
- ⚠️ **三本は、動画の側でも別の `Segment ID` を持つ**——`final-chorus-1`／`-2`／`-3`。

## ⚠️ この1本に紙は無い——`Base Lighting` の一文は、ここでは成り立たない

- ⚠️ **動画の仕様 §13 `Base Lighting` は、27本のどれにも同じ一文を貼っている**——
  「the light falls flat and even across the desk and **the paper is the brightest thing in the frame**」。
- ⛔ **この1本には紙が無い**（§4・§5）。**ゆえに「紙が最も明るい」は、この1本では偽である。**
  同じ §13 は直後に「Deep cyan in everything **the desk edge** shadows」とも言うが、
  **この1本は机を端しか持たない**（§16 `PREFER`）。**この一文も、字義どおりには効かない。**
- ⚠️ **この1本が実際に持つのは、§2 の側の一文である**——
  「**the plastic's highlight is the brightest thing in the frame**」。
  **ゆえにこの1枚は、明るさの順位を §2 から取る**——**§13 からではない。**
- ⚠️ **これは、この作品の既に記録された型の欠陥である。** `s05`・`s06` でも同じことが起きている
  （`specs/image/habits-mv-s05.md`・`-s06.md` の該当の節——**§13 が「紙が最も明るい」と言い、
  §16 が「この1本に紙は無い」と言う**）。
  ⛔ **ゆえに、ここでは `Negative` に `no paper, no sheet, no page` を置き、
  `Prompt` の側で明るさの順位を名指しする。** **食い違いを黙って均さない。**

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s20` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚が写すのは、布と、プラスチックと、指先である。** ゆえに `no photographic faces` だけでなく、
  **`no grain`・`no painterly brush strokes`・`no soft airbrush`・`no rendered fabric fold`
  もこの1枚で効く**——**この作品で最も近い1枚では、布の織り目とプラスチックの粒が描かれる**
  （§2 `Texture`——「**The weave of the sleeve is drawable at this distance, and so is the plate's
  grain.**」）。**実写の質感で書けば、この1本は「物の写真」になる。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、名札の角が実写になる。**

## ⚠️ 様式カードの `[名前: …]` の註は、この1枚では**名前と指し先だけ**を持つ

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う——
  **隣の作品はそれを書き、その註を `Prompt` の中にも置いている。**
- ⛔ **この1本に置かれるのは指だけであり、顔は置かれない**（動画の仕様 §3——
  「置くのは**指だけ**である。⚠️ **顔は置かない。**」、§16 `MUST NOT`——
  「**The face does not enter the frame.**」）。
  ⚠️ **この作品の順序は「手が先にあり、顔が後に来る」である**（`bible.world.rules`）——
  **この1本は、その順序の1歩目である。**
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
- ⚠️ **ゆえに `CHARACTERS` は `[山田健太: …]` の註と、この1本で枠に入る範囲だけを持つ。**
  名前のあとの記述は、**人ではなく、枠の側の話である**（「指と袖口と名札が画面の全部である」）。
- ⚠️ **動画の仕様 §15 は、この1本と `s06` の差を名指しで保存している**——
  「`s06` raises an edge to look behind it, `s20` pinches a corner and stops.」
  ⛔ **この差は所作の差であって、註の差ではない。** **註は、この差によって何も増えない。**
- ⚠️ **これは `scene-board` の `do` からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s20` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  この1本の失敗——**名札が外れること**と**動きを足して時間を埋めること**——を禁じているのは、
  **この段落である。**
- ⛔ **この1本では、危険が「外れること」にある。** `s20` §20 の1番目——
  「**The plate may be removed.** ⚠️ **The first risk of this shot**: a pinched corner reads as the
  beginning of taking something off, and **a removed plate spends `s18`'s whole subject in two
  seconds.**」 そして3番目——「**The corner may be lifted too far**, turning a few millimetres into an
  action.」、4番目——「**The shot may be filled with extra motion** to occupy the time — **the amount is
  the shot.**」、6番目——「**The plate's face may be turned toward the camera and read.**」
  **ゆえに `Negative` に `no plate taken off the sleeve, no plate removed, no pin undone,
  no fastening opened, no click, no pin, no velcro` と、
  `no corner lifted beyond a few millimetres, no bend of the plate, no spring back` と、
  `no extra motion added to fill the time` と、
  `no plate's face shown, no plate turned toward the camera` を置く。**
  ⚠️ **`no click, no pin, no velcro` は §14 の「置かれた不在」である**——
  「⚠️ **And one absence, placed rather than left out: nothing unfastens**」。
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——**床は3節**であり、**この作品は `no calling voice as a sound effect` と
  `no face before the name is called` を足して5行にする**）。**ゆえにこの段落は、動画の §18 の写しではない**
  ——**同じ床を、効く場所へ置いたものである。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s20.yaml` の **`key_image`**（この稿で足した）
- `role`: **`所作`**（記録の `role`）。`place`: **`名札`**。`time`: **`勤務日の日中`**。
  `mode`: **`motion`**。`duration`: **`2.393s`**。
- `unit.after`（この1枚が写す状態）: 「指が名札の角をつまみ、**少し持ち上げている。**」
- `reference_set` は**この1本では4点**である——`山田健太.identity`・`山田健太.negatives`・`名札`・
  `名札.appearance`。⚠️ **この1本は `identity` を含む**——動画の仕様 §6——
  「**この1本は `identity` を添付する** — 指の造形がこの人物のものであるためである。⚠️ **顔は置かない。**」
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した一枚を渡す）——
  ⛔ **それでも `CHARACTERS` の註が持つのは名前と指し先だけである**（上の節）。
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
- ⚠️ **記録の `motion.subject` は「山田健太の指と、名札の角。」と言い、動画の仕様 §3 は
  「置くのは指だけである」と言う。** ゆえに `CHARACTERS` の註の後ろは**指の側**に合わせてある
  （`s05` が「手」の側、`s06` が「指」の側に合わせたのと同じ扱いである）。
