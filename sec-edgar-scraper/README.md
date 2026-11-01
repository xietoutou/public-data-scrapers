# SEC EDGAR Scraper

Get data from [SEC EDGAR](https://www.sec.gov/edgar), the US Securities and Exchange Commission's database of company filings, without an API key and without writing code. Three modes in one Actor:

- **Company filings.** Every filing of the companies you choose: 10-K, 10-Q, 8-K, Form 4 insider trades, S-1, proxy statements and more, with direct links to the documents. Back to the 1990s.
- **Full-text search.** Find filings that contain your words, across all companies, from 2001 on. Leave the words empty to get the latest filings of a form type, for example every new S-1 or 8-K.
- **Financials.** Revenue, gross profit, operating and net income, EPS, cash flow, assets, liabilities, equity, cash and debt per year or quarter, from the companies' XBRL data.

Use it for investment research, monitoring competitors and portfolio companies, finding IPOs and funding events, tracking insider trading, building financial datasets, and feeding filings to AI tools.

- **Official data.** Everything comes from the SEC's own public APIs, the same data that powers sec.gov.
- **Clean, flat records.** Tickers, CIK numbers, form types, dates, document links and 8-K item descriptions ("Results of Operations and Financial Condition") ready for spreadsheets.
- **Type a ticker, a CIK or a name.** AAPL, 320193 and "Apple" all work.
- **No API key, no login, no proxy.**
- **Low price.** $1 per 1,000 results.

**Run it online, without code:** [SEC EDGAR Scraper - Filings, Full-Text Search & Financials](https://apify.com/pipiagent/sec-edgar-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `sec-edgar-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

### Company filings

| Field | Example |
|---|---|
| `companyName`, `cik`, `tickers` | Tesla, Inc., 0001318605, ["TSLA"] |
| `formType` | 8-K |
| `filingDate`, `reportDate`, `acceptedAt` | 2026-10-21 |
| `accessionNumber` | 0001628280-26-066738 |
| `items`, `itemDescriptions` | 8-K items: ["2.02", "9.01"], ["Results of Operations and Financial Condition", ...] |
| `documentUrl`, `filingIndexUrl` | Links to the main document and to the list of all files of the filing |
| `description`, `sizeBytes`, `isXBRL`, `fileNumber` | |
| `exchanges`, `sic`, `sicDescription`, `stateOfIncorporation`, `fiscalYearEnd` | Company details |

### Full-text search results

Company, CIK, form type, filing date, period, accession number, the document that matched (for example "EX-99.1" press release), links to the document and the filing, 8-K items, business location, state of incorporation and industry code. One result per filing.

### Financials

One row per company and period: `period` (CY2025 or CY2026Q2), `periodStart`, `periodEnd`, `fiscalYear`, `fiscalPeriod`, `form`, `filedAt`, and the numbers `revenue`, `costOfRevenue`, `grossProfit`, `researchAndDevelopment`, `sellingGeneralAdministrative`, `operatingIncome`, `netIncome`, `epsBasic`, `epsDiluted`, `dilutedSharesOutstanding`, `operatingCashFlow`, `capitalExpenditure`, `totalAssets`, `totalLiabilities`, `stockholdersEquity`, `cashAndEquivalents`, `longTermDebt`. All amounts are in US dollars.

## Input examples

The latest 8-K filings of three companies:

```json
{
    "mode": "filings",
    "companies": ["AAPL", "TSLA", "Microsoft"],
    "formTypes": ["8-K"],
    "maxItemsPerQuery": 20
}
```

All Apple annual reports from 2005 to 2012:

```json
{
    "mode": "filings",
    "companies": ["AAPL"],
    "formTypes": ["10-K"],
    "dateFrom": "2005-01-01",
    "dateTo": "2012-12-31"
}
```

10-K reports filed this year that mention "artificial intelligence":

```json
{
    "mode": "search",
    "searchQuery": "\"artificial intelligence\"",
    "formTypes": ["10-K"],
    "dateFrom": "2026-01-01",
    "maxItems": 1000
}
```

Every S-1 (IPO registration) filed in the last 7 days, with no search words:

```json
{
    "mode": "search",
    "formTypes": ["S-1"]
}
```

Quarterly financials of Apple and NVIDIA:

```json
{
    "mode": "financials",
    "companies": ["AAPL", "NVDA"],
    "financialPeriod": "quarterly"
}
```

## Output examples

A filing:

```json
{
    "type": "filing",
    "companyName": "Tesla, Inc.",
    "cik": "0001318605",
    "tickers": ["TSLA"],
    "formType": "8-K",
    "filingDate": "2026-10-21",
    "reportDate": "2026-10-21",
    "acceptedAt": "2026-10-21T20:41:42Z",
    "accessionNumber": "0001628280-26-066738",
    "description": "8-K",
    "items": ["2.02", "9.01"],
    "itemDescriptions": ["Results of Operations and Financial Condition", "Financial Statements and Exhibits"],
    "documentUrl": "https://www.sec.gov/Archives/edgar/data/1318605/000162828026066738/tsla-20261021.htm",
    "filingIndexUrl": "https://www.sec.gov/Archives/edgar/data/1318605/000162828026066738/0001628280-26-066738-index.htm",
    "sizeBytes": 5568283,
    "isXBRL": true,
    "fileNumber": "001-34756",
    "exchanges": ["Nasdaq"],
    "sic": "3711",
    "sicDescription": "Motor Vehicles & Passenger Car Bodies",
    "stateOfIncorporation": "TX",
    "fiscalYearEnd": "1231",
    "scrapedAt": "2026-10-30T10:09:42Z"
}
```

A financial period:

```json
{
    "type": "financials",
    "companyName": "Apple Inc.",
    "cik": "0000320193",
    "tickers": ["AAPL"],
    "period": "CY2025",
    "periodType": "annual",
    "periodStart": "2024-09-29",
    "periodEnd": "2025-09-27",
    "fiscalYear": 2025,
    "fiscalPeriod": "FY",
    "form": "10-K",
    "currency": "USD",
    "revenue": 416161000000,
    "netIncome": 112010000000,
    "epsDiluted": 7.46,
    "operatingCashFlow": 111482000000,
    "totalAssets": 379297000000,
    "cashAndEquivalents": 45317000000
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 results**. A filing, a search result and a financial period each count as one result. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| The last 100 filings of a company | 100 | $0.10 |
| 1,000 search results | 1,000 | $1.00 |
| 10 years of quarterly financials for 20 companies | about 800 | about $0.80 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Full-text search covers 2001 onward** and returns at most 10,000 documents per search, ordered by relevance. Narrow the dates or form types to get everything. When several documents of one filing match, the filing is saved once.
- **Financials come from XBRL**, which US companies have filed since about 2009 to 2011. Funds, foreign private issuers filing 20-F and many very small companies have little or no XBRL data.
- **Periods are calendar periods.** The SEC aligns each number to the nearest calendar quarter or year (`period`), so Apple's fiscal Q3 2026 appears as CY2026Q2. `fiscalYear` and `fiscalPeriod` show the company's own labels.
- **Fourth quarters are often missing** in quarterly mode, because most companies report the fourth quarter only inside the annual report. Use annual minus the first three quarters.
- **A number is empty when the company does not report it** under the standard name, for example banks have no gross profit. Some companies use their own custom tags.
- **Companies without a ticker** (private funds, some subsidiaries) need their CIK number. You can find it on the company's EDGAR page.
- **Document links point to sec.gov.** The Actor does not download the documents themselves.

---

Full documentation, all input options and a free trial: **[SEC EDGAR Scraper on Apify](https://apify.com/pipiagent/sec-edgar-scraper)**
