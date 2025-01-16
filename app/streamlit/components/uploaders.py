import os
import streamlit as st
import json
from app.config.upload_config import UploadConfig
from app.config.enums import InputFileType
from app.streamlit.components.upload_file_summary import file_summary

def upload_file(config: UploadConfig):
    accepted_types = [item.value for item in InputFileType]
    uploaded_file = st.file_uploader("Choose a file", type=accepted_types)
    
    if uploaded_file is not None:
        file_name = uploaded_file.name.lower()

        if st.button(f"Save {uploaded_file.name} to directory"):
            path = config.upload_dir
            save_path = save_uploaded_file(uploaded_file, path)
            st.success(f"File saved successfully to: {save_path}")

        if 'summary_result' not in st.session_state:
            st.session_state.summary_result = None
            st.session_state.summary_title = None


        # if file_name.endswith(".pdf"):
        if st.button(f"Generate {uploaded_file.name} summary"):
            with st.spinner('Generating Summary...'): 
                st.session_state.summary_result, st.session_state.summary_title = file_summary(os.path.join(config.upload_dir, file_name))

        if st.session_state.summary_result:
            st.write("**Summary Result:**")
            st.write(st.session_state.summary_result)
        
            if st.button("Save summary"):
                summary_file_name = f"{os.path.splitext(uploaded_file.name)[0]}_summary.txt"
                save_path = save_summary(st.session_state.summary_result, st.session_state.summary_title, summary_file_name, config.summary_dir)

                if save_path:
                    st.success(f"Summary saved successfully to: {save_path}")
                    st.session_state.summary_result = None
                    st.session_state.summary_title = None

        # elif file_name.endswith(".txt"):
        #     text = uploaded_file.read().decode("utf-8", errors="replace")

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

def save_summary(summary_text, title, file_name, path):
    """Saves the generated summary text to the specified directory."""

    try:
        if not os.path.exists(path):
            os.makedirs(path)

        result = {
            'title': title,
            'summary': summary_text  
        }
        save_path = os.path.join(path, file_name)
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        
        return save_path
    except Exception as e:
        st.error(f"An error occurred while saving the summary: {str(e)}")
        return None