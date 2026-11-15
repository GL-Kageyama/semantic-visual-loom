<!-- i18n-version: 1.0.0 | canonical: projects/ukebi/ukebi-v3/README.md | translated: 2026-11-15 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# 受火 V3 — 改稿十话的影像化

`_archive/ukebi-v2` 的后继。旧版保留。这个 work 还没有 `bible.yaml` / `ledger.yaml` / `shots/`。尚在 breakdown 之前。各话的框架在 [`episodes/`](episodes/index.md)。是框架，不是 shot 记录。

## 要做什么

- 把改稿十话移入 sVL 的 shot 记录。
- 镜头表合计 **195**——ep1 21 / ep2 试作 18 / ep3 16 / ep4 18 / ep5 17 / ep6 22 / ep7 18 / ep8 16 / ep9 14 / ep10 35。
- 不按话切。按镜头切。**一个镜头，一个变化。**

## 正

| 什么 | 哪里 |
|---|---|
| 故事、台账 | `soul-voice-teller/examples/works/novels/ukebi-anime/台帳/`、`構想/design.md` |
| 改稿散文 | `.../草稿/draft_*.md` |
| 镜头表 | `.../草稿/ショット表_*.md`（ep2 是 `第2話_送る_試作.md`） |
| 26 张图 | `distill-essence-engine/examples/works/novels/ukebi-anime/`（26/26 已采用） |
| 旧版 | `../_archive/ukebi-v2/`、`../_archive/ukebi-video-*` |

⚠️ 正文与镜头表在本仓库之外。只 clone 本仓库读不到。work 的记录放在这里，正本放在外面。

## 试作前要补的洞

对 `_archive/ukebi-v2` 运行 `check.py` 的实测：**违规 157 / 注 60**。

- L16 `motion` 30 · L17 `Style Motion` 30 · L21 `no background music` 30 · L38 演出摘要带 30 · L6 `attached` 30。
- L14 5（超出声明的不再可逆变化）· L27 `bible.language` 1 · S0 `jsonschema` 1。
- 注：L48／L50 无 `dramaturgy`、L51 无 `population`、L52 无 `body_parts`、L18 无 `key_image`。
- `check.py --self-test`：515 例中 510 例（没有 `jsonschema` 时 5 例失败）。`check_i18n.py --self-test`：17/17。

V3 在写 195 个镜头之前先定这个型。同一个洞不要做 195 次。

## 要决定的事

1. **试作**：ep1（开场·21 镜头·5 分钟）还是 ep3（改稿最大·16 镜头·7 分钟）。
2. **路线**：WAN 3.0 / MINIMAX H3 / SEEDANCE 2.5。V2 是 WAN 3.0 的 30 秒；改稿的镜头更短。
3. `bible.language: ja`。每个镜头写 `population` 与 `body_parts`。
4. **26 张图的对应表**：让 `REF_CHARACTER` / `REF_HANA` / `OKURIBI.sheet` 指向真实文件。只在人物或空间出现的画面里附上。
5. **ep10 的场面板与改稿不一致。** 旧板写「不放台账、秤、印」「他的手是空的」。改稿的 ep10 把台账抱在臂中，并在提问前展示初页的折痕。重烧，或补一张新板。

## 顺序

1. 从改稿写 `bible.yaml` 与 `ledger.yaml`。名字是 サチ、フミ、トワ、ナギ、花。开示按 `構想/design.md` 的表（ep4 花入席／ep5 初台词／ep7 印／ep10 名）。
2. 用 `breakdown` 把试作一话写进 `shots/`。
3. 用 `design` 写 §1–20 与 §18 的七个槽。先补 L16／L17／L21／L38／L6 的型。
4. 用 `ledger` 导出 `reference_set` / `forbidden_set`。指向 26 张真实文件。
5. `check.py` 达到 0 违规（或记录有意的除外）之后，再 10 张图 → 全部看 → 视频。

## 不要碰

- `../_archive/` 是记录。不要改。
- `distill-essence-engine` 的卡片只读。不要写。
- 不要把旧名（幸恵、結城文、折笠千代、早瀬甚吾、篠宮）带进 v3。
