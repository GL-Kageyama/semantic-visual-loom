"""`video-spec` §1–20 とショット記録の欄との対応。**宣言であり、検査される。**

⚠️ **散文で置くと腐る。** だからここは目録であって、`check.py` が
**両方向に閉じているか**を確かめる（L11・L12）——**節が欄を名指し、欄が節を名指し、
どちらにも漏れが無いこと。** 新しい節が仕様に足されれば、L11 が鳴る。

⚠️ **「落ちる」は「失われる」ではない。** ショット記録の欄にならない節も、
仕様（`spec:` が指す先）にはそのまま在る。**落ちるのは記録からであって、作品からではない。**
"""

import re

# ---------------------------------------------------------------- 仕様の節

#: §1–20。**順序も含めて目録である。**
SPEC_SECTIONS = (
    "1. VIDEO",
    "2. WORLD",
    "3. SUBJECTS",
    "4. ENVIRONMENT",
    "5. OBJECTS",
    "6. REFERENCES",
    "7. NARRATIVE",
    "8. TEMPORAL STRUCTURE",
    "9. ACTION",
    "10. CAMERA",
    "11. MOTION",
    "12. EMOTION",
    "13. LIGHTING",
    "14. AUDIO",
    "15. CONTINUITY",
    "16. CONSTRAINTS",
    "17. GENERATION PRIORITIES",
    # ⚠️ **モデル名を目録に書かない。** §18 は**モデル固有の投影**であって、
    #    作品の節ではない——`video-spec` の雛形も `18 PROMPT MAPPING` と書く。
    #    実物は `18. WAN 3.0 PROMPT MAPPING` のように**モデル名を名乗る**が、
    #    その名前は**インスタンスの束縛**であり、節の同一性ではない。
    #    だからここは**族の代表**であり、突き合わせは `SECTION_FAMILIES` が行う。
    #    ⚠️ **1つの作品が複数のモデルを使えるようにするためである**（決定 2026-09-13）。
    "18. PROMPT MAPPING",
    "19. GENERATION INSTANCE",
    "20. ITERATION",
)

#: 節見出しの**族**。目録の綴り（鍵）→ 実際の見出しに当てる正規表現。
#:
#: ⚠️ **§18 だけが族である。** 他の19節は綴りが固定で、揺れていない
#:    （実測: 99本すべてが同一の見出し）。**揺れていないものに族を許すと、
#:    検査が緩む。** 族にするのは、**実際に可変であるものだけ**である。
#:
#: ⚠️ **モデル名は §18 の見出しにしか現れない。** だからここが、ある仕様が
#:    **どのモデルへ束ねられたか**を機械が読める唯一の場所である（`L18`）。
SECTION_FAMILIES = {
    "18. PROMPT MAPPING": re.compile(r"^18\.(?: .+)? PROMPT MAPPING$"),
}

#: §18 の見出しから**モデル名**を取り出す。名乗りは `MODELS` の鍵である。
MODEL_OF_SECTION = re.compile(r"^18\. (.+) PROMPT MAPPING$")


def canonical(title):
    """実際の節見出しを、**目録の綴りに均す**。族でなければそのまま返す。

    ⚠️ **均すのは突き合わせのためであって、報告のためではない。** 鳴らすときは
    実際の見出しを出す——**「目録と違う」と言いながら目録の綴りを見せたら、
    どこが違うのか分からない。**
    """
    for want, pat in SECTION_FAMILIES.items():
        if pat.match(title):
            return want
    return title


def named_model(title):
    """§18 の見出しが名乗るモデル。名乗っていなければ `None`。"""
    m = MODEL_OF_SECTION.match(title or "")
    return m.group(1) if m else None

# ---------------------------------------------------------------- 行き先の種別

#: 節の残り（`to` に入らなかった部分）がどこへ行くか。
REST = {
    "series": "作品定数——bible か台帳へ。プロジェクトに一つ",
    "spec": "仕様に残る——§18 がモデルへ渡す文そのもの、またはその材料",
    "take": "生成の記録——テイクへ（1生成に1枚）",
    "seam": "別基盤へ——Semantic Audio Loom が消費する（契約は M6）",
}

# ---------------------------------------------------------------- 節 → 行き先

