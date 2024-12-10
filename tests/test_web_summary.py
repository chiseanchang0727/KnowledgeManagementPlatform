import unittest
from llm.models.text_summary import get_web_summary

class TestUtils(unittest.TestCase):
    def test_llm(self):

        response = get_web_summary(url="https://udn.com/news/story/7252/8287961")


        print(f'response: {response}')



if __name__ == "__main__":
    unittest.main()