# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十八のショット「一枚が切り離され、着ける者のいないまま机に残る」（開示 / motion / 14.840s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、開示の変化点の最後である。** `名札の予備.着けられた` が `unknown` から `absent` へ動く
（`ledger.disclosure` の3つの変化点のうちの3つ目、**そして最後**）。
⚠️ **世界の状態は変わっていない**——**名札は初めから着けられていない。**
**変わったのは観客の知識である。** ゆえに `disclosure_state` は `unknown` → `absent` と動く
（`shots/habits-mv-s18.yaml` の `disclosure_state` が `absent` を持つのは、そのためである）。

⚠️ **この1枚は、この作品で人を一人も置かない唯一の1枚である。** 動画の仕様 §1 `Generation Intent`——
「**everything else in the work ends with a hand at rest, and this is the only one that ends with no
hand in the frame at all.**」 ⚠️ **この作品の27本は、これまで必ず手を持っていた**——
**手が先にあり、顔が後に来る**（`bible.world.rules`）。**この1枚は、その手すら置かない。**
⚠️ **この1枚は、この作品で最も空の1枚である**（動画の仕様 §15 `Visual`——
「**This is the emptiest frame in the work.**」／§2 `Visual Density`——
「**Low, and falling to a single object.**」）。
⚠️ **但し、同じ仕様の §8 `Temporal Density` の言い方——「the work's longest held frame, and its only
empty one」——は、その仕様の頭が自ら取り消している**（「⚠️ **`priorities` に「この作品で最も長い静止であり、
唯一の空の枠である」と書いていた。** **どちらも誤りである**——**3.856秒は27本で5番目**……
**そして空の枠は `s27` の最後の7.309秒も持つ。**」）。
⛔ **ゆえにこの稿は「最も空」だけを引き、「最も長い静止」「唯一の空」は引かない。**
⚠️ **この1本は、この作品で最も長い1本である**——14.840秒（`ledger.yaml` の `song_coverage` が
27本の `duration` から数えて1番目に置く1本である）。**そのうち 3.856秒が静止である**
（`beats` の `10.984-14.840s`。動画の仕様 §17 の4番目——「**3.856秒の静止である。**」）。

⚠️ **この1枚が写すのは、この1本が終わったあとの状態である。** `unit.after` は
「一枚が切り離され、**着けられる者のいないまま、机の上に残る。**」——
⚠️ **渡すのは開始のコマではない。** 動画の仕様 §7 `Beginning` は
「**The bundle lies on the desk and the hand takes it.**」と言い、§9 `ACT_LEAVE` の `After` は
「**no hand is in the frame, and the plate is on the desk.**」と言う。
⚠️ **この1枚は、その `ACT_LEAVE` のあとである。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s18.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a bundle of nameplates being separated at one edge.**
    **The light, not the figure, is the subject** — and here it comes from above and behind, so
    **when the hand leaves, the plate it left behind is the brightest thing in the frame.**」
    ——**動画の側が先に、この様式を「端で切り離される名札の束へ翻訳した」と書いている。**
    画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s18.yaml` ＋
  **既存の出力**——**凍結した二枚**——
  `distill-essence-engine/examples/habits/character/メイン/03_侘田すみれ/ChatGPT Image 2026年9月21日 05_48_10.png`
  （**キャラクター設定画**）と `.../同/ChatGPT Image 2026年9月21日 05_54_22.png`（**表情シート**）
  ——**`ledger.yaml` の `侘田すみれ.identity` が「**二枚を一組で凍結する**」と言う組であり、
  動画の仕様 §6 も同じ先を指す**（⚠️ **この2つの PNG は、実測 2026-09-28 に実在を確かめた**）
  ＋ 同じ作品の既存の生成物（`media/` の動画）
- ⛔ **`さくら` の画像は渡さない。** `shots/habits-mv-s18.yaml` の `reference_set` が挙げるのは
  `さくら.negatives` **だけ**であり、動画の仕様 §6 も「**この1本には添付しない。**
  ⚠️ **この1本には、彼女の側は渡らない。**」と書く。
  ⚠️ **その理由も実測に在る**——`メイン/04_さくら/` に在るのは `prompt.md` だけで、
  **PNG が1枚も無い**（実測 2026-09-28。二十七名には在り、この一名には無い）。
  **ゆえにこの1枚に渡るのは、禁制の側だけである**——**`no cherry blossom, no petals, no pink` が、
  下の段落に在るのは、そのためである。**
- ⚠️ **`名札の予備` にも `束` にも基盤画像は無い。** `ledger.yaml`——
  「⚠️ **基盤画像は無い。** 意図であって資産ではない。」（`locations.名札の予備`・`locations.束`）。
  ⚠️ **ゆえにこの稿が、その姿を最初に言葉で持つ**——**置ける語は台帳の側に在る**
  （`props.名札.appearance`——「学校の指定の名札。**プラスチック。** 左袖に付く。**読めない。**
  ⚠️ **予備がある**——**着けられないまま、束の中にある。**」）。
  ⛔ **但し、後半の2語はそのままは置かない**——**下の「学校」の節を見る。**
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
  **和が、そのまま下の7欄である**。
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** 様式カードの雛形は
  `Not photorealistic, …` で終わるが、**この作品はそれを2段落目に置く**——**この作品は実写ではない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s18` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1本では、それが特に効く**——**動画の仕様 §7 `Beginning` が「束が机に在り、手がそれを取る」で
  ある以上、この1枚を先頭フレームにすれば、切り離しが起きる前の状態が消える。**
  ⚠️ **この1枚が「切り離されたあとの机」を写すのは、そのためである**——
  **渡すのは、この1本が終わったあとの状態＝世界の側であって、開始のコマではない。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** **この作品の前提は「名は、どこにも読めない」である**
  ——**文字列に日本語の字を置けば、置かれる側へ回る。**
