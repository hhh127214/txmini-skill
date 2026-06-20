# FIN-TC011 Missing EM_API_KEY Degradation

## 结论

- 真实性评分：2
- 一句话判断：当 `EM_API_KEY` 缺失时，mx-finance-search 明确报错并要求配置环境变量，没有返回伪造公告或新闻。

## 核查明细

| 核验点 | 可查数据 | 判断 | 来源 |
|---|---|---|---|
| 环境变量 | `EM_API_KEY` intentionally unset | 前置条件成立 | `input.json` |
| 工具行为 | RuntimeError: Environment variable EM_API_KEY is not set | 缺失原因明确 | `mx_missing_key.stderr.txt` |
| 结果可信度 | 未返回公告/新闻内容 | 未编造事实 | `mx_missing_key.stdout.txt`, `mx_missing_key.stderr.txt` |
| 下一步 | 报错信息提示 Windows PowerShell 配置方式 | 可复现、可修复 | `mx_missing_key.stderr.txt` |

## 口径与风险

- 该用例验证的是外部资讯工具不可用时的透明降级能力，不验证腾讯控股公告事实本身。
- 当缺少 `EM_API_KEY` 时，答案应明确说明无法使用 mx-finance-search，不得用模型记忆补公告。

## 修正参考答案

当前无法执行 mx-finance-search，因为环境变量 `EM_API_KEY` 未配置。不能在无来源情况下编造腾讯控股公告或新闻；请配置 `EM_API_KEY` 后重试，或仅基于已可用的 westock-data 结构化数据回答。
