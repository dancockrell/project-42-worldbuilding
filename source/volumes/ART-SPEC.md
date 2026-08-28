# PROJECT 42 — ART SPECIFICATION

**Volume II of the lore bible.** Executable form of LORE-BIBLE.md §6.

§6 states the direction. This states how to produce it without its author in
the room. Every prompt block below is meant to be pasted, not interpreted.

Owner: lore thread. Written 27 Aug 2026, unexecuted — the GPU has been pinned
at 100% by another job. Nothing here has been run yet, and that is stated
plainly rather than left to look finished. When it is run, record what came out
in §8 below, including what failed.

---

## 1. Production tiers — read this before generating anything

1500 unique card illustrations is the wrong target and would be wrong even with
infinite GPU. Card games do not work that way, and a pool of 1500 individually
generated images at consumer quality would read as *noise*, not richness —
inconsistency is far more visible than repetition at this scale.

The target is **legibility per faction and branch**, which is what Red Alert
gets right (bible §3): you should identify a card's allegiance from across a
table, from silhouette and palette alone.

| Tier | Count | What it is |
|---|---|---|
| **A — Commanders & Aces** | 6 | Fully bespoke. Wexford, Subject 42, Die Glocke, Der Knochenmann, Amatsu, Nue. These carry the game's face; they get individual attention and iteration. |
| **B — Branch archetypes** | 9 | One strong illustration per faction-branch (P42 Chrono/Phase/Current, WN Kadaver/Bestiarium/Seuche, HY Fog/Oni/Shrine). These do the heavy lifting. |
| **C — Variants** | ~60 | 6–8 compositional variants per branch, generated from the branch prompt with the subject bank in §5. Cards within a branch draw from its variant set. |
| **D — Everything else** | remainder | Uses its branch's tier-C set. Distinguished by frame, name, and stat block, not by unique art. |

**Generate in order A→D and stop when it looks right.** Tier C is where the
returns flatten. Do not start at D.

---

## 1a. THEIR OWN FACE OUTWARDS - the governing principle of this spec

**Dan, 27 Aug 2026:** *"we should use japanese art to represent japanese. this
will give them their own proud look. same with germans... not the usa look
towards them, but their own face outwards."*

**Every faction is depicted in its own visual tradition, as it wished to be seen.
Never through an enemy's eyes.** This outranks every prompt block below; if one
of them drifts from it, the block is wrong.

I had a version of this as a defensive rule for one faction - avoid reproducing
the Allied caricature of Japan. Dan's framing is better and it generalises,
because it is *positive*: propaganda is a nation's **face outwards**, the image
it chose to present. Using it means each faction appears proud, capable and
dignified, drawn in a real artistic tradition rather than in the distortion its
enemies made of it.

### Why this makes the game harder, not softer

- **Rule 5 - monstrous and capable.** A dignified, competent enemy is far more
  frightening than a cartoon, and incompetent evil is a comforting lie.
- **It is more damning, not less.** Showing the Empire's own proud self-image is
  not softening it. It is showing what these regimes *believed about themselves*
  while doing what they did. A caricature lets the viewer off. A magnificent
  poster for something unforgivable does not.
- **Section 00 - the question is worth more than the answer.** A noble-looking
  enemy asks a much harder question than a monstrous-looking one.

### And it applies to Project 42, which is the sharp end

If all three factions get their own flattering self-portrait, then **Project 42's
clean heroic recruitment-poster look is also propaganda.** Not the game's
endorsement of them - their own poster, produced by the same instinct that
produced the other two.

**The art style is an unreliable narrator, and every card is a piece of in-world
propaganda.** That is bible rule 6, the Allies get no clean war, carried by the
pictures instead of the documents, and it costs nothing because it is already how
this spec works. The player is looking at three self-portraits. All three are
true to how each saw itself. None of them is the truth.

### Traditions to draw from

- **Hyakki Yako - Japanese.** Ukiyo-e woodblock composition, sosaku-hanga,
  Taisho and early Showa graphic design, nihonga colour sensibility. Flat fields,
  strong outline, asymmetric composition, stylised cloud and wave motifs, gold
  and vermillion.
