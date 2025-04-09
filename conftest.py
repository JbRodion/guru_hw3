import pytest
from selene import browser

@pytest.fixture(scope="session")
def conf_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture(scope="session")
def url_browser():
    browser.open('https://duckduckgo.com/')

    yield
    browser.quit()

