# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第二十四のショット「二つの顔が、順に起きる」（開示 / motion / 5.026s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、`final-chorus` の6本目である**（動画の仕様 §19——`Segment ID: final-chorus-6`）。
⚠️ **この1本で、この作品は二度目に顔を置く。** 動画の仕様の頭（§1 の前）は
「**この作品で顔が置かれるのは、`s10`（暮林蒼）と `s24`・`s25`（四人）だけである**
——**合計五人である。** 残る二十二本は、手だけである。」と書く。
⚠️ **この稿は、その数を写さない**——**3本と22本を足しても、27本にならない（25本である）。**
**足りない2本がどれかは、この稿では決めない**（裁定は著者のもの）。**この1枚が拠り所にするのは、
数ではなく「この1本が顔を置く側である」という一事である。**
⚠️ **この1本の変化は「順に」である。** `unit.after` は「**二つの顔が、起きている。**」——
⛔ **但し、同時ではない。** 動画の仕様 §16 `MUST NOT`——「**The two faces do not rise at the same time.**
⚠️ **This is the shot's whole construction** — **simultaneity would make the two people one gesture.**」
⚠️ **そして二つの場所は、繋がらない**——§16 は「**No cut and no camera crossing between the two places.**」を持つ。
⛔ **暮林蒼は、この1枚にも、この1本の参照集合にも入らない。** 動画の仕様 §15——
「⚠️ **暮林蒼 is not in this shot and is not in its reference set** — **the person who carries the
transferred habit and the person it came from are placed in `s10` and `s24`, and never side by side.**」
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——**二つの顔が、起きて止まっている。**
**手が先で顔が後である順序は、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
⚠️ **この1本は `ledger.disclosure` の変化点ではない。** 台帳の3点は `s10`・`s17`・`s18` であり、
動画の仕様 §15 がその意味を書いている——「**This shot's `disclosure_state` is already the post-`s18`
state** — **the faces are not a new disclosure of the world; they are the work spending what it has.**」
⛔ **ゆえにこの1枚は、「明かす」1枚ではない。****使う1枚である。**
⚠️ **サビの14本には、この1本は入らない。** 台帳の `locations.名札` の註は
「**サビの14本は、すべてこの現場である**」と書き、その同じ註が
「⚠️ **`s24`・`s25` は、ここではない**」と明記する——**数え直して16本から14本へ直した側である。**
**ゆえにこの1枚の現場は `束` である**（台帳 `locations.束`——**この1本と `s25` が、その最後の2本である**）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s24.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into two faces coming up over two desks.** **The light, not the
    figure, is the subject** — and here the same tube that has lit every hand in this work now lights two
    faces, **so the faces arrive in the light the hands were already in.**」
    ——**動画の側が先に、この様式を「二つの顔へ翻訳した」と書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s24.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/16_秋山誠/ChatGPT Image 2026年9月18日 05_17_49.png`
  と `.../サブ/24_前田亮太/ChatGPT Image 2026年9月20日 19_58_25.png`
  （**人のかたちの一枚ずつ**。`ledger.yaml` の `秋山誠.identity` と `前田亮太.identity` が指す先であり、
  動画の仕様 §6 も同じ先を指す）
  ⛔ **`暮林蒼` の一枚は、渡らない。** 動画の仕様 §6——
  「⚠️ ⚠️ **暮林蒼は、この1本の参照集合に入らない**——**二人は `s10` と `s24` に分かれて立ち、隣り合わない**」
  ＋ 同じ作品の既存の生成物（`media/` の動画）
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s24` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が「起きて止まった二つの顔」を写すのは、そのためである**
  ——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  **二度目が一度目と同時でないことは、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。** ⚠️ **この1本の2段落には、日本語の字が1つも無い**（下の節に理由を書く）。
- 記録: `shots/habits-mv-s24.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` には `[名前: …]` の註を書く**（`s07`〜`s09` と逆である）——**この1本には、
置かれる人が二人いる。** ⚠️ **註は2つになる。この作品で2つ置くのは、この1本が初めてである。**
⛔ **どちらの註も、名指すだけで、外見を書き起こさない。** 理由は下の節に書く。

