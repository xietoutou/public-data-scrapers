# Weibo Comments Scraper

Export the comments under any public post on [Weibo](https://weibo.com) (微博), China's largest microblogging platform.

Use it to measure how the public reacted to a post, a product launch or a statement, to collect Chinese-language comments for sentiment analysis, or to see which regions and which kinds of accounts are commenting.

- **Comments and replies.** Each comment comes with its likes and reply count. Turn on replies to get the full thread.
- **Who is commenting.** Region of the comment, author name, verification type and follower count.
- **English field names.** Clean JSON. Text stays in Chinese.
- **No login, no cookie and no proxy needed.**
- **Low price.** $5 per 1,000 comments.

**Run it online, without code:** [Weibo Comments Scraper - Comments & Replies of Any Post](https://apify.com/pipiagent/weibo-comments-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `weibo-comments-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "postUrls": ["https://weibo.com/1669879400/RjCH5q8hs"],
    "includeReplies": true,
    "maxItems": 1000
}
```

## Output example

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
    "authorUrl": "https://weibo.com/u/1787569845",
    "authorVerified": true,
    "authorVerifiedType": "company",
    "authorFollowers": 619498,
    "authorCity": "北京",
    "scrapedAt": "2026-09-29T11:20:05Z"
}
```

Replies have `isReply: true` and the id of the comment they answer in `parentCommentId`. Emoticons appear as codes in square brackets, for example `[期待]`.

## How much does it cost?

You pay per saved result: **$5.00 per 1,000 comments**. There is no start fee and no monthly rental. A reply counts as one result.

| Run | Results | Cost |
|---|---|---|
| 100 top comments of a post | 100 | $0.50 |
| 1,000 comments of a post | 1,000 | $5.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Very large threads are not always complete.** Weibo stops serving more comments after some depth, which differs from post to post.
- **You need the post URL.** Weibo requires login to search posts or to list the posts of a user, so the Actor cannot find posts for you. To get started without a URL, use the trending posts mode of the Weibo Scraper below.
- **Deleted posts and posts hidden from visitors are skipped** with a warning.

---

Full documentation, all input options and a free trial: **[Weibo Comments Scraper on Apify](https://apify.com/pipiagent/weibo-comments-scraper)**
