<!-- i18n-version: 2.1.0 | canonical: references/formats/video-spec.md | translated: 2026-09-18 -->

**Language:** [English](video-spec.md) | [日本語](video-spec-ja.md) | [中文](video-spec-zh.md)

# 视频规格（video-spec）

- **目的**: 叙述（再体验・吸引） ／ **粒度×时间**: 整段弧线 × 并列 ／ **尺寸・比例**: 电影 16:9，`DURATION` 的片段
- **摘要**: 唯一输出**带有时间**的格式。把片段的时长不均等地分配到弧线上，并承载静止画毫无词汇的四个轴——时间、运动、镜头移动、声音。

## 这个格式唯一的不同之处

本引擎的其他格式都把时间**丢弃**，落在静止的平面上。只有这个把时间**折入**。压缩的对象不是「会说话的一点」，而是**会说话的一段持续**，选择的提问也随之改变。

> 不是*哪一个瞬间*，而是**哪些瞬间值得几秒，哪些一闪而过**。

给每个节拍同等时间的摘要，等同于视频里的塞满。**不均等的时长本身就是构图。**

## 环境变量
`SUBJECT`＝弧线, `DURATION`＝片段长度（**时长由模型决定**）, `ASPECT`＝画面比例, `BEATS`＝带秒数区间的节拍表, `CORE`＝占据最大份额的节拍, `HOOK`＝片段收束的那个音

## 构图语法

**节拍表，而非镜头清单**。把弧线排成带**刻意不均等**秒数区间的节拍。其中一个节拍——核心的揭示——占据最大份额（参考值：约 `DURATION` 的 30%）。稀疏的节拍靠质感与持续撑住，密集的节拍在几秒内叠入多个事件。

**静止画不具备的四个轴：**

| 轴 | 固定什么 | 省略会怎样 |
|---|---|---|
| **时间** | 节拍的秒数区间、密度（疏／密）、转场 | 均匀的节奏——每个节拍都读起来同样重要 |
| **运动** | 主体的动作、物理（重量・惯性・流动・冲击） | 轻飘失重的动作 |
| **镜头** | 跨时间的移动（而非镜头类型）、时机、对象 | 只是持续了 N 秒的静止画面 |
| **声音** | 台词、音效、环境音、音乐及其情绪功能 | 只靠画面承载意义 |

**同一性锁定**。当弧线跨越多次生成时，连续性区块（主体外貌、环境、照明、色板）要**整块贴入每一个实例**——不概括，不以引用代替。独立的生成之间没有记忆。即使只有单一片段也要写：负面提示词所守护的正是它。

**停在那个音上，而不是它之后**。最后一秒是观者决定「还有没有下一段」的地方。落在钩子上——不要在其后再加一个收束的节拍。

## do
- 给节拍**明确不均等的**秒数区间，并说明哪个疏、哪个密
- 把最大的单一份额用在核心揭示上
- 把镜头写成**跨时间的移动**（对象・速度・时机），而不是镜头类型
- 固定物理——重量・惯性・流动——让动作具有质量
- 完整写出同一性锁定，并在每个实例中逐字重复
- 分开可复用的规格（WHAT/HOW）与已解决的实例（WHEN・时长・输出）
- 在 §14 指名作品的语言，并让它抵达 `Audio Prompt`——**若有说话，那就是该语言**；没有说话的作品也要声明。**空白不是中立**（空白会被生成器的默认语言填满）
- 把字幕与 BGM 的禁令写进 Negative——**除非我方指定，两者都不出现**
- 停在钩子上

## avoid
- 把 `DURATION` 切成等长区间
- 没有镜头移动的镜头清单（静止画的幻灯片）
- 未说明重量与惯性的运动（轻飘的漂移）
- 因省略而造成的无声——把台词、音效、环境音、音乐留作未指定
- 把语言留作未指定——**生成器会用它的默认语言说话**（实测：带说话的影片被烧上了中文字幕）
- 以为音乐和字幕只在你要求时才出现——**省略就是在要求模型的默认行为**（实测：`no on-screen subtitles` 已在 Negative 里，字幕仍被烧上）
- 用概括代替贴入连续性区块
- 在钩子之后再加节拍
- 呈现原作在弧线的此刻尚未揭示的内容（参见⑧忠于原作——后续的揭示泄漏进较早的片段，是这个格式特有的失败）

## 模板是一份规格，而不是一个句子

**不要把这个格式压成一段散文。** 本引擎的其他卡片都以一个填空句收尾——因为静止画就是一条提示词。视频则是一份*文档*：成果物是一份各节可分别指认的规格书，唯其如此，时间、运动、镜头与声音才能各自修订而不必重写其余。一段散文恰恰摧毁了这张卡片为之存在的那四个轴。

