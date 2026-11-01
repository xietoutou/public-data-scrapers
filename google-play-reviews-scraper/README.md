# Google Play Store Reviews Scraper

Extract app reviews from the [Google Play Store](https://play.google.com/store/apps), together with app details and app search results. Product teams use it to find out what users complain about, marketers use it to watch competitors, and researchers use it to collect review text for sentiment analysis.

- **Full review history.** Goes back through all reviews of an app, not only the first few pages. In our tests it read 150,000 reviews of one app in a single pass.
- **Developer replies included.** Each review comes with the developer's answer and its date, when there is one.
- **Filter and sort.** Newest, most relevant or highest rating first. Keep only 1-star reviews, or any other star rating.
- **Any language and country.** Collect reviews written in English, Spanish, Japanese or any other language Google Play supports.
- **No login and no proxy needed.** Press Start and get data.
- **Low price.** $0.20 per 1,000 results.

**Run it online, without code:** [Google Play Store Reviews Scraper - Android App Reviews](https://apify.com/pipiagent/google-play-reviews-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `google-play-reviews-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Reviews | One review | Star rating, text, date, helpful votes, app version, user name, developer reply and reply date |
| App details | One app | Title, developer, rating, number of ratings, rating breakdown by stars, installs, price, category, version, last update, description, screenshots, developer contact |
| Search | One app | Title, developer, rating, installs, price, category, description, position in the results |

**Step-by-step tutorial:** [How to Export Google Play Reviews of Any App to CSV or JSON (No API Key)](https://dev.to/frank0306_2838afa1791aac9/how-to-export-google-play-reviews-of-any-app-to-csv-or-json-no-api-key-15pe)

## Input examples

The newest 1,000 reviews of an app:

```json
{
    "mode": "reviews",
    "appIds": ["com.spotify.music"],
    "sort": "newest",
    "maxItems": 1000
}
```

Only 1-star reviews of two apps, written in German, 500 per app:

```json
{
    "mode": "reviews",
    "appIds": [
        "https://play.google.com/store/apps/details?id=com.spotify.music",
        "com.duolingo"
    ],
    "rating": "1",
    "language": "de",
    "country": "de",
    "maxItemsPerApp": 500,
    "maxItems": 1000
}
```

Details of several apps:

```json
{
    "mode": "appDetails",
    "appIds": ["com.mojang.minecraftpe", "com.whatsapp"]
}
```

Find apps by keyword:

```json
{
    "mode": "search",
    "searchQueries": ["meditation", "photo editor"]
}
```

## Output examples

A review:

```json
{
    "type": "review",
    "reviewId": "31aa0cbe-02d6-48c1-9644-8537effbf067",
    "appId": "com.ticktick.task",
    "appName": "TickTick:To Do List & Calendar",
    "userName": "Paul Revell",
    "userImage": "https://play-lh.googleusercontent.com/a-/ALV-UjX9BuxCzyw0BLRRZH3mqefzQNgrhcNILF1sJgEDl4s2-fsymGQCTA",
    "rating": 5,
    "text": "Overall a really great app. Just 2 reasons for taking 2 stars off. It's not a badly priced app but would be nice to have a monthly subscription option...",
    "thumbsUp": 7,
    "appVersion": "8.1.3.5",
    "postedAt": "2026-08-17T07:07:20Z",
    "developerReplyText": "Hi, you can click on Settings - Avatar - and then click on the gray folding icon at the bottom on the Premium Subscription interface to see the options for monthly premium subscription.",
    "developerReplyAt": "2026-08-17T01:38:27Z",
    "language": "en",
    "country": "us",
    "url": "https://play.google.com/store/apps/details?id=com.ticktick.task&reviewId=31aa0cbe-02d6-48c1-9644-8537effbf067",
    "scrapedAt": "2026-09-29T12:15:24Z"
}
```

An app (description and screenshots shortened here):

```json
{
    "type": "app",
    "appId": "com.mojang.minecraftpe",
    "url": "https://play.google.com/store/apps/details?id=com.mojang.minecraftpe&hl=en&gl=us",
    "title": "Minecraft: Dream it, Build it!",
    "summary": "Millions of crafters have smashed billions of blocks! Now you can join the fun!",
    "description": "Dive into an open world of building, crafting, and survival in the ultimate sandbox adventure...",
    "developer": "Mojang",
    "developerId": "4772240228547998649",
    "developerUrl": "https://play.google.com/store/apps/dev?id=4772240228547998649",
    "developerEmail": "help@minecraft.net",
    "developerWebsite": "http://help.mojang.com",
    "developerAddress": null,
    "privacyPolicyUrl": "http://go.microsoft.com/fwlink/?LinkId=521839",
    "genre": "Arcade",
    "genreId": "GAME_ARCADE",
    "rating": 4.306842,
    "ratingsCount": 5846369,
    "reviewsCount": 635022,
    "ratings1Star": 620437,
    "ratings2Star": 178542,
    "ratings3Star": 269253,
    "ratings4Star": 496540,
    "ratings5Star": 4281580,
    "installs": "50,000,000+",
    "minInstalls": 50000000,
    "installsEstimate": 97881894,
    "price": 6.99,
    "currency": "USD",
    "isFree": false,
    "inAppPurchases": "$0.99 - $49.99 per item",
    "containsAds": false,
    "contentRating": "Everyone 10+",
    "releasedAt": "2011-08-16T06:17:21Z",
    "updatedAt": "2026-09-25T17:26:28Z",
    "version": "1.26.52.3",
    "androidVersion": "8.0",
    "recentChanges": "What's new in 26.52: Various bug fixes!",
    "iconUrl": "https://play-lh.googleusercontent.com/tI4StRSPVhpGJH5R013naszLUawOjao1ya8FvyaNO7XY_cJFHFqo1EFaEJv_7zz3rRJ5lEpLiw14ZqQLCOYc",
    "headerImageUrl": "https://play-lh.googleusercontent.com/S_Z7YSNVWWd3BNh3AwV0iVv0hNqJ8zvn-HwLTlYqVLU4uxSohpwKpIa-EmwwwoxOlSw8voqu5CsxQGbojanT",
    "videoUrl": "https://play.google.com/video/lava/web/player/yt:movie:BLtLrFNRE-E?autoplay=1&embed=play",
    "screenshots": ["https://play-lh.googleusercontent.com/ywPBuExmYGLE6oL7QENmI7wOxMPOU-XatzosE6M4bgXudBsMQWcKp1QHhHrJM1QeTadoVo7lnpO5O12WyzlYQA"],
    "language": "en",
    "country": "us",
    "scrapedAt": "2026-09-29T11:25:16Z"
}
```

## How much does it cost?

You pay per saved result: **$0.20 per 1,000 results**. There is no start fee and no monthly rental. A review, an app and a search result each count as one result.

| Run | Results | Cost |
|---|---|---|
| 100 newest reviews of one app | 100 | $0.02 |
| 3,000 reviews each for 5 apps | 15,000 | $3.00 |
| Details of 200 apps | 200 | $0.04 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Reviews come in one language per run.** Google Play returns only the reviews written in the language you choose. To collect reviews in several languages, start one run per language.
- **Only reviews with text.** The number of ratings of an app is much larger than the number of reviews, because most users give stars without writing anything. Ratings without text cannot be collected. The app details show both numbers (`ratingsCount` and `reviewsCount`).
- **Search returns at most 30 apps per keyword.** This is what Google Play shows on its search page. Some keywords return fewer. Use several related keywords to find more apps.
- **Search results have fewer fields.** They do not include the number of ratings, the rating breakdown, the version or the update date. Turn on **Add full app details to search results** to add them.
- **Version is empty for some apps.** Apps such as Spotify show "Varies with device" on Google Play, so `version` and `androidVersion` are empty for them. About 1 in 5 reviews has no `appVersion` either.
- **The date of a review is the date of its last edit.** When a user edits a review after the developer answered, the reply can be older than the review.
- **Speed.** About 8,500 reviews per minute. We tested runs up to 20,000 reviews on Apify and 150,000 reviews in one pass from our own machine without being slowed down by Google. Larger runs were not tested.
- **The exact install count is an estimate.** `installs` and `minInstalls` are the public numbers. `installsEstimate` is a more precise figure that Google includes in the page data.

---

Full documentation, all input options and a free trial: **[Google Play Store Reviews Scraper on Apify](https://apify.com/pipiagent/google-play-reviews-scraper)**
