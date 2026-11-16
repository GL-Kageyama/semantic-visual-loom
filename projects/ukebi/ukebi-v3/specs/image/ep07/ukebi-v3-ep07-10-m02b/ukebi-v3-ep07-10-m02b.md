# 画像仕様 — 第7話「値付ける」 m02b「爪の先が数える」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `SCENE`: a nail counting silently
- `CHARACTERS`: [トワ: a tall thin woman, black hair, a grey robe, the jaw and throat visible; her eyes lowered, never opening]; only her hand and jaw in the frame
- `SUBJECT`: the nail and the jaw
- `ACTION`: the nail counting; no sound
- `LOCATION`: inside the fire — the low desk
- `LIGHT`: the soul fire on the desk
- `DIRECTION`: from the desk's lower left
- `ACCENT`: the nail at the jaw

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `トワ.identity` | `~/Desktop/受け火映像アセット/トワ.png` | 設定画（細い・背が高い・黒髪・灰の衣。伏せた目） |
| `魂火.appearance` | — | 画像なし——掌の魂火。第7話は米粒ほど、青白・縁が赤い。block |

⚠️ **デスクトップの畫像はこの端末の外にある**——clone しただけでは讀めない。`reference/` の畫像は clone で讀める。
⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep07/ukebi-v3-ep07-10-m02b/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for a nail counting silently — the master staging of one scene from the story, in 16:9. [トワ: a tall thin woman, black hair, a grey robe, the jaw and throat visible; her eyes lowered, never opening]; only her hand and jaw in the frame. The nail counting; no sound, inside the fire — the low desk, under the soul fire on the desk. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the nail and the jaw, the nail counting; no sound, inside the fire — the low desk, lit by the soul fire on the desk, with the nail at the jaw.  Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line on the iron, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. The memory is inside the fire: a low desk in a dark room, the crossing at the wet edge of the frame, never a second room and never through a window; no pavement, no asphalt, no concrete. The light is the soul fire on the desk, blue-white with a rust rim; it does not flicker like a lamp; it reaches the desk and the floor, and the crossing edge stays dark; the rest falls into black, and the pool of light has a hard edge. No gradient across any surface. The fire is small, a pale blue-white body palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim; one closed contour, no tongue, no smoke, no steam, no sparks, no embers, no second flame.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no full face
