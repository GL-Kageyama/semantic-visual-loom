# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十四のショット「手が閉じ、何も持たないまま止まる」（所作 / motion / 2.474s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、この作品で唯一「紙もプラスチックも画面に無い」1本である**——動画の仕様 §2——
「**this shot has no paper in it at all**」、§15——「**This is the only shot in the work with no
paper and no plastic in it.**」。⛔ **ゆえにこの1枚は、机と手だけで出来ている。**
⚠️ **この1本の出来事は、閉じることである**（§12——「**The event is the closure.**」）。
⚠️ **この手は、`s12` の手と対である**（§3 `Continuity Requirements`——「**`s12` の手が「開いて止まる」、
この手が「閉じて止まる」である**——**二本は対である。**」）。**ゆえにこの1枚も、掌を見せない**
（§12——「**does not have it open to check**」）。
⚠️ **この1枚は、この1本の終わりの状態を写す。** 記録の `unit.after` は
「**手が閉じ、何も持たないまま止まっている。**」である——**渡すのは開始のコマではない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/seedance-2.5/habits-mv-s14.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into an empty hand closing on nothing.**」
    ——**動画の側が先に、この様式を「何も無い所で閉じる空の手」へ翻訳したと書いている。**
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s14.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/08_関翔太/prompt.md`
  （凍結した設定画の読み。「出典の語」の節）と、同じ作品の既存の生成物（`media/` の動画3本）
- 添付する参照: **`specs/image/生成時参照イラスト/s14/` の1枚**——`関翔太_設定画.png`。
  ⚠️ **この1枚は、この作品の動画の側の同じ1枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s14/`。実測 2026-09-28、ハッシュが一致した）。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s14` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「閉じ終えた手」を写すのは、そのためである**——**渡すのは、この1本が終わった
  あとの状態＝世界の側であって、開始のコマではない。** ⚠️ **閉じることは、閉じ終えた1枚からは
  読み取れない。ゆえに変化は、動画の側に残る。**
  ⛔ **かつ、この1枚は「動きの無い1枚」ではない。** §11 `Environmental Motion`——
  「**Dust moves over the desk and around the closed hand. It keeps moving after the fingers have
  stopped.**」
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s14.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⚠️ **実測（2026-09-28、この稿を書く時点）**——`media/` に在るのは動画3本
  （`01_4400c8e6…mp4`・`02_c544590b…mp4`・`03_083a2440…mp4`）であり、
  `takes/` に在るのは `s01`・`s02`・`s03` の3本である。⛔ **この1本の分は、動画も画像もまだ無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の註は、この1本では「手」の側である**——**顔が置かれないからである。**
⛔ **註に置くのは、人物の名と、凍結した一枚を指すことだけである。** **外見は書き起こさない**
（理由は下の節に書く）。⚠️ **この作品には、手を書く語が無い**——**凍結した一枚が手を持つ。**

- `SCENE`: the second half of the chorus's question about the reading hand — a right hand that has closed on nothing and stopped, on a desk that has nothing on it
- `CHARACTERS`: `[関翔太: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **the hand and the bare desk are the whole figure in the frame**; **no face, no chin, no hair, no shoulder, no arm, no sleeve**, the fingers are closed and nothing is in them
- `SUBJECT`: the closed empty right hand, and the bare desk it rests on
- `ACTION`: having closed — the fingers came down to the palm with nothing between them, the wrist did not turn and the arm did not move, the closure is a closure and not a grab, and it does not open again
- `LOCATION`: a desk top in a school room in the middle of a working day, 2026 — the desk's worn wooden face with the polish of forearms on it, its edge at the frame's lower right, and **nothing on it at all**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling even across the bare wood and blooming on the pale surfaces, falling across the back of the hand so that **the closing is read entirely in the knuckles and in the shadow between the fingers**; deep cyan in everything the desk edge shadows; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**, and **the light does not move**
- `ACCENT`: the shadow between the closing fingers — the shot's most detailed passage — and the polish of forearms on the wood, the two warm-grey things the tube finds in a narrow, cold room

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the fourteenth step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of a right hand closed on nothing, resting on a bare desk, in a school room in the middle of a working day, 2026. The hand is the whole figure in the frame and the only motion it has ever had: it lies where it lay, it has closed in place, the fingers came down to the palm with nothing between them, and it does not open again. Nothing is in the hand — the closure is a closure and not a grab, there is nothing to grab, and the hand is not a fist: no clench, no whitened knuckles, and no grip. There is no arm in the frame past the wrist: the wrist runs out of the picture on the right and the picture's edge crops it — no sleeve, and no face: no chin, no hair, no shoulder above the desk. The desk is bare — worn wood with the polish of forearms on it, its grain under the hand, and its worn edge at the frame's lower right; there is no paper and no plastic anywhere in the frame, and nothing of any kind lies on the desk. The light is a fluorescent tube above and behind the camera, falling flat and even across the bare wood and blooming on the pale surfaces: it falls across the back of the hand, so the closing is read entirely in the knuckles and in the shadow between the fingers, which is the shot's most detailed passage, and deep cyan fills everything the desk edge shadows. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one material and no gradient inside a single material. The palette is desk and skin, and nothing else. Layered atmospheric depth from near to far; dust suspended and individually rendered over the desk where the tube catches it, moving around the closed hand, and it keeps moving after the fingers have stopped. Very low visual density: one focal point, the closed hand, with the bare desk filling the rest of the frame and nothing else in it. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at hand height, close, looking slightly down, the hand at the frame's centre with the wrist running out of the picture on the right, the desk's edge at the lower right, and **the camera does not travel and does not push in**. One scene, one staging; the same bare desk, the same hand and the same tube wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no chin, no hair, no shoulder above the desk, no portrait, no second figure, no second hand, no person in the frame, no object in the hand, no object in the closed hand, no object gripped, no paper in the frame, no sheet of paper, no plastic in the frame, no nameplate in the frame, no object on the desk, no pen, no cup, no key, no book, no opening again of the hand, no release, no fingers opening at the end, no view of the empty palm, no clenched fist, no whitened knuckles, no fist raised, no arm in the frame past the wrist, no sleeve, no cuff, no forearm, no turn of the wrist, no second movement of the hand, no camera movement, no push-in, no follow of the hand, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この1枚の画面は、裸の机の面と、その上の閉じた手である。** 動画の仕様 §2 は
  「**The palette is desk and skin, and nothing else — this shot has no paper in it at all.**」と言い、
  §10 は手の高さの close を取る。**空が入る余地は、構図の側に無い。**
  ⚠️ **しかもこの1本は、カメラが静止したままである**（§11 `Subject Motion`——「**The arm is not
  in frame; the wrist does not turn.**」、§20 の6番目——「**The camera may push in**, asking the fist
  a question the shot does not answer.」）——**空へ逃げる動きも無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s14` §2——
  「**Luminous realist anime, translated into an empty hand closing on nothing.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**裸の机が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**
- ⚠️ **この1枚には、様式の「最も明るい一点」が人物の上に無い。** **最も明るいのは、裸の机の面である**
  ——⚠️ **動画の仕様 §13 の定型は「the paper is the brightest thing in the frame」と言うが、
  この画面には紙が無い**（下の「記録との対応」に、この食い違いを記録した）。

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s14` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⛔ **この1本の細部は、指と掌の間の影である。** 動画の仕様 §13——
  「**The shadow between the closing fingers is the shot's whole rendering problem.**」
  **実写の手が戻れば、この1枚は「何かを握っている実在の手」になる**——
  **§20 の1番目——「an empty fist looks like a mistake to a generator」——が、そのまま起きる。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、何も持たない手が実物になる。**（1本目の同じ節を見よ。）

## ⚠️ 註は「どの手か」だけを教える——外見は、凍結した一枚が持つ

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**）。
  ⛔ **だが、置かれるのは手だけである**——**註は「手」の側に付く。**
- ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**手は凍結した設定画のものである**」だけである——**註の形は、この作品で1つに決まっている。**
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
- ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな手か」を教えることではない。**
  動画の仕様 §3——「**外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。**
  置くのは**右手だけ**である。⚠️ **顔は置かない。**」
  ⚠️ **この人物の凍結した一枚は、読みと註を持つ**——`サブ/08_関翔太/prompt.md` の
  「出典の語」の節である。**ゆえにこの1枚は、手を語で書かない。**
  **語が無いところでは、書かないことが仕様である。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ 空の手は、掴んだことになる——この1枚の中心の禁制

- 動画の仕様 §20 の1番目——「**An object may be placed in the hand.** ⚠️ **The first risk of this
  shot and the one that would invert its meaning**: an empty fist looks like a mistake to a
  generator, and **a filled one is a different shot entirely.**」
- ⛔ **ゆえに `Negative` に `no object in the hand` を置く。** これはこの作品で
  **`s12` の `no object in the palm` と対になる行である**——**開いた掌と、閉じた手の、同じ禁制。**
- ⚠️ **同じ危険が、机の側からも伸びる**（§20 の3番目——「**An object may be added to the desk**
  — a pen, a stack, a cup — which gives the hand something to have been near.」）。
  §16 `MUST NOT` の3番目——「**No object is placed on the desk in this shot** — **an empty desk is
  the shot.**」⛔ **ゆえに `no object on the desk` と `no paper in the frame` を置く。**
- ⚠️ **そして、この1本の禁制は「物」だけではない。** §20 の4番目——
  「**The fist may be clenched as a gesture of resolve; the shot's closure is not a clench.**」
  ⛔ **ゆえに `no clenched fist, no whitened knuckles, no fist raised` を置く**
  ——⚠️ **`no fist` とは書かない。閉じた手は拳ではない、というのがこの1本の側である**
  （§11——「**The closure is a closure, not a grab** — there is nothing to grab.」）。

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。** ⚠️ **要求を節に割れば5節であり、この段落はその5節を
  すべて文字として持つ。**
- ⚠️ **`no stack of paper` が尾に在る**——⚠️ **この1本の画面には、そもそも紙が無い。**
  **禁じる必要の無い1本ではあるが、尾はこの作品の共有の枠である**——**ゆえに1語も変えずに置く。**

## ⚠️ 手首の切れ目は、枠の縁で起きる（2026-09-30、著者の裁定）

- 実測（2026-09-30）。この稿の文字列は投入され、1枚が生成された
  （`media/NG_14_ChatGPT Image 2026年9月30日 02_02_49.png`——**著者が NG と名付けた**）。
  ⛔ **その1枚でも、手は枠の内側で終わっていた**——手首の先が輪郭線で閉じ、その下に落ち影が付き、
  **右に約400pxの裸の机が残る**（実測——肌の列は x≈1265 で尽きる。枠は1672px）。
  ⚠️ **`s12` の1枚と同じ形である**——**この2本は同じ家族である**（`Prompt` が手を枠の中央に置き、
  同じ段落が腕を禁じる）。**ゆえに、2本とも同じ欠陥が出た。**
- ⚠️ **この作品は、答えを既に持っている。** 動画の仕様 `s05` §10——
  「**the cuff at the frame's edge**, so that the plate reads as **worn rather than as lying on a
  surface**」。⚠️ **`s19`・`s21`・`s22`・`s23` も同じ形である**（「arm not in the frame **beyond the
  plain cuff**」）。**切れ目を枠の縁に置けば、体の続きが見える。**
- ⛔ **ゆえにこの稿は、2段落を直した**（2026-09-30。裁定は——「禁制を緩める。切れ目は枠の縁、
  ただし袖・袖口・前腕は描かない」）。`Prompt` の腕の行を「**no arm in the frame past the wrist**——
  **the wrist runs out of the picture on the right and the picture's edge crops it**」へ、`Prompt` の
  構図の行へ「**with the wrist running out of the picture on the right**」を、`Negative` の
  「no arm in the frame」を「**no arm in the frame past the wrist**」へ。
  ⛔ **袖・袖口・前腕は、禁じたままである。**
- ⚠️ **動画の仕様 §10 の1行も、同じ語で直した**（2026-09-30——
  「looking slightly down, **with the whole desk empty around it**」→
  「…**with the wrist running out of the picture on the right and the rest of the desk empty**」）。
  **この1枚は、その動画の参照画像である**——**構図が食い違えば、参照が嘘になる。**
  ⚠️ **動画の側の §11（「The arm is not in frame; the wrist does not turn.」）は動かしていない**
  ——**腕は、いまも描かれない。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s14.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `関翔太.identity` を含む4点**である
  （`関翔太.identity`／`関翔太.negatives`／`名札`／`名札.appearance`）。
  ⚠️ **顔を置かない1本が `identity` を持つのは、手の造形のためである**（動画の仕様 §6——
  「**この1本は `identity` を添付する。** ⚠️ **顔は置かない。**」）。
  ⚠️ **関翔太は第二巻の人物である**（記録の註——サブ 8/24、第二巻第3話・主役回、
  第二巻第13話にもう一度立つ）。⛔ **画面には、その巻の印が何も無い**——
  **この作品の四巻の違いは、この作品では違いではない**（`s13` の記録の註と同じ理屈である）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⚠️ **凍結した一枚の道を、ここに実測で固定する。** この1本が `identity` として添付する一枚は
  `distill-essence-engine/examples/habits/character/サブ/08_関翔太/ChatGPT Image 2026年9月20日 19_53_47.png`
  である（実測 2026-09-28、`ls` で確認——`サブ/08_関翔太/` の中身は、この PNG と `prompt.md`
  の2つだけである）。⚠️ **この道は、動画の仕様 §6 と一致する。**
- ⚠️ **動画の仕様 §3 の `Reference:` の行は、道もファイル名も誤っていた**——§6 とは別の人物の
  フォルダを指していた。⚠️ **この稿を書いている時点で、著者の側が直している**（`s11`〜`s15` の5本）。
  ⛔ **誤っていた名前をここに写さない**——**消えた名前を引用に残せば、直っていないように読める。**
  ⚠️ **画像の側が取る一枚は、上の1行だけである。**
- ⚠️ **食い違い2（仕様の内側・裁定は著者のもの）。** 動画の仕様 §13 の `Base Lighting` は
  「**the paper is the brightest thing in the frame**」と言うが、**同じ仕様の §2 が
  「this shot has no paper in it at all」と言い、§15 が「the only shot in the work with no paper
  and no plastic in it」と言う。** ⛔ **同じ仕様の §2 と §13 が、紙の在否で食い違っている。**
  **この1枚で最も明るいのは、裸の机の面である**（上の `LIGHT` はそう書いた）。
  ⚠️ **同じ定型は `s12` の §13 にも在る**（あちらは紙も名札も置かない1本である）。
  **この定型は27本で共有されており、紙を持たない1本では意味を失う。** **この1枚は、定型ではなく
  画面の側を書いた。**
- ⚠️ **食い違い3（記録と画面）。** 記録の `reference_set` は**小道具 `名札` と `名札.appearance` を
  持つ**が、⚠️ **動画の仕様 §5 は明示する**——「**この1本に紙も名札も置かない。** **物が在れば、
  閉じた手はそれを掴んだことになる**——**掴まないことが、この1本である。**」、そして
  「**No other object is in frame.**」。⛔ **ゆえにこの1枚は、名札を描いていない。**
  **`place` は「現場の鍵」であって、「画面に在る物」ではない**（`ledger.yaml` の `locations` の註）。
- ⚠️ **記録の `attached` の註は、まだ「この作品はまだ1本も生成していない」と言う。**
  ⛔ **だが、いまの状態はそうではない**（実測 2026-09-28——`media/` に動画3本、`takes/` に3本、
  その3本は `s01`・`s02`・`s03` である）。**この1本は、その3本に入っていない。**
- ⛔ **この稿の文字列は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
