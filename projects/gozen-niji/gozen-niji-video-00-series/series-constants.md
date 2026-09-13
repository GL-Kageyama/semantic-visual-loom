# シリーズ定数 — 午前二時に、あなたは誰の時間を生きていますか 全57本 / Wan 3.0

> **これは第0話ではない。** 全57本が共有する不変部（§1–6・§15・§17・Negative）を一箇所に置いた台帳。
> 各セグメントの `wan-spec.md` は §7–20（その1本だけの設計）を持ち、不変部はここを参照する。
>
> **貼るときはここを開かなくていい。** 各セグメントの `paste.md` は単体で完結している（不変部はプロンプト本体に毎回書き込まれている——独立生成をまたぐ identity lock がまさにそれ）。

---

## 再配分の原則（2026-08-29 再構成）

旧構成は「原典1話＝1本の30秒」で、1本の中に複数場面（深夜→朝→学校）と複数行の画面文字と台詞を折り畳んでいた。これは詰め込みで、画面の文字が読めず、余白が消え、話の筋まで失われる。

新構成は **「原典1話を、その内部の「転」ごとに30秒×複数本へ再分割」** する。

- **1本＝1つの「転」**。場面・感情・所作が一度だけ変わる単位で切る。
- **切れ目は「引き」で切る**。各本の末尾は、答えでなく問い・静止・画面の一行。原典の「話末の引き」をセグメント粒度へ拡張した。
- **画面文字は1本につき1つの「やりとり」**（1行〜数行の1回の表示。送信＋返信の1往復は許すが、同時に何往復も詰めない）。物語に必要な行は、それぞれ自分の1本を得る——詰め込むのでなく**配る**。
- **指の所作（②選択）を57本で引き直す**。第1話の「止まる」が第35本で反転し、第38本で「押す」に変わり、第54本で「打つ」に着地する。

---

## §0 対応表 — 原典12話 → 新57本

| 原典 | 本数 | セグメント（切れ目） |
|---|---|---|
| 1 午前二時、あなたのスマホは他人のもの | 5 | 01 撫でる指 ／ 02 午前2時の通知 ／ 03 宛先は自分自身 ／ 04 消えた記録 ／ 05 待つ |
| 2 おまえが言えなかった、たった一言 | 4 | 06 雰囲気変わった？ ／ 07 ありがとう、いつもごめんね ／ 08 ……嬉しい ／ 09 枕の横 |
| 3 午前二時の幽霊の名前 | 4 | 10 画面の中の何か ／ 11 預けた時間 ／ 12 ニジ ／ 13 返してくれたら帰れる |
| 4 現実を生きるほど、増える | 4 | 14 触ったら負け ／ 15 会話と部活 ／ 16 領収書 ／ 17 どうせ |
| 5 届いた、届いていない、の狭間で | 4 | 18 小春のお辞儀 ／ 19 だから、届けたんだよ ／ 20 美月 ／ 21 次は、おまえが届けなよ |
| 6 宛先リスト、三十二人 | 5 | 22 三十二人 ／ 23 名前が流れる ／ 24 一番上の名前 ／ 25 最後に返すといいよ ／ 26 すれ違い |
| 7 文化祭前夜、スクリーンタイムを全部開く | 5 | 27 文化祭前夜 ／ 28 全部開く ／ 29 逃げた時間は、ひとつもなかった ／ 30 ひとつも無駄じゃなかったよ ／ 31 わたしは |
| 8 わたしは、おまえが預けた時間 | 4 | 32 集まった姿 ／ 33 受け取らなかった感情 ／ 34 返すの ／ 35 最初の宛先 |
| 9 届かなかった言葉を、いま | 5 | 36 指が、止まった ／ 37 ……無理だよ ／ 38 送信を押す ／ 39 既読が付いた ／ 40 返すと、薄くなる |
| 10 疎遠になった、あの人のところへ | 5 | 41 下から返していく ／ 42 あの子 ／ 43 打っては消して ／ 44 届いてる ／ 45 あと一つ |
| 11 最後の宛先、湊 | 6 | 46 屋台の灯り ／ 47 声をかける ／ 48 時間を預けてました ／ 49 湊も預けてる ／ 50 ちゃんと生きてたよ ／ 51 残る記録は、ひとつ |
| 12 また明日 | 6 | 52 最後の記録 ／ 53 宛先は、自分 ／ 54 返すよ ／ 55 返せた ／ 56 行ってらっしゃい ／ 57 また明日 |

