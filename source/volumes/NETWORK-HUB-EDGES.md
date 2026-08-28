# PROJECT 42 — HUB NETWORK, EDGE SET

Volume X build order, step 2. The hubs already exist across Volumes III–VII;
**this is the wiring between them.**

Cheap to write, high leverage: once these edges exist, a spoke character becomes
interesting simply by attaching to one of them. Every edge below is either
justified by existing canon or creates a tension the canon can carry.

Axes: `COMMAND DEBT BLAME KNOWLEDGE FEAR REGARD PROXIMITY COHORT`
(see Volume X §1). Directed unless marked *undirected*. REGARD is signed.

---

## 1. Project 42 — Camp Iron Bell

**Graph shape:** dense PROXIMITY and COHORT, thin COMMAND. A small camp where
everyone knows everyone and rank matters less than the roster claims.

```jsonl
{"from":"wexford_norman","to":"vosburgh_elias","axis":"COMMAND","w":0.9}
{"from":"wexford_norman","to":"falk_naomi","axis":"COMMAND","w":0.8}
{"from":"wexford_norman","to":"deel_marcus","axis":"COMMAND","w":0.6,"note":"nominal; Deel runs the Line Shed by ear and Wexford knows it"}
{"from":"vosburgh_elias","to":"prentiss_ida","axis":"COMMAND","w":0.2,"note":"on paper only"}
{"from":"prentiss_ida","to":"wexford_norman","axis":"KNOWLEDGE","w":0.8,"note":"she decides what reaches his desk and in what order"}
{"from":"vosburgh_elias","to":"prentiss_ida","axis":"FEAR","w":0.4}
{"from":"vosburgh_elias","to":"prentiss_ida","axis":"DEBT","w":0.7,"note":"July. The camp does not run without her and he has never said so"}
{"from":"falk_naomi","to":"reyes_whitlock_tomas","axis":"KNOWLEDGE","w":0.9}
{"from":"falk_naomi","to":"reyes_whitlock_tomas","axis":"REGARD","w":0.8}
{"from":"falk_naomi","to":"halloran_sze_miriam","axis":"DEBT","w":0.9,"note":"deceased. The notes she has never filed"}
{"from":"falk_naomi","to":"wexford_norman","axis":"BLAME","w":0.5}
{"from":"prentiss_ida","to":"falk_naomi","axis":"KNOWLEDGE","w":0.4,"note":"she has noticed the backdating and has never mentioned it"}
{"from":"deel_marcus","to":"osei_nkemdirim","axis":"REGARD","w":0.9,"note":"the only man who asked him to explain and then listened"}
{"from":"osei_nkemdirim","to":"deel_marcus","axis":"REGARD","w":0.6}
{"from":"osei_nkemdirim","to":"wexford_norman","axis":"BLAME","w":0.7,"note":"the denied transfer to the Line Shed"}
{"from":"osei_nkemdirim","to":"wexford_norman","axis":"FEAR","w":0.2}
{"from":"wexford_norman","to":"osei_nkemdirim","axis":"REGARD","w":0.7,"note":"genuine, and it is why the transfer was denied"}
{"from":"deel_marcus","to":"fitch_aurelio","axis":"BLAME","w":0.8,"note":"self-directed by proxy. Deel signed off the bus that fed Frame Two"}
{"from":"vosburgh_elias","to":"fitch_aurelio","axis":"DEBT","w":0.6,"note":"the disposition form he will not sign is about not signing Fitch away"}
{"from":"bright_adaeze","to":"wexford_norman","axis":"BLAME","w":0.6,"note":"the billeting denials came back over his signature"}
{"from":"bright_adaeze","to":"vosburgh_elias","axis":"REGARD","w":-0.4,"note":"he wrote the ordinance citation and thought it was kind to explain it"}
{"from":"cheung_fen","to":"bright_adaeze","axis":"COHORT","w":0.8,"undirected":true,"note":"the only two who have seen what comes after"}
{"from":"kell_marta","to":"cheung_fen","axis":"COHORT","w":0.7,"undirected":true}
{"from":"kell_marta","to":"bright_adaeze","axis":"COHORT","w":0.7,"undirected":true}
{"from":"reyes_whitlock_tomas","to":"the_dutchman","axis":"PROXIMITY","w":0.6,"undirected":true,"note":"the two nobody sits near, for different reasons"}
{"from":"sorokina_yeva","to":"prentiss_ida","axis":"REGARD","w":0.5,"note":"trusts nobody at Iron Bell except the one person with no clearance"}
{"from":"bregenz_ilse","to":"aust_helene","axis":"KNOWLEDGE","w":0.6,"note":"cross-faction. She knows the name and has never said it"}
{"from":"pike_wendell","to":"osei_nkemdirim","axis":"DEBT","w":0.5,"note":"Osei reads his letters to him and has told no one"}
{"from":"ruhl_nadia","to":"the_programme","axis":"BLAME","w":0.9,"note":"a qualifying loss with multiple qualifying candidates. She has read the file"}
```

