# Prior art: check what already exists before building

Building from scratch is the most expensive option and should be chosen on purpose, not by default. Do this after the business core is agreed and before writing plan.md.

## Where to look

Search in this order. Stop when you have two or three serious candidates.

1. **Ready-made products or services.** Is there a SaaS, a spreadsheet template, a no-code tool or a feature in something the person already uses that does the core flow? If yes, building may be the wrong answer.
2. **Industry practice.** How is this flow normally run in the person's field? Accounting rules, sales pipeline stages, approval chains, regulatory requirements. These are not design choices to reinvent; follow them unless the person has a reason not to.
3. **Open-source projects and starters.** Projects or templates that already cover most of the flow.
4. **Libraries and APIs.** For the hard parts: payments, auth, maps, PDF, email, scheduling, search.
5. **Similar products.** How do comparable products handle the same flow, wording and exceptions? Borrow what users already understand.

Use web search when available. If you cannot search, say so and list what you know, marked as unverified.

## What to check for each candidate

- Does it cover the core flow, including the exceptions that matter?
- Cost: price, and the cost of running and maintaining it.
- Fit: can the person use it without a developer? Does it hold their data in a way they accept?
- Health: recently maintained, licence allows the use, not a dead end.
- Lock-in: how hard is it to leave later?

## The decision

For each part of the system, pick one:

- **Use as is**: it covers the need; building would add cost without adding value.
- **Adapt**: it covers most of it; extend, configure or wrap it.
- **Build**: nothing fits, or the part is the person's real advantage and should be owned.

Present it to the person in plain words before planning. Example:

> Login and payments: use an existing service, no reason to build.
> Invoice layout: adapt an open-source template.
> The commission rules: build, because they are specific to how your team works.

## Record it

In plan.md, under "Decisions":

```markdown
- [part]: use / adapt / build [name] — because [one line]
  - Considered and rejected: [option] — because [one line]
```

Rejected options matter. They stop the next agent, or the next session, from proposing them again.
