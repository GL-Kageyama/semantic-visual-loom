"""catalog.py — 技法の**目録**（`references/<軸>/index.yaml`）を読む共通の口。

⚠️ **カメラと光で、読む器を2つ持たない。** 読み方が2つに割れれば、
**片方の習慣（重ねる・空を正しいと言わない）だけが育つ**——軸ごとに差が生まれる。
ここが唯一の口であり、`camera.py` と `lighting.py` はこの口に名前を付けるだけである。

⚠️ **目録はこのリポジトリの中に在る。** 様式カード・形式カードと違い、
`distill-essence-engine` の隣を必要としない——**ゆえに clone した人の手元でも読める。**
`SVL_CAMERA_DIR` / `SVL_LIGHTING_DIR` は**重ねる**ためのものであり、置き換えるための
ものではない（`grammars.py` と同じ心持）。

⚠️ **「無い」と「読めない」と「形が違う」を、同じ顔で返さない。**
呼ぶ側の層はその3つで言うことが違う（`L42`・`L53`・`L55` と同じ規律）。
"""

import os
from pathlib import Path

try:
    import yaml
except ImportError:                       # check.py が先に止める
    yaml = None

#: 目録のファイル名。⚠️ **軸ごとに1つだけである。** 目録を2つに割れば、
#: 層が別の目録を読む余地ができる——**台帳を割るなと書いたのと同じ理由である。**
INDEX_NAME = "index.yaml"

#: 目録の並びを収める鍵。⚠️ **軸が違っても鍵は同じである**——
#: 呼ぶ側が `techniques:` を書き分けると、写し間違いが形の差として鳴らなくなる。
LIST_KEY = "techniques"


def dirs(repo_root, subdir, env_name):
    """目録の置き場。**探す順の並び**である（`grammars._dirs` と同じ形）。"""
    own = Path(repo_root) / "references" / subdir
    env = os.environ.get(env_name) if env_name else None
    p = Path(env) if env else None
    if p is not None and p.is_dir():
        return [p] + ([own] if own.is_dir() and own.resolve() != p.resolve() else [])
    return [own] if own.is_dir() else []


def index_path(repo_root, subdir, env_name):
    for d in dirs(repo_root, subdir, env_name):
        p = d / INDEX_NAME
        if p.is_file():
            return p
    return None


def read(repo_root, subdir, env_name, list_key=LIST_KEY):
    """目録を読む。返り値は `(entries, where, problem)`。

    - `entries` … `{id: 項目}`（目録の順を保つ）。
    - `where`   … 読んだファイル（無ければ「探した範囲」の文）。
    - `problem` … `None` | `"missing"` | `"unreadable"` | `"malformed"`。

    ⚠️ **空を「0件だから正しい」と読ませない。** `entries` が空のとき、
    呼ぶ側は必ず `problem` を見る——**目録が空なら、その層は1件も照合していない。**
    """
    if yaml is None:
        return {}, "PyYAML が無い", "unreadable"
    root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[2]
    p = index_path(root, subdir, env_name)
    if p is None:
        return {}, "／".join(f"`{d / INDEX_NAME}`"
                            for d in dirs(root, subdir, env_name)) or "**置き場が無い**", "missing"
    try:
        raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except (yaml.YAMLError, OSError, UnicodeDecodeError):
        return {}, f"`{p}`", "unreadable"
    items = raw.get(list_key) if isinstance(raw, dict) else None
    if not isinstance(items, list):
        return {}, f"`{p}`", "malformed"
    entries = {}
    for item in items:
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
