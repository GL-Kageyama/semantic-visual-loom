# 画像仕様 — 『白地図』第1章「暖簾」 **S08（山）**（運動（作画） / motion / 12s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である（`L18`）。
⚠️ **この1枚は動画の最初のコマではない。** 添付（参照画像）として動画へ渡る。
⛰️ **この1本が山である。** 依頼——「暖簾に色が入ってくるシーンに盛り上がりを持って行って欲しい」。
⚠️ **この1枚が切るのは `CORE`（5-9s）である。** **白が朱に喰われている最中**——
**塗り終えた朱を切れば、この1枚はモデルへ「最初から朱」を渡すことになる**
（**12秒かけて戻るという、この1本の内容そのものが消える**）。
⚠️ **この1本だけが `transformation` を名乗る**（`PLAN.md` §0-b）。**文法は §9 と §11 が負う。**

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**回される工程である**
  - `format`: `scene-board` ／ `style`: `gouache-abstract`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hakuchizu-ch01-seg08.yaml`
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: `shots/hakuchizu-ch01-seg08.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `gouache-abstract` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`／`ASPECT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——**和は7**である。
⚠️ **`ASPECT` は `scene-board` の「16:9」と同じ値を指す。**

- `SCENE`: colour returning to a white cloth — the white being covered a course at a time along the weave
- `CHARACTERS`: nobody is in the frame and nobody is drawn on the cloth — the colour arrives because it is remembered, and no hand touches the cloth
- `SUBJECT`: the vermilion running along the weave of a noren, covering the white a course at a time, the lower courses still empty white
- `ACTION`: the colour rising from the white ground and covering the cloth a course at a time, the lower part of the cloth still white
- `LOCATION`: the front of the noren shop, the cloth seen straight on and close enough that the weave is legible
- `LIGHT`: morning light lying flat and without direction — how far the vermilion has faded is told by the density of the pigment, not by light
- `ACCENT`: the wet edge where the vermilion has run and not dried — pigment sitting on the white with body
- `ASPECT`: `16:9`

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A hand-painted abstract gouache scene board of the vermilion running along the weave of a white noren, covering the white a course at a time, the colour rising from the white ground and moving upward while the lower part of the cloth is still empty white — at the front of the noren shop, the cloth seen straight on and close enough that the weave is legible, with the wet edge where the vermilion has run and not dried catching the frame. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. Simplified large shapes, expressive hand-drawn strokes, a restrained palette, opaque gouache strokes with thin transparent washes, dry-brush texture and pigment unevenness, irregular edges, small patches of exposed paper, quiet and unfinished, like a single sketchbook page. The stroke is the event and gouache is opaque: the colour covers what it crosses, so the wet boundary of the last stroke is still visible where it stopped. The cloth the colour has not reached is empty white paper — nothing is drawn on it, and nothing is written on it or anywhere in the frame. The vermilion is the faded red of a cloth that has been through a second winter — nearer to madder than to a bright red, paler on the hems that faced the sun and deeper on the hems that stayed in shade — and its lower hems are dyed indigo. The fringe at the hem the colour has reached hangs a little to one side, as cloth that a light wind has moved and that is settling back, while the part of the cloth that is still white hangs perfectly straight and flat. The pigment is still wet: it sits on the paper with body, its surface uneven and its edges irregular, and it is not a flat evenly-painted ground. The story's four colours are in this frame, and the white ground is kept pure white, not cream or ivory. Flat and paper-based, no directional light, no spatial illusion. Nobody is in the frame: the colour arrives because it is remembered, and nobody paints it, and no hand touches the cloth.

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no flat vermilion without pigment body, no dry even vermilion paint, no uniformly painted cloth, no even flat colour field, no checkered pattern, no plaid, no printed textile pattern, no checkerboard, no strong wind or gust, no colour spilling off the cloth, no colour flooding the street, no legible text on the noren, no shop name on the noren, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no hand touching the cloth, no numerals, no numbers, no directional light

## ⚠️ ここで Negative が動く——**この1枚だけである**

`ledger.disclosure` の `negative: changed` がその記録である。**節が2つ入れ替わる**——
- **出る**: `no fully-painted flat vermilion cloth`（白い暖簾に平坦な朱が塗られては困る。
  **この危険は、色が戻った時点で消える。**）
- **入る**: `no flat vermilion without pigment body` と `no dry even vermilion paint`
  （⚠️ **危険が入れ替わるのであって、減るのではない。** 色が戻ったあとに困るのは**乾いて均した朱**である
  ——草稿 L23「朱は**まだ乾いていない**。指の腹に、**絵の具の重さ**が残る」）。

⚠️ **この入れ替えは §18（動画）の側で検査される**（`L10`）——**画像の側は誰も読まない。**
⚠️ **それでもここで同じ入れ替えをする。** 画像と動画が別々のことを禁じれば、
**添付画像が、動画の禁制と食い違う画を運ぶことになる。**

## ⛔ 2026-09-22 の指示と、その訂正で、この1枚の肯定文から「格子」と「人物」が外れた

⚠️ **著者が初回の採用候補（`08_20260922-041d36….mp4`）を観て、指示した**——
**① 画の左下の「灯」の字を外す。② ついでに「格子」も外す。**

