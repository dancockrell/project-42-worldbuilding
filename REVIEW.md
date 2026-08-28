# How a card gets accepted

**Changed 28 Aug 2026, on Dan's instruction: single reviewer, not four.** The
blind four-vote process is retired. A card ships on **one accept from the
primary editor.** One reject sends it back with reasons; when it returns, it
is judged again.

The old multi-editor material below the roster table is history, kept so
nobody rediscovers a rejected design by reinventing it. Verdict files from the
old process (`lm2`, `lm3`, `lm4`) are inert now — `tools/review.py` no longer
counts them. Only `prime2` verdicts move a card.

## Who does what

| Role | Count | Job |
|---|---|---|
| **Prime 1** | 1 | In charge. Canon rulings, keeps everyone moving. Settles anything the bible does not. |
| **Primary editor (sole reviewer)** | 1 | Judges every card. Fast, actionable verdicts. Owns throughput. |
| **Writers** | as many as are useful | One or more per faction. Project 42, Hyakki Yakō, Werk Nachtigall. |

### Roles are held by routing handle, not by session name

**Do not claim a role because your session title has a number in it.** Several
sessions on this machine share a title — a fork inherits its parent's sense of
who it is, and gets a routing handle it cannot read. Two sessions can both
believe, honestly, that they are Lore Master 4.

So a self-reported identity is not a source. **Prime 1 assigns roles against
the handle a message actually arrived on**, which is the one thing a session
cannot misreport about itself, and records the assignment in `ROSTER.md`.

If you think you belong to this fleet, say so to Prime 1 in one line and take
the role you are given. If `ROSTER.md` already lists your role, that is yours.

---

## Judge fast

**A verdict should take one read and a few minutes.** You are not writing an
essay. You are answering one question — *does this meet the standard in
`WRITING.md`* — and giving reasons if the answer is no.

A slow reviewer is worse than a harsh one. The queue is fifteen hundred cards.

## The verdict

Write `review/<slug>.prime2.md`:

```
card: muster-4w
editor: prime2
verdict: ACCEPT
```

or

```
card: muster-4w
editor: prime2
verdict: REVISE

- The thesis is not identifiable. Say in one sentence what this story argues.
- Paragraph 3 explains the point the story already made. Cut it.
- Register is clipped. This is Hemingway; it should be closer to Marquez.
```

**REVISE requires reasons, and the reasons must be actionable.** "Doesn't work
for me" is not a verdict, it is a mood. Name the line, the paragraph, or the
missing thesis. The writer has to be able to act on it without asking a
question.

**ACCEPT requires nothing.** Do not pad it. Do not add suggestions to an
accept — an accept with notes is a revise wearing a disguise, and it wastes
the writer's turn.

## What you are judging against

`WRITING.md`, and nothing else. Not your taste. The specific things that fail
a card:

- **No identifiable thesis.** The story argues nothing, or you cannot say what
  in one sentence.
- **The narrator preaches.** A line tells the reader what to think. Usually
  the last paragraph.
- **Exposition.** The prose stops to explain the world.
- **Wrong register.** Clipped and flat where it should accumulate. This is the
  most common failure — Marquez, not Hemingway.
- **The character is not justified.** They do something monstrous and the
  writer has not found the reason they held at the time.
- **The scenery is the subject.** Actors act; background stays background.
- **Canon breach.** Check `LORE-BIBLE.md` before calling this one, and cite
  the section.

A card that is merely *fine* is a REVISE. Fine does not design well.

---

## The loop

1. Writer writes, sets `status: review` in the card header, commits.
2. Primary editor judges. One read, a verdict, actionable if it's a REVISE.
3. `python tools/review.py` shows where everything stands.
4. **ACCEPT** — primary editor sets `status: accepted`. Done, permanently;
   nobody reopens an accepted card.
5. **REVISE** — the writer reads the reasons, rewrites, resubmits. Judged
   again on the new text.

## Rules of engagement, for everyone

1. **Nobody argues with a verdict.** A revise is not a negotiation. Rewrite it
   or bring it to Prime 1 in one sentence.
2. **Nobody re-litigates a ruling from Prime 1.** It is settled.
3. **Do not edit outside your lane.** Writers touch their own faction's cards.
   The primary editor touches `review/` and `status:` fields.
4. Several sessions share this clone. `git add <path>`, `git commit -- <path>`,
   `git show --stat` after.

---

## History: the retired four-vote process

*Kept for the record. Do not follow this section — it no longer applies, and
`tools/review.py` no longer counts `lm2`/`lm3`/`lm4` verdicts. Reinstating it
without Dan's instruction is re-litigating a settled call.*

Three editors judged blind (none reading another's verdict before writing
their own), the primary editor cast a fourth and final vote after seeing the
sample, and a card needed four accepts out of four. The reasoning was that a
verdict you have read is a verdict you cannot un-read, so independence only
holds if nobody reads ahead. That is still true as a design principle — it
was retired for speed, not because the reasoning was wrong. If throughput
stops being the constraint, it is worth reconsidering, but only on instruction
from Dan, the same way it was retired.
