#!/usr/bin/env python3
"""look.py — **技法を引く。** 目録から、条件に合うものを刷る。

    使い方:  python3 engine/shot/look.py --light --role 情景
             python3 engine/shot/look.py --light --kind 自然 --function 設定
             python3 engine/shot/look.py --light --job 時間 --position 頭
             python3 engine/shot/look.py --light --id 055
             python3 engine/shot/look.py --light --name ゴールデン

⚠️ **読み取り専用である。** 1バイトも書かない——目録にも、作品にも、どこにも。

⚠️ **これは献立ではなく地図である。** 絞り込みは「この role に使える光」を並べるが、
   **どれを選ぶかはショットが決める**——`roles` は担える仕事の集合であって、決定ではない。
   目録は全件 `status: draft` であり、**作品の使い方が食い違えば、作品が勝つ。**

⚠️ **§13 へ運ぶのは `en` の行である。** 技法の名は生成器へ渡らない——
   §13 が名乗った句は `L56` が目録へ当てる（`--id` で確かめられる）。
   ⚠️ **光の名は名詞ゆえ、`L56` は活用を許さない**——`en` をそのまま書くこと。

⚠️ **軸はまだ1つである。** `--light` だけ。`--style`・`--composition` は
   それぞれの目録ができたときに足す——**空の軸を先に作らない**（空は「0件だから正しい」に見える）。
"""

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

# ⚠️ **読み手を新しく書かない。** 目録を読む器は `engine/ledger/lighting.py` に在る。
sys.path.insert(0, str(HERE.parent / "ledger"))

import lighting  # noqa: E402

#: `--role` に限定つきの綴り（`情景（establishing）`）を渡されたときの切り方。
QUALIFIER = "（"


def _base_role(value):
    return str(value or "").split(QUALIFIER)[0].strip()


def select(entries, role=None, function=None, job=None, position=None,
           kind=None, tid=None, name=None):
    """目録を絞る。**与えられた条件のすべて**を満たすものだけを返す。"""
    out = []
    for key, item in entries.items():
        if tid is not None and str(item.get("id") or key) != tid:
            continue
        if name is not None and name not in str(item.get("name") or ""):
            continue
        if kind is not None and item.get("kind") != kind:
            continue
        if role is not None and _base_role(role) not in (item.get("roles") or []):
            continue
        if function is not None and function not in (item.get("functions") or []):
            continue
        directing = item.get("directing") or {}
        if job is not None and job not in (directing.get("job") or []):
            continue
        if position is not None and position not in (directing.get("position") or []):
            continue
        out.append(item)
    return sorted(out, key=lambda e: str(e.get("id") or ""))


def _one(item):
    lines = [f"{item.get('id')} {item.get('name')}（{item.get('kind')}）"]
    lines.append(f"  en: {' / '.join(item.get('en') or [])}")
    lines.append(f"  roles: {'・'.join(item.get('roles') or [])}"
                 f"    functions: {'・'.join(item.get('functions') or [])}")
    grams = item.get("grammars") or []
    lines.append("  grammar: "
                 + ("・".join(f"{g.get('card')}（{g.get('confidence')}）" for g in grams)
                    if grams else "—"))
    d = item.get("directing") or {}
    lines.append(f"  directing: {'・'.join(d.get('job') or [])}"
                 f" / 相手: {'・'.join(d.get('pairs_with') or [])}"
                 f" / 位置: {'・'.join(d.get('position') or [])}")
    lines.append(f"  source: {item.get('source')}   status: {item.get('status')}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(
        description="技法の目録から、条件に合うものを刷る（読み取り専用）")
    ap.add_argument("--light", action="store_true",
                    help="光の演出の目録（references/lighting）を引く")
    ap.add_argument("--kind", help="作り方（灯・自然・光学・編集）")
    ap.add_argument("--role", help="そのショットの role（15の種別の1つ）")
    ap.add_argument("--function", help="劇的関数（設定・様式美 など）")
    ap.add_argument("--job", help="演出上の仕事（位置づけ・立体・分離・焦点・感情・時間・意味・様式）")
    ap.add_argument("--position", help="場面の位置（頭・中・尾・つなぎ・全編）")
    ap.add_argument("--id", help="技法の id（3桁。例: 055）")
    ap.add_argument("--name", help="技法和名の一部（例: ゴールデン）")
    args = ap.parse_args()

    if not args.light:
        ap.error("軸を1つ渡すこと（いまは --light だけである）")
    if not any([args.kind, args.role, args.function, args.job, args.position,
                args.id, args.name]):
        ap.error("絞り込みを1つ以上渡すこと（--kind / --role / --function / "
                 "--job / --position / --id / --name）")

    entries, where, problem = lighting.catalog(REPO)
    if problem:
        sys.exit(f"光の目録が読めない（{problem}）: {where}")
    if not entries:
        # ⚠️ **空の目録を「条件に合う光が無い」と言わない。** 前者は目録の欠陥であり、
        #    後者は組み合わせの不在である——**同じ顔で返せば、直すべき側が分からない。**
        sys.exit(f"光の目録が**空である**——1件も引いていない: {where}")

    hits = select(entries, role=args.role, function=args.function,
                  job=args.job, position=args.position, kind=args.kind,
                  tid=args.id, name=args.name)
    print(f"=== 光の演出 — {len(hits)}件 / 目録 {len(entries)}件（{where}）\n")
    for item in hits:
        print(_one(item))
        print()
    if not hits:
        print("**条件に合う光が無い。** ⚠️ **目録が空なのではなく、"
              "この組み合わせが無い**——条件を1つ外して引き直すこと。\n")
    print("⚠️ **目録は草案（status: draft）である。** `roles` は担える仕事の集合であり、"
          "決定ではない——**どれを選ぶかはショットが決める。**\n"
          "⚠️ **§13 へ運ぶのは `en` の行である。** 技法の名は生成器へ渡らない。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
