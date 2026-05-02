import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Smart Medical Chatbot")

st.title("🩺 Smart Medical Analysis Chatbot")

df = pd.read_csv("Training.csv")

# Remove unwanted column
if "Unnamed: 133" in df.columns:
    df = df.drop(columns=["Unnamed: 133"])

# Encode Disease Column
le = LabelEncoder()
df["prognosis"] = le.fit_transform(df["prognosis"])

precautions = pd.read_csv("symptom_precaution.csv")

# Keep only required precaution columns
precautions = precautions.drop(
    columns=["Precaution_3", "Precaution_4"],
    errors="ignore"
)

selected_columns = [
    'itching',
    'shivering',
    'acidity',
    'stomach_pain',
    'vomiting',
    'fatigue',
    'joint_pain',
    'high_fever',
    'dehydration',
    'headache',
    'cough',
    'prognosis'
]

df_filtered = df[selected_columns]

X_filtered = df_filtered.drop("prognosis", axis=1)
y_filtered = df_filtered["prognosis"]

model = DecisionTreeClassifier()
model.fit(X_filtered, y_filtered)

st.success("✅ AI Model Loaded Successfully")

st.subheader("Select Your Symptoms")

user_input = {}

for symptom in X_filtered.columns:
    user_input[symptom] = st.selectbox(
        symptom.replace("_", " ").title(),
        ["No", "Yes"]
    )

# Convert to ML format
input_data = pd.DataFrame([{
    k: 1 if v == "Yes" else 0 for k, v in user_input.items()
}])

# PREDICTION BUTTON
if st.button("Predict Disease"):

    prediction_code = model.predict(input_data)[0]
    predicted_disease = le.inverse_transform([prediction_code])[0]

    st.success(f"✅ Possible Disease: {predicted_disease}")

    # FETCH PRECAUTIONS
    precaution_info = precautions[
        precautions["Disease"] == predicted_disease
    ]

    st.subheader("💊 Suggested Precautions")

    if not precaution_info.empty:
        st.write("✔", precaution_info["Precaution_1"].values[0])
        st.write("✔", precaution_info["Precaution_2"].values[0])
    else:
        st.warning("No precautions available.")

    st.info("⚠️ This is AI prediction only. Please consult a doctor.")