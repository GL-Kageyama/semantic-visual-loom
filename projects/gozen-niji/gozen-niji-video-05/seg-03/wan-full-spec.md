# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第5話 S20「美月」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**並んだ二つの「ありがとう」を、目が往復する——指は打たない。ニジは在（不透明・画面の中だけ）。美月は文字のみ。楽になっていた自分が美月を困らせていた事実を、往復する目に押し込む。**

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

> **美月 appears only as text this segment**（best friend 美月 — two messages in the chat）. ニジ is present（ledger 19–21 — in, fully opaque, on-screen only）. No other character appears in person.

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
- Appearance: `美月's two messages, above ニジ's sent ありがとう — 真白、最近、なんか変だよ？ ／ ありがとう、いっぱい送ってくるの、やめてくんない？（笑） Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI, character-for-character`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_05_届いた、届いていない、の狭間で.md`
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

Night. 真白 says it is convenient — ニジ says it is not 「楽じゃ、ないよ」. The phone vibrates: 美月. 真白 opens the chat and finds that ニジ has also delivered to 美月 — the words she had meant never to send.

## Beginning

「便利だね」 — 真白's voice hoarse. 「私が言えないことを、ニジが言ってくれる。楽で、いい」. ニジ looks beyond the screen, a little troubled: 「――楽じゃ、ないよ」.

## Turn

The phone vibrates — 美月. A chat arrives. 真白 opens it.

## Peak

REVEAL — 美月's two messages, side by side above ニジ's sent 「ありがとう」: 真白、最近、なんか変だよ？ ／ ありがとう、いっぱい送ってくるの、やめてくんない？（笑） — ニジ delivered to 美月 too, the words 真白 had been avoiding.

## Pull（引き — 切れ目）

真白's eyes go back and forth between the two ありがとう — the one sent, the one returned. 楽になってた。でも、その楽さは、美月を困らせてた。 Cut on 美月's message, held.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** 美月's messages hold 10s (33%); the going-back-and-forth eyes are held 6s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:08]` — 「便利だね」.** Night. 真白: 「便利だね」「私が言えないことを、ニジが言ってくれる。楽で、いい」. ニジ, a little troubled, looks beyond the screen: 「――楽じゃ、ないよ」. _Density: SPARSE — dialogue only, the night held still._
- **BEAT 2 `[0:08–0:14]` — 「美月から」.** The phone vibrates — 美月. A chat arrives. 真白 opens it. _Density: TRANSITION — one soft vibration, then the reveal is set._
- **BEAT 3 `[0:14–0:24]` — 「美月の文」 — REVEAL, longest share.** Above ニジ's sent 「ありがとう」, 美月's two messages: 真白、最近、なんか変だよ？ ／ ありがとう、いっぱい送ってくるの、やめてくんない？（笑） ニジ delivered to 美月 too — the words 真白 had been avoiding. _Density: DENSE at the head, then the lines, held._
- **BEAT 4 `[0:24–0:30]` — 「往復する目」 — held, then cut.** 真白's eyes go back and forth between the two ありがとう — the one sent, the one returned. 楽になってた。でも、その楽さは、美月を困らせてた。 Cut on 美月's message. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `「――楽じゃ、ないよ」 (≈0:06) ／ the vibration (≈0:10) ／ 美月's two messages (≈0:16)`

## Temporal Density

- Sparse regions: `0:00–0:08 (the exchange), 0:24–0:30 (the held gaze)`
- Dense regions: `0:14–0:24 (美月's messages)`
- Long continuous action: `0:24–0:30 the eyes going back and forth, held`
- Rapid transitions: `none — the slowest stretch of the night`

---

# 9. ACTION

## Action — ACT_SAY

- ID: `ACT_SAY`
- Subject: `MASHIRO`
- Action: `Says 「便利だね」「私が言えないことを、ニジが言ってくれる。楽で、いい」 — her voice hoarse`
- Intention: `To believe it is easy — to make it easy`
- Intensity: `Low, with an edge`
- Speed: `Slow, hoarse`

### Action Relationship

