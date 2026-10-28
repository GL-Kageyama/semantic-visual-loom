---
name: direction
description: '作品の劇作——①のうち、作品が何を主張し、価値がどう転換し、幕とシーケンスがどこで切れ、各ショットが何のためにあるかを決める部分。台帳の第三の登録簿と、各ショットの劇的記録を書く。仕様は書かない。breakdown の後、design の前に走る。⚠️ 第五段階ではない。'
argument-hint: '(任意) 作品名、または演出するシーケンス。例: /semantic-visual-loom:direction drama-pilot'
---

<!-- i18n-version: 1.0.0 | canonical: skills/direction/SKILL.md | translated: 2026-10-29 -->

**Language:** [English](SKILL.md) | [日本語](SKILL-ja.md) | [中文](SKILL-zh.md)

# direction — ① 作品の劇作

**①は何が変わるかを言った。②はショットを決める。この文書は、①のうち、その変化が何のためにあるかを決める部分である。**

⚠️ **第五段階ではない。** ①の中、`breakdown` がショットリストを出した後、`design` が仕様を書く前に走る——`staging` が②の中で走るのと同じ形である。書くのは台帳の第三の登録簿と、ショット記録の `dramatic` 欄である。**§18 のスロットも仕様も書かない。**

## ⚠️ なぜこれが要るか——台帳は二つの登録簿しか持っていなかった

制作台帳は**連続性**（世界の状態）と**開示**（観客の知識の状態）を持つ。どちらも**何が真か**についてである。**観客が何を感じ、何を予期し、何を持ち帰るか**については、どちらも持っていない。

だから劇的さは偶然だった——§18 の散文が上手いかどうかに依存していた。`aim` はショットが何を試したかを記録したが、読む検査は一つも無かった。`take.verdict.council` は席だけがあって、誰も座っていなかった。作品のレベルで、幕の転換も、シーケンスの対比も、モチーフの回収も決めていなかった。

⚠️ **失敗は「プロンプトが下手だった」ではない。** **作品が、自分の変化に何の値があるかを決めていなかった**ということである。ショットは `unit` を完璧に実行して、それでも誰も覚えないショットになりうる。

## この段階が持つもの

| | 何 | どこ |
|---|---|---|
| **treatment** | premise · question · argument · visual thesis · value poles · ending image | `ledger.yaml` → `dramaturgy` |
| **幕** | 各幕の `turn` · `climax` · `value_from` / `value_to` · `rhythm` | 同上 |
| **シーケンス** | `contrast` · `escalation` · `transition` · `payoff` · `flat` · `withheld` · `cuts` · `tempo` | 同上 |
| **モチーフ** | 初出・反復・回収 | 同上 |
| **見せ場** | どのショットがどの形式カードを使うか、なぜか | 同上 |
| **音の弧** | 沈黙、音楽が入る所、作中の音 | 同上 |
| **各ショットの劇的記録** | `function` · `value` · `audience` · `button` | `shots/<id>.yaml` → `dramatic` |

**持たないもの**: ショットリスト（**`breakdown`**）、仕様と `DIRECTION` 節（**`design`**）、テイクと評（**`shot`**）。⚠️ **採用も持たない**——それは作者の行為である。

⚠️ **ショットは単位のままである。** 幕とシーケンスは**ショットの上に重なる眺め**であって、生成単位ではない。1ショットはやはり1変化である。

## 決定の順序

⚠️ **この順序は設計の主張であり、検査は強制しない。** 上から下へ決め、決めたそばから書く。**個々のショットから作品を逆算しない**——それが、良いショットの集まりを、主張の無い作品に変える。

