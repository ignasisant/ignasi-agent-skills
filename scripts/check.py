#!/usr/bin/env python3
"""Pre-push check: every skill folder has a SKILL.md with name/description frontmatter, and JSON is valid."""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
errs = []
m = json.loads((root/".claude-plugin/marketplace.json").read_text())
for p in m["plugins"]:
    d = root/p["source"]
    json.loads((d/".claude-plugin/plugin.json").read_text())
    for sk in (d/"skills").iterdir():
        f = sk/"SKILL.md"
        if (sk/"PUT_SKILL_MD_HERE.txt").exists(): errs.append(f"{sk.name}: placeholder still present")
        if not f.exists(): errs.append(f"{sk.name}: missing SKILL.md"); continue
        head = f.read_text().split("---")
        if len(head) < 3 or "name:" not in head[1] or "description:" not in head[1]:
            errs.append(f"{sk.name}: SKILL.md needs name/description frontmatter")
print("\n".join(errs) or "OK: all skills ready")
sys.exit(1 if errs else 0)
