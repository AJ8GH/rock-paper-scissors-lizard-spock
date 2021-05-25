import pytest
from splinter import Browser

FLASK_ENV='test'

def test_title():
    browser = Browser(headless=True)

    browser.visit('http://localhost:5000')

    assert browser.is_text_present('Rock Paper Scissors Lizard Spock')

    browser.quit()

def test_entering_name():
    browser = Browser(headless=True)

    browser.visit('http://localhost:5000')
    browser.fill('name', 'test name')
    button = browser.find_by_name('play')
    button.click()

    assert browser.is_text_present('Welcome test name!')

    browser.quit()

if __name__ == '__main__':
    pytest.main()
