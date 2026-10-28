<!-- i18n-version: 1.0.0 | canonical: docs/dramaturgy.md | translated: 2026-10-29 -->

**Language:** [English](dramaturgy.md) | [日本語](dramaturgy-ja.md) | [中文](dramaturgy-zh.md)

# 劇作——台帳の第三の登録簿

**製作台帳は「何が真か」を持つ。** 連続性は**世界の状態**を持ち、開示は**観客の知識の状態**を持つ。
どちらも *何が事実か* に答える。

⚠️ **どちらも、その変化が何の値だったかには答えない。** ショットは `unit` のとおりに正確に働いて、
それでも誰も覚えていないショットでありうる。**劇作は第三の登録簿であり、作品がそれを決める場所である。**

**第五段階ではない。** 同じ `ledger.yaml` の中の登録簿である——**台帳は分割しない**
（[`CLAUDE.md`](../CLAUDE-ja.md) の Fixed Policy）。連続性・開示・劇作は**ひとつのファイルへの三つの問い**であり、
参照集合と禁制集合は今もその一点から導出される。

## なぜ台帳の中に在り、隣に無いのか

台帳を一つにする規則を生んだ失敗は、**「どの参照画像をどのショットに付けるか」**だった——
それは連続性であり同時に開示でもある問いであり、二つを分けると答えられなくなる。

**劇作は同じ種類の問いを立てる。** 「このショットの隣に接地ショットがあるか」は、
**世界**について（連続性）、**観客が何を見てよいか**について（開示）、そして
**デバイスは何のために在るか**について（劇作）の問いである。第三を別ファイルに置けば、
三つの答えは、それぞれが内部で正しいまま、互いにずれる。

## 何を持つか

```yaml
dramaturgy:
  version: 1
  premise: "…"          # 何が起きる話か（一行）
  question: "…"         # 観客が最後まで持ち越す問い
  argument: "…"         # この作品が言うこと——誰かが反対できる一文
  visual_thesis: "…"    # 光・色・構図で言う同じこと
  value_poles:
    - ja: 安全
      en: safety
    - ja: 危険
      en: danger
  acts:
    - id: act-1
      shots: [s01, s02, s03, s04]
      turn: "…"          # この幕の一つの変化
      climax: s03
      value_from: 安全
      value_to: 危険
      rhythm: "溜め → 爆発 → 余韻"
  sequences:
    - id: seq-1
      shots: [s01, s02, s03]
      contrast: "静 → 動"
      escalation: "…"
      transition: "…"
      payoff: s09
      flat: false
  motifs:
    - id: light
      first: s01
      recurrences: [s04, s07]
      payoff: s12
  set_pieces:
    - shot: s07
      format: impossible-camera   # ショットの §6 REF_FORMAT と一致すること
      why: "…"
  sound_arc:
    silence: [s01, s02]
    score_enters: s03
    note: "…"
  ending_image: "…"    # 最後に残る一枚
```

⚠️ **`acts` と `sequences` はショットの上に重ねた眺めであり、生成単位ではない。**
**ショットは単位のままである。** 1ショットは1変化のままであり、幕はその4本の読み方である。

⚠️ **`payoff` は前方を指してよい。** 予約された回収は状態ではない——連続性台帳の `… yet` と同じ規律である。
`L41` は行き先が実在するかだけを見る。

⚠️ **`note` の無い `flat: true` は宣言ではない。** 緊張の曲線が意図的に平らなシーケンスは
**なぜかを言う**; `L44` は素の旗で鳴る。

⚠️ **`value_poles` は作品自身の写像**（`{ja, en}`）である。記録が日本語を書き、`DIRECTION` が英語を運ぶ。
⚠️ **`en` は節に文字として現れる語でなければならない**——`L43` はそれを探し、
活用も同義語も追わない。**対の無い値は設定であって、賭けではない。**

## ショットの劇的記録

```yaml
# shots/<id>.yaml
dramatic:
  function: 転換              # 設定/上昇/転換/発見/決断/結果/溜め/解放/余韻
                              # または非物語の 質感/余白/様式美
  value:
    from: 安全
    to: 危険
    stake: "父の記憶"
  audience:
    feel: "息を止める"
    expect: "彼が扉を開ける"
    know: "母がまだ生きている"
  button: "閉じた扉の向こうの光"
  performance:
    objective: "娘を守る"
    obstacle: "扉が開かない"
    tactic: "体で押す"
    subtext: "許しを請う"
    intensity: 8
```

