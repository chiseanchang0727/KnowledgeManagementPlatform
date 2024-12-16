import os
import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader  # Make sure PyPDF2 is installed: pip install PyPDF2
from app.config.upload_config import UploadConfig
from app.config.enums import InputFileType

def upload_file(config: UploadConfig):
    accepted_types = [item.value for item in InputFileType]
    uploaded_file = st.file_uploader("Choose a file", type=accepted_types)
    
    if uploaded_file is not None:
        file_name = uploaded_file.name.lower()

        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            # call a bot to show summary

        elif file_name.endswith(".txt"):
            content = uploaded_file.read().decode("utf-8", errors="replace")
            st.write("Here’s the content of your text file:")
            # call a bot to show summary
        
        elif file_name.endswith(".pdf"):
            reader = PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            # call a bot to show summary


        # Save the file when the button is clicked
        if st.button(f"Save {uploaded_file.name} to directory"):
            path = config.dir
            save_path = save_uploaded_file(uploaded_file, path)
            st.success(f"File saved successfully to: {save_path}")
    

def save_uploaded_file(uploaded_file, path):
    """Saves the uploaded file to the specified directory."""
    try:
        if not os.path.exists(path):
            os.makedirs(path)

        save_path = os.path.join(path, uploaded_file.name)
        
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return save_path 
    
    except Exception as e:
        # Handle any exceptions that may occur during the saving process
        st.error(f"An error occurred while saving the file: {str(e)}")
        return None
