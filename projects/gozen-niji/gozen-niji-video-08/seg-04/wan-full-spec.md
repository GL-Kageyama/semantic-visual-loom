# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第8話 S35「最初の宛先」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「触れて、止まる」の反転——S03 の止まりが、驚きから決めかねに反転する（指の背骨の第35本）。ニジは在る（画面の中だけ・完全に不透明・主役は真白の指）。登場人物は真白とニジのみ（小春は名前と文字だけの宛先）。画面文字なし。押さない・打たない・送らない。**

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

> **ニジ appears this segment**（ledger S35 — 在）. 真白とニジのみが人物。小春は名前と文字だけの宛先で、顔は出さない。

---

# 4. ENVIRONMENT

## Location

- ID: `BEDROOM`
- Name: `真白の部屋 (her bedroom)`
- Description: `Small, futon on the floor, curtained window, wall clock, desk, few objects. Dark except for the phone. The recurring stage — most night takes live here`

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
- Appearance: `No message text this segment — only ordinary UI: a thread list, then one opened thread — 小春's consultation, read and left unanswered — the message itself left unreadable, out of focus. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
- Continuity Importance: `HIGH`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads 2:00 at the hinge of the night`
- Narrative Importance: `MEDIUM`
- Visual Importance: `MEDIUM`
- Continuity Importance: `MEDIUM`

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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_08_わたしは、おまえが預けた時間.md`
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

真白 opens the first addressee — 小春's consultation, read and left unanswered for a month — and her fingertip comes down, touches the glass above it, and stops.

## Beginning

The room, still dark. ニジ's last line still in the air: 返してくれたら、わたしは、帰れる。 真白 looks at the thread list. The first addressee: 小春.

## Turn

She opens the thread. 小春's consultation — a long message, read, left unanswered for a month. あの言葉. 真白 reads it again, once.

## Peak

Her fingertip descends, makes contact with the glass above the thread — and stops. Not pressing, not tapping, not sending. The stop of S03, reversed: there it stopped from shock, here it stops from being unable to decide.

## Pull（引き — 切れ目）

Hold on the stopped fingertip, on the glass above the thread. Cut on the finger. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The stopped finger holds 9s (30%).

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「宛先リスト」 — ESTABLISH.** Dark bedroom. ニジ's last line still in the air. 真白 looks at the thread list — the first addressee: 小春. _Density: SPARSE — a held silence, no speech._
- **BEAT 2 `[0:07–0:15]` — 「最初の宛先」.** She opens the thread. 小春's consultation — a long message, read and left unanswered for a month. あの言葉. 真白 reads it again, once. Her eyes move over the line. _Density: TRANSITION — the thread opens; quiet recognition._
- **BEAT 3 `[0:15–0:24]` — 「止まる」 — PEAK, longest share.** Her fingertip descends, contacts the glass above the thread — and STOPS. Not pressing, not tapping, not sending. The stop of S03, reversed: not from shock, but from being unable to decide. _Density: DENSE at the head, then the finger alone, held._
- **BEAT 4 `[0:24–0:30]` — 「触れたまま」.** Hold on the stopped fingertip, on the glass above the thread. Cut on the finger. Nothing after it. _Density: HELD — then a clean cut on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the first addressee 小春 (≈0:05) ／ the month-old consultation, read and unanswered (≈0:10) ／ the fingertip touching and stopping (≈0:16, then held)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the thread list), 0:24–0:30 (the held stop)`
- Dense regions: `0:15–0:24 (the finger stopping)`
- Long continuous action: `0:15–0:24 the fingertip held on the glass`
- Rapid transitions: `none — a slow, still night`

---

# 9. ACTION

## Action — ACT_SCAN

- ID: `ACT_SCAN`
- Subject: `MASHIRO`
- Action: `Looks at the thread list; her eyes find the first addressee — 小春`
- Intention: `To face what 返すの begins with`
- Intensity: `Low`
- Speed: `Slow`

### Action Relationship

