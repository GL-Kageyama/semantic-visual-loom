# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第12話 S57「また明日」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「また明日」——スマホを閉じ、光源が画面から窓へ移り、外へ出る。第1本の「撫でる」が始めた弧の終着。ニジは登場しない（朝・外）。朝の通知「今日、あなたが誰かに預けた時間はありません」の下に小さく「また明日」。カメラは玄関の内側に留まる。**

---

# 1. VIDEO

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

# 2. WORLD

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
- ニジ never leaves the screen.

## Visual Language

- Art Direction: `Soft cel anime — flat color planes, clean closed thin lineart, soft-edged shadow terminators`
- Color Language: `Muted, low-saturation. Night = desaturated indigo lit by one cold blue-white screen. Day = pale, slightly overexposed, equally muted. The screen's blue-white is the only value allowed to be bright — and, from seg.10, ニジ's rainbow is the only hue allowed to be saturated`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces`
- Rendering: `Two-step cel shading with softened terminators; gentle bloom around the phone screen; light haze in the dark air`
- Visual Density: `Low. Simple uncluttered rooms, generous negative space, one focal point per beat`

---

# 3. SUBJECTS

## MASHIRO

- ID: `MASHIRO`
- Name: `真白 (Mashiro)`
- Type: `CHARACTER`
- Role: `Protagonist — the one who deposited the time`

### Appearance

- Japanese high-school girl, 16–17, second year. Deliberately unremarkable — the girl slightly outside the middle of the circle.
- Shoulder-length dark hair, a thin neck; small frame; quiet face that gives little away. 「真白」is blankness, not whiteness — an undecorated stillness, not white hair.
- Back curved from long hours over a phone; the memory of the screen's light on her face.
- At night: plain pajamas, in a futon on the floor. By day: standard Japanese school uniform, white collar.
- **Solid and real — she casts a shadow in the scene.** (The contrast anchor: ニジ, her copy, has none.)

### Behavior

- Personality: `Inward, observant, agreeable on the surface. Reads the room and matches it. Small voice`
- Typical Motion: `Almost nothing moves except her fingers. Her body stays still far more than it moves`
- Emotional Range: `Narrow and suppressed. She does not scream, gasp, or widen her eyes. Her reactions register as stillness — a finger stopping, a held breath`

### Continuity Requirements

- Must preserve: `face, shoulder-length hair and color, the thin neck, build, age; the curved posture; the same phone (same size, same case); the same futon, room layout, window and curtain; the restraint — her expression never resolves into a clear readable emotion`

> **ニジ is absent this segment**（ledger 57 — morning, outside）.

---

# 4. ENVIRONMENT

## Location

- ID: `HOME_ENTRYWAY`
- Name: `真白の家の玄関 (her home's entryway)`
- Description: `Morning. Her small home — the futon she has slept in, the curtained window, then the entryway with her shoes and the door. Ordinary pale daylight fills the room; the door opens onto bright daylight beyond. The camera stays inside`

## Environmental Behavior

- Wind: `none — the curtain moves only where her hand opens it`
- Particles: `none — no dust motes, no floating lights, no VFX`
- Background Motion: `none — an ordinary morning, nothing else moves`

---

# 5. OBJECTS

## PHONE

- Type: `smartphone`
- Appearance: `真白's ordinary modern smartphone, plain case, Japanese UI. The only light source at night; the only surface on which the anomaly appears. Glass carries a soft bloom, never a hard specular glint`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
- Continuity Importance: `CRITICAL`

## SCREEN_TEXT

- Type: `UI text`
- Appearance: `The screen-time notification 今日、あなたが誰かに預けた時間はありません, with また明日 small beneath it. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
- Continuity Importance: `CRITICAL`

---

# 6. REFERENCES

## REF_STYLE

- Type: `STYLE`
- Source: `references/styles/soft-cel-anime.md`
- Priority: `HIGH`
- Defines: `rendering, palette discipline, lineart weight, shading steps, motion idiom (holds, twos and threes)`
- Does not define: `events, identity, or emotional tone`

## REF_FORMAT

- Type: `FORMAT`
- Source: `references/formats/video-spec.md`
- Priority: `HIGH`
- Defines: `the §1–20 skeleton, uneven density, the identity lock, the six §18 slots`

## REF_SOURCE

- Type: `SOURCE`
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_12_また明日.md`
- Priority: `CRITICAL`
- Defines: `every event, the exact on-screen text, the ending line, and what is and is not revealed`

## REF_BIBLE

- Type: `BIBLE`
- Source: `soul-voice-teller/examples/gozen-niji/台帳/series-bible.md`
- Priority: `CRITICAL`
- Defines: `the staged disclosure, the voice rules, and the addressee ledger`

## REF_CHARACTER

- Type: `CHARACTER`
- Source: `gozen-niji-mashiro-character-sheet/prompt.md ／ gozen-niji-niji-character-sheet/prompt.md`
- Priority: `HIGH`
- Defines: `the locked character design — 真白 (solid, real, casts a shadow) and ニジ (her copy, one step younger, no shadow, a rainbow afterimage blue → green → blue)`

---

# 7. NARRATIVE

## Core Event

Morning. 真白 closes the phone, opens the curtain, and goes outside. The screen-time notification reads 今日、あなたが誰かに預けた時間はありません — with また明日 small beneath it. The camera stays inside the entryway.

## Beginning

Morning. Ordinary daylight through the window. The futon's warmth is gone. The screen-time notification has arrived; 真白 opens it.

## Turn

On screen: 今日、あなたが誰かに預けた時間はありません — and beneath it, small, また明日. She closes the phone. The light source passes from the screen to the window.

## Peak

She stands, opens the curtain. Outside is clear. She goes out — the empty entryway, her shoes, the bright ordinary daylight beyond the door. The camera stays inside.

## Pull（引き — 切れ目）

「……うん。また、明日」. Cut on 真白 stepping out into the ordinary daylight, the camera still inside the entryway.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The going-out holds 12s (40%).

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「通知」.** Morning, ordinary daylight. The screen shows the notification: 今日、あなたが誰かに預けた時間はありません — with また明日 small beneath it. _Density: DENSE — the final on-screen text, held for legibility._
- **BEAT 2 `[0:07–0:14]` — 「閉じる」.** She closes the phone. The light source passes from the screen to the window. _Density: TRANSITION — quiet, ordinary._
- **BEAT 3 `[0:14–0:26]` — 「外へ」 — REVEAL, longest share.** She stands, opens the curtain. Outside is clear. She goes out — the empty entryway, her shoes, the bright ordinary daylight beyond the door. The camera stays inside. _Density: SPARSE, unhurried — the last motion of the series._
- **BEAT 4 `[0:26–0:30]` — 「また、明日」.** 「……うん。また、明日」. Cut on 真白 stepping out into the daylight. Nothing after it. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the notification また明日 (≈0:03) ／ the phone closing (≈0:09) ／ her stepping out (≈0:22)`

## Temporal Density

- Sparse regions: `0:14–0:30 (the going-out and the line)`
- Dense regions: `0:00–0:07 (the notification)`
- Long continuous action: `0:14–0:26 the going-out`
- Rapid transitions: `none — the slowest, most ordinary segment of the series`

---

# 9. ACTION

## Action — ACT_READ

- ID: `ACT_READ`
- Subject: `MASHIRO`
- Action: `Reads the screen-time notification — 今日、あなたが誰かに預けた時間はありません, with また明日 beneath it`
- Intention: `To see the last notification`
- Intensity: `Low`
- Speed: `Slow`

### Action Relationship

- Before: `—` (continues from S56's dissolved light)
- After: `ACT_CLOSE`

## Action — ACT_CLOSE

- ID: `ACT_CLOSE`
- Subject: `MASHIRO`
- Action: `Closes the phone. The light source passes from the screen to the window`
- Intention: `To end it`
- Intensity: `Low`
- Speed: `Slow, ordinary`

### Action Relationship

- Before: `ACT_READ`
- After: `ACT_GO`

## Action — ACT_GO

- ID: `ACT_GO`
- Subject: `MASHIRO`
- Action: `Stands, opens the curtain, and goes outside — the empty entryway, her shoes, the bright daylight beyond`
- Intention: `To go out into the morning`
- Intensity: `CRITICAL (the peak, expressed as the going-out)`
- Speed: `Slow, unhurried`

### Action Relationship

- Before: `ACT_CLOSE`
- After: `— (cut on her stepping out)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Interior, at the entryway. The camera stays inside — it does not follow her out`
- Lens Character: `Long-ish, shallow. The daylight beyond the door is bright and soft`
- Depth of Field: `Moderate — the entryway in focus, the outside soft and bright`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Close on the screen and her hand — the notification, held for legibility. 今日、あなたが誰かに預けた時間はありません, また明日 small beneath it.
- **`[0:07–0:14]`** — The phone closes; the light source passes to the window. A slow tilt up to her face in the morning light.
- **`[0:14–0:26]`** — She stands, opens the curtain, and crosses to the entryway. The camera holds inside the entryway as she puts on her shoes and steps toward the bright daylight beyond the door. No crane up, no following dolly.
- **`[0:26–0:30]`** — Hold inside the entryway as she steps out into the daylight. Cut precisely on the pull. Nothing after it.

---

# 11. MOTION

## Subject Motion

- Her fingers close the phone; then the rest of her body moves, for the first time in the series, as one ordinary whole
- She stands, opens the curtain, crosses to the entryway, puts on her shoes, and steps out — unhurried
- No arms outstretched, no reaching gesture

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only. Nothing glitches, flickers, or distorts
- The curtain moves only where her hand moves it

## Environmental Motion

- Ordinary morning daylight — pale, slightly overexposed, muted. No golden-hour glow
- Nothing else moves; no wind, no particles, no dust motes

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the floor takes her weight as she stands`
- Inertia: `High, and natural — her body moves as a whole, not with the series' earlier stillness`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Ordinary recognition (the notification また明日)
- ↓ A quiet completion (closing the phone)
- ↓ The going-out (into the ordinary daylight)
- ↓ The line — not a promise, just a fact (また、明日)

## Emotional Events

- Event: `The notification また明日` — Emotion: `Recognition — the last thing the screen will say` — Intensity: `MEDIUM` — Timing: `≈0:03`
- Event: `Closing the phone` — Emotion: `The light source passing to the window — a quiet completion` — Intensity: `LOW` — Timing: `≈0:09`
- Event: `Her stepping out` — Emotion: `The going-out, without ceremony — no tears, no grand gesture` — Intensity: `HIGH — expressed only as an ordinary morning. No facial performance` — Timing: `≈0:22`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Ordinary morning daylight through the window — pale, slightly overexposed, muted`
- Fill Light: `Soft, even — the daylight fills the room`
- Rim Light: `A pale edge where the daylight catches her hair`
- Ambient Light: `Pale daylight. The room is legible, evenly, for the first time in the series`
- Color Temperature: `≈5500K daylight. No golden-hour warmth, no sunset glow`

## Lighting Events

- **`[0:00]`** — Morning daylight already in the room. The screen is dim beside it.
- **`[0:07–0:14]`** — The screen goes dark; the light source passes to the window. Her face is lit by daylight, not from below.
- **`[0:14–0:26]`** — She opens the curtain; the daylight brightens and evens. The entryway, the door, the bright daylight beyond.
- **`[0:30]`** — Cut on the daylight as she steps out. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

> 真白, quiet and even: 「……うん。また、明日」. Nothing else. No narration, no voice-over. No tears. The line is a fact, not a promise, not a goodbye.

## Sound Effects

- The soft click of the phone closing
- The rustle of the curtain as she opens it
- Her footsteps to the entryway, and the slip of shoes
- Faint morning room tone — the day, not the night

## Environment

- Quiet morning room tone — the ordinary sounds of a house waking, nothing more

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Gentle, ordinary. Never sinister, never sentimental — no swelling, no sting`
- Emotional Function: `Hold the morning's stillness, then leave it — room tone and daylight as she steps out`

---

# 15. CONTINUITY

> 57本は57回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

- **Identity**: 真白 — plain Japanese high-school girl 16–17, shoulder-length dark hair, thin neck, small frame, curved posture over a phone. Same face in every take.
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen.
- **The room**: futon on the floor, curtained window, wall clock, sparse.
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light.
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue.
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。

## MUST

- **ニジ does NOT appear** — no ghost, no spirit, no apparition, no second person, no afterimage
- Render the on-screen Japanese exactly: `今日、あなたが誰かに預けた時間はありません` with `また明日` small beneath it
- The morning is ordinary daylight — pale, slightly overexposed, muted
- The camera stays inside the entryway — it does not follow 真白 out
- End by cutting on 真白 stepping out into the daylight, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 57 レンジより）

- **No ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage.** ニジ does not appear
- No golden hour, no sunset glow, no warm low sun — ordinary daylight only
- No crane up, no elevated shot, no arms outstretched — the camera stays inside the entryway
- No tears, no crying

## PREFER

- The going-out unhurried — the whole segment is one ordinary morning
- Silence over score at the peak
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the room furnishing, the entryway, the shoes
- The notification's exact typeface may vary — the text must remain legible
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not appear at all — morning, outside, no ghost, no rainbow (ledger 57). This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school girl in her small room on an ordinary morning. Beats, deliberately uneven: [0:00–0:07] on the phone screen, the screen-time notification reads 今日、あなたが誰かに預けた時間はありません, with また明日 small beneath it; [0:07–0:14] she closes the phone, and the light source passes from the screen to the window; [0:14–0:26] THE REVEAL — she stands, opens the curtain, and goes out, the camera staying inside the entryway as she puts on her shoes and steps toward the bright ordinary daylight beyond the door; [0:26–0:30] 「……うん。また、明日」, and the shot cuts on her stepping out into the daylight. The going-out holds the largest share of the duration. Ends on the daylight, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. Now it is morning — ordinary pale daylight, slightly overexposed, muted, fills the room; the screen is dark. The screen shows the notification 今日、あなたが誰かに預けた時間はありません, with また明日 small beneath it. No ghost, no apparition, no afterimage, no second figure. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her fingers close the phone; then her body moves as one ordinary whole — she stands, opens the curtain, crosses to the entryway, puts on her shoes, and steps out, unhurried, with no arms outstretched. Ordinary weight and inertia: the phone has heft, the floor takes her weight as she stands. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The curtain moves only where her hand moves it. No wind, no particles, no dust motes, no golden-hour glow. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Interior, at the entryway. Longish lens, moderate depth of field — the entryway in focus, the outside soft and bright. Slow, deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] close on the screen and her hand, the notification held for legibility. [0:07–0:14] the phone closes, the light passes to the window; a slow tilt up to her face. [0:14–0:26] she stands, opens the curtain, and crosses to the entryway; the camera holds inside the entryway as she puts on her shoes and steps toward the daylight — no crane up, no following dolly. [0:26–0:30] hold inside the entryway as she steps out; cut precisely on the pull.

