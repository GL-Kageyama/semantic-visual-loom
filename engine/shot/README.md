<!-- i18n-version: 1.0.0 | canonical: engine/shot/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# engine/shot/ — Printing the Specification Skeleton

**Print the lines of a shot's specification that can be derived**—from the record,
the ledger, and the bible. **Not a byte is written.** Not to `projects/`, not to a
specification, not anywhere.

```bash
python3 engine/shot/print_spec.py projects/<project>              # every shot
python3 engine/shot/print_spec.py projects/<project> --shot <id>  # one shot
```

⚠️ **Pasting what it prints is the author's act.** The tool only shows what is forced.

## What It Prints

**Six lines**—against **166** non-blank lines in one demo specification
(`hitosara-ch01-seg04`).

| Line | Derived from | Copying it silences |
| --- | --- | --- |
| §1 `Aspect` | `bible.constants.video.aspect` | `L26` |
| §1 `Resolution` | `bible.constants.video.resolution` | `L26` |
| §1 `Frame Rate` | `bible.constants.video.frame_rate` | `L26` |
| §1 `Orientation` | `bible.constants.video.orientation` | `L26` |
| §1 `Duration` | `shot.duration` | `L23` |
| §19 `Instance ID` | `shot.shot` | `L13` |

⚠️ **The value of this tool is not that it fills lines in.** It is that it **names, per
line, which check goes silent if you hand-copy that line.** A line copied by hand is a
line that **nobody will report when its source moves**—which is why `L23`, `L26` and
`L13` exist for exactly these lines.

⚠️ **A specification is not assembled from these six lines.** They are the part where
**the machine already knows the answer.** The rest is the work.

## ⚠️ What It Does Not Derive

**§2 WORLD, §3–§5, §7–§13, §14 DIALOGUE, §15–§17, §18 (the seven slots), §20**—all of
these the author writes. `print_spec.py` names this list on every run, because
**a number is only as wide as what was counted.**

### §6 REFERENCES — the shape is not stable

⚠️ **This is measured, not assumed.** The two structured works write §6 differently.

| | `projects/hitosara` | `projects/ukebi/ukebi-v2` |
| --- | --- | --- |
| syntax | ``- REF_KEY: `value` (HIGH)`` | ``- `REF_KEY` — `value` · `HIGH`。`` |
| keys | 6: CHARACTER / LOCATION / GEOGRAPHY / STYLE / FORMAT / SOURCE | 5: CHARACTER / STYLE / FORMAT / SOURCE / BIBLE |
| value vocabulary | card names (`luminous-anime`) | paths (`references/styles/soft-cel-anime.md`) |

⚠️ **A field whose shape is not stable cannot be derived.** Derive it and the tool
**lies once per work**—it would print a confident wrong value, in the same format,
for the same line, in both works. So §6 is not parsed. The holes are recorded below.

⚠️ **One key is an exception: `REF_STYLE`** (`L31`, `check_style_reference`).
**It is read, because it can be read without a guess**—the three spellings above
are matched by one pattern, and **the two vocabularies (card name, path) are folded
into one name before comparing** (take the last path segment, drop `.md`).
**So `L31` does not decide which vocabulary is right—it makes both comparable.**
⚠️ **The other §6 keys are still not read**—the rule above holds for them.

## The Home of the Work Constants

`bible.constants.video`—`aspect` / `resolution` / `frame_rate` / `orientation`.

⚠️ **`duration` is not there.** Length is a **dependent variable**: its home is
`shot.duration` and its reader is `L23`. Putting it here would mean **two layers
reporting the same defect under separate codes.**

⚠️ **This is not a new field.** `projects/ukebi/ukebi-video-00-series/series-constants.md`
held §1's constants **by hand for all 12 takes**, and `schemas/bible.schema.json` names
`bible` as its successor. The home was already there——**and nothing read it.**

⚠️ **The work constants were copied by hand into three places**: §1, §19's `Output:`
line, and (in Ukebi) `series-constants.md`. And the copies are already drifting.

## What Reads It

- **`L26`** — `bible.constants.video` against §1's four lines
- **`engine/shot/print_spec.py`** — this tool

⚠️ **`L26` reports nothing today**—**160** comparisons (40 specifications × 4 lines,
across the two structured works), **0** disagreements—and its note says so.
⚠️ **Reporting nothing is not the same as being unnecessary.** The failure mode it
guards is **already present in this repository** (§19's `Output:` line is spelled
differently in 10/10 specifications), and `L23` is also kept while agreeing **40/40**.

## It Decides Nothing

⚠️ **This tool writes nothing and decides nothing.** Where the derived value and the
specification on disk disagree, it prints **both** and stops. **Which one is right is
the author's judgment**—the same position `L25` takes.

## What Is Still Missing

**Recorded, not fixed**—that is this repository's practice.

1. **§19's `Output:` is a third hand-copy.** It is spelled differently in **10/10**
   specifications (`1920×1080` / `landscape` against §1's `1920x1080` / `Landscape`).
   The values agree; the spelling does not. **So `L26` does not read it**—reading it
   would produce **10 false positives.** Whether to normalize and read it, split it into
   four fields, or leave it as prose is **undecided.**
2. **The `<seconds>` inside §19's `Instance ID` is checked by nobody.** `L13` strips the
   trailing `-<seconds>s-<take>` before comparing, so the copy of the length inside the
   identifier is compared against nothing.
3. **The four prose constants in `bible.constants` are read by nobody** (`根本律`,
   `光源`, `カメラ`, `様式変数`). How to make them machine-readable is **undecided.**
4. **§6's `REF_CHARACTER` cannot be derived.** §6 cites it in **9/10** shots, while
   `reference_set` carries `BAKER.sheet` in only **4/10**—the two sides disagree about
   what "the character is attached" means.
5. **seg04's `REF_LOCATION` override is recorded nowhere.** All five `KITCHEN/朝` shots
   carry the **same location references** (`KITCHEN.base` + `KITCHEN.geography`), yet §6
   uses the `-morning` board for four of them and the bare `hitosara-kitchen-board` for
   seg04. Deriving from `(place, time)` gives **9/10**, and **the tenth is
   indistinguishable from the record.** ⚠️ This is the clearest hole here: the choice
   exists only in §6 itself.
6. **seg10's §6 cites `hitosara-kitchen-geography`** while its `reference_set` declares
   no geography at all (`TABLE.base`) —§6 says "LOW: the room is only suggested." It is
   the only shot whose §6 geography citation has no counterpart in `reference_set`.
7. **`locations.KITCHEN.states.朝.board` is referenced by no shot's `reference_set`,**
   yet §6 uses its value in **four** shots. (`昼` is referenced by seg06, `明け方` by
   seg07/08, `MILL.朝` by seg01—only `KITCHEN.朝` is unreferenced.)

⚠️ **Items 4–7 are not defects in the work.** They are places where **the record does
not know what the specification does.** The fix, if there is one, is to give the choice
a home—**not to make the tool guess.**
