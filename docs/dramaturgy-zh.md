<!-- i18n-version: 1.0.0 | canonical: docs/dramaturgy.md | translated: 2026-10-29 -->

**Language:** [English](dramaturgy.md) | [日本語](dramaturgy-ja.md) | [中文](dramaturgy-zh.md)

# 剧作——台帐的第三种登录簿

**制作台帐持有「什么是真的」。** 连续性持有**世界的状态**，揭示持有**观众知识的状态**。
两者回答的都是 *什么是事实*。

⚠️ **两者都不回答：那个变化值多少。** 一个镜头可以精确地完成它的 `unit`，
仍然是一个没人记得的镜头。**剧作是第三种登录簿，是作品决定这件事的地方。**

**它不是第五阶段。** 它是同一个 `ledger.yaml` 里的登录簿——**台帐不分割**
（[`CLAUDE.md`](../CLAUDE-zh.md) 的 Fixed Policy）。连续性、揭示与剧作是**对同一个文件提出的三个问题**，
参照集合与禁制集合仍然从这一点导出。

## 为什么它在台帐里，而不是在旁边

「台帐只有一个」这条规则，来自一次真实的失败：**「哪张参照图配哪个镜头」**——
那个问题同时是连续性和揭示，两者分开就答不出来。

**剧作提出的是同一种问题。** 「这个镜头旁边有没有接地镜头」既是关于**世界**的问题（连续性），
是关于**观众被允许看见什么**的问题（揭示），也是关于**装置是为了什么**的问题（剧作）。
把第三样放进自己的文件，三个答案就会各自内部正确，而彼此错开。

## 它持有什么

```yaml
dramaturgy:
  version: 1
  premise: "…"          # 发生了什么，一行
  question: "…"         # 观众带到最后的那个问题
  argument: "…"         # 作品说的话——一句有人可以反对的话
  visual_thesis: "…"    # 用光、色与构图说的同一句话
  value_poles:
    - ja: 安全
      en: safety
    - ja: 危険
      en: danger
  acts:
    - id: act-1
      shots: [s01, s02, s03, s04]
      turn: "…"          # 这一幕的同一个变化
      climax: s03
      value_from: 安全
      value_to: 危険
      rhythm: "蓄 → 爆 → 余韵"
  sequences:
    - id: seq-1
      shots: [s01, s02, s03]
      contrast: "静 → 动"
      escalation: "…"
      transition: "…"
      payoff: s09
      flat: false
  motifs:
    - id: light
      first: s01
      recurrences: [s04, s07]
      payoff: s12
  set_pieces:
    - shot: s07
      format: impossible-camera   # 必须与镜头的 §6 REF_FORMAT 一致
      why: "…"
  sound_arc:
    silence: [s01, s02]
    score_enters: s03
    note: "…"
  ending_image: "…"    # 最后留下的一张
```

⚠️ **`acts` 与 `sequences` 是叠在镜头上的眺望，不是生成单位。** **镜头仍是单位。**
一个镜头仍然是一个变化；幕是读那四个镜头的一种方式。

⚠️ **`payoff` 可以指向前方。** 预约的回收不是状态——与连续性台帐里的 `… yet` 同一条纪律。
`L41` 只看目标是否存在。

⚠️ **没有 `note` 的 `flat: true` 不是宣言。** 紧张曲线故意平直的序列要**说明为什么**；
`L44` 会在光秃秃的旗子上响。

⚠️ **`value_poles` 是作品自己的映照**（`{ja, en}`）。记录写日文，`DIRECTION` 带英文。
⚠️ **`en` 必须是字面出现在那一节里的词**——`L43` 找它，不追词形变化，也不追同义词。
**没有对偶的价值是设定，不是赌注。**

## 镜头的戏剧记录

```yaml
# shots/<id>.yaml
dramatic:
  function: 転換              # 设定/上升/转折/发现/决断/结果/蓄/释放/余韵
                              # 或非叙事的 质感/留白/样式美
  value:
    from: 安全
    to: 危険
    stake: "父の記憶"
  audience:
    feel: "息を止める"
    expect: "彼が扉を開ける"
    know: "母がまだ生きている"
  button: "閉じた扉の向こうの光"
  performance:
    objective: "娘を守る"
    obstacle: "扉が開かない"
    tactic: "体で押す"
    subtext: "許しを請う"
    intensity: 8
```

