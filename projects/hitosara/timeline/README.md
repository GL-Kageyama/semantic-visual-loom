# `timeline/` — 編集がまだ無い

**このディレクトリは意図的に空である。** タイムラインは `*.yaml` である
（`schemas/timeline.schema.json`）。1本も無い。

⚠️ **物はここに置かない。** 編集で出来たファイル（繋いだもの）は `../renders/` である——
**記録はここ、物は `renders/`。** ⚠️ **向きは1つ**——**記録が物を名乗る**（写しは食い違う）。

⚠️ **いま `check.py` は、このディレクトリを読まない。** 読むのは段3である。
`SCHEMAS` 定数（`engine/ledger/check.py`）に `"timeline"` は在るが、
**`Project` はこのディレクトリを開かず、`validate_shape()` も
`timeline.schema.json` を当てない。** **宣言が正しいことと、
宣言どおりに読まれることは別である。**

⚠️ **だから、いまこのディレクトリが空であることは、何の報告でもない。**
`takes/` の空は報告される（「1本も無い」）。**こちらの空は報告されない**
——**同じ「空」でも、片方は検査されていて、片方は検査されていない。**
**この差は、ここに書いておかないと見えない。**

⚠️ **`*.md` は読まれない**（読む側が `*.y*ml` を選ぶ）。
だからこの文はタイムラインとして数えられない——**数えられては困る。**

## このディレクトリが埋まるとき

- 選別 — `take.verdict`（`machine` / `adherence` / `council`）と `adopted`
- 尺の解決 — `shot.duration`（意図）→ `take.params.duration`（生成）→
  `clips[].in` / `clips[].out`（採用）。**3つが初めて別々の値を持ちうる。**
- 文字の焼き込み — `text_events`。**生成器は文字を描かない**
  （`shots/hitosara-ch01-seg03.yaml` の `text_channel`、`seg07`、`seg10`）。
- 採用理由 — `clips[].cut_reason`
