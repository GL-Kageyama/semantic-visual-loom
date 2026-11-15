<!-- i18n-version: 1.0.0 | canonical: projects/ukebi/ukebi-v3/README.md | translated: 2026-11-15 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# Ukebi V3 — filming the revised ten episodes

The successor to `_archive/ukebi-v2`. The old version stays. This work does not yet have `bible.yaml` / `ledger.yaml` / `shots/`. It is before breakdown. The ten episode frames are in [`episodes/`](episodes/index.md); they are frames, not shot records.

## What is made

- Move the revised ten episodes into sVL shot records.
- The shot tables total **195**—ep1 21 / ep2 trial 18 / ep3 16 / ep4 18 / ep5 17 / ep6 22 / ep7 18 / ep8 16 / ep9 14 / ep10 35.
- Do not cut by episode. Cut by shot. **One shot, one change.**

## Source of truth

| What | Where |
|---|---|
| Story, ledger | `soul-voice-teller/examples/works/novels/ukebi-anime/台帳/`, `構想/design.md` |
| Revised prose | `.../草稿/draft_*.md` |
| Shot tables | `.../草稿/ショット表_*.md` (ep2 is `第2話_送る_試作.md`) |
| Twenty-six images | `distill-essence-engine/examples/works/novels/ukebi-anime/` (26/26 adopted) |
| Old version | `../_archive/ukebi-v2/`, `../_archive/ukebi-video-*` |

⚠️ The prose and the shot tables live outside this repository. A clone alone cannot read them. The work's records live here; the source stays outside.

## Holes to close before the pilot

Measured by running `check.py` on `_archive/ukebi-v2`: **157 violations / 60 notes**.

- L16 `motion` 30 · L17 `Style Motion` 30 · L21 `no background music` 30 · L38 staging-summary band 30 · L6 `attached` 30.
- L14 5 (undeclared irreversible changes) · L27 `bible.language` 1 · S0 `jsonschema` 1.
- Notes: L48/L50 no `dramaturgy`, L51 no `population`, L52 no `body_parts`, L18 no `key_image`.
- `check.py --self-test`: 510 of 515 (five fail without `jsonschema`). `check_i18n.py --self-test`: 17/17.

V3 settles that shape before writing 195 shots. The same hole should not be made 195 times.

## Decisions

1. **Pilot**: ep1 (opening, 21 shots, 5 min) or ep3 (the largest revision, 16 shots, 7 min).
2. **Route**: WAN 3.0 / MINIMAX H3 / SEEDANCE 2.5. V2 is WAN 3.0 at 30 s; the revised shots are shorter.
3. `bible.language: ja`. Write `population` and `body_parts` per shot.
4. **A map for the twenty-six images**: make `REF_CHARACTER` / `REF_HANA` / `OKURIBI.sheet` point at real files. Attach them only where the person or space is present.
5. **The ep10 scene board contradicts the revision.** The old board says "no ledger, no scale, no seal" and "his hands are empty." The revised ep10 has the ledger in his arms and shows the first page's fold before the question. Re-bake it or add a new board.

## Order

1. Write `bible.yaml` and `ledger.yaml` from the revision. Names: サチ, フミ, トワ, ナギ, 花. Disclosure: `構想/design.md`'s table (ep4 花 takes the seat / ep5 first line / ep7 the seal / ep10 the name).
2. `breakdown` the pilot episode into `shots/`.
3. `design` §1–20 and §18's seven slots. Fill the L16 / L17 / L21 / L38 / L6 shape first.
4. `ledger` derives `reference_set` / `forbidden_set`. Point at the twenty-six real files.
5. Only after `check.py` reaches zero violations (or records the intended waivers): images 10 → look at all → video.

## Do not touch

- `../_archive/` is a record. Do not fix it.
- `distill-essence-engine`'s cards are read-only. Do not write them.
- Do not carry the old names (幸恵, 結城文, 折笠千代, 早瀬甚吾, 篠宮) into v3.