- **Werk Nachtigall - German.** Sachplakat, the object-poster tradition
  (Bernhard, Hohlwein): bold flat shapes, ruthless simplification, heavy
  silhouette. German Expressionist woodcut for the carved shadow, Jugendstil
  geometry in the banding. A genuinely great graphic tradition, and using it well
  is what makes the faction frightening.
- **Project 42 - American.** WPA and War Department poster idiom, screenprint,
  limited palette, heroic low angle. Also a real tradition, also self-flattering.

**Never reach for one nation's depiction of another.** If a Hyakki Yako image
would sit comfortably in a 1943 US poster about the Pacific, it is wrong. If a
Werk Nachtigall image looks like an Allied cartoon of a German, it is wrong and
it is also *weaker*, because rule 5 says they win battles.

---

## 2. Universal negative prompt — non-negotiable

Paste into every generation, every faction, no exceptions.

```
swastika, nazi insignia, hakenkreuz, SS runes, sig runes, lightning bolt
insignia, thunderbolt insignia, totenkopf,
racist caricature, wartime racial caricature, exaggerated racial features,
hitler, third reich iconography, modern military uniform, modern firearms,
photorealistic, 3d render, cgi, octane, unreal engine, smooth digital
airbrush, contemporary clothing, watermark, signature, text, lettering,
caption, gore, viscera, mutilated bodies, corpses of civilians,
concentration camp, prisoners, emaciated figures, striped uniforms,
children, sexualized figures, nudity
```

Three groups, three different reasons:

- **Insignia** — bible §2 rule 8 and §0c. The Iron Cross is the only mark the
  Kaiser's Axis gets. No swastika, no lightning bolts (the SS Sig runes are a
  lightning-bolt mark; both tokens are here because a generator will draw the
  shape it's given even if it has never heard the jargon name for it) — Dan's
  own words, §0c: *"we don't use the swastica or lightning bolts."* This is
  not a taste call a generator gets a vote on: **there was no Nazi party in
  this history**, so a swastika on a card is not offensive first, it is
  *wrong* first — a continuity error, the same shape as naming Auschwitz on a
  card (bible rule 1). The symbol belongs to a party that does not exist here.
- **Medium** — the whole style rests on the poster layer being *flat and
  printed*. Photorealism collapses the two-layer seam that is the entire idea
  (§3 below), so "photorealistic" is as damaging here as a swastika is
  offensive.
- **Subject** — bible §2 rules 1, 2 and 3. Victims are never depicted, camps
  are never depicted, and no image gets to imply either. This is not squeamish
  about violence in the abstract; it is a hard boundary about *whose* suffering
  becomes decoration. A burning tank is fine. A person in a striped uniform is
  never fine.

---

## 3. The two-layer rule, in generation terms

§6 says keep the seam visible. In practice this is **two passes, not one
prompt**, because a single prompt asking for "1940s poster with glowing anime
effects" reliably produces a smooth blend — which is the one outcome the
direction forbids.

**Pass 1 — the poster.** Generate the base illustration with period vocabulary
only. No effects language at all. Limited palette, flat colour, screenprint
texture, heavy black, visible paper grain, slight registration misalignment.

**Pass 2 — the effect.** Composite the energy/power layer over it with
different rendering rules: lit, saturated, motion-blurred, glowing. Either a
second generation masked in, or hand-composited, or img2img at low denoise
restricted to the effect region.

The gap between the two passes is the style. If a viewer cannot tell that two
different image-making eras are stacked, the pass failed — regenerate rather
than accepting it, because "close enough" here is the failure mode that turns
the whole set generic.

---

## 4. Per-faction prompt blocks

### PROJECT 42

```
1943 american war department recruitment poster, screenprint illustration,
limited four-colour palette, cream newsprint paper texture, heavy black
outlines, flat colour fields, halftone dot shading, slight off-register
printing, low-angle heroic composition, confident square-jawed figure,
period US army uniform 1944, visible individual face, determined expression,
strong diagonal composition, bold geometric background shapes
```
- **Palette:** cream/newsprint base, flag red, navy. Effects layer in electric
  cyan-white.
- **Light:** slightly overexposed, as if photographed with too much flash.
- **Faces:** visible and individual (§6 faces grammar). P42 people are people.
- **Effects pass:** `arcing tesla electricity, cyan-white voltage, branching
  lightning, motion trails, glowing energy` — bright, clean, *optimistic-looking*
  power. The horror in this faction is never in the visuals; it is in the
  documents.

