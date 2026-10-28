# ═══ 演出要約 ════════════════════════════════════
# 『灯を返す』「峠の道」 / 離脱 / motion —— 下りていく彼女と、光る提灯
#
#   彼女は背を向け、道を下りていく。提灯は枠の手前に残る。
#   太陽が地平線に触れ、光が水平になる——**提灯の紙が、内側から白くなる。**
#   ⚠️ **5秒で切る。** 切れ目の向こうに、**彼女はもう居ない**——同じ枠のまま、道だけが残る。
#   **火は入っていない。** 光が消えると、提灯はただの紙の塊に戻る。道だけが残る。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 灯を返す Clip 5/5 / 9s

⚠️ **生成器へ投入するのは §18 と `## DIRECTION` だけである。** §1–17 は下敷きであり、
§19–20 は我々の記録である——**どちらも投入しない。**

⚠️ **この1本の変化は「余韻」であり、値は `闇 → 光` である。**
**火は入っていない。それでも提灯は光る**——太陽の残光を受けて。
**無いことが、在ることになる。** これがこの作品の主張である。

⚠️ **`s02` の `闇 → 光` と語が同じである。** 意図した韻である——
**同じ転換が、二度目は違う意味で起きる**（世界の光 → 彼女の置いたものの光）。

⚠️ **この1本は接地ショットである。** デバイスは使わない。**最後の一枚は、一番静かに撮る。**

---

# 1. VIDEO

- Duration: `9s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: **One hard cut inside the clip, at 5s.** **She leaves and the
  light arrives.** The camera stays with what she set down, and the sun does the
  rest — and the cut takes her away before we can watch her go.

# 2. WORLD

## World Concept

The same road, at the bend, at the gap — now seen from behind her, looking down the
road. **The last of the sun comes horizontally along the pass and touches only what
is standing still.**

## World Rules

- **The last light is low.** For a few seconds at the horizon, light travels almost horizontally and lights **only what is not moving.**
- **The lantern does not burn.** Its paper goes white because light passes through it. **No flame, no glow source, no ember.**
- **She does not look back.** She walks down and away.
- **Nothing else is in the frame.** No figure appears; no car passes.
- **Nothing is explained.** No caption, no voice, no sign.
- **No legible text** appears anywhere.

## Visual Language

- Art Direction: Luminous realist anime — a very low sun, a nearly horizontal beam, anamorphic flare raking across the frame, magenta and gold at the horizon against deep cyan below.
- Color Language: **The warm half of the palette returns for a few seconds** and then leaves with the sun. **The paper is the last thing to hold it.**
- Texture: Paper's translucency; the wet road's long reflection; the dust in a horizontal beam.
- Rendering: Clean anime lineart; the figure small and dark against a bright horizontal band. Not photorealistic, not a 3D render.
- Visual Density: **Low.** The frame empties as she goes.
- Time: 夕暮れ
- Atmosphere: The last minute of light, and nothing wasted in it.

# 3. SUBJECTS

## The Girl

- Reference: (none — not identity-locked; **her face is never shown, only her back**)
- Appearance: Seen from behind, walking away down the road. White shirt, dark trousers, **both hands empty.**
- Behavior: She walks down the road, away from the camera, and does not stop or turn.
- Continuity Requirements: Must Preserve: white shirt, dark trousers, **empty hands**, her back to the camera. May Change: her distance down the road.

## The Lantern

- Appearance: Paper, small, on the top edge of the guardrail, **unlit.** Its wire handle lies over.
- Behavior: **It does not move.** It is lit from outside, by the sun, for a few seconds.

# 4. ENVIRONMENT

- Location: `峠の道` — the bend, looking down the road
- Environment Elements: The road descending, the guardrail's top edge in the foreground, the cut wall, the horizon.
- Environmental Behavior: **The sun drops to the horizon and the beam flattens.** Dust in the beam stops falling and drifts sideways. **Then the light goes.**

# 5. OBJECTS

- The lantern on the rail, the rail itself, the road.
- **No car, no sign, no flowers, no offerings. No second object on the rail.**

# 6. REFERENCES

- REF_LOCATION: `峠の道.base` — **未作成。** この作品の画像の経路はまだ走っていない (MEDIUM)
  ⚠️ **この1本は、いま何も添付していない**（ショット記録の `attached: []`）。
- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
  ⚠️ **この1本は文法を使わない。** 最後の一枚は、世界が自分の光で作る。
- REF_SOURCE: `projects/drama-pilot/bible.yaml` (CRITICAL)

# 7. NARRATIVE

- Core Event: She walks away, the sun touches the horizon, **and the paper she left behind goes white.**
- Beginning: Lantern on the rail in the foreground; she is still standing before it.
- Turn: She turns and walks down the road.
- Peak: **The sun reaches the horizon and the paper goes white from inside** — no flame.
- Pull: **The light leaves, and the lantern is only paper again.** The road stays.

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-5s` — density: `held` — She turns her back and walks down the road; the sun touches the horizon, the beam flattens, and **the paper goes white from within.**
  - **CUT at `5s`** — hard, at the same lens and the same frame; no dissolve, no reframing.
  - BEAT 2 `5-9s` — density: `sparse` — **The road is empty.** The paper is still white; then the light fails, and the lantern is only paper.
