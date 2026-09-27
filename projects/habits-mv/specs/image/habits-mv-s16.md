# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十六のショット「二つの手が同時に止まり、光だけが動く」（モンタージュ / motion / 8.457s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、この作品で唯一、二人ぶんの `identity` を添付する1枚である。**
`reference_set` は6点であり、そのうち2点が人のかたちの一枚である
（`根本湊.identity`・`関口浩一.identity`）。⚠️ **そして置かれるのは、二本の手だけである**
——記録の `motion.subject` は「根本湊の手と、関口浩一の手。」と言い、動画の仕様 §3 は
二つの節の `Appearance` にどちらも「**置くのは右手だけである。**⚠️ **顔は置かない。**」と書く。
⚠️ **二人ぶんの一枚が渡り、二本の手だけが置かれる**——**この非対称が、この1枚の設計である。**
⛔ **ゆえにこの1枚の `CHARACTERS` には、二つの註が並ぶ**（下の節に書く）。
⚠️ **註は二つでも、置かれる人は一人も居ない。**

⚠️ **この1本の変化は「同時」である。** 動画の仕様 §1——「**two hands in two places stop at the
same moment, and light is all that moves for the rest of the shot.** ⚠️ **The simultaneity is the
change**」。⚠️ **そして「同時」は、止まった1枚からは読み取れない**（下の節に書く）——
**ゆえにこの1枚は、止まったあとの状態だけを写し、変化は動画の側に残す。**
⚠️ **この8.457秒が、サビの中で最も長い**（サビ全体 20.744秒の 41%）。**そのうち 3.257秒が静止である**
（`beats` の `5.2-8.457s`）。⚠️ **これは `chorus-2`（`s12`–`s16`）で最も長い静止である**
（`s15` 1.767／`s13` 1.473／`s12` 1.273／`s14` 1.074）。⛔ **作品全体では最も長くない**——
**この8本がこれより長い**（`s27` 7.309／`s17` 4.963・4.069／`s04` 3.955／`s03` 3.900／
`s18` 3.856／`s10` 3.514／`s26` 3.500／`s23` 3.303。動画の仕様の頭が27本を並べて書いている）。
⚠️ **「最も長い」は、並べてから書く。**

⚠️ **この1本は、この作品で最後の日中の1本である**——動画の仕様 §15 `Temporal`——
「**This shot ends the daylight half of the work** — the next shot is the evening.」
⚠️ **そしてサビ2の最後の1本である**（動画の仕様 §19——`Segment ID: chorus-2-5`）。
**このあと曲はブリッジへ入り、現場は夕方へ移る。**

⚠️ **この1枚が写すのは、この1本が終わったあとの状態である。** `unit.after` は
「二つの手が止まり、**机の上には紙だけがある。**」——⚠️ **渡すのは開始のコマではない。**
⚠️ **動画の仕様 §8 の `MOVEMENT 4` は「**The paper lies under both hands**」と言う**——
**二本の手は、止まった場所に在り続ける。** **この1枚もそう描く。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s16.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into two hands at rest on two desks.** **The light, not the
    figure, is the subject** — and here it is the only thing moving, so the shot's art direction is
    the art direction of two still surfaces under one live tube.」
    ——**動画の側が先に、この様式を「二つの机の上の二本の手へ翻訳した」と書いている。**
    画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s16.yaml` ＋
  **既存の出力**——**凍結した二枚**——
  `distill-essence-engine/examples/habits/character/サブ/10_根本湊/ChatGPT Image 2026年9月20日 19_56_46.png`
  と `.../サブ/20_関口浩一/ChatGPT Image 2026年9月21日 01_11_22.png`（**人のかたちの一枚ずつ**。
  動画の仕様 §6 が指す先であり、`ledger.yaml` の `根本湊.identity`・`関口浩一.identity` も同じ先を指す）
  ＋ 同じ作品の既存の生成物（`media/` の動画）
- 添付する参照: **`specs/image/生成時参照イラスト/s16/` の2枚**——`根本湊_設定画.png`・`関口浩一_設定画.png`。
  ⚠️ **この2枚は、この作品の動画の側の同じ2枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s16/`。実測 2026-09-28、ハッシュが一致した）。
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
  **和が、そのまま下の7欄である**（`specmap.MODELS` の註と同じ7欄。
  `check.py --self-test` の `L22_FIVE`／`L22_FOUR` がこの2枚を例に持っている）。
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** 様式カードの雛形は
  `Not photorealistic, …` で終わるが、**この作品はそれを2段落目に置く**——**この作品は実写ではない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s16` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「止まった二本の手」を写すのは、そのためである**——**渡すのは、この1本が終わった
  あとの状態＝世界の側であって、開始のコマではない。** ⛔ **そして「同時に止まった」ことは、
  止まった1枚からは読み取れない**——**ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。**
- 記録: `shots/habits-mv-s16.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の註は、この1本では「手」の側である**——**顔が置かれないからである**（`s05`・`s06` と同じ形）。
⛔ **註に置くのは、人物の名と、凍結した一枚を指すことだけである。****外見は書き起こさない。**
⚠️ **この1本は、註を二つ持つ**——**この作品で唯一である**（置かれる手が、二人ぶん在るからである）。

