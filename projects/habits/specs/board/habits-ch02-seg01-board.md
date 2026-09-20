# 絵コンテ — 『ハビッツ！！！』第二巻『重なった名』 第一話「八十軒目」 第一のショット「束が、受付の机から、助手席へ」（所作 / motion / 10s）

⚠️ **これはこの経路の①である**——**GPT Image 2.5 に描かせる絵コンテ**であり、
**②で MiniMax H3 がその画像を動画にする**（取り込み元は資料
『GPTimage2.5×MiniMaxH3による動画化手法』）。**この紙が、動画の設計そのものになる。**

⚠️ **この紙は「画像の経路」ではない。** `key_image` ではなく、`specs/image/` の仕様でもない
——**①は文字を描かせる**（コマ番号・日本語の説明文・欄）からである。**絵コンテは撮る前の紙である**
（`specmap.MODELS` の `MINIMAX H3` の註）。ゆえに `L21` の床（字幕を出すな）は**この紙には掛からない**
——⚠️ **掛からないことを、ここに書いておく。** **黙って外れた床は、外れたことが見えない。**

⚠️ **この紙を読む検査は、まだ無い。** ショットの記録にこの紙の欄が無く（`schemas/shot-record.schema.json`）、
`key_image:` にも書けない（画像の経路ではない）。**`L18` は「4 本が `key_image` を持たない」と註で言う。**
**ゆえにこの紙は、我々の検査の外にある。穴である**——**この穴は、穴のまま記録する**
（`schemas/` を動かして塞ぐ話は、まだしていない）。

---

## ✅ ずれの宣言（このサンプルが、著者の裁定から離れるところ）

**著者の裁定（2026-09-20）の文面は「1枚のボードに12コマ」であった。**
**このサンプルは、それを3枚に分けて持つ**（4＋4＋4＝12）。
⚠️ **12という数は守っている。割り方が違う。** 理由と、何がどうなるかを書く。

1. **固定方針「ショットが単位、1ショット＝1変化・1場所・一時刻」が、割る側の根拠である。**
   この一話の場面表は**三つの場面を三つの時刻で立てている**（朝／日中／日没前）。
   **1枚のボードに12コマを入れれば、1回の生成が三つの変化を運ぶことになる。**
   ⚠️ **MiniMax H3 の出力上限（4〜15秒）は、この割り方の理由ではない**（訂正 2026-09-20）——
   上限は**尺**の側の都合である。**12コマを3枚に分けたのは、方針の側である。**
2. **コマ数は、この一話の側では12のままである。** コマ番号を**通しで振る**——
   第一のボード `01`–`04`、第二 `05`–`08`、第三 `09`–`12`。
   **著者の12は、一話の通し番号として残る。** 変わったのは**生成の回数**（1 → 3）である。
3. ⚠️ **コマ数そのものも、出典からは離れている。** ①は「**16コマ前後**」と書く。
   **12は著者の裁定である**（`specmap.MODELS` の `MINIMAX H3` の註——「16コマはこの枠に入らない」）。
4. ⚠️ **これは発明（要承認）である**（方針 §5a）。**承認されていない。**

## ⚠️ `L3` は、このずれを鳴らさない（穴の記録）

**一話を1枚にすれば、一つの生成が三つの時刻を運ぶ。** `L3` は**時刻語が3種**で鳴る——
**朝と昼では2種である。鳴らない。**（`semantic.check_one_time` の閾値。2026-09-20 に確認。）
**鳴らないことは、許していることではない。** **検査の穴であって、設計の穴ではない**
——ゆえにこの紙は、**ずれを自分で書く**。

## ⚠️ ①の「白黒」から離れる（色で描く）

- ①は「**白黒の絵コンテ風で描く**」「白黒の線画ベースで、見本資料のように仕上げる」と書く。
- **この紙は、フルカラーである。** 根拠は我々の好みではない——
  **②の側が「フルカラーで作成してください。白黒の線画だけにしないでください」と書いている。**
  ②が動画に対して言うその一行を、**一工程ぶん手前で適用する**。
  ⚠️ **理由は、この経路の構造にある**——**①の紙は、そのまま②の動画の中身になる**からである
  （①の白黒は、②が打ち消すために存在する）。
  ⚠️ **第二の根拠**——この作品の様式 `luminous-anime` は**彩度を要求する**。
  その Negative は `no muted desaturated palette` を含む。**白黒の絵コンテは、この様式では作れない。**

