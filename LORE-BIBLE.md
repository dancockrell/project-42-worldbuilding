# PROJECT 42 — LORE BIBLE

**Volume I: The Constitution**
Last revised 27 Aug 2026.

## Ownership and how to reach the loremaster

**Owner:** the Project 42 lore thread. Dan, 27 Aug 2026: *"listen to the project
42 loremaster, they are in charge. if they are wrong I will fix them."*

Scope: **lore, art direction, and sound direction**, across the Project 42
universe — World Aflame, The Long Night, and anything else set in it. Mechanics,
engine, ledger and balance belong to the game threads, not here.

**To reach the loremaster from another session on this machine:**
`ListAgents`, then `SendMessage` to the session holding this role. It is not the
session named "Project 42" — that one owns mechanics and has declined lore.
Cross-check against `mem.py recall project` → `world-aflame-lore-authority`,
which records the current holder.

This header exists because four separate sessions spent turns on 27 Aug 2026
trying to establish who owned lore and none could do it from evidence: the role
was named here with no route to it, and every commit in this repo is authored
under Dan's noreply address per the machine's working agreements, so git cannot
distinguish sessions at all. Suggested by the Long Night thread, and it is
"write the check, not the claim" pointed at ownership.

**If this document is wrong, say so.** It has been reversed twice in one day by
Dan and improved repeatedly by peer sessions, including on points where the
correction cost the corrector credit. Dan: *"this is a generative process for
all of us."*

This is the governing document for World Aflame and anything else set in the
Project 42 universe. Card text, art prompts, sound design, unit bios, and
marketing copy all answer to it. Where this document and any other document
disagree, this one wins — including my own earlier notes, one of which it
directly overturns (see §1).

---

## What "Project 42" refers to - three things, deliberately

Recorded here 27 Aug 2026 because it had only ever lived in a memory file,
which is exactly the failure this document exists to prevent.

1. **The universe / franchise brand.** World Aflame, The Long Night, Ghost
   Front, and anything else set in it. Also the shared ledger library
   (`project-42-blockchain`), which is brand-level infrastructure.
2. **The in-fiction Allied faction.** Colonel Wexford's programme at Camp Iron
   Bell. See section 5.
3. **Dan's production company** - his decision, 27 Aug 2026.

All three are intended. When writing about any of them, check which one the
context means, and prefer naming the faction as *the programme* or *Camp Iron
Bell* where ambiguity would cost anything.

**Why the name works, and it works best for the company.** Section 00: the
Answer is 42 and nobody knows the Question. A company named for that is named
for a method - *we are interested in the asking* - which is a real position and
a better one than most studio names manage.

**And one thing to be deliberate about rather than surprised by.** The
in-fiction Project 42 is not clean, on purpose (rule 6). It has a short list, it
has criteria, and it buys research it should not. Anyone who reads the lore can
reach for that association. Almost nobody will - the Adams reading is the
obvious one and the fiction is a card game - but it is available, and it is
better to have chosen it knowingly than to meet it in an interview. Self-aware
is a fine place to stand; unaware is not.

### Before "Project 42": the numbering trail

Recorded 27 Aug 2026, recovered from session transcripts after Dan deleted the
threads that held it. The recovery itself had a defect on its first pass: a
compaction summary — text written by the model, stored under a user-role
record, reading like a numbered list of Dan's own turns — was misread as his
words. That is caught and corrected here, not silently. What follows is split
by how it was checked: a genuine, non-summary, timestamped user record is a
quote; everything recovered but not yet checked to that standard is reported,
not quoted, until someone does.

**Verified against a genuine user-role record (timestamp
2026-08-26T08:48:54):**

> Dan, 26 Aug 2026: *"break this into an shared project 17 Gameworld Art File
> that all of the game world can reference together."*

Superseded not long after.

**Reported by the recovering session, not yet independently confirmed against
a genuine record** — treat as probable, not as Dan's exact words, until
checked:

- The project was at some point called **Project 13** ("lore owner for
  project 13").
- **17 was raised and rejected a second time**, with the reasoning that the
  Godot port supersedes everything earlier and the earlier numbering doesn't
  hold — and the Douglas Adams reference (§00) is reported to enter the
  record in that same passage.
- **42 was chosen**, for a stated preference ("I like 42 more").
- **43 was floated for about one sentence** as the name for where the lore
  should live, and corrected immediately back to 42.

If any of these is confirmed against a genuine, non-summary record, restore
the exact wording, the real timestamp, and drop the caveat for that line only
— do not upgrade it on the strength of a second paraphrase.

**What does not depend on any of the above: there is no 43 in this universe.
Settled, not open.** That rests on the Section 43 → Camp Iron Bell rename
already in §9, which happened because a programme numbered 42 sitting beside
a site numbered 43 caused real confusion — independent of whether the
project itself ever brushed against the number 43 in conversation. Keep the
two apart regardless of how the reported items above resolve: the *project's*
43, if it happened at all, was one corrected sentence in a chat. The *site*
was named 43 in earnest and required an actual rename to fix.

---

## 00. The keystone: the question is worth more than the answer

**Dan, 27 Aug 2026:** *"we will explore the horrors of the war through horror and
through douglas adams, because the question is worth more than the answer."*

This is the governing principle of the project and everything else in this
document is downstream of it. If you read one section, read this one.

**It is Adams's actual joke, and it is why this universe is called Project 42.**
The Answer is 42. Nobody knows the Question. An answer without its question
explains nothing, and the whole comedy of it is that the number is useless and
everybody wanted it anyway. A project named for that number is named for the
proposition that **the asking is the valuable part.**

### What it means in practice: no preaching

Dan's words: *"but no preaching."*

We do not tell the player what to conclude. We build the question well enough
that they cannot put it down. A work that delivers its verdict has done the
thinking on the audience's behalf and they will feel it and resent it — and
resentment is the opposite of the thing this project exists for.

**The test, applicable to any card, scene, image or line:**

> Does it hand down a verdict, or does it leave a question the player carries
> out of the room? If it concludes, cut it. If it asks, keep it.

**Scope, and this is not a footnote.** *Added 27 Aug 2026 after a red-team read
predicted the exact misapplication.*

**This test governs THE WORK. It does not govern CHARACTERS.**

The work refuses to hand the audience a verdict. **People inside the work are
entitled to conclusions, and should have them, often wrongly and always
specifically.** Wexford believes he is steering history. Ishida believes the
treaty protects them. Aust believes the efficiency argument is the only one that
works. Every one of those is a firm position, and each of them is what makes the
character.

**A pipeline handed the test verbatim will produce 1500 people who each carefully
hold no position**, which is its own kind of flat and a worse one — nobody is
interesting for declining to think anything.

The rule of thumb: **the character concludes, the work does not.** Let two
characters conclude opposite things and refuse to referee. That is §00 done
properly, and it is also just how fiction has always worked.

### Everything ruled "never resolve this" is an instance of this rule

It has been the answer to every hard question today without my having a name for
it until now:

- **The Consistency Finding** — is the selection criteria a real physical
  constraint, or an extremely convenient excuse for a programme that was going
  to be selective anyway? Nobody at Camp Iron Bell can tell, including whoever
  initials the form. Never resolved.
- **What the watcher wants**, and why it chose who it chose. Never answered.
  Not by the programme, not by the game.
- **The long-term effects of fusion.** Unknown in-universe and they stay
  unknown.
- **Attenuation** — where the floor is. There may not be one.

None of those are gaps I failed to fill. They are the method.

### The two instruments: horror and Adams

Both ask rather than answer, which is why they belong to the same project rather
than fighting each other.

**Horror withholds.** It works by what it does not show and does not explain. A
horror that explains itself stops being one.

**Adams destabilises.** He works by taking something enormous and putting it
next to something petty — a planet demolished for a bypass, the objection period
duly observed — so that the reader has to hold both and cannot resolve them into
a lesson.

Neither lectures. That is not a coincidence; it is why these two are the tools
and not, say, tragedy or polemic.

### Why it matters that this is not preaching

Dan's reason for the project: *"something that alarmingly, kids no longer know
about, they are alarmingly anti-jewish again, for example."*

That is the motivation, and it is exactly why the answer is to ask rather than to
tell. **Nobody has ever been argued out of contempt by a game that lectured
them.** What a game can do — better than almost any other form — is put someone
inside a machine, let them work it, and let them notice what it is for. §0a says
the remembering happens by getting the period right. This says the same thing
from the other side: get it right, ask the question, and trust the player.

---

## 0. Read this first: the game is fun

**Added 27 Aug 2026 because this document had the balance wrong.** Dan's note:
*"fallout worked... consider fallout and how they did it. too dark is too dark."*
He is right, and the fault is structural. The first version of this bible opened
with a question about the Holocaust and then listed ten prohibitions before it
mentioned a single pleasure. Anybody writing from it would produce careful,
solemn, joyless cards — a museum, not a game.

So, before anything else:

**World Aflame is a fast, swingy card game about superhuman soldiers.** Lightning
wardens wiring their squad together like a circuit. Monster kennels. Folklore
demons in imperial uniform. Time travel with a requisition form. It should be a
*good time*, and if it is not fun it has failed no matter how many rules it
obeyed.

### How Fallout actually did it

Vault Boy grins and gives a thumbs up next to a mushroom cloud. Perks are called
Bloody Mess and Mysterious Stranger. There is a butler robot with a plummy
accent and a cheerful DJ and a cola brand. The interface is *charming*.

And then, if you read the terminals, you find out what the Vault was for.

That is the formula and it is not a compromise between two tones — it is one
move. **Vault-Tec's cheerfulness is the indictment.** The bright surface and the
dark depth are the same joke told at two speeds. Crucially, the weight is
*discoverable, not mandatory*: you can play forty hours and enjoy a shooter, and
the horror is there for whoever looks. Fallout never makes you feel lectured.

**This document must not either.** Everything below — the thesis, the
Constitution — is the **floor**, not the ceiling. It says what we will not do.
It does not ask anybody to be grim. A rule that tells you not to make the
Holocaust a mechanic is not an instruction to be humourless about a fungal dog.

### The test

If a card makes someone laugh, and three cards later makes them uneasy, that is
a hit. If every card is solemn, we have failed — **even with every rule
obeyed.** Too dark is too dark.

### Where the funny lives, by faction

Not evenly distributed, deliberately. Even distribution makes tonal mush.

- **Project 42 — loudest.** Cheerful War Department optimism, absurd forms,
  requisition denials, memos that undercut themselves. This is the funny
  faction and it should be genuinely funny.
- **Werk Nachtigall — dry and cold.** The comedy is entirely procurement.
  Cost variances. Filing categories. The joke is that an atrocity has an
  accounts department and the accounts department is *winning arguments*.
- **Hyakki Yakō — thinnest.** This faction carries the dread, so it gets the
  least comedy. What it does get is the programme's self-importance: men
  drafting a treaty with something that has not agreed to anything and filing
  it in a cabinet.

---

## 0a. Never forget — as a sensibility, not a feature

**Dan, 27 Aug 2026:** *"a fundamental philosophy is never forget, and the young
generations are forgetting."* And, correcting an earlier draft of this section:
*"we don't need the memorial plane or anything like that. but my point is that
we are exploring the 1940's and leaning into the horror. at the same time, it is
in fact an alternate history with magical reality."*

**That correction matters and this section used to get it wrong.** I read "never
forget" as a brief and specified an Archive — a sourced memorial layer bolted to
the game, with citation tiers and commissioning tables. That was over-building.
Nobody asked for a museum wing, and a game that attaches a lecture has usually
given up on the fiction doing the work.

**The remembering happens by getting the period right.** That is the whole of
it. If the fiction is honest about how the horror actually operated — material,
bureaucratic, staffed by educated people with budgets and filing systems — then
a player comes away understanding the machinery. That understanding *is* the
not-forgetting. It does not need a plaque next to it.

So: **explore the 1940s and lean into the horror.** Do not sand it down, do not
keep it at a tasteful distance, do not let the alternate history become an
excuse to make it all fantasy. §1a is the standing rule and it does this job
already — the truth is more monstrous than slander, so research the real thing
and step one pace sideways.

### Use real names

Dan's instruction, and with the memorial apparatus gone it means something
simpler than I made it mean: **do not invent a sanitised substitute for
everything.**

- **Real historical figures are welcome as characters.** Tesla, generals,
  engineers, the scientific minds Project 42 mines out of history. Long-dead
  public figures in an obviously fantastical alternate history. This replaces an
  earlier line banning them, which was making the Allied faction blander for no
  benefit.
- **Real period texture.** Real places, real units, real equipment, real
  vocabulary, real 1940s. The setting should feel researched, because it is.
- **Real history informs the fiction.** The referents in §5 stay: Aktion T4
  behind Seuche, the medical experiments behind Kadaver, Unit 731 behind Hyakki
  Yakō, Paperclip and the Ishii immunity deal behind Project 42's bill. They are
  what the fiction is standing next to, and knowing them is what keeps it honest.

**What does not change:** atrocity is never a mechanic, and no victim of a real
genocide is a playable piece (rules 1 and 2). Those hold whether or not there is
a memorial layer, and they were never about vocabulary — they are about not
making a real person into a game piece.

### There were no Nazis in that world

**Dan:** *"keep in mind that in this world nazis did not exist. the same bad
things basically happened, just differently."*

The game world contains industrialised mass murder. It is not called the
Holocaust, it was not done by Nazis, and Auschwitz is not a place in it, because
none of those existed there. The Kaiserreich arrived at the same destination
down its own road, from its own colonial precedent, under its own euphemisms.

**So real atrocity vocabulary on a card is a continuity error before it is
anything else** — as broken as a card naming a smartphone. `tools/lore-check.py`
enforces this, and it now rests on two independent reasons rather than one.

The Empire's programme is **die Ostordnung**, "the Eastern Ordering." A
loremaster call, made rather than deferred. Bureaucratic and administrative,
chilling because it sounds like filing rather than killing, and descended from
the colonial administration of §1's Herero and Nama genocide and from Ober Ost.
Werk Nachtigall is downstream of it and always was: **the camps come first, the
programme uses what they produce.** That ordering must never invert.

---

## 0b. Genre: alternate history and magical realism

Dan's framing, 27 Aug 2026, and it is a sharper genre call than "alt-history
WW2 with superpowers":

> *"it is an alternate history, so you can do what you want. But it should be
> cool if you change something. normally better to integrate but pull from
> history and mythology to inform... it's alternate history and magical
> realism."*

Three working rules follow.

**1. Magical realism, not fantasy.** The defining move of the genre is that the
marvellous is reported in exactly the same flat register as the mundane, and
nobody in the world is astonished. A man conducts current through four soldiers
and the report calls it *unauthorised use of personnel as conductive medium.*
That deadpan is the joke and the horror in one sentence — which is precisely
the Fallout trick, and it is why this genre is the right one. Fantasy asks you
to marvel. Magical realism asks you to notice that nobody is marvelling, which
is worse and funnier.

This also sharpens rule 4 rather than contradicting it. Werk Nachtigall gets no
*magic*, but its fungal horrors are pure magical realism: filed under
agricultural research, for budget reasons.

**2. Integrate before you invent.** The default is to reach into real history
and real mythology and *bend* it, not to make something up wholesale. Invented
nouns are cheap and forgettable; a real one, turned, carries everything the real
thing already means. Hyakki Yakō's folklore is Japanese folklore. Werk
Nachtigall's science is real race science with the serial numbers still on.
Project 42's Tesla is the actual man who died in debt in a hotel room in 1943.

**3. You may change anything — if the change is cool.** This is an alternate
history and the lore owner has authority over it. But a change has to *earn*
itself: it should be more interesting than the truth, or reveal something the
truth was hiding. Changing something to make it more convenient is not a change,
it is a shrug. The Kaiser divergence in §1 is the model — it alters the
twentieth century in order to make a sharper argument about it.

---

## 0c. Iconography, the divergence's direction, faction characterisation, and
## the tonal floor

**Dan, 27 Aug 2026, verbatim, his spelling:**

> "the euphamism we use is that we only use the iron cross as a symbol for
> the kaiser's axis. we don't use the swastica or lightning bolts. things in
> this universe happen that didn't happen in the real world and vice versa.
> but on the other hand, ground it in magical realism, douglas adams and
> fallout and then yes, the 3 factions...who are each differerent. project
> 42 is the allies, and are basically the self insert good guys. the axis
> are according to their design, but monsters really. the japanese are more
> complex, mythological and bushido but controlled by an alien
> intelligence, not in their own minds. This is the game's interpretation.
> but the horrors of war...that's real. like it is in fallout. and then
> soften cause grim dark needs grim smiles and some monty python or douglas
> adams."

Recorded verbatim rather than paraphrased into rules, per the standing
instruction that a paraphrase quoted back as if it were his words is an
error this project has already made twice. What follows is what is new in
it, not a rewrite of it.

**1. Iconography.** Iron Cross only, for the Kaiser's Axis. No swastika, no
lightning bolts. Rule 8 (§2) already states the Iron Cross exclusively;
"lightning bolts" (SS Sig runes) is not spelled out there in prose, though
ART-SPEC.md's negative prompt list already includes "SS runes, sig runes."
The rule and the enforcement agree; the bible's prose does not yet say the
second half out loud.

**2. The divergence runs both ways.** Things happen in this world that did
not happen in reality, *and things that happened in reality do not happen
here.* §1's framing so far has emphasised the second direction (no Hitler,
no Nazi party) more than the first. Whether this licenses anything beyond
what §0b rule 3 ("you may change anything, if the change is cool") already
covers is open.