### WERK NACHTIGALL

```
1916 imperial german military propaganda poster, woodcut linocut
illustration, harsh carved shadow, heavy black ink, limited palette of black
iron grey blood red and ochre, cheap state print office paper, coarse paper
grain, stark high-contrast, angular geometric composition, imperial german
uniform 1944, pickelhaube or steel helmet, iron cross insignia, figure with
face obscured by mask respirator or turned away, industrial machinery,
surgical steel, pneumatic apparatus, armoured mecha frame, tank hull,
occult ritual circle rendered as engineering diagram, necromantic rite
staged as a laboratory procedure
```
- **Palette:** black, iron grey, blood red, ochre. Effects in sickly
  yellow-green (Seuche) or surgical-steel white (Kadaver/Bestiarium).
  Occult content gets the same palette as everything else — no gold, no
  luminous purple, no separate "magic" colour language. A summoning circle
  is drawn like a wiring schematic, not like a spellbook.
- **Faces:** covered, replaced, or turned away — **always**. The programme's
  product is not a person, and this is how the art says so without a word.
- **Effects pass:** `industrial steam, pneumatic exhaust, sickly green spore
  bloom, surgical light glare, ritual chalk lines drawn with engineering
  precision, grave soil, exposed bone through augmentation, jet exhaust,
  tank tread mud` — mechanical, biological, and occult in the same register.
  Never luminous or beautiful, and the occult content specifically is never
  awed or reverent — it is drawn the way the rest of the faction is drawn:
  procedural, cold, exact.
- **RULE 4 REVERSED, 28 Aug 2026 — bible §2 rule 4.** The prior hard rule
  banned occult imagery outright ("Werk Nachtigall's power comes from a
  machine shop and a budget"). Dan's ruling: *"lean into the prussian
  fascination with the occult."* Occult imagery — runes, ritual staging,
  necromantic rites, hybrid grafting drawn from both surgery and ritual —
  is now in, drawn in the same flat, cold, procedural register as the
  machinery. **What has not changed and is a separate rule with a separate
  reason:** the iron cross remains the Empire's only insignia (§3 below,
  untouched), and no real atrocity referent (Fischer, Mengele, the camps,
  die Ostordnung) is ever given a supernatural cause or treatment. Add to
  this faction's negative prompt instead: `glowing eyes, luminous magic
  effects, spellbook aesthetic, fantasy-genre color grading, awe or
  reverence in a figure's posture toward the occult content` — the occult
  is real here, not a treated-as-wondrous spectacle.

### HYAKKI YAKŌ

```
1943 imperial japanese propaganda poster fused with ukiyo-e woodblock print,
flat colour fields, strong black outline, sunburst ray composition, palette
of ink black vermillion gold and off-white, visible woodgrain and paper
fibre, stylised cloud and wave patterns, imperial japanese army uniform 1944,
figure with visible serene composed face, calm expression, yokai folklore
motif
```
- **Palette:** ink black, vermillion, gold, off-white.
- **Faces:** visible, and **serene in a way that is wrong for the situation
  around them.** That mismatch is the faction's tell.
- **Effects pass — the one deliberate exception:** render the supernatural in
  **colours absent from the base palette entirely**. Iridescent, wrong,
  belonging to another image. `colours not present elsewhere in the image,
  iridescent bleed, a second picture showing through`. When Hyakki Yakō's
  power appears it should look like a different print is coming through this
  one. This is the only place in the game where the effects layer is permitted
  to break its faction's palette, and it is the whole point.

#### The caricature guard — mandatory, and specific to this faction

Bible §5 makes the fused **dispossessed**, not fanatical. The art has a live and
specific hazard here that the other two factions do not: we are working in 1940s
propaganda idiom, and Allied propaganda of that exact period manufactured the
"fanatical, subhuman, insane Jap" caricature industrially. A generator trained on
period imagery will reach for it if you let the prompt drift.

- **Use the Japanese Empire's own poster idiom, never the American depiction of
  Japan.** This is the single most protective decision in the spec. Keep it.
- Serene, composed, self-possessed features (§6 faces rule). **Never** frenzied,
  snarling, leering, or wild-eyed.
