# 画像仕様 — 第10話「該当なし」 s24「瞳に彼の輪郭が小さく映り、瞳が動かない」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 5つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`LIGHT`／`ACCENT`）
- `SCENE`: his outline small in her pupil; the pupil still
- `CHARACTERS`: [花: a girl a head shorter than the man, thin, shoulders carried low; long near-black indigo hair unbound and heavy, covering the ears; a dark-indigo school jacket and a plain knee-length skirt, one piping line at the collar, no crest, no name tag; black shoes; brows and mouth still, only the eyes move] — only her eyes in the frame
- `SUBJECT`: her pupil and the small outline
- `ACTION`: the pupil still
- `LOCATION`: the boundary crossing at night — no sky
- `LIGHT`: one small soul fire off-frame, low, and nothing else
- `DIRECTION`: from below
- `ACCENT`: her pupil

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `花.identity` | `~/Desktop/受け火映像アセット/花.png` | 設定画（少女。現在は乾いている） |
| `魂火.appearance` | — | 画像なし——掌の魂火。第10話は炭ほど、青白・縁が赤い。block |
| `踏切.base` | `reference/踏切/青い鬼火の無人踏切.png` | 補正版の板（砂利と土・白黒の腕木・灯なし） |

⚠️ **デスクトップの畫像はこの端末の外にある**——clone しただけでは讀めない。`reference/` の畫像は clone で讀める。
⚠️ **`魂火.appearance` と `客の火.appearance` は画像を持たない**（block）。**画像が無いことを、欄を消して隠さない。**
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep10/ukebi-v3-ep10-26-s24/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for his outline small in her pupil; the pupil still — the master staging of one scene from the story, in 16:9. [花: a girl a head shorter than the man, thin, shoulders carried low; long near-black indigo hair unbound and heavy, covering the ears; a dark-indigo school jacket and a plain knee-length skirt, one piping line at the collar, no crest, no name tag; black shoes; brows and mouth still, only the eyes move] — only her eyes in the frame. The pupil still, at the boundary crossing at night — no sky, under one small soul fire off-frame, low, and nothing else. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is her pupil and the small outline, the pupil still, in the boundary crossing at night — no sky, lit by one small soul fire off-frame, low, and nothing else, with her pupil.  Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line along the rail heads and the fishplates, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. Where the crossing is in the frame, its two barrier arms are raised at sixty degrees with white and black bands of even width, left plain, with no sign, no signal, no lamp, no fence and no guardrail; the ground is gravel and earth with two wheel ruts, no pavement, no asphalt, no concrete and no painted line. The light is small in the frame and the darkness around it is large; the pool of light has a hard edge and reaches only the near ground and the water, and the rest falls into black. No gradient across any surface.

no crowd, no pavement, no asphalt, no concrete, no painted road line, no yellow-black barrier, no yellow stripe, no warning light, no sign, no signal, no lamp, no fence, no guardrail, no stars, no moon, no sun, no sky, no horizon, no clouds, no warm amber, no orange, no yellow, no magenta, no gold, no neon, no saturated red, no bloom, no lens flare, no glow, no god rays, no secondary light source, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no flame in the frame, no visible light source, no point of light
