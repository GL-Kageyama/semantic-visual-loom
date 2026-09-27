# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十のショット「手が止まり、顔が起きる——呼ばれて」（開示 / motion / 9.814s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、`verse-2` の2本目である**（動画の仕様 §19——`Segment ID: verse-2-2`）。
⚠️ **この1本が、この作品で最初に顔を置く場所である。** 記録の頭は
「✅ **この1本が、この作品で最初に顔を置く場所である。**（`s02`〜`s04` は顔の**部分**である。
**部分ではなく、顔が起きるのは、ここが最初である。**）」と書き、`aim` は
「**この作品で最初の「顔」を置けるか。** 世界の規則が許す唯一の入口——**呼ばれて、振り向く**——
を、この1行が持っている。」と言う。
⚠️ **ゆえにこの1本だけが、顔を持てる。** 世界の規則は「**顔は、呼ばれた後にだけ置かれる。**」
（`bible.constants.顔`）——**この二行だけが、その「呼ばれる」を歌の中に持っている**
（`l10`「**いちばん古い一枚が、いちばん下にある。**」＋ `l11`「**違う読みで呼ばれて、振り向く。**」）。
⛔ **呼び声は、画面に置かない。** 動画の仕様 §16 `MUST NOT`——
「**The caller is never shown, and the frame does not turn toward them.**」
「**No voice is heard.** ⚠️ **Not as dialogue, not as a sound effect, not as a muffled call from off.**
The name is called and **the audience is on the wrong side of it.**」
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——`unit.after` は
「**手が止まり、顔が起きる。**——この作品で、最初に置かれる顔である。」
⚠️ **この1本は `ledger.disclosure` の変化点である**——
`宛名票の一行.いちばん古い一枚` が `unknown` から `present` へ動く（台帳の3点のうちの1つ）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s10.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a face that has just been called.** **The light, not the
    figure, is the subject** — and here the light is a tube in a school room, so the turn brings the
    face out of its own shadow and into the same flat light as the box.」
    ——**動画の側が先に、この様式を「呼ばれたばかりの顔へ翻訳した」と書いている。**
    画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s10.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/ChatGPT Image 2026年9月20日 03_29_35.png`
  （**キャラクター設定画**）と `.../ChatGPT Image 2026年9月20日 03_49_14.png`（**表情シート**）
  ——**凍結した二枚。** `ledger.yaml` の `暮林蒼.identity` が指す先であり、動画の仕様 §6 も同じ先を指す。
  ⚠️ **表情シートを添付する意味が、この作品で最初に要る1本である**（動画の仕様 §3）
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s10` §6——「**この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が「起きて止まった顔」を写すのは、そのためである**
  ——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  **手が先で顔が後である順序は、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。**
- 記録: `shots/habits-mv-s10.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` には `[名前: …]` の註を書く**（`s07`〜`s09` と逆である）——**この1本には、
置かれる人が居る。** ⚠️ **ただし註は「名指す」だけで、外見を書き起こさない。** 理由は下の節に書く。

