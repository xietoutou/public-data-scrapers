# YouTube Channel Videos Scraper

Export every video of any [YouTube](https://www.youtube.com) channel, without an API key and without the quota limits of the official YouTube Data API.

Use it to audit a competitor's channel, to track what creators publish, to build a list of videos for analysis, or to monitor channels on a schedule.

- **Every upload.** Videos come newest first, page after page, until the channel ends or your limit is reached.
- **Numbers you can sort.** Text like "27K views" is parsed into a number, and the original text is kept.
- **Shorts and live streams on request.** Two switches add them.
- **No API key, no login and no proxy setup.**
- **Low price.** $1 per 1,000 videos.

**Step-by-step tutorial:** [How to Export a YouTube Channel's Full Upload History and Find Its Best-Performing Topics](https://dev.to/frank0306_2838afa1791aac9/how-to-export-a-youtube-channels-full-upload-history-and-find-its-best-performing-topics-2i1e)

**Run it online, without code:** [YouTube Channel Videos Scraper - All Uploads with Stats](https://apify.com/pipiagent/youtube-channel-videos-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `youtube-channel-videos-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "channelUrls": ["@GoogleDevelopers", "https://www.youtube.com/@MrBeast"],
    "maxItemsPerQuery": 500,
    "includeShorts": true
}
```

## Output example

```json
{
    "type": "video",
    "videoId": "SOF3_evPje8",
    "url": "https://www.youtube.com/watch?v=SOF3_evPje8",
    "title": "Design and replicate voices with Gemini 3.8 Flash TTS",
    "viewCount": 27000,
    "viewCountText": "27K views",
    "durationSeconds": 849,
    "durationText": "14:09",
    "publishedTimeText": "2 days ago",
    "publishedAtEstimated": "2026-10-22T11:27:14Z",
    "isLive": false,
    "isShort": false,
    "channelName": "Google for Developers",
    "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "channelHandle": "@GoogleDevelopers",
    "channelUrl": "https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "channelTab": "videos",
    "scrapedAt": "2026-10-24T11:27:14Z"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 videos**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| The last 100 videos of a channel | 100 | $0.10 |
| A channel with 2,000 uploads | 2,000 | $2.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Dates in this list are estimates.** YouTube shows relative times such as "2 days ago". The Actor keeps that text and adds an estimated date in `publishedAtEstimated`. For exact dates and likes, feed the `url` values into the [YouTube Scraper](https://apify.com/pipiagent/youtube-scraper) in video details mode.
- **Likes and comment counts are not in this list.** YouTube does not show them on the channel page.
- **Shorts in this list have only a title and a view count.** For full Shorts data use the [YouTube Shorts Scraper](https://apify.com/pipiagent/youtube-shorts-scraper).
- **Members-only and private videos are not listed.**

---

Full documentation, all input options and a free trial: **[YouTube Channel Videos Scraper on Apify](https://apify.com/pipiagent/youtube-channel-videos-scraper)**
