# Project 42

Shared worldbuilding for an alternate-history Second World War, fought by three
systems.

**Read it here: https://dancockrell.github.io/project-42-worldbuilding/**

This repository is the universe. The games are built from it and link back to
it — [World Aflame](https://github.com/dancockrell/world-aflame-godot) is the
card game, and The Long Night and Ghost Front are the same setting from other
angles. Lore lives here so that no single game owns it and no single game's
context can lose it.

---

## The argument

The Kaiser is still on the throne in 1944. There were never any Nazis. And the
horror happened anyway — because the machinery predated the man everyone
blames, and it had chairs, and funding, and respectable people running it.

It is a war of systems rather than of people. The three systems are monstrous.
The people inside them are exemplars of their own cultures, doing things that
were, at the moment they did them, entirely justified in their own minds.

- **Project 42** — the Allies. Time travel, electricity, phasing, and the
  United States.
- **Werk Nachtigall** — the Kaiser's Empire. Walking frames, hybrids, jets,
  and the Prussian fascination with the occult.
- **Hyakki Yakō** — the Empire of Japan. Folklore, bushidō, and something
  older that is feeding them.

---

## What is in here

| | |
|---|---|
| **`LORE-BIBLE.md`** | The authority. Where the bible and anything else disagree, the bible wins. Read §00 before writing a word of fiction. |
| **`source/volumes/`** | 36 deep documents — factions, sites, characters, timeline, art and sound direction. |
| **`source/cards/`** | One entry per card. A hundred words of bio, five hundred of story. |
| **`docs/`** | The generated site. Do not edit by hand. |

## Cards

Every character, animal or thing that acts gets two pieces:

**A hundred-word bio** carrying the power fantasy — what it is, what it does,
why you want it.

**A five-hundred-word story** selling the character. A card is S-tier here
because it has an interesting part in an interesting story, not because it
hits hard.

Stories are thought experiments. Each one has a thesis, and the thesis is
demonstrated by construction rather than stated by a narrator. Characters are
not liars; they have limits — of circumstance, of culture, of mind — and they
report exactly what they perceive, and the reader sees past it.

## Building the site

```bash
python tools/build.py
```

Stdlib only. No dependencies, no npm, no build tooling. Writes `docs/`, which
GitHub Pages serves. It refuses to build a site from zero cards, because an
empty build and a broken parser look identical from the outside.

---

*The Answer is 42. Nobody knows the Question. An answer without its question
explains nothing, and the whole comedy is that the number is useless and
everybody wanted it anyway.*
