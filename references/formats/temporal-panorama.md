# Temporal panorama（temporal-panorama）

- **Purpose**: Narration (one person's time laid across one frame) ／ **Granularity×time**: one place × layered time ／ **Size & aspect**: cinematic 16:9, single clip of `DURATION`
- **Summary**: **Several moments of one person occupy one image at once** — afterimages, multiple exposure, a figure repeated along a road — and the shot reads the life as a shape rather than as a schedule.

## Environment variables
`PLACE`＝where the times are laid, `FIGURE`＝the one whose times these are, `LAYERS`＝how many moments, `ORDER`＝what the audience reads first, `DURATION`＝clip length

## Composition grammar

⚠️ **This card is `video-spec` plus one grammar.** Fill §1–20 exactly as that card requires; what follows is only what this grammar adds to it.

**One person, many moments, one frame.** The layers are **the same figure at different times**, and the shot never cuts between them. ⚠️ **Several different people in one frame is not this grammar** — it is a crowd.

**The layers have an order the eye can read.** Left to right, near to far, high to low, faint to solid. **Say in §10 which order the frame asks the audience to read** — and let the last layer be the one the shot ends on, not the one it begins with.

**The figure does not acknowledge the other layers.** Each moment is complete in itself. ⚠️ **A figure turning to look at its own afterimage is a different film** — the moment of self-recognition is not this grammar's business.

**The youngest and oldest must be distinguishable at a glance.** One gesture, one posture, one wardrobe difference. **If the audience cannot order the layers, the shot is a smear.**

**Distinguish from `time-fold`.** There the place holds and the thing it is made of changes. Here **the place holds and one person's moments accumulate** — the subject is the figure, not the span.

## do
- Keep it one figure, repeated — same person, different moments
- Give the layers a readable order, and state it in §10
- Keep the figure from acknowledging its own other moments
- Make the moment the shot ends on the oldest or the newest — not the middle

## avoid
- Several different characters in one frame
- A figure looking at, or reacting to, another layer of itself
- Layers that cannot be ordered by the eye
- A time-lapse or a speed ramp standing in for layering

## Negative
`no multiple different characters, no figure acknowledging its own afterimage, no time-lapse, no speed ramp, no cut between moments, no on-screen text naming the times, no double exposure as an accident`

## Examples
- —

## Written into
- §8 TEMPORAL STRUCTURE
- §11 MOTION

⚠️ **The machine-readable half of this list is [`references/grammars/index.yaml`](../grammars/index.yaml)** — `L42` reads the index, not this prose. **Two places, one list**: the card is for a person, the index is for the checker.

## When it earns its place
- **The value it turns.** A life becomes a shape — **the audience sees a span as an object rather than as a sequence.**
- **What the audience loses without it.** The single image that holds a whole passage. **A montage gives the moments; this gives their sum.**
- **The grounding shot.** A shot of the same place with one figure and one moment, ordinary camera — **so the layers are measured against a single body in a single time.**
- **What it costs.** One figure, and no cut. **The layers are the budget.**

## Failure it is confused with
- ⚠️ **A double exposure made by accident** — layers with no order and no single figure. This card's layers are placed, and the figure is the same person.
- **A time-lapse.** That compresses time into a rate; this layers time into a picture.
- **`time-fold`.** That is about the place; this is about the person.

## Sources
The video side's own format card. **Its grammar is written into the `video-spec` skeleton — §8 TEMPORAL STRUCTURE and §11 MOTION's subject motion**, which ask how time is divided but have no field for *one person's times held at once*. `distill-essence-engine/references/formats/` has no equivalent: a still image can hold the layers, and cannot show the eye moving through them.
