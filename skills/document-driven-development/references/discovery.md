# Discovery: finding the business core with the person

Goal: by the end, you and the person agree on the core flow in a few plain sentences. Everything else can be refined later.

## Ground rules

- One question at a time. Never send a questionnaire.
- Ask about the past, not the future. "Walk me through the last time you did this" gets real steps; "what would you like it to do" gets a wish list.
- Draft, then ask for corrections. A wrong draft is cheaper than a blank page.
- Use their vocabulary. If they say "deal", don't write "opportunity".
- Play back what you heard and wait for an explicit yes.
- If they don't know, offer the common industry way and ask whether it fits.
- Separate "must have for the core flow" from "nice to have". Park the second list in roadmap.md.

## Adapting to the person

Most people are a mix. Pick the closest one or two and adjust as you learn more.

### Engineer

- Strengths: fast on structure, edge cases, data.
- Risk: jumps to stack and architecture before the business is clear; builds what is interesting rather than what is needed.
- Do: keep asking "who uses this and what happens before and after this step". Let them own technical choices, but record them in plan.md with the reason.
- Show: data shapes, sequence of steps, interfaces.

### Designer moving into business

- Strengths: user experience, flows, taste.
- Risk: the screens are clear but the rules behind them are not (who can approve, what happens when payment fails, what is stored).
- Do: start from their screens or sketches, then ask what each button does to the business: what gets created, who gets notified, what can be undone.
- Show: rough screens with the rules written next to them.

### Sales

- Strengths: knows the customer, the objections, the pipeline.
- Risk: describes the pitch, not the process; every customer request sounds like a must-have.
- Do: walk through one real deal from first contact to payment. Ask which steps are slow, manual or error-prone today. Ask which customers would pay for this and how they would know it works.
- Show: the pipeline as a numbered list of stages with what moves a deal from one to the next.

### Finance

- Strengths: precise rules, auditability, numbers that must add up.
- Risk: assumes rules are obvious (rounding, tax, period close, approvals) and does not say them.
- Do: ask for one real example with real numbers, end to end. Ask what must be traceable, who approves what, and what an auditor would check. Industry rules (double-entry, reconciliation) usually apply; confirm rather than invent.
- Show: a sample record or table with the calculation spelled out.

### Operations or other domain expert

- Strengths: knows every exception from experience.
- Risk: the knowledge lives in their head and spreadsheets; they skip steps that feel obvious to them.
- Do: ask to see the current spreadsheet, form or checklist they use. Ask "what goes wrong most often" and "what do you do then".
- Show: the current process as a flow, with the exceptions marked.

### Founder or idea person

- Strengths: vision, energy.
- Risk: the idea is large and vague; scope keeps growing.
- Do: find the one user and the one job that would prove the idea. Ask what result in four weeks would convince them to continue. Push everything else to roadmap.md.
- Show: a one-paragraph intent and a v0.1 that fits in days.

## The business-core canvas

Fill this in together. When every line has an answer the person agrees with, discovery is done.

```markdown
## Who and why
- Main user: [who, in their words]
- The job they are trying to get done: [one sentence]
- How they do it today, and what hurts: [one or two sentences]

## Core flow (as it really happens)
1. [step]
2. [step]
3. [step]

## Things it keeps track of
- [thing]: [the rules about it]

## Exceptions that actually happen
- [situation] → [what should happen]

## What "it works" means to them
- [observable result, in their terms]

## Not now
- [things deliberately left out]
```

The canvas feeds intent.md (who and why, not now) and spec.md (flow, things, exceptions, what works means).

## Signs discovery is not done

- You cannot describe the core flow without using a technical term.
- The person corrected your last playback in a way that changed the flow.
- You find yourself guessing what happens when something fails.
- The list of must-haves keeps growing.
