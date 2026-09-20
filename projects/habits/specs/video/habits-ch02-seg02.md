# MiniMax H3 Full Specification — 『ハビッツ！！！』第二巻第1話「八十軒目」 第二のショット「箱が、玄関の前に置かれ、一行が、目に入る」 / 14s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である。

⚠️ **このショットは、この一話の「一拍」である。**（場面表——「一拍の位置＝第2場面。運搬が止まる場所。」
「**運搬は、ここでも完了しない。** 置くことは、届けることではない。」）
**このサンプルで最も長い一枚である**（14秒。①は10秒、③は12秒）——
**一拍に最大の秒を与える。三枚ともコマ数は4である。差は、密度ではなく、秒である。**

⚠️ **このショットは MiniMax H3 の経路である。** **§18 の見出しがモデルを名乗る**（`L18`）。
**添付は `key_image` ではない**——①で作った**絵コンテの画像そのもの**が動画全体の設計として渡る。
ゆえに `## 6. REFERENCES` の `REF_BOARD` が、この経路で最も重い参照である。
⚠️ **ボードは、まだ無い。** `specs/board/habits-ch02-seg02-board.md` は**在り処の宣言**である。

⚠️ **このショットに、会話は無い。**（本文——「誰も、出てこない。」）
**ゆえに §18 `Audio Prompt` は、言葉を持たない。** **それでも言語を名乗る**——
**「この作品は日本語を話す」は、台詞の有無によらない**（`L27`。無言の一枚に言語を書かないと、
生成器は自分の既定で埋める——実測 2026-09-18、中国語の字幕が焼かれた）。

⚠️ **このショットに、開示の変化点がある。**（`ledger.yaml`——宛名票の一行。`present`。）
**`negative: covered` が宣言されている**——**ゆえに `L10` は、この一枚の §18 Negative を
①の §18 Negative と節の集合で突き合わせる。**
**「覆った」は「同じである」を要求する**（`covered` の定義）。**だから三枚の Negative は同一である。**
⚠️ **無理に揃えたのではない。** **この三つのショットで、禁止が消える瞬間は一度も無い。**

⚠️ **このショットに、音楽は無い。** **床がそれを禁じている**（`specmap.BASE_NEGATIVES` の
`no background music`）——§16 `MUST NOT` と §18 `Negative Prompt` の両方が持つ。
⚠️ **これは「指定しなかった」のではない。** §14 と §18 `Audio Prompt` が
**「このショットは音楽を一切持たない」と明記する。**
⚠️ **当初はこのサンプルに限り床を外していた**が、**同日のうちに著者が撤回した**
——「**1話を分割するのであれば、やっぱりBGMは禁止しよう**」。**床は戻っている。**

⚠️ **`role` は 所作 であって 開示 ではない。**（`habits-ch02-seg02.yaml`）
**画面の内側で起きるのは「置く」ことと「目が行く」ことである。** 開示の設計は台帳が持つ。

⚠️ **このショットは、草稿の第2節が持つものの一部しか運ばない。**
細い路地・畳むミラー・消火栓・カーブミラー・午前の四十軒・昼の十分・犬のいる四軒目——
**それらは、この一話の三つのショットの、どこにも入っていない**（`habits-ch02-seg02.yaml` の拍は
八十軒目そのものだけを立てている）。**落ちたのではなく、撮っていない。記録として書く。**

---

# 1. VIDEO

