import unittest
from splinter import Browser

class HomePageTest(unittest.TestCase):
    def test_title(self):
        browser = Browser()
        browser.visit('http://localhost:5000')
        assert browser.is_text_present('Rock Paper Scissors Lizard Spock')

if __name__ == '__main__':
    unittest.main()
