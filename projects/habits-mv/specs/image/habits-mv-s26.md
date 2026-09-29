# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第二十六のショット「手が止まり、頁の上を光が渡る」（余白 / still / 9.506s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
⚠️ **そして `mode: still` のショットにも、画像は要る**——**この1本が、この作品で最初の `still` である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、この作品で最初の `mode: still` である**（`shots/habits-mv-s26.yaml`——
「✅ **この1本が、この作品で最初の `mode: still` である。**」）。
⚠️ **`still` は「画面が止まる」ではない**——**止まるのは主題（碓氷千夏の手）であり、光と埃は動き続ける**
（`shot-record.schema.json` の `mode` の註）。9.506秒。⛔ **ゆえにこの1本の1枚にも、埃が要る。**
⚠️ **この1本は `s01` と同じ場所へ戻る。** `s26` §4——「⚠️ **`s01` と同じ現場である** ——
`出席簿の転出欄`。**この作品は、ここへ戻る。** **開いた頁は、閉じられない。**」
⛔ **「戻る」は「同じ1枚を作る」ではない。****下の節に、違えてはならないものと、違えなければならないものを書く。**
⚠️ **参照集合には `碓氷千夏.negatives` だけが入っている**（`s26` §3）——**設定画は渡さない。**
**この1本は手だけを写す。****ゆえにこの1枚にも、`[名前: …]` の註を書かない**（下の節）。
⚠️ ⚠️ **この1本と `s27` で、歌はもう終わっている。** **画面は、曲のあとに残る。**
`bible.song.lines` の `l31`（155.505秒）は「**光が、紙の上に落ちている。**」であり、
**この2本が、その一行の2本である**——9.506秒＋14.309秒＝23.815秒は `outro` の尺そのものである
（`shots/habits-mv-s26.yaml` の頭）。⛔ **この1本は、この作品で歌の無い画面である。**
⛔ **この1本は `ledger.disclosure` の変化点ではない**（台帳の3点は `s10`・`s17`・`s18`）。
**この1枚は、明かす1枚ではない。****明かすものが、もう残っていない1枚である。**
⚠️ **この1本は、この作品の夕方の8本のうちの1本である**（実測 2026-09-28——`shots/*.yaml` の `time` を
数えた：`勤務日の夕方` が8本＝`s01`〜`s04`・`s17`・`s18`・`s26`・`s27`／`勤務日の日中` が19本。8＋19＝27）。
**`s01` も同じ8本の中に居る**——**ゆえにこの1本は、同じ時刻へ戻っている。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/seedance-2.5/habits-mv-s26.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a page with a hand resting on it.** **The light, not the
    figure, is the subject** — and here the light is the only thing that moves, so **the shot's art
    direction is the art direction of a still surface under a live tube.**」
    ——**動画の側が先に、この様式を「手の載った頁へ翻訳した」と書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s26.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/prompt.md`
  （凍結した設定画の読み。⚠️ **但しこの1本には添付しない**——**読むのは、禁制の側が何を禁じるかを
  確かめるためである**）と、**同じ場所の別の1枚**——`specs/image/habits-mv-s01.md`（⚠️ **この作品で
  唯一、この現場の1枚である。** **この1枚は、その1枚と並べて読まれる**）
- 添付する参照: **無い。** ⛔ **`specs/image/生成時参照イラスト/` に `s26` のフォルダは無い**
  ——**この1本の `reference_set` は `碓氷千夏.negatives` だけを挙げ、`identity` を挙げないからである。**
  ⚠️ **不在は、置き忘れではない。** 動画の側も同じである（`specs/video/生成時参照イラスト/` にも `s26` は無い）。
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
  `references/formats/scene-board.md` は `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT` を、
  `references/styles/luminous-anime.md` は `SUBJECT`／`ACTION`／`LOCATION`／`ACCENT` を宣言している）。
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** 様式カードの雛形は
  `Not photorealistic, …` で終わるが、**この作品はそれを2段落目に置く**——**この作品は実写ではない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s26` §6——この27本は「参照画像」の型である。
  **`first_frame` ではない**）。⚠️ **この1枚が「止まった手と、渡り終えた光」を写すのは、そのためである**
  ——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  ⚠️ **但し、この1本では開始のコマと終わりのコマが1つの点で違う**——**光の縁が、頁の上に在るか、
  既に渡り終えているかである。****下の節に、どちらを写したかを書く。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** この作品の前提は「名は、どこにも読めない」である
  ——**文字列に日本語の字を置けば、置かれる側へ回る。** ⚠️ **この1本の2段落には、日本語の字が1つも無い。**
