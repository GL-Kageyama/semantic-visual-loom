# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 11/11 / 9s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg11.md`）。

⚠️ **これが最後の1本である。** **この1本が終わったあと、何も起きない。**
草稿 L21「**朱は、白のなかに、ひとりで残った。**」
⚠️ **結末を作らない**（`PLAN.md` §0-g——**落ちを作らない。回収しない。**）。
**最後の1本がすることは、置いていくことである。**

⛔ **この1本に、画にならない開示点がひとつ在る。**
`ledger.disclosure` の **`灯.渡した声: 名を失った`** は、
**この作品のどこにも画として現れない**——**現れないことによって運ばれる。**
⚠️ **これは穴である。** **穴として記録する**（下の §19 と §20 を読むこと）。
**「名を失う」を画にした瞬間、この話は「名前を失う話」という別の話になる。**

⛔ **§18 の `Negative Prompt` が S09・S10 と同一である理由。**
`ledger.disclosure` はこの開示点を **`negative: covered`** と宣言している——
**ゆえに `L10` は「直前の動画仕様（S10）と、否定節の集合が一致すること」を要求する。**
⚠️ **そして、この1本では `covered` が特に正しい。**
**画に現れない開示は、否定節を変えない**——**変えるものがあるなら、それは画である。**

---

# 1. VIDEO

