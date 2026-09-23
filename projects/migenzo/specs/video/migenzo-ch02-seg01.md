# ⛔ **この仕様は、② の手順7（`skills/staging/SKILL.md`）に従って §1–20 を書き終えたものである。**
#   ⚠️ **この1本は、§10 staging を先に持ち、そのあとで §1–20 を書き足したものである**
#   （著者裁定 c＝`PLAN.md` §4-c 問い10——**§10 staging ×13 → 画像仕様 ×13 → §1–20 ×13**）。
#   ⛔ **ゆえに §10 の本文は、前の稿から一字も変えていない**——**足したのは、下の4点である**
#   （「A place it is put」の名乗り／様式の側／予算／4欄の `Camera Events`）。
#
#   ⛔ **視点の答えを、ここで明記する**（`skills/staging/SKILL.md` 手順1——
#   「**Say which one this shot is.**」）。⚠️ **この1本は「A place it is put」である。**
#   ⛔ **01 は「a premise that is dropped」であり、反対側である**（`PLAN.md` §4-c 問い12——
#   01 の前の稿は、まさにこの2つを取り違えていた）。**取り違えない。**
#   ⚠️ **`time-fold` では、置かれた枠が本来の形である**——
#   「**The camera is the anchor**……**A fixed frame is the native case**」。
#
#   ⛔ **この1本は、`video-spec` 以外を名乗る4本のうちの1本である**（`PLAN.md` §0-b——**01・02・07・11 の4本**）——
#   ⚠️ **ゆえに §18 の禁制の集合は、01 とも 03 とも違う。**
#   実測（2026-09-23）——**`time-fold` の `Negative` は9節、`impossible-camera` は6節で、
#   両者は1節も共通しない**（4枚の技法カードは、互いに `no cut` の1節だけを共有する）。
#   ⚠️ **この移動は台帳に書いてある**——`ledger.disclosure` の3本目
#   （`migenzo-ch03-seg01`）が `negative: changed` である（訂正、同日、著者裁定＝問い13）。
#   ⛔ **02 は変化点を持たない**（`ledger.disclosure` の註——**二十年は状態の継続である**）。
#
#   ⛔ **この1本の形式変数は `time-fold` が決める**——`PLACE`＝暗室／`PASSES`＝二十年／
#   `SURVIVOR`＝この部屋の状態（現像トレイと赤い安全光）／`RANGE`＝二十年／`DURATION`＝9s。
#   ⚠️ **§6 に置き、§8 と §18 が使う。**
#
#   ⚠️ **§10 と §18 を同じ手が書いている**——**理由が §18 まで運ばれるためである**
#   （`skills/staging/SKILL.md`——**「A prohibition with no reason is not a decision — it is a habit.」**）。

# ═══ 演出要約 ════════════════════════════════════
# 『未現像』第2章「見ないことの記録者」 / モンタージュ / motion —— 二十年が、この部屋を通り過ぎる
#
#   壁に、薄い影がひとつ。二十年前と同じ高さ、同じ向きである。
#   影だけが濃さを増し、9秒の終わりに、それは彼女の体より少し重い。
#   トレイと安全光は、1フレームも変わらない。切らない。視点は動かない。誰も出ない。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 未現像 第2章「見ないことの記録者」 Clip 2/13 / 9s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**
⚠️ **§18 の文字列は英語である**（`CLAUDE.md`「Things That Must Not Be Broken」）。**訳してはならない。**
⚠️ **この仕様は画像仕様と対である**（`specs/image/migenzo-ch02-seg01.md`）。**両者は別のものを指す**
——動画は §1–20 を持ち、画像は7欄と `Negative` を持つ（`L18`）。

⛔ **この1本には、変化がない。** ⚠️ **変わるのは影の濃さだけであり、それは出来事ではない**——
**二十年が、この部屋を通り過ぎること**である。⛔ **この1本が観客に渡すのは「何かが変わった」ではなく
「変わらないまま過ぎた」である**（`shots/migenzo-ch02-seg01.yaml`）。
⚠️ **変化点を持たないショットが1本在ることは、抜けではなく設計である**（`ledger.disclosure`）。
⛔ **ゆえに、この1本に「何か」を足してはならない**——**足せば、この1本は別の1本になる。**

---

# 1. VIDEO

