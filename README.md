Parkinson’s Disease Progression Prediction

MSc Data Analytics – Dublin Business School

Overview

This project implements machine learning regression models to predict Parkinson’s disease progression using voice-based biomedical data. The models estimate Motor UPDRS and Total UPDRS scores based on features extracted from patient voice recordings.

Methodology

CRISP-DM analytics lifecycle

Data cleaning, feature selection, and standardisation

Exploratory Data Analysis (EDA)

Model training and evaluation

Model interpretability using Explainable AI

Models

Voting Regressor

LSTM

GRU

Evaluation Metrics

R²

RMSE

MAE

The Voting Regressor achieved the best overall performance across both prediction targets.

Explainability

SHAP (SHapley Additive Explanations) was used to analyse feature importance and improve model interpretability.

Application

A Python-based Tkinter desktop application demonstrates real-time prediction using pre-trained models stored in the models/ directory.

Project Structure
├── notebooks/    # EDA, modeling, evaluation
├── src/          # Core Python logic
├── app/          # Tkinter application
├── models/       # Trained .pkl files
├── images/       # Result visualisations
├── docs/         # Report and presentation
└── requirements.txt

Dataset

Parkinson’s Telemonitoring Dataset

Source: UCI Machine Learning Repository

Technologies

Python, Pandas, NumPy, Scikit-learn, TensorFlow, SHAP, Matplotlib, Tkinter

Run Instructions
pip install -r requirements.txt
python app/app.py

Author

Yadav Vijayan
MSc Data Analytics, Dublin Business School
