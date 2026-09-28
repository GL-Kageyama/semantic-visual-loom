import re, sys, os, pathlib
ROOT = str(pathlib.Path(__file__).resolve().parent.parent / "specs" / "video")
for s in sys.argv[1:]:
    t = open(os.path.join(ROOT, "odyssey-%s.md" % s), encoding="utf-8").read()
    b = t.split("# 18.", 1)[1]
    print("########## %s ##########" % s)
    for slot in ("Visual Prompt", "Camera Prompt"):
        m = re.search(r"^## " + re.escape(slot) + r"[ \t]*$", b, re.M)
        if not m:
            print("--- %s --- MISSING" % slot); continue
        rest = b[m.end():]
        n = re.search(r"^## ", rest, re.M)
        body = (rest[:n.start()] if n else rest).strip()
        print("--- %s ---" % slot)
        print(body[:800])
        print()
