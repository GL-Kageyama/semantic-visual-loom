# 画像仕様 — 第3話「綴じる」 m03c「顔が上がり、閉じた戸を見る」

⚠️ **この仕様は §1–20 を持たない。** 画像プロンプトは節ではなく**1枚の文**である。
⚠️ **`REF_FORMAT` と `REF_STYLE` が、どのカードの穴かを名乗る。** `L22` が読む。
⚠️ このショットは**動画の仕様をまだ持たない**（`spec:` を書いていない）。`L11` が1本ずつ報告する。

## 主題

- `REF_FORMAT`: `scene-board` —— 5つの穴（`SCENE`／`CHARACTERS`／`ACTION`／`LOCATION`／`LIGHT`）
- `REF_STYLE`: `one-lamp-cel` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）
- `SCENE`: a face lifting from the page to a closed door
- `CHARACTERS`: [フミ: a thin man rounded forward at the back, short black hair still creased from sleep, a worn grey and burnt-brown jacket with the collar open, ink on the fingertips and along the nail edges, sunken eyes, no glasses] is the only figure, with only his face and shoulders in the frame
- `SUBJECT`: the face
- `ACTION`: lifting the face, the eyes stopping on the door
- `LOCATION`: inside the guest fire — the desk room, a closed door at the far side
- `LIGHT`: one small guest fire from below, and nothing else; the door stays in darkness
- `DIRECTION`: from below
- `ACCENT`: the pale line of the door's edge

## 参照画像

**生成のときに添える画像である。** ⚠️ **この節は意図であって、添付の記録ではない**——
何を添えたかは `takes/` に在る（まだ無い）。

| 台帳の鍵 | 添えるファイル | 何 |
|---|---|---|
| `フミ.identity` | `~/Desktop/受け火映像アセット/フミ.png` | 設定画（丸い背・指のインク・上着） |
| `フミ.negatives` | — | Negative の一覧（画像ではない） |
| `記憶.appearance` | `~/AI創作工房/distill-essence-engine/examples/works/novels/ukebi-anime/ukebi-anime-prop-sheet-記憶/霧深き線路に灯る記憶の灯火.png` | 物の設定画（机・窓・頁）。Desktop には無い——distill の採用済み |

⚠️ **パスはこの端末の外にある。** clone しただけでは読めない。
⚠️ **手だけのショットでも設定画を添える。** 添付はテキストに勝つので、`Negative` の「no face」「no second hand」を効かせる。

## 投入する1本の文字列

A scene board for a face lifting from the page to a closed door — the master staging of one scene from the story, in 16:9. [フミ: a thin man rounded forward at the back, short black hair still creased from sleep, a worn grey and burnt-brown jacket with the collar open, ink on the fingertips and along the nail edges, sunken eyes, no glasses] is the only figure, with only his face and shoulders in the frame. Lifting the face, the eyes stopping on the door, at inside the guest fire — the desk room, a closed door at the far side, under one small guest fire from below, and nothing else; the door stays in darkness. The blocking, the camera and the light are fixed as the standard every cut of this scene must match. One scene, one staging. The subject is the face, lifting the face, the eyes stopping on the door, in inside the guest fire — the desk room, a closed door at the far side, lit by one small guest fire from below, and nothing else; the door stays in darkness, with the pale line of the door's edge. Solid things are cel-painted: flat colour planes, clean closed lineart, hard-edged shadows in two clear steps, minimal specular highlights. Only the air is soft — a thin mist and fine ash suspended in it catch the single light at every depth, so the near ground, the middle distance and the far end separate into deep layers by value, never by a gradient laid across a surface. The light is small in the frame and the darkness around it is large; the shadows are long; wet gravel and standing water double the one light once. The camera is at his eye height. His face rises from the page and stops; the door is closed and no one stands at it. The frame holds after the eyes stop.

no bloom, no lens flare, no glow, no god rays, no secondary light source, no sun, no moon, no stars, no gradient across any surface, no airbrush, no painterly brush strokes, no photographic texture, not photorealistic, no 3D render, no watermark, no on-screen subtitles, no background music, no legible text, no crowds, no rain, no second person, no open door, no hand on the door
