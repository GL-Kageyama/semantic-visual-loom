"""Extract, per shot, every fact the spec must be built from. One JSON, no retyping."""
import json, re, pathlib, yaml

SHOTS = pathlib.Path(__file__).resolve().parent.parent / "shots"
out = {}
for p in sorted(SHOTS.glob("odyssey-s*.yaml")):
    raw = p.read_text(encoding="utf-8")
    sid = p.stem.replace("odyssey-", "")
    head = [l[2:] for l in raw.splitlines() if l.startswith("# ")]
    # the title line: "verse-1 / still / 反応 / meaning-responsive —— ..."
    title = head[0]
    parts = [x.strip() for x in title.split("——")[0].split("/")]
    seq = [l for l in head if l.startswith("行:")]
    notes = []
    for l in head[1:]:
        if l.startswith("====="): break
        notes.append(l)
    d = yaml.safe_load(raw)
    beats = []
    ts = d.get("motion", {}) or {}
    for b in (d.get("beats") or []):
        beats.append({"range": b.get("range"), "density": b.get("density"),
                      "text": b.get("what", b.get("text", ""))})
    out[sid] = {
        "id": sid,
        "section": parts[0], "mode": parts[1], "role": parts[2], "format": parts[3],
        "title": title.split("——", 1)[1].strip() if "——" in title else "",
        "line": seq[0] if seq else "",
        "header_notes": notes,
        "duration": d.get("duration"),
        "place": d.get("place"), "time": d.get("time"),
        "unit_before": (d.get("unit") or {}).get("before"),
        "unit_after": (d.get("unit") or {}).get("after"),
        "aim": (d.get("aim") if isinstance(d.get("aim"), str) else d.get("aim")),
        "motion": dict(ts),
        "spec": d.get("spec"),
        "beats": beats,
        "reference_set": d.get("reference_set"),
        "forbidden_set": d.get("forbidden_set"),
        "disclosure_state": d.get("disclosure_state"),
        "raw_keys": sorted(d.keys()),
    }
pathlib.Path(__file__).with_name("roster.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
if __name__ == "__main__":
    print("shots:", len(out))
    print("keys of s06:", out["s06"]["raw_keys"])
    import collections
    print("formats:", dict(collections.Counter(v["format"] for v in out.values())))
    print("modes  :", dict(collections.Counter(v["mode"] for v in out.values())))
    print("roles  :", dict(collections.Counter(v["role"] for v in out.values())))
    print("places :", dict(collections.Counter(v["place"] for v in out.values())))
