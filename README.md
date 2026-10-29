# Document-Driven Development

**English** | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [Français](README.fr.md)

A skill that helps any coding agent turn an idea into working software: agree on the business core first, check what already exists, write short documents, and prove the result with runnable checks.

> The 15 minutes you save by skipping the spec become a 3-hour debug bill. Slow at the start, fast throughout.

## Who it is for

Anyone who builds with an AI agent, technical or not. The agent adapts how it asks questions to the person in front of it:

- **Engineers**: skips the basics, keeps pushing on users and business rules before stack choices.
- **Designers, sales, finance, operations, founders**: no technical questions. The agent asks about real situations ("walk me through the last deal"), shows drafts to correct, and makes the technical calls itself.

## How it works

```
read the person → agree on the business core → check what exists → intent / spec / plan → build in slices → checks pass → gate
```

1. **Business core first.** Who uses it, the real flow, the rules, the exceptions, and what "it works" means, agreed in plain words.
2. **Don't build in a vacuum.** Look for existing products, industry practice, open source and libraries. Decide use, adapt or build for each part.
3. **Short documents.** `intent.md` (why, for whom, not building), `spec.md` (flow, rules, acceptance checks), `plan.md` (decisions and rejected options), `roadmap.md` (versions and gates, optional). Only what the code cannot show.
4. **Prove it.** Every acceptance criterion becomes a pass/fail check, one command runs them all, hard rules live in tooling, reviews compare against the spec, and every bug becomes a new check.
5. **Process matches the stakes.** A small change is two sentences and a check run; a new product gets the full flow.

## Install

The skill is plain Markdown and follows the open Agent Skills format, so it works with any model.

**One command, any agent** (Claude Code, Cursor, Codex and others; needs Node.js):

```bash
npx skills add s87343472/document-driven-development
```

**Claude Code plugin** (can update automatically when a new version is pushed):

```text
/plugin install document-driven-development --marketplace s87343472/document-driven-development
```

The options below install by hand.

**Claude Code, by hand**

```bash
# this project only
mkdir -p .claude/skills && cp -r skills/document-driven-development .claude/skills/
# all projects
cp -r skills/document-driven-development ~/.claude/skills/
```

To stop it from triggering automatically, add `disable-model-invocation: true` to the frontmatter of your local copy and call it with `/document-driven-development`.

**Claude.ai or the Claude API**: zip the `skills/document-driven-development` folder and upload it as a skill.

**Other agents** (Codex, Cursor, Gemini CLI, and others): copy the folder into the tool's skills directory if it supports Agent Skills. Otherwise add one line to your `AGENTS.md` or rules file:

```
For new products, new features or changes to business behaviour, follow skills/document-driven-development/SKILL.md.
```

**Plain chat**: paste `SKILL.md` into the conversation. Add files from `references/` when you reach that step.

## What is inside

```
skills/document-driven-development/
├── SKILL.md                 core behaviour, loaded every time
└── references/              loaded only when needed
    ├── discovery.md         questioning playbook per type of person, business-core canvas
    ├── prior-art.md         searching for existing solutions, use / adapt / build
    ├── templates.md         intent, roadmap, spec, plan, with a worked example
    ├── verification.md      checks, enforcement, review, regression
    └── principles.md        reasoning and anti-patterns
scripts/check.py             repository self-check, also run in CI
.claude-plugin/               Claude Code plugin marketplace entry
```

## Changelog

- **3.0 (2026-10)**
  - Added: adapting discovery to the person (engineer, designer, sales, finance, operations, founder); finding the business core together; prior-art check with use / adapt / build decisions; a verification layer (runnable checks, one command, enforced rules, spec-based review, bugs become checks); process depth matched to the stakes.
  - Removed, because current models handle it on their own: describing the stack and file tree in `plan.md`, documenting an existing codebase before changing it, long templates, and the "never code without documents" rule for small changes.
  - Repo: portable frontmatter only (the old `disable-auto-invoke` field was not a real field and was ignored), references in their own folder, stale files removed, self-check and CI added; one-command install via `npx skills` and the Claude Code plugin marketplace.
- **2026-06**: roadmap.md, architecture spine, validation gates, documents as runtime.
- **2026-03**: split into core, templates and principles for context efficiency.
- **2026-01**: first release.

## Article series

The method comes from the nine-part series "The New Coding Paradigm in the AI Era" (in Chinese) on [sagasu.art](https://www.sagasu.art/).

## License and author

MIT. Created by SagaSu: [sagasu.art](https://www.sagasu.art/) · [@sujingshen](https://x.com/sujingshen)
