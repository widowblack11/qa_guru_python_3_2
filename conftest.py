import pytest
from selene.support.shared import browser


@pytest.fixture
def open_browser():
    browser.config.window_height = 1920
    browser.config._window_width = 1080
    browser.open('https://google.com')
    print("Открыт браузер заданного размера")
    yield
    browser.quit()
    print("Браузер закрыт")
