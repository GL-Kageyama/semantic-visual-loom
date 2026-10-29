"""camera.py — カメラ技法の**目録**（`references/camera/index.yaml`）を読む。

⚠️ **これは検査（`L53`）のための目録であり、人のための文書ではない。**
人が読む解説はこのリポジトリの外に在る——
**二重に書くのは読者が違うからであり、片方だけ直せば食い違う。**

⚠️ **目録はこのリポジトリの中に在る。** 様式カード・形式カードと違い、
`distill-essence-engine` の隣を必要としない——**ゆえに clone した人の手元でも読める。**
`SVL_CAMERA_DIR` は**重ねる**ためのものであり、置き換えるためのものではない
（`grammars.py` と同じ心持）。

⚠️ **「無い」と「読めない」と「形が違う」を、同じ顔で返さない。**
`L53` はその3つで言うことが違う（`L42` と同じ規律）。
"""

import os
from pathlib import Path

try:
    import yaml
except ImportError:                       # check.py が先に止める
    yaml = None

#: 目録の置き場を指す環境変数。⚠️ **重ねる**——指した先を先に読み、無ければ
#: このリポジトリの `references/camera` へ降りる。
CAMERA_ENV = "SVL_CAMERA_DIR"

#: 目録のファイル名。⚠️ **1つだけである。** 目録を2つに割れば、`L53` が
#: 別の目録を読む余地ができる——**台帳を割るなと書いたのと同じ理由である。**
INDEX_NAME = "index.yaml"


def _dirs(repo_root):
    """目録の置き場。**探す順の並び**である（`grammars._dirs` と同じ形）。"""
    own = Path(repo_root) / "references" / "camera"
    env = os.environ.get(CAMERA_ENV)
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

    - `entries` … `{id: 項目}`（目録の順を保つ）。
    - `where`   … 読んだファイル（無ければ「探した範囲」の文）。
    - `problem` … `None` | `"missing"` | `"unreadable"` | `"malformed"`。

    ⚠️ **空を「0件だから正しい」と読ませない。** `entries` が空のとき、
    呼ぶ側は必ず `problem` を見る——**目録が空なら、この層は1件も照合していない。**
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
    items = raw.get("techniques") if isinstance(raw, dict) else None
    if not isinstance(items, list):
        return {}, f"`{p}`", "malformed"
    entries = {}
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            return {}, f"`{p}`", "malformed"
        key = str(item.get("id") or "").strip()
        if not key:
            return {}, f"`{p}`", "malformed"
        if key in entries:
            # ⚠️ **同じ id を2度登録させない。** 後が先を黙って覆えば、
            #    **目録を読む者ごとに違う技法が見える。**
            return {}, f"`{p}`", "malformed"
        entries[key] = item
    return entries, f"`{p}`", None
