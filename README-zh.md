<!-- i18n-version: 1.0.0 | canonical: README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# semantic-visual-loom

<p align="center">
  <img src="assets/repo-hero.png" width="100%" alt="semantic-visual-loom">
</p>

**把故事一直运到电影的基盘。**

> **故事，变成一连串的镜头。**

**生成模型做出来的是标本**——而且**独立的生成之间，互不相识。**
所以状态要放在生成之外。**那个容器就是制作台账。一个文件**，
把连续性与开示放在一起。

放在其中心的单位是**镜头**——⚠️ **一个镜头为一个变化而存在。**
**长度是从属变量。**

## 与既有 AI 影像工具的不同

| | 常见的样子 | 这个基盘 |
| --- | --- | --- |
| 单位 | 1 条提示词 ＝ 1 段视频 | **1 个镜头 ＝ 1 次生成**。作品是镜头的序列 |
| 状态 | 每次都重写进提示词 | 由**制作台账**持有（连续性＋开示） |
| 文字 | 让生成器去画 | 分离为**文字通道**，用合成烧进去 |
| 验收 | 目视 | **事前验证**——在规格的阶段报警矛盾 |

**最有效的是第二行。** 用各自不同的提示词做 30 个镜头，
**到第 8 个就不知道谁知道了什么。** 台账把这接过来了。

## 现状能做什么

**故事进去。交给生成器的字符串出来。**

**生成不在这个基盘里跑。** 基盘所做的，是
**把故事变成镜头的规格**，以及**在生成之前，把其中的矛盾报警出来。**

| | 交出去的东西 | 出来的东西 |
| --- | --- | --- |
| **① 分解** | 故事、情节、草稿 | **镜头序列**——按一个变化的单位切开，每个镜头带一个职能——以及作品台账与开示的变化点 |
| **② 设计** | 一个镜头 | **§1–20 的规格**与**图像规格**——其中 **§18 的英语 7 个槽位**，就是交给生成器的字符串 |
| **③ 台账** | 一个镜头 | **台账**（被养大）以及从中导出的**参照集合**（被固定的东西）与**禁制集合**（不得拍到的东西） |
| **④ 镜头** | 回来的东西 | **镜次**——一次生成，一张 |

**写提示词的是②。** 7 个槽位是 `Master` / `Visual` / `Motion` / `Camera` /
`Audio` / `Negative` / `Style Motion`，而**分开这件事本身就是要点**
（[`references/formats/video-spec.md`](references/formats/video-spec-zh.md) §18）。

⚠️ **提示词由两个轴构成，而两者都是卡片**——**Format（形式＝规格的形状）**与
**Style（样式＝视觉语言）**。⚠️ **卡片默认位于本仓库的旁边**
（`distill-essence-engine/references/formats` 与 `.../styles`）——而
**这一侧作品的卡片，是叠加而不是替换**：

```bash
SVL_FORMATS_DIR=references/formats SVL_STYLES_DIR=references/styles \
  python3 engine/ledger/check.py projects/ippitsu
```

⚠️ **没有人指点的卡片，没有人读**——而**被点名却读不到的卡片会触发违规**。
所以要**设置环境变量。不设置，作品自己的卡片就不可见。**
**两个轴是什么、它们在哪里、哪一项检查读什么**，见
[`docs/cards-zh.md`](docs/cards-zh.md)。

⚠️ **①–④ 是对 Claude Code 会话的指示，不是程序**——它们定下的是
**决定的顺序**，而**这个仓库里没有这 4 个的代码。**
⚠️ **而且在②落到磁盘上之前，检查器什么都读不到**——镜头记录要求 `duration`，
决定它的是②。

```bash
python3 engine/ledger/check.py projects/hitosara         # 演示「Until One Plate Is Made」
python3 engine/ledger/check.py projects/ukebi/ukebi-v2   # Ukebi V2
python3 engine/ledger/check.py --self-test               # 检查器会不会报警
python3 engine/shot/print_spec.py projects/hitosara      # 打印值已被强制的行
```

