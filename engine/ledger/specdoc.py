"""specdoc.py — §1–20 の仕様書（`wan-full-spec.md`）を読む。

**なぜ台帳の検査が仕様書を読むのか。** 台帳の `disclosure` は「いつ、観客が何を知るか」を
宣言する。**その宣言が、モデルに渡る文に現れているかを確かめる相手が要る。**
相手は §18 `Negative Prompt` である——**モデルに渡るのはこの節であって、§16 ではない**
（§16 は本ごとに書き直される注記で、塊を持たない。実測は `HISTORY.md`）。

⚠️ **この層は「意味」を読まない。節と段落を切り出すだけである。**
意味の照合（`negative: changed` が本当か）は `semantic.py` の L10 が負う。

⚠️ **切る単位が2つある。** 動画の仕様は**節**（§1–20）で、画像の仕様は**段落**である
——画像の正典は1つの節の中の段落の列だからである（`paragraphs()` の註を見よ）。

⚠️ **節の見出しは `#` の数が揃っていない。** 実測: `## Negative Prompt` の次は
`## Instance` ではなく **`# 19. GENERATION INSTANCE`（h1）** である。
`^## ` で切ると、§18 の末尾に §19 の見出しが食い込む。
**だから見出しは `#{1,6}` で切り、水準を問わない。**
"""

import re
from pathlib import Path

HEADING = re.compile(r"^(#{1,6})[ \t]*(.+?)[ \t]*$")
RULE = re.compile(r"^-{3,}$")


def sections(text):
    """`[(見出し, 本文)]` に割る。**見出しの水準は問わない。**"""
    out = []
    title, buf = None, []
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            if title is not None:
                out.append((title, "\n".join(buf).strip()))
            title, buf = m.group(2).strip(), []
            continue
        if title is not None and not RULE.match(line.strip()):
            buf.append(line)
    if title is not None:
        out.append((title, "\n".join(buf).strip()))
    return out


def section(text, title_prefix):
    """見出しが `title_prefix` で始まる最初の節の本文。**無ければ `None`。**

    ⚠️ `None` と `""` を区別する。**節が無いことと、節が空であることは違う。**
    """
    for t, body in sections(text):
        if t.startswith(title_prefix):
            return body
    return None


def paragraphs(body):
    """本文を段落（空行区切り）に割る。**空の段落は落とす。**

    ⚠️ **`None` はそのまま返す。** 「本文が無い」と「段落が無い」は別である
    （`section` と同じ規律）。

    ⚠️ **これは画像の仕様のためだけにある。** 動画の仕様は §1–20 という節を持つが、
    画像の仕様は節を持たない——**正典は1つの節の中の段落の列である。**
    なぜ見出しで割らないかは `specmap.SPEC_KINDS` の註を見よ
    （**見出しが本文の間にあると、著者の1回の選択がその見出しを巻き込む**）。
    """
    if body is None:
        return None
    return [p.strip() for p in re.split(r"\n[ \t]*\n", body) if p.strip()]


def clausify(body):
    """本文を節（コンマ区切り）に割る。**空の節は落とす。**"""
    if body is None:
        return None
    return [c for c in (x.strip() for x in body.split(",")) if c]


def negative_prompt(path):
    """§18 `Negative Prompt` の節の列。**節が無ければ `None`。**

    ⚠️ `None`（節が無い）を返す。**空の列を返してはならない**——呼び手が
    「変わらなかった」と読んでしまう。**節が無いのは、変わらなかったのではない。**

    ⚠️ **ファイルが無いときは `FileNotFoundError` を投げる。** ここで `None` を返すと、
    「仕様書が無い」と「§18 が無い」が同じ顔になる。**呼び手は両方とも違反にしなければ
    ならないが、理由は違う。**
    """
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(str(p))
    return clausify(section(p.read_text(encoding="utf-8"), "Negative Prompt"))
