# Document-Driven Development

A Claude Code skill that teaches AI to help you build products using a document-driven approach.

## What is Document-Driven Development?

**Documentation is the Single Source of Truth. Code is the implementation of documentation.**

Instead of letting AI generate code based on vague requirements, this skill guides you to:

1. **Think first** - Clarify intent, scope, and success criteria
2. **Document second** - Create structured documentation
3. **Code third** - Generate code based on clear specifications

The deliverable is not always a web app. Skills, agents, MCP servers, CLI tools, and .md methodologies all use the same document system.

## The Documentation System

| Layer         | File         | Purpose                                      | Stability           |
| ------------- | ------------ | -------------------------------------------- | ------------------- |
| Intent        | `intent.md`  | WHY and FOR WHOM                             | Rarely changes      |
| Roadmap       | `roadmap.md` | Version path + invariant architecture spine  | Occasionally changes (multi-version products only) |
| Specification | `spec.md`    | WHAT to build                                | Changes per feature |
| Plan          | `plan.md`    | HOW to implement                             | Changes often       |

These are build-time documents. Agentic products may also have **runtime documents** — the standard / memory / state files the running product itself reads and writes. Keep them versioned and human-readable so the user can see, and edit, how the product thinks. See `skills/document-driven-development/principles.md`.

## Installation

### For Claude Code

Add the skill to your project:

```bash
# Create the skills directory in your project
mkdir -p .claude/skills

# Copy the skill
cp -r skills/document-driven-development .claude/skills/
```

Or add to your global skills:

```bash
cp -r skills/document-driven-development ~/.claude/skills/
```

### For Claude (Web/API)

Copy the content of `skills/document-driven-development/SKILL.md` (plus `templates.md` and `principles.md` if context allows) into your system prompt or project instructions.

## Usage

Once installed, Claude will apply this methodology when you:

- Explicitly ask to build a project with DDD
- Ask to add features to an existing project
- Mention `intent.md`, `spec.md`, `plan.md`, or `roadmap.md`
- Ask about organizing requirements for AI collaboration

Note: the skill ships with `disable-auto-invoke: true` to avoid over-triggering. Remove that line from SKILL.md's frontmatter if you want it to activate automatically.

## Showcase

### Before: Vibe Coding (Without This Skill)

```
You: Help me build a personal blog

Claude: Sure! Here's a complete blog implementation...
[Generates 500 lines of code]

You: Wait, I wanted it simpler, no database, just markdown files...

Claude: Oh, let me redo that...
[Generates another 500 lines, still not quite right]

# Result: Multiple iterations, wasted time, code doesn't match expectations
```

### After: Document-Driven (With This Skill)

```
You: Help me build a personal blog

Claude: Great! Let's use document-driven development to make sure I build
exactly what you need. First, some questions:

1. What's the main purpose of this blog?
2. Who will read it?
3. What does "done" look like for v0.1?
4. What do you NOT want to build?

You: It's for sharing tech articles. Readers are developers. For v0.1 I just
want to render markdown files. No comments, no CMS, no database.

Claude: Perfect. Let me create the documentation first:

**intent.md** - [creates file capturing vision and non-goals]
**spec.md** - [creates file with v0.1 features and acceptance criteria]
**plan.md** - [creates file with tech stack and architecture]

Now I'll generate code based on these documents...
[Generates focused code that matches exactly what user wanted]

# Result: Clear expectations, right output first time, documented for future iterations
```

## Supported Scenarios

| Scenario                    | Support Level                   |
| --------------------------- | ------------------------------- |
| New project (0 to 1)        | Full support                    |
| Feature iteration           | Full support                    |
| Working with existing codebases | Full support                |
| Multi-version products      | Full support (use roadmap.md)   |
| Agentic products            | Full support (runtime documents) |
| Complex SaaS (multi-module) | Partial (consider modular docs) |

## Key Principles

