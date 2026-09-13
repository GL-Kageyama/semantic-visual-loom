"""`video-spec` §1–20 とショット記録の欄との対応。**宣言であり、検査される。**

⚠️ **散文で置くと腐る。** だからここは目録であって、`check.py` が
**両方向に閉じているか**を確かめる（L11・L12）——**節が欄を名指し、欄が節を名指し、
どちらにも漏れが無いこと。** 新しい節が仕様に足されれば、L11 が鳴る。

⚠️ **「落ちる」は「失われる」ではない。** ショット記録の欄にならない節も、
仕様（`spec:` が指す先）にはそのまま在る。**落ちるのは記録からであって、作品からではない。**
"""

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
    "18. WAN 3.0 PROMPT MAPPING",
    "19. GENERATION INSTANCE",
    "20. ITERATION",
)

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
    "18. WAN 3.0 PROMPT MAPPING": {
        "to": (),
        "rest": "spec",
        "evidence": "⚠️ **スロットは7つである**（Master / Visual / Motion / Camera / Audio / "
                    "Negative ＋ **Style Motion**）——`PROMPT_SLOTS` を見よ。"
                    "実測の6つは**仕様に在るもの**で、`Style Motion` は**決定（2026-09-13）で"
                    "足した行き先**である（実測 0/99）。"
                    "**§6 が「the six §18 slots」と書き、§6 の `REF_FORMAT` がそれを定義する**"
                    "——§18 の形は**様式カード（`references/formats/video-spec.md`）の持ち物**である。"
                    "⚠️ **節の名が `WAN 3.0` を名乗る**＝ここは**モデル固有の投影**であって、記録ではない。"
                    "**だから `spec:` はここを指す**——モデルが変われば §18 だけが差し替わり、欄は残る。"
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
#: ⚠️ **7つとも `##` の小節である**（実測: 99本すべてが6小節。`Style Motion` は 0/99）。
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
    "spec": "§1–20 を指す。**仕様は自分自身を指す欄を持たない**",
    "attached": "**実際に何を添付したか。§1–20 に欄が無い**——"
                "受け火 V1 はここが無いまま生成され、花のシートが無いクリップが2本出た",
}
