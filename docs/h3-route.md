<!-- i18n-version: 1.0.0 | canonical: docs/h3-route.md | translated: 2026-09-20 -->

**Language:** [English](h3-route.md) | [日本語](h3-route-ja.md) | [中文](h3-route-zh.md)

# The MINIMAX H3 route

Video has three routes. **`WAN 3.0` attaches a `key_image`** — it generates from text and pulls the look toward that image. **`MINIMAX H3` attaches a storyboard image and has no image path at all**: the generator receives the board itself as the design of the whole clip, and draws every panel of it. ⚠️ **This page is about that second route**; the third, `SEEDANCE 2.5`, has its own page ([`docs/seedance-route.md`](seedance-route.md)). The route is not chosen by a flag. It is read off the heading of §18, and the name in that heading is what picks it.

The routes **do not share a grammar of time.** On `WAN 3.0` the clip is one continuous take; on this route **each panel is its own scene, joined to the next by natural animation.** A rule copied from the other route does not read as a mistake — it reads as an instruction, and the generator obeys it.

What follows is the set of constraints that hold **on this route only**: what the strings handed to the generator may say, and what the paper drawn by the first stage may show. They are not guesses. Each one is written down because a shot made on this route came back wrong in a specific way, and the wrongness could be traced to a word or to a drawn line.

## The constraints

These are **not §16 MUST / MUST NOT.** §16 is the shot's own requirements, and it is written per shot. These are constraints of the route: they hold for every shot that travels it, and they bind both the strings in §18 and the text of the board.

### On the strings handed over

**1. A panel is a scene, not a frame of one take.** The board's panels are each their own scene, and they are joined to the next by natural animation. `Master`, `Camera` and `Motion` must not forbid that join — **forbid it and the generator answers by running two places together as one room.**

**2. `one continuous take` is the `WAN 3.0` house style.** Do not carry it into a specification on this route. It is the first line of `references/formats/video-spec.md`, which describes the other route.

**3. Do not write an unconditional `no cut`.** The only cut that may be forbidden is the cut to an unrelated location — `no cuts to unrelated locations` is the shape that holds. A blanket rule closes **the only lawful way for a panel to change place.**

**4. When a panel changes place, the specification says which it is** — a cut, or a move that stays continuous. The source never uses the word カット, so cut-versus-continuous is the shot's own decision; **a specification that stays silent lets the two places become one.**

**5. The protagonist's identity is not "the only person".** Write `keep the protagonist the same person in every panel`. `keep one and the same man` reads as *he is the only one there*, and the second person the scene needs is either erased or folded into the protagonist.

**6. Keep the source's qualifier.** The source says 「不必要な登場人物やシーンを追加しない」. Flattened to `no additional person`, it forbids the second person the scene needs — **the qualifier is the whole of the rule.** The working shape is `no additional person beyond the storyboard`.

**7. Carry §16's qualifiers into §18.** `no colleague invented at the counter` is right. Drop `invented` and an allowance becomes a prohibition that collides with the reference set, and the generator resolves the collision by removing the person.

**8. Write in the affirmative.** A blank is not left blank — it is filled, and **the default is not neutral.** It is a specific face, a specific room, a specific posture. A person in the frame is given an appearance even when they are given no name: ⚠️ **not writing a name is a decision; not writing an appearance is not.**

### On the paper

**9. One cut, one picture.** A cut's cell holds exactly one image, and a cut is never divided into smaller pictures inside its cell. **Divide it and the generator counts more panels than the board has** — the cut division and the time split both come apart.

**10. The panels' seconds add up to the shot's duration** (§1 `Duration:`). **Do not change the sum.** A panel drawn at a length the sum does not allow makes the clip run long.

**11. Do not split one body across two distances.** Head, torso and foot belong at the same distance and in the same frame, **reading as one person and not as two things at two distances.** Hold the lens at that one middle distance for the whole panel.

**12. Write what is *not* in the frame in the affirmative too.** A panel that must hold nobody says so: the frame holds the bundle and nothing else — no head, no shoulder, no arm and no hand in the foreground. **Emptiness left to omission is filled.**

**13. If the specification says the camera does not close on the paper, the board does not close on it either.** The panel's description and the board's picture have to be at the same distance, or the drawn one wins.

**14. No legible text inside a panel, and the lettering on the sheet is the work's language.** Name the lettering that is allowed — the title, the subtitle, the column headings, the cut numbers, the content column and the margin columns — **as an allow-list**, and forbid the rest: ⚠️ **including stamps and revision marks.**

**15. Do not let the board's Negative contradict its Format.** ⚠️ When the two disagree, **lettering is added outside the ruled fields to make them agree** — the generator repairs the contradiction by drawing.

**16. The board is paper, not an image route.** It is neither `key_image` nor a `specs/image/` specification, so **`L21`'s floor — no on-screen subtitles — does not apply to it.** A board is drawn with lettering; that is what makes it a board.

## What no check can see

- **Nothing reads the board.** No field points at it, so `check.py` never opens it. ⚠️ **This page does not close that hole** — `L28` reads §18, not the paper.
- **`L2` never fires on this route.** One shot here may lawfully hold more than one place, so the layer that reports a place crossing has nothing to report.
- **A flat negation cannot be caught as a string.** `no additional person` occurs in the corrected specifications and is *correct* there, because §18's `Master` says nobody but him is in the scene. **Judging it needs meaning, and meaning needs a ledger of the entities.**
- **No check can read the drawn picture.** A doubled face, a divided cut cell, a panel that ran long — all of those happen on the image side. **Constraints on the text do not make the picture right.**
- **Correcting the text does not change a board that has already been drawn.** A correction reaches the picture only by regenerating it.

## Where to read more

- [`references/formats/video-spec.md`](../references/formats/video-spec.md) — the §18 slots, and the time grammar the routes do not share
- [`docs/seedance-route.md`](seedance-route.md) — the third route
- [`skills/design/SKILL.md`](../skills/design/SKILL.md) — where the design stage chooses the route and writes the board prompt
- [`engine/ledger/README.md`](../engine/ledger/README.md) — `L28`, the layer that reads the strings on this route, and the holes it leaves
- [`engine/ledger/specmap.py`](../engine/ledger/specmap.py) — `MODELS["MINIMAX H3"]`, and `MODEL_ROUTE`, which holds the forbidden phrases with their reasons
