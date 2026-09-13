# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第4話 S17「どうせ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「対話。指は休む」——指は完全に休み、言葉だけが動く。ニジが、真白が心の中で呟きかけた「どうせ」を代わりに言う。「その言葉が、いちばん、あぶないんだよ」と少しだけ悲しそうに笑う（泣かない）。ニジは在（不透明・画面の中だけ・「わたし」禁）。画面文字なし。**

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

> **ニジ appears this segment**（ledger 16–17 — opaque, inside the screen only, her rainbow faint in the dark air）. No other character appears.

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
- Appearance: `No screen text this segment — dialogue only. The screen shows ニジ, not text`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
- Continuity Importance: `HIGH`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads 2:00 — the hinge of the night`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_04_現実を生きるほど、増える.md`
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

ニジ says the word 真白 was about to whisper — 「どうせ」— and names it the most dangerous word: 「その言葉が、いちばん、あぶないんだよ」 Then she smiles, slightly sad, a smile 真白 does not know, and says 返すまで、ずっと、残るんだよ。

## Beginning

真白: 「スマホをやめれば、いいと思ってた」 → ニジ: 「減らしても、消えないよ」 → 真白: 「……じゃあ、どうすればいいの」

## Turn

ニジ: 「どうせ」 — the word 真白 was forming inside, spoken for her. 「おまえ、いま、『どうせ、私に返せるわけない』って、思ったでしょ」

## Peak

真白: 「――っ」 struck silent. ニジ: 「どうせ、ね。その言葉が、いちばん、あぶないんだよ」 — and she smiles, slightly sad, a smile 真白 does not know. 「だって、預けたんだもの。減らしても、消えない。返すまで、ずっと、残るんだよ」

## Pull（引き — 切れ目）

真白 sits down on the floor, the phone — ニジ on its screen — left on the desk above. 宛先。返す。預けた時間。私が、誰に、何を、預けてるの。 思い当たらなかった。 Cut on ニジ's slightly sad smile, held in the screen, the rainbow faint in the dark air. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The naming どうせ holds 9s (30%); the warning holds 9s (30%).

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the bedroom; the named word どうせ is its own beat.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「消えない」.** Night, 2:00 A.M. ニジ on the screen, opaque, the rainbow faint in the air. 真白: スマホをやめれば、いいと思ってた。 ニジ: 減らしても、消えないよ。 真白: ……じゃあ、どうすればいいの。 _Density: SPARSE — a quiet exchange, the fingers at rest._
- **BEAT 2 `[0:07–0:16]` — 「どうせ」 — the naming, longest share.** ニジ: どうせ。 — the word 真白 was about to whisper, spoken for her. おまえ、いま、『どうせ、私に返せるわけない』って、思ったでしょ。 _Density: DENSE at the head, then held on the named word._
- **BEAT 3 `[0:16–0:25]` — 「あぶない」.** 真白: ――っ. ニジ: どうせ、ね。その言葉が、いちばん、あぶないんだよ。 She smiles, slightly sad — a smile 真白 does not know. だって、預けたんだもの。減らしても、消えない。返すまで、ずっと、残るんだよ。 _Density: TRANSITION — the warning, the sad smile._
- **BEAT 4 `[0:25–0:30]` — 「座り込む」.** 真白 sits down on the floor, the phone left on the desk. 宛先。返す。預けた時間。私が、誰に、何を、預けてるの。思い当たらなかった。 Cut on ニジ's slightly sad smile, held in the screen. _Density: HELD — then cut precisely on the pull. Nothing after it._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the naming どうせ (≈0:08) ／ the warning and the sad smile (≈0:18) ／ 真白 sitting down (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the exchange), 0:25–0:30 (sitting down)`
- Dense regions: `0:07–0:16 (the naming), 0:16–0:25 (the warning)`
- Long continuous action: `0:25–0:30 真白 sitting, the question unresolved`
- Rapid transitions: `none — a dialogue segment that ends on a held stillness`

---

# 9. ACTION

## Action — ACT_ASK

- ID: `ACT_ASK`
- Subject: `MASHIRO`
- Action: `「スマホをやめれば、いいと思ってた」 → 「……じゃあ、どうすればいいの」`
- Intention: `To find the way out — the rule 触ったら負け failed her`
- Intensity: `Low, tired`
- Speed: `Small, slow`

### Action Relationship