⛔ **① 字について。** ⚠️ **この1枚の `CHARACTERS` は、初め「no figure in frame」と書いていた**——
**つまり画像の側は、人を置かないと言っていた。** **そして動画の側（§18）は、
「the woman … at the edge of the frame」と言っていた。**
⛔ **2つは食い違っており、モデルはその食い違いを、名の字を書くことで解いた。**
⛔ **私は、ここで一度誤った。** ⚠️ **著者の「「灯」という文字を外すだけね、人物は外さない」を
「この1本に人物を残せ」と読み、この1枚を動画の側に合わせた**——**人は人として置かれ、
字は置かれない、という形に。** ⛔ **著者が同じ日のうちに正した**——
「**人物は外さないを勘違いしている。／全体からは外さないという意味。／０８に人物は不要**」。
⚠️ **ゆえに、この1枚の `CHARACTERS` と1段落目は、「誰も居ない」へ戻った。**
⛔ **ただし、戻った先は初めと同じではない**——**初めは「no figure in frame」だけで、
理由が書かれていなかった。** **いまは「色は記憶から来る。誰も塗らない」が、理由として在る。**
⛔ **灯は、この作品からは外れていない**——**S06・S07 に写り、台帳の `灯.identity` は生きている**
（`specs/video/hakuchizu-ch01-seg08.md` §3 の註）。

⛔ **② 格子について。** ⚠️ **`SCENE`・`SUBJECT`・`ACTION`・`LOCATION`・1段落目から、
格子と桝目の語が外れた。** **色の器は、草稿 L15 の「布の目」である。**
⚠️ **この1枚は「布の一部が朱、一部が白」を切るので、市松の危険は残る**——
**ゆえに下の4節はそのまま残す。**

## ⛔ 2026-09-22 の裁定（第二・第三）で、この1枚の負うものが増えた

**第二（格子）**——**布に載るのは格子である。** ゆえに4節を足した——
`no checkered pattern` ／ `no plaid` ／ `no printed textile pattern` ／ `no checkerboard`
（**動画の §18 と同語**）。⚠️ **危険はこの1枚で最大である**——
**布の一部が朱、一部が白という、市松にいちばん近い状態を切っている。**
**この1枚が先に作られ、動画はこの1枚を animate する。**

**第三（たなびき）**——⚠️ **動画の側で `no swinging cloth` が落ちたが、この画像の側は
初めからこの節を持っていない。落とすものは無い。**
⛔ **逆に、この1枚では「布が動く」ことを禁じられない**——**色の着いた裾は、少し揺れている。**
⚠️ **それでも `no strong wind or gust` を1節だけ足した**（著者——「もちろん強い風は受けないよ」）。
**弱い風は肯定文が名指し、強い風は否定文が塞ぐ**——**片方だけでは、ねじれる。**

⛔ **`no movement in the part of the cloth that is still white` は、この1枚には入れない。**
**静止画は動きを持てない**——**動画の側の法である。** ⚠️ **この1枚で対応するのは、
「白いままのところは、真っすぐ平らに垂れている」という肯定文である**（1段落目）。

⚠️ **1段落目から `⚠️` を1つ落とした。** `The pigment is still wet:` の前に在った——
**この1本の文字列は生成器へ渡る。** ⚠️ **記号は、このカードの側の印であって、プロンプトではない。**
（⚠️ **走査した範囲**——`specs/image/*.md` の11枚の2段落と、`specs/video/*.md` の11本の §18。
**この1箇所だけであった。** ⚠️ **リポジトリ全体ではない。**）

## 記録との対応

- `unit` … 「薄い鉛筆の格子が置かれている」→「朱。まだ乾いていない」。**この1枚はその途中である。**
  ⚠️ **2026-09-22 の第三の指示のあと、後ろ側（S08 の側）は「格子」を名指さない**——
  **この1枚が切るのは、布が下の列から朱に覆われていく途中である。**
  ⚠️ **前側（S07 の側）が格子を持つかどうかは、未決である**
  （`specs/video/hakuchizu-ch01-seg08.md` §20 の申し送り1）。
- `beats` … **切る瞬間は 5-9s（`held`＝`CORE`、12秒のうちの4秒＝33%）**。
  ⚠️ **`video-spec` §8 は尺を不均等に配れと言う**——**この1本の不均等の在り処が、この4秒である。**
- `attached` … `暖簾の店の前.base`・`暖簾の店の前.geography`・
  `暖簾の店の前.states.朱が戻った`・`暖簾.appearance`・`暖簾.negative`
  ⛔ **`灯.identity`・`灯.negatives` が落ちている**——**2026-09-22 の著者の裁定
  「０８に人物は不要」**（`specs/video/hakuchizu-ch01-seg08.md` §3 の註）。
  ⚠️ **この1枚に人物は居ないので、人物の基準を渡す先が無い。**
  ⛔ **動画の側（§19 の `Attached` と `shots/hakuchizu-ch01-seg08.yaml` の `reference_set`）も、
  同じ5つになった**——**`L6` は両方向に突き合わせる。**
  ⚠️ **ゆえに、この1本の生成から、灯の名を持つ参照が消えた**（残るは Negative の2節）。
  ⛔ **旧い註を記録する**——**それは2度書かれた。** ①「`灯.identity` は添付されているが、
  この1枚に灯は写らない」、②「第三の指示で、この1枚は動画の側に合わせた。**添付は、
  人物の基準を渡す**」。⚠️ **①はこの1枚の実態として正しく、②は私の誤読である。**
  **いまは①に戻り、②の理由づけは消えた。**
- ⚠️ **この1枚（著者が作った初回の1枚）には、字も線も無い**——
  `08_ChatGPT Image …16_14_20.png`。⛔ **動画の側の初回生成には、両方あった**
  （§20 の `Observed Problems`）。**同じ画を指す2つの経路が、別の答えを出した。**
  ⚠️ **画像の側は「名を名指さない」を守り、動画の側は守らなかった**——**差はそこである。**