四个阶段、命令全表、所需之物、以及项目构成都在 [`docs/usage.md`](docs/usage-zh.md) 里。

**⚠️ 跑起来的，只有事前验证、以及与回来了的东西的对照**（`L25`）。
**生成、甄选、剪辑不在基盘里**——作者用手去跑，基盘**读记录**。
⚠️ **`L25` 不打开 `media/`。** 所以**记录与实物的不一致不会报警。**
⚠️ **违规 0 件不是「正确」。** **要读注，要读没有被检查的范围。**

## 构成

**存在的东西**

```text
semantic-visual-loom/
├── schemas/         # 数据结构的正典（bible / ledger / shot-record / take / timeline）
├── engine/ledger/   # 制作台账与事前验证（不跑生成就把设计的破绽压掉）
├── engine/shot/     # 打印镜头规格中可以导出的行（只读。什么也不写）
├── docs/            # 用法，以及更深入的解说（cards / routes）
├── skills/          # 4 个 Skill——分解、设计、台账、镜头
├── tools/           # 检查（i18n 的镜像）
├── references/      # 这一侧的卡片——formats/（video-spec）与 styles/（sumi-e）
├── assets/          # 仓库的脸（README 的 hero）
└── projects/        # 每部作品的实体
```

**⚠️ `projects/` 里同居着两种东西**——**生的规格书**（Ukebi 与 Gozen-niji 的 §1–20，
就那样留着）与**结构化的记录**（`bible.yaml` / `ledger.yaml` / `shots/`；
有 `hitosara`、`ukebi-v2`、`habits` 与 `habits-promo-chinatsu` **四本**）。
⚠️ **所有作品都带着自己的 `bible.yaml` 和 `ledger.yaml`，作品不抱着作品**
——而这正是它要紧的理由：**`check.py` 不递归**，所以
**作品抱着作品时，跑父目录也读不到。** `L29` 会点名没有被读到的作品。
⚠️ **生的规格书那一侧不放生成物，而 `reference/` 里的参照资产留着。**
**输入不是标本这件事、删掉会失去什么**，写在 [`docs/usage.md`](docs/usage-zh.md) 里。

## 演示 `projects/hitosara/`

**「Until One Plate Is Made」**——从粉、水、盐与时间开始，直到面包变成一盘。
10 个镜头。**与 Ukebi 完全独立。**

