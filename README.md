☁️ Cloud-Optimized Diabetes Mellitus Prediction Platform

A cloud-powered, machine learning–driven application that predicts diabetes mellitus risk using AWS SageMaker, EC2, and S3. Includes a lightweight Flask-based web interface for real-time predictions and a scalable deployment architecture.

---

🧠 Project Overview

This system integrates AWS cloud services and machine learning to build a secure and scalable platform that predicts diabetes risk from user-inputted health data. The application is deployed on AWS infrastructure and interacts with a machine learning model in real time via a web interface.

---

🎯 Objectives

- Predict the risk of diabetes using advanced machine learning models.
- Build a secure, scalable solution using AWS services.
- Offer real-time predictions through a simple, user-friendly web application.
- Ensure end-to-end cloud-based deployment using EC2, S3, and SageMaker.

---

🛠️ Tech Stack

| Category          | Tools/Technologies                              |
|-------------------|--------------------------------------------------|
| Programming       | Python                                           |
| Machine Learning  | scikit-learn, XGBoost, Random Forest             |
| Web Framework     | Flask                                            |
| Cloud Infrastructure | AWS SageMaker, EC2, S3                          |
| Front-End         | HTML, CSS                                        |
| Deployment Tools  | GitHub, WinSCP                                   |

---

📊 Machine Learning Models Evaluated

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Naive Bayes
- Support Vector Machine (SVM)
- XGBoost (Accuracy: **95.50%**)
- Random Forest ✅ (Best Accuracy: **97.15%**)
- Gradient Boosting

---

📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

🧩 System Architecture

User Input → Flask Web App (EC2) → AWS SageMaker Model → Prediction Output ↑ ↓ HTML UI Model + Data in S3

