# 画像仕様 — 第7話「値付ける」 s07「彼の目が動き、記憶が切れて踏切が入る」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `SCENE`: his eyes moving; the memory cutting; the crossing entering
- `CHARACTERS`: [送り火: a man of medium height, short dark-indigo hair with the ears uncovered, a knee-length dark-indigo coat with the collar down, hands large for the body, narrow eyes, the mouth closed, no expression], with only his eyelids and brow in the frame
- `SUBJECT`: his eyes and the cut
- `ACTION`: the eyes moving; the memory cutting
- `LOCATION`: the boundary crossing at night — the memory's edge, no sky
- `LIGHT`: one small pale soul fire, no larger than a grain of rice, and nothing else
- `DIRECTION`: from below
- `ACCENT`: the eyelid and the rail beyond

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `送り火.identity` | `~/Desktop/受け火映像アセット/送り火.png` | 設定画（顔・体格・コート・手） |
| `送り火.negatives` | — | Negative の一覧（画像ではない） |
| `魂火.appearance` | — | 画像なし——掌の魂火。第7話は米粒ほど、青白・縁が赤い。block |
| `踏切.base` | `reference/踏切/青い鬼火の無人踏切.png` | 補正版の板（砂利と土・白黒の腕木・灯なし） |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep07/ukebi-v3-ep07-13-s07/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for his eyes moving; the memory cutting; the crossing entering — the master staging of one scene from the story, in 16:9. [送り火: a man of medium height, short dark-indigo hair with the ears uncovered, a knee-length dark-indigo coat with the collar down, hands large for the body, narrow eyes, the mouth closed, no expression], with only his eyelids and brow in the frame. The eyes moving; the memory cutting, at the boundary crossing at night — the memory's edge, no sky, under one small pale soul fire, no larger than a grain of rice, and nothing else. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is his eyes and the cut, the eyes moving; the memory cutting, in the boundary crossing at night — the memory's edge, no sky, lit by one small pale soul fire, no larger than a grain of rice, and nothing else, with the eyelid and the rail beyond.  Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line on the iron, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. The memory is inside the fire: a low desk in a dark room, the crossing at the wet edge of the frame, never a second room and never through a window; no pavement, no asphalt, no concrete. The light is the soul fire on the desk, blue-white with a rust rim; it does not flicker like a lamp; it reaches the desk and the floor, and the crossing edge stays dark; the rest falls into black, and the pool of light has a hard edge. No gradient across any surface. The fire is small, a pale blue-white body palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim; one closed contour, no tongue, no smoke, no steam, no sparks, no embers, no second flame.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no full face
