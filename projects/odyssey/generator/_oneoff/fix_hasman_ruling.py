# ⛔ これは 2026-09-29 の一度きりの編集であり、**履歴であって道具ではない。**
#    **当てた結果は `../content/` に入っている。再実行してはならない**——
#    当てる相手（古い文字列）は、もう存在しない。
# -*- coding: utf-8 -*-
"""裁定①（2026-09-29）+ 追加実測（塊を指す文2箇所）を s29–s32 に適用する。

すべての NEW_* 断片は「文字列の中身」（囲みの " は含まない）。
"""
import ast
import pathlib
import io

FILES = ["s29.py", "s30.py", "s31.py", "s32.py"]
TAIL_LOOKING = "を見る）"                                   # を見る）
CLAIM = "同一性の塊は §18 に貼られ"          # 同一性の塊は §18 に貼られ
CLAIM2 = "同一性の塊を、人が居ない画に"  # 同一性の塊を、人が居ない画に
BLOCK_EN = "The identity block pasted into §18"
REFCHAR_ANCHOR = '"ref_character": "'
RESOLVED_ANCHOR = "同一性は `Visual Prompt`"
RISK_ANCHOR = "§18 の `Visual Prompt` には同一性の塊が"


def q(x):
    return '"' + x + '"'


def find(lines, sub, start=0):
    for i in range(start, len(lines)):
        if sub in lines[i]:
            return i
    raise AssertionError("not found: %r" % sub)


def span_end(lines, i):
    j = i
    while j < len(lines):
        if lines[j].rstrip().endswith('",'):
            return j
        j += 1
    raise AssertionError("no span end from %d" % i)


def tail_quote(line):
    s = line.rstrip()
    return s[s.rfind('"'):]


def ind(line):
    return line[:len(line) - len(line.lstrip())]


HEADER = [
    "⛔ **この1本の画には、人が一人も入らない。"
    "****記録の `unit` と `beats` のどこにも、人物が現れない**——",
    "**ゆえにこの1本は、人を一人も置かない。**"
    "（§3 と §15 を見る）。",
]

A = ("⛔ **この1本の画には、人が一人も入らない。**"
     "**記録の `unit`（前・後）と `beats` のどこにも、人物が現れない**")
B = "——**ゆえにこの1本は、人を一人も置かない。**"
C = "**参照集合は「固定するもの」を挙げており、「画に居る者」を挙げているのではない**"
D = "（§15 の `identity` を見る）"
C3 = C[:-2] + "。**"

REF_HEAD = ('`男` — ⚠️ **この1本の画には入らない。'
            '****この1本のどこにも、人物が現れない**'
            '（§3 と §15）。')
REF_29 = [
    REF_HEAD,
    '`女神` — **この1本には添付しない。彼女は'
    'この1本に、四つの姿のどれとしても現れ'
    'ない。** ',
    '参照集合が挙げているのは `男.identity`・'
    '`男.negatives`・`海`・`海.geography`・',
    '`海.states.夜`・`舟`・`舟.appearance`・`舟.negative` の8鍵である。',
    '⚠️ **`男.identity` と `男.negatives` が集合に在っても、'
    'それは人の外見を固定するためであり**——',
    '**この1本に人が居ることは、この集合からは出てこない。**',
]

IDENTITY = [
    '**Must preserve** — この1本が写すものの、一句一句'
    '（海の面、光、時刻、そしてこの1本で'
    '動かないと決めたもの）。',
    '⛔ **この1本の画には、人が一人も入らない**'
    '——**ゆえにこの1本に、守るべき顔も、'
    '体も、衣も無い。**',
    '**同一性の基準は、この1本では人物ではなく、'
    'この枠そのものである**——**記録の `unit`（前・後）と '
    '`beats` のどこにも、人物が現れないからである**',
    '（§3 と §18 を見る）。',
    ' **May change** — 無い。**この1本に、変わりうる人物が一人も居ない。**',
]

MUST = ('⛔ **人が一人も入らないこと** — '
        '**この枠は、海だけで在る。**'
        '**参照集合が人の外見を挙げていても、'
        'それは画に人を置く指示ではない。**')

MASTER = ('⚠️ **No person is in this frame and no part of the raft is in it either — '
          'the water is alone, at every distance and in every focus.**\\n\\n')

VMETA = [
    ' ⚠️ **No person is in this frame at all, at any distance and in any focus: this shot is the sea ',
    'alone, with no figure in it and no part of the raft in it.**"),',
]

RESOLVED = ('⚠️ **参照集合が `男.identity` を挙げていても、'
            'この1本は同一性の塊を §18 に貼らない**'
            '——**記録の `unit` と `beats` のどこにも、人物が'
            '現れないからである**（§3 と §15 を見る）。')

