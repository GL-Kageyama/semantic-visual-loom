# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 7/11 / 9s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg07.md`）。

⚠️ **この1本の変化は「薄い鉛筆の格子が浮かぶこと」である。色はまだ来ない。**
⚠️ **切らない。** `モンタージュ` と名乗るが、**カットを1つも使わない**——
覚えているものは、**すべて同じ一枚の布の上に、順に置かれる。**
理由は `shots/hakuchizu-ch01-seg07.yaml` の冒頭に記録してある（**1ショットは1変化である**、
**山の文法が浮く**、そして——`gouache-abstract` の「**The camera is one page of a sketchbook.**」
**切ることは、頁を破ることである**）。
⚠️ **線と色を2本に分けたのは、様式が既に持っている工程を2本に分けたことである。**
`hakuchizu-imageboard/01-1` の共通様式は「**薄い鉛筆グリッドの線画を構造として残し、
その上に四色が薄塗りのウォッシュで戻る**」と書く——**下層はグリッドであり、図ではない。**
**S07 はその下層であり、S08 は上層である。** ⚠️ **草稿は色の話しか書かない**（下の註）。
⛔ **2026-09-22 の著者の裁定（第二）**——「**暖簾の上に、具体的なモチーフは重ならない**」。
**ゆえに布に載るのは格子であって、形ではない。手も、頭も、品も、描かない。**
⚠️ **旧版はここに「両手と下げた頭」を置いていた。** それは、こちらが
`visible thin pencil line art` を「図」と読んだ誤りである（`PLAN.md` §4-e）。
**様式の下層は、地図の経緯線である。**
⚠️ **この1本は、この話で最初の開示点である**（`ledger.disclosure` の4点のうちの1点目）——
**ゆえに §18 の `Negative Prompt` は S06 と同一である**（§16 の註を見よ）。
⚠️ **`hakuchizu-imageboard/01-1` の「線画だけの領域を作らない」との関係**は
`PLAN.md` §1 の註に残す——**採った読みは「その註はイメージボードのパネルの話である」。**

---

# 1. VIDEO

