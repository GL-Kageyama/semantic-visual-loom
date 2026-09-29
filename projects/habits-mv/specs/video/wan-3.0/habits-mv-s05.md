# ═══ 演出要約 ════════════════════════════════════
# 『ハビッツ！！！』主題歌MV『誰の名』 chorus-1「名札」 / 所作 / motion —— その字は、誰の字。
#
#   紙の上を滑っていた手が止まり、字の一点を指している。
#   2.473秒——滑りが途中で止まり、指はそのまま動かない。
#   字は読めず、指は一点を押さえるだけである——この1本は、まだ何も明かさない。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 『ハビッツ！！！』主題歌MV『誰の名』 habits-mv-s05「手が滑り、一点を指す」 / 2.473s

⚠️ **この仕様は `WAN 3.0` の経路のものである。** 対の仕様は `../seedance-2.5/habits-mv-s05.md` に在る
——**この作品は、2つの経路を並立させている**（`L39` が対を読む）。**同じショットの2つの言い方であり、別のショットではない。**
⚠️ **ゆえに、片方を直したら、もう片方を読む。** ⚠️ **機械が見るのは、題と §18 の見出しと、§18 `Negative Prompt` の一致までである**——
**本文のずれは、いま誰も見ていない**（`L39` の限界）。

---

⚠️ **この2.473秒は、この曲で最初の「畳みかけ」である。** サビの1行が2.473秒で来る——
`regime: beat` の1本目である（`bible.song.sections` の `chorus-1`）。
⚠️ **`l04`「その字は、誰の字。」——ここで明かさないことが求められる。** サビの問いに、
**画面は手で答える。** 顔は置かない。
⚠️ **この2.473秒は、この作品で2番目に小さい値である**——**最小は `s20` の2.393秒。**
⚠️ **同じ2.473秒が4本ある**（`s05`・`s07`・`s12`・`s13`）——**ゆえに「最も短い」とは書かない。**
**1.2秒のショットは単位にならない**
（`ledger.song_coverage` の註）——**ゆえにここは1行＝1本である。**
⚠️ ⚠️ **`s24`・`s25` を `名札` に数えていた誤りを直した。** サビの現場は14本である（`ledger.yaml` の `名札` の註）。

---

# 1. VIDEO

