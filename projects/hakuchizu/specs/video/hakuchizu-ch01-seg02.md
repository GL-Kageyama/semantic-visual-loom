# ═══ 演出要約 ════════════════════════════════════
# 『白地図』第1章「暖簾」 / 運動 / motion —— 足音が白を踏み、生まれた影がもう消えている
#
#   足音が白を踏み、生まれた影が、次の一歩が来る前に消えている。
#   画面には常に影がひとつ以下しか無い——8秒かけて、その速さを観客の身体に入れる。
#   誰の顔も出さない。出るのは白と、足音と、影だけである。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 2/11 / 8s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg02.md`）。
⚠️ **この1本は、人が画に入ってくる1本である**（S11 は人が画から出ていく1本である）。

⚠️ **この1本の変化は「白い通りに、影がひとつ増えること」である。**
⚠️ **影が先である。** 草稿は人物ではなく**影**を先に置く——ゆえにこの1本は、
**「誰かが来た」ではなく「白に何かが落ちた」**として始まる。
⚠️ **顔を描かない。** これは `bible.constants.顔` と `ledger.characters.灯.identity` が定めている
——**ゆえにこの1本は、人物を「後ろ姿と輪郭と影」として扱う最初の1本である。**
⚠️ **この1本のカメラは、影を追わない。** 影が入ってきても、カメラは動かない——
**動かせば、S08 のために取ってある「一度」がここで消える。**

---

# 1. VIDEO

