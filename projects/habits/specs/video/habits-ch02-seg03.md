# MiniMax H3 Full Specification — 『ハビッツ！！！』第二巻第1話「八十軒目」 第三のショット「指が、束の端にかかり、めくられない」 / 12s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である。

⚠️ **このショットは、この話の「止まる側」である。**（場面表——「**置いた後の一歩は、第3場面にある**」
「**第三場面＝C**（**「手が止まる」——次の番地の伝票をめくらない。反応軸の「解放しない」が、
そのまま為まいの宣言になる**）」）。**一拍は②である**——**この③は、その一拍のあとの静止である。**
**ゆえに②と③を一つのショットにしない**——**目に入ることと、めくらないことは、別の変化である。**

⚠️ **この作品の運搬は、ここでも完了しない。** **止まるのは手であって、運搬ではない**
——**束は、助手席に、残る。**

⚠️ **このショットは MiniMax H3 の経路である。** **§18 の見出しがモデルを名乗る**（`L18`）。
**添付は `key_image` ではない**——**絵コンテの画像そのもの**が動画全体の設計として渡る。
⚠️ **ボードは、まだ無い。** `specs/board/habits-ch02-seg03-board.md` は**在り処の宣言**である。

⚠️ **§18 `Negative Prompt` は、このサンプルの三枚で同一である。**
**ゆえにこの一枚——最後に読まれる位置——に、持続する禁制の増減は無い。**
（`L14` は、宣言の外にあるショットの §18 に増減があれば鳴る。**増やしていないから、鳴らない。**）
⚠️ **これは、無理に揃えたのではない。** **この三つのショットで、禁止が消える瞬間は一度も無い。**

⚠️ **このショットに、音楽は無い。** **床がそれを禁じている**（`specmap.BASE_NEGATIVES` の
`no background music`）——§16 `MUST NOT` と §18 `Negative Prompt` の両方が持つ。
⚠️ **これは「指定しなかった」のではない。** §14 と §18 `Audio Prompt` が
**「このショットは音楽を一切持たない」と明記する。**
⚠️ **当初はこのサンプルに限り床を外していた**が、**同日のうちに著者が撤回した**
——「**1話を分割するのであれば、やっぱりBGMは禁止しよう**」。**床は戻っている。**
⚠️ **三枚が同じ Negative を持つことは、変わっていない**——**床の節が1つ増えただけである。**

⚠️ **このショットに、開示の変化点は無い。** 変化点は②である。**この一枚は、その状態が続いている**
——`disclosure_state` に `present` と書くのは、**新しい開示ではなく、②のあとであるということ**である。

⚠️ **このショットの四つのパネルは、秒が等しい**（3s × 4）。**§8 の `STRUCTURED` / `NON_UNIFORM` は
様式の定数である**（`specmap`——プロモの30本すべてがこの値を持つ）。**この一枚の非一様性は、
秒ではなく密度にある**（sparse／sparse／held／held）。⚠️ **§19 に、そのとおり書いた。**

⚠️ **このショットは、草稿の第3節が持つものの一部しか運ばない。**
向かいの家に順に灯りがつくこと・一日の埃・サンバイザー・腰の重さ——
**それらは、この一話の三つのショットの、どこにも入っていない。** **落ちたのではなく、撮っていない。**

---

# 1. VIDEO

