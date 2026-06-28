#!/var/ossec/framework/python/bin/python3

import json
import sys
import requests

THEHIVE_URL = "http://host.docker.internal:9000"   # For WSL
THEHIVE_API_KEY = "w3pQVoPu4enQBahtG1otraNr/JHB4A9L"

def main():
    alert_file = sys.argv[1]
    with open(alert_file) as f:
        alert = json.load(f)

    thehive_alert = {
        "title": alert.get("rule", {}).get("description", "Wazuh Alert"),
        "description": json.dumps(alert, indent=2),
        "severity": min(alert.get("rule", {}).get("level", 3), 5),
        "tags": ["wazuh", "siem"],
        "source": "Wazuh"
    }

    headers = {
        "Authorization": f"Bearer {THEHIVE_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(f"{THEHIVE_URL}/api/alert", json=thehive_alert, headers=headers)
        print(f"TheHive response: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
