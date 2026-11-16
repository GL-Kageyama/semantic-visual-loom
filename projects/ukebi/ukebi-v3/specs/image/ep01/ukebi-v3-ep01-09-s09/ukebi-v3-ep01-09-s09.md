# 画像仕様 — 第1話「迎え火」 s09「火の内側に、三つの値の層が開く」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `art-board` —— 4つの穴（`LOCATION`／`HOUR`／`LIGHT_SOURCE`／`DIRECTION`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `LOCATION`: the boundary crossing at night — the fire low over the rails, no figure, no sky
- `HOUR`: an hour without a clock — no time of day, no sky, no sun, no moon, no stars
- `LIGHT_SOURCE`: the guest fire itself, opening into three value layers
- `DIRECTION`: from the far end, low
- `SUBJECT`: the interior of the fire, three value layers
- `ACTION`: opening into a pale core, a warm middle and a dark bottom
- `LIGHT`: the fire's own interior, and nothing else
- `ACCENT`: the three layers: pale core, warm middle, dark bottom

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `踏切.base` | `reference/踏切/青い鬼火の無人踏切.png` | 補正版の板（砂利と土・白黒の腕木・灯なし） |
| `客の火.appearance` | — | 画像なし——第1話の客の火。block（青白い芯・温かい中間・暗い底） |

⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**

## 生成物の置き場

`specs/image/ep01/ukebi-v3-ep01-09-s09/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

An art board of the boundary crossing at night — the fire low over the rails, no figure, no sky in 16:9, empty of characters. One lighting state — an hour without a clock — no time of day, no sky, no sun, no moon, no stars, the guest fire itself, opening into three value layers from the far end, low — establishing the palette, the light direction, the surface texture and the level of detail that every later shot of this place must match. Compositional space left open where the figure will stand. A background standard: one location, one state, no figures. No figure; the three layers are light, not a room; no memory is shown inside the flame. The plate is a painted anime background, with every surface finished to the same level as the painted background, with texture and soft modelling, never a flat cel diagram, never a photograph, never a 3D render. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line along the rail heads and the fishplates, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. Where the crossing is in the frame, its two barrier arms are raised at sixty degrees with white and black bands of even width, left plain, with no sign, no signal, no lamp, no fence and no guardrail; the ground is gravel and earth with two wheel ruts, no pavement, no asphalt, no concrete and no painted line. The light is small in the frame and the darkness around it is large; the pool of light has a hard edge and reaches only the near ground and the water, and the rest falls into black. No gradient across any surface. The fire is small, a pale blue-white body palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim; one closed contour, no tongue, no smoke, no steam, no sparks, no embers, no second flame.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no figure, no person, no hands
