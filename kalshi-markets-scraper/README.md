# Kalshi Scraper

Get live odds, volume, trades and price history from [Kalshi](https://kalshi.com), the largest regulated prediction market in the US. Use it for market research, odds tracking, forecasting models, arbitrage screening against other prediction markets, or to give an AI agent real-time probabilities.

- **Search by keyword or category.** Kalshi's own API has no text search. This Actor does: type `bitcoin`, `fed rate` or `super bowl` and get the matching markets.
- **Clean results, most active first.** Results are sorted by 24h volume by default, and auto-generated parlay markets that flood the raw API are left out.
- **No API key, no login.** Press Start and get data.

**Run it online, without code:** [Kalshi Scraper - Prediction Market Odds, Order Books & Trades](https://apify.com/pipiagent/kalshi-markets-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `kalshi-markets-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| **Markets** | One market (one outcome) | Implied probability, yes/no bid and ask, last price, volume, 24h volume, open interest, close time, settlement rules, optional order book |
| **Trades** | One executed trade | Time, price, number of contracts, taker side |
| **Price history** | One candle | Open, high, low, close, volume, open interest per 1 minute, 1 hour or 1 day |

**Step-by-step tutorial:** [Track Kalshi Prediction Market Odds in Python (Fed Rate Probabilities, Volume and Price History)](https://dev.to/frank0306_2838afa1791aac9/track-kalshi-prediction-market-odds-in-python-fed-rate-probabilities-volume-and-price-history-2iip)

## Input examples

The 50 most active crypto and economics markets:

```json
{
    "categories": ["Crypto", "Economics"],
    "maxItems": 50
}
```

Every market that mentions the Fed, closing within 30 days, with order books:

```json
{
    "searchTerms": ["fed", "interest rate"],
    "closesWithinDays": 30,
    "includeOrderbook": true
}
```

Daily price history for one market over the last 90 days:

```json
{
    "mode": "priceHistory",
    "marketTickers": ["KXSB-27-CHI"],
    "candleInterval": "1440",
    "historyDays": 90
}
```

You can paste kalshi.com market URLs instead of tickers.

## Output example

One result in Markets mode:

```json
{
    "marketTicker": "KXFEDDECISION-26OCT-H0",
    "eventTicker": "KXFEDDECISION-26OCT",
    "seriesTicker": "KXFEDDECISION",
    "title": "Will the Federal Reserve Hike rates by 0bps at their October 2026 meeting?",
    "outcome": "Fed maintains rate",
    "eventTitle": "Fed decision in October 2026?",
    "category": "Economics",
    "status": "active",
    "impliedProbability": 0.295,
    "yesBid": 0.29,
    "yesAsk": 0.30,
    "noBid": 0.70,
    "noAsk": 0.71,
    "spread": 0.01,
    "lastPrice": 0.30,
    "previousPrice": 0.28,
    "priceChange": 0.02,
    "volume": 1367380.71,
    "volume24h": 106349.76,
    "openInterest": 512034.0,
    "closeTime": "2026-10-28T17:59:00Z",
    "rules": "If the Federal Reserve ...",
    "settlementSources": ["Federal Reserve"],
    "url": "https://kalshi.com/markets/kxfeddecision",
    "scrapedAt": "2026-09-29T08:52:47Z"
}
```

Prices are in US dollars per contract, from 0 to 1, so a price of 0.30 means the market gives the outcome about a 30% chance. `impliedProbability` is the midpoint between the best yes bid and ask, or the last traded price when the book is one-sided.

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 results**. There is no start fee and no monthly rental. Filters run before results are saved, so you never pay for markets you filtered out.

| Run | Results | Cost |
|---|---|---|
| Top 100 markets | 100 | $0.10 |
| All open crypto markets | about 1,500 | $1.50 |
| One year of daily candles for 10 markets | 3,650 | $3.65 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

---

Full documentation, all input options and a free trial: **[Kalshi Scraper on Apify](https://apify.com/pipiagent/kalshi-markets-scraper)**
