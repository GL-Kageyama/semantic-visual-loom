# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第十七のショット「鍵が起き、札の面が光の中に出る——宛先は、無い」（開示 / motion / 13.963s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、開示の変化点である。** `鍵に付いた預かり札.宛先` が `unknown` から `absent` へ動く
（`ledger.disclosure` の3つの変化点のうちの2つ目）。⚠️ **世界の状態は変わっていない**——
**札には、初めから宛先が無い。****変わったのは観客の知識である。**
⚠️ **そして、この開示は画面から来ない。** 記録の `aim`——「**曲そのものが開示を持ち込む唯一の場所である。**
「宛先の無い札」——**画面が明かすのではなく、歌が明かす。**」（`l20`「宛先の無い札が、一枚。」）。
⛔ **ゆえに、この1枚は「明かす顔」を持たない**——**誰も、確かめない。**

⚠️ **この1枚は、この作品で唯一「金属」を写す1枚である。** 動画の仕様 §2 `Color Language`——
「The palette is metal, string and paper — **the one place in this work where metal appears at all.**」、
§15 `Visual`——「⚠️ **The one new value in the frame is metal.**」
⚠️ **この作品の物は、紙と手とプラスチックである**——**その中で、鍵だけが別の物質である。**

⚠️ **この1本は、この作品で3番目に長い。** 13.963秒。⚠️ **この並びは `ledger.yaml` の
`song_coverage` が27本の `duration` から数えたものである**——`s18` 14.840／`s27` 14.309／`s17` 13.963。
⛔ **記録の頭は「この作品で2番目に長い」と書いている**——**数え直せば、3番目である**（下の「記録との対応」に記した）。
⚠️ **この1本は `held` の区間を2つ持つ**——0-4.069秒（4.069秒）と 9.0-13.963秒（4.963秒）。
**和は 4.069＋4.963＝9.032秒であり、13.963秒の 65% が `held` である**
（残りは 4.069-6.5秒の `transition` 2.431秒と、6.5-9.0秒の `sparse` 2.500秒）。
⚠️ **この作品で、これほど長く止まる1本は他に無い**——**止まっているあいだ、
札の下端だけが揺れ続ける**（動画の仕様 §4 `Environmental Behavior`）。

⚠️ **この1枚が写すのは、この1本が終わったあとの状態である。** `unit.after` は
「手が鍵を起こし、**札の面が光の中に出る。宛先は、無い。**」——⚠️ **渡すのは開始のコマではない。**
⚠️ **動画の仕様 §8 の `MOVEMENT 4` は「**the face is in the light and the addressee's column is
empty**」と言う**——**この1枚は、その状態である。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **この組は、この作品の動画の仕様が既に名乗っている。** `specs/video/habits-mv-s17.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` であり、§2 `Visual Language` は
    「**Luminous realist anime, translated into a key and a tag being lifted off a desk.** **The light,
    not the figure, is the subject** — and here the tag comes up into the tube's light and goes
    translucent at the same time as it goes empty.」
    ——**動画の側が先に、この様式を「机から起こされる鍵と札へ翻訳した」と書いている。**
    画像の側はその1枚である。
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s17.yaml` ＋
  **既存の出力**——**凍結した二枚**——
  `distill-essence-engine/examples/habits/character/メイン/03_侘田すみれ/ChatGPT Image 2026年9月21日 05_48_10.png`
  （**キャラクター設定画**）と `.../同/ChatGPT Image 2026年9月21日 05_54_22.png`（**表情シート**）
  ——**`ledger.yaml` の `侘田すみれ.identity` が「**二枚を一組で凍結する**」と言う組であり、
  動画の仕様 §6 も同じ先を指す** ＋ 同じ作品の既存の生成物（`media/` の動画）
- ⚠️ **`預かり札` には基盤画像が無い。** `ledger.yaml` の `locations.鍵に付いた預かり札`——
  「⚠️ **基盤画像は無い。** 意図であって資産ではない。」 ⚠️ **ゆえにこの稿が、この札の姿を
  最初に言葉で持つ**——**語が無いところでは、この1枚が語を置く側になる。**
  ⚠️ **置ける語は台帳の側に在る**——`props.預かり札.appearance`——「鍵に付いた札。
  **宛先が書かれていない。** 穴が開き、紐が通っている。」
- 添付する参照: **`specs/image/生成時参照イラスト/s17/` の2枚**——`侘田すみれ_設定画.png`・`侘田すみれ_表情シート.png`。
  ⚠️ **この2枚は、この作品の動画の側の同じ2枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s17/`。実測 2026-09-28、ハッシュが一致した）。
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
  **和が、そのまま下の7欄である**（`specmap.MODELS` の註と同じ7欄）。
