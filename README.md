Parkinson’s Disease Progression Prediction Using Machine Learning

Master’s Research Project – MSc Data Analytics, Dublin Business School

Project Overview

This project focuses on predicting Parkinson’s disease progression using voice-based biomedical data and machine learning techniques.
The goal was to explore how data analytics and predictive models can support healthcare analysis by estimating Motor UPDRS and Total UPDRS scores.

The project follows a complete end-to-end data analytics lifecycle, from data understanding to model evaluation and interpretation.

Objectives

Analyse real-world biomedical voice data related to Parkinson’s disease

Build machine learning regression models to predict disease progression

Compare traditional machine learning and deep learning approaches

Interpret model behaviour using Explainable AI techniques

Demonstrate predictions using a simple Python-based application

Methodology

The project was carried out using the CRISP-DM framework, including:

Data understanding and exploratory data analysis (EDA)

Data cleaning, feature selection, and standardisation

Model development and training

Model evaluation using performance metrics

Model interpretability and explainability

Models Implemented

Voting Regressor

Long Short-Term Memory (LSTM)

Gated Recurrent Unit (GRU)

Model Evaluation Metrics

R² Score

Root Mean Squared Error (RMSE)

Mean Absolute Error (MAE)

The Voting Regressor achieved the best overall performance across prediction tasks.

Explainable AI

To improve transparency and interpretability, SHAP (SHapley Additive exPlanations) was used to analyse feature importance and understand how different variables influenced model predictions.

Prototype Application

A Python Tkinter desktop application was developed to demonstrate real-time prediction of UPDRS scores using the trained model.

Pre-trained model files are stored in the models/ directory and are used directly by the application.

Project Structure
parkinsons-disease-progression-prediction/
├── notebooks/        # Jupyter notebooks (EDA, modeling, evaluation)
├── src/              # Python source code
├── app/              # Tkinter application
├── models/           # Trained model and scaler (.pkl files)
├── data/             # Dataset (if included) or data references
├── images/           # Plots and result visualisations
├── docs/             # Project report and presentation
├── README.md
└── requirements.txt

Dataset

Parkinson’s Telemonitoring Dataset

Source: UCI Machine Learning Repository

The dataset contains biomedical voice measurements collected from Parkinson’s disease patients.

Technologies Used

Python

Pandas, NumPy

Scikit-learn

TensorFlow

SHAP

Matplotlib, Seaborn

Tkinter

How to Run the Application

Clone the repository:

git clone https://github.com/your-username/parkinsons-disease-progression-prediction.git


Install required dependencies:

pip install -r requirements.txt


Run the application:

python app/app.py

Key Learning Outcomes

Practical experience applying machine learning to healthcare data

Understanding the importance of model interpretability in sensitive domains

Experience working with real-world datasets and evaluation metrics

Improved skills in structuring and presenting analytical projects