- `SCENE`: the sixth of the final chorus — two hands press paper in two places and two faces rise, one after the other, inside one frame, and the frame does not cut
- `CHARACTERS`: `[秋山誠: **the frozen setting sheet holds his face** — the name is here only so the right sheet is taken, and no appearance is re-derived in words]` `[前田亮太: **the frozen setting sheet holds his face** — the name is here only so the right sheet is taken, and no appearance is re-derived in words]` — **two hands and, above them, two faces, in two places**; the turns happen in the hair and the neck, the shoulders move very little, and neither face is turned to the lens
- `SUBJECT`: two faces rising above two bundles of paper, one after the other, in one composition
- `ACTION`: two presses and two turns — each hand comes down flat on its own bundle in one fast even movement and stops, and **then** that face rises: the hair takes the light on one side and moves before the face, the neck carries the turn, and the face is up and still; **the second turn comes after the first and never with it**, and **nothing is lifted from either bundle**
- `LOCATION`: two desks with a bundle of paper on each, in two school rooms, in the middle of a working day, 2026, held in one frame — **the same composition twice**, the bundle low in the frame and the face entering above it; ⛔ **no wall, no window, no clock, no weather and no prop that would tell the two places apart**
- `LIGHT`: the room's constant state, and the same light in both halves — the flat light of a fluorescent tube above and behind the camera falling across both desks, bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the desk edges shadow gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the skin of two faces — **the only new value the palette has taken on since the work's first face**, and the only warm thing in either half

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the sixth of the final chorus of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of two faces rising above two bundles of paper on two desks, in the middle of a working day, 2026, with the skin of those two faces as the only new value the palette has taken on since the work's first face. One composition holds both places and it does not cut: each half is a bundle lying low in the frame with a hand flat on it and, above it, a face coming up, and the two halves are the same shape at the same small amplitude. In each half the hand comes down flat on the bundle in one fast even movement and stops, and then the turn happens: the hair takes the light on one side only and moves before the face, the neck carries the turn, the shoulders move very little, and the face is up and still, looking up from the paper and not into the lens — and the second turn comes after the first and never at the same moment as it. Neither face is smiled, neither is startled, neither widens the eyes and neither carries a reaction to anything: two people looking up in two rooms, one after the other, and nothing in either half explains why. The bundles are paper — slips, registers and tags, their edges unsquared — and they do not move: neither one is lifted, turned or carried, nothing comes out of either of them, and the characters on them are present on screen and not readable, drawn as the different marks of cut print and of ballpoint and of pencil, none of them legible. Nothing in the frame tells the two places apart: there is no wall, no window, no clock, no difference of weather and no prop that belongs to one half and not the other, so that the only difference between the halves is how much deep cyan the shadows hold. The light is one fluorescent tube above and behind the camera, falling flat and even across both desks; the paper is the brightest thing in the frame, the tube is the only light, and everything the desk edges shadow has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. Layered atmospheric depth from near to far, dust suspended and individually rendered where the tube catches it, and it keeps moving after both faces have stopped; low visual density — one focal point, the rising face, twice, with the desk going out of the frame's attention as each face arrives. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens close at the desk and the face above it, the same placement in both halves, unmoving, and it does not follow either face up. One scene, one staging; the same desks, the same tube and the same two turns wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no cut, no dissolve, no wipe, no transition between the two places, no second camera angle, no reframe between the two presses, no pan, no tilt, no push-in, no pull-back, no cut between the two turns, no face rising at the same moment as the other face, no simultaneous turn, no two faces moving at once, no caller in the frame, no second figure, no person at the source of the call, no one rendered in the direction of the call, no mouth opening, no speaking, no voice, no muffled call from off, no look into the camera, no eye contact with the lens, no smile, no startle, no widened eyes, no lifted brow, no tears, no fear, no exaggerated expression, no performance, no full turn of the body, no turn of the torso, no swivel, no overshoot, no third hand, no third place, no figure shared across the two places, no person added to either half, no sheet coming out of either bundle, no lifting of either bundle, no turning of either bundle, no tearing of the bundle, no reading, no insert of the writing, no magnified detail of the characters, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no light change, no light change at either turn, no second object on the desk, no mug, no pen cup, no terminal, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies」「Volumetric god rays」
  「Anamorphic lens flare」「**a saturated dusk palette: magenta and gold against deep cyan shadow**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**二つの机と、その上の束と、その上に起きる二つの顔しか
  映さない**——**空が入る余地は、構図の側に無い。****部屋も要らない**（台帳 `locations.束`——
  「机の上。**束は、動かされない。**」）。
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s24` §2 `Visual Language`——
  「**Luminous realist anime, translated into two faces coming up over two desks.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**二つの顔が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その「光」が顔を受け止める**（`s24` §2——
  「**the faces arrive in the light the hands were already in**」）。**光は、順序を読ませる道具である。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**（`s01` の同じ節を見よ。）

## ⚠️ 二つの顔を、同時に起きしてはならない

- ⛔ **これがこの1本の一番目の危険である。** 動画の仕様 §20 の1番目——
  「**The faces may rise together.** ⚠️ **The first risk of this shot**: two hands in one frame invite a
  single simultaneous reveal, and **the shot is built on hand-face-hand-face.**」
  §16 `MUST NOT` は「**The two faces do not rise at the same time.** ⚠️ **This is the shot's whole
  construction** — **simultaneity would make the two people one gesture.**」と定める。
- ⚠️ **画像の側では、これが二重に効く。** **1枚の絵は、二つの顔が同時に起きている絵と、
  順に起きたあとの絵を区別しない。** ゆえに `Prompt` は
  「**the second turn comes after the first and never at the same moment as it**」と書き、
  `Negative` は `no face rising at the same moment as the other face, no simultaneous turn,
  no two faces moving at once` を持つ——**順序は、動画の側の変化である**（上の `## 渡す先`）。