## ⚠️ 文字の言語（①の「すべて日本語」と、家の「渡す文字列は英語」）

- ①は「**文字はすべて日本語**」「**英語表記は使わない**」と書く。**この紙も、そうする。**
- ⚠️ **それと、投入するプロンプトの言語は別である。** 家の規約は「**生成に渡す文字列は英語**」
  （`CLAUDE.md`）。ゆえに**下の `Merged` は英語であり、紙の上に描かれる文字はすべて日本語である。**
  **この二つは矛盾しない**——**指示の言語**と、**紙に焼かれる字**の話である。
- ⚠️ **人名はローマ字にしない**（決定）。プロンプトの中の「暮林蒼」は**日本語の字のまま置く。**
  ゆえに Negative は「**読める名**」を禁じるのであって、**字種を禁じない。**

## ⚠️ 画面の中の文字と、欄の文字（同じ紙の上で、別の規則が掛かる）

- **コマの中（絵）**——**読める文字は一つも無い。** 伝票も、宛名票も、貼り紙も、
  端末の画面も、**判読できない。** この作品の規則である（`bible.yaml`——**要承認**）。
- **欄（余白）**——**日本語で書く。** コマ番号・説明文・見出し・三つの欄は、
  **制作資料として読める**。**これは紙の側の文字であって、世界の中の文字ではない。**
- ⚠️ **この区別を書かないと、モデルはどちらかに倒れる**——
  **欄を潰すか、コマの中に読める名を描く。** 下の Negative は、そこを名指しで禁じている。

## ⚠️ コマの画角は「単調でない」ために選ばない

- ①は「引き・中距離・寄り・横顔・後ろ姿・俯瞰・あおり・足元アップ などを**バランスよく**入れて、
  **単調にならないように**」と書く。
- **この紙は、それをしない。** 画角は**この作品の定数**が決める——
  **三つの置き場**（run-10【ルックとカメラ】——「カメラは、机上の手、左袖の名札、
  めくられる名簿の三箇所に置かれる」）と、**一話に一度だけの手の近景**
  （同じ定数——「**手の近景を毎話一つ。**」）。
- ⚠️ **三つのショットのうち、手の近景を使うのは第三のショットである**（`habits-ch02-seg03.md` §10）。
  **ゆえにこの紙の4コマは、手に寄らない。** **発明（要承認）**——出典は「毎話一つ」という
  **予算**を与えるだけで、**どのショットが使うかは書いていない。**

---

## 渡す先

- 生成器: `chatgpt-image-2.5`（種別 `image`）——**投入は著者が手で行う。** このリポジトリは回さない
- 作る道具: `distill-essence-engine`——**フォーマット `storyboard`（`table` モード・絵コンテ表）／
  様式 `luminous-anime`**（2つの軸を別々に引く）
  - ⚠️ **カードの `table` は「カット番号／絵／内容（＋秒数）」の縦3列である。**
    ①はこれに**三つの欄**（キャラクターデザイン／舞台設定／作品メモ）を足す——
    **カードの拡張であり、発明（要承認）である。**
  - ⚠️ **カードは `table` を「文字を許す様式」と組むよう言う**（`storyboard.md`——`manga-ink` を名指す）。
    `luminous-anime` の Negative は**文字を禁じていない**（`no legible text` を持たない）。
    **ゆえにこの組み合わせは成立する。**
- 入力: `bible.yaml` ＋ `ledger.yaml` ＋ `shots/habits-ch02-seg01.yaml` ＋
  `distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md`（設定画 改訂稿5）
- 記録: `shots/habits-ch02-seg01.yaml` ※**この紙の欄は、まだショットの記録に無い**（穴）
- 生成物の置き場: このディレクトリ（`01_….png`）。**まだ無い。**

## 渡す先の穴（エンジンへの入力・10欄）

- `REF_FORMAT`: `storyboard` —— 7つの穴（`SUBJECT`／`N`／`SHOT`／`ARRANGEMENT`／`CUT`／`CONTENT`／`SECONDS`）
- `REF_STYLE`: `luminous-anime` —— 4つの穴（`SUBJECT`／`ACTION`／`LOCATION`／`ACCENT`）
- ⚠️ **`SUBJECT` は両方のカードに在る**——7＋4＝11 ではなく、**和は10**である。

