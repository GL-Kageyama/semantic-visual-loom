---
name: shot
description: 'Stage ④ of semantic-visual-loom — the record and the sample. Use when a shot record has to stand on its own as one pasteable unit, or when a generation has come back and has to be written down as a take. Completes the self-contained record and writes one take per generation, with the provider, the parameters and the verdict. Emits the finished record and the takes — and does not adopt.'
argument-hint: '(optional) the project name, or the shot. e.g. /semantic-visual-loom:shot hitosara'
---

<!-- i18n-version: 1.0.0 | canonical: skills/shot/SKILL.md | translated: 2026-09-14 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# shot — ④ the record and the sample

**One generation, one sheet.** The shot record is written so that it **stands alone** — the
schema says *pre-flight verification runs against this one sheet alone*. And what comes back is
**a sample**: a candidate for adoption, **not the work.**

⚠️ **This is a document, not a program.** It instructs a session. **Generation does not run in
this repository** — the only command that runs is the checker, and it runs against
**the record and the takes this stage writes.**

## What this stage owns

| | What | Where |
|---|---|---|
| **the self-contained record** | the seven required fields, plus the derived sets written into it | `projects/<name>/shots/<id>.yaml` |
| **the sample** | `shot` · `kind` · `index` · `file` · `provider` · `params` · `verdict` | `projects/<name>/takes/<id>-<kind>-<n>.yaml` |
| **the failure of a sample** | `failure_type` | same |

