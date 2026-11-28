# BidNet Direct Scraper

Extract US government bids, RFPs and RFQs from [BidNet Direct](https://www.bidnetdirect.com), a bid site that lists solicitations from state, local and federal agencies across the United States. At the time of testing it listed 28,424 open solicitations and about 6.5 million closed ones. Use it to find new sales opportunities, watch what agencies in your region buy, track competitors' markets or build a bid database.

- **Two ways to collect bids.** Search the whole site with keywords, states, industry categories and agency type, or collect every bid from the agency pages you choose.
- **Open, closed and awarded bids.** Closed and awarded bids show much more to visitors: the agency, the description, the source link and often the buyer contact.
- **Clean, flat output.** English field names, dates in ISO format, closing times converted to UTC, full links to every bid.
- **No login and no proxy needed.** Press Start and get data.
- **Low price.** $3 per 1,000 results.

**Run it online, without code:** [BidNet Direct Scraper - US Government Bids, RFPs & RFQs](https://apify.com/pipiagent/bidnet-direct-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `bidnet-direct-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Open bids (search) | Open bids (agency pages) | Closed and awarded bids |
|---|---|---|---|
| Title, state, publication date, closing date | Yes | Yes | Yes |
| Agency type (member agency, state and local, federal) | Yes | No | Yes in search |
| Days left until closing | Yes | No | No |
| Issuing organization (agency name) | No, locked | Yes | Yes |
| Solicitation number | No, locked | Yes | Yes for member agency notices |
| Exact closing time with time zone | With details | With details | With details |
| AI overview (short summary written by BidNet) | With details, state and local and federal bids | With details, when shown | With details, when shown |
| Description and source link | No, locked | No, locked | With details |
| Solicitation type, owner organization, question deadline, buyer contact | No, locked | No, locked | With details, member agency notices |
| Award date | No | No | Yes, awarded bids on agency pages |

"Locked" means BidNet Direct shows "Registered members only" to visitors who are not logged in. This Actor does not log in, so it cannot get those fields. Each result has a `lockedFields` list that says which fields were locked on that bid's page.

"With details" means you turn on **Open each solicitation page**.

## Input examples

The newest open bids on the whole site:

```json
{
    "maxItems": 100
}
```

Open paving and roofing construction bids in Florida and Georgia, with closing times and AI overviews:

```json
{
    "mode": "search",
    "keywords": ["paving", "roofing"],
    "states": ["Florida", "Georgia"],
    "categories": ["Construction"],
    "includeDetails": true,
    "maxItems": 200
}
```

Federal bids published in the last 24 hours:

```json
{
    "agencyType": "federal",
    "publishedWithin": "24h",
    "maxItems": 500
}
```

Closed bids posted by member agencies, with agency, description and buyer contact:

```json
{
    "status": "closed",
    "agencyType": "member",
    "includeDetails": true,
    "maxItems": 100
}
```

Every open bid of one agency, with its solicitation numbers:

```json
{
    "mode": "agencies",
    "agencyUrls": ["https://www.bidnetdirect.com/new-york/albany-county"],
    "status": "open"
}
```

## Output examples

An open bid from a search, with details turned on:

```json
{
    "solicitationId": "444246770396",
    "title": "LMIG Resurfacing",
    "status": "open",
    "agencyType": "State & Local Bids",
    "location": "Georgia",
    "publicationDate": "2026-11-24",
    "closingDate": "2026-12-15",
    "daysLeft": 18,
    "publishedAt": "2026-11-24T12:58:00Z",
    "closesAt": "2026-12-15T15:00:00Z",
    "closingTimeText": "12/15/2026 10:00 AM EST",
    "aiOverview": "Road widening and asphalt resurfacing project covering approximately 26.47 miles across 14 different road segments, involving various asphalt types and pavement widths with center and edge line striping.",
    "lockedFields": ["Issuing Organization", "Solicitation Number", "Description", "Source"],
    "detailsScraped": true,
    "url": "https://www.bidnetdirect.com/georgia/solicitations/open-bids/statewide/LMIG-Resurfacing/444246770396?origin=0&target=view",
    "searchKeyword": "paving",
    "searchCategory": "Construction",
    "scrapedAt": "2026-11-27T00:21:32Z"
}
```

An open bid from an agency page:

```json
{
    "solicitationId": "0000444631",
    "title": "ICE MELT 2026-2027 SEASON",
    "status": "open",
    "solicitationNumber": "RFB #2026-161",
    "issuingOrganization": "Albany County",
    "location": "New York",
    "publicationDate": "2026-11-26",
    "closingDate": "2026-12-17",
    "publishedAt": "2026-11-26",
    "closesAt": "2026-12-17T16:00:00Z",
    "closingTimeText": "12/17/2026 11:00 AM EST",
    "lockedFields": ["Description", "Bid Documents", "Buyer Contact"],
    "detailsScraped": true,
    "url": "https://www.bidnetdirect.com/new-york/solicitations/open-bids/ICE-MELT-2026-2027-SEASON/0000444631?purchasingGroupId=8411151&origin=2",
    "agencyPageName": "Albany County",
    "agencyPageUrl": "https://www.bidnetdirect.com/new-york/albany-county",
    "scrapedAt": "2026-11-27T00:27:59Z"
}
```

A closed member agency bid with details (contact details replaced with placeholders here):

```json
{
    "solicitationId": "0000444386",
    "title": "OUTDOOR & WINTER GEAR",
    "status": "closed",
    "solicitationNumber": "RFQ-WC260810",
    "referenceNumber": "0000444386",
    "issuingOrganization": "Westchester County - Purchasing",
    "agencyType": "Member Agency Bids",
    "solicitationType": "RFQ - Request for Quote (Informal)",
    "location": "New York",
    "locationDetail": "United States, New York, Westchester County",
    "publicationDate": "2026-11-23",
    "closingDate": "2026-11-25",
    "publishedAt": "2026-11-23T18:30:00Z",
    "closesAt": "2026-11-25T19:00:00Z",
    "closingTimeText": "11/25/2026 02:00 PM EST",
    "description": "OUTDOOR & WINTER GEAR",
    "purchaseType": "One Time Only- Delivery Date:ASAP",
    "piggybackContract": "No",
    "sourceId": "PU.AG.USA.1275.C3868901",
    "contactName": "Jane Doe",
    "contactEmail": "buyer@example.gov",
    "contactPhone": "555-010-0100",
    "detailsScraped": true,
    "url": "https://www.bidnetdirect.com/new-york/westchester-county-purchasing/solicitations/OUTDOOR-WINTER-GEAR/0000444386?origin=0",
    "scrapedAt": "2026-11-27T00:22:32Z"
}
```

Every result has the same set of fields. Fields the page did not show are `null`, and they are left out of the examples above to keep them short.

## How much does it cost?

You pay per saved result: **$3.00 per 1,000 results**. There is no start fee and no monthly rental. Turning on **Open each solicitation page** does not change the price, it only makes the run slower.

| Run | Results | Cost |
|---|---|---|
| The newest 100 open bids | 100 | $0.30 |
| 1,000 bids from one state | 1,000 | $3.00 |
| 10,000 bids | 10,000 | $30.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Open bids hide the agency and solicitation number in search.** BidNet Direct locks the issuing organization, solicitation number, description, documents and buyer contact of open bids for visitors who are not logged in. The agency pages mode gets the agency name and solicitation number of open bids from the agency's own list.
- **The Actor waits 5 seconds between requests.** BidNet Direct's robots.txt asks crawlers for a 5 second delay, and the Actor follows it. One list page holds 25 bids, so a search saves about 100 bids in 25 seconds, or roughly 250 to 300 bids per minute. With **Open each solicitation page** on, each bid takes about 5 more seconds, so 10 bids with details took about 60 seconds in our tests.
- **Results do not include the category.** BidNet Direct uses categories only as a filter. When you pick categories, each one runs its own search and the `searchCategory` field tells you which category found the bid.
- **Member agency bids show only a publication date, not a time.** For these bids `publishedAt` holds a date like `2026-11-24`. Closing times always include the time and time zone when details are on.
- **Keywords in the agency pages mode only check the title and solicitation number,** and the Actor reads every page of the agency's list to find matches. A purchasing group page such as `new-york` with 357 open bids took 15 pages and 80 seconds.
- **A bid is saved once per run.** When several keywords or categories find the same bid, it is saved with the first keyword and category that found it.
- **"Max results" counts the whole run.** With several keywords, the first keyword can use up the limit before the next one starts. Raise the limit or run keywords separately.
- **Awarded bids are only available in the agency pages mode,** and they show the award date but not the winning vendor.
- **Dates are shown as BidNet Direct shows them.** In our tests some closed bids had a closing date earlier than their publication date. The Actor does not change these values.

---

Full documentation, all input options and a free trial: **[BidNet Direct Scraper on Apify](https://apify.com/pipiagent/bidnet-direct-scraper)**
