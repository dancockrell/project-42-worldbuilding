"""Check card prose against the fact each named subject's owning volume states.

Why this exists: today's wiki audit found the single highest-yield defect class
of the day was ATTRIBUTES NOBODY CHOSE -- a sentence needed a rank, a pronoun,
a service, and the unmarked default filled it in, wrong about as often as a
coin. Sixty percent on unnamed-role gender. A naval Petty Officer became an
army Sergeant because the sentence needed a rank. WRITING.md now states the
rule for this project: "the test is not is this plausible, it is did anyone
decide this." This is that test, automated, running BEFORE fifteen hundred
cards exist rather than auditing after.

Method: for each subject in FACTS below, the OWNER volume is the authority
(matching canon-numbers-check.py's shape in the sibling repo). A card is
checked only if it plausibly concerns that subject -- matched by surname,
case-insensitive, appearing in the card file at all. A card that never
mentions a subject is not checked against that subject's facts; that is a
NOT CHECKED outcome for that pairing, not a pass.

Three states, never two, per this machine's own rule: a card can PASS a fact,
FAIL a fact, or be NOT APPLICABLE (subject not present in that card).
"""
import io, os, re, sys

DOCS_ROOT = os.environ.get("DEFAULTS_CARDS_ROOT", "source/cards")

# Each fact: subject surname (for matching which cards apply), the volume that
# owns the fact, a short human name for the attribute, the exact substring
# that must appear in the OWNER (so a moved fact fails loud rather than
# silently checking a superseded one), and the RETIRED forms that must not
# appear in any card touching this subject.
FACTS = [
    {
        "subject": "Aust",
        "owner": "source/volumes/WORLD-HOLLERNBRUCH-DEEP.md",
        "attribute": "Aust's age (44, per the record)",
        "owner_required": "Forty-four. Qualified 1924, Leipzig.",
        "retired": [],  # nothing wrong stated yet; slot proves the pairing works
    },
    {
        "subject": "Aust",
        "owner": "source/volumes/WORLD-HOLLERNBRUCH-DEEP.md",
        "attribute": "Aust's objection count and span (19 objections / 8 years)",
        "owner_required": "She has filed nineteen objections in eight years.",
        "retired": ["twenty objections", "eighteen objections", "nine years",
                    "seven years", "twenty-nine objections"],
    },
    {
        "subject": "Pflug",
        "owner": "source/volumes/WORLD-HOLLERNBRUCH-DEEP.md",
        "attribute": "Pflug's title (Werkmeister, Bestiarium)",
        "owner_required": "Werkmeister Otto Pflug",
        "retired": ["sergeant pflug", "herr pflug", "doctor pflug",
                    "hauptmann pflug"],
    },
    {
        "subject": "Grau",
        "owner": "source/volumes/WORLD-HOLLERNBRUCH-DEEP.md",
        "attribute": "Grau's age (29) and rank (Unterarzt)",
        "owner_required": "Unterarzt Peter Grau",
        "retired": ["doctor grau", "sergeant grau", "captain grau"],
    },
    {
        "subject": "Brehm-Sandt",
        "owner": "source/volumes/WORLD-HOLLERNBRUCH-DEEP.md",
        "attribute": "Brehm-Sandt's title (Oberregierungsrat, Director)",
        "owner_required": "Oberregierungsrat Klaus Brehm-Sandt",
        "retired": ["general brehm-sandt", "colonel brehm-sandt",
                    "herr brehm-sandt"],
    },
]


def cards():
    out = []
    for dp, _, fns in os.walk(DOCS_ROOT):
        for fn in fns:
            if fn.endswith(".md"):
                out.append(os.path.join(dp, fn).replace(os.sep, "/"))
    return sorted(out)


def main():
    all_cards = cards()
    # Floor mirrors canon-numbers-check.py's shape: refuse to certify a run
    # over a suspiciously small or missing corpus rather than print a
    # trivially-true PASS. Set low because this project starts at 3 cards and
    # is meant to run from card zero, not after a large corpus exists.
    if not os.path.isdir(DOCS_ROOT):
        print("NOT CHECKED: %s does not exist. Refusing to report a clean run."
              % DOCS_ROOT)
        return 2
    if len(all_cards) == 0:
        print("NOT CHECKED: 0 card files found under %s. Refusing to report a "
              "clean run." % DOCS_ROOT)
        return 2
    if not FACTS:
        print("NOT CHECKED: no facts configured.")
        return 2

    fails = []
    applicable = 0
    for fact in FACTS:
        owner = fact["owner"]
        if not os.path.exists(owner):
            fails.append("%s: owner volume %s is missing" % (fact["attribute"], owner))
            continue
        osrc = io.open(owner, encoding="utf-8").read()
        if fact["owner_required"] not in osrc:
            fails.append(
                "%s: owner %s no longer states %r -- the fact moved and this "
                "check is now the stale one" % (fact["attribute"], owner, fact["owner_required"]))

        subj_low = fact["subject"].lower()
        for path in all_cards:
            text = io.open(path, encoding="utf-8").read()
            if subj_low not in text.lower():
                continue  # subject not in this card: NOT APPLICABLE, not a pass
            applicable += 1
            low = text.lower()
            for bad in fact["retired"]:
                if bad in low:
                    fails.append("%s: %s carries retired form %r"
                                 % (fact["attribute"], path, bad))

    print("%d facts x %d cards -- %d subject/card pairings applicable"
          % (len(FACTS), len(all_cards), applicable))
    if fails:
        print("FAIL -- %d site(s):" % len(fails))
        for f in fails:
            print("  " + f)
        return 1
    if applicable == 0:
        print("NOT CHECKED: none of the configured subjects appear in any "
              "current card. The check ran; it had nothing to check yet.")
        return 2
    print("PASS -- no retired attributes found on cards mentioning a tracked subject")
    return 0


sys.exit(main())