> セグメント番号は**通し番号（01–57）**。フォルダは `gozen-niji-video-{原典話:02d}/seg-{セグメント内番号:02d}`（例 `gozen-niji-video-01/seg-03`）。ファイル単体でも `ep01-seg03` と分かるよう、各 wan-spec の §19 に通し番号を明記する。

---

## §0.5 画面文字一覧（各セグメントが映す、たった1つの「やりとり」）

物語の証拠は画面の文字である。各行は**自分の1本**を得る。文字は1本につき1交換。カメラは一度、大きく、静止して映す。

| # | セグメント | 画面文字（原典に忠実・character-for-character） |
|---|---|---|
| 01 | 撫でる指 | （なし——UIの「いいね 23」と既読のままの3トークのみ） |
| 02 | 午前2時の通知 | `午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ` |
| 03 | 宛先は自分自身 | `おまえが私にくれた時間、私が生きてるよ。` |
| 04 | 消えた記録 | （なし——設定画面の合計から1時間21分だけ抜けている数字） |
| 05 | 待つ | `おまえ、いま、起きてるんだろ。` |
| 06 | 雰囲気変わった？ | （なし——美月の表情と問い） |
| 07 | ありがとう、いつもごめんね | `ありがとう、いつもごめんね。` |
| 08 | ……嬉しい | （なし——美月の笑顔。送信済みの文字は07で既出） |
| 09 | 枕の横 | `おまえの代わりに、届けたよ。` |
| 10 | 画面の中の何か | （なし——虹色の残像が輪郭を得る） |
| 11 | 預けた時間 | （なし——対話のみ） |
| 12 | ニジ | （なし——名前の瞬間） |
| 13 | 返してくれたら帰れる | （なし——対話のみ） |
| 14 | 触ったら負け | （なし——伏せたスマホ） |
| 15 | 会話と部活 | `会話 ／ 部活`（アプリ欄にアプリ名でなく「会話」「部活」） |
| 16 | 領収書 | （なし——対話のみ） |
| 17 | どうせ | （なし——対話のみ） |
| 18 | 小春のお辞儀 | （なし——学校シーン） |
| 19 | だから、届けたんだよ | `相談してくれて、ありがとう。ちゃんと、読んだよ。私の言葉で、きっと、大丈夫。` ＋小春の返信 `ありがとうございます！　ちょっと、元気出ました！　真白さん、優しいんですね。` |
| 20 | 美月 | `真白、最近、なんか変だよ？ ／ ありがとう、いっぱい送ってくるの、やめてくんない？（笑）` |
| 21 | 次は、おまえが届けなよ | （なし——対話のみ） |
| 22 | 三十二人 | `美月…………3時間14分 ／ お母さん……1時間02分 ／ 小春…………0時間47分` |
| 23 | 名前が流れる | （なし——リストが流れる。名前の列） |
| 24 | 一番上の名前 | `氷室湊……4時間52分` |
| 25 | 最後に返すといいよ | （なし——対話のみ） |
| 26 | すれ違い | （なし——湊の背中） |
| 27 | 文化祭前夜 | （なし——日中・動き） |
| 28 | 全部開く | （なし——設定→スクリーンタイム→宛先リストを辿る指） |
| 29 | 逃げた時間は、ひとつもなかった | （なし——一覧が名前に繋がる） |
| 30 | ひとつも無駄じゃなかったよ | （なし——ニジの笑顔） |
| 31 | わたしは | `わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ`（声） |
| 32 | 集まった姿 | （なし——反芻。輪郭が明瞭） |
| 33 | 受け取らなかった感情 | （なし——対話のみ） |
| 34 | 返すの | （なし——対話のみ） |
| 35 | 最初の宛先 | （なし——小春のトーク。指が止まる） |
| 36 | 指が、止まった | （なし——空の返信ボックス・カーソル点滅） |
| 37 | ……無理だよ | （なし——対話のみ） |
| 38 | 送信を押す | `相談してくれて、ありがとう。遅くなって、ごめんね。` |
| 39 | 既読が付いた | `真白さん、ありがとうございます。 ／ あのときのお礼、言えてなかったんで。――嬉しいです。` |
| 40 | 返すと、薄くなる | （なし——欄が空いた画面＋薄いニジ） |
| 41 | 下から返していく | （なし——短い挨拶を返して欄が空く連なり） |
| 42 | あの子 | `元気にしてますか。急にごめんね。` |
| 43 | 打っては消して | （なし——入力中の文字が出ては消える） |
| 44 | 届いてる | （なし——既読の付かない送信済み。ニジの声） |
| 45 | あと一つ | `ありがとう。 ／ ごめんね、返事、遅れて。――ちょっと、びっくりしちゃって。 ／ あのときのこと、ずっと、気にしてた。――元気そうで、よかった。` |
| 46 | 屋台の灯り | （なし——湊の背中） |
| 47 | 声をかける | （なし——対話のみ） |
| 48 | 時間を預けてました | （なし——対話のみ） |
| 49 | 湊も預けてる | （なし——湊のスマホが少し明るい） |
| 50 | ちゃんと生きてたよ | （なし——対話のみ） |
| 51 | 残る記録は、ひとつ | `午前2時00分〜午前3時21分 ／ 使用時間　1時間21分 ／ アプリ　メッセージ` |
| 52 | 最後の記録 | （なし——ほとんど見えないニジ・白い光） |
| 53 | 宛先は、自分 | （なし——名簿の最後の一行＝自分自身の名前） |
| 54 | 返すよ | `おまえが私にくれた時間、私が生きてるよ。`（今度は真白の指で、一文字ずつ） |
| 55 | 返せた | （なし——白い光が虹色を取り戻す） |
| 56 | 行ってらっしゃい | （なし——虹色が光に溶ける） |
| 57 | また明日 | `今日、あなたが誰かに預けた時間はありません`（下に小さく `また明日`） |