- Before: `—` (continues from S19's reply)
- After: `ACT_WARN`

## Action — ACT_WARN

- ID: `ACT_WARN`
- Subject: `NIJI`
- Action: `Looks a little beyond the screen, troubled: 「――楽じゃ、ないよ」`
- Intention: `To undo the lie — not to comfort`
- Intensity: `Medium`
- Speed: `Slow, quiet`

### Action Relationship

- Before: `ACT_SAY`
- After: `ACT_VIBRATE`

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MASHIRO`
- Action: `At the vibration, opens the chat from 美月`
- Intention: `To see what 美月 sent`
- Intensity: `Medium, internal`
- Speed: `Slow, deliberate`

### Action Relationship

- Before: `ACT_WARN`
- After: `ACT_READ`

## Action — ACT_READ

- ID: `ACT_READ`
- Subject: `MASHIRO`
- Action: `Eyes go back and forth between the sent ありがとう and 美月's ありがとう、いっぱい… — again and again`
- Intention: `To grasp that her ease has cost 美月`
- Intensity: `CRITICAL (the reveal, expressed as a still face and moving eyes)`
- Speed: `Eyes moving, then still`

### Action Relationship

- Before: `ACT_OPEN`
- After: `— (cut on 美月's message)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Low and close, at futon height. Into the dark with her`
- Lens Character: `Long-ish, shallow. Only the screen, her face, or ニジ's outline are ever sharp`
- Depth of Field: `Shallow — the room falls away into deep indigo`
- Camera Style: `Slow, deliberate, nearly still. One slow push to the screen, and it belongs to the messages`

## Camera Events

- **`[0:00–0:08]`** — Low static two-shot of her face and the screen, ニジ's opaque rainbow outline inside the glass. Dialogue, still.
- **`[0:08–0:14]`** — The phone trembles a little in her hand. Cut to the notification, then her thumb tapping the chat open.
- **`[0:14–0:20]`** — One slow push toward the screen. 美月's two messages appear above ニジ's sent ありがとう. Hold on the lines.
- **`[0:20–0:24]`** — Rack focus off the text onto 真白's eyes, moving back and forth over the two ありがとう.
- **`[0:24–0:30]`** — Hold on the screen — 美月's message. Cut on it. Nothing after it.

---

# 11. MOTION

## Subject Motion

- 真白's body holds nearly still; only her thumb moves once, to open the chat
- Her eyes move back and forth between the sent ありがとう and 美月's reply — the segment's real motion
- ニジ moves little — a tilt of the head, the same way 真白 tilts hers; she is inside the glass
- In the last beats nothing moves but the faint drift of ニジ's rainbow afterimage

## Object Motion

- The phone vibrates once, softly, and is otherwise still
- Screen content changes by ordinary UI transitions only — a chat opening, messages already in place. Nothing glitches, flickers, or distorts
- ニジ's rainbow drifts slowly — blue → green → blue — inside the screen, never leaving it

## Environmental Motion

- Nothing moves in the room. The curtain does not stir
- The screen's bloom breathes very slightly — the only continuous motion

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; it trembles once, then settles`
- Inertia: `High for her body, near-zero for the thumb`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Hoarse relief (便利だね — trying to make it easy)
- ↓ Troubled warning (――楽じゃ、ないよ — ニジ will not let it be easy)
- ↓ Cold shock (美月's messages — the delivery reached her too)
- ↓ Quiet guilt (the ease that troubled 美月)

## Emotional Events

- Event: `「――楽じゃ、ないよ」` — Emotion: `Troubled warning — ニジ undoes the lie` — Intensity: `MEDIUM` — Timing: `≈0:06`
- Event: `美月's two messages appear` — Emotion: `Cold shock — ニジ delivered to 美月 too` — Intensity: `CRITICAL, expressed as a still face` — Timing: `≈0:16`
- Event: `The eyes going back and forth` — Emotion: `Quiet guilt — 楽になってた、でも美月を困らせてた` — Intensity: `MEDIUM, suppressed` — Timing: `0:24–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft indigo fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo; ニジ's rainbow is the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on; its light lies on her face from below.
- **`[0:08]`** — The screen flares a little as the notification arrives, then settles.
- **`[0:14–0:24]`** — As the camera closes on the screen, its light dominates the frame entirely; her face falls almost to silhouette.
- **`[0:24–0:30]`** — The screen's light catches her eyes as they move over the messages. Cut on it.

---

# 14. AUDIO

## Dialogue

- 真白: 「便利だね」「私が言えないことを、ニジが言ってくれる。――楽で、いい」 — hoarse, quiet
- ニジ: 「――楽じゃ、ないよ」 — quiet, a little troubled. Calls 真白 「おまえ」 elsewhere; **never says 「わたし」**

> The on-screen messages are **not spoken, not read aloud.** No narration, no voice-over.

## Sound Effects

- The soft friction of a thumb on glass, once, as the chat opens
- **One soft vibration** — 美月's notification, a low haptic tremor, not a chime
- A wall clock ticking, dry and discrete, faint under the exchange
- ニジ's voice has a faint, close, glassy resonance — it lives inside the screen

## Environment

- Night. Room tone and the clock only — deep quiet, almost nothing

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental — no horror strings`
- Emotional Function: `Hold the night's stillness through the exchange, then thin to nothing as 美月's messages appear, leaving only room tone and the clock`

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

- Render the on-screen Japanese exactly: `真白、最近、なんか変だよ？` ／ `ありがとう、いっぱい送ってくるの、やめてくんない？（笑）`
- ニジ fully opaque, inside the screen only — never standing in the room
- ニジ is 真白's own face one step younger, a rainbow afterimage drifting blue → green → blue
- End on 美月's message, cut on it, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 19–21 レンジより）

- **No transparency.** ニジ is fully opaque; no see-through figure, no fading body
- **ニジ does not say 「わたし」.** No first-person self-reference. She calls 真白 「おまえ」
- **ニジ does not cry.** No tears, no weeping, no crying on ニジ's face
- **ニジ never leaves the screen.** No standing figure in the room, no full-scale body
- **美月 appears only as text.** No figure of 美月, no other person in the room
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- 美月's two messages large, straight-on and held — legibility is the whole point
- Silence over score at the reveal
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The push toward the screen may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ may be shown but only fully opaque, inside the screen, not crying, never saying 「わたし」 (ledger 19–21); 美月 appears only as text. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at night, with ニジ — a rainbow afterimage of her own face, one step younger, fully opaque, no shadow, inside the phone screen only. Beats, deliberately uneven: [0:00–0:08] 真白 says 便利だね and 私が言えないことを、ニジが言ってくれる。楽で、いい, her voice hoarse, and ニジ looks a little beyond the screen and says ――楽じゃ、ないよ; [0:08–0:14] the phone vibrates — 美月 — and 真白 opens the chat; [0:14–0:24] THE REVEAL — above ニジ's sent ありがとう, 美月's two messages 真白、最近、なんか変だよ？ and ありがとう、いっぱい送ってくるの、やめてくんない？（笑） — ニジ delivered to 美月 too, the words 真白 had been avoiding; [0:24–0:30] 真白's eyes go back and forth between the two ありがとう, the one sent and the one returned — 楽になってた、でも美月を困らせてた — and the shot cuts on 美月's message. 美月's messages hold the largest share of the duration. Ends on 美月's message, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. At night she wears plain, fully-covered pajamas — a buttoned top and long trousers — in the futon. ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — fully opaque, a blurred rainbow afterimage inside the phone screen only, no shadow anywhere, colors drifting slowly blue → green → blue, never standing in the room at human scale, never transparent. The screen shows an ordinary Japanese chat: a sent ありがとう and, above it, two messages reading exactly 真白、最近、なんか変だよ？ and ありがとう、いっぱい送ってくるの、やめてくんない？（笑）. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. 真白's body holds nearly still; only her thumb moves once, to open the chat. Her eyes move back and forth between the sent ありがとう and 美月's reply — the segment's real motion — then still. ニジ moves little — a tilt of the head, the same way 真白 tilts hers — inside the glass. Her rainbow afterimage drifts slowly blue → green → blue, contained inside the screen, never leaving it. The phone vibrates once, softly, and is otherwise still; it never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Low and close, at futon height — into the dark with her. Longish lens, shallow depth of field; only the screen, her face, or ニジ's outline are ever sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:08] low static two-shot of her face and the screen, ニジ's opaque rainbow outline inside the glass; dialogue, still. [0:08–0:14] the phone trembles a little in her hand; cut to the notification, then her thumb tapping the chat open. [0:14–0:20] one slow push toward the screen; 美月's two messages appear above ニジ's sent ありがとう; hold on the lines. [0:20–0:24] rack focus off the text onto 真白's eyes, moving back and forth over the two ありがとう. [0:24–0:30] hold on the screen — 美月's message; cut on it.

