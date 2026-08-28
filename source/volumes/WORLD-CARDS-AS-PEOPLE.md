# PROJECT 42 — VOLUME XII: CARDS AS PEOPLE

How 1500 cards become 1500 characters, and a constitutional ruling that had to be
made before a single Werk Nachtigall bio could be written.

---

## 1. The gap, found while building the spoke layer

The commission is a bio per card. That requires every card to map to a person.

**Project 42 and Hyakki Yakō are straightforward.** Their cards are personnel — a
Current Warden is a soldier, a Kitsune-Warden is somebody folklore was fused
onto. Both are people already.

**Werk Nachtigall is not**, and working out why exposed something the
Constitution had left open.

A Muster 12 is a *product*. Its bio would have to be about **whoever it was made
from** — and Volume IV establishes that the Office is downstream of *die
Ostordnung*, that the camps come first, and that the programme uses what they
produce.

Follow that one step further and a Werk Nachtigall card becomes **a genocide
victim with a Power value**, which is **rule 2**, which is the rule this entire
universe was built to protect.

Nobody had flagged this. It was reachable from published canon in two steps.

---

## 2. The ruling

**Rules 1–3 override §00.** Ordinarily this setting leaves hard questions open —
that is the method. **This one gets a definite answer**, because an ambiguous
answer means a player could reasonably read a card as a murdered person, and rule
2 exists precisely to make that unreadable.

> **Werk Nachtigall's material is condemned criminals, prisoners of war, and the
> Office's own failed personnel. It is never the victims of *die Ostordnung*.**

And the reason it is never them is **not** that the Office has scruples. The
Office has no scruples. It is:

**The paperwork does not permit it.**

Victims of *die Ostordnung* are accounted for by a different ministry, under a
different appropriation, on a schedule Section VI has no authority over.
Transferring material across that boundary would require an inter-departmental
disposition with signatures from two offices that have never corresponded, and
**there is no form.** Somebody would have to create one. Creating one would
require explaining, in writing, what it was for.

**So it has never been done, and the reason it has never been done is that it
would be a nuisance.**

### Why this is the right answer rather than a convenient one

It is worse than the alternative, not softer.

An Office that declines on moral grounds would be an Office with a conscience,
and rule 7 forbids that — the institution is never sympathetic. **An Office that
declines because the filing is difficult is exactly what this faction is**, and
it says something true about how bureaucracies actually constrain atrocity: not
by objecting, but by being slow, territorial, and jealous of their own
appropriations.

**It also keeps the ordering intact** (Volume IV §6). *Die Ostordnung* remains
the larger horror standing behind the fiction, unreached by any mechanic,
untouchable by any player. Werk Nachtigall's programme is downstream of it in
*budget and personnel and precedent* — which is what Volume IV actually said —
without a single victim becoming a playable piece.

### What this permits and forbids

**Permitted:** a Muster 12's file, naming a condemned man's sentence and the date
the transfer was approved. A Baureihe 7 requisition. A Gestell 4 disposition
where the occupant is a serving soldier who cannot get out.

**Forbidden, and no game may write it:** any implication that a unit's material
came from a camp. Any card, line, image or bio that would let a player conclude
it. **`tools/lore-check.py` cannot catch this** — it is a matter of implication,
not vocabulary — so it is a human review item and it is stated here so that
review has something to check against.

---

## 3. What a card's bio actually is, per faction

Each is a **document**, per Volume IX. The document *type* is the faction's
relationship to personhood, expressed as an artefact.

| Faction | The bio is | Names the person? |
|---|---|---|
| **Project 42** | A personnel file, incident report, or denied requisition | **Yes.** P42 people are people and the file says so. |
| **Werk Nachtigall** | A disposition, an estimate annexe, a theatre log | **Almost never.** The Office numbers products. A name appearing at all is an event. |
| **Hyakki Yakō** | A letter, a ward observation, a ceremony record | **Yes, and it matters.** They are people, and the programme's own paperwork keeps saying so even while treating them otherwise. |

**That table is the faces rule from §6 of the bible, in prose form.** P42 faces
are visible and individual. Werk Nachtigall faces are covered or turned away.
Hyakki Yakō faces are visible and serene in a way that is wrong. **The bios
should do exactly what the art does**, and a reader who never sees a card image
should still be able to tell the three factions apart from the documents alone.

