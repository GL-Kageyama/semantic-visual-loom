# Wan 3.0 Full Specification — 『ハビッツ！！！』碓氷千夏 キャラクタープロモーション 第三ショット「名を出さずに、用件から切り出す」 / 4s

⚠️ **生成器へ投入するのは §18 だけである。** §1–17 は下敷きであり、§19–20 は我々の記録である。

⚠️ **このショットは、日本語で話す。**（決定 2026-09-18、著者）
**口が動いているのは、喋っているからである。**
⚠️ **五つのうち、声を持つのはこの一つだけである。** 他の四つは口が開かないか、
開いても名が来ない。
⚠️ **これは反転である。** この一段は決定の直前まで「**声そのものを置かない**」と書いていた
——**その記録は下に残す**（「字を招かない」の言語の項）。**消さない。**

⚠️ **用件の中身は、書かない。** 出典に一行も無い——⚠️ **台詞を発明しないことと、
声を置かないことは、別である。** このショットは、**言葉を一字も書かないまま、日本語で喋る。**
⚠️ **ゆえに観客は、中身を受け取らない。** **字幕を出さないからである**——
受け取るのは、**喋っているという事実と言葉の音**である。
⚠️ **中身が届かないことを、沈黙で表さない。** 口は動き、声はあり、**語だけが書かれない。**

⚠️ **この作品の規則は「発話があるなら、それは必ず作品の言語である」である**（`bible.yaml`）。
⚠️ **発話を禁じる規則は、もう無い。** **禁じられているのは名であって、声ではない。**

⚠️ **聞き手は、枠の外にいる。** `rolemap` の `対話` が持つ固有基準のうち、**「聞き手の反応」は
空欄である**——**聞き手が枠に居ないからである。** ⚠️ **これは検査の穴ではなく、記録された不在である**——
**引けない基準を、引けたことにしない。**
⚠️ **「声との同期」は、このショットで引ける**（**反転**——言語を置く前は、これも空欄であった）。
**口が動くのは喋っているからであり、音と口が食い違えば、このショットは壊れている。**

⚠️ **§18 `Negative Prompt` は、五ショットで同一である**（第一ショットのヘッダを読む）。
**発話は Negative ではなく §14 と `Audio Prompt` が負う。**
**（⚠️ 字幕の禁止は、逆に Negative が負う——上の「字幕は、基盤が必ず禁じる」。）**

⚠️ **人名はローマ字にしない**（決定）。**Negative は字種を禁じない。**

⚠️ **BGM は置かない**（著者指示 2026-09-18）。⚠️ **このショットには声がある**——
**ゆえに、とくに置かない。** 音楽を敷けば、**声が「演出された声」になる。**