# `to`      … ショット記録の欄。無ければ ()
# `rest`    … `to` に入らなかった部分の行き先（`REST` の鍵）
# `evidence`… 実測。30本を数えた値
SPEC_MAP = {
    "1. VIDEO": {
        "to": ("duration",),
        "rest": "series",
        "evidence": "Basic は30本で1種——Duration `30s`・Aspect `16:9`・Resolution `1920x1080`・"
                    "Frame Rate `24fps`・Orientation `Landscape`。**5つのうち4つは作品定数。**"
                    "Generation Intent は30本で30種——散文による要約であり、§7 Core Event と §2 の言い換え。",
    },
    "2. WORLD": {
        "to": ("time",),
        "rest": "series",
        "evidence": "World Concept 9種・World Rules 7種・Visual Language 12種。"
                    "**不変ではない**——各本が1〜2文だけ書き換える（`in this clip the soul-fire is gone` の類）。"
                    "その差分は §18 Visual Prompt に既に現れている。`Time` の1行だけが `time` へ移る。",
    },
    "3. SUBJECTS": {
        "to": (),
        "rest": "series",
        "evidence": "各実体の `Reference:` が台帳の `characters.<名>.identity` になる。"
                    "Appearance 70節で33種・Behavior 55節で43種・Continuity Requirements 55節で7種——"
                    "**前半2つは各本が書き分け、3つ目はほぼ定型である。**"
                    "書き分けの中身（`no mark on his forehead (the seal appears only from S08)`）は**開示**であり、"
                    "ショット側では `disclosure_state` が持つ——**§3 からではなく §16 から読む**（下記）。",
    },
    "4. ENVIRONMENT": {
        "to": ("place",),
        "rest": "series",
        "evidence": "Location は3種（`CROSSING` が大半）。`ID:` の1行だけが `place` へ移る。"
                    "Environment Elements 22種・Environmental Behavior 16種は台帳へ。",
    },
    "5. OBJECTS": {
        "to": (),
        "rest": "series",
        "evidence": "30本で29種。ただし差は1行——`台帳` がほぼ常に在り、頁の状態が変わるだけ。台帳の `props` へ。",
    },
    "6. REFERENCES": {
        "to": ("reference_set",),
        "rest": "spec",
        "evidence": "30本で12種。`REF_CHARACTER` / `REF_HANA` の**有無**が開示で変わる（花は 03-3 以降）。"
                    "`REF_STYLE` / `REF_FORMAT` / `REF_SOURCE` / `REF_BIBLE` は30本すべてに在る。",
    },
    "7. NARRATIVE": {
        "to": ("unit",),
        "rest": "spec",
        "evidence": "Core Event 30種・Beginning 30種・Turn 30種・Peak 30種・Pull 29種。"
                    "**小節は4つ（Beginning/Turn/Peak/Pull）で、§8 の BEAT は3つ**（29本。1本だけ4つ）"
                    "——**1対1ではない。** Pull は「切れ目」であって時間ではない。"
                    "Beginning/Turn/Peak は §8 の BEAT 行と同じ3分割の散文版であり、**要約である。**",
    },
    "8. TEMPORAL STRUCTURE": {
        "to": ("beats",),
        "rest": "series",
        "evidence": "Temporal Sequence が BEAT 行を持ち、`range` / `density` / `what` がそのまま欄になる。"
                    "⚠️ **Timing Policy は30本すべて `STRUCTURED` / `NON_UNIFORM`** ——定数である。"
                    "Temporal Units も2種しかない。Temporal Density は §8 の散文による言い換え。",
    },
    "9. ACTION": {
        "to": (),
        "rest": "spec",
        "evidence": "`ACT_*` は30本で86個・73種。1本に2〜4個、`Before` / `After` で鎖になる。"
                    "**これは仕様の中の器官の並びであって、台帳は読まない。**"
                    "八器官＝八動詞は §2 World Rules の側にあり、そちらが台帳へ行く。",
    },
    "10. CAMERA": {
        "to": (),
        "rest": "spec",
        "evidence": "Camera Language 30種・Camera Events 30種。Camera Behavior は2種"
                    "——**`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`**"
                    "がほぼ定型である。**「1本の連続テイク」を名指す唯一の節であるが、落ちない**"
                    "——落ちる理由は「連続テイクだから」ではない（`README.md`）。",
    },
    "11. MOTION": {
        "to": ("motion",),
        "rest": "spec",
        "evidence": "⚠️ **小節は4つ（Subject / Object / Environmental Motion ＋ Physical Characteristics）で、欄は3つ**"
                    "（`subject` / `quality` / `law`）——**1対1ではない。**"
                    "Physical Characteristics の5項目（Weight / Inertia / Acceleration / Fluidity / Impact）のうち"
                    "欄に対応するのは Fluidity だけ（`law` の限定作画）。**残り4項目は落ちる。**",
    },
    "12. EMOTION": {
        "to": (),
        "rest": "spec",
        "evidence": "Emotional Arc 29種・Emotional Events 30種。**ランクは読まない。**",
    },
    "13. LIGHTING": {
        "to": (),
        "rest": "spec",
        "evidence": "Base Lighting 26種・Lighting Events 30種。色温度と光源の法は §2 Visual Language と §15 にも書かれ、"
                    "**三重に書かれている。**",
    },
    "14. AUDIO": {
        "to": ("text_channel", "sound"),
        "rest": "seam",
        "evidence": "Dialogue 30種。**声の行は `text_channel` の `kind: voice` になる**——"
                    "画像生成器に描かせないためである。Sound Effects 23種・Music 25種・Environment 6種は"
                    "Semantic Audio Loom が消費する（`sound.scene_ref`）。**契約は M6。**",
    },
    "15. CONTINUITY": {
        "to": (),
        "rest": "series",
        "evidence": "Identity 13種・Visual 11種・Motion 25種・Sound 22種。"
                    "⚠️ **Identity は仕様自身が「§18 プロンプトへ毎回まるごと書き込まれる」と書いている**"
                    "——§15 は §18 の材料である。Visual/Motion/Sound Continuity は"
                    "**様式の運動イディオムの規則**であり、その移動先は未決定（U08）。",
    },
    "16. CONSTRAINTS": {
        "to": ("forbidden_set", "disclosure_state"),
        "rest": "spec",
        "evidence": "⚠️ **`MUST NOT` の見出しはレンジ名を持つ**"
                    "（`## MUST NOT（この1本の禁止・開示台帳 03 レンジより）`、10レンジ×3本＝30）。"
                    "**台帳はここを読む**——`forbidden_set` と `disclosure_state` はどちらもこの節から出る。"
                    "MUST 30種・PREFER 27種・ALLOW 22種は**人が読む注記**であり、落ちる。",
    },
    "17. GENERATION PRIORITIES": {
        "to": (),
        "rest": "spec",
        "evidence": "30本で30種。**§15・§16 の並べ直しである**——"
                    "1〜5番目は §16 MUST NOT と §15 から、6番目は §8 から、7番目は §16 PREFER から取られている。"
                    "**優先順そのものは新しい情報である**（何を先に犠牲にするか）。だから仕様に残す。",
    },
    "18. PROMPT MAPPING": {
        "to": (),
        "rest": "spec",
        "evidence": "⚠️ **スロットは7つである**（Master / Visual / Motion / Camera / Audio / "
                    "Negative ＋ **Style Motion**）——`PROMPT_SLOTS` を見よ。"
                    "実測の6つは**仕様に在るもの**で、`Style Motion` は**決定（2026-09-13）で"
                    "足した行き先**である（実測 0/99）。"
                    "**§6 が「the six §18 slots」と書き、§6 の `REF_FORMAT` がそれを定義する**"
                    "——§18 の形は**様式カード（`references/formats/video-spec.md`）の持ち物**である。"
                    "⚠️ **実物の見出しはモデル名を名乗る**（実測: 99/99 が `18. WAN 3.0 PROMPT MAPPING`）"
                    "＝ここは**モデル固有の投影**であって、記録ではない。"
                    "**だから `spec:` はここを指す**——モデルが変われば §18 だけが差し替わり、欄は残る。"
                    "⚠️ **雛形は `18 PROMPT MAPPING` と書き、モデル名を持たない**——"
                    "**名前はインスタンスの束縛である。** だから目録も名を持たず、"
                    "突き合わせは `SECTION_FAMILIES` が行う。"
                    "Negative Prompt は30本で18種（開示の変化点で動く）。",
    },
    "19. GENERATION INSTANCE": {
        "to": (),
        "rest": "take",
        "evidence": "Instance 30種・Resolved Values 30種。**7つの鍵が30本すべてに揃っている**"
                    "（Duration / References / Temporal Structure / Camera Events / Action Events / Audio Events / Output）"
                    "——**仕様自身が持つ §1–18 への索引である。**"
                    "`Instance ID` が `ukebi-v2-ch03-seg03-30s-01` の形をとる＝テイクの名前である。",
    },
    "20. ITERATION": {
        "to": (),
        "rest": "take",
        "evidence": "Version 2種（すべて `2.0.0`）・Anticipated risks 30種・Next Generation 30種。"
                    "⚠️ **Observed Problems と Changes は30本すべて `_(none yet)_` で、内容が無い**"
                    "——**「空ファイルは内容でない」と同じ形である。**"
                    "まだ生成していないのだから空なのは正しいが、**空を「問題なし」と読んではならない。**",
    },
}

