---
name: document-driven-development
description: |
  Help users build products using a document-driven approach. Activate this skill when:
  - User wants to create a new project or product
  - User wants to add features or iterate on existing project
  - User asks how to organize requirements for AI collaboration
  - User mentions intent.md, spec.md, plan.md
  - User asks about document-driven development
  Guide users to establish a three-layer documentation system before writing code.
---

# Document-Driven Development Skill

## Core Philosophy

**Documentation is the Single Source of Truth. Code is the implementation of documentation, not the other way around.**

Key principles:
- Generation is cheap; controlled evolution is scarce
- Documentation is the universal language for human-AI collaboration
- Small steps with continuous validation beats big-bang delivery
- When in doubt, update the document first, then regenerate code

## The Three-Layer Documentation System

### 1. intent.md (Intent Layer) - Most Stable

**Purpose**: Answer WHY and FOR WHOM

**Must Include**:
- **Project Vision**: One sentence describing what you're building and why
- **Target Users**: Who will use this? What are their needs?
- **Core Problem**: What problem does this solve? Why not use existing solutions?
- **Success Criteria**: How do you know the project succeeded?
- **Non-Goals**: What you explicitly will NOT do (equally important)

**Template**:
```markdown
# Project Intent

## Vision
[One sentence: what and why]

## Target Users
### Primary User
- Who: [description]
- Needs: [what they need]

### Secondary User (if any)
- Who: [description]
- Needs: [what they need]

## Core Problem
### Why build this?
[The problem you're solving]

### Why not existing solutions?
[Why current options don't work]

## Success Criteria
- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]

## Non-Goals
- [What you will NOT build]
- [Features you explicitly exclude]
```

**Update Frequency**: Rarely. Only when project direction fundamentally changes.

---

### 2. spec.md (Specification Layer) - Moderately Stable

**Purpose**: Answer WHAT to build and HOW users will use it

**Must Include**:
- **Feature List**: What features does this version include?
- **User Journey**: Step-by-step how users interact with each feature
- **Acceptance Criteria**: Testable conditions for each feature
- **Non-Functional Requirements**: Performance, security, accessibility

**Template**:
```markdown
# Product Specification

## Version
[Version number, e.g., v0.1]

## Features

### Feature 1: [Name]
**Description**: [What it does]

**User Journey**:
1. User does [action]
2. System responds with [response]
3. User sees [result]

**Acceptance Criteria**:
- [ ] [Testable condition 1]
- [ ] [Testable condition 2]

### Feature 2: [Name]
[Same structure]

## Non-Functional Requirements

### Performance
- [e.g., Page load < 2 seconds]

### Compatibility
- [e.g., Support Chrome, Firefox, Safari latest 2 versions]

## Out of Scope (This Version)
- [Features planned for future versions]
```

**Key Rule**: spec.md describes WHAT, never HOW (no technology choices here).

**Update Frequency**: When adding/changing features.

---

### 3. plan.md (Plan Layer) - Most Flexible

**Purpose**: Answer HOW to implement technically

**Must Include**:
- **Tech Stack**: Frameworks, libraries, tools with rationale
- **Architecture**: System structure, file organization
- **Data Model**: Data structures and relationships
- **Key Implementation Details**: Important technical decisions

**Template**:
```markdown
# Technical Plan

## Version
[Corresponding to spec.md version]

## Tech Stack

### Framework
- [Name]: [Why this choice]

### Styling
- [Name]: [Why this choice]

### Other Tools
- [Tool]: [Purpose]

## Architecture

### File Structure
```
project/
├── [folder]/
│   └── [files]
└── [other folders]
```

### Component Design
- [Component 1]: [Responsibility]
- [Component 2]: [Responsibility]

## Data Model

### [Entity Name]
- field1: type - description
- field2: type - description

## Implementation Notes
- [Important technical decision and why]
- [Constraints to be aware of]

## Performance Considerations
- [Optimization strategies]
```

**Update Frequency**: Often. Technical approach may change as you learn more.

---

## Workflow

### Workflow A: New Project (0 to 1)

**Phase 1: Clarify Intent**
Before any coding, help user think through:
1. What are you building and why?
2. Who is this for?
3. What does "done" look like?
4. What are you NOT building?

→ Output: `intent.md`

**Phase 2: Define Minimum Viable Scope**
1. What's the smallest useful version (v0.1)?
2. What features does it include?
3. How will users interact with it?
4. How do we verify it works?

→ Output: `spec.md` (v0.1)