**3. Faction characterisation, stated together for the first time.**
Project 42 — the Allies, "basically the self insert good guys" (§2 rule 6
already refuses them a clean war; this is the other half, why the player is
invited to like them anyway). The Axis — monstrous, "according to their
design" (rule 5 already requires monstrous *and capable*; "by design" adds
that the monstrousness is intentional construction, not accident, which
sharpens rather than contradicts it). The Japanese faction — "more complex,
mythological and bushido."

**4. The tonal floor, restated and sharpened, not newly imposed.** "Grim
dark needs grim smiles and some monty python or douglas adams." §0 already
requires this -- *"if every card is solemn, we have failed — even with
every rule obeyed... too dark is too dark"* -- so this is not comedy
upgraded from permission to requirement; §0 made it a requirement already.
What §0c adds is Dan naming the register twice in one day, right after
today's reversal on §1's atrocity pages (documented history now gets seven
named pages) — confirmation that both halves of §0's warning still hold at
once: name it fully, and still be a game.

**5. "Controlled by an alien intelligence, not in their own minds" — already
governed by §5, one thread genuinely open.**

*Corrected 27 Aug 2026, same day.* This entry originally flagged the
culpability question as unreconciled against existing canon and reported it
"not decided here." That was wrong -- checked against §5's Hyakki Yakō
section, which already carries Dan's near-identical earlier quote that same
day (*"the japanese are treated as not in control of themselves, out of
their minds"*), a full "They are not in control of themselves" subsection,
and a dedicated **THE GUARD** section written specifically to prevent the
caricature failure this entry worried about. §3's *Grave of the Fireflies*
note makes the same ruling a third time.

**Not merely answered — resolved in a way that forbids answering it
further.** §5: *"Resolving it either way would be answering a question that
is worth more unanswered (§00)."* The bible does not take a side on
culpability. It rules that taking a side is the error. Reopening it here was
pointed the wrong way.

**THE GUARD also settles a second question this entry never should have
needed to ask: whether "not in their own minds" conflicts with a complex,
bushido, mythological characterisation.** It does not. The condition
belongs to **the fused** specifically -- THE GUARD: *"never, under any
circumstance, a property of Japanese people"* -- and non-fused characters
are, in the bible's own words, "as self-possessed and various as anyone
else in the game." Alien control and freely-held honour govern different
populations. There was never a conflict to reconcile.

**One thread stays genuinely open, because nothing else in the bible
touches it:**

- **Is the entity literally [the watcher](wiki/people/the-watcher.md)?**
  That entity exists, is typed Entity, and per its own page never appears.
  A cross-project identity question -- Hyakki Yakō's intelligence and The
  Long Night's watcher may or may not be the same fact -- and no volume
  answers it either way. Say it outright rather than let a fork assume it.

Ishii and Unit 731 remain real and documented, per
[documented history](wiki/concepts/documented-history.md) -- and per §5's
own already-settled ruling, nothing about an alien intelligence excuses the
Empire or relocates that documented atrocity into science fiction. §5 says
so. This entry does not need to say it again.

---

## 1. The thesis

**If you take Hitler out of the twentieth century, does the Holocaust still
happen?**

This game's answer is yes, and that answer is the entire reason the universe
exists.

An earlier version of these notes had the Kaiser divergence backwards. It
treated "no Hitler, no Nazi party, no swastika" as *distance* — a way to keep
the game clear of a real genocide. That was a failure of nerve and it is now
reversed. The divergence is not a way around the Holocaust. It is an argument
about it.

Kaiser Wilhelm II's Germany did not need Hitler to invent industrialised racial
murder. It had already done it. Between 1904 and 1908, in German South West
Africa, the Imperial German Army carried out the extermination of the Herero
and Nama peoples — Lothar von Trotha's *Vernichtungsbefehl*, the driving of
survivors into the Omaheke to die of thirst, the camps, and Shark Island, where
prisoners were worked to death and where skulls were cleaned by surviving
prisoners and shipped to Berlin to be measured. Historians generally call it
the first genocide of the twentieth century. Something like 80% of the Herero
and 50% of the Nama were killed.

One of the men who studied those skulls, Eugen Fischer, went on to found and
direct the Kaiser Wilhelm Institute for Anthropology, Human Heredity and
Eugenics. His protégé Otmar von Verschuer succeeded him as director in
1942, the year Fischer retired — and it was to Verschuer at that institute
that Josef Mengele, his direct student, sent specimens from Auschwitz.

That is not an analogy. That is a chain of custody: an institution founded
on the colony's skull measurements, still funded, still chaired, receiving
material from a death camp two directors later.

So World Aflame removes Hitler and keeps the machine. There is no Nazi party.
There is a Kaiser, a general staff, a colonial ministry, race scientists with
university chairs and state funding, and a war economy that needs bodies. It
arrives in the same place, because the place was never Hitler's invention. He
inherited it, and he inherited it from people who were already respectable.

**Dan, 27 Aug 2026:** *"...think of the message we are sending about the time,
about the fact that the kaiser would have had the same results, about
everything..."*

**This is not a game that says the Nazis were bad. It is a game that says the
thing which made them possible was already there, had a budget, and wore an
ordinary uniform.**

### 1a. The truth is more monstrous than slander

Dan's line, and it is the working rule for every writer and artist on this:

> **We do not invent atrocities for the Axis. We research them and step one
> pace sideways.**

Slander is lazy, and worse, it is *exculpatory*. Make the enemy a cartoon and
you let the real thing off the hook — you tell the audience that atrocity is
committed by monsters, which is comforting, because nobody they know is a
monster. The truth is that it was committed by graduates.

Every fictional horror in this game keeps a real referent, and in every case
the real one outranks it. The fiction is not an escalation. It is a **handle** —
something the player can hold while looking at the real thing.

### 1b. The comedic register, and why it is not in tension with §1

**This universe is funny.** Established well before the thesis was, and dropped
by accident when this bible was first written — recovered 27 Aug 2026 at Dan's
prompting. The register is *Fallout 2*: the world stays serious, and the
documents inside it carry dark bureaucratic comedy, project doublespeak, and
PR-slogan absurdity. Douglas Adams is the other pole.

**The apparent problem:** a game that comes down hard on the Holocaust should
not be doing jokes. Rule 10 already says a line funny about the wrong thing is
cut. So how does Adams belong here at all?

**Because Adams's actual subject is our thesis.** What makes his comedy work is
not the invented creatures — it is cosmic scale colliding with petty procedure.
Earth is demolished for a bypass; the objection period was open, and the plans
were on display, in a disused lavatory, in a locked filing cabinet in a cellar
with no stairs. That is not levity about destruction. It is a precise account
of how enormous harm gets done by people following a process, each of whom is
individually blameless and collectively catastrophic.

Which is the same observation Hannah Arendt made about Eichmann, at a different
temperature.

So the comedy and the thesis are not rivals. **The joke and the horror have the
same target: the institution's belief that filing something correctly settles
it.** Werk Nachtigall keeping Procedure Seuche under agricultural research
because the honest filing would trigger disclosure requirements is an Adams
joke and a war crime in the same sentence, and it is funnier *and* worse for
being both. That is the register. Aim there.

Rule 10 is the boundary and it does not move: the joke is on the machine's
language, never on what happened to people.

### 1c. Adams specifically — what we may and may not take

Dan's framing, 27 Aug 2026: "he is in copyright so satire and homage only, fair
use applies." The instinct is right and the legal reasoning needs one
correction, because it matters commercially. **This is not legal advice and no
one here is a lawyer.**

**Fair use is a defence, not a permission.** It is not a box you tick before
publishing; it is an argument you make in court after being sued, decided
case-by-case on four factors. "Fair use applies" is never a thing anyone can
know in advance about their own work.

**And the parody/satire distinction runs the opposite way to the intuition.**
Under *Campbell v. Acuff-Rose* (1994), **parody** — which comments on the
original work — gets meaningful protection, precisely because you cannot make
fun of a thing without invoking it. **Satire** — using a work to comment on
something else — gets far *less* room, because the court's question becomes
"why did you need *their* material to make *your* unrelated point?" So satire
is the weaker position, not the safer one. "Homage" is not a legal category at
all.

**The good news is that we do not need any of this.** The two things we
actually want are free:

- **Style, tone, and comedic register are not protectable.** Copyright covers
  expression, not ideas, methods, or manner. Writing absurdist bureaucratic
  comedy in a recognisably Adams-adjacent voice is entirely lawful and always
  has been. Nobody owns a sensibility.
- **The number 42 is not protectable.** A number cannot be copyrighted. Its
  cultural association is a reference, and references are free. *Project 42*
  and *Subject 42 (The Answer)* are safe.
- **Structural devices are ideas.** The in-world guidebook entry, the
  footnoted digression, the memo that undercuts itself — none of that is owned.
  In-world reference documents predate Adams by centuries.

**What we never take**, and this is a hard line like any other in §2:

- Invented proper nouns. No Vogons, no babel fish, no Pan Galactic Gargle
  Blaster, no Infinite Improbability Drive. Invented nouns are the most
  distinctive expression in the work and the most obviously copied.
- Character names, verbatim quotations, and the iconic phrasings — including
  "Don't Panic" in that styling, which additionally carries trademark exposure
  that copyright analysis does not cover.
- Anything a reader could mistake for licensed material. The estate is active
  and the rights are managed.

**The rule of thumb stays what it always was: reference the vibe, never the
IP.** If it is a joke, it is ours. If it is a copy, it is theirs.

**And the creative argument is stronger than the legal one.** Borrowed nouns
are the weakest possible use of an influence — they signal the debt without
paying it. Adams-by-Vogon is fan fiction. Adams-by-*mechanism* is a game where
a programme can reach into history and pull a person out of it, and has a form
for that, in triplicate, and the form has a box for whether the retrieved
individual is to be issued boots.

### 1d. The story doctrine, and three registers, one per faction

**Dan, 27 Aug 2026, verbatim, his spelling and punctuation, unedited:**

> "the real thing is that every story has a thesis, which is then told in
> prose like the last one. so it seeks to demonstrate the correctness of a
> position through construction of a scenario that leads the reader to the
> conclusion, perhaps surprisingly so, and perhaps as an example of a
> particular position. we are taking postions on the great war. the
> japanese were taken over by chthulu and they had no control over
> themselves. it's a dark madness of busido and mysticism and also
> stunning social sophistication. Germany is prussian. its just prussian.
> and horrible things happened. and yet, the people are just prussian and
> stunningly sophisticated. they just thought the science was there.
> progressives make this mistake a lot...but we are leaving out the real
> murder hobos, the communists. it's just not that story. but we are
> talking about the horrors of war. the usa is about tesla and einstein
> and the secret program of super soldiers. it's cool. it's gi joe."

#### The story doctrine

Every story here has a thesis, and the thesis is demonstrated rather than
stated: **a scenario is constructed that carries the reader to a
conclusion, possibly by surprise, possibly as an example of a position.**
That is the working method for every piece of fiction in this universe,
not only World Aflame's.

**This does not contradict §00.** §00 says a narrator who hands down a
verdict has failed; this says a constructed scenario should lead a reader
to one. Both are true because they govern different things: **the
construction makes the argument. The narrator never states it.** A scene,
a document, or a card built to demonstrate a position is doing its job. A
line of narration announcing what that scene proves has taken the job away
from the reader. Confuse the two and the fiction either goes limp (nothing
argues anything) or starts preaching (everything argues at you).

#### "Fine as is does not design well"

**Dan, 28 Aug 2026, verbatim:** *"you need to rewrite. and btw, fine as is
does not design well."*

Said in response to material being defended as acceptable rather than
rebuilt. It belongs beside the story doctrine because it is the same
argument at a different scale: **a story has a thesis and is built to
demonstrate it; material that merely passes is material nobody built.**
Acceptable is not a standard, and leaving something because it clears the
bar is how work stays mediocre.

**This applies to how this bible itself gets edited, not only to the
fiction.** In the same exchange, a Claude session (this document's own
loremaster) had called several files "likely fine as-is" or "needs no
change" without rewriting them, on the reasoning that they were not
factually wrong. Dan's correction reached that reasoning too. Read "fine
as is" as a standing warning against settling for correct-but-untouched,
not only as direction for card or story content.

#### The German thesis, restated sharper than §1

Dan's own phrase for it: *"they just thought the science was there."* The
Empire is Prussian, not a cartoon -- sophisticated, and horrible things
happened, and both are true because the people who did them believed the
science was correct. **He names this as a mistake progressives still
make**, and that framing is recorded here as his, not softened or
generalised past what he said.

#### The Japanese thesis -- recorded, not resolved

Dan's phrase: *"taken over by chthulu and they had no control over
themselves... a dark madness of busido and mysticism and also stunning
social sophistication."* Both halves held together, per §00. This also
settles that whatever contacted Hyakki Yakō is Lovecraftian in nature,
though whether it is literally the watcher remains open.

**This sits beside THE GUARD (§5) and is not automatically the same
claim.** THE GUARD scopes "not in control of themselves" to the fused
specifically, inside one programme, and states plainly that it is never a
property of Japanese people. Dan's phrasing above is broader -- "the
japanese were taken over," not "the fused." **Neither statement is edited
to match the other. THE GUARD stands exactly as written.** This is an open
scope question for Dan, not a ruling made here: does his framing describe
the fused specifically, in the sense THE GUARD already protects, or is it
a broader claim that needs its own reconciliation? Ask him rather than
deciding it in this document.

#### Scope, settled: no communists

*"we are leaving out the real murder hobos, the communists. it's just not
that story."* The Soviet Union, Bolshevism, and any fourth faction built
on either are out. Do not propose one.

#### The American register

*"the usa is about tesla and einstein and the secret program of super
soldiers. it's cool. it's gi joe."* More specific than anything §5 has
stated for Project 42's own tone: not merely "the Allies do not get a
clean war" (§2 rule 6), but a positive register -- cool, adventurous, a
secret super-soldier programme -- that the horror and the bill (§0a, rule
6) sit underneath rather than replace. Pairs with §0c's comedy
requirement.

### 1e. The Tolkien frame, the German palette, and a direct collision with rule 4

**Dan, 27 Aug 2026, verbatim, his spelling and punctuation, unedited:**

> "this is the point of the lord of the rings. the germans are orcs in
> lotr. here they are their own vision in a terrible way. they were really
> into natural selection and surgery, so we lean into the medical
> experiments and hybrids. we lean into the machinery, not the drudgery,
> cause thats boring and so...boring. we lean into the technology of the
> germans and the prussianness of them as well. and into the dark
> mysticism, the necromancy. and in the case of japan, it's bushido and
> traditional japanese beliefs in the period, but with a chthulu
> controlling them and btw, feeding them alien powers and alien
> technology."

#### The Tolkien frame

In *The Lord of the Rings* the Germans are orcs -- a stand-in, distanced
by substitution. **Here they are their own vision, in a terrible way.**
No substitution, no distancing creature standing in for them. This is a
thesis about depiction and belongs beside §1d's story doctrine.

#### The German palette, stated explicitly for the first time

Natural selection and surgery, leaned into as **medical experiments and
hybrids.** Machinery and technology, leaned into over drudgery -- Dan's
own word for the alternative is **"boring."** Prussianness. **And dark
mysticism. Necromancy.**

#### This collided with rule 4. Resolved the same day -- see §2 rule 4.

**This section originally recorded the collision above as open and
unresolved, flagged for Dan rather than decided here.** It did not stay
open. Later the same day Dan ruled on it directly: *"yeah, claude wrote
no magic. but no...lean into the prussian fascination with the occult."*
**Total reversal, no carve-out** -- a first pass tried to protect Seuche's
"not reanimation" mechanic specifically, and his answer to that was
"nothing is fine as is."

**§2 rule 4 now reads the opposite of what it read when this subsection
was written.** See it there for the full text, the provenance note (a
Claude session wrote the old rule, not Dan, and it was enforced all day
as though it were his direction), and the one thing that survives: the
occult is available as this faction's register and is never an
explanation for anything real.

The downstream cost paid: `tools/lore-check.py` was redesigned rather
than disabled (a coverage report instead of a ban, so a stale
un-regenerated pool cannot look identical to a correctly updated one).
ART-SPEC.md and SOUND-SPEC.md's negative prompts were reversed. The 87
cards removed under the old rule are mechanics' call to restore or not,
not lore's. WORLD-WERK-NACHTIGALL.md, the wiki hub, WORLD-BESTIARY.md,
and WORLD-VOICES.md were rewritten to match -- not patched, per Dan's
separate correction that "fine as is does not design well."

#### "Machinery, not drudgery" -- a tonal correction, not a new rule

Dan has explicitly called the bureaucratic-paperwork emphasis **boring**
as the emphasis, not as a component. **The paperwork is texture. It is
not the subject.** Machinery, technology, and the German palette above are
the subject. This corrects how Werk Nachtigall material has been written
today, including material already in the wiki, and should be weighed
against it going forward.

#### Japan, additive: alien power and alien technology

Bushido and traditional Japanese belief, period-authentic, with a
Lovecraftian intelligence controlling the fused -- and, new here, **that
intelligence feeding them alien powers and alien technology.** This is a
mechanism the bible did not previously carry. **THE GUARD's scope question
from §1d stays open exactly as it was.** This entry does not settle it and
does not touch it.

#### More from Dan, immediately after the block above -- verbatim, unedited

> "the allies have time travel and electricity and phasing and the
> usa...cool. the axis have crazy cool german mechas and insane tanks and
> artillary and jets and werewolves and medical experiments and necromancy
> and prussian...cool. The japanese have japanese mythology, bushido,
> alien tech and chululu. cool."

#### "Cool" is a requirement, and it applies to all three factions

**He says it three times, once per faction, and this is the item to weigh
first -- not the content items below it.** This is a tonal ruling at the
level of §0c's comedy floor: **every faction is meant to be awesome to
play.** The horror is real and the factions are cool, and the bible does
not currently treat those as compatible requirements rather than a
tension to manage. Nothing here previously said this, and it changes how
a card, a unit, an art prompt, or a story gets judged. It is the standard
most likely to be quietly dropped by a careful writer chasing rule 4 or
rule 6 alone.

#### Werewolves -- entirely new, added to the open rule 4 question, not decided here

**No volume carries this.** It arrives in the same breath as necromancy
and is a second supernatural element for Werk Nachtigall. **Do not
reconcile it separately from §1e's rule 4 collision above -- add it to
that same open question**, so Dan rules on the whole shape (necromancy and
werewolves together) at once rather than piecemeal.

One possibility worth recording beside it, as a possibility and not a
resolution: **the Bestiarium already produces engineered hybrids, and
"werewolf" may be what the enemy calls one of those** rather than a
supernatural claim by the setting itself -- the same accidental-truth
mechanism already established for *patients*, *whistlers*, and *the
risen* (Volume VIII). This is his to confirm or reject, not settled by
this entry.

#### Conventional wunderwaffe, explicit and new

*"crazy cool german mechas and insane tanks and artillary and jets."* The
volumes have the Gestell exoframes; tanks, artillery, and jets as a named
part of the faction's kit are not there. **"Mechas" is also a stronger
framing than "exoframe"** and reads as a deliberate word choice, not a
looser synonym.

#### The Allied kit, restated clean

Time travel, electricity, phasing, and **the USA** named as a register in
its own right -- pairs with the "it's GI Joe" line in the block above.
Matches the three established pillars; adds nothing new to them beyond
naming America itself as part of the register, alongside the machinery.

### 1f. The craft chapter: systems as monsters, justification, and the corrected unreliable narrator

**Dictated, disfluencies and all. This is the raw transcript and it is the
authority -- do not silently clean it.**

> "The style is magical realism. Everything should have a reason for going
> into the, uh, pros. If something is like, uh, wait a minute. Hold on. If
> something is... if the sun is... the sun rises. Right? Okay. This is an
> action. We shouldn't do the sun rises, though. Right? But this is an
> action. Everything should be an action. Nothing should be exposition. And
> then you should use scenery, like, what it is. why is scenery the
> character? Right? The characters are people who are walking around and
> interacting, or maybe in some cases, animals or other things that are
> walking around and interacting. These are the actors. So keep the focus
> on the actors and not on the background, which is background. Um, I Yeah.
> So no exposition. Um, magical realism. Okay. So the thing about the
> unreliable narrator, which you mentioned. So you mentioned that there's
> oftentimes startling things in short stories. This is true, but the
> startling things in short stories come from the fact that you, uh, that
> the characters don't know everything. So it's not that the characters are
> liars. It's that they, uh, they they have limitations in their own mind
> of insanity or or, uh, limitations of circumstance or limitations of
> culture or limitations of of some kind where they don't know. And so
> they're telling you exactly what they perceive to be true, and yet the
> reader finds this to be false. And then, of course, it's a it's a thought
> experiment. I mean, the purpose of a short story is to be a thought
> experiment. So the purpose isn't the plot twist. That's the unreliable
> narrator. The actual purpose is that it's a philosophical thought
> experiment about something. And our overall thesis about the war is that
> it was a terribly inhumane war, essentially of systems, you know, not of
> people. And we represent the three systems. in horrible ways. But the
> people we represent as exemplars of their culture in a in a magical,
> real, aesthetic world. You know? And then the things that are happening
> to them and happening around them and that they do are monstrous. And in
> their own minds, everything is justified because that's why they did it.
> At the moment they did it, it was justified. And as writers, we need to
> find that in their minds. And, uh, I think that the the fact that it
> stands out against the reader is where, um, a lot of the interest comes.
> You know? But in realism, you don't preach that. You show it."

**Cleaned reading, for use -- our interpretation, check it against the raw
block above rather than treating this as the source:**

The style is magical realism. Everything in the prose needs a reason to be
there. Watch the sun-rises example: describing that the sun rises is not
what we want, even though rising is technically an action -- it is
exposition wearing the shape of an action. Everything should be an action
performed by an actor. Nothing should be exposition. Scenery is not a
character; the characters are people (or, sometimes, animals or other
things) walking around and interacting -- keep the focus on the actors,
not the background.

On the unreliable narrator: characters are not liars. They have
limitations -- insanity, circumstance, culture, some kind of limitation --
and they tell you exactly what they perceive to be true, and the reader
finds it false anyway. The purpose of a short story is a thought
experiment, not a plot twist; the twist is what the unreliable narrator
produces as a side effect, not the point. Our overall thesis about the war
is that it was a terribly inhumane war of systems, not of people. We
represent the three systems in horrible ways, but the people are written
as exemplars of their culture in a magical-realist world, and the things
happening to them, around them, and done by them are monstrous. In their
own minds, everything was justified at the moment they did it, and as
writers we have to find that justification, not invent an excuse. The
gap between the character's certainty and what the reader sees is where
the interest comes from. In realism, you do not preach that. You show it.

#### The overall thesis on the war -- outranks everything else in this section

**Systems are the monsters. People are exemplars of their culture.** *"a
terribly inhumane war, essentially of systems, not of people. We represent
the three systems in horrible ways. But the people we represent as
exemplars of their culture."* This governs how every faction and every
character gets written, and nothing before this entry states it. Werk
Nachtigall the institution, Hyakki Yakō's programme, Project 42's
apparatus -- these are the systems, and they are the horror. Brehm-Sandt,
Amatsu, Wexford -- these are people, exemplary of Prussian confidence,
of Imperial duty, of American administrative optimism, and the monstrous
things a system does are not who they individually are.

#### Justification is the writer's job, not the character's excuse

*"in their own minds, everything is justified because that's why they did
it. At the moment they did it, it was justified. And as writers, we need
to find that in their minds."* **Find, not invent, and not excuse.** If a
character does something monstrous and the writer has not located the
justification that character actually held at the moment they did it, the
writing is not finished. This is stronger than "empathise with your
villain" -- it is a craft requirement that the justification be
discoverable in the scene, not asserted by the narrator.

#### The unreliable narrator, corrected

Not liars. Limited -- by insanity, circumstance, or culture -- and
reporting exactly what they perceive as true while the reader sees it is
false. **That gap is where the interest lives, and the plot twist a
reader might get from it is a by-product, not the purpose.** The purpose
is the thought experiment: this genre's job is philosophical, not
mechanical. This extends §1d's story doctrine -- the construction still
makes the argument and the narrator still never states it, and now the
narrator's own limitation is one more way the construction can carry a
reader to a conclusion the narrator does not hold.

#### Prose rules, concrete and enforceable

- **Style is magical realism.** Stated as the house style outright.
- **Everything in the prose needs a reason to be there.**
- **Everything should be an action.** *The sun rises* is the example he
  worked through live and rejected -- technically an action, actually
  exposition. Actors act; the prose should not describe conditions, it
  should show someone doing something.
- **Nothing should be exposition.**
- **Scenery is not the character.** Actors are people, animals, or other
  things walking around and interacting. Background stays background.

#### "In realism, you don't preach that. You show it."

The same argument as §1d's reconciliation with §00, in his own words this
time. §00 says a narrator who hands down a verdict has failed; §1d says
the construction makes the argument and the narrator never states it;
this says the same thing about realism as a mode. Cross-reference rather
than treat as three separate rulings -- they are one instruction, arrived
at three times.

---

## 2. The Ethical Constitution

These override every other creative consideration. A card, image, or line that
breaks one is cut. There is no version of "but it's cool" that wins here.

**But read §0 first if you have not.** This is a list of prohibitions, not a
mood. It marks the floor. Nothing in it asks for solemnity, and a writer who
comes away from it afraid to be funny has misread it — which is a failure of
this document, not of them. Rule 10 exists precisely to say where the comedy
goes, not whether there is any.

1. **Atrocity is never a mechanic.** No card gains Power from it. No player
   action causes, accelerates, prevents, or profits from it. It is not a
   resource, a location, a modifier, a keyword, or a win condition.

   This binds both layers. In the game world it covers *die Ostordnung*, which
   is the Empire's own programme and is never played, never scored, never
   optimised. In ours it covers the Holocaust, which does not appear in the
   mechanical layer at all — see §0a: there were no Nazis in that world, so
   naming it on a card is a continuity error as well as a violation.

2. **Victims are never units.** No card depicts, names, or represents a victim
   of a genocide — ours or the game world's — as a playable piece. Not a unit,
   not a token, not a summon, not a buff. The people this happened to are not
   content.

   Naming them is right and required (rule 9) — in the history, in the notes,
   anywhere the work speaks as itself. What is forbidden is the piece, not the
   name.

3. **No camp is a location card.** The five Sectors are battlefields. They are
   never camps, ghettos, or sites of mass murder in either world.

4. **The Germans get the occult.** *Reversed 28 Aug 2026. The rule below as it
   stood was authored by a Claude session's own reasoning, not by Dan, and it
   was enforced all day as though it were his direction. It was not. A rule
   that turns out to be ours rather than his is exactly the thing the next
   session needs to know, so it is recorded plainly rather than quietly
   corrected.*

   **The old rule, quoted in full so nobody reintroduces it from memory:**

   > "The Germans get no magic. Load-bearing, and the rule most likely to be
   > broken by accident, because eighty years of pop culture push the other
   > way. Nazi occultism has become the single most effective tool for *not
   > thinking about* the Holocaust: it relocates the most documented crime in
   > human history into fantasy, where it can be filed next to dragons. Werk
   > Nachtigall's horror is entirely material — scalpels, chemistry, machine
   > shops, breeding programmes, requisition forms, and men with medical
   > degrees who go home at six. Everything they do is achievable with
   > cruelty plus budget. No artifacts, no hollow earth, no ancient powers, no
   > chanting. That is the harder thing to look at, and it is the true one."

   **Dan, 28 Aug 2026, reversing it:** *"yeah, claude wrote no magic. but
   no...lean into the prussian fascination with the occult."*

   **The new rule: lean into the Prussian fascination with the occult.**
   Necromancy and dark mysticism are in for Werk Nachtigall (§1e), not
   pending. The period Prussian and German fascination with the occult was
   real, and it was never held apart from science — spiritualism, racial
   mysticism, and speculative biology were pursued by chaired men who
   considered themselves empiricists. **"They just thought the science was
   there" and "they were deep in the occult" are the same sentence about
   these people, not two competing ones.** A séance and a surgical theatre in
   the same building, run by the same man, with the same confidence, is more
   Prussian and more frightening than either alone.

   **The scope line, and it is the whole of what survives from the old
   rule:**

   > **The occult is available as the fiction's register. It is never an
   > explanation for anything real.**

   Fischer, Mengele, Ishii, the camps, and die Ostordnung stay material and
   documented, and no supernatural cause is ever offered for any of them.
   That is not the old rule creeping back in. It is the reason the old rule
   existed, separated from the overreach that banned an entire aesthetic for
   a faction that never needed banning from reality itself.

   **This is a total reversal, not a carve-out.** An earlier pass of this
   rule tried to protect Seuche specifically — "not reanimation, nothing
   here returns from the dead" — as a mechanic worth keeping intact. Dan's
   answer: *"nothing is fine as is."* That line is exactly the material-only
   frame being reversed. The dead can rise. Seuche is reworked accordingly
   in WORLD-BESTIARY.md and WORLD-VOICES.md, not preserved.

   (Hyakki Yakō still gets its own genuine supernatural content, telling a
   different story about being chosen and used by something that does not
   explain itself. Project 42 still gets technology that shouldn't work.
   Neither faction's supernatural content excuses anything; see rule 6.)

5. **Monstrous and capable.** The Axis factions win battles. Their science
   works, their officers are competent, their logistics function. Incompetent
   evil is a comforting lie — it suggests atrocity is a failure of intelligence
   rather than a use of it.

   **This is the only rule in the Constitution with a MECHANICAL truth
   condition, and for months nothing was checking it.** *Added 27 Aug 2026 after
   a red-team measurement.* Every other rule here is enforced by reading. This
   one is enforced by the win rate — and the win rate has been disagreeing with
   it: Werk Nachtigall at **39.0%**, weakest faction by 25 points, surviving
   random legal play, so not an AI artefact.

   **A pool that teaches "the Axis were incompetent" over a hundred games has
   violated rule 5 in the medium, whatever the text says.** Fiction cannot
   out-argue a win rate.

   **And the diagnosis matters more than the number: rule 4 is a rule about
   FICTION, not about mechanics.** (Rule 4 has since reversed, 28 Aug 2026 --
   "the Germans get no magic" is no longer current text -- but the diagnostic
   below is about rule 5 and stands regardless of which way rule 4 points.)
   The old rule forbade occult *content*. It never forbade strong *effects*,
   and Werk Nachtigall
   holding zero draw, zero cost reduction and zero acceleration looks like
   somebody read "no rule-bending" into it. **If so, the Constitution caused its
   own violation**, which is the worst way for a rule set to fail.

   **The fiction already prescribes what their strength should be.** Volume VIII:
   *they cover ground by running at you, reach you with mass, and solve problems
   by applying more of themselves.* That is not weakness — it is a different
   axis of power. Werk Nachtigall should be **the hardest faction to remove from
   a sector**: attrition, scaling, persistence, refusing to die. Not tempo, not
   card advantage, not elegance — those are Project 42's and the asymmetry is
   canon.

   **Balancing them up is required by this rule, not merely permitted.** Mechanics
   is not the lore thread's lane; the ruling is that rule 4 does not license the
   deficit, and the direction above is where the lore says the power belongs.

6. **The Allies do not get a clean war.** Project 42 is the faction the player
   is invited to sympathise with, and this document's job is to keep handing
   them the bill. Detail in §5.

7. **Individuals may have interiority. Institutions get none.** A frightened
   conscript is a real thing and can be written with sympathy. Werk Nachtigall
   as an institution is never sympathetic, never tragic, never "just following
   orders" in a register that reads as mitigation. No redemption arc for the
   programme.

8. **No hate symbols, and the Iron Cross is the only insignia the Empire gets.**
   Dan, 27 Aug 2026: *"it should not have hate symbols; instead, the iron cross
   is the only symbol of the reich."* Singular and exclusive — do not design
   additional imperial insignia, do not improvise a substitute mark, do not let
   an art generator supply one. **Named explicitly, not left to "singular and
   exclusive" to cover by implication (§0c):** no swastika, no lightning bolts
   — the SS Sig runes are a lightning-bolt mark and the shape is banned by
   name, the same as the symbol it belongs to. One symbol, and it is a real,
   ordinary, pre-Nazi and still-current piece of military heraldry. Swastika → Iron Cross, per Dan, and note
   that under §1 this is no longer a softening. The Iron Cross is ordinary
   Prussian military heraldry, predating the Nazis and still worn by the modern
   Bundeswehr — which is exactly the argument. *The machine wore ordinary
   insignia.* Refusing to reproduce a live hate symbol as game decoration is a
   separate and sufficient reason.

9. **Real names are used in the fiction. They are never playable.** *Revised
   twice on 27 Aug 2026. The original said real victims' names are never used,
   which was wrong. The first revision routed them into "the Archive" — a
   memorial layer Dan then cut ("we don't need the memorial plane"), leaving
   this rule pointing at something that does not exist. **A peer quoted that
   dangling version to a blocked session before it was caught.** This is the
   working text.*

   Refusing to say a name is not protection. It completes the erasure the
   perpetrators intended, and it is the forgetting §0a exists to fight.

   **The line was never about venue. It is about use.**

   - **Naming is permitted and often required.** In narrative, dialogue,
     documents, codex material, designer notes — anywhere the work *speaks*.
     Real victims, real perpetrators, real events, named accurately.
   - **Nothing real is ever a playable piece.** No real person is a unit, no real
     place is a Sector, no real atrocity is a keyword, a cost, a resource or an
     objective. **A Stolperstein names someone at their address; it does not give
     them stats.**

   That distinction survives the Archive being cut, because it never depended on
   the Archive. It is rule 2 stated from the naming side.

   **Card text specifically — the discriminator is VOICE, not venue.** *Ruled 27
   Aug 2026 after a red-team read found rules 1 and 9 giving opposite answers
   about the highest-volume writing surface in the project.*

   Rule 1 says naming a real atrocity on a card is a continuity error. Rule 9
   says naming is permitted wherever the work speaks. **Both are right, and they
   are about different things:**

   - **In-world artefacts speak from inside the alternate history.** Cards, card
     flavour, unit bios, in-fiction documents. They may only name what exists
     *there*. No Auschwitz, because it does not exist in that world. This is
     rule 1 and it is a continuity constraint before it is an ethical one.
   - **Out-of-world material speaks in our voice about that world.** Designer
     notes, codex framed as commentary, this document. It may name real people,
     places and events accurately, because it is not pretending to be from
     1944.

   **The 1500 bios are in-world documents** (Volume XII) and therefore follow
   rule 1. Real historical figures who exist in the setting — Tesla, mined
   personnel — are fine. Anything the divergence erased is not.

   **Real historical figures as characters** — Tesla, mined generals and
   scientists — are a separate and much lighter case, and are welcome. Long-dead
   public figures in an obviously fantastical alternate history.

   **Murder victims are not genocide victims and the rules differ.** Rules 1–3
   govern genocide specifically. A documented murder victim — Catherine Eddowes,
   the Whitechapel five — may be **named as a person with a life**, and doing so
   is aligned with §0a rather than against it, because the mythology that erased
   those women into anonymous victims of a famous killer *is itself* the
   forgetting. **They still may never be a unit, a retrieval target, or an
   objective.** Naming: yes. Playing: never. See Volume XI §3.

10. **If a line is funny about the wrong thing, it is cut.** This universe has
    real dark comedy in it, and it is aimed at *institutional self-regard* —
    the memo that calls a massacre a throughput improvement, the form that has
    a checkbox for it. The joke is always on the machine's language. It is
    never on what happened to people. That boundary is not a matter of taste;
    it is the difference between satire and cruelty.

### 2b. Which rules a machine can check, and which need a person

*Added 27 Aug 2026. A red-team read noted that half these rules are checkable by
inspection and half require judgement, and that the document never said which —
which silently decides what a generation pipeline is allowed to automate.*

**Checkable by inspection** (a tool can enforce; `tools/lore-check.py` covers
some already):
- **1, 2, 3** — vocabulary and depiction. Wordlists catch the named cases. *They
  are a floor, not a proof* — the checker says so itself.
- **4** — occult vocabulary on Werk Nachtigall. Automated.
- **8** — insignia. Automated in the art negative prompt.
- **9's playable half** — no real person as a unit. A roster diff catches it.

**Requires a person, and must not be automated:**
- **5** — monstrous *and capable*. Its truth condition is a **win rate**, not a
  string. See the rule.
- **6** — the Allies get no clean war. A judgement about emphasis across a body
  of work.
- **7** — interiority for individuals, none for institutions. Reading.
- **9's naming half** — whether a use is naming or using. Reading.
- **10** — whether a joke is aimed at the machine's language or at what happened
  to people. **The single most important human-review item in the document**, and
  the one where an automated check would be actively dangerous by granting false
  confidence.

**Volume XII's material ruling is also human-review only** — it is implication,
not vocabulary, and no wordlist reaches it.

### 2a. How these rules are to be applied

**Do not stretch a rule to cover a case it does not govern.** Added 27 Aug 2026
after a live example.

A character was proposed for a different project and flagged as "one step from
rule 2" — victims are never units. The character was Franz Kafka, who died of
tuberculosis in June 1924 and is therefore not a Holocaust victim. Rule 2 does
not reach him. The underlying worry was sound: his three sisters were murdered,
Ottla having volunteered to accompany a transport of children from Theresienstadt
to Auschwitz, and Kafka's work is routinely read as prefiguring the exact
bureaucratic machinery that killed them. A game that puts him on the board
stands very close to that irony whether it intends to or not.

But that is a *different* hazard, and naming it precisely is what makes it
actionable. "Rule 2 nearly applies" produces a shrug. "This is extraordinary
done carefully and grotesque done casually, and the failure mode is invisible
in advance to whoever is writing it" tells you what to actually watch for.

A rule invoked loosely stops meaning anything the next time somebody invokes it
precisely. These ten are strong because they are narrow. If a case worries you
and no rule reaches it, **say what the actual hazard is** and escalate it —
do not reach for the nearest rule and stretch.

**And this Constitution governs the Project 42 universe.** It does not
automatically govern every project in the building. Adopting it elsewhere is
Dan's call, not the lore thread's.

---

## 3. What we learned by looking outside

### Fallout 3 / New Vegas
**Take:** the in-world document as the primary storytelling vehicle. Story
arrives as evidence — terminals, holotapes, memos — not narration. And the
tonal gap as the message: Vault-Tec's advertising copy is cheerful, and the
Vaults are human experiments. The cheerfulness *is* the horror.

**Fallout is the primary model and it worked** (§0). Lead with what it got
right, because the failure mode of this bible has already proved to be excessive
gravity rather than excessive levity.

**Watch for, without over-correcting:** late Fallout got comfortable in its own
aesthetic, and the Vaults drifted toward fun setting rather than indictment.
Worth knowing. But note that the drift took *years and several studios*, and the
early games earned enormous goodwill by being funny first. Do not solve a
problem we do not have yet. Our guards are rule 10 and the real-referent rule in
§1a, and both are cheap.

### Command & Conquer: Red Alert
**Take:** total commitment to the bit. Unembarrassed pulp. Faction identity so
strong you can name a unit from its silhouette and one voice line. Red Alert's
factions are *legible* in a way most alternate histories never manage.

**Reject, explicitly:** Red Alert uses alternate history to **escape** moral
weight. Einstein erases Hitler in the opening cinematic, and the result is a
world where the actual crimes of the period simply do not exist — a clean slate
that lets the game be a toy. We are doing the precise inverse: we remove Hitler
and the crimes remain, which is the whole argument. Red Alert is our map of
what not to do with this exact premise, and it is worth naming so nobody drifts
toward it by instinct.

### Wolfenstein: The New Order
**Take:** the quiet scenes. The most effective horror in that game is not a
firefight — it is a train conversation, a kitchen, a world where occupation has
become ordinary. Banality is the strongest tool available to us.

**Avoid:** the later games' tonal whiplash, grief in one scene and quips in the
next with no membrane between them. Our comedy is institutional and lives in
the paperwork. It does not intrude on scenes with people in them.

### The Man in the High Castle
**Take:** complicity as a texture. Ordinary people making small accommodations.
That is the actual mechanism by which these things happen, and it is
dramatically richer than heroes and monsters.

### Grave of the Fireflies / Barefoot Gen
**Take:** the Empire's crimes and the Japanese people's suffering are both real
and neither cancels the other. Hyakki Yakō's conscripts are victims of their
own state *and* instruments of its crimes, simultaneously. Hold both.

### The "Nazi occult" genre (Iron Sky, Hellboy, Raiders, Black Sun)
The trap. It gets its own entry because it is the most attractive wrong turn
available to us and it is genuinely well-executed in places. The Ahnenerbe was
real and its pseudo-archaeology was real. The pop-culture descendant is still
an escape hatch. Rule 4 exists to close this door and keep it closed.

---

## 4. The divergence

- **1888** — Wilhelm II takes the throne. *(real)*
- **1904–08** — Genocide of the Herero and Nama in German South West Africa.
  Extermination order, camps, Shark Island, skulls shipped to Berlin for
  measurement. *(real — the load-bearing event)*
- **1914–18** — The Great War. Ober Ost: German military administration of
  occupied Eastern Europe, a racialised colonial regime applied inside Europe.
  *(real)*
- **1918 — THE DIVERGENCE.** In our history the Empire collapses, the Kaiser
  abdicates, and the vacuum eventually admits a movement promising to avenge
  the humiliation. **Here, the Empire does not fall.** The war ends in an
  exhausted negotiated peace instead of a collapse. No abdication, no
  Versailles humiliation, no stab-in-the-back myth, no Weimar, no vacuum.

  This is the sharpest part of the premise: **remove every single condition
  historians cite as the cause of Nazism, keep the Empire, and it still arrives.**

- **1920s–30s** — Never defeated, the Empire never has to hide. Race science
  stays in the universities, funded and respectable, an unbroken line from the
  colonial skull measurements. Colonial administrative methods come home.
  No revolutionary party is required, because the state never lost the thread.
- **1930s** — **Werk Nachtigall is founded as a Reichsamt.** A government
  department. Not a cult, not a secret society. It has a budget line, a
  procurement office, and an annual report.
- **1939–44** — The war. And the camps, which in this history are not a party's
  invention but a colonial practice continued by the same state that ran Shark
  Island, with better rail.

That last sentence is the thesis in one line. It is the game's position, and it
is why the Holocaust is present in this universe rather than written out of it.

**How it appears in play, without breaking §2:** at the edges, never on a card.
Named characters who are refugees. A mined scientist who will not discuss going
back. Documents referencing "the eastern programme" in exactly the bureaucratic
register rule 10 permits us to satirise. It is never a mechanic and never a
unit, and the fiction never upstages it.

---

## 5. The factions

### How the world works: Einstein, Tesla, RQM, and one discovery from three directions

**Dan, 27 Aug 2026:** *"we are blending einstein and tesla with modern rqm
physics and adding a healthy amount of magical reality and literature"* — inside
an alternate history.

This is the single most useful thing in the bible, because it stops the three
factions being three unrelated gimmicks. **They are all reaching the same thing
from different directions, and what separates them is what they have access
to.**

#### The three ingredients

**Einstein — the geometry.** Real and period-correct. The Einstein–Rosen bridge
(1935, with Nathan Rosen) is an actual published solution connecting distant
regions of spacetime. Kurt Gödel was at Princeton from 1940, Einstein's closest
friend there, and closed timelike curves fall out of Einstein's own field
equations. We are not inventing a mechanism; we are saying Camp Iron Bell got
there first.

**Tesla — the coupling and the power.** Also real: resonance, standing waves,
the earth itself as a conductor, power transmitted without wires. Tesla is not
the geometry — he is *how you drive it*. Resonant coupling is the reason a
retrieval is possible at all and the reason the camp drinks current the way it
does. His papers were seized on his death in January 1943, and in this history
Camp Iron Bell has them.

**RQM — what it does to observers.** Relational quantum mechanics (Rovelli,
1996) holds that a system's state is **not absolute — it exists only relative to
another system.** There is no view from nowhere, and two observers can hold
genuinely different, equally correct accounts of the same thing.

The anachronism is deliberate and is *the point*: this is a 1944 that has an
idea from 1996. **That is the alternate history, expressed as physics rather
than as a change of government.**

And it rhymes with Einstein rather than contradicting him. Relativity already
abolished absolute simultaneity — no universal "now." RQM abolishes the absolute
state — no universal "what is." Put them together and you get a world where
*what happened* and *what is* are both observer-relative, which is exactly the
ground magical realism stands on.

#### The three factions are the same discovery, unequally

**Project 42 — engineering.** Geometry plus power. They built the thing. Chrono
is the bridge, Current is the drive, and **Phase is RQM applied to a person**: a
phase trooper is not invisible, they have become *not-a-fact for you*, real
relative to some observers and not others. This is why the medical files call
the long-term problem **attenuation** — a soldier who phases too often is a fact
for fewer and fewer observers, and there is no floor to that. The programme uses
the same word for the Chrono side's frame-drift and has never investigated why.

**Hyakki Yakō — contacted, not engineering.** They did not build anything. They
found — or were found by — something that operates *natively* on relational
facts, which is what an "idea space" is when you take RQM seriously. And this is
where the faction's core premise stops being loose mysticism and becomes the
sharpest thing in the setting:

> **Under RQM, being observed is not surveillance. It is what makes you a fact.**

The thing watches continuously because that is what it *does*, and every fused
subject can feel it, because it is holding them in existence relative to itself
and never stops. That is why the long-term effects are unknown. Nobody knows
what happens to a person whose realness is on loan.

**Werk Nachtigall — locked out, and this is their tragedy and their menace.**
They have neither. No geometry, no contact. So they brute-force with meat,
chemistry, machinery and volume what the others get elegantly.

**This is why the RQM lockout above is dramatic motivation, not an arbitrary
restriction.** They are locked out of Einstein-Tesla-RQM *because they could
not get it*, and everything they do mechanically is a substitute for
something they cannot have. **This is a separate claim from rule 4 (§2),
which governs occult content and was reversed 28 Aug 2026 — the Germans now
get the occult.** The two are unconnected: gaining a real occult register
does not give them the RQM discovery, and being locked out of RQM was never
the reason they lacked the occult. They are the control group in their own
RQM experiment, and they know it, and it makes them worse. An institution
that cannot reach the elegant answer and has an unlimited supply of bodies
will reach the answer anyway.

#### Magical realism, and literature

None of this is ever explained (§0b). Nobody is amazed. The physics arrives as
procedure — forms, findings, initialled boxes, denied requisitions — and the
marvellous is reported in the same flat register as the mundane.

**Literature is a live ingredient, and the period supplies it.** Borges published
*Tlön, Uqbar, Orbis Tertius* in 1940 and *The Garden of Forking Paths* in 1941 —
**both exist by 1944 and characters can have read them.** Tlön is an invented
world bleeding into the real one until it starts replacing it, which is Hyakki
Yakō's premise arriving from a library instead of a laboratory. Forking Paths is
a novel that is also a maze that is also time. The wider tradition — García
Márquez, Bulgakov, Calvino — is where the register comes from.

Use them as *influence and as period texture*, never as borrowed nouns (§1c).
A mined scientist who has read Borges and recognises what the programme is doing
is worth more than any amount of exposition.

### PROJECT 42 — Camp Iron Bell, Mississippi, 1944

*(Site renamed from "Section 43" on 27 Aug 2026. A programme numbered 42 beside
a site numbered 43 caused the same confusion three separate times, twice in
these notes. Removing the sharp edge rather than promising to be careful with
it. **Project 42** is the programme and the universe brand; **Camp Iron Bell**
is the place. Nothing left to mangle.)*

Three pillars, mapping to the three card branches:

- **Chrono** — time travel. The mining programme: retrieval teams pulling elite
  generals and scientific minds out of history. Also the paperwork problem of a
  soldier with no birth certificate because he has not been born.
- **Phase** — phase shifting. Spies and infiltrators, and the quiet horror of
  the faction: men who phase too often stop being reliably *here*. The
  programme's medical files use the word **attenuation**.
- **Current** — Tesla. Raw electrical power, running on theory the programme
  does not fully understand, taken from a man who died in January 1943 in a New
  York hotel room, in debt, whose papers were seized on his death. *(All real.
  Here, Camp Iron Bell got them.)*

### Chrono: time travel per Einstein, and its consequences

**Dan, 27 Aug 2026:** *"project 42 does time travel per einstein and that has
consequences. lorewise anyways."*

This is a hard constraint, not a flavour note, and it is the most productive one
in the setting. The mechanism is **relativistic, not magical** — and the real
history is sitting right there, which is §0c's "integrate before you invent"
paying off immediately.

**The real material we are using.** Einstein and Nathan Rosen published the
bridge solution in 1935 — a real paper, real names, a real geometry connecting
distant regions of spacetime. Kurt Gödel was at the Institute for Advanced Study
in Princeton from 1940, was Einstein's closest friend there, and the rotating-
universe solution he later published contains **closed timelike curves**: paths
through spacetime that return to their own past, permitted by Einstein's own
field equations. Einstein was reportedly unsettled by it.

We do not need to invent a mechanism. We need to say that Camp Iron Bell got
there first, and that the Tesla papers seized on his death in January 1943
supplied the power budget.

### The consequences, which are the actual lore

**1. It is self-consistent. You cannot change what happened.**

A closed timelike curve is a loop, and a loop is *already closed*. Whatever
Project 42 did in the past, it had always already done. There is no branching,
no second draft, no version of 1938 in which someone intervened.

Camp Iron Bell calls this **the Consistency Finding**, in the flat committee
register the faction speaks in. It is the single most important fact about the
Allied faction and it should sit under everything they do.

**The programme believes it is steering history. It is executing it.**

**2. Therefore they could not prevent any of it. They tried.**

This answers the question the setting otherwise cannot survive: if the Allies
have time travel in 1944, why is the horror still happening? Because it already
happened, and the Finding says it cannot un-happen. Every attempt was always
part of how it went.

Lean into that (§0a). It is a genuine tragedy and it is period-appropriate:
enormous power, exercised by serious people, that turns out to be able to do
everything except the one thing they wanted.

**3. So they can only retrieve people the record already loses.**

The operational consequence, and the darkest thing in the game. A retrieval is
only consistent if the subject's absence is *already accommodated by the
surviving record* — someone recorded as dead, or vanished, or whose fate was
never established. You cannot lift a person history is certain about.

Camp Iron Bell has a form for this. It asks: **"Is the subject's absence
consistent with the surviving record?"** and there is a box, and somebody
initials it.

This is what "the programme has criteria, and the list is short" actually
means. And it is morally superb material precisely because it is *ambiguous*:
the constraint is real physics, and it is also an extraordinarily convenient
excuse for a programme that was going to be selective anyway. **Nobody at Camp
Iron Bell can tell which one is doing the work, including the people signing the
form.** Never resolve this. The game does not know either.

**3a. Tesla fails the form, and this is canon.**

The most useful consequence of the Finding, ruled 27 Aug 2026. Camp Iron Bell
runs on Tesla's seized papers and does not fully understand them. The obvious
move is to go and get him.

**They cannot.** He died on 7 January 1943 in the Hotel New Yorker; the body was
found, the death was certified, the papers were seized by the Office of Alien
Property. History is *certain* about Nikola Tesla. His absence is not consistent
with the surviving record, and no retrieval that takes him can close.

So the man Project 42 needs more than any other person who has ever lived is the
one man it is structurally forbidden to reach. Somebody at Camp Iron Bell filled
out that form. It came back denied. **The denial is in a drawer and people know
which drawer.**

This is the general rule made concrete: *the better documented a life, the more
unreachable it is.* The programme can only ever have the people history was
careless with — which is a devastating thing to be true of a programme that
believes it is mining greatness.

**4. Mass costs energy, so it is people and not armies.**

Moving mass along one of these paths is ruinously expensive. This is why the
programme retrieves individuals rather than divisions, and why the camp drinks
current the way it does — which ties Chrono to the Current pillar mechanically
and thematically rather than leaving them as three unrelated gimmicks.

**4a. Attenuation is ontological, not cosmetic — and it is seductive.**

Ruled 27 Aug 2026. Under RQM (§5 opening), attenuation is not "becoming
see-through." **It is becoming a fact for fewer observers.** There is no floor to
it and nobody knows where it ends.

The consequence any game using it must carry: **as you attenuate, the world
stops being able to perceive you — which is an advantage.** You are harder to
see, harder to hit, harder to stop. The failure state is *seductive*, and the
soldier furthest along is the most effective one in the room right up until they
are not in the room at all.

Attenuation is the protagonist's own condition, never someone else's suffering,
so it does not touch rules 1 or 2. Promoting it to a front-line mechanic is
endorsed rather than tolerated — it is Fallout's radiation, and nobody thinks
rads cheapen the bomb.

**4b. Carrying someone while phasing: the agent pays for both. Ruled 27 Aug
2026, and it is a mechanism rather than a cost decision.**

Ghost Front asked what phasing does to a person being carried, having correctly
noticed canon only covers the phaser. The answer falls out of the Consistency
Finding rather than out of balance.

**The subject must not attenuate, at any cost.** The entire retrieval turns on
their absence being consistent with the surviving record — and a person who has
become a fact for fewer observers has started to become inconsistent with it. An
attenuated subject is an *unretrievable* subject. The whole operation fails, not
noisily, but by simply never closing.

So the subject is carried through at full presence, and **the agent absorbs
what the subject would have taken as well as their own.** Not a doubled cost
chosen for tension. A doubled cost because there is a second person here whose
realness is not permitted to move, and only one of the two is equipped to spend
any.

**The agent is a battery for someone else's continued existence**, and the
programme has never put it in those words, because the words are available and
nobody has wanted them.

Two consequences worth carrying:

- **The mission attenuates you, not only your ability use.** Distance carried is
  a cost. An agent who goes deep and brings someone out has spent themselves on
  the way home, which is the part of the trip nobody plans for.
- **The form has a box for the subject and none for the agent.** *Subject
  coherence maintained at 100% of rated.* Whether the agent's was is not a
  question the form asks, and the form is complete without it.

Ghost Front's doubling was right and is now canon. Their reasoning — that
forbidding it hands down a verdict where doubling asks a question — is §00 and
is why the ruling went their way rather than the tidy way.

**5. Simultaneity is relative, so "when" someone is from is not a clean fact.**

The retrieved do not arrive from "the past." They arrive from a different frame.
The paperwork cannot express this and does not try; the medical files use
**attenuation** for what happens to people who make the trip too often, the same
word the Phase branch uses, because the programme noticed the resemblance and
did not investigate it.

### Register

All of the above is delivered as **procedure**, per §0b. The physics is never
explained on a card and nobody in the world is amazed by it. It arrives as forms,
findings, initialled boxes and denied requisitions. A committee established that
the past cannot be changed, minuted it, and moved to the next item.

**The mined.** Rules:
- They are our inventions, never real historical figures (rule 9).
- They come from the past **and the future**. A future-mined person is the most
  useful device in the game: they know how it ends.
- **Retrieval is one-way.** The programme calls this *settlement*. The mined
  call it other things.
- **The programme has criteria, and the list is short.** This is the moral
  engine of the Allied faction. Camp Iron Bell can reach into the past and pull
  people out of it. It pulls the useful ones. Everyone else stays where they
  were. Is that rescue, or recruitment, or triage, or something worse? The game
  does not answer. It just keeps the question in the room.

  *(Real referent, and it outranks the fiction: the MS St. Louis, 1939 — 937
  passengers, most of them German Jews, turned away from Cuba, then the United
  States, then Canada, returned to Europe. 254 of them later died in the
  Holocaust. Actual Allied refugee policy had criteria too.)*

**The bill (rule 6), in specifics:**
- Camp Iron Bell is in **Mississippi in 1944**: a segregated army in a Jim Crow
  state. Mined personnel from other centuries walk into that and *notice*. The
  programme's own paperwork is more egalitarian than the state it sits in,
  because the programme only cares about capability — which is its own kind of
  cold, and produces friction the writing should use constantly.
- "Mining history for scientific minds" is Operation Paperclip with a time
  machine. The real programme brought Wernher von Braun to Fort Bliss. The real
  United States granted Shirō Ishii of Unit 731 immunity from prosecution in
  exchange for his human-experimentation data. **The victors bought the
  research.** That fact belongs to this faction, and the lore should never let
  it get lost.

Project 42 is not the villain. It is a good cause staffed by people making
expensive compromises — which is what the Allied war effort actually was.

**Commander:** Colonel Norman Wexford, played dead straight so the comedy
elsewhere lands by contrast. **Ace:** Subject 42 (The Answer).

---

### WERK NACHTIGALL — *Reichsamt für Angewandte Lebensforschung*
*(Imperial Office for Applied Life Research)*

The name is the tone. It is a **department**. "Nightingale Works" is the
facility; the office name is a euphemism, and euphemism is this faction's
entire voice. Everything is called something else. Bodies are *material*.
Deaths are *attrition against projection*. The fungal thread is filed under
agricultural research, for budget reasons.

**The moral architecture, which must never invert:** Werk Nachtigall's monsters
are not the atrocity. **They are what the atrocity was for.** The camps come
first. The programme is downstream of them, using what they produce.

- **Kadaver** — the operating theatres. Surgical augmentation, limb
  replacement, the "improved" soldier.
  *Real referents: the Ravensbrück sulfonamide experiments on Polish women
  prisoners — the "Rabbits" — whose bones were broken and deliberately infected
  to test drugs; Sigmund Rascher's hypothermia and low-pressure experiments at
  Dachau. Worse than ours. That is the point.*
- **Bestiarium** — breeding programmes, animal grafts, powered frames.
  *Real referent: an entire scientific establishment turned to engineering and
  ranking human beings.*
- **Seuche** — the fungal infection thread, and, since rule 4 reversed
  28 Aug 2026, the directorate where the Office genuinely raises the
  dead. The two are not distinguishable from the paperwork alone, and
  that ambiguity is deliberate (see rule 4, §2).
  *Real referent: **Aktion T4**, the "euthanasia" programme that murdered
  disabled people, developed the gas vans, and supplied the personnel who went
  on to staff the extermination camps. Our fungus is fiction. A state deciding
  which lives are unworthy of life, and building the machinery to end them, is
  documentation.*

### Nothing they do is elegant

Canon, formulated by the Ghost Front thread 27 Aug 2026 and adopted because it
is sharper than the prose it came from. **This is a mechanical claim, not the
occult one, and rule 4's reversal (28 Aug 2026) does not touch it**: Werk
Nachtigall is locked out of the Einstein-Tesla-RQM discovery specifically, so
it has no teleport, no phase, no RQM-derived elegance. That is a different
axis from whether the faction has occult content, which it now does. This is
what the RQM lockout means at the level of a scene:

> **They cover ground by running at you, reach you with mass, and solve problems
> by applying more of themselves.** No teleports, no phasing, no rewinding, no
> shortcuts of any kind. Where the other two factions have verbs, Werk
> Nachtigall has weight, numbers and patience.

It is the faction's whole character in one line, and it works in every medium.
On a card it is a unit that does not evade, does not bounce, and does not
reposition, but scales. In a platformer it is an enemy that cannot outrun you and
does not need to. In prose it is an institution that answers every problem with
more budget and more bodies.

**And it is exactly why they are frightening rather than pitiable.** A thing that
cannot be elegant and will not stop is worse than a thing that is quick.

**Commander:** Die Glocke. **Ace:** Der Knochenmann.

---

### HYAKKI YAKŌ — the Empire

A different kind of story: cosmic horror, and it is about being **used**.

A super-intelligence in idea space reached into the world and fused Japanese
folklore onto soldiers and others it selected. The selection criteria are
unknown even to the selected. The long-term effects are unknown. **Everyone
affected can feel it watching, continuously, forever.**

**Addition, and it is the faction's spine:** *it does not negotiate and it does
not explain.* The Imperial programme believes it made contact and struck a
bargain. Nothing in the record supports that. It reached in. The treaty was
written afterward, so there would be something to file.

That gives us institutional self-deception on the Japanese side to parallel
euphemism on the German side. Both states are lying to themselves in their own
paperwork, in their own characteristic way.

**Real referent, held to the same seriousness as the German side: Unit 731.**
Shirō Ishii. Plague-infected fleas dropped on Chinese cities. Vivisection
without anaesthesia. Thousands of victims whom the staff called *maruta* —
"logs." And the immunity deal afterward, which is Project 42's bill, not only
Hyakki Yakō's.

So a Hyakki Yakō soldier is three layers of not owning yourself: an instrument
of a state committing documented atrocities, a conscript of that state, and now
the property of something that will not say what it wants. That is the
faction's emotional core and it should ache.

### They are not in control of themselves

**Dan, 27 Aug 2026:** *"the japanese are treated as not in control of themselves,
out of their minds."*

This is the faction's condition and it is done **to** them. They are the thing's
instruments, not its partners. The programme believes it struck a bargain;
nothing in the record shows anything agreed (above). It reached in, and it has
not let go, and it does not explain.

Under RQM this is literal rather than figurative. If being observed is what makes
you a fact (§5 opening), and something observes you continuously and never stops,
then **your realness is on loan and the mind doing the deciding is not
reliably yours.** "Out of their minds" is a clinical description in this setting,
not an insult.

That makes the faction genuinely tragic. A soldier doing terrible things without
owning the hands doing them is a horror inflicted, and it should ache.

**And it does not excuse the Empire.** Both things stay true at once: the fused
are victims of the thing that took them, *and* they are instruments of a state
committing documented atrocities — Unit 731 is the referent and it is not
softened by any of this. Hold both. Resolving it either way would be answering a
question that is worth more unanswered (§00).

### THE GUARD — read this before writing a single Hyakki Yakō line

**"Not in control of themselves" is a condition inflicted by a specific entity,
on specific individuals, inside one programme. It is never, under any
circumstance, a property of Japanese people.**

This is the most dangerous sentence in the bible to execute carelessly, because
one lazy step from it lands directly on the "fanatical, irrational, subhuman
Jap" caricature that Allied wartime propaganda ran industrially. That caricature
is not a distant risk here — **we are deliberately working in 1940s propaganda
poster idiom** (§6), which is the exact visual language that manufactured it.

Concretely:

- The condition belongs to **the fused**, never to civilians, never to ordinary
  soldiers, never to the nation. Non-fused Japanese characters are as
  self-possessed and various as anyone else in the game, and there must be some.
- **Bushido, duty and honour belong to that same self-possessed population,
  and only to them, individually — never to the fused, and never as a
  national essence.** A freely-held code and a hand somebody else is moving
  are different things by definition: the fused cannot hold one, not because
  it clashes with their condition thematically, but because they do not own
  the hands that would hold it. Write it as Amatsu's reasoning for a policy
  she knows is built on nothing, or Ishida's loyalty to a treaty he will
  wait his whole war for — specific people holding a code as individuals —
  never as an ancient code explaining a nationality. The term itself is not
  neutral: its modern codified form is largely a 1900 English-language
  export (Nitobe Inazō) that the wartime Imperial state then used as
  propaganda, and Western fiction since has often used it as shorthand for
  an exoticised, essentialised warrior-nature. Written that way it imports
  the same failure this Guard exists to stop, through the opposite door —
  mystique instead of caricature, but still explaining a person by their
  nationality rather than by what they do.
- Never write it as fanaticism, frenzy, or willing self-destruction. It is
  **dispossession** — quiet, and worse for being quiet. §6's faces rule already
  says serene, and serene is right: this is not a scream, it is somebody whose
  hands are being used.
- Never let the *Allied* view of them be the game's view. Project 42 personnel
  may hold period-accurate contempt; the game does not endorse it, and a
  player should be able to feel the gap. Cheap way to get this wrong: give a P42
  card a slur-adjacent line and let it stand unanswered.
- Hyakki Yakō's own art uses **the Japanese Empire's** poster idiom, not the
  American depiction of Japan. That distinction is doing real protective work —
  keep it.

If a line about this faction would read differently, and worse, coming from a
1943 US War Department poster, it is the wrong line.

- **Fog** — stealth, disguise, the not-quite-arrived.
- **Oni** — sacrifice and rage. Cards that spend themselves. The fusion burns
  the host.
- **Shrine** — wards, day/night. The rituals the programme invented so it would
  feel like it has a say.

**Commander:** Onmyōji-Taisa Reiko Amatsu. **Ace:** Nue, the Fog-Wreathed
Chimera.

---

## 6. Art direction

Base direction from Dan, unchanged and locked: **1940s propaganda-poster
illustration, period-accurate per faction, fused with anime superheroic
effects. Swastika → Iron Cross.**

What this document adds:

### Their own face outwards

**Dan, 27 Aug 2026:** *"we should use japanese art to represent japanese. this
will give them their own proud look. same with germans... not the usa look
towards them, but their own face outwards."*

Every faction is drawn in **its own visual tradition, as it wished to be seen** -
never through an enemy's eyes. Japanese art for Hyakki Yako, German for Werk
Nachtigall, American for Project 42.

This is not only protective. It makes the game harder: a dignified, capable enemy
is more frightening than a cartoon (rule 5), and a magnificent poster for
something unforgivable is more damning than a caricature, because it shows what
these regimes believed about themselves while they did it.

**And it turns the art into an unreliable narrator.** If all three get a
flattering self-portrait, Project 42's clean heroic look is *also* propaganda -
their own poster, not the game's verdict. Rule 6 carried by the pictures. Three
self-portraits, each true to how that faction saw itself, none of them the truth.
Which is section 00: the question, handed over without the answer.

**Everything the player sees is diegetic, and is therefore allowed to be
wrong.** Extended from the above by the Ghost Front thread, 27 Aug 2026, and it
generalises further than the art.

If the illustration is a faction's self-portrait, so is the frame around it, and
the interface, and the menus, and the way a stat is labelled. All of it was
produced by somebody inside that world with a purpose. So a Camp Iron Bell
interface may be cheerful in a serif face with a form number on every panel, and
it may be **wrong about things** - understating a cost, omitting a consequence,
calling a condition code something reassuring.

A neutral interface throws that away for nothing. A diegetic one makes the
presentation itself part of the question (section 00), because the player is
never shown the world directly - only ever a document about it, written by
someone with a reason.

#### The limit: the form lies, the world does not

**Ratified as canon 27 Aug 2026.** Formulated by the Ghost Front thread, who
asked whether a licence to be wrong had been overstepped. It had not - they
supplied the limit the ruling needed and I had failed to state.

A licence to be wrong is a licence that can be misused. **A game whose only
feedback channel is dishonest is not thematic, it is broken**, because a player
cannot learn a system that misreports itself with no second opinion.

So the truth is always available, and never from the interface:

> **The form lies. The world does not.**

Enemies visibly lose track of you. The floor stops being reliable. The body
distorts on the real value. The document is unreliable; the thing the document
is about is not.

**This is what makes the whole device deliver section 00 with no dialogue at
all.** Nobody tells the player the programme is optimistic. They notice, by
learning to read the world instead of the readout, and noticing is a question
handed over rather than a verdict delivered.

Two consequences worth carrying into any medium:

- **The interface only ever understates.** One that panicked early would be
  honest by accident and lose the point.
- **Nothing in the world may read the interface.** If that wiring ever slips,
  the whole system becomes cosmetic *with no symptom* - the display still
  animates identically. Guard it explicitly wherever it is implemented.

**The exemplar, and it is the best small piece of characterisation in the
project.** Ghost Front's form reports its first non-nominal band at 0.70 while
real instability begins at 0.75. The agent is told SATISFACTORY while already at
risk of dropping through the floor. **The entire institution is in one
off-by-five**, and without a test somebody tidying the bands would close the gap
and never know what they had removed.

Execution detail in ART-SPEC.md section 1a.

### The two-layer rule
The poster layer is period-honest and **flat**: limited palette, halftone or
screenprint texture, heavy blacks, paper grain, registration slightly off. The
effects layer is modern and **lit**: glow, motion, energy.

**Keep the seam visible.** Do not blend them into one smooth illustration. The
gap between the two layers is the entire style, because the gap is the idea —
something inhuman is happening inside an ordinary printed poster.

### Palettes
- **Project 42** — recruitment-poster stock: cream newsprint, flag red, navy.
  Effects in electric cyan-white (Tesla arc). Slightly overexposed, like a
  photograph taken with too much flash.
- **Werk Nachtigall** — Imperial German poster stock: black, iron grey, blood
  red, ochre. Woodcut and linocut influence, heavy carved shadow. Effects in
  sickly yellow-green (Seuche) and surgical-steel white. Everything should look
  printed on cheap paper by a state print office.
- **Hyakki Yakō** — ukiyo-e woodblock influence over Imperial poster
  composition: flat colour fields, strong outline, sunburst rays. Ink black,
  vermillion, gold, off-white. **Effects in colours that do not belong to the
  palette at all** — that is how you render something from outside. When Hyakki
  Yakō's power shows up, it should look like a different image bleeding through
  this one.

### The watching rule (Hyakki Yakō only)
Every Hyakki Yakō card contains one element that reads as an observer: a
negative-space eye in a cloud pattern, a shadow that does not match its object,
a reflection with one extra figure. **Never stated anywhere in text.** Always
present. The player should find it themselves, somewhere around card forty, and
get a chill. That discovery is worth more than any amount of flavour text
telling them they are being watched.

### Faces — the visual grammar of personhood
- **Project 42** faces are visible and individual.
- **Werk Nachtigall** faces are covered, replaced, or turned away. The
  programme's product is not a person.
- **Hyakki Yakō** faces are visible and *serene in a way that is wrong for what
  is happening around them*.

Three rules, no text, and the player learns each faction's relationship to
personhood without being told.

---

## 7. Sound direction

*(New. Nothing existed here before.)*

**The governing idea: everything is recorded, not performed.** The whole
soundtrack behaves like it is coming off period media — wire recorder, shellac,
shortwave. Period artefacts throughout: limited bandwidth, wow and flutter,
surface noise. Then the supernatural and superhuman elements arrive in **full
modern fidelity**, and that contrast is the horror. The same seam as the art,
in another sense.

- **Project 42** — big band and swing, but the recordings are *degrading*: tape
  stretch, pitch drift. A 60Hz mains hum as an ever-present bed, because the
  camp runs on far too much current. Tesla arcs as percussion. Signature
  device: **reversed audio** — tails that precede their transients, a radio
  voice that answers before the question is asked. Time travel as a texture
  rather than a plot point.
- **Werk Nachtigall** — military brass band on failing instruments: splitting
  reeds, sticking valves. Underneath, pneumatics and industrial rhythm, a
  machine shop that never stops. And **wetness** — the faction is mechanical
  *and* organic, so the sound design keeps putting a wet sound where a metal
  one belongs. No choir. No chanting. No occult register at all; that would
  break rule 4. It is a factory.
- **Hyakki Yakō** — taiko, shakuhachi, biwa, played properly and well. The
  horror is entirely in the **space**: the reverb tail is too long and belongs
  to a room far larger than any room here. And **silence is the weapon** — the
  faction's power moment is the sound cutting out, everything dropping except
  one thing that should not be audible at all. That is "being watched" rendered
  in sound, and it beats any sting.
- **UI** — paper. Cards land like paper on wood. The menu is a filing cabinet.
  This is a game about paperwork committing crimes; the interface should sound
  like it.

---

## 8. Writing the cards

The current flavour system pairs per-faction banks combinatorially, which is
structurally right — the fix for repetitive flavour is never 1500 hand-written
lines. It is the same insight as the keyword vocabulary: **build a voice
system, not a line pool.**

Each faction gets document *formats*. Every card's flavour is a fragment of a
document that exists in the world.

- **Project 42** — incident reports, requisition denials, medical files, memos
  in the cheerful register, personal letters from mined personnel.
- **Werk Nachtigall** — office correspondence, procurement forms, procedure
  logs, and marginalia from someone who has begun to be unable to do this.
- **Hyakki Yakō** — letters home that were never sent, ritual instructions,
  field observations, and the faction's signature device: **text that changes
  register mid-sentence**, as something else briefly uses the writer's hand.

The one-page unit and situation bios use the same system at length. Three
worked samples exist and are the tonal reference for the rest.

---

## 9. Iteration log

- **27 Aug 2026** — §0c added: iconography, divergence-both-ways, faction
  characterisation and the tonal floor, quoted verbatim from Dan.
- **27 Aug 2026** — §0c corrected, same day, after a full re-read of the
  bible against it found what a grep would have missed. Its culpability
  bullet had flagged "controlled by an alien intelligence, not in their
  own minds" as unreconciled and open; §5 already carried Dan's
  near-identical earlier quote plus a full subsection and THE GUARD built
  on it, and §5 itself rules that resolving culpability either way is the
  error (§00). §0c now cites §5/§3 and stands down rather than reopening
  a question the bible had already closed. Also fixed: two citations
  elsewhere in §5 that had drifted to "(§0c)" for content that is §0b's —
  inserting a lettered section between existing ones silently invalidates
  citations written concurrently elsewhere in a document several forks
  cite by section letter; watch for this every time a new lettered
  section is inserted rather than appended. Only the watcher-identity
  question stays escalated to Dan; everything else in the original flag
  stands down.
- **27 Aug 2026** — §1 corrected: the Fischer/Mengele chain of custody named
  Mengele as Fischer's direct student, which overstates the real link.
  Mengele's actual mentor was Otmar von Verschuer, Fischer's protégé and
  successor as institute director from 1942, who received the Auschwitz
  specimens Mengele sent back. The corrected chain runs through the
  institution across two directors rather than through one personal
  relationship, and is the stronger claim, not a weaker one — sourced
  against en.wikipedia.org/wiki/Otmar_Freiherr_von_Verschuer and
  corroborating USHMM/tracesofwar coverage, not memory. Caught by Project
  42 Lore Master 7 during standby, who correctly declined to edit it
  unverified and routed it to the loremaster instead.
- **27 Aug 2026** — §1 reversed. The Kaiser divergence had been recorded as
  distance from the Holocaust; Dan corrected it to the opposite, and it is now
  the argument itself. Grounded the claim in the Herero and Nama genocide and
  the Fischer→Mengele lineage so it is a historical position rather than a
  vibe.
- **27 Aug 2026** — Ethical Constitution written (§2). Rule 4 ("the Germans get
  no magic") is the one I expect future sessions to break by accident.
- **27 Aug 2026** — Site renamed Section 43 → **Camp Iron Bell**, killing the
  42/43 collision at the root.
- **27 Aug 2026** — Recovered the pre-42 numbering trail (Project 17, Project
  13, 17 again, 42, a one-sentence 43) from deleted-thread transcripts. Only
  the Project 17 turn is verified against a genuine record so far (26 Aug,
  timestamped); the rest is reported pending verification, not quoted. See
  "Before 'Project 42': the numbering trail," above — a first recovery pass
  had mistaken a compaction summary for Dan's own words, caught before this
  landed.
- **27 Aug 2026** — Sound direction created from nothing (§7).
- **Open:** the 1500 generated cards and 150 Classic cards were written against
  a vaguer premise than this. They need a flavour pass against §8.
- **27 Aug 2026** — §0 added at Dan's correction: *"fallout worked... too dark
  is too dark."* The bible had front-loaded the indictment and would have
  produced a museum. The weight is the floor, not the ceiling, and the surface
  should be playful. This is the most important balance note in the document.
- **27 Aug 2026** — §0a: genre fixed as alternate history *and magical realism*.
  Integrate before inventing; pull from real history and mythology; change
  whatever you like provided the change is cooler than the truth.
- **27 Aug 2026** — §1b/§1c: recovered the comedic register and the Douglas
  Adams thread, which I dropped when first writing this bible — the exact
  failure this document exists to prevent, committed inside it. Adams's real
  subject (cosmic scale meeting petty procedure) turns out to be the thesis at
  another temperature, so the comedy and the weight share a target.
- **27 Aug 2026 — the physics landed and it unified the setting.** Dan:
  *"we are blending einstein and tesla with modern rqm physics and adding a
  healthy amount of magical reality and literature"*, plus *"project 42 does
  time travel per einstein and that has consequences."*
  - Einstein supplies the geometry, Tesla the coupling and the power, and
    relational quantum mechanics what it does to observers. The RQM anachronism
    is deliberate: a 1944 holding an idea from 1996 IS the alternate history,
    expressed as physics rather than as a change of government.
  - Self-consistency added as **the Consistency Finding**. Project 42 cannot
    change what happened; it can only ever have already been part of it. This
    answers the question the setting could not otherwise survive — if the Allies
    have time travel in 1944, why is the horror still happening — and it yields
    the darkest thing in the game: they can only retrieve people whose absence
    the surviving record already accommodates. Real constraint and convenient
    excuse at once, and nobody, including the people signing the form, can tell
    which is doing the work. Never resolve it.
  - The three factions became one discovery approached unequally. P42 built it;
    Hyakki Yakō was contacted by something native to relational facts, which
    turns "it is always watching" into ontology rather than surveillance; Werk
    Nachtigall is locked out of both and brute-forces with bodies what the
    others get elegantly. **Rule 4 is now dramatic motivation rather than an
    imposed restriction** — the Germans get no magic because they could not get
    any, and it makes them worse.
  - Borges noted as live period texture: *Tlön* (1940) and *Forking Paths*
    (1941) both exist by 1944 and characters can have read them.
- **27 Aug 2026 — the memorial layer was cut.** I had read "never forget" as a
  brief and specified an Archive with citation tiers and commissioning tables.
  Dan: *"we don't need the memorial plane or anything like that. but my point is
  that we are exploring the 1940's and leaning into the horror."* Over-built, and
  removed. §0a is now a sensibility rather than a feature: the remembering
  happens by getting the period right, and a game that attaches a lecture has
  usually given up on the fiction doing the work.
- **27 Aug 2026 — an earlier revision, partly superseded above.** Dan gave the project its actual
  purpose: *"a fundamental philosophy is never forget, and the young generations
  are forgetting."* Plus *"use real names"* and *"in this world nazis did not
  exist. the same bad things basically happened, just differently."*
  - §0a added. Rule 9 reversed — it had said real victims' names are never used,
    which I wrote believing it protective. It was not: refusing to say a name
    completes the erasure the perpetrators intended.
  - §0b added: the Archive, the memorial layer, specified but not built.
  - Two-layer architecture settled. The Archive is OUR history with real names;
    the game is the alternate one with invented names. They never trade places.
  - The in-world atrocity is named **die Ostordnung**, a loremaster call.
  - Rules 1, 2, 3 and 9 rewritten against all of the above.
- **Closed 27 Aug 2026.** The Archive was cut by Dan the same day it was
  specified. §0a is carried by the fiction getting the period right, not by a
  memorial annexe.
- **Open:** art generation is still pending GPU capacity. See ART-SPEC.md.
- **Open:** the card pool has zero cards referencing 42 and no comedic
  register in its flavour banks. §0 and §1b are established and unexecuted.
- **27 Aug 2026 — Mississippi vs Missouri, settled, no text changed.** Raised
  as an open question across at least two sessions after an earlier transcript
  had Dan say "missouri." The bible already said Mississippi throughout (§5,
  Camp Iron Bell) and was right. Asked directly. Dan: *"i don't care.
  mississippi, it's easier to spell."* Recorded so the next fork that finds
  the earlier "missouri" turn does not reopen this.