- Duration: `12s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One storyboard of four panels read in order, **each panel treated as its own scene and joined to the next by natural animation** (the source's own ②: 「各コマを独立したシーンとして扱い、静止画と静止画の間を自然なアニメーションでつないでください」). A single change: his hand is not yet on the bundle, and then his fingertips are on the edge of the top slip and have not turned it, with the engine still off. **Nothing completes.**

# 2. WORLD

## World Concept

2026, Japan — in this shot, the inside of a delivery van parked in Adachi, Tokyo, at the end of a working day. There is no magic, no institution and no secret organization: there is only a daily life in which the etiquette of the written name is thoroughly in place. **The name is the subject of this work, and the name the work is about is the one that is read the wrong way** — and this shot is where a man who has turned slips all day stops his hand on the next one and turns nothing.

## World Rules

- **The people in the work do not know that they are inside a film.**
- **The hand comes first and the face comes after. The order is not swapped.** ⚠️ **In this shot the face is not placed at all** — nothing has called him.
- **The sound is not a calling voice; it is the sound of paper and hands.** A calling voice is heard only on the side of the one called.
- **The carrying never completes.** The bundle stays on the passenger seat, smaller than it was.
- **The name lives on the side of being called, not on the side of being written.**
- **Only so many places can stand at once.** This shot places one.
- **No text is burned into this work.**
- **The writing seen in this work is print, ballpoint and pencil — and none of it is legible.**
- **This work speaks Japanese.**

## Visual Language

- Art Direction: Luminous realist anime, translated into the inside of a van at the end of a day. A Japanese delivery vehicle, 2026: a bundle of printed slips held by two rubber bands, its edge still square from the morning, the seat's dent from the morning still in it, the paper slightly cold because it has been in the van all day, and the low sun coming flat across the cabin. **The light, not the figure, is the subject** — and here the light is a low sun that is running out.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The palette is narrow — red sky, blue above it, the pale of paper, the brown of two rubber bands, and the warm side reduced to skin and to the paper.
- Texture: Layered atmospheric depth from near to far; the light lying on the top slip as a band with a straight edge, and the blue of the cabin's shadow beside it. No grain, no paper texture, no painterly stroke.
- Rendering: Clean anime lineart on the figure, drawn at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — **no second tone inside one piece of cloth, no gradient inside a single material, no soft airbrush.** Bloom in the low sun.
- Visual Density: Low. One focal point — the fingertips and the edge of the top slip — with generous negative space.
- Time: `日没前（八十軒目を出たあと）` — the end of the working day, before the light goes.
- Atmosphere: A van parked where a day of work has stopped, and no one watching it.

# 3. SUBJECTS

## 暮林蒼

- Reference: the frozen setting sheet — `distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md` (character sheet, revision 5) ＋ `expression.md` (expression sheet). **Both are the source of this work's 暮林蒼; the face is theirs and is not re-derived here.**
- Appearance: A man of twenty-six, a last-mile delivery courier — the tallest of the figures this work draws. **On the five axes the sheet fixes:** the forehead above the eyes is broad, and the cap is worn shallow so that breadth still reads; the cheekbones spread wide and set the width of the face; the jaw is short and its corner stands, and the chin itself is square; the nose is long with the tip falling; the ears are large and stand out sideways. **The sixth axis, the spacing of the eyes, is left to the style and is not fixed.** The age is not carried by the face: it is carried by the forearms — **the skin below the sleeve is darker than the face, and the skin the sleeve covers is paler than either.** Black hair, cut short enough to sit under a cap. The work jacket and cap of a delivery company; the terminal at one hip, with the belt dipping on that side alone; shoes worn down first at the outer heel. **The day has been worked in him: the jacket is creased where the belt and the seat have pressed it all day, and the hand that reaches for the bundle is the hand that has turned eighty slips since morning.** ⚠️ **The fatigue is carried by the forearms and the creases, never by the face** — the face is not placed.
- Behavior: The hand that has turned slips all day goes to the bundle and **does not turn it.** ⚠️ **This is the shot:** the fingers take the edge of the top slip, the pad of the finger rests on the paper, and **nothing is turned, nothing is started, nothing is switched on, and he does not move.** The foot stays on the brake and does not press it. The key stays in the ignition and is not turned. **The sinking into the seat is deeper than at any other hour of the day, and it is the only movement with weight in the shot.**
- Continuity Requirements: **Must preserve** — the face and the build of the frozen setting sheet; the cap worn shallow; the terminal at one hip; the two tones of the forearm; the same person as in the two shots before, on the same day, in the same jacket. **May change** — the position of the hands, the angle of the shoulders against the seat. ⚠️ **The face is given no expression: it is not placed.**

## nobody

- **No one else is in frame, and no one appears in the street.** The frame holds him alone in the cabin. **A bicycle passes outside and is never seen; a dog barks far off and is never seen.**

# 4. ENVIRONMENT

- Location: `宛名票の一行` — **the site of this episode's naming, not a room.** ⚠️ **In this shot the slip is in the bundle on the passenger seat and is not shown** — the naming happened in the shot before, and this shot is what follows it. **The key does not move; the frame does.**
- Environment Elements: The inside of the van — the driver's seat, the passenger seat with the morning's dent still in it, the windscreen and the two side windows, and the rear door left standing open behind him. Beyond the glass: a narrow street, house fronts, and the sky above them, red at the horizon and still blue overhead.
- Environmental Behavior: The low light lies across the cabin and its band on the bundle narrows and moves while he does not; the paper keeps the air it holds; the dust in the cabin moves. **These move through every panel and after the hand has stopped** — that is what keeps this from being a still.

# 5. OBJECTS

- **The bundle of slips on the passenger seat**, where the morning put it. **Two brown rubber bands, one thicker and one thinner, exactly as they were** — they have not shifted. **The edge of the stack is still square: the same hand squared it before setting it down this morning.** ⚠️ **The bundle is thinner than it was: the morning held one hundred and seventeen slips and this hour holds thirty-seven**（草稿 `draft_02-01_八十軒目.md` 305–309）。**No count of them appears in the frame, and no number is written on or beside the stack.**
- **The slips themselves**: print and ballpoint on paper, ordered, and **nowhere legible.** The top slip is the next address of the day; **its corner is what the fingertips take, and the audience is never shown what is written on it.**
- **The paper is slightly cold.** It has been in the van all day, and it is the same cold as the morning. ⚠️ **This is a temperature, and temperatures are not visible** — it is carried by the fingers and by nothing else.
- **The ignition key**, in the ignition and not turned. **The parking brake, on since the morning.**
- **The seat's dent**, made this morning and kept all day.
- ⚠️ **The square thing is in his jacket pocket, against his thigh, holding the day's photographs.** **It is not in frame in this shot** and is not raised — see §15.
- No other object is in frame.

# 6. REFERENCES

- REF_CHARACTER: 暮林蒼 — the setting sheet, revision 5 (`distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md`) (CRITICAL)
- REF_BOARD: `specs/board/habits-ch02-seg03-board.md` — the storyboard this generation is built on. **This is the H3 route's true attachment** — the image itself, not a `key_image`. ⚠️ **Not yet produced.**
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_STYLE: `luminous-anime` (HIGH)
- REF_SOURCE: `projects/habits/bible.yaml` and `projects/habits/ledger.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: A hand that has turned slips all day goes to the next one and does not turn it.
- Beginning: He steps back down the gravel — ten steps, the same as coming — and the rear door stands open behind him.
- Turn: He sits, and the seat takes him deeper than at any other hour.
- Peak: **His fingertips take the edge of the top slip.**
- Pull: **They do not turn it.** The engine is not started, the lights are not switched on, he does not move — and the light goes out on the bundle.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - PANEL 1 `0-3s` — density: `sparse` — One step back; down the step; **three steps of gravel make a sound.** Ten steps to the van — **the same as coming.** The rear door is left open.
  - PANEL 2 `3-6s` — density: `sparse` — The driver's door; he sits. **The sinking is the deepest of the day.** The key is already in the ignition and is not turned; the foot is over the brake and does not press it.
  - PANEL 3 `6-9s` — density: `held` — The bundle on the passenger seat, where the morning put it. **The two rubber bands are still two and have not shifted. The bundle is thinner.** The sky is red; **the light is coming onto the bundle too.**
  - PANEL 4 `9-12s` — density: `held` — **The hand goes to the bundle; the fingertips take the edge.** The pad of a finger is on the paper — the first slip's corner. **He does not turn it.** No engine, no lights, no movement. **The light goes out on the bundle.**
