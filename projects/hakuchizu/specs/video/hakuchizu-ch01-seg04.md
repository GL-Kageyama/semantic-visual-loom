# ═══ 演出要約 ════════════════════════════════════
# 『白地図』第1章「暖簾」 / 所作 / motion —— 白い自転車の形を避け、歩く線がひとつ曲がる
#
#   灯の歩く線が、白い自転車の形の手前で一度だけ外へそれ、すぐ元へ戻る。
#   避けているあいだも歩調は落ちない。それる幅は、読める最小のぶんだけである。
#   自転車として見せない。灯は自転車を見ない——見なくても避けられることが、癖である。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 4/11 / 5s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg04.md`）。

⚠️ **この1本の変化は「避けること」ではない。** 変化は**線**である——
**灯の歩く線が、一点で曲がり、また戻る。**
⚠️ **「避けている」を撮れば、この1本は「障害物をよける人」の1本になる。**
**癖であること**は、**避けたあとに線が元へ戻ること**でしか出ない（草稿 L5「避けるのが癖になっていた」）。
⚠️ **この1本に `transformation` を使わない。** 線は置き換わるのではなく、**一度それて戻る**——
ゆえに基本的な映像化フォーマットで足りる（`video-spec`）。
⚠️ **この1本で、様式の「the revision stays visible」が初めて物語の意味を持つ。**
曲がった線は消えない——**ゆえに癖は、通りの側に蓄積する。**

---

# 1. VIDEO

