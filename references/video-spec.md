<!-- i18n-version: 2.1.0 | canonical: references/video-spec.md | translated: 2026-09-18 -->

**Language:** [English](video-spec.md) | [日本語](video-spec-ja.md) | [中文](video-spec-zh.md)

# Video specification（video-spec）

- **Purpose**: Narration (re-experience / attraction) ／ **Granularity×time**: whole arc × one continuous take ／ **Size & aspect**: cinematic 16:9, single clip of `DURATION`
- **Summary**: The only format whose output **has time**. Folds an arc into one continuous generated take by spending duration unevenly, and carries the four axes a still image has no vocabulary for — time, motion, camera movement, sound.

## The one thing that makes this format different

Every other format in this engine folds time **away** — it lands on a still surface. This one folds time **in**. The compression target is not "the one point that speaks" but **the one continuous stretch that speaks**, and the selection question changes accordingly:

> Not *which instant*, but **which instants earn seconds, and which get one**.

A digest that gives every beat equal time is the video equivalent of cramming. **Uneven duration is the composition.**

## Environment variables
`SUBJECT`＝the arc, `DURATION`＝clip length (**the model decides the duration**), `ASPECT`＝aspect ratio, `BEATS`＝the beat list with second ranges, `CORE`＝the beat that gets the largest share, `HOOK`＝the note the clip ends on

## Composition grammar

**Beat table, not a shot list.** Lay the arc out as beats with explicit second ranges that are **deliberately unequal**. One beat — the core reveal — takes the largest single share (a useful anchor: ~30% of `DURATION`). Sparse beats hold on texture and duration; dense beats stack several events into a few seconds.

**Four axes a still image does not have:**

| Axis | What it fixes | Failure if omitted |
|---|---|---|
| **Time** | beat ranges, density (sparse / dense), transitions | uniform pacing — every beat reads equally important |
| **Motion** | subject motion, physics (weight, inertia, fluidity, impact) | floaty, weightless movement |
| **Camera** | movement over time (not just shot type), timing, target | a still frame that happens to last N seconds |
| **Sound** | dialogue, SFX, ambient, music, and their emotional function | picture carrying meaning alone |

**Identity lock.** When an arc spans more than one generation, the continuity block (subject appearance, environment, lighting, palette) is **pasted whole into every instance** — not summarized, not referenced. Independent generations share no memory. Even for a single clip, write it: it is what the negative prompt defends.

**End on the note, not after it.** The last second is where the viewer decides whether there is a next. Land the clip on the hook and cut — do not add a resolving beat after it.

## do
- Give beats **explicitly unequal** second ranges; state which is sparse and which is dense
- Spend the largest single share on the core reveal
- Write camera as **movement over time** (target, speed, timing), not as a shot type
- Fix physics — weight, inertia, fluidity — so motion has mass
- Write the identity lock in full, and repeat it verbatim per instance
- Separate the reusable specification (WHAT/HOW) from the resolved instance (WHEN, duration, output)
- Name the work's language in §14 and carry it into the `Audio Prompt` — **if there is speech it is in that language**, and a work with no speech declares it too, because a blank is not neutral
- Write the subtitle and BGM prohibitions into the Negative — **they are off unless you ask for them**
- End on the hook

## avoid
- Dividing `DURATION` into equal intervals
- A shot list with no camera movement (a slideshow of stills)
- Motion with no stated weight or inertia (floaty drift)
- Silence by omission — leaving dialogue, SFX, ambient and music unspecified
- Leaving the language unstated — **the generator speaks its own default** (measured: Chinese subtitles burned into a video that had speech)
- Assuming music and subtitles arrive only when asked for — **an omission is a request for whatever the model does by default** (measured: `no on-screen subtitles` was already in the Negative, and subtitles were burned in anyway)
- Summarizing the continuity block instead of pasting it
- Adding a beat after the hook
- Showing anything the source has not yet revealed at this point in the arc (see ⑧ Stay faithful — a later reveal leaking into an earlier clip is the characteristic failure of this format)

## The template is a specification, not a sentence

