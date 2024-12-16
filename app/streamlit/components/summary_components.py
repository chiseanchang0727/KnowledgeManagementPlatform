import os
import streamlit as st
from app.utils.data_loader import read_txt

def display_text_summary_interactive(file_path):
    """
    Displays the title of the article and generates a summary based on user interaction.

    Args:
        file_path (str): The path to the text file containing the news data.
    """
    try:
        if not os.path.exists(file_path):
            st.error(f"The file '{file_path}' does not exist.")
            return

        article_title = """
        <h2 style="font-size: 24px; font-weight: bold; color: #333;">
            造紙行業因成本壓力與需求回升掀起新一輪漲價潮，主要紙企紛紛上調價格並進行停機檢修以促進盈利修復。
        </h2>
        """
        st.markdown(article_title, unsafe_allow_html=True)

        with st.expander("點擊顯示重點資訊"):
            text = read_txt(file_path)

            # Display the summary
            st.write(text)

    except Exception as e:
        st.error(f"An error occurred: {e}")

