# Sports Injury Reports

Get the current injury report of every team in the NFL, NBA, MLB, NHL, WNBA, college football and college basketball, from [ESPN](https://www.espn.com)'s public website, without an API key.

Fantasy players, betting model builders, sports apps, newsletters and analysts use it to know who is out before the next game, and to build their own injury history by running it every day.

- **All teams of a league in one run.** One row per injured player, for as many leagues as you pick.
- **The details that matter.** Status (Out, Doubtful, Questionable, Day-To-Day, injured reserve...), fantasy status, injury type, body part, side, expected return date, last update time, and ESPN's short and long notes.
- **Clean IDs and links.** ESPN player and team IDs, team abbreviation, position, headshot and player page link, so you can join the data with box scores and rosters.
- **No login, no API key, no proxy.**
- **Low price.** $0.50 per 1,000 injured players.

**Run it online, without code:** [Sports Injury Reports - NFL, NBA, MLB, NHL Injuries](https://apify.com/pipiagent/sports-injury-reports) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `sports-injury-reports.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## Input example

```json
{
    "leagues": ["nfl", "nba"],
    "teams": ["Chiefs", "Lakers", "BOS"]
}
```

## Output example

```json
{
    "type": "injury",
    "league": "nba",
    "leagueName": "NBA",
    "season": "2026-27",
    "teamId": "1",
    "teamName": "Atlanta Hawks",
    "teamAbbreviation": "ATL",
    "playerId": "4712863",
    "playerName": "Mouhamed Gueye",
    "position": "F",
    "positionName": "Forward",
    "status": "Out",
    "fantasyStatus": "OUT",
    "injury": "Foot",
    "bodyPart": "Leg",
    "detail": "Fracture",
    "side": "Left",
    "expectedReturn": "2026-11-20",
    "updatedAt": "2026-10-19T19:38:00Z",
    "shortComment": "Gueye underwent surgery Tuesday to repair a fractured left foot that he suffered during a workout last week, Brad Rowland of the Locked On Podcast Network reports.",
    "longComment": "Gueye will be re-evaluated by medical staff in 3-to-4 months, which means he'll miss all of training camp and preseason...",
    "headshot": "https://a.espncdn.com/i/headshots/nba/players/full/4712863.png",
    "playerUrl": "https://www.espn.com/nba/player/_/id/4712863/mouhamed-gueye"
}
```

## How much does it cost?

You pay per saved result: **$0.50 per 1,000 injured players**. There is no start fee and no monthly rental.

| Run | Results | Cost |
|---|---|---|
| NBA injury report | 87 | $0.04 |
| NFL, NBA, MLB and NHL | 1,210 | $0.61 |
| The same four leagues every day for a month | about 36,000 | about $18 |

Set **Max results** or a maximum charge per run in the run options, and the Actor stops when it is reached.

## Limits you should know

- **This is the current list only.** ESPN shows who is injured now, not past injuries. Schedule the Actor daily to build a history.
- **Expected return dates are estimates** from ESPN and are often empty or change.
- **NFL lists include players marked Active.** ESPN keeps players who returned from an injury on the NFL report for a while with the status Active. Filter on `status` if you only want players who are out or questionable. In our test, 596 of 800 NFL rows were Active.
- **Out of season, lists are short.** A league in its off-season may return only long-term injuries, or none.
- **This is unofficial.** The Actor reads the public JSON data that ESPN's own website and apps load. It is not made by, endorsed by or connected to ESPN.

---

Full documentation, all input options and a free trial: **[Sports Injury Reports on Apify](https://apify.com/pipiagent/sports-injury-reports)**
