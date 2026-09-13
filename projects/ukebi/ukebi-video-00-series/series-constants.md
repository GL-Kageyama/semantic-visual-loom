# シリーズ定数 — 受け火 全12本 / Wan 3.0

> **これは第0話ではない。** 全12本が共有する不変部（§1–6・§15・§17・Negative）を一箇所に置いた台帳。
> 各セグメントの `wan-spec.md` は §7–20（その1本だけの設計）を持ち、不変部はここを参照する。
>
> **貼るときはここを開かなくていい。** 各セグメントの `paste.md` は単体で完結している（不変部はプロンプト本体に毎回書き込まれている——独立生成をまたぐ identity lock がまさにそれ）。

---

## 再配分の原則（2026-08-29）

原典は11章（序章＋第1〜8章＋終章＋最終空白頁）の連作短篇。各章は約700〜1130字の自己完結した短篇で、台詞はほぼ無く、一つの器官が一度だけ止まる「転」を核にする。

- **言葉が少ないから、話を割らない。** ただし序章（八器官の総覧＋喉の留まり）と第8章（背を向ける→振り返る）だけは、一つの章の中に「転」が二つあるため **2本ずつ** に割る。
- **1本＝1つの「転」**＝1器官の所作。場面・感情・所作が一度だけ変わる単位で切る。
- **切れ目は「引き」で切る**。各本の末尾は、答えでなく問い・静止・定型句。原典の「章末の引き」をセグメント粒度へ拡張した。
- **最終空白頁は終章に統合**（S12）。二人称の読者介入は S12 末尾で完結する。

---

## §0 対応表 — 原典11章 → 新12本

| 原典 | 本数 | セグメント（切れ目） |
|---|---|---|
| 序章「迎え火」 | 2 | 01 八器官の総覧 ／ 02 喉の奥の留まり |
| 第1章「送る」／手 | 1 | 03 手が止まる |
| 第2章「綴じる」／指 | 1 | 04 指が止まる |
| 第3章「呑む」／喉 | 1 | 05 該当なしの席 |
| 第4章「預かる」／腕 | 1 | 06 膝の上 |
| 第5章「測る」／耳 | 1 | 07 手首をつかまれる |
| 第6章「値付ける」／目 | 1 | 08 額の判 |
| 第7章「悼む」／声 | 1 | 09 悼まれることを払いのけない |
| 第8章「捨てる」／背 | 2 | 10 背の向こうに篠宮花 ／ 11 目が初めて花を見る |
| 終章「該当なし」＋最終空白頁 | 1 | 12 頁の外へ／受け火は、あなただった |

| S | フォルダ | 器官（所作） | ゲスト／主 | 引き（切れ目） |
|---|---|---|---|---|
| S01 | ukebi-video-00/seg-01 | 八器官の総覧（手→背、淀みない） | あなた（二人称） | 喉の奥に何かが留まっているのを見てしまう |
| S02 | ukebi-video-00/seg-02 | 喉（留まり） | あなた（二人称） | 定型句 |
| S03 | ukebi-video-01/seg-01 | 手（すくう→送る→止まる） | 幸恵 | 手が止まる・定型句 |
| S04 | ukebi-video-02/seg-01 | 指（綴じる→読むを知る→止まる） | 結城文 | 指が止まる・定型句 |
| S05 | ukebi-video-03/seg-01 | 喉（呑む→動かない） | 名なしの胎児／少女初出 | 該当なしの席に少女・定型句 |
| S06 | ukebi-video-04/seg-01 | 腕（預かる→止まる） | コダマ／少女 | 「あんたを預からせて」・定型句 |
| S07 | ukebi-video-05/seg-01 | 耳（測る→止まる） | 少女 | 手首をつかまれる・定型句 |
| S08 | ukebi-video-06/seg-01 | 目（値付ける→止まる） | 折笠千代／少女 | 額に「該当なし」の判・定型句 |
| S09 | ukebi-video-07/seg-01 | 声（悼む→止まる） | 早瀬甚吾／少女 | 悼まれることを払いのけない・定型句 |
| S10 | ukebi-video-08/seg-01 | 背（捨て返そう→背を向ける→止まる） | 少女 | 背の向こうに「篠宮花、という」 |
| S11 | ukebi-video-08/seg-02 | 背→目（振り返る→見る） | 少女 | 目が初めて花を見る・定型句（震え） |
| S12 | ukebi-video-09/seg-01 | 全器官停止→口が開く | 少女 | 頁の外へ／「受け火は、あなただった」 |