- `SUBJECT`: 暮林蒼が、営業所の受付で伝票の束を受け取り、助手席に置く
- `N`: 4
- `SHOT`: MEDIUM／MEDIUM／CU（引き出し）／MEDIUM ※**手の近景は無い**（上の宣言）
- `ARRANGEMENT`: `table`（絵コンテ表・縦・上から下）
- `CUT`: 01／02／03／04（**一話の通し番号**。第二のボードは 05–08）
- `CONTENT`: 各コマの動作＋台詞＋日本語の説明文（下表）
- `SECONDS`: 3／2／3／2（**不均等**——ショットの記録の拍のまま）
- `ACTION`: 名を呼ばずに用件から入り、束を受け取り、腕を伸ばさずに助手席へ置き、ラジオをつけない
- `LOCATION`: 足立区の営業所の受付——朝、蛍光灯の下、日の出前の勤務日
- `ACCENT`: 蛍光灯の管が、そろえられた束の端に当たる一点のハイライト

## 内容（Content）

**②選択＝「秒を得るのは、そろえられた端と、つけられないラジオである」。**
場面表は「**この話の速さは、呼ばないことから来る**」と書く。このショットで一番長いのは
01（3秒）と03（3秒）——**用件から入る口と、端をそろえる指**である。
⚠️ **台詞の山（02）に秒を与えない**——**名はあとから来るのだから、短い。**

**③翻訳＝particular × indirect。** この作品の主題（**受け取る人の名前を覚えないまま、
その家の玄関の段差だけを覚えている**——`series-bible.md`）を、このショットは**一行も説明しない。**
代わりに**「名を呼ばずに、用件から入る」**という動作に置く——
**覚えないことが、無礼ではなく手順として出る。**
⚠️ **罠は二つ。** ①**名を読ませる紙を描くこと**——読める名を置けば、この作品の前提が一枚で終わる。
②**顔を先に置くこと**——受付の人が先に顔を上げれば、**「手が先にあり、顔が後に来る」が反転する。**

**⑧忠実の要＝運搬は完了しない・誰も足さない・読める名は無い・ラジオはつかない。**
束は**置かれる**のであって、**届けられない。** 受付の人は**この話の二十八名の誰でもない**
——⚠️ **台帳に鍵が無いので、`attached` にも `forbidden_set` にも欄が無い**（穴。
`habits-ch02-seg01.yaml` の末尾に記録）。**ボードでは「受付の手」として描き、名を与えない。**

## フォーマット（Format）

絵コンテ表 `table`：**カット番号／絵／内容**の縦3列に、**右の余白へ三欄**
（「キャラクターデザイン」「舞台設定」「作品メモ」）。上に**日本語の全体タイトルと副題**。
**コマ番号は通し**（`01`–`04`）。**秒数は不均等**（3／2／3／2）。
⚠️ **四つの秒の合計が、このショットの尺である**（`10s`——`habits-ch02-seg01.md` §1）。**合計を変えない。**
⚠️ **1カットの絵は1枚である。カットを小分けにしない**——表は4行であり、絵も4枚である。
**割ると、生成器はコマを4枚ではなく6〜7枚と数え、カットわりが 03|04 の1箇所である保証が消える。**
**紙は制作資料として整然と**——罫線、欄、余白。**コマは16:9の小さな絵。**

| カット | 絵（画角） | 秒 | 内容欄（日本語） |
|---|---|---|---|
| `01` | 受付の前、中距離（二人が机の高さで読める。**受付は、後ろ姿**） | 3 | 名を呼ばずに、用件から入る。顔は、まだ置かれない。 |
| `02` | 机の上の**受付の**手と、遅れて来る**受付の**顔。中距離 | 2 | 手は、机の上にある。名は、あとから来る。 |
| `03` | 引き出しに寄る（手には寄らない）。**絵は1枚** | 3 | 置く前に、指で、端をそろえる。そろえる音が、する。小さい。 |
| `04` | 助手席へ。中距離。**絵は1枚** | 2 | 腕を伸ばさない。胸の下で持つ。ラジオは、つけない。 |

