# Wan 3.0 Full Specification — 『ハビッツ！！！』碓氷千夏 キャラクタープロモーション 第一ショット「名が呼ばれ、返事が一拍遅れる」 / 5s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である
——**どちらも投入しない。**

⚠️ **この作品の §18 `Negative Prompt` は、五ショットで同一である。**
理由は豁免ではなく**設計**である——この二十八秒で**禁止が消える瞬間は一度も無い。**
禁止が消えれば、モデルが描いてよいものが増える。**この作品は、それを一度もしない。**
⚠️ **ゆえに `L14`（宣言を超えた区間）は、この作品で一度も鳴らない。**
**鳴らないのは、そう設計したからである。**
⚠️ **ショットごとに違うのは §16 の MUST ／ PREFER ／ ALLOW であって、MUST NOT ではない。**
⚠️ **`Style Motion` も五ショットで同一である**——7つのスロットのうち、これだけは仕様の外
（様式カード）から来る（`specmap.PROMPT_SLOT_SOURCE`）。**同一であることが正しい。**

⚠️ **人名はローマ字にしない**（決定）。プロンプトの中の「碓氷千夏」は**日本語の字のまま置く。**
ゆえに Negative は「**読める文字**」を禁じるのであって、**字種を禁じない**——
`no Japanese kanji or kana` は**使わない。使えば、名そのものが消える。**

⚠️ **開示の第一変化点である**（`ledger.yaml`）。ここで名が在る——**ただし、読めない。**
§18 `Negative Prompt` の `no legible name text` は、この変化点の**前から**在る（`bible.yaml` の
`negative_base`）。→ 台帳の宣言は **`covered`** である。
**変わらないことは、応答していないことではない。**

⚠️ **BGM は置かない**（著者指示 2026-09-18）。§14 と §18 `Audio Prompt` がそれを負う。
**指定による無音であって、省略による無音ではない**（`video-spec` の `avoid`）。

⚠️ **この作品は、動画と画像の二経路を持つ。**（決定 2026-09-18、著者。`bible.yaml`「画像の経路」）
画像の仕様は `specs/image/shot-01-called.md` に在り、**§1–20 を持たない**——
**1段落の `Prompt` と1段落の `Negative` である。**
⚠️ **画像の `Negative` は、このファイルの §18 `Negative Prompt` と同一である。**
   理由は三つある（画像仕様のヘッダ）——**とくに②が効く。画像はこの動画へ添付される。
   経路ごとに禁止が違えば、画像が許したものを動画が受け取る。**
⚠️ **この一致を読む検査は、いま無い**（`L21` は §18 を読まない）。**穴のまま記録する。**
⚠️ **§18 の七欄は、動画の仕様の持ち物である。** 画像の仕様は七欄を持たない。
⚠️ **人名はローマ字にしない**（上の決定）——**画像の `Prompt` の中の「碓氷千夏」も同じである。**

⚠️ **§2 の規則は、`bible.yaml` の日本語の規則の移し替えである。**
「一字も変えない」は**日本語の側の約束**であって、**写しの言語は英語である**
（`CLAUDE.md`——文書の正典は英語）。**食い違ったら、`bible.yaml` が勝つ。**

---

# 1. VIDEO