- `SCENE`: the second of the second verse — a hand presses the oldest slip at the bottom of the stack, a name is called off the frame, and after the hand has finished the face rises; the caller is never shown
- `CHARACTERS`: `[暮林蒼: **the frozen setting sheet holds his face** — the name is here only so the right sheet is taken, and no appearance is re-derived in words]` — the hand at the oldest slip and, above it, the work's first face; the turn happens in the hair and the neck, the shoulders move very little, and the eyes are not turned to the lens
- `SUBJECT`: the work's first face rising above a cardboard box of four stacked address slips, with one hand resting on the oldest slip at the bottom
- `ACTION`: the hand has come down on the oldest slip and finished; a beat with nothing moving in the frame; then a small turn — the hair taking the light on one side and moving before the face — and the face is up and still, looking up from the box; **nothing is lifted from the stack**
- `LOCATION`: the side of a box of address slips in a school room, in the middle of a working day, 2026 — the box in the lower part of the frame and the face entering above it; **the direction the call came from is outside the frame and is never shown**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera on the box and on the face alike, bloom on the pale surfaces, deep cyan in everything the box shadows, and the hair taking the light on one side only so that **the turn is visible in the hair before the face**; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the skin of one face — the only new thing in a palette of paper, board and cloth, and the only warm thing in the frame

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the second of the second verse of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of the work's first face rising above a cardboard box of four stacked address slips, with one hand resting on the oldest slip at the bottom, in the middle of a working day, with the skin of that one face as the only new thing in a palette of paper, board and cloth. The hand came down on the oldest slip and finished; then a beat in which nothing in the frame moved; then the turn — the hair taking the light on one side only, and moving before the face — and the face is up and still, looking up from the box and not into the lens, with the turn happening in the hair and the neck and the shoulders moving very little. Nothing was lifted from the stack: the hand is still on the oldest slip, the four stay where they are, their edges lifted with dust settled into the lift, and the characters on them are present on screen and not readable, drawn as the three different marks of cut print and of ballpoint and of pencil, none of them legible. The caller is not in the frame and the frame does not turn toward them: there is no second figure anywhere in it, no one rendered in the direction the voice came from, no mouth opening and no speaking, and the voice is only on the side of the one who is called. The box sits in the lower part of the frame and the face enters above it; the face is not smiled, not startled and not widened — a person looking up from a box — and it carries no reaction to what has been said. The light is one fluorescent tube above and behind the camera, the same flat light on the box and on the face, and the turn brings the face out of its own shadow and into it; bloom on the pale surfaces, and everything the box shadows gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. Skin is the only new thing in the palette, and the hair holds the light on one side of it. Layered atmospheric depth from near to far, dust suspended and individually rendered over the box and still moving after the face has stopped, and low visual density — one focal point, the turn, with the box and the hand going out of the frame's attention as the face arrives. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at the height of the box and the face above it, the same placement as the shot before it, unmoving, and it does not follow the face up. One scene, one staging; the same box, the same tube and the same face wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no caller in the frame, no second figure, no person at the source of the call, no one rendered in the direction of the call, no mouth opening, no speaking, no speaking mouth, no voice, no muffled call from off, no look into the camera, no eye contact with the lens, no smile, no startle, no widened eyes, no lifted brow, no tears, no fear, no exaggerated expression, no performance, no full turn of the body, no turn of the torso, no swivel, no overshoot, no legible text on any surface, no legible name text, no readable characters on any prop, no legible characters on the slips, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no lifting from the stack, no slip taken, no slip handed to anyone, no second hand, no third hand, no reading, no insert of the writing, no magnified detail of the characters, no rack focus onto a slip, no push-in on the face, no pan toward the caller, no light change, no second object on the desk, no mug, no pen cup, no terminal, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered rather than a flat gradient」「Volumetric god rays — visible shafts of light
  travelling through air」「Anamorphic lens flare and bloom around the light source」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon, the light source inside the frame or
  just outside its edge; the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**箱と、その上に起きる顔しか映さない**——
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s10` §2 `Visual Language`——
  「**Luminous realist anime, translated into a face that has just been called.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**起きた顔が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その「光」が振り向きを現す**（`s10` §2——「**here the light is a tube in a school
  room, so the turn brings the face out of its own shadow**」）。**光は、順序を読ませる道具である。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ 呼んだ者を、この1枚にも置かない

- **この1本は「呼ばれる」を内容に持つ。** ⚠️ **だからこそ、呼んだ者は画面に居ない。**
  動画の仕様 §16 `MUST NOT` は「**The caller is never shown, and the frame does not turn toward them.**」
  と定め、§3 `nobody` は「⚠️ **呼んだ者は、画面に居ない。** **この1本に、二番目の人物は置かない。**」と言い、
  §4 は「⚠️ **呼んだ者が居るはずの方向は、画面の外である。** **そこを映さない** —
  **映せば、この1本は「呼ばれた」ではなく「呼んだ」になる。**」と添える。
- ⚠️ **カメラも、そちらを見ない。** 動画の仕様 §10——「**The camera does not look for the source of
  the call** — **there is no source in this scene, and looking for one would make it a shot about the
  caller.**」⚠️ **ゆえに `Negative` に `no caller in the frame, no second figure, no person at the
  source of the call, no one rendered in the direction of the call, no pan toward the caller` を置く。**
  動画の仕様 §20 の1番目——「**The caller may be shown.** ⚠️ **The first risk of this shot**: a generator
  given a turn will supply a second person to turn toward. **A caller in the frame makes this a shot
  about them.**」
- ⚠️ **音も置かない。** `s10` §20 の2番目——「**A voice may be produced.** ⚠️ **`no calling voice as a
  sound effect` sits in the slot this route reads as prose** — and a call is exactly what a generator
  will add to a turn.」⚠️ **ゆえに `Negative` に `no voice, no muffled call from off, no speaking,
  no mouth opening` を置く。** ⚠️ **`no calling voice as a sound effect` は既に床の13節に在る**
  ——**この段落は、その床が届かない「口」と「声」を塞ぐ。**

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s10` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render**」と、同じ一覧の末尾の「**no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚は、この作品で最初に顔を写す1枚である。** ゆえに `no photographic faces` は
  **この1枚でいちばん効く行である**——**凍結した二枚はアニメの絵であり、実写ではない。**
  ⚠️ **この1枚の顔が、以後のすべての顔の基準になる**（動画の仕様 §3 `Continuity Requirements`——
  「⚠️ **この1本の顔が、以後の顔（`s26`・`s27` を含む）の基準である。**」）——**外れれば、1枚で終わらない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、この顔が実写になる。**

