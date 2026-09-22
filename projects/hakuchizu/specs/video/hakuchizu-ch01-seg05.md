# ═══ 演出要約 ════════════════════════════════════
# 『白地図』第1章「暖簾」 / 総覧 / still —— 朝の光が列を渡りきり、白はどこも同じ白になる
#
#   朝の光が雨戸の列を渡りきり、白はどこも同じ白になる。
#   6秒。列ぜんたいを一度に主題にするので、寄りの画を1枚も挟まない。
#   誰も立たない。動くのは光だけである。列に番号も目印も置かない。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 5/11 / 6s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg05.md`）。
⚠️ **`mode: still` である。ゆえに §11 は空にできない**（`L24`）——
**止まるのは主題であって、画面ではない。光は動く**（`motion` の註）。

⚠️ **この1本の変化は「数えられなくなること」である。**
⚠️ **人は立たない**（S01・S03 と同じ）。ゆえに `reference_set` に人物の鍵が無い。
⚠️ **`PLAN.md` の表から変えた1本である。** 表は「**灯は雨戸の列を数えずに通り過ぎる**」と書いていたが、
**採らなかった**——理由は `shots/hakuchizu-ch01-seg05.yaml` の冒頭に記録してある。
⚠️ **この1本の主題は「数は町を戻さない」である**（草稿 L7「数字は町を戻さない。
数字を覚えても、暖簾の朱は戻らない」）。**ゆえに数を画の側に置けない**——
**数える手がかりが1つも無いことが、この1本の内容である。**

---

# 1. VIDEO

