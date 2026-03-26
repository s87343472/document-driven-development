# Document Templates

## intent.md Template

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

---

## spec.md Template

```markdown
# Product Specification

## Version
[e.g., v0.1]

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

## Non-Functional Requirements

### Performance
- [e.g., Page load < 2 seconds]

### Compatibility
- [e.g., Support Chrome, Firefox, Safari latest 2 versions]

## Out of Scope (This Version)
- [Features planned for future versions]
```

**Key Rule**: spec.md describes WHAT, never HOW (no technology choices here).

---

## plan.md Template

```markdown
# Technical Plan

## Version
[Corresponding to spec.md version]

## Tech Stack

### Framework
- [Name]: [Why this choice]

### Styling
- [Name]: [Why this choice]

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

## Data Model

### [Entity Name]
- field1: type - description

## Implementation Notes
- [Important technical decision and why]
- [Constraints to be aware of]
```

---

## Example: Minimal Blog Project

### intent.md (excerpt)
```markdown
## Vision
A minimal personal blog for sharing technical articles.

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
/content/posts/*.md   # Article files
/app/posts/[slug]/    # Article pages
/lib/posts.ts         # Article utilities
```
