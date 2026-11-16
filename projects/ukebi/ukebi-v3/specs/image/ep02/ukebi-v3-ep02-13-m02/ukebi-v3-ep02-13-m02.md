# 画像仕様 — 第2話「送る」 m02「壺を傾け、一滴も出ない」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `SCENE`: a woman tilting a narrow-mouthed pot, no drop falling
- `CHARACTERS`: [サチ: a woman thin from the road, dark hair tied back, a worn travelled robe, cloth footwear, a narrow-mouthed unglazed pot in one hand, the wrist tied with a cord] is the only figure, her hand and the pot
- `SUBJECT`: the pot
- `ACTION`: tilting the pot; a dry sound once; no drop
- `LOCATION`: inside the fire — the hot road
- `LIGHT`: the earth-coloured interior
- `DIRECTION`: from the fire's edge
- `ACCENT`: the dry mouth of the pot

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `サチ.identity` | `~/Desktop/受け火映像アセット/サチ.png` | 設定画。⚠️ 履き物は設定画では草履形——台帳は布。再焼きまで、プロンプトで布と指定する |
| `壺.appearance` | — | 画像なし——窄口・無地・空。土色の素焼き、片手に収まる、手首に紐。水は一滴も無い |
| `客の火.appearance` | — | 画像なし——ゲストの火。第2話は土の色（青白い火ではない）。block |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep02/ukebi-v3-ep02-13-m02/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for a woman tilting a narrow-mouthed pot, no drop falling — the master staging of one scene from the story, in 16:9. [サチ: a woman thin from the road, dark hair tied back, a worn travelled robe, cloth footwear, a narrow-mouthed unglazed pot in one hand, the wrist tied with a cord] is the only figure, her hand and the pot. Tilting the pot; a dry sound once; no drop, at inside the fire — the hot road, under the earth-coloured interior. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the pot, tilting the pot; a dry sound once; no drop, in inside the fire — the hot road, lit by the earth-coloured interior, with the dry mouth of the pot.  Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line on the iron, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. The memory is inside the fire: the road is hot and pale, and the crossing appears only as a wet edge at the border of the frame, never as a second room and never through a window; no pavement, no asphalt, no concrete. The light is the guest fire's, small and low at the frame's edge; the rest falls into black, and the pool of light has a hard edge. No gradient across any surface.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no sandals, no straw sandals, no flame in the frame, no visible light source, no point of light
