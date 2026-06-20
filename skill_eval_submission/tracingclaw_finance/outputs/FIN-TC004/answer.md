# FIN-TC004 Percentage Change Verification

## 结论

- 真实性评分：0
- 一句话判断：候选结论“最近一个交易日上涨超过 5%”不属实，westock-data 显示最近交易日为下跌。

## 核查明细

| 核验点 | 候选回答 | 可查数据 | 判断 | 来源 |
|---|---|---|---|---|
| 最近交易日 | 最近一个交易日 | 2026-06-18 | 日期明确 | `westock_quote.stdout.txt` |
| 涨跌幅 | 上涨超过 5% | change_percent = -1.17 | 候选结论错误 | `westock_quote.stdout.txt` |
| 收盘价 | 未给出 | price/last = 440.2 | 可核查 | `westock_quote.stdout.txt`, `westock_kline.stdout.txt` |

## 口径与风险

- 港股行情应使用港元价格口径。
- 本用例核验的是最近已收盘交易日，不使用盘中推测。

## 修正参考答案

不属实。腾讯控股 hk00700 在 2026-06-18 的收盘价为 440.2 港元，涨跌幅为 -1.17%，并非上涨超过 5%。候选答案应判 0 分。
