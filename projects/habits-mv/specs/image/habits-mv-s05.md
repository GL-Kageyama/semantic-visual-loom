# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第五のショット「手が滑り、一点を指す」（所作 / motion / 2.473s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、この作品で初めて「サビの現場」を写す1枚である。** 動画の仕様 §1——
「**a hand slides across a nameplate and stops on a single point of a character**」、
そして「**It is the work's first question asked by a hand**」。
⛔ **この1本は顔を置かない**（§3——「**顔は置かない。**」、§16——「**The face does not enter the frame.**
No chin, no hair, no shoulder above the sleeve.」）。**ゆえにこの1枚も、顔を写さない。**
⚠️ **名は、画面の中でいちばん読めない**——§16 は「**The nameplate is not readable.** ⚠️ **This is the
shot where that is hardest** — the plate is the subject and fills the frame, and it still cannot be read.」と言う。
⚠️ **名札は、机の上に置かれない。** §17——「**The plate is worn on a sleeve** — ⚠️ **not lying on a desk.**」
⛔ **この1本に紙は無い**（§4 `Environment Elements`——**左袖、その上、机の面の一部**。
⚠️ **§5 の「紙」の項は、本文が名札の面のことを書いている**——**食い違いは下の節に記録した**）。
⚠️ **この1枚は、この1本の終わりの状態を写す。** `unit.after` は
「手が止まり、**字の一点を指している。**」である——**渡すのは開始のコマではない。**
⚠️ **止まった指は、静止した1枚に写る。** **ゆえにこの1枚は、この1本の「変化のあと」をそのまま持つ。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **1本目から4本目までと同じ組である。** `specs/video/seedance-2.5/habits-mv-s05.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` を名乗り、§2 `Visual Language` は
    「**Luminous realist anime, translated into a left sleeve and the hands at it.**」
    ——**動画の側が、この1本では「左袖へ翻訳した」と書いている。**
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s05.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/01_佐藤美咲/prompt.md`
  と**凍結した一枚**（`character-sheet × luminous-anime`）。
  ⚠️ **この1本は `identity` を添付する側である**（動画の仕様 §6——「**この1本は `identity` を添付する**
  — **手の造形がこの人物のものであるためである。**」）。**ゆえに絵の側でも渡す。**
  ⚠️ **顔を置かない1本であるのに添付するのは、そのためである**——**渡すのは顔ではなく、手の造形である。**
- 添付する参照: **`specs/image/生成時参照イラスト/s05/` の1枚**——`佐藤美咲_設定画.png`。
  ⚠️ **この1枚は、この作品の動画の側の同じ1枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s05/`。実測 2026-09-28、ハッシュが一致した）。
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
  **和が、そのまま下の7欄である**（実測 2026-09-28、`s01`・`s02` の2枚で確認）。
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** 様式カードの雛形は
  `Not photorealistic, …` で終わるが、**この作品はそれを2段落目に置く**——**この作品は実写ではない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s05` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「止まった指」を写すのは、そのためである**——**渡すのは、この1本が終わった
  あとの状態＝世界の側であって、開始のコマではない。** ⚠️ **動画の仕様 §16 は
  「**A hand crosses the plate and stops on one point of one character.**」と言う**
  ——**滑ることは、止まった1枚からは読み取れない。ゆえに変化は、動画の側に残る。**
  ⛔ **かつ、この1枚は「動きの無い1枚」ではない。** §4 `Environmental Behavior`——
  「**指が止まったあとも、埃とプラスチックの上の光は動き続ける。**」
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s05.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **この1本の1枚は、まだ無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の註は、この1本では「手」の側である**——**顔が置かれないからである。**
⛔ **註に置くのは、人物の名と、凍結した一枚を指すことだけである。**
**外見は書き起こさない**（理由は下の節に書く）。⚠️ **この作品には、手を書く語が無い**——
**凍結した一枚が手を持つ。**（下の「註」の節を見よ。）

- `SCENE`: the fifth step, and the work's first question asked by a hand — a right hand has crossed the nameplate and stopped on a single point of one character, and the point is not readable either
- `CHARACTERS`: `[佐藤美咲: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **the hand and the plate are the whole figure in the frame**; **no face, no chin, no hair, no shoulder above the cuff**, the fingers do not close, and no arm is in the frame
- `SUBJECT`: the finger stopped on one point of one character, and the plate it has crossed
- `ACTION`: having crossed the plate left to right, fast and flat, the pads reading the surface rather than the name, and having stopped there — one finger pressing one point and staying, the wrist not lifted, the fingers not closing, and no second movement
- `LOCATION`: the school's designated nameplate fixed to a left sleeve, in a school in the middle of a working day, 2026 — **the sleeve filling the rest of the frame**, the cuff at the frame's edge, part of the desk's surface beyond it, and **the person the plate is fixed to not in the frame**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling even across plastic and cloth, **the plate's cream face the brightest thing in the frame**, with the tube's highlight on the plastic, since plastic is the one material in this work that gives the tube back while the sleeve behind it is cloth and does not; dust over the sleeve; everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the tube's highlight on the plastic — the one material in this work that gives the tube back, and the only thing in the frame that is neither skin nor cloth nor ink

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the fifth step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration at the height of a left sleeve, of a right hand that has crossed a school nameplate and stopped on a single point of one character. The plate is the school's designated nameplate — plastic, fixed to a cloth sleeve, a dark border, rounded corners, characters on its face that are present and cannot be made out — and it is worn on the sleeve and not lying on a desk; the cuff is at the frame's edge, part of the desk's surface lies beyond it, and the person the plate is fixed to is not in the frame. The hand is the only motion the figure has: it has come across the plate from left to right, fast and flat, the pads of the fingers reading the surface rather than the name, and it has stopped on one point of one character and stays there — the wrist is not lifted, the fingers do not close, there is no arm in the frame, and there is no second movement and no overshoot. The plate is at the frame's centre and stays where it is; it does not flex, it does not lift, and it is not turned. The characters on the plate are written in the Japanese script and cannot be made out, and the point the finger has stopped on is not named and cannot be read either. The character of the materials is what this frame is about: plastic is smooth and gives the tube back as a highlight, the cloth of the sleeve behind the plate does not, and the seam where the plate meets the cloth is drawn close. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. Saturated where the light falls and deep cyan in the unlit half; the palette is school plastic — the plate's cream, its dark border, skin, and the cuff of the sleeve it is fixed to. Layered atmospheric depth from near to far; dust suspended and individually rendered over the sleeve where the tube catches it, and it is the only thing in the frame that is still moving. Very low visual density: one focal point, the finger and the point it has stopped on, with the sleeve filling the rest of the frame. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at sleeve height, close, near enough that the plate fills the middle of the frame, and the camera does not travel with the hand. One scene, one staging; the same sleeve, the same plate and the same tube wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no chin, no hair, no shoulder above the cuff, no portrait, no second figure, no person wearing the plate, no plate lying on a desk, no plate off the sleeve, no plate taken off, no plate bending, no flexing plate, no lifting of the plate, no turning of the plate, no looking under the plate, no under-side of the plate, no second movement of the hand, no closed fist, no tapping finger, no fingers closing, no arm in the frame, no wrist lifted, no follow of the hand, no camera movement, no hand lifted off the plate, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no insert of the writing, no magnified detail of the characters, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この1枚の画面は、左袖と名札である。** 動画の仕様 §10——「**close, at the left sleeve** ——
  **the second of this work's three camera sites**」。**空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s05` §2——
  「**Luminous realist anime, translated into a left sleeve and the hands at it.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**袖の上の名札が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**（1本目の同じ節を見よ。）
- ⚠️ **この1枚には、様式の「最も明るい一点」が人物の上に無い**（凍結した一枚の問題意識——
  「**この一枚には、様式が与えるはずの「最も明るい一点」が人物の上に一つも無い。**」）。
  **最も明るいのは、プラスチックの面である。**

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s05` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚は、この作品で唯一「プラスチック」を写す。** 動画の仕様 §2 `Texture`——
  「**Plastic is smooth and gives a highlight; the sleeve behind it is cloth and does not.**」
  ⛔ **実写のプラスチックは、この作品のものではない**——**この1枚の plastic は、
  セル画の一つの影の階調である。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、この名札が実物になる。**（1本目の同じ節を見よ。）

## ⚠️ 註は「どの手か」だけを教える——外見は、凍結した一枚が持つ

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**）。
  ⛔ **だが、置かれるのは手だけである**——**註は「手」の側に付く。**
- ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**手は凍結した設定画のものである**」だけである——**註の形は、この作品で1つに決まっている。**
- ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな手か」を教えることではない。**
  動画の仕様 §3——「**外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。**」
  ⚠️ **そして、この人物の凍結した一枚には、手を書く行が無い**——
  **ゆえにこの1枚は、手を語で書かない。** **語が無いところでは、書かないことが仕様である。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `identity` を添付する側である——この1枚が、その一枚である

- `s01` は凍結した一枚を**意図的に持たなかった**（「人のかたちの一枚を渡せば、生成器は顔を置く」）。
  ⛔ **この1本は逆である。** 動画の仕様 §6——「**この1本は `identity` を添付する** ——
  **手の造形がこの人物のものであるためである。**」
- ⚠️ **ゆえに、この1枚は「手の一枚」そのものである。** **この1枚が外れれば、
  サビの14本の手が、同じ様式の手でなくなる**（動画の仕様 §15 Identity——
  「**Must preserve** — the hand of the frozen sheet, and **the same style of hand as the fourteen
  other hands of this work.**」）。⛔ **この1枚の外れは、1枚で終わらない。**
- ⛔ **顔は置かれない。** §16——「**The face does not enter the frame.** No chin, no hair, no
  shoulder above the sleeve.」 ⚠️ **世界の規則がそう決めている**（`bible.world.rules`——
  「**手が先にあり、顔が後に来る。順序は入れ替えない。顔は、呼ばれた後にだけ置かれる。**」）。
  **この1本はサビであり、サビは明かさない側である**（記録の頭——「**この作品は、サビで顔を置かない。**」）。
  ⛔ **ゆえにこの1枚に顔が在れば、それは「順序」と「サビ」の両方の違反である。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **この1本は、その危険が最も大きい。** 動画の仕様 §20 の1番目——
  「**The name may be rendered legible.** ⚠️ **The first risk of this shot and the worst one**:
  the plate fills the frame, and **a readable name at this site answers the song's question in the
  wrong direction.**」
  ⛔ **画像の側では、この段落がそれを止める**——**`no legible name text` が、この1枚の中心の禁制である。**
  ⚠️ **しかも、この1本はサビである**——**曲が「その字は、誰の字。」と問うている。
  読めた瞬間に、問いが答えになる。**
- ⚠️ **この1本には、もう一つの近い危険が在る**（§20 の3番目）——「**The face may be placed above
  the sleeve.** Sleeve height is close to a chin, and a generator will supply one.」
  ⛔ **ゆえにこの段落は `no face in the frame, no chin, no hair, no shoulder above the cuff` を持つ。**
  ⚠️ **そして4番目——「The hand may lift the plate.」は `s06` の所作である。**
  **この段落は `no lifting of the plate`／`no turning of the plate`／`no looking under the plate` で、
  その越境を止める。**
- ⚠️ **絵の側の実測が、既に在る。** `s03` の動画は 2026-09-28 に送られ、§20 の `Observed Problems` が言う
  ——「**左の頁の手書きが、ラテン文字の草書として戻った** ——日本語の字ではない。§18 は
  `no real-world alphabet` を**既に持っていた**——**この経路では散文として読まれた**（`L30`）。」
  **ゆえにこの段落にも `no Latin cursive` を置く。** **字を描く1本では、否定は効いた場所に置かねばならない。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。** ⚠️ **要求を節に割れば5節であり、この段落はその5節を
  すべて文字として持つ**（`no watermark`／`no on-screen subtitles`／`no background music`／
  `no calling voice as a sound effect`／`no face before the name is called`）——
  **数えたのは私であり、照合するのは `L21` である。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s05.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `佐藤美咲.identity` を含む4点**である
  （`佐藤美咲.identity`／`佐藤美咲.negatives`／`名札`／`名札.appearance`）。
  ⚠️ **顔を置かない1本が `identity` を持つのは、手の造形のためである**（動画の仕様 §6）。
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した一枚を渡す）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⚠️ **食い違い1（読み取り・裁定は著者のもの）。** 記録の `unit.before` は
  「一枚の紙の上を、**手が滑っている。**」と言い、`motion.subject` は「佐藤美咲の右手と、
  **その下の紙**」と言う。⚠️ **だが、動画の仕様の画面に紙は無い**——
  §4 `Environment Elements` は「**左袖、その上、机の面の一部**」であり、§5 の「**紙**」の項は
  **本文が名札の面のことを書いている**（「名札の面は、この作品で唯一**曲がらない**面である」）。
  §17 は「**The plate is worn on a sleeve** — **not lying on a desk.**」と明記する。
  ⛔ **この1枚は、動画の仕様の側で書いた**——**紙を描いていない。**
  **この段落も、紙については何も禁じていない**（**裁定が下るまで、どちらとも書かない**）。
- ⚠️ **食い違い2（読み取り）。** 動画の仕様 §13 の `Base Lighting` は
  「**the paper is the brightest thing in the frame**」と言うが、**この画面に紙は無い。**
  **この1枚で最も明るいのは、名札の面である**（上の `LIGHT` はそう書いた）。
  ⚠️ **同じ定型は `s06` の §13 にも在る**——**そちらは §16 が「No paper in this shot」と明記しており、
  同じ食い違いが2本で起きている。**
- ⛔ **この1枚は、まだ投入されていない。** 実測（2026-09-28）——`specs/image/` に在る画像は
  `01_ChatGPT Image 2026年9月28日 05_34_07.png` と `02_ChatGPT Image 2026年9月28日 05_36_27.png`
  の2枚であり、`media/` に在るのは動画3本だけである。**この1本の分は、まだ無い。**
  **`attached` を書くのは、送った日である。**
