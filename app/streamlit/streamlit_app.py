import streamlit as st
import os
from dotenv import load_dotenv
from utils.helpers import YamlLoader
from app.streamlit.components.historical_pulp_futrues_plot import historcial_pul_future
from app.streamlit.components.summary_components import display_text_summary_interactive
from app.streamlit.components.uploaders import upload_file
# Set layout to wide
st.set_page_config(
    layout="wide"
)

load_dotenv()
conifg_loader = YamlLoader(file_path=os.environ["CONFIGS"])
upload_config = conifg_loader.get_upload_config()



theme1 = 'Pulp Futures: Historcial Data and Prediction'
theme2 = 'Domain Information'
theme3 = "Upload files"
# Sidebar content
with st.sidebar:
    st.title("Domain Info Management")
    # st.write("Bleached Pulp Futures and Prediction")
    # st.write("News Summary by AI")

    # Create navigation options
    page = st.radio(
        "Theme",  # Label for the radio button
        [theme2, theme3],  # Options for navigation
        index=0  # Default selection
    )

if page == theme1:
    with st.container():    
        st.title("Bleached Softwood Kraft Pulp Futures")
        tab1, tab2 = st.tabs(['Historcial Data', 'Prediction'])
        with tab1:
            with st.container():    
                st.header("Historical Data")
                historcial_pul_future()
        with tab2:
            with st.container():
                st.header('Future Pulp Value Predcition')

elif page == theme2:
    with st.container():
        st.title("文件摘要")
        
        # Get all files from the directory
        summary_dir = './data/summaried_data/'
        try:
            files = [f for f in os.listdir(summary_dir) if f.endswith('.txt')]
                            
            
            # Create sections for each file
            for file_name in files:
                with st.expander(f"📄 {file_name}"):
                    file_path = os.path.join(summary_dir, file_name)
                    display_text_summary_interactive(file_path)
                    
        except FileNotFoundError:
            st.error(f"Directory not found: {summary_dir}")
        except Exception as e:
            st.error(f"Error accessing files: {str(e)}")

elif page == theme3:
    with st.container():
        st.title("上傳資料")
        upload_file(config=upload_config)
