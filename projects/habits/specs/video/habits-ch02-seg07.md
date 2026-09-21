# Seedance 2.5 Full Specification — 『ハビッツ！！！』第二巻第7話「表札と宛名票」 第二のショット「宛名票の名が、目で、表札へ運ばれ、重ならないところで、止まる」 / 12s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である。

⚠️ **このショットは、この話の「一拍」である。**（話割り——「現場／一拍＝届け先の玄関／表札と宛名票」。
場面表——「**一拍の位置＝第2場面。運搬が止まる場所。**」）
**このショットは、この話でいちばん長い拍を持つ**——**そしてその長さは、往復が反復するからである。**
本文は同じ行を五度書く——「上で、また、無い」「行って、来て、戻る」「同じ、ところで、無い」。

⚠️ **このショットは `SEEDANCE 2.5` の経路である。** **§18 の見出しがモデルを名乗る**（`L18`）。
⚠️ **これはこの経路の1本目である。** `specmap.MODEL_ROUTE` の `SEEDANCE 2.5` は**空のタプル**である
——**「禁じる語が無い」ではなく「測っていない」**（`WAN 3.0` の空とは意味が違う）。

⚠️ **⚠️ この経路は `Negative Prompt` を、床として受け取らない。**（`specmap.MODEL_UNRECEIVED_SLOTS`）
公式に否定として扱われるのは**字幕と音声だけ**である（`"No subtitles."` / `"No BGM"` / `"No audio."`）。
**残りは、ただの散文として読まれる**——**§18 `Negative Prompt` の九十余節は、この経路では助言になる。**
⚠️ **効かなかった否定は、渡さなかった否定と見分けがつかない。描かれてから分かる。**
⚠️ **だからこの仕様は、禁制を二箇所に置く**——**§18 `Negative Prompt`**（**この作品が何を禁じるかの記録**。
⚠️ **この経路はこれを受け取らない**）と、**§18 `Master Prompt` の散文**（**この経路が実際に読む側**）。
**同じことを二度書いているのではない。片方は床で、片方は助言である。**
⚠️ **`L30` がこれを鳴らす。** **それが正しい**——**鳴らなければ、この経路の否定が床であるかのように読まれる。**
**作品が承知で使うなら、作品がそれを書く**（`bible.route_limits_accepted`）。**著者が決める。**

⚠️ **このショットに、会話は無い。** **受付の者は出ない。戸は開かない。**
**ゆえに §18 `Audio Prompt` は、言葉を持たない。** **それでも言語を名乗る**——
**「この作品は日本語を話す」は、台詞の有無によらない**（`L27`。無言の一枚に言語を書かないと、
生成器は自分の既定で埋める——実測 2026-09-18、中国語の字幕が焼かれた）。
⚠️ **この経路には字幕を出す公式の記法が在る**（`【】`）。**ゆえに `no on-screen subtitles` の床は、
この経路でむしろ強く効く**——**そしてこの経路は、その床を数少ない「本当に効く否定」として持っている。**

⚠️ **このショットに、音楽は無い。** **床がそれを禁じている**（`specmap.BASE_NEGATIVES` の
`no background music`）——§16 `MUST NOT` と §18 の両方が持つ。
⚠️ **`No BGM` は、この経路が実際に否定として受け取る数少ない語の一つである**（上の註）。
**ゆえにこの一枚では、床の三節のうち二節が、本当に床である。**

⚠️ **`role` は 所作 であって 開示 ではない。**（`habits-ch02-seg07.yaml`）
**画面の内側で起きるのは「運ぶ」ことと「止まる」ことである。** 開示の設計は台帳が持つ。

⚠️ **⚠️ このショットは、場面表の第二場面を分割している。これが発明（要承認）である。**
場面表の②は**二つのことをする**——**(a) 名を、目で表札へ運び、重ならないところで止まる**（本文 `:339`–`:417`）と、
**(b) 戸が開き、受付の者が出て、姓の読みを訊く**（本文 `:419`–`:475`）。**このショットは (a) だけを持つ。**
⚠️ **落ちたのではない。撮っていない。** **(b) は、まだ無いショットである。記録として書く。**

⚠️ **このショットは、開示の検査を受けていない。** 台帳 `disclosure` はこの話の変化点を**まだ宣言していない**
——照合する相手が無い。`L7` が註で報告する。**違反0件ではない。**
⚠️ **この話の変化点は第三場面の側にある**（本文 `:593`「私は、読みを、直しません。」）——
**このショットは、変化点の手前である。**

---

# 1. VIDEO

