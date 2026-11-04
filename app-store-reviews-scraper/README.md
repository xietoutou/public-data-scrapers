# App Store Reviews Scraper

Extract app reviews from the [Apple App Store](https://apps.apple.com), together with app details and app search results. Product teams use it to find out what iPhone and iPad users complain about, marketers use it to watch competitors, and researchers use it to collect review text for sentiment analysis.

- **Many countries in one run.** Apple shows only a limited number of reviews per country. Add a list of countries, or type `all`, and the Actor collects the reviews of every country and removes duplicates.
- **Up to 1,000 reviews per country.** The Actor can read the newest and the most helpful list of each country and merge them.
- **Every review says where it comes from.** The `country` field lets you compare markets.
- **No login and no proxy needed.** Press Start and get data.
- **Low price.** $0.25 per 1,000 results.

**Run it online, without code:** [App Store Reviews Scraper - iOS & Apple App Reviews by Country](https://apify.com/pipiagent/app-store-reviews-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `app-store-reviews-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Reviews | One review | Star rating, title, text, date, app version, helpful votes, user name, country |
| App details | One app in one country | Title, developer, rating, number of ratings, price, category, version, release notes, last update, size, languages, description, screenshots |
| Search | One app | The same fields as app details, plus the position in the search results |

**Step-by-step tutorial:** [How to Compare iOS App Store Reviews Across Countries After a Release (Python + pandas)](https://dev.to/frank0306_2838afa1791aac9/how-to-compare-ios-app-store-reviews-across-countries-after-a-release-python-pandas-411m)

## Input examples

The newest 500 reviews of an app in the United States:

```json
{
    "mode": "reviews",
    "appIds": ["324684580"],
    "countries": ["us"],
    "maxItems": 500
}
```

As many reviews as possible from five countries:

```json
{
    "mode": "reviews",
    "appIds": ["https://apps.apple.com/us/app/whatsapp-messenger/id310633997"],
    "countries": ["us", "gb", "de", "fr", "jp"],
    "sort": "both",
    "maxItems": 5000
}
```

The newest 100 reviews from every country:

```json
{
    "mode": "reviews",
    "appIds": ["310633997"],
    "countries": ["all"],
    "maxItemsPerCountry": 100,
    "maxItems": 20000
}
```

Details of two apps in three countries:

```json
{
    "mode": "appDetails",
    "appIds": ["324684580", "310633997"],
    "countries": ["us", "de", "jp"]
}
```

Find apps by keyword:

```json
{
    "mode": "search",
    "searchQueries": ["meditation"],
    "countries": ["us"],
    "maxItems": 200
}
```

## Output examples

A review:

```json
{
    "type": "review",
    "reviewId": "14602498196",
    "appId": "324684580",
    "appName": "Spotify: Music and Podcasts",
    "country": "us",
    "userName": "Kayla💅🤍",
    "userUrl": "https://itunes.apple.com/us/reviews/id1767727729",
    "rating": 4,
    "title": "Listen",
    "text": "Love Spotify but hate Spotify premium and the ads!!!!",
    "appVersion": "9.1.86",
    "voteCount": 0,
    "voteSum": 0,
    "postedAt": "2026-09-28T07:48:59Z",
    "sortedBy": "mostRecent",
    "url": "https://apps.apple.com/us/app/id324684580?see-all=reviews",
    "scrapedAt": "2026-09-29T11:43:22Z"
}
```

`voteCount` is the number of people who voted on the review. `voteSum` is the helpful votes minus the not helpful votes.

An app (description, languages and screenshots shortened here):

```json
{
    "type": "app",
    "appId": "324684580",
    "bundleId": "com.spotify.client",
    "url": "https://apps.apple.com/us/app/spotify-music-and-podcasts/id324684580",
    "country": "us",
    "title": "Spotify: Music and Podcasts",
    "description": "With the Spotify app, you can explore an extensive library of music and podcasts for free...",
    "developer": "Spotify",
    "developerId": "324684583",
    "developerUrl": "https://apps.apple.com/us/developer/spotify/id324684583",
    "developerWebsite": "https://www.spotify.com/",
    "seller": "Spotify",
    "genre": "Music",
    "genres": ["Music", "Entertainment"],
    "rating": 4.77263,
    "ratingsCount": 42331211,
    "ratingCurrentVersion": 4.77263,
    "ratingsCountCurrentVersion": 42331211,
    "price": 0.0,
    "currency": "USD",
    "formattedPrice": "Free",
    "isFree": true,
    "version": "9.1.86",
    "releaseNotes": "We’re always making changes and improvements to Spotify. To make sure you don’t miss a thing, just keep your Updates turned on.",
    "releasedAt": "2011-07-14T11:22:37Z",
    "updatedAt": "2026-09-23T17:49:27Z",
    "contentRating": "12+",
    "minimumOsVersion": "16.1",
    "fileSizeBytes": 311322624,
    "languages": ["AF", "AM"],
    "iconUrl": "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/fd/b0/e6/fdb0e66d-165c-aa66-ac6b-1ee1e01911e8/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-85-220.png/512x512bb.jpg",
    "screenshots": ["https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/f3/ce/05/f3ce0547-690a-b355-b1dd-6b6e91808279/IOS_-_5.5_-_S01_-_EN_-_CA_U005bEnglish__U0028Canada_U0029_U005d.png/392x696bb.png"],
    "ipadScreenshots": [],
    "scrapedAt": "2026-09-29T11:47:46Z"
}
```

## How much does it cost?

You pay per saved result: **$0.25 per 1,000 results**. There is no start fee and no monthly rental. A review, an app and a search result each count as one result.

| Run | Results | Cost |
|---|---|---|
| 100 newest reviews of one app | 100 | $0.03 |
| Newest and most helpful reviews of one app in 19 countries | 17,064 | $4.27 |
| 200 apps for one search keyword | 200 | $0.05 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **At most 500 reviews per app, country and sort order.** Apple publishes 10 pages of 50 reviews and nothing beyond that. With **Both** sort orders you get up to 1,000 reviews per country, because the newest and the most helpful list rarely overlap. In our test Spotify returned between 600 and 1,000 reviews per country. Older reviews cannot be reached.
- **To get more reviews, add more countries.** Reviews are stored per country. A run over all countries returned 15,255 reviews of WhatsApp at 100 per country. Small countries have few reviews or none.
- **Only reviews with text.** Most users give stars without writing anything. Those ratings are counted in `ratingsCount` of the app details, but they cannot be collected one by one.
- **No developer replies.** Apple's public review feed does not include the developer's answers.
- **No direct link to a single review.** The App Store has no page for one review, so `url` opens the review page of the app.
- **Apple sometimes returns an empty page.** About one request in seven comes back empty although reviews exist. The Actor asks again up to five times, which fixed every case in our tests. If a page stays empty, the log shows a warning and up to 50 reviews can be missing.
- **Search returns at most 200 apps per keyword and country.** This is the limit of Apple's search.
- **An app can be missing in a country.** Apps that are not sold in a country are skipped there with a warning in the log.
- **The app name comes from the first country in your list.** Apps often have translated names. All reviews of a run carry the same `appName`.
- **Speed.** About 3,800 reviews per minute. We tested runs up to 17,000 reviews and 400 requests on Apify without being slowed down by Apple. Larger runs were not tested.

---

Full documentation, all input options and a free trial: **[App Store Reviews Scraper on Apify](https://apify.com/pipiagent/app-store-reviews-scraper)**
