# ═══ 演出要約 ════════════════════════════════════
# 『白地図』第1章「暖簾」 / 運動（作画） / motion —— 白い布が、朱になる
#
#   白い布の上に、朱が戻ってくる。布の目に沿って、いちばん下の列から上へ、12秒かけて。
#   色に遅れて、色の着いたところだけが風を覚える。カメラは核の4秒で一度だけ漂う。
#   白いままの部分は、12秒のあいだ1つも動かない。一瞬で色づかせない——それは手品である。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 白地図 第1章「暖簾」 Clip 8/11 / 12s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/hakuchizu-ch01-seg08.md`）。

⛰️ **この1本が山である。** 依頼——「**暖簾に色が入ってくるシーンに盛り上がりを持って行って欲しい**」。
⚠️ **盛り上がりは、この1本を大きくすることで作っていない。**
**手前の3段——S06 の8秒・S07 の9秒・この1本の `FROM` の3秒——で作っている。**
**この1本が長いのは、作った盛り上がりを受け止める側だからである**（`PLAN.md` §1）。
⚠️ **この1本だけが `transformation` を名乗る。** 理由——**色が戻ることは、この文法そのものである。**
切らない・過程を置かない・主体は1つ・戻りは決定である。
⚠️ **隣の S09（布が鳴る）には使わない。** あれは**音が来る**ことであって、物質が変わることではない。
**文法を、変化していないショットに着せない。**
⚠️ **`Style Motion` の第一の法が、この1本の法である。**
`gouache-abstract`:「**The stroke is the event, and gouache is opaque.** A stroke covers what it crosses,
so motion is a hand returning to a shape and revising it — and the revision stays visible.」
草稿 L15「**色が白を喰い戻す。**」——**この一文の実演である。**
⚠️ **この1本だけが、カメラの身振りを1つ使う**（§10 の註）。

⛔ **2026-09-22 の著者の裁定（第三）**——「**０８は色が入って、暖簾がたなびくこと。
演出があるとすれば、そのたなびき方**」。
⚠️ **ゆえにこの1本は、色が戻ることに加えて、布が風を受ける。**
⛔ **演出は「たなびき方」に置く**——**たなびきを第4の出来事にしない。**
**たなびきは、色の到着の「様でありかた」である**（§9 の註・§11 `Object Motion`）。
⛔ **布は、白いあいだは風を知らない**（草稿 L9「風が吹いても白は揺れない。白は風を知らない」＝ S06）。
**この1本で、布はじめて風を覚える。**
⚠️ **ゆえに法は1つである**——**動くのは、色の着いたところだけである。**
**白いままの部分は、12秒のあいだ1つも動かない**（§11・§16 MUST）。
⚠️ **草稿 L15 は、この位置で「布が風を受けて、ぱさりと鳴る。白のなかにはなかった音だった」と書く。**
⛔ **この1本は、その音を鳴らさない**——**「音が戻る」は S09 の1つの変化である**（§14 の註）。
⚠️ **これは著者の裁定を仰ぐ1点である**（§20）。

⛔ **§18 の `Negative Prompt` が S07 と違う理由は、2つある。両方をここに記録する。**
① **`ledger.disclosure` の `negative: changed`**（S08 の開示点 `暖簾.朱: 戻った`）——
   `no fully-painted flat vermilion cloth` が落ち、`no flat vermilion without pigment body` と
   `no dry even vermilion paint` が入る。**台帳が記録しているのは、こちらだけである。**
② **`transformation` カードの `Negative` 8節**が加わる（`references/formats/transformation.md`——
   「**This card is `video-spec` plus one grammar**」）。
   ⚠️ **台帳はこの8節を記録していない。** **§18 が S07 と大きく違うのは、主にこちらである。**

---

# 1. VIDEO

