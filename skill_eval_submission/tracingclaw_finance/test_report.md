# tracingclaw_finance Test Report

## Execution Status

tracingclaw_finance 10 条评估用例已全部真实运行。运行证据已同步到 `evidence/`，核查输出已同步到 `outputs/`。

## Execution Environment

| Item | Value |
|---|---|
| Target Skill | tracingclaw_finance |
| Skill Version | Current assignment version |
| Agent/Base Model | Skill workflow executed with westock-data and mx-finance-search evidence |
| Execution Date | 2026-06-20 |
| westock-data | Available; search/quote/kline/finance/notice commands executed |
| mx-finance-search | Available; announcement/news searches executed |
| EM_API_KEY | Configured as environment variable; value not stored in reports |
| Runner | `tools/run_finance_suite.py` |

## Summary

| Metric | Value |
|---|---:|
| Total Cases | 12 |
| Executed Cases | 12 |
| Passed Cases | 12 |
| Failed Cases | 0 |
| Average Score | 92.3 |
| Raw Evidence Files | 61 |
| Case Output Files | 12 |

## Case Results

| Case ID | Title | Priority | Score | Pass | Evidence |
|---|---|---|---:|---|---|
| FIN-TC001 | Financial Statement Fact Check | P0 | 94 | true | `evidence/FIN-TC001`, `outputs/FIN-TC001/answer.md` |
| FIN-TC002 | Candidate Profit Answer Verification | P0 | 96 | true | `evidence/FIN-TC002`, `outputs/FIN-TC002/answer.md` |
| FIN-TC003 | Latest Closed Trading Day Price | P0 | 95 | true | `evidence/FIN-TC003`, `outputs/FIN-TC003/answer.md` |
| FIN-TC004 | Percentage Change Verification | P0 | 96 | true | `evidence/FIN-TC004`, `outputs/FIN-TC004/answer.md` |
| FIN-TC005 | Announcement Verification | P0 | 88 | true | `evidence/FIN-TC005`, `outputs/FIN-TC005/answer.md` |
| FIN-TC006 | News Claim Verification | P1 | 84 | true | `evidence/FIN-TC006`, `outputs/FIN-TC006/answer.md` |
| FIN-TC007 | Multi-Claim Candidate Scoring | P0 | 95 | true | `evidence/FIN-TC007`, `outputs/FIN-TC007/answer.md` |
| FIN-TC008 | Non-Existent Company | P0 | 94 | true | `evidence/FIN-TC008`, `outputs/FIN-TC008/answer.md` |
| FIN-TC009 | Unsupported Claim Without Source | P0 | 90 | true | `evidence/FIN-TC009`, `outputs/FIN-TC009/answer.md` |
| FIN-TC010 | Period Mismatch Detection | P0 | 90 | true | `evidence/FIN-TC010`, `outputs/FIN-TC010/answer.md` |
| FIN-TC011 | Missing EM_API_KEY Degradation | P1 | 92 | true | `evidence/FIN-TC011`, `outputs/FIN-TC011/answer.md` |
| FIN-TC012 | Cross-Source Conflict Resolution | P0 | 93 | true | `evidence/FIN-TC012`, `outputs/FIN-TC012/answer.md` |

## Evidence Summary

| Area | Evidence |
|---|---|
| 财报事实 | `westock-data finance hk00700 --type zhsy --num 8` returned 2024-12-31 annual report data. |
| 行情事实 | `westock-data quote/kline hk00700` returned 2026-06-18 close price 440.2 and change_percent -1.17. |
| 公告/新闻 | `mx-finance-search` returned annual-results/news evidence; `westock-data notice list` returned announcement lists. |
| 拒答场景 | `westock-data search 不存在科技股份有限公司` returned no matching stock. |
| 工具缺失 | `mx-finance-search` without `EM_API_KEY` returned a transparent missing-key error and no fabricated content. |
| 来源冲突 | `westock-data` returned HKD financial-statement data while `mx-finance-search` returned RMB news/announcement data; output aligned currency/source口径 before judgement. |

## Defect Analysis

- FIN-TC005 的公告核查可用，但最强证据应进一步锁定港交所官方年度业绩公告原文；当前结果包含公告列表和财经资讯证据。
- FIN-TC006 的新闻 claim 本身较模糊，“重大进展”属于强判断，输出已做降级，但判定天然不如结构化财报/行情用例稳定。
- FIN-TC010 涉及人民币公告口径和 westock-data 港元口径并存，输出已明确提示不能混用。
- FIN-TC011 验证了缺少 `EM_API_KEY` 时的失败路径；该 case 的工具退出码为 1，但这是预期拒绝/降级行为。
- FIN-TC012 验证了同一事实不同来源/币种口径看似冲突时的处理能力：不能只凭表面数值不同判定新闻错误，应优先对齐财报、公告、币种和指标定义。

## Overall Judgement

tracingclaw_finance 当前评估结果较稳：结构化财报、行情、候选答案评分、拒答、无来源预测和期间错配均能用可追溯证据完成核查。新闻/公告类用例也能跑通，但证据强度低于结构化数据，后续可进一步增加“官方公告原文优先级”要求。
