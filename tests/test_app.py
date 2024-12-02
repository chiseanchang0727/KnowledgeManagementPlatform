import unittest
from dotenv import load_dotenv
import unittest.test
from app.utils.data_loader import load_csv
from app.utils.plot_helper import plot_data
from app.utils.base import get_historical_files_path
import pandas as pd



class TestUtils(unittest.TestCase):
    load_dotenv()
    def test_load_data(self):
        data = load_csv(get_historical_files_path('Bleached Softwood Kraft Pulp Futures Historical Data.csv'))
        self.assertIsInstance(data, pd.DataFrame)

    def test_plot_data(self):
        # Test with sample data
        data = pd.DataFrame({
            "X": [1, 2, 3],
            "Y": [4, 5, 6]
        })
        try:
            plot_data(data, "X", "Y")
        except Exception as e:
            self.fail(f"plot_data raised an exception {e}")






if __name__ == '__main__':
    unittest.main()