"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser
from selene.support.shared.jquery_style import s

@pytest.fixture(scope="function")
def size_browser(request):
    resolutions = {
        "desktop": (1920, 1080),
        "mobile": (428, 926)
    }
    return resolutions[request.param]

@pytest.mark.parametrize("size_browser", ["desktop"], indirect=True)
def test_desktop(size_browser):
    browser.driver.set_window_size(*size_browser)
    s('.HeaderMenu-link--sign-in').click()

@pytest.mark.parametrize("size_browser", ["mobile"], indirect=True)
def test_mobile(size_browser):
    browser.driver.set_window_size(*size_browser)
    s('.flex-column [aria-label="Toggle navigation"]').click()






