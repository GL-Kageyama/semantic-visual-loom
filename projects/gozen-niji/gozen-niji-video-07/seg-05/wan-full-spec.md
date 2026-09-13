# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第7話 S31「わたしは」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**ニジが、初めて、真白の目をまっすぐ見る。そして、初めて「わたし」と言う——「――わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ」。不透明のまま、体が消えることはない。**

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

## NIJI

- ID: `NIJI`
- Name: `ニジ (Niji)`
- Type: `CHARACTER (apparition, on-screen only)`
- Role: `The ghost of 2 A.M. — the crystallization of feelings 真白 never received`

### Appearance

- **真白's own face, one step younger** — longer lashes, slightly fuller cheeks. The same shoulder-length dark hair and thin neck; the same way of tilting her head.
- A blurred rainbow afterimage that resolves into that outline. Colors drift slowly: blue → green → blue.
- The outline is slightly blurred at the edges. **No shadow anywhere** — unlike 真白's solid, defined outline.
- Exists **inside the screen**. Never stands in the room at human scale.

### Behavior

- Personality: `Bright, teasing, unguarded — she smiles more honestly than 真白 can. She never cries. She calls 真白「おまえ」`
- Continuity: `her opacity is a strict function of the segment number (see the ledger); it never varies within a beat except in seg.55`

> **ニジ appears this segment**（ledger 31 — in, opaque; first direct eye contact with 真白 and her first わたし）. No other character appears — 美月・小春・湊 do not appear.

---

# 4. ENVIRONMENT

## Location

- ID: `CLASSROOM`
- Name: `教室 (the darkened classroom, night)`
- Description: `The classroom at night — 真白 alone, the phone screen the only light, ニジ inside the screen. ニジ meets 真白's eyes for the first time`

## Environmental Behavior

- Wind: `none — the curtain does not move`
- Particles: `only the faintest haze catching the screen's bloom; no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; at most one distant car's headlights crossing the curtain, once`

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
- Appearance: `No message text this segment — ニジ's self-introduction is spoken (声), not rendered as text. No captions, no subtitles burned in`
- Narrative Importance: `LOW`
- Visual Importance: `LOW`
- Continuity Importance: `LOW`

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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_07_文化祭前夜、スクリーンタイムを全部開く.md`
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

真白 asks ニジ the question she has held back for so long. ニジ looks into 真白's eyes for the first time — and, for the first time, calls herself わたし, and tells her what she is.

## Beginning

真白 holds the phone, and asks the question she has never once been able to voice. 「……ニジ、教えて」

## Turn

「なに？」「あなたは、――何なの」

## Peak

ニジ looks into 真白's eyes — the first time she has ever met her gaze directly. Then, for the first time: わたし。「――わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ」

## Pull（引き — 切れ目）

ニジ's face, inside the screen, opaque — still meeting 真白's eyes. 真白's eyes widen, just barely. Cut on ニジ, still there, not vanishing.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** ニジ's first わたし and her answer hold 11s (37%); the eye-contact holds 7s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「教えて」 — the question, at last.** 真白 holds the phone and asks, small and quiet: 「……ニジ、教えて」「あなたは、――何なの」. _Density: SPARSE — one held question._
- **BEAT 2 `[0:06–0:09]` — 「なに？」 — the blank beat.** ニジ tilts her head, blank and uncomprehending: 「なに？」. _Density: SPARSE — a beat of near-nothing, the exchange suspended._
- **BEAT 3 `[0:09–0:16]` — 「目を、見る」 — first eye contact.** ニジ looks into 真白's eyes — the first time, held. The gaze itself is the turn. _Density: HELD — no dialogue, only the meeting of eyes._
- **BEAT 4 `[0:16–0:27]` — 「わたしは」 — the first わたし, longest share.** 「――わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ」. _Density: DENSE at the head, then the line, held._
- **BEAT 5 `[0:27–0:30]` — 「真白の目」 — the smallest widening, then cut.** 真白's eyes widen, just barely. Cut on ニジ, still there, not vanishing. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the question (≈0:03) ／ the blank なに？ (≈0:07) ／ the first eye contact (≈0:11) ／ the first わたし (≈0:18) ／ 真白's eyes widening (≈0:29)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the question), 0:06–0:09 (the blank beat)`
- Dense regions: `0:16–0:27 (the answer, longest share)`
- Long continuous action: `0:09–0:16 the eye contact, held; 0:27–0:30 the widening`
- Rapid transitions: `none — a slow, held night`

