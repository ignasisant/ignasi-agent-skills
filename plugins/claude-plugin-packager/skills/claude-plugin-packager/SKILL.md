---
name: claude-plugin-packager
description: Package skills, commands, subagents, hooks and MCP servers into a Claude Code plugin and marketplace, then validate and test-install it. Use when the user wants to ship or share their Claude Code setup as a plugin.
---

# Claude Plugin Packager

Turn loose Claude Code assets into an installable plugin.

## Workflow
1. **Inventory** what exists: skills, slash commands, subagents, hooks, MCP servers.
2. **Layout** the plugin:
```
my-plugin/
  .claude-plugin/plugin.json
  skills/<name>/SKILL.md
  commands/  agents/  hooks/hooks.json  .mcp.json
```
3. **Paths.** Use ${CLAUDE_PLUGIN_ROOT} in hooks and MCP configs. Never use absolute or home-directory paths.
4. **Marketplace.** Add .claude-plugin/marketplace.json at the repo root listing each plugin with name, source, description and version.
5. **Version.** Use semver and keep a CHANGELOG.md.
6. **README.** Include the two install commands: /plugin marketplace add <user>/<repo> and /plugin install <name>@<marketplace>.

## Validate before shipping
- All JSON parses.
- Every SKILL.md has name and description frontmatter.
- No absolute paths and no secrets (keys, tokens, .env content).
- Hook scripts are executable.

## Test-install
Run /plugin marketplace add ./ then /plugin install <name>@<marketplace> in a clean session and confirm each skill and command appears.