**Phase 3: Technical Planning**
1. What tech stack fits the requirements?
2. How should the code be organized?
3. What are the key data structures?

→ Output: `plan.md` (v0.1)

**Phase 4: Generate Code**
Based on the three documents:
1. Reference spec.md for WHAT to build
2. Follow plan.md for HOW to build
3. Verify against acceptance criteria

**Phase 5: Validate**
1. Check against spec.md acceptance criteria
2. If issues found, trace back to documents
3. Update documents if needed, then regenerate

---

### Workflow B: Feature Iteration (Adding to Existing Project)

**Step 1: Understand the Change**
- What new capability is needed?
- Does this change the project's core intent?

**Step 2: Update Documents**
1. Check intent.md - usually no change needed
2. Update spec.md - add new feature description and acceptance criteria
3. Update plan.md - add technical implementation approach

**Step 3: Generate Code**
- Provide AI with updated spec.md and plan.md
- Reference existing code structure from plan.md
- Ensure consistency with existing implementation

**Step 4: Validate and Commit**
- Test against new acceptance criteria
- Commit documents and code together

---

### Workflow C: Working with Existing Templates/Projects

When user has an existing codebase or template:

**Step 1: Document Current State**
Create or update plan.md with:
- Existing tech stack (as constraints)
- Current file structure
- What can and cannot be changed

**Step 2: Define Changes**
Update spec.md with:
- New features to add
- Modifications to existing features
- What stays the same

**Step 3: Generate Incremental Changes**
- AI generates code that fits existing structure
- Respect constraints documented in plan.md

---

## Key Principles

### 1. Document First, Code Second
Never generate code without clear documentation. When user asks "help me build X":
1. First ask clarifying questions
2. Help create/update documents
3. Then generate code based on documents

### 2. Trace Problems to Documents
When code doesn't work as expected:
- Is it a spec problem? (Wrong requirements) → Update spec.md
- Is it a plan problem? (Wrong approach) → Update plan.md
- Is it an implementation problem? → Fix code to match documents

### 3. One Core Goal Per Version
Each version should have ONE primary objective:
- v0.1: Basic working prototype
- v0.2: Add one key feature
- v0.3: Add another feature
- ...

Don't try to do everything at once.

### 4. Keep Documents and Code in Sync
- When code changes, documents must update
- When documents change, code must follow
- Commit them together

### 5. Documents are for Communication
Write documents so that:
- Future you can understand past decisions
- AI can generate accurate code
- Others can quickly understand the project

---

## Anti-Patterns to Avoid

### Don't: Write code first, document later
This leads to documentation that's always outdated.

### Don't: Over-specify in documents
plan.md should describe WHAT to achieve, not exact code. Let AI figure out the best implementation.

### Don't: Put technology in spec.md
spec.md is about user needs, not technical solutions. "User can search articles" (good) vs "Use Elasticsearch for search" (belongs in plan.md).

### Don't: Skip versions
Don't jump from v0.1 to v1.0. Each version should be working software.

### Don't: Ignore non-goals
Explicitly stating what you WON'T do is as important as what you will do.

---

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

---

## Example: Minimal Blog Project

### intent.md (excerpt)
```markdown
## Vision
A minimal personal blog for sharing technical articles, demonstrating document-driven development.

## Target Users
- Primary: Myself (writer) - need simple publishing workflow
- Secondary: Readers - need good reading experience

## Success Criteria
- [ ] Publish article in < 5 minutes
- [ ] Page load < 2 seconds
- [ ] Mobile-friendly

## Non-Goals
- No comments system
- No user accounts
- No CMS backend
```

### spec.md v0.1 (excerpt)
```markdown
## Features

### Feature 1: Article Rendering
**Description**: Display markdown articles as formatted web pages

**User Journey**:
1. User visits /posts/[slug]
2. System renders markdown content
3. User sees formatted article with title, date, content

**Acceptance Criteria**:
- [ ] Markdown renders correctly (headings, code, lists)
- [ ] Article metadata displays (title, date)
- [ ] 404 for non-existent articles
```

### plan.md v0.1 (excerpt)
```markdown
## Tech Stack
- Next.js 14 (App Router): SSG support, good DX
- Tailwind CSS: Utility-first, fast styling
- gray-matter: Parse markdown frontmatter

## File Structure
```
/content/posts/*.md   # Article files
/app/posts/[slug]/    # Article pages
/lib/posts.ts         # Article utilities
```
```

This example shows the essence - just enough detail to guide implementation, not a complete specification.