⚠️ **`value` は、ショットのたった一つの変化の値であり、二つ目の変化ではない。** `unit` が
何が変わるかを言い、`value` がそれが何を代償にしたかを言う。**ひとつの変化の二つの読み**である
——二つ目の値の転換が要るショットは、2本のショットである。

⚠️ **非物語の関数**（質感・余白・様式美）**は値の転換を要さない**——だが `button` は要る。
**どのショットも一枚で終わるからである。**

⚠️ **`function` と `role` は別の軸である。** `role` はそのショットの仕事（`L15` が読む）;
`function` はそのショットが起きるとき物語がどこに在るか（`L40` が読む）。語彙は重なる
（転換・余白・様式美）——⚠️ **片方から他方を推測しない。**

⚠️ **`audience.know` は `disclosure_state` ではない。** 後者は世界の事実であり、前者は
その瞬間に観客が持っているものである。**どの層も両者を比べない**——観客が人物より先に
知っているかは判断であり、それを推測する層は物語を書いてしまう。

⚠️ **`performance` は人物がいて `mode: motion` のショットで期待され**、その不在は
**違反ではなく註**である——人物のいないショットもある。⚠️ **`objective == obstacle` は
`L47` を鳴らす**: 自分の障害が言い直している願望は、願望ではなく説明である。

⚠️ **§17 と §18 の間に置くのは、順序の主張である。** §18 は七つのスロットへの対応表であり、
演出はその手前で決まっていなければならない——**スロットを書いた後で演出を足すのは、理由を後から着けることである。**
⚠️ **番号は動かさない。** 既存の仕様は §18–20 の番号をそのまま使い続ける。
**だからこの節は番号を持たない**——番号を持てば、100本を超える仕様が一斉に赤くなる。

## `DIRECTION` 節

仕様は、§17 と §18 の間に、番号を持たない節を**一つ持ってよい**:

```text
DIRECTION  ← ledger.dramaturgy + shot.dramatic + §12 EMOTION
  Play {FUNCTION} for {AUDIENCE_FEEL}. The value turns from {VALUE_FROM} to
  {VALUE_TO}; the stake is {STAKE}. Use {DEVICE} only to {DEVICE_WHY};
  keep {INVARIANT}. End on {BUTTON}.
```

⚠️ **スロットではない。** `PROMPT_SLOTS` は七つのままであり、`L17`・`L28`・`L30` は変わらない。
**生成時にはその本文が `Master Prompt` の先頭へ連結される**——仕様の上では独立した節、
生成器の上では Master の第一段落である。

⚠️ **感情が生成器へ届いた最初の経路である。** §12 EMOTION は**どのスロットの出所でもない**
仕様の節である（`specmap.PROMPT_SLOT_SOURCE`）——これまでは、ショットの感情は書かれ、綴じられていた。

⚠️ **演出要約の写しではない。** 演出要約は**読むために書かれ**、出所ではないと明記されている
（[`skills/design/SKILL.md`](../skills/design/SKILL-ja.md)）。`DIRECTION` は台帳・ショット記録・§12 から
**書かれる**——**日本語の記録から訳されない。** 英語は型であって、描き直しではない。

## シーケンスは何を拘束するか

`contrast`・`escalation`・`transition` はシーケンスを**記述する**。**三つの欄は、それを拘束する**
——そして、どれもショットと照合できるから、この三つが
**劇作のうち最初に、紙ではなく画に届く部分**である。

```yaml
sequences:
  - id: seq-2
    shots: [s04, s05]
    withheld:
      - shot: s04
        wanted: "the flame entering the lantern — the audience is waiting for it"
        given: "it does not light. The flame is never in this film."
    cuts: [s05]
    tempo: [9, 9]
```

⚠️ **`withheld` は、観客が欲しがって、渡されなかったものの席である。** `wanted` と `given` は
違っていなければならず、どちらも空であってはならない——**約束したものを渡すのは欠けでは
なく先延ばしであり、何も渡さないのは選択ではなく事故である。** `L48` が読む。**作品の最後の
1本の欠けは、違反ではなく註である**——見せないことが結末になりうる。

