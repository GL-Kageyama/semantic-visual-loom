# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第二のショット「目が、一行を左から右へ渡る」（所作 / motion / 9.015s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚は、この作品で最初に「顔の側」を写す1枚である。** `s01` は手だけを写し、
**この1本は初めて目を置く**（動画の仕様 §1——「**still not a face but a part of one**」）。
⛔ **ゆえに、この1枚は人のかたちの一枚を添付する側である**——`s01` と**逆**である。
⚠️ **隣の1枚（`habits-mv-s01`）と、答えが3箇所で逆になる。** どれも下の節に書く。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **1本目と同じ組である。** `specs/video/habits-mv-s02.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` を名乗り、§2 は
    「**Luminous realist anime, translated into the opened page of a register at the end of a working day**」
    ——**動画の側が、この1本でも既に「頁へ翻訳した」と書いている。**
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s02.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/prompt.md`
  と**凍結した二枚**（設定画＋表情シート）。⚠️ **この1本は `identity` を添付する側である**
  （動画の仕様 §6——「**この1本は `identity` を添付する**」）。**ゆえに絵の側でも渡す。**
- 投入する文: **下の節の1段落目が `Prompt` であり、エンジンの出力であって、`chatgpt-image-2.5` へ
  投入する正典である。****2段落目が `Negative` である**
- ⚠️ **下の7欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`REF_FORMAT` と `REF_STYLE` が「どのカードの穴か」を名乗る。** `L22` がそれを読み、
  **名乗ったカードが実際にその穴を宣言しているか**を確かめる——**名乗りは宣言であって、一致ではない。**
  ⚠️ **この組では、`L22` は鳴らない**（実測 2026-09-28）——`scene-board` の5穴と
  `luminous-anime` の4穴の**和が、そのまま下の7欄である。**
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s02` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「行末で止まった目」を写すのは、そのためである**——**渡すのは、この1本が終わった
  あとの状態＝世界の側であって、開始のコマではない。** **目の「位置」は運動ではない**——
  **行を渡ることは、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s02.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` には `[名前: …]` の註を書く**（`s01` と逆である）——**この1本には、
置かれる人が居る。** ⚠️ **ただし註は「名指す」だけで、外見を書き起こさない。** 理由は下の節に書く。

- `SCENE`: the second step — an eye crosses one line of writing on the opened page from left to right and stops at the end of it; nothing is understood
- `CHARACTERS`: `[碓氷千夏: a girl in her teens, a student — **the face is the frozen setting sheet's and is not re-derived in words here**]` — **only the eye and the side of the brow are in the frame**, above the line; **the rest of the face is not detailed**, the head does not tilt, and no hand is in the frame
- `SUBJECT`: the one eye at rest above a single ruled line it has just crossed, and the line itself
- `ACTION`: having crossed the line and stopped at its end — the eye still, the brow and the mouth held, **one blink placed after the stop**
- `LOCATION`: the opened page of the attendance register on the desk at the end of a working day, 2026 — **almost the whole frame is paper**, with the desk's worn edge in the near foreground
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera lying along the ruled columns and stopping where the fore-edge shadows, bloom on the pale surface, the paper the brightest thing in the frame; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the pale of one eye — the only thing in a page of cream, ruling grey and ink black that is neither paper nor printing nor ink

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the second step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of one eye at rest above a single ruled line it has just crossed, on the opened page of an attendance register, in a desk in a school staff room at the end of a working day, with the pale of the eye as the only thing in the frame that is neither paper nor printing nor ink. Almost the whole frame is paper: the page lies square to the frame and does not move, and the light of a fluorescent tube above and behind the camera lies flat along the ruled columns and stops where the fore-edge shadows. The ruling is printed in thin lines of uneven width, and inside the columns the characters were written in ink by more than one hand — present on screen and not readable, the marks of cut print and of ballpoint and of pencil drawn as the three different marks they are and none of them legible. The line occupies the lower third of the frame and the eye is above it, so that the distance between them is the whole composition; the desk's worn edge is in the near foreground and nothing else is in the frame. Above the line there is one eye and the side of the brow, and the rest of the face is not the subject of this plate and is not detailed; the eye is at the end of the line and is still, the brow is held, the mouth is not in the frame, the head does not tilt, and no hand and no finger enter. The eye has just come along the line from left to right at a rate that did not change, and it is not going on: not decelerating, simply not continuing, and nothing follows it — no recognition, no reaction, no turn. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. Saturated where the light falls and deep cyan in the fore-edge shadow; the palette has narrowed to the page — cream, ruling grey, ink black, and the pale of one eye. The page's fibre and the ink's absorption are both visible at this distance, and the dust suspended in the air above the page is individually rendered where the tube catches it and is the only thing still moving. Very low visual density: one focal point, the line of writing and the eye above it, with the rest of the frame given to blank paper. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at desk height, looking slightly down, the same placement as the shot before it, the page square to the frame. One scene, one staging; the same page, the same tube and the same eye wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no insert of the writing, no magnified detail of the characters, no rack focus onto the line, no finger in the frame, no hand in the frame, no finger tracking the line, no head tilt, no nod, no bent head, no second figure, no person behind the desk, no lifted brow, no narrowed lid, no expression, no smile, no tears, no fear, no exaggerated expression, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies」「Volumetric god rays」
  「Anamorphic lens flare」「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この1枚の画面は、ほとんどが紙である**（`s02` §2——「**Almost the whole frame is paper.**」）。
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s02` §2——
  「**Luminous realist anime, translated into the opened page of a register at the end of a working day.**」）。
  **この1枚は訳文の側に立つ。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**（1本目の同じ節を見よ。）

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s02` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が `not photorealistic` を先頭に持つ側である。**
- ⚠️ **かつ、この1枚は顔を写す最初の1枚である。** ゆえに `no photographic faces` は
  **この1枚でいちばん効く行である**——**凍結した二枚はアニメの絵であり、実写ではない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、この顔が実写になる。**（1本目の同じ節を見よ。）

## ⚠️ 名前の註は書くが、外見は書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**）。
- ⛔ **だが、外見を書き起こさない。** 動画の仕様 §3——
  「**外見の記述は出典に一行も無い**（方針 §5a）。**凍結した二枚が外見である。**」
  そして §3 の Reference は「**the face is theirs and is not re-derived here**」と言う。
- ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな顔か」を教えることではない。**
  この1本では**その仕事を、添付された凍結の二枚が負う**——
  **ゆえに註は名指すだけである。** ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**
  ——**黙ってやらず、ここに書く。** `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `identity` を添付する側である——この1枚が、その一枚である

- `s01` は `碓氷千夏.identity` を**意図的に持たなかった**（「人のかたちの一枚を渡せば、生成器は顔を置く」）。
  ⛔ **この1本は逆である。** 動画の仕様 §6——「**この1本は `identity` を添付する**——
  **目を置く1本である。**」
- ⚠️ **ゆえに、この1枚は「人のかたちの一枚」そのものである。**
  **この1枚が外れれば、`s02`・`s03`・`s04` の顔が同じ人物でなくなる**
  （`s01` §3 の Continuity——「**`s02`〜`s04` の同じ手と一致すること**」）。
  ⛔ **この1枚の外れは、1枚で終わらない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **この1本の動画の仕様は、その危険を自分で名指している。** §20 の1番目——
  「**The writing may be rendered legible.** ⚠️ **The first risk of this shot, and on this route
  the one the `Negative Prompt` cannot stop.**」
  ⛔ **画像の側では、その `Negative Prompt` が止める。** 実測（2026-09-28、動画3本）——
  **机の上の手書きが、日本語の字ではなく、ラテン文字の草書として戻った。**
  **動画の §18 は `no real-world alphabet` を既に持っていた。散文として読まれた。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である。
  **ゆえにこの段落は、動画の §18 の写しではない**——**同じ床を、効く場所へ置いたものである。**
  実測（2026-09-28）——**5節すべてを覆っている。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s02.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `碓氷千夏.identity` を含む**——`s01` と逆である。
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した二枚を渡す）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
