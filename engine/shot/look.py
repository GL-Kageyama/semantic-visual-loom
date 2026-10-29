#!/usr/bin/env python3
"""look.py — **技法を引く。** 目録から、条件に合うものを刷る。

    使い方:  python3 engine/shot/look.py --light --role 情景
             python3 engine/shot/look.py --light --kind 自然 --function 設定
             python3 engine/shot/look.py --light --job 時間 --position 頭
             python3 engine/shot/look.py --light --id 055
             python3 engine/shot/look.py --light ゴールデン
             python3 engine/shot/look.py --composition --role 情景
             python3 engine/shot/look.py --composition 三分割
             python3 engine/shot/look.py --light ゴールデン --composition 三分割
             python3 engine/shot/look.py --style --medium 手描き --star 3
             python3 engine/shot/look.py --style 水彩

⚠️ **読み取り専用である。** 1バイトも書かない——目録にも、作品にも、どこにも。

⚠️ **これは献立ではなく地図である。** 絞り込みは「この role に使える光」を並べるが、
   **どれを選ぶかはショットが決める**——`roles` は担える仕事の集合であって、決定ではない。
   目録は全件 `status: draft` であり、**作品の使い方が食い違えば、作品が勝つ。**

⚠️ **§13 へ運ぶのは `en` の行である。** 技法の名は生成器へ渡らない——
   §13 が名乗った句は `L56` が目録へ当てる（`--id` で確かめられる）。
   ⚠️ **光の名は名詞ゆえ、`L56` は活用を許さない**——`en` をそのまま書くこと。

⚠️ **構図は §18 `Camera Prompt` へ運ぶ。** 構図の節は §1–20 に無い——`L58` は
   `Camera Prompt` を、カメラとは別の問いで読む。
   ⚠️ **`en` を持たない項目が在る**——`twin`（カメラの目録が同じ技法を持つ）。
   **句はカメラの側にだけ在り、`L54` が読む。** ここは「どちらの目録に住むか」を刷る。

⚠️ **画風は名と媒材と★である。** `roles` も `directing` も持たない——
   この軸の柱は `medium`（媒材）であり、**名前が媒材そのものである**からだ。
   ⚠️ **`card` は「同じものを指す様式カード」の名である**——カードそのものではない。
   目録の100件のうちカードを持つのは21件、隣（`near_card`）を持つのは17件、
   **残る62件は名前だけである。** 名は使えるが、カードは無い。

⚠️ **軸は3つである。** `--light`・`--composition`・`--style`。
   ⚠️ **軸ごとに、受ける絞り込みが違う**（画風に `--role` は無い）——**受けない
   絞り込みを黙って無視しない。** 無視すれば「0件」が刷られ、
   **「その画風が無い」と読まれる**（本当は「その軸にその欄が無い」）。
"""

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

# ⚠️ **読み手を新しく書かない。** 目録を読む器は `engine/ledger/lighting.py`・
#    `engine/ledger/composition.py` に在る（中身は同じ `catalog.py` である）。
sys.path.insert(0, str(HERE.parent / "ledger"))

import composition  # noqa: E402
import lighting  # noqa: E402
import styles  # noqa: E402

#: `--role` に限定つきの綴り（`情景（establishing）`）を渡されたときの切り方。
QUALIFIER = "（"

#: 軸の一覧。**目録の読み手・画面の名・註**を、軸ごとに1箇所へ集める。
#: ⚠️ **軸ごとに読み方を書き分けない**——片方の習慣だけが育つ。
#: ⚠️ **`filters` は、その軸が受ける絞り込みである。** 受けないものを渡されたら、
#: 黙って0件を刷らずに止まる——**「欄が無い」と「技法が無い」は別のことである。**
AXES = {
    "light": {
        "module": lighting,
        "label": "光の演出",
        "where": "§13 `LIGHTING`",
        "filters": ("kind", "role", "function", "job", "position", "id", "name"),
        "last": ["⚠️ **§13 へ運ぶのは `en` の行である。** 技法の名は生成器へ渡らない。",
                 "⚠️ **光の名は名詞である**——`L56` は活用を許さない。`en` をそのまま書くこと。"],
        "footer": "⚠️ **目録は草案（status: draft）である。** `roles` は担える仕事の集合であり、"
                  "決定ではない——**どれを選ぶかはショットが決める。**",
    },
    "composition": {
        "module": composition,
        "label": "構図",
        "where": "§18 `Camera Prompt`",
        "filters": ("kind", "role", "function", "job", "position", "id", "name"),
        "last": ["⚠️ **§18 `Camera Prompt` へ運ぶのは `en` の行である。** 技法の名は生成器へ渡らない。",
                 "⚠️ **`en` が「—」の項目は `twin` である**——句はカメラの目録が持ち、`L54` が読む。"],
        "footer": "⚠️ **目録は草案（status: draft）である。** `roles` は担える仕事の集合であり、"
                  "決定ではない——**どれを選ぶかはショットが決める。**",
    },
    "style": {
        "module": styles,
        "label": "画風",
        "where": "§6 `REF_STYLE`（`bible.style` の名）",
        "filters": ("medium", "star", "family", "id", "name"),
        "last": ["⚠️ **§6 `REF_STYLE` へ書くのは名（slug）である**——`bible.style` に名乗れば `L32` が行き先を見る。",
                 "⚠️ **`card` を持つのは100件のうち21件である。** カードが無い名も**使える**——`en` が句である。"],
        "footer": "⚠️ **目録は草案（status: draft）である。** `star` は解剖の見立てであり、"
                  "生成の実測ではない——**作品の使い方が食い違えば、作品が勝つ。**",
    },
}

