<!-- i18n-version: 1.0.0 | canonical: engine/shot/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# engine/shot/ — 打印规格的骨架

**打印一个镜头规格中可以导出的行**——从记录、台账与作品台账中。**一个字节也不写。**
不写入 `projects/`，不写入规格，哪里都不写。

```bash
python3 engine/shot/print_spec.py projects/<project>              # 全部镜头
python3 engine/shot/print_spec.py projects/<project> --shot <id>  # 只打印一个
```

⚠️ **把打印出来的行贴上去，是作者的行为。** 这个工具只显示被强制的东西。

## 它打印什么

**6 行**——对照一个规格中（除去空行）的 **166** 行（`hitosara-ch01-seg04`）。

| 行 | 来源 | 照抄它会让谁沉默 |
| --- | --- | --- |
| §1 `Aspect` | `bible.constants.video.aspect` | `L26` |
| §1 `Resolution` | `bible.constants.video.resolution` | `L26` |
| §1 `Frame Rate` | `bible.constants.video.frame_rate` | `L26` |
| §1 `Orientation` | `bible.constants.video.orientation` | `L26` |
| §1 `Duration` | `shot.duration` | `L23` |
| §19 `Instance ID` | `shot.shot` | `L13` |

⚠️ **这个工具的价值不在于把行填上。** 而在于**逐行点名：你手抄这一行，会让哪一个
检查沉默。** 手抄的行，**即使抄写的来源变了，也没有人会长鸣**——`L23`、`L26`、`L13`
之所以存在，正是因为**恰恰对这些行，它会长鸣。**

⚠️ **规格并不是由这 6 行拼装而成的。** 这里是**机器已经知道答案**的部分。其余才是工作。

## ⚠️ 它不导出的东西

**§2 WORLD、§3–§5、§7–§13、§14 DIALOGUE、§15–§17、§18（七个槽位）、§20**——这些由作者
书写。`print_spec.py` **每次运行都会报出这份清单**——因为**数字的宽度，只等于它所数过的
范围。**

### §6 REFERENCES —— 形状不稳定

⚠️ **这是实测，不是假设。** 两部结构化作品写法各不相同。

| | `projects/hitosara` | `projects/ukebi/ukebi-v2` |
| --- | --- | --- |
| 语法 | ``- REF_KEY: `value` (HIGH)`` | ``- `REF_KEY` — `value` · `HIGH`。`` |
| 键 | 6 个：CHARACTER / LOCATION / GEOGRAPHY / STYLE / FORMAT / SOURCE | 5 个：CHARACTER / STYLE / FORMAT / SOURCE / BIBLE |
| 值的词汇 | 卡片名（`luminous-anime`） | 路径（`references/styles/soft-cel-anime.md`） |

⚠️ **形状不稳定的字段无法导出。** 一旦导出，这个工具就会**每部作品撒一次谎**——对同一
行、以同一格式，在两部作品中都打印出一个**自信的错误值**。所以 §6 不予解析。这些洞
记录在下面。

⚠️ **例外是两个键——`REF_STYLE`（`L31`）和 `REF_FORMAT`（`L32`）。**

**`REF_STYLE` 由 `L31`（`check_style_reference`）读取。读它不会变成猜测**
——上面的三种拼写由**一个正则表达式**接收，**两种词汇（卡片名、路径）在比较之前被归并成
一个名字**（取末尾一段，去掉 `.md`）。⚠️ **因此 `L31` 并不判定哪种词汇正确**——**它只是让
两者可以互比**，然后把结果与**家（`bible.style`）**对照。

**`REF_FORMAT` 由 `L32`（`check_format_reference`）读取，为的是抵达卡片本身。**
`L31` 把命名与家对照，而 **`L32` 问的是「被点名的卡片能否读到」「它是否声明了 `## Negative`」**
——因为 `Negative Prompt` 被规定为 `§16 ＋ 本卡片的 Negative ＋ 样式卡片的 Negative`
（`specmap.PROMPT_SLOT_SOURCE`），**而此前没有任何东西读过那张卡片的 `Negative`。**
⚠️ **`L32` 不与家对照——`REF_FORMAT` 没有家**（见 [`docs/cards-zh.md`](../../docs/cards-zh.md)）。

⚠️ **其他键仍然不读**——上面的规则对它们照旧成立。

