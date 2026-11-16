# 画像仕様 — 第9話「捨てる」 m03「長い落ち影が線路のほうへ伸びて行く」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `SCENE`: inside the fire — the rainy ballast and a long falling shadow, no sky
- `CHARACTERS`: none
- `SUBJECT`: the long shadow on the wet ballast
- `ACTION`: the shadow stretching toward the rails; no face, no legs
- `LOCATION`: inside the fire — the rainy crossing
- `LIGHT`: the soul fire at the frame's edge
- `DIRECTION`: from the frame's edge, low
- `ACCENT`: the long shadow on the wet ballast

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `魂火.appearance` | — | 画像なし——掌の魂火。第9話は炭ほど、青白・縁が赤い。block |
| `踏切.base` | `reference/踏切/青い鬼火の無人踏切.png` | 補正版の板（砂利と土・白黒の腕木・灯なし） |

⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**

## 生成物の置き場

`specs/image/ep09/ukebi-v3-ep09-11-m03/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for inside the fire — the rainy ballast and a long falling shadow, no sky — the master staging of one scene from the story, in 16:9. No figure is in the frame. The shadow stretching toward the rails; no face, no legs, at inside the fire — the rainy crossing, under the soul fire at the frame's edge. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the long shadow on the wet ballast, the shadow stretching toward the rails; no face, no legs, in inside the fire — the rainy crossing, lit by the soul fire at the frame's edge, with the long shadow on the wet ballast.  Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line on the iron, the only warm colour outside the fire. The memory is inside the fire: a rainy level crossing, the wet rails, the barrier's white and black bands, the crossing at the edge of the frame; no pavement, no asphalt, no concrete. Rain falls inside the memory; the crossing is wet; the present outside the memory is dry. The light is the soul fire at the frame's edge, blue-white with a rust rim; it lights the wet rails and the face; the rest falls into black. No sky: no stars, no moon, no sun, no horizon. No gradient across any surface. The fire is small, a pale blue-white body palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim; one closed contour, no tongue, no smoke, no steam, no sparks, no embers, no second flame.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no figure, no person, no hands
