# -*- coding: utf-8 -*-
"""odyssey-s13 — video-spec — 海 / 夜 / 7.739s. For the first time the shore leaves the frame."""
import common as K


C = {
 "n": "s13",
 "title": "この作品で初めて、岸が枠の外へ出る",
 "duration": "7.739",
 "format": "video-spec",
 "has_man": False,
 "segment": "chorus-1-1",

 "header": """# chorus-1 / motion / 離脱 / video-spec
⚠️ **行: `l10` ／ 場所: `海` ／ 時刻: `夜` ／ 尺: 7.739秒。**
⚠️ **形式（`video-spec`）は §6 の `REF_FORMAT` に書く提案である。** ショット記録に `REF_FORMAT` の欄は無い——**形式は仕様の側にある。****ゆえにここに書いた形式は、まだ検査されていない。**
⛔ **この作品で初めて、岸が枠の外へ出る。** 出所: 曲の `l10`「死なない島を出て」——**サビの1行目である。**
⚠️ **この行は3回歌われる**（`l10`／`l19`／`l28`）。**この作品は3本とも役を同じにした**——**差分は §6 の形式が持つ。** ⛔ **`s13` は意図であり、`s20` は島の応答であり、`s27` は労働である。**
⚠️ **形式は `video-spec`。****この一変化を、いちばん素の文法で立てる。**
⛔ **この1本の画面に、人物は一人も居ない。**⚠️ **`s18` の記録の逐語:「この作品で初めて、男が水の上に居る。」**——**曲順で `s18`（`l16`）はこの1本（`l10`）より後である。**
⛔ **2026-09-29 の裁定①: この1本は同一性の塊を §18 に貼らない**（`has_man: False`。§20 を見る）。
⚠️ **この仕様のショット記録は `shots/odyssey-s13.yaml` である。**""",

 "intent": "One continuous take of one change — **岸が枠の外へ出る。** 最初のコマでは**島の岸が画面の下端にあり、海はまだ島のものである。** 最後のコマでは**岸が枠の外へ出て、海だけが残っている**——⚠️ **島が消えているのが、切れ目のコマである。** ⛔ **切らない。視点を変えない。** ⚠️ **カメラは島から海へ、左へ回る**——**動機は「彼が離れること」ではなく「島が離れること」である**（`motion.quality` の逐語）。",

 "world_concept": K.world_concept(
   "⚠️ **この1本は、島を出ることを、離れていく側の画で立てる。** "
   "**動機は「彼が離れること」ではなく「島が離れること」である**（`motion.quality` の逐語）"
   "——⛔ **ゆえにこの1本に、離れる者は一人も写らない。** "
   "**残るのは、離れていく側（島）と、離れた先（海）だけである。** "
   "⚠️ **この1本の終わりは、この作品で初めて、陸の無い画である。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本に返事は無い。****彼は画面に居ない。** ⚠️ **そして島は応えない**"
               "——**島が応えるのは2度目である**（`s20` の逐語:「**2度目の出発には、島の側が応える。**」）。"
               "**1度目は、島はただ小さくなる。**",
     "goddess": "⚠️ **この1本に彼女の姿は無い。****四つの姿のどれとしても現れない。** "
                "**この1本の光は星であり**（`ledger.locations.海.states.夜` の逐語:「光源は星と、"
                "その水面の反射だけである。」）、**彼女の第四の姿（枠の外の背後から来る水面の光）ではない。** "
                "⚠️ **声も、この1本の記録には無い**（§20 を見る）。",
     "name": "⚠️ **この1本には歌がある**——`l10` である。**名はどこにも無い。****島の名も、人の名も。**",
     "bow": "⚠️ **この1本に持ち手が無い。****弓も、斧も、櫂も写らない。**",
     "places": "この1本が置くのは一つ——`海`、**夜である。** ⚠️ **島は枠に入るが、"
               "この1本の場所は `海` である**——**ゆえに島は、`海.geography` の側から名指される**"
               "（「島の岸から見た海と、舟から見た海は、**同じ一つの海である**」）。",
     "japanese": "⚠️ **この1本には歌がある**——`l10`「死なない島を出て」である。"
                 "**画面の中の声ではない。****歌はポストで載る。**",
   },
   extra=[
     "⛔ **この1本が、この作品で初めて岸を枠の外へ出す。** "
     "**ゆえにこの1本の画面は、水の側から見た島である。**",
     "⚠️ **この1本に、離れる者は一人も写らない。****動機が「島が離れること」だからである**"
     "（`motion.quality` の逐語）——**人を一人入れれば、この1本は「彼が離れる」の画になる。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, seen from the water's surface and photographed as a film frame: long low swells "
     "with no white water moving steadily in one direction, the horizon level and unbroken, and — low in "
     "the frame, at the start — the island itself, a dark outline of land with one white line of water at "
     "its foot. ⚠️ **After the first 4.999秒 there is no land in the frame at all.** ⚠️ **No other "
     "vessel, no sail, no bird, no second island, no rock in the water.** ⚠️ **No marble, no columns, "
     "no architecture of any later age.**",
   "Color Language":
     "A narrow, graded palette — black water, a sky one shade above it, and one white line: the reflected "
     "path on the surface, whose brightest stretch is the water at the island's own foot. ⚠️ **Nothing is "
     "lit apart from the stars and their reflection** — **the shot has no second light.**",
   "Texture":
     "The water's surface fine-grained and broken, running; the swells' faces smooth and black; the "
     "island read as outline only, not as surface — coarse dark sand and wet shingle at its foot are "
     "**barely** readable at this distance and this light. ⚠️ **No skin and no cloth are in this frame** "
     "— no person is in it at any moment. Film grain present and even.",
   "Visual Density":
     "Low — and it **decreases** over the shot: the frame starts with water, horizon and a strip of land, "
     "and settles into water, horizon and one white line. ⚠️ **島が出て行くほど、画は薄くなる。**",
   "Atmosphere": "The hour in which the thing left behind is the only thing that moves.",
   "Time": "`夜` — the source is the stars and their reflection on the water; **the waves are black and "
           "the reflected path alone is white**（`ledger.locations.海.states.夜` の逐語）。"
           "**`s09`〜`s15` と同じ夜である。**⚠️ **この作品は話を進めない**——**ゆえにこの夜と、"
           "`s16` の夜明けとのあいだに、順序を読まない。** **画の中に日付を与えるものは何も無い。**",
 }),

 "subjects": [
   {"name": "nobody",
    "ref": "⛔ **この1本に、人物は一人も居ない。** 顔も、立ち姿も、肩も、遠景の点も写らない。"
           "⚠️ **参照集合は、それでも `男.identity` を引く。**",
    "appearance": "**無い。** ⚠️ **この1本の主題は、海と、出て行く島である。**",
    "behavior": "**無い。** ⚠️ **動くのは水面と、島の画面の中の大きさと、カメラの向きである。**",
    "continuity": "⚠️ **人を一人も入れないこと** — 島の上にも、水面にも、どの距離にも。"
                  "**入れば、この1本は「彼が離れる」の画になり、動機が入れ替わる。**"
                  "⚠️ **影も、水面への映り込みも入れない。**",
    "notes": ["⛔ **この判断の根拠を書く。** 記録の `unit`・`motion.subject`・ビートは、**彼を一度も"
              "名指さない。** そして **`s18` の記録の逐語:「この作品で初めて、男が水の上に居る。」**"
              "——**曲順で `s18`（`l16`）は、この1本（`l10`）の後である。** ⚠️ **ゆえにこの1本の水面に、"
              "彼はまだ居ない。**",
              "⚠️ **この1本は、同一性の塊を §18 に置かない**（`has_man: False`）——**人物がこの枠に"
              "居ない以上、人物の錠を貼れば、居ない者を貼ることになる**（2026-09-29 の裁定①）。"
              "**§20 を見る。**"]},
   {"name": "海",
    "ref": "**この1本の場所である。** ⚠️ **参照は `ledger.locations.海` の `base`・`geography`・"
           "`states.夜` である。** ⚠️ **水は一つであり、水平線も一つである**"
           "（`海.geography` の逐語:「The same waterline and the same horizon appear in both, so that the "
           "two views are demonstrably one sea.」）。",
    "appearance": "**長く低いうねりであり、白波を立てない。****水平線は一本で、途切れない。** "
                  "**夜であり、波は黒く、水面に一本の道だけが白い**（`海.states.夜`）。"
                  "⚠️ **陸は水際の島のほかに無い。****帆も、鳥も、他の舟も無い。**",
    "behavior": "**うねりが一方向へ進む。****そして島が、後ろへ下がる**——⚠️ **水は島を追わない。** "
                "**島の水際の白い線が、この1本のいちばん明るいものである**（`motion.subject` の逐語:"
                "「**そして岸の水際の白。**」）——**そしてそれは、枠の外へ出る。**",
    "continuity": "**Must preserve** — うねりの方向と低さ、白波が無いこと、水平線が水平で途切れないこと、"
                  "波が黒く反射の道だけが白いこと、そして陸が島ひとつだけであること。 "
                  "**May change** — 水面の細かさ、反射の道の幅、島の画面の中の大きさ、砂の明るさ。",
    "notes": ["⚠️ **`海.base` の逐語:「the surface broken only by the raft's own wake and by weed "
              "passing」**——⚠️ **この1本の枠に筏は入らない**（§5 と §20 を見る）。"
              "**ゆえに水面を割るものは、うねりと反射だけである。**",
              "⚠️ **この1本の最後の3.738秒、この海は陸を持たない。****この作品で初めてである。**"]},
   {"name": "島",
    "ref": "⚠️ **台帳に `島` という鍵は無い。** この島は、この作品の島である"
           "——**`岸` の `base`・`geography` が陸の側であり、`海.geography` が「島の岸から見た海」として"
           "名指す。** **この仕様は、この1本の側から島を名指す。**",
    "appearance": "**夜の島である。****その岸は、粗い暗い砂と濡れた小石であり、水際には低い濡れた岩がある**"
                  "（`岸.base` の逐語:「Coarse dark sand and wet shingle…Low wet rocks at the water's "
                  "edge.」）。⚠️ **この距離とこの光では、島は面ではなく輪郭である**——"
                  "**黒い線であり、その足もとに白い線が一本ある。**",
    "behavior": "**島は動かない。** ⚠️ **動くのは、島とカメラのあいだの距離である**"
                "——**ゆえに島は、枠の中で小さくなり、やがて枠の外へ出る。** "
                "**島は一度も振り向かないし、応えない。**",
    "continuity": "**Must preserve** — **同じ一つの島であること**、水際の白い線があること、"
                  "陸が低いこと（高い山も峰も無い）、そして**島が一つだけであること。** "
                  "**May change** — 枠の中の大きさ、輪郭の読み取れる量、白い線の長さ。",
    "notes": ["⛔ **島を主題にしないこと。****ビートは島を明示するが、カメラは島へ向き直らない**"
              "——**島は枠の下端にあり、そこから出て行く**（`aim` の逐語:「**島を出ることを、"
              "島を写さずに写せるか。**」）。**§20 に、この読みを書いた。**",
              "⚠️ **この1本の島の消え方は、この作品の他のどの1本にも無い**"
              "——**`s16` の夜明けには、島は浜であり、仕事場である。**"]},
 ],

 "environment": {
   "location": "`海` — **夜である。** ⚠️ **カメラは水面すれすれにある。** **この1本は、"
               "この作品で初めて、陸の無い画で終わる。**",
   "elements": "**長く低いうねり**（白波は無い）、**途切れない水平線**、**一本の反射の道**、"
               "**島の黒い輪郭と、その足もとの白い線**、そして**空と星。** "
               "⚠️ **他の船も、帆も、鳥も、二つ目の島も、水面の岩も無い。** "
               "⚠️ **月を光源にしない**——**この夜の光は星である。**",
   "behavior": "**うねりが一方向へ進む。** **島は小さくなり、後ろへ下がり、枠の外へ出る。** "
               "**水平線は動かない。** ⚠️ **海は彼に反応しない**（`s21` の註と同じ規則）"
               "——**応えるのは `s20` の島だけである。** **この1本の海は、島を追いもしない。**",
 },

 "objects": [
   "**無し。** ⚠️ **この1本の枠に物は一つも無い。****この作品の小道具は4つだけであり**"
   "（`ledger.props`）、**そのどれもこの枠に来ない**——**帆も、斧も、太陽の牛も無く、"
   "舟はこの1本では枠の外にある**（§20 を見る）。",
   "**島の水際の白い線** — ⚠️ **物ではない。****この1本のいちばん明るいものであり、"
   "最後のビートで枠の外へ出る。**",
   "**反射の道** — **星と、その水面の反射である。** ⚠️ **この1本の唯一の光源である。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****そしてこの1本の画面に、彼は居ない。**"
                  "`女神` — ⛔ **この1本に添付しない。****彼女は四つの姿のどれとしても現れない。**"
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.夜`・`舟`・`舟.appearance`・`舟.negative` の8鍵である。"
                  "⚠️ **`舟` が挙げられているのは、この1本の枠に筏が入るからではない**"
                  "——**カメラの足場の側である**（§5 と §20 を見る）。",
 "ref_extra": [
   "- ⚠️ **形式カード `video-spec` の文法は、この作品の下敷きそのものである**"
   "——**他の形式はどれも「`video-spec` に文法を1つ足したもの」である**"
   "（例: `impossible-camera` の逐語:「This card is `video-spec` plus one grammar. Fill §1–20 exactly "
   "as that card requires; what follows is only what this grammar adds to it.」）。"
   "**ゆえに §1–20 の骨格は `s01` と同じであり、この1本はそれに何も足さない。**",
   "- ⚠️ **形式カード `video-spec` の6つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `SUBJECT`＝the arc — **「島を出ることを、島を写さずに写す」ことである。**"
   "**彼は一人も枠に居ない**（`aim` の逐語:「⛔ **島を出ることを、島を写さずに写せるか。**"
   "そして**この一変化が、3回反復される最初の1回として立てられるか。**」）。",
   "  - `DURATION`＝clip length (**the model decides the duration**) — ⚠️ **この作品の尺は、"
   "曲から来る**（`bible.song.lines[].at` の差）。**この1本は `7.739s` である**"
   "——**「4秒より短いから伸ばす」をしない**（`docs/seedance-route.md` の明示の規則）。",
   "  - `ASPECT`＝aspect ratio — **`16:9`**（裁定④。§1 の4定数が固定する）。",
   "  - `BEATS`＝the beat list with second ranges — **3つであり、明示的に不等である**"
   "（`0-1.997s` transition ／ `1.997-4.999s` sparse ／ `4.999-7.739s` dense）。§8 を見る。",
   "  - `CORE`＝the beat that gets the largest share — **最後のビートである**（`4.999-7.739s`、2.740秒）。"
   "⚠️ **変わったことが起きるのは最後の2.740秒であり、そこへ向けて最初の4.999秒が使われる。**",
   "  - `HOOK`＝the note the clip ends on — ⚠️ **島が消えているコマである。**"
   "**説明のビートをそのあとに足さない**（カードの逐語:「End on the note, not after it.」）"
   "——**この1本は、島が枠の外へ出たコマで終わる。**",
   "- ⚠️ **カードの逐語:「A digest that gives every beat equal time is the video equivalent of "
   "cramming. **Uneven duration is the composition.**」**——この1本の配分は §8 に在る。**",
 ],

 "narrative": {
   "core": "**島が離れる** — 出て行く側を写すことで、「島を出る」が立つ。",
   "beginning": "**島の岸が画面の下端にまだある。****海は島のものである。**",
   "turn": "**島が小さくなる。** 波が前に流れる。",
   "peak": "**岸が枠の外へ出る。****海だけが残る。**",
   "pull": "⚠️ **島が消えているのが、切れ目のコマである。** **カメラはそこで止まり、"
           "**この1本は陸の無い画で終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last 2.740秒.** 最初の1.997秒は**岸がまだ枠の中にあることに**"
            "払われ、次の3.002秒は**島が小さくなること**に払われ、**最後の2.740秒がこの1本の出来事である**"
            "——**岸が枠の外へ出て、海だけが残る。** ⚠️ **`held` を1つも使わない。** "
            "⛔ **島は、最後のビートが終わるまで枠の中に残る**——**早く消せば、この1本は何も起きない。**",

 "actions": [
   ("ACT_ISLAND", "島はまだ画面の下端にある。**海は島のものである。**",
    "**島が小さくなりはじめる**——**波だけが前に流れる。**"),
   ("ACT_SHRINK", "島は小さくなっている。",
    "**島が後ろへ下がる**——**カメラは島から海へ、左へ回る。**"),
   ("ACT_LEAVE", "岸はまだ枠の中にある。",
    "**岸が枠の外へ出る**——**海だけが残る。**"),
   ("ACT_ERASE", "海だけが残っている。",
    "**島が消えているのが、切れ目のコマである**——**カメラはそこで止まる。**"),
 ],

 "camera": {
   "language": "Third person, **at the surface of the water**, low, **turned back toward the island at "
               "the first frame and holding its shore low in the lower part of the frame.** "
               "⚠️ **このカメラの位置は、誰の位置でもない**——**この1本に人は居ない。**",
   "events": "One event only. `0-1.997s` — **the island's shore sits at the lower edge of the frame and "
             "the camera does not yet turn**; then `1.997-4.999s` — **the island grows smaller and the "
             "camera begins a slow yaw left, from the island to the open sea**; then `4.999-7.739s` — "
             "**the shore leaves the frame altogether, only the sea is left, and the camera stops.** "
             "⚠️ **動機は「彼が離れること」ではなく「島が離れること」である**（`motion.quality` の逐語）。"
             "⚠️ **この1本は一度も島へ向き直らない**——**向き直れば、この1本は島の画になる。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends none of them** "
               "—— ⚠️ **この1本の移動は、位置の移動ではなく、回転である。****回転は一様であり、"
               "重さを持つ。** **No crane. No dolly. No Steadicam** — **ゆえにこの1本は、水の高さを"
               "一度も離れない。** **No handheld, no whip, no shake, no snap zoom, no rack focus, "
               "no unnatural rotation, and no unmotivated move.**",
 },

 "motion": {
   "subject": "**この1本の主題の運動は、後ろへ遠ざかる島である。****島は小さくなり、枠の中で下がり、"
              "やがて外へ出る。** ⚠️ **島は回らないし、揺れない**——**動くのは大きさだけである。**",
   "object": "**動く物は無い。****この1本に物は一つも置かれていない。**",
   "environment": "**うねりが一方向へ進み、白波を立てない。****水平線は動かない。** "
                  "**反射の道は、その流れの中で揺れ続ける。** ⚠️ **島は動かない**"
                  "——**動くのは、島とカメラのあいだの距離である。**",
   "weight": "**島の重さは、動かないことで出る。** ⚠️ **速いものは一つも無い**——**この1本は、"
             "重いものが遠ざかる速さでできている。**",
   "inertia": "**一度小さくなりはじめた島は、とまらない。** ⚠️ **最後のコマまで、島は枠の中で"
              "小さくなり続けている**——**止まるのは、この1本の最後のコマである。**",
   "acceleration": "**加速しない。****回転も、うねりも、島の後退も、一様である。** "
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この7.739秒の全コマで、"
               "水面は動いている。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**白波を立てない水であり、"
             "島は静かに出て行く。**",
 },

 "emotion": {
   "arc": "**離れることが、離れる者の画を持たない。** ⚠️ **この1本の感情は、島の側にある**"
          "——**置いていかれる側である。** **彼が居ないので、観客は島の側から見ることになる。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****島が枠の外へ出ることである。** "
             "**誰も写さないのに、見送る感じだけが残る。**",
 },

 "lighting": {
   "base": "**夜である。****光源は星と、その水面の反射だけである。****波は黒く、反射の道だけが白い**"
           "（`ledger.locations.海.states.夜` の逐語）。⚠️ **月も、火も、灯も無い。** "
           "⚠️ **島は光らない**——**島は、星の下の黒い輪郭である。** "
           "**この1本のいちばん明るいのは、島の水際の白い線である。**",
   "events": "**One, and it runs the whole shot.** **反射の道が一本あり、島の水際でいちばん白い**"
             "——**その白い線が、最後のビートで枠の外へ出る。** ⚠️ **光源は動かない。** "
             "⚠️ **様式カードの逐語:「The grade holds for the whole shot — a colour temperature that "
             "swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**低いうねりが水を進む音。****水が島の岸に当たる音。****弱い風。** "
          "⚠️ **この1本に人の音は一つも無い。** ⚠️ **島の音は無い**——**島は動かない。** "
          "⚠️ **呼ぶ声は無い**（§20 を見る）。",
   "music": K.NO_MUSIC + " ⚠️ **主題歌はこの1本のあいだ鳴っている**（`l10`）——**が、"
            "この1本の中には無い。****編集で載る。** **生成された音床が来れば、同じ瞬間に"
            "二つの音楽が重なる。**",
   "environment": "夜の外海。**水、風、そして遠さ。** ⚠️ **鳥の声も、帆の音も、他の船の音も無い**"
                  "（`海.base` の逐語:「No land, no sail, no bird, no other vessel.」）。",
 },

 "continuity": {
   "identity": "⚠️ **この1本に人が一人も居ないので、人物の同一性は掛からない。** "
               "**掛かるのは島と海の同一性である**——**島が一つであること、低く平らであること、"
               "水際の白い線があること、そして水と水平線が一つであること。** "
               "⛔ **`男.identity` は参照集合に在るが（§6）、この1本は同一性の塊を §18 に貼らない**"
               "——**人物が枠に居ないためである**（2026-09-29 の裁定①。§20 を見る）。"
               "**ゆえに `s05` が立てた顔は、この1本には要らない。**",
   "spatial": "**カメラは水面すれすれにある。** ⚠️ **水際の線と水平線は、この作品のどの岸の画と"
              "同じものである**（`海.geography` の逐語:「The same waterline and the same horizon appear "
              "in both, so that the two views are demonstrably one sea.」）——**ゆえにこの1本は、"
              "舟から見る海と同じ一つの海である。** ⛔ **この1本で初めて、島が枠の外へ出る**"
              "——**それでも島は同じ一つの島である。** "
              "⚠️ **この1本は `video-spec` を名乗り、この形式は §15 から何も免除しない**"
              "——**免除を名乗るのは、`coexisting-realities` を名乗る4本だけである。**"
              "**この1本の場所と時刻は、台帳の `海`／`夜` のままである。**",
   "temporal": "**夜である。****`s09`〜`s15` と同じ夜である。** ⚠️ **この作品は話を進めない**"
               "（§2 の逐語:「the work does not advance a story」）——**曲順で `s16`（`l14`、夜明け）は、"
               "この1本より後に筏を作る。****ゆえにこの1本の夜と、あの夜明けとのあいだに、"
               "順序を読まない。** **画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **この1本の光は星とその反射だけである。**"
             "⚠️ **これはこの作品で初めて、陸の無い画で終わる1本である。**",
   "motion": "Full animation, not limited. **水面が動き、島が小さくなり、カメラが左へ回る。** "
             "⚠️ **回り切ったあと、カメラは動かない。**",
   "sound": "**うねり、水際の岸、弱い風。****音楽なし。言葉なし。** ⚠️ **呼ぶ声は無い。**",
 },

 "must_not": K.must_not_common(has_man=False, goddess_extra=(
     "⚠️ **この1本の彼女は、四つの姿のどれとしても現れない。** **ここにあるのは、夜の海と島だけである。** "
     "⚠️ **海を女の形にしないこと**——**夜の海は、いちばん輪郭を結びたがる**"
     "（`characters.女神.negatives` の逐語:「no visible body, no hands, no feet, no arms, "
     "no silhouette with a readable outline」）。")) + [
   "**No person in frame at any moment** — no figure at any distance, in any focus, **no one on the "
   "island, no one on the water, no silhouette, no hands, no oar, no one steering**, and no shadow or "
   "reflection of a person anywhere. ⚠️ **`s18` の記録の逐語:「この作品で初めて、男が水の上に居る。」**",
   "**No boat, no ship, no hull, no keel, no planking, no sail, and no raft in the frame** — "
   "⚠️ **この1本の枠に筏の一部も写さない**（`s14` のビート1が、舳先が画面の下端に入ると書く"
   "——**この1本では、まだ入っていない**）。",
   "**No land other than the one island that leaves the frame** — no second island, no headland, "
   "no far coast, no rock standing in the water, **and no other shore anywhere.** ⚠️ **この1本の終わりに、"
   "陸は無い。**",
   "**No moon, no torch, no lamp, and no second light on the water** — **この夜の光は星と、その反射だけである**"
   "（`海.states.夜` の逐語:「光源は星と、その水面の反射だけである。」）。",
   "**No white water, no breaking crest, no foam and no spray**（`海.base` の逐語:「Long low swells with "
   "no white water」）。",
   "**No bird and no other vessel**（`海.base` の逐語:「No land, no sail, no bird, no other vessel.」）。",
   "**No cut to a second setup.** ⚠️ **この1本は1つの画である。**",
   "⚠️ **この1本の筏は、この禁制の対象ではない。** `舟` は §3 の参照集合に在り、**この1本のカメラはその上にある**——**禁じられているのは船であり、筏ではない**（`props.舟.negative` の逐語:「**no boat, no ship, no hull, no keel, no planking**」）。⚠️ **そしてこの1本の枠に、筏の一部も入らない**（§16 の下の項を見る）。",
   "⚠️ **この1本に男は居ないが、`男.negatives` は参照集合に在る**（§6）——**彼の禁制はこの1本でも"
   "掛かる**（逐語:「no muscular hero's body, no heroic pose, no heroic lighting」・"
   "「no youthful face, no beardless face, no clean or unlined skin」・「no armour, no helmet, "
   "no greaves, no shield」）。⚠️ **ここでは、それが「人を一人も置かないこと」として効く。**",
 ],

 "must": [
   "**岸が枠の外へ出る** — そして**島が消えていることが、切れ目のコマである。**",
   "⚠️ **同一性の塊を §18 に貼らないこと** — **人物が枠に居ないので、この1本は人物の錠を運ばない**"
   "（`has_man: False`。2026-09-29 の裁定①）。**§20 を見る。**",
   "⛔ **人を一人も入れない** — 島の上にも、水面にも、どの距離にも、**影にも、映り込みにも。**",
   "⚠️ **動機が「島が離れること」であること** — **彼の画にしないこと**（`motion.quality` の逐語）。",
   "⚠️ **水際の線と水平線は、この作品の岸の画と同じものである** — **同じ一つの海であることが、"
   "二つの画のあいだで読めること。**",
   "⚠️ **島は、一度もこの1本の主題にならない** — 島は枠の下端にあり、そこから出て行く"
   "（`aim` の逐語:「島を出ることを、島を写さずに写せるか」）。",
   "**星の光だけであること** — **月も、二つ目の光も無い。**",
   "⚠️ **変化は最後のコマで終わる** — **島が枠の外へ出たコマで、この1本は終わる。**",
 ],

 "prefer": "The water kept black and the swells low and unbroken; one reflected path, brightest where it "
           "catches at the island's own foot; the island read as outline only, low and level, with no "
           "peak and nothing built on it; **the sea left holding the whole frame at the end.**",
 "allow": "A lens flare where the light crosses the frame; a moderate depth of field that lets the far "
          "water and the island both go soft; **a yaw that ends when the last of the shore has left the "
          "frame.**",

 "priorities": [
   "**岸が枠の外へ出ること** — **そして島が消えているコマで終わること。** **この1本の切れ目はそれである。**",
   "⛔ **人を一人も入れないこと** — **入れば、この1本の動機が彼の側へ移り、`l10` の最初の1本が"
   "「彼が離れる」の画になる。**",
   "⚠️ **動機が「島が離れること」であること** — 回転は島から海へ、一様に。",
   "⚠️ **同一性の塊を §18 に置かないこと** — **人物が枠に居ないためである**（2026-09-29 の裁定①）。",
   "⚠️ **水際の線と水平線が、岸の画と同一であること。**",
   "**星の光だけであること** — **月も、火も、二つ目の光も無い。**",
   "⚠️ **島が最後まで枠の中に残ること** — **早く消せば、この1本は何も起きない。**",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `video-spec` を名乗る**——**この形式の禁制（`no uniform pacing`・"
   "`no equal-length beats`・`no static slideshow of stills` ほか）は §16 の床に在り、"
   "**カード自身の `Negative` も §16 の側から届く。** "
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "A 7.739-second cinematic take (16:9) of the open sea at night seen from the surface of the water, one "
   "clip, one continuous take, one change: **the island's shore leaves the frame, and only the sea is "
   "left — the island going out of the frame is the final frame.** **No person is in this frame at any "
   "moment: no one is on the island, no one is on the water, and no one steers anything here.**\n\n"
   "0-1.997s: **the island's shore is still at the lower edge of the frame, and the sea belongs to the "
   "island.**\n"
   "1.997-4.999s: **the island grows smaller; only the waves run forward.**\n"
   "4.999-7.739s: **the shore leaves the frame and only the sea is left — and the take ends on that "
   "frame.**\n\n"
   "**The camera is at the surface of the water and turns slowly left, from the island to the open sea; "
   "the move is motivated by the island leaving and not by anyone leaving, and it is a rotation and not a "
   "travel.** **It never turns back toward the island, and it stops when the last of the shore has left "
   "the frame.** **The night's only light is the stars and their single reflected path on the water: the "
   "waves are black and the reflected path alone is white, and the brightest stretch of it is the water "
   "at the island's own foot.** **No other vessel, no sail, no bird, no second island, no rock standing "
   "in the water, and the horizon level and unbroken.** **After 4.999 seconds there is no land in this "
   "frame at all.** **This is a bronze-age island before classical Greece: no made thing of any kind "
   "stands in this frame.** **This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the shore leaves the frame and the sea is left.)"),

 "visual_scene": (
   "Open sea at night seen from the surface of the water, photographed as a film frame: long low swells "
   "with no white water moving steadily in one direction, the water black and broken into fine facets, "
   "and one reflected path of starlight lying on it in white; the horizon level and unbroken beyond. "
   "**Low in the frame, at the start, the island: a dark outline of land, low and level, with coarse dark "
   "sand and wet shingle at its foot barely readable at this distance and one white line of water along "
   "its waterline** — and then the island is gone and there is only the sea and the horizon. **No figure "
   "is in the frame at any distance or in any focus, nothing stands on the island, and no shadow or "
   "reflection of a person falls anywhere in it.** No other vessel, no sail, no bird, no second island, "
   "no moon."),

 "visual_meta": K.VISUAL_META.replace(
   "Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked; ",
   "**no skin and no cloth anywhere in this frame**: ").replace(
   "wet shingle with individual stones",
   "a dark island outline over coarse dark sand and wet shingle, read as outline only").replace(
   "warm ochre where the low sun falls",
   "cold white held in the one reflected path on the black water") + (
   " ⚠️ **No person is in this frame at any moment.** "
   "⚠️ **The island is low and level, with no peak and "
   "nothing built on it, and it leaves the frame in the last movement**; the light on the water is the "
   "stars' own reflected path and nothing else."),

 "motion_prompt": (
   "Full animation, not limited. **The long low swells move steadily in one direction and do not break.** "
   "**The island grows smaller, falls back in the frame and at last leaves it — its size is the only "
   "thing about it that moves: it does not turn, does not rock, and does not resolve into surface.** "
   "**The reflected path of starlight wavers on the running water and runs unbroken.** **The horizon does "
   "not move at all.** **The camera turns slowly left and stops.** No motion blur smears, no stutter, no "
   "floaty weightless motion, no static frames — **the water moves in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **at the surface of the water**, low, turned back toward the island at the first frame "
   "and holding its shore low in the lower part of the frame. One event only: **a slow yaw left, from the "
   "island to the open sea, which ends when the last of the shore has left the frame; the camera then "
   "stops.** ⚠️ **The move is motivated by the island leaving, not by anyone leaving; the stop is "
   "motivated by the shore having gone.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and "
   "this shot spends none of them** — the move is a rotation, not a travel, and it carries a real rig's "
   "even rate. No crane. No dolly. No Steadicam. **Do not turn back toward the island and do not move "
   "again after the stop.** No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural "
   "rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **low swells moving over the water, water meeting the island's "
   "shingle, and a little wind** — and when the shore leaves the frame the water sound is the only sound "
   "that remains. ⚠️ **There is no human sound in this shot at all** — **and nothing is heard from the "
   "island, which does not move.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⛔ **この1本の §18 は人物の同一性を運ばない**"
                        "——**人物がこの枠に居ないためである**（`has_man: False`）"
                        "——**`Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は書かれていない。**"
                        "⚠️ **`男.negatives` は参照集合に在る**——**ゆえに §16 は彼の禁制も運ぶ**（§20 を見る）。",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water ＋ shingle ＋ wind ／ no music",
 "unresolved": [
   "✅ **裁定（2026-09-29）: この1本は人物を枠に置かず、同一性の塊も §18 に貼らない**（`has_man: False`）"
   "——**記録の `unit`・`motion.subject`・ビートが彼を一度も名指さないためである。** "
   "⚠️ **この仕様は裁定の前、塊を作品の錠として §18 に置いていた**——**裁定①がそれを落とした。** "
   "⛔ **ゆえに `Master Prompt` にも `Visual Prompt` にも `{IDENTITY}` は無い。** "
   "⚠️ **`男.negatives` は参照集合に在るので、§16 は彼の禁制を運び続ける。**",
   "⚠️ **`aim` の「島を写さずに」の読みが二つある。** 記録のビートは島を明示する"
   "（**島が小さくなる**／**島が消える**）。**この仕様は「島を、一度も主題にしない」と読んだ**"
   "——島は枠の下端に留まり、カメラは島へ向き直らず、島は面ではなく輪郭である。"
   "⚠️ **もう一方の読み（島を一度も画に入れない）は、ビートと衝突する。**",
   "⚠️ **カメラの足場を、記録は書かない。** 参照集合が `舟` を挙げるので、**この仕様は足場を筏と読んだ**"
   "——**そして `s14` のビート1が「舳先が画面の下端に入る」と書くので、この1本では筏を枠に入れない。**"
   "⚠️ **筏の上に彼が立っていないことは、この読みの一部である**（`s18` の記録を見る）。"
   "**ゆえにこの1本の筏は、無人のまま水の上にある。****それが正しいかは、記録からは読めない。**",
   "⚠️ **彼女の声をこの1本に置くかどうかを、記録は何も言わない。****この仕様は置いていない**"
   "——**この1本は島の画であり、呼ぶ声が入れば、それは応答になる**（応えるのは `s20` である）。",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
 ],
 "risks": [
   "⛔ **誰かが写る。** 島の上に、あるいは水面に——**遠景の点一つで、この1本は「彼が離れる」の画になり、"
   "`l10` の3本のうち、この1本の動機が入れ替わる。**",
   "⛔ **島が主題になる。** ⚠️ **カメラが島へ向き直る、島に山を作る、島に何か建てる**——"
   "**この1本の島は、低い黒い輪郭であり、出て行くものである。**",
   "**島が早く消えすぎる。** ⚠️ **動きが最初のビートで終われば、最後の2.740秒に何も残らず、"
   "切れ目のコマが空になる。**",
   "**島が消えない。** ⚠️ **動機が弱ければ、この1本は海の画のままで終わり、`l10` の変化が起きない。**",
   "**回転が動機を持たない。** ⚠️ **`cinematic-still` は動機の無い移動を禁じる**——"
   "**この回転の動機は「島が離れること」であり、それはドリーやクレーンでは立たない。**",
   "**白波が立つ。** ⚠️ **波を低く保てないと、この海は別の海になる。**",
   "**月が光源として入る。** ⚠️ **海の夜の光は星である**——**月明かりの青い海は、この作品の夜ではない。**",
   "**二つ目の島、または水に立つ岩が入る。** ⚠️ **この1本の終わりに、陸は無い。**",
 ],
}

if __name__ == "__main__":
    print("s13 content OK — keys:", len(C))
