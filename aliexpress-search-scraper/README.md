# AliExpress Search Scraper

Extract products from [AliExpress](https://www.aliexpress.com) search results, the way a shopper sees them. Type a keyword such as "phone case" and get every product's title, price, original price, discount, number sold, rating, images, shipping and delivery time. Use it for product research, dropshipping, price monitoring, competitor tracking and market research.

- **The numbers that matter for product research.** Price, discount, units sold and rating for every product in the search results.
- **Exact units sold.** Where AliExpress shows "5,000+ sold", the Actor usually also gives you the exact number behind it, for example 9,358.
- **Your currency and country.** Choose the currency and the ship-to country, and get the prices, shipping and delivery times a shopper there would see.
- **Same sort and price filters as the website.** Best match, most orders, price low to high, price high to low, plus a price range.
- **No login needed.** Press Start and get data.
- **Low price.** $1.50 per 1,000 results.

**Run it online, without code:** [AliExpress Search Scraper - Products, Prices, Orders & Ratings](https://apify.com/pipiagent/aliexpress-search-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `aliexpress-search-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

One result is one product from the search results.

| Field | Example | What it is |
|---|---|---|
| `title` | "AJAZZ AK820 75% Wired Mechanical Keyboard" | Product title as shown in the search results |
| `price` | 3.03 | Current price shown in the search results, as a number |
| `currency`, `priceText` | "USD", "US $3.03" | Currency code and the price exactly as displayed |
| `originalPrice`, `discountPercent` | 17.06, 82 | Price before the discount, when AliExpress shows one |
| `ordersCount` | 9358 | Units sold (exact number when available, otherwise read from the text) |
| `ordersText` | "5,000+ sold" | The sold text as displayed |
| `rating` | 4.9 | Star rating out of 5 |
| `imageUrl`, `imageUrls` | https://ae-pic-a1.aliexpress-media.com/... | Main image and the extra images shown in the card |
| `shippingText`, `freeShipping` | "Free shipping", true | Shipping labels shown in the card |
| `deliveryDaysMin`, `deliveryDaysMax` | 6, 11 | Delivery time estimate in days, when shown |
| `isChoice`, `isAd` | true, false | AliExpress Choice product, sponsored product |
| `tags` | ["Fastest delivery in 6 days"] | Other labels on the card, such as coupons and delivery promises |
| `productId`, `url` | "1005010706907312" | Product ID and link to the product page |
| `keyword`, `page`, `position` | "phone case", 1, 3 | Which search found it and where it ranked |

## Input examples

The 200 best-selling Bluetooth speakers, prices in US dollars for the United States:

```json
{
    "searchKeywords": ["bluetooth speaker"],
    "maxResultsPerKeyword": 200,
    "sort": "orders"
}
```

Mechanical keyboards between 20 and 60 euros for shoppers in Germany, most expensive first, without sponsored products:

```json
{
    "searchKeywords": ["mechanical keyboard"],
    "maxResultsPerKeyword": 100,
    "sort": "priceDesc",
    "minPrice": 20,
    "maxPrice": 60,
    "currency": "EUR",
    "shipTo": "DE",
    "includeAds": false
}
```

Several keywords in one run:

```json
{
    "searchKeywords": ["wireless earbuds", "yoga mat", "kitchen knife set"],
    "maxResultsPerKeyword": 500,
    "maxItems": 1500
}
```

## Output example

A product from a search for "phone case" (US dollars, shipping to the United States):

```json
{
    "productId": "1005013423916382",
    "url": "https://www.aliexpress.com/item/1005013423916382.html",
    "title": "Luxury Glass Camera Preservation For Magesafe Magnetic Wireless Charge Phone Case For iPhone 18 17 Pro Max/18 17 Pro Shockproof Back Cover",
    "price": 3.03,
    "currency": "USD",
    "priceText": "US $3.03",
    "originalPrice": 17.06,
    "originalPriceText": "US $17.06",
    "discountPercent": 82,
    "ordersCount": 7,
    "ordersText": "7 sold",
    "rating": 5,
    "imageUrl": "https://ae-pic-a1.aliexpress-media.com/kf/S8ed7967e9f7e4aa29809ddb7fd10e68cv.jpg",
    "imageUrls": [
        "https://ae-pic-a1.aliexpress-media.com/kf/S8ed7967e9f7e4aa29809ddb7fd10e68cv.jpg",
        "https://ae-pic-a1.aliexpress-media.com/kf/S00af28de6bd74f2a862c27b4e6915201w.jpg",
        "https://ae-pic-a1.aliexpress-media.com/kf/Sb558982f16684583b0b659ce5d186950O.jpg"
    ],
    "shippingText": "Free shipping",
    "freeShipping": true,
    "deliveryDaysMin": 4,
    "deliveryDaysMax": 10,
    "tags": ["New shoppers save $14.03", "Free shipping"],
    "isChoice": false,
    "isAd": false,
    "categoryId": "202229005",
    "shipTo": "US",
    "keyword": "phone case",
    "page": 1,
    "position": 13,
    "scrapedAt": "2026-10-24T11:26:26Z"
}
```

A product from the mechanical keyboard example above (euros, shipping to Germany, some fields left out):

```json
{
    "productId": "1005012036345764",
    "url": "https://www.aliexpress.com/item/1005012036345764.html",
    "title": "Rapid Trigger Hall Switches O3C SayoDevice OSU O3C Magnetic Pink Switches Keyboard With Knob Screen Copy Paste Shotcut",
    "price": 44.39,
    "currency": "EUR",
    "priceText": "€ 44,39",
    "originalPrice": null,
    "originalPriceText": null,
    "discountPercent": 6,
    "ordersCount": 66,
    "ordersText": "66 sold",
    "rating": 5,
    "imageUrl": "https://ae-pic-a1.aliexpress-media.com/kf/A2d966f35ffb14bd5a08faa3c7afa1a49D.jpg",
    "shippingText": "Free shipping",
    "freeShipping": true,
    "deliveryDaysMin": 2,
    "deliveryDaysMax": 9,
    "tags": ["30-day lowest price: 47,53€", "Free shipping"],
    "isChoice": false,
    "isAd": false,
    "shipTo": "DE",
    "keyword": "mechanical keyboard",
    "position": 42
}
```

## How much does it cost?

You pay per saved product: **$1.50 per 1,000 results**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| One keyword, first page | 60 | $0.09 |
| One keyword, 1,000 products | 1,000 | $1.50 |
| Three keywords, 2,000 products each | 6,000 | $9.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **About 2,700 products per keyword at most.** AliExpress shows 60 products per page and stops at page 60. The same product often appears on more than one page, and the Actor saves it only once, so a keyword gives about 2,700 different products in our tests. To get more, use several related keywords, different sort orders or several price ranges.
- **Large runs slow down.** AliExpress shows a captcha page to addresses that load many pages. The Actor then moves to a different Apify datacenter proxy address and slows down. You are not charged for refused pages, but they take time. In our tests 1,000 products took about 50 seconds, about 2,700 products took 2 to 3.5 minutes, and 6,000 products took 6 to 7 minutes, with 12% to 19% of page loads refused and retried. If AliExpress keeps refusing for a long time, the Actor stops that keyword, keeps what it already saved and moves on to the next keyword.
- **No store name in search results.** AliExpress does not include the seller's store in its search result cards, so the Actor does not return it.
- **Search results only.** The Actor does not open product pages, so there are no descriptions, variants, specifications or reviews.
- **Some fields are empty for some products.** New products have no rating or sold count. Delivery days and shipping labels appear only when AliExpress shows them in the card. In a test with 6,000 products, the sold count was filled for 87%, the rating for 68% and delivery days for 47%.
- **No original price in the EU.** For EU countries such as Germany, AliExpress does not show a crossed-out original price in search results, so `originalPrice` is empty there. The "30-day lowest price" label appears in `tags` instead.
- **Prices are what the search page shows.** For a few products AliExpress shows a "new shopper" deal price in the search results. The `price` field holds the price shown in the card, and the product page can show a different price per variant.
- **Unusual keywords.** When nothing matches, AliExpress shows a few similar products instead of an empty page, and the Actor saves those.

---

Full documentation, all input options and a free trial: **[AliExpress Search Scraper on Apify](https://apify.com/pipiagent/aliexpress-search-scraper)**
