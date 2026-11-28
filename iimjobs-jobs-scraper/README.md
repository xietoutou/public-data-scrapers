# IIMJobs Jobs Scraper

Get job listings from [IIMJobs.com](https://www.iimjobs.com), India's job board for MBA graduates and mid to senior professionals: banking and finance, CA and CFA, consulting, sales and marketing, HR, operations, legal and general management roles. You get one clean table with the full job description, salary in LPA when the employer shows it, skills, experience range, cities and the company's AmbitionBox rating.

Recruiters, HR and talent analysts, job market researchers and job aggregators use it to track who is hiring, for which roles, in which cities and at what pay.

- **Search like on the site, or take the whole board.** Keywords, categories, cities, experience range and posting date. With no keywords you get every open job in the chosen categories (about 24,000 on the whole board).
- **Full details.** Description as plain text (HTML optional), skills, industries, salary in lakhs per year, AmbitionBox rating and review count, recruiter designation, diversity hiring tags and the apply link.
- **Daily feed of new jobs.** Turn on **Only new jobs since the last run** and schedule the Actor; each run saves only jobs it has not saved before.
- **Contacts written in the job text.** Emails and phone numbers that employers put into the public description are pulled out into their own columns.
- **No login, no API key, no proxy needed.**
- **Low price.** $1.20 per 1,000 jobs.

**Run it online, without code:** [IIMJobs Jobs Scraper - MBA, Finance & Management Jobs India](https://apify.com/pipiagent/iimjobs-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `iimjobs-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Example | Notes |
|---|---|---|
| `jobId`, `title`, `designation` | 1747818, Relationship Manager - Large Corporate Banking | |
| `company`, `companyLogo` | Dimensions HRD Consultants | The company or recruitment firm that posted the job. Empty for confidential jobs |
| `companyRating`, `companyReviewsCount`, `companyReviewsUrl` | 3.9, 29 | From AmbitionBox, when IIMJobs links the company to an AmbitionBox profile |
| `companyType`, `companyIndustry`, `companyEmployeesIndia` | Foreign MNC, Financial Services, 50001-100000 | From the same AmbitionBox profile |
| `category`, `industries`, `skills` | Banking & Finance, [Banking / Financial Services], [Corporate Banking, Trade Finance] | |
| `locations`, `isRemote` | [Bangalore, Mumbai], false | Every city the job is open in |
| `experienceMin`, `experienceMax` | 12, 18 | Years |
| `salaryMin`, `salaryMax`, `salaryText`, `salaryDisclosed` | 25, 30, "25-30 LPA", true | Lakhs of rupees per year (LPA). Only when the employer shows the salary |
| `isPremium`, `diversityHiring` | false, [Women] | Diversity tags such as women, women returning to work, persons with disabilities, ex-defence |
| `recruiterDesignation` | Managing Partner | The poster's job title, as shown on the job page |
| `postedAt` | 2026-11-25T05:59:33Z | ISO 8601 UTC |
| `description`, `descriptionHtml` | | Plain text by default, HTML optional |
| `contactEmails`, `contactPhones` | [hr@example.com], [+91XXXXXXXXXX] | Only contacts written in the public job text, see below |
| `searchKeyword` | investment banking | The keyword that found the job |
| `jobUrl`, `applyUrl`, `externalApply` | | `applyUrl` is the company's own application page when the job sends you there, otherwise the IIMJobs page |

Fields that a job does not have are `null` or an empty list, so every record has the same columns.

## Input examples

Investment banking jobs in Mumbai, best matches first:

```json
{
    "keywords": ["investment banking"],
    "locations": ["Mumbai"],
    "maxItems": 100
}
```

Daily feed of new finance and consulting jobs for 5 to 10 years of experience:

```json
{
    "categories": ["bankingFinance", "consultingGeneralManagement"],
    "experienceMin": 5,
    "experienceMax": 10,
    "postedWithinDays": 2,
    "onlyNew": true
}
```

Product manager jobs, newest first, keeping only jobs whose title, designation or skills contain both "product" and "manager" (the two words do not have to be next to each other, so a few jobs such as "Product Marketing Manager" stay in):

```json
{
    "keywords": ["product manager"],
    "matchAllWords": true,
    "sortBy": "newest",
    "maxItems": 200
}
```

The whole board without descriptions (fast). Set **Max results**: with no filters and no limit at all, the Actor only saves an example of the 50 newest jobs.

```json
{
    "includeDescription": false,
    "maxItems": 30000
}
```

Category values: `bankingFinance`, `salesMarketing`, `itSystems`, `consultingGeneralManagement`, `hrIr`, `scmOperations`, `legal`, `bpo`, `genAi`.

## Output example

```json
{
    "jobId": 1747818,
    "title": "Relationship Manager/Senior Relationship Manager - Large Corporate Banking",
    "designation": "Relationship Manager/Senior Relationship Manager - Large Corporate Banking",
    "company": "Dimensions HRD Consultants",
    "companyRating": 3.9,
    "companyReviewsCount": 29,
    "companyType": null,
    "companyIndustry": "Recruitment",
    "companyEmployeesIndia": "51-200",
    "companyReviewsUrl": "https://www.ambitionbox.com/reviews/dimensions-hrd-consultants-reviews",
    "companyLogo": "https://recruiter-static-content.s3.ap-south-1.amazonaws.com/CompanyLogos/centralised-25570.webp",
    "category": "Banking & Finance",
    "searchKeyword": "investment banking",
    "industries": ["Banking / Financial Services / Broking"],
    "skills": ["Corporate Banking", "Banking", "BFSI Sales", "Credit Analysis", "Financial Analysis", "Trade Finance", "Corporate Sales", "Client Relationships"],
    "locations": ["Bangalore", "Delhi NCR", "Mumbai"],
    "isRemote": false,
    "experienceMin": 12,
    "experienceMax": 18,
    "salaryMin": null,
    "salaryMax": null,
    "salaryText": null,
    "salaryDisclosed": false,
    "isPremium": false,
    "diversityHiring": [],
    "recruiterDesignation": "Managing Partner",
    "postedAt": "2026-11-25T05:59:33Z",
    "description": "Key Responsibilities:\n- Develop, acquire and manage relationships with large corporate clients across various sectors.\n- Drive business growth through new client acquisition, portfolio expansion and deepening existing client relationships...",
    "contactEmails": [],
    "contactPhones": [],
    "externalApply": false,
    "jobUrl": "https://www.iimjobs.com/j/relationship-managersenior-relationship-manager-large-corporate-banking-1747818",
    "applyUrl": "https://www.iimjobs.com/j/relationship-managersenior-relationship-manager-large-corporate-banking-1747818",
    "scrapedAt": "2026-11-25T20:33:32Z"
}
```

## How much does it cost?

You pay per saved job: **$1.20 per 1,000 jobs**. There is no start fee and no monthly rental. Filters are applied before saving, so you pay only for jobs that match. Descriptions, ratings and contacts are included at no extra charge.

| Run | Jobs | Cost |
|---|---|---|
| Daily feed of new jobs in two categories | about 100 | $0.12 |
| One keyword, all matching jobs | about 500 | $0.60 |
| The whole board | about 24,000 | $28.80 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Speed.** Listings are fast (about 6 minutes for the whole board without descriptions). Each description needs one more request, and the Actor reads about 2 jobs per second to stay polite to the site, so the whole board with descriptions takes about 3.5 hours (raise the run timeout in the run options, the default is one hour). In our test, all 542 Legal jobs with descriptions took 5 minutes. For a daily feed, use **Posted within (days)** and **Only new jobs**, which keeps runs to a few minutes.
- **Keyword search works like the IIMJobs search box.** It also returns jobs that match only some of the words, so "product manager" brings many "Account Manager" jobs. Turn on **Every keyword word must appear** to keep only exact matches. The search reaches back about three months; category listings without keywords include every open job (about five months).
- **Salaries are shown for only about 1 in 10 jobs.** Most employers hide them, and then the salary fields are empty.
- **Applicant counts, view counts and recruiter names are not included.** IIMJobs shows them only to logged-in users or in its app.
- **The AmbitionBox rating** is filled only when IIMJobs links the company to an AmbitionBox profile (about half of the jobs in our tests). Without keywords it also needs **Include full description** to be on. Many jobs are posted by recruitment firms, and then the rating is the firm's rating.
- **Cities are exact.** A job is found under the cities the employer picked. "Delhi NCR" also searches Delhi, Gurgaon, Noida, Greater Noida, Faridabad, Ghaziabad and Manesar. For Mumbai, add "Navi Mumbai" and "Thane" if you want them. **Remote only** reads the whole listing of each city to find remote jobs, so it is slower.
- **This is unofficial.** The Actor is not made by, endorsed by or connected to IIMJobs or AmbitionBox.

---

Full documentation, all input options and a free trial: **[IIMJobs Jobs Scraper on Apify](https://apify.com/pipiagent/iimjobs-jobs-scraper)**