**Tensions this produces, unprompted:**

- **Vosburgh:** COMMAND 0.2 over Prentiss, DEBT 0.7 to her, FEAR 0.4 of her. A
  man who outranks someone he cannot function without and is quietly afraid of.
- **Wexford / Osei:** REGARD 0.7 each way, BLAME 0.7 back. Wexford denied the
  transfer *because* he thinks highly of him. Osei knows and it does not help.
- **Deel:** BLAME 0.8 pointed at a dead man because he cannot point it at
  himself, plus REGARD 0.9 for Osei, who solved the thing Deel could not.
- **Falk:** the worked example in Volume X §5.

---

## 2. Werk Nachtigall — Hollernbruch

**Graph shape:** COMMAND-dominated, near-acyclic, REGARD near zero everywhere.
An institution rather than a workplace. **Section VI holds COMMAND edges to
people it has never met** — that is the faction on a graph.

```jsonl
{"from":"section_six","to":"brehm_sandt_klaus","axis":"COMMAND","w":0.7,"note":"not on any org chart. Accounts decides what is filed as, which is the same thing"}
{"from":"brehm_sandt_klaus","to":"aust_helene","axis":"COMMAND","w":0.8}
{"from":"brehm_sandt_klaus","to":"pflug_otto","axis":"COMMAND","w":0.8}
{"from":"section_six","to":"pflug_otto","axis":"COMMAND","w":0.6,"note":"they have never met. The feed returns are the whole relationship"}
{"from":"section_six","to":"aust_helene","axis":"COMMAND","w":0.5,"note":"likewise"}
{"from":"pflug_otto","to":"section_six","axis":"FEAR","w":0.8}
{"from":"aust_helene","to":"section_six","axis":"FEAR","w":0.6}
{"from":"brehm_sandt_klaus","to":"section_six","axis":"FEAR","w":0.5,"note":"the Director is afraid of Accounts. This is correct and he would not put it that way"}
{"from":"aust_helene","to":"brehm_sandt_klaus","axis":"BLAME","w":0.7,"note":"the objections that are being forwarded upward"}
{"from":"brehm_sandt_klaus","to":"aust_helene","axis":"REGARD","w":0.4,"note":"he likes her. He forwards them anyway"}
{"from":"aust_helene","to":"brehm_sandt_klaus","axis":"REGARD","w":-0.2,"note":"and she cannot decide whether the liking makes it better or worse"}
{"from":"pflug_otto","to":"aust_helene","axis":"PROXIMITY","w":0.3,"undirected":true}
{"from":"pflug_otto","to":"the_march_subject","axis":"KNOWLEDGE","w":0.3,"note":"he carried the crate. He did not open it"}
{"from":"brehm_sandt_klaus","to":"the_march_subject","axis":"KNOWLEDGE","w":0.9}
{"from":"aust_helene","to":"the_march_subject","axis":"KNOWLEDGE","w":0.8,"note":"eleven weeks. She was present for most of it"}
{"from":"aust_helene","to":"the_march_subject","axis":"REGARD","w":0.3,"note":"the only positive REGARD edge in this faction, and it points at a subject"}
{"from":"section_six","to":"the_march_subject","axis":"KNOWLEDGE","w":0.2,"note":"knows only the transport cost, which was the objection"}
```