- 記録: `shots/habits-mv-s26.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`LOCATION` と `LIGHT` の2欄は、`s01` の同じ欄と1字も違わない**（実測 2026-09-28、この2枚を
並べて数えた）——**この1本が「同じ場所へ戻る」とは、まずこの2欄のことである。**
⚠️ **`CHARACTERS` には、カードが求める `[名前: …]` の註を書かない。** 理由は下の節に書く。

- `SCENE`: the return — the transfer column of last year's register, open on a desk at the end of a working day, one hand at rest on the page and the tube's light crossing it; **nothing in the frame moves but the light and the dust**
- `CHARACTERS`: **one right hand, and no one in place** — the back of it, the knuckles, the nails cut short, a small thickening on the first joint of the right middle finger where a pen rests, the plain cuff of a white shirt at the wrist; **no head, no shoulder, no standing figure behind the desk** — **no name is given to the model, because a name brings a person**
- `SUBJECT`: the open page and the one right hand at rest on it — **the hand, the paper and the light, and nothing else in the frame**
- `ACTION`: the light crossing — the tube's edge travelling across the open page from one side to the other and leaving, with the hand at rest on the page through all of it and the page not turning; ⛔ **the subject is still: the hand does not move at all, and nothing is being held down or lifted**
- `LOCATION`: a desk in a school staff room at the end of a working day, 2026 — the desk's worn wooden face, a drawer closed, the back of a chair; **nothing else on the desk**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling across the register and the page, bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the cream of the page edge and the one hand at rest — the only warm things the tube finds in a narrow, cold room

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of an open school attendance register on a desk at the end of a working day, 2026, with one hand at rest on the open page and the light of a fluorescent tube on it. The register lies square to the desk's edge, cloth over board, the thickness of a register's left sleeve, a bound spine, its fore-edge layered cream and not smooth; it is open at the transfer column and the page lies settled on the block, flat and not standing on its own edge, and the hand that opened it is still on it — a right hand, and a hand only: the back of it, the knuckles, the nails cut short, a small thickening on the first joint of the right middle finger where a pen rests, the plain cuff of a white shirt at the wrist — the pads of the fingers resting on the page and not pressing it, and nothing being held down and nothing being lifted. On the page the transfer column is on screen: characters written in ink by more than one hand, present and not readable, the marks of cut print and of ballpoint and of pencil drawn as the three different marks they are and none of them legible. No head is in the frame, no shoulder, no standing figure behind the desk, and there is nothing else on the desk: no mug, no pen cup, no terminal, no stack of paper. The desk is wood with the polish of forearms on it, and its worn edge is in the near foreground. The writing is not read: no eye is in the frame, no head bends over the page, and no finger tracks a line down it — and the page is not turned. The room's light is a fluorescent tube above and behind the camera, falling flat across the register and the page and blooming on the pale surfaces; the paper is the brightest thing in the frame, the tube is the only light, and everything the desk edge shadows has gone to deep cyan. The tube's edge has finished crossing the page and gone, and the page is evenly lit again. Dust is suspended in the air above the desk where the tube catches it and is individually rendered, and it is the busiest thing on screen. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette is narrow and cold — fluorescent white, the grey-green of the cover with its cloth weave, the cream of the page edge — and the warm side is reduced to one hand and to the paper itself. Layered atmospheric depth from near to far. Very low visual density, and falling: one focal point, the open page and the hand at rest on it, with generous negative space and most of the frame given to the desk. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at desk height, looking slightly down, the register square in the frame with its closed edge toward the camera. One scene, one staging; the same desk, the same tube and the same hand wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no head, no shoulder, no standing figure, no person behind the desk, no second figure, no second hand, no moving hand, no raised fingers, no gripping, no pressing fingers, no holding down, no arm beyond the cuff, no closed cover, no closed register, no turned page, no standing page, no second turn of the page, no lifting of the register, no carrying of the register, no reading, no eye in the frame, no head bent over the page, no finger tracking a line, no glow on the page, no flare across the page, no colour change across the page, no flicker, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan shadow**」。
- ⛔ **この部屋に、空は無い。** **この作品の光は、天井の蛍光灯1本である**
  （`s26` §13——「Fluorescent over a working desk at the end of the working day」。
  「**outside there is nothing left to see**」）。⚠️ **この1本は、この時刻（`勤務日の夕方`）に
  ついて、時刻を絵にしろとは一度も言っていない**——§16 `MUST NOT` は
  `no wall clock, no calendar, no digital timer, no date stamp` を持ち、§15 `Temporal` は
  「**Nothing in frame supplies a date.**」と言う。**ゆえに夕方は、この画面の外にある。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**（決定D——`style` は「誰の声か＝語彙」、
  「何を見せるか」は `format` の側である）。**ゆえに、この1枚が様式から取るのは**——clean anime
  lineart・cel shading・単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
- ⚠️ **この作品は、この1本でも既にその翻訳を書いている。** `s26` §2——
  「**Luminous realist anime, translated into a page with a hand resting on it.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**机の上の1本が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**（`s01` の同じ節を見よ。**同じ理由である。**）

## ⚠️ 止まるのは手であって、画面ではない——この1枚は「静止画の見本」ではない

- ⛔ **この1本が `mode: still` であることは、この1枚が「止まった絵」であることを意味しない。**
  `s26` §16 `MUST NOT` は `no static slideshow of stills, no floaty weightless motion` を持ち、
  §15 `Motion` は「**The stillness is a live frame** — **dust and light move through all nine and a
  half seconds.**」と言う。**止まるのは主題（碓氷千夏の手）である。**
- ⚠️ **この作品の運動の床は、この1本でも床である。** `s26` §4 `Environmental Behavior`——
  「**埃が、頁の上を渡る。** ⚠️ **この1本の運動の半分は埃である** —— **`mode: still` の画面が
  静止画にならないのは、埃と光が動き続けるからである。**」
- ⚠️ **ゆえに、この1枚には埃が要る。** そして `s26` §2 `Texture` は、その埃を**この1本で
  いちばん強い位置に置いている**——「dust suspended and individually rendered, **and in this shot
  the dust is the busiest thing on screen.**」
  ⛔ **「何も動かない1枚だから、埃を薄くする」をしない。** **逆である。**
- ⚠️ **この1枚が参照画像として渡るときの危険も、ここに在る。** ⚠️ **空洞を塞いで、
  この1本を「止まった1枚」に読ませてしまうことである**——`s26` §20 の最初の危険は
  「**The generator may fill the stillness.**」である。**この1枚が静けさの見本になれば、
  動画の側はその静けさを9.5秒ぶん引き伸ばす。**

## ⚠️ `s01` と違えてはならないもの、違えなければならないもの

- ⛔ **この1本は `s01` の写しではない。** `s26` §4——「⚠️ **`s01` と同じ現場である** ——
  `出席簿の転出欄`。**この作品は、ここへ戻る。**」 ⚠️ **ゆえに、この2枚を並べて読む者のために、
  ここに線を引く。**
- ⛔ **違えてはならないもの**（実測 2026-09-28、この2枚の7欄と、`s01` §13・`s26` §13 を突き合わせた）:
  - **机**——`LOCATION` の値は `s01` と1字も違わない（**机の木の面、閉じた引き出し、椅子の背、
    机の上には他に何も無い**）。
  - **管**——`LIGHT` の値も1字も違わない。⚠️ **`s01` §13 の `Base Lighting` と `s26` §13 の
    それは、同じ文である**——「Fluorescent over a working desk at the end of the working day, …
    the room's own light has not been switched off yet; outside there is nothing left to see.」
    ⚠️ **管の位置も同じである**（「above and behind the camera」）。`s26` §15 `Spatial` も
    「**The light arrives from the same side as in `s01`.**」と書く。
  - **舞台**——`s01` §16 `PREFER` の「**Desk height for the lens, with the register square in the
    frame and its closed edge toward the camera**」は、この1本でもそのままである
    （`s26` §10——「Third person, **close**, on the open register」）。**カメラは、この1本でも動かない。**
  - **手**——`s26` §15 `Identity`——「**Must preserve** — `s01`'s hand」。**同じ人物の、同じ右手である。**
    ゆえに `CHARACTERS` の語も、`s01` と同じ語で書く（**ただし下の一件を除く**）。
  - **束の外にあるもの**——`s01` の `Negative` の尾と、この1本のそれも同じである。
- ⛔ **違えなければならないもの**（これが「写し」と「反復」を分ける）:
  - **手の状態。** `s01` は**押している**（`s01` §9 `ACT_ARRIVE`——「the pads of the fingers are on
    the cover」）。この1本は**押していない**——`s26` §11 `Weight`——「**the hand rests on the page and
    nothing is being held down.**」 ⛔ **`s01` の終わりのコマは「まだ沈んでいる」だった**
    （`s01` §16 `MUST`——「**The change is still in progress on the last frame**」）。
    **この1本の終わりのコマは、沈み終えている。**
  - **頁の状態。** `s01` の頁は**起きている**（`s01` §11 `Object Motion`——「**The page, once** —
    it rises under the hand and is pressed flat, and **it is still settling on the last frame.**」
    ／`s01` §16 `PREFER`——「**the page standing as the frame's only diagonal**」）。
    この1本の頁は**落ち着いている**——`s26` §11 `Object Motion`——「**The register does not move.
    The page does not turn.**」 ⚠️ **ゆえにこの1枚には、斜めが1本も無い。**
  - **光と主題の関係。** ⛔ **ここが、この2本のいちばん大きな差である。** `s01` §13 `Lighting Events`
    は「**None**」と書き、そのうえで「**the light in the frame changes continuously**, and it
    changes **because the subject moves**」と言う——**光は、手が動くから変わる。**
    `s26` §13 は逆である——「⚠️ **One, and it is the shot's whole change: the tube's edge crosses
    the page from one side to the other.**」 **この1本では、手が止まっているから光が変わる。**
    ⛔ **同じ管が、同じ側から来て、同じ頁に落ちている。****変えたのは、動く側である。**
  - **密度。** `s01` §16 の密度は「Low visual density: one focal point, the cover and the standing
    page and the hand that arrived on it」であり、この1本は `s26` §2 `Visual Density`——
    「**Very low, and falling.** One focal point — the page — with the frame emptying toward it across
    nine and a half seconds.」 **この1本は、`s01` より薄い。**
  - ⚠️ **但し、この1本は `s01` より長い**——8.059秒と9.506秒である。**薄さは、尺の短さではない。**

## ⚠️ 光の縁は、この1枚の中では既に渡り終えている

- ⛔ **この1枚が写すのは、この1本の終わりの状態である**（上の `## 渡す先`）。⚠️ **そしてこの1本の
  終わりの状態では、光の縁はもう頁の上に無い**——`s26` §8 `MOVEMENT 3`（`6.5-9.506s`）は
  「**it goes, and the page remains** — open, unread, and **still not closed.**」であり、
  §9 `ACT_CROSS` は「Before: the page is lit evenly. After: **the light's edge has crossed it and
  gone.**」と書く。**ゆえにこの1枚の頁は、平らに均された面である。**
  ⚠️ **`Prompt` の一行「The tube's edge has finished crossing the page and gone, and the page is
  evenly lit again.」が、その1行である。**