- Before: `— (continues from S16's 領収書)`
- After: `ACT_ANSWER`

## Action — ACT_ANSWER

- ID: `ACT_ANSWER`
- Subject: `NIJI`
- Action: `「減らしても、消えないよ」 — plain, certain`
- Intention: `To tell her the truth plainly`
- Intensity: `Low`
- Speed: `Unhurried`

### Action Relationship

- Before: `ACT_ASK`
- After: `ACT_NAME`

## Action — ACT_NAME

- ID: `ACT_NAME`
- Subject: `NIJI`
- Action: `「どうせ」 — speaks the word 真白 was about to whisper. 「おまえ、いま、『どうせ、私に返せるわけない』って、思ったでしょ」`
- Intention: `To show her the word she was hiding from herself`
- Intensity: `Medium`
- Speed: `Steady, then a stillness around the word`

### Action Relationship

- Before: `ACT_ANSWER`
- After: `ACT_STRUCK`

## Action — ACT_STRUCK

- ID: `ACT_STRUCK`
- Subject: `MASHIRO`
- Action: `「――っ」 — caught out, she cannot answer`
- Intention: `None — the word is taken from her mouth`
- Intensity: `CRITICAL (the exposure, expressed as a caught breath)`
- Speed: `A sharp inhale, then still`

### Action Relationship

- Before: `ACT_NAME`
- After: `ACT_WARN`

## Action — ACT_WARN

- ID: `ACT_WARN`
- Subject: `NIJI`
- Action: `「どうせ、ね。その言葉が、いちばん、あぶないんだよ」 — and she smiles, slightly sad, a smile 真白 does not know`
- Intention: `To warn her, gently`
- Intensity: `Medium, warm-edged`
- Speed: `Slow, soft`

### Action Relationship

- Before: `ACT_STRUCK`
- After: `ACT_SIT`

## Action — ACT_SIT

- ID: `ACT_SIT`
- Subject: `MASHIRO`
- Action: `Sits down on the floor, the phone left on the desk above. 思い当たらなかった`
- Intention: `None — she cannot think of anyone she deposited time with`
- Intensity: `Medium, suppressed`
- Speed: `Slow, sinking, then still`

### Action Relationship

- Before: `ACT_WARN`
- After: `— (cut on ニジ's smile)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, at the screen — straight-on at ニジ, then down at 真白 on the floor`
- Lens Character: `Long-ish, shallow. Only ニジ and, later, 真白's lowered face are ever sharp`
- Depth of Field: `Shallow — the room is a dark indigo blur behind`
- Camera Style: `Slow, deliberate, nearly still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Locked on ニジ on the screen, 真白 just off-frame. The exchange passes between them, unhurried. Static.
- **`[0:07–0:16]`** — A slow push-in on ニジ as she says どうせ — the word filling the air between them. The piece's single sustained move.
- **`[0:16–0:22]`** — Cut to 真白, struck, mouth open on the caught breath. Then back to ニジ, smiling slightly sad.
- **`[0:22–0:25]`** — Hold on ニジ's slightly sad smile, the rainbow faint in the dark air around her.
- **`[0:25–0:30]`** — A slow tilt down as 真白 sinks to the floor, the phone — ニジ on its screen — left on the desk above. Cut on ニジ's smile, held.

---

# 11. MOTION

## Subject Motion

- ニジ barely moves — a slow smile, a blink, the drift of her rainbow; the smile is the whole event
- Her rainbow is 滲み・残像 — a slow color drift blue → green → blue, never light rays, particles, or aura
- 真白's fingers rest entirely; the only movement is the sinking of her body to the floor
- The caught breath 「――っ」 is a small, sharp motion, then nothing

## Object Motion

- The phone stays where it is on the desk — it does not move on its own
- Its screen shows ニジ, opaque, unchanged except for the drift of her rainbow
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Environmental Motion

- The dark room is still. The curtain does not move
- The rainbow bleeding into the dark air is the only continuous motion

## Physical Characteristics

- Weight: `Ordinary. Her body sinks with real weight to the floor`
- Inertia: `High for everything; ニジ's drift is near-weightless but never floaty`
- Acceleration: `Gentle everywhere; the caught breath is the only sharp thing`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Quiet defeat (減らしても、消えないよ)
- ↓ Exposure (ニジ speaks the word she was hiding: どうせ)
- ↓ The warning, and the sad smile (その言葉が、いちばん、あぶないんだよ)
- ↓ The unanswerable (私が、誰に、何を、預けてるの — 思い当たらなかった)