- ⚠️ **この1本の順序は、作品の順序そのものである。** `bible.world.rules`——
  「**手が先にあり、顔が後に来る。順序は入れ替えない。顔は、呼ばれた後にだけ置かれる。**」
  ⚠️ **ゆえに `Prompt` は「手が止まり、そのあと顔が起きる」を、二度、順に書く**——
  **この1枚が写す静止の側でも、その順序は消えない。**

## ⚠️ 二つの場所を、光で区別してはならない

- ⚠️ **この1本は二つの場所を1枚に置く。** 動画の仕様 §13 `Lighting Events`——
  「**None, in either place.** ⚠️ **The faces come into the light the hands were already in** —
  **a change of light would make the arrival an announcement.**」
  §4 `Environment Elements` は「**二つの場所を区別する物を置かない。**」と添える。
- ⛔ **ゆえにこの1枚は、二度目の側にだけ窓を置かない。****机以外に、二つを分ける物は無い。**
  動画の仕様 §20 の7番目——「**The shot may be lit for the faces** — a change of light would make the
  arrival an announcement.」**ゆえに `Negative` に `no light change, no light change at either turn` を置く。**
- ⚠️ **差は、順序だけである。** ⚠️ **この作品の物理は、二つの場所を一つに見せる側にある**——
  `s08` の同じ節（「**同じ位置で二度目を迎える**」）と、この1本の
  「**the same two turns**」は、**同じ規律である。**

## ⚠️ 暮林蒼を、この1枚に置かない

- ⛔ **この作品は、癖を移した者と、移された者を隣り合わせない。** 台帳 `前田亮太` の註——
  「⚠️ **彼の癖を、暮林蒼が持っている**——**移った癖を持つ者が、移した相手を名指す**。
  この作品では、**その二人が `s10` と `s24` に分かれて立つ。** **隣り合わせない。**」
  動画の仕様 §20 の4番目は、**その危険を名指しで書いている**——
  「**暮林蒼 may be added** if a generator blends the two people who share the habit — ⚠️ **the ledger
  keeps them in `s10` and `s24` precisely so that they are never adjacent.**」
