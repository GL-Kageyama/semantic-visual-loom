"""semantic.py — JSON Schema が書けない検査。

**なぜ別の層が要るか。** `schemas/` が保証するのは**形**である。`unit` を
`{ before, after }` の対にしたのは「`before` と `after` が同じ」を鳴らすためだったが、
**JSON Schema は2つのプロパティを比較できない**——標準の仕様にその機能が無い。
`if`/`then` + `const` は**列挙**であって比較ではなく（自由文なので閉じない）、
`$data` 参照は標準仕様に入らなかった提案である。**測って確かめてある**（`HISTORY.md`）。

**だからここが負う。** 検査は三つの層に分かれる。

  層A  ショット1枚の中で閉じる検査（一変化・一環境・一時刻・一運動）
  層B  台帳と突き合わせる検査（参照・禁制・開示・出所）
  層C  入力そのものの検査（**空を OK と言わない**）

⚠️ 層C を最初に置く理由。**相手が空なら、層A も層B も一件も鳴らない。**
鳴らないことは、正しいことの証明ではない——`0 == 0` が通った実例が既にある。
"""

import json
import re
from pathlib import Path

import specdoc
import specmap

# ---------------------------------------------------------------- 層C 空の検査


def check_not_empty(project):
    """⚠️ 空を OK と言わない。**これが最初に鳴る。**"""
    out = []
    if not project.shots:
        out.append(finding("L0", "", "ショットが1本も無い。検査は何も見ていない。"))
    if not project.ledger:
        out.append(finding("L0", "", "制作台帳が空である。参照も禁制も導出できない。"))
    if not project.disclosure:
        out.append(finding("L0", "", "台帳の disclosure が空である。開示の検査は走らない。"))
    return out


def finding(code, shot, message, severity="violation", **extra):
    f = {"code": code, "shot": shot, "message": message, "severity": severity}
    f.update(extra)
    return f


# ---------------------------------------------------------------- 層A 一枚で閉じる

# 環境を分かつ語（§4 の ID / Name に現れる）。**D1 の移植。**
SPLIT = re.compile(r"→|->|／|\s+and\s+|、")

# 時刻の語。**§8 の本文は英語と日本語が混ざる。D2 の移植。**
TIME_WORDS = {
    "morning": r"\bmorning\b|翌朝|朝",
    "afternoon": r"\bafternoon\b|午後",
    "evening": r"\bevening\b|夕方|夕",
    "night": r"\bnight\b|深夜|夜",
    "noon": r"\bnoon\b|\bmidday\b|正午|昼",
    "dawn": r"\bdawn\b|\bsunrise\b|明け方",
    "dusk": r"\bdusk\b|\bsunset\b|日暮",
    "afterschool": r"放課後|\bafter school\b",
}

# 移動の動詞。**D3 の移植。**
MOVE = re.compile(r"\bthen\b|→|moves? to|arrives? at|walks? (to|home)|帰り道", re.I)


def check_unit(shot):
    """L1 — 一つの変化か。**JSON Schema に書けない、この層の存在理由そのもの。**"""
    u = shot.get("unit") or {}
    b, a = u.get("before"), u.get("after")
    if b is None or a is None:
        return []
    if _norm(b) == _norm(a):
        return [finding("L1", shot["shot"],
                        f"unit.before と unit.after が同じ（{b!r}）。"
                        "このショットは何も起こしていない。"
                        "§2.1——一つのショットは一つの変化のためにある。")]
    return []


def _norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().casefold()


def check_one_place(shot):
    """L2 — 一環境か。**D1 の移植。** 連続テイク1本に複数環境は物理的に不可能。"""
    p = shot.get("place", "")
    parts = [x for x in SPLIT.split(p) if x.strip()]
    if len(parts) > 1:
        return [finding("L2", shot["shot"],
                        f"place に複数の場所が並ぶ（{len(parts)} 個）: {p!r}。"
                        "生成では直らない。ショットを割るか台帳に場所を立てる。")]
    return []


