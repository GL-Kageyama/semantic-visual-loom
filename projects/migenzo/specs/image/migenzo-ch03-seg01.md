# 画像仕様 — 『未現像』第3章「未露光」 第一のショット「引き出しのなかの一枚が、二十年ひらかれないまま在る」（開示 / still / 8s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⛔ **この1本は「開示」である——そして、開けるのは 04 である。**
⚠️ **この1本の仕事は、一枚の在ることを、物の乾きで示すことである。**
⛔ **ゆえに、この1枚に、なかの一枚を出さない。** **答えに触れれば、幹の順序が壊れる**
（`PLAN.md` §2「幹の答えを第9章以前に出さない」）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch03-seg01.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/migenzo/migenzo-art-board/prompt.md` と、
  同じ暗室の `migenzo-scene-board/prompt.md`（⚠️ **`_backup_20260905/` は参照しない**）
  ⛔ **人物の設定画は要らない**——**この1本に人物は入らない。**
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch03-seg01.yaml`（`key_image`）
- 生成物の置き場: **`media/`**（作品の根から見た1箇所。`take.file` が名乗る先である）。
  ⚠️ **1枚在る**——`03_01_ChatGPT Image 2026年9月23日 03_17_52.png`（2026-09-23、著者が投入）。
  ⛔ **著者裁定（2026-09-24）——この1枚を採用する。** **選んだのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: a drawer that has stayed closed for twenty years, shown by nothing but how dry its wood is
- `CHARACTERS`: no figure in frame — ⚠️ **この1本に人物は入らない。** **手も入らない**
- `SUBJECT`: a closed wooden drawer standing in the dark recess of the darkroom, its wood paler and drier than any other wood in the room, its grain raised into fine white splinters
- `ACTION`: the red safelight's edge moving a little across the wood, and the dried splinters coming up one by one like white thorns, while the drawer itself does not move at all
- `LOCATION`: the darkroom of the art board — the dark back of the room, the recess where the light barely reaches, the drawer's outline just legible in it
- `LIGHT`: the room's constant state — one dim red safelight reaching only the near edge of the drawer, and the warm amber glow of the developer tray further off; no time of day and no directional light
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は `unit.after` である**——「**同じ引き出しが、この部屋でいちばん乾いたものとして、
画面にある。白いささくれの一本一本まで赤い光を受けて立っている。**」
⚠️ **理由**: `unit.before` の「ただの奥行き」は、**画にならない**——
⛔ **奥行きを焼けば、この1本は「暗い奥に箱がある」1本になり、
`開示` の固有基準（何かが知られること）が、錨の側に1つも無い。**
⚠️ **そして、この1本の変化は、物の側で起きていない**——**「変わったのは、それが何であるかである」。**
**ゆえに錨は、その「何であるか」の側を焼く。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the closed drawer of the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The dark back of the darkroom of the art board: one windowless room whose only light is a dim red safelight, and in a recess where that light barely reaches, a wooden drawer stands closed. Its wood is the palest and the driest in the room — drier than the doorframe, drier than the shelf, drier than anything else that this room has ever held — and the dryness is the whole of what is on it: the grain has lifted into fine white splinters, each one standing, so that the surface reads as a field of tiny white thorns rather than as a smooth panel, and the handle is the driest shape in the frame. The red safelight's edge lies across the near side of the wood and moves a little, and where it falls each splinter stands up in the light; the drawer itself does not move at all, and nothing is happening to it. The wood is closed, and what it holds is not shown and not hinted at: the frame ends at the drawer's face. `[no figure in frame]` — no hand, no person: this frame is a thing and the light on it. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no person, no figure, no body, no hand, no fingers, no arm, no face, no open drawer, no drawer pulled out, no visible contents, no film inside, no film canister, no paper inside, no print, no photograph, no envelope, no box, no label, no writing on the drawer, no sticker, no brass plate, no keyhole, no lock, no padlock, no nails, no metal fittings other than the handle, no dust in the light, no cobweb, no mouse, no insect, no other drawer, no chest of drawers, no shelf, no door, no wall clock, no calendar, no mirror, no bright evenly lit room, no polished wood, no varnished surface, no lacquer shine, no wet wood, no damp, no mould, no dark stain, no aged patina, no antique furniture look, no product photography, no centered symmetrical composition, no bright key light on the drawer

---

## ⛔ この1枚の `Negative` が、いちばん長い理由

- ⛔ **この1本の内容は「乾き」である。** ⚠️ **そして「乾き」は、生成器の既定では出てこない**——
  **既定は、艶のある、手入れされた木である。**
  ⚠️ **ゆえに、この1枚は艶を禁じ、湿りを禁じ、ニスを禁じ、アンティーク家具の見えかたを禁じる。**
- ⛔ **そして、開いた引き出しを禁じる**（`no open drawer, no visible contents`）——
  **開けるのは 04 である**（`shots/migenzo-ch03-seg01.yaml` の `beats` 6-8s）。
  ⚠️ **開いた画を焼けば、この1枚は次の1本の答えを先に置く。**
- ⚠️ **`no product photography` / `no centered symmetrical composition` を落とす理由**——
  ⛔ **「乾いた木の箱」は、生成器にとって商品写真の題材である。**
  **この1枚は、闇の奥にある物である**——`documentary-photo` の物理がそれを決める。

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である。**
  ⚠️ **そしてこの1本では、`no window` が内容である**——**この部屋の木が白いのは、
  二十年、窓を知らないからである**（`shots/migenzo-ch03-seg01.yaml` の `unit.before`）。

## 記録との対応

- `unit` … `before`「乾いて白くなった木の引き出しが、閉じている。……**まだそれは、ただの奥行きである**」
  → `after`「**この部屋でいちばん乾いたものとして、画面にある。
  白いささくれの一本一本まで赤い光を受けて立っている。**」
- `beats` … 0-3s 輪郭だけが見えている／3-6s **ささくれが浮かぶ（主題はこの3秒で立つ）**／
  6-8s 動かない。そのまま終わる。⚠️ **この1枚が切るのは 3-8s である。**
- ⛔ **埃を足さない。** **この部屋は `no window` であり、埃の源が無い**
  （`shots/migenzo-ch03-seg01.yaml` の `motion.subject`）。**ゆえに `no dust in the light` が在る。**
- ⚠️ **この1本の最後に残るのは、木の白さだけである**——「**なにも写っていないその白さが、
  二十年、絹のなかでいちばん重い**」。⛔ **その白さは、この1本では木の側に置かれている。**
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`・`引き出し`
  ⛔ **人物の鍵を置かない。** ⚠️ **`attached` の確定は ③ である。**
