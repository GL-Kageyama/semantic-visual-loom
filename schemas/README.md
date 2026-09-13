<!-- i18n-version: 1.0.0 | canonical: schemas/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# schemas/ — the canonical data structures

**The structures this repository holds are canonical here.** The `.yaml` under `projects/<project>/` follows these five.

## Why JSON Schema

**Because pre-flight verification reads this by machine.** The checkers in `engine/ledger/` read the shot records and judge, in order to "crush design failures without running generation even once."
A format that exists only for people to read is of no use for that.

Japanese explanations go in `description`. **English keys, Japanese explanations** — for the same reason the strings handed to the generator (`Negative`, the prompt, enum values)
are the English-invariant part, the keys stay in English.

## The five

| File | Structure of what | How settled |
|---|---|---|
| `bible.schema.json` | **Work ledger**. The invariant part of the work's world. One per project | Low (where the line between the invariant part and the variable part falls is undecided) |
| `ledger.schema.json` | **Production ledger**. Holds continuity and disclosure **in a single file**. One per project | Medium (the shape of disclosure is settled. The attribute types remain) |
| `shot-record.schema.json` | **Shot record**. One per generation. Self-contained | High (`unit` and `role` are decided) |
| `take.schema.json` | **Take**. One per sample | Medium (dependent on the number of acceptance layers) |
| `timeline.schema.json` | **Timeline**. The sequence of adopted takes + cut points + text + audio | **Lowest** (which one is authoritative is undecided) |

## ⚠️ What this schema cannot fire

**The check for "a single change" does not complete at this layer.**

`unit` was made a pair of `{ before, after }` in order to fire "`before` and `after` are the same."
**But JSON Schema cannot compare two properties** — the standard specification has no such feature.
We measured it for real — it lets `{ before: "same", after: "same" }` through.

**The escape routes were measured too, and they are closed.** `if`/`then` + `const` is **enumeration**, not comparison
(it catches only as much as the literals you write, and `before`/`after` are free text, so it does not close).
The `$data` reference is a proposal that did not enter the standard specification, and reference implementations treat it as a plain literal.
(The measurements are in `HISTORY.md`.)

**Therefore this constraint is borne by the checkers in `engine/ledger/`.**
**"Made them a pair" and "can check the pair" are different things.** Pairing them alone does not give you the latter.

The same shape of hole exists elsewhere. **What JSON Schema guarantees is "shape," not "meaning."**

| What we want to fire | Who fires it |
|---|---|
| `before` and `after` are the same | **The checker** (cannot be written in the schema) |
| Whether it is one environment (whether `place` is singular, whether multiple `place` values appear in `beats`) | **The checker** |
| Whether it is one moment | **The checker** |
| Whether a mismatch of role and mode is a judgment or an accident | **The checker** (if a judgment, it is left in the record) |
| Whether the clothing in a reference image matches the clothing of that shot | **The checker** |
| The discrepancy between `reference_set` (intent) and `attached` (actual) | **The checker** |
| Whether the shape is correct (required, type, enum, the format of `duration`) | **This schema** |

**Every item is caught without running generation even once.**

## Where the decisions come from

| What | Decision |
|---|---|
| `unit` = `{ before, after }` | 2026-09-13, the author. In free text a machine cannot judge "is it one change" |
| `role:` = required | 2026-09-13, the author. If it is empty, what that shot is judged by is not decided |
| `disclosure` = a sequence of change points keyed by shot ID | Key it by `shot:`. Both `at` × `clip:` and an enumeration of Segment IDs were dropped, because both try to write "which shot" in the ledger side's coordinates |
| `at` = the range name of a §16 heading | The derivation rule is taken from the headings (not from shot IDs). Measured 87 and zero failures |
| The shot record holds the "actual" of attachments | In ukebi V1 there were two clips in which HANA appears yet HANA's sheet is missing, and the specification had not a single declaration of attachment |

## What is not yet decided

**They are written into the schema as `description`.** The main ones —

- **The registry of roles (`role`).** Only 5 of 12 are in use (measured; registration is undecided)
- **Whether to make the motion layer a required field.** The claim that "every shot has it" and whether blanks are allowed do not mesh
- **Whether binary is enough for the `density` of `beats`**
- **The type of the `disclosure_state` value**
- **How to hold `… yet` (forward reference).** §16 sets `no name yet` **immediately before** the reveal. This is not a state — it is a forecast of what is about to happen
- **The retention period of attachments**, **whether to keep failed takes**
- **The output format of editing** (OTIO / EDL / FCPXML / our own render)
