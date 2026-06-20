# db_report Test Report

## Execution Status

db_report 10 条评估用例已全部真实运行。运行证据已同步到 `evidence/`，生成报告已同步到 `outputs/`，图表截图证据已同步到 `screenshots/`。

## Execution Environment

| Item | Value |
|---|---|
| Target Skill | db_report_skill |
| Skill Version | Current updated assignment version |
| Agent/Base Model | Local pipeline execution through `scripts/run_pipeline.py` |
| Execution Date | 2026-06-20 |
| Test Resource Path | `C:\Users\17128\Desktop\skill\性能工程 Skill 评估专项考题\db_report\test-resource` |
| Runner | `tools/run_db_report_suite.py` |

## Summary

| Metric | Value |
|---|---:|
| Total Cases | 10 |
| Executed Cases | 10 |
| Passed Cases | 6 |
| Failed Cases | 4 |
| Average Score | 76.1 |
| Generated Evidence Files | 172 |

## Case Results

| Case ID | Title | Priority | Exit Code | Score | Pass | Evidence |
|---|---|---|---:|---:|---|---|
| DBR-TC001 | Single Log Report | P0 | 0 | 92 | true | `evidence/DBR-TC001`, `outputs/DBR-TC001` |
| DBR-TC002 | Comparison JSON Report | P0 | 0 | 86 | true | `evidence/DBR-TC002`, `outputs/DBR-TC002` |
| DBR-TC003 | Pasted Single-Product JSON | P0 | 0 | 82 | true | `evidence/DBR-TC003`, `outputs/DBR-TC003` |
| DBR-TC004 | Comparison Log Exploration | P1 | 0 | 48 | false | `evidence/DBR-TC004`, `outputs/DBR-TC004` |
| DBR-TC005 | Iteration History Report | P0 | 0 | 88 | true | `evidence/DBR-TC005`, `outputs/DBR-TC005` |
| DBR-TC006 | Custom High-Concurrency P95 | P0 | 0 | 76 | false | `evidence/DBR-TC006`, `outputs/DBR-TC006` |
| DBR-TC007 | Large Pasted JSON | P1 | 0 | 45 | false | `evidence/DBR-TC007`, `outputs/DBR-TC007` |
| DBR-TC008 | No Data Request | P0 | 1 | 90 | true | `evidence/DBR-TC008` |
| DBR-TC009 | Non-Existent Path | P0 | 1 | 86 | true | `evidence/DBR-TC009` |
| DBR-TC010 | Anti-Hallucination Unsupported Metrics | P0 | 0 | 68 | false | `evidence/DBR-TC010`, `outputs/DBR-TC010` |

## Evidence Summary

| Case ID | Parsed Records | Products | Scenarios | Charts | Report Formats |
|---|---:|---:|---:|---:|---|
| DBR-TC001 | 30 | 1 | 5 | 11 | md/html/docx |
| DBR-TC002 | 90 | 3 | 5 | 17 | md/html/docx |
| DBR-TC003 | 1 | 1 | 1 | 3 | md/html/docx |
| DBR-TC004 | 30 | 1 | 5 | 16 | md/html/docx |
| DBR-TC005 | 120 | 4 | 5 | 12 | md/html/docx |
| DBR-TC006 | 90 | 3 | 5 | 2 | md/html/docx |
| DBR-TC007 | 1 | 1 | 1 | 3 | md/html/docx |
| DBR-TC008 | 0 | 0 | 0 | 0 | none |
| DBR-TC009 | 0 | 0 | 0 | 0 | none |
| DBR-TC010 | 30 | 1 | 5 | 11 | md/html/docx |

## Defect Analysis

- DBR-TC004 暴露多文件 comparison 风险：用户输入两个 log 并触发 comparison，但实际只摄取了一个文件，最终输出不是严格的双版本对比报告。
- DBR-TC006 暴露 custom 深度不足：报告生成成功，但只产出 2 张图，P95 专项分析偏概要，没有充分展开高并发尾延迟风险。
- DBR-TC007 暴露大段粘贴 JSON 摄取风险：大 JSON 输入被静默裁剪为 1 条记录，未对数据不完整做明确提示。
- DBR-TC010 暴露反幻觉声明不足：报告没有编造 CPU、锁等待、内存、网络等不存在指标，但也没有明确说明这些维度缺少输入数据、无法分析。
- DBR-TC009 的异常处理可接受，但错误信息偏通用，没有精确指出 `test-resource/not_exist.log` 文件不存在。

## Overall Judgement

db_report 当前版本对 single、标准 comparison JSON、iteration 和基础异常路径具备可运行能力，能够稳定生成 md/html/docx 三格式报告。主要短板集中在复杂输入摄取、custom 深度分析和 unsupported metrics 的显式边界声明。本轮评估体系成功覆盖正常、异常、边界、反幻觉和可复现证据维度，适合作为后续回归评估基线。
