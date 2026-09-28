import re, os, json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import lit
ROOT = str(pathlib.Path(__file__).resolve().parent.parent / "specs" / "video")
R = json.load(open(str(pathlib.Path(__file__).resolve().parent / "roster.json")))
NEG = re.compile(r"[Nn]o (figure|person|human|one) is in the frame|"
                 r"[Nn]o figure is in the frame|nothing stands on|"
                 r"no person (is )?in (the|this) frame|"
                 r"[Tt]here is no (figure|person)", re.I)
rows = []
for sid in sorted(R, key=lambda x: int(x[1:])):
    p = os.path.join(ROOT, "odyssey-%s.md" % sid)
    if not os.path.exists(p):
        print("%-5s MISSING" % sid); continue
    t = open(p, encoding="utf-8").read()
    b = t.split("# 18.", 1)[1]
    def slot(name):
        m = re.search(r"^## " + re.escape(name) + r"[ \t]*$", b, re.M)
        if not m: return ""
        rest = b[m.end():]
        n = re.search(r"^## ", rest, re.M)
        return rest[:n.start()] if n else rest
    vis = slot("Visual Prompt"); mas = slot("Master Prompt")
    id_in_vis = lit.IDENTITY in vis
    id_in_mas = lit.IDENTITY in mas
    neg = NEG.search(vis)
    rows.append((sid, R[sid]["place"], id_in_mas, id_in_vis, bool(neg),
                 neg.group(0) if neg else ""))
print("%-5s %-11s %-7s %-7s %-6s %s" % ("shot", "place", "塊/Mas", "塊/Vis", "否定", "判定"))
bad = []
for sid, place, im, iv, ng, txt in rows:
    if iv and ng:
        v = "⛔ 同一欄内で矛盾"; bad.append(sid)
    elif ng and not iv:
        v = "△ 人は居ない（塊なし）"
    elif iv:
        v = "ok 人が居る"
    else:
        v = "? 塊も否定も無い"
    print("%-5s %-11s %-7s %-7s %-6s %s" % (
        sid, place, "YES" if im else "-", "YES" if iv else "-",
        ("YES" if ng else "-"), v))
print()
print("⛔ 同一性の塊と『人は居ない』が同じ Visual Prompt に同居:", len(bad), "本")
print("   ->", " ".join(bad))
