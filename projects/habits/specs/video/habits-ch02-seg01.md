# MiniMax H3 Full Specification — 『ハビッツ！！！』第二巻第1話「八十軒目」 第一のショット「束が、受付の机から、助手席へ」 / 10s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**

⚠️ **この仕様は MiniMax H3 の経路である。**（`specmap.MODELS`。著者の決定 2026-09-20。
取り込み元は資料『GPTimage2.5×MiniMaxH3による動画化手法』——①絵コンテ画像 → ②その画像を動画にする。）
**§18 の見出しがモデルを名乗る**——`L18` はそこを読む。**ゆえにこのショットは WAN 3.0 の経路を持たない**
——**択一である**（同じショットを両方で撮ることは、まだできない。穴である）。

⚠️ **この経路の添付は `key_image` ではない。** **①で作った絵コンテの画像そのものが、
動画全体の設計として渡る。** ゆえに §6 の `REF_BOARD` は**この経路で最も重い参照である**
——**`key_image` は「1つの瞬間の見た目」であり、ボードは「順序と構図の設計」である。**
（`specmap.MODELS` の `MINIMAX H3` の註。）

⚠️ **①の絵コンテは、まだ無い。** **この仕様は、これから作るボードを前提に書かれている**
——§6 の `REF_BOARD` は**在り処の宣言であって、資産の記録ではない**
（`habits-ch02-seg01.yaml` の「まだ無い。意図であって資産ではない」と同じ扱いである）。
ボードの作り方は `specs/board/habits-ch02-seg01-board.md` に在る。

⚠️ **このサンプルは、著者の裁定の「12コマ」を3枚に分けて持つ**（4＋4＋4）。
**裁定の文面は「1枚のボードに12コマ」であった**——**ずれである。**
理由・宣言・穴は `specs/board/habits-ch02-seg01-board.md` の見出しに書いた。

⚠️ **§18 `Negative Prompt` は、このサンプルの三ショットで同一である。**
理由は豁免ではなく**設計**である——**この三つのショットで、禁止が消える瞬間は一度も無い。**
⚠️ **ただし、それは無理をして揃えたのではない。** **画面に立つ者はショットごとに違う**
（①には受付の人が立つ。②③には誰も立たない）——**ゆえに「他の誰も画面に立てない」は、
この Negative では言えない。** **その禁止は、経路自身の語で負う**——
**「ボードが置いていない者を、足さない」**（資料②の【重要】——「不必要な登場人物や
シーンを追加しない」）。⚠️ **この言い換えが弱いことは、認める。**
**穴である**——**②③の Negative は、忍び込む住人を名指しでは禁じていない。**
**名指しで禁じる版は、`disclosure` の `negative:` を `changed` へ動かすことになる**
（`ledger.yaml` の該当箇所に、両案を書いた）。⚠️ **今回は揃える側を採った。**

⚠️ **人名はローマ字にしない**（決定）。プロンプトの中の「暮林蒼」は**日本語の字のまま置く。**
ゆえに Negative は「**読める名**」を禁じるのであって、**字種を禁じない**——
`no Japanese kanji or kana` は**使わない。使えば、名そのものが消える。**

⚠️ **このショットに、開示の変化点は無い。** 開示の変化点は②である（`ledger.yaml`）。
①は**その手前**であり、宛名票のいちばん上の行は**まだ、目に入っていない**
（`disclosure_state: absent`）。⚠️ **`L10` はこのショットを、動画の仕様を持たない位置として
扱わない**——**§18 が在るからである。** **先行する §18 を持つショットが無いので、
`L10` は註を返す**（「「変わった」を言えない」）。**これは期待どおりである。**

⚠️ **このショットに、音楽は無い。** **床がそれを禁じている**（`specmap.BASE_NEGATIVES` の
`no background music`）——§16 `MUST NOT` と §18 `Negative Prompt` の両方が持つ。
⚠️ **これは「指定しなかった」のではない。** §14 と §18 `Audio Prompt` が
**「このショットは音楽を一切持たない」と明記する**——**無音は、指定によって置かれる。**
⚠️ **当初はこのサンプルに限り床を外していた**（著者の裁定 2026-09-20——「今回だけ」）。
⚠️ **同日のうちに裁定が撤回された**——「**1話を分割するのであれば、やっぱりBGMは禁止しよう**」。
**1話を3回の生成に分ける以上、三つの音の床は継ぎ目で鳴る。** **床は戻っている。**

