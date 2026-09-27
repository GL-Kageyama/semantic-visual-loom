# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第三のショット「口が、字の形をなぞって動く」（所作 / motion / 10.000s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、この作品で3番目に「顔の側」を写す1枚である。** `s01` が手を、`s02` が目を置き、
**この1本は口を置く**——動画の仕様 §1 は「**a mouth moves through the shapes of characters and
closes without making a sound**」と言う。⚠️ **顔そのものは、まだ置かれない**——
`bible.constants.顔`「**呼ばれた後にだけ置かれる。手が先にあり、顔が後に来る。順序は入れ替えない。**」
の3歩目であり、**順序の側は動かしていない。**
⛔ **この1本に手は入らない。** 動画の仕様 §16——「**No hand enters this shot.** The hand belongs to
`s01` and returns in `s11`.」
⚠️ **この1枚は、この1本の終わりの状態を写す。** `unit.after` は
「**口が字の形をなぞって動き、また閉じる。音は、まだ出ない。**」である——**渡すのは開始のコマではない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **1本目・2本目と同じ組である。** `specs/video/habits-mv-s03.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` を名乗り、§2 `Visual Language` は
    「**Luminous realist anime, translated into the lower half of a face above a page.**」
    ——**動画の側が、この1本でも既に「顔の下半分へ翻訳した」と書いている。**
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s03.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/prompt.md`
  と**凍結した二枚**（設定画＋表情シート）。⚠️ **この1本は `identity` を添付する側である**
  （動画の仕様 §6——「**この1本は `identity` を添付する** — 口を置く1本である」）。**ゆえに絵の側でも渡す。**
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
  **和が、そのまま下の7欄である**（実測 2026-09-28、`s01`・`s02` の2枚で確認。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s03` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「閉じた口」を写すのは、そのためである**——**渡すのは、この1本が終わった
  あとの状態＝世界の側であって、開始のコマではない。** ⚠️ **動画の仕様 §17 は「**The lips close on
  the last frame**, and the closing is the change.」と言う**——**閉じることは、この1枚からは読み取れない。
  ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s03.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **この1本の1枚は、まだ無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` には `[名前: …]` の註を書く**（`s01` と逆であり、`s02` と同じ側である）
——**この1本には、置かれる人が居る。** ⚠️ **ただし註は「名指す」だけで、外見を書き起こさない。**
理由は下の節に書く。

- `SCENE`: the third step — the shapes of characters have crossed the lips one after another and the mouth is closing on the last of them; no sound is made
- `CHARACTERS`: `[碓氷千夏: **the frozen setting sheet holds her face** — the name is here only so the right sheet is taken, and no appearance is re-derived in words]` — **only the mouth is in the frame**, with the shadow under the lower lip; **no eyes, no brow, no face above the mouth**, the head does not tilt, and no hand is in the frame
- `SUBJECT`: the lips closing on the last of the shapes they have crossed, and the line of writing below them
- `ACTION`: having crossed the shapes without a gap — the lips coming to a close on the last of them, the jaw moved very little, the breath passing as air and no voice made of it
- `LOCATION`: the opened page of the attendance register on the desk at the end of a working day, 2026 — **the page below, seen from the side of the face**, with the desk's worn face barely outside the page
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling so that the mouth's own shadow lies under the lower lip, the page below brighter than the face, bloom on the pale surface, the paper the brightest thing in the frame, and everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the red inside the lips — the only place in a frame of skin, page and ink where the palette has any red in it at all

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the third step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of the lower half of a face above the opened page of an attendance register, on a desk in a school staff room at the end of a working day, with the lips closing on the last of the shapes of characters they have crossed and no sound made of the breath. Only the mouth is in the frame: the upper lip and the lower lip, the corners of the mouth, the shadow under the lower lip, and the dark inside the lips — no eyes, no brow, no face above the mouth, and no hand anywhere in the frame. The shapes have crossed the lips one after another without a gap and the mouth is closing on the last of them; the jaw has moved very little and the lips have done the work, and the breath that passes them is air only — nothing has been said. The page below is the same opened register: cloth over board, the thickness of a register's left sleeve, a bound spine, its fore-edge layered cream and not smooth, and on it the transfer column is on screen with characters written in ink by more than one hand, present and not readable, the marks of cut print and of ballpoint and of pencil drawn as the three different marks they are and none of them legible. The mouth is in the upper third of the frame and the page is below it, so that the shapes are made above the writing they belong to and never touch it. The room's light is a fluorescent tube above and behind the camera, falling flat across the page and blooming on the pale surface, so that the mouth's own shadow is under the lower lip and the page below is brighter than the face; the paper is the brightest thing in the frame, the tube is the only light, and everything the desk edge shadows has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette narrows to skin, to page and to ink, and the inside of the lips is the only place in the frame with any red in it at all. Layered atmospheric depth from near to far; dust suspended and individually rendered in the air above the page where the tube catches it, and moving in front of the mouth where the breath passes it, and it is the only thing in the frame that is still moving. Low visual density: one focal point, the lips and the page below them, with generous negative space and most of the frame given to the page. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at desk height, looking slightly down, holding the mouth and the page in one frame, the page square to the frame with its closed edge toward the camera. One scene, one staging; the same page, the same tube and the same lower half of the face wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no voice, no whisper, no breath that becomes a word, no spoken line, no audible speech, no mouth shaped around a spoken word, no smile, no tightened mouth, no expression, no tears, no fear, no exaggerated expression, no eyes detailed, no gaze, no face above the mouth, no head tilt, no nod, no bent head, no hand in the frame, no finger, no arm in the frame, no second figure, no person behind the desk, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no insert of the writing, no magnified detail of the characters, no second turn of the page, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この1枚の画面は、口の下半分と頁である。** 動画の仕様 §4——
  「**この1本は頁と口の外へ出ない。**」「**部屋は要らない。**」**空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s03` §2——
  「**Luminous realist anime, translated into the lower half of a face above a page.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**机の上の口が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**（1本目の同じ節を見よ。）

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s03` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **かつ、この1枚は2枚目の「顔の一部」である。** ゆえに `no photographic faces` は
  **この1枚でも強く効く**——**凍結した二枚はアニメの絵であり、実写ではない。**
  動画の仕様 §2 `Rendering` は「**Skin is drawn smooth and matte, without pores or specular noise.**」
  と言う——**肌を実写の肌にしないことが、この1本では特に要る。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、この口が実写になる。**（1本目の同じ節を見よ。）

## ⚠️ 名前の註は書くが、外見は書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**。
  `s02` とこの1本は書く）。
- ⛔ **だが、外見を書き起こさない。** 動画の仕様 §3——
  「**凍結した二枚が外見である。**」「**この1本が置くのは口の側だけである** — 上唇と下唇、口角、
  顎の下の影、そして唇の内側の暗さ。」 そして §6 の Reference は、凍結した二枚を `CRITICAL` として指す。
- ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな顔か」を教えることではない。**
  この1本では**その仕事を、添付された凍結の二枚が負う**——**ゆえに註は名指すだけである。**
  ⛔ **註に置くのは、名と「凍結した二枚」の指し先だけである。** ⚠️ **年齢も、性別も、職業も置かない。**
  `projects/habits/ledger.yaml` は「**外見の記述は出典に一行も無い**（方針 §5a）」と言う。
  ⛔ **訂正。** 私は一度ここに「**この作品の動画の仕様27本は、年齢も職業も1字も持たない**」と
  書いた——**誤りである。** 実測（2026-09-28、走査し直した。計器は `[0-9]+歳` と職業語の `grep`）：
  **年齢の語を持つ動画仕様は 2/27 本**（`s06`・`s07`——`52歳`・`45歳`）、
  **職業の語を持つものも 2/27 本**（**同じ2本**——`運転士`・`部門`）。⚠️ **私は「10代」の語を数えて、
  「年齢と職業が無い」と主張していた**——**測った範囲と、主張した範囲が違っていた。**
  ⛔ **この訂正自身も、一度誤った。** 私は「年齢 3/27・職業 4/27」と書いた——
  **外れの一語ずつに理由がある**：`s01` は**私が同じ日に書き足した `女33`** の行で数えられ
  （**自分が今足した語を検索語にすると必ず当たる**）、`職員` は **`職員室`（部屋）** を数えていた。
  ⛔ **結論は変わらないが、理由が違う。** **`CHARACTERS` は註ではなく、生成器へ渡る文字列である**
  ——**書けば描かれる。** 動画の仕様が年齢を書くのは**出典についての日本語の散文**であり、
  **同じ欄が画像では英語の入力になる。** ⚠️ **同じことを書いても、行き先が違う。**
  ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**
  ——**黙ってやらず、ここに書く。** `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `identity` を添付する側である——この1枚が、その一枚である

