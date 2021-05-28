import pytest, random
from splinter import Browser
from doubles import allow

FLASK_ENV='test'

def test_seeing_choices():
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

@pytest.mark.skip(reason='interface not yet built')
def test_player_can_win():
    browser = Browser(headless=True)
    random.seed(0)

    browser.visit('http://localhost:5000')

    browser.fill('name', 'Player')
    button = browser.find_by_name('play')
    button.click()

    button = browser.find_by_css('#rock')
    button.click()

    assert browser.is_text_present('Rock crushes Lizard - Player wins')

    browser.quit()

if __name__ == '__main__':
   pytest.main()
