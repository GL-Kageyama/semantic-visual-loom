# -*- coding: utf-8 -*-
"""The prose that most shots share, parameterized so each shot can be its own shot.

Modelled on s05, which the author approved as the exemplar (「この形で30本書く」).
Where s05 wrote a per-shot ⚠️ sentence after an invariant clause, the clause is here and the
sentence is a parameter.
"""
import lit

# ---- §18 preamble ---------------------------------------------------------
# The 5th paragraph of the preamble is the same in every shot; the shot adds its own after it.
PREAMBLE_TAIL_STD = (
    "⚠️ **この節の `Negative Prompt` と `Style Motion` は、34本で同一である。** 理由は `L10` にある——"
    "`ledger.disclosure` の4つの変化点が `negative: covered`（**§18 の `Negative Prompt` は変わらない**）を"
    "宣言しており、**「覆った」は「同じである」を要求する。** ゆえに**ショット固有の禁制はこの節に書かない**"
    "——それは `shot.forbidden_set`（引き渡しの層）と §16 が持つ。"
    "⚠️ **形式カード自身の `Negative` は §16 の側から届く**——この作品は形式をショットごとに名乗るので、"
    "**カードの `Negative` をここに混ぜれば、`Negative Prompt` がショットごとに動き、"
    "`L10` の4つの `covered` が偽になる。**"
)


def preamble_tail(own):
    return PREAMBLE_TAIL_STD + "\n" + own


# ---- §2 World Concept -------------------------------------------------------
CONCEPT = (
    "A bronze-age Mediterranean island shore at the end of the day, and the open sea beyond it. "
    "**No place in this work is named aloud.** The island holds a cave and a goddess who lives in it; "
    "a man has been on this shore for years and has not been able to leave it. "
    "⚠️ **This is a theme-song music video:** one song of 299.920 seconds, thirty-four shots, no episode — "
    "**the work does not advance a story. It holds one man at the edge of one island and asks the same "
    "question with other light.** ⚠️ **The poem is older than classical Greece, and the picture is built "
    "that way**: rough stone, wood, coarse cloth and bronze; no marble, no columns, no temple."
)


def world_concept(tail):
    return CONCEPT + " " + tail


# ---- §2 World Rules --------------------------------------------------------
# (invariant clause, parameter name or None).  The parameter is the shot's own sentence.
RULES = [
    ("**The people in the work do not know that they are inside a film.** ⚠️ **This is why he does not "
     "look at the lens** — the camera is not there for him.", None),
    ("**The answer is never given.** The goddess offers and the man says nothing. **A shot in which he "
     "opens his mouth is a shot this work does not have.**", "answer"),
    ("**The goddess is never a face.** She is a voice from off-frame, a warmth on surfaces, moving air, "
     "and a light on the water that comes from behind the camera.", "goddess"),
    ("**No proper name is ever seen or heard.** Not on screen, not in the song.", "name"),
    ("**The bow does not appear in this work.** The axe is inside the fifth book; the bow is outside it.",
     "bow"),
    ("**This work does not arrive.** The raft is still offshore in the last frame of the last shot.", None),
    ("**No text appears on any surface.** The work names things by voice; it does not write them.", None),
    ("**The age of the poem is bronze-age Mediterranean, before classical Greece. It does not move.** "
     "⚠️ **He is not dressed as a classical hero** — no armour, no helmet, no greaves, one coarse undyed "
     "wool tunic, bare feet.", None),
    ("**Only so many places can stand at once.**", "places"),
    ("**This work speaks Japanese.** It is the language of the song, and there is no other voice in it.",
     "japanese"),
]


def world_rules(tails, extra=None, drop=()):
    out = []
    for clause, key in RULES:
        if key in drop:
            continue
        if key is None:
            out.append(clause)
        else:
            assert key in tails, "world_rules: missing tail %r" % key
            out.append(clause + " " + tails[key])
    return out + list(extra or [])