## 様式（Style）

`luminous-anime`——**光が主題**。ただしこの場面の光は**夕日ではなく蛍光灯**である。
管は枠の上端か、そのすぐ外。**滲みは管の周りに置き、光源の側へ寄せる。**
彩度は光の当たる側に、影は深いシアン。**狭いパレット**——蛍光灯の白、机の灰色、
輪ゴムの茶、暖色は肌と紙だけに残す。
線は**細く一定**、面ごとの影は**一色**、境界は**硬い**、**柔らかいエアブラシを使わない。**
埃は光の中に浮かせ、**一本ずつ**描く。余白を広く、密度は低く。
**紙は、プロの制作資料として整っていること**——罫線、欄、見出し、詰め込みすぎない余白。

## 合成プロンプト（Merged）

A luminous realist anime storyboard of the first shot of 『ハビッツ！！！』 volume two 『重なった名』, episode one 「八十軒目」 — a bundle of delivery slips going from the counter of a depot to the passenger seat of a van — drawn as a Japanese ekonte sheet: a vertical table of cut number / picture / content, four rows, read top to bottom, **each row's picture cell holding exactly one image — one cut is one picture, and a cut is never divided into smaller pictures inside its cell**, with a Japanese title and subtitle across the top and three ruled margin columns headed 「キャラクターデザイン」「舞台設定」「作品メモ」, the whole sheet laid out as a professional production document on paper, ruled and orderly with generous margins.

Row 1: cut 01, a picture panel (16:9) MEDIUM — a depot counter before the day starts under a fluorescent tube; the courier stands at it and opens with the business and not with a name, **and the person at the counter is here as a hand at the desk and as a back turned to him — the face that is not placed yet in this cut is the counter's face, not his**, [暮林蒼: 「おはようございます。昨日のぶん、ありますか。」]; content column 「名を呼ばずに、用件から入る。顔は、まだ置かれない。」, 3 seconds. Row 2: cut 02, MEDIUM — **the hand on the desk is the counter's hand and the face that rises late is the counter's face, not the courier's**: her hand stays flat on the desk while her face has not yet risen, and it rises after the line has been answered — **the hand first and the face after, and the order is never swapped**; the courier is in the panel and his own face may be read, but the beat belongs to her, [受付: 「暮林さん、おはようございます。ありますよ。」]; content column 「手は、机の上にある。名は、あとから来る。」, 2 seconds. Row 3: cut 03, **one picture** — CU on the drawer as it opens and shuts with its sound arriving after it — the hand enters the frame but the panel is not held on it — and the bundle of slips is set on the counter after fingers square its edge; **the drawer and the squared edge are one image, not two**; content column 「置く前に、指で、端をそろえる。そろえる音が、する。小さい。」, 3 seconds. Row 4: cut 04, **one picture** — MEDIUM — the bundle is taken one-handed below the chest without the arm extending, set on the passenger seat so the seat takes a shallow dent, the key turns and the engine catches, and the radio is not turned on; **the taking, the setting down and the key are one image of the van interior, not three pictures**; content column 「腕を伸ばさない。胸の下で持つ。ラジオは、つけない。」, 2 seconds.

The same protagonist in every panel — 暮林蒼, a last-mile delivery courier of twenty-six, the tallest figure this work draws, his identity locked to the frozen setting sheet: the forehead broad with the cap worn shallow so the breadth still reads, cheekbones spreading wide and setting the width of the face, a short jaw whose corner stands with a square chin, a long nose with the tip falling, large ears standing out sideways, black hair cut short enough to sit under the cap; a work jacket and cap of a delivery company, a handheld terminal clipped at one hip so the belt dips on that side alone; and forearms whose skin below the sleeve is darker than his face, the skin the sleeve covers paler than either; the same depot, the same fluorescent key and the same grey counter in the three panels at the counter, and the same brown of two rubber bands across all four panels. ⚠️ **The place changes between cut 03 and cut 04** — the counter closes the third cut and the van opens the fourth — **and the sheet draws them as two separate panels, not as one room**; only the bundle and the hand carrying it are in both. The person at the counter is present as a hand that has not left the desk and, later, as a face — **a woman of about fifty, shorter than 暮林蒼 and not built like a courier, her hair short and gathered at the back of the head, in a collared shirt of a grey colder than the counter it is seen against with its sleeves rolled to the elbow, so her forearms are bare above the desk; no outer garment, no cap, no work jacket, no terminal at the hip, nothing of his costume on her, and the screen she works at faces away from him** — never named, never given a key, drawn the same way in both panels. **All lettering on the sheet is Japanese** — the title, the subtitle, the cut numbers and every caption — and **no English lettering appears anywhere on the sheet**; inside the panels there is **no legible text at all**: no readable name on any slip, no count written beside the bundle, only the ruled surface of paper and the square edge a hand has squared. **Deliberately uneven seconds.**

