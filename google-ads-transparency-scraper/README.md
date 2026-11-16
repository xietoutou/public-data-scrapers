# Google Ads Transparency Scraper

Get the ads any company runs on Google from the public [Google Ads Transparency Center](https://adstransparency.google.com). Type a competitor's website or name and get its ads on Google Search, YouTube, Maps, Play and Shopping, with format, first and last shown dates, images and links. Use it for competitor research, ad creative inspiration, agency pitches, brand protection and market research.

- **Search the way you think.** Enter a domain (`nike.com`), a brand name (`Nike`), an advertiser ID or any URL copied from the Transparency Center.
- **Filter like the website.** Country, ad format (text, image, video), Google platform and date range.
- **Reach by country.** Optionally add the countries each ad ran in, estimated impressions per country and platform, and the advertiser's legal name.
- **Fast.** One request returns up to 100 ads. 100 ads usually take under 10 seconds.
- **Low price.** $1 per 1,000 results. Extra details cost nothing more.

**Run it online, without code:** [Google Ads Transparency Scraper - Competitor Ads by Domain](https://apify.com/pipiagent/google-ads-transparency-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `google-ads-transparency-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| **Ads** | One ad | Advertiser name and ID, ad ID, format, target domain, first and last shown, image URL, preview URL, link to the ad page |
| **Ads + reach by country** | One ad | Everything above plus countries, impressions per country and platform, first and last shown per country, legal name, number of variations |
| **Ads + text ad copy** | One ad | Headline, display URL and description of text ads that Google stores as text |
| **Advertisers** | One advertiser | Name, advertiser ID, country, number of ads, verified status |

## Input examples

The latest 200 ads of a domain:

```json
{
    "queries": ["nike.com"],
    "maxItems": 200
}
```

YouTube video ads a brand showed in Germany in October:

```json
{
    "queries": ["Adidas"],
    "region": "DE",
    "adFormat": "video",
    "platform": "youtube",
    "dateFrom": "2026-10-01",
    "dateTo": "2026-10-31"
}
```

Compare several competitors, 50 ads each, with reach by country:

```json
{
    "queries": ["apple.com", "samsung.com", "google.com"],
    "maxItemsPerQuery": 50,
    "includeDetails": true
}
```

Find the right advertiser account before scraping:

```json
{
    "mode": "advertisers",
    "queries": ["coca cola"]
}
```

## Output examples

An ad with reach by country and text ad copy:

```json
{
    "type": "ad",
    "advertiserName": "Nike Retail BV",
    "advertiserId": "AR18378488041124659201",
    "creativeId": "CR17623753280947486721",
    "format": "text",
    "targetDomain": "nike.com",
    "firstShown": "2025-10-24T11:00:38Z",
    "lastShown": "2026-11-14T20:11:53Z",
    "imageUrl": null,
    "previewUrl": "https://displayads-formats.googleusercontent.com/ads/preview/content.js?...",
    "adUrl": "https://adstransparency.google.com/advertiser/AR18378488041124659201/creative/CR17623753280947486721",
    "query": "nike.com",
    "regionFilter": null,
    "advertiserLegalName": "Nike Retail BV",
    "impressionsMin": 45000,
    "impressionsMax": 50000,
    "platforms": [
        { "platform": "Google Search", "impressionsMin": 45000, "impressionsMax": 50000 },
        { "platform": "Google Maps", "impressionsMin": 0, "impressionsMax": 1000 }
    ],
    "regionCount": 10,
    "regions": [
        {
            "region": "FR",
            "regionName": "France",
            "impressionsMin": 0,
            "impressionsMax": 1000,
            "firstShown": "2025-10-25",
            "lastShown": "2026-11-14",
            "platforms": [{ "platform": "Google Search", "impressionsMin": 0, "impressionsMax": 1000 }]
        }
    ],
    "variationCount": 2,
    "headline": "Nike Air Force 1 - Shop Nike Air Force 1 - Nike Essentials",
    "displayUrl": "www.nike.com/air_force_1",
    "description": "Discover Nike Air Force 1 Online At Nike.com. Shop The Official Nike Site. Your Path To Victory Starts Here...",
    "scrapedAt": "2026-11-14T20:34:04Z"
}
```

An advertiser:

```json
{
    "type": "advertiser",
    "advertiserName": "Coca-Cola AB",
    "advertiserId": "AR05354394792866349057",
    "country": "NO",
    "adCountMin": 2,
    "adCountMax": 2,
    "verified": false,
    "advertiserUrl": "https://adstransparency.google.com/advertiser/AR05354394792866349057",
    "query": "coca cola",
    "scrapedAt": "2026-11-14T20:34:44Z"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 results**. There is no start fee and no monthly rental. **Include reach by country** and **Include text ad copy** do not change the price.

| Run | Results | Cost |
|---|---|---|
| 100 ads of one domain | 100 | $0.10 |
| 50 ads each for 10 competitors | 500 | $0.50 |
| 5,000 ads | 5,000 | $5.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Most text ads come as a screenshot.** Google keeps many text ads only as an image. For those you get `imageUrl` and no headline. In our tests about 1 in 10 text ads had their copy available as text.
- **Some image and video ads have no direct image.** They are HTML5 or video ads. Use `previewUrl` or open `adUrl` to see them.
- **Impressions are ranges, not exact numbers,** and Google publishes them only for some countries, mostly in the EU. Other countries show 0 or no reach data.
- **Name search picks the closest advertiser.** Big brands often advertise under several accounts. Raise **Advertisers per name**, or run the Advertisers mode first and paste the right advertiser IDs. A domain search is not limited to one advertiser account.
- **Google does not say exactly how many ads match.** The log shows its estimate.

---

Full documentation, all input options and a free trial: **[Google Ads Transparency Scraper on Apify](https://apify.com/pipiagent/google-ads-transparency-scraper)**