## 作品常数的家

`bible.constants.video`——`aspect` / `resolution` / `frame_rate` / `orientation`。

⚠️ **`duration` 不在那里。** 时长是**因变量**：它的家是 `shot.duration`，它的读者是
`L23`。把它放在这里，就意味着**两个层用不同的符号报告同一个缺陷。**

⚠️ **这不是新增的字段。**
`projects/ukebi/ukebi-video-00-series/series-constants.md` 曾**手工**持有 §1 的常数
**全部 12 条**，而 `schemas/bible.schema.json` 指明 `bible` 是它的继承者。
**家本来就在那里——只是没有人在读。**

⚠️ **作品常数曾被手抄到三处**：§1、§19 的 `Output:` 行，以及（在受け火中）
`series-constants.md`。而这些抄本**已经开始漂移。**

## 谁在读它

- **`L26`** —— 把 `bible.constants.video` 与 §1 的四行对照
- **`engine/shot/print_spec.py`** —— 这个工具

⚠️ **`L26` 今天一条也不响**——**160** 次比较（两部结构化作品、40 个规格 × 4 个字段），
**0** 处不一致——它的注也这么说。⚠️ **不响，与不必要，不是一回事。** 它所守的故障
**已经存在于本仓库中**（§19 的 `Output:` 行在 10/10 中拼写不同），而 `L23` 同样是在
**40/40** 一致的情况下被保留的。

## 它什么都不决定

⚠️ **这个工具什么都不写，也什么都不决定。** 当导出值与磁盘上的规格不一致时，它把
**两者并列**出来，然后停下。**哪一个正确，是作者的判断**——与 `L25` 的立场相同。

## 仍然缺失的东西

**记录，而不是修复**——这是本仓库的做法。

1. **§19 的 `Output:` 是第三份手抄本。** 它在 **10/10** 个规格中拼写不同
   （`1920×1080` / `landscape` 对 §1 的 `1920x1080` / `Landscape`）。值一致，拼写不一致。
   **所以 `L26` 不读它**——读它会产出 **10 个假阳性**。是归一化后读取、拆成四个字段，
   还是保留为散文，**尚未决定。**
2. **§19 `Instance ID` 中的 `<seconds>` 没有人在看。** `L13` 在比较前会剥掉末尾的
   `-<seconds>s-<take>`，所以**抄进标识符里的时长，没有被拿去与任何东西比较。**
3. **`bible.constants` 的四条散文常数没有人在读**（`根本律`、`光源`、`カメラ`、
   `様式変数`）。如何使其机器可读，**尚未决定。**
4. **§6 的 `REF_CHARACTER` 无法导出。** §6 在 **9/10** 个镜头中引用它，而
   `reference_set` 只有 **4/10** 携带 `BAKER.sheet`——**两侧对「人物被挂上了」的含义
   意见不一。**
5. **seg04 的 `REF_LOCATION` 覆盖没有任何地方记录。** 五个 `KITCHEN/朝` 镜头携带
   **相同的位置引用**（`KITCHEN.base` + `KITCHEN.geography`），而 §6 在其中四个引用
   `-morning` 板，在 seg04 引用裸的 `hitosara-kitchen-board`。从 `(place, time)` 导出
   得到 **9/10**，而**第十个与记录无法区分。** ⚠️ 这是本文档中最确凿的洞：
   **这个选择只存在于 §6 自身之中。**
6. **seg10 的 §6 引用了 `hitosara-kitchen-geography`**，而它的 `reference_set` 一个
   地理都没有声明（`TABLE.base`）——§6 说「LOW: 房间只是暗示」。**§6 的地理引用在
   `reference_set` 中没有对应物的镜头，只有这一条。**
7. **`locations.KITCHEN.states.朝.board` 没有被任何镜头的 `reference_set` 引用**，
   而 §6 在 **4** 个镜头中使用了它的值。（`昼` 由 seg06 引用，`明け方` 由 seg07/08 引用，
   `MILL.朝` 由 seg01 引用——只有 `KITCHEN.朝` 无人引用。）

⚠️ **第 4–7 项不是作品的缺陷。** 它们是**记录不知道规格在做什么**的地方。若要修，
应当是**给这个选择一个家**——**而不是让工具去猜。**