- ⚠️ **これは、この1本の変化をこの1枚が使ってしまわないためである。** `s26` §8 は、変化を
  **真ん中のビート**に置いている（`3.0-6.5s`、`sparse`）——**開始のコマでも、終わりのコマでもない。**
  ⛔ **1枚に縁を止めて渡せば、その1枚は「縁が頁の上にある絵」になり、動画の側は
  その縁を保持する（＝渡らない）方向へ引かれる。**
  ⚠️ **同じ規律が、この作品の他の1枚にも掛かっている**——`s24`・`s25` が写すのは
  「起きて止まった二つの顔」であり、**起きる途中の顔ではない。**
- ⚠️ **だが、もう一つの危険が在る。** `s26` §20 の2番目の危険——
  「**The light may be rendered as a glow rather than a boundary**, losing the crossing.」
  ⚠️ **ゆえに `Negative` に `no glow on the page, no flare across the page, no colour change across
  the page, no flicker` を置く**（実測 2026-09-28、私が選んだ行である）。
  ⛔ **これも `s26` §16 の写しではない**——§16 の `MUST NOT` に、光の描かれ方を禁じる行は無い
  （**あちらの禁制は動画の側の事象についてであり、この段落は絵の側の描かれ方についてである**）。
  ⚠️ **この段落が効くのは、この作品でここだけである**（下の節を見よ）。
