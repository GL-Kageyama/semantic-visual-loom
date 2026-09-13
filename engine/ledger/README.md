<!-- i18n-version: 1.0.0 | canonical: engine/ledger/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# engine/ledger/ — Production Ledger and Pre-Flight Verification

**Crush the design's failures without running a generation even once.** That is this layer's job.

```bash
python3 engine/ledger/check.py projects/<project>   # run the pre-flight verification
python3 engine/ledger/check.py --self-test          # confirm the checks actually fire
```

## The Two Layers

| Layer | What it sees | Who |
|---|---|---|
| **Form** | required, type, enum, format | `schemas/*.json` (jsonschema, Draft 2020-12) |
| **Meaning** | one change, one environment, intent vs. actual, disclosure | `semantic.py` |

**⚠️ Why layer 2 is needed.** `unit` was made a `{ before, after }` pair
in order to fire on "`before` and `after` are the same" — but **JSON Schema cannot fire on that.**
`if`/`then` + `const` is an **enumeration**, not a comparison, and `$data` references never made it into the standard.
**It has been measured and confirmed** (`HISTORY.md`).
**Making them a pair and being able to check the pair are two different things.**

## What Fires

| Code | What it fires on | Source |
|---|---|---|
| **L0** | **The input is empty** (0 shots, empty ledger, empty disclosure) | "Do Not Call Empty OK" below |
| **L1** | `unit.before` and `unit.after` are the same = that shot causes nothing | §2.1 |
| **L2** | Multiple places line up in `place` = multiple environments in one continuous take | measurement S04, S27 |
| **L3** | Multiple times line up in `time` / three or more kinds of time words in the beat body | measurement S27 |
| **L4** | A movement verb in the beat body (`then` / `→` / `moves to` / `帰り道` (the way home)). **A violation only when paired with L2** | measurement S04 |
| **L5** | The same thing is both referenced and forbidden | a design mistake |
| **L6** | `reference_set` (intent) contradicts `attached` (actual) | measurement of Ukebi V1 |
| **L7a** | **Too early a disclosure** — a shot before the declared change point already holds that value | flower contamination |
| **L7b** | **The ledger did not predict it** — at the change-point shot, the state has not actually changed | Checker No. 2, question 1 |
| **L8** | The reference set pulls a key that is not in the ledger | §2.3 |
| **L9** | **The disclosure check is empty** — every transition the record holds matches a declared position in the ledger | "Firing When a Check Is Empty" below |
| **L10** | **Does a disclosure change point appear in the text that reaches the model (§18)?** | "The Other Party Is §18, Not §16" below |
| **L11** | The specification's sections are not as the registry (§1–20) says. ⚠️ **It also fires when the registry itself is short** | "The Mapping Is a Registry, Not Prose" below |
| **L12** | **The field-to-section mapping is not closed in both directions** | same as above |
| **L13** | **The shot's identity differs from the specification's self-name (§19 `Instance ID`)** | "Identity Is Taken From the Specification Side" below |
| **L14** | **A span beyond the declaration** — §18 holds a **change that does not return** (an addition / a deletion) that the ledger does not declare | "Motion Is Not Evidence of Disclosure" below |
| **L15** | **The role cannot be resolved to the registry**. ⚠️ **A role that is not used does not fire** (it is reported as a note) | "A Registry Exists Only Once It Is Read" below |
| **L16** | **There is no motion axis** — **`motion` is required regardless of `mode`** | same as above |
| **L17** | **§18's slots are not as the registry says** (7 of them, including `Style Motion`) | same as above |
| **L18** | **The shape of the two paths does not fit that field** — or the model §18 names cannot be resolved to the registry | "The Path Is Decided by the Field, Not by `mode`" below |
| **L19** | **A record field has no declared destination** — the dual of `L12` | "That the Aim Arrives" below |
| **L20** | **`Style Motion`'s destination is empty** — the style card has no `Motion character` | "That the Aim Arrives" below |
| **L21** | **The image Negative does not cover the work's prohibitions (`bible.negative_base`)** | "Does the Image Negative Cover the Work's Prohibitions" below |
| **L22** | **The image specification's 7 fields are empty** — or **the card it names does not declare that field** | "Are the Image Specification's 7 Fields Non-Empty" below |
| **L23** | **`shot.duration` contradicts `Duration:` in video specification §1** | "Do the Intent and the Specification Agree on Duration" below |
| **L24** | **What `mode` requires is missing** — §11 for `still` / `composite`, `text_channel` for `composite` | "What `mode` Requires" below |
| **L25** | **The take does not match the shot, the style or the real thing** — 11 types | "Does the Take Match the Real Thing" below |

**L2, L3 and L4 are transplants.** Applied to all 57 segments of Gozen-niji,
a checker that scored **recall 2/2 and 0 false positives** went in just as it was.
**L1, L5, L6, L7, L8, L9 and L10 are new — having a schema is what finally made them writable.**

⚠️ **The transplant is not unconditional.** Applied to the 30 takes of Ukebi V2, `L4` **fired 5 times and all 5 were false positives**
(`→` is a sequence of organs, `Then` is a time connective, `moves to` means "is about to", `walks to` is walking within the frame).
**Write a detector for one work and it false-positives on the other work.**
That is why `L4` **does not fire on its own** — only when the place actually spans a boundary (`L2`) does the movement word become its support.

## ⚠️ Do Not Call Empty OK

**If the other side is empty, not a single check fires.** Not firing is not proof of correctness
— there is already an actual case where `0 == 0` passed. That is why **L0 fires first.**
And L7 **counts and reports the shots that hold no disclosure state** —
without counting, you cannot tell whether "0 violations" means "0 after checking" or "not checked".