- Before: `—` (continues from S34's 「帰れる」)
- After: `ACT_OPEN`

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MASHIRO`
- Action: `Opens the thread — 小春's consultation, a long message, read and left unanswered for a month`
- Intention: `To look again at the words she left behind`
- Intensity: `Medium, internal`
- Speed: `Slow, ordinary`

### Action Relationship

- Before: `ACT_SCAN`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `MASHIRO`
- Action: `Her fingertip descends, touches the glass above the thread — and stops. Not pressing, not tapping, not sending`
- Intention: `None that resolves — she cannot decide. The body arrives before the decision`
- Intensity: `CRITICAL (the emotional peak, expressed as a still fingertip)`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_OPEN`
- Simultaneous With: `The thread, read and unanswered, remaining on screen`
- After: `— (cut on the finger)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. The room falls away into soft indigo`
- Depth of Field: `Shallow — the finger and the thread sharp, the room soft behind`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Locked on 真白's face, lit from below, eyes moving over the thread list. Static.
- **`[0:07–0:15]`** — Cut to the screen: the thread opens — 小春's consultation, read and unanswered. A slow push in toward the message.
- **`[0:15–0:24]`** — Cut to the hand and the glass: her fingertip descends, contacts the glass above the thread, and stops. Hold. No further move.
- **`[0:24–0:30]`** — Locked macro on the stopped fingertip, the thread soft behind it. Cut on the finger.

---

# 11. MOTION

## Subject Motion

- 真白's body holds; only her hand moves — and it moves to stop
- The stop is absolute: not a slowing, not a hesitation. The fingertip descends, touches, and stays
- After the stop, nothing else moves at all
- ニジ, inside the screen, is still — watching, silent

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a thread opening. Nothing glitches, flickers, distorts, or behaves supernaturally
- The wall clock's second hand advances in discrete ticks, out of focus behind

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingertip — until the stop, which is instantaneous`
- Acceleration: `Gentle everywhere except the stop`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes. The only impact is a fingertip ceasing to move`

---

# 12. EMOTION

## Emotional Arc

- Facing the first name (the thread list, the addressee 小春)
- ↓ The weight of what was left unanswered (the month-old consultation)
- ↓ The body arriving before the decision (the stop)
- ↓ Indecision that does not resolve (the held fingertip, then cut)

## Emotional Events

- Event: `The first addressee — 小春` — Emotion: `Facing the beginning of 返す` — Intensity: `LOW` — Timing: `≈0:05`
- Event: `The month-old consultation, read and unanswered` — Emotion: `The weight of what was left behind` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:10`
- Event: `The fingertip touching and stopping` — Emotion: `Indecision — not shock, but being unable to decide. The reversal of S03's stop` — Intensity: `CRITICAL, expressed as stillness` — Timing: `≈0:16, held to 0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow is the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on; its light lying on the ceiling as a soft blue rectangle.
- **`[0:07–0:15]`** — As the thread opens, the screen's light catches her face from below, almost to silhouette.
- **`[0:15–0:24]`** — The screen's light catches the fingertip from below — the knuckle a thin bright line in the dark as it stops on the glass.
- **`[0:30]`** — Cut on the finger. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

> **No speech at all.** This segment is wordless. ニジ's last line is not repeated, not echoed, not voiced. The thread is read, not spoken. No narration, no voice-over.

## Sound Effects

- Deep quiet night room tone, almost nothing
- The wall clock's second hand, dry discrete ticks, faint throughout — growing louder in the held beats
- The soft friction of a fingertip on glass, once, at the moment of contact — then nothing

## Environment

- Deep quiet night room tone. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness, then withdraw. Music thins as the thread opens and is entirely gone by the moment the finger stops, leaving only room tone and the clock`

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

- ニジ is **present** — inside the screen only, 真白's own face one step younger, a rainbow afterimage, **fully opaque** — but this segment's subject is 真白's finger
- The first addressee is 小春 — shown as a name and a thread, **not as a face**
- The consultation is read and left unanswered for a month — 既読, not sent
- 真白's fingertip **touches the glass above the thread and stops**. It does not press, tap, type, or send
- End by cutting on the stopped finger, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 S35 レンジより）

- **No full-body transparency.** ニジ is opaque here — no translucent body, no see-through torso or face, no fading, no dissolving, no disappearing
- **No sending.** The message must not be sent, the send button must not be pressed, no reply must be typed. The sending belongs to episode 9
- **No face of the addressee.** 小春's face must not appear — she is a name and text only
- **No figure in the room, no other faces.** 真白 and ニジ are the only figures
- **No generic ghost.** ニジ is not a horror ghost — no ghostly glow, no spectral aura, no glowing eyes
- **No on-screen text beyond the ordinary UI.** Do not render the consultation's exact characters (per §0.5, this segment has no fixed on-screen text)
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- Holds over movement; when in doubt, do less
- The stopped finger held longer than is comfortable
- Silence over score at the stop

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- Music may be absent altogether
- ニジ's rainbow may drift slowly, blue to green to blue, at the edge of the frame

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear inside the screen only, fully opaque, but the subject is 真白's stopped finger (ledger S35 — 在); no full-body transparency, no sending, no face of the addressee. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M., with a figure inside her phone screen. Beats, deliberately uneven: [0:00–0:07] 真白 looks at the thread list, and her eyes find the first addressee — 小春; [0:07–0:15] she opens the thread — 小春's consultation, a long message, read and left unanswered for a month — and reads it again, once; [0:15–0:24] THE PEAK — her fingertip descends, makes contact with the glass above the thread, and STOPS, not pressing, not tapping, not sending, the stop of S03 reversed from shock into indecision; [0:24–0:30] hold on the stopped fingertip and cut on the finger. The stopped finger holds the largest share of the duration. Ends on the finger, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: inside the phone screen only — 真白's own face one step younger, longer lashes and slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — a rainbow afterimage, no shadow anywhere, fully opaque, watching silently at the edge of the frame; never standing in the room at human scale. The phone screen shows an ordinary Japanese messaging UI in cold blue-white — a thread list, then one open thread, a long consultation message read and unanswered, no face of the addressee. Night is deep indigo lit solely by the cold blue-white screen. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. 真白's body holds; only her hand moves, and it moves to stop. The stop is absolute: the fingertip descends, touches the glass, and stays — not a slowing, not a hesitation, not pressing, not tapping, not typing. After the stop, nothing else moves. ニジ, inside the screen, is still and silent. Ordinary weight and inertia; the phone has heft, the futon compresses. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder. Longish lens, shallow depth of field; the finger and the thread sharp, the room soft behind. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] locked on 真白's face, lit from below, eyes moving over the thread list, static. [0:07–0:15] cut to the screen as the thread opens — 小春's consultation, read and unanswered — with a slow push in toward the message. [0:15–0:24] cut to the hand and the glass; her fingertip descends, contacts the glass, and stops; hold, no further move. [0:24–0:30] locked macro on the stopped fingertip, the thread soft behind it; cut on the finger.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, faint throughout and growing louder in the held beats. The soft friction of a fingertip on glass, once, at the moment of contact — then nothing. No spoken words at all — no dialogue, no narration, no voice-over, no echo of the previous line. Music extremely sparse — a few sustained tones at most — thinning as the thread opens and entirely gone by the moment the finger stops, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no fully transparent figure, no translucent body, no see-through torso, no see-through face, no fading figure, no dissolving, no disappearing, no vanishing, no full-body transparency, no message being sent, no send button pressed, no reply being typed, no second person in the room, no full-body figure in the room, no figure stepping out of the phone, no ghostly glow, no spectral aura, no generic anime ghost girl, no spirit girl, no other faces, no other person's face, no face of the addressee, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep08-seg04-30s-01`
- Segment ID: `S35`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_08, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 8s / 9s / 6s. Stop = BEAT 3 at 9s (30%)`
- Camera Events: `4 events as listed in §10. One slow push in; all else static or held`
- Action Events: `ACT_SCAN → ACT_OPEN → ACT_STOP`
- Audio Events: `no dialogue ／ clock ticking throughout ／ music gone by the stop`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the finger`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The stop may not read.** A generated fingertip may keep moving, press, or tap instead of stopping. The instantaneous stop plus the long hold is the peak; if it does not read, lengthen the hold first.
- **The model may send the message.** The sending is episode 9's whole event. Verify frame by frame that nothing is pressed, typed, or sent.
- **小春's face may appear.** The addressee is a name and text only. If a face renders, remove it — this is a hard disclosure rule.
- **The model may put ニジ in the room or make her transparent.** ニジ is opaque and inside the screen, at the edge of the frame. The negative prompt front-loads both.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the stopped finger reads cleanly, consider holding the stop 1–2 seconds longer, taking the time from beat 1 — the indecision is the whole event.