⚠️ **§2・§3・§4 の日本語の規則と語は、`bible.yaml` と `distill-essence-engine` の設定画から
移し替えたものである。**「一字も変えない」は**日本語の側の約束**であって、
**写しの言語は英語である**（`CLAUDE.md`——文書の正典は英語）。**食い違ったら、家が勝つ。**

---

# 1. VIDEO

- Duration: `10s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One storyboard of four panels read in order, **each panel treated as its own scene and joined to the next by natural animation** (the source's own ②: 「各コマを独立したシーンとして扱い、静止画と静止画の間を自然なアニメーションでつないでください」). **Panels 01 to 03 stand at the counter and panel 04 stands in the van, so the join between 03 and 04 is a cut division** — ⚠️ **the author's ruling (2026-09-20); the source leaves cut-versus-continuous open, and this shot closes it as a cut.** The movement still reads through the division, because the hand that takes the bundle and the hand that sets it down are the same hand. A single change: the bundle of slips is at the edge of the counter and not in his hands, and then it is on the passenger seat and his hands are empty. **The delivery does not complete here.**

# 2. WORLD

## World Concept

2026, Japan. Kawaguchi in Saitama, Adachi in Tokyo, Totsuka in Yokohama — and in this shot, the office a last-mile courier leaves from before dawn in Adachi. There is no magic, no institution and no secret organization: there is only a daily life in which the etiquette of the written name is thoroughly in place. **The name is the subject of this work, and the name the work is about is the one that is read the wrong way** — which is why every name on every in-world prop is printed or handwritten and nowhere legible.

## World Rules

- **The people in the work do not know that they are inside a film.**
- **The hand comes first and the face comes after. The order is not swapped. The face is placed only after the name has been called.**
- **The sound is not a calling voice; it is the sound of paper and hands.** A calling voice is heard only on the side of the one called.
- **The carrying never completes.** Not here, and not in the two shots that follow: the bundle only gets smaller and stays where it is put.
- **The name lives on the side of being called, not on the side of being written.**
- **Only so many places can stand at once.** This shot places two.
- **No text is burned into this work.**
- **The writing seen in this work is print, ballpoint and pencil — and none of it is legible.**
- **This work speaks Japanese.** It is the language of the room and of the people in it.

## Visual Language

- Art Direction: Luminous realist anime, translated into a workplace that has been open since before dawn. A Japanese record-keeping site, 2026: three resolutions of the written name — print, ballpoint pen, pencil — nameplate plastic, the thickness of a register's left sleeve, glue traces on an address slip, layered pencil on a claim tag. **The light, not the figure, is the subject** — and here the light is fluorescent, standing in for the style's low sun.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The palette is narrow — fluorescent white, the grey of the counter, the brown of two rubber bands, and the warm side reduced to skin and to the paper itself.
- Texture: Layered atmospheric depth from near to far; dust suspended where the tube catches it; the paper edge holding a lift of air after a night indoors. No grain, no paper texture, no painterly stroke.
- Rendering: Clean anime lineart on the figure, drawn at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — **no second tone inside one piece of cloth, no gradient inside a single material, no soft airbrush.** Bloom around the tube.
- Visual Density: Low. One focal point — the hands and the bundle — with generous negative space.
- Time: `朝（営業所を出るまで）` — the working day before it starts, under fluorescent light.
- Atmosphere: A depot that is being worked in, and is not being watched.

# 3. SUBJECTS

## 暮林蒼

- Reference: the frozen setting sheet — `distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md` (character sheet, revision 5) ＋ `expression.md` (expression sheet). **Both are the source of this work's 暮林蒼; the face is theirs and is not re-derived here.** The five face axes below are copied from that sheet, in positive form.
- Appearance: A man of twenty-six, a last-mile delivery courier — the tallest of the figures this work draws. **On the five axes the sheet fixes:** the forehead above the eyes is broad, and the cap is worn shallow so that breadth still reads; the cheekbones spread wide and set the width of the face; the jaw is short and its corner stands, and the chin itself is square; the nose is long with the tip falling; the ears are large and stand out sideways. **The sixth axis, the spacing of the eyes, is left to the style and is not fixed.** The age is not carried by the face: it is carried by the forearms, where the weather has kept it — **the skin below the sleeve is darker than the face, and the skin the sleeve covers is paler than either.** Black hair, cut short enough to sit under a cap. The work jacket and cap of a delivery company; a handheld terminal clipped at one hip so that the belt dips on that side alone; shoes worn down first at the outer heel. **Inside the cap band there is a printed size number and no name** — his name is written nowhere on anything he carries.
- Behavior: He does not call anyone by name; he opens with the business at hand. His one consistent movement is to stop — **the hand that stays after the parcel is down, the fingers that never peel the stacked slips apart, the eye that stops on a name it has just read, the foot that stops at the step.** His speed is the other half: the foot that counts steps, the hand that fills a reading faster than the eye can read it. **In this shot he arrives, receives, carries, sets down and drives, and nothing in that completes.**
- Continuity Requirements: **Must preserve** — the face and the build of the frozen setting sheet; the cap worn shallow; the terminal at one hip; the two tones of the forearm; the same person in all four panels and in all three shots of this episode. **May change** — the position of the hands, the angle of the head, the fall of light across him.

## the person at the counter

- ⚠️ **This person has no key in the ledger and no sheet in `distill-essence-engine`.** `attached` cannot name them and `forbidden_set` cannot forbid them — **the hole is recorded in `habits-ch02-seg01.yaml`, and it is the same shape as the hole at the office in 第一巻.**
- **Why there is no key — and why one is not added here.** The ledger's stock characters are not "everyone in frame": **each of them is the subject of one episode, and each is registered as one paper plus one hand** (連絡帳, 車内の名札, 保険証, 内見の鍵束 …). **This person has no paper of their own** — the only paper on the desk is his bundle — **so they are not that kind of entry.** ⚠️ **A key also needs a name, and the name is a recorded 未決** (「受付の者の名は決められていない」). **So the key is not added, and the warning above stays true.**
- Appearance: **Positive and specific — a blank is not neutral: leave it empty and the generator fills it with the only face it has, which is his.** A woman of about fifty, shorter than 暮林蒼 and not built like a courier; her hair is short and gathered at the back of the head; she wears a collared shirt in a grey colder than the counter it is seen against, its sleeves rolled to the elbow, so her forearms are bare above the desk. **No outer garment, no cap, no work jacket, no terminal at the hip — nothing of his costume on her.** ⚠️ **Deliberately a shirt and not a cardigan: §16 and §18 `Negative Prompt` both carry `no cardigan`, and an item named positively here must not be forbidden there.** She is in frame as **hands first** — a hand that stays on the desk while the face has not yet risen — and then, after the name has been said, as a face. The work's rule is not reversed for them: **the hand comes first and the face comes after.** **The screen she works at faces away from him.**
  - ⚠️ **発明（要承認）: the age, the gender and the shirt are not in the 出典.** The 出典 (the author's own prose, `draft_02-01_八十軒目.md`) writes this person as 「受付の人」 and **describes them not once**. These three were written because **the first generation collapsed the two figures into one** — the blank was filled with the courier. **The author approves or strikes them.**
  - **Not invented:** the hand-first order, the late face, the screen facing away, the drawer, and the two hands that square the edge before the bundle is set down — **all of these are the 出典's own.**
- Behavior: They call his name **after** the business has been opened, not before. **The name arrives late.** They are **never named in the work** — a recorded decision (「受付の者を、名で呼ばない」).

# 4. ENVIRONMENT

- Location: `宛名票の一行` — **the site of this episode's naming, not a room.** The naming of 第二巻第1話 happens at an address slip on the side of a box (see the second and third shots); here the frame is the office this courier leaves from, and **the key does not move because the room changed.** One site per episode.
- Environment Elements: The counter, its drawer, the fluorescent tube, a cart with small wheels moving behind, and the parking area beyond the door. **All of it exists as light and surface; the room is never the subject and never gains one.**
- Environmental Behavior: Dust moves in the light; the paper edge keeps its lift; the cart keeps its noise behind the two figures. **These move through every panel and after the hands have stopped** — that is what keeps this from being four stills.

# 5. OBJECTS

- **The bundle of slips.** Slips already gathered into one bundle. **One hundred and seventeen slips this morning.** Two rubber bands around it — **one thicker, one thinner, and both brown.** The stack is square at the edges because it was squared by a hand before it was set down: **the edge is a state, not a decoration.**
- The slips themselves: **print and ballpoint on paper, and nowhere legible.** No name on any slip is readable, and no count of the slips is written in the frame.
- **The counter and its drawer.** The drawer opens late and closes with its sound arriving slightly after it.
- **The passenger seat**, which takes a shallow dent when the bundle is set on it.
- **The cart behind** — small wheels, a large sound, and a load being stacked fast by hands that are never in frame.
- No other object is in frame.

# 6. REFERENCES

- REF_CHARACTER: 暮林蒼 — the setting sheet, revision 5 (`distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md`) (CRITICAL)
- REF_BOARD: `specs/board/habits-ch02-seg01-board.md` — the storyboard this generation is built on. **This is the H3 route's true attachment** — the image itself, not a `key_image`. ⚠️ **Not yet produced.**
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_STYLE: `luminous-anime` (HIGH)
- REF_SOURCE: `projects/habits/bible.yaml` and `projects/habits/ledger.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: A bundle of slips is handed over and set down where it will stay all day.
- Beginning: He is standing at the counter. His hands are empty and the business is already open.
- Turn: The drawer opens; the bundle comes out; the edge is squared before it is set down.
- Peak: He takes it without reaching — **the arm does not extend; the bundle is held below the chest.**
- Pull: The bundle goes onto the passenger seat, the seat takes its dent, the engine starts — **and the radio is not turned on.** The shot ends there.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - PANEL 1 `0-3s` — density: `sparse` — The office. He stands at the counter and opens with the business, **not with a name**: 「おはようございます。昨日のぶん、ありますか。」 **The face is not placed yet** — the hand comes first.
  - PANEL 2 `3-5s` — density: `held` — The counter's hand stays on the desk, and the face rises **after a moment**. 「暮林さん、おはようございます。ありますよ。」 — **the name arrives late, from the other side.**
  - PANEL 3 `5-8s` — density: `sparse` — The drawer opens and shuts, its sound arriving late. The bundle is set on the counter — **and before it is set down, fingers square the edge. The sound of that is small.**
  - PANEL 4 `8-10s` — density: `sparse` — He takes it one-handed. **The arm does not extend; it is held below the chest.** Onto the passenger seat; the seat dents; the key turns; the engine catches. **The radio is not turned on.**
