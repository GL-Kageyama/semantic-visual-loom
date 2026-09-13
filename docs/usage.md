<!-- i18n-version: 1.0.0 | canonical: docs/usage.md | translated: 2026-09-14 -->

**Language:** [English](usage.md) | [日本語](usage-ja.md) | [中文](usage-zh.md)

# Usage

How to run pre-flight verification over a project's records.

**Only one thing runs here.** Generation does not run inside this foundation—
**the author runs generation by hand, and the foundation reads the records.**
What runs is the check that fires contradictions at the specification stage,
**before anything is generated** (and, afterwards, the matching of what came back).

## Requirements

`python3` and PyYAML. **There is no install step.**

```bash
python3 -m pip install --user pyyaml
```

## The commands

```bash
python3 engine/ledger/check.py --self-test                 # does the checker fire at all
python3 engine/ledger/check.py projects/hitosara           # pre-flight verification for one project
python3 engine/ledger/check.py projects/ukebi/ukebi-v2     # Ukebi V2
python3 tools/check_i18n.py                                # the document mirrors
```

| flag | |
|---|---|
| *(positional)* | the path to a project directory. Required unless `--self-test` is given. |
| `--schemas` | the schema directory. Defaults to `<repo>/schemas`. |
| `--self-test` | takes no project. Exits `0` when every case behaved as expected. |

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

⚠️ **`projects/ukebi` and `projects/gozen-niji` are raw specification trees, not
projects.** They hold no `bible.yaml` / `ledger.yaml` / `shots/`, so running the
checker over them reports **"読めていない"** and `L0` fires **"there is not a single
shot; the check is looking at nothing."** That is the correct behaviour, not an error.

## The layers

The check is **26 layers, `L0`–`L25`**, plus schema-shape validation.
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

## Where to read more

| | |
|---|---|
| [`README.md`](../README.md) | what this foundation is, and what it is made of |
| [`engine/ledger/README.md`](../engine/ledger/README.md) | the production ledger, the layers, and what each check does not see |
| [`schemas/README.md`](../schemas/README.md) | the data structures |
| [`projects/hitosara/README.md`](../projects/hitosara/README.md) | the demo—10 shots, independent of Ukebi |
