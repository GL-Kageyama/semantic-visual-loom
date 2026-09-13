# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第7話 S29「逃げた時間は、ひとつもなかった」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**名前に繋がった記録——また撫でる指が、フィードではなく「名前」を撫でる。いいねを押した時間、既読を付けた時間、返事を打っては消した時間、その全部に宛先の名前が付いていた。逃げた時間は、ひとつもなかった。ニジは画面の中に、不透明で在る（声はまだ S30）。**

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

> **ニジ appears this segment**（ledger 29–30 — in, opaque; not yet わたし）. No other character appears — 美月・小春・湊 do not appear.

---

# 4. ENVIRONMENT

## Location

- ID: `CLASSROOM`
- Name: `教室 (the darkened classroom, night)`
- Description: `The classroom at night after the festival eve — 真白 alone, the phone screen the only light, the list of deposited time open on the screen. The window outside is already dark`

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
- Appearance: `No message text this segment — only the ordinary list of screen-time records, each line a time attached to a name (美月, お母さん, 小春). Rendered as diegetic UI, not as evidence text; no captions, no subtitles`
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

真白 looks over the list and realizes every record is attached to a name. 逃げた時間は、ひとつもなかった。

## Beginning

The list is open (from S28). 真白's eyes move over it. Every single record has an addressee's name attached.

## Turn

The time 真白 spent on her phone in the night. All of it, time spent with someone, time toward someone. いいねを押した時間。既読を付けた時間。返事を打っては消した時間。——全部に、宛先の名前が付いてた。

## Peak

逃げた時間は、ひとつもなかった。スマホに逃げてた、と思ってた。無駄にしてた、と思ってた。でも、記録には全部、宛先があった。Her time had escaped nowhere. It was all time toward someone.

## Pull（引き — 切れ目）

窓の外はもう真っ暗。 On the desk, tomorrow's preparations lie spread out. 真白's finger strokes the screen — the names. 美月の名前。お母さんの名前。小春の名前。Cut on the finger stroking the names.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The name-connection holds 11s (37%); the realization is held 8s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「一覧」 — ESTABLISH.** The list is open; 真白's eyes move over it; every record has an addressee's name attached. _Density: SPARSE — quiet reading, no event._
- **BEAT 2 `[0:06–0:17]` — 「名前に繋がる」 — REVEAL, longest share.** The time 真白 spent on her phone in the night, all of it time toward someone — いいねを押した時間、既読を付けた時間、返事を打っては消した時間、全部に宛先の名前が付いてた。 _Density: DENSE at the head (the list → the names), then held._
- **BEAT 3 `[0:17–0:25]` — 「逃げた時間は」 — PEAK, held.** 逃げた時間は、ひとつもなかった。スマホに逃げてた、と思ってた、無駄にしてた、と思ってた、でも記録には全部、宛先があった。 _Density: SPARSE, internal — the event is a recognition._
- **BEAT 4 `[0:25–0:30]` — 「名前を撫でる」 — held, then cut.** 真白's finger strokes the screen — the names: 美月の名前、お母さんの名前、小春の名前。 Cut on the finger. _Density: HELD — then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the records connecting to names (≈0:09) ／ the realization 逃げた時間は、ひとつもなかった (≈0:19) ／ the finger stroking the names (≈0:27)`

## Temporal Density

- Sparse regions: `0:00–0:06 (reading the list), 0:17–0:25 (the realization)`
- Dense regions: `0:06–0:17 (the names)`
- Long continuous action: `0:25–0:30 the finger stroking the names`
- Rapid transitions: `none — a slow, held night`

---

# 9. ACTION

## Action — ACT_SCAN

- ID: `ACT_SCAN`
- Subject: `MASHIRO`
- Action: `Eyes move over the list, once, reading — each record a time, and a name attached`
- Intention: `To see what the opened list holds`
- Intensity: `Low`
- Speed: `Slow, and slowing`

### Action Relationship

- Before: `— (continues from S28's list)`
- After: `ACT_RECOGNIZE`

## Action — ACT_RECOGNIZE

- ID: `ACT_RECOGNIZE`
- Subject: `MASHIRO`
- Action: `Sees it — いいねを押した時間、既読を付けた時間、返事を打っては消した時間、全部に宛先の名前が付いている`
- Intention: `To understand what the records are`
- Intensity: `Medium, internal`
- Speed: `Still; only the eyes move`

### Action Relationship

- Before: `ACT_SCAN`
- After: `ACT_REALIZE`
- Causes: `ACT_REALIZE`

## Action — ACT_REALIZE

