# 🏦 Loan Approval Prediction System

## 📖 Executive Summary

Financial institutions often rely on manual or rigid rule-based systems to approve loans, leading to inefficiencies and potential bias.  
This project implements an **End-to-End Machine Learning Pipeline** to automate the credit decisioning process.

Using **38,000+ historical loan records**, we developed a predictive model that identifies high-risk applicants with high precision—reducing default rates while streamlining approvals for creditworthy customers.

---

## 🛠️ Project Architecture

The solution is built with **three core components**:

1. **Data Science Pipeline (`.ipynb`)**  
   - Data cleaning, EDA, feature engineering, model training.

2. **Machine Learning Model (`.pkl`)**  
   - Serialized Logistic Regression pipeline (**Champion Model**).

3. **REST API (`main.py`)**  
   - FastAPI service for real-time credit decisions.

---

## ⭐ Key Features

- **Robust Preprocessing**: Automated missing value handling, outlier detection, and categorical encoding.  
- **Leakage Prevention**: Removed future-looking fields (e.g., `total_payment`, `recoveries`).  
- **Explainability**: SHAP values included to justify each decision.  
- **Deployment Ready**: Packaged with a lightweight FastAPI server.

---

## 📊 Model Performance

Four algorithms were evaluated (Logistic Regression, Random Forest, XGBoost, SVM).  
**Logistic Regression** was selected as the Champion Model for its robustness and interpretability.

| Metric | Score |
|--------|--------|
| **ROC-AUC** | 0.72 – 0.75 |
| **Precision (Bad Loans)** | High |
| **Recall (Good Loans)** | Balanced |

### Top Predictive Features
- **Interest Rate** – Strongest correlation with default risk.  
- **DTI (Debt-to-Income)** – High values indicate potential repayment issues.  
- **Annual Income** – Higher income increases approval likelihood.  

---

## 🚀 Getting Started

### **Prerequisites**
- Python **3.8+**
- `pip` package manager


cd loan-approval-prediction

