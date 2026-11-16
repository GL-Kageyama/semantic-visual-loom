# 画像仕様 — 第3話「綴じる」 s01「踏切が、闇に沈んでいる」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。
⚠️ **人物0の画なので `scene-board` ではなく `art-board` である。** 人物の居ない板は
「物はセル」の規則の外にあり、**全面が描き込み**でよい（`one-lamp-cel` の Scope、踏切の板 版4）。

## 主題

- `REF_FORMAT`: `art-board` —— 4つの穴（`LOCATION`／`HOUR`／`LIGHT_SOURCE`／`DIRECTION`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `LOCATION`: the boundary crossing at night — two rails, black sleepers, gravel and earth with two wheel ruts, no pavement, no sky
- `HOUR`: an hour without a clock — no time of day, no sky, no sun, no moon, no stars
- `LIGHT_SOURCE`: the soul-fire, just outside the upper left edge of the frame, low; the source itself is never shown
- `DIRECTION`: from the upper left, low, along the rails
- `SUBJECT`: the rails, the wet gravel and the standing water
- `ACTION`: lying still while the light from outside the frame finds the wet edges
- `LIGHT`: one small pale blue-white pool from the off-frame soul-fire, from the upper left, and nothing else
- `ACCENT`: the wet gravel and the standing water doubling that one light once

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `踏切.base` | `reference/踏切/青い鬼火の無人踏切.png` | 補正版の板（砂利と土・白黒の腕木・灯なし） |
| `魂火.appearance` | — | 画像なし——`_shared/fire.md` の block（掌・梅の大きさ・青白い芯） |

⚠️ **`魂火.appearance` は画像を持たない**（`_shared/fire.md` の block）。**踏切の板は補正版を添える**（`reference/踏切/青い鬼火の無人踏切.png`）。**画像が無いことを、欄を消して隠さない。**

## 生成物の置き場

`specs/image/ep03/ukebi-v3-ep03-01-s01/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

An art board of the boundary crossing at night in 16:9, empty of characters. One lighting state — an hour that has no clock, and one soul-fire just outside the frame — establishing the palette, the light direction, the surface texture and the level of detail that every later shot of this place must match. Compositional space left open where the figure will stand. A background standard: one location, one state, no figures. The boundary crossing: two rails run in from the lower right and leave the frame at the upper left, off centre, so the view is not mirrored; the far end of the rails disappears into black before any horizon. The sleepers are black; the rust on the rail heads is the only red outside the fire; the road is gravel and earth with two wheel ruts worn through it, and there is no pavement, no asphalt, no concrete, no painted line. The rails are joined by fishplates with four bolts at each joint, the bolt heads rounded and worn; the sides of the rails are rusted, the running surface polished to a dull silver. The crossing boards between the rails are laid crosswise, their edges worn and dark with dried mud, the gaps between them black. Two barrier arms stand raised at sixty degrees and stay raised, painted in white and black bands of even width and left plain; the paint is worn at the corners and the counterweights hang below the pivots; the near post stands at the left edge and the far post is smaller at the right, so the two arms are never the same size; there is no sign, no signal, no lamp, no fence, no guardrail. A little grass grows between the sleepers, dry and thin and bent one way. The ground is wet although no rain falls: standing water sits in the ruts and between the stones, its edge black with mud, and the wet gravel holds the light. The only light is the soul-fire, and the source is not in the frame: it sits just outside the upper left edge, low, and its light enters as one small pale blue-white pool that finds the wet gravel and the standing water and stops there. The source itself is never shown — no flame, no wick, no lamp, no point of light, no glow in the sky. There is no sky: the top of the frame is unbroken black, with no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. The light is a shape, not a wash: the pool has a hard edge, every stone and sleeper casts one long shadow, and the wet surfaces double the one light once; the reflection in the standing water is the only place the pale blue-white repeats. No bloom, no lens flare, no glow ring, no god rays, no second light source, no ambient fill, no bounce light; whatever the light does not reach falls into unbroken black. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper: three to five values, the pale blue-white only at the light, the rust only on the rail heads and the worn iron, everything else one deep indigo-black family. No warm amber, no orange, no yellow, no magenta, no gold; no bright green, no bright yellow, no metallic sheen. The plate is a painted anime background, with every surface finished to the same level as the painted background: the gravel is painted stone by stone with wet edges, the sleepers are cracked and dark, the rail heads are polished, the water holds a still reflection, the grass is dry and thin, and the air is the only soft thing — a thin mist and fine ash suspended at every depth, catching the light, never glowing. Not a photograph, not a 3D render, not a flat cel diagram, not a gradient across any surface; no airbrush, no painterly brush strokes, no photographic texture. The camera is low, at rail height, on the road side, looking across and along the rails; the light is small in the frame and the darkness around it is large; the shadows are long. The space between the rails and to the left is left open where the figure will stand. Nobody has crossed: the road is empty, the arms stay up, and no footprint breaks the mud.

no figure, no person, no hands, no crowd, no flame in the frame, no visible light source, no point of light, no glow in the sky, no stars, no moon, no sun, no sky, no horizon, no clouds, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain
