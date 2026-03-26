# DDD Principles & Anti-Patterns

## Core Philosophy

**Documentation is the Single Source of Truth. Code is the implementation of documentation, not the other way around.**

- Generation is cheap; controlled evolution is scarce
- Documentation is the universal language for human-AI collaboration
- Small steps with continuous validation beats big-bang delivery
- When in doubt, update the document first, then regenerate code

## Document Update Frequency

| Document | Update Frequency | Changes When |
|----------|-----------------|--------------|
| intent.md | Rarely | Project direction fundamentally changes |
| spec.md | Moderately | Adding/changing features |
| plan.md | Often | Technical approach evolves |

## Quick Reference

| Question | Document | Section |
|----------|----------|---------| 
| Why are we building this? | intent.md | Vision, Core Problem |
| Who is this for? | intent.md | Target Users |
| What features to build? | spec.md | Features |
| How do users use it? | spec.md | User Journey |
| How do we know it's done? | spec.md | Acceptance Criteria |
| What tech stack? | plan.md | Tech Stack |
| How is code organized? | plan.md | Architecture |
| What's the data structure? | plan.md | Data Model |

## Key Principles

### 1. Document First, Code Second
Never generate code without clear documentation.

### 2. Trace Problems to Documents
When code doesn't work:
- Spec problem (wrong requirements) → Update spec.md
- Plan problem (wrong approach) → Update plan.md
- Implementation problem → Fix code to match documents

### 3. One Core Goal Per Version
- v0.1: Basic working prototype
- v0.2: Add one key feature
- v0.3: Add another feature

### 4. Keep Documents and Code in Sync
Commit them together.

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| Write code first, document later | Documentation always outdated |
| Over-specify in plan.md | Removes AI's implementation flexibility |
| Put technology choices in spec.md | spec.md is about user needs, not tech |
| Skip versions | Each version should be working software |
| Ignore non-goals | Scope creep starts here |
