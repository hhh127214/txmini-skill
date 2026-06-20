# tracingclaw_finance Meta-Testcase Result

## Evaluation Output

```json
{
  "reason": "tracingclaw_finance evaluation set covers financial statements, quotes, percentage change, announcements, news, candidate-answer scoring, refusal behavior, unsupported internal claims, period mismatch, missing EM_API_KEY degradation, and cross-source conflict resolution. Evidence is source-backed and outputs preserve currency/date/period/source口径.",
  "score": 98,
  "pass": true
}
```

## Dimension Scores

| Dimension | Weight | Score | Reason |
|---|---:|---:|---|
| Coverage | 30 | 30 | Covers structured finance, quote/kline, announcement/news, candidate scoring, unknown company, unsupported source, period mismatch, missing-key path, and source conflict. |
| Determinism | 25 | 24 | Questions, candidate answers, pass/fail criteria, required tools, and expected output shape are explicit. News claim strength remains slightly subjective. |
| Reproducibility | 20 | 20 | Raw command outputs, inputs, command metadata, answer files, and environment-key failure evidence are recorded. |
| Non-overlap | 10 | 9 | Cases target distinct financial verification risks; several Tencent-based cases share the same ticker by design for controlled data. |
| Automation Readiness | 15 | 15 | YAML is parseable, rubric-linked, and now includes a traceability matrix plus explicit evidence paths for each risk. |

## Required Checks

| Check | Result |
|---|---|
| At least 5 cases exist | Pass: 11 cases |
| No-candidate and candidate-answer modes included | Pass |
| Structured data and announcement/news checks included | Pass |
| Source traceability and financial口径 required | Pass |
| Refusal behavior included | Pass: unknown company, unsupported internal claim, missing key |
| Temporal mismatch detection included | Pass |
| Cross-source conflict handling included | Pass: FIN-TC012 |
| Tool requirements declared | Pass |
| No internal links or private APIs required | Pass |

## Conclusion

The tracingclaw_finance evaluation set passes the meta-testcase threshold. The added missing-key case improves robustness by verifying that the suite can distinguish a valid external-tool failure from an unsupported financial answer.