- `SCENE`: the last step of the second chorus — two right hands, in two places, have finished pressing and are at rest on two sheets of paper in the same frame; the presses have stopped, and in the shot the stopping is simultaneous, which a still frame cannot carry
- `CHARACTERS`: `[根本湊: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` and `[関口浩一: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **the two hands and the two sheets are the whole figure in the frame**; **no face, no head, no chin, no hair, no shoulder above either cuff**, no arm past either cuff, and the two hands are two hands in two places and not one hand drawn twice
- `SUBJECT`: the two sheets of paper at rest under the two right hands, and the light crossing them
- `ACTION`: both presses finished — the pads came down flat on the paper and stayed, the sheets took the press and did not move, neither hand has lifted, turned a page or read anything, and neither hand has left the sheet; the stop is simultaneous, and no second movement follows it
- `LOCATION`: two desks in two school rooms in the middle of a working day, 2026 — **one frame holding both places**, the same composition twice with no cut and no border between them, the two places not distinguished by prop, by light or by time of day, and **nothing on either desk but the paper**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling even across both desks, bloom on the pale surfaces, **the paper the brightest thing in the frame and the same values twice**, and everything the desk edges shadow gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the cream of the two sheets and the two hands — the only warm things the tube finds, in a narrow, cold room, and the same accent twice

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the last step of the second chorus of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of two right hands at rest on two sheets of paper, on two desks in two school rooms in the middle of a working day. One frame holds both places: the same composition twice, with no cut, no split panel and no border between them — the two desks occupy the same frame geometry and the two presses have stopped at the same point in it. Each hand is a hand only — a right hand, the back of it, the knuckles, the nails cut short, the plain cuff of a shirt at the wrist — and no arm is in the frame past either cuff. The presses are finished: the pads came down flat on the paper and stayed, the sheets took the press and did not move, and neither hand has lifted, turned a page or read anything. No head enters either half of the frame, no shoulder, no standing figure behind either desk, and there is nothing on either desk but the paper: no mug, no pen cup, no terminal, no second sheet, no nameplate. The characters on the two sheets are present and not readable — the marks of cut print and of ballpoint and of pencil drawn as the different marks they are, none of them legible, and the two sheets are two sheets and not one sheet written twice. The light is one fluorescent tube above and behind the camera, falling flat and even across both desks and blooming on the pale surfaces; the paper is the brightest thing in the frame, the tube is the only light, the palette is the same twice, and everything the desk edges shadow has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. Layered atmospheric depth from near to far; dust suspended and individually rendered above both desks where the tube catches it, and in this frame the dust and the light's edge are the only things that are not still. Low visual density: one focal point, the two pressed sheets, with the frame given mostly to the two desk surfaces and the space between them. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at desk height looking slightly down, the two sheets at the same point in the frame, and the composition held for the whole take. One scene, one staging; the same two desks, the same tube and the same press wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no head, no chin, no hair, no shoulder above either cuff, no standing figure, no person at either desk, no second figure, no third hand, no portrait, no arm past either cuff, no cut, no dissolve, no split screen, no panel, no border between the two places, no seam between the two halves, no inset, no double exposure, no sequential stop, no stagger, no one hand stopping before the other, no second press, no lift, no turning of a page, no read, no light change between the two places, no pan between the two hands, no push-in on either sheet, no camera move toward either desk, no distinguishing of the two places by prop or by light or by time of day, no nameplate in the frame, no plate lying on a desk, no plate worn on a sleeve, no plastic plate, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no insert of the writing, no magnified detail of the characters, no rack focus onto a sheet, no eye in the frame, no finger tracking a line, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**二つの机と、その上の紙しか映さない**——
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s16` §2 `Visual Language`——
  「**Luminous realist anime, translated into two hands at rest on two desks.**」、
  「**two still surfaces under one live tube**」。**この1枚は、その訳文の側に立つ。**
  訳す前の側（空）を写せば、**二つの机の上の1本が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その「光」が唯一の運動である**（`s16` §2——「**here it is the only thing
  moving**」）。**光は、この1本では主役であると同時に、唯一の動き手である。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。** ⚠️ **隣の作品が同じ手を使っている**
  （`migenzo` の `no window, no time of day, no directional light`——同じ理由である）。

