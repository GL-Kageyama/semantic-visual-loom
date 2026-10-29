"""composition.py — 構図の**目録**（`references/composition/index.yaml`）を読む。

⚠️ **これは検査（`L57`・`L58`）のための目録であり、人のための文書ではない。**
100項目の出所と当てはめの限界は、目録の頭の註に書いてある。

⚠️ **読む器は `catalog.py` に在る**（カメラ・光と同じ器）。軸ごとに読み方を
書き分けない——**片方の習慣（重ねる・空を正しいと言わない）だけが育つ。**

⚠️ **構図には運動の型も `kind`（誰が作るか）も無い。** すべて撮影時に決まるからである。
柱は `kind`（**その名が何を指すか**——構図・画角・配置）である——
⚠️ **光の `kind`（灯・自然・光学・編集）と同じ鍵だが、問いが違う。**
"""

import catalog as _catalog

#: 目録の置き場を指す環境変数。⚠️ **重ねる**——指した先を先に読み、無ければ
#: このリポジトリの `references/composition` へ降りる。
COMPOSITION_ENV = "SVL_COMPOSITION_DIR"

#: 目録の置き場の名前（`references/<これ>`）。
SUBDIR = "composition"

#: 目録のファイル名。⚠️ **1つだけである。**
INDEX_NAME = _catalog.INDEX_NAME


def _dirs(repo_root):
    """目録の置き場。**探す順の並び**である。"""
    return _catalog.dirs(repo_root, SUBDIR, COMPOSITION_ENV)


def _index_path(repo_root):
    return _catalog.index_path(repo_root, SUBDIR, COMPOSITION_ENV)


def catalog(repo_root=None):
    """目録を読む。返り値は `(entries, where, problem)`。

    - `entries` … `{id: 項目}`（目録の順を保つ）。
    - `where`   … 読んだファイル（無ければ「探した範囲」の文）。
    - `problem` … `None` | `"missing"` | `"unreadable"` | `"malformed"`。

    ⚠️ **空を「0件だから正しい」と読ませない。** `entries` が空のとき、
    呼ぶ側は必ず `problem` を見る——**目録が空なら、この層は1件も照合していない。**
    """
    return _catalog.read(repo_root, SUBDIR, COMPOSITION_ENV)