⚠️ **このショットは、一度、中国語の字幕を焼いて生成された**（2026-09-18）。
   ⚠️ **原因は `§18` の書き方である**——「**she keeps talking**」「**Ends mid-sentence**」。
      **Wan 3.0 は発話を検出すると字幕を焼く。**
   ✅ **打った手は三つである。**
     ① **発話を名指す語を落とした**——「she keeps talking」→「**the mouth keeps moving**」、
        「mid-sentence」→「**with the mouth still moving**」。
        ⚠️ **`Audio Prompt` の「Silence, specified」は前から在った。それでも焼かれた**——
           **効かなかったのは、`Master Prompt` の側が発話を名指していたからである。**
        ⚠️ **この①は、いま反転した**——**このショットは喋るからである。**
           **落とした語は `Master Prompt` に戻った**（「**she is still speaking**」）。
           **字幕を止める担い手は、`Master Prompt` から `Negative` へ移った**（下の言語の項）。
     ② **`§18` の `Master` に一行を足した**——「**The frame stays clean throughout — the room,
        the light, the dust and her, and nothing laid over the image.**」（五ショット共通）
     ③ **共通の `Negative` を強めた**——「no burned-in subtitles, no subtitles in any language,
        no translated captions」（五ショット両経路、10本）。
   ✅ **言語は、作品の側で名指した**（決定 2026-09-18、著者——「**日本語の言語指定で触っているなら、
      必ず日本語を話すべき**」）。
      · `bible.language: Japanese`——**作品定数として置いた。** 読む者は `L27` である。
      · `Audio Prompt`（五ショット共通）——「**The language of this work is Japanese** … **if any
        speech is placed in it, that speech is Japanese.**」
      · `Master Prompt`（**このショットだけ**）——「**a Japanese room in a Japanese work, and
        Japanese is its only language**」。
      ⚠️ **口が動くのは、五つのうちこのショットだけである**——**ゆえに発話の名指しも、ここにだけ要る。**
      ⚠️ **当初は「発話を招かない形」で書いた。****それは反転した**——
         **このショットは喋る。** 言語の名指しは、いま**保険ではなく指定である。**
      ⚠️ **それでも Wan の既定が中国語であることは変わらない**——**ゆえに名指しは、いまも要る。**
         **万一モデルが喋ったとき、出るのが日本語になるようにしておく。**
      ⚠️ **効いたかどうかは、再投入の結果だけが言う。**（この一文は、反転しても変わらない。）

   ✅ **字幕は、基盤が必ず禁じる**（決定 2026-09-18、著者——「**字幕は、こちらから指定しない限り、
      必ず不要にして**」）。
      · `specmap.BASE_NEGATIVES` が `no watermark` と `no on-screen subtitles` を**全作品の
        両経路の Negative に必ず入れる**——`L21` が動画の §18 と画像の `Negative` の両方で
        突き合わせる。**作品は書かなくてよい。**
      · この作品は、その上に**字幕の側を五節へ強めている**（上の③——`no burned-in subtitles,
        no subtitles in any language, no translated captions`）。
      ⚠️ **「発話を名指す語を落とす」という手は、ここで反転した**——**このショットは喋るからである。**
         **字幕を止める担い手は、`Master Prompt` から `Negative` へ移った。**
   ⚠️ **詳細は `bible.yaml`「字を招かない」に在る。**

✅ **二経路を持つ**（決定 2026-09-18、著者）。画像仕様は `specs/image/shot-03-matter.md`——
   **§1–20 を持たない。** 画像の `Negative` は、この §18 と同一である（第一ショットのヘッダ）。
   ⚠️ **音は1枚に写らない。**（**口が動くことは写る。**）
      ⚠️ **それでも音の節は、画像の `Negative` に在る**——**この §18 の写しだからである。**
      **写らないものを禁じても、何も変わらない**——**が、消さない。**
      **二経路の禁止が一字も違わないことが、この作品の決定である。**

---

# 1. VIDEO

- Duration: `4s`
- Aspect: `16:9`
- Resolution: `1920x1080`
- Frame Rate: `24fps`
- Orientation: `Landscape`
- Generation Intent: One continuous take. A single change: the mouth begins to move, and the name does not come. **The shot is the shortest in the work, because what it withholds is only visible while it is short.**

# 2. WORLD

## World Concept

2026, Japan. A public elementary school in Tokyo, and the staff room of it. There is no magic, no institution and no secret organization — there is only a daily life in which the etiquette of the written name is thoroughly in place. **She has never once addressed anyone by name, and this shot is that habit, unobstructed.**

## World Rules

- **The people in the work do not know that they are inside a film.**
- **The hand comes first and the face comes after. The order is not swapped. The face is placed only after the name has been called.**
- **The sound is not a calling voice; it is the sound of paper and hands.**
- **Outside the work, for the first time, someone calls out. Inside the work it is never spoken. Being spoken outside does not cancel being unspoken inside. The cost is kept, not erased.**
- **This work places no one in frame but her.** The caller and the listener are outside the frame.
- **No text is burned into this work.**
- **No name is spoken in this work.** Speech exists — she is speaking — and the name never arrives.
- **If any speech is placed in this work, it is Japanese.** No other language is spoken in it.
- **This work does not decide whether the four beats are the same day.**

## Visual Language