- Temporal Density: **The cut lands on the brightest second** — the shot gives up its own ending, and keeps the light.

# 9. ACTION

- `ACT_TURN` — Before: she stands at the rail with the lantern unlit. After: she is down the road, and the lantern has taken and lost the sun.
- Causes: the sun's descent. **She causes the departure; the world causes the light.**

## Blocking

- The lantern sits **on the rail in the foreground**, low in the frame, at one edge.
- She stands beside it at 0s, turns, and walks **away from the camera**, down the road, staying on the frame's other side.
- **The distance between the lantern and her grows for the first five seconds** — and then the cut takes her out of the frame entirely. **After the cut, she is not in the shot at all.**

# 10. CAMERA

- Camera Language: **A frame placed behind the lantern, low, looking down the road.** The lantern is close and near the frame's edge; the road recedes through the centre. ⚠️ **The style's physical law, in the card's own words** (`luminous-anime`) — *Camera moves with weight and commitment.* **This shot declines the move** — the light is arriving horizontally, and the frame is already where it lands.
- Camera Events: `5s` — **a hard cut, to the identical frame.** ⚠️ **The camera does not move across it**; the cut removes her, not the frame.
- Camera Behavior: **Still.** The lantern does not grow; she shrinks.

# 11. MOTION

## Subject Motion

She turns, walks down the road, and keeps going — **for five seconds. Then the cut takes her, and the shot keeps going without her.** **She never looks back, never stops, never touches the lantern again.**

## Object Motion

**The lantern does not move** except for the paper settling under the light. **It is the still point of the shot.**

## Environmental Motion

The sun drops to the horizon; the beam flattens from above to horizontal; dust drifts sideways in it; the light fails. **The world's final movement is the light leaving.**

## Physical Characteristics

- Weight: The paper is light; the light on it has no weight at all, and that is the point.
- Inertia: The beam holds its horizontal angle for two seconds, then is gone.
- Acceleration: The failure of light is quick — **the sun is below the horizon, and then it is.**
- Fluidity: Light through paper is the whole of the shot's physics.
- Impact: None.

# 12. EMOTION

- Before: She has set it down, and she is leaving it.
- Pressure: The sun is almost gone, and the frame is nearly empty.
- Turn: **The paper lights up with something that is not fire.**
- After: The light goes, and nothing of it remains but paper.
- Button: **The unlit lantern, white, against a sky that has already lost its sun.**

# 13. LIGHTING

- Base Lighting: The sun is very low and in the frame's centre distance, along the road; the pass is in shadow except a horizontal band.
- Lighting Events: `4-5s` — **the sun touches the horizon and the beam flattens.** `6-7s` — **the light fails.** After that, only skylight.

# 14. AUDIO

