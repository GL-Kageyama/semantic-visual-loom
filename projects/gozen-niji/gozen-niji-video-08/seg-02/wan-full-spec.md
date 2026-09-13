# Wan 3.0 Full Specification — 午前二時に、あなたは誰の時間を生きていますか 第8話 S33「受け取らなかった感情」/ 30s

> 貼り付け用の**自己完結したフル仕様（§1–§20）**。§1–6・§15・§17・Negative（共通不変部）は [series-constants](../../gozen-niji-video-00-series/series-constants.md) から、§7–20 は [wan-spec.md](wan-spec.md) から、この1本に**そのまま貼れる形**へ統合したもの。
> 設計ノート（§0 対応表・§0.5 画面文字一覧・指の所作・ニジ開示台帳・「転」）は含まない。WAN 3.0 へ渡すのはこのファイルだけでよい。
> プロンプト本文は英語。画面文字・台詞・固有名（真白・ニジ・美月）のみ日本語。
> この1本の個性：**「受け取らなかった感情」の定義——ニジが自分の手を見て、指がわずかに透ける（指の背骨の第33本・透明化の第一度）。ニジは在る（画面の中だけ・指だけがわずかに透ける）。登場人物は真白とニジのみ。画面文字なし。二人もカメラも音楽も、その手に言及しない。**

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

ニジ names what she is made of — the feelings other people aimed at 真白 that she never received — and while she speaks, she looks at her own hand: the fingers are faintly transparent.

## Beginning

The room, still dark. ニジ begins to list it, evenly, like a count: 「いいねを押した時間。既読を付けた時間。おまえが誰かの投稿を見てた時間。」 Each one a moment 真白 has lived.

## Turn

「そのひとつひとつに、おまえに向けられた感情が、あったんだよ。」 And then, the ones that did not land: 既読無視した、小春の不安 — a read receipt left on a consultation. 「おまえは受け取らなかった。届いたのに、受け取らなかった。」

## Peak

ニジ looks at her own hand. The thin fingers are slightly transparent — the dark showing faintly through them. She says nothing about it. Then, evenly: 「わたしは、おまえの分身でも、理想像でもない。——わたしは、おまえが受け取らなかった、人の感情の結晶。」

## Pull（引き — 切れ目）

Hold on the hand, the fingers faintly transparent, the definition still in the air. Neither of them remarks on it. Cut on the hand. Nothing after it.

> These narrative stages do not require equal duration.

---

# 8. TEMPORAL STRUCTURE

> **Deliberately non-uniform.** The transparent hand holds 10s (33%).

## Temporal Sequence

- **BEAT 1 `[0:00–0:06]` — 「挙げる」 — ESTABLISH.** Dark bedroom. ニジ lists it evenly: いいねを押した時間。既読を付けた時間。おまえが誰かの投稿を見てた時間。 Each a moment 真白 has lived. _Density: SPARSE — quiet speech, no event yet._
- **BEAT 2 `[0:06–0:14]` — 「受け取らなかった」.** ニジ: そのひとつひとつに、おまえに向けられた感情が、あったんだよ。既読無視した、小春の不安。…おまえは受け取らなかった。届いたのに、受け取らなかった。真白 remembers — 返事を打っては消した夜。既読を付けたまま閉じた画面。 _Density: TRANSITION — the mechanism lands; a quiet recognition._
- **BEAT 3 `[0:14–0:24]` — 「透ける指」 — PEAK, longest share.** ニジ raises her own hand in front of her face and looks at it. The fingers are faintly transparent — the dark showing through them. Neither says a word about it. The camera does not emphasize it. Over this: わたしは、おまえの分身でも、理想像でもない。――わたしは、おまえが受け取らなかった、人の感情の結晶。 _Density: DENSE, then a long HOLD on the hand._
- **BEAT 4 `[0:24–0:30]` — 「結晶」.** Hold on the hand, fingers faintly transparent. The definition hangs. 真白 says nothing. Cut on the hand. Nothing after it. _Density: HELD — then a clean cut on the pull._

## Timing Policy

- Timing Mode: `STRUCTURED`
- Distribution: `NON_UNIFORM`
- Priority Events: `the list of times (≈0:03) ／ 届いたのに、受け取らなかった (≈0:11) ／ the fingers faintly transparent (≈0:15, then held)`

