# ═══ 演出要約 ════════════════════════════════════
# 『声の試聴』ミラボB / 対話 / motion —— 静けさが、一度の台詞になり、静けさに戻る
#
#   窓の無い試聴室で、小さな機体がカメラへ一度だけ喋る。
#   10秒、カメラは動かず、機体は同じ高さに浮かんだまま、声と光だけが動く。
#   音楽も字幕も文字も無く、人は一人も映らない——声だけを取り出すための1本である。
# ═════════════════════════════════════════════════

# Wan 3.0 Full Specification — 声の試聴 ミラボB / 10s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である。

# 1. VIDEO

- Duration: `10s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: **a dark screen lights, speaks one line, and goes quiet.**

# 2. WORLD

## World Concept

A bare listening room with no window. Warm-grey walls, no furniture, no props. The room exists so that **nothing competes with the voice** — it has no clock, no writing, and no person in it.

## World Rules

- **Only the voice changes.** The device holds its height and its facing; it does not approach, depart, or turn.
- **No person.** No human in frame, no hand entering frame, no reflection of anyone, no shadow of a person.
- **One device.** No second device, no companion unit, no copy in the background.
- **The line is read once.** It is not repeated, not paraphrased, not continued.
- **No music.** No bed, no chord, no melody, no sting.
- **No writing.** No subtitle, no title, no name, no caption, and **nothing legible on the screen.**
- **No cut.** This ten seconds is one continuous take.
- **It ends on silence.** After the last word the screen dims to rest and the clip holds.

## Visual Language

- Art Direction: Luminous realist anime, held still — one small device against a plain warm-grey wall. **Low visual density**, generous empty space around it.
- Color Language: the wall's warm grey, the shell's light matte grey, and **one amber line** on a dark screen. No third hue competes with that line.
- Texture: clean cel shading at one shadow tone per material, the boundary crisp; the shell matte, the screen's glass dark and slightly reflective.
- Rendering: soft volumetric light from frame left, dust suspended and visible against the grey.
- Visual Density: low.
- Time: `時刻を持たない`
- Atmosphere: quiet, level, and attentive — **friendly without being a mascot.**

# 3. SUBJECTS

## ミラボ

A small AI companion unit, about the size of a melon, hovering at chest height in the centre of the frame and facing the camera. **The body is a single rounded shell in matte light grey**, with a soft seam running around its waist and no visible fastening. The front is a **dark glass screen** that fills the face area, faintly reflective, with a thin bezel.

**The screen holds one thing only: a single horizontal amber line, and that line is the mouth.** There are no eyes, no icons, no dials, and **no legible mark of any kind** on the screen — the line is the whole of the face.

- Motion: the unit hovers, so a small rise and fall of a few millimetres runs for the entire shot, and the shell never tilts more than a degree.
- Behaviour: it speaks as an assistant that is glad to be asked — bright, quick and clear; the line's brightness rises with the voice and falls at rest.
- Emotional range: attentive → a bright lift at the end of the second sentence. **No coyness, no wink, no pleading tilt.**

## Voice (for §14 and §18 only — not a visual subject)

**Higher than the first candidate, clear and light, with a clean centre and a fine glassy edge.** It is a small machine's voice, not a child's: the brightness sits high and stays open, and **the vowels are firm rather than soft**. **No breathiness, no whisper, no vocal fry, no chipmunk squeak, no sing-song.** Tempo is a touch quicker than the first candidate; each word is finished cleanly and the ends of sentences lift a little.

# 4. ENVIRONMENT

- A windowless room. The back wall is plain warm grey, matte, with no seam, no skirting board, no fixture.
- **No furniture, no prop, no door, no window.** The frame's background is the wall and nothing else.
- Air: fine dust suspended in the key light, drifting slowly throughout the shot.
- **A faint warm pool of light under the device**, cast on nothing — the wall behind it does not catch it as a shadow of a person would.
- **No environmental event** — no door opens, no light changes, nothing passes behind it.

# 5. OBJECTS

- **The device is the subject, not a prop.** It is held in the air and handled by no one.
- **No stand, no cable, no table, no pedestal.** Nothing supports it in frame.
- No other object is present.

# 6. REFERENCES

- REF_STYLE: `luminous-anime` (HIGH)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_SOURCE: `projects/explainer-voice-samples/bible.yaml` (CRITICAL)
- **No image reference is attached.** The appearance is fixed by §3, not by a picture.

# 7. NARRATIVE

- **The event:** a device whose screen was dark lights, speaks one line to camera, and goes quiet.
- Beginning: the device floats at rest; the line is closed and dim.
- Development: the screen comes up; the first sentence.
- Turn: the line closes for a moment, with no words in it.
- Climax: the second sentence, which names the three places.
- End: the line closes and dims; the room is quiet again. **Nothing is added after the last word.**

# 8. TEMPORAL STRUCTURE

- **NON_UNIFORM.** The beats are deliberately uneven; the line holds the largest share.
- Sparse: the first second and the last six tenths.
- Dense: the two sentences.
- Held: the gap between them, 0.8s.

| Range | Density | What happens |
|---|---|---|
| 0–1.0s | sparse | The line is closed and dim; the screen rises in brightness. |
| 1.0–5.6s | dense | The first sentence; the line opens and closes with the words. |
| 5.6–6.4s | held | The line closes; the glow settles. No words. |
| 6.4–9.4s | dense | The second sentence; the line breaks three times at the three places. |
| 9.4–10s | sparse | The line closes and dims; silence returns. |

# 9. ACTION

- **Single action: speak once.** Before: line closed, at rest. After: line closed, at rest, the line completed.
- Speed: even, at a natural assistant's tempo; no acceleration, no rallentando.
- Intensity: moderate — clear, not emphatic.
- **Causes:** the brightness rising at 0–1s causes the first sentence; the closing at 5.6s causes the second. **No other cause enters the frame.**

# 10. CAMERA

- Third person, at the device's screen height, straight on, medium close-up — the whole shell with air around it.
- **One camera event only:** a very slow, weighted settle of a few centimetres across the whole take. The camera is placed, not travelling.
- **No cut. No handheld. No whip. No shake. No push-in. No zoom. No rotation.**
- The camera does not follow the line; the framing stays the same from first frame to last.

# 11. MOTION

## Subject Motion

The amber line on the screen **opens and closes with the words**: it lengthens as a vowel is held and narrows between phrases. The screen's brightness follows the voice by a small amount. **The shell holds its height and facing**; only the few-millimetre hover drift and a sub-degree sway are present.

## Object Motion

None. There is no other object.

## Environmental Motion

Dust drifts through the key light for the entire shot, including after the last word. The wall does not change.

## Physical Characteristics

The hover has weight: the unit settles when the glow drops rather than floating weightlessly. **No floaty drift into a camera move; no impact; no motion blur smear; no strobing.**

# 12. EMOTION

- Arc: **attentive → a bright lift.** It does not rise to enthusiasm and does not fall to apology.
- The emotional event is at 6.4s: the second sentence begins with a brighter line and a slightly quicker step, not with more volume.
- **No coyness, no pleading.** The warmth is in the evenness of the delivery.

# 13. LIGHTING

- Key: soft, from frame left and slightly above, grazing the shell's curve; colour temperature 4300K.
- Fill: a broad, low fill from frame right, one stop down, so the shadow side stays open.
- Rim: a thin cool rim along the shell's right edge, barely visible against the grey.
- **Self-emission:** the amber line, and a faint warm pool under the device. **The glow is small and contained** — it does not light the wall.
- **No lighting event.** The room light does not change; only the screen's own brightness moves.

# 14. AUDIO

- **The language of this work is Japanese.** Every word in this shot is spoken in Japanese; **the line is delivered in Japanese, with Japanese phonemes and Japanese prosody.** Do not translate, do not subtitle, do not dub.
- **Dialogue (one speaker, ミラボ):**
  「今日は、脆弱性とサイバー攻撃について話します。壊れる場所は、入力、メモリ、依存の三つです。」
  Delivery: **high and clear, a fine glassy edge, clean open centre; a touch quicker, every word finished, the ends lifting a little.** The first sentence ends level; the second lists the three places without stressing any one of them.
- **Sound Effects:** none beyond the voice and the room.
- **Environment:** a quiet, dry interior — no reverb tail, no air-conditioning hum, no traffic, **no servo whine, no beep, no UI chime.**
- **Music: none.** No bed, no score, no sting. **Nothing rises under the last word.**
- **Nothing is written on screen:** no subtitles, no captions, no title, no name.

# 15. CONTINUITY

- **Identity lock:** the same unit throughout — the same melon-sized matte light-grey shell, the same dark glass screen, the same single amber line, the same height above the floor. **Repeated verbatim in §18.**
- **Space:** it stays on the same mark, centred, at the same distance from the lens.
- **Time:** no clock, no change of room light, no off-screen event.
- **Visual:** the same warm-grey wall, the same key from frame left, the same low density.
- **Motion:** full animation, not limited; the dust and the hover are the continuous movers.

# 16. CONSTRAINTS

## MUST NOT

- No human in frame, no hand entering frame, no reflection of a person, no shadow of a person.
- No second device, no companion unit.
- No readable text anywhere — on the screen or off it: no icon, no glyph, no subtitle, no title, no name, no watermark.
- No music of any kind; no bed; no sting.
- No beep, chime, servo whine, or UI sound.
- No cut; no camera move other than the settle; no zoom; no shake.
- No arms, no legs, no wheels, no eyes, no eyeballs on the screen.
- No mascot costume, no plush body, no child-like proportions.
- No coyness: no wink, no pleading tilt, no sing-song cadence.
- No change of place, no approaching the camera, no rising to the ceiling.
- No lip-sync drift: the line must match the Japanese words.

## MUST

- One continuous 10-second take.
- The line spoken once, in Japanese, intelligible and complete.
- The amber line on the screen moves with the line.
- The clip ends in silence after the last word.

## PREFER

- The device in the upper half, with air above it.
- The key from frame left, so the shadow side stays open.

## ALLOW

- A small brightness lift on the second sentence, once.
- The hover's natural few-millimetre drift.

# 17. GENERATION PRIORITIES

1. **The voice comes first.** Intelligibility and timbre outrank beauty of the frame.
2. **The line is complete and in Japanese.** A beautiful shot with a broken line is a failed take.
3. **No person appears.** Not in the frame, not as a reflection, not as a silhouette.
4. **Identity holds.** The same shell and the same single line from first frame to last.
5. **The room stays quiet.** No music, no UI sound, even if the picture feels bare.

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 10-second continuous cinematic take (16:9) of a small hovering AI companion unit, alone in a bare listening room, speaking one line, one clip. Beats, deliberately uneven: [0-1s] the unit floats at rest with its amber line closed and dim, and the screen's glow rises; [1-5.6s] it speaks the first sentence, the amber line on its screen opening and closing with the words; [5.6-6.4s] the line closes for a moment and the glow settles, with no words in it; [6.4-9.4s] it speaks the second sentence and the line breaks three times at the three places; [9.4-10s] the line closes and dims and the room returns to silence. The core beat — the line spoken — holds the largest share of the duration; the remaining beats pass quickly. no one in the frame. Japanese speech. Ends on the room returning to silence, and holds.

## Visual Prompt

Luminous realist anime, held still: a small AI companion unit, about the size of a melon, hovering at chest height at the centre of a bare listening room, against a plain warm-grey wall with no window, no furniture and no prop. **Low visual density**, generous empty space around it. The body is a single rounded shell in matte light grey with a soft seam at the waist and no visible fastening; the front is a dark glass screen, faintly reflective, with a thin bezel. **The screen holds one thing only: a single horizontal amber line, and that line is the mouth** — no eyes, no icons, no dials, no legible mark of any kind. Clean cel shading at one shadow tone per material with a crisp boundary; the shell matte, the glass dark, one amber emission and no third hue competing with it. Soft volumetric key from frame left at 4300K, a broad fill from frame right one stop down, a thin cool rim along the shell's right edge, and a faint contained warm pool of light under the unit that does not light the wall. Fine dust suspended in the key light. **No legible writing anywhere** — no subtitle, no title, no name.

## Motion Prompt

Full animation, not limited — the air is the continuous mover. The amber line on the screen opens and closes with the words: it lengthens as a vowel is held and narrows between phrases, and the screen's brightness follows the voice by a small amount. The unit hovers: a few millimetres of rise and fall, plus a sub-degree sway, for the entire shot. Dust drifts through the key light throughout, including after the last word. **The shell holds its height and facing; there is no tilt beyond a degree, no impact, no collision, no motion blur smear, no stutter, no held frame, no strobing.**

## Camera Prompt

Third person, at the device's screen height, straight on, medium close-up — the whole shell with air around it. One camera event only: a very slow, weighted settle of a few centimetres over the whole take, the camera placed rather than travelling. **No handheld, no whip, no shake, no push-in, no zoom, no unnatural rotation.** One continuous take; no cut. The framing does not follow the line; it is the same from the first frame to the last.

## Audio Prompt

**The language of this work is Japanese** — every word in this shot is spoken in Japanese, with Japanese phonemes and Japanese prosody; do not translate it, do not subtitle it, do not dub it. One speaker, ミラボ, a small AI companion unit. The line, spoken once, a touch quicker than an even tempo: 「今日は、脆弱性とサイバー攻撃について話します。壊れる場所は、入力、メモリ、依存の三つです。」 Its voice is **higher still, clear and light, with a fine glassy edge and a clean open centre; small-machine rather than child; firm vowels, clean consonants, the ends of sentences lifting a little.** It is **not breathy, not whispered, not a vocal fry, not a chipmunk squeak, not sing-song**, and every word is finished cleanly. The first sentence ends level; the second lists the three places without stressing any one of them. Room: a dry, quiet interior with no reverb tail, no hum and no traffic. **No second voice; no narration; no beep, no chime, no servo whine, no UI sound.** **Music: none — no bed, no score, no sting, and nothing rises under the last word.** **Nothing is written on screen:** no subtitles, no captions, no title, no name, in any language, and no legible mark on the device's screen.

## Negative Prompt

no people, no one, no person, no figure, no second person, no listener in frame, no human in frame, no hand entering frame, no second device, no companion unit, no readable text, no legible writing, no icon on screen, no glyph, no on-screen subtitles, no caption, no captions, no burned-in subtitles, no subtitles in any language, no title card, no name on screen, no watermark, no background music, no music bed, no score, no musical sting, no beep, no chime, no servo whine, no room reverb tail, no second voice, no narration, no whisper, no vocal fry, no chipmunk voice, no child voice, no sing-song cadence, no arms, no legs, no wheels, no eyes, no eyeballs on screen, no mascot costume, no plush body, no cut, no handheld, no whip, no shake, no zoom, no push-in, no lip-sync drift, no line moving without sound, no coy expression, no wink, no pleading tilt, no change of place, no approaching the camera, no strobing, no object in frame, no furniture, no window, no clock, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces, no morphing or drifting identity

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. **The atmosphere is the primary mover**: dust drifts through the key light continuously, and the unit's hover keeps its own small drift even when it is at rest. Camera moves with weight and commitment. No stutter, no shooting on threes, no held frames. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `vs-04-10s-01`
- Duration: `10s`
- Output: `1920x1080` / `24fps` / 16:9
- Attached: none (`reference_set: []`, `attached: []`)
- Output file (planned): `media/vs-04.mp4`

# 20. ITERATION

| Observed | Change | Next |
|---|---|---|
| 10.0s / 300 フレーム。**`854x480` / `30fps` で返った**（§1 は `1920x1080` / `24fps`） | 仕様は直さない——**頼んだ値と来た値は別の欄である**（実測は `takes/vs-04-video-1.yaml`） | 画を使うなら 1080p で取り直す。**声の参照には影響しない** |
| 声を取り出した: `references/gen_machine_bright.wav`（0.42–9.54s / 9.12s） | **採用**（2026-11-01、著者） | `characters/mirabo.voice.yaml` の `reference_audio` に差した |
