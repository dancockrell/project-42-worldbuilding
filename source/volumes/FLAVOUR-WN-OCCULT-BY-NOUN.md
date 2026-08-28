# WN OCCULT NOUN-KEYED FLAVOUR — TIER 1 ADDITION

Paste-ready for `WN_FLAVOR_OCCULT_BY_NOUN` in `card_generator.gd`. Keys are
the exact lowercase strings from `WN_NOUNS_BY_BRANCH` -- same 24 nouns as
`WN_FLAVOR_BY_NOUN`, same case, checked against it line by line before
delivery.

**Written under bible §2 rule 4, reversed 28 Aug 2026: Werk Nachtigall gets
the occult.** Every line below stays inside the Constitution regardless:
rules 1-3 and 9 are untouched, no real atrocity is ever given a supernatural
cause, and the register stays the Office's own -- flat, procedural, faintly
irritated. Rule 10 governs: menace is supplied by the reader, never played
as awe or reverence. A séance and a surgical theatre get the same tone.

**This is an addition, not a replacement.** `WN_FLAVOR_BY_NOUN` (the
material-only tier-1 bank) stays live and mixes with this one -- the two
registers coexisting on the same noun is the point: Section Six files a
summoning circle exactly like a feed return, and a card should be able to
draw either line and land in the same faction.

**One entry in the original bank is now wrong and needs fixing at the same
time this lands:** `"the risen"` in `WN_FLAVOR_BY_NOUN` still asserts
"Risen as dough rises... that is all the word means and all it has ever
meant" -- flatly false under the reversal (WORLD-BESTIARY.md, Muster 7).
Replacement lines for that entry are included at the end of this file,
to be swapped in-place rather than left contradicting this addition.

