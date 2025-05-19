import requests
import os
from dotenv import load_dotenv
import csv

load_dotenv()

API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")
BASE_URL = "https://api.football-data.org/v4/competitions/PL/standings"

headers = {"X-Auth-Token": API_KEY}


def scrape_results(filename):
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code != 200:
        print("Error")
        return

    data = response.json()
    standings = data["standings"][0]["table"]

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


if __name__ == "__main__":
    scrape_results("..\\results\\PL Standings.csv")
