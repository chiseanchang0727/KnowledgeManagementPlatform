import streamlit as st
from app.components.historical_pulp_futrues_plot import historcial_pul_future

# Set layout to wide
st.set_page_config(
    layout="wide"
)


theme1 = 'Pulp Futures: Historcial Data and Prediction'
theme2 = 'News Summary'

# Sidebar content
with st.sidebar:
    st.title("Domain Info Management")
    # st.write("Bleached Pulp Futures and Prediction")
    # st.write("News Summary by AI")

    # Create navigation options
    page = st.radio(
        "Theme",  # Label for the radio button
        [theme1, theme2],  # Options for navigation
        index=0  # Default selection
    )


st.title("Bleached Softwood Kraft Pulp Futures")

# tab1, tab2 = st.tabs(['Historcial Data', 'Prediction'])
# with tab1:
#     with st.container():    
#         st.header("Historical Data")
#         historcial_pul_future()
# with tab2:
#     with st.container():
#         st.header('Future Pulp Value Predcition')


if page == theme1:
    with st.container():    
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
        st.header('News Summary')