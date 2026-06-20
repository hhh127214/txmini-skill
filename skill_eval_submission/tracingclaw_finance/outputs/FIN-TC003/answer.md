# FIN-TC003 Latest Closed Trading Day Price

## 结论

- 真实性评分：2
- 一句话判断：最近一个已收盘交易日的收盘价可由 westock-data quote/kline 核验。

## 核查明细

| 核验点 | 可查数据 | 判断 | 来源 |
|---|---|---|---|
| 标的 | 腾讯控股，hk00700，港股 | 命中目标证券 | `westock_quote.stdout.txt` |
| 最近交易日 | 2026-06-18 | 日期明确 | `westock_quote.stdout.txt`, `westock_kline.stdout.txt` |
| 收盘价 | 440.2 | 行情与 K 线一致 | `westock_quote.stdout.txt`, `westock_kline.stdout.txt` |
| 币种 | 港股价格，按港元口径展示 | 口径明确 | `westock_quote.stdout.txt` |

## 口径与风险

- `quote` 返回的 `time` 为 2026-06-18，`price` 为 440.2。
- `kline` 中 2026-06-18 的 `last` 也是 440.2，可作为已收盘交易日价格证据。

## 修正参考答案

腾讯控股 hk00700 最近一个已收盘交易日为 2026-06-18，收盘价为 440.2 港元。
