---
name: ledger
description: 'Stage ③ of semantic-visual-loom — the production ledger, which fixes what is fixed. Use when a shot has to be told what it may show, or when continuity and disclosure have to be held in one file. Grows the continuity vocabulary, declares the disclosure change points, and derives the reference and forbidden sets per shot. Emits the ledger and the derived sets on each shot record — not the staging, and not the selection.'
argument-hint: '(optional) the project name. e.g. /semantic-visual-loom:ledger hitosara'
---

<!-- i18n-version: 1.0.0 | canonical: skills/ledger/SKILL.md | translated: 2026-09-14 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# ledger — ③ the production ledger

**Independent generations have no memory of each other.** So the state is placed outside the
generation, in one file, and **the reference set and the forbidden set are derived from that one
point.** This stage is where the derivation happens.

⚠️ **This is a document, not a program.** It instructs a session. **There is no code for
stage ③ in this repository** — the only command that runs is the checker, and it runs against
**the ledger and the records this stage writes.**

## What this stage owns

| | What | Where |
|---|---|---|
| **the continuity vocabulary, grown** | `characters:` / `locations:` / `props:`, and each `states:` | `projects/<name>/ledger.yaml` |
| **the disclosure change points** | `disclosure:` — keyed by `shot`, each with `negative:` | `projects/<name>/ledger.yaml` |
| **the derived sets, per shot** | `reference_set` · `forbidden_set` | `projects/<name>/shots/<id>.yaml` |
| **the declaration of what was attached** | `attached` | `projects/<name>/shots/<id>.yaml` |
| **the record's copy of the state** | `disclosure_state` | `projects/<name>/shots/<id>.yaml` |

⚠️ **The continuity ledger and the disclosure ledger are one file.** Continuity is the state of
the world; disclosure is the state of the audience's knowledge. **The failure that actually
happened was "which reference image to attach to which shot"** — and that judgment is at once a
judgment of continuity and a judgment of disclosure. **Do not split it in two.**

⚠️ **① opened the vocabulary; ③ grows it and then derives.** The keys do not come from the
shot — they come from the ledger, and **`known_keys()` derives them from exactly three places**
(see step 1). **A key that is not in the ledger is a thing that does not exist**, being pinned.

## The order of decisions

⚠️ **This order is a design claim; the checker does not enforce it.** The layers run in an
order of their own. What follows is the order that **makes a thing exist before something
derives from it.**

1. **`characters:`** — `identity` is required, plus `states:` (`wardrobe` · `constant` ·
   `note`) and `negatives:`.
   ⚠️ **A character contributes exactly five key families**, and no more:
   the bare name, `.sheet` (**the same thing as `.identity`**), `.identity`, `.negatives`, and
   `.states.<name>` for each state. A location contributes the bare name, `.base`,
   `.geography`, `.states.<name>`. A prop contributes the bare name, `.appearance`, `.negative`.
   **Memorise this list or read `known_keys()` — do not invent a key.**
2. **`locations:`** — `base` is required. ⚠️ **`geography` is the one that is attached to every
   shot** — it carries the spatial relation, and a generator that does not know where things
   stand cannot place them.
3. **`props:`** — `appearance` and `negative`. ⚠️ **Nothing here is `required`** — a prop may be
   a bare name with no fields at all.
4. **`disclosure:`** — **change points only**, keyed by `shot`.
   ⚠️ **Do not list every shot.** Between change points the previous state continues.
   ⚠️ **Why the coordinate is a shot id and not a range:** the coordinate of disclosure is **the
   order of the clips**. Measured across 30 takes, **two of the four reveals happen mid-chapter**,
   so a range cannot express them. **Both of the alternatives fell** — writing the coordinate as
   `at` × clip, and enumerating `Segment ID`s — because both try to write *which shot* in the
   ledger's own coordinates.
   **Fires if wrong:** `L7a` (a shot before the declared change point already holds that value) ·
   `L7b` (at the change-point shot, the state has not actually changed) · `L9` (the check is empty).