def check_one_time(shot):
    """L3 — 一時刻か。**D2 の移植。** 見出しの時刻語と、ビート本文の時刻語の両方を見る。"""
    out = []
    t = shot.get("time", "")
    parts = [x for x in SPLIT.split(t) if x.strip()]
    if len(parts) > 1:
        out.append(finding("L3", shot["shot"],
                           f"time に複数の時刻が並ぶ（{len(parts)} 個）: {t!r}。"))
    body = " ".join(_beat_text(b) for b in shot.get("beats") or [])
    hits = sorted({k for k, pat in TIME_WORDS.items() if re.search(pat, body, re.I)})
    if len(hits) >= 3:
        out.append(finding("L3", shot["shot"],
                           f"ビート本文に異なる時刻の語が {len(hits)} 種ある: {','.join(hits)}。"
                           "⚠️ 見出しの time が単数でも、本文が複数の時刻を要求していれば跨いでいる。"))
    return out


def check_move(shot):
    """L4 — 移動の動詞。**D3 の移植。だが、単独では鳴らさない。**

    ⚠️ **実測が教えた。** D3 は午前二時の57本で 誤検出 0 だった。
    同じ検査器を**受け火 V2 の30本に当てると、5件鳴って5件とも誤検出だった。**

      `→`         器官の**並び**（手すくう→指頁をめくる→…）。場所ではない
      `Then`      **時間の接続詞**（Then the 定型句）。移動ではない
      `moves to`  **「〜しようとする」**（moves to discard her）。場所ではない
      `walks to`  頁の外へ歩く。**場所は変わらない**

    **検出器を片方の作品に合わせて書くと、もう片方の作品で誤検出する。**
    これは既に記録のある失敗の裏返しである——「同じ欠陥が2つの表記で書かれているとき、
    片方の表記に合わせると、もう片方を取り逃す」。

    だから **L4 は L2 と対でしか鳴らさない。** 場所が実際に跨っているときだけ、
    移動の語はその裏付けになる。単独なら**註**であって、違反ではない。
    """
    body = " ".join(_beat_text(b) for b in shot.get("beats") or [])
    m = MOVE.search(body)
    if not m:
        return []
    multi_place = len([x for x in SPLIT.split(shot.get("place", "")) if x.strip()]) > 1
    if multi_place:
        return [finding("L4", shot["shot"],
                        f"ビート本文に移動の語がある（{m.group(0)!r}）。"
                        "**place も跨っている**ので、これは L2 の裏付けである。")]
    return [finding("L4", shot["shot"],
                    f"ビート本文に移動の語がある（{m.group(0)!r}）。"
                    "**だが place は跨っていない。** 語が別の意味で使われている可能性がある"
                    "——器官の並び（`→`）・時間の接続詞（`Then`）・「〜しようとする」（`moves to`）・"
                    "画面内の歩行（`walks to`）。**違反ではない。**",
                    severity="note")]


def _beat_text(beat):
    if isinstance(beat, dict):
        return str(beat.get("what", ""))
    return str(beat)


# ---------------------------------------------------------------- 層B 台帳と突き合わせる


def check_reference_forbidden(shot):
    """L5 — 参照集合と禁制集合の衝突。**設計ミスであり、生成の失敗ではない。**"""
    ref = set(shot.get("reference_set") or [])
    forb = set(shot.get("forbidden_set") or [])
    both = sorted(ref & forb)
    if both:
        return [finding("L5", shot["shot"],
                        f"同じものを参照し、かつ禁じている: {', '.join(both)}。"
                        "どちらが勝つかは生成器が決める。**決めさせてはいけない。**")]
    return []


