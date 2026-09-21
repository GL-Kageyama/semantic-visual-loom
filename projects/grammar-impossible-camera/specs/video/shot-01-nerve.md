# Wan 3.0 Full Specification — 瞳の内側 Clip 1/1 / 12s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**

⚠️ **この仕様は形式カード `impossible-camera` を1度だけ使う。**
カードの4つの欄が、この仕様の背骨である。

| カードの欄 | この1本の値 |
|---|---|
| `EYE` | **在りえない視点。** 洗いの前端が、その位置である |
| `ENTRY` | **瞳。** どうやって中へ入ったかを、この1本が自分で言う |
| `PATH` | **視神経。** さかのぼる——尺度も物理も、その世界のものである |
| `ARRIVAL` | **3歳の夏の光。** 視点はそこで終わる |

⚠️ **このカードは `video-spec` に文法を1つ足したものである。**
この仕様が足したのは **「視点の存在が、そのまま時間である」という1点**だけである——
⚠️ **これはカメラの移動ではない。** カメラの移動は、カメラをどこかに置いたままにする。
ここでは **「カメラがどこかに在る」という前提そのものが捨てられている。**
⚠️ **`meaning-responsive` と混同しないこと。** あちらは視点が意味に応える。
こちらは視点が、**カメラの行けないところへ行く。**

⚠️ **⚠️ この作品は、2枚のカードが噛み合う唯一の場所である。**
様式 `watercolor` の `Motion character` は「**カメラは窓ではなく紙である**」と言い、
**動くのは水であって筆ではない**と言う。このカードは「**これはカメラの移動ではない**」と言う。
**この2つは同じことを言っている。** ゆえに **§10 の画は動かず、進むのは洗いである**——
**その前端が視点の位置であり、控えられた白が、まだ入っていない場所である。**

⚠️ **この作品は物語ではない。** 1ショットだけの最小の作品であり、
**7枚の文法カードの1枚が、仕様として立つかを試すために在る。**

---

# 1. VIDEO

