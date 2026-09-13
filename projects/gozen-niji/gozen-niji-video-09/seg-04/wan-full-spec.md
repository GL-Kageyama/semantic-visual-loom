# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第9話 S39「既読が付いた」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**開いては閉じる——既読を待つ反復。昼の「岸」の光の中で待つ。ニジは在・薄い（この1本から輪郭がはっきり薄くなる・画面の中だけ）。小春は文字のみ。画面文字は小春の返信二行 `真白さん、ありがとうございます。 ／ あのときのお礼、言えてなかったんで。――嬉しいです。`。感情はすべて、既読と「嬉しいです」に押し込む。**

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

> **ニジ appears this segment**（ledger 36–40 — 在・薄い; the outline thins clearly from 39–40）. 小春 appears only as text — never as a person, face, or figure.

---

# 4. ENVIRONMENT

## Location

- ID: `SCHOOL_DESK`
- Name: `学校の昼 (a desk at school, lunch)`
- Description: `Pale, muted, slightly overexposed daylight at a desk — the daytime "shore". No students are visible; the school exists only as a faint distant murmur beyond the frame. The phone in her hands`

## Environmental Behavior

- Wind: `none — nothing stirs`
- Particles: `none — pale, even daylight, still and muted; no dust motes, no floating lights, no VFX`
- Background Motion: `almost none — no visible movement; at most a faint distant murmur of a school, far off`

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
- Appearance: `小春's reply, two incoming bubbles, character-for-character: 真白さん、ありがとうございます。 ／ あのときのお礼、言えてなかったんで。――嬉しいです。 Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
- Continuity Importance: `HIGH`

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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_09_届かなかった言葉を、いま.md`
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

At school, at lunch, 真白 opens and closes the phone, waiting. The read receipt comes. Then 小春's reply — 真白さん、ありがとうございます。 ／ あのときのお礼、言えてなかったんで。――嬉しいです。 — and it lands: 届いた。

## Beginning

The phone in her hands in pale daylight. She opens it, closes it, opens it again — the waiting. The sent message sits there, still unread.

## Turn

既読. The read receipt appears on her message. 真白 holds her breath. The typing indicator — three dots — appears and vanishes.

## Peak

小春's reply arrives: 真白さん、ありがとうございます。 ／ あのときのお礼、言えてなかったんで。――嬉しいです。 The camera closes until the line is the frame.

## Pull（引き — 切れ目）

届いた。 She reads 嬉しいです over and over. Cut on the reply. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The reply holds 11s (37%); the read receipt is held 9s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:05]` — 「開いては閉じる」.** Pale daylight. The phone in her hands. She opens it, closes it, opens it again — the waiting. The sent message still unread. _Density: SPARSE — a repeated small gesture, no event._
- **BEAT 2 `[0:05–0:14]` — 「既読」 — the turn.** The read receipt appears on her message. 真白 holds her breath. The typing indicator — three dots — appears and vanishes. _Density: DENSE at the head (the read receipt), then held._
- **BEAT 3 `[0:14–0:25]` — 「返信」 — PEAK, longest share.** 小春's reply arrives, two bubbles: 真白さん、ありがとうございます。 あのときのお礼、言えてなかったんで。――嬉しいです。 A slow dolly in until the line fills the frame. _Density: DENSE at the head (the reply), then the line, held._
- **BEAT 4 `[0:25–0:30]` — 「届いた」.** She reads 嬉しいです over and over, word by word. 届いた. Cut on the reply. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the read receipt (≈0:08) ／ the typing indicator (≈0:11) ／ 小春's reply (≈0:16) ／ 届いた (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:05 (opening and closing), 0:25–0:30 (reading again)`
- Dense regions: `0:05–0:14 (the read receipt), 0:14–0:25 (the reply)`
- Long continuous action: `0:14–0:25 the reply, held and read`
- Rapid transitions: `none — a held, quiet segment in daylight`

---

# 9. ACTION

## Action — ACT_OPENCLOSE

- ID: `ACT_OPENCLOSE`
- Subject: `MASHIRO`
- Action: `Opens the phone, closes it, opens it again — the waiting gesture`
- Intention: `To see if 小春 has read it`
- Intensity: `Low, restless`
- Speed: `Quick, repeated, small`

### Action Relationship