def check_attached(shot):
    """L6 — 意図と実際の食い違い。**受け火 V1 の実測が要求した欄。**

    花が出演しているのに花のシートが無いクリップが2本あり、
    しかも V1 の仕様には添付の宣言が1つも無かった。**記録が無いとは、そういうことである。**

    ⚠️ **「無い」と「食い違っている」を混同しない。** `attached` の欄そのものが
    無いショットは、**食い違いではなく、記録が無い**のである——
    `attached: []` にすると、この検査器は「意図にあるのに1つも添付されていない」と
    **30本ぶん偽って鳴る。** 書かなかったことと、書いて空だったことは違う。
    """
    if "attached" not in shot:
        return [finding("L6", shot["shot"],
                        "添付の記録が無い（`attached` の欄そのものが無い）。"
                        "**食い違いではない——記録が無いのである。**"
                        "原因も決まらない（読めないものは、遡れない）。",
                        no_record=True)]
    ref = set(shot.get("reference_set") or [])
    att = set(shot.get("attached") or [])
    out = []
    missing = sorted(ref - att)
    extra = sorted(att - ref)
    if missing:
        out.append(finding("L6", shot["shot"],
                           f"意図にあるが、実際に添付されていない: {', '.join(missing)}。"
                           "⚠️ どちらが正しいかは、この検査器には決められない。**食い違いを挙げるだけである。**"))
    if extra:
        out.append(finding("L6", shot["shot"],
                           f"意図に無いものが添付されている: {', '.join(extra)}。"
                           "参照シートは自分の衣装を宣言しており、**参照画像の服が文字に優先する**（実測）。"))
    return out


def check_keys_known(project, shot):
    """L8 — 台帳に無いキーを引いていないか。**引けないキーは、存在しないものを固定しようとしている。**"""
    known = project.known_keys()
    out = []
    for name, keys in (("reference_set", shot.get("reference_set") or []),
                       ("attached", shot.get("attached") or [])):
        for k in keys:
            if k not in known:
                out.append(finding("L8", shot["shot"],
                                   f"{name} の {k!r} が台帳に無い。"
                                   f"台帳にあるのは: {', '.join(sorted(known)) or '（無し）'}"))
    return out


def check_disclosure(project):
    """L7 — 開示。**台帳の「意図」とショット記録の「実際」を突き合わせる。**

    L7a 早すぎる開示   宣言された変化点より**前**のショットが、既にその値を持っている
    L7b 台帳が予測していない  宣言された変化点のショットで、状態が実際には変わっていない

    ⚠️ **開示状態を持たないショットを数えて報告する。** 数えないと、
    「違反0件」が「検査した結果0件」なのか「検査していない」なのか読めない。
    """
    out = []
    order = project.order()
    idx = {s: i for i, s in enumerate(order)}
    bare = [s for s in order if not (project.shots[s].get("disclosure_state") or {})]

    # ⚠️ **書いていない属性は、食い違いではない。**
    #    台帳が宣言していても、どのショット記録も実際を書いていないなら、
    #    その変化点は検査されていない——照合する相手が無いのである。
    recorded = set()
    for s in order:
        recorded |= set((project.shots[s].get("disclosure_state") or {}).keys())

    for cp in project.disclosure:
        target, attr, val = cp.get("shot"), cp.get("attr"), cp.get("value")
        if target is None or attr is None:
            out.append(finding("L7", str(target),
                               f"変化点 {cp!r} に shot か属性が無い。形は ledger.schema.json が見るが、"
                               "**意味はここでしか見られない。**"))
            continue
        if target not in idx:
            out.append(finding("L7", target,
                               f"台帳が宣言した変化点 {target!r} のショットが存在しない。"))
            continue
        if attr not in recorded:
            out.append(finding("L7", f"（{attr}）",
                               f"台帳は {target} で {attr} が {val!r} になると宣言しているが、"
                               "**どのショット記録もこの属性の実際を書いていない。**"
                               "照合する相手が無いので、この変化点は検査されていない——"
                               "**違反0件ではない。**",
                               severity="note"))
            continue

        # L7a — 早すぎる開示
        for s in order[:idx[target]]:
            st = project.shots[s].get("disclosure_state") or {}
            if attr in st and _norm(st[attr]) == _norm(val):
                out.append(finding("L7", s,
                                   f"早すぎる開示。{attr} が {val!r} になるのは {target} のはずだが、"
                                   f"{s} で既にそうなっている。**観客は先に知ってしまう。**"))

        # L7b — 台帳が予測していない
        st = project.shots[target].get("disclosure_state") or {}
        if attr in st and _norm(st[attr]) != _norm(val):
            out.append(finding("L7", target,
                               f"台帳は {attr} が {val!r} になると宣言しているが、"
                               f"実際は {st[attr]!r} である。**台帳が §16 を予測していない。**"))

    if bare:
        out.append(finding("L7", f"{len(bare)}本",
                           f"開示状態を持たないショットが {len(bare)} 本ある: "
                           f"{', '.join(bare[:8])}{' …' if len(bare) > 8 else ''}。"
                           "**これらのショットは開示の検査を受けていない。**",
                           severity="note" if len(bare) < len(order) else "violation"))
    return out


