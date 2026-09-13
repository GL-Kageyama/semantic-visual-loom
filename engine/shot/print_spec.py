#!/usr/bin/env python3
"""print_spec.py — **仕様の骨を刷る。** 記録・台帳・作品台帳から、導出できる行だけを。

    使い方:  python3 engine/shot/print_spec.py projects/<project>
             python3 engine/shot/print_spec.py projects/<project> --shot <shot-id>

⚠️ **これは読み取り専用である。** 1バイトも書かない——`projects/` にも、仕様にも、
   どこにも。**刷られた行を貼るのは著者である。**

⚠️ **刷るのは「導出できる行」だけである。** 仕様の1割にも満たない。
   覆わない範囲は、ショットごとに**この道具が自分で申告する**——
   **数は、数えた範囲の広さしか持たない。**

⚠️ **刷った行は、写すと検査が黙る。** だから行ごとに「**これを写すと、どの検査が黙るか**」を
   添える。**この道具の値打ちは、行を埋めることではなく、どこが自動で埋まるかを示すことにある。**
   手で写した行は、写し元が動いても**誰も鳴らさない**——`L23`・`L26` が在るのは、
   その行については**それが鳴るから**である。

⚠️ **§6 は導出しない。** 形が作品ごとに別物である（実測は `engine/shot/README.md`）——
   **安定していない欄を導出すれば、この道具は作品ごとに嘘をつく。**
"""

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

# ⚠️ **読み手を新しく書かない。** `engine/ledger` の `Project`・`specmap` を
#    そのまま使う——同じ記録を読む者が2人いれば、**片方だけ直したときに食い違う。**
sys.path.insert(0, str(HERE.parent / "ledger"))

try:
    import yaml  # noqa: F401  （`check`・`semantic` が要る）
except ImportError:
    sys.exit("PyYAML が要る: python3 -m pip install --user pyyaml")

import check     # noqa: E402  ⚠️ `Project` はここに在る（読み込みの正典）
import semantic  # noqa: E402
import specmap   # noqa: E402


#: §19 が名乗る同一性。⚠️ **`L13` と同じ形で読む**（あちらは接尾辞を剥がして比べる）。
INSTANCE_LINE = re.compile(r"^-\s*Instance ID:\s*`([^`]*)`", re.M)

#: ⚠️ **導出しないものの一覧。** 「刷らない」ではなく「**刷らないと書く**」——
#:    黙って省けば、著者は**忘れられているのか導出できないのか区別できない。**
NOT_DERIVED = (
    "§2 WORLD", "§3", "§4", "§5", "§7", "§8", "§9", "§10", "§11", "§12", "§13",
    "§14 DIALOGUE", "§15", "§16", "§17", "§18（7スロット）", "§20",
)


def derivable(project, shot):
    """そのショットについて**導出できる行**。⚠️ **導出できない行を空で埋めない。**

    ⚠️ **空欄は「書かれていない」と読まれる**——そして `L0` は「空を OK と言わない」と定めた。
    だからここは、**値が無い行を `missing` として持ち上げる**のであって、空文字にしない。
    """
    bible = (project.bible or {}).get("bible") or {}
    home = ((bible.get("constants") or {}).get("video")) or {}
    rows = []

    for key, _, label in specmap.VIDEO_CONSTANTS:
        rows.append({
            "section": "§1 VIDEO",
            "key": key,
            "label": label,
            "value": home.get(key) if key in home else None,
            "source": f"bible.constants.video.{key}",
            "check": "L26",
            "note": None,
        })

    rows.append({
        "section": "§1 VIDEO",
        "key": "Duration",
        "label": "Duration",
        "value": shot.get("duration"),
        "source": "shot.duration",
        "check": "L23",
        "note": "尺は**従属変数**である——作品定数ではなく、ショットごとに決まる。",
    })

    rows.append({
        "section": "§19 GENERATION INSTANCE",
        "key": "Instance ID",
        "label": "Instance ID",
        "value": shot.get("shot"),
        "source": "shot.shot（＋ 末尾 `-<seconds>s-<take>`）",
        "check": "L13",
        "note": "⚠️ 末尾の `-<seconds>s-` を**見ている者は、いない**"
                "（`L13` は接尾辞を剥がして比べる）。",
    })
    return rows


def actual_lines(spec_path):
    """仕様が**いま言っている**値。⚠️ **仕様が無ければ `None`**——`{}` ではない。

    ⚠️ **「仕様が無い」と「仕様にその行が無い」は別である**（`L23` と同じ規律）。
    前者は `None`、後者は `""` で表す。
    """
    if spec_path is None or not Path(spec_path).is_file():
        return None
    s1 = semantic._section_body(spec_path, "1.")
    s19 = semantic._section_body(spec_path, "19.")
    out = {}
    for key, line, _ in specmap.VIDEO_CONSTANTS:
        m = line.search(s1 or "")
        out[key] = m.group(1).strip() if m else ""
    m = specmap.DURATION_LINE.search(s1 or "")
    out["Duration"] = m.group(1).strip() if m else ""
    m = INSTANCE_LINE.search(s19 or "")
    out["Instance ID"] = m.group(1) if m else ""
    return out