- Duration: `9s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take, with no cut in it. A single change: the shadow of a woman on the darkroom wall grows heavier over twenty years, while the developer tray and the red safelight do not change at all.

# 2. WORLD

## World Concept

撮られなかった瞬間は、あらゆる可能な像を無限に含む重ね合わせとして保存される。
現像とは、その無限を一つの像へ崩壊させる喪失の行為である。
見ることは可能態を殺し、見ないことは可能態を無限に生かしつつ永久に留置する。

⚠️ **この段落は `bible.world.concept` の逐語である**（出典は `構想/world.md`「世界の核」）。
**要約しない。**（⚠️ **この1本は、この段落が画面で実演される1本ではない**——**下の「使わない法」を見よ**。）

## World Rules

- **「脂痕——現像の代償が、レンズの指紋・手の脂として像に残る。」**
  ⚠️ **この1本が示すのは、この法の蓄積である**——`draft_02-4`
  「何度も何度も、像の上に脂を置いてきた。**そのぶんだけ影が濃くなっていく**」。
  ⛔ **脂痕そのものは、この1本の画面に無い。** **在るのは、その重さだけである。**
- **「現像のたび、現像者は自身の可能態を一つ崩壊させる」**——⚠️ **影の重さの原因である。**
  ⛔ **だが、この法もまた、画面で説明されない。**
- **「暗室は、内と外を区別していない場所である。」** 単一光源。現像トレイの液面は、**スクリーン内スクリーン**。
  ⚠️ **この1本の壁は、その法の見える面である**——⛔ **外へ通じる戸口は、枠に入らない**（§4）。
- **「奇跡は、一度も起こらない。」** ⚠️ **この1本では、「何も起こらないこと」がそれである。**
- ⛔ **この1本が使わない法を、明記する**（使わなければ、モデルは13本ぶんの法を1本に詰める）——
  「像は、ネガの重ね合わせとして待機する」（**01 が使う**）／
  「遮光は、シャッターを降ろすことと等価である」（**10・11 が使う**）／
  「落とせるのは、直前に色を持っていた具体的な何かだけである」（**11 が使う**）／
  「一度も重ね合わせでなかったものは、現像できない」（**10・13 が使う**）。

## Visual Language

- Art Direction: The palette fixed: the red of the safelight, the amber of the developer, the white of the unexposed paper, and the near-black of the surrounding room, the red and amber kept to their sources and never staining the whole frame. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, blown highlights on the white paper, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness.
  ⚠️ **この段落は `bible.world.visual_language.art_direction` の逐語である**（著者自身の英語）。
  **要約しない。§15 と §18 `Visual Prompt` にも同じ一字で貼る**——独立した生成は記憶を共有しない。
  ⚠️ **この1本では、白（銀塩の白）が画面の主題ではない**——**パレットは同じでも、占める面積が違う。**
- Light: A single light source, and no time of day. The dim red safelight and the warm amber glow of the developer tray are not a direction and not an hour — they are the room's constant state. No window, no clock, no daylight, no directional light.（`bible.world.visual_language.light` の逐語）
  ⛔ **様式カードの `available natural light` を写さない**——**この部屋の赤い安全光は到着しない。**
  ⚠️ **そして、この1本はその光を主題にしない**——**影を落としているのが、その光である**（§13）。
- Color Language: **3色と、ほぼ黒。** 赤は安全光、琥珀は現像液、白は銀塩の白——
  ⚠️ **この1本で面を占めるのは、ほぼ黒と、その上の影である。**
  ⛔ **赤と琥珀は、その出所に留まる。**
- Texture: フィルム粒。**影は、壁の粗さを持つ**——滑らかな影にしない。
- Rendering: **影は「濃くなる」のであって、「伸びる」のでも「動く」のでもない。**
- Visual Density: **低い。** 画面に在るのは、壁と、影と、トレイの液面と、赤い光だけである。
- Time: 時刻を持たない（**そして、この1本は二十年を持つ**——§8）
- Atmosphere: 二十年が通り過ぎた部屋の、動かない空気。**埃も無い。**

# 3. SUBJECTS

## 壁の影（the shadow）

- Reference: 無し——⛔ **`絹.identity` では固定できない**（**影は設定画ではない**。
  `shots/migenzo-ch02-seg01.yaml` の申し送り）。**ゆえに、形は言葉で書く**（§18 `Visual Prompt`）。
- Appearance: **薄い影がひとつ。** 絹の輪郭をなぞっていて、それ以上のものではない。
  ⚠️ **形は、二十年、同じである**——同じ高さ、同じ向き、同じ立ちかた（`draft_02-1`
  「二十年、おなじ高さに、おなじ向きで吊るしてきた」）。
- Behavior: **濃さを増す。連続で。速くならない。** ⚠️ **形は変わらない**——**変わるのは重さだけである。**
  `draft_02-4`「影の指先が、絹の指先より、すこし、重い」。
- Continuity Requirements: ⛔ **この9秒のあいだ、影は動かない**——
  `draft_02-4` の「影の指が独りでに動く」は**第2章の後半の出来事**であり、この1本の変化ではない。
  ⛔ **そして影は、2つ目の survivor ではない**——**影は、この1本で唯一変わるものである。**

## 現像トレイと液面（the tray）

- Reference: `暗室.base`（**アートボードに含まれる**——`ledger.locations.暗室.base` の註）。
- Appearance: **琥珀の液面。静止している。** ⚠️ **この1本のトレイには、印画紙が無い**（§5）。
- Behavior: **9秒のあいだ、1フレームも変わらない。**
- Continuity Requirements: ⛔ **これが survivor の1つ目である**——
  **変わらないから、影の濃さが「経過」として読める**（`time-fold`）。

## 赤い安全光（the safelight）

- Reference: `暗室.base`。
- Appearance: **上の光源。** 赤い。⚠️ **壁の影を落としているのは、この光である。**
- Behavior: **動かない。** ⚠️ **光は、方向ではなく状態である**（`bible.constants.光`）——**動かないのは、それが状態だからである。**
- Continuity Requirements: ⛔ **これが survivor の2つ目である。**
  ⛔ **そして、光源そのものは枠に入らない**（§16）——**在るのは、光が届いている面である。**

## 絹の体（the body）

- ⛔ **この1本の画面に無い。** ⚠️ **影を落としている体は、枠の外に立っている。**
- ⚠️ **これは判断であり、書き落としではない**（`shots/migenzo-ch02-seg01.yaml`）——
  ⛔ **老けない体を枠に置けば、20年を畳んだ画のなかに「一度も老けない女」が立つ**
  （**依頼の「誤解させない」に、これが最も反する**）。
  ⚠️ **そして、カードの `avoid` が禁じるのは加齢の手段であって、加齢を描かないことではない**——
  **描かないことが「変わらない人」に見えるなら、その画は間違って見える。**
- Continuity Requirements: ⛔ **それでも、絹がこの1本に居ないことは「絹が要らない」ではない**——
  **影は絹の影であり、彼女の体の形をしている**（§18 `Visual Prompt` が、その形を肯定で書く）。

# 4. ENVIRONMENT

- Location: `暗室`（`ledger.locations`）——⛔ **`最後の暗室` ではない。** この1本は、仕事の暗室である。
- Environment Elements: **影を受ける壁**、現像トレイと液面、赤い安全光。
  ⛔ **窓も、時計も、戸口も、引き出しも、瓶も、道具も無い**（§16）。
- Environmental Behavior: **何も動かない。** 液面は静止し、安全光は動かない——
  ⚠️ **この1本の画面で進むのは、影の濃さだけである。**
- ⚠️ **この部屋の地理は `ledger.locations.暗室.geography` が持つ**——
  **中央にトレイ（液面）、上に赤い安全光、一方の壁に引き出し、そして戸口。**
  ⛔ **この1本の枠に入るのは、そのうちトレイと安全光である。**
  ⚠️ **戸口は入らない**——**外は、この画の外に無い**（`world.md`——**内と外を区別していない場所**）。
  ⛔ **そして影を受けるのは、引き出しの無い側の壁である**——**これは判断である。**
  **引き出しを枠に入れれば、この1本に4の主題（空の引き出し）が混ざる**（1ショット1変化）。

# 5. OBJECTS

- 現像トレイと液面 — **9秒のあいだ、1フレームも変わらない。** ⛔ **この1本の survivor である。**
  ⛔ **そして、この1本のトレイは空である**——**印画紙が無い。**
  ⚠️ **理由は2つある。** **（1）** 01 の終わりに、絹は紙を液から引き上げている——
  **ゆえに、この1本の始まりに紙は無い**（連続性）。**（2）**
  **紙を置けば、「これから何かが現像される」という予告になる**——⛔ **この1本は何も予告しない。**
  ⚠️ **（1）の出所**（2026-09-23、著者裁定「**残す＋出所を記録**」で、ここに書いた）——
  `specs/video/migenzo-ch01-seg01.md` §9 `ACT_LIFT` の After
  「**紙は液から出ており、脂痕が像の上に残っている。**」／
  `shots/migenzo-ch01-seg01.yaml` の `beats` `7-10s`
  「**絹が紙の縁をつまんで引き上げる。**」。
  ⛔ **ゆえに、この1本の空のトレイは、前のショットが作った状態である**——
  **`暗室.base` の「一枚」を否定しているのではなく、01 の結末を受け取っている。**
  ⚠️ **（2）は、② の読みである**（**出所は見つかっていない**、2026-09-23 の走査）——
  **ゆえに、この1本を縛るのは（1）であり、（2）ではない。**
  ⚠️ **そして、07・10 との型の違いはここである**——あの2本は出所の無い読みで
  **台帳の base を打ち消していた**（2026-09-23 の裁定で肯定形へ揃えた）。
  ⛔ **この1本は、base ではなく、直前のショットに従っている。**
- 赤い安全光 — **状態である。** ⚠️ **光源そのものは枠に入らない**（§16）。
- ⛔ **印画紙・未露光のフィルム・脂痕・トング・瓶・引き出し・レンズ** — **どれも、この1本には無い。**
  ⚠️ **無いことは、まだ書いていないことであると同時に、この1本に出さないことである**（§16）。

# 6. REFERENCES

- REF_LOCATION: `暗室` (HIGH — `migenzo-art-board` が基準である)
- REF_GEOGRAPHY: `暗室.geography` (MEDIUM — 位置関係は4点。**この1本は「壁」と「トレイ」の2点を使う**)
- REF_STYLE: `documentary-photo` (HIGH)
- REF_FORMAT: `time-fold` (HIGH — **この1本の文法である**。⛔ **`video-spec` 以外を名乗る4本のひとつ**（`PLAN.md` §0-b——**01・02・07・11**）)
  - ⚠️ **カードの形式変数は5つである**（`references/formats/time-fold.md`）——
    `PLACE`＝**暗室**／`PASSES`＝**二十年**／`SURVIVOR`＝**この部屋の状態（現像トレイと赤い安全光）**／
    `RANGE`＝**二十年**／`DURATION`＝**9s**。
    ⛔ **`DURATION` は尺であって、`RANGE` ではない**——**畳まれる側と、畳む側である。**
    ⚠️ **カードは `SURVIVOR` を1つ要求する**——**この1本の survivor は「この部屋の状態」という1つである。**
    その見える形が、トレイと安全光である（§10 `Camera Behavior`）。
- REF_CHARACTER: ⛔ **無し。** ⚠️ **この1本に、人物の鍵は要らない**——
  **絹の体は枠に入らず、影は設定画では固定できない**（§3）。
  ⚠️ **画像仕様と記録が、ここで一致している**（`specs/image/migenzo-ch02-seg01.md` の
  「⛔ **人物の設定画は要らない**」／`shots/migenzo-ch02-seg01.yaml` の「⛔ **人物の鍵を、ここに置かない。**」）
  ——⛔ **01 と違い、ここに食い違いは無い。**
- REF_SOURCE: `projects/migenzo/bible.yaml` (CRITICAL)
- REF_LEDGER: `projects/migenzo/ledger.yaml` (CRITICAL — ⚠️ **この1本は開示の変化点を持たない**)

# 7. NARRATIVE

- Core Event: **無し。** ⚠️ **起きることは、影が重くなることだけである**——
  `draft_02-4`「失くしたものは、消えたのではなく、**ここに影の色になって積もっていた**」。
- Beginning: **薄い影が、彼女の輪郭をなぞっている。** ⚠️ **この3秒は「いま」である。**
- Turn: **濃さが、連続で増える。** ⛔ **段が無い**——**段を置けば、それは「何かが起きた」になる。**
- Peak: **影は、絹の体より重い。** ⚠️ **それだけが、二十年である。**
- Pull: **変わらないものが2つ、変わったものと同じ枠に在る。** ⛔ **この1本は、何も決めずに終わる。**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-3s` — density: `held` — 暗室。上に赤い安全光、下に現像トレイの琥珀の液面、
    **壁に薄い影。** ⚠️ **この3秒は「いま」である**——影は、輪郭をなぞっているだけである。
    ⛔ **ここで何も予告しない。** `draft_02-1`「二十年、おなじ高さに、おなじ向きで吊るしてきた」——
    **同じであることが、この前半の内容である。**
  - BEAT 2 `3-6s` — density: `transition` — **二十年が、この枠を通り過ぎる。**
    **影が濃さを増していく。** ⚠️ **カットしない。** 濃さは連続である——**途中に段を置かない。**
    `draft_02-4`「何度も何度も、像の上に脂を置いてきた。**そのぶんだけ影が濃くなっていく**」。
  - BEAT 3 `6-9s` — density: `held` — **影は、絹の体より重い。** それだけが二十年である。
    ⚠️ **トレイも安全光も、9秒前と1フレームも変わっていない。**
    ⛔ **ここで影を動かさない**（§3）。
