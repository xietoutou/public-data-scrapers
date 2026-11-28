# kaufDA Brochures Scraper

Get the current weekly brochures (Prospekte) and offers (Angebote) that [kaufDA](https://www.kaufda.de) shows for any German city: retailer, brochure title, valid from and until, page count, cover image, and for single offers the product name, brand, price, original price, discount, unit price and image.

Use it for retail price monitoring, competitor promotion tracking, grocery price research, deal newsletters and apps, and market research on German supermarkets, discounters, DIY stores and furniture retailers.

- **Any German city.** Type "Berlin", "München" or "Frankfurt am Main". Brochures and offers are the ones kaufDA shows for that city.
- **Brochures and offers.** One brochure row per weekly Prospekt, one offer row per product, each offer linked to its brochure and page.
- **Filter by retailer or product.** Lidl, ALDI Nord, REWE, Kaufland, EDEKA and many more, or product keywords such as "Kaffee" or "Butter".
- **Prices as numbers.** Price, original price and discount percent are numbers, ready for spreadsheets. Product text stays in German.
- **No login and no proxy needed.** Press Start and get data.
- **Low price.** $1.00 per 1,000 results.

This Actor is not made by kaufDA or Bonial and is not affiliated with them. It reads the pages kaufDA shows to every visitor.

**Run it online, without code:** [kaufDA Brochures Scraper - German Prospekte & Weekly Offers](https://apify.com/pipiagent/kaufda-brochures-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `kaufda-brochures-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Record | One result is | Main fields |
|---|---|---|
| Brochure | One weekly brochure (Prospekt) | `retailer`, `title`, `validFrom`, `validUntil`, `publishedFrom`, `publishedUntil`, `pageCount`, `badges` (new, expiring soon), `brochureUrl`, `coverImageUrl`, `retailerLogoUrl`, `city` |
| Offer | One product offer from a brochure | `productName`, `brand`, `description`, `price`, `originalPrice`, `originalPriceIsRrp`, `discountPercent`, `unitPrice`, `conditions`, `categories`, `retailer`, `validFrom`, `validUntil`, `imageUrl`, `brochureId`, `brochurePage`, `offerUrl` |

Every result has a `type` field (`brochure` or `offer`), the `sourceUrl` of the kaufDA page it came from and `scrapedAt`. All times are ISO 8601 in UTC.

## Input examples

All current brochures in Berlin:

```json
{
    "mode": "brochures",
    "city": "Berlin",
    "maxItems": 500
}
```

Brochures and offers of two retailers in Munich:

```json
{
    "mode": "all",
    "city": "München",
    "retailers": ["Lidl", "ALDI Süd"]
}
```

Coffee and butter offers in Hamburg, only from REWE and EDEKA:

```json
{
    "mode": "offers",
    "city": "Hamburg",
    "searchTerms": ["Kaffee", "Butter"],
    "retailers": ["REWE", "EDEKA"]
}
```

## Output examples

A brochure:

```json
{
    "type": "brochure",
    "brochureId": "2501341622",
    "contentId": "8111b0f1-24b0-4804-be42-f1f6b61bdea8",
    "title": "LIDL LOHNT SICH",
    "retailer": "Lidl",
    "retailerId": "DE-1013",
    "validFrom": "2026-11-29T23:00:00Z",
    "validUntil": "2026-12-05T22:00:00Z",
    "publishedFrom": "2026-11-21T23:00:00Z",
    "publishedUntil": "2026-11-27T23:00:00Z",
    "pageCount": 78,
    "brochureType": "brochure",
    "badges": ["new"],
    "brochureUrl": "https://www.kaufda.de/contentViewer/static/8111b0f1-24b0-4804-be42-f1f6b61bdea8",
    "coverImageUrl": "https://content-media.bonial.biz/8111b0f1-24b0-4804-be42-f1f6b61bdea8/preview.jpg",
    "retailerLogoUrl": "https://publisher-media.bonial.biz/publisher-logos/c6c969cd-ef13-4e8e-bf1b-41953e4a48be.png?impolicy=448x314",
    "city": "München",
    "sourceUrl": "https://www.kaufda.de/Muenchen/Lidl/p-r74",
    "scrapedAt": "2026-11-27T00:28:23Z"
}
```

An offer:

```json
{
    "type": "offer",
    "offerId": "904430a5-e44a-4095-a4dc-ce3a90884a4d",
    "productName": "Multifunktionstisch-Set",
    "brand": "PARKSIDE",
    "description": "platzsparend zusammenklappbar mit Tragegriff, 4-stufig höhenverstellbar, Belastung pro Tisch: max. 35 kg. ca. 100 x 60 cm 3-teilig",
    "price": 39.99,
    "originalPrice": 49.99,
    "originalPriceIsRrp": false,
    "discountPercent": 20,
    "currency": "EUR",
    "unitPrice": null,
    "conditions": [],
    "priceNote": "Nur online",
    "categories": ["Funktionstisch", "Parkside"],
    "retailer": "Lidl",
    "retailerId": "DE-1013",
    "validFrom": "2026-11-29T23:00:00Z",
    "validUntil": "2026-12-05T22:00:00Z",
    "imageUrl": "https://content-media.bonial.biz/904430a5-e44a-4095-a4dc-ce3a90884a4d/99f13f8e-68b3-430c-9974-6cbbfcff6d48.jpg",
    "brochureId": "2501341622",
    "brochureContentId": "8111b0f1-24b0-4804-be42-f1f6b61bdea8",
    "brochurePage": 69,
    "offerUrl": "https://www.kaufda.de/contentViewer/static/8111b0f1-24b0-4804-be42-f1f6b61bdea8?page=69&productId=904430a5-e44a-4095-a4dc-ce3a90884a4d",
    "searchTerm": null,
    "city": "München",
    "sourceUrl": "https://www.kaufda.de/Muenchen/Lidl/p-r74",
    "scrapedAt": "2026-11-27T00:28:23Z"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 results**. Brochures and offers cost the same. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| Default run (50 Berlin brochures) | 50 | $0.05 |
| All brochures and offers in Berlin | about 840 | about $0.84 |
| 1,000 offers | 1,000 | $1.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Offers are a sample, not every product of a brochure.** kaufDA's public pages show up to 16 offers per retailer page and up to 16 offers per product keyword page. A whole-city run of Berlin returned 699 offers. Every product inside a 78-page brochure is only visible in kaufDA's brochure viewer, which this Actor does not read.
- **About 140 brochures per big city.** A whole-city run of Berlin checked 60 retailers and saved 140 brochures from 85 retailers in about 2 minutes. A deeper test that also checked 32 category pages and 200 retailer pages found only 149, so the default crawl covers almost everything kaufDA links for the city.
- **Only the cover image.** Each brochure has a cover image link and a link that opens it on kaufDA. Images of the inner pages are not included.
- **Product keywords are kaufDA's own keyword pages.** Free text search is not supported. German words such as "Kaffee", "Butter" or "Kinder Überraschung" work. A word kaufDA has no page for, such as "coffee", gives 0 results and a warning in the log.
- **Slow on purpose.** kaufDA asks crawlers to wait 2 seconds between pages, and the Actor does. Each retailer or keyword costs one page, so a run with 5 retailers takes about 15 seconds.
- **Times are in UTC.** A brochure valid from Monday 00:00 German time shows `validFrom` as Sunday 23:00 UTC (22:00 UTC in summer).
- **Same brochure in many cities.** National chains run one brochure in many cities. When you combine cities, remove duplicates by `brochureId` and `offerId`.
- **Only brochures that are online now.** You get the current brochures and the upcoming ones kaufDA already shows. Expired brochures are not available, so there is no history. Run it on a schedule to build your own.

---

Full documentation, all input options and a free trial: **[kaufDA Brochures Scraper on Apify](https://apify.com/pipiagent/kaufda-brochures-scraper)**
