# ASX Announcements Scraper

Get company announcements from the [Australian Securities Exchange](https://www.asx.com.au) (ASX): every market announcement that listed companies lodge, with headline, release time, announcement type, the price-sensitive flag and a direct link to the PDF. Use it to track the companies you follow, watch for market-moving news, build a research database or feed announcement text into your own analysis.

- **Any company or the whole market.** Enter ASX codes such as CBA or BHP, or leave the list empty to get the latest announcements from all listed companies.
- **Filters that match the ASX website.** Date range, price-sensitive only and announcement type (results, quarterly reports, dividends, takeovers and more).
- **PDF page count and text, if you want them.** Turn on one option and the Actor downloads each PDF and adds its page count or its full text.
- **History back to December 2008.** The same archive the asx.com.au announcement search uses.
- **Company profiles.** Description, directors, address, website, share registry, index membership, price and key statistics.
- **No login and no proxy needed.** Press Start and get data.
- **Low price.** $3 per 1,000 results.

**Run it online, without code:** [ASX Announcements Scraper - Company Announcements & PDFs](https://apify.com/pipiagent/asx-announcements-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `asx-announcements-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Announcements | One announcement | ASX code, company name, headline, release time (UTC), Sydney release date, announcement type, price-sensitive flag, file size, PDF link, sector, industry, ISIN, other codes the announcement lists |
| Announcements with "Read the PDF" | One announcement | Everything above plus page count, and the PDF text if you choose it |
| Company profiles | One company | Description, sector, listing date, website, address, share registry, directors and secretaries, indices, last price, market cap, 52-week range, P/E, EPS, dividend yield, franking |

## Input examples

The latest announcements from all ASX companies:

```json
{
    "maxItems": 200
}
```

Price-sensitive announcements of two companies in 2025:

```json
{
    "tickers": ["WES", "FMG"],
    "dateFrom": "2025-01-01",
    "dateTo": "2025-12-31",
    "priceSensitiveOnly": true
}
```

Dividend and results announcements of CBA, with the page count of each PDF:

```json
{
    "tickers": ["CBA"],
    "announcementTypes": ["distribution announcement", "periodic reports"],
    "pdfContent": "pageCount",
    "maxItems": 50
}
```

Today's price-sensitive announcements with the PDF text:

```json
{
    "dateFrom": "today",
    "priceSensitiveOnly": true,
    "pdfContent": "text",
    "maxPdfTextChars": 20000
}
```

Company profiles:

```json
{
    "mode": "companyProfiles",
    "tickers": ["CBA", "BHP"]
}
```

You can also paste company page links such as `https://www.asx.com.au/markets/company/CBA`, or codes written as `ASX:CBA` or `CBA.AX`.

## Output examples

An announcement:

```json
{
    "type": "announcement",
    "ticker": "CBA",
    "companyName": "COMMONWEALTH BANK OF AUSTRALIA.",
    "relatedTickers": [],
    "searchedTicker": "CBA",
    "announcementId": "03160230",
    "documentKey": "2924-03160230-2A1709910",
    "headline": "September Quarter 2026 Basel III Pillar 3",
    "publishedAt": "2026-11-10T20:30:16Z",
    "publishedDateSydney": "2026-11-11",
    "announcementType": "Periodic Reports - Other",
    "announcementTypes": ["Periodic Reports - Other"],
    "priceSensitive": true,
    "fileSize": "668KB",
    "fileSizeKb": 668,
    "pageCount": 26,
    "pdfUrl": "https://asx.api.cmfyapp.com/asx-research/1.0/file/2924-03160230-2A1709910",
    "companyUrl": "https://www.asx.com.au/markets/company/CBA",
    "isin": "AU000000CBA7",
    "scrapedAt": "2026-11-27T09:04:24Z"
}
```

An announcement with the PDF text (shortened here):

```json
{
    "type": "announcement",
    "ticker": "PIL",
    "companyName": "PEPPERMINT INNOVATION LIMITED",
    "headline": "Reinstatement to Quotation",
    "publishedAt": "2026-11-27T08:00:08Z",
    "announcementType": "Reinstatement to Official Quotation",
    "priceSensitive": true,
    "fileSize": "78KB",
    "pageCount": 1,
    "pdfUrl": "https://asx.api.cmfyapp.com/asx-research/1.0/file/2924-03168131-6A1357699",
    "sector": "Information Technology",
    "industry": "Software",
    "pdfText": "Market\nAnnouncement\n\n27 November 2026 ... Peppermint Innovation Limited (ASX: PIL) –\nReinstatement to Quotation\nThe suspension of trading in the securities of Peppermint Innovation Limited (‘PIL’) will be lifted from\nthe commencement of trad..."
}
```

A company profile (lists shortened):

```json
{
    "type": "companyProfile",
    "ticker": "CBA",
    "companyName": "COMMONWEALTH BANK OF AUSTRALIA.",
    "description": "Banking, financial and related services.",
    "sector": "Financials",
    "industryGroup": "Banks",
    "isin": "AU000000CBA7",
    "dateListed": "1991-09-12",
    "websiteUrl": "http://www.commbank.com.au/",
    "shareRegistry": "MUFG CORPORATE MARKETS (AU) LTD - LOCKED BAG A14, SYDNEY SOUTH, NSW, AUSTRALIA, 1232",
    "directors": [{"name": "Mr Paul O'Malley", "title": "Chair"}, {"name": "Mr Matthew Comyn", "title": "Managing Director, CEO, Director"}],
    "indices": ["S&P/ASX 200", "S&P/ASX 20", "S&P/ASX 50"],
    "priceLast": 169.29,
    "marketCap": 284471866236,
    "priceFiftyTwoWeekHigh": 185.59,
    "priceFiftyTwoWeekLow": 146.98,
    "priceEarningsRatio": 26.08041,
    "dividendYieldPercent": 2.9707629860580034,
    "lastDividend": 2.7,
    "frankingPercent": 100,
    "exDividendDate": "2026-08-19",
    "url": "https://www.asx.com.au/markets/company/CBA"
}
```

Profiles also include the company's registered address and the phone number listed on its ASX page.

## How much does it cost?

You pay per saved result: **$3.00 per 1,000 results**. There is no start fee and no monthly rental. Reading the PDF page count or text does not change the price.

| Run | Results | Cost |
|---|---|---|
| The latest 100 announcements | 100 | $0.30 |
| Price-sensitive announcements of WES and FMG in 2025 | 26 | $0.08 |
| Every announcement released on 26 November 2026 | 779 | $2.34 |
| 10,000 market-wide announcements | 10,000 | $30.00 |
| Profiles of 20 companies | 20 | $0.06 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **History starts on 1 December 2008.** Earlier announcements are not in the archive that asx.com.au searches.
- **Delisted companies cannot be searched by code.** Codes such as OSH (Oil Search) or SYD (Sydney Airport) are no longer found, so the Actor skips them with a warning. Their old announcements still appear when you leave the codes empty and set a date range.
- **Dates are Sydney calendar days.** "From date" and "To date" follow the ASX trading day in Sydney time. `publishedAt` is in UTC, and `publishedDateSydney` gives the Sydney date.
- **Announcement types are the 19 ASX categories.** The filter works on the broad categories the ASX website offers. Each result also lists the detailed sub-types, such as "Appendix 3Y" or "Dividend Pay Date".
- **"Only the company's own announcements" is on by default.** ASX also lists a company under announcements lodged by others that name it, for example the substantial holder notices a bank files about its stakes in other companies. These are left out unless you turn the option off. Announcements lodged jointly by several companies are kept only for the company they were lodged under.
- **Page count needs the PDF.** The announcement list does not include the page count, so `pageCount` is empty unless you turn on **Read the PDF**. Each PDF is then downloaded, which makes runs much slower: in our tests 50 announcements with text took 104 seconds (about 2 seconds each), and 20 with page counts, including large reports, took 26 seconds.
- **PDF text is plain text.** Layout and tables are flattened. Scanned PDFs have no text layer, so `pdfText` stays empty for them. In our test of 50 announcements from one day, all 50 PDFs gave text. PDFs larger than 10 MB are skipped by default (the link is still saved) and long text is cut at 50,000 characters; you can change both.
- **Sector and industry are sometimes empty.** ASX does not send them for every announcement.
- **Profile prices are a snapshot.** Price and statistics fields show what the company page showed at the time of the run.
- **Large runs are possible.** One query on the ASX side returns at most 10,000 announcements, and the Actor continues automatically by date. A test run collected 10,600 market-wide announcements with no duplicates.

---

Full documentation, all input options and a free trial: **[ASX Announcements Scraper on Apify](https://apify.com/pipiagent/asx-announcements-scraper)**
