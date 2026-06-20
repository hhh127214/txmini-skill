# db_report Meta-Testcase Design

## Goal

This meta-testcase checks whether the db_report evaluation set itself is high quality. It follows the `llm-rubric` style: an evaluator reviews `ideal_state.md`, `rubrics.yaml`, `testcases.yaml`, evidence, and report outputs, then returns a structured judgement.

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
| Coverage | 30 | Covers normal, abnormal, boundary, process, and anti-hallucination paths across single/comparison/iteration/custom. |
| Determinism | 25 | Each case has clear pass/fail criteria and observable outputs. |
| Reproducibility | 20 | Inputs, official resources, execution conditions, and evidence locations are explicit. |
| Non-overlap | 10 | Cases cover distinct risks and are not redundant. |
| Automation Readiness | 15 | YAML structure, rubric references, and expected outputs support semi-automatic scoring. |

## Meta-Testcase Prompt

Evaluate the db_report evaluation set. Check whether it can reliably judge the current `db_report_skill` without relying on removed historical features. Use the rubric above.

Required checks:

1. At least 5 cases exist; 10 are expected.
2. Cases cover all four report types: `single`, `comparison`, `iteration`, `custom`.
3. Cases include failure paths for no data and missing files.
4. Cases include anti-hallucination checks for unsupported metrics.
5. Each case has input, expected output, judge conditions, priority, and rubric references.
6. Official `test-resource` references are clear and do not require repackaging.
7. Scoring dimensions map to observable artifacts.
8. The test set does not require old deleted scripts such as `min_delivery_check.py`.

## Failure Examples

The meta-testcase should fail or strongly penalize the evaluation set if:

- cases are only topic names without executable inputs;
- expected outputs are vague or subjective;
- no failure-path case exists;
- judge criteria require unavailable internal APIs;
- no evidence path or scoring process is defined;
- comparison and iteration cases are indistinguishable.