**It does not own** the staging (**② `design`**), the derivation of the sets
(**③ `ledger`**), or **adoption (⑤ selection — and that is the author's act).**

⚠️ **The record is the paste unit.** That is not a stylistic preference — it is the reason the
seven fields are `required`. **The file handed to a generation session carries the values, not a
pointer to them.**

## The order of decisions

⚠️ **This order is a design claim; the checker does not enforce it.** The layers run in an
order of their own. What follows is the order that **makes the sheet complete before it is
handed over.**

1. **Make the record stand alone.** Every value a session needs is in this one file.
   ⚠️ **But do not hand-copy what is derived.** The distinction is exact: **decisions are
   written here** (`unit`, `role`, `mode`, `motion`, `beats`, `duration`), while **derivations
   are written by ③ and regenerate from the ledger** (`reference_set`, `forbidden_set`).
   A hand-edited copy of a derivation is **a second canonical, and copies diverge.**
2. **All seven required fields are present** — `shot` · `unit` · `role` · `place` · `time` ·
   `mode` · `duration`. **Fires if wrong:** the form layer (`S1`).
   ⚠️ **`role` is required because an empty one leaves undecided what judges that shot.**
   ⚠️ **The form layer looks at its presence; `L15` looks at whether its value resolves.**
   Two different questions, two different layers.
3. **Both paths are written** — `spec:` (video) and `key_image:` (image).
   **Fires if wrong:** `L18`. ⚠️ **The path is decided by the field, not by `mode`** — every
   shot carries both.
4. **The sets are re-derived, not remembered** — `reference_set` from `known_keys()`, the
   forbidden set disjoint from it, and `attached` written as a declaration.
   **Fires if wrong:** `L5` · `L6` · `L8`.
5. **`disclosure_state` is read, not copied.** **Fires if wrong:** `L7a` · `L7b` · `L9`.
   ⚠️ **This is the step where copying is most tempting and most damaging.** Copy the ledger
   into the record and **`L7` is merely reading the same thing twice** — `L9` exists to say so,
   and it cannot tell a copy from an independent read when they agree.
6. **`sound` and `text_channel`** — each has a **declared destination**, and they go to
   different places. ⚠️ **`text_channel` splits by kind**: `overlay` is burned by `timeline`
   (**the generator does not draw text**), `voice` goes to §14. ⚠️ **`sound` has no reader in
   this repository** — its destination is the audio foundation.
7. **Run it, then hand the sheet over.**

```bash
python3 engine/ledger/check.py projects/<name>   # read the violations AND the notes
python3 engine/ledger/check.py --self-test       # confirm the checker fires at all
```

**Generation happens outside this repository** — there is no code here that calls a generator,
and no API key.

8. **One generation, one take.** `shot` · `kind` · `index` are required.
   ⚠️ **`index` counts per `(shot, kind)`, not per shot** — **images and videos are separate
   series.** ⚠️ **`kind` is derivable from `provider.model` and is deliberately not derived**:
   **derive it and the path changes silently the moment a model name is rewritten.**
   **Being derivable is not a reason to omit a field.**
9. **`params.source` points at the canonical — never copy the string that was fed.**
   ⚠️ **A copy diverges**, and **a second canonical is worse than a pointer.** The same
   discipline as `place` and `duration`: **the record points; it does not duplicate.**
   ⚠️ **Write `params.source_version`.** **The specification is corrected after generation
   (§20 exists for that)** — so **the path stays the same while the contents change**, and a
   path alone cannot say which text was fed.
   ⚠️ **This field does not exist on the image path** — an image specification holds no §19,
   so it has no version to freeze.
10. **`verdict` — the three layers.** `machine` (deterministic), `adherence` (spec
    conformance), `council` (evaluators). ⚠️ **Judgment and measurement are not separated in
    `machine`** — a measured number is itself the material of a judgment, and splitting them
    would add a distinction that carries no information.
11. ⚠️ **Do not write `adopted: true`.**
12. **Run it again.**

⚠️ **Step 11 is the boundary of this stage, and it is not a formality.** **Adoption is
selection, and the author is the editor.** Writing `adopted: true` here is **worse than writing
nothing**: the checker reads what is written, so **an adoption written by a session becomes an
adoption the checker believes.** ⚠️ **`L25` fires on two or more `adopted: true` for one
`(shot, kind)`**, and its message says it plainly — **if there are two, selection has not
happened yet.** **Leave the field out, and the absence is the record.**

## ⚠️ What is still red when this stage ends

⚠️ **This is the last stage in this repository's body — ⑤ selection, ⑥ assembly and ⑦
acceptance are not in it.** So the honest statement is not "what is red" but
**"what has no reader yet."**

| What remains, and why | |
|---|---|
| **`L25`'s take-vs-real comparison** | it needs the media, and **the foundation does not open `media/`** — the declaration in `projects/hitosara/media/README.md` says so, and `L25` honoured it |
| **⑥ and ⑦** | **there is no code for them in this repository's body** — the timeline and the acceptance record exist as schemas and as prose |
| **`timeline/`** | ⚠️ **`Project` does not open it at all** — so nothing reads the order, and **nothing checks that a clip's `take` index resolves to a take that exists** |

⚠️ **The note `L25` prints is the honest report** — how many takes were read, and how many are
written as adopted. **Read it: it says in its own words that it is not judging good or bad.**

## ⚠️ Fields and rules that nobody reads

⚠️ **Write these down as holes. Do not fill them in with a rule.**

- ⚠️ **`params.references` is written on no take — what was actually attached is recorded
  nowhere.** `attached` is **a declaration**, and `L6` compares the ledger's `reference_set`
  against it — **not against the fact of attachment.** **The real thing has no record.**
  ⚠️ **Fill the field and the hole closes; fill it by copying `attached` and `L6`'s distinction
  collapses into reading the same thing twice** (the same failure `L9` names).
- ⚠️ **`L25` does not open `media/`, and a name is a name, not a proof.** The declared count and
  the number of files **do not agree**, for two reasons, and **a machine fires on neither**:
  **① placed but no record** (invisible, because `media/` is not read) and **② the file the
  record names is already gone** (unnoticed, because existence is not confirmed).
  ⚠️ **Do not write the numbers here — numbers move, and written numbers contradict.**
  ⚠️ **Closing this hole means changing that declaration first, and that is undecided.**
- **An image take has no other side to match against.** An image specification holds no §1 — it
  names neither resolution nor duration — **so there is no value for the record's side to
  compare.** The comparison is not skipped; **it has no counterpart.**
- **`take.file: null` means "not placed yet", not empty.** The field is nullable for exactly
  that distinction, and the two must not be given the same face.
- ⚠️ **What belongs in `params` differs per provider, and how to normalise it while keeping
  model-independence is undecided.** ⚠️ **Do not settle it here** — a normalisation invented by
  one session becomes a shape every later take is measured against.
- **`verdict.council`:** **which evaluators are called differs by role**, and whether the
  role-to-evaluator map belongs here or in a separate table **is undecided.**
- ⚠️ **Nothing reads `timeline/`.** `Project` does not open it, so **the order of the clips is
  not read by anything** — the checker falls back to the natural order of the shot ids, and
  `Project.order()`'s own docstring says that when `timeline/` arrives **that should be treated
  as authoritative (undecided).**
- ⚠️ **`clips` is by definition the list of adopted takes, and not one video take has
  `adopted: true`.** **So a timeline of video clips cannot be written now** — the schema requires
  only `shot` and `take`, but **the record of which samples were lined up, in which order, is not
  on the record side.** ⚠️ **This is not "it cannot be written" but "it cannot be moved"** —
  ⚠️ **and a Skill that emits an empty timeline is worse than no Skill at all.**
  The hole is already written where it happened — read
  [`projects/hitosara/renders/README.md`](../../projects/hitosara/renders/README.md) before
  proposing ⑥.

## ⚠️ What the checker does not decide here

- **Whether the take is any good.** `L25` compares **measured values against the record and the
  specification** — it never judges the image. ⚠️ **It does not open `media/`**, so
  **a discrepancy between the record and the actual object does not fire.**
- **Whether to adopt.** **Adoption is the author's act**, and this layer only **reads what is
  written.**
- **Whether the seed should be reproduced.** `params.seed` is preserved so that a take **can** be
  regenerated — not because it will be.

## Language

- **`params.source` points at the canonical, and the canonical is English.** The string that was
  fed in is English and **must not be translated** — translating changes the output.
  ⚠️ **Do not write a translation of it here either** — **a translation is a copy, and copies
  diverge.**
- **`failure_type` and the record's free text may be Japanese.** They are records, not strings
  handed to a generator. **The question is never "is this Japanese," it is "does this string
  arrive."**
- **The canonical of the documents is English**, and the mirrors sit beside it in the same
  directory — see [`CLAUDE.md`](../../CLAUDE.md).

## Where to read more

- [`schemas/take.schema.json`](../../schemas/take.schema.json) — the sample's form, and the reason each field exists
- [`schemas/shot-record.schema.json`](../../schemas/shot-record.schema.json) — the paste unit, field by field
- [`projects/hitosara/takes/README.md`](../../projects/hitosara/takes/README.md) — takes of a real work, and **which fields are written and which are not**
- [`projects/hitosara/renders/README.md`](../../projects/hitosara/renders/README.md) — **where the hole after this stage is written down**