- Duration: `14s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One storyboard of four panels read in order, **each panel treated as its own scene and joined to the next by natural animation** (the source's own ②: 「各コマを独立したシーンとして扱い、静止画と静止画の間を自然なアニメーションでつないでください」). A single change: the box is on the truck bed and the top line of the address slip has not entered his eye, and then the box is down in front of the entrance and the line has entered it. **His eyes do not rise. Nobody comes out.**

# 2. WORLD

## World Concept

2026, Japan — in this shot, a residential plot in Adachi, Tokyo, in the middle of a working day. There is no magic, no institution and no secret organization: there is only a daily life in which the etiquette of the written name is thoroughly in place. **The name is the subject of this work, and the name the work is about is the one that is read the wrong way** — which is why every name on every in-world prop is printed or handwritten and nowhere legible. **Here the name is on the side of a box, and the work's whole first episode rests on one line of it entering a man's eye without his face moving to meet it.**

## World Rules

- **The people in the work do not know that they are inside a film.**
- **The hand comes first and the face comes after. The order is not swapped. The face is placed only after the name has been called.**
- **The sound is not a calling voice; it is the sound of paper and hands.** A calling voice is heard only on the side of the one called.
- **The carrying never completes.** The box is set down; it is not delivered. **Nobody comes out.**
- **The name lives on the side of being called, not on the side of being written.**
- **Only so many places can stand at once.** This shot places one.
- **No text is burned into this work.**
- **The writing seen in this work is print, ballpoint and pencil — and none of it is legible.**
- **This work speaks Japanese.**

## Visual Language

- Art Direction: Luminous realist anime, translated into a residential plot at midday. A Japanese delivery site, 2026: a cardboard box with a printed address slip glued to its side, peeling at one edge with dust in the lift, four fields ruled on the slip, gravel in front of the entrance, a single step, and a gatepost with ivy that stops partway up. **The light, not the figure, is the subject** — and here the light is the hard flat noon of a narrow street.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The palette is narrow — the pale of cardboard, the white of the slip, the grey of the gravel, the warm side reduced to skin and to the leaves.
- Texture: Layered atmospheric depth from near to far; dust suspended over the gravel and standing in the lift of the slip's lifted edge. No grain, no paper texture, no painterly stroke.
- Rendering: Clean anime lineart on the figure, drawn at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — **no second tone inside one piece of cloth, no gradient inside a single material, no soft airbrush.**
- Visual Density: Low. One focal point — the hands, the box, and the slip — with generous negative space.
- Time: `昼（八十軒目）` — the middle of a working day, in the open.
- Atmosphere: A street where a delivery is being made and no one is watching it.

# 3. SUBJECTS

## 暮林蒼

- Reference: the frozen setting sheet — `distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md` (character sheet, revision 5) ＋ `expression.md` (expression sheet). **Both are the source of this work's 暮林蒼; the face is theirs and is not re-derived here.**
- Appearance: A man of twenty-six, a last-mile delivery courier — the tallest of the figures this work draws. **On the five axes the sheet fixes:** the forehead above the eyes is broad, and the cap is worn shallow so that breadth still reads; the cheekbones spread wide and set the width of the face; the jaw is short and its corner stands, and the chin itself is square; the nose is long with the tip falling; the ears are large and stand out sideways. **The sixth axis, the spacing of the eyes, is left to the style and is not fixed.** The age is not carried by the face: it is carried by the forearms — **the skin below the sleeve is darker than the face, and the skin the sleeve covers is paler than either.** Black hair, cut short enough to sit under a cap. The work jacket and cap of a delivery company; a handheld terminal clipped at one hip so that the belt dips on that side alone; shoes worn down first at the outer heel. **This is the eighth house of the day, in the afternoon of the same day as the first shot, and nothing about him is dirtier or looser than it was that morning.**
- Behavior: His one consistent movement is to stop — and in this shot it is the foot that stops and the eye that stops. **The foot counts the gravel: three steps, and the fourth makes no sound. The foot takes the step at the entrance without the eye leaving the slip. The eye stops on the top line and does not rise.** He does not look up, does not knock, does not call out. **He takes the proof photograph twice, because the first one cut the edge of the box.**
- Continuity Requirements: **Must preserve** — the face and the build of the frozen setting sheet; the cap worn shallow; the terminal at one hip; the two tones of the forearm; the same person as in the first and third shots. **May change** — the position of the hands, the angle of the head, the fall of light across him. **The face is not given a new expression here: it is not placed at all.**

## nobody

- **No second person appears in this shot, and none comes out of the house.** The frame holds him alone. ⚠️ **This is not carried by the Negative** (the three shots share one Negative, and the first shot has a person in frame) — **it is carried by the positive slots**, and by the source's own rule that no character and no scene are added beyond the board. ⚠️ **A weak guard, and it is recorded as a hole**（`habits-ch02-seg02.yaml`／`ledger.yaml` の該当箇所）.

# 4. ENVIRONMENT

- Location: `宛名票の一行` — **the site of this episode's naming, not a room.** ⚠️ **Of the episode's three shots, this is the only one where the slip itself is inside the frame.** The key does not move; the frame does.
- Environment Elements: The front of a private house — gravel, a single step at the entrance, a closed door, a gatepost with ivy that has been cut and stops partway up. The narrow street behind it, and the truck at the kerb with its rear door raised. **The house is old; the paint on the step edge is worn through at the middle, where feet land.**
- Environmental Behavior: Dust moves over the gravel and stands in the lift of the slip's lifted edge; the leaves on the gatepost move. **These move through every panel and after the hands have stopped.** There is no wind event.

# 5. OBJECTS

- **The box.** Cardboard, taken from the front of the truck bed — **not the front of the stack in the address order, but the one within reach.** It has weight: the arm drops and then recovers. **Its corner presses into the palm.** The box is set down in front of the entrance and no further.
- **The address slip**, glued to the side of the box. **Peeling: the edge is lifted, and dust has gone into the lift. Four fields are ruled on it.** ⚠️ **The four fields are ruled lines and headings only — no name on it is legible, and none is in any alphabet a viewer can read.** The topmost line is the one that enters his eye; **it is not shown to the audience as text — the shot shows a man's eye stopping, not a document.**
- **The square thing.** ⚠️ **The source names it only by its shape**（草稿——「四角いものを、箱へ、向ける。」）。**This specification does not name it either, and does not decide what it is.** It is raised toward the box twice; **its screen lights and its content is never legible** — the lower part of the framed image holds the step, and the box's edge sits inside the frame the second time.
- **The step at the entrance** — **one step, not two, not three.** The foot takes it while the eye is still down.
- **The truck's rear door**, raised and left raised, and the boxes still on the bed behind — **a stack in address order, of which this box was the nearest.**
- No other object is in frame.

# 6. REFERENCES

- REF_CHARACTER: 暮林蒼 — the setting sheet, revision 5 (`distill-essence-engine/examples/habits/character/メイン/02_暮林蒼/prompt.md`) (CRITICAL)
- REF_BOARD: `specs/board/habits-ch02-seg02-board.md` — the storyboard this generation is built on. **This is the H3 route's true attachment** — the image itself, not a `key_image`. ⚠️ **Not yet produced.**
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_STYLE: `luminous-anime` (HIGH)
- REF_SOURCE: `projects/habits/bible.yaml` and `projects/habits/ledger.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: A box is set down in front of an entrance and one line of the slip on its side enters a man's eye.
- Beginning: The truck is stopped, the rear door raised, and the box is still on the bed.
- Turn: The box is set down and the hands leave it; the square thing is raised and the screen lights.
- Peak: **The top line of the slip enters his eye — and the eye does not rise.**
- Pull: The foot is already taking the step, and the shot ends with the eye still down and nobody coming out.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - PANEL 1 `0-4s` — density: `sparse` — The truck stops; the engine stops; **the key is not pulled.** The rear door is raised.
  - PANEL 2 `4-7s` — density: `sparse` — The nearest box is taken. It has weight: **the arm drops and then recovers.** The walk starts, the stride narrow. **Three steps of gravel make a sound; the fourth makes none.**
  - PANEL 3 `7-10s` — density: `sparse` — The box is set down in front of the step; the hands leave it. The square thing is raised toward it; **the screen lights; the box's edge is cut; it is taken again.**
  - PANEL 4 `10-14s` — density: `held` — The slip on the box's side: peeling, the edge lifted, four fields. **The top line enters his eye.** Meanwhile the foot is taking the step; **the eye is not raised. Nobody comes out.**
