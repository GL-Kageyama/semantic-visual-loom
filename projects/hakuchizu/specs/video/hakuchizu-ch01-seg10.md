# ═══ 演出要約 ════════════════════════════════════
# 『白地図』第1章「暖簾」 / 開示 / still —— 払い終える。白にいちばん近かったものが、ひとつ減る
#
#   二階のベランダの白い形のうち、いちばん白に近いものが、ひとつ減る。
#   減りかたは動かない——薄くもならず、飛びもしない。6秒のうちの1秒で、拍を置かずに減る。
#   紐だけが残る。何が減ったのかは分からない——分からないことが、この1本の内容である。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 10/11 / 6s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg10.md`）。

⚠️ **これが開示の1本である。** 草稿 L19「白が、**一枚ぶん減った**。／
**いちばん白に近いものが、いちばん先に戻る。**」
⚠️ **開示は、大きくすることで起きない。** **小ささで起きる**——
**減ったことが、観客に分からないくらいの差で起きる。**
⛔ **分かった瞬間に、この1本は「白い物が消える場面」になる。**

⛔ **この1本に、承認を要する発明がひとつ在る。**
**草稿は「うしろのほうで」としか書かない。** **その「うしろ」を、
隣家の二階の干し場と定めたのは、我々の解釈である。**
**根拠**——**通りから見えて、店の内側でなく、灯より高い位置にある**こと。
⚠️ **承認が下りれば、`shots/hakuchizu-ch01-seg10.yaml` と画像仕様に同じ一行を書く。**

⛔ **§18 の `Negative Prompt` が S09・S11 と同一である理由。**
`ledger.disclosure` はこの1本の開示点（`灯.支払い: 済んだ`）を **`negative: covered`** と宣言している——
**ゆえに `L10` は「直前の動画仕様（S09）と、否定節の集合が一致すること」を要求する。**
⚠️ **落とした節がある。** `no lifted cloth`・`no swinging cloth`・`no movement in the vermilion cloth` は
**3本のどれかで偽である**（S09 では布が鳴る）。**ゆえに集合から外れている。**
**共有するのは、3本すべてにとって真である節だけである。**

---

# 1. VIDEO