- Duration: `12s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take, with the style's one camera drift inside it. A single change: the white cloth becomes vermilion, the colour running along the weave and covering the white one course at a time, and it does not dry; and in the manner of that change the cloth learns the wind only where the colour has taken it, so the coloured hem streams — damp and heavy, lagging behind the colour — while the part that is still white does not move at all.

# 2. WORLD

## World Concept

A place exists only at the resolution of whoever remembers it. When the last person who remembers it is gone, the town returns to blank paper.

## World Rules

- 戻りかけの色ほど早く消える（S01）。
- 白は音を持たない（S09）。
- 白の下には、人がいた気配が透けている（S03）。
- **「思い出したぶんだけ、白のなかから色が立ち上がる。」**
  ⚠️ **この1本が実演するのはこの行である。** **思い出したぶんだけ**——
  ゆえに**色は、布の目に沿って、下の列から順に白を覆う**（§9・§11）。
  ⚠️ **布の外へは、1滴も出ない。** **布が、色の器である。**
  ⛔ **2026-09-22 の著者の指示により、この1本の文字列から「格子」が外れた。**
  **色の器は、いまは布の目そのものである**（§16 の節・§20 の記録を見よ）。
- **「白は風を知らない。」**（草稿 L9——「風が吹いても白は揺れない。白は風を知らない。」）
  ⚠️ **この1本が、この法の初めての実演である。** **色が戻って、布はじめて風を覚える。**
  ⚠️ **ゆえに、動くのは色の着いたところだけである**——**風は、色の戻ったところから効く**
  （`bible.world.rules` の「音が戻るのは、色が戻ったところからである」と、同じ形の法である）。
  ⚠️ **この法は草稿に在るが、`bible.world.rules` にはまだ無い**——**この1本の法として、ここに置く。**
- 覚えることは、払うことである（S10・S11）。
  ⚠️ **この1本は「覚えた」側であり、支払いはまだ来ていない**（S10）。
- 数は町を戻さない（S05・S10）。
- **「置いた色は、もう白に戻らない。」**
  ⚠️ **この1本が、この法を成立させる1本である。** **以後、この朱は二度と白くならない。**

## Visual Language

- Art Direction: Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る。**
  ⚠️ **この1本は「soft gouache washes over visible thin pencil line art」が
  実際に起きる1本である**——**S07 が下の層で、ここが上の層である。**
  ⛔ **ただし 2026-09-22 の著者の指示で、この1本の文字列から鉛筆の層の名（格子）が外れた。**
  **ゆえにこの1本では、下の層は S07 の添付（参照画像）としてのみ在る。**
  ⚠️ **S07 の格子が残るなら、この1本はそれを覆う**——
  **S07 からも外れるなら、この1本は白い布の上に直接置かれる**（§20 の申し送り）。
- Color Language: **朱が来る。** ⚠️ **茜に近い朱。染めて二度目の冬を越した、褪せた赤**（草稿 L11）。
  **日が当たるほうの房は白っぽく、日陰の房はまだ濃い。房は藍。**
  ⚠️ **黄土と金彩は来ない。** この1本に在るのは朱と藍だけである。
  ⚠️ **群青（ultramarine）は S01 で消えたきりである**——`art_direction` の四色のうち、
  **この1本が使うのは2色である。**
- Texture: ⚠️ **絵の具は不透明である。** 色は**面ではなく、物**である——
  草稿 L15「絵の具の**盛り上がり**が白の上に載って乾いていく」。**盛り上がりを描く。**
- Rendering: ⚠️ **覆われた白は、透けない。** 水彩のように下が透けるなら、それは別の様式である。
- Visual Density: **高い。** ⚠️ **この作品で最も情報量の多い4秒（5-9s）を持つ1本である。**
- Time: `朝`
- Atmosphere: 白が、朱に喰い戻される。**色の着いた裾から、布が風を覚える。**

# 3. SUBJECTS

## 戻ってくる朱

⚠️ **主体は1つである**（`transformation` の `one change one subject`）。
**主体は朱である。布は主体ではない。**
⚠️ **布の動きは、朱の到着の証拠であって、第2の主体ではない**——
**動くのは、色が着いたところだけである**（§9 の註・§11 `Object Motion`）。

- Reference: `暖簾.negative` のうち**乾きと平坦を禁じる2節**が、この1本で入れ替わる（`ledger.disclosure`）
- Appearance: **染めて二度目の冬を越した、褪せた朱。** 新しい朱ではない——
  **褪せかたまで戻る。** 日が当たるほうの房は白っぽく、日陰の房はまだ濃い。
  房は**藍**。⚠️ **まだ乾いていない**——**指の腹に、絵の具の重さが残る**（草稿 L23）。
- Behavior: **白の底からにじみ、布の目に沿って、白を下の列から順に覆う。**
  ⚠️ **放射状に広がらない。** ⚠️ **速くならない**——**灯が二十年かけて覚えたものであり、その速さで戻る。**
  ⚠️ **順は、いちばん下の列から上へである。** **それだけが、この1本の段取りである。**
- Continuity Requirements: ⚠️ **色の器は、布の目そのものである**——
  **色は布の目に沿って走り、布の外へは行かない。**
  ⛔ **2026-09-22 の著者の指示までは、ここは「S07 で浮かんだ格子」だった。**
  **格子は、この1本の文字列から外れた**（§16 の節・§20 の記録）。
  ⚠️ **色は、思い出の順に来る**——**いちばん下の列からである。**
  ⚠️ **色が先で、布が後である。** **色の通ったところまでしか、布は動かない**（§11）。

## 暖簾（`KEEP` の側）

- Reference: `暖簾.appearance`・`暖簾の店の前.states.朱が戻った`
- Behavior: ⚠️ **白いあいだ、布は動かない**（草稿 L9）。**S06 で観客が身体で覚えた
  「この布は動かない」が、この1本の前提である。**
  ⛔ **色が着いたところから、布は風を覚える**（著者の裁定・第三）。
  **動くのは、色の着いたところだけである**——**上は棒に留まったまま、下の裾だけが、遅れて流れる。**
  ⚠️ **濡れているので、重い。** **乾いた旗のように鳴らない、はためかない、膨らまない**——
  **押されて、少し流れて、戻る**（草稿 L23「朱はまだ乾いていない」）。
  ⚠️ **順は、色と同じである**——**下から上へ。** **色が上がれば、動くところも上がる。**
  ⚠️ **9-11秒で、たなびきは落ち着く。** **12秒の終わりに、布はまた垂れている**——
  **S09 の「一度だけ揺れる」は、そこで新しく来る風である。**
- Continuity Requirements: ⚠️ **房は「下へ垂れる」であって、「染まる」ではない。**
  染まるは面の話であり、**垂れるは物が下へ着く話である。**
  ⚠️ **房は、いちばん最後まで動く**——**自由な端であり、しかも濡れている。**

## 灯（⛔ この1本には写らない）

⛔ **2026-09-22 の著者の裁定**——「**０８に人物は不要**」。
⚠️ **この裁定は、先に出た「人物は外さない」を打ち消さない**——**著者の註が、それを言っている**——
「**全体からは外さないという意味。０８に人物は不要**」。
⛔ **ゆえに、外れるのはこの1本の画からだけである。灯は、この作品に居る。**

- Reference: ⛔ **無し。** **この1本は `灯.identity` を添付しない**（§6・§19）——
  **添付は、写る者の基準を渡す欄である。** **写らない者に、基準は要らない。**
- Appearance: ⛔ **この1本には、後ろ姿も、輪郭も、置かない。** **画の端にも置かない。**
- Behavior: ⛔ **「この1本に灯の所作は無い」のではない。** **この1本に灯は居ない。**
  ⚠️ **色は、誰かが塗るのではない**——**思い出された色が、白の下から来る**——
  **§18 `Visual Prompt` が、そう書いている。**
- ⚠️ **外していないもの**——**S06・S07 に灯は写り**、台帳の `灯.identity` は生きており、
  `forbidden_set` の `灯の顔` も、§18 `Negative Prompt` の2節も、そのままである。

⚠️ **§18 `Negative Prompt` の2節（`no fully rendered face for 灯`・`no fully rendered person
other than 灯`）は、この裁定でも動かしていない**——**節の集合を動かせば、開示の記録
（`ledger.disclosure` の `negative: changed`・81節）と `L10`・`L14` が動く。**
⛔ **ゆえに、生成へ渡る文字列のうち、灯の名を持つのは、この2節だけになった**——
**この2節を持つ5本に字は出ていない**（§20 `Observed Problems` ① の傍証）。**報告する点である。**

# 4. ENVIRONMENT

- Location: `暖簾の店の前`（`.base`・`.geography`・`.states.朱が戻った`）
- Environment Elements: 店の前の石畳、**朱い暖簾**、閉じた店。
  ⚠️ **店の内側は画に入らない**（`PLAN.md` §0-f）。**湯気を出さない、薬缶を置かない。**
- Environmental Behavior: ⛔ **風が、この1本で初めて通る。** ⚠️ **弱い風である**（著者・2026-09-22
  ——「もちろん強い風は受けないよ」）。**一方向に、ひとつだけ**——
  ⚠️ **強くならない、吹き抜けない、通り過ぎない**（S09 の風と、同じ風である）。
  ⛔ **布は、風に持っていかれない。** **押されて、少しだけ流れる。**
  ⚠️ **風は、色の着いたところでだけ見える**——**白いままの部分が動かないので、風はそこに無い。**
  ⚠️ **埃も、鳥も、湯気も無い。**
  ⚠️ **戸を開けない**——**戸が開くのは S09 の気配である。**

# 5. OBJECTS

- `暖簾` — この1本の面である。**朱が戻る場所である。**
- 暖簾の店の前 — この1本の場所である。
- `白い形`・`水の跡`・`薬缶` — **この1本には無い。**

# 6. REFERENCES

- REF_LOCATION: `暖簾の店の前.base` (HIGH)
- REF_GEOGRAPHY: `暖簾の店の前.geography` (MEDIUM)
- ⛔ **`REF_CHARACTER` は、この1本には無い。**
  旧い行は ``- REF_CHARACTER: `灯.identity` (HIGH)`` だった。⚠️ **2026-09-22 の著者の裁定で、
  この1本に人物は要らない**（§3 の註）——**人物の基準を渡す先が無い。**
  ⚠️ **ゆえに `attached`（`shots/hakuchizu-ch01-seg08.yaml`・§19）からも落ちている。**
  ⚠️ **この1本に人物は居ないが、灯は作品から外れていない**（§3 の註）。
- REF_PROP: `暖簾.appearance` (HIGH — この1本の `KEEP` である)
- REF_STYLE: `gouache-abstract` (HIGH)
- **REF_FORMAT: `transformation`** — ⚠️ **この1本だけである。**
  `video-spec` に文法が1つ加わった形であり、**その文法は §9 `ACTION` と §11 `MOTION` が負う**
  （`references/formats/transformation.md`）
- REF_SOURCE: `projects/hakuchizu/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/hakuchizu/ledger.yaml` (CRITICAL — `negative: changed` がこの1本の §18 を決める)

# 7. NARRATIVE

- Core Event: 白い布が、朱になる。**色の着いた裾から、布が風を受けて、たなびく。**
- Beginning: **`FROM`。** 白い布（S07 の終わりの状態）。**何も起きない。**
  ⚠️ **風は、まだ布に効いていない**——**白は風を知らない**（草稿 L9）。**白い部分は1つも動かない。**
  ⛔ **この1本の文字列は、布の上に何も名指さない**（2026-09-22 の著者の指示）。
  ⚠️ **S07 の1枚が格子を持っていれば、最初のコマは添付からそれを引き継ぐ**——
  **この1本は、それを名指さず、禁じもしない**（§20 の申し送り）。
- Turn: **いちばん下の列に、朱が入る。最初の一筆が置かれる。**
  ⚠️ **そして、その一筆の裾だけが、はじめて風を受ける**——**ひとつ、小さく動く。**
- Peak: **`CORE`。** 朱が下の列から順に布を覆い、列が上へ上がっていく。**色が白を喰い戻す。**
  ⚠️ **たなびきは、色の後ろを追う**——**色が上がれば、動くところも上がる。**
  **白いままの上のほうは、12秒のあいだ1つも動かない。**
- Pull: **`TO`。** 朱。**まだ乾いていない。**
  ⚠️ **たなびきは落ち着いている**——**布は、また垂れている。** **最後に動くのは、房である。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-3s` — density: `held` — **`FROM`。** 白い布。**何も起きない。**
    ⚠️ **支払いの直前の静止である。** 手前の S06 と S07 で作った溜めの、最後の3秒。
    **ここを削れば、山は山でなくなる。**
    ⚠️ **白いあいだ、布は風を知らない**——**この3秒、布は1つも動かない**（S06 と同じ状態である）。
  - BEAT 2 `3-5s` — density: `sparse` — **白の底から朱がにじみはじめる。**
    最初の一筆は、**いちばん下の列である。**
    ⚠️ **その一筆の裾だけが、はじめて風を受ける**——**ひとつ、小さく動く。**
    ⛔ **白いままの部分は、ここでも動かない。**
  - BEAT 3 `5-9s` — density: `held` — **`CORE`。** 朱が下の列から順に布を覆い、
    列が上へ上がっていく。
    ⚠️ **たなびきは、色に遅れて、上へ移る**——**動くのは、色の着いたところだけである。**
    ⚠️ **この4秒が12秒の33%である。** **この1本の不均等の在り処が、この4秒である。**
    ⚠️ **カメラはここで一度だけ漂う**（§10）。
  - BEAT 4 `9-11s` — density: `held` — 藍の房が下へ垂れる。**絵の具の盛り上がりが白の上に載って
    乾いていく**——ただし**乾ききらない。**
    ⚠️ **たなびきが、落ち着いていく**——**濡れた布の落ち着きかたで、ゆっくり止まる。**
  - BEAT 5 `11-12s` — density: `sparse` — **`TO`。** 朱。**まだ乾いていない。**
    ⚠️ **この1秒は、色を見せる1秒ではない。濡れていることを見せる1秒である。**
    ⚠️ **布は、また垂れている**——**最後に動いているのは、房である。**
