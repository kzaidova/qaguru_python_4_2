from selene import browser
import pytest
@pytest.fixture
def open_and_close_browser():
    browser.config.window_height = 999
    browser.config.window_width = 999
    browser.open('https://google.com')
    print('я открыл браузер')
    yield browser
    browser.close()
    print('я закрыл браузер')