- ⚠️ **`Negative` の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` が
  **段落の集合**として読むからである。
  ⚠️ **ゆえに下の1段落目は、否定で終わらない。** 様式カードの雛形は
  `Not photorealistic, …` で終わるが、**この作品はそれを2段落目に置く**——**この作品は実写ではない。**
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである。**
  ⚠️ **1段落＝1行である**（折り返さない）。**空行1つが、そのまま `Negative` を繋ぐ空行である。**
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）。
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s17` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「光の中の札の面」を写すのは、そのためである**——**渡すのは、この1本が終わった
  あとの状態＝世界の側であって、開始のコマではない。** ⚠️ **動画の仕様 §7 `Beginning` は
  「the tag is face-down on the desk beside it.」と言う**——**伏せられた面は、起きた1枚からは
  読み取れない。ゆえに変化は、動画の側に残る。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** **この作品の前提は「名は、どこにも読めない」である**
  ——**文字列に日本語の字を置けば、置かれる側へ回る。**
- 記録: `shots/habits-mv-s17.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **まだ1枚も無い。** **投入した日に、`attached` を書く。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` の註は、この1本では「手」の側である**——**顔が置かれないからである**（`s05`・`s06` と同じ形）。
⛔ **註に置くのは、人物の名と、凍結した二枚を指すことだけである。****外見は書き起こさない**（理由は下の節に書く）。