---

## この作品の視覚の背骨 — 指（57所作）

57本を貫く反復は出来事ではなく**ひとつの所作**である。各セグメントの設計はこの列のどこに位置するかを必ず自覚すること。第1本の「撫でる」→第3本の「止まる」→第35本の「触れて止まる（反転）」→第38本の「押す」→第54本の「打つ」→第57本の「閉じる」へ。

| # | 指がしていること |
|---|---|
| 01 | 撫でる（確立。親指が同じ場所を繰り返す） |
| 02 | 目覚め、時計からスマホへ目を移す |
| 03 | **止まる**（核・初の静止。止まったまま持続） |
| 04 | 設定を開く（合計が減っている） |
| 05 | 画面の縁を握る（力が入る） |
| 06 | 美月の開く指を、妙に細かく見る |
| 07 | （美月の）親指がするりと撫でる開き方——第1話の真白と同じ所作 |
| 08 | 画面を開いては閉じる |
| 09 | スマホを枕の**下から横へ**置く |
| 10 | 布団を掴んで、白くなる |
| 11 | （対話。指は休む） |
| 12 | 名前を付ける（指は画面に触れない） |
| 13 | （対話。指は休む） |
| 14 | 伏せたスマホへ伸びて、机の上を**探す** |
| 15 | 記録を手に取る |
| 16 | 画面の上に座るニジを見る |
| 17 | （対話。指は休む） |
| 18 | （小春のお辞儀。指は休む） |
| 19 | トークを開く（送信済みを見る） |
| 20 | 並んだ二つの文字を、目が往復する |
| 21 | （対話。指は休む） |
| 22 | リストに触れて**流す** |
| 23 | リストを流しながら眺める |
| 24 | 湊の名前の上で長く止まる |
| 25 | （対話。指は休む） |
| 26 | （すれ違い。指は休む） |
| 27 | （日中。指は休む） |
| 28 | 設定→スクリーンタイム→宛先リストを、全部開く |
| 29 | また**撫でる**——ただしフィードではなく**名前**を |
| 30 | 一番長く止まる名前（湊） |
| 31 | 初めて真白の目を見る（指は休む） |
| 32 | （対話。指は休む） |
| 33 | 自分の手を見る。指がわずかに透ける |
| 34 | （対話。指は休む） |
| 35 | スレッドに触れて、その上で**止まる**（第3本の止まりの反転——驚きではなく、決めかねて） |
| 36 | 送信ボタンの上で指が浮き、震える |
| 37 | （無理。指が引く） |
| 38 | 初めて**送信を押す** |
| 39 | 開いては閉じる（既読待ち） |
| 40 | （欄が空いた。指は休む） |
| 41 | 下から返していく（短い挨拶を打つ連なり） |
| 42 | あの子の名前の上を長く止まる |
| 43 | 打ち始める・消す・打ち始める・消す（第7本で回想された所作の実演） |
| 44 | 布団の中で**握る**。握った指の間から光がもれる |
| 45 | （返信。指は休む） |
| 46 | （屋台。指は休む） |
| 47 | 湊に声をかける（**手は空**） |
| 48 | （対話。手は空） |
| 49 | （対話。湊のスマホだけが明るい） |
| 50 | 湊が名前を呼ぶ（手は空） |
| 51 | 午前2時、残る記録を開く |
| 52 | ほとんど見えないニジを見る（指は休む） |
| 53 | 名簿の最後の一行＝自分自身の名前に気づく |
| 54 | 第3本と同じ一文を、**自分の指で打つ**（一文字ずつ） |
| 55 | （笑顔を見る。指は休む） |
| 56 | （行ってらっしゃい。指は休む） |
| 57 | スマホを閉じる（光源が画面から窓へ）→ 外へ |

