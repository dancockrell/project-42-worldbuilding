"""Build the readable Project 42 site from source markdown.

WHY A GENERATOR AND NOT RAW MARKDOWN ON GITHUB
GitHub renders markdown, but it renders it as a code-hosting page: narrow
gutters, UI chrome, no way to move from one story to the next. This wiki
exists to be *read* -- specifically so stories can be reviewed one after
another and judged. That needs a reading column, real typography, and a
next-story link. Hence ~200 lines of generator instead of a folder of files.

Stdlib only. No build tooling, no dependencies, no npm.

    python tools/build.py

Writes docs/, which GitHub Pages serves. Exit 0 = built.
Exit 2 = could not evaluate (no source, or the parser found nothing).
"""
import html
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source")
OUT = os.path.join(ROOT, "docs")

FACTIONS = [
    ("p42", "Project 42", "The Allies. Time travel, electricity, phasing, and "
     "the United States."),
    ("wn", "Werk Nachtigall", "The Kaiser's Empire. Frames, hybrids, jets, "
     "and the Prussian fascination with the occult."),
    ("hy", "Hyakki Yak\u014d", "The Empire of Japan. Folklore, bushid\u014d, "
     "and something older that is feeding them."),
]
FACTION_NAME = {k: n for k, n, _ in FACTIONS}


def parse_card(path):
    """Cards are a small fixed format. Anything else is a defect, not a page.

    # TITLE
    faction: wn
    type: Unit
    tier: S

    ## Bio
    ...

    ## Story
    ### STORY TITLE
    ...
    """
    text = io.open(path, encoding="utf-8").read()
    card = {"slug": os.path.splitext(os.path.basename(path))[0]}

    m = re.search(r"^#\s+(.+)$", text, re.M)
    if not m:
        return None
    card["title"] = m.group(1).strip()

    for key in ("faction", "type", "tier", "image", "image_caption"):
        km = re.search(r"^%s:\s*(.+)$" % key, text, re.M | re.I)
        card[key] = km.group(1).strip() if km else ""

    # "Draw" is the current heading. "Bio" is accepted so the first entries
    # written before the rename keep building rather than silently losing
    # their hundred words to an empty panel.
    bio = re.search(r"^##\s+(?:Draw|Bio)\s*$(.*?)(?=^##\s|\Z)", text,
                    re.M | re.S)
    card["bio"] = bio.group(1).strip() if bio else ""

    story = re.search(r"^##\s+Story\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    body = story.group(1).strip() if story else ""
    sm = re.match(r"^###\s+(.+?)\s*$(.*)", body, re.M | re.S)
    if sm:
        card["story_title"] = sm.group(1).strip()
        card["story"] = sm.group(2).strip()
    else:
        card["story_title"] = ""
        card["story"] = body

    card["words"] = len(re.findall(r"[A-Za-z\u00c0-\u024f']+", card["story"]))
    return card


def inline(s):
    """Bold, italic, and em-dashes. Deliberately small -- prose, not markup."""
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", s)
    return s


def prose(block):
    out = []
    for para in re.split(r"\n\s*\n", block.strip()):
        para = para.strip()
        if not para:
            continue
        if para.startswith("### "):
            out.append("<h3>%s</h3>" % inline(para[4:]))
        elif para == "---":
            out.append("<hr>")
        else:
            out.append("<p>%s</p>" % inline(para).replace("\n", "<br>\n"))
    return "\n".join(out)


def page(title, body, crumb=""):
    return TEMPLATE.replace("{{TITLE}}", html.escape(title)) \
                   .replace("{{CRUMB}}", crumb) \
                   .replace("{{BODY}}", body)


TEMPLATE = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "template.html"), encoding="utf-8").read()


