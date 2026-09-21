---
name: design
description: 'Stage ② of semantic-visual-loom — stage a shot, and specify it. Use after the shots exist, when a shot has to become something a generator can be handed. Decides place, time, mode, motion, beats and duration, then writes the video specification of sections 1-20 and the image specification, and takes the identity from section 19. Emits the staging record and both specification documents — not the reference sets.'
argument-hint: '(optional) the project name, or the shot to stage. e.g. /semantic-visual-loom:design hitosara'
---

<!-- i18n-version: 1.0.0 | canonical: skills/design/SKILL.md | translated: 2026-09-14 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# design — ② staging a shot

**① said what changes. ② says where the camera stands, at what moment, what moves, and what
the generator is handed.** The record it writes is **the same artifact ① opened** — plus two
specification documents per shot, which are the only things a generator ever sees.

⚠️ **This is a document, not a program.** It instructs a session. **There is no code for
stage ② in this repository** — the only command that runs is the checker, and it runs against
**the records this stage writes.**

## What this stage owns

| | What | Where |
|---|---|---|
| **the staging record** | `place` · `time` · `mode` · `motion` · `beats` · `duration` · `spec` · `key_image` · `aim` · `text_channel` | `projects/<name>/shots/<id>.yaml` |
| **the video specification** | §1–20 in the registry's order, §18's 7 slots, §19's self-name | `projects/<name>/specs/video/<id>.md` |
| **the image specification** | named paragraphs inside one section — `Prompt`, `Negative` | `projects/<name>/specs/image/<id>.md` |
| **the board prompt** | ⚠️ **only on the video route that goes through a storyboard** — the ① of that route: a storyboard sheet for `distill-essence-engine` (`storyboard` × `luminous-anime`) | `projects/<name>/specs/board/<id>-board.md` |

**It does not own** `reference_set` / `forbidden_set` / `attached` / `disclosure_state`
(those are **③ `ledger`**). ⚠️ **They are derived, not written here** — this stage decides
what the shot *is*, and ③ computes what it is *allowed to show* from the ledger.

⚠️ **① and ② write one artifact.** Do not read the boundary as a directory boundary — read it
as **which decisions are made where.** The shot file on disk looks the same in the middle of ②
as it does at the end of it.

## The order of decisions

⚠️ **This order is a design claim; the checker does not enforce it.** The layers run in an
order of their own. What follows is the order that **makes a thing exist before something
reads it** — and one edge in it is load-bearing: **`place` and `time` come before `beats`,
because `L3` and `L4` read the beat body, not only the field.**

1. **`place` — exactly one.** Drawn from the continuity vocabulary ① opened
   (`locations:` in `ledger.yaml`). ⚠️ **The value does not travel.** What reaches the
   generator is `prompt:Visual Prompt` **and** `handover:distill` — **the field points at
   something, and the something is what arrives.** Measuring `place` by value produces
   dozens of false positives; only `duration` may be compared as a value.
   **Fires if wrong:** `L2` (*split the shot, or add the place to the ledger*).
2. **`time` — exactly one.** **Fires if wrong:** `L3`. ⚠️ **`L3` reads two places.** A singular
   `time` is not enough — if the beat bodies carry **three or more kinds** of time word, the
   shot spans them, and `L3` says so. **Write less in the beats, or split the shot.**
   ⚠️ **Wardrobe is resolved by place × time, not by time** — that rule is not machine-readable
   yet (see the holes below), so write both so a person can resolve it.