- Duration: `8s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: one shadow arrives on the white street and then holds, and the white around it does not take colour.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01 が実演した）。
- **白は音を持たない**（S09 が実演する）。⚠️ **この1本は、その手前である**——
  **足音は鳴ってよい。だが、この1本は足音を主役にしない**（§14）。
- **白の下には、人がいた気配が透けている**（S03・S04・S10 が使う）。
  ⚠️ **この1本は、その気配ではなく、まだ生きている人が歩いてくる1本である。**
- 思い出したぶんだけ、白のなかから色が立ち上がる（S08）。
- 覚えることは、払うことである（S10・S11）。
- 数は町を戻さない（S05・S10）。
- 置いた色は、もう白に戻らない（S11）。

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
- Color Language: **この1本には、まだ色が無い。** 四色のうち一色も現れない——
  ⚠️ **ゆえに、この1本の画は白と黒に近い。** 色が戻るのは S08 である。
- Texture: 荒い紙。**影は、紙の上に置かれた一筆である。**
- Rendering: 影は**輪郭を持つ**——`art_direction` が `no spatial illusion` を定めているので、
  影は**光学的な影ではなく、色の一筆**として置かれる。⚠️ **ぼかさない。**
- Visual Density: 低い→中。**2-5秒のあいだ、画面は「影が置かれていること」だけを写す。**
- Time: `朝`
- Atmosphere: 白い通りに、朝の光と、ひとつの影。

# 3. SUBJECTS

## 灯

- Reference: `灯.identity` — **ただし参照画像は `attached` に従う**（この1本は `灯.identity` を持つ）
- Appearance: 後ろ姿。**背と、輪郭と、影。** ⚠️ **顔は描かない**（`bible.constants.顔`——
  「顔を描くと、その人物が誰であるかが確定してしまう」）。**歩く人の影が、先に画へ入る。**
- Behavior: **歩いてくる。** 通りを渡り、通りすぎる。**立ち止まらない。**
  見ることはしない——**この1本の人物は、まだ何も見ていない。**
- Continuity Requirements: ⚠️ **顔を描かないことは、この1本で最も壊れやすい。**
  モデルは後ろ姿を描いても、**振り返らせて顔を出したがる**（§16・§20）。

## The Shadow

- Appearance: **紙の上に置かれた、輪郭を持つ一筆。** 長い。**平たい。**
  ⚠️ **柔らかい写真の影ではない**——`gouache-abstract` の `no photorealism` がここで効く。
- Behavior: **画に入り、置かれ、そのまま在る。** 動くのは**歩みのぶんだけ**である。
- Continuity Requirements: ⚠️ **影はひとつだけである**（`ledger.characters.灯`——二人目を置かない）。

# 4. ENVIRONMENT

- Location: `通り`（`hakuchizu-mionomachi-street` の意図）
- Environment Elements: 石畳、閉じた雨戸の並び、二階のベランダ、屋根。**店はまだ画に入らない。**
- Environmental Behavior: 何も動かない。**動くのは影だけである。**

# 5. OBJECTS

- `通り` — 白紙に戻った下町の通り。**この1本の「物」は、影が載る地面そのものである。**
- 暖簾・暖簾の店の前・白い形・水の跡・薬缶 — **どれもこの1本には無い。**

# 6. REFERENCES

- REF_LOCATION: `hakuchizu-mionomachi-street` (MEDIUM)
- REF_GEOGRAPHY: `通り.geography` (LOW)
- REF_CHARACTER: `灯.identity` (HIGH — 後ろ姿と輪郭だけである)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — 影がひとつであることを `灯` が持つ)

# 7. NARRATIVE

- Core Event: 白い通りに、影がひとつ入ってくる。
- Beginning: 通りは白い。**何も無い。**
- Turn: **影が画に入る。** ⚠️ **人が先ではない**——影が先である。
- Peak: 影が通りを渡り、置かれる。**白は、影を受けても白のままである。**
- Pull: 影が通りすぎ、**白には何も残らない。** 跡も、色も。

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — 白い通り。**まだ何も無い。**
  - BEAT 2 `2-5s` — density: `held` — **影が入り、渡り、置かれる。** この3秒が核心である。
  - BEAT 3 `5-8s` — density: `sparse` — 影が通りすぎる。**白は何も保たない。**
- Temporal Density: **核心の3秒は「動いている」のに `held` である**——
  ⚠️ **`held` は「静止」ではなく「密度が保たれること」である**（`bible` の `beats` の註）。
  影が渡っているあいだ、**画面の情報量は増えない。**

# 9. ACTION

- `ACT_ENTER` — Before: 通りは白く、何も無い。After: ひとつの影が画のなかに入っている。
  Causes: 誰かが歩いてくること。⚠️ **人物より影が先に読める。**
- `ACT_CROSS` — Before: 影が画の縁にある。After: 影が通りを渡り、白の上に置かれている。
  Simultaneous With: `ACT_ENTER`。⚠️ **影は地面を滑らない**——足が動くぶんだけ動く。
- `ACT_PASS` — Before: 影が画のなかにある。After: 影が画を出る。**白には何も残らない。**
  ⚠️ **置いた色は、もう白に戻らない**（7つ目の法）——**だが影は色ではない。**
  ゆえにこの1本は、**7つ目の法の手前**である。

# 10. CAMERA

- Camera Language: 三人称、通りの幅で、立っている人の目の高さ。**通りそのものが画角である。**
- Camera Events: `0-2s` 白い通りに留まる。`2-5s` 影が入ってくるが、**カメラは影を追わない。**
  `5-8s` 影が出ていく。カメラは留まったまま終わる。
- Camera Behavior: **8秒のあいだ、一度も動かない。** パンも、寄りも、引きも無い。
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。** 使うなら山（S08）である。
  ⚠️ **辞退は辞退として書く**（`skills/staging/SKILL.md`）。

# 11. MOTION

## Subject Motion

**影は、足のぶんだけ動く。** ⚠️ **滑らない。** 影が先に伸びて、人がそれに追いつく、
という見え方が正しい——ゆえにこの1本の運動は、**影と輪郭のあいだの、わずかなずれ**として現れる。

## Object Motion

**町は動かない。** 戸は開かない、布は掛かっていない、水はまだ無い。
**この8秒で位置を変えるものは、影と人の歩みだけである。**

## Environmental Motion

**無い。** 埃も、風も、鳥も、この1本には無い。⚠️ **朝の光は、S01 で到着し終えている**——
この1本の光は**もう動かない。**

## Physical Characteristics

- Weight: 影は**紙の上の一筆である**——ゆえに重さを持たない。人が持つのは、歩みの重さだけである。
- Inertia: 歩みは**一定である。** 速まらない、遅くならない。
- Acceleration: 無い。
- Fluidity: **滑らかでない。** この様式の運動は**手が形へ戻ること**である——
  ゆえに影の輪郭は、**わずかに揺れながら置き直される**（`Style Motion`）。
- Impact: 無い。**白は、影を受けても何も失わない。**

# 12. EMOTION

- Emotional Arc: 何も無い → **白に、ひとつの影** → 影が行き、**何も残らない**。
- Emotional Events: **影が置かれた瞬間**（`2-5s` のあいだ）。強度は低い——
  ⚠️ **この1本は、人物に感情を与えない。** 見ているのは観客だけである。

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。** ⚠️ `art_direction` が
  `no directional light` を定めているので、**影は光から出た影ではない。**
  ゆえに影は**「光が作ったもの」ではなく「置かれたもの」として描かれる。**
- Lighting Events: **無い。** この1本のあいだ、光は動かない。

# 14. AUDIO

- Dialogue: 無し。
- Sound Effects: **足音のみ。** ⚠️ **足音は鳴ってよい**——この世界の禁は
  「白は音を持たない」であって「音が無い」ではない。**音が戻るのは S09 である。**
  ⚠️ **ゆえに足音は、控えめである**——**主役にしない。**
- Music: 無し。
- Environment: 通りの空気。**車も、鳥も、人も、他には居ない。**
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: **灯——後ろ姿、輪郭、影。顔は描かない。**
  ⚠️ **この1本で確立した「顔を描かない」が、以後10本すべてを拘束する。**
- Spatial: 通りは1つの場所である。**この1本は通りを出ない。**
- Temporal: 朝。S01 の直後である。**色はもう消えている。**
- Visual: 四色のうち**一色も出さない。**
- Motion: 動くのは影と歩みだけである。**カメラは動かない。**
- Sound: 足音のみ。

# 16. CONSTRAINTS

## MUST NOT

- No second person. **影はひとつだけである**——`ledger.characters.灯`。
- No second shadow. No more than one shadow in frame.
- No visible face on the figure. **振り返らせない。**
- No blurred shadow. No soft photographic shadow — 影は**置かれた一筆である。**
- No cat in frame — 草稿 L5「猫はもういない」。
- No house numbers, no numerals, no numbers.
- No noren in frame. No shop front in frame — **この1本はまだ店の前に着いていない。**
- No water mark, no bicycle shape, no laundry shape.
- **No fully-painted flat vermilion cloth** — 朱はまだ戻っていない。この禁止は S01–S07 が持つ。
- No legible text of any kind.

## MUST

- Full animation, not limited.
- **影が先に読める。** 人が先に読めてはならない。
- 影は**輪郭を持つ**——ぼけない。
- 白は、影を受けても**白のままである。**

## PREFER

- 影の輪郭が、**紙の上の一筆として置かれている**こと。
- 歩みが**一定である**こと。

## ALLOW

- 影の輪郭が、`Style Motion` のとおり**わずかに置き直される**こと。

# 17. GENERATION PRIORITIES

1. **顔を描かない。** ⚠️ **最も起きやすい失敗である。** 後ろ姿を描かせても、モデルは
   横顔や、首の角度で顔を覗かせる。**この1本で崩れれば、以後10本が崩れる。**
2. **影をひとつにする。** 二人目を置けば、この作品の支払いの構造（`灯` がひとりであること）が崩れる。
3. **カメラを動かさない。** 追えば、山の「一度」が消える。
4. **色を出さない。** この1本は白と、影の濃さだけである。
5. **影をぼかさない。** 写真の影にすれば、様式が割れる。
6. **足音を主役にしない。**
7. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

An 8-second continuous cinematic take (16:9) of one shadow arriving on a white street and then going on, one clip. Beats, deliberately uneven: [0-2s] the street is white and empty and nothing is in it; [2-5s] a single shadow enters the frame before the person does, crosses the street and is laid on the white, and the white does not take any colour from it; [5-8s] the shadow leaves the frame and nothing is left behind — no trace, no colour, no mark. The core beat — the shadow crossing and lying on the white — holds the largest share, three of the eight seconds, and the density of the frame does not increase while it crosses. The figure is seen from behind only: back, outline and shadow, and the face is never drawn and the figure never turns. The shadow is a single stroke of pigment laid on the paper, holding a hard edge, not soft and not photographic. The town does not move. The story's four colours are all absent from this frame; the shot is white and the darkness of one shadow. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on a white street with nothing left in it, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. A downtown street returned to blank paper: stone paving, a row of closed shutters, second-floor verandas, roofs. One figure seen from behind, walking, carrying no colour: back, outline and one shadow, the face not drawn at all and not turned toward the viewer. The shadow is one stroke of pigment laid on the paper with a hard edge and an uneven surface, long and flat, and it is the only dark thing in the frame. Nothing else in the street is coloured: no vermilion, no ultramarine, no ochre and no gold gilt anywhere. No second person, no second shadow, no cat, no noren, no shop front, no house numbers, no lettering, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. One shadow enters the frame slightly ahead of the feet that cast it and the outline of the figure follows it in; the shadow crosses the paving and comes to lie on the white, and it slides at the pace of the walk and never ahead of it and never behind it. The walk is even: no acceleration, no pause, no hesitation, no glance back. The shadow does not blur, does not soften at the edges, does not flicker and does not stretch beyond the walking. The town does not move: no door opens, no shutter moves, no second figure steps anywhere in the frame, and the light does not shift. Nothing is left behind where the shadow passed — no trace, no mark, no colour, no change in the white. No morphing shapes, no motion blur, no stutter, no held frames, no flow or bleed in the pigment.

## Camera Prompt

Third-person, at the width of the street and the height of a person standing in it, the street itself filling the frame. The camera holds still for the whole eight seconds: no push, no pull, no pan, no tilt, no truck, no rack focus, no handheld, no shake. [0-2s] holding on the empty white street. [2-5s] still holding as the shadow enters and crosses, and the camera does not follow the shadow or the figure — they move through a frame that does not move. [5-8s] still holding until the frame is empty again. The style allows one drift; this shot spends none — the one drift in this work is spent later, and spending it here would cost the shot that needs it. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. Sound effects: footsteps only, at a low level, kept under the image and never made the subject of the shot — this world's law is that the white holds no sound, and sound returns in a later shot of the same sequence, so this shot must not spend it here. No other sound effects: no door, no shutter, no shutter rattle, no wind, no bird, no distant traffic, no cloth. No ambient bed beyond the still air of a street with nobody else in it. Music: none, and no swell, no sting, no melody. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no fully-painted flat vermilion cloth, no second person, no second shadow, no more than one shadow in frame, no visible face on the figure, no blurred shadow, no soft photographic shadow, no cat in frame, no house numbers

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. The walk here is a hand laying one stroke after another along the ground, and the shadow keeps the uneven edge of the hand that laid it. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither. The palette stays restrained throughout. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg02-8s-01`
- Segment ID: `01-2`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `8s`
- References: `REF_LOCATION (hakuchizu-mionomachi-street, MEDIUM) ／ REF_GEOGRAPHY (通り.geography, LOW) ／ REF_CHARACTER (灯.identity, HIGH) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: `灯.identity`・`灯.negatives`・`通り.base`（`shots/hakuchizu-ch01-seg02.yaml` の `attached` に従う）
- Temporal Structure: `3 beats, NON_UNIFORM — sparse 2s / held 3s / sparse 3s. The core = BEAT 2 at 2-5s (38%)`
- Camera Events: `0 events. One continuous take, camera still for the whole clip`
- Action Events: `ACT_ENTER → ACT_CROSS → ACT_PASS`
- Audio Events: `no dialogue ／ footsteps only ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。