- Duration: `5s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: her head has not begun to move, and then the reply arrives one beat late. **The call itself is never in the mix.**

# 2. WORLD

## World Concept

2026, Japan. A public elementary school in Tokyo, and the staff room of it. There is no magic, no institution and no secret organization — there is only a daily life in which the etiquette of the written name is thoroughly in place. **The name is the subject of this work, and in this shot it enters the frame for the first time: present, and not readable.**

## World Rules

- **The people in the work do not know that they are inside a film.**
- **The hand comes first and the face comes after. The order is not swapped. The face is placed only after the name has been called.**
- **The sound is not a calling voice; it is the sound of paper and hands.**
- **Outside the work, for the first time, someone calls out. Inside the work it is never spoken. Being spoken outside does not cancel being unspoken inside. The cost is kept, not erased.**
- **This work places no one in frame but her.** The caller and the listener are outside the frame.
- **No text is burned into this work.**
- **No name is spoken in this work.** No voice is placed at all.
- **This work does not decide whether the four beats are the same day.**

## Visual Language

- Art Direction: Luminous realist anime — **the light, not the figure, is the subject.** Translated into an interior: a fluorescent ceiling light stands in for the style's low sun, and what the style does with sky it does here with a lit wall, a lit shoulder and the plastic of a nameplate.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The palette is narrow — fluorescent white, paper white, the warm side reduced to skin and to one small plastic highlight.
- Texture: Layered atmospheric depth from near to far; dust suspended in the air where the light catches it; no grain, no paper texture, no painterly stroke.
- Rendering: Hyper-detailed layered light — bloom around the tube, anamorphic flare only where the tube sits at the frame edge, particles individually rendered rather than a flat wash. Clean anime lineart on the figure, **kept deliberately subordinate to the light.**
- Visual Density: Low. One focal point, generous negative space.
- Time: `2026年の勤務日の日中` — a working day, daytime, fluorescent.
- Atmosphere: An office that is being worked in, and is not being watched.

# 3. SUBJECTS

## 碓氷千夏

- Reference: the frozen pair — `ChatGPT Image 2026年9月18日 20_29_36.png` (character sheet, revision 4) ＋ `ChatGPT Image 2026年9月17日 21_56_32.png` (expression sheet, revision 2). **Both are attached; neither is summarised.**
- Appearance: A woman of thirty-three. A washable shirt, and the school-designated nameplate at the left of the chest. ⚠️ **The source ledger records sex and age and the administrative facts of her life; it records no description of her appearance.** That absence is design, not a gap — so nothing about her face or build is invented here. **The face is the frozen image.**
- Behavior: She reads her own name with her fingers rather than with her eyes; she does not call anyone by name; her one consistent reaction is to ask, and she does not ask here. Her movement is small, slow, and does not complete.
- Continuity Requirements: **Must preserve** — the face and build of the frozen pair; the nameplate at the left of the chest; the shirt with no outer garment. **May change** — the angle of the head, the position of the hands, the fall of light across her.

# 4. ENVIRONMENT

- Location: `名札` — **the site of the naming, not a room.** Here it is the name she wears: the left of the chest, and the cloth over it.
- Environment Elements: The staff room exists only as light and surface behind and around her — the lit wall, the edge of a desk, the fluorescent tube at the frame's upper edge. Dust in the air.
- Environmental Behavior: The dust falls continuously through every beat. The light does not change colour; it holds. **The room is never the subject and never gains one.**

# 5. OBJECTS

- The nameplate — plastic, printed, worn at the left of the chest. Under the present layer there is an older layer of writing. **None of it is legible.**
- The pin — **not fastened, and it is not fastened here.**
- The shirt — washable cloth, thin enough to take the light at the shoulder.
- No other object is in frame.

# 6. REFERENCES

- REF_CHARACTER: the frozen pair (`20_29_36.png` ＋ `21_56_32.png`) (CRITICAL)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_STYLE: `luminous-anime` (HIGH)
- REF_SOURCE: `projects/habits-promo-chinatsu/bible.yaml` (CRITICAL)
- ⚠️ **No location board is referenced.** The site of the naming is a body and a cloth; there is no room asset to attach.

# 7. NARRATIVE

- Core Event: A name is called and the reply does not come with it.
- Beginning: Her back and half of her profile. She is doing something with her hands.
- Turn: The head begins to move.
- Peak: She has finished turning, and her mouth has still not opened.
- Pull: One beat, held, and the shot cuts. **The shot ends on the beat, not after it.**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-3s` — density: `sparse` — The staff room. Her back and half of her profile. The name is called; **the voice is not heard.** The head begins to move.
  - BEAT 2 `3-5s` — density: `held` — **She finishes turning. Her mouth does not open.** One beat. **This beat is the shot's subject.**
- Temporal Density: The held beat is the shorter one and carries the shot. **Length is not where the weight is.**

# 9. ACTION

- `ACT_TURN` — Before: the head has not moved. After: the head has finished turning. **The turn does not begin until the beat before it has been given.**
- `ACT_WITHHOLD` — Before: the mouth is closed. After: the mouth is still closed. **This is not the absence of an action; it is the action.**

# 10. CAMERA

- Camera Language: Third person, close, at her shoulder — the style's light-first hierarchy, with the figure filling much of the frame and the fluorescent tube at the upper edge as the source.
- Camera Events: One event only. `0-5s` — a very slow, weighted settle of a few centimetres, the camera placed rather than travelling. **Nothing is revealed by it.**
- Camera Behavior: No handheld, no whip, no shake, no cut, no push-in on the face. One continuous take.

