---
name: staging
description: 'The camera, decided in one hand — the part of stage ② that decides where the bodies are staged, where the camera stands, what the style permits it, how many camera events the shot has, and why each prohibition exists; then writes §9 Blocking and §10, and carries them into §18’s Camera Prompt without dropping the reasons. Use inside design (②), after motion and duration and before the specifications are written. ⚠️ Not a fifth stage and not a new field.'
argument-hint: '(optional) the project name, or the shot to stage. e.g. /semantic-visual-loom:staging hitosara'
---

<!-- i18n-version: 1.1.0 | canonical: skills/staging/SKILL.md | translated: 2026-10-29 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# staging — the camera, decided in one hand

**① said what changes. ② decides the shot. This document is the part of ② that decides the
camera — and it exists because the camera was being decided in two places at once.**

⚠️ **It is not a fifth stage, and it adds no field.** It runs **inside ②**
([`skills/design/SKILL.md`](../design/SKILL.md)), at step 7 — **after `motion` and `duration`,
before the video specification is written.** What it writes is **§9's `## Blocking`**, **§10**,
and **§18's `Camera Prompt`** — all of which the specification already had. Nothing new lands on
disk.

## ⚠️ Why this exists: one decision, written twice

The camera is written twice in one specification — once as **a design decision** (§10 `CAMERA`),
once as **the string that actually reaches the generator** (the `Camera Prompt` slot of §18).
The format card has always said the second is derived from the first:

**`Camera Prompt` is drawn from §10 — the camera events in order: timing, movement, target, speed,
transition** ([`references/formats/video-spec.md`](../../references/formats/video-spec.md) §18, and
`specmap.PROMPT_SLOT_SOURCE` carries the same line).

⚠️ **§18 is the only section a generator ever receives.** So when the two are written in different
passes — §10 by whoever designs the shot, §18 by whoever assembles the prompt — **the reasons stay
in §10 and §18 keeps only the prohibitions.** What the model is handed is
**"no pan, no push, no rack"**, with nothing saying what the hold protects. The camera reads as
**never placed**, and the shot reads as the thing this foundation keeps re-learning:
**a slideshow, or liquid moving for its own sake.** The published failure is in `HISTORY.md`.

⚠️ **A prohibition with no reason is not a decision — it is a habit.** And a habit cannot be
revised: the next shot inherits it, and the shot after that treats it as the style.

## The order of decisions

⚠️ **This order is a design claim; one edge of it is checked** (decision 7, through `L33`).
Decide them in this order **and write each one down as you go** — decision 3 is what makes the
others reachable.

**1. Where the camera stands — and what it is.** This is §10's `Camera Language`, and it is
**not the same question as "what does it do."** ⚠️ **"A place it is put" and "a premise that is
dropped" are both answers**, and they are written in the same line: a macro frame at the subject's
own scale with the plane of focus razor-thin, or **a page that does not travel, because the premise
"a camera is somewhere" has been dropped.** Say which one this shot is.
⚠️ **Say what the camera wants.** A placement is not a prohibition. Write, in one line, **what
this camera is trying to show the audience** — and let the prohibitions follow from it. **A camera
that wants nothing produces a slot that forbids everything and does nothing**, and the audience
cannot tell it apart from a camera nobody placed.
⚠️ **Write the style's physical law here too** — what movement costs in this style, and how fast it
may be. The card's `## Motion character` is where that is written (**read it; do not touch it**),
and decision 7 is where it has to survive.

**2. Where the bodies are — blocking.** ⚠️ **The camera cannot be decided before the stage is.**
Blocking is **where each person stands, where they enter and leave, how high they are, and how far
apart from each other and from the frame's edge** — and it is written in **§9 ACTION's
`## Blocking` subsection**, not in §10. §10 is the camera; blocking is the stage picture the
camera is placed against. ⚠️ **The two are decided together and written apart**, and a shot where
they were decided separately reads as a camera pointed at a room rather than at a person.
- ⚠️ **Blocking must answer to `unit`.** Where the body is at the shot's start is the place of
  `unit.before`; where it ends is the place of `unit.after`. **A body that does not move in `unit`
  must not move in blocking** — the change is one, and the stage picture is where it is visible.
- ⚠️ **Height and distance are the two cheapest things in cinema and the two most often left
  unwritten.** Below, above, across the room, at the frame's edge, with the back turned — **each
  of these is a decision the audience reads instantly**, and none of them exists unless it is
  written.
- ⚠️ **Nothing checks blocking.** `L33` reads the camera against the style and `L47` reads the
  performance record; **the stage picture is unmeasured.** A hole, recorded as one.

**3. Where the decision is kept — the work's own document.** ⚠️ **The camera is kept in §10 of
`specs/video/<id>.md`, not in the session.** This is not bookkeeping: **§18 is *derived* from §10**,
so a decision that lives only in the conversation **has no source to be derived from** —
and the derivation does not fail loudly; it produces a slot full of prohibitions.
**Write the decision *and its reason* into §10 first.** §18 is then a copy that carries them,
and copying is a thing a check can see.

