#!/usr/bin/env python3
"""check.py — 事前検証。**生成を1回も走らせずに、設計の破綻を潰す。**

    使い方:  python3 engine/ledger/check.py projects/<project>
             python3 engine/ledger/check.py --self-test

二つの層を走らせる。

  1. **形** — `schemas/*.json` に当てる（jsonschema・Draft 2020-12）
  2. **意味** — `semantic.py`。**スキーマが書けない検査はここが負う**

⚠️ **層2 が要る理由。** `unit` を `{ before, after }` の対にしたのは
「`before` と `after` が同じ」を鳴らすためだったが、**JSON Schema はそれを鳴らせない。**
対にしたことと、対を検査できることは別である。→ `schemas/README.md`・`HISTORY.md`

⚠️ **空を OK と言わない。** ショットが0本なら `L0` が鳴る。
"""

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

try:
    import yaml
except ImportError:
    sys.exit("PyYAML が要る: python3 -m pip install --user pyyaml")

SCHEMAS = ("bible", "ledger", "shot-record", "take", "timeline")


# ---------------------------------------------------------------- 読み込み


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _natural(s):
    """`ch01-seg02` を辞書順ではなく数の順に並べる。"""
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


class Project:
    """`projects/<name>/` を読む。**読めないものは黙って空にしない。**"""

    def __init__(self, root):
        self.root = Path(root)
        self.name = self.root.name
        self.read_errors = []

        b = self.root / "bible.yaml"
        l = self.root / "ledger.yaml"
        self.bible = _load(b) if b.exists() else {}
        self.ledger = _load(l) if l.exists() else {}
        if not b.exists():
            self.read_errors.append(f"bible.yaml が無い（{b}）")
        if not l.exists():
            self.read_errors.append(f"ledger.yaml が無い（{l}）")

        self.shots = {}   # ショットID → ショット記録（1本につき1枚）
        self.takes = {}   # ショットID → テイクの列（1本につき何枚でも）
        d = self.root / "shots"
        if not d.is_dir():
            self.read_errors.append(f"shots/ が無い（{d}）")
        else:
            for p in sorted(d.glob("*.y*ml")):
                doc = _load(p)
                key = doc.get("shot")
                if not key:
                    self.read_errors.append(f"{p.name}: ショットIDが読めない")
                    continue
                if key in self.shots:
                    self.read_errors.append(f"{p.name}: ショット {key} が二重に在る")
                    continue
                self.shots[key] = doc

        d = self.root / "takes"
        if not d.is_dir():
            self.read_errors.append(f"takes/ が無い（{d}）— テイクの記録が1本も無い")
        else:
            for p in sorted(d.glob("*.y*ml")):
                doc = _load(p)
                key = (doc.get("take") or {}).get("shot")
                if not key:
                    self.read_errors.append(f"{p.name}: ショットIDが読めない")
                    continue
                self.takes.setdefault(key, []).append(doc)

        # 台帳の disclosure を {shot, attr, value} に均す。
        self.disclosure = []
        for cp in (self.ledger.get("disclosure") or []):
            if not isinstance(cp, dict):
                continue
            shot = cp.get("shot")
            for k, v in cp.items():
                if k != "shot":
                    self.disclosure.append({"shot": shot, "attr": k,
                                            "value": v, "raw": cp})

    # ------------------------------------------------------------ 台帳の座標

    def order(self):
        """ショットの並び。⚠️ **明示の並びを持たない——ID の自然順である。**

        台帳の disclosure は「変化点の間は直前の状態が続く」と定めるので、
        並びが要る。`timeline/` が入ったら、そちらを正とするべきである（未決定）。
        """
        return sorted(self.shots, key=_natural)

    def known_keys(self):
        """参照集合が引けるキー。**台帳から導出する。人手で並べない。**

        人物 `C`   → `C.sheet`（＝identity）・`C.identity`・`C.states.<名>`・`C.negatives`
        場所 `L`   → `L.base`・`L.states.<名>`・`L.geography`
        道具 `P`   → `P.appearance`・`P.negative`
        裸の名前も許す（その実体そのものを指す）。
        """
        keys = set()
        for name, entry in (self.ledger.get("characters") or {}).items():
            keys |= {name, f"{name}.sheet", f"{name}.identity", f"{name}.negatives"}
            for st in (entry or {}).get("states") or {}:
                keys.add(f"{name}.states.{st}")
        for name, entry in (self.ledger.get("locations") or {}).items():
            keys |= {name, f"{name}.base", f"{name}.geography"}
            for st in (entry or {}).get("states") or {}:
                keys.add(f"{name}.states.{st}")
        for name, entry in (self.ledger.get("props") or {}).items():
            keys |= {name, f"{name}.appearance", f"{name}.negative"}
        return keys


