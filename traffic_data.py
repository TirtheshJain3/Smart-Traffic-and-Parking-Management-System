import requests
import json
from datetime import datetime

TOMTOM_API_KEY = "JxdohUdoPZSwqUy9a4NGKmWJemOFicDG"

# Solapur bounding box
BBOX = "17.55,75.80,17.75,76.00"  # south,west,north,east

URL = (
    "https://api.tomtom.com/traffic/services/5/incidentDetails"
    f"?key={TOMTOM_API_KEY}"
    f"&bbox={BBOX}"
    "&language=en-GB"
    "&timeValidityFilter=present"
)

print("Fetching traffic incidents...")

response = requests.get(URL, timeout=10)
response.raise_for_status()
data = response.json()

incidents = []

for inc in data.get("incidents", []):
    incidents.append({
        "id": inc.get("id"),
        "description": inc.get("properties", {}).get("description"),
        "coordinates": inc.get("geometry", {}).get("coordinates")
    })

output = {
    "city": "Solapur",
    "generated_at": datetime.now().isoformat(),
    "total_incidents": len(incidents),
    "incidents": incidents
}

with open("traffic_incidents.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print(f"Saved {len(incidents)} incidents")