- Temporal Density: ⛔ **二十年は、9秒に均等に配られていない**——**畳まれる側が、偏っている。**
  ⚠️ **`RANGE`（二十年）が着地するのは 3-6s である**（`time-fold`「**Uneven duration.**」——
  「**The seconds are not spread evenly over the span; choose the part of the passage the shot lingers on.**」）。
  **この1本が留まるのは、「いま」（0-3s）と、「重さ」（6-9s）である。**
  ⛔ **だが、動きの速さは変えない**——**濃さは、9秒のあいだ同じ速さで増える**（§11）。
  ⚠️ **速さを変えれば、それは「急に何かが起きた」であり、この1本の内容ではない。**
- ⛔ **`coexisting-realities` と取り違えない**（カードの註）——
  **この1本は、2つの時代を並べない。** **時間は、一つの部屋を、順に通り過ぎる。**

# 9. ACTION

- `ACT_HOLD` — Before: トレイと安全光が、そこにある。After: **同じ位置に、同じ明るさで、ある。**
  Simultaneous With: `ACT_DEEPEN`。Causes: 無し。
  ⛔ **これが、この1本の survivor である**——**この9秒で、この2つは1フレームも変わらない。**
- `ACT_DEEPEN` — Before: 影は薄く、輪郭をなぞっている。After: **影は、絹の体より少し重い。**
  Simultaneous With: `ACT_HOLD`。Causes: **二十年のあいだに積もった代償**——
  ⚠️ **だが、この1本は原因を画面に出さない**（§2）。**出るのは、重さだけである。**
  ⛔ **段が無い。** ⛔ **形は変わらない**——**変わるのは濃さだけである。**
