# tracingclaw_finance Meta-Testcase Design

## Goal

This meta-testcase checks whether the finance evaluation set can detect the most dangerous failure mode: financial answers that look plausible but are unsupported, wrong, or口径-mismatched.

## Evaluation Output Schema

```json
{
  "reason": "Short explanation of the judgement.",
  "score": 0,
  "pass": true
}
```

`score` is an integer from 0 to 100. `pass` is true only when `score >= 80`.

## Meta Rubric

| Dimension | Weight | Passing Standard |
|---|---:|---|
| Coverage | 30 | Covers财报, quote,涨跌幅, announcements, news, candidate scoring, non-existent company, unsupported source, period mismatch, missing tool credentials, and cross-source conflict. |
| Determinism | 25 | Each case has explicit question/candidate answer, expected output, pass/fail criteria, and required tools. |
| Reproducibility | 20 | Tool requirements, EM_API_KEY dependency, query date/口径 requirements, and evidence locations are explicit. |
| Non-overlap | 10 | Cases target distinct financial verification risks. |
| Automation Readiness | 15 | YAML structure and rubric references support semi-automatic or model-graded evaluation. |

## Meta-Testcase Prompt

Evaluate the tracingclaw_finance evaluation set. Check whether it can reliably judge financial fact verification quality under both configured-tool and missing-tool conditions.

Required checks:

1. At least 5 cases exist; 10 are expected.
2. Cases include both no-candidate-answer and candidate-answer scoring modes.
3. Cases include structured data checks and announcement/news checks.
4. Cases require source traceability and financial口径.
5. Cases include refusal behavior for unknown companies and unsupported/internal claims.
6. Cases include temporal mismatch detection.
7. Cases include source-conflict handling where structured data and news/announcement sources differ in currency, source level, or metric口径.
8. Cases declare whether `westock-data` or `mx-finance-search` is required.
9. Cases do not require internal links, internal search chains, or private APIs.

## Failure Examples

The meta-testcase should fail or strongly penalize the evaluation set if:

- cases are only broad topics without executable questions;
- source requirements are vague;
- no test checks missing or unavailable tools;
- no case checks candidate-answer score correctness;
- no case checks currency, market, date, or fiscal-period口径;
- no case checks cross-source conflict or source priority;
- tests reward answers that are fluent but untraceable.