def nonblank(path):
    try:
        return sum(1 for ln in Path(path).read_text(encoding="utf-8").splitlines() if ln.strip())
    except (OSError, UnicodeDecodeError):
        return 0


def verdict(row, actual):
    """⚠️ **どちらが正しいかは決めない。** 両方を出すだけである（`L25` と同じ立場）。

    ⚠️ **`key` で引く。** `label` は人が読む名前であり、**引く鍵ではない**——
    ここを取り違えれば、この道具は `L26` と**逆のことを言う**（実際に一度そうなった）。
    """
    if actual is None:
        return "仕様がまだ無い"
    if row["value"] is None:
        return "**導出できない**（家に無い）"
    got = actual.get(row["key"], "")
    if not got:
        return f"**仕様に `{row['label']}:` が無い**"
    if row["key"] == "Instance ID":
        # ⚠️ **接尾辞は比較から外す。** `L13` と同じ扱いである。
        if semantic.TAKE_SUFFIX.sub("", got) == row["value"]:
            return "一致（末尾の接尾辞は除いて比べた）"
        return f"**食い違い: 仕様は `{got}`**"
    if str(row["value"]).strip() == got:
        return "一致"
    return f"**食い違い: 仕様は `{got}`**"


def show(project, sid, index):
    shot = project.shots[sid]
    src = semantic._spec_of(shot, "video")
    spec_path = (project.root / src) if src else None
    exists = spec_path is not None and Path(spec_path).is_file()
    rows = derivable(project, shot)
    actual = actual_lines(spec_path)

    total = nonblank(spec_path) if exists else 0
    print(f"--- {sid}")
    if src:
        print(f"    spec: {src}" + (f"  （空行を除いて {total} 行）" if exists else "  ⚠️ まだ無い"))
    else:
        print("    spec: ⚠️ 記録に `spec:` が無い")

    if exists:
        print(f"\n    ⚠️ **導出できるのは、この仕様の {len(rows)} 行である**"
              f"（空行を除く {total} 行のうち）。")
        print(f"       覆わない（著者が書く）: {'・'.join(NOT_DERIVED)}")
        print("       §6 REFERENCES は**導出しない**——形が作品ごとに別物である（README）。")
    print()

    section = None
    for r in rows:
        if r["section"] != section:
            section = r["section"]
            print(f"    {section}")
        val = f"`{r['value']}`" if r["value"] is not None else "**(無い)**"
        print(f"      - {r['label']}: {val}")
        line = f"          ← {r['source']} · {verdict(r, actual)} · 写すと {r['check']} が黙る"
        print(line)
        if r["note"]:
            print(f"          {r['note']}")
    if index < len(project.order()):
        print()


def main():
    ap = argparse.ArgumentParser(
        description="仕様の骨を刷る — 導出できる行と、それを写すと黙る検査")
    ap.add_argument("project", help="projects/<project> のパス")
    ap.add_argument("--shot", help="このショットだけを刷る")
    a = ap.parse_args()

    root = Path(a.project)
    if not root.is_dir():
        sys.exit(f"{root} が無い")
    project = check.Project(root)

    # ⚠️ **読めなかったことを黙らない。** 空の台帳は「0件」として通り、
    #    **「0件だから正しい」と読まれる**——`_load` が `Unreadable` を投げる理由である。
    for e in project.read_errors:
        print(f"⚠️ {e}", file=sys.stderr)
    if not project.bible:
        print("⚠️ bible.yaml が無い——§1 の作品定数は、どこからも導出できない。",
              file=sys.stderr)

    order = project.order()
    if not order:
        sys.exit(f"{root} にショットが1本も無い"
                 "（⚠️ **「0件」は「違反0件」ではない**——`L0` が鳴らす形である）")

    if a.shot:
        if a.shot not in project.shots:
            sys.exit(f"{a.shot} は無い。在るもの: {', '.join(order)}")
        order = [a.shot]

    if len(order) > 1:
        print(f"{project.name} — {len(order)} 本\n")
    for i, sid in enumerate(order, 1):
        show(project, sid, i)

    print("⚠️ **この道具は、何も決めない。** 導出できる行を示し、"
          "食い違いがあれば**両方を並べる**だけである。")
    print("   貼るかどうかは、著者が決める。")


if __name__ == "__main__":
    sys.exit(main())