- Temporal Density: ⚠️ **The four panels are equal in seconds (3s each); the non-uniformity is in density** — sparse, sparse, held, held. **The weight of the shot is in the two held panels at the end, where nothing is done.**

# 9. ACTION

- `ACT_RETURN` — Before: he is standing at the entrance, the rear door open behind him. After: he is in the driver's seat, and the seat has taken his weight. **Nothing on the van is started.**
- `ACT_REACH` — Before: his hand is not on the bundle. After: **his fingertips are on the edge of the top slip and stay there.**
- `ACT_WITHHOLD` — Before: the key is in the ignition. After: **the key is still in the ignition, the engine is still off, and the lights are still off.** ⚠️ **This is not the absence of an action; it is the action.**

# 10. CAMERA

- Camera Language: Third person, inside the cabin. ⚠️ **This is the episode's one close shot of a hand** — run-10【ルックとカメラ】 grants the budget in the same constant as the camera's three sites (「カメラは、机上の手、左袖の名札、めくられる名簿の三箇所に置かれる」), and adds 「**手の近景を毎話一つ。**」 **Of this episode's three shots, this one spends it** — ⚠️ **発明（要承認）**: the source grants the budget of one and does not say which shot spends it. The lens sits at the level of the passenger seat, **close on the fingertips and the edge of the top slip**, with the low light lying across the paper.
- ⚠️ **The close is on the corner, never on the writing.** The budget buys proximity to a hand, not to a name — **the audience is not brought close to what he does not read.**
- Camera Events: One event only. `0-12s` — a very slow, weighted settle of a few centimetres, the camera placed rather than travelling. **Nothing is revealed by it.**
- Camera Behavior: No handheld, no whip, no shake, no push-in on the hand or on the paper, and **no movement toward the bundle** — the audience is not brought closer to what he does not read. **No sudden zoom, and no freeze-frame:** the shot is held by the light and the dust, not by stopping the picture. **Each panel is treated as its own scene; panel joins panel by natural animation.**