## Emotional Events

- Event: `ニジ says どうせ, the word 真白 was about to whisper` — Emotion: `Exposure — the hidden word taken from her` — Intensity: `HIGH` — Timing: `≈0:08`
- Event: `真白's caught breath 「――っ」` — Emotion: `Caught out` — Intensity: `CRITICAL — expressed only as a sharp inhale` — Timing: `≈0:16`
- Event: `ニジ's slightly sad smile` — Emotion: `The warning, and a gentleness 真白 does not know` — Intensity: `MEDIUM` — Timing: `≈0:20`
- Event: `真白 sits down, 思い当たらなかった` — Emotion: `The unanswerable` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:26`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, low, close. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on 真白's hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow is the only saturated hue, and it does not alter the room's darkness`

## Lighting Events

- **`[0:00]`** — The screen's blue-white and ニジ's rainbow share the frame; the room is dark around them.
- **`[0:07–0:16]`** — As the camera closes on ニジ, her rainbow bleeds faintly into the dark air — a soft wash that never brightens the room.
- **`[0:16–0:25]`** — The slightly sad smile catches the screen's glow from below.
- **`[0:25–0:30]`** — As 真白 sinks to the floor, she falls out of the screen's reach into shadow. Cut on ニジ, still lit, on the desk above.

---

# 14. AUDIO

## Dialogue

- 真白: 「スマホをやめれば、いいと思ってた」 — small, tired
- ニジ: 「減らしても、消えないよ」 — plain, certain
- 真白: 「……じゃあ、どうすればいいの」
- ニジ: 「どうせ。おまえ、いま、『どうせ、私に返せるわけない』って、思ったでしょ」 — steady, then still around the word
- 真白: 「――っ」 — a caught breath, not a word
- ニジ: 「どうせ、ね。その言葉が、いちばん、あぶないんだよ。だって、預けたんだもの。減らしても、消えない。返すまで、ずっと、残るんだよ」 — soft, slightly sad, not crying

> ニジ never says わたし. No narration, no voice-over.

## Sound Effects

- The faint, dry ticking of the wall clock, present throughout
- The soft fabric of 真白 sinking to the floor at the end
- A very faint, almost inaudible shimmer — ニジ's rainbow, as sound, barely there

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, warm-edged, faintly sad. Never sinister, never sentimental — no horror strings`
- Emotional Function: `Hold the room's stillness under the exchange, then thin toward the close, leaving only room tone, the clock, and ニジ's voice`

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

- Show ニジ **in**, and only in, the screen — never standing in the room at human scale
- Keep ニジ **fully opaque** — her face is 真白's own face, one step younger (longer lashes, fuller cheeks, the same tilt of the head)
- Let her smile be **slightly sad, not crying** — a smile 真白 does not know, with no tears
- Let her rainbow be a **滲み・残像** (a slow bleed of color, blue → green → blue), never light rays, particles, or an aura — and it may bleed only faintly into the dark room air
- End by cutting on ニジ's slightly sad smile, held in the screen, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 16–17 レンジより）

- **No transparency.** ニジ is opaque — no see-through, no dissolving, no fading to invisibility
- **No わたし.** ニジ never refers to herself as "I" — the first-person self-naming is withheld until S31
- Do not let ニジ stand in the room at human scale — she exists inside the screen only
- Do not let ニジ cry — the slightly sad smile is the limit; no tears, no weeping

## PREFER

- Holding ニジ's face straight-on and still — the sad smile is the whole pull
- Her voice over score at the warning
- The room nearly empty; negative space over detail

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in during beat 2 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ appears only opaque and inside the screen (ledger 16–17); no transparency, no わたし, no crying. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M., facing ニジ inside the screen of the phone on the desk. Beats, deliberately uneven: [0:00–0:07] 真白 says スマホをやめれば、いいと思ってた, ニジ answers 減らしても、消えないよ, and 真白 asks ……じゃあ、どうすればいいの; [0:07–0:16] ニジ says どうせ — the word 真白 was about to whisper, spoken for her — おまえ、いま、『どうせ、私に返せるわけない』って、思ったでしょ; [0:16–0:25] 真白 is struck (――っ), and ニジ says どうせ、ね。その言葉が、いちばん、あぶないんだよ, smiling slightly sad, a smile 真白 does not know, and だって、預けたんだもの。減らしても、消えない。返すまで、ずっと、残るんだよ; [0:25–0:30] 真白 sits down on the floor, the phone left on the desk above, and the shot cuts on ニジ's slightly sad smile, held in the screen, the rainbow faint in the dark air. The naming holds the largest share of the duration. Ends on ニジ, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: a rainbow afterimage that resolves into 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same tilt of the head — sitting on top of the phone screen, fully opaque, never transparent, no shadow. She stays inside the screen, never standing in the room at human scale; only her rainbow bleeds faintly into the dark room air, a slow drift blue → green → blue. She never says わたし and never refers to herself as "I". She smiles slightly sad, without crying. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. Almost all movement belongs to ニジ's face and 真白's sinking body; the fingers rest entirely. ニジ barely moves — a slow, slightly sad smile, a blink; her rainbow drifts slowly blue → green → blue, a bleed and an afterimage, never light rays, particles, or an aura. 真白's only movement is her body sinking slowly to the floor at the end. The phone stays where it is; its screen shows ニジ, opaque, unchanged except for the drift of her rainbow. The wall clock's second hand advances in discrete ticks. Gentle acceleration everywhere; the caught breath is the only sharp thing. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, at the screen — straight-on at ニジ, then down at 真白 on the floor. Longish lens, shallow depth of field; only ニジ and, later, 真白's lowered face are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] locked on ニジ on the screen, 真白 just off-frame. [0:07–0:16] a slow push-in on ニジ as she says どうせ. [0:16–0:22] cut to 真白, struck, mouth open on the caught breath, then back to ニジ smiling slightly sad. [0:22–0:25] hold on ニジ's slightly sad smile, the rainbow faint in the dark air. [0:25–0:30] a slow tilt down as 真白 sinks to the floor, the phone left on the desk above; cut on ニジ's smile, held.

## Audio Prompt

Almost silent. Deep quiet night room tone. The faint dry ticking of a wall clock, present throughout. Dialogue, unhurried: 真白, small and tired — スマホをやめれば、いいと思ってた; ニジ, plain and certain — 減らしても、消えないよ; 真白 — ……じゃあ、どうすればいいの; ニジ, steady, then still around the word — どうせ。おまえ、いま、『どうせ、私に返せるわけない』って、思ったでしょ; 真白, a caught breath, not a word — ――っ; ニジ, soft and slightly sad, not crying — どうせ、ね。その言葉が、いちばん、あぶないんだよ。だって、預けたんだもの。減らしても、消えない。返すまで、ずっと、残るんだよ. ニジ never says わたし. No narration, no voice-over. The soft fabric of 真白 sinking to the floor at the end. Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only room tone, the clock, and ニジ's voice. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no transparent apparition, no see-through figure, no ghost dissolving into transparency, no fading to invisibility, no full-size figure standing in the room, no apparition outside the screen, no ghost saying "watashi", no first-person self-reference from the ghost, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep04-seg04-30s-01`
- Segment ID: `S17`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_04, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 9s / 9s / 5s. Naming = BEAT 2 at 9s (30%), warning = BEAT 3 at 9s (30%)`
- Camera Events: `5 events as listed in §10. One sustained push-in (0:07–0:16), one slow tilt (0:25–0:30)`
- Action Events: `ACT_ASK → ACT_ANSWER → ACT_NAME → ACT_STRUCK → ACT_WARN → ACT_SIT`
- Audio Events: `dialogue (6 lines) ／ ニジ never says わたし ／ music gone by the close`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on ニジ's smile`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The sad smile may read as crying.** The limit is a slightly sad smile, no tears. If ニジ weeps, regenerate — she 泣かない.
- **ニジ may render transparent.** Same risk as S16. Verify frame by frame; she must be opaque.
- **The caught breath 「――っ」 may read as a scream.** It is a small sharp inhale, nothing more. If it performs, restrain it.
- **The sinking to the floor may read as collapse.** She sinks slowly, with weight, not falls. Keep it slow and quiet.
- **ニジ may say わたし.** The first-person self-naming is withheld until S31. If it appears, regenerate the dialogue.

## Changes

- _(none yet)_

## Next Generation

- If the sad smile and the unanswerable question land, this closes episode 4; S18 opens episode 5 in the daylight, without ニジ.