3. **`mode`** — one of `MODES`: `still` · `motion` · `composite`. ⚠️ **The meaning is "does the
   subject move."** `still` = **the subject stops** — light and dust still move, and the frame
   is not frozen. `composite` = the subject stops **and the picture is a composite of layers**
   (the generator is never asked to draw text; `timeline`'s `text_events` burns it).
   **Fires if wrong:** the schema's enum · `L24`.
4. **`motion` — `subject` · `quality` · `law`, and it is required in every mode.**
   ⚠️ **`mode: still` needs it too** — **in film, motion is the ground and stillness is the
   special case.** An empty field is not "no motion declared"; it is
   **"the destination of §11 is empty."**
   **Fires if wrong:** `L16`. ⚠️ **`L16` does not read `mode`** — so do not reason
   "this is still, motion is optional." That rule is dead.
5. **`beats`** — `range` · `density` · `what`, at least one. ⚠️ **`density` is not a binary**:
   `sparse` · `held` · `dense` · `transition`. Measurement widened it — most beats in a real
   work are **held** (sustained), which is not "dense".
   **Fires if wrong:** `L3` (time words in `what`) · `L4` (a movement verb in `what`).
   ⚠️ **`L4` never fires alone.** A movement verb is **a violation only when `place` actually
   spans** — otherwise it is a note, because `→` is a sequence of organs, `Then` is a time
   connective, and `moves to` means "is about to". **Write a detector for one work and it
   false-positives on the next one.** Do not "fix" a note here.
   ⚠️ **`what` is Japanese and does not travel.** Only `range` and `density` enter the Master
   Prompt's `{BEATS}`.
6. **`duration`** — `"<n>s"`, matching §1's `Duration:` exactly.
   **Fires if wrong:** `L23`. ⚠️ **There are three durations and only two of them are here.**
   The record's `duration` is the **intent**; `take.params.duration` is the **generation**;
   `timeline.clips[].in`/`out` is the **adoption**. **Intent does not bind adoption** — the
   author finds the right length per take. ⚠️ **This is the only field the checker may compare
   by value** (33 of 33 agreed, measured).
7. **The video specification, §1–20** — in `specmap.SPEC_SECTIONS`' order, all twenty. Write
   `spec:` in the record to point at it. **Fires if wrong:** `L11`.
   ⚠️ **Two failures are different and live in different layers.** "§1 is missing" is `L11`;
   "§1 is there but has no `Duration:` line" is **`L23` and nobody else.** A requirement that
   cannot be matched up **is not being matched up.**
8. **§18's 7 slots** — `Master Prompt` · `Visual Prompt` · `Motion Prompt` · `Camera Prompt` ·
   `Audio Prompt` · `Negative Prompt` · `Style Motion`. **Fires if wrong:** `L17`.
   ⚠️ **A slot may exist and carry nothing.** `Style Motion`'s source is the style card's
   `Motion character`, and **most style cards do not have one** — a card without it makes the
   slot present and empty, and `L17` passes it. **Fires if wrong:** `L20`.
   ⚠️ **Pick a style whose card carries `Motion character`, or record why the slot is empty.**
   ⚠️ **§18's heading names the model, and the name decides the route** (`specmap.MODELS`).
   **`WAN 3.0` attaches a `key_image`; `MINIMAX H3` attaches a storyboard image and has no image
   path at all; `SEEDANCE 2.5` attaches nothing by default.** On that second route **this stage also writes the board prompt** (the row in the
   table above) and points at it from §6's `REF_BOARD`. ⚠️ **The board is not a `key_image` and
   must not be written as one**——**its paper draws lettering** (panel numbers, captions, margin
   columns), and **the image path's floor forbids text on screen.** ⚠️ **Nothing checks the
   board**: no field points at it, so **`check.py` never opens it. A hole.**
   ⚠️ **On this route a panel is a scene, not a frame of one take.** The source method the route
   came from says **treat each panel as its own scene and join still to still with natural
   animation** — so **§18's `Master` / `Camera` / `Motion` must not forbid that join.**
   ⚠️ **`no cut` written as a blanket rule closes the only lawful way for a panel to change
   place**, and the generator answers by running two places together as one room.
   **Forbid the cut to an unrelated location; do not forbid the transition** — and when a panel
   changes place, **the specification must say how it changes, because the source does not**: it
   never uses the word カット, so **cut-versus-continuous is the shot's own decision, and leaving
   it unwritten is how two places come back as a single room.**
   ⚠️ **`one continuous take`** ([`references/video-spec.md`](../../references/video-spec.md)) **is
   the `WAN 3.0` house style and does not carry to this route.** The routes do not share a
   grammar of time, and **the string handed over must say what this route does, not what the other
   one does** — the failure that produced this warning is recorded in `HISTORY.md`.
   ⚠️ **The full list of the constraints that hold on this route — the strings handed over and the
   paper alike — is [`docs/h3-route.md`](../../docs/h3-route.md).**
   ⚠️ **On the third route the gate is the slot, not the phrase.** **`SEEDANCE 2.5` does not
   receive `Negative Prompt` as a floor** — the vendor honours negation only for subtitles and
   audio, and the rest of that slot is read as prose. **`L30` fires when a specification on that
   route fills the declared slot** (`specmap.MODEL_UNRECEIVED_SLOTS`). **When you write one: put
   the prohibitions in the slots that are read, in the affirmative** — `Master`, `Visual`,
   `Camera`, `Motion`, `Audio`. ⚠️ **Do not empty the `Negative Prompt` slot to stop the
   fire** — `L21` requires it to cover the floor, so emptying it fails a different check, and
   **the record of what the work forbids is not the same thing as what the route can hear.** ⚠️ **The
   fire stays until the work declares `bible.route_limits_accepted`** — **an exclusion is the
   work's to write**, and writing it is a decision for the author, not for this stage. The route's
   constraints are [`docs/seedance-route.md`](../../docs/seedance-route.md).
9. **The image specification** — ⚠️ **not sections.** It is **named paragraphs inside one
   section**: `Prompt` first, `Negative` second, in that order. Write `key_image:` in the
   record to point at it. **Fires if wrong:** `L18` (the shape of the path).
   ⚠️ **Why paragraphs and not sections**: the author selects the whole thing **in one
   gesture**, and a heading between them would be swept into the selection. **The recipe lives
   in `specmap.SPEC_KINDS`; do not re-derive it.**
   **Fires if wrong:** `L21` (the Negative does not cover `bible.negative_base` — **cover, not
   equal**) · `L22` (one of the 7 fields is empty, or the card it names does not declare it).
10. **§19's `Instance ID`** — ⚠️ **the identity is taken from the specification side, not from
    the record side.** The shot's `shot` id is that string with the trailing
    `-<seconds>s-<take>` dropped. ⚠️ **Never from `Segment ID`** — the same range carries two
    spellings there, and deriving from it drops records.
    **Fires if wrong:** `L13`.
11. **`text_channel`** — only `composite` requires it, and the three kinds go to three different
    places: `overlay` is burned by `timeline` (**the generator does not draw text**), `voice`
    goes to §14 as the Audio Prompt, and **`lettering` is drawn by the generator inside the
    picture** — its destination is §18's `Master Prompt`. **Fires if wrong:** `L24` (a `composite`
    shot must carry at least one `overlay` — **`lettering` burns nothing, so it does not count**).
    ⚠️ **`lettering` says who draws the text and nothing about whether it can be read.** **That is
    the shot's own decision, written into §18's slots** — a work may need one shot that is legible
    and another that is not, and **a kind that fixed legibility would be too narrow for both.**
