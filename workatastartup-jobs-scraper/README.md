# Work at a Startup Jobs Scraper

Collect open jobs at Y Combinator startups from the public YC jobs board ([ycombinator.com/jobs](https://www.ycombinator.com/jobs)) and Work at a Startup ([workatastartup.com](https://www.workatastartup.com/jobs)). Each result is one job with the title, company, YC batch, location, salary, equity, experience, visa policy and the full job description. Recruiters, job seekers, sales teams and researchers use it to track who is hiring at YC companies, compare salaries and build lead lists of funded startups.

- **One row per job, ready for a spreadsheet.** Salary is split into minimum, maximum, currency and period. Equity is split into minimum and maximum percent.
- **Company facts on every row.** YC batch, one-liner, website, team size, founding year, location, tags and LinkedIn page.
- **Full description.** The job description and the interview process (when the company wrote one), as plain text and HTML.
- **Useful filters.** Role, keyword, location, remote, job type, YC batch, years of experience, visa sponsorship, salary shown and posting age.
- **No login and no proxy needed.** It reads only pages that anyone can open without an account.
- **Low price.** $0.60 per 1,000 jobs.

This Actor is not made by, affiliated with or endorsed by Y Combinator.

**Run it online, without code:** [Work at a Startup Jobs Scraper - Y Combinator Startup Jobs](https://apify.com/pipiagent/workatastartup-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `workatastartup-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Group | Fields |
|---|---|
| Job | `title`, `jobId`, `employmentType` (Full-time, Internship, Contract), `role` (Engineering, Sales and so on), `roleType` (Backend, Full stack and so on), `skills` |
| Place | `location`, `isRemote` |
| Pay | `salaryText`, `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`, `equityText`, `equityMinPercent`, `equityMaxPercent` |
| Requirements | `minExperience`, `minExperienceYears`, `minSchoolYear` (internships), `visa` |
| Dates | `postedAgo` (as the site shows it, for example "5 months"), `postedDateApprox`, `lastActiveAgo` |
| Links | `jobUrl`, `workAtAStartupUrl`, `applyUrl`, `companyUrl`, `companyWebsite`, `companyLinkedinUrl`, `companyLogoUrl` |
| Company | `companyName`, `companySlug`, `companyBatch`, `companyOneLiner`, `companyDescription`, `companyTeamSize`, `companyFoundedYear`, `companyLocation`, `companyCountry`, `companyTags`, `companyStatus` |
| Description | `description`, `descriptionHtml`, `interviewProcess` (only with **Include full description** on) |

## Input examples

Design jobs at any YC startup:

```json
{
    "roles": ["design"],
    "maxItems": 100
}
```

Remote Python jobs:

```json
{
    "keywords": ["python"],
    "remote": "remoteOnly",
    "maxItems": 50
}
```

Internships that sponsor visas:

```json
{
    "jobTypes": ["internship"],
    "visaSponsorshipOnly": true,
    "maxItems": 50
}
```

Jobs at companies from one YC batch in San Francisco:

```json
{
    "batches": ["W25"],
    "locations": ["San Francisco"],
    "maxItems": 50
}
```

Every open job of specific companies (slugs or URLs):

```json
{
    "companies": ["https://www.ycombinator.com/companies/omnistrate", "whatnot"],
    "maxItems": 500
}
```

## Output example

A real result from a test run (the description is shortened here):

```json
{
    "jobId": 97146,
    "title": "Product Engineer",
    "companyName": "Just Appraised",
    "companySlug": "just-appraised",
    "companyBatch": "S17",
    "companyOneLiner": "Just Appraised makes software for local governments.",
    "location": "US / CA / Remote (US; CA)",
    "isRemote": true,
    "employmentType": "Full-time",
    "role": "Engineering",
    "roleCode": "eng",
    "roleType": "Full stack",
    "salaryText": "$130K - $160K",
    "salaryMin": 130000,
    "salaryMax": 160000,
    "salaryCurrency": "USD",
    "salaryPeriod": "year",
    "equityText": null,
    "equityMinPercent": null,
    "equityMaxPercent": null,
    "minExperience": "3+ years",
    "minExperienceYears": 3,
    "minSchoolYear": null,
    "visa": "US citizen/visa only",
    "skills": [],
    "postedAgo": "5 months",
    "postedDateApprox": "2026-06-27",
    "lastActiveAgo": "about 1 month",
    "jobUrl": "https://www.ycombinator.com/companies/just-appraised/jobs/ZZs78Wb-product-engineer",
    "workAtAStartupUrl": "https://www.workatastartup.com/jobs/97146",
    "applyUrl": "https://account.ycombinator.com/authenticate?continue=https%3A%2F%2Fwww.workatastartup.com%2Fapplication%3Fsignup_job_id%3D97146&defaults%5BsignUpActive%5D=true&defaults%5Bwaas_company%5D=1693",
    "companyUrl": "https://www.ycombinator.com/companies/just-appraised",
    "companyWebsite": "https://www.justappraised.com",
    "companyDescription": "Our goal is to empower local government employees with the tools, technology, and support they need ...",
    "companyTeamSize": 40,
    "companyFoundedYear": 2017,
    "companyLocation": "San Francisco",
    "companyCountry": "US",
    "companyTags": ["SaaS", "GovTech"],
    "companyStatus": "Active",
    "companyLinkedinUrl": null,
    "companyLogoUrl": null,
    "description": "About Just Appraised\n\nAt Just Appraised, we’re modernizing the infrastructure behind local government. ...",
    "descriptionHtml": "<h2><strong>About Just Appraised</strong></h2>\n<p>At ...",
    "interviewProcess": null,
    "scrapedAt": "2026-11-27T00:56:23Z"
}
```

A job from another test run, with visa sponsorship and skills:

```json
{
    "title": "Forward Deployed Data Engineer",
    "companyName": "Vori",
    "companyBatch": "W20",
    "location": "San Francisco, CA, US",
    "salaryText": "$150K - $180K",
    "visa": "Will sponsor",
    "skills": ["PostgreSQL", "Python", "SQL", "Data Warehousing", "ETL", "Data Analytics"],
    "postedAgo": "over 1 year"
}
```

## How much does it cost?

You pay per saved job: **$0.60 per 1,000 results**. There is no start fee and no monthly rental. Turning on **Include full description** does not change the price.

| Run | Results | Cost |
|---|---|---|
| Default run | 50 | $0.03 |
| One role in one city | 500 | $0.30 |
| A large export | 5,000 | $3.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **ycombinator.com limits how fast pages can be loaded.** In our tests it allowed about 80 page loads in a row and then answered "too many requests" (HTTP 429). After that, about 13 page loads a minute went through. The Actor slows down by itself when this happens, so it never hammers the site, but it means large runs are slow.
- **Narrow filters take longer.** Filters are checked after a company's jobs are loaded, so a rare combination has to look through many companies. Measured on Apify: the default run (50 jobs with descriptions) took 47 seconds, 20 design jobs took 36 seconds, 10 remote Python jobs took 53 seconds, and 5 jobs at W25 companies in San Francisco took 171 seconds. Filters by location, remote, job type, batch, experience, visa and salary are pre-checked on a lighter page, which makes them faster.
- **Finance and Legal roles are slow to find.** The other roles have their own listing page on ycombinator.com that points the Actor to the right companies first. Finance and Legal do not, so the Actor checks one company after another at the rate above. At that rate, checking all of the roughly 1,700 hiring companies this way would take more than an hour.
- **Posting dates are approximate.** The site shows the age of a job in words ("6 days", "about 1 month", "over 1 year"). `postedAgo` keeps those words and `postedDateApprox` turns them into a date, which can be off by weeks or months for older jobs. **Posted within (days)** uses the same wording.
- **Not every job shows every field.** In a test of 100 jobs, 93 showed a salary, 14 showed equity, 41 listed skills and 17 described the interview process.
- **Applying needs a YC account.** `applyUrl` leads to Y Combinator's sign-in page. The Actor does not log in and does not apply for you.
- **No founder contact details.** The Actor does not collect founders' emails or phone numbers, or anything that is only visible after login. Job descriptions are saved as the company wrote them, so a description can contain contact details that the company chose to publish.
- **Coverage.** The list of hiring companies comes from YC's public jobs sitemap and listing pages. On 2026-11-27 the sitemap listed 7,108 job pages at 1,728 companies. A company that has only just posted its first job may not be in the sitemap yet.
- **Location matching is by words.** "US" matches "San Francisco, CA, US" but not "Austin". A job counts as remote when its location says "Remote".
- **One-liners can be cut short.** The site shortens some `companyOneLiner` values and ends them with "…". `companyDescription` holds the full text.

---

Full documentation, all input options and a free trial: **[Work at a Startup Jobs Scraper on Apify](https://apify.com/pipiagent/workatastartup-jobs-scraper)**