- Duration: `6s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: morning light crosses a row of white shutters and the row loses the difference that let it be counted.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01）。
- 白は音を持たない（S09）。
- 白の下には、人がいた気配が透けている（S03）。
  ⚠️ **この1本の雨戸の家は「もう十年も空いている」**（草稿 L7）——**気配はあるが、人は居ない。**
- 思い出したぶんだけ、白のなかから色が立ち上がる（S08）。
- 覚えることは、払うことである（S10・S11）。
- **「数は町を戻さない。」** ⚠️ **この1本が実演するのはこの行である。**
  **ゆえにこの1本は、数を数えられなくすることで、この法を画にする。**
- 置いた色は、もう白に戻らない（S11）。

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
- Color Language: **一色も無い。** ⚠️ **この1本に在るのは、白の濃淡だけである**——
  **そしてその濃淡が、この6秒で消える。** **この作品で、色が「減る」のは S01 と、ここだけである。**
- Texture: 荒い紙。**雨戸は、白い面である**——板の目は描いてよいが、**文字は置かない。**
- Rendering: ⚠️ **光沢を作らない。** 白は**照らない**——照れば、この1本は「光る町」の1本になる。
- Visual Density: **低い。** ⚠️ **総覧である**——**列ぜんたいが一度に主題である。**
  **ゆえに寄りの画を1枚も挟まない。**
- Time: `朝`
- Atmosphere: 無人の朝。**空き家の列。**

# 3. SUBJECTS

⚠️ **この1本に人物は居ない。**

## 朝の光

- Reference: （参照画像なし——光は `bible` が持つ）
- Appearance: **面としての明るさ。** 手前から奥へ渡る。
  ⚠️ **光条を作らない、光芒を作らない、レンズフレアを作らない**（§16）。
- Behavior: **渡る。** 速まらない、遅くならない。**影で示されない**（`no directional light`）。
- Continuity Requirements: ⚠️ **光は「明るさ」であって「光線」ではない。**

## 白い雨戸の列

- Reference: `props.白い形.appearance`（`attached` に従う）
- Appearance: **一列に並んだ白い雨戸。** 手前が明るく、奥が暗い——
  **その差が、列に「ひとつずつ」という数え方を与えている。**
- Behavior: **動かない。** 開かない、閉まらない、きしまない。
- Continuity Requirements: ⚠️ **番号を置かない。** `no legible signage` は床である——
  **数える手がかりを、画の側に置かない。**

# 4. ENVIRONMENT

- Location: `通り`（`hakuchizu-mionomachi-street` の意図）
- Environment Elements: 石畳、**白い雨戸の列**、二階のベランダ、屋根。**店はまだ画に入らない。**
- Environmental Behavior: **無い。**
  ⚠️ **埃を置かない**（判断）——**埃は S06 で、風の唯一の証拠として使う。**

# 5. OBJECTS

- `通り` — 白紙に戻った下町の通り。
- `白い形` — この1本では**雨戸の列**として現れる。
- 暖簾・暖簾の店の前・水の跡・薬缶 — **どれもこの1本には無い。**

# 6. REFERENCES

- REF_LOCATION: `hakuchizu-mionomachi-street` (MEDIUM)
- REF_GEOGRAPHY: `通り.geography` (LOW)
- REF_PROP: `白い形.appearance` (MEDIUM — この1本では雨戸の列である)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL)
- ⚠️ **`REF_CHARACTER` を書かない。** この1本に人物が居ないので、**名乗る相手が無い。**

# 7. NARRATIVE

- Core Event: 朝の光が雨戸の列を渡りきり、白はどこも同じ白になる。
- Beginning: 手前が明るく、奥が暗い。**その差が、列に順序を与えている。**
- Turn: **差が縮みはじめる。** 列は「並んでいるもの」から「続いている面」へ変わる。
- Peak: 差が消える。**単位が無くなる。**
- Pull: 白はどこも同じ白である。**数えられない。**
  ⚠️ **数える者が居ないのではなく、数える単位が無い。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — 白い雨戸の列。**手前が明るく、奥が暗い。**
  - BEAT 2 `2-4s` — density: `held` — **光が奥へ渡り、暗さの差が縮む。** この2秒が核である。
  - BEAT 3 `4-6s` — density: `sparse` — 光が列を渡りきる。**白はどこも同じ白になる。**
- Temporal Density: **核の2秒は、明るさが均されていく2秒である。**
  ⚠️ **出来事は「差が縮むこと」だけである**——**それ以外の情報を、この2秒に足さない。**

# 9. ACTION

- `ACT_LIGHT_CROSS` — Before: 列に濃淡の差がある。After: 差が無く、白はどこも同じ白である。
  Causes: 朝。⚠️ **光は影を動かさない。** 差は**明るさの差**であって、**影の長さの差ではない。**
- ⚠️ **この1本に人の所作は無い。** `mode: still` であり、**主題は止まっている。**

# 10. CAMERA

- Camera Language: 三人称、**列の正面**、立っている人の高さ。
  ⚠️ **総覧である**——**列の端から端までが、1つの画に入っている。**
  **寄りの画を1枚も挟まない**（`役割` の定義）。
- Camera Events: `0-2s` 列に留まる。`2-4s` 光が奥へ渡るが、**カメラは光を追わない。**
  `4-6s` 同じ白い列に留まって終わる。
- Camera Behavior: **6秒のあいだ、一度も動かない。** 寄りも、引きも、パンも無い。
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。** 使うなら山（S08）である。
  ⚠️ **辞退は辞退として書く**（`skills/staging/SKILL.md`）。

# 11. MOTION

⚠️ **`mode: still` でも §11 は要る**（`L24`・スキーマ）。**止まるのは主題である。**

## Subject Motion

**主題は止まっている。** 雨戸は1枚も動かない——**動くのは、その上の明るさだけである。**
⚠️ **明るさが動くことは、紙がまだ塗られていないことを、どこでも同じに確かめることである。**

## Object Motion

**無い。** 戸は開かない、人は歩かない、布は掛かっていない。

## Environmental Motion

**無い。** 埃も、風も、鳥も無い。
⚠️ **埃を置かないのは判断である**——**埃は S06 で、風の唯一の証拠として使う。**

## Physical Characteristics

- Weight: **光は重さを持たない。** 持っているのは**紙の白さ**だけである。
- Inertia: 光の到着は**途中で止まらない。** 速まらないが、戻りもしない。
- Acceleration: 無い。
- Fluidity: ⚠️ **光が「流れない」。** 明るさは**面ごとに置き換わる**——
  この様式の光は、**塗りの厚さの変化として現れる。**
- Impact: 無い。**白は光を受けても、何も失わない。**

# 12. EMOTION

- Emotional Arc: 差がある → **差が縮む** → **差が無い。数えられない。**
- Emotional Events: **暗さの差が消えた瞬間**（`4-6s` の頭）。
  ⚠️ **この1本の感情は「喪失」ではない。** **「手がかりの消滅」である**——
  観客は、数えようとして、**数えるものを失う。**

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。**
- Lighting Events: `2-4s` 光が列を手前から奥へ渡る。⚠️ **光源は動かない**——
  **この世界の光は、どこからも来ない。** ゆえに**影は伸びない、縮まない**（§16）。

# 14. AUDIO

- Dialogue: 無し。
- Sound Effects: **無し。** ⚠️ **この1本には、鳴るものが1つも無い**——
  人が居ないので足音も無く、布も無く、風も無い。
- Music: 無し。
- Environment: 空き家の列の、何も鳴っていない空気。
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: **人物は1人も居ない。**
- Spatial: 通りは1つの場所である。**この1本は通りを出ない。**
- Temporal: 朝。S04 の直後である。
- Visual: 一色も出さない。
- Motion: 動くのは光だけである。**カメラは動かない。**
- Sound: 無音。

# 16. CONSTRAINTS

## MUST NOT

- No person in frame. No cat in frame.
- **No close view. No single shutter isolated** —— ⚠️ **総覧である。** 寄れば、この1本は
  「雨戸の1枚」の1本になり、**数えられなくなることが画にならない。**
- **No house numbers. No door numbers. No lettering on the shutters** ——
  ⚠️ **この1本の主題が「数は戻らない」である以上、数を画に置けない。**
- **No lengthening shadows. No shortening shadows** ——
  `no directional light` の実装である。**光は明るさであって、影ではない。**
- No light shaft. No sunbeam. No lens flare. No god rays.
- No noren in frame. No shop front in frame.
- No numerals, no numbers anywhere in the frame.
- **No fully-painted flat vermilion cloth** — 朱はまだ戻っていない。この禁止は S01–S07 が持つ。

## MUST

- Full animation, not limited: **光は6秒のあいだ渡りつづける。**
- **明るさの差が、この6秒で消えること**——ゆえに**最後の1フレームには単位が無い。**
- 白は**照らない**こと。光沢を作らない。
- **列の端から端までが、1つの画に入っていること。**

## PREFER

- 最初の2秒で、**濃淡の差が「順序」として読める**こと。
- 最後の2秒で、**どこから数えはじめるのかが判らない**こと。

## ALLOW

- 雨戸の板の目が、細い線として残ること（**文字ではない**）。

# 17. GENERATION PRIORITIES

1. **数を置かない。** ⚠️ **この1本の最重要の失敗である。** 「雨戸の列」と言えば、モデルは
   番号・表札・数字を置く。**この1本は、数える単位が消えることを撮っている。**
2. **光を光条にしない。** 「朝の光が渡る」は、モデルにとって光芒である。
   **この作品の光は明るさである。**
3. **寄りを挟まない。** 総覧は「広い画」ではない——**列ぜんたいが一度に主題である。**
4. **影を動かさない。** 影が伸びれば、この1本は「時間の経過」の1本になる。
5. **人を入れない。** 空き家の列である。
6. **色を出さない。**
7. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 6-second continuous cinematic take (16:9) of morning light crossing a row of white shutters until the white is the same white everywhere, one clip. Beats, deliberately uneven: [0-2s] the row of white shutters with the near ones lighter and the far ones darker, and that difference in darkness giving the row an order, a one-by-one; [2-4s] the light crosses toward the far end and the difference narrows, and the row stops reading as things standing in a line and starts reading as one continuing surface; [4-6s] the light finishes crossing and the white is the same white everywhere, so that there is no longer any unit to count by. The core beat — the difference narrowing — holds the largest share, two of the six seconds. No person stands in this frame and nobody counts anything: what the shot removes is the unit, not the counter. The light arrives as brightness and never as a ray or a shaft, and it casts nothing, so no shadow lengthens or shortens. Nothing in the frame is coloured and nothing is numbered: no numerals, no house numbers, no door numbers, no lettering on the shutters, no signage of any kind. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on a white that is the same everywhere and gives no place to begin counting from, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. A downtown street returned to blank paper, seen from the front: a long row of closed white shutters running from the near edge of the frame to the far edge, all of it in one frame with no close view anywhere, the paving in front of them, the second-floor verandas and the roofs above. The shutters are white paper where shutters were: flat, unnumbered, unlettered, without house numbers, without door numbers, without plates, with only the grain of the boards left as faint lines. The near end of the row is a little darker than the far end and the difference is small and even, the sort of difference that gives things an order. No cast shadow anywhere, no light shaft, no sunbeam, no lens flare, no god rays. No person, no cat, no noren, no shop front, no numerals, no numbers, no lettering, no signage, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. The subject is brightness moving across a row of flat white surfaces and the row itself never moves: no shutter opens, no shutter closes, no shutter creaks, nothing rocks and nothing shifts. The light travels from the near end of the row to the far end at an even pace, and as it goes the difference in darkness between the near and the far narrows until there is none, and by the end the white is the same white everywhere. The light arrives as a change in brightness only: it is not a beam, not a shaft, not a ray, and it does not sweep like a spotlight. Nothing casts a shadow in either direction, so no shadow lengthens and no shadow shortens while the light moves. No morphing shapes, no motion blur, no stutter, no held frames, no flow or bloom or bleed in the pigment, no fade to grey.

## Camera Prompt

Third-person, in front of the row, at the height of a person standing, with the whole row from the near edge of the frame to the far edge inside one frame and no close view anywhere in the clip, so that the entire row is the subject at once. The camera holds still for the whole six seconds: no push, no pull, no pan, no tilt, no crane, no rack focus, no handheld, no shake, and no move to follow the light as it crosses. [0-2s] holding on the row with its difference in darkness. [2-4s] still holding as the difference narrows, and the camera does not follow the light to the far end. [4-6s] still holding on the white that is the same everywhere, to the end. The style allows one drift; this shot spends none — the one drift in this work is spent later, and spending it here would cost the shot that needs it. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. No sound effects: nothing in this shot makes a sound, because the frame holds no person to make footsteps, no cloth to answer a wind and no wind to answer; the houses have stood empty for ten years and the shot must not give them a sound now. No ambient bed beyond the still air of an empty morning street. Music: none, and no swell, no sting, no melody. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no fully-painted flat vermilion cloth, no person in frame, no cat in frame, no close view, no single shutter isolated, no house numbers, no door numbers, no lettering on the shutters, no lengthening shadows

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. Here the revision is what the shot is about: the light revises the row until nothing in it can be told from anything else in it, and the revision cannot be undone or counted. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither. The palette stays restrained throughout, which here means one white with a difference in it and then without it. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg05-6s-01`
- Segment ID: `01-5`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `6s`
- References: `REF_LOCATION (hakuchizu-mionomachi-street, MEDIUM) ／ REF_GEOGRAPHY (通り.geography, LOW) ／ REF_PROP (白い形.appearance, MEDIUM) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: `通り.base`・`通り.geography`・`白い形.appearance`・`白い形.negative`
- Temporal Structure: `3 beats, NON_UNIFORM — sparse 2s / held 2s / sparse 2s. The core = BEAT 2 at 2-4s (33%)`
- Camera Events: `0 events. One continuous take, camera still for the whole clip`
- Action Events: `ACT_LIGHT_CROSS`
- Audio Events: `no dialogue ／ no sound effects ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。

## Anticipated risks (to check in the first generation)

- **⚠️ 数が入る。** これがこの1本の最重要の失敗である。雨戸・表札・番号は、
  この作品で最も「置かれやすい」ものである。**主題が数の不在である以上、1つでも置けば終わる。**
- **⚠️ 光が光条になる。** 「朝の光が渡る」は光芒を作る。**この作品の光は明るさである。**
- **⚠️ 影が伸びる。** 影で時間を示せば、`no directional light` が破れる。
- **⚠️ 寄りが入る。** 総覧は「広い画」ではない——**列ぜんたいが一度に主題である。**
- **⚠️ 人が入る。** 空き家の列である。
- **⚠️ 6秒で差が消えない。** 消えなければ、この1本は「朝の通り」の1本である。