def check_circular(project):
    """L9 — **この記録は、台帳に対して何か新しいことを言っているか。**

    台帳の disclosure が「意図」で、ショット記録の disclosure_state が「実際」である。
    **だが、実際を意図から写したら、この検査は何も見ていない。**

    ⚠️ これは実際に起きた。受け火 V2 を写すとき `disclosure_state` を台帳から導出し、
    L7 は 0 件になった。**0件は「正しい」ではなく「同じものを二度読んだ」。**

    ⚠️ **見るのは「遷移」だけである。** ショットごとの値を台帳の導出と突き合わせると、
    **台帳が宣言していて、どのショット記録も書いていない属性**（受け火 V2 の
    `HANA.speech` / `HANA.mark` / `HANA.name`）が比較に入り込み、**食い違いに見える。**
    L6・L7 と同じ罠である——**書いていないものは、食い違いではない。**
    遷移を数えれば、書かれていない属性はそもそも遷移を持たない。

    ⚠️ **初出は遷移ではない。** 最初に現れた値は「出発点」であって、台帳が宣言する
    変化点ではない。数えるのは2回目以降の変化だけである。

    ⚠️ **この註は、読み直しでは消えない。** 記録が持つ遷移がすべて台帳の宣言位置と
    一致しているなら、**写したのか独立に読んだのか、区別がつかない。**
    §16 を別の道具で読み直しても、同じ遷移が出るなら、この註は鳴り続ける——
    **一致は独立性の証拠ではない。** 消えるのは、記録が台帳に無い遷移を持ったときだけである。
    """
    if not project.disclosure or not project.shots:
        return []
    order = project.order()
    idx = {s: i for i, s in enumerate(order)}

    declared = {}  # 属性 → 台帳が宣言した変化点の位置
    for cp in project.disclosure:
        if cp.get("shot") in idx:
            declared.setdefault(cp["attr"], set()).add(idx[cp["shot"]])

    seen = {}          # 属性 → 直前に記録された値
    transitions = 0    # 記録が持つ遷移の数（初出は数えない）
    unexplained = []   # 台帳が宣言していない位置で変わっている
    for i, s in enumerate(order):
        for attr, val in (project.shots[s].get("disclosure_state") or {}).items():
            v = _norm(val)
            if attr not in seen:
                seen[attr] = v      # 初出＝出発点。遷移ではない
                continue
            if seen[attr] == v:
                continue
            seen[attr] = v
            transitions += 1
            if i not in declared.get(attr, ()):
                unexplained.append(f"{s} の {attr}")

    # ⚠️ 遷移が無いなら、この検査は空である。L7 が「書いていない」と報告する。
    #    台帳が宣言していない所で変わっているなら、記録は新しいことを言っている。
    if not transitions or unexplained:
        return []
    return [finding("L9", f"{transitions}箇所",
                    f"**この記録は、台帳に対して何も新しいことを言っていない。** "
                    f"記録が持つ遷移 {transitions} 箇所は、すべて台帳が宣言した位置と一致する"
                    "——つまり disclosure_state は台帳の disclosure から完全に導出できる。"
                    "**写したのか、独立に読んだのか、区別がつかない。** "
                    "⚠️ **同じ原文を別の道具で読み直しても、この註は消えない**——"
                    "一致は独立性の証拠ではない。消えるのは、記録が台帳に無い遷移を"
                    "持ったときだけである。",
                    severity="note")]


