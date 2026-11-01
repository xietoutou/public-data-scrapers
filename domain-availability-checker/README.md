# Domain Availability Checker

Check whether domain names are available or already taken, thousands at a time. Paste your name ideas or a portfolio, press Start, and get one row per domain: `available`, `registered` or `unknown`, plus the registrar, creation and expiry dates and status for every registered name.

Use it to brainstorm brand names across many extensions, to find names that are about to drop, or to check a portfolio's expiry dates.

- **Bulk.** 1,000 domains in about 3 minutes, across .com, .net, .org, .io, .ai, .co, .app, .dev, .de, .uk and 1,200+ other extensions.
- **Official registry data.** Answers come from the registries' own RDAP servers (the modern replacement for WHOIS), found through the official IANA list, with WHOIS for several country domains that have no RDAP.
- **More than yes or no.** Registered names show registrar, creation and expiry dates, days until expiry, status codes and a `lifecycleStage` that flags names in their redemption or pending-delete period.
- **Paste anything.** Domains, URLs and email addresses work. Subdomains, duplicates and international names are handled for you.
- **No API key, no login, no proxy.**
- **Low price.** $2 per 1,000 domains. Invalid inputs are free.

**Run it online, without code:** [Domain Availability Checker - Bulk Check Any Extension](https://apify.com/pipiagent/domain-availability-checker) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `domain-availability-checker.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "domains": ["mybrand.com", "mybrand.io", "mybrand.ai", "mybrand.co", "mybrand.de", "mybrand.app"]
}
```

## Output examples

An available domain:

```json
{
    "input": "qzvj0de9gyd7o.com",
    "domain": "qzvj0de9gyd7o.com",
    "tld": "com",
    "valid": true,
    "registered": false,
    "availability": "available",
    "registrationSource": "rdap",
    "rdapUrl": "https://rdap.verisign.com/com/v1/domain/qzvj0de9gyd7o.com"
}
```

A registered domain:

```json
{
    "input": "stripe.com",
    "domain": "stripe.com",
    "registered": true,
    "availability": "registered",
    "registrationSource": "rdap",
    "lifecycleStage": "active",
    "registrar": "SafeNames Ltd.",
    "createdAt": "1995-09-12T04:00:00Z",
    "expiresAt": "2027-09-11T04:00:00Z",
    "domainAgeDays": 11369,
    "daysUntilExpiry": 317,
    "statusCodes": ["clientDeleteProhibited", "clientTransferProhibited", "clientUpdateProhibited"],
    "nameservers": ["ns-1087.awsdns-07.org", "ns-423.awsdns-52.com"]
}
```

A domain that is about to drop:

```json
{
    "domain": "5fvfofc9f.online",
    "registered": true,
    "lifecycleStage": "pendingDelete",
    "expiresAt": "2026-09-12T23:59:59Z",
    "daysUntilExpiry": -46,
    "statusCodes": ["pendingDelete", "serverHold", "redemptionPeriod"]
}
```

## How much does it cost?

You pay per checked domain: **$2.00 per 1,000 domains**. There is no start fee and no monthly rental. Invalid inputs and duplicates are not charged.

| Run | Domains | Cost |
|---|---|---|
| Name ideas across 10 extensions | 100 | $0.20 |
| A brainstorm list | 1,000 | $2.00 |
| A large portfolio | 10,000 | $20.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **"Available" is a strong hint, not a guarantee.** It means the registry has no record of the name. Premium, reserved or blocked names can still be impossible to register or cost more, and someone can register the name after the check. Always confirm at a registrar before you buy.
- **Not every country domain has a free public data source.** For extensions such as .es, .pt, .nz, .hk, .gr, .vn, .za and .cl, a domain is marked `registered` when it has name servers in DNS, and otherwise `unknown`, with the reason in `checkNote`. In a test of 192 domains across 45 extensions, 4 stayed unknown.
- **Some registries publish very little.** .de shows no dates and no registrar; .nl, .at and .be show no expiry date.
- **Owner data is usually hidden** since the GDPR. Names, emails and phone numbers are never collected.
- **WHOIS countries are slower.** WHOIS servers are asked about one domain per second, so 1,000 .ru domains take about 20 minutes.

---

Full documentation, all input options and a free trial: **[Domain Availability Checker on Apify](https://apify.com/pipiagent/domain-availability-checker)**
