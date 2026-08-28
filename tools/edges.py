"""Query canon relationships before writing a scene with two named characters.

Why: three writers hand-writing fifteen hundred stories will each independently
invent a plausible relationship between two characters who already have one on
record in NETWORK-HUB-EDGES.md -- and every invention will look fine on its own
page, because nothing checks prose against a graph. That is the number-
propagation defect from the wiki audit at fifteen hundred times the surface,
and prose has no checker. This is not a generator input. It is a lookup, so a
writer reaches for the canon fact instead of a third plausible one.

Usage:
    python tools/edges.py falk_naomi
    python tools/edges.py falk_naomi reyes_whitlock_tomas
    python tools/edges.py --list

Node ids match NETWORK-HUB-EDGES.md's jsonl exactly (underscored, lowercase).
`--list` prints every known node id, because the id is the thing you cannot
guess reliably (aust_helene, not aust or helene_aust).
"""
import io, json, os, re, sys

VOLUME = "source/volumes/NETWORK-HUB-EDGES.md"


def load_edges():
    if not os.path.exists(VOLUME):
        print("NOT CHECKED: %s does not exist." % VOLUME)
        sys.exit(2)
    text = io.open(VOLUME, encoding="utf-8").read()
    lines = re.findall(r"^\{.*\}$", text, re.M)
    if not lines:
        print("NOT CHECKED: 0 edge lines parsed out of %s -- the file exists "
              "but nothing matched the jsonl pattern. Refusing to report an "
              "empty graph as complete." % VOLUME)
        sys.exit(2)
    edges = []
    for ln in lines:
        try:
            edges.append(json.loads(ln))
        except json.JSONDecodeError as e:
            print("NOT CHECKED: malformed edge line, refusing to load a "
                  "partial graph: %r (%s)" % (ln[:80], e))
            sys.exit(2)
    return edges


def fmt(e):
    # NETWORK-HUB-EDGES.md enforces "absent, not zero" (the_watcher's REGARD)
    # by omitting the edge line entirely, not by a null weight field -- so
    # there is no w=None case in real data. Every edge that exists has a
    # weight. Formatting it as if null were possible would be untested
    # coverage of a branch nothing here can trigger.
    w = e["w"]
    w_str = "%+.1f" % w if e["axis"] == "REGARD" else "%.1f" % w
    arrow = "<->" if e.get("undirected") else "->"
    line = "  %-24s %s %-24s  %-10s %s" % (e["from"], arrow, e["to"], e["axis"], w_str)
    if e.get("note"):
        line += "\n      %s" % e["note"]
    return line


def main(argv):
    if "--list" in argv:
        edges = load_edges()
        nodes = sorted({e["from"] for e in edges} | {e["to"] for e in edges})
        print("%d nodes across %d edges:" % (len(nodes), len(edges)))
        for n in nodes:
            print("  " + n)
        return 0

    if not argv:
        print(__doc__)
        return 2

    edges = load_edges()
    targets = [a.lower() for a in argv]
    all_nodes = {e["from"] for e in edges} | {e["to"] for e in edges}
    unknown = [t for t in targets if t not in all_nodes]
    if unknown:
        print("NOT FOUND: %s is not a node in %s." % (", ".join(unknown), VOLUME))
        print("This means either the node has no edges yet (spoke/periphery, "
              "not a hub) or the id is wrong -- run --list to check spelling.")
        return 1

    if len(targets) == 1:
        n = targets[0]
        hits = [e for e in edges if e["from"] == n or e["to"] == n]
    else:
        a, b = targets[0], targets[1]
        hits = [e for e in edges
                if {e["from"], e["to"]} == {a, b}]
        if not hits:
            print("NO EDGE ON RECORD between %s and %s." % (a, b))
            print("That is not the same as 'they have no relationship' -- it "
                  "means nobody has written one down yet. If your scene needs "
                  "one, that is new canon: decide it deliberately and add it "
                  "to NETWORK-HUB-EDGES.md rather than leaving it implicit in "
                  "prose only you can see.")
            return 0

    print("%d edge(s):" % len(hits))
    for e in sorted(hits, key=lambda e: (e["from"], e["to"], e["axis"])):
        print(fmt(e))
    return 0


sys.exit(main(sys.argv[1:]))