- Duration: `5s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: 灯's walking line bends outward at one point and comes back, and the bend stays on the paper.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01）。
- 白は音を持たない（S09）。
- **白の下には、人がいた気配が透けている**（S03 が実演した）。
  ⚠️ **この1本は、その気配が「まだ使われている物」として画面に残っている1本である**——
  **自転車の形をした白**は、誰かが使っていた物の抜け殻である。
- 思い出したぶんだけ、白のなかから色が立ち上がる（S08）。
- 覚えることは、払うことである（S10・S11）。
- 数は町を戻さない（S05・S10）。
- 置いた色は、もう白に戻らない（S11）。
  ⚠️ **この1本は、この法の「線」版である**——**置かれた線は、消えない**（`motion.law`）。

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
- Color Language: **一色も無い。** ⚠️ **この1本に在るのは、白と、鉛筆の線と、白い形だけである。**
- Texture: 荒い紙。**灯の歩く線は、薄い鉛筆の線として紙の上に在る**——
  ⚠️ **絵の具ではない。** にじまない、太らない、盛り上がらない。
- Rendering: ⚠️ **線画だけの領域を作らないという註の、この作品での読み**（`PLAN.md` §1）。
  この1本には**白い面が3つある**——**通り・白い形・線**——
  **線だけの画面にはならない。**
- Visual Density: 低い。
- Time: `朝`
- Atmosphere: 白い通りに、白い自転車の形。**人は、それを見ない。**

# 3. SUBJECTS

## 灯の歩く線

- Reference: `灯.identity`（`attached` に従う）
- Appearance: **紙の上に置かれた、薄い鉛筆の線。** まっすぐである。
  一点で外へふくらみ、**すぐ戻る。** ⚠️ **線は消えない**——ふくらみは通りに残る。
- Behavior: **前に進む。** 速さは変わらない——**それるあいだも、歩調は落ちない。**
- Continuity Requirements: ⚠️ **線は鉛筆であって、絵の具ではない。**

## 灯

- Appearance: 後ろ姿。**背と、輪郭。** ⚠️ **顔は描かない**（`bible.constants.顔`）。
- Behavior: **歩く。** ⚠️ **白い形を見ない**——見なくても避けられることが、癖である。
- Continuity Requirements: ⚠️ **足元に影を置かない**（S02 の主題である）。

## 白い自転車の形

- Reference: `props.白い形.appearance`（`attached` に従う）
- Appearance: **自転車の形をした白。** ⚠️ **自転車として描かない**——
  **輪郭線を引かない、スポークを描かない、機械の細部を描かない**（§16）。
  草稿 L5「いまは**自転車の形をした白**が壁にもたれて立っている」。
- Behavior: **動かない。** 壁にもたれたままである。
- Continuity Requirements: ⚠️ **影も光も持たない**（`no shadow cast by the white shape`）。

# 4. ENVIRONMENT

- Location: `通り`（`hakuchizu-mionomachi-street` の意図）
- Environment Elements: 石畳、閉じた雨戸の並び。**店はまだ画に入らない。**
- Environmental Behavior: **無い。**

# 5. OBJECTS

- `白い形` — この1本の障害物であり、**かつて自転車だったもの**である。
- `通り` — 線が置かれる面。
- 暖簾・暖簾の店の前・水の跡・薬缶 — **どれもこの1本には無い。**

# 6. REFERENCES

- REF_LOCATION: `hakuchizu-mionomachi-street` (MEDIUM)
- REF_GEOGRAPHY: `通り.geography` (LOW)
- REF_CHARACTER: `灯.identity` (HIGH)
- REF_PROP: `白い形.appearance` (HIGH — この1本の相手である)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — 白い形の禁止は台帳が持つ)

# 7. NARRATIVE

- Core Event: 灯の歩く線が、白い自転車の形を避ける。
- Beginning: 線はまっすぐである。**白い自転車の形が、進路の先にある。**
- Turn: **線が一点で外へそれる。** 幅は**狭い**——**避けていることが読める最小の幅**である。
- Peak: ⚠️ **この1本に山は無い。** それた線が、**そのまま戻る。**
- Pull: 線はまたまっすぐになる。**白の上には、ふくらみが1つ残っている。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — 白い通り。閉じた雨戸の前に、白い自転車の形。**線はまっすぐ。**
  - BEAT 2 `2-3s` — density: `held` — **線が外へそれる。** ⚠️ **この1秒がこの1本の核である。**
  - BEAT 3 `3-5s` — density: `sparse` — 線が戻る。**ためらわない**——`癖` は、ためらわない。
- Temporal Density: ⚠️ **核が、この1本で最も短い拍である。** 5秒のうちの1秒——
  **前後の2秒ずつは、この1秒を効かせるために置かれている。**
  ⚠️ **核が最長でないことは事故ではない**（`beats` がそう記録している）。
  **この1本の不均等は「長い平坦・短い屈折・長い平坦」である。**

# 9. ACTION

- `ACT_WALK` — Before: 線はまっすぐで、白い形の手前にある。After: 線は外へそれ、白い形の横を通る。
  Causes: **癖**——意識を要さない。⚠️ **灯は白い形を見ていない。**
- `ACT_RETURN` — Before: 線は外にふくらんでいる。After: 線はまたまっすぐである。
  **ふくらみだけが、白の上に残っている。**
  ⚠️ **戻る速さが、癖を語る。** ためらえば「気にしている人」になる。

# 10. CAMERA

- Camera Language: 三人称、通りと平行に、**立っている人の高さ**——
  ⚠️ **ただし石畳に大きな面積を割く**（S03 ほど低くはない。**あの低さは S03 のものである**）。
  **線が読めること**が、この1本の画角の条件である。
- Camera Events: `0-2s` 白い形と、まっすぐな線に留まる。`2-3s` 線がそれるが、
  **カメラは線を追わない。** `3-5s` 線が戻る。**留まったまま終わる。**
- Camera Behavior: **5秒のあいだ、一度も動かない。**
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。** 使うなら山（S08）である。
  ⚠️ **辞退は辞退として書く**（`skills/staging/SKILL.md`）。

# 11. MOTION

## Subject Motion

**線は、前へ進む。** 一点で外へふくらみ、**すぐ戻る。** ⚠️ **ふくらみは、置かれたまま残る**——
`gouache-abstract` の法「**a stroke covers what it crosses, and the revision stays visible**」。

## Object Motion

**白い自転車の形は動かない。** 壁にもたれたままである。

## Environmental Motion

**無い。** 埃も、風も、鳥も無い。⚠️ **光は S01 で到着し終えている。**

## Physical Characteristics

- Weight: 線は**紙の上の薄い鉛筆である**。重さを持たない。
- Inertia: **歩調は落ちない。** それるあいだも、同じ速さである——
  ⚠️ **これが「癖」の物理である。** 意識してよければ、速度が変わる。
- Acceleration: 無い。**それることも、戻ることも、同じ速さである。**
- Fluidity: ⚠️ **滑らかに曲がらない。** この様式の線は**置かれたもの**である——
  ゆえに屈折は、**一本の線が途中で向きを変えた**ように見える。
- Impact: 無い。**白い形に触れもしない。**

# 12. EMOTION

- Emotional Arc: 何も無い → **線が、ひとりでにそれる** → 線が戻る。**灯は何も感じていない。**
- Emotional Events: **線が戻る速さ。** ⚠️ **この1本の感情は、灯の内側には無い**——
  **観客の側にだけ生まれる**（「二十年、そうしてきた」と読むのは観客である）。

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。** ⚠️ **影は落ちない。**
- Lighting Events: **無い。** ⚠️ **白い形に影を落とさない。** 「白い形」が白いのは、
  光が当たっているからではない——**それが、もう色を持たないからである。**

# 14. AUDIO

- Dialogue: 無し。
- Sound Effects: **足音のみ。** 控えめである——**主役にしない。**
  ⚠️ **自転車の音を足さない。** **この形は、もう鳴らない。**
- Music: 無し。
- Environment: 通りの空気。**他には誰も居ない。**
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: **灯——後ろ姿、輪郭、顔は描かない。**
- Spatial: 通りは1つの場所である。**この1本は通りを出ない。**
- Temporal: 朝。S03 の直後である。
- Visual: 一色も出さない。
- Motion: 動くのは線だけである。**カメラは動かない。**
- Sound: 足音のみ。
- ⚠️ **この1本に残るもの:** 白の上の、**ふくらみ1つ**。S08 以降も、この線は消えない。

# 16. CONSTRAINTS

## MUST NOT

- No second person. No cat in frame — 草稿 L5「**猫はもういない。**」
- **No outline drawing of a bicycle. No mechanical detail drawn in line. No spokes drawn.**
  ⚠️ **この1本の中心的な禁止である**——**白は形であって、輪郭線ではない。**
- No shading on the white shape. No shadow cast by the white shape.
- **No shadow at the figure's feet** —— 影は S02 の主題であり、**この1本の主題は線である。**
- No visible face on the figure.
- No noren in frame. No shop front in frame.
- No house numbers, no numerals, no numbers.
- No legible text of any kind.
- **No fully-painted flat vermilion cloth** — 朱はまだ戻っていない。この禁止は S01–S07 が持つ。

## MUST

- Full animation, not limited: **線は5秒のあいだ進みつづける。**
- **線が一点で外へそれ、すぐ戻ること。** それる幅は**狭い。**
- **ふくらみが白の上に残ること**——線は消えない。
- 白い形は**動かない**こと。

## PREFER

- 戻る速さが、**ためらいを含まない**こと。
- 白い形が、**遠目に自転車と読めるが、描かれてはいない**こと。

## ALLOW

- 石畳の上に、線の濃淡がわずかに残ること（鉛筆の圧として）。

# 17. GENERATION PRIORITIES

1. **自転車を描かない。** ⚠️ **最も起きやすい失敗である。** 「自転車」と言えば、
   モデルはスポークとサドルとハンドルを描く。**この形は、白い面である。**
2. **灯に白い形を見せない。** 見れば、この1本は「よける人」の1本になる。**癖は、見ない。**
3. **線を消さない。** それた線が戻ったとき、**ふくらみが残っていなければ、
   この様式の法がこの作品で一度も働いていないことになる。**
4. **カメラを動かさない。**
5. **影を置かない。** 灯の足元にも、白い形の下にも。
6. **色を出さない。**
7. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 5-second continuous cinematic take (16:9) of a walking line bending outward at one point and coming back, one clip. Beats, deliberately uneven: [0-2s] the white street with the white bicycle-shaped thing leaning against a closed shutter, and the line of the walk running straight; [2-3s] the line bends outward around the shape, by the smallest width at which the bend can still be read as a bend, and the walk does not slow; [3-5s] the line comes back and runs straight again, without hesitation, and the outward bulge stays on the paper where it was laid. The core beat — the line bending — is the shortest beat in this shot, one second of the five, and the two seconds before it and the two after it exist to make that one second read. The figure walks and never looks at the white shape: not looking is what makes the avoidance a habit rather than a decision. The white bicycle-shaped thing is a shape of white paper where a bicycle was: no outline is drawn around it, no spokes are drawn, no mechanical detail is drawn in line, it carries no shading and casts no shadow, and it does not move. The story's four colours are all absent from this frame. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on a straight walking line with one bulge left in it, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. A downtown street returned to blank paper: stone paving given a large share of the frame, a row of closed shutters, a white bicycle-shaped thing leaning against one of them as a shape of white paper with no outline, no spokes and no mechanical detail drawn in it, carrying no shading and no shadow. One figure seen from behind, walking, face not drawn; the line of the walk lies on the paving as a thin faint pencil line, running straight and bending outward once around the white shape and returning, the bulge left visible where the line was revised. No colour anywhere in the frame. No second person, no cat, no noren, no shop front, no house numbers, no lettering, no shadow at the figure's feet, no shadow under the white shape, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. The line advances and bends outward at one point by a narrow width and comes back at once, and the pace of the walk never changes while it bends: the bending is what a twenty-year habit looks like, not what noticing looks like. The revision stays visible: where the line moved outward it remains moved outward, and the bulge is left lying on the paper. The figure walks on without turning the head and without looking at the white shape. The white bicycle-shaped thing does not move, does not rock, does not lean further and does not answer being passed. The town does not move: no door opens, no shutter moves, no second figure steps anywhere in the frame, no cat, and the light does not shift. No morphing shapes, no motion blur, no stutter, no held frames, no flow or bleed in the pigment, and nothing in the frame casts a shadow.

## Camera Prompt

Third-person, parallel to the street, at the height of a person standing, with the stone paving given a large share of the frame so that the line on it can be read. The camera holds still for the whole five seconds: no push, no pull, no pan, no tilt, no track, no rack focus, no handheld, no shake, and no move to follow the line as it bends. [0-2s] holding on the white shape and the straight line. [2-3s] still holding as the line bends, and the camera does not follow it outward. [3-5s] still holding as the line returns, to the end. The style allows one drift; this shot spends none — the one drift in this work is spent later, and spending it here would cost the shot that needs it. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. Sound effects: footsteps only, at a low level, kept under the image and never made the subject of the shot, and their pace does not change while the line bends. No other sound effects: no bicycle sound, no bell, no chain, no wheel, no door, no shutter, no wind, no bird, no traffic — the white shape has not made a sound in a long time and must not make one here. No ambient bed beyond the still air of a street with nobody else in it. Music: none, and no swell, no sting, no melody. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no fully-painted flat vermilion cloth, no second person, no cat in frame, no outline drawing of a bicycle, no mechanical detail drawn in line, no spokes drawn, no shading on the white shape, no shadow cast by the white shape, no shadow at the figure's feet, no visible face on the figure

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. This shot is that law made into the story: the line is revised once, outward, and the revision is left where the hand put it, which is why the bulge stays on the paper after the figure has gone. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither. The palette stays restrained throughout, which here means white, pencil line and one white shape. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg04-5s-01`
- Segment ID: `01-4`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `5s`
- References: `REF_LOCATION (hakuchizu-mionomachi-street, MEDIUM) ／ REF_GEOGRAPHY (通り.geography, LOW) ／ REF_CHARACTER (灯.identity, HIGH) ／ REF_PROP (白い形.appearance, HIGH) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: `灯.identity`・`灯.states.支払いの前`・`灯.negatives`・`通り.base`・`通り.geography`・`白い形.appearance`・`白い形.negative`
- Temporal Structure: `3 beats, NON_UNIFORM — sparse 2s / held 1s / sparse 2s. The core = BEAT 2 at 2-3s (20% — the shortest beat is the core)`
- Camera Events: `0 events. One continuous take, camera still for the whole clip`
- Action Events: `ACT_WALK → ACT_RETURN`
- Audio Events: `no dialogue ／ footsteps only ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。

## Anticipated risks (to check in the first generation)

- **⚠️ 自転車が描かれる。** これがこの1本の最重要の失敗である。**白い面として出なければ、
  この作品の「白地図」という前提が、この1本で崩れる。**
- **⚠️ 灯が白い形を見る。** 見せれば、癖が判断になる。**`no visible face on the figure` は
  この1本では「見る」を禁じる役目も負っている。**
- **⚠️ 線が消える。** それた線が戻ったとき、ふくらみが残っていなければ、
  **様式の法がこの作品で一度も働いていないことになる。**
- **⚠️ 速度が落ちる。** 「避ける」を「気づく」として演じれば、歩調が変わる。
- **⚠️ 影が入る。** 白い形の下にも、灯の足元にも。
- **⚠️ 色が入る。** 一色も要らない。
