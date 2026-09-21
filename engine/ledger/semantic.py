"""semantic.py — JSON Schema が書けない検査。

**なぜ別の層が要るか。** `schemas/` が保証するのは**形**である。`unit` を
`{ before, after }` の対にしたのは「`before` と `after` が同じ」を鳴らすためだったが、
**JSON Schema は2つのプロパティを比較できない**——標準の仕様にその機能が無い。
`if`/`then` + `const` は**列挙**であって比較ではなく（自由文なので閉じない）、
`$data` 参照は標準仕様に入らなかった提案である。**測って確かめてある**（`HISTORY.md`）。

**だからここが負う。** 検査は六つの層に分かれる。

  層A  ショット1枚の中で閉じる検査（一変化・一環境・一時刻・一運動）
  層B  台帳と突き合わせる検査（参照・禁制・開示・出所）
  層C  入力そのものの検査（**空を OK と言わない**・**読まなかったものを名指しする**）
  層D  §1–20 との対応の検査（目録・両方向の閉包・同一性・**仕様の種類とモデル**・
       **画像の経路の中身**・**尺の一致**）
  層E  宣言の到達の検査（**台帳が届いていない区間**）
  層F  **目録そのものの検査**（種別・運動の層・§18 のスロット・**欄の行き先**・
       **`mode` が要求するもの**——**登録が読まれているか、行き先が実在するか**）

⚠️ 層C を最初に置く理由。**相手が空なら、層A も層B も一件も鳴らない。**
鳴らないことは、正しいことの証明ではない——`0 == 0` が通った実例が既にある。

⚠️ 層F を足した理由。**登録するだけでは、目録は読まれない。** 実測で
**17欄のうち7欄をどの検査も読んでいなかった**（`README.md`）。うち `motion` は
**読むと名指しされていた検査が存在しなかった。** だから目録を足すときは、
**それを読む検査を同時に足す**——L15・L16・L17 がそれである。

⚠️ **いま読まれていないのは2欄である**——`effect`・`sound`。
**`duration` と `text_channel` は `L23`・`L24` が読むようになった**（決定 2026-09-13）。
残る2欄はいずれも読み手が別の層にいる（⑦検収／Semantic Audio Loom。契約は M6）ので、
**この層で鳴らす話ではない。** 数の出所は `HISTORY.md`。

⚠️ **L18・L19・L20 を足した理由（決定 2026-09-13、U02）。**
作品が**複数の生成の仕組み**を使えるようになった——動きのあるショットは動画モデル、
静的なショットは**別の仕組み**（このリポジトリを通らない）。すると2つのことが
成り立たなくなる。

  1. **「全ショットが §1–20 を持つ」は成り立たない。** 画像プロンプトは節を持たない。
     `L11` を `mode` で絞らねば、**静的なショットで誤って鳴る**（L18 がその絞り方を持つ）。
  2. **「欄は生成へ渡る」も成り立たない。** 日本語の欄は渡らず、尺は編集で決まり、
     参照は API の引数になり、音は別基盤へ行く。**行き先の宣言が無い欄は、
     黙って落ちる**——これが `L19` である。**「狙いが届く」ことの機械的な形。**

⚠️ **`L20` は空の行き先を鳴らす。** `Style Motion` の出所は様式カードの
`Motion character` であり、**実測で55枚のうち2枚しか持たない**。
持たない様式を選べば、**スロットは在るのに何も運ばない**——`L17` はそれを通す。
**空の検査は OK と言う。** だから別に鳴らす。

⚠️ **`L21` は両方の経路を見るようになった（決定 2026-09-18、著者）。** それまでは
画像の経路だけを見ており、**動画の §18 を読む検査は「まだ無い——穴である」と
記録されていた。** その穴から実際の欠陥が出た——**動画に中国語の字幕が焼かれた。**
**禁制が届かなかったのは、動画の経路である。** 同時に、要求が
**基盤の禁制（`specmap.BASE_NEGATIVES`）＋ 作品の禁制（`bible.negative_base`）**の
和になった——**作品が書き忘れても消えない床を、基盤が持つ。**

⚠️ **`L27` を足した理由（決定 2026-09-18、著者）——「言語指定で触っているなら、
必ずその言語を話す」。** それまでこの基盤は、**作品が何語で話すかをどこにも
書けなかった**（`bible` に `language` が無く、§14 AUDIO の定義にも無かった）。
**空欄は、生成器の既定で埋まる**——Wan 3.0 の既定は中国語である。
`L27` は**宣言**（`bible.language`）と**到達**（§18 `Audio Prompt`）を見る。
⚠️ **生成物が実際にその言語で喋ったかは見えない**——穴である。

⚠️ **`L28` を足した理由（決定 2026-09-20、著者）——「この生成手法で上手く生成させる
ための Tips を、基本的な制約へ格上げする」。** 経路が2つ在るのに、**時間の文法が
2つ在ることを検査は見ていなかった。** 実測——`MINIMAX H3` の §18 が
`One continuous take … never by a cut` と書き（**それは `WAN 3.0` の家風である**）、
**生成器は受付の机と車内を、ひと続きの部屋として走らせた。**
`L28` は**その語がその経路のものか**だけを見る（`specmap.MODEL_ROUTE`）。
⚠️ **意味は見ない**——平板な否定が欠陥かどうかは**実体の台帳**が要る。穴である。
⚠️ **`MINIMAX H3` の §18 を持たない作品では、1文字も出ない**——**それも穴である。**

⚠️ **`L29` を足した理由（決定 2026-09-20、著者）——「作品が作品を抱えてはならない」。**
`check.py` は再帰しない。ゆえに**作品が作品を抱えていると、親を走らせても子は読まれず**、
**しかも出力はそれを言わない**——**読み手は読んだと思う。** 実測: `check.py projects/habits` は
4本を読み、**出力に `promo-chinatsu` は0回**であった。**実害は既に出ている**——
0.29.0 が台帳の一覧からこの作品を落としかけた（**`find -maxdepth 2` では見えない**）。
`projects/habits/promo-chinatsu` は**直下へ出した**（`projects/habits-promo-chinatsu`）。
⚠️ **根が作品であるときだけ違反である**——題材の置き場（`projects/ukebi`）が作品を抱えるのは
**正しい**（親に台帳が無いので、読まれると思われようがない）。**そちらは註である。**

⚠️ **`L31` を足した理由（決定 2026-09-21、著者）。** それまでこの基盤は、
**作品が名乗る様式（`bible.style`）と、動画の仕様の §6 `REFERENCES` が名乗る様式を、
一度も突き合わせていなかった。** `L17` は仕様にスロットが**在る**ことを見て、
`L20` はそのスロットの**行き先が空でない**ことを見る——**だが、両方に書かれた名は
誰も読まなかった。** 穴は文書化されていた——`engine/shot/README.md` が
「**形が安定していない欄は、導出できない**」と書いており、**§6 は機械の読み手を
持たなかった。** 実測（2026-09-21、動画の仕様118本）: **49本が `- REF_STYLE:` の行で
名乗り**（名乗り形19本・em ダッシュ形30本）、**69本は §6 を小節で持ち `- Source:` に
パスを書く**（`gozen-niji` 57・`ukebi/ukebi-video-*` 12——**どちらも家を持たない**）。
語彙も2つに割れている（**カード名 19本・パス 99本**、同じ `luminous-anime` を
ある作品は名で、ある作品は `references/styles/…md` と書く）。
`L31` は**両方を1つの名に畳んでから**比べる——ゆえに**語彙が違っても鳴らない。**
⚠️ **カードを1枚も開かない。** ゆえに**「様式が正しく適用されたか」を何も言わない**
——**「2つの層が同じ名を名乗っているか」だけを言う。** 穴である。
⚠️ **どちらの語彙が正かは決めない**——**新しい仕様を何で書くかは、いまも未決定である。**
⚠️ **家を持たない作品では鳴らない**（`L17` が「様式を宣言していない」で鳴らす）
——**同じ欠陥を2つの層が別々の符号で報告しない。**

⚠️ **`L21`–`L24` を足した理由（決定 2026-09-13、著者）。** 経路が1つから**2つ**になり
（全ショット画像 → 全ショット動画）、**経路を決めるのが `mode` でなくなった**。
`L21`・`L22` は**画像の経路の中身**を見る——あちらは §1–20 を持たないので、
`L11` は原理的にあちらを見られない。`L23` は**意図と仕様の尺**を突き合わせる
（**値で突き合わせてよいと実測で確かめた唯一の欄である**——`place`・`time` を
値で比べれば60件の偽陽性が出る）。`L24` は**`mode` が要求するもの**を見る
——`L16` が `mode` を読まなくなったので、**ここが `mode` の唯一の読み手である。**
"""

import collections
import json
import re
from pathlib import Path

import rolemap
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


def check_nested_works(project):
    """⚠️ **この走りが読まない作品を、名指しする。**

    **作品が作品を抱えていると、`check.py` は再帰しない**（`shots/*.yaml` を平らに読む）——
    親を走らせても、**子は1本も読まれない。** そして出力はそれを言わない。
    実測（2026-09-20）: `check.py projects/habits` は4本を読み、
    **出力に `promo-chinatsu` は0回**であった。**読み手は読んだと思う。**

    ⚠️ **根が作品であるときだけ違反である。** 作品が作品を抱えることは、
    **この基盤の規則に反する**——`docs/usage.md`「What a project is」。
    根が作品でなければ（`projects/ukebi` のような題材の置き場）、
    **註である**——**題材の置き場を走らせる者は、そもそも読まれると思っていない。**
    """
    root = project.root
    below = []
    for b in sorted(root.glob("**/bible.yaml")):
        d = b.parent
        # ⚠️ **`bible.yaml` だけでは作品ではない。** 作品は台帳も持つ。
        if ".git" in d.parts or d == root or not (d / "ledger.yaml").is_file():
            continue
        below.append(d)
    if not below:
        return []

    rel = [str(d.relative_to(root)) for d in below]
    named = "、".join(f"`{r}`" for r in rel[:3])
    if len(rel) > 3:
        named += f" ほか {len(rel) - 3} 本"

    msg = (f"この下に別の作品が {len(rel)} 本在る——{named}。"
           "**この走りはそれらを1本も読まない。**")
    if project.bible:
        msg += ("⚠️ **そして、このディレクトリはそれ自体が作品である**"
                "——**作品が作品を抱えている。**")
    msg += "**作品ごとに走らせること。**"
    return [finding("L29", f"{len(rel)}本", msg,
                    severity="violation" if project.bible else "note")]


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
    """L2 — 一環境か。**D1 の移植。** 連続テイク1本に複数環境は物理的に不可能。

    ⚠️ **その前提は `WAN 3.0` の経路のものである。** `MINIMAX H3` の経路では、
    絵コンテの**各コマがそれ自体で1つのシーン**であり、**1つのショットが複数の場所を正当に持つ。**
    ⚠️ **この層はそれを読めない**——見るのは台帳の `place` ただ1つであり、
    §10 のカメラの記述も §18 の文字列も開かない。**だから鳴らない。**
    **何も見なかった層は、通った層とまったく同じに見える**——ここに穴として書く。
    ⚠️ **挙動は変えない。** 検出するには `spec` を読むことになり、波及が大きい。
    """
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

        # ⚠️ **動画の仕様が無ければ、§18 では確かめられない。**
        #    ——**検査が空なのではなく、相手が違う。** 相手は画像プロンプトであり、
        #    それを読むのは引き渡しの層である（だから註であって、違反ではない）。
        #    ⚠️ **決定（2026-09-13）の前は、ここが「画像のショットだから」だった。**
        #    いまは**全ショットが動画の仕様を持つ**ので、`mode` は理由にならない
        #    ——理由は**記録が無いこと**である。読めないものを読んだ顔をしない。
        # ⚠️ **`L11`・`L18` と同じ規則（`_spec_of`）を使う。**
        if _spec_of(project.shots[target], "video") is None:
            declared_img = (cp.get("raw") or {}).get("negative")
            out.append(finding("L10", str(target),
                               f"`mode: {project.shots[target].get('mode')}` の変化点である。"
                               "**このショットには動画の仕様（`spec:`）が無い**——"
                               "この変化点は §18 に対しては確かめられない。"
                               "相手は画像プロンプトであり、**引き渡しの層が読む**（段2）。"
                               + (f"⚠️ 宣言された `negative: {declared_img}` は §18 の話であり、"
                                  "**このショットでは読まれない。**" if declared_img else ""),
                               severity="note"))
            continue

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
        # ⚠️ **相手は「直前の §18 を持つショット」である。** 素朴に1つ前を見ると、
        #    間に動画の仕様を持たないショットが挟まった瞬間に「`spec:` が無い」と鳴る
        #    ——**無いのではなく、相手が違う。** 動画の層は連続していない。
        prev = next((order[j] for j in range(i - 1, -1, -1)
                     if _spec_of(project.shots[order[j]], "video") is not None), None)
        if prev is None:
            out.append(finding("L10", str(target),
                               "先行する §18 を持つショットが無い。"
                               "**「変わった」を言えない。**"
                               "（先頭であっても、動きの層の先頭であっても同じである。）",
                               severity="note"))
            continue

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
    src = _spec_of(project.shots[shot], "video")
    if not src:
        raise _NoSpec(f"ショット {shot} に `spec:` が無い。**§18 を読む相手が分からない。**"
                      "記録が無いので、この変化点は検査されていない。")
    try:
        return specdoc.negative_prompt(project.root / src)
    except FileNotFoundError:
        raise _NoSpec(f"ショット {shot} の `spec: {src}` が読めない。")


# ---------------------------------------------------------------- 層D 対応の検査

TOP_SECTION = re.compile(r"^(\d+)\.\s+(\S.*?)\s*$")


