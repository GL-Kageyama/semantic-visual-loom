<!-- i18n-version: 1.2.0 | canonical: docs/cards.md | translated: 2026-10-29 -->

**Language:** [English](cards.md) | [日本語](cards-ja.md) | [中文](cards-zh.md)

# 卡片——Format 与 Style

**提示词由两个轴搭成，而两个轴都是卡片。** **Format（形式）**是规格的形状，
**Style（样式）**是在那个形状里画出的视觉语言。**两者都不是本仓库里的一份清单**——
**各自是一个 Markdown 卡片的目录**，**卡片在跑的时候，按名字被读出来。**

⚠️ **它们是两个层，不是同一个东西的两种看法。** 一个层的卡片顶不上另一个层的卡片——
而且**一个作品可以只拿其中一个**。`L22` 就是在那个缺陷之后写下的。

## 卡片住在哪里

**默认住在仓库的旁边**——在 `distill-essence-engine` 里：

```text
distill-essence-engine/references/formats/   # the format cards
distill-essence-engine/references/styles/    # the style cards
```

⚠️ **那个目录不是本仓库的一部分**，所以**刚 clone 下来的人手上没有它。**
打不开卡片的检查**会说出来**，而不是当作通过——**「没能确认」不是「确认了」。**

**这一侧的作品要拿自己的卡片时，就放在本仓库里，用同一个两层的形状：**

```text
references/formats/    # this side's format cards — `video-spec`
references/styles/     # this side's style cards — `sumi-e`
references/grammars/   # the registry — `index.yaml`
```

⚠️ **目录不是第三个层。** 它自己一张卡片也不持——**只是把属于文法的形式卡片列出来。**
而**把它放在这里、而不是在跑的时候推出来**，是为了让**镜头所用的名字，只有一处可以登记。**

⚠️ **两个目录是同一个东西从两侧看过去的样子**——`_cards_dirs()` **每个层找一份清单**，
而**决定那份清单顺序的，是环境变量。**

## 一共有多少张卡片

**数于 2026-10-29。** 数的范围是 `_cards_dirs()` 会去搜的两个目录，数的办法是
**数每个目录里的 `.md`，把镜像搁在一边**——`video-spec-ja.md` 与 `video-spec-zh.md`
是 `video-spec.md` 的译文，不是它们自己的卡片，所以这三份是一张。

| 目录 | 形式的卡片 | 样式的卡片 |
|---|---|---|
| `references/`——**本仓库自己的** | **16** | **16** |
| `distill-essence-engine/references/`——旁边那个，在它存在的时候 | 45 | 55 |

**这 16 和 16 是什么。**

- **16 张形式卡片** = `video-spec` **＋ 十五个文法**：`transformation`、`time-fold`、
  `remembered-world`、`impossible-camera`、`meaning-responsive`、`recognizing-world`、
  `coexisting-realities`，以及暂置的八张——`recursive-frame`、`scale-rupture`、
  `material-substitution`、`population-emergence`、`temporal-panorama`、`light-as-actor`、
  `frame-escape`、`physics-with-a-rule`。**哪一张是文法、哪一张是别的种类的卡片，
  由「`video-spec` 加一条规则」这件事决定**——而记录那条规则的，是下面的目录。
- **16 张样式卡片** = `sumi-e` **＋ 从图像侧搬过来的十四张**（`watercolor`、`mokuhanga`、
  `oil-painting`、`gouache-abstract`、`cinematic-still`、`documentary-photo`、`instant-photo`、
  `landscape-photo`、`macro-photo`、`street-photo`、`studio-portrait`、`sketch-broadstroke`、
  `blueprint-plan`、`lab-notebook`）**＋ `impossible-medium`，这里是唯一一张没有图像侧原盘的
  卡片。**

⚠️ **这 32 张里，有镜像的只有一张。** 只有 `video-spec-ja.md` 与 `video-spec-zh.md` 这一对，
所以**31 张是没有译文的英语正典**——而
[`tools/check_i18n.py`](../tools/check_i18n.py) 不把它们算进自己的文档里：**它数的是交给
读者的文档，而这些是跑的时候被打开的卡片。**

## 文法目录

`references/grammars/index.yaml` **是文法的清单，也是检查所读的清单。**
文法卡片是写给人的散文，**目录是同样的事实，换成检查能打开的形。**

```text
- name: transformation            # the name §6 REF_FORMAT uses
  card: transformation            # references/formats/<card>.md
  status: established             # established | provisional
  routes: [WAN 3.0, MINIMAX H3, SEEDANCE 2.5]
  written_into: ["9. ACTION", "11. MOTION"]
  essential_moves: [ … ]          # what the grammar does, in one line each
  negative_conflicts: ["no deforming silhouette"]   # clauses that would forbid the move
  grounding: …                    # the ordinary shot this grammar is measured against
  failure: …                      # the defect it is most often confused with
```