- Temporal Density: The held panel is the last one and it is the longest. **The weight of this episode is in the beat where nothing is done about what has been seen.**

# 9. ACTION

- `ACT_SET_DOWN` — Before: the box is carried in both hands. After: the box is on the ground in front of the step and the hands have left it. **This is a placement, not an arrival.**
- `ACT_RECORD` — Before: the square thing is at his side. After: it has been raised twice and the screen has lit twice. ⚠️ **The source places no sound at it** — the light is the event.
- `ACT_LOOK` — Before: the eye has not reached the slip. After: **the eye is on the top line and stays there.** ⚠️ **The eye does not rise** — this is the action, and its restraint is the shot.

# 10. CAMERA

- Camera Language: Third person, **medium**, placed at the hand and then at the box — **this work puts the camera at one of three sites** (run-10【ルックとカメラ】: 「カメラは、机上の手、左袖の名札、めくられる名簿の三箇所に置かれる」). Here the lens sits below his eye line: **the slip is seen because he is looking at it, and the frame never turns to read it.**
- ⚠️ **This shot is not the episode's one hand-close** — run-10's 「**手の近景を毎話一つ。**」 is spent in the third shot. ⚠️ **The hand on the box is the subject of this shot, and the shot still keeps its distance from it.** **A close-up here would spend the episode's budget on the wrong hand** — the episode's close belongs to the hand that stops. ⚠️ **The camera does not become the square thing.** We do not see what the screen holds; we see the box, and the light on his hands.
- Camera Events: One event only. `0-14s` — a very slow, weighted settle of a few centimetres, the camera placed rather than travelling. **Nothing is revealed by it.**
- Camera Behavior: No handheld, no whip, no shake, no push-in. **No sudden zoom, and no move toward the slip** — the frame keeps the storyboard's compositions and its camera distance. **Each panel is treated as its own scene; panel joins panel by natural animation.**

