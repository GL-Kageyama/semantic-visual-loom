"""lighting.py — 光の演出の**目録**（`references/lighting/index.yaml`）を読む。

⚠️ **これは検査（`L55`・`L56`）のための目録であり、人のための文書ではない。**
100項目の出所と当てはめの限界は、目録の頭の註に書いてある。

⚠️ **読む器は `catalog.py` に在る**（`camera.py` と同じ器）。軸ごとに読み方を
書き分けない——**片方の習慣（重ねる・空を正しいと言わない）だけが育つ。**

⚠️ **光には運動の型が無い。** カメラ目録の `motion_pattern` に当たる列は無く、
柱は `kind`（誰が作るか）である——**カメラの表を空欄ごと写さない。**
"""

import catalog as _catalog

#: 目録の置き場を指す環境変数。⚠️ **重ねる**——指した先を先に読み、無ければ
#: このリポジトリの `references/lighting` へ降りる。
LIGHTING_ENV = "SVL_LIGHTING_DIR"

#: 目録の置き場の名前（`references/<これ>`）。
SUBDIR = "lighting"

#: 目録のファイル名。⚠️ **1つだけである。**
INDEX_NAME = _catalog.INDEX_NAME


def _dirs(repo_root):
    """目録の置き場。**探す順の並び**である。"""
    return _catalog.dirs(repo_root, SUBDIR, LIGHTING_ENV)


def _index_path(repo_root):
    return _catalog.index_path(repo_root, SUBDIR, LIGHTING_ENV)


def catalog(repo_root=None):
    """目録を読む。返り値は `(entries, where, problem)`。

    - `entries` … `{id: 項目}`（目録の順を保つ）。
    - `where`   … 読んだファイル（無ければ「探した範囲」の文）。
    - `problem` … `None` | `"missing"` | `"unreadable"` | `"malformed"`。

    ⚠️ **空を「0件だから正しい」と読ませない。** `entries` が空のとき、
    呼ぶ側は必ず `problem` を見る——**目録が空なら、この層は1件も照合していない。**
    """
    return _catalog.read(repo_root, SUBDIR, LIGHTING_ENV)
