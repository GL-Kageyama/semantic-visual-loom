# Wan 3.0 Full Specification — 受け火 第2章 S04「指が止まる」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../ukebi-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（対応表・開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（送り火・結城文）・定型句のみ日本語。
> この1本の個性：**指＝綴じる（淀みない→止まる）＋結城文のペンだこの魂火と「読んで」＋花の不在＋三人称制限＋白紙の頁と一番下の白い欄＋定型句（指示先は結城文）**。

---

# 1. VIDEO

## Basic

- Duration: `30s`
- Aspect Ratio: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`

## Generation Intent

- Purpose: `Fold one chapter (one organ, one reversal) of an 11-chapter short-story cycle into a single 30-second take that ends on its pull`
- Register: `Restrained and spare. Emotion is never named — it surfaces through the body (a hand stopping, a throat that will not swallow, a scale that will not tilt). The horror and the tenderness both live in ordinary objects and withheld action`
- Rule: `One organ = one turn. The arc is distributed across 12 takes; nothing is added after the pull`

---

# 2. WORLD

## World Concept

- Concept: `A boundary at a railroad crossing that leads nowhere, where a nameless man sends the dead to the other world with eight organs of his own body — each organ a verb: hands that send, fingers that bind, a throat that swallows, arms that hold, ears that measure, eyes that price, a voice that mourns, a back that discards`
- Era: `Timeless — the dead of every era mingle at the same crossing`
- Location: `A railroad crossing whose rails reach no station, no town; a barrier raised that never lowers`
- Time: `Time does not flow. There is no morning; only the hour work begins`
- Weather: `No rain falls, yet the air is damp; every sound is far away`
- Atmosphere: `Sparse, still, low-saturation deep indigo and rust red, lit only by the pale blue-white soul-fires`

## World Rules

- **The fundamental law** — all sending is preceded by being received. 送り火 only sends, and has never himself been received.
- **Eight organs = eight verbs.** One soul is processed by one organ with one verb. No organ hesitates; no motion doubts.
- **The supernatural is never performed, only recorded.** Its evidence is the world's own objects — the ledger, the scale, the seal — and the pale blue-white soul-fire. Nothing else.
- **The soul-fire is the sole light source.** The physical world does not react — no wind, no moving shadows, nothing stirred. All sound is distant except the dry rustle of the ledger's page.
- **Fragments of the living world (the Bon festival, summer) are only hinted at, never drawn in.**

## Visual Language

- Art Direction: `Soft cel anime — flat color planes, clean closed thin lineart, soft-edged shadow terminators`
- Color Language: `Muted, low-saturation. The world is deep indigo and rust red. The soul-fire's pale blue-white is the only bright value — and the only light source. The fire is pale blue-white yet reads red, wavering between blue and red`
- Texture: `No grain, no paper texture, no painterly stroke. Clean flat surfaces. Things read damp though dry — the rust's red, the air`
- Rendering: `Two-step cel shading with softened terminators; faint haze in the damp air; the soul-fire glows without bloom or lens flare`
- Visual Density: `Low. One focal point per beat. Generous negative space. Nothing is crowded`

---

# 3. SUBJECTS

## 送り火 (OKURIBI)

- ID: `OKURIBI`
- Name: `送り火 (nameless)`
- Type: `CHARACTER`
- Role: `Protagonist — lord of the boundary; an apparatus that sends souls to the next world through eight organs`

### Appearance

- A plain, unremarkable man, neither young nor old — nothing about him draws the eye. Namelessness itself is his appearance.
- Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat.
- Open scooping hands — hands made to scoop, that have never been scooped.
- No mark on his forehead (the seal appears only from S08).

### Behavior

- Personality: `Does not name; quiet. Does not name emotion. Has nothing that could be called an answer`
- Typical Motion: `Only the eight-organ ritual moves; everything else is near-still`
- Emotional Range: `Suppressed. No readable emotion on the face. Response appears as stillness — a hand that stops, a throat that will not move`

### Continuity Requirements

- Must preserve: `face, hair, build, age, the dark-indigo coat, and the namelessness (nothing about him draws the eye)`

