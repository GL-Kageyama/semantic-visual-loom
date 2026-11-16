# 画像仕様 — 第3話「綴じる」 m02b「火が、頁の端を食う」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）
- `SCENE`: the fire taking the edge of the page from the corner
- `CHARACTERS`: [フミ: a thin man rounded forward at the back, short black hair still creased from sleep, a worn grey and burnt-brown jacket with the collar open, ink on the fingertips and along the nail edges, sunken eyes, no glasses] is the only figure, seated, his hand at the page
- `SUBJECT`: the flame and the page edge
- `ACTION`: eating along the edge, the paper darkening
- `LOCATION`: inside the guest fire — the desk in the dark room
- `LIGHT`: one small guest fire from the page's edge, and nothing else
- `DIRECTION`: from the right, at the page's edge
- `ACCENT`: the thin red line where the paper turns

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `フミ.identity` | `~/Desktop/受け火映像アセット/フミ.png` | 設定画（丸い背・指のインク・上着） |
| `フミ.negatives` | — | Negative の一覧（画像ではない） |
| `記憶.appearance` | `~/AI創作工房/distill-essence-engine/examples/works/novels/ukebi-anime/ukebi-anime-prop-sheet-記憶/霧深き線路に灯る記憶の灯火.png` | 物の設定画（机・窓・頁）。Desktop には無い——distill の採用済み |

⚠️ **デスクトップの畫像はこの端末の外にある**——clone しただけでは讀めない。`reference/` の畫像は clone で讀める。
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 生成物の置き場

`specs/image/ep03/ukebi-v3-ep03-12-m02b/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for the fire taking the edge of the page from the corner — the master staging of one scene from the story, in 16:9. [フミ: a thin man rounded forward at the back, short black hair still creased from sleep, a worn grey and burnt-brown jacket with the collar open, ink on the fingertips and along the nail edges, sunken eyes, no glasses] is the only figure, seated, his hand at the page. Eating along the edge, the paper darkening, inside the guest fire — the desk in the dark room, under one small guest fire from the page's edge, and nothing else. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the flame and the page edge, eating along the edge, the paper darkening, inside the guest fire — the desk in the dark room, lit by one small guest fire from the page's edge, and nothing else, with the thin red line where the paper turns. Every figure is cel-painted: flat colour planes on the skin, hair and cloth, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights; the place behind the figure is a painted anime background, finished to the same level as the painted background, with texture and soft modelling, never a flat diagram, never a photograph, never a 3D render. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long; the paper and the wood are matte and hold the light without shining. The camera is close on the page's corner. The flame travels the edge; the paper darkens and curls without burning the writing. His hand stays where it is. The palette is limited to sunken indigo, rust red, pale white-blue, black, and the white of paper, with the skin a warm pale grey-brown; the rust is a thin red line on the iron, the only warm colour outside the fire. There is no sky: no stars, no moon, no sun, no clouds, no horizon, no horizon glow, no gradient. The room is inside the fire: the crossing appears only as a wet edge at the border of the frame, never as a second room; no pavement, no asphalt, no concrete. The light is the guest fire's, small and low at the frame's edge; the rest of the room falls into black, and the pool of light has a hard edge. No gradient across any surface. The fire is small, a pale blue-white body palest at the centre and cooling to a faint blue at the edge with one thin rust-red rim; one closed contour, no tongue, no smoke, no steam, no sparks, no embers, no second flame.

no bloom, no lens flare, no glow, no god rays, no secondary light source, no sun, no moon, no stars, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no legible writing on the page, no pavement, no asphalt, no concrete, no second room, no stars, no moon, no sun, no sky, no horizon, no yellow-black barrier, no sign, no lamp
