# Career Site Jobs Scraper

Get every open job straight from a company's own career site. Paste the job page of the companies you care about and get one clean list of jobs, whether the company uses Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable, Recruitee, Personio, Teamtailor or BambooHR. Use it for recruiting and sourcing, sales prospecting (a company that hires is a company that buys), competitor tracking, salary research, job boards and labour market research.

- **10 applicant tracking systems in one Actor.** Mix Greenhouse, Lever, Workday and the others in one run. The Actor recognises the system from the URL.
- **One format for all of them.** Title, department, location, country, remote or hybrid, employment type, salary range, posting date, apply link and description always have the same field names.
- **Fresh data from the source.** Jobs come from the official public job board of each company, the same place the company's careers page reads them from. No aggregator delay, no expired reposts.
- **Big employers work too.** Workday career sites show at most 2,000 jobs per search. The Actor splits large boards into smaller groups so you get all of them (tested with 2,683 NVIDIA jobs).
- **No login and no proxy needed.**
- **Low price.** $1.00 per 1,000 jobs.

**Run it online, without code:** [Career Site Jobs Scraper - Greenhouse, Lever, Ashby, Workday](https://apify.com/pipiagent/career-site-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `career-site-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

One result is one job posting.

| Field | Example | Notes |
|---|---|---|
| `company`, `companySlug`, `ats` | OpenAI, openai, Ashby | Company name as the job board shows it, or from the URL when the board has none |
| `jobId`, `requisitionId` | JR2028777 | The board's own job id and the internal requisition number when published |
| `title`, `department`, `team` | Research Engineer, Research | |
| `location`, `locations` | San Francisco | Primary location and the full list for multi-location jobs |
| `country`, `countryCode` | United States, US | From the job board, or worked out from the location text |
| `workplaceType`, `isRemote` | remote / hybrid / onsite | From the job board, or from the word "remote" or "hybrid" in the location or title |
| `employmentType`, `seniority` | Full-time, Mid-Senior level | Employment types are normalised to Full-time, Part-time, Contract, Temporary, Internship |
| `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`, `salaryText` | 212000, 295000, USD, year | Only when the company publishes pay |
| `postedAt`, `updatedAt` | 2026-10-28T04:39:11Z | ISO 8601, UTC |
| `jobUrl`, `applyUrl` | https://jobs.ashbyhq.com/openai/... | |
| `description`, `descriptionHtml` | About the Team... | Plain text by default, HTML optional |
| `careerPageUrl`, `scrapedAt` | | The input line the job came from, and when it was collected |

### Which fields does each system fill?

| System | Department | Country | Remote / hybrid | Salary | Posting date |
|---|---|---|---|---|---|
| Greenhouse | yes | from location text | sometimes | when published | yes |
| Lever | yes | yes | yes | when published | yes |
| Ashby | yes | yes | when set | when published | yes |
| Workday | no | yes | when set | no | yes (exact date with descriptions on, approximate without) |
| SmartRecruiters | yes | yes | yes | no | yes |
| Workable | yes | yes | remote only | no | yes |
| Recruitee | yes | yes | yes | when published | yes |
| Personio | yes | from location text | no | when published | yes |
| Teamtailor | yes | yes | yes | no | yes |
| BambooHR | yes | yes | yes | as text, when published | with descriptions on |

## Input examples

The 10 newest jobs at four companies on four different systems:

```json
{
    "careerPages": [
        "https://job-boards.greenhouse.io/airbnb",
        "https://jobs.lever.co/spotify",
        "https://jobs.ashbyhq.com/openai",
        "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite"
    ],
    "maxJobsPerCompany": 10
}
```

Engineering and product jobs in the US or remote, posted in the last 14 days, without interns:

```json
{
    "careerPages": [
        "https://boards.greenhouse.io/stripe",
        "https://jobs.ashbyhq.com/openai",
        "https://salesforce.wd12.myworkdayjobs.com/External_Career_Site"
    ],
    "titleKeywords": ["engineer", "product manager"],
    "excludeTitleKeywords": ["intern"],
    "locations": ["United States", "Remote"],
    "postedWithinDays": 14
}
```

Every remote sales job, without descriptions (fastest and smallest):

```json
{
    "careerPages": ["https://job-boards.greenhouse.io/gitlab", "https://jobs.lever.co/spotify"],
    "remoteOnly": true,
    "departments": ["sales"],
    "includeDescription": false
}
```

## Output example

A job from Ashby with a published salary:

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
    "locations": ["San Francisco"],
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
    "careerPageUrl": "https://jobs.ashbyhq.com/openai",
    "scrapedAt": "2026-10-28T11:47:32Z"
}
```

A job from Workday:

```json
{
    "company": "Nvidia",
    "companySlug": "nvidia/NVIDIAExternalCareerSite",
    "ats": "Workday",
    "jobId": "JR2028777",
    "title": "Senior Firmware Engineer",
    "location": "Israel, Tel Aviv",
    "locations": ["Israel, Tel Aviv"],
    "country": "Israel",
    "countryCode": "IL",
    "employmentType": "Full-time",
    "postedAt": "2026-10-28T00:00:00Z",
    "requisitionId": "JR2028777",
    "jobUrl": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/Israel-Tel-Aviv/Senior-Firmware-Engineer_JR2028777",
    "applyUrl": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/Israel-Tel-Aviv/Senior-Firmware-Engineer_JR2028777/apply",
    "description": "We are looking for an excellent Senior Firmware Engineer to join the Firmware team. ..."
}
```

Fields that a job board does not provide are `null`, so every record has the same columns.

## How much does it cost?

You pay per saved job: **$1.00 per 1,000 jobs**. There is no start fee and no monthly rental. Filters run before jobs are saved, so you only pay for jobs that match.

| Run | Jobs | Cost |
|---|---|---|
| 10 newest jobs at 4 companies | 40 | $0.04 |
| All jobs at a mid-size company | 300 | $0.30 |
| All 2,683 NVIDIA jobs | 2,683 | $2.68 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **You choose the companies.** This Actor reads the job boards you give it. It does not search all companies on the internet. To track a market, build a list of company job pages once and run it on a schedule.
- **Big boards take minutes, not seconds.** Small and mid-size boards finish in a few seconds. In our tests all 2,683 NVIDIA jobs on Workday took about 3 minutes without descriptions and about 11 minutes with descriptions, and a Lever board with 4,100 jobs took about 5 minutes, because these job boards answer slowly for large lists. Workday needs one extra request per job for the description, the exact posting date, the country and the workplace type, so turn off **Include job description** when you only need the list. Without descriptions, Workday jobs have only an approximate posting date ("posted 3 days ago"). SmartRecruiters and BambooHR also need one extra request per job for descriptions.
- **Do not run many copies against the same Workday site at once.** Workday slows down when it gets many requests from parallel runs. One run per company is fastest.
- **Workday boards over 2,000 jobs.** Workday shows at most 2,000 jobs per search. The Actor splits the list by job category or location to get the rest. A job that has no category at all can be missed in that case.
- **Company name.** Lever, BambooHR and Workday do not publish a clean company name, so it is built from the URL (for example "Nvidia" from `nvidia.wd5.myworkdayjobs.com`). Personio shows the legal entity (for example "tado GmbH").
- **Country and remote flag are sometimes worked out from text.** When a job board gives only a location like "San Francisco, CA" or "Remote - Germany", the country and remote flag are derived from that text. This is right in most cases but not always, for example "Remote - EMEA" has no single country and stays empty.
- **Salary only when published.** Many companies do not publish pay. Greenhouse pay ranges do not say per year or per hour, so ranges below 500 are marked as hourly and the rest as yearly.
- **Posted within (days) skips jobs without a date.** BambooHR dates need descriptions turned on; the Actor loads them automatically when you use this filter.
- **Careers page detection is best effort.** It works when the company's page links to or embeds a supported job board in its HTML (Figma, Notion, Linear and Cursor worked in our tests). Pages that load jobs only with JavaScript, or that block automated visits, are not detected. Paste the job board URL in that case.
- **SmartRecruiters company ids.** SmartRecruiters returns an empty list instead of an error for a company id that does not exist, so a typo looks like "no open jobs". Check the id in the URL of the company's SmartRecruiters page.
- **Other systems.** iCIMS, Taleo, SuccessFactors, Jobvite and custom-built career sites are not supported.

---

Full documentation, all input options and a free trial: **[Career Site Jobs Scraper on Apify](https://apify.com/pipiagent/career-site-jobs-scraper)**