- ID: `ACT_REALIZE`
- Subject: `MASHIRO`
- Action: `The recognition lands — 逃げた時間は、ひとつもなかった。 Her time had never escaped; it was all time toward someone`
- Intention: `None — the body receives the understanding before the mind`
- Intensity: `CRITICAL (the realization, expressed as stillness)`
- Speed: `Zero, and held`

### Action Relationship

- Before: `ACT_RECOGNIZE`
- After: `ACT_STROKE_NAMES`

## Action — ACT_STROKE_NAMES

- ID: `ACT_STROKE_NAMES`
- Subject: `MASHIRO`
- Action: `Her finger strokes the screen again — this time the names: 美月の名前、お母さんの名前、小春の名前`
- Intention: `To touch the names — the same stroke, turned from the feed to the people`
- Intensity: `Medium, suppressed`
- Speed: `Slow, gentle — the same arc, on a new surface`

### Action Relationship

- Before: `ACT_REALIZE`
- After: `— (cut on the finger)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the dark classroom with her`
- Lens Character: `Long-ish, shallow. Only the screen or the finger are ever sharp`
- Depth of Field: `Very shallow — the classroom falls away into near-black`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Locked close on the list on the screen, her eyes reading over it. Optional: an imperceptibly slow push-in.
- **`[0:06–0:12]`** — One slow continuous dolly in on the list — the times, then the names attached to them. The piece's single sustained move, and it belongs to the reveal.
- **`[0:12–0:17]`** — Absolutely locked on the names, filling the frame. Static.
- **`[0:17–0:22]`** — Rack focus off the list onto her face, lit from below. The list goes soft; her still face becomes the subject.
- **`[0:22–0:26]`** — Hold on her face. No camera movement at all.
- **`[0:26–0:30]`** — A slow pull back to bring the list and her hand into frame together — the finger beginning to stroke the names. Cut on the finger.

---

# 11. MOTION

## Subject Motion

- Only her eyes and her finger move; the rest of her body holds
- The realization is stillness — moving, then not moving; the body arrives before the understanding
- The finger strokes the names in the same arc she once stroked the feed — gentle, unhurried

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a list scrolling under the finger. Nothing glitches, flickers, or distorts
- ニジ, inside the screen, is still — a rainbow afterimage holding her outline

## Environmental Motion

- The classroom is still and dark; nothing moves in it
- No wind, no moving shadows, no particles

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand`
- Inertia: `High for her body, near-zero for the finger`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet reading (the list, opened and held)
- ↓ Recognition (the records all pointing at someone)
- ↓ The realization landing (逃げた時間は、ひとつもなかった)
- ↓ A tender return (the finger stroking the names)

## Emotional Events

- Event: `The records connect to names` — Emotion: `Recognition — the time was all toward someone` — Intensity: `MEDIUM` — Timing: `≈0:09`
- Event: `逃げた時間は、ひとつもなかった` — Emotion: `The realization landing — not relief, a quiet correction of a long wrong` — Intensity: `CRITICAL — expressed only as stillness. No facial performance` — Timing: `≈0:19, held to 0:25`
- Event: `The finger strokes the names` — Emotion: `A tender return — the same stroke, turned toward the people` — Intensity: `MEDIUM, suppressed` — Timing: `0:26–0:30`

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
- **`[0:06–0:17]`** — As the camera closes on the list, its light dominates the frame; her face falls almost to silhouette. The evidence outshines the person.
- **`[0:17–0:25]`** — Rack focus to her face, lit from below, almost to silhouette.
- **`[0:26–0:30]`** — The screen's light catches the finger from below as it strokes the names. Cut on the finger.

---

# 14. AUDIO

## Dialogue

> **No speech.** This segment is wordless. The realization is not spoken, not whispered, not read aloud. ニジ is present but does not speak yet — her voice belongs to S30. No narration, no voice-over.

## Sound Effects

- The soft friction of a thumb on glass, close and continuous, through the whole segment — its rhythm the segment's pulse
- The near-silence of an emptied school at night

## Environment

- Deep quiet, almost nothing — the kind of silence in which a screen's light feels loud

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender. Never sinister, never sentimental — no horror strings, no swelling`
- Emotional Function: `Hold the room's stillness under the realization. It may thin toward the close, leaving only room tone and the thumb on glass`

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
- Show the records all pointing at someone — every time with a name attached
- Let the realization 逃げた時間は、ひとつもなかった land as stillness, held
- End on the finger stroking the names — 美月, お母さん, 小春 — cut on the finger

## MUST NOT（この1本の禁止・開示台帳 29–30 レンジより）

