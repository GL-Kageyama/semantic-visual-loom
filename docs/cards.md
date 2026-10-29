<!-- i18n-version: 1.2.0 | canonical: docs/cards.md | translated: 2026-10-29 -->

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
references/grammars/   # the registry — `index.yaml`
references/camera/     # the technique registry — `index.yaml` (100 camera techniques)
```

⚠️ **The registry is not a third layer.** It holds no cards of its own; **it lists the format
cards that are grammars**, and **it lives here rather than being derived at run time** so that a
name a shot uses has one place to be registered.

⚠️ **The two directories are the same thing seen from two sides**—`_cards_dirs()` searches
**one list per layer**, and **the order of that list is what the environment variable sets.**

## How many cards there are

**Counted 2026-10-29**, over the two directories `_cards_dirs()` searches, by **counting the
`.md` files in each and setting the mirrors aside**—`video-spec-ja.md` and `video-spec-zh.md`
are translations of `video-spec.md`, not cards of their own, so the three are one card.

| directory | format cards | style cards |
|---|---|---|
| `references/` — **this repository's own** | **16** | **16** |
| `distill-essence-engine/references/` — the neighbour, where it is there | 45 | 55 |

**What the 16 and the 16 are.**

- **16 format cards** = `video-spec` **+ the fifteen grammars**: `transformation`, `time-fold`,
  `remembered-world`, `impossible-camera`, `meaning-responsive`, `recognizing-world`,
  `coexisting-realities`, and the eight provisional ones — `recursive-frame`, `scale-rupture`,
  `material-substitution`, `population-emergence`, `temporal-panorama`, `light-as-actor`,
  `frame-escape`, `physics-with-a-rule`. **What makes one of these a grammar and not another
  kind of card is that it is `video-spec` plus one rule**, and that rule is what the registry
  below records.
- **16 style cards** = `sumi-e` **+ fourteen carried over from the image side** (`watercolor`,
  `mokuhanga`, `oil-painting`, `gouache-abstract`, `cinematic-still`, `documentary-photo`,
  `instant-photo`, `landscape-photo`, `macro-photo`, `street-photo`, `studio-portrait`,
  `sketch-broadstroke`, `blueprint-plan`, `lab-notebook`) **+ `impossible-medium`, the one card
  here with no image-side original.**

⚠️ **Of these 32 cards, one has mirrors.** `video-spec-ja.md` and `video-spec-zh.md` are the
only pair, so **31 cards are canonical English with no translation**—and
[`tools/check_i18n.py`](../tools/check_i18n.py) does not count them among its documents: **it
checks the documents handed to a reader, and these are cards a run opens.**

## The grammar registry

`references/grammars/index.yaml` **is the list of grammars, and it is the list the checks
read.** A grammar card is prose addressed to a person; **the registry is the same facts in a
shape a check can open.**

```text
- name: transformation            # the name §6 REF_FORMAT uses
  card: transformation            # references/formats/<card>.md
  status: established             # established | provisional
  routes: [WAN 3.0, MINIMAX H3, SEEDANCE 2.5]
  written_into: ["9. ACTION", "11. MOTION"]
  essential_moves: [ … ]          # what the grammar does, in one line each
  negative_conflicts: ["no deforming silhouette"]   # clauses that would forbid the move
  grounding: …                    # the ordinary shot this grammar is measured against
  failure: …                      # the defect it is most often confused with
```

⚠️ **`status` says whether the list is canonical, not whether the card is good.** The seven
`established` cards are the ones this repository already had. **The eight `provisional` ones
fill seats that the author's own list will replace**—so **a provisional entry is not to be
quoted as canon.**

⚠️ **`routes` is a declaration, not a measurement.** The only entry with a measured reason is
`coexisting-realities`, whose own card says a single continuous take cannot hold two places
—**so `WAN 3.0` is excluded there and nowhere else.** Do not widen or narrow `routes` without
a card saying why.

⚠️ **`written_into` uses the section names of `specmap.SPEC_SECTIONS`** (`"9. ACTION"`), so the
registry and the specification share one spelling. **The card writes the same list as `§9
ACTION`**—two spellings, two readers, one list.

⚠️ **`negative_conflicts` holds only clauses that already stand in some card's `## Negative`.**
**It does not add to the floor**—it names phrases that would forbid the grammar's own move if
a work copied them into §18. **An empty list means "no clause here forbids it," not "checked
and clear."**

