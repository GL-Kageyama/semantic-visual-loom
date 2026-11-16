<!-- i18n-version: 1.0.0 | canonical: projects/ukebi/ukebi-v3/README.md | translated: 2026-11-17 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# Ukebi V3 — filming the revised ten episodes

The successor to `_archive/ukebi-v2`. The old version stays. This work now has `bible.yaml` / `ledger.yaml` / `shots/`. **All ten episodes are recorded: 28 + 27 + 34 + 22 + 27 + 25 + 27 + 25 + 21 + 36 = 272 shot records and 272 image specs. Their video specs are deferred.** Each shot's spec and outputs live in one folder: `specs/image/epNN/<the same name as the spec>/`. Outputs keep their own names—the folder carries the shot, and spec and folder sort together by number. The whole picture is in [`進捗表.md`](進捗表.md), the record-derived one-pager is [`概要.md`](概要.md), and the per-episode sheets are [`概要/ep03.md`](概要/ep03.md) through [`概要/ep10.md`](概要/ep10.md).

## What is made

- Move the revised ten episodes into sVL shot records.
- The design rows total **222** (S195 + M27); the cuts total **272** provisional shots—ep1 27 / ep2 34 / ep3 28 / ep4 22 / ep5 27 / ep6 25 / ep7 27 / ep8 25 / ep9 21 / ep10 36.
- Do not cut by episode. Cut by shot. **One shot, one change.**

## Source of truth

| What | Where |
|---|---|
| Story, ledger | `soul-voice-teller/examples/works/novels/ukebi-anime/台帳/`, `構想/design.md` |
| Revised prose | `.../草稿/draft_*.md` |
| Shot tables | `.../草稿/ショット表_*.md` (ep2 is `第2話_送る_試作.md`) |
| Thirty-one images | `distill-essence-engine/examples/works/novels/ukebi-anime/` (31/31 adopted) |
| Crossing board (corrected) | `reference/踏切/board.md` — re-baked here; the old board contradicts the ledger (pavement, arms, lamp) |
| Old version | `../_archive/ukebi-v2/`, `../_archive/ukebi-video-*` |

⚠️ The prose and the shot tables live outside this repository. A clone alone cannot read them. The work's records live here; the source stays outside.

## Inheriting the original prompt materials

**The prompts are not invented here.** The look was decided in `distill-essence-engine/examples/works/novels/ukebi-anime/`—the crossing art board, the episode-3 scene board, the character and prop sheets, and the `_shared/` blocks (fire, figures, common, the adoption table). Their `prompt.md` Merged prompts and `input.md` content are the source; the image specs under `specs/image/` inherit their palette, light, negatives and vocabulary. **They do not start from zero.**

⚠️ **Measured.** A 332-word prompt composed only from the eight fields lost the crossing's white-black arms, the off-frame source, the palette and the "painted background" anchor; the image came back as a warm, photoreal night. A 736-word prompt that inherited the existing art board's constants recovered them. **The default is inheritance.**

⚠️ `distill-essence-engine` is read-only: read its cards and examples, write the record here. The source lives outside this repository, so a clone cannot read it; the paths are recorded for the author.

## Holes to close before the pilot

Measured by running `check.py` on `_archive/ukebi-v2`: **157 violations / 60 notes**.

- L16 `motion` 30 · L17 `Style Motion` 30 · L21 `no background music` 30 · L38 staging-summary band 30 · L6 `attached` 30.
- L14 5 (undeclared irreversible changes) · L27 `bible.language` 1 · S0 `jsonschema` 1.
- Notes: L48/L50 no `dramaturgy`, L51 no `population`, L52 no `body_parts`, L18 no `key_image`.
- `check.py --self-test`: 513 of 513 with `jsonschema` present; without it, the S0 examples cannot run. `check_i18n.py --self-test`: 17/17.

V3 settled that shape at episode 3. The same hole should not be made 272 times.

## Decisions

1. **Pilot**: ep3. Its 28 records are written.
2. **Route**: WAN 3.0 for video (deferred), `CHATGPT IMAGE 2.5` for `key_image`. V2 is WAN 3.0 at 30 s; the revised shots are shorter.
3. `bible.language: Japanese`. `population`, `body_parts` and `cast` are written per shot.
4. **A map for the thirty-one images**: make `REF_CHARACTER` / `REF_HANA` / `OKURIBI.sheet` point at real files. Attach them only where the person or space is present.
5. **The ep10 scene board contradicts the revision.** The old board says "no ledger, no scale, no seal" and "his hands are empty." The revised ep10 has the ledger in his arms and shows the first page's fold before the question. Re-bake it or add a new board.

## Order

1. ✅ Write `bible.yaml` and `ledger.yaml` from the revision. Names: サチ, フミ, トワ, ナギ, 花. Disclosure: `構想/design.md`'s table.
2. ✅ `breakdown` all ten episodes into `shots/` (272 records).
3. ✅ Write the image specs for all 272 shots. ⏸ §1–20 and §18's seven slots are deferred; `L11` and `L14` name the empty video side. ⚠️ Nine ep9 memory shots drop `no rain` on purpose; `L21` reports them as a declared hold.
4. ◐ `reference_set` / `attached` are written per shot. `forbidden_set` is not yet derived.
5. Next: the video specs for all 272 shots, and the takes.

## Do not touch

- `../_archive/` is a record. Do not fix it.
- `distill-essence-engine`'s cards are read-only. Do not write them.
- Do not carry the old names (幸恵, 結城文, 折笠千代, 早瀬甚吾, 篠宮) into v3.