- ⚠️ **ゆえに `Negative` に `no third hand, no third place, no figure shared across the two places,
  no person added to either half` を置く。** ⛔ **この1本は、彼を名で禁じない**——
  **文字列に日本語の字を置けば、置かれる側へ回る**（`s01` の `## 渡す先` と同じ理由である）。
  **名指しではなく、構図で外す**——**二つの場所、二つの顔、三つ目は無い。**
  ⚠️ **彼が `s10` に立っていることは、この1枚の外側の事実である**——**この1枚は、それを写さない。**

## ⚠️ 名前の註は書くが、外見は書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が二人いる**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**。
  `s07`〜`s09` も書かない。**手だけで、人が置かれないからである**）。
- ⛔ **だが、外見を書き起こさない。** 動画の仕様 §3——
  「**外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。**」
  ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな顔か」を教えることではない。**
  **その仕事を、渡された二枚が負う**——**ゆえに註は名指すだけである。**
- ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**顔は凍結した設定画のものである**」だけである——**註の形は、この作品で1つに決まっている。**
  ⚠️ **註が作品の持たないことを持てば、註そのものが新しい事実になる**（方針 §5a——
  `ledger.yaml` の `characters` の註「**外見の記述は出典に一行も無い。凍結した二枚が外見である。**」）。
- ⛔ **そして、ここが決定的である**——**`CHARACTERS` の欄は註ではない。生成器へ渡る文字列である。**
  **そこに書かれたものは、描かれる。** ⚠️ **動画の仕様が年齢や職業を書くとき、その宛先は人間である**
  ——`s06` の `Reference:` の行は「**出典の語は「路線バス運転士・52歳」である**」と引き、
  `s07` の同じ行は「**スーパー惣菜部門・45歳**」を引く。**あれは、出典についての日本語の散文であり、
  読み手は人間である。**（⚠️ **数を数えない**——**数え方は語の切り方で動き、動く数は要らない。
  要るのは、宛先である。**）
  ⛔ **同じ語をこの欄へ置けば、宛先が変わる**——**英語の入力として生成器に届き、絵になる。**
  **ゆえに註には、名と、凍結した設定画へのポインタだけを置く。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `identity` を添付する側である——この1枚が、その二枚である

- ⛔ **この1本は `identity` を2点とも添付する。** 動画の仕様 §6——
  「**この1本は `identity` を添付する** — **この作品で二人目に顔を置く1本である。**」
  `shots/habits-mv-s24.yaml` の `reference_set` も、同じ2点を持つ（`秋山誠.identity`・`前田亮太.identity`）。
- ⚠️ **ゆえに、この1枚は「人のかたちの二枚」そのものである。** 動画の仕様 §15——
  「**Must preserve** — both people from their frozen sheets, **and the face standard set in `s10`.**」
  ⛔ **この1枚の外れは、1枚で終わらない**——**顔を置くショットは `s10`・`s24`・`s25` の3本しかなく、
  この1本で外れれば、以後の二本が同じ人物でなくなる。**
- ⚠️ **そして、この1本は「二枚を一組で凍結する」側ではない。** `碓氷千夏` と `暮林蒼` は
  **設定画＋表情シートの二枚一組**である（台帳の `identity`）。⚠️ **サブの四人は一枚である**——
  台帳の `秋山誠.identity`・`前田亮太.identity` は、どちらも
  「——**人のかたちの一枚**（`character-sheet × luminous-anime`）」と書く。
  **ゆえにこの1枚は、渡された一枚ずつの側に立つ。**

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s24` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚は、この作品で二度目に顔を写す1枚である。** ゆえに `no photographic faces` は
  **この1枚でも強く効く**——**凍結した一枚はアニメの絵であり、実写ではない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、二つの顔が実写になる。**（`s01` の同じ節を見よ。）

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s24` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**切れ目**と**同時に起きる二つの顔**と**三つ目の場所**——を禁じているのは、
  **この段落である。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**
  ——**同じ床を、効く場所へ置いたものである。**
  ⚠️ **この1本では `no face before the name is called` が、いちばん近い行である**——
  **この1本の二つの顔は、どちらも「呼ばれた後にだけ」置かれる**（`bible.world.rules`）。
  **床と内容が、ここでも同じ方向を向く。**

