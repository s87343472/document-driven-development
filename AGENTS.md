# Working on this repository

This repo ships one skill: `skills/document-driven-development/`.

- `SKILL.md` holds the core behaviour and must stay under 500 lines. Detail goes into `references/`, and every reference file must be mentioned in `SKILL.md`.
- Frontmatter uses only portable fields: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
- The four READMEs (en, zh-CN, ja, fr) carry the same sections. Change one, change all.
- Run `python3 scripts/check.py` before every commit. CI runs it too.