散文段落依然存在——但只作为 **§18 七个槽位中的一个**，在生成时由已填好的规格*导出*。

## 规格骨架（§1–20）

按此顺序填写。右栏是各原则的落点。

| § | 固定什么 | 引擎 |
|---|---|---|
| **1 VIDEO** | `DURATION`・`ASPECT`・分辨率・帧率・朝向 ／ 目的・叙述功能・情绪・节奏 | — |
| **2 WORLD** | 概念・时代・地点・时刻・天气・氛围 ／ 世界规则 ／ **Visual Language** | ⑥样式落在 Visual Language |
| **3 SUBJECTS** | 同一性・外貌・行为（性格／典型动作／情绪幅度） ／ **连续性要求：Must Preserve・May Change** | ③翻译 ＋ ④保持一致 |
| **4 ENVIRONMENT** | 地点・要素 ／ 环境行为（风・天气・粒子・背景运动） | ③翻译 |
| **5 OBJECTS** | 外貌・材质・功能 ／ 三种重要度（叙述／视觉／连续性） | ③翻译 |
| **6 REFERENCES** | 每个参照各自 **Defines** / **Influences** / **Does Not Define** 什么 | ④保持一致 |
| **7 NARRATIVE** | 核心事件・开端・展开・转折点・高潮・结尾 | ①理解 |
| **8 TEMPORAL STRUCTURE** | **秒数区间不均等的节拍表** ／ 时序方针（`NON_UNIFORM`） ／ 疏与密的区域 | ②**选择——本格式的心脏** |
| **9 ACTION** | 每个行为的意图・强度・速度 ／ Before・After・Simultaneous With・**Causes** | ⑤构图（因果） |
| **10 CAMERA** | 镜头语言 ／ **带时机・移动・对象・速度的镜头事件** | ⑤构图延伸至时间 |
| **11 MOTION** | 主体／物体／环境的运动 ／ **物理：重量・惯性・加速・流动・冲击** | ⑤构图延伸至时间 |
| **12 EMOTION** | 作为链条的情绪弧 ／ 带强度的情绪事件 | ③翻译 |
| **13 LIGHTING** | 主光・辅光・轮廓光・环境光・色温 ／ 照明事件 | ③翻译 ＋ ⑥样式 |
| **14 AUDIO** | 台词（说话者・内容・语气）・音效・环境音・音乐及其情绪功能 ／ **作品所说的语言（指名）** | **本格式独有的轴** |
| **15 CONTINUITY** | 同一性・空间・时间・视觉・运动的连续——**同一性锁定** | ④保持一致 |
| **16 CONSTRAINTS** | MUST / MUST NOT / PREFER / ALLOW | ⑦负面 |
| **17 GENERATION PRIORITIES** | 冲突时的优先顺序——把对原作的忠实置于观感之上 | ⑧忠于原作 |
| **18 PROMPT MAPPING** | 七条提示词——六条来自 §1–17，第七条来自**样式卡** | — |
| **19 GENERATION INSTANCE** | 一次生成的解决值（时长・参照・事件・输出） | — |
| **20 ITERATION** | 观察到的问题 → 变更 → 下次生成 | — |

让 §1–18 保持可复用，把一切依赖时长的内容放进 §19；如此，即使片段长度或生成模型改变，同一份规格仍能存续。

⚠️ **标题成族的节只有 §18**: `18. <模型名> PROMPT MAPPING`。
那个名字要与登记簿（`specmap.MODELS`）对照，而**那个名字决定路径。**
登记在册的视频路径有三条——**`WAN 3.0` 附上 `key_image`**；
而**`MINIMAX H3` 附上分镜图像，根本没有图像路径**——
后者的纸由 `distill-essence-engine` 制作（格式 `storyboard`、样式 `luminous-anime`），
住在 `specs/board/<id>-board.md`。
而**`SEEDANCE 2.5` 默认什么都不附**——它读一条很长的提示词，
**而那条提示词可以自带时钟**（`0-3s:` `3-6s:`）——另一方面，
**它的 `Negative Prompt` 槽位并不被当作地板来接收**（`L30`）。
⚠️ **这条路径的约束全部在 [`docs/seedance-route.md`](../docs/seedance-route.md) 里。**
⚠️ **一个镜头只持有一个 `spec`**，所以**一个镜头无法持有两条以上的路径**——用两条路径拍同一个镜头再比较，现在还做不到。

