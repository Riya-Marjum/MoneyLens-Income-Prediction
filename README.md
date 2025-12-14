# 💰 MoneyLens – Income Prediction App

## 🖼️ App Preview

Below is a preview of the **MoneyLens Streamlit application**:

![MoneyLens App Screenshot](Screenshot.png)

MoneyLens is a machine learning–based web application that predicts whether a person earns **more than $50K per year or ≤ $50K**, using demographic and employment-related data.

The project is built using **Python, XGBoost, and Streamlit**, and is trained on the **UCI Adult Census Income Dataset**.

---

## 🔥 Project Highlights
- End-to-end ML pipeline: **Data Cleaning → EDA → Model Training → Evaluation → Deployment**
- Compared multiple classification models
- Best-performing model deployed using **Streamlit**
- Clean and interactive UI for real-time predictions

---

## 🚀 Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Joblib  
- **Visualization:** Matplotlib, Seaborn  
- **Deployment:** Streamlit  
- **Training Platform:** Google Colab  

---

## 🤖 Machine Learning Models Used
- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- Decision Tree  
- Random Forest  
- Gradient Boosting  
- XGBoost  

---

## 🏆 Best Model Performance
- **Model:** Gradient Boosting / XGBoost  
- **Accuracy:** ~84%  
- **Balanced precision and recall**, suitable for income classification

---

## 📊 Dataset Information
- **Source:** UCI Adult Census Income Dataset  
- **Target Variable:** Income (`>50K` or `≤50K`)  

### Features Used
- Age  
- Workclass  
- Education & Education Number  
- Marital Status  
- Occupation  
- Relationship  
- Race  
- Sex  
- Capital Gain & Capital Loss  
- Hours per Week  
- Native Country  
🏗 How to Run Locally
1️⃣ Run Notebook (Model Training)

Open Income_Prediction .ipynb in Google Colab

Execute cells sequentially:

Data loading

Preprocessing

Model training & evaluation

2️⃣ Run Streamlit App
pip install -r requirements.txt
streamlit run app.py
---

## 📁 Project Structure
