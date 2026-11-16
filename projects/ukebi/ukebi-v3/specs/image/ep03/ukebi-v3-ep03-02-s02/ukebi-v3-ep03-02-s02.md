# 画像仕様 — 第3話「綴じる」 s02「細い火が、低く漂って来る」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）
- `SCENE`: a thin fire drifting low over the rails, the shape of a writer's callus showing at the bottom of the flame
- `CHARACTERS`: No figure is in the frame
- `SUBJECT`: the thin guest fire and the pen callus at its base
- `ACTION`: drifting low over the rails and coming to a stop above the gravel
- `LOCATION`: the same level crossing at night — rails and gravel, no hour and no sky
- `LIGHT`: one small pale fire at the frame's edge, low and from the left; the drifting guest flame is a shape and casts no light on the place
- `DIRECTION`: from the left, low
- `ACCENT`: the hardened callus at the base of the flame as the one bright detail

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `踏切.base` | — | 画像なし——補正前の板は使わない。`base` は意図 |

⚠️ **`踏切.base` と `魂火.appearance` は画像を持たない。** 踏切の板は台帳と三箇所食い違うので使わない（舗装・腕木・灯）。魂火は block である。**画像が無いことを、欄を消して隠さない。**

## 生成物の置き場

`specs/image/ep03/ukebi-v3-ep03-02-s02/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for a thin fire drifting low over the rails, the shape of a writer's callus showing at the bottom of the flame — the master staging of one scene from the story, in 16:9. No figure is in the frame. Drifting low over the rails and coming to a stop above the gravel, at the same level crossing at night — rails and gravel, no hour and no sky, under one small pale fire at the frame's edge, low and from the left; the drifting guest flame is a shape and casts no light on the place. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the thin guest fire and the pen callus at its base, drifting low over the rails and coming to a stop above the gravel, in the same level crossing at night — rails and gravel, no hour and no sky, lit by one small pale fire at the frame's edge, low and from the left; the drifting guest flame is a shape and casts no light on the place, with the hardened callus at the base of the flame as the one bright detail. Solid things are cel-painted: flat colour planes, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long; wet gravel and standing water double the one light once. The flame is small in the frame and the darkness around it is large. The camera stays low and still; only the flame travels, left to right, and the air carries fine ash.

no bloom, no lens flare, no glow, no god rays, no secondary light source, no sun, no moon, no stars, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no person, no figure, no hands
