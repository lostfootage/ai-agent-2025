# frontend_app.py

pip install streamlit


"""
Streamlit Frontend for AI Pharmacy Script Reader
Author: Kimberly Navarrete
"""

import streamlit as st
import requests

st.title("🩺 AI Pharmacy Script Reader")

st.write("Upload a prescription file and select the extraction method:")

uploaded_file = st.file_uploader("Choose a file (.png, .jpg, .txt)", type=["png", "jpg", "jpeg", "txt"])
method = st.selectbox("Extraction Method", ["simple", "huggingface"])

if uploaded_file is not None:
    if st.button("Extract Prescription Info"):
        with st.spinner('Extracting...'):
            files = {"file": uploaded_file.getvalue()}
            data = {"method": method}
            response = requests.post("http://127.0.0.1:8000/upload/", files={"file": (uploaded_file.name, uploaded_file)}, data=data)

            if response.status_code == 200:
                result = response.json()["extracted_data"]
                st.success("Extraction Successful!")
                st.json(result)
            else:
                st.error("Error: " + str(response.content))

streamlit run frontend_app.py
