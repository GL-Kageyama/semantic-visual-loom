<!-- i18n-version: 1.1.0 | canonical: docs/cards.md | translated: 2026-09-22 -->

**Language:** [English](cards.md) | [日本語](cards-ja.md) | [中文](cards-zh.md)

# Cards — Format and Style

**A prompt is built from two axes, and both of them are cards.** **Format** is the shape of
the specification; **Style** is the visual language drawn inside that shape. **Neither is a
list in this repository**—**each is a directory of Markdown cards**, and **a card is read at
run time, by name.**

⚠️ **They are two layers, not two views of one thing.** A card of one layer cannot stand in
for a card of the other, and **a work can carry one without the other**—which is the defect
`L22` was written after.

## Where the cards live

**By default, beside this repository**—in `distill-essence-engine`:

```text
distill-essence-engine/references/formats/   # the format cards
distill-essence-engine/references/styles/    # the style cards
```

⚠️ **That directory is not part of this repository**, so **a fresh clone does not have it.**
A check that cannot open a card **says so** rather than passing—**"could not verify" is not
"verified."**

**A work of this side's own cards live inside this repository**, in the same two-layer shape:

```text
references/formats/    # this side's format cards — `video-spec`
references/styles/     # this side's style cards — `sumi-e`
```

⚠️ **The two directories are the same thing seen from two sides**—`_cards_dirs()` searches
**one list per layer**, and **the order of that list is what the environment variable sets.**

## How many cards there are

**Counted 2026-09-22**, over the two directories `_cards_dirs()` searches, by **counting the
`.md` files in each and setting the mirrors aside**—`video-spec-ja.md` and `video-spec-zh.md`
are translations of `video-spec.md`, not cards of their own, so the three are one card.

| directory | format cards | style cards |
|---|---|---|
| `references/` — **this repository's own** | **8** | **16** |
| `distill-essence-engine/references/` — the neighbour, where it is there | 45 | 55 |

**What the 8 and the 16 are.**

- **8 format cards** = `video-spec` **+ the seven grammars this side added**: `transformation`,
  `time-fold`, `remembered-world`, `impossible-camera`, `meaning-responsive`,
  `recognizing-world`, `coexisting-realities`.
- **16 style cards** = `sumi-e` **+ fifteen carried over from the image side** (`watercolor`,
  `mokuhanga`, `oil-painting`, `gouache-abstract`, `cinematic-still`, `documentary-photo`,
  `instant-photo`, `landscape-photo`, `macro-photo`, `street-photo`, `studio-portrait`,
  `sketch-broadstroke`, `blueprint-plan`, `lab-notebook`) **+ `impossible-medium`, the one card
  here with no image-side original.**

⚠️ **Of these 24 cards, one has mirrors.** `video-spec-ja.md` and `video-spec-zh.md` are the
only pair, so **23 cards are canonical English with no translation**—and
[`tools/check_i18n.py`](../tools/check_i18n.py) does not count them among its documents: **it
checks the documents handed to a reader, and these are cards a run opens.**

⚠️ **The neighbour's 45 and 55 are counted by the same rule, over that directory as it stands
today.** They are **the image side's inventory, and this repository does not own them**—so
**those two numbers can move without anything here changing.**

## The environment variables

| layer | variable | |
|---|---|---|
| format | `SVL_FORMATS_DIR` | where the format cards are |
| style | `SVL_STYLES_DIR` | where the style cards are |

⚠️ **Each layer reads its own variable.** Pointing at a style directory **does not move the
format layer**—and **the converse holds too.** *A naming that is not read must not look like
one that is.*

⚠️ **The variable overlays; it does not replace.** The directory it names is searched
**first**, and **the default directory beside this repository is searched after it**—so **one
card added by a work does not make the engine's cards unreachable.** *This matters because the
card a work names is one name, and a replacement would cost it every other card.*

⚠️ **Pointing at a directory that is not there is not an error**—**that directory is skipped
and the default still applies.** *A wrong pointer must not silently become "no cards."*

⚠️ **A relative path is resolved against the working directory**, so run from the root of this
repository:

```bash
SVL_FORMATS_DIR=references/formats SVL_STYLES_DIR=references/styles \
  python3 engine/ledger/check.py projects/ippitsu
```