## ⚠️ `L14` ——「宣言を超えた区間」（−5）

⚠️ **この仕様は `L14` に当たる。** 台帳はこの位置に変化点を宣言していない。
**`L14` の言い分は正しい**——**このショットで、この作品の動画の §18 は、戻らない仕方で変わった。**
⚠️ **そしてその変化は、このショットの欠陥ではない。理由をここに書く**——`L14` 自身が
「`disclosure` に行を足すか、**足さない理由を記録に書く**」と求めている。

**この作品の動画の §18 Negative は、ショットごとに書かれている**
（49／49／52／50／49／56／56／72／72／72／72 節）。⚠️ **ひとつの集合の差分ではない。**
⚠️ **S08〜S11 の 72 は、2026-09-22 の魚の訂正のあとの数である**
（この4本が6節を同じ形で足した——`PLAN.md` §4-d）。
**各ショットが、その画に入りうるものだけを禁じる**——ゆえに画の内容が変われば、禁制も入れ替わる。
⚠️ **`L14` が咎めるのは、入れ替えのうち二度と戻らないものだけである**——
S02 が足す6節（`no blurred shadow` ほか）は、**すべて S03 で戻る。回転は鳴らない。**

| −5（消えた） | このショットにしか無い理由 |
|---|---|
| `no lens flare`／`no light shaft`／`no sunbeam` | **S01 は、空を見る唯一の1本である。** 主題は「色が引いて、光が平らになる」——**光源が画のなかにある。** S02 以後、画は地面と灯の後ろ姿へ降り、**光源は枠に入らない。** ⚠️ **同じ用は、全11本が持つ `no directional light`（`negative_base`）が負う**——**ゆえにこの3節は、S01 の言い換えである。著者は落としてもよい。** |
| `no noren in frame`／`no shop front in frame` | **S01 は、まだ店の前に着いていない1本である**（`PLAN.md` §1）。**暖簾と店の前は、S06 以後の主題である**——S06 以後、`no noren in frame` は**この作品が写すものを禁じる**ことになる。**ゆえにこの2節は、S01 だけのもので正しい。** |

