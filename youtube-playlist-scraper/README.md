# YouTube Playlist Scraper

Export every video of any public [YouTube](https://www.youtube.com) playlist, in playlist order, without an API key and without the quota limits of the official YouTube Data API.

Use it to save a course or tutorial series as a table, to analyze a creator's series, to track playlists that a brand or a music label curates, or to collect video lists for research and AI datasets.

- **Every video, in order.** Each result has its `playlistPosition`, page after page until the playlist ends or your limit is reached. A 246-video playlist takes about 3 seconds.
- **Playlist details on every row.** Title, description, owner, number of videos and total views of the playlist.
- **Videos from any channel.** Playlists that mix channels keep the right channel on each video.
- **Numbers you can sort.** Text like "1.3M views" is parsed into a number, and the original text is kept.
- **No API key, no login and no proxy setup.**
- **Low price.** $1 per 1,000 videos.

**Run it online, without code:** [YouTube Playlist Scraper - All Videos of Any Playlist](https://apify.com/pipiagent/youtube-playlist-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `youtube-playlist-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "playlistUrls": [
        "https://www.youtube.com/playlist?list=PL4cUxeGkcC9gcy9lrvMJ75z9maRw4byYp",
        "https://www.youtube.com/watch?v=17WoOqgXsRM&list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH"
    ],
    "maxItemsPerQuery": 500
}
```

## Output example

```json
{
    "type": "video",
    "videoId": "X0kjv0MozuY",
    "url": "https://www.youtube.com/watch?v=X0kjv0MozuY",
    "title": "Coding Challenge #103: Fire Effect",
    "viewCount": 108000,
    "viewCountText": "108K views",
    "durationSeconds": 1776,
    "durationText": "29:36",
    "publishedTimeText": "8 years ago",
    "publishedAtEstimated": "2018-10-30T20:39:00Z",
    "isLive": false,
    "isShort": false,
    "channelName": "The Coding Train",
    "channelId": "UCvjgXvBlbQiydffZU7m1_aw",
    "channelHandle": "@TheCodingTrain",
    "channelUrl": "https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw",
    "channelIsVerified": true,
    "thumbnailUrl": "https://i.ytimg.com/vi/X0kjv0MozuY/hqdefault.jpg",
    "playlistPosition": 151,
    "playlistId": "PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH",
    "playlistUrl": "https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH",
    "playlistTitle": "Coding Challenges",
    "playlistDescription": "Is it the gravy train or a train wreck? Watch me take on some viewer submitted coding projects!",
    "playlistOwnerName": "The Coding Train",
    "playlistOwnerId": "UCvjgXvBlbQiydffZU7m1_aw",
    "playlistVideoCount": 246,
    "playlistViewCount": 2720005,
    "scrapedAt": "2026-10-28T20:39:00Z"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 videos**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| One tutorial series | 40 | $0.04 |
| A 250-video playlist | 250 | $0.25 |
| A channel's full uploads playlist with 2,000 videos | 2,000 | $2.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Public and unlisted playlists only.** Private playlists, Watch Later and Liked videos need a login and are skipped.
- **Mixes cannot be scraped.** Playlists whose id starts with `RD` are generated for each viewer.
- **Private, deleted and unavailable videos are left out**, as YouTube hides them from the playlist page. So the number of results can be lower than `playlistVideoCount`.
- **Dates are estimates.** Playlists show relative times such as "8 years ago". The Actor keeps that text and adds an estimated date in `publishedAtEstimated`. For exact dates and likes, feed the `url` values into the [YouTube Scraper](https://apify.com/pipiagent/youtube-scraper) in video details mode.
- **Likes and comment counts are not in the playlist.** YouTube does not show them there.

---

Full documentation, all input options and a free trial: **[YouTube Playlist Scraper on Apify](https://apify.com/pipiagent/youtube-playlist-scraper)**