> セグメント番号は**通し番号（01–12）**。フォルダは `ukebi-video-{原典章:02d}/seg-{セグメント内番号:02d}`（例 `ukebi-video-08/seg-02`）。ファイル単体でも `ch08-seg02` と分かるよう、各 wan-spec の §19 に通し番号を明記する。

---

## §0.5 画面文字一覧（各セグメントが映す、世界に実在する文字）

物語の証拠は世界の中の文字である。**台帳・秤・判・頁に実在する文字だけ**を画面に映す。各行は character-for-character、一文字も変えない。

| S | セグメント | 画面文字（原典に忠実） |
|---|---|---|
| S01 | 八器官の総覧 | （なし） |
| S02 | 喉の奥の留まり | （なし） |
| S03 | 手が止まる | 台帳の一行 `幸恵` |
| S04 | 指が止まる | 台帳の一行 `結城文` ／ 一番下の欄だけ白い |
| S05 | 該当なしの席 | 台帳の印 `該当なし` |
| S06 | 膝の上 | （なし） |
| S07 | 手首をつかまれる | 秤の印 `該当なし` |
| S08 | 額の判 | 判 `該当なし`（額に） |
| S09 | 悼まれることを払いのけない | （なし） |
| S10 | 背の向こうに篠宮花 | （なし） |
| S11 | 目が初めて花を見る | （なし） |
| S12 | 頁の外へ | 頁の一行 `彼は＿＿＿に受け取られた。` |

- **定型句** `この魂は、まだ誰にも名付けられていない。` は**画面文字ではない**。地の文＝境の地の声の、近くて遠いささやき（ナレーション）として、各章の引きに重なる。S02〜S09 と S11 の引きに現れる。S01・S10 は章の途中のため現れない。S12 で解消される（代わりに「花は、花に、名付けられた」という声）。
- 定型句の**指示先は章ごとにずれる**。前半（S02〜S05）はゲストの魂を指すように聞こえ、第8章（S11）で震え、終章で初めて**送り火自身と花**を指していたとわかる。各セグメントはこのずれを意識してナレーションの温度を微調整する。
- 原典草稿と照合し、食い違ったら**草稿を正**とする。

## この作品の視覚の背骨 — 八器官（12所作）

12本を貫く反復は出来事ではなく**ひとつの器官の所作**である。各セグメントの設計はこの列のどこに位置するかを必ず自覚すること。八器官＝八動詞の対応は絶対に崩さない：**手＝送る／指＝綴じる／喉＝呑む／腕＝預かる／耳＝測る／目＝値付ける／声＝悼む／背＝捨てる**。

| S | 器官がしていること |
|---|---|
| 01 | 手すくう→指頁をめくる→喉上下→腕抱える→耳傾く→目透かす→声低く響く→背見送る（淀みない・迷いない）。その横をあなたが見て、喉の留まりに気づく |
| 02 | 火でも魂でもない何かが喉の奥で燃える。送り火は気づかない。あなただけが見ている |
| 03 | 手で火をすくい、掲げ、流れへ送る（淀みない）→ 問いが手のひらへ戻る → 手が喉の奥に触れる → **止まる** |
| 04 | 指で台帳を開き、名を記す（結城文）→ 頁を閉じる → 白紙の頁 → 「読んで」→ 読めない → **指が止まる** |
| 05 | 喉で火を呑む → 喉が上下 → **喉が動かない**（八器官・初の停止）→ 台帳の一番下に「該当なし」→ その席に少女 |
| 06 | 腕でコダマの火を抱える → 「あなたは、誰かに預けられたことがあるか」→ **腕が止まる** → 花「代わりに、あんたを預からせて」→ 膝の上へ |
| 07 | 耳で秤の針を聞く → 少女の重さで針が振れず「該当なし」→ 少女が秤を降り、彼の手首をつかむ → **耳が止まる** |
| 08 | 目で火を透かして値付ける → 少女に値がなく「該当なし」→ 判を下ろせない → **値付けを止める** → 少女が判を奪い、額に押す |
| 09 | 声で名を乗せて悼む → 少女「あなたを悼む声がない」→ **声が止まる** → 悼まれることを初めて払いのけない |
| 10 | 背で花を流れへ捨て返そうとする → 背を向ける → 背の向こうに篠宮花 → **背が止まる** |
| 11 | 振り返る → **目が初めて花を見る**（値付けの目でなく、ただ見る。初の、彼から彼女への器官の動き） |
| 12 | 八器官すべて止まる → ただの男 → 息 → 「なんと呼ばれたい」→ 口が開く → 「花」→ 花は花に名付けられる → 送られる（頁の外へ） |

---

## ⑧忠実の中枢 — 受け火開示台帳（12段階）

