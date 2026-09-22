# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 9/11 / 7s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg09.md`）。

⚠️ **この1本の変化は「音が戻ること」である。そして、戻らないものが画の縁を決める。**
世界の法——**「白は音を持たない。音が戻るのは、色が戻ったところからである」**（`bible.world.rules`）。
⚠️ **ゆえにこの1本は、S08 の直後にしか置けない。** **法の順序そのものを実演している。**
⚠️ **くぐる者は来ない。** 草稿 L17「揺れる朱の下を、**誰かがくぐるはずだった**」——
**「はずだった」を画にする方法は、揺れの下を空のまま置くことである。**
**待たせる、という演出をしない**——**この1本は、待つのではなく、来なかったことを写す。**
⚠️ **この作品でいちばん短い出来事が、この1本の核である**（`2-3s`・`dense`・1秒）。

⛔ **§18 の `Negative Prompt` が S10・S11 と同一である理由。**
`ledger.disclosure` は S10 の開示点（`灯.支払い: 済んだ`）と S11 の開示点（`灯.渡した声: 名を失った`）を
ともに **`negative: covered`** と宣言している——
**ゆえに `L10` は「3本の否定節の集合が一致すること」を要求する。**
⚠️ **したがって、この集合は3本ぶんの危険を1つの集合として持つ。**
⚠️ **落とした節がある。** `no movement in the vermilion cloth`・`no swinging cloth`・
`no hand touching the cloth` は、**この1本では偽である**（布は一度鳴り、S11 では手が触れる）。
**ゆえに「一度だけ」を否定節で負わせず、§11 と §10 が肯定形で負う。**
**共有するのは、3本すべてにとって真である節だけである。**

---

# 1. VIDEO

