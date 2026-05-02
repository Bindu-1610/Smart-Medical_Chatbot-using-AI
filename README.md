# 🩺 Smart Medical Analysis Chatbot using AI

## 📌 Project Overview

The **Smart Medical Analysis Chatbot** is an Artificial Intelligence based healthcare assistant that predicts possible diseases based on user symptoms and suggests medical precautions.

The system applies **Machine Learning classification techniques** to analyze symptoms entered by users and provide preliminary health guidance.

This project is implemented using:

* Python
* Machine Learning
* Jupyter Notebook
* Streamlit Web Application
* Medical Dataset Analysis
---
## 🎯 Objectives

* Predict diseases based on symptoms using AI.
* Provide precautionary medical suggestions.
* Develop an interactive healthcare chatbot system.
* Demonstrate Machine Learning application in healthcare.
* Build both notebook-based and web-based implementations.
--
## 🧠 Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Jupyter Notebook
* Decision Tree Classifier
---
## 📊 Dataset Used

The project uses medical symptom datasets inspired from publicly available healthcare datasets.

### Dataset Files

* **Training.csv** → Disease training dataset containing symptoms and prognosis.
* **symptom_precaution.csv** → Medical precaution recommendations.

### Dataset Structure

Each row represents:

* Symptoms (binary values: 1 = present, 0 = absent)
* Disease label (prognosis)

Example:

| fever | cough | fatigue | prognosis |
| ----- | ----- | ------- | --------- |
| 1     | 1     | 0       | Flu       |
---
## ⚙️ System Workflow

1. Load medical dataset.
2. Preprocess symptoms data.
3. Train Machine Learning model.
4. Accept user symptoms.
5. Predict disease.
6. Retrieve precautions.
7. Display medical suggestion.
---
## 🤖 Machine Learning Model

The system uses a **Decision Tree Classifier** because:

* Suitable for classification problems.
* Works efficiently with binary symptom data.
* Easy to interpret and explain.
* Requires less computational power.
* Ideal for academic AI projects.
---
## 📒 Jupyter Notebook Implementation

The notebook version performs:

* Data loading
* Data preprocessing
* Model training
* Accuracy evaluation
* Disease prediction testing

Run using:

```bash
jupyter notebook medical_chatbot.ipynb
```

---

## 🌐 Streamlit Web Application (VS Code)

The Streamlit application provides an interactive user interface.

### Features

* Symptom selection interface
* Real-time disease prediction
* Precaution recommendation system
* User-friendly medical chatbot interaction

Run application:

```bash
streamlit run app.py
```

## 📁 Project Structure

```
SmartMedicalChatbot/
│
├── medical_chatbot.ipynb
├── app.py
├── Training.csv
├── Testing.csv
├── symptom_precaution.csv
└── README.md
```
## ▶️ Installation Guide

### Step 1: Clone or Download Project
```
git clone <repository-link>
```
### Step 2: Install Dependencies
```
pip install pandas scikit-learn streamlit
```
### Step 3: Run Notebook
```
jupyter notebook
```
### Step 4: Run Web Application
```
streamlit run app.py
```
---

## ✅ Features

* AI Disease Prediction
* Symptom Analysis
* Medical Precaution Suggestion
* Notebook + Web Application
* Healthcare Decision Support System

---

## ⚠️ Disclaimer

This system is designed for **educational and research purposes only**.
The predictions are AI-generated and should not replace professional medical consultation.

---

## 🚀 Future Enhancements

* Voice-based medical assistant
* Deep learning disease prediction
* Doctor recommendation system
* Cloud deployment
* Patient history database
* Mobile healthcare application

---

## 👩‍💻 Author
Smart Medical Analysis Chatbot -- MODEM HIMABINDU
---

---
