<!-- 2026-09-29: この契約は、31本の仕様を委任して書かせたときのものである。
     生成器がリポジトリへ入ったので、道はリポジトリからの相対に直した。 -->

# odyssey 動画仕様 — 執筆契約

あなたは `semantic-visual-loom/projects/odyssey/` の**動画仕様（§1–20）**を書く。
対象は割り当てられたショットだけ。**他のショットのファイルには触らない。**

## 0. まず読むもの（この順で）

1. `../specs/video/odyssey-s05.md`
   ——**人物の居る1本の見本。** これが文体・密度・節の作り方の基準である。
2. `../specs/video/odyssey-s02.md`
   ——**人物の居ない1本の見本。**
3. 自分の担当ショットの記録 `../shots/odyssey-sNN.yaml`
   ——**これが唯一の正。** ヘッダのコメントに、その1本の設計意図が全部書いてある。**必ず全部読む。**
4. そのショットが名乗る**形式カード** `../../../references/formats/<format>.md`
   ——**`## Composition grammar` を必ず読む。** 形式は「`video-spec` に文法を1つ足したもの」である。
   **環境変数（`WITNESS`・`DRIFT` …）は全部その1本の中で使う。**
5. `content/s02.py` ——**content モジュールの書き方の見本。**
6. `common.py` ——**共通の散文の道具。** これを使って書く。
7. ⚠️ **要約はもう無い。** 以前は `/tmp/odyssey_digest.txt` に34本の要約があったが、
   **それは `shots/` から作った写しであって、正ではない**（しかも古くなっていた）。
   **正は `shots/odyssey-sNN.yaml` である。** 要約が要るなら自分で起こす。

## 1. 出すもの

`content/<sid>.py` を1ショットにつき1つ。中身は `C = { ... }` の辞書1つ。

```python
import common as K

C = {
  "n": "s06", "title": "...", "duration": "6.143", "format": "meaning-responsive",
  "has_man": True, "segment": "verse-1-2",
  "header": """...""",            # 先頭の註（ショット記録のヘッダから起こす）
  "intent": "...",                # §1 Generation Intent
  "world_concept": K.world_concept("..."),
  "world_rules": K.world_rules(tails={...}, extra=[...]),
  "visual_language": K.visual_language(**{...}),
  "subjects": [ {...}, ... ],
  "environment": {"location": "...", "elements": "...", "behavior": "..."},
  "objects": ["..."],
  "ref_character": "...",
  "narrative": {"core": "...", "beginning": "...", "turn": "...", "peak": "...", "pull": "..."},
  "density": "...",
  "actions": [("ACT_X", "Before", "After"), ...],
  "camera": {"language": "...", "events": "...", "behavior": "..."},
  "motion": {"subject": "...", "object": "...", "environment": "...",
             "weight": "...", "inertia": "...", "acceleration": "...", "fluidity": "...", "impact": "..."},
  "emotion": {"arc": "...", "events": "..."},
  "lighting": {"base": "...", "events": "..."},
  "audio": {"dialogue": K.NO_DIALOGUE, "sfx": "...", "music": K.NO_MUSIC, "environment": "..."},
  "continuity": {"identity": "...", "spatial": "...", "temporal": "...", "visual": "...",
                 "motion": "...", "sound": "..."},
  "must_not": K.must_not_common(has_man=True, goddess_extra="...") + ["..."],
  "must": ["..."], "prefer": "...", "allow": "...",
  "priorities": ["...", "...", "Everything else."],
  "preamble_tail": K.preamble_tail("..."),
  "master": "...", "visual_scene": "...", "visual_meta": K.VISUAL_META,
  "motion_prompt": "...", "camera_prompt": "...", "audio_prompt": K.AUDIO_PROMPT % ("...",),
  "resolved_references": "...", "camera_events_count": "1 event as listed in §10",
  "audio_events": "...",
  "unresolved": ["..."], "risks": ["..."],
}
```

**`beats` は書かない**——生成器がショット記録から取る（`L37` のため）。

