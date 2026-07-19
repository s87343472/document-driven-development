# Document-Driven Development

**English** | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [Français](README.fr.md)

A Claude Code skill that teaches AI to help you build products using a document-driven approach.

> The 15 minutes you save by skipping the spec become a 3-hour debug bill. **Slow at the start, fast throughout.**

## Table of Contents

- [What is Document-Driven Development?](#what-is-document-driven-development)
- [The Core Formula](#the-core-formula)
- [The Documentation System](#the-documentation-system)
- [Installation](#installation)
- [Usage](#usage)
- [Showcase](#showcase)
- [Key Principles](#key-principles)
- [Project Structure](#project-structure)
- [Best Practices](#best-practices)
- [FAQ](#faq)
- [Read the Article Series](#read-the-article-series)
- [Changelog](#changelog)

## What is Document-Driven Development?

**Documentation is the Single Source of Truth. Code is the implementation of documentation.**

When you tell an agent "build me a signup page," it perfectly implements *its* understanding — filled in with the averages of its training data, not your unstated assumptions about security, edge cases, and business rules. Natural language is ambiguous by default; humans fill the gaps with shared experience, but you and the agent share none.

Instead of letting AI generate code from vague requirements, this skill guides you to:

1. **Think first** — Clarify intent, scope, and success criteria
2. **Document second** — Create structured documentation
3. **Code third** — Generate code based on clear specifications

The deliverable is not always a web app. Skills, agents, MCP servers, CLI tools, and .md methodologies all use the same document system.

## The Core Formula

```
intent.md  →  roadmap.md  →  spec.md  →  plan.md  →  code
  (WHY)        (PATH)        (WHAT)       (HOW)
```

- **Generation is cheap; controlled evolution is scarce.** The bottleneck is no longer typing code — it's deciding what should exist. Documents are where that deciding happens.
- **Trace problems to documents.** When code fails, fix the source of truth, then regenerate.
- **Describing what you want ≠ defining what should be built.** A spec turns the former into the latter.

## The Documentation System

| Layer         | File         | Purpose                                     | Stability           |
| ------------- | ------------ | ------------------------------------------- | ------------------- |
| Intent        | `intent.md`  | WHY and FOR WHOM                            | Rarely changes      |
| Roadmap       | `roadmap.md` | Version path + invariant architecture spine | Occasionally (multi-version products only) |
| Specification | `spec.md`    | WHAT to build                               | Changes per feature |
| Plan          | `plan.md`    | HOW to implement                            | Changes often       |

These are build-time documents. Agentic products may also have **runtime documents** — the standard / memory / state files the running product itself reads and writes. Keep them versioned and human-readable so the user can see, and edit, how the product thinks. See [`principles.md`](skills/document-driven-development/principles.md).

## Installation

### For Claude Code

```bash
# In your project
mkdir -p .claude/skills
cp -r skills/document-driven-development .claude/skills/

# Or globally
cp -r skills/document-driven-development ~/.claude/skills/
```

### For Claude (Web/API)

Copy the content of `skills/document-driven-development/SKILL.md` (plus `templates.md` and `principles.md` if context allows) into your system prompt or project instructions.

## Usage

Once installed, Claude will apply this methodology when you:

- Explicitly ask to build a project with DDD
- Ask to add features to an existing project
- Mention `intent.md`, `spec.md`, `plan.md`, or `roadmap.md`

Note: the skill ships with `disable-auto-invoke: true` to avoid over-triggering. Remove that line from SKILL.md's frontmatter if you want it to activate automatically.

## Showcase

### Before: Vibe Coding

```
You: Help me build a personal blog
Claude: Sure! [Generates 500 lines of code]
You: Wait, I wanted it simpler, no database, just markdown files...
Claude: Oh, let me redo that... [Another 500 lines, still not quite right]

# Result: multiple iterations, wasted time, code doesn't match expectations
```

### After: Document-Driven

```
You: Help me build a personal blog
Claude: Let's use document-driven development. First, some questions:
  1. What's the main purpose? 2. Who will read it?
  3. What does "done" look like for v0.1? 4. What do you NOT want?

You: Tech articles, for developers. v0.1 just renders markdown.
    No comments, no CMS, no database.

Claude: [creates intent.md, spec.md, plan.md, then generates focused code]

# Result: right output first time, documented for future iterations
```

## Key Principles

1. **Document First, Code Second** — Never generate code without clear documentation
2. **Trace Problems to Documents** — When code fails, check if it's a spec or plan issue
3. **One Core Goal Per Version** — v0.1, v0.2, v0.3... small steps
4. **Keep Documents and Code in Sync** — Commit them together
5. **Documents are for Communication** — Write for future you and AI
6. **Define the Architecture Spine Before v0.1** — Name what will NOT change across versions, so a thin v0.1 isn't throwaway
7. **Each Version Has a Validation Gate** — Tools: works as specified. Products: retention, usage, or payment — not interest. Don't advance until the gate passes
8. **In Agentic Projects, Documents Can Be the Runtime** — The agent reads and writes them live; keep them human-readable and versioned

## Project Structure

```
document-driven-development/
├── README.md               # English (this file)
├── README.zh-CN.md         # 简体中文
├── README.ja.md            # 日本語
├── README.fr.md            # Français
├── LICENSE
└── skills/
    └── document-driven-development/
        ├── SKILL.md        # Behavior rules + workflows (context-efficient core)
        ├── templates.md    # intent / roadmap / spec / plan templates + example
        └── principles.md   # Philosophy, principles 1-8, anti-patterns
```

## Best Practices

### Do's

- **Start with intent.md** — Even a 5-line intent.md is better than none
- **Define non-goals explicitly** — "No user accounts" prevents scope creep
- **Name the spine before v0.1** — Later versions fill it in, not rebuild it
- **Keep versions small** — v0.1 should be achievable in hours, not days
- **Update docs when requirements change** — Fix the source of truth, not just the code
- **Commit docs and code together**

### Don'ts

- **Don't skip to code** — Resist the urge to "just start coding"
- **Don't over-document** — plan.md describes WHAT to achieve, not exact code
- **Don't put tech in spec.md** — "User can search" (good) vs "Use Elasticsearch" (put in plan.md)
- **Don't aim for v1.0 immediately** — v0.1 → v0.2 → v0.3 is the way
- **Don't advance past a failed gate** — You'd be building on unvalidated assumptions

## FAQ

**Q: Isn't this slower than just asking AI to write code?**
For trivial tasks, yes. For anything you'll iterate on, no. The time spent on documentation is recovered many times over when you avoid "that's not what I wanted" loops.

**Q: Do I need all the documents?**
For small projects you can combine them, and roadmap.md only matters for multi-version products. But keeping them separate helps you think at different levels: WHY → PATH → WHAT → HOW.

**Q: What if my requirements change mid-project?**
Update the documents first, then the code. Documentation stays the source of truth.

**Q: Can I use this with other AI tools besides Claude?**
Yes. The methodology works with any AI coding assistant — copy SKILL.md into your system prompt.

## Read the Article Series

This skill distills the 9-part series **"The New Coding Paradigm in the AI Era"** (in Chinese), based on 43 industry sources, papers, and field reports on Spec-Driven Development:

- [#01 — The End of Vibe Coding is Planning First](https://www.sagasu.art/p/vibe-coding-end-is-planning-first)
- [#02 — Specification as Protocol: When Documents Become the Source of Truth](https://www.sagasu.art/p/specification-is-protocol-when-document-becomes-code-fact-source)
- [#03 — The Truth About Speed: What the Data Says](https://www.sagasu.art/p/speed-truth-data-document-driven-fast-or-not)
- #04–#09 — see the full series on [sagasu.art](https://www.sagasu.art/)

## Changelog

- **2026-06** — Refreshed for the AI-coding-tool / agent era: deliverable types beyond web apps, roadmap.md bridge layer, architecture-spine principle, per-version validation gates, documents-as-runtime for agentic projects (principles 6-8)
- **2026-03** — Refactored for context efficiency: split into SKILL.md + templates.md + principles.md, added Stop Condition, tightened triggering
- **2026-01** — Initial release v1.0

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

MIT License — see [LICENSE](LICENSE) for details.

## Author

Created by **SagaSu**

- Blog: <https://www.sagasu.art/>
- Twitter: [@sujingshen](https://x.com/sujingshen)

## Acknowledgments

Based on the "Document-Driven Development" methodology series. The core idea: **generation is cheap, controlled evolution is scarce.**
