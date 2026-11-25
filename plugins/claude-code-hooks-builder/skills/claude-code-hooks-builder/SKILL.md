---
name: claude-code-hooks-builder
description: Design, write and test Claude Code hooks. Use when the user wants to auto-format or test after edits, block risky commands, protect secret files, inject context at session start, or get desktop alerts.
---

# Claude Code Hooks Builder

## Events
PreToolUse, PostToolUse, UserPromptSubmit, Stop, SessionStart, Notification, PreCompact.

## Settings shape (.claude/settings.json)
```json
{"hooks":{"PreToolUse":[{"matcher":"Bash","hooks":[{"type":"command","command":"./.claude/hooks/guard.sh"}]}]}}
```

## How hooks behave
- The hook receives a JSON event on stdin. Parse it with jq.
- Exit 0 allows. Exit 2 blocks and sends stderr back to Claude. Other non-zero codes are non-blocking errors.

## Workflow
1. Ask which event and which action the user wants.
2. Write a small script: read stdin with jq, quote every variable, fail closed for blocking guards.
3. Keep it fast. Slow hooks (full test suite) belong on Stop, not on every edit.
4. Test each hook by piping a sample event into the script and checking the exit code.
5. Add the hook to settings and show the final JSON.

## Common hooks
- Block rm -rf and force pushes (PreToolUse, Bash).
- Refuse edits to .env and key files (PreToolUse, Edit|Write).
- Format after edits (PostToolUse, Edit|Write).
- Run tests before Claude stops (Stop).