# ---------------------------------------------------------------- §18 のスロット

#: §18 が持つスロット。**順序も含めて目録である。** L17 が仕様と突き合わせる。
#:
#: ⚠️ **出所は `video-spec`（`distill-essence-engine`）の §18 が明記している。**
#: ここに写すのは**このリポジトリが検査するため**である——clone した人に
#: `video-spec` は無く、**読めないものを検査の相手にはできない。**
#:
#: ⚠️ **7つ目 `Style Motion` は決定（2026-09-13、著者）で足された。**
#: 実測が要求した——55枚の様式カードのうち **2枚だけが `Motion character` を持つ**のに、
#: その2枚の寄与先が**§18 のどこにも無かった**（様式カードが寄与できる2つのうち
#: Visual Prompt は運動の語を明示的に禁じており、運動を受け取る Motion Prompt の
#: 出所は §9＋§11 だけである）。**読まれない節は、書かれた分だけ嘘になる。**
#:
#: ⚠️ **7つとも `##` の小節である。** 実測（2026-09-13）——既存の99本はすべて**6小節**で、
#:    `Style Motion` は **0/99** である。**カードの側も6つと書いていた**ので、
#:    決定（2026-09-13）で **`references/video-spec.md` を7つに直した**
#:    （あのカードは `distill-essence-engine` からこのリポジトリへ移管されている）。
#:    **だから `Style Motion` を持つ仕様は、いま新しく書かれるものだけである。**
PROMPT_SLOTS = (
    "Master Prompt",
    "Visual Prompt",
    "Motion Prompt",
    "Camera Prompt",
    "Audio Prompt",
    "Negative Prompt",
    "Style Motion",
)

#: 各スロットの出所。**目録と対で置く。** 出所の無いスロットは、何も運ばない。
#: L17 は**両方向**を見る（スロットに出す所が無い／出所がスロットを指す）。
PROMPT_SLOT_SOURCE = {
    "Master Prompt": "§1 ＋ §7 ＋ §8",
    "Visual Prompt": "§2 Visual Language ＋ §3 ＋ §4 ＋ §5 ＋ §13（**運動の語は禁じられている**）",
    "Motion Prompt": "§9 ＋ §11",
    "Camera Prompt": "§10",
    "Audio Prompt": "§14",
    "Negative Prompt": "§16 ＋ カードの Negative ＋ 様式カードの Negative",
    "Style Motion": "**様式カードの `Motion character`**",
}

# ---------------------------------------------------------------- 欄 → 出所

#: ショット記録の欄が、どこから来たか。
#:   `("spec",   節)` … 節からそのまま移る
#:   `("struct", 節)` … 節の散文を構造化した**追加欄**（節に欄としては無い）
#:   `("added",  None)` … §1–20 に無い欄
FIELD_SOURCE = {
    "shot": ("added", None),
    "unit": ("struct", "7. NARRATIVE"),
    "role": ("added", None),
    "effect": ("added", None),
    "place": ("spec", "4. ENVIRONMENT"),
    "time": ("spec", "2. WORLD"),
    "mode": ("added", None),
    "duration": ("spec", "1. VIDEO"),
    "spec": ("added", None),
    "key_image": ("added", None),
    "motion": ("struct", "11. MOTION"),
    "beats": ("struct", "8. TEMPORAL STRUCTURE"),
    "reference_set": ("struct", "6. REFERENCES"),
    "forbidden_set": ("struct", "16. CONSTRAINTS"),
    "attached": ("added", None),
    "disclosure_state": ("struct", "16. CONSTRAINTS"),
    "text_channel": ("struct", "14. AUDIO"),
    "sound": ("struct", "14. AUDIO"),
}

