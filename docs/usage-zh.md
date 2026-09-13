<!-- i18n-version: 1.0.0 | canonical: docs/usage.md | translated: 2026-09-14 -->

**Language:** [English](usage.md) | [日本語](usage-ja.md) | [中文](usage-zh.md)

# 用法

如何对项目的记录跑事前验证。

**这里只跑一件事。** 生成不在这个基盘里跑——
**由作者手工执行，基盘只读记录。**
跑的是那个**在生成之前**于规格阶段触发矛盾的检查
（以及生成之后，把回来的东西对上的那一步）。

## 需要什么

`python3` 和 PyYAML。**没有安装步骤。**

```bash
python3 -m pip install --user pyyaml
```

## 命令

```bash
python3 engine/ledger/check.py --self-test                 # 检查器到底会不会报警
python3 engine/ledger/check.py projects/hitosara           # 对一个项目做事前验证
python3 engine/ledger/check.py projects/ukebi/ukebi-v2     # Ukebi V2
python3 tools/check_i18n.py                                # 文档的镜像
```

| 参数 | |
|---|---|
| （位置参数） | 项目目录的路径。除非给了 `--self-test`，否则必需。 |
| `--schemas` | 模式（schema）目录。默认为 `<仓库>/schemas`。 |
| `--self-test` | 不接受项目。**当每一条例子都如预期时，以 `0` 退出。** |

⚠️ **`skills/` 的 4 个不是命令**——**是对 Claude Code 会话的指示。**
它们定下**分解（①）、设计（②）、台账（③）、镜头（④）**的决定顺序。
⚠️ **调用带着名字空间**——`/semantic-visual-loom:breakdown`、`:design`、`:ledger`、`:shot`。
⚠️ **⑥构成与⑦验收不在其中**——**因为输入不在记录那一侧。** 理由在
[`projects/hitosara/renders/README.md`](../projects/hitosara/renders/README-zh.md)。

## ⚠️ 正确读取退出码

| 退出码 | 含义 |
|---|---|
| **`0`** | 没有**违规** |
| **`1`** | 有违规 |

⚠️ **`0` 不是「正确」。** 报告里还带着**注**——读到了、但不是违规的东西——以及
**检查没有看过的范围。** **不报告的检查，看起来和通过的检查一样。**
不要只读数字，**要读注，读没有被检查的范围。**

## 项目是什么

`check.py` 取**项目目录**的路径并读它。
**它什么都不写，也不打开 `media/`。**

```
projects/<name>/
├── bible.yaml      # 世界、根本律、视觉语言（必需）
├── ledger.yaml     # 连续性＋开示，放在同一个文件里（必需）
├── shots/          # 一个镜头一张镜头记录（<id>.yaml）（必需）
├── takes/          # 回来的东西的记录
├── specs/          # §1–20 的文档（video/ 与 image/）
├── media/          # 生成物的存放处   ⚠️ 基盘不打开这里
├── renders/        # 由剪辑做出的东西（作品）
└── timeline/       # 剪辑
```

检查读的是 `bible.yaml` / `ledger.yaml` / `shots/` / `takes/`，以及
**镜头记录所指的规格文档**（`spec:` 与 `key_image:`）。

⚠️ **缺 `bible.yaml` / `ledger.yaml` / `shots/` 会被报告，而不会被悄悄当成空。**
而且**一个文件读不了，检查也会跑到底**——中途停下，
**会让一个坏掉的文件遮住其它所有的报告。**

⚠️ **`media/` 与 `takes/` 是两回事。** 一个存放处、一个记录——**放下过，不等于记录过。**
所以可能存在「文件在 `media/` 里、却没有镜次」的状态。
**因为检查不打开 `media/`，记录与实物相矛盾时不会报警**——那是一个洞，并且作为一个洞被报告。
**如果 `takes/` 是空的，它就说「没有一条镜次记录」。0 件不是合格。**

⚠️ **`projects/` 里同居着两种东西**——**生的规格书**与**结构化的记录**
（`bible.yaml` / `ledger.yaml` / `shots/`）。

