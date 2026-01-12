# Document-Driven Development

A Claude Code skill that teaches AI to help you build products using a document-driven approach.

## What is Document-Driven Development?

**Documentation is the Single Source of Truth. Code is the implementation of documentation.**

Instead of letting AI generate code based on vague requirements, this skill guides you to:

1. **Think first** - Clarify intent, scope, and success criteria
2. **Document second** - Create structured documentation
3. **Code third** - Generate code based on clear specifications

## The Three-Layer Documentation System

| Layer | File | Purpose | Stability |
|-------|------|---------|-----------|
| Intent | `intent.md` | WHY and FOR WHOM | Rarely changes |
| Specification | `spec.md` | WHAT to build | Changes per feature |
| Plan | `plan.md` | HOW to implement | Changes often |

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

Copy the content of `skills/document-driven-development/SKILL.md` into your system prompt or project instructions.

## Usage

Once installed, Claude will automatically apply this methodology when you:

- Say "I want to build a [project]"
- Ask to add features to an existing project
- Mention `intent.md`, `spec.md`, or `plan.md`
- Ask about organizing requirements for AI collaboration

### Example Conversation

```
You: I want to build a personal blog

Claude: Great! Let's use document-driven development. First, let me help you
clarify the intent:

1. What's the main purpose of this blog?
2. Who is your target audience?
3. What does success look like?
4. What features do you NOT want?

[Claude guides you through creating intent.md, spec.md, and plan.md
before generating any code]
```

## Supported Scenarios

| Scenario | Support Level |
|----------|--------------|
| New project (0 to 1) | Full support |
| Feature iteration | Full support |
| Working with templates | Full support |
| Complex SaaS (multi-module) | Partial (consider modular docs) |

## Key Principles

1. **Document First, Code Second** - Never generate code without clear documentation
2. **Trace Problems to Documents** - When code fails, check if it's a spec or plan issue
3. **One Core Goal Per Version** - v0.1, v0.2, v0.3... small steps
4. **Keep Documents and Code in Sync** - Commit them together
5. **Documents are for Communication** - Write for future you and AI

## Project Structure

```
document-driven-development/
├── README.md
├── LICENSE
└── skills/
    └── document-driven-development/
        └── SKILL.md
```

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

This skill is based on the "Document-Driven Development" methodology series. The core idea: **generation is cheap, controlled evolution is scarce**.
