# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十九のショット「紙が返り、字の面が上を向く」（所作 / motion / 2.474s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、`final-chorus` の1本目である**（動画の仕様 §19——`Segment ID: final-chorus-1`）。
⚠️ **この1本の変化は「紙が返ること」である**——`unit.after` は
「紙が返り、**字の面が上を向いている。**」。`motion.quality` は
「速い。**返る動きが一つ。**紙が浮き、落ちて止まる。」と言う。**それだけである。**
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——**字の面は上を向き、誰も読んでいない。**
⛔ **浮きは、この1枚には写らない。** 浮くのは**返る途中**であり、この1枚は**落ちて止まったあと**である
（動画の仕様 §17 の優先順位1は「**The float**」——**それは動画の側が持つ**）。
⚠️ **顔は置かれない。** 動画の仕様 §3 の木村智美の指の節は「置くのは**指だけ**である。⚠️ **顔は置かない。**」と書き、
§16 `MUST NOT` は「**The face does not enter the frame**, and no pointing finger appears.」を持つ。
⚠️ **この現場は、サビの14本が共有する現場である**（`ledger.locations.名札`——
`S05`〜`S08`・`s12`〜`S16`・`s19`〜`s23`）。**14本が同じ場所であることは、14本が同じ絵であることではない**
（動画の仕様 §4）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s19.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a sheet of paper turning over on a desk.**」そして
    「here the sheet is lit on both sides, so **the turn is read as a change of value rather than a change
    of position.**」——**動画の側が先に、この様式を「机の上で返る紙へ翻訳した」と書いている。**
    画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s19.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/11_木村智美/ChatGPT Image 2026年9月18日 05_13_12.png`
  （**凍結した人のかたちの一枚**。`ledger.yaml` の `木村智美.identity` が指す先であり、
  動画の仕様 §6 も同じ先を指す）＋ 同じ作品の既存の生成物（`media/` の動画）
- 添付する参照: **`specs/image/生成時参照イラスト/s19/` の1枚**——`木村智美_設定画.png`。
  ⚠️ **この1枚は、この作品の動画の側の同じ1枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s19/`。実測 2026-09-28、ハッシュが一致した）。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s19` §6——「**この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が「字の面が上を向いて止まった紙」を写すのは、そのためである**
  ——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  **浮くことも、返ることも、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。**
- 記録: `shots/habits-mv-s19.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の `[名前: …]` の註は、この1枚では「名前と、どの一枚を取るか」だけを持つ**——
理由は下の節に書く。**外見は、凍結した一枚が持つ。**

- `SCENE`: the first of the final chorus — a sheet of paper lying face-down on a desk has turned over and landed with its written side up, and nothing reads it
- `CHARACTERS`: `[木村智美: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **the hand, the cuff and the desk are the whole figure in the frame**; **no face, no chin, no hair, no shoulder above the cuff**, the hand is finished and does not point, and no arm is in the frame
- `SUBJECT`: the sheet with its written side up at the frame's centre, and the one right hand that has finished turning it
- `ACTION`: having turned over — the sheet is face-up, it has floated once and fallen, and it has stopped; the hand that turned it is flat and at rest, **it does not hover, it does not point, and nothing is read**
- `LOCATION`: a desk in a school room in the middle of a working day, 2026, with the sleeve and its nameplate at the edge of frame — the desk's worn wooden face, and **the nameplate worn on the cloth and not on the desk**; **nothing else on the desk**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling across the desk and the paper, bloom on the pale surfaces, so that **the sheet's two faces differ in value because of their angle to the tube and not because the light changes**; deep cyan in everything the desk edge shadows; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the sheet's two faces as two values of the same cream — the one warm thing the tube finds on the desk, and the brightest thing in the frame

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the first of the final chorus of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of a sheet of paper on a desk that has turned over and landed with its written side up, and the one right hand that turned it, at a desk in a school room in the middle of a working day, with the sheet's two faces as two values of the same cream and the light, not the figure, as the subject. The sheet lies at the frame's centre, square to the desk's edge, written side up, its grain visible on the side that landed upward and dust settled along its lifted edge; the characters on it are present on screen and not readable — the marks of cut print and of ballpoint and of pencil drawn as the three different marks they are, and none of them legible. The hand is one right hand and nothing else of a figure — the pads, the back of the hand, the knuckles, the wrist, no further, the arm not in the frame beyond the plain cuff — and it is finished: it has stopped, it does not hover, and it does not point at the writing. No head enters the frame, no shoulder, no face, and no standing figure; the sleeve and its nameplate are at the edge of frame only, the nameplate present and unreadable and worn on the cloth and not on the desk. Nothing else is on the desk. The writing is not read: no eye is in the frame, no head bends over the sheet, and no finger tracks a line of it. The light is one fluorescent tube above and behind the camera, falling flat and even across the desk and the paper, bloom on the pale surfaces, so that the sheet's two faces differ in value because of their angle to the tube and not because the light changes; the paper is the brightest thing in the frame, and everything the desk edge shadows has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one material and no gradient inside a single material. The palette is paper, desk and skin — and the sheet's two faces are two values of the same cream. Layered atmospheric depth from near to far; dust suspended and individually rendered in the air above the desk where the tube catches it, still moving after the paper has stopped, and it is the only thing in the frame that is still moving. Low visual density: one focal point, the sheet with its written side up, with the desk filling the rest of the frame. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens close on the desk at the sleeve site, looking slightly down and not moving at all, the sheet at the frame's centre and the sleeve and its nameplate at the edge of frame. One scene, one staging; the same desk, the same tube and the same sleeve wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no reading, no eye in the frame, no head bent over the sheet, no finger tracking a line, no face in the frame, no head, no shoulder, no standing figure, no second figure, no pointing finger, no hand hovering over the writing, no second turn of the sheet, no second sheet, no sheet lifted, no sheet carried, no sheet put anywhere, no sheet handed to anyone, no crease, no flutter, no curl at the corner, no nameplate on the desk, no nameplate lying flat, no nameplate taken off the sleeve, no second nameplate, no push-in as the sheet lands, no tilt down onto the writing, no rack focus onto the characters, no insert of the writing, no magnified detail of the characters, no cut, no zoom, no reframe, no second camera angle, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies」「Volumetric god rays」
  「Anamorphic lens flare」「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**机と、その上の紙と、袖しか映さない**——
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s19` §2 `Visual Language`——
  「**Luminous realist anime, translated into a sheet of paper turning over on a desk.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**机の上の紙が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その「光」が紙の裏表を値の差にしている**（`s19` §2——「**the turn is read as a
  change of value rather than a change of position**」）。**光は、返ったことを読ませる道具である。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ 短い所作が三本続く——この1本と `s20`・`s21` を、同じ絵にしてはならない

