import streamlit as st
import pandas as pd
import joblib

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="MoneyLens",
    page_icon="💰",
    layout="wide"
)

# ================= LOAD MODEL =================
model = joblib.load("model/xgb_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# ================= CUSTOM CSS =================
st.markdown("""
<style>
.card {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
.title {
    font-size: 48px;
    font-weight: 700;
    color: #22c55e;
}
.subtitle {
    color: #9ca3af;
    font-size: 18px;
    margin-bottom: 30px;
}
.result-high {
    background: linear-gradient(135deg, #16a34a, #22c55e);
    padding: 25px;
    border-radius: 16px;
    color: white;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
}
.result-low {
    background: linear-gradient(135deg, #dc2626, #ef4444);
    padding: 25px;
    border-radius: 16px;
    color: white;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## 💡💰MoneyLens")
    st.markdown("AI-powered Income Prediction")
    st.markdown("👩‍💻 Built by Riya")

# ================= LABEL ENCODER MAPS =================
workclass_map = {
    'Federal-gov': 0, 'Local-gov': 1, 'Never-worked': 2, 'Private': 3,
    'Self-emp-inc': 4, 'Self-emp-not-inc': 5, 'State-gov': 6, 'Without-pay': 7
}

education_map = {
    '10th': 0, '11th': 1, '12th': 2, '1st-4th': 3, '5th-6th': 4,
    '7th-8th': 5, '9th': 6, 'Assoc-acdm': 7, 'Assoc-voc': 8,
    'Bachelors': 9, 'Doctorate': 10, 'HS-grad': 11,
    'Masters': 12, 'Preschool': 13, 'Prof-school': 14, 'Some-college': 15
}

marital_map = {
    'Divorced': 0, 'Married-AF-spouse': 1, 'Married-civ-spouse': 2,
    'Married-spouse-absent': 3, 'Never-married': 4,
    'Separated': 5, 'Widowed': 6
}

occupation_map = {
    'Adm-clerical': 0, 'Armed-Forces': 1, 'Craft-repair': 2,
    'Exec-managerial': 3, 'Farming-fishing': 4, 'Handlers-cleaners': 5,
    'Machine-op-inspct': 6, 'Other-service': 7, 'Priv-house-serv': 8,
    'Prof-specialty': 9, 'Protective-serv': 10, 'Sales': 11,
    'Tech-support': 12, 'Transport-moving': 13
}

relationship_map = {
    'Husband': 0, 'Not-in-family': 1, 'Other-relative': 2,
    'Own-child': 3, 'Unmarried': 4, 'Wife': 5
}

race_map = {
    'Amer-Indian-Eskimo': 0, 'Asian-Pac-Islander': 1,
    'Black': 2, 'Other': 3, 'White': 4
}

sex_map = {'Female': 0, 'Male': 1}

country_map = {
    'United-States': 39, 'India': 18, 'Mexico': 25, 'Philippines': 30,
    'Germany': 11, 'Canada': 3, 'England': 8, 'Japan': 19,
    'China': 4, 'Iran': 20, 'Italy': 21
}

# ================= LAYOUT =================
col1, col2 = st.columns([2, 1])

# ================= INPUTS =================
with col1:
    st.markdown("<div class='title'>MoneyLens 💰</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Predict income category using Machine Learning</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    age = st.slider("Age", 18, 90, 30)
    education_num = st.slider("Education Number (1–16)", 1, 16, 10)
    hours_per_week = st.slider("Hours per Week", 1, 100, 40)

    workclass = st.selectbox("Workclass", list(workclass_map.keys()))
    education = st.selectbox("Education", list(education_map.keys()))
    marital_status = st.selectbox("Marital Status", list(marital_map.keys()))
    occupation = st.selectbox("Occupation", list(occupation_map.keys()))
    relationship = st.selectbox("Relationship", list(relationship_map.keys()))
    race = st.selectbox("Race", list(race_map.keys()))
    sex = st.selectbox("Sex", list(sex_map.keys()))
    native_country = st.selectbox("Native Country", list(country_map.keys()))

    capital_gain = st.number_input("Capital Gain", 0, 100000, 0)
    capital_loss = st.number_input("Capital Loss", 0, 5000, 0)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= PREDICTION =================
# ================= PREDICTION =================
with col2:
    st.markdown("### 📊 Prediction Result")

    predict_btn = st.button("🚀 Predict Income")

    if predict_btn:
        input_df = pd.DataFrame([{
            "age": age,
            "workclass": workclass_map[workclass],
            "education": education_map[education],
            "education.num": education_num,
            "marital.status": marital_map[marital_status],
            "occupation": occupation_map[occupation],
            "relationship": relationship_map[relationship],
            "race": race_map[race],
            "sex": sex_map[sex],
            "capital.gain": capital_gain,
            "capital.loss": capital_loss,
            "hours.per.week": hours_per_week,
            "native.country": country_map[native_country]
        }])

        num_cols = [
            "age",
            "education.num",
            "capital.gain",
            "capital.loss",
            "hours.per.week"
        ]

        input_df[num_cols] = scaler.transform(input_df[num_cols])

        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.markdown(
                "<div class='result-high'>💸 Income > 50K</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-low'>📉 Income ≤ 50K</div>",
                unsafe_allow_html=True
            )
    else:
        st.info("Click **Predict Income** to see the result")
