# YouTube Comments Scraper

Export the comments of any [YouTube](https://www.youtube.com) video or Short, with replies if you want them, without an API key and without the quota limits of the official YouTube Data API.

Use it for sentiment analysis, product and brand research, finding questions your audience asks, moderating your own channel, or building text datasets.

- **Comments and replies.** Turn on **Include replies** to get the full threads. Each reply links to its parent comment.
- **Top or newest first.** Top comments are in the order YouTube shows them; newest first is best for monitoring.
- **Useful fields.** Likes, reply count, author and author channel, pinned and "hearted by creator" flags, and a direct link to each comment.
- **No API key, no login and no proxy setup.**
- **Low price.** $1 per 1,000 comments.

**Run it online, without code:** [YouTube Comments Scraper - Comments & Replies of Any Video](https://apify.com/pipiagent/youtube-comments-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `youtube-comments-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "videoUrls": ["https://www.youtube.com/watch?v=jNQXAC9IVRw", "https://youtu.be/dQw4w9WgXcQ"],
    "commentSort": "newest",
    "includeReplies": true,
    "maxItemsPerQuery": 2000
}
```

## Output example

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

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 comments**. A reply counts as one result. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| 500 top comments of a video | 500 | $0.50 |
| 3,000 comments with replies | 3,000 | $3.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Like counts are rounded by YouTube.** Large numbers come as "4.8M", so `likeCount` is rounded too.
- **Dates are estimates.** YouTube shows relative times such as "6 years ago". The Actor keeps that text and adds an estimated date in `publishedAtEstimated`.
- **Videos with comments turned off are skipped** with a warning, as are private and deleted videos.
- **Very large comment sections take time.** YouTube sends about 20 comments per page, so 10,000 comments take a few minutes.

---

Full documentation, all input options and a free trial: **[YouTube Comments Scraper on Apify](https://apify.com/pipiagent/youtube-comments-scraper)**