- ⛔ **能動の動作を、この1本に置かない**——**誰も画面に居ない**（§3）。

# 10. CAMERA

- Camera Language: 三人称。**暗室で立っている人の眼の高さ。**
  ⚠️ **枠の上半分は壁であり、そこに影がある。** 下半分に、現像トレイの琥珀の液面と、
  赤い安全光。⛔ **この1本の主題は影であって、絹ではない**（**彼女の体は枠に入らない**）。
  ⚠️ **据えられた一台である。** ⛔ **`time-fold` の文法が、動く余地そのものを消している**——
  「**A fixed frame is the native case**」。**ゆえに、この1本の保持は辞退ではない**——
  **文法が定めた位置である。**
- Camera Language（問いの答え）: ⛔ **この1本は「A place it is put」である。**
  ⚠️ **`skills/staging/SKILL.md` は2つの答えを並べ、「Say which one this shot is.」と言う**——
  「**"A place it is put"**」と「**"a premise that is dropped"**」。
  ⛔ **カメラは、この部屋に据えられている**——**前提が落ちているのではない**（それは 01 である）。
  ⚠️ **`time-fold` の `ENTRY` は、固定枠そのものである**——**置かれた位置が、この文法の内容である。**
- Camera Language（様式の側）: ⚠️ **様式 `documentary-photo` の法**——
  「**The camera stands and watches, at eye level.** It holds; **if it moves at all it moves
  to keep the subject in frame, never to make a point.**」そして「**Stillness is fully available.**」
  ⛔ **この1本は、様式の許す唯一の身振りを、要らないものとして持たない**——
  **影は枠の内側にあり、追うものが無い**（下の「予算」）。
- Camera Language（予算）: ⚠️ **様式はカメラを所有し、形式はそれを狭めてよい**——
  **だが、反転させてはならない**（`skills/staging/SKILL.md`）。
  ⛔ **この1本に要るのは「使わない」ではなく「要らない」である**——
  **枠が既に、変わるものを1つだけ含んでいる。** 動けば、**畳んだ時間が「移動」になる**。
  ⚠️ **辞退は辞退として書く**——**§18 に、そのまま運ぶ**（下の `Camera Prompt`）。
- Camera Events: `0-9s` none——**壁の影に留まる。**
  ⚠️ **この9秒は、1つの保持である**——**畳まれた時間のなかに、切れ目を置かない。**
  ⛔ **カットも、ディゾルブも、段も無い**（カードの `Negative`——
  `no cut, no time-skip, no cross-dissolve`）。
  ⚠️ **保持は「書かないこと」ではない**（`skills/staging/SKILL.md` 手順5）——
  **4つの欄で書く。**
  - **`0-3s`** — 動き: **無し。** 対象: **壁の影。** 速さ: **—**（動かない）。
    ⚠️ **この保持が使われるのは、入口を述べることである**——
    **同じ高さ・同じ向きの影であることが、この1本の始まりの陳述である**（§8）。
  - **`3-6s`** — 動き: **無し。** 対象: **壁の影。** 速さ: **—**（動かない）。
    ⚠️ **この保持が使われるのは、二十年を通すことである**——**変わるのは影の濃さだけであり、
    枠は動かない。** ⛔ **動けば、畳まれた時間が「移動」になる。**
  - **`6-9s`** — 動き: **無し。** 対象: **壁の影。** 速さ: **—**（動かない）。
    ⚠️ **この保持が使われるのは、重さを着地させることである**——
    **トレイと安全光が9秒前と同一であることが、その尺度である**（§8）。