- Art Direction: Luminous realist anime — **the light, not the figure, is the subject.** This is the one shot where the face carries the frame, and the light is what keeps that from becoming a portrait: the fluorescent key comes from the upper edge, and the shadowed side of the face is where the shot's meaning sits.
- Color Language: Saturated where the light falls, deep cyan in the unlit half. The warm side reaches its high point here — skin lit, everything else cool.
- Texture: Layered depth; the room behind is present as light and blur, never as detail. No grain, no paper texture, no painterly stroke.
- Rendering: Hyper-detailed layered light — bloom at the tube, dust suspended between the lens and the face, clean anime lineart on the face **kept subordinate to the light**.
- Visual Density: Low. One face, one direction of gaze, and empty space on the side the listener is not on.
- Time: `2026年の勤務日の日中` — a working day, daytime, fluorescent.
- Atmosphere: Ordinary, and slightly out of frame — she is speaking to a place the shot does not cover.

# 3. SUBJECTS

## 碓氷千夏

- Reference: the frozen pair — `ChatGPT Image 2026年9月18日 20_29_36.png` (character sheet, revision 4) ＋ `ChatGPT Image 2026年9月17日 21_56_32.png` (expression sheet, revision 2). **Both are attached; neither is summarised.**
- Appearance: A woman of thirty-three, in a washable shirt, the nameplate at the left of the chest. ⚠️ **The source records no description of her appearance**; the frozen image is the appearance, and this is the shot where the face is largest, so drift is most visible here.
- Behavior: **She begins from the matter at hand and does not name the person she is speaking to** — run-06: 「誰かを名で呼ばずに用件から話し始める。」 Her gaze goes to the side the listener is on, which is outside the frame. **It does not come to the lens.**
- Continuity Requirements: **Must preserve** — the frozen face, the nameplate at the left of the chest, the shirt, no outer garment. **May change** — which side the listener is on (unfixed in the source), the angle of the head, the amount of the room in frame.

# 4. ENVIRONMENT

- Location: `名札` — **the site of the naming, not a room.** Here it is the name at the left of the chest in a room where she is talking to someone without saying it.
- Environment Elements: The lit wall, the edge of a desk, the fluorescent tube at the frame's upper edge, and the space on the listener's side. Dust in the air.
- Environmental Behavior: The dust falls continuously. The light holds. **Nothing in the room responds to her, because the one who would respond is not in it.**

# 5. OBJECTS

- The nameplate — plastic, worn at the left of the chest, present in frame and **unreadable.**
- The shirt — washable cloth; the collar and shoulder take the key.
- No other object is in frame. **Nothing is held, and nothing is being done with the hands.**

# 6. REFERENCES

- REF_CHARACTER: the frozen pair (`20_29_36.png` ＋ `21_56_32.png`) (CRITICAL)
- REF_FORMAT: `video-spec` — this defines the seven §18 slots
- REF_STYLE: `luminous-anime` (HIGH)
- REF_SOURCE: `projects/habits/promo-chinatsu/bible.yaml` (CRITICAL)
- ⚠️ **No location board is referenced.**

# 7. NARRATIVE

- Core Event: She starts talking from the matter, and the name that should open the sentence never arrives.
- Beginning: The mouth has not moved.
- Turn: The mouth begins to move.
- Peak: **The position where the name belongs stays empty.** The sentence runs on without it.
- Pull: She is still speaking when the shot cuts. **Nothing is resolved, and nothing is answered.**

# 8. TEMPORAL STRUCTURE

- Timing Policy: `STRUCTURED` / `NON_UNIFORM`
- Temporal Sequence:
  - BEAT 1 `0-2s` — density: `sparse` — **The mouth begins to move.** The matter comes first, without a name. The place where the name belongs is empty.
  - BEAT 2 `2-4s` — density: `held` — She keeps speaking. **The name does not come.** The sentence runs past the place where it belongs.
- Temporal Density: Two beats of equal length, and the second one is the one that carries — **it is not the length that makes the held beat; it is that nothing arrives in it.**

# 9. ACTION

- `ACT_SPEAK` — Before: the mouth is closed. After: the mouth is moving and **a Japanese voice is in the mix**. ⚠️ **The words are not written; the voice is. The audience receives that she is speaking — not what she says.**
- `ACT_OMIT` — Before: the sentence has not begun. After: the sentence is running without a name. **This is an action, and it is the shot's action.**

# 10. CAMERA

