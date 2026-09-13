<!-- i18n-version: 1.0.0 | canonical: README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# semantic-visual-loom

**A foundation that carries an AI-generated story all the way to film.**

> **Footage is not generated. It is edited.**

What the generative model makes is a **sample**. **What turns it into a work is editing.**
So what this foundation holds is not a generator but the **process of production**—breakdown, design, fixing, generation, selection, editing, acceptance.
The unit placed at its center is the **shot**, and the vessel that carries state is the **production ledger**.

**Sound's sister**: `semantic-audio-loom`. Paired with the same construction (`semantic-` + a word of the senses + `-loom`).

## Differences from Existing AI Film Tools

| | The common shape | This foundation |
| --- | --- | --- |
| Unit | 1 prompt = 1 video | **1 shot = 1 generation**. A work is a sequence of shots |
| State | Rewritten into the prompt every time | Held by the **production ledger** (continuity + disclosure) |
| Text | Let the generator draw it | Separated as a **text channel** and burned in by compositing |
| Acceptance | Visual inspection | **Pre-flight verification**—fires contradictions at the specification stage |

**The second row is the one that matters most.** Make 30 shots with separate prompts, and
**by the 8th you no longer know who knew what.** The ledger takes that on.

## State

**Generation does not run inside this foundation. Pre-flight verification does.**

```bash
python3 engine/ledger/check.py projects/hitosara         # demo "until one plate is made"
python3 engine/ledger/check.py projects/ukebi/ukebi-v2   # Ukebi V2
python3 engine/ledger/check.py --self-test               # does the checker fire
```

The full command list, the requirements, and the layout of a project are in
[`docs/usage.md`](docs/usage.md).

**⚠️ The check is only pre-flight verification and the matching of what came back** (`L25`).
**Generation, selection, and editing are not in the foundation**—the author runs them by hand, and the foundation **reads the records**.
⚠️ **`L25` does not open `media/`.** Therefore **a discrepancy between the record and the actual object does not fire**—a hole.

⚠️ **Zero violations is not "correct."** `check.py` says so at the end.
**Read the notes, and read the range that is not checked.**

## Structure

**What exists**

```text
semantic-visual-loom/
├── schemas/         # the canonical of the data structures (bible / ledger / shot-record / take / timeline)
├── engine/ledger/   # the production ledger and pre-flight verification (crush breakdowns in the design without running generation)
├── docs/            # usage
├── tools/           # checks (i18n mirrors)
├── references/      # cards. Includes the video-spec moved over from distill
└── projects/        # the substance of each work
```

**⚠️ Two kinds live side by side in `projects/`.**

- **Raw specification documents**—§1–20 of Ukebi and Gozen Niji (`video-*/seg-*/wan-full-spec.md`). **They are left as they are.**
- **Structured records**—`bible.yaml` / `ledger.yaml` / `shots/`. **There are two: `ukebi-v2` and `hitosara`.**

⚠️ **For Ukebi and Gozen Niji, no generated output is placed**—**only records and specifications.**

**Old generated output lowers the work's degree of quality uniformity.**

⚠️ **However, the reference assets in `reference/` are kept** (**9 images**. Duplicated into each segment).
**They are not generated output but input**—and **the only record of "which segment had what attached to it"**
(`wan-full-spec.md` names its references only as `REF_STYLE` / `REF_SOURCE`).
⚠️ **Delete them, and the record of attachment goes with them.**

## Demo `projects/hitosara/`

**"Until One Plate Is Made"**—from flour and water and salt and time, until bread becomes one plate.
10 shots. **Completely independent of Ukebi.**

**This is placed here to show everything this foundation reads.**
It steps through a registry that Ukebi V2 does not pass—8 of the 15 roles, all three `mode` values,
`attached` on every shot, and it also uses `text_channel` and `sound`.

