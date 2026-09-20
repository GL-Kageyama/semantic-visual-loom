# 絵コンテ — 『ハビッツ！！！』第二巻『重なった名』 第一話「八十軒目」 第二のショット「箱が、玄関の前に置かれ、一行が、目に入る」（所作 / motion / 14s）

⚠️ **この紙は経路の①である**（GPT Image 2.5 の絵コンテ → ②で MiniMax H3 が動画にする）。
**紙の上に描かれる文字はすべて日本語であり、投入する文字列は英語である。**
**コマの中に読める文字は無く、欄には日本語が読める。**

⚠️ **この紙は「画像の経路」ではない**（①は文字を描かせるからである）——
`key_image` でも `specs/image/` の仕様でもない。**ゆえに `L21` の床（字幕を出すな）はこの紙に掛からない。**
⚠️ **この紙を読む検査は、まだ無い。** 穴である（`habits-ch02-seg01-board.md` の見出しに、まとめて書いた）。

⚠️ **このサンプルは、著者の裁定の「1枚のボードに12コマ」を3枚に分けて持つ**（4＋4＋4＋……12）。
**この紙はその2枚目**（通し番号 `05`–`08`）。**理由と宣言は
`specs/board/habits-ch02-seg01-board.md` の見出しに書いた**——⚠️ **要旨だけ再掲する**：
**固定方針「1ショット＝1変化・1場所・一時刻」が割る側の根拠である。**
**1枚に12コマを入れれば、1回の生成が三つの変化（朝・昼・日没前）を運ぶ。**
**コマ数12は一話の通し番号として残る。変わったのは生成の回数である。**
**これは発明（要承認）である。**

⚠️ **この一話の「一拍」は、このショットである。** **このサンプルで最も長い一枚**（14秒）——
**一拍に最大の秒を与える。三枚ともコマ数は4である。差は、密度ではなく、秒である。**
⚠️ **ゆえにこの紙は、この一話でいちばん長い紙である。**

## ⚠️ この紙に固有の四つのこと

1. **このショットに、台詞は無い**（「誰も、出てこない。」）。**それでも言語は日本語である**——
   欄の文字がすべて日本語であることは、この作品の言語の名乗りでもある
   （動画の §18 は無言の一枚でも言語を名指しする。実測 2026-09-18——名指ししないと中国語の字幕が焼かれた）。
2. **宛名票は、この一話でこの一枚だけが画面に持つ。** ゆえに**この紙の Negative が最も重い**
   ——**票は在り、誰にも読めない。** **票を消すのも、読ませるのも、別の話になる。**
3. ⚠️ **箱の側面の票には、四つの欄が罫線で引かれているだけである。** **名は書かれていない**
   ——**「欄がある」ことは描いてよい。** **「名が読める」ことは描かない。**
4. ⚠️ **四角いものは、名指ししない。** 出典は形だけを書く（草稿——「四角いものを、箱へ、向ける。」）。
   **この紙も名を与えず、何であるかを決めない。** **画面は光るが、その中身は読めない。**

## ⚠️ 画角の宣言（走りの側の規則）

**この紙の4コマは、手の近景を使わない。** run-10【ルックとカメラ】の
「**手の近景を毎話一つ。**」は**第三のショット（`09`–`12`）が使う**。
⚠️ **このショットの主題は手である**（箱を置く手）。**それでも距離を保つ**——
**ここで寄れば、一話の予算を、止まらない手に使うことになる。**
**06 のコマだけは低い位置に置く**（足と砂利＝①の「足元アップ」に当たる）が、
**これは手の近景ではない。**
⚠️ **①は「引き・中距離・寄り・横顔・後ろ姿・俯瞰・あおり・足元アップを、バランスよく」と言う。
この紙は、そのために画角を選ばない**——**画角はこの作品の定数が決める**（発明（要承認））。

---

## 渡す先

