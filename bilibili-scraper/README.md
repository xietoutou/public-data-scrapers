# Bilibili Scraper

Extract public data from [Bilibili](https://www.bilibili.com) (哔哩哔哩), China's largest video community with more than 300 million monthly users. Use it for brand monitoring in China, influencer research, trend tracking, market research and training data.

- **Eight kinds of data in one Actor.** Video search, video statistics, creator profiles, creator uploads, popular videos, the top 100 ranking, comments and danmaku.
- **English field names.** Output is clean JSON with names like `views`, `likes` and `publishedAt`, ready for spreadsheets and code. Text content stays in the original language.
- **No login and no proxy needed.** Press Start and get data.
- **Low price.** $3 per 1,000 results.

**Run it online, without code:** [Bilibili Scraper - Videos, Creators, Comments & Danmaku](https://apify.com/pipiagent/bilibili-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `bilibili-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Search videos | One video | Title, views, likes, favorites, comments, danmaku count, tags, creator, publish date |
| Video details | One video | Everything above plus coins, shares, category and publish location |
| Creator uploads | One video | Title, views, comments, publish date for every upload of a creator |
| Creator profiles | One creator | Followers, total likes, video count, level, verification, bio |
| Popular videos | One video | The videos trending on Bilibili right now, with full statistics |
| Top 100 ranking | One video | The site-wide ranking, with rank and full statistics |
| Comments | One comment | Text, likes, reply count, author, author location, images |
| Danmaku | One on-screen comment | Text, the second of the video it appears at, send time, color |

Danmaku (弹幕) are the comments that fly across the video while it plays. Each one is tied to an exact second of the video, which shows what viewers reacted to and when.

## Input examples

Search the newest videos about a brand:

```json
{
    "mode": "search",
    "searchQueries": ["耐克", "Nike"],
    "sortOrder": "pubdate",
    "maxItems": 200
}
```

Get full statistics for specific videos:

```json
{
    "mode": "videoDetails",
    "videoUrls": ["https://www.bilibili.com/video/BV1X4a36KEuH", "BV14Baa6JENd"]
}
```

Get every upload of a creator:

```json
{
    "mode": "userVideos",
    "userIds": ["https://space.bilibili.com/59905809"],
    "maxItems": 500
}
```

Get the danmaku of a video:

```json
{
    "mode": "danmaku",
    "videoUrls": ["BV1X4a36KEuH"],
    "maxItems": 5000
}
```

## Output examples

A video:

```json
{
    "type": "video",
    "bvid": "BV1X4a36KEuH",
    "aid": 117347717285664,
    "url": "https://www.bilibili.com/video/BV1X4a36KEuH",
    "title": "⚡️她连唐笑都在调上⚡️",
    "durationSeconds": 177,
    "publishedAt": "2026-09-28T09:00:00Z",
    "tags": ["手书", "鬼畜", "原神"],
    "authorId": 59905809,
    "authorName": "哦呼w",
    "authorUrl": "https://space.bilibili.com/59905809",
    "views": 883833,
    "likes": 75178,
    "coins": 13543,
    "favorites": 20400,
    "shares": 3852,
    "comments": 1770,
    "danmakuCount": 333,
    "scrapedAt": "2026-09-29T09:20:11Z"
}
```

A comment:

```json
{
    "type": "comment",
    "commentId": "315364562513",
    "videoBvid": "BV1X4a36KEuH",
    "isReply": false,
    "parentCommentId": null,
    "text": "这样真的能抓到二级号吗？",
    "likes": 320,
    "replyCount": 74,
    "publishedAt": "2026-09-28T13:30:53Z",
    "authorId": 3546929495541855,
    "authorName": "夜月三重奏",
    "authorLevel": 4
}
```

A danmaku:

```json
{
    "type": "danmaku",
    "videoBvid": "BV1X4a36KEuH",
    "text": "等会，你说在什么上？",
    "videoTimeSeconds": 12.4,
    "sentAt": "2026-09-28T09:43:42Z",
    "displayMode": "scroll",
    "color": "#ffffff"
}
```

## How much does it cost?

You pay per saved result: **$3.00 per 1,000 results**. There is no start fee and no monthly rental. Turning on **Add full statistics** does not change the price.

| Run | Results | Cost |
|---|---|---|
| 100 search results | 100 | $0.30 |
| All 355 uploads of one creator | 355 | $1.07 |
| 5,000 danmaku | 5,000 | $15.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Search returns at most 1,000 videos per keyword.** This is Bilibili's own limit. To get more, use several related keywords or different sort orders.
- **Comments are limited to the top and newest ones.** Bilibili shows visitors who are not logged in only the top and newest comments of each video, plus the first replies under them, usually 5 to 60 comments per video. The `comments` field of a video shows how many exist in total. For large volumes of viewer reactions, use danmaku.
- **Danmaku is a sample on very popular videos.** Bilibili keeps a rolling pool of a few hundred to a few thousand danmaku per video, and the Actor returns that pool.
- **Search listings do not include coins and shares.** Turn on **Add full statistics** to add them.

---

Full documentation, all input options and a free trial: **[Bilibili Scraper on Apify](https://apify.com/pipiagent/bilibili-scraper)**