- ⛔ **そして、この段落は共有の尾から1節を落としている**——`no stack of paper` である。
  ⛔ **この1本の主題は、二つの机の上の二つの束そのものである**（この稿の `Prompt`——「The bundles are paper」）。
  **尾は27本で共有されているが、その1節だけは、束を主題に持つ1本では主題を禁じてしまう。**
  ⚠️ **尾の目的は「机の上に二つ目の物を置かない」であって、「紙を描かない」ではない**——
  **この1本では、前者は `no second object on the desk, no mug, no pen cup, no terminal` が負う。**
  **ゆえに落としたのは1節であり、他の36節は一字も動かしていない。**
  ⚠️ **この1節を落としているのは、この作品で6本である**（実測 2026-09-28——**27本の画像仕様の
  `Negative` の段落を走査して数えた**）——`s09`・`s10`・`s11`・`s21`・`s24`・`s25`。
  **落とす形が同じでも、理由は1本ずつ違う**——**この1本の理由は、束が主題であることである。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s24.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「**二つの顔が、起きている。**——この作品で、顔が最後に置かれる場所である。」
- `reference_set` は**この1本では6点**である——`秋山誠.identity`・`秋山誠.negatives`・
  `前田亮太.identity`・`前田亮太.negatives`・`束`・`束.appearance`。
  ⚠️ **この1本は `identity` を2点とも含む**（動画の仕様 §6）。**画像の側の `content` も同じ側に立つ。**
  ⛔ **それでも、参照集合に `暮林蒼` は1点も無い**——**隣り合わせないからである**（上の節）。
- ⚠️ **食い違い1（読み取り・裁定は著者のもの）。** `ledger.yaml` の `props.束.appearance` は
  「紙の束。**伝票・名簿・札。** 端が揃っていない。**一枚が、切り離される。**」と書くが、
  ⛔ **この1本の束からは、一枚も出ない。** 動画の仕様 §5——
  「⚠️ **この1本の束からは、一枚も出ない。** **`s11` と `s21` は一枚を出し、この1本は出さない。**
  **同じ物が、別のことをする。**」 ⚠️ **ゆえにこの1枚は、小道具の `appearance` の最後の一節を写さない**
  ——**そこは `s11`・`s21` の動作である。** `Prompt` は
  「**nothing comes out of either of them**」と書き、`Negative` は
  `no sheet coming out of either bundle, no lifting of either bundle, no turning of either bundle`
  を持つ。**「一枚が、切り離される。」は、この1本では起きない。**
  ⚠️ **そして、同じ動画の仕様の中で §4 と §5 が食い違っている。** §4 `Location` の末尾は
  「**束は机の上にあり、動かされない。一枚だけが、そこから出る。**」と書く——**§5 の一行と、
  同じ1本の中で逆向きである。** ⛔ **この稿は §5 を取る**——**§5 は、どの1本が一枚を出すかを
  名指しで数えている側である**（`s11`・`s21`）。**裁定は著者のもの。**
- ⚠️ **食い違い2（読み取り）。** `shots/habits-mv-s05.yaml` の頭は
  「⚠️ **この作品は、サビで顔を置かない。**」と書く。⛔ **この1本は `final-chorus` であり、
  顔を置く**——**字面の側では、その一行はこの1本に当てはまらない。**
  ⚠️ **辻褄は動画の仕様 §15 が合わせている**——「**the faces are not a new disclosure of the world;
  they are the work spending what it has.**」（この節は「明かす」を禁じているのであって、
  **「使う」を禁じてはいない**）。⚠️ **台帳の `locations.名札` の註も、この1本をサビの14本から外す**
  （「⚠️ **`s24`・`s25` は、ここではない**」）。**裁定は著者のものである。**
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
