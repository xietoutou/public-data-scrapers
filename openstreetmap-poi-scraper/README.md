# OpenStreetMap POI Scraper

Extract places and businesses from [OpenStreetMap](https://www.openstreetmap.org): restaurants, cafes, shops, hotels, doctors, dentists, offices, tradespeople and 30+ other categories, for any city, district, country, bounding box or radius. Use it to build local lead lists, map competitors, research a market or feed location data into your own tools.

- **Search by place name.** Type "Kreuzberg, Berlin", "Austin, Texas" or "Portugal" and the Actor searches inside the official boundary of that place. A bounding box or a point with a radius also works.
- **Lead filters.** Keep only places with a phone, a website or an email, or only places **without** a website (for web agencies looking for clients).
- **Big areas work.** When an area is too large for one query, the Actor splits it into smaller tiles automatically, so a whole city does not time out.
- **Reliable on busy servers.** The public Overpass servers are often overloaded. The Actor sends one request at a time, backs off politely when a server is busy and switches to another server instead of failing the run.
- **Low price.** $1.00 per 1,000 places, no start fee.

**Run it online, without code:** [OpenStreetMap POI Scraper - Places, Businesses & Leads](https://apify.com/pipiagent/openstreetmap-poi-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `openstreetmap-poi-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

One result is one place. Each place has these fields:

| Group | Fields |
|---|---|
| Identity | `name`, `category`, `primaryTagKey`, `primaryTagValue`, `brand`, `operator`, `cuisine` |
| Address | `street`, `houseNumber`, `postcode`, `city`, `state`, `country`, `fullAddress` |
| Location | `latitude`, `longitude` (every place has them, also buildings and areas) |
| Contact | `phone`, `website`, `email`, `facebook`, `instagram` |
| Details | `openingHours`, `wheelchair`, `wikidata` |
| Links and raw data | `osmId`, `osmType`, `osmUrl`, `tags` (every OpenStreetMap tag of the place), `searchLocation`, `scrapedAt` |

Phone numbers and websites are also read from the `contact:phone`, `contact:website`, `mobile` and `url` variants that many mappers use, so you do not miss them.

**Categories you can pick:** restaurant, fast food, cafe, bar or pub, nightclub, bakery, hotel or lodging, supermarket or grocery, clothing store, shop (any kind), pharmacy, dentist, doctor or clinic, hospital, veterinarian, school or kindergarten, university or college, gym, hairdresser or beauty salon, car repair, car dealer, bank, ATM, fuel station, EV charging station, parking, office (any kind), lawyer, real estate agent, craft and trades, tourist attraction, museum or gallery, place of worship, post office, police and park. Anything else can be searched with a custom OpenStreetMap tag such as `shop=bicycle`.

## Input examples

Cafes in one district (the default input):

```json
{
    "locations": ["Kreuzberg, Berlin"],
    "categories": ["cafe"],
    "maxItems": 100
}
```

Restaurants and bars in central Paris with a phone number but no website, for a web agency lead list:

```json
{
    "boundingBox": "48.85,2.33,48.87,2.36",
    "categories": ["restaurant", "bar"],
    "requirePhone": true,
    "withoutWebsite": true,
    "maxItems": 300
}
```

Restaurants and hotels within 1.5 km of a point:

```json
{
    "coordinates": "40.7580, -73.9855",
    "radiusMeters": 1500,
    "categories": ["restaurant", "hotel"],
    "maxItems": 500
}
```

Custom OpenStreetMap tags. Each line is one search, a comma means "and":

```json
{
    "locations": ["Austin, Texas"],
    "customTagFilters": ["amenity=restaurant, cuisine=sushi", "shop=bicycle"]
}
```

All dental practices in a big city whose name contains "dental":

```json
{
    "locations": ["Bangkok"],
    "categories": ["dentist"],
    "nameContains": "dental"
}
```

## Output example

```json
{
    "osmId": 278295436,
    "osmType": "node",
    "osmUrl": "https://www.openstreetmap.org/node/278295436",
    "name": "Barcomi's Café & Kaffeerösterei",
    "category": "Cafe",
    "primaryTagKey": "amenity",
    "primaryTagValue": "cafe",
    "street": "Bergmannstraße",
    "houseNumber": "21",
    "postcode": "10961",
    "city": "Berlin",
    "state": null,
    "country": "DE",
    "fullAddress": "Bergmannstraße 21, 10961 Berlin, DE",
    "latitude": 52.489026,
    "longitude": 13.3933796,
    "phone": "+49 30 6948138",
    "website": "https://www.barcomis.de/",
    "email": null,
    "facebook": null,
    "instagram": null,
    "openingHours": "Mo-Th 10:00-18:00; Fr-Su,PH 10:00-19:00",
    "brand": null,
    "operator": null,
    "cuisine": "coffee_shop",
    "wheelchair": "no",
    "wikidata": null,
    "searchLocation": "Kreuzberg, Berlin",
    "tags": {
        "addr:city": "Berlin",
        "addr:housenumber": "21",
        "addr:postcode": "10961",
        "addr:street": "Bergmannstraße",
        "amenity": "cafe",
        "contact:phone": "+49 30 6948138",
        "cuisine": "coffee_shop",
        "name": "Barcomi's Café & Kaffeerösterei",
        "outdoor_seating": "yes",
        "website": "https://www.barcomis.de/",
        "wheelchair": "no",
        "wifi": "no"
    },
    "scrapedAt": "2026-11-24T22:41:11Z"
}
```

## How much does it cost?

You pay per saved place: **$1.00 per 1,000 results**. There is no start fee and no monthly rental. Filters run on the OpenStreetMap server, so places that do not pass them are never charged.

| Run | Results | Cost |
|---|---|---|
| Cafes in one district | 100 | $0.10 |
| Restaurants, cafes and bars in a city | 5,000 | $5.00 |
| Every shop in a large city | 25,000 | $25.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **The data is only as complete as OpenStreetMap.** Volunteers map places, so coverage is very good in most of Europe and big cities, and thinner in many rural areas and in parts of Asia, Africa and Latin America. Not every business is on the map, and there are no reviews, ratings or photos.
- **Not every place has a phone or website.** In our test runs: Munich restaurants, cafes, bars, hotels, dentists and hairdressers had a phone in 54% and a website in 56% of 6,108 places (email 22%). Berlin shops: phone 29%, website 36%, email 10% of 21,658. Manhattan restaurants: phone 57%, website 65%. Bangkok restaurants: phone 14%, website 10%, city 3% of 3,000. Use the filters if you only want places with contact details.
- **Addresses are often incomplete.** Many places have a street and house number but no city or postcode (city was filled for 35% to 65% of places in our tests). Every place has coordinates.
- **"Without a website" means "no website in OpenStreetMap".** The business may still have one that nobody has added to the map.
- **Data can be up to one day old.** The main public server (overpass-api.de) is often at capacity and can queue a request for a minute. So the Actor reads from the free continent mirrors at ovp.dresel.systems first, which answer in seconds but update once a night, and uses the main server as the fallback. Edits made on OpenStreetMap today may not show up until tomorrow. If every server is down, the run fails with a clear message and you can simply start it again.
- **Speed.** In our tests a district took about 25 seconds (100 cafes), Berlin Mitte with 3 categories 41 seconds (7,453 places), Munich with 6 categories about 2 minutes (6,108 places), every shop in Berlin about 5 minutes (21,658 places) and hospitals plus dentists across Portugal about 3 minutes (1,270 places). Large areas are split into tiles automatically. Runs are slower when the mirrors are busy and the main server has to answer.
- **Place names must match OpenStreetMap.** Names are matched exactly (not fuzzy) against the local, English and international names. When a name exists several times, the biggest place is used and the log lists the others. "New York", for example, finds New York State, not the city.
- **Some places have no boundary under their common name.** "London" is mapped as a point, so the Actor searches a circle around its center (about 24 km for London) and says so in the log. Use the boundary name, such as "Greater London", for the exact area.
- **A place can appear twice** if mappers drew it both as a point and as a building outline. Results are de-duplicated by OpenStreetMap ID only.

---

Full documentation, all input options and a free trial: **[OpenStreetMap POI Scraper on Apify](https://apify.com/pipiagent/openstreetmap-poi-scraper)**
