import unittest
from unittest.mock import patch, MagicMock
from app.utils.data_loader import load_csv
from app.utils.plot_helper import plot_data
from config import get_historical_files_path
import pandas as pd
import streamlit as st
from app.components.historical_pulp_futrues_plot import historcial_pul_future 


class TestUtils(unittest.TestCase):
    def setUp(self):
        # Simulated data for testing
        self.mock_data = pd.DataFrame({
            "Date": pd.date_range(start="2022-01-01", periods=10, freq="D"),
            "Price": [100, 102, 104, 106, 108, 110, 112, 114, 116, 118]
        })

    @patch("your_module.load_csv")  # Mocking load_csv function
    @patch("your_module.get_historical_files_path")  # Mocking get_historical_files_path
    @patch("streamlit.slider")  # Mocking Streamlit slider
    @patch("streamlit.selectbox")  # Mocking Streamlit selectbox
    @patch("streamlit.button")  # Mocking Streamlit button
    @patch("streamlit.write")  # Mocking Streamlit write
    @patch("streamlit.pyplot")  # Mocking Streamlit pyplot
    def test_historical_pulp_future(self, mock_pyplot, mock_write, mock_button, mock_selectbox, mock_slider, mock_get_path, mock_load_csv):
        # Mock return values
        mock_get_path.return_value = "mock/path/to/data.csv"
        mock_load_csv.return_value = self.mock_data
        mock_slider.return_value = (pd.Timestamp("2022-01-01"), pd.Timestamp("2022-01-10"))
        mock_selectbox.side_effect = lambda label, options: options[0]  # Return the first option for any selectbox
        mock_button.return_value = True  # Simulate the button click

        historcial_pul_future()


        # Assertions
        mock_get_path.assert_called_once_with("Bleached Softwood Kraft Pulp Futures Historical Data.csv")
        mock_load_csv.assert_called_once()
        mock_slider.assert_called_once()
        mock_selectbox.assert_called()
        mock_button.assert_called_once()
        mock_pyplot.assert_called_once()  # Ensure a plot was generated
        mock_write.assert_called()  # Ensure data was written to the Streamlit interface


if __name__ == "__main__":
    unittest.main()
