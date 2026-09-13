<!-- i18n-version: 1.0.0 | canonical: projects/hitosara/takes/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# `takes/` — the record of what came back

Take records are `*.yaml` (`schemas/take.schema.json`). **One per sample.**

⚠️ **`media/` and `takes/` are different.** `media/` is the place for **things**, `takes/` is **records**.
**Placing something is not recording it**——so unless you look at both, you cannot know what exists now.

## How to read the record

| Field | |
|---|---|
| `shot` / `kind` / `index` | Which shot's, which path's, the how-manieth. ⚠️ **`index` is counted per `(shot, kind)`**——images and videos are separate sequences |
| `file` | The file name inside `media/`. ⚠️ **A claim, not a proof of existence** (below) |
| `provider.model` | The generation model. Pulls the registry in `specmap.MODELS` |
| `params.source` / `source_version` | The **canonical location** of the fed string and **the version at that time**. ⚠️ **Do not keep a copy**——copies contradict |
| `verdict.machine.measured` | **The value measured from the file that came back.** "The value requested" and "the value that arrived" are different |
| `adopted` | Whether it was adopted. **Adoption is selection, and the author is editing** |

⚠️ **Whether the thing `file` points at exists is not confirmed by the check.** The foundation does not open `media/`,
as `media/README.md` declares, and `L25` keeps that declaration.
**`take.file` is a claim, not a proof**——this hole is reported by `L25` in a note.

## What exists now

**Takes exist as many as there are `*.yaml`.** ⚠️ **Do not write the count here**——the count moves,
**write it and it will contradict.** The count and the breakdown **`L25`'s note counts on the spot and states.**

- ⚠️ **The number of takes and the number of mp4s in `media/` do not match.** There are two directions——
  **① It is in `media/`, but there is no record** (placing something is not recording it).
  **② The file a record claims no longer exists** (`file` is a claim, not a proof).
  ⚠️ **The machine fires for neither direction**——because `L25` does not open `media/`.
- Since there are two paths, **there can be shots that advance on only one side.**
  **A state where only one side has advanced is not "incomplete" but "that state"**——
  but **unless you can read from the record which side has advanced, it is not a state.**
  ⚠️ **Do not write which shots those are in this text**——**it moves.** Count the records and you will know.
- ⚠️ **The name in `file` moves at the author's hand.** Even if it is renamed the machine does not fire (it does not open `media/`)
  ——**the record quietly goes stale.** So **before reading the record, first count `media/`.**

## ⚠️ Do not call empty "OK"

`check.py` reports like this if `takes/` is empty——

> `takes/` exists, but **there is not a single take record**——generation has never run.
> "0 takes" is not "0 violations." **The selection check is empty.**

**0 items is not a pass.** The same holds even if there are records——`L25`
**lists "things not confirmed" in a note** (takes whose images have nothing to match against,
cases where the specification was corrected after generation, the existence of `file`). **Read the note.**

⚠️ **`*.md` is not read.** `Project.__init__` reads only `*.y*ml`.
So this text is not counted as a take——**being counted would be a problem.**
