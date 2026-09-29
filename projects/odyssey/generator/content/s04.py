# -*- coding: utf-8 -*-
"""odyssey-s04 — video-spec — 岸 / 日没 / 11.399s. No person. intro-4."""
import common as K


C = {
 "n": "s04",
 "title": "声の入る1コマ手前で、島を置く",
 "duration": "11.399",
 "format": "video-spec",
 "has_man": False,
 "segment": "intro-4",

 "band": [
   "『永遠より遠い』 intro「岸」 / 情景 / motion —— 声の入る1コマ手前で、島を置く",
   "色を失った海と、判別できなくなっていく岸——水平線だけが細く残る。",
   "11.399秒を、カメラは島から離れるためではなく島を置くために後ろへ下がる——島が枠の外へ出るのが、切れ目である。",
   "この1本の中では何も言われず、歌も入らない——声は、切れ目の直後に来る。",
 ],
 "header": """⚠️ **41.500–52.899。`intro` の最後の1本である。** 出所は `bible.song.sections` の `intro`——
**次の1本（`s05`）から歌が始まる。**
⚠️ **実測**: 41.5→52.5秒は長い減衰であり（52.25秒で −27.8 dB）、そして **52.75秒に +8.9 dB——声の入りである。**
⛔ **ゆえにこの1本の切れ目は、この作品で最も強い音の事象と一致する。****歌が始まる直前に終わる。**
⚠️ **形式は `video-spec`。****声を迎える画は、いちばん素である。** ⚠️ **`s01` と同じ形式である**——
**`intro` は `video-spec` で始まり `video-spec` で終わる。** 真ん中の2本だけが文法を持つ。
⛔ **この1本に人は一人も居ない。** `intro` の4本（`s01`〜`s04`）はすべてそうである——
**島が先にあり、人は後に来る。**
⚠️ **この仕様のショット記録は `shots/odyssey-s04.yaml` である。**""",

 "intent": "One continuous take of one change — **the light finishes going out and the island leaves the frame.** At the first frame the path of light is already breaking up, the sea is going to one colour, and the shore can still be told from the water; by the last frame the sand and the stones are black, the white of the crests is the only bright thing in the picture, the horizon is a thin line, **and the camera has drawn back until the island's own ground has fallen out of the frame** — and the take ends on that frame. ⚠️ **No person is in this shot, at any distance, in any focus.** ⚠️ **The change completes on the last frame of the take** — the island is still leaving the frame when the cut arrives — **and the frame is never still in the meantime**: the swell keeps arriving and going back at a rate that does not change, and the camera is still drawing back.",

 "world_concept": K.world_concept(
   "⚠️ **この1本は `intro` の最後である。****島を、人の居ないまま、もう一度だけ見せる。** "
   "**次の1本（`s05`）で彼が現れ、その次の瞬間に歌が始まる**——"
   "**ゆえにこの1本は、この作品で最後の「誰も居ない島」である。**"),

 "world_rules": K.world_rules(
   tails={
     "answer": "⚠️ **この1本に人は一人も居ない。****ゆえに返事は返されないのではなく、問いがまだ立てられていない。**"
               "**この作品の返事は `s05` からである。**",
     "goddess": "⚠️ **彼女はこの1本に、四つの姿のどれとしても現れない**——"
                "**この1本の光は日の光そのものであり、そしてそれは消えていく。**",
     "name": "⚠️ **この1本は、歌のまだ始まらない区間の最後である**（`intro`）。**名はどこにも無い。**",
     "bow": "⚠️ **この1本に持ち手が居ない。****弓も斧も無い。**",
     "places": "この1本が置くのは一つ——`岸`、**そしてその岸を、最後に画面の外へ出す。**",
     "japanese": "⚠️ **この1本に歌は無い**——**声はこの1本の切れ目の次のコマからである**（52.899秒）。",
   },
   extra=[
     "⛔ **この1本は、この作品で最も強い音の事象の直前に終わる。** ⚠️ **実測の +8.9 dB はこの1本の外にある**"
     "——**この1本は、その音を受け取らない。****受け取るのは `s05` である。**",
   ]),

 "visual_language": K.visual_language(**{
   "Art Direction":
     "A bronze-age Mediterranean island shore at the end of the day, photographed as a film, with the "
     "light almost gone. Rough wet stone, coarse sand, sea-worn driftwood; the sea is the largest "
     "object in the frame and **by the last frame it is the only one.** ⚠️ **No marble, no columns, no "
     "architecture of any later age, and no made thing of any kind.**",
   "Color Language":
     "A narrow, graded palette that moves in one direction only — warm ochre where the low sun still "
     "falls, cold slate blue in the water and the wet stone, and then almost nothing: **the shore goes "
     "to a black that holds no colour, leaving one thin pale line at the horizon.** ⚠️ **The palette "
     "does not come back up.** ⚠️ **Nothing is lit apart from the shore** — the same light falls on "
     "everything in the frame, and **the shot has no second light.**",
   "Texture":
     "Wet shingle with grain and individual stones; coarse dark sand; dry weed that is fibrous and "
     "salt-bleached; the water's surface fine-grained and broken, never glassy. ⚠️ **No skin and no "
     "cloth are in this frame** — **この1本に人は居ない。** Film grain present and even.",
   "Visual Density":
     "Low, and lower as the shot goes on. One focal point — the white of the breaking swell — and it is "
     "the last thing the light leaves; **by the last frame the picture holds water, one line and nothing "
     "else, and that emptiness is the ending.**",
   "Atmosphere": "The minute in which a place stops being visible without ever stopping being there.",
   "Time": "`日没` — the last of the day, on the island's shore, later than `s01` and `s03`. **The same "
           "evening as `s05`〜`s08`; the work does not fix a date.** ⚠️ **This shot runs from the last "
           "ochre to almost no light at all.**",
 }),

 "subjects": [
   {"name": "nobody",
    "ref": "**この1本に、人物は一人も居ない。** 顔も、立ち姿も、肩も、遠景の点も、写らない。"
           "⚠️ **それでもこの1本は「誰かが来る直前」である**——**人は入らないが、人の気配は、この作品の順序そのものである。**",
    "appearance": "**無い。** ⚠️ **この1本の主題は光であって、人物ではない。**",
    "behavior": "**無い。** ⚠️ **動くのは波と光だけであり、誰かではない。**",
    "continuity": "⚠️ **人を一人も入れないこと。****入れば、`s05` が最初の人間でなくなる**"
                  "——**この作品の順序は、島が先で人が後である。**",
    "notes": ["⚠️ **`Negative Prompt` はこの経路では床にならない**（§18 の前書き）。**ゆえにこれは肯定形で負う** "
              "— §16 `MUST NOT` と、`Master Prompt` 自身の散文が負う。",
              "⚠️ **弱い守りである。記録として書く。** ⚠️ **そしてこの1本の弱さは `s01` と同じ種類である**"
              "——**日没の海を求められた生成器は、そこに人を置く。**"]},
   {"name": "The shore, the water and the last of the light",
    "ref": "**この1本の主題である。** ⚠️ **参照は `ledger.locations.岸` の `geography` と `states.日没` である**"
           "——**この1本は、`s01` が立てた岸を、最後にもう一度写す。**",
    "appearance": "**水際の線、粗い暗い砂、濡れた小石、流木の一本、乾いた海藻、そして海。** "
                  "⚠️ **形はすべて在るが、後半ではどれも判別できない**——"
                  "**この1本の後半で、物は「無くなる」のではなく「見えなくなる」。**",
    "behavior": "**波が同じ間隔で寄せて返す**。**波の白だけが明るく、砂と海藻と小石はもう見えない。** "
                "⚠️ **海はこの1本では一つの色になり、そして水平線だけが残る。** "
                "⚠️ **環境は何にも反応しない**——**この1本には、反応すべき相手が居ない。**",
    "continuity": "**Must preserve** — 水際の線、水平線の高さ、砂の粗さ、潅木のbank、そして `s01` が立てた"
                  "低いカメラの高さ。**May change** — 光、色、波の白の位置、そして画の中の岸の大きさ。"
                  "⚠️ **水平線はこの作品のどのショットでも水平である**（`岸.geography`）。",
    "notes": ["⚠️ **この1本のカメラは `s01` の高さである**——`s01` の §15 が「岸のショットはこの高さから撮る」と"
              "書いている。**この1本はその最後の使用である。**",
              "⚠️ **この1本に、この経路が最も自然に足すものは舟である。** 禁制は §16 と `Master Prompt` の"
              "散文の両方に在る。"]},
 ],

 "environment": {
   "location": "`岸` — **この作品の地面であり、`s01` が立てた岸である。** ⚠️ **この1本はそこを離れる**"
               "——**カメラが下がり、島の地面が画面の外へ出る。****しかし場所は変わらない。退くのは画だけである。**",
   "elements": "水際の線、粗い暗い砂、濡れた小石、流木の一本、乾いた海藻、低い湿った岩、"
               "そして向こうの海と水平線。⚠️ **範囲を広げない** — **この1本は岸と海で閉じる。**"
               "**森も洞も、この区間にはまだ来ない。**",
   "behavior": "**波は `s01` と同じ間隔で寄せて返す**——**この1本のあいだ、一度も速さを変えない。** "
               "乾いた海藻はこの1本では動かない（`s01` では一度転がった）。"
               "⚠️ **風の出来事は無い** — 空気は動くが、天候は変わらない。"
               "⚠️ **環境は画面に反応しない**——**人の居ない1本に、反応は要らない。**",
 },

 "objects": [
   "**波の白**, the crests of a low swell — **この1本のあいだ、ただ一つ明るいもの。** "
   "**最後まで光を手放さない**——**レベルが下がるにつれて、白だけが残る。**",
   "**砂**, coarse and dark, in the near ground — **この1本の前半ではまだ判別できる。**"
   "**中盤で黒くなる**——**無くなるのではなく、見えなくなる。**",
   "**小石**, flat, wet, dark, a handful at the waterline — **`s01` と同じ位置に同じものがある。**",
   "**乾いた海藻**, above the waterline — ⚠️ **この1本では動かない。**",
   "**流木**, one bare limb, sea-worn, at the edge of the frame — **形を持つ最後の物であり、"
   "カメラが下がるときに最初に画面から出る。**",
   "⚠️ **この作品の小道具は4つだけであり**（`ledger.props`）、**そのどれもこの1本には来ない** "
   "— 舟・帆・斧・太陽の牛は、まだ作られていないか、まだ記憶にすら無い。",
 ],

 "ref_character": "**この1本に人物は一人も居ない**——**ゆえに添付しない。** `男` も `女神` も、"
                  "**この1本には四つの姿のどれとしても現れない。** 参照集合が挙げているのは "
                  "`岸`・`岸.geography`・`岸.states.日没` の3鍵である。",

 "narrative": {
   "core": "**光が消え、島が画面から出る** — 誰も居ない島が、その最後の姿を渡す。",
   "beginning": "**日の道が砕け、海が一つの色になる。****岸はまだ判別できる。**",
   "turn": "**砂が黒くなる。****波の白だけが残る。**",
   "peak": "**水平線だけが細く残る。** カメラは下がりつづけ、**岸の地面が画面の下へ出ていく。**",
   "pull": "⚠️ **カメラが下がりきり、島が画面から出るのが、切れ目のコマである。**"
           "**その直後に声が入る**——**この1本は、歌の1コマ手前で終わる。**",
 },

 "beats": None,  # filled from the shot record by gen.py

 "density": "**Uneven, and weighted to the last four and a half seconds.** 最初の3秒は**光が消えること**に払われ、"
            "次の4秒は**砂が黒くなること**に払われ、**最後の4.4秒がこの1本の出来事である**"
            "——**カメラが下がりきり、島が画面から出る。** "
            "⚠️ **`held` を1つも使わない。** ⚠️ **そしてこの1本は、この作品で最も強い音の事象の前に終わる**"
            "——**ビートの末尾が `dense` であるのは、変化が切れ目のコマで終わるからである。**",

 "actions": [
   ("ACT_FADE", "日の道が水面に一本の帯として残っている。",
    "**日の道が消え、海が一色になる**——**岸はまだ判別できる。**"),
   ("ACT_BLACKEN", "砂と小石と海藻に、まだ形が読める。",
    "**砂が黒くなり、判別できなくなる**——**波の白だけが明るい。**"),
   ("ACT_NARROW", "帯は広く、水平線はまだ太い。",
    "**水平線だけが細く残る**——**画面の大半が、色を持たない水になる。**"),
   ("ACT_WITHDRAW", "岸の地面が画面の下のほうにまだ入っている。",
    "**カメラが下がりきり、島の地面が画面から出る****——そしてそれが、この1本の切れ目のコマである。**"),
 ],

 "camera": {
   "language": "Third person, **at the shore's own height** — the lens at a standing person's chest, "
               "the height `s01` established for the shore. ⚠️ **この1本はその高さの最後の使用者である。**",
   "events": "One event only. `0-11.399s` — **a slow continuous pull-back at a rate that does not "
             "change, still withdrawing on the last frame of the take.** ⚠️ **動機は島から離れることではなく、"
             "「島を置くこと」である**——**この1本は、島を画面の外へ置いて、歌に渡す。** "
             "⚠️ **この1本は一度も切らない。**",
   "behavior": "**The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly** "
               "— a slow backward travel with the low frequency of a rig that has mass, and it does not "
               "wobble. ⚠️ **止めない。** **変化は切れ目のコマで終わり、カメラはそのコマでもまだ動いている。** "
               "No handheld, no whip, no shake, no snap zoom, no rack focus, no unnatural rotation, "
               "and **no unmotivated move.** ⚠️ **構図は変わる側である**——**岸が画面から出て、"
               "水面と水平線だけが残る。**",
 },

 "motion": {
   "subject": "**波の白だけが明るい。** 砂、海藻、小石はもう見えない。"
              "⚠️ **この1本の主題の運動は「光が引くこと」である**——**波は動きつづけるが、"
              "動いていることが見えなくなる。**",
   "object": "**波が寄せて返る** — 同じ間隔で、一度も速さを変えずに。**白だけが残る。** "
             "⚠️ **岩は動かず、海藻もこの1本では動かない。** ⚠️ **この1本に動く物は無い**"
             "——**動くのは水と光だけである。**",
   "environment": "**日が沈みきり、届く光が減る。** **海は一つの色になる。** "
                  "⚠️ **風の出来事は無い**——**空気は動くが、天候は変わらない。** "
                  "⚠️ **音の側の環境は水と風だけである**（§14）。",
   "weight": "**水は重く、その上の光は重さを持たない。** ⚠️ **二つの速さが違うことが、この1本の内容である**"
             "——**波は重く寄せ、光は速く引く。**",
   "inertia": "**波は行き過ぎてから戻る。** ⚠️ **光は行き過ぎない**——**光は一方向にだけ引き、戻らない。** "
              "⚠️ **この1本の中に、戻る変化は一つも無い。**",
   "acceleration": "**加速しない。** ⚠️ **波の間隔も、カメラの引きも、一定である**——"
                   "**日の沈みが加速しないのと同じである。**",
   "fluidity": "Continuous; no snap, no held cel, no stutter. ⚠️ **この11.399秒に、止まったフレームは一つも無い**"
               "——**カメラは最後のコマまで下がりつづけ、水は一度も止まらない。**",
   "impact": "**無い。** ⚠️ **この1本に衝撃は一つも無い**——**あるのは音の側で、そしてそれはこの1本の外にある。**",
 },

 "emotion": {
   "arc": "**人が現れる前の、最後の一枚。** そして**それが「始まる直前」に見えること**が、この1本の感情である。"
          "⚠️ **誰も写さないのに、待っているように見える**——**それを作るのは、光が減りつづけることである。**",
   "events": "⚠️ **この1本の出来事は、表情でも、まなざしでもない。****島が画面から出ることである。** "
             "**そしてこの1本は、それを名指さない**——**置いて、終わるだけである。**",
 },

 "lighting": {
   "base": "The sun's own light, already below the horizon's work, the last of it raking across the "
           "water; no fill, no artificial source, and a flare only while any of it is in frame. "
           "⚠️ **この1本の光源は一つであり、それは日である。** ⚠️ **この1本に専用の光は無い**"
           "——**人を別に照らす理由が、この1本には無い。**",
   "events": "**One, and it runs the whole shot.** 日の道が砕けて消え、**画面のレベルが一方向にだけ下がり、"
             "岸が黒くなり、そして水平線の細い線だけが残る。** ⚠️ **その線が最後まで消えないのが、切れ目のコマである。** "
             "⚠️ **光源は動かない**——**様式カードの逐語:「The grade holds for the whole shot — a colour "
             "temperature that swings is a different style.」**",
 },

 "audio": {
   "dialogue": K.NO_DIALOGUE,
   "sfx": "**水と、小石と、低い風。** ⚠️ **この1本に人の音は一つも無い。** "
          "⚠️ **そして声の不在は、置かれているのであって、省かれていない**——"
          "**この1本の最後のコマの次に、声が入る。**",
   "music": K.NO_MUSIC + " ⚠️ **この1本では、それがどこよりも効く: 主題歌『永遠より遠い』の最初の声が、"
            "この1本の切れ目の次のコマに来る**（52.899秒）——**生成された音床は、"
            "この1本の末尾で、来るはずの声と衝突する。**",
   "environment": "日没の岸、島の水際。**水、石、そしてほぼ暗くなった空気。** ⚠️ **呼ぶ声は無い**"
                  "——**この1本には、呼ぶ者も、呼ばれる者も居ない。**",
 },

 "continuity": {
   "identity": "⚠️ **この1本に人物が居ないので、人物の同一性は掛からない。** "
               "**掛かるのは場所の同一性である**——**水際の線、水平線の高さ、砂の粗さ、潅木のbank、"
               "そして `s01` が立てたカメラの高さである。** ⚠️ **`s04`〜`s08` はその高さから撮られる**"
               "（`s01` の §15）。**この1本が、その高さを最後に使う。**",
   "spatial": "岸は画面の手前を左から右へ走り、海はその向こうにある。**カメラは水際の高さに立ち、"
              "ゆっくり後ろへ下がる。** ⚠️ **退いても、場所は変わらない**"
              "——**変わるのは画の中の岸の大きさだけである。**",
   "temporal": "一日の終わり、**`s01`・`s05`〜`s08` と同じ夕べである**——**この1本はそのうちで最も遅い。** "
               "⚠️ **この1本は、この作品で最初の人間の直前である**"
               "——**画の中に日付を与えるものは何も無い。**",
   "visual": "**The film grain and the rejection of the painted surface — no painterly stroke, no airbrush, no plastic surface, no CGI look, no illustration — are the same in all thirty-four shots. The palette is the shot's own, and so is the light.** ⚠️ **光は日の光だけである。**"
             "⚠️ **この1本は `video-spec` を名乗る**——**文法を持たない。**"
             "**ゆえに §15 が免除するものは一つも無い。**",
   "motion": "Full animation, not limited. **光が引き、水が寄せ、カメラが下がる。** "
             "⚠️ **カメラは1回だけ動き、切れ目のコマでもまだ動いている。**",
   "sound": "**水、石、低い風。****音楽なし。言葉なし。** ⚠️ **声はこの1本の中に無い**"
            "——**それは次のコマに、主題歌として入る。**",
 },

 "must_not": K.must_not_common(has_man=False, goddess_extra=(
     "**この1本に人は一人も居ないので、女神の禁制はここで最も素の形で掛かる**——"
     "**誰も居ない場所に、人の形を作らない。**")) + [
   "**No person in frame at all** — no face, no figure, no silhouette, no hand, no distant point that "
   "could be a person. ⚠️ **この1本の最初の禁制であり、この経路でいちばん弱い守りである** — §18 を見る。",
   "**Nothing is placed in this frame** — no object brought in, no prop arranged, no fire lit, no "
   "footprint, no mark of a hand.",
   "⚠️ **No second light** — **人を別に照らす光も、岸を照らす専用の光も無い。**",
 ],

 "must": [
   "**The light finishes going out and the island leaves the frame** — the path breaks, the sand goes "
   "black, the horizon is a thin line, **and the camera has drawn back until the island's own ground is "
   "out of the picture.**",
   "**No person appears, at any distance, in any focus.**",
   "⚠️ **The change is still in progress on the last frame** — the island is still leaving the frame "
   "when the take ends.",
   "⚠️ **There is no still frame in this take.** Water and camera move in every frame; a frozen picture "
   "is a failure of this section.",
   "**The camera does not stop before the cut.**",
   "⚠️ **The shot ends one frame before the voice** — **この1本は、歌の最初の声を受け取らない。**",
   "**The shore is `s01`'s shore, from `s01`'s camera height** — this shot does not build a second place.",
 ],

 "prefer": "The horizon low in frame and level; the white of the crests carried as the one bright "
           "value to the end; the near ground readable early and unreadable late; the frame emptying as "
           "the camera withdraws.",

 "allow": "A lens flare while any of the light is still in frame; the swell's white breaking unevenly "
          "across the frame; the dry weed left where it is.",

 "priorities": [
   "**Nobody in the frame.** ⚠️ **ここに人が入れば、`s05` が最初の人間でなくなる**"
   "——**この作品の順序は、島が先で人が後である。****この経路が最も弱い危険である。**",
   "**The light goes out and is still going out at the cut** — the last frame is not a settled dark. "
   "⚠️ **切れる前に変化が終わった画は、歌に止まった一枚を渡す。**",
   "**The island leaves the frame on the last frame** — **それが、この1本の出来事である。**",
   "**It is water, not a surface** — the swell has mass, and the light on it does not.",
   "**One pull-back, motivated by placing the island** — no cut, no second setup.",
   "**No boat on the water, and nothing made in the frame.** ⚠️ **この経路の出力は「海と夕日」を"
   "求められると、たいてい舟を置く。**",
   "**The shore is `s01`'s shore, from `s01`'s height** — this shot is the last user of that height.",
   "**Japanese is what this work speaks** — named in §18, even though this shot holds no words.",
   "Everything else.",
 ],

 "preamble_tail": K.preamble_tail(
   "⚠️ **この1本は `video-spec` を名乗る。****ゆえにここに足すものは無い**——"
   "**この形式は文法を持たず、その禁制（`no uniform pacing` ほか）は §16 に在って、ここには無い。** "
   "**だから34本の `Negative Prompt` は、`s01` と同じ一行である。**"),

 "master": (
   "An 11.399-second cinematic take (16:9) of a bronze-age island shore at the end of the day, one clip, "
   "one continuous take, one change: **the light finishes going out and the island leaves the frame.** "
   "**There is no person in this shot at any distance or in any focus — the frame holds water, shingle "
   "and the last of the light, and nothing else.** The light is the sun's own and it is going; the "
   "palette moves in one direction only and does not come back up.\n\n"
   "0-2.998s: **the path of light breaks up and goes out.** The sea goes to one colour; the shore can "
   "still be told from the water; the swell is already arriving at the rate it will keep.\n"
   "2.998-6.999s: **the sand and the stones go black.** Only the white of the crests stays bright; the "
   "near ground stops being legible without going anywhere.\n"
   "6.999-11.399s: **only the horizon is left, a thin pale line.** The camera draws back until the "
   "island's own ground has fallen out of the picture — **and the take ends on that frame, one frame "
   "before the voice enters.**\n\n"
   "**The camera draws back slowly at a rate that does not change and is still drawing back on the last "
   "frame; it never cuts and never stops.** **No person is in this frame at any distance or in any "
   "focus — no figure, no silhouette, no hand.** **No boat, no ship, no hull, no sail, no other vessel "
   "is anywhere in this frame, and nothing built stands in it either: no jetty, no wall, no path, no "
   "fire.** **This is a bronze-age shore before classical Greece: rough stone, coarse sand, sea-worn "
   "wood.** **This is a Japanese work.** No subtitles. No BGM.\n"
   "(One continuous take, one change: the light goes out and the island leaves the frame.)"),

 "visual_scene": (
   "A bronze-age Mediterranean island shore at the end of the day, photographed as a film frame, with "
   "the light almost gone: coarse dark sand and wet shingle with sea-worn driftwood, dry weed and small "
   "flat stones; low wet rocks at the waterline; a rising bank of dense low scrub behind, with no trees "
   "and no path; the sea filling the frame beyond, the horizon level and unbroken and low in the "
   "picture. **The white of the swell's crests is the one bright value in the frame** and the near "
   "ground is going to a black that holds no colour."),

 "visual_meta": K.VISUAL_META.replace(
   "Coarse wool with visible fibre and a worn shoulder seam; skin roughened and marked", (
   "Dry weed that is fibrous and salt-bleached").strip()) + (
   " ⚠️ **No skin and no cloth are anywhere in this frame — this shot holds no person.**"),

 "motion_prompt": (
   "Full animation, not limited. **The sea is the mover**: long low swells arriving and going back on an "
   "interval that does not change across the whole take, the surface never still and never repeating a "
   "shape. **The light on the water is what is going out** — the band breaks, the surface takes one "
   "colour, and the level keeps falling in one direction with nothing coming back up. **The camera draws "
   "back slowly and does not stop; it is still withdrawing on the last frame.** Water has mass and "
   "overshoots and returns; the light does not. **The dry weed does not move in this shot.** No motion "
   "blur smears, no stutter, no floaty weightless motion, no static frames — **water and camera move in "
   "every frame of the take.**"),

 "camera_prompt": (
   "Third person, **at the shore's own height** — the lens at a standing person's chest, the height `s01` "
   "established for the shore. One event only: **a slow continuous pull-back, at a rate that does not "
   "change, still running on the last frame of the take.** ⚠️ **The move is motivated: it places the "
   "island — it is not a retreat from it.** ⚠️ **The style permits a dolly, a crane and a Steadicam, and "
   "this shot spends the dolly** — a slow backward travel with the low frequency of a rig that has mass. "
   "⚠️ **Do not stop before the cut.** ⚠️ **The composition is allowed to change** — the island's ground "
   "leaves the frame and the water and the horizon are what remain. No handheld, no whip, no shake, no "
   "snap zoom, no rack focus, no unnatural rotation, no unmotivated move."),

 "audio_prompt": K.AUDIO_PROMPT % (
   "Sound effects, nothing mixed forward: **water arriving and going back, small stones turning over in "
   "the wash, and a low wind.** ⚠️ **There is no human sound in this shot at all** — and **the absence "
   "of a voice is placed rather than left out: the work's first voice arrives on the next frame, and "
   "this shot must not reach for it.**"),

 "resolved_references": "`REF_STYLE (cinematic-still, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE "
                        "(bible.yaml ＋ ledger.yaml, CRITICAL)`。⚠️ **添付は0点である**（裁定②。そしてこの経路は"
                        "既定で何も添付しない）。⚠️ **この1本に人物は居ないので、同一性の塊は §18 に入らない**"
                        "——**入るのは場所の記述である。**",
 "camera_events_count": "1 event as listed in §10",
 "audio_events": "no dialogue ／ water ＋ stones ＋ low wind ＋ one placed absence ／ no music",
 "unresolved": [
   "⚠️ **この1本が「島を置く」と読まれるかどうかは、機械には測れない。** **測れるのは、"
   "カメラが切れ目のコマでもまだ下がっていることまでである**（§16 `MUST`）。**そこから先は、見た者が言う。**",
   "⚠️ **`cinematic-still` のレターボックス。** 様式カードは 2.39:1 の画面を指定する。"
   "この作品は `16:9` を固定する（裁定④）ので、**黒帯が入るかどうかは、この仕様からは決まらない。**",
   "⚠️ **「島が画面から出る」の読み。****記録は「カメラが下がりきり、島が画面から出る」と書く**"
   "——**この仕様は「岸の地面が画面の下へ出る」と読んだ。****退く画で島が小さくなって終わる読みもある。**"
   "⚠️ **どちらが正しいかは、著者が見て決める。**",
 ],
 "risks": [
   "**人が置かれる。** ⚠️ **この1本のいちばん高い危険である**——**入れば `s05` が最初の人間でなくなる。**"
   "禁制は §16 と `Master Prompt` の散文の両方に在る。",
   "**舟が置かれる。** ⚠️ 「海と夕日」を求められた生成器が最初に足すものであり、この作品は全ショットで禁じている。",
   "**カットが入り、二本の画になる。** ⚠️ **この1本の変化は「島が画面から出ること」であり、"
   "切れれば二本目の画になる。**",
   "**光が先に尽きる。** 変化は最後の4.4秒に属する——**0秒で真っ暗なら、この1本は渡すものを渡していない。**",
   "**カメラが止まる。** ⚠️ **切れ目のコマでもまだ下がっていることが、この1本の `MUST` である。**",
   "**水が軽くなる** — ガラスのような均一な面は、この作品の物理（水は重く、その上の光は重くない）を失う。",
   "**照明が平板になる。** ⚠️ **平板なテレビ照明は様式自身の第一の禁制である**——"
   "低い光の岸の画で最も起きやすい。",
 ],
}

if __name__ == "__main__":
    print("s04 content OK — keys:", len(C))