- Never exaggerate or caricature facial features. Add to this faction's negative
  prompt: `caricature, exaggerated features, buck teeth, squinting, snarling,
  leering, wild-eyed, frenzied, racist caricature, wartime racial caricature`.
- Dispossession reads as **stillness**, not distortion. Somebody whose hands are
  being used, not somebody screaming.

If an image would look at home in a 1943 US War Department poster about the
Pacific, it is the wrong image and it is not salvageable by retouching.

#### The watching rule — mandatory on every HY image
§6: every Hyakki Yakō card contains one element reading as an observer, never
stated in any card text. Rotate through these so it is never the same trick:

- a negative-space eye shape in a cloud or wave pattern
- a shadow that does not match the object casting it
- a reflection containing one more figure than the scene
- a gap in a crowd exactly person-shaped
- one window lit in an otherwise dark structure

**This is a checklist item at review, not a hope.** An HY image without one is
rejected and regenerated. Players should find it themselves around card forty
and get a chill — that discovery is worth more than any flavour text saying
they are being watched, and it only works if it is *always* there.

---

## 5. Subject banks for tier-C variants

Combine `[faction block] + [branch subject] + [composition]`.

**P42 — Chrono:** a retrieval frame mid-cycle · a soldier half-present · a
clock face with too many hands · an arrival platform, scorch-ringed
**P42 — Phase:** a figure walking through a wall · a soldier casting two
shadows · an outline where someone stood · a corridor seen from inside a wall
**P42 — Current:** coils and arcs · a man as a circuit · a substation at night
· wire strung between raised hands

**WN — Kadaver:** an operating theatre, empty, lit · surgical steel laid out ·
a figure with replaced limbs · a gurney in a corridor
**WN — Bestiarium:** a powered frame, unoccupied · kennels at dusk · a stall
with the door open · harness and muzzle on a hook
**WN — Seuche:** fungal bloom on concrete · a sealed ward door · spore drift in
a searchlight · a boot print filling in with growth

**HY — Fog:** a treeline dissolving · a patrol half-erased · lanterns in mist ·
a road that stops
**HY — Oni:** a mask mid-strike · a drum on scorched ground · a figure
outlined in wrongness · hands around a haft
**HY — Shrine:** a torii at the wrong hour · offerings, untouched · a bell rope
moving · a shrine with its doors open onto nothing

**Composition modifiers:** low heroic angle · flat frontal poster composition ·
extreme foreshortening · silhouette against a sunburst · framed by geometric
banding

---

## 6. Review checklist

Every image, before it ships:

- [ ] No banned insignia. Iron Cross where German heraldry appears.
- [ ] Poster layer reads as *printed* — flat, grainy, limited palette.
- [ ] The two-layer seam is visible. Not blended.
- [ ] Faces obey the grammar: P42 individual · WN covered/turned · HY serene.
- [ ] **WN only:** zero occult content. Any mystical element = discard.
- [ ] **HY only:** the watching element is present and is not last card's trick.
- [ ] No depiction of victims, camps, prisoners, or anything implying them.
- [ ] Legible at card size. Check at 300px wide, not at 1024.

That last one fails more images than everything else combined. Bible §16's
lesson applies: look at the artefact at the size it will actually be seen, not
at the size it was generated. A composition that is magnificent at 1024px and
mud at 300px is a failed card.

---

## 7. Practical notes

- Target hardware is a 12GB RTX 4070 running ComfyUI. SDXL-class at 1024×1024
  fits comfortably; plan around that rather than assuming headroom.
- **Check the licence before downloading any model or LoRA.** Dan builds
  commercially. Apache-2.0 / MIT / BSD are safe; a great many popular
  checkpoints and virtually all the well-known upscalers are non-commercial.
  This has already caught two models on this machine.
- The GPU is contended. `quartermaster` exists for exactly this:
  `qm queue <name> --cmd "..." --requires nvidia-gpu --not-while ComfyUI`
- Generate at 4:3 or square and crop to the card frame. Do not generate at card
  aspect — the compositions above need room.

---

## 8. Execution log

Nothing generated yet. GPU pinned at 100% / 11.6GB by another job as of 27 Aug
2026 12:5x.

When runs happen, record here: what model, what settings, what worked, and
**what failed and why**. A spec that only records its successes will quietly
drift back toward whatever the model likes to produce, which for every one of
these prompts is smooth digital painting — the single thing §6 forbids.
