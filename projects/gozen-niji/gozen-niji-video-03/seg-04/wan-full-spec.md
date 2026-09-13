# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第3話 S13「返してくれたら帰れる」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「返してくれたら帰れる」——消滅でなく帰還という言葉。ニジは真白の毎日（既読を付けたまま、返事を打っては消す）を知っている。手を振ると虹色がゆっくり消え、最後に一色残って、それも消える——暗い画面に残るのは自分の顔。**

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

> **ニジ appears this segment**（ledger 11–13 — present, fully opaque, inside the screen only）. No other character appears this segment.

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

- Type: `none`
- Appearance: `No message text this segment — no UI, no bubbles, no notification. The screen carries only ニジ's face until her rainbow fades, leaving 真白's own reflection in the dark glass`
- Narrative Importance: `HIGH`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_03_午前二時の幽霊の名前.md`
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

真白 asks the thing she most wanted to know — 「どうしたら、消えるの。」 ニジ corrects her: not disappear, but 「返してくれたら、帰れるんだよ。」 She knows 真白 cannot do it yet — 「だって、おまえ、いつも、返してないじゃん。」 Then she waves, and the rainbow fades until 真白's own face is reflected in the dark screen.

## Beginning

Continuing from the naming. 真白 holds the phone, eyes on ニジ in the screen. The question she has been carrying since the first moment forms: 「どうしたら、消えるの。」

## Turn

ニジ tilts her head, faintly troubled, and looks beyond the screen. 「消える、じゃなくて、――返してくれたら、帰れるんだよ。」 真白: 「返す？ 何を。」 ニジ: 「おまえが預けた時間。宛先に、返すの。」

## Peak

ニジ smiles, but somehow differently than before — the rainbow in the screen flickers, just slightly. 「でも、おまえ、まだ、返せないんでしょ。」 真白: 「……なぜ、分かるの。」 ニジ: 「だって、おまえ、いつも、返してないじゃん。」 真白 has nothing to say.

## Pull（引き — 切れ目）

「じゃあね。また、明日。」 ニジ waves. The rainbow fades slowly — one color left, then gone. 真白 watches the dark screen, and finds only her own face reflected in it. 明日も、来るのかな。 Cut on the reflection.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The condition 「返してくれたら帰れる」 holds 8s (27%); the goodbye-and-fade holds 7s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:08]` — 「どうしたら、消えるの」 — the question.** 真白: どうしたら、消えるの。 ニジ, faintly troubled: 消える、じゃなくて、――返してくれたら、帰れるんだよ。 _Density: DENSE — the condition, stated._
- **BEAT 2 `[0:08–0:15]` — 「返す？ 何を」 — the exchange.** 真白: 返す？ 何を。 ニジ: おまえが預けた時間。宛先に、返すの。 The rainbow in the screen flickers, just slightly. _Density: DENSE — the 宛先, planted for the episodes to come._
- **BEAT 3 `[0:15–0:23]` — 「いつも、返してないじゃん」 — PEAK.** ニジ: でも、おまえ、まだ、返せないんでしょ。 真白: ……なぜ、分かるの。 ニジ: だって、おまえ、いつも、返してないじゃん。 真白 has nothing to say. _Density: SPARSE, held — the being seen through._
- **BEAT 4 `[0:23–0:30]` — 「また、明日」.** ニジ: じゃあね。また、明日。 She waves. The rainbow fades slowly — one color left, then gone. 真白's own face, reflected in the dark screen. Cut on the reflection. _Density: HELD — then cut. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `返してくれたら、帰れるんだよ (≈0:04) ／ 宛先に、返すの (≈0:11) ／ いつも、返してないじゃん (≈0:19) ／ the fade and reflection (≈0:25)`

## Temporal Density

- Sparse regions: `0:15–0:23 (the being seen through), 0:23–0:30 (the fade and reflection)`
- Dense regions: `0:00–0:15 (the condition and the 宛先)`
- Long continuous action: `0:23–0:30 the slow fade of the rainbow`
- Rapid transitions: `none — a held, closing segment`

---

