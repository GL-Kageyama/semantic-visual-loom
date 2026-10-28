---
name: direction
description: '作品的剧作——①中决定作品主张什么、价值如何转逆、幕与序列在哪里断开、每个镜头为何存在的部分。它写台帐的第三本登记簿与每个镜头的剧作记录；不写规格。在 breakdown 之后、design 之前运行。⚠️ 不是第五阶段。'
argument-hint: '(可选) 作品名，或要执导的序列。例: /semantic-visual-loom:direction drama-pilot'
---

<!-- i18n-version: 1.0.0 | canonical: skills/direction/SKILL.md | translated: 2026-10-29 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# direction — ① 作品的剧作

**①说了什么在变。②决定镜头。本文档是①中决定这些变化为何存在的部分。**

⚠️ **不是第五阶段。** 它在①中运行：`breakdown` 产出镜头表之后，`design` 写规格之前——与 `staging` 在②中运行是同一形态。它写的是台帐的第三本登记簿与镜头记录的 `dramatic` 字段。**它不写 §18 的槽位，也不写规格。**

## ⚠️ 为什么需要它——台帐只有两本登记簿

制作台帐持有**连续性**（世界的状态）与**开示**（观众的知识状态）。两者都关于**什么是真的**。它们都不关于**观众感受到什么、预期什么、带走什么**。

因此戏剧性是偶然的：它取决于 §18 的散文是否恰好写得好。`aim` 记录了镜头尝试什么，却没有任何检查读取它。`take.verdict.council` 有一个席位，却没有人坐。作品层面没有任何东西决定幕的转逆、序列的对比、母题在哪里回收。

⚠️ **失败不是「提示词写得差」。** 而是**作品从未决定自己的变化值什么**。一个镜头可以完美执行 `unit`，却仍然是一个没人记得的镜头。

## 这个阶段拥有什么

| | 什么 | 哪里 |
|---|---|---|
| **treatment** | premise · question · argument · visual thesis · value poles · ending image | `ledger.yaml` → `dramaturgy` |
| **幕** | 各幕的 `turn` · `climax` · `value_from` / `value_to` · `rhythm` | 同上 |
| **序列** | `contrast` · `escalation` · `transition` · `payoff` · `flat` · `withheld` · `cuts` · `tempo` | 同上 |
| **母题** | 初现、复现、回收 | 同上 |
| **场面** | 哪个镜头使用哪张格式卡，为什么 | 同上 |
| **声音之弧** | 沉默、音乐进入处、画内音 | 同上 |
| **每个镜头的剧作记录** | `function` · `value` · `audience` · `button` | `shots/<id>.yaml` → `dramatic` |

**不拥有**：镜头表（**`breakdown`**）、规格与 `DIRECTION` 节（**`design`**）、take 与评语（**`shot`**）。⚠️ **也不拥有采用**——那是作者的行为。

⚠️ **镜头仍是单位。** 幕与序列是**覆在镜头之上的视图**，不是生成单位。一个镜头仍然是一个变化。

## 决定的顺序

⚠️ **这个顺序是设计主张；检查器不强制。** 从上到下决定，边决定边写。**不要从单个镜头反推作品**——那会把一堆好镜头变成一个没有主张的作品。

