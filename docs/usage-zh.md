<!-- i18n-version: 1.1.0 | canonical: docs/usage.md | translated: 2026-09-18 -->

**Language:** [English](usage.md) | [日本語](usage-ja.md) | [中文](usage-zh.md)

# 用法

如何对项目的记录跑事前验证。

**生成不在这个基盘里跑**——**由作者手工执行，基盘只读记录。**
跑的是那个**在生成之前**于规格阶段触发矛盾的检查（以及生成之后，把回来的东西对上的
那一步）。此外，还有打印**值已经被强制的行**的工具。

## 需要什么

`python3` 和 PyYAML。**没有安装步骤。**

```bash
python3 -m pip install --user pyyaml
```

## 命令

**命令有 3 个**——**做作品的 2 个，以及维护仓库的 1 个。**

```bash
# 检查器——在规格阶段触发矛盾
python3 engine/ledger/check.py --self-test                 # 检查器到底会不会报警
python3 engine/ledger/check.py projects/hitosara           # 对一个项目做事前验证
python3 engine/ledger/check.py projects/ukebi/ukebi-v2     # Ukebi V2

# 打印器——规格中可以导出的行。什么都不写
python3 engine/shot/print_spec.py projects/hitosara
python3 engine/shot/print_spec.py projects/hitosara --shot hitosara-ch01-seg04

# 仓库自身的文档检查——不用来做作品
python3 tools/check_i18n.py                                # 文档的镜像
```

**`engine/ledger/check.py`**

| 参数 | |
|---|---|
| （位置参数） | 项目目录的路径。除非给了 `--self-test`，否则必需。 |
| `--schemas` | 模式（schema）目录。默认为 `<仓库>/schemas`。 |
| `--self-test` | 不接受项目。**当每一条例子都如预期时，以 `0` 退出。** |

**`engine/shot/print_spec.py`**

| 参数 | |
|---|---|
| （位置参数） | 项目目录的路径。 |
| `--shot` | 只打印一个镜头。 |

⚠️ **两者不是二选一——它们覆盖的范围不一样。**
**`print_spec.py` 打印的行，是抄下去的瞬间就会沉默的行**（所以每一行都会报出它让谁沉默）。
**也就是说，`check.py` 报告不了那些行。** 反过来，**`check.py` 触发的东西，正是
`print_spec.py` 拒绝导出的东西。**
⚠️ **被强制的行交给打印器，被拒绝的交给检查器**——两者都不覆盖对方的范围。

⚠️ **`engine/shot/print_spec.py` 什么都不写**——它读记录、台账与作品台账，只打印
**值已经被强制的行**（§1 的四个作品常数、`Duration`、§19 的 `Instance ID`）。
⚠️ **把它贴上去是作者的行为。** 与磁盘上的规格不一致时，它把**两者**并列，然后停下。
它不导出的东西与留下的洞，在 [`engine/shot/README.md`](../engine/shot/README-zh.md) 里。

⚠️ **`skills/` 里的东西不是命令**——**是对 Claude Code 会话的指示**，
而**把故事变成规格的，正是这 4 个。** 见下面的 **四个阶段**。

## 四个阶段

**故事进去。交给生成器的字符串出来。**
⚠️ **4 个都不是程序**——是交给会话的文档，而
**这个仓库里没有这 4 个的代码。** 跑起来的只有检查器。

| 阶段 | 交出去的东西 | 出来的东西 | 落在哪里 |
|---|---|---|---|
| **① 分解** | 故事、情节、草稿 | 镜头序列、作品台账、开示的变化点 | `bible.yaml`、`ledger.yaml`、`shots/` |
| **② 设计** | 一个镜头 | 演出记录、§1–20 的视频规格（**§18 的 7 个槽位**）、图像规格——以及在**经由分镜（絵コンテ）的视频路径上，交给 `distill-essence-engine` 的板式提示词** | `shots/<id>.yaml`、`specs/video/<id>.md`、`specs/image/<id>.md`、`specs/board/<id>-board.md` |
| **③ 台账** | 一个镜头 | 被养大的台账，以及落在每个镜头记录上的导出集合 | `ledger.yaml`、`shots/<id>.yaml` |
| **④ 镜头** | 回来的东西 | 能独立成立的记录，以及镜次 ⚠️ **不采用** | `shots/<id>.yaml`、`takes/<id>-<kind>-<n>.yaml` |

**写提示词的是②。** 7 个槽位是 `Master` / `Visual` / `Motion` /
`Camera` / `Audio` / `Negative` / `Style Motion`——**全部是英语**，而
**分开这件事本身就是要点**
（[`references/formats/video-spec.md`](../references/formats/video-spec-zh.md) §18）。
⚠️ **分开交出去。过去的只有 §18**——§19 与 §20 是我们自己的记录。