- Temporal Density: The held panel is the second one and it is the shortest. **Length is not where the weight is** — the weight is in the beat where the name arrives after the business does.

# 9. ACTION

- `ACT_RECEIVE` — Before: the bundle is at the edge of the counter and not in his hands. After: the bundle is held below his chest. **He does not reach for it.**
- `ACT_SET_DOWN` — Before: the bundle is in his hands. After: the bundle is on the passenger seat and his hands are empty. **This is not an arrival; it is a placement.**
- `ACT_WITHHOLD` — Before: the engine is running. After: the radio is still off. **This is not the absence of an action; it is the action.**

# 10. CAMERA

- Camera Language: Third person, **medium**, placed at the hand — **this work puts the camera at one of three sites** (run-10【ルックとカメラ】: 「カメラは、机上の手、左袖の名札、めくられる名簿の三箇所に置かれる」). Here the lens sits at counter height, the bundle in the lower middle of the frame, and the two figures read from the hands up.
- ⚠️ **This shot is not the episode's one hand-close.** run-10 carries a second, tighter budget in the same constant — 「**手の近景を毎話一つ。**」——and **it is spent in the third shot**, where the fingertips stop on the edge of the top slip (see `specs/video/habits-ch02-seg03.md` §10). ⚠️ **The assignment of which shot spends it is 発明（要承認）**: the source grants the budget of one per episode and does not say which shot spends it. **What is not ours to choose is spending it three times** — the three shots are placed at the hand, and only one of them is close.
- Camera Events: One event only. `0-10s` — a very slow, weighted settle of a few centimetres, the camera placed rather than travelling. **Nothing is revealed by it.** ⚠️ **The division between panels 03 and 04 is not a second camera event**: the camera does not travel from the counter to the van — **it is placed again in the second place.**
- Camera Behavior: No handheld, no whip, no shake, no push-in on a face, no sudden zoom, no unnatural rotation. **Each panel is treated as its own scene, and panel joins panel by natural animation.** ⚠️ **The change of place between panels 03 and 04 is a cut division, not a continuous move** — panel 03 ends at the counter and panel 04 opens in the van. **The camera does not follow the bundle from one place to the other**; §10's single camera event stands unchanged. ⚠️ **Natural animation joins the panels across that division**: the hand that takes the bundle and the hand that sets it down are the same hand, and the movement reads through the cut. What stays forbidden is §16's clause — **no cut to an unrelated location** — and this is not one: the same action continues on the far side of it.

