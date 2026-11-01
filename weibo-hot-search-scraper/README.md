# Weibo Hot Search Scraper

Get the live hot search chart (微博热搜) of [Weibo](https://weibo.com), China's largest microblogging platform. The chart is the most watched ranking of what people in China are talking about right now.

Use it to follow public attention in China, to spot a brand or a crisis the moment it trends, or to build a history of trending topics for research.

- **The whole chart in seconds.** About 50 topics with rank, heat score, category and label.
- **Two charts.** All topics, or entertainment only.
- **Made for schedules.** Run it every 10 or 30 minutes and you get a time series of what trended and for how long.
- **No login, no cookie and no proxy needed.**
- **Low price.** $5 per 1,000 results, about $0.25 for a full chart.

**Run it online, without code:** [Weibo Hot Search Scraper - Trending Topics in China](https://apify.com/pipiagent/weibo-hot-search-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `weibo-hot-search-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "chart": "hotSearch"
}
```

## Output example

```json
{
    "type": "trend",
    "chart": "hotSearch",
    "rank": 1,
    "topic": "房贷贴息1个百分点",
    "heat": 3020516,
    "category": "财经",
    "label": "新",
    "onChartSince": "2026-09-29T10:20:21Z",
    "url": "https://s.weibo.com/weibo?q=%23%E6%88%BF%E8%B4%B7%E8%B4%B4%E6%81%AF1%E4%B8%AA%E7%99%BE%E5%88%86%E7%82%B9%23",
    "scrapedAt": "2026-09-29T11:20:05Z"
}
```

`label` is Weibo's own tag for the topic: 新 means new, 热 means hot, 爆 means exploding. `heat` is Weibo's popularity score.

## How much does it cost?

You pay per saved result: **$5.00 per 1,000 results**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| One full chart | about 50 | $0.25 |
| The chart every 30 minutes for a day | about 2,400 | $12.00 |
| Only the top 10, every hour for a day | 240 | $1.20 |

Use **Max results** to save only the top of the chart and lower the cost.

## Limits you should know

- **The chart has no history.** Weibo shows only the current ranking. To get history, run the Actor on a schedule.
- **Promoted entries are left out.** Paid placements have no rank, so the Actor skips them.
- **Posts under a topic are not included.** Weibo requires login to search posts.

---

Full documentation, all input options and a free trial: **[Weibo Hot Search Scraper on Apify](https://apify.com/pipiagent/weibo-hot-search-scraper)**
