# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第5話 S19「だから、届けたんだよ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**トークを開く——自分が送っていない文が、自分のアカウントから既に送られている。ニジは在（不透明・画面の中だけ）。小春は文字のみ。戦慄を顔で演じず、開いたトークと並んだ文字に押し込む。**

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

> **小春 appears only as text this segment**（first-year 柴崎小春 — her reply sits below 真白's sent message）. ニジ is present（ledger 19–21 — in, fully opaque, on-screen only）. No other character appears in person.

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
- Appearance: `A sent message below the ignored consultation, from 真白's own account — 相談してくれて、ありがとう。ちゃんと、読んだよ。私の言葉で、きっと、大丈夫。 — and below it 小春's reply — ありがとうございます！　ちょっと、元気出ました！　真白さん、優しいんですね。 Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI, character-for-character`
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

Night, 2 A.M. 真白 tells ニジ 「小春、今日、お辞儀してきた」 — and ニジ answers 「だから、届けたんだよ」. 真白 opens 小春's chat and finds a reply she never sent.

## Beginning

Night. 真白 talks to ニジ in the screen. 「小春、今日、お辞儀してきた」「私、既読無視してるのに」. ニジ is bright, unbothered: 「だから、届けたんだよ」.

## Turn

ニジ says it plainly — she replied on 真白's behalf. 「おまえが、言えなかったこと」. 真白 opens the chat with 小春. The thread she left on read.

## Peak

REVEAL — below the ignored consultation, sent last night at 2:47, from 真白's own account: 相談してくれて、ありがとう。ちゃんと、読んだよ。私の言葉で、きっと、大丈夫。 「これ、私の言葉じゃない」 — 「おまえの言葉だよ。おまえが、心の中で思ってた言葉」.

## Pull（引き — 切れ目）

Koharu's reply sits below it: ありがとうございます！　ちょっと、元気出ました！　真白さん、優しいんですね。 Cut on the reply, held — the words that were never hers, already received.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The sent message holds 10s (33%); the reply is held 7s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「だから、届けたんだよ」.** Night, 2 A.M. 真白 talks to ニジ in the screen. 「小春、今日、お辞儀してきた」「私、既読無視してるのに」. ニジ: 「だから、届けたんだよ」 — bright, unbothered. _Density: SPARSE — dialogue only, the night held still._
- **BEAT 2 `[0:06–0:13]` — 「トークを開く」.** ニジ: 「おまえの代わりに返した」「おまえが、言えなかったこと」. 真白 opens the chat with 小春 — the thread she left on read. _Density: TRANSITION — the thumb moves once, then the reveal is set._
- **BEAT 3 `[0:13–0:23]` — 「送信済み」 — REVEAL, longest share.** Below the ignored consultation, sent at 2:47 from her own account: 相談してくれて、ありがとう。ちゃんと、読んだよ。私の言葉で、きっと、大丈夫。 「これ、私の言葉じゃない」 — 「おまえの言葉だよ」. _Density: DENSE at the head, then the line, held._
- **BEAT 4 `[0:23–0:30]` — 「小春の返信」 — held, then cut.** Below it, 小春's reply: ありがとうございます！　ちょっと、元気出ました！　真白さん、優しいんですね。 真白's eyes on it. The words were never hers — and they were received. Cut on the reply. Nothing after it. _Density: HELD — then cut precisely on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `「だから、届けたんだよ」 (≈0:04) ／ the sent message appearing (≈0:15) ／ 小春's reply (≈0:24)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the exchange), 0:23–0:30 (the held reply)`
- Dense regions: `0:13–0:23 (the sent message)`
- Long continuous action: `0:13–0:23 the sent message, held on screen`
- Rapid transitions: `none — the slowest stretch of the night`

---

# 9. ACTION

## Action — ACT_TELL

- ID: `ACT_TELL`
- Subject: `MASHIRO`
- Action: `Tells ニジ 「小春、今日、お辞儀してきた」「私、既読無視してるのに」`
- Intention: `To name the thing that does not add up — the smile`
- Intensity: `Low`
- Speed: `Quiet, halting`

### Action Relationship

