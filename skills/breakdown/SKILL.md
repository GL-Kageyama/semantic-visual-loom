---
name: breakdown
description: 'Stage ① of semantic-visual-loom — cut a work into shots. Use when a project starts, or when a story, plot, or draft has to become a shot list. Opens bible.yaml, opens the continuity vocabulary of ledger.yaml, cuts at the unit of one change, and gives each shot a role from the registry. Emits the shot list, the work ledger, and the disclosure change points — not the staging, and not the reference sets.'
argument-hint: '(optional) the project name, or the work to break down. e.g. /semantic-visual-loom:breakdown hitosara'
---

<!-- i18n-version: 1.0.0 | canonical: skills/breakdown/SKILL.md | translated: 2026-09-14 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# breakdown — ① cutting a work into shots

**One shot exists for one change.** That is this foundation's fixed policy, and this stage is
where it is carried out. **A work is cut at the unit of one change**, and each piece is given
a role.

⚠️ **This is a document, not a program.** It instructs a session. **There is no code for
stage ① in this repository** — the only command that runs is the checker, and it runs against
**the records this stage writes.**

## What this stage owns

| | What | Where |
|---|---|---|
| **the work's ledger** | `style`, `world.rules`, `world.visual_language`, `constants`, `negative_base` | `projects/<name>/bible.yaml` |
| **the continuity vocabulary** | `characters:` / `locations:` / `props:`, and each `states:` | `projects/<name>/ledger.yaml` |
| **the shot list** | `shot`, `unit.before` / `unit.after`, `role`, and the order | `projects/<name>/shots/` |
| **the disclosure change points** | `disclosure:` — a series keyed by `shot` | `projects/<name>/ledger.yaml` |

**It does not own** `place` / `time` / `mode` / `motion` / `beats` / `duration` or either
specification document (those are **② `design`**), and it does not own `reference_set` /
`forbidden_set` / `attached` / `disclosure_state` (those are **③ `ledger`**).

⚠️ **The two ledgers are one file.** Continuity and disclosure are held together
(`CLAUDE.md`, "The production ledger is one"). **Do not split it in two.**

## The order of decisions

⚠️ **This order is a design claim; the checker does not enforce it.** The layers run in an
order of their own, and `L15` (role) and `L24` (mode) run **last, over the whole project** —
they are not gates you pass on the way through. What follows is the order that **makes the
data exist before something needs it.**

1. **The work's ledger first** — `bible.yaml`. `style` names a card that lives in
   `distill-essence-engine`, and `negative_base` is **the work's prohibitions**: every image
   specification downstream is measured against this list.
   **Fires if wrong:** `L17` (`bible.style` empty) · `L21` · `L20`.
2. **The continuity vocabulary** — `characters:` / `locations:` / `props:` and their `states:`.
   ⚠️ **This is not bookkeeping — it is what makes everything after it nameable.**
   `known_keys()` (`check.py`) derives the reference keys from **exactly here**, and **`L2`'s
   own message says so**: split the shot, or add the place to the ledger. With no vocabulary
   there is nothing for `place` to be drawn from and nothing for `reference_set` to pull.
   **Fires if wrong:** `L8` (a reference key that is not in the ledger).
   ⚠️ **Nothing checks that `place` is a `locations:` key.** That is a **data dependency, not
   a fired rule** — `L2` fires only on **more than one** place in the field.
3. **Cut at one change** — per shot, `unit.before` and `unit.after`.
   **Fires if wrong:** `L1` (both sides the same = that shot causes nothing) · `L0` (0 shots).
4. **Take the identity from the specification side** — `shot` is §19's `Instance ID` with the
   trailing `-<seconds>s-<take>` dropped. ⚠️ **Not from `Segment ID`** — the same range carries
   two spellings there, and deriving naively drops records (`L13` reports it as a note).
   **Fires if wrong:** `L13`.
5. **Give each shot a role** — from `rolemap.ROLES`, **15 names**. ⚠️ **The registry is open**:
   meet a name that is not in it and **define it on the spot, then register it** — `総覧` /
   `語り` / `離脱` came out of measurement that way.
   **Fires if wrong:** `L15`.
6. **Write the disclosure change points** — `disclosure:`, keyed by `shot`.
   ⚠️ **Change points only — do not list every shot.** Between change points the previous
   state continues. **Fires if wrong:** `L7a` · `L7b` · `L9` (every transition matches a
   declared position — **agreement is not evidence of independence**).
7. **Run it.**

