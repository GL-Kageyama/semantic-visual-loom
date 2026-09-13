<!-- i18n-version: 1.0.0 | canonical: projects/hitosara/timeline/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# `timeline/` — there is no editing yet

**This directory is intentionally empty.** A timeline is `*.yaml`
(`schemas/timeline.schema.json`). There is not a single one.

⚠️ **Do not put things here.** The files editing produced (what was joined) are `../renders/`——
**the record here, the thing in `renders/`.** ⚠️ **The direction is one**——**the record claims the thing** (copies contradict).

⚠️ **Right now `check.py` does not read this directory.** What reads it is stage 3.
The `SCHEMAS` constant (`engine/ledger/check.py`) has `"timeline"` in it, but
**`Project` does not open this directory, and `validate_shape()` does not apply
`timeline.schema.json`.** **That a declaration is correct and that it is read
as declared are different things.**

⚠️ **So that this directory is empty right now is not a report of any kind.**
The emptiness of `takes/` is reported ("not a single one"). **The emptiness here is not reported**
——**the same "empty," yet one is checked and the other is not.**
**This difference is invisible unless it is written here.**

⚠️ **`*.md` is not read** (the reading side selects `*.y*ml`).
So this text is not counted as a timeline——**being counted would be a problem.**

## When this directory fills up

- Selection — `take.verdict` (`machine` / `adherence` / `council`) and `adopted`
- Resolving the duration — `shot.duration` (intent) → `take.params.duration` (generation) →
  `clips[].in` / `clips[].out` (adopted). **For the first time the three can hold different values.**
- Burning in text — `text_events`. **The generator does not draw text**
  (`text_channel` of `shots/hitosara-ch01-seg03.yaml`, `seg07`, `seg10`).
- The reason for adoption — `clips[].cut_reason`