[![Until One Plate Is Made](https://i.ytimg.com/vi/pJyiziIUaPY/hqdefault.jpg)](https://www.youtube.com/watch?v=pJyiziIUaPY)

⚠️ **那里面是作品，不是标本**——区别在
[`projects/hitosara/renders/README.md`](projects/hitosara/renders/README-zh.md)。
⚠️ **而且，这个基盘真正要说的事，影像里映不出来**——
**10 个镜头，是从一张台账里出来的。** 那就是上面表的第 2 行，
**也是影像自己无法主张的唯一一件事。**

**把它放在这里，是为了展示这个基盘读的全部东西。**
它踩了一个 Ukebi V2 没有通过的目录——15 种职能中的 8 种、`mode` 的 3 个值全部、
`attached` 在每个镜头上、还用了 `text_channel` 与 `sound`。

⚠️ **所有镜头都有两条路径**——`spec:` 是视频，`key_image:` 是图像，而
**投进生成器的只有 §18。**
⚠️ **生成按 10 张图像 → 全部看过 → 10 段视频的顺序转。**
⚠️ **这是视频自称 `WAN 3.0` 的那条路径。** 在第二条视频路径（`MINIMAX H3`）上，
**镜头根本没有图像路径**——生成器拿到的是分镜图像，
而制作那张纸的提示词住在 `specs/board/`（[`docs/usage.md`](docs/usage-zh.md)）。
⚠️ **各路径不共享时间的文法**——落在第二条上的约束在
[`docs/h3-route.md`](docs/h3-route-zh.md) 里。
⚠️ **第三条视频路径 `SEEDANCE 2.5` 默认什么都不附**——它读一条很长的提示词，
**而那条提示词可以自带时钟**——但是**它的 `Negative Prompt` 槽位并不被当作地板来接收。**
**`L30` 响的就是这道门**——约束在 [`docs/seedance-route.md`](docs/seedance-route-zh.md) 里。
**其余在 [`projects/hitosara/README.md`](projects/hitosara/README-zh.md) 里。**

## 预定之中、但还没有的东西

```text
├── engine/handover/ # 交接单（§18 的 7 个槽位、图像提示词、声音）与往返检查
├── engine/visual/   # Visual Asset Engine
│                    #   参照资产已经住在各作品自己的 `reference/` 里——69 处、9 种。
│                    #      那就是它现在的住处。
│                    #   ⚠️ 未定——中央的置场，与重复的处理（同一张图最多被复制 37 次）。
│                    #      §6 的 `REF_*` 名字，什么也没有指着。
│                    #   ⚠️ `assets/` 已成仓库的脸（README 的 hero），所以不能放在那里。
│                    #      卡的实体是 `distill-essence-engine` 的财产，从这里只能读。
│                    #   ⚠️ 未定——台账的值用全角括号抱着日文注解
│                    #      （`…character-sheet（手と前掛け。顔は映さない）`），而 §6 只用名字的部分
│                    #      （10/10）。⚠️ 要拆开就意味着写入 `projects/`，而本仓库中没有任何
│                    #      工具这么做。
├── engine/assembly/ # 时间线、剪辑、文字合成、渲染
├── providers/       # 图像、视频、合成的生成器
└── interchange/     # OTIO / EDL / FCPXML
```

⚠️ **`skills/` 里缺着 2 段**——**⑥构成与⑦验收。**
写不出来。**因为输入不在记录那一侧。** `clips[]` 按定义是**采用镜次的列**，
而**视频镜次里一张 `adopted: true` 都没有。**
不是难写——⚠️ **是动不了**，而
⚠️ **吐出一条空时间线的 Skill，比没有 Skill 更糟。** 洞写在它发生的地方——
[`projects/hitosara/renders/README.md`](projects/hitosara/renders/README-zh.md)。

⚠️ **不要把它们作为「预定」留在这里。** 它们不是在等作业——
**是在等被采用的镜次，而采用是作者的行为。**
排成预定，**看起来就像等一等它们自己会来。**

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

### 为 `habits-ch01-seg01` 跑 ②——⚠️ **等正文写出来之后**

这条镜头记录没有 `spec:`，而**它正是 `python3 engine/ledger/check.py projects/habits` 报告的唯一违规。**
**这不是事故，而是被声明的状态**——最小形（方针 §7）只切 `bible.yaml` ＋ `ledger.yaml` ＋ `shots/`，
**不切 `specs/`。****第一卷一次也没有跑过 ②，因为它的正文还不存在。**
⚠️ **等那一话的正文写出来再跑 ②——并在同一轮裁定 `duration`。** 这条记录里的 `8s` 是
**「发明（待承认）」**，先跑 ② 就会把**未经承认的推测固定进 §1，此后 `L23` 会把它称作「一致」。**

## 语言

**开发用日语推进，文档的正典是英语。**
镜像用后缀方式并排在**同一个目录**里——规则在 [`CLAUDE.md`](CLAUDE-zh.md) 里。

**20 份文档 × 3 种语言已经齐备**——⚠️ **这是 [`tools/check_i18n.py`](tools/check_i18n.py)
作为正典报告的本数，不是把仓库里的 `.md` 数了一遍的数。**
**数，只拥有它所数范围那么宽。**
**它看什么、不看什么**，写在 [`docs/usage.md`](docs/usage-zh.md) 里。

## 许可证

MIT
