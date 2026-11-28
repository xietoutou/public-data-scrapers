# Yahoo! Auctions Japan Scraper

Extract public listings from [Yahoo! Auctions Japan](https://auctions.yahoo.co.jp) (ヤフオク!), one of Japan's largest marketplaces for used and collectible goods. Search live listings by keyword or category, pull closed auctions with their final prices for price research, and get full item pages with description and specs. Resellers, import buyers, collectors and market researchers use it to track prices of cameras, trading cards, watches, car parts, figures and more.

- **Four kinds of data in one Actor.** Keyword search, category browsing, sold (closed) auctions with final prices, and full item details.
- **Sold prices for price research.** Closed auctions come with the final price, bid count and end time, plus Yahoo's own average, lowest and highest final price for your search.
- **English field names.** Output is clean JSON with names like `currentPrice`, `bids` and `endTime`, ready for spreadsheets and code. Titles, descriptions and category names stay in Japanese, as on the site.
- **No login and no proxy needed.** Press Start and get data.
- **Low price.** $1.20 per 1,000 results.

**Run it online, without code:** [Yahoo! Auctions Japan Scraper - Listings & Sold Prices](https://apify.com/pipiagent/yahoo-auctions-japan-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `yahoo-auctions-japan-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Search | One live listing | Title, current price, buy-it-now price, bids, watchers, end time, time left, condition, shipping fee, free shipping, prefecture, seller rating, category, image |
| Category | One live listing | The same fields, for every listing in a category |
| Sold | One closed auction | Final price, bids, end time, condition, prefecture, seller rating, category, image |
| Item details | One item page | Everything above plus description, specs, brand, all image URLs, seller name and rating counts, shipping methods, package size, return policy, tax |

Turn on **Include item details** in Search, Category or Sold mode to add the item page fields to every listing.

All prices are in Japanese yen (JPY) and include tax, as Yahoo shows them. All times are in UTC (ISO 8601).

## Input examples

Search buy-it-now listings between 3,000 and 20,000 yen in new condition:

```json
{
    "mode": "search",
    "searchTerms": ["ポケモンカード"],
    "minPrice": 3000,
    "maxPrice": 20000,
    "listingType": "buyNow",
    "conditions": ["NEW"],
    "maxItems": 200
}
```

Get the highest recent sale prices for a camera model:

```json
{
    "mode": "sold",
    "searchTerms": ["ニコン F3"],
    "soldSort": "priceHighest",
    "maxItems": 500
}
```

Browse a category (digital SLR cameras):

```json
{
    "mode": "category",
    "categories": ["https://auctions.yahoo.co.jp/category/list/2084261634/"],
    "maxItems": 1000
}
```

Get full item pages for chosen auctions:

```json
{
    "mode": "details",
    "auctionIds": ["d1253573795", "https://auctions.yahoo.co.jp/jp/auction/m1253454164"]
}
```

## Output examples

A live listing from a search:

```json
{
    "type": "listing",
    "auctionId": "d1253573795",
    "title": "NIKON ニコン F3 / MD-4 モータードライブ フィルムカメラ 2143",
    "url": "https://auctions.yahoo.co.jp/jp/auction/d1253573795",
    "status": "open",
    "currentPrice": 10150,
    "finalPrice": null,
    "buyNowPrice": null,
    "currency": "JPY",
    "bids": 24,
    "watchCount": 44,
    "isBuyNowOnly": false,
    "startTime": "2026-11-24T07:15:30Z",
    "endTime": "2026-11-27T12:14:38Z",
    "timeLeftSeconds": 13955,
    "condition": "USED40",
    "conditionName": "やや傷や汚れあり",
    "freeShipping": false,
    "shippingFee": 1000,
    "shippingFeeType": "flat",
    "shippingFeeTiming": "shownOnListing",
    "prefectureCode": 15,
    "location": "新潟県",
    "sellerId": "2hQbBKd8bgT2aQQ18zwBim24bQMdn",
    "sellerGoodRatingPercent": 99.5,
    "sellerIsStore": false,
    "sellerType": "individual",
    "isFleaMarketItem": false,
    "isFeatured": false,
    "categoryId": "2084044778",
    "categoryName": "ニコン",
    "categoryPath": "家電、AV、カメラ > カメラ、光学機器 > フィルムカメラ > 一眼レフ > マニュアルフォーカス > ニコン",
    "imageUrl": "https://auctions.c.yimg.jp/images.auctions.yahoo.co.jp/image/dr000/auc0211/user/8b8c5b61d4802e25ef59697fdef32d9d82e26359c90b7f0555cc6e16f5dae4f0/i-img1200x900-17955044842157bzmwma467.jpg",
    "searchKeyword": "ニコン F3",
    "page": 1,
    "position": 1,
    "scrapedAt": "2026-11-27T08:22:02Z"
}
```

A sold auction with **Include item details** turned on (description shortened here):

```json
{
    "type": "sold",
    "auctionId": "v1253925696",
    "title": "タムロン TAMRON AF 18-250mm F3.5-6.3 [IF] MACRO A18 ASPHERICAL LD Di II ニコンFマウント",
    "url": "https://auctions.yahoo.co.jp/jp/auction/v1253925696",
    "status": "closed",
    "finalPrice": 3000,
    "buyNowPrice": 3000,
    "currency": "JPY",
    "bids": 1,
    "isBuyNowOnly": true,
    "endTime": "2026-11-27T08:03:08Z",
    "condition": "USED40",
    "conditionName": "やや傷や汚れあり",
    "location": "東京都",
    "sellerId": "6RnyLzPUu43j1rwaW5Y882Qkixf7p",
    "sellerGoodRatingPercent": 100,
    "sellerType": "individual",
    "categoryPath": "家電、AV、カメラ > カメラ、光学機器 > レンズ > 一眼カメラ用（オートフォーカス） > ニコン",
    "startPrice": 3000,
    "biddersCount": 1,
    "returnsAccepted": false,
    "sellerDisplayName": "xmx",
    "sellerRatingScore": 968,
    "sellerGoodRatings": 968,
    "sellerBadRatings": 0,
    "shippingPaidBy": "buyer",
    "shippingMethods": ["おてがる配送ゆうパック"],
    "shippingSchedule": "支払い手続きから1～2日で発送",
    "packageSize": "TO_60CM",
    "packageWeight": "TO_2KG",
    "brand": "ニコン",
    "description": "先日とても良いレンズを購入できて喜んでおりましたが....\n写真は綺麗に撮れましたが、...",
    "imageUrls": [
        "https://auctions.c.yimg.jp/images.auctions.yahoo.co.jp/image/dr000/auc0211/user/fe412df682e97a6c0946ac1964fafdb43d3397becca0e619866e0eac3278f4be/i-img819x1200-17957479813508pfr3fi90059.jpg"
    ],
    "scrapedAt": "2026-11-27T08:29:34Z"
}
```

Item specs, when the seller filled them in (here a trading card listing):

```json
"specs": {"tradingCardType": "ボックス", "tradingCardBoxQuantity": "2個", "tradingCardShrink": "あり"}
```

In Sold mode the run also saves Yahoo's price summary for each search in the key-value store under `SOLD_PRICE_STATS`:

```json
[{"keyword": "ニコン F3", "totalResults": 14858, "averagePrice": 18205, "minPrice": 1, "maxPrice": 600000, "currency": "JPY"}]
```

### Condition codes

| `condition` | Shown on Yahoo |
|---|---|
| NEW | 未使用 |
| USED10 | 未使用に近い |
| USED20 | 目立った傷や汚れなし |
| USED40 | やや傷や汚れあり |
| USED60 | 傷や汚れあり |
| USED80 | 全体的に状態が悪い |
| USED | 中古 (no grade given) |
| OTHER | Not graded, for example vehicles |

## How much does it cost?

You pay per saved result: **$1.20 per 1,000 results**. There is no start fee and no monthly rental. Turning on **Include item details** does not change the price, it only makes the run slower.

| Run | Results | Cost |
|---|---|---|
| 100 search results | 100 | $0.12 |
| 1,000 sold auctions | 1,000 | $1.20 |
| 10,000 category listings | 10,000 | $12.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Search results cannot be re-sorted.** Yahoo's robots.txt does not allow the sort parameters on search and category pages, so live listings come in Yahoo's default order (recommended for search, featured for categories). Sold mode can be sorted by end time or final price.
- **Some filters are applied by the Actor, not by Yahoo.** Condition, free shipping, seller type and minimum bids are not allowed as URL parameters under robots.txt, so the Actor loads the normal result pages and drops listings that do not match. The same goes for price and listing type in Category and Sold mode. With strict filters a run reads more pages per saved result and stops after **Max pages per query** (default 100 pages, 5,000 listings).
- **Sold history covers about the last six months.** On 2026-11-27 the oldest closed auction in the results ended on 2026-05-31. Every sold result we checked had at least one bid, so they are completed sales.
- **Sold results have no shipping fee amount.** Yahoo's closed search does not show it. Turn on item details to get the shipping methods and who pays.
- **PayPay Flea Market listings have no details.** Yahoo mixes listings from its sister site PayPay Flea Market (IDs starting with `z`) into search results; in our sold test they were about a quarter of the results. They are saved with `isFleaMarketItem: true` and a paypayfleamarket.yahoo.co.jp link, but the item details step skips them because their pages live on a different site.
- **Seller names are masked in search results.** Yahoo shows `********` there, so listings carry the seller's internal ID and good-rating percentage. Item details add the display name the item page shows, which is often partly masked too.
- **Shipping fees that depend on the destination** (`shippingFeeType: byPrefecture`) are the amount Yahoo shows on the search page. The real fee depends on where the item is shipped.
- **No exact match means no results.** When a keyword has no exact matches, Yahoo fills the page with loosely similar items. The Actor skips those and logs a warning unless you turn on **Keep similar-item results**.
- **Keyword matching is Yahoo's.** For example "ニコン F3" also finds lenses with "F3.5" in the title. Use more specific keywords or a category to narrow it down.
- **Item pages for old auctions disappear.** Item details mode skips IDs that Yahoo no longer serves and logs a warning.
- **Speed.** In our tests 1,000 search or sold results took about 20 seconds of scraping, and item details add about 0.8 seconds per result.

---

Full documentation, all input options and a free trial: **[Yahoo! Auctions Japan Scraper on Apify](https://apify.com/pipiagent/yahoo-auctions-japan-scraper)**