- Duration: `12s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take of one change, in four timed movements — **the name on the printed slip is carried up to the carved nameplate by the eye, does not land, is carried again, and stops where the two do not overlap.** ⚠️ **The arm carries nothing.** The box is already in the crook of his arm and the fingers do not move. **Nobody comes out of the house.**

# 2. WORLD

## World Concept

2026, Japan — in this shot, the front of a private house in Adachi, Tokyo, in the middle of a working day. There is no magic, no institution and no secret organization: there is only a daily life in which the etiquette of the written name is thoroughly in place. **The name is the subject of this work, and the name this work is about is the one that is read the wrong way.** Here two names stand one above the other — **one carved into wood, one printed on paper** — and the shot is what happens when a man carries the lower one up to the upper one with his eyes and they do not meet. **Both are present and neither can be read.**

## World Rules

- **The people in the work do not know that they are inside a film.**
- **The hand comes first and the face comes after. The order is not swapped.** ⚠️ **Here nothing is called at all** — the face is already placed, and it does not move.
- **The carrying never completes.** In this shot the thing being carried is **the name**, and it is carried by the eye. **It arrives where it is not.**
- **The speed does not change.** The eye goes up and comes down at the same rate every time. **Becoming faster would be the emotion, and here there is no emotion in the speed.**
- **The writing seen in this work has three resolutions — print, ballpoint and pencil — and this shot holds two of them at once: carved into wood, and printed in ink on paper.** ⚠️ **That difference must be visible.** ⚠️ **Neither is legible.**
- **No text is burned into this work.** ⚠️ **In-world text is a different thing from a subtitle**, and this shot draws the first and forbids the second.
- **Only so many places can stand at once.** This shot places one.
- **This work speaks Japanese.**

## Visual Language

- Art Direction: Luminous realist anime, translated into the front of a house at midday. A Japanese delivery site, 2026: a gatepost of wood with a small square nameplate screwed to it, two characters cut into the plate and filled with black; a cardboard box held against the body with a printed address slip glued to its side, four ruled fields on it; a worn stone at the foot of the post; a sliding door with glass, closed, and behind the glass nothing that reads. **The light, not the figure, is the subject** — and here the light divides the nameplate into a lit half and a shadowed half.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The palette is narrow — the pale of cardboard, the white of the slip, the grey of the stone, the warm brown of the post, and black in two places: the hollow of the carved characters, and the ink of the printed ones.
- Texture: Layered atmospheric depth from near to far; dust suspended and individually rendered in the air in front of the post. **The grain of the post runs vertically and its spacing is wide.** No grain overlay, no paper texture, no painterly stroke.
- Rendering: Clean anime lineart on the figure, drawn at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — **no second tone inside one piece of cloth, no gradient inside a single material, no soft airbrush.** ⚠️ **The carved characters and the printed characters are drawn as different marks, not as one texture applied twice.**
- Visual Density: Low. One focal point — the two surfaces and the eye that travels between them — with generous negative space.
- Time: `昼（届け先の玄関の前）` — the middle of a working day, outdoors. **The same midday as the shot before and the shot after; this episode's three scenes are placed in one noon.**
- Atmosphere: The front of a house where a delivery has stopped and no one is watching it.

# 3. SUBJECTS

## 暮林蒼

- Reference: the frozen setting sheet — `distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md` (character sheet, revision 5) ＋ `expression.md` (expression sheet). **Both are the source of this work's 暮林蒼; the face is theirs and is not re-derived here.**
- Appearance: A man of twenty-six, a last-mile delivery courier — the tallest of the figures this work draws. **On the five axes the sheet fixes:** the forehead above the eyes is broad, and the cap is worn shallow so that breadth still reads; the cheekbones spread wide and set the width of the face; the jaw is short and its corner stands, and the chin itself is square; the nose is long with the tip falling; the ears are large and stand out sideways. **The sixth axis, the spacing of the eyes, is left to the style and is not fixed.** The age is not carried by the face: it is carried by the forearms — **the skin below the sleeve is darker than the face, and the skin the sleeve covers is paler than either.** Black hair, cut short enough to sit under a cap. The work jacket and cap of a delivery company; a handheld terminal clipped at one hip so that the belt dips on that side alone; shoes worn down first at the outer heel. **He is standing still, and he has been standing still since the shot began.**
- Behavior: **The eye is the actor of this shot and the body is not.** The eye rests on the printed slip, rises to the carved plate, finds nothing, comes back, takes the name again, and rises again — **at the same speed every time**. ⚠️ **The head does not tilt and the feet do not shift.** The fingers do not move; the paper's edge stays caught under the pads of his fingers; **the corner of the box stays pressed into the palm.** At the end there is one change and it is not a movement: **the blink slows.**
- Continuity Requirements: **Must preserve** — the face and the build of the frozen setting sheet; the cap worn shallow; the terminal at one hip; the two tones of the forearm; the same person as in every other shot of this work. **May change** — nothing in this shot. ⚠️ **The face is placed and the expression is not** — **no expression is given to it here.**

## nobody

- **No second person appears in this shot, and the door does not open.** The frame holds him alone.
- ⚠️ **This is not carried by the `Negative Prompt`** — ⚠️ **and on this route it could not be, even if it were written there** (the route receives negation only for subtitles and audio). **It is carried by the positive slots: §16 `MUST NOT`, and the Master Prompt's own sentence that the door stays shut.**
- ⚠️ **A weak guard, and it is recorded as a hole**（`habits-ch02-seg07.yaml`／`ledger.yaml` の該当箇所）.
- ⚠️ **The 受付の者 of this episode has no ledger key** — he is not one of the twenty-eight. **This shot does not need him, and the shot that will is not yet made.**

# 4. ENVIRONMENT

- Location: `表札と宛名票` — **the site of this episode's naming, not a room.** ⚠️ **Neither the plate nor the slip is a prop of this scene alone; they are the two halves of the episode's naming, and this is the only shot that holds both at once.**
- Environment Elements: The front of a private house — a post with a nameplate, a worn stone at its foot with a chipped corner, a closed sliding door with glass, and a single raised step. **The inside of the entrance is not shown**: no desk, no floor, no light from within. **The frame holds only what is outside the doorway.** The narrow street behind him.
- Environmental Behavior: Dust moves in the air in front of the post and catches the light; **the shadow on the plate's left half is a shadow and stays a shadow.** ⚠️ **These keep moving after the eye has stopped** — that is what keeps this from being a still. There is no wind event.

# 5. OBJECTS

- **The gatepost's nameplate.** Wood, square, screwed to the post. **Two characters are cut into it** — recessed into the grain, the hollow filled with black, **the upper half of the plate faded lighter than the lower**, the four corners rounded, **two screw heads visible with cross slots.** ⚠️ **The characters are carved, and the carving is what makes them what they are** — a flat mark would be a different object. ⚠️ **And they cannot be read.**
- **The address slip**, glued to the side of the box. Paper, ruled into four fields, **facing the camera.** The topmost field carries a name. **The characters are printed in black ink** — flat, even-edged, laid on the surface rather than cut into it. ⚠️ **This is the second of the work's three resolutions, and the shot's whole subject is that it is not the first.** ⚠️ **And they cannot be read either.**
- **The box**, held in the crook of his arm, its corner pressed into the palm so that the pressed place goes white. ⚠️ **It is not set down in this shot.** The setting down is the third scene's.
- **The stone at the foot of the post** — square, one corner chipped, **worn where feet land.**
- No other object is in frame.

# 6. REFERENCES

- REF_CHARACTER: 暮林蒼 — the setting sheet, revision 5 (`distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md`) (CRITICAL)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_STYLE: `luminous-anime` (HIGH)
- REF_SOURCE: `projects/habits/bible.yaml` and `projects/habits/ledger.yaml` (CRITICAL)
- ⚠️ **REF_BOARD は無い。** この経路は絵コンテを要求しない。**この経路の参照素材は `role` を持つ**——
  `reference_image`（最大30点）・`reference_video`・`reference_audio`・**`first_frame`**・**`last_frame`**。
  **この経路の入力の型は5つである**（テキストのみ／参照画像／先頭フレーム／動画編集／動画延長）。
  ⚠️ **このショットは「テキストのみ」の型で立っている**——**参照素材がまだ一枚も無いからである。**
- ⚠️ **この経路は、実在の顔を含む参照画像・参照動画を受け取らない**（公式の警告）。
  **この作品の人物は実在しないので、この制限には当たらない。**——**当たらないことを、ここに書く。**

# 7. NARRATIVE

- Core Event: **A man carries the name on the printed slip up to the carved nameplate with his eyes, and it is not there.**
- Beginning: The foot has already stopped, the box is already in his arm, and the eye is already on the slip.
- Turn: The eye arrives at the plate and finds nothing, and goes back down for the name.
- Peak: **It repeats — and the repetition is identical. Same route, same speed, same absence.**
- Pull: **The eye stops where the two do not overlap, and the body does nothing about it.** The shot ends on the blink slowing and the name still not legible.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - MOVEMENT 1 `0-3s` — density: `sparse` — **The plate.** He is standing; the foot is already still. The box is against him and the fingers do not move. **The carved characters: recessed, black in the hollow, the upper half faded.** Sun on the right half of the plate; the left half in shadow.
  - MOVEMENT 2 `3-6s` — density: `sparse` — **The slip.** The paper faces the camera, four ruled fields, **the topmost one carrying the printed characters.** The eye is on the paper — and then goes up, **taking the name with it.**
  - MOVEMENT 3 `6-9s` — density: `sparse` — **The circuit.** Up, and it is not there; down, and the name is taken again; up again. ⚠️ **The speed is the same.** One stop at the top, one stop at the bottom. **No sound comes from the circuit.**
  - MOVEMENT 4 `9-12s` — density: `held` — **The stop.** It stops where the two do not overlap and does not move. **The eye stays up there.** One of the screws is new. **The blink slows.** The breathing stays shallow and the shoulders do not move.
- Temporal Density: **The held movement is the last one and it is the shortest in what happens and the heaviest in what does not.** ⚠️ **The episode's weight is in the beat where nothing is done about what has been seen** — and here it is done four times before the shot ends.

# 9. ACTION

- `ACT_CARRY` — Before: the name is on the paper and nowhere else. After: **it has been carried to the plate and back, repeatedly, by the eye.** ⚠️ **Nothing is transported. The transport is the looking.**
- `ACT_CHECK` — Before: the eye has not compared the two. After: **the two have been compared and do not agree.** ⚠️ **The shot does not say which is right** — it says only that they do not overlap.
- `ACT_STOP` — Before: the eye is moving at a constant rate. After: **the eye is still, and the only change left is the blink slowing.** ⚠️ **This is the change of the shot** — and its restraint is the shot.

# 10. CAMERA

- Camera Language: Third person, **medium**, placed at the two surfaces — **this work puts the camera at one of three sites** (run-10【ルックとカメラ】: 「カメラは、机上の手、左袖の名札、めくられる名簿の三箇所に置かれる」). Here the lens sits below his eye line: **the plate and the slip are seen because he is looking at them, and the frame never turns to read either.**
- ⚠️ **This shot is not the episode's one hand-close** — run-10's 「**手の近景を毎話一つ。**」 belongs to the hand that sets the box down, and that is the third scene. **A close-up here would spend the episode's budget on a hand that does not move.**
- Camera Events: One event only. `0-12s` — a very slow, weighted settle of a few centimetres, the camera placed rather than travelling. **Nothing is revealed by it.**
- Camera Behavior: No handheld, no whip, no shake. ⚠️ **And no rack focus between the two surfaces** — **the camera does not do with the lens what the eye is doing.** No push-in on either the plate or the slip, and no cut to a legible insert. **The frame keeps its distance and its composition for the whole take.**

# 11. MOTION

## Subject Motion

**An eye going up and coming down at a constant rate, four times, and then stopping.** ⚠️ **It is the only motion the figure has.** The fingers do not move; the head does not tilt; the shoulders do not rise; the feet do not shift. **The last movement in this shot is a blink that takes longer than the ones before it.**

## Object Motion

⚠️ **None.** The box does not move, the slip does not move against the box, and the plate is screwed to the post. **Everything the eye is looking at is still** — which is why the eye has to be the thing that moves.

## Environmental Motion

Dust moves in the air in front of the post and catches the light. **It keeps moving after the eye has stopped** — that is what keeps this from being a still.

## Physical Characteristics

- Weight: **The box has weight and the arm is carrying it** — the shoulder is set and the arm does not drift. ⚠️ **This is the only place the shot's weight shows**, because the eye has none.
- Inertia: The eye's reversals have no overshoot and no ease — **it arrives and it turns, at the same rate both ways.**
- Acceleration: **None.** ⚠️ **This is the shot's physical law: nothing in it accelerates.** The rate in movement 2 is the rate in movement 3 and the rate in movement 4.
- Fluidity: Continuous; no snap, no held cel, no stutter. ⚠️ **Stillness at the end is not a held frame** — the dust and the light go on moving.
- Impact: **None.** No contact is made with anything in this shot.

# 12. EMOTION

- Emotional Arc: **The interval between a name arriving and a name not being there** — held open, and then repeated.
- Emotional Events: **The eye stopping on the top line and going up.** ⚠️ **And the fourth time, which is the same as the first** — the emotion is not in a change of behaviour, because there is none. It is in the count.

# 13. LIGHTING

- Base Lighting: Hard, flat midday light with the style's bloom on the pale surfaces. The sun is high and slightly behind and to the right of the camera. **The plate is divided: the right half is lit and the left half is in the shadow of the post.** The slip's white is the brightest thing in the frame and the hollow of the carved characters is the darkest. Deep cyan in the shadow the post throws. Dust suspended in front of the post.
- Lighting Events: **None.** ⚠️ **The light does not change once in this shot** — it must not, because the shot's only motion is the eye, and a change of light would be read as a change of meaning.

# 14. AUDIO

- Dialogue: **None.** No line is spoken in this shot, by him or by anyone else, and **the door does not open.** ⚠️ **This is not a silent shot** — see Sound Effects. ⚠️ **The work still speaks Japanese**; §18 names it.
- Sound Effects: **Dust and paper, and nothing else placed.** The small paper sound of the slip's edge held under the fingers; the dry sound of air moving over a stone step; ⚠️ **and the absence of any sound from the circuit** — **the eye goes up and comes down four times and makes no sound at all**, and that absence is placed rather than left out. **Nothing is mixed forward.**
- Music: **None, by specification.** ⚠️ **This is not an omission** — §16 and §18 both carry the floor's `no background music`, and ⚠️ **on this route `No BGM` is one of the few negations that is actually received.** There is no bed, no score, no sting, and nothing rises at the held movement.
- Environment: An open residential street in the middle of the day. Distant traffic and the air over the step are permitted; a musical sting is not. **No calling voice as a sound effect** — and here there is no voice at all.

# 15. CONTINUITY

- Identity: The setting sheet, unsummarised, attached on every instance. **No drift of face, build or costume across the four movements.**
- Spatial: The post is at the frame's left and the box is at the frame's bottom right throughout; **the two surfaces keep their positions in the frame for the whole take.** ⚠️ **Nothing is moved for the camera.**
- Temporal: The same working day, and the same noon, as the shot before and the shot after. **Nothing in frame supplies a date.**
- Visual: The palette and the style are the same in all shots of this episode. **The light is the noon of this shot** — the episode's three scenes are placed in one noon.
- Motion: Full animation, not limited. **The atmosphere is the primary mover**; the eye is the subject.
- Sound: Dust, paper, and one placed absence. **No music. No calling voice as a sound effect.**
- ⚠️ **This shot and the three shots of the first episode use two different routes** (`SEEDANCE 2.5` here, `MINIMAX H3` there). ⚠️ **What must not drift is the person, the palette and the light** — **not the wording of the prompt.**

# 16. CONSTRAINTS

## MUST NOT

- **The door does not open.** No resident, no receiving hand, no second person, no passer-by; **no character added beyond the shot.**
- **The eye does not change speed.** No acceleration, no haste, no slow-motion, no change of rhythm between the circuits.
- **No legible text on any surface** — not on the nameplate, not on the slip, not on the box, not on the house. ⚠️ **Both surfaces are present and neither can be read.** **Either half of that failing is a different shot.**
- **No flat characters on the nameplate.** The characters are **cut into the grain and filled black** — ⚠️ **if they are painted on, the plate stops being a plate and the shot loses its second resolution.**
- No romaji in place of the Japanese name; no real-world alphabet in frame.
- **No blank plate and no nonsense glyphs** — ⚠️ **a plate with no characters at all, or with invented ones, fails in the other direction.** The work forbids both.
- No camera move toward either surface, no rack focus between them, no push-in on the writing, no cut to a legible insert. **The audience is not shown what he reads.**
- **No blink before the last movement.** The blink is the shot's only end.
- No calling voice as a sound effect; no spoken line; no voice-over; no narration.
- No music of any kind in this shot.
- No wall clock, no calendar, no digital timer, no date stamp, no house number rendered readable.
- No uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion.
- No on-screen subtitles, no captions, no burned-in subtitles in any language.
- No background music — no bed, no score, no sting, and nothing that rises at the held movement.
- No watermark.
- Not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces.

## MUST

- **The name is carried from the printed slip to the carved plate by the eye, and it is not there.**
- **The characters are carved on the plate and printed on the slip, and the difference between the two is visible.**
- **Neither set of characters can be read.**
- **The eye's speed does not change across the circuits.**
- **The box is not set down and the door does not open.**

## PREFER

- The lens below his eye line, with the plate in the upper left of the frame and the slip in the lower right, **so that the eye's travel and the frame's diagonal are the same line**; the split light on the plate as the frame's only strong contrast.

## ALLOW

- Dust in the air in front of the post; the chipped corner of the stone; the shadow of the post on the plate's left half.

# 17. GENERATION PRIORITIES

1. **Neither name is legible** — both surfaces are present and neither can be read. Either half failing is a different shot.
2. **The carving is carving** — the plate's characters are cut into the wood, and the difference from the printed ones is visible. **This is the shot's reason for existing, and this route is the only one of the three that can draw it.**
3. **The speed does not change** — the circuits are identical to each other. The count is the meaning.
4. **The door does not open** — nobody comes out, and the box is not set down.
5. **Japanese is what this work speaks** — named in §18, even though this shot holds no words.
6. One change only — the name is carried and stops where the two do not overlap. Nothing else happens.
7. Everything else.

---

# 18. SEEDANCE 2.5 PROMPT MAPPING

⚠️ **この経路の §18 は、他の二つの経路と書き方が違う。** **時区分をプロンプトの中に書ける**（`0-3s:`）——
**ゆえに `Master Prompt` が、それ自体で一本の時間割を持つ。**
⚠️ **そして `Negative Prompt` を、この経路は床として受け取らない**（冒頭の註）。
**ゆえに禁制は、`Master Prompt` の散文の中にも、肯定形で一度書いてある。**

## Master Prompt

A 12-second cinematic piece (16:9), luminous realist anime, at the front of a private house on a narrow street in Adachi, Tokyo, 2026, at midday. One continuous take, one change: a delivery courier stands still at the entrance holding a box against his body, and **carries the name printed on the slip glued to the box up to the name carved into the nameplate on the post with his eyes, and it is not there, and he carries it again, and stops where the two do not overlap.**
0-3s: the post and the plate. He is standing; his feet are already still. The plate is wood, square, screwed on, **its two characters cut into the grain with the hollow filled with black, the upper half of the plate faded lighter than the lower, the four corners rounded, two screw heads with cross slots.** The sun is on the right half of the plate; the left half is in the post's shadow.
3-6s: the slip glued to the side of the box faces the camera — paper, four ruled fields, **its topmost field carrying two characters printed in black ink, flat and even-edged, laid on the surface rather than cut into it.** His eyes are on the paper, and then they go up, **taking the name with them.**
6-9s: they arrive at the plate and **the name is not there**; they come back down and take it again; they go up again. **The speed is the same every time. One stop at the top, one stop at the bottom.** Nothing makes a sound.
9-12s: **they stop where the two do not overlap and do not move. His eyes stay up there.** One of the screws is new. **His blink slows.** His breathing stays shallow and his shoulders do not move.
**His face is placed and no expression is placed on it. His head does not tilt, his fingers do not move, the box is not set down, and the door does not open — no one comes out of the house and no one is at the door.** **The two sets of characters are drawn as different marks — one cut into wood and filled black, the other printed flat in ink — and neither set can be made out: they are present on screen and unreadable.** **This is a Japanese work and these are Japanese characters, set in the Japanese script.** No subtitles. No BGM.
(One continuous take, one change: the name is carried up by the eye and stops where the two do not overlap.)

## Visual Prompt

Luminous realist anime, translated into the front of a house at midday: the light, not the figure, is the subject, and here the light divides the nameplate into a lit half and a shadowed half. A man of twenty-six, a last-mile delivery courier and the tallest of the figures this work draws, his identity locked to the frozen setting sheet: the forehead broad with the cap worn shallow so the breadth still reads, cheekbones spreading wide and setting the width of the face, a short jaw whose corner stands with a square chin, a long nose with the tip falling, large ears standing out sideways, the spacing of the eyes left to the style; black hair cut short enough to sit under the cap; a work jacket and cap, a handheld terminal clipped at one hip so the belt dips on that side alone. The age is not carried by the face — it is carried by the forearms: the skin below the sleeve darker than the face, the skin the sleeve covers paler than either. **No expression is placed on the face in this shot.** The nameplate: wood, square, screwed to the post, **two characters cut into the grain and filled with black, the upper half of the plate faded lighter than the lower, four rounded corners, two screw heads with cross slots** — **carved, not painted, and not readable.** The address slip glued to the side of the box: paper, ruled into four fields, **the topmost field carrying two characters printed flat in black ink** — **printed, not carved, and not readable.** A box held in the crook of his arm, its corner pressed white into the palm. A worn stone at the foot of the post with one chipped corner, a closed sliding door with glass, and nothing readable behind the glass. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp. Saturated where the light falls, deep cyan in the post's shadow; the pale of cardboard, the white of the slip, the grey of the stone, the warm brown of the post. Bloom on the pale surfaces, dust suspended and individually rendered in the air in front of the post, generous negative space and low visual density.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. **An eye going up and coming down, four times, at a rate that does not change; and then stopping; and then a blink that takes longer than the ones before it.** Nothing else in the figure moves: the fingers do not move, the head does not tilt, the shoulders do not rise, the feet do not shift, and the box is not set down. **The eye's reversals have no overshoot and no ease — it arrives and it turns, the same both ways.** Dust moves in the air in front of the post and catches the light — **it keeps moving after the eye has stopped**, and the shadow on the plate's left half stays where it is. **No acceleration anywhere in this shot.** No impact, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third person, medium, placed at the two surfaces — **the lens sits below his eye line throughout: the plate and the slip are seen because he is looking at them, and the frame never turns to read either. Keep this framing medium; do not close on the writing.** One camera event only: a very slow, weighted settle of a few centimetres over the whole take, revealing nothing. ⚠️ **Do not rack focus between the plate and the slip** — **the camera does not do with the lens what the eye is doing.** No handheld, no whip, no shake, no push-in, no sudden zoom, no unnatural rotation, no cut to an insert of either surface. **Keep the composition for the whole take.**

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of everything this work holds. **No line is spoken in this shot: he says nothing, the door does not open, and there is no voice-over and no narration.** **The Japanese is not spoken here; it is what this work is** — and **nothing is written on screen**: no subtitles, no captions, in any language. Sound effects, nothing mixed forward: the small paper sound of the slip's edge held under his fingers; air moving over a stone step; distant traffic on a narrow street. ⚠️ **And one absence, placed rather than left out: the circuit makes no sound at all** — the eye goes up and comes down four times and nothing is heard. **Music: none — this shot carries no music of any kind.** No bed, no score, no sting, no drum, and nothing rises at the end. **No calling voice as a sound effect**; no spoken name; no crowd; no dog.

## Negative Prompt

no legible name text, no legible name on any in-world prop, no legible text on the address slip, no legible text on the nameplate, no legible text on any surface, no readable house number, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank nameplate, no empty plate, no painted letters on the nameplate, no flat characters where the carving should be, no printed characters where the carving should be, no carving where the printing should be, no signature, no handwriting by the courier, no calling voice as a sound effect, no face before the name is called, no character added beyond the shot, no unnecessary character, no resident at the door, no opened door, no receiving hand, no passer-by added, no bystander added, no second person with the courier's face, no second person wearing his cap or his jacket, no completed delivery, no setting the box down, no handing over, no knock, no doorbell, no smile, no tears, no fear, no exaggerated expression, no blink before the end, no change of speed in the eye, no acceleration, no slow motion, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no rack focus between the plate and the slip, no push-in on the writing, no cut to a legible insert, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no swelling music, no watermark, no morphing or drifting facial identity, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket worn over the work jacket, no outer garment, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces, no rounded jaw, no short nose, no small ears, no face younger than the age stated

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-ch02-seg07-12s-01`
- Segment ID: `02-7`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `12s`
- References: `REF_CHARACTER (setting sheet rev.5, CRITICAL) ／ REF_FORMAT (video-spec) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`
- Temporal Structure: `4 movements, NON_UNIFORM — 3s / 3s / 3s / 3s. The held movement = MOVEMENT 4`
- Camera Events: `1 event as listed in §10`
- Action Events: `ACT_CARRY → ACT_CHECK → ACT_STOP`
- Audio Events: `no dialogue ／ paper ＋ air ＋ one placed absence ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **not yet generated.**

## Observed Problems

- _(this shot has not been generated, so there are no observations of it.)_ ⚠️ **But this is not `_(none yet)_` either: the shot has not been sent, and the reason is not the shot.** ⚠️ **`L30` fires on this specification** — §18 `Negative Prompt` has content, and **this route does not receive that slot as a floor.** **It cannot be fixed by editing §1–17.** The two ways out are the author's:
  - **(a) 作品が引き受ける** — write `SEEDANCE 2.5: Negative Prompt` into `bible.route_limits_accepted`（`specmap.ROUTE_LIMITS_KEY`）。**違反が註になる**——**除外は作品の宣言であって、基盤の判断ではない。**
  - **(b) 禁制を絞る** — ⚠️ **だが `L21` が待っている。** §18 `Negative Prompt` は**基盤の3節と作品の禁制を覆わねばならない**
    ——**空にすれば、今度は `L21` が鳴る。** **この二つは、片方を閉じれば片方が開く。**
- ⚠️ **そして、どちらを選んでも、この経路の否定は床にならない。** **`L30` が言えるのはそこまでである**
  ——**その否定が実際に効いたかは、生成の外では見えない。**

## ⚠️ `L14` ——「宣言を超えた区間」（＋22／−19）

⚠️ **この仕様は、`L14` にも当たる。** 台帳はこの位置に変化点を宣言していない。
**`L14` の言い分は正しい**——**このショットで、この作品の動画の Negative は、戻らない仕方で変わった。**
⚠️ **そしてその変化は、このショットの欠陥ではない。理由をここに書く**——`L14` 自身が
「`disclosure` に行を足すか、**足さない理由を記録に書く**」と求めている。

**この作品の動画の Negative は、いま82節で、三本とも同一である**（`habits-ch02-seg01/02/03` の §18）。
⚠️ **同一なのは偶然ではない**——三本は `L10` に `negative: covered` を宣言されており、
**「覆った」は「同じである」を要求する。** ゆえに **82節は、この作品の動画の「床」として書かれた。**
⚠️ **ただし、その82節は第一話の現場で書かれている**——**絵コンテが添付され、受付の者が居り、
伝票と名簿があり、八十軒を数える話である。このショットは、そのどれでもない。**

| −19 の内訳 | 節 | このショットに無い理由 |
|---|---|---|
| **経路の形** | `no character added beyond the storyboard`／`no additional person beyond the storyboard`／`no panel frames`／`no panel numbers`／`no storyboard text in the picture`（5節） | **第一話の三本は `MINIMAX H3` の経路で、絵コンテ画像を添付する。**⚠️ **この経路は絵コンテを要求しない**（`## 6. REFERENCES`）。**ゆえにこの5節は、作品の語ではなく経路の語である**——このショットの同じ用は `no character added beyond the shot` が負う。 |
| **第一話の題材** | `no on-screen count of the slips`／`no number written beside the bundle`／`no specimen chart`／`no measured chart of steps`／`no figure written beside any step`／`no furigana field`／`no printed form`／`no signature taken`／`no unnecessary second courier`／`no colleague invented at the counter`（10節） | **八十軒を数える話であり、受付の者と伝票と名簿の話である。**⚠️ **とくに `no printed form` は、このショットでは逆に害になる**——**このショットが要るのは、印刷された宛名票そのものである。** |
| **言い換え** | `no legible text on the delivery slips`／`no name written by the subject`／`no identifying clothing`／`no cuts to unrelated locations`（4節） | **同じ禁止の、別の名である**——このショットは**「宛名票の字」と「表札の字」を別々に禁じる**（その方がこの話に正確である）。⚠️ **`L14` 自身が「意味は見ない」と書いている**——**ゆえにこの4節は、この検査では区別できない。** |