⚠️ **A work that keeps one shot on more than one route places the specifications under
route-named directories** — `specs/video/<route>/<id>.md`, one per route. **`L39` reads the
pair**; a work with a single route keeps them where §10's path says.

**4. The budget — what this shot spends, and what it does not.** Movement is not free in any
style, and it is priced differently in each: **in one style a focus rack is a full gesture; in
another, a camera that travels spends the picture's whole reserve.** Two rules hold here:
- ⚠️ **The style owns the camera. The format may narrow it — it may never invert it.** A card that
  permits a drift cannot come back as a shot whose specification reads *movement is impossible*.
- ⚠️ **A decline is written as a decline, not as an impossibility.** The form is
  **"The style permits a focus rack; this shot spends neither."** A shot that holds is a shot that
  **chose to hold** — write it that way, in §18, because §18 is what reaches the model.

**5. Derive it from the person and the scene — not from taste.** The camera is a consequence of
**`role`** (that shot's job), **the person in the shot**, and **`place` × `time`**.
⚠️ **The vocabulary for this already exists and nobody points at it.** `rolemap.py`'s
`MOTION_PATTERNS` carries a frame group — **カメラのみ** (its own criterion: **運動が何を開示するか・
速度曲線・被写体との関係**), **停止** (**停止の張力・その静止が意味するもの**), and **時間の運動**
(**その速度である理由・速度が開示するもの**). These are reachable only as **`運動（…）`** in `role`
(the qualified spelling, full-width parentheses). ⚠️ **Step ②'s `motion` never points there** —
which is why a shot whose *camera* is the mover ends up with an empty `motion` and a camera nobody
decided. **When the camera itself is the subject, say so in `role` with the qualified spelling,
and judge the shot by that pattern's criterion.** ⚠️ **`L15` reports the qualified spelling as a
note, never as a violation** — so **nothing forces you to name the pattern, and naming it is the
whole point.**

⚠️ **The moves are named, and the names are in [`references/camera/index.yaml`](../../references/camera/index.yaml)**
— 100 techniques, each with its English line, the `MOTION_PATTERNS` group it belongs to, the
`role`s it can serve, the grammar it most often pairs with, and where in the shot it usually sits.
**Read the style card first, then this** — the card decides what a movement costs, and **the
catalog does not know the style.** ⚠️ **It is a map, not a menu.** An entry's `roles` is **the set
of jobs the move can do**, not a choice between them: **the shot's `role` decides what the move is
for**, and **a move asked for by taste alone is a move the scene did not ask for.** ⚠️ **Every
entry is `status: draft`** — the mapping was applied from general film practice and **has not been
measured against any work's own shots**; when a work's use disagrees, **the work wins and the
catalog is corrected.** Take the chosen entry's `en` line into §10, and derive §18 from it —
**the technique's name is not handed to the generator; its English line is.**

**6. How many camera events — in the policy's own vocabulary.** The unit of the shot is
**one change** — and one change is **one camera event**
([`CLAUDE.md`](../../CLAUDE.md), Fixed Policy). §10's `Camera Events:` line carries each event
**with its range**: `0-8s` none; a push at `2-5s`. ⚠️ **A hold is an event, not an absence of
writing** — "none" is a decision, and it is written with a range like any other.
⚠️ **The card asks for four things per event — timing, movement, target, speed** — and
**a prohibition is far easier to write than a placement.** "No pan" says what must not happen;
it does not say **where the camera goes, toward what, and how fast.** ⚠️ **When the shot holds,
write what the hold is spent on; when it moves, write all four.** §18's derivation adds
`transition`.

**7. The reason for every prohibition — written where it can travel.** Every prohibition in §18's
`Camera Prompt` must be derivable from a reason written in §10, **and the reason must arrive with
it.** Two disciplines, both already the foundation's:
- ⚠️ **An override is written as an override** — in the work's own record, never by editing the
  other side's card ([`CLAUDE.md`](../../CLAUDE.md), Fixed Policy; and *Things That Must Not Be
  Broken*: **the cards are `distill-essence-engine`'s property — read them, do not rewrite them**).
- ⚠️ **The reason travels *into the slot that reaches the model*.** A reason that stays in §10 is
  a reason the generator never hears — and this is the failure that produced this document.

## What gets written, and where

| | Where | What it carries |
|---|---|---|
| **`## Blocking`** | §9 of `specs/video/<id>.md` | where each body stands, enters, leaves; height, distance, the stage picture |
| **`Camera Language`** | §10 of `specs/video/<id>.md` | where the camera stands, what it is, what it wants, and the style's physical law |
| **`Camera Events`** | §10 | each event with its range — timing, movement, target, speed |
| **`Camera Behavior`** | §10 | the reason, and what the hold is spent on |
| **`Camera Prompt`** | §18 | the events in order, **with the reasons carried** — the string that reaches the generator |
| **`Negative Prompt`** | §18 | what is forbidden. ⚠️ **The camera-stability prohibition is the known case: it is written in §10 and it reaches the model through this slot** — the format card says so itself |

⚠️ **One hand writes §10 and §18.** That is the whole mechanism: the loss this document exists to
prevent is a **handover** loss, and a handover between two hands cannot be checked into existence.

## ⚠️ The style owns the camera

- **Read the card's `## Motion character`** — it decides **what movement means in this style**:
  what the primary mover is, whether a held frame is permitted, how much movement is a full
  gesture. **§10 decides what moves in *this clip*.** The two are different questions, and a
  specification that answers the second without the first **overwrites the style**.
- ⚠️ **Do not touch the cards** ([`CLAUDE.md`](../../CLAUDE.md)). If this shot must go against the
  style, **the work writes the exclusion**, in the work's own words, on the record side.
- ⚠️ **The slot to check yourself against is `Style Motion`** — it is the seventh slot, drawn
  from the card and not from §1–17. If §18's `Camera Prompt` contradicts what `Style Motion` says
  the style does, **the specification has inverted the card** (see decision 4).

## What the checker reads (`L33`)

**One layer reads this stage: `L33` — *does §18's `Camera Prompt` forbid a gesture the style card
offers?*** It is deliberately the only one: **one check, whose comparison words come from the card
side and not from this document's prose.** ⚠️ **Blocking (decision 2) has no layer at all** —
**nothing reads §9's `## Blocking`**, and a stage picture is the one decision here that is
entirely the author's.

- **What it reads.** `bible.style` → that card's `## Motion character`; and
  [`cards.yaml`](cards.yaml), this side's reading of the 16 cards — **each `clause` and `quote`
  verbatim, re-verified against the card on every run** (if the quote is no longer in the card, it
  reports **"this side's reading is old"** and does not compare).
- **When it fires.** A gesture the card offers appears in §18's `Camera Prompt` **only inside a
  negation** — for example the card offers a focus rack and the slot says *no rack*. **A shot that
  merely never mentions the gesture does not fire**: silence is not a prohibition.
- **When it stays quiet.** When the card offers **no** camera gesture (then there is nothing to
  compare — reported as exactly that, not as a pass); when the card cannot be read; when no video
  specification was seen; when the acknowledgment form above is present.
- ⚠️ **What it does not see.** Whether §10 and §18 **agree**; whether the reason is any good;
  whether the hold was the right decision. **It reads the gestures this side wrote down, and a
  gesture nobody wrote down does not fire** — **a reading that is incomplete does not announce
  itself.** And ⚠️ **it does not read the `Negative Prompt` slot** — where, on some events, the
  camera prohibition actually travels.
- ⚠️ **Run it with the card directories pointed at** —
  `SVL_FORMATS_DIR=references/formats SVL_STYLES_DIR=references/styles`. **Without them this
  repository's own cards are not read**, and both this layer and `L20` fall back to notes.

## ⚠️ What this stage does not decide

- **Whether the camera is any good.** Nothing checks the quality of a specification, and **one
  should not be invented on the record side.**
- **Which route, and which model.** §18's heading names the model, and **that name decides the
  route** (`L18`). ⚠️ **The route decides what §18's `Camera` must not forbid** — on the storyboard
  route a panel is its own scene, and **`no cut` as a blanket rule closes the only lawful way for a
  panel to change place.** The constraints are
  [`docs/h3-route.md`](../../docs/h3-route.md) and [`docs/seedance-route.md`](../../docs/seedance-route.md).
- **The work's prohibitions.** §18's `Negative Prompt` covers `bible.negative_base`; the list is
  the work's, not this stage's.

## Language

- **Everything that reaches the generator is English.** The `Camera Prompt`, the `Negative`, every
  §10 line that is copied into a slot — **write them in English and do not translate them.**
- ⚠️ **The exception is the vocabulary's own spellings.** `運動（カメラのみ）` and `停止` are
  **`rolemap.py`'s strings**, read by `L15` — **translate them and the checker stops recognising
  them.** The question is never "is this Japanese", it is **"does this string arrive"**.

## Where to read more

- [`skills/design/SKILL.md`](../design/SKILL.md) — stage ② in full, and where step 7 sits in it
- [`references/formats/video-spec.md`](../../references/formats/video-spec.md) — §10's shape, and §18's derivations
- [`cards.yaml`](cards.yaml) — this side's reading of the style cards, and the `L33` index
- [`engine/ledger/rolemap.py`](../../engine/ledger/rolemap.py) — the role catalogue and the motion patterns
- [`engine/ledger/README.md`](../../engine/ledger/README.md) — every layer, and **what it does not see**