# ---------------------------------------------------------------- 形の検査


def validate_shape(project, schema_dir):
    """`schemas/` に当てる。**形だけを見る。意味は見ない。**"""
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        return [{"code": "S0", "shot": "",
                 "message": "jsonschema が無い: python3 -m pip install --user jsonschema"}]

    out = []
    cache = {}

    def validator(name):
        if name not in cache:
            p = Path(schema_dir) / f"{name}.schema.json"
            cache[name] = (Draft202012Validator(json.loads(p.read_text(encoding="utf-8")))
                           if p.exists() else None)
        return cache[name]

    def apply(doc, name, where):
        v = validator(name)
        if v is None:
            out.append({"code": "S0", "shot": where,
                        "message": f"スキーマ {name}.schema.json が無い"})
            return
        for e in sorted(v.iter_errors(doc), key=lambda e: list(e.path)):
            path = "/".join(str(x) for x in e.path) or "(root)"
            out.append({"code": "S1", "shot": where,
                        "message": f"[{name}] {path}: {e.message}"})

    if project.bible:
        apply(project.bible, "bible", project.name)
    if project.ledger:
        apply(project.ledger, "ledger", project.name)
    for s, doc in project.shots.items():
        apply(doc, "shot-record", s)
    for s, docs in project.takes.items():
        for d in docs:
            apply(d, "take", f"{s}#{(d.get('take') or {}).get('index')}")
    return out


# ---------------------------------------------------------------- 出力


def report(project, findings, shape, stream=sys.stdout):
    order = project.order()
    print(f"=== 事前検証  {project.name}", file=stream)
    print(f"    ショット {len(order)} 本 / テイク "
          f"{sum(len(v) for v in project.takes.values())} 本 / "
          f"台帳の変化点 {len(project.disclosure)} 個", file=stream)
    print(f"    並び: ID の自然順（timeline が入れば、そちらを正とすべきである）",
          file=stream)

    for e in project.read_errors:
        print(f"    ⚠️ 読めていない: {e}", file=stream)
    print(file=stream)

    allf = shape + findings
    viol = [f for f in allf if f.get("severity", "violation") == "violation"]
    notes = [f for f in allf if f.get("severity") == "note"]

    if not allf:
        print("--- 鳴ったもの: 0 件", file=stream)
        if not order:
            print("    ⚠️ **ただしショットが0本である。** 0 件は「正しい」ではない。",
                  file=stream)
        return 0

    def dump(title, items, stream=stream):
        if not items:
            return
        by = {}
        for f in items:
            by.setdefault(f["code"], []).append(f)
        for code in sorted(by):
            # ⚠️ 同じ所見を30回並べても読めない。**文面で畳み、ショットを連ねる。**
            groups = {}
            for f in by[code]:
                groups.setdefault(f["message"], []).append(f["shot"])
            print(f"--- {title}{code}  {len(by[code])} 件 / {len(groups)} 種", file=stream)
            for msg, shots in sorted(groups.items(), key=lambda kv: -len(kv[1])):
                named = [s for s in shots if s]
                if len(named) == len(shots) and named:
                    head = (f"    {', '.join(named[:4])}"
                            + (f" ほか {len(named) - 4} 本" if len(named) > 4 else ""))
                else:
                    head = f"    （{len(shots)} 件）"
                print(f"{head}\n        {msg}", file=stream)
            print(file=stream)

    dump("", viol)
    dump("註 ", notes)
    print(f"=== 違反 {len(viol)} 件 / 註 {len(notes)} 件", file=stream)
    if not viol:
        print("    ⚠️ 違反0件は「正しい」ではない。**註と、検査されていない範囲を読むこと。**",
              file=stream)
    return 1 if viol else 0


# ---------------------------------------------------------------- 自己検査