def main():
    # Windows consoles default to cp1252 and die on the first macron in
    # "Hyakki Yakou". The site would already be written by then, so the
    # failure looks like a broken build when it is a broken print.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if not os.path.isdir(SRC):
        print("build: NOT CHECKED - no source/ at %s" % SRC)
        return 2

    cards = {k: [] for k, _, _ in FACTIONS}
    total = 0
    for key, _, _ in FACTIONS:
        d = os.path.join(SRC, "cards", key)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            c = parse_card(os.path.join(d, fn))
            if c is None:
                print("build: SKIPPED %s/%s - no title line" % (key, fn))
                continue
            cards[key].append(c)
            total += 1

    # The denominator. A generator that silently found nothing and a finished
    # site both produce a working index page, so refuse rather than report.
    if total == 0:
        print("build: NOTHING FOUND - 0 cards parsed from %s" % SRC)
        print("build: an empty build and a broken parser look identical here.")
        return 2

    os.makedirs(os.path.join(OUT, "cards"), exist_ok=True)

    ordered = []
    for key, name, _ in FACTIONS:
        for c in cards[key]:
            ordered.append(c)

    for i, c in enumerate(ordered):
        prv = ordered[i - 1] if i else None
        nxt = ordered[i + 1] if i + 1 < len(ordered) else None
        nav = []
        if prv:
            nav.append('<a class="prev" href="%s.html">&larr; %s</a>'
                       % (prv["slug"], html.escape(prv["title"])))
        if nxt:
            nav.append('<a class="next" href="%s.html">%s &rarr;</a>'
                       % (nxt["slug"], html.escape(nxt["title"])))
        body = [
            '<article class="card">',
            '<p class="kicker">%s &middot; %s%s</p>' % (
                html.escape(FACTION_NAME.get(c["faction"], c["faction"])),
                html.escape(c["type"] or "Unit"),
                (" &middot; <b>%s tier</b>" % html.escape(c["tier"]))
                if c["tier"] else ""),
            "<h1>%s</h1>" % inline(c["title"]),
        ]
        if c["image"]:
            body.append(
                '<figure><img src="../%s" alt="%s" loading="lazy">'
                '<figcaption>%s</figcaption></figure>'
                % (html.escape(c["image"]),
                   html.escape(c["image_caption"] or c["title"]),
                   inline(c["image_caption"])))
        else:
            body.append('<figure class="pending"><div class="plate"></div>'
                        '<figcaption>Art pending.</figcaption></figure>')
        body += [
            '<section class="bio">%s</section>' % prose(c["bio"]),
            '<section class="story">',
        ]
        if c["story_title"]:
            body.append("<h2>%s</h2>" % inline(c["story_title"]))
        body.append(prose(c["story"]))
        body.append("</section>")
        body.append('<p class="wc">%d words</p>' % c["words"])
        body.append("</article>")
        body.append('<nav class="pager">%s</nav>' % "".join(nav))
        io.open(os.path.join(OUT, "cards", c["slug"] + ".html"), "w",
                encoding="utf-8").write(
            page(c["title"], "\n".join(body),
                 '<a href="../index.html">Project 42</a>'))

    idx = ['<h1>Project 42</h1>',
           '<p class="lede">Shared worldbuilding for a war that was fought by '
           'systems. Three of them. Every card here is a person, an animal, or '
           'a thing that acts &mdash; a hundred words of what it is, and five '
           'hundred of it doing something.</p>']
    for key, name, blurb in FACTIONS:
        idx.append('<section class="faction">')
        idx.append("<h2>%s</h2>" % html.escape(name))
        idx.append('<p class="blurb">%s</p>' % html.escape(blurb))
        if cards[key]:
            idx.append("<ul class=\"cards\">")
            for c in cards[key]:
                idx.append('<li><a href="cards/%s.html">%s</a>'
                           '<span class="meta">%s</span></li>'
                           % (c["slug"], inline(c["title"]),
                              html.escape(c["type"] or "")))
            idx.append("</ul>")
        else:
            idx.append('<p class="empty">Nothing written yet.</p>')
        idx.append("</section>")
    io.open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        page("Project 42", "\n".join(idx)))

    io.open(os.path.join(OUT, ".nojekyll"), "w", encoding="utf-8").write("")

    print("build: %d cards across %d factions" % (total, len(FACTIONS)))
    for key, name, _ in FACTIONS:
        print("  %-16s %d" % (name, len(cards[key])))
    print("build: wrote docs/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