- Camera Language: Third person, at her height, close enough that the frame is her face and the empty side of the room. The style's light-first hierarchy holds; **the empty side is kept empty, and it is the frame's second subject.**
- Camera Events: One event only. `0-4s` — a very slow, weighted settle, a few centimetres, in the direction of the listener's side and stopping short. **It does not reach them.**
- Camera Behavior: No handheld, no whip, no shake, no cut, no push-in to the mouth. One continuous take.

# 11. MOTION

## Subject Motion

The mouth moves; the head is nearly still; her gaze stays on the listener's side. **Small, and it does not build.** Nothing is emphasised.

## Object Motion

None.

## Environmental Motion

Dust falls continuously. The light holds. **The dust is what proves the shot is not a photograph with a moving mouth pasted on it.**

## Physical Characteristics

- Weight: The head has weight and does not float; the small movements read as a body held upright.
- Inertia: None required; there is no travelling movement.
- Acceleration: None; the mouth's motion is even.
- Fluidity: Continuous and unhurried. No snap, no stutter.
- Impact: None.

# 12. EMOTION

- Emotional Arc: The shape of a sentence that has learned not to open with a name.
- Emotional Events: The instant the sentence passes the place where the name belongs and continues.

# 13. LIGHTING

- Base Lighting: Fluorescent key from the upper edge; the lit side of the face is warm and the shadowed side is deep cyan. Dust suspended between the lens and the face. The style's bloom is at the tube, above and out of the way. **This is the brightest the figure gets in the work, and the shadow side is where the shot's meaning sits.**
- Lighting Events: One — a slow shift as her head moves a few degrees, moving the light's edge across the cheek and leaving it there.

# 14. AUDIO

- Dialogue: **Japanese, and the words are not written down.** The mouth moves because words are being said. ⚠️ **The matter itself is not in the source, so this shot does not put a script in her mouth** — no line is written here, and none is invented. **The language is fixed; the words are not.**
- Sound Effects: **None.** Nothing is held and nothing is being done with the hands — the work's effects are paper and hands, and this shot has neither.
- Music: **None.** No score, no BGM, no drone, no pad, no sting, no swell. ⚠️ **A bed under a speaking voice turns the voice into a performance**, and this one is not a performance.
- Environment: An office interior with a fluorescent hum — **the same bed as the other four shots.** ⚠️ **この段はこの一段が足した**（発明・要承認）——**声に部屋を与えるためである。** 無音の部屋に声だけを置けば、**その声は声優の声、すなわちナレーションになる**（§16 MUST NOT）。⚠️ **声は、部屋の中の人である。**
- ⚠️ **このショットは、もはや無音ではない。** 指定されているのは**声の言語**であって、**沈黙ではない**——`video-spec` の `avoid` が禁じる「省略による無音」に戻さないために、四つとも名指しで書く。

# 15. CONTINUITY

- Identity: The frozen pair, unsummarised, attached on every instance. Same face, same shirt, same nameplate, no outer garment.
- Spatial: The nameplate stays at the left of the chest. The listener's side stays outside the frame.
- Temporal: This shot does not fix the date, and nothing in frame supplies one.
- Visual: Same palette, same fluorescent key, same dust as the other four shots.
- Motion: Full animation, not limited. The atmosphere is the primary mover: dust falls even though the sound does not exist.
- Sound: **A Japanese voice — the words unwritten.** The previous shot was cloth; the next is paper. This one carries a voice, and the other four do not.

# 16. CONSTRAINTS

## MUST NOT

- No second person in frame — no caller, no listener, no colleague, no passer-by, no hand but hers. **The listener is on the other side of the frame edge and is never shown, not even as a shoulder.**
- No legible text on any surface — on the nameplate, on paper, on a screen, on a wall.
- No romaji in place of the Japanese name.
- **No spoken name; no voice-over; no narration; no language but Japanese.** She speaks, and the name is not among what she says. **A voice placed over the image rather than in the room is a voice-over, and it is forbidden.**
- **No subtitles and no captions, in any language.** Nothing is written on screen — **the words are not written down anywhere, including there.**
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

