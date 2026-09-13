# 画像仕様 — 一皿ができるまで 第1章 Clip 4/10（運動（躍動） / motion / 6s）

⚠️ **これはこのショットの見せ場の1枚である。** 決定（2026-09-13、著者）で、全ショットは
画像 → 動画の順に回る。**この1枚は動画へ添付（参照画像）として渡る**——
だから**§7 Beginning の瞬間ではなく、このショットの山を切る**。
⚠️ **前の版はここを `before` の側（§7 Beginning "Flour and water sit apart"）にしていた**——
それは「画像は動画の最初のコマである」という**当時の前提**の下でのことであり、
**著者がその前提を選び直した**（同日、「見せ場の1枚」＋「添付として渡す」）。
**だから直した。**
⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である
——**種類の話であって、モードの話ではない**（`L18` がこの形を見る）。
⚠️ **02 と紛らわしい。別の1枚である。** 02 は**界面の拡大**（粉と水の境目だけ）であり、
04 は**中景の穴**（粉の窪みと、そこへ入る手）である。**尺度と、手の有無が違う。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg04.yaml`
    ——gozen-niji の `series-constants.md`（シリーズ定数＋開示台帳）と同じ型である
- 投入する文: **下の節の1段落目が `Prompt` であり、エンジンの出力であって、`chatgpt-image-2.5` へ
  投入する正典である**（決定B）。**2段落目が `Negative` である**（決定A）
- ⚠️ **下の7欄はエンジンへの入力である**——出所の記録であると同時に、そのまま流し込む穴である。
  ⚠️ **`REF_FORMAT` と `REF_STYLE` が「どのカードの穴か」を名乗る。** `L22` がそれを読み、
  **名乗ったカードが実際にその穴を宣言しているか**を確かめる——**名乗りは宣言であって、一致ではない。**
- ⚠️ **⑦Negative の出力はここではなく、下の節の2段落目へ書く。** エンジンの合成プロンプトは
  Negative を最後の一文に溶かすが、**この記録は2段落として別々に保つ**——`L21` と開示の系列が
  **段落の集合**として読む。
- ⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**——
  **見出しが本文の間にあると、選択がそれを巻き込む。** 空行1つが、そのまま `Negative` を
  繋ぐ空行である。**繋がった文字列の写しは置かない**（写しは食い違う）。
- ⚠️ **この1枚は、このショットの動画へ添付（参照画像）として渡る**——最初のコマではない。
  最初のコマにすると、**そのショットの変化が画面上で起きなくなる**（`mode` と `unit` が偽になる）
- 記録: `shots/hitosara-ch01-seg04.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the flour and the water become one mass under the hands
- `CHARACTERS`: a pair of hands, flour to the wrists — no face, no body
- `SUBJECT`: one mass of dough under a pair of flour-dusted hands
- `ACTION`: folding and turning it, the mass taking shape under the palms
- `LOCATION`: a wooden kneading bench scarred by scraping, one-room bakery, morning
- `LIGHT`: morning light from the side across the bench, the sheen of the dough catching it
- `ACCENT`: the warm gold light lying across the sheen of the dough

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of one mass of dough under a pair of flour-dusted hands, folding and turning it, the mass taking shape under the palms, at a wooden kneading bench scarred by scraping in a one-room bakery in the morning, with the warm gold light lying across the sheen of the dough as the strongest highlight. A scene board for the master staging of this one scene, in 16:9 — the blocking, the camera and the light fixed as the standard every cut of the scene must match. Morning light comes from the side across the bench and the sheen of the dough catches it. Hyper-detailed layered light: the shaft travelling through the air from a window at the frame edge, anamorphic flare and bloom around the source, flour dust suspended and individually rendered rather than a flat wash. A saturated palette of magenta and gold against deep cyan shadow, the damp bench and the taut surface faintly reflective and doubling the light. Composition low and close at the height of the bench, the mass across the lower third with the hands coming in from the frame edge; everything subordinate to the light, clean anime lineart on the hands kept deliberately below the light. The dough has already come together — one smooth mass, the surface drawn taut and taking the light. Hands and coarse linen apron only, no face, no body, no ring, no watch. Low visual density: one focal point, generous negative space. No readable lettering anywhere.

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no oven interior, no visible flame, no glow through the door seam, no cut loaf, no visible crumb, no cross-section, no second hand, no dough hook, no bench scraper, no flour cloud, no flour storm, no loose flour heap, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この1本だけに足した語がある——**失敗の形を先に名指しする**

この1枚は**捏ねの山**である——**生地は既にひとつにまとまり、表面が張っている。**
⚠️ **だから「まだまとまっていない」形を禁じる語を落とした。** 前の版はここに
`no formed dough`・`no smooth elastic mass` を置いていた——**それは当時の前提
（この1枚＝§7 Beginning の瞬間）の下でのことであり、いまは偽である。**
まとまっていない塊を禁じることは、**この1枚が写すものを禁じること**になる。
⚠️ **禁制は、ショットが変わるときに一緒に見直さねばならない**——
前の版の語は、前の版の絵に対しては正しかった。
残したのは `no flour cloud`・`no flour storm`・`no loose flour heap` である——
粉は**光の中に浮いている**ものであって、**巻き上がっても、山で残ってもならない。**
`no second hand` も同じである——**手は1つだけ**、しかも**枠の縁から**入る。
⚠️ **禁じる語を足すことは、欠陥を消すことではない。** 消えるかどうかは生成を見なければ
分からない。**足したのは、失敗の形を先に名指しするためである。**

## ⚠️ この Negative は、開示の系列の一部である

`no oven interior`・`no visible flame`・`no glow through the door seam` の3節は、
**08 で開くまで全部の画像プロンプトに在り、08 で落ちる。**
`no cut loaf`・`no visible crumb`・`no cross-section` の3節は、**09 で割るまで在り、09 で落ちる。**
⚠️ **この系列は、動画の §18 と同じ系列である。** 同じ禁制が、2つの経路の両方に要る
——**この1枚が動画へ添付として渡るからである。** 画像が窯の中を写していれば、
その絵が**参照画像として動画の中へ入り**、§18 が禁じているものを**動画の側で開けてしまう。**
⚠️ **「最初のコマだから」ではない**（前の版はそう書いていた）。
**添付だからである**——禁制は、渡る経路の**両方**で守られねばならない。
⚠️ **この系列を読む検査は、いま無い。** `L10`・`L14` の相手は §18 である。
**相手は引き渡しの層である**（段2）。

## 記録との対応

- `unit` … 「粉と水は、まだ別々にそこにある」→「手の下で、ひとつの塊になる」。
  **この1枚が写すのは `after` の側である**——**このショットの変化が済んだところ。**
- ⚠️ **`before` の側はここに無い。** §7 Beginning は "Flour and water sit apart in the
  same hollow." と言うが、**この1枚はその絵ではない。** その瞬間は
  **動画の BEAT 1（`0-1.5s`）が担う**——⚠️ **`before` はどの画像にも写らない。**
- ⚠️ **これは欠落ではない。** 見せ場の1枚とは**そういう1枚**である——
  **変化の結果を1枚に固定し、その1枚へ向かって動画を走らせる。**
- `motion`（**画像へは行かない**）… 「押し、畳み、回す」。**この1枚には現れない**
  ——1枚は動かない。動くのは動画の側である。
- `forbidden_set` に `KAMADO`・`PAN` … **窯もパンも、まだ画面に出ない。**
- `attached` … `BAKER.sheet`・`KITCHEN.base`・`KITCHEN.geography`・`KONA.appearance`・`MIZU.appearance`
