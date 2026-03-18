---
name: document-driven-development
description: Guide projects using document-driven development — intent.md (why), spec.md (what), plan.md (how). Activate when user wants to start a new project from scratch, add a significant feature to an existing project, or explicitly mentions intent.md / spec.md / plan.md. Also activate when user describes building something new and has NOT yet defined scope or requirements. Do NOT activate for quick code fixes, one-off scripts, or when a clear spec already exists in the conversation.
---

# Document-Driven Development

Documentation is the single source of truth. Code implements documentation — not the other way around.

## The Three Documents

| Document | Answers | Changes |
|----------|---------|---------|
| `intent.md` | Why & for whom | Rarely |
| `spec.md` | What to build & how users interact | When adding/changing features |
| `plan.md` | How to implement technically | Often, as you learn |

## Workflow

### New Project (0 → 1)

1. **intent.md** — clarify vision, target users, core problem, success criteria, non-goals
2. **spec.md v0.1** — smallest useful version: features, user journeys, acceptance criteria
3. **plan.md v0.1** — tech stack with rationale, file structure, key data models
4. Generate code referencing spec + plan
5. Validate against acceptance criteria; trace failures back to documents

### Adding a Feature (existing project)

1. Check intent.md — usually no change needed
2. Update spec.md — add feature, user journey, acceptance criteria
3. Update plan.md — add technical approach
4. Generate code; commit documents and code together

### Working with an Existing Codebase

1. Document current state in plan.md (tech stack as constraints, file structure)
2. Define changes in spec.md
3. Generate incremental changes that fit the existing structure

## Document Templates

### intent.md
```markdown
# Project Intent

## Vision
[One sentence: what and why]

## Target Users
- Primary: [who, what they need]
- Secondary: [who, what they need]

## Core Problem
[Why build this? Why not existing solutions?]

## Success Criteria
- [ ] [Measurable criterion]

## Non-Goals
- [What you will NOT build]
```

### spec.md
```markdown
# Product Specification — v0.x

## Feature: [Name]
**Description**: [What it does]

**User Journey**:
1. User does [action]
2. System responds with [response]
3. User sees [result]

**Acceptance Criteria**:
- [ ] [Testable condition]

## Non-Functional Requirements
- Performance: [e.g., response < 2s]
- Compatibility: [e.g., Chrome/Firefox latest 2]

## Out of Scope (this version)
- [Future features]
```

### plan.md
```markdown
# Technical Plan — v0.x

## Tech Stack
- [Framework]: [Why this choice]

## File Structure
[directory tree]

## Data Model
[key types/interfaces]

## Implementation Notes
- [Important decision and why]
- [Constraints to be aware of]
```

## Key Principles

**One core goal per version.** v0.1 is a working prototype. v0.2 adds one key capability.

**Spec describes WHAT, not HOW.** "User can search articles" → spec.md. "Use Elasticsearch" → plan.md.

**Non-goals matter as much as goals.** Explicitly stating what you won't build prevents scope creep.

**Trace failures to documents.** When code breaks: spec problem? plan problem? implementation problem? Fix the right layer.

## Gotchas

**Spec gets too technical.** Technology names creeping into spec.md → move them to plan.md. Spec should be readable by a non-engineer.

**Plan.md over-specifies.** Don't write exact code in plan.md. Describe the goal; let Claude find the best implementation. Over-specified plans become outdated fast.

**Skipping intent.md for "simple" projects.** Even a small tool benefits from one paragraph on who it's for and what it won't do. You'll reference it when scope debates come up later.

**Updating code without updating documents.** After any significant implementation decision that differs from plan.md, update plan.md before continuing. Diverged documents are worse than no documents.

**Acceptance criteria that can't be tested.** "The UI should be nice" is not an acceptance criterion. "Translation result appears within 3 seconds" is.

**Version mismatch between spec and plan.** Both should share the same version number. Mismatched versions cause confusion about what's been implemented.

**Writing intent.md after building.** Post-hoc intent is rationalization, not direction. Write it before a line of code — a rough draft beats nothing.