- Duration: `9s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: a faint pencil grid surfaces on a white cloth, one line at a time, in a fixed order, and the cloth stays white.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01）。
- 白は音を持たない（S09）。
  ⚠️ **この1本は、思い出の側である**——**ゆえにこの1本の記憶には、音が1つも無い。**
  草稿 L13 は「**薬缶の音の下で**、すこし頭を下げて受け取る」と書くが、
  **その音は S09 で戻る**（`bible.world.rules`——**音が戻るのは、色が戻ったところからである**）。
  ⚠️ **ゆえにこの1本は、音の無い記憶である。**
- 白の下には、人がいた気配が透けている（S03）。
- 思い出したぶんだけ、白のなかから色が立ち上がる（S08）。
  ⚠️ **この1本は、色が立ち上がる直前である**——**格子だけが浮かび、色はまだ1つも無い。**
- 覚えることは、払うことである（S10・S11）。
- 数は町を戻さない（S05・S10）。
- 置いた色は、もう白に戻らない（S11）。
  ⚠️ **この1本は、その「格子」版である**——**置かれた格子は、置かれたまま残る**（`motion.law`）。
  ⛔ **下の行は、2026-09-22 の時点で未決である。**
  ⚠️ **旧い行**——「**S08 の色は、この格子の上に載る。**」
  ⛔ **2026-09-22 の著者の指示で、S08 の文字列から格子が外れた**
  （`specs/video/hakuchizu-ch01-seg08.md` §20）。
  ⚠️ **ゆえに、この1本の格子が S08 へ渡るかは、著者の裁定を仰いでいる**——
  **この1本は、いまも格子を変化として持っている**（**こちらからは書き換えていない**）。
  **申し送りは `specs/video/hakuchizu-ch01-seg08.md` §20 の1点目である。**

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
- Color Language: **一色も無い。** ⚠️ **この1本は、`art_direction` の
  「visible thin pencil line art」のうち、**地の構造の層**である——
  **様式の下層を、9秒間だけ見せる。**
- Texture: 荒い紙。**格子の線は鉛筆であり、絵の具ではない**——にじまない、太らない、盛り上がらない。
- Rendering: ⚠️ **格子を消さない。** この様式の法「**the revision stays visible**」——
  **置かれた線は、置かれたまま残る。**
- Visual Density: **中。** ⚠️ **線は、まとめて現れない。一本ずつである。**
- Time: `朝`
- Atmosphere: 白い暖簾の上に、地図の骨が、順に浮かんでくる。

# 3. SUBJECTS

## 浮かんでいく格子

- Reference: `暖簾.appearance`・`暖簾.negative`（`attached` に従う）
- Appearance: **薄い鉛筆の格子。** ⚠️ **地図の経緯線である**——
  **布を桝目に割る、等間隔の細い線。** ⛔ **図は1つも描かれない**
  （2026-09-22 の著者の裁定——§9 `ACT_GRID_FIRST` の註）。
  ⚠️ **色を持たない。** 布の上に**在る**のであって、**布に染みているのではない。**
  ⚠️ **桝目の中は、空である。** 白いままである。
- Behavior: **一本ずつ浮かぶ。** 順は決まっている——**布を縦に走る線 → 布を横に走る線。**
  ⚠️ **この順は入れ替わらない**（草稿 L21「**おなじ順で、おなじぶんだけ**」）。
- Continuity Requirements: ⚠️ **この1本には、人も顔も無い**——**布に載るのは格子だけである。**
  ⚠️ **それでも `forbidden_set` の3件（店主・顔・人）は、この1本でも有効である**——
  **節を消せば、台帳と食い違う。**

## 灯

- Reference: `灯.identity`（`attached` に従う）
- Appearance: 後ろ姿、輪郭。⚠️ **顔は描かない。**
- Behavior: ⚠️ **この1本に灯の所作は無い。** **立っているだけである**——
  **この9秒は、灯の内側で起きている。**

# 4. ENVIRONMENT

- Location: `暖簾の店の前`（`.base`・`.geography`・`.states.白`）
- Environment Elements: 店の前の石畳、**白い暖簾**、閉じた店。
  ⚠️ **店の内側は画に入らない**（`PLAN.md` §0-f）。
- Environmental Behavior: **無い。** ⚠️ **風を起こさない**——**布は、まだ動かない。**

# 5. OBJECTS

- `暖簾` — この1本の面であり、**覚えている側**である。
  ⚠️ **布は、この町で唯一、まだ何かを覚えている面である。**
  ⚠️ **この9秒で、布は「白い紙」から「地図の地」になる**——**まだ1色も無い地図である。**
- 暖簾の店の前 — この1本の場所である。
- `白い形`・`水の跡`・`薬缶` — **この1本には無い。**

# 6. REFERENCES

- REF_LOCATION: `暖簾の店の前.base` (HIGH)
- REF_GEOGRAPHY: `暖簾の店の前.geography` (MEDIUM)
- REF_CHARACTER: `灯.identity` (HIGH)
- REF_PROP: `暖簾.appearance` (HIGH — この1本の面である)
- REF_STYLE: `gouache-abstract` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — `covered` 宣言がこの1本の §18 を決める)

# 7. NARRATIVE

- Core Event: 白い布の上に、薄い鉛筆の格子が浮かぶ。**布が、地図の地になる。**
- Beginning: 白い無地の布。**まだ何も思い出されていない。まだ地図ではない。**
- Turn: **最初の線が浮かぶ**——布を縦に走る1本。
- Peak: **縦の線が揃う。** ⚠️ **桝目の中は空である**——図は描かれない。
- Pull: 格子が止まる。**色は来ない。布は白いままである。**
  ⚠️ **この2秒が、山への溜めである。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — 白い布。**最初の線——布を縦に走る1本。**
  - BEAT 2 `2-5s` — density: `held` — **縦の線が、1本ずつ増える。** 同じ間隔で、同じ順で。
    この3秒が核である。
  - BEAT 3 `5-7s` — density: `sparse` — **横の線が1本ずつ入り、桝目が閉じていく。**
  - BEAT 4 `7-9s` — density: `held` — **格子が止まる。色は来ない。** 山への溜めである。
- Temporal Density: ⚠️ **核の3秒（33%）は、縦の線が揃う3秒である。**
  **`sparse` の3秒ずつは、核を挟む前後の余白である。**
  ⚠️ **最後の2秒が `held` であることが、この1本を山の溜めにしている**——
  **格子が止まったあとの2秒に、色が来ない。**

# 9. ACTION

- `ACT_GRID_FIRST` — Before: 布の上に何も無い。After: **布を縦に走る、1本の薄い鉛筆の線が浮かんでいる。**
  Causes: 覚えていること。⚠️ **この線は、S08 で色が入る桝目の辺になる。**
  ⛔ **布に載るのは格子だけである。手も、頭も、品も、描かない。**
  ⚠️ **2026-09-22 の著者の裁定（第二）である**——「**暖簾の上に、具体的なモチーフは重ならない**」。
  ⚠️ **この裁定に至った道。** 旧版はここに**両手と下げた頭**を置いていた——
  それは、こちらが `hakuchizu-imageboard/01-1` の
  「**薄い鉛筆グリッドの線画を構造として残し**」を**「図」と読み違えた**ものである。
  **様式の下層は、地図の経緯線である**（`PLAN.md` §4-e）。
  ⚠️ **そして、布に載るものが「名を持った形」であるかぎり、生成器はそれを描く**——
  **品の名を書けば魚が描かれ、手を書けば手が描かれる。**
  **ゆえに、この1本が名指すのは「格子」だけである。**
- `ACT_GRID_DOWN` — Before: 線は1本である。After: **縦の線が揃い、布が桝目に割れている。**
  ⚠️ **桝目は空である。** 割れるのは**布**であって、**枠ではない。**
- `ACT_GRID_ACROSS` — Before: 縦の線だけがある。After: **横の線が入り、桝目が閉じる。**
- `ACT_HOLD` — Before: 格子が揃っている。After: **変わらない。** 格子が止まり、色が来ない。
  ⚠️ **この停止が、`transformation` の `TRIGGER` を画面に置いている**（S08 の0-3秒）。

# 10. CAMERA

- Camera Language: 三人称、店の前、**布が画の大部分を占める。** 立っている人の高さ。
  ⚠️ **布の面が、この9秒の舞台である。**
- Camera Events: `0-2s` 布の面に留まる。`2-5s` 線が増えるが、**カメラは格子に寄らない。**
  ⚠️ **線が浮かぶたびに寄れば、この1本は「編集されたモンタージュ」になる**——
  **この1本は切らない、と決めている。ゆえに寄らない。**
  `5-7s` 同じ面に留まる。`7-9s` 格子が止まる。**カメラは何もしない。**
- Camera Behavior: **9秒のあいだ、一度も動かない。**
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——「It holds still, or drifts once.」）。
  **この1本は、その1つを使わない。** ⚠️ **使うのは次の1本（S08）である**——
  **この作品で動くカメラは、S08 の5-9秒だけである。**
  ⚠️ **辞退は辞退として書く**（`skills/staging/SKILL.md`）。

# 11. MOTION

## Subject Motion

**格子が、一本ずつ浮かぶ。** ⚠️ **順は決まっている**——**縦 → 横。**
速さは一定である——**急がない。** **二十年かけて覚えたものが、9秒で置き直される。**
⚠️ **線は「引かれる」のではない。** この様式では、線もまた**置かれたもの**である。
⚠️ **格子は、桝目を1つずつ作っていく。** **1本の線が、2つの桝目を同時に生む。**

## Object Motion

**布は動かない。** 揺れない、浮かない、鳴らない。
⚠️ **S06 と S09 のあいだの風は、この1本には無い**——**この9秒は、灯の内側である。**

## Environmental Motion

**無い。** 埃も、風も、鳥も無い。

## Physical Characteristics

- Weight: **格子の線は鉛筆である**——重さを持たない、**盛り上がらない。**
- Inertia: 線の追加は**途中で止まらない。** 7-9秒で止まるのは、**もう引く線がないからである。**
- Acceleration: 無い。**一本ずつ、同じ間隔で浮かぶ。**
- Fluidity: ⚠️ **線は滲まない、広がらない。** **線は線である。**
- Impact: 無い。**布は、線を受けても白いままである。** **桝目の中も、白いままである。**

# 12. EMOTION

- Emotional Arc: 白 → **骨が浮かんでくる** → 格子が閉じる → **色は来ない。**
- Emotional Events: **格子が閉じた瞬間**（`7s`）。強度は中——
  ⚠️ **この2秒は、感情の停止である。** **観客は、色が来ることを予期している。**
  ⚠️ **この1本は、その予期だけを置いて終わる。**

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。** 影は落ちない。
- Lighting Events: **無い。** ⚠️ **格子を光で見せない**——**格子は鉛筆の濃さで見せる。**

# 14. AUDIO

- Dialogue: 無し。
- Sound Effects: **無し。** ⚠️ **薬缶の音を足さない**——
  草稿 L13 は「**薬缶の音の下で**」と書くが、**その音は S09 で戻る。**
  **この1本は、音の無い記憶である。** ⚠️ **音を足せば、S09 の「ぱさり」が新しくなくなる。**
- Music: 無し。⚠️ **この作品で最も禁じたい場所である**——
  **思い出の場面に音楽を置けば、この作品は「回想シーン」の修辞を持つ。**
- Environment: 店の前の、何も鳴っていない空気。
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: **灯——後ろ姿、輪郭、顔は描かない。**
- Spatial: 店の前である。**この1本は店の前を出ない。店の内側へ入らない。**
- Temporal: 朝。S06 の直後である。**S06 で「この布は動かない」を観客は覚えている。**
- Visual: 一色も出さない。**格子だけである。**
- Motion: 動くのは格子だけである。**布は動かず、カメラも動かない。**
- Sound: 無音。
- ⚠️ **この1本で浮かんだ格子は、S08 で色が入る桝目になる。**
  **格子が無いところへは色が行かない**——**ゆえにこの1本の格子の位置が、山の形を決める。**

# 16. CONSTRAINTS

⚠️ **この節は、S06 と同一の `Negative Prompt` を作る**（`L10`——`ledger.disclosure` が
S07 の開示点を `negative: covered` と宣言している）。**内訳を分けて書く。**

## MUST NOT

**この1本（S07）の危険:**
- **No montage cuts. No superimposed images. No dissolves. No fades between the memories** ——
  ⚠️ **この1本の中心的な禁止である。** **切れば、この1本は3つの変化の寄せ集めになる。**
- **No checkered pattern. No plaid. No printed textile pattern. No checkerboard** ——
  ⚠️ **格子は、布の柄ではない。** **地図の経緯線である**（2026-09-22 の裁定。`PLAN.md` §4-e）。
  ⚠️ **「布＋格子」は、モデルにとってチェック柄（ギンガム・タータン）の語彙に最も近い**——
  **等間隔の線を布の上に置けば、まず柄として呼ばれる。**
  ⚠️ **これは新しい危険である**——`bible.negative_base` の15節にも、
  `video-spec` カードの `Negative` にも、**柄を禁じる語は無い。**
  **ゆえに §16 に節を立て、§18 の `Negative Prompt` に足した**
  （⚠️ **台帳の `disclosure` を `covered` から `changed` へ上げた理由である**）。
- **No panel divisions. No split frame. No comic panels** —— 布は**1つの面**である。
  ⚠️ **この節は枠の話であって、布の話ではない**——**格子は布を桝目に割るが、
  枠をパネルに割らない。** **画は、最後まで1枚である。**
- **No face on the cloth. No drawn face** —— **この1本に顔は無い**（布に載るのは格子だけである）。
  ⚠️ **それでも節は残す。** ⛔ **理由は「S06 と同じ集合に保つこと」ではない**——
  **この1本は `changed` である**（上記の4節。`ledger.disclosure`）。
  **法が続いているから残す**——**S06 が布の上から人を降ろし、この1本も降ろしたままである。**
- No shopkeeper. No figure of the shopkeeper in frame —— **覚えられているのは腰の曲がりかたである。**
  ⚠️ **この1本には、その腰も描かれない。**
- **No lettering. No legible text on the noren. No shop name on the noren.**
  ⚠️ **草稿 L13「名を呼ぶかわりに、そうして店と家が、二十年、静かにつながっていた」**——
  **名を呼ばないことが、この作品の内容である。**
- **No drawn figure on the cloth. No illustration on the cloth. No emblem or sign on the noren** ——
  ⛔ **布に載るのは格子だけである**（2026-09-22 の裁定）。**桝目の中に、何も描かない。**
- No colour on the noren. No wash on the cloth. No shading —— **色は S08 である。**
  ⚠️ **格子は `wash` ではない**（鉛筆である）——**この節は格子を禁じていない。**
- No shop interior. No steam. No smoke. No door opening.
- No cat in frame. No visible face on the figure. No numerals, no numbers.
- **No fully-painted flat vermilion cloth** — 朱はまだ戻っていない。この禁止は S01–S07 が持つ。

**S06 から引き継いだ危険**（⛔ **「同じ集合に居る」のではない**——**この1本は4節を足して `changed` になった**）:
⚠️ **消しても `L10` は鳴らない。** `changed` は**集合が違うこと**だけを確かめ、**方向を見ない**
（`semantic.py` の `changed = set(a) != set(b)`）——
⛔ **ゆえに、この1本から節を消すときは、機械が誰も止めない。**
- **No swinging cloth. No fluttering noren. No wind in the cloth. No lifted cloth** ——
  S06 では**風が来て、布が答えなかった。** ⚠️ **この1本にも風は無い。**
- **No hand touching the cloth** —— ⚠️ **読みを明記する。**
  この節が守っているのは **S06 の指先**である。**この1本には、手が1つも描かれない**——
  **布の上に在るのは格子であって、手ではない。**

## MUST

- Full animation, not limited: **格子は9秒のあいだ、一本ずつ浮かびつづける。**
- **順が入れ替わらないこと**——**布を縦に走る線 → 布を横に走る線。**
- **布に載るのが、格子だけであること。** ⛔ **図を描かない**——**手も、頭も、品も、字も**
  （§9 `ACT_GRID_FIRST` の註）。
- **桝目の中が、空のままであること。**
- **格子が止まったあと、色が来ないこと。** ⚠️ **この2秒が山の溜めである。**
- **線を消さないこと**（`the revision stays visible`）。
- **面を1つに保つこと**——切らない、重ねない。⚠️ **桝目は布のものであって、枠のものではない。**
- **格子が、布の柄に見えないこと。** ⚠️ **地図の経緯線である**——**手で引かれた線であって、
  織られた柄ではない。** **布の目と、格子の向きが同じでも、格子は布に属さない。**

## PREFER

- 線の間隔が**一定である**こと（**おなじ順で、おなじぶんだけ**）。
- 格子が**布の目に沿っている**こと——⚠️ **S08 の色は布の目に沿って走る。
  格子と布の目が同じ向きであることが、山の前提である。**

## ALLOW

- 布の上に、線の濃淡が鉛筆の圧として残ること。

# 17. GENERATION PRIORITIES

1. **色を出さない。** 格子だけである。**色が来れば、山が消える。**
   ⚠️ **格子は、モデルにとって「塗り絵の下絵」である**——**桝目を見れば、塗りたがる。**
2. **桝目の中に図を描かない。** ⛔ **布に載るのは格子だけである**（2026-09-22 の裁定）。
   **名を持った形を書けば、モデルはそれを描く**——**手も、頭も、品も、書かない。**
3. **切らない、パネルに割らない、柄にしない。** ⚠️ **格子は布を割る。枠は1つの画である。**
   `モンタージュ` と名乗る1本を、モデルは必ずカットで組む。
   ⚠️ **そして「布＋格子」と言えば、モデルはまずチェック柄を描く**——
   **手で引いた経緯線であって、織りの柄ではない。**
4. **顔を描かない。店主を描かない。**
5. **字を入れない、名を書かない。**
6. **カメラを動かさない、寄らない。**
7. **音を入れない。**
8. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 9-second continuous cinematic take (16:9) of a faint pencil grid surfacing on a plain white cloth, one clip. Beats, deliberately uneven: [0-2s] the white cloth with nothing on it, and the first guide line surfacing on it, running down the cloth; [2-5s] the rest of the lines that run down the cloth surfacing one at a time at an even spacing, in the same order and the same amount as every time before; [5-7s] the lines that run across the cloth surfacing one by one and closing the cells; [7-9s] the grid stops and no colour comes. The core beat — the lines running down the cloth completing — holds the largest share, three of the nine seconds, and the two seconds after the grid stops are held empty so that the colour does not arrive inside them. The grid is the guide grid of a hand-drawn map, the structure that the washes will sit on; its lines are ruled by hand onto the surface of the cloth with a pencil, unevenly spaced the way a ruled guide is, and it is not printed on the cloth, not part of the weave and not a pattern in the fabric. It is not a picture of anything either: no hand, no head, no figure, no goods, no package, no emblem, no lettering and no illustration of any kind are drawn on the cloth, and the cells of the grid stay empty and white. This is one surface and the shot is never cut: every line is laid on the same single cloth, in order, one at a time, and no cut, dissolve, fade or superimposition is used, and the camera never moves closer as a new line surfaces. The cloth stays one surface and the frame stays one image: the lines divide the cloth into cells and do not divide the picture into panels. The head of no one is in the frame and no face is drawn, and the shopkeeper is not drawn at all — what is remembered is a gesture and a way of bending, not a figure. Nobody is named and nothing is written. The story's four colours are all absent from this frame: this is the thin pencil layer under the washes, with the washes not yet laid. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. Ends on a white cloth holding a faint grid and no colour, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. The front of a shop closed for the morning on a street returned to blank paper: a plain white noren, flat and unlettered, filling most of the frame, with 灯 seen from behind at the edge of the frame, back and outline, face not drawn. A faint pencil grid has surfaced on the cloth — thin, pale, evenly spaced guide lines running down the cloth and across it, the structural grid of a hand-drawn map, drawn as line only on the surface of the cloth and not soaked into it, with no colour and no wash anywhere and no shading. The cells of the grid are empty: nothing is drawn inside them and nothing is drawn between the lines — no hand, no head, no figure, no goods, no package, no emblem and no illustration of any kind are on the cloth or on the noren. The shop's interior is not in the frame; no kettle, no steam and no smoke are in the frame; no cast shadow anywhere, no light shaft, no sunbeam, no lens flare. No second person, no shopkeeper, no cat, no signage, no lettering, no numerals, no numbers, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. The guide lines surface one at a time and never all at once, in a fixed order that does not change: first the lines that run down the cloth, then the lines that run across it, and then they stop. The pace is even and unhurried, as if a hand were re-drawing in nine seconds what took twenty years to learn. The cloth itself never moves: it does not swing, does not lift, does not flutter and does not answer anything, and there is no wind in this shot. Nothing on the cloth soaks in, spreads or bleeds, no line already laid is erased or revised away, and the cells the grid makes stay empty and white. No figure and no illustration appears inside a cell. No cut, no dissolve, no fade, no wipe, no superimposition, no panel divisions, no split frame, no picture-in-picture, nothing entering or leaving the frame, and no zoom or push toward a line as it surfaces. No morphing shapes, no motion blur, no stutter, no held frames.

## Camera Prompt

Third-person, in front of the shop, at the height of a person standing, with the surface of the cloth filling most of the frame. The camera holds still for the whole nine seconds: no push, no pull, no pan, no tilt, no rack focus, no handheld, no shake, and above all no move closer to each new line — moving in on each line as it surfaces would turn this shot into an edited montage, and this shot is one surface that is never cut. [0-2s] holding on the blank cloth and the first line running down it. [2-5s] still holding while the remaining lines run down it. [5-7s] still holding while the lines across it close the cells. [7-9s] still holding as the grid stops and no colour comes, to the end. The style allows one drift; this shot spends none — the one drift in this work is spent in the next shot, and spending it here would cost that one. One continuous take; no cut.

## Audio Prompt

No dialogue and no voice of any kind. No sound effects at all: no wind, no cloth sound, no footsteps, no door, no shutter, no bird, no traffic, and in particular no kettle and no boiling water — the memory being laid on the cloth happened under the sound of a kettle, and that sound is not in this shot, because sound returns only after the colour returns, which happens in the next shot of this sequence, and putting the kettle here would spend it too early. No ambient bed beyond the still air in front of a shop that is not open yet. Music: none, and no swell, no sting, no melody, and above all no sentimental theme — music over this shot would give it the rhetoric of a flashback, which this work does not use. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no fully-painted flat vermilion cloth, no swinging cloth, no fluttering noren, no wind in the cloth, no lifted cloth, no colour on the noren, no wash on the cloth, no shading, no door opening, no steam, no smoke, no cat in frame, no visible face on the figure, no hand touching the cloth, no montage cuts, no superimposed images, no checkered pattern, no plaid, no printed textile pattern, no checkerboard

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. Here the strokes are pencil and the colour has not been laid over them yet: the shot is the map's guide grid before any wash, and the grid is not covered until the next shot. **The camera is one page of a sketchbook.** It holds still, or drifts once — and this shot spends neither. The palette stays restrained throughout, which here means no palette at all. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg07-9s-01`
- Segment ID: `01-7`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `9s`
- References: `REF_LOCATION (暖簾の店の前.base, HIGH) ／ REF_GEOGRAPHY (暖簾の店の前.geography, MEDIUM) ／ REF_CHARACTER (灯.identity, HIGH) ／ REF_PROP (暖簾.appearance, HIGH) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Attached: `灯.identity`・`灯.negatives`・`暖簾の店の前.base`・`暖簾の店の前.geography`・`暖簾の店の前.states.白`・`暖簾.appearance`・`暖簾.negative`
- Temporal Structure: `4 beats, NON_UNIFORM — sparse 2s / held 3s / sparse 2s / held 2s. The core = BEAT 2 at 2-5s (33%)`
- Camera Events: `0 events. One continuous take, camera still for the whole clip`
- Action Events: `ACT_GRID_FIRST → ACT_GRID_DOWN → ACT_GRID_ACROSS → ACT_HOLD`
- Audio Events: `no dialogue ／ no sound effects ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`
- Disclosure point: `暖簾.下のやりとり: 思い出された` — **`negative: changed`**
  （§18 は S06 と同一では**ない**。**2026-09-22 の裁定（第二）で4節が入った**——`ledger.disclosure`）

# 20. ITERATION

## Version

`0.1.0` — **まだ一度も生成していない。** これは設計であって、記録ではない。

## Observed Problems

- 無し。**生成は一度も走っていない**（`PLAN.md` §0-h）。
- ⛔ **2026-09-22 の著者の裁定（第二）で、この1本の中身が入れ替わった。**
  旧版は「**両手と下げた頭が、細い線で置かれる**」だった。裁定は
  「**暖簾の上に、具体的なモチーフは重ならない**」——**ゆえに布に載るのは格子だけである。**
  ⚠️ **旧版の内容は、こちらの読み違いであった**——
  `hakuchizu-imageboard/01-1` の「**薄い鉛筆グリッドの線画**」を「図」と読んだ
  （`PLAN.md` §4-e）。
- ⚠️ **`hakuchizu-imageboard/01-1` の「線画だけの領域を作らない」との関係は、まだ註である**
  （`PLAN.md` §1）。**採った読みは「その註はイメージボードのパネルの話である」。**
- ⚠️ **「線と色を2本に分けた」ことは、いまも発明である**（草稿は色の話しか書かない）。
  ただし**その中身は様式の下層であり、こちらの創作ではない。**

## Anticipated risks (to check in the first generation)

- **⚠️ 色が来る。** 格子だけの9秒は、モデルにとって「塗り絵の下絵」である——**塗りたがる。**
  これがこの1本の最重要の失敗である。
- **⚠️ 桝目の中に図が描かれる。** ⛔ **名を持った形を書けば、モデルはそれを描く**
  （実測: 品の名を書いた句が、布の上に魚を描かせた）。**この1本は、形を1つも名指さない。**
- **⚠️ 枠がパネルに割られる。** 格子は**布**のものである——**画は最後まで1枚である**
  （`no panel divisions` は枠の話である）。
- **⚠️ 切られる。** `モンタージュ` という語が、モデルにカットを打たせる。
  切れれば、**山の文法（切らない・過程を置かない・主体は1つ）が浮く。**
- **⚠️ 顔が描かれる、店主が描かれる。**
- **⚠️ 字が入る。** 草稿は「名を呼ぶかわりに」と書く——**名を書けば、その対比が消える。**
- **⚠️ 音楽が入る。** 思い出の場面は、モデルが最も音楽を足したがる場所である。
- **⚠️ 線が「引かれる」動きになる。** **線は置かれるのであって、描かれるのではない**——
  ペン先が走る画になれば、S08 の「一筆」の意味が薄れる。