- Temporal Density: ⚠️ **`held` が3つ（3秒＋4秒＋2秒）あり、その間を `sparse` が挟む。**
  **この作品で最も `held` の多い1本である**——**山は、止まっている時間が最も長い。**

# 9. ACTION

⚠️ **`transformation` の文法は、この節と §11 が負う。5項をここに明示する。**

- **`FROM`** … 白い布。**色はどこにも無い。**
  ⛔ **この行は、2026-09-22 の著者の指示で「薄い鉛筆の格子だけがある」から変わった**——
  **著者は、この1本の文字列から格子を外した**（§16 の節・§20 の記録）。
- **`TO`** … 朱。**染めて二度目の冬を越した、褪せた赤。まだ乾いていない。房は藍。**
- **`TRIGGER`** … **灯が思い出し終えること。** ⚠️ **トリガーは「来る」ものではない**——
  **S07 の7-9秒で、すでに置かれている。**
  ゆえにこの1本の0-3秒は、**トリガーが引かれるのを待つのではなく、結果が来るのを待つ3秒である。**
- **`KEEP`** … **構図、そして白いままの部分。** ⚠️ **この2つは、12秒のあいだ1つも変わらない**
  （§16 の MUST）。
  ⚠️ **変わるのは、色と、色の着いたところの布の形である**——**布の動きは、色の到着に属する。**
  ⛔ **旧い `KEEP` は「格子・構図」と3つ挙げ、「格子は、色に覆われても消えない
  （`the revision stays visible`）——色の下に読める」と書いていた。**
  **この2行は、2026-09-22 の著者の指示で外れた**——**格子はこの1本の文字列に無い。**
  ⚠️ **そして、この「色の下に読める」が、格子を布の柄として描かせた節である**
  （§20 の記録——初回生成の 8-10秒に、朱の上へ薄い線が残った）。
- **`DURATION`** … `12s`。**この作品で最長である。**

- `ACT_WELL` — Before: 白の底に色が無い。After: **いちばん下の列が、朱で覆われている。**
  ⚠️ **その一筆の裾が、はじめて風を受けて、ひとつ動く。**
  Causes: **`TRIGGER`**（灯が思い出し終えたこと）。⚠️ **一瞬では起きない。**
- `ACT_RUN` — Before: 下の列が1つ覆われている。After: **朱が下の列から順に布を覆い、
  列が上へ上がっている。**
  ⚠️ **色の着いたところだけが、風を受けて、色に遅れて流れている。**
  ⚠️ **主体は朱である。** ⚠️ **布がするのは、色の着いたところが風を受けることだけである。
  布は何もしない**——**布は器である。**
  ⚠️ **列を飛ばさない。布の外へ出ない。**
- `ACT_SETTLE` — Before: 布は朱である。After: **藍の房が下へ垂れ、盛り上がりが載っている。
  たなびきが落ち着き、布はまた垂れている。**
  ⚠️ **乾ききらない。** **濡れは S11 まで保たれる。**
- ⚠️ **`ACT_DRY` は無い。** **乾かせば、S11 の指の腹が確かめるものが消える。**
- ⚠️ **`ACT_STREAM` を4つ目に立てない。** ⛔ **著者の裁定——演出は「たなびき方」に置く。**
  **ゆえにたなびきは、動作ではなく、`ACT_WELL`／`ACT_RUN`／`ACT_SETTLE` の「様でありかた」である。**
  ⚠️ **動作を1つ足せば、この1本は「色が戻り、そして布が動く」という2つの出来事を持つ。**
  **そうではなく、この1本は「色が戻ると、布はじめて風を覚える」という1つの出来事である。**
- ⚠️ **第2の主体を置かない**（`no second simultaneous transformation`）。
  **布の動きは、第2の主体ではない**——**朱の到着の、証拠である。**

# 10. CAMERA

- Camera Language: 三人称、店の前、**布が画の大部分を占める。** 立っている人の高さ。
- Camera Events: `0-3s` 布に留まる。`3-5s` 最初の一筆が置かれる——**カメラは動かない。**
  ⚠️ **一筆目で動けば、この身振りは「色の到着」に使われてしまう。**
  `5-9s` **カメラは一度だけ漂う。** `9-11s` 房に留まる。`11-12s` 留まったまま終わる。
  ⚠️ **たなびきは、カメラの身振りを1つも増やさない**——**布の動きとカメラの漂いは別である。**
- Camera Behavior: **12秒のうち、動くのは5-9秒の4秒だけである。**
  ⚠️ **様式はカメラに身振りを1つ許している**（`gouache-abstract`——
  「**It holds still, or drifts once.**」）。**この作品は、その「一度」をこの1本に使う。** 理由——
  ① **漂いは有限の資源である。** 11本のうち1本しか使えない。
     ならば**使うなら、いちばん大きい出来事の上で使う。**
  ② ⚠️ **漂いは、核の4秒に置かれる**——**色が布を覆い上がる4秒と、カメラが動く4秒が同じである。**
     ⛔ **色を追わない。色に速さを合わせない**——**速さを合わせれば、色は画のなかで止まって見える。**
     **動くのは4秒、向きはひとつ、それだけである。**
  ③ ⚠️ **他の10本は、この身振りを1度も使わない。** 使えば、
     **山の1本が、他の1本と同じ身振りを持つことになる。**
  ⚠️ **`L33` がこの欄を読む**（`skills/staging/cards.yaml`）——
  **禁じるのではなく、認めて書く**（ゆえに §18 の `Camera Prompt` は、この語を肯定形で1度だけ置く）。

# 11. MOTION

## Subject Motion

⚠️ **`transformation` の文法は、この節と §9 が負う。**
**白の底から朱がにじみ、にじんだ朱が、布の目に沿って、下の列から白を覆う。**
草稿 L15「白の底から朱がにじみ、**にじんだ朱が布の目に沿って走り**」「**色が白を喰い戻す。**」
⚠️ **放射状に広がらない。** **布の外へは色が行かない**——**色は、布の目に沿って走る。**
⚠️ **順は、下から上へ、一列ずつである。** **列は飛ばさない。**
⛔ **この段落は、2026-09-22 の著者の指示で書き換わった**——
**旧い文は「格子の桝目をひとつずつ埋める」「桝目の中を走る」だった。**
⚠️ **戻した先は、草稿そのものである**——**草稿 L15 は「布の目に沿って走り」と書いている**（S07 の註）。
⚠️ **速くならない。** **12秒かけて、白が朱になる**——**一瞬で色づけば、それは手品である。**

## Object Motion

⛔ **動くのは、色の着いたところだけである。** **白いままの部分は、12秒のあいだ1つも動かない**——
**S06 で観客が身体で覚えた「この布は動かない」は、色の着いたところでは、もう成り立たない。**
⚠️ **これが、著者の裁定「演出は、たなびき方」の実体である。** たなびき方は、5つである——

1. ⚠️ **下からである。** 色は下の列から来る。**しかも動けるのは、棒に留められていない裾だけである**
   ——**上は、棒に留まっている。** ゆえに**たなびきは、裾で起きる。**
2. ⚠️ **色に遅れる。** **色が先で、布が後である**——**たなびきは、色の先頭を追い越さない。**
   **色が上がれば、動くところも、遅れて上がる。**
3. ⚠️ **重い。** **濡れているからである**（草稿 L23「朱はまだ乾いていない」）。
   **押されて、少し流れて、戻る**——**乾いた旗のように鳴らず、はためかず、膨らまない。**
   ⛔ **風は弱い。** **布は風に持っていかれない。**
4. ⚠️ **一方向である。** **風はひとつである**——**往復しない、波打たない、震えない。**
5. ⚠️ **終わりに落ち着く。** **9-11秒で、たなびきは止まりかける。**
   **12秒の終わりに、布はまた垂れている**——**S09 の「一度だけ揺れる」は、そこで新しく来る風である。**

⚠️ **房は、いちばん最後まで動く**——**自由な端であり、しかも濡れている。**
房は9-11秒に**下へ垂れる**——⚠️ **染まるのではなく、着くのである。**
**この様式の色は物である**——ゆえに房は、**物として下へ落ち着く。**

## Environmental Motion

⛔ **風が、この1本で初めて通る**（著者の裁定・第三）。**弱い風である**——
⚠️ **強くならない、吹き抜けない、通り過ぎない**（S09 の風と、同じ風である）。
⚠️ **風は、色の着いたところでだけ見える**——**白いままの部分が1つも動かないので、風はそこに無い。**
**無いもの**——埃も、鳥も、湯気も無い。⚠️ **戸を開けない。**

## Physical Characteristics

- Weight: ⚠️ **絵の具は重さを持つ。** 盛り上がりが白の上に載る——
  **この1本の色は、面ではなく物である。** ⚠️ **布も、まだ濡れている**——
  **ゆえにたなびきは重い。** **押されて少し流れ、すぐ落ち着く。**
