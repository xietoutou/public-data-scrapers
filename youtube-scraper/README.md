# YouTube Scraper

Extract public data from [YouTube](https://www.youtube.com) without an API key and without the quota limits of the official YouTube Data API. Use it for influencer research, competitor tracking, content research, comment analysis and training data.

- **Seven kinds of data in one Actor.** Video search, all uploads of a channel, Shorts, playlist videos, full video details, comments with replies, and channel profiles.
- **Numbers you can sort.** Text like "1.2M views" is parsed into a number. The original text is kept in a separate field.
- **No API key, no login and no proxy setup.** Press Start and get data.
- **Low price.** $1 per 1,000 results.

**Run it online, without code:** [YouTube Scraper - Search, Channel Videos, Comments & Details](https://apify.com/pipiagent/youtube-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `youtube-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Search videos | One video | Title, views, duration, publish time, channel, thumbnail |
| Channel videos | One video | The same fields for every upload of a channel |
| Playlist videos | One video | Every video of a playlist with its position, plus the playlist title, owner and size |
| Shorts | One Short | Shorts by keyword or of a channel. With "Shorts: add full details" on: channel, exact views, likes, comments, publish date, hashtags |
| Video details | One video | Full description, exact views, likes, comment count, exact publish date, keywords, category, channel subscribers |
| Comments | One comment or reply | Text, likes, reply count, author, pinned and hearted flags |
| Channel details | One channel | Subscribers, video count, total views, description, country, join date, links |

## Input examples

Search videos uploaded this month:

```json
{
    "mode": "search",
    "searchQueries": ["web scraping", "python tutorial"],
    "uploadDate": "month",
    "maxItems": 200
}
```

All uploads of two channels:

```json
{
    "mode": "channelVideos",
    "channelUrls": ["@GoogleDevelopers", "https://www.youtube.com/@MrBeast"],
    "maxItemsPerQuery": 500,
    "maxItems": 1000
}
```

Every video of a playlist, in playlist order:

```json
{
    "mode": "playlist",
    "playlistUrls": ["https://www.youtube.com/playlist?list=PL4cUxeGkcC9gcy9lrvMJ75z9maRw4byYp"],
    "maxItems": 1000
}
```

Comments and replies of a video, newest first:

```json
{
    "mode": "comments",
    "videoUrls": ["https://www.youtube.com/watch?v=jNQXAC9IVRw"],
    "commentSort": "newest",
    "includeReplies": true,
    "maxItems": 5000
}
```

## Output examples

Video details:

```json
{
    "type": "video",
    "videoId": "jNQXAC9IVRw",
    "url": "https://www.youtube.com/watch?v=jNQXAC9IVRw",
    "title": "Me at the zoo",
    "viewCount": 438341989,
    "viewCountText": "438,341,989 views",
    "likeCount": 19960247,
    "commentCount": 10631026,
    "publishedAt": "2005-04-24T03:31:52Z",
    "durationSeconds": 19,
    "keywords": ["me at the zoo", "jawed karim", "first youtube video"],
    "category": "Film & Animation",
    "isLive": false,
    "channelName": "jawed",
    "channelId": "UC4QobU6STFB0P71PMvOGN5A",
    "channelHandle": "@jawed",
    "channelUrl": "https://www.youtube.com/channel/UC4QobU6STFB0P71PMvOGN5A",
    "channelSubscriberCount": 6640000,
    "thumbnailUrl": "https://i.ytimg.com/vi/jNQXAC9IVRw/hqdefault.jpg",
    "commentsEnabled": true,
    "scrapedAt": "2026-09-29T21:48:01Z"
}
```

A comment:

```json
{
    "type": "comment",
    "commentId": "UgzuC3zzpRZkjc5Qzsd4AaABAg",
    "commentUrl": "https://www.youtube.com/watch?v=jNQXAC9IVRw&lc=UgzuC3zzpRZkjc5Qzsd4AaABAg",
    "videoId": "jNQXAC9IVRw",
    "videoTitle": "Me at the zoo",
    "isReply": false,
    "parentCommentId": null,
    "text": "We're so honored that the first ever YouTube video was filmed here!",
    "likeCount": 4800000,
    "likeCountText": "4.8M",
    "replyCount": 985,
    "publishedTimeText": "6 years ago",
    "publishedAtEstimated": "2020-09-30T21:48:05Z",
    "isPinned": true,
    "isHeartedByCreator": true,
    "authorName": "@SanDiegoZoo",
    "authorChannelUrl": "https://www.youtube.com/channel/UCC5NfQ6Mf0dq_eEwv4P_hWA",
    "authorIsVerified": true
}
```

A channel:

```json
{
    "type": "channel",
    "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "url": "https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "handle": "@GoogleDevelopers",
    "name": "Google for Developers",
    "subscriberCount": 2680000,
    "videoCount": 6099,
    "totalViews": 360437715,
    "country": "United States",
    "joinedDate": "2007-08-23",
    "rssUrl": "https://www.youtube.com/feeds/videos.xml?channel_id=UC_x5XG1OV2P6uZZ5FSM9Ttw"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 results**. There is no start fee and no monthly rental. A video, a comment, a reply and a channel each count as one result.

| Run | Results | Cost |
|---|---|---|
| 100 search results | 100 | $0.10 |
| 2,000 uploads of a channel | 2,000 | $2.00 |
| 3,000 comments of a video | 3,000 | $3.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Search returns about 500 videos per keyword.** This is YouTube's own limit. To get more, use several related keywords or different sort orders.
- **Dates in lists are estimates.** Search results, channel uploads, playlists and comments only show relative times such as "3 years ago". The Actor keeps that text and adds an estimated date in `publishedAtEstimated`. Video details mode returns the exact publish date.
- **Large numbers are rounded by YouTube.** Subscriber counts, and like counts on comments, come as "2.68M" or "4.8M", so the numeric value is rounded too. Video details mode returns exact views and likes.
- **Transcripts and video downloads are not included.**
- **Private, deleted and age-restricted videos are skipped** with a warning.
- **Shorts and live streams of a channel are off by default.** Turn them on with the two switches in the input.

---

Full documentation, all input options and a free trial: **[YouTube Scraper on Apify](https://apify.com/pipiagent/youtube-scraper)**
