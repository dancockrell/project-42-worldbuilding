# HY NOUN-KEYED FLAVOUR — TIER 1

Paste-ready for `HY_FLAVOR_BY_NOUN`. Keys are the exact lowercase strings from
`HY_NOUNS`.

---

## Read this before writing or editing a line

**These nouns are people, not products.** A Kitsune-Warden is a person with
kitsune folklore fused onto them by something that did not ask. Werk
Nachtigall's bank describes manufactured things; **this bank describes what
happened to somebody.**

Four rules, all from LORE-BIBLE.md §5 and its guard:

1. **Dispossession, never frenzy.** Write stillness. A fused soldier does
   terrible things and does not own the hands doing them, and afterwards is calm,
   and the calm is the horror. Never fanatical, never raving, never ecstatic —
   that is the caricature Allied propaganda manufactured industrially in this
   exact period, and we work in that period's visual idiom, so the risk is live.
2. **The watching is constant, quiet, and never intensifies.** No stings. It is
   frightening in retrospect, at three in the morning, when you notice you have
   stopped minding.
3. **The programme's paperwork lies to itself** the way the Office's does — the
   treaty nothing signed, the ceremony that may do nothing. That is where the
   institutional comedy lives. **Never at the expense of the fused.**
4. **It does not excuse the Empire.** Unit 731 remains the referent. Both true at
   once, neither resolving.

**Test:** if a line would read worse coming from a 1943 US War Department poster,
it is the wrong line.

