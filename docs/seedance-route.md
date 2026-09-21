<!-- i18n-version: 1.0.0 | canonical: docs/seedance-route.md | translated: 2026-09-21 -->

**Language:** [English](seedance-route.md) | [日本語](seedance-route-ja.md) | [中文](seedance-route-zh.md)

# The SEEDANCE 2.5 route

Video has three routes. **`WAN 3.0` attaches a `key_image`** — it generates from text and pulls the look toward that image. **`MINIMAX H3` attaches a storyboard image** — the generator receives the board as the design of the whole clip and draws every panel of it. **`SEEDANCE 2.5` attaches nothing by default** — it reads one long prompt, and that prompt may carry its own clock. As with the others, the route is not chosen by a flag: it is read off the heading of §18, and the name in that heading picks it.

⚠️ **One shot has been taken on this route** (measured 2026-09-21, `habits-ch02-seg07`), **and its constraint list below is still empty** — because **no defect has been traced to a word.** The emptiness is the measured state — **not a claim that the route has no constraints.**

## What is measured

Confirmed against the vendor's own documentation.

- **Duration** — 4 to 30 seconds, or `-1` to let the model choose the length. **This is the widest ceiling of the three routes, and it is not a reason to lengthen a shot**: length is a dependent variable, and a shot is one change.
- **Resolution** — 480p and 720p at 8-bit, and 1080p at 10-bit.
- **Frame rate** — 24 fps.
- **Ratios** — `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `21:9`, and `adaptive`.
- **Reference assets** — up to 50 in one request: 30 images, 10 videos, 10 audio clips. Each carries a `role`: `reference_image`, `reference_video`, `reference_audio`, `first_frame`, `last_frame`.
- **Input types** — five: text only; reference images; a first frame, or a first and a last frame; video editing; video extension. **The constraints on ratio and duration differ by type** — a first-frame request requires `adaptive`.
- **Time inside the prompt** — intervals may be written in seconds, as `0-3s:` and `3-6s:`. The vendor's own samples do this.
- **Audio notation** — `()` music, `<>` sound effects, `{}` dialogue, `【】` subtitles.
- **In-world text** — the vendor's sample prompts have the model draw a brand name and a slogan into the picture. ⚠️ **That section is written under the earlier generation's name, so it is not evidence of a strength specific to 2.5.**

⚠️ **What could not be confirmed: that this route is strong at text.** The vendor's own wording says something else — that it *minimizes uncontrolled occurrences in subtitles and background music*. The text-generation section is filed under the earlier generation, the 2.5 changelist has no lettering item, and no accuracy figure or benchmark exists in the primary sources. **A route is not adopted here on the strength of a claim its own documentation does not make.**

## The gate: a slot this route does not receive

**This route has no parameter for negation.** Negation is honoured only for subtitles and audio — written in the prompt as `No subtitles.`, `No BGM`, `No audio.` **Everything else in §18's `Negative Prompt` is read as prose.**

⚠️ **A negation that did not work cannot be told apart from a negation that was never handed over. It is discovered after the picture comes back.**

So the slot is declared in `specmap.MODEL_UNRECEIVED_SLOTS`, and **`L30` fires when a specification on this route fills it.** **A gate is a fact about the route, not a mistake in the work** — the fire is the point: it says where the floor and the route disagree.

**A work that means to use the route anyway writes it down**, in `bible.route_limits_accepted` — a list of `"<MODEL>: <slot>"`. That turns the violation into a note the author has named. **The exclusion is the work's to write; an engine that remembers which works are special has stopped being an engine.**

⚠️ **Declaring it does not make the negation work.** It records that the author knows it does not.

### The declaration is matched exactly, and audited both ways

**The string is compared character for character.** A declaration spelled differently is **ignored in silence**, and the author gets back the same violation they would have got had they written nothing — **the mechanism looks broken.** ⚠️ **This is the inverse of `L21`'s rule that an unreported exclusion looks like a check that passed: a declaration that does not take effect is the same as no declaration.** So the layer reports both directions:

| what the work wrote | what the layer says |
|---|---|
| a string that **matches no gate** | **violation** — "it has not hit a single gate." ⚠️ **A near-miss spelling is named** (case, spacing, full-width colon are folded **only to name it**); when there is none, **the gates the route actually holds are listed** |
| a string that **correctly names a gate**, in a work whose §18 **has never reached it** | **note** — "this declaration is doing nothing right now." **Not a violation** — the work may reach that route later. ⚠️ **But not silence either**, for the same reason |

⚠️ **The spelling is not folded through.** Folding names a near miss; **it never lets one pass** — letting it pass would also let through a declaration that genuinely names a different gate. **This is the rule `L21` already applies**: only the floor's clauses may be excluded.

### What a specification on this route can do instead

Put the prohibitions where the route reads them. The route reads prose, so a shot that must not hold something says so **in the affirmative**, in the slots that are read — `Master`, `Visual`, `Camera`, `Motion`, `Audio`.

⚠️ **And keep the `Negative Prompt` slot filled anyway.** Emptying it is not the same as solving it: **`L21` requires the slot to cover the foundation's floor and the work's own base negatives**, so an emptied slot fails a different check. The two are not alternatives — **one is the record of what the work forbids, the other is what the route can hear.**

⚠️ **Two of the five floor clauses do land here.** `no on-screen subtitles` and `no background music` are exactly the negations this route honours — and **they are a floor here for a stronger reason than on the other two routes**: this route has an official notation for producing subtitles, so the risk it guards against is one the route can manufacture on request.

## Subtitles are not in-world text

**A subtitle is burned on top of the picture by the machinery. In-world text is inside the picture, drawn by whatever draws the picture.** The floor forbids the first and says nothing about the second, and **the two must not be collapsed: a reader who collapses them lifts the floor and lets subtitles in.**

The work's `text_channel` records which of the two a shot needs. `kind` names **who draws it**:

| kind | who draws it | where it goes |
|---|---|---|
| `overlay` | the composition | `edit:timeline` — burned in at assembly |
| `voice` | nobody — it is heard, not drawn | `prompt:Audio Prompt` |
| `lettering` | the generator, inside the picture | `prompt:Master Prompt` |

⚠️ **`lettering` does not claim anything about legibility.** It says one thing: this text is drawn by the generator, not burned in at assembly. **Whether it can be read is the specification's decision, made per shot** — a work may need one shot that is readable and another that is not, and a kind that fixed legibility would be too narrow for both.

⚠️ **A `composite` shot must still carry at least one `overlay`.** A shot whose only text is `lettering` burns nothing, so counting it as composite would let it through a check it does not satisfy.

## What collides with the fixed policy

**The vendor documents a notation for several cuts inside one generation** — `Shot 1`, `Shot 2`. **This is the opposite of the fixed policy that a shot is one change and is not divided into segments.** Nothing in the foundation reads for it, so a specification on this route is written knowing the collision exists. **A route that can do a thing is not required to do it.**

## Real faces

The vendor states that this route **does not accept reference images or reference videos containing real human faces**. **A work whose people are real cannot take this route.**

## The constraints of this route

⚠️ **Empty — and for the opposite reason the other routes' entries are not.** A restriction goes into `MODEL_ROUTE` **only after a shot on that route has come back wrong in a specific way that traces to a word.** Writing one now would be a guess, and **a guessed restriction fires on correct specifications.** When a shot on this route comes back wrong, the phrase and its reason go here.

## What no check can see

- **Whether a negation read as prose had any effect.** `L30` reads that the slot is filled; it cannot see the picture. **The layer's own note says as much.**
- **Whether the generator drew the text, drew nothing, or drew nonsense.** A model asked for unreadable characters may return a blank surface or invented glyphs. ⚠️ **This route is being used for shots where both are failures** — and the clause that forbids them sits in the slot the route does not receive.
- **Whether the clip is 4 to 30 seconds of one thing, or several cuts inside one generation.** The notation exists; no field says which was asked for. ⚠️ **Writing `Shot 1` into a prompt is what makes it true** — nothing here prevents it.
- **Whether the reference roles were used as intended.** `first_frame` and `last_frame` are declared to the vendor, not to this repository.
- **Whether the note was read.** `L30` reports the declaration, and audits it in both directions — **but reading it is a person's job, and nothing checks that it happened.**
- ⚠️ **Whether the work took the limit on, or merely obeyed `L21`.** `L21` requires five clauses in this slot, and **`L30` fires on any content at all** — so a work that wrote only the five it owes fires exactly like a work that knowingly kept eighty-five. **Measured**: narrowing the specification to those five leaves the violation standing; emptying the slot moves it to `L21`. ⚠️ **On a gated route the declaration is therefore a toll rather than a judgement — and the layer cannot say which kind of work paid it.**

## Where to read more

- [`references/formats/video-spec.md`](../references/formats/video-spec.md) — the §18 slots, and the time grammar the routes do not share
- [`docs/h3-route.md`](h3-route.md) — the second route, and the worked example of a constraint list with measurements behind it
- [`engine/ledger/README.md`](../engine/ledger/README.md) — `L30`, and the holes it leaves
- [`engine/ledger/specmap.py`](../engine/ledger/specmap.py) — `MODELS["SEEDANCE 2.5"]`, `MODEL_UNRECEIVED_SLOTS`, and `ROUTE_LIMITS_KEY`
