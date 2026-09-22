<!-- i18n-version: 1.0.0 | canonical: README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# semantic-visual-loom

<p align="center">
  <img src="assets/repo-hero.png" width="100%" alt="semantic-visual-loom">
</p>

**A foundation that carries a story all the way to film.**

> **A story becomes a run of shots.**

**What the model makes is a sample**—and **independent generations have no memory of each other.**
So state is placed outside the generation: **that vessel is the production ledger, one file**,
holding continuity and disclosure together.

The unit placed at its center is the **shot**——⚠️ **one shot exists for one change**,
and **length is a dependent variable.**

⚠️ **The films are in this repository.** `*.mp4`, `*.m4a` and `*.png` are stored through
**Git LFS** ([`.gitattributes`](.gitattributes)): what is committed is a **small text pointer**,
and the picture itself lives in **this repository's LFS storage on GitHub**——**there is no second
repository.** ⚠️ **A clone without `git-lfs` brings down pointers instead of video**: install it
before cloning, or run `git lfs pull` afterwards.
⚠️ **LFS is metered apart from the repository, and it counts against the owner's account**——
GitHub's included allowance is **10 GiB of storage and 10 GiB of transfer a month** on Free
([billing docs](https://docs.github.com/en/billing/concepts/product-billing/git-lfs)).
**What this repository actually holds is in [`HISTORY.md`](HISTORY.md).**

## Differences from Existing AI Film Tools

| | The common shape | This foundation |
| --- | --- | --- |
| Unit | 1 prompt = 1 video | **1 shot = 1 generation**. A work is a sequence of shots |
| State | Rewritten into the prompt every time | Held by the **production ledger** (continuity + disclosure) |
| Text | Let the generator draw it | Separated as a **text channel** and burned in by compositing |
| Acceptance | Visual inspection | **Pre-flight verification**—fires contradictions at the specification stage |

**The second row is the one that matters most.** Make 30 shots with separate prompts, and
**by the 8th you no longer know who knew what.** The ledger takes that on.

## What You Can Do Today

**A story goes in. The strings a generator is handed come out.**

**Generation does not run inside this foundation.** What it does is **turn a story into the shot
specifications**, and **fire the contradictions in them before anything is generated.**

| | you hand in | you get out |
| --- | --- | --- |
| **① breakdown** | a story, a plot, a draft | the **shot list**—the work cut at the unit of one change, each shot given a role—plus the work ledger and the disclosure change points |
| **② design** | one shot | the **§1–20 specification** and the **image specification**—including **§18's seven English slots**, which is what the generator is handed |
| **③ ledger** | one shot | the **ledger**, grown—and the **reference set** (what is fixed) and the **forbidden set** (what must not be shown) derived from it |
| **④ shot** | what came back | the **take**—one generation, one sheet |

**② is where the prompt is written.** The seven slots are `Master` / `Visual` / `Motion` / `Camera` /
`Audio` / `Negative` / `Style Motion`, and **being separated is itself the point**
([`references/formats/video-spec.md`](references/formats/video-spec.md) §18). ⚠️ **The `Camera` slot
is written by [`skills/staging/`](skills/staging/SKILL.md)**—**the camera decided in one hand**,
inside ②, between `motion`/`duration` and the specification.

⚠️ **The prompt is built from two axes, and both are cards**—**Format** (the shape of the
specification) and **Style** (the visual language). **A card lives beside this repository by
default** (`distill-essence-engine/references/formats` and `.../styles`), **and a work of this
side's own overlays it** rather than replacing it:

```bash
SVL_FORMATS_DIR=references/formats SVL_STYLES_DIR=references/styles \
  python3 engine/ledger/check.py projects/ippitsu
```

⚠️ **A card nothing points at is a card nothing reads**—and **a card that is named but
unreadable fires a violation**, so **set the variable, or the work's own cards are invisible.**
**What the two axes are, where they live, and which check reads what**, is in
[`docs/cards.md`](docs/cards.md).

⚠️ **①–④ are instructions to a Claude Code session, not programs**—they lay down **the order of
decisions**, and **there is no code for them in this repository.** ⚠️ **And the checker reads
nothing until ② is on disk**: a shot record requires `duration`, which ② decides.

```bash
python3 engine/ledger/check.py projects/hitosara         # demo "until one plate is made"
python3 engine/ledger/check.py projects/ukebi/ukebi-v2   # Ukebi V2
python3 engine/ledger/check.py --self-test               # does the checker fire
python3 engine/shot/print_spec.py projects/hitosara      # the lines of a spec whose value is forced
```

The four stages, the full command list, the requirements, and the layout of a project are in
[`docs/usage.md`](docs/usage.md).

**⚠️ What actually runs is pre-flight verification and the matching of what came back**
(`L25`). **Generation, selection, and editing are not in it**—the author runs them by hand,
and the foundation **reads the records**. ⚠️ **`L25` does not open `media/`**, so
**a discrepancy between the record and the actual object does not fire.**
⚠️ **Zero violations is not "correct."** Read the notes, and read the range that is not checked.

## Structure

**What exists**

```text
semantic-visual-loom/
├── schemas/         # the canonical of the data structures (bible / ledger / shot-record / take / timeline)
├── engine/ledger/   # the production ledger and pre-flight verification (crush breakdowns in the design without running generation)
├── engine/shot/     # prints the derivable lines of a shot's specification (read-only; writes nothing)
├── docs/            # usage, and the deep dives (cards / routes)
├── skills/          # the skills — breakdown, design, ledger, shot, and staging (inside ②)
├── tools/           # checks (i18n mirrors)
├── references/      # this side's own cards — formats/ (video-spec) and styles/ (sumi-e)
├── assets/          # the repository's face (the README hero)
└── projects/        # the substance of each work
```

**⚠️ Two kinds live side by side in `projects/`**—**raw specification trees** (§1–20 of Ukebi and
Gozen Niji, left as they are) and **structured records** (`bible.yaml` / `ledger.yaml` / `shots/`;
**four** of them—`hitosara`, `ukebi-v2`, `habits` and `habits-promo-chinatsu`).
⚠️ **Every work carries its own `bible.yaml` and `ledger.yaml`, and a work does not hold a work**
—and this is why that matters: **`check.py` does not recurse**, so **a work held by a work is not
read by a run over its parent.** `L29` names the works a run does not read.
⚠️ **No generated output is placed beside the raw trees, while their `reference/` assets are
kept.** Why input is not a sample, and what is lost if it is deleted, is in
[`docs/usage.md`](docs/usage.md).

## Demo `projects/hitosara/`

**"Until One Plate Is Made"**—from flour and water and salt and time, until bread becomes one plate.
10 shots. **Completely independent of Ukebi.**

[![Until One Plate Is Made](https://i.ytimg.com/vi/pJyiziIUaPY/hqdefault.jpg)](https://www.youtube.com/watch?v=pJyiziIUaPY)

⚠️ **What is on that video is the work, not a sample**—the distinction is in
[`projects/hitosara/renders/README.md`](projects/hitosara/renders/README.md).
⚠️ **And the footage cannot show the thing this foundation is actually about**——
**the 10 shots come out of one ledger.** That is the second row of the table above,
and **it is the one claim a video cannot make on its own.**

**It is placed here to show everything this foundation reads**—it steps through a registry that
Ukebi V2 does not pass (8 of the 15 roles, all three `mode` values, `attached` on every shot,
`text_channel` and `sound`).

⚠️ **Every shot has two paths**—`spec:` for the video, `key_image:` for the image—and
**only §18 is fed into the generator.** ⚠️ **Generation runs 10 images → look at all → 10 videos.**
⚠️ **This is the route where the video names `WAN 3.0`.** On the second video route (`MINIMAX H3`)
**a shot has no image path at all**—the generator is handed a storyboard image instead, and the
paper that makes it lives in `specs/board/` ([`docs/usage.md`](docs/usage.md)).
⚠️ **The routes do not share a grammar of time**, and the constraints that hold on the second
one are in [`docs/h3-route.md`](docs/h3-route.md).
⚠️ **A third video route, `SEEDANCE 2.5`, attaches nothing by default**—it reads one long prompt,
and **that prompt may carry its own clock**—but **its `Negative Prompt` slot is not received as a
floor.** That gate is what `L30` fires on, and the route's constraints are in
[`docs/seedance-route.md`](docs/seedance-route.md).
**The rest is in [`projects/hitosara/README.md`](projects/hitosara/README.md).**

## Planned, But Not Yet There

```text
├── engine/handover/ # handover sheets (the 7 slots of §18, image prompts, sound) and round-trip checks
├── engine/visual/   # Visual Asset Engine
│                    #   Reference assets already live per work, in `reference/` — 69 places,
│                    #      9 distinct images. That is their home today.
│                    #   ⚠️ undecided: the central home, and the duplication (one image copied up
│                    #      to 37 times); §6's `REF_*` names point at nothing.
│                    #   ⚠️ `assets/` is now the repository's face (the README hero), so they
│                    #      cannot be put there. The cards are `distill-essence-engine`'s
│                    #      property and are only read from here.
│                    #   ⚠️ undecided: the ledger's values carry a Japanese gloss in full-width
│                    #      parentheses (`...character-sheet（手と前掛け。顔は映さない）`) while §6 uses
│                    #      only the name (10/10). ⚠️ Splitting them would mean writing into `projects/`,
│                    #      which no tool in this repository does.
├── engine/assembly/ # timeline, cuts, text compositing, rendering
├── providers/       # generators for image, video, compositing
└── interchange/     # OTIO / EDL / FCPXML
```

⚠️ **Two stages are missing from `skills/`**——**structure (⑥) and acceptance (⑦).**
They cannot be written, because **the input is not on the record side.** `clips[]` is by definition
**a list of adopted takes**, and **not one video take carries `adopted: true`.**
It is not that they are hard to write——⚠️ **it is that they cannot be moved**, and
**a skill that emits an empty timeline is worse than no skill.** The hole is written where it happened:
[`projects/hitosara/renders/README.md`](projects/hitosara/renders/README.md).

⚠️ **Do not leave them here as "planned."** They are not waiting on work——
**they are waiting on adopted takes, and adoption is the author's act.**
Listed as a plan, they look like they will arrive on their own.

**⚠️ `timeline/` has only a schema and not a single record**—⚠️ **its name is in the `SCHEMAS`
constant, but there is no one to read it.** [`docs/usage.md`](docs/usage.md) lists the schemas.

## Next

**Not yet started.**

### Remove the video-related material from `distill-essence-engine`—⚠️ **that is their work**

**There is nothing to do in this repository**, and **their policy does not need to change.**
Their fixed policy folds the engine **into the capacity of one generation, not into a medium**,
and forbids **writing rules that assume the output is a single frame**—**what gets dropped is not
the policy but the video-leaning material** (the video examples and the YouTube fetching in
`scripts/fetch.py`). So **one line there saying "planned for removal at some point" is enough**—
and since **their multilingualization is complete** (en / ja / zh), **one line becomes three files' worth.**

⚠️ **This work is done in their repository, under their rules.** This repository's `CLAUDE.md`
states that `distill-essence-engine` is **read but never rewritten.**
⚠️ **The owner of §1–20 and `video-spec.md` has already moved here.**

### Run ② for `habits-ch01-seg01`—⚠️ **gated on its prose**

That shot record carries **no `spec:`**, and it is the one violation
`python3 engine/ledger/check.py projects/habits` reports. **A declared state, not an oversight**—
the minimal form (policy §7) cuts `bible.yaml` + `ledger.yaml` + `shots/` and **no `specs/`**.
**② has never been run for the first volume, because its prose does not exist yet.**
⚠️ **Run ② when that episode is written—and settle `duration` in the same pass.** The record's `8s`
is marked **invention (awaiting approval)**; running ② first would freeze an unapproved guess into
§1, and `L23` would then report it as a match.

## Language

**Development proceeds in Japanese, and the canonical of the documents is English.**
Mirrors use the suffix scheme and sit in the **same directory**—the rules are in
[`CLAUDE.md`](CLAUDE.md).

**21 documents × 3 languages are in place**——**that is the count
[`tools/check_i18n.py`](tools/check_i18n.py) reports as the canonical set, not a count of every
`.md` in the repository.** ⚠️ **A number is only as wide as what was counted.** What that check sees,
and what it does not, is in [`docs/usage.md`](docs/usage.md).

## License

MIT
