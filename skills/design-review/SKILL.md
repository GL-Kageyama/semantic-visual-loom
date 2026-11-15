---
name: design-review
description: 'The design council — five seats read a work''s design package before breakdown, score it 0–100 on five lenses, and return findings with coordinates. Use to run an evaluation → revision loop before shots exist. ⚠️ It reads the design, not the picture; it advises, never rewrites.'
argument-hint: '(optional) the project and the episode. e.g. /semantic-visual-loom:design-review ukebi/ukebi-v3 ep03'
---

<!-- i18n-version: 1.0.0 | canonical: skills/design-review/SKILL.md | translated: 2026-11-16 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# design-review — the council before ①

**The design is the cheapest place to fix, and it has no gate.** `check.py` reads `bible` /
`ledger` / `shots` / `specs`; `review` sits after ④ and scores 1–5. This skill is the gate
that runs **before ①**, on the design package alone.

## What it reads

A work's design package: the work plan (`PLAN.md`) and one design note per episode
(`episodes/epNN.md`), plus the source they point at — the story design, the ledger entries,
the shot table, and the list of adopted images. **It does not read the prose as prose**,
**the shots**, or **the specifications**. They do not exist yet, or they are another stage's object.

⚠️ **The reader is the next session, not the audience.** The question is not "does the
audience understand?" — it is **"can this design be cut, kept faithful, and shot?"**

## The five seats

| seat | the question | what it reads |
|---|---|---|
| `change` | can every row be cut at one change? | the cut table, `unit`, static rows, multi-change rows |
| `continuity` | do the marks, the fire, the fold and the disclosure hold across episodes? | the plan's continuity rules, each episode's disclosure, the source's contradictions |
| `fidelity` | does the design keep the source's laws? | the story design, the ledger, the drafts |
| `feasibility` | can it be shot on the route with the adopted assets? | route, style, reference keys, `population` / `body_parts`, duration |
| `cinematic` | does the design promise a film? | specific images, camera, light, motion, rhythm, the pilot's set piece |

**Do not let one seat stand in for another.** A design can be faithful and unshootable;
shootable and dull; cinematic and unfaithful.

## The score

Each seat returns **0–100**. The work's score is the **mean of the five**. **Above 65 passes.**

⚠️ **The score is a judgment about the design, not a measurement of the picture.** Write which
object was read. A design can score well and produce a dull film; that is what "the generator
is a sample" means.

The scale is the sister councils' scale. It is intentionally strict:

| band | meaning |
|---:|---|
| 0–10 | absent; the question is not asked |
| 11–30 | named, but not working |
| 31–50 | partial; a fresh executor would have to guess |
| 51–70 | it works; a fresh executor can proceed |
| 71–90 | rare; measured, coherent, exceptions declared |
| 91–100 | reserved for a textbook-level design; **not given in this loop** |

**65 is the top of the "works" band.** It is not "a good film"; it is "ready to cut and shoot".
**100 is not the target; the effective ceiling is 90.**

## The criteria

Each seat has six criteria. Score each on the bands above:

| seat | criteria | must |
|---|---|---|
| `change` | C1 every row classified; C2 every multi-change row has a named cut point; C3 every `unit.before` / `.after` is writable as a difference; C4 every static row has one chosen change or is merged; C5 the multi-change set is complete; C6 the count is deferred, not the cut | C1–C5 |
| `continuity` | C1 the marks and fire tables hold; C2 the fold's plant and payoff are declared and the meaning is withheld; C3 the disclosure order is kept with no early reveal; C4 source contradictions are recorded with both coordinates; C5 the two fires are distinguished; C6 presence and population hold across episodes | C1–C5 |
| `fidelity` | C1 the seven world laws; C2 the visual prohibitions; C3 the organs, the fixed phrase, the four lines, the memory rules; C4 no invented state, prop or rule; C5 the work's withheld meaning is not explained; C6 the pilot's beat matches the draft and the shot table | C1–C5 |
| `feasibility` | C1 every reference key is real or declared missing; C2 the route's requirements are decided or declared; C3 `population` / `body_parts` are decided or declared; C4 place and time are single and memory is not a location; C5 the pilot's key_image policy and count are fixed; C6 the checker's current violations are understood and sequenced | C1–C5 |
| `cinematic` | C1 every shot has a specific image, not a label; C2 the block shape and the memory length are preserved; C3 the set piece has a visual form; C4 the light grammar is specific and coherent; C5 motion is decided or declared per shot; C6 sound is used as image | C1–C5 |

`primary_score` is the mean of the six. **If any must criterion is below 31, the seat is capped
at 40.** **65 passes when the mean is above 65 and no must is below 31.**

## What a seat returns

```json
{
  "seat": "change",
  "primary_score": 0,
  "critical": false,
  "findings": [
    {
      "where": "episodes/ep03.md:42",
      "what": "the row packs two changes",
      "why": "one shot, one change",
      "fix": "split at the voice"
    }
  ],
  "note": "2–4 sentences. What was read, and what would move the score."
}
```

⚠️ **`critical` is only for a finding that changes the cut, the references, or the source's
meaning.** Do not mark a missing detail as critical. Do not write the design; return the
coordinate and the reason.

## The loop

1. **Evaluate the pilot episode only.** The other episodes wait until they are cut.
2. **Run the five seats independently.** Do not show one seat another's output.
3. **Aggregate**: the mean of the five; list the criticals.
4. **Revise the design documents only.** Do not rewrite the source, the ledger, or the images
   unless the author rules.
5. **Re-evaluate with fresh seats.** Do not pass the previous outputs.
6. **Stop at mean > 65, or at 20 rounds.** Record the round, the mean, the five scores, the
   findings, and what was changed.
7. **Keep dissent.** A finding the author rejects is recorded with the reason; it is not deleted.

⚠️ **A round that scores below 65 is a result, not a failure.** Write down which seat held it down.

## What this skill does not do

- **It does not rewrite the design.** It returns coordinates and reasons; the author decides.
- **It does not mix with the story council.** The story's 13-dimension average is another
  ledger; this score is not added to it.
- **It does not score the prose.** It scores the design's cuttability, fidelity, feasibility,
  and cinematic promise.
- **It does not adopt.** Adoption is selection, and the author is the editor.
- **It does not add seats to average away disagreement.** Five seats; if they disagree, write
  the disagreement.

## Where to read more

- [`skills/breakdown/SKILL.md`](../breakdown/SKILL.md) — the stage this gate precedes.
- [`skills/review/SKILL.md`](../review/SKILL.md) — the council after ④, a different object.
- [`skills/design/SKILL.md`](../design/SKILL.md) — the specifications this gate does not read.
- [`CLAUDE.md`](../../CLAUDE.md) — the fixed policy the seats judge against.