⚠️ **`status` 说的是「这份清单是不是正典」，不是卡片好不好。**
七张 `established` 是本仓库本来就持有的卡片。**八张 `provisional` 占着作者自己的清单
将要替换的席位**——所以**暂置的条目不许当作正典引用。**

⚠️ **`routes` 是宣言，不是实测。** 唯一有实测理由的是 `coexisting-realities`，
它的卡片自己写着「一条连续的镜头抱不住两个地方」——**所以 `WAN 3.0` 只在那里被排除，
别处都不。** 卡片没有写出理由时，**不扩也不缩 `routes`。**

⚠️ **`written_into` 用 `specmap.SPEC_SECTIONS` 的节名书写**（`"9. ACTION"`），
所以目录与规格共用一个拼写。**卡片把同一份清单写成 `§9 ACTION`**——
两个拼写，两个读者，一份清单。

⚠️ **`negative_conflicts` 里只放已经立在某张卡片 `## Negative` 里的句子。**
**不往地板里加东西**——它只名指：作品若把它抄进 §18，**就会禁掉那个文法核心的句子。**
**空的清单是「这里不禁它」，不是「照合过、没问题」。**

⚠️ **旁边的 45 和 55 也是同一条规则，按那个目录今天的样子数出来的。**
它们是**图像侧的库存，不是本仓库的东西**——所以**这边什么都不变，那两个数也可能动。**

## 环境变量

| 层 | 变量 | |
|---|---|---|
| format | `SVL_FORMATS_DIR` | 形式的卡片在哪里 |
| style | `SVL_STYLES_DIR` | 样式的卡片在哪里 |
| registry | `SVL_GRAMMARS_DIR` | `index.yaml` 在哪里——**叠加，从不替换**：本仓库自己的 `references/grammars/` 依旧读得到 |

⚠️ **每个层读自己的变量。** 指向样式的目录，**并不会挪动形式的层**——**反过来也一样。**
*没被读到的名号，不能长得跟被读到的一样。*

⚠️ **变量是叠加，不是替换。** 它指到的目录**先**被搜，**仓库旁边的默认目录在它之后**被搜——
所以**作品多放一张卡片，不会让引擎的卡片变得读不到。** *这一点要紧，是因为作品名号的卡片
只有一个名字，而替换会赔掉其余每一张卡片。*

⚠️ **指向一个不存在的目录不是错误**——**那个目录被跳过，默认照样生效。**
*一个指错的路径，不能悄悄变成「没有卡片」。*

⚠️ **相对路径按工作目录来解**，所以从本仓库的根跑：

```bash
SVL_FORMATS_DIR=references/formats SVL_STYLES_DIR=references/styles \
  python3 engine/ledger/check.py projects/ippitsu
```

⚠️ **不设变量，本仓库里的卡片就不会被读**——而且**规格名号了一张谁也打不开的卡片，
会触发违规。** 所以**带视频规格的作品必须设这个变量**，否则它放在自己旁边的卡片，
在检查器眼里是不存在的。

## 规格怎么名号一张卡片

**视频规格的 §6 `REFERENCES` 名号它引用的卡片：**

```text
- `REF_FORMAT`: `video-spec`
- `REF_STYLE`: `luminous-anime`
```

**第一行指出这份规格建在哪张形式卡片上，第二行指出它用哪张样式卡片来画。**
⚠️ **两者都不是规格的某一节**——**名字住在 §6，而卡片是另一个文件。**

名字可以是**卡片名**，也可以是**路径**——**在拿来跟任何东西比之前，两者都先折成一个名字**
（取路径最后一段，去掉 `.md`）。⚠️ **哪一套词汇才对，这里不做判断**；
层只是让两者可比。

⚠️ **`bible.style` 是作品里样式的家，而 `REF_FORMAT` 没有这样一个栏位。**
这是有意的——**两条路径名号的格式并不一样**：视频的路径名号一张视频规格卡片，
图像的路径名号一张图像的卡片——所以**一个只写一个名字的栏位，必然对其中一条路径说谎。**

## 卡片声明什么

| 节 | format | style | |
|---|---|---|---|
| `## Environment variables` | 必需 | 必需 | 卡片填的洞。**规格自称的卡片的并集，就是该规格应当持有的字段**（对方按作品而定） |
| `## Negative` | 必需 | 必需 | 这张卡片追加的排除 |
| `## Motion character` | —— | 可选 | 这种样式动起来的时候做什么 |

⚠️ **唯一可选的是 `## Motion character`。** 一张既填栏位、**又**参与
`Negative Prompt` 的卡片，**必须把另外两节都声明出来。**

## 哪个检查读什么

