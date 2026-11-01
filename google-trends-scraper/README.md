# Google Trends Scraper

Get data from [Google Trends](https://trends.google.com) without copying charts by hand: how search interest in a term changes over time, where people search for it most, which related searches are growing, and what is trending in a country right now. Marketers, SEO teams, journalists, researchers and analysts use it for keyword research, seasonality checks, brand comparisons and content ideas.

- **Four kinds of data in one run.** Interest over time, interest by region, related queries (top and rising) and trending searches with news articles. Pick any combination.
- **Compare up to 5 terms** on the same 0-100 scale, exactly like the Compare button on Google Trends, and run as many comparisons as you like in one run.
- **Handles Google's rate limits.** Google Trends often answers automated traffic with "too many requests". The Actor paces its requests, waits and retries, switches to another address by itself when Google slows it down, keeps everything already collected and tells you exactly which terms to run again.
- **Spreadsheet friendly.** One row per term and data type with summary columns (average, peak, latest value, top region), plus the full detail. English field names, dates in ISO format (UTC).
- **No login, no API key, no proxy setup.**
- **Fair price.** $1.50 per 1,000 results, and one result holds a whole timeline or a whole region table, not one data point.

**Run it online, without code:** [Google Trends Scraper - Interest, Regions, Related & Trending](https://apify.com/pipiagent/google-trends-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `google-trends-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Data type | One result is | Main fields |
|---|---|---|
| Interest over time | One search term in one location and time range | Average, peak value and date, latest value, step size, full timeline of 0-100 values with dates |
| Interest by region | One search term in one location | Top region, number of regions, every country, state, city or US metro with its 0-100 value |
| Related queries | One search term | Up to 25 top queries with their 0-100 value, up to 25 rising queries with growth % or "Breakout" |
| Trending now | One trending search in one country | Search volume, increase %, start and end time, still trending or not, categories, related searches, up to 5 news articles with picture |

Every keyword result also repeats the settings it was collected with: `searchTerm`, `comparedWith`, `geo`, `timeRange`, the exact `startDate` and `endDate` Google used, `category` and `property` (web, images, news, YouTube or shopping search), and a link to the same view on Google Trends.

## Input examples

Compare three brands in the United States over the past 5 years, with regional interest:

```json
{
    "searchTerms": ["nike, adidas, puma"],
    "dataTypes": ["interestOverTime", "interestByRegion"],
    "geos": ["US"],
    "timeRange": "past5Years"
}
```

Seasonality of several products, each on its own scale, for a custom date range in the Food & Drink category:

```json
{
    "searchTerms": ["iced coffee", "hot chocolate", "matcha"],
    "dataTypes": ["interestOverTime", "relatedQueries"],
    "timeRange": "custom",
    "startDate": "2023-01-01",
    "endDate": "2024-12-31",
    "category": 71
}
```

City level interest on YouTube search in Japan:

```json
{
    "searchTerms": ["ラーメン"],
    "dataTypes": ["interestByRegion"],
    "geos": ["JP"],
    "property": "youtube",
    "regionLevel": "city"
}
```

What is trending right now in three countries, sports only, sorted by search volume:

```json
{
    "dataTypes": ["trendingNow"],
    "trendingGeos": ["US", "GB", "IN"],
    "trendingHours": "24",
    "trendingCategories": ["Sports"],
    "trendingSortBy": "searchVolume",
    "maxTrendingPerCountry": 25
}
```

## Output examples

Interest over time (the `timeline` is shortened here, a 12 month run has 53 weekly points):

```json
{
    "type": "interestOverTime",
    "searchTerm": "coffee",
    "comparedWith": ["tea"],
    "geo": "worldwide",
    "geoName": "Worldwide",
    "timeRange": "past12Months",
    "startDate": "2025-10-27",
    "endDate": "2026-10-27",
    "category": 0,
    "categoryName": "All categories",
    "property": "web",
    "resolution": "WEEK",
    "averageInterest": 75,
    "peakInterest": 100,
    "peakDate": "2026-05-03T00:00:00Z",
    "latestInterest": 57,
    "latestDate": "2026-10-18T00:00:00Z",
    "firstInterest": 55,
    "dataPoints": 53,
    "timeline": [
        {"date": "2025-10-26T00:00:00Z", "value": 55, "isPartial": false},
        {"date": "2025-11-02T00:00:00Z", "value": 62, "isPartial": false},
        {"date": "2025-11-09T00:00:00Z", "value": 68, "isPartial": false}
    ],
    "url": "https://trends.google.com/trends/explore?date=today+12-m&q=coffee%2Ctea",
    "scrapedAt": "2026-10-27T22:05:48Z"
}
```

Interest by region (shortened, this one listed 56 countries):

```json
{
    "type": "interestByRegion",
    "searchTerm": "coffee",
    "comparedWith": ["tea"],
    "geo": "worldwide",
    "timeRange": "past12Months",
    "regionLevel": "country",
    "topRegion": "Singapore",
    "topRegionCode": "SG",
    "regionCount": 56,
    "regions": [
        {"geoCode": "SG", "geoName": "Singapore", "value": 100},
        {"geoCode": "SH", "geoName": "St. Helena", "value": 88},
        {"geoCode": "AU", "geoName": "Australia", "value": 87}
    ],
    "url": "https://trends.google.com/trends/explore?date=today+12-m&q=coffee",
    "scrapedAt": "2026-10-27T22:05:49Z"
}
```

Related queries (shortened, 25 top and 25 rising):

```json
{
    "type": "relatedQueries",
    "searchTerm": "coffee",
    "geo": "worldwide",
    "timeRange": "past12Months",
    "topCount": 25,
    "risingCount": 25,
    "top": [
        {"query": "coffee shop", "value": 100, "url": "https://trends.google.com/trends/explore?q=coffee+shop&date=today+12-m"},
        {"query": "coffee table", "value": 94, "url": "https://trends.google.com/trends/explore?q=coffee+table&date=today+12-m"}
    ],
    "rising": [
        {"query": "how to remove coffee stain from carpet", "growthPercent": 7950, "growthText": "Breakout", "isBreakout": true, "url": "https://trends.google.com/trends/explore?q=how+to+remove+coffee+stain+from+carpet&date=today+12-m"},
        {"query": "how to brew pour over coffee", "growthPercent": 7150, "growthText": "Breakout", "isBreakout": true, "url": "https://trends.google.com/trends/explore?q=how+to+brew+pour+over+coffee&date=today+12-m"}
    ],
    "scrapedAt": "2026-10-27T22:05:51Z"
}
```

A trending search:

```json
{
    "type": "trendingNow",
    "title": "susan saint james",
    "rank": 2,
    "geo": "US",
    "geoName": "United States",
    "searchVolume": 200000,
    "searchVolumeText": "200K+",
    "increasePercent": 1000,
    "startedAt": "2026-10-27T13:30:00Z",
    "endedAt": null,
    "isActive": true,
    "categories": ["Entertainment"],
    "relatedQueries": ["susan st james", "dick ebersol", "kate and allie", "jane curtin"],
    "timeWindowHours": 24,
    "url": "https://trends.google.com/trends/explore?q=susan+saint+james&date=now+1-d&geo=US",
    "picture": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTzadYc2xDz--qyHNNsMv_MPsot657dCHBn4-oQaHcoI166wXBBCXoellKcf8I",
    "newsArticles": [
        {
            "title": "Susan Saint James, Emmy-winning actor of ‘McMillan & Wife’ and ‘Kate & Allie,’ dies at 80",
            "url": "https://www.cnn.com/2026/10/27/entertainment/susan-saint-james-death",
            "source": "CNN",
            "publishedAt": "2026-10-27T16:32:09Z",
            "picture": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTzadYc2xDz--qyHNNsMv_MPsot657dCHBn4-oQaHcoI166wXBBCXoellKcf8I"
        }
    ],
    "scrapedAt": "2026-10-27T21:48:55Z"
}
```

In CSV and Excel exports the `timeline`, `regions`, `top` and `rising` lists become numbered columns (for example `timeline/0/date`, `timeline/0/value`). The summary columns are always there for quick sorting and filtering.

## How much does it cost?

You pay per saved result: **$1.50 per 1,000 results** ($0.0015 each). There is no start fee and no monthly rental.

One search term gives one result per data type you pick. A 5 year timeline with 260 weekly values is still one result.

| Run | Results | Cost |
|---|---|---|
| 1 comparison of 5 terms, interest over time only | 5 | $0.0075 |
| 20 terms, interest over time + by region + related queries | 60 | $0.09 |
| Trending now, 50 searches in each of 10 countries | 500 | $0.75 |
| The prefilled example (2 terms, 3 data types, 20 trending searches) | 26 | $0.04 |

Terms for which Google has no data produce no result and cost nothing. Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Google rate-limits Google Trends heavily, and sometimes blocks it completely for a while.** This is the main reason Google Trends scrapers fail, and this Actor is not immune. It sends about one request per second, retries with growing pauses and moves to other addresses when Google refuses one. In our tests most keyword runs finished with full data, but at busy times Google refused every address the Actor could use for tens of minutes, and keyword runs started in that window failed. A search group is given up after about 90 seconds of refusals; the run then continues, keeps everything already saved and lists what failed in the status message. If two groups in a row fail, the Actor stops early instead of using your time. If that happens, start the run again later. **Trending now uses a different Google service and worked in every test, even while keyword data was blocked.** Very large runs (hundreds of terms) are more likely to hit a block; split them into several smaller runs.
- **A made-up or misspelled term can look like a block.** In our tests Google answered a random letter string with "too many requests" instead of "no data", and the next requests from the same addresses were refused too. Check spelling before large runs.
- **Values are relative, not search counts.** Google scales every chart so that its highest point is 100. Values from different runs or different comparison groups are not on the same scale. Only terms on the same line are compared on one scale.
- **Google samples its data.** Running the same query twice can give values that differ by a few points. This is how Google Trends works, not an error.
- **The last point of a timeline is often incomplete.** It is marked with `isPartial: true` and is not used for `latestInterest`.
- **Related topics are not included.** Google currently returns an empty related topics list to automated visitors, so the Actor does not offer it.
- **Related queries need enough search volume.** Rare terms, small regions and short time ranges often have no related queries. You are not charged when nothing is found.
- **Metro areas exist only for the United States.** City level data is often empty, especially for worldwide searches; the Actor then falls back to the default level (countries or subregions) and says so in the log.
- **Trending now covers what Google lists for the chosen window**: usually several hundred searches per day for big countries, fewer for small ones. Search volumes are Google's rounded buckets (for example 200K+). There is no worldwide trending list.

---

Full documentation, all input options and a free trial: **[Google Trends Scraper on Apify](https://apify.com/pipiagent/google-trends-scraper)**