RISK_29 = [
    '⛔ **人が入る。** ⚠️ **この1本の画には、'
    '人が一人も入ってはならない**——'
    '**この経路は、夜の海の画に人物を足したがる。**',
    '**人が入れば、この1本は別のショットになる。**',
]
RISK_SHORT = [
    '⛔ **人が入る。** ⚠️ **この1本の画には、'
    '人が一人も入ってはならない**——'
    '**この経路は、夜の海の画に人物を足したがる。**',
]

TYP0 = "入れ : ば"
TYP1 = "入れば"

for fn in FILES:
    path = str(pathlib.Path(__file__).resolve().parents[1] / "content" / fn)
    lines = io.open(path, encoding="utf-8").read().split("\n")
    log = []

    def splice(i, j, new, label):
        log.append("%-24s lines %d-%d -> %d" % (label, i + 1, j + 1, len(new)))
        lines[i:j + 1] = new

    i = find(lines, '"has_man": True,')
    splice(i, i, [' "has_man": False,'], "has_man")

    hdr = find(lines, CLAIM)
    splice(hdr, hdr + 1, list(HEADER), "header")

    i = find(lines, CLAIM, hdr + 2)
    j = i
    while not (lines[j].rstrip().endswith('",') or '"]' in lines[j]):
        j += 1
    tail = tail_quote(lines[j])
    w, w2 = ind(lines[i]), ind(lines[i + 1])
    prefix = w + ('"notes": ["' if '"notes": [' in lines[i] else '"')
    body = [prefix + A + '"', w2 + q(B)]
    if j - i == 3:
        body += [w2 + q(C), w2 + '"' + D + "。" + tail]
    elif j - i == 2:
        body.append(w2 + '"' + C3 + D + tail)
    else:
        raise AssertionError("%s: notes span %d lines" % (fn, j - i + 1))
    splice(i, j, body, "notes")

    i = find(lines, REFCHAR_ANCHOR)
    k = lines[i].index(REFCHAR_ANCHOR) + len(REFCHAR_ANCHOR)
    pre = lines[i][:k]
    if fn == "s29.py":
        j = find(lines, "主張しない", i)
        assert j - i == 5, "s29 ref_character span %d" % (j - i + 1)
        w2 = ind(lines[i + 1])
        body = [pre + REF_29[0] + '"'] + [w2 + q(x) for x in REF_29[1:-1]] + \
               [w2 + '"' + REF_29[-1] + tail_quote(lines[j])]
        splice(i, j, body, "ref_character")
    else:
        splice(i, i, [pre + REF_HEAD + tail_quote(lines[i])], "ref_character")

    i = find(lines, '"identity": K.identity(')
    j = find(lines, '一人も居ない。**"),', i)
    w = ind(lines[i])
    w2 = " " * (len(w) + len('"identity":'))
    body = [w + '"identity": ' + q(IDENTITY[0])] + [w2 + q(x) for x in IDENTITY[1:-1]] + \
           [w2 + q(IDENTITY[-1]) + ","]
    splice(i, j, body, "identity")

    first = find(lines, BLOCK_EN)
    second = find(lines, BLOCK_EN, first + 1)
    for site, label in ((second, "priorities"), (first, "must")):
        j = span_end(lines, site)
        splice(site, j, [ind(lines[site]) + q(MUST) + ","], "§16 " + label)

    i = find(lines, "{IDENTITY}")
    splice(i, i + 1, [ind(lines[i]) + q(MASTER)], "master")

    i = find(lines, "No person is in this frame at all:")
    j = find(lines, 'water.**"),', i)
    w = ind(lines[i])
    splice(i, j, [w + q(VMETA[0]), w + '"' + VMETA[1]], "visual_meta")

    i = find(lines, RESOLVED_ANCHOR)
    splice(i, i, [ind(lines[i]) + '"' + RESOLVED + tail_quote(lines[i])], "resolved_references")

    i = find(lines, CLAIM2)
    j = span_end(lines, i)
    splice(i, j, [], "unresolved (deleted)")

    i = find(lines, RISK_ANCHOR)
    j = span_end(lines, i)
    new = RISK_29 if fn == "s29.py" else RISK_SHORT
    w = ind(lines[i])
    splice(i, j, [w + q(x) for x in new[:-1]] + [w + q(new[-1]) + ","], "risks")

    if any(TYP0 in x for x in lines):
        i = find(lines, TYP0)
        splice(i, i, [lines[i].replace(TYP0, TYP1)], "typo")

    out = "\n".join(lines)
    ast.parse(out)
    io.open(path, "w", encoding="utf-8").write(out)
    print("=== %s ===" % fn)
    for x in log:
        print("   " + x)
print("OK - all four rewritten")
