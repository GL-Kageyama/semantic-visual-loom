---
name: direction
description: 'The work''s dramaturgy — the part of stage ① that decides what the work argues, how its values turn, where its acts and sequences break, and what each shot is for. It writes the ledger''s third register and each shot''s dramatic record; it does not write the specification. Use after breakdown and before design. ⚠️ Not a fifth stage.'
argument-hint: '(optional) the project name, or the sequence to direct. e.g. /semantic-visual-loom:direction drama-pilot'
---

<!-- i18n-version: 1.0.0 | canonical: skills/direction/SKILL.md | translated: 2026-10-29 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# direction — ① the work's dramaturgy

**① said what changes. ② decides the shot. This document is the part of ① that decides what the changes are *for*.**

⚠️ **It is not a fifth stage.** It runs **inside ①**, after `breakdown` has produced the shot list and before `design` writes a specification — the same way `staging` runs inside ②. What it writes is the ledger's third register and the shot records' `dramatic` fields. **It writes no §18 slot and no specification.**

## ⚠️ Why this exists: the ledger had two registers

The production ledger holds **continuity** (the state of the world) and **disclosure** (the state of the audience's knowledge). Both are about **what is true**. Neither is about **what the audience feels, expects, or carries out of the work.**

Drama was therefore emergent: it lived in whether the §18 prose happened to be good. `aim` recorded what a shot tried, but no check read it. `take.verdict.council` had a seat and no one sat in it. Nothing at the work level decided an act's turn, a sequence's contrast, or where a motif pays off.

⚠️ **The failure is not "the prompts were bad."** It is that **the work never decided what its changes were worth.** A shot can execute its `unit` perfectly and still be a shot nobody remembers.

## What this stage owns

| | What | Where |
|---|---|---|
| **the treatment** | premise · question · argument · visual thesis · value poles · ending image | `ledger.yaml` → `dramaturgy` |
| **the acts** | each act's `turn`, `climax`, `value_from` / `value_to`, `rhythm` | same |
| **the sequences** | `contrast` · `escalation` · `transition` · `payoff` · `flat` | same |
| **the motifs** | first appearance, recurrences, payoff | same |
| **the set pieces** | which shot uses which format card, and why | same |
| **the sound arc** | silence, where score enters, diegetic sound | same |
| **each shot's dramatic record** | `function` · `value` · `audience` · `button` | `shots/<id>.yaml` → `dramatic` |

**It does not own** the shot list (**`breakdown`**), the specification and `DIRECTION` section (**`design`**), or the take and its verdict (**`shot`**). ⚠️ **It also does not own adoption** — that is the author's act.

⚠️ **The shot remains the unit.** Acts and sequences are a **view laid over shots**, not a generation unit. One shot is still one change.

## The order of decisions

⚠️ **This order is a design claim; the checker does not enforce it.** Decide them top to bottom, and write each one down as you go. **Do not reverse-engineer the work from individual shots** — that is how a collection of good shots becomes a work with no argument.

1. **Premise — what happens, in one line.** If it needs two sentences, the work has two premises and one of them is decoration.
2. **Question — what the audience carries to the end.** Not "will they survive" but the specific uncertainty the work keeps open. **It must be answerable by the ending.**
3. **Argument — what the work says.** The claim the ending makes. ⚠️ **Do not confuse it with the theme word** ("love", "memory"). An argument is a sentence someone could disagree with.
4. **Visual thesis — what light, colour and composition say.** The same argument in the visual register. ⚠️ **It must be visible in at least two shots, or it is a mood.**
5. **Value poles — the pairs the work turns between.** Write them as `{ja, en}`: the Japanese the records use, the English the `DIRECTION` section will carry. **A value with no opposite is a setting, not a stake.**
6. **Acts — where the work turns.** Each act gets one `turn` (one change), a `climax`, a `value_from` → `value_to`, and a `rhythm`. **An act with no turn is a duration, not an act.**
7. **Sequences — how adjacent shots argue.** Each sequence gets a `contrast` (what the next shot is against), an `escalation` (what grows), a `transition` (how it hands over), and a `payoff` (what it collects, if anything). Then **the three constraints — the part of this register that reaches the frame**:
   - **`withheld`** — what the audience wants and does not get, on a named shot: `wanted` (what they are waiting for) and `given` (what the shot gives instead). ⚠️ **The two must differ and neither may be empty** — giving what you promised is deferring, giving nothing is an accident. ⚠️ **A shot nobody is waiting for cannot withhold anything**, so write this only where the audience wants something specific.
   - **`cuts`** — which shots break time inside themselves. ⚠️ **A cut is the sequence's decision, not the shot's**: it means something only next to the shot beside it. The shot record then carries `cut: internal`, **and the specification must stop saying one continuous take** — the generator never reads the record.
   - **`tempo`** — the sequence's shape in seconds, one number per shot, **matching each shot's `duration`**. ⚠️ **`duration` is the source of truth; `tempo` is the copy.** Three or more equal values are a level rhythm and need `flat: true` and a `note`.
   ⚠️ **A sequence that is flat on purpose says `flat: true` and says why** — that is a decision, not a gap.
8. **Shot functions — what each shot is for.** For every shot, write `function`, `value.from` / `value.to`, `stake`, `audience.feel` / `expect` / `know`, and `button`. ⚠️ **The value is the value of the shot's one change, not a second change.** ⚠️ **Non-narrative functions (質感・余白・様式美) need no value turn** — but they still need a `button`, because every shot ends on an image.
9. **Set pieces — which format card earns its place.** Name the card in the shot's §6 `REF_FORMAT`; record the choice in `set_pieces` with a `why`. **The card is the device; do not copy its name into the shot record as a second field.**
10. **Sound — silence first.** Decide where there is no music, where score enters, and where diegetic sound carries the scene. ⚠️ **The floor stays `no background music`**; a work that wants music writes `no background music` into `bible.base_negatives_waived`. **Do not create a second waiver seat.**
11. **Ending image — the last thing that remains.** ⚠️ **It must be an image, not a moral.** If the argument can only be stated in words, the visual thesis has not landed.

## What gets written, and where

```yaml
dramaturgy:
  version: 1
  premise: "…"
  question: "…"
  argument: "…"
  visual_thesis: "…"
  value_poles:
    - ja: 安全
      en: safety
    - ja: 危険
      en: danger
  acts:
    - id: act-1
      shots: [s01, s02, s03, s04]
      turn: "…"
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
      withheld:
        - shot: s01
          wanted: "her face when the world answers"
          given: "the valley's light, and her back"
      cuts: [s03]
      tempo: [8, 8, 8]
  set_pieces:
    - shot: s07
      format: impossible-camera
      why: "…"
  ending_image: "…"
```

```yaml
# shots/<id>.yaml
dramatic:
  function: 転換
  value:
    from: 安全
    to: 危険
    stake: "父の記憶"
  audience:
    feel: "息を止める"
    expect: "彼が扉を開ける"
    know: "母がまだ生きている"
  button: "閉じた扉の向こうの光"
```

⚠️ **`function` is a Japanese record value** (設定・上昇・転換・発見・決断・結果・溜め・解放・余韻, plus 質感・余白・様式美 for non-narrative shots). `design` writes it into the specification's `DIRECTION` section through `specmap.DRAMATIC_FUNCTION_EN` — **the record stays Japanese; the string handed to the generator is English.**

⚠️ **`audience.know` is not `disclosure_state`.** The latter is a fact about the world; the former is what the audience knows at this moment. **No layer compares them** — that is a judgment the design session makes by reading both.

## Devices: the card is the name

AI-specific staging lives in the **format cards**, not in a new field. A shot names its card in §6 `REF_FORMAT`; `dramaturgy.set_pieces` records why that card is used there. ⚠️ **Do not add `device:` to the shot record** — a second name for the same thing is a place for the two to disagree.

⚠️ **"Use them often" is a goal, and the budget is what makes it a discipline.** The budget is not a cap on ambition; it is the rule that **every device must carry a value turn**:

- **One principal device per shot.** A second is allowed only when it carries the **same** value turn from another face.
- **Two to three device shots in a five-shot sequence** is the default; **a set piece may carry four** — each must carry a turn and have a grounding shot immediately before or after.
- ⚠️ **A device shot needs a grounding shot**: the same world, an ordinary camera, before or after it. **No more than two consecutive device shots without grounding.**
- ⚠️ **A device that carries nothing is decoration — cut it.** The rule is not "use fewer"; it is **"leave no decoration."**

⚠️ **Face morphing is not the floor's business.** `BASE_NEGATIVES` carries only `no watermark`, `no on-screen subtitles`, `no background music`. Identity stability is the `video-spec` card's `## Negative` (`no morphing or drifting facial identity`). **AI transformation happens in the world, the material, the scale and the light — not in the face.** That is the house aesthetic, not a restriction.

## What the checker reads

- **`L40`** — a shot with `dramatic` and a narrative `function` whose `value.from == value.to`. Non-narrative functions are exempt; a shot with no `dramatic` is a note count.
- **`L41`** — an act with no `turn`, a sequence with no `contrast`, a `payoff` pointing at a shot that does not exist, or a `shots` entry that does not exist. No `acts`/`sequences` is a note.
- **`L44`** — the intensity curve: the same `intensity` across three or more shots, or no peak in an act. A sequence declaring `flat: true` is a note.
- **`L47`** — `performance.objective == performance.obstacle`. A missing `performance` is a note count, not a violation.
- **`L48`** — a `withheld` whose `wanted` equals its `given`, or either is empty. A withholding on the work's last shot is a note.
- **`L49`** — a cut declared by a sequence and not carried by the shot, or the reverse; **and a specification that still says one continuous take.**
- **`L50`** — a `tempo` that does not match the shots' `duration`, or three or more equal values with no `flat: true` and `note`.

⚠️ **No layer reads whether the turn is good, the contrast is sharp, or the device is memorable.** That belongs to the council and the author.

## What this stage does not decide

- **Whether the work is moving.** No check can tell you; the council advises and the author decides.
- **The specification.** `design` writes §1–20, including the `DIRECTION` section.
- **The take, the adoption, the edit.** ④ and the author.
- **The route and the model.** §18's heading names the route (`L18`).

## Language

- **The record side is Japanese.** `function`, `value.from` / `value.to`, `stake`, `audience`, `button` — these are read by the author and by `L40`/`L43`/`L47`.
- **The strings handed to the generator are English.** `DIRECTION` is written in English by `design`, from these records and §12. **Do not translate the record into the prompt; write the English type.**

## Where to read more

- [`skills/breakdown/SKILL.md`](../breakdown/SKILL.md) — ①'s first half, and the shot list this stage reads
- [`skills/design/SKILL.md`](../design/SKILL.md) — ②, and the step that writes `DIRECTION`
- [`skills/staging/SKILL.md`](../staging/SKILL.md) — the camera inside ②
- [`references/formats/video-spec.md`](../../references/formats/video-spec.md) — §12 EMOTION and the `DIRECTION` section
- [`schemas/ledger.schema.json`](../../schemas/ledger.schema.json) — the `dramaturgy` shape
- [`schemas/shot-record.schema.json`](../../schemas/shot-record.schema.json) — the `dramatic` shape