# 11. MOTION

## Subject Motion

A hand squares an edge; a hand takes a bundle without reaching; a hand sets it down. **All three finish and stop.** The feet stay where they are. **The face moves once, and it moves late** — it is the counter's face, not his.

## Object Motion

The bundle is the only object that travels, and it travels less than a metre. The rubber bands stay where they are; the slips do not shift inside them.

## Environmental Motion

Dust moves through the fluorescent light, the paper edge keeps its lift, and the cart keeps moving behind the two figures. **All of it keeps moving after the hands have stopped** — that is what keeps this from being a still.

## Physical Characteristics

- Weight: The bundle has weight enough that it is held below the chest rather than out at arm's length. **The seat takes a dent and keeps it.**
- Inertia: Nothing overshoots. The edge is squared and stays squared; the bundle is set down and does not slide.
- Acceleration: Each of the three hand movements is one short acceleration into a stop. **Nothing is hurried and nothing is slow.**
- Fluidity: Continuous; no snap, no held cel, no stutter.
- Impact: None.

# 12. EMOTION

- Emotional Arc: The interval between a business being opened and a name arriving.
- Emotional Events: The moment the counter's face rises — **after** the line has already been answered with the business at hand.

# 13. LIGHTING

- Base Lighting: Fluorescent ceiling light, at the upper edge of the frame or just outside it. The style's contribution is the falloff, not the sun: bloom at the tube, a lit wall behind the counter, deep cyan in the unlit half of the office, dust suspended in the light.
- Lighting Events: One — as the bundle is set on the counter, the tube catches the top slip and stays there. **This is the only highlight that moves in the shot.**