⚠️ **If you do not set them, the cards inside this repository are not read**—and **a
specification that names a card nobody can open fires a violation.** So **a work with video
specifications needs the variable set**, or the cards it keeps beside it are invisible to the
checker.

## How a specification names a card

**§6 `REFERENCES` of a video specification names the cards it draws on**:

```text
- `REF_FORMAT`: `video-spec`
- `REF_STYLE`: `luminous-anime`
```

**The first names the format card this specification is built on; the second the style card it
is drawn in.** ⚠️ **Neither is a section of the specification**—**§6 is where the names live, and
the card is a separate file.**

The name may be **a card name** or **a path**—**both are folded to one name before anything is
compared** (take the last path segment, drop `.md`). ⚠️ **Which vocabulary is correct is not
decided here**; the layer makes both comparable.

⚠️ **`bible.style` is the work's home for the style, and `REF_FORMAT` has no such home.** That
is deliberate: **the two routes name different formats**—the video route names a video
specification card, and the image route names an image one—so **a single field holding one
name would have to lie about the other route.**

## What a card declares

| section | format | style | |
|---|---|---|---|
| `## Environment variables` | required | required | the holes the card fills; the union of the two layers is the image prompt's seven fields |
| `## Negative` | required | required | the exclusions this card adds |
| `## Motion character` | — | optional | what this style does when it moves |

⚠️ **Only `## Motion character` is optional.** A card that fills slots **and** takes part in
`Negative Prompt` **must declare both of the other two.**

## Which check reads what

| check | reads | fires on |
|---|---|---|
| `L20` | a style card's `## Motion character` | the named style has no such section—**so `Style Motion` exists and carries nothing** |
| `L22` | **image** specifications, both layers | a hole no card declares; a card carrying holes the specification does not fill; a card that cannot be opened or has no `## Environment variables` |
| `L31` | the style card named in §6 ⇄ `bible.style` | the home and the specification name different styles |
| `L32` | the format card named in §6 | the named card cannot be opened, or declares no `## Negative` |

⚠️ **`L31` and `L32` are neighbours on purpose**—**they read the same §6 and differ only in the
key.** Separated, one of them gets fixed and the other is forgotten.

⚠️ **`L20` and `L32` report three outcomes, not two**—**a missing card directory is a note;
a missing card is a violation; a card missing its section is a violation.** *A directory that
is not there and a card that is not there are different causes, and reporting both the same way
leaves the reader unable to tell which one to fix.*

⚠️ **On a clone with no neighbouring engine, `L20` and `L32` therefore report notes, not
violations.** **The same code reports a different sign depending on where it is placed**—that
is the honest reading of "this repository does not hold the cards," not a bug.

## What is not read

**⚠️ Read this list as holes, not as a to-do.**

- **The remaining keys of §6** (`REF_CHARACTER` / `REF_SOURCE` / `REF_BIBLE`). **No check reads
  them**—`L31` reads `REF_STYLE` and `L32` reads `REF_FORMAT`, and nothing else.
- **The style card's `## Negative`.** `PROMPT_SLOT_SOURCE` defines `Negative Prompt` as `§16 +
  this card's Negative + the style card's Negative`, and **only the first of those two card
  terms is read** (`L32`).
- **Whether a card's contents are right.** What is checked is **that the section exists** and
  **that the declared holes are the ones the specification fills**—**what the words in the card
  do to the output is not visible from here.**
- **Every section of a card other than `## Environment variables` and `## Negative`.** A format
  card declares the holes it fills and the exclusions it adds; **anything else it says is
  addressed to a reader.** ⚠️ **This is why `L22` cannot be extended to the video route**—a
  video specification uses §1–20 and fills none of the holes a video format card declares, so
  **the check would fire on every correct specification.**
- **The board.** No shot record field points at `specs/board/`, so **no check opens it**
  ([`docs/usage.md`](usage.md)).

## Where to read more

- [`engine/ledger/README.md`](../engine/ledger/README.md) — every layer, what it reads, and
  what it does not.
- [`engine/shot/README.md`](../engine/shot/README.md) — §6 and its unstable shape.
- [`references/formats/video-spec.md`](../references/formats/video-spec.md) — the format card
  this repository carries.
