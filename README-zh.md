<!-- i18n-version: 1.0.0 | canonical: README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# semantic-visual-loom

**把 AI 生成的故事一直运到电影的基盘。**

> **影像不是被生成的。是被剪辑的。**

生成模型做出来的是**标本**。**把它变成作品的是剪辑。**
所以这个基盘所持有的不是生成器，而是**制作的工程**——分解、设计、固定、生成、甄选、剪辑、验收。
放在其中心的单位是**镜头**，而承载状态的容器是**制作台账**。

**声音的姐妹**：`semantic-audio-loom`。以同样的做法配成一对（`semantic-` ＋ 感官的词 ＋ `-loom`）。

## 与既有 AI 影像工具的不同

| | 常见的样子 | 这个基盘 |
| --- | --- | --- |
| 单位 | 1 条提示词 ＝ 1 段视频 | **1 个镜头 ＝ 1 次生成**。作品是镜头的序列 |
| 状态 | 每次都重写进提示词 | 由**制作台账**持有（连续性＋开示） |
| 文字 | 让生成器去画 | 分离为**文字通道**，用合成烧进去 |
| 验收 | 目视 | **事前验证**——在规格的阶段报警矛盾 |

**最有效的是第二行。** 用各自不同的提示词做 30 个镜头，
**到第 8 个就不知道谁知道了什么。** 台账把这接过来了。

## 状态

**生成不在这个基盘里跑。事前验证会跑。**

```bash
python3 engine/ledger/check.py projects/hitosara         # 演示「Until One Plate Is Made」
python3 engine/ledger/check.py projects/ukebi/ukebi-v2   # Ukebi V2
python3 engine/ledger/check.py --self-test               # 检查器会不会报警
```

命令全表、所需之物、以及项目构成都在 [`docs/usage.md`](docs/usage-zh.md) 里。

**⚠️ 这个基盘所做的，只有事前验证、以及与回来了的东西的对照**（`L25`）。
**生成、甄选、剪辑不在基盘里**——作者用手去跑，基盘**读记录**。
⚠️ **`L25` 不打开 `media/`。** 所以**记录与实物的不一致不会报警。**
⚠️ **违规 0 件不是「正确」。** **要读注，要读没有被检查的范围。**

## 构成

**存在的东西**

```text
semantic-visual-loom/
├── schemas/         # 数据结构的正典（bible / ledger / shot-record / take / timeline）
├── engine/ledger/   # 制作台账与事前验证（不跑生成就把设计的破绽压掉）
├── docs/            # 用法
├── tools/           # 检查（i18n 的镜像）
├── references/      # 卡。包括从 distill 移管过来的 video-spec
└── projects/        # 每部作品的实体
```

**⚠️ `projects/` 里同居着两种东西**——**生的规格书**（Ukebi 与 Gozen-niji 的 §1–20，
就那样留着）与**结构化的记录**（`bible.yaml` / `ledger.yaml` / `shots/`；
有 `ukebi-v2` 与 `hitosara` 两本）。
⚠️ **生的规格书那一侧不放生成物，而 `reference/` 里的参照资产留着。**
**输入不是标本这件事、删掉会失去什么**，写在 [`docs/usage.md`](docs/usage-zh.md) 里。

## 演示 `projects/hitosara/`

**「Until One Plate Is Made」**——从粉、水、盐与时间开始，直到面包变成一盘。
10 个镜头。**与 Ukebi 完全独立。**

**把它放在这里，是为了展示这个基盘读的全部东西。**
它踩了一个 Ukebi V2 没有通过的目录——15 种职能中的 8 种、`mode` 的 3 个值全部、
`attached` 在每个镜头上、还用了 `text_channel` 与 `sound`。

⚠️ **所有镜头都有两条路径**——`spec:` 是视频，`key_image:` 是图像，而
**投进生成器的只有 §18。**
⚠️ **生成按 10 张图像 → 全部看过 → 10 段视频的顺序转。**
**其余在 [`projects/hitosara/README.md`](projects/hitosara/README-zh.md) 里。**

## 预定之中、但还没有的东西

```text
├── skills/          # 分解、设计、台账、镜头、构成、验收
├── engine/handover/ # 交接单（§18 的 7 个槽位、图像提示词、声音）与往返检查
├── engine/shot/     # 镜头记录的生成与检证
├── engine/visual/   # Visual Asset Engine
├── engine/assembly/ # 时间线、剪辑、文字合成、渲染
├── providers/       # 图像、视频、合成的生成器
├── assets/          # 参照资产（角色表、板）
└── interchange/     # OTIO / EDL / FCPXML
```

**⚠️ `timeline/` 只有 schema，一条记录也没有**——⚠️ **`SCHEMAS` 常量里有它的名字，
但没有人去读它。** schema 的一览在 [`docs/usage.md`](docs/usage-zh.md) 里。

## Next

**还没有着手。**

### 从 `distill-essence-engine` 里除去视频系的材料——⚠️ **那是那边的工作**

**在本仓库里没有要做的事**，**也不需要改变那边的方针。**
那边的固定方针规定了**「引擎不折进媒体，而是折进一次生成的容量」**，
并禁止**「写假定输出是单一画格的规则」**——
**要丢掉的不是方针，而是偏向视频的材料**（视频的例子，以及 `scripts/fetch.py` 里的 YouTube 获取）。
所以**在那边写一行「之后预定除去」就够了**——而且
**那边的多语言化已经完成**（en / ja / zh），**一行会变成三份文件。**

⚠️ **这个工作在那边的仓库里、按那边的规则做。**
本仓库的 `CLAUDE.md` 规定 `distill-essence-engine` **可以读，但绝不改写**。
⚠️ **§1–20 与 `video-spec.md` 的主人，已经移到这边了。**

## 语言

**开发用日语推进，文档的正典是英语。**
镜像用后缀方式并排在**同一个目录**里——规则在 [`CLAUDE.md`](CLAUDE-zh.md) 里。

**10 份文档 × 3 种语言已经齐备**，[`tools/check_i18n.py`](tools/check_i18n.py) 检查它们——
**它看什么、不看什么**，写在 [`docs/usage.md`](docs/usage-zh.md) 里。

## 许可证

MIT