原作は少女を**段階的にしか開示しない**。第3章で「少女」として現れ、第8章で「篠宮花」と名と正体（＝送り火が最初に捨てた半身）を開示し、終章で送り火が「花」と名付ける。各セグメントの §16 MUST NOT はこの表から引く。**先の状態を前のセグメントで出してはならない。**

| S | 花 | 額の判 | 開示されること |
|---|---|---|---|
| S01 | **不在**（喉の留まり＝処理不能の異物。姿は出さない） | なし | — |
| S02 | **不在** | なし | — |
| S03 | **不在** | なし | 台帳「幸恵」 |
| S04 | **不在** | なし | 台帳「結城文」・一番下の白い欄 |
| S05 | **初出**（少女・制服・名なし。「該当なし」の席に座る） | なし | 台帳「該当なし」 |
| S06 | 在（隣に立つ → 膝の上に預かる） | なし | — |
| S07 | 在（秤から降り、手首をつかむ） | なし | 秤「該当なし」 |
| S08 | 在（判を奪い、額に押す） | **有**（額の淡い四角い判「該当なし」） | 判「該当なし」 |
| S09 | 在（悼む） | 有 | — |
| S10 | 在（背の向こう） | 有 | **「篠宮花、という」名 ／ 花＝最初に捨てた自分（半身）** |
| S11 | 在（目が見る） | 有 | 開示済み |
| S12 | 在（名を問う → 花と名付ける） | 有 | 「花は、花に、名付けられた」／受け火 |

### 花の不変則（全12本共通）

- **第3章（S05）までは、少女の姿を一切出さない。** S01〜S04 の §16 MUST NOT 先頭に `no girl, no schoolgirl, no sailor uniform, no long dark hair, no second person, no female figure, no silhouette of another person, no reflection of a girl` を置く。
- 初出（S05）では「少女・制服」であり、**名前も正体もまだ無い**。「篠宮」も「花」も言わない。ただ該当なしの席に座り、送り火を見ている。
- **顔は送り火に似せない。** 写し・反射・同一人物の示唆をしない。花が誰の写しでもないことは不変則（S10 で「捨てた半身」とわかっても、それは顔の相似ではない）。
- 呼称は第8章まで「少女」。S10 で「篠宮花」、S12 で送り火の口から「花」。
- 台詞は短く芯がある。数えるほどしかない：S06「代わりに、あんたを預からせて」／S07「あなたの重さは」／S09「あなたを悼む声がない」／S12「あんたは、なんと呼ばれたい」。

### その他の人物・魂火の開示

- **幸恵**（第1章/S03）——旅路で斃れた女。土の色の魂火。行く先を見失った火。
- **結城文**（第2章/S04）——一度も読まれなかった作家。ペンだこの魂火。
- **名なしの胎児**（第3章/S05）——名前のつく前に捨てられた魂。どの火より小さい。
- **コダマ**（第4章/S06）——引き取り手のない孤児。伸ばしたままの両手の魂火。
- **折笠千代**（第6章/S08）——生涯「無価値」と値踏みされた女。伏せた目の魂火。
- **早瀬甚吾**（第7章/S09）——独り死んだ兵。誰にも見送られなかった死体の重さの魂火。

---

## §1 VIDEO（全本共通）

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold one chapter (one organ, one reversal) of an 11-chapter short-story cycle into a single 30-second take that ends on its pull`
- Register: `Restrained and spare. Emotion is never named — it surfaces through the body (a hand stopping, a throat that will not swallow, a scale that will not tilt). The horror and the tenderness both live in ordinary objects and withheld action`
- Rule: `One organ = one turn. The arc is distributed across 12 takes; nothing is added after the pull`

---

## §2 WORLD（全本共通）

## World Concept

- Concept: `A boundary at a railroad crossing that leads nowhere, where a nameless man sends the dead to the other world with eight organs of his own body — each organ a verb: hands that send, fingers that bind, a throat that swallows, arms that hold, ears that measure, eyes that price, a voice that mourns, a back that discards`
- Era: `Timeless — the dead of every era mingle at the same crossing`
- Location: `A railroad crossing whose rails reach no station, no town; a barrier raised that never lowers`
- Time: `Time does not flow. There is no morning; only the hour work begins`
- Weather: `No rain falls, yet the air is damp; every sound is far away`
- Atmosphere: `Sparse, still, low-saturation deep indigo and rust red, lit only by the pale blue-white soul-fires`

## World Rules

- **根本律**：送ることは、受け取られることに先立たれる。（All sending is preceded by being received. 送り火は送るばかりで、送られたことが一度もない。）
- 八器官＝八動詞。ひとつの魂を、ひとつの器官で、ひとつの動詞で処理する。どの器官にも淀みがなく、どの動きにも迷いがない。
- 超常は**演じない、記録する**。その証拠は台帳・秤・判という世界の物と、青白い魂火だけ。
- 魂火が唯一の光源。物理世界は何も反応しない——風も、動く影も、乱れる物もない。音はみな遠い（台帳の紙の「かさり」だけが聞こえる）。
- 現世の断片（盆・夏）は匂わせるだけで描き込まない。

## Visual Language

- Art Direction: `Soft cel anime — flat color planes, clean closed thin lineart, soft-edged shadow terminators`
- Color Language: `Muted, low-saturation. The world is deep indigo and rust red. The soul-fire's pale blue-white is the only bright value — and the only light source. 火は青白いのに赤くも見える（青と赤のあいだでゆらゆら揺れる）`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces. 濡れていないのに濡れて見える——錆の赤も、花の制服も、空気も`
- Rendering: `Two-step cel shading with softened terminators; faint haze in the damp air; the soul-fire glows without bloom or lens flare`
- Visual Density: `Low. One focal point per beat. Generous negative space. Nothing is crowded`

