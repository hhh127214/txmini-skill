# db_report Skill Analysis

## Skill Positioning

`db_report_skill` is a self-contained database performance report generation Skill. It converts local performance test data or pasted JSON records into database performance reports.

The evaluation target is the current updated version of the Skill only. Deleted historical features, older internal dependencies, and removed check scripts are not treated as required behavior.

## Inputs

Supported input sources:

- local `.log` sysbench files;
- local `.json` StandardRecords files or JSON arrays;
- local `.csv` files with standard record columns;
- local `.xlsx` files with expected sheet headers;
- pasted JSON performance rows.

Unsupported input sources:

- internal database APIs;
- internal HTTP APIs;
- task IDs used to query company-internal systems;
- missing or inaccessible file paths without local data.

## Report Types

The Skill supports four report types:

- `single`: default single-run performance report.
- `comparison`: multi-product, multi-version, or multi-configuration comparison report.
- `iteration`: historical version trend report.
- `custom`: focused report based on user-specified dimensions.

Report type recognition is keyword-based:

- comparison: `对比`, `比较`, `vs`, `差异`, `哪个更好`.
- iteration: `迭代`, `版本演进`, `历史趋势`, `变化趋势`.
- custom: `客制化`, `专项`, `定制`, `深度分析`, `详细分析`.
- otherwise: `single`.

## Outputs

Expected final outputs:

- `report.md`
- `report.html`
- `report.docx`
- `charts/*.png`
- `data/intent.json`
- `data/extracted_data.json`
- `data/analysis_results.json`
- `data/insights.json`

The three report formats should be generated independently from shared `report_data`, not by converting a single format into the others.

## Core Quality Risks

1. Data hallucination: generated TPS/QPS/P95/P99/duration values not traceable to input.
2. Weak input gating: formal reports generated when the user provides only natural language.
3. Incorrect report type routing: comparison, iteration, or custom requests handled as single reports.
4. Incomplete scenario analysis: sysbench scenarios merged or omitted.
5. Weak comparison fairness: different products or versions compared without coverage/fairness disclosure.
6. Weak output quality: missing charts, missing formats, unresolved placeholders, or incomplete chapters.
7. Process opacity: no preserved intermediate files or execution evidence.

## Evaluation Implications

The evaluation set should test both result quality and process evidence. It should not require removed historical scripts, but it should require observable evidence that the current five-stage pipeline behaves correctly:

1. intent parsing;
2. data ingestion;
3. analysis;
4. chart generation;
5. report rendering.