# 9. ACTION

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MASHIRO`
- Action: `Asks 「どうしたら、消えるの」, the thing she most wanted to know, her fingers resting on the phone`
- Intention: `To find the way to make it end`
- Intensity: `Medium`
- Speed: `Slow, careful`

### Action Relationship

- Before: `—` (continues from S12's naming)
- After: `ACT_HEAR`

## Action — ACT_HEAR

- ID: `ACT_HEAR`
- Subject: `MASHIRO`
- Action: `Listens as ニジ corrects her — 消える、じゃなくて、返してくれたら、帰れるんだよ — and names the 宛先`
- Intention: `To understand what returning would mean`
- Intensity: `Medium, internal`
- Speed: `Still. Only her eyes move`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_SILENT`

## Action — ACT_SILENT

- ID: `ACT_SILENT`
- Subject: `MASHIRO`
- Action: `Asks ……なぜ、分かるの, and at ニジ's answer — だって、おまえ、いつも、返してないじゃん — she has nothing to say. Her fingers hold, still`
- Intention: `None — she has been seen through, and cannot answer`
- Intensity: `CRITICAL (the being seen through, expressed as a silence)`
- Speed: `Still, and held`

### Action Relationship

- Before: `ACT_HEAR`
- After: `ACT_WATCH`

## Action — ACT_WATCH

- ID: `ACT_WATCH`
- Subject: `MASHIRO`
- Action: `Watches ニジ wave and the rainbow fade — one color left, then gone. Her own face is reflected in the dark screen`
- Intention: `To hold the question 明日も、来るのかな`
- Intensity: `Medium, suppressed`
- Speed: `Very slow`

### Action Relationship

- Before: `ACT_SILENT`
- After: `— (cut on the reflection)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. The screen or her face are sharp; the room falls away`
- Depth of Field: `Very shallow — the room is a soft indigo blur throughout`
- Camera Style: `Slow, deliberate, nearly still. The one move belongs to the fade`

## Camera Events

- **`[0:00–0:08]`** — Locked close on the screen and ニジ's face inside it. The question and the correction play out between the screen and her face, lit from below.
- **`[0:08–0:15]`** — A slight, slow cut to her face, listening, then back to the screen. The rainbow flickers, just slightly.
- **`[0:15–0:23]`** — Hold on her face — the silence after いつも、返してないじゃん. Her expression gives nothing; the screen's light the whole frame.
- **`[0:23–0:30]`** — Locked on the screen as ニジ waves and the rainbow fades — one color left, then gone. The dark glass now reflects 真白's own face. Cut to black on the reflection.

---

# 11. MOTION

## Subject Motion

- Her fingers rest on the phone throughout, never moving; the whole segment is a stillness she cannot break
- Only her eyes move — to ニジ, to the fading rainbow, to her own reflected face
- At いつも、返してないじゃん, her lips part and close again, saying nothing
- ニジ waves once, and fades — the only other motion in the segment

## Object Motion

- The phone does not move on its own. Ever
- Screen content does not scroll, type, or distort. The rainbow afterimage fades slowly, its colors dimming — one color left, then gone
- The wall clock's second hand advances in discrete ticks, faint, out of focus

## Environmental Motion

- The screen's bloom breathes very slightly — the only continuous motion, thinning as the rainbow fades
- Nothing in the room moves. The curtain does not stir

## Physical Characteristics

