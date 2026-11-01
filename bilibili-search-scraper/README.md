# Bilibili Search Scraper

Search [Bilibili](https://www.bilibili.com) (哔哩哔哩), China's largest video community, by keyword and export the matching videos with their statistics.

Use it to monitor how a brand, product or topic is covered on Bilibili, to find creators who talk about your category, or to track trends in China.

- **Search like a user, export like an analyst.** Keywords in, a table of videos out.
- **Sort and filter.** Best match, newest, most viewed, and video length.
- **English field names.** Clean JSON with `views`, `likes` and `publishedAt`. Text stays in the original language.
- **No login and no proxy needed.**
- **Low price.** $3 per 1,000 videos.

**Run it online, without code:** [Bilibili Search Scraper - Find Videos by Keyword](https://apify.com/pipiagent/bilibili-search-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `bilibili-search-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "searchQueries": ["耐克", "Nike"],
    "sortOrder": "pubdate",
    "maxItemsPerQuery": 200,
    "maxItems": 400
}
```

## Output example

```json
{
    "type": "video",
    "bvid": "BV1KwWXzKEcn",
    "aid": 115410787698957,
    "url": "https://www.bilibili.com/video/BV1KwWXzKEcn",
    "title": "AI",
    "durationSeconds": 31,
    "publishedAt": "2025-10-21T06:43:20Z",
    "category": "日常",
    "tags": ["秘书", "AI"],
    "authorId": 417221062,
    "authorName": "AIvbju",
    "authorUrl": "https://space.bilibili.com/417221062",
    "views": 158100,
    "likes": 1528,
    "favorites": 1738,
    "comments": 53,
    "danmakuCount": 17,
    "searchQuery": "AI",
    "scrapedAt": "2026-10-10T13:52:00Z"
}
```

## How much does it cost?

You pay per saved result: **$3.00 per 1,000 videos**. There is no start fee and no monthly rental. Turning on **Add full statistics** does not change the price.

| Run | Results | Cost |
|---|---|---|
| 100 videos for one keyword | 100 | $0.30 |
| 1,000 videos for one keyword | 1,000 | $3.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **At most 1,000 videos per keyword.** This is Bilibili's own limit. To get more, use several related keywords or different sort orders.
- **Coins and shares need the extra switch.** Search listings do not include them. Turn on **Add full statistics** to add them.
- **Duplicates across keywords are kept.** Each result has a `searchQuery` field that says which keyword found it.

---

Full documentation, all input options and a free trial: **[Bilibili Search Scraper on Apify](https://apify.com/pipiagent/bilibili-search-scraper)**
