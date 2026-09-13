<!-- i18n-version: 1.0.0 | canonical: projects/hitosara/timeline/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# `timeline/` — 编辑还没有

**这个目录是刻意空的。** 时间线是 `*.yaml`
（`schemas/timeline.schema.json`）。一本都没有。

⚠️ **不要把物放在这里。** 编辑做出来的文件（接起来的东西）是 `../renders/`——
**记录在这里，物在 `renders/`。** ⚠️ **方向只有一个**——**记录声称物**（副本会相互矛盾）。

⚠️ **现在 `check.py` 不读这个目录。** 读它的是第3阶段。
`SCHEMAS` 常量（`engine/ledger/check.py`）里有 `"timeline"`，但
**`Project` 不打开这个目录，`validate_shape()` 也不套用
`timeline.schema.json`。** **宣言正确，和宣言被照着读，
是两回事。**

⚠️ **所以，现在这个目录是空的，不是任何一种报告。**
`takes/` 的空会被报告（「一本都没有」）。**这边的空不会被报告**
——**同样是「空」，一边被检查着，一边没有被检查。**
**这个差别，不写在这里就看不见。**

⚠️ **`*.md` 不会被读**（读的一侧只选 `*.y*ml`）。
所以这段文字不会被算作时间线——**被算进去就麻烦了。**

## 这个目录被填满的时候

- 选别 — `take.verdict`（`machine` / `adherence` / `council`）与 `adopted`
- 尺的解决 — `shot.duration`（意图）→ `take.params.duration`（生成）→
  `clips[].in` / `clips[].out`（采用）。**三者第一次可以持有不同的值。**
- 文字的烧入 — `text_events`。**生成器不画文字**
  （`shots/hitosara-ch01-seg03.yaml` 的 `text_channel`、`seg07`、`seg10`）。
- 采用理由 — `clips[].cut_reason`