⚠️ **`value` 是镜头那一个变化的值，不是第二个变化。** `unit` 说变了什么，`value` 说它付出了什么。
**同一个变化的两种读法**——需要第二个价值转折的镜头，是两个镜头。

⚠️ **非叙事的职能**（质感・留白・样式美）**不需要价值转折**——但仍然需要 `button`，
**因为每个镜头都以一张画面结束。**

⚠️ **`function` 与 `role` 是不同的轴。** `role` 是那个镜头的工作（`L15` 读它）；
`function` 是这个镜头发生时故事在哪里（`L40` 读它）。两者的词汇重叠（转折、留白、样式美）
——⚠️ **不要从一个推出另一个。**

⚠️ **`audience.know` 不是 `disclosure_state`。** 后者是关于世界的事实，前者是观众此刻持有的东西。
**没有任何层比较两者**——观众是否走在人物前面是判断，而会去猜它的层，等于在写故事。

⚠️ **人物在场且 `mode: motion` 的镜头期待 `performance`**，而它的缺席是**注，不是违规**
——有些镜头里根本没有人。⚠️ **`objective == obstacle` 会让 `L47` 鸣响**：
被自己的障碍复述了一遍的愿望，是说明，不是愿望。

⚠️ **放在 §17 与 §18 之间，是一个关于次序的主张。** §18 是七个槽位的对应表，
而调度必须在它之前定下来——**先写完槽位再补上调度，等于事后给它安一个理由。**
⚠️ **编号不动。** 既有的规格继续使用 §18–20 的编号，
所以这个节不带号，也不会推倒任何一份已经写好的规格。
**带号的话，一百多份规格会一起变红。**
⚠️ **它也不必长。** 长度不是目的；**一句能让生成器照着演的话**就够了。
不要为了填满而写第二段——**第二段是从第一段里掉出来的东西。**

## `DIRECTION` 节

规格可以在 §17 与 §18 之间，带**一个**不带编号的节：

```text
DIRECTION  ← ledger.dramaturgy + shot.dramatic + §12 EMOTION
  Play {FUNCTION} for {AUDIENCE_FEEL}. The value turns from {VALUE_FROM} to
  {VALUE_TO}; the stake is {STAKE}. Use {DEVICE} only to {DEVICE_WHY};
  keep {INVARIANT}. End on {BUTTON}.
```

⚠️ **它不是槽位。** `PROMPT_SLOTS` 仍是七个，`L17`・`L28`・`L30` 不变。
**生成时它的正文被接到 `Master Prompt` 的开头**——在规格里是一个独立的节，
在生成器那里是 Master 的第一段。

⚠️ **这是感情第一次有路可走，抵达生成器。** §12 EMOTION 是一个**不喂任何槽位**的规格节
（`specmap.PROMPT_SLOT_SOURCE`）——在此之前，镜头的感情被写下来，然后被归档。

⚠️ **它不是调度散文的抄本。** 调度摘要**是写给读的**，并且明确写着它不是来源
（[`skills/design/SKILL.md`](../skills/design/SKILL-zh.md)）。`DIRECTION` 是从台帐、镜头记录与 §12
**写出来的**——**不是从日文记录翻译过来的。** 英文是型，不是描摹。

## 序列约束着什么

`contrast`、`escalation`、`transition` 描述一个序列。**另有三栏约束它**，
而这三栏每一栏都能与镜头对照——它们是戏剧构造中以画面为单位、
而不是以纸面为单位的第一部分。

```yaml
sequences:
  - id: seq-2
    shots: [s04, s05]
    withheld:
      - shot: s04
        wanted: "the flame entering the lantern — the audience is waiting for it"
        given: "it does not light. The flame is never in this film."
    cuts: [s05]
    tempo: [9, 9]
```

⚠️ **`withheld` 是「观众想要、却没有得到」的位置。** `wanted` 与 `given` 必须不同，
两者都不能为空——**给出你承诺过的东西是拖延，不是欠缺；**
**什么也不给是事故，不是选择。** `L48` 读它。
**作品最后一个镜头上的欠缺是注记，不是违规**——不展示可以就是结局。

