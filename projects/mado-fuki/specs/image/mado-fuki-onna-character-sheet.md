# 画像仕様 — キャラクターシート（参照・人物 / still）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
`§18` も `Negative Prompt` も `Style Motion` も無い——それらは**動画の仕様**の持ち物である。
⚠️ **見出しに番号を振らないのは意図である。** `# 1. …` の形にすれば、`L18` が
「画像の仕様が §1–20 を持っている」と鳴る。**鳴るのが正しい。**

⚠️ **この1枚はショットではない。** `shots/*.yaml` の `key_image:` から引かれない——
ゆえに **`L22` はこの文を読まない。** 読む層が無いことを、隠さずに書いておく。
**規律は人の側に置く。**

⚠️ **この1枚は「参照」であって「画」ではない。** 動画の4本に添付して、
**同じ女であること**を運ぶために在る。**この1枚自体は、作品のどのフレームでもない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`
  - `format`: `character-sheet` ／ `style`: `cinematic-still`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml`（`world.visual_language`・`constants.窓`）＋
    `ledger.yaml`（`characters.女`）＋ `specs/video/mado-fuki-s01.md` §3 ＋
    `specs/video/mado-fuki-s02.md` §3
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- 記録: **この1枚には記録（`shots/*.yaml`）が無い。** 出来た画像の置き場と、
  `identity` へ書く語だけが下の「できたあとに」に在る。

## 主題（英語・2枚のカードの穴・8欄）

- `REF_FORMAT`: `character-sheet` —— 4つの穴（`SUBJECT`／`N`／`EXPRESSIONS`／`DETAILS`）
- `REF_STYLE`: `cinematic-still` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`GRADE`）

⚠️ **`SUBJECT` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
4＋5＝9 ではなく、**和は8**である。

- `SUBJECT`: a woman — in the work seen only from behind, dark sweater with the sleeves pushed up to the forearm, a grey cloth in her right hand, short dark hair cut to the nape, slim build, ordinary height
- `N`: five views in one row — front, straight back, back three-quarter left, back three-quarter right, and a closer back from the waist up
- `EXPRESSIONS`: no expression heads — the row beneath the figures holds the right hand and the cloth instead
- `DETAILS`: the cloth's wrung edge and the way the right hand takes it, the sleeve rolled to the forearm, the sweater's shoulder seam, the hem where it falls over the trousers
- `ACTION`: standing still, arms relaxed and clear of the silhouette, the cloth held down at her right side
- `LOCATION`: a plain white ground, no scene
- `LIGHT`: flat even light, no cast shadow
- `GRADE`: neutral — **no colour grade**（この作品の色はショットごとに動く。シートは色を運ばない）

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A character model sheet of a woman on a plain white ground, five views in one row: front, straight back, back three-quarter left, back three-quarter right, and a closer back from the waist up, all at the same character height and the same eye line on a shared horizontal guide, standing with her arms relaxed and clear of the silhouette, a grey cloth held down at her right side. Below the row, no expression heads: the right hand taking the cloth's edge, and the same hand pressing the cloth flat against an unseen pane and stopping. Beside the figures, enlarged detail insets of the cloth's wrung edge, the sleeve rolled to the forearm, the sweater's shoulder seam, and the hem over the trousers. Flat even light, no cast shadow, no background scene. A production reference readable as a specification, not a finished illustration. Her build is slim and her height ordinary; the sweater is dark, plain knit, with a soft shoulder and no pattern; the trousers are dark and straight; the shoes are flat and worn; her hair is short and dark, cut to the nape, and the ears stand clear of it. The face is given by its ground and not by its features: the upper half and the lower half of the face are close to equal with the lower half a little the longer, the forehead narrow, the cheekbones high and defined with the cheek beneath them flat, the corner of the jaw sharp and set low, the eyes sitting at the middle height of the face and slightly close together, the bridge of the nose straight and defined, and the ears visible and standing slightly away from the head. Her expression is neutral and unreadable. The clothing is contemporary and nothing in it dates her, and she wears no jewellery. A real person photographed under flat studio light — no anamorphic bokeh, no shallow-focus fall-off and no colour grade, because this sheet is a reference and not a frame of the film.

no profile view, no expression heads, no second person, no cast shadow, no background scene, no window, no sea, no room, no dramatic lighting, no dramatic pose, no anamorphic bokeh, no colour grade, no teal-and-orange grade, no props beyond the cloth, no mirror, no lettering of any kind, no callout lines, no annotations, no watermark, no on-screen subtitles, no CGI, no illustration, no painterly brush strokes, no makeup, no smile, no stylised expression

## ⚠️ 正面は1つ、横顔は無い（著者の裁定 2026-10-30）

**最初は正面も横顔も持たないシートとして書いた。** この作品は彼女の顔を一度も映さないからである
（`bible.yaml` の規則「彼女の顔は主役にならない。手と背中が主役である」、`negative_base` の
`no second person`、4本の §16 の `No close-up of the face`、`s02` は手と前腕だけ）。
**著者が「顔もあった方がいいのでは」と言い、正面を1枚だけ足すことにした。**