# 11. MOTION

## Subject Motion

A step back, a step down, ten steps of gravel, a door, and a body sitting into a seat until it stops. Then **a hand crossing to the passenger seat, fingertips taking the edge of the top slip, and stopping there.** ⚠️ **Nothing else moves in him** — no turn, no lift, no reach for the key, no shift of the foot.

## Object Motion

The bundle does not move. **The rubber bands do not shift. The top slip lifts at its corner under the fingertip and does not turn.** The key does not turn.

## Environmental Motion

The band of low light on the bundle narrows as the sun goes down, and the dust in the cabin moves through it. **Both keep moving after the hand has stopped** — **and when the light has gone, the dust is still moving.**

## Physical Characteristics

- Weight: The body has a day's weight in it: **the seat takes him deeper than at any other hour**, and the step down to the ground is taken with the whole foot.
- Inertia: The bundle has not shifted all day; the dent has not come out of the seat; the squared edge is still square. **Nothing in this shot recovers.**
- Acceleration: Each movement is one short acceleration into a stop and none of them overshoots. **Nothing is hurried and nothing is slow.**
- Fluidity: Continuous; no snap, no held cel, no stutter.
- Impact: The body meets the seat once, and it is the only impact in the shot.

# 12. EMOTION

- Emotional Arc: **The hand that has turned eighty slips since morning goes to the eighty-first and does not turn it.**
- Emotional Events: **The stop itself.** ⚠️ **There is no expression for it** — no face is placed, no sigh, no hand held to the head, no look at the sky. **The whole of it is in a fingertip resting on the corner of one slip, and the light going out.**

# 13. LIGHTING

- Base Lighting: A low sun outside, coming flat through the glass. **The sky is red at the horizon and still blue overhead**; the light on the bundle has a straight edge, with the strong side red and the weak side white, and the blue of the cabin's shadow beside it. Bloom in the low sun.
- Lighting Events: One — **the band of light on the bundle narrows through the held panels and goes out on the bundle** at the end of the shot. ⚠️ **The shot does not end on a black frame** — the cabin's shadow light remains; **it is the light on the paper that has gone.**

# 14. AUDIO

- Dialogue: **None.** No line is spoken in this shot, by him or by anyone else. ⚠️ **This is not a silent shot** — see Sound Effects. ⚠️ **The work still speaks Japanese**; §18 names it.
- Sound Effects: **Gravel — three steps that make a sound, the same as coming. Ten steps, the same as coming.** The driver's door closing; the seat taking his weight; the key already sitting in the ignition and not turned; **the small sound of a fingertip taking the edge of the top slip, once.** Then, from outside and never seen: **a bicycle passing and its sound receding, and a dog barking far off — once — and stopping.** ⚠️ **The dog does not bark again.** After that, **nothing**: the held panels are held without sound being added to them. Nothing is mixed forward.
- Music: **None, by specification.** ⚠️ **This is not an omission** — §16 and §18 `Negative Prompt` both carry the floor's `no background music`, and §14 states the silence as this shot's own decision. There is no bed, no score, no sting; **and nothing rises when the light goes out.**
- Environment: The inside of a closed van at the end of a day — the cabin's own quiet, the sound of the street through the glass, and the two sounds from outside that are never given a source in frame.

# 15. CONTINUITY

