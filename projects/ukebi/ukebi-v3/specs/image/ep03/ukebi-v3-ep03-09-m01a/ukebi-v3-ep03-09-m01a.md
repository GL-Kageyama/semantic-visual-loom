# 画像仕様 — 第3話「綴じる」 m01a「火の内側——机と、紙の束」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）
- `SCENE`: inside the flame — a desk and a sheaf of paper stacked without order
- `CHARACTERS`: No figure is in the frame
- `SUBJECT`: the desk, the sheaf and the dark room around them
- `ACTION`: lying still while the fire's edge moves at the border of the frame
- `LOCATION`: inside the guest fire — a desk in a dark room, the wet edge of the crossing at the border of the frame
- `LIGHT`: one small guest fire at the frame's edge, lighting only this interior, and nothing else
- `DIRECTION`: from the left edge of the frame
- `ACCENT`: the uneven top edge of the sheaf

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `記憶.appearance` | `~/AI創作工房/distill-essence-engine/examples/works/novels/ukebi-anime/ukebi-anime-prop-sheet-記憶/霧深き線路に灯る記憶の灯火.png` | 物の設定画（机・窓・頁）。Desktop には無い——distill の採用済み |
| `踏切.base` | — | 画像なし——補正前の板は使わない。`base` は意図 |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **`踏切.base` と `魂火.appearance` は画像を持たない。** 踏切の板は台帳と三箇所食い違うので使わない（舗装・腕木・灯）。魂火は block である。**画像が無いことを、欄を消して隠さない。**

## 生成物の置き場

`specs/image/ep03/ukebi-v3-ep03-09-m01a/` —— **このフォルダは在る。この仕様もこの中に在る。**
生成物はこの中へ、**名前を変えずに**置く。
⚠️ **ファイル名は記録ではない。** どのショットの出力かは、フォルダが持つ。

## 投入する1本の文字列

A scene board for inside the flame — a desk and a sheaf of paper stacked without order — the master staging of one scene from the story, in 16:9. No figure is in the frame. Lying still while the fire's edge moves at the border of the frame, at inside the guest fire — a desk in a dark room, the wet edge of the crossing at the border of the frame, under one small guest fire at the frame's edge, lighting only this interior, and nothing else. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the desk, the sheaf and the dark room around them, lying still while the fire's edge moves at the border of the frame, in inside the guest fire — a desk in a dark room, the wet edge of the crossing at the border of the frame, lit by one small guest fire at the frame's edge, lighting only this interior, and nothing else, with the uneven top edge of the sheaf. Solid things are cel-painted: flat colour planes, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long; wet gravel and standing water double the one light once. The camera is close on the desk. The room is shallow and dark; the crossing shows only as a wet edge at one border. Nothing on the desk moves.

no bloom, no lens flare, no glow, no god rays, no secondary light source, no sun, no moon, no stars, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no person, no figure, no hands
