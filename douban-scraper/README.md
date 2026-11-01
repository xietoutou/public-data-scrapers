# Douban Scraper

Extract ratings and reviews from [Douban](https://www.douban.com) (豆瓣), the site Chinese audiences use to rate movies, TV shows and books. It is China's counterpart to IMDb and Goodreads, and a Douban score often decides how a release performs in China.

Use it to measure how Chinese audiences received a film, series or book, to collect Chinese-language review text for sentiment analysis, or to track charts over time.

- **Reviews with star ratings.** Each review comes with the reviewer's own 1 to 5 star score, useful votes, date and city.
- **Rating breakdown.** Get the share of 1 to 5 star ratings, not just the average.
- **English field names.** Output is clean JSON with names like `rating`, `stars` and `usefulCount`. Text content stays in Chinese.
- **No login and no proxy needed.**
- **Low price.** $4 per 1,000 results.

**Run it online, without code:** [Douban Scraper - Movie, TV & Book Ratings and Reviews](https://apify.com/pipiagent/douban-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `douban-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Short reviews | One short review | Text, stars, useful votes, date, author, author city |
| Long reviews | One review article | Title, text, stars, useful votes, comment count, author |
| Details | One movie, TV show or book | Rating, number of ratings, rating breakdown, cast, genres, summary, review counts, watched and wishlist counts |
| Charts | One title on a chart | Rank, title, rating, number of ratings |
| Find titles | One matching title | Title, type, rating, Douban URL |

## Input examples

Short reviews of two movies:

```json
{
    "mode": "shortReviews",
    "subjectUrls": [
        "https://movie.douban.com/subject/1292052/",
        "https://movie.douban.com/subject/26266893/"
    ],
    "maxItems": 300
}
```

Long reviews of a book, with full text:

```json
{
    "mode": "reviews",
    "subjectUrls": ["https://book.douban.com/subject/2567698/"],
    "includeFullText": true
}
```

The Top 250 movies:

```json
{
    "mode": "chart",
    "chart": "movieTop250",
    "maxItems": 250
}
```

## Output examples

A short review:

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

Details of a movie:

```json
{
    "type": "movie",
    "id": "1292052",
    "url": "https://movie.douban.com/subject/1292052/",
    "title": "肖申克的救赎",
    "originalTitle": "The Shawshank Redemption",
    "year": "1994",
    "rating": 9.7,
    "ratingCount": 3345703,
    "ratingDistribution": {"1star": 0.1, "2star": 0.1, "3star": 1.4, "4star": 13.0, "5star": 85.4},
    "shortReviewCount": 667086,
    "reviewCount": 14945,
    "watchedOrReadCount": 5745076,
    "wishlistCount": 519573,
    "genres": ["剧情", "犯罪"],
    "countries": ["美国"],
    "directors": ["弗兰克·德拉邦特"],
    "actors": ["蒂姆·罗宾斯", "摩根·弗里曼"],
    "honors": [{"title": "豆瓣电影Top250", "rank": 1}]
}
```

Ratings are on Douban's scale of 10. A reviewer's `stars` are on a scale of 5. Dates are in China Standard Time (UTC+8).

## How much does it cost?

You pay per saved result: **$4.00 per 1,000 results**. There is no start fee and no monthly rental. Getting the full text of long reviews does not change the price.

| Run | Results | Cost |
|---|---|---|
| All available short reviews of one movie | 150 | $0.60 |
| The Top 250 movies | 250 | $1.00 |
| Details of 100 titles | 100 | $0.40 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

Douban shows only part of its content to visitors who are not logged in. The Actor collects everything a visitor can see:

- **Short reviews: up to 150 per title**, the ones Douban ranks as most useful.
- **Long reviews: up to 40 per title**, the ones Douban ranks as most useful.
- **Find titles: the best matches only**, usually 5 to 20 per keyword. It is meant for finding a title's URL, not for listing a whole category. For lists, use charts.
- **Music is not supported.**

Counts such as `shortReviewCount` show how many reviews exist in total.

---

Full documentation, all input options and a free trial: **[Douban Scraper on Apify](https://apify.com/pipiagent/douban-scraper)**