- Duration: `6s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: one white shape on the line goes back to paper, and the line is left empty — and no one can say which one went.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01）。
- 白は音を持たない。音が戻るのは、色が戻ったところからである（S09）。
- 白の下には、人がいた気配が透けている（S03）。
- 思い出したぶんだけ、白のなかから色が立ち上がる（S08）。
- **「いちばん白に近いものが、いちばん先に戻る。」**（草稿 L19）
  ⚠️ **これはこの1本の法である。** **ゆえに減るのは、いちばん白いものではない**——
  **いちばん「白に近い」ものである。** **その差は、見て分かる差ではない。**
- **数は町を戻さない**（S05）。**ゆえに灯は数えない**——
  **数えれば、減ったものに名前が付く。**
- 覚えることは、払うことである（S11）。

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
- Color Language: ⚠️ **この1本で減るのは、色ではなく白である。** **朱は減らない。**
- Texture: ⚠️ **白い形は、輪郭線を持たない。** **白そのものである**——
  **縁を描けば、それは「白い物」になり、減ったときに「物が消えた」になる。**
- Rendering: ⚠️ **戻ることは、紙が置いた白を引き取ることである。**
  **縁から先に、紙の白に戻る**——**グラデーションではない**（S11 と同じ法）。
- Visual Density: ⚠️ **この1本は、11本のうちで最も密度が低い。** **それが正しい。**
- Time: `朝`
- Atmosphere: 干し場の白。**一枚ぶん、少ない。** ⚠️ **誰にも、どれが減ったか分からない。**

# 3. SUBJECTS

## 白い形（干し場の洗濯物）

- Reference: `白い形.appearance`・`白い形.negative`（`attached` に従う）
- Appearance: 隣家の二階の干し場に、白い形が数枚。**輪郭線を持たない、白そのもの。**
  ⚠️ **一枚だけ、わずかに白に近い。** **「いちばん白い」ではない**——
  **白に近い、という差である。**
- Behavior: ⚠️ **揺れない。** **風はもう通っていない**（S09 で通り過ぎた）。
  **一枚が、紙の白に戻る**——**縁から先に。**
- Continuity Requirements: ⚠️ **減ったあと、干し場の竿は空く。**
  **空いた竿は、白いままである**——**竿の形を描かない。**
  **「干してあった」と分かる形を残さない**——**残せば、それは不在の印になる。**

## 灯

- Reference: `灯.identity`・`灯.states.支払いの前`（`attached` に従う）
  ⚠️ **支払いは、この1本のあいだに済む**（`ledger.disclosure`）。
  **だが、済んだことを画にしない。**
- Appearance: 後ろ姿、輪郭。**画の縁、下のほう。** ⚠️ **顔は描かない。**
- Behavior: ⚠️ **数えない。指を折らない。目を細めない。**
  **立ち止まって、見ているだけである。**
  ⚠️ **減ったことに気づいた顔を描かない**——**気づきは、この1本では起きない。**

# 4. ENVIRONMENT

- Location: `暖簾の店の前`（`.base`・`.geography`・`.states.朱が戻った`）
  ⚠️ **画は店の前から動かない。** **干し場は、通りの奥に見えている。**
- Environment Elements: 店の前の石畳、**朱い暖簾**、奥に隣家の二階の干し場。
  ⚠️ **店の内側は画に入らない**（`PLAN.md` §0-f）。
  ⛔ **「隣家の二階の干し場」は我々の解釈である**（冒頭の註）。
- Environmental Behavior: ⚠️ **風は無い。** **S09 で通り過ぎた。**
  **この1本で動くのは、減る一枚だけである。**

# 5. OBJECTS

- `白い形` — この1本の主題である。**一枚が減る。**
- `暖簾` — 画に入る。⚠️ **動かない。** **この1本では、もう鳴らない。**
- `薬缶` — ⚠️ **この1本では鳴らない。** **音も無い**（S09 で一度鳴いた）。

# 6. REFERENCES

- REF_LOCATION: `暖簾の店の前.base` (HIGH)
- REF_GEOGRAPHY: `暖簾の店の前.geography` (MEDIUM)
- REF_CHARACTER: `灯.identity` (HIGH)
- REF_PROP: `白い形.appearance` (HIGH — この1本の主題である)
- REF_PROP: `暖簾.appearance` (MEDIUM — ⚠️ **画には在るが、動かない**)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — 開示点と `covered` 宣言)

# 7. NARRATIVE

- Core Event: **白い形が、一枚ぶん減る。**
- Beginning: 干し場に白い形が並んでいる。**一枚だけ、わずかに白に近い。**
- Turn: **その一枚が、紙の白に戻る。** ⚠️ **縁から先に。** **一瞬で消えない。**
- Peak: ⚠️ **無い。** **この1本に山は無い**——
  **山は S08 である。** **この1本は、山のあとに残る差分である。**
- Pull: **竿が、白いままである。** ⚠️ **何が減ったのか、誰にも分からない。**
  **灯は数えない。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `held` — 干し場の白。**一枚だけ、わずかに白に近い。**
  - BEAT 2 `2-3s` — density: `dense` — **一枚が、紙の白に戻る。** ⚠️ **1秒。この1本の核。**
  - BEAT 3 `3-4s` — density: `held` — ⚠️ **観客が「何が減ったのか分からない」ことを確かめる1秒。**
  - BEAT 4 `4-6s` — density: `sparse` — 竿が白いままである。**灯は数えない。**
- Temporal Density: ⚠️ **核（`2-3s`）は、この1本で最も短い拍である**（`dense`・1秒）。
  **残る5秒は、すべて「減ったあと」である。**
  ⚠️ **この配分が、開示を小さく保つ**——**見せ場を長く取れば、開示は大きくなる。**

# 9. ACTION

- `ACT_SEE` — Before: 干し場に白い形が並んでいる。After: 変わらない。**この2秒で、観客は並びを覚える。**
  ⚠️ **覚えさせなければ、減ったことは分からない**——**分かる必要は無いが、気づく余地は要る。**
- `ACT_GO` — Before: 一枚が、白に近い。After: **その一枚が、紙の白に戻っている。**
  Causes: ⚠️ **無い。** **払いが済んだからである。**
  **この1本に、外部の原因を置かない**——**風でも、手でも、音でもない。**
- `ACT_EMPTY` — Before: 干し場の竿が並んでいる。After: **竿が、白いままである。**
  ⚠️ **空いたことが分かる形を残さない。** **竿を描かない。**
  **「干してあった場所」を描けば、不在が印になる。**
- `ACT_STAND` — Before: 灯が見ている。After: 変わらない。**灯は数えない。**
  ⚠️ **この節は、変化を持たない。** **それがこの節の内容である。**

# 10. CAMERA

- Camera Language: 三人称、店の前から、**干し場と、下に居る灯が同じ画に入る。**
  ⚠️ **干し場へ寄らない。** **寄れば、減るものが主題になる。**
- Camera Events: **無い。**
- Camera Behavior: **6秒のあいだ、一度も動かない。**
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。**
  ⚠️ **特に、減る瞬間に寄らない。** **寄りは「見せ場」の文法であり、**
  **この1本の開示は、見せ場ではない。**

# 11. MOTION

⚠️ **`still` の1本である。** **ゆえにこの節は「何も動かない」ことを書くために在る**
（`L24`——`still` は §11 が空だと落ちる）。

## Subject Motion

**動くものは、ひとつだけである。**
**白い形の一枚が、紙の白に戻る**——⚠️ **縁から先に、紙が引き取るように。**
**グラデーションではない。** **淡くなるのでもない**——**紙になるのである。**
⚠️ **他の白い形は動かない。** **灯も動かない。** **朱も動かない、鳴らない。**
⚠️ **減る速さは、遅い。** **この1秒で、観客は「見なかったことにする」しかない。**

## Object Motion

**無い。** ⚠️ **竿は揺れない。** **布は動かない。** **石畳は動かない。**

## Environmental Motion

**無い。** ⚠️ **風は通らない**（S09 で通り過ぎた）。
**この1本の動きは、白の内側でだけ起きる。**

## Physical Characteristics

- Weight: ⚠️ **白い形は、重さを持たない。** **洗濯物の重さを描けば、それは物である。**
- Inertia: **無い。** **戻ることは、慣性を持たない。**
- Acceleration: **無い。** **一定の速さで、縁から戻る。**
- Fluidity: ⚠️ **滑らかではない。** **紙が引き取るのである**——**角を持つ。**
- Impact: **無い。**

# 12. EMOTION

- Emotional Arc: 並んでいる → **一枚減る** → **誰も気づかない** → 数えない。
- Emotional Events: ⚠️ **この1本の感情は、観客の側にしか無い。**
  **灯に気づかせない。** **気づかせれば、この話は「数える話」になる**——
  **この話は、数えない話である。**
- ⚠️ **強度は最も低い。** **それが正しい。** **ここは山ではない。**

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。**
- Lighting Events: **無い。** ⚠️ **減る瞬間に光を当てない。** **当てれば、それは演出である。**

# 14. AUDIO

- Dialogue: **無し。** 台詞も、ナレーションも無い（`PLAN.md` §0-e）。
- Sound Effects: ⚠️ **この1本、音がひとつも無い。** **薬缶も、もう鳴らない。**
  **布も鳴らない。** **減ることに音は無い**——
  **音を置けば、白が減ることは「出来事」になる。**
- Music: 無し。
- Environment: **S09 で戻った音が、この1本では引いている。**
  ⚠️ **戻った音も、減る。**
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註——
  **発話のある動画に中国語の字幕が焼かれた実測**）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: **灯——後ろ姿、輪郭、顔は描かない。** ⚠️ **数えない。動かない。**
- Spatial: 店の前から、奥の干し場までが一つの画に入る。**店の内側へ入らない。**
- Temporal: 朝。S09 の直後である。**朱は戻り、まだ濡れている。**
- Visual: 朱と藍と、白。⚠️ **この1本で減るのは白である。**
- Motion: **一枚だけが減る。** 他は動かない。**カメラは動かない。**
- Sound: **無い。** ⚠️ **S09 で戻った音が、ここでは引いている。**

# 16. CONSTRAINTS

⚠️ **この節は、S09・S11 と同一の `Negative Prompt` を作る**（`L10`——`covered` 宣言）。
**内訳を分けて書く。**

## MUST NOT

**この1本（S10）の危険:**
- **No numerals, no numbers. No counting marks** —— ⚠️ **この1本の最重要の失敗である。**
  **数えれば、減ったものに名前が付く。** 草稿 L19 は数を書いていない。
- **No visible person among the white shapes. No figure on the veranda**
  —— ⚠️ **洗濯物は洗濯物である。** **人が居れば、それは「居なくなった人」の画になる。**
- **No lifted or swinging laundry** —— ⚠️ **風は無い。** **揺れれば、減ることに原因ができる。**
- **No outline around the white shapes. No shadow under the white shapes**
  —— ⚠️ **輪郭と影は、白い形を「物」にする。** **物になれば、消えるのは物である。**
- **No marks of departure** —— ⚠️ **去った印を置かない。** **この話は、去ったことを写さない。**
  ⛔ **`ledger.disclosure` の `灯.支払い: 済んだ` は、
  「減った白の正体を誰も名指しできないこと」そのものである。**
- **No goods drawn on the cloth. No fish drawn on the cloth. No bundle or package on the cloth.
  No illustration on the cloth. No emblem or sign on the noren. No scales and no drawn eye** ——
  ⛔ **布に載っているのは、格子だけである。** **桝目の中に、何も描かない。**
  ⚠️ **2026-09-22 の著者の裁定（第二）である**——「**暖簾の上に、具体的なモチーフは重ならない**」。
  **ゆえに S07 が置くものも、格子だけになった**（`hakuchizu-ch01-seg07.md` §9）。
- **No checkered pattern. No plaid. No printed textile pattern. No checkerboard** ——
  ⚠️ **朱の下に在るのは、地図の経緯線であって、布の柄ではない。**
  ⚠️ **朱い布に格子が残るので、この3本では特に柄に読まれやすい**——
  **`bible.negative_base` にも、`video-spec` カードの `Negative` にも、柄を禁じる語は無い。**
  **ゆえに §16 に節を立て、§18 の `Negative Prompt` に足した**（`PLAN.md` §4-e）。
  **S09〜S11 はその布を保つので、同じ6節をこの3本が同じ形で負う**（`L10` の同一条件）。
- No visible face on the figure. No cat in frame.
- No lettering. No legible text on the noren. No shop name on the noren.
- No shop interior. No shopkeeper. No face on the cloth. No drawn face. No typography.

**S09 から来る危険**（同じ集合に居るため。**消せば `L10` が鳴る**）:
- **No person passing under the noren. No second person** —— **誰もくぐらない。**
- **No visible kettle as a present object. No visible stove or fire. No steam. No smoke**
  —— ⚠️ **この1本では、薬缶は鳴りもしない。**
- No door opening. No second movement in the cloth.

**S11 から来る危険**（同じ集合に居るため。**消せば `L10` が鳴る**）:
- **No cloth following the hand. No stretched or pulled cloth. No hand painting the cloth. No brush in frame**
  —— **この1本では、手は朱に触れない。**
- **No called or written name** —— ⚠️ **この話のフックである。**
  **ここでも、名前は呼ばれないし、書かれない。**
- No pale gradient on the hand. No soft photographic shadow.

## MUST

- Full animation, not limited.
- **一枚だけが減ること。** **二枚を減らさない。**
- **減り方が「紙に戻る」であること。** **淡くなるのでも、消えるのでもない。**
- **縁から先に戻ること。** **グラデーションにしないこと。**
- **空いた竿を描かないこと。** **不在の印を残さない。**
- **灯が数えないこと。** **気づいた顔を描かないこと。**
- **カメラが寄らないこと。** **減る瞬間に、カメラが答えないこと。**

## PREFER

- 減る一枚の差が、**「いちばん白い」ではなく「白に近い」**であること。
  ⚠️ **差が大きければ、開示は「白い物が消えた」になる。**

## ALLOW

- 干し場の白い形が、**数枚、互いに少しずつ違う白**であること
  （⚠️ **同じ白を並べれば、減った一枚が目立つ**）。

# 17. GENERATION PRIORITIES

1. **数えない、名指ししない。** ⚠️ **この1本の最重要の失敗である。**
   「一枚減る」と言えば、モデルは**数字**か**印**を置く。**どちらも、この話を殺す。**
2. **一枚だけ減らす。** 二枚減れば、それは「減っている」という状態になる。
3. **減り方を「淡く」にしない。** **紙に戻るのである。**
4. **輪郭と影を描かない。** 白い形を「物」にしない。
5. **干し場に人を出さない。** **揺らさない。**
6. **カメラを動かさない、寄らない。**
7. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 6-second continuous cinematic take (16:9) of one white shape going back to paper on a laundry line, one clip. Beats, deliberately uneven: [0-2s] the white shapes hanging on the line in the second-floor drying place of the neighbouring house, one of them a shade nearer to white than the others, and it is not the whitest one; [2-3s] that one shape goes back to paper, the paper taking it back from its edge first, and it does not fade and it does not disappear — it becomes paper; [3-4s] the second in which nobody can say which one went, and the line holds; [4-6s] the pole is left white and the shape is not there, and 灯 below does not count. The core beat — the single second in which the shape goes — is the shortest beat in the shot, and the five seconds around it are the after, because a long held look would make the disclosure large and this disclosure has to be small: the difference between the shape that went and the ones that stayed is a shade, not a contrast, and someone watching may miss it, and missing it is permitted. 灯 stands at the lower edge of the frame and does not count, does not fold a finger and does not narrow the eyes: counting would give the missing thing a name, and nobody may be able to name what went — that is the content. No cause is placed on this: no wind, no hand, no sound. The vermilion noren is in the frame and does not move. Wind has already passed through in the previous shot and does not return here. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on the white pole and the white shapes that stayed, with the empty place not marked, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. The front of a shop closed for the morning on a street returned to blank paper, with the second-floor drying place of the neighbouring house behind it, all inside one frame: the vermilion noren in the frame and not moving, the stone paving, and 灯 seen from behind at the lower edge of the frame, back and outline, face not drawn. The white shapes on the line are white itself with no outline line and no drawn edge, each a slightly different white from the others, and one of them a shade nearer to white; the pole is plain white paper and is not drawn as an object, and nothing marks the place where a shape was. The shop's interior is not in the frame; no kettle, no stove, no fire, no steam and no smoke are in the frame; no sunbeam, no light shaft, no lens flare, no cast shadow, no soft photographic shadow and no shadow under the white shapes. No person on the veranda, no figure among the white shapes, no second person, no shopkeeper, no cat, no lettering, no shop name, no signage, no numerals, no numbers, no tally marks, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. One white shape and no other goes back to paper: the paper takes it back from its edge first, at a slow even rate, and the shape becomes paper rather than fading, rather than growing pale, rather than dissolving and rather than disappearing suddenly; there is no gradient and no soft dissolve across it. No second shape changes, no second shape is added and nothing else on the line moves. The laundry does not lift and does not swing, because there is no wind in this shot. 灯 stands and does not move, does not count, does not fold a finger and does not raise the eyes. The vermilion cloth does not move and does not sound. No morphing shapes, no motion blur, no stutter, no held frames, no flow or bloom or bleed in the pigment, no slow motion, no reversed motion.

## Camera Prompt

Third-person, in front of the shop, at the height of a person standing, with the drying place and 灯 below it inside one frame. The camera holds still for the whole six seconds: no push, no pull, no pan, no tilt, no rack focus, no handheld, no shake, and above all no move closer at the moment the shape goes — a move closer at that moment would make the disclosure a set piece, and this disclosure is not a set piece. [0-2s] holding on the line. [2-3s] still holding as the shape goes, and the camera does not answer it. [3-4s] still holding on the line as it stands. [4-6s] still holding on the white pole and the white shapes that stayed, to the end. The style allows one drift; this shot spends none — the one drift in this work was spent in the eighth shot, and there is only one. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. No sound effects: in this shot nothing sounds — the cloth does not sound, the kettle does not sound and there is no sound to the reduction, because a sound on it would turn the white going back to paper into an event. No music, nothing ambient beyond the air of the street, and no ambient bed rising to fill the gap. The return of sound in the previous shot is receding here, and that receding is part of this shot. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no flat vermilion without pigment body, no dry even vermilion paint, no person passing under the noren, no second person, no visible person among the white shapes, no visible kettle as a present object, no visible stove or fire, no steam, no smoke, no door opening, no second movement in the cloth, no cloth following the hand, no stretched or pulled cloth, no figure on the veranda, no lifted or swinging laundry, no outline around the white shapes, no shadow under the white shapes, no marks of departure, no counting marks, no called or written name, no pale gradient on the hand, no soft photographic shadow, no visible face on the figure, no cat in frame, no hand painting the cloth, no brush in frame, no goods drawn on the cloth, no fish drawn on the cloth, no bundle or package on the cloth, no illustration on the cloth, no emblem or sign on the noren, no scales and no drawn eye, no checkered pattern, no plaid, no printed textile pattern, no checkerboard

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. Here the same law runs in reverse: a laid white wash is taken back, and because gouache is opaque the taking-back is a revision too — the paper comes back from the edge first and the earlier state of the shape stays readable in what remains, so the reduction is a correction rather than an erasure, and it does not become a fade. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither. The palette stays restrained throughout, and the white ground stays pure white. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg10-6s-01`
- Segment ID: `01-10`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `6s`
- References: `REF_LOCATION (暖簾の店の前.base, HIGH) ／ REF_GEOGRAPHY (暖簾の店の前.geography, MEDIUM) ／ REF_CHARACTER (灯.identity, HIGH) ／ REF_PROP (白い形.appearance, HIGH) ／ REF_PROP (暖簾.appearance, MEDIUM) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: `灯.identity`・`灯.states.支払いの前`・`灯.negatives`・`暖簾の店の前.base`・`暖簾の店の前.geography`・`暖簾の店の前.states.朱が戻った`・`白い形.appearance`・`白い形.negative`・`暖簾.appearance`・`暖簾.negative`
- Temporal Structure: `4 beats, NON_UNIFORM — held 2s / dense 1s / held 1s / sparse 2s. The core = BEAT 2 at 2-3s (17% — the shortest and densest beat)`
- Camera Events: `0 events. One continuous take, camera still for the whole clip`
- Action Events: `ACT_SEE → ACT_GO → ACT_EMPTY → ACT_STAND`
- Audio Events: `no dialogue ／ no sound effects at all ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`
- Disclosure point: **`灯.支払い: 済んだ`**（`negative: covered`）
  ⚠️ **この開示は、画の外で起きている。** **画に写るのは、その差だけである**——
  **ゆえに `covered`（否定節は変わらない）で正しい。**
  ⛔ **「減った白の正体」は、この作品のどこでも名指しされない。**
  **名指しできないことが内容である**（草稿 L19 は数を書かない）。

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。

## Anticipated risks (to check in the first generation)

- **⚠️ 数える。** 減った枚数、残った枚数、印。**この1本の最重要の失敗である。**
- **⚠️ 差が大きすぎる。** 「いちばん白に近い」が「いちばん白い」になり、
  コントラストになれば、**開示が「白い物が消えた」になる。**
- **⚠️ 二枚減る。** 状態になる。
- **⚠️ 淡くなる。** **紙に戻らなければならない。** グラデーションは白を「光」にする。
- **⚠️ 輪郭と影が付く。** 白い形が「物」になる。
- **⚠️ 干し場に人が居る。** 洗濯物が「居なくなった人」の画になる。
- **⚠️ 揺れる。** 風が無いのに揺れれば、減ることに原因ができる。
- **⚠️ 空いた竿が描かれる。** 不在の印になる。
- **⚠️ カメラが寄る。** 開示が見せ場になる。
- **⚠️ 灯が気づく。** 気づけば、数える話になる。
- **⛔ 隣家の二階の干し場が、承認されない可能性がある**（冒頭の註）。
  **その場合、`place` は「通りの奥」まで戻る**——**`shots/hakuchizu-ch01-seg10.yaml` から直す。**