# 14. AUDIO

- Dialogue: **Japanese. Two voices, and one word from him besides his first line.**
  - His line, at the counter, before any name is used: 「おはようございます。昨日のぶん、ありますか。」 — **the ending falls slightly; the business still arrives.**
  - The counter's line, after the face has risen: 「暮林さん、おはようございます。ありますよ。」 — **the name arrives inside it, not first.**
  - His answer: 「はい」 — one word, and nothing is added to it.
  - **A number is called in the background, once: 「三番、行きます」** — **a number is called in this work, and a name is not.** It comes from off frame and **the speaker is never placed in the frame.**
- Sound Effects: Paper and hands, at the edge of audibility — the drawer opening and closing with its sound arriving late, fingers squaring an edge, the bundle meeting the counter, the bundle meeting the seat, the engine catching. **A cart with small wheels behind, and a large sound.** Nothing is mixed forward except the two lines.
- Music: **None, by specification.** ⚠️ **This is not an omission** — §16 and §18 `Negative Prompt` both carry the floor's `no background music`, so the silence is **this shot's own decision, written here**, and a bed arriving would be a failure of §14 against a clause that is in force. No bed, no score, no sting; **nothing rises when the drawer closes.**
- Environment: An office interior before the day starts. A fluorescent hum is permitted; a musical sting is not.

# 15. CONTINUITY

- Identity: The setting sheet, unsummarised, attached on every instance. **No drift of face, build or costume across the four panels.**
- Spatial: The counter is at the frame's left in the first three panels, and the passenger seat is at the frame's right in the fourth. **Neither is moved for the camera.**
- Temporal: This shot is the same working day as the two that follow it, and nothing in frame supplies a date.
- Visual: The fluorescent key, the palette and the dust are the same in all three shots of this episode.
- Motion: Full animation, not limited. **The atmosphere is the primary mover**, and the hands are the subject.
- Sound: Paper and hands, two lines in Japanese, and no music. **No calling voice as a sound effect.**

# 16. CONSTRAINTS

## MUST NOT

- No second delivery courier; no colleague added at the counter; no one who is not in the storyboard.
- No legible text on any surface — on a slip, on the bundle, on the notice by the counter, on the terminal, on a screen. **Names exist in this work and are not readable.**
- No on-screen count of the slips; no number written beside the bundle.
- No romaji in place of the Japanese name.
- No calling voice as a sound effect; no spoken name; no voice-over; no narration. **The one line that calls a number is not a name.**
- No face before the name is called.
- No completed delivery: no receiving hand, no opened door, no doorstep, no signature.
- No smile, no tears, no fear, no exaggerated expression.
- No wall clock, no calendar, no digital timer, no date stamp.
- No uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no cuts to unrelated locations.
- No panel frames, panel numbers, captions or explanatory text carried over from the storyboard into the picture.
- No on-screen subtitles, no captions, no burned-in subtitles in any language.
- No background music — no bed, no score, no sting, and nothing that rises at the end. **The fluorescent hum is environment, not music.**
- No watermark.
- Not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces.

## MUST

