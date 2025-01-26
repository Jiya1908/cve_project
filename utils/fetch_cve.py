import requests
from models import CVE
from database import db

API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def fetch_cve_data(start_index=0, results_per_page=10):
    params = {
        "startIndex": start_index,
        "resultsPerPage": results_per_page
    }
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        cve_list = response.json().get('vulnerabilities', [])
        for item in cve_list:
            cve_data = item['cve']
            cve = CVE(
                cve_id=cve_data['id'],
                description=cve_data['descriptions'][0]['value'],
                severity=cve_data.get('metrics', {}).get('cvssMetricV2', {}).get('baseSeverity', "N/A"),
                published_date=cve_data['published'],
                last_modified_date=cve_data['lastModified'],
            )
            db.session.merge(cve)  # Prevent duplicates
        db.session.commit()
    else:
        print(f"Failed to fetch CVE data: {response.status_code}")
