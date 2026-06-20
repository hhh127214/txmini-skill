# Skill Evaluation Traceability Matrix

This matrix explains how skill analysis findings are translated into ideal-state requirements, rubric dimensions, test cases, and execution evidence.

## db_report

| Skill Capability / Risk | Ideal-State Requirement | Rubric Dimension | Test Cases | Evidence |
|---|---|---|---|---|
| Local performance log ingestion | Correctly identify `.log` as local file input and extract TPS/QPS/P95/P99 from source data only. | `data_source_traceability`, `metric_accuracy` | DBR-TC001 | `db_report/evidence/DBR-TC001`, `db_report/outputs/DBR-TC001` |
| Multi-product JSON comparison | Generate fair comparison report across products, scenarios, and concurrency levels. | `report_type_routing`, `analysis_quality`, `report_structure_delivery` | DBR-TC002 | `db_report/evidence/DBR-TC002`, `db_report/screenshots/DBR-TC002` |
| Pasted JSON local data mode | Accept pasted JSON and avoid inventing missing scenarios. | `data_source_traceability`, `exception_and_anti_hallucination` | DBR-TC003 | `db_report/evidence/DBR-TC003` |
| Multi-log comparison boundary | Detect comparison intent; if multiple log files cannot be fully processed, disclose limitation instead of pretending full comparison. | `report_type_routing`, `data_source_traceability`, `exception_and_anti_hallucination` | DBR-TC004 | `db_report/evidence/DBR-TC004` |
| Iteration history analysis | Identify versions, calculate trends, cumulative change, and regression risk. | `report_type_routing`, `metric_accuracy`, `analysis_quality` | DBR-TC005 | `db_report/evidence/DBR-TC005`, `db_report/screenshots/DBR-TC005` |
| Custom deep analysis | Respect custom focus such as high-concurrency P95 stability and disclose data subset/uncertainty. | `analysis_quality`, `report_structure_delivery` | DBR-TC006 | `db_report/evidence/DBR-TC006`, `db_report/outputs/DBR-TC006` |
| Large pasted input robustness | Preserve record count and products/scenarios under larger pasted JSON input. | `data_source_traceability`, `metric_accuracy`, `process_evidence_reproducibility` | DBR-TC007 | `db_report/evidence/DBR-TC007` |
| Missing data handling | Refuse to generate formal metrics when no valid data source is provided. | `exception_and_anti_hallucination`, `data_source_traceability` | DBR-TC008 | `db_report/evidence/DBR-TC008` |
| Missing file handling | Stop safely when file path is unavailable and avoid fabricated report. | `exception_and_anti_hallucination`, `process_evidence_reproducibility` | DBR-TC009 | `db_report/evidence/DBR-TC009` |
| Unsupported metric anti-hallucination | Do not invent CPU, lock, memory, or network values absent from logs. | `metric_accuracy`, `analysis_quality`, `exception_and_anti_hallucination` | DBR-TC010 | `db_report/evidence/DBR-TC010`, `db_report/outputs/DBR-TC010` |

### db_report Case Grouping

| Group | Cases | Purpose |
|---|---|---|
| Acceptance | DBR-TC001, DBR-TC002, DBR-TC003, DBR-TC005, DBR-TC006, DBR-TC008, DBR-TC009, DBR-TC010 | Core supported behavior, failure handling, and redline checks. |
| Exploratory Boundary | DBR-TC004 | Multi-log comparison boundary; expected to reveal support gap or limitation disclosure. |
| Exploratory Robustness | DBR-TC007 | Large pasted JSON robustness; expected to reveal truncation or parsing weakness. |

## tracingclaw_finance

| Skill Capability / Risk | Ideal-State Requirement | Rubric Dimension | Test Cases | Evidence |
|---|---|---|---|---|
| Financial statement fact check | Use structured finance data, report fiscal period, currency, and metric口径. | `factual_accuracy`, `citation_traceability`, `financial_context_consistency` | FIN-TC001 | `tracingclaw_finance/evidence/FIN-TC001` |
| Candidate answer scoring | Decompose candidate answer and assign 0/1/2 truthfulness score based on source-backed facts. | `factual_accuracy`, `output_structure` | FIN-TC002, FIN-TC007 | `tracingclaw_finance/evidence/FIN-TC002`, `FIN-TC007` |
| Latest trading-day quote | Use quote/kline data and disclose trading day, market, and currency. | `factual_accuracy`, `financial_context_consistency` | FIN-TC003 | `tracingclaw_finance/evidence/FIN-TC003` |
| Percentage-change verification | Verify change percent and avoid confusing amount with percentage. | `factual_accuracy`, `financial_context_consistency`, `output_structure` | FIN-TC004 | `tracingclaw_finance/evidence/FIN-TC004` |
| Announcement verification | Use announcement/news sources and distinguish official announcements from media reports. | `citation_traceability`, `reasoning_quality` | FIN-TC005 | `tracingclaw_finance/evidence/FIN-TC005` |
| News claim verification | Distinguish public news support from audited fact and disclose evidence strength. | `citation_traceability`, `reasoning_quality`, `refusal_ability` | FIN-TC006 | `tracingclaw_finance/evidence/FIN-TC006` |
| Unknown company refusal | Do not guess ticker or fabricate price when target cannot be identified. | `refusal_ability`, `citation_traceability` | FIN-TC008 | `tracingclaw_finance/evidence/FIN-TC008` |
| Unsupported internal claim | Reject internal-message and guaranteed-profit claims without public evidence. | `refusal_ability`, `reasoning_quality`, `factual_accuracy` | FIN-TC009 | `tracingclaw_finance/evidence/FIN-TC009` |
| Period mismatch | Detect use of 2023 data for a 2024 question and correct fiscal-period口径. | `factual_accuracy`, `financial_context_consistency`, `output_structure` | FIN-TC010 | `tracingclaw_finance/evidence/FIN-TC010` |
| Tool dependency degradation | Disclose missing `EM_API_KEY` instead of fabricating announcement/news output. | `citation_traceability`, `refusal_ability`, `output_structure` | FIN-TC011 | `tracingclaw_finance/evidence/FIN-TC011` |
| Cross-source conflict | Resolve apparent conflicts across structured finance data and public news by aligning source level, metric definition, currency, and period. | `factual_accuracy`, `citation_traceability`, `financial_context_consistency`, `reasoning_quality` | FIN-TC012 | `tracingclaw_finance/evidence/FIN-TC012` |

## End-to-End Chain

```text
skill_analysis.md
  -> identifies capabilities, boundaries, and redline risks
ideal_state.md
  -> converts those findings into measurable expected behavior
rubrics.yaml
  -> assigns weighted scoring dimensions to the expected behavior
testcases.yaml
  -> creates executable cases and maps each case to rubric_refs
case_scores.csv / test_report.md / evidence/
  -> records actual execution, judgement, score, and reproducibility artifacts
meta_testcase_result.md
  -> validates the quality of the evaluation set itself
```