```gdscript
const HY_FLAVOR_BY_NOUN := {
"kitsune-warden": [
	"The fusion chose. Nobody has established what it chose for.",
	"She was a railway clerk in March and she is this in April.",
	"Nothing in her record suggested it. Nothing in anyone's record does.",
	"The programme maintains that terms were agreed.",
	"She has stopped explaining and the file records that as compliance.",
	"Serene, which is wrong for what is happening around her, and that is the tell.",
],
"oni-drummer": [
	"He does not remember agreeing to the drum.",
	"There is a gap the shape of a held breath and he cannot fill it in.",
	"Something is keeping time with him from a direction he cannot point at.",
	"He knows which rhythm makes his friends fight harder.",
	"And which one means there will not be enough of him left afterward.",
	"The only choice the fusion permits is when it ends.",
],
"miko-sentinel": [
	"The ceremony was performed correctly. This appears not to have mattered.",
	"She officiates for people who were chosen before she began.",
	"Fusions have happened without the rite and failed with it.",
	"The programme continues it in full, every time, for reasons that are not belief.",
	"Stopping would be an admission and the admission is not available.",
	"She has never said this aloud and has thought it in every ceremony since June.",
],
"yokai-tender": [
	"Assigned to the fused, which is a posting nobody requested.",
	"Not a doctor. There is no medicine for this and the establishment lists him anyway.",
	"He can tell who else has it. They leave each other alone.",
	"Keeps notes the programme has not asked for and would not know how to file.",
	"The long-term effects are unknown. That is the official position and it is true.",
	"He has begun to suspect the notes are for nobody.",
],
"shrine-keeper": [
	"Keeps a building the programme cannot say is load-bearing or decorative.",
	"The treaty is in the third cabinet. Nine articles, beautifully drafted.",
	"Written in our hand, on our paper, and nothing signed the other side.",
	"Somebody drafted terms they hoped had been agreed and filed them officially.",
	"He dusts it. That is the entire ritual and he is aware of that.",
	"It has never read the treaty. He does not think it files things.",
],
"fog-walker": [
	"Concealment that is not hiding. A fact for fewer of the people present.",
	"The patrol was there and then was half-erased, and nobody heard anything.",
	"She does not know how she does it and has stopped being asked.",
	"The road stops. So does she, and then she is elsewhere.",
	"Lanterns in mist, and one of them is not carried by anyone.",
	"Nothing about this is stealth. Stealth would require someone to be looking.",
],
"nue-kin": [
	"Fused with something the folklore describes in four incompatible ways.",
	"The programme's file uses the folklore's word because it has no word of its own.",
	"Whatever came in did not consult the taxonomy.",
	"He is not a chimera. He is a man, and it is using him.",
	"The record calls it a successful fusion and defines neither term.",
	"Nobody has asked him what it feels like. The form has no box.",
],
"tengu-scout": [
	"Sees further than the eye should and files reports nobody can corroborate.",
	"Every one has been correct. That is not the same as trusted.",
	"Chosen while carrying water, according to the only account that exists.",
	"He does not fly. The folklore says otherwise and the folklore is not a manual.",
	"The programme sends him ahead because it can, not because it understands.",
	"He has never once been surprised by what he found, and that frightens him.",
],
"onibi-carrier": [
	"Carries a light that is not fuel and cannot be extinguished on request.",
	"The quartermaster has no line for this and has invented one.",
	"It does not warm anything. It has been measured.",
	"Filed under equipment, because the alternative filing needs a signature.",
	"He sleeps with it and does not say whether he sleeps.",
	"It goes where he goes. Nobody has tested whether that is his choice.",
],
"yurei-bound": [
	"Bound is the programme's word and it does not elaborate.",
	"Something was left unfinished and it was not hers.",
	"She is not a ghost. She is a woman with an obligation she did not incur.",
	"The folklore has a shape for this and the shape is not comforting.",
	"The record says she volunteered. The record says that about everyone.",
	"She is calm about it, which is the part that reads wrong.",
],
"kappa-diver": [
	"Works the water because that is what the fusion made available.",
	"Down longer than a man can be down and back without ceremony.",
	"The programme has costed the capability and not the person.",
	"He was a fisherman. He is a fisherman. Both of those are true differently now.",
	"The report notes an operational advantage and appends nothing else.",
	"He does not like the water any more and has told no one.",
],
"tanuki-trickster": [
	"The one genuinely funny fusion, and the programme finds it embarrassing.",
	"Filed under an operational category invented specifically to contain him.",
	"Nothing he does is regulation. Everything he does works.",
	"Amatsu has declined to discipline him twice, in writing, without stating why.",
	"He makes the others laugh, which the establishment does not track.",
	"He is the only one who talks about it. Nobody has told him to stop.",
],
"inugami-handler": [
	"Handles what the folklore says should be handling him.",
	"The relationship is not in either direction the file assumes.",
	"He gave something up for this and the record does not say what.",
	"Loyalty is the word the report uses, about a thing that did not consent either.",
	"They understand each other and neither chose to.",
	"He has asked for a transfer three times and given a different reason each time.",
],
"amanojaku-whisper": [
	"Says the opposite of what is wanted, and is right often enough to keep.",
	"The programme has decided this is a capability rather than a problem.",
	"Contradicts orders and the contradictions have been correct eleven times.",
	"Nobody has worked out whether he chooses this.",
	"The folklore says perverse. The file says consultative.",
	"He would like to agree with someone once and has not managed it.",
],
"zashiki-warashi": [
	"Attached to a place rather than a unit, which the establishment cannot express.",
	"Where she is, things go well. The programme has measured this and does not print it.",
	"She is very young and nobody will say the number.",
	"The rite was performed on someone who did not understand it.",
	"If she leaves, the file predicts an outcome and does not name it.",
	"Nobody has asked her whether she wants to stay.",
],
"nekomata-claw": [
	"Twice-lived, in the folklore's sense, which the programme records literally.",
	"Whatever was ended did not take, and the file is silent on the attempt.",
	"She is patient in a way the others are not, and it is not calm.",
	"The fusion took to her faster than to anyone before or since.",
	"No explanation was offered and none was requested.",
	"She has outlasted three officers who wrote about her.",
],
"ittan-momen": [
	"Length of cloth, in the folklore. A man, in the establishment.",
	"Moves in a way the eye reports and the mind declines to accept.",
	"The programme has filmed this twice and reviewed the film once.",
	"Silent, which was not true of him before.",
	"His weight is recorded as unchanged and this has been queried.",
	"Somebody wrote unremarkable in the margin and initialled it.",
],
"rokurokubi-watch": [
	"Keeps watch, and the folklore's joke about how is not made here.",
	"Awake for the whole night, every night, since the fusion.",
	"He has not reported being tired and Falk's opposite number has stopped asking.",
	"Sees what approaches before it approaches and cannot say from where.",
	"The programme calls this an early-warning function.",
	"He would like to sleep. This is in a letter that was never sent.",
],
"karakasa-sentry": [
	"One of the small folklore, fused onto somebody who wanted the large.",
	"He volunteered for something and received something else.",
	"The unchosen stay, and he is nearly one of them, and is not.",
	"There is no ceremony for a disappointing fusion and one was held anyway.",
	"He guards a door. It is genuinely useful and that is the humiliation.",
	"Nobody has ever explained the selection to anybody.",
],
"bakeneko-familiar": [
	"Something in it counts differently than it used to.",
	"Attached to a person who did not request the attachment.",
	"The programme lists them as one entry, which neither of them agreed to.",
	"It does not obey. It accompanies, which is worse to write a report about.",
	"He talks to it. The file records this without comment.",
	"Whatever it is, it was not there in February.",
],
"hitodama-bearer": [
	"Carries what the folklore says leaves a person at the end.",
	"The programme has not asked whose.",
	"It is warm. That is the only measurement anyone has taken.",
	"He does not put it down and has not been ordered to.",
	"Filed under an equipment category with one entry.",
	"The quartermaster has stopped coming to that part of the establishment.",
],
"shinigami-adjacent": [
	"Adjacent is the programme's word and it was chosen carefully.",
	"Present at more endings than the roster accounts for.",
	"Nobody has suggested he causes them. Nobody has ruled it out either.",
	"He arrives slightly before he is needed and this is in every log.",
	"The men do not avoid him. They arrange not to be near.",
	"He knows, and has never mentioned it to anyone.",
],
"kodama-warden": [
	"Fused with something that belonged to a place, and the place is gone.",
	"The grove was cleared in 1939 for the works.",
	"Nobody connected the two facts until a clerk did, and the note was filed.",
	"He is quiet in a way that predates all of this.",
	"The programme has not returned him and has not been asked to.",
	"He would like to see the ground. That request is in nine.",
],
"gaki-fed": [
	"The hungriest folklore, fused onto a man in a supply unit.",
	"The programme has queried his rations three times and approved them three times.",
	"Nothing is enough. This is recorded as a medical observation.",
	"He is embarrassed, which is the detail nobody expected.",
	"Accounts has noticed and Accounts is not the department for this.",
	"He eats alone now. Nobody asked him to.",
],
"jorogumo-weave": [
	"Patient work, and the folklore's implication is not the programme's.",
	"She was a weaver. The fusion appears to have known that.",
	"That is the only case where selection matched a life, and it proves nothing.",
	"One data point, and the programme has built a theory on it anyway.",
	"The theory is in a paper nobody outside the programme will read.",
	"She has never been asked whether the match felt like recognition.",
],
}
```

**150 lines, 25 nouns, six each.** Extend rather than replace, and re-read the
guard above before adding any.
