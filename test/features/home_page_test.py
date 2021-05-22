import unittest, os
from splinter import Browser

FLASK_ENV='test'
browser = Browser(headless=True)

class HomePageTest(unittest.TestCase):
    def test_title(self):
        browser.visit('http://localhost:5000')
        assert browser.is_text_present('Rock Paper Scissors Lizard Spock')

    def test_entering_name(self):
        browser = Browser(headless=True)
        browser.visit('http://localhost:5000')
        browser.fill('name', 'test name')
        button = browser.find_by_name('play')
        button.click()
        assert browser.is_text_present('Welcome test name!')

if __name__ == '__main__':
    unittest.main()