# 11. MOTION

## Subject Motion

The head turns, small and slow — run-10: 「速度は遅い」. It completes the turn and stops. **The face arrives after the turn, not with it.**

## Object Motion

None. The nameplate moves only because she does.

## Environmental Motion

Dust falls continuously through both beats. The fluorescent light holds steady. Both keep moving after the subject has stopped — **that is what keeps this from being a still.**

## Physical Characteristics

- Weight: The head has weight; the turn decelerates into its stop rather than arriving.
- Inertia: The turn does not overshoot.
- Acceleration: One acceleration at the beginning of the turn, then a long deceleration.
- Fluidity: Continuous; no snap, no held cel, no stutter.
- Impact: None.

# 12. EMOTION

- Emotional Arc: The interval in which a name has arrived and an answer has not.
- Emotional Events: The instant the turn finishes and the mouth is still closed.

# 13. LIGHTING

- Base Lighting: Fluorescent ceiling light, at the upper edge of the frame or just outside it. The style's contribution is the falloff, not the sun: bloom at the tube, a lit wall behind her, deep cyan in the unlit half of the room, dust suspended in the light.
- Lighting Events: One — the light catches the plastic of the nameplate as the turn brings the left of the chest toward the lens, and stays there. **This is the only highlight that moves in the shot.**

# 14. AUDIO

- Dialogue: None. **The call is heard only on the side of the one called, and the audience is not that side.**
- Sound Effects: Paper and hands, at the edge of audibility — cloth, a chair, a drawer, a pen set down. Nothing is mixed forward.
- Music: **None.** No score, no BGM, no drone, no pad, no sting, no swell.
- Environment: An office interior. A fluorescent hum is permitted; a musical tone is not.

# 15. CONTINUITY

- Identity: The frozen pair, unsummarised, attached on every instance. No drift of face, build or costume.
- Spatial: The nameplate is at the left of the chest in every shot of this work. It is not moved for the camera.
- Temporal: This shot does not fix the date, and nothing in frame supplies one.
- Visual: The palette, the fluorescent key and the dust are the same in all five shots.
- Motion: Full animation, not limited. The atmosphere is the primary mover, and here the atmosphere is dust in fluorescent light.
- Sound: Paper and hands. No voice, and no music.

# 16. CONSTRAINTS

## MUST NOT

- No second person in frame — no caller, no listener, no colleague, no passer-by, no hand but hers.
- No legible text on any surface — on the nameplate, on paper, on a screen, on a wall. **The name exists in frame and is not readable.**
- No romaji in place of the Japanese name.
- No calling voice as a sound effect; no audible speech; no spoken name; no voice-over; no narration.
- No face before the name is called.
- No completed action, no finished movement, no resolved gesture.
- No smile, no tears, no fear, no pleading, no exaggerated expression.
- No wall clock, no calendar, no digital timer, no date stamp.
- No cardigan, no jacket, no blazer, no outer garment.
- No identifying clothing, hairstyle or prop; no signature; no handwriting by the subject.
- No uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations.
- No watermark, no on-screen subtitles, no captions.
- Not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces.

## MUST

- The turn completes and the mouth does not open. **The withheld reply is the shot.**
- The dust keeps falling after she has stopped.

## PREFER

- Her back and half of her profile in the first beat; the turn bringing the left of the chest, and the nameplate, toward the lens.

## ALLOW

- The fluorescent tube at the upper edge of the frame, blooming.

# 17. GENERATION PRIORITIES

1. **The withheld reply** — the mouth does not open. This outranks expression, beauty and legibility of feeling.
2. **No voice** — the call is not in the mix, and nothing takes its place.
3. **The name is not readable** — the nameplate is present and illegible. Either half of that failing is a different shot.
4. **One change only** — the turn, and the beat. Nothing else happens.
5. **The face arrives after the name** — the order is not swapped for a better frame.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 5-second continuous cinematic take (16:9), luminous realist anime, in the staff room of a Japanese public elementary school, 2026, at the left of 碓氷千夏's chest, where the nameplate is worn. Beats, deliberately uneven: [0-3s] her back and half of her profile, the head beginning to move — no voice in the mix at all; [3-5s] she finishes turning and her mouth does not open — one beat, held, and that beat is the shot. The face arrives after the name, never with it. The frame stays clean throughout — the room, the light, the dust and her, and nothing laid over the image. Dust falls through fluorescent light and keeps falling after she has stopped. Ends on the beat and cuts. (One take, one change: the turn, and the reply that does not come with it.)

