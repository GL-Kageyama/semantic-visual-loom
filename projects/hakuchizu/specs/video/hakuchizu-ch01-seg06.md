# ═══ 演出要約 ════════════════════════════════════
# 『白地図』第1章「暖簾」 / 反応 / still —— 止まる。房に触れそうになって、やめる
#
#   灯の指先が房の手前まで来て、触れずに戻る。
#   8秒のあいだ、布は1ミリも動かない——風は一度通り過ぎるが、布は答えない。
#   風が来たことは、石畳を滑る埃でしか判らない。変わったのは、布ではなく灯の側である。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 6/11 / 8s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg06.md`）。
⚠️ **`mode: still` である。ゆえに §11 は空にできない**（`L24`）。

⚠️ **この1本の変化は「触れないこと」である。** 草稿 L9「灯は房に触れそうになって、**やめる。**」
⚠️ **やめることは、行為である。** 何も起きないのではない——**起きかけたことが、灯の側で止められる。**
**ゆえにこの1本は、この話で最初に「灯が決める」1本である。**
（S08 の色は結果であり、S10 の支払いは決算である。**決めたのは、ここである。**）
⚠️ **`mode: still` と「手が一度動く」の食い違いは、事故ではなく判断である。**
理由は `shots/hakuchizu-ch01-seg06.yaml` の冒頭に記録してある（主題は暖簾であり、
**暖簾は8秒のあいだ、風を受けても1ミリも動かない**）。
⚠️ **この1本の風は、S09 で戻ってくる。同じ風である。**
ここでは布が答えず、S09 では布が鳴る——**その差が、色の値である。**

⛔ **§18 の `Negative Prompt` が S07 と同一である理由。** `ledger.disclosure` は S07 の開示点
（`暖簾.下のやりとり: 思い出された`）を **`negative: covered`** と宣言している——
**ゆえに `L10` は「両者の否定節の集合が一致すること」を要求する。**
⚠️ **したがって、この集合は2本ぶんの危険を1つの集合として持つ。**
内訳は §16 の註に書く。**片方だけの危険を消せば、`L10` が鳴る。**

---

# 1. VIDEO