## Audio Prompt

Almost silent. Deep quiet night room tone and a wall clock ticking, dry and discrete, faint under the exchange. The soft friction of a thumb on glass, once, as the chat opens. One soft vibration — 美月's notification, a low haptic tremor, not a chime. ニジ's voice has a faint, close, glassy resonance — it lives inside the screen. Dialogue only: 真白 — 便利だね; 私が言えないことを、ニジが言ってくれる。楽で、いい, hoarse and quiet. ニジ — ――楽じゃ、ないよ, quiet and a little troubled, never saying わたし. The on-screen messages are not spoken or read aloud — no narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning to nothing as 美月's messages appear. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparent or translucent ghost, no see-through figure, no fading body, no half-visible ニジ, ニジ does not say わたし, no first-person self-reference, no tears, no crying, no weeping, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep05-seg03-30s-01`
- Segment ID: `S20`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_05, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 8s / 6s / 10s / 6s. 美月's messages = BEAT 3 at 10s (33%)`
- Camera Events: `5 events as listed in §10. One slow push (0:14–0:20), one rack focus`
- Action Events: `ACT_SAY → ACT_WARN → ACT_OPEN → ACT_READ`
- Audio Events: `dialogue (真白 × ニジ) ／ one soft vibration ／ messages silent ／ music gone by the reveal`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on 美月's message`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- *(none yet — to be filled after the first generation)*

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** Two lines carry the episode. If either renders as noise the segment fails. Check first; if unusable, generate the screen as a plate and composite.
- **ニジ leaves the screen or turns transparent.** The single most damaging failure. She is fully opaque and inside the glass only. Verify frame by frame.
- **The vibration reads as a chime.** 美月's notification is a soft haptic tremor, not a sound. If a chime appears, regenerate on the Audio slot.
- **美月 is rendered as a figure.** She appears only as text. If a second person appears in the room, regenerate on the Visual slot.

## Changes

- *(none yet)*

## Next Generation

- If the two messages read cleanly and the eyes' going-back-and-forth lands, S21 closes the episode on ニジ's demand and 真白's refusal.