def _spec_of(shot, kind):
    """そのショットの、**その種類の**仕様の在り処。`SPEC_KINDS` を引く唯一の場所。

    ⚠️ **規則と、規則を使う検査を離さない。** `L10`・`L11`・`L13`・`L14`・`L17`・`L18` が
    ここを通る——同じ絞り方を各所に写せば、**片方だけ直したときに、もう片方が
    別の符号で同じ欠陥を唄る。** 実際にそれが起きた: 混ざった並びを測ると
    `L10` は「`spec:` が無い」と偽り、`L13` は「仕様が自分を名乗っていない」と偽り、
    `L17` は「スロットが1つも無い」と偽った——**3つとも、無いのではなく種類が違う。**

    ⚠️ **経路は `mode` ではなく欄が決める。** 決定（2026-09-13、著者）
    「全ショット画像 → 全ショット動画」の下では、**10本すべてが両方を持つ**——
    だから `mode` は引かれない。引くのは `SPEC_KINDS[kind]["field"]` である。

    ⚠️ **`None` は「もう一方の種類である」ではない。** 呼び手は `is None` で絞る
    ——**分からないことを理由に検査を飛ばさない**（`L18` が「記録が無い」と報告する）。
    """
    return (shot or {}).get(specmap.SPEC_KINDS[kind]["field"]) or None


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

    ⚠️ **動画の仕様を持たないショットは、ここでは検査しない。** 相手は §1–20 を
    持つ仕様だけである。**その一致は `L18` が見る**——片方だけを
    直せば、もう片方が別の符号で同じ欠陥を唄ることになる。

    ⚠️ **決定（2026-09-13）の前は「`mode` が画像を要求するショット」と書いていた。**
    いまは**全ショットが動画の仕様を持つ**ので、`mode` は絞り方にならない。
    """
    out = []
    if len(specmap.SPEC_SECTIONS) != 20:
        out.append(finding("L11", "", f"目録の節が {len(specmap.SPEC_SECTIONS)} 個である。"
                                      "20 のはずである——**目録が短くなれば、足された節を鳴らせない。**"))
    want = list(specmap.SPEC_SECTIONS)
    seen = 0
    for s in project.order():
        shot = project.shots[s]
        src = _spec_of(shot, "video")
        if not src:
            out.append(finding("L11", s, "`spec:` が無い。**このショットの動画の仕様は"
                                         "検査されていない。**"))
            continue
        p = project.root / src
        if not p.is_file():
            out.append(finding("L11", s, f"`spec: {src}` が読めない。"))
            continue
        # ⚠️ **族を均してから比べる。** §18 はモデル名を名乗るので、生の見出しでは
        #    一致しない——**均すのは突き合わせのためであり、報告は生の見出しで行う。**
        raw = _spec_tops(p)
        got = [specmap.canonical(t) for t in raw]
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
                                               "**節が足されれば鳴る。**",
                      severity="note"))
    else:
        out.append(finding("L11", "", "§1–20 を **1本も** 確かめていない。"
                                      "**検査が空である**——違反0件は「正しい」ではない。",
                      severity="note"))
    return out


def _section_body(path, prefix):
    """トップレベルの節の本文を、**小節ごと**返す。`specdoc.section` では足りない。

    ⚠️ **`specdoc.section` は見出しの水準を問わずに割る。** だから `# 11. MOTION` の
    直後に `## Subject Motion` が来ると、**§11 の本文は空になる**——実測で
    そうなっている（`hitosara/specs/video/shot-04-knead.md` の §11）。**節の中身は
    小節にある。** 「空である」と読んでよいのは、**小節も全部空のときだけ**である。

    ⚠️ **画像の仕様に対しては `""` を返す。** あちらは節を持たないのが正しい形である
    （`L18`）。呼び手は「空」と「節が無い」を混同しないこと。
    """
    out, inside = [], False
    for t, body in specdoc.sections(Path(path).read_text(encoding="utf-8")):
        if TOP_SECTION.match(t):
            inside = t.startswith(prefix)
            if inside and body:
                out.append(body)
            continue
        if inside and body:
            out.append(body)
    return "\n".join(out).strip()


def _model_of(path):
    """仕様の §18 が名乗るモデル。§18 が無ければ `None`、名乗らなければ `""`。"""
    for t in _spec_tops(path):
        if specmap.canonical(t) == "18. PROMPT MAPPING":
            return specmap.named_model(t) or ""
    return None


def check_spec_kind(project):
    """L18 — **2つの経路が、それぞれの形をしているか。**

    ⚠️ 決定（2026-09-13、著者）——**全ショット画像 → 全ショット動画。**
    だから **`mode` は仕様の種類を決めない。経路は欄が決める**（`SPEC_KINDS`）。
    `spec` が動画の仕様、`key_image` が画像の仕様であり、**10本すべてが両方を持つ。**

    ⚠️ **`L11` の絞り方は、ここが持つ。** どの仕様が §1–20 を持つべきかを決めるのは
    `SPEC_KINDS[kind]["sections"]` であり、`L11` は `_spec_of` を通してそれに従う。
    **規則と、規則を使う検査を離さない。**

    ⚠️ **モデルが要る理由。** §18 は**モデル固有の投影**である——同じ §1–17 が、
    モデルが変われば別の文になる。**どのモデルへ束ねたかが書かれていなければ、
    `Style Motion` が何を引くのかも、`duration` がどこへ行くのかも決まらない。**

    ⚠️ **画像の仕様が無いことは、違反ではない。** 記録が無いのであって、
    食い違っているのではない——**だから註であり、しかも1件に畳む**
    （30本ぶんの註は、30本ぶんの情報ではない）。受け火 V2 の30本がここに落ちる。
    """
    out = []

    # ① 目録そのものが壊れていないか。**経路が2つとも引けねばならない。**
    fields = [v.get("field") for v in specmap.SPEC_KINDS.values()]
    if not specmap.SPEC_KINDS:
        out.append(finding("L18", "", "`SPEC_KINDS` が空である。**経路が1つも無い。**"))
    # ⚠️ **目録そのものが短くなっていないか。** L11（20節）・L15（12種）と同じ形である。
    #    種類を1つ落とせば、**その経路は誰にも検査されない**——しかも黙って落ちる。
    #    2 は決定（2026-09-13、著者）「全ショット画像 → 全ショット動画」の数である。
    if len(specmap.SPEC_KINDS) != 2:
        out.append(finding("L18", "",
                           f"経路の目録が {len(specmap.SPEC_KINDS)} 種類である。"
                           "2 のはずである（動画と画像）——**経路が1つ落ちれば、"
                           "その経路は誰にも検査されない。**"))
    if any(not f for f in fields):
        out.append(finding("L18", "", f"`SPEC_KINDS` に欄を持たない種類がある: "
                                      f"{sorted(specmap.SPEC_KINDS)}。"))
    if len(set(fields)) != len(fields):
        out.append(finding("L18", "",
                           f"`SPEC_KINDS` の2つの種類が同じ欄を指している: {fields}。"
                           "**同じファイルを動画の仕様とも画像の仕様とも読むことになる。**"))
    if any(not v.get("negative") for v in specmap.SPEC_KINDS.values()):
        out.append(finding("L18", "", "`SPEC_KINDS` に、Negative の見出しを持たない種類がある。"))
    # ⚠️ **様式の4欄を宣言した種類は、その節の見出しも持たねばならない。**
    #    片方だけでは `L22` が「何を確かめればよいか分からない」で止まる。
    for kind, spec in sorted(specmap.SPEC_KINDS.items()):
        if spec.get("vars") is not None and not spec.get("vars_section"):
            out.append(finding("L18", "",
                               f"`SPEC_KINDS['{kind}']` が様式の欄を宣言しているのに、"
                               "その節の見出し（`vars_section`）を持たない。"
                               "**欄の名前だけでは、仕様のどこを読むのかが決まらない。**"))
    # ⚠️ **段落を名乗る種類は、「その段落がどの節に入っているか」も名乗らねばならない。**
    #    片方だけでは `L21` が「何を読めばよいか分からない」で止まる
    #    （`vars`・`vars_section` と同じ形である）。
    for kind, spec in sorted(specmap.SPEC_KINDS.items()):
        paras = spec.get("body_paragraphs")
        if paras is None:
            continue
        if not spec.get("body_section"):
            out.append(finding("L18", "",
                               f"`SPEC_KINDS['{kind}']` が段落の並びを名乗っているのに、"
                               "その段落が入る節の名前（`body_section`）を持たない。"
                               "**段落の名前だけでは、仕様のどこを読むのかが決まらない。**"))
        # ⚠️ **`negative` は「Negative がどこか」を指す。** 段落の並びに無い名前を
        #    指していれば、**その種類の Negative は誰にも読めない。**
        if spec.get("negative") not in paras:
            out.append(finding("L18", "",
                               f"`SPEC_KINDS['{kind}']` の `negative`（`{spec.get('negative')}`）が"
                               f"`body_paragraphs`（{'／'.join(paras)}）に無い。"
                               "**指す先が名乗られていなければ、Negative は読めない。**"))

    seen = collections.Counter()
    missing = collections.Counter()
    for s in project.order():
        shot = project.shots[s]
        for kind, spec in sorted(specmap.SPEC_KINDS.items()):
            src = _spec_of(shot, kind)
            if not src:
                missing[kind] += 1
                continue
            p = project.root / src
            if not p.is_file():
                # ⚠️ **欄は在るのに開けない。** 動画の側は L11 も鳴らすが、
                #    ここでは「開けない」ことだけを言う——**同じ欠陥を2つの層が
                #    別々の符号で報告しない**よう、動画の不在は L11 に譲る。
                if kind != "video":
                    out.append(finding("L18", s, f"`{spec['field']}: {src}` が読めない。"
                                                 f"**{kind} の仕様が在ると書いてあるのに開けない。**"))
                continue
            has_sections = bool(_spec_tops(p))
            seen[kind] += 1

            if spec["sections"] and not has_sections:
                continue                  # L11 が「目録にある節が無い」で鳴らす
            if not spec["sections"] and has_sections:
                out.append(finding("L18", s,
                                   f"`{spec['field']}` の仕様が §1–20 を持っている。"
                                   "**画像プロンプトは節を持たない**——"
                                   "`video-spec` 自身が「他のカードはすべて穴埋めの一文で終わる」と"
                                   "書いている。**画像の経路へ動画の仕様を当てている。**"))
                continue
            if kind != "video":
                continue

            model = _model_of(p)
            if model is None:
                continue                  # §18 が無い。L11 が鳴らしている
            if model == "":
                out.append(finding("L18", s,
                                   "§18 が**モデルを名乗っていない**（`18. PROMPT MAPPING`）。"
                                   "**§18 はモデル固有の投影である**——"
                                   "どのモデルへ束ねたかが書かれていなければ、"
                                   "この節が何を引くのかを誰も読めない。"))
                continue
            m = specmap.MODELS.get(model)
            if m is None:
                out.append(finding("L18", s,
                                   f"§18 が名乗るモデル `{model}` が `MODELS` に無い。"
                                   f"登録されているモデル: {'／'.join(specmap.MODELS)}。"
                                   "**登録されていないモデルへ束ねた仕様は、"
                                   "そのモデルの性質を誰も知らない。**"))
                continue
            if m["種別"] != kind:
                out.append(finding("L18", s,
                                   f"§18 は `{model}`（{m['種別']}）を名乗るが、"
                                   f"`{spec['field']}` は **{kind}** の経路である。"
                                   "**生成の仕組みが違うものを当てている。**"))

    # ② **画像の経路が無いことを、1件に畳んで報告する。**
    #    ⚠️ **「記録が無い」と「食い違っている」は別である。**
    for kind, n in sorted(missing.items()):
        if kind == "video":
            continue                      # L11 が1本ずつ鳴らしている
        out.append(finding("L18", "",
                           f"**{n} 本が `{specmap.SPEC_KINDS[kind]['field']}` を持たない。**"
                           "経路が1つしか書かれていない——"
                           "⚠️ **記録が無いのであって、食い違っているのではない。**"
                           f"だから違反ではない。**だが、この {n} 本の画像の側は"
                           "一度も検査されていない。**", severity="note"))

    if seen:
        out.append(finding("L18", f"{sum(seen.values())}本",
                           "2つの経路の形を確かめた（"
                           + "／".join(f"{k} {v} 本" for k, v in sorted(seen.items()))
                           + "）。**動画は §1–20 を持ち、画像は持たない。**",
                           severity="note"))
    else:
        out.append(finding("L18", "", "仕様を **1本も** 確かめていない。**検査が空である。**",
                           severity="note"))
    return out


def _stem(clause):
    """禁止の語から**語幹**を取る。**`L21` の比較の単位である。**

    ⚠️ **禁止の語を文字列で比べてはならない。** 実測——受け火 V2 の台帳は
    `no photorealistic` と書き、§18 は `not photorealistic` と書く。
    **生の文字列で比べれば 30/30 が偽陽性になる。**
    否定の語は意味を持たず、**意味を持つのは語幹のほうである**
    （`L4` が「移動」を動詞で判定したときに踏んだのと同じ形の誤りである）。
    """
    c = specmap.NEGATOR.sub("", str(clause).strip().lower())
    return re.sub(r"\s+", " ", c).strip()


def _specs_of(project, kind):
    """その経路の仕様を `[(ショットID, パス)]` で返す。**読めないものは数えない。**

    ⚠️ **「記録が無い」は `L18` が1件に畳んで報告する**——**同じ欠陥を2つの層が
    別々の符号で報告しない。** だからここは黙って落とし、呼び手も黙って帰る。
    """
    out = []
    for s in project.order():
        src = _spec_of(project.shots[s], kind)
        if not src:
            continue                      # L18 が「持たない」と報告している
        p = project.root / src
        if not p.is_file():
            continue                      # L18 が「読めない」と報告している
        out.append((s, p))
    return out


def _negative_of(path, kind):
    """その仕様の Negative を**節の列**として返す。`(節, 欠陥の文)`——片方は必ず `None`。

    ⚠️ **種類ごとに指し方が違う**（`specmap.SPEC_KINDS`）。動画は**節の見出し**
    （`## Negative Prompt`）、画像は**1つの節の中の2段落目**である。
    **指しているものは同じで、指し方が違う。**

    ⚠️ **段落の数も見る。** 「2段落である」は名乗りであって、**名乗りは一致ではない**
    （`L22` のカードの名乗りと同じ形）。**数が違えば、`index` は別の段落を指す**
    ——黙って読むと、`Prompt` を Negative として読む。
    """
    k = specmap.SPEC_KINDS[kind]
    text = path.read_text(encoding="utf-8")
    if not k["sections"]:
        body = specdoc.section(text, k["body_section"])
        if body is None:
            return None, (f"`{k['field']}` の仕様に `## {k['body_section']}` の節が無い。"
                          "**禁制を1つも確かめられない**——"
                          "節が無いのは、禁制が揃っていることではない。")
        names = k["body_paragraphs"]
        paras = specdoc.paragraphs(body) or []
        if len(paras) != len(names):
            return None, (f"`{k['body_section']}` の節が "
                          f"{len(names)} 段落（{'／'.join(names)}）であるはずが、"
                          f"**{len(paras)} 段落である。**"
                          "**段落の数が違えば、どこを読んでいるのかが決まらない**"
                          "——`Negative` を読んだつもりで `Prompt` を読むことになる。")
        return specdoc.clausify(paras[names.index(k["negative"])]), None
    body = specdoc.section(text, k["negative"])
    if body is None:
        return None, (f"§18 に `## {k['negative']}` の節が無い。"
                      "**禁制を1つも確かめられない**——"
                      "節が無いのは、禁制が揃っていることではない。")
    return specdoc.clausify(body), None


def check_negative_coverage(project):
    """L21 — **両方の経路の Negative が、基盤と作品の禁制を覆っているか。**

    ⚠️ **覆うであって、等しいではない。** Negative は要求された禁制を
    **全部含まねばならない**が、**それ以上を持ってよい**——開示の系列
    （「窯の中を見せない」等）は**ショットごとに違う**からである。
    だから足りない節だけを鳴らし、余分な節は鳴らさない。

    ⚠️ **要求は2層の和である**（決定 2026-09-18、著者）。
      · **基盤が必ず付けるもの**（`specmap.BASE_NEGATIVES`）——作品が書き忘れても消えない。
      · **作品が決めるもの**（`bible.negative_base`）——作品ごとに違う。
    どちらか一方でも欠ければ鳴る。**和でなければ、基盤の層は床にならない。**

    ⚠️ **語幹で比べる**（`_stem`）。`no` / `not` の違いは偽陽性である。

    ⚠️ **かつてこの検査は画像の経路しか見ていなかった。** 動画の §18 を読む検査は
    「まだ無い——穴である」と記録されていた。**その穴から実際の欠陥が出た**
    （実測 2026-09-18——動画に**中国語の字幕が焼かれた**）。
    **禁制が届かなかったのは、動画の経路である。** だから両方を見る。

    ⚠️ **相手が1本も無ければ、何も言わずに帰る。** 「記録が無い」ことは `L18` が
    1件に畳んで報告する——**同じ欠陥を2つの層が別々の符号で報告しない。**

    ⚠️ **祖父条項がある**（`specmap.WAIVED_KEY`、決定 2026-09-18、著者——「**hitosara は
    対象外にする**」）。基盤の禁制は増える。**規則より前に書かれた作品**には、書いていなかった
    ことを理由に赤が立つ——**規則は遡らない。** ゆえに**作品が自分で除外を宣言する。**
    ⚠️ **除外は註で報告する**——**報告しない除外は、通った検査に見える。**
    ⚠️ **除外できるのは基盤の節だけである。** 作品が自分の禁制を除けば、
    この検査は作品の側を何も見ていない。

    ⚠️ **除外の席は1つだけである。** ⚠️ **かつて2つ目を作った**（2026-09-20——
    仕様の §16 にバッククォートで1行書き、**一枚に限り**基盤の節を外す仕組み）。
    著者の裁定「**BGM の免除：今回だけ**」のために作った。**同じ日のうちに裁定が
    撤回され**（「**1話を分割するのであれば、やっぱりBGMは禁止しよう**」）、
    **使い手が居なくなったので、機構ごと外した。**
    ⚠️ **外したのは、使い手のいない経路を文書が案内しないためである**
    （`bible.base_negatives_waived` の註と同じ規律——**読む相手のいない宣言を書かない**）。
    **床を外す席は、作品の側の1つに戻っている。**
    """
    out = []
    bible = ((getattr(project, "bible", None) or {}).get("bible") or {})
    work = bible.get("negative_base") or []
    waived = [c for c in (bible.get(specmap.WAIVED_KEY) or []) if isinstance(c, str)]
    loom = list(specmap.BASE_NEGATIVES)
    loom_stems = {_stem(c) for c in loom}
    waived_stems = {_stem(c) for c in waived}
    dropped = [c for c in loom if _stem(c) in waived_stems]
    stray = [c for c in waived if _stem(c) not in loom_stems]
    loom = [c for c in loom if _stem(c) not in waived_stems]
    extra = [c for c in work if _stem(c) not in {_stem(x) for x in specmap.BASE_NEGATIVES}]
    required = loom + extra

    paths = [(kind, _specs_of(project, kind)) for kind in ("video", "image")]
    if not any(specs for _, specs in paths):
        return out                        # 相手が無い。L18 が報告済みである。

    if not work:
        out.append(finding("L21", "",
                           "作品の禁制が宣言されていない（`bible.negative_base`）。"
                           f"**掛かるのは基盤の {len(loom)} 節だけである**——"
                           "作品が決めた禁制が1つも無ければ、この検査は"
                           "**作品の側を何も見ていない。**"))

    if dropped:
        out.append(finding("L21", "",
                           f"**祖父条項が掛かっている**（`bible.{specmap.WAIVED_KEY}`）——"
                           f"基盤の {len(dropped)} 節を要求から外した: "
                           f"{'／'.join(dropped)}。"
                           "**この作品は、その節が基盤に来る前に書かれた。**"
                           "⚠️ **除外は作品の宣言であって、基盤の判断ではない。**",
                           severity="note"))
    if stray:
        out.append(finding("L21", "",
                           f"`bible.{specmap.WAIVED_KEY}` が、基盤の禁制に無い節を名指している: "
                           f"{'／'.join(stray)}。**除外できるのは基盤の節だけである**——"
                           "作品が自分の禁制を除けば、この検査は作品の側を何も見ていない。"))

    for kind, specs in paths:
        if not specs:
            continue
        label = "動画の §18 Negative" if kind == "video" else "画像の Negative"
        caught = 0
        for s, p in specs:
            clauses, flaw = _negative_of(p, kind)
            if flaw:
                out.append(finding("L21", s, f"{label}: {flaw}"))
                continue
            got = {_stem(c) for c in clauses}
            miss = [c for c in required if _stem(c) not in got]
            if miss:
                caught += 1
                out.append(finding("L21", s,
                                   f"{label} が禁制を覆っていない——"
                                   f"{len(required)} 節のうち {len(miss)} 節が無い: "
                                   f"{'／'.join(miss)}。"
                                   "**Negative は足し算であり、書き忘れは黙って消える**"
                                   "——禁制が届かなければ、描かれてから分かる。"))
        loom_label = (f"基盤の {len(loom)} 節"
                      + (f"（祖父条項で {len(dropped)} 節を外した）" if dropped else ""))
        out.append(finding("L21", f"{len(specs)}本",
                           f"{label} を、{loom_label} ＋ 作品の {len(work)} 節"
                           f"（重複を除いて {len(required)} 節）と突き合わせた。"
                           f"覆っているのは {len(specs) - caught}/{len(specs)} 本である。",
                           severity="note"))
    return out


def check_work_language(project):
    """L27 — **作品が言語を宣言しているか。そして、その言語が §18 `Audio Prompt` に届いているか。**

    ⚠️ **なぜ要るか**（決定 2026-09-18、著者）——「**言語指定で触っているなら、
    必ずその言語を話す。**」**生成器は、言語を指定されなければ自分の既定で喋る。**
    実測——Wan 3.0 の既定は中国語であり、**発話を検出した動画に中国語の字幕が焼かれた。**
    **空欄は、モデルの母語で埋まる。**

    ⚠️ **この検査が読むのは「宣言が届いたか」までである。** 生成物が実際にその言語で
    喋ったかは**この層からは見えない**（生成はこの基盤の外で起きる）——
    **穴である。穴のまま記録する。**

    ⚠️ **`Audio Prompt` のスロットが無ければ、ここでは鳴らさない。** それは `L17` の
    欠陥である——**同じ欠陥を2つの層が別々の符号で報告しない。**
    """
    out = []
    bib = (getattr(project, "bible", None) or {}).get("bible") or {}
    lang = str(bib.get("language") or "").strip()
    if not lang:
        out.append(finding("L27", "",
                           "作品が言語を宣言していない（`bible.language`）。"
                           "**生成器は、言語を指定されなければ自分の既定で喋る**"
                           "——空欄は、モデルの母語で埋まる。"
                           "実測: 発話のある動画に**中国語の字幕が焼かれた。**"))
        return out

    specs = _specs_of(project, "video")
    checked = caught = 0
    for s, p in specs:
        body = specdoc.section(p.read_text(encoding="utf-8"), "Audio Prompt")
        if body is None:
            continue                      # L17 が「スロットが無い」と報告している
        checked += 1
        if lang.lower() not in body.lower():
            caught += 1
            out.append(finding("L27", s,
                               f"§18 `Audio Prompt` に作品の言語（`{lang}`）が無い。"
                               "**宣言は作品台帳に在るのに、生成器へ渡る文に無い**"
                               "——届かなければ、モデルは自分の既定で喋る。"))
    if not checked:
        return out                        # 相手が無い。L17 が報告済みである。

    out.append(finding("L27", f"{checked}本",
                       f"§18 `Audio Prompt` を作品の言語（`{lang}`）と突き合わせた。"
                       f"届いているのは {checked - caught}/{checked} 本である。"
                       "⚠️ **生成物が実際にその言語で喋ったかは、この層からは見えない**"
                       "——生成はこの基盤の外で起きる。",
                       severity="note"))
    return out


def _route_phrase_ok(route):
    """`MODEL_ROUTE` の1行が、**本文を走査してよい形か。** 破れていれば理由を、正しければ `""`。

    ⚠️ **空の語は、どの §18 にも当たる。** だから目録が壊れているときは
    **本文を1行も読まない**——読めば、**直した仕様の上で鳴る検査**になる
    （空の検査はOKと言う、の裏返しである）。**目録の欠陥は目録の欠陥として鳴らす。**
    """
    if not isinstance(route, (tuple, list)):
        return "行がタプルでない"
    for pair in route:
        if not isinstance(pair, (tuple, list)) or len(pair) != 2:
            return "`(語, 理由)` の対でない項目が在る"
        phrase, why = pair
        if not str(phrase).strip():
            return "空の語が在る——**空の語は、どの §18 にも当たる**"
        if not str(why).strip():
            return f"`{phrase}` に理由が無い——**理由の無い語は、次の者が消してよいと読む**"
    return ""


def check_model_route(project):
    """L28 — **§18 が、その経路のものでない語を運んでいないか。**

    ⚠️ **なぜ要るか**（決定 2026-09-20、著者）——**この会話で得た Tips を、
    生成手法を用いる際の基本的な制約へ格上げする。** そのうち**文法に属するもの**は
    検査できる: **経路が違えば、時間の文法が違う。**
    実測——`habits-ch02-seg01` の §18 が `One continuous take … never by a cut` と書き、
    **生成器は受付の机と車内を、ひと続きの部屋として走らせた。**
    **その句は `WAN 3.0` の家風であり、この経路のものではなかった。**

    ⚠️ **この層が読むのは §18 の本文だけである**（`_section_body`）。§20
    `Observed Problems` は**消した文字列を原因として引用している**ので、
    **ファイル全体を走査すれば、直した仕様の上で鳴る**——`L4` が踏んだ形である。

    ⚠️ **経路で絞るのがこの層の仕事である。** `one continuous take` は
    **`WAN 3.0` の15本すべての §18 に在り、それは正しい。**
    絞らなければ15件の偽陽性が出て、**註が読まれなくなる。**

    ⚠️ **この層は「その語が正しいか」を決めない。「どの経路の語か」を決める。**
    平板な否定（`no additional person`）が欠陥かどうかは、**§18 が置く実体との照合**で
    決まり、**実体の台帳が要る**——**この層にはできない。穴である。**
    却下した4語とその実測は `specmap.MODEL_ROUTE` の註に在る。

    ⚠️ **`MINIMAX H3` の §18 を1本も持たない作品では、この層は1文字も出さない。**
    それは「確かめて正しい」ではなく**「相手が無い」**である——
    **この沈黙がこの層の最大の穴であり、`README.md` の穴の表に書く。**

    ⚠️ **経路の名前を、この本文に書かない。** かつて違反の文面が
    `docs/h3-route.md` を直書きしていた——**3つ目の経路を登録した日に、その文面は嘘になった**
    （実測 2026-09-21）。**引く先は `specmap.MODEL_ROUTE_DOC` が経路ごとに持つ。**
    経路が増えれば表が増え、**この関数は一字も変わらない。**
    """
    # ① **目録そのものを見る。** 壊れていれば本文を読まない。
    #    ⚠️ **動画の経路についてだけ閉じる。** 画像の経路（`CHATGPT IMAGE 2.5`）は
    #    §18 を持たない——**この層が読むものが無いので、行も要らない**
    #    （`_specs_of(project, "video")` と同じ範囲である）。
    routes = {m for m, d in specmap.MODELS.items() if d.get("種別") == "video"}
    if set(specmap.MODEL_ROUTE) != routes:
        return [finding("L28", "",
                        "`MODEL_ROUTE` の鍵が、`MODELS` の**動画の経路**と一致しない。"
                        f"動画の経路: {'／'.join(sorted(routes)) or '（無し）'} ／ "
                        f"`MODEL_ROUTE`: {'／'.join(specmap.MODEL_ROUTE) or '（空）'}。"
                        "**語彙を持たない経路の行も要る**——"
                        "落とせば「禁じる語が無い」と「書き忘れた」の区別が消える。")]
    # ⚠️ **文書の表も同じ範囲へ閉じる。** 閉じなければ、経路を足した日に
    #    **その経路の違反だけが文書を引かない**——そして**それは黙って起きる。**
    if set(specmap.MODEL_ROUTE_DOC) != routes:
        return [finding("L28", "",
                        "`MODEL_ROUTE_DOC` の鍵が、`MODELS` の**動画の経路**と一致しない。"
                        f"動画の経路: {'／'.join(sorted(routes)) or '（無し）'} ／ "
                        f"`MODEL_ROUTE_DOC`: {'／'.join(specmap.MODEL_ROUTE_DOC) or '（空）'}。"
                        "**引く先を持たない経路の行も要る**（値 `None`）——"
                        "落とせば「引く文書が無い」と「書き忘れた」の区別が消える。")]
    broken = [f"`{m}`: {why}" for m, r in specmap.MODEL_ROUTE.items()
              if (why := _route_phrase_ok(r))]
    if broken:
        return [finding("L28", "",
                        "`MODEL_ROUTE` が本文を走査してよい形になっていない——"
                        + "／".join(broken)
                        + "。**空の語はどの §18 にも当たる。**"
                        "ゆえにこの層は**本文を1行も読んでいない**。")]

    out = []
    specs = _specs_of(project, "video")
    routed = {}                 # 経路 → **その経路の禁じる語と突き合わせた本数**
    for s, p in specs:
        model = _model_of(p)
        if not model:
            continue            # §18 が無い（None）／名乗らない（""）——L18 が報告している
        route = specmap.MODEL_ROUTE.get(model)
        if route is None:
            continue            # 目録に無いモデル——L18 が報告している
        if not route:
            continue            # その経路に禁じる語は無い（`WAN 3.0`・`SEEDANCE 2.5`）
        body = _section_body(p, "18.")
        if not body:
            continue            # §18 が空——L11 が報告している
        routed[model] = routed.get(model, 0) + 1
        low = body.lower()
        # ⚠️ **引く文書は経路ごとである。** 直書きすれば、経路が増えた日に嘘になる。
        doc = specmap.MODEL_ROUTE_DOC.get(model)
        tail = (f"**この経路の文法ではない**——`{doc}`。" if doc
                else "**この経路の文法ではない。**")
        for phrase, why in route:
            if phrase.lower() in low:
                out.append(finding("L28", s,
                                   f"§18（`{model}`）に `{phrase}` が在る。{why}{tail}"))
    if not routed:
        return out              # 相手が無い。**沈黙は「正しい」ではない**（穴である）

    # ⚠️ **経路ごとに分けて報告する。** 1つにまとめれば、**どの経路を突き合わせたのかが消える**
    #    ——そして経路が3つになった今、**「3本突き合わせた」は何も言っていない。**
    out.append(finding("L28", "／".join(f"{m} {n}本" for m, n in routed.items()),
                       "経路ごとに §18 を、その経路の禁じる語と突き合わせた——"
                       + "／".join(f"`{m}` の §18 を {n} 本" for m, n in routed.items())
                       + "。⚠️ **この層が見るのは「その語が別の経路のものか」だけである**——"
                       "**平板な否定が欠陥かどうかは、意味の照合と実体の台帳が要る。**"
                       "⚠️ **禁じる語を持たない経路は、ここに数えられない**"
                       "——**突き合わせていないのではない。突き合わせる語が無いのである。**",
                       severity="note"))
    return out


def _slot_body(path, slot):
    """§18 の小節 `slot` の本文。**`_prompt_slots` と同じ切り方である。**

    ⚠️ **見出しの水準を問わない**（`specdoc.sections` が畳む）——`##` でも `###` でも、
    **同じ名前で切れる。** 無ければ `""` を返す——⚠️ **「小節が無い」と「小節が空である」を
    ここでは区別しない**（区別が要るのは `L17` である。**同じ欠陥を2つの層が
    別々の符号で報告しない**）。
    """
    inside = False
    for t, body in specdoc.sections(Path(path).read_text(encoding="utf-8")):
        if TOP_SECTION.match(t):            # トップレベルの節見出し（`18. SEEDANCE 2.5 …`）
            inside = t.startswith("18.")
            continue
        if inside and t == slot:
            return body
    return ""


def check_unreceived_slots(project):
    """L30 — **§18 が、その経路が受け取れないスロットへ中身を書いていないか。**

    ⚠️ **なぜ要るか**（著者の裁定 2026-09-21）——経路は、能力が違う。
    `SEEDANCE 2.5` は**否定を専用のパラメータで受け取らない**（公式に否定として
    扱われるのは字幕と音声だけである）。**§18 に 90 節の禁制を書いても、
    その 90 節は散文として読まれる**——**床にならない。**
    ⚠️ **効かなかった否定は、渡さなかった否定と見分けがつかない。**
    ゆえに**経路が「受け取れないスロット」を宣言し、中身が在れば鳴らす。**

    ⚠️ **これは `L28` の裏返しである。** `L28` は「**その語が、その経路のものか**」を見る。
    この層は「**その欄を、その経路が持っているか**」を見る。
    **どちらも、経路の側の事実を data に持つ**（`MODEL_ROUTE` / `MODEL_UNRECEIVED_SLOTS`）。

    ⚠️ **中身が在ること自体は欠陥ではない。** 欠陥は「**届かないと知らずに書くこと**」である。
    だから**作品が引き受ける道を残す**（`specmap.ROUTE_LIMITS_KEY`）——
    **違反を、著者が名指しで引き受けた註に変える。**
    ⚠️ **報告しない除外は、通った検査に見える。**

    ⚠️ **この層は「その否定が実際に効いたか」を見ない。** 生成はこの基盤の外で起きる
    ——**見えるのは「経路が受け取らないと宣言している欄に、中身が在る」ことまでである。**
    **穴である。穴のまま記録する。**

    ⚠️ **相手が無くても黙らない。** `L28` は「その経路の §18 を1本も持たない作品では
    1文字も出さない」という穴を持つ（**沈黙は「正しい」ではない**）。
    **この層は、見た本数を必ず言う**——**0 本なら 0 本と言う。**

    ⚠️ **そして、宣言そのものも突き合わせる**（2026-09-21 に足した）。
    `bible.route_limits_accepted` は**完全一致**で照合される——綴りが違えば
    **黙って無視される。** 著者は「承知で使う」と書いたつもりで同じ違反を受け取り、
    **機構が効かないと読む。** ⚠️ **「報告しない除外は、通った検査に見える」の裏返しである**
    ——**効かない宣言は、宣言しなかったことと同じである。**
    ゆえに2方向から報告する: **どの門にも当たっていない宣言**（違反）と、
    **まだ当たっていない宣言**（註——この作品はその経路の §18 を持たない）。

    ⚠️ **綴りの揺れを吸収して通しはしない。** 吸収すれば、**本当に違う門を名指した宣言まで通る**
    （`L21` の `stray` と同じ規律——**除外できるのは基盤の節だけである**）。
    揺れは、**近い綴りを名指すことで**報せる。
    """
    # ① **目録そのものを見る。** 壊れていれば本文を読まない。
    routes = {m for m, d in specmap.MODELS.items() if d.get("種別") == "video"}
    if set(specmap.MODEL_UNRECEIVED_SLOTS) != routes:
        return [finding("L30", "",
                        "`MODEL_UNRECEIVED_SLOTS` の鍵が、`MODELS` の**動画の経路**と一致しない。"
                        f"動画の経路: {'／'.join(sorted(routes)) or '（無し）'} ／ "
                        f"`MODEL_UNRECEIVED_SLOTS`: "
                        f"{'／'.join(specmap.MODEL_UNRECEIVED_SLOTS) or '（空）'}。"
                        "**測っていない経路の行も要る**（空のタプル）——"
                        "落とせば「受け取れないスロットが無い」と「書き忘れた」の区別が消える。")]
    broken = []
    for m, decl in specmap.MODEL_UNRECEIVED_SLOTS.items():
        for pair in decl:
            if not (isinstance(pair, tuple) and len(pair) == 2):
                broken.append(f"`{m}`: 対になっていない項目 `{pair!r}`")
                continue
            slot, why = pair
            if slot not in specmap.PROMPT_SLOTS:
                broken.append(f"`{m}`: `{slot}` は `PROMPT_SLOTS` に無い"
                              "——**目録に無いスロットは、どこにも行かない**")
            elif not str(why).strip():
                broken.append(f"`{m}`: `{slot}` に理由が無い"
                              "——**理由の無い門は、次の者が開けてよいと読む**")
    if broken:
        return [finding("L30", "",
                        "`MODEL_UNRECEIVED_SLOTS` が本文を走査してよい形になっていない——"
                        + "／".join(broken)
                        + "。ゆえにこの層は**本文を1行も読んでいない。**")]

    bible = ((getattr(project, "bible", None) or {}).get("bible") or {})
    accepted = {c.strip() for c in (bible.get(specmap.ROUTE_LIMITS_KEY) or [])
                if isinstance(c, str)}

    out, notes = [], []
    examined, filled = {}, {}          # (経路, スロット) → 本数
    seen_routes = set()                # **門を持つ経路のうち、§18 を1本でも持っていたもの**
    checked = 0
    for s, p in _specs_of(project, "video"):
        model = _model_of(p)
        if not model:
            continue                   # §18 が無い／名乗らない——L18 が報告している
        decl = specmap.MODEL_UNRECEIVED_SLOTS.get(model)
        if decl is None:
            continue                   # 目録に無いモデル——L18 が報告している
        if not decl:
            continue                   # **この経路は受け取れないスロットを持たない**
        body = _section_body(p, "18.")
        if not body:
            continue                   # §18 が空——L11 が報告している
        seen_routes.add(model)
        checked += 1
        for slot, why in decl:
            key = (model, slot)
            examined[key] = examined.get(key, 0) + 1
            if not _slot_body(p, slot).strip():
                continue               # 空である——**門は守られている**
            filled[key] = filled.get(key, 0) + 1
            label = f"{model}: {slot}"
            if label in accepted:
                notes.append(finding("L30", s,
                                     f"§18 の `{slot}` に中身が在る。{why}"
                                     f"⚠️ **この作品は、それを承知で使うと宣言している**"
                                     f"（`bible.{specmap.ROUTE_LIMITS_KEY}` の `{label}`）——"
                                     "**除外は作品の宣言であって、基盤の判断ではない。**",
                                     severity="note"))
            else:
                out.append(finding("L30", s,
                                   f"§18（`{model}`）の `{slot}` に中身が在る。{why}"
                                   f"**この経路は `{slot}` を床として受け取らない。**"
                                   f"⚠️ **承知で使うなら、作品がそれを書く**——"
                                   f"`bible.{specmap.ROUTE_LIMITS_KEY}` に `{label}`。"))
    out += notes

    # ---- 宣言そのものを突き合わせる
    #
    # ⚠️ **除外は、届かなければ除外ではない。** `accepted` は完全一致で照合されるので、
    #    綴りが違えば**黙って無視される**——そして著者には、**何も書かなかったときと
    #    同じ顔の違反**が返る。**機構が壊れているように見える。**
    #
    # ⚠️ **正規化して通さない。** 畳んだ照合は、**近い綴りを名指すためにだけ**使う。
    #    通してしまえば、**本当に別の門を名指した宣言まで通る**（`L21` の `stray`——
    #    「除外できるのは基盤の節だけである」——と同じ規律である）。
    all_labels = {f"{m}: {slot}"
                  for m, d in specmap.MODEL_UNRECEIVED_SLOTS.items()
                  for slot, _ in d}
    used_labels = {f"{m}: {slot}" for m, slot in examined}

    def _fold(text):
        """照合のための畳み方。⚠️ **通すためではなく、近い綴りを名指すためである。**"""
        return " ".join(str(text).replace("：", ":").replace("　", " ").split()).casefold()

    folded = {_fold(lb): lb for lb in all_labels}
    gated = [m for m in sorted(specmap.MODEL_UNRECEIVED_SLOTS)
             if specmap.MODEL_UNRECEIVED_SLOTS[m]]
    for label in sorted(accepted):
        if label in all_labels:
            # ⚠️ **門は在るが、この作品はそこへ一度も来ていない。**
            #    **いま何もしていない**——黙って置けば、「効いている」と読まれる。
            if label not in used_labels:
                out.append(finding("L30", label,
                                   f"`bible.{specmap.ROUTE_LIMITS_KEY}` の `{label}` は、"
                                   "**この作品の §18 に一度も当たっていない。**"
                                   "⚠️ **この宣言は、いま何もしていない**——"
                                   "この作品がその経路の §18 を持てば、そのとき効く。"
                                   "**沈黙は「正しい」ではない。**",
                                   severity="note"))
            continue
        near = folded.get(_fold(label))
        if near:
            hint = f"⚠️ **`{near}` の綴り違いである可能性がある。**"
        else:
            head, _, _slot = label.partition(":")
            gates = specmap.MODEL_UNRECEIVED_SLOTS.get(head.strip())
            if gates:
                hint = (f"⚠️ **`{head.strip()}` が受け取らないのは "
                        + "／".join(f"`{g}`" for g, _ in gates) + " だけである。**")
            elif gates is not None:
                hint = f"⚠️ **`{head.strip()}` は、受け取れないスロットを1つも宣言していない。**"
            else:
                hint = ("⚠️ **門を持つ経路は "
                        + ("／".join(f"`{m}`" for m in gated) or "（無し）")
                        + " である。**")
        out.append(finding("L30", label,
                           f"`bible.{specmap.ROUTE_LIMITS_KEY}` の `{label}` が、"
                           "**どの門にも当たっていない。**"
                           "⚠️ **宣言は完全一致で照合される**——"
                           "効かなかった宣言は、**宣言しなかったことと見分けがつかない**"
                           "（`L30` はそのまま鳴りつづける）。" + hint))

    # ⚠️ **見た本数を必ず言う。** **沈黙は「正しい」ではない**——
    #    そして **0 本を 0 本と言わなければ、「確かめた」と区別がつかない。**
    gates = [m for m, d in specmap.MODEL_UNRECEIVED_SLOTS.items() if d]
    if not gates:
        return out                     # 門を持つ経路が1つも無い——言うことが無い
    if not checked:
        out.append(finding("L30", "0本",
                           "受け取れないスロットを持つ経路 "
                           + "／".join(f"`{m}`" for m in gates)
                           + " の §18 を、この作品は**1本も持たない。**"
                           "⚠️ **この層は本文を1行も読んでいない**——"
                           "**それは「確かめて正しい」ではない。**",
                           severity="note"))
        return out
    for (model, slot), n in examined.items():
        out.append(finding("L30", f"{model} {n}本",
                           f"`{model}` の §18 を {n} 本、`{slot}` の小節と突き合わせた。"
                           f"中身が在ったのは {filled.get((model, slot), 0)} 本である。"
                           "⚠️ **この層が見るのは「経路が受け取らないと宣言している欄に、"
                           "中身が在るか」だけである**——**その否定が実際に効いたかは、"
                           "この層からは見えない。**"
                           + (f"⚠️ **門を持つ経路のうち、この作品が使っているのは "
                              f"{'／'.join(sorted(seen_routes))} である。**"
                              if seen_routes else ""),
                           severity="note"))
    return out


def check_image_vars(project, repo_root=None):
    """L22 — **画像の仕様の7欄が非空か。そして、名乗ったカードがその欄を宣言しているか。**

    `L20` の画像版である。画像の仕様は**節を持たない**（`L18`）。だが
    **構造を持たないのではない**——`distill-essence-engine` の2枚のカードが
    宣言する穴を埋めることで作られる。**`L11` はここを通す**（相手は §1–20 である）。

    ⚠️ **7 は 4＋5 の和である。** エンジンは**2つの軸を別々に引く**——
    `format` カードが穴を宣言し、`style` カードも穴を宣言する。
    **片方だけでは画像プロンプトは作れない。** 実測（2026-09-13）:
    `scene-board` は5、`luminous-anime` は4、`ACTION`・`LOCATION` が重なって和は7。

    ⚠️ **この検査は、実測で見つかった欠陥から生まれた。** 画像仕様は様式カードを
    持っていたが**フォーマットカードを持っていなかった**——だから10本の `Prompt` の
    構図は**どのカードからも来ておらず**、`luminous-anime` 自身の Visual breakdown
    （「wide and sky-heavy」）と**食い違っていた**。**7欄を数えるだけの検査では
    これを捕まえられない**——4欄は最初から全部埋まっていたからである。
    だから**名乗り**（`REF_FORMAT`／`REF_STYLE`）を読み、
    **名乗ったカードが実際にその穴を宣言しているか**まで見る。

    ⚠️ **欄が在ることは、書いたことではない。** 見出しだけ置いて値を空にすれば、
    この検査が無ければ**誰も気づかない**（`L16` が `motion` に対して言うのと同じこと）。

    ⚠️ **中身が正しいかは見ない。** `SUBJECT` の値が本当に主題かは、
    **この層には読めない。** 見るのは**空でないこと**までである。

    ⚠️ **カードはこのリポジトリの外にある**（`L20` と同じ）。読めなければ
    「確かめられない」と報告する——**確かめていないことを、確かめた顔にしない。**
    """
    out = []
    kind = specmap.SPEC_KINDS.get("image") or {}
    if not kind.get("vars") or not kind.get("vars_section"):
        out.append(finding("L22", "",
                           "`SPEC_KINDS['image']` が画像の仕様の欄を宣言していない。"
                           "**何を確かめればよいかが決まっていない検査は、"
                           "何も確かめない。**"))
        return out

    specs = []
    for s in project.order():
        src = _spec_of(project.shots[s], "image")
        if not src:
            continue                      # L18 が報告している
        p = project.root / src
        if not p.is_file():
            continue                      # L18 が報告している
        specs.append((s, p))
    if not specs:
        return out                        # 相手が無い。L18 が報告済みである。

    want = tuple(kind["vars"])
    seen = 0
    for s, p in specs:
        text = p.read_text(encoding="utf-8")
        body = specdoc.section(text, kind["vars_section"])
        if body is None:
            out.append(finding("L22", s,
                               f"画像の仕様に `## {kind['vars_section']}` の節が無い。"
                               f"**{len(want)} 欄（{'／'.join(want)}）を"
                               "1つも確かめられない。**"))
            continue
        seen += 1
        got = {m.group(1).strip(): m.group(2).strip() for m in
               (re.match(r"^-\s*`([^`]+)`\s*:\s*(.*)$", ln.strip())
                for ln in body.splitlines()) if m}
        absent = [v for v in want if v not in got]
        empty = [v for v in want if got.get(v) == ""]
        if absent:
            out.append(finding("L22", s,
                               f"画像の仕様に無い欄がある: {'／'.join(absent)}。"
                               f"**`{kind['vars_section']}` は "
                               f"{len(want)} 欄で1組である**——"
                               "1つ欠ければ、その変数は空のまま生成へ渡る。"))
        if empty:
            out.append(finding("L22", s,
                               f"欄が空である: {'／'.join(empty)}。"
                               "**欄を置いたことは、書いたことではない。**"))

    # ---- 名乗りの側。⚠️ **欄が7つ在ることは、7つが正しい穴であることではない。**
    out.extend(_image_card_slots(specs, kind, repo_root))

    out.append(finding("L22", f"{seen}本",
                       f"画像の仕様の {len(want)} 欄を確かめた（{seen}/{len(specs)} 本）。"
                       "⚠️ **確かめたのは空でないことまでである**——"
                       "**引いた値が正しいかは、この層には読めない。**",
                       severity="note"))
    return out


#: 画像仕様が名乗るカードの行。`` - `REF_FORMAT`: `scene-board` `` の形を読む。
#: ⚠️ **`REF_FORMAT` は動画仕様（`# 6. REFERENCES`）にも在る。** だが画像仕様は
#: 節を持たないので、同じ名で書いても**読む側が節で絞らない**——だから衝突しない。
#: ⚠️ **行頭の空白を許す。** この行は箇条書きの入れ子にも、`## 主題` の直下にも置ける
#: ——**置き場が2つあることを、読み手が制限してはならない。**
REF_CARD = re.compile(r"^\s*-\s*`?(REF_(?:FORMAT|STYLE))`?\s*[:：]\s*(.+?)\s*$", re.M)

#: 名乗りの値から**カード名だけ**を取る。`` `scene-board` —— 5つの穴（…） `` の形を許す。
#: ⚠️ **註を書けなくしてはならない。** 名乗りは人にも読める記録である。
REF_CARD_NAME = re.compile(r"`([A-Za-z0-9._-]+)`|^([A-Za-z0-9._-]+)")


def _card_name(value):
    """名乗りの値 → カード名。読めなければ `None`。"""
    m = REF_CARD_NAME.match((value or "").strip())
    return (m.group(1) or m.group(2)) if m else None


def _image_card_slots(specs, kind, repo_root):
    """**名乗ったカードが、その欄を実際に宣言しているか。**

    ⚠️ **動画の仕様にはこれが無い。** 動画仕様の `REF_FORMAT: video-spec` は
    `# 6. REFERENCES` に**人向けに**書かれているだけで、**機械は読んでいない。**
    画像の側で初めて読む——**理由は、こちらで実際に欠陥が出たからである**
    （様式カードだけを名乗り、フォーマットカードを持っていなかった）。

    ⚠️ **名乗りが書かれていなければ、その仕様は何も名乗っていない。** これは
    **違反である**——`L19` が欄の行き先を両方向に閉じるのと同じ理屈で、
    **7つの穴がどこから来たかが書かれていなければ、その7つは検算できない。**
    """
    out = []
    ref_keys = kind.get("ref_keys") or {}
    vars_from = kind.get("vars_from") or {}
    if not ref_keys or not vars_from:
        return out                        # `SPEC_KINDS` が名乗りを持たない

    root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[2]
    cards = {}
    for layer in ref_keys:
        cards[layer] = _cards_dir(root, layer)

    # 名乗りを1本ずつ読む。⚠️ **同じ名乗りが10本に在る**ので、報告は**層ごとに1件**に畳む。
    unreadable = {}
    declared = {}
    for s, p in specs:
        found = {m.group(1): m.group(2).strip() for m in
                 REF_CARD.finditer(p.read_text(encoding="utf-8"))}
        for layer, key in ref_keys.items():
            name = found.get(key)
            if not name:
                out.append(finding("L22", s,
                                   f"画像の仕様が `{key}` を名乗っていない。"
                                   f"**{len(vars_from.get(layer, ()))} 欄が"
                                   "どのカードの穴なのか、書かれていない**——"
                                   "書かれていなければ、検算できない。"))
                continue
            name = _card_name(name)
            if not name:
                out.append(finding("L22", s,
                                   f"`{key}` の値からカード名が読めない: `{found.get(key)}`。"
                                   "**名乗りが書いてあることと、名乗りが読めることは別である。**"))
                continue
            declared.setdefault(layer, {}).setdefault(name, []).append(s)

    for layer, names in declared.items():
        d = cards.get(layer)
        if d is None:
            unreadable[layer] = True
            continue
        for name, shots in names.items():
            card = d / f"{name}.md"
            if not card.is_file():
                out.append(finding("L22", "／".join(shots[:3]) + ("…" if len(shots) > 3 else ""),
                                   f"名乗られたカード `{name}` が無い（`{card}`）。"
                                   f"**名乗りは在るが、そのカードが実在しない。**"))
                continue
            got = _card_env_vars(card)
            if got is None:
                out.append(finding("L22", name,
                                   f"カード `{name}` に `## Environment variables` が無い。"
                                   "**穴を宣言していないカードは、穴を埋められない。**"))
                continue
            wanted = set(vars_from.get(layer, ()))
            missing = sorted(wanted - got)
            extra = sorted(got - wanted)
            if missing:
                # ⚠️ **これが、実測で見つかった欠陥そのものである。**
                #    様式カードだけを名乗っていれば、`SCENE`／`CHARACTERS`／`LIGHT` が
                #    ここに並ぶ——**構図がどのカードからも来ていないことが見える。**
                out.append(finding("L22", "／".join(shots[:3]) + ("…" if len(shots) > 3 else ""),
                                   f"{layer} カード `{name}` が宣言していない欄を、"
                                   f"画像の仕様が持っている: {'／'.join(missing)}。"
                                   "**その値はどのカードの穴でもない**——"
                                   "生成へは渡るが、**カードの文法を通っていない。**"))
            if extra:
                out.append(finding("L22", "／".join(shots[:3]) + ("…" if len(shots) > 3 else ""),
                                   f"{layer} カード `{name}` が宣言しているのに、"
                                   f"画像の仕様に無い欄がある: {'／'.join(extra)}。"
                                   "**カードの穴が埋まっていない**——"
                                   "その変数は空のまま生成へ渡る。"))

    if unreadable:
        out.append(finding("L22", "",
                           f"カードが**読めない**（{'／'.join(sorted(unreadable))}）——"
                           f"`{STYLE_CARD_ENV}` を設定するか、"
                           "`distill-essence-engine` を隣に置くこと。"
                           "**このリポジトリを clone した人には無い。**"
                           "だから**名乗ったカードがその欄を宣言しているかは"
                           "確かめられない**——**確かめていないことを、"
                           "確かめた顔にしない。**",
                           severity="note"))
    elif declared:
        layers = "／".join(f"{k} {len(v)}枚" for k, v in sorted(declared.items()))
        out.append(finding("L22", "",
                           f"画像の仕様が名乗ったカード（{layers}）を読み、"
                           f"{len(kind.get('vars') or ())} 欄がその穴の和であることを"
                           "確かめた。⚠️ **カードの中身が正しいかは、この層には"
                           "読めない**——カードは `distill-essence-engine` の持ち物である。",
                           severity="note"))
    return out


#: カードの `## Environment variables` 行から、変数名を取る。
#: ⚠️ **カードによって書き方が違う**——`luminous-anime` は素の並び、`scene-board` は
#: `NAME＝説明` の形である。**だから名前だけを取る**（`＝` または `=` の手前まで）。
CARD_VAR = re.compile(r"`([A-Z][A-Z0-9_]*)`")


def _card_env_vars(card):
    """カードが宣言する穴の名前。⚠️ **読めないときは `None`**——空と読めないは違う。"""
    try:
        text = card.read_text(encoding="utf-8")
    except OSError:
        return None
    body = specdoc.section(text, "Environment variables")
    if body is None:
        return None
    return {m.group(1) for m in CARD_VAR.finditer(body)}



def check_duration(project):
    """L23 — **意図と仕様の尺が一致するか。** `shot.duration` ↔ 動画仕様 §1 `Duration:`。

    ⚠️ **値を比べてよい欄は、実測でこれだけである。** `place` や `time` を値で
    比べれば **60件の偽陽性**が出る——**渡るのは欄の値ではなく、欄が指す先**だからである
    （`FIELD_DESTINATION` が `place` を `handover:distill` へ送るのはそのためである）。
    尺は違う——**§1 の `Duration:` と `shot.duration` は同じ量を指す。**
    だからここは比べてよい。実測で **33/33 が一致**している。

    ⚠️ **「§1 が無い」と「§1 に `Duration:` が無い」は別である。** 前者は `L11` が
    鳴らす（§1–20 の目録）。後者は**誰も鳴らさない**——だからここで鳴らす。
    **突き合わせられない意図は、突き合わされていない。**

    ⚠️ **動画の仕様を持たないショットは、ここへ来ない**（`L11` が報告する）。
    """
    out = []
    pairs = []
    for s in project.order():
        shot = project.shots[s]
        src = _spec_of(shot, "video")
        if not src:
            continue                      # L11 が鳴らしている
        p = project.root / src
        if not p.is_file():
            continue                      # L11 が鳴らしている
        body = _section_body(p, "1.")
        if not body:
            continue                      # L11（節が無い）か L18（画像の仕様）が報告する
        pairs.append((s, shot.get("duration"), p, body))
    if not pairs:
        return out                        # 相手が無い。L11・L18 が報告済みである。

    agreed = 0
    for s, want, p, body in pairs:
        m = specmap.DURATION_LINE.search(body)
        if not m:
            out.append(finding("L23", s,
                               "動画の仕様の §1 に `Duration:` が無い。"
                               "**このショットの尺は、仕様の側から読めない**——"
                               "`shot.duration` と突き合わせる相手が無い。"))
            continue
        got = m.group(1).strip()
        if want is None:
            out.append(finding("L23", s,
                               f"§1 は `Duration: {got}` と言うが、"
                               "**記録に `duration` が無い。**"
                               "仕様だけが尺を持ち、意図が無い——"
                               "形の層も必須で見ている。"))
            continue
        if str(want).strip() != got:
            out.append(finding("L23", s,
                               f"尺が食い違っている——記録は `{want}`、"
                               f"§1 は `{got}` である。"
                               "**生成へ渡るのは §1 のほうである**——"
                               "記録と食い違えば、**採用の判断が別の尺の上で行われる。**"))
            continue
        agreed += 1

    out.append(finding("L23", f"{agreed}本",
                       f"尺を突き合わせた（{len(pairs)} 本の動画の仕様、"
                       f"{agreed} 本が一致）。"
                       "⚠️ **これを値で比べてよいのは、尺が"
                       "「欄の値そのものが渡る」唯一の欄だからである**"
                       "——`place`・`time` を値で比べれば偽陽性が出る。",
                       severity="note"))
    return out


def check_work_constants(project):
    """L26 — **§1 の作品定数が、家（`bible.constants.video`）と一致するか。**

    ⚠️ **この4つは、かつて3箇所に手で写されていた**——§1・§19 の `Output:` 行・
    （受け火では）`series-constants.md`。**写しは実際にずれる。** 実測: §1 の
    `1920x1080` に対し §19 の `Output:` は `1920×1080` と書き、**10/10 で綴りが違う。**
    値は同じで、綴りだけが違う——**手で写す運用は、静かに壊れる。**

    ⚠️ **`L23` の隣に在る。** あちらは「意図（`shot.duration`）↔ §1」を比べ、
    こちらは「家（`bible`）↔ §1」を比べる。**同じ §1 を読むが、相手が違う。**

    ⚠️ **`duration` をここで扱わない。** 尺は**従属変数**であり、家は `shot.duration`、
    読む者は `L23` である。**同じ欄を2つの層が読めば、同じ欠陥を別の符号で報告する**
    ——このリポジトリの規律に反する。

    ⚠️ **§19 の `Output:` 行を読まない。** あれはこの4つの**三つ目の写し**だが、
    綴りが違う（`1920×1080` / `landscape`）ので、読めば**10件の偽陽性**が出る。
    **正規化して読むか、4欄に割るかは未決定である**（穴は `engine/shot/README.md`）。

    ⚠️ **「§1 が無い」と「§1 に `Aspect` が無い」は別である**（`L23` と同じ規律）。
    前者は `L11` が報告する。後者は**誰も報告しない**——だからここで報告する。
    **突き合わせられない定数は、突き合わされていない。**

    ⚠️ **相手が空なら鳴る。** §1 が在るのに家が無いなら、それは「家が無い」である
    ——**`L21` と同じ形**（覆うべきものが無ければ、この検査は**何も見ていないのと同じである**）。

    ⚠️ **`takes/` も `media/` も開かない。** 開くのは `bible.yaml` と §1 だけである。
    """
    out = []
    home = (((project.bible or {}).get("bible") or {}).get("constants") or {})
    want = home.get("video") or {}

    pairs = []
    for s in project.order():
        shot = project.shots[s]
        src = _spec_of(shot, "video")
        if not src:
            continue                      # L11 が鳴らしている
        p = project.root / src
        if not p.is_file():
            continue                      # L11 が鳴らしている
        body = _section_body(p, "1.")
        if not body:
            continue                      # L11（節が無い）か L18（画像の仕様）が報告する
        pairs.append((s, p, body))
    if not pairs:
        return out                        # 相手が無い。L11・L18 が報告済みである。

    if not want:
        out.append(finding("L26", "",
                           "§1 の作品定数（`Aspect` / `Resolution` / `Frame Rate` / "
                           "`Orientation`）を突き合わせる相手が無い——"
                           "**家（`bible.constants.video`）が無い。**"
                           f"⚠️ **他の側は在る**（動画の仕様 {len(pairs)} 本が §1 を持つ）。"
                           "家が無ければ、この4つは**どこからも機械で読めない**——"
                           "受け火の `series-constants.md` が手で持っていたものが、"
                           "**手に戻る。**"))
        return out

    # ⚠️ **欠けた欄は、ショットごとではなく一度だけ報告する。**
    #    家の欠けは作品に1つの欠陥であって、40本の欠陥ではない。
    absent = [k for k, _, _ in specmap.VIDEO_CONSTANTS if k not in want]
    for k, _, label in specmap.VIDEO_CONSTANTS:
        if k in absent:
            out.append(finding("L26", "",
                               f"家（`bible.constants.video`）に `{k}` が無い。"
                               f"§1 の `{label}:` を突き合わせる相手が、家の側に無い——"
                               "**その欄だけが、突き合わされない。**"))

    compared = agreed = 0
    for s, p, body in pairs:
        for key, line, label in specmap.VIDEO_CONSTANTS:
            if key in absent:
                continue                  # 上の一度きりの報告で足りる
            m = line.search(body)
            if not m:
                out.append(finding("L26", s,
                                   f"動画の仕様の §1 に `{label}:` が無い。"
                                   f"**この作品定数は、仕様の側から読めない**——"
                                   f"家の `{key}` と突き合わせる相手が無い。"))
                continue
            got = m.group(1).strip()
            compared += 1
            if str(want[key]).strip() != got:
                out.append(finding("L26", s,
                                   f"作品定数が食い違っている——家は `{key}: {want[key]}`、"
                                   f"§1 は `{label}: {got}` である。"
                                   "**生成へ渡るのは §1 のほうである**——"
                                   "だから家を直しても、**古い値が仕様に残れば生成へ届く。**"
                                   "⚠️ **どちらが正しいかは、ここでは決めない。**"))
                continue
            agreed += 1

    out.append(finding("L26", f"{agreed}件",
                       f"作品定数を突き合わせた（動画の仕様 {len(pairs)} 本 × "
                       f"{len(specmap.VIDEO_CONSTANTS) - len(absent)} 欄、"
                       f"{compared} 件を比較して {agreed} 件が一致）。"
                       "⚠️ **この層は、今日のデータでは1件も鳴らない。**"
                       "**写しはずれる**という実例は既に在る（§19 の `Output:` 行が"
                       "10/10 で綴り違い）——**だから鳴らないことと、要らないことは別である。**"
                       "⚠️ **この註は「家が正しい」とは言っていない。**"
                       "家と §1 が一致した、と言っているだけである。",
                       severity="note"))
    return out


_NUM = re.compile(r"\d+(?:\.\d+)?")
_RESOLUTION = re.compile(r"(\d+)\s*[x×]\s*(\d+)")


def _num(text):
    m = _NUM.search("" if text is None else str(text))
    return float(m.group(0)) if m else None


def _resolution(text):
    m = _RESOLUTION.search("" if text is None else str(text))
    return (int(m.group(1)), int(m.group(2))) if m else None


def _spec_version(path):
    """仕様の §19 が名乗る版。⚠️ **画像の仕様は §19 を持たない**——`None` を返す。"""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    m = specmap.SPEC_VERSION_LINE.search(text)
    return m.group(1).strip() if m else None


def check_take(project):
    """L25 — **テイクが、ショットと仕様と実物と突き合っているか。**

    ⚠️ **`S1` は形を見る。ここは中身を見る。** 13本がスキーマを通ることは、
    **その13本が何かについて正しいことを、何も言わない。**

    ⚠️ **ここが「仕様 ↔ 実物」を比べる唯一の場所である。** `L23` は
    `shot.duration`（意図）と §1（仕様）を比べる——だが **§1 と、戻ってきた
    ファイルを比べる検査は、これまでどこにも無かった。** だから
    「24fps と書いたのに 30fps が返った」を**言える場所が無かった。**

    ⚠️ **`media/` は開かない。** `take.file` が名乗るファイルが在るかどうかは
    **確かめない**——`projects/hitosara/media/README.md` の宣言である。
    **これは穴である。穴のまま註で報告する。**
    """
    out = []
    docs = [(s, d.get("take") or {}) for s, v in project.takes.items() for d in v]
    if not docs:
        return out          # check.py が「テイクの記録が1本も無い」と報告する

    # ⚠️ **種別ごとに「テイクの本数」を数える。** `(shot, kind)` を数えると、
    #    **1つのショットに2本在るときに1本と数える**——この註は
    #    「テイク N 本を読んだ（内訳）」と言うのだから、
    #    **内訳の和が N にならなければ、その註は自分の本文と食い違っている。**
    kinds = {}
    seen_index = set()
    adopted = {}
    n_no_source = n_src_missing = n_unmatched = n_compared = 0
    drift = []

    for s, tk in docs:
        kind = tk.get("kind")
        idx = tk.get("index")
        where = f"{s}#{idx}"

        if s not in project.shots:
            out.append(finding("L25", where,
                               f"テイクが **存在しないショット** `{s}` を名乗っている。"
                               "記録の側に相手が無い——**このテイクは誰のものでもない。**"))
            continue

        if kind not in specmap.SPEC_KINDS:
            out.append(finding("L25", where,
                               f"`kind` が `{kind}` である。`SPEC_KINDS` の語彙は "
                               f"{sorted(specmap.SPEC_KINDS)} である——"
                               "**別の語彙を作れば、経路の検査が黙って外れる。**"))
            continue

        kinds[kind] = kinds.get(kind, 0) + 1

        if (s, kind, idx) in seen_index:
            out.append(finding("L25", where,
                               "同じ `(shot, kind, index)` のテイクが2本以上ある。"
                               "**記録から、どちらが後の生成かを読めない。**"
                               "通し番号は「上書き」と「別の生成」を区別しない。"))
        seen_index.add((s, kind, idx))

        if tk.get("adopted") is True:
            adopted.setdefault((s, kind), []).append(where)

        model = (tk.get("provider") or {}).get("model")
        if model not in specmap.MODELS:
            out.append(finding("L25", where,
                               f"`provider.model` が `{model}` である。`MODELS` に無い——"
                               "**目録に無い生成器のテイクは、目録の側から検査できない。**"))
        elif specmap.MODELS[model]["種別"] != kind:
            out.append(finding("L25", where,
                               f"`kind` は `{kind}` だが、`MODELS` は `{model}` を "
                               f"`{specmap.MODELS[model]['種別']}` と宣言している。"
                               "**経路が食い違っている。**"))

        params = tk.get("params") or {}
        src = params.get("source")
        if not src:
            n_no_source += 1
        else:
            spath = project.root / src
            if not spath.is_file():
                n_src_missing += 1
                out.append(finding("L25", where,
                                   f"`params.source` が `{src}` を指すが、**そのファイルが無い。**"
                                   "投入した文字列の正典が失われている——"
                                   "**このテイクは再生成できない。**"))
            else:
                now, was = _spec_version(spath), params.get("source_version")
                if was and now and was != now:
                    drift.append(f"{where}（投入 `{was}` → 現在 `{now}`）")

        measured = (((tk.get("verdict") or {}).get("machine") or {})
                    .get("measured") or {})
        if not measured:
            continue

        shot = project.shots[s]
        vsrc = _spec_of(shot, "video")
        if kind != "video" or not vsrc:
            n_unmatched += 1
            continue
        vpath = project.root / vsrc
        body = _section_body(vpath, "1.") if vpath.is_file() else None
        if not body:
            continue
        n_compared += 1

        line = specmap.FRAME_RATE_LINE.search(body)
        got = measured.get("frame_rate")
        if line and got is not None:
            want = _num(line.group(1))
            if want is not None and abs(want - got) > 1e-6:
                out.append(finding("L25", where,
                                   f"**フレームレートが食い違っている**——仕様の §1 は "
                                   f"`{line.group(1).strip()}`、戻ってきたファイルは `{got}` である。"
                                   "⚠️ **どちらを正とするかは決まっていない**——"
                                   "だが、**頼んだ値と来た値が別であることを、記録が黙って持てはならない。**"))

        line = specmap.RESOLUTION_LINE.search(body)
        if line and measured.get("width") and measured.get("height"):
            want = _resolution(line.group(1))
            if want and want != (measured["width"], measured["height"]):
                out.append(finding("L25", where,
                                   f"**解像度が食い違っている**——仕様の §1 は `{want[0]}x{want[1]}`、"
                                   f"戻ってきたファイルは `{measured['width']}x{measured['height']}` である。"))

        line = specmap.DURATION_LINE.search(body)
        got = measured.get("duration")
        if line and got is not None:
            want = _num(line.group(1))
            fps = measured.get("frame_rate")
            if want is not None:
                # ⚠️ **許容は1フレームである**——だから**1フレームは鳴ってはならない。**
                #    だが `6.0 + 1/24` は浮動小数ではちょうど1フレームにならない
                #    （`1.0000000000000007`）——**そのまま比べると、境界そのものが検査の誤りになる。**
                #    差を**フレーム数に直してから丸める。**
                if fps:
                    off, tol, unit = round(abs(want - got) * fps, 6), 1.0, "フレーム"
                else:
                    off, tol, unit = round(abs(want - got), 6), 0.05, "秒"
                if off > tol:
                    out.append(finding("L25", where,
                                       f"**尺が食い違っている**——仕様の §1 は `{line.group(1).strip()}`、"
                                       f"戻ってきたファイルは `{got}` である"
                                       f"（差は {off:g}{unit}、許容は1{unit}）。"))

    for (s, kind), places in adopted.items():
        if len(places) > 1:
            out.append(finding("L25", s,
                               f"`adopted: true` のテイクが `{kind}` の経路に {len(places)} 本ある"
                               f"（{', '.join(places)}）。**採用は1本である**——"
                               "採用が2本あるなら、それは**まだ選別していない**ということである。"))

    n_adopted = sum(len(v) for v in adopted.values())
    out.append(finding("L25", f"{len(docs)}本",
                       f"テイク {len(docs)} 本を読んだ（"
                       + "／".join(f"`{k}` {kinds.get(k, 0)} 本"
                                   for k in sorted(specmap.SPEC_KINDS))
                       + f"）。採用と書いてあるのは {n_adopted} 本である。"
                       f"⚠️ **採用は著者の判定である**——この層は**書いてあることを読むだけ**で、"
                       "**良し悪しを判定していない。**",
                       severity="note"))

    if n_compared:
        out.append(finding("L25", f"{n_compared}本",
                           "**仕様の §1 と、戻ってきたファイルの実測を突き合わせた**"
                           "（フレームレート・解像度・尺）。"
                           "⚠️ **これが「仕様 ↔ 実物」を比べる唯一の場所である**——"
                           "`L23` は意図と仕様を比べるが、**実物を見ない。**",
                           severity="note"))

    holes = []
    if n_unmatched:
        holes.append(f"**画像の {n_unmatched} 本には、突き合わせる相手が無い**——"
                     "画像の仕様は §1–20 を持たないから、`1920x1080` に当たる宣言がどこにも無い。"
                     "**実測値は記録してあるが、比べていない。**")
    if n_no_source:
        holes.append(f"**{n_no_source} 本が `params.source` を持たない**——"
                     "投入した文字列の正典が指されていない。")
    if drift:
        holes.append("**仕様が生成のあとに直っている**（"
                     + "／".join(drift)
                     + "）。⚠️ **これは食い違いではない**——`source_version` は"
                       "**投入した時点の版**を凍結している。"
                       "**だが、このテイクはもう一度そのままでは再生成できない。**")
    holes.append("**`take.file` が名乗るファイルの存在は、確かめていない**——"
                 "基盤は `media/` を開かない（`media/README.md` の宣言）。"
                 "**名乗りは名乗りであって、証明ではない。**")
    out.append(finding("L25", f"{len(holes)}点",
                       "この検査が確かめていないこと——" + " ／ ".join(holes),
                       severity="note"))
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


# ⚠️ **秒は小数でありうる。** 実測で `hitosara-ch01-seg09-2.5s-01` がある——
#    2.5秒のショットは実在し、**その `Instance ID` が `2.5s` と言うのは正しい。**
#    整数だけを読む綴りは、**規則（`-<秒>s-<テイク>`）を狭く実装していた**——
#    読めなかったのは ID の側ではなく、**読み手の側である。**
#    ⚠️ **広げても、数の無い接尾辞（`-Xs-01`）は鳴る。** 自己検査が両方を確かめる。
TAKE_SUFFIX = re.compile(r"-\d+(?:\.\d+)?s-\d+$")
# ⚠️ 同じ形の逸脱が `Segment ID` にもある。`\d\d-\d` は **10本目の `01-10` を読めない**
#    ——章の本数が2桁になれば、それは逸脱ではなく**同じ綴り**である。
#    註が鳴るのは `A-1` のような**別の綴り**に対してだけである。
SEGMENT_FORM = re.compile(r"\d+-\d+")


def check_identity(project):
    """L13 — **ショットの同一性が、仕様の自己名と一致するか。**

    仕様は §19 で**自分自身の名前**を書いている——`Instance ID: ukebi-v2-ch03-seg03-30s-01`。
    末尾の `-<秒>s-<テイク>` を落とした本体が、ショットIDである。

    ⚠️ **これが食い違うと、L10 は黙って別の §18 を読む。** 記録が指す `spec:` と
    記録の名前がずれれば、開示の変化点を**隣のショットの文**に対して検算することになる。
    **読み違えは、鳴らない。**

    ⚠️ **`Segment ID` は同一性の鍵ではない。** 30本を数えると `NN-N` が27本、
    **序章の3本だけ `A-N`** である——**同じレンジに2つの綴りがある。**
    §16 の終章の見出しが `開示台帳` の4文字を欠いているのと**同じ形の逸脱**であり、
    **素朴に導出すると3本を落とす。** 報告はするが、**既存の成果物は直さない**（記録だから）。
    """
    out = []
    seg_forms = {"NN-N": 0, "A-N": 0, "その他": 0}
    ok = 0
    for s in project.order():
        shot = project.shots[s]
        src = _spec_of(shot, "video")
        if not src:
            continue                      # L10・L11 が既に鳴らしている
        p = project.root / src
        if not p.is_file():
            continue
        # ⚠️ **画像の仕様は §19 を持たない。** だから「仕様が自分を名乗っていない」
        #    は**欠陥ではない**——**名乗る節が無いのである。**
        #    ⚠️ **決定（2026-09-13）の前は、この絞り方が `mode` だった。**
        #    いまは `_spec_of` が「動画の仕様」を引くので、**画像の側は最初から
        #    ここへ来ない**——`skipped` は「動画の仕様が読めなかった本数」である。
        inst = specdoc.section(p.read_text(encoding="utf-8"), "Instance")
        if inst is None:
            out.append(finding("L13", s, "§19 `Instance` の節が無い。**仕様が自分を名乗っていない。**"))
            continue
        m = re.search(r"^-\s+Instance ID:\s*`([^`]*)`", inst, re.M)
        if not m:
            out.append(finding("L13", s, "§19 に `Instance ID` が無い。**同一性の出所が無い。**"))
            continue
        iid = m.group(1)
        if not TAKE_SUFFIX.search(iid):
            out.append(finding("L13", s, f"`Instance ID: {iid}` に `-<秒>s-<テイク>` の接尾辞が無い。"
                                         "**本体を取り出せない。**"))
            continue
        body = TAKE_SUFFIX.sub("", iid)
        if body != s:
            out.append(finding("L13", s, f"ショットIDが仕様の自己名と違う——"
                                         f"`Instance ID: {iid}` の本体は `{body}` である。"
                                         "⚠️ **このままだと L10 は隣のショットの §18 を読む。**"))
        else:
            ok += 1
        sm = re.search(r"^-\s+Segment ID:\s*`([^`]*)`", inst, re.M)
        v = sm.group(1) if sm else ""
        if SEGMENT_FORM.fullmatch(v):
            seg_forms["NN-N"] += 1
        elif re.fullmatch(r"A-\d", v):
            seg_forms["A-N"] += 1
        else:
            seg_forms["その他"] += 1
    if ok:
        out.append(finding("L13", f"{ok}本", "ショットの同一性を**動画の仕様**の §19 と"
                                             "突き合わせた（`Instance ID` の本体を使う）。"
                                             "⚠️ **画像の仕様は §19 を持たない**——"
                                             "「名乗っていない」のではなく、**名乗る節が無い。**"
                                             "だからここでは検査していない。",
                           severity="note"))
    if seg_forms["A-N"] or seg_forms["その他"]:
        out.append(finding("L13", "", f"⚠️ **`Segment ID` の形が2つある**——"
                                      f"`NN-N` {seg_forms['NN-N']}本／`A-N` {seg_forms['A-N']}本"
                                      f"／その他 {seg_forms['その他']}本。"
                                      "**同一性の鍵は `Instance ID` の側である。**"
                                      "`Segment ID` から素朴に導出すると、序章の3本を落とす"
                                      "——§16 の終章の見出しが4文字を欠いているのと同じ形である。"
                                      "**既存の成果物は直さない**（記録だから）。", severity="note"))
    return out


# ---------------------------------------------------------------- 層E 宣言の到達


def _negative_series(project):
    """台帳の順序で、各ショットの §18 節集合を読む。読めない位置は理由つきで `None`。

    ⚠️ **集合にする。** `negative_prompt` はリストを返すが、**節の並び順は
    意味を持たない**（L10 も `set(a) != set(b)` で見ている）。並びで比べると、
    **同じ禁止を書き直しただけの位置が「動いた」ことになる。**
    """
    out = []
    for s in project.order():
        try:
            n = _neg(project, s)
        except _NoSpec as e:
            out.append((s, None, str(e)))
            continue
        # ⚠️ **仕様は読めたが §18 が無い、という場合がある**（画像のショット）。
        #    `_neg` はそこでも `None` を返す——**`frozenset(None)` で落ちてはならない。
        #    検査器が落ちるのは、検査が空になるのと同じくらい役に立たない。**
        if n is None:
            out.append((s, None, f"ショット {s} の仕様に §18 `Negative Prompt` の節が無い。"))
            continue
        out.append((s, frozenset(n), None))
    return out


def check_beyond_declaration(project):
    """L14 — **宣言を超えた区間。**

    ⚠️ **「§18 が動いたのに宣言が無い」で素朴に鳴らすと、30本で18件鳴る。**
    そのうち6件は**回転**である——たとえば `02-01` の節集合は `01-01` の集合と
    **frozenset として完全に同一**である（49節）。`03-01` も同じ集合へ戻る。
    **回転は明かしではない。**

    ⚠️ **§18 は単調でない。** 台帳は単調（「まだ」→「もう」。戻らない）を前提するが、
    §18 は**ショットごとに書き出された投影**なので、そのショットの必要に応じて往復する。
    **だから「動き」は明かしの証拠にならない。** L10 が「台帳の主張を falsify する」
    検査なのに対し、L14 が問うのは**台帳が届いていない区間**である。

    そこで取るのは**持続する変化**だけである——ある節が

      (a) **どの先行する集合にも無く**（＝新しく現れ）、
      (b) **以後すべての集合に在る**（＝戻らない）

    とき、その節は**回転ではない**。実測（受け火 V2 の30本）: この条件を満たす位置は
    **6箇所**——`03-03`・`06-01`・`06-03`・`08-01`・`09-02`・`09-03`。
    うち台帳が宣言しているのは2つ。**残る4つが、宣言を超えた区間である。**

    ⚠️ **削除も鳴らす。** 逆向き——**どの先行する集合にも在り、以後すべてに無い**節も
    同じく不可逆である。実測で `01-01` が加わる（`no first-person body parts`・
    `no viewer's hands` が消えて戻らない）。**対称に見ると 7 箇所。**
    **禁止が消えることは、モデルが何を描いてよいかの恒久的な拡大である**——
    増分（新たに禁じる）より危ない方向ですらある。

    ⚠️ **意味は見ない。** L10 と同じ規律である——`no girl` が消えて
    `no female figure` が以後ずっと残るなら、**集合としては戻らない増分**であり、
    この検査は鳴る。**それが同じ禁止の言い換えかどうかは、決めない。**
    決められないものを決めれば、L4 と同じ誤検出になる（片方の作品の語彙に
    合わせた検出器は、もう片方の作品で鳴る）。

    ⚠️ **戻らない増分は、非可逆である。** §18 は以後ずっとその禁止を持つ。
    台帳に足すか、**足さない理由を記録に書く**——書かなければ、
    その区間は**誰も検収していない**（L7a の前提が崩れる）。
    """
    out = []
    series = _negative_series(project)
    declared = {cp.get("shot") for cp in project.disclosure}

    unread = [s for s, n, _ in series if n is None]
    # ⚠️ **「動画の仕様が無い」と「読めない」は別である。** 記録が無ければ
    #    §18 は在りえない——読めないのではない。同じ符号で報告すると、
    #    「置き場が違う」と「記録が無い」が見分けられなくなる。
    #    ⚠️ **決定（2026-09-13）の前は、ここが「画像のショットだから」だった。**
    no_video = {s for s in unread if _spec_of(project.shots[s], "video") is None}
    broken = [s for s in unread if s not in no_video]
    if no_video:
        out.append(finding("L14", f"{len(no_video)}本",
                           "**動画の仕様（`spec:`）が無いので、§18 が在りえない**"
                           "——**この検査の相手ではない。** 相手は画像プロンプトであり、"
                           "**引き渡しの層が読む**（段2）。「読めない」のではない。",
                           severity="note"))
    if broken:
        out.append(finding("L14", f"{len(broken)}本",
                           "`spec:` が無いか読めないので、**この検査はこれらのショットを"
                           "見ていない**: " + "／".join(broken[:5])
                           + ("…" if len(broken) > 5 else ""),
                           severity="note"))

    read = [i for i, (_, n, _) in enumerate(series) if n is not None]
    if not read:
        out.append(finding("L14", "",
                           "§18 を1本も読めない。**違反0件ではなく、検査していない。**"
                           "**検査が空である。**"))
        return out

    # ⚠️ **動きの層は連続していない。** 静的なショットが間に挟まれば、§18 の列は
    #    そこで切れる。**切れ目を跨いだ変化は、跨いで比べねば見えない**
    #    ——1つ前とだけ比べると、`A → (画像) → A'` の `A → A'` が丸ごと落ちる。
    #    だから **§18 が読めた位置どうしを、隣り合うものとして扱う。**
    pairs = list(zip(read, read[1:]))

    # ① 動きと回転を数える（註）。**鳴らすためではなく、この検査の形の根拠である。**
    moves, seen, rot = [], {}, []
    for i, j in pairs:
        a, b = series[i][1], series[j][1]
        if a == b:
            continue
        moves.append(j)
        if frozenset(b) in seen:
            rot.append((series[j][0], series[seen[frozenset(b)]][0]))
        else:
            seen[frozenset(b)] = j
    if rot:
        out.append(finding("L14", f"{len(rot)}/{len(moves)}",
                           "§18 が動いた位置のうち、**先行する集合へ戻るもの**が "
                           f"{len(rot)} 箇所ある（例: {rot[0][0]} は {rot[0][1]} の集合へ戻る）。"
                           "**回転は明かしではない**——§18 は単調でなく、"
                           "**動きは開示の証拠にならない。**"
                           "だから L14 は動きではなく**持続する増分**で鳴らす。",
                           severity="note"))

    # ② 持続する変化（増分と削除の**両方**）。ここだけが鳴る。
    #
    #    ⚠️ **削除も鳴らす。** 実測（受け火 V2）: 増分だけだと 6 箇所で、
    #    `01-01` が落ちる——`no first-person body parts`・`no viewer's hands` が
    #    消えて以後ずっと戻らない。**禁止が消えることは、モデルが何を描いてよいかの
    #    恒久的な拡大である。** 増分（新たに禁じる）より危ない方向ですらある。
    #    対称に見ると 7 箇所（`01-01`・`03-03`・`06-01`・`06-03`・`08-01`・`09-02`・`09-03`）。
    beyond = []
    for i, k in pairs:
        cur, prv = series[k][1], series[i][1]
        if cur == prv:
            continue
        before = [series[j][1] for j in read if j <= i]
        after = [series[j][1] for j in read if j >= k]
        acc = [c for c in sorted(cur - prv)
               if all(c not in b for b in before) and all(c in a for a in after)]
        rem = [c for c in sorted(prv - cur)
               if all(c in b for b in before) and all(c not in a for a in after)]
        if (acc or rem) and series[k][0] not in declared:
            beyond.append((series[k][0], acc, rem))

    for shot, acc, rem in beyond:
        both = "＋" + str(len(acc)) + "／−" + str(len(rem)) if acc and rem else (
            "＋" + str(len(acc)) if acc else "−" + str(len(rem)))
        parts = []
        if acc:
            parts.append("**増えた**（" + "／".join(f"`{c}`" for c in acc[:3])
                         + ("…" if len(acc) > 3 else "") + "）")
        if rem:
            parts.append("**消えた**（" + "／".join(f"`{c}`" for c in rem[:3])
                         + ("…" if len(rem) > 3 else "") + "）")
        out.append(finding("L14", shot,
                           f"**宣言を超えた区間である。** §18 に**戻らない変化**がある（{both}）"
                           "——" + "、".join(parts) + "。以後どのショットでも戻らないのに、"
                           "台帳はこの位置に変化点を宣言していない。"
                           "⚠️ **この区間は、まだ誰も検収していない**——"
                           "明かしは不可逆なので、宣言が無ければ"
                           "**先のショットが既にその状態を持っていても鳴らない**（L7a の前提が崩れる）。"
                           "⚠️ **意味は見ていない**——同じ禁止の言い換えである可能性は残る。"
                           "⚠️ **消えた側は、増えた側より重い**——"
                           "禁止が消えれば、モデルはそれを描いてよい。"
                           "`disclosure` に行を足すか、**足さない理由を記録に書く。**"))

    if not beyond:
        out.append(finding("L14", f"{len(read)}本",
                           "§18 の持続する変化に、宣言を超えるものは無い。"
                           f"（§18 は {len(moves)} 箇所で動いた。）",
                           severity="note"))
    return out


# ---------------------------------------------------------------- 層F 目録を読む


def check_role_registered(project):
    """L15 — **種別が目録にあるか。** `rolemap.ROLES`。

    ⚠️ **登録の意味は、この検査で初めて生まれる。** 目録を書いても、
    それを読む検査が無ければ、`role` は**誰も読まない欄**のままである
    ——実測で17欄のうち7欄がそうだった（`README.md`）。

    ⚠️ **逆向きは鳴らさない。** 目録にあってデータに無い種別は、
    **作品の性質であって目録の欠陥ではない**（一場所・一反復の作品に
    情景や様式美は現れない）。**註**で報告する——U11 の材料である。

    ⚠️ **綴りを違反にしない。** 実測の `運動（停止）` は
    **主役「運動」＋運動の層のパターン「停止」**である。目録の `運動` の行は
    名前を持たないので、**データが先に名を書いた。** 綴りの違いだけで
    6本を違反にすれば、それは検出ではなく**目録の側の遅れ**である。
    だから `rolemap.resolve` がパターンを引いて確かめ、
    **限定つきの綴りを使っていること自体は註**で報告する。
    """
    out = []
    if len(rolemap.ROLES) < 12:
        out.append(finding("L15", "",
                           f"種別の目録が {len(rolemap.ROLES)} 種である。12 のはずである——"
                           "**目録が短くなれば、名のない種別を鳴らせない。**"))
    counted = collections.Counter()
    qualified = []
    unanswered = []
    for s in project.order():
        v = project.shots[s].get("role")
        if v is None or not str(v).strip():
            # 形（スキーマ）が必須で見ている。**意味の側は重ねて鳴らさない**が、
            # 黙ってもいない——註で「分類されていない」と言う。
            unanswered.append(s)
            continue
        kind, pat, why = rolemap.resolve(v)
        if kind is None:
            out.append(finding("L15", s, f"種別が目録に引けない——{why}。"
                                         "⚠️ **名のない種別に出会ったら、その場で定義して"
                                         "登録する**（`rolemap.py`）。"
                                         "登録しないまま使えば、この検査が鳴り続ける。"))
            continue
        counted[kind] += 1
        if pat:
            qualified.append(f"{s}（{kind}・{pat}）")

    if unanswered:
        out.append(finding("L15", f"{len(unanswered)}本",
                           f"種別が無い（空である）ショットが {len(unanswered)} 本ある: "
                           f"{', '.join(unanswered[:5])}{' …' if len(unanswered) > 5 else ''}。"
                           "**このショットは何で裁かれるのかが決まっていない**——"
                           "種別が無いと、**全場面が同じ基準で裁かれ、全場面が同一になる。**"
                           "（形の層も同じことを言う。**重ねて鳴らさないが、黙らない。**）",
                           severity="note"))

    if counted:
        unused = [k for k in rolemap.ROLES if k not in counted]
        out.append(finding("L15", f"{len(counted)}種",
                           f"種別の目録を確かめた（{len(rolemap.ROLES)} 種のうち "
                           f"{len(counted)} 種を使っている）。使われていない "
                           f"{len(unused)} 種: {'／'.join(unused)}。"
                           "⚠️ **これは目録の欠陥ではない**——一場所・一反復の作品には"
                           "現れない種別である。**「使われていない」と「使えない」は別である。**",
                           severity="note"))
    if qualified:
        out.append(finding("L15", f"{len(qualified)}本",
                           "⚠️ **限定つきの綴りを使っているショットがある**: "
                           + "／".join(qualified[:5])
                           + ("…" if len(qualified) > 5 else "")
                           + "。これは**主役 `運動` ＋ 運動の層のパターン**であって、"
                           "目録の `運動` の行が名前を持たないことの帰結である。"
                           "**違反ではない**——パターンは目録に在り、引けている。"
                           "⚠️ **ただし綴りが2つある状態でもある**"
                           "（素の `運動` と `運動（停止）`）。"
                           "**どちらを正典にするかは決まっていない。**",
                           severity="note"))
    return out


def check_motion_required(shot):
    """L16 — **運動の層が無い。** `motion` は**全ショットで必須である。**

    ⚠️ **旧規則（`mode: still` なら Omit も可）は死んだ。** あれは
    **「動画を回さないショット」にだけ意味があった**——静止のショットは画像で終わり、
    動画モデルへ運動を渡さないからである。**決定（2026-09-13、著者）
    「全ショット画像 → 全ショット動画」がその前提を消した。** いまは10本すべてが
    動画の経路を持つ（`L18`）——だから**どのショットでも、運動の層が無ければ
    生成へ渡る運動が無い。**

    ⚠️ **だからここは `mode` を読まない。** 読まなくなったのは規則が単純になったからで、
    欄が読まれなくなったからではない——`mode` の読み手は `L24` である。
    **同じ規則を2箇所で判定しない**（片方だけ直せば、もう片方が別の符号で同じ欠陥を唄る）。

    ⚠️ **`mode` が無いショットの分岐も消えた。** 「`mode` が無いので要否を決められない」は
    **旧規則の下でだけ意味があった**——いまは要否が `mode` によらないので、
    **決められないことは起こらない。** `mode` の不在は形の層が鳴らす。

    ⚠️ **この30件は「元が無い」ではない。** 受け火 V2 では §11 MOTION が
    **30本すべてに在り、4小節とも非空**であるのに、**移り先の欄だけが空いている**。
    L6 が「添付の記録が無い」で30件鳴っているのと同じ形＝**本物の欠落**である
    （L13 の `Segment ID` のような註ではない）。

    ⚠️ **規則をスキーマに書かない理由。** `if`/`then` で書ける（JSON Schema は
    できる）。書かないのは、**同じ欠陥を2つの層が別々の符号で報告する**からであり、
    そして**決定の理由を書く場所がスキーマには無い**からである——
    スキーマのエラーは「`'motion' is a required property`」と言うだけで、
    **なぜ必須なのか、何が欠けているのかを言えない。** `unit` の対と同じ扱いである。
    """
    sid = shot["shot"]

    if "motion" not in shot:
        return [finding("L16", sid,
                        f"**運動の層が無い**（`mode: {shot.get('mode')}`）。"
                        "**`motion` は全ショットで必須である**（決定 2026-09-13）——"
                        "**映像では運動が地であって、静止が特殊ケースである。**"
                        "⚠️ **元が無いのではない**——§11 MOTION は在り、"
                        "**移り先の欄だけが空いている。**"
                        "`subject`（何が動くか）・`quality`（どう動くか）・"
                        "`law`（どの様式の物理に従うか）を書く。"
                        "⚠️ **`mode: still` でも要る**——止まるのは**主題**であって、"
                        "画面ではない（決定 2026-09-13）。**光と粉塵は動く。**")]

    m = shot.get("motion")
    if not isinstance(m, dict):
        return []                           # 形が辞書でないことはスキーマが見る
    empty = [k for k in ("subject", "quality", "law") if not str(m.get(k) or "").strip()]
    if empty:
        return [finding("L16", sid,
                        f"運動の層はあるが、空の欄がある: {'／'.join(empty)}。"
                        "**欄を置いたことは、書いたことではない**"
                        "——空の `motion` は「運動を宣言した」ではない。"
                        "（`role` の `minLength` と同じ理由である。）")]
    return []


def _has_content(v):
    """「書いてある」の最小の判定。**空文字・空の列・空の辞書は、書いていない。**"""
    if v is None:
        return False
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, (list, tuple, dict)):
        return bool(v)
    return True


def _text_channel_kinds(shot):
    """`text_channel` が持つ行を、`kind` で数える。**読めない行は数えない。**

    ⚠️ **空の列も、`kind` の無い行も、ここでは数えない**——前者は「何も無い」、
    後者は**形の層（スキーマ）の欠陥**である。**同じ欠陥を2つの層が
    別々の符号で報告しない**（`S1` が `kind` を必須にしている）。
    """
    out = collections.Counter()
    ch = shot.get("text_channel")
    if not isinstance(ch, (list, tuple)):
        return out
    for row in ch:
        if isinstance(row, dict) and isinstance(row.get("kind"), str):
            out[row["kind"]] += 1
    return out


def check_mode_demands(project):
    """L24 — **`mode` が要求するもの。** `specmap.MODE_DEMANDS`。

    ⚠️ **ここが `mode` の読み手である。** `L16` はもう `mode` を読まない
    （運動は全モードで必須になった）。だから `mode` を読む検査がここに無ければ、
    **`mode` は17欄のうち「どの検査も読まない欄」に戻る。**

    ⚠️ **規則は「主題が動くか」から出ている。**
      `still`／`composite` → **主題が止まる**——止まる主題を書く場所が §11 MOTION である。
        空なら、**止まっているのか書き忘れたのかが分からない。**
      `composite` → **画は層の合成である**——焼く層（`timeline` の `text_events`）へ
        渡す `text_channel` が空なら、**そのショットは何も合成しない。**

    ⚠️ **確かめられないことを、確かめた顔にしない。**
    **§11 の中身が本当に主題を止めているかは、機械には読めない。**
    文が "the dough swells" と書いてあっても、この層は止まっていると読めない。
    だから註でそう報告する——**「主題は止まる」を語彙の文字列一致で見る、はしない。**
    それは**私が書いた文に合わせて私が作った検査**であり、**空の検査と同じである。**

    ⚠️ **相手が無ければ何も言わずに帰る**（`L20` と同じ形）。静止のショットが1本も無い
    作品では、この検査は何も見ていない——**その報告は註が行う**（下記）。
    """
    out = []

    # ① 目録そのものが閉じているか。**両方向に。**
    if set(specmap.MODES) != set(specmap.MODE_DEMANDS):
        only_modes = sorted(set(specmap.MODES) - set(specmap.MODE_DEMANDS))
        only_demands = sorted(set(specmap.MODE_DEMANDS) - set(specmap.MODES))
        out.append(finding("L24", "",
                           f"`MODES` と `MODE_DEMANDS` の鍵が一致しない"
                           f"（`MODES` だけ: {only_modes or 'なし'}／"
                           f"`MODE_DEMANDS` だけ: {only_demands or 'なし'}）。"
                           "**要求を書いていない `mode` は、"
                           "何も要求しない `mode` と区別がつかない**"
                           "——空の行は「要求が無い」の宣言である。"))

    seen = collections.Counter()
    for s in project.order():
        shot = project.shots[s]
        mode = shot.get("mode")
        seen[str(mode)] += 1
        for demand in specmap.MODE_DEMANDS.get(mode, ()):
            kind, _, target = demand.partition(":")
            if kind == "field":
                if not _has_content(shot.get(target)):
                    out.append(finding("L24", s,
                                       f"`mode: {mode}` は `{target}` を要求するが、"
                                       "**空である。**"
                                       "`composite` は「画は層の合成である」を意味する"
                                       "——焼くものが無ければ、"
                                       "**そのショットは何も合成しない。**"))
            elif kind == "channel":
                # ⚠️ **`text_channel` が非空であることでは足りない**（裁定 2026-09-21）。
                #    生成器が描く `lettering` は**焼かない**——だから `lettering` だけを
                #    持つ合成のショットは、**何も焼かないのに非空である。**
                kinds = _text_channel_kinds(shot)
                if not kinds.get(target):
                    out.append(finding("L24", s,
                                       f"`mode: {mode}` は `text_channel` に "
                                       f"`{target}` の行を要求するが、**1つも無い。**"
                                       + ("**欄そのものが空である。**"
                                          if not kinds else
                                          f"在るのは {'／'.join(sorted(kinds))} だけである"
                                          f"——**`{target}` は焼かない側である。**")
                                       + "`composite` は「画は層の合成である」を意味する"
                                       "——**焼くものが無ければ、"
                                       "そのショットは何も合成しない。**"))
            elif kind == "section":
                src = _spec_of(shot, "video")
                if not src:
                    continue              # L11 が鳴らしている
                p = project.root / src
                if not p.is_file():
                    continue              # L11 が鳴らしている
                if not _section_body(p, target):
                    out.append(finding("L24", s,
                                       f"`mode: {mode}` は §{target.rstrip('.')} を"
                                       "要求する（主題が止まる）が、**空である。**"
                                       "**止まっているのか、書き忘れたのかが"
                                       "分からない**——"
                                       "⚠️ **中身が本当に主題を止めているかまでは、"
                                       "この層には読めない。**"))
            else:
                out.append(finding("L24", "",
                                   f"`MODE_DEMANDS` の要求 `{demand}` の種類 `{kind}` を"
                                   "知らない。**知らない要求は、確かめられないまま通る。**"))

    if not out:
        n_still = sum(v for k, v in seen.items() if k in ("still", "composite"))
        out.append(finding("L24", f"{len(project.shots)}本",
                           f"`mode` が要求するものを確かめた（"
                           + "／".join(f"{k} {v} 本" for k, v in sorted(seen.items()))
                           + f"）。§11 を要求されるショットは {n_still} 本である。"
                           "⚠️ **確かめたのは「§11 が空でないこと」までである**"
                           "——**そこに書かれた運動が、本当に主題を止めているかは"
                           "機械には読めない。**"
                           "**この穴は、穴のまま記録する。**",
                           severity="note"))
    return out


#: §18 の小節見出しを、順序どおりに返す。**`##` の水準を問わない**——
#: `specdoc.HEADING` は水準を畳むので、`sections()` の**並び**で切り出す。
def _prompt_slots(path):
    out, inside = [], False
    for t, _ in specdoc.sections(Path(path).read_text(encoding="utf-8")):
        if TOP_SECTION.match(t):            # トップレベルの節見出し（`18. WAN 3.0 …`）
            inside = t.startswith("18.")
            continue
        if inside:
            out.append(t)
    return out


def check_prompt_slots(project):
    """L17 — **§18 のスロットが、目録のとおりであるか。** `specmap.PROMPT_SLOTS`。

    **L11 が §1–20 に対してやっていることの、§18 版である。**

    ⚠️ **これが「様式の運動の行き先を作る」の実体である。** スロットを目録に
    足すだけでは、`motion.law` と同じ穴になる——**目録は読まれて初めて在る。**

    ⚠️ **両方向を見る。** 仕様に在って目録に無い小節（`extra`）と、
    目録に在って仕様に無い小節（`miss`）の**両方**を鳴らす。片方だけなら、
    **目録から消えたスロットが黙って落ちる。**

    ⚠️ **`Style Motion` は実測 0/99 である。** 決定（2026-09-13）で足した
    **行き先**であって、**まだ誰も書いていない。** だからこの検査は
    **いま鳴る**——それが正しい。**鳴らない検査は存在しないのと同じである。**

    ⚠️ **様式カードは読まない。** `Motion character` の**中身**は
    `distill-essence-engine` にあり、**このリポジトリを clone した人には無い。**
    読めないものを検査の相手にはできない。**穴は穴のまま記録する**（下記）。
    """
    out = []
    if len(specmap.PROMPT_SLOTS) != 7:
        out.append(finding("L17", "",
                           f"§18 のスロットの目録が {len(specmap.PROMPT_SLOTS)} 個である。"
                           "7 のはずである——**目録が短くなれば、足されたスロットを"
                           "鳴らせない。**"))
    # ⚠️ 出所の無いスロットは、何も運ばない。**目録と出所を両方向に閉じる**（L12 と同じ形）。
    for slot in specmap.PROMPT_SLOTS:
        if slot not in specmap.PROMPT_SLOT_SOURCE:
            out.append(finding("L17", slot,
                               f"スロット `{slot}` の出所が宣言されていない。"
                               "**どこから来るか分からないスロットは、行き先になれない。**"))
    for slot in sorted(set(specmap.PROMPT_SLOT_SOURCE) - set(specmap.PROMPT_SLOTS)):
        out.append(finding("L17", slot,
                           f"`PROMPT_SLOT_SOURCE` が `{slot}` を指しているが、目録に無い。"))

    want = list(specmap.PROMPT_SLOTS)
    seen, with_slot = 0, 0
    for s in project.order():
        shot = project.shots[s]
        src = _spec_of(shot, "video")
        if not src:
            continue                        # L11 が鳴らしている
        p = project.root / src
        if not p.is_file():
            continue                        # L11 が鳴らしている
        # ⚠️ **画像の仕様は §18 を持たない。** 「§18 の小節が1つも無い」は
        #    **画像プロンプトでは欠陥ではない**——§18 は `video-spec` のものである。
        #    ⚠️ **決定（2026-09-13）の前は、この絞り方が `mode` だった。**
        #    いまは `_spec_of` が動画の仕様を引くので、画像の側はここへ来ない。
        # ⚠️ **絞る規則は `_spec_of` が持つ。** 各所に写せば、片方だけ直したときに
        #    もう片方が別の符号で同じ欠陥を唄る。
        got = _prompt_slots(p)
        seen += 1
        if not got:
            out.append(finding("L17", s,
                               "§18 の小節が1つも無い。**スロットを1つも確かめられない**"
                               "——節が空なのは、スロットが揃っていることではない。"))
            continue
        extra = [t for t in got if t not in want]
        miss = [t for t in want if t not in got]
        if extra:
            out.append(finding("L17", s,
                               f"目録に無いスロットがある: {'／'.join(extra)}。"
                               "**スロットが足されたなら、`specmap.PROMPT_SLOTS` と "
                               "`PROMPT_SLOT_SOURCE` にも足す**——出所の宣言が無いスロットは、"
                               "**何を運ぶのかが決まっていない。**"))
        if miss:
            out.append(finding("L17", s,
                               f"目録にあるスロットが無い: {'／'.join(miss)}。"
                               + ("⚠️ **`Style Motion` は決定（2026-09-13）で足した"
                                  "行き先である**（実測 0/99）。"
                                  "**様式カードの `Motion character` を引く欄**であり、"
                                  "これが無いあいだ、"
                                  "**55枚のうち2枚が持つ運動イディオムは"
                                  "どこからも読まれない。**"
                                  if "Style Motion" in miss else "")))
        if not miss:
            with_slot += 1

    # ⚠️ **スロットの出所は様式である。** だから `Style Motion` を持つ仕様が在るのに
    #    作品台帳が様式を宣言していなければ、**その欄は空と同じである**——
    #    何を引くのかが決まっていない。
    # ⚠️ **これが `bible.style` の読み手である。** 欄を足して読み手を足さなければ、
    #    `motion` と同じ穴になる（実測で17欄のうち7欄がそうだった）。
    style = ((getattr(project, "bible", None) or {}).get("bible") or {}).get("style")
    if with_slot and not style:
        out.append(finding("L17", "",
                           f"{with_slot} 本が `Style Motion` を持つが、"
                           "**作品台帳が様式を宣言していない**（`bible.style`）。"
                           "このスロットの出所は**様式カードの `Motion character`** であり、"
                           "**どの様式かを決めずに置いた欄は、空と同じである。**"))

    if seen:
        out.append(finding("L17", f"{seen}本",
                           f"§18 のスロットを目録と突き合わせた（{len(want)} スロット）。"
                           f"7つとも揃っているのは {with_slot}/{seen} 本である。"
                           + (f"作品の様式は `{style}` と宣言されている。"
                              if style else "⚠️ 作品の様式は宣言されていない。")
                           # ⚠️ **ここは「読んでいない」ではない。** `L20` が読む。
                           #    以前この註は「様式カードは読んでいない」と書いていた
                           #    ——**`L20` が在るのに、偽であった。**
                           + "⚠️ **様式カードは `L20` が読む**（`## Motion character` が"
                           "カードに在るかまで）。**引いた中身が正しいかは、"
                           "まだ検査されていない**——カードは "
                           "`distill-essence-engine` の持ち物である。"
                           "**この穴は、穴のまま記録する。**",
                           severity="note"))
    return out


def _dests(v):
    """行き先の値を、タプルに均す。**1つの欄が2箇所へ行くことがある**（尺）。"""
    return (v,) if isinstance(v, str) else tuple(v)


def check_field_destination(schema_dir):
    """L19 — **記録の欄すべてに、行き先が宣言されているか。** `L12` の双対である。

    ⚠️ **これが「狙いが届く」ことの機械的な形である。** `CLASS` が保証するのは
    「欄が**どこから**来たか」であって、「**どこへ**行くか」ではない。
    行き先の無い欄は、**生成へ届かない**——しかも黙って届かない。

    ⚠️ **行き先は `mode` によらない。** 決定（2026-09-13、著者）「全ショット画像 →
    全ショット動画」の下では、**どのショットも両方の経路を持つ**——だから
    「静的なショットには生成の尺が無い」は成り立たない。**同じ欄は、いつも同じ場所へ行く。**
    ⚠️ **これは単純化ではなく、規則の死である。** 以前は値が `mode` → 行き先の辞書で、
    この検査が「全モードぶん書かれているか」を見ていた——**全モードで同じ値になるなら、
    その分岐は一度も鳴らない。鳴らない分岐は、鳴ることを確かめるまで存在しないのと同じである。**

    ⚠️ **`自前` は「落ちる」ではない。** 日本語の欄は**そもそも渡らない**
    （CLAUDE.md「生成に渡す文字列を日本語にしない」）。**渡らないことと、
    渡すはずのものが届かないことは別である。** だから `自前` にも理由を書く。

    ⚠️ **両方向に閉じる。** 行き先が実在しない欄（`PROMPT_SLOTS` に無いスロットへ
    送る、`take.params` に無い鍵へ送る）も鳴らす——**送り先が無ければ、届かない。**
    そして **`SPEC_KINDS` が指す欄がスキーマに実在すること**も見る——
    **経路を足したのに欄を足していなければ、その経路はどこにも無い。**

    ⚠️ **`text_channel` は欄ごとでは閉じない**（裁定 2026-09-21）。この欄は `kind` で
    割れ、**種類ごとに行き先が違う**（`specmap.TEXT_CHANNEL_KINDS`）。
    だから**スキーマの `enum` と、その表の鍵を両方向に閉じる**——
    **片方だけ足せば、足した種類はどこにも行かないか、行き先の無い種類になる。**
    そして**表の値は、欄の行き先に含まれていなければならない**——
    **欄が宣言していない行き先へ、種類だけが行くことはできない。**
    """
    out = []
    path = Path(schema_dir) / "shot-record.schema.json"
    if not path.is_file():
        out.append(finding("L19", "", f"ショット記録のスキーマが読めない: {path}"))
        return out
    schema = json.loads(path.read_text(encoding="utf-8"))
    fields = set(schema.get("properties", {}))
    if not fields:
        out.append(finding("L19", "", "スキーマに欄が1つも無い。**空のスキーマと検査している。**"))
        return out

    # ⚠️ **`text_channel` の種類の閉包。** スキーマの `enum` と `TEXT_CHANNEL_KINDS`。
    try:
        enum = set(schema["properties"]["text_channel"]["items"]
                   ["properties"]["kind"]["enum"])
    except (KeyError, TypeError):
        enum = set()
        out.append(finding("L19", "text_channel",
                           "スキーマの `text_channel[].kind` に `enum` が無い。"
                           "**種類が自由文になれば、行き先を決められない**——"
                           "**決められない行き先は、届かない。**"))
    if enum or specmap.TEXT_CHANNEL_KINDS:
        for k in sorted(enum - set(specmap.TEXT_CHANNEL_KINDS)):
            out.append(finding("L19", "text_channel",
                               f"スキーマの `kind` に `{k}` が在るが、"
                               "`TEXT_CHANNEL_KINDS` に行き先が無い。"
                               "**行き先の無い種類は、どこにも届かない**——しかも黙って。"))
        for k in sorted(set(specmap.TEXT_CHANNEL_KINDS) - enum):
            out.append(finding("L19", "text_channel",
                               f"`TEXT_CHANNEL_KINDS` が `{k}` を指すが、"
                               "スキーマの `enum` に無い。**書けない種類に、行き先は要らない。**"))
        # ⚠️ **欄の行き先は、種類の行き先の上位集合でなければならない。**
        field_dests = set(_dests(specmap.FIELD_DESTINATION.get("text_channel")))
        for k in sorted(set(specmap.TEXT_CHANNEL_KINDS) & enum):
            d = specmap.TEXT_CHANNEL_KINDS[k]
            if d not in field_dests:
                out.append(finding("L19", "text_channel",
                                   f"種類 `{k}` の行き先 `{d}` が、欄の行き先 "
                                   f"({'／'.join(sorted(field_dests)) or '（空）'}) に無い。"
                                   "**欄が宣言していない行き先へ、種類だけが行くことはできない**"
                                   "——引き渡しの層は欄の行き先しか読まない。"))

    # ⚠️ **`SPEC_KINDS` の閉包。** 経路の欄は、記録の欄でなければならない。
    for kind, spec in sorted(specmap.SPEC_KINDS.items()):
        if spec.get("field") not in fields:
            out.append(finding("L19", str(spec.get("field")),
                               f"`SPEC_KINDS['{kind}']` が欄 `{spec.get('field')}` を指すが、"
                               "ショット記録のスキーマに無い。"
                               "**経路を宣言したのに、欄が無い**——"
                               "その経路は**どこにも存在しない。**"))

    # ⚠️ 送り先の実在を確かめるために、**本物の `take` スキーマを読む**。
    take_params = set()
    tp = Path(schema_dir) / "take.schema.json"
    if not tp.is_file():
        out.append(finding("L19", "", f"テイクのスキーマが読めない: {tp}。"
                                      "**`params` の鍵を確かめられない。**"))
    else:
        take_params = set(json.loads(tp.read_text(encoding="utf-8"))
                          ["properties"]["take"]["properties"]["params"]
                          .get("properties", {}))

    # ① 欄 → 行き先。すべての欄が行き先を宣言しているか。
    for f in sorted(fields - set(specmap.FIELD_DESTINATION)):
        out.append(finding("L19", f, f"欄 `{f}` の行き先が宣言されていない。"
                                     "**行き先の無い欄は、生成へ届かない**——"
                                     "しかも黙って届かない。"))
    for f in sorted(set(specmap.FIELD_DESTINATION) - fields):
        out.append(finding("L19", f, f"`FIELD_DESTINATION` が欄 `{f}` を指しているが、"
                                     "スキーマに無い。"))

    for f, v in sorted(specmap.FIELD_DESTINATION.items()):
        if f not in fields:
            continue
        # ⚠️ **空の行き先は、行き先が無いのと同じである。** 宣言した顔をして、
        #    1箇所へも行かない——**空の検査は OK と言う。**
        if not _dests(v):
            out.append(finding("L19", f, f"欄 `{f}` の行き先が空である。"
                                         "**宣言した顔をして、1箇所へも行かない**"
                                         "——行き先の無い欄は、黙って落ちる。"))
            continue
        # ② 行き先の種類と、送り先の実在。**送り先が無ければ、届かない。**
        for d in _dests(v):
            if d == "自前":
                continue
            kind, _, target = d.partition(":")
            if kind not in specmap.DESTINATIONS:
                out.append(finding("L19", f, f"欄 `{f}` の行き先 `{d}` の"
                                             f"種類 `{kind}` が語彙に無い。"
                                             f"語彙: {'／'.join(specmap.DESTINATIONS)}。"))
                continue
            if not target:
                out.append(finding("L19", f, f"欄 `{f}` の行き先 `{d}` に"
                                             "送り先が無い。**種類だけでは届かない。**"))
                continue
            if kind == "prompt" and target not in specmap.PROMPT_SLOTS:
                out.append(finding("L19", f, f"欄 `{f}` が §18 のスロット "
                                             f"`{target}` へ行くと宣言されているが、"
                                             "そのスロットは目録に無い。"))
            elif kind == "params" and target not in take_params:
                out.append(finding("L19", f, f"欄 `{f}` が `take.params` の "
                                             f"`{target}` へ行くと宣言されているが、"
                                             "その鍵はテイクのスキーマに無い。"))
            elif kind == "handover" and target not in specmap.HANDOVER:
                out.append(finding("L19", f, f"欄 `{f}` が基盤 `{target}` へ"
                                             "行くと宣言されているが、その基盤は"
                                             "目録に無い。"))
            elif kind == "edit" and target not in specmap.EDIT_TARGETS:
                out.append(finding("L19", f, f"欄 `{f}` が `{target}` へ"
                                             "行くと宣言されているが、その先は"
                                             "目録に無い。"))

    # ③ 理由。**渡らないこと、一部だけが渡ることは、書かねば残らない。**
    for f in sorted(fields - set(specmap.DESTINATION_WHY)):
        out.append(finding("L19", f, f"欄 `{f}` の行き先の理由が書かれていない。"
                                     "**なぜそこへ行くのか（あるいは行かないのか）が"
                                     "無ければ、行き先は後から変えられない。**"))
    for f in sorted(set(specmap.DESTINATION_WHY) - fields):
        out.append(finding("L19", f, f"`DESTINATION_WHY` が欄 `{f}` を指しているが、"
                                     "スキーマに無い。"))

    # ④ 語彙そのものが空でないか。**空の語彙は、すべてを通す。**
    for name, table in (("DESTINATIONS", specmap.DESTINATIONS),
                        ("HANDOVER", specmap.HANDOVER),
                        ("EDIT_TARGETS", specmap.EDIT_TARGETS)):
        if not table:
            out.append(finding("L19", "", f"`{name}` が空である。**空の目録は、"
                                          "何も鳴らさない。**"))

    if not out:
        n_self = sum(1 for v in specmap.FIELD_DESTINATION.values()
                     if "自前" in _dests(v))
        n_dest = sum(len(_dests(v)) for v in specmap.FIELD_DESTINATION.values())
        out.append(finding("L19", f"{len(fields)}欄",
                           f"欄の行き先は閉じている（{len(fields)} 欄 ／ "
                           f"{n_dest} の行き先、うち `自前` が {n_self}）。"
                           "**行き先の無い欄は1つも無い。**"
                           f"⚠️ **行き先は `mode` によらない**——経路が2つあるので、"
                           f"{len(specmap.SPEC_KINDS)} つの経路の欄もここで閉じている。"
                           "⚠️ **これは「届く」ことの検査であって、"
                           "「届いた」ことの検査ではない。**",
                           severity="note"))
    return out


#: カードの置き場。⚠️ **このリポジトリの外にある**（`distill-essence-engine`）。
#: だから **clone した人には無い。** 読めないときは「確かめられない」と報告する。
STYLE_CARD_ENV = "SVL_STYLES_DIR"

#: 層 → エンジンの下のフォルダ名。⚠️ **2層ある。** `L20` は様式だけを読み、
#: `L22` は両方を読む——**画像プロンプトは2つの軸の和だからである。**
CARD_DIRS = {"style": "styles", "format": "formats"}


def _cards_dir(repo_root, layer):
    """カードの置き場（層ごと）。⚠️ **指しても、そこに無ければ「読めない」。**

    指した先を確かめずに返すと、**「カードが実在しない」と「置き場が違う」が
    同じ符号で鳴る**——原因の違うものを同じ顔で報告しない。
    """
    import os
    sub = CARD_DIRS.get(layer)
    if not sub:
        return None
    env = os.environ.get(STYLE_CARD_ENV)
    if env:
        p = Path(env)
        if layer == "style":
            return p if p.is_dir() else None
        # ⚠️ **`SVL_STYLES_DIR` は様式のための環境変数である。** フォーマットの
        #    ために流用すれば、**様式を指したままフォーマットを読んだ顔をする。**
        #    だからフォーマットは、指し先が `formats` を名乗るときだけ従う。
        return p if (p.is_dir() and p.name == sub) else None
    sib = Path(repo_root).parent / "distill-essence-engine" / "references" / sub
    return sib if sib.is_dir() else None


def _styles_dir(repo_root):
    """様式カードの置き場。`L20` が使う。**中身は `_cards_dir` と同じである。**"""
    return _cards_dir(repo_root, "style")


def check_style_motion(project, repo_root=None):
    """L20 — **`Style Motion` の行き先が、空でないか。** 様式カードの `Motion character`。

    ⚠️ **`L17` はここを通す。** スロットが仕様に**在る**ことを見るだけで、
    **そのスロットが何かを運ぶか**は見ていない。`Motion character` を持たない様式を
    選べば、`Style Motion` は**在るが空である**——**空の検査は OK と言う。**

    ⚠️ **カードはこのリポジトリの外にある。** 読めなければ「確かめられない」と
    報告する——**確かめていないことを、確かめた顔にしない**（L9・L14 と同じ形）。
    """
    out = []
    style = ((getattr(project, "bible", None) or {}).get("bible") or {}).get("style")
    if not style:
        return out                       # L17 が「様式を宣言していない」と鳴らしている

    # `Style Motion` を実際に持つ仕様があるか。無ければ、この検査は何も見ていない。
    with_slot = 0
    for s in project.order():
        # ⚠️ **`_spec_of` を通す。** ここだけ `shot.get("spec")` を直に読むと、
        #    経路の決め方が2箇所に分かれる——**片方だけ直したときに、
        #    もう片方が別の符号で同じ欠陥を唄る。**
        src = _spec_of(project.shots[s], "video")
        if not src:
            continue
        p = project.root / src
        if p.is_file() and "Style Motion" in _prompt_slots(p):
            with_slot += 1
    if not with_slot:
        return out                       # L17 が「目録にあるスロットが無い」で鳴らす

    root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[2]
    d = _styles_dir(root)
    if d is None:
        out.append(finding("L20", "",
                           f"様式 `{style}` のカードが**読めない**——"
                           f"`{STYLE_CARD_ENV}` を設定するか、"
                           f"`distill-essence-engine` を隣に置くこと。"
                           "**このリポジトリを clone した人には無い。**"
                           "だから `Style Motion` が中身を運ぶかは**確かめられない**"
                           "——**確かめていないことを、確かめた顔にしない。**",
                           severity="note"))
        return out
    card = d / f"{style}.md"
    if not card.is_file():
        out.append(finding("L20", "",
                           f"様式カード `{card}` が無い。**`bible.style` が指す様式が"
                           "実在しない**——`Style Motion` は何も引けない。"))
        return out
    if "## Motion character" not in card.read_text(encoding="utf-8"):
        out.append(finding("L20", "",
                           f"様式 `{style}` のカードに `## Motion character` が無い。"
                           f"**{with_slot} 本の `Style Motion` は、在るが空である**——"
                           "`L17` はスロットが在ることで通してしまう。"
                           "**行き先を宣言したのに、運ぶものが無い。**"))
    else:
        out.append(finding("L20", "",
                           f"様式 `{style}` は `Motion character` を持つ。"
                           f"{with_slot} 本の `Style Motion` は中身を運ぶ。"
                           "⚠️ **引いた中身が正しいかは、まだ検査していない**——"
                           "カードは `distill-essence-engine` の持ち物である。",
                           severity="note"))
    return out


#: §6 `REFERENCES` が様式を名乗る行。**2つの綴りを1つの正規表現で受ける。**
#: ⚠️ **`REF_CARD` を広げない。** あちらは画像仕様の名乗りを読む（`L22`）——
#: **別の欄であり、広げれば画像の側が別のものを拾う。**
#: ⚠️ **前例は `ASPECT_LINE` である。** `Aspect Ratio:` と `Aspect:` の2綴りを
#: 1つで受けている。**同じ形の決定を、ここでもする。**
STYLE_REF_LINE = re.compile(r"^\s*-\s*`?REF_STYLE`?\s*[:：]\s*(.+?)\s*$"
                            r"|^\s*-\s*`REF_STYLE`\s*[—–-]\s*(.+?)\s*$", re.M)

#: 名乗りの値から**様式の名**を取る。⚠️ **名乗りは人にも読める記録である**——
#: 註が後ろに付いていても、値だけを取る（`REF_CARD_NAME` と同じ心持）。
STYLE_REF_BACKTICK = re.compile(r"`([^`]+)`")

#: ⚠️ **`[^A-Za-z0-9._/-]` を含む値は読まない。** 様式の名はスラグである。
_STYLE_SLUG = re.compile(r"^[A-Za-z0-9._/-]+$")


def _style_ref_name(value):
    """名乗りの値 → **様式の名**。読めなければ `None`。

    ⚠️ **語彙は2つ在る。** 実測（2026-09-21）: カード名（`luminous-anime`）が19本、
    **パス**（`references/styles/soft-cel-anime.md`）が99本である。
    ⚠️ **どちらの語彙が正かは、ここでは決めない。** 決めるのは著者である——
    ここは**両方を1つの名に畳む**だけである（末尾の要素を取り、`.md` を落とす）。
    **それで118本すべてが、実在するカードの名に着地する**（走らせて確認）。
    """
    v = (value or "").strip().strip("`").strip()
    if not v or not _STYLE_SLUG.match(v):
        return None
    v = v.rsplit("/", 1)[-1]             # ⚠️ 名乗りのパスは POSIX である（`os` を持ち込まない）
    if v.endswith(".md"):
        v = v[:-3]
    return v or None


def _style_ref_vocab(value):
    """名乗りの**語彙**。`"パス"` か `"カード名"` か。

    ⚠️ **どちらが正かは決めない。** 註が「この作品はどちらで書いているか」を
    言えるようにするためだけに数える——**作品ごとに違いうる**（実測: `hitosara` は
    カード名、`ukebi-v2` はパス）。
    """
    v = (value or "").strip().strip("`").strip()
    return "パス" if "/" in v else "カード名"


def _style_ref_of(path):
    """動画の仕様の §6 が名乗る様式。`(名, 綴り, 語彙)`。読めなければ `(None, None, None)`。

    ⚠️ **綴りは3つ在る**（実測 2026-09-21、動画の仕様118本）:

    | 綴り | 本数 | 形 |
    |---|---|---|
    | **A/B** | **49** | ``- REF_STYLE: `x` (HIGH)`` ／ ``- `REF_STYLE` — `path` · `HIGH`。`` |
    | **C** | **69** | `## REF_STYLE` の小節が `- Source: `path`` を持つ |

    ⚠️ **C は「節」である。** `_section_body` は見出しを落とすので、**C は読めない**
    ——だからここは `specdoc.sections` を直に歩き、**§6 の中の小節**を探す。
    ⚠️ **C は、いまのところ家を持たない作品にしか現れない**（`gozen-niji` 57・
    `ukebi/ukebi-video-*` 12）。**だが家が足された日に読めなくなる**——だから受ける。
    """
    try:
        text = Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None, None, None
    inside = False
    for t, body in specdoc.sections(text):
        if TOP_SECTION.match(t):
            inside = t.startswith("6.")
            if inside:
                m = STYLE_REF_LINE.search(body)          # A / B
                if m:
                    raw = next(g for g in m.groups() if g)
                    b = STYLE_REF_BACKTICK.search(raw)
                    val = b.group(1) if b else raw
                    name = _style_ref_name(val)
                    if name:
                        return name, "A/B", _style_ref_vocab(val)
            continue
        if not inside:
            continue
        if t.strip() == "REF_STYLE":                     # C
            m = specmap.STYLE_SOURCE_LINE.search(body)
            if m:
                name = _style_ref_name(m.group(1))
                if name:
                    return name, "C", _style_ref_vocab(m.group(1))
    return None, None, None


def check_style_reference(project):
    """L31 — **家（`bible.style`）と、仕様の §6 が名乗る様式が、同じか。**

    ⚠️ **`L20` の隣に在る。** あちらは「**カードが `Motion character` を持つか**」を
    訊く。こちらは「**家と仕様が、同じ名を指しているか**」を訊く。
    **同じ `bible.style` を読むが、相手が違う**（`L23` と `L26` の関係と同じである）。

    ⚠️ **この検査にカードは1枚も要らない。** 家と §6 だけで書ける——
    **両方ともこのリポジトリの中に在る。** カードを要するのは `L20` と `L22` である。
    ⚠️ **ゆえに `L20` と違い、clone した人の手元でも鳴る。**

    ⚠️ **実測（2026-09-21、動画の仕様118本）。** **49本が `REF_STYLE` の行で名乗り、
    69本が §6 の小節で名乗る。語彙はカード名19本・パス99本に割れている。**
    そして——**リポジトリの4作品を突き合わせて、この層は1件も鳴らなかった。**

    ⚠️ **そして、この2つは一度も突き合わされていなかった。** `L20` が訊くのは
    「カードに節が在るか」だけであり、**仕様が名乗った名と家の名が同じかは、
    誰も訊いていなかった。** `SPEC_KINDS["video"]` は `ref_keys` を持たず、
    名乗りを読む `_image_card_slots` は、その1行目で降りる——
    **動画の §6 は、人向けに書かれているだけで、機械は読んでいない。**

    ⚠️ **語彙は2つ、綴りは3つである**（`_style_ref_of` の表を見よ）。
    ここは**両方を1つの名に畳んでから**比べる。**どちらの語彙が正しいかは決めない**
    ——`L26` が「正規化して読むか、4欄に割るかは未決定である」と書いたのと同じ形の
    未決定が、2箇所目に来ている。**この検査は、その決定を待たずに書ける。**

    ⚠️ **食い違ったとき、どちらが正しいかは決めない。** 家が古いのか、仕様が古いのかは、
    **ここでは分からない**——`L26` と同じである。
    ⚠️ **生成へ渡るのは §6 のほうである**（`L22` が名乗りを読み、`L20` がその名で
    カードを引く）。**だが家を直しても、古い名が仕様に残れば生成へ届く。**

    ⚠️ **読まないもの。**
    - **§6 の他のキー**（`REF_CHARACTER` / `REF_FORMAT` / `REF_SOURCE` / `REF_BIBLE`）。
      **この検査は `REF_STYLE` 1つだけを読む。**
    - **画像の仕様。** あちらは節を持たない（`L18`）——**§6 が無いので、相手にならない。**
    - **`takes/` も `media/` も開かない。** 開くのは `bible.yaml` と §6 だけである。
    - ⚠️ **家を持たない作品の §6**（実測 69本）。**突き合わせる相手が無い**——
      `L17` が「様式を宣言していない」で鳴らす。**同じ欠陥を2つの層が別々の符号で
      報告しない**（`L26` が `duration` を読まないのと同じ規律）。

    ⚠️ **相手が無ければ鳴らさない。** 動画の仕様が1本も無ければ、この層は
    **何も見ていない**——`L11`・`L18` が報告する。
    """
    out = []
    style = ((getattr(project, "bible", None) or {}).get("bible") or {}).get("style")
    if not style:
        return out                       # L17 が「様式を宣言していない」と鳴らしている

    pairs = []
    for s in project.order():
        # ⚠️ **`_spec_of` を通す。** ここだけ `shot.get("spec")` を直に読むと、
        #    経路の決め方が2箇所に分かれる（`L20` と同じ理由）。
        src = _spec_of(project.shots[s], "video")
        if not src:
            continue                      # L11・L18 が鳴らしている
        p = project.root / src
        if not p.is_file():
            continue
        pairs.append((s, p))
    if not pairs:
        return out                        # 相手が無い。L11・L18 が報告済みである。

    compared = agreed = 0
    spellings, vocabularies = {}, {}
    for s, p in pairs:
        got, how, vocab = _style_ref_of(p)
        if got is None:
            out.append(finding("L31", s,
                               "動画の仕様の §6 が、様式を名乗っていない——"
                               f"**`REF_STYLE` が読めない。**"
                               f"家は `style: {style}` を宣言しているのに、"
                               "**この仕様の側からは、どの様式を引くのかが読めない。**"
                               "⚠️ **綴りは3つ在る**（`- REF_STYLE: `x`` ／ "
                               "`- `REF_STYLE` — `x`` ／ `## REF_STYLE` の `- Source:`）。"))
            continue
        compared += 1
        spellings[how] = spellings.get(how, 0) + 1
        vocabularies[vocab] = vocabularies.get(vocab, 0) + 1
        if got != style:
            out.append(finding("L31", s,
                               f"様式が食い違っている——家は `style: {style}`、"
                               f"§6 は `{got}` を名乗る。"
                               "**生成へ渡るのは §6 のほうである**——"
                               "だから家を直しても、**古い名が仕様に残れば生成へ届く。**"
                               "⚠️ **どちらが正しいかは、ここでは決めない。**"))
            continue
        agreed += 1

    # ⚠️ **名乗りが0本なら、内訳を並べない。** 空の内訳は「綴り: 。」になる
    #    ——**註は、読める形でだけ書く。**
    if compared:
        told = "・".join(f"{k} が {v}本" for k, v in sorted(spellings.items()))
        vocab = "・".join(f"{k} が {v}本" for k, v in sorted(vocabularies.items()))
        head = (f"家と §6 の様式を突き合わせた（動画の仕様 {len(pairs)} 本、"
                f"{compared} 本が名乗り、{agreed} 本が一致）。"
                f"⚠️ **この作品の綴り**: {told}。"
                f"⚠️ **この作品の語彙**: {vocab}。")
    else:
        head = (f"家と §6 の様式を突き合わせた（動画の仕様 {len(pairs)} 本、"
                f"**だが1本も名乗っていない**）。"
                "⚠️ **この作品には、突き合わせる相手が無い。**")
    out.append(finding("L31", f"{agreed}件", head +
                       # ⚠️ **「今日は0件」は、測った範囲つきで書く。**
                       #    「この層は鳴らない」とだけ書けば、**鳴る作品が現れた回に
                       #    嘘になる**——だから作品ではなく**実測**を名乗る。
                       "⚠️ **実測したリポジトリの4作品を突き合わせた限り、"
                       "この層は1件も鳴らなかった**（2026-09-21）。"
                       "**綴りは3つ、語彙は2つ**——リポジトリ全体ではそうである"
                       "（同じ家 `luminous-anime` を、ある作品はカード名で、"
                       "ある作品は `references/styles/…md` と書く）。"
                       "**だから鳴らないことと、要らないことは別である。**"
                       "⚠️ **この註は「家が正しい」とは言っていない。**"
                       "家と §6 が同じ名に畳まれた、と言っているだけである。",
                       severity="note"))
    return out


# ---------------------------------------------------------------- まとめ

CHECKS_SHOT = (check_unit, check_one_place, check_one_time, check_move,
               check_reference_forbidden, check_attached, check_motion_required)


def run(project, schema_dir=None, repo_root=None):
    out = list(check_not_empty(project))
    # ⚠️ **層C の隣に置く。** 同じ仕事である——**この走りが見ていないものを言う。**
    out += check_nested_works(project)
    for s in project.order():
        shot = project.shots[s]
        for fn in CHECKS_SHOT:
            out += fn(shot)
        out += check_keys_known(project, shot)
    out += check_disclosure(project)
    out += check_circular(project)
    out += check_negative_response(project)
    out += check_spec_sections(project)
    out += check_spec_kind(project)
    out += check_negative_coverage(project)
    out += check_work_language(project)
    out += check_model_route(project)
    out += check_unreceived_slots(project)
    out += check_image_vars(project, repo_root=repo_root)
    out += check_duration(project)
    out += check_work_constants(project)
    out += check_take(project)
    out += check_identity(project)
    out += check_beyond_declaration(project)
    out += check_role_registered(project)
    out += check_prompt_slots(project)
    out += check_style_motion(project, repo_root=repo_root)
    # ⚠️ **`L20` の直後に置く。** 同じ `bible.style` を読み、相手だけが違う
    #    ——あちらはカード、こちらは仕様の §6。**離すと、片方だけが直される。**
    out += check_style_reference(project)
    out += check_mode_demands(project)
    if schema_dir:
        out += check_field_source(schema_dir)
        out += check_field_destination(schema_dir)
    return out