- Duration: `2.473s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take of one change — **a hand slides across a nameplate and stops on a single point of a character.** ⚠️ **It is the work's first question asked by a hand**, and it is asked in two and a half seconds: **the beat sections of this song do not have time to explain, and they do not explain.**

# 2. WORLD

## World Concept

2026, Japan. Kawaguchi in Saitama, Adachi in Tokyo, Totsuka in Yokohama — and in this shot, a nameplate on a left sleeve, in a school, in the middle of a working day. There is no magic, no institution and no secret organization: there is only a daily life in which the etiquette of the written name is thoroughly in place. **The name is the subject of this work, and the name this work is about is the one that is read the wrong way** — which is why every name on every in-world prop is printed or written and nowhere legible. ⚠️ **This is a theme-song music video:** one song of 179.320 seconds, twenty-seven shots, no episode — **the work does not advance a story. It holds one question and asks it again with other hands.**

## World Rules

- **The people in the work do not know that they are inside a film.**
- **The hand comes first and the face comes after. The order is not swapped. A face is placed only after it has been called.**
- **The name lives on the side of being called, not on the side of being written.** A name is made of the number of times it has been called.
- **The sound is not a calling voice; it is the sound of paper and hands.** A calling voice is heard only on the side of the one called.
- **The carrying in this work never completes.** It is not received, or it is treated as not received, or it is received and not read where it arrives. **Not completing is the only way a movement is kept from becoming an event** — an event is a carrying that completes.
- **No text is burned into this work.** In-world text is a different thing from a subtitle, and this work draws the first and forbids the second.
- **The writing seen in this work is print, ballpoint and pencil — and none of it is legible.**
- **Only so many places can stand at once.** This shot places one.
- **This work speaks Japanese.** It is the language of the room and of the people in it.

## Visual Language

- Art Direction: Luminous realist anime, translated into a left sleeve and the hands at it. **The light, not the figure, is the subject** — and here the light is fluorescent on plastic, which is the one material in this work that gives the tube back.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The palette is school plastic — the plate's cream, its dark border, skin, and the cuff of the sleeve it is fixed to.
- Texture: Layered atmospheric depth from near to far; dust suspended and individually rendered where the tube catches it. **Plastic is smooth and gives a highlight; the sleeve behind it is cloth and does not.** No grain overlay, no painterly stroke.
- Rendering: Clean anime lineart on the figure, drawn at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — **no second tone inside one piece of cloth, no gradient inside a single material, no soft airbrush.** ⚠️ **The written name is drawn as the resolution it is** — cut, printed, ballpoint and pencil are four different marks, not one texture applied four times.
- Visual Density: **Very low, and deliberately so at this speed.** One focal point — the finger and the point it has stopped on — with the sleeve filling the rest of the frame.
- Time: `勤務日の日中` — the middle of a working day, indoors. **Fourteen shots of this work are in this daylight and this room.**
- Atmosphere: A room where somebody is looking at a name on their own sleeve and nobody is watching them do it.

# 3. SUBJECTS

## 佐藤美咲の右手

- Reference: the frozen setting sheet — `distill-essence-engine/examples/habits/character/サブ/01_佐藤美咲/ChatGPT Image 2026年9月18日 05_05_37.png` （人のかたちの一枚, `character-sheet × luminous-anime`）.
- Appearance: **外見の記述は出典に一行も無い**（方針 §5a）。**この一枚が外見である。** この1本が置くのは**右手と、その下の名札**である。⚠️ **顔は置かない。**
- Behavior: **手が滑り、途中で止まる。指が一点を押さえ、そのまま動かない。** ⚠️ **速い** — サビの1行の速さに、画面が一つの所作で応える。
- Continuity Requirements: **Must preserve** — 凍結した一枚。**May change** — 何も変えない。⚠️ **爪と関節は、この作品の他のサビの手と同じ描き方であること**（別の人物だが、同じ様式の同じ手である）。

## nobody

- **この1本に、二番目の人物は居ない。** ⚠️ **名札は人に付いている**（`ledger.yaml` の `名札` の `geography`）——**ゆえに袖は写るが、着けている者は写らない。**

# 4. ENVIRONMENT

- Location: `名札` — **全巻を貫く小道具の現場である** — run-10【ルックとカメラ】の「**左袖の名札**」。⚠️ **この作品は、名札を机の上に置かない**（`名札の予備` の側がそれを負う）。
- Environment Elements: 職員室・教室・昇降口のいずれか。**左袖、その上、机の面の一部。** ⚠️ **部屋を特定しない** — サビの14本は同じ現場だが、**同じ絵ではない**（机の向きと、誰の手かが違う）。⚠️ **`time` は違わない**——**この14本は、すべて日中である。**
- Environmental Behavior: 埃が袖の上を渡る。**袖は動かない。** ⚠️ **指が止まったあとも、埃とプラスチックの上の光は動き続ける。**

# 5. OBJECTS

- **名札** — 学校の指定の名札。**プラスチック。左袖に付く。** ⚠️ **読めない。** 縁が起き、留め具が袖の布を掴んでいる。
- **紙** — 名札の面は、この作品で唯一**曲がらない**面である。
- **袖** — 布。⚠️ **この1本で、布とプラスチックの差が読めること** — 様式の `Rendering` が要求する「素材ごとに一つの影」の、最初の実例である。
- No other object is in frame.

# 6. REFERENCES

- REF_CHARACTER: 佐藤美咲 — `distill-essence-engine/examples/habits/character/サブ/01_佐藤美咲/ChatGPT Image 2026年9月18日 05_05_37.png` (CRITICAL). **この1本は `identity` を添付する** — 手の造形がこの人物のものであるためである。⚠️ **顔は置かない**（世界の規則「顔は、呼ばれた後にだけ置かれる」）。
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_STYLE: `luminous-anime` (HIGH)
- REF_SOURCE: `projects/habits-mv/bible.yaml` and `projects/habits-mv/ledger.yaml` (CRITICAL)
- ⚠️ **REF_BOARD は無い。** この経路は絵コンテを要求しない。**この経路が受け取るのは参照画像である**——
  `key_image` の1枚（`specs/image/habits-mv-s05.md`）。**文から起こし、その見た目へ寄せる**
  （`specmap.MODELS` の `WAN 3.0` の註。実測——**添付画像の服が、テキスト指定に勝つ**）。
  ⚠️ **先頭フレームではない**——最初のコマにすると、**この1本の変化が画面上で起きなくなる**
  （`mode` と `unit` が偽になる。⚠️ この1枚は、この1本が終わったあとの状態を写している）。
- ⚠️ **この経路には、実在の顔を含む参照画像についての公式の警告が無い**——それは `SEEDANCE 2.5` の制限である。
  **この作品の人物は実在しない**——**当たらないことを、ここに書く。**
- ⚠️ **§1–17 は下敷きであり、生成器へ投入するのは §18 だけである。**

# 7. NARRATIVE

- Core Event: **A hand slides across a nameplate and stops on one point of a character.**
- Beginning: The nameplate is on the sleeve, lit, unread, and **the hand is not on it yet.**
- Turn: **The hand arrives and slides** — right, fast, and without hesitation.
- Peak: **It stops.** One finger is pressing a single point of one character, and **that point is not readable either.**
- Pull: ⚠️ **The shot ends on the finger.** **Nothing is said and nothing is decided** — the question has been asked by a hand, and the shot is over.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - MOVEMENT 1 `0-1.1s` — density: `dense` — **the hand slides** across the plate, right. Fast, flat, the pads of the fingers reading the surface rather than pressing it.
  - MOVEMENT 2 `1.1-2.473s` — density: `held` — **it stops.** One finger is on one point of one character. ⚠️ **The plate is not read and the point is not named.**
- Temporal Density: **Two movements, one dense and one held, and the held one is the longer half.** ⚠️ **In a beat section the shot has to arrive fast and then stand still** — **the stopping is what there is time for.**

# 9. ACTION

- `ACT_SLIDE` — Before: the plate is on the sleeve and no hand is on it. After: **a hand has crossed the plate from left to right.** ⚠️ **The hand is reading the surface, not the name.**
- `ACT_POINT` — Before: the hand is moving. After: **one finger is on one point and stays there.** ⚠️ **The point is not identified, and the shot does not say what it is.**

# 10. CAMERA

- Camera Language: Third person, **close**, at the left sleeve — **the second of this work's three camera sites** (run-10: 机上の手、左袖の名札、めくられる名簿). The lens is at sleeve height, close enough that the plate fills the frame and **the person it is fixed to is not in it.**
- Camera Events: **None.** ⚠️ **この1本には、カメラの出来事が無い。** 2.473秒は、置かれた位置から動かない。
- Camera Behavior: No handheld, no whip, no shake, **no follow of the sliding hand**. ⚠️ **The camera does not travel with the finger** — the hand crosses a frame that is standing still, and **that is the whole difference between a beat shot and a chase.**

# 11. MOTION

## Subject Motion

**A right hand crossing a nameplate and stopping.** ⚠️ **It is the only motion the figure has.** The wrist does not lift, the arm is not in frame, and the fingers do not close.

## Object Motion

⚠️ **None.** The plate is fixed to the sleeve and the sleeve does not move. **The plate is the one rigid object in this work** — everything else in it is paper.

## Environmental Motion

Dust moves over the sleeve and catches the tube. **It keeps moving after the finger stops.**

## Physical Characteristics

- **Weight**: **None that the shot shows.** ⚠️ **The hand is not pressing** — the pads are reading the surface, and the plate does not flex under them.
- **Inertia**: **The stop has no overshoot.** The hand is moving and then it is not — **one frame of transition, no settle.**
- **Acceleration**: **One, at the start.** ⚠️ **This is a beat shot: the movement begins at full rate**, because the line it answers has no room to wind up.
- **Fluidity**: Continuous and fast. ⚠️ **Fast is not smeared** — the work's motion is always readable, at every speed.
- **Impact**: **One, and it is soft** — the pads meeting plastic. **Nothing else touches anything.**

# 12. EMOTION

- Emotional Arc: **The instant a question is asked by a hand** — and the shot does not wait for an answer.
- Emotional Events: ⚠️ **The event is the stop**, and **the shot gives it no weight at all**: the line is 2.473 seconds long and the shot ends when the line does.

# 13. LIGHTING

- Base Lighting: Fluorescent over a working desk in the middle of the day, with the style's bloom on the pale surfaces. The tube is above and behind the camera, so the light falls flat and even across the desk and the paper is the brightest thing in the frame. Deep cyan in everything the desk edge shadows.
- Lighting Events: **None.** ⚠️ **A light change inside two and a half seconds would be read as a dramatic beat**, and this shot is a beat without drama.

# 14. AUDIO

- Dialogue: **None.** ⚠️ **This shot is under a sung line** — `l04`「その字は、誰の字。」is in the song, and **nobody in the frame says anything.** **The work still speaks Japanese**; §18 names it.
- Sound Effects: **Cloth and plastic, and nothing else placed.** The small sound of a sleeve when a hand moves across a plate fixed to it; ⚠️ **no sound from the stopping** — **a finger coming to rest on plastic makes no sound, and the absence is placed rather than left out.**
- Music: **None, by specification.** ⚠️ **This is a beat shot: the song is at its densest here**, which is exactly why nothing else may be under it. No bed, no score, no sting.
- Environment: A school room in the middle of a working day. Distant corridor, a door, a chair. **No calling voice as a sound effect.**

# 15. CONTINUITY

- Identity: **Must preserve** — the hand of the frozen sheet, and **the same style of hand as the fourteen other hands of this work.** **May change** — nothing. ⚠️ **The person is not identified by clothing, hairstyle or prop** (§18).
- Spatial: The plate is at the frame's centre throughout; **the hand crosses it and the frame does not move.** ⚠️ **Nothing is moved for the camera.**
- Temporal: The middle of the same working day as the twenty-six other shots. **Nothing in frame supplies a date.**
- Visual: The same fluorescent key and the same palette as all twenty-seven shots. ⚠️ **The plate is the only thing in this work that gives the tube back**, and that is true in all fourteen of the shots at this site.
- Motion: Full animation, not limited. ⚠️ **At this speed the temptation is to shoot on threes** — **the work does not: 24fps, full animation, even in two and a half seconds.**
- Sound: Cloth, plastic, no voice, no music. **No calling voice as a sound effect.**
- ⚠️ **この作品は、2つの経路を並立させている**（`seedance-2.5/` と `wan-3.0/`）。**この仕様は `WAN 3.0` の側である。** 本編の三本（`MINIMAX H3`）とは別である。⚠️ **ずれてはならないのは、人物と、パレットと、光である**——**プロンプトの字面ではない。**

# 16. CONSTRAINTS

## MUST NOT

- No legible text on any surface — not on the register, not on the address slip, not on the claim tag, not on the nameplate, not on the bundle. ⚠️ **These characters are on screen and none of them can be read.**
- No romaji in place of the Japanese name; no real-world alphabet in frame.
- **No blank surface where the writing should be, and no nonsense glyphs** — a surface with nothing on it and a surface with invented marks both fail, in opposite directions.
- No face before the name is called.
- No calling voice as a sound effect; no spoken line; no voice-over; no narration. ⚠️ **This shot has no dialogue** — see §14.
- No music of any kind in this shot. ⚠️ **この経路が否定を床として受け取るかは、まだ測っていない**——`specmap.MODEL_UNRECEIVED_SLOTS` の `WAN 3.0` は空である（⚠️ **空は「受け取る」の意味ではない。測っていないという意味である**） — a bed arriving is a violation of this section, not a matter of taste.
- No on-screen subtitles, no captions, no burned-in subtitles in any language. ⚠️ **この経路が字幕をどう扱うかは、まだ測っていない**——**ゆえにこの節は、この経路では床ではなく、仕様の要求である。**（⚠️ 対の `SEEDANCE 2.5` には字幕の公式の記法が在り、**あちらではこの一句が、より必要である。**）
- No watermark.
- No wall clock, no calendar, no digital timer, no date stamp.
- No uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion.
- No character added beyond the shot; no person the shot does not hold.
- No identifying clothing, hairstyle, or prop — **the people of this work are not told apart by what they wear.**
- No smile, no tears, no fear, no exaggerated expression.
- Not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces.
- **The nameplate is not readable.** ⚠️ **This is the shot where that is hardest** — the plate is the subject and fills the frame, and it still cannot be read.
- **The face does not enter the frame.** No chin, no hair, no shoulder above the sleeve.
- **The hand does not lift the plate, turn it, or look under it.** ⚠️ **That gesture belongs to `s06`** — this shot slides and stops, and does nothing else.
- **The hand does not close into a fist, and the fingers do not tap.**

## MUST

- **A hand crosses the plate and stops on one point of one character.**
- **It is the only motion in the frame, and the frame itself does not move.**
- **The plate, the point and the character are all unreadable.**

## PREFER

- Sleeve height for the lens, with the plate filling the middle of the frame and **the cuff at the frame's edge**, so that the plate reads as worn rather than as lying on a surface.

## ALLOW

- Dust over the sleeve; the tube's highlight on the plastic; the cloth's weave behind the plate.

# 17. GENERATION PRIORITIES

1. **Fast, and then absolutely still** — the beat's speed is the first half and the stop is the second.
2. **The plate is worn on a sleeve** — ⚠️ **not lying on a desk.** The work has one site for the nameplate off a person, and it is `名札の予備`.
3. **Nothing is read** — the plate, the point and the character stay unreadable.
4. **The camera does not move** — a beat shot with a travelling camera stops being a beat.
5. **Japanese is what this work speaks** — named in §18, even though this shot holds no words.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

⚠️ **この経路の `Master Prompt` は、時区分を角括弧で本文の中に置く**（`[0-3s]`）——
**他の二つの経路と書き方が違う。** **ゆえに `Master Prompt` が、それ自体で一本の時間割を持つ。**
⚠️ **この経路が `Negative Prompt` をどう扱うかは、まだ測っていない**
（`specmap.MODEL_UNRECEIVED_SLOTS` の `WAN 3.0` は空である——⚠️ **空は「受け取らない」の意味でも、
「受け取る」の意味でもない。測っていないという意味である**）。
⚠️ **ゆえに禁制は二箇所に置く**——**ここの `Negative Prompt`**（**この作品が何を禁じるかの記録**）と、
**`Master Prompt` の散文**（**この経路が実際に読む側**）。**同じことを二度書いているのではない。**
⚠️ **`L30` はこの仕様を読まない**——あれが読むのは `spec:` が指す1本であり、**それは対の側である。**
**ゆえにここへ否定をどれだけ書いても、鳴るものが無い。** ⚠️ **鳴らないことは、届いたことの証拠ではない。**
（⚠️ 対の側は逆である——あちらは `SEEDANCE 2.5: Negative Prompt` を承知で使い、`L30` は名指された註になる。）
⚠️ **この節の `Negative Prompt` は、この作品の27本で同一であり、対の仕様とも同一である。**
理由は `L10` にある——`disclosure` の3つの変化点が `negative: covered`
（**§18 は変わらない**）を宣言しており、**「覆った」は「同じである」を要求する。**
ゆえに**ショット固有の禁制はこの節に書かない**——それは `shot.forbidden_set`（引き渡しの層）が持つ。

## Master Prompt

A 2.473-second continuous cinematic take (16:9), luminous realist anime, on a school nameplate fixed to a left sleeve, in the middle of a working day, 2026. One change only: **a hand slides across the plate and stops on a single point of a character** — ⚠️ **the plate is worn on the sleeve, not lying on a desk, and the person wearing it is not in the frame.** Beats, deliberately uneven: [0-1.1s] **the hand slides** across the plate, right, fast and flat — the pads of the fingers reading the surface rather than pressing it — over a plate that is **plastic, on a left sleeve, with a dark border and characters on its face that cannot be made out**; [1.1-2.473s] **it stops.** One finger is on one point of one character, and **it stays there** — no lift, no turn, no second movement — and the point it has stopped on **is not named and cannot be read.** **The hand only slides and stops: it does not lift the plate, turn it, or look under it, and it does not close into a fist.** **The nameplate is fixed to a left sleeve and the person wearing it is not in the frame: no face, no chin, no shoulder above the cuff.** **The characters on the plate are present and cannot be made out: they are Japanese characters, set in the Japanese script, and they are not legible.** **This is a Japanese work.** No subtitles. No BGM. Ends with the finger still on the character and the dust still crossing the sleeve — **the atmosphere is the last mover and it is the shot's ending** — and cuts.

## Visual Prompt

Luminous realist anime, translated into a left sleeve and the hand at it: the light, not the figure, is the subject, and here the light is fluorescent on plastic — **the one material in this work that gives the tube back.** The plate: the school's designated nameplate, plastic, fixed to a cloth sleeve, a dark border, rounded corners, characters on its face — **present and not readable.** Around it, the weave of the sleeve and the cuff at the frame's edge; **the person wearing it is not in the frame.** One hand — the back of it, the knuckles, the nails — sliding and stopping. Clean anime lineart at one thin even weight with no thickening at the contour; cel shading held to a single shadow tone per material with the boundary left crisp — **plastic gets a highlight, cloth does not, and the difference is visible.** Saturated where the light falls, deep cyan in the unlit half; the plate's cream, its dark border, skin, and the sleeve. Bloom on the plastic, dust suspended and individually rendered, very low visual density.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. **A hand sliding right across a plate, fast and flat, and then stopping on one point: no overshoot, no settle, one frame of transition.** Nothing else moves — the sleeve does not move, the plate does not flex, the fingers do not close, and there is no arm in frame. ⚠️ **At this speed the temptation is to shoot on threes; the work does not.** Dust moves over the sleeve and catches the light, and **it keeps moving after the finger has stopped.** **No acceleration after the start, no impact beyond one soft contact with plastic, no motion blur smears, no stutter, no held frames.**

## Camera Prompt

Third person, close, at the left sleeve — sleeve height, near enough that the plate fills the middle of the frame and **the person it is fixed to is not in it.** ⚠️ **The camera does not move at all in this shot: no event, no settle, no drift.** ⚠️ **Do not follow the sliding hand** — the hand crosses a frame that is standing still. No handheld, no whip, no shake, no push-in, no sudden zoom, no unnatural rotation, no cut. **Keep the composition for the whole take.**

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of everything this work holds. **No line is spoken in this shot: nobody in the frame says anything, and there is no voice-over and no narration.** **The Japanese is not spoken here; it is what this work is** — and **nothing is written on screen**: no subtitles, no captions, in any language. Sound effects, nothing mixed forward: the small sound of a cloth sleeve when a hand moves across a plate fixed to it, a distant corridor, a chair. ⚠️ **And one absence, placed rather than left out: the stopping makes no sound** — a finger coming to rest on plastic is silent, and the silence is placed rather than left out. **Music: none — this shot carries no music of any kind.** ⚠️ **This is a beat shot: the song is at its densest here, which is why nothing else may be under it.** No bed, no score, no sting, no drum. No calling voice as a sound effect.

## Negative Prompt

no watermark, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no background music, no music bed, no score, no musical sting, no swelling music, no drum, no calling voice as a sound effect, no spoken name, no voice-over, no narration, no crowd, no face before the name is called, no legible name text, no legible text on any surface, no readable characters on any prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no blank surface where the writing should be, no signature, no handwriting by the subject, no identifying clothing, hairstyle, or prop, no character added beyond the shot, no additional person beyond the shot, no wall clock, no calendar, no digital timer, no date stamp, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no smile, no tears, no fear, no exaggerated expression, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no gradient shading, no second shadow tone within a single material, no soft airbrush, no rendered fabric fold, no thick contour line, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-mv-s05-2.473s-01`
- Segment ID: `chorus-1-1`
- Specification Version: `0.1.0`
- Generation Date: `—`
- ⛔ **この経路では、まだ1本も生成していない。** 日付が空なのは、そのためである——
  **この節は「これから何を投入するか」であって、記録ではない。**
