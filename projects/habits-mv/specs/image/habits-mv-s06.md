# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第六のショット「指が名札の縁を起こし、裏を見る」（所作 / motion / 2.474s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1.` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、この作品でいちばん「見せない」ことを内容にする1枚である。** 動画の仕様 §1——
「**a finger lifts the edge of a nameplate and looks under it.** ⚠️ **The shot shows the intention and
withholds the result**: the plate comes up, and what is under it is not in the frame.」
⛔ **この1本の意味は、明かさないことの側に在る**（§17 の1番目——「**The plate comes up and the answer
does not** —— ⚠️ **showing the back would answer the song's question with an object, which is the one
thing this work never does.**」）。**ゆえにこの1枚にも、裏は写らない。**
⚠️ **名札は、この作品で唯一、曲がらない物である**（記録の `motion.law`、§11 `Fluidity`——
「**The plate does not bend** — plastic is the one material in this work that holds its shape.」）。
⛔ **この1本に紙は無い**（§4 `Environment Elements`——**左袖、名札、名札の下の縫い目**。
§16——「**No paper in this shot** — the plate is plastic and the sleeve is cloth, and nothing else is here.」）。
⚠️ **この1本は、名札と袖の隙間へ入る唯一の1本である**（§4）。
⚠️ **この1枚は、この1本の終わりの状態を写す。** `unit.after` は
「指が名札の縁を起こし、**裏を見ている。**」である——**渡すのは開始のコマではない。**
⚠️ **浮いたまま止まっている縁は、静止した1枚に写る。** **ゆえにこの1枚は、この1本の「変化のあと」をそのまま持つ。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **1本目から5本目までと同じ組である。** `specs/video/seedance-2.5/habits-mv-s06.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` を名乗り、§2 `Visual Language` は
    「**Luminous realist anime, translated into a left sleeve and a plate being lifted at its edge.**」
    ——**動画の側が、この1本でも「左袖へ翻訳した」と書いている。**
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s06.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/02_鈴木和彦/prompt.md`
  と**凍結した一枚**（`character-sheet × luminous-anime`）。
  ⚠️ **この1本は `identity` を添付する側である**（動画の仕様 §6——「**この1本は `identity` を添付する**
  — **指の造形がこの人物のものであるためである。**」）。**ゆえに絵の側でも渡す。**
  ⚠️ **顔を置かない1本であるのに添付するのは、そのためである**——**渡すのは顔ではなく、指の造形である。**
- 添付する参照: **`specs/image/生成時参照イラスト/s06/` の1枚**——`鈴木和彦_設定画.png`。
  ⚠️ **この1枚は、この作品の動画の側の同じ1枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s06/`。実測 2026-09-28、ハッシュが一致した）。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s06` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「浮いたまま止まった縁」を写すのは、そのためである**——**渡すのは、この1本が
  終わったあとの状態＝世界の側であって、開始のコマではない。** ⚠️ **動画の仕様 §16 は
  「**A finger lifts one edge of the plate and the plate stays up.**」と言う**
  ——**起こすことは、起きた1枚からは読み取れない。ゆえに変化は、動画の側に残る。**
  ⛔ **かつ、この1枚は「動きの無い1枚」ではない。** §4 `Environmental Behavior`——
  「**縁が浮いたあと、そこに入った埃が動く** —— それが浮いたことを画面の側で確かめる唯一のものである。」
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s06.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **この1本の1枚は、まだ無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の註は、この1本では「指」の側である**——**顔が置かれないからである。**
⛔ **註に置くのは、人物の名と、凍結した一枚を指すことだけである。**
**外見は書き起こさない**（理由は下の節に書く）。⚠️ **この作品には、手を書く語が無い**——
**凍結した一枚が手を持つ。**（下の「註」の節を見よ。）

- `SCENE`: the sixth step, and the work's second question answered by a hand — a finger has lifted one edge of the nameplate by a few millimetres and the plate stays up, and what is under it is not in the frame
- `CHARACTERS`: `[鈴木和彦: **one finger, and no one in place** — **the hand the frozen setting sheet holds**]` — **the finger and the plate are the whole figure in the frame**; **no face, no chin, no hair, no shoulder above the cuff**, the hand does not rotate, and no arm is in the frame
- `SUBJECT`: the edge of the plate lifted by a few millimetres, and the cloth beneath it that has gone bright
- `ACTION`: having taken the edge with the nail and lifted it once — the plate up a few millimetres and not put back down, the hand not rotating, the arm not coming in, and no second movement
- `LOCATION`: the school's designated nameplate fixed to a left sleeve, in a school in the middle of a working day, 2026 — **the sleeve filling the rest of the frame**, **the seam at the plate's left edge**, and **the person the plate is fixed to not in the frame**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera, **getting under the plate because the plate has moved and not because the light has changed**, so that **the cloth beneath the lifted edge is the frame's only bright passage and is brighter than the cloth beside it**; bloom on the plastic; everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the lit cloth under the lifted edge — the frame's only bright passage, and the one place in the frame where the light has got under the plate

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the sixth step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration at the height of a left sleeve, of one finger that has taken the edge of a school nameplate and lifted it by a few millimetres, with the plate still up. The plate is the school's designated nameplate — plastic, fixed to a cloth sleeve, a dark border, rounded corners, characters on its face that are present and cannot be made out — and it stays on the sleeve: it is lifted at one edge and it is not taken off, put back down, or turned, and the under-side of it is nowhere in this frame. What is under the plate is not shown: no tilt, no turn, no cut, no reflection and no insert gives it away, and the frame does not lean toward the opened seam. The seam between plastic and cloth, at the plate's left edge, is the frame's most detailed passage, and where the edge has lifted the cloth beneath is brighter than the cloth beside it, because the light has got under the plate by the plate moving and not by the light changing. The plate does not bend: plastic is the one material in this work that holds its shape, it keeps its highlight, and the cloth behind it gives and does not. The hand is the only motion the figure has and there is only one of it: a nail at the corner, one lift, no return, no rock and no overshoot, the hand not rotating, the arm not coming in, and no second finger anywhere in the frame. The characters on the plate are written in the Japanese script and cannot be made out. There is no paper in this frame — the plate is plastic and the sleeve is cloth — and no face enters it: no chin, no hair, no shoulder above the cuff, and nobody wearing the plate is in the frame. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. Saturated where the light falls and deep cyan in the unlit half; the palette is school plastic — the plate's cream, its dark border, skin, and the shadow the lifted edge makes on the sleeve. Layered atmospheric depth from near to far; dust suspended in the seam the lifted edge has opened where the tube catches it, and it keeps moving after the finger has stopped, and it is the only thing in the frame that is still moving. Very low visual density: one focal point, the lifted edge and the shadow under it, with the sleeve filling the rest of the frame. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at the plate's height, close, near enough that the plate and the lifted edge fill the frame, and the camera does not move at all. One scene, one staging; the same sleeve, the same plate and the same tube wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no under-side of the plate, no back of the plate, no tilt of the plate, no turn of the plate, no cut to the under-side, no reflection in the plastic, no insert of what is beneath the plate, no revealing of the back, no plate taken off, no plate coming back down, no second lift, no rocking, no overshoot, no plate bending, no flexing plate, no face in the frame, no chin, no hair, no shoulder above the cuff, no portrait, no second figure, no person wearing the plate, no paper in the frame, no sheet of paper, no page, no arm in the frame, no hand rotating, no second finger, no camera tilt, no push-in, no leaning toward the seam, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no insert of the writing, no magnified detail of the characters, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この1枚の画面は、左袖と名札の縁である。** 動画の仕様 §10——「**close, at the left sleeve** ——
  **the second of this work's three camera sites**, at the height of the plate」。**空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s06` §2——
  「**Luminous realist anime, translated into a left sleeve and a plate being lifted at its edge.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**起きた縁が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**（1本目の同じ節を見よ。）
