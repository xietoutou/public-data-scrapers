# Google News Scraper

Extract news articles from [Google News](https://news.google.com): search by keyword, read the top stories, follow a topic such as Business, or get local news for a city. Use it for media monitoring, brand and competitor tracking, PR reports, market research and news datasets.

- **Four sources in one Actor.** Keyword search, top stories, eight news topics and local news.
- **Goes past the 100 article limit.** Google shows about 100 articles per search. Give a date range and the Actor searches week by week and day by day, then removes duplicates.
- **Real article links.** Google News links point to Google. One switch adds the real publisher link.
- **Any language and country.** Works with every Google News edition.
- **No login, no API key and no proxy needed.** Press Start and get data.
- **Low price.** $1.50 per 1,000 results.

**Run it online, without code:** [Google News Scraper - Search, Topics, Date Range & Real Links](https://apify.com/pipiagent/google-news-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `google-news-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | What you get | Articles per run |
|---|---|---|
| Search by keyword | Articles that match your keywords, with optional date range, time range and publisher filter | About 100 per keyword, or thousands with a date range |
| Top stories | The front page of Google News for a country | 30 to 40 |
| Topic | One section: World, Nation, Business, Technology, Entertainment, Science, Sports or Health | 40 to 70 |
| Location | Local news for a city | Up to 70 per city |

Every article has these fields:

| Field | Meaning |
|---|---|
| `title` | Headline, without the publisher name at the end |
| `publisher`, `publisherUrl` | Name and website of the news source |
| `publishedAt` | Publication time in UTC |
| `googleNewsUrl` | Link to the article on Google News |
| `articleUrl` | Real link on the publisher's website. Filled only when **Get the real article links** is on |
| `description` | Text of the feed entry. Google News gives the headline and the publisher here, not a summary of the article |
| `relatedArticles` | Other articles about the same story, each with title, publisher and Google News link. Mostly in top stories and topics |
| `searchQuery`, `topic`, `location` | What found the article |
| `language`, `country`, `scrapedAt` | Edition and time of scraping |

## Input examples

Search the newest articles about a brand:

```json
{
    "mode": "search",
    "searchQueries": ["Tesla", "\"Elon Musk\" interview"],
    "timeRange": "7d",
    "maxItems": 200
}
```

Collect all coverage of a topic in one month:

```json
{
    "mode": "search",
    "searchQueries": ["\"quantum computing\""],
    "dateFrom": "2026-08-01",
    "dateTo": "2026-08-31",
    "maxItems": 5000
}
```

Search only some publishers and get the real links:

```json
{
    "mode": "search",
    "searchQueries": ["bitcoin"],
    "sites": ["reuters.com", "cnbc.com"],
    "timeRange": "7d",
    "resolveUrls": true
}
```

Business news in France:

```json
{
    "mode": "topic",
    "topic": "BUSINESS",
    "language": "fr",
    "country": "FR"
}
```

Local news:

```json
{
    "mode": "location",
    "location": ["London", "New York"]
}
```

## Output examples

A search result with the real article link:

```json
{
    "articleId": "CBMipgFBVV95cUxQMFNkQmpvTmdlZER6dDF6NXlNZ2x2WnpicUlHeDBvRjNRUzlaZy01OUI5Sm91YV9DRUh0Qmk4TzNwTTQ1alBveEdGOHNHcy0wa1pqR0lsZVR2dUxoQ3R1V1FnZTJuZG9MS1d3OWs3eTgxb0ZmUl96dGNiWkhzMk1wN3oyV0xFYjVrdGtIQ1Vzb0l0SWdBWlZEalo3WmxNbVpxNjJoX1dR",
    "title": "AI godfathers warn of runaway ‘intelligence explosion’",
    "publisher": "theguardian.com",
    "publisherUrl": "https://www.theguardian.com",
    "publishedAt": "2026-09-28T15:00:00Z",
    "googleNewsUrl": "https://news.google.com/rss/articles/CBMipgFBVV95cUxQMFNkQmpvTmdlZER6dDF6NXlNZ2x2WnpicUlHeDBvRjNRUzlaZy01OUI5Sm91YV9DRUh0Qmk4TzNwTTQ1alBveEdGOHNHcy0wa1pqR0lsZVR2dUxoQ3R1V1FnZTJuZG9MS1d3OWs3eTgxb0ZmUl96dGNiWkhzMk1wN3oyV0xFYjVrdGtIQ1Vzb0l0SWdBWlZEalo3WmxNbVpxNjJoX1dR?oc=5",
    "articleUrl": "https://www.theguardian.com/technology/2026/sep/28/ai-godfathers-warn-of-runaway-intelligence-explosion",
    "description": "AI godfathers warn of runaway ‘intelligence explosion’ theguardian.com",
    "relatedArticles": [],
    "searchQuery": "artificial intelligence",
    "topic": null,
    "location": null,
    "language": "en",
    "country": "US",
    "scrapedAt": "2026-09-29T11:27:39Z"
}
```

A top story with related articles (shortened to two):

```json
{
    "articleId": "CBMiVkFVX3lxTE1Ja19tUVlfSUhsMWtlZVFwemlyeW90VVNCajM0MHNFcVkwY19xSVlILTNwUFVweWtFZllQb2ZuNGhZQV9xYXlwQlktaUpVb1FiNTVKWmlR",
    "title": "RAF Fairford latest: Incident 'clearly involves' foreign actor, says US secretary of state",
    "publisher": "BBC",
    "publisherUrl": "https://www.bbc.com",
    "publishedAt": "2026-09-29T11:20:08Z",
    "googleNewsUrl": "https://news.google.com/rss/articles/CBMiVkFVX3lxTE1Ja19tUVlfSUhsMWtlZVFwemlyeW90VVNCajM0MHNFcVkwY19xSVlILTNwUFVweWtFZllQb2ZuNGhZQV9xYXlwQlktaUpVb1FiNTVKWmlR?oc=5",
    "articleUrl": "https://www.bbc.com/news/live/c65y7nl29k0et",
    "description": "RAF Fairford latest: Incident 'clearly involves' foreign actor, says US secretary of state BBC\nRubio Says Incident at UK Air Base RAF Fairford ‘Clearly Involved’ a Foreign Actor The New York Times\nThe Small English Town Rattled by Alleged Terror Plot Near U.S. Bomber Base WSJ",
    "relatedArticles": [
        {
            "title": "Rubio Says Incident at UK Air Base RAF Fairford ‘Clearly Involved’ a Foreign Actor",
            "publisher": "The New York Times",
            "url": "https://news.google.com/rss/articles/CBMimwFBVV95cUxQTVpfc0otQi04dzZ0S1E4TXBKbjlaQ252aXE1Q2hQbUw1WURoU2ViTlhsSVFoY2hFRklCdXZLdzFvYk51VlFIYkZvY0RjNDZPRDNtdlg1T29KbmdFZE1ha25MRzVMTDRQWEZuYXJlLTM4N3RuYndFZnFUVVZXdkVYdF9JMTRuT1BRT214eVEzN0ZqSm5Uc0VPaXc2WQ?oc=5"
        },
        {
            "title": "The Small English Town Rattled by Alleged Terror Plot Near U.S. Bomber Base",
            "publisher": "WSJ",
            "url": "https://news.google.com/rss/articles/CBMisAFBVV95cUxOZ3BJQmh1NEtYQ2tEaXNWdGdpMjR1ZVg1RFhLLW5sdnBjQ2xnWXQxdzU1dWw5MHZ1aHA1TmVyMXdlZXRKWWNONzUtcmFtVWNIdnZLal9aMklfZHlaTUV5SXkyZF94S011QW9YNmxpQkZkYksyc19IeW1GNFdQZmRBWXI3ZTdSTGtkLUY5V2E0RS0yTVpHc2U1M1BCSnB3SnUxRHBVZGYwSk5TWmNVc3dPZw?oc=5"
        }
    ],
    "searchQuery": null,
    "topic": "TOP_STORIES",
    "location": null,
    "language": "en",
    "country": "US",
    "scrapedAt": "2026-09-29T11:34:50Z"
}
```

## How much does it cost?

You pay per saved article: **$1.50 per 1,000 results**. There is no start fee and no monthly rental. Turning on **Get the real article links** does not change the price.

| Run | Results | Cost |
|---|---|---|
| One keyword search | 100 | $0.15 |
| One month of "quantum computing" news | 1,216 | $1.82 |
| Three months of "climate change" news | 2,547 | $3.82 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **One search returns about 100 articles.** This is Google's limit. Without a date range you get the about 100 articles Google ranks highest for the keyword, not all of them.
- **A date range gets more, but not everything.** The smallest search window is one day, and one day also returns about 100 articles at most. In our tests a busy keyword ("artificial intelligence") hit this limit on 30 of 31 days and returned 1,937 articles for the month, about 60 per day. A narrower keyword ("quantum computing") returned 1,216 articles for the same month and hit the limit on 9 days. The run log lists the days that hit the limit. To get more from those days, use narrower keywords or the publisher filter.
- **Old articles have a date but no exact time.** For articles older than a few weeks Google gives only the day. The time then shows as 07:00 or 08:00 UTC, which is midnight in California.
- **There is no article summary or full text.** Google News feeds contain the headline, publisher, date and link. The `description` field repeats the headline and publisher.
- **Real article links are slower.** Decoding needs one extra request per article, about 60 to 70 seconds per 100 articles. In our largest test the Actor decoded 2,148 links in one run of 19 minutes with no failures and no rate limiting. Google can change this without notice. If Google starts to refuse these requests, the Actor keeps the articles and leaves `articleUrl` empty. Links in `relatedArticles` are not decoded.
- **Top stories, topics and locations have no history.** They show what is on Google News now, 30 to 70 articles. Run them on a schedule to build a history.
- **Location works for cities, not for every place.** London, New York, Paris, Berlin, Sydney, Chicago and Toronto returned local news in our tests. Tokyo, Texas and Japan returned nothing. Pick the language and country that match the city. For other places use search mode with the place name as the keyword.
- **Results depend on the edition.** The same keyword returns different articles for different languages and countries.

---

Full documentation, all input options and a free trial: **[Google News Scraper on Apify](https://apify.com/pipiagent/google-news-scraper)**
