#!/usr/bin/env python3
"""camera.py — **技法を引く。** 目録から、そのショットに使える動きを刷る。

    使い方:  python3 engine/shot/camera.py --role 情景
             python3 engine/shot/camera.py --role 情景 --motion 停止
             python3 engine/shot/camera.py --job 確立 --position 頭
             python3 engine/shot/camera.py --id 007
             python3 engine/shot/camera.py --name クレーンアップ

⚠️ **読み取り専用である。** 1バイトも書かない——目録にも、作品にも、どこにも。

⚠️ **これは献立ではなく地図である。** 絞り込みは「この role に使える動き」を並べるが、
   **どれを選ぶかはショットが決める**——`roles` は担える仕事の集合であって、決定ではない。
   目録は全件 `status: draft` であり、**作品の使い方が食い違えば、作品が勝つ。**

⚠️ **`en` の行が、§18 へ運ぶ文字列である。** 技法の名は生成器へ渡らない——
   `skills/staging/SKILL.md` の第5段が、この目録を先に読むよう定めている。
   §18 が名乗った句は `L54` が目録へ当てる（`--id` で確かめられる）。
"""

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

# ⚠️ **読み手を新しく書かない。** 目録を読む器は `engine/ledger/camera.py` に在る。
sys.path.insert(0, str(HERE.parent / "ledger"))

import camera  # noqa: E402

#: `--role` に限定つきの綴り（`情景（establishing）`）を渡されたときの切り方。
QUALIFIER = "（"


def _base_role(value):
    return str(value or "").split(QUALIFIER)[0].strip()


def select(entries, role=None, motion=None, job=None, position=None,
           tid=None, name=None):
    """目録を絞る。**与えられた条件のすべて**を満たすものだけを返す。

    ⚠️ **`motion` は1つの型として当てる。** `停止・微細運動` のような複合は、
    目録では2つの並びであり、**`・` で割った1つずつが当たる**——
    `機械・乗物` は名前自体が `・` を含むので、**割らずに先に丸ごと当てる**
    （`L53` と同じ規律）。
    """
    out = []
    for key, item in entries.items():
        if tid is not None and str(item.get("id") or key) != tid:
            continue
        if name is not None and name not in str(item.get("name") or ""):
            continue
        if role is not None and _base_role(role) not in (item.get("roles") or []):
            continue
        if motion is not None:
            patterns = item.get("motion_pattern") or []
            if motion not in patterns:
                continue
        directing = item.get("directing") or {}
        if job is not None and job not in (directing.get("job") or []):
            continue
        if position is not None and position not in (directing.get("position") or []):
            continue
        out.append(item)
    return sorted(out, key=lambda e: str(e.get("id") or ""))


def _one(item):
    lines = [f"{item.get('id')} {item.get('name')}"]
    lines.append(f"  en: {' / '.join(item.get('en') or [])}")
    lines.append(f"  運動: {'・'.join(item.get('motion_pattern') or []) or '—'}"
                 f"   移動: {'する' if item.get('travels') else 'しない'}"
                 f"   status: {item.get('status')}")
    lines.append(f"  roles: {'・'.join(item.get('roles') or [])}")
    lines.append(f"  functions: {'・'.join(item.get('functions') or [])}")
    grams = item.get("grammars") or []
    lines.append("  grammar: "
                 + ("・".join(f"{g.get('card')}（{g.get('confidence')}）" for g in grams)
                    if grams else "—"))
    d = item.get("directing") or {}
    lines.append(f"  directing: {'・'.join(d.get('job') or [])}"
                 f" / 相手: {'・'.join(d.get('pairs_with') or [])}"
                 f" / 位置: {'・'.join(d.get('position') or [])}")
    lines.append(f"  physical: {item.get('physical')}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(
        description="カメラ技法の目録から、条件に合う動きを刷る（読み取り専用）")
    ap.add_argument("--role", help="そのショットの role（15の種別の1つ）")
    ap.add_argument("--motion", help="MOTION_PATTERNS の1つ（例: 停止）")
    ap.add_argument("--job", help="演出上の仕事（8つのうち1つ。例: 確立）")
    ap.add_argument("--position", help="場面の位置（頭・中・尾・つなぎ・全編）")
    ap.add_argument("--id", help="技法の id（3桁。例: 007）")
    ap.add_argument("--name", help="技法和名の一部（例: クレーン）")
    args = ap.parse_args()

    if not any([args.role, args.motion, args.job, args.position,
                args.id, args.name]):
        ap.error("絞り込みを1つ以上渡すこと（--role / --motion / --job / "
                 "--position / --id / --name）")

    entries, where, problem = camera.catalog(REPO)
    if problem:
        sys.exit(f"カメラの目録が読めない（{problem}）: {where}")

    hits = select(entries, role=args.role, motion=args.motion, job=args.job,
                  position=args.position,
                  tid=args.id, name=args.name)
    print(f"=== カメラ技法 — {len(hits)}件 / 目録 {len(entries)}件（{where}）\n")
    for item in hits:
        print(_one(item))
        print()
    if not hits:
        print("**条件に合う技法が無い。** ⚠️ **目録が空なのではなく、"
              "この組み合わせが無い**——条件を1つ外して引き直すこと。\n")
    print("⚠️ **目録は草案（status: draft）である。** `roles` は担える仕事の集合であり、"
          "決定ではない——**どれを選ぶかはショットが決める。**\n"
          "⚠️ **§18 へ運ぶのは `en` の行である。** 技法の名は生成器へ渡らない。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
