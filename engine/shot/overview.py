#!/usr/bin/env python3
"""overview.py — **作品の概要を刷る。** 何を作るか、どこまで作ったかを、1枚に。

    使い方:  python3 engine/shot/overview.py projects/<project>
             python3 engine/shot/overview.py projects/<project> --no-changes
             python3 engine/shot/overview.py projects/<project> --episode ep03

⚠️ **`--episode` は `shots/<dir>/` から読んだショットだけを刷る。** ID の接頭辞では
   絞らない——命名は作品ごとに違う。空なら刷らない。保存名は `概要/<話>.md`。

⚠️ **これは読み取り専用である。** 1バイトも書かない——`projects/` にも、仕様にも、
   どこにも。**刷られた1枚を保存するかどうかは、著者が決める。**

⚠️ **数えるのは記録だけである。** `media/` は開かない。だからこの1枚は
   **「標本が在るか」を言わない**——言えるのは**「テイクとして記録されたか」**だけである。
   **置いたことは、記録したことではない。**

⚠️ **尺は記録の `duration` であり、意図である。** 生成物の尺は
   `take.params.duration` か `verdict.machine.measured.duration` に在る——
   **この1枚は、両者を突き合わせない**（`L23`・`L25` の持ち場である）。

⚠️ **`specs/board/` は記録から引けない。** ボードを指す欄が、ショットの記録に無いからだ。
   この1枚が言えるのは**紙が何枚在るか**だけで、**どのショットの紙かは言えない。**
"""

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

# ⚠️ **読み手を新しく書かない。** `engine/ledger` の `Project`・`semantic`・`specmap` を
#    そのまま使う——同じ記録を読む者が2人いれば、**片方だけ直したときに食い違う。**
sys.path.insert(0, str(HERE.parent / "ledger"))

try:
    import yaml  # noqa: F401  （`check`・`semantic` が要る）
except ImportError:
    sys.exit("PyYAML が要る: python3 -m pip install --user pyyaml")

import check     # noqa: E402
import semantic  # noqa: E402
import specmap   # noqa: E402


DUR = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*s?\s*$")


def sec(x):
    """秒を、桁を落とさずに書く。`8.0` は `8`、`10.500` は `10.5`。

    ⚠️ **`-0` を刷らない。** 浮動小数の差が -0.000 になるとき、
    `-0s` は**「負の差」という意味に見える**——差は算術であり、符号の主張ではない。
    """
    if x is None:
        return "—"
    if abs(x) < 5e-4:
        x = 0.0
    s = f"{x:.3f}".rstrip("0").rstrip(".")
    return f"{s}s"


def dur_of(shot):
    """ショットの `duration`。読めなければ `None`——**0 にしない。**"""
    d = (shot or {}).get("duration")
    if isinstance(d, (int, float)):
        return float(d)
    if isinstance(d, str):
        m = DUR.match(d)
        if m:
            return float(m.group(1))
    return None


def cell(x):
    """表の1セル。改行は潰し、`|` は逃がす——**どちらも行を割る。**"""
    if x is None:
        return "—"
    return " ".join(str(x).split()).replace("|", "\\|")


def cast_cell(shot):
    """枠に映る人物。⚠️ **欄が無いことと、空であることを分ける。**

    `cast` が無い＝**宣言していない**（`欠落`）、`[]`＝**誰も居ない**（`—`）。
    `reference_set` から代用しない——あれは「何を固定したか」であって、出演ではない。
    """
    c = (shot or {}).get("cast")
    if c is None:
        return "**欠落**（`cast`）"
    if not c:
        return "—"
    return "、".join(str(x) for x in c)


def change_of(shot):
    """1本の変化を、1つのセルに。⚠️ **要約しない。**

    ⚠️ **表のセルの中では、生の改行が使えない。** Markdown の表は行で区切られており、
    セルの中で改行すれば**表そのものが壊れる**。だから `<br>` で割る——
    **前と後を、縦に積む**ための唯一の方法である。
    """
    u = (shot or {}).get("unit") or {}
    before = one_line(u.get("before")) or "**欠落**（`unit.before`）"
    after = one_line(u.get("after")) or "**欠落**（`unit.after`）"
    return f"[前]<br>{before}<br>[後]<br>{after}"


def one_line(text):
    """散文を1行に。⚠️ **削らない。** 改行と連続する空白だけを潰す。"""
    return " ".join(str(text or "").split())


