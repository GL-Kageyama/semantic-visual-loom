# 画像仕様 — 第8話「悼む」 s02「軍の外套の火が来る（徽章なし・帽子・若い）」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `art-board` —— 4つの穴（`LOCATION`／`HOUR`／`LIGHT_SOURCE`／`DIRECTION`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `LOCATION`: the boundary crossing at night — the coat-shaped guest fire coming, no figure, no sky
- `HOUR`: an hour without a clock — no time of day, no sky, no sun, no moon, no stars
- `LIGHT_SOURCE`: the guest fire, the shape of a soldier's coat
- `DIRECTION`: from the far end, low
- `SUBJECT`: the coat-shaped fire
- `ACTION`: coming low over the rails
- `LIGHT`: one coat-shaped pale fire, and nothing else
- `ACCENT`: the coat's outline

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `ナギ.states.火` | — | 画像なし——軍の外套の形の火。青白・縁だけ赤。輪郭だけで、体ではない |
| `踏切.base` | `reference/踏切/青い鬼火の無人踏切.png` | 補正版の板（砂利と土・白黒の腕木・灯なし） |
| `魂火.appearance` | — | 画像なし——掌の魂火。第8話は芥子粒ほど、青白・縁が赤い。block |

⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**

## 生成物の置き場

`specs/image/ep08/ukebi-v3-ep08-02-s02/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

An art board of the boundary crossing at night — the coat-shaped guest fire coming, no figure, no sky in 16:9, empty of characters. One lighting state — an hour without a clock — no time of day, no sky, no sun, no moon, no stars, the guest fire, the shape of a soldier's coat from from the far end, low — establishing the palette, the light direction, the surface texture and the level of detail that every later shot of this place must match. Compositional space left open where the figure will stand. A background standard: one location, one state, no figures. The fire is a coat outline, not a body; no insignia, no flag; it casts no light on the place. The plate is a painted anime background, with every surface finished to the same level as the painted background, with texture and soft modelling, never a flat cel diagram, never a photograph, never a 3D render. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line along the rail heads and the fishplates, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. Where the crossing is in the frame, its two barrier arms are raised at sixty degrees with white and black bands of even width, left plain, with no sign, no signal, no lamp, no fence and no guardrail; the ground is gravel and earth with two wheel ruts, no pavement, no asphalt, no concrete and no painted line. The light is small in the frame and the darkness around it is large; the pool of light has a hard edge and reaches only the near ground and the water, and the rest falls into black. No gradient across any surface. The fire is the shape of a soldier's coat — a small flame whose outline is a coat with no insignia, no flag and no lettering; it is blue-white with one rust-red rim, the same colour as the soul fire, but its shape is a coat and not a body. No face, no head, no hands; the outline only.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no figure, no person, no hands
