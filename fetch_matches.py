import requests

API_KEY = "9160f5c9b2a740dbac821f127b43ab60"
BASE_URL = "https://api.football-data.org/v4"

headers = {
    "X-Auth-Token": API_KEY
}

response = requests.get(f"{BASE_URL}/competitions/WC/matches", headers=headers)

data = response.json()

for match in data["matches"]:
    home = match["homeTeam"]["name"] or "TBD"
    away = match["awayTeam"]["name"] or "TBD"
    home_score = match["score"]["fullTime"]["home"]
    away_score = match["score"]["fullTime"]["away"]
    status = match["status"]

    if home_score is None:
        score = "vs"
    else:
        score = f"{home_score} - {away_score}"

    print(f"{home} {score} {away} ({status})")