Clean anime lineart on the figures at one thin even weight with no thickening at the contour, held deliberately subordinate to the light; cel shading in a single shadow tone per material with the boundary left crisp, no second tone inside one piece of cloth; saturated where the fluorescent light falls and deep cyan in the unlit half, a narrow palette of fluorescent white, counter grey, rubber-band brown, and the warm side reduced to skin and to paper; bloom around the tube at the upper edge of the frame; dust suspended in the air and individually rendered; generous negative space and low visual density. **The panels are drawn in full colour, not as black-and-white line art.**

not photorealistic, no photograph of a real person, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces, no thick contour line, no gradient shading, no soft airbrush, no second shadow tone within a single material, no rendered fabric fold, no legible text inside any panel, no legible name on any in-world prop, no legible text on the delivery slips, no count written beside the bundle, no romaji in place of the Japanese name, no English lettering anywhere on the sheet, no lettering on the sheet beyond the title, the subtitle, the column headings, the cut numbers, the content column and the three margin columns, no revision stamp on the sheet, no stamp of any kind on the sheet, no studio name and no artist name printed on the sheet, no second person added to any panel, no courier behind him, no colleague invented at the counter, no completed delivery, no receiving hand at a door, no signature, no smile, no tears, no fear, no exaggerated expression, no face placed before the name is called, no calling voice as a sound effect, no voice-over, no narration, no panel frame drawn inside a panel, no cut divided into smaller pictures, no second picture inside a cut's cell, no subtitle inside a panel, no wall clock, no calendar, no digital timer, no date stamp, no specimen chart, no measured chart of steps, no figure written beside any step, no furigana field, no printed form, no name written by the courier, no watermark, no signature block, no artist credit burned into the picture, no morphing or drifting facial identity

## 記録との対応

- `shot`: `habits-ch02-seg01` ／ `unit.before` → `unit.after`（束が机の端に寄せられ、手には無い → 助手席に置かれ、手はもう束に無い）
- `beats`: 0-3s 用件から入る／3-5s **受付の**顔が遅れて来る／5-8s 引き出しと、端をそろえる／8-10s 受け取り、助手席へ、ラジオはつけない
  ——**この4拍が、そのまま 4コマである。** **コマ数はここから出ている**（発明ではない）
  ⚠️ **そして1カットの絵は1枚である**（上の Format）。**割ると、この4拍が6〜7枚になり、
  カットわりが 03|04 の1箇所である保証が消える。**
  ⚠️ **手と顔の主は受付である**——`3-5s` の拍は「**受付の人が、顔を上げる**」であり、
  §3 の「**手が先にあり、顔が後に来る**」も**受付の側の規則**である（`habits-ch02-seg01.md` §3・§11・§12）。
  **蒼の顔は置いてよいが、この拍は彼女のものである。**
- `place` / `time`: `宛名票の一行` ／ `朝（営業所を出るまで）`
- `attached`: `暮林蒼.identity`・`暮林蒼.negatives`・`伝票の束.appearance`・`伝票の束.negative`・`宛名票の一行.base`
- ⚠️ **この紙は、動画の仕様 §18 の `REF_BOARD` である**（`specs/video/habits-ch02-seg01.md` §6）。
  **動画の側は、この紙を「順序と構図の設計」として受け取る。**
- ⚠️ **動画の §18 は「漫画の枠線、番号、説明文、字幕などは動画に表示しない」と書く**（②の規則）。
  **この紙に在るものは、動画には入らない。** 紙と動画は、同じ設計の別の面である。
- ⚠️ **この紙は、まだ生成されていない。** 置き場はこのディレクトリ、名は `01_….png` の形である。
