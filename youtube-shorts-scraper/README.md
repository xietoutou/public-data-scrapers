# YouTube Shorts Scraper

Extract [YouTube Shorts](https://www.youtube.com/shorts) by keyword or from any channel, without an API key and without the quota limits of the official YouTube Data API.

Use it to find the Shorts that went viral in your niche, to track what competitors and creators post, to research hooks and hashtags, or to collect short-video data for analysis.

- **Two ways in.** Search Shorts by keyword, or list all Shorts of a channel.
- **The numbers that matter.** Exact views, likes, comment count, publish date, hashtags and the channel of every Short.
- **No API key, no login and no proxy setup.** Press Start and get data.
- **Low price.** $1 per 1,000 Shorts.

**Run it online, without code:** [YouTube Shorts Scraper - Views, Likes, Channels & Hashtags](https://apify.com/pipiagent/youtube-shorts-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `youtube-shorts-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input examples

Shorts about two topics from this month:

```json
{
    "searchQueries": ["cooking hacks", "air fryer recipes"],
    "uploadDate": "month",
    "maxItems": 200
}
```

The latest Shorts of two creators:

```json
{
    "channelUrls": ["@MrBeast", "https://www.youtube.com/@NicksKitchen"],
    "maxItemsPerQuery": 50
}
```

## Output example

```json
{
    "type": "video",
    "videoId": "hE6xmg9Mmkc",
    "url": "https://www.youtube.com/shorts/hE6xmg9Mmkc",
    "title": "Tomato Slicing Hack",
    "viewCount": 82360339,
    "likeCount": 1365156,
    "commentCount": 4189,
    "durationSeconds": 17,
    "publishedAt": "2025-04-16T16:01:44Z",
    "isShort": true,
    "description": "#tomato #chef #shorts",
    "hashtags": ["#tomato", "#shorts", "#chef"],
    "channelName": "Nick's Kitchen",
    "channelId": "UC2HNqPgeKtVr2gZmLeeIk3g",
    "channelHandle": "@NicksKitchen",
    "channelUrl": "https://www.youtube.com/channel/UC2HNqPgeKtVr2gZmLeeIk3g",
    "thumbnailUrl": "https://i.ytimg.com/vi/hE6xmg9Mmkc/hqdefault.jpg",
    "searchQuery": "cooking hacks",
    "scrapedAt": "2026-10-24T11:26:35Z"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 Shorts**. There is no start fee and no monthly rental. **Add full details** does not change the price.

| Run | Results | Cost |
|---|---|---|
| 100 Shorts for one keyword | 100 | $0.10 |
| 500 Shorts of a channel | 500 | $0.50 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **About 100 Shorts per keyword.** YouTube stops the Shorts search list at roughly 100 to 140 results. Changing the sort order or upload date adds only a few more. To get more, use several related keywords.
- **No "most viewed" sort.** YouTube returns nothing for Shorts sorted by views. Sort the downloaded table by `viewCount` instead.
- **Upload date filters shrink the list a lot.** With "This week" YouTube often returns only about a dozen Shorts for a keyword, and once in a while none.
- **Without full details, Shorts have only a title and a view count.** The view count is then rounded by YouTube ("40M"). Keep **Add full details** on for exact numbers and the channel.
- **Full details make runs slower.** The Actor opens every Short, so 100 Shorts take about 2 minutes, compared with about 10 seconds without it.
- **Channel Shorts come newest first.** YouTube does not offer another order for a channel.
- **Duplicates across keywords are kept.** Each result has a `searchQuery` field that says which keyword found it.

---

Full documentation, all input options and a free trial: **[YouTube Shorts Scraper on Apify](https://apify.com/pipiagent/youtube-shorts-scraper)**
