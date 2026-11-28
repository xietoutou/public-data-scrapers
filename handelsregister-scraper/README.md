# Handelsregister Scraper

Search the official German common register portal [handelsregister.de](https://www.handelsregister.de) (Gemeinsames Registerportal der Länder) and get one clean record per company: name, register court, register type and number, seat, federal state and status. Use it for KYC and supplier checks, lead lists of German companies, market research and for matching your own customer data to official register numbers.

- **Straight from the source.** Data comes from the public register portal run by the German federal states, not from a third-party copy. This Actor is independent and not affiliated with the portal.
- **Search by name or look up by number.** Type company names or keywords, or paste register entries like `München HRB 6684`.
- **All filters of the advanced search.** Register type (HRA, HRB, GnR, PR, VR, GsR), register court, federal state, legal form, seat, postal code, city and street.
- **History included.** Previous names and seats, and the branch offices the portal lists, come with every company.
- **No login and no proxy needed.** Press Start and get data.
- **Fair to the portal.** The Actor keeps to the portal's limit of about 60 requests per hour.
- **Low price.** $4 per 1,000 results.

**Run it online, without code:** [Handelsregister Scraper - German Company Register Search](https://apify.com/pipiagent/handelsregister-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `handelsregister-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Example | What it is |
|---|---|---|
| `name` | Siemens Aktiengesellschaft | Company name as registered |
| `registerCourt` | Amtsgericht München | Local court that keeps the entry |
| `registerCourtCode` | D2601 | The portal's code for that court |
| `registerType` | HRB | HRA, HRB, GnR, PR, VR or GsR |
| `registerNumber` | 6684 | Register number, with letter suffix if there is one |
| `registerId` | Amtsgericht München HRB 6684 | Court, type and number in one line |
| `formerRegisterCourt` | Amtsgericht Lüdenscheid | Earlier court, when the portal shows one |
| `seat` | Berlin und München | Registered seat |
| `federalState` | Bayern | Federal state of the court |
| `status` | current | `current`, or `closed` when the register sheet is closed |
| `statusText` | aktuell | Status in the portal's own words |
| `previousNames` | [{name, seat}] | Earlier names and seats from the history |
| `branchCount` | 2 | Number of branch offices (Zweigniederlassungen) |
| `branches` | [{name, seat, status}] | The branch offices the result list shows |
| `availableDocuments` | ["AD", "CD", "HD", "SI"] | Which register printouts the portal offers for this entry |
| `searchQuery` | Siemens | The search that found this company |

The register types mean: **HRA** sole traders and partnerships (e.K., OHG, KG), **HRB** corporations (GmbH, AG, SE, UG), **GnR** cooperatives, **PR** partnerships of liberal professions, **VR** registered associations (e.V.), **GsR** registered civil-law partnerships (eGbR).

## Input examples

Search for a company name:

```json
{
    "searchQueries": ["Siemens"],
    "maxItems": 10
}
```

Find all GmbHs and AGs with "Bahn" in their name in two federal states, including closed entries:

```json
{
    "searchQueries": ["Bahn"],
    "registerType": "HRB",
    "federalStates": ["Baden-Württemberg", "Berlin"],
    "includeDeleted": true,
    "maxItems": 500
}
```

Look up exact register entries:

```json
{
    "registerLookups": ["München HRB 6684", "Berlin (Charlottenburg) HRB 50000 B"]
}
```

## Output examples

A company with name history:

```json
{
    "name": "BSH Hausgeräte GmbH",
    "registerCourt": "Amtsgericht München",
    "registerCourtCode": "D2601",
    "registerType": "HRB",
    "registerNumber": "75534",
    "registerId": "Amtsgericht München HRB 75534",
    "formerRegisterCourt": null,
    "seat": "München",
    "federalState": "Bayern",
    "status": "current",
    "statusText": "aktuell",
    "previousNames": [
        {"name": "Bosch-Siemens Hausgeräte Gesellschaft mit beschränkter Haftung", "seat": "München"},
        {"name": "BSH Bosch und Siemens Hausgeräte GmbH", "seat": "München"}
    ],
    "branchCount": 0,
    "branches": [],
    "availableDocuments": ["AD", "CD", "HD", "DK", "UT", "VÖ", "SI"],
    "searchQuery": "Siemens",
    "scrapedAt": "2026-11-28T10:08:33Z"
}
```

A company with a branch office:

```json
{
    "name": "Ernst Becker Bahn- und Tiefbau GmbH",
    "registerCourt": "Amtsgericht Essen",
    "registerCourtCode": "R2503",
    "registerType": "HRB",
    "registerNumber": "34338",
    "registerId": "Amtsgericht Essen HRB 34338",
    "formerRegisterCourt": null,
    "seat": "Essen",
    "federalState": "Nordrhein-Westfalen",
    "status": "current",
    "statusText": "aktuell",
    "previousNames": [],
    "branchCount": 2,
    "branches": [
        {"name": "Ernst Becker Bahn- und Tiefbau GmbH Zweigniederlassung Berlin", "seat": "Berlin", "status": "current"}
    ],
    "availableDocuments": ["AD", "CD", "DK", "UT", "VÖ", "SI"],
    "searchQuery": "Bahn",
    "scrapedAt": "2026-11-28T10:09:55Z"
}
```

## How much does it cost?

You pay per saved company: **$4.00 per 1,000 results**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| One company name, first 10 matches | 10 | $0.04 |
| One broad keyword, all matches the portal shows | 100 | $0.40 |
| 30 keywords with about 35 matches each | 1,000 | $4.00 |

Searches without matches cost nothing. Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Each search returns at most 100 companies.** This is the portal's own limit. When a search has more matches, the run log says so. Add filters (register court, register type, federal state) or more words, or split the search into several narrower ones.
- **About one search per minute.** The portal's terms allow about 60 retrievals per hour per user, and the Actor keeps to that: the first few requests go out a few seconds apart, then one request every 61 seconds, and never more than 60 requests in an hour. One search is one request, so the first 4 searches finish within a minute and after that you get about 1 search per minute (up to 100 companies each). The default run with one name finishes in 20 to 30 seconds. In our test, 7 searches took 3 minutes 40 seconds. A run with 60 searches takes about an hour.
- **Do not start several runs at the same time.** The limit is per user. Put all your names into one run instead.
- **Result list only, no register printouts.** The portal offers printouts (AD current, CD chronological, HD historical, SI structured content and more) for every entry. Each download would use one of the 60 requests per hour and they contain personal data of managing directors, so the Actor does not download them. `availableDocuments` tells you which ones exist, so you can open them on the portal yourself.
- **No addresses, managing directors or share capital.** The portal's result list does not show them, so they are not in the output.
- **Only the first branch office is listed.** When an entry has several branches, the result list shows the first one. `branchCount` has the full number.
- **"Exact company name" needs the full official name**, for example "Siemens Aktiengesellschaft", not "Siemens AG".
- **The federal state filter also matches branch offices.** A company registered in Essen can appear in a Berlin search when it has a branch in Berlin.
- **Duplicates are removed within a run.** When two searches find the same company, it is saved once, with the first search in `searchQuery`.

---

Full documentation, all input options and a free trial: **[Handelsregister Scraper on Apify](https://apify.com/pipiagent/handelsregister-scraper)**
