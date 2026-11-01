# ESPN Scraper

Get sports data from ESPN's public website: scores and schedules, box scores with player stats, play-by-play, standings, team rosters, news and injury reports. It covers the NFL, NBA, WNBA, MLB, NHL, college football and basketball, the Premier League and 18 other soccer competitions, plus ATP and WTA tennis, PGA and LPGA golf, Formula 1 and UFC. Sports analysts, fantasy and betting tool builders, journalists, app developers and researchers use it to fill spreadsheets, databases and dashboards without copying tables by hand.

- **Eight kinds of data in one Actor.** Games and scores, game details (box scores, team stats, player stats, play-by-play), team schedules, standings, teams, rosters, news and injury reports.
- **Full seasons in one run.** Pick "Whole season" and get every game of a league, for example all 1,401 NBA games of 2025-26 in under 10 seconds.
- **Complete college slates.** College football (FBS) and Division I basketball return every game of the day, not only the 25 featured games ESPN shows by default.
- **Flat, clean output.** One row per game, per player, per standings row or per article, with English field names, ISO dates in UTC and full links. Ready for Excel, Google Sheets or code.
- **No login, no API key, no proxy.** Press Start and get data.
- **Low price.** $1.00 per 1,000 results, no start fee.

**Run it online, without code:** [ESPN Scraper - Scores, Box Scores, Standings, Rosters & News](https://apify.com/pipiagent/espn-scraper) on Apify (free plan available).

## Run it from Python

```bash
pip install apify-client
export APIFY_TOKEN=<your token>   # Windows: set APIFY_TOKEN=<your token>
python example.py
```

[example.py](example.py) runs the scraper with [input.json](input.json) and saves `espn-scraper.csv`. Edit input.json, or pass another file: `python example.py my-input.json`. The API token is on the [Integrations page](https://console.apify.com/settings/integrations) of Apify Console.

## What data can you get?

| Mode | One result is | Main fields |
|---|---|---|
| Games and scores | One game | Teams, scores, status, start time, quarter or half scores, records, venue, TV, betting line (spread, over/under, moneyline), soccer goal scorers, links |
| Game details | One game, plus one row per player (optional: one row per play) | Everything above plus attendance, referees, 25 to 30 team stats per side, game leaders, opening and closing lines, recap headline; player box score lines; play-by-play text with clock and score |
| Team schedule | One game | Every game of the teams you list for a season, finished and upcoming. Soccer clubs include all competitions (league, cups, Champions League) |
| Standings | One team | Position, group, wins, losses, ties, win %, games behind, points, streak, home and away records, playoff seed, note (for example "Champions League"). Tennis gives the ATP or WTA ranking, F1 the driver and constructor standings |
| Teams | One team | Team ID, name, abbreviation, colors, logo, links to the team, roster and schedule pages |
| Rosters | One player | Name, jersey, position, age, birth date, height, weight, birthplace, college, experience, injury status, nationality. Soccer players also get season totals (appearances, goals, assists, cards) |
| News | One article | Headline, summary, publish time, author, teams and players mentioned, image, link |
| Injury reports | One injured player | Team, player, position, status (Out, Day-To-Day, Questionable...), fantasy status, injury, body part, side, expected return date, last update time, short and long ESPN comment |

Tennis matches and UFC fights come as games (the two players or fighters fill the home and away fields). Golf tournaments and F1 sessions come as leaderboard rows, one per player or driver.

## Input examples

NBA and Premier League scores from the last 7 days:

```json
{
    "mode": "games",
    "leagues": ["nba", "eng.1"],
    "dateRange": "last7Days"
}
```

Every game of a full season:

```json
{
    "mode": "games",
    "leagues": ["nba"],
    "dateRange": "season",
    "season": 2026,
    "maxItems": 5000
}
```

Box scores and player stats for every NFL game of a week:

```json
{
    "mode": "gameDetails",
    "leagues": ["nfl"],
    "dateRange": "custom",
    "dateFrom": "2026-10-22",
    "dateTo": "2026-10-28"
}
```

Box score and play-by-play for specific games, by ESPN link:

```json
{
    "mode": "gameDetails",
    "gameIds": [
        "https://www.espn.com/nba/game/_/gameId/401909877/nets-celtics",
        "https://www.espn.com/soccer/match/_/gameId/401879268/leeds-united-arsenal"
    ],
    "includePlays": true
}
```

Full schedules of two teams:

```json
{
    "mode": "teamSchedule",
    "leagues": ["nba", "eng.1"],
    "teams": ["Lakers", "https://www.espn.com/soccer/team/_/id/359/arsenal"]
}
```

Current injury reports of the four major US leagues:

```json
{
    "mode": "injuries",
    "leagues": ["nfl", "nba", "mlb", "nhl"]
}
```

Standings, rosters, news and injury reports work the same way: pick the mode and the leagues, and add teams if you want only some of them.

## Output examples

A game (Premier League):

```json
{
    "type": "game",
    "league": "eng.1",
    "leagueName": "English Premier League",
    "sport": "soccer",
    "gameId": "401879268",
    "name": "Leeds United at Arsenal",
    "startTime": "2026-10-10T11:30:00Z",
    "status": "final",
    "statusDetail": "FT",
    "homeTeamName": "Arsenal",
    "homeTeamAbbreviation": "ARS",
    "homeScore": 2,
    "homeRecord": "5-0-1",
    "homeForm": "DWDWW",
    "awayTeamName": "Leeds United",
    "awayScore": 1,
    "winner": "Arsenal",
    "venueName": "Emirates Stadium",
    "venueCity": "London",
    "attendance": 60315,
    "broadcasts": ["USA Net", "Universo"],
    "headline": "Arsenal come from behind to overcome Leeds",
    "scoringSummary": ["55' James Justin (LEE)", "62' Riccardo Calafiori (ARS)", "70' Bruno Guimarães (ARS)"],
    "gameUrl": "https://www.espn.com/soccer/match/_/gameId/401879268/leeds-united-arsenal",
    "scrapedAt": "2026-10-28T11:48:02Z"
}
```

An upcoming game with betting odds (NFL):

```json
{
    "type": "game",
    "league": "nfl",
    "gameId": "401873023",
    "name": "Carolina Panthers at Green Bay Packers",
    "startTime": "2026-10-30T00:15:00Z",
    "week": 8,
    "status": "scheduled",
    "statusDetail": "Thu, October 29th at 8:15 PM EDT",
    "homeTeamName": "Green Bay Packers",
    "homeRecord": "4-3",
    "awayTeamName": "Carolina Panthers",
    "awayRecord": "3-3",
    "venueName": "Lambeau Field",
    "broadcasts": ["Prime Video"],
    "oddsProvider": "Draft Kings",
    "oddsDetails": "GB -3.5",
    "spread": -3.5,
    "overUnder": 47.5,
    "homeMoneyline": -185,
    "awayMoneyline": 154,
    "openingSpread": -7,
    "openingOverUnder": 45.5,
    "gameUrl": "https://www.espn.com/nfl/game/_/gameId/401873023/panthers-packers"
}
```

Game details (shortened, the real record has about 60 team stat fields such as `homeStatFieldGoalsMade` and `awayStatTotalRebounds`):

```json
{
    "type": "gameDetails",
    "league": "nba",
    "gameId": "401909877",
    "name": "Brooklyn Nets at Boston Celtics",
    "statusDetail": "Final/OT",
    "homeTeamName": "Boston Celtics",
    "homeScore": 125,
    "homeLinescores": [26, 30, 30, 31, 8],
    "awayTeamName": "Brooklyn Nets",
    "awayScore": 124,
    "attendance": 19156,
    "officials": ["John Goble", "Jonathan Sterling", "JD Ralls"],
    "homeStatFieldGoalsMade": 42,
    "homeStatFieldGoalsAttempted": 93,
    "homeStatThreePointFieldGoalPct": 27,
    "homeStatPointsInPaint": 52,
    "leaders": ["BOS Points: Jayson Tatum 40", "BKN Rebounds: Michael Porter Jr. 12"],
    "oddsDetails": "BOS -13.5",
    "openingSpread": -11.5,
    "seriesSummary": "BOS leads series 1-0",
    "recapHeadline": "Jayson Tatum hits a buzzer-beating jumper in OT to give the Celtics a 125-124 win over the Nets"
}
```

A player's box score line:

```json
{
    "type": "playerStats",
    "gameId": "401909877",
    "startTime": "2026-10-27T23:30:00Z",
    "gameName": "Brooklyn Nets at Boston Celtics",
    "teamAbbreviation": "BOS",
    "opponent": "Brooklyn Nets",
    "playerId": "4065648",
    "playerName": "Jayson Tatum",
    "position": "F",
    "starter": true,
    "minutes": 42,
    "points": 40,
    "fieldGoalsMade": 10,
    "fieldGoalsAttempted": 20,
    "freeThrowsMade": 18,
    "freeThrowsAttempted": 22,
    "rebounds": 5,
    "assists": 8,
    "plusMinus": 5,
    "playerUrl": "https://www.espn.com/nba/player/_/id/4065648/jayson-tatum"
}
```

A standings row:

```json
{
    "type": "standing",
    "league": "eng.1",
    "season": 2026,
    "seasonName": "2026-27 English Premier League",
    "position": 1,
    "teamName": "Manchester City",
    "gamesPlayed": 8,
    "wins": 7,
    "ties": 0,
    "losses": 1,
    "points": 21,
    "pointsFor": 20,
    "pointsAgainst": 9,
    "pointDifferential": 11,
    "overallRecord": "7-0-1",
    "note": "Champions League"
}
```

A player from a roster:

```json
{
    "type": "player",
    "league": "nfl",
    "teamName": "Green Bay Packers",
    "playerId": "4242390",
    "fullName": "Aaron Banks",
    "jersey": "65",
    "position": "G",
    "positionName": "Guard",
    "positionGroup": "offense",
    "age": 29,
    "dateOfBirth": "1997-09-03",
    "height": "6' 5\"",
    "weightLbs": 325,
    "birthPlace": "Alameda, CA, USA",
    "college": "Notre Dame",
    "experienceYears": 6,
    "injuryStatus": "Questionable",
    "playerUrl": "https://www.espn.com/nfl/player/_/id/4242390/aaron-banks"
}
```

An injury:

```json
{
    "type": "injury",
    "league": "nba",
    "season": "2026-27",
    "teamName": "Atlanta Hawks",
    "teamAbbreviation": "ATL",
    "playerId": "4712863",
    "playerName": "Mouhamed Gueye",
    "position": "F",
    "status": "Out",
    "fantasyStatus": "OUT",
    "injury": "Foot",
    "bodyPart": "Leg",
    "detail": "Fracture",
    "side": "Left",
    "expectedReturn": "2026-11-20",
    "updatedAt": "2026-10-19T19:38:00Z",
    "shortComment": "Gueye underwent surgery Tuesday to repair a fractured left foot that he suffered during a workout last week...",
    "playerUrl": "https://www.espn.com/nba/player/_/id/4712863/mouhamed-gueye"
}
```

A news article:

```json
{
    "type": "article",
    "league": "nba",
    "headline": "Kyrie Irving has found new purpose in Dallas alongside Cooper Flagg",
    "description": "Irving and the Mavericks host the Oklahoma City Thunder on Wednesday at 9:30 p.m. ET on ESPN.",
    "published": "2026-10-28T11:15:57Z",
    "byline": "Tim MacMahon",
    "teams": ["Dallas Mavericks"],
    "athletes": ["Kyrie Irving", "Cooper Flagg"],
    "url": "https://www.espn.com/nba/story/_/id/50298824/kyrie-irving-cooper-flagg-dallas-mavericks-new-line"
}
```

## How much does it cost?

You pay per saved result: **$1.00 per 1,000 results**. There is no start fee and no monthly rental. Every row counts as one result, whatever its type.

| Run | Results | Cost |
|---|---|---|
| NBA and Premier League scores, last 7 days | 64 | $0.06 |
| Box score of one NBA game with player stats | about 30 | $0.03 |
| Same game with play-by-play added | about 600 | $0.60 |
| Every NBA game of the 2025-26 season | 1,401 | $1.40 |
| Every MLB game of 2026 | 2,953 | $2.95 |
| Current Premier League table | 20 | $0.02 |

Set **Max results** or a maximum charge per run in the run options, and the Actor stops when it is reached.

## Limits you should know

- **This is unofficial.** The Actor reads the public JSON data that ESPN's own website and apps load. It is not made by, endorsed by or connected to ESPN. If ESPN changes these feeds, the Actor may need an update.
- **Dates follow US Eastern time.** ESPN puts a game on the US Eastern calendar day. A Premier League match at 11:30 UTC is on the same day, but a late NBA game at 02:00 UTC belongs to the previous day. `startTime` is always in UTC.
- **Big seasons take a minute or two.** MLB, college football and college basketball are loaded day by day because ESPN's monthly lists are too large or cut off for them. A full MLB season took 97 seconds and a full college football season 104 seconds in our tests. Other leagues load a season in under 10 seconds.
- **Game details are for team sports.** Tennis, golf, F1 and UFC are covered in Games, Standings (tennis rankings, F1 standings) and News, not in box scores. F1 rows give the finishing order of qualifying, sprint and race sessions (practice is skipped), without lap times. Golf rows give score to par and round scores, not hole by hole.
- **Betting odds appear only when ESPN shows them.** That is usually one sportsbook line (DraftKings) for US leagues, close to game time. Soccer games rarely have odds.
- **Soccer player stats are basic.** Goals, assists, shots, saves, fouls and cards per player. US sports have full box score lines.
- **Rosters are current only.** ESPN does not publish past rosters, so the Season field is ignored in Rosters mode.
- **News is the latest 50 articles** per league or per team. There is no archive search.
- **Injury reports are the current list only.** ESPN shows who is injured now, not past injuries, so schedule the Actor daily to build a history. The US leagues (NFL, NBA, WNBA, MLB, NHL, college football and basketball) have full reports; soccer leagues usually return none.
- **Season numbers follow ESPN.** NBA, NHL and college basketball use the year the season ends (2025-26 = 2026). Soccer uses the year it starts (2025-26 = 2025). NFL, MLB, WNBA and college football use the calendar year.
- **Records in soccer are wins-draws-losses** ("5-0-1" means 5 wins, 0 draws, 1 loss), as ESPN writes them.

---

Full documentation, all input options and a free trial: **[ESPN Scraper on Apify](https://apify.com/pipiagent/espn-scraper)**
