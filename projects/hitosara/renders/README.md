<!-- i18n-version: 1.0.0 | canonical: projects/hitosara/renders/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# `renders/` — where what editing produced (the work) goes

> **A story becomes a run of shots.**

**`media/` is the place for samples, and this is the place for the work.**

| | |
|---|---|
| `media/` | **Samples.** What the generator returned. A few per shot |
| `renders/` | **The work.** Samples chosen, cut, and joined |

⚠️ **Even for the same video, a different place means a different meaning.** Put a sample in `renders/` and it wears the face of a work,
**put a work in `media/` and it wears the face of "a take with no record."**

⚠️ **What was joined by hand is also here.** Whether it was done by hand or by the foundation **does not change the place**
——**a work is a work.**

## ⚠️ Why we do not distinguish by name

`media/README.md` stipulates "file names start with `NN__`." **That plan was abandoned.**
⚠️ **That spelling has been rewritten by the author's hand many times**——it moved even while I was watching.
**A rule that moves cannot carry a distinction.** So **we separate by place.**

⚠️ **Do not put it in `takes/`.** That one is a **record** (`*.yaml`).
Put it there and **`L25` reads it and `provider.model` becomes a lie**——**this is not a take.**

## ⚠️ Do not place things alone

Each file in `renders/` **needs a record that claims it**——otherwise
**the same hole as `02_20260913-….mp4` opens again** (the entity and the record contradict, and the machine does not fire).

⚠️ **This rule is currently broken.** The two files under "what exists now" below
**both have no record in `timeline/`**——because a claiming record cannot be written (next section).
**Writing a rule and the rule being kept are different things.**

**Rule: the name of `renders/<name>.mp4` is the same as the `timeline/<name>.yaml` that produced it.**
⚠️ **The direction is one**——**the record claims the thing. The thing does not claim the record** (copies contradict).

⚠️ **But `timeline.schema.json` has no field that claims the render file.**
Putting it in `interchange` (`additionalProperties: true`) would let you write it, but **that is not "a field exists."**
**So a check that reads this rule cannot be written now. It is a hole.**

## ⚠️ Right now, the record side cannot be written

**Even if a joined thing exists, a `timeline/` record claiming it cannot be written now.**
`clips[]` requires `shot` and `take` (`schemas/timeline.schema.json`)——but
**not a single video take has `adopted: true`** (`02` and `06` are `false`. The rest write nothing).
**In other words, which samples were lined up in which order is not on the record side.**

⚠️ **Selection is the author's work.** Say "these N, in this order," and that becomes the record.
**Until then, the things in this directory cannot be pulled up from the record.**

## ⚠️ Neither the emptiness nor the fullness of this directory is reported

Same as `timeline/`. The emptiness of `takes/` is reported ("not a single one").
**No one reads this one**——**a check that does not report looks the same as a check that passed.**

⚠️ **`.mp4` is already tracked by LFS in `.gitattributes`** (same as `media/`).
⚠️ **Placing alone does not make it LFS.** Only once you `git add` does it become a 133-byte pointer.
⚠️ **The second column of `git lfs ls-files` is not the presence or absence of the local entity.**
`*` means "a complete object" and `-` means "**an LFS pointer**" (`git lfs ls-files --help`)——
in other words, it is a mark that **the copy on disk is a pointer (or absent)**, and
**it does not say whether the entity is in `.git/lfs/objects/`.** (Same as `media/README.md`)

## What exists now

⚠️ **Do not write the count**——the count moves, **write it and it will contradict.** If you want to count, read `git lfs ls-files`.
What exists is **2 files**——**the same picture, with only the presence of audio differing.**

| | |
|---|---|
| `hitosara.mp4` | **Silent.** The version the author joined by hand. **The canonical picture of this work** |
| `hitosara+soft-gold-sky.mp4` | **The same picture + `soft-gold-sky`.** The version to publish |

⚠️ **`+` is the mark of "the picture is the same and sound was added."** The picture was not re-encoded (`-c:v copy`).

⚠️ **This version is already published**——on the author's own channel
(YouTube, `https://www.youtube.com/watch?v=pJyiziIUaPY`).
**The music record below is carried in that video's description**, so the condition
"take this table along with it" is met there.

⚠️ **But what is on YouTube and what is in this directory are not the same object.**
YouTube serves **its own encode** of it, and ⚠️ **whether the file that was uploaded is this one,
or a lighter one made for it, is not written anywhere.** **Two surfaces exist, and which is
canonical is not decided**——**and no check fires this** (no one reads `renders/`, as above).

### ⚠️ The sound of the silent one is not absent but **empty**

`hitosara.mp4` **has** an `aac` audio track. But **its contents are pure digital silence**——
measured at `mean_volume: -91.0 dB` **and** `max_volume: -91.0 dB` (the same over the whole interval and over partial intervals).
**"There is no track" and "the track is empty" are different.**
So **in the `+` version the BGM does not mix in underneath; the BGM is the whole of this work's sound.**

⚠️ **Do not carelessly "layer the BGM on and thin it out" onto a silent file**——
because what you would be layering onto is empty. **And there is no check that fires this discrepancy**
(`renders/` is read by no one). **So this table is a record only a person can read.**

## ⚠️ The music record (required for the version you publish)

⚠️ **If you show this version to people, take this field along with it.** Not writing the source is
**the same as not meeting the license conditions.**

| | |
|---|---|
| Track | **`soft-gold-sky`** |
| Source | `catalog.json` of **open-lofi** (`https://github.com/btahir/open-lofi`) |
| Pack declaration | **`"license": "CC0-1.0"`** (one for the whole pack, 166 tracks) |
| Cut position | **0 → 49.249208 seconds** (cut to match the work's duration). **Fade out from 45.2 seconds** (0.3-second fade in) |
| Measured loudness | **−16.0 LUFS** (LRA 7.8). Applied a gain of **−0.70 dB** |
| Breakdown of the measurements | **Read `HISTORY.md`**——⚠️ **not written here** (they are past measured values) |

### ⚠️ The pack's declaration and the files' claims contradict

⚠️ **[Measured]** **All** 166 tracks' ID3 `comment` is **`made with suno; created=…; id=…`**
——**the pack declares "CC0," but the files themselves claim to be generated output.**
The claim of `soft-gold-sky.mp3` is
`made with suno; created=2026-03-13T05:06:05Z; id=fd5744ef-b45f-4571-b7d4-ef801b92d95f`.

⚠️ **This is a live example of this foundation's principle itself**——
**"That a declaration is correct and that it is read as declared are different things."**

**Therefore:**

- **If you are only watching locally, the risk is low.**
- ⚠️ **If you publish, the risk is the author's.** The declared CC0
  **is not in a form the distributor can verify** (as long as it is generated output, the chain of rights does not close).
  **To err on the safe side, choose a track whose declarer is the author themselves**——for example
  **Incompetech (Kevin MacLeod)'s CC BY 4.0** is **declared by the author himself.**
  ⚠️ **CC BY requires attribution. That is why this table is needed.**

⚠️ **FreePD is closed** [Measured]——the 2026 guidance still recommends it, but **it does not open.**

⚠️ **`*.md` is not read.** So this text is not counted as a render——**being counted would be a problem.**
