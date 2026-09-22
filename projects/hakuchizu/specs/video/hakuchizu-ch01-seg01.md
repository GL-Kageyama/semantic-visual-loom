# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 1/11 / 6s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg01.md`）。**両者は別のものを指す**
——動画は §1–20 を持ち、画像は7欄と `Negative` を持つ（`L18`）。
⚠️ **画像が先である**（著者の指示 2026-09-22）。**この仕様は、10枚のキー画像を見たあとに回される。**

⚠️ **この1本の変化は「色が消えること」である。** 草稿 L1——戻りかけの色が、朝のうちに戻る。
⚠️ **動くのは色であって、町ではない。** 誰も立たない。**立たないことが、この1本の仕事である**
（`forbidden_set` に `灯` が在る——この1本は人物を持たない唯一の4本のひとつ）。
⚠️ **これは世界の法が最初に実演される1本である**——「**戻りかけの色ほど早く消える**」
（`bible.world.rules` の1行目）。**観客はここで、この町の法を1つだけ覚える。**

---

# 1. VIDEO

- Duration: `6s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the last of the colour leaves the street and the street is white.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- **「戻りかけの色ほど早く消える。」** 濃く塗った朱や群青ほど、夜までかかって薄くなる。
  ⚠️ **この1本が実演するのは、この1行だけである。** 他の6つの法は、まだ画面に来ていない。
- 白は音を持たない（S09 が実演する）。
- 白の下には、人がいた気配が透けている（S03・S04・S10 が使う）。**この1本には、まだその形が無い**
  ——**この1本は、白がまだ何も透かしていない最後の1本である。**
- 思い出したぶんだけ、白のなかから色が立ち上がる（S08）。
- 覚えることは、払うことである（S10・S11）。
- 数は町を戻さない（S05・S10）。
- 置いた色は、もう白に戻らない（S11）。

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る**——独立した生成は記憶を共有しない。
- Color Language: この1本だけが、四色のうち二色を持ち、しかも**その二色が減っていく**。
  黄土と金彩は**まだ1つも現れていない**——ゆえにこの6秒の色数は、この作品で最も少ない。
- Texture: 荒い紙。**濃く塗ったところほど、遅く白へ戻る**——ゆえに画面には、
  塗りの厚さの地図が一瞬だけ現れる。
- Rendering: 薄塗りのウォッシュが、**紙に吸われて輪郭を残さずに消える**。
  ⚠️ **ぼかさない。** この様式の色は**置かれたもの**である。
- Visual Density: 低い。**この6秒は、この作品で最も少ないものが写っている6秒である。**
- Time: `夜明け前`
- Atmosphere: 音の無い通り。**朝は、まだ明るさでしか来ていない。**

# 3. SUBJECTS

## The Remaining Colour

- Reference: （参照画像なし——`attached` に色の鍵は無い。色は `bible` が持つ）
- Appearance: 屋根と戸の上に残った**朱と群青の名残**。**面ではなく、塗り残しである**——
  濃く塗ったところが、まだ薄くなりきらずに残っている。黄土と金彩は無い。
- Behavior: **薄くなり、消える。** 動かない、流れない、にじまない——
  **上から紙が戻ってくる。** 朱が先に消え、群青が後を追う。
- Continuity Requirements: 四色は `bible.world.visual_language.art_direction` が決める。
  **この1本に人物は要らない。** 参照画像は1枚も添付しない。

# 4. ENVIRONMENT

- Location: `通り`（`hakuchizu-mionomachi-street` の意図）
- Environment Elements: 石畳、閉じた雨戸の並び、二階のベランダ、屋根。**店はまだ画に入らない。**
- Environmental Behavior: 何も動かない。埃も、布も、水も、まだこの1本には無い。
  **朝の光だけが、動かずに濃くなっていく。**

# 5. OBJECTS

- `通り` — 白紙に戻った下町の通り。**この1本では、屋根と戸の上の色だけが「物」である。**
- 暖簾・暖簾の店の前・白い形・水の跡・薬缶 — **どれもこの1本には無い。**
  ⚠️ **無いことは、まだ書いていないことであると同時に、この1本に出さないことである**（§16）。

# 6. REFERENCES

- REF_LOCATION: `hakuchizu-mionomachi-street` (MEDIUM — 意図であって資産ではない)
- REF_GEOGRAPHY: `通り.geography` (LOW — 順路は §7 と §15 が持つ)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — この1本は色の系列の起点である)
- ⚠️ **`REF_CHARACTER` を書かない。** この1本に人物が居ないので、**名乗る相手が無い**
  （`L31` は `REF_STYLE` だけを読む。この行は人向けである）。

# 7. NARRATIVE

- Core Event: 通りから、最後の色が消える。
- Beginning: 屋根と戸の上に、戻りかけの朱と群青がまだ残っている。**朱のほうが、もう薄い。**
- Turn: **朱の名残が消える。** 消えた場所には、何も置かれない。
- Peak: 群青の名残が消える。通りは白だけになる。
- Pull: 朝の光が白の上に薄く積もりはじめ、**白は光を受けても白のままである。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `held` — 屋根と戸の上に、戻りかけの色がまだある。
    **朱が先に薄くなっている**——草稿 L1「戻りかけの色ほど早く消えて、濃く塗った朱や群青ほど、夜までかかって薄くなる」。
  - BEAT 2 `2-4s` — density: `sparse` — 朱の名残が消える。**消えた場所には、もう何も無い。**
  - BEAT 3 `4-6s` — density: `sparse` — 群青の名残が消える。通りは白だけになる。朝の光が積もりはじめる。
- Temporal Density: **3つの拍は、どれも静かである。** 不均等は「濃さ」ではなく「残っている色の量」にある
  ——**最初の2秒だけが、まだ何かを見せている。**

# 9. ACTION

- `ACT_THIN` — Before: 朱と群青の名残が屋根と戸の上にある。After: 朱が先に、群青が後に、無くなる。
  Simultaneous With: 朝の光の到着（`ACT_SETTLE`）。Causes: 夜が明けること。
- `ACT_SETTLE` — Before: 白は薄暗い。After: 朝の光が白の上に薄く積もり、**白は白のままである。**
  Causes: 朝。⚠️ **光は影を作らない**——この世界に方向性の光は無い。

# 10. CAMERA

- Camera Language: 三人称、通りの幅で、立っている人の目の高さ。**通りそのものが画角である。**
  ⚠️ **方向性の光が無いので、この画には「どちらから来た光」も無い。**
- Camera Events: `0-2s` 屋根と戸の上に留まる。`2-4s` 朱が消えるが、**カメラは色を追わない。**
  `4-6s` 白へ留まり、そのまま終わる。
- Camera Behavior: **6秒のあいだ、一度も動かない。** 手ぶれも、寄りも、引きも無い。
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。** 使うなら山（S08）である。
  ⚠️ **辞退は辞退として書く**（`skills/staging/SKILL.md`）——**禁じるのではなく、認めて断る。**

# 11. MOTION

## Subject Motion

**色は動かない。色は、そこに在ることをやめる。** 薄くなることは、
**その上に紙が戻ってくること**であって、色がどこかへ行くことではない——
ゆえにこの1本の運動は、**面が縮むこと**としてだけ現れる。**中心からではなく、縁から。**

## Object Motion

**町は動かない。** 戸は開かない、人は歩かない、布は掛かっていない。
**この6秒で位置を変えるものは、画面に1つも無い。**

## Environmental Motion

**朝の光が、動かずに濃くなる。** ⚠️ **影は伸びない**——`art_direction` が
`no directional light` を定めているので、**光の到着は明るさの変化としてのみ現れる。**
埃も、風も、まだこの1本には無い。

## Physical Characteristics

- Weight: 色は**モノとして載っている**（この様式の絵の具は不透明である）。ゆえに
  **薄くなる速さは、塗りの厚さに比例する**——濃いところが最後まで残る。
- Inertia: 消えはじめた色は、**途中で止まらない。** 速まらないが、戻りもしない。
- Acceleration: 無い。**この1本に加速は1つも無い**——`sparse` と `held` の差は、
  動きの速さではなく**残っている色の量**である。
- Fluidity: 流れない。**にじまない。** 水彩のぼかしは、この様式の外にある。
- Impact: 無い。**この1本は、何も起こらないことが出来事である。**

# 12. EMOTION

- Emotional Arc: 何も起こらない → 気づくと、色が1つ減っている → 通りのほうが、静かになっている。
- Emotional Events: **最後の群青が消えた瞬間。** 強度は低い——**この1本は、感情を立てない。**

# 13. LIGHTING

- Base Lighting: 夜明け前。**方向を持たない、平らな薄明**。影は落ちない。
- Lighting Events: `4-6s` 朝の光が到着し、白の上がわずかに明るくなる。**光源は動かない**——
  この世界の光は**どこからも来ない。**

# 14. AUDIO

- Dialogue: 無し。**この作品は台詞もナレーションも持たない。**
- Sound Effects: **無し。** ⚠️ **これは省略ではない**——この1本は、まだ**音が戻っていない側**である
  （`bible.world.rules`「白は音を持たない」。音が戻るのは S09 である）。
- Music: 無し。**BGM はこの作品の床で禁じられている**（§16）。
- Environment: 通りの、何も鳴っていない空気。
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**——「**空欄は中立ではない**」
  （`bible.language` の註。実測: 発話のある動画に中国語の字幕が焼かれた）。
  **話さないことと、言語を持たないことは違う。**

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Identity: **人物は1人も居ない。** ゆえに人物の同一性は、この1本では何も拘束しない。
- Spatial: 通りは1つの場所である。**この1本は通りを出ない**（路地・広場・橋は撮らない）。
- Temporal: 夜明け前。**この1本の6秒で、朝は「明るさ」だけを返す。**
- Visual: 四色の地図が、二色に減る。**黄土と金彩はまだ現れない。**
- Motion: **動くのは色だけである。** 町も、光も、埃も動かない。
- Sound: 無音。⚠️ **「静か」ではなく「無い」である**——S09 で音が戻ったとき、
  **この無音が効く。**

# 16. CONSTRAINTS

## MUST NOT

- No person in frame. No second person. No figure of any kind.
- No cat in frame — 草稿 L5「猫はもういない」。**もう居ないものを、白の下から出さない。**
- No noren in frame. No shop front in frame. **この1本は、店の前にまだ着いていない。**
- No house numbers, no numerals, no numbers of any kind.
- No light shaft, no sunbeam, no lens flare — `no directional light` の実装である。
- No legible text of any kind, anywhere.
- No water mark on the paving, no bicycle shape, no laundry shape — **白の下の気配は、まだ透けていない。**
- No lettering on the shutters, no lettering on the doors.
- **No fully-painted flat vermilion cloth** — 朱はまだ**戻っていない**。この禁止は S01–S07 が持つ。

## MUST

- Full animation, not limited: **色は6秒のあいだ、動かずに減りつづける。**
- 朱が先に消え、群青が後を追う（`bible.world.rules` の1行目）。
- 消えた場所には**何も置かない**——跡も、輪郭も、影も。
- 朝の光は、白を**白のまま**にする。白は照らない。

## PREFER

- 屋根と戸の上の色が、**塗りの厚さの地図**として読めること。
- 最初の2秒で、朱がもう薄いことが読めること。

## ALLOW

- 石畳の上に、白の濃淡がわずかに残ること（紙のムラとして）。

# 17. GENERATION PRIORITIES

1. **色は消えるのであって、動かない。** ⚠️ **最も起きやすい失敗は「色が流れる・にじむ・飛ぶ」である**
   ——この様式の色は置かれた物であり、**紙が上から戻る**（`motion.law`）。
2. **誰も居ない。** 人物を1人置けば、この1本は「情景」ではなく「人物の1本」になる。
3. **白は照らない。** 光沢はこの様式の外にある（`gouache-abstract` の `avoid`）。
4. **黄土と金彩を出さない。** この1本に在るのは朱と群青だけである。
5. **数えるものを置かない。** 数字・番号・刻みは、S05 で「数は戻らない」を撮るために取ってある。
6. **カメラを動かさない。** 動かせば、山で使うはずの「一度」がここで消える。
7. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 6-second continuous cinematic take (16:9) of the last of the colour leaving a street that is already going white, one clip. Beats, deliberately uneven: [0-2s] the remains of vermilion and ultramarine still lying on the roofs and doors, the vermilion already the thinner of the two; [2-4s] the vermilion goes, and nothing is placed where it was — no trace, no outline, no shadow; [4-6s] the ultramarine goes and the street is white only, while morning light settles thinly on the white and the white stays white. The core beat — the vermilion going — holds the largest share. The town does not move and no figure is in the street; the colour thins and stops being there, and it never flows, bleeds or blows away. The story's four colours have only two of themselves in this frame, and ochre and gold gilt have not arrived. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on a street that is white everywhere and holds no colour at all, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. A downtown street returned to blank paper: stone paving, a row of closed shutters, second-floor verandas, roofs. The only colour left is the remains of vermilion and ultramarine on the roofs and doors, thin and uneven, thicker where it was laid thicker. Vermilion and ultramarine foremost and nothing else; ochre and gold gilt are not in this frame. Flat, even, directionless light with no cast shadow and no light shaft. No person, no second person, no cat, no noren, no shop front, no house numbers, no lettering, no light shaft, no sunbeam, no lens flare, no water mark on the paving, no bicycle shape, no laundry shape, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. The subject is the colour itself, and the colour does not travel: it thins where it lies and stops being there, the paper coming back over it from above, edge inward, thickest last. The vermilion goes first and the ultramarine follows, and where each has gone nothing is placed — no trace, no outline, no shadow, no mark of departure. The town does not move: no door opens, no shutter moves, no figure steps, no cloth hangs anywhere in the frame. The morning light arrives without moving and without casting; no shadow lengthens or shortens, because this world has no directional light. No flow, no bleed, no bloom, no blur, no drip, no fade to grey, no colour draining downward, no colour flying away, no morphing shapes, no motion blur, no stutter, no held frames.

## Camera Prompt

Third-person, at the width of the street and the height of a person standing in it, the street itself filling the frame. The camera holds still for the whole six seconds: no push, no pull, no pan, no tilt, no rack focus, no handheld, no shake. [0-2s] holding on the roofs and the doors where the colour still is. [2-4s] still holding as the vermilion goes, and the camera does not follow the colour. [4-6s] still holding on the white to the end. The style allows one drift; this shot spends none — the one drift in this work is spent later, and spending it here would cost the shot that needs it. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. No sound effects: nothing in this shot makes a sound, and this is not an omission — the white has no sound in it yet, and sound returns in a later shot of the same sequence, which is why this one must be empty. No ambient bed beyond the still air of a street with nobody in it. Music: none, and no swell, no sting, no melody. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no fully-painted flat vermilion cloth, no person in frame, no cat in frame, no noren in frame, no shop front in frame, no house numbers, no light shaft, no sunbeam, no lens flare

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. Here the revising hand is the paper itself: it comes back over the colour and the colour is covered, not thinned. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither. The palette stays restrained throughout. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg01-6s-01`
- Segment ID: `01-1`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `6s`
- References: `REF_LOCATION (hakuchizu-mionomachi-street, MEDIUM) ／ REF_GEOGRAPHY (通り.geography, LOW) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: **無し**（`shots/hakuchizu-ch01-seg01.yaml` の `attached` が空である。⚠️ **この1本は画像を1枚も添付しない**——
  `key_image` は在るが、**添付の集合は記録の側が決める**）
- Temporal Structure: `3 beats, NON_UNIFORM — held 2s / sparse 2s / sparse 2s. The core = BEAT 2 at 2-4s (33%)`
- Camera Events: `0 events. One continuous take, camera still for the whole clip`
- Action Events: `ACT_THIN → ACT_SETTLE`
- Audio Events: `no dialogue ／ no sound effects ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。

## Anticipated risks (to check in the first generation)

- **⚠️ 色が流れる。** これがこの1本の最も起きやすい失敗である。**消えることは、動くことではない**——
  紙が上から戻るのである。**にじみを作れば、この1本は水彩の1本になり、様式が割れる。**
- **⚠️ 人物が入る。** 通りを撮れば、モデルは歩く人を置きたがる。**この1本に人は居ない**——
  S02 が「人が入ってくる1本」であり、**この2本は対である。**
- **⚠️ 店が入る。** 「下町の通り」と言えば、モデルはのれんの店を置く。**この1本はまだ店の前に着いていない。**
- **⚠️ 黄土と金彩が入る。** 四色は作品のものであり、モデルは4つとも置きたがる。
  **この1本に在るのは朱と群青だけである**（`bible.world.visual_language.art_direction` の「only as small accents」は、
  **そもそもこの1本には適用されない**——アクセントがまだ来ていない）。
- **⚠️ 光が方向を持つ。** 朝の光は、モデルに影を落とさせる。**この世界に方向性の光は無い。**
- **⚠️ 音が入る。** 音の指定は §14 が「無し」と言うが、**モデルは環境音を足したがる。**