- Camera Behavior: **動かない。** ⚠️ **理由は2つあり、2つめがこの1本に固有である。**
  **（1）文法**——固定枠が `time-fold` の本来の形である（上）。
  **（2）survivor**——⚠️ **カードは「One survivor」を要求する**——
  「**Something in the frame does not change across the whole span — that is what makes
  the passage legible as time. Name it.**」
  ⛔ **カメラが動けば、9秒のあいだ変わらないものが2つになる**（トレイと安全光、そしてカメラ）。
  **survivor が2つ在れば、どちらが時間を証しているのか読めない。**
  ⚠️ **ゆえに、この1本で動かないのは、カメラと、トレイと、安全光である**——
  **変わってよいのは、影の濃さだけである。**
  ⚠️ **辞退は辞退として書く**（`skills/staging/SKILL.md`）——**§18 に、そのまま運ぶ。**

# 11. MOTION

## Subject Motion

**影の濃さが、増す。連続で。速くならない。** ⛔ **形は変わらない**——**影は、絹のままである。**
⚠️ **変わるのは、重さだけである。** `draft_02-4`「影の指先が、絹の指先より、すこし、重い」。
⛔ **動きとして見せない**——**ドリフトも、モーフィングも、伸びも無い。**
⚠️ **この9秒に、出来事は1つも無い。** **あるのは、積もることが続いていることだけである。**

## Object Motion

**トレイも、安全光も、動かない。** ⚠️ **液面は静止している**——波ひとつ無し。雫も無い。
⛔ **この2つが動けば、この1本は「時間が止まった部屋」ではなくなる**（§10）。

## Environmental Motion

**空気は動かない。埃も無い。** ⚠️ **この部屋の画面で進むのは、
赤い安全光が壁に落としているものの濃さだけである。**

## Physical Characteristics

- Weight: **影が、重くなる。** ⚠️ **影は物ではない**——**だが、この1本では、重さが量である。**
- Inertia: **積もりは、途中で止まらない。** 速くならないが、**戻りもしない。**
- Acceleration: **無い。** ⛔ **この1本に、加速は1つも無い**——
  **`held` と `transition` の差は、動きの速さではなく、畳まれている時間の量である**（§8）。
- Fluidity: **液は流れない。** ⛔ **影は、にじまない**——**輪郭は、9秒のあいだ保たれる。**
- Impact: **無い。** ⛔ **この1本は、何も起きないことが出来事である**——衝突も、打撃も、無い。

# 12. EMOTION

- Emotional Arc: **同じ**（0-3s）→ **積もっている**（3-6s）→ **重い**（6-9s）。
  ⛔ **この1本は、感情を立てない。** ⚠️ **絹の感情は画に出ない**——**体が枠の外だからである**（§3）。
  **出るのは、重さだけである。**
- Emotional Events: **無し。** ⛔ **「影が濃くなった瞬間」を置かない**——
  **置けば、それは「何かが起きた」であり、この1本の内容ではなくなる**（§7）。
  ⚠️ **この1本が観客に渡すのは、感情ではなく、経過の長さである。**

# 13. LIGHTING

- Base Lighting: **赤い安全光と、琥珀の現像液の灯。** ⛔ **方向を持たない、時刻を持たない**——
  「A single light source, and no time of day. …… they are the room's constant state.
  No window, no clock, no daylight, no directional light.」（`bible.world.visual_language.light`）
  ⚠️ **光は、方向ではなく状態である**（`bible.constants.光`）——**ゆえに `Lighting Events` は無しである。**
  ⚠️ **そして、この1本では、その光が影を落としている**——**壁の影は、赤い安全光の産物である。**
- Lighting Events: **無し。** ⛔ **この9秒で、光は一度も動かない。**
  ⚠️ **影が濃くなることは、光の変化ではない**——**光は同じままで、積もっている。**

# 14. AUDIO

- Dialogue: **無し。** **この作品は、台詞もナレーションも持たない**（`PLAN.md` §0-f）。
- Sound Effects: **無し。** ⚠️ **この1本には、そもそも出来事が1つも無い**——
  ⛔ **生成器に音を求めない**（`PLAN.md` §0-f——**出力のクリップの音声は全て捨て、
  BGM は著者が最後に被せる**）。
- Music: **無し。** **BGM は、この作品の床で禁じられている**（§16）。
- Environment: **無し。** ⚠️ **暗室は音を持つ場所である**（液・フィルム・部屋の低い音）——
  ⛔ **それでも、この経路には求めない。** **求めなければ、床が守る。**
- **Language: Japanese.** ⚠️ **発話は無いが、宣言する**——「**空欄は中立ではない**」
  （`bible.language` の註。実測: 発話のある動画に中国語の字幕が焼かれた）。
  **話さないことと、言語を持たないことは違う。**

# 15. CONTINUITY

## Identity Lock（逐語——要約しない）

The palette fixed: the red of the safelight, the amber of the developer, the white of the unexposed paper, and the near-black of the surrounding room, the red and amber kept to their sources and never staining the whole frame. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, blown highlights on the white paper, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness.

- Identity: ⛔ **この1本に、人物の同一性は要らない**（§6）——
  ⚠️ **影は `絹.identity` では固定できない。それでも影は、彼女の体の形をしている**——
  **ゆえに、形は §18 `Visual Prompt` の肯定の側が書く**（同じ高さ、同じ向き、同じ立ちかた）。
  ⛔ **そして、絹の体は枠に入らない。**
- Spatial: **暗室は、1つの場所である。** ⛔ **この1本は、暗室を出ない**——
  **そして、外へ通じる戸口も枠に入らない**（§4）。
- Temporal: **時刻を持たない。** ⚠️ **この9秒は、連続した二十年である**——切れ目が無い（`time-fold`）。
- Visual: **影は、壁の粗さを持つ、ふつうの影である**——⛔ **演出の影ではない。**
  ⛔ **赤と琥珀は、その出所に留まる。**
- Motion: **動くのは、影の濃さだけである。** ⛔ **視点も、光も、液も、形も動かない。**
- Sound: **無音。**

# 16. CONSTRAINTS

## MUST NOT

- **No person. No figure. No body. No face in the room.**
  ⛔ **影を落としている体は、枠の外に立っている。**
