# Douban Reviews Scraper

Export reviews from [Douban](https://www.douban.com) (豆瓣), the site Chinese audiences use to rate and review movies, TV shows and books. It is China's counterpart to IMDb and Goodreads.

Use it to learn how Chinese audiences received a film, a series or a book, and to collect Chinese-language review text with star ratings for sentiment analysis.

- **Star rating on every review.** The reviewer's own 1 to 5 star score, plus useful votes, date and city.
- **Short and long reviews.** One-line reactions or full review articles.
- **English field names.** Clean JSON. Text stays in Chinese.
- **No login and no proxy needed.**
- **Low price.** $4 per 1,000 reviews.

**Run it online, without code:** [Douban Reviews Scraper - Movie, TV & Book Reviews with Stars](https://apify.com/pipiagent/douban-reviews-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `douban-reviews-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "subjectUrls": [
        "https://movie.douban.com/subject/1292052/",
        "https://book.douban.com/subject/2567698/"
    ],
    "reviewType": "shortReviews",
    "maxItems": 300
}
```

## Output example

```json
{
    "type": "shortReview",
    "reviewId": "32514679",
    "subjectId": "1292052",
    "subjectType": "movie",
    "subjectTitle": "肖申克的救赎",
    "subjectUrl": "https://movie.douban.com/subject/1292052/",
    "text": "恐惧让你沦为囚犯，希望让你重获自由。",
    "stars": 5,
    "usefulCount": 26476,
    "createdAt": "2008-02-27 21:43:23",
    "authorId": "1289463",
    "authorName": "如小果",
    "authorCity": "北京",
    "scrapedAt": "2026-09-29T10:02:41Z"
}
```

Long reviews also have `title`, `commentCount`, `shareCount` and a link to the review. `stars` is empty when the reviewer wrote without rating. Dates are in China Standard Time (UTC+8).

## How much does it cost?

You pay per saved result: **$4.00 per 1,000 reviews**. There is no start fee and no monthly rental. Getting the full text of long reviews does not change the price.

| Run | Results | Cost |
|---|---|---|
| All available short reviews of one movie | 150 | $0.60 |
| Short reviews of 20 movies | 3,000 | $12.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

Douban shows only part of its reviews to visitors who are not logged in. The Actor collects everything a visitor can see:

- **Short reviews: up to 150 per title**, the ones Douban ranks as most useful.
- **Long reviews: up to 40 per title**, the ones Douban ranks as most useful.
- **Music is not supported.**

---

Full documentation, all input options and a free trial: **[Douban Reviews Scraper on Apify](https://apify.com/pipiagent/douban-reviews-scraper)**
