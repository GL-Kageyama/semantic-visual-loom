# 画像仕様 — 第4話「呑む」 s03「火の内側に、片腕と名の前の息が現れる」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `SCENE`: the fire opening, one arm of the wrapped child and the breath before the name
- `CHARACTERS`: [名なしの子: a small bundle wrapped in wet grey cloth, no larger than two hands, blue-white, no skin tone; no joints; the face made by folds, the eyes and mouth closed]; only one small arm leaves the wet cloth in the frame
- `SUBJECT`: the fire's interior and the one arm
- `ACTION`: the fire opening; the arm showing; the breath
- `LOCATION`: inside the fire at the boundary crossing
- `LIGHT`: the blue-white fire's interior
- `DIRECTION`: from within the flame
- `ACCENT`: the one arm and the breath

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `名なしの子.identity` | `~/Desktop/受け火映像アセット/名なしの子.png` | 設定画（濡れた布の塊。青白。関節を描かない） |
| `客の火.appearance` | — | 画像なし——ゲストの火。第4話は青白・いちばん小さい。block |
| `踏切.base` | `reference/踏切/踏切_土とレール.png` | 新しい色の板（砂利と土・白黒の腕木・灯なし・錆と濡れた土） |

⚠️ **デスクトップの畫像はこの端末の外にある**——clone しただけでは讀めない。`reference/` の畫像は clone で讀める。
⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep04/ukebi-v3-ep04-03-s03/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for the fire opening, one arm of the wrapped child and the breath before the name — the master staging of one scene from the story, in 16:9. [名なしの子: a small bundle wrapped in wet grey cloth, no larger than two hands, blue-white, no skin tone; no joints; the face made by folds, the eyes and mouth closed]; only one small arm leaves the wet cloth in the frame. The fire opening; the arm showing; the breath, inside the fire at the boundary crossing, under the blue-white fire's interior. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the fire's interior and the one arm, the fire opening; the arm showing; the breath, inside the fire at the boundary crossing, lit by the blue-white fire's interior, with the one arm and the breath.  Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust red is on the iron — the rail heads, the fishplates, the worn edges of the arms and the counterweights — and in the damp earth at the ruts' edges; the rust is the one warm colour outside the fire, never orange, never yellow. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. Where the crossing is in the frame, its two barrier arms are raised at sixty degrees with white and black bands of even width, left plain, with no sign, no signal, no lamp, no fence and no guardrail; the ground is gravel and earth with two wheel ruts, no pavement, no asphalt, no concrete and no painted line. The light is small in the frame and the darkness around it is large; the pool of light has a hard edge and reaches only the near ground and the water, and the rest falls into black. No gradient across any surface.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber glow, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no flame in the frame, no visible light source, no point of light
