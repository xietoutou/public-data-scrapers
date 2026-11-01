# Workday Jobs Scraper

Get every open job from companies whose career site runs on [Workday](https://www.workday.com) (`myworkdayjobs.com`), which many large employers use, such as NVIDIA and Salesforce. Add the career sites you care about and get one clean table of their jobs. Use it for recruiting and sourcing, sales prospecting (a company that hires is a company that buys), competitor tracking and labour market research.

- **Big employers, all jobs.** Workday shows at most 2,000 jobs per search; the Actor splits large sites so you get every job (tested with 2,683 NVIDIA jobs).
- **Fresh data from the source.** The same job list the company's careers site shows. No aggregator delay, no expired reposts.
- **Fast list mode.** Turn descriptions off to get titles, locations and links for thousands of jobs in a few minutes.
- **Filters before you pay.** Job title keywords, locations, remote only, department and posted within the last N days. You are charged only for jobs that match.
- **No login, no API key and no proxy needed.**
- **Low price.** $1.00 per 1,000 jobs.

**Run it online, without code:** [Workday Jobs Scraper - All Jobs from myworkdayjobs.com Sites](https://apify.com/pipiagent/workday-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `workday-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

One result is one job posting, with the same fields for every company:

| Field | Example | Notes |
|---|---|---|
| `company`, `companySlug` | Salesforce, salesforce/External_Career_Site | |
| `jobId`, `requisitionId` | JR360125 | |
| `title`, `department`, `team` | Director, Finance Data Strategy & Stewardship | |
| `location`, `locations` | Canada - Toronto | Primary location and the full list for multi-location jobs |
| `country`, `countryCode` | Canada, CA | From Workday (needs descriptions on) |
| `workplaceType`, `isRemote` | remote / hybrid / onsite | When the company sets it (needs descriptions on) |
| `employmentType`, `seniority` | Full-time | Normalised to Full-time, Part-time, Contract, Temporary, Internship |
| `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`, `salaryText` | | Workday does not publish structured pay; look in the description |
| `postedAt`, `updatedAt` | 2026-10-28T00:00:00Z | Exact date with descriptions on, approximate ("posted 3 days ago") without |
| `jobUrl`, `applyUrl` | | |
| `description`, `descriptionHtml` | | Plain text by default, HTML optional |
| `careerPageUrl`, `scrapedAt` | | The input line the job came from, and when it was collected |

Fields that Workday does not provide for a job are `null`, so every record has the same columns.

## Input examples

The 10 newest jobs at each company:

```json
{
    "careerPages": [
        "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite",
        "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site"
    ],
    "maxJobsPerCompany": 10
}
```

Engineering and product jobs in the US or remote, posted in the last 14 days, without interns:

```json
{
    "careerPages": [
        "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite",
        "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site"
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
    "company": "Salesforce",
    "companySlug": "salesforce/External_Career_Site",
    "ats": "Workday",
    "jobId": "JR360125",
    "title": "Director, Finance Data Strategy & Stewardship",
    "department": null,
    "team": null,
    "location": "Canada - Toronto",
    "locations": [
        "Canada - Toronto"
    ],
    "country": "Canada",
    "countryCode": "CA",
    "workplaceType": "onsite",
    "isRemote": false,
    "employmentType": "Full-time",
    "seniority": null,
    "salaryMin": null,
    "salaryMax": null,
    "salaryCurrency": null,
    "salaryPeriod": null,
    "salaryText": null,
    "postedAt": "2026-10-28T00:00:00Z",
    "updatedAt": null,
    "requisitionId": "JR360125",
    "jobUrl": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Canada---Toronto/Director--Finance-Data-Strategy---Stewardship_JR360125",
    "applyUrl": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site/job/Canada---Toronto/Director--Finance-Data-Strategy---Stewardship_JR360125/apply",
    "description": "To get the best candidate experience, please consider applying for a maximum of 3 roles within 12 months ...",
    "careerPageUrl": "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site",
    "scrapedAt": "2026-10-28T17:40:38Z"
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

- **You choose the companies.** This Actor reads the Workday job boards you give it. It does not search every company on Workday. To track a market, build a list of companies once and run it on a schedule.
- **Descriptions cost time on Workday.** Workday needs one extra request per job for the description, the exact posting date, the country and the workplace type. In our tests all 2,683 NVIDIA jobs took about 3 minutes without descriptions and about 11 minutes with them. Turn off **Include job description** when you only need the list.
- **Sites over 2,000 jobs.** Workday shows at most 2,000 jobs per search. The Actor splits the list by job category or location to get the rest. A job with no category at all can be missed in that case.
- **Do not run many copies against the same Workday site at once.** Workday slows down when it gets many parallel requests. One run per company is fastest.
- **No department or salary fields.** Workday's public job list does not include them.
- **Company name comes from the URL**, for example "Nvidia" from `nvidia.wd5.myworkdayjobs.com`.
- **Only Workday.** Job boards on other systems are skipped with a warning. Use [Career Site Jobs Scraper](https://apify.com/pipiagent/career-site-jobs-scraper) for a mixed list.

---

Full documentation, all input options and a free trial: **[Workday Jobs Scraper on Apify](https://apify.com/pipiagent/workday-jobs-scraper)**
