---
name: prompt-eval-harness
description: Build an eval suite for any system prompt, skill or agent. Use when the user wants to test, compare or regression-check prompts, models or agents with realistic and adversarial cases, code and LLM-judge graders, and cost and latency reports.
---

# Prompt Eval Harness

Build a repeatable eval suite so prompt changes are measured, not guessed.

## Workflow
1. **Criteria.** Ask what good means (correctness, format, tone, safety). Write each as a gradable check with a clear pass rule.
2. **Cases.** Create evals/cases.jsonl with 20-50 cases: typical, edge, adversarial and refusal. Each case has id, tag, input and expected or rubric. Freeze 20% as a held-out split.
3. **Graders.** Use code graders first (JSON schema, regex, required fields). Use an LLM judge only for subjective criteria: temperature 0, 1-5 rubric, written reason.
4. **Runner.** Write a Python or TypeScript script that runs every case for each variant (prompt version x model) with concurrency and response caching. Save raw outputs in evals/results/.
5. **Report.** One table per variant: pass rate, pass rate per tag, p95 latency, cost per 1k cases. List the 5 worst cases with their failure mode.
6. **Regression.** Save the best run as baseline. Flag any tag that drops more than 5 points.

## Rules
- Never tune the prompt on the held-out split.
- Check cases for duplicates and leaked answers.
- With fewer than 30 cases per tag, say differences may be noise.
- Read API keys from environment variables; never write them to files.
