import requests
import json
import os
from datetime import datetime, timezone

API_KEY = "9160f5c9b2a740dbac821f127b43ab60"
BASE_URL = "https://api.football-data.org/v4"


headers = {"X-Auth-Token": API_KEY}

response = requests.get(f"{BASE_URL}/competitions/WC/matches", headers=headers)
data = response.json()

# Create the folder to store raw files if folder doesn't exist yet
os.makedirs("data/raw", exist_ok=True)

# Give the file a timestamp in its name so each run creates a new file
timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
filename = f"data/raw/matches_{timestamp}.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved {len(data['matches'])} matches to {filename}")