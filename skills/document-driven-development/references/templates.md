# Templates

Short is better. Delete any section that has nothing real to say.

## intent.md

```markdown
# Intent

## In one sentence
[What this is and why it should exist]

## For whom
- Main user: [who, and the job they are trying to get done]
- Others affected: [who else, if anyone]

## The problem today
[How it is done now and what hurts]

## Why not something that exists
[Result of the prior-art check, one or two lines]

## Success looks like
- [Observable result in the user's terms]

## Not building
- [Explicitly out of scope]
```

## roadmap.md (only for products with several versions)

```markdown
# Roadmap

## What stays fixed
[The parts and boundaries that later versions build on, not rebuild]

## v0.1
- Goal: [one sentence]
- Includes: [...]
- Later: [...]
- Gate: [tools: checks pass and the user confirms it fits / products: real use, retention or payment]

## v0.2
- Goal: ...
```

## spec.md

No technology names here. The person should be able to read and approve it.

```markdown
# Spec — v0.1

## Core flow
1. [Who] does [what]
2. The system [does what]
3. [Who] sees / receives [what]

## Things and rules
- [Thing]: [rules about it]

## Exceptions
- [Situation] → [what should happen]

## Acceptance checks
Each one must be checkable with a pass/fail result.
- [ ] [Condition] — checked by: [test / script / manual walkthrough with the user]

## Not in this version
- [...]
```

## plan.md

Only what is not visible from the code.

```markdown
# Plan — v0.1

## Decisions
- [Part]: use / adapt / build [name] — because [reason]
  - Rejected: [option] — because [reason]

## Approach
[How the core flow is implemented, in a few lines. Name the parts that must not change between versions.]

## Constraints
- [Limits that are not obvious: budget, data location, existing systems, deadlines]

## Checks
- Run all: `[one command]`
- [What it covers, and anything checked manually]
```

## Worked example: a small studio's quote-to-invoice tool

The person runs a five-person design studio, is not technical, and tracks quotes in a spreadsheet.

### intent.md

```markdown
## In one sentence
Turn an accepted quote into an invoice in one step, so nothing gets billed twice or forgotten.

## For whom
- Main user: the studio owner, who sends quotes and invoices herself
- Others affected: clients, who receive the invoice

## The problem today
Quotes live in a spreadsheet; invoices are typed again by hand. Last quarter two jobs were never invoiced.

## Why not something that exists
Her accounting software can invoice but has no quotes; quoting tools tried were too heavy for five people.
Decision: keep her accounting software for invoices, build only the quote step and the hand-off.

## Success looks like
- Every accepted quote becomes an invoice in her accounting software within a day, with no retyping.

## Not building
- Time tracking, client portal, payments
```

### spec.md (excerpt)

```markdown
## Core flow
1. Owner creates a quote from a client and a list of line items
2. Client accepts by replying to the email
3. Owner marks the quote accepted
4. The system creates a draft invoice in the accounting software with the same lines
5. Owner reviews and sends it from there

## Exceptions
- Client accepts only part of the quote → owner removes lines before marking accepted
- Quote marked accepted twice → no second invoice is created

## Acceptance checks
- [ ] Accepted quote creates exactly one draft invoice with the same totals — checked by: automated test against the accounting sandbox
- [ ] Marking accepted twice creates no second invoice — checked by: automated test
- [ ] Owner can do the full flow without help — checked by: walkthrough with the owner
```
