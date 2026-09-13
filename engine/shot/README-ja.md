<!-- i18n-version: 1.0.0 | canonical: engine/shot/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# engine/shot/ — 仕様の骨を刷る

**ショットの仕様のうち、導出できる行を刷る**——記録と、台帳と、作品台帳から。
**1バイトも書かない。** `projects/` にも、仕様にも、どこにも。

```bash
python3 engine/shot/print_spec.py projects/<project>              # 全ショット
python3 engine/shot/print_spec.py projects/<project> --shot <id>  # 1本だけ
```

⚠️ **刷られた行を貼るのは、著者である。** この道具は、強制されるものだけを示す。

## 刷るもの

**6行**——1本の仕様の、**166** 行（空行を除く）に対してである
（`hitosara-ch01-seg04`）。

| 行 | 出所 | 写すと黙る検査 |
| --- | --- | --- |
| §1 `Aspect` | `bible.constants.video.aspect` | `L26` |
| §1 `Resolution` | `bible.constants.video.resolution` | `L26` |
| §1 `Frame Rate` | `bible.constants.video.frame_rate` | `L26` |
| §1 `Orientation` | `bible.constants.video.orientation` | `L26` |
| §1 `Duration` | `shot.duration` | `L23` |
| §19 `Instance ID` | `shot.shot` | `L13` |

⚠️ **この道具の値打ちは、行が埋まることではない。** **行ごとに「その行を手で写すと、
どの検査が黙るか」を名指しすることである。** 手で写した行は、**写し元が動いても誰も
鳴らさない**——`L23`・`L26`・`L13` が在るのは、**まさにその行についてそれが鳴るから**である。

⚠️ **仕様は、この6行から組み上がるのではない。** ここは**機械が既に答えを知っている**
部分である。残りが仕事である。

## ⚠️ 導出しないもの

**§2 WORLD、§3–§5、§7–§13、§14 DIALOGUE、§15–§17、§18（7スロット）、§20**——これらは
著者が書く。`print_spec.py` は**毎回この一覧を名乗る**——**数は、数えた範囲の広さしか
持たないからである。**

### §6 REFERENCES —— 形が安定していない

⚠️ **これは前提ではなく、実測である。** 構造化した2作品は、§6 を別々に書く。

| | `projects/hitosara` | `projects/ukebi/ukebi-v2` |
| --- | --- | --- |
| 文法 | ``- REF_KEY: `value` (HIGH)`` | ``- `REF_KEY` — `value` · `HIGH`。`` |
| 鍵 | 6つ: CHARACTER / LOCATION / GEOGRAPHY / STYLE / FORMAT / SOURCE | 5つ: CHARACTER / STYLE / FORMAT / SOURCE / BIBLE |
| 値の語彙 | カード名（`luminous-anime`） | パス（`references/styles/soft-cel-anime.md`） |

⚠️ **形が安定していない欄は、導出できない。** 導出すれば、この道具は**作品ごとに1回
嘘をつく**——同じ行について、同じ書式で、**確信をもった誤った値**を、両方の作品で刷る。
だから §6 は読まない。穴は下に書いてある。

## 作品定数の家

`bible.constants.video`——`aspect` / `resolution` / `frame_rate` / `orientation`。

⚠️ **`duration` はそこに無い。** 尺は**従属変数**である——家は `shot.duration` で、
読む者は `L23` である。ここに置けば、**同じ欠陥を2つの層が別の符号で報告する**ことに
なる。

⚠️ **これは新しい欄ではない。**
`projects/ukebi/ukebi-video-00-series/series-constants.md` が §1 の定数を
**全12本ぶん、手で**持っており、`schemas/bible.schema.json` は `bible` をその後継と
名指ししている。**家は既にそこに在った——そして、誰も読んでいなかった。**

⚠️ **作品定数は3箇所へ手で写されていた**——§1、§19 の `Output:` 行、（受け火では）
`series-constants.md`。そして**写しは既にずれ始めている。**

## これを読む者

- **`L26`** —— `bible.constants.video` と §1 の4行を突き合わせる
- **`engine/shot/print_spec.py`** —— この道具

⚠️ **`L26` は今日、1件も鳴らない**——**160** 件を比べて（構造化した2作品・40本の仕様
× 4欄）、食い違いは **0** 件である——そして註がそう言っている。
⚠️ **鳴らないことは、要らないことと同じではない。** この層が守っている故障は
**既にこのリポジトリに在る**（§19 の `Output:` 行は 10/10 で綴りが違う）。そして `L23` も、
**40/40** で一致しながら kept である。

## 何も決めない

⚠️ **この道具は何も書かず、何も決めない。** 導出値とディスク上の仕様が食い違えば、
**両方を並べて**止まる。**どちらが正しいかは著者の判断である**——`L25` と同じ立場である。

## まだ無いもの

**直さずに、書く**——それがこのリポジトリの流儀である。

1. **§19 の `Output:` は三つ目の手写しである。** **10/10** の仕様で綴りが違う
   （`1920×1080` / `landscape` 対 §1 の `1920x1080` / `Landscape`）。値は一致し、綴りは
   一致しない。**だから `L26` はそこを読まない**——読めば**10件の偽陽性**が出る。
   正規化して読むか、4欄に割るか、散文のまま置くかは**未決定である。**
2. **§19 `Instance ID` の中の `<seconds>` を、誰も見ていない。** `L13` は末尾の
   `-<seconds>s-<take>` を剥がしてから比べるので、**識別子の中に写された尺は、
   何とも比べられていない。**
3. **`bible.constants` の散文4項目を、誰も読んでいない**（`根本律`、`光源`、`カメラ`、
   `様式変数`）。機械可読にする方法は**未決定である。**
4. **§6 の `REF_CHARACTER` は導出できない。** §6 は **9/10** のショットでこれを引き、
   `reference_set` が `BAKER.sheet` を運ぶのは **4/10** である——**「人物が付いている」
   とは何かについて、両側が食い違っている。**
5. **seg04 の `REF_LOCATION` の上書きは、どこにも記録されていない。** `KITCHEN/朝` の
   5本は**同じ位置の参照**（`KITCHEN.base` + `KITCHEN.geography`）を運ぶのに、§6 は
   4本で `-morning` のボードを、seg04 で裸の `hitosara-kitchen-board` を引く。
   `(place, time)` から導出すれば **9/10** で、**10本目は記録から区別できない。**
   ⚠️ ここがこの文書でいちばん確かな穴である——**選択は §6 自身にしか無い。**
6. **seg10 の §6 は `hitosara-kitchen-geography` を引く**のに、その `reference_set` は
   地理を1つも宣言していない（`TABLE.base`）——§6 は「LOW: 部屋は示唆のみ」と言う。
   §6 の地理の引用が `reference_set` に対応物を持たないショットは、**これ1本だけである。**
7. **`locations.KITCHEN.states.朝.board` は、どのショットの `reference_set` からも
   引かれていない**のに、§6 はその値を **4本**で使う。（`昼` は seg06 が、`明け方` は
   seg07/08 が、`MILL.朝` は seg01 が引く——引かれていないのは `KITCHEN.朝` だけである。）

⚠️ **4–7 は、作品の欠陥ではない。** **記録が、仕様のしていることを知らない**箇所である。
直すとすれば、**選択に家を与えること**であって、**道具に推測させることではない。**
