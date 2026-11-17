# 画像仕様 — 第4話「呑む」 s01「カメラがレールの高さへ下り、水たまりが闇を返す」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `art-board` —— 4つの穴（`LOCATION`／`HOUR`／`LIGHT_SOURCE`／`DIRECTION`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `LOCATION`: the boundary crossing at night — rails, gravel, a puddle, no pavement, no sky
- `HOUR`: an hour without a clock — no time of day, no sky, no sun, no moon, no stars
- `LIGHT_SOURCE`: one small soul fire off-frame, low, cold; the source is not in the frame
- `DIRECTION`: from the left, off-frame
- `SUBJECT`: the dark crossing and the puddle
- `ACTION`: the camera descending to rail height; the puddle returning the dark
- `LIGHT`: one small pale soul fire off-frame, low, and nothing else
- `ACCENT`: the puddle's dark sheen

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `踏切.base` | `reference/踏切/踏切_土とレール.png` | 新しい色の板（砂利と土・白黒の腕木・灯なし・錆と濡れた土） |



## 生成物の置き場

`specs/image/ep04/ukebi-v3-ep04-01-s01/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

An art board of the boundary crossing at night — rails, gravel, a puddle, no pavement, no sky in 16:9, empty of characters. One lighting state — an hour without a clock — no time of day, no sky, no sun, no moon, no stars, one small soul fire off-frame, low, cold; the source is not in the frame from the left, off-frame — establishing the palette, the light direction, the surface texture and the level of detail that every later shot of this place must match. Compositional space left open where the figure will stand. A background standard: one location, one state, no figures. The frame is almost all dark. The plate is a painted anime background, with every surface finished to the same level as the painted background, with texture and soft modelling, never a flat cel diagram, never a photograph, never a 3D render. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust red is on the iron — the rail heads, the fishplates, the worn edges of the arms and the counterweights — and in the damp earth at the ruts' edges; the rust is the one warm colour outside the fire, never orange, never yellow. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. Where the crossing is in the frame, its two barrier arms are raised at sixty degrees with white and black bands of even width, left plain, with no sign, no signal, no lamp, no fence and no guardrail; the ground is gravel and earth with two wheel ruts, no pavement, no asphalt, no concrete and no painted line. The light is small in the frame and the darkness around it is large; the pool of light has a hard edge and reaches only the near ground and the water, and the rest falls into black. No gradient across any surface.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber glow, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no figure, no person, no hands, no flame in the frame, no visible light source, no point of light