- Duration: `9s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the hand takes the weight of the wet vermilion once and lets go, and the cloth does not follow it.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01）。
- 白は音を持たない。音が戻るのは、色が戻ったところからである（S09）。
- 白の下には、人がいた気配が透けている（S03）。
- 思い出したぶんだけ、白のなかから色が立ち上がる（S08）。
- いちばん白に近いものが、いちばん先に戻る（S10）。
- **覚えることは、払うことである**（`bible.world.rules`）。
  ⚠️ **この1本で、支払いが画になる。** **触れることが支払いである。**
- **「置いた色は、もう白に戻らない。」**
  ⚠️ **この1本の結末はこれである。** **朱は置かれたまま残る。**
  **灯は白へ戻っていく**——**置いた色だけが、残る。**

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
- Color Language: **朱と藍。** ⚠️ **この1本の朱は、まだ濡れている。**
  **S08 が濡れを残したのは、この1本のためである**——
  **乾いていれば、指先に重さは残らない。**
- Texture: ⚠️ **指先の朱は、絵の具である。** **汚れではない。**
  **量は少ない**——**触れたぶんだけである。**
- Rendering: ⚠️ **灯が白へ戻ることは、紙が手を引き取ることである。**
  **指先から先に、紙の白に戻る**——**グラデーションではない、縁からである。**
- Visual Density: ⚠️ **この1本で、いちばん濃いのは `0-2s` の触れる2秒である。**
  **核（`2-5s`）は、その手が離れる3秒である。**
- Time: `朝`
- Atmosphere: 朱い暖簾と、その前を去る者。**置かれた朱だけが、残る。**

# 3. SUBJECTS

## 朱い布

- Reference: `暖簾.appearance`・`暖簾.negative`・`暖簾の店の前.states.朱が戻った`（`attached` に従う）
- Appearance: 染めて二度目の冬を越した褪せた朱。**房は藍。** ⚠️ **まだ乾いている途中である。**
- Behavior: ⚠️ **手が離れても、布は手を追わない。**
  **引かれない、伸びない、揺れない。** **置かれたままである。**
  ⚠️ **この1本で布は鳴らない**（S09 で一度鳴いた）。
  **触れられることは、鳴ることではない。**
- Continuity Requirements: ⚠️ **触れた跡を布に残さない。** **指の形を描かない**——
  **描けば、それは署名である。**

## 灯

- Reference: `灯.identity`・`灯.states.支払いの後`（`attached` に従う）
  ⚠️ **支払いは S10 のあいだに済んでいる**（`ledger.disclosure`）。
  **この1本は、済んだあとの手である。**
- Appearance: 後ろ姿、輪郭。⚠️ **顔は描かない。**
  ⚠️ **指先に、朱がわずかに付いている。**
- Behavior: ⚠️ 触れる → 離す → しばらく居る → 去る。
  **四つである。** **そのどれも、決心に見せない**——
  **二十年おなじ順で来た者の、四つ目の動作である。**
  ⚠️ **この1本で、灯は名前を呼ばれないし、名乗らないし、振り向かない。**
- Continuity Requirements: ⚠️ **去ったあと、灯の影が白の上に薄く残る。**
  **そして、その影はまだ色を持っている**——
  ⚠️ **指先だけが、少し白い。** **影のほうが、あとまで色を持つ。**

## 白い形・薬缶

- ⚠️ **この1本には無い。** **音も無い。**

# 4. ENVIRONMENT

- Location: `暖簾の店の前`（`.base`・`.geography`・`.states.朱が戻った`）
- Environment Elements: 店の前の石畳、**朱い暖簾**、閉じた店、
  ⛔ **そして通りの家並み**——**閉じた白い雨戸の列、二階のベランダ、屋根**。
  ⛔ **2026-09-22 の著者の指摘**——「**街の風景が消えてしまっていた**」。
  ⚠️ **街は、この1本の否定文にだけ居た**（§16 `No figure on the veranda`・
  `No outline around the white shapes`）——**肯定文が名指さない名詞は描かれない。**
  ⛔ **書き落としであって、判断ではない**——台帳 `暖簾の店の前.geography` は
  「通りの側に面した店。**隣家の二階のベランダが、同じ画のうちに入る**」と定め、
  `通り.base` は「石畳、**閉じた雨戸**、二階のベランダ」を持つ。
  ⚠️ **S10 の §18 は既に名指している**（`with the second-floor drying place of the
  neighbouring house behind it, all inside one frame`）——**落ちていたのは S11 だけである。**
  ⚠️ **街は `白い形` ではない**（§5）——**`白い形` は自転車と洗濯物の形である。**
  ⚠️ **店の内側は画に入らない**（`PLAN.md` §0-f）。
- Environmental Behavior: ⚠️ **風は無い。** **布は鳴らない。**
  **人がひとり、歩いて出ていくだけである。**

# 5. OBJECTS

- `暖簾` — この1本の主題である。**触れられ、置いていかれる。**
- `灯の影` — ⚠️ **この1本だけの物体である。** **白の上に薄く落ち、色を持つ。**
- `白い形`・`薬缶` — **この1本には無い。**
  ⚠️ **`白い形` は自転車の形と洗濯物の形である**（台帳 `props.白い形`）——
  **ゆえに、不在は正しい。** ⛔ **街（家並み・雨戸・屋根）は、これとは別である**——
  **街は環境であって、物体ではない**（§4 の 2026-09-22 の註）。

# 6. REFERENCES

- REF_LOCATION: `暖簾の店の前.base` (HIGH)
- REF_GEOGRAPHY: `暖簾の店の前.geography` (MEDIUM)
- REF_CHARACTER: `灯.identity` (HIGH)
- REF_PROP: `暖簾.appearance` (HIGH — この1本の主題である)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — 画にならない開示点と `covered` 宣言)

# 7. NARRATIVE

- Core Event: **触れて、離す。** **布は追わない。**
- Beginning: 灯が朱に触れる。**濡れた絵の具の重さが、指先に残る。**
- Turn: **手が離れる。布は手を追わない。**
- Peak: ⚠️ **無い。** **山は S08 である。**
- Pull: しばらく居て、**歩き出す。**
  **朱は、白のなかに、ひとりで残る。** **灯の影は、まだ色を持っている。**
  ⚠️ **落ちを作らない。回収しない。** **ここで終わる。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `dense` — **触れる。** 濡れた絵の具の重さが、指先に残る。
  - BEAT 2 `2-5s` — density: `held` — **手が離れる。布は追わない。** ⚠️ **3秒。この1本の核。**
  - BEAT 3 `5-7s` — density: `held` — **暖簾の前に、しばらく居る。** ⚠️ **最後の静止である。**
  - BEAT 4 `7-9s` — density: `sparse` — **歩き出す。** 朱は白のなかに残る。
- Temporal Density: ⚠️ **核（`2-5s`・33%）は、「何も起きない3秒」である。**
  **濃いのは `0-2s` の触れる2秒**——**この作品は、濃い拍と核の拍が別である。**
  ⚠️ **触れる（濃い）→ 離す（核・無）→ 居る（静止）→ 去る（薄い）。**
  **この並びは、この作品の全体の縮みである**——**S08 が「溜め→核→余韻」だったのに対し、
  ここは「起きる→起きない→居る→去る」である。**

# 9. ACTION

- `ACT_TOUCH` — Before: 朱は置かれたままである。After: **指先に、朱の重さが残っている。**
  ⚠️ **強く触れない。** **押さない、撫でない、掴まない。**
  **触れる、で終わる。** ⚠️ **布はこの2秒、動かない。**
- `ACT_RELEASE` — Before: 指が朱に触れている。After: **手が離れている。** **布は追っていない。**
  ⚠️ **この3秒で、動くのは手だけである。**
  **布が追えば、この話は「別れの話」になる。**
- `ACT_STAY` — Before: 灯が暖簾の前に居る。After: 変わらない。**2秒である。**
  ⚠️ **これは決心ではない。** **二十年おなじ順で来た者が、そこで止まるだけである。**
  **振り向かない、見上げない、息をつかない。**
- `ACT_LEAVE` — Before: 灯が画のなかに居る。After: **灯が画の外に居る。**
  ⚠️ **カメラは追わない。** **歩幅を変えない、速くしない。**
  **灯の影が、白の上に薄く残っている。** **そして、まだ色を持っている。**
  ⚠️ **指先だけが、少し白い**——**縁から、紙が引き取った。**

# 10. CAMERA

- Camera Language: 三人称、店の前、**朱い布と、その前の石畳が同じ画に入る。**
  ⛔ **そして、通りの家並みも同じ画に入る**——**閉じた雨戸の列、二階のベランダ、屋根**
  （2026-09-22 の指摘。§4）。**カメラは動かないが、画は街を含む。**
  ⚠️ **カメラは店の奥へ入らない**（`PLAN.md` §0-f）。
- Camera Events: **無い。**
- Camera Behavior: **9秒のあいだ、一度も動かない。**
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。** **使ったのは S08 である。**
  ⚠️ **そして、灯が画の外へ出ても、カメラは追わない。**
  **追えば、この1本は「去る人を送る画」になる**——
  **残るのは朱であり、送る者は居ない。**
  ⚠️ **作品の最後の画は、動かない。**

# 11. MOTION

## Subject Motion

⚠️ **動くのは、灯と、灯の手だけである。**
**朱は動かない。** 触れられ、離され、置かれたままである。
**布が手を追わないこと**——⚠️ **これがこの1本の値である。**
**手が離れたあと、布は引かれない、伸びない、揺れない、しならない。**
**灯は歩いて画の外へ出る。** **影は白の上に残る。**
**指先が、縁から紙の白に戻る**——⚠️ **グラデーションではない。**

## Object Motion

**無い。** ⚠️ **布は動かない。** **石畳は動かない。** **戸は開かない。**
⚠️ **灯の影だけが、残る**——**影は動かない。** **去ったあと、そこに在る。**

## Environmental Motion

**無い。** ⚠️ **風は無い。** **埃も立たない。**
**人がひとり歩くだけで、通りは動かない。**

## Physical Characteristics

- Weight: ⚠️ **朱は重い。** **濡れた絵の具の重さである**——
  **この重さが、触れた指先に移る。** **ゆえに指先の朱は、汚れではなく、量である。**
- Inertia: ⚠️ **布は慣性を持たない。** **離されても、揺れ戻らない。**
  **揺れ戻れば、それは別の1本である。**
- Acceleration: 無い。**手は一定の速さで離れる。**
- Fluidity: **無い。** ⚠️ **歩き去ることも、滑らかに流さない**——**角を持つ。**
- Impact: ⚠️ **触れることは、衝撃ではない。** **接触である。**

# 12. EMOTION

- Emotional Arc: 触れる → **離す** → 居る → 去る。
- Emotional Events: ⚠️ **感情を、顔で出さない。** **顔は描かない。**
  **出すのは、動作の四つである。**
  ⚠️ **「去る」を感傷にしない。** **歩幅を変えない。**
  **この1本の終わりは、悲しみではない**——**順番どおりである。**
- ⚠️ **強度は、最も低いほうである。** **上げるのは S08 の仕事だった。**

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。**
- Lighting Events: **無い。** ⚠️ **去る者に光を当てない。**

# 14. AUDIO

- Dialogue: **無し。** 台詞も、ナレーションも無い（`PLAN.md` §0-e）。
  ⚠️ **この作品は、最後まで誰も喋らない。**
- Sound Effects: **無し。** **足音も置かない。**
  ⚠️ **足音を置けば、去ることに音が付く**——**この1本の終わりは、音を持たない。**
  ⚠️ **布も鳴らない。** **薬缶も、もう鳴らない**（S09 で一度鳴いた）。
- Music: 無し。⛔ **ここに音楽を置けば、この作品は「終わりのある話」になる。**
- Environment: ⚠️ **静かである。** **S09 で戻った音は、S10 で引き、ここで消えている。**
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註——
  **発話のある動画に中国語の字幕が焼かれた実測**）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: **灯——後ろ姿、輪郭、顔は描かない。** **この1本で歩いて出る。**
- Spatial: 店の前である。**この1本は店の前を出ない。店の内側へ入らない。**
  ⛔ **「出ない」は、カメラの話である**——**画は街を含む**（2026-09-22 の指摘。§4・§10）。
  ⚠️ **この一行を「街は画に入らない」と読んではならない**——**街は、この場所の画のうちに在る**
  （台帳 `暖簾の店の前.geography`）。
- Temporal: 朝。S10 の直後である。**朱は戻り、まだ乾ききっていない。**
- Visual: 朱と藍と、白。⚠️ **指先の朱は、この1本だけのものである。**
- Motion: **手が離れる。布は追わない。人が出ていく。** **カメラは動かない。**
- Sound: **無い。** ⚠️ **この作品は、音が消えたところで終わる。**

# 16. CONSTRAINTS

⚠️ **この節は、S09・S10 と同一の `Negative Prompt` を作る**（`L10`——`covered` 宣言）。
**内訳を分けて書く。**

## MUST NOT

**この1本（S11）の危険:**
- **No called or written name** —— ⚠️ **この1本の最重要の失敗である。**
  **この話のフックである**（`ledger.disclosure` の `灯.渡した声: 名を失った`）。
  **名が呼ばれ、書かれ、字幕で出た瞬間、この話は別の話になる。**
- **No cloth following the hand. No stretched or pulled cloth** ——
  ⚠️ **手が離れるとき、朱は引かれない。** **追えば、それは別れの画である。**
- **No hand painting the cloth. No brush in frame** ——
  ⚠️ **この1本の色は、誰も塗らない。** **触れることは、描くことではない。**
- **No pale gradient on the hand** —— ⚠️ **白への戻りは、縁からである。**
  **グラデーションにすれば、灯は薄れていく人になる。**
- **No soft photographic shadow** —— **灯の影は、平らな濃みである。**
- **No marks of departure** —— ⚠️ **去った印を、白の上に残さない。**
  **足跡も、触れた跡も、署名も無い。**
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
- No shop interior. No shopkeeper. No lettering. No legible text on the noren. No shop name on the noren.

**S09 から来る危険**（同じ集合に居るため。**消せば `L10` が鳴る**）:
- **No person passing under the noren. No second person**
  —— ⚠️ **この1本のくぐる者は、灯である。そして灯は、くぐらない。**
  **通り過ぎもしない**——**去るのは通りである。**
- **No visible kettle as a present object. No visible stove or fire. No steam. No smoke. No door opening.**
- No second movement in the cloth.

**S10 から来る危険**（同じ集合に居るため。**消せば `L10` が鳴る**）:
- No visible person among the white shapes. No figure on the veranda.
- No lifted or swinging laundry. No outline around the white shapes.
- **No shadow under the white shapes** —— ⚠️ **灯の影は、白い形の下の影ではない。**
- No counting marks.

## MUST

- Full animation, not limited.
- **触れて、離す、の二つが別の動作であること。**
- **布が手を追わないこと。** **引かれない、伸びない、揺れない。**
- **「居る」2秒を、決心に見せないこと。** **振り向かない、見上げない、息をつかない。**
- **カメラが灯を追わないこと。** **最後の画は、動かない。**
- **去る速さを変えないこと。** **速めない、遅らせない。**
- **指先が、縁から白に戻ること。** **淡くなるのではない。**
- **影が、指先より長く色を持つこと。**
- **音を一切置かないこと。** **足音も無い。**

## PREFER

- 触れる2秒のあいだ、**布がまったく動かない**こと。
- 灯の歩幅が、**来たときと同じ**であること。

## ALLOW

- 灯が画の外へ出たあと、**石畳の上が、しばらく空いている**こと。
  ⚠️ **そこに何も置かない**——**敷居も、影の形も、印も。**

# 17. GENERATION PRIORITIES

1. **名前を出さない。** ⚠️ **この1本の最重要の失敗である。**
   「二十年来た者が去る」と言えば、モデルは**看板**か**字幕**か**呼び声**を置く。
   **この話は、名を失った話である**——**名を出すことが、そのまま矛盾である。**
2. **布を追わせない。** 「手が離れる」と言えば、布が揺れ戻る。
   **布が追えば、この1本は別れの画になる。**
3. **指先の朱を、汚れにしない。** **量である。**
4. **白への戻りを、グラデーションにしない。** **縁からである。**
5. **灯の顔を描かない。** **感情を顔で出さない。**
6. **カメラを動かさない、灯を追わない。**
7. **音を置かない。音楽を置かない。**
8. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 9-second continuous cinematic take (16:9) of a hand touching a wet vermilion cloth once and letting go, one clip. Beats, deliberately uneven: [0-2s] 灯 reaches out and touches the vermilion cloth, and the weight of the wet pigment stays on the fingertip, a small amount of vermilion on the skin, and the cloth does not move at all while it is touched; [2-5s] the hand releases and the cloth does not follow it — it is not pulled, not stretched and does not swing back, it is left laid there; [5-7s] 灯 stands before the noren a while, and this standing is not a decision, it is where the body of someone who has come the same way in the same order for twenty years happens to stop, with no turning around and no looking up; [7-9s] 灯 walks off and out of the frame at the same pace as always, and the camera does not follow, and the vermilion is left alone in the white. The core beat — the three seconds in which the hand releases and nothing else happens — is the shot's largest share, and the densest beat is the two seconds of the touch, so the dense beat and the core beat are not the same beat here. As 灯 leaves, the fingertips go slightly white from the edge, as paper taking the hand back, not a fade and not a gradient, and the shadow on the white ground still holds colour and holds it longer than the fingertips do. Nothing is called out, nothing is written and no name appears anywhere in the frame. The cloth is the faded vermilion of a cloth through a second winter, paler on the hems that faced the sun, its lower hems indigo, and still wet. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on the vermilion cloth alone in the white with the ground empty beneath it, and the clip ends there, without a resolving beat and without a farewell.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. The front of a shop closed for the morning on a street returned to blank paper, the long row of closed white shutters running along the street with the second-floor verandas and the roofs above, all of it in one frame: the vermilion noren in the frame with the stone paving below it in the same frame, and 灯 seen from behind, back and outline, face not drawn, with a small amount of vermilion on one fingertip that is quantity and not dirt. The shutters are white paper where shutters were: flat, unnumbered, unlettered, without house numbers, without door numbers, without plates, with only the grain of the boards left as faint lines. The cloth is the faded vermilion of a cloth through a second winter, paler on the hems that faced the sun and deeper on the hems that stayed in shade, its lower hems indigo, with pigment body and an uneven still-wet surface, and no mark of a hand on it and no shape of fingers on it. The shadow on the ground is flat gouache, not photographic, and the white ground stays pure white around it. No shop interior, no kettle, no stove, no fire, no steam, no smoke, no sunbeam, no light shaft, no lens flare. No second person, no passer-by, no shopkeeper, no cat, no lettering, no shop name, no signage, no numerals, no numbers, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. The hand touches once and releases once: the touch is a contact and not a grip, not a press, not a stroke, and the cloth does not move while it is touched. When the hand releases, the cloth does not follow it — no stretch, no pull, no swing back, no shiver, no settling, and no second movement afterwards. 灯 then stands without shifting weight and without turning around and without looking up, and then walks off at an even pace and out of the frame, and the walking does not slow and does not hurry. As 灯 goes the fingertips go slightly white from the edge inward, as paper taking them back, while the shadow on the ground keeps its colour longer. The cloth does not sound. No morphing shapes, no motion blur, no stutter, no held frames, no flow or bloom or bleed in the pigment, no slow motion, no trailing afterimage on the walking figure.

## Camera Prompt

Third-person, in front of the shop, at the height of a person standing, with the hanging cloth and the ground below it inside one frame. The camera holds still for the whole nine seconds: no push, no pull, no pan, no tilt, no rack focus, no handheld, no shake, no move closer at the touch, and no move that would cross toward the shop's interior. [0-2s] holding as the hand touches. [2-5s] still holding as the hand releases and the cloth stays. [5-7s] still holding as 灯 stands. [7-9s] still holding on the cloth as 灯 walks out of the frame, and the camera does not follow and does not reframe and does not tilt to keep the figure — the last frame of this work is still. The style allows one drift; this shot spends none — the one drift in this work was spent in the eighth shot, and there is only one. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. No sound effects at all: no footsteps as 灯 walks, no sound from the cloth when it is touched and none when the hand leaves, and nothing ambient beyond the air of the street. Music: none, and no swell, no sting and no final chord — music here would give this ending a shape, and this shot has no ending, it has a departure. The sound that returned in the ninth shot has receded through the tenth and is gone here. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no flat vermilion without pigment body, no dry even vermilion paint, no person passing under the noren, no second person, no visible person among the white shapes, no visible kettle as a present object, no visible stove or fire, no steam, no smoke, no door opening, no second movement in the cloth, no cloth following the hand, no stretched or pulled cloth, no figure on the veranda, no lifted or swinging laundry, no outline around the white shapes, no shadow under the white shapes, no marks of departure, no counting marks, no called or written name, no pale gradient on the hand, no soft photographic shadow, no visible face on the figure, no cat in frame, no hand painting the cloth, no brush in frame, no goods drawn on the cloth, no fish drawn on the cloth, no bundle or package on the cloth, no illustration on the cloth, no emblem or sign on the noren, no scales and no drawn eye, no checkered pattern, no plaid, no printed textile pattern, no checkerboard

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. Here the hand does not revise anything: it touches a laid surface and takes nothing and leaves nothing, and because gouache is opaque the touch does not blend into the cloth, it only sits on the finger — the pigment is carried away as quantity, and the cloth stays exactly as it was laid. The leaving figure is the reverse case: a laid figure is taken back, and the paper comes back from the edge first, so the whitening is a correction and not a fade. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither, and the page it holds is the last page. The palette stays restrained throughout. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg11-9s-01`
- Segment ID: `01-11`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `9s`
- References: `REF_LOCATION (暖簾の店の前.base, HIGH) ／ REF_GEOGRAPHY (暖簾の店の前.geography, MEDIUM) ／ REF_CHARACTER (灯.identity, HIGH) ／ REF_PROP (暖簾.appearance, HIGH) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: `灯.identity`・`灯.states.支払いの後`・`灯.negatives`・`暖簾の店の前.base`・`暖簾の店の前.geography`・`暖簾の店の前.states.朱が戻った`・`暖簾.appearance`・`暖簾.negative`
- Temporal Structure: `4 beats, NON_UNIFORM — dense 2s / held 3s / held 2s / sparse 2s. The core = BEAT 2 at 2-5s (33% — the three seconds in which nothing happens)`
- Camera Events: `0 events. One continuous take, camera still for the whole clip`
- Action Events: `ACT_TOUCH → ACT_RELEASE → ACT_STAY → ACT_LEAVE`
- Audio Events: `no dialogue ／ no sound effects at all ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`
- Disclosure point: **`灯.渡した声: 名を失った`**（`negative: covered`）
  ⛔ **この開示点は、画を持たない。** **この作品のどこにも、画として現れない。**
  **運ばれるのは、この作品が名を一度も出さないことによってである**——
  **ゆえに `covered` が正しい**：**現れない開示は、否定節を変えない。**
  ⚠️ **これは穴である。** **穴として記録する**（§20 を読むこと）。
  ⚠️ **この作品の語りが「名を失った」と言うことは、どこにも無い。**
  **`草稿` L21 以降にも、その語は無い。**

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。

### ⛔ 2026-09-22 の訂正——**街の風景が、この1本の仕様から消えていた**

⚠️ **著者の指摘**——「**街の風景が消えてしまっていた**」。

⛔ **実測**（この1本の全文を日英で走査した）——**街（家並み・雨戸・屋根・ベランダ）を
名指す肯定の行は、0 であった。** 街が居たのは**否定文だけ**である——
§16 `No figure on the veranda`・`No outline around the white shapes`、
§18 `Negative Prompt` の `no figure on the veranda, no lifted or swinging laundry,
no outline around the white shapes, no shadow under the white shapes`。
⚠️ **肯定文が名指さない名詞は描かれない。否定文は、無い名詞を呼び戻せない**——
**ゆえにこの1本は、ベランダを禁じながら、ベランダを一度も置いていなかった。**

⛔ **書き落としであって、判断ではない。** 台帳 `暖簾の店の前.geography` は
「通りの側に面した店。**隣家の二階のベランダが、同じ画のうちに入る**」と定め、
著者が作った S11 の絵（`specs/image/11_…16_19_03.png`）にも街は写っている。
⚠️ **S10 の §18 は既に名指していた**——**落ちていたのは、この1本だけである。**

**直した4箇所**（＋記録1）——
1. §4 `Environment Elements` … 通りの家並み（閉じた白い雨戸の列・二階のベランダ・屋根）を足した。
2. §5 `OBJECTS` … `白い形` の不在は**正しい**と書き分けた（`白い形` は自転車と洗濯物の形であり、街ではない）。
3. §10 `Camera Language` … 画が街を含むことを書いた。
4. §18 `Visual Prompt` … **生成へ渡る文字列**に、S05 の英語で家並みを戻した
   （`the long row of closed white shutters running along the street with the
   second-floor verandas and the roofs above, all of it in one frame` ＋
   `The shutters are white paper where shutters were: … with only the grain of the
   boards left as faint lines.`）。
   ⚠️ **その一文は、S05 で実証済みである**——**S05 の絵**（`specs/image/05_…16_10_13.png`）**は、
   同じ一文から、白い雨戸の長い列を描き、数字も札も字も置かなかった。**
   ⛔ **ゆえに「house numbers」「plates」という語を肯定文が持つことは、この作品では
   数字を呼ばない**——**心配は、測って消した。**
5. ⚠️ §15 `Spatial` … 「店の前を出ない」が**カメラの話**であると書き足した（記録のみ。文字列は動かしていない）。

⛔ **`Negative Prompt` は1節も動かしていない**（76節のまま。`negative: covered` は不変）。
⚠️ **ゆえに開示の記録も動かない**——検査は `違反 4 件 / 註 24 件` のままである。

⚠️ **残る危険**——**`no outline around the white shapes` の「the white shapes」が、
いま同じ文字列のなかで白い家並みの近くに座っている。** 台帳の `白い形` は
自転車と洗濯物を指すので**文法的には正しい**が、**モデルが広く読めば、家並みの線を消しうる。**
⚠️ **観測してから決める**（否定文を動かせば、開示の記録が動く）。

## Anticipated risks (to check in the first generation)

- **⚠️ 名前が出る。** 看板、字幕、呼び声、どれでも。**この1本の最重要の失敗である。**
- **⚠️ 布が手を追う。** 揺れ戻り、しなり、伸びる。**別れの画になる。**
- **⚠️ 灯が振り向く、見上げる、ため息をつく。** **決心に見える。**
- **⚠️ カメラが灯を追う。** 作品の最後の画が動く。**残るものが朱でなくなる。**
- **⚠️ 白への戻りがグラデーションになる。** **灯が薄れていく人になる。**
- **⚠️ 指先の朱が、汚れになる。** **量ではなく、汚れである。**
- **⚠️ 街が、色を持つ。** 家並み・屋根・雨戸が、四色のどれかで塗られる。**街は白である**——
  `The shutters are white paper where shutters were` が、肯定文の側の歯止めである（2026-09-22）。
- **⚠️ 街に、人が居る。** 窓、ベランダ、戸口。**否定文が3節で塞いでいる**——
  ⚠️ **2026-09-22 の訂正で、この3節が初めて、実在のものを塞ぐようになった。**
- **⚠️ 足音が入る。** **去ることに音が付く。**
- **⚠️ 音楽が入る。** **この作品に終わりができる。**
- **⛔ 画にならない開示点。** `灯.渡した声: 名を失った` は、
  **この作品のどの画にも現れない**（§19）。
  ⚠️ **これは我々が承知のうえで置いた穴である。**
  **もし著者が画を要ると思うなら、画はこの1本ではなく、
  台帳の `disclosure` に新しい1行として足されるべきである**——
  **この1本に足せば、この1本の主題（去ること）が二つになる。**
