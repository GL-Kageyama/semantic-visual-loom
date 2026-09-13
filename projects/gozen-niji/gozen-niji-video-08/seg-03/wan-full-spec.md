# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第8話 S34「返すの」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「返すの」の一語への着地——ニジが泣きそうな顔で笑い、泣かない（指の背骨の第34本・対話の休止）。ニジは在る（画面の中だけ・完全に不透明）。登場人物は真白とニジのみ。画面文字なし。虹色がほんの少しだけ揺れるのは、この1本が初めて。**

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

> **ニジ appears this segment**（ledger S33–34 — 在）. 真白とニジのみが人物。美月・小春・湊は登場しない。

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
- Appearance: `No message text this segment — only ordinary UI: the dark, otherwise empty screen holding ニジ inside it as she speaks, no message, no chat thread, no text. Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
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

真白 asks what she must do, and ニジ lands on a single word — 返すの — then smiles with a face on the edge of crying, without crying.

## Beginning

The room, still dark. 真白's hand, on her knee, has clenched slightly. She asks it quietly: 「……じゃあ、どうすればいいの」

## Turn

「返してくれたら、わたしは、帰れる」 「返す？」 — and ニジ spells it out: 「おまえが受け取らなかった感情を。——宛先に、返すの」 Not erase, not ignore, not destroy: 「消すんじゃない。無視するんじゃない。わたしを壊すんじゃない。——返すの。おまえが避けてた宛先に、——言葉を届けるの。」

## Peak

ニジ smiles — a face on the edge of crying, and does not cry. The iridescence trembles, very slightly, for the first time. 「そうすれば、わたしは、ちゃんと生きてたって、みんなに知ってもらえる。」

## Pull（引き — 切れ目）

「返してくれたら、わたしは、帰れる。」 The condition, hanging. Cut on the smile — the face on the edge of crying. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The smile holds 9s (30%).

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「どうすれば」 — ESTABLISH.** Dark bedroom. 真白's hand, on her knee, clenched slightly. She asks, quiet: ……じゃあ、どうすればいいの。ニジ: 返してくれたら、わたしは、帰れる。 _Density: SPARSE — a quiet exchange, no event yet._
- **BEAT 2 `[0:06–0:15]` — 「返すの」.** 真白: 返す？ ニジ: おまえが受け取らなかった感情を。——宛先に、返すの。消すんじゃない。無視するんじゃない。わたしを壊すんじゃない。——返すの。おまえが避けてた宛先に、——言葉を届けるの。 _Density: TRANSITION — the three negations, then the single word lands._
- **BEAT 3 `[0:15–0:24]` — 「笑顔」 — PEAK, longest share.** ニジ smiles — a face on the edge of crying, and does not cry. The iridescence trembles, very slightly, for the first time. そうすれば、わたしは、ちゃんと生きてたって、みんなに知ってもらえる。 _Density: DENSE at the head, then the smile, held._
- **BEAT 4 `[0:24–0:30]` — 「帰れる」.** 返してくれたら、わたしは、帰れる。 The condition, hanging. The smile holds — the face on the edge of crying. Cut on the smile. Nothing after it. _Density: HELD — then a clean cut on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `「……じゃあ、どうすればいいの」 (≈0:03) ／ the three negations landing on 返すの (≈0:12) ／ the smile, on the edge of crying (≈0:18, then held)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the exchange), 0:24–0:30 (the held smile)`
- Dense regions: `0:15–0:24 (the smile + the iridescence trembling)`
- Long continuous action: `0:15–0:24 the smile held, the iridescence trembling slightly`
- Rapid transitions: `none — a slow, still night`

---

# 9. ACTION

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MASHIRO`
- Action: `Her hand, on her knee, clenched slightly; she asks 「……じゃあ、どうすればいいの」`
- Intention: `To know what the answer asks of her`
- Intensity: `Medium, internal`
- Speed: `Slow, quiet`

### Action Relationship

