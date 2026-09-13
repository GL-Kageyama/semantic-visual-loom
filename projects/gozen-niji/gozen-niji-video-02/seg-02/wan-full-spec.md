# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第2話 S07「ありがとう、いつもごめんね」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「美月の親指が、するりと撫でる開き方」——第1話の真白と同じ所作（指の背骨の第7本）。ニジは不在（送信済みの文字としてのみ）。登場人物は真白と美月。画面文字は送信済みの一文「ありがとう、いつもごめんね。」。最大の秒はその一文の開示に、次に「これ、私じゃない」の否定に。**

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

> **美月 appears this segment**（best friend — bright, direct; sees through 真白's lie but does not press it）. ニジ is absent（ledger 06–09 — the ghost exists only as sent text）.

---

# 4. ENVIRONMENT

## Location

- ID: `CLASSROOM`
- Name: `教室 (the classroom)`
- Description: `Ordinary Japanese classroom, morning light making long thin shadows across desks`

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
- Appearance: `One sent message, exactly: ありがとう、いつもごめんね。 — from 真白's own account, timestamped 午前3時. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `CRITICAL`
- Visual Importance: `CRITICAL`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_02_おまえが言えなかった、たった一言.md`
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

The sentence 真白 never sent — `ありがとう、いつもごめんね。` — sits in her thread with 美月 as a sent message, timestamped 3:00 A.M., from her own account, while she slept.

## Beginning

美月, at the next seat, asks 「あれ、真白、昨日、ありがとうって送った？」 Her thumb strokes the chat open — the same smooth gesture 真白 knows in her own hand.

## Turn

The thread opens. 昨夜、午前3時ちょうど。 Sent from 真白's account: `ありがとう、いつもごめんね。` 真白 sent nothing last night — after that other message she hid the phone under the pillow and slept. The message came from that phone, anyway.

## Peak

「これ、私じゃない」 — 真白 says it, voice shaking. On her knees, her hand closes; nails dig into the palm.

## Pull（引き — 切れ目）

Cut on the sent message, `ありがとう、いつもごめんね。`, held on screen, unmoving — and the denial 「これ、私じゃない」 hanging in the air. 誰が、送った。 Not answered.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The reveal of the sent message holds 11s (37%); the denial is held 4s.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the morning classroom; the sent line is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「ありがとうって送った？」.** Morning classroom, unchanged. 美月, at the next seat: 「あれ、真白、昨日、ありがとうって送った？」 _Density: SPARSE — one question, quiet daylight._
- **BEAT 2 `[0:06–0:15]` — 「開く」.** 美月's thumb strokes the chat open — the same smooth gesture 真白 knows in her own hand. The thread opens. _Density: TRANSITION — one insert, the borrowed gesture._
- **BEAT 3 `[0:15–0:26]` — 「届いた言葉」 — REVEAL, longest share.** The sent bubble, timestamped 3:00 A.M., from 真白's own account: ありがとう、いつもごめんね。 A slow dolly in until the line fills the frame. Nothing else moves. _Density: DENSE at the head, then the line alone, held._
- **BEAT 4 `[0:26–0:30]` — 「これ、私じゃない」 — held, then cut.** Cut to her hand closing in her lap, nails into the palm. 「これ、私じゃない」 — voice shaking. Cut on the line and the denial. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the sent bubble with the timestamp (≈0:17) ／ the line filling the frame (≈0:21) ／ the hand closing and the denial (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the question), 0:26–0:30 (the denial)`
- Dense regions: `0:15–0:26 (the reveal of the sent message)`
- Long continuous action: `0:15–0:26 the line held on screen`
- Rapid transitions: `none — the reveal is the whole point`

---

# 9. ACTION

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MITSUKI`
- Action: `Asks 「あれ、真白、昨日、ありがとうって送った？」`
- Intention: `To check something she half-remembers. Light, curious`
- Intensity: `Low`
- Speed: `Ordinary, bright`