- Dialogue: None.
- Sound Effects: Her footsteps on the road, receding; **the paper's faint rustle as the light changes it**; then the wind.
- Music: None.
- Environment: Open pass, evening, and then the quiet that comes after a fall of light.

# 15. CONTINUITY

- Identity: The same girl — white shirt, dark trousers, **empty hands.**
- Spatial: The rail, the gap and the road hold their places; the lantern is on the same rail as `s04`.
- Temporal: **Two passages, joined by one cut.** The first holds her and the last of the light; the second is the same frame with her gone.
- Visual: **The warm palette returns and is taken away; it does not return again.**
- Motion: She moves away; the lantern does not move.
- Sound: Footsteps recede to nothing; wind remains.

# 16. CONSTRAINTS

## MUST NOT（この1本の禁止）

- No close-up of a face.
- No looking back.
- No flame, no ember, no glow source inside the lantern — **the light is the sun's, passing through paper.**
- No lit lantern.
- No readable text of any kind.
- No dialogue.
- No camera move.
- **No dissolve, no fade, no reframing across the cut** — it is a cut, at the same lens.
- No second object on the rail.
- No car or figure entering the road.

## MUST

- The lantern stays in the foreground, on the rail, **and does not move** — including across the cut.
- She walks away and stays away. **After the cut she is not in the frame at all.**
- **The sun reaches the horizon and the paper goes white for a few seconds**, then the light goes.
- The last third of the shot is darker than the middle.

## PREFER

- The lantern at the frame's edge, the road through the centre, her back small in the middle distance.
- The beam nearly horizontal, the dust drifting sideways in it.

## ALLOW

- Anamorphic flare raking across the frame as the sun touches the horizon.

# 17. GENERATION PRIORITIES

1. **The cut at 5s takes her out of the frame** — the audience is not allowed to watch her go.
2. **The paper goes white without a flame** — the light is the sun's.
3. **The lantern does not move** — it is the still point, and the only thing that survives the cut.
4. **She never looks back.**
5. **The light fails** — the last third is darker than the middle.
6. **No camera move** — the cut is not a move.
7. Everything else.

## DIRECTION

Play aftermath for a breath that is taken away. The value turns from dark to
light, and the light is not hers: the sun reaches the horizon, the beam flattens,
and the paper she set down goes white from inside. The stake is that what was set
down still takes the light. **Then cut — at five seconds, on the same lens, with no
dissolve — and she is gone from the frame.** Do not let the audience watch her
leave: the shot keeps the lantern and gives up the girl. No flame, no glow source
— only light passing through paper, for a few seconds, and then gone. End on the
unlit lantern, white, on an empty road.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 9-second wide shot (16:9), one clip, from behind an unlit paper lantern set on a mountain-road guardrail at dusk, looking down the road. The camera is placed once and does not move; inside the clip there is one hard cut, at 5 seconds, to the identical lens and the identical frame. **She is the only person in the frame** — until the cut, after which the frame holds nobody at all. [0-5s] a girl in a white shirt and dark trousers turns her back, her hands empty, and walks down the road away from the camera, the lantern close in the foreground at the frame's edge, and as she recedes the sun touches the horizon and the beam flattens from above to horizontal, and the lantern's paper goes white from within — no flame, no glow source, only the sun passing through it. [cut at 5s] [5-9s] the same frame with her gone: the road empty, the paper still white, then the light fails and the lantern is only paper. The lantern does not move at all, including across the cut; she never looks back. No close-up of a face, no flame, no ember, no lit lantern, no readable text, no dialogue, no second object on the rail, no car, no camera move, no dissolve, no fade.

## Visual Prompt

Luminous realist anime at the last of the dusk: a very low sun on the horizon down the road, a nearly horizontal beam with anamorphic flare raking across the frame, magenta and gold at the horizon against deep cyan below, dust drifting sideways in the beam, the wet road holding a long reflection. A small paper lantern in the foreground at the frame's edge, unlit, its paper translucent, glowing with transmitted sunlight for a few seconds and then only paper. The figure small, dark, seen from behind against a bright horizontal band. Clean anime lineart, never photorealistic. Not a 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces.