5. **`negative:` on every change point** — `changed` or `covered`.
   **Fires if wrong:** `L10`. ⚠️ **The other party is §18, not §16.** Of the 20 sections, **only
   §18 `Negative Prompt` reaches the model** — §16 is a note for people to read and holds not one
   block. **Apply a tool that makes blocks to a document that holds no blocks and it will always
   approach "one block per take."** ⚠️ **`negative:` is a reserved key** — a change point is a bag
   of attributes, so an unreserved `negative` would read as a disclosure attribute.
6. **Derive `reference_set`** — every key in it must be in `known_keys()`.
   **Fires if wrong:** `L8`. ⚠️ **`L8` checks `attached` too**, against the same set.
7. **Derive `forbidden_set`** — ⚠️ **and it must not intersect the reference set.**
   **Fires if wrong:** `L5`. **Which one wins is decided by the generator, and you must not let
   it decide.** That is a design mistake, not a generation failure.
8. **Write `attached` — knowing it is a declaration, not a record.**
   **Fires if wrong:** `L6`. ⚠️ **"There is no record" and "it contradicts" are different.**
   A shot with **no `attached` field at all** is not a contradiction — **there is no record**,
   and the cause cannot be traced (what cannot be read cannot be traced back). Writing
   `attached: []` fires "the intent has one but none was attached" and **that is a falsehood.**
   **A blank is a claim, not a fact.**
   ⚠️ **The reference sheet declares its own wardrobe** — measured, **the clothing in a
   reference image wins over the text.** So an extra attachment is not harmless.
9. **`disclosure_state` — the record's copy of the state.**
   **Fires if wrong:** `L7a` · `L7b` · `L9`.
10. **Run it — and then run `L9`'s question on yourself.**

```bash
python3 engine/ledger/check.py projects/<name>   # read the violations AND the notes
python3 engine/ledger/check.py --self-test       # confirm the checker fires at all
```

⚠️ **Step 10 is the one that is easy to skip.** `L9` counts transitions: **if every transition
the record holds matches a declared position in the ledger, that record has said nothing new
against the ledger** — you cannot tell whether it was copied or read independently.
**Hold a transition that is not in the ledger and the record is saying something new.**
⚠️ **This note does not go away when you read the same source text again.**
**Agreement is not evidence of independence** — and **`L9` is the check that doubts the
correctness of the other checks.**

## ⚠️ What is still red when this stage ends

⚠️ **This is the last stage of the foundation's own body, so zero violations becomes reachable
here** — and that is exactly why this table matters. **"Reachable" is not "achieved."**

| Expected red at exit, and whose it is | |
|---|---|
| `L25` | **④ sampling and ⑤ selection are not in this repository's body** — nothing has been generated, so the take-vs-real check has nothing to confirm |
| `L6` · `L10` · `L14` | **not "still red" but "may fire"** — they fire on a real gap in an existing artifact, and each one names a specific record that is missing or a change that does not return |

⚠️ **`L6` firing is not a stage failure.** A shot with no `attached` field is **a record that has
not been written** — and the checker reports what you did not write. **Read the note beside it
before treating it as a contradiction.**

## ⚠️ Fields and rules that nobody reads

⚠️ **Write these down as holes. Do not fill them in with a rule.**

- ⚠️ **A prohibition can be written only at the unit of a tool, while a disclosure can be
  written at the unit of a part.** `known_keys()` gives a prop exactly `P.appearance` and
  `P.negative` — so `forbidden_set: [KAMADO]` forbids **the thing called the kiln, whole.**
  But the disclosure ledger handles **the part** `KAMADO.interior`: shot 07 **may photograph the
  door, but may not photograph the light through the gap.** **There is no field to write this
  asymmetry in.** Today the distinction is carried by `disclosure_state` and by prose on the
  specification side. **Record the hole; do not invent a field** — a machine-readable form that
  nothing reads is worse than prose a person reads.
- ⚠️ **No check reads the disclosure series on the image-prompt side.** What `L10` and `L14`
  face is **§18, not the image prompt.** But the image specifications hold **the same series**,
  and it opens at the same place. **The ledger declares where it drops, and nothing reads it.**
  ⚠️ **`L21` does not pass through here** — `L21` looks at whether the image **covers the work's
  prohibitions**, not whether the series opens at the ledger's position, because that **differs
  from shot to shot** (hence "cover, not equal"). **The other party is the handover layer.**
  Until then, **what a machine does not read, keep in a form a person can read.**
