import unittest
import os
from llm.applications.text_summary import get_text_summary
from config.configs import Configs

class TestUtils(unittest.TestCase):
    def test_llm(self):
        file_path = './data/text_data/paper_price.txt'

        summary = get_text_summary(file_path)


        print(f'summary: {summary}')



if __name__ == "__main__":
    unittest.main()