12. **Run it.**

```bash
python3 engine/ledger/check.py projects/<name>   # read the violations AND the notes
python3 engine/ledger/check.py --self-test       # confirm the checker fires at all
```

## ⚠️ What is still red when this stage ends

⚠️ **This is where zero violations becomes reachable — and it is not yet the exit condition.**
② closes the record, but **the sets ③ derives are still empty**, so the checker is still red.

| Expected red at exit, and whose it is | |
|---|---|
| `L5` · `L6` · `L8` · `L7a` and `L7b` beyond the declared points | **③ `ledger`'s** — the sets are derived there |
| `L9` | **③ `ledger`'s** — it fires when the disclosure check is *empty* |
| `L25` | **nothing has been generated** — and this stage does not generate |

⚠️ **The layers ② owns should now be quiet.** If `L11`, `L16`, `L17`, `L18`, `L20`, `L21`,
`L22`, `L23` or `L24` is still firing, **this stage is not done** — and the note each one
prints tells you which decision above it belongs to.

## ⚠️ Fields and rules that nobody reads

⚠️ **Write these down as holes. Do not fill them in with a rule.**

- **`effect` and `sound` are read by nobody.** `semantic.py`'s own module docstring states it:
  two fields still have no reader, and these are the two. ⚠️ **`sound` is not unread because it
  is unimportant** — its destination is declared (`handover:loom`, the audio foundation) and
  **the contract with that side's Scene Definition is undecided.** A field whose reader is in
  another repository is **a hole, not a defect.** Note also that `sound`'s `scene_ref` is not
  required — **an empty `sound` passes the form layer too.**