## ⚠️ 「同時」は、止まった1枚からは読み取れない——ゆえに変化は動画の側に残る

- **この1本の変化は、時間の側にしか無い。** 動画の仕様 §1——「**two hands in two places stop at
  the same moment**」、§7 `Peak`——「**Both stop at the same instant.** ⚠️ **The simultaneity is the
  shot: neither place can know about the other.**」
- ⛔ **一枚の絵は、二本の手が止まっていることを写せる。** **「同時に」止まったことは写せない**
  ——**同じ1枚の中で、先に止まった手と後から止まった手は、同じ絵になる。**
  ⚠️ **これは `s05` の「滑ることは、止まった1枚からは読み取れない」と同じ構造である**
  （`s05` の `## 渡す先`）。⛔ **ゆえに、この1枚は「止まったあと」だけを持ち、
  「同時」は動画の側に残す。**
- ⚠️ **だが、この1枚は二つの場所を1つの枠に入れなければならない。** 動画の仕様 §15 `Spatial`——
  「**The two places occupy the same frame geometry**」、§16 `MUST`——「**Two hands, in two places,
  stop at the same moment in one continuous frame.**」
  ⛔ **二つの場所を1つの枠に入れる手段は、ここでは「切らないこと」しかない。**
  **ゆえに `Negative` に `no cut, no dissolve, no split screen, no panel, no border between the two
  places, no seam between the two halves, no inset, no double exposure` を置く。**
- ⚠️ **危険は「順番」の側にも在る。** 動画の仕様 §20 の1番目——「**The stops may be sequential.**
  ⚠️ **The first risk of this shot**: the whole difference from `s08` is the simultaneity, and a
  generator given two hands will stagger them.」
  ⚠️ **この1枚は止まったあとを写すので、順番そのものは写せない**——**だが、二本の手が
  「同じ姿勢で、同じ高さで」止まっていることは写せる。**
  **ゆえに `Negative` に `no sequential stop, no stagger, no one hand stopping before the other` を置く。**
  ⚠️ **`s08` との差はここである**（`s16` の頭——「**`s08` が「同じ姿勢で止まる」、この1本は
  「同時に止まる」。** **前者は収束、後者は同時である。**」）。
- ⚠️ **動きを別のもので置き換えない。** 動画の仕様 §16 `MUST NOT`——「**Nothing replaces the
  movement** — no second press, no lift, no read.」
  **ゆえに `Negative` に `no second press, no lift, no turning of a page, no read` を置く。**

## ⚠️ `place` は `名札` だが、この1枚に名札は無い

- **この1本の `place` は `名札` である**（全巻を貫く小道具の現場）。**そして置かれる物は紙である。**
  動画の仕様 §4 `Environment Elements`——「机、その上の紙。**二度、同じ構成で。**」、
  §5 `OBJECTS`——「**紙** — 二度、二つの机の上に。**読めない。**」「**机の面** — 紙の下。」
  「**No other object is in frame.**」
  ⛔ **この画面に、名札は無い。**
