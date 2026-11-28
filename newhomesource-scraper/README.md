# NewHomeSource Scraper

Extract public new construction listings from [NewHomeSource](https://www.newhomesource.com), a large US directory of new home communities, builders, floor plans and quick move-in homes. Use it for builder and competitor research, land and market studies, pricing analysis, real estate lead lists and maps of new development.

- **A whole metro area in seconds.** One run returns every community the site lists for a metro area, for example 590 for Austin, 1,386 for Houston and 1,244 for Dallas in our tests.
- **Three kinds of data.** Communities, quick move-in homes and floor plans.
- **Ready for maps and spreadsheets.** Every result has latitude and longitude, numeric prices, beds, baths and square feet, and clean English field names.
- **No login needed.** Press Start and get data.
- **Low price.** $1.00 per 1,000 results.

This Actor is not made by, affiliated with or endorsed by NewHomeSource. It reads the same public pages any visitor can see.

**Run it online, without code:** [NewHomeSource Scraper - New Construction Homes & Builders](https://apify.com/pipiagent/newhomesource-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `newhomesource-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| What to scrape | One result is | Main fields |
|---|---|---|
| Communities | One new home community | Name, builder, city, state, ZIP, latitude, longitude, price from and to, previous price, beds, baths, garage and square feet ranges, number of plans, status (Active, Coming soon, Grand opening, Close out), image, link |
| Communities with detail pages | One community | Everything above plus street address, county, amenities, nearby schools with GreatSchools rating, school district, description, sales office hours, number of quick move-in homes and floor plans, all photos |
| Quick move-in homes | One home that is built or being built | Street address, plan name, set price, beds, baths, garage, square feet, home type, community, builder, location, link |
| Floor plans | One plan you can build | Plan name, starting price, beds, baths, garage, square feet, home type, community, builder, location, link |

With **Include detail pages** turned on, homes and plans also get stories, construction status (for example "Under Construction" or "Ready to build"), features, description, county and all photos.

## Input examples

Every community in the Austin, TX area (this is also what an empty input does):

```json
{
    "listingType": "communities",
    "locations": ["https://www.newhomesource.com/communities/tx/austin-area"],
    "maxItems": 1000
}
```

Communities with a home under $400,000 in two metro areas:

```json
{
    "listingType": "communities",
    "locations": ["tx/houston-area", "tx/dallas-area"],
    "maxPrice": 400000,
    "maxItems": 3000
}
```

Quick move-in homes with at least 3 bedrooms under $400,000:

```json
{
    "listingType": "homes",
    "locations": ["https://www.newhomesource.com/communities/tx/austin-area"],
    "minBeds": 3,
    "maxPrice": 400000,
    "maxItems": 50
}
```

Floor plans of one builder, with detail pages:

```json
{
    "listingType": "plans",
    "locations": ["tx/austin-area"],
    "builders": ["Perry"],
    "includeDetails": true,
    "maxItems": 10
}
```

## Output examples

A community:

```json
{
    "type": "community",
    "communityId": 218260,
    "communityName": "Saddle Ridge at Wildhorse Ranch",
    "builderName": "Milestone Community Builders",
    "builderId": 28451,
    "city": "Manor",
    "state": "TX",
    "zip": "78653",
    "location": "Manor, TX 78653",
    "streetAddress": null,
    "latitude": 30.330999,
    "longitude": -97.57198,
    "priceFrom": 339999,
    "priceTo": 457166,
    "priceText": "From $339,999",
    "previousPrice": 359999,
    "priceReduced": true,
    "isHotDeal": false,
    "bedsMin": 2,
    "bedsMax": 4,
    "bathsMin": 2,
    "bathsMax": 3,
    "garagesMin": 2,
    "garagesMax": 2,
    "sqftMin": 1700,
    "sqftMax": 2678,
    "numberOfPlans": 12,
    "status": "Active",
    "isMasterPlanned": false,
    "isAgeRestricted": false,
    "isBasicListing": false,
    "imageUrl": "https://nhs-dynamic-secure.akamaized.net/Images/Homes/MileS57978/110534818-260705.jpg",
    "marketName": "Austin, TX",
    "url": "https://www.newhomesource.com/community/tx/manor/saddle-ridge-at-wildhorse-ranch-by-milestone-community-builders/218260",
    "scrapedAt": "2026-11-27T00:42:51Z"
}
```

Extra fields of a community with detail pages (shortened):

```json
{
    "communityName": "Chisholm Trails 45s",
    "county": "Williamson",
    "amenities": ["Park", "Pool", "Trails"],
    "schoolDistricts": ["Georgetown Independent School District"],
    "schools": [
        {
            "name": "East View High School",
            "type": "Public High School",
            "grades": "9 to 12",
            "greatSchoolsRating": 5,
            "address": "4490 E University Ave, Georgetown, TX, 78626",
            "district": "Georgetown Independent School District"
        }
    ],
    "builderLogoUrl": "https://nhs-dynamic-secure.akamaized.net/images/brands/2534-MED.jpg",
    "images": ["https://nhs-dynamic-secure.akamaized.net/Images/Homes/TaylorMorrison/114436556-261018.jpg"]
}
```

A quick move-in home with detail pages (description and photos shortened):

```json
{
    "type": "home",
    "name": "509 Porter Country Pkwy (Decker)",
    "planName": "Decker",
    "streetAddress": "509 Porter Country Pkwy",
    "specId": 3292212,
    "planId": 2661684,
    "price": 279999,
    "priceText": "$279,999",
    "beds": 3,
    "baths": 2,
    "garages": 3,
    "sqft": 1537,
    "stories": 1,
    "homeType": "Single family home",
    "listingStatus": "Quick move-in",
    "constructionStatus": "Under Construction",
    "communityName": "Porter Country",
    "builderName": "Milestone Community Builders",
    "city": "Buda",
    "state": "TX",
    "zip": "78610",
    "latitude": 30.048056,
    "longitude": -97.804906,
    "county": "Hays",
    "features": ["1 Story", "Single Family"],
    "description": "The Decker at 509 Porter Country Pkwy is a move-in ready single-story home at Porter Country with 3 bedrooms, 2 baths, and 1,537 square feet. ...",
    "url": "https://www.newhomesource.com/specdetail/509-porter-country-pkwy-buda-tx-78610/3292212",
    "scrapedAt": "2026-11-27T00:44:55Z"
}
```

A floor plan:

```json
{
    "type": "plan",
    "name": "Carson",
    "planId": 3740212,
    "price": 359990,
    "priceText": "From $359,990",
    "beds": 3,
    "baths": 2.5,
    "garages": 2,
    "sqft": 1700,
    "stories": 2,
    "homeType": "Single family home",
    "listingStatus": "Floor plan",
    "constructionStatus": "Ready to build",
    "communityName": "Saddle Ridge at Wildhorse Ranch",
    "builderName": "Milestone Community Builders",
    "city": "Manor",
    "state": "TX",
    "url": "https://www.newhomesource.com/plan/carson-milestone-community-builders-manor-tx/3740212",
    "scrapedAt": "2026-11-27T00:32:30Z"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 results**. There is no start fee and no monthly rental. Turning on **Include detail pages** does not change the price.

| Run | Results | Cost |
|---|---|---|
| 100 Austin communities | 100 | $0.10 |
| All 590 Austin communities | 590 | $0.59 |
| All 1,386 Houston communities | 1,386 | $1.39 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Community lists are fast and complete. Everything else is limited.** One request returns the whole community list of a metro area. Detail pages, quick move-in homes and floor plans need one page request per community or per result. NewHomeSource runs a bot check that stops automated visitors after roughly 15 to 20 page requests. In our tests runs with detail pages were stopped after 5 to 16 pages. So these modes cover only the first several communities of a metro area per run. Each community page holds all of its homes and plans (for example 17 quick move-in homes and 17 floor plans for one Austin community), so homes and plans without detail pages go further than runs with detail pages.
- **When the bot check appears, the run stops and keeps what it saved.** The Actor never tries to solve or get around the check. The status message says how many pages were read.
- **Runs can occasionally fail at the start.** If the IP the run uses was already flagged by the site, the very first request is refused and the run fails with a clear message. Wait a while and run it again. In our tests a flagged IP stayed blocked for at least 10 minutes.
- **Filters are applied by the Actor, not by the site.** The site does not serve filtered pages to automated visitors, so the Actor reads the full list and filters it. Filter values on community ranges match when the range can meet them, for example a community priced from $339,999 to $457,166 passes a maximum price of $400,000.
- **Some fields need detail pages.** Street address, county, amenities and schools for communities, and stories and construction status for homes and plans, only appear with **Include detail pages** turned on.
- **Basic listings have fewer facts.** About a quarter of the Austin communities are basic listings with less information on the site, so some fields are empty.
- **Master plan communities list no homes themselves.** In homes and plans mode they are skipped; the builder communities inside them are listed and scanned separately.
- **The community list can be a little longer than the site's result count.** For Austin the list held 590 communities while the page said 573 results.
- **Builder phone numbers and email addresses are not collected.**

---

Full documentation, all input options and a free trial: **[NewHomeSource Scraper on Apify](https://apify.com/pipiagent/newhomesource-scraper)**