# ---- §2 Visual Language ----------------------------------------------------
def visual_language(**kw):
    d = {
        "Art Direction":
            "A bronze-age Mediterranean island shore at the end of the day, photographed as a film. "
            "Rough wet stone, coarse sand, low dense scrub, sea-worn driftwood; undyed wool and stiff "
            "salt cloth. ⚠️ **No marble, no columns, no architecture of any later age.**",
        "Color Language":
            "A narrow, graded palette — cold slate blue in the water and the wet stone, warm ochre "
            "where the low sun falls. ⚠️ **Nothing is lit apart from the shore** — the same raking "
            "light falls on everything in the frame, and **the shot has no second light.**",
        "Texture":
            "Wet shingle with grain and individual stones; coarse wool with visible fibre and a worn "
            "seam; skin roughened and marked; the water's surface fine-grained and broken. Film grain "
            "present and even.",
        "Rendering":
            "Photographic — anamorphic optics, a moderate depth of field, subtle oval bokeh, a gentle "
            "flare where the light is in frame. **Not a photograph's stillness: a film frame, with a "
            "real lens's fall-off at the edges.** No illustration, no CGI look, no cartoon color.",
        "Visual Density": "Low to moderate.",
        "Time": "`日没` — the last of the day. **The work does not fix a date.**",
        "Atmosphere": "The hour when the light stops being able to be ignored.",
    }
    d.update(kw)
    return ["%s: %s" % (k, v) for k, v in d.items()]


# ---- §3 the man ------------------------------------------------------------
MAN_REFERENCE = (
    "⚠️ **画像は1枚も無い。この作品は参照を渡さない**（裁定②。そしてこの経路は既定で何も添付しない）。"
    "**参照は `ledger.characters.男.identity` の英文そのものである**——そして `video-spec` 形式カードの"
    "規則により、**その塊は §18 にまるごと貼られる。「要約も、参照もしない」**（逐語:「the continuity "
    "block … is pasted whole into every instance — not summarized, not referenced」）。"
    "⚠️ **この基盤に、この規則を使った先例は1本も無い**——**この作品が最初である。**"
)

MAN_APPEARANCE = (
    "**§18 の `Visual Prompt` と `Master Prompt` に逐語で入っている塊が、この人物の外見である。**"
    "ここでは要約しない——**要約は、この作品でいちばん高くつく省略である。** ⚠️ **要点だけを数えるなら**: "
    "海で年を経た一人の男。背が高く、骨が太く、肩幅が広い。**筋肉質ではなく、厚い**——一生、櫂を引き、"
    "荷を担いできた体である。肌は日と塩で濃く焼け、粗い。前腕と手の甲には、淡い傷と縄の痕が交差している。"
    "髪は黒く、こめかみに白が混じり、切っておらず、塩で固まり、耳を越えて垂れる。髭は濃く、乱れ、黒に白が混じる。"
    "額は重く、目は奥にあり、鼻は一度折れて曲がったまま、顎は硬い。**若くない男の顔であり、老いても見えない顔である。** "
    "着ているものは**これだけ**: 粗い無染色のウールの tunic 一枚、肩の縫い目が擦り切れ、plain な革の紐で帯にしている。"
    "**外套は無く、サンダルは無く、留め金も指輪も装身具も無い。****足は裸、脚は裸、腕は裸である。**"
)

MAN_IDENTITY_CONTINUITY = (
    "**Must preserve** — ⚠️ **§18 の `Visual Prompt` と `Master Prompt` に貼られた同一性の塊の、一句一句。**"
    "体格・肌・髪・髭・顔・傷・**着ている一枚と、着ていないすべて**。**裸足であること。** "
    "⚠️ **この作品の顔の基準は `s05` が立てた**——**この1本はそこから外れてはならない。** "
    "**May change** — %s"
)


def man_subject(behavior, may, extra_notes=None, name="男"):
    return {
        "name": name,
        "ref": MAN_REFERENCE,
        "appearance": MAN_APPEARANCE,
        "behavior": behavior,
        "continuity": MAN_IDENTITY_CONTINUITY % may,
        "notes": extra_notes or [],
    }


