# 画像仕様 — 『未現像』第2章「見ないことの記録者」 第一のショット「二十年が、この部屋を通り過ぎる」（モンタージュ / motion / 9s）

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
**§18 も `Negative Prompt` も `Style Motion` も無い**——それらは**動画の仕様**の持ち物である。
⚠️ **これは `mode` の話ではない。** 画像の仕様は**どのショットでも** §1–20 を持たない
——**種類の話であって、モードの話ではない**（決定 2026-09-13、著者）。

⚠️ **この1本の文法は `time-fold` である**（`PLAN.md` §0-b）——
⛔ **ゆえに、この1枚に「動き」を焼かない。** **この1本には出来事が1つも無い。**
⚠️ **床の要求は「切らない」である**（`no cut, no time-skip, no cross-dissolve`）——
**画像の1枚には、その要求が最初から満たされている。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは生成を実行しない
- 作る道具: `distill-essence-engine`——**2つの軸を別々に引く**
  - `format`: `scene-board`（5つの穴）／`style`: `documentary-photo`（5つの穴）
- 入力（`content`）: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/migenzo-ch02-seg01.yaml` ＋
  **既存の出力**——`distill-essence-engine/examples/migenzo/migenzo-art-board/prompt.md` と、
  同じ暗室の `migenzo-scene-board/prompt.md`（⚠️ **`_backup_20260905/` は参照しない**）
  ⛔ **人物の設定画は要らない**——**絹の体は、この枠に入らない。**
- 投入する文: **下の節の1段落目が `Prompt`、2段落目が `Negative`**
- ⚠️ **1段落＝1行である**（折り返さない）。
- ⚠️ **この1枚は動画へ添付（参照画像）として渡る**——最初のコマではない。
- 記録: `shots/migenzo-ch02-seg01.yaml`（`key_image`）
- 生成物の置き場: このディレクトリ。
  ⚠️ **第二世代が在る**——`02_01_ChatGPT Image 2026年9月24日 00_53_17.png`（2026-09-24、焼き直し）。
  ⚠️ **第一世代は、このディレクトリに無い**（**実測**、2026-09-24——このディレクトリの `02_01_*` は、この1枚だけである）。
  ⚠️ **`git status` は、この位置について何も言わない**——**第一世代が在った場所を、この稿は見ていない**（追跡されていた形跡も無い）。
  ⛔ **著者裁定（2026-09-24）——この1枚を採用する。** **選んだのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。

## 主題（英語・2枚のカードの穴・7欄）

- `REF_FORMAT`: `scene-board` —— `SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`
- `REF_STYLE`: `documentary-photo` —— `SUBJECT`／`ACTION`／`SCENE`／`LIGHT`／`ASPECT`
- ⚠️ **同名の3欄（`SCENE`・`ACTION`・`LIGHT`）には同じ値が入る。** **和は10ではなく7である。**

- `SCENE`: twenty years passing through one room without a single event — a shadow on the wall getting heavier and nothing else changing
- `CHARACTERS`: no figure in frame — ⚠️ **壁の影だけである。** **影を落としている体は、この枠の外に立っている**
- `SUBJECT`: a woman's shadow lying thin on the darkroom wall, and, lower in the frame, the developer tray with its amber liquid and the red light above it — both of them unchanged
- `ACTION`: the shadow thickening very slowly, continuously, with no step in it, while the tray and the red light in the frame do not change at all
- `LOCATION`: the darkroom of the art board — one windowless room, the wall taking the most of the frame, the tray below
- `LIGHT`: the room's constant state — the dim red light of a safelight that stands outside the frame, which is also what lays the shadow on the wall, and the warm amber glow of the developer tray; ⛔ **枠が持つのは光そのものであって、灯ではない**; no time of day and no directional light
- `ASPECT`: 16:9, landscape

⛔ **この1枚が切る瞬間は `unit.after` である**——「**影だけが濃くなっている。**」
⚠️ **理由**: `unit.before` と `after` の差は、**画面では濃さだけである。**
**ゆえに錨は、その濃さの側を焼く**——**濃さは、この1本の答えそのものである。**
⚠️ **そして、この1枚の影は、この1本の9秒のどこにも「動かない」**——
**`draft_02-4` の「影の指が独りでに動く」は、第2章の後半の出来事である。**

## 投入する1本の文字列（英語・1段落目が `Prompt`、2段落目が `Negative`）

A scene board for the twenty years that pass through the darkroom in the novel 『未現像』 ("Undeveloped") — the master staging of one scene, in 16:9. The wall of the darkroom of the art board takes most of the frame: one windowless room lit by a safelight that stands outside the frame — what is in the frame is the red light it makes, lying on the wall and on the near rim of the tray, and not the fixture that makes it — everything outside the light's reach sunk in near-black, and lower in the frame the developer tray with its amber liquid lying still. On the wall the safelight lays the shadow of a woman — a thin, quiet silhouette, standing, the shape of a person who has stood in the same place at the same height facing the same way for twenty years — and her body is not in the frame; only what the light does with it is. The shadow lies a little heavier than the woman it belongs to: the fingertips of the shadow are a little fuller than fingertips are, as though the shape had gathered weight without changing its outline. The tray and the red light lying on the wall are exactly as they were at the beginning; nothing about them has changed and nothing about them is moving. There is no event anywhere in this frame. `[no figure in frame — only the shadow of a woman, cast on the wall]`; the person who casts it is outside the frame. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. The palette is held to the red of the safelight, the amber of the developer and the silver-white of the paper, and the red and amber are kept to their sources and never stain the whole frame. The same place as the art board. No typography anywhere in the frame.

no watermark, no on-screen subtitles, no background music, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no small hand pressing the lens, no person, no figure, no body, no face, no second shadow, no two shadows, no silhouette of a child, no shadow of a second person, no moving shadow, no long dramatic shadow with hard edges, no shadow of a hand raised, no cast shadow with a visible light source in frame, no lamp, no bulb, no bare light source, no window light, no sunbeam, no dust in the air, no ripple on the liquid, no drop falling, no bubbles, no print in the tray, no film in the tray, no tongs, no open drawer, no bottles or jars, no enlarger, no clock on the wall, no calendar, no mirror, no poster or picture on the wall, no pipes, no cables, no bright evenly lit room, no glossy floor, no portrait lighting, no clean modern darkroom, no stainless steel, no dramatic mood lighting

---

## ⚠️ 影は「人物」ではない——そして、この1枚の `Negative` は、そこを分ける

- ⛔ **`bible.negative_base` の核2節は、娘の顔を禁じているだけである。**
  ⚠️ **この1枚に要るのは、それとは別の禁止である**——**影のほかに人物を置かない。**
  **ゆえに `no person, no figure, no body, no face` がここに在る。**
- ⚠️ **そして、肯定の側が影を名指している**——「a thin, quiet silhouette … her body is not in the frame;
  **only what the light does with it is**」。⛔ **否定形だけでは、生成器は人物を足す。**
- ⛔ **「濃い影」を、演出にしない**——`no long dramatic shadow with hard edges` がそれである。
  ⚠️ **この部屋の影は、赤い安全光が壁に落とす、ふつうの影である。**

## ⚠️ `Not photorealistic` と `available natural light` を、ここに写さない

- ⛔ **どちらも写さない**——**根拠は `migenzo-ch01-seg01.md` の該当2節である**
  （ボード由来の句であり、この作品の様式ではない）。**赤い安全光は、到着しない。**

## ⛔ 灯を、肯定の側から枠の外へ出す（2026-09-23、著者裁定＝再生成）

- ⚠️ **焼かれた1枚**——`02_01_ChatGPT Image 2026年9月23日 03_04_21.png`。**見えたままを書く。**
- ⛔ **この1枚は、焼き直す**（2026-09-23、著者——「推奨で進めよ」）。
  **理由は1点である**——**赤い安全光の灯そのものが、枠の左上に入った。**
  ⚠️ **芯（壁の薄い影と、下のトレイ）は在る。**
- ⛔ **そして、この1枚は機械で鳴らせる唯一の違反を持つ**——
  **この `Negative` は `no lamp` / `no bulb` / `no bare light source` を持ち、
  `no cast shadow with a visible light source in frame` まで持つ。それでも灯が描かれた。**
- ⚠️ **原因は、否定の側ではなく、肯定の側である**——**初稿のプロンプトは
  「one windowless room whose only light is a dim red safelight」と書いていた。**
  ⛔ **「安全光」と名指せば、生成器は安全光の器具を描く。**
  ⚠️ **同じ一文が、既存のアートボードにも在る**（`migenzo-art-board/prompt.md`——
  「lit only by a dim red safelight」）。**すなわち、この作品の既存の言語が、灯を持つ。**
- ⛔ **ゆえに、直したのは肯定の側である**——**灯は枠の外に立ち、枠が持つのはそれが作る赤い光である。**
  ⚠️ **`Negative` は1節も足していない**（**既に足りていた。足りなかったのは肯定の側である**）。
- ⚠️ **これは `bible.constants.光`「光は、方向ではなく状態である」の帰結である**——
  **器具が枠に入れば、光は「その場所の状態」でなく「部屋の物」になる。**
- ⛔ **動画の仕様（`specs/video/migenzo-ch02-seg01.md` §16・§18）は、既にこれを禁じている。**
  **ゆえに、この1枚をそのまま添付すれば、§16 と参照画像が食い違う。**

## 記録との対応

- `unit` … `before`「薄い影が、輪郭をなぞっている」→ `after`「**影だけが濃くなっている。
  それはもう輪郭をなぞる影ではなく、彼女の体より少し重いもの**である」。
- `beats` … 0-3s 「いま」／3-6s 濃さが連続で増す／6-9s **影は、絹の体より重い。それだけが二十年である。**
  ⚠️ **この1枚が切るのは 6-9s である。** ⛔ **段を置かない**（置けば「何かが起きた」になる）。
- `role: モンタージュ` … ⚠️ **この1本の仕事は、切らずに時間を通すことである。**
  ⚠️ **survivor はトレイと赤い安全光である**（`PLAN.md` §0-b）——
  **この2つが変わらないから、影の濃さが「経過」として読める。**
  ⛔ **ゆえに、この1枚はトレイと安全光を、before と同じ位置・同じ明るさで持つ。**
- ⚠️ **この1枚の影は、台帳の鍵では固定できない**（`shots/migenzo-ch02-seg01.yaml` の申し送り）——
  **影は `絹.identity` ではない。それでも影は、彼女の体の形をしている。**
  ⛔ **肯定の側が、その形を書いている**（standing, the same place, the same height, the same way）。
- `place` / `time` … `暗室` / 時刻を持たない
- `attached`（見込み）… `暗室.base`・`暗室.geography`。⛔ **人物の鍵を引かない。**
  ⚠️ **`attached` の確定は ③ である。**