⚠️ **The neighbour's 45 and 55 are counted by the same rule, over that directory as it stands
today.** They are **the image side's inventory, and this repository does not own them**—so
**those two numbers can move without anything here changing.**

## The camera registry

`references/camera/index.yaml` **is the list of camera techniques, and it is the list the
checks read.** It answers a different question from the grammar registry: the grammar registry
says **which format cards are grammars**, and the camera registry says **what the moves are
called** — 100 techniques, each carrying the English line, the motion group, the roles it can
serve, the grammars it commonly pairs with, and the directing job it does.

```text
- id: "007"                              # the source list's number
  name: クレーンアップ
  en: [crane up, camera rises on a crane]  # the line §18 is built from
  motion_pattern: [カメラのみ]             # rolemap.MOTION_PATTERNS
  roles: [開示, 情景]                     # the jobs the move can do — a set, not a choice
  functions: [転換, 発見]                 # specmap.DRAMATIC_FUNCTION_EN
  grammars: [{card: impossible-camera, confidence: △}]
  travels: true                          # does the camera change position
  directing: {job: [解放, 確立], pairs_with: [幕切れで視野を開く, 勝利の後], position: [尾]}
  physical: 位置=上昇しながら弧 ／ …       # what the camera's body does
  status: draft
```

⚠️ **`roles` is a set, and that is the design.** A move can serve several jobs; **the shot's
`role` decides which one**, and a table that collapses this to one row per technique **would be
a lie.** ⚠️ **`travels` is a design fact, not a measurement**: pans, tilts, rolls and zooms turn
or reframe **without changing where the camera stands**, so they are `false` even though the
picture moves.

⚠️ **Every entry is `status: draft`.** The mapping was applied from general film practice,
**not measured against any work's own shots.** **A work's use wins**: when the two disagree,
**the catalog is corrected, not the work.**

⚠️ **`L53` reads the whole list and judges none of it**: each `motion_pattern` must resolve
against `rolemap.MOTION_PATTERNS`, each `role` against `rolemap.ROLES`, each function against the
schema's enum, and each grammar card against the grammar registry. **Whether a move is right for
a shot is not a question this layer can ask.**

## The lighting registry

`references/lighting/index.yaml` **is the list of lighting techniques, and it is the list the
checks read.** It answers a different question from the camera registry: the camera list says
**how the camera moves**, and this one says **who is making the light** — 100 techniques, each
carrying the English line, the maker, the roles it can serve, the functions it leans toward,
the grammar it commonly pairs with, and the directing job it does.

```text
- id: "038"                              # the source list's number, normalised to three digits
  name: スリット光
  en: [Slit light]                       # the line §13 is built from
  kind: 灯                               # 灯 · 自然 · 光学 · 編集 — who makes it
  roles: [開示, 様式美]                   # a set, not a choice
  functions: [発見, 様式美]
  grammars: [{card: light-as-actor, confidence: ○}]
  directing: {job: [焦点, 意味], pairs_with: [帯が1本], position: [中]}
  source: "38"                           # the number as the source printed it
  status: draft
```

⚠️ **`kind` is the pillar here, and it is not a motion type.** The camera list resolves almost
one-to-one against `MOTION_PATTERNS`; **light has no motion group at all** — the column is
absent, not empty. What replaces it is **who makes the light**: `灯` (lamps on the set), `自然`
(sun, sky, water), `光学` (lens and aperture), `編集` (the grade). ⚠️ **Those four are not the
source cards' four pages**: the page titled "effects added in the edit" holds 10 edits, 14 lens
effects and one that needs mist in the air.

⚠️ **`name` is not unique, and the layer does not ask it to be.** The source prints 42 and 43
under the same Japanese name while their English names read `High contrast` and `Low contrast`.
**The copy keeps the source; `en` and `source` tell them apart.**

⚠️ **`physical` is absent.** The cards carry a name and an English name and nothing else —
**a field with no source is not a missing field**, and asking for it would invite a guess.

⚠️ **`L55` reads the whole list and judges none of it.** **`L56` reads §13 `LIGHTING` against
the catalog's `en` lines** — the first layer in this repository to open §13 at all.
⚠️ **`L56` does not inflect the head word**: light names are nouns, and inflection makes
`Bloom` match `the source blooms` — **a light the shot did not name.**

