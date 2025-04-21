from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Airtable configuration
AIRTABLE_BASE_ID = "app59RhWQEcM6gMLt"
AIRTABLE_TABLE_NAME = "Imported table"
AIRTABLE_API_KEY = "patvoUhA9bzbZjhQh.bec53ab20727cde451c5dae63341aa770cc07b462eb587356abeaab6d4e206d0"
AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
HEADERS = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}

@app.route("/")
def index():
    # Fetch data
    response = requests.get(AIRTABLE_URL, headers=HEADERS)
    if response.status_code != 200:
        return f"Error fetching data: {response.status_code}"

    data = response.json()
    records = data.get("records", [])
#Fields we want
    desired_fields = [
        "FullName",
        "GraduationYear2",
        "JobTitle",
        "LinkedInUrl",
        "Rating",
    ]

    alumni_data = [
        {
            field: record.get("fields", {}).get(field, "N/A")
            for field in desired_fields
        }
        for record in records
    ]

    return render_template("index.html", alumni=alumni_data)


if __name__ == "__main__":
    import pprint

    # Testing endpoint
    print("Testing Airtable endpoint…")
    resp = requests.get(AIRTABLE_URL, headers=HEADERS)
    pprint.pprint({
        "status": resp.status_code,
        "payload": resp.json(),
    })

    # Start Flask in debug mode
    app.run(debug=True)


