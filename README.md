# fraud-detection-ml
End-to-end machine learning project for detecting fraudulent financial transactions using Python and scikit-learn.

Fraud Detection Using Machine Learning

Full Python Data Science Project

Overview


  This repository presents an end-to-end machine learning solution for detecting fraudulent financial transactions.

   The project demonstrates a production-oriented data science workflow, covering data preprocessing, feature engineering, model training using pipelines, and deployment through a lightweight inference application.


The solution is designed with enterprise banking and financial services use cases in mind, emphasizing reproducibility, interpretability, and deployment readiness.

Business Context

Financial institutions process millions of transactions every day. Even a small percentage of fraudulent activity can result in significant financial loss, reputational damage, and regulatory risk.


Objective


To classify transactions as fraudulent or legitimate with a focus on:


  Reducing false negatives (missed fraud cases)
   

   Maintaining model interpretability
   

   Ensuring consistent and reliable inference behavior
   

   Supporting deployment in enterprise environments
   

Technical Approach

  Problem Type: Binary Classification


Machine Learning Framework: Scikit-learn


Model: Logistic Regression (interpretable baseline model)


Preprocessing


One-Hot Encoding for categorical features


Feature scaling for numerical variables


Pipeline Design


End-to-end preprocessing and modeling implemented using:


Pipeline


ColumnTransformer


Model Persistence


Trained pipeline serialized using Joblib



This design ensures that the same transformations applied during training are consistently applied during inference, which is critical in regulated and large-scale environments.



System Architecture


Raw Transaction Data

        ↓
Exploratory Data Analysis

        ↓
Feature Engineering

        ↓
Preprocessing & Modeling Pipeline

        ↓
Model Evaluation

        ↓
Serialized Model Artifact

        ↓
Streamlit Inference Application


Application Output (Inference UI)


The project includes a Streamlit-based inference application that allows users to:


Enter transaction details manually


Perform real-time fraud prediction


View clear and interpretable prediction results


This interface simulates a fraud screening tool used by operational or risk teams.


Project Structure

fraud-detection-ml/
│
├── AIML Dataset.csv               # Transaction dataset
├── Analysis_Model.ipynb           # EDA, feature engineering, model training
├── app.py                         # Streamlit inference application
├── fraud_detection_pipeline.pkl   # Trained and serialized ML pipeline

Dataset Summary


Each transaction record contains:


Transaction type


Transaction amount


Sender balance (before and after transaction)


Receiver balance (before and after transaction)


Target Variable


isFraud


1 → Fraudulent transaction


0 → Legitimate transaction


Model Evaluation Considerations


Evaluation focuses on business-relevant risk metrics, including:


Precision and Recall


Confusion Matrix analysis


Interpretation of errors from a financial risk perspective:


False Negatives: Direct financial loss risk


False Positives: Customer experience and operational cost impact


Deployment


A lightweight Streamlit application is included to demonstrate:


Real-time inference using trained ML pipelines

Integration of data science models into applications


Deployment-ready artifacts suitable for enterprise workflows

Setup Instructions

Clone the Repository

git clone https://github.com/your-username/fraud-detection-ml.git

cd fraud-detection-ml


Install Dependencies

pip install pandas numpy scikit-learn streamlit matplotlib seaborn joblib


Run the Application

streamlit run app.py


Engineering Best Practices Demonstrated

*output*

<img width="1893" height="952" alt="output" src="https://github.com/user-attachments/assets/c3e22b6f-3d83-4121-a794-8a6fa8b863f4" />


End-to-end reproducibility


Pipeline-based machine learning design


Clean separation of training and inference logic


Interpretable baseline modeling


Maintainable and enterprise-friendly code structure


Potential Enhancements


Tree-based ensemble models (Random Forest, Gradient Boosting)


Handling class imbalance (SMOTE, cost-sensitive learning)


Model explainability (SHAP, feature attribution)


Cloud deployment with CI/CD pipelines


Real-time transaction ingestion and monitoring


Author

Vignesh Raj
Machine Learning & Data Science Practitioner
India
