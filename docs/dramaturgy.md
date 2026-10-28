<!-- i18n-version: 1.0.0 | canonical: docs/dramaturgy.md | translated: 2026-10-29 -->

**Language:** [English](dramaturgy.md) | [日本語](dramaturgy-ja.md) | [中文](dramaturgy-zh.md)

# Dramaturgy — the ledger's third register

**The production ledger holds what is true.** Continuity holds **the state of the world**;
disclosure holds **the state of the audience's knowledge**. Both answer *what is the case.*

⚠️ **Neither answers what the changes are worth.** A shot can do exactly what its `unit` says
and still be a shot nobody remembers. **Dramaturgy is the third register**, and it is where the
work decides that.

**It is not a fifth stage.** It is a register in the same `ledger.yaml` — **the ledger is not
split** ([`CLAUDE.md`](../CLAUDE.md), Fixed Policy). Continuity, disclosure and dramaturgy are
**three questions asked of one file**, and the reference set and the forbidden set are still
derived from that one point.

## Why it is in the ledger and not beside it

The failure that produced the one-ledger rule was **"which reference image goes with which
shot"** — a question that is at once continuity and disclosure, and that becomes unanswerable
when the two are kept apart.

**Dramaturgy asks the same kind of question.** "Does this shot have a grounding shot beside it"
is a question about **the world** (continuity), about **what the audience is allowed to see**
(disclosure), and about **what the device is for** (dramaturgy). Put the third in its own file
and the three answers drift apart while each is internally correct.

## What it holds

```yaml
dramaturgy:
  version: 1
  premise: "…"          # what happens, in one line
  question: "…"         # what the audience carries to the end
  argument: "…"         # what the work says — a sentence someone could disagree with
  visual_thesis: "…"    # the same argument in light, colour and composition
  value_poles:
    - ja: 安全
      en: safety
    - ja: 危険
      en: danger
  acts:
    - id: act-1
      shots: [s01, s02, s03, s04]
      turn: "…"          # the act's one change
      climax: s03
      value_from: 安全
      value_to: 危険
      rhythm: "溜め → 爆発 → 余韻"
  sequences:
    - id: seq-1
      shots: [s01, s02, s03]
      contrast: "静 → 動"
      escalation: "…"
      transition: "…"
      payoff: s09
      flat: false
  motifs:
    - id: light
      first: s01
      recurrences: [s04, s07]
      payoff: s12
  set_pieces:
    - shot: s07
      format: impossible-camera   # must match the shot's §6 REF_FORMAT
      why: "…"
  sound_arc:
    silence: [s01, s02]
    score_enters: s03
    note: "…"
  ending_image: "…"    # the last thing that remains
```

⚠️ **`acts` and `sequences` are a view laid over shots, not a generation unit.** **The shot
remains the unit.** One shot is still one change; an act is a way to read four of them.

⚠️ **`payoff` may point forward.** A scheduled payoff is not a state — the same discipline as
`… yet` in the continuity ledger. `L41` checks only that the target exists.

⚠️ **`flat: true` without a `note` is not a declaration.** A sequence whose tension curve is
deliberately level says **why**; `L44` fires on the bare flag.

⚠️ **`value_poles` is the work's own mapping**, `{ja, en}`. The records write the Japanese;
`DIRECTION` carries the English. ⚠️ **The `en` must be a word that literally appears in the
section** — `L43` looks for it and does not follow inflections or synonyms. **A value with no
opposite is a setting, not a stake.**

## The shot's dramatic record

```yaml
# shots/<id>.yaml
dramatic:
  function: 転換              # 設定/上昇/転換/発見/決断/結果/溜め/解放/余韻
                              # or 質感/余白/様式美 for non-narrative shots
  value:
    from: 安全
    to: 危険
    stake: "父の記憶"
  audience:
    feel: "息を止める"
    expect: "彼が扉を開ける"
    know: "母がまだ生きている"
  button: "閉じた扉の向こうの光"
  performance:
    objective: "娘を守る"
    obstacle: "扉が開かない"
    tactic: "体で押す"
    subtext: "許しを請う"
    intensity: 8
```

⚠️ **`value` is the value of the shot's one change, not a second change.** `unit` says what
changes; `value` says what it cost. **Two readings of one change** — a shot that needs a second
value turn is two shots.

⚠️ **Non-narrative functions** (質感・余白・様式美) **need no value turn** — but they still need
a `button`, because every shot ends on an image.

⚠️ **`function` and `role` are different axes.** `role` is that shot's job (`L15` reads it);
`function` is where the story is when the shot happens (`L40` reads it). Their vocabularies
overlap (転換, 余白, 様式美) — ⚠️ **do not infer one from the other.**

⚠️ **`audience.know` is not `disclosure_state`.** The latter is a fact about the world; the
former is what the audience holds at this moment. **No layer compares them** — whether the
audience is ahead of the characters is a judgment, and a layer that guessed it would be writing
the story.

⚠️ **`performance` is expected where a person is present and `mode: motion`**, and its absence
is **a note, not a violation** — some shots have nobody in them. ⚠️ **`objective == obstacle`
fires `L47`**: an objective its own obstacle restates is an explanation, not a wish.

## The `DIRECTION` section

A specification **may** carry one unnumbered section between §17 and §18:

```text
DIRECTION  ← ledger.dramaturgy + shot.dramatic + §12 EMOTION
  Play {FUNCTION} for {AUDIENCE_FEEL}. The value turns from {VALUE_FROM} to
  {VALUE_TO}; the stake is {STAKE}. Use {DEVICE} only to {DEVICE_WHY};
  keep {INVARIANT}. End on {BUTTON}.
```

