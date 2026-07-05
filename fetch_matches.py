import requests

API_KEY = "9160f5c9b2a740dbac821f127b43ab60"
BASE_URL = "https://api.football-data.org/v4"

headers = {
    "X-Auth-Token": API_KEY
}

response = requests.get(f"{BASE_URL}/competitions/WC/matches", headers=headers)

data = response.json()

# Printing the first match to see what the data looks like
import json
print(json.dumps(data["matches"][0], indent=2))