## Temporal Density

- Sparse regions: `0:00–0:06 (the list), 0:24–0:30 (the held hand)`
- Dense regions: `0:14–0:24 (the transparent fingers + the definition)`
- Long continuous action: `0:14–0:24 the hand held up, looked at, unremarked`
- Rapid transitions: `none — a slow, still night`

---

# 9. ACTION

## Action — ACT_LIST

- ID: `ACT_LIST`
- Subject: `NIJI`
- Action: `Lists the times, evenly, like a count — いいね・既読・誰かの投稿を見ていた時間`
- Intention: `To name the raw material before the conclusion`
- Intensity: `Low, measured`
- Speed: `Steady, unhurried`

### Action Relationship

- Before: `—` (continues from S32's 「そのままの意味だよ」)
- After: `ACT_RECOGNIZE`

## Action — ACT_RECOGNIZE

- ID: `ACT_RECOGNIZE`
- Subject: `MASHIRO`
- Action: `Remembers — 返事を打っては消した夜。既読を付けたまま閉じた画面。 Her eyes drop`
- Intention: `To recognize her own history in what she is being told`
- Intensity: `Medium, internal`
- Speed: `Slow, and stilling`

### Action Relationship

- Before: `ACT_LIST`
- After: `ACT_LOOK`

## Action — ACT_LOOK

- ID: `ACT_LOOK`
- Subject: `NIJI`
- Action: `Raises her own hand in front of her face and looks at it, calmly, the way one checks whether something is dirty`
- Intention: `None stated — she does not react to what she sees`
- Intensity: `CRITICAL (the emotional peak, expressed as an unremarked fact)`
- Speed: `Slow, then held`

### Action Relationship

- Before: `ACT_RECOGNIZE`
- Simultaneous With: `Her own line, spoken evenly — the definition of herself`
- After: `ACT_HOLD`

## Action — ACT_HOLD

- ID: `ACT_HOLD`
- Subject: `NIJI`
- Action: `Keeps the hand up, fingers faintly transparent, and keeps talking — she never acknowledges it`
- Intention: `To continue the answer as if nothing had changed`
- Intensity: `Medium, steady`
- Speed: `Held; only the rainbow drifts`

### Action Relationship

- Before: `ACT_LOOK`
- After: `— (cut on the hand)`

---

# 10. CAMERA

## Camera Language

- Perspective: `Close and level, through the glass into the screen, at the edge where 真白 sits`
- Lens Character: `Long-ish, shallow. The room falls away into soft indigo`
- Depth of Field: `Shallow — ニジ's hand and face sharp, the room soft behind`
- Camera Style: `Slow, deliberate, nearly still. It never emphasizes the transparency — it simply does not leave`

## Camera Events

- **`[0:00–0:06]`** — Locked on ニジ inside the screen, listing the times. Static.
- **`[0:06–0:14]`** — Cut to 真白, lit from below, her eyes dropping as the mechanism lands. Then a slow return to ニジ.
- **`[0:14–0:24]`** — ONE LOCKED FRAME containing ニジ's hand and her face together. No push in, no rack focus, no reframe, no move of any kind — it simply stays while she looks at her hand and keeps talking.
- **`[0:24–0:30]`** — Hold on the hand, fingers faintly transparent. Cut on the hand.

---

# 11. MOTION

## Subject Motion

- ニジ's movement is small and complete — she raises one hand and looks at it, then holds
- 真白's body holds; her eyes drop once and then stay down
- The transparency has no physics — no shimmer, no flicker, no pulsing. A constant, quiet fact
- The rainbow drifts slowly: blue to green to blue

## Object Motion

- The phone does not move on its own. Ever
- Screen content is static except the rainbow's drift
- The wall clock's second hand advances in discrete ticks, out of focus behind

## Environmental Motion

- The screen's bloom breathes very slightly on the ceiling — the only continuous motion
- Nothing else in the room moves

## Physical Characteristics

- Weight: `Ordinary. The phone has heft in her hand; the futon compresses under her`
- Inertia: `High — the hand is the only movement, and it is slow`
- Acceleration: `Gentle everywhere; nothing snaps or jerks`
- Fluidity: `Limited-animation — holds punctuated by the smallest precise movements`
- Impact: `None. Nothing collides, falls, or strikes`

---

# 12. EMOTION

## Emotional Arc

- Recognition (the list of times — her own history, itemized)
- ↓ Dread, unnamed (届いたのに、受け取らなかった)
- ↓ The cost, unremarked (a hand, held up, faintly transparent)
- ↓ Stillness (the definition that does not land)

## Emotional Events

- Event: `届いたのに、受け取らなかった` — Emotion: `Dread, unnamed — the mechanism turning on her own choices` — Intensity: `MEDIUM, suppressed` — Timing: `≈0:11`
- Event: `The fingers, faintly transparent` — Emotion: `The cost, unremarked — neither character, nor camera, nor score acknowledges it` — Intensity: `CRITICAL, expressed as restraint` — Timing: `≈0:15, held to 0:24`
- Event: `わたしは…人の感情の結晶` — Emotion: `Stillness — the definition that does not land` — Intensity: `MEDIUM` — Timing: `≈0:20`

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
- **`[0:14–0:24]`** — The locked frame holds ニジ's hand and face together; where the fingers are transparent, the dark behind shows through — with no glow, no edge highlight, no shimmer. A constant, quiet fact of how they render.
- **`[0:30]`** — Cut on the hand. No flash, no dim, just the cut.

---

# 14. AUDIO

## Dialogue

- ニジ: 「いいねを押した時間。既読を付けた時間。おまえが誰かの投稿を見てた時間」 — even, like a count
- ニジ: 「そのひとつひとつに、おまえに向けられた感情が、あったんだよ」
- ニジ: 「既読無視した、小春の不安。……おまえは受け取らなかった。届いたのに、受け取らなかった」
- ニジ: 「わたしは、おまえの分身でも、理想像でもない。——わたしは、おまえが受け取らなかった、人の感情の結晶」

> ニジ uses 「わたし」 — calm, almost explanatory, the voice of someone stating what they are. She is **not crying**. No voice-over, no narration.

## Sound Effects

- Deep quiet night room tone, almost nothing
- The wall clock's second hand, dry discrete ticks, faint throughout
- Soft futon fabric, once, as 真白 shifts

## Environment

- Deep quiet night room tone. The kind of silence in which a clock gets louder

## Music

- Style: `Extremely sparse — a few sustained tones, or nothing at all`
- Tempo: `Very slow, or absent`
- Mood: `Suspended, unresolved. Never sinister, never sentimental`
- Emotional Function: `One low sustained tone may enter under the mechanism and hold, UNCHANGED, through the confession — it must not swell, brighten, or shift when the hand appears. It may stop before the cut. No horror strings, no sting`

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

- ニジ is **present** — inside the screen only, 真白's own face one step younger, a rainbow afterimage
- **Only the fingers are faintly transparent.** The rest of her is solid and opaque
- **Neither character, nor the camera, nor the score remarks on the transparency.** 真白's eyes stay on ニジ's face, not her hand
- ニジ uses 「わたし」; she states the definition evenly, without crying
- 真白 remembers her own history — 打っては消した夜、既読のまま閉じた画面 — as a held silence, not a reaction
- End by cutting on the hand, fingers faintly transparent, with nothing after it

## MUST NOT（この1本の禁止・開示台帳 S33–34 レンジより）

- **No full-body transparency.** The transparency is fingers-only, faint. No see-through torso, no see-through face, no fading figure, no dissolving, no disappearing
- **No flashy disappearance effect.** No dramatic fade-out, no dissolving into light, no particle burst, no spectacle of vanishing
- **No shimmer, no flickering transparency, no pulsing, no glowing edges on the hand**
- **Do not emphasize the hand.** No camera push on it, no music swell, no reaction shot, no gasp, no pointing, no character noticing it
- **No figure in the room, no other faces.** 真白 and ニジ are the only figures
- **No generic ghost.** ニジ is not a horror ghost — no ghostly glow, no spectral aura, no glowing eyes
- Do not have anyone cry or sob

## PREFER

- One locked frame over any emphasis; when in doubt, do less
- The viewer discovering the fingers before the story acknowledges them
- Silence over score at the moment the hand appears

## ALLOW

- Slight variation in the wall-clock design, futon pattern, room furnishing
- The music may be absent altogether
- ニジ's rainbow may drift slowly, blue to green to blue

---

# 17. GENERATION PRIORITIES

> 制約が衝突するとき、以下の順で優先する。

1. **The staged disclosure** — nothing may be revealed earlier than the ledger allows. For this segment: ニジ must appear inside the screen only, with only her fingers faintly transparent (ledger S33–34 — 在); no full-body transparency, no flashy disappearance, no emphasis on the hand. This outranks everything, including beauty.
2. **Identity stability** — 真白's face must not drift across a cut.
3. **The exact Japanese on-screen text** — it is the evidence; if it is unreadable the piece fails.
4. **The uneven density** — the turn of the take must visibly hold the largest share of the 30 seconds.
5. **Restraint** — no performed emotion, no horror grammar.
6. **The style** — flat cel planes, soft light, limited animation.
7. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 30-second continuous cinematic take (16:9), soft cel anime, of a high-school girl's quiet bedroom at 2:00 A.M., with a figure inside her phone screen. Beats, deliberately uneven: [0:00–0:06] the figure lists the times evenly, like a count — いいねを押した時間。既読を付けた時間。おまえが誰かの投稿を見てた時間; [0:06–0:14] it says each of those moments held a feeling aimed at her — そのひとつひとつに、おまえに向けられた感情が、あったんだよ — and then, 既読無視した、小春の不安。…おまえは受け取らなかった。届いたのに、受け取らなかった, and 真白 remembers the nights she typed and erased, the screens she closed read and unanswered; [0:14–0:24] THE PEAK — the figure RAISES ITS OWN HAND IN FRONT OF ITS FACE AND LOOKS AT IT, and ITS FINGERS ARE FAINTLY TRANSPARENT, the dark showing through them, only the fingers, the rest of it solid, and it says nothing about this and the girl says nothing about it and the camera stays in ONE LOCKED FRAME with no push and no music cue, while it says わたしは、おまえの分身でも、理想像でもない。――わたしは、おまえが受け取らなかった、人の感情の結晶; [0:24–0:30] hold on the hand, fingers faintly transparent, and cut on the hand. The transparent hand holds the largest share of the duration. Ends on the hand, nothing after it.

## Visual Prompt

Soft cel-shaded anime. Clean closed thin lineart, flat cel color planes shaded in two steps with soft-edged terminators, gentle bloom around the phone screen, light haze in the dark air, muted low-saturation palette, simple uncluttered room, generous negative space, one focal point per shot. 真白: same face, same shoulder-length dark hair, a thin neck, same slight build, same age 16–17, same curved posture over the phone. The same phone: identical size, shape and case. The same room: futon on the floor, curtained window, wall clock, sparse. The same lighting logic: at night the phone screen is the only light source, cold blue-white from below. The same palette: muted and low-saturation; only the screen is bright. The same restraint: her expression never resolves into a legible emotion. ニジ: inside the phone screen only — 真白's own face one step younger, longer lashes and slightly fuller cheeks, the same shoulder-length dark hair and thin neck, the same way of tilting her head — a rainbow afterimage, no shadow anywhere, fully opaque body and face, but her FINGERS ONLY faintly transparent so the dark of the room shows through them with no glow, no shimmer, no edge highlight and no flicker; never standing in the room at human scale. Night is deep indigo lit solely by the cold blue-white screen. No grain, no paper texture, no painterly stroke.

## Motion Prompt

Limited animation, shot on twos and threes — holds punctuated by small precise movements, never continuous interpolation. ニジ's movements are small and complete: she raises one hand in front of her own face and studies it calmly, the way one checks whether something is dirty, then keeps talking WITHOUT REACTING TO IT. 真白 does not react either; her eyes stay on ニジ's face, not on its hand. The transparency has no physics at all — no shimmer, no flicker, no pulsing, no fading in and out; it is a constant quiet fact of how the fingers render. The rainbow drifts slowly, blue to green to blue. Ordinary weight and inertia; the phone has heft, the futon compresses. The phone never moves by itself and never glitches, flickers or distorts. The wall clock's second hand advances in discrete ticks. Only the screen's bloom breathes faintly on the ceiling. No impacts, no collisions, no motion blur smears, no squash and stretch.

## Camera Prompt

Close and level, through the glass into the screen, at the edge where 真白 sits. Longish lens, shallow depth of field; ニジ's hand and face sharp, the room soft behind. Slow and deliberate, nearly still; the camera drifts and never whips or shakes. [0:00–0:06] locked on ニジ inside the screen, static, listing the times. [0:06–0:14] cut to 真白 lit from below, her eyes dropping, then a slow return to ニジ. [0:14–0:24] ONE LOCKED FRAME containing ニジ's hand and her face together — no push in, no rack focus, no reframe, no move of any kind; it simply stays while she looks at her hand and keeps talking. [0:24–0:30] hold on the hand, fingers faintly transparent; cut on the hand.

## Audio Prompt

Almost silent. Deep quiet night room tone. A wall clock's dry discrete ticking, faint throughout. Soft futon fabric, once, as 真白 shifts. Spoken lines only: ニジ lists the times evenly — いいねを押した時間。既読を付けた時間。おまえが誰かの投稿を見てた時間 — then そのひとつひとつに、おまえに向けられた感情が、あったんだよ, then 既読無視した、小春の不安。……おまえは受け取らなかった。届いたのに、受け取らなかった, then わたしは、おまえの分身でも、理想像でもない。――わたしは、おまえが受け取らなかった、人の感情の結晶. Her voice is calm, almost explanatory, using わたし; she is not crying. No narration, no voice-over. Music extremely sparse — one low sustained tone at most, holding UNCHANGED through the confession and not swelling when the hand appears, stopping before the cut. No horror strings, no sting, no swelling emotion.

## Negative Prompt

no fully transparent figure, no translucent body, no see-through torso, no see-through face, no fading figure, no dissolving, no disappearing, no vanishing, no full-body transparency, no flashy disappearance, no dramatic fade-out, no dissolving into light, no particle burst, no spectacle of vanishing, no shimmer, no flickering transparency, no pulsing, no glowing edges on the hand, no camera push on the hand, no music swell, no reaction shot, no gasp, no pointing at the hand, no character noticing the hand, no second person in the room, no full-body figure in the room, no figure stepping out of the phone, no ghostly glow, no spectral aura, no generic anime ghost girl, no spirit girl, no other faces, no supernatural effects, no glitch, no screen distortion, no flickering, no floating particles, no moving shadows, no wind, no jump scare, no horror sting, no distorted face, no screaming, no crying, no exaggerated shocked expression, no subtitles, no captions, no English text, no watermark, no narration, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no morphing or drifting facial identity, no scene cuts to unrelated locations, not photorealistic, no 3D render, no glossy webtoon gloss, no airbrush portrait rendering, no heavy gradient, no painterly brush strokes, no busy detail, no grain

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `gozen-niji-ep08-seg02-30s-01`
- Segment ID: `S33`
- Specification Version: `1.0.0`
- Generation Date: `2026-08-29`

## Resolved Values

- Duration: `30s`
- References: `REF_STYLE (soft-cel-anime, HIGH) ／ REF_SOURCE (draft_08, CRITICAL) ／ 共通不変部 (series-constants)`
- Temporal Structure: `4 beats, NON_UNIFORM — 6s / 8s / 10s / 6s. Hand = BEAT 3 at 10s (33%)`
- Camera Events: `4 events as listed in §10. One locked frame (0:14–0:24) that never moves`
- Action Events: `ACT_LIST → ACT_RECOGNIZE → ACT_LOOK → ACT_HOLD`
- Audio Events: `four lines of dialogue ／ clock ticking faint ／ no voice-over ／ music unchanged through the confession`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip, cut on the hand`

---

# 20. ITERATION

## Version

`1.0.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The whole figure goes translucent.** The most likely failure and the most damaging. The transparency is a curve across episodes, and this is its first degree — fingers only, faint. Verify frame by frame.
- **The transparency gets emphasized.** A push-in, a music swell, a reaction shot, a gasp. If any appear, regenerate — the restraint is the scene, and S34/S35 depend on this not being pointed at yet.
- **The fingers read as glowing.** They must show the dark through them with no glow, no edge highlight, no shimmer. A glow turns cost into spectacle.
- **The model may put her in the room.** ニジ never leaves the screen.
- **Identity drift.** Her face may shift across the take. §15 (in series-constants) is the defense.

## Changes

- _(none yet)_

## Next Generation

- If "only the fingers, faint" holds, consider generating the hand as a separate macro plate at the correct opacity and compositing it into the locked frame — the shot does not move, so a composite is clean.