⚠️ **Every shot has two paths.** `spec:` is the video's specification (§1–20 and §18),
`key_image:` is the image's specification (it does not have §1–20).
**The image is the one frame that is that shot's highlight, and it passes to the video as an attachment (reference image)**
—**it is not the first frame** (that way, that shot's change does not happen on screen).
**Generation runs in the order 10 images → look at all → 10 videos.**

⚠️ **Only §18 is fed into the generator.** §1–17 in `specs/video/` are the **underlay from which §18 is assembled**,
and §19–20 are **our own record**—**neither is fed in.**
The image specification (`specs/image/`) has no §18, and **the two paragraphs inside one section** are the canonical.
Details in `projects/hitosara/README.md`.

| | |
|---|---|
| `bible.yaml` | The world, its root laws, its visual language. **The style is `luminous-anime`** (the card has a `Motion character`) |
| `ledger.yaml` | The ledger is **one**. People, places, props, **disclosure** (the position where the oven opens, the position where the bread breaks) |
| `shots/` | 10. `role` / `mode` / `beats` / `reference_set` / `attached` / `disclosure_state` / `motion` |
| `specs/video/` | 10. They have §1–20. §18 calls itself `WAN 3.0` and fills 7 slots. **Only §18 is fed in** |
| `specs/image/` | 10. **They do not have §1–20.** 7 fields (the union of the `format` and `style` holes) and one sentence and its Negative |
| `media/` | Where generated output goes. ⚠️ **The foundation does not read here**—it reports neither that it exists nor that it passed. **Samples only** |
| `takes/` | The record of what came back. **The actual object and the record are separate** (below) |
| `renders/` | **What editing produced (the work).** ⚠️ **Samples and works are separated by place**—they cannot be separated by name |
| `timeline/` | **Empty.** ⚠️ **That emptiness is not even reported** |

⚠️ **`media/` and `takes/` are separate.** A place and a record—**placing something is not recording it.**
So a state is possible in which something is in `media/` but has no take.
**That difference is reported by `L25` in a note**—⚠️ **not as a check that counts numbers, but as a report to the reader.**
**If `takes/` is empty, it says "there is not a single take record." Zero is not a pass.**

⚠️ **The emptiness of `timeline/` is not even reported**—because nobody opens it yet.
**A check that does not report looks the same as a check that passed.**

## Planned, But Not Yet There

```text
├── skills/          # breakdown, design, ledger, shots, structure, acceptance
├── engine/handover/ # handover sheets (the 7 slots of §18, image prompts, sound) and round-trip checks
├── engine/shot/     # generation and verification of shot records
├── engine/visual/   # Visual Asset Engine
├── engine/assembly/ # timeline, cuts, text compositing, rendering
├── providers/       # generators for image, video, compositing
├── assets/          # reference assets (character sheets, boards)
└── interchange/     # OTIO / EDL / FCPXML
```

**⚠️ `timeline/` has only a schema, and not a single record.**
`timeline.schema.json` **has not yet been hit by any layer**—
⚠️ **its name is in the `SCHEMAS` constant, but there is no one to read it.**

## Next

**Not yet started.**

### Remove the video-related material from `distill-essence-engine`—⚠️ **that is their work**

**There is nothing to do in this repository.**

⚠️ **There is no need to change their policy.** Their fixed policy states that **"the engine folds into the capacity of one generation, not into a medium"** and forbids **"writing rules that assume the output is a single frame"**—
**what gets dropped is not the policy but the video-leaning material** (the video examples and the YouTube fetching in `scripts/fetch.py`).
So **writing one line there saying "planned for removal at some point" is enough.**

⚠️ **Their multilingualization is complete** (en / ja / zh). **One line becomes three files' worth.**

⚠️ **This work is done in their repository, under their rules.**
This repository's CLAUDE.md states that `distill-essence-engine` is **read but never rewritten**.

⚠️ **The owner of §1–20 and `video-spec.md` has already moved here.**

## Language

**Development proceeds in Japanese**, and the working language of development remains Japanese (commit messages, `HISTORY.md`, conversation).
**The canonical of the documents is English.**

⚠️ **These two are different things.** The working language is the language the work is done in; the canonical is the language the documents are authoritative in.

Mirrors use the suffix scheme and sit in the **same directory** (`README.md` / `README-ja.md` / `README-zh.md`). **No `-en` mirror is created**, because the canonical is English.
**The subfolder scheme (`ja/` `zh/`) is not used**—so that the depth of the canonical and the mirrors does not change.

**10 documents × 3 languages are in place.** `tools/check_i18n.py` checks them:

```bash
python3 tools/check_i18n.py --self-test   # firing and non-firing examples for each rule
python3 tools/check_i18n.py               # the real thing
```

⚠️ **The check reports how many files it looked at and which blocks it treated as invariant.** Without that, a check that saw nothing looks like a check that passed.
⚠️ **It does not see whether the prose is translated correctly**—if the meaning contradicts, it still passes as long as the line and heading counts agree.

## License

MIT
