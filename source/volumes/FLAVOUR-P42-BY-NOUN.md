# P42 NOUN-KEYED FLAVOUR — TIER 1

Paste-ready for `P42_FLAVOR_BY_NOUN`. Keys are the exact lowercase strings from
`P42_NOUNS`.

Register per Volume IX: **cheerful, form-numbered, institutionally unable to tell
the truth about cost.** The horror is never in the sentence; it is in what the
sentence is about. Every line is a first half.

Draws on Volume III throughout — the hum, Cabinet Nine, Frame Two under its tarp,
Prentiss, the milk cooler, the mess hall that does not hum.

**A note on the joke nouns.** *Filing Golem, Overtime Specter, Requisition Ghost,
Bureaucrat-Prime* are **camp humour, not literal beings.** Iron Bell names its
own absurdities the way any institution does. Never write them as supernatural —
P42 has technology that should not work, not ghosts. The joke is that the
paperwork feels haunted, which is a thing every soldier in every army has
believed.

```gdscript
const P42_FLAVOR_BY_NOUN := {
"field agent": [
	"Deployed and recovered, which is a different form from retrieved.",
	"Went out on a Tuesday against a window the Line Shed set.",
	"Nobody at the far end knows they are coming and nobody will help.",
	"Two or three people. Mass costs energy and the estimate is unforgiving.",
	"Cleared to Item 4 usage at their discretion. Discretion was the word they gave him.",
	"Came back. The form has a box for that and no box for the rest.",
],
"splice technician": [
	"Signs for what goes in and does not sign for what comes out.",
	"Trained on Frame One, which has never moved anything living.",
	"Knows the noise from inside the building, which is the part they teach.",
	"Holds the buckets. Somebody has to and it is always the same detail.",
	"Nine to forty minutes, and the waiting is what nobody warns you about.",
	"Has seen every arrival and has never described one in writing.",
],
"current warden": [
	"Reads a live wire the way other people read weather.",
	"Holds the load across a chain of people without killing any of them.",
	"The report calls it unauthorised use of personnel as conductive medium.",
	"One commendation and one court-martial, the same afternoon.",
	"The camp browns out three towns and a man three miles east loses his milk.",
	"Never fired a shot. The line broke anyway.",
],
"phase runner": [
	"Not invisible. A fact for fewer of the people present.",
	"The files use the word attenuation and do not define it.",
	"Has begun sitting nearer to doors, and could not tell you why.",
	"People stop noticing him in rooms and then apologise when he speaks.",
	"There is no floor to this and the tables do not say so.",
	"3-C, satisfactory. Minor coherence variance. No action indicated.",
],
"chrono clerk": [
	"Files the 42-D and initials the box and goes to lunch.",
	"Is the subject's absence consistent with the surviving record? One box.",
	"The whole programme turns on half a page and he keeps it in a folder.",
	"Has never asked what happens if the answer is no.",
	"Knows which people history was careless with, professionally.",
	"The list is short and he is the one who keeps it short.",
],
"capacitor corps": [
	"Stores what the Line Shed cannot spend fast enough.",
	"Half-deaf and unusually calm, like everyone on that detail.",
	"Smells of hot varnish and ozone, permanently, including on leave.",
	"The only building with a fire watch around the clock.",
	"Charged against a projection somebody signed in triplicate.",
	"When the hum drops, they already know.",
],
"arc welder": [
	"Runs on borrowed current and a requisition that came back approved in part.",
	"Rated for a duty cycle nobody has ever respected.",
	"Built from the drawings, which were correct, which did not help.",
	"The Line Shed lends it out and expects it back in that condition.",
	"Somebody wrote a manual for this after the fact.",
	"Works. Nobody has asked it to explain how.",
],
"static grenadier": [
	"Carries what the Line Shed could not safely store.",
	"Every item on his person is on somebody's inventory.",
	"The safety review is scheduled for March and it is January.",
	"Approved for field use pending the thing that has not happened yet.",
	"Discharges once and is then a man carrying an empty frame.",
	"Nobody stands close on purpose and nobody has said so.",
],
"vector corporal": [
	"Reads a room the way Pike reads a shell, and has been asked to explain it.",
	"Promoted for something the citation describes as initiative.",
	"Between a promotion and a punishment, and the paperwork is silent on which.",
	"Has been right often enough that nobody enjoys it.",
	"Knows where a thing will be before it is there.",
	"The file records the outcome and not the method.",
],
"feedback loop": [
	"Answers a question that was never officially asked.",
	"Whatever it does, it does again, which the estimate did not model.",
	"Somebody has drawn a diagram of this and the diagram bites its own tail.",
	"The manual says do not, and does not say why.",
	"Approved on the strength of the last one working.",
	"Runs until told otherwise. Nobody has been told to tell it.",
],
"paradox auditor": [
	"Checks the closure and files whether it closed.",
	"There is no branching. There is no second draft. He audits that.",
	"Whatever was done had always already been done and he confirms it.",
	"The Consistency Finding is his whole job and he calls it the Finding.",
	"Has never found an inconsistency, which is either the system working or nothing.",
	"Signs off on a loop that was closed before he looked.",
],
"fuse sergeant": [
	"Between the Line Shed and everything the Line Shed could ruin.",
	"Replaces what fails, and keeps a count nobody has asked for.",
	"Has a name for the tinnitus that is not in any manual.",
	"The hum dropping is his cue and it is the only one he needs.",
	"Signed for the bus that fed Frame Two. Has not stopped signing things.",
	"Would rather it blew here than there.",
],
"grounding crew": [
	"Gives the current somewhere to go that is not a person.",
	"Works nights because the retrievals are at night.",
	"The ballfield is the only ground flat enough and it is still called that.",
	"Copper into Mississippi clay, and the clay does not always take it.",
	"Nobody thanks this detail and the detail has noticed.",
	"When it works, nothing happens, which is the problem with the job.",
],
"wavefront scout": [
	"Goes first, which is a sentence the form does not elaborate on.",
	"Reports what the air is doing before the air does it.",
	"Describes it as swimming, or as being spoken to in a language he nearly knows.",
	"Every log says the same thing and no report has ever remarked on it.",
	"Out ahead of the closure, on his own, against a window.",
	"Came back early once and would not say why.",
],
"bureaucrat-prime": [
	"A joke the camp made about a person who does not exist and then kept.",
	"Everything at Iron Bell passes through one desk and it is not the Colonel's.",
	"No clearance. Never asked. Has predicted eleven outcomes from paperwork alone.",
	"Takes a fortnight in July and the camp does not run.",
	"The programme staggered the July retrievals rather than examine why.",
	"Decides what reaches him and in what order, which is the same as deciding.",
],
"filing golem": [
	"Camp humour. Nobody believes it and everybody says it.",
	"Made of forms, in the sense that a man is made of the things he signs.",
	"It is not haunted. It is just very long, and it is Tuesday.",
	"Three signatures, one of them the Colonel's, and a fourth that got added later.",
	"Grew by accretion and nobody can say which memo started it.",
	"You cannot kill it because there is no disposition form.",
],
"overtime specter": [
	"A joke, and the joke is that nobody has gone home.",
	"The mess hall does not hum and men sit in it at eleven at night.",
	"Not talking. For the quiet. Nobody has ever said that out loud.",
	"The cooks know and put the urn on.",
	"Scheduled against a relief that was never scheduled.",
	"Has been here longer than the establishment it is drawn against.",
],
"requisition ghost": [
	"A request that will not die, and Cabinet Nine is full of its relatives.",
	"Filed in nine, which is what the camp says about anything that will not happen.",
	"Denied twice, resubmitted twice, denied on different grounds each time.",
	"Somebody keeps every one of these. Says it is for the memoir.",
	"Command suspects it is a battery.",
	"There is a drawer, and people know which drawer.",
],
"answer-seeker": [
	"The answer is known. Nobody has the question.",
	"Camp Iron Bell was drawn from a list that was generated to be meaningless.",
	"There is a standing bet on what it stands for, now four hundred dollars.",
	"Nobody at the War Department can settle it, which is the only joke they ever landed.",
	"Asks the thing everyone has agreed not to ask, in a form nobody can file.",
	"The asking is the problem. Never the answer.",
],
"number cruncher": [
	"Works out what a night costs and is told to work it out again.",
	"The cost line would be recognised by an accountant in another country.",
	"Three towns, one night, and eleven dollars of somebody's milk.",
	"Nineteen, ever. That is the whole programme and it fits on a card.",
	"Rated capacity is not a hundred percent of anything.",
	"Has never been asked for the figure that matters.",
],
"ledger sentinel": [
	"Guards a record rather than a place, which he would say is the same thing.",
	"Two of the letters are in the file. Two are not.",
	"Nobody knows where they went and that is what keeps the Major awake.",
	"The file is complete. The thing it describes is elsewhere.",
	"Adequate to purpose, in the phrase that gets read.",
	"What is not in the file is also his responsibility and nobody has told him.",
],
"circuit monk": [
	"Learned the apparatus by ear because nobody understands the notes.",
	"They are running on theory from a man who died owing money.",
	"The papers arrived inside a fortnight and nobody asks how.",
	"Will say plainly what everyone else will not: we do not know why this works.",
	"Unhurried in a way that reads as faith and is actually experience.",
	"Frame Three works. Frame Four is identical and has never closed a retrieval.",
],
"induction coilman": [
	"Copper, oil, and a resonance somebody found rather than designed.",
	"The oil note climbs a fifth and that is the whole warning system.",
	"Rewound it twice from the same drawings and got two different machines.",
	"Nobody says the obvious thing about the one that already worked.",
	"Aloud it sounds like superstition. Quietly it sounds like physics.",
	"He has stopped saying it aloud.",
],
"departure clerk": [
	"Handles the ones going out, which is a shorter form than the ones coming in.",
	"Retrieval is one-way. Deployment is not. The distinction is his whole desk.",
	"Settlement is the word Washington chose. He uses it. They use it differently.",
	"Issues one helmet, one rifle, and a century.",
	"Has never once been thanked and has stopped noticing.",
	"Signs them out against a window and waits.",
],
"standing order": [
	"Written once, by somebody reassigned, and it has outlasted the committee.",
	"Nobody can rescind it because nobody can find who issued it.",
	"It has been in force since a date on a form.",
	"Two men asked about it and their files say reassigned.",
	"Everyone obeys it and nobody has read it in eighteen months.",
	"Still pending, somewhere, in the way these things are.",
],
}
```

**150 lines, 25 nouns, six each.** Extend rather than replace.
