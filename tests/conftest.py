from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://github.com/'