`--self-test` holds **one example that fires and one that does not, for each check** (169 examples).
⚠️ **Read the notes too.** Because **a note that does not appear also looks like "0 violations"**
— with no example that confirms the note, deleting the note leaves the self-test green.
⚠️ **Read the note's "count" too.** `L25`'s note says "read N takes (broken down by role)" —
**a note whose breakdown does not sum to N contradicts its own body.**
Count the takes per role by `(shot, kind)`, and **when one shot holds two, you count one**.
The self-test holds an example that reads that (without it, a miscounted note **is indistinguishable from 0 violations**).
⚠️ **It also holds a pair that changes exactly one path.** `L13` and `L17`, given **the same body**,
do not fire when placed in `key_image:` and do fire when placed in `spec:`. **Place only one of them,
and deleting the narrowing leaves the self-test green** — with no firing side, you cannot notice that you killed the check.
⚠️ **In particular** — **`L21` holds an example that does not fire with `no photorealistic` (ledger) and `not photorealistic` (spec)**
(that very false positive found in measurement), **`L23` holds one that does not fire on a specification whose durations agree**,
and **`L24` holds one that does not fire on `motion`.**
**`L22` holds four examples** — all 7 fields filled and the naming matching (does not fire), a field empty (fires),
**a named card that does not declare that field** (fires), **a named card that cannot be read** (does not fire; a note).
And **it reads the real thing** — `L18` reads Ukebi V2's 30 takes, `L19` reads the real schema,
`L20` the real 55 style cards. **A check that passes only on synthetic data will fire in the field.**
⚠️ **`L25` was fixed once by "an example that should not have fired, firing."** The duration tolerance is one frame, but
`6.0 + 1/24` is not exactly one frame in floating point (`1.0000000000000007`) —
**compared as is, the boundary itself becomes an error in the check.** The self-test reported 166/167, so
it was changed to **convert the difference into frames first, then round**. **Watching only the green, this error would have stayed.**

⚠️ **The form layer (S0, S1) is in the self-test too.** The meaning layer alone is not enough —
**if the schema is short, an empty required field passes straight through.** That the same record fires on the real schema
and does not fire on a schema with `required` emptied is something **the self-test builds and confirms on the spot**
(the same shape as L11 watching that "it fires even when the registry is short").

⚠️ **It also holds an example that breaks the registry.** The case where `SPEC_SECTIONS` is shrunk to 3 sections and
the case where one field is removed from `SPEC_MAP` are built and fired by the self-test on the spot
— **the checker itself confirms that "a shorter registry makes the check empty."**

⚠️ **Only L9 holds an example that is "expected to fire."** The other checks watch that "a correct example does not fire",
but L9 **is the check that fires when a check is empty**, so **it must fire on a copied record.**

⚠️ **L14 holds a "does not fire on rotation" example.** This is **the most important example of all**
— the naive version (firing on "§18 moved and there is no declaration") **fires on this example.**

## ⚠️ "There Is No Record" and "It Contradicts" Are Different

**A blank is a claim, not a fact.**

- **L6** A shot with no `attached` field at all is **not a contradiction — there is no record.**
  Writing `attached: []` fires on "the intent has one but none was attached", and that is **a falsehood**.
- **L7** If **no shot record writes** an attribute the ledger declared, that change point is
  **unchecked** — there is nothing to match it against. **That is not 0 violations.**

**Without the distinction, the checker reports "what you did not write" as "what is wrong."**

## ⚠️ Firing When a Check Is Empty (L9)

**0 violations and an empty check are indistinguishable.**

The ledger's `disclosure` is the "intent"; the shot record's `disclosure_state` is the "actual".
**Copy the actual from the intent and L7 is merely reading the same thing twice.**

So `L9` **counts transitions**. If every transition the record holds **matches a declared position in the ledger**,
that record has said nothing new against the ledger — **you cannot tell whether it was copied or read independently.**
Hold a transition that is not in the ledger and the record is saying something new, so it does not fire.

- **A first appearance is not a transition.** The first value to appear is a starting point, not a change point the ledger declares.
- **An attribute you did not write does not enter the comparison.** Transitions are counted, so something that holds no transition at all
  (the same discipline as `L6` and `L7` — **what you did not write is not a contradiction**).

> ⚠️ **This note does not disappear when you read the same source text again. Agreement is not evidence of independence.**
> If reading §16 with another tool yields the same transitions, **that is merely reading the same source text twice.**

**This check is the check that doubts the correctness of the other checks.**

## ⚠️ The Other Party Is §18, Not §16

**A disclosure change point appears in the text that reaches the model.**

The specification document holds §1–20. **Of those, only §18 `Negative Prompt` reaches the model**
— §16 `MUST NOT` is **a note for people to read**, rewritten per work, holding not one block.
**Apply a tool that makes blocks (a ledger) to a document that holds no blocks and it will always approach "one block per take."**

So each change point in `disclosure` declares a `negative:`.

| Value | Meaning |
|---|---|
| `changed` | §18's section changed at this change point |
| `covered` | §18 does not change. **It already held that state** |

**L10 actually reads §18 and checks it in both directions.** Say "it changed" and it has not, and
the ledger is wrong; say "it does not change" and it has changed, and **the reason is wrong.**

> ⚠️ **That §18 does not change is not that it is not responding.**
> §18 is a **safety envelope** — it may hold that prohibition before the ledger declares it.
> In Ukebi V2, the prohibition on the girl's name exists **continuously from the first change point**,
> and at the two points of the line and the name, §18 does not move one section. **Moving and carrying are different.**
> It is the same discipline as `L6`, `L7` and `L9` — **what you did not write is not a contradiction.**

⚠️ **But §18 is not monotone.** Making §18 the other party was right, but
**"§18 moved = the disclosure moved" does not hold** — §18 is a per-shot projection.
What L14 looks at is **not motion but the increment that does not return** (below).

⚠️ **It fires when `negative:` is missing.** If a change point does not write `negative:`,
that change point has **never been confirmed against the text that reaches the model** —
not "0 violations" but "not checked".

⚠️ **`negative:` is a reserved key.** A change point is a "bag of attributes", so unless it is reserved
you would read it as if a disclosure attribute called `negative` existed (`DISCLOSURE_RESERVED`).

⚠️ **Reading §18 requires the shot record's `spec:`.** Without it, or when what it points to cannot be
read, L10 **fires rather than silently skipping**. **What cannot be read is not checked.**

## ⚠️ That the Declaration Is Correct and That It Is Read as Declared Are Different

**`specmap.py` may declare "this field comes from this section", and nobody is guaranteed to read that field.**
Measurement: **of the 18 fields, the checker never reads 2 of them** — `effect` and `sound` (the counting method and the measured values are in `HISTORY.md`).
⚠️ **`duration` and `text_channel` are now read** (`L23`, `L24`).
⚠️ **The remaining 2 fields also have their readers in another layer** — ⑦ acceptance (`effect`) / Semantic Audio Loom
(`sound`, contract M6). **They are not fields this layer should read**, so nothing fires here.

⚠️ **L12 does not fire on this.** What L12 looks at is **whether the mapping is closed in both directions**,
not **whether that field is read.**

## ⚠️ A Registry Exists Only Once It Is Read

