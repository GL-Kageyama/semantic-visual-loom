<!-- i18n-version: 1.0.0 | canonical: projects/ukebi/README.md | translated: 2026-11-15 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# Ukebi — projects/ukebi

The revised ten episodes are filmed here. The old version is in `_archive/`.

## Layout

| Path | What | State |
|---|---|---|
| `ukebi-v3/` | The new work for the revised ten episodes (195 shots) | README only; before breakdown |
| `_archive/ukebi-v2/` | The old thirty-shot migration (30 s × 30 = 15 min) | Old version; names, disclosure and specs predate the revision |
| `_archive/ukebi-video-00…09/` | The old raw §1–20 specs (30) | Old version; read-only |
| `_archive/ukebi-video-00-series/` | The old twelve-segment constants | Old version; read-only |

A run over the parent does not read `_archive/` (`check.py` reads `shots/` one level deep; it does not walk into a sibling work). The `spec:` paths of `ukebi-v2` point inside the work, so the move does not break them.

## Source of truth

- The story, the ledger and the shot tables are in `soul-voice-teller/examples/works/novels/ukebi-anime/`.
- The twenty-six adopted images are in `distill-essence-engine/examples/works/novels/ukebi-anime/`.
- This repository moves those two into sVL shot records.

## Why V2 is not used as it stands

- V2 is a migration of the old thirty specs. Thirty shots × 30 s = 15 minutes. The revised ten episodes are 195 shots, about 71 minutes.
- V2 carries the old names (幸恵, 結城文, 折笠千代, 早瀬甚吾, 篠宮). The revision uses サチ, フミ, トワ, ナギ, 花.
- V2 reveals the name at ch08. The revision gives it in episode 10.
- V2 does not contain the revised ep1 / ep3 / ep10 or the twenty-six images.

## Next

See [`ukebi-v3/README.md`](ukebi-v3/README.md). A one-episode pilot first.