1. **Document First, Code Second** - Never generate code without clear documentation
2. **Trace Problems to Documents** - When code fails, check if it's a spec or plan issue
3. **One Core Goal Per Version** - v0.1, v0.2, v0.3... small steps
4. **Keep Documents and Code in Sync** - Commit them together
5. **Documents are for Communication** - Write for future you and AI
6. **Define the Architecture Spine Before v0.1** - Name what will NOT change across versions, so a thin v0.1 isn't throwaway
7. **Each Version Has a Validation Gate** - Tools: works as specified. Products: retention, usage, or payment — not interest. Don't advance until the gate passes
8. **In Agentic Projects, Documents Can Be the Runtime** - The agent reads and writes them live; keep them human-readable and versioned

## Project Structure

```
document-driven-development/
├── README.md
├── LICENSE
└── skills/
    └── document-driven-development/
        ├── SKILL.md        # Behavior rules + workflows (context-efficient core)
        ├── templates.md    # intent / roadmap / spec / plan templates + example
        └── principles.md   # Philosophy, principles 1-8, anti-patterns
```

## Best Practices

### Do's

- **Start with intent.md** - Even a 5-line intent.md is better than none
- **Define non-goals explicitly** - "No user accounts" prevents scope creep
- **Name the spine before v0.1** - Later versions fill it in, not rebuild it
- **Keep versions small** - v0.1 should be achievable in hours, not days
- **Update docs when requirements change** - Don't just fix code, fix the source of truth
- **Commit docs and code together** - They should always be in sync

### Don'ts

- **Don't skip to code** - Resist the urge to "just start coding"
- **Don't over-document** - plan.md describes WHAT to achieve, not exact code
- **Don't put tech in spec.md** - "User can search" (good) vs "Use Elasticsearch" (put in plan.md)
- **Don't aim for v1.0 immediately** - v0.1 → v0.2 → v0.3 is the way
- **Don't advance past a failed gate** - You'd be building on unvalidated assumptions

### When to Use This Approach

| Situation                             | Recommendation                          |
| ------------------------------------- | --------------------------------------- |
| New project with unclear requirements | Highly recommended                      |
| Adding features to existing project   | Recommended                             |
| Quick bug fix                         | Not needed                              |
| Exploring/prototyping ideas           | Optional (lightweight intent.md only)   |
| Complex multi-module system           | Use modular docs (spec/, plan/ folders) |

## FAQ

### Q: Isn't this slower than just asking AI to write code?

**A:** For trivial tasks, yes. For anything you'll iterate on, no. The time spent on documentation is recovered many times over when you avoid "that's not what I wanted" loops.

### Q: Do I need all the documents?

**A:** For small projects, you can combine them, and roadmap.md only matters for multi-version products. But keeping them separate helps you think at different levels: WHY (intent) → PATH (roadmap) → WHAT (spec) → HOW (plan).

### Q: What if my requirements change mid-project?

**A:** Update the documents first, then update the code. This keeps your documentation as the source of truth and makes it easier for AI to understand the new context.

### Q: Can I use this with other AI tools besides Claude?

**A:** Yes! The methodology works with any AI coding assistant. For non-Claude tools, copy the SKILL.md content into your system prompt.

## Changelog

- **2026-06** - Refreshed for the AI-coding-tool / agent era: deliverable types beyond web apps, roadmap.md bridge layer, architecture-spine principle, per-version validation gates, documents-as-runtime for agentic projects (principles 6-8)
- **2026-03** - Refactored for context efficiency: split into SKILL.md + templates.md + principles.md, added Stop Condition, tightened triggering
- **2026-01** - Initial release v1.0

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Created by **Sujing Shen**

- Blog: <https://www.sagasu.art/>
- Twitter: [@sujingshen](https://x.com/sujingshen)

## Acknowledgments

This skill is based on the "Document-Driven Development" methodology series. The core idea: **generation is cheap, controlled evolution is scarce**.

Read the full methodology series on the [blog](https://www.sagasu.art/).
