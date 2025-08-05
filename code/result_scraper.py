import requests
import os
from dotenv import load_dotenv
import csv
from collections import defaultdict
from openpyxl import Workbook
from pathlib import Path

load_dotenv()

API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")
BASE_URL = "https://api.football-data.org/v4"

HEADERS = {"X-Auth-Token": API_KEY}


def save_current_league_table(filename):
    url = f"{BASE_URL}/competitions/PL/standings"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception("Failed to get standings")

    standings = response.json()["standings"][0]["table"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Position",
                "Team",
                "Played",
                "Won",
                "Draw",
                "Lost",
                "Points",
                "GF",
                "GA",
                "GD",
            ]
        )
        for cur_team in standings:
            writer.writerow(
                [
                    cur_team["position"],
                    cur_team["team"]["shortName"],
                    cur_team["playedGames"],
                    cur_team["won"],
                    cur_team["draw"],
                    cur_team["lost"],
                    cur_team["points"],
                    cur_team["goalsFor"],
                    cur_team["goalsAgainst"],
                    cur_team["goalDifference"],
                ]
            )


def save_latest_matchday(filename):
    print(filename.resolve())
    url = f"{BASE_URL}/competitions/PL/matches?season=2024"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception("Failed to get matches")

    matches = response.json()["matches"]
    grouped_matches = defaultdict(list)
    for match in matches:
        md = match.get("matchday")
        if md is not None:
            grouped_matches[md].append(match)

    wb = Workbook()
    wb.remove(wb.active)

    for matchday, matches in sorted(grouped_matches.items()):
        sheet = wb.create_sheet(title=f"Matchday {matchday}")
        sheet.append(["Home Team", "Away Team", "Score", "Status"])

        for match in matches:
            home = match["homeTeam"]["shortName"]
            away = match["awayTeam"]["shortName"]
            status = match["status"]

            if status == "FINISHED":
                score = f"{match['score']['fullTime']['home']} - {match['score']['fullTime']['away']}"
            else:
                score = "vs"
            sheet.append([home, away, score, status])
    wb.save(filename)


if __name__ == "__main__":
    # save_current_league_table(Path("results") / "PL" / "PL Standings.csv")
    save_latest_matchday(Path("results") / "PL" / "Fixtures.xlsx")