- ⚠️ **裁定は著者のものである。** `s26` §16 `PREFER` は「The page filling the frame with **the
  light's edge entering from one side**, so that **the crossing is read as a boundary and not as a
  brightness.**」と言う——**もし著者が「縁の見える1枚」を選ぶなら、この段落の一行を差し替える。**

## ⚠️ 註を、この1枚では書かない——`s01` と同じ規律である

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **註の仕事は「どの設定画を取るか」を教えることである**——`s24`・`s25` が
  `[秋山誠: **the frozen setting sheet holds his face** — the name is here only so the right sheet
  is taken]` と書くのは、**その1本が `identity` を添付するからである。**
- ⛔ **この1本は `identity` を添付しない。** `shots/habits-mv-s26.yaml` の `reference_set` は5点であり、
  **そのどれも設定画ではない**——`碓氷千夏.negatives` と、出席簿の4点である。
  `s26` §3——「⚠️ **この1本は設定画を添付しない。** 参照集合が挙げているのは `碓氷千夏.negatives`
  だけである ——**ゆえに渡るのは禁制の側だけである。**」
  ⚠️ **渡る一枚が無いのに名を書けば、名は設定画を呼びに行く**——**註が、`s01` の規律を破る。**
- ⚠️ **ゆえに `CHARACTERS` は、`s01` と同じ形で、手だけを持つ**——**名前を1つも書かない。**
  `s01` の同じ節——「**註を書けば、置かれる。**」
