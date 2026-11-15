# review/design — 設計の評議会（1話1ディレクトリ）

**設計を評価してから、改稿する。** 対象は `PLAN.md` と `episodes/epNN.md`。
ショット記録でも §1–20 でもない。**まだ存在しないもの**を評価しない。

**全話を回す前提で、話ごとに切る。**

- `epNN/vNN/<seat>.json` — 五席の返答（`change` / `continuity` / `fidelity` / `feasibility` / `cinematic`）
- `epNN/scores.md` — 回ごとの平均と、五つの点、critical、変えたこと

**得点は五席の平均。65を超えたら通す。20回で打ち切る。**
⚠️ **点は設計についての判断であって、画の実測ではない。**
⚠️ **文学評議会の13次元と混ぜない。** 物語は別の台帳で評価済み。
⚠️ **65を下回った回は失敗ではなく結果である。** どの席が足を引いたかを書く。

## 走らせ方

`skills/design-review/SKILL.md` の五席を、**独立した subagent** として走らせる。
一つの席に、別の席の返答を見せない。前の回の返答も渡さない。

**その話を切った話だけ**を評価する。まだ切っていない話は、切ってから評価する。

## 記録

```
review/design/
  README.md
  ep01/                 # まだ（切っていない）
  ep02/                 # まだ
  ep03/                 # パイロット
    scores.md
    v01/                # 診断（旧基準）
      change.json
      continuity.json
      fidelity.json
      feasibility.json
      cinematic.json
    v02/                # 姉妹の帯で採点
  ep04/ ... ep10/
```

**反対は残す。** 著者が採らなかった指摘は、理由とともに `episodes/epNN.md` の「未決」へ残す。
