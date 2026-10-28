---
name: review
description: 'The council after stage ④ — four evaluators (emotional-impact, aesthetic-critic, admiration, hook) read a shot''s specification and the work''s treatment, and their scores are written into the take''s verdict.council. It advises; it never adopts. ⚠️ It reads the specification, not the picture — generation happens outside this repository.'
argument-hint: '(optional) the project name, or the shot. e.g. /semantic-visual-loom:review drama-pilot'
---

<!-- i18n-version: 1.0.0 | canonical: skills/review/SKILL.md | translated: 2026-10-29 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# review — the council that sits down after ④

**A shot came back, and somebody has to say what it does to a person.** The checker will not — it reads form, and quality is not form. So the judgment is made by named evaluators, **written down as numbers and notes, and left in the take.**

⚠️ **This stage does not adopt.** It fills `verdict.council` and stops. **Adoption is selection, and the author is the editor** — `skills/shot` says it, `L25` enforces it, and nothing here changes it.

## ⚠️ The limit, stated first

**The evaluators cannot see the video.** Generation happens outside this repository — there is no call to a model here and no `media/` reader. **What is evaluated is the specification and the treatment**: the strings that will be fed, the §1–20 that frames them, the `DIRECTION` section, the `dramatic` records behind it.

⚠️ **So a score here is a judgment about the design, not a measurement of the result.** Two consequences, and both stay written:

- **A specification can score well and produce a dull clip.** That is not a failure of the council; it is what "the generator is a sample" means.
- **When a generation exists, the score does not silently become a score of it.** Say which object was scored. ⚠️ **Do not let a judgment of the design stand in for a judgment of the picture** — the note must name what was read.

## What this stage owns

| | What | Where |
|---|---|---|
| **the council** | four evaluators' scores and notes | `projects/<name>/takes/<id>-<kind>-<n>.yaml` → `verdict.council` |
| **the blind comparison** | which of two takes author and council prefer, and why | same take, in its `note` |
| **the recall record** | which three shots are remembered a day later | the work's history, not the checker |

**It does not own** the verdict's other two layers (`machine`, `adherence` — `shot` writes them), **the specification** (`design`), **the take itself** (`shot`), or **adoption** (the author).

## The four evaluators

Each is a seat, and each answers a different question. **Do not let one stand in for another** — a shot can be beautiful and hollow, or moving and unmemorable.

| evaluator | the question it answers | what it reads here |
|---|---|---|
| **emotional-impact** | does this move a person, or only describe movement? | `dramatic.value` and `stake`, `audience.feel`, §12's emotion chain, `DIRECTION`'s instruction |
| **aesthetic-critic** | is the visual language coherent — beauty, not prettiness? | §7 style, §11 motion, `visual_thesis`, the `value_poles`' English turning in `DIRECTION` |
| **admiration** | does an outcome exceed prediction **and** feel inevitable? | the shot's `unit`, its `button`, and whether the device was foreseeable |
| **hook** | does it make someone need the next moment? | `audience.expect` and `audience.know`, the sequence's `transition`, the act's `turn` |

⚠️ **The set is not fixed forever.** These four cover what this revision is for — drama, beauty, surprise, pull. **A role may call for another** (a documentary landscape needs no hook). ⚠️ **Do not add an evaluator that only restates a check** — a seat that echoes `L40` is not a judgment.

## What gets written, and where

```yaml
# takes/<id>-<kind>-<n>.yaml
verdict:
  council:
    emotional-impact:
      score: 4
      note: "…"          # what was read, and what it would take to reach 5
    aesthetic-critic:
      score: 3
      note: "…"
    admiration: 2        # the bare number is still legal — the field is oneOf
    hook:
      score: 4
      note: "…"
```

⚠️ **`score` is 1–5.** The scale is fixed here so that a later comparison means something; **the note carries the argument.** A score with no note is a verdict with no reason, and **a reason is what the author reads before choosing.**

⚠️ **Write the object form, not the bare number.** The schema accepts both (`schemas/take.schema.json`, `council` is `oneOf` `number` | `{score, note}`) because **older records exist and must not be rewritten.** ⚠️ **A new record with no note throws away the only part a person can use.**

⚠️ **No layer reads `council`.** The checker cannot tell a 5 from a 1, and that is deliberate — **a check that scored quality would turn "is this good" into "did the string appear."** The record is for the author and for the next revision.

## The blind comparison

**The purpose of this revision is that the work becomes more dramatic.** So it has to be measured against itself, not against nothing.

1. **Take the same shot twice** — the old specification and the new one, **same route, same duration, same key image.** If any of those differ, the comparison is of two things, not of two versions.
2. **Hide which is which.** ⚠️ **If the evaluator knows which is new, it is grading the revision, not the shot.**
3. **Ask both the council and the author.** ⚠️ **Record disagreement, do not resolve it** — the author's choice is the decision, and the council's dissent is the most useful line in the record.
4. **Write the result in the take**, and the aggregate in the work's history.

⚠️ **A tie is a result.** **It says the revision did not reach this shot**, and that is more informative than a forced preference.

## The recall record

**A day later, which three shots do you still see?**

⚠️ **Write the answer down before reading the scores** — reading them first makes the memory a summary of the council. **Remembering is the objective of this revision**; a work whose shots score well and are forgotten has not succeeded.

⚠️ **This is not a check and will never be one.** It is a sentence in the work's history, written by the author.

## What this stage does not decide

- **Whether to adopt.** ⚠️ **Never write `adopted: true`.** See [`skills/shot/SKILL.md`](../shot/SKILL.md) — a session that adopts becomes a session the checker believes.
- **What the specification should say.** A note may suggest; `design` decides and rewrites.
- **Whether the shot's `unit` changed.** ⚠️ **A review that quietly edits the shot is not a review.** The record it read must still be the record that was scored.
- **Whether the council was right.** Later takes and the author's memory settle that, not this document.

## Language

- **The notes may be Japanese.** They are records, read by the author — the same layer as `role` and `dramatic`.
- **The strings handed to the generator are English**, and this stage hands none. ⚠️ **Do not translate a `DIRECTION` section or a §18 slot while reviewing it** — a translation is a copy, and copies diverge.
- **The evaluator names are English** (`emotional-impact`, `aesthetic-critic`, `admiration`, `hook`) — they are keys, and a key that changes spelling splits one seat into two.

## Where to read more

- [`schemas/take.schema.json`](../../schemas/take.schema.json) — `verdict.council` and why the seat accepts both shapes
- [`skills/shot/SKILL.md`](../shot/SKILL.md) — the take this stage fills, and the boundary it must not cross
- [`skills/direction/SKILL.md`](../direction/SKILL.md) — the treatment and `dramatic` records the evaluators read
- [`docs/dramaturgy.md`](../../docs/dramaturgy.md) — the ledger's third register, in full
- [`HISTORY.md`](../../HISTORY.md) — where the measurements of this revision are recorded