#: 軸が受ける絞り込みの語（`args` の名前）。⚠️ **報告の文面もここから作る。**
FILTER_LABEL = {"kind": "--kind", "role": "--role", "function": "--function",
                "job": "--job", "position": "--position", "id": "--id",
                "name": "--name", "medium": "--medium", "star": "--star",
                "family": "--family"}


def _base_role(value):
    return str(value or "").split(QUALIFIER)[0].strip()


def select(entries, role=None, function=None, job=None, position=None,
           kind=None, tid=None, name=None, medium=None, star=None,
           family=None):
    """目録を絞る。**与えられた条件のすべて**を満たすものだけを返す。"""
    out = []
    for key, item in entries.items():
        if tid is not None and str(item.get("id") or key) != tid:
            continue
        if name is not None and name not in str(item.get("name") or ""):
            continue
        if kind is not None and item.get("kind") != kind:
            continue
        if family is not None and item.get("family") != family:
            continue
        # ⚠️ **媒材は頭で当てる。** `手描き` で `手描き（油）` を引けねば、
        #    同じ媒材が括弧の数だけ別の語になる（`L59` と同じ切り方である）。
        if medium is not None and not str(item.get("medium") or "").startswith(medium):
            continue
        if star is not None and item.get("star") != star:
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
    head = f"{item.get('id')} {item.get('name')}"
    tags = [str(item["kind"])] if item.get("kind") else []
    if item.get("family"):
        tags.append(str(item["family"]))
    if tags:
        head += f"（{'・'.join(tags)}）"
    lines = [head]
    twin = item.get("twin")
    if twin:
        lines.append(f"  en: —（twin: {twin.get('catalog')} {twin.get('id')}"
                     "——句はあちらの目録が持つ）")
    else:
        lines.append(f"  en: {' / '.join(item.get('en') or [])}")
    # ⚠️ **画風の項目だけが `star` を持つ。** 光・構図の列を空欄で刷らない
    #    ——空欄は「無い」ではなく「ここでは訊いていない」である。
    if item.get("star") is not None:
        lines.append(f"  ★{item.get('star')}    medium: {item.get('medium')}")
        card, near = item.get("card"), item.get("near_card")
        if card:
            lines.append(f"  card: `{card}`（同じものを指す様式カード）")
        elif near:
            lines.append(f"  near_card: `{near.get('id')}`（隣であって同じでない"
                         f"——ずれ: {near.get('gap')}）")
        else:
            lines.append("  card: —（様式カードを持たない名である。`en` の句は在る）")
    if item.get("roles") or item.get("functions"):
        lines.append(f"  roles: {'・'.join(item.get('roles') or [])}"
                     f"    functions: {'・'.join(item.get('functions') or [])}")
    if "grammars" in item:
        grams = item.get("grammars") or []
        lines.append("  grammar: "
                     + ("・".join(f"{g.get('card')}（{g.get('confidence')}）" for g in grams)
                        if grams else "—"))
    d = item.get("directing")
    if d:
        lines.append(f"  directing: {'・'.join(d.get('job') or [])}"
                     f" / 相手: {'・'.join(d.get('pairs_with') or [])}"
                     f" / 位置: {'・'.join(d.get('position') or [])}")
    if item.get("population_hint"):
        lines.append(f"  population_hint: {item['population_hint']}"
                     "（`L58` が記録の `population` と照合する）")
    lines.append(f"  source: {item.get('source')}   status: {item.get('status')}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(
        description="技法の目録から、条件に合うものを刷る（読み取り専用）")
    ap.add_argument("--light", nargs="?", const="", metavar="NAME",
                    help="光の演出の目録（references/lighting）を引く。"
                         "値を渡せば名の一部で絞る")
    ap.add_argument("--composition", nargs="?", const="", metavar="NAME",
                    help="構図の目録（references/composition）を引く。"
                         "値を渡せば名の一部で絞る")
    ap.add_argument("--style", nargs="?", const="", metavar="NAME",
                    help="画風の目録（references/styles）を引く。"
                         "値を渡せば名の一部で絞る")
    ap.add_argument("--kind", help="種類（光: 灯・自然・光学・編集／構図: 構図・画角・配置）")
    ap.add_argument("--role", help="そのショットの role（15の種別の1つ）")
    ap.add_argument("--function", help="劇的関数（設定・様式美 など）")
    ap.add_argument("--job", help="演出上の仕事（軸ごとに語彙が違う。例: 焦点・様式）")
    ap.add_argument("--position", help="場面の位置（頭・中・尾・つなぎ・全編）")
    ap.add_argument("--id", help="技法の id（3桁。例: 055）")
    ap.add_argument("--name", help="技法和名の一部（例: ゴールデン）")
    ap.add_argument("--medium", help="媒材の頭の語（画風のみ。手描き・版・写真・"
                                     "デジタル・立体・複合・任意）")
    ap.add_argument("--star", type=int, help="★の数（画風のみ。3・2・1）")
    ap.add_argument("--family", help="族の名（軸ごとに語彙が違う）")
    args = ap.parse_args()

    chosen = [(axis, getattr(args, axis)) for axis in AXES
              if getattr(args, axis) is not None]
    if not chosen:
        ap.error("軸を1つ以上渡すこと（--light / --composition / --style）")
    # ⚠️ **受けない絞り込みを黙って無視しない。** 無視すれば0件が刷られ、
    #    「その技法が無い」と読まれる——**本当は「その軸にその欄が無い」。**
    given = [name for name in FILTER_LABEL if getattr(args, name) is not None]
    for axis, _value in chosen:
        unused = [FILTER_LABEL[n] for n in given if n not in AXES[axis]["filters"]]
        if unused:
            ap.error(f"{AXES[axis]['label']}の目録は {'・'.join(unused)} を受けない"
                     f"（受けるのは "
                     f"{'・'.join(FILTER_LABEL[n] for n in AXES[axis]['filters'])}）")
    # ⚠️ **軸の値（`--light ゴールデン`）は絞り込みである。** 軸だけ渡されたら、
    #    目録を全件刷る——**それは「引いた」ではなく「写した」である。**
    named_axes = [axis for axis, v in chosen if v]
    if args.name and named_axes:
        ap.error("`--name` と軸の値は同時に渡さないこと（どちらか1つ）")
    if not named_axes and not given:
        allowed = "・".join(FILTER_LABEL[n] for n in AXES[chosen[0][0]]["filters"])
        ap.error(f"絞り込みを1つ以上渡すこと（{allowed}、または軸に名を添える）")

    for axis, value in chosen:
        spec = AXES[axis]
        entries, where, problem = spec["module"].catalog(REPO)
        if problem:
            sys.exit(f"{spec['label']}の目録が読めない（{problem}）: {where}")
        if not entries:
            # ⚠️ **空の目録を「条件に合う技法が無い」と言わない。** 前者は目録の欠陥であり、
            #    後者は組み合わせの不在である——**同じ顔で返せば、直すべき側が分からない。**
            sys.exit(f"{spec['label']}の目録が**空である**——1件も引いていない: {where}")

        hits = select(entries, role=args.role, function=args.function,
                      job=args.job, position=args.position, kind=args.kind,
                      tid=args.id, name=args.name or (value or None),
                      medium=args.medium, star=args.star, family=args.family)
        print(f"=== {spec['label']} — {len(hits)}件 / 目録 {len(entries)}件（{where}）\n")
        for item in hits:
            print(_one(item))
            print()
        if not hits:
            print(f"**条件に合う{spec['label']}が無い。** ⚠️ **目録が空なのではなく、"
                  "この組み合わせが無い**——条件を1つ外して引き直すこと。\n")
        print(spec["footer"])
        for line in spec["last"]:
            print(line)
        if axis != chosen[-1][0]:
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
