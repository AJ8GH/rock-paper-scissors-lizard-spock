import unittest
from splinter import Browser

FLASK_ENV='test'

class HomePageTest(unittest.TestCase):
    def test_seeing_choices(self):
        browser = Browser(headless=True)

        browser.visit('http://localhost:5000')
        button = browser.find_by_name('play')
        button.click()

        assert browser.is_element_present_by_tag('img')
        assert browser.is_element_present_by_css('#rock')
        assert browser.is_element_present_by_css('#paper')
        assert browser.is_element_present_by_css('#scissors')
        assert browser.is_element_present_by_css('#lizard')
        assert browser.is_element_present_by_css('#spock')

        browser.quit()

if __name__ == '__main__':
    unittest.main()