- Weight: `Ordinary. The phone has heft; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers`
- Acceleration: `Gentle everywhere`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes. The only departure is a fading color`

---

# 12. EMOTION

## Emotional Arc

- A question carried from the first moment (どうしたら、消えるの)
- ↓ Correction — not disappear, but go home (返してくれたら、帰れる)
- ↓ Being seen through (いつも、返してないじゃん — no answer)
- ↓ The goodbye, and the reflection (明日も、来るのかな)

## Emotional Events

- Event: `返してくれたら、帰れるんだよ` — Emotion: `The world's rule, spoken gently — a correction, not a threat` — Intensity: `MEDIUM` — Timing: `≈0:04`
- Event: `いつも、返してないじゃん` — Emotion: `Being seen through. 真白's daily evasion named, and she cannot answer` — Intensity: `CRITICAL — expressed as silence, not reaction` — Timing: `≈0:19`
- Event: `The fade and the reflection` — Emotion: `The absence, and her own face left in the glass. 明日も、来るのかな` — Intensity: `HIGH, withheld` — Timing: `0:23–0:30`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and hand from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow is the only saturated hue — until it fades`

## Lighting Events

- **`[0:00]`** — Screen already on, ニジ's rainbow drifting inside the glass.
- **`[0:08–0:15]`** — The rainbow flickers, just slightly, as she speaks of the 宛先.
- **`[0:15–0:23]`** — Her face lit from below, nearly to silhouette, in the silence.
- **`[0:23–0:30]`** — The rainbow fades, one color left, then gone. The screen dims to a dark glass that reflects 真白's own face. Cut to black.

---

# 14. AUDIO

## Dialogue

- 真白: 「どうしたら、消えるの」
- ニジ: 「消える、じゃなくて、――返してくれたら、帰れるんだよ」
- 真白: 「返す？ 何を」
- ニジ: 「おまえが預けた時間。宛先に、返すの」
- ニジ: 「でも、おまえ、まだ、返せないんでしょ」
- 真白: 「……なぜ、分かるの」
- ニジ: 「だって、おまえ、いつも、返してないじゃん」
- ニジ: 「じゃあね。また、明日」

> ニジ's speech carries **no 「わたし」** — no first-person self-reference, to the very end. She calls 真白「おまえ」, ending with a period. No narration, no voice-over.

## Sound Effects

- The wall clock's dry discrete ticking, present throughout, growing louder as the rainbow fades
- The soft silence of the fade — the rainbow dims with no sound at all
- Almost nothing else

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender, unresolved. Never sinister, never sentimental — no swelling, no sting`
- Emotional Function: `Hold the room's stillness, then thin to nothing as the rainbow fades, leaving only room tone and the clock at the reflection`

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

- Render ニジ as 真白's own face, one step younger, **fully opaque**, a rainbow afterimage **inside the phone screen** — through her very last moment
- ニジ's dialogue — exactly: `消える、じゃなくて、――返してくれたら、帰れるんだよ` ／ `おまえが預けた時間。宛先に、返すの` ／ `だって、おまえ、いつも、返してないじゃん` ／ `じゃあね。また、明日`
- The rainbow fades slowly — one color left, then gone. After it, the dark screen reflects **真白's own face**, not ニジ's
- The fingers rest throughout — no gesture; the segment's act is a departure, not a touch
- End on the reflection, cut to black, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 11–13 レンジより）

