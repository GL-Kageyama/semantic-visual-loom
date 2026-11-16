# 画像仕様 — 第1話「迎え火」 s02「水たまりが、視聴者の足元で止まる」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `SCENE`: the viewer's feet at the edge of a puddle, the wet gravel, the puddle holding the black sky
- `CHARACTERS`: [あなた: the viewer — only the two feet, looking down; no body, no face, no hands] — the only figure, and only the two feet are in the frame
- `SUBJECT`: the puddle and the two feet
- `ACTION`: looking down; the puddle's reflection going black at the feet
- `LOCATION`: the boundary crossing at night — wet gravel, a puddle, no pavement, no sky
- `LIGHT`: one distant pale cold white light from the far end, low, and nothing else
- `DIRECTION`: from the far end of the rails, low
- `ACCENT`: the puddle reflecting the black sky and the distant light at its far edge

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `あなた` | — | 画像なし——POV only。足だけ。全身も顔も手も出さない |
| `踏切.base` | `reference/踏切/青い鬼火の無人踏切.png` | 補正版の板（砂利と土・白黒の腕木・灯なし） |

⚠️ **POV の足だけ。** 全身・顔・手を出さない。`あなた` は参照画像を持たない。

## 生成物の置き場

`specs/image/ep01/ukebi-v3-ep01-02-s02/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for the viewer's feet at the edge of a puddle, the wet gravel, the puddle holding the black sky — the master staging of one scene from the story, in 16:9. [あなた: the viewer — only the two feet, looking down; no body, no face, no hands] — the only figure, and only the two feet are in the frame. Looking down; the puddle's reflection going black at the feet, at the boundary crossing at night — wet gravel, a puddle, no pavement, no sky, under one distant pale cold white light from the far end, low, and nothing else. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the puddle and the two feet, looking down; the puddle's reflection going black at the feet, in the boundary crossing at night — wet gravel, a puddle, no pavement, no sky, lit by one distant pale cold white light from the far end, low, and nothing else, with the puddle reflecting the black sky and the distant light at its far edge.  Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line along the rail heads and the fishplates, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. Where the crossing is in the frame, its two barrier arms are raised at sixty degrees with white and black bands of even width, left plain, with no sign, no signal, no lamp, no fence and no guardrail; the ground is gravel and earth with two wheel ruts, no pavement, no asphalt, no concrete and no painted line. The light is small in the frame and the darkness around it is large; the pool of light has a hard edge and reaches only the near ground and the water, and the rest falls into black. No gradient across any surface.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no full body, no face, no hands, no second person, no flame in the frame, no visible light source, no point of light