## 結城文 (YUKI)

- ID: `YUKI`
- Name: `結城文`
- Type: `SUBJECT (a soul of the dead)`
- Role: `The guest soul to be sent — a writer who was never once read`

### Appearance

- A pale blue-white fire, **not human-shaped**, with a pen callus hard in the flame.
- Inside the fire: a writer's hand that wrote and was never read.
- Pale blue-white yet red at once, wavering between blue and red. It sways before the ledger as if wanting to turn pages.

### Behavior

- Sways before the ledger — a fire written and never read, waiting to be bound.
- It speaks a single word to 送り火: 「読んで」 — read me.

---

# 4. ENVIRONMENT

## Location

- ID: `CROSSING`
- Name: `踏み切り (the railroad crossing)`
- Description: `A crossing whose rails reach no station and no town, no one ever crossing; rust-red rails; a barrier raised that never lowers. The raised barrier's shadow falls black across the track. No rain falls, yet the air is damp and every sound is far away. Time does not flow`

## Environment Elements

- `線路` (the rails) — rust red; the rails run onward toward the current into which the souls are sent; the far side grows faintly lighter
- `台帳` (the ledger) — dry paper; each turned page rasps かさり, the only sound at the boundary; souls' names are entered line by line; the last row is always blank

## Environmental Behavior

- Wind: `none`
- Particles: `only the faintest haze in the damp air — no dust motes, no floating lights, no VFX`
- Background Motion: `almost none; time does not flow`
- Sound: `all distant except the dry rustle of the ledger's page`

---

# 5. OBJECTS

## 魂火 (TAMABI) — 結城文's fire

- Type: `light / soul`
- Appearance: `a pale blue-white fire, not human-shaped, with a pen callus hard in the flame, wavering between blue and red`
- Function: `the sole light source; inside it is a whole life — a writer written and never read`
- Narrative Importance: `CRITICAL`
- Visual Importance: `HIGH`
- Continuity Importance: `CRITICAL`

## 台帳 (the ledger)

- Type: `book`
- Appearance: `dry white paper, ink characters; one line bears the name 結城文; the bottommost slot is always blank`
- Material: `paper`
- Function: `binds the names; the name 結城文 is written with the one close sound; closing is binding`
- Narrative Importance: `HIGH`
- Visual Importance: `MEDIUM`
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
- Source: `soul-voice-teller/examples/ukebi/草稿/draft_02_綴じる.md`
- Priority: `CRITICAL`
- Defines: `every event, the exact on-screen text, the ending line, and what is and is not revealed`

## REF_BIBLE

- Type: `BIBLE`
- Source: `soul-voice-teller/examples/ukebi/台帳/series-bible.md`
- Priority: `CRITICAL`
- Defines: `the staged disclosure, the voice rules, and the organ ledger`

---

# 7. NARRATIVE

## Core Event

A man binds each soul's name into a single page before sending it. His fingers bind; then, touching a blank page and hearing 「読んで」, they try to read — and, unable to, stop. Binding fingers that come to know "reading" for the first time.

## Beginning

There is a ledger at the crossing. The paper is dry; every page turned makes a かさり — the only sound in a soundless place. A writer's soul-fire arrives — 結城文, with a pen callus on the finger; a fire that sways as if wanting to turn pages.

## Turn

送り火 moves his fingers — the second of the eight organs. He opens the ledger, binds the soul into a page; the pen records the name 結城文 in a single line, and the ink sinks into the paper. The bottommost slot of the ledger is always blank — the fingers have never once bound it. The bound page is closed. Closing is binding. No one opens it.

## Peak

The fingers touch the first page. It is blank — not only the bottommost slot. 「読んで」, 結城文's fire says. He tries to read it. He cannot. He has fingers that bind, and no fingers that read. The blank page trembles under his fingers; the かさり sounds like it is trembling. His binding fingers come to want to know "reading" for the first time.

## Pull（引き — 切れ目）

