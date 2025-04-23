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

    response = requests.get(AIRTABLE_URL, headers=HEADERS)
    if response.status_code != 200:
        return f"Error fetching data: {response.status_code}"


    data = response.json()
    records = data.get("records", [])

#Fields we want displayed
    desired_fields = [
        "First Name",
        "Last Name",
        "Graduation Year",
        "Job Title",
        "PredictedCategory",
        "LinkedIn Profile",
    ]

#Sort  alumni by full name 
    sorted_records = sorted(
        records,
        key=lambda rec: rec
            .get("fields", {})
            .get("FullName", "")
            .lower()
    )

    alumni_data = [
        {
            field: rec.get("fields", {}).get(field, "N/A")
            for field in desired_fields
        }
        for rec in sorted_records
    ]
   

   
    return render_template("index.html", alumni=alumni_data, columns=desired_fields)

if __name__ == "__main__":
    app.run(debug=True)
