# 画像仕様 — 第7話「値付ける」 s06「机の上が照らされ、部屋が開く」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `art-board` —— 4つの穴（`LOCATION`／`HOUR`／`LIGHT_SOURCE`／`DIRECTION`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `LOCATION`: inside the fire — a low desk in a dark room, the crossing at the wet edge, no sky
- `HOUR`: an hour without a clock — no time of day, no sky, no sun, no moon, no stars
- `LIGHT_SOURCE`: the soul fire on the desk, blue-white with a rust rim
- `DIRECTION`: from the desk's lower left
- `SUBJECT`: the desk and the room
- `ACTION`: the desk lighting; the room opening
- `LIGHT`: the soul fire on the desk, and nothing else
- `ACCENT`: the desk's surface and the floor

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `魂火.appearance` | — | 画像なし——掌の魂火。第7話は米粒ほど、青白・縁が赤い。block |

⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**

## 生成物の置き場

`specs/image/ep07/ukebi-v3-ep07-06-s06/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

An art board of inside the fire — a low desk in a dark room, the crossing at the wet edge, no sky in 16:9, empty of characters. One lighting state — an hour without a clock — no time of day, no sky, no sun, no moon, no stars, the soul fire on the desk, blue-white with a rust rim from the desk's lower left — establishing the palette, the light direction, the surface texture and the level of detail that every later shot of this place must match. Compositional space left open where the figure will stand. A background standard: one location, one state, no figures. The light is the soul fire on the desk; it does not flicker like a lamp; it reaches the desk and the floor; the crossing edge stays dark; no larger than a grain of rice. The plate is a painted anime background, with every surface finished to the same level as the painted background, with texture and soft modelling, never a flat cel diagram, never a photograph, never a 3D render. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line on the iron, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. The memory is inside the fire: a low desk in a dark room, the crossing at the wet edge of the frame, never a second room and never through a window; no pavement, no asphalt, no concrete. The light is the soul fire on the desk, blue-white with a rust rim; it does not flicker like a lamp; it reaches the desk and the floor, and the crossing edge stays dark; the rest falls into black, and the pool of light has a hard edge. No gradient across any surface. The fire is small, a pale blue-white body palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim; one closed contour, no tongue, no smoke, no steam, no sparks, no embers, no second flame.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber glow, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no figure, no person, no hands
