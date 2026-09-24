<!-- i18n-version: 1.0.0 | canonical: projects/migenzo/media/README.md | translated: 2026-09-25 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# `media/` — where the author drops generated output

**The foundation does not read here.** This is the place for generated output (images and video), and
neither `check.py` nor `semantic.py` opens this directory.

## ⚠️ The samples moved here on 2026-09-25

Until 2026-09-25 the generated images sat in `specs/image/` and the generated video in `specs/video/`,
each beside its own specification.
**`take.file` names a file inside `media/`** (`schemas/take.schema.json`)——so the samples were moved
to the one place the records point at.
⚠️ **The specifications did not move.** `specs/` holds the specifications, and it is a different place
from here. ⚠️ **The two are told apart by what they are, not by where they sit.**

## ⚠️ Put both images and video **here**

⚠️ **Do not put video in `takes/`.** `takes/` is the place for **records** (`*.yaml`)——
**do not mix things and records in the same place.** The actual file goes here, the record goes in `takes/`.

⚠️ **Do not put joined things here.** This is the place for **samples**, and not the place for **works**
——what is joined is `../renders/`.
⚠️ **Mix them and a missing sample can no longer be told apart from an existing work.**

## ⚠️ Two files are **not** here

`specs/image/生成時参照イラスト/`（2枚）——**they are the input to a generation.**
⚠️ **They are not samples of this work's shots**; they are sheets made elsewhere (in
`distill-essence-engine`) and handed to the generator as references.
⛔ **Whether they belong here is undecided**——**this text does not decide it.**

## ⚠️ Names

⚠️ **`NN_MM_` at the head is the shot and the segment**——`06_01_…` is the file of the one whose §19
says `Segment ID: 06-1` (read by putting the names against §19), and after that comes whatever the
generator returned as its own name.
⚠️ **This spelling moves.** Do not count and write the names that exist now in this text——
**write them and they will contradict.**

## ⚠️ Git LFS

⚠️ **`.mp4` and `.png` are tracked by Git LFS** (`.gitattributes`).

```gitattributes
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.png filter=lfs diff=lfs merge=lfs -text
```

⚠️ **Placing alone does not make it LFS.** Only once you `git add` does it become **a pointer**,
and the entity goes into `.git/lfs/objects/`.
**A file left untracked does not exist inside the repository**——
**people who clone will not see it, and if it disappears no one will notice.**
⚠️ **The entity goes up together at push time.**

⚠️ **The second column of `git lfs ls-files` is not the presence or absence of the local entity.**
`*` means "a complete object" and `-` means "**an LFS pointer**"——in other words it is a mark that
**the copy on disk is a pointer (or absent)**, and **it does not say whether the entity is in
`.git/lfs/objects/`.** ⚠️ **If you want to confirm an entity, open
`.git/lfs/objects/<first 1–2 chars of the oid>/<3–4 chars>/<oid>`.**

## ⚠️ `L25` keeps this declaration

`L25` **does not open and does not `stat`** the file `take.file` claims——
so **even if the contents of this directory and the records in `takes/` contradict, the machine does
not fire.**

⚠️ **That discrepancy has two directions.** **① It is here, but there is no record.**
**② A record claims it, but it is not here.** ⚠️ **The machine fires for neither direction**——
because `L25` does not open `media/`.
⚠️ **To close this hole with a check, you would have to change this declaration first** ("the
foundation does not open this"). **Whether to close it is undecided.**

⚠️ **That things exist in this directory is not a report of any kind.**
**That a file exists is not that the shot passed.**
⚠️ **Do not write the counts in this text.** The counts move——**write them and they will contradict.**

⚠️ **`*.md` is not read.** So this text is not counted as material.