### The Werk Nachtigall exception, and it is the faction's best material

**When a Werk Nachtigall bio *does* name someone, that is the whole point of the
bio.**

The Office's files are numbers. So a file with a name in it — because a clerk
wrote one in, because a physician appended something, because somebody's hand
slipped into the margin — is an anomaly, and the anomaly is the story.

*"The disposition carries a name in the margin, in a different hand, unsigned. It
has not been actioned."*

**Use this sparingly.** One in twenty, at most. Its power is entirely in being
rare.

---

## 4. Spokes: how a card becomes a character

Volume X build order, step 3. A spoke has **two or three edges, at least one to a
hub.**

### The generation rule

For a card with noun *N* and branch *B*, in faction *F*:

1. **Attach to the obvious hub.** The noun implies it. A *Current Warden* attaches
   to Bright or Deel. A *Muster 12* attaches to Aust or Brehm-Sandt. A
   *Miko-Sentinel* attaches to Amatsu.
2. **Add one conflicting edge** (Volume X §2). Not to the same hub. This is what
   makes the character rather than the role.
3. **Optionally add one lateral edge** to another spoke — this is what makes the
   network dense rather than a star, and density is what makes the periphery
   interesting later.

**A spoke with only step 1 is a role, not a character.** Reject it and re-roll,
the same way a node with no conflicting edges gets re-rolled.

### Seeded spokes, as worked examples

```jsonl
{"id":"corp_haines","name":"Corporal Wilma Haines","faction":"P42","noun":"grounding crew","edges":[
  {"to":"deel_marcus","axis":"COMMAND","w":0.6},
  {"to":"deel_marcus","axis":"BLAME","w":0.6,"note":"she laid the bus that fed Frame Two, to his drawing"},
  {"to":"fitch_aurelio","axis":"COHORT","w":0.9,"note":"they trained together"}]}

{"id":"pfc_okonkwo","name":"Pfc Daniel Okonkwo","faction":"P42","noun":"departure clerk","edges":[
  {"to":"prentiss_ida","axis":"COMMAND","w":0.3},
  {"to":"reyes_whitlock_tomas","axis":"REGARD","w":0.7,"note":"signs him out every time and has started saying his name twice"},
  {"to":"falk_naomi","axis":"KNOWLEDGE","w":0.3,"note":"has noticed she is at the mess more often than she eats"}]}

{"id":"unterarzt_grau","name":"Unterarzt Peter Grau","faction":"WN","noun":"patients","edges":[
  {"to":"aust_helene","axis":"COMMAND","w":0.7},
  {"to":"aust_helene","axis":"REGARD","w":0.6,"note":"he admires her and does not know what she files"},
  {"to":"section_six","axis":"FEAR","w":0.7}]}

{"id":"gefr_lindt","name":"Gefreiter Anselm Lindt","faction":"WN","noun":"walkers","edges":[
  {"to":"pflug_otto","axis":"COMMAND","w":0.5},
  {"to":"pflug_otto","axis":"DEBT","w":0.8,"note":"Pflug got him out of one in November and neither has mentioned it"},
  {"to":"section_six","axis":"BLAME","w":0.6,"note":"recovery was costed twice and declined twice"}]}

{"id":"sotsu_mifune","name":"Superior Private Kaoru Mifune","faction":"HY","noun":"karakasa-sentry","edges":[
  {"to":"ishida_captain","axis":"COMMAND","w":0.6},
  {"to":"ishida_captain","axis":"REGARD","w":-0.3,"note":"Ishida told him the treaty protects them and he believed it once"},
  {"to":"the_watcher","axis":"FEAR","w":0.5}]}
```

**Note what the second edge does in every case.** Haines is commanded by the man
she blames. Okonkwo has started saying a vanishing man's name twice, and nobody
has told him to. Grau admires a woman whose filings he has not read. Lindt owes
his life to his commander and blames Accounts, correctly, for the two men still
out there. Mifune believed something once.

**None of that is in the card. All of it is in two edges.**

---

## 5. Open, deliberately

- Whether anyone at Hollernbruch has ever proposed the transfer, and what
  happened to the proposal.
- Whether Okonkwo has worked out why he says the name twice.
