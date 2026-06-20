# Skill Evaluation Submission

## Project Scope

This package contains the evaluation framework for two target Skills:

- `db_report`: database performance report generation.
- `tracingclaw_finance`: financial answer verification and fact checking.

The goal is not to develop or repair the Skills. The goal is to define ideal behavior, scoring rubrics, executable test cases, execution evidence, and meta-testcases for judging the quality of the evaluation set itself.

## Package Structure

```text
skill_eval_submission/
├── 00_核心提交文件/
│   ├── db_report_理想态规范.md
│   ├── db_report_评分规则_Rubrics.yaml
│   ├── db_report_测试用例集.yaml
│   ├── db_report_元测试设计.md
│   ├── tracingclaw_finance_理想态规范.md
│   ├── tracingclaw_finance_评分规则_Rubrics.yaml
│   ├── tracingclaw_finance_测试用例集.yaml
│   ├── tracingclaw_finance_元测试设计.md
│   └── 全链路追踪矩阵.md
├── README.md
├── traceability_matrix.md
├── final_validation_report.md
├── db_report/
│   ├── skill_analysis.md
│   ├── ideal_state.md
│   ├── rubrics.yaml
│   ├── testcases.yaml
│   ├── meta_testcase_design.md
│   ├── meta_testcase_result.md
│   ├── test_report.md
│   ├── test_report.html
│   ├── case_scores.csv
│   ├── outputs/
│   ├── screenshots/
│   └── evidence/
└── tracingclaw_finance/
    ├── skill_analysis.md
    ├── ideal_state.md
    ├── rubrics.yaml
    ├── testcases.yaml
    ├── meta_testcase_design.md
    ├── meta_testcase_result.md
    ├── test_report.md
    ├── test_report.html
    ├── case_scores.csv
    ├── outputs/
    ├── screenshots/
    └── evidence/
```

The package also includes `traceability_matrix.md` and `final_validation_report.md` at the root level.

`00_核心提交文件/` contains Chinese-named copies of the four core deliverables requested by the mentor: ideal state, rubrics, testcases, and meta-testcase design. The original per-Skill directories keep the complete execution reports, scores, outputs, screenshots, and evidence.

`traceability_matrix.md` shows the design chain from Skill capability analysis to ideal-state requirements, rubrics, test cases, and execution evidence.

## External Resources

This submission references the official resources provided with the assignment. These files are not duplicated in this zip package.

For `db_report`, test cases reference:

- `db_report/test-resource/mock_tdsqlb_v22_7_2.log`
- `db_report/test-resource/mock_tdsqlb_v22_7_3.log`
- `db_report/test-resource/mock_records_aggregation.json`
- `db_report/test-resource/mock_iteration_history.json`

For `tracingclaw_finance`, execution requires the two tool Skills provided by the assignment:

- `westock-data`
- `mx-finance-search`

`mx-finance-search` requires `EM_API_KEY`. Cases that depend on this key record the requirement explicitly. Cases for missing-key degradation are also included.

## Scoring Target

`db_report` has 10 executed test cases. `tracingclaw_finance` has 12 executed test cases, including one explicit missing-`EM_API_KEY` degradation case and one cross-source conflict case. The evaluation set is considered ready when:

- all P0 cases have executable input and deterministic judge criteria;
- execution evidence is recorded in `outputs/`, `screenshots/`, or `evidence/`;
- `case_scores.csv` is filled after execution;
- the meta-testcase score is at least 80/100.