---

# 9. ACTION

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MASHIRO`
- Action: `Holds the phone and asks — 「……ニジ、教えて」「あなたは、――何なの」`
- Intention: `To finally voice the question she has never once been able to ask`
- Intensity: `Low, quiet`
- Speed: `Slow, small voice`

### Action Relationship

- Before: `— (continues from S30's smile)`
- After: `ACT_BLANK`

## Action — ACT_BLANK

- ID: `ACT_BLANK`
- Subject: `NIJI`
- Action: `Tilts her head, blank and uncomprehending — 「なに？」`
- Intention: `Not avoidance — genuine failure to understand the question`
- Intensity: `Low`
- Speed: `Still, a small head-tilt`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_LOOK`

## Action — ACT_LOOK

- ID: `ACT_LOOK`
- Subject: `NIJI`
- Action: `Looks into 真白's eyes — the first time, held, unblinking, through the screen`
- Intention: `The gaze is the answer before the words — she stops playing, and meets her`
- Intensity: `Medium, held`
- Speed: `Still — only the gaze moves`

### Action Relationship

- Before: `ACT_BLANK`
- After: `ACT_NAME`

## Action — ACT_NAME

- ID: `ACT_NAME`
- Subject: `NIJI`
- Action: `Says it, for the first time — 「――わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ」`
- Intention: `To tell her, plainly, what she is — her first わたし`
- Intensity: `Medium, calm`
- Speed: `Even, slow — 句点で切る`

### Action Relationship

- Before: `ACT_LOOK`
- After: `— (cut on ニジ, still there)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Into the screen with her`
- Lens Character: `Long-ish, shallow. Only the screen or her face are ever sharp`
- Depth of Field: `Very shallow — the classroom falls away into near-black`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Close on 真白's face, lit from below, as she asks — 「……ニジ、教えて」「あなたは、――何なの」.
- **`[0:06–0:09]`** — Cut inside the screen — ニジ tilts her head, blank: 「なに？」.
- **`[0:09–0:16]`** — Hold on ニジ's face as her eyes meet 真白's, through the glass. No camera movement. The gaze is the shot.
- **`[0:16–0:27]`** — Hold on ニジ as she says ――わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ. The rainbow afterimage soft behind her.
- **`[0:27–0:30]`** — Close on 真白's eyes, widening just barely, then back to ニジ — still there, opaque, not vanishing. Cut on ニジ.

---

# 11. MOTION

## Subject Motion

- 真白 holds the phone still; only her lips move, small, and then her eyes widen — the barest fraction
- ニジ tilts her head once, then meets 真白's eyes and holds still — only her eyes move, then her lips, slow
- ニジ's rainbow colors drift slowly — blue → green → blue — the only continuous motion

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only. Nothing glitches, flickers, or distorts

## Environmental Motion

- The classroom is still and dark; nothing moves in it
- No wind, no moving shadows, no particles

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand`
- Inertia: `High for the bodies, near-zero for the finger`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Courage (voicing the question she never could)
- ↓ Blankness (ニジ's genuine なに？ — the exchange suspended)
- ↓ Recognition (the first meeting of eyes — the gaze is the turn)
- ↓ Astonishment (her first わたし — おまえが預けた時間が集まった姿だよ)
- ↓ The smallest widening (真白's eyes, just barely)

## Emotional Events

- Event: `真白 voices the question — あなたは、何なの` — Emotion: `Courage — the long-withheld question, finally asked` — Intensity: `MEDIUM, quiet` — Timing: `≈0:03`
- Event: `ニジ looks into 真白's eyes — the first time` — Emotion: `Recognition — the meeting of eyes before any word` — Intensity: `HIGH, held` — Timing: `0:09–0:16`
- Event: `ニジ's first わたし — おまえが、誰かに、預けた、時間が、集まった、姿だよ` — Emotion: `Astonishment — the disclosure, given plainly, without drama` — Intensity: `HIGH` — Timing: `≈0:18`
- Event: `真白's eyes widen, just barely` — Emotion: `The smallest breach in her restraint — not shock, the beginning of understanding` — Intensity: `MEDIUM, withheld` — Timing: `≈0:29`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft darkness fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `Near-black. The classroom is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against near-black; ニジ's rainbow the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on her face from below.
- **`[0:06–0:16]`** — Inside the screen, ニジ's rainbow is the frame's only saturated color; cold blue-white on 真白's face outside, the two lights meeting through the glass.
- **`[0:16–0:27]`** — Close on ニジ as she speaks — the rainbow soft behind her.
- **`[0:27–0:30]`** — 真白's eyes in the screen's light, widening; then ニジ, still lit, still there. Cut.

---

# 14. AUDIO

## Dialogue

- 真白: 「……ニジ、教えて」→「あなたは、――何なの」 — small, quiet, the question held back until now
- ニジ: 「なに？」→「――わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ」 — even, calm, slow — her first わたし

> No other speech. ニジ's わたし is the first time she uses the first person. No narration, no voice-over.

## Sound Effects

- The near-silence of an emptied school at night, held
- Almost nothing — the quiet itself is the sound

## Environment

- Deep quiet, almost nothing

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, warm. Never sinister, never sentimental — no horror strings, no swelling`
- Emotional Function: `Hold the room's stillness under the exchange; thin to nothing at her わたし, leaving only room tone`

---

# 15. CONTINUITY

> 57本は57回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

- **Identity**: 真白 — plain Japanese high-school girl 16–17, shoulder-length dark hair, thin neck, small frame, curved posture over a phone. Same face in every take.
- **The phone**: same size, same plain case, Japanese UI, cold blue-white screen.
- **The room**: futon on the floor, curtained window, wall clock, sparse.
- **The light law**: at night the screen is the only light, from below her face; her face nearly silhouetted; no fill light.
- **The palette law**: muted and low-saturation everywhere; the screen's blue-white is the only bright value; (seg.10+) ニジ's rainbow is the only saturated hue.
- **The motion law**: limited animation, holds, twos and threes; almost all movement belongs to the fingers.
- **(seg.10+) ニジ**: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same neck tilt and shoulder-length hair — a rainbow afterimage inside the screen, casting no shadow, at the opacity this segment requires.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は [series-constants §16 相当](../../gozen-niji-video-00-series/series-constants.md)。ここには**この1本に固有**の制約のみ。

## MUST

- Render ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same head-tilt — a blurred rainbow afterimage, **fully opaque**, inside the screen only, never at human scale in the room
- ニジ looks into 真白's eyes — the first time, held, through the glass
- ニジ's line is exactly: わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ — spoken calmly, 句点で切る, her first わたし
- End on ニジ, still there — cut on her, not vanishing

## MUST NOT（この1本の禁止・開示台帳 31 レンジより）

- **Do not make ニジ transparent.** No translucent apparition, no see-through figure, no fading ghost — she is opaque
- **Do not let ニジ's body dissolve or disappear.** No dissolving into light, no fading out, no vanishing at the cut — she is still there when the shot ends
- **Do not have ニジ leave the screen or enter the room.** She exists inside the screen only, never at human scale
- **ニジ must not cry.** No tears — she does not know how to cry
- No 美月, no 小春, no 湊 as live figures — only 真白 and ニジ
- No on-screen subtitles or captions burned in (the line is spoken, not text)
- Do not have 真白 scream, gasp, or widen her eyes beyond the barest fraction

## PREFER

- The meeting of eyes over any performed emotion — the gaze is the turn
- 真白's smallest widening over any explicit reaction
- Silence over score at ニジ's わたし

## ALLOW

- Slight variation in the classroom furnishing
- The gaze may be a single held shot or a cut between the two faces through the glass
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must be shown fully opaque inside the screen (ledger 31 — in, opaque); no transparency, no dissolving body; she meets 真白's eyes for the first time and says わたし for the first time. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school girl alone in her darkened classroom at night, ニジ inside the phone screen. Beats, deliberately uneven: [0:00–0:06] 真白 asks, small and quiet — ……ニジ、教えて; あなたは、何なの; [0:06–0:09] ニジ tilts her head, blank: なに？; [0:09–0:16] ニジ looks into 真白's eyes — the first time, held, through the glass; [0:16–0:27] ニジ's first わたし: ――わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ; [0:27–0:30] 真白's eyes widen, just barely, and the shot cuts on ニジ — still there, not vanishing. ニジ is fully opaque, no shadow, inside the screen only, 真白's own face one step younger with the same shoulder-length dark hair and thin neck, a rainbow afterimage. The eye contact and the first わたし hold the largest share. Ends on ニジ, still there, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. By day she wears a standard Japanese school uniform; here, after school, she is alone in the classroom in that uniform. A darkened classroom: the phone screen the only light, cold blue-white from below, her face nearly silhouetted, shadows deep and soft, no fill. ニジ: inside the screen only, never at human scale in the room — 真白's own face one step younger (longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same head-tilt), a blurred rainbow afterimage that resolves into that outline, fully opaque, no shadow, colors drifting slowly blue → green → blue, meeting 真白's eyes. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. 真白 holds the phone still; only her lips move, small, and then her eyes widen — the barest fraction. ニジ tilts her head once, then meets 真白's eyes and holds still — only her eyes move, then her lips, slow. Her rainbow colors drift slowly, blue → green → blue. Ordinary weight and inertia: the phone has heft in her hand. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. Only the screen's bloom breathes faintly in the dark. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder — into the screen with her. Longish lens, very shallow depth of field; only the screen or her face are ever sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] close on 真白's face, lit from below, as she asks. [0:06–0:09] cut inside the screen — ニジ tilts her head, blank: なに？. [0:09–0:16] hold on ニジ's face as her eyes meet 真白's, through the glass, no camera movement. [0:16–0:27] hold on ニジ as she says ――わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ, the rainbow afterimage soft behind her. [0:27–0:30] close on 真白's eyes, widening just barely, then back to ニジ — still there, opaque, not vanishing; cut on ニジ.

## Audio Prompt

Deep quiet night room tone — the near-silence of an emptied school. Dialogue only, small and warm: 真白 — ……ニジ、教えて; あなたは、何なの. ニジ — なに？; ――わたしは、おまえが、誰かに、預けた、時間が、――集まった、姿だよ, even and calm, 句点で切る — her first わたし. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning to nothing at her わたし, leaving only room tone. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparency, no translucent apparition, no see-through figure, no fading ghost, no dissolving body, no vanishing figure, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep07-seg05-30s-01`
- Segment ID: `S31`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_07, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `5 beats, NON_UNIFORM — 6s / 3s / 7s / 11s / 3s. ニジ's answer = BEAT 4 at 11s (37%)`
- Camera Events: `5 events as listed in §10. No rack focus — cuts only`
- Action Events: `ACT_ASK → ACT_BLANK → ACT_LOOK → ACT_NAME`
- Audio Events: `dialogue (真白 + ニジ) ／ music thinning to nothing at her わたし`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on ニジ — still there`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ may dissolve or vanish at the cut.** This is the one segment where that must absolutely not happen. If her body fades or disappears, regenerate — the pull is that she is still there.
- **The first わたし may be delivered with too much weight.** It is calm and plain, not a dramatic reveal. If it is read as a swelling climax, pull it back to an even, slow delivery.
- **The eye contact may not read as the first time.** The gaze is the turn. If it reads as ordinary looking, hold the shot longer and drop the smile — she is meeting her, not performing.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the eye contact, the first わたし, and the final still-present cut all read, episode 7 is complete — S32 begins the next turn, after the disclosure.