⚠️ **§18 的标题自称模型，而视频的路径有三条。** `L18` 把这个标题与
登记簿（`specmap.MODELS`）对照——**`WAN 3.0` 取 `key_image`，`MINIMAX H3` 不取。**
后者的附件是**分镜图像**，而**制作那张图像的纸是 `distill-essence-engine`**
（格式 `storyboard`、样式 `luminous-anime`）。所以板式提示词也是这个基盘的文档，
住在 `specs/board/`。
⚠️ **分镜不是「图像的路径」。** 那张纸**要画文字**——格号、说明文、栏位——
而**图像路径的底板禁止画面上的文字。** 所以 `key_image` 持不了它。
**纸是拍摄之前的、整段视频的设计。** 生成器按顺序读它的格子，
**把每一格当作它自己的一场戏，与下一格之间由自然的动画接起来。**
⚠️ **第三条路径 `SEEDANCE 2.5` 默认什么都不附。** 它读一条很长的提示词，
**而那条提示词可以自带时钟**（`0-3s:` `3-6s:`）。⚠️ **而且它并不把 `Negative Prompt` 槽位
当作地板来接收**——厂商当作否定处理的**只有字幕与音频**，
**那个槽位剩下的部分会被当作散文来读。** **`L30` 响的就是这道门**——路径声明
「自己不接收的槽位」（`specmap.MODEL_UNRECEIVED_SLOTS`），填了它的规格会被报告。
**仍然要用这条路径的作品，就写 `bible.route_limits_accepted`**——**豁免由作品来写。**
⚠️ **各路径不共享时间的文法。** 落在 `MINIMAX H3` 上的约束——**交给它的字符串、
以及那张纸的文字，两者都在内**——在 [`docs/h3-route-zh.md`](h3-route-zh.md)，
而落在 `SEEDANCE 2.5` 上的在 [`docs/seedance-route-zh.md`](seedance-route-zh.md)。
⚠️ **没有任何东西检查板子。** 镜头记录没有任何栏指向它，所以 **`check.py` 从不打开它**
——**这是一个洞，并且作为一个洞被报告**
（见 [`engine/ledger/README.md`](../engine/ledger/README-zh.md) 的 `L18` 注）。
⚠️ **能解除底板某一节的，是作品，而且只能是作品。** `bible.base_negatives_waived` 是它唯一的席位。
⚠️ **曾经存在过第二个席位**——在一份规格的 §16 里写一行反引号，**仅限那个镜头**解除基础的节。
**它在造出来的当天就被拆掉了**，因为它所服务的那条裁定被撤回，而**再没有一份规格使用它。**
规则与实测在 [`engine/ledger/README.md`](../engine/ledger/README-zh.md)（`L21`）。

⚠️ **调用带着名字空间**——`/semantic-visual-loom:breakdown`、`:design`、`:ledger`、`:shot`、`:staging`。

⚠️ **①的输入形状未定。** 作品是**以情节来的、以脚本来的、还是以小说来的**，
这个仓库里哪里都没有写——和人或与会话一起读，**把你读到的形状记下来。**
⚠️ **而且镜头序列没有 schema**——`shot-record` 要求 `duration`，
**而决定它的是②。** 所以**只有①，出不了检查器能读的记录。**
⚠️ **在②落到磁盘上之前，检查器什么都读不到。**

⚠️ **⑥构成与⑦验收不在其中**——**因为输入不在记录那一侧。**
`clips[]` 按定义是采用镜次的列，而**视频镜次里一张 `adopted: true` 都没有。**
⚠️ **是动不了**，而⚠️ **吐出一条空时间线的 Skill，比没有 Skill 更糟。**
理由在 [`projects/hitosara/renders/README.md`](../projects/hitosara/renders/README-zh.md) 里。

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
├── specs/          # §1–20 的文档（video/ 与 image/），以及板式提示词（board/）
├── media/          # 生成物的存放处   ⚠️ 基盘不打开这里
├── renders/        # 由剪辑做出的东西（作品）
└── timeline/       # 剪辑
```

⚠️ **那个目录待在哪儿不是随意的。而且规则是单向的**——
**反过来不成立。** `projects/ukebi/` 就是理由（**11 棵生的规格书之树和 1 本作品**）：

> **所有作品都在自己的目录里带着自己的 `bible.yaml` 和 `ledger.yaml`。
> 但抱着作品的目录，并不一定本身就是作品。**
> ⚠️ **反过来不成立——作品不得抱着作品。**

⚠️ **`check.py` 不递归**——它**平着**读 `root/shots/*.yaml`。所以
**作品抱着作品时，跑父目录也读不到，而且输出不会说出来。**
`L29` 会点名没有被读到的作品。

检查读的是 `bible.yaml` / `ledger.yaml` / `shots/` / `takes/`，以及
**镜头记录所指的规格文档**（`spec:` 与 `key_image:`）。
⚠️ **`specs/board/` 不在其中**——**没有任何栏指向板子**，所以分镜提示词
**在任何一层之外。那是洞，不是豁免。**

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

检查由**34 层，`L0`–`L33`**，以及模式（schema）的形状验证构成。
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
**21 份文档 × 3 种语言已经齐备**（这是 `tools/check_i18n.py` 作为正典报告的本数），
规则在 [`CLAUDE.md`](../CLAUDE-zh.md) 里。

## 延伸阅读

| | |
|---|---|
| [`README.md`](../README-zh.md) | 这个基盘是什么，由什么构成 |
| [`docs/cards.md`](cards-zh.md) | **卡片的那两个轴**（Format / Style）、它们住在哪，以及**哪个检查读什么** |
| [`engine/ledger/README.md`](../engine/ledger/README-zh.md) | 制作台账、各层、以及每个检查不看什么 |
| [`docs/h3-route.md`](h3-route-zh.md) | 落在 `MINIMAX H3` 这条路径上的约束——交出去的字符串，以及那张纸 |
| [`docs/seedance-route.md`](seedance-route-zh.md) | 落在 `SEEDANCE 2.5` 这条路径上的约束——实测到的、它不接收的槽位、以及检查看不见的东西 |
| [`engine/shot/README.md`](../engine/shot/README-zh.md) | 打印器导出什么，以及它留下的七个洞 |
| [`schemas/README.md`](../schemas/README-zh.md) | 数据结构 |
| [`projects/hitosara/README.md`](../projects/hitosara/README-zh.md) | 演示——10 个镜头，与 Ukebi 完全独立 |
