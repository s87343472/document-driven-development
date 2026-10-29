#!/usr/bin/env python3
"""Repository self-check. Run: python3 scripts/check.py

Fails (exit 1) if the skill or the READMEs drift out of shape.
Standard library only, so it runs anywhere.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "document-driven-development"
SKILL = SKILL_DIR / "SKILL.md"

# Fields accepted by the Agent Skills standard (and by claude.ai / the Skills API).
# Tool-specific fields would make the skill fail to upload in some places.
PORTABLE_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
SKILL_MAX_LINES = 500
DESCRIPTION_MAX = 1024
READMES = ["README.md", "README.zh-CN.md", "README.ja.md", "README.fr.md"]
ROOT_ALLOWED = {".git", ".github", ".claude-plugin", ".gitignore", "AGENTS.md", "LICENSE", "scripts", "skills", *READMES}

errors = []


def fail(msg):
    errors.append(msg)


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if m:  # top-level keys only; indented lines belong to the previous key
            fields[m.group(1)] = m.group(2).strip()
    return fields


def check_skill():
    text = SKILL.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if fm is None:
        fail("SKILL.md: frontmatter missing or not on the first line")
        return text
    if fm.get("name") != SKILL_DIR.name:
        fail(f"SKILL.md: name must be '{SKILL_DIR.name}', got '{fm.get('name')}'")
    desc = fm.get("description", "")
    if not desc:
        fail("SKILL.md: description is empty")
    elif len(desc) > DESCRIPTION_MAX:
        fail(f"SKILL.md: description is {len(desc)} chars, max {DESCRIPTION_MAX}")
    extra = set(fm) - PORTABLE_FIELDS
    if extra:
        fail(f"SKILL.md: non-portable frontmatter fields {sorted(extra)}")
    lines = text.count("\n") + 1
    if lines > SKILL_MAX_LINES:
        fail(f"SKILL.md: {lines} lines, max {SKILL_MAX_LINES}")
    return text


def check_references(skill_text):
    mentioned = set(re.findall(r"references/([\w.-]+\.md)", skill_text))
    present = {p.name for p in (SKILL_DIR / "references").glob("*.md")}
    for name in sorted(mentioned - present):
        fail(f"SKILL.md mentions references/{name}, which does not exist")
    for name in sorted(present - mentioned):
        fail(f"references/{name} is never mentioned in SKILL.md, so no agent will load it")


def check_links():
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = target.split("#", 1)[0]
            if path and not (md.parent / path).exists():
                fail(f"{md.relative_to(ROOT)}: broken link -> {target}")


def check_readmes():
    counts = {}
    for name in READMES:
        p = ROOT / name
        if not p.exists():
            fail(f"{name} is missing")
            continue
        text = p.read_text(encoding="utf-8")
        counts[name] = len(re.findall(r"^## ", text, flags=re.M))
        for other in READMES:
            if other != name and other not in text:
                fail(f"{name}: language switcher has no link to {other}")
    if len(set(counts.values())) > 1:
        fail(f"READMEs have different numbers of sections, out of sync: {counts}")


def check_marketplace(skill_text):
    path = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        fail(f"marketplace.json: cannot read ({e})")
        return
    m = re.search(r'^  version: "([^"]+)"', skill_text, flags=re.M)
    skill_version = m.group(1) if m else None
    if data.get("metadata", {}).get("version") != skill_version:
        fail(f"marketplace.json version {data.get('metadata', {}).get('version')} != SKILL.md version {skill_version}")
    for plugin in data.get("plugins", []):
        for s in plugin.get("skills", []):
            if not (ROOT / s / "SKILL.md").exists():
                fail(f"marketplace.json: plugin '{plugin.get('name')}' lists {s}, which has no SKILL.md")


def check_root():
    for p in ROOT.iterdir():
        if p.name not in ROOT_ALLOWED:
            fail(f"unexpected file at repo root: {p.name} (add it to ROOT_ALLOWED if intended)")


def main():
    skill_text = check_skill()
    check_references(skill_text)
    check_marketplace(skill_text)
    check_links()
    check_readmes()
    check_root()
    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("PASS: skill frontmatter, size, references, marketplace, links, READMEs, repo root")


if __name__ == "__main__":
    main()
