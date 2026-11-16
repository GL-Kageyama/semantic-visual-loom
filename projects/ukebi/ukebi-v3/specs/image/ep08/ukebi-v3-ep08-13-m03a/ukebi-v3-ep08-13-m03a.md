# 画像仕様 — 第8話「悼む」 m03a「二枚が一つの包みになり、もう一度折られる」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `SCENE`: the two sheets folded together into one packet
- `CHARACTERS`: [ナギ: a young thin soldier, narrow shoulders, a burnt-brown and grey military coat, a cap; no insignia, no flag; the posture of a soldier] is the only figure; only his two hands and the paper
- `SUBJECT`: the two hands and the packet
- `ACTION`: folding the two sheets together
- `LOCATION`: inside the fire — the night field
- `LIGHT`: the distant soul fire at the edge
- `DIRECTION`: from the frame's edge, low
- `ACCENT`: the packet's folded edge

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `ナギ.identity` | `~/Desktop/受け火映像アセット/ナギ.png` | 設定画（4面。生成に渡すと四人になる——1面に切り抜くか立ち絵を燒くまで、記憶の畫は燒かない） |
| `手紙.appearance` | — | 画像なし——四つに折った白い紙。字は無い。厚い軍の紙。裂けた縁は一度だけ |
| `魂火.appearance` | — | 画像なし——掌の魂火。第8話は芥子粒ほど、青白・縁が赤い。block |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep08/ukebi-v3-ep08-13-m03a/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for the two sheets folded together into one packet — the master staging of one scene from the story, in 16:9. [ナギ: a young thin soldier, narrow shoulders, a burnt-brown and grey military coat, a cap; no insignia, no flag; the posture of a soldier] is the only figure; only his two hands and the paper. Folding the two sheets together, at inside the fire — the night field, under the distant soul fire at the edge. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the two hands and the packet, folding the two sheets together, in inside the fire — the night field, lit by the distant soul fire at the edge, with the packet's folded edge.  Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line on the iron, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. The memory is inside the fire: a night field, a soldier's coat laid on the grass, the crossing at the wet edge of the frame, never a second room and never through a window; no rain; no pavement, no asphalt. The light is the soul fire at the frame's edge, blue-white with a rust rim; it lights the coat and the ground; the crossing edge stays dark; the rest falls into black. No gradient across any surface. The fire is small, a pale blue-white body palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim; one closed contour, no tongue, no smoke, no steam, no sparks, no embers, no second flame.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no full face