- The bundle changes hands and is set down. **The delivery does not complete.**
- **Two people are in this shot and they are two people** — the person at the counter is not 暮林蒼 and does not carry his face, his cap, his jacket or his build.
- The counter's face rises **after** the line has been answered.
- The radio stays off after the engine catches.
- **The change of place between panels 03 and 04 is a cut division and reads as one** — panel 03 ends at the counter, panel 04 opens in the van, and **the two places are never run together as one room**. ⚠️ **The division is between places, not between actions**: the hand that takes the bundle and the hand that sets it down are the same hand, so the movement crosses the cut.
- Dust, the paper's edge and the cart keep moving after the hands stop.

## PREFER

- Counter height for the lens, with the bundle in the lower middle of the frame and both figures read from the hands up; the squared edge of the stack catching the tube as it is set down.

## ALLOW

- The fluorescent tube at the upper edge of the frame, blooming; the cart crossing behind, out of focus.

# 17. GENERATION PRIORITIES

1. **The carrying does not complete** — the bundle is set down, not delivered. This outranks beauty and outranks legibility of feeling.
2. **The name arrives late** — the business is opened first and the counter's face comes after. **The order is not swapped for a better frame.**
3. **No name is readable** — every written name in frame is present and illegible. Either half of that failing is a different shot.
4. **The radio stays off** — the last beat withholds, and it withholds after the engine has already started.
5. **Japanese is what is spoken** — the two lines are Japanese, and the language is not left to the model's default.
6. One change only — the bundle changes hands and is placed. Nothing else happens.
7. Everything else.

---

# 18. MINIMAX H3 PROMPT MAPPING

## Master Prompt

A 10-second cinematic piece (16:9), luminous realist anime, in the office of a last-mile delivery company in Adachi, Tokyo, 2026, before the day starts. **The storyboard image attached to this generation is the design of the whole video: read its four panels in order 01 → 02 → 03 → 04, do not reorder them, do not skip one, and treat each panel as its own scene, joined to the next by natural animation — except that panels 03 and 04 are joined by a cut, because the place changes there.** **Panels 01 to 03 stand at the counter; panel 04 stands in the van. That change of place is a cut division between panels 03 and 04 — panel 03 ends at the counter and panel 04 opens in the van. Do not carry the camera from one place to the other, and do not run the two places together as one room.** One take, one change: a bundle of delivery slips is at the edge of the counter and not in his hands, and then it is on the passenger seat and his hands are empty. [01] he stands at the counter and opens with the business, not with a name; his face is not placed yet. [02] the hand at the counter stays on the desk and the face rises late. [03] the drawer opens and shuts with its sound arriving after it, and the bundle is set down — squared first by fingers, the sound of that small. [04] he takes it without extending his arm, holds it below the chest, sets it on the passenger seat, and turns the key; the radio is not turned on. **Keep the compositions and the camera distance of the storyboard; keep the protagonist the same person in every panel** — same face, same hair, same cap worn shallow, same jacket. **He is the protagonist, not the only person: the person at the counter is someone else, and they are described in the Visual Prompt — they must not take his face, his cap, his jacket or his build.** **Full colour, not black-and-white line art.** Japanese dialogue at the counter, spoken in Japanese. Sound of paper and hands throughout. The frame stays clean: **no panel frames, no panel numbers, no captions and no subtitles are carried over from the storyboard into the picture.** **Do not add unnecessary characters or scenes.** Ends on the radio staying off, and cuts. (One take, one change: the bundle changes hands and is set down where it will stay all day.)

## Visual Prompt

Luminous realist anime, translated into a workplace before dawn: the light, not the figure, is the subject, and here the light is fluorescent. A man of twenty-six, a last-mile delivery courier and the tallest of the figures this work draws, his identity locked to the frozen setting sheet: the forehead broad with the cap worn shallow so the breadth still reads, cheekbones spreading wide and setting the width of the face, a short jaw whose corner stands with a square chin, a long nose with the tip falling, large ears standing out sideways, the spacing of the eyes left to the style; black hair cut short enough to sit under the cap; a work jacket and cap, a handheld terminal clipped at one hip so the belt dips on that side alone. The age is not carried by the face — it is carried by the forearms: the skin below the sleeve darker than the face, the skin the sleeve covers paler than either. At the counter, standing behind the desk, someone other than the courier: **a woman of about fifty, shorter than him and not built like a courier, her hair short and gathered at the back of the head, in a collared shirt of a grey colder than the counter it is seen against with its sleeves rolled to the elbow — no outer garment, no cap, no work jacket, no terminal at the hip, nothing of his costume on her.** She is present first as **a hand that has not left the desk**, her forearm bare to the elbow above it, and only later, after the name has been said, as **a face** — **the hand first and the face after, never reversed**. **The screen she works at faces away from the courier**, and she is seen over it. The bundle of delivery slips, one hundred and seventeen of them, held by two brown rubber bands, one thicker and one thinner, its edges square because a hand squared them. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp. Saturated where the light falls, deep cyan in the unlit half; fluorescent white, counter grey, rubber-band brown, and the warm side reduced to skin and to the paper. Bloom around the fluorescent tube at the upper edge of the frame, dust suspended and individually rendered, generous negative space and low visual density. **No legible writing anywhere** — the slips, the notice by the counter and the terminal read as printed and handwritten surfaces with no readable name, and no count is written beside the bundle.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. Three hand movements, each one short acceleration into a stop and none of them overshooting: fingers squaring the edge of the stack before it is set down; a hand taking the bundle without the arm extending; a hand setting it on the passenger seat so the seat takes a shallow dent and keeps it. The counter's face rises late and stops. Dust moves through the fluorescent light, the paper edge keeps its lift, and a cart with small wheels keeps moving behind the two figures — **all of it keeps moving after the hands have stopped.** No impact, no collision, no motion blur smears, no stutter, no held frames. **The panels are joined by movement; the change of place between panels 03 and 04 is a cut division, not a continuous move, and the movement reads across it.**