- ⛔ **そして、この欄は註ではない——生成器へ渡る文字列であり、書かれたものは描かれる。**
  ⚠️ **動画の仕様が年齢や職業を書くとき、その宛先は人間である**（`s06` の `Reference:` の行は
  「**出典の語は「路線バス運転士・52歳」である**」と引く——**あれは、出典についての日本語の散文であり、
  読み手は人間である**）。⛔ **同じ語をこの欄へ置けば、宛先が変わる**——**英語の入力として
  生成器に届き、絵になる。**
- ⛔ **そして `s01` の `CHARACTERS` から、一語だけ落としている**——`s01` は
  「**a girl's hand**」と書くが、**この1枚は「a right hand」とだけ書く**（実測 2026-09-28、
  この2欄を並べて数えた）。⚠️ **理由は、人を指す名詞をこの欄に置かないためである**——
  **置けば、その語が作品の持たない事実になる**（`ledger.yaml` の註——「**外見の記述は出典に一行も
  無い**（方針 §5a）。**凍結した二枚が外見である。**」）。
  ⚠️ **手の語そのものは、落としていない**——`爪の短い手、右手中指の第一関節の小さな膨らみ`は
  `01_碓氷千夏/prompt.md` の `**ルック＝**` の行に在る（**出典の語である**）。
  ⚠️ **`s01` の側を直すかどうかは、著者の裁定である**——**この稿は `s01` を触っていない。**
