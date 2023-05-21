"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser
from selene.support.shared.jquery_style import s


@pytest.mark.parametrize("permision_w", [
    (1920, 1080),
    (1600, 900),
    (1600, 1024),
    (1280, 720),
], ids=["1920, 108",
        "1600, 900",
        "1600, 1024",
        "1280, 720"])
def test_github_desktop(permision_w):
    browser.driver.set_window_size(permision_w[0], permision_w[1])
    browser.open('https://github.com/')
    s('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize("permision_m", [
    (428, 926),
    (372, 812),
    (414, 896),
    (414, 736),
], ids=["428, 926",
        "372, 812",
        "414, 896",
        "414, 736"])
def test_github_mobile(permision_m):
    browser.driver.set_window_size(permision_m[0], permision_m[1])
    browser.open('https://github.com/')
    s('.flex-column [aria-label="Toggle navigation"]').click()


