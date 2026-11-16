# 画像仕様 — 第3話「綴じる」 m01b「火の光が、窓枠で止まる」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。
⚠️ **人物0の画なので `scene-board` ではなく `art-board` である。** 人物の居ない板は
「物はセル」の規則の外にあり、**全面が描き込み**でよい（`one-lamp-cel` の Scope、踏切の板 版4）。

## 主題

- `REF_FORMAT`: `art-board` —— 4つの穴（`LOCATION`／`HOUR`／`LIGHT_SOURCE`／`DIRECTION`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `LOCATION`: inside the guest fire — the desk room, a window at the far wall
- `HOUR`: an hour without a clock — the room's darkness, no sky, no sun, no moon, no stars
- `LIGHT_SOURCE`: the guest fire from behind the camera, its light stopping at the window frame
- `DIRECTION`: from behind the camera
- `SUBJECT`: the window frame and the black beyond it
- `ACTION`: the light reaching the window frame and stopping there
- `LIGHT`: one small guest fire from behind the camera, its light stopping at the window frame, and nothing else
- `ACCENT`: the lit edge of the window frame against the black

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `記憶.appearance` | `~/AI創作工房/distill-essence-engine/examples/works/novels/ukebi-anime/ukebi-anime-prop-sheet-記憶/霧深き線路に灯る記憶の灯火.png` | 物の設定画（机・窓・頁）。Desktop には無い——distill の採用済み |
| `踏切.base` | — | 画像なし——記憶の縁。板は添えない（窓・別室を呼ぶ） |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **`踏切.base` は画像を持たない。** 踏切の板は台帳と三箇所食い違うので使わない（舗装・腕木・灯）。

## 生成物の置き場

`specs/image/ep03/ukebi-v3-ep03-10-m01b/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

An art board of the desk room inside the guest fire in 16:9, empty of characters, the camera turned to a window. One lighting state — an hour that has no clock, and one small guest fire from behind the camera — establishing the palette, the light direction, the surface texture and the level of detail that every later shot of this place must match. Compositional space left open where the figure will stand. A background standard: one room, one state, no figures. The room is inside the flame and shallow: a window sits at the far wall, its panes dark and gridded, the frame plain and old; the desk is at the near edge, out of focus; the room beyond the window is black — no street, no yard, no second room, no horizon. The only light is the small guest fire behind the camera: one small pale blue-white body, palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim, one closed contour, no tongue, no smoke, no steam, no sparks, no embers, no second flame; it is behind the lens and is not in the frame. Its light reaches the window frame and stops there; the panes are black, and the pool of light has a hard edge. There is no sky beyond the glass: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. No bloom, no lens flare, no glow ring, no god rays, no second light source, no ambient fill, no bounce light. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper: three to five values, the pale blue-white only on the window frame, the rust only on the worn iron, everything else one deep indigo-black family. No warm amber, no orange, no yellow, no magenta, no gold; no bright green, no bright yellow, no metallic sheen. The plate is a painted anime background, with every surface finished to the same level as the painted background: the wood is painted grain by grain, the glass is painted as flat black, the air is the only soft thing — a thin mist and fine ash suspended at every depth, catching the light, never glowing. Not a photograph, not a 3D render, not a flat cel diagram, not a gradient across any surface; no airbrush, no painterly brush strokes, no photographic texture. The camera is close on the window; the light is small in the frame and the darkness around it is large.

no figure, no person, no hands, no crowd, no second room, no street beyond the glass, no yard, no horizon, no pavement, no asphalt, no concrete, no legible text, no stars, no moon, no sun, no sky, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no crowds, no rain