- 生成器: `chatgpt-image-2.5`——**投入は著者が手で行う。**
- 作る道具: `distill-essence-engine`——**フォーマット `storyboard`（`table` モード）／様式 `luminous-anime`**
- 入力: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-ch02-seg02.yaml` ＋
  設定画 改訂稿5（`distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md`）
- 記録: `shots/habits-ch02-seg02.yaml` ※**この紙の欄は、まだショットの記録に無い**（穴）
- 生成物の置き場: このディレクトリ（`05`–`08` のボード1枚 → `02_….png`）。**まだ無い。**

## 渡す先の穴（エンジンへの入力・10欄）

- `SUBJECT`: 暮林蒼が、箱を玄関の前に置き、宛名票のいちばん上の行が目に入る
- `N`: 4
- `SHOT`: MEDIUM／LOW ANGLE（砂利と足）／MEDIUM／MEDIUM ※**手の近景は無い**
- `ARRANGEMENT`: `table`（絵コンテ表・縦・上から下）
- `CUT`: 05／06／07／08
- `CONTENT`: 各コマの動作＋日本語の説明文（下表）
- `SECONDS`: 4／3／3／4（**不均等**——ショットの記録の拍のまま）
- `ACTION`: 車を止め、箱を降ろして玄関の前に置き、四角いものを二度向け、一行が目に入り、目は上がらない
- `LOCATION`: 足立区の住宅の前——勤務日の真ん中、日のある路上
- `ACCENT`: 四角いものの画面が光り、その光が箱と手に落ちる——この一枚で唯一の新しい光

## 内容（Content）

**②選択＝「秒を得るのは、四歩目の無音と、止まった目である」。**
この紙で最も長いのは 05（4秒）と 08（4秒）——**置かれる前と、見られた後**である。
⚠️ **台詞が無いので、秒は音と目に配られる。** **砂利の三歩に音を与え、四歩目に与えない。**
**それがこの紙の音の設計である。**

**③翻訳＝particular × indirect。** この作品の主題（**受け取る人の名前を覚えないまま、
その家の玄関の段差だけを覚えている**）を、**このショットは一行も説明しない。**
代わりに**「一行が目に入って、顔が追わない」**という動作に置く——
**読まないことが、無関心ではなく手順として出る。**
⚠️ **罠は三つ。** ①**票を読ませること**——読める名を描けば、作品の前提が一枚で終わる。
②**顔を上げさせること**——この一枚の主題は「目が止まる」であって「見上げる」ではない。
③**人を出すこと**——誰かが出れば、置くことが届けることに変わる。

**⑧忠実の要＝運搬は完了しない・一段・四歩目は鳴らない・名は読めない。**
**箱は置かれるのであって、渡されない。** **住人は出てこない**（台帳——運搬は一度も完了しない）。

## フォーマット（Format）

絵コンテ表 `table`：**カット番号／絵／内容**の縦3列に、**右の余白へ三欄**
（「キャラクターデザイン」「舞台設定」「作品メモ」）。上に**日本語の全体タイトルと副題**。
**コマ番号は通し**（`05`–`08`——第一のボードの続きである）。**秒数は不均等**（4／3／3／4）。
⚠️ **四つの秒の合計が、このショットの尺である**（`14s`——`habits-ch02-seg02.md` §1）。**合計を変えない。**
⚠️ **1カットの絵は1枚である。カットを小分けにしない**——表は4行であり、絵も4枚である。
**割ると、生成器はコマを4枚ではなく、それ以上の数として数える。**
**紙は制作資料として整然と。コマは16:9。**

| カット | 絵（画角） | 秒 | 内容欄（日本語） |
|---|---|---|---|
| `05` | 路肩に止まる車の後ろ。中距離（扉は上がったまま） | 4 | 車が、止まる。エンジンは、止まる。鍵は、抜かない。後ろの扉が、上がる。 |
| `06` | 砂利と足。低い位置から | 3 | いちばん手前の箱を取る。重さで、腕が下がる。歩幅は、狭い。砂利が三歩、鳴る。四歩目は、鳴らない。 |
| `07` | 段差の前の箱と、四角いもの。中距離 | 3 | 段差の前に、箱を置く。手が、離れる。四角いものを、向ける。画面が、光る。もう一度、向ける。 |
| `08` | 箱の側面と、その下の段差。目線より低く、中距離。**頭・胴・足が、同じ距離で、同じ枠に入る**（紙に寄らない） | 4 | いちばん上の行が、目に入る。足は、段差を上がっている。目は、上がらない。誰も、出てこない。 |

## 様式（Style）

`luminous-anime`——**光が主題**。この場面の光は**真昼の、狭い道の、硬く平らな日差し**である。
**票の白が、画面でいちばん明るい。** **箱の端が、いちばん暗い。**
**車の落とす影は深いシアン。** 砂利の上に埃が浮く。**埃は一本ずつ描く。**
線は**細く一定**、面ごとの影は**一色**、境界は**硬い**、**柔らかいエアブラシを使わない。**
彩度は光の当たる側に寄せ、**暖色は肌と葉だけに残す。**
余白を広く、密度は低く。**紙は、プロの制作資料として整っていること。**

## 合成プロンプト（Merged）

A luminous realist anime storyboard of the second shot of 『ハビッツ！！！』 volume two 『重なった名』, episode one 「八十軒目」 — a box set down in front of a house's entrance, and one line of the address slip glued to its side entering a man's eye — drawn as a Japanese ekonte sheet: a vertical table of cut number / picture / content, four rows, read top to bottom, **each row's picture cell holding exactly one image — one cut is one picture, and a cut is never divided into smaller pictures inside its cell**, with a Japanese title and subtitle across the top and three ruled margin columns headed 「キャラクターデザイン」「舞台設定」「作品メモ」, the whole sheet laid out as a professional production document on paper, ruled and orderly with generous margins.

Row 1: cut 05, a picture panel (16:9) MEDIUM — a delivery van stopped at the kerb of a narrow residential street at midday, its rear door rolled up and staying up, the boxes still on the bed behind; content column 「車が、止まる。エンジンは、止まる。鍵は、抜かない。後ろの扉が、上がる。」, 4 seconds. Row 2: cut 06, LOW ANGLE at the gravel — the nearest box comes off the bed, the arm drops under its weight and then recovers, the stride is narrow, and three steps of gravel are taken while the fourth makes no sound; content column 「いちばん手前の箱を取る。重さで、腕が下がる。歩幅は、狭い。砂利が三歩、鳴る。四歩目は、鳴らない。」, 3 seconds. Row 3: cut 07, MEDIUM — the box is set down in front of the single step and the hands leave it, and a small square object is raised toward the box with its screen lighting and showing nothing legible, its frame cutting the box's edge, and then raised a second time; content column 「段差の前に、箱を置く。手が、離れる。四角いものを、向ける。画面が、光る。もう一度、向ける。」, 3 seconds. Row 4: cut 08, **one picture** — MEDIUM held below his eye line, **and the lens stays at that one middle distance for the whole panel: it does not close on the paper, and the slip is small in the frame**; **his head, his body and his foot are all at that same distance and all in the frame together** — the head in the upper part of the frame, the foot on the step at the entrance, **and the body between them in the frame connecting the two, so that the head and the foot read as one person at one distance and not as two things at two distances**; the box's side and the single step sit in the lower half of the frame with the printed slip glued to the box's side, peeling at one edge with dust caught in the lift and four ruled fields on it, nothing written on it legible in any alphabet; the topmost line of it enters his eye while his foot is already taking the single step at the entrance and his eye does not rise, and nobody comes out of the house; content column 「いちばん上の行が、目に入る。足は、段差を上がっている。目は、上がらない。誰も、出てこない。」, 4 seconds.

The same protagonist in every panel — 暮林蒼, a last-mile delivery courier of twenty-six, the tallest figure this work draws, his identity locked to the frozen setting sheet: the forehead broad with the cap worn shallow so the breadth still reads, cheekbones spreading wide and setting the width of the face, a short jaw whose corner stands with a square chin, a long nose with the tip falling, large ears standing out sideways, black hair cut short enough to sit under the cap; a work jacket and cap of a delivery company, a handheld terminal clipped at one hip so the belt dips on that side alone, and forearms whose skin below the sleeve is darker than his face, the skin the sleeve covers paler than either; nothing about him dirtier or looser than in the morning of the same day. He is alone in every panel: no resident, no passer-by, no second courier. The box is pale cardboard with a printed address slip glued to its side, four fields ruled on the slip; in front of the entrance there is gravel, one worn step, a closed door, and a gatepost with ivy cut partway up. **All lettering on the sheet is Japanese** — the title, the subtitle, the cut numbers and every caption — and **no English lettering appears anywhere on the sheet**; inside the panels there is **no legible text at all**, not on the slip, not on the box, not on the screen of the square object; only ruled lines and headings. **Deliberately uneven seconds.**

Clean anime lineart on the figure at one thin even weight with no thickening at the contour, held strictly subordinate to the light; cel shading in a single shadow tone per material with the boundary left crisp, no second tone inside one piece of cloth; saturated where the hard flat noon light falls and deep cyan in the shadow the truck throws, a narrow palette of the pale of cardboard, the white of the slip, the grey of the gravel, and the warm side reduced to skin and to leaves; bloom on the pale surfaces; dust suspended over the gravel and standing in the lift of the slip's lifted edge, individually rendered; generous negative space and low visual density. **The panels are drawn in full colour, not as black-and-white line art.**

not photorealistic, no photograph of a real person, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces, no thick contour line, no gradient shading, no soft airbrush, no second shadow tone within a single material, no rendered fabric fold, no legible text inside any panel, no legible name on any in-world prop, no legible text on the address slip, no legible text on the screen of the square object, no romaji in place of the Japanese name, no English lettering anywhere on the sheet, no lettering on the sheet beyond the title, the subtitle, the column headings, the cut numbers, the content column and the three margin columns, no revision stamp on the sheet, no stamp of any kind on the sheet, no studio name and no artist name printed on the sheet, no character added beyond the storyboard, no resident at the door, no one coming out of the house, no passer-by, no cyclist, no dog, no second delivery courier, no completed delivery, no receiving hand, no opened door, no signature, no knock, no calling out, no head raised to the door, no eye lifted from the slip, no face turned up, no smile, no tears, no fear, no exaggerated expression, no second step, no stairs, no house number rendered readable, no number written on or beside the box, no voice-over, no narration, no speech balloon, no panel frame drawn inside a panel, no cut divided into smaller pictures, no second picture inside a cut's cell, no close-up of the face in this panel, no head drawn at a larger scale than the foot, no disembodied head, no head and foot at two different distances, no body missing between the head and the foot, no close frame on the slip, no subtitle inside a panel, no wall clock, no calendar, no digital timer, no date stamp, no specimen chart, no measured chart of steps, no figure written beside any step, no furigana field, no printed form, no name written by the courier, no watermark, no signature block, no artist credit burned into the picture, no morphing or drifting facial identity

## 記録との対応

- `shot`: `habits-ch02-seg02` ／ `unit.before` → `unit.after`（箱は荷台にあり、票の一行はまだ目に無い → 箱は玄関の前に降り、一行が目に入っている。**目は上がらない。誰も出てこない。**）
- `beats`: 0-4s 車が止まり、扉が上がる／4-7s 箱を取る——腕が下がり、砂利が三歩鳴る／7-10s 箱を置き、四角いものを二度向ける／10-14s いちばん上の行が目に入り、足は段差を上がり、目は上がらない
  ——**この4拍が、そのまま 4コマである**
- `place` / `time`: `宛名票の一行` ／ `昼（八十軒目）`
- `disclosure_state`: `宛名票の一行.いちばん上の行: present`——**開示の変化点は、この一枚である。**
  （ゆえに動画の §18 Negative は、この一枚で①と節の集合が一致することを要求される。**この紙の Negative は別の勘定である。**）
- `attached`: `暮林蒼.identity`・`暮林蒼.negatives`・`宛名票の一行.appearance`・`宛名票の一行.negative`
- ⚠️ **この紙は、動画の仕様 §18 の `REF_BOARD` である**（`specs/video/habits-ch02-seg02.md` §6）。
- ⚠️ **動画の §18 は「漫画の枠線、番号、説明文、字幕などは動画に表示しない」と書く**（②の規則）。
  **この紙に在るものは、動画には入らない。**
- ⚠️ **この紙は、まだ生成されていない。**
