# 画像仕様 — 第3話「綴じる」 s04a「火が、彼の前で止まる」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）
- `SCENE`: the thin fire stopping in the air in front of a man, his face entering from the frame's edge
- `CHARACTERS`: [送り火: a man of medium height, short dark-indigo hair with the ears uncovered, a knee-length dark-indigo coat with the collar down, hands large for the body, narrow eyes, the mouth closed, no expression], with only the lower half of his face in the frame
- `SUBJECT`: the guest fire
- `ACTION`: drifting to a stop at the height of his mouth
- `LOCATION`: the level crossing at night — the rails behind, no hour and no sky
- `LIGHT`: one small soul fire off-frame at the upper right, lighting the lower half of his face; the stopped guest flame casts no light
- `DIRECTION`: from the upper right, outside the frame
- `ACCENT`: the rim of the soul fire along his jaw, and the small flame as the only bright shape

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `送り火.identity` | `~/Desktop/受け火映像アセット/送り火.png` | 設定画（顔・体格・コート・手） |
| `送り火.negatives` | — | Negative の一覧（画像ではない） |
| `踏切.base` | — | 画像なし——補正前の板は使わない。`base` は意図 |
| `魂火.appearance` | — | 画像なし——`_shared/fire.md` の block（掌・梅の大きさ・青白い芯） |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **`踏切.base` と `魂火.appearance` は画像を持たない。** 踏切の板は台帳と三箇所食い違うので使わない（舗装・腕木・灯）。魂火は block である。**画像が無いことを、欄を消して隠さない。**
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 投入する1本の文字列

A scene board for the thin fire stopping in the air in front of a man, his face entering from the frame's edge — the master staging of one scene from the story, in 16:9. [送り火: a man of medium height, short dark-indigo hair with the ears uncovered, a knee-length dark-indigo coat with the collar down, hands large for the body, narrow eyes, the mouth closed, no expression], with only the lower half of his face in the frame. Drifting to a stop at the height of his mouth, at the level crossing at night — the rails behind, no hour and no sky, under one small soul fire off-frame at the upper right, lighting the lower half of his face; the stopped guest flame casts no light. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the guest fire, drifting to a stop at the height of his mouth, in the level crossing at night — the rails behind, no hour and no sky, lit by one small soul fire off-frame at the upper right, lighting the lower half of his face; the stopped guest flame casts no light, with the rim of the soul fire along his jaw, and the small flame as the only bright shape. Solid things are cel-painted: flat colour planes, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long; wet gravel and standing water double the one light once. The camera is at the height of his mouth and does not move. The face enters from the right edge; the eyes are above the frame and are not seen.

no bloom, no lens flare, no glow, no god rays, no secondary light source, no sun, no moon, no stars, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no full face, no expression on the mouth
