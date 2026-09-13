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

import re

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


# ---------------------------------------------------------------- まとめ

CHECKS_SHOT = (check_unit, check_one_place, check_one_time, check_move,
               check_reference_forbidden, check_attached)


def run(project):
    out = list(check_not_empty(project))
    for s in project.order():
        shot = project.shots[s]
        for fn in CHECKS_SHOT:
            out += fn(shot)
        out += check_keys_known(project, shot)
    out += check_disclosure(project)
    out += check_circular(project)
    return out