---

## §3 SUBJECTS（全本共通の identity lock）

### 送り火（OKURIBI）

- ID: `OKURIBI` / Name: `送り火（名を持たない）` / Type: `CHARACTER` / Role: `Protagonist — 境界の主、八つの器官で魂を転生へ送る装置`
- ただの男。若くも老いていない。**目を引くものが何もない**——無名性そのものが外見。
- 藍黒の短髪、目立たない顔、藍の外套。
- 開いた手が火をすくう（ぬくもりが残る）。手は「すくう」ための手で、すくわれたことがない。
- 額に淡い四角い「該当なし」の判（**第6章/S08以降のみ**——それまでは額に何もない）。
- Personality: `名指さない、静か。感情を名指ししない。答えというものを持っていない`
- Typical Motion: `八器官の儀礼だけが動く。それ以外はほぼ静止`
- Emotional Range: `抑圧。顔に読み取れる感情は出さない。反応は静止として現れる（手が止まる、喉が動かない）`
- **Must preserve across every take**: 顔・髪・体格・年齢・藍の外套・無名性（目を引くものがないこと）。額の判は S08 以降のみ。

### 花（HANA）（第3章/S05以降のみ）

- ID: `HANA` / Name: `篠宮花（第8章/S10まで「少女」）` / Type: `CHARACTER` / Role: `「該当なし」の魂——送り火が最初に捨てた半身`
- 濃い藍のセーラー服。**乾いているのに、濡れているように暗い**布地（雨は降っていないのに）。
- 長い濃い藍の髪。静かに見つめる目。境で、誰も彼を見たことがなかったのに、彼女だけが彼を見ていた。
- 台詞は短く芯がある（S06/S07/S09/S12 の四句）。
- Behavior: `見つめる。静かに。芯が強い。送り火を問う（名を・重さを・悼みを）`
- Continuity: 出現は S05 以降（開示台帳）。**送り火に似せない**——写し・反射・同一人物の示唆をしない。花が誰の写しでもないことは不変則。

### 魂火（TAMABI）

- ID: `TAMABI` / Type: `SUBJECT（死者の魂）` / Role: `送られる魂`
- 青白い火。**人のかたちをしていない**。それでも、火を見るとその人の死に方がわかる。
- 火のなかに死に方が入っている——歩き疲れた旅人には土の色、読まれなかった書き手にはペンだこ、抱かれなかった子には伸ばした両手。
- 青白いのに赤くも見える。青と赤のあいだでゆらゆら揺れる。重さはなく、すくう手にぬくもりが残る。

### Supporting（一話の魂火）

- `SACHI` 幸恵（S03）——土の色。行く先を見失った火。
- `YUKI` 結城文（S04）——ペンだこ。頁をめくりたがるように揺れる火。
- `UNNAMED` 名なしの胎児（S05）——どの火より小さい。ころがって足元に止まる火。
- `KODAMA` コダマ（S06）——伸ばした両手。抱き上げてもらうのを待つ火。
- `CHIYO` 折笠千代（S08）——伏せた目。値をつけられない日々の火。
- `JINGO` 早瀬甚吾（S09）——独りの重さ。誰にも見送られなかった火。

---

## §4 ENVIRONMENT（全本共通）

