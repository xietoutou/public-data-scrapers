# Website Email Extractor

Turn a list of websites or domains into a list of email addresses. Paste the websites, press Start, and get one row per company with every email the website shows publicly, plus the main company address picked for you. Sales teams, recruiters, agencies and researchers use it to build outreach lists and enrich CRM records.

- **Finds the pages that have emails.** The homepage plus contact, about, imprint, team and legal pages, in many languages (Kontakt, Contacto, Impressum, お問い合わせ, 联系我们 and more).
- **The right email first.** `primaryEmail` is the company's own general address (info@, contact@, hello@) when there is one, and `ownDomainEmails` keeps only addresses on the company's domain.
- **Hidden emails decoded.** Cloudflare email protection, HTML entities and addresses written as `name [at] company [dot] com`.
- **Pay only for websites with an email.** Websites without an email, unreachable or blocked websites are saved for free with a status that says why.
- **Phones and social profiles included** at no extra cost: phone numbers in international format, LinkedIn, Facebook, Instagram, X and more.
- **Low price.** $5 per 1,000 websites with an email.

**Run it online, without code:** [Website Email Extractor - Find Emails on Any Website List](https://apify.com/pipiagent/website-email-extractor) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `website-email-extractor.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input examples

```json
{
    "websites": ["timwendelboe.no", "https://www.sacher.com", "kofola.cz"]
}
```

Keep only websites where an email was found, and read more pages per website:

```json
{
    "websites": ["example-dental.com", "example-plumbing.co.uk"],
    "maxPagesPerWebsite": 20,
    "includeEmptyResults": false
}
```

## Output example

```json
{
    "website": "https://timwendelboe.no/",
    "domain": "timwendelboe.no",
    "status": "ok",
    "companyName": "Tim Wendelboe Coffee",
    "primaryEmail": "hello@timwendelboe.no",
    "emails": ["hello@timwendelboe.no", "press@timwendelboe.no"],
    "ownDomainEmails": ["hello@timwendelboe.no", "press@timwendelboe.no"],
    "emailCount": 2,
    "emailsFoundOn": [
        {"email": "hello@timwendelboe.no", "pageUrls": ["https://timwendelboe.no/pages/contact-us"]},
        {"email": "press@timwendelboe.no", "pageUrls": ["https://timwendelboe.no/pages/press"]}
    ],
    "primaryPhone": "+4740004062",
    "phones": ["+4740004062"],
    "facebook": ["https://www.facebook.com/TimWendelboeCoffee"],
    "instagram": ["https://www.instagram.com/timwendelboe"],
    "contactPageUrl": "https://timwendelboe.no/pages/contact-us",
    "pagesCrawledCount": 6,
    "scrapedAt": "2026-10-28T10:03:16Z"
}
```

`status` is `ok` when an email was found, `noContacts` when none was found (phones and social profiles are still listed, free of charge), `unreachable` or `blocked`.

## How much does it cost?

You pay **$5.00 per 1,000 websites with at least one email** ($0.005 per website). Websites without an email, unreachable or blocked websites cost nothing. There is no start fee and no monthly rental, and reading more pages per website does not cost more.

| Run | Websites with an email (typical) | Cost |
|---|---|---|
| 100 websites | about 70 | about $0.35 |
| 1,000 websites | about 700 | about $3.50 |

The share of websites with an email depends on your list. Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Emails are not verified.** The Actor reports addresses as the website shows them. It does not check whether a mailbox exists.
- **Some websites block automated visitors.** In our tests about 8% of websites answered with a bot check or "access denied". These come back as `blocked` and are free.
- **JavaScript-only websites give fewer results.** The Actor reads the HTML the server sends and does not run a browser.
- **It reads contact-like pages, not the whole website.** Up to **Max pages per website** (default 10). Emails that appear only in blog posts or deep product pages can be missed.
- **Emails of other companies can appear**, for example the web agency named on an imprint page. Use `ownDomainEmails` when you only want the company's own addresses.
- **Speed.** About 10 to 15 websites per minute with the default settings.

---

Full documentation, all input options and a free trial: **[Website Email Extractor on Apify](https://apify.com/pipiagent/website-email-extractor)**
