# Lever Jobs Scraper

Get every open job from companies that hire on [Lever](https://www.lever.co). Add the companies you care about and get one clean table of their jobs, straight from their official jobs.lever.co boards. Use it for recruiting and sourcing, sales prospecting (a company that hires is a company that buys), competitor tracking, salary research and job boards.

- **Any Lever board.** Company ids, jobs.lever.co URLs, EU boards, single job links and careers pages that link to Lever.
- **Fresh data from the source.** The same feed the company's careers page reads from. No aggregator delay, no expired reposts.
- **Rich fields.** Lever publishes team, country, workplace type (remote, hybrid, on-site) and employment type for most jobs.
- **Filters before you pay.** Job title keywords, locations, remote only, department and posted within the last N days. You are charged only for jobs that match.
- **No login, no API key and no proxy needed.**
- **Low price.** $1.00 per 1,000 jobs.

**Run it online, without code:** [Lever Jobs Scraper - All Jobs from Any jobs.lever.co Board](https://apify.com/pipiagent/lever-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `lever-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

One result is one job posting, with the same fields for every company:

| Field | Example | Notes |
|---|---|---|
| `company`, `companySlug` | Spotify, spotify | |
| `jobId`, `requisitionId` | 2d67c471-9015-41c0-a041-b982ec4a14fd | |
| `title`, `department`, `team` | Account Executive - Commercial, Spotify Technology | |
| `location`, `locations` | London | Primary location and the full list for multi-location jobs |
| `country`, `countryCode` | United Kingdom, GB | From Lever |
| `workplaceType`, `isRemote` | remote / hybrid / onsite | From Lever (remote, hybrid or on-site) |
| `employmentType`, `seniority` | Full-time | Normalised to Full-time, Part-time, Contract, Temporary, Internship |
| `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`, `salaryText` | | Only when the company publishes a pay range |
| `postedAt`, `updatedAt` | 2026-10-23T21:51:17Z | Created date, ISO 8601 UTC |
| `jobUrl`, `applyUrl` | | |
| `description`, `descriptionHtml` | | Plain text by default, HTML optional |
| `careerPageUrl`, `scrapedAt` | | The input line the job came from, and when it was collected |

Fields that Lever does not provide for a job are `null`, so every record has the same columns.

## Input examples

The 10 newest jobs at each company:

```json
{
    "careerPages": [
        "spotify",
        "https://jobs.lever.co/palantir"
    ],
    "maxJobsPerCompany": 10
}
```

Engineering and product jobs in the US or remote, posted in the last 14 days, without interns:

```json
{
    "careerPages": [
        "spotify",
        "https://jobs.lever.co/palantir"
    ],
    "titleKeywords": [
        "engineer",
        "product manager"
    ],
    "excludeTitleKeywords": [
        "intern"
    ],
    "locations": [
        "United States",
        "Remote"
    ],
    "postedWithinDays": 14
}
```

## Output example

```json
{
    "company": "Spotify",
    "companySlug": "spotify",
    "ats": "Lever",
    "jobId": "2d67c471-9015-41c0-a041-b982ec4a14fd",
    "title": "Account Executive - Commercial, Spotify Technology",
    "department": "Operations and Business Support",
    "team": "Platform",
    "location": "London",
    "locations": [
        "London"
    ],
    "country": "United Kingdom",
    "countryCode": "GB",
    "workplaceType": "hybrid",
    "isRemote": false,
    "employmentType": "Full-time",
    "seniority": null,
    "salaryMin": null,
    "salaryMax": null,
    "salaryCurrency": null,
    "salaryPeriod": null,
    "salaryText": null,
    "postedAt": "2026-10-23T21:51:17Z",
    "updatedAt": null,
    "requisitionId": null,
    "jobUrl": "https://jobs.lever.co/spotify/2d67c471-9015-41c0-a041-b982ec4a14fd",
    "applyUrl": "https://jobs.lever.co/spotify/2d67c471-9015-41c0-a041-b982ec4a14fd/apply",
    "description": "Spotify Technology is our business-to-business software team, helping organizations improve how they build and deliver software. ...",
    "careerPageUrl": "spotify",
    "scrapedAt": "2026-10-28T17:40:31Z"
}
```

## How much does it cost?

You pay per saved job: **$1.00 per 1,000 jobs**. There is no start fee and no monthly rental. Filters run before jobs are saved, so you only pay for jobs that match.

| Run | Jobs | Cost |
|---|---|---|
| 10 newest jobs at 5 companies | 50 | $0.05 |
| All jobs at a mid-size company | 300 | $0.30 |
| All jobs at 20 companies, about 150 each | 3,000 | $3.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **You choose the companies.** This Actor reads the Lever job boards you give it. It does not search every company on Lever. To track a market, build a list of companies once and run it on a schedule.
- **Big boards take a few minutes.** Lever answers slowly for large lists: a board with 4,100 jobs took about 5 minutes in our tests. Most boards finish in seconds.
- **Company name comes from the URL.** Lever does not publish a clean company name, so "spotify" becomes "Spotify".
- **Only Lever.** Job boards on other systems are skipped with a warning. Use [Career Site Jobs Scraper](https://apify.com/pipiagent/career-site-jobs-scraper) for a mixed list.

---

Full documentation, all input options and a free trial: **[Lever Jobs Scraper on Apify](https://apify.com/pipiagent/lever-jobs-scraper)**