- Duration: `7s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the vermilion cloth answers the wind once, and the sound of the world comes back behind it.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01）。
- **「白は音を持たない。白のなかに音は無い——音が戻るのは、色が戻ったところからである。」**
  ⚠️ **この1本が実演するのはこの行である。** **S08 の直後にしか置けない。**
- 白の下には、人がいた気配が透けている（S03）。
- 思い出したぶんだけ、白のなかから色が立ち上がる（S08）。
- 覚えることは、払うことである（S10・S11）。⚠️ **この1本では、まだ払われていない。**
- 数は町を戻さない（S05・S10）。
- 置いた色は、もう白に戻らない（S11）。
  ⚠️ **この1本は、この法の「音」版である**——**戻った音は、もう引っ込まない。**

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
- Color Language: **朱と藍。** ⚠️ **この1本の朱は、S08 の終わりの朱と同じである**——
  **まだ乾いていない。** ゆえに**この1本でも濡れを見せる。**
- Texture: ⚠️ **音は、この様式の物理の外にある。** **音を画で描かない**——
  **鳴ることは、布の縁が動くことで示される。** 音そのものは §14 が負う。
- Rendering: ⚠️ **揺れることは、房の線が一度だけ別の位置に置き直されることである。**
  **前の線は消えない**（`the revision stays visible`）——**ゆえに揺れは、布の側に一度ぶんだけ残る。**
- Visual Density: **`2-3s` の1秒が、この作品で最も濃い1秒である。**
- Time: `朝`
- Atmosphere: 朱い暖簾。**風が来て、今度は布が答える。**

# 3. SUBJECTS

## 朱い布

- Reference: `暖簾.appearance`・`暖簾.negative`・`暖簾の店の前.states.朱が戻った`（`attached` に従う）
- Appearance: 染めて二度目の冬を越した褪せた朱。**房は藍。** ⚠️ **まだ乾いていない。**
- Behavior: ⚠️ **一度だけ鳴る。** ぱさり、で終わる——**翻らない、はためかない、鳴りつづけない。**
  **布の下辺が、奥からの空気で内側へ少し吸われる**——**戸が開く気配である。**
  ⚠️ **気配は画にしない。** **画にするのは、布が内側へ動くことだけである。**
- Continuity Requirements: ⚠️ **同じ風を、S06 は受けている。** S06 では布が答えず、ここでは布が鳴る——
  **風の強さは変えていない。変わったのは布のほうである。**

## 灯

- Reference: `灯.identity`・`灯.states.支払いの前`（`attached` に従う）
  ⚠️ **支払いはまだ済んでいない。指先はまだ色を持っている。**
- Appearance: 後ろ姿、輪郭。⚠️ **顔は描かない。**
- Behavior: ⚠️ **動かない。音に身体を向けない**——
  **二十年、おなじ順で来ている者が、音ごときで振り向くはずがない。**

## 薬缶（音だけ）

- Reference: `薬缶.appearance`・`薬缶.negative`（`attached` に従う）
- ⚠️ **薬缶は画に出ない。** **音と、覚えられている形だけである**（`ledger.props.薬缶`）。
  **ゆえに `attached` に在ることは、画に出ることではない。**

# 4. ENVIRONMENT

- Location: `暖簾の店の前`（`.base`・`.geography`・`.states.朱が戻った`）
- Environment Elements: 店の前の石畳、**朱い暖簾**、閉じた店。
  ⚠️ **店の内側は画に入らない**（`PLAN.md` §0-f）。
- Environmental Behavior: **風が一度通る。** ⚠️ **埃はもう要らない**（それは S06 の装置である）——
  **この1本の風は、布が答えることで示される。**

# 5. OBJECTS

- `暖簾` — この1本の主題である。**鳴るのはこの布である。**
- `薬缶` — ⚠️ **画に出ない。** 音だけである。
- `白い形`・`水の跡` — **この1本には無い**（洗濯物は S10 である）。

# 6. REFERENCES

- REF_LOCATION: `暖簾の店の前.base` (HIGH)
- REF_GEOGRAPHY: `暖簾の店の前.geography` (MEDIUM)
- REF_CHARACTER: `灯.identity` (HIGH)
- REF_PROP: `暖簾.appearance` (HIGH — この1本の主題である)
- REF_PROP: `薬缶.appearance` (LOW — ⚠️ **音としてのみ。画には出ない**)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — 薬缶の禁止と、3本共有の `covered` 宣言)

# 7. NARRATIVE

- Core Event: 布が風を受けて、ぱさりと鳴る。**音が戻る。**
- Beginning: 朱い布。**鳴っていない。** ⚠️ **この2秒の無音が要る**——
  **無音のあとにしか、音は戻らない。**
- Turn: **布が鳴る。朱が揺れる。** ⚠️ **この1秒が、この作品でいちばん短い出来事である。**
- Peak: **揺れの下は、空である。** 石畳が白いまま見えている。
- Pull: 奥で薬缶が鳴る。**湯の音が白のなかをひとつずつ満たしていく。**
  ⚠️ **湯気の匂いも、店の奥の暖かさも、まだ白のままである。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — 朱い布。**鳴っていない。** 房が下へ垂れている。
  - BEAT 2 `2-3s` — density: `dense` — **布が鳴る。朱が揺れる。** ⚠️ **1秒。最短で、最も濃い。**
  - BEAT 3 `3-5s` — density: `held` — **揺れの下は空である。** 石畳が白いまま見えている。
  - BEAT 4 `5-7s` — density: `sparse` — 奥で**薬缶**が鳴る。**匂いは来ない、暖かさも来ない。**
- Temporal Density: ⚠️ **核（`2-3s`）は、この1本で最も短い拍である。**
  **山（S08）の12秒とは、配分の仕方が逆である**——**あちらは4秒の核を長い溜めで挟み、
  こちらは1秒の核を長い余韻で挟む。**
  ⚠️ **不均等の在り処は「1秒に、4つのことが同時に起きる」ことである。**

# 9. ACTION

- `ACT_LISTEN` — Before: 朱い布は鳴っていない。After: 変わらない。**この2秒は、鳴る前の無音である。**
  ⚠️ **無音を置かなければ、ぱさりは効果音になる。**
- `ACT_SOUND` — Before: 布は鳴っていない。After: **布が一度鳴り、朱が一度揺れている。**
  Causes: 風。⚠️ **一度だけである。二度は揺れない**（`the revision stays visible`）。
- `ACT_EMPTY` — Before: 布の下辺が内側へ吸われている。After: **揺れの下の石畳が、白いまま見えている。**
  ⚠️ **誰も通らない。** **戸が開く気配は、布が内側へ動くことだけである。**
- `ACT_KETTLE` — Before: 石畳の上に音が無い。After: **奥で薬缶が鳴り、湯の音が白を満たしていく。**
  ⚠️ **薬缶は画に出ない。** **匂いも暖かさも来ない。**

# 10. CAMERA

- Camera Language: 三人称、店の前、**布と、その下の地面が同じ画に入る。**
  ⚠️ **カメラは店の奥へ入らない**（`PLAN.md` §0-f）——
  **ゆえに「奥で鳴る」は、決して画にならない。**
- Camera Events: `0-2s` 布に留まる。`2-3s` 布が鳴る——**この1秒、カメラは何もしない。**
  `3-5s` 揺れの下の石畳に留まる。`5-7s` 布に留まったまま終わる。
- Camera Behavior: **7秒のあいだ、一度も動かない。**
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。** ⚠️ **使ったのは前の1本（S08）である。**
  ⚠️ **辞退は辞退として書く**（`skills/staging/SKILL.md`）。

# 11. MOTION

## Subject Motion

⚠️ **ここが、この1本で最も注意を要する節である。**
**布は一度だけ動く。** 揺れることは、**房の線が一度だけ別の位置に置き直されることである**——
⚠️ **前の線は消えない**（`the revision stays visible`）。
**ゆえに「一度だけ」は、否定節ではなく、この節が肯定形で負う。**
**二度目の揺れは起きない。** 布の下辺が内側へ吸われるのは、**同じ一度のうちである。**

## Object Motion

**布以外に動くものは無い。** 石畳は動かず、戸は開かない。
⚠️ **薬缶は画に無いので、動くこともない。**

## Environmental Motion

**風が一度通る。** ⚠️ **強くならない**——**吹き抜けるのではなく、通る。**
⚠️ **風は布の縁でだけ見える。**

## Physical Characteristics

- Weight: **布は、まだ濡れた絵の具を持っている。** ゆえに揺れは**少し重い**——
  ぱさり、という一度で終わる重さである。
- Inertia: ⚠️ **揺れは続かない。** 慣性で揺れつづければ、それは別の布である。
- Acceleration: 無い。**一度の揺れに、加速は無い。**
- Fluidity: ⚠️ **房の線は、滑らかに揺れない。** **置き直される**——ゆえに揺れは角を持つ。
- Impact: ⚠️ **音は衝撃ではない。** **一度の接触である。**

# 12. EMOTION

- Emotional Arc: 無音 → **鳴る** → 空 → **奥で鳴る。匂いは来ない。**
- Emotional Events: **布が鳴った1秒。** 強度は中——
  ⚠️ **反応は、灯の側で起きる。** だが**灯は動かない**——
  **応答が「動かないこと」であることは、応答しないことではない。**
  ゆえにこの1本の感情は、**観客の耳の側にだけ生まれる。**

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。** 影は落ちない。
- Lighting Events: **無い。** ⚠️ **音を光で示さない。**

# 14. AUDIO

⚠️ **この1本の主役は、この節である。**

- Dialogue: **無し。** 台詞も、ナレーションも無い（`PLAN.md` §0-e）。
- Sound Effects:
  - **`2-3s`——布が一度鳴る。** 草稿 L15「布が風を受けて、**ぱさりと鳴る**。
    **白のなかにはなかった音だった。**」⚠️ **一度だけである。短い。** 余韻を引かない。
  - **`5-7s`——奥で薬缶が鳴る。** 草稿 L17「二十年、この時間に薬缶が鳴る。
    **湯の音が白のなかをひとつずつ満たしていく。**」
    ⚠️ **薬缶も湯も画に出ない**（`ledger.props.薬缶`——**音と、覚えられている形だけである**）。
  - ⚠️ **この2つ以外の音を足さない。** 通りに人も車も居ない。
- Music: 無し。⛔ **ここに音楽を置けば、音が戻ることは「音響効果」になる。**
- Environment: **この1本から、白は音を持ちはじめる。**
  ⚠️ **S01 から S08 までの無音が、この1本で支払われる。**
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註——
  **発話のある動画に中国語の字幕が焼かれた実測**）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: **灯——後ろ姿、輪郭、顔は描かない。** ⚠️ **動かない。振り向かない。**
- Spatial: 店の前である。**この1本は店の前を出ない。店の内側へ入らない。**
- Temporal: 朝。S08 の直後である。**朱は戻り、まだ濡れている。**
- Visual: 朱と藍。
- Motion: **布は一度だけ動く。** 動くのはそれだけである。**カメラは動かない。**
- Sound: **布と薬缶。** ⚠️ **この1本で、白に音が戻る。**

# 16. CONSTRAINTS

⚠️ **この節は、S10・S11 と同一の `Negative Prompt` を作る**（`L10`——2つの `covered` 宣言）。
**内訳を分けて書く。**

## MUST NOT

**この1本（S09）の危険:**
- **No person passing under the noren. No passer-by** —— ⚠️ **この1本の主題である。**
  **出せば、来なかったことごと消える。**
- **No visible kettle as a present object. No visible stove or fire**
  —— ⚠️ **薬缶は音と、覚えられている形だけである。**
- **No steam. No smoke** —— 草稿 L17「**湯気の匂いも、店の奥の暖かさも、まだ白のままだった**」。
  **白のままのものを、白から出さない。**
- **No door opening** —— **気配は画にしない。** **画にするのは、布が内側へ動くことだけである。**
- **No second movement in the cloth** —— ⚠️ **「一度だけ」を否定節で負う唯一の節である。**
  **二度目の揺れを禁じる**——**「揺れるな」ではない**（布は一度鳴る）。
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
- No numerals, no numbers. No lettering. No legible text on the noren. No shop name on the noren.
- No shop interior. No shopkeeper. No face on the cloth. No drawn face.

**S10 から来る危険**（同じ集合に居るため。**消せば `L10` が鳴る**）:
- No visible person among the white shapes. No figure on the veranda.
- No lifted or swinging laundry. No outline around the white shapes. No shadow under the white shapes.
- No marks of departure. No counting marks.

**S11 から来る危険**（同じ集合に居るため。**消せば `L10` が鳴る**）:
- **No cloth following the hand. No stretched or pulled cloth** ——
  **手が離れるとき、朱は引かれない。**
- **No called or written name** —— ⚠️ **この話のフックである。呼べば、灯が失ったものが戻る。**
- No pale gradient on the hand. No soft photographic shadow.
- No hand painting the cloth. No brush in frame —— **この1本の色は、誰も塗らない。**

## MUST

- Full animation, not limited.
- **布が一度だけ鳴ること。** 二度目を作らないこと。
- **`0-2s` の無音を置くこと**——**無音のあとにしか、音は戻らない。**
- **揺れの下に、誰も通らないこと。** 石畳は白いまま見える。
- **薬缶を画に出さないこと。** 音だけである。
- **匂いと暖かさを出さないこと**——**戻らなかったものの側で終わる。**
- **カメラが店の奥へ入らないこと。** **越えない。**

## PREFER

- 房の線が、**一度だけ別の位置に置き直され、前の線が残っている**こと。
- 薬缶の音が、**遠いこと**——奥から聞こえること。

## ALLOW

- 石畳の上に、布の影が**わずかに落ちる**こと（⚠️ **方向性の光は無いので、これは影ではなく濃みである**）。

# 17. GENERATION PRIORITIES

1. **くぐる者を出さない。** ⚠️ **この1本の最重要の失敗である。** 「揺れる暖簾」と言えば、
   モデルは**くぐる人**を置く。**この1本は、来なかったことを写している。**
2. **薬缶を出さない。** 「奥で薬缶が鳴る」は、モデルにとって**薬缶の画**である。
   **音は音である。**
3. **湯気を出さない。** 「湯の音」と言えば、湯気が立つ。**白のままのものである。**
4. **二度揺らさない。** 翻り、はためき、鳴りつづければ、**この1本は別の1本になる。**
5. **カメラを動かさない、店の奥へ入れない。**
6. **音楽を足さない。**
7. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 7-second continuous cinematic take (16:9) of a vermilion cloth answering the wind once, one clip. Beats, deliberately uneven: [0-2s] the vermilion cloth hanging and not sounding, with the indigo tassels down, and the silence held before anything happens; [2-3s] the wind arrives and the cloth sounds once and the vermilion moves once, and the lower edge is drawn slightly inward by air coming from inside the shop; [3-5s] the paving under the lifted hem is empty and stays visible as white — the place where someone would have passed, left empty because nobody came; [5-7s] from deeper in, a kettle sounds and the noise of hot water fills the white a little at a time. The core beat — the single second in which the cloth sounds — is the shortest beat in the shot and carries the most in it, and the cloth moves once and never a second time. 灯 stands at the edge of the frame and does not move and does not turn toward the sound: a person who has come the same way in the same order for twenty years does not turn around for a sound. The kettle is never in the frame — only its sound is — and the steam, the smell and the warmth of the shop's interior have not come back and are not in the frame. The cloth is the faded vermilion of a cloth through a second winter, paler on the hems that faced the sun, its lower hems indigo, and still wet. The story's four colours have two of themselves in this frame. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on the vermilion cloth and the empty white paving beneath it, on the side of what did not come back, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. The front of a shop closed for the morning on a street returned to blank paper: the vermilion noren in the frame with the stone paving below it in the same frame, 灯 seen from behind at the edge of the frame, back and outline, face not drawn. The cloth is the faded vermilion of a cloth through a second winter, paler on the hems that faced the sun and deeper on the hems that stayed in shade, its lower hems indigo, with pigment body and an uneven still-wet surface; the thin pencil lines of the remembering remain faintly readable under the colour because the revision stays visible, the lines being the two hands and the lowered head and nothing else — no goods drawn on the cloth and no illustration on the cloth; the hem is drawn slightly inward as it was left by the one movement. The paving under the hem is plain white paper with nothing on it and no one crossing it. The shop's interior is not in the frame; no kettle, no stove, no fire, no steam and no smoke are in the frame; no cast shadow anywhere, no light shaft, no sunbeam, no lens flare. No second person, no shopkeeper, no cat, no lettering, no shop name, no signage, no numerals, no numbers, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. The cloth sounds once and moves once: the wind pushes it and the tassel lines are re-laid in a new position a single time, and because a revision stays visible the earlier position of those lines remains on the cloth — but there is no second movement, no second swing, no repeat, and the cloth does not keep ringing, flapping or fluttering afterwards. The lower edge is drawn slightly inward once, by air from inside, and that inward pull belongs to the same single movement and is not repeated. The paving under the hem stays empty: no one passes under the cloth, nothing crosses it, and the hem lifting does not reveal anyone. 灯 stands and does not move, does not step, does not shift weight and does not turn toward the sound. Nothing else in the frame moves: no door opens, no shutter moves, no second figure enters, and the light does not shift. No morphing shapes, no motion blur, no stutter, no held frames, no flow or bloom or bleed in the pigment.

## Camera Prompt

Third-person, in front of the shop, at the height of a person standing, with the hanging cloth and the ground below it inside one frame. The camera holds still for the whole seven seconds: no push, no pull, no pan, no tilt, no rack focus, no handheld, no shake, no move closer when the cloth sounds, and no move that would cross toward the shop's interior — the interior is never seen and the camera does not go in. [0-2s] holding on the cloth before it sounds. [2-3s] still holding as it sounds, and the camera does not answer the movement. [3-5s] still holding on the empty paving under the hem. [5-7s] still holding on the cloth to the end, with the kettle heard and never seen. The style allows one drift; this shot spends none — the one drift in this work was spent in the previous shot, and there is only one. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. Sound effects, and only these two: first, one short sound from the cloth as the wind takes it — a single soft slap of cloth, once, with no ring and no repeat, a sound that has not been in this white before; then, from deeper inside the shop and never in the picture, a kettle sounding and the noise of hot water filling the white a little at a time. Nothing else: no passer-by, no footsteps, no door, no shutter, no steam hiss, no bird, no traffic. No ambient bed beyond the air of the street. Music: none, and no swell, no sting, no melody — music here would turn the return of sound into a sound effect, and the return of sound is this shot's whole subject. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no flat vermilion without pigment body, no dry even vermilion paint, no person passing under the noren, no second person, no visible person among the white shapes, no visible kettle as a present object, no visible stove or fire, no steam, no smoke, no door opening, no second movement in the cloth, no cloth following the hand, no stretched or pulled cloth, no figure on the veranda, no lifted or swinging laundry, no outline around the white shapes, no shadow under the white shapes, no marks of departure, no counting marks, no called or written name, no pale gradient on the hand, no soft photographic shadow, no visible face on the figure, no cat in frame, no hand painting the cloth, no brush in frame, no goods drawn on the cloth, no fish drawn on the cloth, no bundle or package on the cloth, no illustration on the cloth, no emblem or sign on the noren, no scales and no drawn eye, no checkered pattern, no plaid, no printed textile pattern, no checkerboard

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. Here the one movement of the cloth is exactly that: the tassel lines are re-laid once in a new position and the earlier position stays visible on the cloth, so the swing is spent, and the second swing has nowhere to come from. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither. The palette stays restrained throughout. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg09-7s-01`
- Segment ID: `01-9`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `7s`
- References: `REF_LOCATION (暖簾の店の前.base, HIGH) ／ REF_GEOGRAPHY (暖簾の店の前.geography, MEDIUM) ／ REF_CHARACTER (灯.identity, HIGH) ／ REF_PROP (暖簾.appearance, HIGH) ／ REF_PROP (薬缶.appearance, LOW — sound only) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: `灯.identity`・`灯.states.支払いの前`・`灯.negatives`・`暖簾の店の前.base`・`暖簾の店の前.geography`・`暖簾の店の前.states.朱が戻った`・`暖簾.appearance`・`暖簾.negative`・`薬缶.appearance`・`薬缶.negative`
  ⚠️ **`薬缶.appearance` は「音である」**——**この1本に物として写さない**（`no visible kettle as a present object`）。
- Temporal Structure: `4 beats, NON_UNIFORM — sparse 2s / dense 1s / held 2s / sparse 2s. The core = BEAT 2 at 2-3s (14% — the shortest and densest beat)`
- Camera Events: `0 events. One continuous take, camera still for the whole clip`
- Action Events: `ACT_LISTEN → ACT_SOUND → ACT_EMPTY → ACT_KETTLE`
- Audio Events: `no dialogue ／ the cloth once at 2-3s ／ the kettle and hot water at 5-7s ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`
- Disclosure point: **なし**（この1本は開示点を持たない——`ledger.disclosure` の4点は S07・S08・S10・S11 である）
  ⚠️ **それでも §18 は S10・S11 と同一である**——`covered` は「変わらない」ことの宣言であり、
  **S10 の開示点の直前の状態が、この1本である。**

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。

## ⚠️ `L14` ——「宣言を超えた区間」（＋15）

⚠️ **この仕様は `L14` に当たる。** 台帳はこの位置に変化点を宣言していない。
**`L14` の言い分は正しい**——**このショットで、§18 の禁止は、戻らない仕方で15節増えた。**
⚠️ **そしてその変化は、このショットの欠陥ではない。理由をここに書く**——`L14` 自身が
「`disclosure` に行を足すか、**足さない理由を記録に書く**」と求めている。

⚠️ **先に、数え方を書く。** S09 の §18 は S08 に対して**18節**を足している——
**`L14` が鳴らすのは15節である。** 差の3節（`no second person`・`no soft photographic shadow`・`no smoke`）は
**先行するショットの集合にも在る**（S02〜S04・S06）——**「新しく現れた」ではないので、持続する増分ではない。**
**検査の数え方と、差分の見え方は一致しない。**

| ＋15 の内訳 | 節 | このショットから要る理由 |
|---|---|---|
| **台帳の薬缶** | `no visible kettle as a present object`／`no visible stove or fire` | `ledger.props.薬缶.negative` そのものである。⚠️ **S09 は、薬缶が音として入る1本である**（`REF_PROP: 薬缶.appearance` は LOW——**音としてのみ。画には出ない**）。**音の出どころを画にすれば、この1本の曖昧さが消える**——S10・S11 も同じ部屋の音を持つ。 |
| **台帳の白い形** | `no visible person among the white shapes` | `ledger.props.白い形.negative` の1節目である。**S09 は、白い形を人の形として見る1本である。** ⚠️ **この節は S04・S05 にも渡っているべきだった**（`REF_PROP: 白い形.appearance` は S04 が初出）——**両ショットは同じ用を `no fully rendered person other than 灯` と `no second person` で負っている**（台帳の2節目 `no cat in frame` は S04・S05 にある）。**台帳の語そのものは、S09 が初出である。** ⚠️ **S04・S05 へ書き戻せば、この位置は S09 から S04 へ移る**——**件数は減らない。** |
| **S10・S11 の禁制が、共有集合として乗る** | 残る12節（`no called or written name`／`no cloth following the hand`／`no counting marks`／`no figure on the veranda`／`no lifted or swinging laundry`／`no marks of departure`／`no outline around the white shapes`／`no pale gradient on the hand`／`no person passing under the noren`／`no second movement in the cloth`／`no shadow under the white shapes`／`no stretched or pulled cloth`） | ⚠️ **S09・S10・S11 は `L10` に `negative: covered` を宣言されており、「覆った」は「同じである」を要求する**（→ 台帳 S10 の行）。**ゆえに3本は同一の集合を持つ。** ⚠️ **この12節は、S10 の主題（白い形が紙へ戻ること）と S11 の主題（手放すこと）のために要る。** **3本が同一である以上、S09 だけが持たない、は書けない。** |

⚠️ **足して数を減らさなかった。** この15節を以後のショットから外せば `L14` は静かになる——
**だが `no visible person among the white shapes` を外すことは、S10 の主題を禁じないことである。**
**数を小さくすることは、欠陥を直すことではない。**

⚠️ **`disclosure` に行を足す道は取らない。** **このショットは開示の変化点ではない**——
台帳の開示点は S07・S08・S10・S11 にある。**S09 は「音が戻る」ショットである**——
⚠️ **これは我々の読みであって、台帳の開示点ではない**（`PLAN.md` §2 の表に、この位置は無い）。
**ゆえに台帳へ行を足せば、開示の設計そのものを書き換えることになる。**

⚠️ **ゆえに残るのは、著者への問いである**——**この作品の動画の Negative は、一つの集合なのか、
ショットごとに書かれるのか。** ⚠️ **問いの全文と実例は `hakuchizu-ch01-seg02.md` の同じ節に書いた**
（この位置が3箇所あるうちの1つである）。⚠️ **著者が決めるまで、この仕様は送らない。**

## Anticipated risks (to check in the first generation)

- **⚠️ くぐる者が現れる。** これがこの1本の最重要の失敗である。揺れる暖簾の下に、
  モデルは必ず人を置く。**この1本は、来なかったことを写している。**
- **⚠️ 薬缶が画に出る。** 「奥で薬缶が鳴る」は、モデルにとって薬缶の画である。
- **⚠️ 湯気が立つ。** 草稿は「まだ白のままだった」と書く。
- **⚠️ 二度揺れる。** 揺れつづけ、鳴りつづければ、**「一度だけ」というこの1本の値が消える。**
- **⚠️ 灯が振り向く。** 二十年おなじ順で来ている者は、音で振り向かない。
- **⚠️ カメラが店の奥へ入る。** `PLAN.md` §0-f。
- **⚠️ 音楽が入る。** 音が戻る場面に音楽を置けば、**戻った音が効果音に負ける。**
