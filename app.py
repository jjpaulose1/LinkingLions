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

def fetch_all_records():
    all_recs = []
    params = {
        'pageSize': 100,
        # 'view': 'All Alumni'      # <-- if you need a specific view
    }
    while True:
        resp = requests.get(AIRTABLE_URL, headers=HEADERS, params=params)
        data = resp.json()
        all_recs.extend(data.get('records', []))
        if 'offset' in data:
            params['offset'] = data['offset']
        else:
            break
    return all_recs


@app.route("/")
def index():
    records = fetch_all_records()
    #Fields we want displayed
    desired_fields = [
        "First Name",
        "Last Name",
        "Graduation Year",
        "Job Title",
        "PredictedCategory",
        "LinkedIn Profile",
    ]

    alumni_data = []
    for rec in records: 
        fields = rec.get("fields", {})
        filtered = {
            key: fields.get(key, "N/A")
            for key in desired_fields
        }
        alumni_data.append(filtered)
    alumni_data.sort(key = lambda x: (x["Last Name"].lower(), x["First Name"].lower()))


    return render_template("index.html", alumni = alumni_data, columns = desired_fields)


if __name__ == "__main__":
    app.run(debug=True)
    print("App is running")