def self_test():
    """⚠️ **検査器が実際に鳴ることを、検査器自身で確かめる。**

    相手が空なら何も鳴らない。だから「1件も鳴らなかった」は
    「正しい」ではない——この自己検査は、**各検査が鳴る例を1つずつ持つ。**
    """
    sys.path.insert(0, str(HERE))
    import semantic  # noqa: E402

    clean = {
        "shot": "p-ch01-seg01",
        "unit": {"before": "戸が閉まっている", "after": "戸が開いている"},
        "role": "establishing",
        "place": "OKURIBI",
        "time": "night",
        "mode": "motion",
        "duration": "6s",
        "reference_set": ["OKURIBI.sheet"],
        "attached": ["OKURIBI.sheet"],
        "forbidden_set": ["HANA"],
    }

    cases = [
        ("L0 空", None, {}),
        ("L1 一変化でない", {**clean, "unit": {"before": "同じ", "after": "同じ"}}, (semantic.check_unit,)),
        ("L2 環境の跨ぎ", {**clean, "place": "OKURIBI → HANA"}, (semantic.check_one_place,)),
        ("L3 時刻の跨ぎ(欄)", {**clean, "time": "night／morning"}, (semantic.check_one_time,)),
        ("L3 時刻の跨ぎ(本文)", {**clean, "beats": [
            {"range": "0-4s", "density": "sparse", "what": "Morning classroom"},
            {"range": "4-8s", "density": "dense", "what": "Afternoon gym"},
            {"range": "8-12s", "density": "sparse", "what": "放課後、夜"}]},
         (semantic.check_one_time,)),
        ("L4 移動の動詞", {**clean, "beats": [
            {"range": "0-4s", "density": "sparse", "what": "she walks home"}]},
         (semantic.check_move,)),
        ("L5 参照と禁制の衝突", {**clean, "forbidden_set": ["OKURIBI.sheet"]},
         (semantic.check_reference_forbidden,)),
        ("L6 意図と実際の食い違い", {**clean, "attached": []}, (semantic.check_attached,)),
        ("L6 添付の記録が無い", {k: v for k, v in clean.items() if k != "attached"},
         (semantic.check_attached,)),
    ]

    print("=== 自己検査 — 各検査が鳴るか\n")
    bad = 0
    n = 0
    print(f"    {'検査':<24}{'鳴った件数':>10}  判定")
    for label, shot, fns in cases:
        if shot is None:
            p = _Bare()
            got = semantic.check_not_empty(p)
        else:
            p = _One(shot)
            got = [f for fn in fns for f in fn(shot)]
            if not got:
                got += semantic.check_keys_known(p, shot)
        n += 1
        ok = bool(got)
        bad += not ok
        print(f"    {label:<24}{len(got):>10}  {'鳴った' if ok else '⚠️ 鳴らなかった'}")
        for f in got:
            print(f"        {f['code']}  {f['message'][:88]}")

    # 正しい例は鳴ってはならない
    p = _One(clean)
    ok_findings = [f for fn in semantic.CHECKS_SHOT for f in fn(clean)]
    ok_findings += semantic.check_keys_known(p, clean)
    print(f"\n    {'正しい例（鳴ってはならない）':<24}{len(ok_findings):>10}  "
          f"{'鳴らなかった' if not ok_findings else '⚠️ 誤検出'}")
    for f in ok_findings:
        print(f"        {f['code']}  {f['message'][:88]}")
    bad += bool(ok_findings)

    # ---- 層B（台帳と突き合わせる検査）は、Project を組んで当てる
    print("\n=== 自己検査 — 台帳と突き合わせる検査\n")

    def proj(shots, disclosure):
        p = _One(shots[0])
        p.shots = {s["shot"]: s for s in shots}
        p.disclosure = disclosure
        p.ledger = {"characters": {"HANA": {"identity": "x"}},
                    "locations": {}, "disclosure": disclosure}
        return p

    def s(sid, **kw):
        return {**clean, "shot": sid, **kw}

    ledger_cases = [
        ("L7a 早すぎる開示",
         [s("p-ch01-seg01", disclosure_state={"HANA": "present"}),
          s("p-ch01-seg03", disclosure_state={"HANA": "present"})],
         [{"shot": "p-ch01-seg03", "attr": "HANA", "value": "present"}]),
        ("L7b 台帳が予測していない",
         [s("p-ch01-seg03", disclosure_state={"HANA": "absent"})],
         [{"shot": "p-ch01-seg03", "attr": "HANA", "value": "present"}]),
        ("L7 状態を持たないショットの報告",
         [s("p-ch01-seg01"), s("p-ch01-seg02")],
         [{"shot": "p-ch01-seg01", "attr": "HANA", "value": "present"}]),
        ("L7 宣言の変化点が存在しない",
         [s("p-ch01-seg01", disclosure_state={})],
         [{"shot": "p-ch99-seg01", "attr": "HANA", "value": "present"}]),
        ("L8 台帳に無いキー",
         [s("p-ch01-seg01", reference_set=["NOPE.sheet"], attached=["NOPE.sheet"])],
         []),
    ]
    print(f"    {'検査':<28}{'鳴った件数':>10}  判定")
    for label, shots, disc in ledger_cases:
        p = proj(shots, disc)
        got = semantic.check_disclosure(p)
        got += [f for sh in p.order()
                for f in semantic.check_keys_known(p, p.shots[sh])]
        n += 1
        ok = bool(got)
        bad += not ok
        print(f"    {label:<28}{len(got):>10}  {'鳴った' if ok else '⚠️ 鳴らなかった'}")
        for f in got[:3]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # 開示が正しく通る例は鳴ってはならない
    good = proj([s("p-ch01-seg01", disclosure_state={"HANA": "absent"}),
                 s("p-ch01-seg03", disclosure_state={"HANA": "present"})],
                [{"shot": "p-ch01-seg03", "attr": "HANA", "value": "present"}])
    gf = semantic.check_disclosure(good)
    print(f"\n    {'正しい開示（鳴ってはならない）':<28}{len(gf):>10}  "
          f"{'鳴らなかった' if not gf else '⚠️ 誤検出'}")
    for f in gf:
        print(f"        {f['code']}  {f['message'][:88]}")
    bad += bool(gf)

    # ---- L9（検査が空であることの検査）は、他とは逆に「鳴るのが期待」の場合がある
    print("\n=== 自己検査 — 検査が空でないか\n")

    disc1 = [{"shot": "p-ch01-seg03", "attr": "HANA", "value": "present"}]
    circular_cases = [
        # 台帳から写した記録 → 鳴らねばならない
        ("L9 台帳から写した（鳴るべき）",
         [s("p-ch01-seg01", disclosure_state={"HANA": "absent"}),
          s("p-ch01-seg03", disclosure_state={"HANA": "present"})], disc1, True),
        # 台帳が宣言していない位置で変わっている → 記録は新しいことを言っている
        ("L9 台帳に無い遷移（鳴ってはならない）",
         [s("p-ch01-seg01", disclosure_state={"HANA": "absent"}),
          s("p-ch01-seg02", disclosure_state={"HANA": "present"}),
          s("p-ch01-seg03", disclosure_state={"HANA": "present"})], disc1, False),
        # どのショットも開示状態を書いていない → 比較対象が無い
        ("L9 誰も書いていない（鳴ってはならない）",
         [s("p-ch01-seg01"), s("p-ch01-seg03")], disc1, False),
        # ⚠️ 最も重要——台帳が宣言していて、記録が書いていない属性は、
        #    食い違いではない。比較に入り込んではならない。
        ("L9 書いていない属性は無視（鳴るべき）",
         [s("p-ch01-seg01", disclosure_state={"HANA": "absent"}),
          s("p-ch01-seg03", disclosure_state={"HANA": "present"})],
         disc1 + [{"shot": "p-ch01-seg03", "attr": "HANA.speech", "value": "first"}], True),
    ]
    print(f"    {'検査':<34}{'鳴った件数':>10}  判定")
    for label, shots, disc, want in circular_cases:
        p = proj(shots, disc)
        got = semantic.check_circular(p)
        n += 1
        ok = bool(got) == want
        bad += not ok
        verdict = "鳴った" if got else "鳴らなかった"
        print(f"    {label:<34}{len(got):>10}  "
              f"{verdict if ok else '⚠️ 期待と違う（' + ('鳴るべき' if want else '鳴ってはならない') + '）'}")
        for f in got[:2]:
            print(f"        {f['code']}  {f['message'][:88]}")

    print(f"\n=== {n} 例中 {n - bad} 例が期待どおり")
    return 1 if bad else 0


