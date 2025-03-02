import streamlit as st
import pandas as pd
from PIL import Image
import joblib
import openpyxl

# Load your model from the specified path
model_path = "artifacts/model_trainer/model.joblib"
model = joblib.load(model_path)

# Configure page settings
st.set_page_config(page_title="Wine Quality Classification", page_icon="🍷")

# Display a title and description using Markdown
st.title("Classification of Wine Quality")
st.markdown("Upload your Excel file with input features to get the classification results.")

# Load and display an image (optional)
image_path = 'static/assets/img/form-v9.jpg'
image = Image.open(image_path)
st.image(image, caption='Visual Representation of Wine Quality', use_container_width=True)

# File uploader for Excel files
uploaded_file = st.file_uploader("Choose an Excel file...", type=["xlsx"])

if uploaded_file is not None:
    # Read the Excel file into a Pandas DataFrame
    data = pd.read_excel(uploaded_file, engine='openpyxl')

    # Display the DataFrame in the UI (optional)
    st.dataframe(data)

    # Button to trigger predictions
    if st.button('Predict'):
        # Ensure the data is in the correct format, preprocess if necessary
        # For example, if you need to select specific columns:
        # features = data[['column1', 'column2', ..., 'columnN']]

        # Predict using the model
        predictions = model.predict(data)  # Adjust if preprocessing is needed
        # Add predictions to the DataFrame
        data['Prediction'] = predictions
        predictions = data[['Prediction', 'alcohol']]
        predictions = predictions.sort_values(by=['Prediction', 'alcohol'], ascending=False)

        # Display the DataFrame with the predictions in the UI
        st.write("Predictions:")
        st.dataframe(predictions)  # Show the DataFrame with the predictions
