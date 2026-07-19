---
name: document-driven-development
description: Use when user explicitly asks to build a project from scratch, add features with DDD, or mentions intent.md/spec.md/plan.md.
disable-auto-invoke: true
---

# Document-Driven Development

> Refreshed 2026-06 for the AI-coding-tool / agent era. Core (intent → spec → plan, document-first) unchanged. Added: deliverable types beyond web apps, the architecture-spine principle, per-version validation gates, and documents-as-runtime for agentic projects.

**Rule: Never generate code before documentation exists.**

The deliverable is not always a web app. Skills (.skill), agents, MCP servers, CLI tools, and .md methodologies all use the same document system.

## Documents

- `intent.md` — WHY and FOR WHOM (most stable)
- `roadmap.md` — bridge layer for multi-version products: the invariant architecture spine, plus each version's core goal and validation gate (optional for single-version projects)
- `spec.md` — WHAT to build and user journey (moderately stable)
- `plan.md` — HOW to implement technically (most flexible)

These are build-time documents. Agentic products may also have runtime documents the product itself reads and writes — see `principles.md`.

Templates and examples: see `templates.md`
Principles and anti-patterns: see `principles.md`

## Workflow

### A: New Project

1. **Clarify intent** → create `intent.md`
   - What are you building and why?
   - Who is this for?
   - What does "done" look like?
   - What are you NOT building?

2. **Map the path** (multi-version products) → create `roadmap.md`
   - Name the architecture spine: what will NOT change across versions
   - One core goal and one validation gate per version

3. **Define scope** → create `spec.md` (v0.1)
   - Smallest useful version
   - User journeys and acceptance criteria
   - This version's validation gate

4. **Technical plan** → create `plan.md` (v0.1)
   - Tech stack with rationale
   - Architecture (record the spine here) and data model

5. **Generate code** based on spec.md + plan.md

6. **Validate** against acceptance criteria and the version gate → update docs if needed

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
- The version's validation gate has passed (do not advance otherwise)
- Documents and code are committed together
- No undocumented assumptions remain in code