# 11. MOTION

## Subject Motion

An arm drops under weight and recovers; a hand sets a box down and leaves it; a hand raises the square thing twice; **a foot makes three sounds on gravel and none on the fourth step; a foot takes the step at the entrance; an eye stops.** All of them finish and stop.

## Object Motion

The box travels from the truck bed to the ground and does not move again. The slip's lifted edge moves with the air it holds; **the dust inside the lift does not fall out.** The screen of the square thing lights and goes dark twice.

## Environmental Motion

Dust moves over the gravel, and the leaves on the gatepost move. **Both keep moving after the hands have stopped** — that is what keeps this from being a still.

## Physical Characteristics

- Weight: The box has weight enough that the arm drops before it is recovered and the stride narrows. **It comes to rest and stays.**
- Inertia: The box does not slide when it is set down; the slip does not settle flat.
- Acceleration: The lift of the box out of the bed is one pull; the setting down is one descent into a stop; **nothing is hurried and nothing is slow.**
- Fluidity: Continuous; no snap, no held cel, no stutter.
- Impact: The box meets the ground once, with the sound arriving with it.

# 12. EMOTION

- Emotional Arc: The interval between a line entering an eye and nothing being done about it.
- Emotional Events: **The eye stopping — and the face not following it.** The foot continues; the body does the job; the eye is where it is.

# 13. LIGHTING

- Base Lighting: Hard, flat midday light with the style's bloom on the pale surfaces. The sun is high and slightly behind the camera; the slip's white is the brightest thing in the frame and the box's edge is the darkest. Deep cyan in the shadow the truck throws. Dust suspended over the gravel.
- Lighting Events: Two — **the screen of the square thing lights, and the light it throws onto the box and onto his hands is the only new light in the shot.** It does this twice, and both times it goes out at once.

# 14. AUDIO

- Dialogue: **None.** No line is spoken in this shot, by him or by anyone else, and **nobody comes out of the house.** ⚠️ **This is not a silent shot** — see Sound Effects. ⚠️ **The work still speaks Japanese**; §18 names it.
- Sound Effects: **Gravel, three steps — and the fourth step, which makes no sound.** That absence is the sound design of this shot and it is placed, not omitted. Then: the rear door of the truck rolling up and staying up; cardboard taking weight as it comes off the bed; the box meeting the ground; the rubber of a shoe taking the step; and, small, the paper of the slip's lifted edge. **Nothing is mixed forward.**
- Music: **None, by specification.** ⚠️ **This is not an omission** — §16 and §18 `Negative Prompt` both carry the floor's `no background music`, and §14 states the silence as this shot's own decision. There is no bed, no score, no sting, and nothing rises at the held panel.
- Environment: An open residential street in the middle of the day. Distant traffic and the leaves on the gatepost are permitted; a musical sting is not. **No calling voice as a sound effect** — and here there is no voice at all.