- `SCENE`: the first step of the bridge — a hand has raised a key off a desk at the end of a working day, and the paper tag tied to it hangs with its face in the light and the column where an addressee would be empty; the shot does not check the absence
- `CHARACTERS`: `[侘田すみれ: **one right hand, and no one in place** — **the hand the frozen setting sheet holds**]` — **the hand, the key and the tag are the whole figure in the frame**; **no face, no chin, no hair, no shoulder above the cuff**, no arm past the cuff, and the fingers hold the key and do not close on the tag
- `SUBJECT`: the paper tag hanging from the key, its face in the tube's light, with the addressee's column empty
- `ACTION`: the key has been lifted and is held; the tag has swung once and stopped, its lower edge not quite still; **the hand does not point at the column, trace it or turn the tag toward itself**, and nothing in the frame checks what the light has made visible
- `LOCATION`: a desk at the end of a working day, 2026 — the desk's worn wooden face, its worn edge in the near foreground, the desk's cyan filling the frame's lower half, and the room the source does not name
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera on the desk and on the hanging tag, bloom on the pale surfaces, **the tag's paper the brightest thing in the frame**, and everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the tube's hard highlight on the key's metal — **the one place in this work where metal appears at all**, and the one thing in the frame that is neither paper nor desk nor skin

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the first step of the bridge of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of a metal key raised off a desk at the end of a working day, with the paper tag tied to it hanging in the light, its face turned out of its own shadow and into the tube's — and the column where an addressee would be is empty. The key is the only metal in this frame: a metal key with a bored hole at its head, string through the tag's punched hole, and it takes the tube as a hard highlight while the tag's paper behind it does not. The tag is paper and it has come up off the desk: it hangs from the string, has swung once and stopped, and its lower edge is still a moment away from being still; the rest of what is written on it is present and cannot be made out, the marks of print and of ballpoint drawn as the different marks they are, and none of them legible. The addressee's column carries nothing at all — not a name, not a stamp, not a mark — and it is the emptiest paper in the frame. One right hand holds the key: a hand only, the back of it, the knuckles, the nails cut short, the plain cuff of a sleeve at the wrist, and no arm is in the frame past the cuff. The hand does not point at the column, trace it, turn the tag toward itself or hold it up to be looked at; there is no finger at the column, and nothing in the frame checks what the light has made visible. No head enters the frame, no shoulder, no standing figure behind the desk, and nobody looks down at the tag. The desk is wood with the polish of forearms on it, its worn edge in the near foreground, and the desk's cyan fills the frame's lower half. The light is one fluorescent tube above and behind the camera, falling flat on the desk and on the hanging tag; the tag's paper is the brightest thing in the frame, the tube is the only light, and everything the desk edge shadows has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — metal takes a hard highlight where paper does not, and there is no second tone inside either. Layered atmospheric depth from near to far; dust suspended and individually rendered around the hanging tag and over the desk, and it is the only thing in the frame that is still moving. Low visual density: one focal point, the tag's face in the light, with the desk's dark lower half carrying it. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at the height of the desk and the hanging tag, unmoving, and it does not travel toward the column. One scene, one staging; the same desk, the same tube and the same hanging tag wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no face in the frame, no head, no chin, no hair, no shoulder above the cuff, no standing figure, no second figure, no portrait, no arm past the cuff, no finger at the addressee's column, no finger tracing the column, no pointing at the column, no hand turning the tag toward itself, no turning of the tag to be looked at, no lifting of the tag, no holding up of the tag, no looking at the tag, no eye in the frame, no head entering the frame above the hand, no writing in the addressee's column, no name in the column, no filled addressee column, no stamp in the column, no printed name in the column, no second swing, no flutter, no vibration of the tag, no second key, no other keys on the string, no key in a lock, no keyhole, no door, no carrying out of the frame, no push-in on the tag, no tilt down onto the column, no rack focus onto the column, no follow of the tag, no medical equipment, no hospital interior, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no insert of the writing, no magnified detail of the characters, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies」「Volumetric god rays」
  「Anamorphic lens flare」「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この画面に、空は無い。** この1本は**机と、吊られた札と、鍵を握る手しか映さない**——
  **空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s17` §2——
  「**Luminous realist anime, translated into a key and a tag being lifted off a desk.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**吊られた札が、夕景になる。**
- ⚠️ **写してよいのは、様式の側では「語彙」だけである**——決定D の言葉では
  `style`: `luminous-anime` は「**誰の声か＝語彙**」であり、「何を見せるか」は `format` の側である。
  **ゆえに、この1枚が様式から取るのは**——clean anime lineart・cel shading・
  単一の影の段・層を成す大気の遠近・**光の中に浮いて個別に描かれる塵**・
  「**光が主役である**」という一文——**であって、空と夕景ではない。**
  ⚠️ **この1本では、光が「面を空にする」**（`s17` §2——「**the tag comes up into the tube's light
  and goes translucent at the same time as it goes empty**」）。**光は、開示の道具である。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る。** **これは様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**

## ⚠️ 宛先の欄を、この1枚でも指でなぞらない——そして、カメラも指さない

- **この1本の一行は「**宛先の欄を、指でなぞらない。**」である**（動画の仕様の頭——「⚠️ **指で宛先の
  欄をなぞらない。** 「**無いことを、確かめない。**」——**この一行が、この1本の全てである。**」）。
  ⚠️ **動画の仕様 §16 `MUST NOT` はそれを二度書く**——「**The finger does not trace the empty column,
  and the hand does not turn the tag toward itself.** ⚠️ **This is the shot.**」
  「**Nobody in the frame looks at the tag** — no head enters the frame at all.」
- ⛔ **ゆえに `Negative` に `no finger at the addressee's column, no finger tracing the column,
  no pointing at the column, no hand turning the tag toward itself, no turning of the tag to be
  looked at, no looking at the tag, no eye in the frame, no head entering the frame above the hand` を置く。**
  ⚠️ **一枚の絵では、指の位置がそのまま「確かめた」になる**——**写真は動きを写せないぶん、
  この禁制はここでいちばん強い。**
- ⚠️ **カメラも指さない。** 動画の仕様 §10——「**The camera does not move to the empty column** —
  **the disclosure happens where the tag swung to, not where the lens went.**」、
  §17 の3番目——「**The camera does not point**」。
  **ゆえに `Negative` に `no push-in on the tag, no tilt down onto the column, no rack focus onto the
  column, no follow of the tag` を置く。**
  ⛔ **カメラが指せば、手が拒んだことをカメラがやることになる。**
- ⚠️ **危険は4つ、動画の仕様 §20 が名指している**——「**The finger may trace the empty column.**」
  「**The camera may move to the column**」「**The column may be filled in.** ⚠️ **A tag with a name on
  it ends the shot**」「**The key may not read as heavy**」「**A face may be placed** above the hand」
  「**The tag may flutter**」。
  ⚠️ **この段落は、そのうち4つを文字で持つ**——**「重さ」だけは、否定では書けない**
  （下の `ACCENT` が、金属の側でそれを負う）。

## ⚠️ 空なのは、宛先の欄であって、面ではない

- **この1本には、二つの禁制が同時に掛かっている。** 動画の仕様 §16 `MUST NOT`——
  「**No blank surface where the writing should be, and no nonsense glyphs** — a surface with nothing
  on it and a surface with invented marks both fail, in opposite directions.」
  そして同じ節——「**Nothing is written on the tag in the addressee's column** — **it is empty and
  stays empty.**」
- ⛔ **この二行は、両立する。** **面には字が在る**（`預かり札` の面——**読めない**）。
  **空なのは、その中の1つの欄である**——**宛先の欄は、書かれるはずの欄ではなく、
  書かれなかった欄である。** ⚠️ **台帳はそう書いている**——`props.預かり札.appearance`——
  「鍵に付いた札。**宛先が書かれていない。** 穴が開き、紐が通っている。」
  ⚠️ **動画の仕様の `Master Prompt` も同じ側に立つ**——「**Whatever else is written on the tag is
  present and cannot be made out**」。
- ⚠️ **ゆえに、この段落の `no blank surface where the writing should be` は、
  この1枚では面の側を守る行である**——**欄を埋めさせない行は、別に在る**
  （`no writing in the addressee's column, no name in the column, no filled addressee column,
  no stamp in the column, no printed name in the column`）。
  ⛔ **二つの行を逆に読めば、この1枚は「白紙の札」か「名の書かれた札」のどちらかになる。**
  **どちらも、この1本ではない。**

## ⚠️ `Not photorealistic` は、この1枚では**写す**

- **この作品は実写ではない。** `s17` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **この1枚は、この作品で唯一「金属」を写す。** 動画の仕様 §2 `Rendering`——
  「**metal takes a hard highlight and paper does not.**」
  ⛔ **実写の金属は、この作品のものではない**——**この1枚の metal は、
  セル画の一つの影の階調である。** ⚠️ **ハイライト1点で書き、質感で書かない。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、鍵が実物になる。**

## ⚠️ 註は「どの手か」だけを教える——外見は、凍結した二枚が持つ

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**）。
  ⛔ **だが、置かれるのは手だけである**——**註は「手」の側に付く。**
- ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**手は凍結した設定画のものである**」だけである——**註の形は、この作品で1つに決まっている**
  （`s05`・`s06` と同じ形）。
- ⚠️ **理由は「禁じられているから」ではない。宛先が違うからである。** この欄の値は
  **生成器へ渡る文字列**である——**同じ語が、動画の仕様の中では、出典について人間が読む
  日本語の散文であり、この欄では、モデルが読む英語の入力である。**
  ⛔ **中身が同じでも、宛先が違えば、起きることは違う。**
- ⛔ **この人物の `prompt.md` の出典の欄（`26` 行目）——「**女41・介護支援専門員・
  神奈川県横浜市戸塚区**」——を、註に持ち込まない。** **それは出典の要約であって、註の仕事ではない。**
- ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな手か」を教えることではない。**
  動画の仕様 §3——「**凍結した二枚が外見である。** 置くのは**右手だけ**である。⚠️ **顔は置かない。**」
- ⚠️ **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `identity` を添付する側である——この1枚が、その一枚である

- ⛔ **この1本は `identity` を添付する。** 動画の仕様 §6——「**この1本は `identity` を添付する。**
  ⚠️ **顔は置かない。**」 ⚠️ **顔を置かない1本であるのに添付するのは、手の造形のためである。**
- ⚠️ **ゆえに、この1枚は「手の一枚」そのものである。** 動画の仕様 §15 `Identity`——
  「**Must preserve** — the hand of the frozen setting sheet, **and the same person as the hand in
  `s18`.**」 ⛔ **この1枚の外れは、1枚で終わらない**——**`s18` の手が、同じ人物でなくなる。**
- ⚠️ **そして、この人物は二枚一組で凍結されている。** `ledger.yaml` の `侘田すみれ.identity`——
  「**二枚を一組で凍結する。**」 ⚠️ **手しか写さない1枚でも、二枚を渡す**——
  **凍結の単位は「二枚」であって、「写る部分」ではない。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
  ⚠️ **この作品の動画の仕様は、それを §18 の前書きに書いている**
  （`s17` §18——「**`Negative Prompt` を、この経路は床として受け取らない**」）。
- ⚠️ **ゆえに、この作品の床が「床」として実際に効く段は、ここだけである。**
  図の側の失敗——**なぞる指**と**埋まった欄**と**白紙の面**——を禁じているのは、**この段落である。**
- ⛔ **この1本では、危険が「確かめること」にある。** §17 の1番目——「**The absence is shown and not
  checked** — ⚠️ **a finger tracing the column turns a disclosure into a demonstration.**」
  **ゆえにこの段落は `no finger at the addressee's column` を先頭の側に置く。**
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

