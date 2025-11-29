# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn
import os

# 1. Initialize API
app = FastAPI(
    title="Loan Approval Prediction API",
    description="A Machine Learning API to predict loan approval/rejection based on applicant data.",
    version="1.0"
)

# 2. Load the Champion Model
# We check if the file exists to avoid crashing on startup if the path is wrong
MODEL_PATH = 'loan_approval_pipeline.pkl'

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None
    print(f"WARNING: '{MODEL_PATH}' not found. API will run but predictions will fail.")

# 3. Define the Input Data Schema (JSON Structure)
class LoanApplication(BaseModel):
    loan_amount: float
    int_rate: float
    annual_income: float
    dti: float
    term: float
    emp_length: float
    total_acc: float
    installment: float
    grade: str
    home_ownership: str
    purpose: str
    verification_status: str
    application_type: str
# Add a basic home page    
@app.get("/")
def home():
    return {"message": "Loan Prediction API is Running!"}
    
# 4. The Prediction Endpoint
@app.post("/predict")
def predict_loan_approval(application: LoanApplication):
    if model is None:
        raise HTTPException(status_code=500, detail="Model file not found on server.")
    
    try:
        # Convert JSON input (Pydantic model) to a pandas DataFrame
        # The keys must match the column names your model was trained on!
        data_dict = application.dict()
        df_input = pd.DataFrame([data_dict])
        
        # Make the prediction
        # [0] selects the first (and only) result from the array
        prediction = model.predict(df_input)[0]
        
        # Get the probability (confidence score)
        # predict_proba returns [[prob_0, prob_1]], we want prob_1 (Approval probability)
        probability = model.predict_proba(df_input)[0][1]
        
        # Interpret result
        status = "Approved" if prediction == 1 else "Rejected"
        
        return {
            "status": status,
            "approval_probability": f"{probability:.2%}",
            "model_used": "Logistic Regression (Champion)"
        }
    
    except Exception as e:
        # If something goes wrong (e.g., data format error), return a clear message
        raise HTTPException(status_code=400, detail=str(e))

# Entry point for local debugging
if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)
