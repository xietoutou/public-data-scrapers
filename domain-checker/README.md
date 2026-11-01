# Domain Checker

Check a list of domains in one run and get one clean row per domain: is it available or registered, who is the registrar, when was it created, when does it expire, which status codes it has, its DNS records, its SSL certificate and its Majestic Million rank. Domain investors use it to find names that are free or about to drop, marketers and sales teams use it to qualify lead lists, and IT and security teams use it to watch expiry dates and certificates.

- **One row per domain, everything in it.** Availability, registrar, creation and expiry dates, domain age, status codes, name servers, DNSSEC, A, MX and TXT records, SPF, DMARC, SSL certificate and Majestic Million rank with referring subnets.
- **Official registry data.** Registration data comes from the registries' own RDAP servers (the modern replacement for WHOIS), found through the official IANA list. Several country domains without RDAP are read from the registry's WHOIS server.
- **Paste anything.** Domains, website URLs and email addresses all work. Subdomains, duplicates and international names (like münchen.de) are handled for you.
- **No API key, no login, no proxy.**
- **Low price.** $2 per 1,000 domains. Invalid inputs are free.

**Run it online, without code:** [Domain Checker - Bulk Availability, WHOIS (RDAP), DNS & SSL](https://apify.com/pipiagent/domain-checker) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `domain-checker.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Group | Fields |
|---|---|
| Availability | `registered`, `availability` (`available`, `registered` or `unknown`), `registrationSource` (`rdap`, `whois` or `dns`), `checkNote` |
| Registration | `registrar`, `registrarIanaId`, `createdAt`, `updatedAt`, `expiresAt`, `domainAgeDays`, `daysUntilExpiry`, `statusCodes`, `lifecycleStage`, `nameservers`, `dnssec`, `registrantOrganization`, `registrantCountry`, `rdapUrl` |
| DNS (optional) | `dnsStatus`, `hasWebsite`, `hasEmail`, `aRecords`, `aaaaRecords`, `mxRecords`, `dnsNameservers`, `txtRecords`, `spfRecord`, `dmarcRecord`, `dmarcPolicy` |
| SSL certificate (optional) | `sslValid`, `sslIssuer`, `sslSubject`, `sslValidFrom`, `sslValidTo`, `sslDaysLeft`, `sslSanCount`, `sslHost`, `sslError` |
| Majestic Million (optional) | `majesticRank` (1 = the domain with the most referring subnets), `majesticRefSubNets`, `majesticRefIPs`, `majesticListDate` |

### What the status codes mean

Registries attach status codes to every registered domain. The most useful ones:

| Code | Meaning |
|---|---|
| `ok` / `active` | Normal registered domain with no special restrictions. |
| `clientTransferProhibited`, `clientUpdateProhibited`, `clientDeleteProhibited` | Locks set by the registrar to stop unauthorised transfers or changes. Very common and harmless. |
| `serverTransferProhibited`, `serverUpdateProhibited`, `serverDeleteProhibited` | The same locks set by the registry. Common on valuable brand domains. |
| `clientHold`, `serverHold` | The domain is taken out of DNS, so its website and email stop working. Often a sign of an unpaid renewal, a dispute or abuse. |
| `inactive` | The domain has no name servers, so it is registered but not in use. |
| `addPeriod` | Registered in the last few days. |
| `autoRenewPeriod` | The domain passed its expiry date recently and was renewed automatically. The owner can still cancel and let it go during this period (usually 45 days). |
| `redemptionPeriod` | The domain expired and was deleted by the registrar. Only the last owner can restore it, usually within 30 days and for a fee. |
| `pendingDelete` | The final stage before the name becomes available to everyone, usually after about 5 days. |
| `pendingTransfer` | The domain is moving to another registrar. |

`lifecycleStage` sums this up in one word: `active`, `onHold`, `expiredGracePeriod` (expiry date has passed), `redemptionPeriod` or `pendingDelete`. Filter on `redemptionPeriod` and `pendingDelete` to find names that are about to drop.

## Input examples

Check a list of domains with every check turned on:

```json
{
    "domains": ["apify.com", "wikipedia.org", "bbc.co.uk", "zqxv-free-example-domain-2026.com"]
}
```

Only check availability and registration data, as fast as possible:

```json
{
    "domains": ["mybrand.com", "mybrand.io", "mybrand.ai", "mybrand.co", "mybrand.de"],
    "checkDns": false,
    "checkSsl": false,
    "addMajesticRank": false
}
```

Find the domains behind a list of email addresses and website URLs:

```json
{
    "domains": ["sales@ibm.com", "https://www.nytimes.com/section/world", "WWW.Reddit.COM"]
}
```

## Output examples

A registered domain (some TXT records left out):

```json
{
    "input": "stripe.com",
    "domain": "stripe.com",
    "tld": "com",
    "valid": true,
    "registered": true,
    "availability": "registered",
    "registrationSource": "rdap",
    "lifecycleStage": "active",
    "registrar": "SafeNames Ltd.",
    "registrarIanaId": "447",
    "createdAt": "1995-09-12T04:00:00Z",
    "updatedAt": "2025-10-01T01:39:51Z",
    "expiresAt": "2027-09-11T04:00:00Z",
    "domainAgeDays": 11369,
    "daysUntilExpiry": 317,
    "statusCodes": ["clientDeleteProhibited", "clientTransferProhibited", "clientUpdateProhibited", "serverDeleteProhibited", "serverTransferProhibited", "serverUpdateProhibited"],
    "nameservers": ["ns-1087.awsdns-07.org", "ns-1882.awsdns-43.co.uk", "ns-423.awsdns-52.com", "ns-705.awsdns-24.net"],
    "dnssec": false,
    "rdapUrl": "https://rdap.verisign.com/com/v1/domain/stripe.com",
    "dnsStatus": "ok",
    "hasWebsite": true,
    "hasEmail": true,
    "aRecords": ["198.137.150.231", "198.202.176.231"],
    "mxRecords": ["10 aspmx.l.google.com", "20 alt1.aspmx.l.google.com", "20 alt2.aspmx.l.google.com", "30 aspmx2.googlemail.com", "30 aspmx3.googlemail.com"],
    "spfRecord": "v=spf1 ip4:198.2.180.60/32 ip4:13.111.2.227/32 include:spf1.stripe.com include:greenhouse-outbound-mail.stripe.com include:_spf.qualtrics.com ~all",
    "dmarcPolicy": "reject",
    "sslValid": true,
    "sslIssuer": "DigiCert, Inc.",
    "sslValidTo": "2027-05-09T23:59:59Z",
    "sslDaysLeft": 193,
    "majesticRank": 141,
    "majesticRefSubNets": 51384,
    "majesticRefIPs": 138487,
    "majesticListDate": "2026-10-28",
    "url": "https://stripe.com",
    "scrapedAt": "2026-10-28T12:23:20Z"
}
```

An available domain:

```json
{
    "input": "qzvj0de9gyd7o.com",
    "domain": "qzvj0de9gyd7o.com",
    "valid": true,
    "registered": false,
    "availability": "available",
    "registrationSource": "rdap",
    "rdapUrl": "https://rdap.verisign.com/com/v1/domain/qzvj0de9gyd7o.com",
    "dnsStatus": "notRegistered",
    "hasWebsite": false,
    "majesticRank": null
}
```

A domain that is about to drop:

```json
{
    "domain": "5fvfofc9f.online",
    "registered": true,
    "availability": "registered",
    "lifecycleStage": "pendingDelete",
    "registrar": "NameCheap, Inc.",
    "createdAt": "2025-09-12T00:01:03Z",
    "expiresAt": "2026-09-12T23:59:59Z",
    "daysUntilExpiry": -46,
    "statusCodes": ["serverUpdateProhibited", "pendingDelete", "serverHold", "clientTransferProhibited", "serverTransferProhibited", "redemptionPeriod"]
}
```

A country domain without an RDAP server, read from WHOIS:

```json
{
    "domain": "google.it",
    "registered": true,
    "availability": "registered",
    "registrationSource": "whois",
    "registrar": "MarkMonitor International Limited",
    "createdAt": "1999-12-10T00:00:00Z",
    "expiresAt": "2027-04-21T00:00:00Z",
    "statusCodes": ["ok"],
    "checkNote": "From WHOIS server whois.nic.it."
}
```

An input that is not a domain (listed so nothing disappears, not charged):

```json
{
    "input": "co.uk",
    "domain": null,
    "valid": false,
    "error": "\"co.uk\" is a public suffix, not a registrable domain"
}
```

## How much does it cost?

You pay per checked domain: **$2.00 per 1,000 domains**. There is no start fee and no monthly rental. Invalid inputs and duplicates are not charged. Turning the DNS, SSL or Majestic checks on or off does not change the price.

| Run | Domains | Cost |
|---|---|---|
| A short list of name ideas | 100 | $0.20 |
| A lead list | 1,000 | $2.00 |
| A large portfolio | 10,000 | $20.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **"Available" is a strong hint, not a guarantee.** It means the registry has no record of the name. Premium, reserved or blocked names can still be impossible to register or cost more than the normal price, and someone can register the name after the check. Always confirm at a registrar before you buy.
- **Not every country domain has a free public data source.** Registration data comes from RDAP for all generic domains (.com, .net, .org, .xyz, .app and about 1,200 others) and for many country domains (.uk, .fr, .nl, .ca, .au, .br, .in, .pl and more). Extra RDAP servers are used for .io, .co, .me, .us, .de, .ch, .li, .sh and .ac. For .jp, .cn, .eu, .it, .se, .nu, .dk, .at, .be, .ru, .su, .mx and .tr the Actor asks the registry's WHOIS server. For other country domains, such as .es, .pt, .nz, .hk, .gr, .vn, .za and .cl, there is no free source the Actor can use. A domain there is marked `registered` with `registrationSource: "dns"` when it has name servers in DNS, and otherwise `unknown`, with the reason in `checkNote`. In a test of 192 domains across 45 extensions, 127 were answered by RDAP, 42 by WHOIS, 19 from DNS and 4 stayed unknown.
- **Some registries publish very little.** .de shows no dates and no registrar. .nl, .at and .be show no expiry date. .au and .eu show no dates. .jp shows no registrar. Those fields are empty.
- **Owner data is usually hidden.** Since the GDPR most registries hide the registrant. `registrantOrganization` and `registrantCountry` are filled only when the registry publishes them. Names, emails and phone numbers are never collected.
- **Some registries limit how fast you can ask.** The Actor paces its requests per registry, slows down when it is told to and retries. In rare cases a domain still ends as `unknown` with the reason in `checkNote`. Run those again later.
- **Speed.** 200 mixed domains take under a minute and 1,000 domains about 3 to 4 minutes. WHOIS servers are asked about one domain per second, so a long list of one WHOIS country (for example 1,000 .ru domains) takes about 20 minutes.
- **SSL check.** The Actor reads the certificate on port 443 of the domain, and of www.domain if the bare domain does not answer. It does not follow redirects. A site that does not send its full certificate chain is reported as not trusted (`unable to get local issuer certificate`) even when browsers accept it.
- **Subdomains are checked as their main domain.** news.bbc.co.uk is checked as bbc.co.uk, because only main domains are registered. Names like gov.uk or co.uk are public suffixes and are listed as invalid.
- **Majestic Million rank** covers the 1 million domains with the most links from different subnets, updated daily by Majestic. It measures link authority, not traffic. Domains outside the list get `majesticRank: null`. The rank is for the main domain only. The Actor reads the whole list (about 80 MB) once per run; if it cannot be downloaded within 75 seconds the Majestic fields stay empty and everything else is still saved.

---

Full documentation, all input options and a free trial: **[Domain Checker on Apify](https://apify.com/pipiagent/domain-checker)**