## Visual Prompt

Luminous realist anime, translated into an interior: the light, not the figure, is the subject. A woman of thirty-three, identity locked to the frozen reference pair, wearing a washable shirt with the school-designated nameplate at the left of the chest and no outer garment. Clean anime lineart on the figure, kept subordinate to the light. Saturated where the light falls, deep cyan in the unlit half; a narrow palette of fluorescent white, paper white, with the warm side reduced to skin and one plastic highlight. Hyper-detailed layered light — bloom around the fluorescent tube at the upper edge of the frame, dust suspended and individually rendered, a lit wall behind her, generous negative space and low visual density. A plastic nameplate, its printed face lost to the key — the surface reads as plastic, and the printing washes out into it. The pin is not fastened. Nothing else is in frame.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. Her head turns, small and slow, decelerating into a stop with no overshoot; the turn is one acceleration and a long deceleration. The face arrives after the turn, not with it. Nothing else on the subject moves. Dust falls continuously through both beats, and keeps falling after she has stopped. The light holds steady; the only light event is the plastic of the nameplate catching the fluorescent key as the turn brings the left of the chest toward the lens. No impact, no collision, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third person, close, at her shoulder; the figure fills much of the frame and the fluorescent tube sits at the upper edge as the source. One camera event only: a very slow, weighted settle of a few centimetres over the whole take — the camera placed rather than travelling, revealing nothing. No handheld, no whip, no shake, no push-in on the face. One continuous take; no cut.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of every word this work holds; **if any speech is placed in it, that speech is Japanese.** **No speech is placed in this shot.** No dialogue. No calling voice, no spoken name, no voice-over, no narration — nothing is voiced at any point. **Nothing is written on screen**: no subtitles, no captions, in any language. Sound effects at the edge of audibility: cloth, a chair, a drawer, a pen set down — the sound of paper and hands, nothing mixed forward. Ambient: an office interior with a fluorescent hum. **Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell.**

## Negative Prompt

no second person in frame, no caller in frame, no listener in frame, no colleague in frame, no passer-by in frame, no legible text on any surface, no legible name text, no legible name on any in-world prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no glyph-like marks on any surface, no signature, no handwriting by the subject, no calling voice as a sound effect, no audible speech, no spoken name, no voice-over, no narration, no background music, no face before the name is called, no completed action, no finished movement, no resolved gesture, no smile, no tears, no fear, no pleading, no exaggerated expression, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket, no blazer, no outer garment, no identifying clothing, no identifying hairstyle, no identifying prop, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no watermark, no morphing or drifting facial identity, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-promo-chinatsu-s01-5s-01`
- Segment ID: `01-1`
- Specification Version: `0.1.0`
- Generation Date: `—`

⚠️ **この作品は巻を持たない。** `01-1` の `01` は、暗黙の一巻である。

## Resolved Values

- Duration: `5s`
- References: `REF_CHARACTER (frozen pair, CRITICAL) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `2 beats, NON_UNIFORM — 3s / 2s. The held beat = BEAT 2 at 2s (40%)`
- Camera Events: `1 event as listed in §10. One continuous take`
- Action Events: `ACT_TURN → ACT_WITHHOLD`
- Audio Events: `no dialogue ／ no call ／ paper and hands ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **The reply may arrive.** An open mouth, an intake of breath, or a nod would resolve the beat. **The shot ends because the mouth stays closed.**
- **The call may be voiced** — as ambience, as a muffled line, as a caption. There is no call in the mix at any level.
- **The name may be rendered legibly.** A readable 碓氷千夏 on the plastic ends the work's premise. It must be present and unreadable.
- **The face may arrive with the turn.** The order is name then face; a face that turns with the head is a different beat.
- **A second person may be invented** — a shoulder at the frame edge, a hand, a reflection with someone in it. She is the only person in this work.
- **The shot may become a still.** Dust must keep falling after the head stops, or the five seconds read as a photograph held.
