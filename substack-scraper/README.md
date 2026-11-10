# Substack Scraper

Get data from [Substack](https://substack.com) newsletters without an API key and without a login. Five modes in one Actor:

- **Posts of publications.** Every post of the newsletters you choose, newest or most popular first, with likes, comments, restacks, word count, authors and tags. Add the full text with one switch.
- **Post details.** Full text and HTML of single posts.
- **Comments.** All comments of a post, with replies, likes and authors.
- **Search.** Posts that match your keywords across all of Substack, like the search box on substack.com.
- **Publications and rankings.** Substack's category leaderboards (top paid newsletters, or all newsletters) with subscriber counts, followers and paid subscriber ranges, or the same profile data for the publications you list.

Use it for media monitoring, competitor and creator research, finding newsletters to sponsor or pitch, tracking what is said about a topic, building reading lists and RSS-like feeds, and feeding articles to AI tools.

- **Type a URL, a subdomain or a handle.** https://www.lennysnewsletter.com, noahpinion and @lenny all work, custom domains included.
- **Clean, flat records.** ISO dates, numbers as numbers, plain text next to the HTML, ready for spreadsheets.
- **Subscriber counts.** The number Substack shows on author profiles ("462K+ subscribers"), plus followers and the paid subscriber range ("Tens of thousands").
- **No login, no API key, no proxy.**
- **Low price.** $1 per 1,000 results.

**Run it online, without code:** [Substack Scraper - Posts, Comments, Leaderboards & Subscribers](https://apify.com/pipiagent/substack-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `substack-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Posts of publications | One post | Title, subtitle, link, publish date, type (newsletter, podcast, thread), free or paid, word count, likes, comments, restacks, authors, tags, preview text, cover image, podcast link and length. Optional: full text and HTML |
| Post details | One post | The same fields, always with full text and HTML, last update time and whether the text is cut by a paywall |
| Comments | One comment or reply | Text, date, likes, number of replies, author name and handle, parent comment, depth, pinned flag, link |
| Search | One post | Post fields plus the publication's name and link and the keyword that found it |
| Publications and rankings | One publication | Rank, category, name, link, custom domain, description, author, author bio, X/Twitter handle, creation date, paid plan benefits, subscriber count, followers, paid subscriber range, leaderboard rank |

## Input examples

Posts of two newsletters published since September, with full text:

```json
{
    "mode": "posts",
    "publications": ["https://www.lennysnewsletter.com", "noahpinion"],
    "dateFrom": "2026-09-01",
    "includeContent": true
}
```

The 20 most popular posts of a newsletter:

```json
{
    "mode": "posts",
    "publications": ["@lenny"],
    "sortBy": "top",
    "maxItems": 20
}
```

Comments and replies of a post:

```json
{
    "mode": "comments",
    "postUrls": ["https://charlesduhigg.substack.com/p/the-robots-are-coming-and-i-feel"]
}
```

Posts about AI agents from this year, across all of Substack:

```json
{
    "mode": "search",
    "searchQueries": ["ai agents"],
    "dateFrom": "2026-01-01",
    "maxItems": 200
}
```

The top 100 paid newsletters in Technology and Finance, with subscriber counts:

```json
{
    "mode": "publications",
    "categories": ["4", "153"],
    "ranking": "paid",
    "maxItemsPerQuery": 100
}
```

## Output examples

A post:

```json
{
    "type": "post",
    "postId": 174637920,
    "title": "Artificial intelligence is taking over the world!",
    "subtitle": "What's the best way to learn about artificial intelligence? Which apps should I be using?",
    "url": "https://charlesduhigg.substack.com/p/the-robots-are-coming-and-i-feel",
    "publishedAt": "2025-09-27T10:57:16Z",
    "postType": "newsletter",
    "audience": "everyone",
    "isPaid": false,
    "wordCount": 782,
    "reactionCount": 91,
    "commentCount": 14,
    "restackCount": 4,
    "authors": ["Charles Duhigg"],
    "authorHandles": ["charlesduhigg"],
    "tags": [],
    "previewText": "I live near Silicon Valley, where conventional wisdom holds there are three ways to become a billionaire:",
    "publicationId": 1810583,
    "publicationName": "The Science of Better",
    "publicationUrl": "https://charlesduhigg.substack.com",
    "isPaywalled": false,
    "text": "I live near Silicon Valley, where conventional wisdom holds there are three ways to become a billionaire:\n- Be born to a billionaire and then wait.\n...",
    "html": "<p>I live near Silicon Valley, ...</p>"
}
```

A publication from a leaderboard:

```json
{
    "type": "publication",
    "rank": 1,
    "category": "Technology",
    "ranking": "paid",
    "publicationId": 6349492,
    "name": "SemiAnalysis",
    "url": "https://newsletter.semianalysis.com",
    "subdomain": "semianalysis",
    "customDomain": "newsletter.semianalysis.com",
    "description": "Bridging the gap between the world's most important industry, semiconductors, and business.",
    "authorName": "Dylan Patel",
    "authorHandle": "semianalysis",
    "twitter": "dylan522p",
    "hasPaidPlan": true,
    "subscriberCount": 325000,
    "subscriberCountText": "325K+ subscribers",
    "paidSubscribersRange": "Tens of thousands",
    "followerCount": 378966,
    "leaderboardRank": 1
}
```

A comment:

```json
{
    "type": "comment",
    "commentId": 160837451,
    "commentUrl": "https://charlesduhigg.substack.com/p/the-robots-are-coming-and-i-feel/comment/160837451",
    "postTitle": "Artificial intelligence is taking over the world!",
    "isReply": true,
    "parentCommentId": 160496861,
    "depth": 1,
    "text": "nuts! it used to be free!",
    "createdAt": "2025-09-28T17:33:23Z",
    "reactionCount": 0,
    "authorName": "Charles Duhigg",
    "authorHandle": "charlesduhigg"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 results**. A post, a comment, a reply and a publication each count as one result. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| The last 100 posts of a newsletter | 100 | $0.10 |
| 1,000 search results with full text | 1,000 | $1.00 |
| Top 500 paid newsletters of a category | 500 | $0.50 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Paid posts give only the free part.** Without a subscription, Substack shows the beginning of a paid post. The Actor saves that part and sets `isPaywalled` to true. It does not log in and cannot read paid content.
- **The Actor is polite, so big runs take time.** It waits a little between requests to stay within Substack's limits: about 30 posts per second from archives, and about 1 to 2 per second with full text, comments or subscriber counts turned on.
- **Search returns what Substack's own search returns**, ordered by relevance, usually a few hundred posts per keyword. Notes and profiles in the search results are skipped.
- **Leaderboards stop at about 500 publications** per category, the same as on substack.com.
- **Subscriber counts are rounded by Substack** ("325K+"), and some authors hide them. Paid subscriber numbers are only given as ranges.
- **"Only posts about" uses the publication's archive search** and always sorts newest first.
- **This is unofficial.** The Actor reads the same public data that Substack's website loads. It is not made by, endorsed by or connected to Substack.

---

Full documentation, all input options and a free trial: **[Substack Scraper on Apify](https://apify.com/pipiagent/substack-scraper)**
