# HYAKKI YAKŌ — THE FUSED ROSTER

The twenty-five folklore forms, fixed and branch-assigned. **Naming decisions
here are made, not proposed.**

Closing a gap found by `downloads-22` during the domain-7 audit: Werk
Nachtigall's twenty-four creature types were canonised in `WORLD-BESTIARY.md`
§6a and assigned to branches. **Hyakki Yakō's twenty-five existed only in
`card_generator.gd` and a flavour bank** — never ratified, never assigned, never
stated to be canon. In the project's most sensitive domain.

---

## 1. THIS IS NOT A BESTIARY, AND THE DIFFERENCE IS THE WHOLE POINT

`WORLD-BESTIARY.md` catalogues **products** — things the Office made, out of
material, on a budget. It is a list of what exists.

**This is a list of what was done to people.**

Every entry below names a **person** and the folklore fused onto them by
something that did not ask. A Kitsune-Warden is not a kind of creature. It is a
railway clerk, or a fisherman, or a schoolteacher, with kitsune fused onto them
in a ninety-minute ceremony that may have done nothing.

**The moment this list reads as a bestiary it has become the caricature**, and
the guard in `LORE-BIBLE.md` §5 is not decorative:

- **Dispossession, never frenzy.** Stillness, not screaming. The calm is the
  horror.
- **Never fanatical, never raving, never ecstatic.** That is the image Allied
  propaganda manufactured industrially in this exact period, and we work in that
  period's visual idiom, so the risk is live rather than theoretical.
- **Test:** if a line would read worse coming from a 1943 US War Department
  poster, it is the wrong line.

**A second, quieter risk applies to this list specifically.** Twenty-five
Japanese folklore terms in a column, assigned to categories, is exactly the shape
of a nineteenth-century catalogue of somebody else's culture. **What keeps it
from being one is that each entry is a person and the page says so.** Keep it
that way.

---

## 2. THE TWENTY-FIVE

Branch assignment is fixed here and governs which keywords a card may roll.

### Fog — a fact for fewer of the people present

| Form | Note |
|---|---|
| **Fog-Walker** | The root. Concealment that is not hiding. |
| **Kitsune-Warden** | Not trickery. Being differently real to different observers. |
| **Nue-Kin** | The folklore describes it four incompatible ways; whatever came in did not consult the taxonomy. |
| **Amanojaku-Whisper** | Says the opposite of what is wanted and has been right eleven times. |
| **Ittan-Momen** | Moves in a way the eye reports and the mind declines to accept. Weight recorded as unchanged, which has been queried. |
| **Rokurokubi-Watch** | Awake every night since fusion. Has not reported being tired. |
| **Bakeneko-Familiar** | Accompanies rather than obeys, which is harder to write a report about. |
| **Karakasa-Sentry** | The smallest thing in the folklore. [Sgt Kaoru Mifune](wiki/people/mifune-kaoru.md) asked for the storm and got a paper umbrella. He guards a door, it is genuinely useful, and that is the humiliation. |

### Oni — sacrifice; the fusion burns the host and the host chooses when

| Form | Note |
|---|---|
| **Oni-Drummer** | The root, and the clearest first-hand account of the watching anybody has produced. It is in an unsent letter and no theory cites it. |
| **Gaki-Fed** | Nothing is enough. Recorded as a medical observation. He is embarrassed, which nobody expected. |
| **Nekomata-Claw** | Twice-lived in the folklore's sense, which the programme recorded literally. The file is silent on the attempt. |
| **Inugami-Handler** | Gave something up for this and the record does not say what. |
| **Hitodama-Bearer** | Carries what the folklore says leaves a person at the end. The programme has not asked whose. |
| **Shinigami-Adjacent** | *Adjacent* is the programme's word and was chosen carefully. Arrives slightly before he is needed. |
| **Jorogumo-Weave** | She was a weaver. **The only case where selection matched a life**, it proves nothing, and a theory was built on it anyway. |
| **Yurei-Bound** | Something was left unfinished and it was not hers. |

### Shrine — wards and cycles, and it may be entirely decorative

| Form | Note |
|---|---|
| **Shrine-Keeper** | The root. Dusts a treaty nothing signed, and knows it. |
| **Miko-Sentinel** | Officiates for people who were chosen before she began. |
| **Yokai-Tender** | Assigned to the fused. Not a doctor; there is no medicine for this and the establishment lists him anyway. |
| **Kodama-Warden** | The grove was cleared in 1939 for the works. A clerk connected the two facts and the note was filed. |
| **Zashiki-Warashi** | Attached to a place rather than a unit, which the establishment cannot express. Very young, and nobody will say the number. |
| **Onibi-Carrier** | Carries a light that is not fuel. It does not warm anything; that has been measured. |
| **Kappa-Diver** | Down longer than a man can be. He was a fisherman. He does not like the water any more and has told no one. |
| **Tengu-Scout** | Sees further than the eye should. Every report correct, which is not the same as trusted. |
| **Tanuki-Trickster** | **The one genuinely funny fusion**, and the programme finds it embarrassing. Amatsu has declined to discipline him twice, in writing, without stating why. |

**Fog 8 · Oni 8 · Shrine 9 · total 25.**

---

## 3. Writing rules

- **Name the person before the folklore wherever a page allows it.** The form is
  what happened to them, not what they are.
- **The folklore is not a power set.** Nothing here works because the stories say
  so. It works, and the stories are the only vocabulary anybody had.
- **No entry gets a designation number.** That is Werk Nachtigall's grammar and
  it exists to turn people into products. These are people, and the programme's
  own paperwork keeps saying so even while treating them otherwise.
- **The branch is a mechanical assignment, not a personality.** Two Fog subjects
  have nothing in common except what the fusion does.

---

## 3a. The list is checked, not promised

`tools/hy-roster-check.py` diffs this file against `HY_NOUNS` in
`scripts/app/card_generator.gd` **in both directions** -- a name in the code and
not here is an uncanonised form, a name here and not in the code is a canon
claim nothing implements -- and asserts every form is assigned to exactly one
branch. It refuses to compare if either side comes back empty, so a broken
parser reports itself instead of reporting a clean file.

```
python tools/hy-roster-check.py
```

Proven able to fail before being trusted: dropping one row gives
`in code, NOT canonised: ['Gaki-Fed']`, and putting one form under two branches
gives `DOUBLE-ASSIGNED: Gaki-Fed in Fog and Oni`. Both exit 1. The file was
restored from a byte copy and `cmp`-verified afterwards.

**Where this file and the code disagree, that is a defect in one of them and the
checker is what says so.** Neither is automatically right.

---

## 4. Open, deliberately

- What determines which folklore. **No theory has ever addressed this** — all
  eleven were about *who* is selected, not *what* they get.
- Whether the twenty-five are the only forms, or the only ones so far.