⚠️ **足して数を減らさなかった。** 19節をこのショットへ書き戻せば `L14` は静かになる——
**だが `no printed form` を書き戻すことは、このショットが要るものを禁じることである。**
**数を小さくすることは、欠陥を直すことではない。**

⚠️ **`disclosure` に行を足す道は取らない。** **このショットは開示の変化点ではない**——
この話の変化点は第三場面の側にある（本文 `:593`）。**台帳に嘘の行を足せば、`L7a` の前提が崩れる。**

⚠️ **ゆえに残るのは、著者への問いである**——**この作品の動画の Negative は、一つの集合なのか**
（第一話の82節を床として、以後の全ショットが持つのか）、**ショットごとに書かれるのか。**
⚠️ **`＋22` の側も同じ問いを含む**——このショットが新しく禁じている22節を、以後のショットも持つのか。
⚠️ **著者が決めるまで、この仕様は送らない。**

## Anticipated risks (to check in the first generation)

- **The characters may be rendered legible.** ⚠️ **This is the first risk of this shot, and on this route it is the one the `Negative Prompt` cannot stop.** The clause `no legible name text` sits in the slot the route reads as prose. **If a name becomes readable, the work's premise is over.** — **the guard is the Master Prompt's own sentence, and it is weaker than it looks.**
- **The nameplate may come back blank or with invented characters.** ⚠️ **The other direction, and the more likely one on a route with no negative parameter.** A generator asked for "unreadable Japanese characters" may produce no characters at all, or nonsense glyphs. **Both are forbidden by this work** (`no blank nameplate` / `no nonsense glyphs` / `no pseudo-kanji`) — **and neither clause is a floor here.**
- **The carving may flatten into print.** If the plate's characters are painted rather than cut, the shot loses its second resolution and becomes a shot about one surface instead of two.
- **The eye may speed up.** The whole shot is that it does not; a circuit that gets faster turns this into a different scene — impatience instead of procedure.
- **The camera may rack focus** between the plate and the slip — **doing with the lens what the eye is doing**, which shows the audience the comparison instead of letting them watch it.
- **The door may open and someone may come out.** ⚠️ **The most likely addition, and the most damaging**: it completes a delivery that this shot exists to leave incomplete.
- **The box may be set down.** That is the third scene's action, and spending it here leaves that shot with nothing.
- **A blink may arrive early.** The blink is the shot's only ending; one in movement 2 or 3 ends the shot twice.
- **Music may be placed anyway.** ⚠️ **On this route `No BGM` is one of the few negations actually received**, so a bed arriving is **a violation of §16, not a matter of taste.** ⚠️ **The distant traffic is environment; do not let it acquire a pulse.**
- **Subtitles may be burned in.** ⚠️ **This route has an official notation for producing subtitles**（`【】`）, which makes the floor's clause **more necessary here than on either of the other two routes** — **and the clause is one of the two the route honors.**
