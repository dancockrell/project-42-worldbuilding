# How a card gets accepted

Three writers write. Three editors judge it blind. The primary editor then
gives it a final up or down. **A card ships only on four accepts out of
four.** One reject sends it back with reasons, and when it returns it is
judged again from zero.

## Who does what

| Role | Count | Job |
|---|---|---|
| **Prime 1** | 1 | In charge. Canon rulings, and keeps everyone moving. Settles anything the bible does not. |
| **Primary editor** | 1 | Schedules the three judges, chases the slow ones, and casts the fourth and final vote. |
| **Editors** | 3 | Judge blind. Fast verdicts with actionable reasons. |
| **Writers** | 3 | One faction each. Project 42, Hyakki Yakō, Werk Nachtigall. |

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

**The primary editor votes last and may see the three.** That is deliberate:
the three are the blind sample, and the fourth vote is a judgement made with
the sample in hand. It is still a real vote — three accepts do not oblige a
fourth, and the primary editor rejecting on its own reasons is the system
working, not the system being overruled.

The primary editor also owns throughput. If a card has sat for three accepts
and no fourth, or an editor has gone quiet, that is theirs to fix without
asking anyone.

---

## The rule that makes it work: judge blind

**Do not read another editor's verdict before you have written your own.**
Not to be polite about it — a verdict you have read is a verdict you cannot
un-read, and four editors who have seen each other's marks are one editor with
three echoes. The whole value of four is that they are four.

Write yours, commit it, and only then look at the others if you want to.

## Judge fast

**A verdict should take one read and a few minutes.** You are not writing an
essay. You are answering one question — *does this meet the standard in
`WRITING.md`* — and giving reasons if the answer is no.

A slow reviewer is worse than a harsh one. The queue is fifteen hundred cards.

---

## The verdict

Write `review/<slug>.<your-name>.md`:

```
card: muster-4w
editor: lm4
verdict: ACCEPT
```

or

```
card: muster-4w
editor: lm4
verdict: REVISE

- The thesis is not identifiable. Say in one sentence what this story argues.
- Paragraph 3 explains the point the story already made. Cut it.
- Register is clipped. This is Hemingway; it should be closer to Marquez.
```

**REVISE requires reasons, and the reasons must be actionable.** "Doesn't work
for me" is not a verdict, it is a mood. Name the line, the paragraph, or the
missing thesis. The writer has to be able to act on it without asking you a
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
2. The three editors each write a verdict. **Blind — none of them reads
   another's first.**
3. The primary editor reads the board and casts the fourth vote.
4. `python tools/review.py` shows where everything stands.
5. **Four accepts** — the primary editor sets `status: accepted`. Done,
   permanently; nobody reopens an accepted card.
6. **Any revise** — the writer reads every reason, rewrites, resubmits.
   **Judging starts over at zero.** An editor who accepted the first version
   judges the new one on its own merits and may reject it.

Verdict files from a previous round stay in `review/` as the record. Name the
round in the filename if you need to: `<slug>.<editor>.r2.md`.

---

## Rules of engagement, for everyone

1. **Editors do not argue with writers, and writers do not argue with
   verdicts.** A revise is not a negotiation. Rewrite it or bring it to Prime 1
   in one sentence.
2. **Editors do not argue with each other.** Ever. You are supposed to
   disagree — that is what four independent judgments are for.
3. **Nobody re-litigates a ruling from Prime 1.** It is settled.
4. **Do not edit outside your lane.** Writers touch their own faction's cards.
   Editors touch `review/` only.
5. Several sessions share this clone. `git add <path>`, `git commit -- <path>`,
   `git show --stat` after.
