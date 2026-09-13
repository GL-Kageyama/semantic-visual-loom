<!-- i18n-version: 1.0.0 | canonical: projects/hitosara/media/README.md | translated: 2026-09-14 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# `media/` — where the author drops generated output

**The foundation does not read here.** It is the place to put generated output (images and video), and
neither `check.py` nor `semantic.py` opens this directory.

## ⚠️ Put both images and video **here**

⚠️ **Do not put video in `takes/`.** `takes/` is the place for **records** (`*.yaml`)——
**do not mix things and records in the same place.** The actual file goes in `media/`, the record goes in `takes/`.

⚠️ **Do not put edited things (joined things) here.** This is the place for **samples**, and
not the place for **works**——what is joined is `../renders/`.
⚠️ **Mix them and a missing sample can no longer be told apart from an existing work**——
**works wearing the face of "a take with no record"** will line up here.

⚠️ **`.mp4` and `.png` are tracked by Git LFS** (`.gitattributes`).

```gitattributes
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.png filter=lfs diff=lfs merge=lfs -text
```

⚠️ **Placing alone does not make it LFS.** Only once you `git add` does it become
**a 133-byte pointer**, and the entity goes into `.git/lfs/objects/`.
**A file left untracked does not exist inside the repository**——
**people who clone will not see it, and if it disappears no one will notice.**

⚠️ **The entity goes up together at push time.** If only the pointer goes up,
**people who clone cannot have the video.**

⚠️ **The second column of `git lfs ls-files` is not the presence or absence of the local entity.**
`*` means "a complete object" and `-` means "**an LFS pointer**" (`git lfs ls-files --help`)——
in other words, it is a mark that **the copy on disk is a pointer (or absent)**, and
**it does not say whether the entity is in `.git/lfs/objects/`.**
⚠️ **In fact, there are three files that are `-` yet have their entity present** (the old names `2__` `5__` `6__`——
**the objects are local, only the copies on disk are missing**).
**If you want to confirm an entity, open `.git/lfs/objects/<first 1–2 chars of the oid>/<3–4 chars>/<oid>`.**

⚠️ **A state where the pointer cannot be resolved actually occurred** (and was once recorded).
`02__20260913-….mp4` was committed as **a 133-byte pointer**,
**and that file disappeared from the working tree.**
⚠️ **But the entity is in the local LFS**——`0c119d5c…` (10,456,290 bytes).
ffprobe reads it as `1920x1080 / 60 frames / 2.000s`.
⚠️ **Writing "the entity is nowhere" was an error** (`HISTORY.md`, 0.17.1).
⚠️ **Whether it is on the remote cannot be measured from here.**

⚠️ **File names start with `NN__`** (`01__` … `10__`). The name is a clue for pulling up the record.
⚠️ **How to read it——the leading digits are the shot number——was confirmed by the author
pointing at one file by shot number** (`6__78bbaadd-….mp4` = shot 6, 2026-09-13).
**It is not a guess but a reading supported by a single measurement.**
⚠️ **This spelling moves.** Do not count and write the names that exist now in this text——**write them and they will contradict.**

⚠️ **Generated output is large binaries.** Whether to place them is the author's decision.
**This repository does not run generation** (there is no API key in the environment).
The author runs it by hand, and **records** what comes back in `takes/`——
**placing something is not recording it.**

⚠️ **That things exist in this directory is not a report of any kind.**
The emptiness of `takes/` is reported. **Neither the emptiness here nor the fullness here is reported.**
**That a file exists is not that the shot passed.**

## ⚠️ `L25` keeps this declaration

`L25` **does not open and does not `stat`** the file `take.file` claims——
so **even if the contents of this directory and the records in `takes/` contradict, the machine does not fire.**

⚠️ **That discrepancy has two directions.** **① It is here, but there is no record.**
**② A record claims it, but it is not here.**——**② actually happened.**
A take claiming `02__20260913-….mp4` is in `takes/`, but **that file no longer exists.**
`6__78bbaadd-….mp4` is the same——**the take that claims it exists, and the file does not.**
⚠️ **In both cases the entity is in the local LFS**——**what disappeared is the name, not the thing.**
⚠️ **So the number of takes and the number of mp4s here do not match.** **The machine fires for neither direction.**
⚠️ **Do not write the counts in this text.** The counts move——**write them and they will contradict.**

⚠️ **To close this hole with a check, you would have to change this declaration first ("the foundation does not open this").**
**Whether to close it is undecided**——make `media/` readable and a discrepancy between record and actual file fires by machine.
But then **the foundation becomes a thing that peeks into the place where binaries live.**

⚠️ **`*.md` is not read.** So this text is not counted as material.