- ⚠️ **対の仕様も、ここは `0.1.0` / `—` である**——**あちらも、この1本はまだ送られていない。**
  ⛔ **ゆえに、この側へ写す記録は無い。**

## Resolved Values

- Duration: `2.473s`
- References: `REF_CHARACTER (佐藤美咲 — 人のかたちの一枚, CRITICAL) ／ REF_FORMAT (video-spec) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml ＋ ledger.yaml, CRITICAL)`
- Temporal Structure: `2 movements, NON_UNIFORM — 0-1.1s / 1.1-2.473s`. The held movement = `MOVEMENT 2`
- Camera Events: `none — **この1本にカメラの出来事は無い**`
- Action Events: `ACT_SLIDE → ACT_POINT`
- Audio Events: `no dialogue ／ cloth ＋ plastic ＋ one placed absence ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — **最初の稿である。この経路では、まだ一度も生成していない。**
⚠️ **根は対の仕様である**（`../seedance-2.5/habits-mv-s05.md`）——**あちらも `0.1.0` で、この1本はまだ送られていない。**
**この側は、その根から起こした別の言い方である。**
⛔ **この節は仕様の側であって、世代の記録ではない**——**記録は `takes/` に在る。**

## Observed Problems

⛔ **この経路では、まだ1本も生成していない。以下は、すべて対の仕様の観測である**
（`SEEDANCE 2.5`、2026-09-28）——**この経路で同じ問いを見るために、消さずに残す。**
⚠️ **経路を名指していた行は、この側の言い方へ直してある。**

- _(this shot has not been generated, so there are no observations of it.)_ ⚠️ **But this is not `_(none yet)_` either: the shot has not been sent, and the reason is not the shot.**
- ⚠️ **`L30` が対の仕様の上で鳴る**（`SEEDANCE 2.5`）— §18 `Negative Prompt` に中身が在り、
  **あちらの経路はその欄を床として受け取らない。** **§1–17 を直しても消えない。** この作品は**承知で使うと宣言している**
  （`bible.route_limits_accepted` の `SEEDANCE 2.5: Negative Prompt`）——**ゆえに `L30` は違反ではなく、名指された註になる。**
  ⚠️ **除外は作品の宣言であって、基盤の判断ではない。** **そして、宣言が言えるのはそこまでである**
  ——**その否定が実際に効いたかは、生成の外では見えない。**
  ⚠️ **この経路（`WAN 3.0`）では、`L30` は鳴らない。**
  ⛔ **鳴らないことは、届いたことの証拠ではない**（§18 の前書き）。
- ⚠️ **この経路では、まだ1本も生成器へ送られていない。** ⛔ **対の側では3本（`s01`〜`s03`）が 2026-09-28 に送られ、
  `takes/` にテイクが在る**——**機体へ届いたバイトは、あちらである。** **`L6` が27本ぶん鳴りつづけるのは、それが理由である。**
  **欠陥ではない。** **送った日に、`attached` を書く。**

## Anticipated risks (to check in the first generation)

- **The name may be rendered legible.** ⚠️ **The first risk of this shot and the worst one**: the plate fills the frame, and **a readable name at this site answers the song's question in the wrong direction.**
- **The plate may be drawn lying on a desk.** ⚠️ **The work has exactly one site for a nameplate that is not on a person, and it is `名札の予備`** — a plate on a desk here spends that shot.
- **The face may be placed above the sleeve.** Sleeve height is close to a chin, and a generator will supply one.
- **The hand may lift the plate.** The gesture belongs to `s06`; doing it here leaves that shot with nothing.
- **The camera may follow the hand** — which turns a beat shot into a chase and breaks the section's regime.
- **The shot may be shot on threes** to save the two and a half seconds — **the work's motion standard forbids it.**
