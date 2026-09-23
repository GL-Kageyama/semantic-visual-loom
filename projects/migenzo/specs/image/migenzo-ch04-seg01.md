# 画像仕様 — 『未現像』第4章「内側から」 第一のショット「一枚が消え、だれかの渦だけが残る」（開示 / still / 7s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない。

⛔ **この1本は「開示」である——そして、開いたのは誰かである。**
⚠️ **この1本の仕事は、空の底に残された光を、観客に見せることである。**
⛔ **絹は、この1本に居ない**（`shots/migenzo-ch04-seg01.yaml`）。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch04-seg01.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/migenzo/migenzo-art-board/prompt.md` と、
  同じ暗室の `migenzo-scene-board/prompt.md`（⚠️ **`_backup_20260905/` は参照しない**）
  ⛔ **人物の設定画は要らない。** ⚠️ **そして `脂痕` は、S01 と同じ物である**——
  **S01 の画像仕様（`migenzo-ch01-seg01.md`）が、この物の1度目を焼いている。**
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch04-seg01.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。
  ⚠️ **1枚在る**——`04_01_ChatGPT Image 2026年9月23日 03_19_11.png`（2026-09-23、著者が投入）。
  ⛔ **著者裁定（2026-09-24）——この1枚を採用する。** **選んだのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: an empty drawer whose bottom still remembers what was taken out of it, and one stranger's thumb mark left on the wood
- `CHARACTERS`: no figure in frame — ⚠️ **この1本に人物は入らない。** **手も入らない**
- `SUBJECT`: a wooden drawer pulled half open, empty, with a hollow in its bottom shaped like a film canister, and below the handle on the inner board a thumb's whorl printed in fine silver grains
- `ACTION`: the edge of the red safelight crossing the bottom of the drawer, lifting the hollow out of the dark, then rising to the inner board where the whorl comes up and catches
- `LOCATION`: the darkroom of the art board — the drawer pulled half out of its recess, the room's darkness behind it, the tray and its amber liquid further off in the same light island
- `LIGHT`: the room's constant state — one dim red safelight whose edge is what does the work here, and the warm amber glow of the developer tray; no time of day and no directional light
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は `unit.after` である**——**へこみと渦が、同じ枠に在るところである。**
⚠️ **理由**: この1本は、**4-5s の渦が芯である**（`shots/migenzo-ch04-seg01.yaml`）。
⛔ **光がまだ底に入っていない `before` を焼けば、この1枚は「空の引き出し」でしかない**——
**この作品の語彙（へこみ＝二十年の重さ、渦＝代償の光）が、1つも入らない。**
⚠️ **2つが同じ枠に在ることは、情報の重複ではなく対である**（記録の `role` の註）。

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the emptied drawer of the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The darkroom of the art board: one windowless room whose only light is a dim red safelight, and, pulled half way out of its recess, a wooden drawer. Its wood is dry and pale — twenty years of not being opened — and inside it there is nothing at all. On the bottom of the drawer, in the wood, there is a shallow hollow shaped like a small film canister, the place where something of that size and that weight lay for twenty years; and on the inner board just below the handle there is a thumb's whorl, printed into the wood in fine bright grains with the ridge lines one by one and the tightest part of the whorl catching the light — the same way grease catches this room's light, left by a hand that is not the person who has lived here. The edge of the red safelight lies across the bottom of the drawer and is moving slowly, and where it passes each of the two marks comes up out of the dark and then goes back. Nothing else is in the drawer, nothing is being taken from it and nothing is being put into it, and no one is in this frame. `[no figure in frame, no hand]` — the drawer, the hollow and the mark, and the light crossing them. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no person, no figure, no body, no hand, no fingers, no arm, no face, no thumb, no finger, no handprint with a palm, no full handprint, no ink, no stamp pad, no paper and pencil fingerprint, no forensic ruler, no evidence marker, no measuring tape, no magnifying glass, no film canister, no film, no reel, no spool, no paper, no print, no photograph, no negative, no envelope, no ticket, no coin, no dust, no cobweb, no second drawer, no chest of drawers, no shelf, no bright evenly lit room, no polished wood, no varnished surface, no lacquer shine, no dramatic spotlight into the drawer, no glow from inside the drawer, no glowing mark, no neon, no sparkle or star effect on the mark, no text on the wood, no numbers scratched into the wood, no initials, no notches counted into the wood, no close-up of a single fingerprint

---

## ⛔ 渦は「指」ではない——この1枚でいちばん誤られやすいところである

- ⛔ **この1本の芯は、4-5s に「親指の渦が、銀の粒になって光っている」ことである。**
  ⚠️ **そして、その意味は「**これは絹のものではない**」が読めることである**——
  **脂痕と同じ光りかたをするから、観客はそれを、代償の跡ではなく、盗まれた跡として読む。**
- ⛔ **ゆえに、この1枚は指を描かない。** **描くのは、木に残った渦である。**
  ⚠️ **肯定の側が「printed into the wood in fine bright grains」と書いている**——
  **`no thumb, no finger, no handprint with a palm` は、その肯定の裏である。**
- ⛔ **そして `no close-up of a single fingerprint` を落とす理由**——
  **この1枚を指紋の接写にすれば、この1本は鑑識の画になる。**
  ⚠️ **この1本の芯は、木の底の光であって、皮膚の紋理ではない。**
- ⚠️ **`no evidence marker` / `no forensic ruler` も同じ理由である**——
  **この作品の語彙は「証拠」ではなく「代償」である**（`構想/world.md`
  「**代償の痕跡が、唯一の生身の証拠になる**」——**痕跡が証拠になるのであって、
  証拠の道具が画面に在るのではない**）。

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である。**

## 記録との対応

- `unit` … `before`「半分ほど開いている。**なかは、空である。**……**空洞は、空洞としてしか見えていない**」
  → `after`「**木の底に、フィルムの筒のかたちをしたへこみがある**……そして取っ手のすぐ下の
  内側の板に——**だれかの親指の渦が、銀の粒になって光っている。**」
- `beats` … 0-2s 暗い空洞（まだ何も光っていない）／2-4s **へこみが浮かぶ**／
  4-5s **親指の渦が浮かぶ（この1秒が、この1本の芯である）**／5-7s 光が少しずれ、渦が消え、また浮かぶ。
  ⚠️ **この1枚が切るのは 4-7s である。**
- ⛔ **絹は、ここで触れない。** **彼女はこの1本に居ない**（記録の `unit.after`）。
- ⚠️ **この1本は `still` である理由が「変化が既に終わっていること」である**——
  **ゆえに、この1枚にも、起きつつあることを置かない。**
  **在るのは、へこみと渦と、その上を渡っていく光の縁だけである。**
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`・`引き出し`・`脂痕`
  ⛔ **人物の鍵を置かない。** ⚠️ **`attached` の確定は ③ である。**
  ⚠️ **`脂痕` が S01 と同一の物であるかは ③ が判定する**（`shots/migenzo-ch04-seg01.yaml` の申し送り）。
