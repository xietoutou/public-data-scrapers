# Hirist Jobs Scraper

Get job listings from [Hirist.tech](https://www.hirist.tech), India's job board for IT and tech roles: backend, frontend, full stack, mobile, AI/ML, data engineering, analytics, DevOps, cybersecurity, QA, SAP/Oracle, semiconductor, product management and design. You get one clean table with the full job description, salary in LPA when the employer shows it, skills, experience range, cities and the company's AmbitionBox rating.

Tech recruiters, staffing agencies, HR and talent analysts, job market researchers and job aggregators use it to track who is hiring developers and engineers in India, for which skills, in which cities and at what pay.

- **Search like on the site, or take the whole board.** Keywords, 17 categories, cities, experience range and posting date. With no keywords you get every open job in the chosen categories (about 26,700 on the whole board).
- **Full details.** Description as plain text (HTML optional), skills, salary in lakhs per year, AmbitionBox rating, review count, company type and size, recruiter designation, diversity hiring tags and the apply link.
- **Daily feed of new jobs.** Turn on **Only new jobs since the last run** and schedule the Actor; each run saves only jobs it has not saved before.
- **No login, no API key, no proxy needed.**
- **Low price.** $1.80 per 1,000 jobs.

**Run it online, without code:** [Hirist Jobs Scraper - IT & Tech Jobs India (hirist.tech)](https://apify.com/pipiagent/hirist-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `hirist-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Example | Notes |
|---|---|---|
| `jobId`, `title`, `designation` | 1685563, Qualitest - Python Developer - Gen AI, Python Developer | |
| `company`, `companyLogo` | Qualitest | The company or recruitment firm that posted the job. Empty for confidential jobs (Hirist shows "Verified Company" for them) |
| `companyRating`, `companyReviewsCount`, `companyReviewsUrl` | 3.6, 877 | From AmbitionBox, when Hirist links the company to an AmbitionBox profile |
| `companyType`, `companyIndustry`, `companyEmployeesIndia` | Corporate, IT Services & Consulting, 1001-5000 | From the same AmbitionBox profile |
| `category`, `skills` | AI/ML, [Python, FastAPI, Django, SQL] | |
| `locations`, `isRemote` | [Hyderabad, Bangalore, Pune], false | Every city the job is open in |
| `experienceMin`, `experienceMax` | 10, 15 | Years |
| `salaryMin`, `salaryMax`, `salaryText`, `salaryDisclosed` | 50, 55, "50-55 LPA", true | Lakhs of rupees per year (LPA). Only when the employer shows the salary |
| `isPremium`, `diversityHiring` | true, [Women] | Diversity tags such as women, women returning to work, persons with disabilities, ex-defence |
| `recruiterDesignation` | Lead HR | The poster's job title, as shown on the job page |
| `postedAt` | 2026-11-24T10:01:48Z | ISO 8601 UTC |
| `description`, `descriptionHtml` | | Plain text by default, HTML optional |
| `contactEmails`, `contactPhones` | [hr@example.com], [+91XXXXXXXXXX] | Only contacts written in the public job text. On Hirist these are almost always empty, see below |
| `searchKeyword` | python | The keyword that found the job |
| `jobUrl`, `applyUrl`, `externalApply` | | `applyUrl` is the company's own application page when the job sends you there, otherwise the Hirist page |

Fields that a job does not have are `null` or an empty list, so every record has the same columns.

## Input examples

Python jobs in Bengaluru, best matches first:

```json
{
    "keywords": ["python"],
    "locations": ["Bengaluru"],
    "maxItems": 100
}
```

Daily feed of new DevOps and cybersecurity jobs for 3 to 6 years of experience:

```json
{
    "categories": ["devopsSre", "cybersecurity"],
    "experienceMin": 3,
    "experienceMax": 6,
    "postedWithinDays": 2,
    "onlyNew": true
}
```

React Native jobs, newest first, keeping only jobs whose title, designation or skills contain both "react" and "native". The search alone also returns jobs such as "Senior React Developer" or "Cloud Native Architect". With this switch on, both words must appear, but they do not have to be next to each other, so, for example, a job titled "React Developer" with the skill "Cloud Native" would stay in:

```json
{
    "keywords": ["react native"],
    "matchAllWords": true,
    "sortBy": "newest",
    "maxItems": 200
}
```

The whole board without descriptions (fast). Always set **Max results** for this: an input with no search filters and no **Max results** (for example only `{"includeDescription": false}`) is treated as a test run and saves only an example of the 50 newest jobs.

```json
{
    "includeDescription": false,
    "maxItems": 30000
}
```

Category values: `backendDevelopment`, `frontendDevelopment`, `fullStack`, `mobileApplications`, `aiMl`, `dataEngineering`, `dataAnalyticsBi`, `devopsSre`, `cybersecurity`, `qualityAssurance`, `platformEngineeringSapOracle`, `semiconductorVlsiEda`, `emergingTechnologies`, `uiDesign`, `productManagement`, `businessAnalysisProjectManagement`, `others`.

## Output example

```json
{
    "jobId": 1685563,
    "title": "Qualitest - Python Developer - Gen AI",
    "designation": "Python Developer",
    "company": "Qualitest",
    "companyRating": 3.6,
    "companyReviewsCount": 877,
    "companyType": "Corporate",
    "companyIndustry": "IT Services & Consulting",
    "companyEmployeesIndia": "1001-5000",
    "companyReviewsUrl": "https://www.ambitionbox.com/reviews/qualitest-reviews",
    "companyLogo": "https://recruiter-static-content.s3.ap-south-1.amazonaws.com/CompanyLogos/centralised-4388.webp",
    "category": "AI/ML",
    "searchKeyword": "python",
    "skills": ["Artificial Intelligence", "Python", "Generative AI", "FastAPI", "Django", "Flask", "RESTful API", "SQL", "Google Cloud Platform", "Vertex AI", "Prompt Engineering"],
    "locations": ["Hyderabad", "Bangalore", "Chennai", "Noida", "Coimbatore", "Pune", "Tamil Nadu"],
    "isRemote": false,
    "experienceMin": 10,
    "experienceMax": 15,
    "salaryMin": 50,
    "salaryMax": 55,
    "salaryText": "50-55 LPA",
    "salaryDisclosed": true,
    "isPremium": true,
    "diversityHiring": [],
    "recruiterDesignation": null,
    "postedAt": "2026-11-24T10:01:48Z",
    "description": "Hiring: Python Developer Gen AI Engineer\n\nTotal Experience: 10 to 15 years\n\nLocation: Bangalore, Chennai, Hyderabad, Noida, Coimbatore, Pune\n\nEmployment Type: Full-time\n\nMandatory Technical Skills:\n- Python Development: Minimum 6 years of experience.\n- REST API Development: Minimum 6 years of experience...",
    "contactEmails": [],
    "contactPhones": [],
    "externalApply": false,
    "jobUrl": "https://www.hirist.tech/j/qualitest-python-developer-gen-ai-1685563",
    "applyUrl": "https://www.hirist.tech/j/qualitest-python-developer-gen-ai-1685563",
    "scrapedAt": "2026-11-25T22:13:14Z"
}
```

## How much does it cost?

You pay per saved job: **$1.80 per 1,000 jobs**. There is no start fee and no monthly rental. Filters are applied before saving, so you pay only for jobs that match. Descriptions and ratings are included at no extra charge.

| Run | Jobs | Cost |
|---|---|---|
| Daily feed of new jobs in two categories | about 100 | $0.18 |
| One keyword, all matching jobs | about 700 | $1.26 |
| The whole board | about 26,700 | $48.06 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Speed.** Listings are fast (about 5 to 8 minutes for the whole board without descriptions, about 540 pages of 50). Each description needs one more request, and the Actor reads about 2 jobs per second to stay polite to the site, so the whole board with descriptions takes about 4 hours (raise the run timeout in the run options, the default is one hour). In our test, 400 jobs with descriptions took about 4.5 minutes. For a daily feed, use **Posted within (days)** and **Only new jobs**, which keeps runs to a few minutes.
- **Keyword search works like the Hirist search box.** For multi-word keywords it also returns jobs that match only some of the words: "react native" brings "Senior React Developer" and "Cloud Native Architect" jobs, "sap abap" brings other SAP consultant jobs. Turn on **Every keyword word must appear** to keep only jobs that contain every word (in any order, not as an exact phrase).
- **Salaries are shown for fewer than 1 in 10 jobs** (about 7% of the whole board). Most employers hide them, and then the salary fields are empty.
- **Applicant counts, view counts and recruiter names are not included.** Hirist shows them only to logged-in users or in its app.
- **No industry field.** Hirist does not fill in industries for its jobs, so the Actor has none. Use `companyIndustry` from AmbitionBox instead.
- **The AmbitionBox rating** is filled only when Hirist links the company to an AmbitionBox profile (about 6 in 10 jobs in our tests). Many jobs are posted by recruitment firms, and then the rating is the firm's rating.
- **Cities are exact.** A job is found under the cities the employer picked. "Delhi NCR" also searches Delhi, Gurgaon, Noida, Greater Noida, Faridabad, Ghaziabad and Manesar. For Mumbai, add "Navi Mumbai" and "Thane" if you want them. About 1 in 10 jobs is listed as "Anywhere in India/Multiple Locations"; add that as a city to include them. **Remote only** reads the whole listing of each city to find remote jobs, so it is slower.
- **A few jobs appear twice in the site's listings.** The Actor removes the duplicates, so you get fewer rows than the job counts Hirist shows (about 1% fewer).
- **This is unofficial.** The Actor is not made by, endorsed by or connected to Hirist, IIMJobs or AmbitionBox.

---

Full documentation, all input options and a free trial: **[Hirist Jobs Scraper on Apify](https://apify.com/pipiagent/hirist-jobs-scraper)**
