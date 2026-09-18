<!-- i18n-version: 1.0.0 | canonical: projects/habits/promo-chinatsu/renders/README.md | translated: 2026-09-18 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# `renders/` — the work, and the sound it wears

> **A story becomes a run of shots.** Here it becomes twenty-eight seconds of it.

`media/` is the place for samples, and this is the place for the work — the same split as
`projects/hitosara/renders/`. ⚠️ **The rule is in that README, not this one.** What follows is
what is *different* here.

## What exists now

| | |
|---|---|
| `碓氷千夏.mp4` | **Silent.** The five shots joined. **The canonical picture of this work** |
| `碓氷千夏+bamboo-shadow-waltz.mp4` | the same picture + `bamboo-shadow-waltz`. **Adopted** |

⚠️ **Do not write the count** — the count moves. **Eight were auditioned; four were built; one was
adopted.** ⚠️ **The three that were built and not adopted are named rather than dropped** —
`graphite-in-the-quiet` · `morning-in-the-hiss` · `chapter-by-lamplight`. **They existed, and this
record says so.** ⚠️ **They are not in this directory** — it holds the adopted one and the silent
picture, which is what a selection looks like from the outside. ⚠️ **The selection is the
author's** (2026-09-18), and it has the same shape as hitosara's: **four candidates, one kept.**

⚠️ **`+` is the mark of "the picture is the same and sound was added."** Measured: the video
stream of both is **byte-identical** to the source
(`MD5=0f9ea0459665af7a23fe2691f9a67938`, taken with `-map 0:v:0 -c copy`).

## ⚠️ The silent one's sound is not absent but **empty**

`碓氷千夏.mp4` **has** an `aac` audio track, 48 kHz stereo. Its contents are pure digital
silence — measured `mean_volume: -91.0 dB` **and** `max_volume: -91.0 dB`, over the whole file
and over the shot-03 region taken alone. **"There is no track" and "the track is empty" are
different**, and this one is the second.

⚠️ **So the music does not mix in underneath. The music is the whole of this file's sound.**

## ⚠️ And this work declares speech — which the render does not carry

⚠️ **Shot 03 is the one shot of the five that speaks, and it speaks Japanese**
(`specs/video/shot-03-matter.md`, `bible.language: Japanese`). The render's track is empty.
**So the speech the specification declares is not in any file in this directory.**

⚠️ **This is a hole, and it is written down rather than filled.** Two consequences:

- **The `+` file is not "the work with its sound."** It is **the picture with music on it.** The voice, if it ever arrives, has to be **mixed under** this music — not replaced
  by it. Replacing the track again would delete it.
- **A person watching these files hears music and no voice**, in a shot whose whole design is
  that she is speaking. **Whether that is acceptable for the version shown to people is the
  author's decision, not this record's.**

## ⚠️ The work's Negative says `no background music`

⚠️ **Read the clause's jurisdiction before reading this file as a contradiction.**

`bible.negative_base` carries the foundation's three clauses, `no background music` among them,
and it reaches the generator through §18's `Negative Prompt` in **all ten specification files**.
**That clause binds the generator.** What the author does to the picture afterwards is a
different act by a different agent, and the clause does not reach it.

⚠️ **But the clause is not waived here either.** `hitosara` declares
`base_negatives_waived: ["no background music"]` — **this work does not**, and the author's
decision of 2026-09-18 was that only the grandfather clause's *existing* works are exempt.
**So the difference between the two works is real and is not an oversight:**

| | generator's Negative | the render |
|---|---|---|
| `hitosara` | **waived** — the clause does not reach it | music added; **published** |
| `promo-chinatsu` | **in force** — ten files carry it | music added; **adopted, unpublished** |

⚠️ **Whoever shows this file to people is choosing the second row's second column.**
Write down that they chose it. **This record does not decide it for them.**

## ⚠️ The music record (required for any version shown to people)

⚠️ **Take this table along with the file.** Not writing the source is **the same as not meeting
the license conditions.** The pack, its license, and the contradiction inside it are documented
in `projects/hitosara/renders/README.md` — ⚠️ **it is not repeated here, and the same warning
applies**: every track in the pack declares CC0 in `catalog.json` while its own ID3 `comment`
claims `made with suno`. **If you publish, the risk is the author's.**

| | |
|---|---|
| Track | **`bamboo-shadow-waltz`** (adopted). ⚠️ **The other three were built to the same loudness and not adopted** — if one of them is ever adopted instead, this table must move with it |
| Source | `catalog.json` of **open-lofi** (`https://github.com/btahir/open-lofi`) |
| Pack declaration | **`"license": "CC0-1.0"`** (one for the whole pack, 166 tracks) |
| Cut position | **0 → 28.028000 seconds** (cut to the work's duration). **Fade out from 24.028 s**, 0.3-second fade in |
| Measured loudness | **−16.0 LUFS** (the same target `hitosara+soft-gold-sky.mp4` used) |
| Measurements per candidate | `音源調査/_bgm-audition/cuesheet-chinatsu.json` |
| The script that made them | `音源調査/_bgm-audition/build_chinatsu.py` |
| The eight-candidate audition | `音源調査/_bgm-audition/audition-chinatsu-28s.m4a` (238.2 s) |
| Breakdown of the measurements | **Read `HISTORY.md`** — ⚠️ **not written here** (they are past measured values) |

⚠️ **Eight were auditioned, and one was adopted.** The measurements say what each one **is** —
all eight sit at the same loudness, and what separates them is **brightness and mode** (spectral
centroid 317 to 1477, against a pack median of 1372). ⚠️ **They do not say which one belongs to
this work**, and this record does not pretend otherwise: **the author listened and kept
`bamboo-shadow-waltz`.**

## ⚠️ Neither the emptiness nor the fullness of this directory is reported

Same as `projects/hitosara/renders/` — **no check reads `renders/`.** ⚠️ **A check that does not
report looks the same as a check that passed.** So this table is a record **only a person can
read**, and it is the reason the silent track had to be measured by hand above.

⚠️ **The name rule is broken here too.** `renders/<name>.mp4` is supposed to be claimed by
`timeline/<name>.yaml`, and **this work has no `timeline/` directory at all.** The hole is
named, not fixed — the same hole as hitosara's.