def check_negative_response(project):
    """L10 — **開示の変化点は、モデルに渡る文に現れているか。**

    `disclosure` の各変化点は `negative:` を宣言する。

      `changed`  この変化点で §18 `Negative Prompt` の節が変わった
      `covered`  §18 は変わらない。**既にその状態を持っていた**

    ⚠️ **どちらの宣言も、§18 を実際に読んで検算する。** 台帳が「変わった」と言い、
    §18 が変わっていなければ台帳が誤りである。**「変わらない」と言い、§18 が変わって
    いれば、その理由も誤りである。** 宣言は両方向に falsify できる。

    ⚠️ **これが「鳴らない分岐」の実体である。** 第2号の検査器は相手を §16 にしていたので
    「§16 が応答していない」が4つとも偽になり、**分岐は一度も鳴らなかった。**
    相手を §18 に変えると、**§18 は4つのうち2つでしか変わらない**（実測）ので、
    この分岐は実データで鳴る。**鳴らして初めて、分岐は存在する。**

    ⚠️ **宣言が無ければ鳴る。** 変化点が `negative:` を書いていないなら、
    その変化点は**モデルに渡る文に対して一度も確かめられていない**——
    「違反0件」ではなく「検査していない」。**`disclosure` に4行あって `negative:` が
    1つも無い状態は、この検査が空である。**
    """
    out = []
    order = project.order()
    idx = {s: i for i, s in enumerate(order)}
    checked = []

    for cp in project.disclosure:
        target = cp.get("shot")
        if target not in idx:
            continue          # 座標が無いことは L7 が報告する。ここでは重ねて鳴らさない
        declared = (cp.get("raw") or {}).get("negative")

        if declared is None:
            out.append(finding("L10", str(target),
                               "変化点に `negative:` が無い。**§18 に対して確かめられていない。**"
                               "`changed`（この変化点で §18 が変わった）か "
                               "`covered`（§18 が既にその状態を持っていた）を書く。"
                               "**書かなければ、この変化点は検査されていない**——"
                               "違反0件ではない。"))
            continue
        if declared not in ("changed", "covered"):
            out.append(finding("L10", str(target),
                               f"`negative: {declared!r}` は changed / covered のどちらでもない。"))
            continue

        i = idx[target]
        if i == 0:
            out.append(finding("L10", str(target),
                               "先頭のショットに変化点がある。**前のショットが無いので、"
                               "「変わった」を言えない。**",
                               severity="note"))
            continue

        prev = order[i - 1]
        try:
            a = _neg(project, prev)
            b = _neg(project, target)
        except _NoSpec as e:
            out.append(finding("L10", str(target), str(e)))
            continue
        if a is None or b is None:
            out.append(finding("L10", str(target),
                               f"§18 `Negative Prompt` の節が無い（{prev if a is None else target}）。"
                               "**節が無いのは、変わらなかったのではない。**"))
            continue

        changed = set(a) != set(b)
        if declared == "changed" and not changed:
            out.append(finding("L10", str(target),
                               f"`negative: changed` と宣言しているが、§18 は "
                               f"{prev} と1節も違わない（{len(b)} 節）。**台帳が §18 を予測していない。**"))
        elif declared == "covered" and changed:
            out.append(finding("L10", str(target),
                               f"`negative: covered` と宣言しているが、§18 は "
                               f"{prev} から変わっている（+{len(set(b) - set(a))} / "
                               f"−{len(set(a) - set(b))} 節）。**理由が誤っている。**"))
        else:
            checked.append(f"{target} {declared}")

    if checked:
        out.append(finding("L10", f"{len(checked)}点",
                           "§18 の応答を確かめた: " + "／".join(checked) + "。"
                           "**§18 が変わらないことは、応答していないことではない**——"
                           "§18 は安全在圏であり、変化点より先にその禁止を持つことがある。",
                           severity="note"))
    return out


