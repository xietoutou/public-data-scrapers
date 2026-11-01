# Website Contact Scraper

Find email addresses, phone numbers and social media profiles on any list of company websites. Paste the websites, press Start, and get one clean row per company with every contact the website shows publicly. Sales teams, recruiters, agencies and researchers use it to turn a list of domains into a contact list for outreach, CRM enrichment or market research.

- **One row per website.** All emails, phones and profiles from the homepage, contact, about, imprint and team pages are merged and deduplicated.
- **Pay only for websites with contacts.** Websites that cannot be opened or show no contact details are saved for free, with a status that says why.
- **Social profiles included.** LinkedIn, Facebook, Instagram, X (Twitter), YouTube, TikTok, Pinterest, GitHub, WhatsApp and Telegram, without share buttons or post links.
- **Works in many languages.** It finds contact pages called Kontakt, Contacto, Contatti, Impressum, À propos, お問い合わせ, 联系我们 and many more.
- **Clean data.** Phone numbers in international format (+4930...), lowercased emails, junk such as `logo@2x.png` or `user@example.com` removed.
- **Low price.** $5 per 1,000 websites with contacts. The number of pages read per website does not change the price.

**Run it online, without code:** [Website Contact Scraper - Emails, Phones & Social Profiles](https://apify.com/pipiagent/website-contact-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `website-contact-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Field | Example |
|---|---|
| `companyName` | Tim Wendelboe Coffee |
| `primaryEmail` | hello@timwendelboe.no |
| `emails` | All email addresses found on the website |
| `ownDomainEmails` | Only the emails on the company's own domain |
| `primaryPhone`, `phones` | +4740004062 |
| `linkedIn`, `facebook`, `instagram`, `twitter`, `youtube`, `tiktok`, `pinterest`, `github`, `whatsapp`, `telegram` | Profile links |
| `contactPageUrl` | The website's contact page |
| `emailsFoundOn` | Which page each email was found on |
| `title`, `description`, `language` | Homepage title, meta description and language |
| `url`, `domain` | The final address after redirects |
| `pagesCrawled` | Every page the Actor read |
| `status` | `ok`, `noContacts`, `unreachable` or `blocked` |

## Input examples

Scan a list of company websites with the default settings:

```json
{
    "websites": ["timwendelboe.no", "https://www.sacher.com", "kofola.cz"]
}
```

Read more pages per website, set the country for local phone numbers, and keep only websites with contacts:

```json
{
    "websites": ["https://www.example-dental.com", "example-plumbing.co.uk"],
    "maxPagesPerWebsite": 20,
    "defaultCountry": "GB",
    "includeEmptyResults": false
}
```

Only check the homepage of each website, which is the fastest:

```json
{
    "websites": ["coffeecollective.dk", "the-barn.de"],
    "maxDepth": 0
}
```

## Output examples

A website with contacts (shortened):

```json
{
    "website": "https://timwendelboe.no/",
    "url": "https://timwendelboe.no/",
    "domain": "timwendelboe.no",
    "status": "ok",
    "companyName": "Tim Wendelboe Coffee",
    "primaryEmail": "hello@timwendelboe.no",
    "primaryPhone": "+4740004062",
    "emails": ["hello@timwendelboe.no", "press@timwendelboe.no"],
    "ownDomainEmails": ["hello@timwendelboe.no", "press@timwendelboe.no"],
    "emailCount": 2,
    "phones": ["+4740004062"],
    "phoneCount": 1,
    "linkedIn": [],
    "facebook": ["https://www.facebook.com/TimWendelboeCoffee"],
    "instagram": ["https://www.instagram.com/timwendelboe"],
    "youtube": ["https://www.youtube.com/@TimWendelboeCoffee"],
    "socialCount": 5,
    "title": "Tim Wendelboe | Tim Wendelboe Coffee",
    "description": "Tim Wendelboe is a coffee roastery, espresso bar and coffee training centre located in Oslo, Norway.",
    "language": "en",
    "contactPageUrl": "https://timwendelboe.no/pages/contact-us",
    "emailsFoundOn": [
        {"email": "hello@timwendelboe.no", "pageUrls": ["https://timwendelboe.no/pages/contact-us", "https://timwendelboe.no/pages/our-team"]},
        {"email": "press@timwendelboe.no", "pageUrls": ["https://timwendelboe.no/pages/press"]}
    ],
    "pagesCrawled": [
        "https://timwendelboe.no/",
        "https://timwendelboe.no/pages/contact-us",
        "https://timwendelboe.no/pages/about",
        "https://timwendelboe.no/pages/press",
        "https://timwendelboe.no/pages/our-team",
        "https://timwendelboe.no/pages/data-sharing-opt-out"
    ],
    "pagesCrawledCount": 6,
    "error": null,
    "scrapedAt": "2026-10-28T10:03:16Z"
}
```

A website that refused the request (free, shortened):

```json
{
    "website": "https://bookpeople.com/",
    "status": "blocked",
    "emails": [],
    "phones": [],
    "pagesCrawledCount": 0,
    "error": "the website refused automated requests (HTTP 403)",
    "scrapedAt": "2026-10-28T10:01:50Z"
}
```

Each run also saves a **Run summary** (in the Output tab) with the number of websites per status and the list of websites without contacts.

## How much does it cost?

You pay **$5.00 per 1,000 websites with contacts** ($0.005 per website). A website counts when at least one email, phone number or social profile was found. Websites that could not be opened, were blocked or had no contacts cost nothing. There is no start fee and no monthly rental, and reading more pages per website does not cost more.

| Run | Websites with contacts | Cost |
|---|---|---|
| 100 websites | about 85 | about $0.43 |
| 1,000 websites | about 850 | about $4.25 |
| 10,000 websites | about 8,500 | about $42.50 |

The share of websites with contacts depends on your list. In our tests with about 110 real company websites from 20 countries, 85% had contacts. Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Some websites block automated visitors.** In our tests about 8% of websites answered with a bot check or "access denied" (Cloudflare, Sucuri and similar). These come back with status `blocked` and are free. The Actor already retries them once through another server address, which rarely gets past strong bot protection.
- **JavaScript-only websites give fewer results.** The Actor reads the HTML that the server sends and does not run a browser. Websites built entirely in JavaScript show almost nothing to it. In our tests this was about 4% of websites. They come back as `noContacts` with a note in `error`.
- **It reads contact-like pages, not the whole website.** The homepage plus pages such as contact, about, imprint, team, legal and support, up to **Max pages per website** (default 10). Emails that appear only in blog posts or deep product pages can be missed.
- **Emails of other companies can appear.** Imprint pages often name the web agency or the parent company, and some pages show the email of a partner. Use `ownDomainEmails` when you only want the company's own addresses. Typing mistakes on the website are kept as they are.
- **Phone numbers are read carefully.** To avoid order numbers, tax IDs and dates, a number is kept only when it is a link, has a phone label nearby (Tel, Phone, Telefon...), starts with + or 00, or is written in phone-style groups. Local numbers are read with the country of the domain ending (.de, .fr, ...) or the page language, so a `.com` website with local numbers from another country may need **Country for phone numbers**. Fax numbers are skipped.
- **Emails are not verified.** The Actor reports addresses as the website shows them. It does not check whether a mailbox exists.
- **Speed.** About 10 to 15 websites per minute with the default settings. Each website is read politely, one page after another.

---

Full documentation, all input options and a free trial: **[Website Contact Scraper on Apify](https://apify.com/pipiagent/website-contact-scraper)**