- ⚠️ **この1本の光は、縁の下へ入る。** §13——「**The light gets under the plate by the plate moving,
  not by the light changing** —— **and that is the shot's whole lighting design.**」
  ⛔ **空の光を足せば、その設計が消える。**

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s06` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚は、この作品で唯一「曲がらない物」を写す。** 動画の仕様 §11 `Fluidity`——
  「**The plate does not bend** — plastic is the one material in this work that holds its shape.」
  ⛔ **実写のプラスチックは、この作品のものではない**——**この1枚の plastic は、
  セル画の一つの影の階調である。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、この名札が実物になる。**（1本目の同じ節を見よ。）

## ⚠️ 註は「どの手か」だけを教える——外見は、凍結した一枚が持つ

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**）。
  ⛔ **だが、置かれるのは指だけである**——**註は「手」の側に付く。**
- ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**手は凍結した設定画のものである**」だけである——**註の形は、この作品で1つに決まっている。**
- ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな手か」を教えることではない。**
  動画の仕様 §3——「**外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。**」
  ⚠️ **そして、この人物の凍結した一枚には、手を書く行が無い**——
  **ゆえにこの1枚は、手を語で書かない。** **語が無いところでは、書かないことが仕様である。**
  ⚠️ **出典の語で書けるのは、この人物の側のことだけである**（§3——出典の語は「**路線バス運転士・52歳**」であり、
  **動きの署名は「乗ってくる者の手の高さに合わせてドアの開く位置を測る」**）——
  ⛔ **この1枚では、そのどちらも註に置かない。** **動きの署名は、動画の側の設計である。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `identity` を添付する側である——この1枚が、その一枚である

- `s01` は凍結した一枚を**意図的に持たなかった**（「人のかたちの一枚を渡せば、生成器は顔を置く」）。
  ⛔ **この1本は逆である。** 動画の仕様 §6——「**この1本は `identity` を添付する** ——
  **指の造形がこの人物のものであるためである。**」
- ⚠️ **ゆえに、この1枚は「手の一枚」そのものである。** **この1枚が外れれば、
  サビの14本の手が、同じ様式の手でなくなる**（動画の仕様 §15 Identity——
  「**Must preserve** — the hand of the frozen sheet and the same style of hand as the other
  fourteen hands.**May change** — nothing.」）。⛔ **この1枚の外れは、1枚で終わらない。**
- ⚠️ **`s05` の手と、同じ様式の同じ描き方であること**（§3 `Continuity Requirements`）——
  **この2本は、同じ問いを2つの所作で受けている**（記録の頭——「**同じ場所・同じ尺・違う手である。**」）。
  ⛔ **2枚を並べたときに同じ描き方でなければ、サビの対が崩れる。**
- ⛔ **顔は置かれない。** §16——「**The face does not enter the frame.**」 ⚠️ **世界の規則がそう決めている**
  （`bible.world.rules`——「**手が先にあり、顔が後に来る。順序は入れ替えない。顔は、呼ばれた後にだけ置かれる。**」）。

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **この1本の一番の危険は、この作品の中心に触る。** 動画の仕様 §20 の1番目——
  「**The under-side may be shown.** ⚠️ **The first risk of this shot, and the one that would answer
  the song.** A camera at a lifted edge will want to tilt; a generator will want to reveal.
  **The shot's whole meaning is in not revealing.**」
  ⛔ **画像の側では、この段落がそれを止める**——**`no under-side of the plate` が、この1枚の中心の禁制である。**
  ⚠️ **§16 の `MUST NOT` も同じことを4つの動詞で言っている**——「**No tilt, no turn, no cut, no
  reflection.** **This is the shot.**」 **この段落は、その4つをすべて持つ。**
- ⚠️ **残りの危険も、この段落が名指している。** §20——「**The plate may be drawn bending**」
  （→`no plate bending`／`no flexing plate`）、「**The plate may come back down**」
  （→`no plate coming back down`／`no second lift`／`no rocking`）、
  「**A face may be placed**」（→`no face in the frame`／`no chin`／`no hair`／`no shoulder above the cuff`）、
  「**Paper may be added** because every other shot in this section has some — **this one does not**」
  （→`no paper in the frame`／`no sheet of paper`／`no page`）、
  「**The name may become legible**」（→`no legible name text`）。
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

- この仕様を指す欄: `shots/habits-mv-s06.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `鈴木和彦.identity` を含む4点**である
  （`鈴木和彦.identity`／`鈴木和彦.negatives`／`名札`／`名札.appearance`）。
  ⚠️ **顔を置かない1本が `identity` を持つのは、指の造形のためである**（動画の仕様 §6）。
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した一枚を渡す）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⚠️ **この1本の人物は、第四巻の人物である。** 記録の頭——「**鈴木和彦は第四巻の人物である**（サブ 2/24）。
  **このサビは巻を混ぜている** —— `s02`〜`s04` は第一巻、`s05` は第一巻、`s06` は第四巻。
  ⚠️ **これは事故ではなく、この作品の設計である。** MVは六十三話の要約ではない——
  **問いは巻に属さない。**」
  ⛔ **ゆえにこの1枚の手は、`s05` の手と別の人物のものである**——**それでも、同じ様式の同じ描き方である。**
