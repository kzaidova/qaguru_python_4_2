from selene.support.shared import browser
from selene import be, have


def test_positive_case(open_and_close_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_case(open_and_close_browser):
    text = 'jvhkbjlknlkljvkhcjgxhfcgjhvkjblhkjlhjkhcjgxfhgfchgjvhbjkn'
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    browser.element('[id="topstuff"]').should(have.text(('По запросу ' + (text) + ' ничего не найдено.')))
