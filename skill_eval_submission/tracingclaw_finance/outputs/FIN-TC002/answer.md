# FIN-TC002 Candidate Profit Answer Verification

## 结论

- 真实性评分：0
- 一句话判断：候选答案“9999 亿元人民币”与可查财报数据明显不符，且币种也与 westock-data 港股财报返回口径不一致。

## 核查明细

| 核验点 | 候选回答 | 可查数据 | 判断 | 来源 |
|---|---|---|---|---|
| 财年 | 2024 财年 | 2024-12-31 年度报告 | 财年可核查 | `westock_finance_zhsy_num8.stdout.txt` |
| 净利润 | 9999 亿元人民币 | ProfitToShareholders = 209,573,020,528.08 港元 | 核心数字错误 | `westock_finance_zhsy_num8.stdout.txt` |
| 币种 | 人民币 | westock-data 返回 CurrencyUnit = 港元 | 币种口径错误 | `westock_finance_zhsy_num8.stdout.txt` |

## 口径与风险

- 候选回答既没有给出来源，也没有说明 IFRS/Non-IFRS 或归母/税后口径。
- 财报金额必须标注报告期、币种和指标定义。

## 修正参考答案

腾讯控股 hk00700 2024 财年年度报告中，公司权益持有人应占盈利约为 2095.73 亿港元；若按税后盈利口径，则约为 2121.58 亿港元。候选答案应判 0 分。