- Identity: The setting sheet, unsummarised, attached on every instance. **No drift of face, build or costume across the four panels.**
- Spatial: The driver's seat holds him at the frame's left from the second panel on, and the bundle sits on the passenger seat at the frame's right. **Neither is moved for the camera.**
- Temporal: **The same working day as the two shots before it, at its end.** Nothing in frame supplies a date.
- Visual: The palette and the style are the same in all three shots of this episode; **the light here is the low sun, not the fluorescent of the first nor the noon of the second.** Continuity of state across the episode: **the dent in the seat, the squared edge of the stack, the two rubber bands, and the jacket's creases are all from the morning.**
- Motion: Full animation, not limited. **The atmosphere is the primary mover** — the light and the dust — and the hand is the subject.
- Sound: Gravel, a door, a seat, one fingertip, a bicycle, and one bark. **No music. No calling voice as a sound effect.**
- ⚠️ **The square thing is in his pocket, holding the day's photographs, and it is not raised, not looked at, and not in frame.** **Its state is continuity, not action** — if it appears in the picture, the shot has taken on an action it does not have.

# 16. CONSTRAINTS

## MUST NOT

- **Nothing is started, switched on or turned:** no engine, no lights, no radio, no indicator, no wipers, no door opened again — **and the slip is not turned.**
- No second person; no passer-by; **no one seen in the street**; no cyclist put in frame; no dog put in frame.
- No face placed — **no expression, no look at the sky, no sigh, no hand to the head or the neck.**
- No legible text on any surface — on the slips, on the bundle, on the glass, on the dashboard. **The top slip is present under his finger and unreadable.**
- No count of the slips; no number written on or beside the stack; no romaji in place of the Japanese name.
- No camera movement toward the bundle, no push-in on the paper, no cut to a legible insert; **the audience is not shown what he does not read.**
- No freeze-frame, no still image, no held cel: the shot stays alive through light and dust.
- No calling voice as a sound effect; no spoken line; no voice-over; no narration.
- No music of any kind in this shot.
- No wall clock, no calendar, no digital timer, no date stamp, no dashboard readout rendered readable.
- No uniform pacing, no static slideshow of stills, no floaty weightless motion.
- No panel frames, panel numbers, captions or explanatory text carried over from the storyboard into the picture.
- No on-screen subtitles, no captions, no burned-in subtitles in any language.
- No background music — no bed, no score, no sting, and nothing that rises when the light goes out.
- No watermark.
- Not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces.

## MUST

- **The fingertips take the edge of the top slip and do not turn it.**
- **The engine is never started and the lights are never switched on.**
- The bundle is thinner than it was, and the two rubber bands are still two.
- **The light goes out on the bundle** at the end — and the picture does not go black with it.
- Three steps of gravel going back, the same as coming.

## PREFER

- The lens at the level of the passenger seat, the bundle in the lower middle of the frame, the low light lying across it with a straight edge, and the cabin's blue shadow beside it.

## ALLOW

- The band of light narrowing across the held panels; the dust moving in it; the rear door standing open behind him, out of focus.

# 17. GENERATION PRIORITIES

1. **The slip is not turned.** This outranks beauty and outranks legibility of feeling. **An eighty-first slip turned is a different episode.**
2. **Nothing is started** — no engine, no lights. The withholding is the action.
3. **No face is placed** — the stop is in the hand, not in an expression.
4. **The light goes out on the bundle** — the ending is the light's, and the picture stays alive after it.
5. **Japanese is what this work speaks** — named in §18, even though this shot holds no words.
6. One change only — the hand goes to the bundle and stops there. Nothing else happens.
7. Everything else.

---

# 18. MINIMAX H3 PROMPT MAPPING

## Master Prompt