- `s01` は `碓氷千夏.identity` を**意図的に持たなかった**（「人のかたちの一枚を渡せば、生成器は顔を置く」）。
  ⛔ **`s02` とこの1本は逆である。** 動画の仕様 §6——「**この1本は `identity` を添付する** —
  口を置く1本である。⚠️ **表情シートを添付する意味が、この1本で最も大きい**：口は表情の側にある。」
- ⚠️ **ゆえに、この1枚は「人のかたちの一枚」そのものである。** **この1枚が外れれば、
  `s03` と `s04` の口が同じ人物の口でなくなる**（動画の仕様 §15 Identity——
  「**Must preserve** — `s03` の口と同じ口であること。」）。
  ⛔ **この1枚の外れは、1枚で終わらない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **この1本の動画の仕様は、その危険を自分で名指している。** §20 の1番目——
  「**A voice may be produced.** ⚠️ **The first risk of this shot, and the one that would cost the
  work most.** A generator asked for a moving mouth will often supply audible speech or a whisper.
  **`no calling voice as a sound effect` is in the slot this route reads as prose** — the guard is
  the Master Prompt's own sentence.」
  ⛔ **画像の側では、その `Negative` が止める。** §16 の `MUST NOT` は
  「**No voice, no whisper, no breath that becomes a word.**」を持ち、**この段落も同じ行を持つ**——
  **同じ床を、効く場所へ置いたものである。**