- Inertia: 走りはじめた朱は**途中で止まらない。** **止まれば、それは「塗り残し」である。**
  ⚠️ **布の側は、逆である**——**たなびきは続かない。**
  **慣性で流れつづければ、それは別の布である**（S09 と同じ法）。
- Acceleration: ⚠️ **無い。** 速まらない——**加速すれば、それは手品の速さである。**
  布も同じである——**風は弱く、動きは速くならない。**
- Fluidity: ⚠️ **水彩ではない。** 覆われた白は**透けない**——
  **にじみの輪郭が残るのは、修正が残るからである**（`the revision stays visible`）。
  ⚠️ **布は、水のように流れない**——**濡れた布の重さで流れる。**
- Impact: ⚠️ **色は、布を傷めない。** **染み込むのではなく、載る。**
  ⚠️ **風も、布を傷めない。** **押すだけで、持っていかない。**

# 12. EMOTION

- Emotional Arc: 白 → **朱** → **まだ乾いていない。**
- Emotional Events: **`CORE` の4秒**（`5-9s`）。強度は**この作品で最大**——
  ⚠️ **ただし、音楽でも、寄りでも、加速でも作らない。**
  **作るのは、手前の3段（S06 の8秒・S07 の9秒・この1本の0-3秒）の溜めだけである。**

# 13. LIGHTING

- Base Lighting: 朝。**方向を持たない、平らな光。**
  ⚠️ **ゆえに「日が当たるほうの房」は、光の話ではない**——**褪せかたの話である**（草稿 L11）。
- Lighting Events: **無い。** ⚠️ **色を光で見せない。**

# 14. AUDIO

- Dialogue: 無し。
- Sound Effects: **無し。** ⛔ **布が動いても、この1本は鳴らない。**
  ⚠️ **法のためではない。段取りのためである**——**「音が戻る」は S09 の1つの変化である**
  （1ショットは1つの変化である。`CLAUDE.md`）。**この1本が音を持てば、S09 は持つものが無い。**
  `bible.world.rules`——**白は音を持たない。音が戻るのは、色が戻ったところからである。**
  ⚠️ **朱は9-11秒に戻っているので、ここで音を鳴らすことは、法に反しない。**
  **鳴らさないのは、法ではなく段取りである。**
  ⛔ **草稿 L15 は、この位置で「布が風を受けて、ぱさりと鳴る。白のなかにはなかった音だった」と書く。**
  **この1本は、その1文を S09 に譲る**——⚠️ **著者の裁定を仰ぐ1点である**（§20）。
  ⚠️ **ゆえに §18 の `Audio Prompt` は「no sound」を明示する**——
  **動くものが在るのに鳴らない、という状態を、明示的に書く。**
- Music: 無し。⛔ **この1本に音楽を置けば、山は別の山になる。**
  **この作品の山は、手前の溜めだけで作られている。**
- Environment: 店の前の、何も鳴っていない空気。**風は在るが、鳴らない。**
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**（`bible.language` の註）。

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic.

- Character: ⛔ **この1本に人物は居ない**（著者・2026-09-22「０８に人物は不要」）——
  **誰も描かない。手も、頭も、置かない。**
- Spatial: 店の前である。**この1本は店の前を出ない。店の内側へ入らない。**
- Temporal: 朝。S07 の直後である。
- Visual: 朱と藍。⚠️ **黄土と金彩は来ない。**
- **Motion（`KEEP`）**: **構図、そして白いままの部分は、12秒のあいだ1つも変わらない**——
  ⚠️ **変わるのは、色と、色の着いたところの布の形である。**
  ⚠️ **たなびきは、9-11秒で落ち着く**——**終わりに、布はまた垂れている。**
- ⚠️ **この1本の風は、S09 の風と同じ風である。** **風は、この1本で初めて通る**（著者の裁定・第三）。
- Sound: 無音。⚠️ **布が動いても、鳴らない**（§14）。
- ⚠️ **この1本の終わりの状態が、S09・S10・S11 の前提である。**
  **朱は、以後、二度と白くならない**（7つ目の法）。

# 16. CONSTRAINTS

## MUST NOT

**`transformation` の avoid-list**（`references/formats/transformation.md`）:
- **No cut. No dissolve. No wipe.** —— **1つの変化は、1つの画である。**
- **No stated process.** —— ⚠️ **「塗られている」ことを、道具や手順で説明しない。**
- **No intermediate stage held.** —— ⚠️ **半ばまで朱になった布を、途中で保たない。**
  **保てば、この1本は「工程の画」になる。**
- **No caption naming the change. No voice-over naming the change.**
- **No second simultaneous transformation.** —— **主体は朱ひとつである。**

**この1本の危険:**
- **No colour arriving instantly. No flash of colour. No colouring in one frame** ——
  ⚠️ **最も起きやすい失敗である。** **一瞬で色づけば、それは手品である。**
- **No uniformly painted cloth. No even flat colour field** ——
  **塗りの厚さにムラがあること**（`no flat vermilion without pigment body`）。
- **No dry even vermilion paint. No fully dried vermilion** —— 草稿 L23「朱は**まだ乾いていない**」。
- **No colour spilling off the cloth. No colour on the white ground beyond the cloth** ——
  **色は布の上にだけ載る。**
- **No hand touching the cloth. No hand painting the cloth. No brush in frame** ——
  ⚠️ **この1本の色は、誰も塗らない。** **灯の指が触れるのは S11 である。**
- No outward radial spread. No colour crossing a line it does not follow.
  No colour leaving the course it is filling. No skipping a course ——
  **色は布の目に沿って走り、走っている列に留まる。**
  ⛔ **旧い文は「`No colour leaving the cell it is filling`／`No skipping a cell`／
  桝目の中に留まる」だった。****この1本の文字列から格子が外れたので、器は布の目になった**
  （2026-09-22 の著者の指示・§20 の記録）。
- **No panel divisions. No split frame. No comic panels** ——
  ⚠️ **この節は枠の話であって、布の話ではない**——**布を何かに割っても、枠をパネルに割らない。**
  ⛔ **旧い註は「格子は布を桝目に割るが」と書いていた。**
  ⚠️ **この危険は、格子を外した今も残る**——**布が等間隔に区切られて見えれば、枠が読まれる。**
  **枠は最後まで1枚である。**
- **No checkered pattern. No plaid. No printed textile pattern. No checkerboard** ——
  ⛔ **旧い註は「格子は地図の経緯線であって、布の柄ではない」と書いていた。**
  **その註は、初回生成で破れた**——**朱の上に薄い線が残り、柄として読まれた**
  （§20 の記録——8-10秒の画）。
  ⚠️ **ゆえに、この4節は格子を外した後も残す**——
  **布が一色に塗られていく画そのものが、いちばん柄に読まれやすい。**
  **順を「下から上へ」にしてあるのは、その歯止めでもある**（**朱の帯が上がる。市松にしない**）。
  ⚠️ **`bible.negative_base` にも、`video-spec` カードの `Negative` にも、柄を禁じる語は無い**——
  **ゆえに §16 に節を立て、§18 の `Negative Prompt` に足した**（`PLAN.md` §4-e）。
- ⛔ **布は動く。動きかたが法である**（2026-09-22 の著者の裁定・第三）——
  **ただし、動くのは色の着いたところだけである。**
- **No movement in the part of the cloth that is still white. No stirring of the white cloth.
  No wind in the white part of the cloth** ——
  ⚠️ **これが、この1本の映像の第一の法である**（草稿 L9「白は風を知らない」＝ S06）。
  **白いままの部分は、12秒のあいだ1つも動かない。**
- **No dry cloth. No snapping cloth. No flag-like snapping. No whipping cloth** ——
  ⚠️ **布は濡れている**（草稿 L23）。**乾いた旗の動きをさせない。**
- **No billowing cloth. No inflated cloth. No sail-like cloth** ——
  ⚠️ **膨らませない。** **たなびきは、裾で起きる。**
- **No flapping cloth. No oscillating cloth. No rippling cloth. No cloth swinging back and forth**
  —— ⚠️ **風はひとつである。** **往復しない、波打たない、震えない。**
- **No strong wind. No gust. No wind lifting the cloth** ——
  ⚠️ **弱い風である。** **布は、風に持っていかれない**（著者・2026-09-22）。
- **No cloth sound. No rustle of cloth** —— ⚠️ **動くものが在るのに、鳴らない**（§14）。
- **No motion in the cloth above the coloured part** ——
  ⚠️ **たなびきは、色の先頭を追い越さない。** **色が先で、布が後である。**
- No lifted cloth. **No cloth lifted off the bar. No hand lifting the cloth** ——
  ⚠️ **布は、棒から離れない。** **押し上げる手は、この1本に無い**（草稿 L11 の手は S06/S07 の話である）。
