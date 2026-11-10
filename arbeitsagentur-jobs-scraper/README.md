# Arbeitsagentur Jobs Scraper

Get job listings in Germany from the [Jobsuche](https://www.arbeitsagentur.de/jobsuche/) of the Bundesagentur für Arbeit, the federal employment agency and the largest job board in Germany with about a million open positions. Search by job title, city or postcode and radius, and download one clean table with English column names: title, company, location with coordinates, salary range, working time, remote option, contract, start date and, if you want, the full description.

Use it for job alerts and job search in Germany, recruiting and sourcing, labour market and salary research, lead generation (companies that are hiring in a region), relocation research and job aggregator sites.

- **About a million jobs.** Jobs, apprenticeships (Ausbildung), dual study places, internships and self-employment offers from all of Germany.
- **Real filters.** Search terms, location and radius, published or updated in the last N days, job type, full-time or part-time, permanent or fixed-term, employer, career changers, and no temp agencies or private recruiters.
- **Salaries when the employer states them.** Salary range or fixed pay per year or hour, and apprenticeship pay by year.
- **English output.** German codes are translated (full-time, permanent, Bavaria, apprenticeship), so the table works for non-German speakers too.
- **Full descriptions optional.** Turn on **Include full description** to get each job's text, partner site and agency flags.
- **Fast.** 100 jobs per request: 10,000 jobs take about 3 minutes without descriptions.
- **No login, no API key, no proxy.**
- **Low price.** $1.00 per 1,000 jobs.

**Run it online, without code:** [Arbeitsagentur Jobs Scraper - German Jobs with Salaries](https://apify.com/pipiagent/arbeitsagentur-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `arbeitsagentur-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Example | Notes |
|---|---|---|
| `referenceNumber`, `jobUrl` | 10001-1003973437-S | The job's number and its page on arbeitsagentur.de |
| `title`, `company` | (Senior) Data Migration Engineer (m/w/d), Profi Talent Recruitment UG | |
| `occupation`, `otherOccupations` | Data Engineer | The occupation the agency assigned, in German |
| `jobType` | job | job, apprenticeship, internship or trainee, self-employment |
| `workingTime` | ["full-time"] | Also part-time mornings, afternoons, evenings or flexible, shifts, nights or weekends, minijob |
| `remotePossible`, `remoteType`, `remotePercent` | true, share of time, 100 | When the employer says so |
| `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod` | 70000, 90000, EUR, year | Only when the listing states pay |
| `apprenticePayByYear` | [1250, 1350, 1450] | Monthly apprenticeship pay in years 1, 2, 3 |
| `contract`, `contractMonths`, `contractEnds` | permanent | Fixed-term jobs may give the length or end date |
| `suitableForCareerChangers` | true | Quereinstieg possible |
| `startDate`, `publishedAt`, `firstPublishedAt`, `updatedAt` | 2027-02-01, 2026-11-06 | Dates as the job search gives them |
| `city`, `postalCode`, `region`, `country`, `latitude`, `longitude` | München, Bavaria, Germany, 48.15, 11.55 | `locations` lists all places when a job has several |
| `externalUrl`, `partnerSite` | | The listing on the employer's or a partner board's site, when the job comes from there |
| `description`, `isTemporaryAgency`, `isPrivateAgency` | | With **Include full description** only. The text is in the language of the listing, mostly German |

Fields that a listing does not provide are `null`, so every record has the same columns.

## Input examples

Software developer jobs within 25 km of Berlin, published in the last 7 days:

```json
{
    "searchTerms": ["Softwareentwickler", "Software Engineer"],
    "location": "Berlin",
    "radiusKm": 25,
    "publishedWithinDays": 7
}
```

Permanent full-time nursing jobs in three cities, without temp agencies, with descriptions:

```json
{
    "searchTerms": ["Pflegefachkraft"],
    "locations": ["Hamburg", "Köln", "Leipzig"],
    "workingTime": ["full-time"],
    "contract": "permanent",
    "excludeTemporaryAgencies": true,
    "includeDescription": true
}
```

All apprenticeships of one employer:

```json
{
    "employer": "Deutsche Bahn AG",
    "jobType": "apprenticeship",
    "maxItems": 1000
}
```

## Output example

```json
{
    "referenceNumber": "10001-1003973437-S",
    "title": "(Senior) Data Migration Engineer (m/w/d) Schwerpunkt Teamcenter",
    "company": "Profi Talent Recruitment UG PTR",
    "occupation": "Data Engineer",
    "otherOccupations": [],
    "jobType": "job",
    "workingTime": ["full-time"],
    "remotePossible": true,
    "remoteType": "share of time",
    "remotePercent": 100,
    "salaryMin": 70000,
    "salaryMax": 90000,
    "salaryCurrency": "EUR",
    "salaryPeriod": "year",
    "apprenticePayByYear": null,
    "contract": "permanent",
    "contractMonths": null,
    "contractEnds": null,
    "suitableForCareerChangers": null,
    "startDate": "2027-02-01",
    "publishedAt": "2026-11-06",
    "firstPublishedAt": "2026-11-06",
    "updatedAt": "2026-11-06T08:32:51.491",
    "city": "München",
    "postalCode": null,
    "region": "Bavaria",
    "country": "Germany",
    "latitude": 48.152104426,
    "longitude": 11.55020237,
    "locations": null,
    "jobUrl": "https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1003973437-S",
    "externalUrl": null,
    "description": "**Deine Aufgaben:**\n\n- Entwicklung und Umsetzung komplexer Datenmigrationsstrategien für Teamcenter\n- Analyse bestehender Datenlandschaften...",
    "partnerSite": null,
    "isTemporaryAgency": null,
    "isPrivateAgency": true
}
```

## How much does it cost?

You pay per saved job: **$1.00 per 1,000 jobs**. There is no start fee and no monthly rental. Filters are applied before saving, so you pay only for jobs that match.

| Run | Jobs | Cost |
|---|---|---|
| Daily check for new software developer jobs in Berlin | about 10 | $0.01 |
| All nursing jobs (Pflegefachkraft) in Hamburg | about 800 | $0.80 |
| One search across Germany | up to 10,000 | up to $10.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **At most 10,000 jobs per search.** The job search shows 100 pages of 100. For more, split the search with **More locations** or more specific search terms; jobs found twice are saved once.
- **Listings are in German.** Titles, occupations and descriptions stay in the employer's words. Search terms work in German and English, but German job titles find more.
- **Salaries only when stated.** Most employers in Germany do not publish pay; expect a salary on roughly one job in ten.
- **The date filter is approximate on the job search side**, so the Actor checks the published and updated dates again and drops older listings.
- **Descriptions take longer.** **Include full description** reads one extra page per job, about 4 jobs per second.
- **This is unofficial.** The Actor is not made by, endorsed by or connected to the Bundesagentur für Arbeit. It reads the same public job search that the website uses.

---

Full documentation, all input options and a free trial: **[Arbeitsagentur Jobs Scraper on Apify](https://apify.com/pipiagent/arbeitsagentur-jobs-scraper)**