class _Bare:
    shots, ledger, disclosure = {}, {}, []


class _One:
    def __init__(self, shot):
        self.shots = {shot["shot"]: shot}
        self.ledger = {"characters": {"OKURIBI": {"identity": "x"},
                                      "HANA": {"identity": "y"}},
                       "locations": {}, "disclosure": []}
        self.disclosure = []

    def order(self):
        return sorted(self.shots, key=_natural)

    def known_keys(self):
        return {"OKURIBI", "OKURIBI.sheet", "OKURIBI.identity", "OKURIBI.negatives",
                "HANA", "HANA.sheet", "HANA.identity", "HANA.negatives"}


# ---------------------------------------------------------------- 入口


def main():
    ap = argparse.ArgumentParser(description="事前検証 — 生成を1回も走らせずに設計の破綻を潰す")
    ap.add_argument("project", nargs="?", help="projects/<project> のパス")
    ap.add_argument("--schemas", default=str(REPO / "schemas"))
    ap.add_argument("--self-test", action="store_true",
                    help="検査器が実際に鳴ることを確かめる")
    a = ap.parse_args()

    if a.self_test:
        return self_test()
    if not a.project:
        ap.error("projects/<project> を渡すか --self-test を付ける")

    root = Path(a.project)
    if not root.is_dir():
        sys.exit(f"{root} が無い")
    p = Project(root)
    sys.path.insert(0, str(HERE))
    import semantic  # noqa: E402
    return report(p, semantic.run(p), validate_shape(p, a.schemas))


if __name__ == "__main__":
    sys.exit(main())
