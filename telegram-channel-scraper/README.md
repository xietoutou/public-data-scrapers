# Telegram Channel Scraper

Extract posts and channel facts from public [Telegram](https://telegram.org) channels. Telegram has more than 1 billion monthly users, and its channels are a main source for news, crypto, politics and brand communities. Use this Actor for media monitoring, competitor tracking, research, trend analysis and training data.

- **Three kinds of data in one Actor.** Channel posts, keyword search inside channels, and channel info with subscriber counts.
- **No login, no phone number, no API key.** The Actor reads the public web preview that Telegram shows to every visitor.
- **Rich posts.** Text, views, reactions, photos and videos, link previews, hashtags, mentions, polls, forwards and replies.
- **Clean output.** English field names like `views`, `postedAt` and `subscribers`, numbers as numbers ("12.3K" becomes 12300), dates in ISO format. Text stays in the original language.
- **Low price.** $1 per 1,000 results.

**Run it online, without code:** [Telegram Channel Scraper - Posts, Messages, Views & Reactions](https://apify.com/pipiagent/telegram-channel-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `telegram-channel-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Posts of channels | One post | Text, date, views, reactions, media files, link preview, links, hashtags, mentions, poll, forward and reply info |
| Search inside channels | One post | The same fields, only for posts that contain your keyword |
| Channel info | One channel | Name, description, exact subscriber count, photo, video, file and link counts, avatar, verified badge, date of the latest post |

You can also paste links to single posts and get exactly those posts.

**Step-by-step tutorial:** [How to Export Public Telegram Channel Posts to CSV (Text, Views, Dates, Links) Without an Account or API Key](https://dev.to/frank0306_2838afa1791aac9/how-to-export-public-telegram-channel-posts-to-csv-text-views-dates-links-without-an-account-17kg)

## Input examples

Get the newest 200 posts of each channel:

```json
{
    "mode": "posts",
    "channels": ["telegram", "durov"],
    "maxItemsPerChannel": 200,
    "maxItems": 400
}
```

Get all posts of the last 7 days:

```json
{
    "mode": "posts",
    "channels": ["https://t.me/binance_announcements"],
    "postedAfter": "7 days",
    "maxItems": 1000
}
```

Find posts that mention a keyword:

```json
{
    "mode": "search",
    "channels": ["durov", "telegram"],
    "searchQuery": "TON"
}
```

Get subscriber counts and descriptions:

```json
{
    "mode": "channelInfo",
    "channels": ["durov", "telegram", "nytimes"]
}
```

Get single posts:

```json
{
    "mode": "posts",
    "channels": [],
    "postUrls": ["https://t.me/telegram/105"]
}
```

## Output examples

A post (some empty fields are left out here to keep the example short):

```json
{
    "type": "post",
    "channel": "telegram",
    "channelTitle": "Telegram News",
    "messageId": 445,
    "url": "https://t.me/telegram/445",
    "text": "For all the features from this update, like statistics and custom limits for polls, streaming text for bots, silent scheduled messages and more – check out the full blog:\nhttps://telegram.org/blog/ai-bot-revolution-11-new-features\n\nMay Features\n1 • 2 • 3 • 4 • 5 • More",
    "textHtml": "For all the features from this update, like <b>statistics</b> and <b>custom limits</b> for polls, ...",
    "postedAt": "2026-05-14T16:09:50Z",
    "views": 2930000,
    "isEdited": false,
    "authorSignature": null,
    "forwardedFromName": null,
    "forwardedFromUrl": null,
    "replyToMessageId": null,
    "mediaTypes": [],
    "mediaCount": 0,
    "media": [],
    "linkPreviewUrl": "https://telegram.org/blog/ai-bot-revolution-11-new-features",
    "linkPreviewTitle": "Guest AI Bots, Bot-to-Bot Chats, Chat Automation, Custom AI Styles, 100M+ Emoji & Sticker Search and Much More",
    "linkPreviewSite": "Telegram",
    "links": [
        "https://telegram.org/blog/ai-bot-revolution-11-new-features",
        "https://t.me/telegram/440"
    ],
    "hashtags": [],
    "mentions": [],
    "reactionsTotal": null,
    "reactions": [],
    "scrapedAt": "2026-09-29T11:58:10Z"
}
```

The media, reactions and poll parts of other posts look like this:

```json
{
    "mediaTypes": ["video"],
    "mediaCount": 1,
    "media": [
        {
            "type": "video",
            "url": "https://cdn4.telesco.pe/file/12ce1e3294.mp4?token=...",
            "thumbnailUrl": "https://cdn4.telesco.pe/file/Hu_Vcz19B6W2...",
            "durationSeconds": 27,
            "messageId": 78147,
            "isSpoiler": false
        }
    ],
    "reactionsTotal": 111,
    "reactions": [
        {"emoji": "❤", "count": 54, "isPaid": false, "customEmojiId": null},
        {"emoji": "👍", "count": 25, "isPaid": false, "customEmojiId": null}
    ],
    "pollQuestion": "Which feature you would like us to build next?",
    "pollType": "Anonymous Poll",
    "pollMultipleChoice": false,
    "pollVoters": 627000,
    "pollOptions": [
        {"text": "Video calls", "percent": 62.0},
        {"text": "Group voice calls", "percent": 16.0},
        {"text": "Folders for chats", "percent": 22.0}
    ]
}
```

A channel:

```json
{
    "type": "channel",
    "entityType": "channel",
    "username": "durov",
    "name": "Pavel Durov",
    "url": "https://t.me/durov",
    "previewUrl": "https://t.me/s/durov",
    "hasWebPreview": true,
    "description": "Founder of Telegram.",
    "subscribers": 10589274,
    "subscribersIsExact": true,
    "photosCount": 102,
    "videosCount": 46,
    "filesCount": null,
    "linksCount": 200,
    "avatarUrl": "https://cdn4.telesco.pe/file/oMgm3RFBlRf1...",
    "isVerified": true,
    "isScam": false,
    "isFake": false,
    "latestMessageId": 548,
    "latestPostAt": "2026-09-11T16:04:02Z",
    "scrapedAt": "2026-09-29T11:41:02Z"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 results**. There is no start fee and no monthly rental. A post with ten photos is still one result.

| Run | Results | Cost |
|---|---|---|
| Newest 100 posts of two channels | 100 | $0.10 |
| Info for 50 channels | 50 | $0.05 |
| 5,000 posts of a news channel | 5,000 | $5.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Public channels only.** Private channels, invite links (`t.me/+...`), groups, bots and user accounts cannot be read. The Actor skips them with a warning in the log and continues with the other channels. In channel info mode, groups and bots still return their name, description and member count.
- **Some public channels are not shown on the web.** The owner can restrict this, and Telegram hides channels that it limited, for example for adult content or copyright complaints. These channels are skipped with a warning. Channel info still returns their name, description and subscriber count, with `hasWebPreview: false`.
- **Channels blocked by country.** Telegram hides some channels in some countries. The Actor runs on Apify's servers, so a channel that is blocked there looks like it does not exist, even if you can open it at home. In our tests this happened with `rt_russian`. A proxy from another country, set in **Proxy**, can help.
- **Search returns at most about 22 posts per channel and keyword.** This is a limit of Telegram's web search. It returns the newest matching posts and stops. To get more, use several keywords in separate runs, or scrape the posts of the channel and filter them yourself.
- **Search is done by Telegram, channel by channel.** There is no search across all of Telegram. Telegram also matches word forms and link text, so a few results may not contain the exact keyword in the text.
- **No comments.** Comments under posts are not part of the web preview.
- **Views and reactions are rounded by Telegram** above 1,000, for example "12.3K" is saved as 12300. Subscriber counts in channel info are exact.
- **Some posts cannot be shown on the web.** Live streams, giveaways, paid media and some other post types appear with empty text and a `mediaNote` such as "Please open Telegram to view this post". Large videos have a thumbnail and duration but no file link, with the note "Media is too big".
- **Custom emoji reactions have no emoji character.** They are saved with `customEmojiId` and the count.
- **Media links expire.** Photo and video links point to Telegram's servers and stop working after some time. Download the files soon after the run if you need them. The Actor does not download files.
- **Albums are one result.** A post with several photos or videos is one result, with all files in `media`.
- **Service messages are skipped.** Notices like "Channel photo updated" are not saved.
- **Renamed channels.** If a channel has more than one username, the `channel` field shows the name Telegram uses in its post links, which can differ from the name you typed.
- **Speed.** About 20 posts per request and 1 to 2 requests per second, so 1,000 posts take around 1 minute. The Actor reads posts from the newest to the oldest, so reaching very old posts of a large channel takes a long time.

---

Full documentation, all input options and a free trial: **[Telegram Channel Scraper on Apify](https://apify.com/pipiagent/telegram-channel-scraper)**
