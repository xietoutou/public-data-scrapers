# YouTube Search Scraper

Search [YouTube](https://www.youtube.com) by keyword and export the matching videos, without an API key and without the quota limits of the official YouTube Data API.

Use it for keyword and SEO research, to see who ranks for a topic, to find creators for influencer campaigns, or to monitor new videos about your brand.

- **Search like a viewer, export like an analyst.** Keywords in, a table of videos out.
- **Filters.** Upload date (last hour to this year) and sort by relevance, date or views.
- **Numbers you can sort.** "1.2M views" becomes 1200000, and the original text is kept.
- **No API key, no login and no proxy setup.**
- **Low price.** $1 per 1,000 videos.

**Run it online, without code:** [YouTube Search Scraper - Videos by Keyword, Date & Views](https://apify.com/pipiagent/youtube-search-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `youtube-search-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "searchQueries": ["web scraping", "python tutorial"],
    "uploadDate": "month",
    "sortBy": "views",
    "maxItemsPerQuery": 200
}
```

## Output example

```json
{
    "type": "video",
    "videoId": "k-EkfZBVe3U",
    "url": "https://www.youtube.com/watch?v=k-EkfZBVe3U",
    "title": "how to actually get good at Web Scraping",
    "viewCount": 3696,
    "viewCountText": "3,696 views",
    "durationSeconds": 167,
    "durationText": "2:47",
    "publishedTimeText": "2 weeks ago",
    "publishedAtEstimated": "2026-10-10T11:27:11Z",
    "isShort": false,
    "channelName": "Shade of Code",
    "channelId": "UCmxKkv3HQUNbTCshLwwDu3g",
    "channelHandle": "@Shadeofcode",
    "channelUrl": "https://www.youtube.com/channel/UCmxKkv3HQUNbTCshLwwDu3g",
    "channelIsVerified": false,
    "searchQuery": "web scraping",
    "scrapedAt": "2026-10-24T11:27:11Z"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 videos**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| 100 videos for one keyword | 100 | $0.10 |
| 500 videos for each of 4 keywords | 2,000 | $2.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **About 500 videos per keyword.** This is YouTube's own limit. To get more, use several related keywords, different sort orders or upload dates.
- **Dates are estimates.** Search results show relative times such as "2 weeks ago". The Actor keeps that text and adds an estimated date in `publishedAtEstimated`.
- **Likes and comment counts are not in search results.** For those, feed the `url` values into the [YouTube Scraper](https://apify.com/pipiagent/youtube-scraper) in video details mode.
- **"Recent first" is not strictly by date.** YouTube mixes in some relevance.

---

Full documentation, all input options and a free trial: **[YouTube Search Scraper on Apify](https://apify.com/pipiagent/youtube-search-scraper)**