## Camera Prompt

Third person, medium, placed at the hand — counter height, the bundle in the lower middle of the frame, both figures read from the hands up. **The camera is placed at the hand but does not close on it: keep this framing medium.** One camera event only: a very slow, weighted settle of a few centimetres over the whole take — the camera placed rather than travelling, revealing nothing. **Keep the storyboard's compositions and its camera distance.** No handheld, no whip, no shake, no push-in on a face, no sudden zoom, no unnatural rotation. **Each panel is treated as its own scene; panel joins panel by natural animation, and the change from the counter to the van between panels 03 and 04 is a cut division — the camera does not travel between the two places, it is placed again in the second.** **No cut to an unrelated location** — and this is not one: the same hand takes the bundle and sets it down, and the same action continues on the far side of the division.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of every word this work holds; **every line in this shot is spoken in Japanese.** At the counter, before any name is used: 「おはようございます。昨日のぶん、ありますか。」 — the ending falls slightly. After the face has risen: 「暮林さん、おはようございます。ありますよ。」 — the name arrives inside the line, not first. He answers 「はい」, one word, and nothing is added to it. **Once, from off frame, a number is called — 「三番、行きます」 — and the speaker is never placed in the frame.** No calling voice as a sound effect; no spoken name; no voice-over; no narration. **Nothing is written on screen**: no subtitles, no captions, in any language, and no panel numbers or storyboard text carried into the picture. Sound effects at the edge of audibility: paper and hands, a drawer opening and closing with its sound arriving late, fingers squaring an edge, the bundle meeting the counter, the bundle meeting the seat, an engine catching, and a cart with small wheels behind — nothing mixed forward except the two lines. Ambient: an office interior with a fluorescent hum. **Music: none — this shot carries no music of any kind.** No bed, no score, no sting, no drum, and **nothing rises when the drawer closes.**

## Negative Prompt

