# PROJECT 42 — VOLUME X: THE CHARACTER NETWORK

**The commission:** bios for 1500 cards, ~500 words each, across three factions,
with weighted relational networks.

**The arithmetic, stated first:** 1500 × 500 words is roughly **750,000 words**.
That is ten novels. Hand-writing it is not available, and generating it flat from
templates produces 1500 versions of the same person with different nouns — the
exact failure the card flavour just had, at fifty times the scale.

**The second half of the commission solves the first half.** Characters are not
interesting in isolation; they are interesting *in relation*. A line like *"he
has not spoken to Osei since Frame Two"* is alive, and no template produces it.
A **graph** produces it.

So the network is not a diagram of the characters. **The network is what
generates them.**

---

## 1. The eight axes

Each edge is **directed unless marked**, and **weighted 0.0–1.0** unless marked
signed. Direction is where the drama lives: A owing B is a completely different
story from B owing A.

| Axis | Direction | Range | What it means |
|---|---|---|---|
| **COMMAND** | directed | 0–1 | Formal authority. A can order B. |
| **DEBT** | directed | 0–1 | A owes B. Life, favour, silence, money, a signature. |
| **BLAME** | directed | 0–1 | A holds B responsible. **May be unjust — that is permitted and often better.** |
| **KNOWLEDGE** | directed | 0–1 | A knows something about B. Asymmetric by nature. |
| **FEAR** | directed | 0–1 | A is afraid of B. |
| **REGARD** | directed | **−1 to +1** | Affection through contempt. The only signed axis. |
| **PROXIMITY** | *undirected* | 0–1 | Shared space. Barracks, ward, kennel line, watch, corridor. |
| **COHORT** | *undirected* | 0–1 | Arrived together, trained together, or survived the same thing. |

**Why eight and not four:** four axes produce four kinds of person. Eight
directed axes produce a space where two characters can be near each other on
six and opposite on two, which is what a real relationship is.

---

## 2. The engine: character comes from axis conflict

**A node with no conflicting edges is boring, and this is measurable.**

The generator's job is not to fill in a person. It is to find **tension in a
node's edge set** and write from it. Conflict pairs that produce a character
almost automatically:

| Tension | The person it makes |
|---|---|
| High COMMAND **+** high DEBT (same target) | Someone who gives orders to a person they owe. |
| High REGARD **+** high BLAME | Loves them, holds them responsible. The most human one. |
| High COMMAND **+** high FEAR | Commands someone they are afraid of. |
| High KNOWLEDGE **+** low REGARD | Knows something and does not care enough to use it. Or does. |
| High KNOWLEDGE **+** high REGARD | Knows something and is protecting them by not saying it. |
| High PROXIMITY **+** negative REGARD | Cannot get away. Sees them daily. |
| High COHORT **+** high BLAME | Survived the same thing and blames them for it. |
| High DEBT **+** negative REGARD | Owes someone they cannot stand. |

**Rule for generation:** a bio requires **at least two conflicting edges**. A
node that has none gets re-rolled or gets a new edge, not a flat bio.

**Rule for quality:** the *strongest* conflict becomes the spine of the bio. The
rest become the texture.

---

## 3. Hubs and periphery — how 1500 becomes tractable

Real fictional universes are not flat. They have a small number of deep
characters and a large number of people defined by relation to them.

- **Hubs (~40, hand-written).** High degree. Wexford, Falk, Prentiss, Deel,
  Brehm-Sandt, Aust, Pflug, Amatsu, Ishida, and the settled roster. These carry
  real weight and get written properly.
- **Spokes (~200, guided).** Two or three edges, at least one to a hub.
  Generated from the engine with hand review.
- **Periphery (the rest).** One or two edges, usually to a spoke. Their bio is
  interesting **because of who it references**, not because of its own depth.

**This is the trick and it is why the fifteen-hundredth bio can be as good as
the first.** A peripheral gunner is dull described alone. The same gunner is
interesting the moment his file says he was on the detail that carried Fitch out
of the Frame Hall, because the reader already knows about Fitch. **The network
does the work the prose cannot.**

Density matters more than depth at the edges. Keep adding edges rather than
adding paragraphs.

---

## 4. Bio structure — the 500 words

Six movements. Each bio is a **document that exists in the world** (Vol IX), not
narration about one.

1. **The frame** (~30 words). What kind of document. Personnel file, incident
   report, requisition denial, letter, ward log, estimate annexe.
2. **Identity** (~60). Name, role, origin, and how they came to be here. Flat.
3. **The record** (~120). What they have done, in the institution's own voice.
   Understated. The paperwork does not editorialise.
4. **The relation** (~140). **Drawn from the strongest conflicting edge.** This
   is the spine and it is the only part that is really about a person.
5. **The contradiction** (~100). What the record and the relation cannot both be
   true about.
6. **What is not in the file** (~50). The §00 slot. **Every bio ends
   unresolved.** No exceptions — this is the house style and it is the reason
   the set does not read as closed.

---

## 5. Worked example — Captain (Dr) Naomi Falk

Generated from her edge set, not from a template. Her edges:

```
Falk --COMMAND--> (none)          Wexford --COMMAND--> Falk        0.8
Falk --DEBT--> Halloran-Sze       0.9   (deceased)
Falk --KNOWLEDGE--> Reyes-Whitlock 0.9
Falk --REGARD--> Reyes-Whitlock   +0.8
Falk --BLAME--> Wexford           0.5
Falk --FEAR--> Prentiss           0.3
Prentiss --KNOWLEDGE--> Falk      0.4
Falk <--PROXIMITY--> Reyes-Whitlock 0.7
```

**Strongest conflict:** KNOWLEDGE 0.9 + REGARD +0.8 toward the same person,
against COMMAND 0.8 from Wexford requiring her signature on a form that
understates exactly what she knows. That is the spine and the bio wrote itself
from it.

---

> **CAMP IRON BELL — MEDICAL SECTION**
> Officer's record. Falk, Naomi, Capt. (MC). Appended: standing authority to
> sign W.D. 42-C.

Captain Falk came to Iron Bell in September 1943 from a station hospital in
Georgia, on a transfer she did not request and was not asked about. She is a
physician of ordinary competence and unusual patience. The camp has no other
doctor.

Her authority is narrow and total: she signs the coherence codes. **Every
condition code on every W.D. 42-C at Camp Iron Bell carries her initials**, and
the form is the only instrument the programme has for saying whether a man is
still reliably present.

She stopped believing the bands in June.

The tables were written to be signed rather than to be true, and she did not work
that out herself — Dr Miriam Halloran-Sze, settled, read them in her first week
and said so plainly, and then died of a stroke in February with nothing filed.
Falk has her notes. Falk has never filed them either, and the reason is in the
second paragraph rather than the first: **there is no other doctor.** A physician
who refuses to sign is a physician who is replaced by a physician who will, and
Falk has done the arithmetic on who that would be and what it would cost the men
on the establishment.

So she signs. **She has signed 3-C SATISFACTORY on Able Seaman Tomás
Reyes-Whitlock eleven times**, most recently three weeks ago, and she has watched
people stop noticing him in rooms and then apologise when he speaks. She sits
nearer to him at mess than her rank requires. He has asked her one question,
twice, and she has not answered it, and she is the only person at Iron Bell who
knows what the question was.

The record shows an officer performing her duty without exception. The relation
shows a woman who knows the duty is a lie and performs it anyway for reasons she
would defend to a board. **Both are accurate. The file has room for one.**

> *Not in the file: whether she has ever considered that Halloran-Sze also
> chose not to file, and whether that was the same decision.*

---

## 6. Data format

For the generator. One node file per character, edges separate so they can be
weighted and re-weighted without touching prose.

```json
{
  "id": "falk_naomi",
  "name": "Captain (Dr) Naomi Falk",
  "faction": "P42",
  "tier": "hub",
  "role": "medical officer",
  "doc_frame": "officer_record",
  "origin": {"native": true, "year": 1908}
}
```

```json
{"from": "wexford_norman", "to": "falk_naomi", "axis": "COMMAND", "w": 0.8}
{"from": "falk_naomi", "to": "reyes_whitlock", "axis": "KNOWLEDGE", "w": 0.9}
{"from": "falk_naomi", "to": "reyes_whitlock", "axis": "REGARD", "w": 0.8}
{"from": "falk_naomi", "to": "wexford_norman", "axis": "BLAME", "w": 0.5}
```

**Weights are re-tunable without rewriting anybody**, which is the point of
keeping them out of the prose.

---

## 7. Per-faction network shape

The three networks should not look alike. **The shape of a faction's graph is
characterisation.**

- **Project 42** — dense PROXIMITY and COHORT, thin COMMAND. A small camp where
  everyone knows everyone and rank matters less than the roster suggests. High
  KNOWLEDGE asymmetry: Prentiss is a hub on that axis alone.
- **Werk Nachtigall** — **COMMAND-dominated and almost entirely acyclic.** A
  hierarchy, not a community. The distinguishing feature is that **Section VI has
  high COMMAND edges to people it has never met**, and REGARD is near zero
  everywhere, which is what an institution rather than a workplace looks like on
  a graph.
- **Hyakki Yakō** — **the axis that matters is one the other two do not have.**
  Every fused person carries a maximal, permanent, unreciprocated edge to a node
  that is not a character and never appears: *the watcher*. It has KNOWLEDGE 1.0
  of everyone it selected and REGARD undefined. **Do not give it a REGARD value.
  That undefined field is the faction.**

---

## 8. Build order

1. **The 40 hubs**, hand-written, and their edges. In progress — Volumes III–VII
   already contain most of them.
2. **The edge set between hubs.** Cheap, high-value, and it is what makes the
   spokes worth generating.
3. **Spokes**, generated against the conflict engine with review.
4. **Periphery**, generated, referencing spokes and hubs.
5. **Re-weight and regenerate.** Because the weights are separate from the prose,
   the network can be tuned after the fact.

**Do not start at 4.**

---

## 9. Open, deliberately

- Whether the watcher has edges to anyone it did **not** select.
- Whether Prentiss's KNOWLEDGE edges are as high as they look or she is simply
  attentive.
- What Reyes-Whitlock asked Falk.