class _NoSpec(Exception):
    pass


def _neg(project, shot):
    src = project.shots[shot].get("spec")
    if not src:
        raise _NoSpec(f"ショット {shot} に `spec:` が無い。**§18 を読む相手が分からない。**"
                      "記録が無いので、この変化点は検査されていない。")
    try:
        return specdoc.negative_prompt(project.root / src)
    except FileNotFoundError:
        raise _NoSpec(f"ショット {shot} の `spec: {src}` が読めない。")


# ---------------------------------------------------------------- 層D 対応の検査

TOP_SECTION = re.compile(r"^(\d+)\.\s+(\S.*?)\s*$")


def _spec_tops(path):
    """仕様の**トップレベルの節**（`# 1. VIDEO` の形）を、順序どおりに返す。"""
    return [f"{m.group(1)}. {m.group(2)}"
            for ln in Path(path).read_text(encoding="utf-8").splitlines()
            if (h := specdoc.HEADING.match(ln)) and (m := TOP_SECTION.match(h.group(2)))]


def check_spec_sections(project):
    """L11 — **仕様の節が、目録のとおりであるか。**

    ⚠️ **目録そのものが短くなっていないかも見る。** 20節あるはずの目録が
    3節になっていれば、仕様に節が足されても鳴らない——**検査が空になる。**

    ⚠️ **`spec:` が無い／読めないショットは、黙って飛ばさない。** 鳴る。
    """
    out = []
    if len(specmap.SPEC_SECTIONS) != 20:
        out.append(finding("L11", "", f"目録の節が {len(specmap.SPEC_SECTIONS)} 個である。"
                                      "20 のはずである——**目録が短くなれば、足された節を鳴らせない。**"))
    want = list(specmap.SPEC_SECTIONS)
    seen = 0
    for s in project.order():
        shot = project.shots[s]
        src = shot.get("spec")
        if not src:
            out.append(finding("L11", s, "`spec:` が無い。**このショットの仕様は検査されていない。**"))
            continue
        p = project.root / src
        if not p.is_file():
            out.append(finding("L11", s, f"`spec: {src}` が読めない。"))
            continue
        got = _spec_tops(p)
        seen += 1
        extra = [t for t in got if t not in want]
        miss = [t for t in want if t not in got]
        if extra:
            out.append(finding("L11", s, f"目録に無い節がある: {'／'.join(extra)}。"
                                         "**節が足されたなら、`specmap.SPEC_MAP` にも足す**——"
                                         "行き先の宣言が無い節は、記録のどこにも現れない。"))
        if miss:
            out.append(finding("L11", s, f"目録にある節が無い: {'／'.join(miss)}。"))
        if not extra and not miss and got != want:
            out.append(finding("L11", s, f"節は揃っているが順序が違う。目録は順序も含む。"))
    if seen:
        out.append(finding("L11", f"{seen}本", f"§1–20 の目録を確かめた（{len(want)} 節）。"
                                               "**節が足されれば鳴る。**", severity="note"))
    return out


