# Remote Jobs Scraper

Get remote job listings from four remote job boards in one run: [Remote OK](https://remoteok.com), [We Work Remotely](https://weworkremotely.com), [Jobicy](https://jobicy.com) and [Working Nomads](https://www.workingnomads.com). You get one clean table, newest first, with the same columns for every board and duplicates removed.

Use it for job alerts and job search, remote job newsletters and communities, recruiting and sourcing, sales prospecting (companies that hire remotely), salary research and labour market analysis.

- **Four boards, one format.** Title, company, category, tags, job type, seniority, location, salary, posting date, expiry date and links, plus the description as plain text.
- **About 2,000 open jobs** in a full run, collected in about 20 seconds.
- **Filters before you pay.** Keywords, excluded words, locations, worldwide only, posted within the last N days and salary only. You are charged only for jobs that match.
- **Duplicates removed.** A job posted on two boards is saved once.
- **No login, no API key, no proxy.** The Actor reads the public feeds that the boards publish for reuse.
- **Low price.** $1.00 per 1,000 jobs.

**Run it online, without code:** [Remote Jobs Scraper - Remote OK, We Work Remotely, Jobicy](https://apify.com/pipiagent/remote-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `remote-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Example | Notes |
|---|---|---|
| `source`, `sourceJobId` | Jobicy, 158365 | The job board the listing comes from |
| `title`, `company` | Senior Product Manager, GitLab | |
| `category`, `tags` | Product & Operations | Category names and tags as each board writes them |
| `employmentType`, `seniority` | Full-Time, Senior | When the board provides them |
| `location`, `isWorldwide` | UK, USA / false | Where applicants may live. `isWorldwide` is true for "Worldwide", "Anywhere" or "Global", and empty when the board gives no location |
| `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod` | 139200, 235200, USD, year | Only when the listing states a salary |
| `postedAt`, `expiresAt` | 2026-11-01T08:54:49Z | ISO 8601 UTC |
| `jobUrl`, `applyUrl` | | Link to the listing on the job board |
| `companyLogo`, `companyUrl`, `companyHeadquarters` | | When the board provides them |
| `description`, `descriptionHtml` | | Plain text by default, HTML optional |

Fields that a board does not provide are `null`, so every record has the same columns.

## Input examples

Python and data engineering jobs open worldwide, posted in the last 7 days:

```json
{
    "keywords": ["python", "data engineer"],
    "worldwideOnly": true,
    "postedWithinDays": 7
}
```

Customer support jobs for Europe, without team lead roles:

```json
{
    "keywords": ["customer support", "customer success"],
    "excludeKeywords": ["lead", "manager"],
    "locations": ["Europe", "EMEA", "Worldwide"]
}
```

All jobs with a salary, from We Work Remotely and Jobicy only:

```json
{
    "sources": ["weworkremotely", "jobicy"],
    "withSalaryOnly": true,
    "maxItems": 1000
}
```

## Output example

```json
{
    "source": "Jobicy",
    "sourceJobId": "158365",
    "title": "Senior Product Manager, Billing Engine & Platforms Monetization",
    "company": "GitLab",
    "category": "Product & Operations",
    "tags": null,
    "employmentType": "Full-Time",
    "seniority": "Senior",
    "location": "UK, USA",
    "isWorldwide": false,
    "salaryMin": 139200,
    "salaryMax": 235200,
    "salaryCurrency": "USD",
    "salaryPeriod": "year",
    "postedAt": "2026-11-01T08:54:49Z",
    "expiresAt": null,
    "jobUrl": "https://jobicy.com/jobs/158365-senior-product-manager-billing-engine-platforms-monetization",
    "applyUrl": "https://jobicy.com/jobs/158365-senior-product-manager-billing-engine-platforms-monetization",
    "companyLogo": "https://jobicy.com/data/server-nyc0409/galaxy/mercury/2020/12/WRILS-201207055737-109952.jpg",
    "companyUrl": null,
    "companyHeadquarters": null,
    "description": "GitLab is the intelligent orchestration platform for DevSecOps. GitLab enables organizations to increase developer productivity, improve operational efficiency...",
    "scrapedAt": "2026-11-01T17:22:18Z"
}
```

## How much does it cost?

You pay per saved job: **$1.00 per 1,000 jobs**. There is no start fee and no monthly rental. Filters are applied before saving, so you pay only for jobs that match.

| Run | Jobs | Cost |
|---|---|---|
| Daily check for new Python jobs | about 20 | $0.02 |
| All jobs posted in the last 7 days | about 1,500 | $1.50 |
| Everything the four boards show | about 2,000 | $2.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **The boards show recent jobs only.** Remote OK shows its latest 100 jobs, We Work Remotely its latest jobs per category (about 500 in total), Jobicy the last 7 days and Working Nomads its latest few dozen. Run the Actor daily to build a full history.
- **Locations are free text.** Each board writes them its own way ("USA Only", "Anywhere in the World", "EMEA, LATAM", "CET (+/- 3 hours)"), so add several words to **Locations**. Remote OK often gives no location; those jobs are skipped by location filters.
- **Salaries are listed only when the employer states them**, mostly on Jobicy and Remote OK.
- **Credit the source.** The boards share these feeds on the condition that listings link back to them and name them as the source. Every record has `source` and `jobUrl` for that; keep them if you publish the jobs.
- **This is unofficial.** The Actor is not made by, endorsed by or connected to any of the job boards.

---

Full documentation, all input options and a free trial: **[Remote Jobs Scraper on Apify](https://apify.com/pipiagent/remote-jobs-scraper)**
