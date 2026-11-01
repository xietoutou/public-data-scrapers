# Shopify Products Scraper

Get every product of any [Shopify](https://www.shopify.com) store: title, vendor, product type, tags, prices and sale prices, variants with SKU and stock, options, images and description. Paste a store, a collection or a product link and download one clean table.

Use it for competitor price monitoring, stock and restock tracking, product research and dropshipping, catalog migration, market research across many brands, and feeding product data to AI tools.

- **Any Shopify store.** Custom domains (allbirds.com) and myshopify.com addresses, whole stores, single collections or single products.
- **Prices, discounts and stock.** Lowest and highest price, compare-at price, discount percent, in-stock flag and the number of variants in stock.
- **Product or variant rows.** One row per product with a variants list, or one row per size or color with its own price, SKU and stock, ready for price tracking in a spreadsheet.
- **Filters before you pay.** Keywords, excluded words, in stock only, on sale only, price range and new arrivals. You are charged only for products that match.
- **Fast.** 250 products per request, so a store with 10,000 products takes about a minute.
- **No login, no API key, no proxy.** The Actor reads the public product list that every Shopify store publishes.
- **Low price.** $0.50 per 1,000 results.

**Run it online, without code:** [Shopify Products Scraper - Prices, Variants, Stock & Images](https://apify.com/pipiagent/shopify-products-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `shopify-products-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Example | Notes |
|---|---|---|
| `storeName`, `storeUrl`, `currency` | Allbirds, https://www.allbirds.com, USD | From the store's public info |
| `productId`, `handle`, `title`, `url` | Women's Allbirds Flip Flop - Dusty Pink | |
| `vendor`, `productType`, `tags` | Allbirds, Shoes | As the store sets them |
| `priceMin`, `priceMax` | 50, 50 | Lowest and highest variant price, in the store's currency |
| `isOnSale`, `maxDiscountPercent` | true, 30 | A variant has a compare-at price above its price |
| `isAvailable`, `variantCount`, `availableVariantCount` | true, 7, 1 | In-stock flags as shown on the store |
| `options` | Size: 5, 6, 7... | Option names and values |
| `variants` | | Each variant's ID, title, SKU, price, compare-at price, stock flag, options, weight and image |
| `imageUrl`, `images` | | Main image and all image URLs |
| `publishedAt`, `createdAt`, `updatedAt` | 2026-09-25T23:58:13Z | ISO 8601 UTC |
| `description`, `descriptionHtml` | | Plain text by default, HTML optional |

In **Variant** mode every row has the product fields plus `variantId`, `variantTitle`, `sku`, `price`, `compareAtPrice`, `isAvailable`, `option1Name`/`option1` to `option3Name`/`option3`, `weightGrams` and `variantImage`.

## Input examples

All products of two stores:

```json
{
    "storeUrls": ["https://www.allbirds.com", "https://kyliecosmetics.com"]
}
```

One row per variant of a collection, in stock only, for price and stock tracking:

```json
{
    "storeUrls": ["https://www.allbirds.com/collections/mens"],
    "outputMode": "variants",
    "availableOnly": true
}
```

Products on sale between 20 and 100, published in the last 30 days:

```json
{
    "storeUrls": ["gymshark.com"],
    "onSaleOnly": true,
    "minPrice": "20",
    "maxPrice": "100",
    "publishedWithinDays": 30
}
```

## Output example

```json
{
    "storeName": "Allbirds",
    "storeUrl": "https://www.allbirds.com",
    "currency": "USD",
    "productId": 7340901859408,
    "handle": "womens-allbirds-flip-flop-dusty-pink",
    "title": "Women's Allbirds Flip Flop - Dusty Pink",
    "vendor": "Allbirds",
    "productType": "Shoes",
    "tags": ["allbirds::gender => womens", "allbirds::hue => pink", "allbirds::material => sugar"],
    "url": "https://www.allbirds.com/products/womens-allbirds-flip-flop-dusty-pink",
    "priceMin": 50,
    "priceMax": 50,
    "isOnSale": false,
    "maxDiscountPercent": null,
    "isAvailable": true,
    "variantCount": 7,
    "availableVariantCount": 1,
    "options": [{"name": "Size", "values": ["5", "6", "7", "8", "9", "10", "11"]}],
    "imageUrl": "https://cdn.shopify.com/s/files/1/1104/4168/files/A12513_26Q2_Allbirds-Flip-Flop-Dusty-Pink_PDP_LEFT.png?v=1774646345",
    "publishedAt": "2026-09-25T23:58:13Z",
    "createdAt": "2026-03-27T21:03:50Z",
    "updatedAt": "2026-11-01T17:27:30Z",
    "variants": [
        {
            "variantId": 42146889039952,
            "variantTitle": "5",
            "sku": "A12513W050",
            "price": 50,
            "compareAtPrice": null,
            "isAvailable": false,
            "option1Name": "Size",
            "option1": "5",
            "weightGrams": 455
        }
    ],
    "description": "Sun on your feet. Comfort underneath. Light, easy, and made for warm weather..."
}
```

## How much does it cost?

You pay per saved result: **$0.50 per 1,000 results**. A result is one product, or one variant in Variant mode. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| A store with 300 products | 300 | $0.15 |
| A store with 10,000 products | 10,000 | $5.00 |
| Daily price check of 1 collection (60 variants) for a month | 1,800 | $0.90 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Shopify stores only.** The Actor reads the public product list (`/products.json`) that Shopify stores publish. Sites on other platforms, password-protected stores and a few stores with custom storefronts that turn the list off are reported in the log and skipped.
- **Stock is a yes/no flag.** Shopify's public list says whether a variant can be bought, not how many units are left.
- **Prices are in the store's main currency**, without taxes, as the store sets them. International prices shown to visitors from other countries are not included.
- **Only published products.** Drafts and products hidden from the online store are not visible.
- **This is unofficial.** The Actor is not made by, endorsed by or connected to Shopify or the stores.

---

Full documentation, all input options and a free trial: **[Shopify Products Scraper on Apify](https://apify.com/pipiagent/shopify-products-scraper)**