⚠️ **这张卡片是常规格式，三条路径都填它。**
它自身不固定时间的文法——片段的时长由什么构成，由路径决定，
**而各条路径各自记述了那一点**——`WAN 3.0` 读作一条连续镜头；
`MINIMAX H3` 把镜头组成为由独立分格以自然动画相接而成；
`SEEDANCE 2.5` 读作一条很长的提示词——**那条提示词可以自带时钟**
（`0-3s:` `3-6s:`）——而**它的 `Negative Prompt` 槽位并不被当作地板来接收**（`L30`）。
⚠️ **这条路径的约束全部在 [`docs/seedance-route.md`](../docs/seedance-route-zh.md) 里。**
⚠️ **因此，§18 不得说什么，是由路径决定的。** 在 `MINIMAX H3` 上，
每一格本身就是一场戏，与下一格之间用自然的动画相接——
⚠️ **所以 §18 不得禁止这个接缝。** **把 `no cut` 写成无条件的规则，
会堵死一格改变地点的唯一合法手段**，生成器就会把两个地点当成一个房间
连下去。**禁止切到无关的地点，而不禁止过渡**——并且当一格改变地点时，
**规格必须写明是哪一种。** 出处从不使用 `カット` 一词，所以
切还是连，由那个镜头自己决定。⚠️ **落在这条路径上的约束的清单——
交出去的字符串与那张纸，两者都在内——是
[`docs/h3-route.md`](../docs/h3-route-zh.md)。**
⚠️ **一个镜头只持有一个 `spec`**，所以**一个镜头无法持有两条以上的路径**——
用两条路径拍同一个镜头再比较，现在还做不到。
⚠️ **`L28` 读的是规格的 §18，与 `specmap.MODEL_ROUTE` 对照**——
它不打开这张卡片。⚠️ **把一条路径的文法带进另一条路径的规格，才是陷阱**——
产生这条警告的失败记录在 `HISTORY.md` 里。

## §18 的提示词槽位

七条提示词。前六条**主要**取自上文指名的各节。
**第七条不取自规格，而取自样式卡。**
**彼此分离本身就是要点**，不要混为一谈。

```text
Master Prompt   ← §1 + §7 + §8
  A {DURATION} cinematic take ({ASPECT}) of {SUBJECT}, one clip.
  Beats, deliberately uneven: {BEATS}. The core beat — {CORE} — holds the largest
  share of the duration; the remaining beats pass quickly. Ends on {HOOK}.

Visual Prompt   ← §2 Visual Language + §3 Appearance + §4 + §5 + §13
  (the look, held still: art direction, palette, rendering, subject appearance,
  environment, key/fill/rim, color temperature — no motion words)

Motion Prompt   ← §9 + §11
  (what moves, in what order, with what weight, inertia and speed — subject motion,
  object motion, environmental motion, and the physics that governs all three)

Camera Prompt   ← §10
  (the camera events in order: timing, movement, target, speed, transition)

Audio Prompt    ← §14 + the work's language (`bible.language`)
  (dialogue with speaker and delivery, sound effects, ambient bed, music and its
  emotional function — and the work's language, named, so that the generator does
  not fill the blank with its own default)

Negative Prompt ← §16 MUST NOT + this card's Negative + the style card's Negative

Style Motion    ← the style card's Motion character (not §1–17 — the only slot taken from the style)
  (how this style moves at all — full animation or limited, whether a held frame
  is permitted, what the primary mover is. The specification writes what moves in
  THIS clip; the style card writes what movement MEANS in this style.)
```

上文的出处是主要的，不是唯一的。镜头的稳定性禁令就是已知的一例：
它写在 §10，经由 Negative 槽位抵达模型。

⚠️ **`Style Motion` 之所以是第七条。** 其余六条在**本规格之内**决定——
改写某一节，它们随之改变。`Style Motion` 在**本规格之外**决定——
更换样式它随之改变，**同一个 §11 会有不同的含义。**
「什么在动」与「在这个样式里动意味着什么」是两个不同的问题，
混在一起会让**规格覆盖样式**（或反之）。
⚠️ **即使 §11 MOTION 为空，`Style Motion` 也能写。** 即使是主体静止的镜头，
**这个样式如何处理静止的主体**也是确定的——**这是两个不同的槽位。**

## Negative
`no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no background music, no watermark, no morphing or drifting facial identity`

## 事例
- 凌晨两点、你在活着谁的时间 第1话 → 30 秒摘要（gozen-niji-video-01・soft-cel-anime）

## 来源
是以 Wan 3.0 作为中间表示写成的视频生成规格，其后向另外两条路径开放（[`docs/h3-route.md`](../docs/h3-route-zh.md)、[`docs/seedance-route.md`](../docs/seedance-route-zh.md)）——**这张卡片来自哪条路径，记录在 `HISTORY.md` 里**；`storyboard`（最接近的静止画祖先——具备分格与镜头类型，但没有移动、物理与声音）
