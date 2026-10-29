"""camera.py — カメラ技法の**目録**（`references/camera/index.yaml`）を読む。

⚠️ **これは検査（`L53`・`L54`）のための目録であり、人のための文書ではない。**
人が読む解説はこのリポジトリの外に在る——
**二重に書くのは読者が違うからであり、片方だけ直せば食い違う。**

⚠️ **目録はこのリポジトリの中に在る。** 様式カード・形式カードと違い、
`distill-essence-engine` の隣を必要としない——**ゆえに clone した人の手元でも読める。**
`SVL_CAMERA_DIR` は**重ねる**ためのものであり、置き換えるためのものではない。

⚠️ **読む器は `catalog.py` に在る。** 光の目録（`lighting.py`）と同じ器を使う——
**軸ごとに読み方が違えば、片方の習慣だけが育つ。**
"""

import catalog as _catalog

#: 目録の置き場を指す環境変数。⚠️ **重ねる**——指した先を先に読み、無ければ
#: このリポジトリの `references/camera` へ降りる。
CAMERA_ENV = "SVL_CAMERA_DIR"

#: 目録の置き場の名前（`references/<これ>`）。
SUBDIR = "camera"

#: 目録のファイル名。⚠️ **1つだけである。**
INDEX_NAME = _catalog.INDEX_NAME


def _dirs(repo_root):
    """目録の置き場。**探す順の並び**である。"""
    return _catalog.dirs(repo_root, SUBDIR, CAMERA_ENV)


def _index_path(repo_root):
    return _catalog.index_path(repo_root, SUBDIR, CAMERA_ENV)


def catalog(repo_root=None):
    """目録を読む。返り値は `(entries, where, problem)`。

    - `entries` … `{id: 項目}`（目録の順を保つ）。
    - `where`   … 読んだファイル（無ければ「探した範囲」の文）。
    - `problem` … `None` | `"missing"` | `"unreadable"` | `"malformed"`。

    ⚠️ **空を「0件だから正しい」と読ませない。** `entries` が空のとき、
    呼ぶ側は必ず `problem` を見る——**目録が空なら、この層は1件も照合していない。**
    """
    return _catalog.read(repo_root, SUBDIR, CAMERA_ENV)