def at(project, rel):
    return (project.root / rel) if rel else None


def spec_file(project, shot, kind):
    src = semantic._spec_of(shot, kind)
    p = at(project, src)
    return (src, p) if p and p.is_file() else (src, None)


def takes_of(project, sid):
    """そのショットのテイク（`take` の袋）。**空なら空のまま返す。**"""
    return [((doc or {}).get("take") or {}) for doc in (project.takes.get(sid) or [])]


def adoption(takes):
    """採用の状態。⚠️ **欄が無いことは「却下」ではない**（作品の規律）。"""
    if not takes:
        return "—"
    yes = sum(1 for t in takes if t.get("adopted") is True)
    no = sum(1 for t in takes if t.get("adopted") is False)
    undecided = len(takes) - yes - no
    if yes:
        return f"採用 {yes}"
    if no:
        return f"却下 {no}"
    if undecided:
        return "未裁定"
    return "—"


def model_counts(project, order):
    """仕様の §18 が名乗るモデルを、ショットごとに数える。"""
    counts = {}
    unknown = 0
    for sid in order:
        src, path = spec_file(project, project.shots[sid], "video")
        if path is None:
            continue
        try:
            model = semantic._model_of(path)
        except (OSError, UnicodeDecodeError):
            unknown += 1
            continue
        if model:
            counts[model] = counts.get(model, 0) + 1
        else:
            unknown += 1
    return counts, unknown


def spec_places(project, order):
    """経路ごとの仕様の置き場——`specs/video/<経路>/<id>.md`。

    ⚠️ **`spec:` は1つしか名指さない。** 2つの経路を持つ作品では、
    もう片方は**ディレクトリの側にしか無い**——だからここだけは、記録ではなく
    **置き場を数える**。名前が `<id>.md` のものだけを数える。
    """
    base = project.root / "specs" / "video"
    if not base.is_dir():
        return []
    out = []
    for p in sorted(base.iterdir()):
        if p.is_dir():
            n = sum(1 for sid in order if (p / f"{sid}.md").is_file())
            if n:
                out.append((p.name, n))
    return out


def by_act(ledger, order):
    """`dramaturgy.acts` を、ショットIDの集合に均す。無ければ空。"""
    acts = ((ledger.get("dramaturgy") or {}).get("acts") or [])
    out = []
    for a in acts:
        if not isinstance(a, dict):
            continue
        shots = [s for s in (a.get("shots") or []) if s in set(order)]
        out.append((a, shots))
    return out