- **No transparency.** ニジ is fully opaque, even as she fades — she dims, she does not turn see-through
- **No 「わたし」 from ニジ.** No first-person self-reference in her speech
- **No apparition left after the fade.** Once the last color is gone, ニジ must not linger — the screen reflects only 真白
- **No ghost in the room.** No apparition at human scale, no second body outside the screen
- No supernatural VFX — no glitch, no particles, no light rays. The rainbow is a smudged afterimage, and it fades by dimming
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- The farewell carried in stillness — long holds, few cuts
- The slow fade of the rainbow over any explicit statement of departure
- Silence over score at the reflection

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The flicker of the rainbow at the 宛先 may be omitted (a still frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ is present, fully opaque to her last frame, inside the screen only (ledger 11–13); she fades by dimming, never by turning transparent, and nothing of her remains after the last color is gone. No 「わたし」 in her speech. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at night, holding her phone in both hands. Beats, deliberately uneven: [0:00–0:08] she asks どうしたら、消えるの, and the younger face in the screen corrects her — 消える、じゃなくて、――返してくれたら、帰れるんだよ; [0:08–0:15] she asks 返す？ 何を, and ニジ answers おまえが預けた時間。宛先に、返すの, the rainbow flickering just slightly; [0:15–0:23] THE PEAK — ニジ says でも、おまえ、まだ、返せないんでしょ, 真白 asks ……なぜ、分かるの, and ニジ answers だって、おまえ、いつも、返してないじゃん — and 真白 has nothing to say; [0:23–0:30] ニジ says じゃあね。また、明日, waves, and the rainbow fades slowly — one color left, then gone — leaving 真白's own face reflected in the dark screen, and the shot cuts to black on that reflection. The condition holds the largest share of the duration. Ends on the reflection, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ is 真白's own face one step younger (longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head), a rainbow afterimage INSIDE the phone screen, never standing in the room at human scale, with no shadow anywhere, fully opaque. Her colors drift slowly, blue to green to blue — and at the end they fade, one color left, then gone. Night is deep indigo lit solely by one cold blue-white phone screen. No on-screen text, no message bubbles. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Her fingers rest on the phone throughout and never move; the whole segment is a stillness she cannot break. Only her eyes move — to ニジ, to the fading rainbow, to her own reflected face. At いつも、返してないじゃん, her lips part and close again, saying nothing. ニジ waves once, then fades — dimming slowly, opaque to the last, never turning see-through — one color left, then gone. The phone never moves by itself and never glitches, flickers or distorts; its screen content does not scroll or type. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly, thinning as the rainbow fades. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; the screen or her face are sharp, the room falls away. Slow and deliberate, nearly still. [0:00–0:08] locked close on the screen and ニジ's face inside it, the question and the correction playing out between the screen and her face lit from below. [0:08–0:15] a slight, slow cut to her face, listening, then back to the screen; the rainbow flickers just slightly. [0:15–0:23] hold on her face — the silence after いつも、返してないじゃん; her expression gives nothing. [0:23–0:30] locked on the screen as ニジ waves and the rainbow fades — one color left, then gone — the dark glass now reflecting 真白's own face; cut to black on the reflection.

## Audio Prompt

Almost silent. Deep quiet night room tone and a wall clock ticking, dry and discrete, growing louder as the rainbow fades. The fade itself is silent — the rainbow dims with no sound at all. The dialogue, quiet and close: 真白 — どうしたら、消えるの ／ 返す？ 何を ／ ……なぜ、分かるの. ニジ — 消える、じゃなくて、――返してくれたら、帰れるんだよ ／ おまえが預けた時間。宛先に、返すの ／ でも、おまえ、まだ、返せないんでしょ ／ だって、おまえ、いつも、返してないじゃん ／ じゃあね。また、明日. ニジ's speech has no 「わたし」, no first-person self-reference, and she calls 真白 「おまえ」. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning to nothing as the rainbow fades, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparency, no translucency, no see-through body, no わたし in ニジ's speech, no first-person self-reference, no standing in the room at human scale, no figure outside the phone screen, no full-height apparition, no glowing eyes, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep03-seg04-30s-01`
- Segment ID: `S13`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_03, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 8s / 7s / 8s / 7s. Condition = BEAT 1 at 8s (27%)`
- Camera Events: `4 events as listed in §10. One held fade (0:23–0:30)`
- Action Events: `ACT_ASK → ACT_HEAR → ACT_SILENT → ACT_WATCH`
- Audio Events: `eight spoken lines ／ no 「わたし」 from ニジ ／ clock ticking throughout ／ the fade is silent`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut to black on the reflection`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The fade reads as transparency.** The single most damaging failure here. ニジ dims — she does not turn see-through. She is opaque to her last frame, then gone. Verify frame by frame.
- **The model lets ニジ say 「わたし」.** She must never self-reference in the first person, to the very end. Check the audio line by line.
- **The model leaves ニジ after the fade.** Once the last color is gone, the screen must reflect only 真白's own face. If ニジ lingers as a ghostly shape, regenerate.
- **The model renders the reflection as ニジ.** The reflection is 真白's own face — her current face, not the younger one. Check the final frame.

## Changes

- _(none yet)_

## Next Generation

- If the fade lands — opaque to the last, then only 真白's reflection — this segment closes episode 3, planting 宛先 and 返す for the episodes to come; S14 begins the daylight of episode 4.
