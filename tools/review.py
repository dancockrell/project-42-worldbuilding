"""The review board: where every card stands, and who is holding it up.

Reads card headers for `status:` and the verdict files in review/, and prints
one line per card. Its job is to make a stalled card visible -- three accepts
and no fourth looks exactly like nobody having started, unless something says
which.

    python tools/review.py            everything
    python tools/review.py --waiting  only cards that need somebody to act

Exit 0 always. This is a board, not a gate -- a card nobody has judged yet is
the normal state of a queue, not a defect.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "source", "cards")
REVIEW = os.path.join(ROOT, "review")

EDITORS = ["lm2", "lm3", "lm4"]
PRIMARY = "prime2"
NEEDED = len(EDITORS) + 1


def cards():
    out = []
    if not os.path.isdir(CARDS):
        return out
    for faction in sorted(os.listdir(CARDS)):
        d = os.path.join(CARDS, faction)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            text = io.open(os.path.join(d, fn), encoding="utf-8").read()
            st = re.search(r"^status:\s*(\S+)", text, re.M | re.I)
            out.append({
                "slug": fn[:-3],
                "faction": faction,
                "status": (st.group(1).lower() if st else "draft"),
            })
    return out


def verdicts():
    """slug -> {editor: (verdict, round)}. Latest round per editor wins."""
    found = {}
    if not os.path.isdir(REVIEW):
        return found
    for fn in sorted(os.listdir(REVIEW)):
        if not fn.endswith(".md"):
            continue
        text = io.open(os.path.join(REVIEW, fn), encoding="utf-8").read()
        c = re.search(r"^card:\s*(\S+)", text, re.M | re.I)
        e = re.search(r"^editor:\s*(\S+)", text, re.M | re.I)
        v = re.search(r"^verdict:\s*(\S+)", text, re.M | re.I)
        if not (c and e and v):
            print("review: SKIPPED %s - missing card/editor/verdict" % fn)
            continue
        rnd = re.search(r"\.r(\d+)\.md$", fn)
        rnd = int(rnd.group(1)) if rnd else 1
        slug, ed, ver = c.group(1).strip(), e.group(1).strip().lower(), \
            v.group(1).strip().upper()
        prev = found.setdefault(slug, {}).get(ed)
        if prev is None or rnd >= prev[1]:
            found[slug][ed] = (ver, rnd)
    return found


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    only_waiting = "--waiting" in sys.argv
    cs = cards()
    if not cs:
        print("review: no cards in %s" % CARDS)
        return 0
    vs = verdicts()

    counts = {"accepted": 0, "review": 0, "draft": 0, "revise": 0}
    rows = []
    for c in cs:
        v = vs.get(c["slug"], {})
        acc = [e for e in EDITORS + [PRIMARY] if v.get(e, ("", 0))[0] == "ACCEPT"]
        rev = [e for e in EDITORS + [PRIMARY] if v.get(e, ("", 0))[0] == "REVISE"]
        missing = [e for e in EDITORS + [PRIMARY] if e not in v]

        if c["status"] == "accepted":
            state, note = "ACCEPTED", ""
            counts["accepted"] += 1
        elif rev:
            state, note = "REVISE", "rejected by " + ", ".join(rev)
            counts["revise"] += 1
        elif c["status"] != "review":
            state, note = "draft", "not submitted"
            counts["draft"] += 1
        else:
            state = "%d/%d" % (len(acc), NEEDED)
            note = "waiting on " + ", ".join(missing) if missing else \
                "four accepts - primary editor to mark accepted"
            counts["review"] += 1

        waiting = state not in ("ACCEPTED", "draft")
        if only_waiting and not waiting:
            continue
        rows.append("  %-9s %-28s %-9s %s"
                    % (c["faction"], c["slug"], state, note))

    for r in rows:
        print(r)
    print()
    print("review: %d cards - %d accepted, %d in review, %d needing revision, "
          "%d draft" % (len(cs), counts["accepted"], counts["review"],
                        counts["revise"], counts["draft"]))
    if counts["review"] or counts["revise"]:
        print("review: %d of 1500." % counts["accepted"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
