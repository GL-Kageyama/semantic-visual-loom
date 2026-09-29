# -*- coding: utf-8 -*-
"""Assemble one odyssey video spec (§1–20) from a per-shot content dict.

What the template owns, and why:
  · the four work constants (L26), the Duration line (L23), the seven slot headings (L17),
    and §18's `Negative Prompt` / `Style Motion` — all taken from lit.py, which was extracted
    from the written specs. Nothing here retypes them.
  · §18's seven slots are emitted as pure English, and §18's preamble head is shared.
The content dict owns only what is that shot's own: its beats, its subjects, its camera, its prose.
"""
import re
import lit

SEVEN = ["Master Prompt", "Visual Prompt", "Motion Prompt", "Camera Prompt",
         "Audio Prompt", "Negative Prompt", "Style Motion"]

# §16's invariant floor — the three BASE_NEGATIVES of specmap, plus the format's own pacing rule.
FLOOR_ITEMS = [
    "- No music of any kind in this shot. ⚠️ **この経路では `No BGM` が、実際に受け取られる数少ない否定の一つである。**",
    "- No on-screen subtitles, no captions, no burned-in subtitles in any language. ⚠️ **この経路には、字幕を作るための公式の記法がある**（`【】`）——**ゆえにこの節は、他の二つの経路よりここで必要である。**",
    "- No watermark.",
    "- No uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion.",
]

ROUTE_NOTES = [
    "- ⚠️ **REF_BOARD は無い。** この経路は絵コンテを要求しない。**この経路の参照素材は `role` を持つ**——`reference_image`（最大30点）・`reference_video`・`reference_audio`・`first_frame`・`last_frame`。**この経路の入力の型は5つである**（テキストのみ／参照画像／先頭フレーム／動画編集／動画延長）。",
    "- ⚠️ **この34本は「テキストのみ」の型である。** `first_frame` ではない——⚠️ **先頭フレームの型は `ratio: adaptive` を要求する**（`specmap.MODELS` の註）。この作品は `16:9` を固定する。",
    "- ⚠️ **この経路は、実在の顔を含む参照画像・参照動画を受け取らない**（公式の警告）。**この作品の人物は実在しないので、この制限には当たらない。**——**当たらないことを、ここに書く。** ⚠️ **それでも、この作品は参照を渡さない**（裁定②）。**渡さない理由は制限ではなく、選択である。**",
    "- ⚠️ **§1–17 は下敷きであり、生成器へ投入するのは §18 だけである。**",
]

INSTANCE_DATE = """- Generation Date: ⚠️ **未記入。** **この作品は、まだ1本も生成していない。**
- ⚠️ **日付は、生成した者が生成した日に書く。****私ではない**——**何が実際に起きたかを、私は見ていない。** ⛔ **世代の記録は `takes/` に置く**（この作品にはまだ無い）。**この仕様は世代を写さない。**"""

OBSERVED = """- ⚠️ **まだ1本も生成していないので、観察は無い。** **空である。** ⛔ **絵を見る検査は、この基盤に無い**——**見たことを書けるのは、見た者だけである。**"""

VERSION_HEAD = """`0.1.0` — **初版である。** ⛔ **この節は仕様の側であって、世代の記録ではない**——**記録は `takes/` に在る。** **採用は、まだ選ばれていない**——**選ぶのは著者である**（`CLAUDE.md`「**生成はサンプルである。**」）。"""


def _bullets(items):
    return "\n".join(b if b.lstrip().startswith(("-", "1.")) else "- " + b for b in items)