A 12-second cinematic piece (16:9), luminous realist anime, inside a delivery van parked on a narrow street in Adachi, Tokyo, 2026, at the end of a working day. **The storyboard image attached to this generation is the design of the whole video: read its four panels in order 09 → 10 → 11 → 12, do not reorder them, do not skip one, and treat each panel as its own scene, joined to the next by natural animation.** One take, one change: his hand is not yet on the bundle, and then his fingertips are on the edge of the top slip and have not turned it, with the engine still off. [09] he steps back down the gravel — three steps that make a sound, ten steps to the van, the same as coming — and the rear door is left open. [10] he opens the driver's door and sits; **the seat takes him deeper than at any other hour**; the key is already in the ignition and is not turned, and his foot is over the brake and does not press it. [11] the bundle of slips on the passenger seat, where the morning put it: **two brown rubber bands still two and unshifted, the bundle thinner than it was**, the sky red, and the low light lying on the bundle. [12] **his hand goes to the bundle and his fingertips take the edge of the top slip; he does not turn it.** No engine, no lights, no movement — **and the light goes out on the bundle.** **Keep the compositions and the camera distance of the storyboard; keep the protagonist the same person in every panel** — same face, same hair, same cap worn shallow, same jacket, the same day worked into it. **Full colour, not black-and-white line art.** **The frame stays clean: no panel frames, no panel numbers, no captions and no subtitles are carried over from the storyboard into the picture.** **Do not add unnecessary characters or scenes.** **No person appears in this shot but him.** Ends held on the hand and the bundle as the light leaves it, and cuts. (One take, one change: the hand reaches the edge of the next slip and stops.)

## Visual Prompt

Luminous realist anime, translated into the inside of a van at the end of a day: the light, not the figure, is the subject, and here the light is a low sun running out. A man of twenty-six, a last-mile delivery courier and the tallest of the figures this work draws, his identity locked to the frozen setting sheet: the forehead broad with the cap worn shallow so the breadth still reads, cheekbones spreading wide and setting the width of the face, a short jaw whose corner stands with a square chin, a long nose with the tip falling, large ears standing out sideways, the spacing of the eyes left to the style; black hair cut short enough to sit under the cap; a work jacket and cap, a handheld terminal clipped at one hip so the belt dips on that side alone, the jacket creased where the belt and the seat have pressed it all day. The age is not carried by the face — it is carried by the forearms: the skin below the sleeve darker than the face, the skin the sleeve covers paler than either; **and by the day's creases.** **No expression is placed on the face in this shot.** The bundle of printed delivery slips on the passenger seat, held by two brown rubber bands, one thicker and one thinner, unshifted, its edge still square from the morning, **thinner than it was** — and no count of the slips written anywhere. **The top slip's corner is under his fingertip and nothing written on it is legible in any alphabet.** The cabin: the driver's seat holding the day's dent, the windscreen and two side windows, the rear door standing open behind him out of focus, and beyond the glass a narrow street and house fronts under a sky red at the horizon and still blue overhead. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp. The low light lying on the bundle as a band with a straight edge — red on the strong side, white on the weak side — and the cabin's blue shadow beside it. Bloom in the low sun; the cabin's dust moving through the band; generous negative space and low visual density.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. One step back and a step down; ten steps of gravel, three of which make a sound; a door; a body sitting into a seat until it stops, **sinking deeper than at any other hour**; then a hand crossing to the passenger seat, **fingertips taking the edge of the top slip and stopping there.** Everything else in him is still: no turn, no lift, no reach for the key, no shift of the foot. The rubber bands do not shift and the top slip lifts at its corner without turning. The band of low light on the bundle narrows through the held panels and goes out on the bundle, **and the dust keeps moving after the hand has stopped and after the light has gone.** No impact beyond the body meeting the seat, no motion blur smears, no stutter, **no freeze-frame or still image**. **The panels are joined by movement, and each panel is its own scene.**

## Camera Prompt

Third person, inside the cabin — **this is the episode's one close shot of a hand: the lens is at the level of the passenger seat, close on the fingertips and the edge of the top slip, with the low light lying across the paper. The close is on the corner and never on the writing.** One camera event only: a very slow, weighted settle of a few centimetres over the whole take, revealing nothing. **The camera never moves toward the bundle and never brings the audience closer to the paper.** **Keep the storyboard's compositions and its camera distance.** No handheld, no whip, no shake, no push-in, no sudden zoom, no unnatural rotation, no cut to an insert of the slip, **and no freeze-frame.** Each panel is treated as its own scene; panel joins panel by natural animation.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of everything this work holds. **No line is spoken in this shot: he says nothing, and there is no voice-over and no narration.** **The Japanese is not spoken here; it is what this work is** — and **nothing is written on screen**: no subtitles, no captions, in any language, and no panel numbers or storyboard text carried into the picture. Sound effects, nothing mixed forward: **gravel underfoot — three steps that make a sound, ten steps to the van, the same as coming**; a driver's door closing; a seat taking a body's weight; a key sitting in the ignition and not turning; **and once, small, the sound of a fingertip taking the edge of the top slip.** From outside and never seen: **a bicycle passing and its sound receding, and a dog barking far off — once — and stopping; it does not bark again.** Then nothing more: **the held panels are held without any sound being added to them.** Ambient: the quiet inside a closed van at the end of a day, with the street coming through the glass. **Music: none — this shot carries no music of any kind.** No bed, no score, no sting, and **nothing rises when the light goes out.** **No calling voice as a sound effect**; no spoken name; no crowd.