⚠️ **`cuts` は、ショットだけでは決められない切れ目である。**
切れ目は、隣のショットがあって初めて意味を持つ——だから**シーケンスが宣言し**、
ショットの記録が `cut: internal` を持つ。`L49` は両方向を見て、
**さらに仕様の本文を開く**——記録だけを変えて散文を変えなければ、
記録を一度も読まない生成器は、ワンテイクを作り続ける。

⚠️ **`tempo` はシーケンスの形を秒で書いたものであり、正はショットの `duration` に在る。**
`L50` はその写しを照合する。**同じ値が3本以上続けば鳴る**——ただし `flat: true` と
`note` を宣言したシーケンスは除く。**平らな律動は設計でありうる**し、
その平らさが、次の変化を効かせる罠でありうる。

⚠️ **この三つは、シーケンスを良くしない。** 観客が何を欲しがっているかを作品が知っていて、
どこでそれを渡さないかを決める——**その席である。**

## 検査が読むもの、読まないもの

| 層 | 読むもの | 鳴る条件 |
|---|---|---|
| `L40` | `dramatic.function` / `value` | 物語の関数なのに `value.from == value.to` |
| `L41` | `dramaturgy.acts` / `sequences` | `turn` の無い幕; `contrast` の無いシーケンス; 実在しない `payoff` や `shots` の項 |
| `L43` | `DIRECTION` 節、`dramatic`、`value_poles` | `dramatic` を持つショットに節が無い; 英語の関数が無い; 値の英語が無い |
| `L44` | `beats[].intensity` | 同じ強度が3ショット以上続く; 幕に最大値が無い |
| `L47` | `performance.objective` / `obstacle` | 二つが同じ |
| `L48` | `sequences[].withheld` | `wanted` と `given` が同じ、またはどちらかが空 |
| `L49` | `sequences[].cuts`・`cut: internal`・仕様の本文 | 片側だけの宣言。ワンテイクのままで書かれた仕様 |
| `L50` | `sequences[].tempo` とショットの `duration` | 秒数の食い違い。`flat: true` と `note` の無い等間隔 |

**どれも、転換が良いかは読まない。** 曲線が平らで、値が些末で、幕が恣意的でも、すべての層は通る
——**それが設計である。** 質は[評議会](../skills/review/SKILL-ja.md)と作者のものである。

## ⚠️ 記録は opt-in であり、不在は食い違いではない

**ここの欄はすべて任意である。** `dramaturgy` も `dramatic` も持たない作品は通り、註が
何本のショットを見たかを書く。

⚠️ **遡って埋めない。** 後から書かれた `function` は関数ではなく説明である——`aim` が持つのと同じ規律である。
⚠️ **この登録簿より前に作られた作品は、それによって間違いにならない。**

**スイッチは記録であって、版ではない。** `format-version:` という欄は無く、読まれもしない;
`dramatic` を持つショットは `L40`/`L43`/`L47` の範囲に入り、持たないショットは入らない。
**エンジンは、どの作品が特別かを覚えていない。**

## 読まれないもの

- **premise・argument・ending image が良いか。** 散文であり、作者の判断である。
- **`set_pieces[].why`。** `L42` が比べるのは見せ場の `format` と §6 だけである。
- **`sound_arc`。** どの層も開かない——決定であって、読み手のいる欄ではない。
- **`motifs[].recurrences`。** 作者が形を見るために並べてあり、何も解決しない。
- ⚠️ **観客が何かを感じたか。** 生成はこのリポジトリの外で起き、**この登録簿は測ったと言わない。**

## さらに読む先

- [`skills/direction/SKILL.md`](../skills/direction/SKILL-ja.md) ——この登録簿を書く段
- [`skills/design/SKILL.md`](../skills/design/SKILL-ja.md) ——`DIRECTION` を書く段
- [`skills/review/SKILL.md`](../skills/review/SKILL-ja.md) ——それを裁く評議会と、そのやり方
- [`schemas/ledger.schema.json`](../schemas/ledger.schema.json) ——`dramaturgy` の形
- [`schemas/shot-record.schema.json`](../schemas/shot-record.schema.json) ——`dramatic` の形
- [`references/formats/video-spec.md`](../references/formats/video-spec-ja.md) ——§12 EMOTION と `DIRECTION` 節
- [`docs/cards.md`](cards-ja.md) ——形式カード。それがデバイスである