# ---- §15 Identity ----------------------------------------------------------
def identity(extra_must, may, is_standard=False):
    head = ("⚠️ ⛔ **この1本が、この作品の同一性の基準を立てる。** " if is_standard
            else "**Must preserve** — §18 に逐語で貼られた同一性の塊の、一句一句。 ")
    lock = ("⚠️ **この基盤は、参照画像が無い状態でそれを守る規則を1つだけ持っている**——`video-spec` "
            "形式カードの逐語:「**Identity lock.** … the continuity block … is **pasted whole into every "
            "instance** — not summarized, not referenced.」**ゆえにこの仕様は、あの塊を §18 の "
            "`Visual Prompt` と `Master Prompt` の両方に、まるごと貼っている。** ⚠️ **要約しない。** ")
    return head + extra_must + " " + lock + "**May change** — " + may


# ---- §14 Audio -------------------------------------------------------------
NO_DIALOGUE = (
    "**None.** ⚠️ **彼は口を開かない**（`world.rules`）。**この作品に台詞は一つも無い。** "
    "⚠️ **この作品は日本語を話す**；§18 がそれを名乗る。"
)

NO_MUSIC = (
    "**None, by specification.** ⚠️ **これは省略ではない** — §16 と §18 の両方が床の `no background music` "
    "を運び、⚠️ **この経路では `No BGM` が、実際に受け取られる数少ない否定の一つである。** "
    "音床も、スコアも、切れ目のスティングも無い。"
)

AUDIO_PROMPT = (
    "**The language of this work is Japanese** — Japanese is the language of the song, and the song is the "
    "only voice this work will ever have. **No line is spoken in this shot: there is no dialogue anywhere "
    "in this work, and there is no voice-over and no narration.** **The Japanese is not spoken here; it is "
    "what this work is** — and **nothing is written on screen**: no subtitles, no captions, in any language. "
    "%s **No voice of any kind** — no one here calls and no one is called. **Music: none — this shot "
    "carries no music of any kind.** No bed, no score, no sting, no drum."
)


# ---- §16 the prohibitions that hold in every shot --------------------------
def must_not_common(has_man=True, goddess_extra=None):
    out = [
        "No woman in frame at any distance, in any focus; **no face for the goddess**, no portrait, no "
        "close-up of a woman, no white robes, no classical drapery, no veil, no halo, no divine light "
        "around a figure." + ((" ⚠️ " + goddess_extra) if goddess_extra else ""),
        "No boat, no ship, no hull, no keel, no planking, no sail, no raft, and no other vessel.",
        "No blood, no wound, no corpse, no slaughter, no butchery, no carcass.",
        "No fire, no torch, no lamp, no flame used as a light source. ⚠️ **この作品の光は、日の光・月・星だけである。**",
        "No classical architecture, no columns, no marble, no temple, no built structure of any kind — "
        "no jetty, no wall, no stair, no path.",
        "No legible text on any surface; no letters, no numerals, no writing, no marks of a hand.",
        "No modern object, no machine, no synthetic material, no clothing of any later age.",
        "**No cut to a second setup.**",
        "No handheld wobble, no unmotivated camera move, no snap zoom, no unnatural rotation.",
        "No flat television lighting, no snapshot framing, no pure cartoon color, no CGI look, no illustration.",
    ]
    if has_man:
        out.insert(0, "⚠️ **No heroic treatment of the man**: no heroic pose, no heroic lighting, no "
                      "muscular hero's body, no armour, no helmet, no greaves, no shield, no sword, no "
                      "spear, no bow, no arrow, no quiver, no crown, no diadem, no sceptre, no ring, no "
                      "brooch, no jewellery, **no cloak, no sandals, no fitted or tailored clothing, no "
                      "dyed fabric.**")
        out.insert(1, "⚠️ **No youthful face, no beardless face, no clean or unlined skin.** **彼は若くない。**")
    return out


VISUAL_META = (
    "Anamorphic lens with subtle oval bokeh and a gentle flare where the light is in frame; a moderate "
    "depth of field; a graded palette of cold slate blue in the water and the wet stone, warm ochre where "
    "the low sun falls. Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked; "
    "wet shingle with individual stones; even film grain over everything. No painterly stroke, no airbrush, "
    "no plastic surface, no CGI look, no illustration."
)

PRELUDE = "0-2.501s placeholder"

if __name__ == "__main__":
    print("common.py OK — rules:", len(RULES), "| floor clauses available")
