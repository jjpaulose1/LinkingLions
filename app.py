from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Airtable configuration
AIRTABLE_BASE_ID = "app59RhWQEcM6gMLt"
AIRTABLE_TABLE_NAME = "Imported table"
AIRTABLE_API_KEY = "patvoUhA9bzbZjhQh.bec53ab20727cde451c5dae63341aa770cc07b462eb587356abeaab6d4e206d0"
AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
HEADERS = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}"
}


@app.route("/")
def index():
    # Fetch data from Airtable
    response = requests.get(AIRTABLE_URL, headers=HEADERS)
    if response.status_code == 200:
        records = response.json().get("records", [])
        # Extract fields
        desired_fields = ["FullName", "GraduationYear2", "JobTitle", "LinkedInUrl", "Rating"]
        alumni_data = [
            {field: record["fields"].get(field, "N/A") for field in desired_fields}
            for record in records
        ]
        
        return render_template("index.html", alumni=alumni_data)
    else:
        return f"Error fetching data: {response.status_code}"

if __name__ == "__main__":
    app.run(debug=True)
desired_fields = ["FullName", "GraduationYear2", "JobTitle", "LinkedInUrl", "Rating"]
alumni_data = [
    {field: record["fields"].get(field, "N/A") for field in desired_fields}
    for record in records
]


"""
Testing 
# Debugging and testing the Airtable endpoint
response = requests.get(AIRTABLE_URL, headers=HEADERS)
print(response.status_code)
print(response.json())

print("Testing Airtable API...")
response = requests.get(AIRTABLE_URL, headers=HEADERS)
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Data:", response.json())
else:
    print("Error:", response.text)

"""