## ⚠️ 名前の註は書くが、外見は書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s07`〜`s09` は書かない。**人が置かれないからである**）。
- ⛔ **だが、外見を書き起こさない。** 動画の仕様 §3——
  「**外見の記述は出典に一行も無い**（方針 §5a）。**凍結した二枚が外見である。**」
  ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな顔か」を教えることではない。**
  この1本では**その仕事を、添付された凍結の二枚（設定画＋表情シート）が負う**——
  **ゆえに註は名指すだけである。** ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**
  ——**黙ってやらず、ここに書く。** `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `identity` を添付する側である——この1枚が、その一枚である

- ⛔ **この1本は `identity` を添付する。** 動画の仕様 §6——「**この1本は `identity` を添付する** —
  **この作品で最初に顔を置く1本である。**」
- ⚠️ **ゆえに、この1枚は「人のかたちの一枚」そのものである。**
  **この1枚が外れれば、以後の顔（`s26`・`s27` を含む）が同じ人物でなくなる。**
  ⛔ **この1枚の外れは、1枚で終わらない。**
- ⚠️ **表情シートも一緒に渡る。** 動画の仕様 §3——「⚠️ **表情シートを添付する意味が、
  この作品で最初に要る1本である。**」——**この1枚は、二枚一組で凍結されている**
  （`ledger.yaml` の `暮林蒼.identity`——「**二枚を一組で凍結する。**」）。

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s10` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**呼んだ者**と**演じた顔**と**読ませた字**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が「演じること」にある。** `s10` §16 `MUST NOT`——
  「**The face is not smiled, not startled, not widened.** ⚠️ **A reaction would make this a
  performance**, and the shot is about a person looking up.」そして §20 の3番目——
  「**The face may be given a reaction** — a startle, a smile, or widened eyes. **The shot is a person
  looking up.**」**ゆえに `Negative` に `no smile, no startle, no widened eyes, no lifted brow,
  no tears, no fear, no exaggerated expression, no performance` を置く。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——**床は3節**であり、**この作品は `no calling voice as a sound effect` と
  `no face before the name is called` を足して5行にする**）。**ゆえにこの段落は、動画の §18 の写しではない**
  ——**同じ床を、効く場所へ置いたものである。**
  ⚠️ **この1本では `no face before the name is called` が、いちばん近い行である**——
  **この1本の顔は、呼ばれた後にだけ置かれる。****床と内容が、ここで初めて同じ方向を向く。**

- ⛔ **そして、この段落は共有の尾から1節を落としている**——`no stack of paper` である。
  ⛔ **この1本の主題は、紙が重なった山そのものである**（この1本は、四枚がそこに留まることを写す）。
  **尾は27本で共有されているが、その1節だけは、重なりを主題に持つ1本では主題を禁じてしまう。**
  ⚠️ **尾の目的は「机の上に二つ目の物を置かない」であって、「紙を描かない」ではない**——
  **この1本では、前者は `no second object on the desk, no mug, no pen cup, no terminal` が負う。**
  **ゆえに落としたのは1節であり、他の36節は一字も動かしていない。**
  ⚠️ **同じ衝突は、この作品に5本ある**——`s09`・`s11`・`s21`・`s24`・`s25`。

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s10.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「**手が止まり、顔が起きる。**——この作品で、最初に置かれる顔である。」
- `reference_set` は**この1本では5点**である——`暮林蒼.identity`・`暮林蒼.negatives`・
  `宛名票の一行`・`宛名票`・`侘田すみれ.negatives`。
  ⚠️ **この1本は `identity` を含む**——動画の仕様 §6——「**この1本は `identity` を添付する** —
  **この作品で最初に顔を置く1本である。**」
- ⚠️ **`侘田すみれ` は、禁制の側だけが渡る。** 動画の仕様 §6——「**この1本には添付しない。**
  参照集合が挙げているのは `侘田すみれ.negatives` だけである——**ゆえに渡るのは禁制の側だけである。**」
  ⛔ **彼女は画面に居ない**——記録の頭は「**画面には居ない。**」と書き、台帳の註は
  「`s10`（**振り向く相手として名前だけ**）」と書く。**ゆえに `CHARACTERS` にも、
  2段落にも、彼女の名前は1つも置かない。**
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
