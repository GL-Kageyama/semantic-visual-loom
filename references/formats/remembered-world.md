# Remembered world（remembered-world）

- **Purpose**: Narration (memory, not record) ／ **Granularity×time**: one moment × a single point ／ **Size & aspect**: cinematic 16:9, single clip of `DURATION`
- **Summary**: The shot is **someone's memory, not a record** — the moment holds while its contents slip, and the slipping is the grammar rather than a defect.

## Environment variables
`WITNESS`＝whose memory the shot is, `DRIFT`＝what slips and returns, `CONSTANT`＝what never slips, `EXACT`＝what the shot keeps exact, `DURATION`＝clip length

## Composition grammar

⚠️ **This card is `video-spec` plus one grammar.** Fill §1–20 exactly as that card requires; what follows is only what this grammar adds to it.

**This is a single point: time does not pass, and the world slips instead.** Nothing in the frame travels through time — the moment is held, and what changes is the reliability of what is in it. That is why this is not `time-fold`: there, time passes; here time stands and the world is what moves.

**The drift is deliberate, and it is not randomness.** One named thing slips — a face, a background, a sign, a room's shape — and it slips in a way that *keeps its meaning*. A sign whose letters change is still a sign; a room whose walls move is still the same room. Drift that destroys meaning is a defect, not this grammar.

**Something is kept exact.** `EXACT` anchors the shot: the thing the memory is certain of. Without it the drift has nothing to be measured against and reads as a failed generation.

**Drift returns.** A thing that slips and stays slipped is a different grammar. The return is what makes the slipping read as memory rather than as damage.

**⚠️ This grammar collides with the continuity floor.** §15 CONTINUITY and the engine's consistency principle ask for a consecutive world; this asks for a world that is consecutive *in the way memory is*. The specification must say which elements are exempt — and must not exempt everything, because a frame where nothing is exact is not a memory, it is noise.

## do
- Declare the shot a memory in §2's world rules, not only in the picture
- Name what slips and what stays exact, and keep the exact thing exact
- Let the slipped thing return — drift is a departure, not a substitution
- Keep the drift meaning-preserving: the sign stays a sign, the room stays the room

## avoid
- Drift that destroys the subject's identity or the scene's meaning
- Exempting every element, so nothing measures the drift
- Slipping that never returns
- A caption or a voice-over explaining that this is a memory
- Reading the grammar as licence for generation errors

## Negative
`no drift that destroys identity, no illegible text, no garbled characters, no mojibake, no melting or warping faces, no slipped element that never returns, no caption explaining that this is a memory`

## Examples
- —

## Sources
The video side's own format card. **Its grammar is written into the `video-spec` skeleton — §11 MOTION and §15 CONTINUITY** — and it is the one grammar here that argues with a section it uses: §15 fixes the continuity this card deliberately relaxes, so the exemption has to be declared. `distill-essence-engine/references/formats/` has no equivalent, because a still image has no continuity to break.