⚠️ **足した理由は顔を見せることではなく、頭の形を固定することである。** 後ろ姿で見えるのは
**輪郭**——顎の角・耳・生え際・うなじ——であって、目鼻ではない。**ground が決まっていなければ、
その輪郭は様式の平均である。** 4本は別々に生成されるので、**平均が4通りに出れば、頭が4つになる。**

⚠️ **横顔は足さない。** 横顔が要るのは、横を向く画が在るときである。**この作品にそれは無い。**
⚠️ **表情の頭（expression heads）も足さない。** この作品で彼女の表情は一度も読まれない。

## ⚠️ 顔は ground で書く（カードの「Specifying a face」）

`character-sheet` のカードが言う——**指定されない顔は中立ではなく、様式の平均である。
否定形も指定ではない**（「長くも丸くもない」は空欄であり、既定が埋める）。

- **ground＝比率と骨**である。上の仕様では7つの軸を**すべて既定の側から離して**書いた：
  上 half と下 half がほぼ等しく下がやや長い／額が狭い／頬骨が高く張り、その下の頬が平ら／
  顎の角が鋭く低い／目は顔の中ほどで、やや寄っている／鼻梁がまっすぐ立っている／耳が立ち、頭から少し離れる。
  ⚠️ **既定の側**（カードの計測）は「額が広く、目が低く、頬骨が平ら、顎が丸い、目が離れ、鼻が短く、耳が小さい」——**そこへ書けば、それは既定である。**
- **shape（下まぶた、目の下の影、唇の摩耗）は書かない。** それは**拡大の inset でしか読まれない**。
  そして **insets は手・布・袖・肩・裾に使っている**——顔の細部に枠を割かない。
- ⚠️ **この計測はアニメ様式1つで取られている**（カードの `Scope of the measurement`）。
  **写真の様式で同じように振る舞うかは未検証である**——ゆえに値を書き、**生成した1枚を見てから直す。**

⚠️ **顔の造形を選ぶことは、この作品では画面に出ない。** 4本のどれも彼女の顔を映さないからである。
**ゆえにこの選択は「彼女の顔」を決めるのではなく、4本の頭の輪郭を1つに揃えるための道具である。**
⚠️ **ただし、あとで彼女が振り向く画を作ることになったら、この顔が既に決まっている。**

## ⚠️ 代わりに何が仕様を担うか

**同じ高さ・同じアイラインの水平ガイド**と、
**手・布・袖・肩の縫い目・裾の insets**、そして**正面の1つが持つ頭の ground** である。
**カードは「情報が mood に勝つ」と言う**——その情報を、`s02` では手が、`s01`・`s03`・`s04` では
後ろ姿の輪郭が負う。⚠️ **文字は持たない**（`bible` の「読み取れる文字は無い」）。
**callout は書かず、insets が仕様になる。**

## ⚠️ カード2枚が食い違う1点と、どちらを採るか

`cinematic-still` の `## Negative` は **`no flat TV lighting`** を持ち、`## Fidelity anchors` は
**アナモルフィック・浅い被写界深度・色のグレーディング**を名指す。`character-sheet` の側は
**平らな光・影なし・白い地**を要求する。**そのまま重ねれば、2枚のカードが互いを打ち消す。**

**採るのは `character-sheet` の側である。** そのカードが自分で
*The sheet is read as a specification, so information beats mood everywhere they conflict* と
書いている——**この1枚は作品のフレームではない**からである。
ゆえに上の文は、`no flat TV lighting` を**落とし**、`no anamorphic bokeh` と
`no colour grade` を**足している**。⚠️ **これは書き漏れではない——選んだことである。**
⚠️ **色をシートに載せない理由。** この作品の色は `s01` の冷たい青緑から `s04` の金まで動く。
**動くものを参照に固定すれば、4本ともその色に引かれる。**

## ⚠️ できたあとに、何が変わるか

**済んだこと（2026-10-30）。**

1. 画像は `media/mado-fuki-onna-character-sheet.png` に在る。
2. `ledger.yaml` の `characters.女.identity` がそのファイルを名指している。
3. ⚠️ **4本の §6 には `REF_CHARACTER` を足していない。** 足せば**嘘になる**——
   `media/wan-3.0/` の4本は**この1枚より先に生成されており、添えていない。**
   **記録は、画が出たあとに宣言を書き戻さない。** 足すのは**その1本を作り直すとき**である。
4. ⚠️ **顔が出来ても、4本の §16 は 1文字も変えない。** `No close-up of the face` は残る——
   **参照に顔が在ることは、画に顔が出ることではない。**

⚠️ **ゆえに、いま在る4本の頭は揃っていない。** この1枚は**次の生成から効く。**
