# DDD Principles & Anti-Patterns

## Core Philosophy

**Documentation is the Single Source of Truth. Code is the implementation of documentation, not the other way around.**

- Generation is cheap; controlled evolution is scarce. AI coding tools now generate whole versions near-instantly, which makes this MORE true: the bottleneck is no longer typing code, it's deciding what should exist. Documents are where that deciding happens.
- Documentation is the universal language for human-AI collaboration
- Small steps with continuous validation beats big-bang delivery
- When in doubt, update the document first, then regenerate code
- The deliverable is not always a web app. Skills, agents, MCP servers, CLI tools, and .md methodologies all use the same document system.

## Document Update Frequency

| Document | Update Frequency | Changes When |
|----------|-----------------|--------------|
| intent.md | Rarely | Project direction fundamentally changes |
| roadmap.md | Occasionally | The version path or architecture spine changes |
| spec.md | Moderately | Adding/changing features |
| plan.md | Often | Technical approach evolves |

## Quick Reference

| Question | Document | Section |
|----------|----------|---------|
| Why are we building this? | intent.md | Vision, Core Problem |
| Who is this for? | intent.md | Target Users |
| What stays fixed across versions? | roadmap.md | Architecture Spine |
| What's each version for? | roadmap.md | Version Goals & Gates |
| What features to build? | spec.md | Features |
| How do users use it? | spec.md | User Journey |
| How do we know it's done? | spec.md | Acceptance Criteria, Validation Gate |
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

### 5. Documents are for Communication
Write documents so that future you can understand past decisions, AI can generate accurate code, and others can quickly understand the project.

### 6. Define the Architecture Spine Before v0.1
Before building the first version, name the parts of the architecture that will NOT change across versions (the invariant layers and their interfaces). Later versions fill the spine in; they don't rebuild it. This is what stops a thin v0.1 from being throwaway, and stops the architecture from turning into a mess as features pile up. Record the spine in plan.md (and roadmap.md for multi-version products).

### 7. Each Version Has a Validation Gate
A version isn't "done" when it passes acceptance criteria — it's done when it passes its gate. For tools, the gate is "does it work as specified." For products, the gate must include a real-world signal: retention, usage, or payment — not interest, not a waitlist. Do not advance to the next version until the current version's gate passes. State each version's gate in spec.md.

### 8. In Agentic Projects, Documents Can Be the Runtime, Not Just the Spec
When the product itself is an agent, the spec/standard documents can double as the live, inspectable layer the agent reads and writes at runtime — not only a build-time blueprint. Keep them human-readable and versioned so the user can see, and edit, how the agent thinks.

## Build-Time Documents vs Runtime Documents

intent / roadmap / spec / plan are **build-time**: humans author them to decide what to build. In agentic or co-evolving products there is a second kind — **runtime documents**: the standard / memory / state files the running product itself reads and writes (the "middle layer"). Keep them versioned and human-readable so the user can see, and edit, how the product thinks.

The two version axes do not share numbering: the product has versions (v0.1, v0.2 ...), and a runtime document has its own (e.g. a user's standard going v1 → v2 as they level up). Keep them separate.

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| Write code first, document later | Documentation always outdated |
| Over-specify in plan.md | Removes AI's implementation flexibility |
| Put technology choices in spec.md | spec.md is about user needs, not tech |
| Skip versions | Each version should be working software |
| Ignore non-goals | Scope creep starts here |
| Ship v0.1 without a spine | Thin first version becomes throwaway code |
| Advance without passing the gate | Building on unvalidated assumptions |
