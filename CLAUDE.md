<!-- i18n-version: 1.1.1 | canonical: CLAUDE.md | translated: 2026-09-18 -->

**Language:** [English](CLAUDE.md) | [日本語](CLAUDE-ja.md) | [中文](CLAUDE-zh.md)

# semantic-visual-loom — Project Instructions

## Document Rules

Development history (dated change histories, comparisons with past designs, past measurements, and so on) is **not written in README / docs**. History is centralized in `HISTORY.md`.

In README / docs, write **only current information**. Current features, the CLI, and the rationale of the design (a short reason without a date) are OK. If you need background like "it used to be X but we changed it to Y," put it in `HISTORY.md`.

**Placement**:

- `README.md` … what it is and its structure (overview only; deep dives are links to `docs/`)
- `docs/` … usage, and deep dives on the README (ledger, shot records, pre-flight verification)
- `schemas/` … the canonical of the data structures
- `HISTORY.md` … development history and measurements
- The background of the design and the undecided matters are **outside this repository** (see "Where the Design Lives" below)

## Where the Design Lives

**The design is not in this repository.** The repository is the **implementation**.

The design notes (concepts, undecided matters, verification measurements) are in the author's hands and are **not a distributed artifact**.
Therefore, **do not** link from this repository's documents to the design notes (they would be invisible to anyone who clones it).

**What the implementation needs is written inside the implementation.**

## Fixed Policy (do not change)

- **The shot is the unit.** One shot exists for **one change**—one place, one moment, one camera event, one change of a gesture. **Do not load it with anything more.** Length is a dependent variable. Do not divide by episode, by scene, or into "30-second segments."
- **Role is the cross-cutting axis.** The acceptance criteria **differ by role**. Apply a single criterion to all shots, and **only the shots that satisfy that criterion survive, and the work becomes a repetition of a single scene.** Role is not a fixed enumeration—**it is registered as a card, and it grows and is refined.**
- **Motion is also a cross-cutting axis.** Role decides "that shot's job," whereas motion runs beneath every shot. **In film, motion is the ground, and stillness is the special case.**
- **State is placed in the ledger.** Independent generations have no memory of each other. So state is placed outside the generation.
- **The production ledger is one.** The continuity ledger (the state of the world) and the disclosure ledger (the state of the audience's knowledge) are **held in the same file**. The **reference set** (what is fixed) and the **forbidden set** (what must not be shown) handed to generation are **derived from this single point**. **Do not split it in two**—the failure that actually happened was "which reference image to attach to which shot," and that judgment is at once a judgment of continuity and a judgment of disclosure.
- **A work does not hold a work.** **Every work carries its own `bible.yaml` and `ledger.yaml` in its own directory**—but **a directory that holds a work is not necessarily a work itself** (`projects/ukebi/` holds 11 raw segment trees and one work). ⚠️ **The converse does not hold.** `check.py` **does not recurse**—it loads `root/shots/*.yaml` with a flat glob—so **a work held by a work is not read by a run over its parent, and the output does not say so.** `L29` names the works a run does not read.
- **Generation is a sample.** What the generator makes is a candidate for adoption, not the work. **Adoption is selection, and the author is the editor.**
- **The strings handed to the generator are English.** The word sequences of the specification, prompt, and Negative are **written in English**—the canonical is English. **Do not translate them**—translating changes the output.
- **The work has a language, and it speaks it.** If there is speech it is in `bible.language`—**and a work with no speech declares one too, because a blank is not neutral: the generator fills it with its own default.** Measured: a video with speech in it came back with **Chinese subtitles burned into the picture.** ⚠️ **Name the language; do not forbid the symptom** (`L27`).
- **Subtitles and background music are off unless asked for.** The foundation carries both as its floor (`specmap.BASE_NEGATIVES`), and **`L21` requires them on both paths**—the video's §18 `Negative Prompt` and the image's `Negative`. ⚠️ **A work that predates the floor declares `bible.base_negatives_waived`**—**the work writes the exclusion, because an engine that remembers which works are special has stopped being an engine.**

## Language (i18n)

**Development proceeds in Japanese, and the working language of development remains Japanese** (commit messages, `HISTORY.md`, conversation). **The canonical of the documents is English.**

⚠️ **These two are different things.** The working language is the language the work is done in; the canonical is the language the documents are authoritative in. Mixing them breaks one or the other.

- **The canonical file carries no suffix** (`README.md`, `docs/ledger.md`).
- **Mirrors use the suffix scheme and sit in the same directory**—`README-ja.md` / `README-zh.md`, `docs/ledger-ja.md` / `ledger-zh.md`. **No `-en` mirror is created**, because the canonical is English.
- **The subfolder scheme (`ja/` `zh/`) is not used.** It is so that the **depth of the canonical and the mirrors does not change** (when the depth changes, relative paths shift).
- **Invariant blocks** (the strings handed to the generator = specification, prompt, Negative, enum values) are **left in English, untranslated**.
- **`HISTORY.md` stays Japanese.** It is the record of the work, not a document for readers.

**22 documents × 3 languages are in place.** `tools/check_i18n.py` checks them: mirror existence and non-emptiness, the `i18n-version` header, the switcher line, the invariant blocks, and the heading levels.

⚠️ **That check does not see whether the prose is translated correctly.** It reports **how many files it looked at and which blocks it treated as invariant**—because a check that reports nothing looks like a check that passed.

## Tests

**⚠️ There is nothing yet.**

## Things That Must Not Be Broken

- **Do not touch `distill-essence-engine`.** The cards (format, style) are its property. You may **read** from this repository, but **do not rewrite**.
- **Do not split the ledger in two** ("Fixed Policy" above).
- **Do not make the strings handed to generation Japanese.** Explanations may be in Japanese. **The strings you hand over are English.**
- **Do not write the canonical (`README.md`, `CLAUDE.md`, and so on) in Japanese.** The canonical is English; Japanese goes in the `-ja` mirror.

## Git

- `git push` **only when the user explicitly asks for it**. A push without a request is forbidden.
- Append `Co-Authored-By: Claude Code <noreply@anthropic.com>` to the end of commit messages.
- **The manifest version tracks `HISTORY.md`.** When a `## <version>` heading goes into `HISTORY.md`,
  **the same version goes into both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`**.
  ⚠️ **Two files, one version**—bump one and the other becomes a lie. (`claude plugin validate --strict`
  catches that: it compares the two against each other.) ⚠️ **Nothing compares either of them against
  `HISTORY.md`**—so **a version that was never bumped passes every check.**
