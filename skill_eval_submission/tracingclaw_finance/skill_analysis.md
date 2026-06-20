# tracingclaw_finance Skill Analysis

## Skill Positioning

`tracingclaw_finance` is a financial answer verification Skill. It verifies financial questions, candidate answers, and financial conclusions by using available public/structured financial tools.

It is not expected to restore internal company search chains. It should not call internal share-link parsers, internal logs, or private APIs.

## Dependent Tool Skills

### westock-data

Primary source for structured financial data:

- stock search;
- quote;
- kline;
- financial reports;
- funds and capital flows;
- technical indicators;
- shareholders;
- dividends;
- ratings;
- market and macro data.

When the user gives a company name but no code, the Skill should search first and then query data by code.

### mx-finance-search

Secondary source for:

- announcements;
- research reports;
- financial news;
- policy updates;
- event background.

This tool requires `EM_API_KEY`. If the key is absent, the Skill should disclose the limitation and avoid fabricating news, announcements, or research content.

## Verifiable Objects

The Skill should verify:

- financial statement numbers;
- stock prices and percentage changes;
- market, code, and exchange identity;
- announcement claims;
- news/event claims;
- candidate answer coverage and correctness;
- date, currency, market, and financial-period consistency.

## Required Output Shape

Default output should include:

1. conclusion;
2. truthfulness score: 0/1/2;
3. verification details;
4. source and口径;
5. risk or data insufficiency;
6. corrected reference answer.

If the user only asks for the true answer and does not provide a candidate answer, the score section may be simplified, but sources and口径 must still be present.

## Core Quality Risks

1. Fabricated facts with confident wording.
2. Missing source links or unverifiable citations.
3. Mixing currencies such as RMB, HKD, and USD.
4. Mixing financial periods, such as using 2023 data for a 2024 question.
5. Treating news opinions as financial statement facts.
6. Failing to disclose unavailable `EM_API_KEY` or tool errors.
7. Giving a score without decomposing the candidate answer into verifiable claims.
8. Reading or requesting internal share-link access.

## Evaluation Implications

The evaluation set should prioritize:

- factual accuracy;
- source traceability;
- market/time/currency/period口径;
- refusal and graceful degradation;
- candidate-answer scoring consistency;
- correction quality.

