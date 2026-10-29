# Verification: proving it works

Documents tell the agent what to build. Checks tell everyone whether it was built. You need both: guidance without checks drifts, checks without guidance chase the wrong target.

## 1. Every acceptance criterion becomes a check

A good check runs without a human and returns pass or fail.

| Criterion type | Typical check |
|---|---|
| Business rule (totals, states, permissions) | Automated test |
| End-to-end flow | Script that drives the flow, or a browser test |
| Output format (file, email, report) | Script that produces a sample and compares it |
| "The user can do X without help" | Manual walkthrough with the person, recorded in spec.md |
| Performance, limits | Script with a threshold |

If a criterion cannot be turned into any of these, it is too vague. Rewrite it with the person until it can.

## 2. One command runs everything

Keep a single entry point, for example `./check`, `make check` or `npm test`, and write it in plan.md. Run it:

- before saying a slice is done
- after merging work from parallel agents or branches
- before every release
- after switching to a different model or tool

Show the output to the person, not just "tests pass".

Build this script early, in the first slice. An agent that can check its own work can keep going without being watched.

## 3. Hard rules go into tooling, not prose

Anything written in a document is guidance; an agent may judge it does not apply. If a rule must hold every time, enforce it:

- **Works with any tool**: git pre-commit hooks, CI that blocks merging when checks fail, branch protection, linters with custom rules.
- **Agent-tool settings**: permission deny lists and hooks in your coding agent (for example, Claude Code hooks and deny rules) to block reading secrets, force-pushing or deploying.

Good error messages say how to fix the problem, so the agent can correct itself.

The reverse also holds: if something is only a preference, keep it as guidance and let the agent decide.

## 4. Review against the spec

For changes that matter:

- Use a reviewer with fresh context (a separate agent or session) that did not write the code, so it is not anchored on the author's reasoning.
- Ask it to compare the change against spec.md: is every requirement implemented, do the listed exceptions have checks.
- Ask it to report only problems that affect correctness and to skip style. A reviewer asked to find problems will always find something; fixing every remark adds needless complexity.
- At most three rounds. From the second round on, review only what changed since the last round.

The riskier the change, the deeper the review. For one-way changes (deleting data, payments, publishing, sending to real users), the person looks at the real result themselves before it goes live.

## 5. Every bug becomes a check

When a bug or user complaint is found:

1. Write a check that fails because of it.
2. Fix it until the check passes.
3. Look for the same mistake elsewhere and fix those too.

The suite grows into a record of every past mistake. Run it in full when switching models to see whether the new one still handles them.

## 6. Leave a trail for the next agent

Commit documents with the code they describe. In each commit message, write what changed, how it was verified, and how to roll it back. Git history then becomes reliable context for whoever works on it next.

Record rejected approaches in plan.md so they are not proposed again.

## 7. Release in rings

For anything users touch: first the person, then a few willing early users, then everyone. A simple switch for early access is often enough.

## Working with several agents at once

Give each agent its own working copy (for example a git worktree or branch). Each commits only its own changes. After merging, run the full check command once more.
