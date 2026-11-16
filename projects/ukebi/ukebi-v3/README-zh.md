<!-- i18n-version: 1.0.0 | canonical: projects/ukebi/ukebi-v3/README.md | translated: 2026-11-17 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# 受火 V3 — 改稿十话的影像化

`_archive/ukebi-v2` 的后继。旧版保留。这个 work 已有 `bible.yaml` / `ledger.yaml` / `shots/`。**第 3 话是试作：28 个镜头记录与 28 个图像规格。视频规格推迟。** 规格与生成物同居在同一个文件夹：`specs/image/ep03/<与规格相同的名>/`。生成物**不改名**——哪个镜头由文件夹承担。规格与文件夹同名，所以按连号顺序排列。 其余九话已在 [`episodes/`](episodes/index.md) 切好，但尚未写成记录。整体见 [`進捗表.md`](進捗表.md)，由记录导出的一页是 [`概要.md`](概要.md)，第 3 话是 [`概要/ep03.md`](概要/ep03.md)。

## 要做什么

- 把改稿十话移入 sVL 的 shot 记录。
- 设计的行合计 **222**（S195 + M27）；切开后合计 **272** 个暂定镜头——ep1 27 / ep2 34 / ep3 28 / ep4 22 / ep5 27 / ep6 25 / ep7 27 / ep8 25 / ep9 21 / ep10 36。
- 不按话切。按镜头切。**一个镜头，一个变化。**

## 正

| 什么 | 哪里 |
|---|---|
| 故事、台账 | `soul-voice-teller/examples/works/novels/ukebi-anime/台帳/`、`構想/design.md` |
| 改稿散文 | `.../草稿/draft_*.md` |
| 镜头表 | `.../草稿/ショット表_*.md`（ep2 是 `第2話_送る_試作.md`） |
| 31 张图 | `distill-essence-engine/examples/works/novels/ukebi-anime/`（31/31 已采用） |
| 旧版 | `../_archive/ukebi-v2/`、`../_archive/ukebi-video-*` |

⚠️ 正文与镜头表在本仓库之外。只 clone 本仓库读不到。work 的记录放在这里，正本放在外面。

## 试作前补上的洞

对 `_archive/ukebi-v2` 运行 `check.py` 的实测：**违规 157 / 注 60**。

- L16 `motion` 30 · L17 `Style Motion` 30 · L21 `no background music` 30 · L38 演出摘要带 30 · L6 `attached` 30。
- L14 5（超出声明的不再可逆变化）· L27 `bible.language` 1 · S0 `jsonschema` 1。
- 注：L48／L50 无 `dramaturgy`、L51 无 `population`、L52 无 `body_parts`、L18 无 `key_image`。
- `check.py --self-test`：有 `jsonschema` 时 513 例中 513 例；没有时 S0 的例不运行。`check_i18n.py --self-test`：17/17。

**v3 在第 3 话定了这个型。** 同一个洞不要做 272 次。

## 已决定的事

1. **试作**：第 3 话。28 个记录已写。
2. **路线**：视频为 WAN 3.0（推迟），`key_image` 为 `CHATGPT IMAGE 2.5`。V2 是 WAN 3.0 的 30 秒；改稿的镜头更短。
3. `bible.language: Japanese`。每个镜头写 `population`、`body_parts`、`cast`。
4. **31 张图的对应表**：让 `REF_CHARACTER` / `REF_HANA` / `OKURIBI.sheet` 指向真实文件。只在人物或空间出现的画面里附上。
5. **ep10 的场面板与改稿不一致。** 旧板写「不放台账、秤、印」「他的手是空的」。改稿的 ep10 把台账抱在臂中，并在提问前展示初页的折痕。重烧，或补一张新板。

## 顺序

1. ✅ 从改稿写了 `bible.yaml` 与 `ledger.yaml`。名字是 サチ、フミ、トワ、ナギ、花。开示按 `構想/design.md` 的表。
2. ✅ 把第 3 话 breakdown 进 `shots/`（28 个）。
3. ✅ 写了第 3 话的图像规格（28 个）。⏸ §1–20 与 §18 的七个槽推迟。`L11` 与 `L14` 报出视频侧的空。
4. ◐ 每个镜头写了 `reference_set` / `attached`。`forbidden_set` 尚未导出。
5. 下一步：剩余 244 个镜头的记录与图像规格。之后是视频规格。

## 不要碰

- `../_archive/` 是记录。不要改。
- `distill-essence-engine` 的卡片只读。不要写。
- 不要把旧名（幸恵、結城文、折笠千代、早瀬甚吾、篠宮）带进 v3。
