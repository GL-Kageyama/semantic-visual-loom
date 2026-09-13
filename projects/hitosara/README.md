<!-- i18n-version: 1.0.0 | canonical: projects/hitosara/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# `hitosara/` — until a single dish is made

From flour, water, salt, and time, until the bread becomes a single dish. **10 shots.**
A work completely independent of ukebi, and **it is placed here to show everything this foundation reads.**

> **A story becomes a run of shots.**

---

# ⚠️ Only §18 is fed into the generator

`specs/video/shot-XX-*.md` has §1–20. **Of that, only §18 is handed to the model.**

| | | |
|---|---|---|
| **§1–17** | **Groundwork.** The 7 slots of §18 are derived from here | **Not fed** |
| **§18** | `# 18. WAN 3.0 PROMPT MAPPING` — **7 slots. It is English** | **Fed** |
| **§19–20** | Our own record (§19 is the resolved values, §20 is the reflection and the next generation) | **Not fed** |

**Range**: from `# 18. WAN 3.0 PROMPT MAPPING` to the end of the body of `## Style Motion`.

⚠️ **The 7 slots are fed separately.** `Master` / `Visual` / `Motion` / `Camera` / `Audio` /
`Negative` / `Style Motion`. "**Being separated is itself the point**, so do not mix them"
(`references/video-spec.md`).
⚠️ **If the destination has only one field, join them.**
⚠️ **Put that shot's duration into `{DURATION}`** (in this work, 2s–8s).

### ⚠️ §19 and §20 must not be fed

§19 is **our own ledger**, listing `Instance ID` and `Generation Date`.
§20 contains "**the concerns to be confirmed by this generation**" — ⚠️ for example
**"`Lettering may appear on the sacks.`"**. **It would mean putting the name of the failure inside the prompt.**

⚠️ **The §12 heading also has Japanese in it** (`## MUST NOT (prohibitions for this one shot, …)`).
**There is no Japanese inside §18** — do not mix them. **The strings handed over are English.**

---

# ⚠️ The image specifications do not have §18

`specs/image/shot-XX-*.md` does not have §1–20. **Two paragraphs inside one section** are canonical.

| | |
|---|---|
| **1st paragraph** | **`Prompt`** — **fed into `chatgpt-image-2.5` as it is** |
| **2nd paragraph** | **`Negative`** — joined to the 1st paragraph by **a single blank line** |

⚠️ **That blank line is there in the record as it is** (decision A). **Feed it together with the blank line.**
⚠️ **Do not keep a copy of the joined string** — **copies contradict.**
⚠️ **Not having §1–20 is a matter of kind, not a matter of mode.** Every shot has two paths.

---

# ⚠️ The order to run them in

**10 images → look at all of them → 10 videos.**
If the first frame is not what you intended, piling 10 videos on top of it becomes **10 times the waste.**

- **Images are handed to the video as attachments (reference images). Not as the first frame.**
  Make it the first frame and **that shot's change will not occur on screen**
  ——the change is already finished inside the image.
- **The place for generated output is `media/`.** The foundation does not read here (`media/README.md`).
- **Record what comes back in `takes/`. Placing something is not recording it.**
- ⚠️ **`takes/` is read by `L25`. `media/` is read by no one.**
  So **a discrepancy between the actual file and the record is not fired by the machine**——`L25` reports it as prose in a note.
  **What is in `media/` with no record will not be found unless you go looking.**
  ⚠️ **The reverse direction also exists**——**the file a record claims no longer exists**.
  Since `file` is a claim and not a proof, **even if it disappears the machine stays silent.**

---

# Layout

| | |
|---|---|
| `bible.yaml` | World, fundamental laws, visual language. **The style is `luminous-anime`** (the card has `Motion character`) |
| `ledger.yaml` | The ledger is **one** (continuity + disclosure—people, places, props; the position where the oven opens, the position where the bread breaks) |
| `shots/` | 10 files. `role` / `mode` / `beats` / `reference_set` / `attached` / `disclosure_state` / `motion` |
| `specs/video/` | 10 files. Has §1–20. **Only §18 is fed** |
| `specs/image/` | 10 files. Does not have §1–20. **Two paragraphs** are canonical |
| `media/` | Where generated output goes. **The foundation does not read it.** ⚠️ **A difference between the actual file and the record is not fired by the machine** |
| `takes/` | The record of takes. **Placing alone does not make a record.** `L25` reads it |
| `renders/` | **What editing produced (the work).** Samples are `media/`, the work is here——⚠️ **do not mix them** |
| `timeline/` | The record of editing. **Not yet opened** |

⚠️ **The check is pre-flight verification only.** `python3 engine/ledger/check.py projects/hitosara`.
**Zero violations is not "correct"**——read the notes and the range that is not checked.