- Duration: `8s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: A single change: 灯's fingertip stops short of the tassel and comes back, and the white cloth is not moved by the hand or by the wind.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01）。
- 白は音を持たない（S09）。
- 白の下には、人がいた気配が透けている（S03）。
- **「思い出したぶんだけ、白のなかから色が立ち上がる。」**（S08）
  ⚠️ **この1本は、その手前である**——**思い出すかどうかを、灯がここで決める。**
- 覚えることは、払うことである（S10・S11）。
- 数は町を戻さない（S05・S10）。
- 置いた色は、もう白に戻らない（S11）。
- ⚠️ **この1本は、この作品で最初に「決める」1本である。**
  **以後の3つの開示点（S08・S10・S11）は、すべてこの1秒から出ている。**

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
- Color Language: **一色も無い。** 暖簾は**白い無地である**（`暖簾.states.白`）。
  ⚠️ **朱が戻るのは S08 である。**
- Texture: 荒い紙。**暖簾は紙である**——ゆえに**風を知らない。**
  房は**紙の細い帯**であって、糸ではない。
- Rendering: ⚠️ **埃は「置かれた粒」である。** ぼかした煙ではない——この様式では、
  埃も**紙の上を滑る粒**として描かれる。
- Visual Density: **低い。** ⚠️ **この1本の8秒は、この作品で最も長く「何も起きない」8秒である。**
- Time: `朝`
- Atmosphere: 白い暖簾。**風が来て、布は答えない。**

# 3. SUBJECTS

## 暖簾

- Reference: `暖簾.appearance`・`暖簾.negative`（`attached` に従う）
- Appearance: **白い無地の布。** 房が数本、下へ垂れている。
  ⚠️ **字を置かない、店の名を置かない**（`no legible text on the noren`・`no shop name on the noren`）。
  ⚠️ **房は紙の細い帯である。** 糸の質感を作らない。
- Behavior: ⚠️ **動かない。** 揺れない、浮かない、鳴らない——
  草稿 L9「風が吹いても白は揺れない。**白は風を知らない。**」
- Continuity Requirements: ⚠️ **この1本で「この布は動かない」が観客の身体に残る。**
  **S08 の12秒は、その記憶の上に組まれている。**
  ⚠️ **ゆえに、この1本で布が1ミリでも揺れれば、山が安くなる。**

## 灯

- Reference: `灯.identity`・`灯.states.支払いの前`（`attached` に従う）
- Appearance: 後ろ姿、輪郭、**そして指先。** ⚠️ **顔は描かない**（`bible.constants.顔`）。
- Behavior: **止まっている。** 指先が房の手前にあり、**5-6秒で、届く手前で止まる**——
  止まりかたは**急である**。ゆっくり近づいて、ゆっくり引くのではない。**やめる、という速さで止まる。**
- Continuity Requirements: ⚠️ **指先に影を置かない、白くしない。**
  白くなるのは S11 である——**ここでは、指先はまだ色を持っている**（`支払いの前`）。

## 風

- Appearance: **見えない。** 埃が石畳の上を滑ることでだけ読める。
- Behavior: **一度、通り過ぎる。** 強くならない——**吹き抜けるのではなく、通る。**
- Continuity Requirements: ⚠️ **風は布の側には一度も現れない。**

# 4. ENVIRONMENT

- Location: `暖簾の店の前`（`暖簾の店の前.base`・`.geography`・`.states.白`）
- Environment Elements: 店の前の石畳、白い暖簾、閉じた店。
  ⚠️ **店の内側は画に入らない**（`PLAN.md` §0-f——**カメラは店の奥へ入らない**）。
- Environmental Behavior: **埃が滑る。** それだけである。

# 5. OBJECTS

- `暖簾` — この1本の主題である。
- `暖簾の店の前` — この1本の場所である。
- `白い形`・`水の跡`・`薬缶` — **この1本には無い。**
  ⚠️ **湯気を出さない、薬缶を置かない**（§16）——**この店は、まだ開いていない。**

# 6. REFERENCES

- REF_LOCATION: `暖簾の店の前.base` (HIGH)
- REF_GEOGRAPHY: `暖簾の店の前.geography` (MEDIUM)
- REF_CHARACTER: `灯.identity` (HIGH)
- REF_PROP: `暖簾.appearance` (HIGH — この1本の主題である)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — 開示点の `covered` 宣言がこの1本の §18 を決める)

# 7. NARRATIVE

- Core Event: 灯が、房に触れかけて、やめる。
- Beginning: 灯の指先が房の手前にある。**あと少しで届く。まだ触れていない。**
- Turn: 風が来る。**埃が滑る。布は答えない。**
- Peak: **指先が、届く手前で止まる。** ⚠️ **この1秒が、この1本の変化である。**
- Pull: 指が戻る。**房は、まだ白いまま垂れている。**
  ⚠️ **変わったのは布ではなく、灯の側である。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-3s` — density: `held` — 白い暖簾。房が数本、下へ垂れている。灯の指先が、房の手前にある。
    ⚠️ **この3秒は、動かないための3秒である。**
  - BEAT 2 `3-5s` — density: `sparse` — 風が来る。**埃が石畳の上を滑る。房は動かない。**
  - BEAT 3 `5-6s` — density: `held` — **指先が、届く手前で止まる。** この1秒が変化である。
  - BEAT 4 `6-8s` — density: `sparse` — 指が戻る。**房は、まだ白いまま垂れている。**
- Temporal Density: ⚠️ **核は「何も起きない3秒」である**（8秒のうちの3秒＝最大の拍）。
  **変化そのものは、その中の1秒にすぎない。**
  ⚠️ **この1本の不均等は「長い静止・短い風・1秒の決断・2秒の余韻」である。**

# 9. ACTION

