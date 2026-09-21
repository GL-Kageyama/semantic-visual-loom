# Lab notebook（lab-notebook）

- **Medium**: Hand-drawn ／ **Lineage**: Laboratory notebook ／ **Era**: —
- **Summary**: A concept as a working page of a lab notebook — the record of finding it out, handwritten lines with margin notes and cross-outs, one observed result in color.

## Environment variables
`SUBJECT`, `ACTION`, `LOCATION`, `RECORD`＝the record of notes, `ACCENT`＝the observed result, `ASPECT`

## Fidelity anchors
- The working lab-notebook page: ruled or grid paper, handwritten line, margin annotations, a cross-out or correction, an arrow linking notes
- The line slightly loose and hand-drawn — warmer, less polished than a textbook figure
- Flat pale paper, minimal shading
- One accent on the observed result — the entry the whole page was leading to
- Short clean handwritten labels and one simple explanatory caption — the functional document's own grammar; they annotate, they never carry the concept
- Quiet, the page itself is the world

## Visual breakdown
- **Composition**: the page centered; notes lead down the page to the observed result
- **Typography**: short clean handwritten labels and one simple caption line in the same line language — default (functional-document labeling); labels support, never carry
- **Color**: pale paper + ink line + one accent on the observed result
- **Texture & lighting**: flat, papery, dry

## Motion character
- **The page is a record, so time enters as sequence, not as flow** — entry, cross-out, margin note,
  arrow, result. Each act is separate and the page accumulates.
- **The hand is what moves.** A line is written, a value is corrected, an arrow is drawn; the drawn
  subject stays drawn and does not act.
- **The camera holds on the page** and may drift down it as the record descends, but never leaves
  it.
- **Stillness is the ground between acts.** The page is legible for most of the shot; the shot is
  not continuous motion but a series of marks.
- ⚠️ **What this style does not do**: the drawn subject moving as a subject, smooth continuous
  animation, grunge animating for its own sake, 3D rotation, gradients, a camera that leaves the
  page. ⚠️ **One accent holds for the whole shot** — a second colour arriving is a different style.

## do
- Draw the concept as a record: entries, a cross-out, a margin note, an arrow — the sequence of finding it out is the causality
- Let the accent mark the observed result that closes the record
- Keep handwritten grammar (margin arrows, a circled result) as participating in meaning
- Keep cuteness subordinated — a small round subject in the same hand-drawn line, looser than the lab figure
- Label the entries briefly (one or two words each) and give the notebook page one simple explanatory caption — the functional document's own grammar; the labels annotate, the page carries — the label text and the caption line follow the resolved language (en/ja/zh), the viewer's language, not English

## avoid
- Heavy shading, photorealistic rendering, 3D gloss, digital gradient
- Grunginess for its own sake — restraint still holds
- The accent as a random highlighter — it marks the observed result
- Making it a clean textbook figure — this is the working page, not the printed one
- Long sentences, paragraphs, or decorative lettering — only short labels and one simple caption
- The subject moving as a subject, gradients, camera leaving the page

## Negative
`not photorealistic, no 3D render, no digital gradient, no oil texture, no heavy shading, no long text (only short labels and one simple caption), no mojibake, no garbled characters`

## Prompt template (English, fill-in-the-blank)
```text
A lab-notebook page of {SUBJECT} {ACTION} in {LOCATION}.; short clean labels and one simple explanatory caption in the same restrained line language — the labels annotate, they never carry the concept A working page — ruled or grid
paper, slightly loose handwritten line, margin annotations, a cross-out or correction, an
arrow linking notes — the concept drawn as a record of finding it out, {RECORD} the sequence
of notes leading to one observed result. Flat pale paper, minimal shading, dry and quiet.
One accent color {ACCENT} on the observed result that closes the record — meaning, not a
highlighter. Any character small and round with large flat unglossy eyes — drawn in the same
hand-drawn line, warmer than a printed figure. Quiet, the page itself the world.
```

## Sources
The image-side card (`distill-essence-engine/references/styles/lab-notebook.md`) — Functional-document family expansion (0.1.24) — sibling of clean-line-lab.
**The style's identity is not authored here**; it is carried over so that this card stands on its own when it is the one that is read. **`## Motion character` is the addition** — the video side writes it, because the image side does not need it.
