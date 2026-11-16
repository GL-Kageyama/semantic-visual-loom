<!-- i18n-version: 1.0.0 | canonical: projects/ukebi/ukebi-v3/README.md | translated: 2026-11-17 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# 受け火 V3 — 改稿10話の映像化

`_archive/ukebi-v2` の後継。旧版は残す。この work は `bible.yaml` / `ledger.yaml` / `shots/` を持つ。**第3話がパイロットである。28本のショット記録と28本の画像仕様を持つ。動画の仕様は後回しにした。** 残り9話は [`episodes/`](episodes/index.md) で切ってあるが、まだ記録にしていない。全体は [`進捗表.md`](進捗表.md)、記録から導出した1枚は [`概要.md`](概要.md)、第3話は [`概要/ep03.md`](概要/ep03.md)。

## 何を作るか

- 改稿10話を、sVL の shot 記録へ移す。
- 設計の行は **222行**（S195＋M27）。切った後は **272本**——ep1 27／ep2 34／ep3 28／ep4 22／ep5 27／ep6 25／ep7 27／ep8 25／ep9 21／ep10 36。
- 話で切らない。ショットで切る。**1ショット1変化。**

## 正

| 何 | どこ |
|---|---|
| 物語・台帳 | `soul-voice-teller/examples/works/novels/ukebi-anime/台帳/`・`構想/design.md` |
| 改稿の散文 | `.../草稿/draft_*.md` |
| ショット表 | `.../草稿/ショット表_*.md`（ep2 は `第2話_送る_試作.md`） |
| 画像31枚 | `distill-essence-engine/examples/works/novels/ukebi-anime/`（31/31採用） |
| 旧版 | `../_archive/ukebi-v2/`・`../_archive/ukebi-video-*` |

⚠️ **本文とショット表はこのリポジトリの外にある。** clone しただけでは読めない。work の記録はここに置き、正は外に置く。

## パイロットの前に潰した穴

`_archive/ukebi-v2` を `check.py` に通した実測: **違反157／註60**。

- L16 `motion` 30件・L17 `Style Motion` 30件・L21 `no background music` 30件・L38 演出要約の帯 30件・L6 `attached` 30件。
- L14 5件（宣言を超えた不可逆変化）・L27 `bible.language` 1件・S0 `jsonschema` 1件。
- 註: L48／L50 `dramaturgy` 無し、L51 `population` 無し、L52 `body_parts` 無し、L18 `key_image` 無し。
- `check.py --self-test`: `jsonschema` が在れば513例中513例。無ければ S0 の例が走らない。`check_i18n.py --self-test`: 17/17。

**v3 は第3話でこの型を決めた。** 同じ穴を272回作らない。

## 決めたこと

1. **パイロット**: 第3話。28本の記録を書いた。
2. **経路**: 動画は WAN 3.0（後回し）、`key_image` は `CHATGPT IMAGE 2.5`。v2 は WAN 3.0 の30秒。改稿のショットはもっと短い。
3. `bible.language: Japanese`。`population`・`body_parts`・`cast` をショットごとに書く。
4. **31枚の対応表**: `REF_CHARACTER`／`REF_HANA`／`OKURIBI.sheet` が実ファイルを指すようにする。人物・空間が居る画にだけ添える。
5. **ep10 の場面板は改稿と食い違う。** 旧板は「台帳・秤・判を置かない」「彼の手は空」。改稿の ep10 は台帳を腕に抱え、質問の前に初頁の折れ目を見せる。焼き直すか、新しい板を足す。

## 順

1. ✅ 改稿から `bible.yaml` と `ledger.yaml` を書いた。名前はサチ・フミ・トワ・ナギ・花。開示は `構想/design.md` の表。
2. ✅ 第3話を `shots/` へ breakdown した（28本）。
3. ✅ 第3話の画像仕様を書いた（28本）。⏸ §1–20 と §18 の7スロットは後回し。`L11` と `L14` が動画の側の空を名乗る。
4. ◐ `reference_set`／`attached` はショットごとに書いた。`forbidden_set` はまだ導出していない。
5. 次: 残り244本の記録と画像仕様。そのあと動画の仕様。

## 触らない

- `../_archive/` は記録。直さない。
- `distill-essence-engine` のカードは読むだけ。書かない。
- 旧名（幸恵・結城文・折笠千代・早瀬甚吾・篠宮）を v3 へ持ち込まない。
