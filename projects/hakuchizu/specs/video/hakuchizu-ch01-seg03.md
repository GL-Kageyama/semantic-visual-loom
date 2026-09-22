# ═══ 演出要約 ════════════════════════════════════
# 『白地図』第1章「暖簾」 / 質感 / motion —— 水の跡が乾き、乾いた境だけが残る
#
#   石畳の水の跡が乾いていく。水が減り、乾いた境だけが、かすかに濃く残る。
#   乾く速さは一定である——7秒のあいだ、誰も急がない。カメラは下を向き、境の線を追う。
#   撒いた者は最後まで出ない。人も音も風も無い。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 3/11 / 7s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg03.md`）。
⚠️ **この1本は、この作品で唯一「人が一度も画に入らない」1本である**——
**S01 は人が想定されず、S05 は人が遠くに居る。この1本は、人が居たことだけが写る。**

⚠️ **この1本の変化は「水の跡が、乾いていくこと」である。**
⚠️ **この1本は「白の下には人がいた気配が透けている」の最初の実演である**
（`bible.world.rules` の3行目）。**水を撒いた者は画に居ない**——
**居ないのに、その形が残っている。** ⚠️ **これがこの作品の「白地図」の意味である。**
⚠️ **ゆえにこの1本に人物は要らない。** 参照画像は1枚も添付しない——
**人が居ないことを、参照画像の不足で説明しない**（§19）。
⚠️ **水は、色ではない。** ⚠️ **この1本は、四色のうち一色も使わない**（S02 と同じ）。

---

# 1. VIDEO

