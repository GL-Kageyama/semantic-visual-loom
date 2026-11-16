<!-- i18n-version: 1.0.0 | canonical: projects/ukebi/README.md | translated: 2026-11-15 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# 受け火 — projects/ukebi

改稿10話の映像化を、ここで作る。旧版は `_archive/` に置いた。

## 配置

| パス | 中身 | 状態 |
|---|---|---|
| `ukebi-v3/` | 改稿10話（195ショット）の新しい work | README のみ。breakdown 前 |
| `_archive/ukebi-v2/` | 旧30ショット（30秒×30＝15分）の移行記録 | 旧版。名前・開示・仕様は改稿前 |
| `_archive/ukebi-video-00…09/` | 旧 §1–20 の生仕様（30本） | 旧版。読み取り専用 |
| `_archive/ukebi-video-00-series/` | 旧12本のシリーズ定数 | 旧版。読み取り専用 |

親を走らせても `_archive/` は読まれない（`check.py` は `shots/` を一段だけ読み、隣の作品へは降りない）。`ukebi-v2` の `spec:` は work の内側を指すので、移しても壊れない。

## 正

- 物語・台帳・ショット表は `soul-voice-teller/examples/works/novels/ukebi-anime/`。
- 画像の採用26枚は `distill-essence-engine/examples/works/novels/ukebi-anime/`。
- このリポジトリは、その二つを sVL の shot 記録へ移す。

## v2 をそのまま使わない理由

- v2 は旧30本仕様の移行記録。30ショット×30秒＝15分。改稿10話は195ショット・約71分。
- v2 の名前は旧い（幸恵・結城文・折笠千代・早瀬甚吾・篠宮）。改稿はサチ・フミ・トワ・ナギ・花。
- v2 の開示は ch08 で名が出る。改稿は第10話。
- v2 は改稿の ep1／ep3／ep10 と26枚のアセットを含まない。

## 次

[`ukebi-v3/README.md`](ukebi-v3/README.md) を見る。まず1話パイロット。