- 記録: `shots/habits-mv-s18.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⛔ **`CHARACTERS` に、カードが求める `[名前: …]` の註を書かない。** 理由は下の節に書く——
**この1枚には人が置かれない。****註を書けば、置かれる**（`s01` と同じ形である）。

- `SCENE`: the last step of the bridge — one nameplate has been separated from its bundle along its edge and set down on the desk, and the hand that did it has left the frame; the plate stays where it was set and nobody has put it on
- `CHARACTERS`: **no one is placed in the frame** — the hand that separated the plate has already left it, and **no second person, no additional figure and no additional face arrives to take it up**; **no name is given to the model, because a name brings a person** — and the one person this plate is waiting for is exactly the one who must not appear
- `SUBJECT`: one separated nameplate lying face up at the frame's centre on the desk — plastic, a dark border and rounded corners, the characters on its face present and illegible and not in romaji — with the bundle it came off still at the frame's left
- `ACTION`: the separation is over — the seam has run the length of the plate, the plate was set down and does not bend and has not been touched since, and **nothing is done with it afterwards**; the only movement left in the frame is the dust and the light over the desk
- `LOCATION`: a desk at the end of a working day, 2026 — the desk's worn wooden top, its worn edge in the near foreground, the bundle at the frame's left, the plate at its centre, the empty middle of the frame given to the desk, and the room the source does not name
- `LIGHT`: the room's constant state — the flat light of one fluorescent tube above and behind the camera falling on the desk and on the plates, bloom on the plastic, **the separated plate the brightest thing in the frame because no hand is between it and the tube**, saturated where the light falls with deep cyan in the unlit half, and — the hand gone — **a palette that is only plastic and desk**; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the newly exposed edge the plate came away along and the tube's bloom along the top of its plastic — the one detail the frame's falling density is allowed

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the last step of the bridge of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of one plastic nameplate lying separated from its bundle on a desk at the end of a working day, with the plate at the frame's centre and the bundle still at the frame's left — and no one in the frame at all. The plate has come off the bundle along its edge: the seam has run the length of it, the plate is straight and unbent, and it lies face up and square on the desk where it was set down, its dark border and rounded corners toward the camera, and nothing has been done with it since. The characters on its face are present and cannot be made out — cut, printed and ballpoint drawn as the different marks they are, Japanese characters, none of them legible — and the bundle at the frame's left is a stack of the same plates, their characters equally present and equally unreadable, the stack's fore-edge layered and not smooth. Nobody wears it and nobody has come to: no hand is in the frame, no arm, no wrist, no cuff, no person at the desk and no one at the frame's edge — the hand that separated the plate has left, and the plate stays. The desk is wood with the polish of forearms on it, its worn edge in the near foreground, and the empty middle of the frame is given to the desk. The light is one fluorescent tube above and behind the camera, falling flat on the desk and on the plates and blooming on the plastic; the separated plate is the brightest thing in the frame because no hand is between it and the tube, the tube is the only light, saturated where it falls with deep cyan in the unlit half, and after the hand has gone the palette is only plastic and desk. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — the plastic keeps its highlight and does not bend, and it is the only material the light has to work with besides the desk. Layered atmospheric depth from near to far; dust suspended and individually rendered over the desk and the plates, and it is the only thing in the frame that is still moving. Low visual density falling to a single object: one focal point, the separated plate, with the frame emptying toward it and nothing else on the desk. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at desk height, looking slightly down, the plate at the centre of the frame and the bundle at its left edge, unmoving, and the frame held after the hand has gone. One scene, one staging; the same desk, the same tube and the same plate wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no head, no chin, no hair, no shoulder, no cuff at the frame's edge, no hand in the frame, no arm in the frame, no wrist, no fingers, no sleeve, no person at the desk, no person behind the desk, no standing figure, no figure at the frame's edge, no second person, no additional figure, no additional face, no wearer, no one putting the plate on, no plate worn, no plate on a sleeve, no plate pinned to clothing, no plate held up, no plate lifted again, no plate carried away, no plate carried out of the frame, no plate put back on the bundle, no second plate separated, no plate half-separated, no plate still joined to the bundle, no bend in the plate, no torn plate, no curved seam, no overshoot, no second separation, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji in place of the Japanese name, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no blank plate, no unmarked plate, no signature, no handwriting by the subject, no cherry blossom, no petals, no pink, no medical equipment, no hospital interior, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies」「Volumetric god rays」
  「Anamorphic lens flare」「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**机と、その上の一枚と束しか映さない**——
  **枠は、この作品で最も空である**——**空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s18` §2——
  「**Luminous realist anime, translated into a bundle of nameplates being separated at one edge.**」、
  §254——「Luminous realist anime, translated into a bundle of school nameplates being separated at
  one edge」）。**この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**名札の束が、夕景になる。**