#: `("added", None)` の欄の理由。**§1–20 に無いことを、無いまま書いておく。**
ADDED_WHY = {
    "shot": "ショットの同一性。ディレクトリ名から来る——仕様は自分の名前を持たない",
    "role": "種別（主役）。**§1–20 に欄が無い**——だから `検証/種別の分類.md` の実測から人が当てた（U32）",
    "effect": "種別（効果）。同上",
    "mode": "制作モード。**§1 に Mode 欄は無い**——30本すべて `motion` という実測が値である",
    "spec": "**動画の** §1–20 を指す。**仕様は自分自身を指す欄を持たない**",
    "key_image": "**画像の**仕様を指す。⚠️ **このショットの見せ場の1枚である**——"
                   "決定（2026-09-13、著者）「全ショット画像 → 全ショット動画」、"
                   "および同日の決定「**見せ場の1枚**」・「動画へは**添付（参照画像）として**渡す」。"
                   "⚠️ **`first_frame` から改名した。** 前の名は"
                   "「動画の最初のコマ」を意味していたが、**著者が逆を選んだ**——"
                   "最初のコマにすると、そのショットの変化（割る・盛り付ける）が"
                   "**画面上で起きなくなる**（`mode` と `unit` が偽になる）。"
                   "§1–20 に欄が無い（画像プロンプトは節を持たない）",
    "attached": "**実際に何を添付したか。§1–20 に欄が無い**——"
                "受け火 V1 はここが無いまま生成され、花のシートが無いクリップが2本出た",
}

# ---------------------------------------------------------------- モデル

#: 生成モデル。**名前は §18 の見出しに現れるそのままの綴りである。**
#:
#: ⚠️ **料金を書かない。** 値は動き、**実測の日付が無い数は腐る**
#:    （`README.md`「数を書くときは水準を書く」）。単価が要るなら、
#:    測った日と出所を添えて `HISTORY.md` に置く。
#:
#: ⚠️ **この目録は「どのモデルが在るか」ではない。「どのモデルへ束ねたか」である。**
#:    作品は複数のモデルを使える（決定 2026-09-13、U02）——**仕様の種類が違えば
#:    生成の仕組みそのものが違う**。だから仕様が名乗り、`L18` が読む。
#:
#: ⚠️ **担うのは「ショットの種類」ではなく「経路」である。**
#:    決定（2026-09-13、著者）「全ショット画像 → 全ショット動画」の下では、
#:    **どのショットも両方のモデルを通る。** 動きのあるショットだけが Wan、ではない。
MODELS = {
    "WAN 3.0": {
        "slug": "wan-3.0",
        "種別": "video",
        "出所": "著者の決定（2026-09-13）——受け火と同じ",
        "注": "**動画の経路を担う。全ショットが通る。**"
              "⚠️ **入力は「最初のコマ」ではない。** 著者の決定（2026-09-13）で、"
              "`key_image` の画像は**添付（参照画像）として**渡る——"
              "文から生成し、**その見た目へ寄せる**。実測がその効き目を言っている:"
              "「**添付画像の服がテキスト指定に勝つ**」（受け火、制服が勝った）。"
              "だから**最初のコマにすると失われる変化**（割る・盛り付ける）が、"
              "この渡し方なら**画面上で起きる**。"
              "⚠️ `references/video-spec.md` は「Wan 3.0 は1生成＝30秒」と書いていたが、"
              "著者は**一秒ごとに指定できる**と言う。**このリポジトリのカードなので直した**"
              "（決定 2026-09-13）——設計は**尺を可変として組む**（`take.params.duration`）。",
    },
    "CHATGPT IMAGE 2.5": {
        "slug": "chatgpt-image-2.5",
        "種別": "image",
        "出所": "著者の決定（2026-09-13）",
        "注": "**画像の経路を担う。全ショットが通る。**"
              "⚠️ **このリポジトリはこれを回さない**——**著者が手で投入する。**"
              "だから基盤の仕事は「回すこと」ではなく「**渡すものを検査すること**」である。"
              "⚠️ **投入するのは画像仕様の `Prompt` である**（決定B 2026-09-13、著者）——"
              "**それが正典である。**"
              "⚠️ **その `Prompt` は `distill-essence-engine` が作る**（決定C 2026-09-13、著者）——"
              "**回される工程である。** エンジンは Skill であってプログラムではないから、"
              "**回すのは著者ではなく Claude のセッションであり、成果物は仕様ファイルに書かれる。**"
              "だから `handover` の層は**依然として「運ぶ」であって「組む」ではない**——"
              "エンジンは実行時依存ではない。"
              "⚠️ **エンジンの2軸は独立である**（決定D 2026-09-13、著者）——"
              "`format`: `scene-board`（**何を見せるか＝構成の文法**）／"
              "`style`: `luminous-anime`（**誰の声か＝語彙**）。"
              "⚠️ **両軸が別々に穴を宣言する。** `scene-board` は"
              "`SCENE`/`CHARACTERS`/`ACTION`/`LOCATION`/`LIGHT` を、`luminous-anime` は"
              "`SUBJECT`/`ACTION`/`LOCATION`/`ACCENT` を要求する。**和は7欄**——"
              "`ACTION` と `LOCATION` は**両層に同名で在り、同じ値が両方の穴に入る**"
              "（実測: 著者の実例 `gozen-niji-scene-board` が `scene-board` ＋ `soft-cel-anime` で"
              "同じ重なりを踏んでいる）。"
              "⚠️ **⑦Negative の出力は `Prompt` へ溶かさない。** エンジンの合成プロンプトは"
              "Negative を最後の一文に溶かす（実例で実測）が、**この記録は2段落として別々に保つ**——"
              "`L21` と開示系列が**段落の集合**として読むからである。"
              "⚠️ **これはエンジンの文書化された出力形からの逸脱である**——黙ってやらず `HISTORY.md` に書く。"
              "⚠️ **このモデルは Negative を別欄で受けない**（著者の決定 2026-09-13）——"
              "**`Prompt` の本文の末尾に空行を1つ置いて `Negative` を繋ぎ、1本の文字列として投入する。**"
              "⚠️ **その空行は、記録の中にそのまま在る**——**1つの節の2つの段落である。**"
              "だから**繋がった文字列を別に書き写してはならない**（写しは食い違う）。"
              "⚠️ **2段落を1つの節に入れてあるのは、著者が1回で選べるようにするためである**——"
              "**見出しが本文の間にあると、選択はそれを巻き込む**（`SPEC_KINDS` の註を見よ）。"
              "⚠️ **順序が意味を持つ**——画像10枚を全部見てから動画を回す（決定 2026-09-13）。"
              "最初のコマが狙いと違えば、その上に積む動画は10倍の無駄になる。",
    },
}

