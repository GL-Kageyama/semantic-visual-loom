# 画像仕様 — 『ハビッツ！！！』主題歌MV『誰の名』 第四のショット「口が止まり、音が無いことだけが残る」（反応 / motion / 7.155s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。
`mode: motion` のショットにも画像は要る——**画像はそのショットの見せ場の1枚である。**
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1本は、この作品で最も静かな1枚である。** `s03` が「口が動く」で、この1本が「口が止まる」
——**二つで一つの対である**（動画の仕様 §3 の Continuity——「**`s03` が「動く」で、この1本が「止まる」である。
二つで一つの対である。**」）。⚠️ **この1本の変化は、事件ではなく減速である**（§1——
「**The shot's change is a deceleration, not an event**」）。
⛔ **ゆえにこの1枚で、いちばん難しいのは「止まっていること」ではなく「止まりきっていないこと」である。**
⚠️ **画面は止まらない。** 動画の仕様 §16——「**The light and the dust keep moving after the face is at rest.**」
⛔ **この1本に手は入らない**（§16——「No hand enters this shot.」は `s03` の側）。
⛔ **この1本に、口を置き直す運動は無い。** §16——「**The mouth does not resume.** ⚠️ **The shapes do not come back**
——a second attempt would make this the same shot as `s03` with a longer tail.」
⚠️ **この1枚は、この1本の終わりの状態を写す。** `unit.after` は
「**口が止まり、音が無いことだけが残る。**」である——**渡すのは開始のコマではない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `luminous-anime`（4つの穴）
  - ⚠️ **1本目・2本目・3本目と同じ組である。** `specs/video/habits-mv-s04.md` §6 は
    `REF_STYLE: luminous-anime (HIGH)` を名乗り、§2 `Visual Language` は
    「**Luminous realist anime, translated into a face and a page that are both coming to rest.**」
    ——**動画の側が、この1本では「静止へ向かう」と書いている。**
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-mv-s04.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/habits/character/メイン/01_碓氷千夏/prompt.md`
  と**凍結した二枚**（設定画＋表情シート）。⚠️ **この1本は `identity` を添付する側である**
  （動画の仕様 §6——「**この1本は `identity` を添付する** — `s03` と同じ口の続きである。」）。**ゆえに絵の側でも渡す。**
- 添付する参照: **`specs/image/生成時参照イラスト/s04/` の3枚**——`碓氷千夏_設定画.png`・`碓氷千夏_表情シート.png`・`碓氷千夏_キービジュアル.png`。
  ⚠️ **はじめの2枚は、この作品の動画の側の同じ2枚と、バイト単位で同一である**
  （`specs/video/生成時参照イラスト/s04/`。実測 2026-09-28、ハッシュが一致した）。
  ⚠️ **3枚目は、動画の側には無い**——**この稿で著者の側が加えた1枚である**（2026-09-28 作成）。
  ⚠️ **この1枚は、註の字を持たない**——**設定画は改訂の箱と引き出し線の註を持ち、
  表情シートは四つの枠と改訂の箱を持つ。⛔ この1枚は、白地に顔ひとつである。**
  ⛔ **この1本の画面は、字が読めてはならない**（`Negative`——`no legible text on any surface`）。
  **渡す一枚が註の字を持たないことは、この1本では渡す側の利点である。**
  ⚠️ **但し `ledger.yaml` の `碓氷千夏.identity` は、いまも二枚しか名乗っていない**——
  **この1枚は、凍結した組の外から来た参照である。**
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
  ⚠️ **この作品の動画の仕様も、同じことを書いている**（`s04` §6——「この27本は「参照画像」の型である。
  **`first_frame` ではない**」）。
  ⚠️ **この1枚が「止まった口」を写すのは、そのためである**——**渡すのは、この1本が終わった
  あとの状態＝世界の側であって、開始のコマではない。** ⚠️ **動画の仕様 §16 は
  「**The mouth's movement thins out and stops, and the stopping is the shot's change.**」と言う**
  ——**止まることは、止まった1枚からは読み取れない。ゆえに変化は、動画の側に残る。**
  ⛔ **かつ、この1枚は「動きの無い1枚」ではない。** §11 `Environmental Motion`——
  「**Dust and the light's edge are the primary movers of this shot.**」 **埃と光の縁は、静止した1枚にも描ける。**
- ⚠️ **題（`誰の名`）を、この文字列に書かない。** 1本目と同じ理由である
  （**この作品の前提は「名は、どこにも読めない」**）。
- 記録: `shots/habits-mv-s04.yaml`（**この仕様を指す `key_image` を、この稿で足した**）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）
  ⛔ **この1本の1枚は、まだ無い。**

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**
⚠️ **`CHARACTERS` には `[名前: …]` の註を書く**（`s01` と逆であり、`s02`・`s03` と同じ側である）
——**この1本には、置かれる人が居る。** ⚠️ **ただし註は「名指す」だけで、外見を書き起こさない。**
理由は下の節に書く。

- `SCENE`: the fourth step — the mouth has come to rest and nothing has taken the movement's place; the light's edge crossing the page is the only thing still moving
- `CHARACTERS`: `[碓氷千夏: **the frozen setting sheet holds her face** — the name is here only so the right sheet is taken, and no appearance is re-derived in words]` — **only the closed mouth is in the frame**, with the chin's shadow; **no eyes, no brow, no face above the mouth**, the head does not tilt, and no hand is in the frame
- `SUBJECT`: the lips closed and at rest, and the page below them that nothing has been done about
- `ACTION`: having run out rather than been braked — the lips at rest and not resuming, the jaw still, nothing said and nothing done about nothing being said
- `LOCATION`: the opened page of the attendance register on the desk at the end of a working day, 2026 — **the page below, seen from the side of the face**, with the desk's worn face barely outside the page
- `LIGHT`: the room's constant state — the flat light of a fluorescent tube above and behind the camera falling so that the mouth's own shadow lies under the lower lip, the page below brighter than the face, **the light's edge lying across the page as the one thing in the frame that is still travelling**, bloom on the pale surface at the top of the frame, the paper the brightest thing in the frame, and everything the desk edge shadows gone to deep cyan; ⛔ **枠が持つのは光そのものであって、時刻ではない**; **no sun, no sky, no directional light**
- `ACCENT`: the tube's pale bloom at the top of the frame — the only thing in a frame of skin, page and ink that is neither skin nor paper nor ink

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the fourth step of a theme-song music video — the master staging of one scene, in 16:9. A luminous realist anime illustration of the lower half of a face at rest above the opened page of an attendance register, on a desk in a school staff room at the end of a working day, with the lips closed and nothing taking the place of the movement that has just run out. Only the closed mouth is in the frame: the upper lip and the lower lip, the corners of the mouth, the shadow under the lower lip, and the chin's shadow — no eyes, no brow, no face above the mouth, and no hand anywhere in the frame. The shapes have stopped arriving; the lips are at rest and the jaw is still, and no shape returns and no second attempt is made; nothing is said, and nothing is done about nothing being said, and no sigh and no swallow and no turn of the head takes the movement's place. The page below is the same opened register: cloth over board, the thickness of a register's left sleeve, a bound spine, its fore-edge layered cream and not smooth, and on it the transfer column is on screen with characters written in ink by more than one hand, present and not readable, the marks of cut print and of ballpoint and of pencil drawn as the three different marks they are and none of them legible, and the page does not move. The mouth is in the upper third of the frame and the page is below it. The room's light is a fluorescent tube above and behind the camera, falling flat across the page and blooming on the pale surface, so that the mouth's own shadow is under the lower lip and the page below is brighter than the face; the paper is the brightest thing in the frame, the tube's pale bloom sits at the top of the frame, and everything the desk edge shadows has gone to deep cyan. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — no second tone inside one piece of cloth and no gradient inside a single material. The palette is at its narrowest here — skin going flat, page, ink, and the pale of the tube's bloom — with saturation only where the light falls. Layered atmospheric depth from near to far; dust suspended and individually rendered in the air above the page where the tube catches it, and in this frame the dust is the busiest thing on screen, and the edge of the light lies across the page where nothing else is moving. Low visual density, and it falls: one focal point, the mouth at rest and the page below it, with generous negative space and most of the frame given to the page. The blocking, the camera and the light fixed as the standard every cut of this scene must match — the lens at desk height, looking slightly down, the same placement as the three shots before it, holding the mouth and the page in one frame, the page square to the frame with its closed edge toward the camera. One scene, one staging; the same page, the same tube and the same lower half of the face wherever this staging is used.

no watermark, no on-screen subtitles, no captions, no subtitles in any language, no background music, no music bed, no score, no musical sting, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no face before the name is called, no voice, no whisper, no sigh, no breath that becomes a word, no spoken line, no audible speech, no mouth resuming, no second attempt at the shapes, no shapes returning, no closing of the eyes, no blink used as punctuation, no turn of the head, no swallow, no expression, no smile, no tears, no fear, no exaggerated expression, no eyes detailed, no gaze, no face above the mouth, no head tilt, no nod, no hand in the frame, no finger, no arm in the frame, no second figure, no person behind the desk, no new object in the frame, no second turn of the page, no rack focus onto the page, no legible text on any surface, no legible name text, no readable characters on any prop, no romaji, no real-world alphabet, no Latin cursive, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no insert of the writing, no magnified detail of the characters, no second object on the desk, no mug, no pen cup, no terminal, no stack of paper, no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare, no window light, no daylight, no directional light, no time of day, no wall clock, no calendar, no digital timer, no date stamp, no identifying clothing, hairstyle, or prop, no character added beyond the shot, not photorealistic, no 3D render, no photographic faces, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no glossy plastic page, no plastic-looking paper

---

## ⚠️ 様式カードの 空・ゴッドレイ・マゼンタの夕景を、ここに写してはならない

- `luminous-anime` の忠実の錨は**空である**——「Hyper-detailed skies, clouds layered and
  individually rendered」「Volumetric god rays」「Anamorphic lens flare」
  「**a saturated dusk palette: magenta and gold against deep cyan**」、
  そして `Visual breakdown` は「**wide and sky-heavy, a low horizon … the figure small against the world**」。
- ⛔ **この1枚の画面は、口の下半分と頁である。** 動画の仕様 §4——「**the page and the face above it,
  both at rest.**」**空が入る余地は、構図の側に無い。**
- ⚠️ **この作品は、この1本でも既に翻訳を書いている**（`s04` §2——
  「**Luminous realist anime, translated into a face and a page that are both coming to rest.**」）。
  **この1枚は訳文の側に立つ。** 訳す前の側（空）を写せば、**止まった口が、夕景になる。**
  ⚠️ **そしてこの1本では、様式の漏れがいちばん目立つ**——**画面に動くものが少ないからである。**
- ⚠️ **ゆえに `Negative` に `no sky, no sun, no sunset, no dusk sky, no god rays, no lens flare,
  no window light, no daylight, no directional light` が在る**——**様式の漏れを塞ぐ行であって、
  この作品が窓を禁じた行ではない。**（1本目の同じ節を見よ。）

## ⚠️ `Not photorealistic` は、この1枚でも**写す**

- **この作品は実写ではない。** `s04` §2 は「**Clean anime lineart**」と言い、§16 は
  「**Not photorealistic, no 3D render, … no photographic faces**」を持つ。
  `REF_STYLE` は `luminous-anime`——**様式カードの `Negative` が
  `not photorealistic` を先頭に持つ側である。**
- ⚠️ **かつ、この1枚は止まった肌を写す。** 動画の仕様 §2 `Color Language`——
  「**skin going flat**」、`Rendering`——「**Skin is drawn smooth and matte, without pores or
  specular noise.**」 ⛔ **静止した肌は、実写の肌として戻りやすい**——**ゆえに
  `no photographic faces` は、この1枚でも強く効く。**
- ⛔ **隣の作品（`migenzo`）の節（「`Not photorealistic` を、ここに写してはならない」）を、
  この作品へ写してはならない**——**写せば、この口が実写になる。**（1本目の同じ節を見よ。）

## ⚠️ 名前の註は書くが、外見は書かない

- `scene-board` の `do` は「**Give each character's distinguishing appearance … once, in square
  brackets as a hidden note the model reads but does not draw**」と言う。
- ⚠️ **この1本には、置かれる人が居る**——**ゆえに註は書く**（`s01` は書かない。**人が居ないからである**。
  `s02`・`s03` とこの1本は書く）。
- ⛔ **だが、外見を書き起こさない。** 動画の仕様 §3——
  「**凍結した二枚が外見である。**」「**この1本が置くのは `s03` と同じ口が、動きを減らしていく過程である。
  ⚠️ 新しい部位は置かない。**」 そして §6 の Reference は、凍結した二枚を `CRITICAL` として指す。
- ⚠️ **註の仕事は「どの人物か」を教えることであって、「どんな顔か」を教えることではない。**
  この1本では**その仕事を、添付された凍結の二枚が負う**——**ゆえに註は名指すだけである。**
  ⛔ **註に、年齢・性別・職業そのほかの記述を置かない。** 名のほかは、
  「**凍結した設定画が顔を持つ**」「**正しい一枚が取られるためだけに名が在る**」の2つだけである
  ——**註の形は、この作品で1つに決まっている。**
  ⚠️ **出典の語を註へ写すこともしない**——**様式カードの `do` は「distinguishing appearance」を
  一度だけ書けと言うが、この作品はそれを凍結した二枚に負わせる。**
  **これは `do` の後半（appearance）からの意図的な逸脱である**——**黙ってやらず、ここに書く。**
  `L22` は穴の名だけを見るので、**この逸脱では鳴らない。**

## ⚠️ `identity` を添付する側である——この1枚が、その一枚である

- `s01` は `碓氷千夏.identity` を**意図的に持たなかった**（「人のかたちの一枚を渡せば、生成器は顔を置く」）。
  ⛔ **`s02`・`s03` とこの1本は逆である。** 動画の仕様 §6——
  「**この1本は `identity` を添付する** — `s03` と同じ口の続きである。」
- ⚠️ **ゆえに、この1枚は「人のかたちの一枚」そのものである。** **この1枚が外れれば、
  `s03` とこの1本の口が、同じ人物の口でなくなる**（動画の仕様 §15 Identity——
  「**Must preserve** — the same face as `s03`, and the same person as the hand in `s01`.」
  「⚠️ **The mouth of `s03` and the mouth of this shot must be recognisably one mouth at two speeds.**」）。
  ⛔ **この1枚の外れは、1枚で終わらない。**
- ⚠️ **この1本の対は、この2枚で閉じる**——`s03` の1枚が「動いている口」、この1枚が「止まった口」である。
  **2枚を並べたときに同じ口に見えなければ、対そのものが崩れる。**

## ⚠️ この `Negative` は、この作品で唯一「本当の Negative」である

- **画像の経路には、否定のための専用のパラメータが在る。** 動画の経路（`SEEDANCE 2.5`）には
  **無い**——あちらは**字幕と音声だけ**を否定として扱い、残りは**散文として読む**（`L30`）。
- ⚠️ **この作品は、この経路に否定の床が無いことを、自分で宣言している**（`bible.route_limits_accepted`
  の `SEEDANCE 2.5: Negative Prompt`）。**動画の仕様 §18 は、そのことを長く書いている**——
  「**禁制は二箇所に置く**——**ここの `Negative Prompt`**（⚠️ **この経路はこれを受け取らない**）と、
  **`Master Prompt` の散文**（**この経路が実際に読む側**）。」
  ⛔ **画像の側では、下の2段落目が、その「効く側」である。**
- ⚠️ **そして、この1本の危険は映像の側に在る。** 動画の仕様 §20 の `Anticipated risks` の1番目——
  「**The mouth may resume.** ⚠️ **The most likely failure of this shot** — a generator given a face
  in a close frame will fill the stillness. **A second attempt at the shapes makes this `s03` with a
  longer tail.**」
  ⛔ **画像の側では、その「埋める動き」を `Negative` が止める**——**この段落の `no mouth resuming`
  ／`no second attempt at the shapes`／`no shapes returning` が、その行である。**
  ⚠️ **§20 の6番目——「The writing may become legible as the frame settles on the page.」も同じである。**
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

- この仕様を指す欄: `shots/habits-mv-s04.yaml` の **`key_image`**（この稿で足した）
- `reference_set` は**この1本では `碓氷千夏.identity` を含む4点**である
  （`碓氷千夏.identity`／`碓氷千夏.negatives`／`出席簿`／`出席簿の転出欄`）——**`s01` と逆であり、
  `s02`・`s03` と同じ側である。** ⚠️ **画像の側の `content` も同じ側に立つ**（凍結した二枚を渡す）。
- `forbidden_set` の8行は、**この段落の一部である**——**床の5行は、両方に要る。**
- ⚠️ **この1本が持つ2.527秒は、歌に無い。** 記録の頭——「**27.074–29.601 の 2.527秒に歌詞が無い。**
  **歌の無い時間は、画面の側が持つ。**」 **この1枚は、その2.527秒の終わりの状態である**
  ——**歌が止まっているのではなく、歌の行がまだ来ていない。**
- ⛔ **この1枚は、まだ投入されていない。** 実測（2026-09-28）——`specs/image/` に在る画像は
  `01_ChatGPT Image 2026年9月28日 05_34_07.png` と `02_ChatGPT Image 2026年9月28日 05_36_27.png`
  の2枚であり、`media/` に在るのは動画3本だけである。**この1本の分は、まだ無い。**
  **`attached` を書くのは、送った日である。**
