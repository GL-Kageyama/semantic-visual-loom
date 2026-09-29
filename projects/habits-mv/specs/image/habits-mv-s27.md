# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第二十七のショット「手が退き、紙と光だけが残る」（余白 / still / 14.309s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
⚠️ **そして `mode: still` のショットにも、画像は要る**——**この1本が、この作品の最後の1本である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⛔ **この1本は、この作品の最後の1本である**（`shots/habits-mv-s27.yaml`——「**この作品の最後の
画面である。**」）。⚠️ **この作品で2番目に長い1本である**——**最も長いのは `s18` の14.840秒である**
（`s27` の頭——**この記録は初め「最も長い」と書いていて、`duration` の欄から数え直して誤りと
分かり、直した**）。⚠️ **それでも、この作品の最後の画面は最初の画面より長い**——
`s27` §8——「**the work's last image is longer than its first.**」（14.309秒 対 8.059秒）。
⚠️ **この1本は `s01` と同じ場所であり、`s26` の続きである。** `s27` §4——
「⚠️ **`s01` と同じ現場である** —— `出席簿の転出欄`。**この作品は、ここで終わる。**
**開いた頁は、最後まで閉じられない。**」／§15 `Spatial`——「**the shot is the frame `s26` handed
over, minus a hand.**」 ⛔ **ゆえにこの1枚は、`s26` の1枚から手を引いたものである。**
⚠️ **この1本は `mode: still` である**——**主題は、もう動かない。****手が一度だけ退き、残りは
光だけが動く。**
⚠️ ⚠️ **この1枚には、肌が1つも無い。** `s27` §15 `Visual`——
「**this is the only frame in the work with no skin in it at all.**」
⛔ **この作品の27本の中で、人も手も写らないのは、この1枚だけである。**
**ゆえにこの1枚には、`[名前: …]` の註を書かない**（下の節）。
⚠️ ⚠️ **参照集合には `碓氷千夏.negatives` だけが入っている**（`s01`・`s26` と同じ規律）。
**設定画も、手の一枚も、渡さない。**
⚠️ **この1本のあとに、何も無い。** `s27` の頭——「**曲を切らない。**（設計 04 §2-3）
「**曲を切らない。fade out もかけない。曲の尺が作品の尺である。**」——**この14.309秒は、間奏でも
余りでもない。** 曲の一部である。**ゆえに画面も、ここで終わらない**——**曲が終わるところで終わる。**」
⛔ **この1本は `ledger.disclosure` の変化点ではない**（台帳の3点は `s10`・`s17`・`s18`）。
**この1枚は、明かす1枚ではない。****明かすものが、もう残っていない1枚である。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/seedance-2.5/habits-mv-s27.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a page with nobody on it.** **The light, not the
    figure, is the subject** — and here the figure has left, so **the shot is the art direction of a
    fluorescent tube and two materials.**」
    ——**動画の側が先に、この様式を「誰も居ない頁へ翻訳した」と書いている。** 画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s27.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/prompt.md`
  （凍結した設定画の読み。⚠️ **但しこの1本には添付しない**——**読むのは、禁制の側が何を禁じるかを
  確かめるためである**）と、**同じ現場の2枚**——`specs/image/habits-mv-s01.md` と
  `specs/image/habits-mv-s26.md`（⚠️ **この作品で、この現場の1枚はこの2枚だけである。**
  **この1枚は、その2枚と並べて読まれる**）
- 添付する参照: **無い。** ⛔ **`specs/image/生成時参照イラスト/` に `s27` のフォルダは無い**
  ——**この1本の `reference_set` は `碓氷千夏.negatives` だけを挙げ、`identity` を挙げないからである。**
  ⚠️ **不在は、置き忘れではない。** 動画の側も同じである（`specs/video/生成時参照イラスト/` にも `s27` は無い）。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s27` §6——この27本は「参照画像」の型である。
  **`first_frame` ではない**）。⚠️ **この1枚が「手の退いたあとの頁」を写すのは、そのためである**
  ——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  ⚠️ **但し、この1本では開始のコマと終わりのコマの差が、この作品でいちばん大きい**——
  **手が在るか、無いかである。** **下の節と、下の `## 記録との対応` に、それを書く。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** この作品の前提は「名は、どこにも読めない」である
  ——**文字列に日本語の字を置けば、置かれる側へ回る。** ⚠️ **この1本の2段落には、日本語の字が1つも無い。**
