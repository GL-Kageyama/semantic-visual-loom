# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十三のショット「紙の端が起き、下に影ができる」（所作 / motion / 2.473s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、この作品で影が出来事になる唯一の1本である。** 動画の仕様 §13——
「**The shadow is made by the paper, not by the light**」、§9——
「**Paper makes this shadow; the light only supplies it.**」。⛔ **ゆえにこの1枚の新しさは、
明るさではなく、青灰の影である**（§15——「**The new shadow is the only new value in the frame**」）。
⚠️ **この1本と `s06` の違いは、物の剛さである**（§冒頭——「**プラスチックは曲がらず、紙は起きる。**」）。
⚠️ **この1本は指先だけを置く**（§3——「**置くのは指だけである。⚠️ 顔は置かない。手の甲も置かない**」）。
**ゆえにこの1枚も、指先だけを写す。**
⚠️ **この1枚は、この1本の終わりの状態を写す。** 記録の `unit.after` は
「紙が持ち上がり、**端が影を作っている。**」である——**渡すのは開始のコマではない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/seedance-2.5/habits-mv-s13.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into the lifted edge of a sheet of paper on a desk.**」
    ——**動画の側が先に、この様式を「机の上で紙の端が起きた状態」へ翻訳したと書いている。**
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s13.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/07_川上桜/prompt.md`
  （凍結した設定画の読み。「出典の語」の節）と、同じ作品の既存の生成物（`media/` の動画3本）
- 添付する参照: **`specs/image/生成時参照イラスト/s13/` の1枚**——`川上桜_設定画.png`。
  ⚠️ **この1枚は、この作品の動画の側の同じ1枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s13/`。実測 2026-09-28、ハッシュが一致した）。
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
  ⚠️ **この組では、`L22` は鳴らない**——`scene-board` の5穴と `luminous-anime` の4穴の
  **和が、そのまま下の7欄である**（実測 2026-09-28、`s01`・`s05`・`s11` の3枚で確認）。
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** 様式カードの雛形は
  `Not photorealistic, …` で終わるが、**この作品はそれを2段落目に置く**——**この作品は実写ではない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s13` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「端の立った状態」を写すのは、そのためである**——**渡すのは、この1本が終わった
  あとの状態＝世界の側であって、開始のコマではない。** ⚠️ **起きることは、起き終えた1枚からは
  読み取れない。ゆえに変化は、動画の側に残る。**
  ⛔ **かつ、この1枚は「動きの無い1枚」ではない。** §11 `Environmental Motion`——
  「**Dust moves over the sheet and into the new shadow. It keeps moving after the finger has stopped.**」
  ⚠️ **埃が新しい影の中へ入ることは、この1枚の中で起きている。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s13.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⚠️ **実測（2026-09-28、この稿を書く時点）**——`media/` に在るのは動画3本
  （`01_4400c8e6…mp4`・`02_c544590b…mp4`・`03_083a2440…mp4`）であり、
  `takes/` に在るのは `s01`・`s02`・`s03` の3本である。⛔ **この1本の分は、動画も画像もまだ無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の註は、この1本では「指」の側である**——**顔が置かれないからである**（`s06` と同じ形）。
⛔ **註に置くのは、人物の名と、凍結した一枚を指すことだけである。** **外見は書き起こさない**
（理由は下の節に書く）。⚠️ **この作品には、指を書く語が無い**——**凍結した一枚が指を持つ。**

- `SCENE`: the second of the work's two edge-questions, and the one where the change is a shadow — a fingertip has pressed one edge of a sheet of paper until the edge stands, and a shadow lies under it
- `CHARACTERS`: `[川上桜: **one fingertip, and no one in place** — **the hand the frozen setting sheet holds**]` — **the fingertip, the sheet and its shadow are the whole figure in the frame**; **no face, no chin, no hair, no shoulder, and no back of a hand**, the finger has stopped, and no arm is in the frame
- `SUBJECT`: one corner of one sheet of paper, up off a desk, and the blue-grey shadow it makes — **the only new thing in the frame**
- `ACTION`: having been pressed and lifted — one fingertip came down on the edge and raised it, the rest of the sheet never left the desk, the sheet bends at the edge and does not crease, and the finger has not moved since
- `LOCATION`: a desk top in a school room in the middle of a working day, 2026 — the sheet lying square to the desk's edge with the desk's grain in the near foreground, and **nothing else in the frame**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling even across the desk, so that **the paper is the brightest thing in the frame**, and the gap under the lifted edge filled by the room's cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**, and **the light does not change**
- `ACCENT`: the blue-grey of the new shadow and the cut edge of the sheet drawn as a cut edge — the two things the tube finds in a narrow, cold room

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the thirteenth step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of one edge of a sheet of paper standing up off a desk, held by one fingertip, in a school room in the middle of a working day, 2026. The frame holds three things and nothing else: the flat of the sheet, one raised corner, and the shadow in the gap beneath it. The sheet lies square to the desk's edge, the rest of it stays flat on the desk, and only this corner is up — the fingertip came down on the edge and lifted it, and the finger has not moved since. Paper gives and does not break: the sheet bends at the edge, the edge is drawn as a cut edge, and there is no crease and no fold. The shadow under the lifted edge is the shot's whole event and the only new thing in the frame — a blue-grey gap between paper and desk, filled by the room's cyan, with a soft boundary, and it was made by the paper and not by the light. Nothing is lifted off the desk and nothing is turned over; the under-side of the sheet is not shown, and the face and the back of the hand are not in the frame. The light is a fluorescent tube above and behind the camera, falling flat and even across the desk: the paper is the brightest thing in the frame, the tube's bloom sits on the pale surfaces, and everything the desk edge shadows goes to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one material and no gradient inside a single material. The palette narrows to paper, desk and skin, plus the blue-grey of the new shadow. Layered atmospheric depth from near to far; dust suspended and individually rendered where the tube catches it, moving over the sheet and into the new shadow, and it keeps moving after the finger has stopped. Very low visual density: one focal point, the lifted edge and its shadow, with the flat of the sheet filling the rest of the frame. The blocking, the camera and the light fixed as the standard every cut of this scene must match — a low, raking view along the desk surface at paper height, so that the shadow under the edge is legible as a gap between paper and desk; **the camera does not move**, it does not tilt down onto the shadow and does not push in on the edge. One scene, one staging; the same desk, the same sheet and the same tube wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no chin, no hair, no shoulder, no back of a hand, no arm in the frame, no portrait, no second figure, no person in the frame, no second finger, no second hand, no lifting of the sheet off the desk, no sheet in the air, no sheet lifted clear of the desk, no turned-over sheet, no under-side shown, no view of the under-side, no tilt onto the under-side, no crease, no folded sheet, no bent sheet, no crumpled paper, no second sheet in the frame, no page turned, no nameplate in the frame, no plastic in the frame, no object other than the sheet and the desk, no object on the desk, no pen, no movement of the shadow, no second shadow, no cast shadow of the finger, no camera movement, no tilt down onto the shadow, no push-in, no follow of the shadow, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この1枚の画面は、机の面と、その上の紙の端である。** 動画の仕様 §10——「**close**, on the sheet
  on the desk … at paper height, **looking along the surface** so that the shadow can be seen to be a
  shadow」。**空が入る余地は、構図の側に無い。** ⚠️ **しかもこの1本は、カメラが静止したままである**
  （§10 の `Camera Events` は「**None.**」）——**空へ逃げる動きも無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s13` §2——
  「**Luminous realist anime, translated into the lifted edge of a sheet of paper on a desk.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**机の上の紙が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**