⚠️ **`cuts` 是一个镜头不能独自决定的切口。**
切口的含义只在紧邻的镜头旁才成立——所以**由序列声明**，
由镜头记录持有 `cut: internal`。`L49` 双向检查，
**并且打开规格的正文**：只改记录而不改散文，
从不读记录的生成器仍会做出一镜到底。

⚠️ **`tempo` 是用秒写下的序列形状；正本是镜头的 `duration`。**
`L50` 只对照这份副本。**三个以上相同的值会鸣响**——除非序列声明了 `flat: true` 与
`note`。**平缓的律动可以是设计**，
它的平缓也可以是让下一次变化生效的陷阱。

⚠️ **这三栏不会让序列变好。** 作品知道观众想要什么，然后决定
在哪里不给——**那是它们的席位。**

## 检查读什么，不读什么

| 层 | 读什么 | 什么时候响 |
|---|---|---|
| `L40` | `dramatic.function` / `value` | 叙事的职能，而 `value.from == value.to` |
| `L41` | `dramaturgy.acts` / `sequences` | 没有 `turn` 的幕；没有 `contrast` 的序列；不存在的 `payoff` 或 `shots` 项 |
| `L43` | `DIRECTION` 节、`dramatic`、`value_poles` | 带 `dramatic` 的镜头没有节；英文职能缺失；价值的英文缺失 |
| `L44` | `beats[].intensity` | 相同的强度连续三个以上镜头；幕里没有峰值 |
| `L47` | `performance.objective` / `obstacle` | 两者相同 |
| `L48` | `sequences[].withheld` | `wanted` 与 `given` 相同，或其中之一为空 |
| `L49` | `sequences[].cuts`、`cut: internal`、规格正文 | 只有一侧的声明。仍写着一镜到底的规格 |
| `L50` | `sequences[].tempo` 与镜头的 `duration` | 秒数不一致。没有 `flat: true` 与 `note` 的等间隔 |

**没有一个读那个转折好不好。** 曲线可以平直，价值可以琐碎，幕可以任意，而每一层都通过
——**这就是设计。** 质量属于[评议会](../skills/review/SKILL-zh.md)和作者。

## ⚠️ 记录是自选的；缺席不是分歧

**这里的每一个栏位都是可选的。** 没有 `dramaturgy` 也没有 `dramatic` 的作品照样通过，
它的注释会写出看了多少个镜头。

⚠️ **不要回溯补写。** 事后写下的 `function` 不是职能，是说明——与 `aim` 同一条纪律。
⚠️ **在这个登录簿之前做成的作品，并没有因为它而做错。**

**开关是记录，不是版本。** 没有 `format-version:` 这个栏位，也没有任何东西读它；
带 `dramatic` 的镜头进入 `L40`/`L43`/`L47` 的范围，不带的就不进入。
**引擎不记得哪些作品是特别的。**

## 读不到的东西

- **premise、argument、ending image 好不好。** 这是散文，是作者的判断。
- **`set_pieces[].why`。** `L42` 只比见场的 `format` 与 §6，别的什么都不比。
- **`sound_arc`。** 没有任何层打开它——它是一个决定，不是一个有读者的栏位。
- **`motifs[].recurrences`。** 列出来是让作者看见形状；没有任何东西去解决它们。
- ⚠️ **观众有没有感觉到什么。** 生成发生在本仓库之外，**这个登录簿从不说它测量过。**

## 再往哪里读

- [`skills/direction/SKILL.md`](../skills/direction/SKILL-zh.md) ——写这个登录簿的那一段
- [`skills/design/SKILL.md`](../skills/design/SKILL-zh.md) ——写 `DIRECTION` 的那一步
- [`skills/review/SKILL.md`](../skills/review/SKILL-zh.md) ——裁它的评议会，以及怎么裁
- [`schemas/ledger.schema.json`](../schemas/ledger.schema.json) ——`dramaturgy` 的形
- [`schemas/shot-record.schema.json`](../schemas/shot-record.schema.json) ——`dramatic` 的形
- [`references/formats/video-spec.md`](../references/formats/video-spec-zh.md) ——§12 EMOTION 与 `DIRECTION` 节
- [`docs/cards.md`](cards-zh.md) ——形式卡片。它就是装置
