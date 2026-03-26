---
name: document-driven-development
description: Use when user explicitly asks to build a project from scratch, add features with DDD, or mentions intent.md/spec.md/plan.md.
disable-auto-invoke: true
---

# Document-Driven Development

**Rule: Never generate code before documentation exists.**

## Documents

- `intent.md` — WHY and FOR WHOM (most stable)
- `spec.md` — WHAT to build and user journey (moderately stable)
- `plan.md` — HOW to implement technically (most flexible)

Templates and examples: see `templates.md`
Principles and anti-patterns: see `principles.md`

## Workflow

### A: New Project

1. **Clarify intent** → create `intent.md`
   - What are you building and why?
   - Who is this for?
   - What does "done" look like?
   - What are you NOT building?

2. **Define scope** → create `spec.md` (v0.1)
   - Smallest useful version
   - User journeys and acceptance criteria

3. **Technical plan** → create `plan.md` (v0.1)
   - Tech stack with rationale
   - Architecture and data model

4. **Generate code** based on spec.md + plan.md

5. **Validate** against acceptance criteria → update docs if needed

### B: Feature Iteration

1. Check intent.md — usually no change
2. Update spec.md — add feature + acceptance criteria
3. Update plan.md — add technical approach
4. Generate code → validate → commit docs + code together

### C: Existing Codebase

1. Document current state in plan.md (as constraints)
2. Define changes in spec.md
3. Generate incremental changes respecting existing structure

## Stop Condition

Task is complete when:
- All acceptance criteria in spec.md are met
- Documents and code are committed together
- No undocumented assumptions remain in code
