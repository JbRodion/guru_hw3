import pytest
from selene import browser

@pytest.fixture(scope="session")
def conf_browser():
    browser.config.window_size = (1920,1080)
    yield
    browser.quit()

@pytest.fixture(scope="function")
def url_browser(conf_browser):
    browser.open('https://duckduckgo.com')