## 記録との対応

- この仕様を指す欄: `shots/habits-mv-s17.yaml` の **`key_image`**（この稿で足した）
- `unit.after`（この1枚が写す状態）: 「手が鍵を起こし、**札の面が光の中に出る。宛先は、無い。**」
- `reference_set` は**この1本では5点**である——`侘田すみれ.identity`・`侘田すみれ.negatives`・
  `預かり札`・`預かり札.negative`・`鍵に付いた預かり札`。
  ⚠️ **この1本は `identity` を含む**（動画の仕様 §6——**顔は置かないが、手の造形を渡す**）。
  ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した二枚を渡す）。
- ⛔ **食い違い1（読み取り・裁定は著者のもの）。** 動画の仕様 §3 は `Reference` を
  ⛔ **下に引く2行は実在しない。** **誤りを名指すために引いているのであって、
  ここから写してはならない**（実在する2枚は、この節のすぐ下に別に書いてある）——
  `.../メイン/03_侘田すみれ/ChatGPT Image 2026年9月18日 20_29_36.png`（キャラクター設定画）＋
  `.../ChatGPT Image 2026年9月17日 21_56_32.png`（表情シート）と書く。
  ⚠️ **実測（2026-09-28）——その2つの PNG は、`メイン/03_侘田すみれ/` に無い。**
  `メイン/03_侘田すみれ/` に在るのは `ChatGPT Image 2026年9月21日 05_48_10.png` と
  `ChatGPT Image 2026年9月21日 05_54_22.png` の2枚である
  ⚠️ **`20_29_36` と `21_56_32` は、隣の人物のものである**——**碓氷千夏の2枚が、まさにその分である**
  （`メイン/01_碓氷千夏/`）。**ゆえに §3 の行は、指し先だけが違うのではなく、人物が違う。**
  ⚠️ **同じファイルの §6 は正しい**——**そちらは `05_48_10`＋`05_54_22` を指し、
  `ledger.yaml` の `侘田すみれ.identity` と同じ組である。**
  **この1枚は §6 の側を採った。** ⚠️ **`s18` の §3 も同じ2つの存在しない PNG を指している**
  ——**同じ誤りが2本に在る。**
  ⚠️ **その後、著者の側がこの2行を直した**（実測 2026-09-28——**動画の仕様 §3 は、
  いま `05_48_10`＋`05_54_22` を指す**。`s18` の §3 も同じ）。**ゆえに上に引いた2行は、
  いま動画の仕様には無い。** ⛔ **ここに残したのは、見つけた食い違いの記録であって、
  いまの状態ではない**——**画像仕様の側の引用だけが、古い姿を留めている。**
- ⛔ **食い違い2（読み取り・裁定は著者のもの）。** 記録の頭は
  「⚠️ **この1本は、この作品で2番目に長い。**——13.963秒。」と言うが、
  ⚠️ **`ledger.yaml` の `song_coverage` は27本を数えて
  「`s18` 14.840／`s27` 14.309／`s17` 13.963」と並べている**——**3番目である。**
  ⚠️ **同じ頭の次の行は「Bridge は曲で最も長い節（28.803秒）」と言うが、
  台帳の `侘田すみれ` の註は「**この曲で2番目に長い節である**（28.803秒）——
  ⚠️ **最も長いのは final-chorus の 29.681秒である**」と書く。**
  **この1枚は台帳の側を採った**（`s17` は3番目に長く、Bridge は2番目に長い節である）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⛔ **この1枚は、まだ投入されていない。** 実測（2026-09-28）——`specs/image/` に在る画像は
  `01_ChatGPT Image 2026年9月28日 05_34_07.png` と `02_ChatGPT Image 2026年9月28日 05_36_27.png`
  の2枚であり、**この札の画像は、まだ1枚も無い。**
  **`attached` を書くのは、送った日である。**
