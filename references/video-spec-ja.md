<!-- i18n-version: 2.1.0 | canonical: references/video-spec.md | translated: 2026-09-18 -->

**Language:** [English](video-spec.md) | [日本語](video-spec-ja.md) | [中文](video-spec-zh.md)

# 動画仕様（video-spec）

- **目的**: 叙述（再体験・誘引） ／ **粒度×時間**: 弧の全体 × 連続した一本の生成 ／ **サイズ・比率**: シネマ 16:9、`DURATION` の単一クリップ
- **要約**: 出力が**時間を持つ**唯一のフォーマット。時間を不均等に配ることで弧を連続した一本のテイクに畳み、静止画には語彙が無い4つの軸——時間・運動・カメラの移動・音——を担う。

## このフォーマットだけが違う一点

このエンジンの他のフォーマットはすべて時間を**捨てて**静止した面に着地する。これだけは時間を**畳み込む**。圧縮の対象は「語る一点」ではなく**語る一続きの持続**であり、選択の問いもそれに応じて変わる。

> *どの瞬間か*ではなく、**どの瞬間が秒を得て、どれが一瞬で済むか**。

すべてのビートに同じ時間を与えるダイジェストは、動画における詰め込みに等しい。**不均等な持続こそが構成である。**

## 環境変数
`SUBJECT`＝弧, `DURATION`＝クリップ長（**尺はモデルが決める**）, `ASPECT`＝アスペクト比, `BEATS`＝秒範囲つきのビート表, `CORE`＝最大の配分を取るビート, `HOOK`＝クリップが着地する音

## 構成の文法

**ショットリストではなくビート表**。弧を、**意図的に不均等な**秒範囲つきのビートとして並べる。ひとつのビート——核の開示——が最大の配分を取る（目安：`DURATION` の約30%）。疎のビートは質感と持続で保たせ、密のビートは数秒に複数の出来事を積む。

**静止画が持たない4つの軸：**

| 軸 | 何を固定するか | 欠かすとどうなるか |
|---|---|---|
| **時間** | ビートの秒範囲、密度（疎／密）、遷移 | 均一なテンポ——どのビートも同じ重さに読める |
| **運動** | 主体の動き、物理（重さ・慣性・流動・衝撃） | 浮わついた無重量の動き |
| **カメラ** | 時間をまたぐ移動（ショット種別ではない）、タイミング、対象 | N秒続くだけの静止フレーム |
| **音** | 台詞・効果音・環境音・音楽と、その情動的な機能 | 絵だけで意味を運ぶことになる |

**同一性のロック**。弧が複数の生成にまたがるとき、継続性ブロック（主体の外見・環境・照明・パレット）は**毎インスタンスに丸ごと貼る**——要約しない、参照で済ませない。独立した生成は記憶を共有しない。単一クリップでも書く：ネガティブプロンプトが守る対象がこれである。

**音の上で終える、その後ではなく**。最後の一秒は、観る者が「次があるか」を決める場所。フックに着地して切る——その後に解決のビートを足さない。

## do
- ビートに**明示的に不均等な**秒範囲を与え、どれが疎でどれが密かを述べる
- 最大の単一配分を核の開示に使う
- カメラを**時間をまたぐ移動**として書く（対象・速度・タイミング）。ショット種別ではなく
- 物理——重さ・慣性・流動——を固定し、動きに質量を持たせる
- 同一性のロックを省略せずに書き、インスタンスごとに一字一句そのまま繰り返す
- 再利用可能な仕様（WHAT/HOW）と、解決されたインスタンス（WHEN・尺・出力）を分ける
- §14 で作品の言語を名指し、`Audio Prompt` へ届かせる——**発話があるならそれはその言語であり**、発話の無い作品も宣言する。**空欄は中立ではない**（空欄は、生成器の既定で埋まる）
- 字幕と BGM の禁制を Negative に書く——**こちらから指定しない限り、どちらも出ない**
- フックで終える