1. **Premise——发生了什么，一行。** 如果需要两句，作品有两个前提，其中一个是装饰。
2. **Question——观众带到最后的疑问。** 不是「能否活下来」，而是作品持续打开的特定不确定。**结尾必须能回答它。**
3. **Argument——作品说什么。** 结尾立起的主张。⚠️ **不要与主题词（「爱」「记忆」）混淆。** 主张是一句有人可以反对的话。
4. **Visual thesis——光、色、构图说什么。** 同一主张在视觉层面的表达。⚠️ **它必须至少在两个镜头中可见，否则只是一种气氛。**
5. **Value poles——作品转逆其间的价值对。** 写成 `{ja, en}`：日语给记录用，英语给 `DIRECTION` 节用。**没有对立面的价值是设定，不是赌注。**
6. **Acts——作品在哪里转逆。** 每一幕有一个 `turn`（一个变化）、`climax`、`value_from` → `value_to`、`rhythm`。**没有转逆的幕是时长，不是幕。**
7. **Sequences——相邻镜头如何对抗。** 每个序列有 `contrast`（下一个镜头针对什么）、`escalation`（什么在增长）、`transition`（如何交棒）、`payoff`（回收什么，若有）。然后是**三条约束——这个登记簿里抵达画面的部分**：
   - **`withheld`**——观众想要、却没有得到的东西。指名镜头上的 `wanted`（他们在等什么）与 `given`（镜头改给了什么）。⚠️ **两者必须不同，且都不能为空**——给出你承诺过的是拖延，什么也不给是事故。⚠️ **没有人在等的镜头，什么也欠缺不了**——只在观众具体地想要某样东西的地方写。
   - **`cuts`**——哪些镜头在自己内部切断时间。⚠️ **切口是序列的决定，不是镜头的决定**：它只在紧邻的镜头旁才有含义。镜头记录随后持有 `cut: internal`，**而规格必须不再写一镜到底**——生成器从不读记录。
   - **`tempo`**——用秒写下的序列形状，每个镜头一个数，**与各镜头的 `duration` 一致**。⚠️ **正本是 `duration`，`tempo` 是副本。** 三个以上相同的值就是平缓的律动，需要 `flat: true` 与 `note`。
   ⚠️ **有意平坦的序列写 `flat: true` 并说明理由**——那是决定，不是缺口。
8. **Shot functions——每个镜头为何存在。** 为每个镜头写 `function`、`value.from` / `value.to`、`stake`、`audience.feel` / `expect` / `know`、`button`。⚠️ **价值是该镜头那一个变化的价值，不是第二个变化。** ⚠️ **非叙事功能（质感・留白・样式美）不需要价值转逆**——但仍需要 `button`，因为每个镜头都以一个画面结束。
9. **Set pieces——哪张格式卡赢得位置。** 在镜头的 §6 `REF_FORMAT` 中指名卡片；在 `set_pieces` 中连同 `why` 记录选择。**卡片就是装置；不要把它的名字复制成镜头记录的第二个字段。**
10. **Sound——从沉默开始。** 决定哪里没有音乐、音乐在哪里进入、画内音在哪里承担场景。⚠️ **底线仍是 `no background music`**；想要音乐的作品把 `no background music` 写进 `bible.base_negatives_waived`。**不要创建第二个豁免席位。**
11. **Ending image——最后留下的东西。** ⚠️ **它必须是一个画面，不是一句教训。** 如果主张只能用语言说出，视觉主张就没有落地。

## 写什么，写到哪里

```yaml
dramaturgy:
  version: 1
  premise: "…"
  question: "…"
  argument: "…"
  visual_thesis: "…"
  value_poles:
    - ja: 安全
      en: safety
    - ja: 危険
      en: danger
  acts:
    - id: act-1
      shots: [s01, s02, s03, s04]
      turn: "…"
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
      withheld:
        - shot: s01
          wanted: "her face when the world answers"
          given: "the valley's light, and her back"
      cuts: [s03]
      tempo: [8, 8, 8]
  set_pieces:
    - shot: s07
      format: impossible-camera
      why: "…"
  ending_image: "…"
```

```yaml
# shots/<id>.yaml
dramatic:
  function: 転換
  value:
    from: 安全
    to: 危険
    stake: "父亲的记忆"
  audience:
    feel: "屏住呼吸"
    expect: "他会打开门"
    know: "母亲还活着"
  button: "闭着的门后的光"
```

⚠️ **`function` 是日语的记录值**（设定・上升・转逆・发现・决断・结果・蓄・解放・余韵，以及非叙事的质感・留白・样式美）。`design` 通过 `specmap.DRAMATIC_FUNCTION_EN` 把它写进规格的 `DIRECTION` 节——**记录保持日语，交给生成器的字符串是英语。**

⚠️ **`audience.know` 不是 `disclosure_state`。** 后者是世界的事实，前者是此刻观众知道的东西。**没有任何层比较两者**——那是同时阅读两者的设计会话的判断。