def main():
    ap = argparse.ArgumentParser(
        description="作品の概要を刷る — 何を作るか、どこまで作ったか")
    ap.add_argument("project", help="projects/<project> のパス")
    ap.add_argument("--no-changes", action="store_true",
                    help="変化の列（unit.before / after）を刷らない")
    ap.add_argument("--episode", metavar="DIR",
                    help="話ごとの下位ディレクトリ名（例 ep03）。その話のショットだけを刷る")
    a = ap.parse_args()

    root = Path(a.project)
    if not root.is_dir():
        sys.exit(f"{root} が無い")
    project = check.Project(root)

    # ⚠️ **読めなかったことを黙らない。** 空の記録は「0件」として通り、
    #    **「0件だから正しい」と読まれる。**
    for e in project.read_errors:
        print(f"⚠️ {e}", file=sys.stderr)

    order = project.order()
    if not order:
        sys.exit(f"{root} にショットが1本も無い"
                 "（⚠️ **「0件」は「違反0件」ではない**——`L0` が鳴らす形である）")

    # ⚠️ **話ごとの1枚は、読み元のディレクトリで絞る。** ID の接頭辞では絞らない——
    #    命名は作品ごとに違い、`shot_paths` は `Project` が読んだ事実そのものである。
    if a.episode:
        order = [s for s in order
                 if project.shot_paths.get(s)
                 and project.shot_paths[s].parent.name == a.episode]
        if not order:
            sys.exit(f"{root} の shots/{a.episode}/ にショットが無い"
                     "（⚠️ **空の概要を刷らない。**）")

    bible = (project.bible or {}).get("bible") or {}
    ledger = project.ledger or {}
    drama = ledger.get("dramaturgy") or {}
    song = bible.get("song") or {}
    slug = (project.bible or {}).get("project") or project.name

    durs = {sid: dur_of(project.shots[sid]) for sid in order}
    total = sum(v for v in durs.values() if v is not None)
    nods = sum(1 for v in durs.values() if v is None)

    video = {sid: spec_file(project, project.shots[sid], "video") for sid in order}
    image = {sid: spec_file(project, project.shots[sid], "image") for sid in order}
    takes = {sid: takes_of(project, sid) for sid in order}
    models, model_unknown = model_counts(project, order)
    places = spec_places(project, order)

    board = sorted((project.root / "specs" / "board").glob("*.md")) \
        if (project.root / "specs" / "board").is_dir() else []

    print(f"# 概要 — {project.name}"
          + (f" / {a.episode}" if a.episode else ""))
    print()
    print("⚠️ **この1枚は、記録から導出した。** 仕様でも記録でもない。")
    if a.episode:
        print(f"⚠️ **この1枚は `shots/{a.episode}/` の {len(order)}本だけを読んでいる。** "
              "作品全体は `概要.md` である。")
    print("⚠️ **この道具は何も書かない。** 刷るだけであり、保存するかは著者が決める。")
    print("⚠️ **`media/` は開かない。** 標本が在るかは、この1枚では言えない——"
          "言えるのは**テイクとして記録されたか**だけである。")
    print("⚠️ **尺は記録の `duration`（意図）であって、生成物の実測ではない。**")
    print()

    # ---------------------------------------------------------------- 0
    print("## 0. 何を作るか")
    print()
    print("| | |")
    print("|---|---|")
    print(f"| 作品 | `{slug}` |")
    style = bible.get("style")
    print(f"| 様式 | {cell(style) if style else '**欠落**（`bible.style`）'} |")
    lang = bible.get("language")
    print(f"| 言語 | {cell(lang) if lang else '**欠落**（`bible.language`）'} |")
    if models:
        named = "／".join(f"{k} {v}本" for k, v in sorted(models.items()))
        extra = f"（名乗らない {model_unknown}本）" if model_unknown else ""
        print(f"| 経路（仕様が名乗る） | {named}{extra} |")
    else:
        print("| 経路（仕様が名乗る） | **欠落**（動画の仕様が1本も無い） |")
    if places:
        print("| 経路ごとの仕様 | " +
              "／".join(f"{name} {n}本" for name, n in places) +
              "（`specs/video/<経路>/<id>.md`） |")
    if song:
        print(f"| 曲 | {sec(song.get('duration'))}／"
              f"{len(song.get('sections') or [])}節／"
              f"{len(song.get('lines') or [])}行（`bible.song`） |")
    else:
        print("| 曲 | **欠落**（`bible.song`） |")
    tail = f"（尺の読めない {nods}本を除く）" if nods else ""
    print(f"| ショット | **{len(order)}本**／合計 **{sec(total)}**{tail} |")
    print(f"| 連続性の語彙 | 人物 {len(ledger.get('characters') or {})}／"
          f"場所 {len(ledger.get('locations') or {})}／"
          f"道具 {len(ledger.get('props') or {})} |")
    disc = project.disclosure
    if a.episode:
        disc = [d for d in disc if d.get("shot") in set(order)]
    print(f"| 開示の変化点 | {len(disc)} 件 |")
    print()

    fields = (("premise", "何が起きるか"),
              ("question", "観客が持ち越す問い"),
              ("argument", "作品が言うこと"),
              ("visual_thesis", "視覚の主張"),
              ("ending_image", "最後に残るもの"))
    if drama:
        print("**作品の一行**——`dramaturgy` から。")
        print()
        for key, label in fields:
            if drama.get(key):
                print(f"- **{label}**: {one_line(drama[key])}")
            else:
                # ⚠️ **無い欄を黙って飛ばさない。** 飛ばせば、読む者は
                #    「その欄が無い」と「その欄が空である」を区別できない。
                print(f"- **{label}**: **欠落**（`ledger.dramaturgy.{key}`）")
        print()
    else:
        print("- **作品の一行**: **欠落**（`ledger.dramaturgy` そのものが無い）"
              "——`direction` が走っていない。")
        print()

    # ---------------------------------------------------------------- 1
    print("## 1. 段階ごとの現在地")
    print()
    print("| 段 | 現在 | 全体 | 出所 |")
    print("|---|---|---|---|")
    print(f"| ショットの記録 | {len(order)}本 | {len(order)}本 | "
          "`shots/*.yaml`・`shots/*/*.yaml`（話ごとの下位を一段だけ読む） |")
    v_ok = sum(1 for sid in order if video[sid][1])
    v_src = sum(1 for sid in order if video[sid][0])
    print(f"| 動画の仕様 | {v_ok}本 | {len(order)}本 | `spec:` が指すファイル"
          f"{f'（欄が無い {len(order) - v_src}本）' if v_src < len(order) else ''} |")
    i_ok = sum(1 for sid in order if image[sid][1])
    i_src = sum(1 for sid in order if image[sid][0])
    print(f"| 画像の仕様 | {i_ok}本 | {len(order)}本 | `key_image:` が指すファイル"
          f"{f'（欄が無い {len(order) - i_src}本）' if i_src < len(order) else ''} |")
    print(f"| ボードの紙 | {len(board)}枚 | — | `specs/board/*.md`"
          "——⚠️ **記録からは引けない** |")
    t_ok = sum(1 for sid in order if takes[sid])
    t_all = sum(len(takes[sid]) for sid in order)
    print(f"| テイク（記録） | {t_ok}本ぶん／{t_all}枚 | {len(order)}本 | "
          "`takes/*.yaml`・`takes/*/*.yaml`（話ごとの下位を一段だけ読む） |")
    adopted = sum(1 for sid in order for t in takes[sid] if t.get("adopted") is True)
    rejected = sum(1 for sid in order for t in takes[sid] if t.get("adopted") is False)
    undecided = t_all - adopted - rejected
    print(f"| 採用 | **{adopted}枚** | — | `take.adopted: true` |")
    print(f"| 却下 | {rejected}枚 | — | `take.adopted: false` |")
    print(f"| 未裁定 | {undecided}枚 | — | ⚠️ **`adopted` の欄が無い**"
          "——**却下ではない** |")
    print()
    if adopted:
        print(f"⚠️ **採用 {adopted}枚は、`adopted: true` を書いたテイクの数である。** "
              "**書いていないテイクは、採用でも却下でもない。**")
    else:
        print("⚠️ **「採用0枚」は「作品が無い」ではない。** 選別がまだ1度も書かれていない、"
              "という意味である。")
    print()

    # ---------------------------------------------------------------- 2
    acts = by_act(ledger, order)
    seqs = [s for s in ((drama.get("sequences") or [])) if isinstance(s, dict)]
    if acts or seqs:
        print("## 2. 幕とシーケンス")
        print()
        if acts:
            print("| 幕 | 本数 | ショット | 転換 | 山 | 価値 |")
            print("|---|---|---|---|---|---|")
            for act, shots in acts:
                value = f"{act.get('value_from', '—')} → {act.get('value_to', '—')}"
                print(f"| {cell(act.get('id'))} | {len(shots)} | "
                      f"{cell(shots[0]) + '–' + cell(shots[-1]) if shots else '—'} | "
                      f"{cell(act.get('turn'))} | {cell(act.get('climax'))} | {value} |")
            print()
        if seqs:
            print("| シーケンス | 本数 | 対比 | 欠けさせるもの | 切れ目 |")
            print("|---|---|---|---|---|")
            for s in seqs:
                shots = [x for x in (s.get("shots") or []) if x in set(order)]
                # ⚠️ **`withheld` は袋のことも、袋の列のこともある**（実測で両方在る）。
                #    形を決めつけない——**決めつければ、片方の作品でこの道具が落ちる。**
                wh = s.get("withheld")
                whs = wh if isinstance(wh, list) else ([wh] if isinstance(wh, dict) else [])
                parts = []
                for w in whs:
                    if isinstance(w, dict):
                        who = f"`{w.get('shot')}` " if w.get("shot") else ""
                        parts.append(f"{who}{one_line(w.get('wanted'))} → "
                                     f"{one_line(w.get('given'))}")
                withheld = "／".join(parts) or "—"
                cuts = s.get("cuts")
                if isinstance(cuts, list):
                    cuts = "内側で切る（" + "、".join(f"`{c}`" for c in cuts) + "）"
                elif cuts:
                    cuts = "内側で切る"
                else:
                    cuts = "—"
                print(f"| {cell(s.get('id'))} | {len(shots)} | "
                      f"{cell(s.get('contrast'))} | {cell(withheld)} | {cuts} |")
            print()
        if not acts:
            print("⚠️ **欠落**（`ledger.dramaturgy.acts`）——幕が1つも無い。")
            print()
        if not seqs:
            print("⚠️ **欠落**（`ledger.dramaturgy.sequences`）——シーケンスが1つも無い。")
            print()
    else:
        print("## 2. 幕とシーケンス")
        print()
        print("⚠️ **欠落**（`ledger.dramaturgy.acts`・`sequences`）——作品の上に重なる眺めが、"
              "まだ記録されていない（`L41` は対象外と言う）。")
        print()

    # ---------------------------------------------------------------- 3
    # ⚠️ **変化は、ショットの列と同じ表に置く。** 別の節に割ると、
    #    読む者は「どのショットの何が変わるか」を2箇所で突き合わせることになる。
    #    **流れは、1つの表を上から下へ読むことで追える。**
    print("## 3. ショットの列——変化の流れ")
    print()
    head = "| # | ショット | 人物（cast） | 役 | 場所 | 時刻 | 尺 | 動き（mode） |"
    rule = "|---|---|---|---|---|---|---|---|"
    if not a.no_changes:
        head += " 変化 |"
        rule += "---|"
    head += " 仕様 | 画像 | テイク | 採用 |"
    rule += "---|---|---|---|"
    print(head)
    print(rule)
    for i, sid in enumerate(order, 1):
        s = project.shots[sid]
        v = "在" if video[sid][1] else ("—" if not video[sid][0] else "**無**")
        im = "在" if image[sid][1] else ("—" if not image[sid][0] else "**無**")
        n = len(takes[sid])
        row = (f"| {i} | `{sid}` | {cell(cast_cell(s))} | {cell(s.get('role'))} | "
               f"{cell(s.get('place'))} | {cell(s.get('time'))} | {sec(durs[sid])} | "
               f"{cell(s.get('mode'))} | ")
        if not a.no_changes:
            row += f"{cell(change_of(s))} | "
        row += f"{v} | {im} | {n if n else '—'} | {adoption(takes[sid])} |"
        print(row)
    print()
    print("⚠️ **変化は `unit.before`（前）と `unit.after`（後）である。** "
          "1ショットは1つの変化のために在る——**要約していない。** "
          "表のセルの中では改行できないので、`<br>` で前と後を割っている。")
    print("⚠️ **`cast` は台帳の `characters` のキーである。** `—` は「誰も居ない」、"
          "`欠落` は「宣言していない」。**`reference_set` を出演の一覧として読まないこと**"
          "——あれは「何を固定したか」である。")
    print("⚠️ **`動き（mode）` の値**: `motion`＝主題が動く、`still`＝主題が止まる"
          "（光と粉塵は動く）、`composite`＝主題が止まり、画は層の合成である"
          "（生成器に文字を描かせない）。")
    print("⚠️ **仕様の「無」は、欄が在ってファイルが無いことである**（`—` は欄が無い）。"
          "**「0件」は「違反0件」ではない**——`check.py` が別に鳴る。")
    print()

    # ---------------------------------------------------------------- 4
    if song:
        print("## 4. 曲の区切り")
        print()
        sections = [x for x in (song.get("sections") or []) if isinstance(x, dict)]
        lines = [x for x in (song.get("lines") or []) if isinstance(x, dict)]
        line_sec = {x.get("id"): x.get("section") for x in lines}
        covered = set()
        per = {x.get("id"): [] for x in sections}
        seen = {x.get("id"): set() for x in sections}
        for c in (ledger.get("song_coverage") or []):
            if not isinstance(c, dict):
                continue
            sid_sec = c.get("section") or line_sec.get(c.get("line"))
            if c.get("line"):
                covered.add(c.get("line"))
            if sid_sec in per:
                # ⚠️ **1本が複数の行を覆うことがある**（`s07` が l03 と l04）。
                #    節ごとに重複を落とす——**落とさなければ尺を二度数える。**
                for s in (c.get("shots") or []):
                    if s in set(order) and s not in seen[sid_sec]:
                        per[sid_sec].append(s)
                        seen[sid_sec].add(s)
        print("| 節 | 時間 | 節の尺 | 本数 | ショット | 尺の合計 | 差 |")
        print("|---|---|---|---|---|---|---|")
        for x in sections:
            start, end = x.get("at"), x.get("until")
            span = (end - start) if isinstance(start, (int, float)) and \
                isinstance(end, (int, float)) else None
            shots = [s for s in per.get(x.get("id"), []) if s in set(order)]
            got = sum(v for v in (durs.get(s) for s in shots) if v is not None)
            diff = (got - span) if span is not None else None
            span_c = f"{start:.3f}–{end:.3f}" if span is not None else "—"
            print(f"| `{x.get('id')}` | {span_c} | {sec(span)} | {len(shots)} | "
                  f"{', '.join(f'`{s}`' for s in shots) or '—'} | {sec(got)} | "
                  f"{sec(diff) if diff is not None else '—'} |")
        print()
        n_lines = len(lines)
        if n_lines:
            print(f"⚠️ **歌詞行の被覆**: {len(covered)}／{n_lines} 行"
                  f"（`ledger.song_coverage` の `line` が名指した数）。")
        print("⚠️ **「差」は算術であって判定ではない。** 許容は `L34` が読む。"
              "ここでは両方を並べる。")
        print()
    else:
        print("## 4. 曲の区切り")
        print()
        print("⚠️ **欠落**（`bible.song`）——**曲を持たないと記録されている。** "
              "曲を持たないことが決定か、まだ書かれていないかは、この1枚では言えない。")
        print()

    # ---------------------------------------------------------------- 6
    print("## 5. 止まっているところ")
    print()
    no_v_field = [s for s in order if not video[s][0]]
    no_v_file = [s for s in order if video[s][0] and not video[s][1]]
    no_i_field = [s for s in order if not image[s][0]]
    no_i_file = [s for s in order if image[s][0] and not image[s][1]]
    no_take = [s for s in order if not takes[s]]
    no_adopt = [s for s in order if takes[s]
                and not any(t.get("adopted") is True for t in takes[s])]
    bad_dur = [s for s in order if durs[s] is None]

    def listing(ids):
        if not ids:
            return "—"
        if len(ids) <= 20:
            return "、".join(f"`{s}`" for s in ids)
        return "、".join(f"`{s}`" for s in ids[:20]) + f" ほか {len(ids) - 20}本"

    print("| 止まっている段 | 本数 | ショット |")
    print("|---|---|---|")
    print(f"| 動画の仕様の欄が無い | {len(no_v_field)} | {listing(no_v_field)} |")
    print(f"| 動画の仕様のファイルが無い | {len(no_v_file)} | {listing(no_v_file)} |")
    print(f"| 画像の仕様の欄が無い | {len(no_i_field)} | {listing(no_i_field)} |")
    print(f"| 画像の仕様のファイルが無い | {len(no_i_file)} | {listing(no_i_file)} |")
    print(f"| テイクが1枚も無い | {len(no_take)} | {listing(no_take)} |")
    print(f"| テイクは在るが採用が無い | {len(no_adopt)} | {listing(no_adopt)} |")
    print(f"| 尺が読めない | {len(bad_dur)} | {listing(bad_dur)} |")
    print()
    print("⚠️ **「止まっている」は欠陥ではない。** 段は上から順に走る——"
          "**採用が無いのは、著者がまだ選んでいないという意味である。**")
    print("⚠️ **欄が無いことは、決定のことがある**——`MINIMAX H3` の経路は"
          "画像の仕様をまったく持たない。**理由は記録の註に在る**——"
          "**この1枚は理由を読まない。**")
    print()

    # ---------------------------------------------------------------- 7
    print("## 6. この1枚が言っていないこと")
    print()
    print("- **標本が在るか。** `media/` を開いていない——**記録と実物の食い違いは鳴らない。**")
    print("- **画の良し悪し、テイクの選別。** この1枚は数えるだけで、判定しない。")
    print("- **並びの正。** `timeline/` を読んでいない——並びはショットIDの自然順である"
          "（`Project.order()` がそう言う）。")
    print("- **ボードの対応。** `specs/board/` は記録から引けない——"
          "数はファイルを数えただけで、どのショットの紙かは言えない。")
    print("- **違反。** この道具は検査しない——`python3 engine/ledger/check.py <project>` を別に回す。")
    print("- **作品の良さ。** どの層も読まない。**それは著者の判断である。**")
    print()
    print("⚠️ **`**欠落**（在処）` は、その場所に値が無いことを言う。** "
          "**欠落は欠陥ではない**——不在が決定のこともある。この1枚は在処を名指すだけで、"
          "理由を読まない。")
    print("⚠️ **この道具は、何も決めない。** 記録から導出した1枚を刷るだけである。")


if __name__ == "__main__":
    sys.exit(main())