- No shading —— ⚠️ **褪せのムラは顔料の密度であって、陰影ではない。**
- No steam. No smoke. No door opening. No shop interior. No shopkeeper.
- No face on the cloth. No drawn face. No visible face on the figure. No cat in frame.
- **No goods drawn on the cloth. No fish drawn on the cloth. No bundle or package on the cloth.
  No illustration on the cloth. No emblem or sign on the noren. No scales and no drawn eye** ——
  ⛔ **布には、何も載せない。** ⛔ **そして、この節は文字にも掛かる**——
  **布の上にも、壁の上にも、画のどこにも、字を置かない**（下の `No lettering` の節）。
  ⚠️ **2026-09-22 の著者の裁定（第二）である**——「**暖簾の上に、具体的なモチーフは重ならない**」。
  **ゆえに S07 が置くものも、格子だけになった**（`hakuchizu-ch01-seg07.md` §9 の註）。
  ⛔ **そして同じ日の第三の指示で、その格子もこの1本の文字列から外れた**——
  **この1本では、布に載るのは色だけである**（§20 の記録）。
  ⚠️ **初回生成では、この布の上に魚の絵が描かれた。** 理由は **S07 が品の名を書いたこと**であり、
  **S08 は S07 の線の上に色を通すので、S07 の誤りは、この1本では色の画になって現れる。**
  ⛔ **品を描けば、無字の暖簾が看板になる。**
- No numerals, no numbers. No lettering. No legible text on the noren. No shop name on the noren.
  ⛔ **2026-09-22 の初回生成で、画の左下に「灯」の字が描かれた**（§20 の記録——8枚の既存節では
  防げなかった）。**ゆえに、この1本の肯定文から、名の字が外された**——
  **同じ日の裁定で、人そのものも、この1本の画から外れた**（§3 の註・§20 の記録）。
  ⚠️ **Negative の節は、名詞を消せない**——**肯定文が名指した名詞を、モデルは描く。**
  ⛔ **この節は、いまも残す。** **消したのは語であって、危険ではない。**
- ⛔ **`no fully-painted flat vermilion cloth` は、この1本では落ちる**（`ledger.disclosure` の
  `negative: changed`）。**朱は戻ったので、この節は用済みである。**

## MUST

- Full animation, not limited: **色は12秒のあいだ、走りつづける。**
- **`KEEP` を1つも変えないこと**——構図、そして**白いままの部分**。
- **`TRIGGER` を待たないこと。** **結果が来るのを待つ3秒である。**
- **色が布の目に沿って走ること。** 放射状に広がらない。
- **布が、色の器であること**——**列を飛ばさない。布の外へ出ない。**
- **順があること。** ⚠️ **いちばん下の列から、上へ。**
  ⚠️ **順は、市松を避ける歯止めでもある**——**面で塗らせず、列で塗らせれば、
  布は一度に半分だけ色になる**（**朱と白が並ぶ時間を、帯の形に保つ**）。
- ⛔ **たなびきの法（著者の裁定・第三）**——**5つとも守ること。**
  ① **動くのは、色の着いたところだけである**（白いままの部分は、1つも動かない）。
  ② **下からである**——**裾が動く。棒に留まった上は動かない。**
  ③ **色に遅れる**——**たなびきは、色の先頭を追い越さない。**
  ④ **濡れて重い**——**乾いた旗にしない。はためかせない、膨らませない、鳴らさない。**
  ⑤ **一方向である**——**往復しない、波打たない、震えない。**
- **9-11秒で、たなびきが落ち着くこと。** ⚠️ **終わりに、布はまた垂れている。**
  ⛔ **S09 の「一度だけ揺れる」を、ここで先に使わない。**
- **朱が褪せていること**——新しい朱ではない。**褪せかたまで戻る。**
- **盛り上がりを描くこと。** 絵の具は物である。
- **乾ききらないこと。**
- **カメラは5-9秒に一度だけ漂うこと**——**核の4秒に、一度だけ。色を追わず、速さを合わせず。**
- **布が動いても、鳴らさないこと**（§14）。

## PREFER

- 一筆目が置かれる位置が、**思い出の順の最初である**こと。
- ⛔ **旧い文は「格子の線が、色の下に読めること——修正は残る」だった。**
  **この1行は外れた**——**格子はこの1本の文字列に無く、そしてこの1行が、
  初回生成で朱の上に薄い線を残させた**（§20 の記録）。
  ⚠️ **代わりに残るのは、色そのものの修正の跡である**——**塗り重ねた跡と、乾ききらない面**。
- 日が当たるほうの房が白っぽく、日陰の房が濃いこと。
- ⛔ **たなびきが、色の波の跡を追っていること**——**色の通った列の裾から、遅れて動き出す。**

## ALLOW

- 紙の目に沿った、絵の具の濃淡（**顔料の密度である**）。

# 17. GENERATION PRIORITIES

1. **一瞬で色づかない。** ⚠️ **この1本の最重要の失敗である。**
   **12秒かけて白が朱になる**——**速さは、灯が二十年かけた速さである。**
2. **放射状に広げない。布の外へ出ない。** 色は**布の目に沿って**走り、**列の中に留まる**
   ——**布が、色の器である。**
   ⚠️ **塗り跡の区画は、モデルにとって「塗り絵の区画」である**——**列で、順に塗らせる。**
   **順を書かねば、モデルは好きなところから塗る。**
3. **半端な段階を保たない。** 途中で止めれば、この1本は工程の画になる。
4. ⛔ **たなびきを、乾いた旗にしない。** ⚠️ **これが著者の言う「演出」である**——
   **濡れて、重く、下から、色に遅れて、一方向、そして落ち着く。**
   **弱い風である**——**布は、風に持っていかれない。**
5. **色の着いたところだけを動かす。** ⚠️ **白いままの部分は、1つも動かない**——
   **S06 の8秒が、この1本のために使われている。**
6. **音を足さない。音楽を足さない。** ⚠️ **布が動いても、鳴らさない**（§14）。
7. **乾かさない。** 濡れは S11 まで保たれる。
8. **カメラは5-9秒に一度だけ漂う。** 追わない、速さを合わせない、他の区間で動かない。
9. **顔を描かない。店主を描かない。店の内側を入れない。**
10. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 12-second continuous cinematic take (16:9) of a plain white noren becoming vermilion, one clip. Beats, deliberately uneven: [0-3s] the plain white cloth with nothing on it and nothing happening, which is the last three seconds of a build-up that began two shots earlier; [3-5s] the vermilion begins to well up from beneath the white at its lowest course, so that the colour arrives in the order of the remembering, and that first strip of cloth at the hem is the first piece of it to learn the wind and stirs once; [5-9s] the core, four of the twelve seconds, in which the bleeding vermilion runs along the weave and covers the white one course at a time, taking the lowest course first and then the course above it, and the colour eats back into the white, while the streaming of the cloth follows the colour upward and never gets ahead of it; [9-11s] the indigo tassels come to hang down and the raised body of the paint sits on the white and begins to dry, without drying through, and the streaming comes to rest, the cloth settling the way wet cloth settles; [11-12s] vermilion, and still not dry, and the cloth hanging down again. The change has one subject and one trigger: the vermilion is the subject and the trigger is that the woman has finished remembering, which was placed two shots ago and is not shown again here. The cloth learns the wind only where the colour has reached it, and nowhere else: the part that is still white hangs exactly as it has hung all along, without moving at all, and the coloured hem streams — the wind is a light one and does not carry the cloth anywhere, the cloth is pushed a little, streams a little, and comes back, damp and heavy, in one direction only, never snapping like a dry flag, never whipping, never flapping, never billowing, never swinging back and forth, and never outrunning the colour. Nothing is drawn on the cloth, then or now: no hand, no figure, no goods and no illustration appear on it, and no lettering and no written character appear anywhere in the frame. The colour does not arrive at once and is never shown in a single frame: it is the faded vermilion of a cloth through a second winter, paler on the hems that faced the sun and deeper on the hems that stayed in shade, its lower hems indigo, with pigment body and an uneven surface, and it does not spread outward from a point, it does not skip a course, it never leaves the course it is filling, it does not leave the cloth, and it does not dry. The story's four colours have two of themselves in this frame. The white ground is kept pure white, not cream or ivory, and no overall yellow cast. Flat and paper-based, no directional light, no spatial illusion. No sound of any kind comes from the cloth or from the wind. Ends on a vermilion cloth that is still wet and has just come to rest, and the clip ends there, without a resolving beat.

## Visual Prompt