- **No second shadow. No two shadows. No shadow of a second person. No silhouette of a child.**
  ⚠️ **この枠に在る影は、ひとつだけである。**
- **No moving shadow. No step in the shadow. No event of any kind.**
  ⛔ **この9秒に、出来事は1つも無い。** ⛔ **段を置けば、「何かが起きた」になる**（§8）。
- **No long dramatic shadow with hard edges. No dramatic mood lighting.**
  ⚠️ **この部屋の影は、赤い安全光が壁に落とす、ふつうの影である**（§13）。
- **No shadow of a hand raised. No hand in frame. No small hand pressing the lens.
  No child's hand of any kind.**
  ⛔ **`no small hand pressing the lens` は 01〜10 の10本が負う床である**（`PLAN.md` §2）。
  **11 で落ちる。**
- **No cut. No time-skip. No cross-dissolve. No return to the place after leaving it.**
  ⛔ **`time-fold` が要求する**——**1つの枠で、二十年を通す**（§10）。
- **No date stamp. No caption. No title card carrying elapsed time. No numbers of any kind.**
  ⛔ **「二十年」は、数字として画面に出せない**（`ledger.characters.絹` の註）。
- **No aging makeup. No prosthetic. No stated "years later".**
  ⛔ **カードが禁じる加齢の手段である。**
  ⚠️ **そして、この1本には老けるものが1つも無い**——**絹の体は枠に入らない**（問い9、§3）。
- **No lamp, no bulb, no bare light source, no cast shadow with a visible light source in frame.**
  ⚠️ **光は在るが、光源は枠に入らない。**
- **No window light, no sunbeam, no dust in the air.**
- **No ripple on the liquid. No drop falling. No bubbles, no foam.**
- **No print in the tray. No film in the tray. No tongs. No open drawer. No bottles or jars.
  No enlarger.**
  ⚠️ **この1本の画面に在ってよいものは、壁と、影と、トレイの液面と、赤い光である**（§5）。
- **No clock on the wall. No calendar. No mirror. No poster or picture on the wall.
  No pipes, no cables.**
- **No glossy floor. No stainless steel. No clean modern darkroom.**
- **No portrait lighting. No bright evenly lit room.** ⛔ **光は、状態であって照明ではない。**
- **No lettering, no readable text.**

## MUST

- **影は、薄いところから重いところへ、連続で進む。** ⛔ **段を置かない。**
- **影の形は変わらない。** 輪郭は、絹のままである。⚠️ **変わるのは、濃さだけである。**
- **トレイと安全光は、9秒のあいだ1フレームも変わらない**（survivor）。
- **影を落としているのは、赤い安全光である。** ⚠️ **この部屋の、恒常の状態である。**
- **この1本の位置が、最初から最後まで同じであることを、最初の3秒で述べる**——
  ⛔ **その3秒は、静止である**（§8・§10）。
- **Full animation, not limited** —— **影は、9秒のあいだ、増えつづける。**

## PREFER

- 0-3s が、**「いま」**として読めること——**同じであることが、この前半の内容である。**
- 6-9s の影が、**「重い」**として読めること——⛔ **「濃い」ではなく「重い」である。**
- トレイと安全光の不変が、**経過の尺度**として読めること（`time-fold`）。

## ALLOW

- 影の縁が、**壁の粗さのぶんだけ**、わずかに揺らいでいること——⚠️ **動きではなく、質感である。**
- 液面が、**鏡にならない程度に**、光を返すこと。

# 17. GENERATION PRIORITIES

1. **影が動く1本にしない。** ⛔ **これが、この1本の最も起きやすい失敗である**——
   ⚠️ `draft_02-4` の「影の指が独りでに動く」は、**第2章の後半の出来事**である。
   **動かせば「異常が起きた」1本になり、この1本は「何も起きなかった」1本でなくなる。**
2. **カットを入れない。** ⛔ **切れば、二十年は「2つの状態」になる**（`time-fold`）。
3. **誰も枠に入れない。** ⛔ **影を落としている体まで撮れば、この1本は「女の1本」になる**——
   ⚠️ **そして、20年を畳んだ画のなかに、一度も老けない女が立つ。**
   **依頼の「誤解させない」に、これが最も反する。**
4. **「二十年」を数字で出さない。** 日付も、字幕も、タイトルカードも、暦も。
5. **濃さに段を置かない。** ⛔ **段は「何かが起きた」である。** **連続で、同じ速さで。**
6. **光源を枠に入れない。** 赤い光は在るが、ランプは無い（§13）。
7. **トレイに紙を置かない。** ⛔ **紙は予告になる**（§5）。
8. その他すべて。

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 9-second continuous cinematic take (16:9) of twenty years passing through one room, one clip, with no cut anywhere in it. Beats, deliberately uneven: [0-3s] held — the darkroom as it is today, the red safelight above, the amber liquid of the developer tray lying still below, and on the wall a thin shadow that only traces the outline of the woman who casts it, standing at the same height and facing the same way she has for twenty years; [3-6s] transition — the twenty years pass through the frame and the shadow thickens, continuously, at the same rate from the first second to the last, with no step in it, no event, and no one crossing the frame; [6-9s] held — the shadow is now a little heavier than the body that casts it, the fingertips a little fuller than fingertips are, and that is the whole of the twenty years. The camera does not move for a single frame of the nine seconds, and it never cuts away or comes back: the frame is the container and not the traveller, so this place is never left and a return is not available to it. The thing that does not change across the whole span is named and held constant — the developer tray and the red safelight, which are the room's own state — and it is what makes the passage read as time rather than as several unrelated states. Twenty years are spent unevenly across the nine seconds: they land in the middle three, and the first and last three are the room holding still. The woman whose shadow this is never enters the frame; the person who casts it stands outside it. No date, no caption, no number and no title card appears anywhere, and no age is shown: the span is carried by the shadow alone, and the shape of the shadow does not change — only its weight. Ends on the heavier shadow with the tray and the safelight exactly as they were in the first second, and the clip ends there, without a resolving beat.

