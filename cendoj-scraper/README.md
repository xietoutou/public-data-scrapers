# CENDOJ Scraper

Search [CENDOJ](https://www.poderjudicial.es/search/indexAN.jsp), the official public database of Spanish court decisions run by the Centro de Documentación Judicial, and download the results as a clean table. It covers sentencias, autos and acuerdos from the Tribunal Supremo, Audiencia Nacional, Tribunales Superiores de Justicia, Audiencias Provinciales, Tribunales de Instancia and juzgados. Law firms, legal-tech companies, legal AI teams and researchers use it to track new case law, build datasets and feed search or RAG systems.

- **More than 200 results per search.** CENDOJ shows at most 200 results for one search. When you sort by date, the Actor moves through the dates on its own and keeps going. In our test it collected all 509 matches of a search that CENDOJ caps at 200.
- **All the search filters of the CENDOJ form.** Search text with CENDOJ's own operators, court, jurisdiction, resolution type, region, decision date, ponente, decision number, appeal number, section and language.
- **Exact lookups.** Paste ECLI or ROJ identifiers and get those decisions.
- **Readable court names.** Codes such as `SAP M` or `STIC` become "Audiencia Provincial de Madrid" or "Tribunal de Instancia, Sección Civil de Burgos".
- **No login and no proxy needed.** Press Start and get data.
- **Low price.** $0.60 per 1,000 results.

**Run it online, without code:** [CENDOJ Scraper - Spanish Case Law (Jurisprudencia) Search](https://apify.com/pipiagent/cendoj-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `cendoj-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

One result is one court decision as CENDOJ lists it.

| Field | Example | What it is |
|---|---|---|
| `roj` | `SAP M 16879/2025` | ROJ identifier (Repertorio Oficial de Jurisprudencia) |
| `ecli` | `ECLI:ES:APM:2025:16879` | European Case Law Identifier |
| `decisionType` | `Sentencia` | Sentencia, Auto, Auto aclaratorio or Acuerdo |
| `date` | `2025-12-19` | Date of the decision |
| `court` | `Audiencia Provincial de Madrid` | Court, with chamber and seat when CENDOJ shows them |
| `courtCode`, `courtLevel` | `AP`, `Audiencia Provincial` | Court code from the ROJ and its level |
| `chamber` | `Sala de lo Civil` | Chamber (sala). CENDOJ shows it for the Tribunal Supremo |
| `jurisdiction` | `Civil` | Jurisdiction, when the chamber, the court or your filter tells it |
| `courtSeat`, `city` | `Madrid`, `Madrid` | Province or region of the court, and its municipality |
| `ponente` | `FRANCISCO RAMON MOYA HURTADO DE MENDOZA` | Judge rapporteur, as published |
| `decisionNumber` | `410/2025` | Número de resolución |
| `appealNumber` | `1246/2025` | Número de recurso |
| `summary` | `Desahucio por precario...` | The summary (resumen) CENDOJ shows in the list |
| `language` | `es` | Language of the decision |
| `publishedDate` | `2026-02-16` | Date CENDOJ published the decision |
| `documentUrl` | `https://www.poderjudicial.es/search/AN/openDocument/...` | Official link to the decision |
| `pdfUrl` | | Direct PDF link. Only acuerdos have one (see Limits) |
| `cendojId`, `title`, `searchQuery`, `scrapedAt` | | CENDOJ internal id, list title, the search that found it, time of the scrape |

## Input examples

Every Sentencia of the Audiencia Provincial de Madrid about desahucio in 2025:

```json
{
    "searchText": "desahucio",
    "courts": ["AP"],
    "regions": ["MADRID"],
    "jurisdictions": ["CIVIL"],
    "resolutionTypes": ["SENTENCIA"],
    "dateFrom": "2025-01-01",
    "dateTo": "2025-12-31",
    "maxItems": 1000
}
```

The most relevant decisions for a phrase, using CENDOJ's search syntax:

```json
{
    "searchText": "\"cláusula suelo\" Y nulidad",
    "sort": "relevance",
    "maxItems": 200
}
```

Look up exact decisions:

```json
{
    "ecli": ["ECLI:ES:TS:2026:10318A"],
    "roj": ["SAP M 12824/2026", "STS 4543/2026"]
}
```

New decisions of the Sala de lo Social of the Tribunal Supremo, for a weekly scheduled run:

```json
{
    "courts": ["TS_SOCIAL"],
    "lastDays": 30,
    "maxItems": 500
}
```

## Output examples

A Tribunal Supremo decision:

```json
{
    "roj": "ATS 10516/2026",
    "ecli": "ECLI:ES:TS:2026:10516A",
    "title": "ATS, a 13 de noviembre de 2026",
    "decisionType": "Auto",
    "date": "2026-11-13",
    "court": "Tribunal Supremo. Sala de lo Civil",
    "courtCode": "TS",
    "courtLevel": "Tribunal Supremo",
    "chamber": "Sala de lo Civil",
    "jurisdiction": "Civil",
    "courtSeat": null,
    "city": "Madrid",
    "ponente": "PEDRO JOSE VELA TORRES",
    "decisionNumber": "165/2026",
    "appealNumber": "6421/2022",
    "summary": "Comisión de apertura. Devolución actuaciones a la Audiencia Provincial. Reiteración de la jurisprudencia de la sala",
    "otherDetails": null,
    "language": "es",
    "publishedDate": "2026-11-20",
    "cendojId": "11933594",
    "documentUrl": "https://www.poderjudicial.es/search/AN/openDocument/614b5b1be72b9ce9a0a8778d75e36f0d/20261120",
    "pdfUrl": null,
    "searchQuery": "example: newest Tribunal Supremo decisions",
    "scrapedAt": "2026-11-25T23:13:48Z"
}
```

An Audiencia Provincial decision:

```json
{
    "roj": "SAP M 16879/2025",
    "ecli": "ECLI:ES:APM:2025:16879",
    "title": "SAP Madrid, a 19 de diciembre de 2025",
    "decisionType": "Sentencia",
    "date": "2025-12-19",
    "court": "Audiencia Provincial de Madrid",
    "courtCode": "AP",
    "courtLevel": "Audiencia Provincial",
    "chamber": null,
    "jurisdiction": "Civil",
    "courtSeat": "Madrid",
    "city": "Madrid",
    "ponente": "FRANCISCO RAMON MOYA HURTADO DE MENDOZA",
    "decisionNumber": "410/2025",
    "appealNumber": "1246/2025",
    "summary": "Desahucio por precario. Ocupación consentida pro la propiedad. Comodato sin duración determinada. Precario",
    "language": "es",
    "publishedDate": "2026-02-16",
    "cendojId": "11619617",
    "documentUrl": "https://www.poderjudicial.es/search/AN/openDocument/408b308a0a103c28a0a8778d75e36f0d/20260216",
    "searchQuery": "desahucio; courts=AP; jurisdictions=CIVIL; types=SENTENCIA; regions=MADRID; from=2025-01-01; to=2025-12-31",
    "scrapedAt": "2026-11-25T23:15:20Z"
}
```

## How much does it cost?

You pay per saved decision: **$0.60 per 1,000 results**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| The default example | 20 | $0.012 |
| One year of desahucio sentencias of one Audiencia Provincial | 509 | $0.31 |
| A large research dataset | 10,000 | $6.00 |

Set a maximum charge per run in the run options and the Actor stops when it is reached.

## Limits you should know

- **Speed: about 6 seconds per 50 decisions.** CENDOJ's robots.txt asks automated clients to wait 5 seconds between requests, and the Actor always respects that. It sends one request at a time and gets 50 decisions per request, so it saves about 400 to 500 decisions per minute. In our tests the default example (20 decisions) took about 10 seconds, 300 decisions took 49 seconds and 509 took 76 seconds. Each ECLI or ROJ lookup takes one request, about 6 seconds.
- **No full text and no PDF of judgments.** CENDOJ shows a CAPTCHA ("Control Descargas masivas") before it opens any decision document. We saw it on the very first document request, both from Apify's servers and from a home connection. The Actor does not solve or bypass CAPTCHAs, so it collects the list data and the official `documentUrl`. Open that link in your browser to read the judgment. Acuerdos are the exception: CENDOJ links them as plain PDF files, and the Actor puts that link in `pdfUrl`.
- **200 results per search when sorting by relevance or by recently published.** This is CENDOJ's own cap. Sort by newest or oldest decision date to go past it.
- **Very busy days.** When one single day has more than 200 matching decisions, the Actor splits that day by jurisdiction, and then by region if needed. If some decisions of that day still cannot be reached, it logs a warning with the number that may be missing, and you can add a court filter to get them. This only happens on broad searches without search text, and the extra requests make them slower.
- **Some fields are not in CENDOJ's result list.** The section (sección) of a court and the parties are not shown there. The chamber is shown for the Tribunal Supremo but not for the Audiencia Nacional or lower courts. `jurisdiction` is empty when neither the court, the chamber nor your filters tell it.
- **Broad searches can be slow on CENDOJ's side.** A search over all courts and all years can take CENDOJ 10 to 20 seconds to answer its first page. Adding a court, a region or a date range usually brings it back to about 1 second.
- **A search needs at least one criterion.** CENDOJ refuses a search with no text and no filter. The Actor then runs its small example instead.
- **Anonymized data.** CENDOJ removes personal data of the parties from published decisions. The Actor keeps the data exactly as CENDOJ publishes it and never tries to identify anyone. Judges' names in `ponente` are published by CENDOJ.

---

Full documentation, all input options and a free trial: **[CENDOJ Scraper on Apify](https://apify.com/pipiagent/cendoj-scraper)**
