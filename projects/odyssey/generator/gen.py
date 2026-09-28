# -*- coding: utf-8 -*-
"""Render content modules into spec files, filling the beat table from the shot records.

Usage: python3 gen.py s02 s04 ...     (no args: every content module present)
"""
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
ROOT = pathlib.Path(__file__).resolve().parents[3]
ROSTER = json.loads((HERE / "roster.json").read_text(encoding="utf-8"))

# ⛔ **`ROOT` が本当にリポジトリの根を指しているかを、書く前に確かめる。**
#    ⚠️ **2026-09-29 の実測**: この1行を `parents[2]` と誤って書いたため、
#    `ROOT` は `<repo>/projects` を指し、**31本が `projects/projects/` へ書かれた。**
#    ⛔ **しかも「変わらない」という検算は通った**——**本物の仕様は1バイトも
#    触られていなかったからである。** **測った範囲と、主張した範囲がずれていた。**
#    ⚠️ **書き先が在ること自体は、正しさの証拠にならない。**
assert (ROOT / "CLAUDE.md").is_file() and (ROOT / "projects" / "odyssey").is_dir(), (
    "ROOT がリポジトリの根を指していない: %s" % ROOT)


def load(sid):
    path = HERE / "content" / ("%s.py" % sid)
    spec = importlib.util.spec_from_file_location("content_%s" % sid, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod.C


def build(sid):
    import tpl
    c = load(sid)
    rec = ROSTER[sid]
    # The beat table must agree with the shot record (L37); take it from there unless overridden.
    if not c.get("beats"):
        c["beats"] = [(b["range"], b["density"], b["text"]) for b in rec["beats"]]
    for k in ("duration", "format", "place", "time"):
        assert k not in c or str(c[k]).rstrip("s") == str(rec[k]).rstrip("s"), \
            "%s: %s disagrees with the shot record (%r vs %r)" % (sid, k, c.get(k), rec[k])
    c.setdefault("duration", rec["duration"].rstrip("s"))
    c["format"] = rec["format"]
    return c


def main(argv):
    sids = argv or sorted(p.stem for p in (HERE / "content").glob("s*.py"))
    for sid in sids:
        c = build(sid)
        import tpl
        text = tpl.render(c)
        dest = ROOT / "projects/odyssey" / ROSTER[sid]["spec"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        print("wrote %-40s %5d lines" % (dest.relative_to(ROOT), text.count("\n")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
