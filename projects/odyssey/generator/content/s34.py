# -*- coding: utf-8 -*-
"""odyssey-s34 — video-spec — 海 / 夜 / 8.431s. 曲の後奏（291.489–299.920）。この作品の最後の画面。"""
import common as K


C = {
 "n": "s34",
 "title": "舟は、まだ沖にある",
 "duration": "8.431",
 "format": "video-spec",
 "has_man": True,
 "segment": "outro-2",

 "band": [
   "『永遠より遠い』 outro「海」 / 離脱 / motion —— 歌が終わったあとの8.4秒——着かせずに閉じる",
   "舟は進み続けるが、水平線との距離は測れない——暗さが少しだけ濃くなる。",
   "8.431秒、カメラは舟から離れて海の画になる——舟がまだ沖にあるのが、切れ目である。",
   "どこにも着かず、歌も無い——この8.431秒は、無音である。",
 ],
 "header": """⛔ **この8.431秒が、この作品の最後の画面である。**
出所: 曲の後奏（291.489–299.920）。**歌はもう無い。**
⚠️ **節 `outro` の対応にせず、`l34` の2本目として受けた**——理由は `ledger.song_coverage` の註にある（habits-mv の `l31` と同じ手当て）。
**ゆえにこの1本は、`s33` と同じ行の2本目である。****行が10.000秒を持ち、その後奏が8.431秒である。**
⛔ **形式は `video-spec`。****最後の画は、いちばん素の形式でなければならない。**
⚠️ **この作品が繰り返し使った文法を、ここで全部脱ぐ。****脱ぐことは、この1本の内容である**（記録の逐語）。
⛔ **その回数はここに写さない**——**実測として読まれる数である**（§20 の「未処理」を見る）。
⛔ **着かせずに閉じる。** `world.rules` の五番の逐語:「**この作品は、帰り着かない。**上陸・犬・乳母・殺害・床・和睦を映さない。**最後の画面でも、舟はまだ沖にある。**」
——⚠️ **この一行が、この1本の設計そのものである**（記録の逐語）。
⚠️ **役は `離脱` である。** 固有基準は「境界の可視化・**出た先の示唆**」——⛔ **この1本が出た先を示唆しないことが、この作品の最後の判断である**（記録の逐語）。
⚠️ **この仕様のショット記録は `shots/odyssey-s34.yaml` である。**""",

 "intent": "⛔ **歌が終わったあとの8.4秒で、この作品を閉じられるか。** "
           "⛔ **着かせずに閉じる**——**それがこの作品の最後の一変化である**（`aim` の逐語）。"
           "⚠️ **ゆえにこの1本は、何も明かさずに終わる。****明かさないことが、"
           "この1本の最後の一変化である。**",

 "world_concept": K.world_concept(
   "⚠️ **この1本の場所は `海`、時刻は `夜` である。**"
   "**歌は終わっており、この1本には歌が無い。**"
   "⛔ **この作品は、帰り着かない**（`world.rules` の五番）——"
   "**最後の画面でも、舟はまだ沖にある。**"
   "⚠️ **この1本が置くのは、海だけが残る画面である。**"
   "**男はもう読めない大きさに小さくなり、舟だけが読める。**"
   "⛔ **そしてその先に、何も示唆しない。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⛔ **この1本にも、答えは返らない。****最後の画面まで、"
               "この作品は答えを一度も渡さない。**"
               "⚠️ **この1本で質問も消える**——**舟はまだ沖にあり、"
               "その先は画にならない。**",
     "goddess": "⚠️ **この1本に彼女は四つの姿のどれとしても現れない。**"
                "**この1本の画には、人のかたちが一つも無い**"
                "——**舟の上の男は、この1本の最後には読めない大きさになる。**",
     "name": "⚠️ **この1本に名は無い。****そして `disclosure_state` の四番は `absent` である**"
             "——**観客は、彼の名を最後まで知らない。****この1本でも、"
             "それは与えられない。**",
     "bow": "⚠️ **この1本に弓は無い。****斧も、帆も、この1本の画には無い**"
            "——**帆は張られておらず、彼は櫂を扱っている。**",
     "places": "この1本が置くのは一つ——`海`、**この作品でいちばん多く写る場所である**。"
               "⚠️ **この1本のカメラは、舟の上に無い**——**水の上にあり、"
               "舟から離れてゆく。**"
               "**ゆえにこの1本の画は、海と、その中の小さな舟から成る。**",
     "japanese": "⚠️ **この作品の言語は日本語である**（`bible.language`）。"
                 "⛔ **この1本には言葉が無い**——**歌は終わっており、"
                 "この8.431秒は無音である**（`motion.law` の逐語）。"
                 "**ゆえにこの1本の `Audio Prompt` は、言語を名乗るだけである。**",
   },
   extra=[
     "⛔ **形式 `video-spec` は、この作品の素の形式である。**"
     "⚠️ **記録はこの形式について、こう書いている**——"
     "「**形式（`video-spec`）は ② で §6 `REF_FORMAT` に書く提案である。**"
     "**ショット記録に `REF_FORMAT` の欄は無い**——形式は仕様（§6）の側にある。"
     "⚠️ **ゆえにここに書いた形式は、まだ検査されていない。**」"
     "⚠️ **その提案は、この仕様の §6 に書かれた**——**採用するかどうかは著者が決める。**",
     "⚠️ **この形式の四つの軸**（時間・運動・カメラ・音）は、"
     "**この作品の他の形式が畳んでしまうものである。**"
     "**この1本では、その四つがそのまま立っている**——"
     "**脱ぐとは、この四つを素で使うことである。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "Open sea at night, far from any land, photographed as a film frame **from the water itself, low, "
     "just above the surface**: **the raft lies small and dark on the water — twenty-odd pine logs "
     "lashed with hand-twisted cordage, a short mast carrying no sail, a steering oar tied at the "
     "stern, and one man working that oar aboard it** — and long low swells run to a horizon that "
     "carries no land. ⚠️ **No shore, no island, no sail, no bird, and no other vessel.**",
   "Color Language":
     "A narrow, graded palette, and it has one source: **the night is lit by the stars and by their "
     "reflection on the water, so the waves are black and the reflected path alone is white**"
     "（`ledger.locations.海.states.夜` の逐語:「光源は星と、その水面の反射だけである。波は黒く、"
     "反射の道だけが白い。」）. ⚠️ **Nothing is lit apart from the sea** — **the same starlight falls "
     "on the raft and on the water, and the shot has no second light.** ****最後の2.934秒では、"
     "画のほとんどが黒い水である。**",
   "Texture":
     "Wet pine logs with grain and rope-burn, hand-twisted cordage, undyed coarse wool with visible "
     "fibre; the water's surface fine-grained and broken. Film grain present and even. "
     "⚠️ **この1本では、丸太も縄も毛織りも、遠くにある**——**質感は、"
     "近い距離にあるものの質感である。**",
   "Rendering":
     "Photographic — anamorphic optics, **a long lens kept wide so the raft reads small**, subtle oval "
     "bokeh, **a gentle flare on the one reflected path**. **Not a photograph's stillness: a film "
     "frame, with a real lens's fall-off at the edges.** No illustration, no CGI look, no cartoon color.",
   "Visual Density": "**Falling.** ⚠️ **この1本の画に入っているものの数は、"
                     "8.431秒のあいだに減る**——**舟が小さくなり、"
                     "暗さが少しだけ濃くなる。****最後の2.934秒は、"
                     "海と、その中の小さな舟だけである。**",
   "Time": "`夜` — the source is the stars and their reflection on the water; the waves black and the "
           "reflected path alone white. ⚠️ **この作品は一日のうちの三つの時刻しか使わない**"
           "（`日没`・`夜`・`夜明け`）。"
           "⛔ **この1本の最後のコマに、夜明けを置かない**——**置けば、"
           "この作品は「この先がある」と言うことになる。**",
   "Atmosphere": "The hour in which the work lets go of him and stays with the sea.",
 }),

 "subjects": [
   K.man_subject(
     behavior="⛔ **この1本で、彼は漕ぎ続ける。****この1本は、"
              "彼が読めなくなるまで離れて終わる**"
              "（`motion.quality` の逐語:「**舟は進み続ける。**」）。"
              "**漕ぐ手は止まらず、舟は進み、この8.431秒のあいだに、"
              "彼は画の中で小さくなる。**"
              "⛔ **彼はレンズを見ない。****この作品の人は、"
              "自分が映画の中に居ることを知らない**（`world.rules` の一番）。",
     may="漕ぐ手の角度、舟の上下、小さくなる速さ。"
         "⛔ **顔は、この1本の最後には読めない**——**読めたら、この1本は彼の画になる。**",
     extra_notes=[
       "⛔ **この1本の主役は、彼ではなく、舟と海である。**"
       "**彼は「舟の影」の中に居る**——**記録が `motion.subject` に挙げているのは、"
       "海面・**舟の影**・水平線の3つである。**",
       "⚠️ **`s05` が立てた顔の基準は、この1本では遠さの側に置かれる。**"
       "**カメラが離れてゆくので、顔は最初から読めない。**"
       "**同一性の塊は、それでも §18 にまるごと在る**（§15 と §18 を見る）。",
       "⚠️ **この1本に彼の声は無い。****漕ぐ音も、"
       "この1本の最後では遠い**（§14）。",
     ]),
   {"name": "この1本の海",
    "ref": "**この1本の、残る側である。** ⚠️ **参照は `ledger.locations.海` の "
           "`base` と `states.夜`、そして `海.geography` の逐語である。**"
           "⚠️ **参照画像は無い**（裁定②）。",
    "appearance": "**四方を水に囲まれ、どの方向にも陸が見えない**（`海.geography` の逐語）。"
                  "**長く低いうねりであり、白波を立てない。**"
                  "**星の反射が、一つの方向へ伸びる道になっている。**"
                  "⛔ **その道の先にも、何も無い**——**島も、岸も、灯も無い。**",
    "behavior": "**波が寄せ、舟が上下する。**"
                "⛔ **そしてこの1本の海は、舟を追いかけない**"
                "——**カメラが離れても、"
                "海は同じ速さで同じ方向へ動き続ける。**",
    "continuity": "**Must preserve** — 白波が無いこと、反射の道が一つの方向へ伸びること、"
                  "**そしてどの方向にも陸が見えないこと**。"
                  "**May change** — 反射の線の位置、うねりの高さ、画の中の水の割合。",
    "notes": ["⛔ **この1本の最後のコマは、この海の画である。**"
              "**舟は、その中にまだ在る**——**それだけが、この作品の最後の事実である。**",
              "⚠️ **この1本の海には、彼の舟しか無い**——**帆も、"
              "他の船も、鳥も無い。**"]},
 ],

 "environment": {
   "location": "`海` — **夜である。****カメラは水の上にあり、舟から離れてゆく。**"
               "**この1本の画は、海と、その中の小さな舟から成る。**"
               "⚠️ **陸は、どの方向にも見えない**（`海.geography` の逐語）。",
   "elements": "**長く低いうねり**（白波の無いもの）、**一つの方向へ絶えず動く水面**、"
               "**星の反射の道**、**舟と、その上の漕ぐ影**、**そして水平線**。"
               "⛔ **島も、岸も、帆も、鳥も、他の船も無い。**",
   "behavior": "**波が寄せ、舟が上下する。**"
               "⚠️ **この1本の環境は、男に反応しない**"
               "——**彼が漕ぐのは変わらず、海は変わらず、"
               "変わるのは画の中の遠さだけである**（`motion.quality` の逐語:"
               "「**しかし水平線との距離は、この8.431秒では測れない。**」）。",
 },

 "objects": [
   "**舟** — **この1本の地面である。**二十数本の丸太、手で撚った縄、粗削りの板、"
   "**船尾に縛られた舵の櫂**、**何も張られていない短いマスト。**"
   "⚠️ **この1本のあいだ、舟は前へ進み続ける。****そして画の中では小さくなる。**"
   "**帆は張られていない**——**彼は櫂を扱っている。**",
   "**舵の櫂** — ⚠️ **この1本の「漕ぐ手」が扱っているものである。**"
   "**この作品の舟に、漕ぎ櫂は無い**（`舟.appearance` の逐語:「No keel, no ribs, no planking, "
   "no mast step, no rudder — a steering oar tied at the stern, lashed, not fitted.」）"
   "——**ゆえにこの1本の漕ぎは、船尾の舵の櫂で行われる。**"
   "⛔ **この読みは推論である**（§20 の「未処理」を見る）。",
   "**航跡** — 舟の後ろへ伸びる。⚠️ **この1本では、航跡も小さくなる。**",
   "**水平線** — ⚠️ **この1本のいちばん遠いものである。**"
   "⛔ **ここに何も置かない**——**陸も、灯も、"
   "水平線の上の形も無い。**"
   "⚠️ **この1本のカメラは後退するので、水平線の高さは画の中で動かない。**"
   "**動くのは、舟の大きさだけである。**",
   "⚠️ **この作品の小道具4つのうち、この1本に来るのは舟だけである**（`ledger.props`）"
   "——**帆も、斧も、太陽の牛も、この1本の画には無い。**",
 ],

 "ref_character": "`男` — ⚠️ **この1本に添付しない。****同一性は英文で運ばれる**（§3 と §18）。"
                  "`女神` — **この1本には添付しない。彼女はこの1本に現れない。** "
                  "参照集合が挙げているのは `男.identity`・`男.negatives`・`海`・`海.geography`・"
                  "`海.states.夜`・`舟`・`舟.appearance`・`舟.negative` の8鍵である。"
                  "⚠️ **集合に `帆` は無い**——**この1本は帆を張らない。**",
 "ref_extra": [
   "- ⚠️ **形式カード `video-spec` は「この基盤の通常の形式であり、"
   "三つの経路すべてがこれを埋める」と書いている**"
   "（逐語:「This card is the normal format, and all three routes fill it.」）。",
   "- ⚠️ **カードの逐語:「**Not *which instant*, but **which instants earn seconds, and which get "
   "one**」**」**——**この1本では、最後の2.934秒が、いちばん多くを稼いだ時間である**"
   "（**海だけが残る時間である**）。",
   "- ⚠️ **カードの逐語:「**End on the note, not after it.** The last second is where the viewer "
   "decides whether there is a next. Land the clip on the hook — do not add a resolving beat after "
   "it.」**⛔ **ゆえにこの1本は、舟がまだ沖にあるコマで終わり、"
   "その後ろに解決の1コマを置かない。**",
   "- ⚠️ **カードの逐語:「**Assuming music and subtitles arrive only when asked for** — an omission "
   "is a request for whatever the model does by default (measured: `no on-screen subtitles` was "
   "already in the Negative, and subtitles were burned in anyway)」**"
   "——⚠️ **この1本は曲の後奏であり、歌はもう無い。****ゆえにこの1本で音楽を省けば、"
   "生成器は自分の既定を置く。** **§16 と §18 の `Audio Prompt` に、"
   "無いことを書いた。**",
   "- ⚠️ **形式カード `video-spec` の6つの変数**（⚠️ 定義はカードの逐語である）:",
   "  - `SUBJECT`＝the arc — **`海面と、舟の影と、水平線`である**"
   "（`motion.subject` の逐語）。"
   "**弧は「舟が小さくなり、海だけが残る」である。**"
   "⚠️ **彼を弧の主語にしない**——**この1本では、"
   "彼は海の中の小さな影になる。**",
   "  - `DURATION`＝clip length — **`8.431s`。**"
   "⚠️ **カードの逐語:「the model decides the duration」**"
   "——**この作品では曲が決めている**（`bible.time_source: song`。"
   "291.489–299.920 の実測である）。"
   "⛔ **「4秒より短いから伸ばす」をしない**（`docs/seedance-route.md` の明示の規則）。"
   "**この1本は短くないが、規則は同じである。**",
   "  - `ASPECT`＝aspect ratio — **`16:9`。**"
   "⚠️ **この作品は34本すべてでこれを固定する**（§19 の `Output`）。",
   "  - `BEATS`＝the beat list with second ranges — "
   "**`0-2.496s`（transition）／`2.496-5.497s`（sparse）／`5.497-8.431s`（dense）。**"
   "⚠️ **非均等である**——**3.001秒と2.934秒が、"
   "2.496秒の後ろに並ぶ。**",
   "  - `CORE`＝the beat that gets the largest share — **`2.496-5.497s`である。**"
   "**3.001秒**（8.431秒の35.6%）。"
   "⚠️ **カードの錨は「~30%」であり、この1本はそれを満たす。**"
   "⚠️ **ただし閉じのビートは2.934秒であり、差は0.067秒である**"
   "——**ゆえにこの1本の共有は、"
   "「カメラが離れる時間」と「海だけが残る時間」の2つに、"
   "ほぼ半分ずつ配られている。**",
   "  - `HOOK`＝the note the clip ends on — **`舟は、まだ沖にある。`**"
   "**どこにも着いていない**（`unit.after` の逐語）。"
   "⛔ **この1本の最後のコマに、"
   "その先を示すものを一つも置かない。**",
 ],

 "narrative": {
   "core": "**歌が終わったあとの8.4秒で、この作品を閉じられるか** — "
           "**着かせずに閉じることが、この1本の答えである。**",
   "beginning": "**舟が進んでいる。****まだ近い。**"
                "⚠️ **この2.496秒は、"
                "この作品でいちばん近くに彼が居る時間である**"
                "——**そしてそれが、この1本の始まりである。**",
   "turn": "**カメラが舟から離れる。****暗さが少しだけ濃くなる。****舟が小さくなる。**"
           "⛔ **この1本の一つの出来事は、"
           "これである**——**この作品は、彼から離れる。**",
   "peak": "**海の画になる。**"
           "⚠️ **峰は「何かが起こる」ではなく「何かが小さくなる」である**"
           "——**ゆえにこの1本の山は、"
           "画の中のものが減っていくことに在る。**",
   "pull": "**舟はまだ沖にある**——**着いていないことが、切れ目のコマである**"
           "（`beats` の3番目の逐語）。"
           "⛔ **この1本の直後に、何も無い。****この作品は、"
           "ここで終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Sinking, and the last two beats are deliberately near-equal.** "
            "⚠️ **この1本は8.431秒あり、3つのビートを持つ**——"
            "**2.496秒・3.001秒・2.934秒である**"
            "（`L37` が敷き詰めを検算する。**合計は8.431秒である**）。"
            "⚠️ **いちばん短いのは最初であり、"
            "いちばん長いのは真ん中である**（35.6%）。"
            "**閉じのビートは0.067秒だけ短い**——"
            "**この1本の後半2つは、ほぼ同じ長さを持つ。**"
            "⚠️ **`held` を1つも使わない。** 止まるのは主題であって、画面ではない"
            "（`shot-record.schema.json` の `motion`）——**この1本では海が動き続け、"
            "カメラだけが一度止まる。**",

 "actions": [
   ("ACT_ROW", "舟が進んでいる。**まだ近い。**",
    "**漕ぐ手が、水に入り、出る**——**この1本の時間が、"
    "漕ぎの繰り返しとして始まる。****この1本のあいだ、漕ぎは止まらない。**"),
   ("ACT_WITHDRAW", "**舟は、まだ近い。**",
    "**カメラが舟から離れる。****暗さが少しだけ濃くなる。****舟が小さくなる。**"
    "⚠️ **これはカメラの出来事であって、世界の出来事ではない**"
    "——**海では何も起こっていない。**"),
   ("ACT_SEA", "**舟が小さくなっている。**",
    "**海の画になる。****舟はまだ沖にある**——**着いていないことが、"
    "切れ目のコマである。** ⛔ **この1本は、"
    "そこで終わる。**"),
 ],

 "camera": {
   "language": "Third person, **from the water itself, low, just above the surface, looking at the "
               "raft** — the lens is not aboard and never goes aboard. "
               "⚠️ **この1本のカメラは、この作品で唯一、男から離れてゆくカメラである**"
               "（`motion.quality` の逐語:「**カメラは舟から離れ、海の画になる。**」）。",
   "events": "**One camera event, and it has a start, a target and an end.** "
             "⚠️ **`0-2.496s`: カメラは止まっている**（**舟がまだ近い**）。"
             "⚠️ **`2.496s`→`5.497s`: 後退（ドリー）。**"
             "**的は舟である。****速さは一定で、"
             "ゆっくりである。****この1本のあいだに舟が小さくなる。**"
             "⚠️ **`5.497s`→`8.431s`: カメラは止まっている。**"
             "**止まったカメラの中で、海だけが動き続ける。**"
             "⛔ **この1本に、切りのもう一つのセットアップは無い。**"
             "**1本は1つの画である。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the "
               "dolly** — ⚠️ **動機は、この1本の内容そのものである**"
               "（`motion.law` の逐語:「**この作品のカメラは、常に何かを追っているか、"
               "何かへ寄っているか、何かから離れている。**」）——"
               "**この1本は、何かから離れている。****それだけが、"
               "この1本のカメラ移動の理由である。** "
               "**The crane and the Steadicam are not spent.** No handheld, no whip, no shake, no "
               "snap zoom, no rack focus, no unnatural rotation, **no unmotivated move**, "
               "**no fade, no dissolve, no iris**, and **no cut to a second setup.**",
 },

 "motion": {
   "subject": "⛔ **この1本の主題の運動は、海面と、舟の影と、水平線である**"
              "（`motion.subject` の逐語）。"
              "**舟は進み続ける。****しかし水平線との距離は、"
              "この8.431秒では測れない**（`motion.quality` の逐語）"
              "——**ゆえにこの1本の主題の運動は、「進んでいるのに、"
              "近づいていない」である。**"
              "⚠️ **彼はその中の小さな影である。**",
   "object": "**櫂が、水に入り、出る。****舟が、前へ進む。****そして画の中で小さくなる。**"
             "⚠️ **舟の上下は、うねりに従う**——**寄せて、"
             "持ち上げられて、下りる。**"
             "**この1本のあいだ、周期は変わらない。**",
   "environment": "**波が寄せ、舟が上下し、暗さが少しだけ濃くなる**"
                  "（`motion.quality` の逐語）。"
                  "⚠️ **カメラが後退するので、"
                  "うねりの数が画の中で増える**——**遠くまで見えるようになるためである。**"
                  "⛔ **海は、この1本のあいだ、何も始めない。**",
   "weight": "**舟は重い。****うねりは、舟を持ち上げて、下ろす。**"
             "⚠️ **この1本の質量は、海の側にある**"
             "——**遠くから見ると、舟は海の動きに完全に従っている。**",
   "inertia": "**うねりは、寄せたあと、返る。****舟は、返りに少し遅れて従う。**"
              "⚠️ **この1本のいちばん大きな運動は、"
              "この遅れである**——**そしてカメラは、"
              "その遅れを小さくしてゆく。**",
   "acceleration": "**カメラの後退は、加速しない。****一定である。**"
                   "**ゆえに舟の縮み方も一定である。**"
                   "⚠️ **この1本に、速くなる区間が一つも無い。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この8.431秒に、"
               "止まったフレームは一つも無い**——**海が動き続けるからである。**",
   "impact": "**無い。** ⛔ **この1本に衝撃は一つも無い**"
             "——**最後の画面に、"
             "何かが起こってはならない。**",
 },

 "emotion": {
   "arc": "**この作品が、彼から離れる。** ⚠️ **置き去りにするのではない**"
          "——**見ていられなくなって離れるのでもない。**"
          "**この1本の感情は、"
          "「彼を残して、海が残る」という事実である。**"
          "⛔ **悲しみにしない。****安堵にもしない。**"
          "**この1本は何も決めない**——**決めないことが、"
          "この作品の最後の一変化である。**",
   "events": "⚠️ **この1本の感情の出来事は、"
             "「離れる」である。****時刻を持つのはカメラの後退の2つだけである**"
             "（`2.496s` に始まり、`5.497s` に終わる）。"
             "⛔ **この1本の最後の2.934秒には、"
             "感情の出来事が一つも無い**——**海だけが残る。**",
 },

 "lighting": {
   "base": "**夜である。****光源は星と、その水面の反射だけである。****波は黒く、"
           "反射の道だけが白い**（`ledger.locations.海.states.夜` の逐語）。"
           "⚠️ **この1本の光源は一つであり、それは星である。**"
           "⚠️ **月も、火も、灯も無い。**"
           "⛔ **そしてこの1本に、夜明けは来ない**"
           "——**東の空が明るくなることを、この作品の最後の8.431秒はしない。**",
   "events": "**One, and it is not a lighting change: as the camera draws away, more black water "
             "enters the frame and the lit raft takes less of it, so the darkness in the picture "
             "thickens slightly**"
             "（`motion.quality` の逐語:「**暗さが少しだけ濃くなる。**」）。"
             "⚠️ **光源の明るさは、この1本のあいだ変わらない**"
             "——**変わるのは、画の中の黒い水の割合である。**"
             "⛔ **露出を落とさない。****フェードしない。**"
             "⛔ **そしてこの1本の最後のコマに、光を足さない。**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE + " ⚠️ **この1本には、話す者が一人も居ない**"
     "——**そして歌も無い。****この8.431秒は、"
     "この作品でいちばん音の少ない時間である。**",
   "sfx": "**海の音である。****うねりが寄せる音、水が丸太に沿って滑る音、"
          "そして遠くの漕ぐ音。**"
          "⚠️ **この1本の音は、画に従う**"
          "——**舟が小さくなるにつれて、漕ぐ音は遠くなり、"
          "最後の2.934秒は海の音だけになる。**"
          "⚠️ **白波の音は無い**——**この海は白波を立てない。**"
          "⛔ **この読みは推論である**（§20 の「未処理」を見る）。",
   "music": K.NO_MUSIC + " ⚠️ **この8.431秒は、曲のあとである**"
            "——**後奏（291.489–299.920）であり、歌はもう無い**（記録の逐語）。"
            "⚠️ **ゆえに「no background music」の床が、"
            "この1本で最も効く**（`motion.law` の逐語:「基盤の床の3行目が、"
            "この1本で最も効く」）。"
            "**生成された音床が来れば、この作品の最後の画面に、"
            "曲のあとの音楽が載る。**",
   "environment": "**夜の外海。****水の音と、遠い漕ぎの音である。**"
                  "⛔ **そしてこの1本には、"
                  "この作品の言葉が一つも無い**——**歌は終わり、"
                  "彼は口を開かない。**",
 },

 "continuity": {
   "identity": K.identity(
     extra_must="⚠️ **この1本では、同一性の塊は遠さの側にある**"
                "——**顔は読めないが、塊は §18 にまるごと貼られている。****要約しない。**",
     may="舟の上下、漕ぐ手の角度、小さくなる速さ。"),
   "spatial": "**四方を水に囲まれ、どの方向にも陸が見えない**（`海.geography` の逐語:"
              "「From the raft, the water surrounds the frame on all sides and no land is visible in any "
              "direction, including behind.」）。⚠️ **この1本のカメラは水の上にあり、"
              "舟から離れてゆく。**"
              "⚠️ **ゆえにこの1本は、この作品で唯一、"
              "舟の外から舟を写す1本である。**"
              "⛔ **そして、どこにも着かない。**",
   "temporal": "**夜である。****この作品の三つの時刻のうちの一つである**"
               "（`日没`・`夜`・`夜明け`）。⚠️ **この1本は曲の最後の8.431秒であり、"
               "曲はこの1本で終わる。**"
               "**画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** **光は星の光だけである。**"
             "⚠️ **そしてこの1本の舟と海は、`s20` の舟と海と同一でなければならない**"
             "——**丸太、縄、舵の櫂、張られていないマスト、そしてうねりの低さである。**"
             "**遠いことと、崩れていることは別である。**",
   "motion": "Full animation, not limited. **海が、この1本のあいだ一度も止まらない。** "
             "⚠️ **カメラは、2.496秒から5.497秒までだけ動き、"
             "その前後は止まっている。**"
             "**舟は一度も止まらない。**",
   "sound": "海の音と、遠い漕ぎの音。**音楽なし。言葉なし。**"
            "⚠️ **この1本は、この作品でいちばん静かな1本である。**",
 },

 "must_not": K.must_not_common(has_man=True, goddess_extra=(
     "⚠️ **この1本の画には、人のかたちが一つも無い**——**舟の上の男は、"
     "この1本の最後には読めない大きさになる。**")) + [
   "**No land, no island, no shore, and no light on the horizon** — ⛔ **この作品は、"
   "帰り着かない**（`world.rules` の五番）。",
   "**No arrival, no landing, no beach, no house, and no person waiting** — "
   "⛔ **着かせずに閉じることが、この1本の内容である。**",
   "**No suggestion of what lies beyond the last frame** — **夜明けも、"
   "水平線の上の形も、光も置かない**（`role: 離脱` の固有基準 "
   "「**出た先の示唆**」に対する、この作品の最後の判断である）。",
   "**No fade to black, no fade in, no dissolve, no iris, and no closing vignette** — "
   "⛔ **この1本は、"
   "「終わった」と見せるために暗くしない。****舟がまだ沖にあるコマで終わる。**",
   "**No cut, and no second setup** — ⚠️ **1本は1つの画である。**"
   "**この1本には、"
   "後ろに解決の1コマが無い。**",
   "**No camera move that is not the one dolly retreat** — ⛔ **この1本の動機は"
   "「離れること」ただ一つであり、それ以外の移動を足さない。**",
   "**No boat, no ship, no hull, no sail set, and no second oar invented** — "
   "⚠️ **この1本の舟は筏であり、"
   "帆を張っておらず、彼は船尾の舵の櫂を扱っている。**"
   "⚠️ **`must_not_common` の "
   "「No boat, no ship, no hull, no keel, no planking, no sail, no raft, and no other vessel」は、"
   "この1本でも逐語で効く**（`s20` と `s33` と同じ手当てである）。",
   "**No music of any kind, and no song continuing into this shot** — "
   "⚠️ **この1本は曲のあとである。**",
   "**No dialogue, no voice, no whisper, and no audible breath from him.**",
   "**No bow, no arrow, no axe, and no fire in this frame.**",
   "**No heroic treatment, no monumental framing, and no light on the raft that the sea does not "
   "have.**",
 ],

 "must": [
   "⛔ **舟が、この1本のあいだ進み続けること。**",
   "⛔ **カメラが2.496秒に離れ始め、5.497秒に止まること** — **この1本の唯一のカメラ出来事である。**",
   "⛔ **最後のコマに、舟がまだ沖にあること** — **着いていないことが、"
   "この1本の切れ目のコマである。**",
   "⛔ **この1本のあとに、何も置かないこと** — **この作品は、ここで終わる。**",
   "⚠️ **水平線の高さが、この1本のあいだ動かないこと** — **後退するカメラでは、"
   "水平線は同じ高さに留まる。****動くのは舟の大きさだけである。**",
   "⚠️ **光が星の光だけであること** — **光源の明るさは、"
   "この1本のあいだ変わらない。**",
   "⚠️ **画の中のものが減ってゆくこと** — **この1本の密度は、"
   "落ちてゆく。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "⚠️ **歌がこの1本へ続かないこと** — **後奏であり、歌はもう無い。**",
 ],

 "prefer": "The night held black and the reflected path the only white; the swell kept long, low and "
           "crestless; **the raft kept small and dark and still readable as a raft in the last frame**; "
           "**the horizon kept at the same image height for the whole take**; **the camera's retreat kept "
           "at one steady speed with no ease-out into a stop.**",
 "allow": "The reflected path crossing the water between the lens and the raft and leaving it; the "
          "swell's height varying slightly; the raft pitching on the swell; **the oar's sound growing "
          "farther as the raft shrinks**; weed passing the raft.",

 "priorities": [
   "⛔ **着かせないこと。** ⛔ **その先を示唆しないこと。** "
   "**この1本の検収は「まだ沖にある」であり、"
   "陸や光を置いた瞬間に、この作品の最後の判断が破れる。**",
   "⛔ **最後のコマに、この1本の答えが写っていること**"
   "——**舟がまだ沖にあることである。**",
   "⛔ **切らないこと。****二つ目のセットアップを持たないこと。**",
   "⛔ **フェードしないこと** — **最後の画は、"
   "「終わった」と見せるために暗くしない。**",
   "⛔ **音楽を省かないこと** — **この1本は曲のあとであり、"
   "省けば生成器が自分の既定を置く。**",
   "**The identity block pasted into §18 is preserved clause by clause.**",
   "**光は星の光だけであること。**",
   "⚠️ **この1本が8.431秒であること**（曲の後奏の実測である）。",
   "⚠️ **ビートが非均等であること** — **2.496秒・3.001秒・2.934秒である。**",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `video-spec` を名乗るが、その禁制（`no uniform pacing`・`no equal-length beats`・"
   "`no static slideshow of stills`・`no floaty weightless motion`・`no scene cuts to unrelated "
   "locations`）は §16 に在って、ここには無い。**"
   "**ゆえに34本の `Negative Prompt` は、`s01` と同じ一行である。**"
   "⚠️ **この形式の四つの軸（時間・運動・カメラ・音）は §8・§11・§10・§14 に書いた**"
   "——**この節に持ち込めば、34本の同一性が崩れる。**"),

 "master": (
   "A 8.431-second cinematic take (16:9) of the sea at night after the last line has been sung — "
   "**the sea's surface, the raft's small dark shape on it, and the horizon** — one clip, one camera "
   "move, one continuous take.\n\n"
   "Beats, deliberately uneven: `0-2.496s` the raft drives on, still close; `2.496-5.497s` **the "
   "camera draws away from the raft, the darkness thickens a little, and the raft shrinks**; "
   "`5.497-8.431s` **the frame is the sea, and the raft is still offshore.** "
   "The core beat — `2.496-5.497s`, the camera drawing away — holds the largest single share of the "
   "duration (3.001s of 8.431s, 35.6%), and the closing beat is 0.067s behind it (2.934s); the "
   "opening beat passes quickly (2.496s). "
   "**Ends on the note: the raft is still offshore, and nothing has been reached.** "
   "**No beat follows it, and the take does not fade.**\n\n"
   "⚠️ **{IDENTITY}**\n\n"
   "**The camera is on the water, low, just above the surface, and it never goes aboard.** "
   "**It is still until 2.496s, it retreats steadily from 2.496s to 5.497s with the raft as its "
   "target, and it is still again to the end** — **a dolly, spent on the one motive this shot has: "
   "leaving him.** **The horizon stays at the same height in the frame throughout, and only the raft's "
   "size changes.** **The light is the starlight and its broken reflection, and it does not change; "
   "the darkness thickens only because more black water enters the frame.** "
   "**No land, no island, no shore, no light on the horizon, no arrival, and nothing beyond the last "
   "frame is suggested.** **No cut, no dissolve, no iris and no fade.** "
   "**No music: the song has already ended and this take is silent of it.** "
   "**No dialogue, no voice, and no woman in frame at all, at any distance, in any focus.** "
   "**No sail is set on this raft, and the sea holds no other vessel.** "
   "**This is a bronze-age sea before classical Greece: no made thing of any later age.** "
   "**This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one camera move: the camera leaves the raft, and the sea is what is left.)"),

 "visual_scene": (
   "Open sea at night, far from any land, photographed as a film frame **from the water itself, low, "
   "just above the surface**: **the raft lies small and dark on the water — twenty-odd pine logs "
   "lashed with hand-twisted cordage, a short mast carrying no sail, a steering oar tied at the "
   "stern, and one man working that oar aboard it.** **No face, no profile and no limb of his is "
   "readable at this distance.** Long low swells with no white water run to a horizon that carries "
   "no land, and one broken path of reflected starlight lies on the water between the lens and the "
   "raft. **No other vessel, no shore, no light and no bird is anywhere in the frame, and the "
   "horizon is empty.**"),

 "visual_meta": (
   "Anamorphic lens with subtle oval bokeh and a gentle flare on the one reflected path; **a long "
   "lens kept wide so the raft reads small**; a graded palette of black water with one broken white "
   "path of reflected starlight, and no warm tone anywhere in the frame. Wet pine logs, hand-twisted "
   "cordage and coarse undyed wool where they are near enough to read; even film grain over "
   "everything. No painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration. "
   "⚠️ **No face is resolved in this frame, and no feature of the man is legible: the identity block "
   "carried above is this work's lock, held for every shot whose reference set carries it, and at "
   "this distance nothing of it can be rendered as a feature.**"),

 "motion_prompt": (
   "Full animation, not limited. **The swell runs in one direction at a steady rate with no crest and "
   "no white water, lifting the raft and setting it down; the reflected path breaks into short "
   "strokes on the moving face of the water; the oar is driven and released without pause.** "
   "**The camera retreats steadily from 2.496s to 5.497s — no acceleration and no ease-out into the "
   "stop — and the raft shrinks with it; before and after that it is still.** "
   "**Nothing else in the frame moves toward anything: the raft makes no progress against the "
   "horizon in this take, and its distance from the horizon cannot be measured across these 8.431 "
   "seconds.** **The darkness thickens only because more black water enters the frame.** "
   "No motion blur smears, no stutter, no floaty weightless motion, no static frames — **the water "
   "moves in every frame of the take.**"),

 "camera_prompt": (
   "Third person, **from the water itself, low, just above the surface, looking at the raft** — the "
   "lens is never aboard. **One camera event: still from `0-2.496s`, a steady dolly retreat from "
   "`2.496s` to `5.497s` with the raft as its target, then still from `5.497s` to the end of the "
   "take.** **The horizon holds the same image height throughout, and only the raft's size changes.** "
   "⚠️ **The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** — "
   "the style's law forbids a move without a motive, and **this shot's one motive is leaving him: "
   "that is what this shot's role means here.** **The crane and the Steadicam are not spent.** "
   "**No cut, no dissolve, no iris, no fade, and no second setup.** "
   "⚠️ **Do not drift, do not creep, and do not let the frame breathe.** No handheld, no whip, no "
   "shake, no snap zoom, no rack focus, no unnatural rotation, and **no unmotivated move.**"),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **the swell sliding along the raft's logs, water moving on "
   "the open sea, the raft's logs creaking a little, and the oar's strokes coming from farther away "
   "as the raft shrinks** — **this shot's sound follows its picture.** "
   "⚠️ **No crest breaks and nothing slaps or slaps back.** "
   "⚠️ **No music at all: the song has already ended, and this take is the silence after it** — "
   "**the generator's default music must not be placed here.** "
   "⚠️ **No voice, no whisper and no dialogue: no one speaks in this take.** "
   "⚠️ **No bell, no bird and no shore reaches this shot.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (video-spec) ／ "
                        "REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**"
                        "（裁定②。そしてこの経路は既定で何も添付しない）。"
                        "⚠️ **同一性は `Visual Prompt` と `Master Prompt` の英文が運ぶ。**"
                        "⚠️ **この1本の参照集合の8鍵のうち、画に入るのは `男`・`海`・`舟` である**"
                        "（`帆` は集合に無い）。",
 "camera_events_count": "1 camera event — a dolly retreat at 2.496s, as listed in §10",
 "audio_events": "no dialogue ／ the swell, the water, the raft's logs, the oar from farther away ／ "
                 "no music (the song has already ended)",
 "unresolved": [
   "⚠️ **`CORE` を、この仕様は真ん中のビート（`2.496-5.497s`）と読んだ。**"
   "⚠️ **実測——2.496秒・3.001秒・2.934秒であり、合計は8.431秒である。**"
   "**いちばん大きいのは真ん中の3.001秒（35.6%）であり、"
   "閉じのビートは0.067秒だけ短い。**"
   "⚠️ **カードは `CORE` を「the beat that gets the largest share」と定義している**"
   "——**ゆえに共有の側で名指した。**"
   "⛔ **記録は閉じのビートを `dense` と印しているが、"
   "そのビートは最大の共有を持たない。****閉じのビートを `CORE` と書けば、"
   "この仕様は持っていない共有を名乗ることになる。**"
   "**この判断が正しいかは、著者が決めることである。**",
   "⚠️ **最後のビートに舟が残るかどうかを、この仕様は「残る」と読んだ。**"
   "⚠️ **記録の逐語は「**海の画になる。**」であり、"
   "「舟が画から消える」とも読める。**"
   "**しかし `world.rules` の五番は「**最後の画面でも、舟はまだ沖にある**」と言い、"
   "カードは `HOOK` を「the note the clip ends on」と定義している**"
   "——**フックが画に読めなければ、この1本は着いたかどうかを言えない。**"
   "**ゆえにこの仕様は、舟を最後まで画の中に小さく残した。**"
   "⛔ **どちらの読みを採るかは、絵を見て決めることである。**",
   "⚠️ **「**暗さが少しだけ濃くなる**」を、この仕様は「画の中の黒い水の割合が増える」と読んだ**"
   "（**光源の明るさは変わらない**）。"
   "⚠️ **もし露出が落ちることを指すなら、それは照明の変化であり、"
   "§13 の `Lighting Events` を書き換える必要がある。**"
   "⛔ **いずれにせよ、フェードにはしない**——"
   "**この作品の最後の画面を、暗くして終わらせない。**",
   "⚠️ **記録の逐語「**この8.431秒は無音である**」を、"
   "この仕様は「音楽が無い」と読んだ**"
   "——**括弧が理由を曲の終わりに置いているためである**"
   "（「（曲はここで終わっている）」）。"
   "⛔ **もし全音の無音を指すなら、§14 の `Sound Effects` と `Environment` は空になり、"
   "この1本は完全な無音の8.431秒になる。**"
   "**この読みは著者の裁定を要する。**",
   "⚠️ **この仕様の §14 に、「**この1本の音は画に従う**」と書いた**"
   "（**舟が小さくなるにつれて漕ぐ音が遠くなる**）。"
   "⚠️ **これは記録から読めない**——**記録は音の混合について何も言っていない。**"
   "**この仕様が置いた設計である。**"
   "⛔ **混合を距離に従わせない判断もありうる**"
   "（**遠さは画の側の事実であり、音の側の事実ではない**）。",
   "⚠️ **記録の逐語「**この作品が27回使った文法を、ここで全部脱ぐ。**」の数は、"
   "この仕様では写さなかった。**"
   "⚠️ **34本すべての仕様が出た時点の実測は、こうである**"
   "——`video-spec` 10本・`meaning-responsive` 5本・`time-fold` 4本・"
   "`impossible-camera` 4本・`coexisting-realities` 4本・`transformation` 3本・"
   "`remembered-world` 3本・`recognizing-world` 1本（**合計34本**）。"
   "**ゆえに「他の文法を使った本」は24本であり、"
   "この数え方では27が出ない。**"
   "⛔ **27が何を数えた数なのかを、私は記録から読めなかった。**"
   "**ゆえに仕様には、回数を書かずに「繰り返し使った文法」と書いた。**"
   "⚠️ **これは、この仕様を書いた時点ではなく、"
   "34本が揃った時点の実測である。**",
   "⚠️ **この1本の「漕ぐ手」を、この仕様は「船尾の舵の櫂を扱う手」と読んだ。**"
   "⚠️ **`舟.appearance` は、この舟に漕ぎ櫂を持たせていない。****ゆえにこの読みは推論である**"
   "（`s33` と同じ読みであり、同じ理由である）。",
   "⚠️ **`must_not_common` は「**No boat, no ship, no hull, no keel, no planking, no sail, no raft, "
   "and no other vessel.**」を逐語で含む**——**そしてこの1本の画には、"
   "舟が入る。** ⚠️ **この仕様は、`s20` と `s33` の先例にならって、"
   "逐語の行を消さずに、その下に「この作品の舟は筏であり、ボートではない」と書き足した。**"
   "（⚠️ **記録の `forbidden_set` の側は「no boat, no ship, no hull, no other vessel」であり、"
   "筏を禁じていない**——**ゆえにこの1本の禁制は、"
   "共通の一行のほうが広い。**）",
   "⚠️ **与えられた指示は「`s34` は曲の最終行（`outro`、18.44秒）である」と述べていた。**"
   "⚠️ **記録が与えるこの1本の尺は `8.431s` である**"
   "（`duration` の逐語、および後奏の実測 291.489–299.920）。"
   "**18.431秒は `l34` の10.000秒と後奏の8.431秒の合計であり、"
   "その前半は `s33` が受けている。**"
   "⛔ **ゆえにこの1本を18秒に伸ばしてはならない**"
   "（`docs/seedance-route.md` の明示の規則:「4秒より短いから伸ばす」をしない）。"
   "**記録の側が正である。**",
 ],
 "risks": [
   "⛔ **着く。** この1本の最大の危険である——**陸・岸・浜・家・待つ人が、"
   "この作品の最後の一変化を消す。**",
   "⛔ **その先を示唆する。** ⚠️ **夜明け、水平線の上の形、"
   "遠い灯——どれか一つでも置けば、"
   "`離脱` の固有基準にこの作品が答えていないことになる**"
   "（**この作品の最後の判断は、示唆しないことである**）。",
   "⛔ **フェードで終わる。** ⚠️ **最後の画は、"
   "フェードを呼び寄せる**——**そしてこの作品は、"
   "「終わった」と見せるために暗くしない。**",
   "⛔ **切りが入る。** ⚠️ **二つ目のセットアップ、"
   "舟の寄り、水平線の切り——どれもこの1本には無い。**",
   "⛔ **音楽が載る。** ⚠️ **この1本は曲のあとであり、"
   "省けば生成器が自分の既定を置く。**",
   "⚠️ **舟が最後のコマで読めない。** ⚠️ **小さくしすぎれば、"
   "`HOOK`（**まだ沖にある**）が画から消える**"
   "——**小さく、しかし舟として読めること。**",
   "⚠️ **舟がボートになる。** ⚠️ **丸太・縄・舵の櫂である**"
   "（`舟.appearance` の逐語）。****帆が立ってもいけない**——"
   "**この1本の参照集合に `帆` は無い。**",
   "⚠️ **光源が増える。** ⚠️ **この1本の光は星と、"
   "その水面の反射だけである**——**月も、灯も、"
   "夜明けの色も無い。**",
 ],
}
