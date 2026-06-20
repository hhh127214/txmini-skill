# tracingclaw_finance Ideal State

## 1. Capability Boundary

The ideal Skill verifies financial facts using available public or provided tool Skills. It does not use internal search-chain reconstruction, internal links, internal logs, or private APIs.

Allowed tools:

- `westock-data` as the first-priority structured data source;
- `mx-finance-search` as the second-priority news, announcement, and research source.

If `mx-finance-search` is unavailable because `EM_API_KEY` is missing, the Skill must disclose that limitation and continue only with verifiable structured data when possible.

## 2. Input Understanding

The Skill should identify whether the user provides:

- only a financial question;
- a question plus candidate answer;
- a standalone financial conclusion;
- an internal share link;
- incomplete or ambiguous company/market/date information.

For internal share links, the ideal behavior is to ask the user to paste the original question and answer, then verify the pasted content using available tools.

## 3. Verification Workflow

The ideal workflow:

1. Split the question or candidate answer into minimal verifiable claims.
2. Identify market, ticker, exchange, period, currency, and metric.
3. Use `westock-data` first for structured facts.
4. Use `mx-finance-search` for announcements, news, research, or event context.
5. Resolve conflicts by preferring structured data and official announcements over news commentary.
6. Assign truthfulness score 0/1/2.
7. Provide corrected reference answer with source and口径.

## 4. Financial口径 Requirements

Financial statement data must state:

- company name and code;
- market and exchange;
- fiscal year or report period;
- metric口径, such as revenue, net profit attributable to shareholders, non-IFRS net profit, EPS;
- currency and unit;
- source and query time.

Market quote data must state:

- trading date;
- whether the market is open or closed;
- latest price or close price口径;
- currency;
- update time or query time;
- delayed/realtime status if available.

## 5. Scoring Rules for Candidate Answers

Truthfulness score:

- `2`: main need and secondary needs are factually correct, with consistent口径.
- `1`: main need is correct, but secondary details,口径, or explanation has minor issues.
- `0`: main need is wrong, core number is wrong, conclusion is misleading, or key fact is missing.

Core financial statement numbers, stock prices, market cap, percentage changes, or major announcements being wrong should normally result in score 0.

## 6. Refusal and Data Insufficiency

The Skill should refuse or mark data insufficient when:

- the company/security cannot be identified;
- the required tool is unavailable and no alternate reliable source exists;
- the user asks for non-public/internal data;
- the date or metric is ambiguous and cannot be inferred safely;
- no source supports the claim.

It should not fabricate a number to satisfy the user.

## 7. Red Lines

- No invented financial statement numbers.
- No invented prices,涨跌幅, announcements, news, or research reports.
- No currency mixing.
- No period mixing.
- No investment advice disguised as fact verification.
- No internal-link parsing requirement.
- No unsupported confidence when sources are missing.

