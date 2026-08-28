# How to write a card

Every entry is three things: a picture, a hundred words, and a story of five
hundred. Nothing else. Read this whole page before you write your first one —
seven people are writing these and they have to read as one hand.

---

## 1. The picture

An image and a caption. The caption says what is in the frame, plainly, and
does not editorialise about it. Art direction lives in
`source/volumes/ART-SPEC.md` and it governs — including the iconography rule:
**the Iron Cross only for the Kaiser's Empire. Never a swastika, never
lightning bolts.** There was no Nazi party in this world, so a swastika is a
continuity error before it is anything else.

## 2. The Draw — a hundred words

What it is, what it does, and why you want it in your deck. This is the part
that makes a reader want to play the card, and it should be specific enough to
be frightening or thrilling rather than impressive in the abstract.

Concrete numbers beat adjectives. *Four hundred pounds, runs down a horse,
takes commands by whistle at eleven hundred metres* tells you more than
*terrifyingly powerful*. One detail that is slightly wrong is worth ten that
are merely large — the brass plate riveted behind the ear, because the Office
labels its property.

## 3. The story — five hundred words

**This is the part that decides whether the card is any good.** A card is
S-tier here because its character has an interesting part in an interesting
story, not because it hits hard.

### Write the thesis first

Before a word of prose: **what is this story arguing?** One sentence. A story
is a thought experiment — it constructs a scenario that carries the reader to
a position, and the interest is in the position, not in a twist.

Then, and only then, choose the location, the characters and the situation
that will demonstrate it. In that order. A story assembled the other way round
is a scene, and a scene argues nothing.

The thesis should be **punchy and interesting**, and it should hold up in a
university literature seminar. If you cannot say it in one sentence, you do not
have one yet.

### The narrator is not lying

Characters are never liars. They have limits — of circumstance, of culture, of
mind — and inside those limits they tell you **exactly what they perceive to
be true.** The reader sees past it. That gap is where the whole effect lives.

And find the justification. When a character does something monstrous, they had
a reason at the moment they did it, and it was sufficient to them then. Your
job is to **locate that reason**, not to invent an excuse and not to withhold
it. If you have not found it, the story is not finished.

### Show it. Do not preach it.

No line of the story tells the reader what to think. The construction does the
arguing. If your last paragraph explains the point, cut the last paragraph —
the story was already over.

---

## The prose

**Magical realism.** The marvellous is reported in the same voice as the
weather. Nobody in the story is astonished by it. Eleven letters arrive with no
postmark and the officer writes *provenance unrecorded* and moves on to the
next form, because that is his job and the letters are not his department.

**Márquez, not Hemingway.** This is the correction most likely to be needed.
Sentences may run long and warm and accumulate; a clause may carry a whole
history; heat and smell and cloth and food belong in the prose. Terse is
allowed at a moment of impact and nowhere else. **Never more clipped than
Hemingway, and usually a long way from him.**

**No exposition.** Nothing stops to explain the world. If a reader needs to
know a thing, a character does something that shows it.

**Everything is an action.** Actors act: people, animals, and things that
move. The sun does not rise in these stories. Scenery is background and stays
background — it is not the subject of the sentence and it is not the character.

**Every line earns its place.** Go through line by line and ask why each one
is there. This is not an instruction to cut until it is short. A line that
carries weather, or a hand, or a grudge, has earned it; a line that reports a
procedure nobody cares about has not.

---

## The setting's own argument, which every story serves

It was an inhumane war fought by **systems**, not by people. There are three
systems and all three are monstrous. The people inside them are **exemplars of
their own cultures** — competent, cultured, often decent — doing things that
were, at the moment they did them, entirely justified in their own minds.

Every faction has to be **cool**. A player picks a side and it should feel
great. Horror and cool are both required and they are not in tension.

`LORE-BIBLE.md` governs everything here, and §2 overrides even this file.
Where a story and the bible disagree, the bible wins.

---

## Source format

```
# CARD NAME
faction: wn | p42 | hy
type: Unit | Commander | Ace | Event
tier: S | A | B | C
image: art/slug.png
image_caption: What is in the frame.

## Draw

A hundred words.

## Story

### STORY TITLE

Five hundred words.
```

Save as `source/cards/<faction>/<slug>.md`. Then:

```bash
python tools/build.py
```

It refuses to build from zero cards rather than write a site that looks
finished, and it prints how many it parsed. Check that number against how many
you wrote.