- Before: `—` (continues from S33's 「結晶」)
- After: `ACT_NEGATE`

## Action — ACT_NEGATE

- ID: `ACT_NEGATE`
- Subject: `NIJI`
- Action: `Names what 返す is not — 消すんじゃない、無視するんじゃない、わたしを壊すんじゃない — then lands on 返すの`
- Intention: `To close the door on every way out except the one`
- Intensity: `Medium, measured`
- Speed: `Even, unhurried`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_SMILE`

## Action — ACT_SMILE

- ID: `ACT_SMILE`
- Subject: `NIJI`
- Action: `Smiles with a face on the edge of crying — and does not cry. The iridescence trembles, very slightly`
- Intention: `Not reassurance — a hope she can barely hold`
- Intensity: `CRITICAL (the emotional peak, expressed as a smile that almost breaks)`
- Speed: `Slow, and held`

### Action Relationship

- Before: `ACT_NEGATE`
- Simultaneous With: `そうすれば、わたしは、ちゃんと生きてたって、みんなに知ってもらえる`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `NIJI`
- Action: `Holds the smile — the face on the edge of crying — through the last line`
- Intention: `To keep the promise on her face while she names the condition`
- Intensity: `Medium, steady`
- Speed: `Held; only the iridescence trembles`

### Action Relationship

- Before: `ACT_SMILE`
- After: `— (cut on the smile)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, through the glass into the screen, at the edge where 真白 sits`
- Lens Character: `Long-ish, shallow. The room falls away into soft indigo`
- Depth of Field: `Shallow — ニジ's face sharp, the room soft behind`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:06]`** — Locked on 真白's hand on her knee, then up to her face as she asks. Static, close.
- **`[0:06–0:15]`** — Cut to ニジ inside the screen, listing the three negations. The camera stays on her face as the word 返すの lands.
- **`[0:15–0:24]`** — Cut to ニジ's face, static, close, for the smile — a face on the edge of crying. Hold. No push, no rack, no reframe.
- **`[0:24–0:30]`** — Hold on the smile through the last line. Cut on the smile.

---

# 11. MOTION

## Subject Motion

- 真白's body holds; her hand, on her knee, is clenched slightly and does not move
- ニジ's only movement is the smile — slow to arrive, then held — and the very slight tremble of her iridescence
- The rest is stillness. This is a held breath of a segment

## Object Motion

- The phone does not move on its own. Ever
- Screen content is static except the slow drift and slight tremble of the rainbow
- The wall clock's second hand advances in discrete ticks, out of focus behind

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand; the futon compresses under her`
- Inertia: `High — almost nothing moves at all`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by the smallest precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- A question asked into the dark (どうすればいいの)
- ↓ The single word that closes every exit (返すの)
- ↓ Something like hope (a smile on the edge of crying)
- ↓ The condition, hanging (帰れる)

## Emotional Events

- Event: `「……じゃあ、どうすればいいの」` — Emotion: `A question asked quietly, with her hand already clenched` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:03`
- Event: `The three negations landing on 返すの` — Emotion: `The door closing on every way out except one` — Intensity: `MEDIUM` — Timing: `≈0:12`
- Event: `The smile — a face on the edge of crying, without crying` — Emotion: `Something like hope, held barely` — Intensity: `CRITICAL, expressed as restraint` — Timing: `≈0:18, held`

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
- **`[0:15–0:24]`** — As the smile arrives, ニジ's rainbow trembles very slightly — its first instability in the whole series. No other change in the light.
- **`[0:30]`** — Cut on the smile. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

- 真白: 「……じゃあ、どうすればいいの」 — quiet
- ニジ: 「返してくれたら、わたしは、帰れる」
- 真白: 「返す？」
- ニジ: 「おまえが受け取らなかった感情を。——宛先に、返すの」
- ニジ: 「消すんじゃない。無視するんじゃない。わたしを壊すんじゃない。——返すの。おまえが避けてた宛先に、——言葉を届けるの」
- ニジ: 「そうすれば、わたしは、ちゃんと生きてたって、みんなに知ってもらえる」
- ニジ: 「返してくれたら、わたしは、帰れる」

> ニジ uses 「わたし」 — calm, almost a voice of certainty, but the smile says more than the words. She is **not crying**, not sobbing. No voice-over, no narration.

## Sound Effects

- Deep quiet night room tone, almost nothing
- The wall clock's second hand, dry discrete ticks, faint throughout
- Soft futon fabric, once, as 真白 shifts

## Environment

- Deep quiet night room tone. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender without being sentimental. Never sinister`
- Emotional Function: `Hold the room's stillness under the exchange. It may thin toward the smile, leaving only room tone and the clock. No horror strings, no sting, no swelling`

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

- ニジ is **present** — inside the screen only, 真白's own face one step younger, a rainbow afterimage, **fully opaque**
- The three negations must land on the single word: 消すんじゃない → 無視するんじゃない → わたしを壊すんじゃない → **返すの**
- ニジ smiles with a **face on the edge of crying, and does not cry**
- The iridescence trembles **very slightly** — its first instability, no more
- End by cutting on the smile, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 S33–34 レンジより）

- **No full-body transparency.** ニジ is opaque here — no translucent body, no see-through torso or face, no fading, no dissolving, no disappearing
- **No flashy disappearance effect.** No dramatic fade-out, no dissolving into light, no particle burst, no spectacle of vanishing
- **No crying, no tears, no sobbing.** The smile is on the *edge* of crying; it must not cross into tears
- **No figure in the room, no other faces.** 真白 and ニジ are the only figures
- **No generic ghost.** ニジ is not a horror ghost — no ghostly glow, no spectral aura, no glowing eyes
- Do not have 真白 cry, gasp, or widen her eyes

## PREFER

- Holds over movement; when in doubt, do less
- The smile held over a reaction
- Negative space over detail; the room may be nearly empty

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- Music may be absent altogether
- ニジ's rainbow may drift slowly, blue to green to blue, and tremble once, very slightly

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear inside the screen only, fully opaque, smiling on the edge of crying without crying (ledger S33–34 — 在); no full-body transparency, no tears. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M., with a figure inside her phone screen. Beats, deliberately uneven: [0:00–0:06] 真白's hand, on her knee, clenched slightly, and she asks ……じゃあ、どうすればいいの, and the figure answers 返してくれたら、わたしは、帰れる; [0:06–0:15] 真白 asks 返す？ and the figure spells it out — おまえが受け取らなかった感情を。——宛先に、返すの, then the three negations 消すんじゃない。無視するんじゃない。わたしを壊すんじゃない。——返すの。おまえが避けてた宛先に、——言葉を届けるの; [0:15–0:24] THE PEAK — the figure SMILES WITH A FACE ON THE EDGE OF CRYING, and does not cry, and its iridescence trembles very slightly for the first time, while it says そうすれば、わたしは、ちゃんと生きてたって、みんなに知ってもらえる; [0:24–0:30] 返してくれたら、わたしは、帰れる — the condition hanging — and the smile holds, and the shot cuts on the smile. The smile holds the largest share of the duration. Ends on the smile, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: inside the phone screen only — 真白's own face one step younger, longer lashes and slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — a rainbow afterimage, no shadow anywhere, fully opaque, her smile honest and slightly trembling, blue drifting slowly to green and back; never standing in the room at human scale. Night is deep indigo lit solely by the cold blue-white screen. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost nothing moves. 真白's body holds; her hand, on her knee, is clenched slightly and does not move. ニジ's only movement is the smile — slow to arrive, then held — and the very slight tremble of her iridescence, its first instability, no more than a shiver. The rainbow drifts slowly, blue to green to blue, never shimmering or pulsing. Ordinary weight and inertia; the phone has heft, the futon compresses. The phone never moves by itself and never glitches, flickers or distorts. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, through the glass into the screen, at the edge where 真白 sits. Longish lens, shallow depth of field; ニジ's face sharp, the room soft behind. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked on 真白's hand on her knee, then up to her face as she asks, static and close. [0:06–0:15] cut to ニジ inside the screen, listing the three negations, the camera staying on her face as the word 返すの lands. [0:15–0:24] cut to ニジ's face, static, close, for the smile — a face on the edge of crying; hold, no push, no rack, no reframe. [0:24–0:30] hold on the smile through the last line; cut on the smile.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, faint throughout. Soft futon fabric, once, as 真白 shifts. Spoken lines only: 真白 asks ……じゃあ、どうすればいいの, then 返す？; ニジ answers 返してくれたら、わたしは、帰れる, then おまえが受け取らなかった感情を。——宛先に、返すの, then 消すんじゃない。無視するんじゃない。わたしを壊すんじゃない。——返すの。おまえが避けてた宛先に、——言葉を届けるの, then そうすれば、わたしは、ちゃんと生きてたって、みんなに知ってもらえる, then 返してくれたら、わたしは、帰れる. Her voice is calm, using わたし; she is not crying, not sobbing. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning toward the smile and leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no fully transparent figure, no translucent body, no see-through torso, no see-through face, no fading figure, no dissolving, no disappearing, no vanishing, no full-body transparency, no flashy disappearance, no dramatic fade-out, no dissolving into light, no particle burst, no spectacle of vanishing, no shimmer, no flickering transparency, no pulsing, no second person in the room, no full-body figure in the room, no figure stepping out of the phone, no ghostly glow, no spectral aura, no generic anime ghost girl, no spirit girl, no other faces, no tears, no sobbing, no crying face, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep08-seg03-30s-01`
- Segment ID: `S34`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_08, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 9s / 9s / 6s. Smile = BEAT 3 at 9s (30%)`
- Camera Events: `4 events as listed in §10. All static or held`
- Action Events: `ACT_ASK → ACT_NEGATE → ACT_SMILE → ACT_HOLD`
- Audio Events: `seven lines of dialogue ／ clock ticking faint ／ no voice-over ／ music thinning toward the smile`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the smile`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The smile crosses into tears.** The whole point is a face *on the edge* of crying that does not cry. If tears appear, regenerate — no one cries in this series.
- **The iridescence trembles too much.** It is a very slight instability, not a pulse or a flicker. If it reads as VFX, reduce it to almost nothing.
- **The negations blur into one speech.** The three 消す・無視する・壊す must land one at a time before 返すの. If they run together, slow the delivery.
- **The model may put her in the room or make her transparent.** ニジ is opaque and inside the screen. The negative prompt front-loads both.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If the smile reads and she does not cry, this segment is done; the condition it leaves hanging — 返してくれたら、わたしは、帰れる — is what S35's stopped finger answers.
