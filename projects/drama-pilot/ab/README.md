# 盲検 A/B — `s04` の1本

**この作品の値の転換が起きる1本で、`## DIRECTION` が効くかどうかだけを測る。**

⚠️ **測っているのは「演出の節が生成器に届くこと」の効果であって、作品全体の効果ではない。**
1 組の結果は証拠ではない——**証拠は組数である。** それでも、最初の1組を取らない者は
2 組目を持たない。

---

## 何を比べるか

| | ファイル | `## DIRECTION` | 生成時に Master の先頭へ |
|---|---|---|---|
| **新** | [`../specs/video/drama-pilot-s04.md`](../specs/video/drama-pilot-s04.md) | 在る | **連結される** |
| **旧** | [`old-drama-pilot-s04.md`](old-drama-pilot-s04.md) | 無い | — |

⚠️ **2本は `## DIRECTION` 以外、1バイトも違わない。** 対照は本編の写しであり、
写し直したのは 2026-10-29 である。**本編が変わったら、写しも取り直す**——
さもなければ A/B は「節の効果」ではなく「二つの版の差」を測ることになる。

⚠️ **経路・尺・様式・Negative・キー画像（あれば）を揃える。** 揃えられない条件が
あれば、**その組は捨てる**——**揃っていない組は、A/B ではない。**

⚠️ **生成はこのリポジトリの外で起きる。** ここにあるのは仕様と手順だけである。

---

## 手順

```sh
cd projects/drama-pilot/ab
mkdir -p pair-1

# 1. 2本を生成し、`pair-1/new.mp4`（新）と `pair-1/old.mp4`（旧）に置く。
#    新: `../specs/video/drama-pilot-s04.md` ＋ `## DIRECTION` を Master の先頭へ
#    旧: `old-drama-pilot-s04.md`（`## DIRECTION` を連結しない）

# 2. 伏せる。原ファイルの写しが .raw/ に残り、A.mp4 / B.mp4 が無作為に置かれる。
/opt/homebrew/bin/python3.12 - <<'PY'
import random, shutil, pathlib
d = pathlib.Path("pair-1")
raw = d / ".raw"
raw.mkdir(exist_ok=True)
for n in ("new", "old"):
    shutil.copyfile(d / f"{n}.mp4", raw / f"{n}.mp4")
order = random.sample(["new", "old"], 2)
shutil.move(str(d / f"{order[0]}.mp4"), str(d / "A.mp4"))
shutil.move(str(d / f"{order[1]}.mp4"), str(d / "B.mp4"))
(d / "codebook.txt").write_text(
    f"A = {order[0]}\nB = {order[1]}\n", encoding="utf-8")
print("A と B を置いた。⚠️ codebook.txt と .raw/ は、選んだ後に開く。")
PY
```

⚠️ **`codebook.txt` と `.raw/` を、選ぶ前に開かない。** 開けば、その組は盲検ではない——
**開いてしまった組は、捨てる。** 記録に「開いた」と書けば済む話ではない。
**盲検は、記録の正しさではなく、選択の独立性である。**

---

## 何を見て選ぶか

1. **もう一度見たいのは、どちらか。**
2. **明日、どの1枚を覚えているか。**（24時間後に書く。**当日に書かない。**）
3. **人に見せるなら、どちらか。**

⚠️ **「仕様に忠実なのはどちらか」で選ばない。** それは原作者の仕事ではなく、
`L11`–`L39` の仕事である。**ここで測るのは、届いたかどうかである。**

⚠️ **違いが分からなければ、そう書く。** 「差が無い」は失敗ではなく、
**この節が効かないという測定値である。** 差を無理に作れば、測定値が消える。

---

## 記録

`pair-1/result.md` に書く（`codebook.txt` を開く前に、1〜3 を書く）。

```markdown
# pair-1 — s04

- 選んだのは: A / B / 差が無い
- 理由（1〜2行）:
- 24時間後に覚えていた1枚: ／ 何も覚えていない
- 経路: WAN 3.0
- 生成日: YYYY-MM-DD
- 揃えた条件: 尺 9s・様式 luminous-anime・Negative は両者同一・キー画像なし
- ⚠️ 揃えられなかった条件:

## 正体（選択を書いた後に開く）

- A = ／ B =
```

⚠️ **採用はここでは決めない。** 採用は `takes/` に著者が書く行為である——
**A/B は選別の材料であって、選別そのものではない。**