| 检查 | 读的东西 | 什么情况下响 |
|---|---|---|
| `L20` | 样式卡片的 `## Motion character` | 名号的那种样式没有这一节——**于是 `Style Motion` 存在，却什么也没装** |
| `L22` | **图像**规格，两个层 | 没有任何卡片声明过的洞；带着规格不填的洞的卡片；打不开的卡片，或没有 `## Environment variables` 的卡片 |
| `L31` | §6 名号的样式卡片 ⇄ `bible.style` | 家与规格名号的是不同的样式 |
| `L32` | §6 名号的形式卡片 | 名号的卡片打不开，或没声明 `## Negative` |
| `L42` | §6 `REF_FORMAT`、文法目录、`dramaturgy.set_pieces` | 名号的文法不在目录里；它声明 `written_into` 的节不存在或为空；§18 名号了不在它 `routes` 里的路径；见场（set piece）的 `format` 与 §6 的名不同 |
| `L45` | 目录的 `negative_conflicts` 与 §18 `Negative Prompt` | 规格名号了文法，而它自己的 `Negative Prompt` 禁掉了那个文法的核心动作 |
| `L46` | `aim` 的 `grammar: <name>` 前缀与目录 | `aim` 名号了目录里没有的文法 |

⚠️ **`L31`、`L32`、`L42`、`L45`、`L46` 相邻是有意的**——**它们读同一个 §6 和同一个目录，
只差一个键。** 分开摆，就会修了一个、忘了其余。

⚠️ **`L42` 与 `L46` 在一个一个文法都不名号的作品上，天生是安静的。**
`video-spec` 的规格没有要登记的文法；不以 `grammar:` 开头的 `aim` 是自由散文，照过。
**什么都不名号的作品，不是一个失败了的作品**——注释会写出「看了几本」，
所以**沉默留得下来，是能读的。**

⚠️ **`L20` 与 `L32` 报的是三种结果，不是两种**——**没有卡片的存放处是注；卡片不存在是违规；
卡片缺那一节也是违规。** *目录不在和卡片不在是两种原因，用同一张脸报出来，
读的人就分不清该修哪一个。*

⚠️ **所以在没有旁边那个引擎的 clone 上，`L20` 与 `L32` 报的是注，不是违规。**
**同一段代码，放在不同的环境里给出不同的符号**——这是对「本仓库不持有卡片」的诚实读法，
不是缺陷。

## 读不到的东西

**⚠️ 这份清单要当作洞来读，不要当作待办来读。**

- **§6 剩下的键**（`REF_CHARACTER` / `REF_SOURCE` / `REF_BIBLE`）。**没有任何检查读它们**——
  `L31` 读 `REF_STYLE`，`L32` 读 `REF_FORMAT`，其余没有。
- **样式卡片的 `## Negative`。** `PROMPT_SLOT_SOURCE` 把 `Negative Prompt` 定义成
  「§16 ＋ **这张卡片的 Negative** ＋ 样式卡片的 Negative」，而
  **那两个卡片项里被读到的只有第一个**（`L32`）。
- **卡片的内容对不对。** 看的是**那一节在不在**，以及
  **声明的洞是不是规格填的那些洞**——**卡片里的字对输出做了什么，从这里看不见。**
- **卡片里除 `## Environment variables` 与 `## Negative` 之外的每一节。** 形式卡片声明
  它填的洞和它追加的排除——**它说的别的都是说给读者听的。**
  ⚠️ **这正是 `L22` 不能扩到视频路径的原因**——视频规格用 §1–20，
  一个洞也不填视频形式卡片声明的那些洞，所以**检查会在每一份正确的规格上响。**
- **文法卡片的 `## Written into` 散文。** 检查读的是目录的 `written_into`，
  不是卡片里的清单——**卡片写 `§9 ACTION`，目录写 `"9. ACTION"`，
  而检查器只打开目录。** 两份清单由 `L42` 的覆盖注释对齐：
  **磁盘上有、目录里没有的卡片，那里会名指出来。**
- **目录的 `essential_moves`、`grounding`、`failure`。** 这些是文法的意义，
  **没有任何检查拿它们与规格比。** `L45` 只读 `negative_conflicts`——
  **装置是否按卡片说的那样在动，从这里读不到。**
- **`dramaturgy.set_pieces[].why`。** `L42` 比的只是见场的 `format` 与 §6，
  **见场值不值得放在那里，是作者的判断。**
- **分镜纸。** 镜头记录没有任何栏位指向 `specs/board/`，所以**没有检查会打开它**
  （[`docs/usage.md`](usage-zh.md)）。

## 再往哪里读

- [`engine/ledger/README.md`](../engine/ledger/README-zh.md) ——每一个层，读什么，
  以及不读什么。
- [`engine/shot/README.md`](../engine/shot/README-zh.md) ——§6，以及它那没定下来的形状。
- [`references/formats/video-spec.md`](../references/formats/video-spec-zh.md) ——
  本仓库持有的那张形式卡片。