- `ACT_WIND` — Before: 埃は止まっている。After: 埃が石畳を滑り、通り過ぎている。**布は動かない。**
  Causes: 風。⚠️ **風が来たことは、埃でしか判らない。**
- `ACT_STOP` — Before: 灯の指先が房へ近づいている。After: **指先が止まり、戻る。**
  Causes: **灯の決断。** ⚠️ **この1本の変化はこれである。**
  ⚠️ **布は1ミリも関与しない**——**布は、触れられなかったことを知らない。**
- ⚠️ **`ACT_TOUCH` は無い。** 触れれば、この話は別の話になる。

# 10. CAMERA

- Camera Language: 三人称、店の前、**立っている人の高さ**。**房と、灯の手が同じ画に入る。**
  ⚠️ **店の内側は画に入らない**——`PLAN.md` §0-f。
- Camera Events: `0-3s` 房と指先に留まる。`3-5s` 風が埃を滑らせるが、**カメラは埃を追わない。**
  `5-6s` 指が止まる——**この1秒、カメラは何もしない。**
  ⚠️ **止まる瞬間に寄れば、この決断は演出になる。** **この1本の決断は、遠目でなければ読めない。**
  `6-8s` 指が戻る。留まったまま終わる。
- Camera Behavior: **8秒のあいだ、一度も動かない。**
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。** 使うなら山（S08）である。
  ⚠️ **辞退は辞退として書く**（`skills/staging/SKILL.md`）。

# 11. MOTION

⚠️ **`mode: still` でも §11 は要る**（`L24`・スキーマ）。**止まるのは主題である。**

## Subject Motion

**主題（暖簾）は、8秒のあいだ1ミリも動かない。** 動くのは**灯の指先だけ**である——
**近づき、止まり、戻る。** ⚠️ **この3つの動作のうち、この1本が使うのは3つ目までである。**

## Object Motion

**無い。** 店の戸は開かない、埃以外に動くものは無い。

## Environmental Motion

**埃が、石畳の上を滑る。** ⚠️ **ぼかさない**——埃は**置かれた粒**であり、
**滑ることは、粒の位置が変わること**である。**煙のように揺らめかせない。**

## Physical Characteristics

- Weight: **布は紙である**——ゆえに**風を受けても重さが変わらない。** 紙は風を知らない。
- Inertia: **指の停止に、慣性が無い。** 止まることは、**運動の終わりではなく、決定である。**
- Acceleration: ⚠️ **近づく速さは読めない**（0-3秒は静止である）。
  **見えるのは「止まったこと」と「戻ったこと」だけである。**
- Fluidity: **滑らかでない。** 指の停止は**角を持つ**——**やめる、という速さである。**
- Impact: ⚠️ **接触が無い。** **この1本の物理は、接触の手前で止まっている。**

# 12. EMOTION

- Emotional Arc: 静けさ → 風 → **指が止まる** → 静けさが戻る。**布は何も知らない。**
- Emotional Events: **指が止まった1秒。** 強度は**中**——
  ⚠️ **この作品で最初に灯の内側が動く瞬間である。**
  ⚠️ **ただし、表情では示さない。顔は描かれない**（`bible.constants.顔`）。

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。** 影は落ちない。
  ⚠️ **ゆえに「指が影を作る」ことは無い。**
- Lighting Events: **無い。** ⚠️ **風を光で示さない**——風は埃で示される。

# 14. AUDIO

- Dialogue: 無し。
- Sound Effects: **無し。** ⚠️ **風の音も足さない**——
  **この1本の主題は「布が答えないこと」であり、風に声を与えれば、
  観客は布の返事を待つ。** ⚠️ **返事は S09 である。**
  ⚠️ **これは読みである**（草稿 L15「白のなかにはなかった音だった」を、
  **この作品では「白は鳴らない」と読んだ**）。**裁定を仰ぐ形でここに残す。**
