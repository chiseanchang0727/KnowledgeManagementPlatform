import os
import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from app.config.upload_config import UploadConfig
from app.config.enums import InputFileType
from app.streamlit.components.upload_file_summary import file_summary

def upload_file(config: UploadConfig):
    accepted_types = [item.value for item in InputFileType]
    uploaded_file = st.file_uploader("Choose a file", type=accepted_types)
    
    if uploaded_file is not None:
        file_name = uploaded_file.name.lower()

        if st.button(f"Save {uploaded_file.name} to directory"):
            path = config.dir
            save_path = save_uploaded_file(uploaded_file, path)
            st.success(f"File saved successfully to: {save_path}")
    

        if file_name.endswith(".pdf"):

            if st.button(f"Generate {uploaded_file.name} summary"):
                summary_result = file_summary(os.path.join(config.dir, file_name))
                st.write("**Summary Result:**")
                st.write(summary_result)

                if summary_result:
                    if st.button("Save summary"):
                        summary_file_name = f"{os.path.splitext(uploaded_file.name)[0]}_summary.txt"
                        save_path = save_summary(summary_result, summary_file_name, config.dir)
                        if save_path:
                            st.success(f"Summary saved successfully to: {save_path}")
                    else:
                        st.warning("No summary to save.")     

        elif file_name.endswith(".txt"):
            text = uploaded_file.read().decode("utf-8", errors="replace")
        



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

def save_summary(summary_text, file_name, path):
    """Saves the generated summary text to the specified directory."""
    try:
        if not os.path.exists(path):
            os.makedirs(path)

        save_path = os.path.join(path, file_name)
        
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(summary_text)
        
        return save_path
    except Exception as e:
        st.error(f"An error occurred while saving the summary: {str(e)}")
        return None