Hand-colored old map — rough slightly-textured white paper, soft gouache washes over visible thin pencil line art. The story's four colors — vermilion, ultramarine, ochre, and a faint glimmer of gold gilt — with vermilion and ultramarine foremost and ochre and gold only as small accents. No overall yellow cast; the white ground kept pure white (not cream or ivory). Natural variation in pigment density, dry-brush marks, exposed paper, wet ink edges, large quiet negative space. Flat and paper-based, no directional light, no spatial illusion. Minimal, tactile, poetic, slightly melancholic. The front of a shop closed for the morning on a street returned to blank paper: a noren filling most of the frame, and nobody in the frame — the colour arrives because it is remembered, and nobody paints it. The cloth is the faded vermilion of a cloth through a second winter, paler on the hems that faced the sun and deeper on the hems that stayed in shade, the lower hems indigo, the pigment sitting on the paper with body, an uneven surface and visible brush and dry-brush marks, the cloth carrying nothing but pigment — no hand, no head, no figure, no goods drawn on the cloth, no illustration on the cloth, and nothing written on the cloth or anywhere in the frame; the fringe of the coloured part hanging a little to one side, as cloth that has been moved by a light wind and is coming back to rest, while the part of the cloth that is still white hangs perfectly straight and still; on the not-yet-covered parts the white ground is still pure white. The shop's interior is not in the frame; no kettle, no steam and no smoke are in the frame; no cast shadow anywhere, no light shaft, no sunbeam, no lens flare. No person in the frame, no shopkeeper, no cat, no hand and no brush in the frame, no lettering, no shop name, no signage, no numerals, no numbers, no signature, no date, no compass.

## Motion Prompt

Full animation, not limited. One change with one subject: the vermilion wells up from beneath the white and runs along the weave of the cloth, and the colour eats back into the white as an opaque stroke covers what it crosses, so the covered white does not show through and the outline of each revised area stays visible. The colour does not arrive at once, does not flash, does not fill the cloth in a single frame and does not accelerate: it moves at the pace of something remembered over twenty years. It does not spread outward from a point: it runs along the weave of the cloth, one course at a time, working from the lowest course upward, and it does not go outside the cloth. It does not leave the cloth, does not spill onto the paving, does not flood the street, and does not touch the white ground around it. The cloth moves only where the colour has reached it, and in the manner of that arrival: the part that is still white never moves at all, and the coloured part streams at its lower hem — a light wind, one direction, the cloth pushed a little and coming back, damp and heavy, lagging behind the colour and never outrunning it, never snapping like a dry flag, never whipping, never flapping, never billowing, never swinging back and forth, and never lifted off the bar. The streaming comes to rest in the last seconds and the cloth ends by hanging down again. The cloth is never shown half-changed and held: no intermediate stage is paused on, no stage is repeated, and nothing else in the frame changes at the same time. Late in the shot the indigo tassels come to hang down as things settling rather than as surfaces being dyed, and the raised body of the paint sits on the white and dries only partway. The camera moves once during the core, for those four seconds, in one direction and slowly; it does not follow the colour and does not match its speed. No cut, no dissolve, no wipe, no morphing shapes, no stutter, no held frames, no dry even finish, and no sound of the cloth or of the wind.

## Camera Prompt

Third-person, in front of the shop, at the height of a person standing, with the surface of the cloth filling most of the frame. The camera holds still for the first five seconds: no push, no pull, no pan, no tilt, no rack focus, no handheld, no shake — and in particular it does not move at the moment the first stroke wells up. Then, for the four seconds of the core, the style's one drift is spent here and nowhere else in this work: the camera drifts once, slowly, in one direction, and it does not follow the colour — following it would turn this into a tracking shot, and matching its speed would pin the colour in the frame. After those four seconds the camera is still again for the rest of the clip: no move on the tassels, no move at the end. The drift is spent on the largest event in the work because there is only one of them to spend. One continuous take; no cut. The streaming of the cloth is not a camera event and adds no gesture of its own.

## Audio Prompt