- **The mouth moves and no name arrives.** The sentence must be shaped so that a name is missing from its opening.
- The gaze stays on the listener's side. **It does not come to the lens.**
- **She speaks Japanese, and the words are not written down.** The voice is in the room, not over the image; no effects, no music.

## PREFER

- The empty side of the frame kept as generous negative space, equal in weight to the face.

## ALLOW

- A single small head movement that carries the light's edge across the cheek.

# 17. GENERATION PRIORITIES

1. **The name does not come** — not spoken, not mouthed as a name, not supplied in text. This outranks legibility of speech.
2. **Japanese, and only Japanese.** The voice that is placed is the language of the work. ⚠️ **A voice in any other language is a different shot** — and a subtitle that renders her words is the same failure in writing.
3. **She does not look at the lens** — the gaze goes to the listener's side, which is where the frame ends. **A talking face that finds the camera is a different shot**, and the mouth is the subject here, not the eyes.
4. **The listener is never shown** — not a shoulder, not a silhouette, not a reflection.
5. **Short** — this shot is 4 seconds because the withheld name is only visible while it is short.
6. Everything else.

---

# 18. WAN 3.0 PROMPT MAPPING

## Master Prompt

A 4-second continuous cinematic take (16:9), luminous realist anime, in the staff room of a Japanese public elementary school, 2026 — a Japanese room in a Japanese work, and Japanese is its only language — at the left of 碓氷千夏's chest, where the nameplate is worn. Beats, deliberately uneven in what they carry rather than in length: [0-2s] her mouth begins to move — she starts from the matter at hand, and the place where a name belongs stays empty; [2-4s] she is still speaking and the name does not come. Her voice is in the room, in Japanese, addressed to someone outside the frame; what she says is not written down and is never shown as text. Her gaze stays on the side the listener is on, outside the frame; she never looks at the lens. Sound: her voice, and the fluorescent room under it — no effects, no music. The frame stays clean throughout — the room, the light, the dust and her, and nothing laid over the image. Dust falls through fluorescent light. Ends with the mouth still moving and cuts.

## Visual Prompt

Luminous realist anime, translated into an interior: the light, not the figure, is the subject. A woman of thirty-three, identity locked to the frozen reference pair, wearing a washable shirt with the school-designated nameplate at the left of the chest and no outer garment. Clean anime lineart on the face, kept subordinate to the light. Saturated where the light falls, deep cyan in the unlit half; the warm side reaches its high point here — skin lit, everything else cool. Hyper-detailed layered light — bloom at the fluorescent tube at the upper edge, dust suspended between the lens and the face, the room behind present only as lit blur and never as detail, low visual density with generous negative space on the listener's side. A plastic nameplate at the left of the chest, its printing washed out by the key. Nothing else is in frame; nothing is held, and the hands are not doing anything.

## Motion Prompt

Full animation, not limited — the atmosphere is the primary mover. Her mouth moves evenly and unhurriedly, with no build and no emphasis; the head is nearly still and holds upright with weight, not floating; her gaze stays on the listener's side. The light's edge moves a few degrees across her cheek as the head moves, and stays. Dust falls continuously through both beats — the dust is what proves the shot is not a photograph with a moving mouth on it. No impact, no collision, no motion blur smears, no stutter, no held frames.

## Camera Prompt

Third person, at her height, close enough that the frame is her face and the empty side of the room. One camera event only: a very slow, weighted settle of a few centimetres toward the listener's side, stopping short and never reaching them. The empty side is kept empty and is the frame's second subject. No handheld, no whip, no shake, no push-in to the mouth. One continuous take; no cut.

## Audio Prompt

**The language of this work is Japanese** — Japanese is the language of the room, of the people in it, and of every word this work holds; **if any speech is placed in it, that speech is Japanese.** **She is speaking, in Japanese, to someone outside the frame** — her voice is in the room, not over the image. **No spoken name**, no voice-over, no narration: the name is not among what she says, and what she says is not written down. **Nothing is written on screen** — no subtitles, no captions, no rendered words, in any language. No sound effects. Fluorescent room tone under the voice. **Music: none. No score, no BGM, no background music, no drone, no pad, no sting, no swell.**

## Negative Prompt