- Music: 無し。
- Environment: 店の前の、何も鳴っていない空気。
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: **灯——後ろ姿、輪郭、指先。顔は描かない。**
- Spatial: 店の前である。**この1本は店の前を出ない。店の内側へ入らない。**
- Temporal: 朝。S05 の直後である。
- Visual: 一色も出さない。**暖簾は白い無地である。**
- Motion: **布は動かない。** 動くのは指先と埃だけである。**カメラは動かない。**
- Sound: 無音。
- ⚠️ **この1本で確立するもの:** **「この布は動かない」。**
  **S08 は、この記憶の上で色を戻す。**

# 16. CONSTRAINTS

## MUST NOT

⚠️ **この節は、S07 と同一の `Negative Prompt` を作る**（`L10`——`covered` 宣言）。
**内訳を分けて書く。**

**この1本（S06）の危険:**
- **No swinging cloth. No fluttering noren. No lifted cloth. No wind in the cloth** —— **この1本の中心である。**
- **No hand touching the cloth** —— 触れれば、この話は別の話になる。
- No colour on the noren. No wash on the cloth. No shading —— 朱は S08 である。
- No shop interior —— `PLAN.md` §0-f。
- No shopkeeper. No figure of the shopkeeper in frame —— **この話で一度も立たない。**
- No steam. No smoke. No door opening —— **この店は、まだ開いていない。**
- No visible face on the figure. No cat in frame. No numerals, no numbers.
- **No fully-painted flat vermilion cloth** — 朱はまだ戻っていない。この禁止は S01–S07 が持つ。

**S07 へ渡す危険**（⛔ **2026-09-22 の裁定（第二）以降、S06 と S07 は同じ集合ではない**——
S07 が**柄を禁じる4節**を足して `changed` になった。**この2節は、いまも両方が持つ**）:
- **No montage cuts. No superimposed images** —— S07 は `モンタージュ` と名乗りながら**一度も切らない**。
  ゆえに**切ること・重ねることを、この集合は禁じている。**

## MUST

- Full animation, not limited: **埃は5秒のあいだ滑りつづけ、指は止まり、戻る。**
- **布は1ミリも動かないこと**——揺れない、浮かない、鳴らない。
- **指は、届く手前で止まること。** 止まりかたは**急である。**
- **布に触れないこと。**
- 店の内側を画に入れないこと。

## PREFER

- 最初の3秒で、**何も起きないことが保たれる**こと。
- 停止のあと、**指がためらわずに戻る**こと。

## ALLOW

- 埃の粒が、石畳の上に**わずかに残る**こと。

# 17. GENERATION PRIORITIES

1. **布を動かさない。** ⚠️ **この1本の最重要の失敗である。** 風が来れば、モデルは布を揺らす。
   **この1本は、布が答えないことを撮っている**——**揺れれば、山が安くなる。**
2. **触れさせない。** 「触れそうになって、やめる」は、モデルにとって「触れる」である。
3. **顔を描かない。** 決断の瞬間に顔を描けば、この作品の人物の定義が崩れる。
4. **店の内側を入れない。**
5. **暖簾に字を入れない。** のれんは、字が入る場所である——**この作品では入らない。**
6. **湯気を出さない、薬缶を置かない。** この店は、まだ開いていない。
7. **カメラを動かさない。** 特に、止まる1秒に寄らない。
8. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

