# Greenhouse Jobs Scraper

Get every open job from companies that hire on [Greenhouse](https://www.greenhouse.com). Add the companies you care about and get one clean table of their jobs, straight from their official Greenhouse job boards. Use it for recruiting and sourcing, sales prospecting (a company that hires is a company that buys), competitor tracking, salary research and job boards.

- **Any Greenhouse board.** Company ids, board URLs (old and new style, EU boards), single job links and careers pages that embed Greenhouse.
- **Fresh data from the source.** The same feed the company's careers page reads from. No aggregator delay, no expired reposts.
- **Fast.** Most boards finish in a few seconds, descriptions included.
- **Filters before you pay.** Job title keywords, locations, remote only, department and posted within the last N days. You are charged only for jobs that match.
- **No login, no API key and no proxy needed.**
- **Low price.** $1.00 per 1,000 jobs.

**Run it online, without code:** [Greenhouse Jobs Scraper - All Jobs from Any Greenhouse Board](https://apify.com/pipiagent/greenhouse-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `greenhouse-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

One result is one job posting, with the same fields for every company:

| Field | Example | Notes |
|---|---|---|
| `company`, `companySlug` | Stripe, stripe | |
| `jobId`, `requisitionId` | 8284978 | |
| `title`, `department`, `team` | Account Executive - Travel, Ticketing & Hospitality (Hunter) | |
| `location`, `locations` | London | Primary location and the full list for multi-location jobs |
| `country`, `countryCode` | United Kingdom, GB | Worked out from the location text |
| `workplaceType`, `isRemote` | remote / hybrid / onsite | Sometimes set by the company, otherwise from the word "remote" or "hybrid" in the location or title |
| `employmentType`, `seniority` | Full-time | Normalised to Full-time, Part-time, Contract, Temporary, Internship |
| `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`, `salaryText` | | Only when the company publishes a pay range. Ranges below 500 are marked hourly, the rest yearly |
| `postedAt`, `updatedAt` | 2026-10-28T16:45:25Z | First published date, ISO 8601 UTC |
| `jobUrl`, `applyUrl` | | |
| `description`, `descriptionHtml` | | Plain text by default, HTML optional |
| `careerPageUrl`, `scrapedAt` | | The input line the job came from, and when it was collected |

Fields that Greenhouse does not provide for a job are `null`, so every record has the same columns.

## Input examples

The 10 newest jobs at each company:

```json
{
    "careerPages": [
        "airbnb",
        "stripe",
        "https://job-boards.greenhouse.io/gitlab"
    ],
    "maxJobsPerCompany": 10
}
```

Engineering and product jobs in the US or remote, posted in the last 14 days, without interns:

```json
{
    "careerPages": [
        "airbnb",
        "stripe"
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
    "company": "Stripe",
    "companySlug": "stripe",
    "ats": "Greenhouse",
    "jobId": "8284978",
    "title": "Account Executive - Travel, Ticketing & Hospitality (Hunter)",
    "department": "1185 Account Executives (EMEA)",
    "team": null,
    "location": "London",
    "locations": [
        "London"
    ],
    "country": "United Kingdom",
    "countryCode": "GB",
    "workplaceType": null,
    "isRemote": null,
    "employmentType": null,
    "seniority": null,
    "salaryMin": null,
    "salaryMax": null,
    "salaryCurrency": null,
    "salaryPeriod": null,
    "salaryText": null,
    "postedAt": "2026-10-28T16:45:25Z",
    "updatedAt": "2026-10-28T16:45:25Z",
    "requisitionId": null,
    "jobUrl": "https://stripe.com/jobs/search?gh_jid=8284978",
    "applyUrl": "https://stripe.com/jobs/search?gh_jid=8284978",
    "description": "Who we are\n\nAbout Stripe\n\nStripe is a financial infrastructure platform for businesses. ...",
    "careerPageUrl": "stripe",
    "scrapedAt": "2026-10-28T17:40:09Z"
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

- **You choose the companies.** This Actor reads the Greenhouse job boards you give it. It does not search every company on Greenhouse. To track a market, build a list of companies once and run it on a schedule.
- **Country comes from the location text.** Greenhouse gives only a location such as "San Francisco, CA" or "Remote - Germany". The country is worked out from it, which is right in most cases but not always ("Remote - EMEA" has no single country).
- **Only Greenhouse.** Job boards on other systems are skipped with a warning. Use [Career Site Jobs Scraper](https://apify.com/pipiagent/career-site-jobs-scraper) for a mixed list.

---

Full documentation, all input options and a free trial: **[Greenhouse Jobs Scraper on Apify](https://apify.com/pipiagent/greenhouse-jobs-scraper)**