---

## ⑧忠実の中枢 — ニジ開示台帳（57段階）

原作は幽霊を**段階的にしか開示しない**。第10本で姿を見せ、第31本で初めて「わたし」と言い、第52本で白い光になる。各セグメントの §16 MUST NOT はこの表から引く。**先の状態を前のセグメントで出してはならない。**

| セグメント | ニジの視覚状態 | 「わたし」 | 他に映ってよい人物 | 絶対に出してはならないもの |
|---|---|---|---|---|
| 01–05 | **不在**——画面の文字としてのみ | — | なし（04に美月） | 人影・目・反射・**虹色** |
| 06–09 | **不在**——送信済みの文字としてのみ | — | 美月 | 人影・目・**虹色**・ニジの声 |
| 10 | **初登場**。滲んだ虹色→輪郭を得る。真白と同じ顔・一歩幼い・完全に不透明 | いいえ | なし | 透明化・「わたし」・名前を先に呼ぶ |
| 11–13 | 在。不透明 | いいえ | なし | 透明化・「わたし」 |
| 14–15 | **不在**——記録（伏せたスマホ・領収書）のみ | — | なし | ニジの姿 |
| 16–17 | 在。不透明。画面の上に座り、虹色が暗い部屋へふわっと滲む | いいえ | なし | 透明化・「わたし」 |
| 18 | **不在**——学校（小春） | — | 小春 | ニジの姿 |
| 19–21 | 在。不透明 | いいえ | 小春（文字のみ）・美月（文字のみ） | 透明化・「わたし」・ニジが泣くこと |
| 22–25 | 在。不透明。リストを指す | いいえ | なし | 透明化・「わたし」 |
| 26 | **不在**——学校（湊・すれ違い） | — | 湊 | ニジの姿・湊が真白を見ること |
| 27–28 | **不在**——日中／教室 | — | なし | ニジの姿 |
| 29–30 | 在。不透明 | いいえ | なし | 透明化 |
| 31 | 在。**初めて真白の目を見る** | **はい（初の名乗り）** | なし | 透明化・体の消失 |
| 32 | 在。**輪郭がこれまでで最も明瞭** | はい | なし | 全身の透明化 |
| 33–34 | 在 | はい | なし | 全身の透明化・派手な消失演出 |
| 35 | 在 | はい | なし | 全身の透明化 |
| 36–40 | 在 → **薄い**（36–38は不透明、39–40で輪郭がはっきり薄くなる） | はい | 小春（文字のみ） | 完全消失 |
| 41–45 | **輪郭がほとんど消えかけ** | はい | なし（中学の友人は**顔を出さない**） | 中学の友人の顔・姿 |
| 46–51 | **登場しない**（この話にニジはいない） | — | 湊（全編） | **ニジが現れること** |
| 52 | ほとんど見えない → 髪が色を失い**白い光**に | はい | なし | 虹色を出すこと |
| 53 | 白い光のまま | はい | なし | 虹色を出すこと |
| 54–55 | 白い光 → **虹色を取り戻す** | はい | なし | 完全消失 |
| 56 | 虹色が**光に溶ける** | はい | なし | 溶けたあとにニジが残ること |
| 57 | **登場しない**（朝・外） | — | なし | ニジが現れること |

### ニジの不変則（全57本共通）

