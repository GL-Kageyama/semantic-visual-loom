# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第二十五のショット「二つの顔が起き、最後の一行が終わる」（開示 / motion / 5.186s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、`final-chorus` の7本目であり、最後の1本である**（動画の仕様 §19——
`Segment ID: final-chorus-7`）。⚠️ **そして、この作品が最後に顔を置く1本である。**
動画の仕様 §6——「**この本が最後に顔を置く1本である。**」§15——
「⚠️ **This is the last shot in the work that places a face.**」
⚠️ **この1本は `s24` の反復である。** `motion.law` は
「**`s24` と同じ法である**——**この2本が対であることを、運動の側が持つ**」と定め、
§8 は「**`s24`'s shape at `s25`'s length.**」と書く。⛔ **同じ1本ではない。**
§8——「⚠️ **The difference between the two shots is 0.160秒 and two people**，
**and the work does not pretend they are more different than that.**」
⚠️ **この1本の尺は、最後に歌われる一行の尺そのものである**（実測 2026-09-28）——
`l30` は 150.319秒に立ち（`bible.song.lines`）、`final-chorus` の節は 155.505秒で終わる。
差は **5.186秒**であり、**この1本の `duration` と1フレームも違わない。**
⚠️ **同じ測り方が `s24` にも当たる**——`l29` 145.293秒と `l30` 150.319秒の差は **5.026秒**である。
⛔ **ゆえにこの1本は、「最後の一行が終わるまで」の1本である。**
⚠️ **そのあと、作品は顔を持たない。** 動画の仕様 §2 `Time`——
「⚠️ **After this shot, the work moves to the evening for its two remaining shots.**」
（`s26`・`s27` は `mode: still` の余白である。）
⚠️ **この1枚が写すのは、この1本が終わったあとの状態である**——**二つの顔が起きて止まり、
その上で歌が終わっている。** **手が先で顔が後である順序は、この1枚からは読み取れない。**
⛔ **この1本は `ledger.disclosure` の変化点ではない**（台帳の3点は `s10`・`s17`・`s18`）。
**この1枚は、明かす1枚ではない**（`s24` の同じ節を見よ）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/seedance-2.5/habits-mv-s25.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into the last two faces the work will place.** **The light,
    not the figure, is the subject** — and here it is the same tube as `s24`, in the same two places,
    **so the repetition is visible before it is heard.**」
    ——**動画の側が先に、この様式を「最後の二つの顔へ翻訳した」と書いている。**
    画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s25.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/サブ/18_清水拓也/ChatGPT Image 2026年9月19日 13_07_28.png`
  と `.../サブ/17_林沙織/ChatGPT Image 2026年9月21日 01_06_30.png`
  （**人のかたちの一枚ずつ**。`ledger.yaml` の `清水拓也.identity` と `林沙織.identity` が指す先であり、
  動画の仕様 §6 も同じ先を指す）＋ 同じ作品の既存の生成物（`media/` の動画）
- 添付する参照: **`specs/image/生成時参照イラスト/s25/` の2枚**——`林沙織_設定画.png`・`清水拓也_設定画.png`。
  ⚠️ **この2枚は、この作品の動画の側の同じ2枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s25/`。実測 2026-09-28、ハッシュが一致した）。
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s25` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。⚠️ **この1枚が「起きて止まった二つの顔」を写すのは、そのためである**
  ——**渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
  **歌が終わることは、この1枚からは読み取れない。****ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 様式カードでも書けるが、
  **この作品の前提は「名は、どこにも読めない」である**——**文字列に日本語の字を置けば、
  置かれる側へ回る。** ⚠️ **この1本の2段落には、日本語の字が1つも無い。**
- 記録: `shots/habits-mv-s25.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` には `[名前: …]` の註を2つ書く**（この作品で2つ置くのは `s24` とこの1本だけである）
——**この1本には、置かれる人が二人いる。** ⛔ **註は名指すだけで、外見を書き起こさない。**
⚠️ **そして7欄の値は、`s24` の7欄と対で読まれる**——**この作品は、この2本を1組として持つ。**

- `SCENE`: the seventh of the final chorus, and the last shot that places a face — two hands press paper in two places and two faces rise, one after the other, and the last sung line ends over them
- `CHARACTERS`: `[清水拓也: **the frozen setting sheet holds his face** — the name is here only so the right sheet is taken, and no appearance is re-derived in words]` `[林沙織: **the frozen setting sheet holds his face** — the name is here only so the right sheet is taken, and no appearance is re-derived in words]` — **two hands and, above them, two faces, in two places**, and these are the last two the work places; the turns happen in the hair and the neck, the shoulders move very little, and neither face is turned to the lens
- `SUBJECT`: two faces rising above two bundles of paper, one after the other, in one composition — **the same construction as `s24`, with two other people**
- `ACTION`: two presses and two turns — each hand comes down flat on its own bundle in one fast even movement and stops, and **then** that face rises: the hair takes the light on one side and moves before the face, the neck carries the turn, and the face is up and still; **the second turn comes after the first and never with it**, and **nothing is lifted from either bundle**
- `LOCATION`: two desks with a bundle of paper on each, in two school rooms, in the middle of a working day, 2026, held in one frame — **the same composition as `s24`**, the bundle low in the frame and the face entering above it; ⛔ **no wall, no window, no clock, no weather and no prop that would tell the two places apart**
- `LIGHT`: the room's constant state, and the same light in both places — the flat light of a fluorescent tube above and behind the camera falling across both desks, bloom on the pale surfaces, the paper the brightest thing in the frame, and everything the desk edges shadow gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the skin of two faces — the same value as `s24`'s, and the only warm thing in either place

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the seventh of the final chorus of a theme-song music video — the master staging of one scene, in 16:9, and the last shot of the work that places a face. A luminous realist anime illustration of two faces rising above two bundles of paper on two desks, in the middle of a working day, 2026, with the skin of those two faces as the only warm thing in either place. One composition holds both places inside a single unbroken picture and it does not cut: the frame is one picture from edge to edge, with no seam, no border, no dividing line and no panel edge anywhere in it, and one continuous stretch of desk, cloth and room runs from one bundle to the other without a break; in each of the two places a bundle lies low in the frame with a hand flat on it and, above it, a face coming up, and the two are the same shape at the same small amplitude — the same construction as the shot before this one, with two other people and nothing else changed. In each of the two places the hand comes down flat on the bundle in one fast even movement and stops, and then the turn happens: the hair takes the light on one side only and moves before the face, the neck carries the turn, the shoulders move very little, and the face is up and still, looking up from the paper and not into the lens — and the second turn comes after the first and never at the same moment as it. Neither face is smiled, neither is startled, neither widens the eyes and neither carries a reaction to anything: two people looking up in two rooms, one after the other, and the frame does not know that it is the last one. The bundles are paper — slips, registers and tags, their edges unsquared — and they do not move: neither one is lifted, turned or carried, nothing comes out of either of them, and the characters on them are present on screen and not readable, drawn as the different marks of cut print and of ballpoint and of pencil, none of them legible. Nothing in the frame tells the two places apart: there is no wall, no window, no clock, no difference of weather and no prop that belongs to one place and not the other, so that the only difference between the two places is how much deep cyan the shadows hold. The light is one fluorescent tube above and behind the camera, falling flat and even across both desks; the paper is the brightest thing in the frame, the tube is the only light, and everything the desk edges shadow has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. Layered atmospheric depth from near to far, dust suspended and individually rendered where the tube catches it, and it is still moving when the frame is taken; low visual density — one focal point, the rising face, twice, with the desk going out of the frame's attention as each face arrives. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens close at the desk and the face above it, the same placement in both places, unmoving, and it does not follow either face up. One scene, one staging; the same desks, the same tube and the same two turns wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no cut, no dissolve, no wipe, no transition between the two places, no split screen, no split-screen image, no two-panel image, no two panels, no four-panel image, no multi-panel image, no panel border, no diptych, no triptych, no collage, no grid, no comic layout, no storyboard layout, no contact sheet, no second image, no image beside the image, no frame within a frame, no border between the two places, no seam, no dividing line between the two places, no dividing strip, no second camera angle, no reframe between the two presses, no pan, no tilt, no push-in, no pull-back, no cut between the two turns, no face rising at the same moment as the other face, no simultaneous turn, no two faces moving at once, no caller in the frame, no second figure, no person at the source of the call, no one rendered in the direction of the call, no mouth opening, no speaking, no voice, no muffled call from off, no look into the camera, no eye contact with the lens, no smile, no startle, no widened eyes, no lifted brow, no tears, no fear, no exaggerated expression, no performance, no full turn of the body, no turn of the torso, no swivel, no overshoot, no third hand, no third place, no figure shared across the two places, no person added to either place, no sheet coming out of either bundle, no lifting of either bundle, no turning of either bundle, no tearing of the bundle, no reading, no insert of the writing, no magnified detail of the characters, no closing title, no caption card, no end card, no credit card, no vignette, no darkened frame edge, no fade to black, no black frame, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no light change, no light change at either turn, no second object on the desk, no mug, no pen cup, no terminal, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies」「Volumetric god rays」
  「Anamorphic lens flare」「**a saturated dusk palette: magenta and gold against deep cyan shadow**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**二つの机と、その上の束と、その上に起きる二つの顔しか
  映さない。****部屋も要らない**（台帳 `locations.束`——「机の上。**束は、動かせない。**」）。
- ⚠️ **この作品は、この1本でも既に翻訳を書いている。** `s25` §2——
  「**Luminous realist anime, translated into the last two faces the work will place.**」
  **この1枚は、その訳文の側に立つ。** 訳す前の側（空）を写せば、**最後の二つの顔が、夕景になる。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**（`s01` の同じ節を見よ。）

## ⚠️ `s24` の反復である——この1枚が違えてよいのは、二人だけである

- ⛔ **この1本は `s24` の写しではない。反復である。** 動画の仕様 §17——
  「**`s24`'s motion, one more time** — ⚠️ **the two shots are a pair and the motion carries the pairing.**」
  §20 の最後の危険は、その壊れ方を名指す——
  「**The motion may be altered from `s24`'s**, which breaks the pair.」
- ⚠️ **画像の側では、これがそのまま「7欄の値」になる。** 差は**二人**であり、
  `s24` の7欄が二つの名を持つのに、この1本の7欄は別の二つの名を持つ——
  **他は同じ値である**（`SUBJECT`・`ACTION`・`LOCATION`・`LIGHT`・`ACCENT` の文面は、
  `s24` と1語も違わない。**実測 2026-09-28、この2枚を並べて数えた**）。
- ⚠️ **動画の仕様は、差を過大に名乗らない。** §8——
  「**The difference between the two shots is 0.160秒 and two people**，**and the work does not
  pretend they are more different than that.**」⛔ **ゆえにこの1枚も、差を作らない**——
  **構図を変えず、光を変えず、束の数も変えない。****変えるのは、立っている二人である。**
- ⚠️ **これは「同じ絵を2枚作る」ということではない。** **同じ舞台を2回使うということである**
  ——`s08` の同じ節（「**同じ位置で二度目を迎える**」）と、同じ規律である。
  ⛔ **但し、`s08` は一度の生成の中で二度目を迎える1本であり、この2本は別々の生成である。**
  **ゆえに揃えるのは、こちらの側の記述である。**

## ⚠️ 二つの顔を、同時に起きしてはならない

- ⛔ **これがこの1本の危険である**（`s24` と同じものである）。動画の仕様 §16 `MUST NOT`——
  「**The two faces do not rise at the same time.**」 §20 の1番目——
  「**The faces may rise together**, as in `s24`.」
- ⚠️ **画像の側では、これが二重に効く。** **1枚の絵は、二つの顔が同時に起きている絵と、
  順に起きたあとの絵を区別しない。** ゆえに `Prompt` は
  「**the second turn comes after the first and never at the same moment as it**」と書き、
  `Negative` は `no face rising at the same moment as the other face, no simultaneous turn,
  no two faces moving at once` を持つ——**順序は、動画の側の変化である。**
- ⚠️ **`bible.world.rules`**——「**手が先にあり、顔が後に来る。順序は入れ替えない。顔は、
  呼ばれた後にだけ置かれる。**」 ⚠️ **この1本がその規則を使うのは、この作品で最後である。**

## ⚠️ 歌の終わりを、この1枚に置かない

- ⛔ **この1本は、歌の終わりを画面に置かない。** 動画の仕様 §16 `MUST NOT`——
  「**Nothing marks the end of the sung section** inside this shot.」 §20の4番目——
  「**The end of the song may be marked inside the shot** — a held last frame, a fade, a silence drop
  — ⚠️ **the work puts its ending in `s26` and `s27`, not here.**」
- ⚠️ **ゆえに `Negative` に `no closing title, no caption card, no end card, no credit card,
  no vignette, no darkened frame edge, no fade to black, no black frame` を置く。**
  ⛔ **但し、この段落は動画の §16 の写しではない**——**動画の側の「fade」「silence drop」は
  時間の側の変化であり、1枚の絵はそれを運べない**（実測 2026-09-28、私が選んだ行である）。
  **この1枚が運べるのは、絵に描かれる「終わり」だけである**——**題字、黒、周辺減光。**
  ⚠️ **そして、そのどれも置かれない。****残すのは `s26`・`s27` の側である。**
- ⚠️ **動画の仕様は、この1本が自分の終わりを知らないことを、三度書いている**——
  §12「⚠️ **Nothing in the frame acknowledges it** — **the song ends over a shot that is still
  holding.**」 §14「⚠️ **the shot does not know that it is the last one with faces in it.**」
  §17「**Nothing marks the ending.**」 ⛔ **ゆえに `Prompt` は
  「**the frame does not know that it is the last one**」と書く。**

## ⚠️ 名前の註は書くが、外見は書かない——そして `identity` を添付する側である

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が二人いる**——**ゆえに註は書く**（`s07`〜`s09` は書かない。
  **手だけで、人が置かれないからである**）。⛔ **だが、外見を書き起こさない。**
  動画の仕様 §3——「**外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。**」
  ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな顔か」を教えることではない。**
- ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**顔は凍結した設定画のものである**」だけである——**註の形は、この作品で1つに決まっている。**
  ⚠️ **註が作品の持たないことを持てば、註そのものが新しい事実になる**（方針 §5a）。
- ⛔ **そして、ここが決定的である**——**`CHARACTERS` の欄は註ではない。生成器へ渡る文字列である。**
  **そこに書かれたものは、描かれる。** ⚠️ **動画の仕様が年齢や職業を書くとき、その宛先は人間である**
  ——`s06` の `Reference:` の行は「**出典の語は「路線バス運転士・52歳」である**」と引き、`s07` の同じ行は
  「**スーパー惣菜部門・45歳**」を引く。**あれは、出典についての日本語の散文であり、読み手は人間である。**
  ⛔ **同じ語をこの欄へ置けば、宛先が変わる**——**英語の入力として生成器に届き、絵になる。**
- ⛔ **そして、この1本は `identity` を2点とも添付する。** 動画の仕様 §6——
  「**この1本は `identity` を添付する。** ⚠️ **顔を置くのは、この作品でここが最後である。**」
  `shots/habits-mv-s25.yaml` の `reference_set` も同じ2点を持つ。
  ⚠️ **動画の仕様 §15**——「**Must preserve** — both people from their frozen sheets, **and `s24`'s
  motion.**」 ⛔ **この1枚の外れは、1枚で終わらない**——**この作品が顔を置くのは、
  この1本が最後だからである。**
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s25` §2 は「**Clean anime lineart**」と言い、§16 `MUST NOT` は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚は、この作品が最後に顔を写す1枚である。** ゆえに `no photographic faces` は
  **この1枚でいちばん強く効く**——**凍結した一枚はアニメの絵であり、実写ではない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、最後の二つの顔が実写になる。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s25` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**切れ目**と**同時に起きる二つの顔**と**画面に置かれた「終わり」**——
  を禁じているのは、**この段落である。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。**ゆえにこの段落は、動画の §18 の写しではない**
  ——**同じ床を、効く場所へ置いたものである。**
  ⚠️ **この1本では `no background music` が、いちばん近い行である**——
  **歌が終わる場所で、この作品は音楽を足さない**（動画の仕様 §14 の `Music`——
  「**This is the last shot under a sung line, and nothing may be added under it.**」）。
  **床と内容が、ここでも同じ方向を向く。**

- ⛔ **そして、この段落は共有の尾から1節を落としている**——`no stack of paper` である。
  ⛔ **この1本の主題は、二つの机の上の二つの束そのものである**（この稿の `Prompt`——「The bundles are paper」）。
  **尾は27本で共有されているが、その1節だけは、束を主題に持つ1本では主題を禁じてしまう。**
  ⚠️ **尾の目的は「机の上に二つ目の物を置かない」であって、「紙を描かない」ではない**——
  **この1本では、前者は `no second object on the desk, no mug, no pen cup, no terminal` が負う。**
  **ゆえに落としたのは1節であり、他の36節は一字も動かしていない。**
  ⚠️ **同じ衝突は、この作品に5本ある**——`s09`・`s10`・`s11`・`s21`・`s24`。

## ⚠️ 2026-10-01 の1枚は、左右2つの絵に割れていた——この稿で文字列を直した

- ⛔ **実測（2026-10-01）。** 著者が投入した `media/25_ChatGPT Image 2026年10月1日 03_59_55.png` は、
  **枠の中央を縦に走る継ぎ目で、左右2つの絵に割れた一枚**である——**左の絵と右の絵は、別の机の別の人である。**
- ⛔ **この1本の法も「切らない」である**（動画の仕様 §16 `MUST NOT`——
  「**No cut and no camera crossing between the two places.**」、§15 `Spatial`——
  「**the two places occupy the same frame geometry as `s24`**」）。
  ⚠️ **§20 の「A cut may be inserted between the two places.」が、まさにこの失敗である。**
- ⚠️ **直したのは2箇所である**（`s22`・`s24` の同じ節と同型）。`Prompt` の「does not cut」の文に、
  **枠が端から端まで1枚であること**（`no seam, no border, no dividing line and no panel edge`）を足し、
  `Negative` の `no transition between the two places` の隣へ、
  `no split screen, no two-panel image, no panel border, no diptych, no collage, no grid, no comic layout,
  no storyboard layout, no contact sheet, no frame within a frame, no seam,
  no dividing line between the two places` を足した。
  ⛔ **足したのは、既にある「切らない」を、生成器が読む語彙へ置き直したものである**——**新しい規則は無い。**
- ⚠️ **`half`／`halves` を `place`／`places` へ替えた**（`Prompt`・`Negative`・`LIGHT`・`ACCENT`）。
  **実測——この語は、この1枚を「二つに割る」側へ招いた**（`s22`・`s24` も同じ語を持ち、同じく割れた）。
- ⛔ **この1枚は、まだ投入し直していない。****再投入は著者が行う。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s25.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「**二つの顔が起き、最後の一行が終わる。**」
- `reference_set` は**この1本では6点**である——`清水拓也.identity`・`清水拓也.negatives`・
  `林沙織.identity`・`林沙織.negatives`・`束`・`束.appearance`。
  ⚠️ **`s24` と同じ形である**——**この1本は `identity` を2点とも含む**（動画の仕様 §6）。
- ⚠️ **食い違い1（読み取り・裁定は著者のもの）。** `shots/habits-mv-s25.yaml` の頭は
  「**この1本のあと、サビは終わる**（節末 155.505）」と書き、動画の仕様 §2 は
  「⚠️ **After this shot, the work moves to the evening**」と書く。
  ⛔ **だが、`bible.song.lines` の `l31`（155.505秒）は `outro` の行である。**
  ゆえに**歌そのものは、この1本のあと1行残っている**——`s26`・`s27` がその1行を持つ
  （`ledger.song_coverage` の最後の対応）。⚠️ **両方の文は、節の側では正しい**
  （`final-chorus` は 155.505秒で終わる）。**「歌が終わる」と「サビが終わる」は、別のことである。**
  **この1枚の側で言えるのは、節の側だけである。**
- ⚠️ **食い違い2（読み取り）。** `ledger.yaml` の `props.束.appearance` の最後の一節は
  「**一枚が、切り離される。**」だが、⛔ **この1本の束からも、一枚も出ない。**
  動画の仕様 §5——「⚠️ **この1本の束からも、一枚も出ない。** **`s11` と `s21` が一枚を出し、
  `s24` と `s25` は出さない。**」 **ゆえにこの1枚は、その一節を写さない**（`s24` と同じ扱いである）。
- `forbidden_set` の8行（`no calling voice as a sound effect`・`no face before the name is called`・
  `no watermark`・`no on-screen subtitles`・`no background music`・
  `no identifying clothing, hairstyle, or prop`・`no legible name text`・`no legible text on any surface`）
  は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** **`attached` を書くのは、送った日である。**