- ⚠️ **この1枚では、様式の「最も明るい一点」が正しい側に落ちる。** 動画の仕様 §13——
  「**the paper is the brightest thing in the frame**」。**この画面には紙が在る。**
  ⛔ **ゆえにこの1本では、§13 の定型が画面と食い違わない**——⚠️ **食い違うのは、
  紙を持たない `s12`・`s14` の側である**（それぞれの仕様の「記録との対応」に記録した）。

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s13` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⛔ **この1本の出来事は、紙の厚みである。** §11 `Physical Characteristics`——
  「**Almost none, and visible** — the edge comes up under one fingertip and **does not need to be
  held**」。**実写の紙は、この「要らない」を写せない**——**実物の紙は、必ず何かの重さで立っている。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、机の上の紙が実物になる。**（1本目の同じ節を見よ。）

## ⚠️ 註は「どの指か」だけを教える——外見は、凍結した一枚が持つ

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**）。
  ⛔ **だが、置かれるのは指先だけである**——**註は「指」の側に付く。**
- ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**指は凍結した設定画のものである**」だけである——**註の形は、この作品で1つに決まっている**
  （`s06` が同じ形を既に取っている：`[鈴木和彦: one finger, and no one in place — the hand the
  frozen setting sheet holds]`）。
- ⛔ **そして、理由は「書かない方がよい」ではない。** `CHARACTERS` の欄は註ではなく、
  **生成器へ渡る文字列である**——**そこに書いたものは、描かれる。** 作品の側の日本語
  （人に読ませる文）と、**この欄の英語（`chatgpt-image-2.5` への入力）は、同じ中身でも宛先が違う。**
  ⚠️ **この作品の動画の仕様の側には、人物の年齢と職業の語を持つ本が在る**——実測（2026-09-28、
  27本を `grep` した。数え方は「`[0-9][0-9]歳` と、職業の語」）——**`s06` と `s07` だけである**
  （`s06` の「路線バス運転士・52歳」・`s07` の「スーパー惣菜部門・45歳」）。
  ⛔ **そして、その語はどちらも `Reference:` の行が引いている「出典の語」の中に在る**——
  **作品が人物を説明した文ではなく、出典を引いた文である。**
  ⚠️ **それでも、あれは人に読ませる日本語の文である。** **同じ語をこの欄に置けば、宛先は
  生成器であり、絵になる。**
- ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな指か」を教えることではない。**
  動画の仕様 §3——「**外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。**」
  ⚠️ **この人物の凍結した一枚は、読みと註を持つ**——`サブ/07_川上桜/prompt.md` の
  「出典の語」の節である。**ゆえにこの1枚は、指を語で書かない。**
  **語が無いところでは、書かないことが仕様である。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ 影は、紙が作る——この1枚の明るさを動かしてはならない

- 動画の仕様 §13 の `Lighting Events` は「**None.**」であり、その理由を自分で書いている——
  「**The shadow is made by the paper, not by the light** — a change of light here would steal the
  shot's whole mechanism.」
- ⛔ **ゆえにこの1枚は、影を「光の加減」で描かない。** 生成器は起きた端を「見せ場」として照らし、
  **持ち上げた紙の下を明るくしてしまう**——**それは `s05` の「紙が最も明るい」定型を写した結果であり、
  この1本では影という出来事を消す**（§20 の3番目——「**No shadow may appear** if the light is
  rendered flat, **in which case the shot has no event at all.**」）。
- ⚠️ **この1枚の影は、机の側に落ちるのでも、指の側に落ちるのでもない。** **紙と机の間の隙間である**
  ——§16 `PREFER`——「a low, raking view along the desk surface, so that **the shadow under the edge
  is legible as a gap between paper and desk**」。⛔ **ゆえに `Negative` に
  `no cast shadow of the finger` を置く**——**指の影が描かれれば、出来事の持ち主が入れ替わる。**
- ⚠️ **この1枚の影は、青灰である。** §15 `Visual`——「**The new shadow is the only new value in the
  frame**, and it is blue-grey **because it is filled by the room's cyan**」。
  **この1枚は、その一行を `LIGHT` と `ACCENT` の両方に書いている。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **この1本の危険は、この作品で最も「物の同一性」に集中している。** 動画の仕様 §20——
  「**The sheet may be lifted off the desk.** ⚠️ **The first risk of this shot**: a raised edge
  invites a lift」／「**The under-side may be shown** by a tilt or a cut」／「**The paper may crease
  or the sheet may be turned**, which changes the material」。
  ⛔ **画像の側では、この段落がそれを止める**——**`no lifting of the sheet off the desk` が、
  この1枚の中心の禁制である。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。** ⚠️ **要求を節に割れば5節であり、この段落はその5節を
  すべて文字として持つ。**
- ⚠️ **`no stack of paper` が尾に在る**——⚠️ **この1本の画面に束は無い。**
  **禁じる必要の無い1本ではあるが、尾はこの作品の共有の枠である**——**ゆえに1語も変えずに置く。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s13.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `川上桜.identity` を含む4点**である
  （`川上桜.identity`／`川上桜.negatives`／`名札`／`名札.appearance`）。
  ⚠️ **顔を置かない1本が `identity` を持つのは、指の造形のためである**（動画の仕様 §6——
  「**この1本は `identity` を添付する。** ⚠️ **指だけを置く** — 顔も手の甲も置かない。」）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⚠️ **凍結した一枚の道を、ここに実測で固定する。** この1本が `identity` として添付する一枚は
  `distill-essence-engine/examples/habits/character/サブ/07_川上桜/ChatGPT Image 2026年9月18日 05_16_15.png`
  である（実測 2026-09-28、`ls` で確認——`サブ/07_川上桜/` の中身は、この PNG と `prompt.md`
  の2つだけである）。⚠️ **この道は、動画の仕様 §6 と一致する。**
- ⚠️ **動画の仕様 §3 の `Reference:` の行は、道もファイル名も誤っていた**——§6 とは別の人物の
  フォルダを指していた。⚠️ **この稿を書いている時点で、著者の側が直している**（`s11`〜`s15` の5本）。
  ⛔ **誤っていた名前をここに写さない**——**消えた名前を引用に残せば、直っていないように読める。**
  ⚠️ **画像の側が取る一枚は、上の1行だけである。**
- ⚠️ **食い違い2（記録と仕様・裁定は著者のもの）。** この1本では、**記録の側の2語が、
  仕様の側の禁制と衝突している。**
  - 記録の `motion.quality` は「持ち上がる動きが一つ。**紙が一度だけ返る。**」と言う。
    ⛔ だが動画の仕様 §16 `MUST NOT` は「**The sheet is not lifted off the desk and not turned
    over.** ⚠️ **One edge only.**」であり、§14 は「**no sound of a page being turned** —
    **this is an edge, not a page**」と書く。**「返る」は、この1本では禁じられている。**
  - 記録の `unit.after` は「**紙が持ち上がり**、端が影を作っている。」と言う。
    ⛔ だが §16 は「**The rest of the sheet stays flat on the desk**」（§16 `MUST` の3番目）と
    言う。⚠️ **「紙が持ち上がる」は、端だけが起きることまでは言っていない。**
  ⚠️ **私は画像の側では、動画の仕様の側に立った**——**この1枚は、端だけが起き、
  残りは机に平らに着いている。** ⛔ **動画の側の裁定は著者のものである。**
- ⚠️ **食い違い3（記録と画面）。** 記録の `reference_set` は**小道具 `名札` と `名札.appearance` を
  持つ**が、⚠️ **動画の仕様 §5 は明示する**——「**この1本に名札を置かない。** `place` は `名札` で
  あるが、**この1本の物は紙である** — **`s06` の名札と対になるために、紙でなければならない。**」、
  そして「**No other object is in frame.**」。⛔ **ゆえにこの1枚は、名札を描いていない。**
  **`place` は「現場の鍵」であって、「画面に在る物」ではない**（`ledger.yaml` の `locations` の註
  ——六つの `place` を27本が巡る）。
- ⚠️ **記録の `attached` の註は、まだ「この作品はまだ1本も生成していない」と言う。**
  ⛔ **だが、いまの状態はそうではない**（実測 2026-09-28——`media/` に動画3本、`takes/` に3本、
  その3本は `s01`・`s02`・`s03` である）。**この1本は、その3本に入っていない。**
- ⛔ **この稿の文字列は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
