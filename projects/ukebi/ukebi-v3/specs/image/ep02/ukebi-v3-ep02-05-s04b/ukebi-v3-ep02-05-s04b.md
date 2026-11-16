# 画像仕様 — 第2話「送る」 s04b「内側で「サチ」という名が一度鳴る」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `art-board` —— 4つの穴（`LOCATION`／`HOUR`／`LIGHT_SOURCE`／`DIRECTION`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `LOCATION`: the boundary crossing at night — the fire low over the rails, no figure, no sky
- `HOUR`: an hour without a clock — no time of day, no sky, no sun, no moon, no stars
- `LIGHT_SOURCE`: the guest fire's interior, earth-coloured
- `DIRECTION`: from the far end, low
- `SUBJECT`: the fire's interior and the momentary images
- `ACTION`: the name sounding once: walking feet, a dry throat, an unreached place
- `LIGHT`: the earth-coloured interior, and nothing else
- `ACCENT`: the three momentary images

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `客の火.appearance` | — | 画像なし——ゲストの火。第2話は土の色（青白い火ではない）。block |
| `踏切.base` | `reference/踏切/青い鬼火の無人踏切.png` | 補正版の板（砂利と土・白黒の腕木・灯なし） |

⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**

## 生成物の置き場

`specs/image/ep02/ukebi-v3-ep02-05-s04b/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

An art board of the boundary crossing at night — the fire low over the rails, no figure, no sky in 16:9, empty of characters. One lighting state — an hour without a clock — no time of day, no sky, no sun, no moon, no stars, the guest fire's interior, earth-coloured from from the far end, low — establishing the palette, the light direction, the surface texture and the level of detail that every later shot of this place must match. Compositional space left open where the figure will stand. A background standard: one location, one state, no figures. The images are inside the fire and last one instant; no body is shown; no room. The plate is a painted anime background, with every surface finished to the same level as the painted background, with texture and soft modelling, never a flat cel diagram, never a photograph, never a 3D render. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line on the iron, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. The memory is inside the fire: the road is hot and pale, and the crossing appears only as a wet edge at the border of the frame, never as a second room and never through a window; no pavement, no asphalt, no concrete. The light is the guest fire's, small and low at the frame's edge; the rest falls into black, and the pool of light has a hard edge. No gradient across any surface.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no figure, no person, no hands, no flame in the frame, no visible light source, no point of light