- ⚠️ **この食い違いは、この作品では初めてではない。** `s13` の動画の仕様 §5 は
  「⚠️ **この1本に名札を置かない。** `place` は `名札` であるが、**この1本の物は紙である**」と
  明記している。**`place` は「曲の1行が立つ現場」の名であって、画面に置かれる物の名ではない。**
- ⛔ **ゆえに `Negative` に `no nameplate in the frame, no plate lying on a desk, no plate worn on a
  sleeve, no plastic plate` を置く。** ⚠️ **この一行が要るのは、`reference_set` が
  `名札.appearance`（＝「学校の指定の名札。**プラスチック。** 左袖に付く。**読めない。**」）を
  渡すからである**——**渡された語は、置かれる側へ回る。**
  ⚠️ **`名札` は「誰の手か」を問う現場の名であり、この1本はその問いを紙の側で受ける。**

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s16` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚は、手だけを写す1枚である。** ゆえに `no photographic faces` は
  **この1枚でも効く**——**凍結した二枚はアニメの絵であり、実写ではない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、二つの机の上の1枚が実写になる。**

## ⚠️ 註は「どの手か」だけを教える——二人ぶん書くが、外見は書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**）。
  ⛔ **だが、置かれるのは手だけである**——**註は「手」の側に付き、二つ並ぶ。**
- ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**手は凍結した設定画のものである**」だけである——**註の形は、この作品で1つに決まっている**
  （`s05`・`s06` と同じ形）。⚠️ **この1本は、それを二人ぶん繰り返すだけである。**
- ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな手か」を教えることではない。**
  動画の仕様 §3 は二人の節にどちらも「**外見の記述は出典に一行も無い**（方針 §5a）。
  **この一枚が外見である。**」と書く。
- ⛔ **註に、二人の `prompt.md` の出典の欄（どちらも `21` 行目）を持ち込まない。** そこには
  「**男19・専門学校生・居酒屋・豊島区。居酒屋26席、店長と学生6名。**」
  「**男42・在宅勤務の多い会社員・港区。全社4,200名、自部署は19名。**」がある——
  ⚠️ **それは出典の要約であって、註の仕事ではない。****註は名指すだけである。**
- ⚠️ **理由は「禁じられているから」ではない。宛先が違うからである。** この欄の値は
  **生成器へ渡る文字列**である——**同じ語が、動画の仕様の中では、出典について人間が読む
  日本語の散文であり、この欄では、モデルが読む英語の入力である。**
  ⛔ **中身が同じでも、宛先が違えば、起きることは違う。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `identity` を添付する側である——この1枚が、その二枚である

- ⛔ **この1本は `identity` を二つ添付する。** 動画の仕様 §6——
  「**REF_CHARACTER: 根本湊 … (CRITICAL). この1本は `identity` を添付する。**」
  「**REF_CHARACTER: 関口浩一 … (CRITICAL). この1本は `identity` を添付する。**」
  ——⚠️ **この作品で、二人ぶんを添付するのはこの1本だけである。**
- ⚠️ **ゆえに、この1枚は「二本の手の一枚」そのものである。** 動画の仕様 §15 `Identity`——
  「**Must preserve** — both hands from their frozen sheets, **in the same style as the other hands**」。
  ⛔ **この1枚の外れは、1枚で終わらない**——**この作品の手は全部で十数本あり、
  そのうち二本がここで決まる。**
- ⚠️ **そして、顔は置かれない。** §16 `MUST NOT`——「**No face before the name is called.**」、
  §3 の二人の節——「⚠️ **顔は置かない。**」
  ⛔ **世界の規則がそう決めている**（`bible.world.rules`——「**手が先にあり、顔が後に来る。順序は
  入れ替えない。顔は、呼ばれた後にだけ置かれる。**」）。**この1本が持つ行は
  「まだ、呼ばれていない。」である**（`l19`·88.564秒）。**ゆえにこの1枚に顔が在れば、
  それは「順序」と「行」の両方の違反である。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s16` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**二つ目の場所**と**切れ目**と**順番**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が「二人目の人物」と「切れ目」にある。** 動画の仕様 §20——
  「**A cut may be inserted** between the two places.」「**A face may be placed** at either desk.」
  「**The paper may be read** — the shot's presses would then be a comparison of two names.」
  **ゆえにこの段落は `no cut, no dissolve, no split screen, no panel`／`no face in the frame,
  no head, no chin, no hair, no shoulder above either cuff`／`no read, no insert of the writing` を持つ。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。**
  ⚠️ **要求を節に割れば5節であり、この段落はその5節をすべて文字として持つ**
  （`no watermark`／`no on-screen subtitles`／`no background music`／
  `no calling voice as a sound effect`／`no face before the name is called`）——
  **数えたのは私であり、照合するのは `L21` である。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s16.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「二つの手が止まり、**机の上には紙だけがある。**」