# 15. CONTINUITY

- Identity: The setting sheet, unsummarised, attached on every instance. **No drift of face, build or costume across the four panels.**
- Spatial: The truck is behind him at the frame's left in the first two panels; the entrance is ahead of him from the third panel on. **Neither is moved for the camera.**
- Temporal: The same working day as the shot before and the shot after. **The day is at its middle, and nothing in frame supplies a date.**
- Visual: The palette and the style are the same in all three shots of this episode. **The light is the noon of this shot, not the fluorescent of the first nor the low sun of the third.**
- Motion: Full animation, not limited. **The atmosphere is the primary mover**; the hands, the foot and the eye are the subject.
- Sound: Gravel, the door, the box, the step, and one silence placed inside them. **No music. No calling voice as a sound effect.**

# 16. CONSTRAINTS

## MUST NOT

- No person coming out of the house; no resident at the door; no passer-by; **no character added beyond the storyboard.**
- No completed delivery: no receiving hand, no opened door, no signature, no handing over — **the box is set down and left.**
- **The eye does not rise.** No face turned up, no head raised to the door, no knock, no calling out.
- No legible text on any surface — on the slip, on the box, on the screen of the square thing, on the house. **The slip is present and unreadable; the screen lights and shows nothing a viewer can read.**
- No romaji in place of the Japanese name; no real-world alphabet in frame.
- No camera move toward the slip, no push-in on the writing, no cut to a legible insert. **The audience is not shown what he reads.**
- No second step, no stairs, no step counted aloud or written down.
- No calling voice as a sound effect; no spoken line; no voice-over; no narration.
- No music of any kind in this shot.
- No wall clock, no calendar, no digital timer, no date stamp, no house number rendered readable.
- No uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion.
- No panel frames, panel numbers, captions or explanatory text carried over from the storyboard into the picture.
- No on-screen subtitles, no captions, no burned-in subtitles in any language.
- No background music — no bed, no score, no sting, and nothing that rises at the held panel.
- No watermark.
- Not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces.

## MUST

- **The top line of the slip enters his eye and the eye does not rise.**
- Three audible steps of gravel and a fourth that makes no sound.
- **One step at the entrance, not more**, taken while the eye is down.
- The slip is visible to the camera and legible to nobody.
- Nobody comes out.

## PREFER

- The lens below his eye line, with the box and the slip in the lower half of the frame and his hands at the bottom edge; the screen's light falling on his hands as the only new light.

## ALLOW

- The truck's raised rear door at the frame's left; dust over the gravel; the leaves on the gatepost moving.

# 17. GENERATION PRIORITIES

1. **The eye does not rise** — the line enters it and the face does not follow. This outranks beauty and outranks legibility of feeling.
2. **Nobody comes out** — the placement does not complete, and no one receives it.
3. **No name is readable** — the slip is present on screen and illegible. Either half of that failing is a different shot.
4. **The fourth step makes no sound** — the count of the gravel is the shot's sound design.
5. **Japanese is what this work speaks** — named in §18, even though this shot holds no words.
6. One change only — the box is set down and the line enters his eye. Nothing else happens.
7. Everything else.

---

# 18. MINIMAX H3 PROMPT MAPPING

## Master Prompt