def _band(c, A):
    """演出要約——**題の上に開く帯である。**

    雛形が持つのは**形だけ**（罫線・副題の位置・3行の字下げ）であり、
    文はそのショットの `content/sNN.py` が持つ（`c["band"]`＝副題＋3行）。
    ⚠️ **この帯は生成器へ1バイトも届かない**——投入されるのは §18 だけである。
    ゆえにここだけが日本語である（`CLAUDE.md`「**Do not make the strings handed
    to generation Japanese**」は投入される文字列の規則であって、帯は投入されない）。
    ⚠️ **欠けたら落ちる**——`c["band"]` は必須である（`L38` が仕様の側でも鳴る）。
    """
    band = c["band"]
    assert len(band) >= 4, "%s: 帯は副題のほかに3行を要る" % c["n"]
    A("# ═══ 演出要約 ════════════════════════════════════")
    A("# " + band[0])
    A("#")
    for ln in band[1:]:
        A("#   " + ln)
    A("# ═════════════════════════════════════════════════")
    A("")


def render(c):
    n, D, fmt = c["n"], c["duration"], c["format"]
    has_man = c.get("has_man", False)
    idblock = lit.IDENTITY
    L = []
    A = L.append

    _band(c, A)
    A("# Seedance 2.5 Full Specification — 主題歌MV『永遠より遠い』 odyssey-%s「%s」 / %ss" % (n, c["title"], D))
    A("")
    A(c["header"].strip("\n"))
    A("")
    A("---")
    A("")
    A("# 1. VIDEO")
    A("")
    A("- Duration: `%ss`" % D)
    A(lit.CONST)
    A("- Generation Intent: %s" % c["intent"])
    A("")
    A("# 2. WORLD")
    A("")
    A("## World Concept")
    A("")
    A(c["world_concept"])
    A("")
    A("## World Rules")
    A("")
    A(_bullets(c["world_rules"]))
    A("")
    A("## Visual Language")
    A("")
    A(_bullets(c["visual_language"]))
    A("")
    A("# 3. SUBJECTS")
    A("")
    for s in c["subjects"]:
        A("## %s" % s["name"])
        A("")
        A("- Reference: %s" % s["ref"])
        A("- Appearance: %s" % s["appearance"])
        A("- Behavior: %s" % s["behavior"])
        A("- Continuity Requirements: %s" % s["continuity"])
        for extra in s.get("notes", []):
            A("- %s" % extra)
        A("")
    A("# 4. ENVIRONMENT")
    A("")
    e = c["environment"]
    A("- Location: %s" % e["location"])
    A("- Environment Elements: %s" % e["elements"])
    A("- Environmental Behavior: %s" % e["behavior"])
    A("")
    A("# 5. OBJECTS")
    A("")
    A(_bullets(c["objects"]))
    A("")
    A("# 6. REFERENCES")
    A("")
    A("- REF_CHARACTER: %s" % c["ref_character"])
    A("- REF_FORMAT: `%s` — this defines the seven §18 slots" % fmt)
    A("- REF_STYLE: `cinematic-still` (HIGH)")
    A("- REF_SOURCE: `projects/odyssey/bible.yaml` and `projects/odyssey/ledger.yaml` (CRITICAL)")
    A("\n".join(ROUTE_NOTES))
    for extra in c.get("ref_extra", []):
        A(extra)
    A("")
    A("# 7. NARRATIVE")
    A("")
    nar = c["narrative"]
    A("- Core Event: %s" % nar["core"])
    A("- Beginning: %s" % nar["beginning"])
    A("- Turn: %s" % nar["turn"])
    A("- Peak: %s" % nar["peak"])
    A("- Pull: %s" % nar["pull"])
    A("")
    A("# 8. TEMPORAL STRUCTURE")
    A("")
    A("- Timing Policy: `STRUCTURED` / `NON_UNIFORM`")
    A("- Temporal Sequence:")
    for i, (rng, dens, text) in enumerate(c["beats"], 1):
        A("  - MOVEMENT %d `%s` — density: `%s` — %s" % (i, rng, dens, text))
    A("- Temporal Density: %s" % c["density"])
    A("")
    A("# 9. ACTION")
    A("")
    for aid, before, after in c["actions"]:
        A("- `%s` — Before: %s After: %s" % (aid, before, after))
    A("")
    A("# 10. CAMERA")
    A("")
    A("- Camera Language: %s" % c["camera"]["language"])
    A("- Camera Events: %s" % c["camera"]["events"])
    A("- Camera Behavior: %s" % c["camera"]["behavior"])
    A("")
    A("# 11. MOTION")
    A("")
    m = c["motion"]
    A("## Subject Motion")
    A("")
    A(m["subject"])
    A("")
    A("## Object Motion")
    A("")
    A(m["object"])
    A("")
    A("## Environmental Motion")
    A("")
    A(m["environment"])
    A("")
    A("## Physical Characteristics")
    A("")
    A("- **Weight**: %s" % m["weight"])
    A("- **Inertia**: %s" % m["inertia"])
    A("- **Acceleration**: %s" % m["acceleration"])
    A("- **Fluidity**: %s" % m["fluidity"])
    A("- **Impact**: %s" % m["impact"])
    A("")
    A("# 12. EMOTION")
    A("")
    A("- Emotional Arc: %s" % c["emotion"]["arc"])
    A("- Emotional Events: %s" % c["emotion"]["events"])
    A("")
    A("# 13. LIGHTING")
    A("")
    A("- Base Lighting: %s" % c["lighting"]["base"])
    A("- Lighting Events: %s" % c["lighting"]["events"])
    A("")
    A("# 14. AUDIO")
    A("")
    a = c["audio"]
    A("- Dialogue: %s" % a["dialogue"])
    A("- Sound Effects: %s" % a["sfx"])
    A("- Music: %s" % a["music"])
    A("- Environment: %s" % a["environment"])
    A("")
    A("# 15. CONTINUITY")
    A("")
    co = c["continuity"]
    A("- Identity: %s" % co["identity"])
    A("- Spatial: %s" % co["spatial"])
    A("- Temporal: %s" % co["temporal"])
    A("- Visual: %s" % co["visual"])
    A("- Motion: %s" % co["motion"])
    A("- Sound: %s" % co["sound"])
    A("- ⚠️ **この34本は、すべて同じ経路である**（`SEEDANCE 2.5`）。**他の作品の三本（`MINIMAX H3`）とは別である。** ⚠️ **ずれてはならないのは、場所と、パレットと、光と%sである**——**プロンプトの字面ではない。**"
      % ("、そして何よりも顔" if has_man else "、そして画面の文法"))
    A("")
    A("# 16. CONSTRAINTS")
    A("")
    A("## MUST NOT")
    A("")
    A(_bullets(c["must_not"]))
    A("- ⚠️ **形式 `%s` 自身の禁制**（カードの `## Negative`、逐語）: `%s`" % (fmt, lit.FORMAT_NEG[fmt]))
    A("")
    A("\n".join(FLOOR_ITEMS))
    A("")
    A("## MUST")
    A("")
    A(_bullets(c["must"]))
    A("")
    A("## PREFER")
    A("")
    A(c["prefer"])
    A("")
    A("## ALLOW")
    A("")
    A(c["allow"])
    A("")
    A("# 17. GENERATION PRIORITIES")
    A("")
    for i, p in enumerate(c["priorities"], 1):
        A("%d. %s" % (i, p))
    A("")
    A("---")
    A("")
    A("# 18. SEEDANCE 2.5 PROMPT MAPPING")
    A("")
    A(lit.PREAMBLE_HEAD)
    A(c["preamble_tail"])
    A("")
    A("## Master Prompt")
    A("")
    A(c["master"].replace("{IDENTITY}", idblock).strip())
    A("")
    A("## Visual Prompt")
    A("")
    vp = c["visual_scene"].strip()
    if has_man:
        vp += " **In the frame. %s** ⚠️ **This description is pasted whole and is not summarized; it is this work's identity lock.**" % idblock
    A(vp + " " + c["visual_meta"].strip())
    A("")
    A("## Motion Prompt")
    A("")
    A(c["motion_prompt"].strip())
    A("")
    A("## Camera Prompt")
    A("")
    A(c["camera_prompt"].strip())
    A("")
    A("## Audio Prompt")
    A("")
    A(c["audio_prompt"].strip())
    A("")
    A("## Negative Prompt")
    A("")
    A(lit.NEGATIVE)
    A("")
    A("## Style Motion")
    A("")
    A(lit.STYLE_MOTION)
    A("(Source: the `Motion character` of the style card `cinematic-still`.)")
    A("")
    A("---")
    A("")
    A("# 19. GENERATION INSTANCE")
    A("")
    A("## Instance")
    A("")
    A("- Instance ID: `odyssey-%s-%ss-01`" % (n, D))
    A("- Segment ID: `%s`" % c["segment"])
    A("- Specification Version: `0.1.0`")
    A(INSTANCE_DATE)
    A("")
    A("## Resolved Values")
    A("")
    A("- Duration: `%ss`" % D)
    A("- References: %s" % c["resolved_references"])
    A("- Temporal Structure: `%d movements, NON_UNIFORM — %s`. The held movement = `none`"
      % (len(c["beats"]), " / ".join(b[0] for b in c["beats"])))
    A("- Camera Events: `%s`" % c["camera_events_count"])
    A("- Action Events: `%s`" % " → ".join(a[0] for a in c["actions"]))
    A("- Audio Events: `%s`" % c["audio_events"])
    A("- Output: `1920×1080, 24fps, 16:9 landscape, single clip`")
    A("")
    A("# 20. ITERATION")
    A("")
    A("## Version")
    A("")
    A(VERSION_HEAD)
    A("")
    A("### 未処理（この版では決めていない）")
    A("")
    A(_bullets(c["unresolved"]))
    A("")
    A("## Observed Problems")
    A("")
    A(OBSERVED)
    A("")
    A("## Anticipated risks (to check in the first generation)")
    A("")
    A(_bullets(c["risks"]))
    A("")

    text = "\n".join(L)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"

    # Fail loudly rather than write a spec that a layer will reject.
    assert re.search(r"^- Duration: `%ss`$" % re.escape(D), text, re.M), n
    assert lit.CONST in text, n
    assert lit.NEGATIVE in text, n
    assert lit.STYLE_MOTION in text, n
    body18 = text.split("# 18. SEEDANCE 2.5 PROMPT MAPPING", 1)[1].split("\n---\n", 1)[0]
    for slot in SEVEN:
        assert re.search(r"^## %s\s*$" % re.escape(slot), body18, re.M), (n, slot)
    CJK = re.compile(r"[぀-ヿ一-鿿]")
    for slot in SEVEN:
        b = re.search(r"^## %s\s*\n(.*?)(?=\n## |\Z)" % re.escape(slot), body18, re.S | re.M).group(1)
        assert not CJK.search(b), "%s: CJK inside slot %s: %r" % (n, slot, CJK.findall(b)[:8])
    for slot in ("Master Prompt", "Visual Prompt"):
        b = re.search(r"^## %s\s*\n(.*?)(?=\n## |\Z)" % re.escape(slot), body18, re.S | re.M).group(1)
        if has_man:
            assert lit.IDENTITY in b, "%s: identity block not verbatim in %s" % (n, slot)
        else:
            # ⚠️ **逆向きも見る。** `has_man` が偽なら、同一性の塊は**どちらの欄にも在ってはならない。**
            # 2026-09-29 の実測: `has_man` を「台帳の参照集合が `男.identity` を名乗るか」で
            # 決めていたため、**人物の居ない10本の画に「一人の男が枠に居る」が貼られ**、
            # 同じ欄の「人は一人も居ない」と正面から矛盾した（裁定②で参照画像が無いので、
            # この文字列が生成器への入力の全部である）。**この検査はその再発を止める。**
            assert lit.IDENTITY not in b, (
                "%s: has_man が偽なのに同一性の塊が %s に在る——"
                "人物の居ない画に人物を貼っている" % (n, slot))
    return text
