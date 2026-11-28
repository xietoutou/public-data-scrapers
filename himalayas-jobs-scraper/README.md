# Himalayas Jobs Scraper

Get remote job listings from [Himalayas](https://himalayas.app), one of the largest remote job boards with about 116,000 open remote jobs. The Actor reads the official public Himalayas Remote Jobs API and gives you one clean table: title, company, job type, seniority, categories, the countries and time zones applicants must be in, salary, dates and the apply link.

Use it for job alerts and job search, remote job newsletters, recruiting and sourcing, sales prospecting (companies that hire remotely), salary research and labour market analysis.

- **Search like on the site.** Keywords, countries, worldwide only, job type, seniority, company and time zone are applied by Himalayas itself, so filtered runs are fast.
- **Extra filters.** Keywords in the title only, categories, salary only and posted or updated within the last N days.
- **Only new jobs.** Turn on **Only new jobs** for daily schedules and pay only for jobs you have not seen before.
- **Salary data.** About 4 in 10 jobs state a salary, with currency and pay period (year, month, hour).
- **No login, no API key, no proxy.** The Actor uses the public API that Himalayas offers to developers.
- **Low price.** $1.00 per 1,000 jobs.

**Run it online, without code:** [Himalayas Jobs Scraper - Remote Jobs with Salaries](https://apify.com/pipiagent/himalayas-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `himalayas-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Example | Notes |
|---|---|---|
| `source`, `jobId` | Himalayas, carrier-com/carrier-icp-associate-sales-director | `jobId` is the company and job part of the Himalayas URL |
| `title`, `company`, `companySlug`, `companyUrl`, `companyLogo` | Carrier ICP Associate Sales Director, Carrier | `companyUrl` is the company's page on Himalayas |
| `employmentType` | Full Time | Full Time, Part Time, Contractor, Temporary, Intern, Volunteer or Other |
| `seniority` | ["Director"] | A list, because a job can accept several levels |
| `categories`, `parentCategories` | ["Sales Director", "Sales Manager"], ["Sales"] | Himalayas' own categories |
| `locationRestrictions`, `isWorldwide` | ["United States"], false | Countries where applicants must live. An empty list means worldwide |
| `timezoneRestrictions` | [-10, -9, -8, -7, -6, -5] | Accepted UTC offsets in hours |
| `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod` | 143000, 286000, USD, year | Only when the job states a salary |
| `updatedAt`, `expiresAt` | 2026-11-25T21:04:15Z | ISO 8601 UTC. `updatedAt` is when the job was posted or last updated |
| `jobUrl`, `applyUrl` | | The job on Himalayas and Himalayas' apply link |
| `excerpt`, `description`, `descriptionHtml` | | Short summary, full text, and HTML (optional) |
| `searchQuery` | python | The keyword that found the job |
| `attribution` | Remote job data from Himalayas (https://himalayas.app) | Source credit |

Fields that a job does not have are `null` or an empty list, so every record has the same columns.

## Input examples

Python and data engineering jobs, newest first:

```json
{
    "keywords": ["python", "data engineer"],
    "maxItems": 50
}
```

React jobs open to people in Germany, with "react" in the title:

```json
{
    "keywords": ["react"],
    "countries": ["Germany"],
    "keywordsInTitleOnly": true,
    "maxItems": 30
}
```

Senior and manager jobs that are open worldwide and state a salary:

```json
{
    "worldwideOnly": true,
    "seniority": ["Senior", "Manager"],
    "withSalaryOnly": true,
    "maxItems": 200
}
```

A daily alert for new customer support jobs:

```json
{
    "keywords": ["customer support", "customer success"],
    "onlyNew": true,
    "maxItems": 500
}
```

## Output example

```json
{
    "source": "Himalayas",
    "jobId": "carrier-com/carrier-icp-associate-sales-director",
    "title": "Carrier ICP Associate Sales Director",
    "company": "Carrier",
    "companySlug": "carrier-com",
    "companyUrl": "https://himalayas.app/companies/carrier-com",
    "companyLogo": "https://cdn-images.himalayas.app/b6jiwu9lo1sd6yzhh64wc6nl0tbx",
    "employmentType": "Full Time",
    "seniority": ["Director"],
    "categories": ["Sales Director", "Associate Sales Director", "Regional Sales Director", "Sales Manager"],
    "parentCategories": ["Sales"],
    "locationRestrictions": ["United States"],
    "isWorldwide": false,
    "timezoneRestrictions": [-10, -9, -8, -7, -6, -5, 14],
    "salaryMin": 143000,
    "salaryMax": 286000,
    "salaryCurrency": "USD",
    "salaryPeriod": "year",
    "updatedAt": "2026-11-25T21:04:15Z",
    "expiresAt": "2027-01-24T21:04:15Z",
    "jobUrl": "https://himalayas.app/companies/carrier-com/jobs/carrier-icp-associate-sales-director",
    "applyUrl": "https://himalayas.app/companies/carrier-com/jobs/carrier-icp-associate-sales-director?utm_source=api",
    "excerpt": "About Carrier Carrier Global Corporation, global leader in intelligent climate and energy solutions, is committed to creating innovations that bring comfort, safety and sustainability to life.",
    "description": "About Carrier\n\nCarrier Global Corporation, global leader in intelligent climate and energy solutions, is committed to creating innovations that bring comfort, safety and sustainability to life...",
    "searchQuery": null,
    "attribution": "Remote job data from Himalayas (https://himalayas.app)",
    "scrapedAt": "2026-11-25T22:01:25Z"
}
```

## How much does it cost?

You pay per saved job: **$1.00 per 1,000 jobs**. There is no start fee and no monthly rental. Filters are applied before saving, so you pay only for jobs that match.

| Run | Jobs | Cost |
|---|---|---|
| Daily check for new Python jobs | about 50 | $0.05 |
| 1,000 jobs with a salary | 1,000 | $1.00 |
| Everything added or updated in one day | about 2,000 | $2.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Max results is 1,000 when you leave it empty.** Himalayas lists about 116,000 jobs, so a run never downloads all of them by accident. Set **Max results** higher (up to 150,000) when you want more. With no filters at all, the Actor saves the 50 newest jobs as an example.
- **Each listing is read at most 5,000 jobs deep** (or 5 times Max results, if that is larger). This matters for filters the Actor checks itself (categories, salary only, keywords in the title only) when few jobs match. Pages deep in the feed load more slowly (about 1.7 seconds each in our test), so a filter that matches nothing can take a few minutes before the run ends with 0 jobs.
- **Large searches are cut off by Himalayas.** The Himalayas search shows 5,000 as the count for any large search. With **Best match** it returns at most about 5,000 jobs; with **Newest first** it went deeper in our tests (about 12,700 jobs for "python"), and the Actor then stops at the reading limit above. Narrow a large search with countries, job type or seniority.
- **The date is the last update, not the first posting.** Himalayas gives one date per job, which changes when the employer edits the job. About 2,000 jobs are added or updated each day (measured in November 2026). **Posted or updated within (days)** uses this date.
- **"Newest first" in search is approximate.** Himalayas sorts searches by its own date, so a few older jobs can appear among newer ones.
- **One country per search.** Himalayas accepts one country at a time, so each keyword is searched once per country. Jobs open worldwide are included unless you turn on **Exclude worldwide jobs**.
- **Speed.** Himalayas allows a limited number of requests from public callers, so the Actor waits half a second between requests. 1,000 jobs take about one minute. If Himalayas asks the Actor to slow down, it waits and tries again.
- **Data is up to two hours old.** Himalayas serves the API from a cache that refreshes every one to two hours.
- **No company profiles.** Only job listings are available through the API.

---

Full documentation, all input options and a free trial: **[Himalayas Jobs Scraper on Apify](https://apify.com/pipiagent/himalayas-jobs-scraper)**
