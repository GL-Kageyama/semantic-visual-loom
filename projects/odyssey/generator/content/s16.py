# -*- coding: utf-8 -*-
"""odyssey-s16 — transformation — 舟の置き場 / 夜明け / 17.234s. Wood becomes the raft."""
import common as K


_MN = K.must_not_common(has_man=True, goddess_extra=(
    "⚠️ **この1本の彼女は、四つの姿のどれとしても現れない。****記録は、この1本で"
    "彼女を一度も名指さない。** **ここにあるのは、夜明けの浜と、木と、斧と、働く男だけである。** "
    "⚠️ **彼女の姿を、働く者のそばに置かないこと**——**この1本の作業は、彼のものである。**"))
_RAFT = "No boat, no ship, no hull, no keel, no planking, no sail, no raft, and no other vessel."
assert _MN.count(_RAFT) == 1
_MN[_MN.index(_RAFT)] = (
    "No boat, no ship, no hull, no keel, no planking, no sail, no raft, and no other vessel. "
    "⚠️ **この1本の筏は、この禁制の対象ではない**——**禁じられているのは船体・竜骨・肋・甲板張り・"
    "欄であり、この1本の丸太と手縒りの縄ではない**（`props.舟.appearance` の逐語:"
    "「**a raft and not a boat**」）。")