- ⚠️ **これは `scene-board` の `do` からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- ⛔ **隣の作品（`migenzo`）と、答えが逆である。** あちらは
  「**`Not photorealistic` を、ここに写してはならない**」という節を持ち、**様式カードの否定を
  落とした**（裁定 2026-09-23、著者）——**あちらの作品は実写である。**
- ⚠️ **この作品は、実写ではない。** `s26` §2 は「**Clean anime lineart**」と言い、
  §16 の `MUST NOT` は「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が `not photorealistic` を
  先頭に持つ側である。**
- ⚠️ **ゆえに、この1枚は様式カードの否定をそのまま負う。**
  ⛔ **隣の作品の節を、この作品へ写してはならない**——**写せば、頁の上の1枚が実写になる。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**（`s26` §18——「**`Negative Prompt`
  を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**読める字**と**偽の字**と**光の描かれ方**——を禁じているのは、**この段落である。**
  ⛔ **そして実測（2026-09-28、動画3本）が、その差を出した**——
  **机の上の手書きが、日本語の字ではなく、ラテン文字の草書として戻った。**
  動画の §18 は `no real-world alphabet` を既に持っていた。**散文として読まれた。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。**
  ⚠️ **この1本では `no background music` が、いちばん余分な行である**——
  **曲は、この1本の前に終わっている**（`s26` §14 `Music`——「**This is the first shot after the
  song ends, and the work does not replace the song with anything.**」）。
  **床は、この1本でも外れない。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s26.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「手が止まり、**画面の中に残っている。**光だけが動き続けている。」
- `reference_set` は**この1本では5点**である——`碓氷千夏.negatives`・`出席簿`・`出席簿.negative`・
  `出席簿の転出欄`・`出席簿の転出欄.geography`。⚠️ **`碓氷千夏.identity` を意図的に持たない**
  （`s01` と同じ理由。`s26` の頭——「**参照集合に `碓氷千夏.identity` を入れない**」）。
- ⚠️ **食い違い1（読み取り。裁定は著者のもの）。** `s26` §15 `Spatial` は
  「**The page, the desk and the hand are in the positions `s01` left them in.**」と言う。⛔ **だが
  `s01` の終わりのコマでは、頁はまだ起きて沈んでおり**（`s01` §11／§16 `MUST`）、**この1本の手は
  何も押さえていない**（`s26` §11 `Weight`——「nothing is being held down」）。**同じ手が
  両方であることはできない。** ⚠️ **この稿は記録の側を取った**——`s26` の `unit.after`・
  §5（「手 — **頁の上にある。動かない。**」）・§9（「**the hand is at rest on the page**」）・
  §11 の4つが「手は頁の上で休んでいる」と言い、§15 の一行だけが「`s01` の位置のまま」と言う。
  **ゆえにこの1枚の頁は、落ち着いている。**（**数を数えたうえで選んだ、ということをここに書く。**）
- ⚠️ **食い違い2。** `s26` §15 `Temporal` は「**the work has returned to the morning's place and the
  evening's light.**」と言うが、⛔ **`s01` の `time` は `勤務日の夕方` である**（`s01.yaml`）——
  `s26` 自身の §2 `Time` も、夕方の区切りに **`s01`〜`s04`** を数えている。
  **ゆえに「朝の場所」は、この作品の側に無い。** ⚠️ **この1本の `LIGHT` の値が `s01` と
  1字も違わないのは、そのためである。**
- ⚠️ **食い違い3（この稿の外・報告のみ）。** `s01` §15 `Visual` は
  「**the work's four evening shots share it.**」と言うが、**`time: 勤務日の夕方` を持つ1本は8本である**
  （実測 2026-09-28、`shots/*.yaml` を数えた——`s01`〜`s04`・`s17`・`s18`・`s26`・`s27`）。
  **「4本」は、夕方が `s01`〜`s04` だけだった時点の数である。** ⛔ **この稿は `s01` を触っていない。**
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