An 8-second continuous cinematic take (16:9) of a hand stopping short of a white cloth and coming back, one clip. Beats, deliberately uneven: [0-3s] the white cloth hanging with a few tassels at its lower edge and 灯's fingertips held just in front of one tassel, near enough to reach and not yet touching, and nothing happening for three seconds; [3-5s] the wind passes and dust slides along the stone paving, and the cloth does not answer it — it does not swing, does not lift, does not flutter and does not make a sound; [5-6s] the fingertips stop short of the tassel and do not arrive; [6-8s] the fingers come back, and the cloth is still hanging white. The core beat — the three seconds in which nothing happens — holds the largest share of the duration, and the change itself is a single second inside the shot, so that the audience learns in the body, before the change comes, that this cloth does not move. What changes here is on 灯's side and not on the cloth's: the cloth is untouched, unmoved and unaware. 灯 is seen from behind and the face is never drawn. The cloth is plain white with no lettering and no shop name on it. The story's four colours are all absent from this frame; the vermilion is not here yet. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on the same white cloth hanging exactly as it was, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. The front of a shop closed for the morning on a street returned to blank paper: a plain white noren hanging unframed and unlettered, a few tassels of thin paper band hanging at its lower edge, the stone paving in front of it, and 灯 seen from behind at the edge of the frame, back and outline and one hand, the face not drawn at all, the fingertips a little short of one tassel. Dust lies as small laid grains on the paving. The cloth is flat white paper with no wash on it, no shading, no colour, no lettering and no shop name; the shop's interior is not in the frame; no kettle and no steam are in the frame. No cast shadow anywhere, no light shaft, no sunbeam, no lens flare. No second person, no shopkeeper, no cat, no numerals, no numbers, no signage, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. The subject of this shot is a cloth that does not move, and the cloth must stay exactly where it is for all eight seconds: it does not swing, does not lift, does not flutter, does not ripple, does not breathe with the wind and does not answer the hand. The wind is shown by the dust alone, and the dust slides along the paving as laid grains changing position, never as blurred smoke. The fingertips approach, stop short of the tassel, and come back; the stop is abrupt, the speed of abandoning a thing rather than the speed of reaching for it, and the fingers never touch the cloth. Nothing else moves: no door opens, no shutter moves, no second figure enters the frame, and the light does not shift. No morphing shapes, no motion blur, no stutter, no held frames, no flow or bloom or bleed in the pigment.

## Camera Prompt

Third-person, in front of the shop, at the height of a person standing, with the hanging cloth and the hand both inside one frame. The camera holds still for the whole eight seconds: no push, no pull, no pan, no tilt, no rack focus, no handheld, no shake, and no move closer at the moment the fingers stop — if the camera moves in on that second, the decision becomes a piece of staging, and it can only be read from a distance. [0-3s] holding on the cloth and the fingertips. [3-5s] still holding while the wind moves the dust, and the camera does not follow the dust. [5-6s] still holding as the fingers stop. [6-8s] still holding as they come back, to the end. The style allows one drift; this shot spends none — the one drift in this work is spent later, and spending it here would cost the shot that needs it. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. No sound effects at all: no wind sound, no cloth sound, no rustle, no flap, no footsteps, no door, no shutter, no bird, no traffic. Giving the wind a voice here would make the audience wait for the cloth to answer, and the cloth's answer is not in this shot — it is in a later shot of the same sequence, and it must arrive there as the first sound the white has made. No ambient bed beyond the still air in front of a shop that is not open yet. Music: none, and no swell, no sting, no melody. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no fully-painted flat vermilion cloth, no swinging cloth, no fluttering noren, no wind in the cloth, no lifted cloth, no colour on the noren, no wash on the cloth, no shading, no door opening, no steam, no smoke, no cat in frame, no visible face on the figure, no hand touching the cloth, no montage cuts, no superimposed images

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. In this shot the hand does not arrive: the revision is withheld, and what stays visible is the shape of a hand that stopped. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither. The palette stays restrained throughout, which here means one white with nothing added to it. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg06-8s-01`
- Segment ID: `01-6`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `8s`
- References: `REF_LOCATION (暖簾の店の前.base, HIGH) ／ REF_GEOGRAPHY (暖簾の店の前.geography, MEDIUM) ／ REF_CHARACTER (灯.identity, HIGH) ／ REF_PROP (暖簾.appearance, HIGH) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: `灯.identity`・`灯.states.支払いの前`・`灯.negatives`・`暖簾の店の前.base`・`暖簾の店の前.geography`・`暖簾の店の前.states.白`・`暖簾.appearance`・`暖簾.negative`
- Temporal Structure: `4 beats, NON_UNIFORM — held 3s / sparse 2s / held 1s / sparse 2s. The core = BEAT 1 at 0-3s (38% — the beat in which nothing happens), the change = BEAT 3 at 5-6s (13%)`
- Camera Events: `0 events. One continuous take, camera still for the whole clip`
- Action Events: `ACT_WIND → ACT_STOP`
- Audio Events: `no dialogue ／ no sound effects ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`
- ⚠️ **`mode: still` と「手が一度動く」の食い違いは判断である**（`shots/hakuchizu-ch01-seg06.yaml` の註）。

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。