def check_field_source(schema_dir):
    """L12 — **欄と節の対応が、両方向に閉じているか。**

    片方向だけでは足りない。**節が欄を名指しても、欄が節を名指さなければ、
    その欄は出所を持たない**——誰かが思いつきで足した欄であり、
    台帳が読むのかどうかも決まっていない。

    ⚠️ **`("added", None)` の欄は、閉じていなくてよい。** ただし**理由を書く**
    （`specmap.ADDED_WHY`）——**§1–20 に無いことを、無いまま記録する。**
    """
    out = []
    path = Path(schema_dir) / "shot-record.schema.json"
    if not path.is_file():
        out.append(finding("L12", "", f"ショット記録のスキーマが読めない: {path}"))
        return out
    schema = json.loads(path.read_text(encoding="utf-8"))
    fields = set(schema.get("properties", {}))
    if not fields:
        out.append(finding("L12", "", "スキーマに欄が1つも無い。**空のスキーマと検査している。**"))
        return out

    # ① 欄 → 出所。すべての欄が出所を宣言しているか。
    for f in sorted(fields - set(specmap.FIELD_SOURCE)):
        out.append(finding("L12", f, f"欄 `{f}` の出所が宣言されていない。"
                                     "**どこから来た欄か分からないものは、検査できない。**"))
    for f in sorted(set(specmap.FIELD_SOURCE) - fields):
        out.append(finding("L12", f, f"`FIELD_SOURCE` が欄 `{f}` を指しているが、スキーマに無い。"))
    for f, (kind, sec) in sorted(specmap.FIELD_SOURCE.items()):
        if kind == "added":
            if f not in specmap.ADDED_WHY:
                out.append(finding("L12", f, f"`added` の欄 `{f}` に理由が無い。"
                                             "**§1–20 に無いことを、無いまま書く。**"))
        elif sec not in specmap.SPEC_SECTIONS:
            out.append(finding("L12", f, f"欄 `{f}` の出所 `{sec}` は目録に無い節である。"))

    # ② 節 → 行き先。すべての節が宣言されているか。
    for sec in specmap.SPEC_SECTIONS:
        m = specmap.SPEC_MAP.get(sec)
        if m is None:
            out.append(finding("L12", sec, f"節 `{sec}` の行き先が宣言されていない。"
                                           "**宣言の無い節は、黙って落ちる。**"))
            continue
        if m["rest"] not in specmap.REST:
            out.append(finding("L12", sec, f"節 `{sec}` の `rest` が `REST` に無い: `{m['rest']}`。"))
        for f in m["to"]:
            if f not in fields:
                out.append(finding("L12", sec, f"節 `{sec}` が欄 `{f}` を名指すが、スキーマに無い。"))

    # ③ 閉じているか。**「追加」でない欄の集合＝節が名指した欄の集合**であること。
    if fields:
        named = {f for m in specmap.SPEC_MAP.values() for f in m["to"]}
        moved = {f for f, (k, _) in specmap.FIELD_SOURCE.items() if k != "added"}
        for f in sorted(moved - named):
            out.append(finding("L12", f, f"欄 `{f}` は節から来ているのに、どの節もそれを名指していない。"
                                         "**節から来た欄は、節の側からも見えなければならない。**"))
        for f in sorted(named - moved):
            out.append(finding("L12", f, f"節が欄 `{f}` を名指しているのに、`FIELD_SOURCE` では追加になっている。"))

    if not out:
        moved = sum(1 for k, _ in specmap.FIELD_SOURCE.values() if k != "added")
        out.append(finding("L12", f"{len(fields)}欄", f"欄と節の対応は閉じている"
                                                      f"（{len(specmap.SPEC_SECTIONS)} 節 → {moved} 欄＋"
                                                      f"{len(fields) - moved} の追加欄）。", severity="note"))
    return out


# ---------------------------------------------------------------- まとめ

CHECKS_SHOT = (check_unit, check_one_place, check_one_time, check_move,
               check_reference_forbidden, check_attached)


def run(project, schema_dir=None):
    out = list(check_not_empty(project))
    for s in project.order():
        shot = project.shots[s]
        for fn in CHECKS_SHOT:
            out += fn(shot)
        out += check_keys_known(project, shot)
    out += check_disclosure(project)
    out += check_circular(project)
    out += check_negative_response(project)
    out += check_spec_sections(project)
    if schema_dir:
        out += check_field_source(schema_dir)
    return out
