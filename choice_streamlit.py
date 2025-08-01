import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import openpyxl
import base64

# ---------- 1. Set Beautiful Background with Overlay ----------

def set_bg(image_path, opacity=0.65):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    page_bg = f"""
    <style>
    body {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
    }}
    [data-testid="stAppViewContainer"] > .main {{
        background: rgba(255,255,255,{opacity}) !important;
        backdrop-filter: blur(0.5px);
    }}
    #MainMenu, footer {{visibility: hidden;}}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)
set_bg("beauty.jpg", opacity=0.70)

st.set_page_config(page_title="🍷 Wine Quality Classifier", page_icon="🍷", layout="wide")  # ← FIRST Streamlit command
def set_bg(image_path, opacity=0.65):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    page_bg = f"""
    <style>
    body {{
        background-image: url("data:beauty.jpg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
    }}
    [data-testid="stAppViewContainer"] > .main {{
        background: rgba(255,255,255,{opacity}) !important;
        backdrop-filter: blur(0.5px);
    }}
    #MainMenu, footer {{visibility: hidden;}}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

set_bg("beauty.jpg", opacity=0.70)

# ---------- 2. Page Setup & Header ----------

st.markdown("""
    <div style='
        background: rgba(255,255,255,0.8);
        border-radius: 20px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.13);
        margin-bottom: 2rem;
        padding: 2rem 2rem 1rem 2rem;
        '>
        <h1 style='text-align:center; color:#730800; font-size:2.6rem;'>🍷 Wine Quality Classifier</h1>
        <p style='text-align:center; font-size:1.18rem; color:#222;'>
            Taste the future: Instantly predict wine quality!<br>
            Choose an option below to get started.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- 3. Model ----------
model_path = "artifacts/model_trainer/model.joblib"
model = joblib.load(model_path)

# ---------- 4. Input Cards ----------
card_style = """
    background: rgba(255,255,255,0.9);
    border-radius: 18px;
    box-shadow: 0 3px 12px rgba(140,16,24,0.11);
    padding: 2rem 1.3rem 1.3rem 1.3rem;
    margin: 1.5rem 0;
"""

option = st.selectbox(
    "How do you want to provide input?",
    options=["Enter details manually", "Upload Excel file"],
    index=0,
    key='input_choice'
)

if option == "Enter details manually":
    st.markdown(f"<div style='{card_style}'>", unsafe_allow_html=True)
    st.subheader("🍇 Enter Wine Details")

    left_column, right_column = st.columns(2)
    with left_column:
        fixed_acidity = st.number_input("Fixed Acidity", format="%.2f")
        volatile_acidity = st.number_input("Volatile Acidity", format="%.2f")
        citric_acid = st.number_input("Citric Acid", format="%.2f")
        residual_sugar = st.number_input("Residual Sugar", format="%.2f")
        chlorides = st.number_input("Chlorides", format="%.2f")
        free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", format="%.2f")
        total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", format="%.2f")
    with right_column:
        density = st.number_input("Density", format="%.4f")
        pH = st.number_input("pH", format="%.2f")
        sulphates = st.number_input("Sulphates", format="%.2f")
        alcohol = st.number_input("Alcohol", format="%.2f")

    predict_btn = st.button('🔮 Predict Wine Quality', key='manual_predict', use_container_width=True)

    if predict_btn:
        input_features = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                                    free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
        prediction = model.predict(input_features)
        st.success(f"🍷 **Predicted Wine Quality:** {prediction[0]}")
    st.markdown("</div>", unsafe_allow_html=True)

elif option == "Upload Excel file":
    st.markdown(f"<div style='{card_style}'>", unsafe_allow_html=True)
    st.subheader("📄 Upload Your Excel File")
    uploaded_file = st.file_uploader("Choose an Excel file...", type=["xlsx"])
    if uploaded_file is not None:
        data = pd.read_excel(uploaded_file, engine='openpyxl')
        st.dataframe(data, use_container_width=True)
        file_predict_btn = st.button('🔮 Predict for All Rows', key='file_predict', use_container_width=True)
        if file_predict_btn:
            predictions = model.predict(data)
            data['Prediction'] = predictions
            output = data[['Prediction', 'alcohol']] if 'alcohol' in data.columns else data[['Prediction']]
            output = output.sort_values(by=['Prediction', 'alcohol'], ascending=False) if 'alcohol' in output.columns else output
            st.success("🍷 **Predictions completed!**")
            st.dataframe(output, use_container_width=True)
            # Download option
            csv = output.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download Results as CSV",
                data=csv,
                file_name="wine_predictions.csv",
                mime="text/csv",
                use_container_width=True
            )
    st.markdown("</div>", unsafe_allow_html=True)

# --- Optional: Footer ---
st.markdown("""
<div style='text-align:center; font-size:0.95rem; color:#888; margin-top:2rem;'>
    &copy; 2025 Your Company | Enjoy responsibly 🍇
</div>
""", unsafe_allow_html=True)
