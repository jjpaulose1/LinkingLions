from flask import Flask, render_template, request
import requests
import os

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
    data = response.json()
    records = data.get("records",[])
    
    if response.status_code != 200:
       return f"Error fetching data" {reponse.status_code}"
    desired fields - [
        "FullName", "GraduationYear2", "JobTitle", "LinkedInUrl", "Rating"
    ]

    alumni_data = [
        {field: record.get("fields", {}).get(field, "N/A")
         for field in desired_fields}
        for record in records
    ]
        
        return render_template("index.html", alumni=alumni_data)


if __name__ == "__main__":
    import pprint
    print("Testing Airtable endpoint..."
    resp = requests.get(AIRTABLE_URL, headers = HEADERS)
    pprint.pprint({
        "status": resp.status_code,
        "payload": resp.json()
        })
app.run(debug=True) 


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

