# Frame escape（frame-escape）

- **Purpose**: Narration (the subject crosses out of the picture) ／ **Granularity×time**: one place × one crossing ／ **Size & aspect**: cinematic 16:9, single clip of `DURATION`
- **Summary**: **The subject leaves the frame and comes back in from somewhere else** — not through a cut, and not by walking around the edge. The picture that contains them turns out to have a border that can be crossed.

## Environment variables
`SUBJECT`＝who or what crosses, `EXIT`＝which edge or surface it leaves by, `RETURN`＝where it re-enters, `PLACE`＝what is on both sides, `DURATION`＝clip length

## Composition grammar

⚠️ **This card is `video-spec` plus one grammar.** Fill §1–20 exactly as that card requires; what follows is only what this grammar adds to it.

**A crossing, not a cut.** The audience must see the subject meet the edge and pass it. ⚠️ **A cut where the subject leaves and reappears is the thing this card exists to refuse** — that is ordinary editing, and it says the frame is a window.

**Both sides are the same place.** What is beyond the edge is the world the shot is in, at a different part of it. **The place's geography must make the re-entry possible** — state it in §4, so the crossing is lawful.

**The frame's edge is visible as an edge.** The subject passes **behind the edge of the picture** — occlusion by the frame itself, or by a surface that coincides with it. **If the edge is not felt, the subject simply moved.**

**One crossing.** Out and back in once. **A shot where the subject leaves and returns twice is a game**, and the audience starts watching the border instead of the person.

**Aspect matters.** ⚠️ **A 16:9 frame's edges are where the grammar lives** — a vertical crop changes which edges exist. Say the aspect in §1 and keep it.

**Distinguish from `recursive-frame`.** There the frame contains a picture of itself. Here **the subject crosses the frame's boundary** — the border is a door, not a mirror.

## do
- State the place's geography so the re-entry is lawful
- Let the audience see the subject meet the edge and pass it
- Make the edge felt — occlusion, a surface, the frame's own border
- Cross once, and end on the subject in the new part of the same place

## avoid
- A cut where the subject leaves the frame and reappears
- A subject that walks around the frame's edge (that is just movement)
- A second crossing in the same shot
- A different place on the far side

## Negative
`no cut where the subject leaves, no walking around the frame edge, no second crossing, no different location beyond the edge, no masked wipe, no on-screen text naming the frame, no aspect change`

## Examples
- —

## Written into
- §10 CAMERA
- §15 CONTINUITY

⚠️ **The machine-readable half of this list is [`references/grammars/index.yaml`](../grammars/index.yaml)** — `L42` reads the index, not this prose. **Two places, one list**: the card is for a person, the index is for the checker.

## When it earns its place
- **The value it turns.** Inside becomes outside — **and the audience's frame is revealed as a border that can be crossed.**
- **What the audience loses without it.** The moment the picture admits it is a picture. **A cut hides the border; this card lets the subject use it.**
- **The grounding shot.** A shot of the same place with an ordinary camera, where the subject stays inside the frame — **so the crossing is measured against a frame that held.**
- **What it costs.** One crossing, one aspect, one place. **The geography must be built to allow it.**

## Failure it is confused with
- ⚠️ **An ordinary exit-and-re-enter cut.** That is editing, and it is the failure this card was written against.
- **A masked wipe.** The subject does not cross; the picture is replaced.
- **A subject leaving and the shot ending.** That is an exit, not an escape — **the return is what makes the border a door.**

## Sources
The video side's own format card. **Its grammar is written into the `video-spec` skeleton — §10 CAMERA's target and §15 CONTINUITY's spatial line**, which place the camera and the geography but have no field for *the frame's own edge as a place*. `distill-essence-engine/references/formats/` has no equivalent: a still image has no crossing, only a composition that stops at its border.