A 14-second cinematic piece (16:9), luminous realist anime, in front of a private house on a narrow street in Adachi, Tokyo, 2026, in the middle of a working day. **The storyboard image attached to this generation is the design of the whole video: read its four panels in order 05 → 06 → 07 → 08, do not reorder them, do not skip one, and treat each panel as its own scene, joined to the next by natural animation.** One take, one change: the box is on the truck bed and the top line of the address slip has not entered his eye, and then the box is down in front of the entrance and the line has entered it. [05] the truck stops, the engine stops, the key is not pulled, and the rear door is raised. [06] the nearest box is taken — it has weight, the arm drops and recovers — and he walks with a narrow stride; three steps of gravel make a sound and the fourth makes none. [07] the box is set down in front of the step, the hands leave it, and a small square object is raised toward it twice, its screen lighting. [08] the address slip glued to the box's side is peeling with dust in the lift of its edge and four ruled fields, and the top line of it enters his eye; meanwhile his foot is already taking the single step at the entrance, **and his eye does not rise. Nobody comes out of the house.** **Keep the compositions and the camera distance of the storyboard; keep the protagonist the same person in every panel** — same face, same hair, same cap worn shallow, same jacket. **Full colour, not black-and-white line art.** **The frame stays clean: no panel frames, no panel numbers, no captions and no subtitles are carried over from the storyboard into the picture.** **Do not add unnecessary characters or scenes.** **No person appears in this shot but him.** Ends on the eye still down, and cuts. (One take, one change: the box is set down and one line of the slip enters his eye.)

## Visual Prompt

Luminous realist anime, translated into a residential plot at midday: the light, not the figure, is the subject, and here the light is the hard flat noon of a narrow street. A man of twenty-six, a last-mile delivery courier and the tallest of the figures this work draws, his identity locked to the frozen setting sheet: the forehead broad with the cap worn shallow so the breadth still reads, cheekbones spreading wide and setting the width of the face, a short jaw whose corner stands with a square chin, a long nose with the tip falling, large ears standing out sideways, the spacing of the eyes left to the style; black hair cut short enough to sit under the cap; a work jacket and cap, a handheld terminal clipped at one hip so the belt dips on that side alone. The age is not carried by the face — it is carried by the forearms: the skin below the sleeve darker than the face, the skin the sleeve covers paler than either. **No expression is placed on the face in this shot.** The box: pale cardboard with a printed address slip glued to its side, the slip peeling at one edge with dust caught in the lift and four ruled fields on it — **ruled lines and headings only, and no name on it is legible in any alphabet.** A small square object in his hand, unnamed and unreadable, whose screen lights twice and shows nothing a viewer can read. Gravel in front of the entrance, a single worn step, a closed door, and a gatepost with ivy that has been cut and stops partway up. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp. Saturated where the light falls, deep cyan in the shadow the truck throws; the pale of cardboard, the white of the slip and the grey of the gravel. Bloom on the pale surfaces, dust suspended and individually rendered over the gravel, generous negative space and low visual density.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. An arm dropping under weight and recovering; a hand setting a box down and leaving it; a hand raising the square thing twice, with the screen lighting and going dark each time; **a foot making three sounds on gravel and none on the fourth step; a foot taking the single step at the entrance; and an eye stopping.** Every movement finishes and stops, and none of them overshoots. Dust moves over the gravel and the leaves on the gatepost move — **both keep moving after the hands have stopped.** No impact beyond the box meeting the ground once, no motion blur smears, no stutter, no held frames. **The panels are joined by movement, and each panel is its own scene.**

## Camera Prompt

Third person, medium, placed at the hand and then at the box — **the lens sits below his eye line throughout: the slip is seen because he is looking at it, and the frame never turns to read it. Keep this framing medium; do not close on the hand or on the paper.** One camera event only: a very slow, weighted settle of a few centimetres over the whole take, revealing nothing. **The camera never becomes the square object and never moves toward the writing.** **Keep the storyboard's compositions and its camera distance.** No handheld, no whip, no shake, no push-in, no sudden zoom, no unnatural rotation, no cut to an insert of the slip. Each panel is treated as its own scene; panel joins panel by natural animation.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of everything this work holds. **No line is spoken in this shot: he says nothing, nobody comes out of the house, and there is no voice-over and no narration.** **The Japanese is not spoken here; it is what this work is** — and **nothing is written on screen**: no subtitles, no captions, in any language, and no panel numbers or storyboard text carried into the picture. Sound effects, nothing mixed forward: **gravel underfoot — three steps that make a sound, and a fourth that makes none**, and that absence is placed rather than left out; the rear door of the truck rolling up and staying up; cardboard taking weight as it comes off the bed; the box meeting the ground once; the rubber of a shoe taking the step; and the paper of the slip's lifted edge, small. Ambient: an open residential street in the middle of the day, distant traffic and leaves on a gatepost. **Music: none — this shot carries no music of any kind.** No bed, no score, no sting, no drum, and nothing rises at the end. **No calling voice as a sound effect**; no spoken name; no crowd; no dog.

