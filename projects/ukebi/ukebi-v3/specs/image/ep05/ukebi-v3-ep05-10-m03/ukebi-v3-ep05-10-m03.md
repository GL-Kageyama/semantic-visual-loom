# 画像仕様 — 第5話「預かる」 m03「影が足音だけを残して過ぎ、足元が見える」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `SCENE`: shadows passing with only footsteps, the child's feet visible
- `CHARACTERS`: [コダマ: a small child, a girl, an oversized coat whose sleeves pass the hands, bare feet, both hands raised] is the only figure; the feet and the hem of the coat
- `SUBJECT`: the feet and the passing shadows
- `ACTION`: shadows passing; the feet still
- `LOCATION`: inside the fire — the old doorway
- `LIGHT`: a low light at the edge, and nothing else
- `DIRECTION`: from the left edge
- `ACCENT`: the bare feet and the shadows

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `コダマ.identity` | `~/Desktop/受け火映像アセット/コダマ.png` | 設定画 版2（女の子。大きすぎる上着・余った袖・裸足・上げた両手） |
| `客の火.appearance` | — | 画像なし——ゲストの火。第5話はコダマの火。小さい、手のひらを上に向けた形。block |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep05/ukebi-v3-ep05-10-m03/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for shadows passing with only footsteps, the child's feet visible — the master staging of one scene from the story, in 16:9. [コダマ: a small child, a girl, an oversized coat whose sleeves pass the hands, bare feet, both hands raised] is the only figure; the feet and the hem of the coat. Shadows passing; the feet still, at inside the fire — the old doorway, under a low light at the edge, and nothing else. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the feet and the passing shadows, shadows passing; the feet still, in inside the fire — the old doorway, lit by a low light at the edge, and nothing else, with the bare feet and the shadows.  Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line on the iron, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. The memory is inside the fire: an old door half-open in a dark doorway, the crossing at the wet edge of the frame, never a second room and never through a window; no pavement, no asphalt, no concrete. The light is the guest fire's, small and low at the frame's edge; the rest falls into black, and the pool of light has a hard edge. No gradient across any surface.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no flame in the frame, no visible light source, no point of light
