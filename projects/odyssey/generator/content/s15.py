# -*- coding: utf-8 -*-
"""odyssey-s15 — coexisting-realities — 海 / 夜 / 10.931s. Two destinations in one frame."""
import common as K


_MN = K.must_not_common(has_man=False, goddess_extra=(
    "⚠️ **この1本には、人が一人も居ない。** **ゆえに女神の禁制は、人の形ではなく、"
    "海そのものの形で来る**——**夜の海を、女の形にしないこと**"
    "（`characters.女神.negatives` の逐語:「no visible body, no hands, no feet, no arms, "
    "no silhouette with a readable outline」）。"))
_RAFT = "No boat, no ship, no hull, no keel, no planking, no sail, no raft, and no other vessel."
assert _MN.count(_RAFT) == 1
_MN[_MN.index(_RAFT)] = (
    "No boat, no ship, no hull, no keel, no planking, no sail, no raft, and no other vessel. "
    "⚠️ **この1本に舟も筏も入らない**——**ゆえにこの禁制は、この1本では一字も違わず効く。**")


C = {
 "n": "s15",
 "title": "永遠より遠い／なんでもない島へ——二つの行き先が、一枠に",
 "duration": "10.931",
 "format": "coexisting-realities",
 "has_man": False,
 "segment": "chorus-1-3",

 "header": """# chorus-1 / motion / 様式美 / coexisting-realities
⚠️ **行: `l12`+`l13` ／ 場所: `海` ／ 時刻: `夜` ／ 尺: 10.931秒。**
⚠️ **形式（`coexisting-realities`）は §6 の `REF_FORMAT` に書く提案である。** ショット記録に `REF_FORMAT` の欄は無い——**形式は仕様の側にある。****ゆえにここに書いた形式は、まだ検査されていない。**
⚠️ **2行を束ねた理由は長さである。** 実測: **`l12` は 7.021秒、`l13` は 3.910秒。** ⚠️ **`l13` は下限4秒に満たない**（`s07` の註を見る）。⚠️ **この2行も、曲が既に並べている対である**（「永遠より遠い／なんでもない島へ」）。
⛔ **この1本で、この作品の主題が一度だけ正面から出る。** **「永遠より遠い」と「なんでもない」**——**この二つは矛盾している。** **そして曲は、それを同じサビの続きの2行として並べている。** ⚠️ **形式は `coexisting-realities`。****この形式がこの作品で要るのは、まさにこの1本のためである。**
⚠️ **役は `様式美`。** 固有基準は「構図・余白・**静止の強度**」—— ⛔ **この1本では、動いているのに静止している。** **引くほど遠くなるだけである。**
⚠️ **この仕様のショット記録は `shots/odyssey-s15.yaml` である。**""",

 "intent": "One continuous take of one change — **二つの遠さが、一つの枠に、二つとして立つ。** 最初のコマでは**水と水平線があり、遠さが二つある。** 最後のコマでは**カメラが引ききり、二つの遠さがどちらも遠くなっている**——⚠️ **同じ一つの枠に並ぶのが、切れ目のコマである。** ⛔ **切らない。分割しない。説明しない。****どちらが `永遠より遠い` で、どちらが `なんでもない島へ` かは、名指さない。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、矛盾する二つの行き先を、一つの画に並べる。** "
   "**「永遠より遠い」と「なんでもない」**——**この二つは矛盾している**（記録のヘッダの逐語）。"
   "**そして曲は、それを同じサビの続きの2行として並べている。** "
   "⛔ **ゆえにこの1本は、その矛盾を説明しない。****説明は、この形式の仕事ではない。** "
   "**この1本の仕事は、二つを同じ一つの枠の中に、同じ一つの光で置くことである。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本に返事は無い。****島は画面に無い**（`unit` の逐語:「海と、水平線だけがある。」）。"
               "**島が応えるのは `s20` である。**",
     "goddess": "⚠️ **この1本に彼女の姿は無い。****四つの姿のどれとしても現れない。** "
                "**この1本の光は星であり**（`ledger.locations.海.states.夜` の逐語:「光源は星と、"
                "その水面の反射だけである。」）、**彼女の第四の姿（枠の外の背後から来る水面の光）ではない。** "
                "⚠️ **この区別は、この1本では特に要る**——**この1本の bearer は光である**（§3 を見る）。",
     "name": "⚠️ **この1本には歌がある**——`l12`+`l13` である。**名はどこにも無い。**"
             "**行き先の名も、島の名も、人の名も。**",
     "bow": "⚠️ **この1本に持ち手が無い。****弓も、斧も、櫂も写らない。**",
     "places": "この1本が置くのは一つ——`海`、**夜である。****陸は無い。** "
               "⚠️ **`海.geography` の逐語:「no land is visible in any direction** including behind」"
               "——**ゆえにこの1本の二つの遠さのうち、遠い側は島ではない。**",
     "japanese": "⚠️ **この1本には歌がある**——`l12`「永遠より遠い」と `l13`「なんでもない島へ」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **この1本の二つの遠さに、先後は無い。** **どちらも過去でも未来でもない。**"
     "**同じ一つの場所と時刻の中に、同時に在る。** ⚠️ **これはこの形式の核である**"
     "（カードの `## Negative` の逐語:「**no reality declared earlier than another**」）。",
     "⛔ **この1本に人は一人も居ない。** **カメラは誰の位置にも立っていない。** "
     "⚠️ **この作品で「人物の居ない1本」の見本は `s02` である**——**この1本はその側である。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, photographed as a film frame, held in depth: **the near water below, broken into "
     "fine facets and running; the far horizon above it, level and unbroken; and the sky over both, "
     "starred.** ⚠️ **二つのあいだに、線も、縁も、段も無い**——**同じ一つの水であり、同じ一つの空である。** "
     "⚠️ **陸がどこにも無い**——**島も、岸も、岬も、水に立つ岩も無い。** ⚠️ **舟も、帆も、鳥も、"
     "人も無い。** ⚠️ **No marble, no columns, no architecture of any later age.**",
   "Color Language":
     "A narrow, graded palette over the whole frame — black water, a sky a shade or two above it, and one "
     "white line: the reflected path of the stars, which runs from the near water out to where the water "
     "ends. ⚠️ **近い側と遠い側で色温度を変えない**——**二つは同じ一つの光でできている。** "
     "⚠️ **月も、火も、灯も無い**——**the shot has no second light.**",
   "Texture":
     "The water's surface fine-grained and broken into facets, running; the far water and the horizon "
     "smooth and undifferentiated; the sky clean and even, with grain over everything. ⚠️ **この1本には、"
     "肌も、布も、木も無い**——**人が一人も居ないので、この1本の面は水と空だけである。** "
     "Film grain present and even.",
   "Visual Density":
     "**Low, and it is the composition.** ⚠️ **この1本は `様式美` である**——**余白が主題である。** "
     "**枠の上三分の二は空であり、下三分の一に水と一本の白い線がある**——"
     "**引くほど、余白が増える。**",
   "Atmosphere": "The hour in which two destinations stand in one frame and neither has been reached.",
   "Time": "`夜` — the source is the stars and their reflection on the water; **the waves are black and "
           "the reflected path alone is white**（`ledger.locations.海.states.夜` の逐語）。"
           "**`s09`〜`s15` と同じ夜である。**⚠️ **この作品は話を進めない**"
           "（§2 の逐語:「the work does not advance a story」）——**ゆえにこの1本と、`s16` の夜明けとの"
           "あいだに、順序を読まない。** **画の中に日付を与えるものは何も無い。**",
 }),

 "subjects": [
   {"name": "二つの遠さ",
    "ref": "⛔ **これがこの1本の `REALITIES` である。** ⚠️ **参照は `海`・`海.geography`・"
           "`海.states.夜` である**——**この作品に参照画像は無い**（裁定②）。",
    "appearance": "**①近い遠さ**——**細かく割れた水面であり、動いている。****速く流れ、"
                  "この1本の手前にある。**／ **②遠い遠さ**——**水平線であり、動かない。**"
                  "**どこまでも続き、着かない。** ⚠️ **二つのあいだに、線も、色の差も、段も無い**"
                  "——**同じ一つの水であり、同じ一つの光である。**",
    "behavior": "**近い側は流れ続け、遠い側は動かない。** ⚠️ **それが二つを区別する唯一のものである。** "
                "**カメラが引けば、二つとも同時に遠くなる**（`motion.quality` の逐語:「引くほど、"
                "二つとも遠くなる」）。⚠️ **この1本のあいだ、どちらも着かない。**",
    "continuity": "**Must preserve** — **同じ一つの水であること**、**同じ一つの光であること**、"
                  "**同じ一つのグレードであること**、**二つのあいだに分割線を引かないこと**、"
                  "**近い側だけが動くこと**、そして**どちらも着かないこと。** "
                  "**May change** — 水面の細かさ、反射の道の位置、水平線の画面の中の高さ。",
    "notes": ["⛔ **左右に割らないこと。** ⚠️ **この形式を二画面にすれば、この1本は別の形式になる**"
              "——**カードの `## Negative` の逐語:「no split screen with a dividing line」。**",
              "⛔ **奥行きで並べること。****近い側が手前にあり、遠い側が奥にある**——"
              "**横に並べば、二つの現実ではなくなる。**",
              "⛔ **どちらが `l12` でどちらが `l13` かを、この1本は名指さない**"
              "——**名指せば、それは説明である**（§20 を見る）。"]},
   {"name": "反射の道",
    "ref": "⛔ **これがこの1本の `BEARER` である。** ⚠️ **人は一人も居ないので、"
           "二つの現実の両方に立つものは、これしかない。**",
    "appearance": "**星空の、水面への一本の反射である。****近い水面で細かく割れ、"
                  "割れながら遠くへ続く。** ⚠️ **切れずに、近い側から水平線の側まで届いている。** "
                  "**この1本でいちばん明るいものである。**",
    "behavior": "**近い水面では速く揺れ、遠い側ではほとんど動かない。** ⚠️ **一つの光が、"
                "二つの遠さの両方に同時に在る**——**ゆえに二つの現実は、主張ではなく、"
                "この一本の線で読める。**",
    "continuity": "**Must preserve** — **一本であること**、**切れないこと**、**近い側と遠い側の"
                  "両方に届いていること**、そして**星の光であること。** "
                  "**May change** — 割れ方、幅、明るさのむら。",
    "notes": ["⛔ **この光は、星のものである。****枠の外の背後から来る光ではない**"
              "——**ゆえに彼女の第四の姿ではない**（`characters.女神.identity` の逐語）。"
              "⚠️ **この区別を書かないと、この1本の bearer は女神になる。**",
              "⛔ **二つ目の光を作らないこと。****この1本の明るいものは、この一本の道だけである。**"]},
   {"name": "人（この枠に居ない者）",
    "ref": "⚠️ **参照集合は `男.identity` と `男.negatives` を挙げる。**",
    "appearance": "⛔ **この1本の枠に入らない。****どの距離にも、どの焦点にも、一人も居ない。** "
                  "⚠️ **舟も無いので、舵を取る者も居ない。**",
    "behavior": "**無い。** ⚠️ **この1本で動くのは、水と、空の星と、カメラの位置だけである。**",
    "continuity": "⛔ **人を一人も入れないこと** — 遠景の点も、影も、映り込みも。 "
                  "⚠️ **入れば、この1本の二つの現実は、誰かの視線になる**"
                  "——**この1本は、誰の位置でもない場所である。**",
    "notes": ["⛔ **この判断の根拠を書く。** 記録の `unit` は「**海と、水平線だけがある。**」であり、"
              "`motion.subject` は「水面、水平線、そしてその上の空。」である——"
              "**どちらも人も舟も名指さない。** ⚠️ **この作品の `unit` は、"
              "小石の一つまで名指す**（`s12` の「海と、手前の砂。」）——**ゆえに、"
              "名指されていない者が居るとは読まない。** **§20 を見る。**",
              "⚠️ **この1本は、同一性の塊を §18 に置かない**（`has_man: False`）——**人物がこの枠に"
              "居ない以上、人物の錠を貼れば、居ない者を貼ることになる**（2026-09-29 の裁定①）。"
              "**§20 を見る。**"]},
 ],

 "environment": {
   "location": "`海` — **夜である。** ⚠️ **この1本は、この場所を離れない。****水は一つであり、"
               "水平線も一つである。** **陸はどの方向にも見えない**（`海.geography` の逐語）"
               "——**ゆえにこの1本の遠い側は、島ではない。**",
   "elements": "**細かく割れた水面**（近景、動いている）、**水平線**（動かない）、**一本の反射の道**、"
               "**その上の空と星。** ⚠️ **舟も、帆も、鳥も、陸も、月も、人も無い。**",
   "behavior": "**水は同じ方向へ流れ続ける。****水平線は一つのところに留まる。** "
               "⚠️ **この1本のあいだ、二つの遠さのどちらも近づかない。** "
               "**カメラが引くので、二つは同時に遠くなる**——**それがこの1本の時間である。**",
 },

 "objects": [
   "**無し。** ⚠️ **この1本の枠に、物は一つも無い。****この作品の小道具4つのうち、"
   "この1本に来るものは無い**（`ledger.props`）——**帆も、斧も、太陽の牛も、筏も無い。**",
   "**反射の道** — ⚠️ **物ではない。****この1本の bearer であり、いちばん明るいものである。**",
   "⚠️ **参照集合は `舟`・`舟.appearance`・`舟.negative` を挙げる。****それでもこの1本の枠に、"
   "筏の一部も入らない**（§20 を見る）。",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****そしてこの1本の画に、彼は居ない。**"
                  "`女神` — ⛔ **この1本に添付しない。****彼女は四つの姿のどれとしても現れない。**"
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.夜`・`舟`・`舟.appearance`・`舟.negative` の8鍵である。"
                  "⚠️ **この集合は `s22` のものと同じである**——**2本目の差分は、"
                  "詞ではなく、カメラの運動と、この1本に人が居ないことで持つ**（§20 を見る）。",
 "ref_extra": [
   "- ⚠️ **形式カード `coexisting-realities` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; "
   "what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §8 に書いた5つの変数、§15 に書いた免除の名指し、そして §16 に運ばれた"
   "カード自身の禁制である。**",
   "- ⚠️ **カードの逐語:「**This card collides with §15 CONTINUITY, and the collision is the card.**」"
   "——**ゆえにこの1本では、§15 の `Spatial` と `Visual` が文法の置き場である。**"
   "**免除の名指しは、そこにしか置けない。**",
   "- ⚠️ **`coexisting-realities` の5つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `REALITIES`＝the realities that stand together — ⛔ **二つである。****①近い側**——"
   "**細かく割れた水面であり、動いている。**／ **②遠い側**——**動かない水平線であり、"
   "どこまでも続く。** ⛔ **どちらも先ではない。****二つは、同じ一つの場所と時刻の中に、"
   "同時に在る。** ⚠️ **どちらが `永遠より遠い` で、どちらが `なんでもない島へ` かを、"
   "この1本は名指さない**——**名指せば、それは説明である。**",
   "  - `BEARER`＝who is in more than one of them — ⛔ **この1本の bearer は、反射の道である。**"
   "⚠️ **この1本には人が一人も居ないので、二つの現実の両方に立つものは光だけである**"
   "——**その一本の道は、近い水面で割れながら、遠い水平線の手前まで切れずに届いている。**"
   "**カードの逐語:「Name a bearer who stands in more than one reality, so the coexistence is visible "
   "rather than asserted.」**——**ゆえにこの1本は、二つの遠さを主張せず、"
   "一本の光の線で立たせる。**",
   "  - `SHARED`＝what belongs to all of them — **水と、光と、グレードと、そして粒である。**"
   "**一つの光源からの一つの反射の道が、近い水面から水平線まで走っている。**"
   "**カードの逐語:「Share something across them — light, sound, a material, a movement — so the "
   "frame reads as one frame.」** ⚠️ **ゆえにこの1本は、二つのあいだに色の差を置かない。**",
   "  - `ORDER`＝how the frame lays them out — ⛔ **奥行きである。****近い側が手前にあり、"
   "遠い側が奥にある**——**横に並ばないし、どちらかが先に来ない。** **この画は一度も切れない**"
   "（カードの `## Negative`）。",
   "  - `DURATION`＝clip length — **`10.931秒` である。** ⚠️ **この作品の尺は曲から来る**"
   "（`bible.song.lines[].at` の差）——**`l12` の 7.021秒と `l13` の 3.910秒の和である。**",
   "- ⛔ **この作品で `coexisting-realities` を使うのは4本である**（`s07`・`s15`・`s22`・`s29`）。"
   "**この1本は2本目である。** ⚠️ **この形式がこの作品で要るのは、まさにこの1本のためである**"
   "（記録のヘッダの逐語）。**それでも、サビの反復の側にもう1本（`s22`）が在る。**",
 ],

 "narrative": {
   "core": "**二つの遠さが、同じ一つの枠に立つ。** どちらも着いていない。",
   "beginning": "**水面と水平線。****遠さが二つある。**",
   "turn": "**近い水面が流れる。** 遠い水平線は動かない。",
   "peak": "**カメラが引ききる。** 二つの遠さが、どちらも遠くなる。",
   "pull": "⚠️ **同じ一枠に並ぶのが、切れ目のコマである。** **この1本は、説明のコマを足さない。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 3.935秒.** 最初の2.995秒は**二つが在ることを立てる**のに"
            "払われ、次の4.001秒は**近い側だけが動くこと**に払われ、**最後の3.935秒がこの1本の出来事である**"
            "——**カメラが引ききり、二つが同じ一枠に並ぶ。** ⚠️ **`held` を1つも使わない。** "
            "⛔ **`様式美` の1本である**——**余白が減っていくのではなく、増えていく。**",

 "actions": [
   ("ACT_TWO", "水面と水平線がある。**遠さが二つある。**",
    "**二つの遠さが、それぞれの速さで動きはじめる**——**近い側は流れ、遠い側は留まる。**"),
   ("ACT_FLOW", "近い水面が流れている。**遠い水平線は動かない。**",
    "**カメラが後ろへ引きはじめる**——**二つとも遠くなりはじめる。**"),
   ("ACT_PULL", "カメラが引いている。",
    "**カメラが引ききる**——**二つの遠さが、どちらも遠くなる。**"),
   ("ACT_STAND", "二つとも遠い。",
    "**同じ一枠に並ぶのが、切れ目のコマである**——**どちらも着いていない。**"),
 ],

 "camera": {
   "language": "Third person, **low, at the water's own level, and behind the near water**——"
               "**この1本は、誰の位置でもない。** ⚠️ **この1本は、二つの遠さのどちらにも属さない"
               "場所から、二つを一つの枠に入れる。**",
   "events": "One event only. `0-2.995s` — **the frame holds the water and the horizon and does not yet "
             "move**; then `2.995-6.996s` — **the near water runs and the far horizon does not, and the "
             "camera begins to pull back**; then `6.996-10.931s` — **the camera finishes its pull and "
             "both distances are farther.** ⚠️ **動機は「二つを同じ枠に留めること」である**"
             "——**引くことが、二つを一つの画にする。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the pull-back** "
               "—— ⚠️ **この1本の移動は、後ろへの一様な引きである。****引きは一様であり、"
               "重さを持つ。** **No crane. No Steadicam. No dolly-in** — **この1本は前へ出ない。** "
               "**No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、二つの遠さが同時に遠くなることである。****近い水面は速く流れ、"
              "遠い水平線は動かない。****そしてカメラが引く。**",
   "object": "**動く物は無い。****この1本に物は一つも置かれていない。**",
   "environment": "**水が同じ方向へ流れ続ける。****水平線は一つのところに留まる。** "
                  "**星は動かない**——**この1本の空は、この10.931秒では動かない。** "
                  "⚠️ **動くのは、水と、カメラの位置だけである。**",
   "weight": "**水の重さは、流れの一様さで出る。****水平線の重さは、動かないことで出る。** "
             "⚠️ **速いものは一つも無い。**",
   "inertia": "**一度引きはじめたカメラは、とまらない。****流れは、この1本のあいだ止まらない。** "
              "⚠️ **最後のコマでも、近い水面は流れている。**",
   "acceleration": "**加速しない。****引きも、流れも、一様である。** "
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この10.931秒の全コマで、"
               "近い水面は動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**二つが並ぶことは、"
             "事件ではなく、構図である。**",
 },

 "emotion": {
   "arc": "**二つの行き先が、どちらも遠い。****矛盾したまま、同じ一つの枠にある。** "
          "⛔ **この1本は、それを説明しない。****ゆえに感情は、解決ではなく、"
          "「両方が同時に在る」ことの側にある。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****カメラが引ききることである。** "
             "**誰も写さないのに、遠さだけが残る。**",
 },

 "lighting": {
   "base": "**夜である。****光源は星と、その水面の反射だけである。****波は黒く、反射の道だけが白い**"
           "（`ledger.locations.海.states.夜` の逐語）。⚠️ **月も、火も、灯も無い。** "
           "⚠️ **空もまた暗く、星だけが粒として在る。**",
   "events": "**One, and it runs the whole shot.** **一本の反射の道が、近い水面で細かく割れ、"
             "遠くではほとんど動かない。** ⚠️ **光源は動かない。** ⚠️ **様式カードの逐語:"
             "「The grade holds for the whole shot — a colour temperature that swings is a different "
             "style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**低いうねりが進む音。****水面が細かく崩れる音。****弱い風。** "
          "⚠️ **この1本に人の音は一つも無い。** ⚠️ **木の音も、縄の音も無い**"
          "——**この1本に筏が無いからである。**",
   "music": K.NO_MUSIC + " ⚠️ **主題歌はこの1本のあいだ鳴っている**（`l12`+`l13`）——**が、"
            "この1本の中には無い。****編集で載る。**",
   "environment": "夜の外海。**水、風、そして遠さ。** ⚠️ **鳥の声も、帆の音も、他の船の音も無い**"
                  "（`海.base` の逐語:「No land, no sail, no bird, no other vessel.」）。",
 },

 "continuity": {
   "identity": "⚠️ **この1本に人が一人も居ないので、人物の同一性は掛からない。** "
               "**掛かるのは水と、光と、空の同一性である**——**同じ一つの水であること、"
               "同じ一つのグレードであること、二つのあいだに分割線を引かないこと。** "
               "⛔ **`男.identity` は参照集合に在るが（§6）、この1本は同一性の塊を §18 に貼らない**"
               "——**貼れば、この枠に居ない者を貼ることになる**（2026-09-29 の裁定①）。"
               "⚠️ **この形式の `BEARER` は光であり、人ではない**（§3 と §6 を見る）。",
   "spatial": "**この1本の枠は `海` の上にあり、夜である。** ⛔ **そしてこの1本は、§15 の免除を求める**"
              "——**形式カードの逐語:「The specification must say what §15 is being asked to exempt — "
              "**the frame's own place and moment** — and must keep exempting only that.」** "
              "⛔ **ゆえに、この1本が §15 に求める免除は、一つだけである**——"
              "**「枠そのものの場所と時刻」。****この枠は、一つの場所と一つの時刻の中に、"
              "二つの行き先を同時に持つ。** ⚠️ **免除を広げない**——**同一性も、水も、光も、色も、"
              "時刻も、グレードも、運動も、免除しない。****それらは一つである。** "
              "⚠️ **カードの `avoid` の逐語:「Exempting all of §15, so nothing in the frame is "
              "continuous」。**",
   "temporal": "**夜である。****`s09`〜`s15` と同じ夜である。** ⛔ **この1本の二つの遠さに、先後は無い**"
               "——**どちらも過去でも未来でもなく、同じ一つの時刻の中にある**"
               "（カードの `## Negative` の逐語:「**no reality declared earlier than another**」）。"
               "⚠️ **画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** ⚠️ **そしてこの1本では、その同一性が免除の境界線である**"
             "——**二つの現実を別のグレードで塗れば、免除が広がりすぎる。** "
             "⛔ **経路について**: **この形式は `WAN 3.0` と `MINIMAX H3` のために書かれている。**"
             "**カードの逐語:「On the `WAN 3.0` route the collision is head-on — one continuous take "
             "cannot hold two places.」** **`MINIMAX H3` では、これは衝突ではない**"
             "——1本が独立したフレームから成るので、**1ショットが複数の場所を持つことは"
             "正規の場合である。** ⚠️ **この作品の経路は `SEEDANCE 2.5` である**"
             "——**切り目の無い1本である**——**ゆえにこの1本は、カード自身が「正面衝突」と"
             "呼ぶ側に立っている。** ⛔ **そしてカードは「**The §18 heading must therefore name "
             "`MINIMAX H3`**」と書く**——**この作品の §18 の見出しは `SEEDANCE 2.5` であり、"
             "それだけである**（34本すべてが同じ見出しである）。**ゆえにこの1本は、"
             "経路の側から救われない。****この1本が払うのは、二つの現実を、一つの場所と"
             "一つの時刻の中の二つの遠さとして置くことである。** ⚠️ **カードの逐語:"
             "「**A layer that saw nothing looks exactly like a layer that passed** — "
             "the specification carries the burden, because no check will.」**",
   "motion": "Full animation, not limited. **近い水面が流れ、反射の道が揺れ、遠い水平線が動かない。** "
             "**カメラはゆっくり後ろへ引き、引ききる。** ⚠️ **この1本のあいだ、"
             "近い水面は一度も止まらない。**",
   "sound": "**水、風。****音楽なし。言葉なし。** ⚠️ **主題歌はこの1本のあいだ鳴っているが、"
            "この1本の中には無い**——**編集で載る。**",
 },

 "must_not": _MN + [
   "**No person in frame at any moment** — no figure at any distance, in any focus, **no one on the "
   "water, no silhouette, no hands, no oar, and no one steering**, and no shadow or reflection of a "
   "person anywhere. ⚠️ **この1本に bearer の体は無い**——**bearer は光である。**",
   "**No vessel of any kind in this frame** — no boat, no ship, no hull, **no raft**, no mast, no oar, "
   "no sail; ⚠️ **この1本の二つの遠さは、何も乗っていない海である**（§20 を見る）。",
   "**No land, no shore, no island, no coastline, no rock standing in the water** — ⚠️ **この1本の"
   "遠い側は、島ではない。****島を置けば、二つの遠さは一つの目的地と一つの目的地になり、"
   "この1本は別の1本になる。**",
   "**No moon, no torch, no lamp, and no path of light other than the one broken reflected path of "
   "the stars** — **二つ目の光源を作らない。** ⚠️ **この光は星のものであり、"
   "枠の外の背後から来る光ではない**（彼女の第四の姿ではない）。",
   "⛔ **No split screen and no dividing line of any kind in this frame** — **no seam down the middle, "
   "no vertical edge, no vignette that separates one side from the other.** **この1本の二つは、"
   "奥行きで並ぶ。**",
   "⛔ **No color grade separating the two distances** — **近い側と遠い側で、色温度も、彩度も、"
   "露出も変えない。****one light and one grade hold across the whole frame.**",
   "**No caption, no title card, no written label anywhere** — **`永遠より遠い` も `なんでもない島へ` "
   "も、画には書かれない。**",
   "**No white water, no breaking crest, no foam and no spray**（`海.base` の逐語:"
   "「Long low swells with no white water」——**この1本に航跡も無い**）。",
   "**No bird**（`海.base` の逐語）。",
   "**No cut to a second setup.** ⚠️ **この1本は1つの画である。**",
   "⚠️ **この1本に男は居ないが、`男.negatives` は参照集合に在る**（§6）——**彼の禁制はこの1本でも"
   "掛かる**（逐語:「no muscular hero's body, no heroic pose, no heroic lighting」・"
   "「no youthful face, no beardless face, no clean or unlined skin」・「no armour, no helmet, "
   "no greaves, no shield」）。⚠️ **ここでは、それが「人を一人も置かないこと」として効く。**",
 ],

 "must": [
   "⛔ **二つの遠さが、同じ一つの枠に立ち、どちらも先ではないこと**（カードの `do` の逐語:"
   "「Lay the realities out in one frame, with none of them earlier than another」）。",
   "⛔ **§15 に求める免除を、名指しすること** — **「枠そのものの場所と時刻」だけであり、"
   "それ以上ではない**（カードの `do` の逐語）。",
   "⛔ **bearer を立てること** — **この1本では、一本の反射の道である**"
   "（カードの `do` の逐語:「Name a bearer who stands in more than one reality, "
   "so the coexistence is visible rather than asserted」）。",
   "⛔ **二つのあいだで何かを共有すること** — **水と、光と、グレードと、粒である**"
   "（カードの `do` の逐語）。",
   "⛔ **この1本がどの経路のために書かれているかを、仕様の中に書くこと**（カードの `do` の逐語:"
   "「say in the specification which route the shot is written for」）——"
   "**この1本は `SEEDANCE 2.5` のために書かれている**（§15）。",
   "⚠️ **同一性の塊を §18 に貼らないこと** — **人物が枠に居ないので、この1本は人物の錠を運ばない**"
   "（`has_man: False`。2026-09-29 の裁定①）。**§20 を見る。**",
   "⚠️ **近い側だけが動くこと** — **遠い側は、この10.931秒のあいだ一度も動かない。**",
   "**星の光だけであること** — **月も、二つ目の光も無い。**",
   "⚠️ **変化は最後のコマで終わる** — **二つが同じ一枠に並んだコマで、この1本は終わる。**",
 ],

 "prefer": "The near water broken into fine facets and running; the far water smooth and "
           "undifferentiated; one unbroken reflected path reaching from the near water out to where the "
           "water ends; **the sky kept as empty as the frame will allow, so that the two distances have "
           "room to stand apart in.**",
 "allow": "A lens flare where the light crosses the frame; a moderate depth of field that lets the far "
          "water and the horizon both go soft; **a pull-back that continues to the last frame.**",

 "priorities": [
   "⛔ **二つの遠さが、同じ一つの枠に、二つとして立つこと** — **そのコマで終わること。**",
   "⛔ **§15 の免除を、枠そのものの場所と時刻に限ること** — **広げない。**",
   "⛔ **奥行きで並べること** — **分割線を引かない。****別のグレードで塗らない。**",
   "⛔ **人が一人も居ないこと** — **bearer は光である。**",
   "⚠️ **同一性の塊を §18 に置かないこと** — **人物が枠に居ないためである**（2026-09-29 の裁定①）。",
   "**近い側だけが動くこと** — **水平線は動かない。**",
   "**星の光だけであること** — **月も、火も、二つ目の光も無い。**",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `coexisting-realities` を名乗る**——**この形式の禁制（`no cut, no dissolve, "
   "no wipe between realities`・`no sequence`・`no split screen with a dividing line` ほか）は "
   "§16 の床に在り、**カード自身の `Negative` も §16 の側から届く。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 10.931-second cinematic take (16:9) of the open sea at night, one clip, one continuous take, one "
   "change: **two distances stand in one frame at once and neither is earlier — the near water runs and "
   "the far horizon does not move, and as the camera pulls back both of them are further away.** "
   "**No land is in this frame at any moment: no island, no shore, no coastline, and no land behind the "
   "camera either.** **Nothing is in this frame but water, one reflected path of starlight, and the sky "
   "over them.**\n\n"
   "**No person is in this frame at any moment, and the frame is not anyone's position — the one "
   "thing that stands in both of the two distances is a single reflected path of light.**\n\n"
   "0-2.995s: **the water and the horizon, and there are two distances in the frame.**\n"
   "2.995-6.996s: **the near water runs; the far horizon does not move.**\n"
   "6.996-10.931s: **the camera finishes its pull-back and both distances are further away — and the "
   "take ends on that frame.**\n\n"
   "**The two are laid out in depth and not side by side**: the near water in front, the far horizon "
   "behind it, **no seam, no dividing line, no vignette and no second grade between them** — one water, "
   "one light, one grade, one grain. **Neither is drawn as the past or the future of the other, and "
   "nothing passes through the frame.** **The night's only light is the stars and their single reflected "
   "path on the water: the waves are black and the reflected path alone is white, and it runs unbroken "
   "from the near water out to where the water ends.** **Long low swells with no white water, the "
   "horizon level and unbroken, no other vessel, no sail, no bird, no moon.** **This is a bronze-age "
   "world: no made thing of any later age stands in this frame.** **This is a Japanese work.** "
   "No subtitles. No BGM.\n"
   "(One continuous take, one change: two destinations in a single frame, neither reached.)"),

 "visual_scene": (
   "Open sea at night, photographed as a film frame and held in depth: **the near water below, broken "
   "into fine facets and running, and above it the far horizon, level and unbroken, and above that the "
   "sky, starred and otherwise empty.** One unbroken reflected path of starlight lies on the water in "
   "white, cut into fine pieces in the near water and almost still where the water goes far. **Between "
   "the two there is no seam, no edge and no second grade** — the same water and the same light "
   "throughout. **No land is anywhere in the frame: no island, no shore, no coastline, no rock standing "
   "in the water. No vessel, no mast, no oar, no sail, no bird and no moon. No figure is in the frame at "
   "any distance or in any focus, and no shadow or reflection of a person falls anywhere in it.**"),

 "visual_meta": (
   "⚠️ **No person is in this frame at any moment — no bearer with a body, no one on the water, no "
   "figure at any distance, in any focus.** "
   + K.VISUAL_META.replace(
     "Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked; ",
     "**no skin and no cloth anywhere in this frame**: ").replace(
     "wet shingle with individual stones",
     "the water's surface broken into fine facets, running").replace(
     "warm ochre where the low sun falls",
     "cold white held in the one unbroken reflected path of the stars") + (
   " ⚠️ **The two distances are laid out in depth and not side by side, with no seam and no dividing "
   "line between them, and no colour temperature separating one from the other**; the far distance is "
   "open water and not an island, and nothing is in the frame but water, that one path of light, and "
   "the sky.")),

 "motion_prompt": (
   "Full animation, not limited. **The near water runs steadily in one direction and is broken into "
   "fine facets; the far horizon does not move at all — it is exactly as far away in the last frame as "
   "in the first, and the camera's pull is what makes it further.** **The reflected path of starlight "
   "wavers and breaks in the near water and lies almost still where the water goes far, and it runs "
   "unbroken from the one to the other.** **The camera pulls back slowly and finishes its pull, and it "
   "does not stop before the last frame.** **Nothing passes through the frame** — **no bird, no vessel, "
   "no weed, and no cloud.** No motion blur smears, no stutter, no floaty weightless motion, "
   "no static frames — **the near water moves in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **low, at the water's own level and behind the near water**, so that the frame belongs "
   "to neither of the two distances and can hold both. One event only: **a slow, even pull-back, "
   "motivated by holding the two distances in one frame — the further it goes, the further both of them "
   "are; it does not stop before the last frame.** ⚠️ **The style permits a dolly, a crane and a "
   "Steadicam, and this shot spends the dolly** — the move is a single backward travel at water level, "
   "and it carries a real rig's even rate. No crane. No Steadicam. **Do not move in, do not rise, do "
   "not descend, and do not hold still.** No handheld, no whip, no shake, no snap zoom, no rack focus, "
   "no unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **low swells moving over the water, the water breaking into "
   "fine pieces, and a little wind** — **and nothing else, because there is no one in this frame and "
   "nothing is on the water.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (coexisting-realities) ／ "
                        "REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②）。"
                        "⛔ **この1本に人は居ないので、同一性の塊は §18 に入らない**（`has_man: False`）"
                        "——**`Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は書かれていない。**"
                        "⚠️ **`男.negatives` は参照集合に在る**——**ゆえに §16 は彼の禁制も運ぶ**（§20 を見る）。"
                        "⚠️ **参照集合の8鍵のうち、この1本の `REALITIES` は `海` の側から立ち、"
                        "`BEARER` は一本の反射の道である。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water ＋ wind ／ no music",
 "unresolved": [
   "✅ **裁定（2026-09-29）: この1本は人物を枠に置かず、同一性の塊も §18 に貼らない**（`has_man: False`）"
   "——**記録の `unit`（「海と、水平線だけがある。」）も `motion.subject` も、人も舟も名指さない。** "
   "⚠️ **この仕様は裁定の前、塊を作品の錠として §18 に置き、その直後の一文で打ち消していた**"
   "——**裁定①が塊を落とした。****ゆえに `{IDENTITY}` は §18 に無い。** "
   "⚠️ **bearer を人ではなく一本の反射の道にした読みは、裁定のあとも変わっていない。** "
   "⚠️ **`男.negatives` は参照集合に在るので、§16 は彼の禁制を運び続ける。**",
   "⚠️ **`s22` との差が何で持つか。** 記録は「この2本は役も形式も同じであり、差は曲の位置だけである」"
   "と書き、`s22` の側に「**それで足りるかが、この1本の問いである**」と在る。"
   "**この仕様は、カメラの運動（この1本は引き、`s22` は三脚で動かない）と、"
   "この1本に人が居ないことで差を持たせた。** ⚠️ **この判断は、記録の側からは読めない。**",
   "⚠️ **どちらが `l12` でどちらが `l13` かを、記録は名指さない。****この仕様は、"
   "近い水面と遠い水平線の二つを二つの遠さとして置き、どちらがどちらの行かは決めない**"
   "——**名指せば、それは説明である。**",
   "⛔ **この1本は `SEEDANCE 2.5` を走る。****カードは `WAN 3.0` と `MINIMAX H3` のために書かれ、"
   "この作品の経路はそのどちらでもない**——**ゆえにこの1本は、カードが「正面衝突」と"
   "呼ぶ側に立っている。** ⛔ **カードは §18 の見出しが `MINIMAX H3` を名乗ることを要求するが、"
   "この作品の見出しは `SEEDANCE 2.5` であり、それだけである**（34本すべてが同じ見出しである）。"
   "⛔ **ゆえにこの1本は、経路の側から救われない**——**この1本が払うのは、"
   "二つの現実を、一つの場所と一つの時刻の中の二つの遠さとして置くことである。**"
   "****それが実際にどう出るかを、私は見ていない。**",
   "⚠️ **2行を束ねた理由は長さである**——`l12` は 7.021秒、`l13` は 3.910秒であり、"
   "**`l13` は下限4秒に満たない**（`s07` の註）。**この束ねが正しいかは、記録の側では決まっている。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **二つが二つとして読めない。** ⚠️ **近い側と遠い側の差が弱ければ、この1本はただの海の画になる**"
   "——**差は、動きの差だけである。**",
   "⛔ **分割される。** ⚠️ **線が一本でも入れば、この1本は別の形式になる**"
   "（カードの `## Negative` の逐語:「no split screen with a dividing line」）。",
   "⛔ **どちらかが島になる。** ⚠️ **遠い側に陸を置けば、二つの遠さは二つの目的地になり、"
   "この1本は「どこかへ着く」の画になる。**",
   "⛔ **人が入る。** ⚠️ **一人でも入れば、bearer が光から人へ移り、`s18` の「初めて」が壊れる。**",
   "**光が二つになる。** ⚠️ **月を置けば、この1本の矛盾は光源の差に解けてしまう。**",
   "**引かない。** ⚠️ **カメラが止まれば、二つの遠さは遠くならず、切れ目のコマが空になる。**",
   "**説明が入る。** ⚠️ **字幕も、題字も、名指しも、この1本の主題を殺す。**",
   "**`様式美` の側に寄りすぎて、動きが消える。** ⚠️ **静止の強度は、"
   "近い水面が動き続けることで出る**——**全コマで水が動いていること。**",
 ],
}

if __name__ == "__main__":
    print("s15 content OK — keys:", len(C))
