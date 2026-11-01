# Bilibili Danmaku Scraper

Export danmaku (弹幕, also called bullet comments) from [Bilibili](https://www.bilibili.com) videos. Danmaku are the comments that fly across the video while it plays. Each one is tied to an exact second of the video, so they show what viewers reacted to and when.

Use it to find the moments of a video that got the strongest reaction, to analyze audience sentiment in China, or to build Chinese-language text datasets.

- **Timestamped.** Every danmaku has the second of the video it appears at and the time it was sent.
- **English field names.** Clean JSON, ready for spreadsheets and code. Text stays in Chinese.
- **No login and no proxy needed.**
- **Low price.** $3 per 1,000 danmaku.

**Run it online, without code:** [Bilibili Danmaku Scraper - Bullet Comments with Timestamps](https://apify.com/pipiagent/bilibili-danmaku-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `bilibili-danmaku-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "videoUrls": ["https://www.bilibili.com/video/BV14Baa6JENd", "BV1X4a36KEuH"],
    "maxItems": 5000
}
```

## Output example

```json
{
    "type": "danmaku",
    "danmakuId": "2217085943611977472",
    "videoBvid": "BV14Baa6JENd",
    "videoTitle": "《原神》六周年主题曲《风的来信》",
    "videoUrl": "https://www.bilibili.com/video/BV14Baa6JENd",
    "cid": 42251257840,
    "text": "六周年快乐！",
    "videoTimeSeconds": 2.02,
    "sentAt": "2026-10-07T15:54:00Z",
    "displayMode": "scroll",
    "color": "#ffffff",
    "userHash": "98f1491f",
    "scrapedAt": "2026-10-10T13:51:56Z"
}
```

`displayMode` is `scroll`, `top` or `bottom`. `userHash` is Bilibili's anonymous id of the sender: the same viewer has the same hash, but it does not reveal the account.

## How much does it cost?

You pay per saved result: **$3.00 per 1,000 danmaku**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| Danmaku of one typical video | about 300 | $0.90 |
| Danmaku of one very popular video | about 2,300 | $6.90 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Very popular videos return a sample.** Bilibili keeps a rolling pool of a few hundred to a few thousand danmaku per video, and the Actor returns that pool. Older danmaku that Bilibili has rotated out are not available.
- **Videos with several parts** return the danmaku of every part, with a `videoPart` number.
- **Deleted and private videos are skipped** with a warning.

---

Full documentation, all input options and a free trial: **[Bilibili Danmaku Scraper on Apify](https://apify.com/pipiagent/bilibili-danmaku-scraper)**