```gdscript
const WN_FLAVOR_OCCULT_BY_NOUN := {
# ---- KADAVER ----
"students": [
	"The instructor draws a second diagram nobody has asked about, in a different ink.",
	"Trained on the table and, twice now, told what the table remembers.",
	"The occult section calls this stock receptive. Nobody has asked to what.",
],
"the tidy": [
	"Made too well for a body and, the file notes without elaborating, for anything else present at the time.",
	"The consulting priest signed the same requisition as the surgeon and neither struck the other's line.",
	"Whoever built this cared, in more than one discipline, and was reassigned regardless.",
],
"patients": [
	"The chalk marks under the table are not the surgeon's. Nobody has asked whose they are.",
	"It moves like a man down a corridor, and something was asked to make sure of that.",
	"Kadaver's rite is short, administrative, and performed before the first incision, not instead of one.",
],
"seconds": [
	"Rebuilt after failure, and the second build kept something the first one lost track of.",
	"The line item reads reissue. The margin, in a different hand, reads returned.",
	"Whatever failed the first time is written down now, in the other book.",
],
"thirds": [
	"Three sets of handwriting on the file, and the third is not medical.",
	"Rebuilt twice, and the second rebuild required a rite the first one did not.",
	"The footnote nobody has read is not about the surgery.",
],
"orderlies": [
	"It carries and repairs the others, and does not ask why one of them was cold this morning and is not now.",
	"Built to maintain the establishment. Which establishment was never fully specified.",
	"Attends to its own first, and its own now includes a directorate it was not issued to know about.",
],
"long shifts": [
	"It has not stopped, and the occult section has stopped asking it to.",
	"There is no off, per the estimate. There was never meant to be a why.",
	"Whatever kept it walking outlasted the surgeon who signed for it.",
],
"consultants": [
	"Rare, and it directs the others, and the consultation this time was not medical.",
	"The Office's word is consulting unit. The word is doing more work than usual.",
	"Held at sector level. The requisition that released it has a second signature nobody will name.",
],
# ---- BESTIARIUM ----
"the litter": [
	"They are no longer fed meat. What feeds them now was drawn up by two departments, not one.",
	"The kennel improves as the kennel is consumed, and the occult section has taken an interest in the mechanism, not the ethics.",
	"Whatever is standing by spring was not entirely bred.",
],
"the kennel": [
	"Counted by weight. Something in the count has started moving before it is touched.",
	"A single entry on the form covers all of it, and the form has a line nobody expected a kennel to need.",
	"The mass moves together in a way the veterinary officer's form has no box for.",
],
"muzzles": [
	"Named for the equipment, because the men will not name the animal, and lately will not name the smell either.",
	"Handled stock. The handler's manual now has a page the veterinary officer is not cleared to read.",
	"Four hundred requisitioned, two hundred approved, and a note appended by a directorate that does not usually correspond about livestock.",
],
"whistlers": [
	"They answer a whistle, and, on a specific and undocumented occasion, answered something that was not one.",
	"Fast, low, entirely obedient, and obedient to more than the whistle now, per an addendum nobody has explained.",
	"The handler was never shown. Increasingly, nobody is sure there is only the one.",
],
"night whistlers": [
	"The whistle carries further at night, and the occult section's notes say the same thing, in different words, about something else.",
	"Worked in dark on purpose. The purpose is filed separately from the tactical one.",
	"The lead time is shorter at night. Nobody has explained why, and one department could, and has not been asked.",
],
"coursers": [
	"A faster line. It fails more often, and what it fails into is not always still an animal.",
	"Still slower than a running man, and the Office has stopped citing that as a comfort.",
	"Attrition on this line is entered as an input, and lately as two inputs, one of them unspecified.",
],
"walkers": [
	"A decade of appropriations purchased a mecha that walks worse than a man, and a second decade purchased the rite that keeps it walking anyway.",
	"The occupant cannot get out unassisted, and the form now asks a second question about why he has not tried.",
	"Heavy, riveted, oil-fed, and, since the estimate before last, blessed -- Accounts' word, not the priest's.",
],
"sitters": [
	"A walker that has stopped. The man is still inside, and the file has stopped assuming that is only sad.",
	"Entered on the establishment as present. The occult section has queried whether present is still accurate.",
	"Nobody is coming for it, in three places the file says so, and in a fourth, newer place, it says why not.",
],
# ---- SEUCHE ----
"starters": [
	"Culture stock, the Office means it as a baker would, and increasingly cannot promise that is the whole of it.",
	"Held warm, drawn against as required, and the requisition no longer specifies which procedure will draw it.",
	"Everything downstream of this began in a tray. Not everything downstream of this stayed in the category the tray implies.",
],
"bakers": [
	"It does not charge. It occupies, and the occult section has asked whether occupies is doing more work than the Office intended.",
	"Warm and yeasty and entirely wrong, in a way that is now sometimes literal.",
	"Ground you crossed ten minutes ago is not available now, and the return does not say which procedure made it so.",
],
"early shift": [
	"Sent ahead to make ground unusable, and the method of unusable is no longer guaranteed to be biological.",
	"First wave, and the wave is not the point, and which directorate sent it is increasingly not the point either.",
	"Released early against the current quarter, against a requisition with two signatures where one used to be enough.",
],
"proofing": [
	"Held stock, not yet issued, kept warm, and kept is not a word either directorate will define further.",
	"Waiting on a release Section VI has not signed, from a form that no longer says which procedure it authorises.",
	"Ready, in the sense the form means ready, and the form no longer distinguishes cultured from raised.",
],
"the quiet ones": [
	"No bread smell. That used to be how you knew it was a six. It is no longer the only way.",
	"Late stage, and late is doing double duty now: fully driven, or simply no longer needing to eat.",
	"The men who learned to tell these apart from the others have stopped being sure what they are telling apart.",
],
"the very quiet": [
	"Further along, and the Office has stopped measuring, in both senses the word could now carry.",
	"No smell, no sound, no entry in the current abstract, and no reliable answer to which procedure this is.",
	"Whatever the scale was, this is off the end of it, and off which end is the part nobody will say.",
],
"spoilage": [
	"Accounts' word for anything that stops performing to projection, cultured or otherwise.",
	"Written off against the quarter, filed the same way regardless of which directorate produced it.",
	"The word covers a great deal and, since the reversal, covers more than it used to and says less about which half.",
],
}
```

**Replacement for `"the risen"` in `WN_FLAVOR_BY_NOUN`** (swap in place --
the old six lines assert a certainty that no longer holds):

```gdscript
"the risen": [
	"Troops think it means risen from the dead. Increasingly, they are not always wrong.",
	"The Office means it as dough rises. The Office also means it the other way, on a proportion it has not been able to state.",
	"Neither directorate can tell from the establishment return which procedure produced this one.",
	"Correct terminology, per an internal note that used to be confident and no longer is.",
	"The vocabulary is agricultural because the filing is agricultural, which now covers two very different mornings.",
	"It came up. Which of the two ways it came up is the question the Office has stopped asking, on purpose.",
],
```

**69 new occult lines across 23 nouns (3 each) -- "the risen" is deliberately
absent here and handled by the 6-line replacement below instead, 24 nouns'
worth of coverage in total.** Mixes with
`WN_FLAVOR_BY_NOUN` on generation -- both registers should be eligible for
the same card. Extend rather than replace, same as the original bank.
