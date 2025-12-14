# 💰 MoneyLens: Income Prediction Tool

**Python | Streamlit | Machine Learning**

MoneyLens is a machine learning–powered web application that predicts whether a person earns **more than $50K per year or ≤ $50K**, based on demographic and employment attributes.  
The model is trained on the **UCI Adult Census Income Dataset** and deployed using **Streamlit** for real-time predictions.

---

## 🔥 Project Highlights

- Developed as part of my **AI/ML Internship Project at ICT Academy**
- End-to-end ML pipeline: **Data Cleaning → EDA → Model Training → Evaluation → Deployment**
- Interactive **Streamlit UI** for real-time income prediction
- Multiple ML models compared to select the best-performing one

---

## 🚀 Live Demo

👉 **Try the App Here:**  
*(Add Streamlit Cloud link after deployment)*

---

## 🖼️ App Preview

Below is a preview of the **MoneyLens Streamlit application**:

![MoneyLens App Screenshot](Moneylens_ui.png)

> 📌 Make sure the image file is named **`screenshot.png`** and is in the **same folder as `README.md`**

---

## 🔧 Tools & Libraries

### Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn

### Deployment
- Streamlit

### Platform
- Google Colab (model training)
- Local system / Streamlit Cloud (deployment)

---

## 🤖 Machine Learning Models Used

| Model | Description |
|------|------------|
| Logistic Regression | Baseline linear classifier |
| k-Nearest Neighbors (KNN) | Distance-based classifier |
| Support Vector Machine (SVM) | Kernel-based non-linear classifier |
| Decision Tree | Interpretable tree-based model |
| Random Forest | Ensemble of decision trees |
| Gradient Boosting | Sequential boosting algorithm |
| XGBoost | Optimized gradient boosting |

---

## 🏆 Best Performing Model

| Metric | Value |
|------|------|
| Model | Gradient Boosting |
| Accuracy | ~83–84% |
| Precision | ~0.83 |
| Recall | ~0.84 |
| F1-Score | ~0.83 |

✅ **Gradient Boosting provided the best balanced performance**, making it suitable for income classification tasks.

---

## 📊 Dataset Information

### Source
- UCI Adult Census Income Dataset

### Features
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

### Target Variable
- Income **> 50K** or **≤ 50K**

---

## 🧠 Key Steps in Notebook

### Data Cleaning
- Handling missing values
- Removing extra whitespaces in categorical features

### Exploratory Data Analysis (EDA)
- Income distribution analysis
- Feature-wise comparisons (e.g., education vs income)

### Feature Engineering
- Label Encoding for categorical variables
- Feature scaling using **StandardScaler**

### Model Training & Evaluation
- Trained and evaluated **7+ ML algorithms**
- Used accuracy, precision, recall, and F1-score

### Deployment
- Trained model integrated into a **Streamlit web application**

---

## 📁 Repository Structure


---

## 🏗 How to Run Locally

### 1️⃣ Run Notebook (Model Training)
- Open `Income_Prediction.ipynb` in **Google Colab**
- Execute cells sequentially:
  - Data loading
  - Preprocessing
  - Model training & evaluation

### 2️⃣ Run Streamlit App

```bash
pip install -r requirements.txt
streamlit run app.py
