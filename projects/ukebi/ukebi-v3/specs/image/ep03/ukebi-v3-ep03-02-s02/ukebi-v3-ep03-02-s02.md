# 画像仕様 — 第3話「綴じる」 s02「細い火が、低く漂って来る」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。
⚠️ **人物0の画なので `scene-board` ではなく `art-board` である。** 人物の居ない板は
「物はセル」の規則の外にあり、**全面が描き込み**でよい（`one-lamp-cel` の Scope、踏切の板 版4）。

## 主題

- `REF_FORMAT`: `art-board` —— 4つの穴（`LOCATION`／`HOUR`／`LIGHT_SOURCE`／`DIRECTION`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `LOCATION`: the boundary crossing at night — rails, gravel and earth, no pavement, no sky
- `HOUR`: an hour without a clock — no time of day, no sky, no sun, no moon, no stars
- `LIGHT_SOURCE`: the thin guest fire itself, low over the rails at the frame's edge; it lights only its own interior and casts no light on the place
- `DIRECTION`: from the left, low
- `SUBJECT`: the thin guest fire and the pen callus at its base
- `ACTION`: drifting low over the rails and coming to a stop above the gravel
- `LIGHT`: one small pale fire at the frame's edge, low and from the left; the guest flame is a shape and casts no light on the place, and nothing else
- `ACCENT`: the hardened callus at the base of the flame as the one bright detail

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `踏切.base` | `reference/踏切/踏切_土とレール.png` | 新しい色の板（砂利と土・白黒の腕木・灯なし・錆と濡れた土） |

⚠️ **踏切の板は補正版を添える**（`reference/踏切/踏切_土とレール.png`）。
**画像が無いことを、欄を消して隠さない。**

## 生成物の置き場

`specs/image/ep03/ukebi-v3-ep03-02-s02/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

An art board of the boundary crossing at night in 16:9, empty of characters. One lighting state — an hour that has no clock, and one thin guest fire low over the rails — establishing the palette, the light direction, the surface texture and the level of detail that every later shot of this place must match. Compositional space left open where the figure will stand. A background standard: one location, one state, no figures. The boundary crossing: two rails run in from the lower right and leave the frame at the upper left, off centre, so the view is not mirrored; the far end of the rails disappears into black before any horizon. The sleepers are black; the rust on the rail heads is the only red outside the fire; the ground is gravel and earth with two wheel ruts worn through it, and there is no pavement, no asphalt, no concrete, no painted line. Two barrier arms stand raised at sixty degrees and stay raised, painted in white and black bands of even width and left plain; there is no sign, no signal, no lamp, no fence, no guardrail. A little grass grows between the sleepers, dry and thin and bent one way. The only light is the thin guest fire itself, low at the frame's edge and drifting over the rails: a small pale blue-white body, palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim, one closed contour, with the shape of a writer's callus at its base; no tongue, no smoke, no steam, no sparks, no embers, no second flame. The guest flame is a shape and casts no light on the place: the rails and the gravel around it stay black, and the flame is the only bright thing in the frame. The flame is no wider than a hand and no taller than a hand; its light stays inside its own contour: the gravel around it is black, with no blue pool and no reflection of the flame on the ground. There is no sky: the top of the frame is unbroken black, with no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. No bloom, no lens flare, no glow ring, no god rays, no second light source, no ambient fill, no bounce light. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper: three to five values, the pale blue-white only at the flame, the rust only on the rail heads and the worn iron, everything else one deep indigo-black family. No warm amber, no orange, no yellow, no magenta, no gold; no bright green, no bright yellow, no metallic sheen. The plate is a painted anime background, with every surface finished to the same level as the painted background: the gravel is painted stone by stone, the sleepers are cracked and dark, the rail heads are polished, the grass is dry and thin, and the air is the only soft thing — a thin mist and fine ash suspended at every depth, catching the light, never glowing. Not a photograph, not a 3D render, not a flat cel diagram, not a gradient across any surface; no airbrush, no painterly brush strokes, no photographic texture. The camera stays low and still; only the flame travels, left to right, and the air carries fine ash.

no figure, no person, no hands, no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber glow, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no tongue of flame, no licking flame, no large flame, no pool of light, no glow on the ground, no blue light on the gravel, no reflection of the flame
