# Alibaba Search Scraper

Extract product listings from [Alibaba.com](https://www.alibaba.com), the largest B2B wholesale marketplace, where factories and trading companies sell in bulk. Type a keyword and get every product with its wholesale price, quantity price breaks, minimum order and full supplier profile. Use it for product sourcing, supplier shortlists, price research, competitor monitoring and market analysis.

- **Search results and product pages.** Search by keyword, or get the full product page (attributes, variants, lead times, packaging) for product links you already have.
- **Supplier data on every product.** Company name, country, years on Alibaba, Verified and Trade Assurance badges, rating, response rate and orders in the last 6 months.
- **Same filters as the website.** Verified suppliers, Verified Pro, supplier country, price range and maximum minimum order.
- **No login and no proxy needed.** Press Start and get data. 3,000 products take about one minute.
- **Low price.** $1.50 per 1,000 results.

**Run it online, without code:** [Alibaba Search Scraper - Wholesale Products, Prices & Suppliers](https://apify.com/pipiagent/alibaba-search-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `alibaba-search-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Search results | One product | Title, price range, quantity price breaks, minimum order, category, images, certifications, supplier name, country, years, Verified, Trade Assurance, rating, review count, response rate, orders in 6 months, rank in the search |
| Product details | One product | Price breaks in USD, minimum order, price terms, units sold, full category path, product attributes, variants (colors, models, sizes), lead time per quantity, package size and weight, images, video, supplier business type, on-time delivery rate, response time, rating |

This is the international wholesale site www.alibaba.com. It does not cover 1688.com or AliExpress.

**Step-by-step tutorial:** [How to Compare Alibaba Wholesale Prices and MOQs Across Hundreds of Suppliers in a Spreadsheet](https://dev.to/frank0306_2838afa1791aac9/how-to-compare-alibaba-wholesale-prices-and-moqs-across-hundreds-of-suppliers-in-a-spreadsheet-2pf8)

## Input examples

Get 500 yoga mats from each of two keywords:

```json
{
    "searchKeywords": ["yoga mat", "pilates mat"],
    "maxResultsPerKeyword": 500
}
```

Only Verified suppliers in China, unit price between $1 and $5, and a minimum order of 10 units or less:

```json
{
    "searchKeywords": ["yoga mat"],
    "maxResultsPerKeyword": 200,
    "verifiedSupplierOnly": true,
    "supplierCountry": "CN",
    "minPrice": 1,
    "maxPrice": 5,
    "maxMinOrder": 10
}
```

Full product pages for links you already have:

```json
{
    "mode": "productDetails",
    "productUrls": [
        "https://www.alibaba.com/product-detail/Premium-Crystal-Clear-TPU-PC-Case_1601918386232.html",
        "1601859320012"
    ]
}
```

## Output examples

A search result:

```json
{
    "type": "searchResult",
    "productId": "1601918386232",
    "title": "Premium Crystal Clear TPU PC Case for iPhone 17 18 Pro Max Strong Magnetic Charging Shockproof Transparent Phone Cover",
    "url": "https://www.alibaba.com/product-detail/Premium-Crystal-Clear-TPU-PC-Case_1601918386232.html",
    "priceText": "US $0.51-$0.68",
    "priceMin": 0.51,
    "priceMax": 0.68,
    "currency": "USD",
    "minOrderQuantity": 200,
    "minOrderUnit": "pieces",
    "minOrderText": "200 pieces",
    "category": "Mobile Phone Cases",
    "categoryId": "380230",
    "imageUrl": "https://s.alicdn.com/@sc04/kf/He0c23016d3854f688506c3d7090724e8a.png",
    "hasVideo": true,
    "readyToShip": false,
    "productCertifications": ["CE", "ROHS"],
    "supplierName": "Guangzhou Ruite Electronic Technology Co., Ltd.",
    "supplierId": "243508786",
    "supplierUrl": "https://ruitetec.en.alibaba.com/",
    "supplierProfileUrl": "https://ruitetec.en.alibaba.com/company_profile.html",
    "supplierCountry": "China",
    "supplierCountryCode": "CN",
    "supplierYearsOnAlibaba": 9,
    "verifiedSupplier": true,
    "verifiedSupplierPro": false,
    "goldSupplier": true,
    "tradeAssurance": true,
    "supplierVerifiedBy": "SGS",
    "supplierRating": 4.7,
    "supplierReviewCount": 88,
    "supplierProductQualityScore": 4.6,
    "supplierServiceScore": 4.8,
    "supplierShippingScore": 4.7,
    "supplierResponseRate": "98.5%",
    "supplierOrders6Months": 260,
    "supplierOrderValue6MonthsUsd": "180,000+",
    "supplierEmployees": 10,
    "supplierFactorySizeM2": 370,
    "supplierMainProducts": "Screen Protector, Phone Case, Headphone Accessories, Mobile Phone Lens Protective Film, Chargers And Adapters",
    "supplierMainMarkets": "United States",
    "keyword": "phone case",
    "page": 1,
    "position": 1,
    "scrapedAt": "2026-10-24T11:18:24Z",
    "priceTiers": [
        {"minQuantity": 200, "maxQuantity": 2999, "price": 0.68, "promotionPrice": null, "unit": "pieces"},
        {"minQuantity": 3000, "maxQuantity": 29999, "price": 0.65, "promotionPrice": null, "unit": "pieces"},
        {"minQuantity": 30000, "maxQuantity": null, "price": 0.51, "promotionPrice": null, "unit": "pieces"}
    ]
}
```

A product page (shortened):

```json
{
    "type": "productDetail",
    "productId": "1601918386232",
    "title": "Premium Crystal Clear TPU PC Case for iPhone 17 18 Pro Max Strong Magnetic Charging Shockproof Transparent Phone Cover",
    "priceMin": 0.51,
    "priceMax": 0.68,
    "currency": "USD",
    "minOrderQuantity": 200,
    "minOrderUnit": "pieces",
    "priceTerms": "FOB",
    "soldText": "800 sold",
    "category": "Consumer Electronics > Phone Case & Accessories > Mobile Phone Cases",
    "attributes": {
        "compatible brand": "For Iphone, For Samsung",
        "material": "TPU+PC",
        "brand name": "Ruite",
        "place of origin": "Guangdong, China"
    },
    "variants": [
        {"name": "color", "values": ["Transparent"]},
        {"name": "compatible model", "values": ["For iPhone17", "For iPhone17 Pro", "For iPhone17 Pro Max", "For iPhone17 Air"]}
    ],
    "leadTimes": [
        {"minQuantity": 1, "maxQuantity": 100, "days": 8},
        {"minQuantity": 101, "maxQuantity": 1000, "days": 12},
        {"minQuantity": 1001, "maxQuantity": 5000, "days": 16}
    ],
    "packageSizeCm": "25X15X1",
    "packageWeightKg": 0.08,
    "shipsFrom": ["China"],
    "supplierName": "Guangzhou Ruite Electronic Technology Co., Ltd.",
    "supplierBusinessType": "Trading Company",
    "supplierYearsOnAlibaba": 9,
    "supplierEmployeesRange": "11-50",
    "supplierRating": 4.7,
    "supplierResponseTime": "≤2h",
    "supplierOnTimeDeliveryRate": "97.0%",
    "supplierOrders6Months": 269,
    "supplierOrderValue6MonthsUsd": "220,000+"
}
```

## How much does it cost?

You pay per saved result: **$1.50 per 1,000 results**. There is no start fee and no monthly rental. Search results and product pages cost the same.

| Run | Results | Cost |
|---|---|---|
| 50 products for one keyword | 50 | $0.08 |
| 1,000 products for one keyword | 1,000 | $1.50 |
| 3,000 products across 3 keywords | 3,000 | $4.50 |
| 100 full product pages | 100 | $0.15 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Alibaba shows at most 100 pages per search.** The Actor reads up to 100 products per page, so one keyword can give several thousand products. We tested 3,000 products for one keyword on Apify's servers (about one minute). To go wider, add related keywords or split by supplier country or price range.
- **Deeper pages repeat some products.** From about page 12 on, 1% to 25% of each page are products already shown. The Actor removes these duplicates within a keyword, so a deep run makes a few more requests than the result count suggests. Duplicates are not removed across different keywords.
- **Rare or misspelled keywords still return products.** Alibaba always shows something, so a keyword with no real matches gives loosely related products instead of an empty result. Check the titles.
- **Some search results are already offline.** Alibaba's search index sometimes lists products that were just removed. In product details mode these are skipped with a warning and not charged (1 of 30 in our test).
- **Not every field is on every product.** For example, the response time, units sold and delivery estimate appear on only a part of the listings. Missing values are `null`.
- **Prices are in US dollars.** Price filters take whole dollar amounts. Some product pages show "contact supplier" instead of a price; for those the price fields are empty (3 of 29 in our test).
- **No sorting and no sponsored flag.** You get Alibaba's default "best match" order. The `position` field keeps that order.
- **Product details make one request per product,** so they run at about 40 products per minute. The long description written by the supplier (images and HTML) is not included.
- **Blocking.** In our tests on Apify's servers no request was refused. If Alibaba starts refusing requests, the Actor retries as a new visitor and, on the Apify platform, switches to Apify's datacenter proxy automatically.

---

Full documentation, all input options and a free trial: **[Alibaba Search Scraper on Apify](https://apify.com/pipiagent/alibaba-search-scraper)**
