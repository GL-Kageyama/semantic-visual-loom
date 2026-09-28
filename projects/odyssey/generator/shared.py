"""Invariant chunks for the odyssey specs — extracted from the three written specs, not retyped.

Why extraction: L10 compares only the §18 `Negative Prompt` clause set at the four declared
disclosure change points, and all four are declared `negative: covered`. So that block must be
byte-identical across all 34 specs. Retyping it 31 times is 31 chances to break L10 silently.
Reading it from an existing spec makes the invariant a construction guarantee.
"""
import re
from pathlib import Path

SPECS = Path(__file__).resolve().parent.parent / "specs" / "video"
SOURCES = ["odyssey-s01.md", "odyssey-s03.md", "odyssey-s05.md"]


def _read(name):
    return (SPECS / name).read_text(encoding="utf-8")


def slot(text, name):
    """Body of a `## <name>` block inside §18, up to the next `## `. Empty string if absent."""
    m = re.search(r"^## " + re.escape(name) + r"\s*\n(.*?)(?=\n## |\n---\s*\n# |\Z)", text, re.S | re.M)
    return m.group(1).strip("\n") if m else None


def section(text, num, title):
    m = re.search(r"^# " + str(num) + r"\. " + re.escape(title) + r"\s*\n(.*?)(?=\n# |\Z)", text, re.S | re.M)
    return m.group(1) if m else None


def consistency(extractor, label):
    """Verify a chunk is byte-identical across every written spec."""
    vals = {}
    for s in SOURCES:
        t = _read(s)
        v = extractor(t)
        if v is None:
            raise SystemExit("MISSING: %s in %s" % (label, s))
        vals.setdefault(v, []).append(s)
    if len(vals) != 1:
        for v, where in vals.items():
            print("--- variant (%s): %s" % (",".join(where), repr(v[:120])))
        raise SystemExit("NOT IDENTICAL: %s has %d variants" % (label, len(vals)))
    return next(iter(vals))


NEGATIVE = consistency(lambda t: slot(t, "Negative Prompt"), "§18 Negative Prompt")
STYLE_MOTION = consistency(lambda t: slot(t, "Style Motion"), "§18 Style Motion")

# §1's five constant lines (L26)
# Duration varies by shot (L23) — the other four are the work constants (L26).
CONSTANT_LINES = consistency(
    lambda t: "\n".join(l for l in section(t, 1, "VIDEO").splitlines()
                        if re.match(r"^- (Aspect|Resolution|Frame Rate|Orientation):", l)),
    "§1 constants")
DURATION_LINE = lambda t: re.search(r"^- Duration: `([0-9.]+)s`", section(t, 1, "VIDEO"), re.M).group(1)

# §18 preamble's shared head: everything before the first ⚠️ paragraph that is per-shot.
PREAMBLE_HEAD = consistency(
    lambda t: section(t, 18, "SEEDANCE 2.5 PROMPT MAPPING").split("⚠️ ⛔")[0].rstrip("\n"),
    "§18 preamble head")

# The four invariant §16 MUST NOT items that carry the floor's negatives.
def floor_items(t):
    keep = []
    for l in section(t, 16, "CONSTRAINTS").splitlines():
        if re.match(r"^- No (music of any kind|on-screen subtitles|watermark|uniform pacing)", l):
            keep.append(l)
    return "\n".join(keep)

FLOOR_ITEMS = consistency(floor_items, "§16 floor items")

# §6's route notes (the paragraphs that do not change per shot)
def route_notes(t):
    body = section(t, 6, "REFERENCES")
    keep = [l for l in body.splitlines()
            if l.startswith("- ⚠️ **REF_BOARD") or l.startswith("- ⚠️ **この34本は")
            or l.startswith("- ⚠️ **この経路は、実在の顔") or l.startswith("- ⚠️ **そしてこの選択の代償")
            or l.startswith("- ⚠️ **§1–17 は下敷き")]
    return "\n".join(keep)

ROUTE_NOTES = consistency(route_notes, "§6 route notes")

if __name__ == "__main__":
    for name, v in [("NEGATIVE", NEGATIVE), ("STYLE_MOTION", STYLE_MOTION),
                    ("CONSTANT_LINES", CONSTANT_LINES), ("PREAMBLE_HEAD", PREAMBLE_HEAD),
                    ("FLOOR_ITEMS", FLOOR_ITEMS), ("ROUTE_NOTES", ROUTE_NOTES)]:
        print("%-16s %5d chars  %3d lines" % (name, len(v), v.count("\n") + 1))
    print()
    print("CONSTANT_LINES:"); print(CONSTANT_LINES)
    print(); print("FLOOR_ITEMS:"); print(FLOOR_ITEMS)
    print(); print("NEGATIVE clauses:", len([c for c in NEGATIVE.split(",") if c.strip()]))