- **Do not make ニジ transparent.** No translucent apparition, no see-through figure, no fading ghost — she is opaque
- **Do not give ニジ the subject わたし.** She calls 真白 「おまえ」 and does not yet say わたし (her first わたし belongs to S31)
- **ニジ does not speak yet** — her first line in this episode is S30
- No 美月, no 小春, no 湊 as live figures — only 真白 and ニジ
- No on-screen subtitles or captions burned in (the list is diegetic UI, not evidence text)
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The stillness of the realization over any performed emotion
- The finger's stroke over any explicit statement
- Silence over score at the realization

## ALLOW

- Slight variation in the list's layout and the classroom furnishing
- The imperceptible push-in may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must be shown fully opaque inside the screen (ledger 29–30 — in, opaque); she does not yet say わたし; no other character. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a Japanese high-school girl alone in her darkened classroom at night. Beats, deliberately uneven: [0:00–0:06] her eyes read the list on the phone screen, each record a time with a name attached; [0:06–0:17] THE REVEAL — 真白が夜中にスマホをいじってた時間、その全部が誰かに向けた時間 — いいねを押した時間、既読を付けた時間、返事を打っては消した時間、全部に宛先の名前が付いてた, and the camera closes slowly until the names fill the frame; [0:17–0:25] THE PEAK — 逃げた時間は、ひとつもなかった。スマホに逃げてた、と思ってた、無駄にしてた、と思ってた、でも記録には全部、宛先があった, the realization landing as stillness; [0:25–0:30] her finger strokes the screen again — this time the names: 美月の名前、お母さんの名前、小春の名前 — and the shot cuts on the finger. ニジ is present inside the screen, fully opaque, no shadow, 真白's own face one step younger with the same shoulder-length dark hair and thin neck, a rainbow afterimage, silent. The name-connection holds the largest share. Ends on the finger, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. By day she wears a standard Japanese school uniform; here, after school, she is alone in the classroom in that uniform. A darkened classroom: the phone screen the only light, cold blue-white from below, her face nearly silhouetted, shadows deep and soft, no fill. On the screen an ordinary Japanese list of screen-time records, each line a time attached to a name. ニジ: inside the screen only, never at human scale in the room — 真白's own face one step younger (longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same head-tilt), a blurred rainbow afterimage that resolves into that outline, fully opaque, no shadow, colors drifting slowly blue → green → blue. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to the eyes and the finger; the body holds still. The realization is stillness — the eyes move, then stop. The finger strokes the names in the same gentle arc she once stroked the feed. ニジ inside the screen holds her outline, her rainbow colors drifting slowly. Ordinary weight and inertia: the phone has heft in her hand. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. Only the screen's bloom breathes faintly in the dark. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder — inside the dark classroom with her. Longish lens, very shallow depth of field; only the screen or the finger are ever sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked close on the list, her eyes reading over it, optionally an imperceptibly slow push-in. [0:06–0:12] one slow continuous dolly in on the list — the times, then the names attached to them. [0:12–0:17] absolutely locked on the names, static. [0:17–0:22] rack focus off the list onto her face lit from below. [0:22–0:26] hold on her face, no camera movement. [0:26–0:30] a slow pull back to bring the list and her hand into frame, the finger stroking the names; cut on the finger.

## Audio Prompt

Almost silent. Deep quiet night room tone — the near-silence of an emptied school. The close continuous friction of a thumb on glass, its rhythm the segment's pulse. No spoken words at all — the realization is not spoken, not whispered, not read aloud; ニジ is present but silent, her voice belongs to the next segment. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only room tone and the thumb on glass. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparency, no translucent apparition, no see-through figure, no fading ghost, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep07-seg03-30s-01`
- Segment ID: `S29`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_07, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 11s / 8s / 5s. Name-connection = BEAT 2 at 11s (37%)`
- Camera Events: `6 events as listed in §10. One sustained dolly (0:06–0:12)`
- Action Events: `ACT_SCAN → ACT_RECOGNIZE → ACT_REALIZE → ACT_STROKE_NAMES`
- Audio Events: `no dialogue ／ thumb-on-glass throughout ／ music thinning to nothing`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the finger`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **ニジ reads as a translucent ghost.** She must be fully opaque. If the model renders her see-through, strengthen the "no transparency" front-load and re-state her opacity in the Visual slot.
- **The realization may not land.** The whole turn is a quiet correction of a wrong. If the stillness does not read, lengthen the hold on her face.
- **The list may render as readable story text.** The names are ordinary UI, not evidence to read — they must stay soft and diegetic. If they draw focus, blur them and keep the finger as the subject.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the name-connection and the realization read, this segment is done; S30 opens with the finger stopping longest on one name and ニジ's first line of the episode.