1. **Premise——何が起きるか、一行で。** 二文が要るなら、その作品には前提が二つあり、片方は装飾である。
2. **Question——観客が最後まで持ち越す問い。** 「生き残るか」ではなく、作品が開き続ける具体的な不確かさ。**終わりで答えられるものでなければならない。**
3. **Argument——作品が言うこと。** 終わりが立てる主張。⚠️ **主題語（「愛」「記憶」）と混同しない。** 主張は、誰かが反対できる文である。
4. **Visual thesis——光・色・構図が何を言うか。** 同じ主張を視覚の層で。⚠️ **少なくとも2ショットで見えなければ、それは気分である。**
5. **Value poles——作品が転換する価値の対。** `{ja, en}` で書く。日本語は記録が使い、英語は `DIRECTION` 節が運ぶ。**対を持たない価値は、賭けではなく設定である。**
6. **Acts——作品がどこで転換するか。** 各幕に一つの `turn`（一つの変化）、`climax`、`value_from` → `value_to`、`rhythm`。**転換の無い幕は、長さであって幕ではない。**
7. **Sequences——隣接ショットがどう対立するか。** 各シーケンスに `contrast`（次のショットが何に対するものか）、`escalation`（何が育つか）、`transition`（どう渡すか）、`payoff`（何を回収するか、あれば）。そのうえで**三つの拘束——この登録簿のうち画に届く部分**：
   - **`withheld`**——観客が欲しがって、渡されないもの。名指したショットに `wanted`（何を待っているか）と `given`（代わりに何を渡すか）。⚠️ **二つは違っていなければならず、どちらも空ではならない**——約束したものを渡すのは先延ばし、何も渡さないのは事故である。⚠️ **誰も待っていないショットは、何も欠けさせられない**——観客が具体的に何かを欲しがる所にだけ書く。
   - **`cuts`**——どのショットが、自分の内側で時間を切るか。⚠️ **切れ目は並びの決定であって、ショットの決定ではない**——隣のショットがあって初めて意味を持つ。ショットの記録が `cut: internal` を持ち、**仕様はワンテイクと言うのをやめなければならない**——生成器は記録を読まない。
   - **`tempo`**——シーケンスの形を秒で、ショットごとに1つ、**各ショットの `duration` と一致させる**。⚠️ **正は `duration` であり、`tempo` は写しである。** 同じ値が3本以上続くならそれは平らな律動であり、`flat: true` と `note` を要る。
   ⚠️ **意図して平らなシーケンスは `flat: true` と理由を書く**——それは欠落ではなく決定である。
8. **Shot functions——各ショットが何のためか。** すべてのショットに `function`、`value.from` / `value.to`、`stake`、`audience.feel` / `expect` / `know`、`button` を書く。⚠️ **値は、そのショットの一つの変化の値であって、二つ目の変化ではない。** ⚠️ **非物語の関数（質感・余白・様式美）は値の転換を要さない**——それでも `button` は要る。どのショットも一枚で終わるからである。
9. **Set pieces——どの形式カードが場所を得るか。** カードはショットの §6 `REF_FORMAT` で名指し、選択は `set_pieces` に `why` とともに記録する。**カードがデバイスである。その名前をショット記録の二つ目の欄に複製しない。**
10. **Sound——沈黙から。** 音楽の無い所、音楽が入る所、作中の音が場面を負う所を決める。⚠️ **床は `no background music` のまま**である。音楽を使う作品は `bible.base_negatives_waived` に `no background music` を書く。**二つ目の除外席を作らない。**
11. **Ending image——最後に残るもの。** ⚠️ **像でなければならない。教訓ではない。** 主張が言葉でしか言えないなら、視覚の主張は届いていない。

## 何を、どこに書くか

```yaml
dramaturgy:
  version: 1
  premise: "…"
  question: "…"
  argument: "…"
  visual_thesis: "…"
  value_poles:
    - ja: 安全
      en: safety
    - ja: 危険
      en: danger
  acts:
    - id: act-1
      shots: [s01, s02, s03, s04]
      turn: "…"
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
      withheld:
        - shot: s01
          wanted: "her face when the world answers"
          given: "the valley's light, and her back"
      cuts: [s03]
      tempo: [8, 8, 8]
  set_pieces:
    - shot: s07
      format: impossible-camera
      why: "…"
  ending_image: "…"
```

```yaml
# shots/<id>.yaml
dramatic:
  function: 転換
  value:
    from: 安全
    to: 危険
    stake: "父の記憶"
  audience:
    feel: "息を止める"
    expect: "彼が扉を開ける"
    know: "母がまだ生きている"
  button: "閉じた扉の向こうの光"
```

⚠️ **`function` は日本語の記録値である**（設定・上昇・転換・発見・決断・結果・溜め・解放・余韻、加えて非物語の質感・余白・様式美）。`design` が `specmap.DRAMATIC_FUNCTION_EN` を通して仕様の `DIRECTION` 節に書く——**記録は日本語のまま、生成器へ渡る文字列は英語である。**

