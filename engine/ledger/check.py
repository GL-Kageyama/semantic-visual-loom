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

# ⚠️ `disclosure` の変化点は「属性の袋」である。**この2つだけは属性ではない。**
#    `shot` 以外を属性として読むので、予約しないと `negative` という
#    開示属性が存在するかのように扱われる。**属性を足すときは、ここを見る。**
DISCLOSURE_RESERVED = ("shot", "negative")


# ---------------------------------------------------------------- 読み込み


class Unreadable(Exception):
    """ファイルは**在る**のに読めない。⚠️ **「無い」とは別である。**"""


def _load(path):
    """⚠️ **読めないファイルを黙って空にしない。**

    構文が壊れていれば `Unreadable` を投げる——**`{}` を返してはならない。**
    空の辞書は「0件」として通り、**「0件だから正しい」と読まれる。**
    """
    try:
        with open(path, encoding="utf-8") as fh:
            return yaml.safe_load(fh) or {}
    except (yaml.YAMLError, OSError, UnicodeDecodeError) as e:
        first = str(e).splitlines()[0] if str(e) else type(e).__name__
        raise Unreadable(f"{path.name}: {type(e).__name__}: {first}") from e


def _natural(s):
    """`ch01-seg02` を辞書順ではなく数の順に並べる。"""
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