# ---------------------------------------------------------------- 仕様の種類

#: ショットが持つ**2つの経路**。**経路は `mode` ではなく欄が決める。**
#:
#: ⚠️ **決定（2026-09-13、著者）——全ショット画像 → 全ショット動画。**
#:    だから **`mode` は仕様の種類を決めない。** 決めるのは**欄**である:
#:    `spec` が動画の仕様を指し、`key_image` が画像の仕様を指す。
#:    ⚠️ **画像は「最初のコマ」ではない。** それはこの決定の後で著者が選び直した
#:    （同日、「見せ場の1枚」＋「添付として渡す」）——`key_image` の註を見よ。
#:    **10本すべてが両方を持つ。**
#:
#: ⚠️ **この決定より前は `SPEC_KIND` があり、`mode` → `image`/`video` を引いていた。**
#:    それは「静止のショットは画像で終わる」を前提にしていた——**その前提が消えた。**
#:    いま `mode` が決めるのは**主題が動くかどうか**だけである（`L16`・`L24` が読む）。
#:
#: ⚠️ **`mode` の3値は残る**（スキーマの `enum` である）。意味は変わる:
#:      `still`     … 主題が止まる。動くのは**光と粉塵だけ**
#:      `composite` … 主題が止まり、**画は層の合成である**（文字の焼き込み）
#:      `motion`    … 主題が動く
#:
#: ⚠️ **`sections` が種類ごとに違うのが要点である。** §1–20 は**動画の仕様**のものであり、
#:    画像プロンプトは節を持たない——1枚の文だからである（`video-spec` 自身が
#:    「他のカードはすべて穴埋めの一文で終わる」と書く）。**混ぜれば `L11` が誤って鳴る。**
#:
#: ⚠️ **`negative` の指すものが、2つの種類で違う。**
#:    動画では**節の見出し**である（`## Negative Prompt`）。
#:    画像では**段落の名前**である——画像の仕様は節を持たない（`sections: False`）。
#:    ⚠️ **指しているものは同じで、指し方が違う。** だから種類ごとに
#:    `body_section`・`body_paragraphs` が「どこを探すか」を言う。
#:    ⚠️ `specdoc.negative_prompt()` は動画の見出しを硬く持つので、
#:    **画像仕様では `None` を返す**（実測 7/7）——**動画の側の道具である。**
SPEC_KINDS = {
    "video": {"field": "spec", "sections": True, "negative": "Negative Prompt"},
    "image": {"field": "key_image", "sections": False, "negative": "Negative",
              # ⚠️ **画像の正典は「1つの節の中の、名前を持った段落の列」である。**
              #    実測（2026-09-13）: 仕様の `## 投入する1本の文字列` の節が
              #    **2段落**を持ち、**1段落目が `Prompt`、2段落目が `Negative`** である。
              #
              # ⚠️ **なぜ節ではなく段落なのか。** **著者が1回で選ぶためである**
              #    （著者の指示 2026-09-13「一回で拾いたい」）。
              #    見出しは**どの水準でも節を切る**（`specdoc.HEADING`）——だから
              #    `## Prompt` と `## Negative` の2節に分ければ**本文の間に見出しが入り**、
              #    著者が `Prompt` の行から `Negative` の行まで選ぶと
              #    **その見出しを巻き込む**（`Prompt` の本文と `Negative` の本文が
              #    連続するなら、**2つは同じ節にしか入れられない**）。
              #    ⚠️ **失うのは見出しのラベルだけである。** 段落の名前はここに在る。
              #
              # ⚠️ **空行1つが、決定A の「空行を1つ置いて繋ぐ」そのものである。**
              #    2段落のまま保つことは、**繋いだ1本を記録の中に置くこと**でもある。
              #    ⚠️ **繋がった文字列を別に書き写してはならない**——写しは食い違う。
              "body_section": "投入する1本の文字列",
              "body_paragraphs": ("Prompt", "Negative"),
              # ⚠️ **画像の仕様が持つ7欄。** 節の見出しは `## 主題（英語・…）` である
              #    （接頭辞で読む）。**画像プロンプトは、この7つを埋めることで作られる。**
              #
              # ⚠️ **7は4＋5の和であって、どちらのカードも7を宣言していない。**
              #    `distill-essence-engine` は**2つの軸を別々に引く**:
              #      `format` カードが穴を宣言し、`style` カードが穴を宣言する。
              #    **片方だけでは画像プロンプトは作れない。** 実測（2026-09-13）:
              #      `scene-board`     … SCENE／CHARACTERS／ACTION／LOCATION／LIGHT
              #      `luminous-anime`  … SUBJECT／ACTION／LOCATION／ACCENT
              #    `ACTION` と `LOCATION` は両層に同名で在り、**同じ値が両方の穴に入る。**
              #    → 和は7。⚠️ **著者自身の `gozen-niji-scene-board` が
              #    この重なりを既に踏んでいる**（`scene-board` ＋ `soft-cel-anime`）。
              #
              # ⚠️ **この発見は欠陥から出た。** 画像仕様は様式カードを持っていたが
              #    **フォーマットカードを持っていなかった**——だから実測で44枚の
              #    フォーマットカードのうち4欄すべてを宣言するものは**0枚**であり、
              #    10本の `Prompt` の構図（「Low and close composition」）は
              #    **どのカードからも来ていなかった**（`luminous-anime` 自身の
              #    Visual breakdown は「wide and sky-heavy」と言う——**食い違っていた**）。
              "vars_section": "主題",
              "vars": ("SCENE", "CHARACTERS", "SUBJECT", "ACTION", "LOCATION",
                       "LIGHT", "ACCENT"),
              #: **その7欄が、どのカードの穴なのか。** `L22` がカードと突き合わせる。
              #: ⚠️ **層を分けて保つのは、片方だけが欠けたときにどちらが欠けたかを
              #:    言えるようにするためである。** 7欄を平らに持てば、
              #:    「`SCENE` が無い」とは言えても「フォーマットカードが無い」とは言えない。
              "vars_from": {"format": ("SCENE", "CHARACTERS", "ACTION", "LOCATION", "LIGHT"),
                            "style": ("SUBJECT", "ACTION", "LOCATION", "ACCENT")},
              #: **画像仕様が名乗るカード。** 動画仕様の `REF_FORMAT:` の画像版である。
              #: ⚠️ **`L22` が「名乗ったカードが、その欄を実際に宣言しているか」を見る。**
              #:    名乗りを書くだけでは**宣言であって、一致ではない。**
              "ref_keys": {"format": "REF_FORMAT", "style": "REF_STYLE"}},
}

