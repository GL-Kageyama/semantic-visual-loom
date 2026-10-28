# Material substitution（material-substitution）

- **Purpose**: Narration (one thing becomes another substance) ／ **Granularity×time**: one place × one material turn ／ **Size & aspect**: cinematic 16:9, single clip of `DURATION`
- **Summary**: **The shape holds; the substance changes.** Skin becomes paper, water becomes glass, cloth becomes smoke — and the object stays recognisable through the change, so the audience reads *what it is made of*, not *what it is*.

## Environment variables
`FORM`＝the shape that holds, `FROM`＝the material it starts as, `TO`＝the material it becomes, `TRIGGER`＝what the change answers, `DURATION`＝clip length

## Composition grammar

⚠️ **This card is `video-spec` plus one grammar.** Fill §1–20 exactly as that card requires; what follows is only what this grammar adds to it.

**The form does not change.** This is the card's whole discipline. **A silhouette that deforms is `transformation`; a silhouette that holds while its substance turns is this card.** Say in §3 which form holds, and hold it.

**One material property flips, and it is nameable.** Weight, opacity, fold, flow, heat, reflection. **"Everything goes soft and dreamy" is not a substitution** — it is a filter. Name the property in §4.

**The trigger is in the world.** A word, a touch, a temperature, a light. ⚠️ **A change with no cause reads as an error in the render**, and the audience's first thought is the machine's failure, not the character's condition.

**The new material must be photographed as material.** Paper creases, glass refracts, smoke occludes. **The camera's behaviour has to acknowledge the new substance** — otherwise the change happened in the metadata, not in the picture.

**Distinguish from `physics-with-a-rule`.** There, a law of the world is broken with a cost. Here nothing is broken: **the substance changes and the world keeps its physics.**

## do
- Name the form that holds, and keep its silhouette through the turn
- Flip one material property, nameable in a word
- Give the change a trigger in the world, visible in frame
- Let the camera respond to the new substance — weight, refraction, occlusion

## avoid
- A silhouette that deforms while the material changes
- "Everything softens" — a substitution with no nameable property
- A change with no cause in the world
- The camera behaving as though the material were still the old one

## Negative
`no deforming silhouette, no melting, no face morphing, no unmotivated material change, no blanket soft-focus, no dream filter, no on-screen text naming the material`

## Examples
- —

## Written into
- §5 OBJECTS
- §11 MOTION

⚠️ **The machine-readable half of this list is [`references/grammars/index.yaml`](../grammars/index.yaml)** — `L42` reads the index, not this prose. **Two places, one list**: the card is for a person, the index is for the checker.

## When it earns its place
- **The value it turns.** What a thing is made of — **and with it, what the thing can be trusted to be.**
- **What the audience loses without it.** The moment a familiar object becomes unfamiliar **without becoming a different object.** Transformation changes the identity; this changes the substance under it.
- **The grounding shot.** A shot of the same object in the same world, ordinary camera and ordinary material — **so the substitution is measured against the thing as it was.**
- **What it costs.** One property, one trigger, and the form. **A second property turns the shot into spectacle.**

## Failure it is confused with
- ⚠️ **A render failure** — the material dissolving because the model lost it. That has no trigger, no held form, and no camera response. **This card has all three.**
- **A dream filter.** If nothing is nameable, nothing was substituted.
- **`transformation`.** If the audience cannot recognise the object afterwards, the identity changed and this is the other card.

## Sources
The video side's own format card. **Its grammar is written into the `video-spec` skeleton — §5 OBJECTS and §11 MOTION's object motion**, which name what the object is and how it moves but have no field for *what it is made of*. `distill-essence-engine/references/formats/` has no equivalent: a still image can show a material, and cannot show it changing while the form holds.
