import streamlit as st
import numpy as np
import joblib
from PIL import Image

# Load your model from the specified path
model_path = "artifacts/model_trainer/model.joblib"
model = joblib.load(model_path)

# Configure page settings
st.set_page_config(page_title="Wine Quality Classification", page_icon="🍷")

# Display a title and description using Markdown
st.title("Classification of Wine Quality")
st.markdown("Enter the input features and get the classification results.")

# Load and display an image
image_path = 'static/assets/img/form-v9.jpg'
image = Image.open(image_path)
st.image(image, caption='Visual Representation of Wine Quality', use_container_width=True)

# Create input sections with a two-column layout
left_column, right_column = st.columns(2)

# Define inputs for the left column
with left_column:
    fixed_acidity = st.number_input("Fixed Acidity", format="%.2f")
    volatile_acidity = st.number_input("Volatile Acidity", format="%.2f")
    citric_acid = st.number_input("Citric Acid", format="%.2f")
    residual_sugar = st.number_input("Residual Sugar", format="%.2f")
    chlorides = st.number_input("Chlorides", format="%.2f")
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", format="%.2f")
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", format="%.2f")

# Define inputs for the right column
with right_column:
    density = st.number_input("Density", format="%.2f")
    pH = st.number_input("pH", format="%.2f")
    sulphates = st.number_input("Sulphates", format="%.2f")
    alcohol = st.number_input("Alcohol", format="%.2f")

# Action button for prediction
if st.button('Predict'):
    # Organize input features into an array
    input_features = np.array([
        [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
         free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
    ])
    # Generate prediction
    prediction = model.predict(input_features)
    # Display the result
    st.success(f'Prediction: {prediction[0]}')  # Assuming the prediction is a single value