## ⚠️ `L14` ——「宣言を超えた区間」（＋2）

⚠️ **この仕様は `L14` に当たる。** 台帳はこの位置に変化点を宣言していない。
**`L14` の言い分は正しい**——**このショットで、§18 の禁止は、戻らない仕方で2節増えた。**
⚠️ **そしてその変化は、このショットの欠陥ではない。理由をここに書く**——`L14` 自身が
「`disclosure` に行を足すか、**足さない理由を記録に書く**」と求めている。

| ＋2（増えた） | このショットから要る理由 |
|---|---|
| `no door opening` | **S06 は、店の前へ着く最初の1本である**（`REF_LOCATION: 暖簾の店の前.base` はここが初出）。主題は「触れそうになって、**やめる**」——**灯は店の前まで来て、店には入らない。** ⚠️ **店の前が枠に入るから、戸が画に入る**——ゆえに**開かないことを禁じねばならない。** S06 以前、店の前は枠の外である（S05 は雨戸の列である）。⚠️ **S11 まで店の前は画にある**——この1節は戻らない。 |
| `no steam` | **薬缶は、この作品では音である**（`ledger.props.薬缶`——「持ち上げる手」と「火からおろす音」）。⚠️ **台帳は「湯気はまだ白い」と書く。** **湯気を画にすれば、店の奥が実体になる**——**色が戻る前だからである。** ⚠️ **同じ組の `no smoke` は S06 で入り、S08 で落ち、S09 で戻る**——**戻るものは `L14` の対象ではない。残るのはこの1節である。** |

⚠️ **足して数を減らさなかった。** この2節を以後のショットから外せば `L14` は静かになる——
**だが `no steam` を外すことは、湯気を画に出してよいと言うことである。**
**数を小さくすることは、欠陥を直すことではない。**

⚠️ **`disclosure` に行を足す道は取らない。** **このショットは開示の変化点ではない**——
台帳が宣言するのは S07 の開示点であり（`暖簾.下のやりとり: 思い出された` ＋ `negative: covered`）、
**S06 はその1本前である。** ここに嘘の行を足せば、**`L10` の `covered` の前提が崩れる。**

⚠️ **ゆえに残るのは、著者への問いである**——**この作品の動画の Negative は、一つの集合なのか、
ショットごとに書かれるのか。** ⚠️ **問いの全文と実例は `hakuchizu-ch01-seg02.md` の同じ節に書いた**
（この位置が3箇所あるうちの1つである）。⚠️ **著者が決めるまで、この仕様は送らない。**

## Anticipated risks (to check in the first generation)

- **⚠️ 布が揺れる。** これがこの1本の最重要の失敗である。**「風が来る」と書けば、
  モデルは布を揺らす。** 布が揺れれば、**S08 の色は「動いていなかった布が動く」話ではなくなる。**
- **⚠️ 指が触れる。** 「触れそうになって、やめる」は、モデルにとって触れることである。
- **⚠️ のれんに字が入る。** のれんは、字が入る場所である。
- **⚠️ 顔が入る。** 決断の瞬間である——ゆえに最も危ない。
- **⚠️ 湯気・薬缶が入る。** この店は、まだ開いていない。
- **⚠️ 決断の1秒に寄る。** 寄れば、この決断は演出になり、読めなくなる。
- **⚠️ 店の内側が映る。** `PLAN.md` §0-f。
