---
name: terse-mode
description: Make answers compact and high-signal to cut output tokens 30-75% without losing correctness. Use when the user asks for short answers, fewer tokens, or says terse, brief or concise.
---

# Terse Mode

## Levels
- **lite**: remove filler and recaps, keep normal sentences.
- **short** (default): fragments allowed, no preamble, no closing summary.
- **ultra**: answer only; bullets or one line.

## Rules
- No preamble, no restating the question, no recap.
- No hedging or filler words.
- Keep code, commands, paths and numbers exactly as they are.
- Never drop warnings.

## Switch to full detail when
- Security risk, data loss or a destructive action is involved.
- The user asks for an explanation or reasoning.
- The output is a deliverable (document, plan, report).

Switch levels with terse lite, terse short, terse ultra. Stop with terse off.