class Project:
    """`projects/<name>/` を読む。**読めないものは黙って空にしない。**"""

    def __init__(self, root):
        self.root = Path(root)
        self.name = self.root.name
        self.read_errors = []

        def read(path):
            """⚠️ **1本読めなくても、検査は最後まで走る。**

            例外を上げて止まると、**壊れた1本が他のすべての報告を隠す**——
            そして**報告しない検査は、通った検査と同じに見える。**
            """
            try:
                return _load(path)
            except Unreadable as e:
                self.read_errors.append(f"読めない: {e}")
                return {}

        b = self.root / "bible.yaml"
        l = self.root / "ledger.yaml"
        self.bible = read(b) if b.exists() else {}
        self.ledger = read(l) if l.exists() else {}
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
                doc = read(p)
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
                doc = read(p)
                key = (doc.get("take") or {}).get("shot")
                if not key:
                    self.read_errors.append(f"{p.name}: ショットIDが読めない")
                    continue
                self.takes.setdefault(key, []).append(doc)
            # ⚠️ **空のディレクトリも報告する。** 「無い」だけを報告すると、
            #    `takes/` を置いた時点で**「テイクの記録が1本も無い」が消える**
            #    ——**置いたことは、撮ったことではない。**
            #    空を OK と言わない（README「⚠️ 空を OK と言わない」）。
            #    ⚠️ これを「0件だから正しい」と読んではならない——**読むのは人である。**
            if not self.takes:
                self.read_errors.append(
                    "takes/ は在るが、**テイクの記録が1本も無い**——"
                    "生成は一度も走っていない。"
                    "「テイク0件」は「違反0件」ではない。**選別の検査が空である。**")

        # 台帳の disclosure を {shot, attr, value} に均す。
        # ⚠️ 変化点は「属性の袋」である（`HANA: present` のように書く）。
        #    **だから、袋に入れてはならない鍵がある。** 予約鍵を属性として読むと、
        #    `negative` という名前の開示属性が存在するかのように扱われる。
        self.disclosure = []
        for cp in (self.ledger.get("disclosure") or []):
            if not isinstance(cp, dict):
                continue
            shot = cp.get("shot")
            for k, v in cp.items():
                if k in DISCLOSURE_RESERVED:
                    continue
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

    # ⚠️ **`role` は日本語で書く。** 生成器へ渡る文字列ではないからである
    #    （§1–20 に欄が無い＝モデルに渡る文に現れない）。目録の `establishing` は
    #    読みのための註であって、綴りの半分ではない。**L15 がそう鳴らす。**
    # ⚠️ **`motion` を持つ。** `mode: motion` なので L16 が要求する（決定 2026-09-13）。
    clean = {
        "shot": "p-ch01-seg01",
        "unit": {"before": "戸が閉まっている", "after": "戸が開いている"},
        "role": "情景",
        "place": "OKURIBI",
        "time": "night",
        "mode": "motion",
        "duration": "6s",
        "motion": {"subject": "火", "quality": "揺れる", "law": "限定作画"},
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

    # ---- L10（開示の変化点は、モデルに渡る文に現れているか）
    #     ⚠️ **相手は本物の仕様書である。** 合成した節では、読む側が壊れていても通る。
    print("\n=== 自己検査 — 開示の変化点と §18 の突き合わせ\n")

    import tempfile
    from pathlib import Path as _P

    SPEC_A = ("## Negative Prompt\n\nno schoolgirl, no nameplate, no readable text\n\n"
              "# 19. GENERATION INSTANCE\n")
    SPEC_B = ("## Negative Prompt\n\nno schoolgirl, no nameplate, no readable text, "
              "no ghost, no translucent figure\n\n# 19. GENERATION INSTANCE\n")
    SPEC_NOSEC = "## Instance\n\nsomething else entirely\n"

    def spec_proj(files, disc_raw):
        """⚠️ `specdoc` に**本物のファイルを読ませる**。合成の節では読む側を検査できない。"""
        d = _P(tempfile.mkdtemp())
        for name, body in files.items():
            (d / name).write_text(body, encoding="utf-8")
        shots = [s("p-ch01-seg01", spec="a.md" if "a.md" in files else None),
                 s("p-ch01-seg02", spec="b.md")]
        p = _One(shots[0])
        p.root = d
        p.shots = {x["shot"]: x for x in shots}
        p.disclosure = [dict(cp) for cp in disc_raw]
        return p

    def cp(neg, shot="p-ch01-seg02"):
        raw = {"shot": shot, "HANA": "present"}
        if neg is not None:
            raw["negative"] = neg
        return {"shot": shot, "attr": "HANA", "value": "present", "raw": raw}

    # 差が出る対（b が a と違う）と、出ない対（同じ）
    SAME = {"a.md": SPEC_A, "b.md": SPEC_A}
    DIFF = {"a.md": SPEC_A, "b.md": SPEC_B}

    neg_cases = [
        ("L10 宣言が無い", SAME, cp(None), True,
         "変化点に `negative:` が無い。**§18 に対して確かめられていない。**"),
        ("L10 changed と言い、§18 は同じ", SAME, cp("changed"), True,
         "`negative: changed` と宣言しているが"),
        ("L10 covered と言い、§18 は違う", DIFF, cp("covered"), True,
         "`negative: covered` と宣言しているが"),
        ("L10 値が changed/covered でない", SAME, cp("maybe"), True, "どちらでもない"),
        ("L10 changed と言い、§18 も違う（鳴ってはならない）", DIFF, cp("changed"), False, None),
        ("L10 covered と言い、§18 も同じ（鳴ってはならない）", SAME, cp("covered"), False, None),
        ("L10 §18 の節が無い", {"a.md": SPEC_NOSEC, "b.md": SPEC_NOSEC},
         cp("changed"), True, "`Negative Prompt` の節が無い"),
    ]
    for label, files, point, want, fragment in neg_cases:
        p = spec_proj(files, [point])
        got = semantic.check_negative_response(p)
        # ⚠️ 註（確かめた報告）と違反を分ける。**註は「鳴った」ではない。**
        v = [f for f in got if f["severity"] != "note"]
        n += 1
        ok = bool(v) == want and (not want or any(fragment in f["message"] for f in v))
        bad += not ok
        verdict = f"違反 {len(v)} 件" if v else "違反0件"
        print(f"    {label:<44}{verdict:>10}  "
              f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in v[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **註の側も読む。** 「違反0件」だけでは註が正しいことは分からない——
    #    **註が出ないことも「違反0件」に見える**からである。ここで見るのは
    #    「記録が無いこと」であって「食い違っていること」ではない（決定 2026-09-13）。
    no_a = {k: v for k, v in SAME.items() if k != "a.md"}
    note_cases = [
        ("L10 先行する §18 が無い＝註", no_a, cp("changed"),
         "先行する §18 を持つショットが無い"),
        ("L10 変化点に動画の仕様が無い＝註", no_a, cp("changed", shot="p-ch01-seg01"),
         "動画の仕様（`spec:`）が無い"),
    ]
    for label, files, point, fragment in note_cases:
        p = spec_proj(files, [point])
        got = semantic.check_negative_response(p)
        notes = [f for f in got if f["severity"] == "note"]
        v = [f for f in got if f["severity"] != "note"]
        n += 1
        ok = bool(notes) and not v and any(fragment in f["message"] for f in notes)
        bad += not ok
        print(f"    {label:<44}{f'註 {len(notes)} 件':>10}  "
              f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in notes[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ---- L11（仕様の節が目録のとおりか）
    #     ⚠️ **本物の節見出しを書いたファイルを読ませる。** 合成の見出しでは、
    #        節を割る側が壊れていても通る（L10 と同じ理由）。
    print("\n=== 自己検査 — 仕様の節の目録\n")

    import specmap  # noqa: E402

    def specfile(*titles):
        return "\n".join(f"# {t}\n\n本文\n" for t in titles)

    ALL20 = tuple(specmap.SPEC_SECTIONS)

    def sec_proj(body):
        d = _P(tempfile.mkdtemp())
        (d / "a.md").write_text(body, encoding="utf-8")
        sh = s("p-ch01-seg01", spec="a.md")
        p = _One(sh)
        p.root = d
        p.shots = {"p-ch01-seg01": sh}
        return p

    sec_cases = [
        ("L11 目録どおり（鳴ってはならない）", specfile(*ALL20), False, None),
        ("L11 目録に無い節がある", specfile(*ALL20, "21. PROVIDER NOTES"), True, "目録に無い節"),
        ("L11 目録の節が無い", specfile(*ALL20[:-1]), True, "目録にある節が無い"),
        ("L11 順序が違う",
         specfile(*ALL20[:17], "19. GENERATION INSTANCE", "18. WAN 3.0 PROMPT MAPPING", "20. ITERATION"),
         True, "順序が違う"),
        ("L11 spec が無い", None, True, "`spec:` が無い"),
    ]
    for label, body, want, fragment in sec_cases:
        p = _One(s("p-ch01-seg01"))
        if body is not None:
            p = sec_proj(body)
        got = [f for f in semantic.check_spec_sections(p) if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<40}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **目録そのものが短くなったら鳴らねばならない。** 短くなれば、
    #    仕様に節が足されても鳴らない——**検査が空になる。**
    saved = specmap.SPEC_SECTIONS
    try:
        specmap.SPEC_SECTIONS = saved[:3]
        got = [f for f in semantic.check_spec_sections(sec_proj(specfile(*ALL20)))
               if f["severity"] != "note"]
    finally:
        specmap.SPEC_SECTIONS = saved
    n += 1
    ok = bool(got) and any("目録の節が" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L11 目録そのものが短い':<40}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
    for f in got[:1]:
        print(f"        {f['code']}  {f['message'][:88]}")

    # ---- L13（ショットの同一性が仕様の自己名と一致するか）
    print("\n=== 自己検査 — ショットの同一性\n")

    def inst(shot_id="p-ch01-seg01", iid=None, seg="01-1", tail=""):
        iid = iid if iid is not None else f"{shot_id}-30s-01"
        return (f"# 19. GENERATION INSTANCE\n\n## Instance\n\n"
                f"- Instance ID: `{iid}`\n- Segment ID: `{seg}`\n{tail}\n")

    def id_proj(body, sid=None, first=None):
        """⚠️ **経路は欄が決める。** `spec:`（動画）と `key_image:`（画像）を別々に置く。"""
        d = _P(tempfile.mkdtemp())
        (d / "a.md").write_text(body, encoding="utf-8")
        kw = {}
        if first is not None:
            (d / "b.md").write_text(first, encoding="utf-8")
            kw["key_image"] = "b.md"
        sh = s(sid or "p-ch01-seg01", spec="a.md", **kw)
        p = _One(sh)
        p.root = d
        p.shots = {sh["shot"]: sh}
        return p

    id_cases = [
        ("L13 一致（鳴ってはならない）", inst(), None, None, False, None),
        ("L13 仕様の自己名と違う", inst(iid="p-ch01-seg07-30s-01"), None, None, True, "の本体は"),
        ("L13 接尾辞が無い", inst(iid="p-ch01-seg01"), None, None, True, "接尾辞が無い"),
        # ⚠️ **尺は小数でありうる。** 実測の `hitosara-ch01-seg09-2.5s-01` が読めず、
        #    検査は「接尾辞が無い」と鳴っていた——**規則ではなく、読み手が狭かった。**
        #    この2件は対である。**片方だけなら、綴りを消しても自己検査は緑のままになる。**
        ("L13 尺が小数でも読める（鳴ってはならない）",
         inst(iid="p-ch01-seg01-2.5s-01"), None, None, False, None),
        ("L13 接尾辞の尺が数でなければ鳴る",
         inst(iid="p-ch01-seg01-Xs-01"), None, None, True, "接尾辞が無い"),
        ("L13 Instance ID が無い",
         "# 19. GENERATION INSTANCE\n\n## Instance\n\n- Segment ID: `01-1`\n", None, None, True,
         "`Instance ID` が無い"),
        ("L13 Instance の節が無い", "# 19. GENERATION INSTANCE\n\n本文\n", None, None, True,
         "の節が無い"),
    ]
    for label, body, sid, first, want, fragment in id_cases:
        got = [f for f in semantic.check_identity(id_proj(body, sid, first))
               if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<40}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **画像の仕様は §19 を持たない。** だから `key_image` に置けば鳴ってはならない。
    #    そして**同じ本文を `spec:` に置けば鳴る**——この対でなければ、
    #    「絞った」のか「検査そのものが死んだ」のかを区別できない。
    #    **片方だけ置けば、検査を殺しても自己検査は緑のままになる。**
    #    ⚠️ **決定（2026-09-13）の前は、この対が `mode` の違いだった。**
    #    いまは**欄の違い**である——`mode` は経路を決めない。
    img_body = "# Shot 01 — 粉屋の棚\n\nAn English one-line prompt, with no sections at all.\n"
    img_cases = [
        ("L13 画像の仕様は `key_image`（鳴ってはならない）",
         inst(), None, img_body, False, None),
        ("L13 同じ本文を `spec:` に置けば鳴る", img_body, None, None, True, "の節が無い"),
    ]
    for label, body, sid, first, want, fragment in img_cases:
        got = [f for f in semantic.check_identity(id_proj(body, sid, first))
               if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<40}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ `Segment ID` の逸脱は**註**であって違反ではない。既存の成果物は直さない。
    got = semantic.check_identity(id_proj(inst(seg="A-1")))
    note = [f for f in got if f["severity"] == "note" and "Segment ID" in f["message"]]
    n += 1
    ok = not [f for f in got if f["severity"] != "note"] and bool(note)
    bad += not ok
    print(f"    {'L13 Segment ID の逸脱は註（違反でない）':<40}{len(note):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")

    # ⚠️ **同じ形の逸脱が `Segment ID` にもあった。** `\d\d-\d` は**10本目の `01-10` を
    #    読めない**——章の本数が2桁になれば、それは逸脱ではなく**同じ綴り**である。
    #    ここも対で見る: **2桁の本数は註を出さず**、別の綴り（`A-1`）は註を出す。
    got2 = semantic.check_identity(id_proj(inst(seg="01-10")))
    note2 = [f for f in got2 if f["severity"] == "note" and "Segment ID" in f["message"]]
    n += 1
    ok = not [f for f in got2 if f["severity"] != "note"] and not note2
    bad += not ok
    print(f"    {'L13 Segment ID 01-10 は逸脱でない（鳴ってはならない）':<40}{len(note2):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")

    # ---- L12（欄と節の対応が閉じているか）
    #     ⚠️ **本物のスキーマを読ませる。** そして**壊したスキーマでも鳴らす。**
    print("\n=== 自己検査 — 欄と節の対応\n")
    real_schemas = REPO / "schemas"

    def broken_schema(**mutate):
        d = _P(tempfile.mkdtemp())
        doc = json.loads((real_schemas / "shot-record.schema.json").read_text(encoding="utf-8"))
        mutate["fn"](doc)
        (d / "shot-record.schema.json").write_text(json.dumps(doc, ensure_ascii=False),
                                                   encoding="utf-8")
        return d

    def add_field(doc):
        doc["properties"]["camera_note"] = {"type": "string"}

    def drop_field(doc):
        del doc["properties"]["text_channel"]

    field_cases = [
        ("L12 本物のスキーマ（鳴ってはならない）", real_schemas, False, None),
        ("L12 出所の無い欄がある", broken_schema(fn=add_field), True, "の出所が宣言されていない"),
        ("L12 宣言が消えた欄を指す", broken_schema(fn=drop_field), True, "スキーマに無い"),
    ]
    for label, pth, want, fragment in field_cases:
        got = [f for f in semantic.check_field_source(pth) if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<40}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **両方向**。節が欄を名指さなくなっても、欄が節から来ていれば鳴る。
    saved_map = specmap.SPEC_MAP
    try:
        specmap.SPEC_MAP = {**saved_map, "14. AUDIO": {**saved_map["14. AUDIO"], "to": ()}}
        got = [f for f in semantic.check_field_source(real_schemas) if f["severity"] != "note"]
    finally:
        specmap.SPEC_MAP = saved_map
    n += 1
    ok = bool(got) and any("どの節もそれを名指していない" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L12 節が欄を名指さない（逆向き）':<40}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
    for f in got[:1]:
        print(f"        {f['code']}  {f['message'][:88]}")

    # ---- L14（宣言を超えた区間）
    #     ⚠️ **いちばん大事な例は「回転で鳴らない」である。**
    #        「§18 が動いたのに宣言が無い」で鳴らす素朴な版は、ここで鳴ってしまう。
    print("\n=== 自己検査 — 宣言を超えた区間\n")

    def beyond_proj(specs, declared_idx=()):
        """`specs` は各ショットの §18 節の並び。**本物のファイルを読ませる。**"""
        d = _P(tempfile.mkdtemp())
        shots = []
        for i, clauses in enumerate(specs, start=1):
            name = f"s{i}.md"
            (d / name).write_text(
                "## Negative Prompt\n\n" + ", ".join(clauses)
                + "\n\n# 19. GENERATION INSTANCE\n", encoding="utf-8")
            shots.append(s(f"p-ch01-seg{i:02d}", spec=name))
        p = _One(shots[0])
        p.root = d
        p.shots = {x["shot"]: x for x in shots}
        p.disclosure = [{"shot": shots[i]["shot"], "attr": "HANA", "value": "present",
                         "raw": {"shot": shots[i]["shot"], "negative": "changed"}}
                        for i in declared_idx]
        return p

    X, Y = "no nameplate", "no readable text"
    beyond_cases = [
        # 宣言済みの増分。**鳴ってはならない**（台帳が届いている）
        ("L14 増分が宣言済み（鳴ってはならない）",
         [[X], [X], [X, Y]], (2,), False, None),
        # ⚠️ 回転。**素朴な版はここで鳴る。** 02 が 00 の集合へ戻る
        ("L14 回転（鳴ってはならない）",
         [[X], [X, Y], [X], [X, Y]], (), False, None),
        # ⚠️ **言い換えは、鳴る。** 意味を見ないからである——`no girl` が消えて
        #    `no female figure` が以後ずっと残るなら、集合としては**戻らない増分**である。
        ("L14 戻らない言い換え（鳴る。意味は見ない）",
         [[X], [X, "no girl"], [X, "no female figure"], [X, "no female figure", "no ghost"]],
         (), True, "宣言を超えた区間である"),
        # 持続する増分。**鳴らねばならない**——以後すべてに在り、先行に無い
        ("L14 宣言を超えた増分",
         [[X], [X, Y], [X, Y], [X, Y]], (), True, "宣言を超えた区間である"),
        # 途中で消える節は「持続する増分」ではない
        ("L14 一度現れて消える節（鳴ってはならない）",
         [[X], [X, Y], [X], [X]], (), False, None),
        # ⚠️ **戻らない削除も鳴る。** 禁止が消えるのは、描いてよいものが増えることである
        ("L14 戻らない削除（鳴る）",
         [[X, "no ghost"], [X, "no ghost"], [X], [X]], (), True, "消えた"),
        # 削除が宣言済みなら鳴らない
        ("L14 削除が宣言済み（鳴ってはならない）",
         [[X, "no ghost"], [X, "no ghost"], [X], [X]], (2,), False, None),
        # ⚠️ **検査が空である。** §18 が1本も読めない
        ("L14 §18 が1本も読めない", [None, None], (), True, "検査が空である"),
    ]
    for label, specs, decl, want, fragment in beyond_cases:
        if specs and specs[0] is None:
            d = _P(tempfile.mkdtemp())
            shots = [s(f"p-ch01-seg{i:02d}", spec="none.md") for i in (1, 2)]
            p = _One(shots[0])
            p.root, p.shots, p.disclosure = d, {x["shot"]: x for x in shots}, []
        else:
            p = beyond_proj(specs, decl)
        got = [f for f in semantic.check_beyond_declaration(p) if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # 回転の註が出ること自体も見る（註は「鳴った」ではない）
    got = semantic.check_beyond_declaration(
        beyond_proj([[X], [X, Y], [X], [X, Y]], ()))
    n += 1
    note = [f for f in got if f["severity"] == "note" and "回転は明かしではない" in f["message"]]
    bad += not note
    print(f"    {'L14 回転を註で報告する':<44}{len(note):>10}  "
          f"{'期待どおり' if note else '⚠️ 期待と違う'}")

    # ---- L10・L14 が「モードの混ざった並び」で正しく鳴るか
    #     ⚠️ **§18 は連続していない。** 静的なショットが間に挟まれば、§18 の列は
    #        そこで切れる。**切れ目を跨いだ変化は、跨いで比べねば見えない。**
    #        L10 は「1つ前を見る」で、L14 は「隣り合う2つを見る」で、
    #        そこを丸ごと落としていた——**鳴らない分岐である。**
    print("\n=== 自己検査 — モードの混ざった並び\n")

    def mix_proj(rows, points=()):
        """`rows` は `(ショットID, mode, 本文, 経路)`。**本物のファイルを読ませる。**

        ⚠️ **経路は欄が決める**（決定 2026-09-13）。だから画像のショットは
        `spec:` を持たず、`key_image:` を持つ——**`mode` では決まらない。**
        `mode` を渡しているのは、**`mode` が経路を決めないことを自分で踏むためである**
        （この表の `still` は画像の経路を指すが、それは欄が決めている）。
        """
        d = _P(tempfile.mkdtemp())
        shots = []
        for sid, mode, body, kind in rows:
            (d / f"{sid}.md").write_text(body, encoding="utf-8")
            field = specmap.SPEC_KINDS[kind]["field"]
            shots.append(s(sid, mode=mode, **{field: f"{sid}.md"}))
        p = _One(shots[0])
        p.root = d
        p.shots = {x["shot"]: x for x in shots}
        p.disclosure = [dict(c) for c in points]
        return p

    S2, S4 = "p-ch01-seg02", "p-ch01-seg04"
    # ⚠️ **画像のショットの仕様は、§18 を持たない一文である。**
    #    §18 を持たせてしまうと、この例は「混ざった並び」を再現しない。
    IMG = "A rustic bakery shelf at dawn, flour dust in warm light, 35mm\n"
    MIXED = [("p-ch01-seg01", "still", IMG, "image"),
             (S2, "motion", SPEC_A, "video"),
             ("p-ch01-seg03", "still", IMG, "image"),
             (S4, "motion", SPEC_B, "video")]

    # ① L10 — 変化点が画像の経路にある。**違反ではなく註である。**
    got = semantic.check_negative_response(
        mix_proj(MIXED, [cp(None, shot="p-ch01-seg03")]))
    n += 1
    v = [f for f in got if f["severity"] != "note"]
    ok = not v and any("動画の仕様（`spec:`）が無い" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L10 変化点が画像の経路（註・違反でない）':<46}{len(got):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
    for f in got[:1]:
        print(f"        {f['code']}  {f['message'][:88]}")

    # ② L10 — **静的なショットを挟んで比べているか。**
    #     seg02 と seg04 は §18 が違う。`covered` と言えば**理由が誤っている。**
    got = [f for f in semantic.check_negative_response(
        mix_proj(MIXED, [cp("covered", shot=S4)])) if f["severity"] != "note"]
    n += 1
    ok = bool(got) and any("理由が誤っている" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L10 挟まれた静的なショットを跨いで比べる':<46}{len(got):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
    for f in got[:1]:
        print(f"        {f['code']}  {f['message'][:88]}")

    got = [f for f in semantic.check_negative_response(
        mix_proj(MIXED, [cp("changed", shot=S4)])) if f["severity"] != "note"]
    n += 1
    bad += bool(got)
    print(f"    {'L10 同じ対で changed は鳴らない':<46}{len(got):>10}  "
          f"{'期待どおり' if not got else '⚠️ 期待と違う'}")

    # ③ L14 — **跨いだ持続変化を捕まえるか。** 旧い版はここを丸ごと落としていた。
    got = [f for f in semantic.check_beyond_declaration(mix_proj(MIXED))
           if f["severity"] != "note"]
    n += 1
    ok = bool(got) and all(f["shot"] == S4 for f in got)
    bad += not ok
    print(f"    {'L14 画像の経路を跨いだ持続変化':<46}{len(got):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
    for f in got[:1]:
        print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **宣言があれば鳴らない。** 跨いだ位置でも、台帳が届いていれば註である。
    got = [f for f in semantic.check_beyond_declaration(
        mix_proj(MIXED, [cp("changed", shot=S4)])) if f["severity"] != "note"]
    n += 1
    bad += bool(got)
    print(f"    {'L14 跨いだ変化が宣言済み（鳴ってはならない）':<46}{len(got):>10}  "
          f"{'期待どおり' if not got else '⚠️ 期待と違う'}")

    # ⚠️ **動画の仕様が無いことは「読めない」ではない。** 同じ符号で報告しない。
    got = semantic.check_beyond_declaration(mix_proj(MIXED))
    n += 1
    notes = [f for f in got if f["severity"] == "note"]
    ok = (any("動画の仕様（`spec:`）が無い" in f["message"] for f in notes)
          and not any("`spec:` が無いか読めない" in f["message"] for f in notes))
    bad += not ok
    print(f"    {'L14 「持たない」と「読めない」を分ける':<46}{len(notes):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")

    print("\n=== 自己検査 — 種別の目録\n")

    import rolemap  # noqa: E402

    def role_proj(roles):
        shots = [s(f"p-ch01-seg{i:02d}", role=r) for i, r in enumerate(roles, start=1)]
        p = _One(shots[0])
        p.shots = {x["shot"]: x for x in shots}
        return p

    role_cases = [
        # ⚠️ **素の名**は引ける。登録された12種のどれでも。
        ("L15 登録済みの種別（鳴ってはならない）", ["情景", "所作"], False, None),
        # ⚠️ **目録の外**。名のない種別に出会ったら、登録する。
        ("L15 目録に無い種別", ["情景", "見立て"], True, "は目録に無い"),
        # ⚠️ **英語の綴り**。目録の `establishing` は読みであって、値ではない。
        ("L15 英語の綴り（読みを値にしている）", ["establishing"], True, "は目録に無い"),
        # ⚠️ **限定つき**。`運動（停止）` は引ける——これが実測の綴りである。
        ("L15 限定つきの運動（鳴ってはならない）", ["運動（停止）"], False, None),
        # ⚠️ **限定の側が目録に無い**なら鳴る。
        ("L15 運動の層に無いパターン", ["運動（跳躍）"], True, "は運動の層の目録に無い"),
        # ⚠️ **限定をつけられるのは運動だけである。**
        ("L15 運動以外に限定をつける", ["開示（遅延）"], True, "限定をつけられるのは"),
    ]
    for label, roles, want, fragment in role_cases:
        got = [f for f in semantic.check_role_registered(role_proj(roles))
               if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # 註の側。**使われていない種別は違反ではない**——註で報告する。
    got = semantic.check_role_registered(role_proj(["情景", "運動（停止）", "運動（停止）"]))
    notes = [f for f in got if f["severity"] == "note"]
    n += 1
    has_unused = any("使われていない" in f["message"] for f in notes)
    has_qual = any("限定つきの綴り" in f["message"] for f in notes)
    ok = (not [f for f in got if f["severity"] != "note"]) and has_unused and has_qual
    bad += not ok
    print(f"    {'L15 未使用の種別と限定つきの綴りを註で報告':<44}{len(notes):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")

    got = semantic.check_role_registered(role_proj([""]))
    n += 1
    ok = (not [f for f in got if f["severity"] != "note"]
          and any("種別が無い" in f["message"] for f in got))
    bad += not ok
    print(f"    {'L15 種別が空：鳴らさないが黙らない':<44}{len(got):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")

    # ⚠️ **目録そのものが短くなれば、名のない種別を鳴らせない。** L11 と同じ形。
    saved_roles = rolemap.ROLES
    try:
        rolemap.ROLES = dict(list(saved_roles.items())[:3])
        got = [f for f in semantic.check_role_registered(role_proj(["情景"]))
               if f["severity"] != "note"]
    finally:
        rolemap.ROLES = saved_roles
    n += 1
    ok = bool(got) and any("目録が" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L15 目録そのものが短い':<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")

    # ---- L16（運動の層が無い）
    #     ⚠️ **決定（2026-09-13）で、`mode` はここを左右しなくなった。**
    #        **全モードで必須である**——だから例も**3つのモードすべて**で置く。
    #        **1つだけ置けば、「全モード」を「1モード」に戻しても緑のままになる。**
    print("\n=== 自己検査 — 運動の層の必須\n")

    MOT = {"subject": "手", "quality": "止まる", "law": "限定作画"}
    NOMOT = {k: v for k, v in clean.items() if k != "motion"}
    mot_cases = [
        # ⚠️ **全モードで必須である。** 3つとも鳴らす——**`still` が本命である**
        #    （決定の前に Omit を許していたのは、そこだけだから）。
        ("L16 mode: motion で motion が無い", NOMOT, True, "運動の層が無い"),
        ("L16 mode: composite で motion が無い",
         {**NOMOT, "mode": "composite"}, True, "運動の層が無い"),
        ("L16 mode: still で motion が無い",
         {**NOMOT, "mode": "still"}, True, "運動の層が無い"),
        # motion があれば鳴らない
        ("L16 motion がある（鳴ってはならない）", {**clean, "motion": MOT}, False, None),
        # ⚠️ **欄を置いたことは、書いたことではない。**
        ("L16 motion はあるが空",
         {**clean, "motion": {"subject": "", "quality": "  ", "law": "限定作画"}},
         True, "空の欄がある"),
    ]
    for label, shot, want, fragment in mot_cases:
        got = [f for f in semantic.check_motion_required(shot) if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **`mode` が無くても、要否は決まる。** 旧規則の下では「決められない」が
    #    起こりえたが、**いまは要否が `mode` によらない**——だから
    #    **`mode` の不在は形の層（`required`）が鳴らす。** ここは重ねて鳴らさない。
    got = [f for f in semantic.check_motion_required({**NOMOT, "mode": None})
           if f["severity"] != "note"]
    n += 1
    ok = bool(got) and any("運動の層が無い" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L16 mode が無くても要否は決まる':<44}{len(got):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")

    # ---- L17（§18 のスロットが目録のとおりか）
    #     ⚠️ **本物の見出しを書いたファイルを読ませる**（L10・L11 と同じ理由）。
    print("\n=== 自己検査 — §18 のスロットの目録\n")

    def sec18(*slots, title="18. WAN 3.0 PROMPT MAPPING"):
        body = "".join(f"## {t}\n\n本文\n\n" for t in slots)
        return f"# {title}\n\n{body}# 19. GENERATION INSTANCE\n\n本文\n"

    def slots_proj(body, style="soft-cel-anime", first=None):
        """⚠️ **経路は欄が決める。** §18 を読む相手は `spec:` であって `mode` ではない。"""
        d = _P(tempfile.mkdtemp())
        (d / "a.md").write_text(body, encoding="utf-8")
        kw = {}
        if first is not None:
            (d / "b.md").write_text(first, encoding="utf-8")
            kw["key_image"] = "b.md"
        sh = s("p-ch01-seg01", spec="a.md", **kw)
        p = _One(sh)
        p.root = d
        p.shots = {"p-ch01-seg01": sh}
        p.bible = {"project": "p", "bible": {"world": {}}}
        if style is not None:
            p.bible["bible"]["style"] = style
        return p

    SIX = ("Master Prompt", "Visual Prompt", "Motion Prompt",
           "Camera Prompt", "Audio Prompt", "Negative Prompt")

    slot_cases = [
        # ⚠️ **7つ揃えば鳴らない。** 行き先が在る状態である。
        ("L17 7スロット揃い（鳴ってはならない）",
         sec18(*SIX, "Style Motion"), "soft-cel-anime", False, None),
        # ⚠️ **実測の状態。** `Style Motion` が無い——これが 99/99 本である。
        ("L17 Style Motion が無い（実測の状態）",
         sec18(*SIX), "soft-cel-anime", True, "`Style Motion` は決定"),
        # 目録に無いスロット
        ("L17 目録に無いスロット", sec18(*SIX, "Style Motion", "Sound Prompt"),
         "soft-cel-anime", True, "目録に無いスロットがある"),
        # §18 の小節が1つも無い
        ("L17 §18 に小節が無い", "# 18. WAN 3.0 PROMPT MAPPING\n\n本文\n",
         "soft-cel-anime", True, "スロットを1つも確かめられない"),
        # ⚠️ **出所が決まっていないスロット**——様式を宣言せずに `Style Motion` を置く。
        ("L17 Style Motion があるのに様式が未宣言",
         sec18(*SIX, "Style Motion"), None, True, "様式を宣言していない"),
    ]
    for label, body, style, want, fragment in slot_cases:
        got = [f for f in semantic.check_prompt_slots(slots_proj(body, style))
               if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **画像の仕様は §18 を持たない。** 「小節が1つも無い」は画像では
    #    欠陥ではない——`L13` と同じ形の誤りである。
    #    ⚠️ **この対が言っているのは「`L17` は `key_image` を読まない」ことである。**
    #    同じ一文（`img_body`）を `key_image` に置けば鳴らず、`spec:` に置けば鳴る。
    #    **片方だけ置けば、検査を殺しても自己検査は緑のままになる。**
    #    ⚠️ **決定（2026-09-13）の前は、この対が `mode` の違いだった。**
    img_cases17 = [
        ("L17 画像の仕様は `key_image`（鳴ってはならない）",
         sec18(*SIX, "Style Motion"), img_body, False, None),
        ("L17 同じ本文を `spec:` に置けば鳴る",
         img_body, None, True, "スロットを1つも確かめられない"),
    ]
    for label, body, first, want, fragment in img_cases17:
        got = [f for f in semantic.check_prompt_slots(
            slots_proj(body, "luminous-anime", first)) if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **出所の無いスロットは、行き先になれない。** 目録と出所を両方向に閉じる。
    saved_slots = specmap.PROMPT_SLOTS
    try:
        specmap.PROMPT_SLOTS = saved_slots + ("Sound Prompt",)
        got = [f for f in semantic.check_prompt_slots(slots_proj(sec18(*SIX, "Style Motion")))
               if f["severity"] != "note"]
    finally:
        specmap.PROMPT_SLOTS = saved_slots
    n += 1
    ok = bool(got) and any("出所が宣言されていない" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L17 出所の無いスロット':<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")

    n += 1
    saved_src = specmap.PROMPT_SLOT_SOURCE
    try:
        specmap.PROMPT_SLOT_SOURCE = {**saved_src, "Style Motion": "様式カードの `Motion character`"}
        got = [f for f in semantic.check_prompt_slots(slots_proj(sec18(*SIX, "Style Motion")))
               if f["severity"] != "note"]
        ok = not got
    finally:
        specmap.PROMPT_SLOT_SOURCE = saved_src
    bad += not ok
    print(f"    {'L17 出所が揃えば鳴らない':<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")

    # ⚠️ **目録そのものが短くなれば、足されたスロットを鳴らせない。**
    n += 1
    try:
        specmap.PROMPT_SLOTS = saved_slots[:5]
        got = [f for f in semantic.check_prompt_slots(slots_proj(sec18(*SIX, "Style Motion")))
               if f["severity"] != "note"]
    finally:
        specmap.PROMPT_SLOTS = saved_slots
    ok = bool(got) and any("スロットの目録が" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L17 目録そのものが短い':<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")

    # ---- L18（2つの経路が、それぞれの形をしているか）
    #     ⚠️ **決定（2026-09-13）で、この検査は `mode` を読まなくなった。**
    #        経路を決めるのは**欄**である。だから例も**欄**で組む。
    #     ⚠️ **いちばん大事な例は「画像の経路で鳴らない」である。**
    #        画像を動画として読んでしまうのが、この検査を立てた理由だからである。
    print("\n=== 自己検査 — 仕様の種類とモデル\n")

    def kind_proj(video, first=None, mode="motion", write_first=True):
        """`spec:`（動画）と `key_image:`（画像）を別々に置く。

        ⚠️ **`first` が `None` なら欄ごと置かない**（＝記録が無い）。
        `write_first=False` なら**欄は置くがファイルは書かない**（＝読めない）——
        **「無い」と「読めない」は別である**（`L14` と同じ区別）。
        """
        d = _P(tempfile.mkdtemp())
        (d / "a.md").write_text(video, encoding="utf-8")
        kw = {}
        if first is not None:
            if write_first:
                (d / "b.md").write_text(first, encoding="utf-8")
            kw["key_image"] = "b.md"
        sh = s("p-ch01-seg01", spec="a.md", mode=mode, **kw)
        p = _One(sh)
        p.root = d
        p.shots = {"p-ch01-seg01": sh}
        return p

    # 動画の仕様＝§1–20 を持つ。画像のプロンプト＝**節を持たない**一文である。
    VIDEO20 = specfile(*ALL20)
    # ⚠️ **§18 の見出しだけを差し替える。** 節の並びは目録のままである。
    def video_naming(model):
        return specfile(*ALL20[:17], f"18. {model} PROMPT MAPPING", *ALL20[18:])

    VIDEO_WAN = video_naming("WAN 3.0")
    VIDEO_IMG = video_naming("CHATGPT IMAGE 2.5")
    VIDEO_XX = video_naming("SORA 9")
    IMAGE_ONELINE = ("A rustic bakery shelf at dawn, flour dust in warm light, "
                     "35mm, shallow depth of field\n")

    kind_cases = [
        # 2つの経路が、それぞれの形をしている。**決定のあとの標準の形である。**
        ("L18 2経路とも正しい（鳴ってはならない）", VIDEO_WAN, IMAGE_ONELINE, False, None),
        # ⚠️ **ここが本命。** 画像の経路は §1–20 を持たない。
        ("L18 画像の経路が §1–20 を持つ", VIDEO_WAN, VIDEO20, True,
         "画像プロンプトは節を持たない"),
        # §18 がモデルを名乗らない——`18. PROMPT MAPPING` は**族に一致するが名乗りが無い**。
        ("L18 §18 がモデルを名乗らない", VIDEO20, IMAGE_ONELINE, True, "名乗っていない"),
        ("L18 目録に無いモデル", VIDEO_XX, IMAGE_ONELINE, True, "`MODELS` に無い"),
        ("L18 種別が違う（画像のモデルを動画へ）", VIDEO_IMG, IMAGE_ONELINE, True,
         "生成の仕組みが違う"),
    ]
    for label, video, first, want, fragment in kind_cases:
        got = [f for f in semantic.check_spec_kind(kind_proj(video, first))
               if f["severity"] != "note"]
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<46}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **欄は在るのに開けない。** 「無い」とは別の符号で報告する——
    #    `L14` が「持たない」と「読めない」を分けているのと同じ理由である。
    got = [f for f in semantic.check_spec_kind(
        kind_proj(VIDEO_WAN, "A one-line prompt\n", write_first=False))
        if f["severity"] != "note"]
    n += 1
    ok = bool(got) and any("が読めない" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L18 画像の経路が読めない':<46}{len(got):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
    for f in got[:1]:
        print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **`mode` は経路を決めない。** だから目録の外の `mode` でも、この検査は鳴らない
    #    ——形の層（`enum`）と L24 が鳴らす。**決定（2026-09-13）の前はここが
    #    「モードが読めないから検査しない」という分岐だった。分岐ごと消えた。**
    got = [f for f in semantic.check_spec_kind(kind_proj(VIDEO_WAN, IMAGE_ONELINE, "wrong"))
           if f["severity"] != "note"]
    n += 1
    bad += bool(got)
    print(f"    {'L18 mode を読まない（鳴ってはならない）':<46}{len(got):>10}  "
          f"{'期待どおり' if not got else '⚠️ 期待と違う'}")

    # ⚠️ **`key_image` を持たないことは、違反ではない。** 記録が無いのであって、
    #    食い違っているのではない——**註であり、しかも1件に畳む。**
    got = semantic.check_spec_kind(kind_proj(VIDEO_WAN))
    n += 1
    notes = [f for f in got if f["severity"] == "note"]
    ok = (not [f for f in got if f["severity"] != "note"]
          and any("記録が無いのであって、食い違っているのではない" in f["message"]
                  for f in notes))
    bad += not ok
    print(f"    {'L18 画像の経路が無い＝註（違反でない）':<46}{len(notes):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
    for f in notes[:1]:
        print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **目録そのものが短くなれば、その経路を確かめられない。**
    #    ⚠️ **決定（2026-09-13）で `SPEC_KIND`（`mode` → 種類）は死んだ。**
    #    いま短くできるのは `SPEC_KINDS` のほうである。
    n += 1
    saved_kinds = specmap.SPEC_KINDS
    try:
        specmap.SPEC_KINDS = {k: v for k, v in saved_kinds.items() if k != "image"}
        got = [f for f in semantic.check_spec_kind(kind_proj(IMAGE_ONELINE, "still"))
               if f["severity"] != "note"]
    finally:
        specmap.SPEC_KINDS = saved_kinds
    ok = bool(got) and any("2 のはずである" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L18 経路の目録そのものが短い':<46}{len(got):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
    for f in got[:1]:
        print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **受け火の実物で鳴らないこと。** 合成データだけで通る検査は、現場で鳴る。
    real_v2 = REPO / "projects" / "ukebi" / "ukebi-v2"
    if real_v2.is_dir():
        p = Project(real_v2)
        v = [f for f in semantic.check_spec_kind(p) if f["severity"] != "note"]
        n += 1
        bad += bool(v)
        print(f"    {'L18 受け火 V2 の30本（鳴ってはならない）':<46}{len(v):>10}  "
              f"{'期待どおり' if not v else '⚠️ 期待と違う'}")
        for f in v[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ---- L19（記録の欄すべてに、行き先が宣言されているか）
    #     ⚠️ **本物のスキーマを読ませ、壊したスキーマでも鳴らす**（L12 と同じ形）。
    print("\n=== 自己検査 — 欄の行き先\n")

    def dest_schema(mutate=None):
        """⚠️ **`take` も写す。** `params` の鍵を確かめるのに要る。"""
        d = _P(tempfile.mkdtemp())
        for name in ("shot-record", "take"):
            doc = json.loads((real_schemas / f"{name}.schema.json").read_text(encoding="utf-8"))
            if mutate and name == "shot-record":
                mutate(doc)
            (d / f"{name}.schema.json").write_text(
                json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        return d

    def add_dest_field(doc):
        doc["properties"]["camera_note"] = {"type": "string"}

    def drop_dest_field(doc):
        del doc["properties"]["text_channel"]

    # ⚠️ **行き先は欄ごとに1つである**（`mode` 次元は無い）。差し替えは**まるごと**行う。
    def dest_of(**override):
        return {**specmap.FIELD_DESTINATION, **override}

    dest_cases = [
        ("L19 本物のスキーマ（鳴ってはならない）", dest_schema(), False, None, None),
        ("L19 行き先の無い欄がある", dest_schema(add_dest_field), True,
         "行き先が宣言されていない", None),
        ("L19 宣言が消えた欄を指す", dest_schema(drop_dest_field), True,
         "スキーマに無い", None),
        # ⚠️ **空の行き先は、行き先が無いのと同じである。** 宣言した顔をして1箇所へも行かない。
        ("L19 行き先が空である", real_schemas, True, "行き先が空である",
         {"FIELD_DESTINATION": dest_of(sound=())}),
        # ⚠️ **語彙の外の種類。** 種類だけでは届かない。
        ("L19 目録に無い種類", real_schemas, True, "語彙に無い",
         {"FIELD_DESTINATION": dest_of(duration="teleport:nowhere")}),
        ("L19 送り先が無い", real_schemas, True, "送り先が無い",
         {"FIELD_DESTINATION": dest_of(motion="edit:")}),
        # ⚠️ **§18 に無いスロットへ送る。** 送り先が実在しなければ届かない。
        ("L19 §18 に無いスロットへ送る", real_schemas, True, "そのスロットは目録に無い",
         {"FIELD_DESTINATION": dest_of(place="prompt:No Such Slot")}),
        # ⚠️ **`take.params` に無い鍵へ送る。**
        ("L19 take.params に無い鍵へ送る", real_schemas, True, "テイクのスキーマに無い",
         {"FIELD_DESTINATION": dest_of(duration="params:nope")}),
        ("L19 目録に無い基盤へ渡す", real_schemas, True, "その基盤は目録に無い",
         {"FIELD_DESTINATION": dest_of(sound="handover:nowhere")}),
        # ⚠️ **経路の欄を宣言したのに、行き先が無い。** 送り口が無ければ届かない。
        ("L19 経路の欄に行き先が無い", real_schemas, True, "行き先が宣言されていない",
         {"FIELD_DESTINATION": {k: v for k, v in specmap.FIELD_DESTINATION.items()
                                if k != "key_image"}}),
        # ⚠️ **理由が無ければ、行き先は後から変えられない。**
        ("L19 理由が書かれていない", real_schemas, True, "理由が書かれていない",
         {"DESTINATION_WHY": {k: v for k, v in specmap.DESTINATION_WHY.items()
                              if k != "sound"}}),
    ]
    for label, sdir, want, fragment, patch in dest_cases:
        saved_patch = {}
        try:
            for k, v in (patch or {}).items():
                saved_patch[k] = getattr(specmap, k)
                setattr(specmap, k, v)
            got = [f for f in semantic.check_field_destination(sdir)
                   if f["severity"] != "note"]
        finally:
            for k, v in saved_patch.items():
                setattr(specmap, k, v)
        n += 1
        ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
        bad += not ok
        print(f"    {label:<46}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **空のスキーマと検査していないか。** 欄が1つも無ければ、すべてが素通りする。
    d = _P(tempfile.mkdtemp())
    (d / "shot-record.schema.json").write_text(
        json.dumps({"type": "object", "properties": {}}), encoding="utf-8")
    (d / "take.schema.json").write_text(
        json.dumps({"properties": {"take": {"properties": {"params":
                   {"properties": {}}}}}}), encoding="utf-8")
    got = semantic.check_field_destination(d)
    n += 1
    ok = any("空のスキーマ" in f["message"] for f in got)
    bad += not ok
    print(f"    {'L19 空のスキーマ＝検査が空になる':<46}{len(got):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
    for f in got[:1]:
        print(f"        {f['code']}  {f['message'][:88]}")

    # ---- L20（`Style Motion` の行き先が空でないか）
    #     ⚠️ **様式カードはこのリポジトリの外にある。** 読めなければ
    #        「確かめられない」と報告する——**確かめていないことを、確かめた顔にしない。**
    print("\n=== 自己検査 — 様式カードの運動イディオム\n")

    def style_proj(style, body):
        d = _P(tempfile.mkdtemp())
        (d / "a.md").write_text(body, encoding="utf-8")
        sh = s("p-ch01-seg01", spec="a.md")
        p = _One(sh)
        p.root = d
        p.shots = {"p-ch01-seg01": sh}
        p.bible = {"bible": {"style": style}}
        return p

    WITH_SLOT = sec18(*SIX, "Style Motion")
    WITHOUT_SLOT = sec18(*SIX)
    cards = semantic._styles_dir(REPO)
    n += 1
    if cards is None:
        # ⚠️ **clone した人には無い。** だから「確かめられない」が正しい答えである。
        got = semantic.check_style_motion(style_proj("luminous-anime", WITH_SLOT))
        ok = any("確かめられない" in f["message"] for f in got)
        bad += not ok
        print(f"    {'L20 カードが読めない＝確かめられないと報告':<46}{len(got):>10}  "
              f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")
    else:
        # ⚠️ **本物のカードを読ませる。** 合成したカードでは、読む側を検査できない。
        has = next((p.stem for p in sorted(cards.glob("*.md"))
                    if "## Motion character" in p.read_text(encoding="utf-8")), None)
        hasnt = next((p.stem for p in sorted(cards.glob("*.md"))
                      if "## Motion character" not in p.read_text(encoding="utf-8")), None)
        print(f"        ← 実測: カード {len(list(cards.glob('*.md')))} 枚。"
              f" `Motion character` を持つ例 `{has}`／持たない例 `{hasnt}`")
        style_cases = [
            # ⚠️ **本命の「鳴ってはならない」例。** 行き先が中身を運ぶ。
            #    ⚠️ カードが1枚も持たなければ、この例は**立てられない**（鳴るはずが無い）。
            *([(f"L20 `{has}` は持つ（鳴ってはならない）", has, WITH_SLOT, False, None)]
              if has else []),
            (f"L20 `{hasnt}` は持たない", hasnt, WITH_SLOT, True, "在るが空である"),
            ("L20 カードが実在しない", "no-such-style-9999", WITH_SLOT, True, "実在しない"),
            # ⚠️ **スロットが1つも無ければ、この検査は何も見ていない。** 黙って通さない。
            ("L20 Style Motion を持つ仕様が無い（鳴ってはならない）",
             hasnt, WITHOUT_SLOT, False, None),
        ]
        for label, style, body, want, fragment in style_cases:
            got = [f for f in semantic.check_style_motion(style_proj(style, body))
                   if f["severity"] != "note"]
            n += 1
            ok = bool(got) == want and (not want or any(fragment in f["message"] for f in got))
            bad += not ok
            print(f"    {label:<46}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
            for f in got[:1]:
                print(f"        {f['code']}  {f['message'][:88]}")

        # ⚠️ **受け火の実物。** 99本が `Style Motion` を持たないので、**ここは鳴らない**
        #    ——だが受け火は `soft-cel-anime`（持つ様式）である。**両方が真である。**
        real_v2 = REPO / "projects" / "ukebi" / "ukebi-v2"
        if real_v2.is_dir():
            p = Project(real_v2)
            got = [f for f in semantic.check_style_motion(p) if f["severity"] != "note"]
            n += 1
            bad += bool(got)
            print(f"    {'L20 受け火 V2（スロットが無いので鳴らない）':<46}{len(got):>10}  "
                  f"{'期待どおり' if not got else '⚠️ 期待と違う'}")

    # ⚠️ **環境変数で指せること。** 隣に無くても、在る場所を教えられる。
    n += 1
    import os as _os
    saved_env = _os.environ.get(semantic.STYLE_CARD_ENV)
    try:
        _os.environ[semantic.STYLE_CARD_ENV] = str(cards or (REPO / "無いディレクトリ"))
        got = semantic._styles_dir(REPO)
        ok = (got is None) if cards is None else (got == cards)
        if cards is None:
            # ⚠️ **指しても、そこに無ければ「確かめられない」。** 嘘をつかない。
            ok = got is None or not Path(got).is_dir()
    finally:
        if saved_env is None:
            _os.environ.pop(semantic.STYLE_CARD_ENV, None)
        else:
            _os.environ[semantic.STYLE_CARD_ENV] = saved_env
    bad += not ok
    print(f"    {'L20 様式の置き場を環境変数で指せる':<46}{'':>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")

    # ---- L21〜L24（画像の経路の中身・尺の一致・`mode` が要求するもの）
    #     ⚠️ **本物の節見出しを書いたファイルを読ませる。** 合成の見出しでは、
    #        節を割る側・語幹を取る側が壊れていても通る（L10・L11 と同じ理由）。
    print("\n=== 自己検査 — 画像の経路の中身と、mode が要求するもの\n")

    # ⚠️ **7欄である。** エンジンは2つの軸を別々に引く——`format` カードが穴を宣言し、
    #    `style` カードも穴を宣言する。実測（2026-09-13）: `scene-board` は5、
    #    `luminous-anime` は4、`ACTION`・`LOCATION` が重なって**和は7**。
    IMG_VARS = ("## 主題（英語・7欄）\n\n"
                "- `SCENE`: the first light finding one shelf\n"
                "- `CHARACTERS`: no figure in frame\n"
                "- `SUBJECT`: a rustic shelf at dawn\n"
                "- `ACTION`: holding still while the light crosses\n"
                "- `LOCATION`: the mill room\n"
                "- `LIGHT`: a low shaft from the window at the frame edge\n"
                "- `ACCENT`: warm gold light\n\n")
    # ⚠️ **`no photorealistic`（台帳）と `not photorealistic`（仕様）を混ぜてある。**
    #    これは**実測で見つかった偽陽性そのもの**であり、**語幹を取らなければ
    #    下の「鳴ってはならない」例が鳴る**——つまりこの例は `_stem` の検査である。
    IMG_BASE = ("no readable text", "no watermark", "no photorealistic")
    IMG_NEG_OK = ("no readable text, no watermark, not photorealistic, "
                  "no on-screen subtitles, no background music, no steam")

    # ⚠️ **カードの実物はこのリポジトリの外にある。** 自己検査が**本物の
    #    `distill-essence-engine` に依存すると、clone した人には通らない。**
    #    だから**同じ形の偽物を組んで**、`repo_root` で指す——
    #    形は `_cards_dir` が読む形（`<repo>/../distill-essence-engine/references/<層>`）。
    def fake_engine(fmt_vars, style_vars, name="scene-board", style_name="luminous-anime"):
        d = _P(tempfile.mkdtemp())
        for sub, nm, vs in (("formats", name, fmt_vars), ("styles", style_name, style_vars)):
            p = d / "distill-essence-engine" / "references" / sub
            p.mkdir(parents=True, exist_ok=True)
            (p / f"{nm}.md").write_text(
                f"# {nm}\n\n## Environment variables\n\n"
                + ", ".join(f"`{v}`" for v in vs) + "\n", encoding="utf-8")
        return d / "repo"

    L22_FIVE = ("SCENE", "CHARACTERS", "ACTION", "LOCATION", "LIGHT")
    L22_FOUR = ("SUBJECT", "ACTION", "LOCATION", "ACCENT")
    ENGINE_OK = fake_engine(L22_FIVE, L22_FOUR)
    # ⚠️ **本物の `illustration` カードと同じ形**（`SUBJECT`・`MOOD` の2つだけ）。
    #    これが「名乗ったカードが、その欄を宣言していない」の実物である。
    ENGINE_WRONG = fake_engine(("SUBJECT", "MOOD"), L22_FOUR)

    def img_spec(negative=IMG_NEG_OK, vars_body=IMG_VARS, ref_format="scene-board",
                 ref_style="luminous-anime"):
        body = f"# 画像仕様\n\n"
        for key, nm in (("REF_FORMAT", ref_format), ("REF_STYLE", ref_style)):
            if nm is not None:
                body += f"- `{key}`: `{nm}`\n"
        # ⚠️ **本物の形である。** 画像の正典は**1つの節の中の2段落**であって、
        #    `Prompt` と `Negative` は**見出しではない**——見出しが本文の間にあると、
        #    著者の1回の選択がそれを巻き込む（`specmap.SPEC_KINDS` の註）。
        #    だからここでも**空行1つ**で2つを並べる。
        #
        # ⚠️ **`negative=None` は「節そのものが無い」**（見出しごと落とす）。
        #    **`negative=""` は「節は在るが Negative が書かれていない」**——
        #    実物ではこちらが起きる形である（`Prompt` を書いて、`Negative` を忘れる）。
        #    **この2つは別の欠陥であり、別の符号で鳴らねばならない。**
        body += "\n" + vars_body
        if negative is None:
            return body
        body += "## 投入する1本の文字列（英語）\n\nA rustic shelf at dawn, one line\n"
        if negative:
            body += f"\n{negative}\n"
        return body

    def img_proj(negative=IMG_NEG_OK, vars_body=IMG_VARS, base=IMG_BASE,
                 mode="motion", video=None, text_channel=None, duration="6s",
                 write_img=True, ref_format="scene-board", ref_style="luminous-anime",
                 waived=None):
        """⚠️ **画像の経路と動画の経路を別々に置く。** 決定（2026-09-13）の標準の形。"""
        d = _P(tempfile.mkdtemp())
        kw = {}
        if write_img:
            (d / "img.md").write_text(img_spec(negative, vars_body, ref_format, ref_style),
                                      encoding="utf-8")
            kw["key_image"] = "img.md"
        if video is not None:
            (d / "vid.md").write_text(video, encoding="utf-8")
            kw["spec"] = "vid.md"
        if text_channel is not None:
            kw["text_channel"] = text_channel
        sh = s("p-ch01-seg01", mode=mode, duration=duration, **kw)
        p = _One(sh)
        p.root = d
        p.shots = {"p-ch01-seg01": sh}
        b = {"negative_base": base}
        if waived is not None:
            b["base_negatives_waived"] = waived
        p.bible = {"bible": b}
        return p

    def video1(dur="6s", line=True):
        head = "# 1. VIDEO\n\n" + (f"- Duration: `{dur}`\n" if line else "- Aspect: 16:9\n")
        return head + "\n" + "".join(f"# {t}\n\n本文\n" for t in ALL20[1:])

    def video11(motion="## Subject Motion\n\nthe dough holds; only the dust drifts\n\n"):
        """⚠️ **本文は小節に在る。** `# 11. MOTION` の直後に `## ` が来る形は
        **実測そのもの**であり、`specdoc.section` では §11 が空に見える——
        だからこの形で「鳴ってはならない」例を作る。"""
        return ("".join(f"# {t}\n\n本文\n" for t in ALL20[:10])
                + "# 11. MOTION\n\n" + motion
                + "".join(f"# {t}\n\n本文\n" for t in ALL20[11:]))

    def run1(label, fn, proj, want, fragment, note=None):
        """⚠️ **註も読む。** 註が出ないことも「違反0件」に見えるからである。"""
        nonlocal n, bad
        got = fn(proj)
        v = [f for f in got if f["severity"] != "note"]
        nts = [f for f in got if f["severity"] == "note"]
        n += 1
        ok = (bool(v) == want
              and (not want or any(fragment in f["message"] for f in v))
              and (note is None or any(note in f["message"] for f in nts)))
        bad += not ok
        head = f"違反 {len(v)} 件" if v else "違反0件"
        print(f"    {label:<50}{head:>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in v[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    run1("L21 禁制を覆っている（鳴ってはならない）", semantic.check_negative_coverage,
         img_proj(), False, None, note="覆っているのは 1/1 本である")
    run1("L21 1節足りない", semantic.check_negative_coverage,
         img_proj(negative="no readable text, not photorealistic"),
         True, "3 節が無い: no watermark")
    # ⚠️ **節は在るのに Negative が無い。** 段落が1つしか無いので、
    #    `Negative` の index は存在しない——**黙って `Prompt` を読んではならない。**
    run1("L21 Negative が書かれていない（1段落）", semantic.check_negative_coverage,
         img_proj(negative=""), True, "1 段落である")
    run1("L21 投入する節が無い", semantic.check_negative_coverage,
         img_proj(negative=None), True, "の節が無い")
    # ⚠️ **段落の数は名乗りである。** 数が違えば `index` は別の段落を指す——
    #    `Negative` を読んだつもりで `Prompt` を読む。だから鳴らねばならない。
    run1("L21 2段落であるはずが3段落", semantic.check_negative_coverage,
         img_proj(negative="no readable text\n\nno watermark, not photorealistic"),
         True, "3 段落である")
    run1("L21 禁制が宣言されていない", semantic.check_negative_coverage,
         img_proj(base=None), True, "作品の禁制が宣言されていない")
    # ⚠️ **相手が無ければ何も言わない。** 「記録が無い」は `L18` が1件に畳む。
    run1("L21 画像の仕様が無い（鳴ってはならない）", semantic.check_negative_coverage,
         img_proj(write_img=False), False, None)

    # ⚠️ **基盤の禁制は、作品が書き忘れても掛かる**（決定 2026-09-18、著者）。
    #    作品が自分の分を全部書いていても、`no on-screen subtitles` が無ければ鳴る
    #    ——**床が無ければ、思い出した者だけが守ることになる。**
    run1("L21 基盤の禁制が無い（作品の分は揃っている）", semantic.check_negative_coverage,
         img_proj(negative="no readable text, no watermark, not photorealistic, no steam"),
         True, "2 節が無い: no on-screen subtitles")

    # ⚠️ **祖父条項**（決定 2026-09-18、著者——「hitosara は対象外にする」）。
    #    基盤の禁制は増える。**規則より前に書かれた作品**は、書いていなかったことを
    #    理由に赤が立つ——**規則は遡らない。** ゆえに作品が除外を宣言する。
    run1("L21 祖父条項で外した節は要求されない", semantic.check_negative_coverage,
         img_proj(negative="no readable text, no watermark, no on-screen subtitles, "
                           "not photorealistic, no steam",
                  waived=["no background music"]),
         False, None, note="祖父条項が掛かっている")
    # ⚠️ **除外できるのは基盤の節だけである。** 作品が自分の禁制を除けば、
    #    この検査は作品の側を何も見ていない——**黙って通してはならない。**
    run1("L21 作品の禁制を除外しようとしている", semantic.check_negative_coverage,
         img_proj(negative=IMG_NEG_OK, waived=["no steam"]),
         True, "基盤の禁制に無い節を名指している")

    # ⚠️ **動画の §18 も見る。** かつては「検査がまだ無い——穴である」と記録されていた。
    #    **その穴から実際の欠陥が出た**（実測 2026-09-18: 動画に中国語の字幕が焼かれた）。
    def vid_spec(negative):
        return ("# 18. WAN 3.0 PROMPT MAPPING\n\n"
                "## Master Prompt\n\n本文\n\n"
                f"## Negative Prompt\n\n{negative}\n\n"
                "# 19. GENERATION INSTANCE\n\n本文\n")

    run1("L21 動画の §18 が覆っていない", semantic.check_negative_coverage,
         img_proj(video=vid_spec("no watermark")),
         True, "動画の §18 Negative が禁制を覆っていない")
    run1("L21 動画の §18 も覆っている（鳴ってはならない）", semantic.check_negative_coverage,
         img_proj(video=vid_spec(IMG_NEG_OK)), False, None)
    run1("L21 動画の §18 に Negative の節が無い", semantic.check_negative_coverage,
         img_proj(video="# 18. WAN 3.0 PROMPT MAPPING\n\n## Master Prompt\n\n本文\n"),
         True, "`## Negative Prompt` の節が無い")

    # ⚠️ **`repo_root` を偽のエンジンへ向ける。** 本物に依存させない。
    l22 = lambda p, eng=ENGINE_OK: semantic.check_image_vars(p, repo_root=eng)

    run1("L22 7欄とも非空（鳴ってはならない）", l22,
         img_proj(), False, None,
         note="7 欄を確かめた")
    run1("L22 欄が1つ無い", l22,
         img_proj(vars_body=IMG_VARS.replace("- `ACCENT`: warm gold light\n", "")),
         True, "無い欄がある: ACCENT")
    run1("L22 欄は在るが空", l22,
         img_proj(vars_body=IMG_VARS.replace("`ACCENT`: warm gold light", "`ACCENT`: ")),
         True, "欄が空である: ACCENT")
    run1("L22 主題の節が無い", l22, img_proj(vars_body=""), True, "の節が無い")
    run1("L22 画像の仕様が無い（鳴ってはならない）", l22,
         img_proj(write_img=False), False, None)

    # ⚠️ **本命。これが実測で見つかった欠陥そのものである。** 4欄しか見ない検査は、
    #    様式カードだけを名乗る画像仕様を**通してしまう**——4欄は最初から埋まっていた。
    #    **名乗りを読まなければ、フォーマットカードの不在は見えない。**
    run1("L22 フォーマットを名乗っていない", l22,
         img_proj(ref_format=None), True, "`REF_FORMAT` を名乗っていない")
    run1("L22 様式を名乗っていない", l22,
         img_proj(ref_style=None), True, "`REF_STYLE` を名乗っていない")
    run1("L22 カードがその欄を宣言していない", lambda p: semantic.check_image_vars(
             p, repo_root=ENGINE_WRONG),
         img_proj(), True, "が宣言していない欄を")
    run1("L22 名乗られたカードが無い", l22,
         img_proj(ref_format="no-such-card"), True, "が無い")
    # ⚠️ **読めないことと、食い違っていることは別である。** 読めなければ註を出す。
    run1("L22 カードが読めない（註・鳴ってはならない）",
         lambda p: semantic.check_image_vars(p, repo_root=_P("/nonexistent/repo")),
         img_proj(), False, None, note="確かめられない")

    run1("L23 尺が一致する（鳴ってはならない）", semantic.check_duration,
         img_proj(video=video1("6s"), duration="6s"), False, None, note="1 本が一致")
    run1("L23 尺が食い違う", semantic.check_duration,
         img_proj(video=video1("10s"), duration="6s"), True, "尺が食い違っている")
    run1("L23 §1 に Duration が無い", semantic.check_duration,
         img_proj(video=video1(line=False)), True, "`Duration:` が無い")
    run1("L23 記録に duration が無い", semantic.check_duration,
         img_proj(video=video1("6s"), duration=None), True, "`duration` が無い")

    # ---- L26（§1 の作品定数が、家 `bible.constants.video` と一致するか）
    #     ⚠️ **この層は、実データでは1件も鳴らない**（40本 × 4欄 = 160回比べて0件）。
    #        だからこそ**自己検査で、鳴る姿を見ておかねばならない**——
    #        **一度も鳴ったのを見ていない検査は、まだ検査ではない。**
    print("\n=== 自己検査 — §1 の作品定数と、その家\n")

    #: ⚠️ **4行とも本物の値である。** 家と §1 の両方が同じ値を持つ形は、実測そのもの。
    L26_ROWS = (("aspect", "Aspect", "16:9"),
                ("resolution", "Resolution", "1920x1080"),
                ("frame_rate", "Frame Rate", "24fps"),
                ("orientation", "Orientation", "Landscape"))

    def l26_home(**over):
        """家。⚠️ **`値=None` は「その欄が無い」**——空文字ではない。**この2つは別である。**"""
        d = {k: v for k, _, v in L26_ROWS}
        for k, v in over.items():
            if v is None:
                d.pop(k, None)
            else:
                d[k] = v
        return {"video": d}

    def l26_spec(**over):
        """§1 に4行を持つ動画仕様。⚠️ **`値=None` は「その行が無い」。**"""
        vals = {k: v for k, _, v in L26_ROWS}
        vals.update(over)
        lines = ["# 1. VIDEO", ""]
        for key, label, _ in L26_ROWS:
            if vals.get(key) is not None:
                lines.append(f"- {label}: `{vals[key]}`")
        return ("\n".join(lines) + "\n\n"
                + "".join(f"# {t}\n\n本文\n" for t in ALL20[1:]))

    def const_proj(spec=None, constants=None):
        """⚠️ **`spec=None` は動画の仕様を書かない。`constants=None` は家を書かない。**
        この2つは**別々に落とせる**——どちらか片方だけが無い形こそが、実測で起きる形である。"""
        d = _P(tempfile.mkdtemp())
        kw = {}
        if spec is not None:
            (d / "vid.md").write_text(spec, encoding="utf-8")
            kw["spec"] = "vid.md"
        sh = s("p-ch01-seg01", mode="motion", duration="6s", **kw)
        p = _One(sh)
        p.root = d
        p.shots = {"p-ch01-seg01": sh}
        p.bible = {"bible": {}}
        if constants is not None:
            p.bible["bible"]["constants"] = constants
        return p

    run1("L26 家と §1 が一致する（鳴ってはならない）", semantic.check_work_constants,
         const_proj(spec=l26_spec(), constants=l26_home()), False, None,
         note="4 件を比較して 4 件が一致")
    run1("L26 作品定数が食い違う", semantic.check_work_constants,
         const_proj(spec=l26_spec(orientation="Portrait"), constants=l26_home()),
         True, "作品定数が食い違っている")
    run1("L26 §1 に Orientation が無い", semantic.check_work_constants,
         const_proj(spec=l26_spec(orientation=None), constants=l26_home()),
         True, "`Orientation:` が無い")
    # ⚠️ **欠けた欄は、ショットごとではなく一度だけ鳴る。** 家の欠けは作品に1つの欠陥である。
    run1("L26 家に frame_rate が無い", semantic.check_work_constants,
         const_proj(spec=l26_spec(), constants=l26_home(frame_rate=None)),
         True, "`frame_rate` が無い")
    # ⚠️ **「相手が空なら鳴る」。** さもなければ、家を消した作品でこの層は**静かに緑になる**
    #    ——`CLAUDE.md`「a check that reports nothing looks like a check that passed」。
    run1("L26 家そのものが無い（他の側は在る）", semantic.check_work_constants,
         const_proj(spec=l26_spec()), True, "家（`bible.constants.video`）が無い")
    # ⚠️ **綴りは2つ在る**（実測: `Aspect Ratio:` が89本、`Aspect:` が10本——後者は
    #    `projects/hitosara` だけである）。片方しか読めなければ、**89本の側が丸ごと読めない。**
    run1("L26 `Aspect Ratio:` の綴りも読む（鳴ってはならない）", semantic.check_work_constants,
         const_proj(spec=l26_spec().replace("- Aspect: ", "- Aspect Ratio: "),
                    constants=l26_home()), False, None, note="4 件を比較して 4 件が一致")
    # ⚠️ **動画の仕様が無ければ、この検査は何も見ていない。** `L11`・`L18` が報告する。
    run1("L26 動画の仕様が無ければ黙る", semantic.check_work_constants,
         const_proj(spec=None, constants=l26_home()), False, None)

    # ---- L27（作品の言語が宣言され、§18 の `Audio Prompt` に届いているか）
    #     ⚠️ **この検査は、この基盤自身の穴から出た。** 実測（2026-09-18）——
    #        発話のある動画に**中国語の字幕が焼かれた。** 作品は言語を
    #        **どこにも書けなかった**（`bible` にも §14 の定義にも欄が無かった）。
    #        **空欄は、生成器の既定で埋まる**——Wan 3.0 の既定は中国語である。
    print("\n=== 自己検査 — 作品の言語と、生成器へ渡る文への到達\n")

    def lang_proj(language=None,
                  audio="The language of this work is Japanese. No dialogue."):
        """⚠️ **`audio=None` は「`Audio Prompt` のスロットが無い」。** `L17` の欠陥であり、
        ここでは鳴らさない——**同じ欠陥を2つの層が別々の符号で報告しない。**"""
        d = _P(tempfile.mkdtemp())
        body = ("# 18. WAN 3.0 PROMPT MAPPING\n\n## Master Prompt\n\n本文\n\n")
        if audio is not None:
            body += f"## Audio Prompt\n\n{audio}\n\n"
        body += ("## Negative Prompt\n\nno watermark, no on-screen subtitles\n\n"
                 "# 19. GENERATION INSTANCE\n\n本文\n")
        (d / "vid.md").write_text(body, encoding="utf-8")
        sh = s("p-ch01-seg01", spec="vid.md")
        p = _One(sh)
        p.root = d
        p.shots = {"p-ch01-seg01": sh}
        p.bible = {"bible": {}}
        if language is not None:
            p.bible["bible"]["language"] = language
        return p

    run1("L27 言語が宣言され、届いている（鳴ってはならない）", semantic.check_work_language,
         lang_proj(language="Japanese"), False, None,
         note="届いているのは 1/1 本である")
    run1("L27 言語が宣言されていない", semantic.check_work_language,
         lang_proj(), True, "作品が言語を宣言していない")
    run1("L27 宣言は在るが、`Audio Prompt` に無い", semantic.check_work_language,
         lang_proj(language="Japanese", audio="No dialogue. Silence, specified."),
         True, "`Audio Prompt` に作品の言語")
    # ⚠️ **スロットが無ければ黙る。** `L17` が「スロットが無い」と報告している。
    run1("L27 `Audio Prompt` が無ければ黙る", semantic.check_work_language,
         lang_proj(language="Japanese", audio=None), False, None)

    # ---- L28（§18 が、その経路のものでない語を運んでいないか）
    #     ⚠️ **この検査の要点は「鳴らない例」のほうである。** 語を足す変更も、
    #        門を外す変更も、**鳴らない例が無ければ自己検査は緑のまま通る**——
    #        `L25` が踏んだ形の事故である。実測（2026-09-20）——`WAN 3.0` の15本が
    #        `one continuous take` を §18 に持ち、**それは正しい**（この経路の家風）。
    print("\n=== 自己検査 — 経路の文法（§18 が、その経路のものでない語を運んでいないか）\n")

    def route_spec(model, slots="本文", problems="本文"):
        """§18 の見出しと `Master Prompt`、そして §20 を差し替えた動画の仕様。"""
        body = "".join(f"# {t}\n\n本文\n" for t in ALL20[:17])
        body += f"# 18. {model} PROMPT MAPPING\n\n## Master Prompt\n\n{slots}\n\n"
        body += "# 19. GENERATION INSTANCE\n\n本文\n"
        return body + f"# 20. ITERATION\n\n## Observed Problems\n\n{problems}\n"

    # 直した3本の §18 が実際に持つ形である（**却下した4語の生きた形**）。
    FIXED = ("the protagonist is kept the same person in every panel; "
             "no additional person beyond the storyboard; "
             "no colleague invented at the counter; "
             "no cuts to unrelated locations; "
             "the atmosphere is the primary mover: particles fall continuously")

    run1("L28 H3 の §18 に `one continuous take`",
         semantic.check_model_route,
         kind_proj(route_spec("MINIMAX H3", "One continuous take of the room.")),
         True, "`one continuous take` が在る")
    run1("L28 H3 の §18 に `never by a cut`",
         semantic.check_model_route,
         kind_proj(route_spec("MINIMAX H3", "Joined by movement, never by a cut.")),
         True, "`never by a cut` が在る")
    run1("L28 H3 の §18 に `one and the same man`",
         semantic.check_model_route,
         kind_proj(route_spec("MINIMAX H3", "keep one and the same man in every panel")),
         True, "`one and the same man` が在る")
    # ⚠️ **門。** 同じ句が `WAN 3.0` の §18 に在るのは正しい——**絞らねば15件の偽陽性。**
    run1("L28 `WAN 3.0` を名乗れば鳴らない（門）", semantic.check_model_route,
         kind_proj(route_spec("WAN 3.0", "One continuous take, never by a cut.")),
         False, None)
    # ⚠️ **§20 は原因として引用している。** ファイル全体を走査すれば、
    #    **直した仕様の上で鳴る**——`L4` が踏んだ形である（`_section_body` が閉じる）。
    run1("L28 §20 が原因として引用していても鳴らない", semantic.check_model_route,
         kind_proj(route_spec("MINIMAX H3", FIXED,
                              problems="Cause: §10 and §18 both said "
                                       "`One continuous take … never by a cut`.")),
         False, None)
    run1("L28 直した H3 の形では鳴らない", semantic.check_model_route,
         kind_proj(route_spec("MINIMAX H3", FIXED)), False, None)
    # ⚠️ **§18 が名乗らない・目録に無いモデルは `L18` の欠陥である。**
    #    **同じ欠陥を2つの層が別々の符号で報告しない。**
    run1("L28 §18 が名乗らなければ黙る", semantic.check_model_route,
         kind_proj(specfile(*ALL20)), False, None)
    run1("L28 目録に無いモデルなら黙る", semantic.check_model_route,
         kind_proj(route_spec("SORA 9", "One continuous take.")), False, None)
    # ⚠️ **動画の仕様が1本も無ければ、1文字も出さない**——**註も出さない。**
    #    それは「確かめて正しい」ではなく**「相手が無い」**である（穴）。
    #    ここだけ `run1` を通さない——**註の不在まで見る**ためである。
    got = semantic.check_model_route(_One(s("p-ch01-seg01")))
    n += 1
    bad += bool(got)
    print(f"    {'L28 動画の仕様が無ければ沈黙する（註も無い）':<50}"
          f"{len(got):>10}  {'期待どおり' if not got else '⚠️ 期待と違う'}")

    # ⚠️ **目録そのものが壊れているときは、本文を走査しない。**
    #    **空の語は、どの §18 にも当たる**——走査すれば**直した仕様の上で鳴る。**
    saved_route = specmap.MODEL_ROUTE
    try:
        specmap.MODEL_ROUTE = {"WAN 3.0": ()}
        run1("L28 目録に動画の経路が欠けている", semantic.check_model_route,
             kind_proj(route_spec("MINIMAX H3")), True, "鍵が")
        specmap.MODEL_ROUTE = {"WAN 3.0": (), "MINIMAX H3": (("", "理由"),)}
        run1("L28 目録に空の語が在る（本文を読まない）", semantic.check_model_route,
             kind_proj(route_spec("MINIMAX H3", "One continuous take.")),
             True, "本文を1行も読んでいない")
        specmap.MODEL_ROUTE = {"WAN 3.0": (), "MINIMAX H3": (("no cut", ""),)}
        run1("L28 目録の語に理由が無い", semantic.check_model_route,
             kind_proj(route_spec("MINIMAX H3")), True, "理由が無い")
    finally:
        specmap.MODEL_ROUTE = saved_route

    # ⚠️ **実物で鳴らないこと。** 合成データだけで通る検査は、現場で鳴る。
    for label, rel, note in (("promo-chinatsu の5本（WAN・鳴ってはならない）",
                              "projects/habits-promo-chinatsu", None),
                             ("hitosara の10本（WAN・鳴ってはならない）",
                              "projects/hitosara", None),
                             ("habits の3本（H3・註だけである）",
                              "projects/habits", "突き合わせた")):
        rp = REPO / rel
        if not rp.is_dir():
            continue
        run1(f"L28 {label}", semantic.check_model_route, Project(rp), False, None, note=note)

    # ---- L29（この走りが読まない作品を名指しするか）
    #     ⚠️ **走査はディスクを見る。** 合成の辞書では代われない——
    #        実物のディレクトリを切って鳴らす。
    def nested_proj(names=("child",), ledger=True, is_work=True):
        d = _P(tempfile.mkdtemp())
        for nm in names:
            sub = d / nm
            sub.mkdir(parents=True, exist_ok=True)
            (sub / "bible.yaml").write_text("project: x\nbible: {}\n", encoding="utf-8")
            if ledger:
                (sub / "ledger.yaml").write_text("x: 1\n", encoding="utf-8")
        p = _One(s("p-ch01-seg01", mode="motion"))
        p.root = d
        p.bible = {"project": "p", "bible": {}} if is_work else None
        return p

    run1("L29 作品が作品を抱えている", semantic.check_nested_works,
         nested_proj(), True, "作品を抱えている")
    run1("L29 題材の置き場が作品を抱えている", semantic.check_nested_works,
         nested_proj(is_work=False), False, None, note="1 本在る")
    # 2段下でも見つける——**作品の中を降りる。** 降りなければ、
    # 「作品が作品を抱えている」を一度も見ない（掛けたい相手はそこにしか居ない）。
    run1("L29 2段下の作品も名指しする", semantic.check_nested_works,
         nested_proj(names=("a/b",), is_work=False), False, None, note="1 本在る")
    run1("L29 4本在れば畳む", semantic.check_nested_works,
         nested_proj(names=("a", "b", "c", "d")), True, "ほか 1 本")

    # ⚠️ **鳴らない例を3つ。** ここだけ `run1` を通さない——**註の不在まで見る**ためである
    #    （註が出ないことも「違反0件」に見える）。
    for label, proj in (
            ("L29 下に作品が無ければ沈黙する（註も無い）",
             nested_proj(names=(), is_work=False)),
            ("L29 `bible.yaml` だけでは作品ではない（註も無い）",
             nested_proj(ledger=False, is_work=False)),
            ("L29 台帳の無い `bible.yaml` は作品ではない（註も無い）",
             nested_proj(names=("a", "b"), ledger=False, is_work=False))):
        got = semantic.check_nested_works(proj)
        n += 1
        bad += bool(got)
        print(f"    {label:<50}{len(got):>10}  "
              f"{'期待どおり' if not got else '⚠️ 期待と違う'}")

    # ⚠️ **実物で鳴ること・鳴らないこと。**
    #    ⚠️ **相手が無ければ黙って飛ばさない**——**「検査しなかった」を緑に数えれば、
    #       自己検査は緑のまま何も見ていない**（`空の検査は OK と言う`）。
    for label, rel, want_note in (
            ("L29 実物 ukebi（題材が作品を抱える・註1件）", "projects/ukebi", "1 本在る"),
            ("L29 実物 gozen-niji（題材だけ・沈黙）", "projects/gozen-niji", None),
            ("L29 実物 hitosara（下に作品が無い・沈黙）", "projects/hitosara", None),
            ("L29 実物 habits（直下へ出した後・沈黙）", "projects/habits", None),
            ("L29 実物 habits-promo-chinatsu（直下へ出した）",
             "projects/habits-promo-chinatsu", None)):
        rp = REPO / rel
        n += 1
        if not rp.is_dir():
            bad += 1
            print(f"    {label:<50}{'相手が無い':>10}  "
                  f"⚠️ 期待と違う（実物が無い——この1本は走っていない）")
            continue
        got = semantic.check_nested_works(Project(rp))
        v = [f for f in got if f["severity"] != "note"]
        nts = [f for f in got if f["severity"] == "note"]
        ok = (not v and len(nts) == (1 if want_note else 0)
              and (not want_note or any(want_note in f["message"] for f in nts)))
        bad += not ok
        print(f"    {label:<50}{f'違反{len(v)}/註{len(nts)}':>10}  "
              f"{'期待どおり' if ok else '⚠️ 期待と違う'}")

    # ---- L25（テイクがショット・様式・**実物**と突き合っているか）
    #     ⚠️ **`S1` は形を見る。ここは中身を見る。** 13本がスキーマを通ることは、
    #        その13本が何かについて正しいことを、何も言わない。
    print("\n=== 自己検査 — テイク（実物と仕様の突き合わせ）\n")

    def video_full(dur="6s", fps="24fps", res="1920x1080", ver=None):
        head = ("# 1. VIDEO\n\n"
                f"- Duration: `{dur}`\n- Aspect: `16:9`\n"
                f"- Resolution: `{res}`\n- Frame Rate: `{fps}`\n")
        body = head + "\n" + "".join(f"# {t}\n\n本文\n" for t in ALL20[1:])
        if ver:
            body += f"\n# 19. GENERATION INSTANCE\n\n- Specification Version: `{ver}`\n"
        return body

    def take_doc(shot="p-ch01-seg01", kind="video", index=1, model="WAN 3.0",
                 measured=None, adopted=None, source="vid.md", sver=None):
        tk = {"shot": shot, "kind": kind, "index": index,
              "provider": {"model": model},
              "params": {"source": source},
              "verdict": {"machine": {"measured": dict(measured or {})}}}
        if sver:
            tk["params"]["source_version"] = sver
        if adopted is not None:
            tk["adopted"] = adopted
        return {"take": tk}

    def take_proj(docs, **kw):
        p = img_proj(**kw)
        p.takes = {}
        for d in docs:
            p.takes.setdefault(d["take"]["shot"], []).append(d)
        return p

    M_OK = {"width": 1920, "height": 1080, "frame_rate": 24,
            "frames": 144, "duration": 6.0}

    run1("L25 実測が仕様と一致する（鳴ってはならない）", semantic.check_take,
         take_proj([take_doc(measured=M_OK)], video=video_full()), False, None,
         note="実測を突き合わせた")

    run1("L25 フレームレートが食い違う", semantic.check_take,
         take_proj([take_doc(measured={**M_OK, "frame_rate": 30})],
                   video=video_full()), True, "フレームレートが食い違っている")

    run1("L25 解像度が食い違う", semantic.check_take,
         take_proj([take_doc(measured={**M_OK, "width": 1672, "height": 941})],
                   video=video_full()), True, "解像度が食い違っている")

    run1("L25 尺が食い違う（許容は1フレーム）", semantic.check_take,
         take_proj([take_doc(measured={**M_OK, "duration": 4.0})],
                   video=video_full()), True, "尺が食い違っている")

    run1("L25 1フレームの違いは鳴らない", semantic.check_take,
         take_proj([take_doc(measured={**M_OK, "duration": 6.0 + 1 / 24})],
                   video=video_full()), False, None, note="実測を突き合わせた")

    run1("L25 目録に無いモデル", semantic.check_take,
         take_proj([take_doc(model="SOME OTHER MODEL", measured=M_OK)],
                   video=video_full()), True, "`MODELS` に無い")

    run1("L25 経路がモデルと食い違う", semantic.check_take,
         take_proj([take_doc(kind="image", model="WAN 3.0", measured={})],
                   video=video_full()), True, "経路が食い違っている")

    run1("L25 存在しないショット", semantic.check_take,
         take_proj([take_doc(shot="p-ch01-seg99", measured=M_OK)],
                   video=video_full()), True, "存在しないショット")

    run1("L25 通し番号の重複", semantic.check_take,
         take_proj([take_doc(measured=M_OK), take_doc(measured=M_OK)],
                   video=video_full()), True, "2本以上ある")

    run1("L25 採用が2本", semantic.check_take,
         take_proj([take_doc(index=1, measured=M_OK, adopted=True),
                    take_doc(index=2, measured=M_OK, adopted=True)],
                   video=video_full()), True, "採用は1本である")

    run1("L25 正典が失われている", semantic.check_take,
         take_proj([take_doc(source="missing.md", measured=M_OK)],
                   video=video_full()), True, "そのファイルが無い")

    run1("L25 仕様が後に直っている（註であって違反ではない）", semantic.check_take,
         take_proj([take_doc(measured=M_OK, sver="0.1.0")],
                   video=video_full(ver="0.1.1")), False, None,
         note="仕様が生成のあとに直っている")

    run1("L25 テイクが空なら何も言わない", semantic.check_take,
         take_proj([], video=video_full()), False, None)

    # ⚠️ **註の内訳を読む。** 註は「違反0件」の中に隠れる——**数え間違えた註は、
    #    違反が0件であることと見分けがつかない。** だから数える側を検査する。
    #    ⚠️ **同じショットに2本在るときが本命である。** 種別ごとの本数を
    #    `(shot, kind)` で数えれば1本になる——**その註は自分の本文と食い違う。**
    for label, docs, want in [
        ("L25 註の内訳はテイクの本数を数える",
         [take_doc(kind="image", model="CHATGPT IMAGE 2.5", index=1,
                   measured={"width": 1672, "height": 941}),
          take_doc(kind="image", model="CHATGPT IMAGE 2.5", index=2,
                   measured={"width": 1672, "height": 941}),
          take_doc(measured=M_OK)],
         "`image` 2 本／`video` 1 本"),
        ("L25 註の内訳は動画も数える",
         [take_doc(index=1, measured=M_OK), take_doc(index=2, measured=M_OK)],
         "`image` 0 本／`video` 2 本"),
    ]:
        n += 1
        got = semantic.check_take(take_proj(docs, video=video_full()))
        nts = [f for f in got if f["severity"] == "note" and "テイク" in f["message"]]
        ok = (len(nts) == 1 and want in nts[0]["message"]
              and not [f for f in got if f["severity"] != "note"])
        bad += not ok
        print(f"    {label:<44}{f'註 {len(nts)} 件':>10}  "
              f"{'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in nts[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    TC = [{"t": "0-4", "kind": "overlay", "content": "分量"}]
    run1("L24 motion は何も要求しない（鳴ってはならない）", semantic.check_mode_demands,
         img_proj(mode="motion", video=video11()), False, None,
         note="`mode` が要求するものを確かめた")
    # ⚠️ **本命。** §11 の本文は小節に在る——`_section_body` が無ければ空に見える。
    run1("L24 still で §11 が非空（鳴ってはならない）", semantic.check_mode_demands,
         img_proj(mode="still", video=video11()), False, None)
    run1("L24 still で §11 が空", semantic.check_mode_demands,
         img_proj(mode="still", video=video11(motion="\n")), True, "は §11 を要求する")
    run1("L24 composite で text_channel が空", semantic.check_mode_demands,
         img_proj(mode="composite", video=video11()), True, "`text_channel` を要求する")
    run1("L24 composite で text_channel 在り（鳴ってはならない）",
         semantic.check_mode_demands,
         img_proj(mode="composite", video=video11(), text_channel=TC), False, None)
    # ⚠️ **逆向きは成り立たない。** `motion` のショットも `text_channel` を持てる。
    run1("L24 motion は text_channel を要求しない（鳴ってはならない）",
         semantic.check_mode_demands,
         img_proj(mode="motion", video=video11(), text_channel=None), False, None)
    run1("L24 動画の仕様が無い（鳴ってはならない）", semantic.check_mode_demands,
         img_proj(mode="still"), False, None)

    # ⚠️ **目録そのものが閉じているか。** 要求を書いていない `mode` は、
    #    何も要求しない `mode` と区別がつかない——**空と、無いことは違う。**
    saved_demands = specmap.MODE_DEMANDS
    try:
        specmap.MODE_DEMANDS = {k: v for k, v in saved_demands.items() if k != "motion"}
        run1("L24 目録が閉じていない（motion の行が無い）", semantic.check_mode_demands,
             img_proj(), True, "鍵が一致しない")
    finally:
        specmap.MODE_DEMANDS = saved_demands
    try:
        specmap.MODE_DEMANDS = {**saved_demands, "still": ("teleport:nowhere",)}
        run1("L24 知らない要求", semantic.check_mode_demands,
             img_proj(mode="still", video=video11()), True, "知らない要求は、確かめられないまま通る")
    finally:
        specmap.MODE_DEMANDS = saved_demands

    # ⚠️ **欄の目録が空なら、L22 は何も確かめない。** 黙って通さない。
    saved_img = specmap.SPEC_KINDS["image"]
    try:
        specmap.SPEC_KINDS = {**specmap.SPEC_KINDS,
                              "image": {**saved_img, "vars": None}}
        run1("L22 欄が宣言されていない", l22,
             img_proj(), True, "が画像の仕様の欄を宣言していない")
    finally:
        specmap.SPEC_KINDS = {**specmap.SPEC_KINDS, "image": saved_img}

    print("\n=== 自己検査 — 形（スキーマ）が鳴るか\n")
    class _Shape:
        bible = ledger = None
        takes = {}

        def __init__(self, shot):
            self.shots = {shot["shot"]: shot}

    def shape(shot, schema_dir):
        return validate_shape(_Shape(shot), str(schema_dir))

    schemas = REPO / "schemas"

    got = shape(dict(clean), schemas)
    n += 1
    bad += bool(got)
    print(f"    {'S1 正しい記録は鳴らない':<44}{len(got):>10}  "
          f"{'期待どおり' if not got else '⚠️ 期待と違う'}")

    for label, key, val, frag in (
            ("S1 必須欄が空", "role", "", "should be non-empty"),
            ("S1 enum の外", "mode", "wrong", "is not one of"),
            ("S1 必須欄が無い", "role", None, "'role' is a required property")):
        r = dict(clean)
        if val is None:
            r.pop(key, None)
        else:
            r[key] = val
        got = shape(r, schemas)
        n += 1
        ok = any(frag in f["message"] for f in got)
        bad += not ok
        print(f"    {label:<44}{len(got):>10}  {'期待どおり' if ok else '⚠️ 期待と違う'}")
        for f in got[:1]:
            print(f"        {f['code']}  {f['message'][:88]}")

    # ⚠️ **検査が空になる側。** スキーマが短ければ、空の必須欄は素通りする。
    #    L11 が「目録が短くても鳴る」ことを見るのと、同じ形である。
    d = _P(tempfile.mkdtemp())
    (d / "shot-record.schema.json").write_text(
        json.dumps({"type": "object", "properties": {"role": {"type": "string"}}}),
        encoding="utf-8")
    empty_role = dict(clean, role="")
    n += 1
    short = shape(empty_role, d)
    bad += bool(short)
    print(f"    {'S1 スキーマが短いと、空の必須欄は素通りする':<44}{len(short):>10}  "
          f"{'期待どおり' if not short else '⚠️ 期待と違う'}")
    print(f"        ← **これが「検査が空になる」である。**"
          f" 同じ記録が本物のスキーマでは {len(shape(empty_role, schemas))} 件鳴る。")

    # ⚠️ **スキーマそのものが無い場合。** S0 が鳴る（黙って飛ばさない）。
    got = shape(dict(clean), d / "無いディレクトリ")
    n += 1
    ok = any(f["code"] == "S0" for f in got)
    bad += not ok
    print(f"    {'S0 スキーマが無い＝検査が空になる':<44}{len(got):>10}  "
          f"{'期待どおり' if ok else '⚠️ 期待と違う'}")

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
    return report(p, semantic.run(p, a.schemas, repo_root=REPO),
                  validate_shape(p, a.schemas))


if __name__ == "__main__":
    sys.exit(main())