## avoid
- `DURATION` を等間隔に割ること
- カメラの移動が無いショットリスト（静止画のスライドショー）
- 重さも慣性も述べられていない運動（浮わついた漂い）
- 省略による無音——台詞・効果音・環境音・音楽を未指定のまま残すこと
- 言語を書かずに残すこと——**生成器は自分の既定で喋る**（実測: 発話のある動画に中国語の字幕が焼かれた）
- 音楽と字幕は頼んだときだけ来ると思うこと——**省略は、モデルの既定を頼むことである**（実測: `no on-screen subtitles` は既に Negative に在り、それでも焼かれた）
- 継続性ブロックを貼らずに要約すること
- フックの後にビートを足すこと
- 弧のこの時点で原作がまだ開示していないものを映すこと（⑧原作に忠実 を参照——後の開示が前のクリップに漏れることが、このフォーマット特有の失敗）

## テンプレートは仕様であって、一文ではない

**このフォーマットを散文の一段落に畳んではならない。** このエンジンの他のカードはすべて穴埋めの一文で終わる——静止画はひとつのプロンプトだからだ。動画は*文書*である。成果物は、節ごとに個別に指し示せる仕様書であり、そうであってこそ時間・運動・カメラ・音を、他を書き直さずに個別に改訂できる。一段落の散文は、このカードが導入するために存在する当の4軸を破壊する。

散文の段落も存在はする——ただし **§18 の7スロットのうちの1つ**として、生成時に埋まった仕様*から*導かれるものとして。

## 仕様のスケルトン（§1–20）

この順に埋める。右列は各原則の着地点。

| § | 何を固定するか | エンジン |
|---|---|---|
| **1 VIDEO** | `DURATION`・`ASPECT`・解像度・フレームレート・向き ／ 目的・叙述機能・ムード・テンポ | — |
| **2 WORLD** | 概念・時代・場所・時刻・天候・雰囲気 ／ 世界の規則 ／ **Visual Language** | ⑥様式は Visual Language に着地する |
| **3 SUBJECTS** | 同一性・外見・振る舞い（性格／典型的な動き／情動の幅） ／ **継続性要件：Must Preserve・May Change** | ③翻訳 ＋ ④一貫 |
| **4 ENVIRONMENT** | 場所・要素 ／ 環境の振る舞い（風・天候・粒子・背景の動き） | ③翻訳 |
| **5 OBJECTS** | 外見・素材・機能 ／ 3つの重要度（叙述／視覚／継続性） | ③翻訳 |
| **6 REFERENCES** | 参照ごとに、何を **Defines** / **Influences** / **Does Not Define** か | ④一貫 |
| **7 NARRATIVE** | 中核の出来事・発端・展開・転回点・クライマックス・結末 | ①理解 |
| **8 TEMPORAL STRUCTURE** | **不均等な秒範囲のビート表** ／ タイミング方針（`NON_UNIFORM`） ／ 疎と密の領域 | ②**選択——このフォーマットの心臓** |
| **9 ACTION** | 行為ごとに意図・強度・速度 ／ Before・After・Simultaneous With・**Causes** | ⑤構成（因果） |
| **10 CAMERA** | カメラ言語 ／ **タイミング・移動・対象・速度を持つカメライベント** | ⑤構成を時間へ |
| **11 MOTION** | 主体／物体／環境の運動 ／ **物理：重さ・慣性・加速・流動・衝撃** | ⑤構成を時間へ |
| **12 EMOTION** | 連鎖としての情動の弧 ／ 強度つきの情動イベント | ③翻訳 |
| **13 LIGHTING** | キー・フィル・リム・アンビエント・色温度 ／ 照明イベント | ③翻訳 ＋ ⑥様式 |
| **14 AUDIO** | 台詞（話者・内容・言い方）・効果音・環境音・音楽とその情動的機能 ／ **作品が話す言語（名指し）** | **このフォーマット固有の軸** |
| **15 CONTINUITY** | 同一性・空間・時間・視覚・運動の継続——**同一性のロック** | ④一貫 |
| **16 CONSTRAINTS** | MUST / MUST NOT / PREFER / ALLOW | ⑦ネガティブ |
| **17 GENERATION PRIORITIES** | 衝突時の優先順——見栄えより原作への忠実を上に置く | ⑧原作に忠実 |
| **18 PROMPT MAPPING** | 7つのプロンプト——6つは §1–17 から、7つ目は**様式カード**から | — |
| **19 GENERATION INSTANCE** | ひとつの生成の解決値（尺・参照・イベント・出力） | — |
| **20 ITERATION** | 観測された問題 → 変更 → 次の生成 | — |