```bash
python3 engine/ledger/check.py projects/<name>   # read the violations AND the notes
python3 engine/ledger/check.py --self-test       # confirm the checker fires at all
```

## ⚠️ What is still red when this stage ends

⚠️ **Zero violations is not this stage's exit condition.** ① and ② write **the same artifact**,
so the checker is **red in the middle** — and it is supposed to be. **What tells you this stage
went wrong is not the count; it is which layers are quiet.**

| Expected red at exit, and whose it is | |
|---|---|
| `L11` · `L16` · `L17` · `L18` · `L21` · `L22` · `L23` · `L24` | **② `design`'s** — nothing has been staged or specified yet |
| `L5` · `L6` · `L7a` and `L7b` beyond the declared points · `L8` | **③ `ledger`'s** — the sets are derived there |
| `L25` | **nothing has been generated** — and this stage does not generate |

⚠️ **Run `--self-test` and read why it exists.** It proves the checker fires at all
(**213 examples**). **A check that reports nothing looks the same as a check that passed** —
and the self-test is the only thing that tells the two apart.

## ⚠️ Fields and rules that nobody reads

⚠️ **Write these down as holes. Do not fill them in with a rule.**

- **The shape of this stage's input is undecided.** Nothing in this repository says whether a
  work arrives as a plot, a script, or a novel. **Read it with a person or with a session, and
  record the shape you read.**
- **The shot list has no schema.** `SCHEMAS` holds `shot-record`, and it **requires
  `duration`** — which ② decides. **So ① cannot emit a valid shot record.** Keep the list in
  the form you keep it in, and know that **the checker reads nothing until ② is on disk.**
- **A role's default mode (`既定モード`) is read by nobody.** `rolemap.py` states it,
  `grep 既定モード engine/ledger/*.py` returns **only the definition**, and there is not even a
  note. ⚠️ **So "the role decides the default mode" is a principle with no reader.**
  Do not invent the rule. Note also that **`()` means *any* and `None` means *undecided*** —
  **do not let the two wear the same face.**
- **The canonical spelling of a qualified role is undecided.** `運動（停止）` resolves, and
  `L15` reports it **as a note**. Whether the registry's plain name or the qualified one is
  canonical **is not decided** — **do not settle it here.**
  ⚠️ Only `運動` accepts a qualifier (`rolemap.QUALIFIABLE`).
- **Who writes the ledger is undecided.** The continuity vocabulary has to exist before ② can
  write `place` and `time`, while the disclosure series is written late — so **if it must be
  one stage, it splits inside this one.** ⚠️ **Record the dependency; do not settle the
  assignment.**
- ⚠️ **A role is declared as a card and is a Python dict.** `CLAUDE.md` says a role "is
  registered as a card, and it grows and is refined" — **the registry is `ROLES` in
  `rolemap.py`**, while the format and style cards live in `distill-essence-engine`, which this
  repository **reads but never rewrites.** **No card exists for a role yet.** Record the gap —
  **do not add a second registry beside the one that is read.**

## ⚠️ What the checker does not decide here

- **Whether the change is the right change.** `unit` is free text — `L1` asks only whether the
  two sides are equal after normalisation. **Making them a pair and being able to check the
  pair are two different things.**
- **Whether a role fits a shot.** `L15` sees whether the value **resolves**, never whether it
  is right. An unused role is reported **as a note** — **that is a property of the work, not a
  defect in the registry.**
- **What the work's prohibitions should be.** `negative_base` is a judgment about the work.

## Language

- **`role` values are Japanese.** They are **not strings that reach the generator** (§1–20 has
  no field for them, so they never appear in the text the model sees), which is why the
  registry's `dialogue` and `establishing` are **notes for reading, not half of the spelling.**
- **The strings that reach the generator are English.** Specifications, prompts and Negatives
  are written in English and **must not be translated** — translating changes the output.
  ② is where that bites; **it is stated here because it is the reason `role` is exempt.**
- **The canonical of the documents is English**, and the mirrors sit beside it in the same
  directory — see [`CLAUDE.md`](../../CLAUDE.md).

## Where to read more

- [`engine/ledger/README.md`](../../engine/ledger/README.md) — every layer, what it reads, and **what it does not see**
- [`schemas/ledger.schema.json`](../../schemas/ledger.schema.json) — continuity and disclosure, in one file
- [`docs/usage.md`](../../docs/usage.md) — the commands, and how to read the exit code
- [`projects/hitosara/README.md`](../../projects/hitosara/README.md) — a work that went through all of this
