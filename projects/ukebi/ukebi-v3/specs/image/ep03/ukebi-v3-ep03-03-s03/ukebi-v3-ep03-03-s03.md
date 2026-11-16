# 画像仕様 — 第3話「綴じる」 s03「火の内側が、開く」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）
- `SCENE`: the small fire opening along its length, and inside it the ink-stained fingers, the sheaf of paper and the worn cuff of a sleeve
- `CHARACTERS`: [フミ: a thin man rounded forward at the back, short black hair still creased from sleep, a worn grey and burnt-brown jacket with the collar open, ink on the fingertips and along the nail edges, sunken eyes, no glasses], with only his right hand and the worn cuff of the jacket in the frame
- `SUBJECT`: the guest fire and the shallow interior it opens
- `ACTION`: opening from a closed flame into a shallow interior that shows the hand
- `LOCATION`: the level crossing at night — the fire low over the gravel, no hour and no sky
- `LIGHT`: one small guest fire at the centre of the frame, lighting only what is inside it, and nothing else
- `DIRECTION`: from within the flame at the centre
- `ACCENT`: the black ink in the ridges of the fingers and along the nail edges

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `フミ.identity` | `~/Desktop/受け火映像アセット/フミ.png` | 設定画（丸い背・指のインク・上着） |
| `フミ.negatives` | — | Negative の一覧（画像ではない） |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep03/ukebi-v3-ep03-03-s03/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for the small fire opening along its length, and inside it the ink-stained fingers, the sheaf of paper and the worn cuff of a sleeve — the master staging of one scene from the story, in 16:9. [フミ: a thin man rounded forward at the back, short black hair still creased from sleep, a worn grey and burnt-brown jacket with the collar open, ink on the fingertips and along the nail edges, sunken eyes, no glasses], with only his right hand and the worn cuff of the jacket in the frame. Opening from a closed flame into a shallow interior that shows the hand, at the level crossing at night — the fire low over the gravel, no hour and no sky, under one small guest fire at the centre of the frame, lighting only what is inside it, and nothing else. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the guest fire and the shallow interior it opens, opening from a closed flame into a shallow interior that shows the hand, in the level crossing at night — the fire low over the gravel, no hour and no sky, lit by one small guest fire at the centre of the frame, lighting only what is inside it, and nothing else, with the black ink in the ridges of the fingers and along the nail edges. Solid things are cel-painted: flat colour planes, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long; wet gravel and standing water double the one light once. The camera is close and level with the fire. The interior is a shallow plane, not a room; the paper and the sleeve are seen only as much as the opening shows. The hand is still.

no bloom, no lens flare, no glow, no god rays, no secondary light source, no sun, no moon, no stars, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second hand, no face, no body beyond the hand and the cuff
