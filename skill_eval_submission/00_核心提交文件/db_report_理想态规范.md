# db_report Ideal State

## 1. Capability Boundary

The ideal `db_report_skill` generates database performance reports only from user-provided local data or pasted JSON. It never queries internal systems and never fabricates performance indicators.

Allowed sources:

- `.log`
- `.json`
- `.csv`
- `.xlsx`
- pasted JSON rows or StandardRecords JSON

Disallowed sources:

- internal APIs;
- internal databases;
- task IDs or plan IDs as data lookup keys;
- guessed benchmark results;
- generated values not present in the input.

## 2. Input and Intent Layer

The Skill should:

- identify whether the user supplied a local file, pasted data, or only natural language;
- map Chinese scenario terms into normalized fields, such as `只读 -> read_only`, `点查 -> point_select`, `集中式 -> 集中式性能`;
- distinguish AND and OR conditions for multiple scenarios;
- classify report type as `single`, `comparison`, `iteration`, or `custom`;
- stop early when no usable data source exists.

## 3. Data Layer

The Skill should:

- parse supported local files into StandardRecords;
- preserve `meta.products`, `meta.scenarios`, `meta.concurrencies`, and `meta.source_info`;
- reject empty records;
- reject records with null TPS, QPS, or P95;
- keep TPS, QPS, P95, P99, duration, version, and scenario values traceable to input data.

It must not estimate, interpolate, backfill, or hardcode performance indicators.

## 4. Analysis Layer

The ideal analysis should:

- keep the five core sysbench scenarios independent where present;
- calculate peak QPS, peak threads, P95 at peak, and concurrency scalability;
- for comparison reports, disclose fairness issues such as missing scenarios or mismatched concurrency levels;
- for iteration reports, calculate version trend, cumulative change, and regression points;
- for custom reports, state the focus dimension, data subset, assumptions, and uncertainty;
- label insights as L1/L2/L3 and keep L3 only in recommendation-style sections.

## 5. Output Layer

The ideal output should include:

- `report.md`;
- `report.html`;
- `report.docx`;
- required charts for the report type;
- intermediate files under `data/`;
- no unresolved placeholders such as `{X}` or `{product}`;
- consistent key numbers across Markdown and HTML.

## 6. Failure Behavior

The Skill should stop and explain the reason when:

- no data source is provided;
- a path is missing or inaccessible;
- the file extension is unsupported;
- parsed data is empty;
- TPS/QPS/P95 fields are missing or null;
- requested comparison or iteration cannot be supported by the data.

Failure responses should ask for local `.log/.xlsx/.json/.csv` data or pasted JSON. They must not suggest internal API access.

## 7. Red Lines

- No fabricated performance metrics.
- No internal database/API dependency.
- No formal report when data is missing.
- No comparison without fairness disclosure.
- No financial, hardware, cost, CPU, or lock-wait metrics unless present in input.
- No hidden conversion-only report generation for docx/html.

