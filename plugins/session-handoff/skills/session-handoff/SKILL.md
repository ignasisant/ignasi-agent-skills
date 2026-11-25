---
name: session-handoff
description: Save a session's goal, decisions, files, commands and next steps into a verified HANDOFF.md before context runs out, then resume from it in a new session. Use before /clear, compaction or end of day, or when the user says to resume.
---

# Session Handoff

## Save
Check git status, the current branch and recent test results first, then write HANDOFF.md:
- **Goal**: one sentence.
- **State**: what works, what is half done.
- **Decisions**: each with the reason.
- **Dead ends**: what failed and why, so it is not retried.
- **Gotchas**: traps found.
- **Files touched**: paths with one line each.
- **Commands**: the ones that work (build, test, run).
- **Next step**: one exact action.

Keep it under 80 lines. Never include secrets.

## Resume
1. Read HANDOFF.md.
2. Verify it against git (branch, last commits, uncommitted files) and run the tests.
3. Report any drift between the file and reality.
4. Continue from Next step.