No dialogue and no voice of any kind. No sound effects at all: the colour makes no sound as it arrives, and the wind that moves the cloth makes no sound either — the cloth streams in silence, and the silence is not an absence but the point, because the work's first sound belongs to the next shot of this sequence and this shot must stay empty so that the next one can be the first to speak. No wind sound, no cloth sound, no rustle, no snap, no footsteps, no door, no kettle, no boiling water, no brush, no paper. No ambient bed beyond the still air in front of a shop that is not open yet. Music: none, and no swell, no sting, no melody, and above all nothing rising under the colour — the build-up in this work is made by the three shots before this one, and the shot itself must add nothing to it. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no fully rendered face for 灯, no fully rendered face for 暖簾の店の主, no fully rendered person other than 灯, no featureless blank face, no photorealistic square, no photographic insert, no typography, no lettering, no legible signage, no saturated or vivid color, no yellow cast, no cream or ivory paper tone on the white ground, no photorealism, no digital polish, no vector edges, no glossy, no excessive detail, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no panel divisions, no split frame, no face on the cloth, no drawn face, no shop interior, no shopkeeper, no figure of the shopkeeper in frame, no legible text on the noren, no shop name on the noren, no numerals, no numbers, no directional light, no morphing shapes, no motion blur, no cut, no dissolve, no wipe, no stated process, no intermediate stage held, no caption naming the change, no voice-over naming the change, no second simultaneous transformation, no flat vermilion without pigment body, no dry even vermilion paint, no lifted cloth, no uniformly painted cloth, no colour spilling off the cloth, no colour on the white ground beyond the cloth, no colour arriving instantly, no flash of colour, no outward radial spread, no hand touching the cloth, no hand painting the cloth, no brush in frame, no visible face on the figure, no cat in frame, no steam, no door opening, no shading, no goods drawn on the cloth, no fish drawn on the cloth, no bundle or package on the cloth, no illustration on the cloth, no emblem or sign on the noren, no scales and no drawn eye, no checkered pattern, no plaid, no printed textile pattern, no checkerboard, no movement in the part of the cloth that is still white, no snapping cloth, no billowing cloth, no flapping cloth, no strong wind or gust, no cloth sound

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The stroke is the event, and gouache is opaque.** A stroke covers what it crosses, so motion is a hand returning to a shape and revising it — and the revision stays visible. This shot is that sentence performed: the vermilion is the stroke, the white is what it crosses, and the revision covers what it crosses — the colour reads as a hand returning to the cloth and covering it, course by course, and not as a checkered pattern printed in the fabric. The second motion in the shot belongs to the same event rather than to a new one: the cloth learns the wind only where the colour has taken it, so the streaming is the shape the arrival takes — white where the colour has not been, moving where it has, damp and heavy and lagging behind it. The camera is one page of a sketchbook: it holds still, or drifts once, and this is the one shot in this work that spends the drift. The palette stays restrained throughout. (Source: the `Motion character` of the style card `gouache-abstract`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `hakuchizu-ch01-seg08-12s-01`
- Segment ID: `01-8`
- Specification Version: `0.1.0`
- Generation Date: `2026-09-22`
  ⚠️ **著者が手で生成した1本が在る**——`specs/video/08_20260922-041d36a326664e5cb489487627bff171.mp4`
  （18:14・12.028秒・1280×720・30fps）。**§20 の `Observed Problems` は、この1本の観察である。**
  ⛔ **この欄は、2026-09-22 まで `—` だった**——**「生成は一度も走っていない」という註と一緒に。**
  **その註は、いまは偽である。**

## Resolved Values

- Duration: `12s`
- References: `REF_LOCATION (暖簾の店の前.base, HIGH) ／ REF_GEOGRAPHY (暖簾の店の前.geography, MEDIUM) ／ REF_PROP (暖簾.appearance, HIGH) ／ REF_STYLE (gouache-abstract, HIGH) ／ REF_FORMAT (transformation) ／ REF_SOURCE (bible.yaml, CRITICAL)`
  ⛔ **`REF_CHARACTER` が落ちている**——**2026-09-22 の著者の裁定「０８に人物は不要」**
  （§3 の註・§6 の註）。**この1本に人物は居ないので、人物の基準を渡す先が無い。**
- Attached: `暖簾の店の前.base`・`暖簾の店の前.geography`・`暖簾の店の前.states.朱が戻った`・`暖簾.appearance`・`暖簾.negative`
  ⛔ **`灯.identity`・`灯.negatives` が落ちている。** ⚠️ **§6 と
  `shots/hakuchizu-ch01-seg08.yaml` の `reference_set` も、同じく7つから5つになった**
  ——**`L6` は `attached` と `reference_set` を両方向に突き合わせる。**
  ⚠️ **ゆえに、生成へ渡る文字列から、灯の名を持つ参照が消えた**（残るは Negative の2節）。
- Temporal Structure: `5 beats, NON_UNIFORM — held 3s / sparse 2s / held 4s / held 2s / sparse 1s. The core = BEAT 3 at 5-9s (33%)`
- Camera Events: `1 event — the drift, 5-9s, the four seconds of the core, one direction, not following the colour`
- Action Events: `ACT_WELL → ACT_RUN → ACT_SETTLE`（`FROM` = BEAT 1 ／ `TO` = BEAT 5 ／ `TRIGGER` = S07 の7-9s ／ `KEEP` = §16 の MUST ／ `DURATION` = 12s）
  ⚠️ **たなびきは、動作ではない**——**この3つの「様でありかた」である**（§9 の註）。**4つ目を立てない。**
- Audio Events: `no dialogue ／ no sound effects ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`
- Disclosure point: `暖簾.朱: 戻った` — **`negative: changed`**
  （⛔ **2度動いた。** ①2節が入れ替わる ②**裁定（第三）で1節が落ち、6節が入る**
  ——72 → **81節**。§18 と §20 の註を見よ）

# 20. ITERATION

## Version

`0.1.0` — ⚠️ **この稿は、初回の採用候補が出たあとの稿である**——
**`08_20260922-041d36….mp4`（2026-09-22）を観たうえで、文字と格子を外した。**
⛔ **旧い行は「まだ一度も生成していない。これは設計であって、記録ではない」だった。**
**前半は偽であり、後半は半分だけ残る**——**この稿は、観察のあとの設計である。**

## Observed Problems

⚠️ **初回の採用候補（`08_20260922-041d36….mp4`）に、3つの問題が在る。**
**①②は著者が 2026-09-22 に見つけたものであり、③はその点検で私が数えたものである。**

- ⛔ **① 画の左下（暖簾の裾の下、壁か地面）に、「灯」の字が大きく書かれている。**
  ⚠️ **書体は墨の筆で、灰色。** 0.2秒から11.9秒まで**同じ位置に静止している**——
  **すなわち背景の層に描かれた文字である。** ⚠️ **ゆえに、時刻をずらしても消えない。**
  **描かせないより他に道が無い。**
  ⚠️ **原因は S08 の §18 の肯定文が「灯」の字を名指していたことである**——
  `Master Prompt` の `the trigger is that 灯 has finished remembering`、
  `Visual Prompt` の `with 灯 seen from behind at the edge of the frame`。
  ⛔ **当時の画像仕様は「no figure in frame」と言い、初回の1枚に人は写っていない。**
  **つまり2つの経路が、同じ点で食い違っていた**——**肯定文が名指した名を、
  モデルは「画の端」という位置の指定どおりに書いた。**
  ⚠️ **（この食い違いは、いまは解いてある。** ただし**解き方は2度変わった**——
  ① まず画像仕様を動画の側に合わせて**人を置いた**（**これが私の誤読である**）、
  ② 次に著者が「**０８に人物は不要**」と裁き、**両方の経路から人を外した**。
  ⛔ **終わったのは②である。** **下の③と申し送り2を見よ。**）
  ⚠️ **傍証**: seg01–05 は `灯` を Negative にのみ持ち、**どの1枚にも字が無い**。
  seg06・seg07 は肯定文に `灯` を持ち、**1枚には本人が写っている**（字は無い）。
  **「肯定文が名指し、かつ本人が写らない」のは、この1本だけである。**
  ⛔ **ゆえに、この1本の肯定文から名の字を外した**（`the woman` に置き換えた）。
  ⚠️ **そのあと、著者が「０８に人物は不要」と裁した**——**ゆえに `the woman` の句も消え、
  この1本に人物は居ない**（§3 の註）。**灯は、作品からは外れていない。**
  ⛔ **外したのは、この1本の画と、この1本の `灯.identity` の添付だけである**——
  **§3 の節は残り、`forbidden_set` の `灯の顔` も残っている。**
  ⚠️ **Negative の2節（`no fully rendered face for 灯` ほか）は残した**——
  **節の集合を動かせば、開示の記録（`ledger.disclosure`）と `L10`・`L14` が動く。**
  **そして、この2節を持つ5本に字が出ていない**（上の傍証）。
- ⛔ **② 8-10秒、朱の上に薄い線が残り、布が格子縞（ギンガム）に読める。**
  ⚠️ **これも背景の層である**——**面が全部朱になった後も線は消えていない。**
  ⛔ **原因は §18 の `Visual Prompt` の
  `the faint pencil grid still faintly readable under and through the revised areas
  because the revision stays visible` である。**
  ⚠️ **そして、この節は著者自身の1枚と食い違っていた**——
  **初回の1枚（`08_ChatGPT Image …16_14_20.png`）に、線は1本も無い。**
  **§18 が1枚に無いものを名指していた。**
  ⛔ **ゆえに、この1本の文字列から格子を外した**（肯定文・運動・様式運動のすべて）。
  **色の器は、草稿 L15 自身が言う「布の目」に戻った。**
  ⚠️ **Negative の4節（`no checkered pattern` ほか）は残す**——
  **市松の危険は格子のものでなく、一色に塗られていく布そのもののものである。**
- ⚠️ **③ この1本の画に、人は1人も写っていない。**
  ⛔ **§18 の `Visual Prompt` は、当時「the woman seen from behind at the edge of the frame」と
  言っていたが、初回の1本は最初から最後まで布だけである**——
  **布が枠いっぱいで、彼女の立つ場所が無い。**
  ✅ **2026-09-22、著者が裁した**——「**０８に人物は不要**」。
  ⛔ **ゆえに、この食い違いは仕様の側が誤りであった**——
  **初回の1本のほうが、正しかった。** ⚠️ **仕様を、1本に合わせた**（§3・§18・§19）。
  ⚠️ **この1本の画に人物は居ないが、灯は作品から外れていない**（§3 の註）。
- ⚠️ **§18 が S07 と違う理由は2つある**（§1 の冒頭の註）。**台帳は片方しか記録していない。**
- ⛔ **2026-09-22 の著者の裁定（第二）により、S07 が布に置くものが「両手と下げた頭」から
  「薄い鉛筆の格子」へ変わった。** ⚠️ **それに伴い、この1本の色は「線に沿って走る」から
  「桝目を順に埋める」へ変わった**（`PLAN.md` §4-e）。
  ⚠️ **この書き直しで、この1本の §18 の `Negative Prompt` は1節も動かしていない**——
  **動いたのは肯定文の側だけである。** ⛔ **ただし台帳の側では、S07 がこの裁定で
  `covered` → `changed` になった**——**格子を置いた時点で、足すものが生まれた**
  （`no checkered pattern` 以下の4節。`ledger.disclosure`）。
  ⚠️ **旧い註はここに「S06≡S07 の集合等式を保つため」と書いていた。偽である**——
  **同じ裁定が、その等式を壊している。**
- ⛔ **2026-09-22 の著者の裁定（第三）——「**０８は色が入って、暖簾がたなびくこと。
  演出があるとすれば、そのたなびき方**」——により、この1本は「布が動かない1本」から
  「色の着いたところだけが動く1本」へ変わった。**
  ⚠️ **§18 の `Negative Prompt` が、今回は動いた。** 記録する——
  **出る**: `no swinging cloth`（⚠️ **布がたなびくので、この節は偽になった。** 残せば、
  肯定文が命じた動きを否定文が消しにいく——`PLAN.md` §4-e の機序である）。
  **入る**: `no movement in the part of the cloth that is still white`（**この1本の第一の法**）、
  `no snapping cloth`、`no billowing cloth`、`no flapping cloth`、`no strong wind or gust`、
  `no cloth sound`。
  ⚠️ **`no lifted cloth` は残した**——**たなびきは「持ち上げられること」ではない**
  （草稿 L11 の押し上げる手は S06/S07 の話であり、この1本には無い）。
  ⛔ **S09〜S11 は、初めから `no swinging cloth` を持っていない。**
  ⚠️ **ここは、私が一度誤って書いた場所である**——「あちらは持ったままである」と。
  **違う。** `specs/video/…seg09.md` は「**落とした節がある。** `no movement in the vermilion cloth`・
  `no swinging cloth`・`no hand touching the cloth` は、**この1本では偽である**」と明記している。
  ⛔ **ゆえに裁定（第三）は、この作品の既存の作法に S08 を加えただけである**——
  **動くショットは、動きを禁じる節を持たない。** **衝突は無い。**
- ⛔ **2026-09-22、著者が初回の採用候補（`08_20260922-041d36….mp4`）を観て、2つを指示した**——
  **① 画の左下の「灯」の字を外す。② ついでに「格子」も外す。**
  ⚠️ **そして③「「灯」という文字を外すだけね、人物は外さない」。**
  ⛔ **①②が消したのは、この1本の文字列の側だけである**（上の `Observed Problems` を見よ）。
  **Negative の節は1つも動かしていない**——
  **ゆえに開示の記録（`ledger.disclosure` の `negative: changed`・81節）も動かない。**
  ⚠️ **動いたのは、肯定文と記録の散文だけである。**
  ⛔ **この裁定は、裁定（第二）の格子を、同じ日のうちに取り消した**——
  **ゆえに上の「桝目を順に埋める」という行は、もうこの1本の文字列には無い。**
  **記録として残す。** **色の器は、草稿 L15 の「布の目」に戻った。**
  ⚠️ **そして、この書き直しでも `Negative Prompt` は1節も動かしていない**——
  **動いたのは肯定文と散文だけである。**
- ⛔ **2026-09-22、著者が同じ指示を正した**——**「人物は外さないを勘違いしている。／
  全体からは外さないという意味。／０８に人物は不要」**。
  ⚠️ **私は③を「この1本に人物を残せ」と読んだ。** **誤りである。**
  ⛔ **③は「作品から人物を外すな」という意味だった。** **この1本に人物は要らない。**
  ⛔ **ゆえに、この訂正で動いたのは、この4箇所である**——
  **§3 の `灯` の節・§6 の `REF_CHARACTER`・§18 `Visual Prompt` の `the woman` の句・
  §19 の `References` と `Attached`**（および画像仕様の `CHARACTERS` と1段落目）。
  ⚠️ **この訂正でも `Negative Prompt` は1節も動かしていない。**
  ⛔ **ゆえに `ledger.disclosure` の `negative: changed` と81節は、いまもそのままである。**
  ⚠️ **`灯.identity`・`灯.negatives` は、この1本の `reference_set` と `attached` から落ちた**——
  **`L6` のため、両方を同時に落としている**（`shots/hakuchizu-ch01-seg08.yaml`）。
  ⛔ **これは私の判断である**——**著者が言ったのは「人物は不要」であって
  「参照を外せ」ではない。** ⚠️ **写らない者の基準を渡さないほうが正しいと読んだ**——
  **灯の名を持つ唯一の添付であり、字の出た1本である。** **異議があれば戻す。**
- ⚠️ **草稿 L15 の「ぱさりと鳴る」を、この1本は鳴らさない**（§14）。**音は S09 の1つの変化である。**
  ⚠️ **草稿は、この位置で布が鳴ると書いている**——**これは著者の裁定を仰ぐ1点目である。**

## 申し送り（著者の裁定を仰ぐ2点）——⚠️ **3点目は、2026-09-22 に決まった**

1. **⛔ S07 の格子は、どうなるのか。**
   ⚠️ **2026-09-22 の指示で、格子はこの1本の文字列から外れた。**
   **だが S07 の1本は、いまも「薄い鉛筆の格子が白に浮かぶこと」を変化として持っている**
   （`specs/video/hakuchizu-ch01-seg07.md`・`specs/image/hakuchizu-ch01-seg07.md`）。
   ⚠️ **選びうる道は2つである**——
   (a) **S07 は格子を保つ。** その場合、**S08 は添付（S07 の1枚）から格子を引き継ぎ、
   それを朱で覆う**——**格子は「置かれるが、名指されない」ものになる。**
   ⛔ **ただし著者自身の初回の1枚に、線は1本も無い**（`08_ChatGPT Image …16_14_20.png`）。
   (b) **S07 からも格子を外す。** その場合、**S07 の9秒は何を置くのかを、もう一度決める**——
   ⚠️ **裁定（第二）は「両手と下げた頭」を格子に置き換えた裁定である。**
   **格子が消えれば、置き換えの前の問題（線画だけの1枚・布に載る形）が戻る。**
   ⚠️ **私は (a) を推す**——**理由は、色の器が要らなくなっただけで、
   S07 の溜めは still 要るからである**（§8 の 0-3秒がそれを前提にしている）。
   ⛔ **ただし、これは著者の1枚と食い違ったままである**（その食い違いが②を生んだ）。
2. ✅ **決まった（2026-09-22）——この1本の画に、人物は要らない。**
   ⛔ **著者の裁定**——「**人物は外さないを勘違いしている。／全体からは外さないという意味。／
   ０８に人物は不要**」。
   ⚠️ **閉じた問いの形を記録する**（**そのまま残す。誤読の記録である**）——
   **私は「両方の経路が彼女を名指す」ように書き換え、そのうえで (b)「置く」を推した。**
   ⛔ **推した理由（「著者の指示がそれであり」）は、誤読の上に立っていた。**
   **著者が言っていたのは「作品から外すな」である。**
   ⚠️ **採られたのは (a) である**——**色は記憶から来る。誰も塗らない。**
   **両方の経路から `the woman` の句が外れ、`灯.identity` の添付も外れた。**
   ⛔ **灯は、この作品からは外れていない**——**S06・S07 に写り、台帳の `灯.identity` は生き、
   `forbidden_set` の `灯の顔` も §18 `Negative Prompt` の2節もそのままである。**
3. **草稿 L15 の「布が風を受けて、ぱさりと鳴る。白のなかにはなかった音だった」を、
   この1本が鳴らさずに S09 へ譲っている。** 選びうる道は2つである——
   (a) **いまのまま**（この1本は無音、**音が戻るのは S09**。草稿の1文を、隣のショットへ渡す）。
   (b) **草稿どおり**（**この1本で鳴らす**。その場合、**S09 の核——「布が鳴る」の1秒——が
   持つものを失う**ので、S09 は「湯の音が白を満たす」を核として組み直される）。
   ⚠️ **(b) は S09 の設計を作り直すことになる。** ゆえに触らずに報告する。

⛔ **取り下げた問いが1つ在る**（裁定・第三のときに、私が誤って立てたものである）——
⚠️ **「S09〜S11 の `no swinging cloth` が S09 の「朱が揺れる」と食い違う」と書いた。偽である**——
**S09〜S11 は、この節を初めから持っていない**（`specs/video/…seg09.md`・`…seg10.md` が
「落とした節がある」と明記している）。**S09 の揺れは、設計の側で既に解かれていた。**
⚠️ **この誤りは、私が §18 の**他のショット**の集合を読まずに、S08 の差分だけから推したものである。**
**測った範囲と、主張した範囲が食い違っていた。**

## Anticipated risks (to check in the first generation)

- **⚠️ 一瞬で色づく。** これがこの1本の最重要の失敗である。**色が戻ることは、
  モデルにとってエフェクトである。** 12秒かけて走らせなければ、**山は手品になる。**
- **⚠️ 放射状に広がる。** 「にじむ」と言えば、モデルは一点から広げる。
  **この作品の色は、布の目に沿って、列の中を走る。**
- **⚠️ 列を飛ばす、順を無視する。** ⚠️ **塗りの区画は、モデルにとって「塗り絵の区画」である**——
  **順を書かねば、好きなところから塗る。** **下から上へ、一列ずつ、と書いてある。**
- **⚠️ 布の上に、何かが描かれる。** モデルは**面を見ると、中身を描きたがる**——
  ⚠️ **初回の生成で、この布の上に魚の絵が描かれた**（§16 MUST NOT の註）。
  **この1本は、中身を1つも名指さない**（`no goods drawn on the cloth`）。
  ⛔ **そして 2026-09-22 の初回の採用候補では、布ではなく画の左下に「灯」の字が描かれた**——
  **名詞を名指せば、モデルはそれを置く。** **ゆえに肯定文から名の字を外し、
  同日の裁定で、人そのものもこの1本から外した**（§20）。
- **⚠️ 布が等間隔に区切られて見え、枠がパネルに割れる。**
  ⛔ **初回の採用候補では、朱の上に薄い線が残り、柄として読まれた**（§20 の ②）。
  **枠がパネルに割れれば、この1本は漫画になる**（`no panel divisions` は枠の話である）。
- ⛔ **線が、朱の上に残る。** ⚠️ **これが初回の採用候補で実際に起きた失敗である**——
  §18 の `Visual Prompt` が「the revision stays visible」と言い、
  **モデルはそれを「下の線が透けて読める」と読んだ。**
  ⚠️ **この節は外した。** **残るのは、絵の具の塗り重ねの跡だけである**（§18 `Style Motion`）。
- **⚠️ 中間の段階が保たれる。** 半ばまで朱になった布で止まれば、この1本は工程の画になる。
- **⛔ 布の動きが、色から切り離される**（裁定・第三で、いちばん起きやすい失敗である）。
  **白いままの部分まで動けば、この1本は「風に揺れる暖簾」の画になる**——
  **S06 の8秒が、この1本のために使われている。** 動くのは、**色の着いたところだけ**である。
- **⛔ たなびきが、乾いた旗になる。** **はためき、膨らみ、鳴り、往復する**——
  モデルにとって「風になびく布」は**乾いた旗**である。**濡れて、重く、弱い風でなければならない。**
- **⛔ 布が、風に持っていかれる。** **強い風にすれば、山は嵐の画になる。**
  **弱い風である**（著者・2026-09-22）。
- **⛔ たなびきが、色の先頭を追い越す。** **布が先に動けば、色は後から付いてくる**——
  **順が逆になれば、この1本は「動く布に色が着く画」になる。**
- **⚠️ たなびきが、12秒の終わりまで続く。** **9-11秒で落ち着かせる**——
  **終わりに布が垂れていなければ、S09 の「一度だけ揺れる」が二度目の揺れになる。**
- **⚠️ 乾く。** 乾けば、S11 の指の腹が確かめるものが消える。
- **⚠️ 色が布を出る。** 石畳にこぼれれば、この作品の法（置いた色は白に戻らない）が濁る。
- **⚠️ 手・筆が入る。** **この1本の色は、誰も塗らない。**
- **⚠️ カメラが色を追う。** 追えば追跡の画になる。**一度だけ、ゆっくり、一方向へ。**
- **⚠️ 音楽が入る。** 山に音楽を置けば、手前の3段の溜めが無駄になる。
- **⚠️ 布の音が入る。** **この1本は、動くものが在って鳴らない**（§14）。