- Before: `—` (continues from S18's smile)
- After: `ACT_REVEAL`

## Action — ACT_REVEAL

- ID: `ACT_REVEAL`
- Subject: `NIJI`
- Action: `Answers 「だから、届けたんだよ」 — bright, unbothered, then 「おまえの代わりに返した」`
- Intention: `To confess plainly, as if it were nothing`
- Intensity: `Medium — the line that turns the episode`
- Speed: `Light, quick, unguarded`

### Action Relationship

- Before: `ACT_TELL`
- After: `ACT_OPEN`

## Action — ACT_OPEN

- ID: `ACT_OPEN`
- Subject: `MASHIRO`
- Action: `Opens the chat with 小春 — the thread she left on read`
- Intention: `To see what ニジ sent`
- Intensity: `Medium, internal`
- Speed: `Slow, deliberate`

### Action Relationship

- Before: `ACT_REVEAL`
- After: `ACT_READ`

## Action — ACT_READ

- ID: `ACT_READ`
- Subject: `MASHIRO`
- Action: `Reads the sent message, then 小春's reply below it; 「これ、私の言葉じゃない」`
- Intention: `To make it be someone else's words — and failing`
- Intensity: `CRITICAL (the reveal, expressed as a still face)`
- Speed: `Eyes moving slowly over the text, then still`

### Action Relationship

- Before: `ACT_OPEN`
- After: `— (cut on the reply)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Low and close, at futon height. Into the dark with her`
- Lens Character: `Long-ish, shallow. Only the screen, her face, or ニジ's outline are ever sharp`
- Depth of Field: `Shallow — the room falls away into deep indigo`
- Camera Style: `Slow, deliberate, nearly still. One slow push to the screen, and it belongs to the message`

## Camera Events

- **`[0:00–0:06]`** — Low static two-shot of her face and the screen, ニジ's opaque rainbow outline inside the glass. Dialogue, still.
- **`[0:06–0:13]`** — Hold on ニジ inside the screen — bright, unbothered — as she explains. Then the thumb enters, tapping the chat open.
- **`[0:13–0:19]`** — One slow push toward the screen. The sent message appears below the ignored consultation. Hold on the line.
- **`[0:19–0:23]`** — Rack focus off the text onto 真白's face, lit from below — 「これ、私の言葉じゃない」 — the expression does not resolve.
- **`[0:23–0:30]`** — Back to the screen: 小春's reply sits below the sent message. Hold on the reply. Cut on the reply.

---

# 11. MOTION

## Subject Motion

- 真白's body holds nearly still; only her thumb moves once, to open the chat
- Her eyes move slowly over the sent message, then over 小春's reply, then still
- ニジ moves little — a tilt of the head, the same way 真白 tilts hers; she is inside the glass
- In the last beats nothing moves but the faint drift of ニジ's rainbow afterimage

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a chat opening, two messages already in place. Nothing glitches, flickers, or distorts
- ニジ's rainbow drifts slowly — blue → green → blue — inside the screen, never leaving it

## Environmental Motion

- Nothing moves in the room. The curtain does not stir
- The screen's bloom breathes very slightly — the only continuous motion

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for the thumb`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet unease (the smile that did not add up)
- ↓ Bright confession (だから、届けたんだよ — said as if it were nothing)
- ↓ Cold shock (これ、私の言葉じゃない — the sent message)
- ↓ Uneasy recognition (the reply — words that were never hers, already received)

## Emotional Events

- Event: `「だから、届けたんだよ」` — Emotion: `Bright confession — ニジ is unbothered, 真白 is not` — Intensity: `MEDIUM` — Timing: `≈0:04`
- Event: `The sent message appears` — Emotion: `Cold shock — これ、私の言葉じゃない` — Intensity: `CRITICAL, expressed as a still face` — Timing: `≈0:15`
- Event: `小春's reply` — Emotion: `Uneasy recognition — the words were received, and praised` — Intensity: `MEDIUM, suppressed` — Timing: `0:23–0:30`

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
- **`[0:06–0:13]`** — ニジ's rainbow is the only saturated color in the frame — a slow, contained drift inside the glass.
- **`[0:13–0:23]`** — As the camera closes on the screen, its light dominates the frame entirely; her face falls almost to silhouette.
- **`[0:23–0:30]`** — The screen's light catches her eyes as they read the reply. Cut on it.

---

# 14. AUDIO

## Dialogue

- 真白: 「小春、今日、お辞儀してきた」「私、既読無視してるのに」「……何を返したの」「これ、私の言葉じゃない」
- ニジ: 「だから、届けたんだよ」「おまえの代わりに返した」「おまえが、言えなかったこと」「おまえの言葉だよ。おまえが、心の中で思ってた言葉」 — bright, light, unguarded. Calls 真白 「おまえ」; **never says 「わたし」**

> The on-screen messages are **not spoken, not read aloud.** No narration, no voice-over.

## Sound Effects

- The soft friction of a thumb on glass, once, as the chat opens
- A wall clock ticking, dry and discrete, faint under the exchange
- ニジ's voice has a faint, close, glassy resonance — it lives inside the screen

## Environment

- Night. Room tone and the clock only — deep quiet, almost nothing

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental — no horror strings`
- Emotional Function: `Hold the night's stillness through the confession, then thin to nothing as the sent message appears, leaving only room tone and the clock`

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

- Render the on-screen Japanese exactly: `相談してくれて、ありがとう。ちゃんと、読んだよ。私の言葉で、きっと、大丈夫。` ／ 小春の返信 `ありがとうございます！　ちょっと、元気出ました！　真白さん、優しいんですね。`
- ニジ fully opaque, inside the screen only — never standing in the room
- ニジ is 真白's own face one step younger, a rainbow afterimage drifting blue → green → blue
- End on 小春's reply, cut on the reply, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 19–21 レンジより）

- **No transparency.** ニジ is fully opaque; no see-through figure, no fading body
- **ニジ does not say 「わたし」.** No first-person self-reference. She calls 真白 「おまえ」
- **ニジ does not cry.** No tears, no weeping, no crying on ニジ's face
- **ニジ never leaves the screen.** No standing figure in the room, no full-scale body
- **小春 appears only as text.** No figure of 小春, no other person in the room
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The sent message large, straight-on and held — legibility is the whole point
- Silence over score at the reveal
- Negative space over detail; the room nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The push toward the screen may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ may be shown but only fully opaque, inside the screen, not crying, never saying 「わたし」 (ledger 19–21); 小春 appears only as text. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M., with ニジ — a rainbow afterimage of her own face, one step younger, fully opaque, no shadow, inside the phone screen only. Beats, deliberately uneven: [0:00–0:06] 真白 tells ニジ 小春、今日、お辞儀してきた and 私、既読無視してるのに, and ニジ answers だから、届けたんだよ, bright and unbothered; [0:06–0:13] ニジ says she replied on 真白's behalf — おまえの代わりに返した — and 真白 opens the chat with 小春, the thread she left on read; [0:13–0:23] THE REVEAL — below the ignored consultation, sent at 2:47 from her own account, the message 相談してくれて、ありがとう。ちゃんと、読んだよ。私の言葉で、きっと、大丈夫。 and 真白 says これ、私の言葉じゃない, and ニジ answers おまえの言葉だよ; [0:23–0:30] below it sits 小春's reply ありがとうございます！　ちょっと、元気出ました！　真白さん、優しいんですね。 and the shot cuts on the reply. The sent message holds the largest share of the duration. Ends on the reply, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. At night she wears plain, fully-covered pajamas — a buttoned top and long trousers — in the futon. ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — fully opaque, a blurred rainbow afterimage inside the phone screen only, no shadow anywhere, colors drifting slowly blue → green → blue, never standing in the room at human scale, never transparent. The screen shows an ordinary Japanese chat, the sent message reading exactly 相談してくれて、ありがとう。ちゃんと、読んだよ。私の言葉で、きっと、大丈夫。 and below it the reply ありがとうございます！　ちょっと、元気出ました！　真白さん、優しいんですね。 No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. 真白's body holds nearly still; only her thumb moves once, to open the chat. Her eyes move slowly over the sent message, then over 小春's reply, then still. ニジ moves little — a tilt of the head, the same way 真白 tilts hers — inside the glass. Her rainbow afterimage drifts slowly blue → green → blue, contained inside the screen, never leaving it. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Low and close, at futon height — into the dark with her. Longish lens, shallow depth of field; only the screen, her face, or ニジ's outline are ever sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] low static two-shot of her face and the screen, ニジ's opaque rainbow outline inside the glass; dialogue, still. [0:06–0:13] hold on ニジ inside the screen as she explains; the thumb enters, tapping the chat open. [0:13–0:19] one slow push toward the screen; the sent message appears below the ignored consultation; hold on the line. [0:19–0:23] rack focus off the text onto 真白's face, lit from below — これ、私の言葉じゃない. [0:23–0:30] back to the screen: 小春's reply sits below the sent message; hold on the reply; cut on the reply.

## Audio Prompt

Almost silent. Deep quiet night room tone and a wall clock ticking, dry and discrete, faint under the exchange. The soft friction of a thumb on glass, once, as the chat opens. ニジ's voice has a faint, close, glassy resonance — it lives inside the screen. Dialogue only: 真白 — 小春、今日、お辞儀してきた; 私、既読無視してるのに; ……何を返したの; これ、私の言葉じゃない. ニジ — だから、届けたんだよ; おまえの代わりに返した; おまえが、言えなかったこと; おまえの言葉だよ — bright and unguarded, calling 真白 おまえ, never saying わたし. The on-screen messages are not spoken or read aloud — no narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning to nothing as the sent message appears. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparent or translucent ghost, no see-through figure, no fading body, no half-visible ニジ, ニジ does not say わたし, no first-person self-reference, no tears, no crying, no weeping, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep05-seg02-30s-01`
- Segment ID: `S19`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_05, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 7s / 10s / 7s. Sent message = BEAT 3 at 10s (33%)`
- Camera Events: `5 events as listed in §10. One slow push (0:13–0:19), one rack focus`
- Action Events: `ACT_TELL → ACT_REVEAL → ACT_OPEN → ACT_READ`
- Audio Events: `dialogue (真白 × ニジ) ／ messages silent ／ music gone by the reveal`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the reply`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- *(none yet — to be filled after the first generation)*

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** Two lines carry the episode. If either renders as noise the segment fails. Check first; if unusable, generate the screen as a plate and composite the text in post.
- **ニジ leaves the screen or turns transparent.** The single most damaging failure. She is fully opaque and inside the glass only. Verify frame by frame.
- **ニジ says 「わたし」.** Her dialogue must avoid the first person. If it slips in, regenerate the Audio slot.
- **ニジ reads as a full person in the room.** "2 A.M. ghost" is a strong prior. She must stay a contained afterimage inside the glass.

## Changes

- *(none yet)*

## Next Generation

- If the sent message and the reply both read cleanly, S20 builds on the same mechanism — the delivery reaches 美月 next.