⚠️ **`audience.know` は `disclosure_state` ではない。** 後者は世界の事実、前者はこの瞬間に観客が知っていることである。**どの層も両者を比較しない**——両方を読む設計セッションの判断である。

## デバイス——カードが名前である

AI 固有の演出は**形式カード**に住む。新しい欄ではない。ショットは §6 `REF_FORMAT` でカードを名指し、`dramaturgy.set_pieces` がその場所でなぜ使うかを記録する。⚠️ **ショット記録に `device:` を足さない**——同じものの二つ目の名前は、食い違う場所になる。

⚠️ **「多用する」は目的であり、予算はそれを規律にする。** 予算は野心の上限ではない。**すべてのデバイスが値の転換を負う**という規則である。

- **1ショットに主デバイスは一つ。** 二つ目は、**同じ**値の転換を別の面から負うときだけ許す。
- **5ショットのシーケンスにデバイスは2–3本**が既定。**見せ場は4本まで**——各本が転換を負い、直前か直後に接地ショットを持つこと。
- ⚠️ **デバイスショットには接地ショットが要る**: 同じ世界を、普通のカメラで、前か後に。**接地を挟まない連続デバイスショットは2本まで。**
- ⚠️ **何も負わないデバイスは装飾である——捨てる。** 規則は「少なく使う」ではなく、**「装飾を残さない」**である。

⚠️ **顔のモーフィングは床の仕事ではない。** `BASE_NEGATIVES` が持つのは `no watermark` / `no on-screen subtitles` / `no background music` だけである。同一性の固定は `video-spec` カードの `## Negative`（`no morphing or drifting facial identity`）が担う。**AI の変容は、顔ではなく、世界・素材・尺度・光で起こす。** それは制約ではなく、この基盤の美学である。

## 検査が読むもの

- **`L40`** — `dramatic` を持ち、物語の `function` を持つショットで、`value.from == value.to`。非物語の関数は対象外。`dramatic` を持たないショットは註の本数。
- **`L41`** — `turn` の無い幕、`contrast` の無いシーケンス、実在しないショットを指す `payoff`、実在しない `shots`。`acts`/`sequences` が無ければ註。
- **`L44`** — 強度の曲線: 同じ `intensity` が3ショット以上続く、または幕に最大値が無い。`flat: true` を宣言したシーケンスは註。
- **`L47`** — `performance.objective == performance.obstacle`。`performance` の不在は違反ではなく、註の本数。
- **`L48`** — `withheld` の `wanted` と `given` が同じ、またはどちらかが空。作品の最後の1本の欠けは註。
- **`L49`** — シーケンスが宣言した切れ目をショットが持っていない、またはその逆。**そして、まだワンテイクと言っている仕様。**
- **`L50`** — `tempo` がショットの `duration` と合わない、または `flat: true` と `note` の無い等間隔。

⚠️ **転換が良いか、対比が鋭いか、デバイスが記憶に残るかは、どの層も読まない。** それは評議会と作者に属する。

## この段階が決めないこと

- **作品が心を動かすか。** 検査には分からない。評議会が助言し、作者が決める。
- **仕様。** `design` が §1–20 を書き、`DIRECTION` 節もそこに書く。
- **テイク・採用・編集。** ④と作者。
- **経路とモデル。** §18 の見出しが経路を名乗る（`L18`）。

## 言語

- **記録側は日本語である。** `function`、`value.from` / `value.to`、`stake`、`audience`、`button`——これらは作者と `L40`/`L43`/`L47` が読む。
- **生成器へ渡る文字列は英語である。** `DIRECTION` は `design` が、これらの記録と §12 から英語で書く。**記録をプロンプトへ翻訳しない。英語の型を書く。**

## さらに読む

- [`skills/breakdown/SKILL.md`](../breakdown/SKILL.md) — ①の前半、この段階が読むショットリスト
- [`skills/design/SKILL.md`](../design/SKILL.md) — ②、`DIRECTION` を書く段
- [`skills/staging/SKILL.md`](../staging/SKILL.md) — ②の中のカメラ
- [`references/formats/video-spec.md`](../../references/formats/video-spec.md) — §12 EMOTION と `DIRECTION` 節
- [`schemas/ledger.schema.json`](../../schemas/ledger.schema.json) — `dramaturgy` の形
- [`schemas/shot-record.schema.json`](../../schemas/shot-record.schema.json) — `dramatic` の形