**Do not collapse this format into a prose paragraph.** Every other card in this engine ends in one fillable sentence, because a still image is one prompt. A video is a *document*: the deliverable is a filled specification whose sections are separately addressable, so that timing, motion, camera and sound can each be revised without rewriting the rest. A single paragraph destroys exactly the four axes this card exists to introduce.

The prose paragraph still exists — but only as **one of the seven slots in §18**, generated *from* the filled specification at generation time.

## Specification skeleton (§1–20)

Fill in this order. The right-hand column is where each engine principle lands.

| § | What it fixes | Engine |
|---|---|---|
| **1 VIDEO** | `DURATION`, `ASPECT`, resolution, frame rate, orientation ／ purpose, narrative function, mood, pace | — |
| **2 WORLD** | concept, era, location, time, weather, atmosphere ／ world rules ／ **Visual Language** | ⑥ Style lands in Visual Language |
| **3 SUBJECTS** | identity, appearance, behavior (personality / typical motion / emotional range) ／ **Continuity Requirements: Must Preserve · May Change** | ③ Translate ＋ ④ Keep consistent |
| **4 ENVIRONMENT** | location, elements ／ environmental behavior (wind, weather, particles, background motion) | ③ Translate |
| **5 OBJECTS** | appearance, material, function ／ the three importances (narrative / visual / continuity) | ③ Translate |
| **6 REFERENCES** | per reference: what it **Defines** / **Influences** / **Does Not Define** | ④ Keep consistent |
| **7 NARRATIVE** | core event, beginning, development, turning point, climax, ending | ① Understand |
| **8 TEMPORAL STRUCTURE** | **the beat table with unequal second ranges** ／ timing policy (`NON_UNIFORM`) ／ sparse vs dense regions | ② **Select — the heart of this format** |
| **9 ACTION** | per action: intention, intensity, speed ／ Before · After · Simultaneous With · **Causes** | ⑤ Compose (causality) |
| **10 CAMERA** | camera language ／ **camera events with timing, movement, target, speed** | ⑤ Compose over time |
| **11 MOTION** | subject / object / environmental motion ／ **physics: weight, inertia, acceleration, fluidity, impact** | ⑤ Compose over time |
| **12 EMOTION** | the emotional arc as a chain ／ emotional events with intensity | ③ Translate |
| **13 LIGHTING** | key, fill, rim, ambient, color temperature ／ lighting events | ③ Translate ＋ ⑥ Style |
| **14 AUDIO** | dialogue (speaker, content, delivery), SFX, ambient, music + its emotional function ／ **the work's language, named** | **this format's own axis** |
| **15 CONTINUITY** | identity, spatial, temporal, visual, motion — **the identity lock** | ④ Keep consistent |
| **16 CONSTRAINTS** | MUST / MUST NOT / PREFER / ALLOW | ⑦ Negative |
| **17 GENERATION PRIORITIES** | the conflict-resolution order — put fidelity to the source above visual appeal | ⑧ Stay faithful |
| **18 PROMPT MAPPING** | the seven prompts — six from §1–17, the seventh from the **style card** | — |
| **19 GENERATION INSTANCE** | resolved values for one generation (duration, references, events, output) | — |
| **20 ITERATION** | observed problems → changes → next generation | — |

Keep §1–18 reusable and put everything duration-dependent in §19, so the same specification survives a change of clip length or generation model.

⚠️ **§18 is the only section whose heading is a family**: `18. <MODEL> PROMPT MAPPING`. The name is
read against the registry (`specmap.MODELS`), and **that name is what picks the route.** Three video
routes are registered — **`WAN 3.0` attaches a `key_image`**; **`MINIMAX H3` attaches a
storyboard image and has no image path at all**, its paper made by `distill-essence-engine`
(format `storyboard`, style `luminous-anime`) and living at `specs/board/<id>-board.md`; and
**`SEEDANCE 2.5` attaches nothing by default** — it reads one long prompt, **and that prompt may
carry its own clock** (`0-3s:` `3-6s:`), while **its `Negative Prompt` slot is not received as a
floor** (`L30`). ⚠️ **The whole of that route's constraints is
[`docs/seedance-route.md`](../docs/seedance-route.md).**
⚠️ **One shot carries one `spec`**, so **a shot cannot hold more than one route** — shooting the
same shot on two of them and comparing them is not possible yet.

