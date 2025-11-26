# test_api.py
import requests
import json

# The URL of your local API
url = "http://127.0.0.1:8000/predict"

# Sample Applicant Data (A "Good" Candidate)
applicant_data = {
    "loan_amount": 15000,
    "int_rate": 0.08,           # Low interest rate (good sign)
    "annual_income": 85000,     # High income
    "dti": 12.5,                # Low Debt-to-Income
    "term": 36,
    "emp_length": 8,
    "total_acc": 15,
    "installment": 450.50,
    "grade": "A",
    "home_ownership": "MORTGAGE",
    "purpose": "debt_consolidation",
    "verification_status": "Source Verified",
    "application_type": "INDIVIDUAL"
}

# Send POST request
response = requests.post(url, json=applicant_data)

# Print the result
print("Status Code:", response.status_code)
print("API Response:", response.json())