- `踏切` — 駅にも町にも続かない線路、誰も渡らない踏切、錆の赤が光るレール、上がったまま動かない遮断機。上がった遮断機の影が線路の上に黒く落ちている。雨は降らないが空気は濡れ、音はみな遠い。時間が流れない。
- `線路` — 錆の赤。レールの先は流れへ続く（魂が送られる先）。向こうが少しだけ明るくなる。
- `台帳` — 乾いた紙。頁をめくるたび「かさり」と音がする（境で唯一の音）。魂の名が一行ずつ記される。**一番下の欄だけはいつも白い。**

Environmental behavior, all takes: `Wind: none. Particles: only the faintest haze in the damp air. No dust motes, no floating lights, no VFX. Background motion: almost none; time does not flow. Sound: all distant except the dry rustle of the registry's page`

---

## §5 OBJECTS（全本共通の中核）

- `魂火` — 青白い火。唯一の光源。人のかたちをしていない。`CRITICAL`（火のなかの死に方＝土の色・ペンだこ・伸ばした両手は各章で変わる。序章の三例＋各ゲストのそれを守る）
- `台帳` — 名を綴じる本。乾いた白い紙、墨の字。名前と「該当なし」の印がここに記される。**世界に実在する文字が現れる唯一の面（§0.5）**
- `秤` — 魂の重さを測る。皿・針。針の傾く音で重さを知る。重い魂は遠く、軽い魂は近く。値のない魂には針が振れず、まっすぐ真上を指す
- `判` — 額に押す四角い印。押されると冷たい。第6章（S08）で少女が奪い、送り火の額に「該当なし」と押す

---

## §6 REFERENCES（全本共通）

- `REF_STYLE` — `references/styles/soft-cel-anime.md` · `HIGH`。Defines rendering, palette discipline, lineart weight, shading steps, motion idiom (holds, twos and threes). Does **not** define events, identity, or emotional tone
- `REF_FORMAT` — `references/formats/video-spec.md` · `HIGH`。Defines the §1–20 skeleton, uneven density, the identity lock, the six §18 slots
- `REF_SOURCE` — `soul-voice-teller/examples/ukebi/草稿/draft_NN` · `CRITICAL`。Defines every event, the exact on-screen text, the ending line, and **what is and is not revealed**
- `REF_BIBLE` — `soul-voice-teller/examples/ukebi/台帳/series-bible.md` · `CRITICAL`。Defines the staged disclosure, the voice rules, and the organ ledger

---

## §15 CONTINUITY — 独立生成をまたぐ identity lock

12本は12回の独立した生成である。モデルは前の話を覚えていない。**各セグメントの §18 プロンプトには、以下が毎回まるごと書き込まれていなければならない。**

- **Identity**: 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. (S08+) a faint pale square seal on his forehead reading 該当なし
- **花 (S05+)**: a high-school girl in a dark-indigo sailor uniform whose fabric reads damp-dark as if wet though the rain never falls on her. Long dark indigo hair, a quiet steady gaze that watches. She must never resemble 送り火
- **The stage**: a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls
- **The light law**: the soul-fire's pale blue-white is the only light and the only bright value; everything else is deep indigo and rust red
- **The palette law**: muted, low-saturation everywhere; the pale blue-white soul-fire is the only bright value
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the organ's gesture
- **The sound law**: no sound except the dry rustle of the registry's page (and, in S12, the man's own breathing)

---

## §17 GENERATION PRIORITIES（全本共通）

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows (花's absence before S05, her name and identity before S10, the seal before S08). This outranks everything, including beauty
2. **Identity stability** — 送り火's face must not drift across a cut; 花 must never resemble 送り火
3. **The exact Japanese on-screen text** — 台帳・秤・判・頁の文字は証拠。unreadable なら作品は失敗
4. **The uneven density** — the organ's stop (the turn) must visibly hold the largest share of the 30 seconds
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality
6. **The style** — flat cel planes, soft light, limited animation
7. Everything else

---

## Negative（全本共通の土台）

各セグメントはこれを土台にし、その本の禁止（受け火開示台帳の「花 不在」の列）を**先頭に**足す。

```
no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges
```

---

## 語り・態（全本共通の演出方針）

- 語り手は「境の地の声」——名を呼ばずに語れる距離。感情を名指ししない。
- **序章（S01・S02）と最終空白頁（S12末尾）のみ二人称「あなた」**。第1〜8章・終章は**三人称制限**（送り火の内側に寄り添う）。
- **能動態→受動態の傾斜**：カメラと所作が、送り火を「送る主体」から「受け取られる宛先」へと章ごとに移す。S03〜S05 は送り火の手・指・喉が主体（能動）。S06〜S07 は預かり・測られる（受動のはじまり）。S08〜S09 は判を押され・悼まれる（受動）。S10〜S12 は背を向け・見て・呼ばれ・送られる（全受動）。