⚠️ **足して数を減らさなかった。** この5節を S02 以後へ書き戻せば `L14` は静かになる——
**だが `no noren in frame` を書き戻すことは、この作品が写すものを禁じることである。**
**数を小さくすることは、欠陥を直すことではない。**

⚠️ **`disclosure` に行を足す道は取らない。** **このショットは開示の変化点ではない**——
台帳の開示点は S07・S08・S10・S11 にある。**嘘の行を足せば、`L7a` の前提が崩れる。**
⚠️ **S08 の変化だけは、台帳が宣言している**（`暖簾.朱: 戻った` ＋ `negative: changed`）。
**この位置が宣言されていないのは、開示ではないからである**——**台帳の書き漏らしではない。**
（S08 も `L14` の条件を満たしている——**＋10／−0**（2026-09-22 に数え直した。`PLAN.md` §4-d）。
**宣言が鳴りを止めている。**）

⚠️ **ゆえに残るのは、著者への問いである**——**この作品の動画の Negative は、一つの集合なのか**
（あるショットの集合を床として、以後の全ショットが持つのか）、**ショットごとに書かれるのか。**
⚠️ **この作品は「ショットごと」で書かれている**——`no person in frame` は S01・S03・S05 で真、
S02・S04・S06 以後は偽である。**「一つの集合」を選ぶなら、床と差分を設計し直すことになる。**
⚠️ **著者が決めるまで、この仕様は送らない。**

## Anticipated risks (to check in the first generation)

- **⚠️ 顔が出る。** この1本の最重要の失敗である。**`no fully rendered face for 灯` は
  `negative_base` の1行目である**——それでもモデルは横顔を作る。**最初のコマで確かめる。**
- **⚠️ 二人目が入る。** 「通り」と言えば、モデルは町の人を足す。**この作品に、灯以外の
  描かれた人物は居ない**（`ledger.characters.暖簾の店の主` も**顔を持たない**）。
- **⚠️ 影がぼける。** 写真の影にすれば、この作品は「白い街の写真」になる。
- **⚠️ 影が伸びる。** 方向性の光が無いので、**影は歩みのぶんだけである。**
  伸びる影は、S05 で「数は戻らない」を撮るために取ってある（`no lengthening shadows`）。
- **⚠️ 店が入る。** この1本はまだ店の前に着いていない。
- **⚠️ 色が入る。** 四色は作品のものであり、モデルは1つ置きたがる。**この1本は白と影だけである。**