- 記録: `shots/habits-mv-s27.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`LOCATION` と `LIGHT` の2欄は、`s01` と `s26` の同じ欄と1字も違わない**（実測 2026-09-28、
この3枚を並べて数えた）——**この1本が「同じ場所で終わる」とは、まずこの2欄のことである。**
⚠️ **`CHARACTERS` には、カードが求める `[名前: …]` の註を書かない**——**この1本には、
置かれる人が居ないどころか、手も無い。** 理由は下の節に書く。

- `SCENE`: the last frame — the transfer column of last year's register, open on a desk at the end of a working day, and after the hand has gone, paper, light and dust; **nobody is in it**
- `CHARACTERS`: **no one in place, and no hand either** — **this is the only frame in the work with no skin in it at all**; **no name is given to the model, because a name brings a person**
- `SUBJECT`: the open page — **a surface, and the tube's light on it**; there is no subject left in the frame to move
- `ACTION`: the withdrawal and what remains — a hand leaving the page along its surface and going out at the frame's edge, and **nothing after it**: the page does not turn, the register does not close, and the light and the dust are all that is still happening
- `LOCATION`: a desk in a school staff room at the end of a working day, 2026 — the desk's worn wooden face, a drawer closed, the back of a chair; **nothing else on the desk**
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling across the register and the page, bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the cream of the page edge and the paper itself — the only warm thing the tube finds in a narrow, cold room, **and there is no skin in the frame for it to find**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of an open school attendance register on a desk at the end of a working day, 2026, with nobody in the frame and the light of a fluorescent tube on it. The register lies square to the desk's edge, cloth over board, the thickness of a register's left sleeve, a bound spine, its fore-edge layered cream and not smooth; it is open at the transfer column, the page lies settled on the block, flat and not standing on its own edge, and no hand is on it and no hand is near it. On the page the transfer column is on screen: characters written in ink by more than one hand, present and not readable, the marks of cut print and of ballpoint and of pencil drawn as the three different marks they are and none of them legible. The page is the only subject: there is no hand, no head, no shoulder and no standing figure in the frame, and nothing else is on the desk — no mug, no pen cup, no terminal, no stack of paper. The desk is wood with the polish of forearms on it, and its worn edge is in the near foreground. The writing is not read: no eye is in the frame, no head bends over the page, no finger tracks a line down it, and the page is not turned. The room's light is a fluorescent tube above and behind the camera, falling flat across the register and the page and blooming on the pale surfaces; the paper is the brightest thing in the frame, the tube is the only light, and everything the desk edge shadows has gone to deep cyan. The tube holds and does not change: no edge crosses the page in this frame, and the page is evenly lit. Dust is suspended in the air above the desk where the tube catches it and is individually rendered, and it is the only moving thing in the frame. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette is narrow and cold — fluorescent white, the grey-green of the cover with its cloth weave, the cream of the page edge — and the warm side is reduced to the paper itself. Layered atmospheric depth from near to far. Very low visual density, falling to a single sheet: one focal point, the open page, with generous negative space and most of the frame given to the desk. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at desk height, looking slightly down, the register square in the frame with its closed edge toward the camera. One scene, one staging; the same desk, the same tube and the same page wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no head, no shoulder, no standing figure, no person behind the desk, no second figure, no hand, no second hand, no returning hand, no fingers, no knuckles, no arm, no cuff, no skin, no silhouette leaving the frame, no closed cover, no closed register, no turned page, no standing page, no second turn of the page, no lifting of the register, no carrying of the register, no reading, no eye in the frame, no head bent over the page, no finger tracking a line, no glow on the page, no flare across the page, no colour change across the page, no flicker, no closing title, no caption card, no end card, no credit card, no vignette, no darkened frame edge, no fade to black, no black frame, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan shadow**」。
- ⛔ **この部屋に、空は無い。** **この作品の光は、天井の蛍光灯1本である**（`s27` §13 は `s26` §13 と
  同じ文であり、「**outside there is nothing left to see**」と言う）。⚠️ **そしてこの1枚は、
  この作品でいちばん空から遠い1枚である**——**写るものが、紙と光と埃しか無い。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**（決定D——`style` は「誰の声か＝語彙」、
  「何を見せるか」は `format` の側である）。**ゆえに、この1枚が様式から取るのは**——clean anime
  lineart・cel shading・単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、その一文が字句どおりになる**（`s27` §2——「**the figure has left**」）。
- ⚠️ **この作品は、この1本でも既にその翻訳を書いている。** `s27` §2——
  「**Luminous realist anime, translated into a page with nobody on it.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**誰も居ない頁が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**（`s01` の同じ節を見よ。**同じ理由である。**）

## ⚠️ この1枚には、肌が1つも無い——この作品で唯一の1枚である

- ⛔ **`s27` §15 `Visual`——**「**this is the only frame in the work with no skin in it at all.**」
  **この作品の27本のうち、人も手も写らないのは、この1枚だけである。**
  ⚠️ **この一文は、`s27` が自分の位置を数え直したうえで書いている**——
  「The same fluorescent key and palette as all twenty-seven shots — **and this is the only frame in
  the work with no skin in it at all.**」 **比較の相手は27本であり、この1本はその外側である。**
  ⚠️ **画像の経路でも、同じことを数え直した**（実測 2026-09-28——**27本の画像仕様の
  `投入する1本の文字列` の1段落目を走査し、`hand`・`finger`・`knuckle`・`nails`・`wrist`・`arm`・
  `palm`・`face`・`eye`・`mouth`・`skin`・`cuff` の12語を、否定の語の直後を除いて数えた**——
  **26本に、否定されていない肌の語が1つ以上ある。** **この1本に在るのは `by more than one hand` の
  1箇所だけである**——**あれは書き手の数を言う句であって、画面の手ではない**）。
  ⚠️ **その句と `Negative` の `no hand` は、同じ1本の中に同居する**——
  **禁じているのは画面の手であり、句が言っているのは紙の側のことである。**
- ⚠️ **この1本の変化は「退く」であり、その変化が済んだあとの画面が、この1枚である。**
  `s27` §9 `ACT_WITHDRAW`——「Before: a hand is on the open page. After: **no hand is in the
  frame.**」／§11 `Subject Motion`——「**After the hand leaves, the subject does not exist in the
  frame** — **there is no figure left to move.**」
  ⛔ **ゆえにこの1枚には、動かす主体が1つも残っていない。****残っているのは、光と埃である。**
- ⚠️ **止まっていることが主題であることは、この1本でも同じである**（`mode: still`）。`s27` §16
  `MUST NOT` は `no static slideshow of stills, no floaty weightless motion` を持ち、§15 `Motion` は
  「**The last seven and a third seconds are a live frame** — **dust and light move through all of
  them.**」と言う。**ゆえにこの1枚にも、埃が要る。**
  ⛔ **そしてこの1本では、埃が「主役の代わり」である**——§11 `Environmental Motion`——
  「**They are not a background in this shot; they are what the frame has instead of a subject.**」
- ⚠️ **この1枚が参照画像として渡るときの危険は、`s26` と逆向きである。** `s26` では
  「静けさを引き伸ばされる」ことが危険だったが、**この1本では、動画の側の1番目の危険が
  「The hand may come back.」である**（`s27` §20——「**The first risk of this shot**: a frame with no
  figure in it reads, to a generator, as an unfinished shot」）。
  ⛔ **ゆえにこの1枚は、空いたままの面として、平らに、明るく、完全に写っている必要がある**
  ——`s27` §16 `PREFER`——「**The page filling the frame with the tube's light on it and the desk's
  cyan around it**, so that **the last image of the work is a surface rather than an absence.**」

## ⚠️ `s01` と、そして `s26` と、違えてはならないもの／違えなければならないもの

- ⛔ **この1本は `s01` の写しではない。****この作品は、同じ机で開き、同じ机で閉じる。**
  `s27` §4——「**この作品は、ここで終わる。****開いた頁は、最後まで閉じられない。**」
  ⚠️ **ゆえに、この2枚を並べて読む者のために、ここに線を引く。**
  ⚠️ **そして `s27` §15 `Spatial` は、この1本が `s26` の続きであることを、いちばん短い文で書く**——
  「**the shot is the frame `s26` handed over, minus a hand.**」
  ⛔ **この1枚と `s26` の1枚の差は、手が1つあるかないかである**（実測 2026-09-28、この2枚の7欄を
  突き合わせた——**`SUBJECT`・`ACTION`・`CHARACTERS` が違い、`LOCATION`・`LIGHT` は1字も違わない**）。
- ⛔ **違えてはならないもの**（`s01` を相手に）:
  - **机**——`LOCATION` の値は `s01` と1字も違わない。
  - **管**——`LIGHT` の値も1字も違わない。⚠️ **`s01` §13 と `s27` §13 の `Base Lighting` は同じ文で
    あり、管の位置も同じである**（「above and behind the camera」）。§15 `Spatial`——
    「**The page, the desk and the light are in the positions `s26` left them in**」。
  - **舞台**——`s01` §16 `PREFER` の「**Desk height for the lens, with the register square in the
    frame and its closed edge toward the camera**」は、この1本でもそのままである（`s27` §10——
    「Third person, **close**, on the open register」）。**カメラは、この1本でも動かない**
    （§16 `MUST NOT`——「**The camera does not follow the hand out.**」）。
  - **頁**——**開いたまま、読まれない。** ⛔ **`s01` が「運搬の最初の一歩が、ここで止まる」と
    書いた頁が、この1本でも同じ状態で残る**（`bible.world.rules` の四番——「**運搬は一度も
    完了しない。**」）。**この1本は、その規則の最後の1枚である。**
  - **手**——`s27` §15 `Identity`——「**Must preserve** — `s01`'s and `s26`'s hand」。**画面から
    出ていった手も、同じ人物の、同じ右手である。**
- ⛔ **違えなければならないもの**（これが「写し」と「最後の1枚」を分ける）:
  - **手の有無。** `s01` は**手が画面の下から入ってくる1本である**（`s01` §7 `Turn`——
    「**The hand arrives from below the frame.**」）。**この1本は、手が画面から出ていく1本である。**
    ⛔ **そしてこの1枚には、手が1つも無い。**
  - **頁の状態。** `s01` の頁は**起きている**（`s01` §16 `PREFER`——「**the page standing as the
    frame's only diagonal**」）。**この1本の頁は落ち着いている**（`s27` §11 `Object Motion`——
    「**The register does not move and the page does not turn.**」）。
    ⚠️ **ゆえにこの1枚には、`s01` の1枚に在った斜めが1本も無い。**
  - **動いているもの。** `s01` §8 は「**a picture that has already stopped cannot receive it**」と
    書いた——**`s01` の8.059秒は、止まらずに走る8秒である。** ⚠️ **この1本は逆である**——
    `s27` §13 `Lighting Events`——「**None.**」／§11——「**One withdrawal, and then nothing.**」
    **この1本の最後のほうは、何も起こらないことが内容である。**
  - **密度と、それでも尺が長いこと。** `s01` の密度は「Low visual density」であり、この1本は
    `s27` §2——「**Very low, falling to a single sheet.**」**この1本は、`s01` より薄く、長い。**
  - ⛔ **そして、この1本には肌が無い**（上の節）。**`s01` には手が在った。****この2枚は、
    同じ机の上の、同じ頁の、同じ光である****——****違うのは、人と、その残り方だけである。**

## ⚠️ 終わりを、この1枚に置かない——`s25` の反対側である

- ⛔ **この1本は、作品の最後の1本である。ゆえに「終わり」を描きたくなる。**
  `s27` §17 `GENERATION PRIORITIES` の4番目は、それを名指しで禁じる——
  「**Nothing marks the ending** — no fade, no music, no light change.」
  §16 `MUST NOT`——「**Nothing arrives after the hand has gone** — no light change, no event,
  no closing title, no fade to black.」
- ⚠️ **ゆえに `Negative` に `no closing title, no caption card, no end card, no credit card,
  no vignette, no darkened frame edge, no fade to black, no black frame` を置く。**
  ⛔ **但し、この段落は動画の §16 の写しではない**——**動画の側の「fade」は時間の側の変化であり、
  1枚の絵はそれを運べない**（実測 2026-09-28、私が選んだ行である）。**この1枚が運べるのは、
  絵に描かれる「終わり」だけである**——**題字、黒、周辺減光。****そして、そのどれも置かれない。**
- ⚠️ **`s25` の同じ節と、向きが逆である。** あちらは**歌の終わり**を画面に置かなかった
  （`s25`——「**the work puts its ending in `s26` and `s27`, not here.**」）。
  ⛔ **この1本こそ、その終わりを受け取る側である。そしてこの1本も、何も置かない。**
  `s27` §12 `Emotional Events`——「⚠️ **The event is the withdrawal, and nothing marks it.**
  ⚠️ **No fade, no music, no light change** —— **the work's last shot ends the way a room is left.**」
- ⚠️ **曲の側も、同じことを言っている。** `shots/habits-mv-s27.yaml` の頭（設計 04 §2-3）——
  「**曲を切らない。fade out もかけない。曲の尺が作品の尺である。**」
  ⛔ **ゆえに画面が自分で終わる必要は無い。** **曲が終わるところで終わる。**
- ⚠️ **裁定は著者のものである。** `s27` §20 の4番目の危険は、まさにこの節の外れである——
  「**A fade to black, a closing title or a score may be added** — **the work does not close
  itself.**」 **この1枚が黒や題字を持てば、動画の側はそれを作る。**

## ⚠️ 註を、この1枚では書かない——この作品で、いちばん強い場合である

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **註の仕事は「どの設定画を取るか」を教えることである。** この作品で註を書くのは
  `s24`・`s25` だけであり、**その2本が `identity` を添付するからである。**
- ⛔ **この1本は `identity` を添付しない。** `shots/habits-mv-s27.yaml` の `reference_set` は5点であり、
  そのどれも設定画ではない。`s27` §3——「⚠️ **この1本は設定画を添付しない。** 参照集合が挙げているのは
  `碓氷千夏.negatives` だけである ——**ゆえに渡るのは禁制の側だけである。**」
  ⚠️ **渡る一枚が無いのに名を書けば、名は設定画を呼びに行く。**
- ⛔ **そしてこの1本では、それだけではない**——**この1枚には手も人も写らない**（上の節）。
  `s27` §16 `MUST NOT`——「**No face, no person and no second hand enters the frame.**」
  ⚠️ **置かれる人が1人も居ない1枚に名前を書けば、その名が人を置く**——
  `s01` の同じ節——「**註を書けば、置かれる。**」
  **ゆえに `CHARACTERS` は、手の記述も持たない。****この作品で、そう書けるのはこの1枚だけである。**
- ⛔ **そして、この欄は註ではない——生成器へ渡る文字列であり、書かれたものは描かれる。**
  ⚠️ **動画の仕様が年齢や職業を書くとき、その宛先は人間である**（`s06` の `Reference:` の行は
  「**出典の語は「路線バス運転士・52歳」である**」と引く——**あれは、出典についての日本語の散文であり、
  読み手は人間である**）。⛔ **同じ語をこの欄へ置けば、宛先が変わる**——**英語の入力として
  生成器に届き、絵になる。**
- ⚠️ **これは `scene-board` の `do` からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**
  ⚠️ **`s01` は手の記述を `CHARACTERS` に持つ**（同じ `do` からの逸脱である）。
  **但し `s01` は手を写す1本であり、この1本は写さない。****ゆえにこの1枚は、`s01` より一歩先へ行く。**

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- ⛔ **隣の作品（`migenzo`）と、答えが逆である。** あちらは
  「**`Not photorealistic` を、ここに写してはならない**」という節を持ち、**様式カードの否定を
  落とした**（裁定 2026-09-23、著者）——**あちらの作品は実写である。**
- ⚠️ **この作品は、実写ではない。** `s27` §2 は「**Clean anime lineart**」と言い、
  §16 の `MUST NOT` は「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が `not photorealistic` を
  先頭に持つ側である。**
- ⚠️ **そしてこの1枚では、この行の効き方が、ほかの26枚と少し違う**——**写る人が居ないからである。**
  ⚠️ **人肌が無いことは、実写らしさを消す方向には働かない**——**机と紙と埃は、実写でいちばん
  写りやすい被写体である。****ゆえにこの1枚では、この行がむしろ弱くなる。**
  ⛔ **隣の作品の節を、この作品へ写してはならない**——**写せば、最後の1枚が実写になる。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**（`s27` §18——「**`Negative Prompt`
  を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**読める字**と**偽の字**と**光の描かれ方**と**画面に置かれた「終わり」**——を
  禁じているのは、**この段落である。**
- ⛔ **そして、この1本では軽いほうの失敗が在る。** `s25`・`s26` では**画面に置かれた「終わり」**が
  危険だったが、**この1本では「手が戻ること」が1番目の危険である**（`s27` §20）。
  ⚠️ **1枚の絵の中で手が戻ることは起きない。だが、この1枚に手が写っていれば、
  動画の側はその手を保持する。** ⛔ **ゆえに `Negative` に `no hand, no second hand,
  no returning hand, no fingers, no knuckles, no arm, no cuff, no skin` を置く**——
  **この段落は、この1本では「何も足さない」ことを守る床である。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**——
  **同じ床を、効く場所へ置いたものである。**
  ⚠️ **この1本では `no background music` が、いちばん遠い行である**——
  **曲は、`s26` の前に終わっている**（`s27` §14 `Music`——「**This is the last shot of the work and
  the one where a closing score is most likely to be added; the song has ended and the work does
  not replace it.**」）。⛔ **床が要るのは、まさにその「足したくなる場所」である。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s27.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「**手が退き、紙と光だけが残っている。**」
- `reference_set` は**この1本では5点**である——`碓氷千夏.negatives`・`出席簿`・`出席簿.negative`・
  `出席簿の転出欄`・`出席簿の転出欄.geography`。⚠️ **`碓氷千夏.identity` を意図的に持たない**
  （`s01`・`s26` と同じ理由）。
- ⚠️ **食い違い1（読み取り。裁定は著者のもの）。** `shots/habits-mv-s27.yaml` の `motion.quality` は
  「そのあと、**残りの11秒は、光だけが動く。**」と言う。⛔ **だが `s27` §1・§8・§13・§14 は
  四度「seven and a third seconds」と書く**——§8 `MOVEMENT 3` は `7.0-14.309s` であり、
  **14.309 − 7.0 = 7.309秒である。** ⚠️ **11は、退きはじめ（3.5秒）から数えた数である**
  （14.309 − 3.5 = 10.809）。**どちらの切り方でも、`duration` の欄から出る数は 7.309 と 10.809 である。**
  ⛔ **この稿は、動画の仕様の4箇所と計算の側を取る。****この1枚には、11と書かない。**
  ⚠️ **そして、同じ「11秒」が `s27` §7 `Pull` にも在る**（「**Eleven seconds of paper, light and
  dust.**」）——**ゆえにこの食い違いは、記録と仕様の間ではなく、`s27` の内側にも在る**
  （§7 対 §8・§13・§14）。**報告のみ。****この稿は `specs/video/` を触っていない。**
- ⚠️ **食い違い2（この1枚の側の、避けられない緊張）。** この1本の**最初の3.5秒には手が在る**
  （`beats` の `0-3.5s`——「頁の上の手。**動かない。**」）。⛔ **だがこの1枚は、手の無い側を写す**
  （終わりの状態である。上の `## 渡す先`）。⚠️ **そして `reference_set` には、手の一枚が1つも
  無い**——`碓氷千夏.negatives` だけである。**ゆえに前半の手は、`s26` のテイクからの連続で
  保たれるのであって、この1枚からは渡らない**（`s27` §15 `Identity`——
  「**Must preserve** — `s01`'s and `s26`'s hand」）。**これは欠陥ではなく、この1本の設計である**——
  **「退く」1本の参照画像が、退いたあとの状態であること**は、この作品の規律の帰結である。
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