- `reference_set` は**この1本では6点**である——`根本湊.identity`・`根本湊.negatives`・
  `関口浩一.identity`・`関口浩一.negatives`・`名札`・`名札.appearance`。
  ⚠️ **この1本は `identity` を二つ含む**——**この作品で唯一である**（動画の仕様 §6）。
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した二枚を渡す）。
- ⛔ **食い違い1（読み取り・裁定は著者のもの）。** 動画の仕様 §3 は二人の `Reference` を
  ⛔ **下に引く2行は実在しない。** **誤りを名指すために引いているのであって、
  ここから写してはならない**（実在する2枚は、この節のすぐ下に別に書いてある）——
  `distill-essence-engine/examples/habits/character/サブ/12_根本湊/ChatGPT Image 2026年9月21日 11_50_00.png`
  と `.../サブ/13_関口浩一/ChatGPT Image 2026年9月21日 12_05_00.png` と書く。
  ⚠️ **実測（2026-09-28）——その2つのディレクトリは無い。**
  `サブ/12_` は `山田健太`（`00_52_45`）、`サブ/13_` は `田村彩`（`00_58_40`）である
  ——**どちらも、名指された PNG を持たない。** **ゆえに §3 の2行は、フォルダの番号も
  ファイル名も誤っている**（実測 2026-09-28——`11_50_00` と `12_05_00` は
  `character/` の下の `find` で 0 件である）。
  ⚠️ **同じファイルの §6 は正しい**——`サブ/10_根本湊/ChatGPT Image 2026年9月20日 19_56_46.png`
  と `サブ/20_関口浩一/ChatGPT Image 2026年9月21日 01_11_22.png` が実在し、
  `ledger.yaml` の `根本湊.identity`・`関口浩一.identity` も同じ先を指す。
  **この1枚は §6 の側を採った。**
  ⚠️ **その後、著者の側がこの2行を直した**（実測 2026-09-28——**動画の仕様 §3 は、
  いま `サブ/10_根本湊/ChatGPT Image 2026年9月20日 19_56_46.png` と
  `サブ/20_関口浩一/ChatGPT Image 2026年9月21日 01_11_22.png` を指す**）。
  **ゆえに上に引いた2行は、いま動画の仕様には無い。** ⛔ **ここに残したのは、
  見つけた食い違いの記録であって、いまの状態ではない。**
- ⛔ **食い違い2（読み取り・裁定は著者のもの）。** 動画の仕様 §4 は
  「⚠️ **この1本が、この現場の最後の使用である。**」と書く（`place: 名札`）。
  ⚠️ **台帳はそう書いていない**——`ledger.yaml` の `locations.名札` は
  「この作品で使うショット: `s05`・`s06`・`s07`・`s08`・`s12`・`s13`・`s14`・`s15`・`s16`・
  `s19`・`s20`・`s21`・`s22`・`s23`」（**14本**）と数えており、
  **`s16` のあとに6本が残っている**（`s19`〜`s23`）。
  ⚠️ **「サビの14本は、すべてこの現場である」という註も同じ数え方である**（サビ1の4本＋
  サビ2の5本＋最後のサビの5本）。**ゆえに `s16` は「サビ2の最後」であって「現場の最後」ではない。**
  **この1枚は、その読みで書いた**（`s16` は `chorus-2` の最後の1本である）。
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** 実測（2026-09-28）——`specs/image/` に在る画像は
  `01_ChatGPT Image 2026年9月28日 05_34_07.png` と `02_ChatGPT Image 2026年9月28日 05_36_27.png`
  の2枚であり、`media/` に在るのは動画3本だけである。**この1本の分は、まだ無い。**
  **`attached` を書くのは、送った日である。**