## Negative Prompt

no legible name text, no legible name on any in-world prop, no legible text on the delivery slips, no legible text on any surface, no on-screen count of the slips, no number written beside the bundle, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no signature, no handwriting by the courier, no calling voice as a sound effect, no face before the name is called, no character added beyond the storyboard, no unnecessary character, no additional person beyond the storyboard, no unnecessary second courier, no colleague invented at the counter, no passer-by added, no bystander added, no second person with the courier's face, no second person wearing his cap or his jacket, no completed delivery, no receiving hand, no opened door, no signature taken, no smile, no tears, no fear, no exaggerated expression, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no cuts to unrelated locations, no panel frames, no panel numbers, no storyboard text in the picture, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no swelling music, no watermark, no morphing or drifting facial identity, no specimen chart, no measured chart of steps, no figure written beside any step, no furigana field, no printed form, no name written by the subject, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket worn over the work jacket, no outer garment, no identifying clothing, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces, no rounded jaw, no short nose, no small ears, no face younger than the age stated

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-ch02-seg02-14s-01`
- Segment ID: `02-1`
- Specification Version: `0.1.1`
- Generation Date: `—`

## Resolved Values

- Duration: `14s`
- References: `REF_CHARACTER (setting sheet rev.5, CRITICAL) ／ REF_BOARD (specs/board/habits-ch02-seg02-board.md, CRITICAL — the attachment of this route) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`
- Temporal Structure: `4 panels, NON_UNIFORM — 4s / 3s / 3s / 4s. The held panel = PANEL 4 at 4s (29%)`
- Camera Events: `1 event as listed in §10. Four panels, each treated as its own scene, joined by natural animation`
- Action Events: `ACT_SET_DOWN → ACT_RECORD → ACT_LOOK`
- Audio Events: `no dialogue ／ three gravel steps ＋ one placed silence ／ rear door, box, step, paper ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, made from one storyboard of four panels`

# 20. ITERATION

## Version

`0.1.1` — **not yet generated. Revised from `0.1.0` on 2026-09-20.** **The storyboard this specification depends on does not exist yet.**

## Observed Problems

- _(this shot has not been generated, so there are no observations of it.)_ ⚠️ **But this is not `_(none yet)_` either: the revision was forced from outside.** The episode's first shot, `habits-ch02-seg01`, was generated once and came back with **two defects — the two figures collapsed into one, and two places ran together as one room.** Both were traced to the §18 string, and **both clauses were in this specification as well.** They are corrected here in the same revision.

## Anticipated risks (to check in the first generation)

- **The screen may become legible.** The square thing's screen is a surface the generator will want to fill. **A readable name, a map, or a UI there ends the work's premise** — the audience must not be shown what he reads.
- **The camera may turn to read the slip.** A push-in on the writing, or a cut to an insert, converts this shot from "a man's eye stops" into "the audience is told a name". **The frame keeps its distance.**
- **A head may rise.** The whole shot is the eye stopping and the face not following; a raised head, a knock, or a call at the door is a different shot.
- **Someone may come out.** The resident at the door is the most likely addition, and the most damaging: it completes the delivery.
- **The delivery may complete** — a receiving hand, an opened door, a signature taken.
- **The step may multiply.** The source fixes one step at this house; two or three steps belong to other houses of the day.
- **The gravel may lose its silence.** The fourth step's missing sound is the design; four equal steps is a different shot.
- **A number may be rendered readable** on the box, the slip, the house or the screen — including a house number, which this shot must not supply.
- **Music may be placed anyway.** The floor's clause is in force and §18 `Negative Prompt` carries it, so a bed arriving — most likely at the held panel, where a generator reaches for one — is **a violation of §16, not a matter of taste.** ⚠️ **The distant traffic is environment; do not let it acquire a pulse.**