⚠️ **Every entry is `status: draft`**, and the grammar card the list leans on most,
`light-as-actor`, is `provisional` in the grammar registry. **The notes say how many entries
cite it** — a provisional card cited from a draft list is still not canon.

## The environment variables

| layer | variable | |
|---|---|---|
| format | `SVL_FORMATS_DIR` | where the format cards are |
| style | `SVL_STYLES_DIR` | where the style cards are |
| registry | `SVL_GRAMMARS_DIR` | where `index.yaml` is — **overlaid, never replaced**: this repository's own `references/grammars/` remains reachable |
| camera | `SVL_CAMERA_DIR` | where the technique list is — **overlaid, never replaced**: this repository's own `references/camera/` remains reachable |
| light | `SVL_LIGHTING_DIR` | where the lighting list is — **overlaid, never replaced**: this repository's own `references/lighting/` remains reachable |

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
| `## Environment variables` | required | required | the holes the card fills; **the union of the cards a specification names is the set of fields that specification must hold** |
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
| `L42` | §6 `REF_FORMAT`, the grammar registry, `dramaturgy.set_pieces` | the named grammar is not in the registry; a section it declares `written_into` is missing or empty; §18 names a route not in its `routes`; a set piece's `format` is not the §6 name |
| `L45` | the registry's `negative_conflicts` and §18 `Negative Prompt` | the specification names a grammar and its own `Negative Prompt` forbids that grammar's essential move |
| `L46` | `aim`'s `grammar: <name>` prefix and the registry | `aim` claims a grammar the registry does not hold |
| `L53` | the camera catalog and this foundation's vocabulary | a `motion_pattern`, `role`, function, grammar card or shape that does not resolve; ⚠️ **a catalog that cannot be opened is a note** |
| `L54` | §18 `Camera Prompt` and the catalog's `en` lines | a whole-take hold beside a technique whose `travels` is true. ⚠️ **a prompt that uses no catalog line is a note** |
| `L55` | the lighting catalog and this foundation's vocabulary | a `kind`, `role`, function, grammar card or shape that does not resolve; ⚠️ **a catalog that cannot be opened is a note** |
| `L56` | §13 `LIGHTING` and the lighting catalog's `en` lines | nothing — **every outcome is a note**: how many specifications carry §13, which lights were named, how many named none, **and which shots name a light that §18's `Visual Prompt` never carries** |

⚠️ **`L53` and `L54` are neighbours the other way round**—**`L53` reads the catalog alone,
`L54` reads a work against it.** **Neither judges whether a move is right for a shot.**
⚠️ **`L55` and `L56` are the same pair for light**, with one difference in the direction of
reading: **`L54` reads §18, `L56` reads §13** — and §13 had no reader at all before `L56`.

⚠️ **`L31`, `L32`, `L42`, `L45` and `L46` are neighbours on purpose**—**they read the same §6
and the same registry, and differ only in the key.** Separated, one of them gets fixed and the
others are forgotten.

⚠️ **`L42` and `L46` are quiet by construction on a work that names no grammar.** A
specification on `video-spec` has no grammar to register; an `aim` that does not start with
`grammar:` is free prose and is left alone. **A work that names nothing is not a work that
failed**—the notes say how many were looked at, so silence stays legible.

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
- **A grammar card's `## Written into` prose.** The check reads the registry's `written_into`,
  not the card's list—**the card writes `§9 ACTION`, the registry writes `"9. ACTION"`**, and
  **the checker only ever opens the registry.** The two lists are kept in step by `L42`'s
  coverage note, which names any card on disk that the registry does not hold.
- **The registry's `essential_moves`, `grounding` and `failure`.** These are the grammar's
  meaning, and **no check compares them to the specification.** `L45` reads only
  `negative_conflicts`; **whether a device is doing what its card says cannot be read from
  here.**
- **`dramaturgy.set_pieces[].why`.** `L42` compares the set piece's `format` with §6 and
  nothing else—**whether the set piece earns its place is the author's judgement.**
- **The board.** No shot record field points at `specs/board/`, so **no check opens it**
  ([`docs/usage.md`](usage.md)).

## Where to read more

- [`engine/ledger/README.md`](../engine/ledger/README.md) — every layer, what it reads, and
  what it does not.
- [`engine/shot/README.md`](../engine/shot/README.md) — §6 and its unstable shape.
- [`references/formats/video-spec.md`](../references/formats/video-spec.md) — the format card
  this repository carries.
