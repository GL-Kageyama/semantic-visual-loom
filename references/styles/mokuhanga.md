# Woodblock print（mokuhanga）

- **Medium**: Printmaking ／ **Lineage**: Ukiyo-e ／ **Era**: Edo
- **Summary**: Hand-carved ink lines and flat planes of mineral pigment transcribe the world into a block print.

## Environment variables
`SUBJECT`＝subject, `ACTION`＝action, `LOCATION`＝place, `ACCENT`＝emblematic prop, `ASPECT`＝aspect ratio

## Fidelity anchors
- Hand-carved ink lines (thick outlines, fine hairlike drawing)
- Flat color planes (solid fills) and the muddying of mineral pigments (indigo, crimson, ochre)
- Print misregistration, the wood-grain of the block, bleeding
- Bold ukiyo-e composition (diagonal perspective, cropping)

## Visual decomposition
- **Composition**: Bold foreground/background division, diagonal perspective, negative space
- **Typography**: No text (block-carved regular script if a title is required)
- **Color**: Broad black plus a few planes of indigo, crimson and ochre
- **Texture & light**: Washi grain, print pressure marks, flat light without shadows

## Motion character
- **The block is the mover, and it works by impression.** The frame re-prints rather than flows: an
  image lands, and then lands again.
- **Misregistration is the motion.** Between impressions the colour planes slip a little against the
  ink line, so an edge doubles and settles — the drift is the print's, not the subject's.
- **The camera is a sheet, not a window.** The frame holds still. A print is an object on paper, and
  a camera that travels turns it back into a scene.
- **Stillness is the ground; the planes stay flat.** A colour plane must not gain a gradient during
  the shot — flat fill is what this medium is.
- ⚠️ **What this style does not do**: smooth continuous animation, dissolving gradients, morphing
  contours, motion blur, or a camera that moves for its own sake. ⚠️ **The ink line stays carved for
  the whole shot** — a line that softens into a brush stroke is a different style.

## do
- Make the ink line the lead and fill color in planes
- Simplify the background so the subject floats free
- Keep the wood-grain of the block and print misregistration

## avoid
- Shaded gradients, photographic texture, 3D gloss
- Rainbow palettes, photorealistic faces
- Smooth gradients, morphing contours, motion blur, camera travel

## Negative
`not photorealistic, no digital gradient, no 3D render, no soft shading`

## Prompt template (English, fill-in-the-blank)
```text
A Japanese ukiyo-e woodblock print of {SUBJECT} {ACTION} in {LOCATION}, with {ACCENT}.
Flat mineral-pigment color planes in indigo, crimson and ochre over broad black,
hand-carved ink outlines with visible chisel marks, wood-grain texture and print misregistration,
bold Japanese composition with diagonal depth, no shading.
```

## Examples
- Run, Melos! → Melos running across the river (melos-imageboard / melos-manga / melos-cover)

## Sources
The image-side card (`distill-essence-engine/references/styles/mokuhanga.md`) — Run, Melos! verification (melos-imageboard / melos-manga / melos-cover).
**The style's identity is not authored here**; it is carried over so that this card stands on its own when it is the one that is read. **`## Motion character` is the addition** — the video side writes it, because the image side does not need it.
