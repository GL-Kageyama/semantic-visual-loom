<!-- i18n-version: 1.1.0 | canonical: docs/usage.md | translated: 2026-09-18 -->

**Language:** [English](usage.md) | [日本語](usage-ja.md) | [中文](usage-zh.md)

# Usage

How to run pre-flight verification over a project's records.

**Generation does not run inside this foundation**—**the author runs generation by
hand, and the foundation reads the records.** What runs is the check that fires
contradictions at the specification stage, **before anything is generated** (and,
afterwards, the matching of what came back), plus the tool that prints the lines of a
specification **whose value is already forced.**

## Requirements

`python3` and PyYAML. **There is no install step.**

```bash
python3 -m pip install --user pyyaml
```

## The commands

**Three commands ship here**—**two for making a work, one for maintaining the
repository.**

```bash
# the checker — fires contradictions at the specification stage
python3 engine/ledger/check.py --self-test                 # does the checker fire at all
python3 engine/ledger/check.py projects/hitosara           # pre-flight verification for one project
python3 engine/ledger/check.py projects/ukebi/ukebi-v2     # Ukebi V2

# the printer — the lines of a specification that can be derived. It writes nothing
python3 engine/shot/print_spec.py projects/hitosara
python3 engine/shot/print_spec.py projects/hitosara --shot hitosara-ch01-seg04

# the repository's own document check — not used to make a work
python3 tools/check_i18n.py                                # the document mirrors
```

**`engine/ledger/check.py`**

| flag | |
|---|---|
| *(positional)* | the path to a project directory. Required unless `--self-test` is given. |
| `--schemas` | the schema directory. Defaults to `<repo>/schemas`. |
| `--self-test` | takes no project. Exits `0` when every case behaved as expected. |

**`engine/shot/print_spec.py`**

| flag | |
|---|---|
| *(positional)* | the path to a project directory. |
| `--shot` | print one shot only. |

⚠️ **The two are not alternatives—they cover disjoint ground.**
**A line `print_spec.py` prints is a line that goes silent the moment you copy it**
(that is why each printed line names the check it silences). **So `check.py` can never
report those lines.** Conversely, **everything `check.py` fires on is something
`print_spec.py` refused to derive.**
⚠️ **Run the printer for the forced lines, and the checker for everything the printer
refuses**—neither one covers what the other does.

