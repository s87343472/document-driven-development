# Principles and anti-patterns

## Why this method exists

Code is now cheap to generate. What is still scarce is knowing what should exist and being sure it works. An agent told "build me a signup page" builds the average signup page from its training data, filling every gap with defaults that may not match the business. Documents capture what only the person knows; checks prove the result matches it.

## Principles

1. **The business core comes first.** Agree on who, the real flow, the rules and the exceptions before anything is built. The agent cannot learn these from code or training data.
2. **Don't build in a vacuum.** Check existing products, industry practice and open source first. Building is a decision, not a default.
3. **Write only what cannot be seen.** Documents hold intent, rules, decisions and rejected options. Do not restate what the code already shows; the agent can read the repo.
4. **Documents are the source of truth for intent; checks are the source of truth for behaviour.** When they disagree with the code, find out which one is wrong and fix that layer.
5. **Trace problems to their layer.** Misunderstood business → spec.md. Wrong approach → plan.md. Wrong code → code.
6. **One core goal per version.** Small versions that work end to end beat a large version that almost works.
7. **Name what will not change.** Before v0.1, decide which parts later versions build on, so a thin first version is not throwaway.
8. **Each version has a gate.** Tools: checks pass and the user confirms. Products: real use, retention or payment, not interest. Do not advance until it passes.
9. **Hard rules are enforced, not requested.** If it must always hold, put it in tooling.
10. **Match the process to the stakes.** A field change does not need three documents; a new product does.
11. **In agent products, documents can be the runtime.** When the product is itself an agent, its standards, memory and state files can be the live layer it reads and writes. Keep them readable and versioned so people can see and edit how it thinks. Their version numbers are separate from the product's.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Starting with the tech stack | The business rules get shaped by the tool instead of the other way round |
| Asking a non-technical person technical questions | They guess, and the guess becomes a requirement |
| Sending a long questionnaire | Answers are shallow; ask one real question at a time |
| Building what already exists | Months spent on a solved problem |
| Restating the code in plan.md | It goes stale and misleads the next agent |
| Acceptance criteria nobody can check | "Done" becomes an opinion |
| Rules only in prose | The agent decides they do not apply this time |
| Reviewer that wrote the code | It repeats its own reasoning instead of checking |
| Fixing every review remark | Adds layers and tests for cases that cannot happen |
| Advancing past a failed gate | Building on assumptions nobody verified |
| Fixing code while the document says otherwise | The next agent follows the document and undoes the fix |