- ⚠️ **`s19`・`s20`・`s21` は、同じ現場（`名札`）・同じ時刻（`勤務日の日中`）・同じ `role`（所作）で、
  三本続けて2.6秒未満である。**
  実測（`shots/` の `duration`）——**`s20` 2.393秒 ＜ `s19` 2.474秒 ＜ `s21` 2.554秒。**
  ⛔ **「この曲で最も速い畳みかけ」とは書けない。** 実測——**2.6秒未満が三本続く区間は、この曲に三つある**
  （`s05`〜`s07` が7.420秒／`s12`〜`s14` が7.420秒／`s19`〜`s21` が7.421秒。**差は1ミリ秒である**）。
  ⚠️ **区間の速さでは、三つを区別できない。** ⚠️ **区別できるのは、三本の長さの揃い方である**——
  前の二つは三本が互いに1ミリ秒以内（2.473/2.474/2.473 と 2.473/2.473/2.474）であるのに対し、
  **この三本は 2.474/2.393/2.554 と互いに違い、そのうちの `s20` が、2.6秒未満の9本のうちで最も短い**
  （⚠️ **27本のうち2.6秒未満は9本で、そのすべてが `所作`・`名札` である**——`shots/` の実測）。
  ⚠️ **三本のうち最も短いのは `s20` であり、動画の仕様 §1 は「この作品の27本のうち、これが最小である」と書く。**
- ⛔ **それでも、三本は同じ絵ではない。** **変わる物が、三本で別である**——
  - **この1本（`s19`）で変わるのは「紙」である。** `motion.quality`——
    「速い。**返る動きが一つ。**紙が浮き、落ちて止まる。」
  - **`s20` で変わるのは「名札の角」である。** `motion.quality`——「速い。**つまむ動きが一つ。**
    ほとんど持ち上がらない。」⚠️ **そして動画の仕様 §4 は「⚠️ **この1本に紙は無い。**」と明記する。**
  - **`s21` で変わるのは「束から出る一枚」である。** `motion.quality`——
    「速い。**押さえる動きが一つ。**紙が一枚、指の間で出る。」
- ⚠️ **ゆえに三本の `SUBJECT` は、それぞれ「紙」「名札の角」「束と、出る一枚」である。**
  ⛔ **同じ構図を三度書けば、この畳みかけは1本に見える。** **`place` が同じであることは、
  絵が同じであることを意味しない**（動画の仕様 §4——「**14本が同じ場所であることは、
  14本が同じ絵であることではない**」）。
- ⚠️ **カメラも三本で別である。** この1本は**机の高さで、袖の現場へ寄る**（動画の仕様 §10——
  「close, on the desk at the sleeve site」）。`s20` は**同じ現場の最も近い1本**であり
  （「**very close**, on the left sleeve — **the work's `名札` site at its closest**」）、
  `s21` は**束の高さ**である（「close, on the desk at the sleeve site, **at the height of the bundle**」）。
- ⚠️ **三本は、動画の側でも別の `Segment ID` を持つ**——`final-chorus-1`／`-2`／`-3`。