## 装置——卡片就是名字

AI 特有的演出住在**格式卡**里，不是新字段。镜头在 §6 `REF_FORMAT` 中指名卡片；`dramaturgy.set_pieces` 记录为什么在那里使用它。⚠️ **不要在镜头记录里加 `device:`**——同一个东西的第二个名字，是两者产生分歧的地方。

⚠️ **「多用」是目标，预算是让它成为纪律的东西。** 预算不是野心的上限，而是**每个装置都必须承担价值转逆**的规则：

- **一个镜头一个主装置。** 只有从另一面承担**同一个**价值转逆时，才允许第二个。
- **五镜头序列中默认 2–3 个装置镜头**；**场面最多 4 个**——每一个都必须承担转逆，并在其前或其后有一个接地镜头。
- ⚠️ **装置镜头需要接地镜头**：同一个世界，普通摄影机，在前或在后。**没有接地的连续装置镜头最多两个。**
- ⚠️ **不承担任何东西的装置是装饰——删掉。** 规则不是「少用」，而是**「不留装饰」**。

⚠️ **面部变形不是底线的事。** `BASE_NEGATIVES` 只有 `no watermark` / `no on-screen subtitles` / `no background music`。身份稳定由 `video-spec` 卡的 `## Negative`（`no morphing or drifting facial identity`）承担。**AI 的变形发生在世界、材质、尺度与光里，不在脸上。** 这不是限制，是这个基盘的美学。

## 检查器读什么

- **`L40`** — 有 `dramatic` 且 `function` 为叙事功能的镜头，`value.from == value.to`。非叙事功能豁免；没有 `dramatic` 的镜头是注记数量。
- **`L41`** — 没有 `turn` 的幕、没有 `contrast` 的序列、指向不存在镜头的 `payoff`、不存在的 `shots`。没有 `acts`/`sequences` 是注记。
- **`L44`** — 强度曲线：相同 `intensity` 连续三个以上镜头，或幕中没有峰值。声明 `flat: true` 的序列是注记。
- **`L47`** — `performance.objective == performance.obstacle`。缺少 `performance` 不是违反，而是注记数量。
- **`L48`** — `withheld` 的 `wanted` 与 `given` 相同，或其中之一为空。作品最后一个镜头上的欠缺是注记。
- **`L49`** — 序列声明的切口镜头没有持有，或相反。**以及仍然写着一镜到底的规格。**
- **`L50`** — `tempo` 与镜头的 `duration` 不一致，或没有 `flat: true` 与 `note` 的等间隔。

⚠️ **转逆是否好、对比是否锐利、装置是否令人难忘，没有任何层读取。** 那属于评议会与作者。

## 这个阶段不决定什么

- **作品是否动人。** 检查器无法知道；评议会建议，作者决定。
- **规格。** `design` 写 §1–20，包括 `DIRECTION` 节。
- **take、采用、剪辑。** ④与作者。
- **路线与模型。** §18 的标题指名路线（`L18`）。

## 语言

- **记录侧是日语。** `function`、`value.from` / `value.to`、`stake`、`audience`、`button`——这些由作者与 `L40`/`L43`/`L47` 阅读。
- **交给生成器的字符串是英语。** `DIRECTION` 由 `design` 从这些记录与 §12 用英语写。**不要把记录翻译成提示词；写英语的类型。**

## 延伸阅读

- [`skills/breakdown/SKILL.md`](../breakdown/SKILL.md) — ①的前半，本阶段读取的镜头表
- [`skills/design/SKILL.md`](../design/SKILL.md) — ②，写 `DIRECTION` 的步骤
- [`skills/staging/SKILL.md`](../staging/SKILL.md) — ②中的摄影机
- [`references/formats/video-spec.md`](../../references/formats/video-spec.md) — §12 EMOTION 与 `DIRECTION` 节
- [`schemas/ledger.schema.json`](../../schemas/ledger.schema.json) — `dramaturgy` 的形状
- [`schemas/shot-record.schema.json`](../../schemas/shot-record.schema.json) — `dramatic` 的形状
