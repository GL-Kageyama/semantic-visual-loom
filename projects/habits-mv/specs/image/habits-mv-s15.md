# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十五のショット「二度のめくりが、一つの位置で起きる」（モンタージュ / motion / 4.867s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、27本で唯一のモンタージュである**（記録の `role: "モンタージュ"`）。
⛔ **そして、カメラは動かず、切らない**——動画の仕様 §16 `MUST` の3番目——
「**The camera does not move and does not cut.**」、§10 `Camera Events`——「**None.**」。
**ゆえにこの1枚は、二つの場所を、一つの枠の中に、区切り無しで持つ。**
⚠️ **この1本の出来事は、重なりである**——§12 `Emotional Events`——
「**The event is the overlap.** **The shot gives the audience two turns in half the time of the
earlier one and does not point at the repetition.**」、§16 `MUST` の2番目——
「**The second turn begins before the first finishes.**」
⚠️ **この1本は顔を置かない**（§3——「置くのは**右手だけ**である。⚠️ **顔は置かない。**」、
§16 `MUST NOT` の最後——「**No third hand and no third page.**」）。
⚠️ **この1枚は、二度とも終わった状態を写す。** 記録の `unit.after` は
「二つの手が止まり、**紙だけが残っている。**」である——**渡すのは開始のコマではない。**
⛔ **そして、この1本では「途中のどの1コマ」も、この1枚には向かない**——§16 `MUST` の2番目が
「二度目は一度目が終わる前に始まる」と言うので、**途中の1コマでは、二つの場所が必ず非対称になる**
（一方は動いており、他方は止まっている）。**両方が止まっている状態だけが、二つを同じ値で持つ。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s15.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a page being turned at a desk.**」
    ——**動画の側が先に、この様式を「机の上でめくられる頁」へ翻訳したと書いている。**
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s15.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/09_長田美穂/prompt.md` と
  `…/サブ/19_斎藤悦子/prompt.md`（凍結した設定画の読み。「出典の語」の節）と、
  同じ作品の既存の生成物（`media/` の動画3本）
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s15` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「二つとも止まった状態」を写すのは、そのためである**——**渡すのは、この1本が
  終わったあとの状態＝世界の側であって、開始のコマではない。** ⚠️ **めくることは、めくり終えた
  1枚からは読み取れない。ゆえに変化は、動画の側に残る。**
  ⛔ **かつ、この1枚は「動きの無い1枚」ではない。** §11 `Environmental Motion`——
  「**Dust moves over both sheets. It keeps moving after both turns have finished.**」
  ⚠️ **埃は、二枚の上を、二度とも止まったあとも動き続ける。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s15.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
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

