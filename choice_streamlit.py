import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import openpyxl

# Load your model from the specified path
model_path = "artifacts/model_trainer/model.joblib"
model = joblib.load(model_path)

# Configure page settings
st.set_page_config(page_title="Wine Quality Classification", page_icon="🍷")

# Display a title and description using Markdown
st.title("Classification of Wine Quality")
st.markdown("Choose how you want to provide your input:")

# Load and display an image (optional)
image_path = 'static/assets/img/form-v9.jpg'
image = Image.open(image_path)
st.image(image, caption='Visual Representation of Wine Quality', use_container_width=True)

# Selection: Manual or File Upload
option = st.radio(
    "Select input method:",
    ("Enter details manually", "Upload Excel file"),
    index=0
)

if option == "Enter details manually":
    st.markdown("### Enter Wine Details")

    # Two-column layout for better UX
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
        density = st.number_input("Density", format="%.2f")
        pH = st.number_input("pH", format="%.2f")
        sulphates = st.number_input("Sulphates", format="%.2f")
        alcohol = st.number_input("Alcohol", format="%.2f")

    if st.button('Predict', key='manual_predict'):
        # Organize input features into an array
        input_features = np.array([
            [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
             free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
        ])
        prediction = model.predict(input_features)
        st.success(f'Prediction: {prediction[0]}')

elif option == "Upload Excel file":
    st.markdown("### Upload Your Excel File")
    uploaded_file = st.file_uploader("Choose an Excel file...", type=["xlsx"])
    if uploaded_file is not None:
        data = pd.read_excel(uploaded_file, engine='openpyxl')
        st.dataframe(data)
        if st.button('Predict', key='file_predict'):
            predictions = model.predict(data)
            data['Prediction'] = predictions
            output = data[['Prediction', 'alcohol']] if 'alcohol' in data.columns else data[['Prediction']]
            output = output.sort_values(by=['Prediction', 'alcohol'], ascending=False) if 'alcohol' in output.columns else output
            st.write("Predictions:")
            st.dataframe(output)