- **Matching `motion.law` is deliberately not written.** The three parts now exist (§18's
  `Style Motion` slot, the record's `motion`, and `bible.style`), but **the check that ties them
  together does not** — and ⚠️ **writing it now would produce a check that never fires**,
  because `motion` is empty across every shot on disk and **the style cards live in
  `distill-essence-engine`, which someone who cloned this repository does not have.**
  **With the other side empty, nothing fires** (the same discipline as "do not call empty OK").
- **`Style Motion`'s contents are not compared to the card's `Motion character`.** `L20` looks
  at the **existence** of `Motion character`, never at whether what it pulled matches `motion`
  or the slot. Same reason as above. **When it cannot be read, report "cannot be confirmed."**
- **The handover sheet does not exist.** The layer that assembles **what is passed from the
  record to the generator** (§18's 7 slots, `take.params`, the image prompt, the sound) is not
  built. What `L19` looks at is **the declaration of a destination**, not **whether the
  assembled text actually carries that field.** ⚠️ **Add the round-trip check at the same time
  as that layer**, or it will never be verified that the aim arrives.
- **`beats` density has no lower bound.** The form layer asks for `minItems: 1`, and the only
  other readers of the beat body are two keyword counts (`L3`'s time words, `L4`'s movement
  verbs). **One beat, or twelve, both pass.** That is a judgment, and it stays one.
- **§11's subsections are four and `motion`'s fields are three — not one to one.** §11's
  Physical Characteristics alone carries five items (weight, inertia, acceleration, fluidity,
  and so on). **Do not read the field list as a table of contents for §11.**
- **`L24` cannot read whether §11's prose actually stops the subject.** The prose may say
  "the dough swells" — and this layer cannot read that as *is the subject stopped*. So it
  reports **a note**, and it does not match the vocabulary's strings. ⚠️ **A check whose
  strings were written to match my own sentences is a check I made for my own text** — it is
  the same thing as an empty check. **Do not build one.**
- ⚠️ **`timeline/` is the ordering authority and does not exist.** The checker falls back to
  the natural order of the shot ids — `Project.order()`'s own docstring says that when
  `timeline/` arrives, **that should be treated as authoritative (undecided).** So do not treat
  the id order as a design decision; **it is a stand-in.**
- **Wardrobe resolution is not machine-readable.** Which `states.<name>.wardrobe` applies is
  resolved from `place` × `time`, and deriving that from prose produces false positives (a
  classroom at night, a school-festival yard at night, a room at dawn). **The conditions are
  confirmed against the artifact side. Record the reading; do not write a rule.**

## ⚠️ What the checker does not decide here

- **Whether the staging is any good.** Every field above is checked for **shape, presence and
  agreement**, never for whether the shot is worth making. **No check reads the quality of a
  specification** — and one should not be invented on the record side.
- **Whether the model §18 names is the right model.** `L18` sees whether the name resolves to
  the registry. **Which model a shot deserves is a judgment.**
- **What the work's prohibitions should be.** ② writes what `bible.negative_base` says; it does
  not decide the list.

## Language

- **Everything that reaches the generator is English.** §1–20, the prompts, the Negatives, the
  slot texts — **write them in English and do not translate them.** Translating changes the
  output. **This is the stage where that bites**, and it is the single most consequential rule
  on this page.
- ⚠️ **The exception is the record, not the specification.** `motion.subject` / `beats.what` /
  `unit.before` are free text and may be Japanese — they are **records**, and a record may be
  written in the language the work is thought in. `beats.range` (`"0-6s"`) and `beats.density`
  (`sparse`) are **English**, because they are inserted into the Master Prompt verbatim.
  **Read the destination table before deciding: the question is never "is this Japanese," it is
  "does this string arrive."**
- **The canonical of the documents is English**, and the mirrors sit beside it in the same
  directory — see [`CLAUDE.md`](../../CLAUDE.md).

## Where to read more

- [`engine/ledger/README.md`](../../engine/ledger/README.md) — every layer, what it reads, and **what it does not see**
- [`schemas/shot-record.schema.json`](../../schemas/shot-record.schema.json) — the record's form, and the reason each field exists
- [`docs/usage.md`](../../docs/usage.md) — the commands, and how to read the exit code
- [`projects/hitosara/README.md`](../../projects/hitosara/README.md) — a work that went through all of this