The fingers stop. One blank page still trembles under them. Cut on the stopped fingers. The 定型句: この魂は、まだ誰にも名付けられていない。

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The stopping holds 11s (37%) to fix the halted fingers.

## Temporal Units

- BEAT — a held third-person gaze over a single stretch of the crossing.

## Temporal Sequence

- **BEAT 1 `[0:00–0:07]` — 「台帳」 — ESTABLISH.** The ledger, dry paper, at the crossing. 結城文's soul-fire arrives — a pen callus, a fire that sways as if wanting to turn pages. _Density: SPARSE — a long held establishing, almost no event._
- **BEAT 2 `[0:07–0:14]` — 「綴じる」.** The fingers open the ledger, bind the soul into a page; the pen records 結城文 in one line, ink sinking into paper. The bottommost slot stays blank. The page is closed. _Density: TRANSITION — the ritual, unhesitating, then a close._
- **BEAT 3 `[0:14–0:19]` — 「読んで」.** The fingers touch the first page — it is blank, not only the bottom slot. 「読んで」, the fire says. _Density: DENSE — the blank page and the single word._
- **BEAT 4 `[0:19–0:30]` — 「止まる」 — CORE, longest share.** He tries to read; he cannot. Binding fingers, no reading fingers. The blank page trembles; the かさり trembles with it. The fingers stop. The 定型句. Cut. _Density: HELD — the stop, then the whisper, then a clean cut._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the fingers stopping (0:19–0:30) ／ 「読んで」(≈0:17) ／ the name 結城文 recorded (≈0:12)`

## Temporal Density

- Sparse regions: `0:00–0:07 (the ledger), 0:19–0:30 (the stop)`
- Dense regions: `0:14–0:19 (the blank page, 「読んで」)`
- Long continuous action: `0:19–0:30 the fingers, trying to read, then still`
- Rapid transitions: `none — a slow, held third-person gaze`

---

# 9. ACTION

## Action — ACT_ARRIVE

- ID: `ACT_ARRIVE`
- Subject: `YUKI (結城文's soul-fire)`
- Action: `Arrives before the ledger, swaying as if wanting to turn pages, a pen callus hard in the flame`
- Intention: `Not flight — waiting. A fire written and never read`
- Intensity: `Low`
- Speed: `Slow, weightless, swaying`

### Action Relationship

- Before: `—`
- After: `ACT_BIND`

## Action — ACT_BIND

- ID: `ACT_BIND`
- Subject: `OKURIBI (送り火)`
- Action: `The fingers open the ledger, bind the soul into a page; the pen records 結城文 in one line; the bottommost slot stays blank; the page is closed`
- Intention: `The ritual — unhesitating, practiced; closing is binding`
- Intensity: `Low, unvarying`
- Speed: `Steady, practiced, each gesture distinct`

### Action Relationship

- Before: `ACT_ARRIVE`
- After: `ACT_TOUCH_BLANK`

## Action — ACT_TOUCH_BLANK

- ID: `ACT_TOUCH_BLANK`
- Subject: `OKURIBI (送り火)`
- Action: `The fingers touch the first page — blank, not only the bottom slot. 「読んで」, the fire says`
- Intention: `Unlooked-for — the fingers that bind now meet a page with nothing to bind`
- Intensity: `Medium, quiet`
- Speed: `Slow; the touch is a halt in itself`

### Action Relationship

- Before: `ACT_BIND`
- After: `ACT_STOP`

## Action — ACT_STOP

- ID: `ACT_STOP`
- Subject: `OKURIBI (送り火)`
- Action: `The fingers try to read, and cannot; the blank page trembles under them; the fingers stop`
- Intention: `None. The stop is not chosen — binding fingers, coming to want "reading", and failing`
- Intensity: `Low, a held stillness`
- Speed: `Slow settle, then a complete halt`

### Action Relationship

- Before: `ACT_TOUCH_BLANK`
- After: `— (cut on the stopped fingers)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Third-person limited, close beside 送り火 — inside his silence, not his first person`
- Lens Character: `Close, over the page; the fingers and the paper are the subjects`
- Depth of Field: `Very shallow — the fingers, the page, and the ledger line are sharp; the crossing falls away`
- Camera Style: `Slow, deliberate, nearly still. It waits over the page; it never whips or shakes`

## Camera Behavior

`Static with slow drift. No pan, no whip, no handheld. One continuous take; no cut until the final.`

## Camera Events

- **`[0:00–0:07]`** — Wide to medium: the ledger on its stand, dry paper; 結城文's fire swaying before it, a pen callus hard in the flame.
- **`[0:07–0:14]`** — Close on the fingers and the page: open, bind, record 結城文 in one line of ink; the bottommost slot stays blank; the page closes.
- **`[0:14–0:19]`** — Close on the fingers touching the first page — blank. Hold on the blankness; 「読んで」 comes over it.
- **`[0:19–0:30]`** — The fingers settle over the blank page, trying to read; they stop. Hold on the stopped fingers and the trembling page. Cut.

---

# 11. MOTION

## Subject Motion

- The fingers carry essentially all the movement; the rest of the body holds.
- Open, bind, record, close — practiced, unhurried, without hesitation.
- The stop is a slow settle, then a complete halt; the fingers do not close, they only stop.
- 結城文's fire sways before the ledger, as if wanting to turn pages.

## Object Motion

- The ledger's dry page turns with a かさり — the only sound in the crossing.
- The blank page trembles under the fingers; the かさり sounds like it is trembling.
- The barrier stays raised and still.

## Environmental Motion

- No wind, no dust, no particles. The faintest haze in the damp air.
- Nothing else moves; time does not flow.

## Physical Characteristics

- Weight: `The page is dry and light; it trembles, but does not lift. The fire has no weight`
- Inertia: `High for the body, near-zero for the fire and the page`
- Acceleration: `Gentle everywhere; the stop is the only abrupt thing, and it is stillness, not a snap`
- Fluidity: `Limited-animation — holds punctuated by small precise gestures`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Stillness (the ledger, the swaying fire)
- ↓ Routine (open, bind, record, close — the unhesitating ritual)
- ↓ Unlooked-for (a blank page, a single word: 読んで)
- ↓ The stop (binding fingers that come to want "reading", and cannot)

## Emotional Events

- Event: `The name 結城文 recorded, the bottommost slot blank` — Emotion: `Routine without ceremony — one more name, one more blank slot beneath it` — Intensity: `LOW` — Timing: `≈0:12`
- Event: `「読んで」` — Emotion: `Unlooked-for — the fingers that bind now meet a page with nothing to bind` — Intensity: `MEDIUM, entirely internal, in the held fingers` — Timing: `≈0:17`
- Event: `The fingers stop` — Emotion: `The stop — binding fingers, coming to want "reading", and failing (the 定型句's reference here leans toward 結城文's soul)` — Intensity: `LOW, a held stillness` — Timing: `≈0:24`

---

# 13. LIGHTING

## Base Lighting

- Key Light: `結城文's soul-fire — pale blue-white, the only light and the only bright value`
- Fill Light: `Almost none. Deep indigo shadow fills everything the fire does not reach`
- Rim Light: `A very faint cool edge on the fingers and the page from the fire's spill`
- Ambient Light: `Near-black indigo and rust red; the page catches the light faintly`
- Color Temperature: `Cold blue-white against deep indigo and rust red, with the pen callus hard in the flame`

## Lighting Events

- **`[0:00]`** — The ledger under the damp dark, the fire the only light, swaying before the page.
- **`[0:07–0:14]`** — The page catches the light as the fingers bind; 結城文 in ink, then the page closes into shadow.
- **`[0:14–0:19]`** — The blank page, lit from the side, its emptiness the frame's only bright surface.
- **`[0:19–0:30]`** — The light wavers faintly as the page trembles; the fingers stop in the shadow. Hold. Cut.

---

# 14. AUDIO

## Dialogue

> **The fire's voice** (結城文's soul-fire): `読んで` — Japanese, character-for-character, near and far. **The 定型句** (境の地の声, near-and-far whisper): `この魂は、まだ誰にも名付けられていない。` as the pull. 送り火 does not speak — he has no reading voice.

