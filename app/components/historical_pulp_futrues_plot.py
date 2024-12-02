import re
import streamlit as st
import pandas as pd
from app.utils.data_loader import load_csv
from app.utils.plot_helper import plot_data
from config import get_historical_files_path

from streamlit_date_picker import date_range_picker, date_picker, PickerType

def data_preprocessing(raw_data):
    data = raw_data.copy()

    data['Date'] = pd.to_datetime(data['Date'])
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month
    data['Day'] = data['Date'].dt.day

    data['Price'] = data['Price'].apply(lambda x: int(float(re.sub(',', '', x))))
    data['Open'] = data['Open'].apply(lambda x: int(float(re.sub(',', '', x))))
    data['High'] = data['High'].apply(lambda x: int(float(re.sub(',', '', x))))
    data['Low'] = data['Low'].apply(lambda x: int(float(re.sub(',', '', x))))
    data['Vol.'] = data['Vol.'].apply(lambda x: int(float(re.sub('K', '', x))*1000))

    return data


def historcial_pul_future():
    # Set up Streamlit
    try:
        file_path = get_historical_files_path('Bleached Softwood Kraft Pulp Futures Historical Data.csv')
        data = load_csv(file_path)  # Ensure `load_csv` is implemented to load CSVs from file paths
        data = data_preprocessing(data)
        if data is None or data.empty:
            st.error("Failed to load data or data is empty.")
            st.stop()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()


    #TODO: make several container with giant statistical number in it
    # Display a preview of the data
    st.write("Data Preview:")
    st.write(data.head())

    # Allow the user to select a date range
    _, col2, _ = st.columns(3)
    with col2:
        # st.write("Select Date Range:")
        available_dates = data[data['Year'] >= 2024]['Date'].tolist()
        min_date = min(available_dates)
        max_date = max(available_dates)

        data_range_string = date_range_picker(
            picker_type=PickerType.date,
            start=min_date,
            end=max_date,
            key='available_date_picker',
            available_dates=available_dates
        )
        start = data['Date'].max()
        end = data['Date'].min()
        if data_range_string:
            start, end = data_range_string
            # st.write(f"Date Range Picker [{start}, {end}]")


    # Filter data based on selected date range
    filtered_data = data[(data['Date'] >= start) & (data['Date'] <= end)]


    x_column = 'Date'
    fig1 = plot_data(filtered_data, x_column, 'Price', plot_type='line')
    if fig1:
        with st.container(height=450, border=False):

            st.pyplot(fig1)
    else:
        st.error("Failed to generate the plot. Please check your input.")
    fig2 = plot_data(filtered_data, x_column, 'Vol.', plot_type='bar')
    if fig2:
        with st.container(height=450, border=False):
            st.pyplot(fig2)
    else:
        st.error("Failed to generate the plot. Please check your input.")