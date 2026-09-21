# Cinematic still（cinematic-still）

- **Medium**: Photography / film ／ **Lineage**: Feature film ／ **Era**: contemporary
- **Summary**: One frame of a film — anamorphic optics and graded light carry story in every shot.

## Environment variables
`SUBJECT`, `ACTION`, `LOCATION`, `LIGHT`＝light, `GRADE`＝color grade

## Fidelity anchors
- Anamorphic lens, subtle oval bokeh and flares
- Shallow depth of field, the background as atmosphere
- Motivated lighting that carries mood and story
- Moody color grading, a deliberate palette
- Cinematic composition, letterboxed 2.39:1 frame
- A film frame, not a photograph — actors, sets, and coverage

## Visual breakdown
- **Composition**: wide or medium shot with a clear subject, negative space for the mood
- **Typography**: letterbox bars, no diegetic text
- **Color**: graded palette (teal-and-orange, warm dusk, cold night)
- **Texture & light**: soft cinematic contrast, gentle flares, film or digital sensor grain

## Motion character
- **The frame is one frame of a take, and the take does not cut.** Time enters as continuation, not
  as a second setup — a cut would make it two stills.
- **What moves was already in the frame.** The camera's slow travel, a flare crossing the lens, a
  held gesture completing: nothing is introduced that the still did not imply.
- **Shallow depth is the mover's constraint.** What leaves the plane of focus loses itself, and
  coming back into it is the beat — the shot's changes happen at the focus plane.
- **The camera moves with a real rig's weight** — dolly, crane, Steadicam — or holds. But a hold
  here is a decision a camera makes, not a photograph's stillness.
- ⚠️ **What this style does not do**: cuts to a second setup, flat television lighting, snapshot
  framing, handheld wobble, unmotivated camera moves. ⚠️ **The grade holds for the whole shot** — a
  colour temperature that swings is a different style.

## do
- Light for mood and story, not for even exposure
- Keep the frame composed like a film shot, shallow and layered

## avoid
- Flat TV lighting, snapshot framing, amateur handheld wobble, pure cartoon color
- Cuts to a second setup, handheld wobble, unmotivated camera moves

## Negative
`no flat TV lighting, no snapshot look, no pure cartoon color, no CGI, no illustration`

## Prompt template (English, fill-in-the-blank)
```text
A cinematic still from a film: {SUBJECT} {ACTION} in {LOCATION}, lit by {LIGHT},
with a {GRADE} color grade. Anamorphic lens, shallow depth of field, light that
obeys the scene's own sources, subtle lens flare, the composition anchored
around {SUBJECT} in a letterboxed 2.39:1 frame.
```

## Sources
The image-side card (`distill-essence-engine/references/styles/cinematic-still.md`) — melos-cinematic-still (cinematic-still verification case).
**The style's identity is not authored here**; it is carried over so that this card stands on its own when it is the one that is read. **`## Motion character` is the addition** — the video side writes it, because the image side does not need it.