§1–18 を再利用可能に保ち、尺に依存するものはすべて §19 に置く。そうすればクリップ長や生成モデルが変わっても同じ仕様が生き残る。

## §18 のプロンプトスロット

7つのプロンプト。最初の6つは**主に**上記の名指しされた節から取る。
**7つ目だけは仕様からではなく、様式カードから取る。**
**分離されていること自体が要点**なので、混ぜない。

```text
Master Prompt   ← §1 + §7 + §8
  A {DURATION} continuous cinematic take ({ASPECT}) of {SUBJECT}, one clip.
  Beats, deliberately uneven: {BEATS}. The core beat — {CORE} — holds the largest
  share of the duration; the remaining beats pass quickly. Ends on {HOOK} and cuts.

Visual Prompt   ← §2 Visual Language + §3 Appearance + §4 + §5 + §13
  (the look, held still: art direction, palette, rendering, subject appearance,
  environment, key/fill/rim, color temperature — no motion words)

Motion Prompt   ← §9 + §11
  (what moves, in what order, with what weight, inertia and speed — subject motion,
  object motion, environmental motion, and the physics that governs all three)

Camera Prompt   ← §10
  (the camera events in order: timing, movement, target, speed, transition)

Audio Prompt    ← §14 + the work's language (`bible.language`)
  (dialogue with speaker and delivery, sound effects, ambient bed, music and its
  emotional function — and the work's language, named, so that the generator does
  not fill the blank with its own default)

Negative Prompt ← §16 MUST NOT + this card's Negative + the style card's Negative

Style Motion    ← the style card's Motion character (not §1–17 — the only slot taken from the style)
  (how this style moves at all — full animation or limited, whether a held frame
  is permitted, what the primary mover is. The specification writes what moves in
  THIS clip; the style card writes what movement MEANS in this style.)
```

The sources above are the main ones, not the only ones. The camera-stability
prohibition is the known case: it is written in §10, and it reaches the model
through the Negative slot.

⚠️ **`Style Motion` が7つ目である理由。** 他の6つは**この仕様の中**で決まる——
節を書き換えれば変わる。`Style Motion` は**この仕様の外**で決まる——
様式を替えれば変わり、**同じ §11 が別の意味を持つ。**
「何が動くか」と「この様式で動くとはどういうことか」は別の問いであり、
混ぜれば**仕様が様式を上書きする**（あるいはその逆）。
⚠️ **§11 MOTION が空でも `Style Motion` は書ける。** 主題が止まるショットでも、
**その様式が止まった主題をどう扱うか**は決まっている——**この2つは別の欄である。**

## Negative
`no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no background music, no watermark, no morphing or drifting facial identity`

## 事例
- 午前二時に、あなたは誰の時間を生きていますか 第1話 → 30秒ダイジェスト（gozen-niji-video-01・soft-cel-anime）

## 出典
Wan 3.0 — Video Generation Specification（対象となる中間表現）／`storyboard`（最も近い静止画の先祖——コマとショット種別は持つが、移動・物理・音を持たない）