- ⚠️ **この作品の光は、天井の蛍光灯1本である。** 動画の仕様 §13——
  「**Fluorescent over a working desk at the end of the working day**, with the style's bloom on the
  pale surfaces. The tube is above and behind the camera and **the room's own light has not been
  switched off yet; outside there is nothing left to see.**」
  ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。**
- ⚠️ **この1本では、光そのものが変化の一部である。** §13 `Lighting Events`——
  「**The plate is bright after the hand has left because the hand is no longer between it and the
  tube** — **the light does not change; the frame does.**」
  ⚠️ **この1枚が「最も明るいのは、切り離された一枚である」と書くのは、そのためである**——
  **空から降りてくる光ではなく、手がどいた跡の光である。**

## ⚠️ この1枚に、人は一人も置かれない——註も書かない

- **この1本は、この作品で唯一、手が画面から出る1本である**（動画の仕様 §1——「**this is the only one
  that ends with no hand in the frame at all**」／§9 `ACT_LEAVE` の `After`——
  「**no hand is in the frame, and the plate is on the desk.**」）。
  ⛔ **ゆえに `CHARACTERS` に `[名前: …]` の註を書かない**——**註を書けば、置かれる。**
  ⚠️ **理由は「禁じられているから」ではない。宛先が違うからである。** `CHARACTERS` の値は
  **生成器へ渡る文字列**である——**動画の仕様に書けば、出典について人間が読む日本語の散文であり、
  この欄では、モデルが読む英語の入力である。** **中身が同じでも、宛先が違えば、起きることは違う。**
  ⚠️ **この1枚は、その極端な場合である**——**置かれる人が一人も居ないので、註そのものが無い。**
- ⚠️ **この1枚で実際に働く禁制は、「人物を描かない」ではなく「手が戻らない」である。**
  §20 `Anticipated risks` の1番目——「**A second person may be placed.** ⚠️ **The first risk of this
  shot**…… **a nameplate on a desk with nobody to wear it reads, to a generator, as an unfinished
  scene.****Anyone in this frame — even a hand at the edge — ends the shot.**」
  ⚠️ **ゆえに `Negative` の `no hand in the frame, no arm in the frame, no wrist, no fingers,
  no sleeve, no cuff at the frame's edge` は、この段落でいちばん重い行である**
  ——**この作品の27本で唯一、手を禁じる必要が在る1本である。**