- Duration: `7s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the trace of water on the paving thins and goes, and the shape of where it lay is all that was ever in the frame.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01）。
- 白は音を持たない（S09）。
- **「白の下には、人がいた気配が透けている。」** ⚠️ **この1本が実演するのはこの行である。**
  **見えない人が、形だけを残す**——ゆえにこの7秒の主役は**人影ではなく、水の輪郭**である。
- 思い出したぶんだけ、白のなかから色が立ち上がる（S08）。
- 覚えることは、払うことである（S10・S11）。
- 数は町を戻さない（S05・S10）。
- 置いた色は、もう白に戻らない（S11）。⚠️ **水は色ではない**——ゆえにこの1本は、この法の外にある。

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
- Color Language: **一色も無い。** 水の跡は**白よりわずかに沈んだ白**であって、色ではない——
  ⚠️ **ゆえにこの1本は、`no saturated or vivid color` が最も効きにくい1本である。**
  **代わりに必要なのは、白の濃淡の階調である。**
- Texture: **この1本の主題は、まさに質感である。** 荒い紙の上に、
  **水が入ったところだけ紙が沈んでいる**——乾くにつれ、**沈みが戻ってくる。**
- Rendering: ⚠️ **光沢を描かない。** `no gloss on the paving`・`no wet reflection`・
  `no mirror-like paving` がこの1本の法である——**この作品の水は、空を映さない。**
- Visual Density: **低い。** 画面にあるのは石畳と、白と、その上のわずかな濃淡だけである。
- Time: `朝`
- Atmosphere: 人は居ない。**だが、居た。**

# 3. SUBJECTS

⚠️ **この1本に人物は居ない。** `Subject` は**水の跡そのもの**である。

## 水の跡

- Reference: `props.水の跡`（`attached` は `水の跡.appearance` と `水の跡.negative` を持つ）
- Appearance: **石畳の上の、白よりわずかに沈んだ面。** 半円を描いて撒かれた形が、
  **扇の縁のような輪郭**として残っている。**濃いところと薄いところがある**——
  撒いた人の手の癖が、そのまま濃淡になっている。
- Behavior: **乾く。** 縁から内側へ向かって、**沈みが戻ってくる。**
  速くならない、遅くならない。
- Continuity Requirements: ⚠️ **撒いた人を描かない**（`no figure sprinkling water`）。
  ⚠️ **これは「居ない」ではなく「もう居ない」である**——
  **この区別が、この1本の全部である。**

# 4. ENVIRONMENT

- Location: `通り`（`hakuchizu-mionomachi-street` の意図）
- Environment Elements: 石畳、閉じた雨戸の並び、二階のベランダ、屋根。**店はまだ画に入らない。**
- Environmental Behavior: **無い。** 動くのは水の跡の乾きだけである。
  ⚠️ **雨を降らせない。** ⚠️ **水滴を空気中に置かない**（`no droplets in the air`）——
  **この水は、すでに地面にある。**

# 5. OBJECTS

- `水の跡` — この1本の唯一の主題である。
- `通り` — 水の跡を載せている面。
- 暖簾・暖簾の店の前・白い形・薬缶 — **どれもこの1本には無い。**

# 6. REFERENCES

- REF_LOCATION: `hakuchizu-mionomachi-street` (MEDIUM)
- REF_GEOGRAPHY: `通り.geography` (LOW)
- REF_PROP: `水の跡.appearance` (HIGH — この1本の主題である)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — 水の跡とその禁止は台帳が持つ)
- ⚠️ **`REF_CHARACTER` を書かない。** この1本に人物が居ないので、**名乗る相手が無い。**

# 7. NARRATIVE

- Core Event: 水の跡が、乾く。
- Beginning: 石畳に、半円の水の跡がある。**濃いところと薄いところがある。**
- Turn: **縁が、内側へ退きはじめる。** ⚠️ **水は流れない**——**蒸れて、戻る。**
- Peak: 跡の真ん中だけが残る。**そこが、いちばん最後まで残る。**
- Pull: 跡が消える。**石畳には、何も無い。** ⚠️ **残るのは、乾いた白だけである。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — 水の跡がある。**輪郭が読める。**
  - BEAT 2 `2-5s` — density: `held` — **縁が内側へ退く。** この3秒が核心である。
  - BEAT 3 `5-7s` — density: `sparse` — 真ん中が消える。**石畳は白だけになる。**
- Temporal Density: ⚠️ **`held` の3秒は「何も起こらない」に近い**——
  **乾きは、気づくことでしか見えない。** ゆえにこの3秒は、
  **輪郭の位置がわずかに動くことだけ**が情報である。

# 9. ACTION

- `ACT_DRY` — Before: 水の跡が石畳の上にある。After: 跡は無く、石畳は白い。
  Causes: 朝。⚠️ **人が乾かすのではない。**
- ⚠️ **この1本には `ACT_SPRINKLE` が無い。** 撒く者は**すでに居ない**——
  `ledger.props.水の跡.negative` が `no figure sprinkling water` を持つのは、
  **この1本が「誰が撒いたか」を答えないためである。**

# 10. CAMERA

- Camera Language: 三人称、通りの幅で、**しゃがんだ人の高さまで低い**——
  ⚠️ **この1本だけは、石畳を見る画角である**（他の10本は立っている人の高さである）。
  **低いことは、この1本の内容である**——**人が居ないので、目線も無い。**
- Camera Events: `0-2s` 水の跡を捉える。`2-5s` 縁が退くが、**カメラは縁を追わない。**
  `5-7s` 白い石畳に留まって終わる。
- Camera Behavior: **7秒のあいだ、一度も動かない。** 寄りも、引きも、パンも無い。
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。** 使うなら山（S08）である。
  ⚠️ **辞退は辞退として書く**（`skills/staging/SKILL.md`）。

# 11. MOTION

## Subject Motion

**水の跡の輪郭が、内側へ退く。** ⚠️ **面が縮むのであって、水が動くのではない**——
この区別は S01 の色と同じ法である（**「減る」は「行く」ではない**）。
**退く速さは、跡の濃さに反比例する**——薄いところから先に乾く。

## Object Motion

**石畳は動かない。** 雨戸は開かない、ベランダの物干しは空である。
⚠️ **この1本に、洗濯物はまだ掛かっていない**——掛かるのは S10 である。

## Environmental Motion

**無い。** 埃も、風も、鳥も無い。⚠️ **光は S01 で到着し終えている。**

## Physical Characteristics

- Weight: **水は重さを持たない。** 持っているのは**紙の沈み**だけである。
- Inertia: 乾きは**途中で止まらない。** 速まらないが、戻りもしない。
- Acceleration: 無い。⚠️ **`sparse` と `held` の差は、動きの速さではない。**
- Fluidity: ⚠️ **流れない。** 広がらない、にじまない、はみ出さない——
  `no falling water`・`no splash`・`no puddle` がこの1本の法である。
- Impact: 無い。

# 12. EMOTION

- Emotional Arc: 何かがある → **それは、誰かが居たことの形である** → 乾く。**何も言わない。**
- Emotional Events: **輪郭が退きはじめた瞬間**（`2-5s` のあいだ）。
  ⚠️ **この1本の感情は「懐かしさ」ではない。** **「気配」である**——
  **人は一度も現れず、一度も語られない。**

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。** 影は落ちない。
- Lighting Events: **無い。** ⚠️ **乾きを光で説明しない**——**明るさで乾きを見せれば、
  この1本は「時間の経過」を光で語る1本になる。この作品はそれをしない。**

# 14. AUDIO

- Dialogue: 無し。
- Sound Effects: **無し。** ⚠️ **水の音を足さない**——**この1本の水は、もう音を立てない。**
- Music: 無し。
- Environment: 通りの空気。**人の居ない、朝の屋外。**
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: **人物は1人も居ない。** ⚠️ **ゆえにこの1本の「同一性」は、水の跡の形である。**
- Spatial: 通りは1つの場所である。**この1本は通りを出ない。**
- Temporal: 朝。S02 の直後である。**灯はもう通りすぎている**——ゆえにここに人は居ない。
  ⚠️ **この前後関係が、この1本に人を置かない理由である**（順序は §7・`unit` が持つ）。
- Visual: 一色も出さない。
- Motion: 動くのは乾きだけである。**カメラは動かない。**
- Sound: 無音。

# 16. CONSTRAINTS

## MUST NOT

- No person in frame. **No figure sprinkling water.** **この1本の法である。**
- No cat in frame — 草稿 L5「猫はもういない」。
- No rain. No falling water. No splash. **No droplets in the air** — 水はすでに地面にある。
- No wet reflection. No mirror-like paving. **No puddle. No gloss on the paving** ——
  ⚠️ **この作品の水は、空を映さない。**
- No noren in frame. No shop front in frame.
- No laundry shape. No bicycle shape.
- No house numbers, no numerals, no numbers.
- No legible text of any kind.
- **No fully-painted flat vermilion cloth** — 朱はまだ戻っていない。この禁止は S01–S07 が持つ。

## MUST

- Full animation, not limited: **乾きは7秒のあいだ止まらない。**
- **輪郭が内側へ退くこと**——面が縮むのであって、水が動くのではない。
- 白は**白のままである**。水の跡は、白よりわずかに沈んだ白である。
- 石畳の質感が読めること——**この1本は `質感` の1本である。**

## PREFER

- 跡の濃淡が、**撒いた手の癖として読める**こと。
- 退く速さが、**濃さに反比例している**こと。

## ALLOW

- 紙のムラとして、乾いたあとに**わずかな濃淡が残る**こと。

# 17. GENERATION PRIORITIES

1. **撒く人を描かない。** ⚠️ **最も起きやすい失敗である。** 「水の跡」と言えば、
   モデルは**撒いている人**か**撒いた後の人**を置く。**この1本に人は居ない。**
2. **水を光らせない。** 濡れた石畳は、モデルが最も反射させたがるものである。
   **この作品の水は、沈みであって、鏡ではない。**
3. **水を動かさない。** 流れ、広がり、はね、滴る——**どれもこの1本に無い。**
   **乾きは「減ること」であって「動くこと」ではない。**
4. **色を出さない。** この1本は白の濃淡だけである。
5. **カメラを動かさない。**
6. **雨を降らせない。** 「朝の通り」と言えば、モデルは雨上がりを作る。**この水は撒き水である。**
7. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 7-second continuous cinematic take (16:9) of a trace of water drying on a stone paving that has already gone white, one clip. Beats, deliberately uneven: [0-2s] the half-round trace is lying on the paving and its outline can be read, darker where the hand that threw it laid more and lighter where it laid less; [2-5s] the outline withdraws inward, thinning from the edges first, the shallower parts going before the deeper ones; [5-7s] the middle of the trace goes, and the paving is only white again. The core beat — the outline withdrawing — holds the largest share, three of the seven seconds, and nothing else in the frame changes while it withdraws. No person is in this frame and nobody threw the water: what is in the frame is only the shape of where someone was, and that is the whole subject. The water is not a colour: it is white sunk very slightly below white, and it never runs, spreads, splashes, drips, shines or reflects. No rain, no falling water, no droplets in the air, no puddle, no mirror-like paving, no gloss. The story's four colours are all absent here and the frame holds one white with a little depth in it. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on paving that is white and dry everywhere, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. A downtown street returned to blank paper, seen low, close to the ground: stone paving filling the frame, a row of closed shutters and second-floor verandas behind it. The trace of thrown water lies on the paving as white sunk slightly below white, half-round, uneven in depth, thicker along one arc where the hand laid more and thin at the edges, with a readable outline and no colour in it at all. No gloss, no reflection, no mirror-like surface, no puddle, no droplets in the air, no rain, no splash, no falling water. No person, no figure, no hands, no second person, no cat, no noren, no shop front, no laundry on the veranda, no bicycle, no house numbers, no lettering, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. The subject is the trace of water and it does not travel: the outline withdraws inward, the shallower areas going before the deeper ones, the paper rising back where the water was, until only the deepest middle is left and then that goes too. The water never runs, never spreads outward, never beads, never drips, never splashes and never flows along a joint in the paving. Nothing else in the frame moves: no figure enters, no hand is shown, no door opens, no shutter moves, no laundry stirs on the veranda, and the light does not shift. The drying is slow and even and does not accelerate or pause. No morphing shapes, no motion blur, no stutter, no held frames, no flow or bloom or bleed in the pigment, and no fade to grey.

## Camera Prompt

Third-person, low, at the height of a person crouching to look at the ground rather than standing, the stone paving filling the frame, the street's shutters and verandas behind it. The camera holds still for the whole seven seconds: no push, no pull, no pan, no tilt, no rack focus, no handheld, no shake, and no move to follow the withdrawing outline. [0-2s] holding on the trace where it lies. [2-5s] still holding as the outline withdraws, and the camera does not follow it inward. [5-7s] still holding on the white dry paving to the end. The style allows one drift; this shot spends none — the one drift in this work is spent later, and spending it here would cost the shot that needs it. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. No sound effects: no water sound, no dripping, no trickle, no splash, no hiss of evaporation, no footsteps, no door, no shutter, no wind, no bird, no traffic. The water in this frame is already on the ground and has finished making whatever sound it made, so making a sound for it here would put an event into a shot whose subject is the absence of the person who made it. No ambient bed beyond the still air of a street with nobody in it. Music: none, and no swell, no sting, no melody. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no fully-painted flat vermilion cloth, no person in frame, no cat in frame, no figure sprinkling water, no rain, no falling water, no splash, no droplets in the air, no wet reflection, no mirror-like paving, no puddle, no gloss on the paving

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. Here the revision is a covering: the paper comes back over the water's ground one pass at a time, and the uneven edge left behind is the record of the hand. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither. The palette stays restrained throughout, which here means one white with a little depth in it and nothing else. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg03-7s-01`
- Segment ID: `01-3`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `7s`
- References: `REF_LOCATION (hakuchizu-mionomachi-street, MEDIUM) ／ REF_GEOGRAPHY (通り.geography, LOW) ／ REF_PROP (水の跡.appearance, HIGH) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: **無し**（`shots/hakuchizu-ch01-seg03.yaml` の `attached` が空である。
  ⚠️ **人物を1枚も添付しない**——**人が居ないことを、参照画像の不足で説明しない**）
- Temporal Structure: `3 beats, NON_UNIFORM — sparse 2s / held 3s / sparse 2s. The core = BEAT 2 at 2-5s (43%)`
- Camera Events: `0 events. One continuous take, camera still and low for the whole clip`
- Action Events: `ACT_DRY`
- Audio Events: `no dialogue ／ no sound effects ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。

## Anticipated risks (to check in the first generation)

- **⚠️ 人が現れる。** これがこの1本の最も起きやすい失敗である（**しかも最も壊れる**）。
  「水の跡」は、モデルにとって**動作の残り**である——**ゆえに動作の主を置きたがる。**
- **⚠️ 水が光る。** 濡れた石畳は鏡になる。**この作品の水は、空を映さない。**
- **⚠️ 水が流れる。** 乾きを「水が引いていくこと」として描けば、この1本は別の1本になる。
- **⚠️ 雨が降る。** 「朝の濡れた通り」は、この作品では**雨上がりではない。**
- **⚠️ 色が入る。** 一色も要らない。
- **⚠️ 目線が上がる。** この1本だけは**低い画角である**——
  立った高さで撮れば、この1本は「通りの1本」になり、S02 と見分けがつかなくなる。