- ⚠️ **そして、この1本には既に絵の側の実測が在る。** `s03` の動画は 2026-09-28 に送られており、
  §20 の `Observed Problems` が言う——「**左の頁の手書きが、ラテン文字の草書として戻った** ——
  日本語の字ではない。§18 は `no real-world alphabet` を**既に持っていた**——**この経路では散文として
  読まれた**（`L30`）。」**字を描く1本では、否定は効いた場所に置かねばならない。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。** ⚠️ **要求を節に割れば5節であり、この段落はその5節を
  すべて文字として持つ**（`no watermark`／`no on-screen subtitles`／`no background music`／
  `no calling voice as a sound effect`／`no face before the name is called`）——
  **数えたのは私であり、照合するのは `L21` である。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s03.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `碓氷千夏.identity` を含む4点**である
  （`碓氷千夏.identity`／`碓氷千夏.negatives`／`出席簿`／`出席簿の転出欄`）——**`s01` と逆であり、
  `s02` と同じ側である。** ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した二枚を渡す）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** 実測（2026-09-28）——`specs/image/` に在る画像は
  `01_ChatGPT Image 2026年9月28日 05_34_07.png` と `02_ChatGPT Image 2026年9月28日 05_36_27.png`
  の2枚であり、`media/` に在るのは動画3本だけである。**この1本の分は、まだ無い。**
  **`attached` を書くのは、送った日である。**