**Registering alone leaves that field a field nobody reads.**
So **layer F** looks at **the registry itself** — **whether the registration is read.**
**Discipline: when you add a registry entry, add the check that reads it at the same time.**

| Registry | Where | What | The check that reads it |
|---|---|---|---|
| **role** | `rolemap.ROLES` | 12 kinds (dialogue, action, reaction, reveal, establishing, texture, tableau, motion, transition, montage, pause, explanation) + 3 kinds that came out of measurement (catalogue, narration, departure) | **L15** |
| **the motion axis** | `rolemap.MOTION_PATTERNS` | 13 patterns (body 6, object and environment 3, frame 3, style 1) | **L15** (qualified spelling), **L16** |
| **§18's slots** | `specmap.PROMPT_SLOTS` | 7 (Master / Visual / Motion / Camera / Audio / Negative / **Style Motion**) | **L17** |
| **models** | `specmap.MODELS` | name, kind (`video` / `image`), source. **Prices are not written** | **L18** |
| **specification kinds** | `specmap.SPEC_KINDS` | `video` (field `spec`, holds §1–20) / `image` (field `key_image`, holds neither) | **L18** (`L11`, `L21` and `L22` follow it) |
| **field destinations** | `specmap.FIELD_DESTINATION` | 18 fields. **There is no `mode` dimension.** The vocabulary is `自前` (own) / `prompt:<slot>` / `params:<key>` / `handover:<base>` / `edit:timeline` | **L19** |
| **what `mode` requires** | `specmap.MODE_DEMANDS` | `still` (§11), `composite` (§11 + `text_channel`), **`motion` (empty row)** | **L24** |
| **handover bases** | `specmap.HANDOVER` | `distill` (image prompts), `loom` (sound) | **L19** |

⚠️ **A registry that gets shorter can no longer fire.** L15 fires if `ROLES` falls below 12 kinds, and
L17 fires if `PROMPT_SLOTS` is not 7 (the same shape as what L11 does for §1–20).
**The checker itself confirms that a check becomes empty.**

### L15 — role

**⚠️ It does not fire in the reverse direction.** A role that is in the registry but unused is
**not a defect in the registry but a property of the work** (a work of one place and one repetition cannot be expected to use all 12 kinds).
So it reports the distribution as a **note** — **it does not stay silent, but it does not make it a violation either.**

⚠️ **The values are Japanese.** A role is **not a string that reaches the generator** (§1–20 has no field for it,
so it never once appears in the text that reaches the model). The registry's `dialogue` and `establishing`
are **notes for reading, not half of the spelling.**

⚠️ **The motion-axis pattern appears only inside the parentheses** — `motion (halt)`.
The registry's `motion` row holds no name, so **the data wrote the name first.**
`MOTION_PATTERNS` is its contents, and **L15 resolves the qualifier side too.**

### L16 — the motion axis

**Rule: `motion` is required — regardless of `mode`.**
§2.2 — **in film, motion is the ground, and stillness is the special case.**

⚠️ **This does not read `mode`.** It once was "optional if `mode: still`", but
**that rule had meaning only for "shots that do not run video"** — under the decision (2026-09-13, the author)
"all shots image → all shots video", **every shot runs as video**, so the premise disappeared.
**What stops is the subject, not the frame. The light and the dust move.**
That is why a shot with `mode: still` also needs `motion`.
⚠️ **The reader of `mode` is `L24`** (below). With this no longer reading it,
`mode` should have returned to being "the field no check reads" — `L24` is what prevents that.

⚠️ **It cannot be resolved from the role.** The role's **default mode** is in the registry, but **that is a default, not a rule**
(in measurement, 13 takes contradict the default, and **there is no reason to make that a violation**.
`projects/ukebi/ukebi-v2/MIGRATION.md`).
⚠️ **`既定モード` is read by no check. There is no note either** (below, "What Is Still Missing").

⚠️ **An empty `motion` is not a declaration of motion.** `{"subject": "", ...}` passes straight through the form layer
(these 3 fields have no `minLength`), so **L16 looks at the empty field too. Placing a field is not writing it.**

⚠️ **This rule is not written into the schema.** It could be written with `if`/`then`, but it is not —
**two layers would report the same defect under separate codes**, and
**a schema error only says "`'motion' is a required property`" and cannot say why it is required.**
It is treated the same as the `unit` pair.

⚠️ **Whether it is needed is decided even without `mode`** — because the decision cut it loose from `mode`.
So the branch "`mode` is absent, so I cannot decide whether it is needed" **also disappeared**.
The absence of `mode` itself is fired by **the form layer** (`mode` is required).

### L17 — §18's slots

**This is the §18 edition of what L11 does for §1–20.**
It matches §18's subsections in the specification against `PROMPT_SLOTS` **in both directions**
(a slot with no source / a source with no slot).

⚠️ **`Style Motion`'s source is the style card's `Motion character`, and the cards live in
`distill-essence-engine`. This repository does not read the cards.**
So what L17 looks at is **the existence of the slot**, not **whether its contents match**.
⚠️ **Record the remaining hole as a hole** — L17's note says so.
**Do not treat what cannot be read as read.**

⚠️ **The style declaration lives in `bible.style`.** The card's contents are not there, but **the name is machine-readable.**
**If that is empty, `Style Motion` pulls nothing** — L17 fires on that too.
**Adding the reader on the day you add the field** is to avoid a repetition of the shape where `motion` stayed at 0/30.

⚠️ **The image path has no §18.** So "there is not one §18 subsection" is
**not a defect for an image prompt** — §18 belongs to `video-spec`.
⚠️ **The narrowing rule is held in one place, `_spec_of` (`specmap.SPEC_KINDS`)** (see the `L18` section) —
copy it around, and when you fix only one, the other sings the same defect under a different code.
⚠️ **The self-test holds a pair: the same body placed in `spec:` and placed in `key_image:`.**
Place only one, and **deleting the narrowing leaves the self-test green.**

### L18 — the path is decided by the field, not by `mode`

**§18 belongs to `video-spec`. An image prompt does not hold §1–20.**

Under the decision (2026-09-13, the author) "all shots image → all shots video",
**every shot holds two paths** — `spec:` (video) and `key_image:` (image).
So **do not ask `mode` for the kind. Ask the field.** `SPEC_KIND` (`mode` → kind) **is dead.**