⚠️ **The routes do not share a grammar of time, and the line at the top of this document
describes only one of them.** `Granularity×time: whole arc × one continuous take` is the
**`WAN 3.0` house style**; on `MINIMAX H3` it does not hold. **There, each panel is its own scene,
joined to the next by natural animation** — ⚠️ **so §18 must not forbid that join.** **`no cut` as
a blanket rule closes the only lawful way for a panel to change place**, and the generator answers
by running two places together as one room. **Forbid the cut to an unrelated location; do not
forbid the transition** — and when a panel changes place, **the specification must say which it is**:
the source never uses the word カット, so cut-versus-continuous is the shot's own decision.
⚠️ **A reader who copies the top line into an `H3` specification has copied the other route's
rule**; the failure that produced this warning is recorded in `HISTORY.md`.
**This paragraph is read by `L28`** (the phrases and their reasons are in `specmap.MODEL_ROUTE`).
⚠️ **The full list of the constraints that hold on this route — the strings handed over and the
paper alike — is [`docs/h3-route.md`](../docs/h3-route.md).**

## §18 prompt slots

Seven prompts. The first six are drawn **mainly** from the sections named above.
**The seventh is drawn not from the specification but from the style card.**
**The separation itself is the point**, so do not mix them.

```text
Master Prompt   ← §1 + §7 + §8
  A {DURATION} continuous cinematic take ({ASPECT}) of {SUBJECT}, one clip.
  Beats, deliberately uneven: {BEATS}. The core beat — {CORE} — holds the largest
  share of the duration; the remaining beats pass quickly. Ends on {HOOK} and cuts.

Visual Prompt   ← §2 Visual Language + §3 Appearance + §4 + §5 + §13
  (the look, held still: art direction, palette, rendering, subject appearance,
  environment, key/fill/rim, color temperature — no motion words)

Motion Prompt   ← §9 + §11
  (what moves, in what order, with what weight, inertia and speed — subject motion,
  object motion, environmental motion, and the physics that governs all three)

Camera Prompt   ← §10
  (the camera events in order: timing, movement, target, speed, transition)

Audio Prompt    ← §14 + the work's language (`bible.language`)
  (dialogue with speaker and delivery, sound effects, ambient bed, music and its
  emotional function — and the work's language, named, so that the generator does
  not fill the blank with its own default)

Negative Prompt ← §16 MUST NOT + this card's Negative + the style card's Negative

Style Motion    ← the style card's Motion character (not §1–17 — the only slot taken from the style)
  (how this style moves at all — full animation or limited, whether a held frame
  is permitted, what the primary mover is. The specification writes what moves in
  THIS clip; the style card writes what movement MEANS in this style.)
```

The sources above are the main ones, not the only ones. The camera-stability
prohibition is the known case: it is written in §10, and it reaches the model
through the Negative slot.

⚠️ **Why `Style Motion` is the seventh.** The other six are decided **inside this
specification** — rewrite a section and they change. `Style Motion` is decided
**outside this specification** — swap the style and it changes, and **the same §11
means something different.** "What moves" and "what moving means in this style" are
different questions, and mixing them lets **the specification overwrite the style**
(or the reverse).
⚠️ **`Style Motion` can be written even when §11 MOTION is empty.** Even in a shot
where the subject holds still, **how that style treats a still subject** is decided —
**these are two different slots.**

## Negative
`no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no background music, no watermark, no morphing or drifting facial identity`

## Examples
- 午前二時に、あなたは誰の時間を生きていますか (At Two in the Morning, Whose Time Are You Living?) ep.1 → a 30-second digest (gozen-niji-video-01, soft-cel-anime)

## Sources
Wan 3.0 — Video Generation Specification (the target intermediate representation); `storyboard` (the nearest still-image ancestor — panels and shot types, but no movement, physics or sound)
