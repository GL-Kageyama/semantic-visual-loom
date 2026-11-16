# 画像仕様 — 第3話「綴じる」 s12「「読んで」——指が強ばる」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）
- `SCENE`: the finger on the fold stiffening as a voice sounds
- `CHARACTERS`: [送り火: a man of medium height, short dark-indigo hair with the ears uncovered, a knee-length dark-indigo coat with the collar down, hands large for the body, narrow eyes, the mouth closed, no expression], with only his right finger in the frame
- `SUBJECT`: the finger
- `ACTION`: stiffening without leaving the fold
- `LOCATION`: the level crossing at night — the white page under the hand, no hour and no sky
- `LIGHT`: one small soul fire from below, and nothing else
- `DIRECTION`: from below
- `ACCENT`: the whitened knuckle where the finger presses

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `送り火.identity` | `~/Desktop/受け火映像アセット/送り火.png` | 設定画（顔・体格・コート・手） |
| `送り火.negatives` | — | Negative の一覧（画像ではない） |
| `踏切.base` | `reference/踏切/青い鬼火の無人踏切.png` | 補正版の板（砂利と土・白黒の腕木・灯なし） |
| `台帳.appearance` | `~/Desktop/受け火映像アセット/台帳.png` | 物の設定画（閉じた台帳・頁・焦げ跡） |
| `魂火.appearance` | — | 画像なし——`_shared/fire.md` の block（掌・梅の大きさ・青白い芯） |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **`魂火.appearance` は画像を持たない**（`_shared/fire.md` の block）。**踏切の板は補正版を添える**（`reference/踏切/青い鬼火の無人踏切.png`）。**画像が無いことを、欄を消して隠さない。**
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep03/ukebi-v3-ep03-23-s12/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for the finger on the fold stiffening as a voice sounds — the master staging of one scene from the story, in 16:9. [送り火: a man of medium height, short dark-indigo hair with the ears uncovered, a knee-length dark-indigo coat with the collar down, hands large for the body, narrow eyes, the mouth closed, no expression], with only his right finger in the frame. Stiffening without leaving the fold, at the level crossing at night — the white page under the hand, no hour and no sky, under one small soul fire from below, and nothing else. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the finger, stiffening without leaving the fold, in the level crossing at night — the white page under the hand, no hour and no sky, lit by one small soul fire from below, and nothing else, with the whitened knuckle where the finger presses. Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long; wet gravel and standing water double the one light once. The camera holds on the finger. The voice comes from off-frame; the finger answers by stiffening, the knuckle going pale. It does not lift from the fold. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line along the rail heads and the fishplates, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. Where the crossing is in the frame, its two barrier arms are raised at sixty degrees with white and black bands of even width, left plain, with no sign, no signal, no lamp, no fence and no guardrail; the ground is gravel and earth with two wheel ruts, no pavement, no asphalt, no concrete and no painted line. The light is small in the frame and the darkness around it is large; the pool of light has a hard edge and reaches only the near ground and the water, and the rest falls into black. No gradient across any surface. The fire is small, a pale blue-white body palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim; one closed contour, no tongue, no smoke, no steam, no sparks, no embers, no second flame.

no bloom, no lens flare, no glow, no god rays, no secondary light source, no sun, no moon, no stars, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second hand, no open mouth, no second person, no pavement, no asphalt, no concrete, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon
