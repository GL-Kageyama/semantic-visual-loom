# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第10話 S45「あと一つ」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「読む」——返ってきた返信の三行を、指を動かさずに読む（指の背骨の第45本）。喉の奥がほどけて、ニジは「もう、ほとんど空になった」と笑う（泣かない）。ニジは画面の中だけ・輪郭がほとんど消えかけ。中学の友人は顔を出さない（返信は文字のみ）。画面文字は返信の三行。**

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

> **ニジ appears this segment**（ledger 41–45 — outline almost gone）. 中学の友人は顔を出さない（名前と文字のみ）.

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
- Appearance: `One three-line reply, character-for-character: ありがとう。 ／ ごめんね、返事、遅れて。――ちょっと、びっくりしちゃって。 ／ あのときのこと、ずっと、気にしてた。――元気そうで、よかった。 Rendered exactly as an ordinary phone renders it: cold blue-white on dark UI`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
- Continuity Importance: `HIGH`

## WALL_CLOCK

- Type: `clock`
- Appearance: `Visible second hand, advancing in discrete ticks. Reads short of 2:00 at the hinge of the night`
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
- Source: `soul-voice-teller/examples/gozen-niji/草稿/draft_10_疎遠になった、あの人のところへ.md`
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

The fifth night. The reply arrives — three lines from あの子. 真白 reads them, and something in her throat comes undone. ――無駄じゃ、なかった。 That night, ニジ's outline is almost gone.

## Beginning

五日目の夜. The screen lights. The reply, three lines:

ありがとう。 ／ ごめんね、返事、遅れて。ちょっと、びっくりしちゃって。 ／ あのときのこと、ずっと、気にしてた。元気そうで、よかった。

## Turn

真白 reads it. Something unknots in her throat. The reply is not to ease her anxiety — it is proof that her time, back then, was alive in あの子's life. ――無駄じゃ、なかった。

## Peak

「……ニジ」 ニジ: 「へへ。もう、ほとんど空になった」 — ニジ laughs; the rainbow afterimage trembles. 残る宛先は、あと、一つ。

## Pull（引き — 切れ目）

Cut on ニジ's almost-faded outline, laughing, the rainbow afterimage trembling — 残る宛先は、あと、一つ. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The reply holds 10s (33%); the episode's last line holds 6s.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「五日目の夜」 — ESTABLISH.** The screen lights. The reply arrives, three lines. ありがとう。ごめんね、返事、遅れて。あのときのこと、ずっと、気にしてた。 _Density: SPARSE — a held frame, the text the only event._
- **BEAT 2 `[0:07–0:17]` — 「返信を読む」 — longest share.** 真白 reads the three lines, once, slowly. Something in her throat comes undone. 無駄じゃ、なかった — the meaning, arriving without a word. _Density: DENSE at the head (the text), then held on the unknotting._
- **BEAT 3 `[0:17–0:24]` — 「ほどける」.** Held on her face — the throat, the eyes, the release without a sound. ニジ's outline is almost gone, the rainbow afterimage thin and faint. _Density: SPARSE, internal — the only event is a loosening._
- **BEAT 4 `[0:24–0:30]` — 「あと一つ」.** 「……ニジ」 ニジ laughs: へへ。もう、ほとんど空になった。 The rainbow afterimage trembles. 残る宛先は、あと、一つ。 Cut on ニジ's almost-faded outline. Nothing after it. _Density: HELD — then a clean cut on the episode's pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the three-line reply (≈0:04) ／ the unknotting (≈0:12) ／ ニジ's もう、ほとんど空になった (≈0:26)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the reply arriving), 0:17–0:24 (the unknotting)`
- Dense regions: `0:07–0:17 (reading the reply)`
- Long continuous action: `0:17–0:24 the held release`
- Rapid transitions: `none — the slowest, most held ending of the episode`

---

# 9. ACTION

## Action — ACT_READ

- ID: `ACT_READ`
- Subject: `MASHIRO`
- Action: `Reads the three-line reply, once, slowly`
- Intention: `To take in what has come back`
- Intensity: `Low, rising`
- Speed: `Very slow`

### Action Relationship

- Before: `— (the reply arrives from S44's waiting)`
- After: `ACT_UNKNOT`

## Action — ACT_UNKNOT

- ID: `ACT_UNKNOT`
- Subject: `MASHIRO`
- Action: `Something in her throat comes undone — no sound, no expression, a loosening`
- Intention: `None — the release arrives without her permission`
- Intensity: `CRITICAL (the emotional peak, expressed as a loosening)`
- Speed: `Held; the eyes barely move`

### Action Relationship

- Before: `ACT_READ`
- After: `ACT_SPEAK`

## Action — ACT_SPEAK

- ID: `ACT_SPEAK`
- Subject: `MASHIRO`
- Action: `Says the name, softly: ……ニジ`
- Intention: `To call her — and to notice how little of her is left`
- Intensity: `Medium, suppressed`
- Speed: `Slow, quiet`

### Action Relationship

- Before: `ACT_UNKNOT`
- After: `ACT_LAUGH`

## Action — ACT_LAUGH

- ID: `ACT_LAUGH`
- Subject: `NIJI`
- Action: `Laughs — へへ。もう、ほとんど空になった — the rainbow afterimage trembling`
- Intention: `To tell her, lightly, what is nearly done`
- Intensity: `Medium, warm`
- Speed: `A small laugh; the afterimage shivers`

### Action Relationship

- Before: `ACT_SPEAK`
- After: `— (cut on the outline)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close, hand-level and over-the-shoulder. Inside the futon with her`
- Lens Character: `Long-ish, shallow. Backgrounds fall away softly`
- Depth of Field: `Very shallow — often only the screen or the fingers are sharp`
- Camera Style: `Slow, deliberate, almost still. It drifts; it never whips or shakes`

## Camera Events

- **`[0:00–0:07]`** — Locked close on the screen: the three-line reply, in cold blue-white. No other movement. Optional: an imperceptibly slow push-in.
- **`[0:07–0:17]`** — A slow dolly in on the reply — the three lines, then the eyes reading them, word by word.
- **`[0:17–0:24]`** — Cut to her face, lit from below, almost to silhouette. The release without a sound. Static.
- **`[0:24–0:30]`** — Cut to ニジ's almost-faded outline inside the screen, laughing, the rainbow afterimage trembling. Cut on the outline.

---

# 11. MOTION

## Subject Motion

- Her fingers rest; the body holds; only the eyes move, reading, slowly
- The unknotting is not a motion but an absence — a loosening with no visible move
- ニジ's laugh is small: the rainbow afterimage shivers, blue → green → blue, thin and faint
- The reply is read once, slowly, then the eyes still

## Object Motion

- The phone does not move on its own. Ever
- Screen content changes by ordinary UI transitions only — a reply arriving. Nothing glitches, flickers, distorts, or behaves supernaturally
- The wall clock's second hand (out of focus behind) advances in discrete ticks

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion besides ニジ's afterimage
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand; the futon compresses under her`
- Inertia: `High for her body, near-zero for her fingers (at rest)`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by small precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Waiting (the reply, at last)
- ↓ The unknotting (無駄じゃ、なかった — without a word)
- ↓ Calling her (……ニジ — noticing how little is left)
- ↓ The last laugh (もう、ほとんど空になった — warmth and the approaching end)

## Emotional Events

- Event: `Reading the three-line reply` — Emotion: `The unknotting — not relief, but the proof that her time was not wasted` — Intensity: `CRITICAL — expressed as a loosening, not a face` — Timing: `≈0:12`
- Event: `……ニジ` — Emotion: `Calling her — and noticing how little of her is left` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:24`
- Event: `ニジ's laugh — もう、ほとんど空になった` — Emotion: `Warmth and the approaching end` — Intensity: `MEDIUM` — Timing: `≈0:26`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `The phone screen — cold blue-white, close, low, from below her face. The only key`
- Fill Light: `Almost none. Deep soft shadow fills everything the screen does not reach`
- Rim Light: `A very faint cool edge on her hair and shoulder from the screen's spill`
- Ambient Light: `Near-black indigo. The room is legible only where the screen reaches it`
- Color Temperature: `≈6500K screen against deep indigo. ニジ's rainbow, now thin and faint, is the only saturated hue`

## Lighting Events

- **`[0:00]`** — Screen already on, its light lying on her face from below.
- **`[0:07–0:17]`** — The reply's cold blue-white dominates; her face falls almost to silhouette as the camera closes on the text.
- **`[0:17–0:24]`** — Cut to her face, lit from below — the release without a sound.
- **`[0:24–0:30]`** — ニジ's faint afterimage lends the screen a thin, dim wash of color, trembling as she laughs. Cut on the outline.

---

# 14. AUDIO

## Dialogue

- 真白: 「……ニジ」 — soft, quiet
- ニジ: 「へへ。もう、ほとんど空になった」 — a small laugh, warm, from the screen

> No other speech. The reply is read, not spoken. No narration, no voice-over.

## Sound Effects

- The soft friction of fabric as she shifts, once, reading
- The wall clock's second hand, dry discrete ticks, faint throughout
- The room's deep quiet

## Environment

- Deep quiet night room tone, almost nothing. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, warm, ending. Never sinister, never sentimental`
- Emotional Function: `Hold the room's stillness under the reading. It thins as she reads, and is entirely gone by ニジ's laugh, leaving only room tone and the clock`

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

- Render the on-screen reply exactly, three lines: `ありがとう。 ／ ごめんね、返事、遅れて。――ちょっと、びっくりしちゃって。 ／ あのときのこと、ずっと、気にしてた。――元気そうで、よかった。`
- Let something in her throat come undone as she reads — no sound, no expression, a loosening
- Render ニジ present: 真白's own face one step younger, a rainbow afterimage **inside the screen only**, with an **almost-faded outline** (輪郭がほとんど消えかけ); she laughs, and does not cry
- End on ニジ's almost-faded outline, the rainbow afterimage trembling — 残る宛先は、あと、一つ. Cut on the outline

## MUST NOT（この1本の禁止・開示台帳 41–45 レンジより）

- **Do not show the middle-school friend's face or figure.** No face, no body, no silhouette of her — the reply is text only
- **Do not let ニジ stand in the room.** She exists only inside the screen, never at human scale
- **Do not make ニジ fully opaque, and do not let her vanish entirely** — her outline is almost faded, but still present
- **ニジ does not cry.** The laugh may carry a faint sadness, but no tears
- No additional on-screen text beyond the reply and the ordinary UI (no captions, no subtitles burned in)

## PREFER

- Framing the reply large, straight-on and held — legibility is the whole point here
- Silence over score at the unknotting
- Holds over movement; when in doubt, do less
- The room nearly empty; negative space over detail

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The imperceptible push-in during beat 1 may be omitted (a fully locked frame is equally correct)
- Music may be absent altogether

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear only inside the screen as an almost-faded outline (ledger 41–45 — outline almost gone), never at human scale, and she must not vanish or cry; the middle-school friend's face and figure must never be shown — the reply is text only. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M. Beats, deliberately uneven: [0:00–0:07] the screen lights and a three-line reply arrives — ありがとう。 ／ ごめんね、返事、遅れて。ちょっと、びっくりしちゃって。 ／ あのときのこと、ずっと、気にしてた。元気そうで、よかった。; [0:07–0:17] 真白 reads it, once, slowly, and something in her throat comes undone, 無駄じゃ、なかった; [0:17–0:24] held on her face, the release without a sound, ニジ's outline almost gone; [0:24–0:30] ……ニジ — ニジ laughs, へへ。もう、ほとんど空になった, the rainbow afterimage trembling, 残る宛先は、あと、一つ, and the shot cuts on her almost-faded outline. The reading holds the largest share of the duration. Ends on the almost-faded outline, with nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: 真白's own face one step younger — longer lashes, slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — a blurred rainbow afterimage, drifting slowly blue → green → blue, existing only inside the screen, never in the room at human scale, no shadow. Her outline is almost faded away (輪郭がほとんど消えかけ): the afterimage thin and faint, barely there, on the verge of dissolving. The phone screen shows an ordinary Japanese UI in cold blue-white — a three-line reply reading exactly ありがとう。 ／ ごめんね、返事、遅れて。――ちょっと、びっくりしちゃって。 ／ あのときのこと、ずっと、気にしてた。――元気そうで、よかった。 No face, no figure, no body of the middle-school friend — the reply is text only. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. The fingers rest; the body holds; only the eyes move, reading slowly. The unknotting is not a motion but an absence — a loosening with no visible move. ニジ's laugh is small: the rainbow afterimage shivers, blue → green → blue, thin and faint. Ordinary weight and inertia: the phone has heft, the futon compresses. Gentle acceleration everywhere. The phone never moves by itself and never glitches, flickers or distorts; its screen changes only by ordinary UI transitions — a reply arriving. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close, hand-level and over-the-shoulder throughout — inside the futon with her. Longish lens, very shallow depth of field; often only the screen or the fingers are sharp. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:07] locked close on the screen, the three-line reply, optionally an imperceptibly slow push-in. [0:07–0:17] a slow dolly in on the reply, then the eyes reading word by word. [0:17–0:24] cut to her face lit from below, the release without a sound, static. [0:24–0:30] cut to ニジ's almost-faded outline inside the screen, laughing, the rainbow afterimage trembling; cut on the outline.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, faint throughout. Soft futon fabric as she shifts, once, reading. Two lines of dialogue: 真白 says softly ……ニジ; ニジ answers from the screen with a small warm laugh, へへ。もう、ほとんど空になった. The reply is read, not spoken. No narration, no voice-over. Music extremely sparse — a few sustained tones at most — thinning as she reads and entirely gone by ニジ's laugh, leaving only room tone and the clock. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no face of the middle-school friend, no figure of the middle-school friend, no body of the middle-school friend, no depiction of the middle-school friend as a person, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no watermark, no morphing or drifting facial identity, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no narration, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep10-seg05-30s-01`
- Segment ID: `S45`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_10, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 10s / 7s / 6s. Reading = BEAT 2 at 10s (33%)`
- Camera Events: `4 events as listed in §10. One slow dolly; all else static or cut`
- Action Events: `ACT_READ → ACT_UNKNOT → ACT_SPEAK → ACT_LAUGH`
- Audio Events: `two lines of dialogue ／ clock ticking throughout ／ music gone by ニジ's laugh`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the almost-faded outline`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Japanese text rendering.** The three-line reply carries the episode's whole meaning. If it renders as noise the segment fails. Check first; if unusable, generate the screen as a plate and composite the text in post.
- **The unknotting may not read.** It is a loosening, not a smile or a tear. If her face resolves into an expression, the restraint breaks. Hold the face still; the release lives in the stillness.
- **The model may draw the middle-school friend.** "A reply from an old friend" is a strong prior for a portrait. The negative prompt front-loads this; verify frame by frame — no face, no figure, text only.
- **ニジ must not vanish or cry.** Her outline is almost faded but still present, and she laughs without tears. If she dissolves entirely or weeps, the episode inverts.

## Changes

- _(none yet)_

## Next Generation

- If the reply and ニジ's almost-faded outline both read, this is the episode's pull: 残る宛先は、あと、一つ — the single remaining name that carries into episode 11 and 湊.
