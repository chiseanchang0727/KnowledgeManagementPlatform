import os
import streamlit as st
from app.utils.data_loader import read_txt
import streamlit_nested_layout
import json

def read_json(file_path):
    """
    Reads and returns JSON data from a file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        dict: JSON data containing title and summary
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def display_text_summary_interactive(file_path):
    """
    Displays the title of the article and its summary from JSON data.

    Args:
        file_path (str): The path to the JSON file containing the news data.
    """
    try:
        if not os.path.exists(file_path):
            st.error(f"The file '{file_path}' does not exist.")
            return

        # Read JSON data
        data = read_json(file_path)
        
        # Display title with custom styling
        title_html = f"""
        <h2 style="font-size: 24px; font-weight: bold; color: #333;">
            {data['title']}
        </h2>
        """
        st.markdown(title_html, unsafe_allow_html=True)

        # Display summary in expander
        with st.expander("點擊顯示重點資訊"):
            st.write(data['summary'])

    except json.JSONDecodeError:
        st.error(f"Error decoding JSON from file: {file_path}")
    except KeyError as e:
        st.error(f"Missing required field in JSON data: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