⚠️ **It is not a slot.** `PROMPT_SLOTS` stays seven, so `L17`, `L28` and `L30` are unchanged.
**At generation time its body is prepended to `Master Prompt`** — an independent section in the
specification, the first paragraph of Master at the generator.

⚠️ **This is the first route emotion has ever had to the generator.** §12 EMOTION is a
specification section that feeds **no slot** (`specmap.PROMPT_SLOT_SOURCE`) — before this, the
shot's feeling was written and filed.

⚠️ **It is not a summary of the staging prose.** The staging summary is written **to be read**
and is explicitly not a source ([`skills/design/SKILL.md`](../skills/design/SKILL.md)).
`DIRECTION` is **written** from the ledger, the shot record and §12 — **not translated from the
Japanese record.** The English is a type, not a rendering.

## What a sequence constrains

`contrast`, `escalation` and `transition` describe a sequence. **Three more fields constrain
it, and each can be checked against a shot** — they are the first part of dramaturgy that
reaches the frame rather than the page.

```yaml
sequences:
  - id: seq-2
    shots: [s04, s05]
    withheld:
      - shot: s04
        wanted: "the flame entering the lantern — the audience is waiting for it"
        given: "it does not light. The flame is never in this film."
    cuts: [s05]
    tempo: [9, 9]
```

⚠️ **`withheld` is the seat for what the audience wanted and did not get.** `wanted` and
`given` must differ and neither may be empty: **giving what you promised is deferring, not
withholding, and giving nothing is an accident, not a choice.** `L48` reads it. **A withholding
on the work's last shot is a note, not a violation** — refusing to show can be the ending.

⚠️ **`cuts` is the cut a shot is not allowed to decide alone.** A cut means something only next
to the shot beside it, so **the sequence declares it** and the shot record carries
`cut: internal`. `L49` checks both directions **and opens the specification's text**: change the
record and not the prose, and the generator — which never reads the record — still makes one
continuous take.

⚠️ **`tempo` is the sequence's shape in seconds; the shot's `duration` is the source of truth.**
`L50` compares the copy. **Three or more equal values fire** unless the sequence declares
`flat: true` with a `note` — a level rhythm can be the design, and its flatness can be the trap
that makes the next change land.

⚠️ **None of the three makes a sequence good.** They are the seats where the work spends what
it knows the audience wants.

## What the checks read, and what they do not

| layer | reads | fires on |
|---|---|---|
| `L40` | `dramatic.function` / `value` | a narrative function whose `value.from == value.to` |
| `L41` | `dramaturgy.acts` / `sequences` | an act with no `turn`; a sequence with no `contrast`; a `payoff` or `shots` entry that does not exist |
| `L43` | the `DIRECTION` section, `dramatic`, `value_poles` | a shot with `dramatic` and no section; the English function missing; a value's English missing |
| `L44` | `beats[].intensity` | the same intensity across three or more shots; no peak in an act |
| `L47` | `performance.objective` / `obstacle` | the two are the same |
| `L48` | `sequences[].withheld` | a wanted element equal to what was given, or either left empty |
| `L49` | `sequences[].cuts`, `cut: internal`, the specification's text | a cut declared on one side only; a spec that still says one continuous take |
| `L50` | `sequences[].tempo` against the shot's `duration` | a length mismatch; three or more equal values with no `flat: true` and `note` |

**None of them reads whether the turn is good.** The curve can be flat, the values trivial and
the acts arbitrary, and every layer passes — **that is the design.** Quality belongs to the
[council](../skills/review/SKILL.md) and to the author.

## ⚠️ Records opt in; absence is not disagreement

**Every field here is optional.** A work with no `dramaturgy` and no `dramatic` passes, and its
notes say how many shots were looked at.

⚠️ **Do not backfill.** A `function` written after the fact is not a function, it is a
description — the same discipline `aim` carries. ⚠️ **A work that was made before this register
existed is not made wrong by it.**

**The switch is the record, not a version.** There is no `format-version:` field and none is
read; a shot with `dramatic` is in scope for `L40`/`L43`/`L47`, and a shot without it is not.
**The engine does not remember which works are special.**

## What is not read

- **Whether the premises, the argument or the ending image are any good.** Prose, and the
  author's judgment.
- **`set_pieces[].why`.** `L42` compares the set piece's `format` with §6 and nothing else.
- **`sound_arc`.** No layer opens it — it is a decision, not a field with a reader.
- **`motifs[].recurrences`.** Listed so the author can see the shape; nothing resolves them.
- ⚠️ **Whether the audience felt anything.** Generation happens outside this repository, and
  **this register never claims to have measured it.**

## Where to read more

- [`skills/direction/SKILL.md`](../skills/direction/SKILL.md) — the stage that writes the register
- [`skills/design/SKILL.md`](../skills/design/SKILL.md) — the step that writes `DIRECTION`
- [`skills/review/SKILL.md`](../skills/review/SKILL.md) — the council that judges it, and how
- [`schemas/ledger.schema.json`](../schemas/ledger.schema.json) — the `dramaturgy` shape
- [`schemas/shot-record.schema.json`](../schemas/shot-record.schema.json) — the `dramatic` shape
- [`references/formats/video-spec.md`](../references/formats/video-spec.md) — §12 EMOTION and the `DIRECTION` section
- [`docs/cards.md`](cards.md) — the format cards, which are the devices