#: 仕様の §1 が持つ尺の行。**`L23` が `shot.duration` と突き合わせる。**
#: ⚠️ **値を突き合わせてよい欄は、実測でこれだけである。** `place`・`time` を値で
#:    比べると、実測で**60件の偽陽性**が出た（欄の値が渡るのではなく、欄が指す先が渡る）。
DURATION_LINE = re.compile(r"^-\s*Duration:\s*`?([^`\n]+?)`?\s*$", re.M)

#: §1 の残り2行。**`L25` が、戻ってきたファイルの実測と突き合わせる。**
#: ⚠️ **`L23` は「意図 ↔ 仕様」を比べる。ここは「仕様 ↔ 実物」を比べる。**
#:    実物が手に入るまで、この2つ目の突き合わせは**どこにも無かった。**
RESOLUTION_LINE = re.compile(r"^-\s*Resolution:\s*`?([^`\n]+?)`?\s*$", re.M)
FRAME_RATE_LINE = re.compile(r"^-\s*Frame Rate:\s*`?([^`\n]+?)`?\s*$", re.M)

#: §19 が名乗る仕様の版。**`L25` が、投入した版と現在の版を比べる。**
#: ⚠️ **画像の仕様は §19 を持たない**——だから画像のテイクには、この照合の相手が無い。
SPEC_VERSION_LINE = re.compile(r"^-\s*Specification Version:\s*`?([^`\n]+?)`?\s*$", re.M)

#: 否定詞。**語幹を取るために落とす。**
#:
#: ⚠️ **禁止の語を文字列で比べてはならない。** 実測——受け火 V2 の台帳は
#:    `no photorealistic` と書き、§18 は `not photorealistic` と書く。
#:    文字列一致で比べれば **30/30 が偽陽性**になる（L4 と同じ形の誤りである）。
NEGATOR = re.compile(r"^(?:no|not|never|without)\s+", re.I)

#: `mode` の値。**スキーマの enum と同じものでなければならない。**
MODES = ("still", "composite", "motion")

#: **`mode` が要求するもの。** `L24` が読む。
#:
#: ⚠️ **静止が特殊ケースである**（固定方針「映像では運動が地であって、静止が特殊ケースである」）。
#:    だから要求を持つのは `still` と `composite` だけであり、**`motion` の行は空である。**
#:    ⚠️ **この空の行を落としてはいけない。** 落とせば「`motion` には要求が無い」と
#:    「`motion` を書き忘れた」の区別が消える——**空と、無いことは違う。**
#:    `L24` が両方向に閉じる（`MODES` と `MODE_DEMANDS` の鍵が一致すること）。
#:
#: 要求の書き方（`L24` がこの接頭辞で分岐する）:
#:   `section:<見出しの接頭辞>` … 動画の仕様の、そのトップレベル節が非空であること
#:   `field:<欄の名前>`         … ショット記録の、その欄が非空であること
#:
#: ⚠️ **`composite` ⇒ `text_channel` 非空は、意味から出る規則である。**
#:    `composite` は「画は層の合成である」を意味し、**文字を焼くのは `timeline` である**
#:    （生成器は文字を描かない）。だから合成のショットに文字が無ければ、
#:    **そのショットは何も合成しない。**
#: ⚠️ **逆向きは成り立たない**——`motion` のショットも `text_channel` を持てる。
#:    **片方向だけである。**
MODE_DEMANDS = {
    "still": ("section:11.",),
    "composite": ("section:11.", "field:text_channel"),
    "motion": (),
}

# ---------------------------------------------------------------- 欄 → 行き先

#: 行き先の語彙。⚠️ **5つしかない。** これを増やすときは、
#: **その行き先を読む側が実在するか**を先に確かめる——`L19` が両方向を見る。
DESTINATIONS = {
    "自前": "**生成へ渡らない。** 作者の装置である——"
            "日本語で書かれ、§1–20 に欄が無く、モデルに渡る文の中に一度も現れない",
    "prompt": "§18 のスロット（`specmap.PROMPT_SLOTS`）。**7つしかない**",
    "params": "`take.params` の鍵（`take.schema.json`）。**プロンプトではなくAPIの引数**",
    "handover": "**別基盤へ渡す。** このリポジトリは回さない——"
                "`distill`（画像プロンプト）／`loom`（Semantic Audio Loom・契約は M6）",
    "edit": "**生成ではなく編集で決まる**（`timeline`）。"
            "「映像は生成されない。編集される。」の実装である",
}

#: `handover` の行き先になれる基盤。
HANDOVER = {
    "distill": "`distill-essence-engine`。画像プロンプトを作る——**読むだけ。書き換えない**",
    "loom": "Semantic Audio Loom。音を消費する——**契約は M6・未定**",
}

#: `edit` の行き先になれる先。
EDIT_TARGETS = {
    "timeline": "`timeline.schema.json`。採用テイクの列・カット点・文字イベント",
}