- Duration: `12s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. **The viewpoint exists where no camera can be, and the journey is the time** — the frame does not travel; the wash does.

# 2. WORLD

## World Concept

The inside of an eye, and the road back along the optic nerve to the light of a summer when the witness was three. **The camera is not at a place** — the premise is dropped, and what the shot composes is the existence of a viewpoint.

## World Rules

- **The entry is stated.** The shot says how it got inside — **through the pupil.** ⚠️ **An unstated entry reads as a continuity error in a previous shot rather than as this grammar.**
- **The path has its own law.** Inside, the world belongs to that viewpoint, and its scale and its physics are its own.
- **The path's physics does not change halfway.** The same law holds from the first frame to the last.
- **The shot arrives.** The viewpoint ends where the shot's meaning is — **at the light of that summer.** ⚠️ **Leaving the viewer inside with no arrival spends the journey and keeps nothing.**
- **This is not a camera move.** A camera move keeps the camera somewhere; here nothing at a place is composed.
- **The reserved white is the road.** What is not yet painted is where the viewpoint has not been — **so the white running out *is* the arrival.**
- **No conventional camera position, and no fisheye distortion standing in for an impossible viewpoint.**
- **No face** in the frame — the pupil is the way in, not the subject.
- **No legible text** appears anywhere.

## Visual Language

- Art Direction: A watercolor painting. Soft wet-on-wet washes, translucent layered pigment, **reserved white paper**, dry-brush edges and delicate colour bleed, paper grain, gentle diffused light. **Contours are pale colour edges, never hard ink lines.**
- Color Language: Pale and translucent, deepened only through layering. **The white of the paper is reserved boldly and the subject floats on negative space.** ⚠️ **The palette stays pale for the whole shot** — a colour that saturates suddenly is a different style.
- Texture: Paper grain, bleeding edges, dry-brush drag, the softness of natural light.
- Rendering: True watercolor. Not photorealistic, not oil, not digital, no hard outline.
- Visual Density: Very low. **A wash, and the white it has not reached.**
- Time: 3歳の夏
- Atmosphere: Quiet and unhurried. **The shot is not dramatic; it is simply going somewhere it should not be able to go.**

# 3. SUBJECTS

## The Viewpoint

- Reference: (none — the viewpoint is not a registered entity; it is the subject of the shot)
- Appearance: **It has none.** It is not drawn and is never shown — **it is legible only as the wet edge of the advancing wash.** Whatever the wash has reached is what the viewpoint is inside of.
- Behavior: **It advances and it does not return.** It enters at the pupil, travels back along the nerve, and **ends at the light.** ⚠️ **It never doubles back, and it never stops partway.**
- Continuity Requirements: Must Preserve: **the law of its own scale and physics** — the same law throughout. May Change: the world it is inside of, entirely.

## The Pupil

- Reference: (none — the pupil is not a registered entity)
- Appearance: A round edge of pale colour, at the near side of the frame, in the first beat only.
- Behavior: **It is there to be entered, and nothing else.** ⚠️ **It is not the subject, and no face is drawn around it.** After the wash has passed it, it is behind the viewpoint and does not return.
- Continuity Requirements: Must Preserve: its legibility as a round opening. May Change: nothing.

# 4. ENVIRONMENT

- Location: `瞳の内側`
- Environment Elements: **Reserved white paper**, and the wash spreading into it. There is no scenery in the ordinary sense — what the frame contains is pigment and the white it has not reached.
- Environmental Behavior: **The wash advances and the white recedes.** The bleeding settles as it goes, the layered pigment deepens where the washes overlap, and dry-brush drag marks the edges. **Nothing in the environment is scenery that could be recognised as a place** — until the arrival, where the accumulated light becomes one.

# 5. OBJECTS

- **The pupil, the white, and the wash. There is nothing else in the frame.**
- ⚠️ **No anatomy, no diagram, no second eye, no blood, no instrument.** The path is not illustrated; it is the pigment's own progress.

# 6. REFERENCES

- REF_LOCATION: `瞳の内側.base` — **未作成。** この作品の画像の経路はまだ1度も走っていない
  （`ledger.yaml` を見よ）(MEDIUM)
  ⚠️ **在ることと、渡したことは違う。** **この1本は、いま何も添付していない**
  （ショット記録の `attached: []` を見よ）。
- REF_STYLE: `watercolor` (HIGH)
- REF_FORMAT: `impossible-camera` — this defines the one grammar this shot is
- REF_SOURCE: `projects/grammar-impossible-camera/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: A viewpoint enters an eye and arrives at the light of a three-year-old summer.
- Beginning: White paper, and one round edge of colour at the near side. **The way in has not been taken.**
- Turn: **The wash crosses the edge and the path begins.** The white ahead is where the viewpoint has not been.
- Peak: The white thins, the light begins to gather from the far side, **and nothing has named itself yet.**
- Pull: The frame fills with light, **and the arrival is named only by how it looks** — a summer, seen by someone who was three.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-3s` — density: `sparse` — The entry, stated: one round edge of pale colour at the near side of the white paper.
  - BEAT 2 `3-7s` — density: `dense` — **The wash crosses the edge.** Pigment blooms outward and the wet edge becomes the viewpoint's position. **The white ahead is where it has not been.**
  - BEAT 3 `7-10s` — density: `transition` — The white thins. **The law does not change** — same scale, same bleeding. Light begins to gather from the far side and **names nothing yet.**
  - BEAT 4 `10-12s` — density: `held` — **The arrival.** The frame fills with light and the viewpoint ends there. **The audience now knows where it arrived.**
- Temporal Density: ⚠️ **The seconds are not spread evenly** — the journey takes the middle, and the arrival is given room to be still.

# 9. ACTION

- `ACT_ENTER` — Before: the edge is uncrossed and the white is whole. After: **the wash has crossed, and the way in has been stated by the crossing itself.**
- `ACT_TRAVEL` — Before: the wash is at the near side. After: **it is deep into the white, and the white ahead is smaller.**
- `ACT_ARRIVE` — Before: the light is gathering but unnamed. After: **the frame is the light, and the viewpoint has ended.**
- Causes: **the viewpoint's own existence.** ⚠️ **Nothing in the frame causes the advance** — no agent acts, nothing enters, and **there is no process beat.** The journey is not explained; it is simply undertaken.

# 10. CAMERA

- Camera Language: **A page.** The frame is a sheet of paper and it does not travel — **the viewpoint's advance is the wash's advance, and the camera is not a thing placed at a point at all.**
- Camera Events: `0-12s` none. **There is no camera move, no pan, no zoom, no rack, and no travelling shot** — ⚠️ **not because a camera is being held still, but because the premise "the camera is somewhere" has been dropped.**
- Camera Behavior: **The page holds.** ⚠️ **A travelling camera would spend the reserved white, and the reserved white is this shot's road** — so the frame staying put is not a limitation here, it is what makes the journey legible. One continuous take; no cut.

# 11. MOTION

## Subject Motion

**The viewpoint advances, and its position is the wet edge.** The wash crosses the pupil's edge, blooms outward into the white, and keeps going — **and because the white ahead is what has not been entered, the shrinking white is the journey's own measure.** It never doubles back and never arrives twice.

## Object Motion

**The pupil does not move.** It sits at the near side until the wash passes it, and then it is behind the viewpoint for the rest of the shot.

## Environmental Motion

**The water is the mover, not the brush.** What changes between frames is a wash spreading into wet paper — pigment blooming outward and settling — **never a contour redrawn by a hand.** ⚠️ **The wet edge never holds still**: the same silhouette is a little different a moment later, **and it does not return to where it was.** ⚠️ **The paper's white stays reserved for the whole shot** — nothing drifts in to fill it, because **the white is the road, not the background.**

## Physical Characteristics

- Weight: None in the ordinary sense. **What has weight here is the pigment's concentration**, and it deepens where washes overlap.
- Inertia: **The advance has it** — once the wet edge is moving it does not stop, and the same law carries it to the end.
- Acceleration: None. **The journey does not hurry and does not slow; the density changes, not the speed.**
- Fluidity: This is the whole of it. **The medium is water and the motion is bleeding.**
- Impact: None.

# 12. EMOTION

- Emotional Arc: The quiet of going somewhere that cannot be gone to, without anyone being told it cannot be done.
- Emotional Events: The last two seconds, when the light has filled the frame and **the audience learns where the journey was always headed.**

# 13. LIGHTING

- Base Lighting: Gentle diffused light, **carried by the reserved white rather than laid on top of it.** The paper's own brightness is the light source the frame reads as.
- Lighting Events: `7-12s` — **light gathers from the far side of the white and grows until it is the frame.** ⚠️ **This is the only light change**, and it is the arrival rather than a lighting beat.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: Almost none — **a single soft, wet sound**, at the moment the wash crosses the edge.
- Music: None.
- Environment: Near silence, with no room around it.

# 15. CONTINUITY

- Identity: **The viewpoint is one viewpoint for the whole shot**, and the pupil keeps its identity as the way in.
- Spatial: **The frame does not move at all.** ⚠️ **What moves is the wash's boundary within it** — the composition's near side and far side do not change places.
- Temporal: **One continuous advance, in one direction.** Nothing is skipped, nothing is repeated, and the law of the path is the same at the end as at the start.
- Visual: **The white stays reserved and the palette stays pale** for the whole shot. The contours stay pale colour edges and never become hard lines.
- Motion: **Continuous. There is no held frame anywhere in it.**
- Sound: Near silence, unbroken.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止）

- No conventional camera position, and **no fisheye distortion standing in for an impossible viewpoint.**
- No unstated entry — **the way in is shown, not implied.**
- No path that changes its own physics.
- No shot without an arrival.
- No cut.
- No face in the path, no second eye, no blood, no medical illustration.
- No hard outline, no oil, no digital rendering, **not photorealistic.**
- No colour that saturates suddenly — **the palette stays pale and translucent.**
- No readable text of any kind.
- No lens flare.

## MUST

- **The entry is stated in the first beat.**
- **The white recedes and finally runs out** — the arrival is the white being spent.
- The path's law — scale and physics — is the same from the first frame to the last.
- The frame does not travel: **the wash moves and the page does not.**
- The arrival is the light of a summer, and **it is named by nothing in the frame.**
- The reserved white survives until the arrival.

## PREFER

- The pupil small and off-centre at the near side, with the larger part of the frame given to unwashed white.

## ALLOW

- Dry-brush drag marking the wet edge as the wash advances.

# 17. GENERATION PRIORITIES

1. **The entry is stated.** ⚠️ **Without it this reads as a continuity error rather than as this grammar.** It outranks beauty.
2. **The path keeps one law** — the same scale and physics from the first frame to the last.
3. **The shot arrives.** The white running out is the arrival, and the arrival carries the shot's meaning.
4. **The frame does not travel** — the wash moves and the page holds.
5. **This is not a camera move** — nothing is composed at a place.
6. **The white stays reserved until the end** — nothing drifts in to fill it.
7. **No fisheye standing in for an impossible viewpoint.**
8. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 12-second continuous watercolor take (16:9), one clip, of a viewpoint travelling where no camera can be — **this is not a camera move: the frame is a page and it does not travel.** Beats, deliberately uneven: [0-3s] the entry is shown — one round edge of pale colour at the near side of reserved white paper, and the way in is stated by the wash crossing it; [3-7s] **the journey** — the wash blooms outward into the white and the wet edge becomes the viewpoint's position, and the white ahead is where it has not been; [7-10s] the white thins and light gathers from the far side, and **the law does not change** — same scale, same bleeding, all the way through; [10-12s] **the arrival** — the frame fills with light and the viewpoint ends there. **The reserved white is the road, so the white running out is the arrival.** (No conventional camera position, no fisheye distortion standing in for an impossible viewpoint, no unstated entry, no path that changes its own physics, no shot without an arrival, no cut.)

## Visual Prompt

A watercolor painting of an advancing wash on reserved white paper. Soft wet-on-wet bleeding, translucent layered pigment, paper grain, dry-brush edges and delicate colour bleed, gentle diffused light. **The white of the paper is reserved boldly and the subject floats on negative space**; contours are pale colour edges and never hard ink lines. The palette is pale and translucent, deepened only through layering, and it stays pale for the whole shot. Very low visual density: a wash, and the white it has not reached. Not photorealistic, no oil, no digital, no hard outline, no saturated colour, no readable text, no lens flare.

## Motion Prompt

**The water is the mover, not the brush.** What changes between frames is a wash spreading into wet paper — pigment blooming outward and settling — **never a contour redrawn by a hand.** The wet edge keeps advancing: the same silhouette is a little different a moment later, **and it does not return to where it was.** **The viewpoint's position is the wet edge**, and the reserved white ahead is where it has not been — so **the journey is legible as the white receding, and the white running out is the arrival.** The path keeps one law: the same scale and the same bleeding from the first frame to the last. **The paper's white stays reserved for the whole shot** — nothing drifts in to fill it, no ambient particles, no haze, no colour arriving. **The frame does not travel.** No path that changes its own physics, no fisheye distortion, no motion blur, no full animation, no contours that hold their shape.

## Camera Prompt

A single sheet of paper, held still. **There is no camera move here — not a held camera, but no camera placed at a point at all**, because the premise that the camera is somewhere has been dropped. No pan, no zoom, no rack, no travelling shot, **no conventional camera position, and no fisheye distortion standing in for an impossible viewpoint.** The page holds for the whole shot and the white is never crossed as a device. One continuous take; no cut.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of this work and of every word it holds; **if any speech is placed in it, that speech is Japanese.** **No speech is placed in this shot.** No dialogue, no voice-over, no narration, no caption. Sound effects: almost none — one soft, wet sound as the wash crosses the edge. Ambient: near silence, with no room around it. **Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell.**

## Negative Prompt

not photorealistic, no oil, no digital, no hard outline, no conventional camera position, no unstated entry, no cut, no fisheye distortion standing in for an impossible viewpoint, no path that changes its own physics, no shot without an arrival, no face in the path, no second eye, no blood, no medical illustration, no readable text, no lens flare, no watermark, no on-screen subtitles, no background music

## Style Motion

**The water is the mover, not the brush** — a wash spreading into wet paper, pigment blooming outward and settling, **and this shot's whole journey is carried by exactly that motion.** **Edges keep advancing** — a wet edge never holds still, and **here the advancing edge *is* the viewpoint**, so the style's ordinary behaviour and the card's journey are the same event. **The camera is a page, not a window** — the frame holds still, **and the reserved white is what the shot is about.** ⚠️ **A travelling camera would spend that white, which is why this shot does not travel: here the white is the road, and it must survive until the arrival.** **Stillness is the ground** — nothing drifts in to fill the white: no ambient particles, no haze, no colour arriving. ⚠️ **What this style does not do**: full animation, crisp articulated limbs, contours that hold their shape, motion blur, or a camera that moves for its own sake. ⚠️ **The palette stays pale and translucent for the whole shot** — a colour that saturates or deepens suddenly is a different style, not a beat of this one. (Source: the `Motion character` of the style card `watercolor`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `grammar-impossible-camera-s01-12s-01`
- Segment ID: `01-1`
- Specification Version: `0.2.0`
  ⚠️ **この行は、この仕様の*現在*の版である**——`L25` がここを読み、各テイクの
  `source_version`（**投入した時点の版**）と突き合わせて、**ずれを註に書く。**
  ⚠️ **註を同じ行に足してはならない。** **足すと、この行は読まれなくなる**
  （`specmap.SPEC_VERSION_LINE` は行末までを版とする）。
  **検査が黙ったことは、検査が通ったことではない。**
  ⚠️ **`0.1.0` から変わったのは §19 と §20 だけである**——**§1–18 は同一**である。
  ゆえに **`0.1.0` を投入したテイクに `L25` がずれを註に書いても、投入文字列は変わっていない。**
- Generation Date: `2026-09-22`（⚠️ **根拠は戻ってきたファイルの時刻**——`media/b7588c5e-6348-4bba-bd51-1d85106dab73.mp4` の `03:14`。
  **著者が名乗った日付ではない。**）
- Adopted Take: `—`（**まだ採用されていない。**⚠️ **テイクは1本、`media/` に在る**——
  **テイクの記録はまだ無い。** 記録を書くのは著者である（`projects/hitosara/media/README.md`）。
  ⚠️ **ファイル名は `NN__` の接頭辞を持たない**——**名前から記録を引けない。**
  ⚠️ **採用は選別であり、著者が編集である**（`CLAUDE.md`）。）

## Resolved Values

- Duration: `12s`
- References: `REF_LOCATION (瞳の内側.base, 未作成) ／ REF_STYLE (watercolor, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
  ⚠️ **この行は「仕様が名指した参照」であって、「実際に渡した参照」ではない。**
  **この1本は、いま何も渡していない**（`attached: []`）。
- Temporal Structure: `4 beats, NON_UNIFORM — 3s / 4s / 3s / 2s. The journey = BEAT 2 at 4s (33%)`
- Camera Events: `none — the frame is a page and it does not travel`
- Action Events: `ACT_ENTER → ACT_TRAVEL → ACT_ARRIVE`
- Audio Events: `no dialogue ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.2.0` — **①（生成する）は済んだ**（著者の手）。⚠️ **②（測る）は開いていない**——
**測定はテイクの記録を要する**（`L25` はテイクが1本も無ければ走らない）。**テイクの記録はまだ無い。**
③（型の同定）と ④（直す）も開いていない。

⚠️ **この仕様で確かめたのは、文法が仕様として書けるかどうかである。**
**文法が効いたかどうかではない**——⚠️ **生成はこの基盤の外で起きる。**
⚠️ **生成は1度走った。** だが **`## Examples` はまだ `- —` である**——
**文法が効いたという記録は、まだどこにも無い。**

⚠️ **この作品は、形式カード `impossible-camera` が初めて使われた記録である。**

## Observed Problems

（**機械の測定は、まだ無い。** 戻ってきたファイルの測定は**テイクの記録**
（`verdict.machine.measured`）に書く——`L25` がそれを §1 と突き合わせる。
⚠️ **この行は「問題が無い」ことを言っていない。** **測っていないのである。**）

## Anticipated risks (to check in the first generation)

1. **The entry may not be stated.** A generator given "inside an eye" may simply open inside, with no crossing — **and then the shot reads as a continuity error rather than as this grammar.**
2. **The shot may become a camera move.** The likeliest failure: a push-in or a travelling shot, which is what every generator does with a journey. ⚠️ **Check whether the page travelled** — if it did, the reserved white was spent and §10 was not obeyed.
3. **It may never arrive.** The white may simply continue, or the shot may end inside with no light. **§8 puts the arrival in the last two seconds.**
4. **The white may be filled.** Particles, haze, or a background drifting in would spend the paper — **and the paper is the road here.**
5. **Fisheye may stand in for the impossible viewpoint.** That is the cheap way to say "this is not a normal camera", and the card forbids it by name.
6. **A face may appear around the pupil.** The card's own rule is that the pupil is the way in and not the subject — **and §4 of this shot fixes the near side as a round edge of colour, nothing more.**