- Before: `—` (continues from S38's send)
- After: `ACT_READRECEIPT`

## Action — ACT_READRECEIPT

- ID: `ACT_READRECEIPT`
- Subject: `MASHIRO`
- Action: `The read receipt appears; she holds her breath`
- Intention: `To confirm — read. 読まれた`
- Intensity: `CRITICAL, expressed as a held breath`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_OPENCLOSE`
- After: `ACT_TYPING`
- Causes: `ACT_TYPING`

## Action — ACT_TYPING

- ID: `ACT_TYPING`
- Subject: `MASHIRO` (observed)
- Action: `The typing indicator — three dots — appears and vanishes on 小春's side`
- Intention: `None — she only watches`
- Intensity: `Medium, suspended`
- Speed: `A brief flicker, then gone`

### Action Relationship

- Before: `ACT_READRECEIPT`
- After: `ACT_REPLY`

## Action — ACT_REPLY

- ID: `ACT_REPLY`
- Subject: `MASHIRO`
- Action: `小春's reply arrives; she reads it over and over, word by word`
- Intention: `To make it real — 届いた`
- Intensity: `CRITICAL, entirely internal`
- Speed: `Very slow, and slowing`

### Action Relationship

- Before: `ACT_TYPING`
- After: `— (cut on the reply)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, at desk level. Over the phone in her hands`
- Lens Character: `Long-ish, shallow. Only the screen or her face is ever sharp`
- Depth of Field: `Shallow — the pale school background falls away softly`
- Camera Style: `Slow, deliberate, nearly still. One slow push to the reply, and it belongs to the reply`

## Camera Events

- **`[0:00–0:05]`** — Close on her hands and the phone in pale daylight. She opens it, closes it, opens it. The sent message, still unread.
- **`[0:05–0:14]`** — A slight tilt down to the screen. The read receipt appears on her message; then the typing indicator — three dots — flickers and goes.
- **`[0:14–0:25]`** — One slow continuous dolly in on 小春's reply — 真白さん、ありがとうございます。 あのときのお礼、言えてなかったんで。――嬉しいです。 — until the line fills the frame. The piece's single sustained move.
- **`[0:25–0:30]`** — Hold on the reply, static. Her eyes move over 嬉しいです, again and again. Cut on the reply.

---

# 11. MOTION

## Subject Motion

- Her hands carry the opening and closing — small, repeated, restless
- At the read receipt, she goes absolutely still, holding her breath
- Then only her eyes move, reading 嬉しいです over and over
- Nothing else in her body moves

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — the read receipt appearing, the typing indicator flickering, the reply arriving. Nothing glitches or distorts
- ニジ's rainbow afterimage drifts slowly blue → green → blue, inside the screen, thinner than before

## Environmental Motion

- Pale daylight, even and still. A faint, distant murmur of a school beyond, no visible movement
- Nothing else moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hands`
- Inertia: `High for her body; her hands are quick only in the opening and closing`
- Acceleration: `Gentle; the opening and closing are small and soft`
- Fluidity: `Limited-animation — small repeated gestures, then holds`
- Impact: `None. The only event is a reply arriving`

---

# 12. EMOTION

## Emotional Arc

- Restless waiting (opening and closing the phone)
- ↓ Suspension (the read receipt; the held breath)
- ↓ Arrival (小春's reply — 嬉しいです)
- ↓ The thing landing (届いた — reading it again and again)

## Emotional Events

- Event: `The read receipt appears` — Emotion: `Suspension — 読まれた` — Intensity: `CRITICAL, expressed as a held breath` — Timing: `≈0:08`
- Event: `小春's reply arrives` — Emotion: `Arrival — 嬉しいです, returned` — Intensity: `CRITICAL, internal` — Timing: `≈0:16`
- Event: `She reads 嬉しいです over and over` — Emotion: `The thing landing — 届いた` — Intensity: `HIGH, suppressed` — Timing: `0:25–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `Pale, flat, slightly overexposed daylight — the day, the "shore". Muted and soft`
- Fill Light: `Even. Daylight fills softly; no hard shadows`
- Rim Light: `A faint pale edge, soft, from the window side`
- Ambient Light: `The pale muted tone of a school interior, slightly washed out`
- Color Temperature: `≈5500K pale day, muted and low-saturation; the screen's blue-white text is the one bright value`

## Lighting Events

- **`[0:00]`** — Pale, even daylight. The screen reads as a bright rectangle, not a light source — it does not illuminate her face.
- **`[0:05–0:14]`** — The screen's text catches the eye as the read receipt and the typing indicator change — small bright changes in a pale frame.
- **`[0:14–0:25]`** — As the camera closes on the reply, the pale day falls away and the screen's blue-white text becomes the whole frame.
- **`[0:25–0:30]`** — Unchanged. Cut on the reply.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. 小春's reply is not read aloud, not whispered, not narrated. No narration, no voice-over.

## Sound Effects

- The soft, small sounds of the phone being opened and closed — faint taps, cloth
- A single held breath, released at the read receipt
- Faint, distant school ambience — the murmur of a lunch break, far away, outside the frame

## Environment

- Daytime, school. The hush of a lunch break, very far off. Nothing in the room with her

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, then quietly released. Never sinister, never sentimental`
- Emotional Function: `Hold the pale stillness under the waiting, then thin to nothing as the reply arrives, leaving only the distant lunch murmur`

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

- Render the on-screen Japanese exactly: `真白さん、ありがとうございます。 ／ あのときのお礼、言えてなかったんで。――嬉しいです。`
- ニジ present, **clearly thin** — her outline distinctly thinner and semi-transparent, but never gone
- The read receipt appears; then the typing indicator (three dots) appears and vanishes
- 小春's reply arrives as two incoming bubbles
- End by cutting on the reply, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 36–40 レンジより）

- **No full disappearance.** ニジ thins, but never vanishes, dissolves, or fades out
- ニジ stays inside the screen; she never stands in the room at human scale
- 小春 appears only as text — never as a person, face, or figure
- No other person, crowd, or silhouette — no students visible in the school
- No voice for the reply — it is not read aloud, whispered, or narrated

## PREFER

- The reply legible, straight-on and held
- Silence over score at the reply
- The pale day kept muted and low-saturation

## ALLOW

- Slight variation in the school background (a desk, a window) — as long as no person is visible
- The dolly to the reply may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ is present and clearly thin — the outline thins but never fully disappears (ledger 36–40); 小春 appears only as text, and no students are visible. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school girl at a desk in pale, muted daylight — the daytime "shore". ニジ is present inside the screen, now clearly thin. Beats, deliberately uneven: [0:00–0:05] the phone in her hands, she opens it, closes it, opens it again — the waiting — the sent message still unread; [0:05–0:14] THE READ RECEIPT — it appears on her message, she holds her breath, and the typing indicator, three dots, appears and vanishes; [0:14–0:25] THE REPLY — 小春's reply arrives as two incoming bubbles, 真白さん、ありがとうございます。 and あのときのお礼、言えてなかったんで。――嬉しいです。 and the camera closes slowly until the line fills the frame; [0:25–0:30] she reads 嬉しいです over and over, word by word — 届いた — and the shot cuts on the reply. The reply holds the largest share of the duration. Ends on the reply, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the air, muted low-saturation palette, simple uncluttered setting, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. This segment is daytime — pale, slightly overexposed, equally muted daylight at a desk; the screen is a bright rectangle, not a light source. ニジ, inside the screen only, is 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same tilt of the head — a blurred rainbow afterimage resolved into that outline, colors drifting slowly blue → green → blue, no shadow anywhere, now clearly thin, her outline distinctly thinner and semi-transparent. The screen shows an ordinary Japanese UI in cold blue-white, with two incoming message bubbles from 小春 reading exactly 真白さん、ありがとうございます。 and あのときのお礼、言えてなかったんで。――嬉しいです。 No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her hands carry the opening and closing of the phone — small, repeated, restless — then go still. At the read receipt she holds absolutely still, only her eyes moving afterward, reading the reply again and again. ニジ's rainbow afterimage drifts slowly blue → green → blue, inside the screen, thinner than before. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions — the read receipt appearing, the typing indicator flickering, the reply arriving. No wind, no visible background movement. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, at desk level, over the phone in her hands. Longish lens, shallow depth of field; only the screen or her face is ever sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:05] close on her hands and the phone in pale daylight, opening and closing. [0:05–0:14] a slight tilt down to the screen as the read receipt appears, then the typing indicator flickers and goes. [0:14–0:25] one slow continuous dolly in on 小春's reply — 真白さん、ありがとうございます。 あのときのお礼、言えてなかったんで。――嬉しいです。 — until the line fills the frame. [0:25–0:30] hold on the reply, static, her eyes moving over 嬉しいです; cut on the reply.

## Audio Prompt

Almost silent. Pale daytime hush, and a very faint, distant murmur of a school lunch break, far outside the frame. The soft, small sounds of the phone being opened and closed — faint taps, cloth. One held breath, released at the read receipt. No spoken words at all — the reply is not read aloud, not whispered, not narrated. No voice-over. Music extremely sparse — a few sustained tones at most — thinning to nothing as the reply arrives, leaving only the distant lunch murmur. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no full disappearance, no complete vanishing, no dissolving into nothing, no fading out to invisibility, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep09-seg04-30s-01`
- Segment ID: `S39`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_09, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 5s / 9s / 11s / 5s. Reply = BEAT 3 at 11s (37%)`
- Camera Events: `4 events as listed in §10. One sustained dolly (0:14–0:25)`
- Action Events: `ACT_OPENCLOSE → ACT_READRECEIPT → ACT_TYPING → ACT_REPLY`
- Audio Events: `no dialogue ／ soft phone handling ／ one held breath ／ distant lunch murmur`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the reply`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ may vanish.** This is the first segment where she thins. She must read as clearly thin, but never disappear. If she vanishes, regenerate and hold her at semi-transparent.
- **Japanese text rendering.** Two bubbles carry the whole arrival. If they render as noise, generate the screen as a plate and composite.
- **The model may add a crowd.** 小春 is text-only; no students may be visible. If faces appear, it breaks the ledger.
- **The reply may read aloud.** It must stay silent — text only.

## Changes

- _(none yet)_

## Next Generation

- If the thinning reads clearly, S40 (返すと、薄くなる) is where the outline thins decisively as the record is returned.
