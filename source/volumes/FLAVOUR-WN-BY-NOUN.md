# WN NOUN-KEYED FLAVOUR — TIER 1

Paste-ready for `WN_FLAVOR_BY_NOUN` in `card_generator.gd`. Keys are the exact
lowercase strings from `WN_NOUNS_BY_BRANCH`.

Every line is **about the specific creature**, and every line is a first half —
a tier-2 general line follows it, so none of these should close a thought.

Registers mix deliberately: some lines are the Office's paperwork, some are the
troops'. That contrast is the two-name rule doing its work inside the prose.

```gdscript
const WN_FLAVOR_BY_NOUN := {
# ---- KADAVER ----
"students": [
	"Training stock. The Office does mean students; they are what surgeons learn on.",
	"Unfinished, and issued anyway, because the quarter closed.",
	"Every join on it was somebody's first.",
	"The theatre log lists four names against it and three of them are instructors.",
	"It was practice. It is in the field now, which was not the plan.",
	"Section VI queried whether training stock should be drawn against establishment.",
],
"the tidy": [
	"An early model, made beautifully, which the Office regards as a fault.",
	"Every join is flush. Nothing since has been.",
	"It cost four times projection and the Office has never repeated the mistake.",
	"Fragile, and lovely, and the file calls it an over-refinement.",
	"Whoever built this cared, and was reassigned.",
	"The Office learned from it that care does not scale.",
],
"patients": [
	"It moves the way a man moves down a hospital corridor.",
	"You will see it coming. That is not the comfort it sounds like.",
	"Post-operative, ambulatory, cleared for issue.",
	"The mountings cannot be hurried; a fast movement would tear them out.",
	"Nine times opened and closed, and the file counts every one.",
	"It has time. That is most of what it has.",
],
"seconds": [
	"Rebuilt after failure. The line item reads reissue.",
	"Seconds the way you say seconds of a meal, and the way you say a second-quality item.",
	"Whatever failed the first time was not written down.",
	"Cheaper than a new one, which settled it.",
	"The second build used a different surgeon and it shows.",
	"Approved for reissue pending nothing in particular.",
],
"thirds": [
	"Rebuilt twice. There is no fourth, and the reason is in a footnote.",
	"Three sets of handwriting on one file.",
	"Section VI has asked whether it remains the same establishment entry.",
	"The Office does not know what to call this and has settled on thirds.",
	"Each rebuild was approved on the strength of the last one working.",
	"Nobody has read the footnote.",
],
"orderlies": [
	"They carry and repair the others, which is what an orderly does.",
	"Built to maintain the establishment rather than to meet you.",
	"It will step over you to reach something it is responsible for.",
	"The only ones with tools instead of the other thing.",
	"Its priorities are written down and you are not on the list.",
	"Attends to its own before it attends to anything else.",
],
"long shifts": [
	"An endurance model. It does not stop and was not built able to.",
	"There is no off. There is a fuel figure and a projection.",
	"Designed against a duty cycle nobody expected to be tested.",
	"It has been walking since a date on a form.",
	"The estimate assumed relief that was never scheduled.",
	"Whatever it was, it has been doing this longer than you have been here.",
],
"consultants": [
	"Rare, and it directs the others. The Office's word is consulting unit.",
	"It does not close with you. It arranges for that.",
	"Somebody expensive decided this one should think.",
	"Where it goes, the establishment goes, and it goes first.",
	"The joke and the paperwork agree again, which nobody enjoys.",
	"Held at sector level and released against request.",
],
# ---- BESTIARIUM ----
"the litter": [
	"Kennel stock. It improves as the kennel is consumed.",
	"They are no longer fed meat. They are fed each other.",
	"The cost variance is favourable and Accounts has noted it approvingly.",
	"By spring what is standing is worth ten of what you started with.",
	"The men detailed to that duty do not re-enlist for it.",
	"Nobody says much about these.",
],
"the kennel": [
	"Not one of them. The mass, moving as an establishment.",
	"You do not fight this. You are somewhere it has not reached yet.",
	"Counted by weight rather than by head.",
	"The feed returns for this line have never reconciled.",
	"A single entry on the form covers all of it.",
	"Inspected annually by a veterinary officer with no clearance.",
],
"muzzles": [
	"Named for the equipment, because the men will not name the animal.",
	"Handled stock. Somebody fits these by hand, every morning.",
	"Four hundred were requisitioned. Two hundred were approved.",
	"The remainder is held pending clarification of a discrepancy.",
	"You can hear the fittings before you can hear anything else.",
	"Whoever buckles these has a schedule.",
],
"whistlers": [
	"They answer a whistle. Somewhere behind them a man is blowing.",
	"It is not hunting you. It was sent.",
	"The whistle arrives first. That is the only warning in the arrangement.",
	"They do not decide anything, which is worse than if they did.",
	"Intelligence confirmed this months after the infantry worked it out.",
	"Fast, low, and entirely obedient.",
],
"night whistlers": [
	"The same, worked in dark, and the whistle carries further than you would like.",
	"You will hear where it is going before you see it is gone.",
	"Issued against a night establishment that was approved without comment.",
	"The dark does not slow them and was never expected to.",
	"Somebody is out there with a whistle and a schedule.",
	"The lead time is shorter at night and nobody has explained why.",
],
"coursers": [
	"A faster line. It fails more often, which the estimate accepted.",
	"Built for speed against a projection rather than against a man.",
	"Still slower than a running man, and the Office knows.",
	"Attrition on this line is entered as an input.",
	"They were promised as the answer to something.",
	"Fast enough to matter and not fast enough to have been worth it.",
],
"walkers": [
	"Heavy, slow, and it fails in cold, which the estimate did not model.",
	"A decade of appropriations purchased this.",
	"The occupant cannot get out unassisted, and that is on the form.",
	"Recovery has been costed twice and declined twice.",
	"It walks worse than a man and continues to be funded.",
	"Section VI has queried whether the occupant is present or equipment in the field.",
],
"sitters": [
	"A walker that has stopped. The man is still inside.",
	"Entered on the establishment as present, at grid reference appended.",
	"It is an obstacle with an occupant.",
	"Nobody is coming for it and the file says so in three places.",
	"Funny from a distance. Not from the other one.",
	"Its disposition remains held pending guidance before the next return.",
],
# ---- SEUCHE ----
"starters": [
	"Culture stock. The Office means it exactly as a baker would.",
	"Held warm, and drawn against as required.",
	"Filed under agricultural research, which Accounts finds adequate to purpose.",
	"Everything downstream of this began in a tray.",
	"The vocabulary follows the filing and the filing was a budget decision.",
	"Kept alive on a schedule somebody signs for.",
],
"bakers": [
	"It does not charge. It occupies.",
	"Ground you crossed ten minutes ago is not available now.",
	"Warm, and yeasty, and entirely wrong.",
	"There was no moment at which the room changed.",
	"The men were told the smell was the bakery. There is a bakery.",
	"Not a duel. A negotiation with a floor plan.",
],
"early shift": [
	"Sent ahead to make ground unusable before anything arrives to use it.",
	"First wave, and the wave is not the point.",
	"It is not there to meet you. It is there before you.",
	"Scheduled against an advance somebody else is making.",
	"By the time it matters, it has already finished.",
	"Released early against the current quarter.",
],
"proofing": [
	"Held stock, not yet issued. Warehoused, and warm.",
	"Waiting on a release that Section VI has not signed.",
	"Ready, in the sense the form means ready.",
	"Nothing about this is idle. It is simply not yet approved.",
	"The Office is confident about the yield and has said so in an abstract.",
	"Kept at temperature until required.",
],
"the risen": [
	"Risen as dough rises. The Office has been clear about this in writing.",
	"Staff are reminded the term carries its ordinary baking sense.",
	"Enemy troops use the word differently and the Office has no objection.",
	"Correct terminology, per an internal note nobody enjoyed writing.",
	"It came up. That is all the word means and all it has ever meant.",
	"The vocabulary is agricultural because the filing is agricultural.",
],
"the quiet ones": [
	"No bread smell. That is how you know it is a six.",
	"Late stage. Nothing left that belonged to whoever this was.",
	"The men who learned to tell them apart learned it the hard way.",
	"It is in no manual and it is passed on anyway.",
	"You will notice what is missing before you notice what is there.",
	"Fully driven, and performing to projection.",
],
"the very quiet": [
	"Further along. Nobody has established whether there is a limit.",
	"The Office has stopped taking measurements on this line.",
	"Whatever the scale was, this is off the end of it.",
	"No smell, no sound, and no entry in the current abstract.",
	"Attrition on this stage is not reported separately.",
	"It has been like this for some time.",
],
"spoilage": [
	"Accounts' word, and the men picked it up.",
	"Not a designation. A category for anything that stops performing to projection.",
	"Written off against the quarter.",
	"The word covers a great deal and is not asked to be specific.",
	"It appears in the abstract as a figure and nowhere else.",
	"Entered, closed, and drawn against next year's estimate.",
],
}
```

**144 lines, 24 nouns, six each.** Extend rather than replace — add lines to a
noun's list and coverage rises without any structural change.