- ⛔ **そして `さくら.negatives` の一行目を、そのまま持ち込まない。**
  `shots/habits-mv-s18.yaml` の註——「**禁制集合に、彼女の一行目をそのまま持ち込まない。**
  `no person, no figure, no character, no face, no body, no human silhouette, no portrait`
  ——**この1本には侘田すみれの手が在る。** そのまま掛ければ、**その手ごと消える。**
  ✅ **不在は「人物を描かない」では作らない。** **「名札は在り、着ける者が居ない」で作る。**」
  ⚠️ **この1枚には、その手すら既に居ない**——**それでも、この行を持ち込まない理由は変わらない。**
  **「居ない」を禁制で作れば、机の上から名札まで消える**——`no portrait` は、**名札の予備という
  現場そのものを消す。** ⚠️ **この1枚が禁じるのは「着ける者」と「戻ってくる手」であって、
  「画面の中の全ての人」ではない**（`no second person, no additional figure, no additional face`
  ／`no wearer, no one putting the plate on`）。
- ⚠️ **`さくら` に渡るのは、禁制の側だけである**（`reference_set` が挙げるのは `さくら.negatives`
  だけであり、`identity` は挙げられていない）。**ゆえに `no cherry blossom, no petals, no pink` と
  `no romaji in place of the Japanese name` が、この段落に在る**——**この2行は、`s18` だけが
  11行を持つ理由そのものである**（記録の頭——「この三行は、この1本が「名札の予備」という現場を持つ故である」）。
  ⚠️ **`no romaji in place of the Japanese name` は、下の「文字は、在るが読めない」の節と対である。**

## ⚠️ 文字は、在るが読めない——二つの失敗は、反対の向きに在る

- 動画の仕様 §16 `MUST NOT`——「**No blank surface where the writing should be, and no nonsense
  glyphs** — **a surface with nothing on it and a surface with invented marks both fail, in opposite
  directions.**」 ⚠️ **この1枚は、その両方を同じ強さで禁じなければならない。**
- ⚠️ **在る側は、§18 `Master Prompt` が書いている**——「**The characters on the plates are present
  and cannot be made out.**」／§2 `Rendering`——「⚠️ **The written name is drawn as the resolution it
  is** — cut, printed, ballpoint and pencil are four different marks, **not one texture applied four
  times.**」 ⚠️ **この1枚の `Prompt` が「cut, printed and ballpoint drawn as the different marks they
  are」と書くのは、そのためである。**
- ⛔ **二つの失敗の向き**——**空の面を禁じる行**（`no blank surface where the writing should be`
  ／`no blank plate`／`no unmarked plate`）は、**白い名札を防ぐ。**
  **偽の字を禁じる行**（`no invented characters`／`no nonsense glyphs`／`no pseudo-kanji`
  ／`no real-world alphabet`／`no Latin cursive`）は、**意味の無い記号を防ぐ。**
  **どちらか一方だけを置けば、この1枚は必ずどちらかの側へ倒れる。**