## 2. 生成器が持つもの（**あなたが書いてはいけないもの**）

`tpl.py` が以下を**すべて**差し込む。書けば二重になる。

- §1 の `Aspect` / `Resolution` / `Frame Rate` / `Orientation`（`L26`）と `Duration`（`L23`）
- §6 の `REF_FORMAT` / `REF_STYLE` / `REF_SOURCE` と経路の註
- §16 の**形式カード自身の `## Negative`**（逐語）と床の4項
- §18 の前書きの共通5段落、**`Negative Prompt`**、**`Style Motion`**、`(Source: …)`
   ——⛔ **§18 の `Negative Prompt` と `Style Motion` は34本で同一でなければならない**（`L10`）。
   **絶対に書かない。**
- §18 の見出し7つ、§19 の日付の欄、§20 の `Version` と `Observed Problems`

## 3. 守る規則

1. **§18 の7スロットは全部英語。** 日本語（CJK）を1字も入れない。**生成器が検査して落ちる。**
2. **人物が居る1本（`has_man: True`）**: `master` の中に `{IDENTITY}` と書くと、そこに
   **同一性の塊（`ledger.characters.男.identity`、867字）が逐語で差し込まれる。**
   ⚠️ **裁定②により参照画像は1枚も無い。この英文だけが顔を守る。** 要約しない。
   `visual_scene` には**書かない**——生成器が自動で後ろに付ける。
   **人物の居ない1本（`has_man: False`）は `{IDENTITY}` を書かない。**
3. **`motion.law` を必ず読む。** ショット記録の `motion.law` が、その1本の運動の法である。
4. **§8 のビートは記録のもの。** `density` には**その1本の時間の配分の理由**を書く。
5. ⚠️ **`Camera Prompt` の書き方に罠がある**（検査 `L33`）。様式 `cinematic-still` は
   ドリー・クレーン・ステディカムを**許している**。**この3語を否定形で書くと検査が鳴る。**
   - ✅ 正: `The style permits a dolly, a crane and a Steadicam, and this shot spends the dolly — …`
     そのうえで辞める場合も**句点・ダッシュ・コロンの後**に置く（`… holds. No crane is used.`）。
   - ⛔ 誤: `no dolly, no crane, no Steadicam`（1つも許されていないと読まれる）
6. **`world_rules` と `visual_language` の共通部は `common.py` のもの。**
   ⚠️ **`Texture` / `Visual Density` / `Atmosphere` は、場所が `s05` の岸と違うなら必ず上書きする**
   ——既定値は岸（濡れた小石・肌・水面）を書いている。**洞窟・海・舟の置き場・沈んだ場所では必ず書き換える。**
7. **数を書くときは記録から測る。** 記録に無い数・「最も」「唯一」「〜に次ぐ」を書かない。
8. **`coexisting-realities` を名乗る4本**（`s07`・`s15`・`s22`・`s29`）は、
   カードの指示どおり**§15 が何を免除しているかを名乗る**（枠そのものの場所と時刻）。
   この4本は `SEEDANCE 2.5` では**カードが言う「正面衝突」の側である**——その事実も書く。
9. **日本語で書く。** ただし §18 の7スロットと、`master`/`visual_scene`/各プロンプトは英語。
10. **句点の後に `**` の並びを壊さない。** markdown として読める形にする。

## 4. 手順

```bash
cd projects/odyssey/generator
python3 gen.py sNN          # 自分のショットを1本ずつ。assert が落ちたら直す
python3 verify.py           # 全既存ショットの不変量。FAILURES を出すな
```

`gen.py` は `duration`・`format` がショット記録と食い違えば落ちる。
`verify.py` は §18 の2ブロック・4定数・7スロット・英語性を確かめる。

**最後に担当ぶんすべてを `gen.py` に通し、`verify.py` が `all invariants hold` を出すことを確認して報告する。**
報告には: 書いたショット、行数、`verify.py` の出力、判断に迷った点を書く。