no legible name text, no legible name on any in-world prop, no legible text on the delivery slips, no legible text on any surface, no on-screen count of the slips, no number written beside the bundle, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no signature, no handwriting by the courier, no calling voice as a sound effect, no face before the name is called, no character added beyond the storyboard, no unnecessary character, no additional person beyond the storyboard, no unnecessary second courier, no colleague invented at the counter, no passer-by added, no bystander added, no second person with the courier's face, no second person wearing his cap or his jacket, no completed delivery, no receiving hand, no opened door, no signature taken, no smile, no tears, no fear, no exaggerated expression, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no cuts to unrelated locations, no panel frames, no panel numbers, no storyboard text in the picture, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no swelling music, no watermark, no morphing or drifting facial identity, no specimen chart, no measured chart of steps, no figure written beside any step, no furigana field, no printed form, no name written by the subject, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket worn over the work jacket, no outer garment, no identifying clothing, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces, no rounded jaw, no short nose, no small ears, no face younger than the age stated

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-ch02-seg01-10s-01`
- Segment ID: `01-1`
- Specification Version: `0.1.1`
- Generation Date: `—`

⚠️ **`01` は第二巻第1話の第一のショットである。** 章は巻である（台帳 `series-bible.md`——「章＝巻。四巻で閉じる。」）。

## Resolved Values

- Duration: `10s`
- References: `REF_CHARACTER (setting sheet rev.5, CRITICAL) ／ REF_BOARD (specs/board/habits-ch02-seg01-board.md, CRITICAL — the attachment of this route) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`
- Temporal Structure: `4 panels, NON_UNIFORM — 3s / 2s / 3s / 2s. The held panel = PANEL 2 at 2s (20%)`
- Camera Events: `1 event as listed in §10. Four panels, each treated as its own scene, joined by natural animation, with a cut division between panels 03 and 04`
- Action Events: `ACT_RECEIVE → ACT_SET_DOWN → ACT_WITHHOLD`
- Audio Events: `2 lines ＋ 「はい」 in Japanese ／ a number called off frame, once ／ drawer, paper, engine, cart ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, made from one storyboard of four panels`

# 20. ITERATION

## Version

`0.1.1` — **first pass generated once, from `0.1.0`, on 2026-09-20; two defects observed (§ below) and this revision is the correction.** The storyboard it depends on was produced by the author from `specs/board/habits-ch02-seg01-board.md`.

⚠️ **This version has not been generated and carries a third correction, made the same day.** The join between panels 03 and 04 is a **cut division** — ⚠️ **and that is the author's ruling, not the source's**: the source's ② says only 「各コマを独立したシーンとして扱い、静止画と静止画の間を自然なアニメーションでつないでください」 and **never uses the word カット, so it decides neither way.** The revision that corrected the two defects above had written the join as continuous — **also this repository's own addition, in the opposite direction** — and the author closed it as a cut on 2026-09-20. **The division is between places, not between actions**: the same hand takes the bundle and sets it down, so the movement reads across the cut.

## Observed Problems

**From the first generation (2026-09-20, board image `01_ChatGPT Image 2026年9月20日 14_10_37.png`):**

- **The person at the counter took the courier's face.** The two figures were rendered as one person, which reads as an error rather than as a choice. **Cause found in the string, not in the model:** §3's Appearance said 「Nothing is invented here」 and gave no form, and the `Negative Prompt` carried a flat `no additional person` / `no colleague at the counter` while the Master and Visual both placed a second person — **so the string asked for two people and forbade the second in the same breath.** The model resolved it by making one. ⚠️ **The source's own ② says 「不必要な登場人物やシーンを追加しない」 — the qualifier 不必要な was dropped on the way into §18.**
- **Panels 03 and 04 ran together as one space.** The counter and the van were rendered as a single continuous room with no transition. **Cause:** §10 and §18 both said `One continuous take … never by a cut`, **which is not in the source.** The source's ② says 「各コマを独立したシーンとして扱い、静止画と静止画の間を自然なアニメーションでつないでください」 — **each panel is its own scene.** The string had removed the generator's only lawful way to change rooms. ⚠️ **`no cuts to unrelated locations` was already in §16 and §18; the added rule was the unconditional one, and it was this repository's own house style** (`references/video-spec.md`: `whole arc × one continuous take`), **carried over from the WAN 3.0 route.**

**Both were corrected in `0.1.1`** by restoring the source's wording into §1, §10 and all four §18 slots, and by writing the counter person in positive form (§3).

## Anticipated risks (to check in the first generation)

- **The storyboard's text may be carried into the picture.** The panel numbers and the Japanese annotations are drawn on the board, and the generator may render them. **The source's own ② template forbids this** — 「漫画の枠線、番号、説明文、字幕などは動画に表示しない」 — and §18 repeats it. **If a panel number appears, the shot has failed.**
- **The name may be spoken as a sound effect.** Only the number is called; the name is spoken once, inside the counter's line. A voice calling 「暮林さん」 from off frame is a different shot.
- **The face may arrive early** — the counter's face rising with the first line, rather than after it.
- **Music may be placed anyway.** The floor's clause is in force and §18 `Negative Prompt` carries it, so a bed arriving — under the fluorescent hum, or rising as the drawer closes — is **a violation of §16, not a matter of taste.** ⚠️ **The fluorescent hum is environment; do not let it acquire a pitch and a pulse.**
- **The delivery may complete** — a receiving hand, an opened door, a signature. **The bundle is set down; nothing else happens to it.**
- **The arm may extend.** The bundle is held below the chest; an outstretched arm is a different shot.
- **The slips may be legible, or countable.** A readable name or a written number on the stack ends the work's premise in one panel.
- ~~**The second person may be invented twice** — a colleague at the counter, a courier behind.~~ ⚠️ **This prediction was wrong and is kept here struck through.** The first generation did **not** add a third person: **it collapsed the two it was given into one.** The risk to watch now is the opposite one — **that the person at the counter takes his face again** — and the guard is the positive description in §3 and §18 `Visual Prompt`, not this line.