- **画面の中にいる。** 第16本以降、虹色がガラスの外の暗い空気へわずかに滲み出ることはあるが、**部屋に等身大で立つことは一度もない**。
- 顔は**真白自身の顔**。ただし一歩幼い——まつ毛が長く、頬がわずかにふくらんでいる。首のかしげ方が真白と同じ。**別人のデザインにしてはならない。**
- 呼称は「**おまえ**」。句点で切る。第31本まで主語「わたし」を避ける。
- **泣かない。**「泣き方を知らないでいた」——真白が泣き方を知らないのと同じで。笑う顔に泣きが混じることはあってよい（第12本「泣きそうに笑う」）。
- 虹色は**滲み・残像**であって、光線・パーティクル・オーラではない。青→緑→また青へ、ゆっくり。

### その他の人物の開示

- **美月**（親友）——第6本初出。明るい。真白の嘘を見抜きかけるが踏み込まない。
- **小春**（一年・柴崎小春）——第18本初出。教科書を胸に抱え、**お辞儀の角度がほんの少し浅い**。
- **湊**（三年・氷室湊）——第26本で**すれ違うだけ**（真白を見ない・書類の束）。第47本で初めて言葉を交わす。
- **中学の友人**（無名）——第42本。**最後まで顔を出さない**。名前と文字だけの宛先。

---

## §1 VIDEO（全本共通）

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold one turn (one dramatic beat) of a 57-part light-novel animation into a single 30-second take that ends on its pull`
- Register: `Restrained. The horror and the tenderness are both delivered by ordinary objects and withheld reaction, never by performance`
- Rule: `One turn = one generation. The arc is distributed across 57 takes; nothing is added after the pull`

---

## §2 WORLD（全本共通）

## World Concept

- Concept: `Contemporary Japan, unchanged in every visible way — except that a screen-time log records time as a receipt for time deposited with other people`
- Era: `Present day`
- Location: `A high-school student's small bedroom; her school; occasionally a corridor, a classroom, a festival yard`
- Time: `The story lives at 2:00 A.M. Daytime exists only as the shore on either side of it`
- Weather: `Clear and still. Nothing outside ever comments on the events`
- Atmosphere: `Absolute domestic ordinariness. The anomaly never disturbs a single physical object`

## World Rules

- The supernatural is **recorded, not staged**. Its evidence is text on a screen.
- The phone's light is the sole light source at night. It does not flicker, pulse, or behave unnaturally.
- Nothing in the physical world reacts to the anomaly — no wind, no moving shadows, no disturbed objects.
- Notifications are **silent**. They arrive as light only.
- ニジ never leaves the screen (see the ledger above).

## Visual Language

