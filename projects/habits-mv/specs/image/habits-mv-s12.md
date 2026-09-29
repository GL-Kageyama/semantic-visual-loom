# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十二のショット「手の甲が返り、掌が上を向く」（所作 / motion / 2.473s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、この作品で初めて「掌」を写す1本である。** 動画の仕様 §2——
「**the light falls from above, so the back of the hand is lit and the palm, once it comes up,
is the shadowed side**」。⛔ **この1本の光は、掌を照らさない。**
⚠️ **この1本は、四つの所作の2本目である**（§2——「**`s05` は「滑って止まる」、`s12` は「返って止まる」**」）。
⛔ **この1本は顔を置かない**（§3——「**顔は置かない。**」、§16——「**The face does not enter the frame.**」）。
**ゆえにこの1枚も、顔を写さない。**
⚠️ **この1枚は、この1本の終わりの状態を写す。** 記録の `unit.after` は
「手が返り、**掌が上を向いている。**」である——**渡すのは開始のコマではない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/seedance-2.5/habits-mv-s12.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into the back of a hand turning over on a desk.**」
    ——**動画の側が先に、この様式を「机の上で返る手の甲へ翻訳した」と書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s12.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/06_大森徹/prompt.md`
  （凍結した設定画の読み。「出典の語」の節）と、同じ作品の既存の生成物（`media/` の動画3本）
- 添付する参照: **`specs/image/生成時参照イラスト/s12/` の1枚**——`大森徹_設定画.png`。
  ⚠️ **この1枚は、この作品の動画の側の同じ1枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s12/`。実測 2026-09-28、ハッシュが一致した）。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s12` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「上を向いた空の掌」を写すのは、そのためである**——**渡すのは、この1本が終わった
  あとの状態＝世界の側であって、開始のコマではない。** ⚠️ **返ることは、返り終えた1枚からは
  読み取れない。ゆえに変化は、動画の側に残る。**
  ⛔ **かつ、この1枚は「動きの無い1枚」ではない。** §11 `Environmental Motion`——
  「**Dust moves over the desk and crosses the open palm. It keeps moving after the hand has stopped.**」
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s12.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
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
⛔ **註に置くのは、人物の名と、凍結した一枚を指すことだけである。**
**外見は書き起こさない**（理由は下の節に書く）。⚠️ **この作品には、手を書く語が無い**——
**凍結した一枚が手を持つ。**

- `SCENE`: the second of the four gestures of the chorus, and the work's first palm — a right hand has turned over where it lay on a desk and the palm is up and empty
- `CHARACTERS`: `[大森徹: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **the hand and the desk are the whole figure in the frame**; **no face, no chin, no hair, no shoulder, no arm, no sleeve**, the fingers are open and no object is in the palm
- `SUBJECT`: the open empty palm, and the desk it came up from
- `ACTION`: having turned over — the turn happened at the wrist and the arm did not move, the fingers opened as it turned rather than after it, and the palm came up and stays; **nothing was given and nothing was taken**
- `LOCATION`: a desk top in a school room in the middle of a working day, 2026 — the desk's worn wooden face with the polish of forearms on it, its edge at the frame's lower right, and **nothing on it**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling even across the wood, **the back of the hand lit and the palm, once it is up, the shadowed side**, bloom where the tube catches the desk, dust over the surface, everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the polish of forearms on the wood and the pale of the palm that has not been in the light — the two warm-grey things the tube finds in a narrow, cold room

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the twelfth step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of a right hand turned over on a desk, the palm up and empty, in a school room in the middle of a working day, 2026. The hand is the whole figure in the frame and the only motion it has ever had: it lies where it lay at the frame's centre, it has turned over at the wrist and the arm did not move, the fingers opened as it turned rather than after it, and the palm faces up and stays there — no overshoot, no settle, and no second movement. Nothing is in the palm and nothing is under the hand: the palm is open, empty, and held at the distance it was turned at, and the fingers do not close. There is no arm in the frame past the wrist: the wrist runs out of the picture on the right and the picture's edge crops it — no sleeve, no cuff and no forearm, and no face: no chin, no hair, no shoulder above the desk. The desk is a worn wooden top with the polish of forearms on it, its grain running under the hand so that the turn reads as happening on a surface rather than in the air, and its worn edge is in the near foreground; the desk is otherwise bare, with no paper, no plastic and no object of any kind on it. The light is a fluorescent tube above and behind the camera, falling flat and even across the wood and blooming where it catches the desk: it falls from above, so the back of the hand is lit and the palm, now that it is up, is the shadowed side — the shot's light does not change to help it, and the pale of the palm is the pale of skin that has not been in the light. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one material and no gradient inside a single material. The palette is desk and skin — the wood's warm grey, and the palm's unlit pale — saturated where the light falls and deep cyan in the unlit half. Layered atmospheric depth from near to far; dust suspended and individually rendered over the desk where the tube catches it, crossing the open palm, and it is the only thing in the frame that is still moving. Very low visual density: one focal point, the open hand, with the desk filling the rest of the frame and generous negative space around it. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at hand height, close, looking slightly down, the hand at the frame's centre with the wrist running out of the picture on the right, and the camera does not travel and does not lean in. One scene, one staging; the same desk, the same hand and the same tube wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no chin, no hair, no shoulder above the desk, no portrait, no second figure, no person in the frame, no paper in the frame, no plastic in the frame, no nameplate in the frame, no object in the palm, no object under the hand, no object on the desk, no gift in the hand, no offering, no closed fingers, no fist, no fingers closing, no second movement of the hand, no re-turn of the hand, no arm in the frame past the wrist, no sleeve, no cuff, no forearm, no wrist lifted, no follow of the hand, no camera movement, no lean in, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この1枚の画面は、机の面と、その上の手である。** 動画の仕様 §10——「**close, on the hand on
  the desk — the work's desk site**, at hand height, looking slightly down」。**空が入る余地は、
  構図の側に無い。** ⚠️ **しかもこの1本は、カメラが静止したままである**（§10 の `Camera Events` は
  「**None.**」）——**空へ逃げる動きも無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s12` §2——
  「**Luminous realist anime, translated into the back of a hand turning over on a desk.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**机の上の手が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**
- ⚠️ **この1枚には、様式の「最も明るい一点」が人物の上に無い。** **最も明るいのは、机の面である**
  ——⚠️ **動画の仕様 §13 の定型は「the paper is the brightest thing in the frame」と言うが、
  この画面に紙は無い**（下の「記録との対応」に、この食い違いを記録した）。

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s12` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⛔ **この1本は、この作品で最も「手だけ」の1本である。** §11 `Subject Motion`——
  「**It is the only motion the figure has.** The arm is not in frame.」
  **実写の手が戻れば、この1枚は人物の肖像の切り抜きになる。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、机の上の手が実物になる。**（1本目の同じ節を見よ。）

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
  動画の仕様 §3——「**外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。**」
  ⚠️ **この人物の凍結した一枚は、読みと註を持つ**——`サブ/06_大森徹/prompt.md` の
  「出典の語」の節である。**ゆえにこの1枚は、手を語で書かない。**
  **語が無いところでは、書かないことが仕様である。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ 掌は、暗い側である——この1枚の光は、掌を助けない

- 動画の仕様 §13 の `Lighting Events` は「**None.**」であり、その理由を自分で書いている——
  「**The palm is dark because it was turned away from the tube**, and the shot's light does not
  change to help it.」
- ⛔ **ゆえにこの1枚は、掌を明るく描かない。** 生成器は開いた掌を「見せ場」として照らす——
  **均一に照らされた掌は、この1本の「返った」という出来事を消す**
  （§20 の4番目——「**The palm may be lit like the back of the hand** — the shot's light is
  directional, and an evenly lit palm loses the turn.」）。
- ⚠️ **この1枚の明暗は、返る前と後で入れ替わる。** §5 `Visual Language`——
  「**the back of the hand is lit and the palm, once it comes up, is the shadowed side**」。
  ⛔ **この1枚は「返ったあと」だから、掌が暗い側である。** **それが1本の証拠である。**
- ⚠️ **ゆえに `Negative` に `no flat light on the palm` ではなく、光の側の行を置いていない**
  ——⚠️ **否定は「何を描かないか」であって、「どう描くか」ではない。**
  **この1枚は `Prompt` の側で、掌を暗い側として書く。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **この1本の危険は、この作品で最も単純である。** 動画の仕様 §20 の1番目——
  「**Something may be placed in the palm.** ⚠️ **The first risk of this shot**: an open hand is an
  invitation, and **a generator will fill it.** **An object in the palm turns this into a giving
  shot and the work's carrying completes for the first time in the wrong place.**」
  ⛔ **画像の側では、この段落がそれを止める**——**`no object in the palm` が、この1枚の中心の禁制である。**
  ⚠️ **同じ危険が、掌の側から机の側へも伸びる**（§20 の3番目——「**An object may be added to the
  desk** — a pen, a stack, a cup」）——**ゆえに `no object on the desk` も置く。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。** ⚠️ **要求を節に割れば5節であり、この段落はその5節を
  すべて文字として持つ。**
- ⚠️ **`no stack of paper` が尾に在る**——⚠️ **この1本の画面には、そもそも紙が無い。**
  **禁じる必要の無い1本ではあるが、尾はこの作品の共有の枠である**——**ゆえに1語も変えずに置く。**

## ⚠️ 手首の切れ目は、枠の縁で起きる（2026-09-30、著者の裁定）

- 実測（2026-09-30）。この稿の文字列は投入され、1枚が生成された
  （`media/NG_12_ChatGPT Image 2026年9月30日 01_51_53.png`——**著者が NG と名付けた**）。
  ⛔ **その1枚では、手は枠の内側で終わっていた**——手首の先が輪郭線で閉じ、その下に落ち影が付き、
  **右に裸の机が残る**（実測——肌の列は x≈1177 で尽きる。枠は1672px）。**ゆえにその1枚は、
  「机の上に置かれた、手の形をした物」に見える。**
- ⚠️ **原因は、この稿の内側の食い違いである。** この `Prompt` は「**the hand at the frame's centre**」と
  置き、**同じ段落が「no arm in the frame … no forearm」と禁じる**——**腕が無いのに、手は枠の中央に在る。
  ゆえに手は、自分の輪郭で終わるしかない。**
- ⚠️ **この作品は、答えを既に持っている。** 動画の仕様 `s05` §10——
  「**the cuff at the frame's edge**, so that the plate reads as **worn rather than as lying on a
  surface**」。⚠️ **`s19`・`s21`・`s22`・`s23` も同じ形である**（「arm not in the frame **beyond the
  plain cuff**」）。**切れ目を枠の縁に置けば、体の続きが見える。**
- ⛔ **ゆえにこの稿は、2段落を直した**（2026-09-30。裁定は——「禁制を緩める。切れ目は枠の縁、
  ただし袖・袖口・前腕は描かない」）。`Prompt` の腕の行を「**no arm in the frame past the wrist**——
  **the wrist runs out of the picture on the right and the picture's edge crops it**」へ、`Prompt` の
  構図の行へ「**with the wrist running out of the picture on the right**」を、`Negative` の
  「no arm in the frame」を「**no arm in the frame past the wrist**」へ。
  ⛔ **袖・袖口・前腕は、禁じたままである**——**この1本の画面は、机と肌である。**
- ⚠️ **`Negative` に、症状の名を足していない。** 「切れた手」の類の語を否定に置けば、
  **その語が描かれる側へ回りうる**——**形は `Prompt` の側で言う。**
- ⚠️ **動画の仕様 §10 の1行も、同じ語で直した**（2026-09-30——
  「The hand at the frame's centre with the desk's grain running under it」→
  「…**with the wrist running out of the picture on the right**…」）。
  **この1枚は、その動画の参照画像である**——**構図が食い違えば、参照が嘘になる。**
  ⚠️ **動画の側の §11（「The arm is not in frame.」）は動かしていない**——**腕は、いまも描かれない。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s12.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `大森徹.identity` を含む4点**である
  （`大森徹.identity`／`大森徹.negatives`／`名札`／`名札.appearance`）。
  ⚠️ **顔を置かない1本が `identity` を持つのは、手の造形のためである**（動画の仕様 §6——
  「**この1本は `identity` を添付する。** ⚠️ **顔は置かない。**」）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⚠️ **凍結した一枚の道を、ここに実測で固定する。** この1本が `identity` として添付する一枚は
  `distill-essence-engine/examples/habits/character/サブ/06_大森徹/ChatGPT Image 2026年9月21日 00_46_20.png`
  である（実測 2026-09-28、`ls` で確認——`サブ/06_大森徹/` の中身は、この PNG と `prompt.md`
  の2つだけである）。⚠️ **この道は、動画の仕様 §6 と一致する。**
- ⚠️ **動画の仕様 §3 の `Reference:` の行は、道もファイル名も誤っていた**——§6 とは別の人物の
  フォルダを指していた。⚠️ **この稿を書いている時点で、著者の側が直している**（`s11`〜`s15` の5本）。
  ⛔ **誤っていた名前をここに写さない**——**消えた名前を引用に残せば、直っていないように読める。**
  ⚠️ **画像の側が取る一枚は、上の1行だけである。**
- ⚠️ **食い違い2（記録と画面）。** 記録の `reference_set` は**小道具 `名札` と `名札.appearance` を
  持つ**が、⚠️ **動画の仕様 §4 は明示する**——「**この1本に名札は置かない** — `place` は `名札` だが、
  **この1本の現場は机の上の手である**」、そして §5——
  「**No other object is in frame.** ⚠️ **この1本に物を足さない** — **足せば、返った掌が何かを持つように
  見える。**」。⛔ **ゆえにこの1枚は、名札を描いていない。** **`place` は「現場の鍵」であって、
  「画面に在る物」ではない**（`ledger.yaml` の `locations` の註——六つの `place` を27本が巡る）。
  ⚠️ **記録の側の裁定は著者のものである**——**私は動画の仕様の側で書いた。**
- ⚠️ **食い違い3（定型文）。** 動画の仕様 §13 の `Base Lighting` は
  「**the paper is the brightest thing in the frame**」と言うが、**この画面に紙は無い。**
  **この1枚で最も明るいのは、机の面である**（上の `LIGHT` はそう書いた）。
  ⚠️ **同じ定型は `s05`・`s06`・`s13`・`s14` の §13 にも在る**——**この定型は27本で共有されており、
  紙を持たない1本では意味を失う。** **この1枚は、定型ではなく画面の側を書いた。**
- ⚠️ **記録の `attached` の註は、まだ「この作品はまだ1本も生成していない」と言う。**
  ⛔ **だが、いまの状態はそうではない**（実測 2026-09-28——`media/` に動画3本、`takes/` に3本、
  その3本は `s01`・`s02`・`s03` である）。**この1本は、その3本に入っていない。**
- ⛔ **この稿の文字列は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