C = {
 "n": "s16",
 "title": "木が、舟になる——17秒の斧",
 "duration": "17.234",
 "format": "transformation",
 "has_man": True,
 "segment": "verse-2-1",

 "band": [
   "『永遠より遠い』 verse-2「舟の置き場」 / 所作 / motion —— 木が、舟になる——17秒の斧",
   "浜に散らばっていた丸太と板が、斧の一撃ごとに組み合わさり、筏になる。",
   "17.234秒を、カメラは作業台の周りを半周する——最後の板が収まるのが、切れ目である。",
   "速くせず、一つずつ起きる——青銅の斧のほかに機構は無く、鋼も鉄も無い。",
 ],
 "header": """# verse-2 / motion / 所作 / transformation
⚠️ **行: `l14` ／ 場所: `舟の置き場` ／ 時刻: `夜明け` ／ 尺: 17.234秒。**
⚠️ **形式（`transformation`）は §6 の `REF_FORMAT` に書く提案である。** ショット記録に `REF_FORMAT` の欄は無い——**形式は仕様の側にある。****ゆえにここに書いた形式は、まだ検査されていない。**
⛔ **この作品で最も長いショットである（17.234秒）。** 出所: 曲の `l14`「木を削って舟にする」——⚠️ **この行は 10.000秒であり、直後に 7.234秒の歌の無い間がある**（148.032–155.266）。**これはこの曲で最も長い、歌の無い間である。** ⚠️ **この1本が吸う**（`ledger.song_coverage` の註を見る）。
⛔ **形式は `transformation`**——**切断も過程も無しに、あるものが別のものになる。** **この作品の2本目の看板である**（1本目は `s03` の `time-fold`）。⚠️ **この形式をこの作品で使うのは3本である**（`s16`・`s17`・`s25`）。**3本は互いに別の仕事をする**——ここは「**木が筏になる**」であり、`s17` は「**布が帆になる**」であり、`s25` は「**人が誰でもない者になる**」である。
⚠️ **7.234秒の歌の無い間について。** `world.rules` の八番——**この作品に音楽は無い**（曲はポストで載る）。**ゆえにこの7秒は、斧の音だけである。** ⛔ **「歌の無い時間は、画面の側が持つ」**——**この1本では、画面が斧の音を持つ。**
⚠️ **節 `verse-2` は43.005秒あり、この曲で最も長い節である**（9節を並べた実測）。
⚠️ **この仕様のショット記録は `shots/odyssey-s16.yaml` である。**""",

 "intent": "One continuous take of one change — **木が、筏になる。** 最初のコマでは**浜に丸太と板が散らばり、まだ何も無い。** 最後のコマでは**筏がある**——**最後の板が収まるのが、切れ目のコマである。** ⛔ **切らない。繋がない。過程を説明しない。****この17.234秒は、通過そのものに払われる。** ⚠️ **そして、この1本の 10.000秒で歌が終わり、そこから 7.234秒、歌が無い**——**その7秒を、画面は斧の音だけで持つ。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、木が筏になるまでを写す。****切断も、繋ぎも、説明も無しに。** "
   "**二つの状態は、同じ一つの subject の、別の時刻である**（カードの逐語:「The two states are the "
   "same subject at different moments」）。"
   "⛔ **そしてこの1本は、この作品でいちばん長い。****17.234秒である。** "
   "⚠️ **長さは従属変数である**（`CLAUDE.md`「**The shot is the unit.**」）——"
   "**この1本が長いのは、曲の `l14` と、そのあとの 7.234秒の歌の無い間を、"
   "この1本が吸うからである。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本に返事は無い。****島は画面に無い。** **この場所は浜であり、"
               "海は水際の二歩先にある**（`舟の置き場.geography` の逐語）。"
               "**島が応えるのは `s20` である。**",
     "goddess": "⚠️ **この1本に彼女の姿は無い。****四つの姿のどれとしても、記録は名指さない。** "
                "**ゆえにこの仕様は、彼女を一度も置かない。**"
                "**この1本の音は、斧と、木と、浜の水だけである。**",
     "name": "⚠️ **この1本には歌がある**——`l14` である。**名はどこにも無い。**"
             "**そして 10.000秒以降、歌も無い。**",
     "bow": "⛔ **この1本の道具は斧である。****弓ではない。** "
            "⚠️ **そして斧は武器ではない**（`斧.negative` の逐語:「no axe held as a weapon」）"
            "——**この1本の斧は、木にしか入らない。**",
     "places": "この1本が置くのは一つ——`舟の置き場`、**夜明けである。** "
               "⚠️ **`舟の置き場.geography` の逐語:「the right-hand end of the shore, "
               "the waterline two paces from the work」**——**この1本は、その作業場である。**",
     "japanese": "⚠️ **この1本には歌がある**——`l14`「木を削って舟にする」である。"
                 "**画面の中の声ではない。****歌はポストで載る。****そして 10.000秒で、歌は終わる。**",
   },
   extra=[
     "⛔ **変わるのは、木だけである。****一人の subject が、この1本のあいだ、subject のままである**"
     "——**カードの `do` の逐語:「State what must stay recognisable, so the change reads as continuity "
     "and not as a substitution」。**",
     "⛔ **7.234秒の歌の無い間を、画面が持つ。****音楽は無く、斧の音だけが続く。**"
     "**この7秒は、この曲で最も長い、歌の無い間である。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "The right-hand end of a bronze-age island shore just before sunrise, photographed as a film frame: "
     "**unseasoned pine logs and hewn planks scattered on the sand and across low driftwood trestles, "
     "shavings underfoot and never swept, cordage coiled where it was dropped**, and the waterline two "
     "paces from the work. ⚠️ **A half-built thing is on the ground and is not yet a raft.** "
     "⚠️ **No building, no shelter, no jetty, no wall, no fire, and no tool other than the bronze axe**"
     "（`舟の置き場.base` の逐語）。 ⚠️ **No marble, no columns, no architecture of any later age.**",
   "Color Language":
     "A narrow, graded palette before the sun — **grey-blue sky moving toward white, dark sand, pale raw "
     "pine, and the patinated green-black of bronze** — with one thing brightening before anything else: "
     "**the shavings' white**（`舟の置き場.states.夜明け` の逐語:「only the shavings' white brightens "
     "first」）。 ⚠️ **The sea beyond stays dark**（同じ註）。 "
     "⚠️ **Nothing is lit from a low sun**——**この時刻に、太陽はまだ出ていない。**",
   "Texture":
     "Coarse dark sand, wet shingle, driftwood grey and dry, **raw unseasoned pine with the saw's and "
     "the axe's marks still pale and open**, **shavings curled and light**, **coarse hand-twisted "
     "cordage**, and **bronze dull in the hollows with only the ground edges bright.** "
     "⚠️ **No steel, no iron, no polished or mirror surface anywhere.** Film grain present and even.",
   "Visual Density":
     "**High, and it stays high.** ⚠️ **この1本は `所作` である**——**手と、道具と、材と、"
     "削り屑が、同じ枠に同時にある。** **動くほど、画の側も密になる。**",
   "Atmosphere": "The hour before the sun, in which a thing on the ground becomes another thing.",
   "Time": "`夜明け` — **空が青から灰白へ移る30分であり、海はまだ暗い**"
           "（`舟の置き場.states.夜明け` の逐語）。"
           "⚠️ **影が無い**——**この時刻には、まだ落ち影が付かない。** "
           "**いちばん先に明るくなるのは、削り屑の白である。** "
           "⚠️ **この作品は話を進めない**——**ゆえにこの夜明けと、`s13`〜`s15` の夜とのあいだに、"
           "順序を読まない。**",
 }),

 "subjects": [
   dict(K.man_subject(
     behavior="⛔ **この1本は、彼の所作である。****彼は材の前に屈み、両手で斧を持つ。** "
              "**斧が入るたびに、木が変わる**（`motion.quality` の逐語）。"
              "⚠️ **速くしない。****一つずつ起きる**——**削り屑が舞い、板が一本外れ、"
              "丸太が組み合わさり、縄が結ばれ、最後の板が収まる。** "
              "**彼は振り向かないし、レンズを見ないし、口を開かない。** "
              "⚠️ **屈んでいるので、この1本に顔はほとんど入らない**——**入るのは、手と、腕と、"
              "肩と、道具である**（§20 を見る）。",
     may="屈みの深さ、手の位置、斧を振る角度、作業台に対する体の向き、"
         "そして最後の板を収めるときの上体の起こし方。",
     extra_notes=["⛔ **この1本の主役は彼ではなく、変わるものである。****彼は、変える者である。**",
                  "⚠️ **彼は一人である。****この1本に、二つ目の体を置かない。**"]),
   ),
   {"name": "木",
    "ref": "⛔ **これがこの1本の `FROM` であり `TO` であり `KEEP` である。****参照は `舟`・"
           "`舟.appearance`・`舟.negative` と、`舟の置き場` の `base` である。**",
    "appearance": "**①最初**——**皮の付いたままの未乾燥の松の丸太と、削った板が、"
                  "浜に散らばっている。****まだ何も無い。**／ **②最後**——**同じ木が組み合わさり、"
                  "手縒りの粗い縄で縛られ、板が渡され、低い作業台になっている。** "
                  "⛔ **木は木のままであり、もう木ではない**（ビート4の逐語）。"
                  "**皮も、木目も、削り跡も、削り屑も、そのまま残っている。**",
    "behavior": "**斧が入るたびに、木が変わる。****削り屑が舞い、板が一本外れ、丸太が組み合わさり、"
                "縄が結ばれ、最後の板が収まる。** ⚠️ **速くしない。****一つずつ起きる。**",
    "continuity": "**Must preserve** — **木であること**（皮、木目、削り跡、削り屑）、"
                  "**手縒りの縄であること**、**低いこと**、そして**竜骨も肋も甲板張りも欄も無いこと。** "
                  "**May change** — 材の配置、組み上がりの度合い、削り屑の量、縄の結び目の数。",
    "notes": ["⛔ **カードの `do` の逐語:「One change, one subject. The subject of the change stays "
              "the subject all the way through — that is what `KEEP` is for.」**——**ゆえにこの1本は、"
              "丸太と筏を二つの subject にしない。**",
              "⛔ **`props.舟.negative` の逐語:「no sail already raised on the raft before the sail "
              "exists」**——**この1本の筏に、帆は張られない。****帆は `s17` の仕事である。**"]},
   {"name": "斧",
    "ref": "⚠️ **参照は `斧.appearance`・`斧.negative` である。**",
    "appearance": "**青銅の両刃の斧である。****対をなす二枚の三日月の刃が、緑青を吹いた青銅で、"
                  "反りのある乾いたオリーヴの柄に付いている。****柄は手の脂で暗い。**"
                  "**窪みは鈍い緑黒であり、明るいのは二つの研いだ刃の側だけである。**"
                  "**頭は、乾いて固くなった濡れ革で縛ってある。**"
                  "⚠️ **楔の跡と、打たれた跡のある、働く道具である。**",
    "behavior": "**振り上げられ、木に入り、また振り上げられる。**⚠️ **この1本のあいだ、"
                "刃は木から離れても、決して人へ向かない。** **この1本のリズムは、この斧が作る。**",
    "continuity": "**Must preserve** — **両刃であること**、**青銅であること**、"
                  "**オリーヴの柄と革の縛りであること**、**刃の側だけが明るいこと。** "
                  "**May change** — 振りの角度、削り屑の舞い方、木に残る跡。",
    "notes": ["⛔ **`斧.negative` の逐語:「no steel, no iron, no mirror finish」、「no single-bit axe, "
              "no hatchet, no saw, no chisel, no other tool」、「no axe held as a weapon」**"
              "——**この1本で、この3つが効く。**",
              "⚠️ **この1本に、斧以外の道具を置かない。****鑿も、鋸も、槌も無い。**"]},
 ],

 "environment": {
   "location": "`舟の置き場` — **夜明けである。****島の浜の、右の端である。****水際は、"
               "作業場から二歩である**（`舟の置き場.geography` の逐語）。"
               "⚠️ **この1本は、この作業場を離れない。**",
   "elements": "**散らばった丸太と板**、**低い流木の台**、**削り屑**（掃かれない）、"
               "**手縒りの縄**、**青銅の斧**、**粗い暗い砂と濡れた小石**、"
               "**水際の低い濡れた岩**、**まだ暗い海。** "
               "⚠️ **建物も、小屋も、桟橋も、壁も、火も無い**（`舟の置き場.base` の逐語）。"
               "⚠️ **この場所には、石で重しをしたまま張っていない帆がある**（同 `base`）"
               "——**この1本では、触られず、張られず、この1本の対象でもない。****帆は `s17` で"
               "初めて張られる。**",
   "behavior": "**海はまだ暗く、空だけが青から灰白へ移っていく。****影は付かない**"
               "（`舟の置き場.states.夜明け` の逐語:「no shadows」）。"
               "**いちばん先に明るくなるのは、削り屑の白である。** "
               "⚠️ **この1本のあいだ、作業は止まらない。**",
 },

 "objects": [
   "**丸太** — **皮の付いたままの、未乾燥の松である。** **斧で削られ、削り屑になり、"
   "やがて筏の一部になる。**",
   "**板** — **削った板である。****面を合わせずに渡される。****一本が外れ、最後の一本が収まる。**",
   "**削り屑** — **舞い、落ち、掃かれない。****この1本でいちばん先に明るくなるものである。**",
   "**手縒りの縄** — **粗い、手で縒った縄である。****丸太を縛る。****金属の留め具も、"
   "釘も無い**（`舟.negative` の逐語）。",
   "**斧** — **青銅の両刃である**（§3 を見る）。**この1本の道具はこれ一つである。**",
   "⚠️ **この作品の小道具4つのうち、この1本に来るのは斧である。****帆は張られず、"
   "太陽の牛はこの作品の別の場所である**（`ledger.props`）。",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — ⛔ **この1本に添付しない。****記録は、この1本で彼女を名指さない。**"
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`舟の置き場`・"
                  "`舟の置き場.geography`・`舟の置き場.states.夜明け`・`舟`・`舟.appearance`・"
                  "`舟.negative`・`斧`・`斧.appearance`・`斧.negative` の11鍵である。"
                  "⚠️ **この1本の参照集合は、この作品でいちばん多い**——**それだけ、"
                  "文が持たねばならないものが多い。**",
 "ref_extra": [
   "- ⚠️ **形式カード `transformation` の文法は「`video-spec` に一つの文法を足したもの」である**"
   "（逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly as that card requires; "
   "what follows is only what this grammar adds to it.」）。**ゆえに §1–20 の骨格は `s01` と同じであり、"
   "違うのは §8 に書いた5つの変数、§9 の `ACTION`、そして §16 に運ばれたカード自身の禁制である。**",
   "- ⚠️ **カードの逐語:「**Its grammar is written into the `video-spec` skeleton — §9 ACTION and "
   "§11 MOTION** — and the card does not replace that one」。**——ゆえにこの1本の文法の置き場は "
   "§9 と §11 である。**",
   "- ⚠️ **`transformation` の5つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `FROM`＝the substance, figure or place as the shot opens — ⛔ **浜に散らばった、"
   "皮付きの未乾燥の丸太と、削った板である。****まだ何も無い**（ビート1の逐語）。"
   "**この1本は、状態から始まらない**——**まだ筏が無いところから始まる。**",
   "  - `TO`＝what it becomes — ⛔ **筏である。****船ではない**（`舟.appearance` の逐語:"
   "「**a raft and not a boat**」）。**低い、丸太と板の面であり、縁では水に洗われる。**",
   "  - `TRIGGER`＝the event the change starts from — ⛔ **斧の一撃目である**（ビート2の逐語:"
   "「斧の一撃目が入る。」）。⚠️ **カードの `do` の逐語:「Give the change a trigger, or state that it "
   "has none — do not leave the moment it starts to chance」。****ゆえにこの1本は、"
   "変わりはじめる瞬間を最初の一撃に固定する。**",
   "  - `KEEP`＝what must stay recognisable across the change — ⛔ **木である。**"
   "**皮、木目、削り跡、削り屑、そして手縒りの縄**——**すべてのコマで、"
   "それが木であることが読める。** ⚠️ **ビート4の逐語:「木は木のままであり、**もう木ではない**」。**",
   "  - `DURATION`＝clip length — **`17.234秒` である。** ⚠️ **この作品で最も長い。**"
   "**内訳は `l14` の 10.000秒と、直後の 7.234秒の歌の無い間である**"
   "（`ledger.song_coverage` の逐語）。",
   "- ⛔ **カードの `do` の逐語:「Spend the shot's seconds on the passage, not on the two states」"
   "、「Let the change finish inside the clip」**——**ゆえにこの1本は、"
   "最初の3.998秒で材を並べ終え、最後の板が収まったところで終わる。****戻らない。**",
   "- ⛔ **この作品で `transformation` を使うのは3本である**（`s16`・`s17`・`s25`）。"
   "**この1本は1本目であり、「木が筏になる」である。**",
 ],

 "narrative": {
   "core": "**木が、筏になる。** 一つの画の中で、そうなっている。",
   "beginning": "**浜と、散らばった材木。****まだ何も無い。**",
   "turn": "**斧の一撃目が入る。** 削り屑が舞う。**板が一本、外れる。**",
   "peak": "**丸太が組み合わさり、縄が結ばれる。****ここから 7.234秒、歌は無い。**",
   "pull": "⚠️ **最後の板が収まるのが、切れ目のコマである。** **木は木のままであり、もう木ではない。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and it stays high to the end.** ⚠️ **4つのビートの実測は、"
            "3.998秒・4.998秒・3.998秒・4.240秒である**——**いちばん長いのは第2のビートであり、"
            "斧の一撃目がそこにある。** **最初の3.998秒は材を並べるのに払われ、"
            "最後の4.240秒は最後の板に払われる。** ⚠️ **`held` を1つも使わない。** "
            "⛔ **`dense` が2つ続く**（第3と第4）——**歌の無い7.234秒が、そこに掛かる。**",

 "actions": [
   ("ACT_SCATTER", "浜と、散らばった材木がある。**まだ何も無い。**",
    "**彼が材の前に屈む**——**丸太と、板と、縄が、手の届くところに来る。**"),
   ("ACT_FIRST", "彼は屈み、斧を構えている。",
    "**斧の一撃目が入る**——**削り屑が舞い、板が一本、外れる。**"),
   ("ACT_JOIN", "板が一本、外れている。",
    "**丸太が組み合わさり、縄が結ばれる**——⚠️ **ここから 7.234秒、歌は無い。**"),
   ("ACT_CLOSE", "丸太が組み合わさり、縄が結ばれている。",
    "**最後の板が収まる**——**木は木のままであり、もう木ではない。**"),
 ],

 "camera": {
   "language": "Third person, **low, at the height of the work and the worker's hands**, moving with him "
               "around the workbench. ⚠️ **この高さは、この1本の所作の高さである**——"
               "**切るものと、切られるものが、同じ枠に読める。**",
   "events": "One event only. `0-3.998s` — **the scattered timber and the man coming down to it**; then "
             "`3.998-8.996s` — **the first blow lands, shavings fly, and a plank comes off**; then "
             "`8.996-12.994s` — **the logs come together and the cordage is tied**, ⚠️ **and from here "
             "the song has gone**; then `12.994-17.234s` — **the last plank goes in, and the change is "
             "finished.** ⚠️ **動機は「働く手に留まること」である**——**半周は、"
             "手を追った結果である。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the Steadicam** "
               "—— ⚠️ **この1本の移動は、作業台の周りの半周である。****半周は一様であり、"
               "重さを持つ。** **No crane. No dolly. No second lap** — **この1本は二周しない。** "
               "**No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、木が木のまま筏になっていくことである。****斧が入るたびに、"
              "材の関係が変わる。**",
   "object": "**丸太、板、削り屑、縄、そして斧である。****斧は振り上げられ、入り、また上がる。** "
             "**削り屑は舞い、落ち、積もる。** **縄は締まり、結び目ができる。**",
   "environment": "**海はまだ暗く、空だけが明るくなっていく。****影は付かない。** "
                  "⚠️ **削り屑の白だけが、いちばん先に明るくなる。** "
                  "**水際の波は、この1本のあいだ、同じ速さで寄せている。**",
   "weight": "**この1本の重さは、材の重さである。****丸太は持たれ、板は渡され、斧は落ちる。** "
             "⚠️ **軽く扱われるものは一つも無い**——**彼は、重いものを一つずつ動かす。**",
   "inertia": "**振り上げた斧は、途中で止まらない。****結ばれた縄は、解けない。** "
              "**組み合わされた丸太は、その形のまま残る**——**この1本のあいだ、"
              "戻るものは一つも無い。**",
   "acceleration": "**加速しない。****斧のリズムは一様である。** ⚠️ **この1本に、"
                   "速くなる区間が一つも無い**——**17.234秒を、同じ速さで働く。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この17.234秒の全コマで、"
               "手か、材か、削り屑か、斧が動いている。**",
   "impact": "**静かなものだけである。****斧が木に入るのは、衝撃ではなく、仕事である。** "
             "⚠️ **割れる音は立つが、木は飛び散らない**——**削り屑が舞うだけである。**",
 },

 "emotion": {
   "arc": "**変わっていく。****その17.234秒は、劇的でない時間である。** ⚠️ **この1本の感情は、"
          "「まだ終わっていない」の側にある**——**7.234秒の歌の無い間が、"
          "その感じをいちばん強く持つ。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****最後の板が収まることである。** "
             "**彼は顔を上げない。****それでも、何かが終わったことは、画の側にある。**",
 },

 "lighting": {
   "base": "**夜明けである。****空が青から灰白へ移る30分であり、海はまだ暗い**"
           "（`舟の置き場.states.夜明け` の逐語）。**低い太陽はまだ出ていない。** "
           "⛔ **影が付かない**——**この時刻の光は、まだ落ち影を作らない。** "
           "**青銅は鈍く、柄は暗い。**",
   "events": "**One, and it runs the whole shot.** **削り屑の白が、いちばん先に明るくなる**"
             "（同じ註の逐語）。**この1本のあいだ、その白だけが先に進む。** "
             "⚠️ **様式カードの逐語:「The grade holds for the whole shot — a colour temperature that "
             "swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "⛔ **この1本の音は、斧である。****斧が木に入る音、木が割ける音、削り屑が落ちる音、"
          "縄が締まる音、板が収まる音。****そして浜の水と、弱い風。** "
          "⚠️ **この1本に人の声は一つも無い**——**息も、掛け声も、歌も無い。** "
          "⛔ **10.000秒で歌が終わり、そこから 7.234秒、斧の音だけが続く。**",
   "music": K.NO_MUSIC + " ⛔ **主題歌はこの1本の 10.000秒で終わる**（`l14`）——**そのあとの "
            "7.234秒は、この曲で最も長い、歌の無い間である。****この1本は、"
            "それを画面の側で持つ。**",
   "environment": "夜明けの浜。**水、風、木、青銅。** ⚠️ **鳥の声も、他の船の音も無い**"
                  "（`海.base` の逐語）。⚠️ **この1本に音楽は無い**——**歌はポストで載る。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="**この1本は彼を写す。****ゆえに塊は、この1本では枠の中身でもある。**"
                "⛔ **そしてこの1本は、彼の手を写す**——**手は塊の一部である。**"
                "⚠️ **彼を二度写さないこと。****一人の体が、一つの枠に一つだけ在る。**",
     may="屈みの深さ、手の位置、斧を振る角度、作業台に対する体の向き、"
         "そして最後の板を収めるときの上体の起こし方。"),
   "spatial": "**この1本の枠は `舟の置き場` にあり、夜明けである。****水際は、作業場から二歩である**"
              "（`舟の置き場.geography` の逐語）。"
              "⚠️ **この1本は `transformation` を名乗り、この形式は §15 から何も免除しない**"
              "——**免除を名乗るのは、`coexisting-realities` を名乗る4本だけである。**"
              "**この1本の場所と時刻は、台帳の `舟の置き場`／`夜明け` のままである。**",
   "temporal": "**夜明けである。****この作品は話を進めない**（§2 の逐語:「the work does not advance "
               "a story」）——**`l11`（`s14`）で筏は海の上にあり、`l14`（この1本）で筏が作られる。**"
               "⚠️ **順序を読まない。****画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** ⚠️ **これはこの作品で最も長い1本であり、"
             "ゆえにグレードの保持がいちばん長く試される1本である。**",
   "motion": "Full animation, not limited. **斧が振られ、木が変わり、縄が結ばれ、板が収まる。** "
             "**カメラは半周する。** ⚠️ **この1本のあいだ、手は一度も止まらない。**",
   "sound": "**斧、木、縄、板、浜の水、風。****音楽なし。言葉なし。** "
            "⛔ **10.000秒から先は、斧の音だけである。**",
 },

 "must_not": _MN + [
   "**No cut, no dissolve, no wipe between the two states** — **この1本は一つの画である**"
   "（カードの `## Negative` の逐語:「no cut, no dissolve, no wipe」）。",
   "**No stated process and no intermediate stage held for the viewer** — **途中の段を、"
   "観客のために止めない。** **この1本のビートは、通過そのものである**"
   "（カードの `## Negative` の逐語:「no stated process, no intermediate stage held」）。",
   "**No caption, no title card, no voice-over and no date stamp naming the change**"
   "（カードの `## Negative` の逐語）。",
   "**No second simultaneous transformation** — ⚠️ **変わるのは木だけである。****働く男は変わらない。**"
   "**削り屑も、縄も、変わらない。**",
   "**No steel, no iron, no mirror finish on the axe; no single-bit axe, no hatchet, no saw, no chisel, "
   "and no other tool**（`斧.negative` の逐語）。",
   "**No axe held as a weapon** — ⛔ **この1本のあいだ、刃は決して人へ向かない**"
   "（`斧.negative` の逐語）。",
   "**No metal fastening, no nail, no rope that is not hand-twisted**（`舟.negative` の逐語）。",
   "**No boat, no ship, no hull, no keel, no ribs, no planking and no gunwale**"
   "（`舟.negative` の逐語）——**この1本に完成した船は無い。****できあがるのは低い筏である。**",
   "**No sail raised, and no sail touched in this frame**（`舟.negative` の逐語:「no sail already "
   "raised on the raft before the sail exists」——**帆は `s17` で初めて張られる**）。",
   "**No building, no shelter, no fire, no jetty, no wall and no stair in this frame**"
   "（`舟の置き場.base` の逐語）。",
   "**No second person in frame at all** — no companion, no crowd, **no other worker.** "
   "⚠️ **この1本の作業は、一人で行われる。**",
   "**No cut to a second setup.** ⚠️ **この1本は1つの画である。**",
 ],

 "must": [
   "**木が筏になる** — **切断も、繋ぎも、説明も無しに。**"
   "**最後の板が収まるのが、切れ目のコマである。**",
   "⛔ **一つの subject が、最初から最後まで subject のままであること**"
   "（カードの `do` の逐語:「One change, one subject.」）。",
   "⛔ **変わりはじめる瞬間を、斧の一撃目に固定すること**（カードの `do` の逐語）。",
   "**The identity block pasted into §18 is preserved clause by clause** — build, skin, hair, beard, "
   "face, the scars, **the one garment he wears and everything he does not wear**, and **that he is "
   "barefoot.**",
   "⛔ **7.234秒の歌の無い間を、斧の音だけで持つこと** — **画面の側が、その7秒を持つ。**",
   "⚠️ **変わるのは木だけであること** — **彼も、削り屑も、縄も変わらない。**",
   "**斧は青銅の両刃であり、武器ではないこと** — **刃は木にしか入らない。**",
   "⚠️ **変化は最後のコマで終わる** — **最後の板が収まったコマで、この1本は終わる。**",
 ],

 "prefer": "Raw unseasoned pine with the axe's marks still pale and open; shavings curling and falling "
           "and never being swept; cordage visibly hand-twisted and pulled tight knot by knot; "
           "**the shavings' white brightening before anything else in the frame.**",
 "allow": "A lens flare where the light crosses the frame; a moderate depth of field that lets the far "
          "shore go soft; **the camera's half turn finishing with the last plank.**",

 "priorities": [
   "**木が筏になること** — **一つの画の中で、切らずに。** **最後の板のコマで終わること。**",
   "⛔ **一つの subject のままであること** — **木が、木のまま、筏になる。**",
   "⛔ **7.234秒の歌の無い間を、画面が持つこと** — **斧の音だけが続く。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "⛔ **彼は一人であること** — **二つ目の体を置かない。**",
   "**斧は青銅の両刃であり、武器ではないこと。**",
   "**影が付かない時刻であること** — **夜明けの、落ち影の無い光。**",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `transformation` を名乗る**——**この形式の禁制（`no cut, no dissolve, no wipe`・"
   "`no stated process`・`no intermediate stage held`・`no second simultaneous transformation` ほか）は "
   "§16 の床に在り、**カード自身の `Negative` も §16 の側から届く。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 17.234-second cinematic take (16:9) of a bronze-age island shore just before sunrise, one clip, "
   "one continuous take, one change: **wood becomes the raft — not cut to it, not dissolved into it, and "
   "with no stage held to explain it. The two states are the same subject at different moments, and the "
   "subject is the wood.**\n\n"
   "**The identity lock of this work, carried here for continuity: "
   "{IDENTITY}** **In this shot he is the one who works: he is bent over the timber with both hands on "
   "the axe, and he does not raise his face to the camera, does not look at the lens and does not "
   "speak.**\n\n"
   "0-3.998s: **the shore and the scattered timber — logs and planks on the sand — and nothing is built "
   "yet.**\n"
   "3.998-8.996s: **the first blow of the axe lands; shavings fly; one plank comes off.**\n"
   "8.996-12.994s: **the logs come together and the cordage is tied — and from this point the song has "
   "gone, and the axe is the only sound there is.**\n"
   "12.994-17.234s: **the last plank goes in — the wood is still wood and is no longer wood, and the "
   "take ends on that frame.**\n\n"
   "**The axe is a bronze double-axe**: two symmetrical crescent blades of patinated bronze on a bowed "
   "seasoned olive haft dark with handling, dull green-black in the hollows and bright only along the "
   "two ground edges, the head lashed with dried-hard wet leather — **a working tool, and never raised "
   "against a person.** **No steel, no iron, no saw, no chisel, no other tool is in this frame.** "
   "**The wood stays wood all the way through: bark on the logs, open pale axe marks, shavings falling "
   "and never swept, coarse hand-twisted cordage, no metal fastening and no nail.** **What is built is "
   "a raft and not a boat: no hull, no keel, no ribs, no planking, no gunwale, and no sail bent to "
   "anything.** **Before sunrise, with no shadows and the sea still dark, and the shavings' white the "
   "first thing to brighten.** **The shore is the right-hand end of the island's shore, the waterline "
   "two paces from the work, with no building, no shelter, no jetty and no fire.** **This is a "
   "bronze-age world and there is no music in this shot.** **This is a Japanese work.** **No subtitles, "
   "and no BGM — from 10.000 seconds the song has stopped and the axe is the only sound.**\n"
   "(One continuous take, one change: wood becomes the raft.)"),

 "visual_scene": (
   "The right-hand end of a bronze-age island shore just before sunrise, photographed as a film frame: "
   "coarse dark sand and wet shingle, unseasoned pine logs and hewn planks scattered across low "
   "driftwood trestles, **shavings curled underfoot and never swept**, coarse hand-twisted cordage "
   "coiled where it was dropped, and the waterline two paces away with the sea still dark beyond. "
   "**The man is bent over the timber with both hands on a bronze double-axe** — two symmetrical "
   "crescent blades of patinated bronze on a bowed olive haft, dull green-black in the hollows and "
   "bright only along the two ground edges, lashed with dried-hard leather — **his face is mostly out "
   "of the frame because he is bent to the work, and what the frame holds is his hands, his arms, his "
   "shoulders and the tool.** **The wood is still wood: bark, open pale axe marks, and shavings in the "
   "air.** **No building, no shelter, no jetty, no fire and no other tool; no boat, no hull, no keel, "
   "no planking, no gunwale and no sail.** **No second person is in the frame at any distance.**"),

 "visual_meta": K.VISUAL_META.replace(
   "wet shingle with individual stones",
   "curled pine shavings over coarse dark sand and wet shingle").replace(
   "warm ochre where the low sun falls",
   "the shavings' white brightening first, before anything else in the frame") + (
   " ⚠️ **The identity block above is the man bent over the timber: the frame holds his hands, his arms "
   "and his shoulders, and he does not raise his face to the camera.** ⚠️ **The axe is bronze and a "
   "working tool**; there is no steel, no iron and no other tool in the frame, and the wood stays wood — "
   "bark, pale axe marks and shavings — **so that what is built reads as the same material at a later "
   "moment.** ⚠️ **No sail is raised or touched in this frame.**"),

 "motion_prompt": (
   "Full animation, not limited. **The axe is raised, driven into the wood, and raised again; each blow "
   "changes the timber.** **Shavings curl up and fall and gather and are never swept.** **One plank "
   "comes off; the logs come together; the cordage is pulled tight knot by knot; the last plank goes "
   "in and stays.** ⚠️ **Nothing is fast — one thing happens at a time, and each thing finishes before "
   "the next begins.** **The sea stays dark and the sky moves from blue toward grey-white; no shadows "
   "are cast; the shavings' white brightens before anything else.** **The camera makes one half turn "
   "around the work and does not repeat it.** No motion blur smears, no stutter, no floaty weightless "
   "motion, no static frames — **the hands move in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **low, at the height of the worker's hands**, moving with him around the workbench. "
   "One event only: **a single half turn around the work, motivated by staying with the hands that are "
   "changing the wood; it begins as he comes down to the timber and finishes as the last plank goes in.** "
   "⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot spends the Steadicam** — the "
   "move is a single arc at the height of the work, and it carries a real rig's even rate. No crane. "
   "No dolly. **Do not make a second lap and do not move again after the plank is in.** No handheld, "
   "no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **the axe entering wood, wood splitting, shavings falling, "
   "cordage pulled tight, a plank settling into place, the water at the shore and a little wind** — "
   "**and no human voice at all: no breath, no effort, no song.** ⛔ **The song stops at 10.000 seconds "
   "into this shot and 7.234 seconds of it have no song: the axe alone carries them.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (transformation) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ**"
                        "——**この1本は彼を写すので、塊は枠の中身でもある。**"
                        "⚠️ **参照集合の11鍵のうち、この1本の `FROM`／`TO`／`KEEP` は `舟` の側から立ち、"
                        "`TRIGGER` は斧の一撃目である。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ axe ＋ wood ＋ cordage ＋ shore water ＋ wind ／ no music, and no song "
                 "after 10.000s",
 "unresolved": [
   "⚠️ **彼の顔がどこまで枠に入るかを、記録は書かない。** 記録の `motion.subject` は「丸太、板、"
   "鉋屑、縄。**そして男の手と斧。**」である——**手と道具だけを名指す。** ⚠️ **この仕様は、"
   "「屈んでいるので顔はほとんど入らない」と読んだ**——**儀礼としてであり、"
   "顔を隠すためではない**（裁定②により、顔は塊の英文だけが守る）。"
   "⚠️ **顔を正面から写す読みも成り立つ。****どちらが正かは著者が決める。**",
   "⚠️ **歌の終わりを、記録はビート3の頭（8.996秒）に置いているように読める**"
   "——**ビート3の逐語:「⚠️ ここから 7.234秒、歌は無い。」** ⛔ **しかし実測の和では `l14` は"
   "10.000秒であり、10.000＋7.234＝17.234である。****ゆえにこの仕様は、歌が終わるのを "
   "10.000秒と書いた**（§8 と §14）。**記録の「ここから」の指す位置は、"
   "この1本の中では決まらない。**",
   "⚠️ **この1本に帆が入るかどうかを、記録は書かない。** `舟の置き場.base` は"
   "「石で重しをした、張っていない帆」を持つが、この1本の `objects` は丸太・板・削り屑・縄・"
   "手と斧だけである。⚠️ **この仕様は、帆を場所の一部として認め、"
   "触られず、張られず、この1本の対象でもないと書いた**（§4）。"
   "**§18 の `Visual Prompt` と `must_not` が、それを二重に押さえている。**",
   "⚠️ **`s16` は `transformation` を使う3本の1本目である。****`s17`（布が帆になる）と `s25`"
   "（人が誰でもない者になる）との差は、この仕様からは読めない。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **船ができる。** ⚠️ **竜骨、肋、甲板張り、欄**——**一つでも出れば、この1本はこの作品の嘘になる。**"
   "**できあがるのは、低い筏である。**",
   "⛔ **過程が説明される。** ⚠️ **途中の段を止める、字幕を入れる、語りを載せる**"
   "——**カードが禁じているのは、まさにそれである。**",
   "⛔ **切られる。** ⚠️ **この1本は1つの画である。****切れば、カードの存在理由が消える。**",
   "⛔ **鋼の斧が出る。** ⚠️ **青銅は鈍く、刃の側だけが明るい。****鉄も、鏡面も無い。**",
   "**速くなる。** ⚠️ **巻き戻しのような早回し、あるいは飛躍した組み上がり**——"
   "**一つずつ起きなければ、17.234秒は持たない。**",
   "**7.234秒の歌の無い間が、音で埋まる。** ⚠️ **ここに音楽を置けば、この作品の床が壊れる。**"
   "**持つのは、斧と、水と、風だけである。**",
   "**帆が張られる。** ⚠️ **`s17` の仕事を先に食う。**",
   "**人が二人になる。** ⚠️ **この1本の作業は、一人で行われる。**",
 ],
}

if __name__ == "__main__":
    print("s16 content OK — keys:", len(C))
