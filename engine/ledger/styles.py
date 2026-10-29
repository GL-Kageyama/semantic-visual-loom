"""styles.py — 画風の**目録**（`references/styles/index.yaml`）を読む。

⚠️ **これは検査（`L59`）のための目録であり、人のための文書ではない。**
100項目の出所と当てはめの限界は、目録の頭の註に書いてある。

⚠️ **読む器は `catalog.py` に在る**（カメラ・光・構図と同じ器）。軸ごとに読み方を
書き分けない——**片方の習慣（重ねる・空を正しいと言わない）だけが育つ。**

⚠️ **この軸だけ、目録がカードと同じ棚に住む。** カメラ・光・構図の
`references/<軸>/` には `index.yaml` しか無いが、`references/styles/` には
**様式カード（`*.md`）が同居している**——16枚がこのリポジトリのもので、
隣の `distill-essence-engine` にも55枚ある。⚠️ **ゆえに `SVL_STYLES_DIR` は
`semantic.STYLE_CARD_ENV` と同じ変数である**——**同じ軸を2つの名で指さない。**
（1つの置き場が、カードと目録の両方を収める。）

⚠️ **指し先に `index.yaml` が無ければ、このリポジトリの目録へ降りる。**
カードの置き場を指したまま目録を読んだ顔をしない、というより——
**カードを足した作品が、目録ごと失うことはない**（重ねる、置き換えない）。
"""

import catalog as _catalog

#: 目録の置き場を指す環境変数。⚠️ **様式カードの置き場と同じ名である。**
#: **重ねる**——指した先に `index.yaml` があればそれを先に読み、
#: 無ければこのリポジトリの `references/styles` へ降りる。
STYLES_ENV = "SVL_STYLES_DIR"

#: 目録の置き場の名前（`references/<これ>`）。⚠️ **カードの棚と同じである。**
SUBDIR = "styles"

#: 目録のファイル名。⚠️ **1つだけである。**
INDEX_NAME = _catalog.INDEX_NAME


def _dirs(repo_root):
    """目録の置き場。**探す順の並び**である。"""
    return _catalog.dirs(repo_root, SUBDIR, STYLES_ENV)


def _index_path(repo_root):
    return _catalog.index_path(repo_root, SUBDIR, STYLES_ENV)


def catalog(repo_root=None):
    """目録を読む。返り値は `(entries, where, problem)`。

    - `entries` … `{id: 項目}`（目録の順を保つ）。
    - `where`   … 読んだファイル（無ければ「探した範囲」の文）。
    - `problem` … `None` | `"missing"` | `"unreadable"` | `"malformed"`。

    ⚠️ **空を「0件だから正しい」と読ませない。** `entries` が空のとき、
    呼ぶ側は必ず `problem` を見る——**目録が空なら、この層は1件も照合していない。**
    """
    return _catalog.read(repo_root, SUBDIR, STYLES_ENV)