⚠️ **`engine/shot/print_spec.py` writes nothing**——it reads the record, the ledger and the bible,
and prints **only the lines whose value is already forced** (§1's four work constants, `Duration`,
and §19's `Instance ID`). ⚠️ **Pasting them is the author's act.** Where it disagrees with the
specification on disk it prints **both** and stops. What it does not derive, and the holes it
leaves, are in [`engine/shot/README.md`](../engine/shot/README.md).

⚠️ **The four skills in `skills/` are not commands**——**they are instructions to a Claude Code
session**, and **they are what turns a story into the specifications.** See **The four stages**
below.

## The four stages

**A story goes in. The strings a generator is handed come out.**
⚠️ **None of the four is a program**——each is a document that instructs a session, and
**there is no code for them in this repository.** The one thing that runs is the checker.

| stage | you hand in | it emits | where it lands |
|---|---|---|---|
| **① breakdown** | a story, a plot, a draft | the shot list, the work ledger, and the disclosure change points | `bible.yaml`, `ledger.yaml`, `shots/` |
| **② design** | one shot | the staging record, the §1–20 video specification (**§18's seven slots**), and the image specification | `shots/<id>.yaml`, `specs/video/<id>.md`, `specs/image/<id>.md` |
| **③ ledger** | one shot | the ledger grown, and the derived sets on each shot record | `ledger.yaml`, `shots/<id>.yaml` |
| **④ shot** | what came back | the self-contained record, and the take ⚠️ **it does not adopt** | `shots/<id>.yaml`, `takes/<id>-<kind>-<n>.yaml` |

**② is where the prompt is written.** The seven slots are `Master` / `Visual` / `Motion` /
`Camera` / `Audio` / `Negative` / `Style Motion`——**all English**, and **being separated is
itself the point** ([`references/video-spec.md`](../references/video-spec.md) §18).
⚠️ **They are fed separately, and only §18 is fed**——§19 and §20 are our own record.

⚠️ **The invocation carries a namespace**——`/semantic-visual-loom:breakdown`, `:design`,
`:ledger`, `:shot`.

⚠️ **The shape of ①'s input is undecided.** Nothing in this repository says **whether a work
arrives as a plot, a script, or a novel**——read it with a person or with a session, and record
the shape you read.
⚠️ **And the shot list has no schema**: `shot-record` requires `duration`, **which ② decides**,
so **① alone cannot emit a record the checker can read.** ⚠️ **The checker reads nothing until
② is on disk.**

⚠️ **Two stages are not among them (⑥ structure, ⑦ acceptance)**——**the input is not on the
record side**: `clips[]` is by definition a list of adopted takes, and **not one video take
carries `adopted: true`.** ⚠️ **They cannot be moved**, and **a skill that emits an empty
timeline is worse than no skill.** The reason is in
[`projects/hitosara/renders/README.md`](../projects/hitosara/renders/README.md).

## ⚠️ Read the exit code correctly

| exit | meaning |
|---|---|
| **`0`** | no **violations** |
| **`1`** | violations were found |

⚠️ **`0` is not "correct."** The report also carries **notes**—things that were read
but are not violations—and **what the check did not look at.**
**A check that reports nothing looks the same as a check that passed.**
Read the notes and the unchecked range, not only the count.

## What a project is

`check.py` takes the path to a **project directory** and reads it.
**It writes nothing, and it does not open `media/`.**

```
projects/<name>/
├── bible.yaml      # the world, its root laws, its visual language (required)
├── ledger.yaml     # continuity + disclosure, in ONE file (required)
├── shots/          # one shot record per shot, <id>.yaml (required)
├── takes/          # the record of what came back
├── specs/          # the §1–20 documents (video/ and image/)
├── media/          # where generated output goes   ⚠️ THE FOUNDATION DOES NOT OPEN THIS
├── renders/        # what editing produced (the work)
└── timeline/       # the edit
```

The checker reads `bible.yaml`, `ledger.yaml`, `shots/`, `takes/`, and **the
specification documents the shot records point at** (`spec:` and `key_image:`).

⚠️ **A missing `bible.yaml`, `ledger.yaml`, or `shots/` is reported, not silently
treated as empty.** And **one unreadable file does not stop the run**—stopping would
let **one broken file hide every other report.**

⚠️ **`media/` and `takes/` are separate.** A place and a record—**placing something
is not recording it.** So a state is possible in which a file sits in `media/` and has
no take. **Because the checker does not open `media/`, a discrepancy between the record
and the actual object does not fire**—that is a hole, and it is reported as one.
**If `takes/` is empty, the report says "there is not a single take record." Zero is not a pass.**

⚠️ **`projects/` holds two kinds side by side**—**raw specification trees** and
**structured records** (`bible.yaml` / `ledger.yaml` / `shots/`).

⚠️ **`projects/ukebi` and `projects/gozen-niji` are raw specification trees, not
projects.** They hold no `bible.yaml` / `ledger.yaml` / `shots/`, so running the
checker over them reports **"読めていない"** and `L0` fires **"there is not a single
shot; the check is looking at nothing."** That is the correct behaviour, not an error.

⚠️ **No generated output is placed beside the raw trees**—**only the records and the
specifications.** **Old generated output lowers the work's degree of quality uniformity.**

⚠️ **Their `reference/` assets are kept** (**9 distinct images**, copied into each segment).
**They are not generated output but input**—and **the only record of "which segment had what
attached to it"** (`wan-full-spec.md` names its references only as `REF_STYLE` / `REF_SOURCE`).
⚠️ **Delete them, and the record of attachment goes with them.**
The counts behind that are in `HISTORY.md`.

⚠️ **`renders/` is where editing output—the work—goes; `media/` is where samples go.**
**Samples and works are separated by place**—they cannot be separated by name.
⚠️ **The emptiness of `timeline/` is not even reported**, because nothing opens it yet:
**a check that reports nothing looks the same as a check that passed.**

## The layers

The check is **28 layers, `L0`–`L27`**, plus schema-shape validation.
**They are not one verdict**—each layer fires on its own and is reported with the
number it saw.

⚠️ **A layer that sees nothing is reported as a note, and a layer that sees nothing
looks exactly like a layer that passed.** For example, a layer about `key_image`
cannot fire on a project whose takes hold no `key_image`—**there is no other side to
compare against.** **Zero is not evidence that the layer agreed.**

**The layers are documented in [`engine/ledger/README.md`](../engine/ledger/README.md)**—
what each one reads, what it fires on, and **what it does not look at.**

## The schemas

| file | what it is the canonical of |
|---|---|
| `bible.schema.json` | the world, its root laws, its visual language |
| `ledger.schema.json` | continuity + disclosure, held in one file |
| `shot-record.schema.json` | one shot |
| `take.schema.json` | what came back from one generation |
| `timeline.schema.json` | the edit ⚠️ **its name is in the `SCHEMAS` constant, but no one reads it yet** |

See [`schemas/README.md`](../schemas/README.md).

## The document check

```bash
python3 tools/check_i18n.py --self-test   # firing and non-firing examples for each rule
python3 tools/check_i18n.py               # the real thing
```

⚠️ **It reports how many files it looked at and which blocks it treated as invariant**—
without that, **a check that saw nothing looks like a check that passed.**
⚠️ **It does not see whether the prose is translated correctly**—if the meaning
contradicts, it still passes as long as the lines and headings agree.

⚠️ **The scheme it checks**: the canonical carries **no suffix**, and the mirrors use the
**suffix scheme in the same directory** (`README.md` / `README-ja.md` / `README-zh.md`).
**No `-en` mirror is created**, because the canonical is English.
⚠️ **The subfolder scheme (`ja/` `zh/`) is not used**—so that **the depth of the canonical
and the mirrors does not change.**
⚠️ **The working language of development stays Japanese** (commit messages, `HISTORY.md`,
conversation) **while the canonical of the documents is English.** These two are different
things: one is the language the work is done in, the other the language the documents are
authoritative in. **16 documents × 3 languages are in place** (the count
`tools/check_i18n.py` reports as canonical), and the rules are in
[`CLAUDE.md`](../CLAUDE.md).

## Where to read more

| | |
|---|---|
| [`README.md`](../README.md) | what this foundation is, and what it is made of |
| [`engine/ledger/README.md`](../engine/ledger/README.md) | the production ledger, the layers, and what each check does not see |
| [`engine/shot/README.md`](../engine/shot/README.md) | what the printer derives, and the seven holes it leaves |
| [`schemas/README.md`](../schemas/README.md) | the data structures |
| [`projects/hitosara/README.md`](../projects/hitosara/README.md) | the demo—10 shots, independent of Ukebi |
