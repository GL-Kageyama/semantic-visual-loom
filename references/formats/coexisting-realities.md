# Coexisting realities（coexisting-realities）

- **Purpose**: Narration (realities side by side) ／ **Granularity×time**: one frame × unfolding ／ **Size & aspect**: cinematic 16:9, single clip of `DURATION`
- **Summary**: More than one reality is **laid out in one frame and none of them is earlier** — the past, a memory, an imagined room and the present stand together, each drawn as present.

## Environment variables
`REALITIES`＝the realities that stand together, `BEARER`＝who is in more than one of them, `SHARED`＝what belongs to all of them, `ORDER`＝how the frame lays them out, `DURATION`＝clip length

## Composition grammar

⚠️ **This card is `video-spec` plus one grammar.** Fill §1–20 exactly as that card requires; what follows is only what this grammar adds to it.

**This is unfolding, and it does not sequence.** The realities are laid side by side and stay unchanged — nothing passes through the frame and none of them arrives first. That is why this is not `time-fold`: there, one place is held while time passes through it; here nothing passes, and the frame holds several realities at once.

**⚠️ This card collides with §15 CONTINUITY, and the collision is the card.** §15 fixes identity, spatial and temporal continuity, and "the left half is this room ten years ago, the right half is now, and the same person stands in both" asks for the opposite. The specification must say what §15 is being asked to exempt — the frame's own place and moment — and must keep exempting only that. The `L2` and `L3` layers are the ones that fire: `L2` reads the ledger's `place`, `L3` the ledger's `time` and the beat text's time words.

**⚠️ The route decides whether this is reachable at all.** On the `WAN 3.0` route the collision is head-on — one continuous take cannot hold two places. **On the `MINIMAX H3` route it is not a collision**: the generation is one shot made of independent frames, and a single shot legitimately holds several places, so `L2` never fires there. **The §18 heading must therefore name `MINIMAX H3`**, because `_model_of` reads the first §18 and that name is what chooses the route. Written for `WAN 3.0`, this card's grammar is a contradiction; written for `H3`, it is the route's native case.

**⚠️ `L2` not firing is not the same as `L2` passing.** The layer reads one field of the ledger and opens neither §10 nor §18, so on this route it has nothing to see. **A layer that saw nothing looks exactly like a layer that passed** — the specification carries the burden, because no check will.

**Distinguish from the style `impossible-medium`.** There, two *media* disagree inside one picture. Here, the drawing is uniform and it is *realities* that coexist. That is a Style; this is a Format, and the two are not interchangeable.

## do
- Lay the realities out in one frame, with none of them earlier than another
- State what §15 is being asked to exempt — the frame's place and moment, and nothing more
- Name a bearer who stands in more than one reality, so the coexistence is visible rather than asserted
- Share something across them — light, sound, a material, a movement — so the frame reads as one frame
- Head §18 with `MINIMAX H3`, and say in the specification which route the shot is written for

## avoid
- Cutting between the realities, or dissolving one into the next
- Sequencing them, so one becomes the past of another
- A caption, a date stamp, or a title card naming which reality is which
- Exempting all of §15, so nothing in the frame is continuous
- Writing this for the `WAN 3.0` route, where a single take cannot hold two places
- Reading a silent `L2` as approval

## Negative
`no cut, no dissolve, no wipe between realities, no sequence, no caption naming realities, no date stamp, no split screen with a dividing line, no color grade separating the realities, no reality declared earlier than another`

## Examples
- —

## Sources
The video side's own format card, and **the one card whose reachability depends on the route** — `MINIMAX H3` carries it, `WAN 3.0` does not (`docs/h3-route.md`, and `L2`'s own docstring records that it cannot see this). **Its grammar is written into the `video-spec` skeleton — §15 CONTINUITY** — and it is the second grammar here that argues with a section it uses. `distill-essence-engine/references/formats/` has no equivalent: a still image holds several realities without any continuity to break, so the image side never needed a card for it.