- Art Direction: `Soft cel anime — flat color planes, clean closed thin lineart, soft-edged shadow terminators`
- Color Language: `Muted, low-saturation. Night = desaturated indigo lit by one cold blue-white screen. Day = pale, slightly overexposed, equally muted. The screen's blue-white is the only value allowed to be bright — and, from seg.10, ニジ's rainbow is the only hue allowed to be saturated`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces`
- Rendering: `Two-step cel shading with softened terminators; gentle bloom around the phone screen; light haze in the dark air`
- Visual Density: `Low. Simple uncluttered rooms, generous negative space, one focal point per beat`

---

## §3 SUBJECTS（全本共通の identity lock）

### MASHIRO

- ID: `MASHIRO` / Name: `真白 (Mashiro)` / Type: `CHARACTER` / Role: `Protagonist — the one who deposited the time`
- Japanese high-school girl, 16–17, second year. Deliberately unremarkable — the girl slightly outside the middle of the circle
- Dark medium-length hair, plain; small frame; quiet face that gives little away
- Back curved from long hours over a phone
- At night: plain pajamas, in a futon on the floor. By day: standard Japanese school uniform
- Personality: `Inward, observant, agreeable on the surface. Reads the room and matches it. Small voice`
- Typical Motion: `Almost nothing moves except her fingers. Her body stays still far more than it moves`
- Emotional Range: `Narrow and suppressed. She does not scream, gasp, or widen her eyes. Her reactions register as stillness — a finger stopping, a held breath`
- **Must preserve across every take**: face, hair length and color, build, age; the curved posture; the same phone (same size, same case); the same futon, room layout, window and curtain; the restraint — her expression never resolves into a clear readable emotion

### NIJI（第10本以降のみ）

- ID: `NIJI` / Name: `ニジ (Niji)` / Type: `CHARACTER (apparition, on-screen only)` / Role: `The ghost of 2 A.M. — the crystallization of feelings 真白 never received`
- **真白's own face, one step younger** — longer lashes, slightly fuller cheeks. The same way of tilting her head
- A blurred rainbow afterimage that resolves into that outline. Colors drift slowly: blue → green → blue
- Exists **inside the screen**. Never stands in the room at human scale
- Behavior: `Bright, teasing, unguarded — she smiles more honestly than 真白 can. She never cries. She calls 真白「おまえ」`
- Continuity: her opacity is a **strict function of the segment number** — see the ledger. It never varies within a beat except in seg.55

### Supporting

- `MITSUKI` 美月 — best friend. Bright, direct, physically easy; slightly shorter, livelier hair, open upright posture. Appears from seg.06
- `KOHARU` 小春 — first-year, smaller and rounder, shoulder-length hair. Holds a textbook to her chest; her bow is slightly too shallow. Appears from seg.18
- `MINATO` 氷室湊 — third-year, festival committee, boys' school uniform. Composed, short neat dark hair, a little taller, carries document bundles. Glimpsed seg.26, speaks seg.47

---

## §4 ENVIRONMENT（全本共通）

- `BEDROOM` — 真白's room. Small, futon on the floor, curtained window, wall clock, desk, few objects. Dark except for the phone. **The recurring stage; most night takes live here**
- `CLASSROOM` — ordinary Japanese classroom, morning light making long thin shadows across desks
- `CORRIDOR` — school hallway, windows throwing white rectangles onto the floor
- `SCHOOL_ENTRANCE` — shoe lockers, pale daylight, blurred students
- `FESTIVAL_YARD`（第46本のみ）— back yard at night, paper lanterns, food-stall smoke and light

Environmental behavior, all takes: `Wind: none — the curtain does not move. Particles: only the faintest haze catching the screen's bloom. No dust motes, no floating lights, no VFX. Background motion: almost none; at most one distant car's headlights crossing the curtain, once`

---

## §5 OBJECTS（全本共通の中核）

- `PHONE` — 真白's ordinary modern smartphone, plain case, Japanese UI. **The only light source at night; the only surface on which the anomaly appears.** Glass carries a soft bloom, never a hard specular glint. `CRITICAL` in all three axes, every take
- `SCREEN_TEXT` — whatever Japanese text that take's disclosure requires, rendered exactly as an ordinary phone would render it: cold blue-white on dark UI. **The exact strings are per-segment and are listed in §0.5.** They must be reproduced character-for-character
- `WALL_CLOCK` — visible second hand, advancing in discrete ticks. Reads 2:00 at the hinge of the night takes

---

## §6 REFERENCES（全本共通）

- `REF_STYLE` — `references/styles/soft-cel-anime.md` · `HIGH`. Defines rendering, palette discipline, lineart weight, shading steps, motion idiom (holds, twos and threes). Does **not** define events, identity, or emotional tone
- `REF_FORMAT` — `references/formats/video-spec.md` · `HIGH`. Defines the §1–20 skeleton, uneven density, the identity lock, the six §18 slots
- `REF_SOURCE` — `soul-voice-teller/examples/gozen-niji/draft_NN` · `CRITICAL`. Defines every event, the exact on-screen text, the ending line, and **what is and is not revealed**
- `REF_BIBLE` — `soul-voice-teller/examples/gozen-niji/series-bible.md` · `CRITICAL`. Defines the staged disclosure, the voice rules, and the addressee ledger

---

## §15 CONTINUITY — 独立生成をまたぐ identity lock

57本は57回の独立した生成である。モデルは前の話を覚えていない。**各セグメントの §18 プロンプトには、以下が毎回まるごと書き込まれていなければならない。**

- **Identity**: 真白 — plain Japanese high-school girl 16–17, dark medium-length hair, small frame, curved posture over a phone. Same face in every take
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen
- **The room**: futon on the floor, curtained window, wall clock, sparse
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers
- **(seg.10+) ニジ**: 真白's own face one step younger, a rainbow afterimage inside the screen, at the opacity this segment requires

---

## §17 GENERATION PRIORITIES（全本共通）

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. This outranks everything, including beauty
2. **Identity stability** — 真白's face must not drift across a cut
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds
5. **Restraint** — no performed emotion, no horror grammar
6. **The style** — flat cel planes, soft light, limited animation
7. Everything else

---

## Negative（全本共通の土台）

各セグメントはこれを土台にし、その本の禁止（ニジ開示台帳の右端の列）を**先頭に**足す。

```
no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain
```