no second person in frame, no caller in frame, no listener in frame, no colleague in frame, no passer-by in frame, no legible text on any surface, no legible name text, no legible name on any in-world prop, no romaji in place of the Japanese name, no real-world alphabet, no invented characters, no nonsense glyphs, no pseudo-kanji, no glyph-like marks on any surface, no signature, no handwriting by the subject, no calling voice as a sound effect, no audible speech, no spoken name, no voice-over, no narration, no background music, no face before the name is called, no completed action, no finished movement, no resolved gesture, no smile, no tears, no fear, no pleading, no exaggerated expression, no wall clock, no calendar, no digital timer, no date stamp, no cardigan, no jacket, no blazer, no outer garment, no identifying clothing, no identifying hairstyle, no identifying prop, no uniform pacing, no equal-length beats, no static slideshow of stills, no floaty weightless motion, no scene cuts to unrelated locations, no on-screen subtitles, no captions, no burned-in subtitles, no subtitles in any language, no translated captions, no watermark, no morphing or drifting facial identity, not photorealistic, no 3D render, no muted desaturated palette, no flat gradient sky, no grain, no painterly brush strokes, no photographic faces

## Style Motion

Full animation, not limited — the opposite of the held-frame idiom. The atmosphere is the primary mover: light shafts sweep and particles fall continuously even when the figure is still. Camera moves with weight and commitment, never with a stutter. No stutter, no shooting on threes, no held frames with only the hair moving. (Source: the `Motion character` of the style card `luminous-anime`.)

---

# 19. GENERATION INSTANCE

## Instance

- Instance ID: `habits-promo-chinatsu-s03-4s-01`
- Segment ID: `01-3`
- Specification Version: `0.1.0`
- Generation Date: `—`

## Resolved Values

- Duration: `4s`
- References: `REF_CHARACTER (frozen pair, CRITICAL) ／ REF_STYLE (luminous-anime, HIGH) ／ REF_SOURCE (bible.yaml, CRITICAL)`
- Temporal Structure: `2 beats, NON_UNIFORM — 2s / 2s. The carrying beat = BEAT 2 at 2s (50%), carried by omission rather than by length`
- Camera Events: `1 event as listed in §10. One continuous take`
- Action Events: `ACT_SPEAK → ACT_OMIT`
- Audio Events: `Japanese speech, words unwritten ／ no effects ／ fluorescent room tone under the voice ／ no music`
- Output: `1920×1080, 24fps, 16:9 landscape, single clip`

# 20. ITERATION

## Version

`0.1.0` — first pass, not yet generated.

## Observed Problems

- _(none yet — to be filled after the first generation)_

## Anticipated risks (to check in the first generation)

- **Subtitles may be burned in.** ⚠️ **これは反転した危険である。** この一段は一度、字幕が焼かれた——
  そのときの原因は「**発話を名指していた**」ことであり、打った手は**発話を名指す語を落とすこと**であった。
  **いま `Master Prompt` は発話を名指す**（「**she is still speaking**」）——**ゆえに同じ危険が戻っている。**
  ⚠️ **担い手は `Negative` である**（字幕の五節＋基盤の `no on-screen subtitles`）。
  **再投入の結果が、この手が効いたかどうかを言う。**
- **The voice may come out as the wrong language.** Wan's default is Chinese. `Audio Prompt` and `Master Prompt` both name Japanese; **that is a specification, not a guarantee.**
- **The voice may read as narration.** ⚠️ **部屋の音が落ちれば、その声は画の上の声になる**（§16 MUST NOT）。
- **The gaze may come to the lens.** This is the shot where a talking face most easily finds the camera. It goes to the listener's side, and the frame edge is where the listener is.
- **The listener may be invented** — a shoulder, a silhouette, a reflection, a pair of hands on the desk. The frame edge is the listener.
- **The words may be invented and put in her mouth.** ⚠️ **この一段は台詞を書いていない**——ゆえに**生成器が書く。** それは**この作品の決定ではない**が、**避けられない**（声を置けば、語が要る）。
  ⚠️ **避けられるのは、その語が読まれることである**——**字幕を出さない。**
- **The shot may run long.** At four seconds the missing name is visible; stretched, the same content reads as a pause rather than an omission.
