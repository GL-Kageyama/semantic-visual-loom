# 画像仕様 — 一皿ができるまで 第1章 Clip 8/10（運動（微細運動） / motion / 5s）

⚠️ **開示の第1点である。ここで窯が開く。** この1枚から
`no oven interior`・`no visible flame`・`no glow through the door seam` の**3節が落ちる**。
⚠️ **この1枚が写すのは「開いた後」である。** 落ちた3節
（`no oven interior`・`no visible flame`・`no glow through the door seam`）は
**3節とも、この1枚で目に見える**——**開いた扉と、その中の火である。**
⚠️ **前の版は閉じた扉と隙間の光を切っていた**（「`before` の最後の瞬間」）。
著者が前提を選び直したので直した（04・06 と同じ）。
⚠️ **これで開示の落ち方が、画像と動画で同じになった。** 前の版では
**許しだけが先に落ちて、絵はまだ何も見せていなかった。**
⚠️ **この仕様は §1–20 を持たない**——**種類の話であって、モードの話ではない**（`L18` がこの形を見る）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）
- 投入: **著者が手で行う。** このリポジトリは生成を実行しない（API キーが環境に無い）
- 作る道具: `distill-essence-engine`——**回される工程である**（決定 2026-09-13）
  - `format`: `scene-board` ／ `style`: `luminous-anime`（**2つの軸を別々に引く**）
  - 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/hitosara-ch01-seg08.yaml`
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
- 記録: `shots/hitosara-ch01-seg08.yaml`

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）

⚠️ **`ACTION` と `LOCATION` は両方のカードに同名で在る**——だから**同じ値が両方の穴に入る。**
5＋4＝9 ではなく、**和は7**である。⚠️ **片方だけでは、この1枚は作れない。**

- `SCENE`: the oven open and the fire inside it moving
- `CHARACTERS`: no figure in frame, no hands
- `SUBJECT`: an iron oven door standing open, the fire inside it
- `ACTION`: burning — the fire not travelling, only trembling in place
- `LOCATION`: a one-room bakery at the wood-fired oven, before dawn
- `LIGHT`: the fire inside the open door as the only source, the room around it dark
- `ACCENT`: the firelight filling the doorway, brighter than anything else in the frame

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A luminous realist anime illustration of an iron oven door standing open with the fire inside it, burning — the fire not travelling, only trembling in place, at the wood-fired oven of a one-room bakery before dawn, with the firelight filling the doorway brighter than anything else in the frame. A scene board for the master staging of this one scene, in 16:9 — the camera and the light fixed as the standard every cut of the scene must match. The fire inside the open door is the only source, and the room around it is dark. Hyper-detailed layered light: bloom and anamorphic flare around the mouth of the oven, the flame individually rendered rather than a flat wash, dust suspended in the air in front of the door and caught by the fire. The palette has narrowed to gold and black — the gold of the fire against deep near-black in the room, the flagstones in front of the oven faintly reflective and doubling the light. Composition level and close in front of the oven, the doorway centred on the lower two thirds with the black room left open above and around it; the doorway the brightest thing in the frame. Clean anime lineart on the iron, held below the light. No figure in frame, no hands. One focal point, generous negative space.

no readable text, no Japanese kanji or kana, no real-world alphabet, no watermark, no captions, no on-screen subtitles, no human face, no full body of the baker, no second person, no wall clock, no calendar, no digital timer, no brand label or packaging text, no kitchen appliance with a display, no cut loaf, no visible crumb, no cross-section, no hand reaching into the oven, no second light source, no lamp, no shelf inside the oven, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## ⚠️ この3節が落ちることは、この1枚で**3節とも目に見える**

⚠️ **落ちる3節は、この1枚の主題そのものである。** `no oven interior` は
**開いた扉の向こう**を、`no visible flame` は**揺れている火**を、
`no glow through the door seam` は**扉いっぱいの火明かり**を禁じていた——
**この1枚は、その3つを全部描く。**
⚠️ **前の版はここが逆だった**（「扉は閉じており、中は写らないから、この1枚の絵を1画素も変えない」）。
**前の版ではそれが正しかった**——当時のこの1枚は閉じた扉だったからである。
⚠️ **そして前の版のほうが、開示の機構として正しく動いていたとは言えない。**
**許しだけが先に落ちて、絵はまだ何も見せていなかった**——
観客から見れば、**禁止が消えたことが画面に現れない。**
いまは**落ちることと見えることが同じ位置で起きる。**
⚠️ **落ちるのは「禁じる必要が無くなったから」である**——`disclosure_state` が
`KAMADO.interior: opened` になり、`ledger.disclosure` が `negative: changed` を宣言している。
⚠️ **「写らないから要らない」と「開いたから要らない」は、別のことである。**
前者なら**この1枚だけ**落とせばよい。**落ちるのはこの1枚から先の全部である。**

## ⚠️ この Negative は、開示の系列の2つ目の折れ目である

- `no oven interior`・`no visible flame`・`no glow through the door seam` … **この1本で落ちる。**
- `no cut loaf`・`no visible crumb`・`no cross-section` … **09 で落ちる。** ここにはまだ在る。
⚠️ **この作品の画像プロンプトの Negative は、ここで半分になる。**
⚠️ **この系列を読む検査は、いま無い。** `L10` は動画の §18 を相手にする。
**画像の側の相手は引き渡しの層である**（段2）。

## 記録との対応

- `unit` … 「窯の扉は閉じている」→「扉が開き、中の火だけが動いている」。
  **この1枚が写すのは `after` の側である**——**このショットの変化が済んだところ。**
- ⚠️ **§7 Beginning（"An iron door, closed, with one line of light at the seam."）は、
  この1枚ではない。** その瞬間は**動画の BEAT 1（`0-1.5s`）が担う。**
- ⚠️ **そして、落ちた3節は3節とも、この1枚の絵になっている**——隙間の光ではなく
  **開いた扉と、その中の火**だからである。**禁止が消える位置と、絵が現れる位置が同じである。**
- `disclosure_state` … `KAMADO.interior: opened` / `PAN.interior: sealed`
- `forbidden_set` … `PAN`・`KONA`
- `attached` … `BAKER.sheet`・`KITCHEN.base`・`KITCHEN.states.明け方`・`KITCHEN.geography`・`KAMADO.appearance`