- ⚠️ **`no_record` is set by `L6` and read by nobody.** The finding carries
  `no_record=True` for "the record is missing," and **the reporter drops it** — it prints
  violations and notes, and this is neither. So **"there is no record" currently counts in the
  same bucket as "it contradicts"**, which is the exact confusion the design set out to avoid.
  ⚠️ **The marker exists and the report does not use it** — record that; **do not add a second
  marker beside it.**
- ⚠️ **Do not make `at` a key.** §16's headings name a range, but the body writes the
  prohibitions of **this one take**, so the forbidden set splits in **9 of the 10 ranges**.
  **It is a grouping for people to read, not a key.**
- **Who writes the ledger is undecided.** The continuity vocabulary must exist before ② writes
  `place` and `time`, while the disclosure series is written late — so **if it must be one
  stage, it splits inside ①.** ⚠️ **Record the dependency; do not settle the assignment.**
  (① carries the same hole from the other side — read both before deciding.)
- **Whether a state transition is declared in the ledger or written per shot is undecided.**
  The schema says so itself: whether "who changes clothes when" goes in the ledger or is written
  every time on the shot record side **is not decided.**
- **Wardrobe resolution is not machine-readable.** Which `states.<name>.wardrobe` applies is
  resolved from **`place` × `time`** — **not from time.** Deriving it from prose produces false
  positives (a classroom at night, a school-festival yard at night, a room at dawn: **"night, yet
  in uniform"** and **"not day, yet in pyjamas"**). **The conditions are confirmed against the
  artifact side.** Record the reading; do not write a rule.
- **Whether a character's knowledge belongs in the ledger is undecided.** A change point is a
  **bag of attributes** (`additionalProperties: true`) and `disclosure_state` is an open object
  — **so an attribute may be anything, and nothing constrains the vocabulary.** ⚠️ **Nothing
  should, yet** — the vocabulary is what the work turns out to need, and it is discovered by
  measuring a work, not by enumerating one in advance.
- **A take is where the attachment is actually recorded, and `take.params.references` is empty.**
  So `attached` is a declaration checked against **another declaration**. ⚠️ **The real thing is
  not what is compared here** — and the layer that would compare it (the handover sheet) does not
  exist. **`L25` reports the take side as `takes/` being empty, and it is a report, not a check.**

## ⚠️ What the checker does not decide here

- **Whether the disclosure timing is right.** The checker sees whether a transition **matches a
  declared position**, never whether that position is the right one to reveal at. **That is the
  work's design, and it is not machine-readable.**
- **Whether the reference set is the right set.** `L5`, `L6` and `L8` see exclusivity,
  agreement and resolvability — **never whether those are the right things to pin.**
- **What the work's prohibitions should be.** `bible.negative_base` is a judgment about the
  work, written in ①.
- **Whether a rewording is a change.** When a section disappears and a rewording of it remains
  forever after, `L14` fires — **it does not decide whether the two are the same prohibition.**
  Decide it and you get the same false positives as `L4`: **a detector tuned to one work's
  vocabulary fires on the next work.**

## Language

- **The ledger's invariant blocks are English.** `negatives:` on a character, `negative:` on a
  prop, everything that will be handed to a generator — **written in English, not translated.**
- ⚠️ **The change points' attribute names are the record's, and the record may be Japanese.**
  `unit.before` and the like are records. **The question is never "is this Japanese," it is
  "does this string arrive"** — and `forbidden_set` **arrives** (it goes to the Negative
  Prompt), while a `disclosure_state` **does not**.
- **The canonical of the documents is English**, and the mirrors sit beside it in the same
  directory — see [`CLAUDE.md`](../../CLAUDE.md).

## Where to read more

- [`engine/ledger/README.md`](../../engine/ledger/README.md) — every layer, what it reads, and **what it does not see**
- [`schemas/ledger.schema.json`](../../schemas/ledger.schema.json) — continuity and disclosure, in one file
- [`docs/usage.md`](../../docs/usage.md) — the commands, and how to read the exit code
- [`projects/hitosara/README.md`](../../projects/hitosara/README.md) — a work that went through all of this
