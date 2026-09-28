import json, os, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import yaml
SH = str(pathlib.Path(__file__).resolve().parent.parent / "shots")
for sid in ["s12","s13","s14","s15","s26","s28","s29","s30","s31","s32"]:
    d = yaml.safe_load(open(os.path.join(SH, "odyssey-%s.yaml" % sid), encoding="utf-8"))
    u = d.get("unit") or {}
    mo = d.get("motion") or {}
    print("=" * 78)
    print("%s  place=%s  time=%s  role=%s  format=%s" % (
        sid, d.get("place"), d.get("time"), d.get("role"), d.get("format")))
    print("  before : %s" % str(u.get("before"))[:150])
    print("  after  : %s" % str(u.get("after"))[:150])
    print("  subj   : %s" % str(mo.get("subject"))[:150])
    bs = d.get("beats") or []
    for b in bs:
        txt = b.get("what") or b.get("text") or ""
        print("    beat %s-%s: %s" % (b.get("from"), b.get("to"), str(txt)[:110]))
    raw = open(os.path.join(SH, "odyssey-%s.yaml" % sid), encoding="utf-8").read()
    who = sorted({w for w in ("男", "彼", "人", "手", "肩", "顔") if w in raw})
    print("  記録に現れる語: %s" % ",".join(who))