#: **記録の欄が、どこへ行くか。** ⚠️ **これが「狙いが届く」ことの宣言である。**
#:
#: 形は `FIELD_SOURCE` の双対である——あちらは「欄が**どこから**来たか」、
#: こちらは「欄が**どこへ**行くか」。**出所と行き先の両方が宣言されて初めて、
#: 「落ちない」と言える。**  `L19` が両方向に閉じているかを見る。
#:
#: ⚠️ **値は `mode` によらない。** 決定（2026-09-13、著者）「全ショット画像 →
#:    全ショット動画」の下では、**どのショットも両方の経路を持つ**——だから
#:    「静的なショットには尺が無い」は成り立たない。**同じ欄が、いつも同じ場所へ行く。**
#:
#: ⚠️ **これは単純化ではなく、規則の死である。** 以前は値が `mode` → 行き先の
#:    辞書であり、`L19` が「全モードぶん書かれているか」を見ていた。**いま全モードで
#:    同じ値になるので、その分岐は一度も鳴らない**——リポジトリの規律では
#:    **鳴らない分岐は、鳴ることを確かめるまで存在しないのと同じである。** だから次元ごと落とした。
#:
#: ⚠️ **値は文字列か、文字列の組である。** 経路が2つあるので、**2つへ行く欄がある**——
#:    画像の側（`handover:distill`）と、動画の側（`prompt:`）の両方である。
#:    `_dests()` が組をそのまま読む。
#:
#: ⚠️ **`自前` は「落ちる」ではない。** 日本語の欄は**そもそも渡らない**——
#:    CLAUDE.md「生成に渡す文字列を日本語にしない」。**渡らないことと、
#:    渡すはずのものが届かないことは別である。** この2つを同じ顔にしない。
FIELD_DESTINATION = {
    "shot":  "自前",
    "unit":  "自前",
    "role":  "自前",
    "effect": "自前",
    "spec":  "自前",
    "mode":  "自前",
    "time":  "自前",

    # ⚠️ **画像の側にも渡る。** 場所は画像プロンプトにも要る——最初のコマが
    #    どこであるかを知らない生成器は、動画の出発点を描けない。
    "place": ("prompt:Visual Prompt", "handover:distill"),

    # ⚠️ **尺は3つある。** 記録の `duration` は**意図**、`take.params.duration` は
    #    **生成**、`timeline.clips[].in`/`out` は**採用**である。
    #    決定（2026-09-13）「適切な秒数を、ショットサンプルごとにみい出す」——
    #    **だから意図は、採用を縛らない。**（`L23` が意図と仕様 §1 を突き合わせる。）
    "duration": ("params:duration", "edit:timeline"),

    # ⚠️ **静止のショットでも、運動は生成へ渡る。** 決定（2026-09-13）——
    #    「主題は止まり、光と粉塵だけが動く」。**それは運動であり、動画の仕様に要る。**
    #    寄り・送り（カメラ）は別の欄（§10）である。
    "motion": ("prompt:Motion Prompt", "edit:timeline"),

    # ⚠️ **ビート表のうち、生成へ渡るのは英語の部分だけである。**
    #    `range`（`0-6s`）と `density`（`sparse`）は Master Prompt の `{BEATS}` に入る。
    #    **`what` は日本語であり、渡らない**——だから `自前` ではなく `prompt` と書き、
    #    その一部であることを `DESTINATION_WHY` が述べる。
    "beats": ("prompt:Master Prompt", "edit:timeline"),

    "reference_set": ("params:references", "handover:distill"),
    "attached": ("params:references", "handover:distill"),
    "forbidden_set": ("prompt:Negative Prompt", "handover:distill"),
    "disclosure_state": ("prompt:Negative Prompt", "handover:distill"),

    # ⚠️ **この欄は `kind` で2つに割れる**（`overlay` と `voice`）。
    #    `overlay`——**画面に焼く文字。生成器には描かせない。** だから `edit:timeline` が
    #    焼く（`timeline.schema.json`「自前レンダを持つ理由は文字合成で、これは基盤がやる」）。
    #    `voice`——**声の行であり、§14 の内容である。** だから `prompt:Audio Prompt` へ行く。
    #    **行き先が2つ在るのは、欄が2種類を束ねているからである。**
    #    ⚠️ **この割り方は `L19` ではなく引き渡しの層が行う**（段2）——`L19` が見るのは
    #    「その行き先が語彙に在り、送り先が実在するか」だけである。
    "text_channel": ("edit:timeline", "prompt:Audio Prompt"),

    # ⚠️ **モードによらない。** 音はどのショットにも在り、行き先は一つである。
    "sound": "handover:loom",

    # ⚠️ **画像の経路そのもの。** 行き先は**2つある**——
    #    ① `distill`（その1枚を作る基盤・画像プロンプトを出す）
    #    ② `params:references`（**作られた1枚が、動画へ添付される**）
    #    ⚠️ **②が落ちれば、画像は作られて誰にも渡らない。**
    #    決定（2026-09-13、著者）「動画へは**添付（参照画像）として**渡す」がこれである。
    "key_image": ("handover:distill", "params:references"),
}