## Sound Effects

- The かさり — the dry rustle of the ledger's page, the only sound in the crossing. It turns once as the name 結城文 is written; then it trembles, the かさり sounding like it is trembling.
- All else is far: no footsteps, no breath, no wind.

## Environment

- The damp near-silence of a soundless place, broken only by the page's かさり.

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, tender without sentiment. Never sinister`
- Emotional Function: `Hold the stillness under the かさり; it may thin toward the close, leaving only the whisper and the trembling rustle`

---

# 15. CONTINUITY

> 12本は12回の独立した生成である。モデルは前の話を覚えていない。以下の identity lock は §18 プロンプトへ毎回まるごと書き込まれる。

## Identity（must remain consistent）

- 送り火 — a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye. Dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat. Open scooping hands. No mark on his forehead.
- The stage — a railroad crossing, rust-red rails leading nowhere, a raised barrier that never lowers, air damp though no rain falls.

## Visual Continuity

- **The light law** — the soul-fire's pale blue-white is the only light and the only bright value; everything else is deep indigo and rust red.
- **The palette law** — muted, low-saturation everywhere; the pale blue-white soul-fire is the only bright value.

## Motion Continuity

- **The motion law** — limited animation, holds, twos and threes; almost all movement belongs to the organ's gesture.

## Sound Continuity

- **The sound law** — no sound except the dry rustle of the registry's page.

---

# 16. CONSTRAINTS

> 共通不変部の MUST/MUST NOT は series-constants §16 相当。ここには**この1本に固有**の制約のみ。

## MUST

- Establish the fingers' ritual — open, bind, record, close — practiced and unhesitating, before the stop.
- Render the on-screen Japanese exactly: the ledger's one line `結城文` and the blank bottommost slot (character-for-character; the slot shows no writing).
- Keep the soul-fire the sole light source.
- End on the fingers stopping over the trembling blank page, cut on the stopped fingers.

## MUST NOT（この1本の禁止・開示台帳 01–04 レンジより）

- **No 花 — no girl, no schoolgirl, no sailor uniform, no long dark hair, no second person, no female figure, no silhouette of another person, no reflection of a girl.**
- No human form in the fire — 結城文 is pale blue-white fire with a pen callus, not a man's figure.
- No on-screen text other than the ledger line `結城文` (the blank page shows no writing).

## PREFER

- Silence over score.
- The fingers and the page as the sole subjects of the frame.
- Negative space over detail.

## ALLOW

- Slight variation in the ledger's binding, the exact line of the ink, the fire's sway.
- The かさり may be the only audible event in the whole segment.

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: 花 is absent — no girl, no silhouette, no reflection, no second figure. This outranks everything, including beauty.
2. **Identity stability** — 送り火's face must not drift across the take.
3. **The exact Japanese** — the on-screen ledger line `結城文`, the blank bottommost slot, and the dialogue `読んで` are evidence; unreadable or altered, the work fails.
4. **The uneven density** — the fingers' stop (the take's spine) must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar, no sentimentality.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a nameless man whose fingers bind the dead into a ledger. Identity: a plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No girl anywhere. Beats, deliberately uneven: [0:00–0:07] the ledger at the crossing, dry paper, and a writer's soul-fire — 結城文 — swaying before it with a pen callus hard in the flame; [0:07–0:14] the fingers open the ledger, bind the soul into a page, and the pen records 結城文 in one line of ink, the bottommost slot staying blank; [0:14–0:19] the fingers touch the first page — it is blank, not only the bottom slot — and the fire says 読んで; [0:19–0:30] he tries to read and cannot — binding fingers, no reading fingers — the blank page trembles, the fingers stop, and the pull whispers この魂は、まだ誰にも名付けられていない。 Cut on the stopped fingers. The stop holds the largest share of the duration. Ends on the 定型句.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the soul-fire, light haze in the damp air, muted low-saturation palette, generous negative space, one focal point per beat. A plain, unremarkable adult man, neither young nor old, nothing about him draws the eye — dark indigo-black hair in a plain short cut, unremarkable features, a simple dark-indigo coat, open scooping hands. No girl, no schoolgirl, no sailor uniform, no long dark hair, no second figure, no female figure, no silhouette of another person, no reflection of a girl. A railroad crossing whose rust-red rails lead nowhere and a raised barrier that never lowers, air damp though no rain falls. The soul-fire is pale blue-white, not human-shaped, the only light and the only bright value; everything else is deep indigo and rust red. A dry ledger whose page bears one line of Japanese in ink — 結城文 — with the bottommost slot left blank. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise gestures, never continuous interpolation. Almost all movement belongs to the fingers and the fire; the body holds still. The fingers open the ledger, bind, record 結城文, and close the page in one practiced, unhurried sequence, without hesitation. Then the fingers settle over a blank page, try to read, and stop completely — the only abrupt thing is stillness, not a snap. The blank page trembles under the fingers; the かさり, the dry rustle of the page, sounds like it is trembling. 結城文's fire sways before the ledger as if wanting to turn pages. No wind, no dust, no particles, the faintest haze in the damp air; the barrier stays raised and still. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Third-person limited, close beside 送り火 — inside his silence, not his first person. Close, over the page; the fingers and the paper are the subjects. Very shallow depth of field; the fingers, the page, and the ledger line are sharp. Slow, deliberate, nearly still; the camera never whips or shakes. [0:00–0:07] wide to medium, the ledger on its stand, 結城文's fire swaying before it. [0:07–0:14] close on the fingers and the page — open, bind, record 結城文 in ink, the bottommost slot blank, the page closing. [0:14–0:19] close on the fingers touching the first page — blank; hold on the blankness as 読んで comes over it. [0:19–0:30] the fingers settle over the blank page, trying to read, then stop; hold on the stopped fingers and the trembling page; cut.

## Audio Prompt

Almost silent — the damp near-silence of a soundless place. The かさり, the dry rustle of the ledger's page, is the only sound: once as 結城文 is written, then trembling — the かさり sounding like it is trembling. A voice — 結城文's soul-fire, near and far: 読んで。 送り火 does not speak. Then the pull, the 定型句 in the boundary's own whisper: この魂は、まだ誰にも名付けられていない。 Music extremely sparse — a few sustained tones at most — thinning toward the close and leaving only the whisper and the trembling rustle. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no girl, no schoolgirl, no sailor uniform, no long dark hair, no second person, no female figure, no silhouette of another person, no reflection of a girl, no supernatural effects, no lens flare, no god rays, no floating particles, no glow bloom, no sparkle, no dramatic camera shake, no speed lines, no onomatopoeia, no English text, no captions, no narration text, no on-screen subtitles, no watermark, no jump scare, no horror sting, no exaggerated expression, no melodrama, no sentimentality, no named emotion on the face, no wind, no moving shadows, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain, no hard cel-shade with hard shadow edges

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `ukebi-ch02-seg01-30s-01`
- Segment ID: `S04`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_02, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 7s / 7s / 5s / 11s. The stop = BEAT 4 at 11s (37%)`
- Camera Events: `4 events as listed in §10. All third-person-limited holds over the page`
- Action Events: `ACT_ARRIVE → ACT_BIND → ACT_TOUCH_BLANK → ACT_STOP`
- Audio Events: `結城文's voice ／ the かさり (the only sound) ／ 定型句 (境の地の声) ／ near-silence`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the stopped fingers`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The stop may read as a flinch.** It must be a complete, unhurried halt — a slow settle, then stillness. If it reads as a twitch, slow the settle.
- **The ledger line 結城文 may render as noise.** It is evidence — character-for-character. If unusable, tighten the shot on the page; the name must read, and the bottommost slot must stay visibly blank.
- **Identity drift.** 送り火's face may shift across the take. §15 is the defense.
- **The model may add a figure.** The negative prompt front-loads `no girl, no second person`; verify frame by frame.

## Changes

- _(none yet)_

## Next Generation

- If the stop reads, S05 turns to the throat that will not swallow — where the girl first appears.
