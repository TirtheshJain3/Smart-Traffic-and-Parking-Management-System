from flask import Flask, jsonify
import requests

app = Flask(__name__)

TOMTOM_API_KEY = "API_KEY"

# Solapur bounding box (south, west, north, east)
BBOX = "17.55,75.80,17.75,76.00"

@app.route("/traffic-incidents")
def traffic_incidents():
    url = (
        "https://api.tomtom.com/traffic/services/5/incidentDetails"
        f"?key={TOMTOM_API_KEY}"
        f"&bbox={BBOX}"
        "&language=en-GB"
        "&timeValidityFilter=present"
    )

    response = requests.get(url)
    data = response.json()

    incidents_list = []

    if "incidents" in data:
        for inc in data["incidents"]:
            incidents_list.append({
                "id": inc.get("id"),
                "type": inc.get("iconCategory"),
                "description": inc.get("description", {}).get("value"),
                "severity": inc.get("magnitudeOfDelay"),
                "geometry": inc.get("geometry", {}).get("coordinates")
            })

    return jsonify({
        "city": "Solapur",
        "count": len(incidents_list),
        "incidents": incidents_list
    })

if __name__ == "__main__":
    app.run(debug=True)