#: 行き先の理由。**`自前` と、一部だけが渡る欄には、必ず書く。**
#: `ADDED_WHY` と同じ作法である——**渡らないことを、渡らないまま記録する。**
DESTINATION_WHY = {
    "shot": "ショットの同一性。**ディレクトリ名とファイル名から来る**——"
            "生成器は「何番目のショットか」を知らない。**知る必要も無い。**",
    "unit": "変化の対。**日本語であり、生成へ渡る文には現れない**——"
            "§1–20 に欄が無い（`FIELD_SOURCE`: `struct` §7）。"
            "**これは作者が「このショットは1つの変化である」と確かめるための装置である。**",
    "role": "種別（主役）。`rolemap.py` が目録であり、**L15 が読む**。"
            "生成へは渡らない——**種別は検収基準を選ぶものであって、プロンプトの語ではない。**",
    "effect": "種別（効果）。同上。**受け火 V2 では 9/30 しか書かれていない。**",
    "spec": "**動画の**仕様を指す。**仕様は自分自身を指す欄を持たない。**",
    "key_image": "**画像の**仕様を指す。**行き先が2つあるのは、この欄だけである**——"
                   "① `distill` … 画像プロンプトを作る基盤であり、"
                   "**このリポジトリはそれを回さない**（著者が手で投入する）。"
                   "② `params:references` … **作られた1枚が、そのショットの動画へ添付される。**"
                   "⚠️ **`attached` と同じ行き先である。** どちらも「生成器に添える画像」だからで、"
                   "違うのは**出所**だけである（`attached` は台帳の参照集合、"
                   "`key_image` は**このショットのために作る1枚**）。"
                   "⚠️ **これは絵コンテではない。** 見せ場の1枚だから、"
                   "**狙いと違えば、その上に積む動画は10倍の無駄になる**"
                   "（決定 2026-09-13「画像10枚 → 全部見る → 動画10本」）。",
    "mode": "制作モード。**主題が動くかどうかだけを持つ**——"
            "`L16`（`motion` の必須）と `L24`（`mode` が要求するもの）が読む。"
            "⚠️ **仕様の種類は決めない。** 経路は欄が決める（`SPEC_KINDS`）——"
            "決定（2026-09-13）が `SPEC_KIND` を死なせた。",
    "time": "時刻。**日本語である**（実測: 受け火 V2 の30本すべてが "
            "`境（時刻が流れない）`）。**だから生成へ渡る文には現れない**——"
            "§2 WORLD の `Time` は §18 Visual Prompt に英語で書き直される。"
            "**欄の値が渡るのではなく、欄が指す先が渡る。**",
    "place": "場所。**英語である**（実測: `CROSSING`）。"
             "だから §18 の本文にそのまま現れる（実測 30/30）。"
             "⚠️ **`CROSSING.base` ではなく `CROSSING` が現れる**——"
             "**参照の鍵は §18 に現れない。現れるのは場所の名前である。**"
             "⚠️ **画像の側にも渡る。** 決定（2026-09-13）で全ショットが画像から始まる——"
             "**最初のコマがどこかを知らない生成器は、出発点を描けない。**",
    "duration": "⚠️ **尺は3つある。** 記録の `duration` は**意図**、"
                "`take.params.duration` は**生成**、`timeline.clips[].in`/`out` は**採用**である。"
                "決定（2026-09-13）——「適切な秒数を、ショットサンプルごとにみい出す。"
                "長ければいいというものでもない」。"
                "**だから意図は、採用を縛らない。**"
                "⚠️ **意図は仕様 §1 の `Duration:` と一致する**（`L23` が見る）——"
                "**採用を縛らないことと、仕様と食い違ってよいことは別である。**",
    "motion": "運動の層。**全ショットに通底する**（CLAUDE.md）。"
              "⚠️ **静止のショットでも生成へ渡る**——決定（2026-09-13）"
              "「主題は止まり、光と粉塵だけが動く」は、**運動の記述である。**"
              "動画の §18 には `Motion Prompt` があり、そこが受け取る。"
              "⚠️ **画像プロンプトの側には渡らない**——`video-spec` は Visual Prompt に"
              "運動の語を禁じている。**だから行き先は動画の側だけである。**",
    "beats": "⚠️ **一部だけが渡る。** `range` と `density` は英語であり、"
             "Master Prompt の `{BEATS}` に入る。"
             "**`what` は日本語であり、渡らない**——§8 の散文が §18 で英語に書き直される。"
             "ビートは**画面に在る時間の配分**でもあり、それは編集が決める。",
    "reference_set": "参照集合。**台帳から導かれる**（`Project.known_keys()`）。"
                     "`params.references`——**プロンプトの語ではなく、API に渡す実体である。**"
                     "⚠️ **画像の側にも渡る。** 最初のコマにも同じ連続性が要る。",
    "attached": "**実際に添付したか。** `reference_set` が「添付するべきもの」であるのに対し、"
                "こちらは「**添付したもの**」である——**L6 が両者の食い違いを鳴らす。**"
                "受け火 V1 はこの欄が無いまま生成され、"
                "**花のシートが無いクリップが2本出た。**",
    "forbidden_set": "禁制集合。§18 の Negative Prompt に入る。"
                     "⚠️ **`disclosure_state` と行き先が同じである**——"
                     "**両方とも Negative として現れる**（L10 が片方を見ている）。"
                     "⚠️ **画像の側にも渡る。** 決定（2026-09-13）で画像が先に走る——"
                     "**開示の禁制は、最初のコマで破られうる。**",
    "disclosure_state": "観客の知識の状態。**台帳の `disclosure` と突き合わせられる**"
                        "（L7・L9）。§18 の Negative Prompt に入る——"
                        "**L10 がここを見ている唯一の検査である。**"
                        "⚠️ **画像の側にも渡る**（決定 2026-09-13）。"
                        "⚠️ **いまその系列を読む検査は無い**——"
                        "画像仕様に人が読める形で書いてあるだけである。**読み手は段2で付く。**",
    "text_channel": "⚠️ **この欄は `kind` で割れる。**"
                    "`overlay`——**文字を生成器に描かせない。** タイムラインの `text_events` が"
                    "焼く（`timeline.schema.json`「自前レンダを持つ理由は文字合成で、"
                    "これは基盤がやる」）。`voice`——§14 の声の行として Audio Prompt へ。"
                    "**行き先が2つ在るのは、欄が2種類を束ねているからである。**"
                    "⚠️ **割るのは引き渡しの層である**（段2）——`L19` は行き先の語彙と"
                    "送り先の実在だけを見る。",
    "sound": "音。**行き先は Semantic Audio Loom であり、基盤は音を作らない。**"
             "⚠️ **契約は M6 で、まだ無い**——だから `handover:loom` は"
             "**渡し口であって、渡している実装ではない。** 空を OK と言わない。",
}