`L11` **requires §1–20 for every shot** — so the old version, which narrowed by `mode`,
**fired wrongly on the side of shots that end as an image.** The current way of narrowing (which field requires §1–20) is
held by `SPEC_KINDS`, and **it does not separate the rule from the checks that use it** — `L18` holds the rule and
`L11`, `L21` and `L22` follow it. **Fix only one and the other sings the same defect under a different code.**

⚠️ **`key_image` is "the one frame that is that shot's showpiece."** It is passed to video
**as an attachment (a reference image)** — **not the first frame** (make it the first frame and
that shot's change does not happen on screen). So **a shot that runs video needs it too**
— the earlier premise that "a still shot ends as an image" disappeared.
⚠️ **The reason the name changed is the same.** The old name `first_frame`
**falsely says what this field is** — hence the rename (`specmap.ADDED_WHY`).
⚠️ **But it is not made required.** Make it required, and existing records that do not know this field
(Ukebi V2's 30 takes) **drop at the form layer** — **there being no record is not contradicting.**
So it is reported **as a note, not a violation**, and moreover **folded into one item** (not 30 lines).

⚠️ **It also fires when the path registry itself is short.** It fires if `SPEC_KINDS` is not two kinds —
**lose one path and that path is checked by nobody.**

⚠️ **The image specification's form is not a "section" but "a paragraph inside one section."** The canonical form is
the **2 paragraphs** held by the section `## 投入する1本の文字列` (## The Single String to Feed In), and **the 1st paragraph is `Prompt`, the 2nd is `Negative`**
(`SPEC_KINDS["image"]["body_section"]` / `body_paragraphs`).
**It differs from video's §18 only in how it points; what it points at is the same** — Negative is in both.

**Why not split it with headings?** A heading **cuts a section at any level** (`specdoc.HEADING`).
Split it into the 2 sections `## Prompt` and `## Negative` and **a heading enters between the bodies**, so when the author selects
from the `Prompt` line to the `Negative` line **in one go, that heading is swept in** — and those 2 lines
**enter the model as one string joining `Negative` after one blank line at the end of the `Prompt` body.**
**Delete the heading and the bodies are continuous**, but **two continuous paragraphs can only go into one section.**
That is why **the paragraph is the unit.**

⚠️ **Do not place a section that separately transcribes the joined string.** A copy contradicts —
**a single blank line is exactly the blank line that joins them.**

⚠️ **Why models are needed.** §18 is **a model-specific projection** — the same §1–17
becomes a different text when the model changes. So §18's heading
accepts **`18. <model name> PROMPT MAPPING`** as a family, and **resolves the model it names against `MODELS`.**
No name (`18. PROMPT MAPPING`) / not in the registry / **the kind differs from the path** — all fire.

⚠️ **`mode` is not read here.** The kind no longer depends on `mode` —
so even a `mode` outside the registry does not fire this check (the form layer and `L24` fire it).
The count is reported as a **note**. **If the check becomes empty, the note says so.**

### L19 — that the aim arrives

**Where `L12` closes "where the field comes from", `L19` closes "where the field goes."**
**A field with no destination does not reach generation — and it fails to reach silently.**

| Destination | Meaning |
|---|---|
| `自前` (own) | **It never appears in generation.** `role`, `unit`, `time`, `beats` and `effect` are Japanese, so **they are not passed in the first place** (`CLAUDE.md`, "do not make the strings you pass Japanese") |
| `prompt:<slot>` | One of §18's 7 slots |
| `params:<key>` | `take.params` (`seed` / `duration` / `aspect` / `references`) |
| `handover:<base>` | **Hand it to another base** — `distill` (image prompts), `loom` (sound) |
| `edit:timeline` | **Not passed to generation; decided in editing** — the adopted duration and so on |

⚠️ **The destination does not depend on `mode`.** With two paths, **the same field always goes to the same place.**
One field can go to two places (`duration` is both a generation parameter and decided in editing) —
so the value is held as a **tuple**. But **it no longer changes with the mode.**
⚠️ **It once looked at "must be written for all modes."**
That branch **never fires even once** — if the value is the same across all modes, the branch might as well not exist.
So **the whole dimension was dropped.**

⚠️ **It also checks that the destination actually exists.** Sending to a slot that is not in the registry, sending to a key that is not in `take.params`,
handing to a base that is not in the registry — **the kind alone does not arrive.**
And **it fires when the reason (`DESTINATION_WHY`) is missing** — **what is not passed, and what is only partly passed,
do not survive unless written.**

⚠️ **An empty destination is the same as no destination.** It wears the face of a declaration and does not go to a single place
— **an empty check calls it OK.**

⚠️ **It closes the path fields themselves too.** It fires if the fields `SPEC_KINDS` points at (`spec`, `key_image`) are
not in the schema — **declare a path and the field is missing, and that path exists nowhere.**

⚠️ **`自前` (own) is not "dropping out."** Not being passed and the thing that should be passed not arriving are different.

### L20 — whether `Style Motion`'s destination is non-empty

**`L17` passes through here.** It only sees that the slot **exists** in the specification,
not **whether that slot carries anything.** `Style Motion`'s source is the style card's
`## Motion character`, and **in measurement only 2 of 55 cards hold it** —
choose a style that does not, and `Style Motion` **exists but is empty. An empty check calls it OK.**

⚠️ **The cards are outside this repository.** Look at `$SVL_STYLES_DIR`, and if there is none, at the neighboring
`distill-essence-engine/references/styles`. **If it cannot be read, report "cannot be confirmed"**
— **do not give what you have not confirmed the face of having confirmed** (the same shape as `L9` and `L14`).
**It is correct that someone who cloned this does not have it.**

⚠️ **It only reads.** The cards are `distill-essence-engine`'s property and are
**not rewritten** (`CLAUDE.md`). Whether what was pulled is correct **has not been checked yet** — the note says so.

### L21 — does the image Negative cover the work's prohibitions

**Cover, not equal.** The image Negative **must contain all** of the work's prohibitions
(`bible.negative_base`), but **it may hold more than that** —
because the disclosure series (such as "do not show the inside of the kiln") **differs from shot to shot.**
So only **the missing sections** fire, and surplus sections do not fire.

⚠️ **This check reads the Negative as a "paragraph."** The image specification holds no sections —
the canonical form is the 2 paragraphs inside the section `## 投入する1本の文字列`, and `Negative` is its **2nd paragraph**
(see the `L18` section). So **the paragraph count is also matched against the naming** —
**2 paragraphs expected and 1 paragraph found, and it fires.** With the wrong count, `index` points at a different paragraph, so
**you read `Prompt` while thinking you read `Negative`.**
The self-test holds "1 paragraph", "3 paragraphs" and "no section" separately —
⚠️ **"there is no section" and "it is not written" are different defects.**

⚠️ **It compares stems.** Measurement — Ukebi V2's ledger writes `no photorealistic` and
§18 writes `not photorealistic`. **Compared as raw strings, 30/30 become false positives**
(the same shape of error as when `L4` judged "movement" by the verb).
The negative word carries no meaning; **the stem is what carries meaning.**
So it drops `no` / `not` / `never` / `without` before comparing —
**the self-test holds a "does not fire" example that mixes the two.**

⚠️ **It fires if the prohibition is not declared.** With no `bible.negative_base`,
**nobody has decided what should be covered** — **with nothing to cover, this check sees nothing.**

⚠️ **It does not run against a video specification's §18.** There, **matching against the disclosure ledger** is the main body and
`L10` and `L14` carry it. **There is still no check that looks at "does it cover the work's prohibitions" on the video side** — a hole.
**Record it as a hole.**

⚠️ **A shot with no image specification does not come here.** That "there is no record" is folded into one item by `L18`
— **two layers do not report the same defect under separate codes.**

### L22 — are the image specification's 7 fields non-empty, and does the card it names hold that field

**The image edition of `L20`, and more than that.** The image specification **holds no sections** (`L18`).
But **it is not without structure** — it is made by filling the **holes in 2 cards** of `distill-essence-engine`.

⚠️ **There are 2.** This image passes through **both** the `format` (`scene-board`) and the `style` (`luminous-anime`).
So the holes are for 2 cards as well —

| Card | Holes |
|---|---|
| `format` (`scene-board`) | `SCENE` / `CHARACTERS` / `ACTION` / `LOCATION` / `LIGHT` |
| `style` (`luminous-anime`) | `SUBJECT` / `ACTION` / `LOCATION` / `ACCENT` |

⚠️ **The sum is 7, not 9.** `ACTION` and `LOCATION` **exist under the same names in both cards**
— so **the same value goes into both holes.** This was confirmed by measurement (`grep` read the
`## Environment variables` of the 2 cards and counted the duplicates). **One of them alone cannot make this one frame.**

⚠️ **And the main body of this check is the naming side.** The specification names
**which card's hole** it is via `REF_FORMAT` and `REF_STYLE`. `L22` resolves that name and looks at **whether the card actually declares that field.**

- **The specification holds a field the card does not declare** → it fires.
  **That value is no card's hole** — it reaches generation, but **it has not passed through the card's grammar.**
- **The card declares a field the specification does not hold** → it fires.
  **The card's hole is unfilled** — that variable reaches generation **still empty**.

⚠️ **Why this is needed.** Measurement — **of the 44 `format` cards, not one declares all 4 style variables.**
So the version where the image specification held only the 4 fields `SUBJECT` through `ACCENT`
**was non-empty in all 4 fields and was still defective** — **the composition comes from no card at all.**
**A check that counts fields cannot catch this. Only a check that reads the naming catches it.**
⚠️ **"The declaration is correct" and "it is read as declared" are different** —
what `L22` confirms is the latter, and **it does not look at the former (whether the card's contents are correct).**

⚠️ **If the card cannot be read, it does not fire. It is a note.** `distill-essence-engine` is
**a separate repository**, and someone who cloned this does not have it — **do not make the absence of the other side a violation.**
⚠️ **`SVL_STYLES_DIR` always applies to `style` and does not apply to `format`**
(it applies only when the destination it points at ends in `formats`) — **so as not to tell the lie of
reading a style card as a format card while still pointing at styles.**

⚠️ **It does not look at whether the contents are correct.** Whether `SUBJECT`'s value is really the subject **cannot be read by this layer.**
All it sees is **that it is non-empty** and **that the naming matches** — the note says so.

### L23 — do the intent and the specification agree on duration

**`shot.duration` ↔ `Duration:` in video specification §1.**

⚠️ **This is the only field whose value may be compared, by measurement.** Compare `place` and `time` by value and
**60 false positives** appear in measurement — because **what is passed is not the field's value but what the field points at**
(that is why `FIELD_DESTINATION` sends `place` to `handover:distill`).
Duration is different — **§1's `Duration:` and `shot.duration` point at the same quantity.**

⚠️ **"There is no §1" and "§1 has no `Duration:`" are different.** The former is fired by `L11`
(the §1–20 registry). The latter **is fired by nobody** — so it fires here.
**An intent that cannot be matched is not being matched.**

⚠️ **When reading §1, read it by subsections** (`_section_body`). `specdoc.section` cuts regardless of the heading's level,
so when `## ` comes right after `# 11. MOTION` **the body looks empty** — that is what measurement shows.
**A section's contents live in the subsections.** It may be read as "empty" **only when the subsections are all empty too.**

### L24 — what `mode` requires

**This is the reader of `mode`.** `L16` no longer reads `mode` (motion became required in all modes).
So with no check here reading `mode`, **`mode` would return to being "the field no check reads."**

| `mode` | New meaning | Requirement |
|---|---|---|
| `still` | The subject stops. What moves is **only the light and the dust** | The video specification's §11 is non-empty |
| `composite` | The subject stops, and **the frame is a composite of layers** | §11 non-empty + **`text_channel` non-empty** |
| `motion` | The subject moves | **None** (empty row) |

⚠️ **The rule comes out of "does the subject move."** The place to write a stopping subject is §11 MOTION —
empty, and **you cannot tell whether it is stopped or you forgot to write it.**
`composite` means "composite" (`timeline.text_events` burns it in, and **the generator does not draw text**)
— with nothing to burn, **that shot composites nothing.**
⚠️ **The reverse does not hold** — a `motion` shot can also hold a `text_channel`. **It is one-directional only.**

⚠️ **Do not drop the empty row.** That `MODE_DEMANDS`'s `motion` row is empty is
**the declaration that "there is no requirement"** — drop it and the distinction between "no requirement" and "forgot to write" disappears.
**Empty and absent are different.** That is why L24 **closes in both directions** (the keys of `MODES` and `MODE_DEMANDS` agreeing).

⚠️ **Do not give what cannot be confirmed the face of having confirmed it.** **Whether §11's contents really stop the subject
cannot be read by a machine.** Even if the text says "the dough swells", this layer cannot read that as stopped.
So it reports that as a note — **it does not look at "the subject stops" by string-matching vocabulary.**
That would be **a check I built to match the text I wrote**, and **the same as an empty check.**

### ⚠️ Firing Against a Running Artifact

| Check | Ukebi V2 (30 takes) | What it is saying |
|---|---|---|
| L6 | **30** | `attached` is 0/30 — **the original artifact had no declaration** |
| L14 | **5** | spans beyond the declaration |
| L15 | **0** (2 notes) | all 8 kinds are registered (the **notes** report the distribution and the qualified spelling) |
| L16 | **30** | `mode: motion` is 30/30, and yet `motion` is 0/30 |
| L17 | **30** | §18 has no `Style Motion` (measurement: 0/99 takes) |
| L18 | **0** (2 notes) | the 30 takes hold the video path (`spec:`), and §18 names `WAN 3.0` (`video`) — **they agree.** One note is **not holding `key_image`** (there is no record, not a contradiction); the other note is the number confirmed |
| L19 | **0** (1 note) | the 18 fields are closed. ⚠️ **The note says "will arrive", not "arrived"** |
| L20 | **0** | the 30 takes hold no `Style Motion`, so **this check sees nothing** (`L17` is firing 30). ⚠️ **Ukebi's style `soft-cel-anime` holds a `Motion character`** — **both are true.** |
| L21 | **0** | the 30 takes hold no `key_image`, so **there is not one other side** (`L18` reports it as a note) |
| L22 | **0** | same as above. ⚠️ **Ukebi V2 holds no `key_image`, so the naming side has never been read either** — **this check has actually fired only inside the self-test.** |
| L23 | **0** (1 note) | the durations agree 30/30 |
| L24 | **0** (1 note) | all 30 are `mode: motion` and **hold no requirement** — so this check **sees nothing on Ukebi**. The note reports that. |

**Decide a rule and the existing artifacts still do not satisfy it.**
§11 MOTION **exists in all 30 and all 4 subsections are non-empty** — **only the destination field is empty.
So these 30 are a real omission** (unlike `attached`'s 0/30. That one is
**the original artifact having no declaration**). **Do not soften the check to lower the number.**

## ⚠️ The Mapping Is a Registry, Not Prose

**A shot record takes `video-spec` §1–20 as its parent.** Then
**which of the 20 sections moves to which field, and which does not move**, must be decided.
**Left as prose it rots** — so it is placed in `specmap.py` **as a registry**, and L11 and L12 confirm it.

| Code | What it fires on |
|---|---|
| **L11** | The specification's sections are not as the registry says (added / missing / out of order) |
| **L12** | The field-to-section mapping is not closed |

⚠️ **L11 also looks at the registry's own length.** A registry that should be 20 sections becoming 3 means
**it will not fire even when a section is added to the specification** — **the check becomes empty.**
⚠️ **L12 looks in both directions.** A section naming a field, with the field not naming the section, means
that field **has no source** — a field somebody added on a whim.
**One direction alone does not make the mapping closed.**

⚠️ **A field marked `("added", None)` does not have to be closed. But write the reason.**
`shot` (identity), `role`, `effect`, `mode`, `spec`, `key_image` and `attached` — these 7 are like that —
**record that there is no field in §1–20, leaving it absent.**
`attached` especially: **the result of generating while it was absent** is the two takes of Ukebi V1.

⚠️ **A section that does not move does not drop out.** It stays as it is in the specification (what `spec:` points at).
**What drops out is from the shot record, not from the work.**

And — **the reason it drops out is not "because it is one continuous take."**
§10 Camera Behavior is the only section that names a "continuous take", and **it does not drop out.**
What actually drops it is **"does the ledger infer about that shot"**
(details and measurements are in `projects/ukebi/ukebi-v2/MIGRATION.md`).

## ⚠️ Identity Is Taken From the Specification Side

**The specification writes its own name in §19** — `Instance ID: ukebi-v2-ch03-seg03-30s-01`.
**The body with the trailing `-<seconds>s-<take>` dropped is the shot ID.**

**⚠️ If they contradict, L10 silently reads a different §18.** If the `spec:` a record points at and the record's name diverge,
it checks the disclosure change points against **a neighboring shot's text** — **a misreading does not fire.**

⚠️ **`Segment ID` is not the key to identity.** In Ukebi V2's 30 takes, 27 are `NN-N`
and **only the 3 of the prologue are `A-N`** — **the same range has the two spellings `A` and `序` (prologue).**
**The same shape of deviation as §16's final-chapter heading lacking the four characters `開示台帳` (disclosure ledger)**,
and either of them, **derived naively, drops 3 takes.** L13 reports this **as a note**
— **existing artifacts are not fixed** (they are records).

⚠️ **The image path holds no §19.** So "the specification does not name itself" is
**not a defect** — **there is no section to name it.** Without narrowing, the image path
**fires falsely** (the same shape of error as `L11` and `L17`).
⚠️ **The narrowing rule is held in one place, `_spec_of` (`specmap.SPEC_KINDS`)** (see the `L18` section).
⚠️ **The self-test holds a pair: the same body placed in `spec:` and placed in `key_image:`** —
place only one, and **deleting the narrowing leaves the self-test green.**

## ⚠️ Motion Is Not Evidence of Disclosure

**Has the ledger arrived?** Where L10 is the check that falsifies the ledger's claims,
what L14 asks is **the span the ledger has not reached.** But **written naively it breaks.**

**Firing on "§18 moved and there is no declaration" fires 18 times across Ukebi V2's 30 takes.**
Of those, **4 are rotations** — `02-01`'s section set is
**completely identical as a frozenset** to `01-01`'s (49 sections), and `03-01` returns to the same set. **A rotation is not a disclosure.**

⚠️ **§18 is not monotone.** The ledger assumes monotonicity ("not yet" → "already"; it does not return), but
**§18 is a projection written out per shot**, so it goes back and forth according to that shot's needs.
**That is why "motion" is not evidence of disclosure.**

So what L14 takes is only **the change that persists** — when a section is

| Direction | Condition | Meaning |
|---|---|---|
| **Added** | In no preceding set, and in every subsequent set | Newly forbidden. **It does not return** |
| **Removed** | In every preceding set, and in no subsequent set | **What may be drawn increased.** It does not return |

that section is **not a rotation**. Measurement: **6 places if additions only**, **7 places if deletions are included**
— `01-01` (−2), `03-03` (+14 / −3), `06-01` (+2 / −1), `06-03` (+1),
`08-01` (+1), `09-02` (+1 / −1), `09-03` (+4). **Of those, the ledger declares 2.**

⚠️ **It fires on deletions too. A prohibition disappearing is a permanent expansion of what the model may draw**
— it is even the more dangerous direction than an addition (a new prohibition).
At `01-01`, `no first-person body parts` and `no viewer's hands` disappear and never return.

⚠️ **It does not look at meaning.** The same discipline as L10 — if `no girl` disappears and `no female figure`
remains forever after, **that is a change that does not return as a set**, and L14 fires.
**It does not decide whether it is a rewording of the same prohibition.**
Decide it and you get the same false positives as L4 (a detector tuned to one work's vocabulary fires on the other).

⚠️ **A change that does not return is irreversible.** §18 holds that prohibition (or does not hold it) forever after.
Add it to the ledger, or **write the reason for not adding it into the record** — write nothing, and that span is
**accepted by nobody** (L7a looks at "does it hold a state before the declared change point",
so **with no declaration, L7a's premise collapses**).

⚠️ **What L14 does not catch.** A section that **wavers and then disappears** — isomorphic to §16's flicker,
and the family of `no ... inside the fire` is like that (it drops at `01-3` and `03-2`, and does not return from `05-1`).
**By definition it is not "irreversible"** (because it wavered first), so it does not fire. **Record it**
(`projects/ukebi/ukebi-v2/MIGRATION.md`) — **do not treat what cannot be judged as judged.**

## ⚠️ Does the Take Match the Real Thing (L25)

**`S1` looks at the form. `L25` looks at the contents.** That a take passes the schema
says nothing about that take being **right about anything**.

⚠️ **What came back finally exists, and that made this check writable.**
Until then **there was no other side to match against** — and **with no other side, it cannot fire.**

**What fires (11 types)**

| | |
|---|---|
| The take names a **shot that does not exist** | there is no other side in the record — **this take belongs to nobody** |
| `kind` is not in `SPEC_KINDS` | ⚠️ **a take on a path not in the registry cannot be checked from the registry's side** |
| `(shot, kind, index)` is duplicated | the serial number does not distinguish "overwrite" from "a separate generation" |
| `provider.model` is not in `MODELS` | same as above |
| `MODELS[model]["種別"]` and `kind` contradict | **the path contradicts** |
| The file `params.source` names does not exist | **the canonical of the string that was fed in is lost** — it cannot be regenerated |
| Measured vs. §1's `Frame Rate` / `Resolution` / `Duration` | **the requested value and the value that came are different** |
| `adopted: true` twice or more for one `(shot, kind)` | **adoption is one take** |

Note (not a violation): **a `source_version` drift** — the specification is corrected after generation (§20 exists for that).
**So the path alone is not enough.** The path stays the same while the contents change.

⚠️ **The duration tolerance is one frame** (divided out from `measured.frame_rate`).
⚠️ **The boundary of the tolerance, unrounded, becomes an error in the check** — `6.0 + 1/24` is
not exactly one frame in floating point (`1.0000000000000007`). **Convert the difference into frames first, then round.**

### ⚠️ What `L25` Has Not Confirmed (report as a note, staying a hole)

- **It does not open `media/`.** `projects/hitosara/media/README.md`
  **declares that "the base does not read here", and `L25` honored that declaration.**
  So it **does not confirm the existence of the file `take.file` names** —
  **a name is a name, not a proof.**
  ⚠️ **The number of mp4s in `media/` and the number of `video` takes do not agree.**
  There are 2 reasons, and **a machine fires on neither** —
  **① placed but no record** (because it does not read `media/`, the difference is invisible),
  **② the file the record names is already gone** (because it does not confirm existence, a loss is not noticed).
  ⚠️ **Do not write the numbers here.** Numbers move — **write them and they contradict.**
  ⚠️ **Closing this hole would mean changing that declaration first** — **undecided.**
- **An image take has no other side to match against.** An image specification holds no §1
  (it names neither resolution nor duration) — **so there is no value to compare on the record's side.**
- **`params.references` is not written on any take** —
  **what was actually attached is recorded nowhere.**
  ⚠️ **The shot record's `attached` is a declaration, not a record** (what `L6` looks at is
  **the contradiction between the ledger's `reference_set` and `attached`**, not **the fact of attachment**).

## ⚠️ What It Guarantees / Does Not Guarantee

**This repository holds not one line of generation.** There is no code that calls a generator,
and no API key. **So it cannot say "what you aimed at will always be generated."**
What it can say is —

| | What | Which check |
|---|---|---|
| **Guarantees** | **It arrives.** Every field of the record has a declared destination (both directions) | **L19** |
| **Guarantees** | **It arrives at the right place.** The shape of the path (`spec:` / `key_image:`) and the model §18 names | **L18** |
| **Guarantees** | **The destination is not empty.** `Style Motion`'s pull-target actually exists | **L20** |
| **Guarantees** | **The image path's contents are not empty.** The Negative covers the work's prohibitions, **the 7 fields are filled, and the card it names holds those fields** | **L21**, **L22** |
| **Guarantees** | **The intent and the specification agree on duration.** | **L23** |
| **Guarantees** | **A still shot is written as still** (§11 non-empty. `composite` also needs `text_channel`) | **L24** |
| **Guarantees** | **What came back matches the shot, the style and the measurement.** | **L25** |
| **Guarantees** | **It is not broken.** L0–L25 fire before generation, and everything that fired can be explained | all |
| **Does not guarantee** | **That the generator draws the aim.** | —— |
| **Does not guarantee** | **That a still shot's §11 really stops the subject.** | —— |
| **Does not guarantee** | **That the file `take.file` names actually exists.** | —— |

⚠️ **Generation is a sample** (`take.schema.json`). So the shape of the guarantee is
**"the aim arrives"**, not **"it is drawn."**
Arriving can be confirmed by a machine. **A broken aim is known before generation.**

⚠️ **The paths doubled, so the places that must be reached doubled too.**
Write only `spec:` and not `key_image:`, and **the image side is never checked**
— `L18` says that **as a note** (there is no record, not a contradiction).
**Do not read a note as "0, so it is correct."**

⚠️ **`L19`'s note is not "confirmed."** "Not one field lacks a destination" means
**the declarations are closed**, not a check that **the text actually carries that field.**
**A round-trip check (reading the assembled text back into the record) does not exist yet** — below, "What Is Still Missing."

## What the Checker Does Not Decide

**It only names the contradictions; it does not decide which side is right.**

- **L6** When the intent and the actual contradict, it cannot decide whether the ledger is stale or the shot record is wrong.
- **L7** Even if the "actual" read independently from §16 agrees with the ledger, **that does not make the ledger correct**
  — it merely read the same source text with a different tool. **Different reading tools miss different things.**
- **L10** It looks only at **whether §18's section set changed**. **It does not look at meaning.**
  Even if sections swap, it may be a rewording of the same prohibition —
  **"changed" is not "became new."**
- **L14** It does not decide whether the increment that does not return is **a disclosure** or **a rewording**. Likewise it **only looks at the set**.
  Decide what cannot be decided and you get the same false positives as L4.
- **L8** A key not in the ledger fires, but **the key naming convention itself is undecided**
  (`<entity>.sheet` / `<place>.geography` are accepted by derivation. Not canonical).
- **L25** **When the specification and the measurement contradict, it does not decide which is right.**
  Whether the specification's `24fps` is wrong, or the model produced `30fps` that was never requested,
  **cannot be decided from this record alone.** ⚠️ **It does not decide, but it does not stay silent** —
  **a record must not silently hold that the requested value and the value that came are different.**
  Likewise a **`source_version` drift** does not decide **whether the correction was right**.

## What Is Still Missing

- **The handover sheet.** A layer that assembles **what is passed from the record to the generator** (§18's 7 slots,
  `take.params`, the image prompt, the sound) **does not exist yet.** What `L19` looks at is
  **the declaration of the destination**, not **whether the assembled text actually carries that field.**
  ⚠️ Add the **round-trip check** (reading the assembled text back into the record) at the same time as that layer.
- **Matching the style card's contents.** What `L20` looks at is the **existence** of `Motion character`,
  not **whether what it pulled matches `motion` or `Style Motion`.**
  The cards live in `distill-essence-engine` and **someone who cloned this repository does not have them.**
  **When it cannot be read, report "cannot be confirmed"** — **record the hole as a hole.**
- **Matching `motion.law`.** The 3 parts — §18's slots, the record's `motion`, and `bible.style` — are
  now in place, but **the matching that ties the two together still does not exist.** ⚠️ **Write it now and it becomes a check that never fires**
  (`motion` is 0/30). **With the other side empty, nothing fires** (the same discipline as L0 and L9).
- **The canonical spelling of a role.** 6 shots use the qualified spelling (`motion (halt)`),
  and **whether to make the registry's name or that one canonical is not decided.** L15 reports it **as a note**.
- ⚠️ **Not one person resolves `ROLES[...]["既定モード"]`.** The registry holds a default mode and
  `rolemap.resolve()` resolves **the spelling** (`motion (halt)` → `motion` + a pattern) —
  **but nobody resolves `既定モード`.** The result of `grep 既定モード engine/ledger/*.py` is
  **only the definition in `rolemap.py`**. **There is no note either.**
  ⚠️ **This is the same shape as `motion` being 0/30** — **the field exists, but no reader does.**
  ⚠️ **Write down the reason for not adding it, too.** The default mode is **not a rule** —
  in measurement, 13 takes of Ukebi V2 contradict it (the breakdown is all role `reveal`).
  Firing it as a violation now would **fire far louder than a note** — and **there are two parties to fix**
  (fix the registry side, or write the reason on the shot side). **Until one is decided, it cannot fire.**

  | How the registry says it | Meaning | Who fixes it |
  |---|---|---|
  | `("still",)` and so on | **There is a default** | If it contradicts, **write the reason** (registry or shot) |
  | `()` | **Any** — any mode is fine (`transition`, `montage`) | Nobody fixes it |
  | `None` | **Undecided** — not decided yet (`catalogue`, `narration`, `departure`) | **Fill in the registry** |

  ⚠️ **`()` and `None` are different** (`rolemap.py`). Use the same symbol for "any" and "undecided" and
  **what is undecided wears the face of what is decided.**
- ⚠️ **A prohibition can be written only at the unit of a tool, while a disclosure can be written at the unit of a part.** What `known_keys`
  gives a tool is only `P.appearance` and `P.negative` — so
  `forbidden_set: [KAMADO]` forbids **the thing called the kiln, whole**.
  But the disclosure ledger handles the **part** `KAMADO.interior`
  (07 of `projects/hitosara` **may photograph the door, but may not photograph the light through the gap**).
  **There is no field to write this asymmetry in, right now** — in 07 that distinction is
  carried by `disclosure_state` and by prose on the specification side (`MUST NOT`).
  **It has not been made into a machine-readable form.**
- **The report that `takes/` is empty lives on the `read_errors` side.** With 0 shots,
  L0 fires, but **0 takes fires no check** — `Project` merely reports
  one line at load time. **A report, not a check.**
  ⚠️ **An empty `timeline/` does not even get that** — because `Project` does not open it.
- ⚠️ **No check reads the disclosure series on the image-prompt side.** What `L10` and `L14` face is §18,
  **not the image prompt.** But the image specifications of `projects/hitosara`
  hold **the same series** as §18 — `no oven interior`, `no visible flame`,
  `no glow through the door seam` **are in all of them until 08 opens, and drop at 08.**
  At 09, `no cut loaf`, `no visible crumb` and `no cross-section` drop too.
  **The ledger declares where they drop**, and yet **there is no check that reads it.**
  ⚠️ **`L21` does not pass through here.** What `L21` looks at is whether the image
  **covers the work's prohibitions (`bible.negative_base`)** — not **whether the disclosure series opens at the ledger's position** —
  because that **differs from shot to shot** (hence "cover, not equal").
  **The other party is the handover layer** (the first item under "What Is Still Missing").
  Until then, this series **is placed as prose on the specification side** —
  **what a machine does not read, keep in a form a person can read.**

- **The requiredness of `role`.** If `role` is empty, what judges that shot is undecided.
  ⚠️ **The form layer's `required` looks at it** (not L15 — L15 looks at **whether the value resolves to the registry**).
- **Matching the wardrobe of a reference sheet.** The rule that resolves **which one applies** from the ledger's `states.<name>.wardrobe` and
  the shot's `place` × `time` does not come out of the prose
  (false positives arise for the classroom at night, the school-festival back yard at night, the room at dawn).
  The conditions that apply are confirmed from the artifact side.
- **Do not make `at` a key.** §16's headings name a range, but the body writes the prohibitions of "this one take", so
  the forbidden set splits in 9 of the 10 ranges. **It is a grouping for people to read, not a key.**