## Negative Prompt

no legible name text, no legible name on any in-world prop, no legible text on the delivery slips, no legible text on any surface, no on-screen count of the slips, no number written beside the bundle, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no signature, no handwriting by the courier, no calling voice as a sound effect, no face before the name is called, no character added beyond the storyboard, no unnecessary character, no additional person beyond the storyboard, no unnecessary second courier, no colleague invented at the counter, no passer-by added, no bystander added, no second person with the courier's face, no second person wearing his cap or his jacket, no completed delivery, no receiving hand, no opened door, no signature taken, no smile, no tears, no fear, no exaggerated expression, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no cuts to unrelated locations, no panel frames, no panel numbers, no storyboard text in the picture, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no swelling music, no watermark, no morphing or drifting facial identity, no specimen chart, no measured chart of steps, no figure written beside any step, no furigana field, no printed form, no name written by the subject, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket worn over the work jacket, no outer garment, no identifying clothing, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces, no rounded jaw, no short nose, no small ears, no face younger than the age stated

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-ch02-seg03-12s-01`
- Segment ID: `03-1`
- Specification Version: `0.1.1`
- Generation Date: `—`

## Resolved Values

- Duration: `12s`
- References: `REF_CHARACTER (setting sheet rev.5, CRITICAL) ／ REF_BOARD (specs/board/habits-ch02-seg03-board.md, CRITICAL — the attachment of this route) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`
- Temporal Structure: `4 panels — 3s each, equal. ⚠️ The non-uniformity of this shot is in density, not in seconds: sparse / sparse / held / held. The held panels = PANEL 3 and PANEL 4 at 3s each (50% of the shot)`
- Camera Events: `1 event as listed in §10. Four panels, each treated as its own scene, joined by natural animation, no freeze-frame`
- Action Events: `ACT_RETURN → ACT_REACH → ACT_WITHHOLD`
- Audio Events: `no dialogue ／ gravel, door, seat, key, one fingertip ／ a bicycle and one bark from outside, never seen ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, made from one storyboard of four panels`

# 20. ITERATION

## Version

`0.1.1` — **not yet generated. Revised from `0.1.0` on 2026-09-20.** **The storyboard this specification depends on does not exist yet.**

## Observed Problems

- _(this shot has not been generated, so there are no observations of it.)_ ⚠️ **But this is not `_(none yet)_` either: the revision was forced from outside.** The episode's first shot, `habits-ch02-seg01`, was generated once and came back with **two defects — the two figures collapsed into one, and two places ran together as one room.** Both were traced to the §18 string, and **the second clause was in this specification as well.** They are corrected here in the same revision.

## Anticipated risks (to check in the first generation)

- **The slip may be turned.** This is the whole shot. A page lifted, a corner released, an eye dropped to read it — any of them turns the episode's held hand into an action.
- **The engine may start.** A key turning, a starter, an indicator, a dashboard lighting up: **the shot's action is the withholding**, and starting ends it.
- **The camera may come closer to the paper.** A push-in on the bundle, or a cut to an insert, tells the audience what he does not read.
- **The face may be given an expression.** A sigh, a look at the sky, a hand to the neck. **None of them is in the source and all of them are easier than a fingertip that stops.**
- **The ending may go black.** The ending is **the light leaving the paper**, not the picture stopping — the cabin's shadow light stays, and the dust keeps moving.
- **The shot may freeze.** A held panel rendered as a still image with only the dust moving is the failure mode next to this design; §18 forbids the freeze-frame by name.
- **The bundle's state may drift** — the rubber bands slipping, the edge coming unsquared, the dent gone from the seat. **All three are the day's record in prop form.**
- **Music may be placed anyway.** The floor's clause is in force and §18 `Negative Prompt` carries it. **The light going out is not a cue** — a bed arriving as the frame darkens is **a violation of §16, not a matter of taste.**

- **The bicycle or the dog may be put in frame.** Neither is ever seen; **only their sound exists, and the dog barks once.**