### Action Relationship

- Before: `—` (continues from S06's opened chat)
- After: `ACT_OPEN`

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MITSUKI`
- Action: `Her thumb strokes the chat open — the same smooth gesture 真白 knows in her own hand`
- Intention: `To open the thread with 真白`
- Intensity: `Low`
- Speed: `Practiced, smooth — the borrowed gesture`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_READ`
- Causes: `ACT_READ`

## Action — ACT_READ

- ID: `ACT_READ`
- Subject: `MASHIRO`
- Action: `Eyes move over the sent message, once — 午前3時, her own account, the line`
- Intention: `To understand. She sent nothing last night`
- Intensity: `Medium, internal`
- Speed: `Slow, and slowing`

### Action Relationship

- Before: `ACT_OPEN`
- After: `ACT_CLENCH`

## Action — ACT_CLENCH

- ID: `ACT_CLENCH`
- Subject: `MASHIRO`
- Action: `On her knees, her hand closes; nails dig into the palm. The reaction, in the hand, not the face`
- Intention: `To keep the face from giving anything away`
- Intensity: `CRITICAL (the fear, expressed only in the hand)`
- Speed: `Slow, tightening, held`

### Action Relationship

- Before: `ACT_READ`
- After: `ACT_DENY`

## Action — ACT_DENY

- ID: `ACT_DENY`
- Subject: `MASHIRO`
- Action: `「これ、私じゃない」 — small, voice shaking`
- Intention: `To deny what her own phone has done`
- Intensity: `Medium, suppressed — a shake in the voice, nothing more`
- Speed: `Quick, then still`

### Action Relationship

- Before: `ACT_CLENCH`
- After: `— (cut on the line)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, at desk height. Over-the-shoulder on the screen for the reveal`
- Lens Character: `Long-ish, shallow. Only the screen or the hands are ever sharp`
- Depth of Field: `Shallow — the classroom falls away to soft daylight`
- Camera Style: `Slow, deliberate, nearly still. One sustained dolly, and it belongs to the reveal`

## Camera Events

- **`[0:00–0:06]`** — Static two-shot at desk level. 美月 asks; 真白 still behind.
- **`[0:06–0:11]`** — Insert: 美月's thumb on glass, macro-close — the same smooth stroke 真白 knows in her own hand.
- **`[0:11–0:15]`** — Rack focus from the finger to the screen as the thread opens. Over-the-shoulder on 真白's screen.
- **`[0:15–0:22]`** — One slow continuous dolly in on the sent bubble — the timestamp, then the line. The segment's single sustained move.
- **`[0:22–0:26]`** — Absolutely locked on the line, filling the frame. Static.
- **`[0:26–0:30]`** — Cut down to her hand in her lap, closing, nails into the palm. Hold. Cut on the line and the denial.

---

# 11. MOTION

## Subject Motion

- 美月's thumb strokes the screen open — the same smooth practiced arc as 真白's own, the borrowed gesture
- 真白's body holds; her hand closes slowly in her lap, tightening
- The denial is a small voice, a shake — the face does not perform
- Almost all movement belongs to the fingers and the closing hand

## Object Motion

- The phone moves only as 美月's thumb opens it — ordinary UI motion, no glitch, no flicker
- Screen content changes by ordinary UI transitions only — a thread opening, a sent bubble
- The sent line does not move once it is on screen

## Environmental Motion

- Morning light is still; long thin shadows lie unmoving
- The classroom's soft out-of-focus movement is distant and untroubled

## Physical Characteristics

- Weight: `Ordinary. The phone has heft`
- Inertia: `High for the bodies, near-zero for the thumb`
- Acceleration: `Gentle everywhere except the hand, which tightens gradually`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet curiosity (the question, lightly asked)
- ↓ Cold recognition (the message she did not send, from her own account)
- ↓ Fear, in the hand (the closing fist, the nails)
- ↓ Denial that does not hold (これ、私じゃない — and 誰が送った, unanswered)

## Emotional Events

- Event: `The sent bubble appears, timestamped 3:00 A.M., from her own account`
  Emotion: `Cold recognition — not yet fear, recognition`
  Intensity: `HIGH`
  Timing: `≈0:17`

- Event: `The hand closes, nails into the palm`
  Emotion: `Fear, expressed only in the hand`
  Intensity: `CRITICAL — no facial performance`
  Timing: `≈0:27`

- Event: `「これ、私じゃない」`
  Emotion: `Denial — small, shaking, unanswered`
  Intensity: `MEDIUM, suppressed`
  Timing: `≈0:28`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Pale flat classroom daylight from the left windows — soft, slightly overexposed`
- Fill Light: `Even, flat. The classroom is bright and unbothered`
- Rim Light: `A faint cool edge along her hair from the window`
- Ambient Light: `Day. Muted, low-saturation`
- Color Temperature: `≈5600K pale daylight. The phone screen's blue-white reads faint against it`

## Lighting Events

- **`[0:00]`** — Morning light already full; long thin shadows across the desks.
- **`[0:11–0:15]`** — As the thread opens, the screen's blue-white rises faintly on 美月's face.
- **`[0:15–0:26]`** — As the camera closes on the screen, its glow dominates the frame; the line is the brightest thing in the daylight.
- **`[0:26–0:30]`** — Cut to the hand in the lap, in flat pale light. Cut on the line.

---

# 14. AUDIO

## Dialogue

- 美月: 「あれ、真白、昨日、ありがとうって送った？」 — light, curious
- 真白: 「これ、私じゃない」 — small, voice shaking

> The sent message is **not spoken, not whispered, not read aloud.** No voice reads it — not 真白's, not 美月's, and not any ghost's. No narration, no voice-over.

## Sound Effects

- The soft friction of 美月's thumb on glass as she opens the chat
- Morning classroom ambience, thinned and distant once the camera closes on the screen
- The subtle sound of a hand tightening in fabric, in the lap

## Environment

- Day. Full and ordinary classroom ambience that recedes as the reveal takes over

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental — no horror strings`
- Emotional Function: `Hold the morning's surface, then thin to nothing as the camera closes on the line. By the denial there is only room tone, the thumb's friction, and a held breath`

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

- Render the on-screen Japanese exactly: `ありがとう、いつもごめんね。` — sent from 真白's own account, timestamped 午前3時
- Show the line as the reveal — the sentence 真白 never sent, delivered while she slept
- Let the reaction live in the hand (the closing fist, the nails), never the face
- End by cutting on the line, held on screen, with the denial 「これ、私じゃない」 and nothing after it

## MUST NOT（この1本の禁止・開示台帳 06–09 レンジより）

- **Do not show the ghost.** No figure, no silhouette, no reflection, no second person, no eyes, no hand but the two girls' own. ニジ does not appear in this episode
- **No rainbow, no iridescence, no colored afterimage.** Her color is introduced later
- **No voice for the ghost.** The sent message is not read aloud, whispered, or narrated — it exists only as text
- Do not make 美月 sinister, doubtful, or knowing — she asks lightly, with no suspicion
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- Framing the line large, straight-on and held rather than skimmed — legibility is the whole point
- The hand in the lap over the face, for the reaction
- Silence over score at the reveal

## ALLOW

- Slight variation in classroom background students and desk arrangement
- The timestamp may render as 午前3:00 (an ordinary UI timestamp); if it does not read, the line alone suffices
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must not be shown (ledger 06–09 — the ghost exists only as sent text); the sent message ありがとう、いつもごめんね。 is text only, never voiced. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school classroom in the morning. Beats, deliberately uneven: [0:00–0:06] 美月 at the next seat asks あれ、真白、昨日、ありがとうって送った？; [0:06–0:15] her thumb strokes the chat open — the same smooth gesture 真白 knows in her own hand — and the thread opens; [0:15–0:26] THE REVEAL — a sent bubble, timestamped 3:00 A.M., from 真白's own account, reads ありがとう、いつもごめんね。 and the camera closes slowly until the line fills the frame; [0:26–0:30] cut to her hand closing in her lap, nails into the palm, and 真白 says これ、私じゃない in a shaking voice, and the shot cuts on the line. The reveal holds the largest share of the duration. Ends on the line, held, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, muted low-saturation palette, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. By day she wears a standard Japanese school uniform. Scene: a Japanese high-school classroom in the morning, pale flat daylight, slightly overexposed and muted. Beside her, 美月 (Mitsuki) — bright and direct, with slightly shorter, livelier hair and an open upright posture, in the same uniform. The phone screen shows an ordinary Japanese messaging thread: one sent bubble reading exactly ありがとう、いつもごめんね。 with the timestamp 午前3:00. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the fingers and one hand. 美月's thumb strokes the screen open in a smooth practiced arc — the same gesture 真白 makes with her own hand. 真白's body holds; her hand closes slowly in her lap, tightening, nails into the palm. The denial is a small voice, a shake — the face does not perform. The phone moves only as 美月's thumb opens it, and its screen changes only by ordinary UI transitions; once on screen the sent line does not move. Gentle acceleration everywhere except the gradually tightening hand. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, at desk height; over-the-shoulder on the screen for the reveal. Longish lens, shallow depth of field; only the screen or the hands are sharp. Slow and deliberate, nearly still. [0:00–0:06] static two-shot, 美月 asks, 真白 still behind. [0:06–0:11] insert, macro-close on 美月's thumb on glass — the same smooth stroke. [0:11–0:15] rack focus from the finger to the screen as the thread opens. [0:15–0:22] one slow continuous dolly in on the sent bubble — the timestamp, then the line. [0:22–0:26] absolutely locked on the line, filling the frame, static. [0:26–0:30] cut down to her hand closing in her lap; hold; cut on the line and the denial.

## Audio Prompt

Day. Full ordinary classroom ambience that recedes as the camera closes on the screen. Two lines of dialogue only: 美月 asks あれ、真白、昨日、ありがとうって送った？ light and curious; 真白 answers これ、私じゃない, small and shaking. The sent message is not spoken, not whispered, not read aloud — no voice reads it, no narration, no voice-over. The soft friction of a thumb on glass as the chat opens. Music extremely sparse — a few sustained tones at most — thinning to nothing as the camera closes on the line, leaving only room tone, the thumb's friction, and a held breath. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no ghost, no spirit, no apparition, no second person, no silhouette of another figure, no reflection of anyone else, no extra hands, no glowing eyes, no rainbow, no iridescence, no colored afterimage, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep02-seg02-30s-01`
- Segment ID: `S07`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_02, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 9s / 11s / 4s. Reveal = BEAT 3 at 11s (37%)`
- Camera Events: `6 events as listed in §10. One sustained dolly (0:15–0:22)`
- Action Events: `ACT_ASK → ACT_OPEN → ACT_READ → ACT_CLENCH → ACT_DENY`
- Audio Events: `two lines of dialogue ／ message silent, never voiced ／ music gone by the denial`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the line`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- *(none yet — to be filled after the first generation)*

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The single line carries the reveal. If it renders as noise the segment fails. Check first; if unusable, generate the screen as a plate and composite the text in post.
- **The model may add a ghost.** "sent at 3 A.M. from her own account" is a strong horror prior. The negative prompt front-loads this; verify frame by frame.
- **The hand may not read as the reaction.** The closing fist is the emotion. If the face performs instead, the restraint is broken — keep the face still.
- **美月 reads as suspicious.** She must ask lightly, with no hidden knowledge. If her curiosity reads as menace, the episode inverts.

## Changes

- *(none yet)*

## Next Generation

- If the line renders cleanly and the hand carries the reaction, this segment is done; S08 depends on 美月's genuine reaction to this same line.
