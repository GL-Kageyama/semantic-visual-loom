"""grammars.py — 形式カードの**目録**（`references/grammars/index.yaml`）を読む。

⚠️ **これは検査のための目録であり、人のための文書ではない。** カードの散文
（`references/formats/<name>.md`）は人へ向き、この目録は `L42`・`L45`・`L46` へ向く。
**二重に書くのは、読者が違うからである**——ゆえに**片方だけを直せば、食い違う。**

⚠️ **目録はこのリポジトリの中にある。** 様式カード・形式カードと違い、
`distill-essence-engine` の隣を必要としない——**ゆえに clone した人の手元でも読める。**
`SVL_GRAMMARS_DIR` は**重ねる**ためのものであり、置き換えるためのものではない
（`_cards_dirs` と同じ心持）。

⚠️ **この目録は「15の文法」を名乗らない。** 欄はあるが、数はここでは主張しない
——数は作者の設計ノートのものであり、目録は**登録されたものの集合**である。
"""

import os
from pathlib import Path

try:
    import yaml
except ImportError:                       # check.py が先に止める
    yaml = None

#: 目録の置き場を指す環境変数。⚠️ **重ねる**——指した先を先に読み、無ければ
#: このリポジトリの `references/grammars` へ降りる。
GRAMMARS_ENV = "SVL_GRAMMARS_DIR"

#: 目録のファイル名。⚠️ **1つだけである。** 目録を2つに割れば、`L42` と `L45` が
#: 別の目録を読む余地ができる——**台帳を割るなと書いたのと同じ理由である。**
INDEX_NAME = "index.yaml"


def _dirs(repo_root):
    """目録の置き場。**探す順の並び**である（`_cards_dirs` と同じ形）。"""
    own = Path(repo_root) / "references" / "grammars"
    env = os.environ.get(GRAMMARS_ENV)
    p = Path(env) if env else None
    if p is not None and p.is_dir():
        return [p] + ([own] if own.is_dir() and own.resolve() != p.resolve() else [])
    return [own] if own.is_dir() else []


def _index_path(repo_root):
    for d in _dirs(repo_root):
        p = d / INDEX_NAME
        if p.is_file():
            return p
    return None


def catalog(repo_root=None):
    """目録を読む。返り値は `(entries, where, problem)`。

    - `entries` … `{name: 項目}`。読めなければ `{}`。
    - `where`   … 読んだファイル（無ければ「探した範囲」の文）。
    - `problem` … `None` | `"missing"` | `"unreadable"` | `"malformed"`。

    ⚠️ **「無い」と「読めない」と「形が違う」を、同じ顔で返さない**
    ——`L42` はその3つで言うことが違う（`L32` の a-1/a-2 と同じ規律）。
    ⚠️ **空を「0件だから正しい」と読ませない。** entries が空のとき、呼ぶ側は
    必ず `problem` を見る——**目録が空なら、この層は1本も照合していない。**
    """
    if yaml is None:
        return {}, "PyYAML が無い", "unreadable"
    root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[2]
    p = _index_path(root)
    if p is None:
        return {}, "／".join(f"`{d / INDEX_NAME}`" for d in _dirs(root)) or "**置き場が無い**", "missing"
    try:
        raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except (yaml.YAMLError, OSError, UnicodeDecodeError):
        return {}, f"`{p}`", "unreadable"
    items = raw.get("grammars") if isinstance(raw, dict) else None
    if not isinstance(items, list):
        return {}, f"`{p}`", "malformed"
    entries, order = {}, []
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            return {}, f"`{p}`", "malformed"
        name = str(item.get("name") or "").strip()
        if not name:
            return {}, f"`{p}`", "malformed"
        if name in entries:
            # ⚠️ **同じ名を2度登録させない。** 後が先を黙って覆えば、
            #    **目録を読む者ごとに違う文法が見える。**
            return {}, f"`{p}`", "malformed"
        entries[name] = item
        order.append(name)
    return entries, f"`{p}`", None


def names(repo_root=None):
    """登録された名の並び（目録の順）。読めなければ `[]`。"""
    entries, _where, _problem = catalog(repo_root)
    return list(entries)


def card_names(repo_root=None):
    """`references/formats/` にある**文法カードの名**（`video-spec` とその鏡を除く）。

    ⚠️ **この関数は「カードは在るが目録に無い」を言うために在る**——`L42` の註が
    それを使う。**検査ではなく、ずれを見せる計器である。**
    """
    root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[2]
    d = root / "references" / "formats"
    if not d.is_dir():
        return []
    out = []
    for p in sorted(d.glob("*.md")):
        stem = p.stem
        if stem == "video-spec" or stem.startswith("video-spec-"):
            continue                      # ⚠️ 基盤の仕様と、その鏡である
        out.append(stem)
    return out
