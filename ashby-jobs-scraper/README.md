# Ashby Jobs Scraper

Get every open job from companies that hire on [Ashby](https://www.ashbyhq.com), the applicant tracking system used by many AI and tech startups such as OpenAI, Notion and Ramp. Add the companies you care about and get one clean table of their jobs, straight from their official jobs.ashbyhq.com boards. Use it for recruiting and sourcing, sales prospecting (a company that hires is a company that buys), competitor tracking, salary research and startup job boards.

- **Any Ashby board.** Company ids, jobs.ashbyhq.com URLs, single job links and careers pages that embed Ashby.
- **Salary ranges.** Published compensation is split into min, max, currency and period.
- **Fast.** Most boards finish in a few seconds, descriptions included.
- **Filters before you pay.** Job title keywords, locations, remote only, department and posted within the last N days. You are charged only for jobs that match.
- **No login, no API key and no proxy needed.**
- **Low price.** $1.00 per 1,000 jobs.

**Run it online, without code:** [Ashby Jobs Scraper - All Jobs from Any jobs.ashbyhq.com Board](https://apify.com/pipiagent/ashby-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `ashby-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

One result is one job posting, with the same fields for every company:

| Field | Example | Notes |
|---|---|---|
| `company`, `companySlug` | OpenAI, openai | |
| `jobId`, `requisitionId` | 9878a31f-423b-43cc-b169-8bb7e55b8fc7 | |
| `title`, `department`, `team` | Land and Data Center Development | |
| `location`, `locations` | San Francisco | Primary location and the full list for multi-location jobs |
| `country`, `countryCode` | United States, US | From Ashby |
| `workplaceType`, `isRemote` | remote / hybrid / onsite | When the company sets it |
| `employmentType`, `seniority` | Full-time | Normalised to Full-time, Part-time, Contract, Temporary, Internship |
| `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`, `salaryText` | | When the company publishes compensation, which many Ashby companies do |
| `postedAt`, `updatedAt` | 2026-10-28T04:39:11Z | Published date, ISO 8601 UTC |
| `jobUrl`, `applyUrl` | | |
| `description`, `descriptionHtml` | | Plain text by default, HTML optional |
| `careerPageUrl`, `scrapedAt` | | The input line the job came from, and when it was collected |

Fields that Ashby does not provide for a job are `null`, so every record has the same columns.

## Input examples

The 10 newest jobs at each company:

```json
{
    "careerPages": [
        "openai",
        "notion",
        "https://jobs.ashbyhq.com/ramp"
    ],
    "maxJobsPerCompany": 10
}
```

Engineering and product jobs in the US or remote, posted in the last 14 days, without interns:

```json
{
    "careerPages": [
        "openai",
        "notion"
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
    "company": "OpenAI",
    "companySlug": "openai",
    "ats": "Ashby",
    "jobId": "9878a31f-423b-43cc-b169-8bb7e55b8fc7",
    "title": "Land and Data Center Development",
    "department": "Scaling",
    "team": "Compute",
    "location": "San Francisco",
    "locations": [
        "San Francisco"
    ],
    "country": "United States",
    "countryCode": "US",
    "workplaceType": null,
    "isRemote": null,
    "employmentType": "Full-time",
    "seniority": null,
    "salaryMin": 212000,
    "salaryMax": 295000,
    "salaryCurrency": "USD",
    "salaryPeriod": "year",
    "salaryText": "$212K – $295K • Offers Equity",
    "postedAt": "2026-10-28T04:39:11Z",
    "updatedAt": null,
    "requisitionId": null,
    "jobUrl": "https://jobs.ashbyhq.com/openai/9878a31f-423b-43cc-b169-8bb7e55b8fc7",
    "applyUrl": "https://jobs.ashbyhq.com/openai/9878a31f-423b-43cc-b169-8bb7e55b8fc7/application",
    "description": "About the Team\n\nOpenAI’s Compute organization builds the infrastructure that powers frontier AI training and inference. ...",
    "careerPageUrl": "openai",
    "scrapedAt": "2026-10-28T11:47:32Z"
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

- **You choose the companies.** This Actor reads the Ashby job boards you give it. It does not search every company on Ashby. To track a market, build a list of companies once and run it on a schedule.
- **Salary only when published.** Many Ashby companies publish a range, but not all.
- **Only Ashby.** Job boards on other systems are skipped with a warning. Use [Career Site Jobs Scraper](https://apify.com/pipiagent/career-site-jobs-scraper) for a mixed list.

---

Full documentation, all input options and a free trial: **[Ashby Jobs Scraper on Apify](https://apify.com/pipiagent/ashby-jobs-scraper)**
