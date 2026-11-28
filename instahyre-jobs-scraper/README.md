# Instahyre Jobs Scraper

Get job listings from [Instahyre.com](https://www.instahyre.com), an Indian hiring platform for software engineering, data, product, sales, operations, finance and other corporate roles. You get one clean table with the full job description, skills, experience range in years, job category and functions, cities, internship stipend, and a profile of the hiring company (tagline, founding year, size, short description).

Recruiters, staffing agencies, HR and talent analysts, job aggregators and sales teams use it to see who is hiring, for which roles, in which cities, and whether a job was posted by the company itself or by a recruitment firm.

- **Search like on the site, or take the whole board.** Skills or job titles, cities, job functions, industries, companies, company size, years of experience, experience level and job type. With no keywords you get every job that matches the filters (about 46,600 on the whole board in November 2026).
- **Full details.** Description as plain text (HTML optional), job category and functions, experience range, internship stipend and duration, and the job title and firm of the person who posted the job.
- **Agency or direct.** `viaRecruitmentAgency` tells you when a recruitment firm posted the job for the hiring company, and `recruiterCompany` names the firm.
- **Daily feed of new jobs.** Turn on **Only new jobs since the last run** and schedule the Actor; each run saves only jobs it has not saved before.
- **Market totals for free.** Instahyre's own counts for your search (total jobs, top functions, industries, companies, cities, company sizes) are saved next to the results at no charge.
- **No login, no API key, no proxy needed.**
- **Low price.** $1.00 per 1,000 jobs, descriptions included.

**Run it online, without code:** [Instahyre Jobs Scraper - India Tech, Sales & Operations Jobs](https://apify.com/pipiagent/instahyre-jobs-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `instahyre-jobs-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Example | Notes |
|---|---|---|
| `jobId`, `title` | 441980, Python Developer | |
| `company`, `companyId`, `companyLogo` | Nineleaps | The hiring company |
| `companyTagline`, `companyAbout` | We build high performance solutions | Short company description written by Instahyre |
| `companyFounded`, `companyEmployees` | 2014, 200 | `companyEmployees` is the size band Instahyre shows (for example 10, 200, 500, 1000) |
| `isFeaturedEmployer`, `isDiversityEmployer` | false, false | The badges Instahyre shows next to the company |
| `jobCategory`, `jobFunctions` | Software Engineering, [Backend Development, Full-Stack Development] | A job can have several functions; `jobCategory` is the main one |
| `skills` | [Python, Django, FastAPI] | The skill tags of the job |
| `locations`, `isRemote`, `acceptsOtherCities` | [Bangalore], false, true | `acceptsOtherCities` is true when candidates from other cities may apply |
| `jobType` | full_time | `full_time` or `internship` |
| `experienceMin`, `experienceMax` | 6, 8 | Years |
| `internshipStipend`, `internshipPaid`, `internshipDurationMonths` | 10000, true, 6 | Internships only. Stipend in rupees per month as entered by the employer |
| `recruiterDesignation`, `recruiterCompany`, `viaRecruitmentAgency` | Talent Partner, Nineleaps, false | The job title and firm of the person who posted the job. Their name and photo are not collected |
| `description`, `descriptionHtml` | | Plain text by default, HTML optional |
| `contactEmails`, `contactPhones` | [hr@example.com], [+91XXXXXXXXXX] | Only contacts written in the public job text, see below |
| `searchKeyword` | python | The keyword that found the job |
| `jobUrl`, `scrapedAt` | | |

Fields that a job does not have are `null` or an empty list, so every record has the same columns.

## Input examples

Python jobs in Bangalore:

```json
{
    "keywords": ["python"],
    "locations": ["Bangalore"],
    "maxItems": 100
}
```

Sales and operations jobs in Mumbai or remote, at large companies, open to someone with 5 years of experience:

```json
{
    "jobFunctions": ["Sales", "Operations"],
    "locations": ["Mumbai", "Remote"],
    "companySize": "large",
    "experienceYears": 5,
    "maxItems": 500
}
```

Daily feed of new internships in Delhi / NCR:

```json
{
    "jobType": "internship",
    "locations": ["Delhi / NCR"],
    "onlyNew": true
}
```

Product manager jobs whose title or skills contain both words:

```json
{
    "keywords": ["product manager"],
    "matchAllWords": true,
    "maxItems": 200
}
```

Refresh jobs you already have:

```json
{
    "jobUrls": ["https://www.instahyre.com/job-441980-python-developer-at-nineleaps-2-bangalore/", "440780"]
}
```

The whole board without descriptions. Set **Max results**: an input with no filters, no **Max results** and **Only new jobs** off (for example `{}`) only saves an example of the first 50 jobs. Output options such as **Include full description** do not count as filters, but **Max results** and **Only new jobs** do, so `{"onlyNew": true}` alone reads the whole board.

```json
{
    "includeDescription": false,
    "maxItems": 50000
}
```

**Job functions** accept a category or a narrower function. Categories: Software Engineering, Data Science & Analytics, IT Operations, Hardware Engineering, Product & Project Management, Design & Creative, Sales, Marketing, Customer Service, Operations, Consulting, Accounting, Finance & Banking, Human Resources, General Management, Legal, Administration & Facilities, Education & Training, Food, Beverages & Hospitality, Other. Functions include Backend Development, Frontend Development, Full-Stack Development, Mobile Development, Software Testing / QA / SDET, DevOps / Cloud, Data Science / Machine Learning, Data Analysis / Business Intelligence, Product Management, UX / Visual Design, Sales / Business Development, Presales, Online Marketing, Customer Service, Supply Chain / SCM / Logistics, Operations Management, Finance, Accounting / Taxation, Talent Acquisition / Recruitment and about 90 more, named as on Instahyre. A short form such as "backend" or "devops" picks every function whose name contains it.

**Industries** are the hiring company's industry as named on Instahyre, for example Computer Software / IT / Internet, Banking / Financial Services, Management Consulting, Healthcare / Hospitals, Retail or Recruitment / Staffing / HR. A single word such as "banking" also works.

**Locations** accept every city and region in the Instahyre location list, for example Bangalore, Hyderabad, Mumbai, Pune, Chennai, Delhi / NCR, Gurgaon, Noida, Kolkata, Ahmedabad, Remote (work from home), Anywhere in India, South India and Anywhere outside India. Common other spellings such as Bengaluru, Gurugram, Bombay or New Delhi are understood.

## Output example

```json
{
    "jobId": 441980,
    "title": "Python Developer",
    "company": "Nineleaps",
    "companyTagline": "We build high performance solutions",
    "companyAbout": "Nineleaps develops web, mobile, big data, and analytics applications, helping startups and large companies address complex technical challenges for users.",
    "companyFounded": 2014,
    "companyEmployees": 200,
    "companyLogo": "https://media.instahyre.com/images/profile/base/employer/5003/dcac758458/nineleaps.webp",
    "companyId": 5003,
    "isFeaturedEmployer": false,
    "isDiversityEmployer": false,
    "searchKeyword": "python",
    "jobCategory": "Software Engineering",
    "jobFunctions": ["Backend Development", "Full-Stack Development"],
    "skills": ["Python"],
    "locations": ["Bangalore"],
    "isRemote": false,
    "acceptsOtherCities": true,
    "jobType": "full_time",
    "experienceMin": 6,
    "experienceMax": 8,
    "internshipStipend": null,
    "internshipPaid": null,
    "internshipDurationMonths": null,
    "recruiterDesignation": "Talent Partner",
    "recruiterCompany": "Nineleaps",
    "viaRecruitmentAgency": false,
    "description": "We are looking for an experienced Python Developer to design, develop, and maintain scalable backend applications and APIs.\n\nResponsibilities:\n- Develop and maintain backend applications using Python.\n- Build and integrate REST APIs using frameworks like FastAPI, Flask, or Django...",
    "contactEmails": [],
    "contactPhones": [],
    "jobUrl": "https://www.instahyre.com/job-441980-python-developer-at-nineleaps-2-bangalore/",
    "scrapedAt": "2026-11-25T22:16:38Z"
}
```

## How much does it cost?

You pay per saved job: **$1.00 per 1,000 jobs**. There is no start fee and no monthly rental. Descriptions, details and market totals are included at no extra charge.

| Run | Jobs | Cost |
|---|---|---|
| Daily feed of new jobs for one skill and city | about 50 | $0.05 |
| One skill, all matching jobs | about 5,000 | $5.00 |
| The whole board | about 46,600 | $46.60 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Speed: Instahyre limits how fast its search can be read.** One search page holds 35 jobs. In our tests Instahyre allowed about 20 search pages a minute and about 250 search pages an hour from one address. When the hourly limit is reached, the Actor waits as long as Instahyre asks (45 minutes in our test, up to an hour) and then goes on, so runs never fail because of it, but they get slower. Without descriptions, up to about 8,000 jobs come back in about 15 minutes. With descriptions (the default), each job needs one more request, read at about 100 jobs a minute: 50 jobs took 40 seconds and 1,000 jobs take about 10 minutes.
- **The whole board takes about 10 hours.** Instahyre's search only pages through the first 10,000 results of one search, so the Actor splits bigger searches by company size, job category and job function. That reads some jobs twice (duplicates are removed and not charged): all 46,600 jobs need about 2,450 search pages, which is about 10 hours at 250 pages an hour, with or without descriptions. Raise the run timeout in the run options (the default is one hour). For a daily feed, use filters and **Only new jobs**, which keeps runs to minutes.
- **No posting date.** Instahyre's public job data has no posting or update date, so there is no date field and no "posted within" filter. Use **Only new jobs since the last run** to get only fresh jobs.
- **No salaries.** Instahyre does not show salaries on its public job pages; only internships have a stipend.
- **Order.** Results come in Instahyre's own order (the order of its search page), not by date.
- **Keyword search works like the Instahyre search box.** It also returns jobs that match only some of the words. Turn on **Every keyword word must appear** to keep only jobs whose title or skill tags contain every word.
- **Company size and experience level take one value per run.** Instahyre's search does not combine several of them.
- **Not included:** recruiter names and photos, applicant numbers, company websites, and anything Instahyre shows only to logged-in users.
- **This is unofficial.** The Actor is not made by, endorsed by or connected to Instahyre.

---

Full documentation, all input options and a free trial: **[Instahyre Jobs Scraper on Apify](https://apify.com/pipiagent/instahyre-jobs-scraper)**