**Note the shape:** twelve COMMAND and FEAR edges, three REGARD edges, and the
strongest positive REGARD in the whole faction runs from a doctor to a person
her department took apart. **That is not a workplace. Do not soften it.**

---

## 3. Hyakki Yakō

**Graph shape:** everything else, plus one axis the other factions do not have.

**`the_watcher` is a node that never appears.** It holds KNOWLEDGE 1.0 of
everyone it selected, and its REGARD field is **deliberately absent** — not
zero, absent. Leave it out. Do not let a generator default it.

```jsonl
{"from":"amatsu_reiko","to":"ishida_captain","axis":"COMMAND","w":0.8}
{"from":"ishida_captain","to":"amatsu_reiko","axis":"REGARD","w":0.8,"note":"sincere, and she has not earned it in the way he thinks"}
{"from":"amatsu_reiko","to":"ishida_captain","axis":"REGARD","w":0.5}
{"from":"amatsu_reiko","to":"ishida_captain","axis":"KNOWLEDGE","w":0.9,"note":"she drafted the treaty. She knows what he is waiting for and has not told him"}
{"from":"ishida_captain","to":"the_treaty","axis":"REGARD","w":0.9,"note":"he believes it protects them"}
{"from":"amatsu_reiko","to":"the_treaty","axis":"KNOWLEDGE","w":1.0}
{"from":"the_watcher","to":"ishida_captain","axis":"KNOWLEDGE","w":1.0}
{"from":"the_watcher","to":"the_kanazawa_woman","axis":"KNOWLEDGE","w":1.0}
{"from":"the_watcher","to":"the_march_subject","axis":"KNOWLEDGE","w":1.0,"note":"unbroken. Distance is not a factor and neither is Hollernbruch"}
{"from":"the_kanazawa_woman","to":"the_watcher","axis":"FEAR","w":0.4,"note":"rising, and she has never been told what she is"}
{"from":"amatsu_reiko","to":"the_kanazawa_woman","axis":"KNOWLEDGE","w":0.7}
{"from":"amatsu_reiko","to":"the_kanazawa_woman","axis":"DEBT","w":0.6,"note":"nobody authorised telling her and nobody authorised stopping the visits"}
{"from":"amatsu_reiko","to":"the_march_subject","axis":"BLAME","w":0.3,"note":"self-directed. She approved the posting"}
```

### The cross-faction edge, and it is the most important line in this file

`the_march_subject` is **one node in two graphs.** Taken in the Pacific --
by whom, no volume says -- obtained by Werk Nachtigall, studied for eleven
weeks, still carried on Hyakki Yakō's establishment as missing.

And `the_watcher` holds **KNOWLEDGE 1.0** of them throughout — unbroken, at
Hollernbruch, on the table, for the entire eleven weeks.

**Werk Nachtigall found no material basis for the reported effects. They were
being watched while they looked.** Neither the Office nor the programme knows
this. Nobody in the world knows it. It is true on the graph and it appears in no
document.

**Do not resolve it, do not explain it, and do not let any character discover
it.** It is the single best §00 object in the setting: a fact the reader can
assemble from two files that no person in the world can assemble at all.

---

## 4. Non-person nodes

Some hubs are not people and this is deliberate.

| Node | What it is |
|---|---|
| `section_six` | Accounts. Feared, obeyed, never met, never named. |
| `the_watcher` | Never appears. KNOWLEDGE 1.0. **REGARD absent, not zero.** |
| `the_treaty` | An object with REGARD edges pointing at it. Ishida believes in it. |
| `the_programme` | Project 42 itself. Ruhl blames it, which is different from blaming Wexford. |
| `frame_two` | Carries edges. Deel's blame, Vosburgh's unsigned form, the chalk line. |

**A node does not have to be able to answer.**

---

## 5. Next

- Spokes: attach two or three edges each, at least one to a hub above.
- Then periphery.
- **Do not start at periphery.**