- ⚠️ **食い違い（読み取り・裁定は著者のもの）。** 記録の `unit.before` は「手のひらが、
  **机の面についている。**」と言うが、動画の仕様の画面は**左袖と名札**であり、§4 `Environment Elements`
  は「**左袖、名札、そして名札の下の縫い目**」の3つだけを挙げる（**机の面は挙げていない**）。
  ⛔ **この1枚は、動画の仕様の側で書いた**——**机の面を描いていない。**
- ⚠️ **食い違い2（読み取り）。** 動画の仕様 §13 の `Base Lighting` は
  「**the paper is the brightest thing in the frame**」と言うが、**§16 は同じ仕様の中で
  「No paper in this shot」と明記している。** **この1枚で最も明るいのは、浮いた縁の下の布である**
  （上の `LIGHT` はそう書いた。§16 `PREFER`——「**the seam and the lit cloth under it as the
  frame's only bright passage**」）。
  ⚠️ **同じ定型は `s05` の §13 にも在り、s05 の画面にも紙は無い**——**同じ食い違いが2本で起きている。**
- ⛔ **この1枚は、まだ投入されていない。** 実測（2026-09-28）——`specs/image/` に在る画像は
  `01_ChatGPT Image 2026年9月28日 05_34_07.png` と `02_ChatGPT Image 2026年9月28日 05_36_27.png`
  の2枚であり、`media/` に在るのは動画3本だけである。**この1本の分は、まだ無い。**
  **`attached` を書くのは、送った日である。**