## Audio Prompt

Quiet morning room tone. The soft click of the phone closing. The rustle of the curtain as she opens it. Her footsteps to the entryway, and the slip of shoes. 真白, quiet and even: 「……うん。また、明日」. No narration, no voice-over, no other speech. Music extremely sparse — a few sustained tones at most — leaving room tone and daylight as she steps out. No horror strings, no sting, no swelling emotion, no tears.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no tears, no golden hour, no sunset glow, no warm low sun, no crane up, no elevated shot, no arms outstretched, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep12-seg06-30s-01`
- Segment ID: `S57`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_12, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 7s / 12s / 4s. Going-out = BEAT 3 at 12s (40%)`
- Camera Events: `4 events as listed in §10. No dolly; the camera stays inside the entryway`
- Action Events: `ACT_READ → ACT_CLOSE → ACT_GO`
- Audio Events: `真白 one line ／ phone click ／ curtain rustle ／ footsteps ／ morning room tone`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the daylight`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The notification carries the ending. If it renders as noise, generate the screen as a plate and composite the text in post.
- **The model may add a ghost.** The ending invites a sentimental apparition. The negative prompt front-loads "no ghost"; verify frame by frame — this is the single most damaging failure.
- **The morning may read as golden hour.** Ordinary pale daylight only — no sunset glow, no warm low sun. The negative prompt front-loads this.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the going-out reads well, consider a vertical 9:16 variant — the viewer is in the same posture as the protagonist.