- `SCENE`: the chorus's only montage — two right hands turning two pages in two places inside one frame, one after the other, and both stopping with only the paper left
- `CHARACTERS`: `[長田美穂: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` and `[斎藤悦子: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **the two hands and the two sheets are the whole figure in the frame**; **no face, no head, no chin, no hair, no shoulder above either cuff**, no arm past either cuff, and the two hands are two hands in two places and not one hand drawn twice
- `SUBJECT`: two right hands at rest on two sheets in two places, in one unbroken frame
- `ACTION`: having turned — each hand turned its own page once, the second turn began before the first had finished, and both have stopped; **the pages were turned and not read**, and neither hand points at the other
- `LOCATION`: two desk tops in two school rooms in the middle of a working day, 2026, held in one frame at two depths — the same worn wood, the same sheet and the same fluorescent tube in both, and **nothing distinguishes the two places**: no difference of light, no different prop, no different time
- `LIGHT`: the room's constant state in both places at once — the flat light of a fluorescent tube above and behind the camera falling even across the desk, so that **the paper is the brightest thing in the frame**, with the tube's bloom on the pale surfaces and deep cyan in everything the desk edge shadows; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**, and **the light is the same in both places**
- `ACCENT`: the two turned pages lying in the same value, twice — and the two sheets' pale, which is the brightest thing in the frame in both places

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the fifteenth step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of two right hands turning two pages at two desks, in two school rooms in the middle of a working day, 2026 — and both turns are already finished. ⚠️ One unbroken frame holds the two places at two depths, a nearer desk and a farther one, with no dividing line, no border, no panel and no seam between them: the same worn wood, the same sheet of paper and the same fluorescent tube in both, and nothing in the frame says which room is which. Two right hands rest on two sheets, each hand at its own sheet — two hands in two places, and not one hand drawn twice. Each hand has turned its own page once, the second turn began before the first had finished, and both have stopped: the two hands are still and do not point at each other, and nothing is in them. The pages were turned and not read — the two turned pages lie where they were turned, in the same value, twice, and no writing on any sheet is legible. Nothing is read: no finger tracks a line and no eye is in the frame. The light is a fluorescent tube above and behind the camera, falling flat and even across both desks and blooming on the pale surfaces: the paper is the brightest thing in the frame in both places, deep cyan fills everything each desk edge shadows, and the light is identical in the two places — no difference of light, no different prop and no different time of day distinguishes them. Clean anime lineart on both hands at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one material and no gradient inside a single material. The palette is paper, desk and skin, twice, in the same values. Layered atmospheric depth from near to far; dust suspended and individually rendered over both sheets where the tube catches it, and it keeps moving after both turns have finished. Low, continuous visual density: one focal point, the turning page, twice, with the desk filling the frame. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the same view of the desk in both places, the two turns occupying the same frame geometry so that the second page turns where the first one did, and **the camera does not move, does not cut and does not reframe**. One scene, one staging; the same desk, the same sheet and the same tube wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no head, no chin, no hair, no shoulder above either cuff, no portrait, no second person, no third hand, no third page, no third place in the frame, no cut, no dissolve, no wipe, no split screen, no panel division, no diptych, no border between the two places, no seam between the two places, no dividing line, no light difference between the two places, no colour difference between the two places, no different prop in the two places, no different time of day in the two places, no reading of the pages, no finger tracking a line, no eye in the frame, no magnified writing, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no closing of the pages, no page turned back, no second turn of the same page, no book, no binding, no spine, no nameplate in the frame, no plastic in the frame, no camera movement, no pan between the two turns, no reframe, no zoom, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この1枚の画面は、二つの机の面と、その上の二本の手である。** 動画の仕様 §10 は
  the work's desk site を close で取ると言い、§11 は「**Each is the only motion its own place
  has.**」と言う。**空が入る余地は、構図の側に無い。**
- ⚠️ **しかもこの1本は、カメラが動かない**（§16 `MUST` の3番目——「**The camera does not move
  and does not cut.**」、§10 `Camera Events`——「**None.**」）——**空へ逃げる動きも無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s15` §2——
  「**Luminous realist anime, translated into a page being turned at a desk.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**二つの机の上の紙が、夕景になる。**
  ⛔ **この1本では、それが特に危ない**——**二つの場所を区別する物を置けないので、様式の空は
  「二つの場所を区別する物」として入り込む余地を持つ**（§16 `MUST NOT` の2番目——
  「**The two places are not distinguished by light, prop or time of day.**」、
  §20 の4番目——「**The two places may be distinguished** by light or prop.」）。
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s15` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⛔ **この1本の出来事は、紙の重さである。** §11 `Physical Characteristics`——
  「**None.** ⚠️ **A page turning is the lightest complete movement in this work.**」
  ‖「**The turning page swings on its own and lies down** — **the only place in this work where
  paper is in the air.**」**実写の紙は、この「自力で揺れて寝る」を写せない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、机の上の紙が実物になる。**（1本目の同じ節を見よ。）

## ⚠️ 註は「どちらの手か」だけを教える——外見は、凍結した二枚が持つ

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が二人居る**——**ゆえに註は二つ書く**（`s01` は書かない。
  **人が居ないからである**）。⛔ **だが、置かれるのは手だけである**——**註は「手」の側に付く。**
- ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**手は凍結した設定画のものである**」だけである——**註の形は、この作品で1つに決まっている**
  （`s08`・`s16` が同じ形を既に取っている——**二つの註が並ぶ1本である**）。
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
- ⚠️ **註の仕事は「どちらの人物か」を教えることであって、「どんな手か」を教えることではない。**
  動画の仕様 §3——「**外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。**
  置くのは**右手だけ**である。」（二人とも同じ一行を持つ）。
  ⚠️ **この二人の凍結した一枚は、読みと註を持つ**——`サブ/09_長田美穂/prompt.md` と
  `サブ/19_斎藤悦子/prompt.md` の「出典の語」の節である。
  **ゆえにこの1枚は、手を語で書かない。** **語が無いところでは、書かないことが仕様である。**
- ⚠️ **二つの註が要るのは、この1本の禁制が「同一性」の側にも掛かるからである。**
  §16 `MUST NOT` の最後——「**No third hand and no third page.**」
  ⛔ **ゆえに `CHARACTERS` は「二本の手は、二人の手であって、一本の手を二度描いたものではない」と
  書き、`Negative` に `no third hand` を置く。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ この1本はモンタージュである——この1枚は、二つの場所を持ち、区切りを持たない

- **この作品の `role` は15種あり、`モンタージュ` はこの1本だけである**（記録の `role`）。
  ⛔ **カットが在れば、この1本は二本になる**——§20 の1番目——
  「**A cut may be inserted**, turning the montage into two shots.」
- ⛔ **ゆえに `Negative` に `no cut, no dissolve, no wipe, no split screen, no panel division,
  no diptych, no border between the two places, no seam between the two places, no dividing line`
  を置く。** ⚠️ **この作品の他の26本には要らない行である**——**分ける手段を持つのは、
  モンタージュを名乗るこの1本だけである。**
- ⚠️ **区切りは「切る」側にだけ在るのではない。** §16 `MUST NOT` の2番目——
  「**The two places are not distinguished by light, prop or time of day.**」、
  §20 の4番目——「**The two places may be distinguished** by light or prop.」
  ⛔ **ゆえに `no light difference between the two places, no colour difference between the two
  places, no different prop in the two places, no different time of day in the two places` を置く。**
  ⚠️ **この1枚の二つの場所は、同じ明るさで、同じ木で、同じ紙である**（上の `LOCATION` と
  `LIGHT` はそう書いた）。
- ⚠️ **そして、この1本の出来事は「同じ位置で起きる」ことである。** §15 `Spatial`——
  「**The two turns occupy the same frame geometry** — **the second page turns where the first one
  did.**」、§16 `PREFER`——「the turning page at the frame's centre **in both halves**, so that
  **the second turn lands where the first one landed.**」
  **ゆえにこの1枚は、二度のめくりが同じ構図の中に並んで見えるように組む。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **この1本の危険は、この作品で最も「構図の側」に寄っている。** 動画の仕様 §20——
  「**A cut may be inserted**」／「**The overlap may be lost** — if the second turn waits for the
  first, the shot is `s08` at half length with nothing to fill it.」／「**The pages may be read**;
  **the work does not read what it turns.**」／「**The two places may be distinguished** by light
  or prop.」／「**A face may be placed** at either desk.」／「**The turning page may be rendered
  stiff**, losing the one moment in this work where paper is in the air.」
  ⛔ **画像の側では、この段落がそのうち5つを止める**——**切る手段・区別する手段・読む手段・
  顔・硬い紙。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。** ⚠️ **要求を節に割れば5節であり、この段落はその5節を
  すべて文字として持つ。**
- ⚠️ **`no stack of paper` が尾に在る**——⚠️ **この1本の画面に束は無い。**
  **禁じる必要の無い1本ではあるが、尾はこの作品の共有の枠である**——**ゆえに1語も変えずに置く。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s15.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では6点である**——二人ぶんの `identity` と `negatives`
  （`長田美穂.identity`／`長田美穂.negatives`／`斎藤悦子.identity`／`斎藤悦子.negatives`）に、
  `名札` と `名札.appearance` が付く。⚠️ **これが正しい形である**——**二人が立つ1本は、
  二人ぶんの同一性を要する**（§3 は二人それぞれに `Reference: the frozen setting sheet` を持つ）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⚠️ **凍結した二枚の道を、ここに実測で固定する。** この1本が `identity` として添付する一枚は
  `distill-essence-engine/examples/habits/character/サブ/09_長田美穂/ChatGPT Image 2026年9月21日 00_48_28.png`
  と
  `distill-essence-engine/examples/habits/character/サブ/19_斎藤悦子/ChatGPT Image 2026年9月21日 01_08_33.png`
  である（実測 2026-09-28、`ls` で確認——`サブ/09_長田美穂/` と `サブ/19_斎藤悦子/` の中身は、
  それぞれこの PNG と `prompt.md` の2つだけである）。
  ⚠️ **この二つの道は、動画の仕様 §6 の2行と一致する。**
  ⛔ **`斎藤悦子` のフォルダは `19_` である**——`11_` ではない（`11_` は `木村智美` である）。
  ⚠️ **同じ形の誤りが、この仕様の §3 の2行に在った**（下の1行を見よ）。
- ⚠️ **動画の仕様 §3 の `Reference:` の2行は、道もファイル名も誤っていた**——§6 とは別の人物の
  フォルダを指していた。⚠️ **この稿を書いている時点で、著者の側が直している**（`s11`〜`s15` の5本）。
  ⛔ **誤っていた名前をここに写さない**——**消えた名前を引用に残せば、直っていないように読める。**
  ⚠️ **画像の側が取る二枚は、上の2行だけである。**
- ⚠️ **食い違い2（記録の内側・裁定は著者のもの）。** ⛔ **同じ記録の隣り合う2欄が、
  「重なる／重ならない」で反対を言っている。**
  - `motion.quality`（記録 48行目）——「速い所作を二度。**一度目が終わる前に、二度目が始まる。**」
  - `motion.law`（記録 50行目）——「`luminous-anime` の運動である。**重ならない**——二つの所作は、
    **同じ位置で、順に起きる。**」
  ⚠️ **動画の仕様は、この語を3箇所で名指ししている**——§11「**the second overlapping the first**」／
  §12「**The event is the overlap.**」／§16 `MUST`「**The second turn begins before the first
  finishes.**」、そして §20 の2番目は「**The overlap may be lost.** if the second turn waits for
  the first, **the shot is `s08` at half length with nothing to fill it.**」と言う。
  ⛔ **つまり「重ならない」は、この1本の出来事そのものを消す語である。**
  **私は画像の側では、動画の仕様の側に立った**——**この1枚は、二度目が一度目の終わる前に
  始まった状態の、その終わりを写す。**
- ⚠️ **食い違い3（記録と画面）。** 記録の `reference_set` は**小道具 `名札` と `名札.appearance` を
  持つ**が、⚠️ **動画の仕様 §4 は「二つの場所を区別する物を置かない」と言い、§5 は
  「**No other object is in frame.**」と言う**（在るのは紙・めくられる頁・机の面である）。
  ⛔ **ゆえにこの1枚は、名札を描いていない。** **`place` は「現場の鍵」であって、
  「画面に在る物」ではない**（`ledger.yaml` の `locations` の註——六つの `place` を27本が巡る。
  ⚠️ **そして `ledger.yaml` は「この作品は、名札を机の上に置かない」と書く**——
  **名札は左袖に付く物である**）。
- ⚠️ **動画の仕様 §4 の註だけが、この1本では噛み合っていない。** §4 は
  「**`s15` と `s16` は、同じ現場を二度使う**（`s08` の8.218秒と `s16` の8.457秒が対である）」と
  書くが、⚠️ **それが名指す対は `s08` と `s16` であり、この1本（`s15`）ではない。**
  実測（2026-09-28、`shots/` の `duration`）——`s08` は `8.218s`、`s16` は `8.457s`、
  `s15` は `4.867s` である。⚠️ **記録の `aim` は、この1本の相手を `s08` の 8.218秒と書く**
  （「**`s08` の 8.218秒に対し、こちらは 4.867秒である。**」）。**§4 の註は `s16` の話を
  この仕様へ写したものであり、`s15` の相手は `s08` である。**
- ⚠️ **記録の `attached` の註は、まだ「この作品はまだ1本も生成していない」と言う。**
  ⛔ **だが、いまの状態はそうではない**（実測 2026-09-28——`media/` に動画3本、`takes/` に3本、
  その3本は `s01`・`s02`・`s03` である）。**この1本は、その3本に入っていない。**
- ⛔ **この稿の文字列は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
