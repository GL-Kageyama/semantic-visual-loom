<!-- i18n-version: 1.0.0 | canonical: projects/ukebi/ukebi-v3/README.md | translated: 2026-11-15 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# 受け火 V3 — 改稿10話の映像化

`_archive/ukebi-v2` の後継。旧版は残す。この work はまだ `bible.yaml` / `ledger.yaml` / `shots/` を持たない。breakdown 前である。各話の枠は [`episodes/`](episodes/index.md) に置いた。枠であって、shot 記録ではない。

## 何を作るか

- 改稿10話を、sVL の shot 記録へ移す。
- ショット表の合計は **195本**——ep1 21／ep2 試作18／ep3 16／ep4 18／ep5 17／ep6 22／ep7 18／ep8 16／ep9 14／ep10 35。
- 話で切らない。ショットで切る。**1ショット1変化。**

## 正

| 何 | どこ |
|---|---|
| 物語・台帳 | `soul-voice-teller/examples/works/novels/ukebi-anime/台帳/`・`構想/design.md` |
| 改稿の散文 | `.../草稿/draft_*.md` |
| ショット表 | `.../草稿/ショット表_*.md`（ep2 は `第2話_送る_試作.md`） |
| 画像26枚 | `distill-essence-engine/examples/works/novels/ukebi-anime/`（26/26採用） |
| 旧版 | `../_archive/ukebi-v2/`・`../_archive/ukebi-video-*` |

⚠️ 本文とショット表はこのリポジトリの外にある。clone しただけでは読めない。work の記録はここに置き、正は外に置く。

## パイロットの前に潰す穴

`_archive/ukebi-v2` を `check.py` に通した実測: **違反157／註60**。

- L16 `motion` 30件・L17 `Style Motion` 30件・L21 `no background music` 30件・L38 演出要約の帯 30件・L6 `attached` 30件。
- L14 5件（宣言を超えた不可逆変化）・L27 `bible.language` 1件・S0 `jsonschema` 1件。
- 註: L48／L50 `dramaturgy` 無し、L51 `population` 無し、L52 `body_parts` 無し、L18 `key_image` 無し。
- `check.py --self-test` は 515例中510例（`jsonschema` 無しで5例落ちる）。`check_i18n.py --self-test` は 17/17。

v3 では、195本を書く前にこの型を決める。同じ穴を195回作らないためである。

## 決めること

1. **パイロット**：ep1（開幕・21ショット・5分）か ep3（改稿が一番大きい・16ショット・7分）。
2. **ルート**：WAN 3.0／MINIMAX H3／SEEDANCE 2.5。v2 は WAN 3.0 の30秒。改稿のショットはもっと短い。
3. `bible.language: ja`。`population` と `body_parts` をショットごとに書く。
4. **26枚の対応表**：`REF_CHARACTER`／`REF_HANA`／`OKURIBI.sheet` が実ファイルを指すようにする。人物・空間が居る画にだけ添える。
5. **ep10 の場面板は改稿と食い違う。** 旧板は「台帳・秤・判を置かない」「彼の手は空」。改稿の ep10 は台帳を腕に抱え、質問の前に初頁の折れ目を見せる。焼き直すか、新しい板を足す。

## 次の順

1. `bible.yaml` と `ledger.yaml` を改稿から書く。名前はサチ・フミ・トワ・ナギ・花。開示は `構想/design.md` の開示表（ep4 花が席に／ep5 初台詞／ep7 判／ep10 名）。
2. `breakdown` でパイロット1話を `shots/` へ。
3. `design` で §1–20 と §18 の7スロット。L16／L17／L21／L38／L6 の型を先に埋める。
4. `ledger` で `reference_set` / `forbidden_set`。26枚の実ファイルを指す。
5. `check.py` が0違反（または意図した除外を記録）になってから、絵10枚 → 全部見る → 動画。

## 触らない

- `../_archive/` は記録。直さない。
- `distill-essence-engine` のカードは読むだけ。書かない。
- 旧名（幸恵・結城文・折笠千代・早瀬甚吾・篠宮）を v3 へ持ち込まない。
