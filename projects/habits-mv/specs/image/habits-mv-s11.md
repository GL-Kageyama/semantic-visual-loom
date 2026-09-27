# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十一のショット「三つが続けて起きる——手、目、口」（所作 / motion / 7.101s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この5本（`s11`〜`s15`）は、この稿で初めて書かれる。** 実測——この稿を書くために
開いた時点で、`shots/habits-mv-s11.yaml`〜`habits-mv-s15.yaml` の**どれも `key_image` を
持っていなかった。** ゆえに `L18` の「`key_image` が読めない」は、**この5本で5つ減る。**
⚠️ **記録が無いのであって、食い違っているのではない**——**だから違反ではない。**
**だが、この5本の画像の側は一度も検査されていない。**
⚠️ **この1本は、この作品で三つ目の「机の上の手」である。** 動画の仕様 §10——
「**close, at the desk** —— **`s01` の机の手、`s05` の左袖と並ぶ、この作品の三つの現場のうちの机である**」。
⛔ **この1本は、その三つの現場のどれでもない1本である**——**手・目・口が一人の中で続けて起きる**
（§3——「**この1本は、その三つを一人で、一本の中で行う**」）。**ゆえにこの1枚も、顔を置く。**
⚠️ **この1枚が写すのは「三つの動き」ではない**（下の節に書く）——**止まった1枚である。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s11.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a hand and a face over a stack on a desk.**」
    ——**動画の側が先に、この様式を「机の上の手と顔へ翻訳した」と書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s11.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/05_篠原麻衣/prompt.md`
  （凍結した設定画の読み。「出典の語」の節）と、同じ作品の既存の生成物（`media/` の動画3本）
- 添付する参照: **`specs/image/生成時参照イラスト/s11/` の1枚**——`篠原麻衣_設定画.png`。
  ⚠️ **この1枚は、この作品の動画の側の同じ1枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s11/`。実測 2026-09-28、ハッシュが一致した）。
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
  **和が、そのまま下の7欄である**（実測 2026-09-28、`s01`・`s05` の2枚で確認）。
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** 様式カードの雛形は
  `Not photorealistic, …` で終わるが、**この作品はそれを2段落目に置く**——**この作品は実写ではない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s11` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s11.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⚠️ **実測（2026-09-28、この稿を書く時点）**——`media/` に在るのは動画3本
  （`01_4400c8e6…mp4`・`02_c544590b…mp4`・`03_083a2440…mp4`）であり、
  `takes/` に在るのは `habits-mv-s01-video-1.yaml`・`s02-video-1`・`s03-video-1` の3本である。
  ⛔ **この5本（`s11`〜`s15`）の分は、動画も画像もまだ無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の註は、この1本では「顔」の側である**——**この1本は顔を置くからである**
（動画の仕様 §10——「**the hand and the face are in one frame**」／§16 `MUST NOT`——
「**No face other than this one, and no second person.**」）。
⛔ **註に置くのは、人物の名と、凍結した一枚を指すことだけである。****外見は書き起こさない**
（理由は下の節に書く）。

- `SCENE`: the eleventh step, and the work's first shot where three movements happen in one person — a right hand has taken one sheet off a stack, an eye has dropped to it, and the mouth has closed on nothing
- `CHARACTERS`: `[篠原麻衣: **the frozen setting sheet holds her face** — the name is here only so the right sheet is taken, and no appearance is re-derived in words]` — **the hand, the eye and the mouth are the whole figure in the frame**; **no second face, no second person, no standing figure behind the desk**, and the stack fills the frame's lower half
- `SUBJECT`: the one sheet held clear of the stack, and the face above it with its eye down and its mouth shut
- `ACTION`: having taken one sheet — the hand arrived on the stack and lifted one sheet clear of it, the eye dropped to the sheet in the same movement, the mouth shaped characters once and closed; **the three are finished and none of them is repeated**
- `LOCATION`: a desk carrying a stack of paper, in the middle of a working day, 2026 — the desk's worn wooden face with the polish of forearms on it, the stack squarish but not squared with its cut edge layered and countable at this distance, **the stack one sheet thinner than it was**, and nothing else on the desk
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling even across the desk and the paper, the light the tube lays between the pages still on the sheet's underside where it came up, **the paper the brightest thing in the frame**, bloom on the pale surfaces, everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the cream of the stack's cut edge and the skin of the one hand — the only warm things the tube finds in a narrow, cold room

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the eleventh step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of one sheet held clear of a stack of paper on a desk, and the face above it with its eye down on the sheet and its mouth closed, in the middle of a working day, 2026. The stack lies on the desk squarish but not squared, cream and the same cream as every other paper in this work, its cut edge layered and countable at this distance, and it is one sheet thinner than it was; the desk is wood with the polish of forearms on it, and its worn edge is in the near foreground. The hand is a right hand and a hand only — it holds the one sheet clear of the stack and does not turn it, the wrist is not lifted, and no arm is in the frame. The face is above the sheet and behind it, one eye down on the page and the other not on it, the mouth shut and not shaping a word; it carries no expression beyond attention — no smile, no tears, no fear, no exaggerated expression — and it is the only face in the frame. No second person is in the frame, no standing figure behind the desk, and no head other than this one. The writing on the sheets is present and cannot be made out: characters written in print and in ballpoint and in pencil, drawn as the three different marks they are, set in the Japanese script, and none of them legible; the sheet in the hand is not read, no finger tracks a line down it, and the eye takes nothing off the page. The room's light is a fluorescent tube above and behind the camera, falling flat and even across the desk and the paper and blooming on the pale surfaces; the light the tube lays between the pages is still on the sheet's underside where it came up, the paper is the brightest thing in the frame, the tube is the only light, and everything the desk edge shadows has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette is narrow and cold — fluorescent white, the cream of the stack, the grey of the desk — and the warm side is reduced to one hand and to the paper itself. Layered atmospheric depth from near to far; dust suspended and individually rendered in the air over the stack where the tube catches it, and it is the only thing in the frame that is still moving. Low visual density: one focal point, the sheet and the face above it, with the stack filling the frame's lower half and generous negative space above the head. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at desk height and close, placed so that the hand and the face are in one frame, the stack square in the lower half of the frame and the face above it, and the camera does not travel. One scene, one staging; the same desk, the same stack and the same tube wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no second face, no second person, no standing figure behind the desk, no head other than this one, no open mouth, no parted lips, no speaking mouth, no whispering mouth, no breath that becomes a word, no spoken word, no sound from the mouth, no second sheet taken, no second sheet in the hand, no lifting of the stack, no sorting of the stack, no squaring of the stack, no turning of the sheet, no second movement of the hand, no arm in the frame, no wrist lifted, no finger tracking a line, no reading, no finger under the characters, no insert of the writing, no magnified detail of the characters, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no second object on the desk, no mug, no pen cup, no terminal, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」。
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」
  と言い、まとめは「**the light, not the character, is the subject**」である。
- ⛔ **この部屋に、空は無い。** **この作品の光は、天井の蛍光灯1本である**
  （`s11` §13——「Fluorescent over a working desk in the middle of the day」）。
  ⚠️ **この1本は、三つが一人の中で続けて起きるので、カメラが手と顔の両方を受ける**
  （§10）——**顔が入るからといって、空が入る余地は構図の側に無い。** 顔の後ろは机であり、
  机の向こうは部屋である。**この作品は、その部屋を写さない。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s11` §2——
  「**Luminous realist anime, translated into a hand and a face over a stack on a desk.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**机の上の一枚が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s11` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⛔ **この1本は、この作品で顔が机の上に在る最初の1本である。**
  動画の仕様 §20 の6番目は「**The face may be given an expression** that the frozen sheet does
  not carry.」と言う——**実写の顔が戻れば、この1本は表情の話になる。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、机の上の顔が実物になる。**（1本目の同じ節を見よ。）

## ⚠️ 註が教えるのは「誰か」だけである——年齢も、性別も、職業も、外見も、書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う——
  **隣の作品はそれを書き、その註を `Prompt` の中にも置いている。**
- ⛔ **この1本には、置かれる人が居る**（ゆえに註は書く）——**だが、註に置けるのは名と、
  凍結した一枚を指すことだけである。**
  ⛔ **年齢も、性別も、職業も、外見も、註に置かない。**
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
- ⚠️ **もう一つの理由は、この作品の側に在る。** `ledger.yaml` は
  「**外見の記述は出典に一行も無い**（方針 §5a）。**凍結した二枚が外見である。**」と書き、
  動画の仕様 §3 も「**外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。**」と書く。
  ⛔ **註が作品の正典より多くを持つなら、その註は新しい事実になる**——**註は記録ではなく、指示である。**
- ⚠️ **この作品の凍結した一枚は、読みと註を持つ**——`サブ/05_篠原麻衣/prompt.md` の
  「出典の語」の節である。**そこに在るのは、呼ばれ方と、癖と、動きの署名と、記名であって、
  髪の色でも、背の高さでもない。** ゆえにこの1枚も、**顔の造形を語で書き起こさない。**
  **語が無いところでは、書かないことが仕様である。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ この1枚は「三つの動き」を写せない——止まっている1枚である

- この1本の主題は**三つが続けて起きること**である（`s11` §1——「**a hand takes a sheet, an eye
  drops to it, and a mouth moves once**」）。**ゆえにこの1本の変化は、時間の側にしか無い。**
- ⛔ **止まった1枚は、順序を写せない。** この1枚に写るのは**三つが終わったあとの状態**である
  ——記録の `unit.after` は「手が止まり、**口が閉じている。音は、出ていない。**」。
  ⚠️ **動画の仕様 §7 の `Pull` も同じことを言う**——「**The mouth closes and no sound comes out.**
  **The shot ends where the three shots before it ended.**」
- ⚠️ **ゆえにこの1枚は、口を開けない。** `Negative` に `no open mouth`／`no parted lips`／
  `no speaking mouth`／`no breath that becomes a word` を置いたのは、そのためである——
  **開いた口を描けば、順序が「口」で止まり、`s04` と同じ結末が消える。**
  ⚠️ **三つが続けて起きることは、この1枚からは読み取れない。ゆえに変化は、動画の側に残る。**
- ⚠️ **かつ、この1枚は「動きの無い1枚」ではない。** §11 `Environmental Motion`——
  「**Dust moves over the stack and catches the tube. It keeps moving after the mouth has closed.**」
  **塵は、この1枚の中でも動き続けている。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **この1本は、その危険が最も大きい2つを同時に持つ。** §20 の1番目——
  「**The shot may be cut into three.**」は動画の側の危険であるが、同じ節の4番目
  「**The writing may become legible** at this distance, **where the face and the page share a
  frame**」は、**この1枚の危険である**——机の上の1本のうち、**顔と紙が同じ枠に入るのは、
  この1本だけである**（§10）。
  ⛔ **画像の側では、この段落がそれを止める**——**`no legible name text` が、この1枚の中心の禁制である。**
- ⚠️ **絵の側の実測が、既に在る。** `s03` の動画は 2026-09-28 に送られ、§20 の `Observed Problems` が言う
  ——「**左の頁の手書きが、ラテン文字の草書として戻った** ——日本語の字ではない。§18 は
  `no real-world alphabet` を**既に持っていた**——**この経路では散文として読まれた**（`L30`）。」
  **ゆえにこの段落にも `no Latin cursive` を置く。** **字を描く1本では、否定は効いた場所に置かねばならない。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。** ⚠️ **要求を節に割れば5節であり、この段落はその5節を
  すべて文字として持つ**（`no watermark`／`no on-screen subtitles`／`no background music`／
  `no calling voice as a sound effect`／`no face before the name is called`）。
- ⛔ **そして、この段落は共有の尾から1節を落としている**——`no stack of paper` である。
  ⛔ **この1本の主題は、まさにその束である**（§5——「**束** — 机の上で揃っていない。**一枚が取られる。**」）。
  **尾は27本で共有されているが、その1節だけは、束を主題に持つ1本では主題を禁じてしまう。**
  ⚠️ **尾の目的は「机の上に二つ目の物を置かない」であって、「紙を描かない」ではない**——
  **この1本では、前者は `no second object on the desk, no mug, no pen cup, no terminal` が負う。**
  **ゆえに落としたのは1節であり、他の36節は一字も動かしていない。** 下の「記録との対応」に経緯を残す。

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s11.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `篠原麻衣.identity` を含む4点**である
  （`篠原麻衣.identity`／`篠原麻衣.negatives`／`束`／`束.appearance`）。
  ⚠️ **この1本は顔を置くので、`identity` を添付する側である**（動画の仕様 §6——
  「**この1本は `identity` を添付する** — **手・目・口を一人で持つ1本である。**」）。
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した一枚を渡す）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⚠️ **凍結した一枚の道を、ここに実測で固定する。** この1本が `identity` として添付する一枚は
  `distill-essence-engine/examples/habits/character/サブ/05_篠原麻衣/ChatGPT Image 2026年9月21日 00_44_21.png`
  である（実測 2026-09-28、`ls` で確認——`サブ/05_篠原麻衣/` の中身は、この PNG と `prompt.md`
  の2つだけである）。⚠️ **この道は、動画の仕様 §6 と `ledger.yaml` の `identity` の両方と一致する。**
- ⚠️ **動画の仕様 §3 の `Reference:` の行は、道もファイル名も誤っていた**——§6 とは別の人物の
  フォルダを指していた。⚠️ **この稿を書いている時点で、著者の側が直している**（`s11`〜`s15` の5本）。
  ⛔ **誤っていた名前をここに写さない**——**消えた名前を引用に残せば、直っていないように読める。**
  ⚠️ **画像の側が取る一枚は、上の1行だけである。**
- ⚠️ **食い違い2（床に受け継がれた行）。** 27本で共有されている `Negative` の尾は
  **`no stack of paper` を持つ**——⚠️ **この1本の主題は、まさにその束である**
  （`s11` §4——「**全巻を貫く小道具の現場である** — 束」／§5——「**束** — 机の上で揃っていない。
  **一枚が取られる。**」）。⛔ **尾はこの作品の共有の枠であり、束を持つ3本
  （`s11`・`s24`・`s25`）は、その枠の中に自分の主題を禁じる行を持っている。**
  ⚠️ **私は尾を1語も変えずに置いた**（枠を薄めれば、この作品で唯一効く否定が痩せる）——
  **裁定は著者のものである。**
- ⚠️ **記録の `attached` の註は、まだ「この作品はまだ1本も生成していない」と言う**
  （`shots/habits-mv-s11.yaml`）。⚠️ **動画の仕様 §20 も同じことを書く**——
  「実測 2026-09-28——`media/` に曲は在るが、`takes/` は無く、機体へ届いたバイトは0である」。
  ⛔ **だが、いまの状態はそうではない**（実測 2026-09-28、この稿を書く時点——
  `media/` に動画3本、`takes/` に3本）。**その3本は `s01`・`s02`・`s03` である。**
  ⚠️ **この5本は、その3本に入っていない**——**つまり、この1本についての古い註は正しいが、
  作品についての古い註は正しくない。** この1枚は、`media/` の側については何も主張しない。
- ⛔ **この稿の文字列は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