## Visual Prompt

The palette fixed: the red of the safelight, the amber of the developer, the white of the unexposed paper, and the near-black of the surrounding room, the red and amber kept to their sources and never staining the whole frame. Heavy film grain, shallow depth of field, slight motion blur, imperfect handheld focus, blown highlights on the white paper, low contrast, faded warm Kodak Portra 400 and Fujifilm Superia color tones, 35mm documentary snapshot feel, nostalgic family-photo warmth against an unsettling stillness. A single light source, and no time of day: the dim red safelight and the warm amber glow of the developer tray are not a direction and not an hour, and there is no window, no clock, no daylight and no directional light. The darkroom of the art board: one windowless room, its wall taking the upper part of the frame, everything past the red light's reach sunk in near-black, and lower in the frame the developer tray with its amber liquid lying still and empty — no print in it, no film in it. The wall is the wall with no drawer in it, and the safelight above is what lays the shadow: a woman's shadow, thin, a quiet standing silhouette, the shape of a person who has stood in the same place at the same height facing the same way for twenty years, and it lies a little heavier than the woman it belongs to, the fingertips of the shadow a little fuller than fingertips are, as though the shape had gathered weight without changing its outline. Her body and her face are not in the frame; only what the light does with her is, and the person who casts it stands outside the frame. The light source itself is not in the frame. The room is otherwise still: no dust, no ripple on the liquid, nothing moving but the density of the shadow. No typography anywhere in the frame, no clock on the wall and no calendar on it.

## Motion Prompt

Full animation, not limited. The subject is the density of the shadow on the wall, and the shadow does not travel: it stays exactly where it is and its outline does not change, and what increases is its weight — continuously, at the same rate across the whole clip, with no step, no jump and no moment where something begins. The nine seconds are a single hold: the frame does not cut, does not dissolve, does not skip time and never leaves the place and returns to it. The developer tray and the red safelight do not move at all for the entire clip — not their position, not their brightness, not the liquid's surface — because they are the thing that measures the passage. Nothing else in the frame moves: no dust in the air, no ripple, no drop, no person entering, no second shadow, no drift and no morphing of the shadow's shape. The hands of the shadow are not raised and never act on their own. The twenty years are spent unevenly — they land in the middle three seconds — and the rate of the change stays even throughout. No date stamp, no caption, no title card carrying elapsed time, no aging and no years-later staging. One continuous take; no cut, no time-skip, no cross-dissolve.

## Camera Prompt

Third-person, at the height of a person standing in the room, the wall filling the upper part of the frame and the developer tray with its amber surface and the red safelight in the lower part. The camera is the anchor of the shot and does not change position at any point in the nine seconds: no push, no pull, no pan, no tilt, no rack focus, no handheld, no shake. [0-3s] holding on the wall and the thin shadow as it is today, which states the shot's fixed position — the frame is a place this camera is put, and the place is never left. [3-6s] still holding as the shadow thickens across the span, with no cut and no change of position to mark the passage. [6-9s] still holding on the heavier shadow, with the tray and the safelight exactly as they were in the first second; this is where the shot arrives, on the weight, and not on a movement. The tray and the safelight are the things that do not change across this span, and they have to stay exactly as they are so that the shadow reads as time rather than as an effect — a camera that drifted would make a second thing that never changes, and the span would stop being legible as a span. The style permits the camera to move to keep the subject in frame; this shot spends none of it, and this shot's form makes the fixed frame the native case. One continuous take; no cut, no time-skip, no cross-dissolve.

## Audio Prompt

No dialogue and no voice of any kind. No sound effects: nothing in this shot makes a sound, and this is not an omission — no event happens here for a sound to belong to. No ambient bed beyond the still air of a room whose only state is its light. Music: none, and no swell, no sting, no melody, no drone. The work's language is Japanese. There is no speech here, and the language is still named, so that the generator does not fill the blank with its own default. (No on-screen subtitles, no burned-in text, no background music.)

## Negative Prompt

no watermark, no on-screen subtitles, no background music, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no morphing or drifting facial identity, no clock, no window, no time of day, no directional light, no studio lighting, no bright daylight, no on-camera flash, no anime, no cel shading, no illustration, no 2D drawing, no smooth CGI, no 3D render, no digital polish, no perfect focus, no red wash over the whole frame, no amber wash over the whole frame, the white stays silver-white, not stained red or amber, no fully rendered face of the daughter, no name for the daughter, no image on the unexposed film, no lettering in frame, no readable text, no person, no figure, no body, no face in the room, no figure other than the shadow on the wall, no second shadow, no two shadows, no shadow of a second person, no silhouette of a child, no moving shadow, no step in the shadow, no event, no long dramatic shadow with hard edges, no dramatic mood lighting, no shadow of a hand raised, no hand in frame, no small hand pressing the lens, no child's hand of any kind, no cast shadow with a visible light source in frame, no lamp, no bulb, no bare light source, no window light, no sunbeam, no dust in the air, no ripple on the liquid, no drop falling, no bubbles, no foam, no print in the tray, no film in the tray, no tongs, no open drawer, no bottles or jars, no enlarger, no clock on the wall, no calendar, no mirror, no poster or picture on the wall, no pipes, no cables, no numbers of any kind, no glossy floor, no stainless steel, no clean modern darkroom, no portrait lighting, no bright evenly lit room, no cut, no time-skip, no date stamp, no caption, no title card carrying elapsed time, no aging makeup, no prosthetic, no cross-dissolve, no return to the place after leaving it, no posed studio lighting, no dramatic color grading, no CGI

## Style Motion