⚠️ **`projects/ukebi` 和 `projects/gozen-niji` 是原始规格书，不是项目。**
它们没有 `bible.yaml` / `ledger.yaml` / `shots/`，所以跑检查会列出**「读不了」**，
并由 `L0` 报警：**「一个镜头都没有。检查什么也没看到。」**
**这不是错误，而是正确的行为。**

⚠️ **生的规格书那一侧不放生成物**——**只有记录与规格。**
**旧的生成物会降低作品品质的统一度。**

⚠️ **不过 `reference/` 里的参照资产留着**（**9 种**。被复制进每个分段）。
**那不是生成物，而是输入**——并且是**「哪个分段附了什么」的唯一记录**
（`wan-full-spec.md` 只把参照写成 `REF_STYLE` / `REF_SOURCE`）。
⚠️ **删掉它们，附着的记录也一起消失。** 这个数字的根据在 `HISTORY.md` 里。

⚠️ **`renders/` 是剪辑做出来的东西（作品）的存放处，`media/` 是标本的存放处。**
**标本与作品用场所分开**——不能用名字分开。
⚠️ **`timeline/` 的空，连那都不被报告**——因为还没有人打开它。
**不报告的检查，看起来和通过了的检查一样。**

## 层

检查由**26 层，`L0`–`L25`**，以及模式（schema）的形状验证构成。
**它不是单一判定**——每一层各自报警，并**连同它看到的数字**一起被报告。

⚠️ **什么也没看到的层会作为注被报告，而什么也没看到的层，看起来和通过的层一模一样。**
例如关于 `key_image` 的层，在镜次不持有 `key_image` 的项目上无法报警——
**因为没有可以比较的另一方。** **0 不是那一层表示同意的证据。**

**各层写在 [`engine/ledger/README.md`](../engine/ledger/README-zh.md) 里**——
每一层读什么、对什么报警、**以及它不看什么。**

## 模式（schema）

| 文件 | 是什么的正典 |
|---|---|
| `bible.schema.json` | 世界、根本律、视觉语言 |
| `ledger.schema.json` | 连续性与开示，放在同一个文件里 |
| `shot-record.schema.json` | 一个镜头 |
| `take.schema.json` | 一次生成回来的东西 |
| `timeline.schema.json` | 剪辑 ⚠️ **名字在 `SCHEMAS` 常量里，但还没有人读它** |

见 [`schemas/README.md`](../schemas/README-zh.md)。

## 文档检查

```bash
python3 tools/check_i18n.py --self-test   # 每条规则的报警例与不报警例
python3 tools/check_i18n.py               # 实物
```

⚠️ **它报告看过的文件数，以及被当作不变区块的那些块**——
没有这个，**什么也没看到的检查，看起来和通过的检查一样。**
⚠️ **它不看散文是否被正确翻译**——即使含义相矛盾，
**只要行和标题对得上，它就会通过。**

⚠️ **这个检查所看的方式**：正典**不带后缀**，镜像以**后缀方式**并排在**同一个目录**里
（`README.md` / `README-ja.md` / `README-zh.md`）。
**不创建 `-en` 镜像**——因为正典是英语。
⚠️ **不使用子文件夹方式（`ja/` `zh/`）**——为了让**正典与镜像的深度不发生变化**。
⚠️ **开发的工作语言保持日语**（提交信息、`HISTORY.md`、会话），
而**文档的正典是英语。** 这两者是不同的东西——**做事所用的语言**，与**文档具有权威所用的语言**。
**15 份文档 × 3 种语言已经齐备**（这是 `tools/check_i18n.py` 作为正典报告的本数），
规则在 [`CLAUDE.md`](../CLAUDE-zh.md) 里。

## 延伸阅读

| | |
|---|---|
| [`README.md`](../README-zh.md) | 这个基盘是什么，由什么构成 |
| [`engine/ledger/README.md`](../engine/ledger/README-zh.md) | 制作台账、各层、以及每个检查不看什么 |
| [`schemas/README.md`](../schemas/README-zh.md) | 数据结构 |
| [`projects/hitosara/README.md`](../projects/hitosara/README-zh.md) | 演示——10 个镜头，与 Ukebi 完全独立 |
