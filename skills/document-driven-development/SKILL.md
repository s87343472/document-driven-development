---
name: document-driven-development
description: Turn an idea into working software by first agreeing on the business core with the person, checking what already exists, writing short intent/spec/plan documents, and proving the result with runnable checks. Use when someone wants to build a new product, tool, agent or feature, wants to change what an existing one does, or mentions intent.md, spec.md, plan.md or roadmap.md. Works for technical and non-technical people. Skip for typo fixes, one-off scripts and questions.
license: MIT
metadata:
  version: "3.0.0"
  updated: "2026-10"
---

# Document-Driven Development

The person knows the business. You know how to build. Documents are where the two meet, and checks are how both of you know it worked.

Talk to the person in their language. Write documents in the language they will read them in.

## How deep to go

Match the process to what a wrong guess would cost.

- **Small change** to an existing project (a field, a fix, a tweak): say in two or three sentences what you will change and what it affects, wait for a yes, build, run the checks. No new documents unless a decision is worth recording.
- **New feature**: update spec.md with the feature and its acceptance checks, update plan.md only if the approach is not obvious, build, verify.
- **New product or big change**: the full flow below.

Never skip understanding the business core. Skip paperwork freely.

## The full flow

### 1. Read the person

Before asking about the product, work out who you are talking to from how they write and what they ask, or ask once in a friendly way. Then adapt:

- **Engineers**: skip basics, but still push on who the users are and what the business rule is. Engineers tend to jump to stack choices; hold that until the core is clear.
- **Non-technical people** (sales, finance, operations, designers, founders): never ask them to make technical choices. Use their words, not yours. Ask about real situations, show drafts they can react to, and make the technical decisions yourself, explaining them in one plain sentence each.

See `references/discovery.md` for how to question each kind of person.

### 2. Find the business core together

This is the most important step. Most failed builds come from a business flow that was never made explicit.

Work with the person until both of you can state, in a few plain sentences:

- who uses it, and what they are trying to get done
- the main flow, step by step, as it happens in real life today
- the key things it tracks (an order, a client, an invoice) and the rules about them
- the exceptions that actually happen (refunds, missing data, a manager override)
- what "it works" looks like for them, in their terms

How:

- Ask one question at a time. Prefer "walk me through the last time you did this" over "what features do you need".
- Draft first, then ask them to correct it. People fix a wrong draft faster than they describe from scratch. A short numbered flow, a rough screen sketch or a sample record all work.
- Play it back in their words and get an explicit "yes, that's it" before moving on.
- If they cannot answer, propose the most common way it is done in their industry and ask if that fits.

Stop discovery when the core flow is agreed. Do not try to resolve every detail up front.

### 3. Check what already exists

Never build in a vacuum. Before designing anything, look for:

- a product or service that already solves it (maybe the answer is "don't build")
- an established industry process or standard (bookkeeping rules, sales pipeline stages, an approval chain)
- open-source projects, templates, libraries or APIs that cover most of it
- how similar products handle the same flow

For each serious candidate, decide: **use as is**, **adapt**, or **build**, with one line on why. Tell the person what you found and what you recommend before writing the plan. Record the decision in plan.md. See `references/prior-art.md`.

### 4. Write the documents

Keep them short. A document nobody reads is worse than none.

| File | Answers | Who should be able to read it |
|------|---------|-------------------------------|
| `intent.md` | Why, for whom, what we will NOT build | The person, in five minutes |
| `roadmap.md` | Versions, each with one goal and one gate; the parts that will not change | The person (multi-version products only) |
| `spec.md` | The business flow, rules, exceptions, acceptance checks | The person. No technology names |
| `plan.md` | Build/adapt/use decisions, approach, rejected options | Engineers and agents |

Only write what cannot be seen by reading the code. Do not restate the file tree or the stack the repo already shows.

For non-technical people, show them intent.md and spec.md and get a yes. Do not ask them to review plan.md; summarize it in plain words instead.

Templates: `references/templates.md`.

### 5. Build in small slices

- Build the smallest version that runs end to end through the core flow. One core goal per version.
- Before each slice, say what will change and what it might affect.
- If something in the documents turns out wrong while building, fix the document first, then the code. Diverged documents are worse than none.

### 6. Prove it works

A slice is not done because the code is written. It is done when its checks pass.

- Turn every acceptance criterion in spec.md into something that runs and returns pass or fail: a test, a script, a command. If a criterion cannot be checked, rewrite it until it can.
- Keep one command that runs all checks (for example `./check` or `npm test`), and run it before calling anything done. Show the person the result.
- Rules that must never be broken go into tooling (pre-commit hooks, CI, permission settings), not just into documents. Documents are guidance; an agent may decide guidance does not apply.
- For important changes, have a separate reviewer with fresh context compare the change against spec.md, report only problems that affect correctness, and skip style.
- For non-technical people, also walk them through the real thing (a link, a screenshot, a sample run) and let them confirm it matches their flow.
- Every bug found later becomes a new check, so it can never come back unnoticed.

Details: `references/verification.md`.

### 7. Pass the gate before the next version

Each version has a gate in roadmap.md or spec.md. For tools: the checks pass and the person confirms it fits their flow. For products: a real signal such as use, retention or payment, not interest. Do not start the next version until the gate passes.

## When something goes wrong

- Find the cause before changing code. If two fixes fail, add logging and look at real data instead of guessing.
- Trace the cause to its layer: wrong business understanding → spec.md; wrong approach → plan.md; wrong code → code. Fix the layer that was wrong.
- When a fix works, look for the same problem elsewhere and fix it there too.

## Done means

- The core flow works end to end, and the person has confirmed it.
- All checks pass from one command.
- Documents match the code and were committed with it.
- Decisions and rejected options are recorded, so the next agent does not repeat them.

## References

Load only when needed:

- `references/discovery.md`: questioning playbook per type of person, business-core canvas
- `references/prior-art.md`: how to search for existing solutions and decide use/adapt/build
- `references/templates.md`: intent, roadmap, spec, plan templates with a worked example
- `references/verification.md`: checks, enforcement, review, regression
- `references/principles.md`: the reasoning behind this method and common anti-patterns