- ⚠️ **そして `no romaji in place of the Japanese name` は、この対の外側に在る**——
  **字が読めないことと、字が日本語であることは、別の要求である。**
  動画の仕様 §16——「**The name on the plate is not rendered in romaji** — **it is Japanese
  characters, and it is not legible either way.**」

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s18` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」／
  `§20`——「**`L30` がこの仕様の上で鳴る。**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**戻ってくる手**と**着ける者**と**白い名札**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が「着けられること」と「持ち去られること」にある。** 動画の仕様 §16——
  「**Nobody puts the plate on.**」／「**The hand does not come back** and nothing is carried out of
  the frame with it.」、§20——「**The plate may be carried away** with the hand, **which completes a
  carrying and loses the four seconds on the desk.**」
  **ゆえにこの段落は `no wearer, no one putting the plate on` と `no plate carried away,
  no plate carried out of the frame` を、ショット固有の側に置く。**
- ⚠️ **この段落は、動画の §18 の写しではない。** 動画の §18 は27本で同一であり
  （`L10`——`disclosure` の3つの変化点が `negative: covered` を宣言している）、
  **ショット固有の禁制は `shot.forbidden_set`（引き渡しの層）が持つ**——
  ⚠️ **この段落は、その両方を効く場所へ置いたものである。**
- ⚠️ **そして `L21` が、この段落を床と突き合わせる。** 要求は**基盤の3節＋作品の5行**である
  （`bible.negative_base` の註——「**この一覧の全行が、動画の §18 `Negative Prompt` と
  画像の `Negative` の両方に要る**」）。⚠️ **要求を節に割れば5節であり、この段落はその5節を
  すべて文字として持つ**（`no watermark`／`no on-screen subtitles`／`no background music`／
  `no calling voice as a sound effect`／`no face before the name is called`）——
  **数えたのは私であり、照合するのは `L21` である。**
  ⚠️ **この段落には、さらに `侘田すみれ.negatives` の2行が入っている**
  （`no medical equipment`／`no hospital interior`——台帳の側の行である）。
  **`reference_set` が `侘田すみれ.negatives` を挙げている以上、その行はここに要る。**

## ⚠️ `束` は紙ではない——それでも `no stack of paper` は、この1枚で働く

- **この1本の `束` は、名札の束である。** 動画の仕様 §5 `OBJECTS`——「**束** — 名札が重なっている。
  **切り離しの起点である。**」、§18 `Visual Prompt`——「**A stack of plastic nameplates**, the
  school's designated kind, a dark border, rounded corners」。
  **ゆえに、この1本の `束` を「紙」と呼ぶ語は、動画の仕様の側には無い。**
- ⛔ **ところが台帳は、そう書いていない。** `ledger.yaml` の `props.束.appearance`——
  「**紙の束。伝票・名簿・札。**端が揃っていない。**一枚が、切り離される。**」
  ⚠️ **そして `props.束` の註自身が、使うショットを `s11`・`s24`・`s25` と数えている**
  ——**`s18` は、そこに挙がっていない。**
  ⚠️ **それでも `s18` が `束` を引くのは、`props.名札.appearance` の側が
  「⚠️ **予備がある**——**着けられないまま、束の中にある。**」と言うからである**
  ——**名札は、束の中に在る。**
- ⚠️ **この食い違いは、この段落では解かない**（下の「記録との対応」に書く）。
  ⚠️ **但し、この段落に `no stack of paper` が入っていることは、ここで効く**——
  **この一行が、名札の束を紙の束として描かせない。**
  ⚠️ **37節の末尾は27本で同一であり、この1本のために足した行ではない**
  （`L10`——§18 は変わらない）。**それでも、この1本では意味が変わる行である。**

## ⚠️ 空の枠を、空のまま渡す

- **この1本の後半は、机と一枚だけでできている。** 動画の仕様 §4 `Environment Elements`——
  「机、その上の束、**切り離される一枚**。⚠️ **この1本の後半は、机と一枚だけでできている。**」、
  §5——「**No other object is in frame.**」
- ⛔ **生成器は、この空を埋める。** 動画の仕様 §20 の1番目の危険が「a nameplate on a desk with
  nobody to wear it reads, to a generator, as an unfinished scene」と言うのは、**この空のことである。**
  ⚠️ **ゆえに、この段落の末尾の側が `no second object on the desk, no mug, no pen cup, no terminal,
  no stack of paper` と `no wall clock, no calendar, no digital timer, no date stamp` を持つ**
  ——**机の上と壁の両方を、同時に塞ぐ。**
- ⚠️ **埋める手は3つ在る、と動画の仕様は数えている**——**人（§16「No character added beyond the
  shot」）**、**物（§5「No other object is in frame」）**、**時刻（§16「No wall clock, no calendar,
  no digital timer, no date stamp」）。** ⚠️ **この段落は、その3つを別々の行で持つ。**
- ⚠️ **そして、この1枚は静止画である。** 動画の側では「埃と光だけが動き続ける」ことで4秒が
  静止画にならない（§4 `Environmental Behavior`）。**絵の側では、埃は止まっている**——
  **ゆえに `Prompt` は「動いているのは埃だけである」と書き、`Negative` は人と物と時刻を禁じる。**
  **この2つは、同じことを二度言っていない。**

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s18` §2 は「**Clean anime lineart on the figure, drawn at one thin
  even weight with no thickening at the contour**」と言い、§16 は「**Not photorealistic, no 3D
  render, … no photographic faces**」を持つ。`REF_STYLE` は `luminous-anime`——**様式カードの
  `Negative` が `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1本の材質は、プラスチックである。** 動画の仕様 §11 `Physical Characteristics`——
  「⚠️ **The plate does not bend and does not tear** — **plastic is the work's one rigid material.**」
  ／§18 `Visual Prompt`——「**plastic keeps its highlight and does not bend.**」
  ⛔ **実写のプラスチックは、この作品のものではない**——**ハイライト1点と、1つの影の段で書く。**
- ⛔ **この1枚には、金属が無い。** この作品で金属を持つのは `s17` だけである（その稿に書いた）。
  **ゆえに `Prompt` はプラスチックを「机以外に光が働く唯一の材質」と書く**——
  **鍵は、この机の上に無い。**

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s18.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「一枚が切り離され、**着けられる者のいないまま、机の上に残る。**」
- `reference_set` は**この1本では7点**である——`侘田すみれ.identity`・`侘田すみれ.negatives`・
  `さくら.negatives`・`名札`・`名札.negative`・`束`・`名札の予備`。
  ⚠️ **`identity` は侘田すみれの1つだけで、`さくら.identity` は入っていない**
  ——**この作品で唯一、参照集合が「画面に居ない人物」の禁制だけを引く1本である。**
  ⚠️ **画像の側は、それより一歩先に立つ**——**置かれる人が一人も居ないので、`[名前: …]` の註を持たない**
  （`s01` の形）。**渡るのは、凍結した二枚（手の造形のため）と、禁制の側だけである。**
- `forbidden_set` は**この1本だけ11行である**（他の26本は8行）。増えた3行は
  `no second person, no additional figure, no additional face`・
  `no romaji in place of the Japanese name`・`no cherry blossom, no petals, no pink`
  ——⚠️ **この3行は、この段落に全部入っている**（記録の頭——「この三行は、この1本が
  「名札の予備」という現場を持つ故である」）。
- ⛔ **食い違い1（読み取り・裁定は著者のもの）。** 動画の仕様 §3 は `Reference` を
  ⛔ **下に引く2行は実在しない。** **誤りを名指すために引いているのであって、
  ここから写してはならない**（実在する2枚は、この節のすぐ下に別に書いてある）——
  `.../メイン/03_侘田すみれ/ChatGPT Image 2026年9月18日 20_29_36.png`（キャラクター設定画）＋
  `.../ChatGPT Image 2026年9月17日 21_56_32.png`（表情シート）と書く。
  ⚠️ **実測（2026-09-28）——その2つの PNG は、`メイン/03_侘田すみれ/` に無い。**
  `メイン/03_侘田すみれ/` に在るのは `ChatGPT Image 2026年9月21日 05_48_10.png` と
  `ChatGPT Image 2026年9月21日 05_54_22.png` の2枚である。
  ⚠️ **`20_29_36` と `21_56_32` は、隣の人物のものである**——**碓氷千夏の2枚が、まさにその分である**
  （`メイン/01_碓氷千夏/`）。**ゆえに §3 の行は、指し先だけが違うのではなく、人物が違う。**
  ⚠️ **同じファイルの §6 は正しい**——**そちらは `05_48_10`＋`05_54_22` を指し、
  `ledger.yaml` の `侘田すみれ.identity` と同じ組である。**
  **この1枚は §6 の側を採った。** ⚠️ **`s17` の §3 にも、同じ2行が同じ形で在る**
  ——**同じ誤りが2本に在る**（`s17` の画像仕様の側にも書いた）。
  ⚠️ **その後、著者の側がこの2行を直した**（実測 2026-09-28——**動画の仕様 §3 は、
  いま `05_48_10`＋`05_54_22` を指す**。`s17` の §3 も同じ）。**ゆえに上に引いた2行は、
  いま動画の仕様には無い。** ⛔ **ここに残したのは、見つけた食い違いの記録であって、
  いまの状態ではない**——**画像仕様の側の引用だけが、古い姿を留めている。**
- ⛔ **食い違い2（読み取り・裁定は著者のもの）。** 動画の仕様 §13 `Base Lighting` は
  「**The paper is the brightest thing in the frame**」と言う。
  ⚠️ **この1本に、紙は無い。** §5 `OBJECTS` が数えるのは**束・切り離された一枚・机の面**だけで、
  **そのどれも紙ではない**（§18——「**A stack of plastic nameplates**」）。
  ⚠️ **同じ仕様の §2 も §45 も、正しい側を書いている**——「**The palette is plastic and desk** —
  **and after the hand leaves, it is only those two.**」／「**when the hand leaves, the plate it left
  behind is the brightest thing in the frame.**」
  **ゆえに §13 の一行は、紙の1本（`s17` など）から来た敷きである。**
  **この1枚は §2・§45 の側を採った**（`LIGHT` は「**the separated plate the brightest thing in the
  frame**」である）。⛔ **そのまま写せば、この1枚に紙が生える。**
- ⛔ **食い違い3（読み取り・裁定は著者のもの）。** `ledger.yaml` の `locations.名札の予備.geography` は
  「⚠️ **この作品は、この現場を「学校」にしない。** ——**決めていないものを決めない。**」と書く。
  ⚠️ **実測（2026-09-28）——動画の仕様の側は、この現場を4箇所で「学校」にしている**
  （§13 `156` 行「the rest of the **staff room**」・§14 `164` 行「A **staff room** at the end of a
  working day」・§18 `Master Prompt` `243` 行「at a desk in a **school staff room**」・
  §18 `Visual Prompt` `254` 行「the **school's** designated kind」）。
  ⚠️ **そのうち `243` 行と `254` 行は、生成器へ実際に投入される2行である。**
  ⚠️ **台帳の側も一枚岩ではない**——`locations.名札.geography` は「**区立小学校の職員室・教室・
  昇降口**」と名指しており、`props.名札.appearance` も「**学校の**指定の名札」と言う。
  ⛔ **この1枚は「学校」を書かない。** **実測——この稿の2段落に `school` も `staff room` も
  1回も無い**（`Prompt` は「a desk at the end of a working day」とだけ書く）。
  ⚠️ **裁定は著者のものである。** この稿は、現場の側の一行（`名札の予備`）に従った。
- ⛔ **食い違い4（読み取り・裁定は著者のもの）。** `ledger.yaml` の `props.束.appearance` は
  「**紙の束**。伝票・名簿・札。」と言い、`props.束` の註は使うショットを `s11`・`s24`・`s25` と
  数える——**`s18` は挙がっていない。** ⚠️ **それでも `s18` の `reference_set` は `束` を引き、
  動画の仕様 §5 は同じ鍵の下で「**名札が重なっている**」と書く。**
  ⚠️ **台帳の側にも、`s18` を引く行は在る**——`props.名札.appearance`——
  「⚠️ **予備がある**——**着けられないまま、束の中にある。**」
  **ゆえに2つの鍵は、同じ「束」を別の材質で書いている。**
  ⚠️ **この稿は、絵の側を動画の仕様に合わせた**（プラスチックの束）。
  **そして下の段落の `no stack of paper` が、その読みを守る。**
- ⛔ **食い違い5（読み取り・裁定は著者のもの）。** 動画の仕様の §8 は
  「**the work's longest held frame, and its only empty one**」と言うが、
  **その仕様の頭が自ら取り消している**（`3.856秒は27本で5番目`・`空の枠は s27 の最後の7.309秒も持つ`）。
  ⚠️ **この1枚は、その2つの主張をどちらも引かない**——**引いたのは §15 の「最も空」だけである。**
  ⚠️ **「最も空」も、この稿が27本を並べて数えたものではない**（**動画の仕様 §15 の一行である**）。
- ⛔ **食い違い6（読み取り・裁定は著者のもの）。** 動画の仕様の頭（`8`〜`9` 行）と §3（`65`〜`67` 行）に、
  Python の文字列連結の跡が残っている——`no romaji in place of the "` ＋ 改行 ＋ 空白 ＋
  `"Japanese name`、`no additional "` ＋ 改行 ＋ 空白 ＋ `"face`。
  ⚠️ **§18 の側は正しい**（`249` 行は「no second person, no additional figure and no additional
  face」と読める）。**ゆえに投入される文字列は汚れていない**——**汚れているのは散文の側である。**
  ⚠️ **この1枚は、その3行をどちらからも写していない**（`Prompt` にも `Negative` にも、この形は無い）。
- ⛔ **この1枚は、まだ投入されていない。** 実測（2026-09-28）——`specs/image/` に在る画像は
  `01_ChatGPT Image 2026年9月28日 05_34_07.png` と `02_ChatGPT Image 2026年9月28日 05_36_27.png`
  の2枚であり、**この名札の画像は、まだ1枚も無い。**
  **`attached` を書くのは、送った日である。**