Full animation, not limited — and the form's native state is available to it. **The moment is unstaged, so time is whatever the subject does while unaware.** **What moves is ordinary and small — a hand, a turn of the head**, and the frame does not arrange itself around the movement. Here there is nothing in the frame that performs and nothing that moves at all except the weight of a shadow, and the room does not know that it is being measured. **The camera stands and watches, at eye level.** It holds; if it moves at all it moves to keep the subject in frame, never to make a point — and this shot spends none of it, because this shot's form makes the fixed frame the native case. **Stillness is fully available**, and this shot is the unstaged moment continuing for twenty years: the liquid does not move, the light does not arrive, and the only thing that changes is the one thing the room cannot see. The light stays available — an artificial source arriving is a different style, and nothing arrives here; the room's light is its constant state. (Source: the `Motion character` of the style card `documentary-photo`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `migenzo-ch02-seg01-9s-01`
- Segment ID: `02-1`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `9s`
- References: `REF_LOCATION (暗室, HIGH) ／ REF_GEOGRAPHY (暗室.geography, MEDIUM) ／ REF_STYLE (documentary-photo, HIGH) ／ REF_FORMAT (time-fold, HIGH) ／ REF_CHARACTER (無し) ／ REF_SOURCE (bible.yaml, CRITICAL) ／ REF_LEDGER (ledger.yaml, CRITICAL)`
- Attached: ⛔ **まだ確定していない——③ が決める。** ② の見込みは `暗室.base`・`暗室.geography`
  （`shots/migenzo-ch02-seg01.yaml` と `specs/image/migenzo-ch02-seg01.md` が一致している）。
  ⛔ **人物の鍵を、ここに置かない。** ⚠️ **`L6` が「記録が無い」と鳴るのが、いまは正しい。**
- Format Variables: `PLACE = 暗室 ／ PASSES = 二十年 ／ SURVIVOR = この部屋の状態（現像トレイと赤い安全光） ／ RANGE = 二十年 ／ DURATION = 9s`
- Temporal Structure: `3 beats, NON_UNIFORM — held 3s / transition 3s / held 3s. The span (twenty years) is spent unevenly: it lands in 3-6s`
- Camera Events: `0 events. One continuous take; the frame is a place the camera is put, and it does not change position`
- Action Events: `ACT_HOLD → ACT_DEEPEN`
- Audio Events: `no dialogue ／ no sound effects ／ no music ／ language declared: Japanese`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **この動画は、まだ一度も生成していない。** これは設計であって、記録ではない。
⚠️ **画像の側の採用の記録は、画像仕様に在る**——`specs/image/migenzo-ch02-seg01.md`（**13本とも採用済み**、
`PLAN.md` §4-f）。⛔ **この動画仕様は、画像の世代を写さない**（**写した分は古びる**）。

## Observed Problems

- 無し。**この動画の生成は、一度も走っていない。**

## Anticipated risks (to check in the first generation)

- **⚠️ 影が動く。** これが、この1本の最も起きやすい失敗である——
  ⚠️ **影の指が独りでに動けば、この1本は「異常が起きた1本」になる**（§17-1）。
  **輪郭が9秒のあいだ保たれているかを確かめる。**
- **⚠️ 影が伸びる、または形が変わる。** **濃さだけが変わること**を確かめる。
- **⚠️ 誰かが枠に入る。** **影を落としている体が撮られていれば、この1本は成立しない**（§3）。
  ⚠️ **そして、老けない女が立っていれば、20年は2人目の survivor になる。**
- **⚠️ カットが入る。** **切れば、二十年は「2つの状態」になる**（`time-fold`）。
  ⚠️ **§18 の3つのスロット（`Master`・`Motion`・`Camera`）すべてに `no cut` が在るかを確かめる。**
- **⚠️ 光源が枠に入る。** **ランプを描けば、この部屋の光は「照明」になる**（§13）。
- **⚠️ トレイに紙が置かれる。** **紙は予告になる**（§5）——⛔ **この1本は何も予告しない。**
  ⚠️ **この検査は、下の註の裁定のあとも生きている**——⚠️ **縛っているのは理由(1)（01 の結末）であり、
  この行は理由(2)（② の読み）に立っている**（**2026-09-23**）。

## ⛔ 空のトレイ——この不在は、2026-09-23 の著者裁定で、ここに決まった

- ⛔ **この1本は、`暗室.base` の「一枚」を打ち消す唯一のショットである**（13本のうち）。
- ⚠️ **根拠は 01 の結末である**——`specs/video/migenzo-ch01-seg01.md` §9 `ACT_LIFT` の After
  「**紙は液から出ており、脂痕が像の上に残っている。**」／`shots/migenzo-ch01-seg01.yaml` の
  `beats` `7-10s`「**絹が紙の縁をつまんで引き上げる。**」。
- ⛔ **著者裁定（2026-09-23）は「残す＋出所を記録」である**——**不在は落とさない。**
  ⚠️ **触ったのは、§5（(1) の出所の行と、(2) が読みである印）と、
  台帳 `暗室.base` の註の一行である。**
- ⛔ **07・10 との型の違い**——あの2本は**出所の無い読み**で base を打ち消していた
  （**ゆえに 2026-09-23 の裁定で、肯定形へ揃えた**）。**この1本は、直前のショットに従っている。**
- ⚠️ **そして、英語で渡る側には `no paper` が無い**——§18 `Negative` は
  `no print in the tray, no film in the tray` までである。**「空」と言っているのは、
  §18 `Visual Prompt` の `empty` の一語だけである**
  （⚠️ **2026-09-23 の走査では、13本の動画仕様のうち、トレイを「空」と言っているのはこの1本だけである**）。
- ⚠️ **画像仕様は、この不在を言っていない**（`specs/image/migenzo-ch02-seg01.md` は
  `the developer tray with its amber liquid lying still` までで、**触っていない**）。
- **⚠️ 「二十年」が数字になる。** **日付・字幕・暦・タイトルカードを確かめる**（`time-fold`）。
- **⚠️ 段が入る。** **濃さに段を置けば、「何かが起きた」になる**（§8）。**連続であることを確かめる。**
- **⚠️ トレイと安全光が動く。** **この2つが動けば、survivor が消える**（§10）。
  ⚠️ **液面の波ひとつが、この1本を壊す。**
