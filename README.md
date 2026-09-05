# Project 42

> **Scope and authority, 5 September 2026:** this repository preserves the alternate-WW2 setting used by World Aflame and earlier related games. It does not govern the fantasy Pirate Island RTS. World Aflame has been retired and both game repositories were deleted on 5 September 2026. [The retained tone correction](#retained-tone-correction) supersedes thesis-driven and bureaucracy-as-horror guidance: new writing uses pulp adventure, without preaching. Older passages remain development evidence, not permission to revive the rejected direction.

Shared worldbuilding for an alternate-history Second World War, fought by three
systems.

**Read it here: https://dancockrell.github.io/project-42-worldbuilding/**

This repository is the universe. The games are built from it and link back to
it historically — World Aflame was the card game, and The Long Night and
Ghost Front explored the same setting from other angles. The World Aflame
repositories have now been deleted. Lore lives here so that no single game owns it and no single game's
context can lose it.

---

## Historical setting rationale

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
| **`LORE-BIBLE.md`** | The retained WW2 lore corpus, subject to the later correction and unresolved cross-repository divergence described above. Its historical claim of unconditional precedence is superseded. |
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

New stories should deliver character, action, and pulp-adventure stakes. The earlier requirement to construct each story around an argumentative thesis is superseded by the later tone correction. The retained source corpus has not been comprehensively rewritten or reconciled by this documentation audit.

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

---

## World Aflame retirement

On 5 September 2026, the owner explicitly directed permanent deletion of `dancockrell/world-aflame` and `dancockrell/world-aflame-godot`. Both game repositories were deleted. This separate lore repository remains historical reference; it is not an active World Aflame implementation or a mandate to resume the old game.

If card-game work returns, start with one coherent design document for the desired Snap-style game. The old rules, faction model, lore, and technical implementation are not automatically requirements for that future project.

The former two-copy lore-divergence notice is historical. It does not describe two currently available GitHub sources or an active synchronization task.

## Retained tone correction

The later correction formerly recorded in World Aflame Godot issue 18 required pulp-adventure tone, rejected bureaucracy and paperwork as the horror device, and rejected preaching or a mandatory argumentative thesis. This summary preserves that correction for interpreting the remaining WW2 corpus now that the source issue's repository has been deleted. It does not make the corpus design authority for Pirate Island or a future card game.