## Motion Prompt

Two motions and no more: she walks away down the road and gets smaller, and the light travels down to horizontal and then fails. The lantern in the foreground does not move at all — its paper settles by a few millimetres as the light changes it, and that is the only movement it makes. Dust drifts sideways in the flattening beam rather than falling. The last third of the shot is visibly darker than the middle. There is one hard cut at 5 seconds — it is not a camera move: the frame does not travel, it stays and she leaves it. No camera move, no push, no pan, no dissolve, no fade, no stutter, no held frames with only the hair moving, no full-body articulation.

## Camera Prompt

A wide frame placed behind the lantern, low, looking down the road, composed once at 0s and held. The lantern is close and near the frame's edge; the road recedes through the centre; the horizon sits low in the middle distance. The camera does not push past the lantern, does not follow her, does not tilt up to the sun. At 5 seconds there is one hard cut to the identical frame: the lens, the framing and the horizon do not change — only she is no longer in it. After the cut the camera is exactly where it was. No pan, no tilt, no zoom, no reframe, no dissolve across the cut. The style permits a slow crane or a long pull-back; this shot spends neither — the light is arriving horizontally, and the frame is already where it lands.

## Audio Prompt

The language of this work is Japanese — Japanese is the language of this work and of every word it holds; if any speech is placed in it, that speech is Japanese. No speech is placed in this shot. No dialogue, no voice-over, no narration. Sound effects: her footsteps receding on the road, the paper's faint rustle as the light changes it, then wind. Ambient: an open mountain pass in the evening, and the quiet that comes after a fall of light. Music: none. No score, no BGM, no background music, no drone, no pad, no swell.

## Negative Prompt

no close-up of a face, no photographic faces, no second person, no flame, no ember, no glow source inside the lantern, no lit lantern, no lit lantern before the last shot, no looking back, no readable text, no dialogue, no second object on the rail, no car, no pedestrian, no camera move, no dissolve, no fade, no reframing across the cut, no photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no watermark, no on-screen subtitles, no background music

## Style Motion

Full animation, not limited: dust drifts sideways in the beam, the paper takes and gives up the light, the reflection on the road lengthens — the atmosphere is the primary mover and the figure is subordinate to it. The camera moves with weight and commitment in this style; this shot declines that move on purpose, because the light is arriving horizontally and a crane would take the shot away from what it is watching. Light changes during the shot and then fails. What this style does not do: stutter, shooting on threes, held frames with only the hair moving, a muted palette, a flat gradient sky.

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `drama-pilot-s05-9s-01`
- Segment ID: `05-1`
- Specification Version: `0.1.0`
- Generation Date: `—`（**まだ生成されていない。**）
- Adopted Take: `—`（**まだ採用されていない。** ⚠️ **採用は選別であり、著者が編集である**）

## Resolved Values

- Duration: `9s`
- References: `REF_LOCATION (峠の道.base, 未作成) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_FORMAT (video-spec) ／ REF_SOURCE (bible.yaml, CRITICAL)`
  ⚠️ **この行は「仕様が名指した参照」であって、「実際に渡した参照」ではない。**
- Temporal Structure: `2 beats + 1 cut, NON_UNIFORM — 5s ／ cut ／ 4s`
- Camera Events: `5s — hard cut, identical frame`
- Audio Events: `no dialogue ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — 最初の版である。**生成はまだ一度も走っていない。**

## Observed Problems

（**機械の測定は、まだ無い。**）

## Anticipated risks (to check in the first generation)

1. **The lantern may light with fire.** The brief wants it lit; the shot wants it
   lit by the sun. **Any flame or ember in the paper destroys the ending.**
2. **It may glow like a lamp.** A soft internal glow with no beam is a different
   physics — the paper must be bright because light is coming *through* it.
3. **She may look back.** One glance returns the shot to `s04` and undoes the
   departure.
4. **The light may not fail.** If the frame ends as bright as its middle, the value
   does not turn and there is no aftermath.
5. **The camera may follow her.** It must stay with the lantern.