## ⚠️ 名札は袖に在る——この1本で、紙は机の上である

- ⚠️ **この1本には、名札と紙が同時に在る。** `ledger.locations.名札` の `geography` は
  「**「左袖」である**——ゆえに**名札は人に付いている。** ⚠️ **この作品は、名札を机の上に置かない**」と定める。
  ゆえに**この1枚でも、机の上にあるのは紙だけである。**
- ⚠️ **動画の仕様 §16 `PREFER` は、その配置を名指しで書いている**——
  「The sheet at the frame's centre with **the sleeve and its nameplate at the edge of frame**,
  so that **the site is stated without the nameplate being the subject.**」
  **この1枚はその側に立つ。****名札は現場を告げるだけで、主題ではない。**
- ⚠️ **ゆえに `Negative` に `no nameplate on the desk, no nameplate lying flat,
  no nameplate taken off the sleeve, no second nameplate` を置く。**
  ⚠️ **名札が机に置かれれば、この作品は「名札」という現場を失う**——
  **`名札` が現場である理由は、それが人に付いていることである。**

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s19` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚が写すのは、人の手と、一枚の紙である。** ゆえに `no photographic faces` だけでなく、
  **`no grain`・`no painterly brush strokes`・`no glossy plastic page`・`no plastic-looking paper`
  もこの1枚で効く**——**返った紙は紙であり、艶のある面ではない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、机の上の紙が実写になる。**

## ⚠️ 様式カードの `[名前: …]` の註は、この1枚では**名前と指し先だけ**を持つ

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う——
  **隣の作品はそれを書き、その註を `Prompt` の中にも置いている。**
- ⛔ **この1本に置かれるのは指だけであり、顔は置かれない**（動画の仕様 §3——
  「置くのは**指だけ**である。⚠️ **顔は置かない。**」、§16 `MUST NOT`——
  「**The face does not enter the frame**, and no pointing finger appears.」）。
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
- ⚠️ **ゆえに `CHARACTERS` は `[木村智美: …]` の註と、この1本で枠に入る範囲だけを持つ。**
  名前のあとの記述は、**人ではなく、枠の側の話である**（「手と袖口と机が画面の全部である」）。
- ⚠️ **これは `scene-board` の `do` からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s19` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  この1本の失敗——**読ませること**と**返りきらないこと**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が「読ませること」にある。** `s19` §20 の1番目——
  「**The sheet may be read.** ⚠️ **The first risk of this shot**: a page landing face-up is an
  invitation to show what is on it, and **the work's whole subject is a name that is present and not
  read.**」 そして2番目——「**The float may be skipped**」、3番目——「**The sheet may be lifted and
  carried**」、5番目——「**The nameplate may be put on the desk**」。
  **ゆえに `Negative` に `no reading, no insert of the writing, no magnified detail of the characters,
  no rack focus onto the characters, no tilt down onto the writing` と、
  `no sheet lifted, no sheet carried, no sheet put anywhere` と、
  `no nameplate on the desk, no nameplate lying flat` を置く。**
  ⚠️ **そして `no crease, no flutter, no curl at the corner` を置く**——動画の仕様 §11——
  「**The sheet does not crease and does not flutter** — it turns over as a plane.」
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——**床は3節**であり、**この作品は `no calling voice as a sound effect` と
  `no face before the name is called` を足して5行にする**）。**ゆえにこの段落は、動画の §18 の写しではない**
  ——**同じ床を、効く場所へ置いたものである。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s19.yaml` の **`key_image`**（この稿で足した）
- `role`: **`所作`**（記録の `role`）。`place`: **`名札`**。`time`: **`勤務日の日中`**。
  `mode`: **`motion`**。`duration`: **`2.474s`**。
- `unit.after`（この1枚が写す状態）: 「紙が返り、**字の面が上を向いている。**」
- `reference_set` は**この1本では4点**である——`木村智美.identity`・`木村智美.negatives`・`名札`・
  `名札.appearance`。⚠️ **この1本は `identity` を含む**——動画の仕様 §6——
  「**この1本は `identity` を添付する** — 指の造形がこの人物のものであるためである。⚠️ **顔は置かない。**」
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した一枚を渡す）——
  ⛔ **それでも `CHARACTERS` の註が持つのは名前と指し先だけである**（上の節）。
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
- ⚠️ **動画の仕様 §13 `Base Lighting` の一文は、この1本では字義どおりには効かない。**
  そこには「**the paper is the brightest thing in the frame**」と在り、この1本は紙を持つので
  **この1本では成り立つ**——⚠️ **だが同じ一文が `s20` にも貼られており、あちらには紙が無い**
  （`s20` §4——「⚠️ **この1本に紙は無い。**」）。**これは `s05`・`s06` で既に記録した型の欠陥である**
  （`specs/image/habits-mv-s05.md` の該当の節）。**ここに、消さずに書く。**
