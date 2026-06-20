# FIN-TC001 Financial Statement Fact Check

## 结论

- 真实性评分：2
- 一句话判断：腾讯控股 hk00700 的 2024 财年年度报告数据可由 westock-data 多期港股综合损益表核验。

## 核查明细

| 核验点 | 可查数据 | 判断 | 来源 |
|---|---|---|---|
| 标的 | 腾讯控股，hk00700，港股 | 命中目标证券 | `westock_finance_zhsy_num8.stdout.txt` |
| 报告期 | 2024-12-31，年度报告 | 财年明确 | `westock_finance_zhsy_num8.stdout.txt` |
| 币种 | 港币，港元 | 币种明确 | `westock_finance_zhsy_num8.stdout.txt` |
| 净利润口径 | ProfitToShareholders = 209,573,020,528.08 港元；EarningAfterTax = 212,158,222,030.32 港元 | 应区分归母/税后口径 | `westock_finance_zhsy_num8.stdout.txt` |

## 口径与风险

- 本用例采用 westock-data 返回的港股综合损益表 `zhsy`。
- 若用户问“净利润”，需要说明采用“公司权益持有人应占盈利/ProfitToShareholders”还是“税后盈利/EarningAfterTax”。
- 数据发布时间为 2025-03-19。

## 修正参考答案

腾讯控股 hk00700 2024 财年年度报告中，公司权益持有人应占盈利约为 2095.73 亿港元；若按税后盈利口径，则约为 2121.58 亿港元。报告期为 2024-12-31，币种为港元。
