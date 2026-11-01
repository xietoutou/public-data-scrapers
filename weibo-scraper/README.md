# Weibo Scraper

Extract public data from [Weibo](https://weibo.com) (微博), China's largest microblogging platform with more than 500 million monthly users. Weibo is where news breaks and where brands, celebrities and the public talk to each other in China.

Use it to track what is trending in China, to measure the reaction to a post or a campaign, to collect Chinese-language comments for sentiment analysis, or to check the reach of an influencer.

- **Full comment threads.** Collect the comments under any public post, with replies, likes and the region each comment was posted from.
- **Hot search chart.** The live ranking of trending topics with heat scores and categories.
- **English field names.** Output is clean JSON with names like `likes`, `reposts` and `createdAt`. Text content stays in Chinese.
- **No login, no cookie and no proxy needed.** Press Start and get data.
- **Low price.** $5 per 1,000 results.

**Run it online, without code:** [Weibo Scraper - Hot Search, Trending Posts, Comments & Profiles](https://apify.com/pipiagent/weibo-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `weibo-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Hot search chart | One trending topic | Rank, topic, heat score, category, label, time on chart |
| Trending posts | One post | Text, likes, comments, reposts, images, video, author, region |
| Post details | One post | The same fields for the posts you list, with the full text of long posts |
| Comments | One comment or reply | Text, likes, reply count, date, region, author, author followers |
| User profiles | One account | Followers, following, post count, total likes received, verification, bio, location, company, school |

## Input examples

The hot search chart right now:

```json
{
    "mode": "trends"
}
```

Comments and replies of a post:

```json
{
    "mode": "comments",
    "postUrls": ["https://weibo.com/1669879400/RjCH5q8hs"],
    "includeReplies": true,
    "maxItems": 1000
}
```

Profiles of accounts:

```json
{
    "mode": "profiles",
    "users": ["人民日报", "https://weibo.com/u/1669879400"]
}
```

## Output examples

A trending topic:

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

A comment:

```json
{
    "type": "comment",
    "commentId": "5346770336090639",
    "postId": "5346769756228362",
    "postUrl": "https://weibo.com/1669879400/RjCH5q8hs",
    "isReply": false,
    "parentCommentId": null,
    "text": "迪迪抱抱[期待][期待]",
    "createdAt": "2026-09-24T12:27:29Z",
    "likes": 18810,
    "replyCount": 1474,
    "postedFrom": "江苏",
    "likedByPostAuthor": false,
    "authorId": "1787569845",
    "authorName": "护舒宝",
    "authorVerified": true,
    "authorVerifiedType": "company",
    "authorFollowers": 619498,
    "authorCity": "北京"
}
```

A user profile:

```json
{
    "type": "user",
    "userId": "2803301701",
    "name": "人民日报",
    "url": "https://weibo.com/u/2803301701",
    "bio": "人民日报法人微博。参与、沟通、记录时代。",
    "location": "北京",
    "followers": 158011657,
    "following": 3096,
    "posts": 153707,
    "totalLikesReceived": 2527373228,
    "isVerified": true,
    "verifiedType": "media",
    "verifiedReason": "《人民日报》法人微博",
    "joinedAt": "2012-07-22 02:28:35"
}
```

Dates are in UTC, except `joinedAt`, which is in China Standard Time (UTC+8). Emoticons appear as codes in square brackets, for example `[期待]`.

## How much does it cost?

You pay per saved result: **$5.00 per 1,000 results**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| The hot search chart | about 50 | $0.25 |
| 1,000 comments of a post | 1,000 | $5.00 |
| 100 user profiles | 100 | $0.50 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

Weibo shows only part of its content to visitors who are not logged in. The Actor collects what a visitor can see:

- **Keyword search is not included.** Weibo requires login to search posts.
- **A user's post history is not included.** Weibo requires login to open the list of posts on a profile. You can still get any post when you have its URL.
- **Repost lists are not included.**
- **Comments are not always complete on very large threads.** Weibo stops serving more comments after some depth, which differs from post to post. The `comments` field of the post shows how many exist in total.
- **Trending posts are a sample.** The feed returns what Weibo recommends at that moment and changes on every run.

---

Full documentation, all input options and a free trial: **[Weibo Scraper on Apify](https://apify.com/pipiagent/weibo-scraper)**
